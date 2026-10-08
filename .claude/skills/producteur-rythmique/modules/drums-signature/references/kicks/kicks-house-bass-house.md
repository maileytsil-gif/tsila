# Vingt recettes de kick Serum 2 pour la house, la bass house et la tech house

Deuxième lot de kicks : les kicks 4/4 de 124 à 130 BPM, propres et punchy en house, plus serrés et plus saturés en bass house, « thumpy » en tech house. À 124 BPM et au-dessus, la signature douce reste une option (`kicks-signature-sous-124.md`), pas une obligation. Rédigé le 05/10/2026. Sources :
- `../kicks-serum-tutoriels.md`, fiches BH (bass house), HC (house classique) et TH (tech house), et sa synthèse `../kicks-serum-synthese.md` ;
- `../../../kick-bass-equilibre/GUIDE.md` ;
- la cartographie de Serum 2 (`../../../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `kicks-signature-sous-124.md`.

## Règles

1. **Règles communes du lot de kicks** : celles de `kicks-signature-sous-124.md` (architecture, voicing, phase, accord et octave, longueur, chute unipolaire, macros `Pitch Decay`, `Cutoff Decay`, `Click`, `Release`, plug-ins tiers après Serum, contrôle, validation).
2. **Le corpus** : aucun tutoriel ne conçoit un kick « bass house » dans Serum ; les fiches BH sont des kicks EDM génériques au rendu punchy, clicky ou saturé. Les fiches TH reprennent pour la plupart des vidéos déjà classées en HC ou BH (TH-01 = HC-04, TH-02 = HC-05, TH-03 = HC-03, TH-04 = HC-06, TH-05 = BH-04, TH-06 = HC-09, TH-07 = BH-05, TH-08 = HC-10, TH-09 = DM-05) : chaque recette cite l'identifiant d'origine.
3. **Durées** [CALCUL] :

   | Tempo | Noire | Croche | Double croche |
   | --- | --- | --- | --- |
   | 124 BPM | 483,9 ms | 241,9 ms | 121,0 ms |
   | 126 BPM | 476,2 ms | 238,1 ms | 119,0 ms |
   | 128 BPM | 468,8 ms | 234,4 ms | 117,2 ms |
   | 130 BPM | 461,5 ms | 230,8 ms | 115,4 ms |

4. **Queue courte s'il y a une basse, queue longue si le kick porte le sub** [SOURCE BH-02]. En bass house, la basse médium et le sub sont chargés : kick court, d'une croche au plus.
5. **Accord.** Plusieurs tutoriels jouent le kick en G0 (49,0 Hz) [SOURCE BH-01, HC-01] : il descend alors dans le registre du sub. Avec un sub séparé (règle « Grave » d'`AGENTS.md`), garder le corps du kick entre 60 et 100 Hz, sur la tonique ou la quinte, une octave au-dessus du sub (`../../../kick-bass-equilibre/GUIDE.md` § 1-2), ou garder G0 et mesurer la corrélation kick-sub.
6. **Distorsion sur le transitoire seulement** : une enveloppe courte → DRIVE (et MIX) [SOURCE BH-01, HC-02, HC-06, HC-12] ; pré-filtre de la distorsion en passe-haut pour épargner le sub [SOURCE HC-12].
7. **Effets natifs filmés** : OTT, Glue Compressor, Saturator, Drum Buss de Live [SOURCE HC-01, HC-03, HC-04]. Non repris : saturation, compression et clip passent par des plug-ins tiers (règle 6 d'`ableton-live-session`).

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| KH01 | Kick house de référence | toutes | BD Sine, chute de 12-24 demi-tons, creux à 300 Hz |
| KH02 | Kick punchy W. A. Production | bass house | LFO 4 multipoint, Coarse ≈ 25, clic n° 2, Monster 4 en FM |
| KH03 | Kick EDM Strob Studio | bass house, EDM | Master Tune, creux d'amplitude, clic de second sinus, scie de queue |
| KH04 | Kick dur MHA | bass house dure | beaucoup de distorsion, punch de hauteur dur |
| KH05 | Kick hard clip Wildcrow | bass house | deux sinus, Hard Clip 100 %, Bend+ |
| KH06 | Kick moderne Mixup Studio | bass house, G-house | couche Monster, clic n° 6 |
| KH07 | Kick FM DONKONG | bass house | FM brève depuis B, courbe médiane, soft clip |
| KH08 | Kick Serum 2 TURNCLOAK | bass house « funky » | Overdrive empilé, hi-hat en transitoire |
| KH09 | Kick 808 court Proper Villains | house, techno | G0, clic n° 6 proche de la TR |
| KH10 | Kick TR-808 WhenJekyllHides | house classique | BD Sine à deux octaves, passe-haut à 130 Hz |
| KH11 | Kick chunky SKETIMUSIC | house, tech house | longueur d'une croche, multibande, FM triangle |
| KH12 | Kick tech house W. A. Production | tech house | hauteur fixe, phase 156, distorsion à mix réduit |
| KH13 | Kick thumpy MERAKKI | tech house | Overdrive stack 2, Splitter, convolution |
| KH14 | Kick PML accordé | house, tech house | LFO en Hz, transitoire carré à +2 octaves |
| KH15 | Kick 909 de base | house classique | Ozgun avant la distorsion |
| KH16 | Kick propre Produciamo | house | ENV 3 sur le filtre, distorsion par le mix |
| KH17 | Kick serré sous une basse chargée | bass house | hold 40, decay 90 |
| KH18 | Kick à transitoire distordu | toutes | enveloppe → DRIVE, pré-filtre passe-haut |
| KH19 | Kick imprimé et compressé en parallèle | toutes | impression, compression parallèle 50 % |
| KH20 | Kick qui roule avant la frontière | variation avant la frontière | doubles croches sur le temps 4 |

## Les vingt recettes

### KH01 Kick house de référence
- **OSC A** : Analog_BD_Sin, OCT −2, RAND 0, PHASE 90° (petit clic) ; MONO ; qualité au maximum.
- **Fondamentale** : C1 (65,4 Hz) sous un sub en F0 ; D1 (73,4 Hz) sous un sub en G0 [CALCUL, `theorie.py sub`].
- **Hauteur** : ENV 2 → CRS, unipolaire, chute de 12 à 24 demi-tons ; ENV 2 : decay 80 ms, sustain 0.
- **Amplitude** : ENV 1 : attaque 0,5 ms, hold 50 ms, decay 120-150 ms, sustain −∞ : moins d'une croche (238 ms à 126 BPM) [CALCUL].
- **Clic** : NOISE, Attacks › Kick, one-shot ; n° 2, 6, 11 ou 15 selon le clic voulu [SOURCE BH-01, HC-01, HC-08].
- **Corps** : FILTER 1 en passe-bas avec DRIVE, ENV 2 → CUTOFF.
- **FX** : Distortion, ENV 3 courte → DRIVE ; EQ : creux vers 300 Hz, coupe vers 500 Hz si les médiums débordent.
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` quantité d'ENV 2 → CUTOFF · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Origine** : architecture commune de `../kicks-serum-synthese.md` ; EQ [SOURCE HC-03, HC-04, BH-01] ; valeurs [ORIGINAL].

### KH02 Kick punchy W. A. Production — LFO 4 multipoint, Monster 4 en FM
- **OSC A** : table Analog « sine » à légères harmoniques (probablement Analog_BD_Sin), RAND 0.
- **Hauteur** : LFO 4 (il accepte plusieurs points), forme très courte, accéléré → Coarse d'A, unipolaire (sinon le pitch descend sous la note), « around 25 ».
- **Note** : G0 dans la vidéo.
- **Clic** : NOISE, catégorie « kick attacks », one-shot, n° 2 (n° 15 bon aussi).
- **FILTER 1** : allumé sans filtrer, pour le DRIVE seulement (harmoniques) ; MIX baissé plutôt que le master ; le NOISE passe aussi dans le filtre.
- **OSC B** : table « Monster 4 », FM depuis A, pour un bruit court ; courbe retouchée dans la matrice ; RAND 0.
- **FX** : Distortion, ENV 2 (decay ≈ 100-130 ms) → DRIVE : seul le transitoire est distordu ; MIX baissé. EQ : coupe vers 500 Hz.
- **Macros** : `Pitch Decay` RATE de LFO 4 · `Cutoff Decay` DRIVE du filtre · `Click` LEVEL de B · `Release` decay d'ENV 1.
- **Origine** : [SOURCE BH-01, Serum 1] : « regular house kick drum » d'après la description, kick EDM et dubstep d'après le titre.

### KH03 Kick EDM Strob Studio — Master Tune, creux d'amplitude, scie de queue
- **OSC A** : sinus ; une octave plus bas ; fondamentale entre 45 et 60-65 Hz.
- **Hauteur** : LFO 1 en ENVELOPE, plusieurs points → Global › Master Tune, unipolaire.
- **Amplitude** : LFO 2 en ENVELOPE, plusieurs points → volume : un creux juste après le clic, puis une remontée pour la queue.
- **Clic** : un second sinus deux octaves au-dessus, joué seulement sur une transition très courte au début ; RAND 0.
- **Queue** : OSC B en scie, dans le filtre ; LFO 4 en ENVELOPE, 1/4 → LEVEL de B : il laisse passer le punch puis remplit derrière, « comme un sidechain ».
- **Plus de clic** : harmoniques et warp, ou NOISE (attaques de kick, one-shot) pitché haut.
- **Après Serum** (plug-ins tiers) : impression en audio ; compression parallèle rapide, attaque au minimum, MIX 50 ; EQ : extrême aigu coupé, résonance du clic retirée, bas-médium en option ; cloche étroite vers 70 Hz automatisée sur le punch seulement, sur une noire.
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` profondeur de LFO 4 → LEVEL de B · `Click` LEVEL du second sinus · `Release` dernier point de LFO 2.
- **Origine** : [SOURCE BH-02, Strob Studio, Serum 1, en français] : « queue courte s'il y a une basse, queue longue si le kick porte le sub ».

### KH04 Kick dur MHA — beaucoup de distorsion
- **OSC A** : Analog « BD Sine », deux octaves plus bas (le SUB marche aussi) ; ENV 1 = l'ADSR du kick.
- **Bruit** : un peu de NOISE blanc, ENV 1 → LEVEL du NOISE, en petite quantité.
- **Hauteur** : LFO 1 en ENVELOPE → Global › Master Tune, une seule flèche (unipolaire) ; LFO plutôt qu'ENV, pour placer des points ; punch de hauteur dur.
- **FX** : Distortion (« quite a lot of distortion »), puis Compressor.
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` — · `Click` DRIVE · `Release` decay d'ENV 1.
- **Usage** : bass house dure, future house ; à doser.
- **Origine** : [SOURCE BH-03, MHA, Serum 1], partie kick (1:03-3:30) : « standard aggressive nice kick ».

### KH05 Kick hard clip Wildcrow — deux sinus, Bend+
- **Patch** : KS08 de `kicks-signature-sous-124.md` (deux sinus : A pour le clic, B pour le corps, quatre LFO en ENVELOPE), **puis** :
  - Distortion Hard Clip, MIX 100 % (Tube distord trop) ;
  - EQ : légère coupe dans les médiums de l'attaque ; baisser l'oscillateur trop fort ;
  - NOISE Bright White, enveloppe à sustain minimal, réglée par le decay ;
  - WARP Bend+ pour un kick plus agressif.
- **Accord** : GTune ; décaler d'un demi-ton pour la tonalité du morceau.
- **Macros** : `Pitch Decay` RATE de LFO 1 · `Cutoff Decay` RATE de LFO 3 · `Click` niveau du NOISE · `Release` quantité de Bend+.
- **Origine** : [SOURCE BH-04 = TH-05, Wildcrow Studio, Serum 1].

### KH06 Kick moderne Mixup Studio — couche Monster
- **OSC A** : sinus par défaut ; ENV 2 très rapide → CRS, unipolaire ; ENV 1 : sustain baissé, decay « dans les 80 », hold augmenté ; RAND de 100 à 0, phase sur une bosse du sinus pour plus d'attaque.
- **OSC B** : table « Monster » (catégorie Spectral), RAND 0, phase retouchée, position balayée ; ENV 3 (decay « 624 ms », lecture douteuse) → LEVEL de B, quantité réduite ; ENV 2 aussi → hauteur de B.
- **Clic** : NOISE, kick attack n° 6, one-shot.
- **FX** : Distortion, pas à fond.
- **Après Serum** : compresseur, saturation de console, clipper (KClip 3 en mode Tape, ≈ 1 dB) : plug-ins tiers.
- **Accord** : sur la tonalité du morceau (exemple : D).
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` decay d'ENV 3 · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Origine** : [SOURCE BH-05 = TH-07, Mixup Studio, Serum 1, en français].

### KH07 Kick FM DONKONG — FM brève depuis B
- **OSC A** et **OSC B** : sinus ; A en FM (B), B à volume nul (modulateur seulement).
- **Hauteur** : LFO en ENVELOPE, 1/8 → pitch ; courbe au milieu : bombée vers le haut = « gabber », vers le bas = « 808 ».
- **Phase** : même départ, RAND baissé, pas d'attaque, ce qui crée un clic ; une macro sur la PHASE règle ce clic.
- **FM** : quantité de FM depuis B par un LFO enveloppe très rapide, seulement au début, unipolaire ; une macro dessus ; jouer aussi sur l'octave de B.
- **Amplitude** : LFO en ENVELOPE → LEVEL, longueur de 1/8 ou 1/16 ; la vidéo est à 158 BPM, où 1/8 dure 190 ms et 1/16 dure 95 ms. À 126 BPM, 1/8 dure 238 ms : pour garder la même durée, régler le LFO en Hz plutôt qu'en division (190 ms = 1,6 double croche à 126 BPM) [CALCUL].
- **FX** : soft clip final, pour un punch dur et une queue propre.
- **Macros** : `Pitch Decay` RATE du LFO de hauteur · `Cutoff Decay` — · `Click` PHASE (macro de la source) · `Release` quantité de FM (macro de la source).
- **Origine** : [SOURCE BH-06, DONKONG, Serum 1, 158 BPM].

### KH08 Kick Serum 2 TURNCLOAK — Overdrive empilé, hi-hat en transitoire
- **Patch** :
  - sinus, LFO ou ENV → pitch, quantité au maximum, enveloppe de volume ; RAND et PHASE à 0 ;
  - transitoire en bruit blanc ; filtre passe-bas sur A, une enveloppe réutilisée sur le NOISE ;
  - petit décalage entre le transitoire d'A et le NOISE ; NOISE dans FILTER 2 en passe-haut ;
  - variante : un sample de hi-hat chargé dans l'oscillateur comme transitoire, enveloppe courte, FM depuis le NOISE.
- **FX** : Distortion pour souder (enveloppe raccourcie pour que le sub ne sature pas) ; deux Compressor, le second fait ressortir le transitoire ; EQ en coupes étroites dans le bas-médium, boosts larges ; Overdrive empilé (« stacked »).
- **Macros** : `Pitch Decay` decay de l'enveloppe de hauteur · `Cutoff Decay` CUTOFF du passe-bas · `Click` niveau du NOISE · `Release` decay de l'enveloppe de volume.
- **Test** : la vidéo ne donne presque aucun chiffre ; tout est à régler à l'oreille.
- **Origine** : [SOURCE BH-07, TURNCLOAK, Serum 2, choix faible] : « funky basses territory ».

### KH09 Kick 808 court Proper Villains — G0, clic proche de la TR
- **OSC A** : Analog › Basic Shapes, sinus ; pattern en noires sur G0.
- **Amplitude** : LFO 1 en ENVELOPE → LEVEL, forme triangle un peu concave avec un point ajouté ; le kick finit tôt pour laisser la place à la basse.
- **Hauteur** : LFO 2 en ENVELOPE → Coarse, unipolaire, environ deux octaves ; BPM désactivé, RATE = vitesse du transitoire.
- **Phase** : random coupé, départ toujours au même endroit.
- **Clic** : NOISE › Attacks › Kicks n° 6, « proche du clic de la TR », one-shot, pitch ajusté.
- **Variantes dites** : autres attaques ; triangle « 90's-ish » ; carré dans un passe-bas avec LFO 2 → CUTOFF pour un son « thuddy » d'electro breaks.
- **Basse** : l'auteur écrit sa basse en si bémol ou en ré sous un kick en sol (relation harmonique plutôt que même fondamentale).
- **Après Serum** : Glue Compressor, Saturator et EQ de Live dans la vidéo ; ici plug-ins tiers.
- **Macros** : `Pitch Decay` RATE de LFO 2 · `Cutoff Decay` — · `Click` niveau du NOISE · `Release` dernier point de LFO 1.
- **Origine** : [SOURCE HC-01, Sound Collective NYC, Serum 1] : 808 court « you'd use in techno or house ».

### KH10 Kick TR-808 WhenJekyllHides — deux BD Sine, passe-haut à 130 Hz
- **OSC A** : « Analog BD Sine », PHASE 0, RAND 0, position réglable.
- **OSC B** : BD Sine une octave plus haut, PHASE 0, RAND 0 ; FILTER en High 24 sur B seul, CUTOFF « disons 130 » Hz, RES 0, un peu de DRIVE.
- **Hauteur** : LFO en ENVELOPE à 1/4 (ou en Hz) → Coarse d'A et de B, unipolaire, quantité « 48 » pour la marge, puis réduite (sinon le son tourne au « laser »).
- **FX** : Distortion Tube, un LFO → DRIVE et MIX, seulement à l'impact.
- **Clic** : NOISE Analog « Bright White », LFO → LEVEL sur l'impact (aide sur les petits haut-parleurs).
- **Global** : MONO, glide optionnel ; macro « spread » = désaccord d'unison de B dans les aigus.
- **Amplitude** : la vidéo vise un 808 long (decay « une seconde et demie », sustain coupé). **Pour la house** : ENV 1 decay 200 ms, sous la croche [ORIGINAL].
- **Macros** : `Pitch Decay` RATE du LFO de hauteur · `Cutoff Decay` CUTOFF du High 24 de B · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Origine** : [SOURCE HC-02, WhenJekyllHides, Serum 1, en français, preset gratuit] ; durée house [ORIGINAL].

### KH11 Kick chunky SKETIMUSIC — longueur d'une croche
- **Patch** : KS04 de `kicks-signature-sous-124.md` (Analog_BD_Sin, LFO 1 → Master Tune, MG Low 18, Soft Clip), avec en plus :
  - Compressor en mode Multiband : bande haute à 0, médiums montés (corps entre 80 et 2 000 Hz), bas montés ;
  - OSC B en triangle à +1 octave ; FM (B) sur A, quantité pilotée par un LFO à chute rapide ; deux octaves d'écart conseillées ;
  - longueur d'une croche : à 126 BPM, hold ≈ 119 ms, decay ≈ 119 ms [CALCUL, × 125/126].
- **Non repris** : OTT, Glue Compressor en soft clip et EQ de Live (natifs).
- **Macros** : celles de KS04 ; `Click` → quantité de FM.
- **Origine** : [SOURCE HC-03 = TH-03, SKETIMUSIC, Serum 1, testé à 125 BPM] : kick « big and chunky ».

### KH12 Kick tech house W. A. Production — hauteur fixe, phase 156
- **OSC A** : Analog BD Sine ; pitch tracking de l'oscillateur désactivé, compensé de +2 octaves : même son quelle que soit la note.
- **Hauteur** : LFO en ENVELOPE, rate 1/8 → Coarse ; forme en deux zones, le transitoire puis la « hardness » (décroissance).
- **Warp** : Bend+ ou Bend−, ≈ 10 %.
- **Phase** : RAND de 100 % à 0, départ à « 156 ».
- **FX** :
  1. Compressor Multiband, bas montés « to about 150 » (unité non dite).
  2. Distortion, LFO 4 → DRIVE, MIX réduit pour garder un sub propre, filtre post en passe-bas ; le même LFO 4 pilote le CUTOFF du filtre principal.
  3. EQ : coupe vers 300 Hz, retouche du haut-médium.
- **Non repris** : Drum Buss et Saturator de Live.
- **Macros** : `Pitch Decay` RATE du LFO de hauteur · `Cutoff Decay` profondeur de LFO 4 · `Click` quantité de Bend · `Release` decay de l'enveloppe d'amplitude.
- **Origine** : [SOURCE HC-04 = TH-01, W. A. Production, Serum 1, 130 BPM] : « Techno / Tech House Kick ».

### KH13 Kick thumpy MERAKKI — Overdrive, Splitter, convolution
- **OSC A** : sinus, registre grave ; RAND 0, attaque 0,1 ms, PHASE 90°.
- **Hauteur** : LFO en ENVELOPE, 1/8 plus court → Coarse, unipolaire ; un second LFO à 1/16 → Coarse, unipolaire.
- **NOISE** : couleur blanche, un peu de stéréo, son filtre intégré monté, enveloppe rapide.
- **OSC B** et **OSC C** : l'un à volume nul comme modulateur FM, octave baissée sur l'autre, RAND 0 ; une table générée en tapant « kick » dans l'éditeur ; enveloppe courte, passe-haut, A hors du filtre ; FM ou PD depuis C (modulateur en scie).
- **FX** :
  1. Distortion Overdrive (nouveau dans Serum 2), stack 2, filtre intégré en post et en passe-haut, MIX réduit.
  2. Splitter, Distortion Tube sur les aigus, MIX baissé.
  3. Reverb à convolution sur les aigus seulement, LFO enveloppe sur le MIX.
- **Macros** : `Pitch Decay` RATE du LFO 1/8 · `Cutoff Decay` MIX de la convolution · `Click` niveau du NOISE · `Release` dernier point du LFO de volume.
- **Origine** : [SOURCE HC-05 = TH-02, MERAKKI, Serum 2], second kick, « tech house or techno ».

### KH14 Kick PML accordé — LFO en Hz, transitoire carré
- **OSC A** : sinus par défaut ; LFO 1 en ENVELOPE → LEVEL, niveau de base à 0, randomness à 0 ; LFO 1 en Hz pour régler la longueur précisément.
- **Hauteur** : LFO 2 en ENVELOPE → CRS, courbe ajoutée, unipolaire ; en Hz plutôt qu'en BPM.
- **Transitoire** : OSC B à +2 octaves, table poussée vers le carré ; LFO 3 en ENVELOPE, en Hz, très rapide → LEVEL de B ; randomness et phase ajustées.
- **Variante** : OSC C en sample, Factory › non-tonal noises › attack, LEVEL 0 modulé par LFO 3.
- **FX** : Distortion « à 9 heures », LFO 3 → DRIVE (seulement sur le transitoire) ; FILTER sur A, B et C, CUTOFF « vers 3 heures », un peu de RES.
- **Accord** : en G dans la vidéo.
- **Macros** : `Pitch Decay` RATE de LFO 2 · `Cutoff Decay` CUTOFF du filtre · `Click` profondeur de LFO 3 · `Release` RATE de LFO 1.
- **Origine** : [SOURCE HC-06 = TH-04 = AF-02, Production Music Live, Serum 2].

### KH15 Kick 909 de base — Ozgun avant la distorsion
- **OSC A** : table Analog sine (BD Sine) ; volume baissé ; LFO 1 en ENVELOPE → LEVEL ; kick pas plus long qu'une demi-mesure.
- **Hauteur** : LFO 2 → Coarse, unipolaire, le point le plus bas finit sur la note ; décaler vers la droite donne plus de punch.
- **Phase** : RAND coupé.
- **Mouvement** : LFO 3 court → position de table.
- **OSC B** : une octave plus haut, table « digital », volume bas, LFO → LEVEL et position.
- **Clic** : NOISE, kick attack, one-shot, même LFO.
- **Arrêt** : avant la Distortion Tube ; « without distortion it's just basic 909 kick ».
- **Note** : F1 vérifiée dans SPAN.
- **Macros** : `Pitch Decay` RATE de LFO 2 · `Cutoff Decay` profondeur de LFO 3 · `Click` niveau du NOISE · `Release` RATE de LFO 1.
- **Origine** : [SOURCE HC-12, Ozgun, Serum 1], partie de base jusqu'à 5:59 ; la suite techno est au lot techno.

### KH16 Kick propre Produciamo — filtre et distorsion par le mix
- **OSC A** : Analog › Basic Shapes, sinus ; MONO ; qualité de Global à « 4 » ; ENV 1 : sustain 0, hold un peu allongé, decay raccourci, OCT −1, attaque et release légèrement montées contre les clics.
- **Clic** : NOISE avec des samples d'attaque (« la punta » du kick).
- **Hauteur** : ENV 2 → pitch, flèche simple, quantité « sans exagérer ».
- **Filtre** : ENV 3 ou LFO en ENVELOPE → CUTOFF, léger mouvement qui nettoie les aigus.
- **FX** : Distortion, un LFO → MIX.
- **Après Serum** (plug-ins tiers) : coupe sous 20 Hz, quelques dB en moins vers 500 Hz, aigus montés pour l'attaque, transient shaper, soft clip, saturation, limiteur.
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` decay d'ENV 3 · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Origine** : [SOURCE HC-13, Produciamo.Musica, Serum 1, en italien].

### KH17 Kick serré sous une basse chargée — bass house
- **Patch** : KH01, avec ENV 1 : hold 40 ms, decay 90 ms (130 ms au total, un peu plus d'une double croche à 128 BPM, 117 ms) ; chute de hauteur de 16 demi-tons en 60 ms ; clic n° 2.
- **Jeu** : bloc « Bass House 128 — kick serré et sub entre les kicks » ci-dessous.
- **Macros** : celles de KH01.
- **Test** : le kick doit garder son attaque sous la basse médium ; sinon remonter le clic plutôt que la longueur.
- **Origine** : « queue courte s'il y a une basse » [SOURCE BH-02] ; valeurs [ORIGINAL].

### KH18 Kick à transitoire distordu — l'enveloppe sur le DRIVE
- **Patch** : KH01, avec :
  - Distortion Tube ou Hard Clip, pré-filtre en passe-haut calé au-dessus de la fondamentale (par exemple 87 Hz pour une tonalité de fa) ;
  - ENV 3 (attaque 0, decay 30-60 ms, sustain 0) → DRIVE et MIX ;
  - DRIVE de base faible.
- **Macros** : `Click` quantité d'ENV 3 → DRIVE · les autres comme KH01.
- **Test** : le sub du kick ne doit pas saturer (décroissance de l'enveloppe trop longue sinon) [SOURCE BH-07].
- **Origine** : transitoire seul distordu [SOURCE BH-01, HC-02, HC-06] ; pré-filtre calé sur la tonalité, « 87 Hz » [SOURCE HC-12] ; durée [ORIGINAL].

### KH19 Kick imprimé et compressé en parallèle
- **Méthode** :
  1. Imprimer le kick validé en audio (procédure de `../../../../../sound-designer-serum/modules/resampling/GUIDE.md`).
  2. Compression parallèle par plug-in tiers : compresseur numérique rapide, attaque au minimum, release au goût, MIX 50.
  3. EQ : cloche étroite vers 70 Hz, automatisée sur le punch seulement, une noire.
  4. Automation de gain sur la queue si besoin.
  5. Remplacer le kick MIDI par l'audio imprimé (ou un Simpler).
- **Origine** : [SOURCE BH-02] ; impression [SOURCE HC-02, HC-05].

### KH20 Kick qui roule avant la frontière — doubles croches sur le temps 4
- **Patch** : KH01 ou KH17.
- **Jeu** : sur la dernière mesure d'une phrase de huit, quatre doubles croches de kick sur le temps 4 ; le sub s'arrête au temps 4. Alterner d'une frontière à l'autre avec le retrait (KS20), un reverse ou un impact.
- **Variante** : macro `Release` au minimum pendant le roulement, pour des coups secs.
- **Jeu** : bloc « House 124 — roulement de kick avant la frontière » ci-dessous.
- **Origine** : règle « Drops » d'`AGENTS.md` (roulement) ; séquence [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60) ; les notes de kick sont les fondamentales visées (règle 4 du lot). Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/kicks/kicks-house-bass-house.md`.

```grille
titre: Bass House 128 — kick serré et sub entre les kicks (KH17)
tempo: 128
accords: Fm7 | Fm7
kick: C1[1:1] C1[2:1] C1[3:1] C1[4:1] | C1[1:1] C1[2:1] C1[3:1] C1[4:1]
sub: F0[1&:2] F0[2&:1] Ab0[2a:1] F0[3&:2] Eb0[4&:2] | F0[1&:2] F0[2&:1] C1[2a:1] F0[3&:2] F0[4&:2]
```

Kick d'une double croche (117 ms) sur les quatre temps ; le sub joue les contretemps et une anacrouse sur la dernière double croche du temps 2.

```grille
titre: Tech House 126 — kick en C1 et basse roulante (KH12, KH13)
tempo: 126
accords: Fm7 | Fm7
kick: C1[1:2] C1[2:2] C1[3:2] C1[4:2] | C1[1:2] C1[2:2] C1[3:2] C1[4:2]
basse: F1[1e:1] F1[1&:1] F1[1a:1] F1[2e:1] Ab1[2&:1] F1[2a:1] F1[3e:1] F1[3&:1] C2[3a:1] F1[4e:1] Eb2[4&:1] F1[4a:1] | F1[1e:1] F1[1&:1] F1[1a:1] F1[2e:1] Ab1[2&:1] F1[2a:1] F1[3e:1] F1[3&:1] Eb2[3a:1] F1[4e:1] C2[4&:1] Ab1[4a:1]
```

La basse roulante remplit les trois doubles croches entre deux kicks ; le kick, accordé en C1, reste au-dessus du sub (F0, sur sa piste).

```grille
titre: House 124 — roulement de kick avant la frontière (KH20)
tempo: 124
accords: Fm7 | Fm7
kick: C1[1:2] C1[2:2] C1[3:2] C1[4:2] | C1[1:2] C1[2:2] C1[3:2] C1[4:1] C1[4e:1] C1[4&:1] C1[4a:1]
sub: F0[1&:2] F0[2&:2] F0[3&:2] Ab0[4&:2] | F0[1&:2] F0[2&:2] Eb0[3&:2]
```

Mesures 7 et 8 : le temps 4 de la mesure 8 roule en doubles croches, sans sub ; le drop suivant repart sur le temps 1.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : Analog_BD_Sin, les tables « Monster 4 » et « Monster » (Spectral), les bruits Attacks › Kick n° 2, 6, 11 et 15, le sample « attack » de Factory › non-tonal noises.
- Lire à l'écran les valeurs « à vérifier » des fiches BH et HC (formes de LFO, quantités de Coarse, réglages de distorsion et d'EQ).
- Écouter les recettes avec le sub, la basse médium et le groove, à niveau égal ; mesurer kick et sub sur des exports séparés ; inscrire le kick validé au registre `../signature.md`.
