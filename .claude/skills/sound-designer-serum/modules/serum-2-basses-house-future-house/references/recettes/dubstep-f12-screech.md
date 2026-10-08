# Vingt recettes de screech pour le Dubstep (famille F12)

Sixième lot Dubstep : le screech dans son genre d'origine. En dubstep, il peut tenir le drop, et pas seulement l'accent, d'où ce lot, joué à 140 BPM en half-time et parfois grave (autour de Fa0 dans F12-02). `house-f12-screech.md` traite le screech comme accent House ; les recettes identiques y renvoient. Celles-ci ajoutent ce qui est propre au dubstep : registre grave avec sub séparé, pitch bend qui crie, montée avant le drop, superposition avec un growl. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F12-02 EDMProd (« 43 Semitone Trick »), F12-01 Rocket Powered Sound, F11-01 ;
- `../etudes-pages-dubstep-dnb.md` : F08-04 ;
- la fiche 10 de `../families.md` et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL]. Deux études seulement portent sur le screech : la part de [ORIGINAL] est grande.

## Règles

1. **Règles communes du lot Dubstep** : celles de `dubstep-f10-riddim.md`. **Règles du screech** : celles de `house-f12-screech.md` :
   - haut-médium de 1 à 5 kHz contrôlé à faible volume ;
   - distorsion après le filtre ;
   - glide sur cette couche seulement ;
   - rapports FM +19, +31 et +43 demi-tons ≈ 3, 6 et 12:1.
2. **Screech grave** : F12-02 joue autour de Fa0 (« registre grave pour garder la fondamentale ») avec un sub sinus hors filtre, phase alignée, niveau suivant LFO 1.
   - Ici, ce sub est sur sa piste : S01 de `house-f01-sub.md`, recalé à 140 BPM.
   - Le screech garde un passe-haut juste sous sa première harmonique utile (120-200 Hz).
3. **Quatre macros communes**, celles de la fiche 10 de `../families.md` : `Scream`, `Rasp`, `Fall`, `Space`. Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| SD01 | 43 demi-tons au tempo d'origine | référence, drop | FM 12:1, High 24 |
| SD02 | Screech FM Virtual Riot en drop | drop | scies unison 16, FM +3 octaves |
| SD03 | Pseudo-sidechain par LFO | drop | LFO Envelope 1/2 pointée |
| SD04 | High 24 résonant | screech grave | pic dans le bas-médium |
| SD05 | Croquant sur les côtés | drop large | Chorus HPF puis SoftClip |
| SD06 | Pitch bend qui crie | fin de note | bend +12 vers le haut |
| SD07 | Montée avant le drop | build | macro sur CRS et CUTOFF |
| SD08 | Rafales | gun screech | ENV 1 courte |
| SD09 | Screech sur growl | drop épais | deux couches séparées en fréquence |
| SD10 | Scream BP grave | drop | filtre Scream BP |
| SD11 | French LP | growl-screech | BOEUF |
| SD12 | Screech « ee » | voix | formant balayé à 1/4 |
| SD13 | Screech sync | drop | sync balayé |
| SD14 | Traitement parallèle | toutes | compression parallèle, sidechain kick + caisse |
| SD15 | Sans fondamentale | accent aigu | Odd/Even à 100 % |
| SD16 | Replié | drop agressif | Sine Fold, Rectify |
| SD17 | Phaser figé haut | métal | deux phasers immobiles |
| SD18 | Décalé | accent | Bode |
| SD19 | Spectral | texture | moteur Spectral |
| SD20 | Ressamplé | toutes | 2-3 passes |

## Les vingt recettes

### SD01 43 demi-tons au tempo d'origine — référence
- **Patch** : C02 de `house-f12-screech.md`, avec trois réglages d'origine.
  - OSC A à la hauteur de la source : notes autour de Fa0 (fa mineur), Fa#, Sol#.
  - LFO 1 en ENVELOPE, 1/2 pointée (1 285,7 ms à 140 BPM) → WT POS, WARP 1 et CUTOFF.
  - OSC B à +43 demi-tons (OCT +3, SEM +7), LEVEL 0, RAND 0.
- **ENV 1 (écran)** : 6,1 ms / 0 / 1,00 s / 0 dB / 15 ms.
- **FX, dans l'ordre vu à l'écran** :
  1. Hyper/Dimension, 3 voix.
  2. Equalizer.
  3. Chorus HPF.
  4. Distortion SoftClip.
  5. Compressor Multiband.
  6. Reverb Plate.
  7. Passe-haut à 120 Hz ajouté [ORIGINAL].
- **Macros** : celles de C02.
- **Sub associé** : S01 sur sa piste, phase alignée (RAND 0 et PHASE 0 % des deux côtés).
- **Jeu** : bloc « Dubstep 140 — screech grave en fa » ci-dessous.
- **Origine** : [SOURCE F12-02, transcription et trois captures, Serum 1] ; durée [CALCUL].

### SD02 Screech FM Virtual Riot en drop
- **Patch** : C03 de `house-f12-screech.md` (A scie unison 16 FM (B), B scie OCT +3 unison 16, LFO 2 → FM 69, Diode 1), joué une octave plus bas que le lead d'origine, avec un passe-haut à 200 Hz.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **Macros** : celles de C03.
- **Sub associé** : S01.
- **Test** : 16 voix d'unison sur deux oscillateurs : vérifier le mono et le CPU. Hyper au lieu de l'unison, si besoin (R16 de `house-f02-reese.md`).
- **Origine** : [SOURCE F12-01, captures, Serum 1] ; la description dit que c'est un lead : ici abaissé en screech de drop [ORIGINAL].

### SD03 Pseudo-sidechain par LFO
- **Patch** :
  - OSC A sur une table riche, OCT −1, RAND 0.
  - LFO 1 en mode ENVELOPE, 1/2 pointée : montée rapide courbée puis lente descente (« pseudo-sidechain »), → WT POS (quantité réduite) et → LEVEL d'A.
  - Le son s'ouvre après l'attaque comme s'il sortait d'un sidechain.
  - FILTER 1 en Band 12, CUTOFF 1,5 kHz, RES 30 %.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion SoftClip, Compressor Multiband, passe-haut à 150 Hz.
- **Macros** : `Scream` CUTOFF · `Rasp` DRIVE · `Fall` PORTA · `Space` MIX d'une Reverb Plate.
- **Sub associé** : S01.
- **Origine** : LFO 1 en mode Envelope, 1/2 pointée, « pseudo-sidechain », sur la position de A [SOURCE F12-02] ; LFO → LEVEL [ORIGINAL].

### SD04 High 24 résonant — le pic dans le bas-médium
- **Patch** :
  - OSC A sur une table riche, OCT −1, RAND 0.
  - FILTER 1 en High 24 sur A seul : DRIVE, CUTOFF bas, FAT monté, RES en pic dans le bas-médium (200-500 Hz).
  - LFO 1 (1/2 pointée, ENVELOPE) → CUTOFF. Pas de key track : le son reste plus constant.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion SoftClip, Equalizer (grave remonté au-dessus du passe-haut), Compressor Multiband.
- **Macros** : `Scream` RES · `Rasp` VAR (FAT) · `Fall` PORTA · `Space` —.
- **Sub associé** : S01. Le passe-haut du filtre laisse le sub seul en dessous.
- **Origine** : filtre High 24 sur A seul, drive, coupure basse, FAT, résonance en pic dans le bas-médium, LFO 1 sur la coupure, pas de key tracking [SOURCE F12-02].

### SD05 Croquant sur les côtés — Chorus HPF puis SoftClip
- **Patch** : SD01 ou SD04, avec l'ordre des effets choisi exprès :
  1. Hyper/Dimension (3 voix, DETUNE bas, MIX bas).
  2. Chorus en mode HPF (MIX et DEPTH bas).
  3. Distortion SoftClip, bon drive.
  4. Compressor Multiband.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Rasp` DRIVE de la SoftClip · `Space` MIX du Chorus · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Test** : A/B avec la distorsion avant le Chorus, à niveau égal : les côtés doivent paraître plus croquants dans l'ordre de la source.
- **Origine** : « distordre après l'élargissement donne du croquant sur les côtés » [SOURCE F12-02].

### SD06 Pitch bend qui crie — vers le haut
- **Patch** : SD01, SD02 ou SD04, avec pitch bend UP +12.
  - Dans le clip de Live, dessiner un bend de 0 à +12 sur la seconde moitié de la dernière note.
  - Ou bien ENV 3 → CRS, +12, attaque 300-600 ms, sur la note voulue.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 150 ms.
- **Macros** : `Fall` ENV 3 → CRS 0 → +12 · les autres comme la recette de départ.
- **Sub associé** : S01, sans bend ; couper le sub sur la note qui crie.
- **Origine** :
  - pitch bend ±12 [SOURCE BassGorilla, `basses.md` § 3, fiabilité faible] ;
  - bend dessiné dans l'enveloppe de clip de Live [SOURCE F05-12] ;
  - bend vers le haut [ORIGINAL].

### SD07 Montée avant le drop — CRS et CUTOFF
- **Patch** : SD01 ou C01, plus MACRO 5 « Rise » sur deux destinations :
  - CRS d'OSC A et d'OSC B, de 0 à +12 ;
  - CUTOFF du filtre principal, +2 octaves.
- **Arrangement** : automatiser MACRO 5 de 0 à 100 % sur les deux dernières mesures du build (3 428,6 ms à 140 BPM), puis la remettre à 0 sur le temps 1 du drop.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 100 ms.
- **Macros** : `Scream`, `Rasp`, `Fall`, `Space` comme la recette de départ, plus MACRO 5 « Rise ».
- **Sub associé** : aucun pendant la montée.
- **Origine** : macros et matrice [cartographie, § 7.3-7.4] ; geste [ORIGINAL] au service de la règle des drops d'`AGENTS.md`.

### SD08 Rafales — gun screech
- **Patch** : C15 de `house-f12-screech.md` : ENV 1 à attaque 0,5 ms, decay 116 ms, sustain −∞, release 52 ms ; le rythme vient des notes MIDI.
- **Macros** : celles de C15.
- **Sub associé** : aucun.
- **Jeu** : bloc « Dubstep 140 — rafales de screech » ci-dessous.
- **Origine** : « le machine gun vient de l'ENV 1 » [SOURCE F11-01].

### SD09 Screech sur growl — deux couches séparées en fréquence
- **Méthode** : deux instances de Serum sur deux pistes, plus le sub.
  - **Growl** (GD01 de `dubstep-f08-growl.md`) : passe-bas à 1 kHz en fin de chaîne.
  - **Screech** (SD01 ou SD04) : passe-haut à 1 kHz.
  - Les deux jouent la même ligne MIDI, ou le screech ne joue que les fins de phrase.
  - Sub S01 en dessous.
- **Macros** : celles de chaque couche.
- **Test** :
  - couper chaque couche à tour de rôle : aucune ne doit masquer l'autre vers 1 kHz ;
  - mono ;
  - faible volume.
- **Origine** : [ORIGINAL]. Le growl vit de 150 Hz à 2 kHz [SOURCE F08-04], le screech de 1 à 5 kHz (fiche 10 de `../families.md`).

### SD10 Scream BP grave — le filtre qui crie
- **Patch** : C04 de `house-f12-screech.md` (Scream BP, DRIVE au-dessus de 50 %), une octave plus bas, CUTOFF 600 Hz-1,2 kHz.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **Macros** : celles de C04.
- **Sub associé** : S01.
- **Origine** : Scream LP/BP [cartographie, § 6] ; registre [ORIGINAL].

### SD11 French LP — growl-screech
- **Patch** : C05 de `house-f12-screech.md` (French LP, BOEUF 30-60 %), joué en Fa1-Do2, LFO 1 → VAR à 1/4 (428,6 ms).
- **ENV 1** : comme C05.
- **Macros** : celles de C05.
- **Sub associé** : S01.
- **Origine** : French LP, VAR = BOEUF [cartographie, § 6] ; recette [ORIGINAL].

### SD12 Screech « ee » — formant à 1/4
- **Patch** : C06 de `house-f12-screech.md` (Formant-III, de « oo » vers « ee »), avec LFO 1 en RETRIG à 1/4 au lieu d'ENV 2.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **Macros** : celles de C06.
- **Sub associé** : S01.
- **Origine** : formants [SOURCE Synth Secrets 23] ; 1/4 « steady syllables » [SOURCE F08-04].

### SD13 Screech sync — balayage
- **Patch** : C09 de `house-f12-screech.md` (Sync balayé par ENV 2 et LFO 1), à 140 BPM, LFO 1 en 1/8 (214,3 ms).
- **ENV 1** : comme C09.
- **Macros** : celles de C09.
- **Sub associé** : aucun.
- **Origine** : Sync [cartographie, § 4.1] ; recette [ORIGINAL].

### SD14 Traitement parallèle — sidechain kick et caisse claire
- **Patch** : C20 de `house-f12-screech.md`, au tempo dubstep. Après Serum, avec des plug-ins tiers :
  - compression parallèle 4:1 rapide ;
  - EQ : creux 100-300 Hz, +2 dB vers 9 kHz, coupe-bas raide ;
  - sidechain rapide sur le kick **et** la caisse claire du temps 3.
- **Sub associé** : celui du drop.
- **Origine** : post-traitement de la source [SOURCE F12-02] ; plug-ins tiers (règle 6 d'`ableton-live-session`).

### SD15 Sans fondamentale — Odd/Even à 100 %
- **Patch** : C12 de `house-f12-screech.md`.
- **Origine** : [DÉDUCTION, cartographie § 4.1].

### SD16 Replié — Sine Fold et Rectify
- **Patch** : C13 de `house-f12-screech.md`, avec QUALITY sur Ultra et la note la plus aiguë vérifiée à part.
- **Origine** : [cartographie, § 4.2] ; Rectify [SOURCE F08-03].

### SD17 Phaser figé haut — métal
- **Patch** : C14 de `house-f12-screech.md` (deux phasers figés à 2 et 3,2 kHz, FEEDBACK 50-70 %).
- **Origine** : phasers figés [SOURCE F08-01].

### SD18 Décalé — Bode
- **Patch** : C16 de `house-f12-screech.md` (Bode, SHIFT +10 à +60 Hz, LFO 2 à 1/2 = 857,1 ms).
- **Origine** : [cartographie, § 8 ; DÉDUCTION].

### SD19 Spectral — texture
- **Patch** : C19 de `house-f12-screech.md`.
- **Origine** : [DÉDUCTION, cartographie § 3.6, 4.3].

### SD20 Ressamplé — deux ou trois passes
- **Patch** :
  1. Construire SD01 ou SD04.
  2. Imprimer une note tenue de 2 à 4 mesures (3,4 à 6,9 s à 140 BPM).
  3. La remettre dans un oscillateur et la retravailler, avec un autre rythme de LFO à chaque passe ; au plus 2-3 passes.
- **Sub associé** : S01.
- **Origine** : [SOURCE F08-04] ; procédure : `../../../resampling/GUIDE.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f12-screech.md`.

```grille
titre: Dubstep 140 — screech grave en fa (SD01, SD04)
tempo: 140
accords: Fm7 | Fm7
screech: F1[1:6] Gb1![2&:2] Ab1[3e:3] F1[4:4] | F1[1:6] Ab1[2&:2] Eb1[3e:3] F1[4:4]
sub: F0[1:6] F0[2&:2] Ab0[3e:3] F0[4:4] | F0[1:6] Ab0[2&:2] Eb0[3e:3] F0[4:4]
```

Notes autour du fa, comme F12-02 (F, F#, G#) ; le sol bémol est le demi-ton voulu, marqué « ! ». La couche screech joue une octave au-dessus du sub (Fa1), avec son passe-haut.

```grille
titre: Dubstep 140 — rafales de screech (SD08)
tempo: 140
accords: Em7 | Em7
gun: E2[1:1] E2[1e:1] E2[1&:1] G2[2:1] E2[2&:1] E2[2a:1] B2[3e:1] E2[4:1] E2[4e:1] D3[4&:2] | E2[1:1] E2[1e:1] E2[1&:1] G2[2:1] E2[2&:1] E2[2a:1] D2[3e:1] E2[4:1] B2[4e:1] E3[4&:2]
```

Rafales qui laissent libre la caisse claire du temps 3.

```grille
titre: Dubstep 140 — montée avant le drop (SD07)
tempo: 140
accords: Gm7 | Gm7
rise: G2[1:16] | G2[1:8] Bb2[3:4] D3[4:4]
```

Deux mesures de build : la macro « Rise » monte de 0 à 100 % sur ces deux mesures. Le drop commence sur le temps 1 suivant, macro remise à 0.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : la table « Groan II » (Massive importée), le filtre High 24, les filtres Scream BP et French LP, l'étendue du pitch bend. Vérifier les destinations des macros.
- Regarder sur le Mac les vidéos screech du registre (F12-03 à F12-05).
- Écouter chaque recette avec le sub, le kick et la caisse claire, à faible volume puis dans le drop, et en garder deux à quatre. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
