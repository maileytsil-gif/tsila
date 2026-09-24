---
name: ableton-live-session
description: Méthode de travail pour produire dans Ableton Live 12 avec Producer Pal, le LOM Bridge (lom.py) et le contrôle d'écran, telle que cet utilisateur la pratique, et **carte d'entrée vers les 27 autres skills musique** (situation → chaîne de skills). Utilise ce skill dès que la demande touche Ableton, un Set Live, une piste, un clip, un device, un plug-in (Serum, Waves, FabFilter, iZotope…), un bus, un niveau, une sauvegarde ou une vérification dans Live — même si l'utilisateur n'écrit que « la basse », « le drop », « le master » ou « corrige ». Utilise-le aussi en tout premier quand l'utilisateur commence un NOUVEAU morceau (« nouveau projet », brief de style/BPM/tonalité) : il donne l'ordre des 8 étapes et les règles apprises à la dure (hot-swap, transport, relecture, sauvegarde, natifs tolérés, une étape par échange).
---

# Session Ableton Live (Producer Pal + LOM Bridge + écran)

## Trois outils, un rôle chacun
- **Producer Pal** (`ppal-*`) : lecture/écriture MIDI, clips, pistes, devices natifs, routage, marqueurs. Pas d'automation, pas de sauvegarde, rien dans un VST.
- **LOM Bridge** (`$LOM_BRIDGE_DIR/lom.py`, défaut `/Volumes/NO NAME/caude/lom-bridge`) : depuis 0.8.0, des **commandes typées** qui vérifient elles-mêmes ce qu'elles font — `state` (carte du Set), `transport`, `meters`, `setparam`, `snapshot`/`restore`, `load` (anti hot-swap vérifié), `notes`, `locator`, **automation d'arrangement** (`apply`, `read`, tout ou rien + relecture), `journal`, `wait`. `py` (Python arbitraire dans Live) reste pour ce qui n'a pas de commande. Voir `references/bridge.md`.
- **Contrôle d'écran** (`app_*`, `computer_batch`) : menus de Live (en **français** : Fichier › Sauver Set Live, Créer › Insérer Silence, Edition › Sélectionner boucle), dialogues (export), fenêtres de plug-ins sans paramètres exposés (Pro-Q 4, soothe3, SPAN). Voir `references/plugins.md`.

Lance un script Python dans Live avec `scripts/pyl.sh fichier.py` (variables `song`, `app` ; mets le retour dans `result`). Le convertisseur aplatit les dicts : renvoie des listes.

## Discipline qui évite les dégâts
0. **Ouvrir la séance par le bridge** : `lom.py ping` (version chargée = version du disque, sinon relancer Live) puis `lom.py state --json` (pistes, devices, paramètres automatisés, repères, transport) — c'est l'état réel, pas la mémoire. Toute écriture du bridge est journalisée : `lom.py journal 10` en fin de séance pour la mémoire du projet.
1. **Relis après chaque action.** Les commandes typées du bridge relisent elles-mêmes (`verified …`, avant/après de `setparam`, contrôle de `load`, note à note pour `notes`) et **défont l'étape** si Live n'a pas écrit ce qui était demandé (`E_ROLLED_BACK` = rien n'est modifié). Tout ce qui passe encore par `py`, Producer Pal ou l'écran se relit à la main : chaîne de devices, notes, `str_for_value`, coverage des clips. Une erreur porte un code (`ERREUR [E_…]`) : `E_STALE` → replanifier, `E_AUTOMATED` → passer par `apply`, `E_AUTOMATION_OVERRIDDEN` → `song.re_enable_automation()`, `E_TRANSPORT_PLAYING` → demander l'arrêt, `E_ROLLBACK_FAILED` → Cmd+Z tout de suite.
2. **Hot-swap** : `browser.load_item` REMPLACE le device sélectionné, où qu'il soit. Charger avec **`lom.py load "<piste>" "<nom>" [source] [replace=<device>]`** : il applique la règle (piste sélectionnée, dernier device sélectionné) et **vérifie** qu'il y a un device de plus, rien d'écrasé, aucune autre piste touchée ; « Serum 2 » existe en VST3 et AU → préciser. Par `py`, la règle à la main : `song.view.selected_track = t` puis `song.view.select_device(t.devices[-1])`, et relire la chaîne de la piste ET des voisines. C'est ainsi qu'un Pro-Q 4 réglé a été écrasé une fois.
3. **Transport** : `read`/`apply`/`notes`/`locator` exigent l'arrêt ; l'utilisateur écoute souvent. `lom.py transport` d'abord ; ne l'arrête pas sans le dire (`lom.py transport stop` une fois d'accord).
3b. **Avant de toucher un réglage à la main** (`setparam`, fenêtre de plug-in) : `lom.py snapshot "<piste>" [device|mixer]` → `restore <id>` remet tout en une étape si l'essai ne convainc pas. `setparam` refuse un paramètre automatisé : c'est voulu (une écriture manuelle surcharge l'automation) ; passer par `apply`, ou `override` en le disant.
4. **Sauvegarde** : `app_menu` Fichier › « Sauver Set Live » après chaque étape validée. Si l'item est grisé, il n'y a rien à sauver.
5. **Une étape par échange** : l'utilisateur veut le plan complet à l'avance mais n'exécute (ou ne valide) qu'une étape à la fois ; il corrige lui-même dans Live entre deux — relis l'état avant d'agir.
6. **Plus d'effets natifs Ableton** dans les chaînes de mix (demande explicite). Liste unique des natifs tolérés : instruments natifs et Auto Filter déjà posés sur les pistes MIDI, Utility (mono, trim, phase), Compressor en sidechain déjà en place, Hybrid Reverb sur un retour. Tout nouveau traitement de mix est un plug-in tiers (`../effets-plugins/references/fiches.md`).

## Mesurer sans oreilles
`lom.py meters <mesure>|1 <secondes> [pistes…]` (ou `scripts/levels.sh <mesure> [pistes…]`, qui l'appelle) lance la lecture, relève la crête de chaque piste et du master pendant la durée demandée, puis arrête et remet le curseur ; si la lecture est déjà en cours, il lit sans rien toucher. Pièges : `output_meter` d'une piste audio lit **après devices et après fader** (mesuré le 15 sept. 2026 ; l'ancienne note « pré-fader » était fausse), celui du master est **pré-devices du master** ; l'échelle de `output_meter` n'est pas linéaire (≈ 0,85 = 0 dB) : les chiffres de `levels.sh` ne valent qu'en **relatif** (avant/après, piste contre piste), jamais en dBFS absolus. Pour un chiffre fiable, exporte et analyse le WAV (skill `live-export-wav`).

## Paramètres de VST
`lom.py setparam "<piste>" "<device>" "<param>" <valeur>` : valeur affichée (dB, Hz, %) résolue par le bridge, `raw` pour 0–1 ou un paramètre quantifié, avant/après relu, refus si automatisé. Par `py`, `scripts/helpers.py` (`solve(p, cible)`, `set_enum(p, 'label')`) pour les cas que `setparam` ne couvre pas (énumérations par libellé). Quels plug-ins exposent quoi et comment vérifier : `../effets-plugins/references/fiches.md` ; techniques de fenêtre : `references/plugins.md` ; réglages éprouvés : `references/mix-chain.md`.

## Conventions du projet en cours
Mémoire persistante : `~/.claude/projects/-Volumes-NO-NAME-caude/memory/` (fichier du projet + `lom-bridge.md`). Note-y chaque piège nouveau. Pistes `AUDIO - X` → `BUS - …` → `BUS MASTER 1 → 2 → 3` → Main ; REF → Main. Numérotation Ableton : C3 = 60.

## Nouveau projet — enchaîner tous les skills
L'utilisateur veut, pour chaque nouveau morceau, la même méthode complète. Ordre à suivre, une étape validée à la fois, plan annoncé d'abord :
1. **Cadre** : inspecter le Set ouvert et le bridge (`lom.py ping`, `lom.py state --json`), **Sauver Set Live sous…** un nouveau nom avant toute modification, créer `projet-<nom>.md` (skill `memoire-projet`), tempo/tonalité/gamme (`theorie-musicale-electronique` : `theorie.py gamme`, `genres.md`, `forme-tension.md`), structure avec repères et durée exacte (skill `arrangement-avance`).
2. **Instruments** : une piste par rôle, kit depuis la signature (skill `drums-signature`), natif ou tiers selon la fiche (rôle `sound-designer-serum` → `vst-sound-design`), rôle sub/kick décidé (skill `kick-bass-equilibre`), niveaux mesurés, sidechain.
3. **Passage central de 8 mesures** : groove (rôle `producteur-rythmique`), basse et hook composés à partir de l'intention (rôle `compositeur-arrangeur` → `melodie-composition`), rendus vivants (skill `midi-expressif`), vérifiés note à note.
4. **Arrangement complet** : sections, entrées/sorties, contrastes, variations toutes les 4/8 mesures (skill `arrangement-avance`, schémas dans `forme-tension.md`).
5. **Mix** : diagnostic et contrôle qualité (rôle `ingenieur-mixage`), procédure (skill `mixage`), pistes AUDIO → bus → masters, chaînes tiers avec fiches, comparaison à niveau équivalent (skill `effets-plugins`).
6. **Automations** : filtres, envois, largeur, transitions, relues (skill `live-automation`).
7. **Voix** si demandées (skill `suno-vocals`).
8. **Export** vérifié (skill `live-export-wav`) et compte rendu bref : créé / emplacements / limites.
Mémoire projet : créer un fichier `projet-<nom>.md` dès l'étape 1 et le tenir à jour (structure, règles musicales, pièges).

## Quatre rôles complémentaires (15 sept. 2026)
Quand la demande est un métier entier plutôt qu'une opération, passer par la méthode du rôle, qui orchestre les skills spécialisés et porte les règles communes (capacités vérifiées, session préservée, modifications contrôlées, jamais « entendu » sans mesure) : `compositeur-arrangeur` (notes, harmonie, forme), `producteur-rythmique` (batterie, basse, groove, Maschine), `sound-designer-serum` (timbre, Serum 2, synthèse), `ingenieur-mixage` (équilibre, masquage, contrôle qualité). Chaque rôle dit quand passer la main aux trois autres.

## Carte « situation → skills » (vérifiée en simulation le 15 sept. 2026)

Entrer par la ligne qui correspond à la demande, dans l'ordre ; chaque skill dit quand passer au suivant. Toute session s'ouvre et se ferme par `memoire-projet`.

| Ce que demande l'utilisateur | Chaîne |
|---|---|
| « Où on en est », « on fait quoi maintenant », plusieurs morceaux à la fois, retour après interruption | **chef-de-projet** (`tableau.py`, arbitrage, plan annoncé) → la ligne correspondante ci-dessous |
| Nouveau morceau (style, BPM, tonalité) | ableton-live-session (sauver sous, ping) → memoire-projet → theorie-musicale-electronique (`genres.md`, `forme-tension.md`, `theorie.py gamme`) → arrangement-avance → drums-signature + kick-bass-equilibre → producteur-rythmique → compositeur-arrangeur → midi-expressif → ingenieur-mixage → live-automation → live-export-wav |
| « On reprend » / fin de session | memoire-projet (`reprise.sh`, en-tête REPRISE, questions sans réponse) → relire l'état réel avant d'agir → memoire-projet (`journal.sh`, REPRISE) |
| Écrire ou corriger des notes (mélodie, hook, accords, basse, contre-chant) | compositeur-arrangeur → theorie-musicale-electronique (`theorie.py progression|contrepoint`) → melodie-composition → midi-expressif |
| Question de théorie seule (« quel mode », « à quel BPM », « pourquoi ça frotte ») | theorie-musicale-electronique seul ; n'ouvrir un rôle que si l'utilisateur demande ensuite d'écrire |
| Batterie, groove, swing, fills | producteur-rythmique → drums-signature (`drum_pattern.py --fixe`, `kit_builder.py`) → theorie (`rythme-avance.md`, `theorie.py euclid|syncope`) → midi-expressif |
| Structure, sections, transitions, minutage | arrangement-avance (+ `forme-tension.md` pour le schéma du genre) → live-automation pour les mouvements |
| Un son, un preset, un timbre | sound-designer-serum → vst-sound-design (natifs par API, Serum par clics) → synthese-reference si un fichier de référence existe → effets-plugins |
| Cuivres : trompette, section, brass synth, stabs, braam, lead « screech » | studio-grade-brass-sound-design (recettes, corpus local `corpus/cuivres/`) → vst-sound-design → midi-expressif (articulations, keyswitches) → effets-plugins → ingenieur-mixage |
| Claviers et synthés funk : Rhodes, Wurli, Clav, orgue B3 + Leslie, synth bass P-Funk / boogie, talkbox, stabs | studio-grade-funk-keys-synth-sound-design (recettes, corpus local `corpus/funk-claviers/`) → vst-sound-design → midi-expressif (voicings, grilles) → producteur-rythmique si le groove est en cause → effets-plugins |
| Capturer de l'audio, flip de sample | resampling (capture) → sampling-composition-avancee (recomposition) → live-export-wav (`analyze_wav.py`) |
| « C'est boueux », « ça se bagarre », « trop fort » | ingenieur-mixage (diagnostic, tableau mesuré/écouté/supposé) → mixage (procédure) → kick-bass-equilibre si le grave est en cause → effets-plugins |
| Master, LUFS, livraison | ingenieur-mixage → live-mix-mastering → mastering-outils → live-export-wav |
| Voix | suno-vocals → effets-plugins → live-automation |
| Maschine / Komplete Kontrol | native-instruments-control (écran au premier plan, aucune API) |
| Citer une œuvre existante | partition-recherche → partition-telechargement → melodie-composition |

Pièges relevés en simulation, à ne pas refaire : la numérotation des mesures de la mémoire peut être périmée (relire les repères avant d'écrire) ; `check_scale.py`, `clip_summary.py`, `expression_report.py`, `snapshot_clips.py` n'existent que dans Live (hors Live, calculer avec `theorie.py`) ; les scripts à paramètres en tête se copient dans le scratchpad avant édition ; les chiffres de `levels.sh` sont relatifs ; aucun outil local ne mesure LUFS ni true peak.
