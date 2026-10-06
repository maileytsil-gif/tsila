# Vingt recettes de tearout, de basses métalliques, FM et colour bass pour le Dubstep (famille F11)

Troisième lot Dubstep : la famille la plus agressive. On y trouve le tearout (sustain ou « gun » en rafales), les basses métalliques, la FM qui hurle et la colour bass, une basse dubstep qui joue des accords. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F11-01 et F11-02 (Rocket Powered Sound), F13-02 et F13-03 (Art1fact), F08-01, F08-02, F08-03, F05-02 ;
- `../etudes-pages-dubstep-dnb.md` : F08-04 Monosounds, F02-14 MusicRadar ;
- la recette « Jauz » du corpus `../../../house-future-rave-bass-house-production/recipes/basse-fm-metallique-bass-house.md` et la talking bass du même corpus ;
- `../documentation-basses.md` § 1 et 4 (FM, repliement) et la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot Dubstep** : celles de `dubstep-f10-riddim.md`. Elles couvrent le tempo, le sub séparé, l'OCT −3 des tutoriels, RAND 0 et les effets après Serum.
2. **Le sub ne passe jamais dans la distorsion.** Toute la saturation de ces recettes se fait au-dessus du passe-haut, entre 120 et 150 Hz.
3. **Repliement** : FM forte, warps de repli et distorsions empilées créent des partiels très aigus qui se replient en composantes inharmoniques [`../documentation-basses.md` § 4].
   - Concevoir avec QUALITY sur High (2×) ou Ultra (4×).
   - Vérifier la note la plus aiguë à part.
4. **FM** :
   - 15-25 % = râpe gutturale ; au-delà de 40 % = métallique et criard, bon pour un drop, pénible ailleurs [SOURCE F08-04] ;
   - rapports non entiers = inharmonique (`house-f03-pluck-hollow.md`, règle 3).
5. **Quatre macros communes** :
   - `Metal` : FM, rapport ou résonance métallique ;
   - `Tear` : drive ou repli ;
   - `Gun` : longueur des coups (decay d'ENV 1) ou découpe ;
   - `Color` : filtre, formant ou peigne.

   Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| T01 | Machine gun | gun tearout | ENV 1 courte, Combs, delay de 13 ms |
| T02 | Kung Fu métallique | growl métallique | Squarify, Flanger −, Bandreject |
| T03 | Tearout tenu | sustain | T02 plus long, LFO sur Master Amp |
| T04 | FM croisée | tearout mouvant | A dans B et B dans A |
| T05 | FM Thru-Zero | métal cloche | type de FM Thru-Zero |
| T06 | FM qui hurle | drop | index > 40 %, rapport 6:1 |
| T07 | Colour bass | dubstep mélodique | accords, peigne accordé |
| T08 | Gun bass à chute | gun bass | chute de hauteur par coup |
| T09 | Tearout au baffle | tearout sale | Convolve Cab + distorsion |
| T10 | Overdrive à étages | tearout organique | « stacks » élevés |
| T11 | Hard Clip modulé | tearout à pulsation | LFO sur le MIX |
| T12 | Rectify | tearout aigre | Rectify au maximum sur B |
| T13 | Repli | tearout brillant | Linear Fold, Sine Fold |
| T14 | Downsample | tearout numérique | Downsample, SampHold |
| T15 | Delays pitchés | métal mouvant | Bode et FEED |
| T16 | Distorsion par bandes | tearout propre | Splitter L/M/H |
| T17 | Bruit dans la distorsion | fizz | NOISE avant la distorsion |
| T18 | Phaser métallique | métal | phasers figés, feedback |
| T19 | Peigne spectral | métal | warp spectral de peigne |
| T20 | Tearout imprimé et découpé | toutes | minutes imprimées, meilleures prises |

## Les vingt recettes

### T01 Machine gun — la rafale vient de l'enveloppe
- **Patch** :
  - Tout allumer et empiler des sources qui se heurtent :
    - NOISE ≈ 72 (écran : « AC hum1 », lecture incertaine) ;
    - OSC A sur la table Spectral « Creeper [SN] » ;
    - OSC B en carrée (Basic Shapes) à faible niveau.
  - FILTER 1 en Combs sur A et B : CUTOFF ≈ 425 Hz, RES ≈ 98, DRIVE au fond, DAMP monté pour corriger le timbre.
- **ENV 1 (écran)** : attaque ≈ 0,5 ms, hold 0, decay 116 ms, sustain −∞, release 52 ms. Le « machine gun » vient de là, pas d'un LFO ; le rythme se dessine avec les notes MIDI.
- **FX** :
  1. Distortion Tube, MIX 50 %.
  2. Filter Combs, RES haute.
  3. Phaser : RATE 0, DEPTH 0, FREQ 0, un peu de FEEDBACK (« effet guitare »).
  4. Hyper/Dimension (UNISON 4), Compressor Multiband.
  5. Delay court : LINK, BPM désactivé, ≈ 12,87 / 12,79 ms, MIX monté (teinte métallique).
  6. Passe-haut à 150 Hz ajouté [ORIGINAL].
- **Calcul** : un delay de 12,87 ms réinjecté fait un peigne de pics espacés de 77,7 Hz [CALCUL].
- **Macros** : `Metal` RES du Combs · `Tear` DRIVE de la Tube · `Gun` decay d'ENV 1, 60 → 200 ms · `Color` temps du Delay, 8 → 20 ms.
- **Sub associé** : S11 de `house-f01-sub.md` (court), recalé à 140 BPM, ou aucun.
- **Jeu** : bloc « Dubstep 140 — rafales » ci-dessous.
- **Origine** :
  - [SOURCE F11-01, transcription et deux captures, Serum 1] ;
  - post-traitement de la source hors Serum : Multipass (Kilohearts) en façon OTT.

### T02 Kung Fu métallique — tout dans Serum
- **Patch** :
  - **OSC A** : table « Phase Werb [SL] » (lecture incertaine), Unison 4, DETUNE très bas, RAND 0 : un étirement « riddim ».
    - Menu de la table : Process › Squarify, pour un son plus carré.
  - **LFO 1** : montée raide, plateau, descente, Trig, 1/4 → WT POS d'A (au-delà du bout de course) et → LEVEL d'A.
  - **OSC B** : table Spectral « Monster 4 [SL] » pour le grave « de gorge », warp Mirror, Unison 6, detune, RAND 0. LFO 1 → WT POS de B jusqu'à mi-course.
  - **FILTER 1** en Flanger − sur A et B : RES 50, key track, CUTOFF 649 Hz (valeur tapée), MIX ≈ 50 %, que LFO 1 pousse à 100 %.
- **ENV 1** : non dite. Attaque 1 ms, sustain 100 %, release 60 ms [ORIGINAL].
- **FX** :
  1. Hyper 34, Dimension taille 1-3 % puis MIX.
  2. Compressor Multiband et gain.
  3. Equalizer : bande haute en passe-bas, Q ≈ 39, fréquence ≈ 222 Hz modulée vers le haut (un passe-bas fait avec l'EQ).
  4. Filter Bandreject : CUTOFF ≈ 93 Hz modulé +30, largeur ≈ 80 modulée vers ≈ 76, RES : effet de voix « qui parle ».
  5. Delay court : LINK, BPM désactivé, ≈ 1360 (unité non dite), MIX et FEEDBACK montés.
- **Macros** : `Metal` RES du flanger · `Tear` MIX du flanger · `Gun` LFO 1 → LEVEL · `Color` CUTOFF du Bandreject.
- **Sub associé** : S01. Le passe-bas d'EQ à 222 Hz laisse peu de médium : vérifier que la couche reste au-dessus du sub.
- **Origine** : [SOURCE F11-02, transcription et deux captures, Serum 1] ; « aucun traitement externe, tout dans Serum ».

### T03 Tearout tenu — LFO sur Master Amp
- **Patch** :
  - T02 avec des notes longues ;
  - LFO 1 sur Global › Master Amp (le volume après les effets) : la pulsation contourne compresseur et delay ;
  - ENV 1 avec un sustain plein.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 120 ms.
- **Macros** : `Gun` LFO 1 → Master Amp, de 0 à −100 · les autres comme T02.
- **Sub associé** : S10, creux calé sur le kick.
- **Jeu** : bloc « Dubstep 140 — tearout tenu » ci-dessous.
- **Origine** : LFO 1 sur Global Master Amp, après les effets [SOURCE F11-02, 12:01] ; variante tenue [ORIGINAL].

### T04 FM croisée — A dans B et B dans A
- **Patch** :
  - OSC A et OSC B en sinus (Default Shapes) : A à OCT −2, B à OCT −1 (−3 et −2 en dubstep grave). Tous deux un peu désaccordés : FIN visible sur A, ≈ 31, illisible avec certitude.
  - Phases différentes : ≈ 136° et ≈ 232° (écran).
  - Warps doubles : A en Diode 1 + FM (B) ; B en Tube + FM (A).
  - Quantités de FM vers 20 % et 15 % ; 21 % donne déjà un autre rythme.
  - Le rythme vient de la phase de départ des deux sinus, la vitesse du mouvement du fine tune.
  - NOISE « Paper Bag », PITCH au maximum (bruit granuleux pour les aigus).
  - FILTER 1 en pic ou encoche avec drive, FILTER 2 en encoche sur une autre zone, modulés en sens inverse par un seul LFO (triangle, Retrig, 2 mesures) ; MIX du filtre 2 baissé.
- **ENV 1** : non dite. Attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** :
  1. Bode, BLUR monté, léger décalage, MIX ≈ 20 %.
  2. Hyper/Dimension discret.
  3. Chorus, MIX ≤ 25 %.
  4. Splitter L/H : Distortion Overdrive dans HIGHS, SPLIT FREQ ≈ 197 Hz sous LFO 1 (de ≈ 200 à ≈ 650 Hz).
  5. Delay ping-pong et Reverb vers 10 % chacun.
- **Macros** : `Metal` les deux quantités de FM · `Tear` DRIVE de l'Overdrive · `Gun` FIN de B (vitesse du mouvement) · `Color` profondeur du LFO sur les encoches.
- **Sub associé** : S01. Le patch d'origine est un mono puissant ; la stéréo vient après.
- **Origine** :
  - [SOURCE F13-02, Art1fact, neurofunk, Serum 2] : la FM croisée est une nouveauté de Serum 2 ;
  - usage en tearout dubstep [ORIGINAL].

### T05 FM Thru-Zero — métal de cloche
- **Patch** :
  - OSC A en sinus, OCT −2, RAND 0. OSC B en sinus, Ratio 3.5 (non entier), LEVEL 0.
  - WARP 1 d'OSC A en FM (B), type Thru-Zero s'il est proposé, base 20 %.
  - ENV 2 → warp +40 %, decay 100-200 ms, sustain 0 : le spectre inharmonique retombe vers la porteuse.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 60 %.
- **ENV 1** : attaque 1 ms, decay 400 ms, sustain −10 dB, release 60 ms.
- **FX** : Distortion Diode 1, passe-haut à 150 Hz, Compressor Multiband.
- **Macros** : `Metal` Ratio de B (presets 2,5 / 3,5 / 4,5) · `Tear` DRIVE · `Gun` decay d'ENV 2 · `Color` CUTOFF.
- **Sub associé** : S01.
- **Origine** :
  - Thru-Zero : « riche, métallique, cloches » [cartographie, § 4.2] ;
  - cloche = non entier ≥ 4 avec enveloppe rapide sur le modulateur ; ratios 2:5 inharmonique, 3:7 complexe [SOURCE recette Jauz du corpus, `[DOC-2]`] ;
  - recette [ORIGINAL].

### T06 FM qui hurle — index au-delà de 40 %
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - OSC B en sinus, OCT +2, SEM +7 (≈ 6:1, à −1,96 cent), LEVEL 0.
  - WARP 1 d'OSC A en FM (B), base 40 %, LFO 1 (1/2, RETRIG) → warp +30 %.
  - FILTER 1 en Band 24, CUTOFF ≈ 1 kHz, RES 20 %.
  - QUALITY sur Ultra.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion Hard Clip, Equalizer (passe-haut à 150 Hz, −4 dB vers 3-5 kHz), Compressor Multiband.
- **Macros** : `Metal` WARP 1, 20 → 80 % · `Tear` DRIVE · `Gun` LFO 1 → warp · `Color` CUTOFF.
- **Sub associé** : S01.
- **Test** : la note la plus aiguë révèle d'abord le repliement ; si elle crisse, baisser `Metal` sur cette note par automation.
- **Origine** :
  - « au-delà de 40 % = métallique et criard (bon pour un drop, pénible ailleurs) » [SOURCE F08-04] ;
  - rapport 6:1 (2 octaves + 7 demi-tons) [SOURCE F05-12 ; CALCUL] ;
  - recette [ORIGINAL].

### T07 Colour bass — des accords dans la basse dubstep
- **Patch** :
  - VOICING POLY 4 (pas MONO) : la couche joue des accords de trois notes au-dessus du sub.
  - OSC A sur une table vocale ou Basic Shapes en scie, OCT −1, RAND 0, Unison 1 (plusieurs voix d'unison par note brouilleraient l'accord).
  - FILTER 1 en Cmb HL6+, key track allumé (le peigne suit chaque note de l'accord), RES 30-45 %.
  - LFO 1 (RETRIG, 1/4) → CUTOFF ±½ octave.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Overdrive légère (une distorsion forte sur un accord crée de l'intermodulation), Compressor Multiband, passe-haut à 80 Hz, juste sous la note la plus grave des accords (fa 2, 87,3 Hz).
- **Macros** : `Metal` RES du peigne · `Tear` DRIVE · `Gun` decay d'ENV 1 · `Color` profondeur de LFO 1.
- **Sub associé** : S01, sur la **fondamentale** de l'accord seulement.
- **Jeu** : bloc « Dubstep 140 — colour bass en accords » ci-dessous.
- **Test** : l'accord doit rester lisible malgré la distorsion. Si les notes se brouillent, baisser le drive ou retirer la tierce.
- **Origine** :
  - [ORIGINAL] : la masterclass colour bass du registre (F11-03) n'est pas étudiée ;
  - intermodulation dans la distorsion : thème signalé sans source lue (`../documentation-basses.md` § 7).

### T08 Gun bass à chute — un coup, une chute
- **Patch** :
  - T01, avec ENV 3 → CRS d'OSC A et d'OSC B : +12 → 0 en 30-50 ms (le « coup »).
  - NOISE en White, ENV 4 → LEVEL, decay 10 ms (la détonation).
- **ENV 1** : attaque 0,5 ms, decay 90 ms, sustain −∞, release 40 ms.
- **FX** : comme T01.
- **Macros** : `Metal` RES du Combs · `Tear` DRIVE · `Gun` ENV 3 → CRS, 0 → +24 · `Color` LEVEL du NOISE.
- **Sub associé** : aucun.
- **Origine** :
  - base « machine gun » [SOURCE F11-01] ;
  - chute brève façon « thwack » +12 → 0 en 50 ms [SOURCE recette Jauz du corpus] ;
  - recette [ORIGINAL]. Le guide « gun bass » du registre (F11-04) n'est pas lu.

### T09 Tearout au baffle — Convolve Cab
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0. FILTER 1 en Low 24, ENV 2 → CUTOFF.
  - FX :
    1. Convolve, IR Factory › Cab (« Cab 2 »), IR GAIN ≈ −8,6 dB, SIZE réduite.
    2. Distortion avec pré-filtre passe-haut.
    3. Compressor Multiband (BELOW) : −18,1 dB, 4:1, 90,1 / 90,1, gain 9,5.
    4. Filter SampHold avec RES.
    5. Distortion Overdrive en second étage.
- **ENV 1** : sustain bas, decay tiré.
- **Macros** : `Metal` RES du SampHold · `Tear` DRIVE du second étage · `Gun` decay d'ENV 1 · `Color` CUTOFF du SampHold.
- **Sub associé** : S01.
- **Origine** : chaîne de P04 de `house-f05-saw-percussive.md` [SOURCE F05-02], poussée en tearout par un second étage de distorsion [ORIGINAL].

### T10 Overdrive à étages — tearout organique
- **Patch** :
  - OSC A en carrée (Basic Shapes), OCT −2, Unison ≈ 3, detune lent. Warp Asym +.
  - Distortion Overdrive avec des « stacks » (étages) élevés : les timbres changent beaucoup selon le nombre d'étages.
  - Contre le clic d'attaque : ENV 1 → MIX et → DRIVE de la distorsion, puis FILTER 1 en passe-bas ouvert par une enveloppe lente (écran : ENV 2 attaque ≈ 296 ms, sustain 50 %).
  - LFO 2 (décroissant, Retrig, 1/4) → WT POS ; LFO 3 (triangle, 1 mesure) plus lent.
  - FILTER 2 en Reverb avant la distorsion.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX, dans l'ordre vu à l'écran** :
  1. Distortion.
  2. Filter.
  3. Hyper/Dimension.
  4. Filter (Bandreject).
  5. Splitter L/H, avec Convolve « Digital Gated » à ≈ 30 % dans les aigus.
  6. Equalizer : léger boost des médiums.
  7. Passe-haut à 150 Hz ajouté [ORIGINAL].
- **Macros** : `Metal` warp Asym + · `Tear` nombre d'étages (presets) ou DRIVE · `Gun` attaque d'ENV 2 · `Color` LFO 3 → mix du filtre.
- **Sub associé** : S01.
- **Origine** :
  - [SOURCE F13-03, Art1fact, séance improvisée, Serum 2, 174 BPM] ;
  - « chaque relance donne un mouvement différent : enregistrer plusieurs prises » (voir T20).

### T11 Hard Clip modulé — tearout à pulsation
- **Patch** :
  - OSC A sur une table riche, OCT −3, RAND 0. LEVEL 0 % et LFO 1 → LEVEL (pentes dessinées, 1 mesure).
  - WARP 1 en Bend −.
  - FILTER 1 en High Notch 12, DRIVE et RES montés.
  - FX : Distortion Hard Clip, DRIVE monté, LFO 1 → MIX.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Filter Diffusor, Hard Clip, Compressor Multiband ×3, Equalizer final (graves retirés).
- **Macros** : `Metal` Bend − · `Tear` DRIVE du Hard Clip · `Gun` LFO 1 → MIX · `Color` CUTOFF du High Notch.
- **Sub associé** : S01.
- **Origine** : Hard Clip, LFO 1 → mix, High Notch 12, OTT ×3 [SOURCE F08-02, Konstricta] ; usage en tearout [ORIGINAL].

### T12 Rectify — tearout aigre
- **Patch** :
  - OSC A en scie (Default Shapes), OCT −3, RAND 0. WARP en PD (B).
  - OSC B en triangle (Basic Shapes), Unison 3, warp Distortion Rectify au maximum.
  - LFO (1/4, RETRIG) → quantité de PD (≈ 35).
  - FILTER 1 en Diffusor, CUTOFF 118, STAGES 72-75.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **FX** : Overdrive, Chorus HPF, Combs, Equalizer (creux à 437 Hz, Q 60, −17,6 dB), Compressor Multiband.
- **Macros** : `Metal` PD · `Tear` Rectify de B · `Gun` LFO → PD · `Color` STAGES du Diffusor.
- **Sub associé** : S01.
- **Origine** : [SOURCE F08-03, DNB Academy] : même patch que G05 de `house-f08-growl.md`, poussé vers le Rectify.

### T13 Repli — Linear Fold et Sine Fold
- **Patch** :
  - OSC A en sinus, OCT −2, RAND 0.
  - WARP 1 en Linear Fold, base 20 %. WARP 2 en Sine Fold, base 10 %.
  - LFO 1 (RETRIG, 1/4) → les deux warps (+40 %).
  - FILTER 1 en MG Low 24, CUTOFF 4-6 kHz. QUALITY sur Ultra.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **FX** : Compressor Multiband, passe-haut à 150 Hz.
- **Macros** : `Metal` Linear Fold · `Tear` Sine Fold · `Gun` LFO 1 · `Color` CUTOFF.
- **Sub associé** : S01.
- **Origine** :
  - Linear Fold = repli métallique, Sine Fold = repli sinusoïdal [cartographie, § 4.2] ;
  - repliement [`../documentation-basses.md` § 4] ;
  - recette [ORIGINAL].

### T14 Downsample — tearout numérique
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0. FILTER 1 en MG Low 24, CUTOFF ≈ 50 %.
  - FX :
    1. Distortion Downsample (le DRIVE réduit la fréquence d'échantillonnage), MIX 50-100 %.
    2. Filter SampHold, RES (la RES baisse la résolution).
    3. LFO 1 (1/8, RETRIG) → DRIVE du Downsample.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Compressor Multiband, passe-haut à 150 Hz.
- **Macros** : `Metal` RES du SampHold · `Tear` DRIVE du Downsample · `Gun` LFO 1 → DRIVE · `Color` CUTOFF du SampHold.
- **Sub associé** : S01.
- **Origine** :
  - Downsample [cartographie, § 8] ;
  - SampHold : la coupure baisse la fréquence d'échantillonnage, la résonance baisse la résolution, son « Atari » [SOURCE F05-02] ;
  - recette [ORIGINAL].

### T15 Delays pitchés — Bode et feedback
- **Patch** :
  - T02 ou T06, plus un module Bode en fin de chaîne : SHIFT ±20-60 Hz, DELAY court (20-60 ms), FEED 40-70 % (delay réinjecté dans le shifter : delays « pitchés »), MIX 20-35 %.
  - LFO 2 (1/2, RETRIG) → SHIFT.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Color` FEED du Bode · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Test** : la queue réinjectée doit s'éteindre avant la note suivante.
- **Origine** : Bode, FEED « delay réinjecté dans le shifter → delays pitchés » [cartographie, § 8] ; recette [ORIGINAL].

### T16 Distorsion par bandes — tearout propre
- **Patch** :
  - T06 ou T02, avec un Splitter L/M/H en premier dans les FX :
    - sous 120 Hz : rien, bande coupée ensuite par le passe-haut ;
    - de 120 Hz à 2 kHz : Tube puis Hard Clip (waveshaping lourd) ;
    - au-dessus de 2 kHz : Tube seul.
  - Puis Compressor Multiband et coupe-bas à 100-150 Hz.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Tear` DRIVE de la bande médiane · les autres comme la recette de départ.
- **Sub associé** : S01, en `Direct`, sur sa piste.
- **Origine** : chaîne Splitter L/M/H (< 120 Hz propre, 120 Hz-2 kHz Tube puis Hard Clip, > 2 kHz Tube) [SOURCE talking bass du corpus].

### T17 Bruit dans la distorsion — le fizz
- **Patch** :
  - T02 ou T10, plus le NOISE (White, ou une texture d'usine), routé `Main`, LEVEL bas.
  - Le bruit passe dans la distorsion finale.
  - Variante : WARP 2 d'OSC A en FM (Noise), 5-10 %.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Color` LEVEL du NOISE · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Origine** :
  - oscillateur Noise poussé dans l'étage final de distorsion (le « fizz ») [SOURCE F02-14] ;
  - noise bas à travers la distorsion [SOURCE F13-03] ;
  - FM depuis le noise, « fizz » pour growl et neuro [SOURCE F03-04].

### T18 Phaser métallique — phasers figés
- **Patch** : T04 ou T06, plus deux Phaser figés (RATE au minimum, DEPTH 0, 4 pôles), FREQ 205 Hz et ≈ 800 Hz, FEEDBACK 50-70 %, après la distorsion.
  - Un troisième phaser à FEEDBACK bas en fin de chaîne.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Metal` FEEDBACK des phasers · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Origine** : phasers figés (seules fréquence et feedback, 4 pôles, FREQ 205 Hz à l'écran), troisième phaser à feedback bas [SOURCE F08-01].

### T19 Peigne spectral
- **Patch** :
  - OSC A en moteur Spectral, sur une table ou un sample riche, OCT −2.
  - Un warp spectral de peigne (`kSpectralComb` dans le binaire ; libellé affiché à lire dans l'interface), quantité sous LFO 1 (RETRIG, 1/4).
  - Volet FREQ LO pour couper le grave du moteur. QUALITY sur High.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion Overdrive, Compressor Multiband, passe-haut à 150 Hz.
- **Macros** : `Metal` quantité du peigne spectral · `Tear` DRIVE · `Gun` LFO 1 · `Color` FREQ LO.
- **Sub associé** : S01.
- **Origine** :
  - warps spectraux, dont `kSpectralComb` ; libellés affichés non documentés [cartographie, § 4.3] ;
  - recette [DÉDUCTION].

### T20 Tearout imprimé et découpé — garder les meilleures prises
- **Patch** :
  1. Construire T02, T04 ou T10, LFO en mode FREE (chaque note bouge autrement).
  2. Imprimer plusieurs minutes d'un riff en audio (procédure de `../../../resampling/SKILL.md`).
  3. Découper les meilleures prises et les rejouer en audio ou dans Simpler (instrument natif toléré).
  4. Varier les phases des LFO et le detune entre deux impressions.
- **Macros** : aucune ; le travail se fait en audio.
- **Sub associé** : S01, en MIDI, jamais imprimé avec le tearout.
- **Test** : A/B entre deux prises à niveau égal ; garder celles qui tiennent sur la caisse claire.
- **Origine** :
  - imprimer plusieurs minutes d'un riff et découper les meilleures prises [SOURCE F02-14] ;
  - chaque relance donne un mouvement différent [SOURCE F13-03].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f11-tearout-metal.md`.

```grille
titre: Dubstep 140 — rafales (T01, T08)
tempo: 140
accords: Fm7 | Fm7
gun: F1[1:1] F1[1e:1] F1[1&:1] F1[2:1] F1[2e:1] F1[2&:1] F1[2a:1] Ab1[3e:1] F1[4:1] F1[4e:1] F1[4&:1] | F1[1:1] F1[1e:1] F1[1&:1] Eb1[2:1] Eb1[2e:1] Eb1[2&:1] F1[3e:1] F1[3&:1] C2[4:1] Ab1[4&:1] F1[4a:1]
```

Rafales de doubles croches ; la caisse claire du temps 3 reste libre. ENV 1 courte (decay 116 ms) : chaque note d'une double croche (107,1 ms) s'éteint presque avant la suivante [CALCUL].

```grille
titre: Dubstep 140 — tearout tenu (T02, T03)
tempo: 140
accords: Gm7 | Gm7
tear: G1[1:8] Bb1[3e:3] G1[4:4] | G1[1:6] F1[2a:2] D1[3e:7]
sub: G0[1:8] Bb0[3e:3] G0[4:4] | G0[1:6] F0[2a:2] D1[3e:7]
```

Tenues longues sous la pulsation de LFO 1 sur Master Amp (T03).

```grille
titre: Dubstep 140 — colour bass en accords (T07)
tempo: 140
accords: Fm9 | Dbmaj7
colour: F2+Ab2+C3[1:6] F2+Ab2+Eb3[2&:2] F2+Ab2+C3[3e:7] | F2+Ab2+Db3[1:6] F2+Ab2+C3[2&:2] F2+Ab2+Db3[3e:7]
sub: F0[1:8] F0[3e:7] | Db1[1:8] Db1[3e:7]
```

Le sub ne joue que les fondamentales (fa, puis ré bémol). Les accords restent au-dessus de fa 2 (87,3 Hz) ; dans la mesure 2, l'accord de ré bémol est renversé pour ne pas descendre sous ce seuil.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « Creeper [SN] », « Phase Werb [SL] » et « Monster 4 [SL] » ;
  - le menu Process › Squarify et le bruit « Paper Bag » ;
  - les filtres Flanger −, Bandreject, Diffusor, High Notch 12 et SampHold ;
  - le type de FM Thru-Zero et le warp spectral de peigne.

  Vérifier les destinations des macros.
- Regarder sur le Mac les tutoriels tearout, gun bass et colour bass du registre (F11-03 à F11-16) pour confirmer T07 et T08.
- Écouter chaque recette avec le sub, le kick et la caisse claire, à niveau égal, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
