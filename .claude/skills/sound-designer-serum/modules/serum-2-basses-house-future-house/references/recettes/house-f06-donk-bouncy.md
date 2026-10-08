# Vingt recettes de donk et de basse bouncy pour la House (famille F06)

Cinquième lot de recettes House : le donk, une basse brève qui « toque », métallique ou élastique, et ses cousines bouncy (slap house, jump-up ramené au tempo House). Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` (F06-01, F06-02) et `../etudes-pages-house.md` (F03-04, Monosounds) ;
- la recette du corpus `../../../../../producteur-live/modules/house-future-rave-bass-house-production/recipes/basse-fm-metallique-bass-house.md`, désignée par « recette Jauz » ;
- la fiche 9 de `../families.md`, la recette 4 « Metallic donk » de `../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/references/cinquante-cinq-recettes.md` ;
- `../documentation-basses.md` § 1 (FM) et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes aux vingt recettes

1. **Le knock ne touche jamais le sub.** L'excursion de hauteur, la FM brève et la distorsion restent dans la couche donk.
   - Le sub (S11 ou S01 de `house-f01-sub.md`) ne suit que les fondamentales, sans excursion (fiche 9 de `../families.md`).
   - Le sub est souvent facultatif : « le donk se suffit souvent au-dessus d'un kick long » (`../motifs.md`).
   - Equalizer du donk : passe-haut entre 90 et 180 Hz (Slynk coupe à 170-180 Hz pour laisser la place au sub).
2. **Court** : ENV 1 sustain 0, decay 130-300 ms ; la longueur des notes MIDI compte peu.
3. **Rapports FM** [CALCUL, `../documentation-basses.md` § 1] : composantes à fc ± n·fm.
   - Rapport entier : son harmonique.
   - 1:8 (modulateur trois octaves au-dessus) : composantes 1, 7, 9, 15, 17… × fc, un spectre creux et clairsemé.
   - 1:1,5 : composantes 0,5, 1, 2, 2,5… × fc, une série de fc/2, donc une note perçue une octave plus bas.
   - 1:1,41 : composantes 0,41, 1, 1,82, 2,41… × fc, un spectre inharmonique, métallique.
4. **Phase** : RAND 0 et PHASE fixe sur porteuse et modulateur, pour que chaque knock soit identique.
5. **Quatre macros communes**, celles de la fiche 9 de `../families.md`, avec `Tone` en plus :
   - `Knock` : quantité d'excursion de hauteur ou d'attaque ;
   - `Metal` : quantité de FM, de rapport ou de résonance ;
   - `Body` : decay d'ENV 1 ;
   - `Tone` : coupure du filtre.

   Vérifier le « + » sur chaque destination.
6. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
7. **Contrôle par l'utilisateur** :
   - le donk seul, puis avec le kick : le knock ne doit pas doubler l'attaque du kick ;
   - avec le sub s'il y en a un ;
   - mono ;
   - les deux notes extrêmes du riff (l'index FM change de caractère avec la hauteur, d'après la recette Jauz) ;
   - les deux bornes de `Knock` et `Metal` ;
   - A/B à niveau égal contre D01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| D01 | Donk de référence | Bass House | hauteur +12/+24 brève, FM 2:1 brève |
| D02 | Donk Slynk | Bass House façon Jauz, Habstrakt | FM 1:8, ENV 1 sur la FM et le filtre |
| D03 | Donk Slynk plus « donk » | Bass House | attaque 0, octave plus basse, table modulée |
| D04 | Donk au peigne | Bass House | filtre Combs, transitoire de bruit |
| D05 | Jauz métallique | Bass House, Future House | FM 2:1 à −30 cents, thwack |
| D06 | Donk inharmonique | ponctuation Bass House | rapport 1,41, passe-bande |
| D07 | Thwack pur | Bass House, G-House | triangle, chute de hauteur de 50 ms |
| D08 | Donk à transitoire de bruit | Bass House | NOISE en one-shot |
| D09 | Bouncy slap house | Slap House, Future House | chute de hauteur et octaves |
| D10 | Jump-up ramené à 128 | Bass House | Squibble, Flg L6+, LFO sur les niveaux |
| D11 | Donk à vélocité | Bass House | vélocité vers le knock et la FM |
| D12 | Donk « boing » en octaves | Bass House, Future House | portamento court proportionnel |
| D13 | Donk PD | Deep Bass House | distorsion de phase, plus douce |
| D14 | Donk Odd/Even | Bass House | octave d'attaque sans changer la hauteur |
| D15 | Donk sync | Bass House | balayage du warp Sync |
| D16 | Donk vocal | Bass House | formant bref |
| D17 | Tom bass | Bass House, Tech House | percussion échantillonnée accordée sur un sinus |
| D18 | Donk ring mod | Bass House métallique | warp RM bref |
| D19 | Donk large au-dessus de 300 Hz | Bass House | Hyper sur les aigus seulement |
| D20 | Donk imprimé et rejoué | toutes | resampling et Simpler |

## Les vingt recettes

### D01 Donk de référence
- **Patch** :
  - OSC A en sinus ou triangle (Basic Shapes), la fondamentale. Note jouée dans le registre médium (F1-F2, 87-175 Hz). RAND 0, PHASE 0 %.
  - OSC B en sinus, rapport 2:1 (Ratio 2.000, SRC = A, ou OCT +1), LEVEL 0, `None`.
  - WARP 1 d'OSC A en FM (B), base 10 %.
  - ENV 2 → CRS d'OSC A : +12 à +24 demi-tons au pic, attaque 0, decay 20-60 ms, sustain 0.
  - ENV 3 → WARP 1 : +30 à +60 %, attaque 0, decay 40-130 ms, sustain 0.
- **ENV 1** : attaque 0,5 ms, decay 130-300 ms, sustain 0, release 30 ms.
- **FX** : Distortion Soft Sat. légère, puis Equalizer en passe-haut à 120 Hz.
- **Macros** : `Knock` ENV 2 → CRS 0 → +24 st · `Metal` ENV 3 → WARP 1 0 → 70 % · `Body` decay d'ENV 1 80 → 400 ms · `Tone` — (pas de filtre).
- **Sub associé** : aucun, ou S11 sur les seules fondamentales.
- **Jeu** : motif « Bass House 128 — donk syncopé » de `../motifs.md`, ou bloc D01 ci-dessous.
- **Origine** : toutes les fourchettes de la fiche 9 de `../families.md` [ORIGINAL, reprises] ; rapport 2:1 [CALCUL].

### D02 Donk Slynk — façon Jauz, Habstrakt, Joyryde
- **Patch** :
  - OSC B en sinus (Basic Shapes), OCT −2 : la porteuse.
  - OSC A en sinus, OCT +1, LEVEL 0 : le modulateur, trois octaves au-dessus de B, soit un rapport 1:8.
  - WARP de B en FM (from A). Dans Serum 2, l'étiquette est FM (A).
  - ENV 1 sur l'amplitude et, « pas trop haut », sur la quantité de FM.
  - FILTER 1 sur A, B et noise, en MG Low 24 (MG Low 12 puis Low 24 à l'écran), RES 0, un peu de DRIVE ; ENV 1 → CUTOFF aussi.
  - Unison 2 sur A et B, detune à l'oreille.
- **ENV 1 (écran, à confirmer)** : attaque ≈ 71 ms, hold 0, decay ≈ 319 ms, sustain −∞, release ≈ 424 ms. L'attaque de 71 ms surprend pour un donk : D03 la met à 0.
- **FX** :
  1. Equalizer en coupe-bas vers 170-180 Hz.
  2. Distortion avec son filtre en passe-haut vers 200 Hz (n'abîme que médiums et aigus), forme non lue, MIX un peu baissé.
  3. Reverb, LO CUT monté, HI CUT ouvert.
  4. Compressor Multiband, bande haute descendue, gain monté. Attaque et release basses donnent un effet « buzzy », il revient à plus propre.
- **Macros** : `Knock` ENV 1 → FM 0 → 50 % · `Metal` quantité de FM de base 0 → 40 % · `Body` decay d'ENV 1 150 → 500 ms · `Tone` CUTOFF 20 → 70 %.
- **Sub associé** : S01. Le tutoriel met un sub à −2 octaves en Direct Out dans le patch ; ici il est sur sa piste.
- **Origine** :
  - [SOURCE F06-02, transcription et trois captures, Serum 1] ;
  - spectre du rapport 1:8 [CALCUL].

### D03 Donk Slynk plus « donk »
- **Patch** : D02, avec quatre changements.
  - Attaque d'ENV 1 à 0.
  - B une octave plus bas (OCT −3), à condition que le passe-haut garde la place du sub.
  - OSC A sur la table SawRoundedToSquare (table de Serum 1, à retrouver), avec ENV 2 → WT POS, decay 80 ms.
  - LEVEL d'A remonté en partie : le modulateur devient aussi audible.
- **ENV 1** : attaque 0, decay ≈ 250 ms, sustain −∞, release 60 ms.
- **Macros** : `Knock` ENV 2 → WT POS 0 → 100 % · `Metal` LEVEL d'A 0 → 40 % · `Body` decay 100 → 400 ms · `Tone` CUTOFF.
- **Sub associé** : S11.
- **Origine** : variantes dites à 7:21 : SawRoundedToSquare avec position modulée par enveloppe, attaque à 0, octaves plus basses, niveau de A remis en partie [SOURCE F06-02] ; valeurs [ORIGINAL].

### D04 Donk au peigne — filtre Combs
- **Patch** :
  - D02 ou D01, avec FILTER 1 en Combs (ou Comb 2 de Serum 2), key track allumé, CUTOFF à la hauteur de la note, VAR (DAMP) 30-50 %.
  - NOISE en White, ENV 4 → LEVEL du NOISE : decay 5-15 ms : une transitoire d'attaque.
- **ENV 1** : attaque 0, decay 200 ms, sustain 0, release 40 ms.
- **FX** : Distortion légère, passe-haut à 150 Hz.
- **Macros** : `Knock` ENV 4 → NOISE 0 → 100 % · `Metal` RES 0 → 70 % · `Body` decay 100 → 400 ms · `Tone` VAR (DAMP).
- **Sub associé** : S11.
- **Test** : avec le key track, chaque note doit garder la même couleur. Sans lui, certaines notes résonnent plus que d'autres.
- **Origine** :
  - « Comb, son préféré, surtout avec attaque », et « noise court en transitoire d'attaque » [SOURCE F06-02, 10:00] ;
  - Combs (VAR = DAMP) et Comb 2 [cartographie, § 6] ;
  - valeurs [ORIGINAL].

### D05 Jauz métallique — FM 2:1 désaccordée
- **Patch** :
  - OSC A en sinus, OCT −1 (couche médium, au lieu du −2 de la recette Jauz qui descend dans le sub).
  - OSC B en sinus, Ratio 2.000 (SRC = A), FIN −30 cents, LEVEL 0.
  - WARP 1 d'OSC A en FM (B), base 45 %. ENV 2 → WARP 1 +60 %, decay 150-300 ms, sustain 0.
  - WARP 2 d'OSC A en Diode 1 pour plus de métal.
  - ENV 3 → CRS d'OSC A, +12 → 0 en 50 ms : le « thwack ».
  - FILTER 1 en MG Low 24, CUTOFF ≈ 25 %, RES 0, ENV 2 → CUTOFF +100 %.
  - VOICING MONO + LEGATO, PORTA 40-80 ms.
- **ENV 1** : sustain bas, release ≈ 33 % de la course, « plucky ».
- **FX** : Distortion Tube légère, puis Compressor Multiband MIX 15-25 %, puis Equalizer (coupe-bas à 100 Hz, −3 dB vers 200-300 Hz), puis Hyper/Dimension discret.
- **Macros** : `Knock` ENV 3 → CRS 0 → +12 · `Metal` FIN de B 0 → −40 cents · `Body` decay d'ENV 1 · `Tone` CUTOFF 15 → 50 %.
- **Sub associé** : S01, sous 100-120 Hz.
- **Origine** :
  - [SOURCE recette Jauz : Garage Bass d'Attack Magazine, `[DOC-2]` thwack, `[HEUR]` Diode] ;
  - « chercher le métal dans un ratio non entier alors que l'original est entier + désaccord de 30 cents » est l'erreur que cette recette signale.

### D06 Donk inharmonique — ponctuation
- **Patch** :
  - OSC A en sinus ou triangle, RAND 0.
  - OSC B en sinus, Ratio 1.41 (SRC = A), LEVEL 0.
  - WARP 1 d'OSC A en FM (B) : base 0, ENV 2 → warp +50 à +80 %, decay 60-120 ms, sustain 0.
  - FILTER 1 en Band 12, CUTOFF 600 Hz-1,5 kHz, RES 20 %.
- **ENV 1** : attaque 0, decay 150 ms, sustain 0, release 30 ms.
- **FX** : Reverb Plate courte (MIX ≤ 10 %, LO CUT haut), passe-haut à 180 Hz.
- **Macros** : `Knock` ENV 2 → warp 0 → 80 % · `Metal` Ratio de B, 1,41 / 1,7 / 2,0 (trois presets) · `Body` decay 80 → 300 ms · `Tone` CUTOFF du passe-bande.
- **Sub associé** : aucun : c'est une ponctuation, hors du sub.
- **Test** : les notes inharmoniques n'ont pas de hauteur nette. Vérifier qu'elles ne contredisent pas l'accord du morceau.
- **Origine** :
  - « Metallic donk : A sinus/triangle, B rapport non entier ~1,4-1,7, FM brève, F bandpass ; ponctuation hors sub » [SOURCE recette 4 de `cinquante-cinq-recettes.md`] ;
  - pourquoi 1,41 plutôt que 1,5 [CALCUL, règle 3].

### D07 Thwack pur — sans FM
- **Patch** :
  - OSC A en triangle, OCT −1, RAND 0, PHASE 0 %.
  - ENV 2 → CRS d'OSC A : +12 au pic, attaque 0, decay 50 ms, sustain 0.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 45 %, ENV 2 → CUTOFF +30 %.
- **ENV 1** : attaque 0, decay 200 ms, sustain 0, release 30 ms.
- **FX** : Distortion Tube DRIVE 20, puis passe-haut à 100 Hz.
- **Macros** : `Knock` ENV 2 → CRS 0 → +24 · `Metal` DRIVE 0 → 50 · `Body` decay 80 → 350 ms · `Tone` CUTOFF 20 → 70 %.
- **Sub associé** : S11.
- **Origine** : « Thwack : env. de pitch +12 st → 0 en 50 ms » [SOURCE recette Jauz, `[DOC-2]`] ; patch [ORIGINAL].

### D08 Donk à transitoire de bruit
- **Patch** :
  - D01 sans l'excursion de hauteur (`Knock` à 0).
  - NOISE en one-shot sur une attaque courte du dossier `Attacks_Misc` (choix de l'utilisateur), PITCH avec Key track, routé `Main`. Ou White avec ENV 4 → LEVEL, decay 8 ms.
- **ENV 1** : attaque 0, decay 200 ms, sustain 0, release 30 ms.
- **Macros** : `Knock` LEVEL du NOISE 0 → 100 % · `Metal` ENV 3 → WARP 1 · `Body` decay · `Tone` PITCH du NOISE.
- **Sub associé** : S11.
- **Test** : le bruit ne doit pas se confondre avec le hat ou le clap.
- **Origine** :
  - « noise court en transitoire d'attaque » [SOURCE F06-02] ;
  - dossiers de NOISE et One Shot [cartographie, § 3.7] ;
  - valeurs [ORIGINAL].

### D09 Bouncy slap house
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0. OSC B en carrée, même octave, LEVEL 50 %.
  - FILTER 1 sur A et B, MG Low 24, CUTOFF ≈ 30 %, RES 15 %. ENV 2 → CUTOFF +50 %, decay 120 ms, sustain 0.
  - ENV 3 → CRS de A et B : −5 à −12 demi-tons au pic, attaque 0, decay 60-90 ms. La note part plus bas et remonte : c'est le rebond.
- **ENV 1** : attaque 0, decay 250 ms, sustain −14 dB, release 50 ms.
- **FX** : Distortion Soft Clip, Compressor Multiband à gain modéré, passe-haut à 100 Hz.
- **Macros** : `Knock` ENV 3 → CRS 0 → −12 · `Metal` LEVEL d'OSC B 0 → 80 % · `Body` decay 120 → 400 ms · `Tone` CUTOFF 20 → 60 %.
- **Sub associé** : S10, un creux par noire.
- **Jeu** : octaves alternées en doubles croches (bloc « Future House 126 — bouncy en octaves » ci-dessous).
- **Origine** : [ORIGINAL]. La page Baltic Audio sur la slap house (F06-06) n'a pas été lue.

### D10 Jump-up ramené à 128 — Bass House
- **Patch** :
  - OSC A sur la table Serum 2 « Squibble » (Digital), OCT −1 (−2 dans la source, à 174 BPM), RAND 0, PHASE ≈ 180° (écran ; la voix dit 101).
  - OSC B en scie (Default Shapes), LEVEL 0 : la source de FM.
  - WARP 2 d'OSC A en FM (B), 21-22 % (dit 21, écran 22).
  - OSC C sur la table « Harmonic Subtle » (Digital, Serum 1), RAND 0, WT POS 256.
  - LFO 1 en Retrig, forme montée-descente, 1/8 → LEVEL d'A (vers le bas) et de C.
  - NOISE en White, STEREO 100 ; LFO 2 en 1/8 → LEVEL du NOISE.
  - VOICING MONO.
  - FILTER 1 en Flg L6+, RES ≈ 59 %, CUTOFF final 893 Hz, autres boutons « vers midi » sauf le DRIVE, MIX un peu baissé. Key track essayé puis retiré.
- **FX** : Distortion Tube, filtre OFF, puis Compressor Multiband (−18,1 dB, 4:1, attaque 90,1, release ≈ 90,1, gain 10,7 dB, bandes à 120 et 2 500 Hz), puis passe-haut à 120 Hz.
- **Tempo** : un 1/8 dure 172,4 ms à 174 BPM, mais 234,4 ms à 128 BPM. Pour garder le même débit de rebonds, passer les LFO en 1/16 (117,2 ms à 128 BPM), ou les garder en 1/8 pour un rebond plus lent [CALCUL, `../tempo-mix.md`].
- **Macros** : `Knock` LFO 1 → LEVEL 0 → 100 % · `Metal` WARP 2 10 → 40 % · `Body` decay d'ENV 1 · `Tone` CUTOFF du Flg 500 Hz → 2 kHz.
- **Sub associé** : S11. Le tutoriel garde un sub à −2 octaves ; ici il est sur sa piste.
- **Origine** :
  - [SOURCE F06-01, transcription et cinq captures, Serum 2, DnB à 174 BPM ; petits chiffres lus avec réserve] ;
  - transposition au tempo House [ORIGINAL]. La version DnB fera partie du lot DnB.

### D11 Donk à vélocité
- **Patch** : D01, plus deux lignes de matrice :
  - Velocity → quantité d'ENV 2 → CRS, si la destination l'accepte ; sinon Velocity → CRS d'OSC A, +6 st au maximum ;
  - Velocity → WARP 1, +30 %.
- **ENV 1** : comme D01.
- **Macros** : celles de D01.
- **Sub associé** : S19, sensible à la vélocité.
- **Jeu** : accents à 120-127 avec knock plein, notes fantômes à 50-70 presque sans knock.
- **Origine** : la vélocité est sans effet tant qu'elle n'a pas de destination [SOURCE F15-01] ; geste [ORIGINAL].

### D12 Donk « boing » en octaves
- **Patch** : D01, avec VOICING MONO + LEGATO, PORTA 30-60 ms, ALWAYS et SCALED allumés, CURVE convexe.
- **ENV 1** : attaque 0, decay 220 ms, sustain −18 dB, release 40 ms. Le sustain n'est pas nul, pour que le glissé s'entende.
- **Macros** : `Knock` ENV 2 → CRS · `Metal` ENV 3 → WARP 1 · `Body` PORTA 0 → 80 ms · `Tone` —.
- **Sub associé** : S11, sans glissé (le sub ne suit que les fondamentales).
- **Jeu** : sauts d'octave en doubles croches (bloc « Future House 126 — bouncy en octaves » ci-dessous).
- **Origine** : PORTA, ALWAYS, SCALED, CURVE [cartographie, § 9] ; geste [ORIGINAL].

### D13 Donk PD — plus doux
- **Patch** :
  - OSC A en sinus, RAND 0.
  - WARP 1 en PD (Self). ENV 2 → warp +40 à +70 %, attaque 0, decay 50-100 ms, sustain 0.
  - ENV 3 → CRS +7 à +12, decay 30 ms.
- **ENV 1** : attaque 0, decay 220 ms, sustain 0, release 40 ms.
- **FX** : Distortion Tape Sat., passe-haut à 100 Hz.
- **Macros** : `Knock` ENV 3 → CRS · `Metal` ENV 2 → PD · `Body` decay · `Tone` —.
- **Sub associé** : S03.
- **Origine** : « PD est plus doux (“CZ-style”) » [SOURCE F03-04] ; PD (Self) [cartographie, § 4.2] ; valeurs [ORIGINAL].

### D14 Donk Odd/Even — octave d'attaque sans changer la hauteur
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - WARP 1 en Odd/Even, base 50 %. ENV 2 → warp +50 % (vers 100 %, paires seules), attaque 0, decay 30-60 ms, sustain 0.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 40 %.
- **ENV 1** : attaque 0, decay 200 ms, sustain 0, release 30 ms.
- **FX** : passe-haut à 100 Hz.
- **Macros** : `Knock` ENV 2 → Odd/Even 0 → +50 % · `Metal` base d'Odd/Even 20 → 50 % · `Body` decay · `Tone` CUTOFF.
- **Sub associé** : S11.
- **Origine** :
  - Odd/Even : « 100 % = paires seules (effet d'octave, la fondamentale manque) » [cartographie, § 4.1] ;
  - l'attaque paraît une octave plus haute puis revient, sans changer la note [DÉDUCTION, jamais essayée].

### D15 Donk sync — « dwoink »
- **Patch** :
  - OSC A en scie ou sinus, OCT −1, RAND 0.
  - WARP 1 en Sync, base 0. ENV 2 → warp +40 à +80 %, attaque 0, decay 40-90 ms, sustain 0 : les harmoniques descendent, la note reste.
  - VAR (WARP Var) vers le soft sync, si le knock est trop dur.
- **ENV 1** : attaque 0, decay 220 ms, sustain 0, release 40 ms.
- **FX** : Distortion Tube légère, passe-haut à 100 Hz.
- **Macros** : `Knock` ENV 2 → Sync 0 → 80 % · `Metal` VAR 0 → 100 % · `Body` decay · `Tone` —.
- **Sub associé** : S11.
- **Origine** : Sync, « les harmoniques montent, la note reste », WARP Var [cartographie, § 4.1] ; geste [ORIGINAL].

### D16 Donk vocal — formant bref
- **Patch** :
  - D01 sans FM, avec FILTER 1 en Formant-I.
  - ENV 2 → CUTOFF (morphe entre formants), attaque 0, decay 60-120 ms : un « dunk » de voyelle.
  - RES 25 %.
- **ENV 1** : attaque 0, decay 200 ms, sustain 0, release 40 ms.
- **FX** : Equalizer : creux sur un pic nasal s'il apparaît, passe-haut à 120 Hz.
- **Macros** : `Knock` ENV 2 → CUTOFF · `Metal` RES · `Body` decay · `Tone` VAR (FORMNT).
- **Sub associé** : S11.
- **Origine** : Formant-I/II/III, CUTOFF qui morphe [cartographie, § 6] ; geste [ORIGINAL].

### D17 Tom bass — percussion accordée sur un sinus
- **Patch** :
  - OSC A en sinus, OCT −1 : le corps.
  - OSC B en moteur Sample, avec un tom ou une percussion courte choisie par l'utilisateur, pitch tracking **allumé** (la percussion suit la note), LEVEL 40-70 %.
  - ENV 2 → CRS d'OSC A +12, decay 40 ms.
- **ENV 1** : attaque 0, decay 250 ms, sustain 0, release 40 ms.
- **FX** : Compressor Single 4:1, attaque 5 ms, passe-haut à 100 Hz.
- **Macros** : `Knock` LEVEL d'OSC B 0 → 80 % · `Metal` ENV 2 → CRS 0 → +12 · `Body` decay · `Tone` —.
- **Sub associé** : S11.
- **Test** : la percussion accordée doit rester juste sur les notes extrêmes ; si elle sonne faux, couper le pitch tracking.
- **Origine** :
  - moteur Sample et pitch tracking [cartographie, § 3.1, 3.3] ;
  - les « toms de rave » sont signalés non chiffrés dans `../../../../../producteur-live/modules/house-future-rave-bass-house-production/references/sound-design-genres.md` ;
  - recette [ORIGINAL]. Aucun sample n'est fourni ni supposé.

### D18 Donk ring mod — métallique « radio »
- **Patch** :
  - OSC A en sinus, RAND 0.
  - OSC B en sinus, Ratio 1.5 à 2.5, LEVEL 0.
  - WARP 1 d'OSC A en RM (B). ENV 2 → warp +60 %, decay 50-100 ms, sustain 0.
  - Base du warp à 0 : le son est pur entre deux knocks.
- **ENV 1** : attaque 0, decay 180 ms, sustain 0, release 30 ms.
- **FX** : passe-haut à 150 Hz, Reverb Plate très courte.
- **Macros** : `Knock` ENV 2 → RM 0 → 80 % · `Metal` Ratio de B (presets) · `Body` decay · `Tone` —.
- **Sub associé** : aucun ou S11.
- **Origine** : « RM donne un son creux, inharmonique, “radio” » [SOURCE F03-04] ; warp RM [cartographie, § 4.2] ; geste [ORIGINAL].

### D19 Donk large au-dessus de 300 Hz
- **Patch** : D02 ou D05, avec la largeur gardée hors du grave.
  - Rack FX : Splitter L/H, SPLIT FREQ 300 Hz.
  - LOWS : rien.
  - HIGHS : Hyper/Dimension (UNISON 3, DETUNE 20 %, MIX 25 %) ou Chorus en mode HPF.
  - Unison d'OSC A à 1 : la largeur vient seulement de l'effet.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Metal` MIX de l'Hyper 0 → 40 %, les autres comme la recette de départ.
- **Sub associé** : S01.
- **Test** : en mono, le knock ne doit pas perdre son attaque.
- **Origine** :
  - Slynk élargit par unison 2 sur A et B [SOURCE F06-02] ;
  - Chorus en mode passe-haut [SOURCE F08-01, F12-02] ;
  - Splitter [cartographie, § 8] ; choix [ORIGINAL].

### D20 Donk imprimé et rejoué
- **Patch** :
  1. Imprimer en audio une note de chaque hauteur utile, ou une boucle de D01-D19 (procédure de `../../../resampling/GUIDE.md`, piste source gardée et désactivée).
  2. Rejouer les prises dans Simpler (instrument natif, toléré par la règle 5 d'`AGENTS.md`) : Slicing pour une boucle, Classic pour une note.
  3. Varier par l'enveloppe de Simpler, le transpose et le reverse.
- **Macros** : celles de Simpler, configurées dans Live.
- **Sub associé** : celui de la recette d'origine.
- **Test** : A/B entre la prise et le patch d'origine à niveau égal. Le transpose de Simpler change aussi la longueur et l'attaque : vérifier les notes extrêmes.
- **Origine** : resampling, piste source gardée [skill `resampling`] ; Simpler toléré [`AGENTS.md`, règle 5] ; usage [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Kick supposé sur les quatre temps (doubles croches 1, 5, 9, 13). Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f06-donk-bouncy.md`. Le bloc « Bass House 128 — donk syncopé » de `../motifs.md` complète ces trois motifs.

```grille
titre: Bass House 128 — donk et sub en contretemps (D01, D02, D05)
tempo: 128
accords: Fm7 | Fm7
donk: F1[1&:1] F1[1a:1] Ab1[2e:1] F2[2&:1] F1[3&:1] C2[3a:1] F1[4e:1] Eb2[4&:1] | F1[1&:1] F1[1a:1] Ab1[2e:1] F2[2&:1] Eb2[3&:1] C2[3a:1] Ab1[4&:1] F1[4a:1]
sub: F0[1&:2] F0[2&:2] F0[3&:2] F0[4&:1] | F0[1&:2] F0[2&:2] Eb0[3&:2] F0[4&:2]
```

Le sub ne joue que les fondamentales en contretemps, sans excursion. Les notes du donk sont des doubles croches : la longueur vient d'ENV 1.

```grille
titre: Future House 126 — bouncy en octaves (D09, D12)
tempo: 126
accords: Gm7 | Gm7
bounce: G1[1&:1] G2[1a:1] G1[2&:1] G2[2a:1] F1[3&:1] F2[3a:1] D2[4&:2] | G1[1&:1] G2[1a:1] G1[2&:1] Bb1[2a:1] C2[3&:1] Bb1[3a:1] G1[4&:2]
sub: G0[1&:2] G0[2&:2] F0[3&:2] D1[4&:2] | G0[1&:2] G0[2&:2] Bb0[3&:2] G0[4&:2]
```

Avec D12, PORTA en ALWAYS fait glisser chaque saut d'octave. Le do de la mesure 2 est une note de passage vers le si bémol.

```grille
titre: Bass House 128 — jump-up ramené au tempo House (D10)
tempo: 128
accords: Em7 | Em7
jump: E1[1e:1] E1[1&:1] E2[2e:1] E1[2a:1] G1[3e:1] E1[3&:1] B1[4e:1] D2[4&:1] | E1[1e:1] E1[1&:1] E2[2e:1] E1[2a:1] D2[3e:1] B1[3&:1] G1[4e:1] E1[4&:1]
sub: E0[1&:2] E0[2&:2] E0[3&:2] B0[4&:2] | E0[1&:2] E0[2&:2] B0[3&:2] E0[4&:2]
```

Ce motif garde la densité d'une ligne jump-up, sans attaque sur les kicks. Le rebond lui-même vient des LFO de D10 (1/16 ou 1/8).

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : les tables Squibble, Harmonic Subtle et SawRoundedToSquare, le filtre Flg L6+, le mode Ratio sur OSC B. Vérifier les destinations des macros.
- Confirmer à l'écran les valeurs d'ENV 1 de D02 (71 / 319 ms / −∞ / 424 ms), lues sur une petite capture.
- Écouter chaque recette avec le kick, puis avec le sub s'il y en a un, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
