# Intégration du pack v18 dans les skills maison

Écrit le 19 septembre 2026, à l'import du pack `bass-house-skills-v18`.
Règles d'arbitrage générales : `/CLAUDE.md`. Ce fichier donne le détail par domaine.

Le pack a été conçu comme un produit autonome : il ne connaît ni l'installation de
cet utilisateur, ni ses plug-ins, ni ses pièges. Il apporte de la matière musicale
sérieuse, mais il revendique aussi des rôles déjà tenus par les skills maison. Ce
document dit qui tient quoi.

## Répartition par domaine

| Domaine | Décide, exécute, mesure (maison) | Apporte la matière (pack v18) |
|---|---|---|
| Séance, plusieurs morceaux, arbitrage | `chef-de-projet` | — |
| Direction d'**un** morceau, brief → chaîne | `chef-de-projet` ouvre ; `ableton-live-session` donne l'ordre des 8 étapes | `composer-producer-director` (graphe conditionnel par style, contrats JSON) |
| **Exécution dans Live** | `ableton-live-session`, `vst-sound-design`, `live-automation`, `live-export-wav` | `bass-house-ableton-bridge` — **plan seulement**, n'exécute jamais |
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

## Trois recouvrements à surveiller

**Direction.** `chef-de-projet` et `composer-producer-director` se déclenchent sur des
demandes proches. `chef-de-projet` gère le portefeuille (où on en est, quoi ensuite,
ouverture/fermeture de séance) ; `composer-producer-director` gère la chaîne de
production d'un seul morceau. Sur « nouveau morceau », entrer par
`ableton-live-session` : le Director sert ensuite à choisir la branche de style
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

Au-delà des 13 `SKILL.md`, la partie exécutable :

- `core/schemas/` — 9 JSON Schemas (ProductionBrief, GrooveSpec, BassInterlockSpec,
  HarmonySpec, SoundSpec, AutomationSpec, CulturalStyleLock, AbletonClipPlan,
  BridgeActionBatch).
- `core/compiler/compile_project.py` — `Specs → AbletonClipPlan → BridgeActionBatch`.
  Ne commande pas Live. `export_plan_to_midi.py` sort des MIDI importables.
- `core/examples/` — 3 morceaux complets (Afro House F#m 122, Afro-Cuban Cm 124,
  Detroit D dorien 128) avec tous les contrats et les MIDI.
- `core/index/director-graph.json` — le graphe de routage par style.
- `data/` — patterns v18 event-based, timing profiles par rôle, matrice d'hybridation.
- `producer-intelligence/` — 15 études de référence et 10 vecteurs de producteurs,
  en principes abstraits (pas de transcription, pas de preset reconnaissable).

C'est la vraie valeur du pack : des contrats vérifiables et des exemples complets.
Le chemin utile est donc **pack pour planifier → skills maison pour exécuter**.

## Maintenance

Le pack est vendu tel quel. Les 509 fichiers indexés dans
`core/index/file-index.json` sont intacts (SHA-256 vérifiés à l'import). Ne pas
éditer un fichier du pack : mettre l'adaptation ici, dans `/CLAUDE.md`, ou dans un
skill maison. Mise à jour vers une v19 = recopier par-dessus, puis relancer la
validation et relire ce fichier.
