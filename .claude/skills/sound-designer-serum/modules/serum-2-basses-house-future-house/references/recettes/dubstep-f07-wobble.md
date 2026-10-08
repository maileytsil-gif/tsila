# Vingt recettes de wobble pour le Dubstep (famille F07)

Cinquième lot Dubstep : le wobble dans son genre d'origine. On y trouve le « lurch » lent du dubstep UK, le wub classique, le wobble profond et le chillstep, à 140 BPM en half-time. `house-f07-wub.md` adapte les mêmes gestes à la House ; les recettes identiques y renvoient, et celles-ci ajoutent ce qui est propre au dubstep : LFO aléatoires et chaotiques, wobble FM profond, macros automatisées dans l'arrangement. Rédigé le 05/10/2026. Sources :
- `../etudes-pages-house.md` : F07-01 Monosounds, F07-23 MusicRadar ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` : F01-08 EDMProd UK dubstep, F15-06 EDMProd liquid, F02-14, F08-04 ;
- le Warping Bass d'Attack Magazine dans `../../../../references/patches-genres.md` ;
- la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL]. Les tutoriels de deep dubstep et de chillstep du registre (F07-17 à F07-20) ne sont pas étudiés : les recettes qui portent ces noms sont [ORIGINAL].

## Règles

1. **Règles communes du lot Dubstep** : celles de `dubstep-f10-riddim.md`. **Règles du wub** : celles de `house-f07-wub.md` :
   - wobble au-dessus de 100 Hz ;
   - sub séparé et stable ;
   - LFO RETRIG pour les riffs, FREE + HOST pour les tenues ;
   - plage de 150 Hz à 1-2 kHz ;
   - distorsion après le filtre.
2. **Divisions à 140 BPM** [CALCUL] :
   - 1/2 = 857,1 ms ;
   - 1/4 = 428,6 ms (« slow dubstep lurch ») ;
   - 1/8 pointée = 321,4 ms ;
   - 1/8 = 214,3 ms (« classic wub ») ;
   - 1/8 triolet = 142,9 ms ;
   - 1/16 = 107,1 ms (« talking »).

   Le « lurch » à 1/4, le wub à 1/8 et le talking à 1/16 sont nommés par F07-01.
3. **Quatre macros communes**, celles de `house-f07-wub.md` : `Rate`, `Depth`, `Vowel`, `Grit`. Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| WD01 | Lurch lent | dubstep UK, référence | LFO 1/4 sur passe-bas |
| WD02 | Wub classique | dubstep | 1/8, 214 ms |
| WD03 | Main Sub UK en médium | dubstep UK | carré, 1/8 pointée, peigne |
| WD04 | Wobble FM profond | deep dubstep | les harmoniques bougent, la fondamentale reste |
| WD05 | Divisions enchaînées | build, drop | 1/4 → 1/8 → 1/8T → 1/16 |
| WD06 | Wobble chillstep | chillstep | passe-bas doux, 1/2 |
| WD07 | Wobble AM qui suit la note | dubstep old-school | modulateur à −4 octaves |
| WD08 | Talking bégayant | dubstep | 1/16 avec cran |
| WD09 | Wobble en triolets | dubstep | 1/8 triolet, 143 ms |
| WD10 | Wobble pointé | dubstep UK | 1/8 pointée contre la caisse claire |
| WD11 | Wobble au peigne | dubstep UK | Cmb HL6+ balayé |
| WD12 | Wub et grain FM | dubstep | même LFO sur filtre et FM |
| WD13 | Un wub par note | stabs | LFO ENVELOPE |
| WD14 | Séquence dessinée | dubstep | LFO d'une mesure (1,7 s) |
| WD15 | Wobble aléatoire | dubstep expérimental | LFO de type S&H |
| WD16 | Wobble chaotique | deep dubstep | LFO Chaos: Lorenz |
| WD17 | Wobble vocal | dubstep | formant à 1/4 |
| WD18 | Warping Bass 3/16 | dubstep | filtre en série, 321 ms |
| WD19 | Wobble de l'arrangement | toutes | macros automatisées |
| WD20 | Wobble ressamplé | toutes | 2-3 passes |

## Les vingt recettes

### WD01 Lurch lent — référence
- **Patch** : W01 de `house-f07-wub.md`, avec trois différences.
  - OSC A une octave plus bas (OCT −2).
  - LFO 1 à 1/4 (428,6 ms), RETRIG, forme montée lente et descente rapide.
  - Plage du filtre de ≈ 150 Hz à 1 kHz.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 100 ms.
- **FX** : Distortion Tube après le filtre, Equalizer (passe-haut à 100 Hz, −3 dB vers 3-5 kHz).
- **Macros** : celles de W01.
- **Sub associé** : S01 de `house-f01-sub.md`, recalé à 140 BPM.
- **Jeu** : bloc « Dubstep 140 — tenues de lurch » ci-dessous.
- **Origine** : 1/4 pour le « slow dubstep lurch », plage, forme, distorsion après filtre [SOURCE F07-01].

### WD02 Wub classique — 1/8
- **Patch** : WD01 avec LFO 1 à 1/8 (214,3 ms), et le grain FM de W02 (sinus une ou deux octaves sous A, même LFO sur la FM).
- **ENV 1** : comme WD01.
- **Macros** : celles de W02.
- **Sub associé** : S01.
- **Origine** : 1/8 pour le « classic wub » ; grain par FM [SOURCE F07-01].

### WD03 Main Sub UK ramenée en médium
- **Patch** : W05 de `house-f07-wub.md`, à 140 BPM : LFO 1 en arche (« Dome »), TRIG, 1/8 pointée (321,4 ms).
  - La chaîne est inchangée : Hyper (UNISON 3, MIX ≈ 28 %), Sine Shaper (DRIVE ≈ 17 %), Cmb HL6+ (HL WID ≈ 90 %).
- **ENV 1** : 0,5 ms / 0 / 1,00 s / 0 dB / 20 ms ; MONO + LEGATO.
- **Macros** : MACRO 1 sur le cutoff, MACRO 2 sur la FM, MACRO 3 sur le drive **et** le mix inversé.
- **Sub associé** : S01. La « Main Sub » d'origine porte FM, distorsion et peigne : le grave passe au sub.
- **Origine** : [SOURCE F01-08, page et captures, 140 BPM].

### WD04 Wobble FM profond — la fondamentale reste
- **Patch** :
  - OSC A en sinus, OCT −1, RAND 0, PHASE 0 % : la fondamentale de la couche médium, entre 80 et 160 Hz.
  - OSC B en sinus, OCT 0 (rapport 1:2), LEVEL 0. WARP 1 d'OSC A en FM (B), base 0.
  - LFO 1 (RETRIG, 1/4) → WARP 1, de 0 à +30 % : les harmoniques impairs (3, 5, 7…) montent et descendent, la fondamentale reste.
  - Pas de filtre.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 120 ms.
- **FX** : Distortion Tape Sat. légère, Equalizer (passe-haut à 70 Hz : la fondamentale de la couche doit rester).
- **Macros** : `Rate` RATE de LFO 1 · `Depth` LFO 1 → WARP 1 · `Vowel` rapport de B (Ratio 2 / 3 / 4) · `Grit` DRIVE.
- **Sub associé** : S01 une octave plus bas, sans FM.
- **Test** : au vumètre, le niveau doit rester stable ; seul le timbre bouge.
- **Origine** :
  - FM 1:2 → harmoniques impairs [CALCUL, `../documentation-basses.md` § 1] ;
  - recette [ORIGINAL]. Le tutoriel « deep FM wobble sub bass » du registre (F07-17) n'est pas étudié.

### WD05 Divisions enchaînées — build et drop
- **Patch** : W04 de `house-f07-wub.md` à 140 BPM.
  - Macro `Rate` sur le RATE de LFO 1, de 1/4 à 1/16.
  - La bascule TRIP est séparée du RATE : pour passer en 1/8 triolet, automater aussi TRIP, ou préparer un second LFO déjà en triolet et passer de l'un à l'autre par une macro.
- **ENV 1** : comme WD01.
- **Macros** : celles de W04.
- **Sub associé** : S01.
- **Jeu** : 1/4 pendant 4 mesures, 1/8 pendant 2, 1/8 triolet pendant 1, 1/16 sur la dernière, puis silence avant le drop.
- **Origine** :
  - automatiser 1/4 → 1/8 → 1/16 sur une phrase [SOURCE F07-01] ;
  - TRIP et DOT sont des bascules séparées : l'automation du RATE reste sur des divisions droites [cartographie, § 7.2].

### WD06 Wobble chillstep — doux et lent
- **Patch** :
  - OSC A en scie, OCT −1, Unison 3, DETUNE bas.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 300 Hz, RES 10 %.
  - LFO 1 (1/2, mode FREE, HOST) → CUTOFF, plage de 300 à 900 Hz, forme sinus.
- **ENV 1** : attaque 20 ms, sustain 100 %, release 400 ms.
- **FX** : Chorus HPF (MIX 20 %), Reverb Plate en envoi (LO CUT haut, MIX ≤ 15 %), passe-haut à 120 Hz.
- **Macros** : `Rate` 1/1 → 1/4 · `Depth` · `Vowel` RES · `Grit` MIX du Chorus.
- **Sub associé** : S12 (glissé), recalé à 140 BPM.
- **Origine** : [ORIGINAL]. Le tutoriel chillstep du registre (F07-18) n'est pas étudié.

### WD07 Wobble AM qui suit la note
- **Patch** : W09 de `house-f07-wub.md` : B en sinus quatre octaves sous A, WARP 1 de A en AM (B), ENV 2 à attaque lente sur le warp.
- **Vitesse** [CALCUL] :
  - Fa1 (87,3 Hz) → 5,5 Hz ;
  - Mi1 (82,4 Hz) → 5,2 Hz ;
  - La1 (110 Hz) → 6,9 Hz.

  À 140 BPM, 5,5 Hz (182 ms par cycle) tombe entre la 1/8 triolet (7 Hz) et la 1/8 pointée (3,1 Hz). Ce wobble ne se cale pas sur le tempo : c'est le geste « old-school ».
- **ENV 1** : comme W09.
- **Macros** : celles de W09.
- **Sub associé** : S01.
- **Origine** : [SOURCE F02-14] ; octave −4 [DÉDUCTION].

### WD08 Talking bégayant — 1/16 avec cran
- **Patch** : W03 de `house-f07-wub.md` à 140 BPM : LFO 1 à 1/16 (107,1 ms), forme à cran au milieu de la descente.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **Macros** : celles de W03.
- **Sub associé** : S10, recalé à 140 BPM.
- **Origine** : 1/16 « talking », cran = bégaiement [SOURCE F07-01].

### WD09 Wobble en triolets — 1/8 triolet
- **Patch** : WD01 avec LFO 1 à 1/8 et TRIP (142,9 ms), RETRIG, SMOOTH 20.
- **ENV 1** : comme WD01.
- **Macros** : `Rate` 1/4T → 1/16T · les autres comme WD01.
- **Sub associé** : S01.
- **Jeu** : une blanche (857,1 ms) porte six wubs [CALCUL].
- **Origine** : TRIP [cartographie, § 7.2] ; division courante en dubstep [ORIGINAL].

### WD10 Wobble pointé contre la caisse claire
- **Patch** : WD01 avec LFO 1 à 1/8 pointée (321,4 ms), RETRIG.
- **ENV 1** : comme WD01.
- **Macros** : celles de WD01.
- **Sub associé** : S01.
- **Jeu** : bloc « Dubstep 140 — wobble pointé » ci-dessous. Une note qui part sur le temps 1 et tient une demi-mesure porte trois wubs, qui partent à 0, 321 et 643 ms ; elle s'arrête sur la caisse claire (857 ms), au milieu du troisième [CALCUL].
- **Origine** : LFO 1 « Dome », TRIG, 1/8 pointée [SOURCE F01-08, écran].

### WD11 Wobble au peigne — Cmb HL6+
- **Patch** :
  - OSC A sur une carrée (BSOD_Square ou Basic Shapes), OCT −1, RAND 0.
  - Rack FX : Distortion Sine Shaper, puis Filter Cmb HL6+, CUTOFF ≈ 9 h (de départ), RES ≈ 10 h 30, DRIVE ≈ 10 h, HL WID ≈ 16 h 30.
  - LFO 1 (1/8 pointée, TRIG) → CUTOFF du peigne.
- **ENV 1** : comme WD03.
- **Macros** : `Rate` · `Depth` LFO 1 → CUTOFF du peigne · `Vowel` HL WID · `Grit` DRIVE et MIX inversé.
- **Sub associé** : S01.
- **Origine** : Filter FX Cmb HL6+, positions lues [SOURCE F01-08, écran, estimations visuelles] ; LFO sur le peigne [ORIGINAL].

### WD12 Wub et grain FM — même LFO
- **Patch** : W02 de `house-f07-wub.md` à 140 BPM, LFO 1 à 1/8 (214,3 ms) vers CUTOFF et WARP 1 (FM).
  - Ajouter LFO 1 → WT POS si A est une table, pour une troisième cible.
- **ENV 1** : comme W02.
- **Macros** : celles de W02.
- **Sub associé** : S01.
- **Origine** : un LFO vers deux ou trois cibles : cutoff, FM, WT position [SOURCE F07-01].

### WD13 Un wub par note — LFO ENVELOPE
- **Patch** : WD01 avec LFO 1 en mode ENVELOPE (un seul cycle), 1/4.
  - Chaque note, courte ou longue, fait un seul « wub ».
- **ENV 1** : attaque 1 ms, decay 400 ms, sustain −6 dB, release 60 ms.
- **Macros** : celles de WD01.
- **Sub associé** : S11.
- **Jeu** : stabs en réponse à la caisse claire.
- **Origine** : mode ENVELOPE [cartographie, § 7.2] ; usage [ORIGINAL].

### WD14 Séquence dessinée — LFO d'une mesure
- **Patch** : W19 de `house-f07-wub.md` à 140 BPM. LFO 1 sur 1 mesure (1 714,3 ms), RETRIG.
  - Forme dessinée : deux wubs de noire, trois de croche, un de croche pointée, une ouverture longue sur le temps 4.
  - GRID X 16, SMOOTH 5-15.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **Macros** : celles de W19.
- **Sub associé** : S10.
- **Origine** : outils de dessin du LFO [cartographie, § 7.2] ; séquence [ORIGINAL].

### WD15 Wobble aléatoire — LFO S&H
- **Patch** :
  - WD01, avec LFO 2 de type S&H (sample-and-hold), BPM, 1/8, RETRIG → CUTOFF ±30 %, en plus de LFO 1.
  - SMOOTH 20-40 pour adoucir les marches.
- **ENV 1** : comme WD01.
- **Macros** : `Vowel` profondeur de LFO 2 · les autres comme WD01.
- **Sub associé** : S01.
- **Test** : chaque passage du riff est différent. Si le groove se perd, réduire la profondeur de LFO 2 ou imprimer une prise réussie (WD20).
- **Origine** : TYPE S&H des LFO [cartographie, § 7.2] ; recette [ORIGINAL].

### WD16 Wobble chaotique — LFO Chaos: Lorenz
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0. FILTER 1 en MG Low 24, CUTOFF ≈ 250 Hz, RES 20 %.
  - LFO 1 de type Chaos: Lorenz → CUTOFF, plage 250 Hz-1 kHz, MONO, RATE lent.
- **ENV 1** : attaque 5 ms, sustain 100 %, release 200 ms.
- **FX** : Distortion Tube, Reverb Plate courte, passe-haut à 100 Hz.
- **Macros** : `Rate` RATE du LFO · `Depth` LFO 1 → CUTOFF · `Vowel` RES · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - types Chaos: Lorenz et Chaos: Rossler, qui remplacent les Chaos 1/2 de Serum 1 [cartographie, § 7.2, 9] ;
  - usage en deep dubstep [ORIGINAL].

### WD17 Wobble vocal — formant à 1/4
- **Patch** : W11 de `house-f07-wub.md` à 140 BPM : Formant-II, LFO 1 en 1/4 (428,6 ms) → CUTOFF.
  - Variante bégaiement : 1/8, faible profondeur.
- **ENV 1** : comme W11.
- **Macros** : celles de W11.
- **Sub associé** : S01.
- **Origine** : 1/4 « steady syllables », 1/8 « fast stutter » [SOURCE F08-04, infographie].

### WD18 Warping Bass 3/16 — à 140 BPM
- **Patch** : W08 de `house-f07-wub.md`, LFO 1 → CUTOFF de FILTER 1 en 1/8 pointée (= 3/16, 321,4 ms à 140 BPM), FILTER 1 vers FILTER 2 (Combs) en série.
- **ENV 1** : comme W08.
- **Macros** : celles de W08.
- **Sub associé** : S01.
- **Origine** : [SOURCE Attack Magazine, Warping Bass, `patches-genres.md`] ; durée [CALCUL].

### WD19 Wobble de l'arrangement — macros automatisées
- **Patch** : WD03 ou WD01, avec trois macros nommées comme sur la capture EDMProd :
  - **SHAPER** : drive du Sine Shaper et MIX inversé ; monte en pointe sur les fins de phrase ;
  - **CHAR.** : CUTOFF du peigne ; monte par paliers ;
  - **WOBBLE** : profondeur de LFO 1 ; bouge lentement.
- **Arrangement** : automatiser les trois macros sur la piste dans Live, plus un envoi de reverb de basse sans grave.
- **ENV 1** : comme la recette de départ.
- **Sub associé** : S01, non automatisé.
- **Test** : les automations doivent servir la phrase de 8 mesures ; une variation avant chaque frontière (règle des drops d'`AGENTS.md`).
- **Origine** :
  - macros SHAPER, CHAR. et WOBBLE automatisées sur la piste « Main Sub », envoi « C-Bass Verb » [SOURCE F01-08, capture] ;
  - « automation de la Macro 2 du sub à la mesure 60 pour un petit wobble » [SOURCE F15-06, page].

### WD20 Wobble ressamplé — deux ou trois passes
- **Patch** : W20 de `house-f07-wub.md` au tempo dubstep. Une note tenue de 2 à 4 mesures (3,4 à 6,9 s à 140 BPM), imprimée, remise dans un oscillateur, retravaillée avec une autre vitesse de LFO à chaque passe ; au plus 2-3 passes.
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01.
- **Origine** : [SOURCE F08-04, F02-14] ; durées [CALCUL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f07-wobble.md`.

```grille
titre: Dubstep 140 — tenues de lurch (WD01, WD06)
tempo: 140
accords: Em7 | Cmaj7
wob: E1[1:8] G1[3e:7] | C1[1:8] E1[3e:3] B0[4:4]
sub: E0[1:8] G0[3e:7] | C1[1:8] E0[3e:3] B0[4:4]
```

Une tenue d'une demi-mesure (857,1 ms) porte deux « lurch » à 1/4. La deuxième tenue part après la caisse claire.

```grille
titre: Dubstep 140 — wobble pointé (WD10, WD18)
tempo: 140
accords: Fm7 | Fm7
wob: F1[1:8] Ab1[3e:3] F1[4:4] | F1[1:8] C2[3e:3] Eb1[4:4]
sub: F0[1:8] Ab0[3e:3] F0[4:4] | F0[1:8] C1[3e:3] Eb0[4:4]
```

La 1/8 pointée (321,4 ms) se décale contre la noire : sur la tenue d'une demi-mesure, les wubs partent à 0, 321 et 643 ms, et la note s'arrête sur la caisse claire (857 ms) [CALCUL].

```grille
titre: Dubstep 140 — divisions enchaînées (WD05)
tempo: 140
accords: Gm7 | Gm7
wob: G1[1:16] | G1[1:6] Bb1[2&:2] D2[3e:3] G1[4:4]
sub: G0[1:16] | G0[1:6] Bb0[2&:2] D1[3e:3] G0[4:4]
```

Mesure 1 tenue (1/4 puis 1/8 par la macro `Rate`), mesure 2 hachée (1/16 sur la dernière note). Ce bloc correspond aux deux dernières mesures d'une phrase de build.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les types de LFO S&H et Chaos: Lorenz ;
  - la bascule TRIP ;
  - le filtre Cmb HL6+ ;
  - la table BSOD_Square.

  Vérifier les destinations des macros.
- Regarder sur le Mac les tutoriels deep dubstep et chillstep du registre (F07-17 à F07-20) pour confirmer WD04 et WD06.
- Écouter chaque recette avec le sub, le kick et la caisse claire à 140 BPM, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
