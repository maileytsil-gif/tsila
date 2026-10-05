# Captures d'écran des tutoriels écrits de basses Serum : valeurs lues

Relevé du 05/10/2026, en session cloud, par un sous-agent de Claude Code. Il complète `etudes-pages-house.md` et `etudes-pages-dubstep-dnb.md` ; identifiants : registre `tutoriels-a-consulter.md`. Contrôle croisé par la session principale sur deux images : Env 1 de F01-06 (188 ms / 0.0 ms / 507 ms / −2.1 dB / 1.98 s) et Compressor de F01-13 (4:1, 5 ms, 70 ms, seuil −32.1 dB) relus à l'identique.

Méthode :
- Chaque page a été récupérée par `curl`. Les images de contenu ont été extraites des balises `<img>` (`src`, `data-src`, `srcset`) et téléchargées (images non conservées dans le dépôt ; noms de fichiers cités pour retrouver la capture sur la page).
- Les webp ont été convertis en PNG avec ffmpeg. Les petites zones ont été agrandies par crop et scale .
- Les images ont ensuite été ouvertes une à une.

Conventions :
- **Image lue ne veut pas dire son entendu.** Aucun audio ni aucune vidéo n'a été écouté (règle 4 d'`AGENTS.md`).
- **Valeur affichée** : nombre écrit dans l'interface (champ, info-bulle, étiquette). On peut le reprendre tel quel.
- **Position visible ≈ x % (estimation visuelle)** : bouton sans nombre affiché, estimé par l'angle de l'aiguille.
  - Course supposée : de 7 h 30 (0 %) à 16 h 30 (100 %), soit 270°. 9 h ≈ 17 %, 10 h ≈ 28 %, 11 h ≈ 39 %, 12 h ≈ 50 %, 14 h ≈ 72 %, 16 h ≈ 94 %.
  - L'estimation n'est donnée que si l'aiguille est nette. Ce n'est **pas** une valeur à reprendre telle quelle.
- **Notes MIDI** : lues dans le piano roll de Live, notation de Live (C3 = 60). Les positions sont données en mesure.temps.double-croche, la durée en double-croches (dc).
- Les noms de contrôles sont laissés en anglais, tels qu'ils s'affichent.

Domaines bloqués : le CDN de MusicRadar (`cdn.mos.cms.futurecdn.net`) est refusé par le proxy (`connect_rejected`). Les captures de **F01-12, F02-14, F07-23 et F13-11** n'ont donc pas pu être lues.

---

### F01-06 808 Bass with Saturation (Attack Magazine)
- **Images lues : 13** :
  - `serum-screen-shot-e1496773834314.jpg` ;
  - `Screen-Shot-2017-06-06-at-13.24.30.png`, `13.26.33`, `13.38.44`, `13.29.48-1`, `unnamed-4.png`, `13.46.01`, `13.48.33`, `13.54.07`, `13.59.54`, `14.04.14`, `14.02.40`, `14.07.28` ;
  - zooms `zoom-*.png`.
  - Les images de la page passent par `i0.wp.com`. Elles ont été prises directement sur `www.attackmagazine.com/wp-content/uploads/…`.
- **Interface** : **Serum 1** (onglets OSC / FX / MATRIX / GLOBAL, logo « SERUM »).
- **Valeurs lues** :
  - **13.24.30 → OSC A, table** : menu Analog › **Analog_BD_Sin** (coché). Filtre par défaut **MG Low 12**. Env 1 par défaut 0.5 ms / 0.0 ms / 1.00 s / 0.0 dB / 15 ms.
  - **13.26.33 → OSC A** : Unison **1**. Detune, Blend et Rand au minimum (aiguilles à 7 h 30), conforme au texte. Phase à 12 h. Level ≈ 14 h (valeur par défaut, estimation visuelle).
  - **13.38.44 → ENV 1 (amplitude)**, valeurs affichées : Attack **188 ms**, Hold **0.0 ms**, Decay **507 ms**, Sustain **−2.1 dB**, Release **1.98 s**.
    - Au zoom, « 188 ms » se lit sans point décimal. Une attaque aussi lente surprend pour une 808, mais c'est ce qui est affiché. Le texte parle d'une « attaque plus lente contre les clics ».
  - **unnamed-4 → ENV 2** (capture corrigée le 03/07/2017), valeurs affichées : Attack **0.2 ms**, Hold **18 ms**, Decay **192 ms**, Sustain **0.00 %**, Release **512 ms**.
  - **13.29.48-1 → ENV 2 → OSC A** : info-bulle « Env 2 Source / Destinations: **A Semi** ». La capture montre encore les valeurs par défaut (0.5 ms / 0.0 ms / 1.00 s / 100.00 % / 15 ms) : elle précède le réglage.
  - **13.46.01 → VOICING** : **MONO** coché, LEGATO décoché, compteur 0 / 1. Le bouton PORTA n'affiche pas de nombre (le texte dit ≈ 300 ms). ALWAYS et SCALED décochés.
  - **13.48.33 → FILTER** : type **MG Low 12**, routage **A** seul. Positions estimées :
    - CUTOFF ≈ 11 h (≈ 39 %) ;
    - RES ≈ 9 h (≈ 17 %) ;
    - DRIVE ≈ 8 h (≈ 6 %) ;
    - FAT ≈ 13 h (≈ 61 %) ;
    - MIX ≈ 100 %.
  - **13.54.07 → FX Distortion** : mode **Tube**. Filtre de la distortion sur **OFF** (case OFF allumée, PRE et POST éteintes). Curseur HP/BP/LP en haut, sur **HP**. Valeurs affichées **F = 644**, **Q = 0.1**. DRIVE ≈ 11 h 45 (≈ 48 %), MIX ≈ 12 h (≈ 50 %).
    - **Contradiction texte/image** : le texte dit d'utiliser le filtre HP pour épargner le sub, mais la capture montre le filtre de la distortion sur OFF.
  - **13.59.54 → OSC A, WT POS** : ≈ 15 h (≈ 83 %), cohérent avec « environ 209 » du texte (209 / 256 ≈ 82 %). Le nombre n'est pas affiché.
    - Sur cette capture, Detune ≈ 12 h, Blend ≈ 14 h et Rand près du maximum. C'est **incohérent avec l'étape 2** (tout à gauche). Avec Unison 1, Detune et Blend n'agissent pas, mais Rand (phase aléatoire) agit.
  - **14.04.14 / 14.02.40 → FabFilter Saturn** (hors Serum), deux bandes **Warm Tape**, Mix 100 %, In 0 dB, Out **−2 dB** :
    - bande basse : DRIVE ≈ 10 h ;
    - bande haute : DRIVE ≈ 12 h ;
    - Dynamics à 12 h, Feedback au minimum.
    - Le séparateur est à la fréquence que le texte donne (123 Hz) ; elle n'est pas affichée sur l'image.
  - **14.07.28 → UAD Neve 31102** (hors Serum) :
    - aigu en étagère sélecteur sur **10 kHz**, gain tourné vers « + » (≈ 10 h) ;
    - médium sélecteur sur **1,6 kHz**, gain tourné nettement vers « + » (≈ 8 h) ;
    - grave sur **off** ;
    - gain d'entrée sur 0.
    - Les dB ne sont pas gradués.
  - **serum-screen-shot (bandeau)** : capture générique de la série (preset « Lead », banque « Vespers ») **sans rapport** avec la recette.
- **Reste illisible** :
  - la **quantité** d'Env 2 vers A Semi (aucun nombre affiché) ;
  - la valeur exacte de PORTA ;
  - les valeurs exactes de cutoff, res, drive et fat du filtre, et du drive et du mix de la distortion ;
  - les gains en dB du Neve ;
  - la fréquence de séparation de Saturn (seul le texte la donne).

### F01-13 Sub-Bass: How To Get Thick Low-End In Your Music (EDMProd)
- **Images lues : 10 sur 16 téléchargées** :
  - `Screen-Shot-2021-11-11-at-3.30.19-pm`, `3.31.18`, `3.33.41`, `3.34.39`, `3.41.14`, `3.54.12`, `3.55.36`, `3.28.27`, `3.17.44`, `3.57.49` ;
  - `Screen-Shot-2021-11-17-at-3.43.15-pm` ;
  - zooms.
  - Non ouvertes : `3.22.06`, `3.36.41`, `3.38.45`, `3.57.14`, `2020-03-12…12.18.49` (échantillon, MIDI transposé, compresseur avant réglage, spectre).
- **Interface** : **Serum 1**. Le DAW est **Ableton Live** (piano roll, Compressor natif).
- **Valeurs lues** :
  - **3.43.15 → piano roll (Power Zone)** : étiquettes **C0, F0, C1** dans le piano roll **de Live**. Le cadre bleu couvre les rangées **F0 à G#0**, son bord haut atteint A0.
    - Cela **tranche la question** laissée ouverte dans `pages-house.md` : la page emploie la notation de Live (C3 = 60). F0-A0 = MIDI **29-33** = **43,7-55 Hz**.
  - **3.30.19 → OSC A** : Init, table **Basic Shapes**, sinus, OCT 0. Filtre par défaut **MG Low 12**, éteint. Env 1 par défaut 0.5 ms / 0.0 ms / 1.00 s / 0.0 dB / 15 ms.
  - **3.31.18 → FX Distortion** : mode **SoftClip**, filtre OFF, **F = 330**, **Q = 2.0** (en partie masqués par une flèche). DRIVE ≈ 15 h 30 (≈ 85-90 %), MIX ≈ 100 %.
    - Le texte parle de saturation « subtile » ; la capture montre un drive haut, en mode Soft Clip.
  - **3.33.41 → OSC A** : Basic Shapes, frame **carré** affichée (WT POS ≈ 11 h).
  - **3.34.39 → FILTER (réglage final du sub carré)** : type **MG Low 24**, routage **A**. Positions estimées :
    - CUTOFF ≈ 10 h 30-11 h (≈ 33-39 %) ;
    - RES ≈ 9 h (≈ 17 %) ;
    - DRIVE et FAT proches du minimum ;
    - MIX ≈ 100 %.
  - **3.41.14 → Compressor de Live en sidechain** (effet natif, règle 5), valeurs affichées :
    - Sidechain allumé, Audio From **Kick / Post FX** ;
    - Ratio **4.00:1**, Attack **5.00 ms**, Release **70.0 ms**, Thresh **−32.1 dB** ;
    - Knee **6.0 dB**, Look **0 ms**, mode **Peak**, Env **Log** ;
    - Out 0.00 dB, Dry/Wet 100 %, Gain 0.00 dB, Mix 100 % ;
    - EQ de sidechain éteint (Freq 200 Hz, Q 0.71 affichés).
    - Le graphe affiche « −22.3 dB » : probablement la réduction de gain, non certain.
  - **3.54.12 → pistes Bass et Sub** (gelées) : les deux à **−6.1 dB**. Les deux formes d'onde montrent l'opposition de phase.
  - **3.55.36 → Serum (sub de renfort)**, valeurs affichées :
    - info-bulle **« A Phase: 178deg. »** ;
    - OSC A Basic Shapes sinus, **OCT −1** ;
    - Env 1 : **3.5 ms / 0.0 ms / 1.00 s / 0.0 dB / 146 ms** ;
    - Macro 1 nommée **« TONE »** (1 destination), Env 2 avec 1 destination, LFO 1 à 1/4 BPM ;
    - filtre allumé, routage A.
  - **3.28.27 → exemple de 808 (preset tiers « 808_Dollar », banque « Production Master »)** :
    - SUB allumé en **DIRECT OUT**, sinus, octave −1 ;
    - OSC A table « Har… » (cachée par une flèche), **OCT −3**, warp **FM (FROM B)** ;
    - OSC B **Harp**, OCT −1 ;
    - filtre **MG Low 12**, routage **A, B et S** ;
    - macros **DISTORTION** et **HARD** (une destination chacune).
  - **3.17.44** : oscilloscope (s(M)exoscope) d'un sinus, Time 0.029, Amp 6.037. Pas de réglage Serum.
  - **3.57.49 → Pro-Q (passe-haut sur un autre instrument)** : Low Cut **263.04 Hz** (C4 +09), **Q 0.955**, **12 dB/oct**.
- **Reste illisible** :
  - le **sous-oscillateur « sinus, triangle, rectangle arrondi »** annoncé par le registre n'apparaît sur aucune capture : seul le sub du preset 808 montre le sélecteur de formes, avec le sinus choisi ;
  - les valeurs exactes de cutoff et de res du sub carré ;
  - le drive exact de la Soft Clip.

### F05-12 How to Make Bass House: The Ultimate Guide (EDMProd)
- **Images lues : 4 sur 8 téléchargées** :
  - `image-58.png`, `image-59.png`, `image-61.png`, `image-63.png` et zooms.
  - Non ouvertes : `image-65`, `67` (presets Splice), `69`, `70` (pitch bend, sans Serum).
- **Interface** : **Serum 1** (ENV / BPM / ANCH, « FM (FROM B) »). DAW : **Live 12** (Scale, Highlight Scale, onglets Notes / Envelopes / MPE).
- **Valeurs lues** :
  - **image-61 → LFO 1 vers le cutoff** :
    - FILTER **MG Low 12** (et non MG Low 24), routage **A** ;
    - au moment de la capture (avant les réglages « à l'oreille » du texte) : CUTOFF ≈ 12 h (≈ 50 %), RES ≈ 8 h 30 (≈ 11 %), DRIVE et FAT ≈ 8 h, MIX 100 % ;
    - LFO 1 : mode **ENV** coché, **BPM** et **ANCH** cochés, TRIG et OFF décochés ;
    - LFO 1 : RATE **1/4**, RISE **Off**, DELAY **Off**, SMOOTH **0.0**, GRID 8 ;
    - forme du LFO : montée rapide jusqu'au sommet vers 15 % du cycle, puis descente presque linéaire jusqu'à zéro (un point intermédiaire sur chaque pente) ;
    - Env 1 : RELEASE **227 ms** (les autres valeurs sont hors cadre) ;
    - VOICING : Mono et Legato décochés, Poly 8.
  - **image-63 → FM** :
    - OSC A table **« BS2 - Subby Saw »**, OCT 0, Unison 1, WARP **FM (FROM B)** ;
    - info-bulle **« A Warp: 28% »** ;
    - OSC B **Basic Shapes** sinus, OCT 0 au moment de la capture (le texte le monte ensuite de 2 octaves et 7 demi-tons), LEVEL au minimum ;
    - LFO 1 a 1 destination, LFO 2 est sélectionné (destination non visible) ;
    - RAND d'OSC A encore près du maximum (le texte dit de le mettre à zéro ensuite).
  - **image-58 → motif de départ** : **E0** seul (MIDI 28, 41,2 Hz), 11 notes, même rythme que l'image 59.
  - **image-59 → motif final** (2 mesures, toutes les notes à la même vélocité) :

    | Position | Note (MIDI) | Durée |
    |---|---|---|
    | 1.1.2 | E0 (28) | 1 dc |
    | 1.1.4 | F0 (29) | 1 dc |
    | 1.2.3 | E0 | 1 dc |
    | 1.3.1 | E0 | 2 dc |
    | 1.3.4 | E0 | 1 dc |
    | 1.4.3 | **B0 (35)** | 2 dc |
    | 2.1.1 | E0 | 2 dc |
    | 2.1.4 | E0 | 1 dc |
    | 2.2.3 | E0 | 1 dc |
    | 2.3.1 | **G0 (31)** | 2 dc |
    | 2.3.4 | F0 | 1 dc |

    - Les écarts entre attaques, en double-croches, sont 2-3-2-3-3-2-3-3-2-3 : un motif en 3 + 3 + 2 décalé.
    - Mode de mi phrygien (fa = seconde mineure).
    - Positions mesurées sur la grille, à ± une double-croche près.
- **Reste illisible** :
  - le réglage final du filtre et du LFO, et l'enveloppe d'amplitude complète (seul Release 227 ms est visible) ;
  - la quantité de LFO 2 vers la FM ;
  - le réglage +2 oct +7 demi-tons, absent des captures (texte seulement).

### F01-02 How to Make Hard-Hitting 808s in Serum 2 (Monosounds)
- **Images lues : 2** : `blog-serum-2-808-bass-ig1.png` et `blog-serum-2-808-bass-ig2.png`.
- **Interface** : aucune. Ce sont deux infographies textuelles, sans capture de Serum ; le pied de page dit « serum 2 guides ».
- **Valeurs lues** :
  - **ig1 « 808 From Init in 6 Steps »** :
    1. Load a sine : Default table, position 1, unison 1.
    2. Add the pitch click : Env 2 to pitch, **+24 st, 60 ms decay**.
    3. Saturate it : Overdrive **25 % drive, 60 % mix**.
    4. Low-pass the fizz : cutoff around **400 Hz, after distortion**.
    5. Set up slides : Mono + Legato, portamento **100 ms**.
    6. Tune to the key : roots **between C1 and A1**.
  - **ig2 « Trap vs Drill 808 Cheat Sheet »** :

    | Réglage | Trap | Drill |
    |---|---|---|
    | Amp decay | ~3 s | ~1 s |
    | Amp sustain | 0 % | 80-100 % |
    | Release | 300 ms | 150 ms |
    | Portamento | 60-100 ms | 200-300 ms |
    | Slides | occasionnels | constants, larges |
    | Longueur des notes | courtes, laissées résonner | exactes, tenues |

- **Écarts avec le texte** :
  - L'infographie donne les tonalités **C1-A1**, le texte C1-G1 (notation scientifique de la page : C1 = 32,7 Hz = C0 dans Live).
  - Elle précise que le passe-bas vient **après** la distortion. Le texte, lui, plaçait la distortion sur un bus FX à part.
- **Reste illisible** : rien. Les deux images sont entièrement lisibles. Aucun réglage d'interface n'est montré.

### F15-06 How To Make Liquid Drum & Bass: The Ultimate Guide (EDMProd)
- **Images lues : 8 sur 12 téléchargées** :
  - `Screen-Shot-2022-10-05-at-1.50.14-pm`, `2022-10-07-at-3.37.22-pm`, `3.37.27`, `3.39.50` ;
  - `2022-10-06-at-5.08.51-pm`, `5.13.49` ;
  - `2022-10-11-at-5.54.59-pm`, `5.55.36` ;
  - zooms.
  - Non ouvertes : `3.41.03` (gamme), `5.11.15` (duplication), `5.16.40` (coupure), `3.51.30` (drone, pas une basse).
- **Interface** : **Serum 1**. DAW : Live.
- **Valeurs lues** :
  - **1.50.14 → preset « BS PWM Sub »** (pack de l'article) :
    - SUB et NOISE éteints ;
    - OSC A table **PWM DS**, OCT 0, **Unison 1**, WT POS **modulé** (anneau de modulation), LEVEL modulé ;
    - OSC B table **PWM DS**, OCT 0, **Unison 2**, WT POS et LEVEL modulés ;
    - FILTER **MG Low 24**, routage **A + B** (S éteint), CUTOFF modulé ;
    - positions du filtre : CUTOFF ≈ 10 h (≈ 28 %), RES ≈ 10 h (≈ 28 %), DRIVE ≈ 11 h 30 (≈ 45 %), FAT ≈ 8 h, MIX 100 % ;
    - Env 1 aux valeurs par défaut : 0.5 ms / 0.0 ms / 1.00 s / 0.0 dB / 15 ms ;
    - LFO 1 : **2 destinations**, mode **OFF** (libre, sans retrigger), BPM **décoché**, ANCH coché, RATE **1.7 Hz**, RISE 0.0 s, DELAY 0.0 s, SMOOTH 0.0, forme triangle ;
    - LFO 2 : 1 destination ;
    - macros : **Macro 1 « FILTER »** (1 destination), **Macro 2 « WOBBLE »** (3 destinations) ;
    - VOICING : **MONO** et **LEGATO** cochés (0 / 3) ; PORTA ≈ 11 h, sans nombre affiché ; ALWAYS et SCALED décochés.
  - **3.37.22 → exemple « additif »** :
    - OSC A **Analog_BD_Sin**, OCT 0, Unison 1, WARP **FM (FROM B)** à ≈ 10 h 30 (≈ 33 %), avec un anneau de modulation ;
    - OSC B **Basic Shapes**, **OCT +2**, frame triangle affichée, LEVEL au minimum.
  - **3.37.27 → FX Distortion** : mode **Sine Shaper**, filtre OFF, **F = 330**, **Q = 2.0**, DRIVE ≈ 10 h (≈ 28 %), MIX ≈ 100 %.
  - **3.39.50 → exemple « soustractif »** :
    - SUB **allumé**, sinus, octave 0 ;
    - OSC A **BSOD_Square**, OCT 0, **Unison 5**, DETUNE ≈ 12 h 30, BLEND ≈ 13 h 30, WT POS ≈ 15 h 30 ;
    - OSC B éteint ;
    - FILTER **MG Low 24**, routage **A + S** : le **sub passe dans le filtre** ;
    - positions du filtre : CUTOFF ≈ 10 h (≈ 28 %), RES ≈ 8 h 30 (≈ 11 %), DRIVE ≈ 11 h (≈ 39 %), FAT ≈ 8 h, MIX 100 %.
  - **5.08.51 → ligne de basse de 4 mesures** (notes de Live, vélocité affichée **97**) :

    | Position | Note (MIDI, Hz) | Durée |
    |---|---|---|
    | 1.1.1 | **D♭0** (25, 34,6 Hz) | 6 temps |
    | 2.3.1 | **C1** (36, 65,4 Hz) | 2 temps |
    | 3.1.1 | D♭0 | 3 temps |
    | 3.4.1 | **E♭0** (27, 38,9 Hz) | 3 temps |
    | 4.3.1 | **E♭1** (39, 77,8 Hz) | 2 temps |

    - En fa mineur, ce sont les degrés VI, V et VII.
    - La tonique fa n'apparaît **pas** dans ces 4 mesures.
  - **5.13.49 → variante (mesures 5-8), le « bass run » encadré en bleu** :

    | Position | Note | Durée |
    |---|---|---|
    | 5.1.1 | C♯0 (= D♭0) | 3 temps |
    | 5.4.1 | **C♯1** | 3 temps |
    | 6.3.1 | C1 | 2 temps |
    | 7.1.1 | C♯0 | 3 temps |
    | 7.4.1 | D♯0 | 3 temps |
    | 8.3.1 | D♯1 | 2 temps |

    - Le saut d'octave C♯0 → C♯1 remplace la tenue de 6 temps.
  - **5.54.59 → reverb de la basse** : **Reverb native de Live**, preset « Bright Room » (règle 5 : à remplacer par un plug-in tiers). Valeurs affichées :
    - Input Filter : Lo Cut et Hi Cut allumés, **1.36 kHz**, largeur **5.10** ;
    - Early Reflections : Spin allumé, Amount 6.93, Rate 0.11 Hz, Shape 0.77 ;
    - Diffusion Network : High allumé, **6.16 kHz / 0.77** ; Low éteint (718 Hz / 0.38) ; Diffusion 96 %, Scale 100 % ;
    - Chorus allumé, Amount 0.12, Rate 0.38 Hz ;
    - Predelay **5.00 ms**, Size 1.90, Decay **1.60 s**, Stereo 100.00, Density High ;
    - Reflect 6.0 dB, Diffuse 2.0 dB, **Dry/Wet 100 %**.
  - **5.55.36 → automation** :
    - piste **« Sub »** : volume **−4.5 dB** ; envoi **C (« C-Bass Verb ») à −25.3 dB** au repos, automatisé ;
    - courbe exponentielle qui monte juste avant une frontière de phrase puis retombe d'un coup. La même forme est appliquée à **Serum Macro 1** (le filtre).
- **Reste illisible** :
  - les destinations exactes des LFO et des macros (matrice non montrée) ;
  - la valeur de PORTA ;
  - les quantités de modulation ;
  - la Macro 2 « WOBBLE » automatisée à la mesure 60 : sa capture n'existe pas.

### F01-08 How To Make Dubstep (UK/140) in 5 Easy Steps (EDMProd)
- **Images lues : 6 sur 9 téléchargées** :
  - `image-9.png`, `image-11.png`, `image-16.png`, `image-17.png`, `2024-image.png`, `2024-image-1.png` ;
  - zooms.
  - Non ouvertes : `2024-image-3`, `6`, `7` (rendu, découpes, transitions).
- **Interface** : **Serum 1**. DAW : Live.
- **Valeurs lues** :
  - **image-9 → « Main Sub » au départ** :
    - OSC A table **BSOD_Square** (la « variation de carré » du texte), OCT 0, Unison 1 ;
    - filtre encore **MG Low 12** (le texte passe ensuite en MG Low 24) ;
    - Env 1 aux valeurs par défaut ;
    - LFO 1 triangle à 1/4.
  - **image-16 → FX et LFO 1 après réglage** :
    - **Hyper** : Unison **3**, RATE ≈ 12 h, DETUNE ≈ 12 h 30, MIX ≈ 10 h (≈ 28 %), RETRIG éteint ;
    - **Dimension** : SIZE ≈ 12 h, MIX près du minimum (≈ 0-6 %) ;
    - **Distortion** : mode **Sine Shaper**, filtre OFF, **F = 330**, **Q = 2.0** ; DRIVE ≈ 9 h (≈ 17 %) avec un **anneau de modulation** (Macro 3 selon le texte) ; MIX ≈ 100 % ;
    - **Filter FX (le « comb »)** : type **Cmb HL6+** ; CUTOFF ≈ 9 h (en cours de réglage), RES ≈ 10 h 30, DRIVE ≈ 10 h, HL WID ≈ 16 h 30, PAN 12 h, MIX ≈ 100 % ;
    - **LFO 1** : forme en arche (« Dome »), **3 destinations**, **TRIG** coché, BPM coché, ANCH coché, **DOT** coché, RATE **« 1/8. »** (croche pointée), RISE Off, DELAY Off, SMOOTH 0.0 ;
    - Env 1 : 0.5 ms / 0.0 ms / 1.00 s / 0.0 dB / **20 ms** ;
    - VOICING : **MONO** et **LEGATO** cochés (0 / 2).
  - **image-17 → EQ Eight de Live** (natif, règle 5) :
    - bandes 4, 5 et 6 actives ;
    - bande 6 en cloche : **2.02 kHz, +3.10 dB, Q 0.71** (valeurs affichées) ;
    - bandes 4 et 5 : deux creux en cloche ; minimum de la courbe ≈ −10 dB vers 150-160 Hz, second point vers 240 Hz (≈ −3 dB) (lecture sur le graphe, estimation).
  - **2024-image → exemple de macro** : Macro 1 a 2 destinations, DETUNE d'OSC A et CUTOFF. Patch générique (scie Default, MG Low 12, SUB sinus allumé). C'est une démonstration, pas le patch de la basse.
  - **2024-image-1 → automations des macros** sur la piste **« Main Sub »** : trois macros automatisées, nommées **SHAPER**, **CHAR.** et **WOBBLE**, plus un envoi « C-Bass Verb ».
    - SHAPER monte en pointe sur les fins de phrase ; CHAR. monte par paliers ; WOBBLE bouge lentement.
    - Ces noms ne correspondent pas directement à la liste du texte (Macro 1 cutoff, 2 FM, 3 drive + mix) : la correspondance n'est pas lisible.
  - **image-11** : vue d'arrangement, ligne du sub trop petite pour lire les notes.
- **Reste illisible** :
  - la quantité du LFO vers le cutoff, le cutoff final et la valeur de FM (FROM B) ;
  - l'**OCT +2** d'OSC B, qui n'apparaît sur aucune capture (texte seulement) ;
  - les notes de la mélodie du sub.

### F08-04 How to Make Dubstep Growls in Serum 2 (Monosounds)
- **Images lues : 2** : `blog-serum-2-dubstep-growls-ig1.png` et `-ig2.png`.
- **Interface** : aucune (infographies textuelles, « serum 2 guides »).
- **Valeurs lues** :
  - **ig1 « Talking Rhythm Cheat Sheet »** :

    | Vitesse du LFO | Effet | Destination |
    |---|---|---|
    | 1/1 | slow mouth open-close | WT Position |
    | 1/2 | classic half-time chew | **Warp amount** |
    | 1/4 | steady syllables | Formant cutoff |
    | 1/8 | fast stutter inside notes | Formant, low depth |
    | 1/4 triplet | the yoi-yoi bounce | WT Position |
    | 1/16 | buzzy texture, use rarely | Phaser rate |

  - **ig2 « The Resample Loop »** :
    1. Design pass one : vowel table, warp, formant, dist to phaser.
    2. Render to audio : one held note, **2-4 bars**, FX printed.
    3. Bring it back in : drag the wav in, or **Resample to Oscillator**.
    4. Mangle it again : new warp mode, new formant, new FX.
    5. Change the rhythm : different LFO shape and rate each pass.
    6. Stop at **2-3 passes** : « more passes add mud, not character ».
- **Écart avec le texte** : l'image associe 1/2 au **warp amount**, alors que le texte en fait le « mouvement principal » (WT Position). Ce sont deux couches compatibles, pas une contradiction ferme.
- **Reste illisible** : rien.

### F15-01 Serum 2 Clip Sequencer: The Complete Guide (EDMProd)
- **Images lues : 5 sur 6 téléchargées**, webp convertis en PNG :
  - `serum-2-clip-01-clip-overview`, `03-expression-routing`, `08-poly-transpose`, `09-pitch-curves`, `11-velocity-routing`.
  - Non ouverte : `07-playback-rate`.
- **Interface** : **Serum 2** (onglets OSC / MIX / FX / MATRIX / GLOBAL, modules CLIP et ARP).
- **Valeurs lues** :
  - **01 → Clip 1, réglages affichés** :
    - Trigger Mode **MONO** ;
    - Length **1. 0. 0** (une mesure), KB Span Off, Trans 0, Mode Normal ;
    - Rate **1x**, BPM coché ;
    - Launch Quant **1/16** ; Retrig, Velo Trig et Note Gate décochés ;
    - grille 1/16, Overdub ; MIDI Out Off.
  - **01 → motif « roulant » (notation affichée par Serum ; Serum place C3 au milieu de son clavier)** :
    - en double-croches : D0 D0 A0 D0 | D0 A#0 D0 D0 | A0 D0 D0 **D1** | D0 A#0 A0… ;
    - la sélection affiche « A0 1.3.1 - 1.3.2 » ;
    - vélocités égales, ≈ 97 (estimation sur la règle 1-127).
  - **03 → menu Mod Source** : clic droit sur **Filter 1 Freq** › Mod Source › **MPE** › **Expr X (Pan)**, Expr Y (Timbre), Expr Z (Press.). Autres sources du menu : Envelopes, LFOs, Note, Oscillators, Macros, Filters, Mod Wheel.
  - **11 → vélocité vers le niveau d'OSC A** :
    - info-bulle **« Velo→A Level : 46% »**, **« Range : 35% [−18.4 dB] → 81% [−3.8 dB] »** ;
    - le patch d'Init de Serum 2 est visible : OSC A table **Default Shapes**, frame 1 = scie, phase **180°**, **RAND 100** ;
    - Filter 1 **MG Low 12** allumé, routage A ;
    - Env 1 **1.0 ms / 0.0 ms / 1.00 s / 0.0 dB / 15 ms** ;
    - LFO 1 en mode **Normal**, RETRIG, 1/4 BPM ;
    - Poly 8.
  - **08 et 09 → Clip 2** :
    - Trigger Mode **POLY**, **Trans 24**, Length 1. 0. 0 ;
    - Rate **« 1t »** (triolet) sur l'image 08 et **« 1x »** sur l'image 09 ;
    - Launch Quant **1/8** ;
    - couloir **Expr X** visible (valeurs de −100 à +100 par note).
    - Notes (09) : courbes de hauteur dessinées, montée de D0 vers A#0 et descente de A0 vers D0, puis une longue chute courbe depuis le dernier D0 jusqu'à environ 9 demi-tons plus bas, à la fin de la mesure (estimation).
- **Reste illisible** :
  - les quantités de modulation d'Expr X vers le filtre ;
  - les valeurs exactes des courbes de hauteur ;
  - le patch « Big Wobber Bass », jamais montré en entier.

### F14-09 The Baddadan Synth Bass Sound (Attack Magazine)
- **Images lues : 3 sur 8 téléchargées** :
  - `Session.jpg`, `Step-5-2.png`, `Step-5-3.png` et zooms.
  - Non ouvertes : `Step-1` à `Step-5.png` (états intermédiaires de Zebra, déjà chiffrés dans le texte).
  - Les images ont été prises sur `www.attackmagazine.com` en direct, sans passer par `i0.wp.com`.
- **Interface** : **pas Serum** (u-he Zebra 2 ; DAW Live).
- **Valeurs lues** :
  - **Session.jpg → motif MIDI** (174 BPM, piano roll de Live replié, 1000 px seulement, d'où des étiquettes floues) :
    - Toutes les notes sont des double-croches courtes à vélocité ≈ 127, sauf le F2 final, plus long (≈ une croche) et plus doux.
    - Mesures 1-2 (identiques en 3-4 et 5-6) :

      | Position | Note (MIDI) |
      |---|---|
      | 1.2.1 | F2 (53) |
      | 1.3.1 | F2 |
      | 1.4.1 | F2 |
      | 1.4.3 | C2 (48) |
      | 2.1.1 | E2 (52) |
      | 2.1.3 | G♭2 (54, étiquette floue, lecture probable) |

    - Mesures 7-8 :

      | Position | Note (MIDI) |
      |---|---|
      | 7.2.1 | E♭2 (51) |
      | 7.3.1 | E♭2 |
      | 7.4.1 | E♭2 |
      | 7.4.3 | D♭2 (49) |
      | 8.1.1 | G♭2 |
      | 8.1.3 | G♭2 |
      | 8.2.1 | F2 (≈ une croche) |

  - **Step-5-3 → Zebra 2, page GLOBAL** :
    - PITCH Transpose **−12** (le F2 du clip sonne une octave plus bas) ;
    - VOICES medium ; MODE **retrigger** ; GLIDE en mode time ;
    - grille : OSC1, OSC2, OSC3, VCF1 et Shape1 sur la voie 1, FMO1 sur la voie 2 ;
    - FX : EQ1 puis Delay1 ;
    - VCF1 en **LP Vintage** ; Shape1 en **Wedge** ; FMO1 en « FM by Input » ;
    - Env 1 à Env 3 en time base 8sX, mode v-slope.
  - **Step-5-2 → EQ 1 de Zebra**, quatre points :
    - creux vers 175-300 Hz (≈ −3 dB) ;
    - bosse vers 3 kHz (≈ +4 dB) ;
    - lecture sur le graphe, estimation.
  - **Step-5-2 → chaîne Live** (effets natifs, règle 5) :
    - **Drum Buss** : Drive 20 %, Soft, Crunch 44 %, Damp 9.20 kHz, Transients 0.00, Boom 0.0 %, Freq 50.0 Hz, Decay 100 %, Trim 0.00 dB, Out −4.17 dB, Dry/Wet 100 % ;
    - **Saturator** (preset « Hard Punch ») : Drive 12.6 dB, Hard Curve, Color allumé, Base −20.0, Freq 80.0 Hz, Width 0.0 %, Depth 5.00, Output −19.8 dB, Soft Clip Off, **Dry/Wet 30 %** ;
    - **Limiter** : Gain 14.5 dB, Ceiling −0.30 dB, Lookahead 3 ms, Release 300 ms Auto, Stereo.
- **Reste illisible** : les positions de boutons de Zebra, sans nombre affiché sur ces captures. Les valeurs de Zebra restent celles du texte.

### GEN-06 How to Make a Bass in Serum 2 (Monosounds), vérification
- **Images lues : 6 sur 7 téléchargées**, webp convertis en PNG :
  - `bass-step1-osc`, `bass-step2-sub-filter`, `bass-step2-filter`, `bass-step3-env`, `bass-step3-matrix-rows`, `bass-step4-fx-rack` et zooms.
  - Non ouverte : `bass-step1-osc-a`.
- **Interface** : **Serum 2**.
- **Valeurs lues** (elles confirment le texte, sauf le dernier point) :
  - **step1-osc → OSC A** :
    - Basic Shapes, **OCT −1**, frame **2** (scie), phase **180°**, **RAND 100**, Unison 1 ;
    - Filter 1 éteint, mais son type grisé se lit « MG Low 12 » (image floue) ;
    - Env 1 par défaut 1.0 ms / 0.0 ms / 1.00 s / 0.0 dB / 15 ms.
  - **step2-sub-filter** :
    - SUB allumé, **OCT −1**, sinus, phase 0° ;
    - Filter 1 **MG Low 24**, routage **A seul** (S éteint) : le sub contourne le filtre.
  - **step2-filter** : MG Low 24, routage A ; CUTOFF ≈ 11 h, RES ≈ 8 h 30, DRIVE et FAT bas, MIX ≈ 100 %, PAN 12 h.
  - **step3-env → ENV 1** : **2.0 ms / 0.0 ms / 350 ms / −5.0 dB / 120 ms** (valeurs affichées). Env 2 a 1 destination.
  - **step3-matrix-rows → MATRIX** :
    - **Env 2 → Filter 1 Freq**, curseur positif d'environ un tiers de la course (≈ 30 %, estimation) ;
    - **Velo → Filter 1 Freq**, faible positif (≈ 10 %, estimation).
  - **step4-fx-rack**, bus MAIN :
    - **Distortion** : **TAPE SAT.**, filtre OFF, **FREQ 425**, **Q 1.9** ; DRIVE ≈ 10 h ; MIX ≈ 11 h 30.
    - **Compressor** : mode **SINGLE**, **THRESH −20.8 dB**, **RATIO 4:1**, **ATTACK 8.0**, **RELEASE 110.0**, **GAIN 3.5** (le « un peu de makeup » du texte) ; le bouton MIX n'affiche pas de nombre.
    - **Equalizer** :
      - bande 1 : **FREQ 32**, **Q 60**, GAIN 0.0, forme **passe-haut** (icône du bas allumée) ;
      - bande 2 : **FREQ 2800**, **Q 60**, GAIN **−3.0**, forme **passe-bas** (icône du bas allumée) ; la courbe chute fortement au-dessus de 2,8 kHz, avec une bosse de résonance.
      - **Contradiction texte/image** : le texte décrit « une coupe douce de −3 dB vers 2,8 kHz » ; l'image montre un **passe-bas résonant à 2,8 kHz**. À trancher dans Serum 2 sur le Mac.
- **Serum 2 par défaut** : deux captures (GEN-06 grisée, F15-01 allumée) montrent **MG Low 12** comme type de Filter 1 à l'Init. Cela corrobore l'affirmation de la page.

### F03-04 FM Synthesis in Serum 2 (Monosounds), complément
- **Images lues : 2 sur 3 téléchargées** : `fm-osc.png` et `fm-osc-ab.png`. Non ouverte : `fm-warp-menu` (menu déjà listé dans le texte).
- **Interface** : **Serum 2**.
- **Valeurs lues** :
  - **fm-osc-ab** :
    - OSC A et OSC B en Basic Shapes sinus ;
    - **OSC B OCT +1**, LEVEL au minimum ;
    - WARP 1 d'OSC A sur **FM (B)**, bouton à ≈ 16 h (position de démonstration, sans nombre) ;
    - les deux oscillateurs en phase 180° et RAND 100.
  - **fm-osc → patch « FM Demo »** :
    - **ENV 1 : 5.0 ms / 0.0 ms / 600 ms / −8.9 dB / 300 ms** (valeurs affichées ; le texte ne donnait aucune enveloppe d'amplitude) ;
    - ENV 2 : 1 destination (le warp) ;
    - Filter 1 éteint ; Poly 16.
- **Reste illisible** : la quantité d'ENV 2 vers le warp, sans nombre affiché.

### F13-11, F02-14, F07-23, F01-12 (MusicRadar)
- **Images lues : 0.** Les captures sont hébergées sur `cdn.mos.cms.futurecdn.net`, refusé par le proxy (`connect_rejected`).
- Les valeurs de ces pages restent celles du texte, déjà relevées dans les deux études.

---

## Synthèse des écarts entre texte et image

| Id | Le texte dit | L'image montre |
|---|---|---|
| F01-06 | filtre HP de la distortion pour épargner le sub | filtre de la distortion sur **OFF** (F 644, Q 0.1, curseur sur HP) |
| F01-06 | Detune, Blend et Rand tout à gauche (étape 2) | la capture de l'étape 5 les montre aux positions par défaut, Rand haut |
| F01-13 | saturation « subtile » par Soft Clip | DRIVE de la Soft Clip ≈ 85-90 % |
| F05-12 | (rien sur le type de filtre) | **MG Low 12** et warp **FM (FROM B) 28 %** sur la table **BS2 - Subby Saw** |
| F01-08 | MG Low 24 | la capture de départ est en MG Low 12 ; la capture finale n'affiche pas le filtre |
| F01-02 | tonalités C1-G1 | infographie : C1-A1 |
| GEN-06 | EQ bande 2 « coupe douce de −3 dB » à 2,8 kHz | passe-bas Q 60 à 2800 Hz (gain −3.0 affiché) |
| F15-06 | « ligne en fa mineur » | les 4 mesures ne jouent que D♭0, C1, E♭0, E♭1, sans la tonique fa |
