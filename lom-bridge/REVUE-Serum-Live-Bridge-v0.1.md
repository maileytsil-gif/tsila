# Revue du prototype « Serum Live Bridge v0.1 »

Revue faite le 12 septembre 2026 à partir des sources de l'archive (1 253 lignes, 17 tests simulés) **et** de l'installation réelle du Mac mini, relevée pendant la séance :

| Élément | Version réelle |
|---|---|
| macOS | 26.6.2 (Darwin 25.6) |
| Ableton Live | 12.4.5 Suite |
| Max (embarqué dans Live) | 9.1.5 |
| Node for Max (node embarqué) | v22.18.0 ; Node système : v26.8.1 |
| Serum 2 | 2.1.5, **VST3** (l'AU est aussi installé, Live utilise le VST3) |
| Producer Pal | 2.2.0 (2.3.0 disponible) |
| Bibliothèque utilisateur Live | `/Volumes/Seagate Portable Drive/ableton /User Library/` (pas `~/Music/Ableton`) |

Deux résultats d'expérience obtenus aujourd'hui sur cette machine pèsent sur toute la revue :

- **Le LOM exposé à Max for Live n'a aucune fonction d'automation.** `Clip.info` ne liste que `clear_envelope` / `clear_all_envelopes` ; `automation_envelope` et `create_automation_envelope` n'existent que dans l'API Python des Remote Scripts (journal Live : `'Clip' object has no attribute 'create_automation_envelope'`). L'« étape suivante » annoncée par le prototype (enveloppes Arrangement) est donc **impossible dans son architecture js/Node for Max**.
- **Même en Python, une enveloppe ne se crée que sur un clip de session et n'agit que dans l'étendue de son clip.** Une écriture d'automation d'arrangement passe par la reconstruction du clip depuis la session (`ClipSlot.create_clip` / `create_audio_clip`, `Clip.create_automation_envelope`, `Envelope.create_event`, `Track.duplicate_clip_to_arrangement`). Ceci est implémenté et vérifié dans `LOMBridge` (Remote Script, ce dossier) : une montée de filtre a été écrite et relue dans el21 aujourd'hui.

Dans el21 réel, les trois instances de Serum 2 n'exposent à Live **qu'un paramètre (« Device On »)** ou deux : sans « Configure », le bridge ne verrait rien de Serum. C'est prévu dans le guide, mais cela vaut pour Producer Pal aussi, et cela borne le périmètre : seuls les paramètres configurés (128 max) sont pilotables, par n'importe quel outil.

---

## 1. Problèmes démontrables par lecture du code

Classés par gravité. **B** = bloquant avant tout test utile, **H** = haute, **M** = moyenne, **F** = faible.

### B1. Le moteur de courbes pollue l'historique d'annulation et fait des marches audibles
- **Fichier** : `live-bridge.js`, `tick()` / `startCurve()`.
- **Scénario** : courbe de 8 mesures à 126 BPM sur un cutoff, tick 50 ms → environ 300 appels `LiveAPI.set('value')` par paramètre.
- **Conséquence** : chaque `set` via LiveAPI est une action annulable dans Live → 300 entrées d'undo par paramètre ; Cmd+Z après une courbe recule d'un cinquantième de seconde. Et 20 mises à jour par seconde sur un filtre résonant = crénelage audible (Serum lisse un peu, pas assez pour un cutoff qui bouge de 20 % à 80 % en 8 mesures ? oui ; en 1 mesure, non).
- **Correction** : pour du mouvement temps réel, l'outil prévu par Cycling '74 est `live.remote~` (contrôle au rythme du signal, **sans** entrée d'undo, sans conflit avec l'automation). Le js ne fait plus que mapper le paramètre (`live.remote~` reçoit `id N`) et générer la courbe avec `line~`/`curve~` ou un `mc.` rampes. Contraintes à annoncer : le paramètre devient gris (inaccessible à la main et à l'automation) tant qu'il est mappé ; il faut démapper à la fin (`id 0`).
- **Test** : dans Live, lancer une courbe de 4 mesures puis compter les Cmd+Z nécessaires pour revenir à l'état d'avant ; écouter un balayage 200 Hz → 8 kHz sur 1 mesure avec un filtre à résonance haute.

### B2. Le bouton START réinitialise la session et efface les snapshots
- **Fichier** : `Bridge-source.maxpat` (`t b b` → `init` + `script start`), `live-bridge.js` `init()`.
- **Scénario** : l'IA a lu des IDs et posé un snapshot ; l'utilisateur reclique START (le seul bouton pour relancer le serveur si le nœud est mort, ou par réflexe).
- **Conséquence** : `session` change, `snapshots = {}` → toute restauration devient impossible et chaque commande ciblée renvoie « Session changed ». Le guide dit « évite de le recliquer », ce qui n'est pas une protection.
- **Correction** : séparer INIT (une fois, par `live.thisdevice`) de START/STOP serveur ; ne réinitialiser la session que quand `live.thisdevice` bang (nouveau Set ou rechargement). `@autostart 1` sur `node.script` pour que le serveur démarre avec le Set.
- **Test** : snapshot, START, restore → doit réussir.

### B3. Le paquet n'est pas chargeable tel quel : pas de `.amxd`, copier-coller manuel entre deux patchs, chemins absolus
- **Fichier** : `LIRE-MOI.md` §2, `setup.cjs`.
- **Scénario** : suivre le guide.
- **Conséquence** : la procédure « copier les objets d'un `.maxpat` dans un Max Audio Effect vierge » est fragile (mode présentation, `plugin~/plugout~` en double si l'on oublie de supprimer, `live.thisdevice` qui ne bangue qu'au chargement du device donc **pas au collage** : `init` ne sera jamais appelé tant qu'on n'a pas sauvegardé et rechargé le device). Les chemins absolus vers `max-server.cjs` et `live-bridge.js` cassent au moindre déplacement du dossier.
- **Correction** : livrer un `.amxd` (format `ampf` + JSON, générable par script : voir `build_amxd.py` de ce dossier qui le fait pour LOM Bridge) ; placer `.js` et `.cjs` **dans le même dossier que le `.amxd`** (Live ajoute ce dossier au chemin de recherche) et référencer les fichiers par nom, pas par chemin absolu ; ou geler le device.
- **Test** : ouvrir un Set vierge, glisser le `.amxd`, la console doit afficher « Live API ready » sans clic.

### H1. Quatre lectures LiveAPI par canal à chaque tick, pour rien
- **Fichier** : `live-bridge.js`, `tick()` lignes 126–129 (`id`, `name`, `min`, `max` relus, puis `set` puis `get value`).
- **Conséquence** : 8 canaux × 6 appels × 20 Hz ≈ 1 000 appels LOM/s sur le thread principal de Live (chaque appel traverse la couche Python `_MxDCore`). Risque réel de saccades d'interface et de décrochages audio pendant la courbe.
- **Correction** : mettre en cache `min`/`max`/`name` au démarrage, surveiller la disparition d'un objet via le callback de `LiveAPI` (observer `name`) au lieu de le relire ; ne pas relire la valeur à chaque tick. Ou passer à `live.remote~` (B1) qui supprime le problème.
- **Test** : mesurer la charge CPU de Live pendant une courbe à 8 canaux ; comparer avec un canal.

### H2. Blocage de tout paramètre déjà automatisé
- **Fichier** : `live-bridge.js`, `writable()` (`automation_state !== 0` → erreur).
- **Scénario** : dans el21, les faders d'AUDIO - Kick, AUDIO - Sub, AUDIO - Lead (send) et plusieurs Device On sont automatisés.
- **Conséquence** : ces cibles sont inaccessibles. En pratique, sur un morceau en cours de mix, c'est une part importante de ce que l'on veut bouger.
- **Correction** : distinguer `automation_state` 1 (automation active) et 2 (déjà surchargée) ; proposer un mode explicite `override: true` qui écrit et signale que Live affichera « Réactiver l'automation ». Et surtout : proposer d'**écrire** l'automation (voir §7) plutôt que de la contourner.
- **Test** : `set_parameters` sur un fader automatisé avec et sans `override`.

### H3. Timeout : l'écriture peut encore se produire après la réponse « issue indéterminée »
- **Fichier** : `max-server.cjs` (timer 5 s remet `busy=false`), `live-bridge.js` `request()` (contrôle `expires` **seulement avant** exécution), `applyChanges()` (vérification 80 ms plus tard).
- **Scénario** : Live est bloqué 4 s (chargement d'un plug-in, analyse d'un sample) ; la requête sort de `deferlow` à 4,4 s, passe le test `expires` (4,5 s), écrit, et la lecture de contrôle part à 4,48 s ; le serveur a répondu 504 à 5 s… ou la réponse arrive à 5,01 s et est ignorée (`pending` vidé). Pendant ce temps `busy=false` → une seconde écriture peut s'intercaler.
- **Conséquence** : écriture réelle mais réponse « inconnue », et possible entrelacement de deux commandes.
- **Correction** : marge cohérente (expiration js = timeout serveur − durée de vérification − marge, ex. 5 s / 3,5 s) ; garder `busy` jusqu'à la réponse js ou un second timeout plus long ; renvoyer dans `status` l'id de la dernière requête exécutée pour que le client puisse lever le doute.
- **Test** : simuler un `deferlow` retardé (Task de 4,6 s avant `request`) et vérifier qu'aucune écriture n'a lieu.

### H4. Fuite mémoire par internement des symboles Max
- **Fichier** : `max-server.cjs` `max.outlet('request', JSON…)`, `live-bridge.js` `reply()` (`outlet(0,'reply', JSON…)`).
- **Mécanisme** : chaque chaîne qui traverse un outlet devient un symbole Max, **interné à vie** dans la table des symboles. Les réponses contiennent des ids de requête aléatoires et des valeurs qui changent : aucune n'est réutilisée. `list_parameters` sur un Serum configuré à 128 paramètres ≈ 30 Ko par appel.
- **Conséquence** : mémoire de Live qui grimpe pendant une longue séance ; jamais libérée avant redémarrage.
- **Correction** : faire passer les charges utiles par un `dict` Max (Node for Max sait envoyer un dictionnaire : `max.setDict` / `outlet` de dict) ou par un fichier/`jsonstring` côté js (`Dict` en js) ; sinon découper et limiter la taille des réponses.
- **Test** : boucler 5 000 `status` et observer la mémoire du processus Live.

### M1. Lecture après 80 ms : fausse confiance pour les VST3
- `applyChanges()` compare `requested` et `actual` avec une tolérance `1e-5 × plage`. Un plug-in VST3 peut normaliser puis dénormaliser (float32) → écarts supérieurs sur des plages larges (fréquences 20–20 000) ; et un paramètre lissé par le plug-in renvoie encore une valeur intermédiaire à 80 ms. Correction : tolérance relative + absolue, et relire aussi `str_for_value` pour comparer l'affichage.

### M2. `list_devices` et `ids(a,'chains')` sur des devices sans chaînes
- Chaque device non-rack déclenche une erreur LiveAPI imprimée dans la console Max (« no such property »). Non bloquant, mais bruit qui masque les vraies erreurs. Tester `a.type` avant (`RackDevice`, `DrumRack`…).

### M3. Le fichier de connexion survit à une fermeture brutale
- `process.on('exit')` ne s'exécute pas sur SIGTERM/crash de Live. Le client lit un port mort et remonte une erreur brute `ECONNREFUSED` au lieu de « Bridge absent ». Correction : traiter `ECONNREFUSED` comme absence et supprimer le fichier périmé ; ajouter un `pid` dans le fichier.

### M4. Deux clients (Claude et Codex) : 409 sans file d'attente ni réessai
- Le bridge refuse la seconde requête pendant la première. Les clients MCP envoient facilement plusieurs appels d'outils en parallèle → erreurs « Bridge busy » en rafale dès la découverte. Correction : file FIFO courte côté serveur (les lectures sont sans risque), refus seulement pour les écritures concurrentes.

### F1. `shutdown` / `serverstop` sont inaccessibles dans le patch
- La boîte `script stop` n'a aucune entrée : code mort. `t l b` sur un message `script stop` fonctionne par accident.

### F2. Détails de robustesse
- `validate()` limite toute chaîne à 256 caractères : un nom de piste long ne pose pas de problème (côté réponse), mais un futur argument de chemin oui.
- `mcp.cjs` ne répond pas à `prompts/list` / `resources/list` (« Method not found ») : la plupart des clients tolèrent, certains journalisent une erreur à chaque connexion.
- `transport.cjs` refuse les ports < 1024 : inutile (`listen(0)` donne ≥ 49152) mais inoffensif.

## 2. Hypothèses à confirmer dans Live (non démontrables par lecture)

| Hypothèse | Pourquoi c'est incertain | Comment vérifier en 2 minutes |
|---|---|---|
| `max.outlet('request', json)` arrive en **un** symbole dans `route request` | Node for Max convertit les chaînes en symboles ; un JSON avec espaces et virgules devrait rester un atome, mais c'est le point le plus souvent cassé dans ce type de pont | Console Max : `print` après `route`, envoyer un JSON avec espaces |
| `js "/chemin avec espaces/live-bridge.js"` charge le script | Les objets `js` acceptent un chemin absolu, mais le guillemetage dans une boîte reconstituée par `setup.cjs` n'a jamais été chargé par Max ici | Ouvrir `Bridge-configured.maxpat` dans Max : la boîte ne doit pas être rouge/pointillée |
| `LiveAPI.mode = 0` a bien le sens « suivre l'objet » | Le prototype s'appuie dessus pour la stabilité des IDs | Renommer/déplacer une piste et relire `get_parameter` |
| `automation_state` et `is_enabled` existent sur les paramètres VST3 configurés | Ajoutés en Live 11 ; jamais lus ici sur un Serum VST3 | `list_parameters` sur un Serum après Configure |
| Le js reçoit `init` **au collage** dans un device existant | `live.thisdevice` ne bangue qu'au chargement d'un device sauvegardé | Suivre le guide §2 tel quel : « Live API not ready » attendu jusqu'au premier rechargement |
| Live reste réactif avec le moteur à 8 canaux | Voir H1 | Observer le compteur CPU et les décrochages |
| Le js survit à un changement de Set | Les `Task` sont annulées par `init`, mais les objets `LiveAPI` d'un snapshot pointent vers des ids morts : `ref()` gère, `snapshotEntries` aussi (contrôle `id`) | Charger un autre Set puis `restore` : doit refuser proprement |

Point d'expérience à ajouter : **quand le moteur audio de Live est éteint** (aucun périphérique sélectionné), Live tombe en App Nap et tout ce qui passe par son thread principal (js, LiveAPI, Producer Pal) répond par timeouts ; le bridge donnerait des 504 en série. À mentionner dans le guide.

## 3. Ce que les simulations masquent

`tests/fake-live.cjs` remplace `LiveAPI`, `Task`, `outlet` par des objets qui **réussissent toujours** : `get` renvoie des tableaux (vrai), `call('str_for_value')` renvoie l'argument (faux : Live renvoie un texte formaté « 1.20 kHz »), `set` accepte n'importe quoi ou « clampe » à 0,5 (pas le comportement d'un VST3), `Task.repeat()` ne fait rien (le moteur n'a jamais tourné dans le temps), et le passage Max des messages (`route`, `prepend`, `deferlow`, symboles) n'est pas testé du tout. Les 17 tests valident la logique JavaScript, pas la faisabilité dans Live. Le rapport le dit honnêtement ; il faut juste ne pas le lire comme une preuve.

## 4. Réponses aux neuf questions

1. **Chargement dans Max for Live** : non prouvé et probablement pas au premier essai (B3, hypothèses 1, 2, 5). Les types LiveAPI utilisés (`Track`, `Chain`, `DrumChain`, `DeviceParameter`, `PluginDevice`) sont corrects ; `get` renvoie bien des tableaux ; `str_for_value` existe.
2. **Compatibilité ES5 / Node** : le js est propre ES5 (aucun `let`, `=>`, `class`). Le Node embarqué dans Max 9.1.5 est **v22.18.0** : `Object.hasOwn`, `??`, `?.`, `node:` préfixes sont disponibles. Le guide exige « Node 18+ » pour le client : le Node système est v26.8.1. OK.
3. **Cycle de vie** : START écrase la session (B2) ; suppression du device tue le nœud mais laisse `connection.json` (M3) ; changement de Set : `init` n'est relancé que si le device est dans le nouveau Set, sinon le nœud continue de servir un js orphelin qui répondra « Live object deleted » : acceptable mais à documenter.
4. **Timeout et écritures partielles** : H3. Les écritures partielles sont bien remontées (`results[].written`), c'est un bon point.
5. **Simulations** : §3.
6. **Moteur 50 ms** : inadéquat pour des filtres et des LFO (B1, H1). `LiveAPI.set` convient aux **changements de valeur** ; les **mouvements** relèvent de `live.remote~` (signal, sans undo) ; les mouvements **à conserver** relèvent de l'automation écrite.
7. **Enveloppes éditables** : impossible en M4L. Méthode supportée et vérifiée sur cette machine : Remote Script Python + reconstruction de clip (voir `LOMBridge/__init__.py`, `README.md`). Les limites à afficher : rien hors d'un clip, fondus de clip perdus, clips bouclés étirés non reproduits, temps d'échantillonnage pour préserver l'automation existante des clips audio.
8. **Producer Pal 2.2.0** fournit déjà : lecture pistes/devices/paramètres **en unités d'affichage** (dB, Hz), écriture de paramètres, création de devices, clips, transport, bibliothèque, sidechain, a/b compare (équivalent d'un snapshot de device). Il ne fait pas : automation, courbes temps réel, snapshots multi-paramètres. Étendre Producer Pal (M4L lui aussi) ne débloque pas l'automation. La bonne répartition : Producer Pal pour l'édition, `LOMBridge` (Remote Script) pour l'automation, et un petit device `live.remote~` si l'on veut vraiment du mouvement temps réel non enregistré. Un second serveur MCP complet fait doublon avec 80 % de Producer Pal.
9. **Transport et secret** : corrects pour un usage local (loopback, port aléatoire, jeton 32 octets en 0600, refus d'`Origin`). Le jeton est lisible par tout processus de l'utilisateur, ce qui est le modèle de confiance normal ici. Manques : pid/fraîcheur du fichier (M3), file d'attente (M4).

## 5. Verdict

**Architecture à revoir** pour l'objectif énoncé, **corrections bloquantes avant test** pour le périmètre qu'il couvre réellement.

Raisons : la fonction qui manque à l'utilisateur (mouvements de filtres et d'effets **conservés dans le morceau**) est hors de portée de cette architecture, pas seulement « non implémentée » ; le moteur temps réel choisit le mauvais mécanisme (undo, charge, crénelage) ; le reste (lecture, écriture, snapshots) existe déjà dans Producer Pal avec de meilleures unités. Le code lui-même est soigné (validation, prévalidation, lecture de contrôle, jeton), et le serveur HTTP/MCP est réutilisable tel quel pour un autre dos.

## 6. Plan court

1. **Première connexion réelle** (1 h) : construire un `.amxd` par script, fichiers `.js`/`.cjs` dans le dossier du device, `@autostart 1`, INIT séparé de START ; vérifier hypothèses 1–2 dans la console Max ; `node cli.cjs status` → `ready: true`.
2. **Un paramètre de Serum** (30 min) : Configure sur Serum 2 (cutoff + 2 macros), `list_parameters`, `set_parameters` +5 %, lire `display` ; comparer avec `ppal-read-device` de Producer Pal sur le même device.
3. **Restauration** (15 min) : snapshot, changement, restore ; puis Cmd+Z pour compter les entrées d'undo créées.
4. **Courbe lente** (1 h) : remplacer le moteur par `live.remote~` + `line~` ; balayage 8 mesures, puis 1 mesure avec résonance, écoute ; vérifier qu'un point de boucle ne coupe pas le mouvement.
5. **Persistance des automations** (déjà disponible) : `python3 lom.py apply spec.json --dry` puis sans `--dry` avec `LOMBridge` ; le sweep CHORDS 2 d'el21 en est la preuve d'aujourd'hui. Si l'on veut une seule porte d'entrée MCP, exposer `LOMBridge` par un `mcp.cjs` équivalent (le serveur HTTP `lom.py serve` existe déjà).
