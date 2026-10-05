# Vingt recettes de saw percussive pour la House (famille F05)

Deuxième lot de recettes House. La basse médium qui frappe : saw percussive, chop Bass House, basse Tech House. Rédigé le 05/10/2026. Sources :
- les études de `../etudes-videos.md` (F05-01, F05-02, F05-03), `../etudes-pages-house.md` (GEN-06, F05-12, F05-14, F07-23, F15-01) et `../etudes-captures.md` (GEN-06, F05-12) ;
- la transcription Antidote Audio de `../../../composer-hooks-funk-electro/references/sources-videos.md` ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Les étiquettes sont celles de `house-f01-sub.md` :
- **[SOURCE Fxx-yy]** : valeur ou geste relevé dans une étude ; « écran » signale une valeur lue sur une capture, à confirmer ;
- **[CALCUL]** : valeur obtenue par une formule ;
- **[DÉDUCTION]** : conséquence tirée de la documentation, non essayée ;
- **[ORIGINAL]** : réglage proposé ici.

## Règles communes aux vingt recettes

1. **C'est une couche médium, jamais le sub.** Le sub vient d'une recette de `house-f01-sub.md`, sur une piste à part (règle « Grave » d'`AGENTS.md`). Chaque fiche propose un sub à lui associer.
   - Dans la couche médium, l'Equalizer de Serum 2 a sa bande basse en **High Pass vers 90 Hz** (80-120 Hz selon la note et le kick), sauf mention contraire.
   - Plusieurs tutoriels laissent le sub dans le même patch (F05-01, GEN-06) : les recettes l'en sortent.
2. **Départ** : menu principal › Init Preset. VOICING sur MONO, sauf mention contraire. Dans l'Init, OSC A va dans FILTER 1.
3. **Phase** : RAND à 0 et PHASE fixe sur les oscillateurs qui frappent. Chaque note part alors de la même façon, ce que F05-01 et F05-02 font aussi (« retrig »). F05-03 garde au contraire RAND à 100. Le choix est dit dans chaque fiche.
4. **Quatre macros communes**, reprises de la fiche 5 de `../families.md`, avec `Tone` en plus :
   - `Punch` : quantité d'ENV 2 (ou de l'enveloppe qui ouvre le filtre) ;
   - `Dirt` : drive de la saturation principale, avec LEVEL en sens inverse ;
   - `Tail` : decay d'ENV 1 ;
   - `Tone` : coupure de base du filtre principal.

   Vérifier le « + » sur chaque destination avant d'assigner (cartographie, § 7.3).
5. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`). Kickstart 2 et LFO Tool, vus dans les études, sont des plug-ins tiers.
6. **Contrôle par l'utilisateur** :
   - la couche seule, puis avec son sub, puis avec le kick ;
   - mono ;
   - les deux bornes de `Punch` et de `Dirt` ;
   - une note grave et une note aiguë de la ligne ;
   - faible volume ;
   - A/B à niveau égal contre P01.

   Le compresseur de bus ne doit pas pomper sur chaque attaque (`../families.md`, fiche 5).

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| P01 | Pluck House chiffré | toute House, référence A/B | ENV 2 sur MG Low 24, Tape Sat. |
| P02 | Saw Model D en ladder | Tech House, Bass House | passe-haut, MG Ladder 175 Hz, compresseur rapide |
| P03 | Saw acid à portamento | Tech House groovy | MG Low 18, résonance, distorsion après filtre |
| P04 | Saw au baffle de guitare | Tech House sale | Convolve Cab, distorsion, Sample & Hold |
| P05 | FM pluck Bass House | Bass House 128 | FM à +2 oct +7 st, LFO Envelope sur le filtre |
| P06 | Thumper | Bass House, Tech House | presque sinus, Stomp Box, passe-bas |
| P07 | Screecher fermé | Bass House | saw unison, ENV 1 aussi sur le filtre |
| P08 | Saw sync « tchak » | Bass House | enveloppe sur le warp Sync |
| P09 | Saw multi-voix libre | Tech House large | unison libre au-dessus du passe-haut |
| P10 | Saw renforcée d'un sinus | Tech House, Deep Tech | corps bas-médium, sans sub |
| P11 | Chop au LFO | Bass House | découpe d'une note tenue |
| P12 | Stab saw courte | Bass House, G-House | quinte courte, mono |
| P13 | Ligne roulante en Clip | Tech House | boucle de trois temps sur un 4/4 |
| P14 | Saw sale Downsample | Tech House, Bass House | filtre, compresseur, Downsample |
| P15 | Acid Ladder accentuée | Tech House acid | vélocité vers l'enveloppe |
| P16 | Carré « 80s » | Nu-disco House | carrée au lieu de la scie |
| P17 | Wide FM | Deep House, Tech House | carrée unison modulée par une saw |
| P18 | Distorsion dynamique | Tech House, Bass House | enveloppe sur le drive |
| P19 | Blip de hauteur | Bass House | ENV 3 brève sur la hauteur de A |
| P20 | Saw MG Dirty | Tech House organique | un seul filtre saturé (PAIN) |

## Les vingt recettes

### P01 Pluck House chiffré — référence de la famille
- **Patch** :
  - OSC A sur Basic Shapes, frame 2 (scie), OCT −1, Unison 1, RAND 0, PHASE fixe.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 40 %, RES 18 %.
  - ENV 2 → CUTOFF ≈ 30 %. ENV 2 : attaque 1 ms, decay 220 ms, sustain 0, release 150 ms.
  - Matrice : Velocity → CUTOFF ≈ 10 %.
  - SUB éteint.
- **ENV 1** : 2 ms / 0 / 350 ms / −5 dB / 120 ms.
- **FX** :
  1. Distortion Tape Sat., DRIVE ≈ 28, MIX 45 %.
  2. Equalizer : bande basse en High Pass, ici à 90 Hz au lieu de 32 Hz ; bande haute à 2,8 kHz, −3 dB (la capture montre un passe-bas résonant, à trancher à l'oreille).
  3. Compressor Single : −20,8 dB, 4:1, attaque 8 ms, release 110 ms, gain 3,5 dB.
- **Sortie** : crêtes vers −6 dBFS par le bouton MAIN.
- **Macros** : `Punch` ENV 2 → CUTOFF 10 → 50 % · `Dirt` DRIVE 0 → 50 · `Tail` decay d'ENV 1 150 → 600 ms · `Tone` CUTOFF 25 → 60 %.
- **Sub associé** : S01 ou S03.
- **Jeu** : motif « Tech House 124 — appel et réponse » ci-dessous.
- **Origine** :
  - toutes les valeurs [SOURCE GEN-06, page et écran], sauf le passe-haut à 90 Hz et l'absence du sub [ORIGINAL] ;
  - la capture montre RAND 100 et PHASE 180° : RAND remis à 0 pour une attaque constante [ORIGINAL].
- **Variantes de la page** :
  - carrée au lieu de la scie : P16 ;
  - Acid Ladder : P15 ;
  - cutoff 25 % sans distorsion : couleur 808 ;
  - au-delà de 30 % de résonance sur un ladder, la fondamentale baisse.

### P02 Saw Model D en ladder — Tech House, Bass House
- **Patch** :
  - OSC A sur la table Serum 2 « AT Model D », position sur la scie, PHASE 52°, RAND 0. Un warp de distorsion « pour l'épaissir un peu », mode non dit : Tube [ORIGINAL].
  - FILTER 2 en High 24 sur A seul : il retire le grave de la scie.
- **ENV 1** : attaque 1 ms, decay 247 ms (237 ms à une autre capture), sustain −2,6 dB (puis −6,1 dB), release 420 ms.
- **ENV 2** : decay 289 ms, sustain −∞, vers le CUTOFF du module Filter des FX. VOICING MONO + LEGATO, ALWAYS.
- **FX** :
  1. Filter MG Ladder, CUTOFF 175 Hz, RES 12 %.
  2. Equalizer : creux à 185 Hz, Q 73, −6,2 dB.
  3. Compressor Single (réglage d'usine « 1176 Glue ») : −26,4 dB, 4:1, attaque 0,6 ms, release 260 ms, gain 9,2 dB.
  4. Equalizer : 343 Hz, Q 41, +2,2 dB ; ≈ 2 040 Hz, Q 67, −6,2 dB.
  5. Filter MG Low 6 contre les aigus « numériques ».
- **Macros** :
  - `Punch` ENV 2 → CUTOFF du ladder 0 → 60 %.
  - `Dirt` quantité du warp 0 → 50 %.
  - `Tail` decay d'ENV 1 120 → 400 ms.
  - `Tone` CUTOFF et RES du ladder ensemble, de 120 à 1 000 Hz et de 5 à 25 %. C'est la « macro de filtre façon Chris Lake ».
- **Sub associé** : S01. F05-01 met un sub en Direct Out dans le patch ; ici il est sur une piste à part.
- **Jeu** : demi-tons du mode mineur autour de la tonique ; F05-01 dit D#, E, F#, E, F#, E, D#, C#, transcription approximative.
- **Origine** : [SOURCE F05-01, voix et écran] ; les valeurs d'ENV 1 diffèrent selon la capture.

### P03 Saw acid à portamento — Tech House groovy
- **Patch** :
  - OSC A sur Basic Shapes, scie, OCT −2, RAND 100 : pas de retrig, chaque note part autrement.
  - FILTER 1 en MG Low 18, coupure basse, un peu de RES, DRIVE et FAT. Le FAT compense la perte de grave due à la résonance.
  - La voix dit ensuite « 12 retenu, 6 aussi valable » : essayer MG Low 12 et MG Low 6.
  - ENV 2 → CUTOFF, mouvement faible : attaque 0,5 ms, decay ≈ 301 ms.
- **ENV 1** : decay ≈ 143 ms, sustain ≈ −8,3 dB, release 15 ms. Sustain bas pour que l'attaque sature plus que le corps.
- **FX** :
  1. Distortion Tube.
  2. Compressor Multiband : −20,9 dB, 5:1, attaque ≈ 95,6, release ≈ 9,0, bandes à 120 et 2 500 Hz.
  3. Equalizer : 142 Hz, Q 53, +5,5 dB ; 818 Hz, Q 46, +0,7 dB.
- **Voicing** : MONO, portamento avec courbe, LEGATO coupé à la fin pour garder le punch des enveloppes à chaque note.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 40 % · `Dirt` DRIVE de la Tube 0 → 70 · `Tail` decay d'ENV 1 80 → 300 ms · `Tone` CUTOFF 15 → 50 %.
- **Sub associé** : S02, pour une ligne roulante. Le tutoriel garde le grave dans la scie, jouée entre C2 et C3 à OCT −2, donc de C0 à C1 réels. Ici le passe-haut de la couche à 80-90 Hz laisse la fondamentale au sub.
- **Jeu** : motif « Tech House 126 — acid roulant » ci-dessous. Sidechain par plug-in tiers (Kickstart 2 dans le tutoriel).
- **Origine** :
  - [SOURCE F05-03, voix et écran ; petits chiffres à confirmer] ;
  - principe dit : couper les aigus, accentuer une zone par la résonance, puis laisser la distorsion recréer les harmoniques ;
  - même geste de chevauchement + portamento chez Sam Smyers [SOURCE F05-03, page].

### P04 Saw au baffle de guitare — Tech House sale
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - FILTER 1 en Low 24, qui retire le haut. ENV 2 → CUTOFF, un peu de punch.
- **ENV 1** : sustain bas, decay tiré, pour que l'attaque sature plus que le corps.
- **FX, dans l'ordre vu à l'écran** :
  1. Convolve : IR Factory › Cab, « Cab 2 » (écran : « ELECTRIC GUITAR CAB 2 »), IR GAIN ≈ −8,6 dB, SIZE réduite.
  2. Distortion, filtre en PRE et en passe-haut. Le mode est mal lu (« Diode ») ; il retire le grave accumulé par le baffle.
  3. Compressor Multiband avec BELOW (effet OTT) : −18,1 dB, 4:1, attaque 90,1, release 90,1, gain 9,5 dB.
  4. Filter en SampHold, avec résonance : CUTOFF baisse la fréquence d'échantillonnage, RES la résolution.
  5. ENV 3 → DRIVE de la Distortion, attaque 0, decay 60-120 ms : la « distorsion dynamique ».
- **Macros** :
  - `Punch` ENV 2 → CUTOFF 0 → 40 %.
  - `Dirt` DRIVE 0 → 70.
  - `Tail` decay d'ENV 1 80 → 300 ms.
  - `Tone` CUTOFF du SampHold, du plus haut (effet nul) à un tiers de la course.
- **Sub associé** : aucun ou S06. La référence du tutoriel (« Bad B » de Julian Jordan) n'a rien sous 60 Hz. Le sub optionnel du tutoriel passait par l'EQ Eight de Live (effet natif, règle 5) : utiliser un sub de F01.
- **Origine** :
  - [SOURCE F05-02, voix et écran] ; « l'EQ fait souvent mieux » que l'OTT, dit le tutoriel ;
  - decay d'ENV 3 [ORIGINAL].

### P05 FM pluck Bass House — Bass House 128
- **Patch** :
  - OSC A en scie, RAND 0. La capture montre une table « BS2 - Subby Saw », probablement d'un pack : Basic Shapes en scie à défaut.
  - WARP 1 d'OSC A en FM (B), ≈ 28 % (écran).
  - OSC B sur Basic Shapes en sinus, LEVEL 0, monté de 2 octaves et 7 demi-tons (OCT +2, SEM +7), routé `None`.
  - FILTER 1 en MG Low 12.
  - LFO 1 en mode Envelope, BPM, 1/4, → CUTOFF. Forme : montée rapide jusqu'au sommet vers 15 % du cycle, puis descente presque linéaire.
  - LFO 2 → quantité de FM, avec modération.
- **ENV 1** : sustain bas, release 227 ms (écran). Attaque 1 ms et decay 250 ms [ORIGINAL].
- **FX** : le tutoriel cite OTT, EQ, distortion, sidechain et largeur sans valeurs. Proposé : Compressor Multiband à gain modéré, puis le passe-haut à 90 Hz [ORIGINAL].
- **Macros** :
  - `Punch` LFO 1 → CUTOFF 0 → 60 % · `Dirt` quantité de FM 10 → 45 % · `Tail` release d'ENV 1 100 → 300 ms · `Tone` CUTOFF 20 → 55 %.
  - **Variante du drop B** : OCT d'OSC B de +2 à +3 (même +7 demi-tons).
- **Sub associé** : S01 ou S10.
- **Jeu** : motif « Bass House 128 — mi phrygien » ci-dessous, relevé sur la capture.
- **Origine** :
  - [SOURCE F05-12, page et écran] ;
  - en FM, le modulateur à +31 demi-tons (rapport ≈ 1:6) donne des bandes à fA ± 6 fA… sur la porteuse : spectre presque harmonique, un peu inharmonique en tempérament égal [CALCUL, `../documentation-basses.md` § 1].

### P06 Thumper — Bass House, Tech House
- **Patch** :
  - OSC A sur Basic Shapes en triangle, ou sinus avec un léger warp Bend +, OCT −1, RAND 0.
  - FILTER 1 éteint.
- **ENV 1** : attaque 0,5 ms, decay 120-180 ms, sustain −∞, release 30 ms.
- **FX** :
  1. Distortion Stomp Box, DRIVE 40-60, MIX 100 %.
  2. Compressor Single : 4:1, attaque 5 ms, release 80 ms.
  3. Filter en MG Low 12, CUTOFF 1,5-3 kHz.
  4. Hyper/Dimension discret : MIX ≤ 15 %, UNISON ≤ 3.
  5. Equalizer, passe-haut à 90 Hz.
- **Macros** : `Punch` decay d'ENV 1 80 → 250 ms · `Dirt` DRIVE de la Stomp Box 0 → 80 · `Tail` release 15 → 80 ms · `Tone` CUTOFF du Filter FX 800 Hz → 5 kHz.
- **Sub associé** : S11, court comme le thumper.
- **Jeu** : coups courts dans les trous du kick.
- **Origine** :
  - geste dit : source proche du sinus, attaque et decay courts, sustain nul, Stomp Box, compression puis passe-bas, Hyper/Dimension subtil, pas d'unison large [SOURCE Antidote Audio « Savage Bass House Basses », transcription, `sources-videos.md`] ;
  - toutes les valeurs [ORIGINAL] : la vidéo ne les dit pas.

### P07 Screecher fermé — Bass House
- **Patch** :
  - OSC A en scie, Unison 3, DETUNE bas, RAND 0.
  - FILTER 1 en MG Low 24, CUTOFF bas (≈ 20 %), RES 20 %.
  - ENV 1 à la fois sur l'amplitude et → CUTOFF (+40 à +60 %) : le filtre s'ouvre avec la note et se referme avec elle.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −12 dB, release 80 ms.
- **FX** : Distortion Soft Clip, puis Compressor Multiband, puis passe-haut à 90 Hz.
- **Macros** : `Punch` ENV 1 → CUTOFF 0 → 70 % · `Dirt` DRIVE 0 → 70 · `Tail` decay d'ENV 1 150 → 600 ms · `Tone` CUTOFF 10 → 40 %.
- **Sub associé** : S07 ou S10. Le tutoriel ajoute un sub dans le patch : ici, sur une piste à part.
- **Jeu** : une seule ouverture par appel ; laisser la réponse à une autre basse.
- **Origine** :
  - geste dit : saw, unison, distorsion, multibande, sub, filtre fermé modulé par ENV 1 [SOURCE Antidote Audio, transcription] ;
  - valeurs [ORIGINAL].

### P08 Saw sync « tchak » — Bass House
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - WARP 1 en Sync, base 10-20 %, VAR vers le « soft sync » pour adoucir.
  - ENV 2 → quantité du warp Sync, +40 à +70 %, attaque 0, decay 60-120 ms, sustain 0.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 50 %.
- **ENV 1** : attaque 1 ms, decay 250 ms, sustain −10 dB, release 80 ms.
- **FX** : Distortion Tube DRIVE 20-30, puis passe-haut à 90 Hz.
- **Macros** : `Punch` ENV 2 → Sync 0 → 80 % · `Dirt` DRIVE 0 → 60 · `Tail` decay d'ENV 1 100 → 400 ms · `Tone` CUTOFF 30 → 80 %.
- **Sub associé** : S01.
- **Jeu** : croches et doubles croches répétées sur une seule note.
- **Origine** :
  - Sync : « les harmoniques montent, la note reste », VAR passe du hard au soft sync [cartographie, § 4.1] ;
  - « scie épaisse par warp Sync », typologie sans valeurs [SOURCE F05-14] ;
  - valeurs [ORIGINAL].

### P09 Saw multi-voix libre — Tech House large
- **Patch** :
  - OSC A en scie, OCT −1, Unison 4, DETUNE 10-15 %, BLEND 50-70 %, RAND 100 : voix non redéclenchées.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 45 %.
  - ENV 2 → CUTOFF +25 %, decay 200 ms.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 100 ms.
- **FX** :
  1. Equalizer en passe-haut à 120 Hz.
  2. Utility, MONO BASS allumé, FREQ 150 Hz.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 50 % · `Dirt` DETUNE 0 → 25 % · `Tail` decay d'ENV 1 150 → 500 ms · `Tone` CUTOFF 25 → 70 %.
- **Sub associé** : S01. Le passe-haut est plus haut que d'habitude, car l'unison s'annule sous 100 Hz.
- **Jeu** : notes de deux doubles croches en contretemps.
- **Test** : mono, la largeur doit disparaître sans perte de niveau marquée.
- **Origine** :
  - « scie multi-voix non redéclenchée » [SOURCE F05-14, typologie] ;
  - pas d'unison sous 100 Hz, largeur sur une partie passée par un passe-haut [SOURCE GEN-06] ;
  - Utility MONO BASS [cartographie, § 8] ;
  - valeurs [ORIGINAL].

### P10 Saw renforcée d'un sinus — corps bas-médium
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - OSC B sur Default position 1 (sinus), même octave que A, PHASE alignée sur A, LEVEL 40-60 %.
  - FILTER 1 en MG Low 24 sur A seul, CUTOFF ≈ 40 %. ENV 2 → CUTOFF +30 %, decay 200 ms.
- **ENV 1** : attaque 2 ms, decay 400 ms, sustain −6 dB, release 100 ms.
- **FX** : Equalizer en passe-haut à 90 Hz, puis Compressor Single 3:1.
- **Hauteur réelle** : le sinus renforce la fondamentale de la ligne médium. Si la ligne est jouée en Fa1-Do2 (87-131 Hz), il n'empiète pas sur le sub en Fa0.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 50 % · `Dirt` LEVEL d'OSC B 0 → 70 % · `Tail` decay d'ENV 1 150 → 600 ms · `Tone` CUTOFF 25 → 60 %.
- **Sub associé** : S01, une octave sous la ligne médium.
- **Origine** : « scie dont le fondamental est renforcé par un sinus » [SOURCE F05-14, typologie] ; valeurs [ORIGINAL].

### P11 Chop au LFO — Bass House
- **Patch** : P01, avec un découpage en plus.
  - LFO 2 → LEVEL d'OSC A, quantité −100.
  - LFO 2 en mode FREE, BPM, RATE 1/4, HOST allumé, MONO.
  - Forme dessinée en marches (Shift-clic, grille X 16) : coupures sur les doubles croches choisies.
- **ENV 1** : comme P01, sustain remonté à −2 dB pour que la note tenue reste pleine entre les coupures.
- **Macros** : `Punch` ENV 2 → CUTOFF 10 → 50 % · `Dirt` DRIVE 0 → 50 · `Tail` quantité du chop 0 → −100 · `Tone` CUTOFF 25 → 60 %.
- **Sub associé** : S10, à la même cadence de creux.
- **Jeu** : une note tenue d'une demi-mesure, découpée en rythme.
- **Test** : le découpage doit rester calé sur la grille quand la lecture démarre ailleurs ; coupures sans clic, sinon SMOOTH 5-10.
- **Origine** :
  - outils de dessin, grille, HOST, SMOOTH [cartographie, § 7.2] ;
  - geste [ORIGINAL] ;
  - équivalent par la voix « laser » de F05-12 en appel et réponse, sans valeurs.

### P12 Stab saw courte — Bass House, G-House
- **Patch** :
  - OSC A en scie, OCT −1. OSC B en scie, SEM +7 (une quinte), LEVEL 70 %. RAND 0 sur les deux.
  - VOICING MONO : la quinte est dans le patch, pas dans le MIDI.
  - FILTER 1 en MG Low 12 sur A et B, CUTOFF ≈ 35 %. ENV 2 → CUTOFF +45 %, decay 120 ms.
- **ENV 1** : attaque 1 ms, decay 160 ms, sustain −∞, release 40 ms.
- **FX** : Distortion Soft Clip DRIVE 20-40, puis Reverb Hall MIX ≤ 10 % avec LO CUT haut, puis passe-haut à 120 Hz.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 70 % · `Dirt` DRIVE 0 → 60 · `Tail` decay d'ENV 1 80 → 300 ms · `Tone` CUTOFF 20 → 60 %.
- **Sub associé** : S11, ou aucun si le stab répond à une autre basse.
- **Test** : quinte et tonique en mono, et la quinte ne doit pas brouiller l'accord du morceau.
- **Origine** :
  - chapitres « Chorus Bass Pluck », « Chorus Bass Stab », soft clipping, Hall, compatibilité mono [SOURCE F05-06, page ; vidéo non visionnée] ;
  - patch [ORIGINAL].

### P13 Ligne roulante en Clip — Tech House
- **Patch** :
  - P01 ou P03.
  - Module CLIP de Serum 2 : Mono + Bar + Retrig, Note Gate off, Rate BPM.
  - Boucle de 3 temps contre le kick en 4/4 : les accents de la basse tournent contre le kick.
  - Velocity → LEVEL d'OSC A, faible quantité.
  - Chance réduite sur les notes de passage, notes d'ancrage à 100 %.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S02 ou S19, avec la même boucle jouée dans Live.
- **Test** :
  - au bout de trois mesures, la boucle revient sur le temps 1 ;
  - vérifier que l'ancrage tombe juste avant ou après le kick, pas dessus.
- **Origine** : module Clip, boucle de 3 temps, Mono + Bar + Retrig, vélocité sans effet tant qu'elle n'a pas de destination, chance par note, Lock Module pour comparer les presets sur la même ligne [SOURCE F15-01].
- **Limite** : les notes du Clip ne sont pas dans le clip de Live. Pour garder le sub en phase, imprimer la ligne ou la recopier dans Live.

### P14 Saw sale Downsample — Tech House, Bass House
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0. FILTER 1 éteint.
  - Matrice : Velocity → RES du Filter FX +40, Velocity → DRIVE de la Distortion +20.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −6 dB, release 100 ms.
- **FX** :
  1. Filter en L/B/H 24 (multimode à morphing), CUTOFF ≈ 300 Hz, RES ≈ 50 %, DRIVE et MORPH ≈ 30 %. LFO 1 (1 mesure) → CUTOFF +10 et → MORPH −20.
  2. Compressor : attaque et release 50-60 ms, environ 4 dB de réduction, 1 dB de gain.
  3. Distortion Downsample, MIX 50 %. LFO 1 → DRIVE en sens inverse.
  4. Equalizer en passe-haut à 90 Hz.
- **Macros** : `Punch` LFO 1 → CUTOFF 0 → +20 · `Dirt` MIX de la Distortion 0 → 70 % · `Tail` decay d'ENV 1 150 → 500 ms · `Tone` CUTOFF 150 → 800 Hz.
- **Sub associé** : S01. Selon la page, le filtre « retire un peu de sub » : il est séparé de toute façon.
- **Origine** :
  - toutes les valeurs [SOURCE F07-23, page MusicRadar ; captures non lues] ;
  - c'était Serum FX sur une piste audio, donc les noms Serum 2 sont à vérifier ;
  - les quantités +10, −20, +40, +20 sont des quantités de matrice sans échelle donnée.

### P15 Acid Ladder accentuée — Tech House acid
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - FILTER 1 en Acid Ladder, CUTOFF ≈ 25 %, RES 50-65 %, VAR (SMOOTH) bas.
  - ENV 2 → CUTOFF +40 %, attaque 0, decay 150-250 ms, sustain 0.
  - Matrice : Velocity → quantité ENV 2 → CUTOFF (si la destination l'accepte), sinon Velocity → CUTOFF +15 % : les notes à 127 servent d'accent.
  - VOICING MONO, PORTA 40-70 ms, SCALED.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −4 dB, release 60 ms.
- **FX** : Distortion Tube DRIVE 30-50, puis Compressor Multiband modéré, puis passe-haut à 90 Hz.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 70 % · `Dirt` DRIVE 0 → 80 · `Tail` decay d'ENV 2 80 → 400 ms · `Tone` CUTOFF 10 → 50 %.
- **Sub associé** : S02.
- **Jeu** : motif « Tech House 126 — acid roulant », accents à 127 et autres notes à 90-100.
- **Origine** :
  - Acid Ladder, ladder à diodes « ubiquitous in acid music » [cartographie, § 6] ;
  - « Ladder Acid : couleur plus agressive » [SOURCE GEN-06, variante] ;
  - réglages [ORIGINAL].

### P16 Carré « 80s » — Nu-disco House
- **Patch** : P01, avec OSC A sur la frame carrée de Basic Shapes.
- **ENV 1** : attaque 2 ms, decay 250 ms, sustain −10 dB, release 80 ms.
- **FX** : comme P01, avec une Distortion plus basse (DRIVE ≈ 15) et un Chorus en mode HPF à faible MIX (10-15 %) pour l'air.
- **Macros** : celles de P01, et `Dirt` sur le MIX du Chorus 0 → 25 %.
- **Sub associé** : S03, triangle sous carré.
- **Jeu** : octaves alternées en croches (Fa1-Fa2), comme une basse disco.
- **Origine** : « carré au lieu de la scie : basse plus ronde, “80s” » [SOURCE GEN-06, variante] ; Chorus et octaves [ORIGINAL].

### P17 Wide FM — Deep House, Tech House
- **Patch** :
  - OSC A sur la frame carrée de Basic Shapes, OCT −1, Unison 3, DETUNE bas.
  - OSC B en scie, même octave, LEVEL bas, source FM.
  - WARP 1 d'OSC A en FM (B), 10-25 %.
  - FILTER 1 sur A et B, MG Low 24, DRIVE et FAT montés. ENV 2 → CUTOFF.
- **ENV 1** : attaque 2 ms, decay 350 ms, sustain −6 dB, release 100 ms.
- **FX** : Equalizer en passe-haut à 120 Hz, à cause de l'unison, et bande haute en High Shelf −3 dB vers 4 kHz. Puis Utility MONO BASS à 150 Hz.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 50 % · `Dirt` quantité de FM 0 → 35 % · `Tail` decay d'ENV 1 150 → 500 ms · `Tone` CUTOFF 25 → 60 %.
- **Sub associé** : S01.
- **Origine** :
  - geste dit : A carré à −2 avec unison 3, B saw à −2, FM from B, filtre A+B, ENV 2 vers cutoff, drive/fat, EQ retirant un peu de grave et d'aigu [SOURCE Sam Smyers « 5 Deep House Basses », transcription, `sources-videos.md`, Serum 1] ;
  - octave −1 au lieu de −2 et valeurs [ORIGINAL], parce que la couche est médium.

### P18 Distorsion dynamique — l'attaque sature, le corps reste propre
- **Patch** : P01 sans le compresseur, puis :
  - ENV 3 → DRIVE de la Distortion, +30 à +50, attaque 0, decay 40-100 ms, sustain 0.
  - Distortion en Tube ou Diode 2, DRIVE de base 10-15.
- **ENV 1** : attaque 1 ms, decay 250 ms, sustain −10 dB, release 80 ms. Sustain bas, decay tiré, pour que l'attaque frappe plus que le corps.
- **FX** : Distortion, puis Compressor Multiband modéré, puis passe-haut à 90 Hz.
- **Macros** : `Punch` ENV 3 → DRIVE 0 → 60 · `Dirt` DRIVE de base 0 → 40 · `Tail` decay d'ENV 1 120 → 400 ms · `Tone` CUTOFF 25 → 60 %.
- **Sub associé** : S11.
- **Test** : l'attaque doit sortir sans que le niveau moyen monte ; comparer `Punch` à 0 et à 60 à niveau égal.
- **Origine** :
  - « distorsion dynamique », enveloppe sur le drive pour un pic à l'attaque [SOURCE F05-02] ;
  - la distorsion est sensible au niveau, d'où une enveloppe d'amplitude à sustain bas [SOURCE F05-03] ;
  - valeurs [ORIGINAL].

### P19 Blip de hauteur — Bass House
- **Patch** : P01, plus ENV 3 → CRS d'OSC A : +5 à +12 demi-tons au pic, attaque 0, decay 20-40 ms, sustain 0.
- **ENV 1** : comme P01.
- **Macros** : `Punch` quantité d'ENV 3 → CRS 0 → +12 st · `Dirt` DRIVE 0 → 50 · `Tail` decay d'ENV 1 150 → 600 ms · `Tone` CUTOFF 25 → 60 %.
- **Sub associé** : S01. L'excursion reste dans la couche médium, jamais dans le sub (`../families.md`, fiche 9).
- **Jeu** : sur la première note d'un motif seulement. Automatiser `Punch` dans Live : à 0 pour les autres notes.
- **Origine** :
  - F05-12 conseille un pitch bend dessiné dans l'enveloppe de clip de Live pour donner de l'attaque à la première note d'un motif [SOURCE F05-12] ;
  - transposition dans une enveloppe de Serum [ORIGINAL].

### P20 Saw MG Dirty — Tech House organique
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - FILTER 1 en MG Dirty, CUTOFF ≈ 35 %, RES 20-30 %, VAR (PAIN) 20-50 %.
  - ENV 2 → CUTOFF +30 %, decay 200 ms.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −6 dB, release 90 ms.
- **FX** : Equalizer en passe-haut à 90 Hz et léger creux vers 300 Hz (−2 dB), puis Compressor Single 3:1. Pas d'autre saturation : le filtre en fait office.
- **Macros** : `Punch` ENV 2 → CUTOFF 0 → 50 % · `Dirt` PAIN 0 → 80 % · `Tail` decay d'ENV 1 150 → 500 ms · `Tone` CUTOFF 20 → 60 %.
- **Sub associé** : S03 ou S13 sous 124 BPM.
- **Origine** :
  - MG Dirty, « MG Ladder avec toute sa distorsion, circuit en surcharge », VAR = PAIN [cartographie, § 6] ;
  - réglages [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Kick supposé sur les quatre temps (doubles croches 1, 5, 9, 13). Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f05-saw-percussive.md`. La notation Producer Pal s'obtient avec `--fichier references/recettes/house-f05-saw-percussive.md --titre <titre> --format ppal`, et `--transposer N` donne la tonalité du Set.

```grille
titre: Bass House 128 — mi phrygien (P05)
tempo: 128
accords: Em | Em
mid: E1[1e:1] F1[1a:1] E1[2&:1] E1[3:2] E1[3a:1] B1[4&:2] | E1[1:2] E1[1a:1] E1[2&:1] G1[3:2] F1![3a:1]
sub: E0[1e:1] F0[1a:1] E0[2&:1] E0[3:2] E0[3a:1] B0[4&:2] | E0[1:2] E0[1a:1] E0[2&:1] G0[3:2] F0![3a:1]
```

Rythme relevé sur la capture du motif final de F05-12, à une double croche près : écarts de 2-3-2-3-3-2-3-3-2-3 doubles croches. La source écrit la ligne en E0-B0 sur un sinus ; ici, elle est doublée : couche médium une octave au-dessus et sub sur la piste à part. Trois attaques tombent sur un kick (3 de la mesure 1, 1 et 3 de la mesure 2) : il faut un sidechain ou le creux de S10. Le fa final (seconde mineure) est la couleur phrygienne voulue, marquée « ! ».

```grille
titre: Tech House 126 — acid roulant (P03, P15)
tempo: 126
accords: Gm7 | Gm7
acid: G1[1e:1] G1[1&:1] Bb1[1a:1] G1[2e:1] G2[2&:1] G1[2a:1] F1[3e:1] G1[3&:1] D2[3a:1] G1[4e:1] Bb1[4&:1] C2![4a:1] | G1[1e:1] G1[1&:1] G2[1a:1] G1[2e:1] F1[2&:1] G1[2a:1] Bb1[3e:1] G1[3&:1] G1[3a:1] D2[4e:1] C2[4&:1] Bb1[4a:1]
sub: G0[1&:2] G0[2&:2] F0[3&:2] G0[4&:2] | G0[1&:2] F0[2&:2] Bb0[3&:2] G0[4&:2]
```

Pour P03 et P15, PORTA en ALWAYS fait glisser sans chevauchement. Accents (vélocité 127) sur G2 et D2, autres notes à 90-100. Le C2 de fin de mesure 1 est une note de passage voulue vers la mesure suivante.

```grille
titre: Tech House 124 — appel et réponse (P01, P02, P11)
tempo: 124
accords: Fm7 | Fm7
mid: F1[1e:1] F1[1&:2] Ab1[2&:1] F1[2a:1] C2[3&:2] Eb2[4e:1] F1[4&:2] | F1[1e:1] F1[1&:2] Ab1[2&:1] F1[2a:1] Eb1[3&:3] C1[4&:2]
sub: F0[1&:2] F0[2&:2] C1[3&:2] F0[4&:2] | F0[1&:2] F0[2&:2] Eb0[3&:3] C1[4&:2]
```

Le sub ne joue que les contretemps (S11 ou S01) ; la couche médium ajoute les doubles croches « e » et « a ». Pour P11, remplacer la mesure 2 de la couche médium par une tenue F1[1&:7] découpée par le LFO.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : la table « AT Model D », le réglage d'usine « 1176 Glue » du Compressor, l'IR « Cab 2 », les filtres SampHold, L/B/H 24, Acid Ladder et MG Dirty. Vérifier que chaque macro accepte sa destination.
- Écouter chaque recette avec son sub (protocole des règles communes) et en garder trois à cinq pour le morceau.
- Consigner le preset retenu et ses macros dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
