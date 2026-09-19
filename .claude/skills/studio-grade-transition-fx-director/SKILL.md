---
name: studio-grade-transition-fx-director
description: Conçoit et orchestre les transitions, uplifters/downlifters, reverse FX, sweeps, tonal risers, impacts multicouches, pre-drop fills, stutters, tape-stops, delay/reverb throws et automations sur 1/2/4/8 mesures pour Pop/Electro/Minimal House/Tech House/Bass House/Future House/Techno. Utilise Ableton Live 12, Serum 2 et, quand leur fonction est justifiée, Waves, FabFilter, iZotope, Native Instruments et Valhalla. Sépare [DOC], [ANALYSIS], [HEUR] et [TEST].
---

# Transitions & FX Director — v15

Ce skill traite la transition comme une **fonction d'arrangement**, pas comme une collection de bruitages. Une transition doit annoncer, masquer, relier, surprendre ou libérer l'énergie entre deux sections.

## Hiérarchie de preuve
- `[DOC]` : comportement confirmé par documentation constructeur.
- `[ANALYSIS]` : conclusion issue de l'analyse d'un morceau/projet.
- `[HEUR]` : méthode de production ou valeur de départ.
- `[TEST]` : choix à valider dans le vrai Set.

## Intake minimum
Déterminer :
- section A → section B ;
- durée disponible : 1/2 / 1 / 2 / 4 / 8 mesures ;
- fonction : `ANNOUNCE`, `LIFT`, `DROP`, `MASK`, `TURNAROUND`, `IMPACT`, `VACUUM`, `EAR-CANDY` ;
- niveau de tension de départ et d'arrivée ;
- élément principal qui doit rester lisible ;
- ownership du grave (`KICK`, `BASS`, `RUMBLE`, aucun) ;
- quantité de spectaculaire souhaitée : subtil / moyen / maximal ;
- palette autorisée : natif / Serum / plugins tiers / resampling.

## Pipeline obligatoire

### 1. Define the boundary
Lire `references/transition-taxonomy.md`.

Décrire la frontière en une phrase :
`A loses X → transition creates Y → B reveals Z`.

Exemple : `break émotionnel perd le sub → 4 mesures de tension filtrée + vocal tail → silence 1/4 beat → drop sec` `[HEUR]`.

### 2. Choose the timescale
Lire `references/time-scale-1-2-4-8-bars.md`.

- 1/2–1 mesure : fill, reverse, stop, micro-stutter, silence, impact cue.
- 2 mesures : turnaround, pitch/filter sweep, delay throw, mini-build.
- 4 mesures : riser complet, densification, automation multi-paramètre.
- 8 mesures : narration de build, superposition progressive, variations par paliers.

Les durées sont des cadres `[HEUR]`, pas des règles de genre.

### 3. Pick transition families
Utiliser au maximum 2–4 familles principales :
`NOISE`, `TONAL`, `RHYTHMIC`, `REVERSE`, `IMPACT`, `SPACE`, `GLITCH`, `SILENCE`.

Éviter un riser + reverse cymbal + snare roll + vocal throw + white noise + pitch rise + reverb bloom si aucun n'a de fonction distincte.

### 4. Choose engine by function
Lire `references/native-ableton-transition-toolbox.md` et `references/serum2-transition-design.md`.

**Ableton Live 12** `[DOC]` :
- Auto Filter : sweeps LFO/envelope/sidechain ;
- Beat Repeat : répétitions tempo-sync, pitch decay et modes Mix/Insert/Gate ;
- Grain Delay : grains retardés et repitchés ;
- Echo : delay + modulation LFO/envelope follower ;
- Hybrid Reverb : convolution + algorithmique, y compris IR utilisateur ;
- Shifter : pitch/frequency shifting et delay pour couches métalliques/glitch ;
- Spectral Time : freeze, spectral delay et frequency shifting ;
- Redux : downsampling/bit reduction ;
- Roar : saturation multi-étage + feedback ;
- Utility/automation : gain/width/phase selon besoin.

**Serum 2** `[DOC]` :
- Wavetable/Sample/Granular/Spectral pour sweeps et textures ;
- pitch tracking peut être désactivé pour noise FX, risers, sweeps et impacts ;
- oscillateurs et filtres peuvent être routés vers Filter/Main/Direct/None et vers les buses ;
- LFO/envelopes assignables à de nombreux contrôles pour construire des mouvements reproductibles.

### 5. Design the curve, not just the endpoint
Lire `references/automation-curves.md`.

Pour chaque mouvement préciser :
`START → SHAPE → END → RESET`.

Exemples `[HEUR]` :
- cutoff : lent puis accéléré ;
- pitch : exponential rise ;
- feedback : faible → montée courte → coupure avant downbeat ;
- reverb send : bloom puis hard mute/duck ;
- stutter rate : valeurs de plus en plus rapides ;
- width : centre → large, puis recentrer l'impact si le grave revient.

### 6. Pre-drop vacuum
Lire `references/pre-drop-fill-and-vacuum.md`.

Le silence est une vraie couche. Avant un drop :
- identifier ce qui doit disparaître ;
- nettoyer sub/rumble/tails ;
- décider si la dernière information est `FILL`, `VOCAL`, `REVERSE`, `STUTTER` ou `SILENCE` ;
- laisser le premier transient du drop respirer.

### 7. Impact architecture
Lire `references/impact-layering.md`.

Architecture possible `[HEUR]` :
`TRANSIENT + BODY + SUB + TONAL + TAIL + DEBRIS`.

N'activer que les couches qui ont une fonction. Si le kick du downbeat possède déjà le sub, le layer SUB de l'impact doit être raccourci, filtré ou supprimé `[HEUR+TEST]`.

### 8. Third-party selection
Lire les fichiers constructeur dédiés.

- **FabFilter Timeless 3** `[DOC]` : Freeze modulable, ping-pong, Tape/Stretch read modes, pitch shift dans/hors feedback, diffusion/lo-fi/dynamics.
- **Volcano 3** `[DOC]` : filtres modulables, XLFO sync, EG/EF/MIDI/XY.
- **Pro-R 2** `[DOC]` : Freeze, Ducking, Auto Gate, predelay sync, Decay Rate EQ.
- **Waves MetaFilter** `[DOC]` : LFO, sequencer 1–16 steps, envelope/sidechain, delay, saturation/bitcrush.
- **Waves H-Delay** `[DOC]` : ping-pong, feedback, LP filter, tempo-sync et caractère variable-pitch lors des changements de délai.
- **Waves SoundShifter** `[DOC]` : time scaling et pitch shifting indépendants.
- **iZotope Stutter Edit 2** `[DOC]` : Buffer, Stutter, Rate/Quantization et Gestures MIDI.
- **NI Guitar Rig Transpose Stretch** `[DOC]` : granular time-stretch/pitch avec freeze jusqu'à un grain.
- **ValhallaDelay** `[DOC]` : Reverse Pitch, Pitch, ducking, diffusion, feedback, beat sync.
- **Supermassive** `[DOC]` : algorithmes avec attaques/densités/decays très variables et contrôle Warp.

Règle : un plugin tiers n'entre que s'il apporte une fonction non déjà remplie proprement par la chaîne native.

### 9. Resample destructive complexity
Lire `references/resampling-and-printing.md`.

Resampler lorsque :
- feedback/freeze devient difficile à rappeler ;
- le geste dépend d'une performance temps réel ;
- plusieurs effets créent une texture qu'il vaut mieux éditer comme audio ;
- il faut inverser, découper ou recaler précisément le résultat.

Conserver une version dry + une version processed imprimée.

### 10. Bridge handoff
Lire `references/bridge-macro-map.md`.

Transmettre de préférence les 8 macros stables :
`TONE`, `MOTION`, `BITE`, `WEIGHT`, `WIDTH`, `SPACE`, `ATTACK`, `VARIATION`.

Une automation complexe doit être exprimée en intention musicale avant d'être convertie en paramètres Live/Serum.

### 11. Validate
Lire `references/validation-checklist.md`.

Obligatoire :
- la transition améliore-t-elle la perception de la frontière ?
- le downbeat suivant paraît-il plus fort même à volume égal ?
- le grave est-il nettoyé avant l'impact ?
- les tails sont-ils intentionnels ?
- les automations reviennent-elles à un état sûr ?
- le mouvement fonctionne-t-il en mono ?
- la transition reste-t-elle utile sans limiter/master fort ?

## Sortie standard
1. `Boundary Function`
2. `Timescale`
3. `Transition Families`
4. `Sound Sources`
5. `FX Chain with Reasons`
6. `Automation Curves`
7. `Pre-Drop / Post-Impact Cleanup`
8. `Resample Point`
9. `Bridge Macro Plan`
10. `Validation Tests`

## Interdictions
- Ne pas automatiser le master volume comme substitut à l'arrangement.
- Ne pas laisser un feedback >100% sans limite/sécurité et sans test `[DOC+TEST]`.
- Ne pas empiler trois risers qui remplissent la même bande et la même fonction.
- Ne pas supposer qu'une longue reverb est automatiquement « cinématique ».
- Ne pas faire passer une transition au-dessus du hook principal si elle n'est pas elle-même le hook.
