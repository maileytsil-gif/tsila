# LOM Bridge 0.4.2 — écriture d'automation d'arrangement dans Ableton Live, pilotable par une IA ou un script

| Fichier | Rôle |
|---|---|
| `LOMBridge/__init__.py` | Remote Script Python (dans Live) : UDP 7421, API Live complète, plan et écriture d'automation |
| `lom.py` | Client Python 3 sans dépendance : CLI, `apply spec.json [--dry]`, serveur HTTP JSON |
| `automations_el21.json` | Spec d'exemple pour le morceau el21 |
| `tests/test_offline.py` | 24 tests logiciels sans Live (`python3 -W ignore -m unittest tests/test_offline.py`) |
| `tests/live_suite.py` | Suite d'essais dans Live sur deux pistes temporaires créées puis supprimées |
| `legacy/` | Ancien device Max for Live (protocole obsolète, sans automation) — non maintenu |

Contexte de développement : macOS 26.6, Live 12.4.5 Suite, Python embarqué de Live ; bibliothèque utilisateur de Live sur `/Volumes/Seagate Portable Drive/ableton /User Library/`.

## Installation
1. Copier `LOMBridge/` dans `User Library/Remote Scripts/` (Live ne lit ce dossier qu'au lancement).
2. Relancer Live → Réglages → Link, Tempo & MIDI → Surface de contrôle : **LOMBridge** (entrée/sortie : Aucune).
3. Le bridge écrit `~/Library/Application Support/LOMBridge/connection.json` (0600) : `port`, `token`, `session`, `version`. `python3 lom.py ping` doit répondre `pong 0.4.2 … session <n>`.
4. Après modification du script : `python3 lom.py reload`. Attention : à chaque **chargement de Set**, Live réinstancie la surface de contrôle avec le module importé au **démarrage** de Live ; un rechargement à chaud est perdu jusqu'au redémarrage (le fichier sur disque fait foi).

## Protocole (OSC sur UDP 127.0.0.1:7421)
- Chaque commande se termine par deux arguments : `!<token>` puis `#<id de requête>`.
- Réponses, l'id de requête étant **toujours le premier argument** : `/begin <id> <cmd>` · `/r <id> …` (0 à n lignes ; certaines commencent par `warn`, `error`, `plan`, `clip`, `rebuilt`) · `/err <id> <texte>` · `/end <id> <cmd>`. Réponses envoyées à l'adresse de l'expéditeur. Le client ne garde que les lignes portant son id.
- **Références d'objets** : chaînes opaques `o:<session>:<n>`, jamais des nombres. Une référence d'une autre session est refusée (`/ping` donne la session courante). Les entiers hors int32 passent en int64 OSC (`h`) sans arrondi.
- Temps : noires absolues depuis 1|1 (le client accepte `17|1`, `17|3.5`, `5|2|3`, 4/4 par défaut).
- Résolution des noms : exacte, sinon sous-chaîne **unique** ; toute ambiguïté est refusée avec la liste des candidats.

| Commande | Effet |
|---|---|
| `/ping` | version, version Live, session |
| `/track <nom\|ref>` → `ref nom` | |
| `/param <piste> <device\|mixer\|ref> <param\|ref>` → `ref nom min max valeur affichage quantifié état_automation` | `mixer` : `Volume`, `Pan`, `Send A`… |
| `/params <deviceRef> [filtre]`, `/solve <paramRef> <valeur affichée>` → `raw affichage saturé` | |
| `/clips <piste>` → `ref début fin nom audio` | clips d'arrangement |
| `/plan <piste> <paramRef> <raw\|disp> <res> <courbe> <hold> <accept\|-> t0 v0 [t1 v1 …]` | **plan sans écriture** : valeurs résolues, clips concernés, extension `hold`, compatibilité, budget de points, échantillonnage estimé. Ligne `plan <json>` puis `clip …`, `warn …`, `error …`, et `ok`/`invalid` |
| `/shape` (mêmes arguments) | construit le **même plan**, refuse s'il a des erreurs, puis écrit (tâche asynchrone). Lignes `shape <clips> <points> <trou>`, `rebuilt <ref> <nom> <anciens pts>`, `warn …` |
| `/read <piste> <paramRef> <tA> <tB> <res>` | valeur réelle le long de la plage (curseur déplacé puis restauré ; transport arrêté ; res dans ]0, 64] ; ≤ 400 points) |
| `/events <piste> <paramRef> [tA tB]` | points des enveloppes **exposées** (voir limites) |
| `/clear <piste> <paramRef> <tA> <tB> <accept\|-> ` | supprime les points de la plage (reconstruction) |
| `/jobs`, `/cancel [<id>]` | tâches en file (max 4) ; annulation d'une tâche par id, ou de toutes |
| `/get /set /call /children /info /path` | accès générique au LOM (`live_set tracks 2 mixer_device volume`, références) |
| `/py <code>` | Python arbitraire dans Live — **UDP seulement, jamais via HTTP** |
| `/reload` | rechargement à chaud |

`accept` = liste séparée par des virgules de pertes ou approximations acceptées : `fades` (clip audio : fondus non recopiables), `expressions` (clip MIDI : expressions de notes/MPE non recopiables), `warp` (marqueurs de warp non reproductibles), `clamp` (valeurs hors plage saturées). Sans acceptation, le plan est **refusé**.

## Comment l'automation est écrite
Contraintes de l'API Live 12.4 constatées : une enveloppe ne se crée que sur un clip de **session** ; elle n'agit que dans l'étendue de **son** clip ; les clips d'arrangement n'exposent pas leurs enveloppes de façon fiable (jamais pour l'audio ; pour le MIDI seulement tant que le clip a été créé dans la session Live courante, plus après réouverture du Set).

Pour chaque clip d'arrangement couvrant la plage, `/shape` :
1. **Plan** (identique à `/plan`) : cibles, valeurs (`disp` résolues par dichotomie sur `str_for_value` et vérifiées), extension `hold` jusqu'à la fin du clip, contrôle de chaque clip (take lane, enregistrement, clip bouclé étiré, audio sans fichier = fatal ; audio/MIDI/warp = acceptation requise), budget de points calculé **avant** génération (≤ 4096), trous signalés. Fenêtre de durée nulle refusée (donner deux temps ou `hold=1`).
2. **Revalidation au démarrage effectif de la tâche** : clips toujours présents aux mêmes positions, paramètre existant, transport arrêté si un échantillonnage est nécessaire ; sinon refus (« replanifier »).
3. **Anciens points** du même paramètre hors fenêtre : exacts si le clip expose l'enveloppe ; sinon, si le paramètre est automatisé, **échantillonnage** par le curseur au pas de 1/8 de temps puis simplification (tolérance 0,0015 normalisé ; ≈ 0,1 s par 1/8 de temps hors fenêtre : 8 mesures ≈ 26 s). Deux **ancrages exactement** sur les bords portent l'ancienne valeur : hors fenêtre, l'automation est strictement identique (cas exposé) ou identique à 0,0015 près (cas échantillonné).
4. **Nouveaux points** : rampes linéaires par vrais points ; courbes (`exp`, `log`, `sc`, `sin`, exposant) échantillonnées au pas `res` ; un saut au début d'un clip prend la valeur **après** le saut, à la fin la valeur **avant** ; deux points au même instant = marche verticale, ordre conservé.
5. **Reconstruction** en session : MIDI (notes, vélocités, probabilité, déviation, release), audio (fichier, warping, mode, gain, transposition, warp markers recréés), boucle, marqueurs, nom, couleur, signature, launch ; enveloppes exposées recopiées ; `duplicate_clip_to_arrangement` à la position d'origine ; suppression du clip de session (et de la scène créée si besoin), **aussi en cas d'erreur**. Live conserve l'automation des autres paramètres sous le clip.
6. Une seule étape d'annulation Live (Cmd+Z) par `/shape` ou `/clear`.

Non recopiables (à accepter explicitement) : fondus de clip, expressions de notes, warp non reproductible. Non reproductibles (refusés) : clips bouclés étirés, take lanes. Rien n'est automatisable hors d'un clip.

## Client
```bash
python3 lom.py ping
python3 lom.py param "AUDIO - Sub" mixer Volume
python3 lom.py plan  "AUDIO - Sub" o:493090:4 --unit disp --accept fades 5|1 -5 8|4.5 -5 9|1 0
python3 lom.py shape "AUDIO - Sub" o:493090:4 --unit disp --accept fades 5|1 -5 8|4.5 -5 9|1 0
python3 lom.py read  "AUDIO - Sub" o:493090:4 5|1 9|1 --res 1
python3 lom.py apply automations_el21.json --dry      # plan serveur pour chaque entrée, rien n'est écrit
python3 lom.py apply automations_el21.json
python3 lom.py jobs ; python3 lom.py cancel <id>
python3 lom.py serve --port 7480                       # HTTP JSON ; Authorization: Bearer <token> ; /py /set /call /reload bloqués sauf --unsafe
```
Spec `apply` : `{"beatsPerBar":4,"automations":[{"track":"AUDIO - Sub","device":"mixer","param":"Volume","unit":"rel|disp|raw","res":8,"curve":"lin","hold":false,"accept":["fades"],"points":[["5|1",-5],["9|1",0]],"note":"…","skip":false}]}`. `rel` = offsets par rapport à la valeur courante affichée. `--dry` appelle `/plan` avec les mêmes arguments que l'écriture.

HTTP : `POST /cmd {"cmd":"/plan","args":[…]}`, `POST /apply {"spec":{…},"dry":true}`, `GET /` = aide. Jeton obligatoire dans l'en-tête `Authorization`, en-tête `Origin` refusé.

## Ce qui a été vérifié
- **Tests logiciels** (24, sans Live) : OSC int64 sans perte, références inchangées sur le fil, client qui ignore les lignes d'autres requêtes, jeton exigé et fichier créé à l'init, id sur chaque ligne, refus des ids numériques et des sessions étrangères, interpolation gauche/droite, budget = nombre de points générés, fenêtre nulle, saturation, `accept`, clips bouclés étirés, ancrages exacts, ordre des points d'un saut, nettoyage après erreur de reconstruction, annulation par id, revalidation quand un clip disparaît, liste blanche HTTP.
- **Dans Live 12.4.5** (`tests/live_suite.py`, 26 contrôles, copie d'el21) : saut au bord d'un clip, 192 points hors fenêtre inchangés, validations `/read` et `/plan`, fusion audio par échantillonnage avec conservation de l'ancienne rampe et du Pan, annulation d'une tâche en cours par id, curseur restauré, revalidation. Sur la copie d'el21 : zones non ciblées d'autres pistes identiques ; sweep du même clip conservé à 0,0011 près (échantillonné) ; Cmd+Z défait tout en une étape ; après sauvegarde et réouverture, valeurs identiques à 0,0000 près.
