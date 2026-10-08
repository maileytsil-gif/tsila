# Vingt recettes de screech pour la House (famille F12)

Neuvième et dernier lot de recettes House : le screech, un cri résonant dans le haut-médium. En Bass House, il sert d'accent, de réponse ou de fin de phrase, pas de basse principale. Le genre vient du dubstep, d'où sont tirées les deux études du registre. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` (F12-01 Rocket Powered Sound, F12-02 EDMProd, et pour les gestes métalliques F11-01, F11-02, F13-02) ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` (F08-04) ;
- la fiche 10 de `../families.md`, `../documentation-basses.md` § 1-2 (FM, formants) et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL]. Peu de sources sont étudiées pour cette famille : la part de [ORIGINAL] et de [DÉDUCTION] est plus grande qu'ailleurs, et chaque fiche le dit.

## Règles communes aux vingt recettes

1. **Accent, pas fondation.** Le screech vit entre 1 et 5 kHz. Equalizer : passe-haut entre 150 et 300 Hz.
   - Le grave reste au sub de `house-f01-sub.md`, ou à la basse principale du drop (F05, F07, F08).
   - Le screech se place en fin de phrase ou en réponse (fiche 10 de `../families.md`).
2. **Résonance limitée, crêtes tenues** : distorsion après le filtre, puis EQ sur les crêtes. Contrôler le haut-médium (1-5 kHz) à **faible volume** (fiche 10).
3. **Glide sur cette couche seulement.** Le sub ne glisse pas avec le screech.
4. **Rapports FM** [CALCUL, `../documentation-basses.md` § 1] :
   - +19 demi-tons ≈ 3:1 ;
   - +31 ≈ 6:1 ;
   - +43 ≈ 12:1.

   En tempérament égal, chacun tombe 1,96 cent sous le rapport entier : un spectre presque harmonique, à peine battant.
5. **Quatre macros communes**, celles de la fiche 10 de `../families.md` :
   - `Scream` : fréquence du filtre ou quantité de FM ;
   - `Rasp` : drive ;
   - `Fall` : glide ou chute de hauteur ;
   - `Space` : delay court.

   Vérifier le « + » sur chaque destination.
6. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
7. **Contrôle par l'utilisateur** :
   - le screech seul à faible volume, puis dans le drop ;
   - aucune crête ne doit percer à 2-4 kHz quand on monte le volume ;
   - mono ;
   - la note la plus aiguë (le repliement des FM fortes s'y entend d'abord, `../documentation-basses.md` § 4) ;
   - les deux bornes de `Scream` et `Rasp` ;
   - A/B à niveau égal contre C01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| C01 | Screech de référence | Bass House, accent | passe-bande balayé, distorsion après |
| C02 | Astuce des 43 demi-tons | Bass House, dubstep | FM 12:1, High 24 résonant |
| C03 | Screech FM Virtual Riot | accent, lead | scies unison 16, FM à +3 octaves |
| C04 | Scream BP | Bass House | filtre Scream BP, drive > 50 % |
| C05 | French LP | Bass House | passe-bas distordant, BOEUF |
| C06 | Screech « ee » | Bass House | formant balayé vers « ee » |
| C07 | Screech au peigne et au delay court | Bass House métallique | Combs + delay de 13 ms |
| C08 | Screech parlant | Bass House | Bandreject balayé |
| C09 | Screech sync | Bass House, Electro House | sync balayé |
| C10 | Screech qui tombe | fin de phrase | chute de hauteur |
| C11 | Échelle de quintes FM | toutes | +19, +31, +43 |
| C12 | Screech sans fondamentale | accent aigu | Odd/Even à 100 % |
| C13 | Screech replié | Bass House | Sine Fold, Rectify |
| C14 | Screech au phaser figé | Bass House | phaser immobile en haut |
| C15 | Screech en rafale | Bass House | enveloppe courte, rythme MIDI |
| C16 | Screech décalé | accent | Bode, décalage de fréquence |
| C17 | Accent de fin de phrase | Bass House | LFO Envelope montant |
| C18 | Screech au bruit | Bass House | FM (Noise) |
| C19 | Screech spectral | Bass House | moteur Spectral |
| C20 | Screech traité en post | toutes | compression parallèle, creux 100-300 Hz |

## Les vingt recettes

### C01 Screech de référence
- **Patch** :
  - OSC A en scie, OCT 0, RAND 0. OSC B en sinus, OCT +1, LEVEL 0 ; WARP 1 d'OSC A en FM (B), 5-10 % (FM légère, facultative).
  - FILTER 1 en Band 12, CUTOFF 1-2 kHz, RES 25-35 %.
  - ENV 2 → CUTOFF +1 octave, decay 200 ms ; LFO 1 (1/8, RETRIG) → CUTOFF ±½ octave.
  - VOICING MONO + LEGATO, PORTA 40-80 ms.
- **ENV 1** : attaque 2 ms, decay 100-400 ms, sustain −10 dB, release 60 ms.
- **FX** :
  1. Distortion Overdrive après le filtre, DRIVE 30-50.
  2. Equalizer : passe-haut à 200 Hz, creux étroit sur la crête la plus forte entre 2 et 4 kHz.
  3. Delay court (1/16, MIX 10-15 %).
- **Macros** : `Scream` CUTOFF 800 Hz → 4 kHz · `Rasp` DRIVE 0 → 70 · `Fall` PORTA 0 → 150 ms · `Space` MIX du Delay 0 → 30 %.
- **Sub associé** : aucun ; c'est une couche d'accent.
- **Jeu** : bloc « Bass House 128 — screech de fin de phrase » ci-dessous.
- **Origine** : toutes les fourchettes de la fiche 10 de `../families.md` [ORIGINAL, reprises].

### C02 Astuce des 43 demi-tons — FM 12:1
- **Patch** :
  - OSC A sur une table riche : la source utilise « Groan II », une table de Massive importée (lien dans la description de la vidéo) ; à défaut, une table Digital. OCT −1 en House (registre grave en Fa0 dans la source).
  - ENV 1 avec un peu d'attaque contre le clic (écran : 6,1 ms / 0 / 1,00 s / 0 dB / 15 ms).
  - LFO 1 en mode Envelope, 1/2 pointée, montée rapide courbée puis lente descente (« pseudo-sidechain »), → WT POS d'A, quantité réduite.
  - VOICING MONO.
  - OSC B : copie de A (même table, position un peu différente, même modulation), LEVEL 0, monté de 3 octaves et 7 demi-tons (OCT +3, SEM +7, soit 43). RAND 0 sur A et B.
  - WARP 1 d'OSC A en FM (B), au milieu ; LFO 1 → ce warp (écran : 26).
  - FILTER 1 en High 24 sur A seul, DRIVE, CUTOFF bas, FAT monté, résonance en pic dans le bas-médium, LFO 1 → CUTOFF, sans key track.
- **FX, dans l'ordre vu à l'écran** :
  1. Hyper/Dimension : 3 voix, DETUNE bas, MIX bas.
  2. Equalizer, grave remonté.
  3. Chorus en mode HPF, MIX et DEPTH bas.
  4. Distortion SoftClip, bon drive : distordre après l'élargissement donne du croquant sur les côtés.
  5. Compressor Multiband, bandes moins écrasées.
  6. Reverb Plate, peu de MIX, LO CUT, taille et pré-délai bas.
- **Retour de la source** : WT POS baissée (moins agressive), plus de filtre.
- **Macros** : `Scream` WARP 1 (FM) · `Rasp` DRIVE de la SoftClip · `Fall` PORTA · `Space` MIX de la Reverb.
- **Sub associé** : S01. La source garde un sub sinus hors filtre, phase alignée, niveau suivant LFO 1 ; ici il est sur sa piste.
- **Calcul** : 43 demi-tons = 2^(43/12) = 11,99, presque 12:1, à −1,96 cent. La source dit que « la quinte ajoute un intérêt harmonique dans le médium » [CALCUL].
- **Origine** : [SOURCE F12-02, transcription et trois captures, Serum 1, EDMProd (Aden), dubstep].

### C03 Screech FM Virtual Riot — lead d'accent
- **Patch** :
  - OSC A en scie (Basic Shapes, scie descendante), OCT 0, Unison 16, detune modulé. WARP en FM (from B).
  - OSC B sur Default (scie), OCT +3, Unison 16 : le modulateur.
  - FILTER 1 en MG Low 12 (visible, réglage non suivi).
  - LFO 1 en Trig, 1/8, montée raide puis descente linéaire, sur OSC B (cible exacte non visible).
  - LFO 2 → warp FM d'A : 69 à l'écran. L'auteur corrige à 2:49 : c'est bien LFO 2.
- **ENV 1** : 0,5 ms / 0 / 1,00 s / 0 dB / 15 ms (Init).
- **FX** : Distortion Diode 1, filtre OFF ; drive et mix non lisibles. Passe-haut à 300 Hz ajouté, à cause des 16 voix [ORIGINAL].
- **Macros** : `Scream` LFO 2 → FM · `Rasp` DRIVE de la Diode 1 · `Fall` PORTA · `Space` MIX d'un Delay.
- **Sub associé** : aucun.
- **Limite** : la description de la vidéo dit que c'est un lead, pas une basse (« bass » dans le titre pour la recherche). À utiliser en accent ou en réponse aiguë.
- **Origine** : [SOURCE F12-01, sept captures sans transcription, Serum 1].

### C04 Scream BP — le filtre qui crie
- **Patch** :
  - OSC A en scie, OCT 0, RAND 0.
  - FILTER 1 en Scream BP, DRIVE 55-80 % (au-dessus de 50 % pour l'entendre), CUTOFF 1-2 kHz, RES 20-30 %.
  - VAR (SCREAM, coupure de la boucle de feedback) modulé par ENV 2 : +30 %, decay 150 ms.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −10 dB, release 60 ms.
- **FX** : Equalizer : passe-haut à 200 Hz, creux sur la crête. Compressor Single 3:1.
- **Macros** : `Scream` VAR (SCREAM) · `Rasp` DRIVE du filtre 50 → 90 % · `Fall` PORTA · `Space` MIX d'un Delay.
- **Sub associé** : aucun.
- **Origine** :
  - Scream LP/BP : fort feedback, qualité de « cri », « DRIVE au-dessus de 50 % pour l'entendre », VAR = SCREAM [cartographie, § 6] ;
  - valeurs [ORIGINAL].

### C05 French LP — passe-bas distordant
- **Patch** :
  - OSC A en scie, OCT 0.
  - FILTER 1 en French LP, CUTOFF 1,5-3 kHz, RES 30 %, VAR (BOEUF, seconde résonance) 30-60 %.
  - ENV 2 → CUTOFF +1 octave, decay 250 ms.
  - LFO 1 (1/4, RETRIG) → VAR.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 60 ms.
- **FX** : passe-haut à 150 Hz, Compressor Multiband à gain modéré.
- **Macros** : `Scream` VAR (BOEUF) · `Rasp` DRIVE du filtre · `Fall` PORTA · `Space` —.
- **Sub associé** : S01, si le screech descend sous 200 Hz.
- **Origine** :
  - French LP : passe-bas distordant, non linéaire ; BOEUF, seconde résonance, se combine avec RES [cartographie, § 6] ;
  - valeurs [ORIGINAL].

### C06 Screech « ee » — formant balayé
- **Patch** :
  - OSC A en scie, OCT 0.
  - FILTER 1 en Formant-III, RES 25-35 %.
  - ENV 2 → CUTOFF : départ sur « oo », arrivée sur « ee », decay 120-200 ms. Le F2 passe de 870 à 2 300 Hz.
  - LFO 1 (1/8) faible → CUTOFF.
- **ENV 1** : attaque 2 ms, decay 250 ms, sustain −10 dB, release 60 ms.
- **FX** : Distortion Overdrive, puis Equalizer (passe-haut à 200 Hz, creux sur le pic nasal).
- **Macros** : `Scream` ENV 2 → CUTOFF · `Rasp` DRIVE · `Fall` PORTA · `Space` MIX d'un Delay.
- **Sub associé** : aucun.
- **Origine** :
  - formants « oo » F2 870 Hz et « ee » F2 2 300 Hz, F3 3 000 Hz [SOURCE Synth Secrets 23, `../documentation-basses.md` § 2] ;
  - le glissement du F2 de « oo » vers « ee » décrit un « yoi » [DÉDUCTION du même §] ;
  - réglages [ORIGINAL].

### C07 Screech au peigne et au delay court
- **Patch** :
  - OSC A sur une table spectrale (la source utilise « Creeper [SN] »), OSC B en carrée à faible niveau, NOISE (≈ 72) : des sources qui se heurtent.
  - FILTER 1 en Combs sur A et B : CUTOFF ≈ 425 Hz, RES ≈ 98, DRIVE au fond, DAMP monté pour corriger le timbre.
- **ENV 1** : attaque 0,5 ms, decay 116 ms, sustain −∞, release 52 ms (écran).
- **FX** :
  1. Distortion Tube, MIX 50 %.
  2. Filter Combs, RES haute.
  3. Phaser : RATE 0, DEPTH 0, FREQ 0, un peu de FEEDBACK (« effet guitare »).
  4. Hyper/Dimension, UNISON 4.
  5. Compressor Multiband.
  6. Delay : LINK, BPM désactivé, ≈ 12,87 / 12,79 ms, MIX monté (teinte métallique).
  7. Passe-haut à 200 Hz ajouté.
- **Calcul** : un delay de 12,87 ms réinjecté agit comme un peigne de pics espacés de 77,7 Hz [CALCUL : 1 / 0,01287 s]. Changer le temps déplace la couleur.
- **Macros** : `Scream` RES du Combs · `Rasp` DRIVE · `Fall` — · `Space` temps du Delay 8 → 20 ms.
- **Sub associé** : aucun.
- **Origine** : [SOURCE F11-01, transcription et deux captures, Serum 1, « machine gun »] ; usage en screech [ORIGINAL].

### C08 Screech parlant — Bandreject balayé
- **Patch** :
  - OSC A sur une table métallique (la source utilise « Phase Werb [SL] », lecture incertaine), Unison 4, DETUNE très bas, RAND 0.
  - FILTER 1 en Flanger − (Flg L6− ou H6−), RES 50, key track, CUTOFF ≈ 649 Hz (valeur tapée par la source), MIX ≈ 50 %.
  - LFO 1 (1/4, Trig) → MIX du flanger jusqu'à 100 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** :
  1. Hyper (34), Dimension (SIZE 1-3 %).
  2. Compressor Multiband.
  3. Equalizer : bande haute en passe-bas, Q ≈ 39, fréquence ≈ 222 Hz modulée vers le haut (un passe-bas fait avec l'EQ).
  4. Filter Bandreject : CUTOFF ≈ 93 Hz modulé +30, largeur ≈ 80 modulée vers ≈ 76, RES : effet de voix « qui parle ».
- **Registre** : la source joue un growl métallique grave. En screech, monter de deux octaves et remonter les fréquences de l'EQ et du Bandreject d'autant (×4) [ORIGINAL].
- **Macros** : `Scream` CUTOFF du Bandreject · `Rasp` MIX du flanger · `Fall` — · `Space` —.
- **Sub associé** : S01 si la ligne reste grave.
- **Origine** : [SOURCE F11-02, transcription et deux captures, Serum 1, « Kung Fu » de PhaseOne et Virtual Riot] ; transposition [ORIGINAL].

### C09 Screech sync — balayage de harmoniques
- **Patch** :
  - OSC A en scie, OCT 0, RAND 0.
  - WARP 1 en Sync. ENV 2 → warp : de +80 % à 0 en 300 ms. LFO 1 (1/8, RETRIG) → warp ±15 %.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 70 %.
  - VOICING MONO + LEGATO, PORTA 60 ms.
- **ENV 1** : attaque 2 ms, decay 400 ms, sustain −6 dB, release 60 ms.
- **FX** : Distortion Overdrive, passe-haut à 200 Hz, Delay 1/8 pointée à MIX 15 %.
- **Macros** : `Scream` quantité de Sync · `Rasp` DRIVE · `Fall` PORTA · `Space` MIX du Delay.
- **Sub associé** : aucun.
- **Origine** : Sync, « les harmoniques montent, la note reste » [cartographie, § 4.1] ; geste [ORIGINAL].

### C10 Screech qui tombe — la chute de fin de phrase
- **Patch** :
  - C01, plus ENV 3 → CRS d'OSC A : de 0 à −12 demi-tons, attaque 150-300 ms (la chute part en fin de note), sustain 0.
  - Variante : PORTA 150-250 ms en ALWAYS vers une note plus grave.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 200 ms.
- **Macros** : `Fall` quantité d'ENV 3 → CRS, 0 → −24 · les autres comme C01.
- **Sub associé** : aucun ; le sub ne tombe pas.
- **Jeu** : bloc « Bass House 126 — screech qui tombe » ci-dessous, en dernière mesure de phrase.
- **Test** : la chute doit finir avant le temps 1 de la phrase suivante.
- **Origine** :
  - « Accent en fin de phrase ; glide uniquement sur cette couche » ; macro `Fall` [`../families.md`, fiche 10] ;
  - mise en œuvre [ORIGINAL].

### C11 Échelle de quintes FM — +19, +31, +43
- **Patch** :
  - OSC A en sinus ou scie, OCT 0, RAND 0. OSC B en sinus, LEVEL 0.
  - WARP 1 d'OSC A en FM (B), 20-35 %, ENV 2 → warp +30 %, decay 250 ms.
  - Trois presets à comparer pour OSC B : +19 demi-tons (OCT +1, SEM +7), +31 (OCT +2, SEM +7), +43 (OCT +3, SEM +7).
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 60 ms.
- **FX** : Distortion légère, passe-haut à 200 Hz.
- **Macros** : `Scream` WARP 1 · `Rasp` DRIVE · `Fall` PORTA · `Space` —.
- **Sub associé** : aucun.
- **Test** : à quantité de FM égale, comparer les trois rapports. Plus le rapport est grand, plus les bandes latérales s'écartent de la porteuse, vers l'aigu.
- **Origine** :
  - +43 [SOURCE F12-02] ; +31 (« 2 octaves et 7 demi-tons ») [SOURCE F05-12] ;
  - rapports 3, 6 et 12 à −1,96 cent [CALCUL, règle 4] ;
  - comparaison [ORIGINAL].

### C12 Screech sans fondamentale — Odd/Even à 100 %
- **Patch** :
  - OSC A en scie, OCT 0, RAND 0.
  - WARP 1 en Odd/Even, à 100 % : les harmoniques paires seulement, sans la fondamentale. Le son paraît une octave plus haut.
  - FILTER 1 en Band 12, CUTOFF 2 kHz, RES 30 %.
  - LFO 1 (1/8, RETRIG) → CUTOFF.
- **ENV 1** : attaque 2 ms, decay 250 ms, sustain −12 dB, release 50 ms.
- **FX** : passe-haut à 300 Hz, Distortion Soft Clip légère.
- **Macros** : `Scream` Odd/Even 50 → 100 % · `Rasp` DRIVE · `Fall` PORTA · `Space` MIX d'un Delay.
- **Sub associé** : aucun.
- **Origine** :
  - Odd/Even, « 100 % = paires seules (effet d'octave, la fondamentale manque) » [cartographie, § 4.1] ;
  - usage en screech [DÉDUCTION, jamais essayée].

### C13 Screech replié — Sine Fold et Rectify
- **Patch** :
  - OSC A en sinus, OCT 0, RAND 0.
  - WARP 1 en Sine Fold (repli sinusoïdal), base 20 %. ENV 2 → warp +50 %, decay 200 ms. WARP 2 en Rectify, 20-40 %.
  - FILTER 1 en MG Low 24, CUTOFF 4-6 kHz : il tient les aigus du repli.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 60 ms.
- **FX** : Equalizer : passe-haut à 200 Hz, creux sur la crête. Activer QUALITY sur High ou Ultra contre le repliement.
- **Macros** : `Scream` ENV 2 → Sine Fold · `Rasp` Rectify · `Fall` PORTA · `Space` —.
- **Sub associé** : aucun.
- **Origine** :
  - modes Sine Fold et Rectify des warps de distorsion [cartographie, § 4.2] ;
  - Rectify au maximum sur le warp de B [SOURCE F08-03] ;
  - suréchantillonnage QUALITY [cartographie, § 9] ;
  - repliement [`../documentation-basses.md` § 4] ;
  - recette [ORIGINAL].

### C14 Screech au phaser figé haut
- **Patch** :
  - C01 sans le LFO sur le filtre.
  - Deux Phaser figés : RATE au minimum, DEPTH 0, 4 pôles, FREQ 2 kHz pour le premier et 3,2 kHz pour le second, FEEDBACK 50-70 %.
  - LFO 2 (1/4) → FREQ du premier phaser ±½ octave.
- **ENV 1** : comme C01.
- **FX** : comme C01, phasers après la distorsion.
- **Macros** : `Scream` FREQ du premier phaser · `Rasp` DRIVE · `Fall` PORTA · `Space` FEEDBACK des phasers.
- **Sub associé** : aucun.
- **Origine** :
  - phasers figés, seules fréquence et feedback, 4 pôles [SOURCE F08-01, à 205 Hz pour un growl] ;
  - distorsion avant phaser [SOURCE F08-04] ;
  - fréquences hautes [ORIGINAL].

### C15 Screech en rafale — l'enveloppe fait le rythme
- **Patch** :
  - C07 ou C01, avec ENV 1 courte : attaque 0,5 ms, hold 0, decay 116 ms, sustain −∞, release 52 ms.
  - Le rythme se dessine avec les notes MIDI, pas avec un LFO.
- **FX** : comme la recette de départ.
- **Macros** : `Scream`, `Rasp`, `Space` comme la recette de départ · `Fall` decay d'ENV 1 60 → 200 ms.
- **Sub associé** : aucun.
- **Jeu** : doubles croches en rafale sur la dernière mesure d'une phrase ; vélocités dégressives.
- **Origine** :
  - « le machine gun vient de l'ENV 1, pas d'un LFO » ; valeurs à l'écran [SOURCE F11-01] ;
  - usage en screech [ORIGINAL].

### C16 Screech décalé — Bode
- **Patch** :
  - C01, plus un module Bode (frequency shifter) dans les FX : SHIFT +10 à +60 Hz, MIX 30-50 %.
  - LFO 2 (1/2, RETRIG) → SHIFT.
- **ENV 1** : comme C01.
- **FX** : Bode après la distorsion, puis passe-haut à 200 Hz.
- **Macros** : `Scream` SHIFT · `Rasp` DRIVE · `Fall` PORTA · `Space` FEED du Bode (delays « pitchés »).
- **Sub associé** : aucun.
- **Test** : un décalage de fréquence fixe rend chaque note inharmonique d'une manière différente. Vérifier les notes extrêmes contre l'accord.
- **Origine** :
  - module Bode : SHIFT, FEED, delays réinjectés dans le shifter [cartographie, § 8] ;
  - Bode à faible MIX pour la stéréo [SOURCE F13-02] ;
  - décalage vers l'inharmonique [DÉDUCTION].

### C17 Accent de fin de phrase — montée par LFO Envelope
- **Patch** :
  - C01, plus LFO 3 en mode ENVELOPE, RATE 1 mesure, forme montante (de 0 à 1 sur la mesure), → CUTOFF (+1 octave) et → DRIVE (+30).
  - Une note tenue d'une mesure monte d'elle-même jusqu'à la frontière.
- **ENV 1** : attaque 5 ms, sustain 100 %, release 100 ms.
- **Macros** : `Scream` LFO 3 → CUTOFF · `Rasp` LFO 3 → DRIVE · `Fall` PORTA · `Space` MIX d'un Delay.
- **Sub associé** : aucun.
- **Jeu** : une seule note tenue en mesure 8. C'est l'une des variations avant la frontière de huit mesures (règle des drops d'`AGENTS.md`) ; alterner avec C10.
- **Origine** :
  - mode ENVELOPE (un cycle par note) [cartographie, § 7.2] ;
  - accent en fin de phrase [`../families.md`, fiche 10] ;
  - geste [ORIGINAL].

### C18 Screech au bruit — FM (Noise)
- **Patch** :
  - OSC A en scie, OCT 0, RAND 0.
  - NOISE en White, LEVEL 0 (source seulement). WARP 1 d'OSC A en FM (Noise), 5-15 %.
  - FILTER 1 en Band 12, CUTOFF 1,5 kHz, RES 30 %, LFO 1 (1/8) → CUTOFF.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −10 dB, release 60 ms.
- **FX** : Distortion Soft Clip, passe-haut à 200 Hz, Equalizer −3 dB vers 6-8 kHz.
- **Macros** : `Scream` CUTOFF · `Rasp` FM (Noise) 0 → 25 % · `Fall` PORTA · `Space` —.
- **Sub associé** : aucun.
- **Origine** :
  - « la FM depuis le noise ajoute du “fizz” pour growl et neuro » [SOURCE F03-04] ;
  - FM du noise « pour des aigus craquants » [SOURCE F07-02] ;
  - recette [ORIGINAL].

### C19 Screech spectral
- **Patch** :
  - OSC A en moteur Spectral, sur une table ou un sample riche.
  - Couper les partiels graves (volet FREQ LO) et garder la bande 1-5 kHz.
  - Un warp spectral de décalage ou d'étalement (libellé à lire dans l'interface) modulé par LFO 1 (1/4).
  - QUALITY sur High pendant la conception.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 60 ms.
- **FX** : Distortion Overdrive légère, passe-haut à 300 Hz.
- **Macros** : `Scream` quantité du warp spectral · `Rasp` DRIVE · `Fall` PORTA · `Space` —.
- **Sub associé** : aucun.
- **Origine** :
  - moteur Spectral et ses warps (`kSpread`, `kSpectralShift`…), libellés affichés non documentés ; volet FREQ LO / HI et Post Warp [cartographie, § 3.6, 4.3] ;
  - couper des partiels et les faire glisser [SOURCE F08-04, section spectrale] ;
  - recette [DÉDUCTION].

### C20 Screech traité en post — compression parallèle et creux
- **Patch** : C01 ou C02, imprimé ou non. Après Serum, avec des plug-ins tiers :
  - Compresseur 4:1, attaque et release rapides, makeup, en **parallèle** ;
  - EQ : creux large entre 100 et 300 Hz (place au kick et à la snare), +2 dB vers 9 kHz, coupe-bas raide ;
  - sidechain rapide sur le kick **et** la snare.
- **Macros** : celles de la recette de départ.
- **Sub associé** : celui de la basse principale du drop.
- **Test** : A/B avec et sans le traitement à niveau égal. Le screech doit rester lisible sans masquer la snare.
- **Origine** :
  - post-traitement optionnel de la source : Compressor 4:1 rapide en parallèle, EQ creux 100-300 Hz, boost vers 9 kHz, shelf grave raide, sidechain kick + snare rapide [SOURCE F12-02] ;
  - la source utilise les effets natifs de Live : ici des plug-ins tiers (règle 6 d'`ableton-live-session`) ; chaînes de bus dans `../../../../../ingenieur-mixage/modules/effets-plugins/GUIDE.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60). Kick supposé sur les quatre temps (doubles croches 1, 5, 9, 13). Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f12-screech.md`.

```grille
titre: Bass House 128 — screech de fin de phrase (C01, C15)
tempo: 128
accords: Em7 | Em7
screech: E3[4&:2] | E3[1e:1] G3[1&:1] E3[2&:2] D3[3e:1] B2[3&:3] E3[4&:2]
```

À placer en mesures 7-8 d'une phrase : le screech entre sur la fin de la mesure 7 et répond dans la mesure 8.

```grille
titre: Bass House 126 — growl et screech en réponse (C04, C06)
tempo: 126
accords: Fm7 | Fm7
growl: F1[1&:2] Ab1[2&:1] F1[2a:1] | Eb1[1&:2] F1[2&:2]
screech: C3[3&:1] Eb3[3a:1] F3[4&:2] | Ab3[3&:2] G3[4&:1] F3[4a:1]
```

Le growl (F08) tient la première moitié de chaque mesure, le screech la seconde : ils ne parlent jamais en même temps. Le sol du screech est une note de passage vers le fa.

```grille
titre: Bass House 126 — screech qui tombe (C10)
tempo: 126
accords: Gm7 | Gm7
fall: G3[1&:3] F3[2a:1] D3[3&:3] C3[4a:1] | Bb2[1&:6] G2[3&:6]
```

Avec PORTA en ALWAYS, chaque note glisse vers la suivante ; la chute d'ENV 3 de C10 s'ajoute sur la dernière tenue (G2). Le do de la mesure 1 est une note de passage vers le si bémol.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « Groan II » (Massive), « Creeper [SN] » et « Phase Werb [SL] » ;
  - les filtres Scream BP, French LP, Formant-III, Flanger −, Bandreject ;
  - le module Bode et les warps spectraux.

  Vérifier les destinations des macros.
- Ce lot repose sur peu de sources étudiées. Les vidéos screech du registre (F12-03, F12-04, F12-05) restent à regarder sur le Mac pour confirmer ou corriger.
- Écouter chaque recette à faible volume puis dans le drop, et en garder deux ou trois pour les accents. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
