# Vingt recettes de kick Serum 2 pour la techno et la rave

Troisième lot de kicks : le style le mieux couvert par le corpus. On y trouve le 909 distordu, le rumble « warehouse », la techno industrielle, la hard techno, la tekno et le reverse bass. Plusieurs fiches sont en Serum 2. Rédigé le 05/10/2026. Sources :
- `../kicks-serum-tutoriels.md`, fiches TE (techno) et RA (rave), et sa synthèse `../kicks-serum-synthese.md` ;
- `../../../kick-bass-equilibre/SKILL.md` ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `kicks-signature-sous-124.md`.

## Règles

1. **Règles communes du lot de kicks** : celles de `kicks-signature-sous-124.md`.
2. **Doublons du corpus** : RA-01 = TE-09, RA-02 = TE-10, RA-03 = TE-04, RA-04 = TE-08, RA-05 = TE-06, RA-09 = TE-14, RA-10 = TE-13, RA-11 = TE-01, RA-13 = TE-12. Les recettes citent l'identifiant TE. Aucune vidéo UK rave, acid rave ou hardgroove ne conçoit son kick dans Serum : la « rave » du corpus est de la rave techno.
3. **Le kick tient le grave.** En techno, le kick et son rumble portent le grave ; la basse joue au-dessus ou entre les coups (`../../../kick-bass-equilibre/SKILL.md` § 1). Accord « entre F et A » [SOURCE TE-11] ; F vérifié dans SPAN [SOURCE TE-09].
4. **Tempos et durées** [CALCUL] :

   | Tempo | Noire | Croche | Double croche |
   | --- | --- | --- | --- |
   | 130 BPM | 461,5 ms | 230,8 ms | 115,4 ms |
   | 140 BPM | 428,6 ms | 214,3 ms | 107,1 ms |
   | 150 BPM | 400,0 ms | 200,0 ms | 100,0 ms |
   | 155 BPM | 387,1 ms | 193,5 ms | 96,8 ms |

   Les vidéos de hard techno et d'industriel tournent à 155 BPM [SOURCE TE-04, TE-08].
5. **Le rumble ne déborde pas sur le kick suivant** : reverb pas trop longue [SOURCE TE-02], n'imprimer que la première partie [SOURCE TE-03] ; un kick plus long qu'une demi-mesure n'est généralement pas nécessaire [SOURCE TE-09].
6. **Grave mono** : Utility de Serum 2 en Bass Mono, entre 130 et 300 Hz selon la vidéo, jamais dans le sub [SOURCE TE-05, TE-06, TE-07, RA-08] ; Splitter Mid/Side avec passe-haut sur le Side vers 300 Hz [SOURCE TE-04]. L'Utility interne de Serum n'est pas un effet natif de Live.
7. **Effets natifs de Live filmés** : Saturator, compresseur, EQ Eight et limiteur [SOURCE TE-11]. Comme pour les autres lots, ils passent par des plug-ins tiers (règle 6 d'`ableton-live-session`). Les plug-ins tiers cités par les vidéos (Trash, Decapitator, Saturn, Inflator, Pro-Q, Pro-R, Kickstart) sont à vérifier sur le Mac.
8. **Variation avant la frontière** : gestes de KS20 (retrait) et KH20 (roulement) ; en techno, couper aussi le rumble.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| KT01 | 909 techno Ozgun | techno mainstage | BD Sine, Tube, pré-EQ calé sur 87 Hz |
| KT02 | Kick techno distordu Ozgun | techno | trou pour le clic, couche Digital à +1 octave |
| KT03 | Rumble warehouse Serum 2 | techno warehouse | rééchantillonnage interne, Convolve, sidechain interne |
| KT04 | Warehouse bunker Strob | techno warehouse | bruit pitché en queue, multibande piloté |
| KT05 | Rumble en couches Strob | techno rumble | même kick en trois couches imprimées |
| KT06 | Industriel Teknovault | techno industrielle | BN12, all-pass, Sine Shaper, couche snare |
| KT07 | Rumble en one-shots Teknovault | techno rumble | samples « duda », Hall, Soft Saturator |
| KT08 | Hard techno Krosper | hard techno | trois LFO de hauteur, Diode, deux Soft Clip |
| KT09 | Industriel Krosper | hard techno industrielle | deux Comb, Sine Shaper, Hard Clip |
| KT10 | Industriel en samples 909 | techno industrielle | trois 909 d'usine, Overdrive, delay avant reverb |
| KT11 | Hard techno en 4 minutes | hard techno | hold, decay 80 ms, ENV 2 de 60 ms |
| KT12 | Techno OddWave | techno | bruit d'attaque comme couleur principale |
| KT13 | Warehouse Lachie | techno warehouse | LFO dessiné sur deux cibles, filtre avant saturation |
| KT14 | Hard techno AKA Sounds | hard techno | transitoire « laser », LP Drive et Fat au maximum |
| KT15 | Hyper techno baltic audio | hyper techno | toutes les valeurs écrites dans la description |
| KT16 | Reverse bass rave | hard rave | punch imprimé et crunch en contretemps |
| KT17 | Hardtekk Krosper | hardtekk | trois couches de sinus, deux bus |
| KT18 | Kick gaté Krosper | hard techno | reverb gatée par LFO, EQ « hollow » |
| KT19 | Tekno Fuzzey | tekno, free party | Rate du LFO = transitoire, decay = longueur |
| KT20 | Industriel Teknovault en deux couches | hard techno industrielle | deux scies, Flanger, reverb inversée |

## Les vingt recettes

### KT01 909 techno Ozgun — le 909 distordu
- **Base** : KH15 de `kicks-house-bass-house.md` (BD Sine, LFO 1 → LEVEL, LFO 2 → Coarse finissant sur la note, LFO 3 → position, OSC B Digital à +1 octave, clic de kick attack).
- **Note** : F1, vérifiée dans SPAN ; le point bas de la hauteur finit sur F.
- **Distorsion** : Distortion Tube, un LFO → DRIVE.
- **EQ avant la distorsion** : la deuxième octave de fa vaut 87 Hz (il dit d'abord 89) ; filtres high et low cut à partir de là, résonance montée vers 87-89 Hz : on retire le grave et on nourrit la distorsion avec le haut.
- **Amplitude** : couper un peu le début de l'enveloppe pour laisser passer le clic.
- **EQ après la distorsion** : +1 à 2 dB (voire plus) dans le grave, Q à 0.
- **Après Serum** : compression au mixage ; la vidéo teste avec un rumble et deux sidechains (un dur sur le sub, un plus libre plein-bande).
- **Macros** : `Pitch Decay` position du point bas de LFO 2 (vers la droite = plus de punch) · `Cutoff Decay` profondeur de LFO 3 · `Click` profondeur du LFO → DRIVE · `Release` dernier point de LFO 1.
- **Origine** : [SOURCE TE-09 = HC-12 = RA-01, Ozgun, Serum 1] : 909 façon techno mainstage.

### KT02 Kick techno distordu Ozgun — trou pour le clic
- **OSC A** : Analog BD Sine, volume baissé ; LFO 1 → LEVEL : petite attaque, un vide laissé pour le clic, puis fondu ; pas plus court qu'une demi-mesure.
- **Phase** : RANDOM désactivé.
- **Hauteur** : LFO 2 très court → Coarse, unipolaire ; la hauteur de départ se règle par la quantité.
- **Clic** : NOISE Bright White, enveloppe très courte sur son niveau.
- **OSC B** (texture) : tables Digital à essayer (ou Analog), octave +1, RANDOM 0 ; ENV 3 → LEVEL et Coarse de B, unipolaire ; ENV 3 → position de table d'A et de B.
- **Filtre** : sur A seul, un peu d'aigu coupé, un peu de DRIVE pour un punch plus fort.
- **FX** : Distortion, une enveloppe → DRIVE, plusieurs modes à essayer ; Filter optionnel pour adoucir le haut.
- **Après Serum** : la vidéo passe par des plug-ins de FL Studio (Disperser, Overdrive, EQ vers 300 Hz, clip) ; à faire avec des plug-ins tiers.
- **Macros** : `Pitch Decay` profondeur de LFO 2 · `Cutoff Decay` profondeur d'ENV 3 → position · `Click` niveau du NOISE · `Release` dernier point de LFO 1.
- **Origine** : [SOURCE TE-10 = RA-02, Ozgun, Serum 1, kick en F].

### KT03 Rumble warehouse Serum 2 — rééchantillonnage interne
- **Kick** : sinus, RANDOM 0, enveloppe de pitch « bête et méchante » → Coarse, unipolaire, bonne octave ; ENV 3 coupe la grosse queue (sustain baissé, hold).
- **Rééchantillonnage** : l'oscillateur passe en mode Sample, flèche à côté du logo → le son est rééchantillonné dans Serum 2, puis Normalize. Scan modulé pour ajouter du punch (Range « à 800 », puis remis « à 100 »). Une deuxième passe possible.
- **Queue** : FX Convolve, IR d'usine du dossier « Massif » (exemple « All of Monument »), Damp au maximum ; Compressor ; Utility qui resserre la stéréo sans la supprimer.
- **Impression de la queue** : jouer la note une fois, rééchantillonner kick et reverb ensemble, bypass des FX, Normalize ; le sample est « 4 octaves en dessous » : remettre l'octave à 0 ; jouer « un G ».
- **Sidechain interne** : LFO par défaut en mode ENVELOPE, courbe de sidechain avec petit fondu de fin → LEVEL.
- **Longueur** : ENV 3, avec ou sans hold.
- **Variantes** : nouveau Convolve (autre IR, mix à fond) pour un rumble « qui rebondit » ; mode Spectral, Start et modes de warp ; enveloppe rapide « bam bam bam ».
- **FX finaux** : Distortion ; passe-haut pour couper les subs ; Compressor Multiband avec un LFO en ENVELOPE sur le gain d'une bande (pompe) ; petite distorsion finale.
- **Macros** : `Pitch Decay` quantité de l'enveloppe de pitch · `Cutoff Decay` decay d'ENV 3 · `Click` Scan · `Release` profondeur du LFO de sidechain.
- **Origine** : [SOURCE TE-01 = RA-11, Strob Studio, Serum 2, en français].

### KT04 Warehouse bunker Strob — bruit pitché en queue
- **OSC A** : sinus (une frame triangle « in phase » peut être ajoutée pour un fondu sinus ↔ triangle) ; RANDOM off, PHASE 0.
- **Hauteur** : LFO en ENVELOPE, BPM délié → Coarse d'A, unipolaire, plage pas trop étendue (punchy sans trop de clic).
- **Amplitude** : LFO 2 en ENVELOPE, BPM délié → LEVEL d'A.
- **Queue** : NOISE pitché dans les fréquences utiles (bruits conseillés : « Paper Bag », catégorie « Organics », souvent stéréo) ; A et NOISE dans un filtre passe-haut (24 ou 18 dB) qui retire l'extrême grave ; LFO 3 sur le niveau du NOISE, qui laisse la place au punch (« comme un sidechain ») puis monte.
- **DRIVE du filtre** modulé par une forme percussive : monte au début, redescend, remonte pour la queue ; pas à fond.
- **Compressor Multiband** (3 bandes) : LFO 5 (ENVELOPE, transitoire court) → gain de la bande High = clic plus violent ; LFO 6, un peu plus lent → bande Low = impact du grave ; « mat », beaucoup de grave, pas un kick hardcore.
- **Reverb avant le compresseur**, pas trop longue, pas de grande salle ; LFO 7 (1/4 = longueur d'un kick) → MIX : 0 au début, reverb ensuite, pas à 100 %.
- **Harmoniques** : fondu vers le triangle, sur l'attaque ou sur la queue ; warps (Bend) sur l'une ou l'autre.
- **Macros** : macro « HP » de la source sur le CUTOFF → `Cutoff Decay` · `Pitch Decay` quantité du LFO de pitch · `Click` profondeur de LFO 5 · `Release` profondeur de LFO 7.
- **Origine** : [SOURCE TE-02, Strob Studio, Serum 1, en français] : la phase du NOISE change l'articulation du kick ; un ratio trop élevé grésille.

### KT05 Rumble en couches Strob — le même kick trois fois
- **Couche 1** : kick simple dans Serum (enveloppes de pitch et de volume, un filtre, très peu de FX, pas de reverb).
- **Couche « Rumble mids »** : même preset, enveloppe de volume très raccourcie, filtre passe-bande dans les bas-médiums, petit mouvement de CUTOFF ; reverb courte et stéréo ; sidechain.
- **Couche « Rumble low »** : même kick, enveloppe de volume avec fondu, queue abaissée ; extrême grave coupé.
- **Reverb imprimée** : même kick + Reverb Plate de Serum (Size, Low cut, Damp au goût), pour réverbérer aussi le sub.
- **« Rumble hi »** optionnel : à partir du Rumble mids, autre fréquence de filtre, un sinus ajouté plus haut au début.
- **Principe** : même source = même fondamentale ; caler la phase à l'oreille en décalant le clip audio ; n'imprimer que la première partie de la reverb.
- **Placement** : hors grille, décalé à la main, sauf un coup pile au contretemps.
- **Après Serum** : bus en plug-ins tiers (EQ, Trash en parallèle à 50, clipper) ; kick et basse vers −6 LUFS court terme dans la vidéo.
- **Macros** : par couche, `Release` = longueur de l'enveloppe de volume.
- **Origine** : [SOURCE TE-03, Strob Studio, Serum 1, en français].

### KT06 Industriel Teknovault — BN12, all-pass, Sine Shaper
- **OSC A** : table « AT Entity » (mélange sinus et carré) ; LFO 1 (ENVELOPE) → Coarse, unipolaire ; LFO 2, plus « clicky » → Global › Main Tuning ; LFO 3 → LEVEL (LEVEL d'A à 0) ; une octave plus bas ; « à −3 » si le pitch devient « lasery ».
- **FILTER 1** : multifiltre BN12 (passe-bande + encoche), DRIVE à fond, fréquence ouverte ; LFO 4 → CUTOFF (unipolaire, peu).
- **FILTER 2** : all-pass qui « étale » le punch (RES et DRIVE montés, MIX baissé, CUTOFF bas) → Bus 1 seulement.
- **OSC B** : Sample, Factory › Non-tonal › snare, dans les filtres, même LFO que A ; unison un peu ouvert, une octave plus bas.
- **Bus 1** : EQ (petit boost), Sine Shaper (« cheat code » industriel, dose faible) ; deuxième EQ et Sine Shaper très léger ; Utility, LEVEL baissé, LFO 3 → ce LEVEL ; Chorus pour la stéréo.
- **Rumble** : OSC C en Sample « drum kick duda kicks », suivi de hauteur désactivé → Bus 2 : Reverb Hall (RATE et DEPTH à 0, MIX à fond, SIZE réduite, un peu de DECAY), EQ passe-bas, Splitter Mid/Side avec passe-haut sur le Side vers 300 Hz, Soft Saturator poussé, EQ, second Soft Saturator léger, Utility avec forme du rumble en LFO.
- **Main FX** : Hard Clipper léger ; Compressor Multiband (threshold baissé, « below » ouvert) ; EQ avec LFO sur un Low Shelf ; Soft Clipper final ; Reverbs Vintage avec LFO sur le MIX ; Splitter Mid/Side final ; Distortion X-Shaper (Asym) en option.
- **Tempo** : 155 BPM.
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` CUTOFF de l'all-pass · `Click` profondeur de LFO 2 · `Release` forme du rumble.
- **Origine** : [SOURCE TE-04 = RA-03, Teknovault, Serum 2].

### KT07 Rumble en one-shots Teknovault — samples « duda »
- **OSC A** (punch) et **OSC B** (rumble) en mode Sample, one-shots « Factory non-tonal drum kick duda » ; suivi de hauteur désactivé, réglage par les demi-tons ; A → None + Bus 1, B → None + Bus 2.
- **Punch** : LFO 1 (ENVELOPE) → LEVEL d'A ; plusieurs punchs essayés (le n° 6 préféré).
- **Bus 2** : Reverb Hall, DECAY monté, SIZE basse ; EQ coupe-aigus ; Distortion Soft Saturator à 50 % (Tube correct, Diode trop d'aigus) ; EQ ; Soft Clipper ; Utility Bass Mono vers 300 Hz (jusqu'à 190, jamais dans le sub), après la reverb et avant la première distorsion ; LFO 2 en forme de rumble → volume du dernier effet, « retour à 50 % ».
- **Main FX** : Soft Saturator, EQ avant (moins d'aigu et de sub) ; boost modéré de la deuxième fondamentale ; Splitter Low/Mid/High, Reverb Vintage sur les médiums seulement, enveloppe sur le MIX ; Utility Bass Mono vers 130 Hz au moins ; Compressor Multiband à threshold 0 (compression vers le haut seulement : trop de compression vers le bas = kick « gated »).
- **Impression** : rendre le kick plusieurs fois (la reverb change la phase à chaque rendu) et garder le meilleur.
- **Macros** : `Pitch Decay` demi-tons du rumble · `Cutoff Decay` DECAY de la Hall · `Click` profondeur de LFO 1 · `Release` profondeur de LFO 2.
- **Origine** : [SOURCE TE-05, Teknovault, Serum 2].

### KT08 Hard techno Krosper — trois LFO de hauteur, preset gratuit
- **OSC A** (corps) : sinus propre, RANDOM 0 ; LFO 1 et LFO 2 (ENVELOPE) → Coarse, le second unipolaire ; LFO 3 → Global › Main Tuning (transitoire plus net) ; LFO 5 → LEVEL.
- **SUB** : −2 octaves ; LFO 3 aussi → Coarse du SUB ; LFO 4 extrêmement court → LEVEL du SUB (il ne fait que le transitoire) ; seul le SUB passe par FILTER 1, routé en `Direct` (hors effets).
- **FX** :
  1. Filter Phs 12−.
  2. Distortion Hard Clip à fond.
  3. Reverb, LFO 6 → MIX : 0 sur le punch, reverb dans la queue (rumble).
  4. Filter Phs 24+, CUTOFF monté, RES augmentée, MIX ≈ 50 %.
  5. Distortion Diode 1, filtre interne en Pre et passe-haut, DRIVE assez bas, MIX ≈ 50 % ; réglage final : avant le compresseur.
  6. Compressor Multiband : threshold tout en bas, « below » augmenté, mids et highs réduits, low beaucoup plus fort.
  7. Distortion Diode 2.
  8. EQ : léger boost du grave, corps vers 200 Hz.
  9. Soft Clip, gain ≈ 80 %, puis second Soft Clip, gain à fond.
  10. Splitter Mid/Side, EQ du Side sans grave ; Utility Bass Mono.
- **FILTER 2** réglé comme FILTER 1, pour renforcer le transitoire.
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` CUTOFF du Phs 24+ · `Click` profondeur de LFO 4 · `Release` profondeur de LFO 6.
- **Origine** : [SOURCE TE-06 = RA-05, Krosper, Serum 2, preset gratuit en lien].

### KT09 Industriel Krosper — deux Comb et un Sine Shaper
- **OSC A** : position de table 2 (sinus propre), −1 octave, RANDOM 0, LEVEL 0.
- **Hauteur** : LFO 1 (ENVELOPE) → Coarse ; LFO 2 (copie) → Coarse ; LFO 3, variante légère → Coarse, unipolaire (tire seulement vers le bas).
- **Amplitude** : LFO 4 → LEVEL d'A.
- **FX** :
  1. Distortion Tube ≈ 90 %.
  2. Reverb, un peu d'aigus coupés, MIX baissé, LFO → MIX (reverb dans la queue seulement).
  3. Distortion Diode 2, DRIVE ≈ 18 % (grain métallique).
  4. Filter Comb : CUTOFF ≈ 30 %, RES ≈ 85 %, MIX ≈ 50 %.
  5. Filter Reverb : CUTOFF ≈ 28 %, MIX 50 %.
  6. EQ : boost vers 400 Hz, LFO sur le gain.
  7. Distortion Sine Shaper ≈ 50 %, le même LFO sur son MIX.
  8. Utility, Bass Mono à 200 Hz.
  9. Filter Comb : CUTOFF ≈ 16 %, RES ≈ 50 %, MIX ≈ 40 %.
  10. Distortion Hard Clip ≈ 60 %.
  11. EQ : légère coupe des aigus, gain modulé par le même LFO.
  12. Compressor, gain poussé.
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` CUTOFF du premier Comb · `Click` DRIVE de la Diode 2 · `Release` profondeur de LFO 4.
- **Origine** : [SOURCE TE-07, Krosper, Serum 2 déduit du vocabulaire ; la fin de la vidéo est une promotion à ignorer].

### KT10 Industriel en samples 909 — Sample Agency
- **OSC A** : mode Sample, Factory › non-tonal › kick 909.
- **OSC B** : copie, octave +1 ; **OSC C** : un autre sample 909.
- **NOISE** : allumé, pour le punch du transitoire.
- **FX** :
  1. Distortion Overdrive.
  2. Distortion Diode 2, ENV 2 → DRY (accent du transitoire) ; ratio de compression augmenté.
  3. Une troisième distorsion possible.
  4. EQ : couper les zones « muddy » selon le morceau ; le kick doit avoir plus de grave que le reste.
  5. Delay en mode Normal, temps court 1/16 (ou canaux déliés 1/8 et 1/16), **avant** la Reverb.
  6. Reverb Hall, SIZE et DECAY courts.
  7. Un filtre « créatif » au choix pour finir.
- **Tempo** : 155 BPM ; 1/16 = 96,8 ms [CALCUL].
- **Macros** : `Pitch Decay` — · `Cutoff Decay` CUTOFF du filtre final · `Click` profondeur d'ENV 2 · `Release` MIX du Delay.
- **Origine** : [SOURCE TE-08 = RA-04, Sample Agency, Serum 2] : départ d'échantillons d'usine, pas un sinus pur.

### KT11 Hard techno en 4 minutes — PowercutSamples
- **OSC A** : sinus de base, RANDOM baissé ; une noire jouée en G (« entre F et A » pour la techno).
- **Amplitude** : ENV 1 : hold « ≈ 100-170 ms » (transcription ambiguë), decay ≈ 80 ms, sustain −∞, courbe du decay aplatie (queue serrée).
- **Hauteur** : ENV 2 : attaque 0, decay ≈ 60 ms, sustain 0 → Coarse, unipolaire.
- **Impression** : rééchantillonner → « kick brut style 909 ».
- **Après Serum** (plug-ins tiers à la place des natifs de la vidéo) : saturation à courbe dure, DRIVE ≈ −3 dB ; compresseur : seuil −10 dB, attaque 10 ms, release 30 ms ; EQ : coupe sous 30 Hz, léger creux vers 120 Hz ; limiteur ; puis nouvelle impression.
- **Tempo** : 140 BPM ; hold + decay ≈ 180-250 ms, sous la croche (214 ms) au bas de la fourchette [CALCUL].
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` — · `Click` quantité d'ENV 2 → Coarse · `Release` hold d'ENV 1.
- **Origine** : [SOURCE TE-11, PowercutSamples, Serum 1].

### KT12 Techno OddWave — le bruit d'attaque comme couleur
- **Note** : C3 de base (ajustée ensuite par octaves ou enveloppe).
- **OSC A** : sinusoïde, RANDOM retiré.
- **Hauteur** : LFO en ENVELOPE, synchronisé au BPM → Coarse ; matrice en bipolaire ; grand sweep du haut jusqu'à la note.
- **NOISE** : « couleur principale du timbre » ; sample d'attaque de kick, One Shot, suivi de clavier désactivé.
- **Amplitude** : LFO 2 en ENVELOPE, BPM, 1/8 (ou 1/4) pour laisser de l'espace à la basse.
- **FX** : Compressor Multiband (threshold un peu baissé, ratio à fond, attaque 0) ; LFO 3 en ENVELOPE, BPM désactivé → gain de la bande haute (contrôle de l'attaque).
- **Filtre** : sur le corps, le NOISE par-dessus ; CUTOFF vers 800-900 Hz.
- **Distorsion** : au choix ; la vidéo prend Decapitator (plug-in tiers).
- **Macros** : `Pitch Decay` profondeur du LFO de pitch · `Cutoff Decay` CUTOFF · `Click` profondeur de LFO 3 · `Release` RATE de LFO 2.
- **Origine** : [SOURCE TE-12 = RA-13, OddWave Studio, Serum 1, en français].

### KT13 Warehouse Lachie — LFO dessiné, filtre avant la saturation
- **OSC A** : sinus de base, région « octave −1 » ; polyphonie réduite (pas de clics), RANDOM off.
- **Amplitude** : enveloppe étirée, mais pas jusqu'au kick suivant.
- **Hauteur** : un LFO dessiné (attaque initiale, puis descente lente jusqu'à juste avant la fin) glissé sur deux cibles dans la matrice, unipolaires ; une seconde zone en courbe raide. Courbe arrondie = une membrane qui vibre ; angles vifs = petits artefacts exploitables.
- **Après Serum** : compression rapide (attaque et release rapides) ; saturation (Saturn dans la vidéo), avec le filtre placé **avant** le saturateur.
- **Macros** : `Pitch Decay` profondeur du LFO · `Cutoff Decay` CUTOFF avant saturation · `Click` — · `Release` decay de l'enveloppe.
- **Origine** : [SOURCE TE-13 = RA-10, Lachie, Serum 1, transcription très partielle].

### KT14 Hard techno AKA Sounds — transitoire « laser »
- **OSC A** : −2 octaves, onde « analog » pure.
- **Hauteur** : ENV 2 → pitch global, decay très serré ≈ 50 ms, sustain 0.
- **Texture** : WARP Asymmetric ou FM (B) ; LFO 1 → position de table, modulé fort.
- **Filtre** : passe-bas, DRIVE et FAT au maximum (sub poussé en saturation, transitoire et queue soudés).
- **FX** : Distortion Tube 100 % wet ; un peu d'Hyper (largeur des aigus) ; Compressor Multiband « to the absolute limit ».
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` profondeur de LFO 1 · `Click` quantité de warp · `Release` decay d'ENV 1.
- **Test** : longs passages sans parole dans la vidéo ; les valeurs sont à lire à l'écran.
- **Origine** : [SOURCE TE-14 = RA-09, AKA Sounds, Serum 2, preset gratuit].

### KT15 Hyper techno baltic audio — les valeurs de la description
- **OSC A** : Analog_BD_Sin, −2 octaves ; **OSC B** : « Dist Fwapper SQ », −2 octaves, LEVEL 0.
- **LFO 1** (ENVELOPE) : attaque courte puis pente raide vers le centre de la grille → LEVEL d'A, plage maximale.
- **LFO 2** (ENVELOPE) : départ juste sous la ligne haute, fin en bas au centre, poignée de courbe sur la dernière ligne basse → pitch d'A, « environ 36 ».
- **LFO 3** (ENVELOPE) : du haut à gauche vers le bas à droite, poignée presque en bas → LEVEL de B (60 → 0), position des deux tables (50 → 0), niveau du NOISE (100 %) ; NOISE = sample d'attaque de kick, One Shot.
- **FX** : Distortion en mode Pre, curseur sur H (passe-haut), F = 82, Q = 1,4, DRIVE ≈ 65 ; LFO 4 (même courbe que LFO 3, poignée deux lignes plus haut) → DRIVE de 100 % à 65 % ; EQ : bande basse 90 Hz, Q 0, +8,5 dB ; un peu d'aigus.
- **Macros** : `Pitch Decay` profondeur de LFO 2 · `Cutoff Decay` F du pré-filtre · `Click` profondeur de LFO 3 → NOISE · `Release` profondeur de LFO 1.
- **Origine** : [SOURCE TE-15, baltic audio, Serum 1] : vidéo sans voix, valeurs écrites dans la description, non minutées.

### KT16 Reverse bass rave — punch imprimé et crunch en contretemps
- **Punch** : sinus, RANDOM 0, enveloppe très courte vers le bas → Coarse ; ENV 3 semblable sur la même destination ; impression audio ; raccourcir le rendu en warp « Auto » (kick plus « thumpy ») ; s'il est trop aigu, rejouer une autre note que F et réimprimer.
- **Crunch** (reverse bass) : second Serum ; RANDOM 0 ; table « B Square » ; octave −2 ; notes en F ou G, motif en contretemps ; enveloppe d'amplitude « wampy », avec une petite introduction vers le punch ; LFO 1 (ENVELOPE) → CUTOFF d'un German LP (plage graves → médiums) et → LEVEL ; sidechain du crunch par le kick.
- **Longueur** : le kick dure environ une noire.
- **Après Serum** (plug-ins tiers) : transient shaper, Inflator ou wave shaper sinus, soft clip, EQ avant la distorsion ; bande d'EQ en cloche dans les médiums qui s'ouvre pendant le crunch.
- **Macros** : par Serum ; `Cutoff Decay` profondeur de LFO 1 sur le German LP.
- **Jeu** : bloc « Hard techno 150 — kick et reverse bass en contretemps » ci-dessous.
- **Origine** : [SOURCE RA-06, Teknovault, Serum 1] : « pas trop sinon territoire hardstyle ».

### KT17 Hardtekk Krosper — trois sinus, deux bus
- **SUB** : −1 octave ; LFO 1 (ENVELOPE) → Coarse (mouvement de début), LFO 2 → LEVEL (longueur) : corps distordu et crunch.
- **OSC A** : RANDOM 0, −1 octave, position de table 2 (sinus) ; LFO 3 → Coarse (punch) ; LFO 4 court → LEVEL (punch seulement).
- **Global** : LFO 5 → Main Tuning, ≈ 20-30 %.
- **OSC B** : −1 octave, position 2 ; LFO 6 → Coarse, LFO 7 → LEVEL ; WARP Tube ≈ 60-70 %.
- **FILTER 1** : OSC A seul, High 12 (CUTOFF, RES, DRIVE : rôle majeur sur le ton du punch) → Bus 1 : EQ, boost très étroit ≈ 780 Hz, +24 dB, Q ≈ 53 % ; Tube 100 % ; Hard Clip 100 % ; EQ vers 30 Hz ; Utility dont le gain suit LFO 4.
- **FILTER 2** : le SUB → Bus 2 : Tube 100 % ; EQ coupe-aigus.
- **Main** : Compressor Multiband, threshold baissé, gain monté, « below » et lows poussés jusqu'à ce que les couches se soudent.
- **Impression** : rendu audio, puis seulement un transient shaper.
- **Ton** : CUTOFF de FILTER 1 et fréquence du premier EQ du Bus 1 (plus profond, plus pointu, plus métallique).
- **Macros** : `Pitch Decay` profondeur de LFO 3 · `Cutoff Decay` CUTOFF du High 12 · `Click` fréquence du boost de 780 Hz · `Release` profondeur de LFO 2.
- **Origine** : [SOURCE RA-07, Krosper, Serum 2, preset gratuit] : proche du hard dance, à garder en tête.

### KT18 Kick gaté Krosper — reverb gatée, EQ « hollow »
- **OSC A** : Default Shapes, −2 octaves, RANDOM 0, position 2, LEVEL 0 ; tous les LFO en ENVELOPE ; LFO 1 → LEVEL : supprime le transitoire initial, ne laisse que la queue.
- **NOISE** : preset « ARP Circuit » ; LFO 2 → LEVEL, forme courte et pointue = punch.
- **Hauteur** : LFO 3 → Coarse d'A, très subtil (descend puis remonte légèrement : un petit « bounce »).
- **Filtre** : sur A et NOISE, Phs 24−, RES montée, CUTOFF un peu bougé, DRIVE, variation montée.
- **FX** :
  1. Hyper/Dimension, RATE au minimum (corps, pas de mouvement).
  2. Reverb, grave retiré, DECAY presque au minimum ; un LFO → MIX sur toute la plage = effet « gated ».
  3. EQ : creux très étroit ≈ 240 Hz, Q ≈ 47, −24 dB ; bande très étroite ≈ 1 100 Hz, +24 dB → forme « hollow ».
  4. Distortion symétrique, DRIVE au maximum.
  5. Compressor Multiband, gain monté, below et low poussés.
  6. Utility, Bass Mono ≈ 200 Hz.
- **Macros** : `Pitch Decay` profondeur de LFO 3 · `Cutoff Decay` CUTOFF du Phs 24− · `Click` profondeur de LFO 2 · `Release` profondeur du LFO sur le MIX de la reverb.
- **Origine** : [SOURCE RA-08, Krosper, Serum 2] : changer le NOISE fait basculer vers le hardstyle.

### KT19 Tekno Fuzzey — le Rate fait le transitoire
- **OSC A** : Analog BD Sin.
- **Hauteur** : LFO → CRS ; déplacer et baisser le point central pour la chute ; BPM et Anchor décochés, mode ENVELOPE ; le RATE du LFO règle le transitoire.
- **Voicing** : MONO ; notes de même longueur qui se suivent.
- **Amplitude** : ENV 1 : attaque ≈ 0,5 ms (à 0 ms, on entend un clic), release très faible, sustain 0 ; longueur au decay. Kick « tribe » = decay à fond.
- **Note** : C2 si le kick est trop aigu.
- **EQ** (après la seconde distorsion, plug-ins de Logic dans la vidéo) : bosse large ≈ 45 Hz, petit creux ≈ 580 Hz, grand shelf aigu.
- **Variantes** : points ajoutés dans le LFO pour des formes de pitch « farfelues » (kicks tekno anciens) ; pitch baissé + Overdrive = « presque un kick techno ».
- **Néo-rave** : kick sec (très peu de decay) et reverse bass sur une piste dupliquée, décalée en contretemps, avec un RATE plus bas et moins d'attaque, compressée en sidechain par le kick.
- **Rumble** : la vidéo le fait par une reverb sidechainée en bus dans Logic ; dans Serum, l'équivalent est la reverb à MIX modulé de KT04 [DÉDUCTION].
- **Macros** : `Pitch Decay` RATE du LFO · `Cutoff Decay` — · `Click` attaque d'ENV 1 · `Release` decay d'ENV 1.
- **Origine** : [SOURCE RA-12, Fuzzey, Serum 1, en français, 45 min] ; les passages gabber, frenchcore et trap ne sont pas repris.

### KT20 Industriel Teknovault en deux couches — scies, Flanger, reverb inversée
- **Punch clicky** : sinus, enveloppe de pitch dessinée, RANDOM 0 → impression, Normalize, raccourci ; réimprimer à une autre note que F ; baisser le pitch du rendu en warp « Auto » pour un kick plus « thumpy ».
- **Raw punch** : deux scies (A et B, l'une « down », l'autre « up ») ; LFO 1 (ENVELOPE) = punch → LEVEL ; LFO 2 = crunch ; Distortion Diode 2 ; WARP FM (B) sur A ; filtre High 24 avec RES et DRIVE, A seul dedans ; un Flanger dans la section filtre, avant la distorsion ; WARP Bend− = crunch ; LFO 3 → CUTOFF ; LFO 4 = enveloppe de pitch.
- **Reverb inversée** (forme dessinée) avant la distorsion, impression : « very heavy punch » ; reverb « Hollow Room » pour une queue.
- **Bus final** : Serum en effet, Distortion Sine Shaper ≈ 28 % (« hollow » le kick), EQ avant.
- **Après Serum** (plug-ins tiers) : Inflator, soft clipper, EQ, transient shaper ; bande médium automatisée qui s'ouvre au punch ; un top kick techno par-dessus, sinon trop « hardstyle ».
- **Macros** : macro « cutoff punch » de la source → `Cutoff Decay` · `Pitch Decay` profondeur de LFO 4 · `Click` niveau du crunch · `Release` MIX de la reverb.
- **Origine** : [SOURCE RA-14, Teknovault, Serum 1] ; le rumble vient d'un plug-in maison, non construit dans la vidéo.

## Motifs vérifiés

Numérotation de Live (C3 = 60) ; les notes de kick sont les fondamentales visées. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/kicks/kicks-techno-rave.md`.

```grille
titre: Techno 130 — kick en G0 et rumble entre les coups (KT03, KT05, KT07)
tempo: 130
accords: Gm | Gm
kick: G0[1:1] G0[2:1] G0[3:1] G0[4:1] | G0[1:1] G0[2:1] G0[3:1] G0[4:1]
rumble: G0[1e:3] G0[2e:3] G0[3e:3] G0[4e:3] | G0[1e:3] G0[2e:3] G0[3e:3] G0[4e:3]
```

Le kick tient le grave en G0 (49,0 Hz) ; le rumble (queue de reverb imprimée ou sidechainée) remplit les trois doubles croches entre deux kicks et s'éteint avant le suivant.

```grille
titre: Hard techno 150 — kick et reverse bass en contretemps (KT16)
tempo: 150
accords: Gm | Gm
kick: G0[1:1] G0[2:1] G0[3:1] G0[4:1] | G0[1:1] G0[2:1] G0[3:1] G0[4:1]
crunch: G1[1&:2] G1[2&:2] G1[3&:2] G1[4&:2] | G1[1&:2] G1[2&:2] Bb1[3&:2] G1[4&:2]
```

Le crunch du reverse bass répond sur chaque contretemps (200 ms à 150 BPM), sidechainé par le kick.

```grille
titre: Techno 130 — rumble coupé avant la frontière (KT03, KT05)
tempo: 130
accords: Gm | Gm
kick: G0[1:1] G0[2:1] G0[3:1] G0[4:1] | G0[1:1] G0[2:1] G0[3:1] G0[4:1]
rumble: G0[1e:3] G0[2e:3] G0[3e:3] G0[4e:3] | G0[1e:3] G0[2e:3]
```

Mesures 7 et 8 : le kick continue seul sur la seconde moitié de la mesure 8 ; le rumble revient avec le drop.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : les tables « AT Entity », « Dist Fwapper SQ », « B Square », les samples d'usine « duda » et 909, les IR du dossier « Massif », le bruit « ARP Circuit », l'Utility interne et son Bass Mono.
- Lire à l'écran les formes de LFO et les quantités des fiches TE et RA.
- Écouter avec le reste du morceau, en mono, à niveau égal ; mesurer kick et basse sur des exports séparés ; inscrire le kick validé au registre `../signature.md`.
