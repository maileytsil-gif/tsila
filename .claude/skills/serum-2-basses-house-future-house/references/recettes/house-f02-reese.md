# Vingt recettes de Reese pour la House (famille F02)

Huitième lot de recettes House : le Reese, deux oscillateurs (ou plus) légèrement désaccordés dont le battement fait bouger la basse. Né en 1988 (Kevin Saunderson, « Just Want Another Chance », sur un Casio CZ en distorsion de phase), passé à la jungle, puis revenu en Bass House, Tech House et Speed Garage. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` (F02-01 DNB Academy, F02-03 Strob Studio) ;
- `../etudes-pages-house.md` (F02-02 ADSR) et `../etudes-pages-dubstep-dnb.md` (F02-14 MusicRadar, F13-11) ;
- le § 2 « Reese » de `../../../sound-designer-serum/references/basses.md` (Attack Magazine, Native Instruments, LANDR, Toolroom) ;
- le Reese du corpus `../../../house-future-rave-bass-house-production/references/sound-design-genres.md`, désigné par « Reese du corpus » ;
- `../sources.md` (Production Music Live, Sam Smyers), `../documentation-basses.md` § 3 (battements) et la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes aux vingt recettes

1. **Le Reese n'est jamais le sub.** Le battement fait varier le niveau de la fondamentale, ce que la règle du sub interdit (`basses.md` § 2, « Le problème mono »).
   - Architecture : sub sinus mono séparé, sur la même ligne MIDI (S01 de `house-f01-sub.md`), et Reese coupé-bas au-dessus.
   - Equalizer du Reese : passe-haut vers 100-120 Hz ; tout ce qui reste sous 120 Hz est mono.
2. **Le désaccord règle un tempo, pas une largeur** (Attack Magazine, dans `basses.md`).
   - Battement = f × (2^(c/1200) − 1), où c est l'écart **total** entre les deux voix : ±20 cents font 40 cents [CALCUL, `../documentation-basses.md` § 3].
   - Il double à chaque octave. À 40 cents d'écart :
     - Fa0 → 1,02 Hz ;
     - Fa1 → 2,04 Hz ;
     - Fa2 → 4,08 Hz.
   - Régler le désaccord sur la note la plus jouée de la ligne.
   - Repère de tempo : à 126 BPM, une noire vaut 2,1 Hz ; sur Fa1, ±20,6 cents battent à la noire [CALCUL].
3. **Fourchettes** :
   - ±15 cents : lent et doux ;
   - ±27 à ±30 cents : signature DnB (Attack Magazine et Native Instruments convergent) ;
   - médiane mesurée sur des patchs : 16,6 cents (Reese du corpus, `[DOC-2]`).
   - La valeur « 0,25-0,5 cent » de LANDR est à ignorer (confusion probable entre cents et demi-tons, `basses.md`).
4. **Phase** :
   - RAND 0 : même départ du battement à chaque note, reproductible ;
   - RAND 100 : départ différent à chaque note, plus vivant ;
   - le Reese du corpus impose RAND 0. Le choix est dit dans chaque fiche.
5. **Un Reese statique est un échec** (Reese du corpus) : un LFO lent sur la coupure, en mode FREE pour la dérive, ou RETRIG pour la répétabilité.
6. **Quatre macros communes**, celles de la fiche 6 de `../families.md`, avec `Width` en plus :
   - `Beat` : désaccord ;
   - `Motion` : profondeur du LFO sur la coupure ;
   - `Grit` : drive ;
   - `Width` : chorus, Hyper ou unison, au-dessus du passe-haut seulement.

   Vérifier le « + » sur chaque destination.
7. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
8. **Contrôle par l'utilisateur** :
   - le Reese seul, puis avec le sub, puis avec le kick ;
   - mono : le niveau ne doit pas fluctuer au vumètre plus que voulu, symptôme décrit par Attack Magazine ;
   - la note la plus grave et la plus aiguë (le battement double à chaque octave) ;
   - les deux bornes de `Beat` ;
   - A/B à niveau égal contre R01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| R01 | Reese médium de référence | Bass House, Tech House | 2 scies ±28 cents, LP 650 Hz |
| R02 | Reese doux | Deep House, Tech House | ±15 cents, LFO libre |
| R03 | Reese Strob Studio | toute House | ±20 cents, Phs 36+, désaccord selon la note |
| R04 | Sinus qui respire | breakdown | 2 sinus ±27 cents, une octave au-dessus |
| R05 | Reese unison impair | Bass House | unison 5, 7 ou 9, detune 10-14 % |
| R06 | Reese PML | toute House | 4 voix légères, MG Low 12 |
| R07 | Reese Bass House du corpus | Bass House, Future Rave | FINE ±17, LP 700 Hz, Splitter à 400 Hz |
| R08 | Reese sombre | Tech House | LP 116-225 Hz, chorus 50 % |
| R09 | Reese jungle lissé | Bass House, Garage | encoche balayée |
| R10 | Reese lourd DNB Academy | Bass House lourde | 3 oscillateurs, Combs, PD |
| R11 | Reese AM déchirant | Bass House sombre | AM qui s'installe, LFO libre |
| R12 | Reese à battement constant | toute House | Note → désaccord, −1/2 par octave |
| R13 | Reese Speed Garage | Speed Garage, UKG | chute de hauteur à l'attaque |
| R14 | Reese en unison Exp | Bass House | modes d'accord de l'unison |
| R15 | Reese à la Casio | toute House | PD (Self), deux oscillateurs |
| R16 | Reese à l'Hyper | Bass House | Hyper au lieu de l'unison |
| R17 | Reese Sam Smyers | Deep House | unison 16, LFO sur FIN |
| R18 | Reese une octave au-dessus | Tech House | bandes séparées par l'octave |
| R19 | Reese imprimé en table | toutes | battement calé sur le tempo |
| R20 | Reese en glissés d'octave | Bass House | legato, portamento 250 ms |

## Les vingt recettes

### R01 Reese médium de référence
- **Patch** :
  - OSC A et OSC B en scie (Basic Shapes), même octave (OCT −1), FIN −14 et +14 (±14 cents, 28 cents d'écart). RAND 0 sur les deux.
  - VOICING MONO + LEGATO.
  - FILTER 1 sur A et B, MG Low 24, CUTOFF ≈ 650 Hz, RES ≈ 14 %.
  - LFO 1 → CUTOFF ±200 Hz, FREE, RATE 2 mesures.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion Overdrive légère (DRIVE 15-25), puis Equalizer en passe-haut à 120 Hz.
- **Battement** : 1,43 Hz sur Fa1, 2,86 Hz sur Fa2 [CALCUL].
- **Macros** : `Beat` FIN ±5 → ±30 cents (A et B en sens opposés) · `Motion` LFO 1 → CUTOFF 0 → 50 % · `Grit` DRIVE 0 → 50 · `Width` MIX d'un Chorus en mode HPF 0 → 40 %.
- **Sub associé** : S01, même ligne, aucun désaccord.
- **Jeu** : bloc « Bass House 126 — Reese tenu avec trous » ci-dessous.
- **Origine** :
  - point de départ « Reese médium : 2 saws, ±28 cents, mono/legato, LP 24 dB ~650 Hz, résonance ~14 %, coupe-bas 120 Hz, overdrive léger » [SOURCE `basses.md` § 2, NI et Attack] ;
  - écart de 28 cents au total, à la place de ±28 [ORIGINAL] : la fiche dit « ±28 », qui pourrait aussi se lire 56 cents d'écart. Pour le son DnB, passer à FIN ±28.

### R02 Reese doux — Deep House, Tech House
- **Patch** : R01, avec FIN −7,5 et +7,5 (15 cents d'écart), CUTOFF ≈ 450 Hz, RES 10 %, et RAND 100 (chaque note bat autrement).
- **ENV 1** : attaque 5 ms, sustain 100 %, release 100 ms.
- **FX** : Distortion Tape Sat. légère, passe-haut à 100 Hz.
- **Battement** : 0,76 Hz sur Fa1 [CALCUL].
- **Macros** : `Beat` FIN ±3 → ±15 · `Motion` LFO 1 FREE 4 mesures → CUTOFF · `Grit` DRIVE · `Width` —.
- **Sub associé** : S12, glissé Deep House.
- **Origine** : « ±15 cents = lent et doux » [SOURCE `basses.md`, NI « version douce ±15 »] ; réglages [ORIGINAL]. Le « ±15 » de NI est ici lu comme 15 cents d'écart : pour l'autre lecture, FIN ±15.

### R03 Reese Strob Studio — désaccord selon la note
- **Patch** :
  - OSC A et OSC B en scie (Default), OCT 0, FIN −20 / +20 (écran : −21 / +21 puis −20 / +20). Mieux vaut désaccorder les deux en sens opposés qu'un seul de 40.
  - VOICING MONO, un peu de portamento.
  - FILTER 1 en Phs 36+ (le « phaser positif ») sur A et B, un peu de DRIVE.
  - LFO 1 en triangle, 4 mesures → CUTOFF.
  - Matrice : source Note → FIN, pour que le battement change avec la hauteur. Le tutoriel veut que les notes aiguës battent plus vite ; R12 fait l'inverse.
- **ENV 1 (écran)** : 0,5 ms / 0 / 1,00 s / 0 dB / 15 ms, les valeurs de l'Init. Release à 60 ms si les notes claquent [ORIGINAL].
- **FX** : Distortion Tube, filtre OFF ; à 50 % de MIX selon le tutoriel, pour garder un grave propre. Puis passe-haut à 120 Hz [ORIGINAL].
- **Macros** : `Beat` FIN ±10 → ±30 · `Motion` LFO 1 → CUTOFF du phaser · `Grit` DRIVE de la Tube · `Width` —.
- **Sub associé** :
  - S03 (triangle) sur sa piste. Le tutoriel ajoute un sub triangle en `Direct Out` dans le patch.
  - Sa variante : monter A et B d'une octave et laisser le sub une octave plus bas, ce qui sépare les bandes (R18).
- **Origine** :
  - [SOURCE F02-03, transcription française bruitée et trois captures, Serum 1] ;
  - « plus on désaccorde, plus le battement est rapide, mais on perd la note » ;
  - distorsion multibande hors du sub ; OTT pour un son plus moderne.

### R04 Sinus qui respire — breakdown
- **Patch** :
  - OSC A et OSC B en sinus, FIN −27 et +27, MONO. RAND 0.
  - Jouer une octave au-dessus de la ligne de sub (Fa1-Do2, 87-131 Hz).
- **ENV 1** : attaque 20 ms, sustain 100 %, release 300 ms.
- **FX** : Reverb Plate (MIX ≤ 10 %, LO CUT haut). Pas de passe-haut fixe : il viderait ce son, qui n'a que sa fondamentale. Le jouer **seul**, sans sub, dans un breakdown.
- **Battement** : 54 cents d'écart sur Fa1 font 2,8 Hz [CALCUL].
- **Macros** : `Beat` FIN ±10 → ±30 · `Motion` attaque d'ENV 1 · `Grit` — · `Width` —.
- **Sub associé** : aucun : ce son ne se superpose pas à un sub.
- **Test** : au vumètre, le niveau monte et descend (c'est voulu). Le couper avant le retour du kick et du sub.
- **Origine** :
  - Attack Magazine construit le Reese avec deux sinus, mono, ±27 cents : un « sub qui respire » ;
  - « cette version a un niveau de volume plutôt incohérent » [SOURCE `basses.md` § 2] ;
  - usage limité au breakdown [ORIGINAL], à cause de la règle du sub.

### R05 Reese unison impair — Bass House
- **Patch** :
  - OSC A en scie, OCT −1. Unison 5, 7 ou 9 (impair : une voix reste au centre), DETUNE 10-14 %.
  - VOICING MONO, un peu de glide.
  - OSC B en scie (ou table « fifth harmonic »), une octave plus bas, LEVEL à doser.
  - FILTER 1 sur A et B, MG Low 12 ou 24, DRIVE et FAT, un peu de RES.
  - LFO 1, BPM désactivé, lent → CUTOFF et → DETUNE d'OSC A, faible quantité.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** :
  1. Distortion Tube ou Diode.
  2. Compressor Multiband.
  3. Chorus ou Dimension, « en gardant la basse mono sous 120 Hz » : Utility, MONO BASS à 120 Hz.
  4. Equalizer : creux vers 250 Hz, et passe-haut à 120 Hz au lieu de l'accentuation à 80-120 Hz de la page, puisque le sub est séparé.
- **Macros** : `Beat` DETUNE 5 → 20 % · `Motion` LFO 1 → CUTOFF · `Grit` DRIVE · `Width` MIX du Chorus.
- **Sub associé** : S01. La page route le sous-oscillateur dans le même filtre ; ici il est sur sa piste.
- **Origine** :
  - « seuls repères chiffrés pour le Reese : unison 5/7/9 et detune 10-14 % » [SOURCE F02-02, page ADSR] ;
  - le reste est à valider ;
  - le DETUNE en % n'est pas convertible en cents sans mesure (Reese du corpus).

### R06 Reese PML — quatre voix légères
- **Patch** :
  - OSC A en scie, OCT −1, Unison 4, DETUNE faible.
  - FILTER 1 en MG Low 12, DRIVE monté.
  - RAND 0.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : passe-haut à 120 Hz, Utility MONO BASS à 120 Hz.
- **Macros** : `Beat` DETUNE · `Motion` LFO 1 FREE → CUTOFF · `Grit` DRIVE du filtre · `Width` —.
- **Sub associé** : S01. Le tutoriel ajoute un sub sinus.
- **Origine** :
  - « saw initiale, filtre MG Low 12, quatre voix légèrement détunées, sub sine et filtre drive ; ancien Serum à transposer » [SOURCE Production Music Live, tutoriel écrit et captures, `../sources.md`] ;
  - valeurs [ORIGINAL].

### R07 Reese Bass House du corpus — FINE ±17, Splitter à 400 Hz
- **Patch** :
  - OSC A et OSC B en scie, FIN −17 et +17. MONO + LEGATO, RAND 0.
  - FILTER 1 en MG Low 24, CUTOFF 700 Hz, RES 25.
  - LFO 1 → CUTOFF, 1 mesure, 35 %.
- **ENV 1** : sustain 100 %, release 24 ms.
- **FX** :
  1. Chorus : délais 30 ms, RATE ≈ 0, DEPTH au maximum, MIX 60 %.
  2. Splitter L/H à 400 Hz : Tube 30 % dans LOWS, Tape Sat. 65 % dans HIGHS.
  3. Equalizer : creux 1,6-3,8 kHz, bosse 450-800 Hz. Passe-haut à 120 Hz ajouté.
- **Macros** : `Beat` FIN ±8 → ±30 · `Motion` LFO 1 → CUTOFF 0 → 50 % · `Grit` drive des deux bandes · `Width` MIX du Chorus.
- **Sub associé** : S01, « sub sinus séparé non désaccordé ».
- **Origine** :
  - [SOURCE Reese du corpus, `[DOC-2]`] : médiane mesurée 16,6 cents → FINE +17 ; « un Reese statique est un échec » ; « jamais en rôle de sub » ;
  - lecture de « FINE +17 » comme ±17 [ORIGINAL].

### R08 Reese sombre — Tech House
- **Patch** :
  - R01, avec CUTOFF 116-225 Hz (filtre très fermé) et RES 10 %.
  - Jouer une octave au-dessus du sub, sinon le passe-haut à 120 Hz vide tout.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Chorus MIX ≈ 50 %, puis passe-haut à 100 Hz.
- **Macros** : `Beat` · `Motion` CUTOFF 100 → 400 Hz · `Grit` · `Width` MIX du Chorus.
- **Sub associé** : S01.
- **Test** : avec un filtre aussi fermé, il reste surtout la fondamentale et le 2e harmonique : vérifier que le battement s'entend encore sur petit haut-parleur.
- **Origine** :
  - « LANDR : passe-bas entre 116 et 225 Hz, chorus à ~50 % » [SOURCE `basses.md` § 2] ;
  - registre une octave au-dessus [ORIGINAL].

### R09 Reese jungle lissé — encoche balayée
- **Patch** :
  - R01, avec FILTER 1 vers FILTER 2 en série. FILTER 2 en Notch 24, CUTOFF 400 Hz-2 kHz, RES 30 %.
  - LFO 2 → CUTOFF de FILTER 2, RETRIG, 2 mesures (ou automation de la macro dans Live).
- **ENV 1** : comme R01.
- **FX** : Distortion Overdrive après les filtres, passe-haut à 120 Hz.
- **Macros** : `Beat` · `Motion` LFO 2 → encoche · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Origine** :
  - « NI : passe-bas cutoff ~650 Hz, résonance ~14 % pour le son jungle lissé, puis overdrive et filtre à encoche balayé automatisé » [SOURCE `basses.md` § 2] ;
  - encoche en série [ORIGINAL].

### R10 Reese lourd DNB Academy — trois oscillateurs, Combs
- **Patch** :
  - OSC A et OSC B en scie, OCT −2 (−3 dans la source, en DnB), FIN −38 et +38 (dit ; l'écran montre −38 et −28).
  - OSC C sur la table Analog « DM - Oscar », SEM +7, à niveau réduit.
  - NOISE allumé (bruit blanc de Serum 2).
  - FILTER 1 sur A, B, C et noise, en Combs, CUTOFF ≈ 30-31, VAR ≈ 50 %. MONO + LEGATO.
  - Warp de A en PD (B) : 73-74 dit, 64 % à l'écran.
  - LFO 1 en RETRIG, montée rapide puis descente lente, 2 mesures → CUTOFF ≈ 45 %.
- **ENV 1** : non lue [ORIGINAL : attaque 2 ms, sustain 100 %, release 80 ms].
- **FX** :
  1. Distortion Overdrive ×2.
  2. Chorus.
  3. Filter MG Low 6 (la voix dit « low cut », l'écran montre un passe-bas).
  4. Compressor Multiband : −18,1 dB, 4:1, 90,1 / 90,1, gain 4,2, bandes à 128 et 2 500 Hz.
  5. Equalizer : 210 Hz, Q 80, 0 dB ; creux à 484 Hz, Q 80, −15,6 dB.
  6. Passe-haut à 120 Hz ajouté [ORIGINAL].
- **Réglage final** : réintroduire la table Oscar, 2 voix d'unison.
- **Macros** : `Beat` FIN ±20 → ±40 · `Motion` LFO 1 → CUTOFF · `Grit` PD 40 → 80 % · `Width` MIX du Chorus.
- **Sub associé** : S01. La source route le sub dans le filtre 1 « pour un grave plus concis » ; ici il est sur sa piste.
- **Battement** : ±38 cents (76 cents d'écart) battent à 3,9 Hz sur Fa1 [CALCUL] : un Reese nerveux.
- **Origine** : [SOURCE F02-01, transcription et quatre captures, Serum 2, DnB].

### R11 Reese AM déchirant
- **Patch** :
  - OSC A sur une table « gnarly » (Digital), OCT −1.
  - LFO 1 en FREE, lent, non synchronisé → WT POS : chaque note bouge autrement.
  - OSC B en sinus, LEVEL 0. WARP 1 d'OSC A en AM (B).
  - ENV 2 → ce warp, attaque lente (400-800 ms), sustain 100 % : l'AM s'installe au cours de la note.
  - NOISE poussé dans la distorsion finale (le « fizz »).
  - FILTER 1 en Notch 24 modulé (double encoche dans la source ; à défaut, NN 12 de la catégorie Multi).
  - MONO + LEGATO, PORTA vers midi.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Reverb, puis Compressor lourd **après** la reverb (le son gonfle entre les notes), puis Distortion forte, puis Equalizer (passe-haut à 120 Hz), puis élargissement au-dessus de 300 Hz.
- **Macros** : `Beat` attaque d'ENV 2 · `Motion` LFO 1 → WT POS · `Grit` DRIVE · `Width` largeur.
- **Sub associé** : S01. Le preset d'origine garde un sub dans le patch.
- **Origine** :
  - analyse du preset d'usine `Bs Reese Evolve` [SOURCE F02-14, page MusicRadar, Serum 1, aucune valeur chiffrée sauf le portamento] ;
  - imprimer plusieurs minutes d'un riff et garder les meilleures prises : voir R19.

### R12 Reese à battement constant — Note → désaccord
- **Patch** :
  - R01, avec FIN de A et B pilotés par la source Note (matrice, quantité négative) : le désaccord diminue de moitié par octave montée.
  - Exemple : ±20 cents sur Fa1, ±10 sur Fa2, ±5 sur Fa3.
- **Calcul** : battement = f × (2^(c/1200) − 1) ≈ f × c × 0,000578 pour de petits écarts. Si f double et c est divisé par deux, le battement reste ≈ 2 Hz [CALCUL].
- **ENV 1** : comme R01.
- **Macros** : `Beat` désaccord de base · `Motion` · `Grit` · `Width`, comme R01.
- **Sub associé** : S01.
- **Test** : sur une ligne qui saute d'une octave, le battement doit garder la même vitesse ; comparer avec R01, où il double.
- **Origine** :
  - « le battement change de vitesse selon la note jouée », et c'est rarement mentionné (`basses.md`, [I]) ;
  - Strob module le désaccord par la note dans l'autre sens (R03) ;
  - recette [ORIGINAL]. L'échelle de la source Note dans la matrice est à régler dans l'interface.

### R13 Reese Speed Garage — chute de hauteur à l'attaque
- **Patch** :
  - R01, avec ENV 3 → CRS de A et B : −3 à −5 demi-tons au départ de la note, retour en 60-120 ms.
  - FILTER 1 : MG Low 24, CUTOFF ≈ 400 Hz, ENV 2 → CUTOFF +40 %, decay 200 ms.
- **ENV 1** : attaque 1 ms, decay 400 ms, sustain −4 dB, release 60 ms.
- **FX** : Distortion Soft Clip, Compressor Single, passe-haut à 120 Hz.
- **Macros** : `Beat` FIN · `Motion` ENV 3 → CRS 0 → −5 · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01, sans chute de hauteur.
- **Jeu** : bloc « Speed Garage 132 — Reese en 2-step » ci-dessous.
- **Origine** : [ORIGINAL]. Les tutoriels Speed Garage et UKG du registre (F02-04, F02-05, F02-08) ne sont pas étudiés.

### R14 Reese en unison Exp — les modes d'accord de Serum 2
- **Patch** :
  - OSC A en scie, OCT −1, Unison 3, panneau d'unison en TUNING = Exp (essayer Linear, Super, Inv), RANGE 2 demi-tons (par défaut), DETUNE 5-15 %.
  - VOICING MONO.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 600 Hz.
  - LFO 1 FREE, 2 mesures → DETUNE ±3 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : passe-haut à 120 Hz, Utility MONO BASS à 120 Hz.
- **Macros** : `Beat` DETUNE · `Motion` LFO 1 → DETUNE · `Grit` DRIVE du filtre · `Width` WIDTH de l'unison.
- **Sub associé** : S01.
- **Test** : comparer les modes TUNING à DETUNE égal. Garder celui dont la voix centrale reste nette.
- **Origine** :
  - réglages d'unison (RANGE, WIDTH, TUNING Linear / Super / Exp / Inv / Random) [cartographie, § 9] ;
  - le mapping DETUNE × RANGE de Serum 2 est signalé non chiffré (Reese du corpus) ;
  - recette [ORIGINAL].

### R15 Reese à la Casio — distorsion de phase
- **Patch** :
  - OSC A et OSC C en sinus, OCT −1, FIN −12 et +12.
  - WARP 1 de chacun en PD (Self), 30-50 %.
  - ENV 2 → les deux warps, +20 %, decay 300 ms.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 60 %.
  - MONO + LEGATO, RAND 0.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Chorus léger, passe-haut à 120 Hz.
- **Macros** : `Beat` FIN ±5 → ±25 · `Motion` quantité de PD · `Grit` ENV 2 → PD · `Width` MIX du Chorus.
- **Sub associé** : S01.
- **Test** : A/B avec R01 à niveau égal. Le son doit garder un battement, avec une couleur plus douce que les scies.
- **Origine** :
  - le Reese d'origine est fait sur un Casio CZ-5000, donc en distorsion de phase ; les deux scies désaccordées sont « la reconstruction moderne » [SOURCE `basses.md` § 2, quatre sources concordantes] ;
  - PD de Serum 2 à rapprocher du CZ sans supposer qu'il est identique (`../documentation-basses.md` § 1) ;
  - recette [DÉDUCTION].

### R16 Reese à l'Hyper — moins de voix, autant de largeur
- **Patch** :
  - R01 avec Unison 1.
  - Rack FX : Splitter L/H à 200 Hz. Dans HIGHS, Hyper/Dimension : UNISON 4-7, DETUNE 20-30 %, MIX 30-50 %, SIZE de Dimension 0.
- **ENV 1** : comme R01.
- **Macros** : `Width` MIX de l'Hyper · les autres comme R01.
- **Sub associé** : S01.
- **Test** : en mono, la largeur doit disparaître sans faire varier le niveau du grave.
- **Origine** :
  - le manuel recommande Hyper **plutôt que** beaucoup d'unisson, pour économiser le CPU ; au-delà de 3 à 7 voix d'unisson par oscillateur, c'est rarement utile [cartographie, § 8-9] ;
  - recette [ORIGINAL].

### R17 Reese Sam Smyers — unison 16, LFO sur FIN
- **Patch** :
  - OSC A en scie, OCT −1 (−2 dans la source), Unison 16.
  - FILTER 1 avec DRIVE et FAT ; ENV 2 → CUTOFF.
  - VOICING MONO, portamento possible.
  - LFO 1 en sinus → FIN d'OSC A, faible profondeur.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : Compressor, passe-haut à 150 Hz (16 voix s'annulent sous 100 Hz).
- **Macros** : `Beat` profondeur de LFO 1 → FIN · `Motion` ENV 2 → CUTOFF · `Grit` DRIVE · `Width` STACK ou nombre de voix.
- **Sub associé** : S01.
- **Test** : si le grave fluctue, diminuer le nombre de voix ou le detune ; enregistrer séparément le Reese médium et le sub pur.
- **Origine** :
  - geste dit : saw −2, unison 16, filtre drive/fat, ENV 2 vers cutoff, mono, portamento possible, LFO sinus sur fine tuning, compresseur [SOURCE Sam Smyers « 5 Deep House Basses », transcription, Serum 1] ;
  - l'unison 16 contredit le conseil CPU du manuel (R16).

### R18 Reese une octave au-dessus — bandes séparées
- **Patch** :
  - R01, joué une octave au-dessus du sub : Reese en Sol2-Do3, sub en Sol0-Do1.
  - FIN ±10 seulement : à cette hauteur, le battement est déjà rapide.
  - CUTOFF ≈ 1,2 kHz.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −6 dB, release 60 ms.
- **FX** : Distortion Tape Sat., passe-haut à 150 Hz.
- **Battement** : 20 cents d'écart sur Sol2 (196 Hz) battent à 2,3 Hz [CALCUL].
- **Macros** : `Beat` FIN ±5 → ±20 · `Motion` CUTOFF · `Grit` DRIVE · `Width` MIX d'un Chorus HPF.
- **Sub associé** : S02, à phase continue, sous une ligne roulante.
- **Jeu** : bloc « Tech House 124 — Reese une octave au-dessus » ci-dessous.
- **Origine** :
  - astuce : monter A et B d'une octave et laisser le sub une octave plus bas, ce qui sépare les bandes ; le Reese est alors moins grave [SOURCE F02-03] ;
  - valeurs [ORIGINAL].

### R19 Reese imprimé en table — battement calé sur le tempo
- **Patch** :
  1. Construire R01 ou R07, imprimer une note tenue de 2 à 4 mesures (procédure de `../../../resampling/SKILL.md`).
  2. La remettre dans OSC A (glisser le WAV ou Resample to) : le battement devient une suite de frames.
  3. LFO 1 → WT POS en BPM (1 mesure ou 2) : le battement suit désormais le tempo, et non plus la note.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **Macros** : `Beat` RATE de LFO 1 · `Motion` profondeur de LFO 1 → WT POS · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Test** : A/B avec la version d'origine sur trois notes. La table sonne à toutes les hauteurs avec le même rythme de battement.
- **Origine** :
  - « ressampler le son et le réimporter comme wavetable » [SOURCE F02-02] ;
  - imprimer plusieurs minutes d'un riff et garder les meilleures prises [SOURCE F02-14] ;
  - battement calé sur le tempo [DÉDUCTION, jamais essayée].

### R20 Reese en glissés d'octave — legato, portamento 250 ms
- **Patch** :
  - R01, avec VOICING MONO + LEGATO, PORTA 250 ms, SCALED allumé.
  - Notes courtes une octave au-dessus des notes graves, reliées par portamento.
  - RAND 0 : attaque identique à chaque note.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **Tempo** : à 128 BPM, 250 ms dépassent une croche (234 ms). Le glissé occupe la croche entière : le réduire à 120-180 ms si la note d'arrivée se brouille [CALCUL].
- **Macros** : `Beat` FIN · `Motion` PORTA 60 → 250 ms · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01 sans glissé. Le sub ne suit que les notes graves, pas les notes une octave au-dessus.
- **Origine** :
  - « notes courtes une octave au-dessus des notes graves, reliées par portamento ; Mono actif, Portamento 250 ms ; RandPhase désactivé » [SOURCE F13-11, page MusicRadar, neurofunk à 174 BPM] ;
  - transposition au tempo House [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Kick supposé sur les quatre temps (doubles croches 1, 5, 9, 13), sauf en Speed Garage. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f02-reese.md`. Le bloc « DnB 174 — Reese long avec trous » de `../motifs.md` servira au lot DnB.

```grille
titre: Bass House 126 — Reese tenu avec trous (R01, R07)
tempo: 126
accords: Fm7 | Fm7
reese: F1[1&:6] Ab1[3&:4] Eb1[4a:1] | F1[1&:6] C2[3&:2] Bb1[4&:1] Ab1[4a:1]
sub: F0[1&:6] Ab0[3&:4] Eb0[4a:1] | F0[1&:6] C1[3&:2] Bb0[4&:1] Ab0[4a:1]
```

Tenues de six doubles croches (714 ms à 126 BPM) : un battement de 1,4 Hz (R01 sur Fa1) y fait un cycle complet. Le si bémol est une note de passage vers le la bémol. Les tenues recouvrent le kick suivant : creux de S10 ou sidechain par plug-in tiers.

```grille
titre: Tech House 124 — Reese une octave au-dessus (R18)
tempo: 124
accords: Gm7 | Gm7
reese: G2[1e:3] G2[2e:2] Bb2[2a:2] D2[3a:3] F2[4a:1] | G2[1e:3] G2[2e:2] C3[2a:2] Bb2[3a:3] G2[4a:1]
sub: G0[1&:2] G0[2&:2] D1[3&:2] F0[4&:2] | G0[1&:2] G0[2&:2] Bb0[3&:2] G0[4&:2]
```

Le Reese et le sub ont des rythmes différents : le sub tient les contretemps, le Reese remplit les doubles croches « e » et « a ». Le do de la mesure 2 est une note de passage.

```grille
titre: Speed Garage 132 — Reese en 2-step (R13)
tempo: 132
accords: Em7 | Em7
reese: E1[1:3] E1[1a:1] G1[2&:3] E1[3a:2] B1[4&:2] | E1[1:3] E1[1a:1] D2[2&:3] B1[3a:2] G1[4&:2]
sub: E0[1:3] E0[1a:1] G0[2&:3] E0[3a:2] B0[4&:2] | E0[1:3] E0[1a:1] D1[2&:3] B0[3a:2] G0[4&:2]
```

En 2-step, la basse attaque avec le kick du temps 1. Recaler les autres attaques sur le vrai pattern de batterie.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : la table « DM - Oscar », une table « gnarly », le filtre Phs 36+, les modes TUNING de l'unison, l'échelle de la source Note dans la matrice. Vérifier les destinations des macros.
- Trancher la lecture des fourchettes « ±28 » et « ±15 » (par voix ou écart total) à l'oreille, avec la table de battement des règles communes.
- Écouter chaque recette avec le sub, puis avec le kick, en mono, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
