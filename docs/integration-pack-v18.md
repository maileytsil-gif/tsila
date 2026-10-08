# Pack v18 : intégration dans les cinq skills

Le pack `bass-house-skills-v18` (13 skills en français, importé le 19 sept. 2026 sur la branche
`claude/new-session-x91wej`, jamais fusionné) est intégré le 8 oct. 2026 comme **13 modules** des cinq skills.
Ce fichier dit où ils sont, qui tient quoi et ce qui diffère de l'installation réelle.

**Règle d'arbitrage** : les skills et modules maison **décident et exécutent** ; le pack **fournit la matière musicale**.
Il n'a jamais le dernier mot sur une opération dans Live, une mesure ou une valeur chiffrée. Chaque `GUIDE.md` du pack
porte cet avertissement sous son titre.

## Où sont les modules du pack

| Skill | Modules du pack v18 |
|---|---|
| `producteur-live` | composer-producer-director (avec les dossiers de support du pack : `core/`, `data/`, `producer-intelligence/`, `history/`, `blueprints/`, ses fichiers racine `README.md`, `MANIFEST.md`, `CHANGELOG-v18.md`, `RESEARCH-LEDGER.md`, `VALIDATION.json`, `requirements-validation.txt`), bass-house-ableton-bridge |
| `compositeur-arrangeur` | bass-house-composition, modern-pop-electronic-music-theory, modern-jazz-chillout-theory, afro-caribbean-latin-detroit-theory |
| `producteur-rythmique` | studio-grade-kick-low-end-sound-design, studio-grade-drums-electronic-percussion |
| `sound-designer-serum` | bass-house-serum2-sound-design, studio-grade-bass-sound-design, studio-grade-sample-vocal-break-design, studio-grade-transition-fx-director |
| `ingenieur-mixage` | bass-house-mixing-mastering |

Dans le tableau suivant, écrit en septembre, les noms des anciens skills maison sont aujourd'hui des noms de modules
(table de correspondance : `docs/regroupement-skills.md`).

## Répartition par domaine

| Domaine | Décide, exécute, mesure (maison) | Apporte la matière (pack v18) |
|---|---|---|
| Séance, plusieurs morceaux, arbitrage | `chef-de-projet` | — |
| Direction d'**un** morceau, brief → chaîne | `chef-de-projet` ouvre ; `producteur-live` donne l'ordre des 8 étapes | `composer-producer-director` (graphe conditionnel par style, contrats JSON) |
| **Exécution dans Live** | `producteur-live`, `vst-sound-design`, `live-automation`, `live-export-wav` | `bass-house-ableton-bridge` — **plan seulement**, n'exécute jamais |
| Théorie, gammes, formes, BPM | `theorie-musicale-electronique` (script `theorie.py`) | `modern-pop-electronic-music-theory`, `modern-jazz-chillout-theory`, `afro-caribbean-latin-detroit-theory` |
| Écriture de notes | `compositeur-arrangeur` → `melodie-composition` → `midi-expressif` | `bass-house-composition`, les 3 skills de théorie ci-dessus |
| Groove, batterie, swing | `producteur-rythmique` ; `drums-signature` (signature sonore de l'utilisateur) | `studio-grade-drums-electronic-percussion` (tout sauf le kick) |
| Kick / sub / relation grave | `kick-bass-equilibre` (mesures sur exports séparés) | `studio-grade-kick-low-end-sound-design` (conception du kick), `studio-grade-bass-sound-design` |
| Timbre, synthèse | `sound-designer-serum` (choix du moteur), `vst-sound-design` (exécution), `synthese-reference` (si fichier de référence) | `bass-house-serum2-sound-design` (familles et sous-types), `studio-grade-bass-sound-design` |
| Structure, sections, minutage | `arrangement-avance` | `bass-house-composition` |
| Transitions, FX de frontière | `arrangement-avance` décide où ; `live-automation` exécute | `studio-grade-transition-fx-director` (conception) — ⚠ voir § Plug-ins |
| Samples, chops, resampling | `resampling`, `sampling-composition-avancee` | `studio-grade-sample-vocal-break-design` |
| Mix | `ingenieur-mixage` (diagnostic, contrôle qualité), `mixage` (procédure), `effets-plugins` (fiches réelles) | `bass-house-mixing-mastering` (cibles et priorités de genre) |
| Master, livraison | `live-mix-mastering`, `mastering-outils`, `live-export-wav` | `bass-house-mixing-mastering` |
| Voix | `suno-vocals` | `studio-grade-sample-vocal-break-design` (traitement des chops) |
| Mémoire | `memoire-projet`, `memoire-persistante` | — |

## Recouvrements à surveiller

**Direction.** `chef-de-projet` et `composer-producer-director` se déclenchent sur des
demandes proches. `chef-de-projet` gère le portefeuille (où on en est, quoi ensuite,
ouverture/fermeture de séance) ; `composer-producer-director` gère la chaîne de
production d'un seul morceau. Sur « nouveau morceau », entrer par
`producteur-live` : le Director sert ensuite à choisir la branche de style
(Afro/Latin, Detroit, Jazz/Chill, électronique par défaut) et à produire les contrats.

**Mix.** `bass-house-mixing-mastering` donne des cibles de genre utiles, mais il ne
connaît pas la chaîne de bus de l'utilisateur (`AUDIO - X` → `BUS - …` → `BUS MASTER
1/2/3` → Main), ni la règle « pas de nouvel effet natif », ni le fait que `levels.sh`
est relatif. Le diagnostic et le contrôle qualité restent à `ingenieur-mixage`.

**Kick.** `studio-grade-kick-low-end-sound-design` conçoit un kick de zéro et propose
un modèle d'ownership `KICK OWNS SUB / BASS OWNS SUB / ALTERNATING / KICK+RUMBLE`.
`kick-bass-equilibre` reste seul juge de la relation réelle dans le Set, parce qu'il
mesure (corrélation 30–120 Hz, annulation, énergie sous/au-dessus de 60 Hz) sur des
exports séparés. Concevoir avec le premier, trancher avec le second.

**Sound design Bass House et basses** (recouvrement apparu après septembre). `bass-house-serum2-sound-design`
(familles et sous-types) recouvre le module maison `bass-house-sound-design` (recettes Serum 2 et Wavetable chiffrées,
stabs hors Basic Shapes) ; `studio-grade-bass-sound-design` recouvre `serum-2-basses-house-future-house` (dix fiches
jouables et 440 recettes). Choisir le sous-type avec le pack, prendre la recette chiffrée dans le module maison.

**Mix de genre.** `bass-house-mixing-mastering` recouvre `mixer-house-professionnel` (priorités Bass House,
Future Rave, Tech House, Minimal, synthèses de 60 tutoriels) ; en cas d'écart, le module maison prime.

## Plug-ins — écart entre le pack et l'installation

Inventaire des fiches maison (`effets-plugins`, `mastering-outils`) : FabFilter Pro-Q 4,
Pro-C, Pro-L ; Waves REQ 6, API-2500, L2/L3/L4, J37, MetaFlanger, F6, WLM Plus,
TG Mastering Chain ; Plugin Alliance bx_glue ; oeksound soothe3 ; iZotope Imager,
Insight, Tonal Balance, Ozone Elements ; Voxengo SPAN ; TDR Nova.

Cités par le pack et **absents de cet inventaire** :

| Cité par le pack | Occurrences | Substitution proposée — **à valider par l'utilisateur** |
|---|---|---|
| ValhallaDelay, H-Delay, Timeless 3 | ~54 | J37 (delay/bande Waves) ; sinon Echo natif, qui tombe sous la règle « pas de nouvel effet natif » → à trancher |
| ValhallaRoom / VintageVerb / Supermassive, Pro-R 2 | ~28 | Hybrid Reverb sur un retour (seul natif toléré en réverb) ; sinon acquisition |
| MetaFilter, Volcano 3 | 15 | Auto Filter natif (toléré sur pistes MIDI) pour le mouvement + Pro-Q 4 pour la forme ; MetaFlanger pour la modulation |
| Stutter Edit 2 | 11 | Pas d'équivalent installé. Beat Repeat natif ou découpe manuelle + `resampling` → à trancher |
| NI Guitar Rig | 11 | **À vérifier** : peut être présent via Komplete (`native-instruments-control`) |
| SoundShifter | 6 | Warp Complex Pro de Live 12 + `resampling` |

Ces substitutions sont des propositions, pas des équivalences mesurées. Tant qu'une
chaîne n'a pas été montée et relue dans le Set, elle reste `[TEST]`.

## Ce que le pack apporte réellement

Au-delà des 13 guides, la partie exécutable, dans `.claude/skills/producteur-live/modules/composer-producer-director/` :

- `core/schemas/` : 9 JSON Schemas (ProductionBrief, GrooveSpec, BassInterlockSpec, HarmonySpec, SoundSpec,
  AutomationSpec, CulturalStyleLock, AbletonClipPlan, BridgeActionBatch) ;
- `core/compiler/compile_project.py` : `Specs → AbletonClipPlan → BridgeActionBatch`, sans commander Live ;
  `export_plan_to_midi.py` sort des MIDI importables ;
- `core/examples/` : 3 morceaux complets (Afro House F#m 122, Afro-Cuban Cm 124, Detroit D dorien 128) avec contrats et MIDI ;
- `core/index/director-graph.json` : le graphe de routage par style ;
- `data/` : patterns event-based, profils de timing par rôle, matrice d'hybridation ;
- `producer-intelligence/` : 15 études de référence et 10 vecteurs de producteurs, en principes abstraits.

Le chemin utile : **pack pour planifier → modules maison pour exécuter**, une étape à la fois.

## Ce qui a changé à l'intégration (8 oct. 2026)

- Chaque `SKILL.md` du pack est devenu `GUIDE.md` : en-tête YAML retiré, description gardée en citation, avertissement
  « pack v18 » ajouté. Rien d'autre n'a été réécrit dans le texte du pack.
- Renvois entre skills du pack réécrits vers les nouveaux chemins (`../core/…` → `../composer-producer-director/core/…`
  ou `../../../producteur-live/modules/composer-producer-director/…`) ; `macro-templates-v7.md` (inexistant) corrigé en
  `macro-templates-v5.md` dans le `README.md` du pack.
- `core/index/file-index.json` et `logical-package-map.json` gardent les chemins et empreintes d'origine (19 sept.) :
  ils documentent le pack tel que livré, plus les fichiers convertis.
- Validation du pack à son nouvel emplacement : **66/66** (`core/validation/validate_v18.py`, dépendances
  `jsonschema` et `mido` dans un environnement isolé ; le script réécrit `VALIDATION.json`, le lancer sur une copie).

## Maintenance

Ne pas réécrire le contenu musical du pack : mettre l'adaptation ici, dans `AGENTS.md` ou dans un module maison.
Une v19 éventuelle se recopie par-dessus les mêmes modules, puis on refait la conversion `GUIDE.md`, les renvois,
`python3 outils/verifier_skills.py` et la validation du pack.
