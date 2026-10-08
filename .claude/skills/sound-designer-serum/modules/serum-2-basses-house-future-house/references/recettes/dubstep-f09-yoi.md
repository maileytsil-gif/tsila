# Vingt recettes de yoi pour le Dubstep (famille F09)

Deuxième lot Dubstep : le yoi, une basse dont chaque note dit « yoi ». Une voyelle glisse du grave vers l'aigu (« oo » vers « ee »), en général à la noire ou au triolet. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F09-01 DraGonis, la seule étude yoi ; pour les gestes voisins, F08-01 et F10-01 ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` : F08-04 Monosounds ;
- la talking bass du corpus `../../../../../producteur-live/modules/house-future-rave-bass-house-production/recipes/talking-bass-formants.md` ;
- `../documentation-basses.md` § 2 (formants) et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL]. Une seule vidéo yoi est étudiée, et c'est un « speedrun » de 1:47 : la part de [ORIGINAL] et de [DÉDUCTION] est grande, et chaque fiche le dit.

## Règles

1. **Règles communes du lot Dubstep** : celles de `dubstep-f10-riddim.md`. Elles couvrent le tempo (140 BPM en half-time), les durées, le sub séparé, l'OCT −3 des tutoriels, RAND 0 et les effets après Serum.
2. **Le mot « yoi »** : glissement du formant F2 du grave vers l'aigu, de l'ordre de « oo » (870 Hz) vers « ee » (2 300 Hz) [DÉDUCTION, `../documentation-basses.md` § 2].
   - Les voyelles du tableau sont anglaises.
   - Un formant fixe ne suit pas la note : lire la voyelle sur la note la plus jouée.
3. **Rythme** : « 1/4 triplet : the yoi-yoi bounce », sur WT POS [SOURCE F08-04, infographie]. 1/4 triolet = 285,7 ms à 140 BPM [CALCUL]. Les LFO sont redéclenchés (RETRIG ou ENVELOPE).
4. **Quatre macros communes** :
   - `Yoi` : amplitude du glissement de voyelle ;
   - `Mouth` : WT POS ou point de départ de la voyelle ;
   - `Rate` : RATE du LFO principal ; DraGonis met le rate du LFO sur une macro ;
   - `Grit` : drive.

   Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| Y01 | Yoi DraGonis | référence | Monster 5, FM (B), HP 12 à deux fréquences opposées |
| Y02 | Yoi au formant | yoi lisible | Formant de « oo » vers « ee » |
| Y03 | Deux pics qui se croisent | yoi nasal | filtre HP (High + Peak) |
| Y04 | Yoi-yoi en triolets | rebond | WT POS en 1/4 triolet |
| Y05 | Yoi table de voyelles | yoi simple | catégorie Vowel |
| Y06 | Yoi de sa propre voix | yoi humain | WAV « yah-woh-yoi » |
| Y07 | Yoi FM | yoi râpeux | quantité de FM en bosse |
| Y08 | Yoi à deux passe-bandes | yoi précis | F1 et F2 séparés |
| Y09 | Yoi à deux vitesses | yoi mâché | Bend − à 1/2 en plus |
| Y10 | Yoi à vitesse par macro | build | macro sur le RATE |
| Y11 | Yoi midtempo | midtempo 100 BPM | même geste, plus lent |
| Y12 | Yoi au coupe-bas mobile | yoi creusé | EQ modulé |
| Y13 | Yoi au phaser | yoi métallique | FREQ du phaser balayée |
| Y14 | Yoi en Path | yoi animé | sorties X et Y |
| Y15 | Un yoi par note | réponse | LFO ENVELOPE, une syllabe |
| Y16 | Yoi spectral | yoi sans filtre | frames morphées |
| Y17 | Yoi au peigne | yoi accordé | peigne qui monte |
| Y18 | Yoi à l'enveloppe | yoi selon la longueur | ENV 2, pas de LFO |
| Y19 | Yoi large | refrain de drop | Hyper aux mix modulés |
| Y20 | Yoi ressamplé | toutes | 2-3 passes |

## Les vingt recettes

### Y01 Yoi DraGonis — référence
- **Patch** :
  - **OSC A** : table « Monster 5 [SL] » (Spectral), OCT −3, RAND 0.
  - **LFO 1** : bosse (montée arrondie puis descente), RETRIG, 1/4 → LEVEL d'A et → WT POS d'A.
  - **WARP 1 d'OSC A** en FM (B), quantité modulée par LFO 1.
  - **OSC B** : sinus « Analog_BD_Sin », LEVEL baissé, WARP en Bend −.
  - **LFO 2** : forme dessinée, 1/2 → Bend − de B.
  - **FILTER 1** en HP 12 (Multi HP : High + Peak) sur A seul, RES haute. LFO 1 → CUTOFF et → VAR (FREQ, le second bouton) en sens opposés : les deux fréquences vont « l'une vers l'autre ».
  - **Macro** : `Rate` sur le RATE de LFO 1.
- **ENV 1** : non dite. Attaque 1 ms, sustain 100 %, release 40 ms [ORIGINAL].
- **FX** :
  1. Hyper/Dimension, MIX modulés, SIZE baissée.
  2. Distortion Tube, filtre en LP à 330 Hz, Q 1,9 (écran).
  3. Compressor en Multiband.
  4. Equalizer, bande basse en coupe-bas, fréquence modulée par LFO 1.
- **Macros** : `Yoi` profondeur de LFO 1 → CUTOFF et VAR · `Mouth` WT POS de base · `Rate` RATE de LFO 1 · `Grit` DRIVE de la Tube.
- **Sub associé** : S01 de `house-f01-sub.md`, sur sa piste.
- **Jeu** : bloc « Dubstep 140 — yoi en noires » ci-dessous.
- **Origine** : [SOURCE F09-01, transcription courte et quatre captures, Serum 1, « pas un tutoriel, un speedrun »] ; les profondeurs ne sont pas lisibles.

### Y02 Yoi au formant — de « oo » vers « ee »
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - FILTER 1 en Formant-III (ou I), RES 25-35 %.
  - LFO 1 en ENVELOPE, 1/4, forme en rampe montante courbée → CUTOFF du formant. Régler les deux bornes à l'oreille : départ sur « oo », arrivée sur « ee ».
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Overdrive, puis Equalizer (passe-haut à 120 Hz, creux sur le pic nasal), puis Compressor Multiband.
- **Macros** : `Yoi` profondeur de LFO 1 · `Mouth` CUTOFF de base · `Rate` RATE de LFO 1 · `Grit` DRIVE.
- **Sub associé** : S01.
- **Test** : sur la note la plus jouée, les deux voyelles doivent se reconnaître. Ne pas balayer toute la course : ce serait une démo de filtre, pas une voix.
- **Origine** :
  - formants « oo » F2 870 Hz et « ee » F2 2 300 Hz [SOURCE Synth Secrets 23, `../documentation-basses.md` § 2] ;
  - « balayer toute la course donne une démo de filtre, pas une voix » [SOURCE talking bass du corpus] ;
  - recette [DÉDUCTION].

### Y03 Deux pics qui se croisent — filtre HP
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - FILTER 1 en HP 12 (Multi : High + Peak), RES 50-70 %.
  - CUTOFF de base ≈ 300 Hz, VAR (FREQ du Peak) ≈ 2 kHz.
  - LFO 1 (bosse, RETRIG, 1/4) → CUTOFF +1,5 octave et → VAR −1,5 octave : les pics se croisent au milieu de la note.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Tube, passe-haut à 120 Hz.
- **Macros** : `Yoi` profondeur des deux modulations ensemble · `Mouth` VAR de base · `Rate` · `Grit`.
- **Sub associé** : S01.
- **Origine** :
  - cutoff et FREQ du filtre HP 12 modulés en sens opposés [SOURCE F09-01] ;
  - Multi HP : VAR = FREQ, cutoff du second SVF [cartographie, § 6] ;
  - valeurs [ORIGINAL].

### Y04 Yoi-yoi en triolets
- **Patch** :
  - OSC A sur une table vocale ou spectrale, OCT −2, RAND 0.
  - LFO 1 en bosse, RETRIG, 1/4 TRIP → WT POS (+20 à +40 %).
  - LFO 2 en 1/8, faible → CUTOFF d'un Formant-I (RES 25 %).
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Overdrive, Phaser (RATE 1/2, FEEDBACK 60 %, MIX 50 %), passe-haut à 120 Hz.
- **Macros** : `Yoi` profondeur de LFO 1 · `Mouth` WT POS de base · `Rate` 1/4T → 1/8T · `Grit` DRIVE.
- **Sub associé** : S10, recalé à 140 BPM.
- **Jeu** : notes d'une blanche : trois « yoi » par blanche.
- **Origine** : 1/4 triolet sur WT POS ; 1/8 sur le formant ; Overdrive puis Phaser [SOURCE F08-04, page et infographie].

### Y05 Yoi table de voyelles
- **Patch** :
  - OSC A sur une table de la catégorie Vowel de Serum 2, OCT −2, RAND 0.
  - LFO 1 en ENVELOPE, 1/4, rampe montante → WT POS, de la frame « oo » à la frame « ee » de la table (à repérer en balayant).
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Diode 2 légère, passe-haut à 120 Hz.
- **Macros** : `Yoi` profondeur de LFO 1 · `Mouth` WT POS de départ · `Rate` · `Grit`.
- **Sub associé** : S01.
- **Origine** : table Vowel (« OOH_YAH_00 ») [SOURCE F10-01] ; WT POS comme couche vocale [SOURCE F08-04] ; recette [ORIGINAL].

### Y06 Yoi de sa propre voix
- **Patch** :
  1. Enregistrer « yoi » plusieurs fois, d'une voix stable en hauteur, et couper le WAV.
  2. Le déposer sur OSC A : Serum 2 en fait une wavetable.
  3. LFO 1 en ENVELOPE, 1/4 → WT POS : le mot enregistré défile à chaque note.
  4. Unison 1, OCT −1.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **FX** : chaîne de Y02.
- **Macros** : `Yoi` profondeur de LFO 1 → WT POS · `Mouth` WT POS de départ · `Rate` · `Grit`.
- **Sub associé** : S01.
- **Droits** : la voix de l'utilisateur ne pose pas de problème ; une voix tierce demande une licence.
- **Origine** :
  - enregistrer « yah-woh-yoi », déposer le WAV, une source à hauteur stable se convertit le mieux [SOURCE F08-04] ;
  - « les formants survivent » [SOURCE talking bass du corpus].

### Y07 Yoi FM — la quantité de FM en bosse
- **Patch** :
  - OSC A en sinus ou table douce, OCT −2, RAND 0.
  - OSC B en sinus, une octave sous A, LEVEL 0.
  - WARP 1 d'OSC A en FM (B), base 5 %. LFO 1 (bosse, RETRIG, 1/4) → WARP 1 +30 %.
  - FILTER 1 en Band 12, CUTOFF ≈ 800 Hz, LFO 1 → CUTOFF +1 octave.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Tube, passe-haut à 150 Hz (composante continue du modulateur grave).
- **Macros** : `Yoi` LFO 1 → WARP 1 · `Mouth` CUTOFF · `Rate` · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - FM (from B) modulé par LFO 1 [SOURCE F09-01] ;
  - FM 15-25 % = râpe gutturale [SOURCE F08-04] ;
  - recette [ORIGINAL].

### Y08 Yoi à deux passe-bandes — F1 et F2 séparés
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - FILTER 1 en Band 12 (F1) : CUTOFF 300 Hz, RES 30 %.
  - FILTER 2 en Band 12 (F2) : CUTOFF 870 Hz, RES 40 %.
  - Les deux en parallèle : A envoyé aux deux filtres, sorties Main.
  - LFO 1 (ENVELOPE, 1/4) → CUTOFF de FILTER 2, de 870 à 2 300 Hz (« oo » → « ee »).
  - LFO 1 → CUTOFF de FILTER 1, de 300 à 270 Hz (presque fixe).
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Overdrive légère, Equalizer (passe-haut à 150 Hz).
- **Macros** : `Yoi` LFO 1 → F2 · `Mouth` CUTOFF de base de F2 · `Rate` · `Grit`.
- **Sub associé** : S01.
- **Test** : couper FILTER 1 puis FILTER 2 pour entendre chaque formant seul.
- **Origine** :
  - « ou deux filtres Band 12 aux fréquences F1 et F2 » [SOURCE talking bass du corpus] ;
  - valeurs de formants [SOURCE Synth Secrets 23] ;
  - routage [ORIGINAL].

### Y09 Yoi à deux vitesses — Bend − en 1/2
- **Patch** : Y01 ou Y02, plus WARP 1 en Bend − et LFO 2 dessiné, RETRIG, 1/2 → quantité du Bend.
  - Le yoi principal à 1/4 et le mâchement à 1/2 se superposent.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Grit` profondeur de LFO 2 · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Origine** :
  - LFO 2 dessiné en 1/2 sur le Bend − de B [SOURCE F09-01] ;
  - 1/2 sur le warp, « half-time chew » [SOURCE F08-04, infographie].

### Y10 Yoi à vitesse par macro — build
- **Patch** : Y01 ou Y04, avec `Rate` sur le RATE de LFO 1, bornes de 1/2 à 1/16. Dans Live, automatiser la macro sur le build : 1/2, 1/4, 1/8, puis 1/16 sur la dernière mesure.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01, coupé sur la dernière demi-mesure du build.
- **Test** : au-delà de 1/16, on n'entend plus de la parole mais une texture [SOURCE F08-04, FAQ].
- **Origine** : rate du LFO piloté par une macro [SOURCE F09-01] ; séquence [ORIGINAL].

### Y11 Yoi midtempo — 100 BPM
- **Patch** : Y02 ou Y05, à 100 BPM, OCT −2, avec LFO 1 à 1/4 (600 ms à 100 BPM) et une forme plus longue (montée sur 60 % du cycle).
- **ENV 1** : attaque 3 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Overdrive, Compressor Multiband, Reverb Plate courte (MIX ≤ 8 %, LO CUT haut), passe-haut à 120 Hz.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01.
- **Jeu** : bloc « Midtempo 100 — yoi lent » ci-dessous.
- **Origine** : [ORIGINAL]. Le tutoriel midtempo « mouthy » du registre (F09-04 : Deathpact, Rezz) n'est pas étudié ; 600 ms [CALCUL].

### Y12 Yoi au coupe-bas mobile
- **Patch** :
  - Y01 sans le filtre HP.
  - Equalizer : bande basse en High Pass, FREQ de 150 Hz à 600 Hz sous LFO 1 (bosse, RETRIG, 1/4).
  - Le coupe-bas monte et creuse la note, puis redescend.
- **ENV 1** : comme Y01.
- **FX** : Equalizer en premier, puis Distortion Tube, puis Compressor Multiband.
- **Macros** : `Yoi` LFO 1 → FREQ de l'EQ · `Mouth` FREQ de base · `Rate` · `Grit`.
- **Sub associé** : S01. Le coupe-bas mobile ne touche pas le sub, qui est sur sa piste.
- **Origine** : EQ dont la fréquence de la bande basse (coupe-bas) est modulée par LFO 1 [SOURCE F09-01, écran] ; usage comme yoi principal [ORIGINAL].

### Y13 Yoi au phaser — métallique
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - Phaser figé : RATE au minimum, DEPTH 0, 4 pôles, FEEDBACK 60-75 %.
  - LFO 1 (ENVELOPE, 1/4) → FREQ du phaser, de 300 Hz à 2 kHz.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Overdrive avant le phaser, puis passe-haut à 120 Hz.
- **Macros** : `Yoi` LFO 1 → FREQ · `Mouth` FREQ de base · `Rate` · `Grit` FEEDBACK.
- **Sub associé** : S01.
- **Origine** :
  - phasers figés, seules fréquence et feedback, 4 pôles [SOURCE F08-01] ;
  - distorsion avant phaser [SOURCE F08-04] ;
  - balayage en yoi [ORIGINAL].

### Y14 Yoi en Path — deux mouvements d'un tracé
- **Patch** : Y02, avec LFO 1 de type Path, ENVELOPE, 1/4.
  - Tracé en arc : X → CUTOFF du formant, Y → WT POS.
  - La voyelle et la table bougent ensemble, mais pas au même rythme.
- **ENV 1** : comme Y02.
- **Macros** : `Yoi` profondeur de X · `Mouth` profondeur de Y · `Rate` · `Grit`.
- **Sub associé** : S01.
- **Origine** : type Path, sortie X et sortie Y séparée [cartographie, § 7.2] ; recette [ORIGINAL].

### Y15 Un yoi par note — LFO ENVELOPE
- **Patch** : Y02 ou Y05, avec LFO 1 en mode ENVELOPE (un seul cycle) au lieu de RETRIG.
  - Chaque note dit un seul « yoi », quelle que soit sa longueur.
  - Comparer avec RETRIG, qui répète « yoi-yoi » sur une note longue.
- **ENV 1** : attaque 1 ms, decay 400 ms, sustain −6 dB, release 60 ms.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S11.
- **Jeu** : notes courtes en réponse à la caisse claire.
- **Origine** : mode ENVELOPE, « comme RETRIG mais un seul cycle puis arrêt » [cartographie, § 7.2] ; usage [ORIGINAL].

### Y16 Yoi spectral — sans filtre formant
- **Patch** :
  - OSC A en moteur Spectral, sur une table vocale ou un sample de voix.
  - LFO 1 (ENVELOPE, 1/4) → WT POS : les frames morphent d'une voyelle à l'autre.
  - QUALITY sur High pendant la conception.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Overdrive, passe-haut à 150 Hz.
- **Macros** : `Yoi` profondeur de LFO 1 · `Mouth` WT POS de départ · `Rate` · `Grit`.
- **Sub associé** : S01.
- **Origine** : « morpher les frames au LFO = voyelle sans filtre formant » [SOURCE F08-04, section spectrale] ; recette [DÉDUCTION].

### Y17 Yoi au peigne — un yoi accordé
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - FILTER 1 en Cmb HL6+ ou Combs, key track allumé, CUTOFF à la hauteur de la note.
  - LFO 1 (ENVELOPE, 1/4) → CUTOFF, de 0 à +12 demi-tons : le pic du peigne glisse d'une octave.
  - VAR (HL WID ou DAMP) à l'oreille.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Diode 2, passe-haut à 120 Hz.
- **Macros** : `Yoi` profondeur de LFO 1 · `Mouth` VAR · `Rate` · `Grit` DRIVE.
- **Sub associé** : S01.
- **Test** : avec le key track, chaque note doit glisser de la même façon.
- **Origine** : peigne Cmb HL6− balayé par LFO dans le riddim [SOURCE F10-01] ; glissement en yoi [DÉDUCTION].

### Y18 Yoi à l'enveloppe — selon la longueur de la note
- **Patch** :
  - Y02 sans LFO.
  - ENV 2 → CUTOFF du formant : attaque 80-250 ms (le « o » qui monte vers le « i »), decay 300 ms, sustain 60 %.
  - Une note courte ne dit que « yo », une note longue dit « yoi ».
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **Macros** : `Yoi` ENV 2 → CUTOFF · `Mouth` CUTOFF de base · `Rate` attaque d'ENV 2 · `Grit`.
- **Sub associé** : S01.
- **Origine** : enveloppe sur la coupure du formant, « LFO lent ou enveloppe » [SOURCE F08-04] ; geste [ORIGINAL].

### Y19 Yoi large — Hyper aux mix modulés
- **Patch** : Y01, avec Hyper/Dimension en fin de chaîne : SIZE baissée, MIX de l'Hyper et MIX de la Dimension modulés par LFO 1 (+20 %).
  - La largeur s'ouvre avec le « yoi ».
  - Utility, MONO BASS à 150 Hz.
- **ENV 1** : comme Y01.
- **Macros** : `Grit` MIX de l'Hyper · les autres comme Y01.
- **Sub associé** : S01.
- **Test** : en mono, le yoi doit rester lisible.
- **Origine** : Hyper/Dimension, mixes modulés, taille baissée [SOURCE F09-01] ; Utility MONO BASS [cartographie, § 8].

### Y20 Yoi ressamplé — deux ou trois passes
- **Patch** :
  1. Construire Y01, Y02 ou Y06.
  2. Imprimer une note tenue de 2 à 4 mesures, effets compris.
  3. La remettre dans un oscillateur (glisser le WAV ou Resample to).
  4. Nouveau formant, nouvelle vitesse de LFO à chaque passe.
  5. S'arrêter après 2 ou 3 passes.
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01, jamais ressamplé avec le yoi.
- **Origine** : boucle de resampling [SOURCE F08-04] ; procédure : `../../../resampling/GUIDE.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f09-yoi.md`.

```grille
titre: Dubstep 140 — yoi en noires (Y01, Y02, Y05)
tempo: 140
accords: Em7 | Em7
yoi: E1[1:4] E1[2:4] G1[3e:3] E1[4:4] | E1[1:4] D1[2:4] B0[3e:3] E1[4:4]
sub: E0[1:4] E0[2:4] G0[3e:3] E0[4:4] | E0[1:4] D0[2:4] B0[3e:3] E0[4:4]
```

Un « yoi » par noire (LFO à 1/4 redéclenché). La note du temps 3 attend une double croche, pour laisser passer la caisse claire.

```grille
titre: Dubstep 140 — yoi-yoi en blanches (Y04, Y09)
tempo: 140
accords: Fm7 | Fm7
yoi: F1[1:8] Ab1[3e:7] | F1[1:8] Eb1[3e:7]
sub: F0[1:8] Ab0[3e:7] | F0[1:8] Eb0[3e:7]
```

Avec le LFO à 1/4 triolet (285,7 ms), une blanche (857,1 ms) porte trois « yoi » [CALCUL].

```grille
titre: Midtempo 100 — yoi lent (Y11)
tempo: 100
accords: Gm7 | Gm7
yoi: G1[1:3] G1[1a:1] Bb1[2&:2] G1[3:4] D2[4&:2] | G1[1:3] G1[1a:1] F1[2&:2] G1[3:4] Bb1[4&:2]
sub: G0[1:4] Bb0[2&:2] G0[3:4] D1[4&:2] | G0[1:4] F0[2&:2] G0[3:4] Bb0[4&:2]
```

À 100 BPM, une noire dure 600 ms : le yoi a le temps de s'ouvrir complètement.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : les tables « Monster 5 [SL] » et « Analog_BD_Sin », la catégorie Vowel, le filtre HP 12 (Multi), le Formant-III, le LFO de type Path. Vérifier les destinations des macros.
- Lire sur le Mac la page Futureproof (F09-02) et regarder F09-03 et F09-04 pour confirmer ou corriger ce lot.
- Écouter chaque recette avec le sub, le kick et la caisse claire, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
