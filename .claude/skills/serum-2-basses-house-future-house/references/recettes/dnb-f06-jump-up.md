# Vingt recettes de jump-up pour la Drum and Bass (famille F06)

Cinquième lot DnB : le jump-up, une basse médium courte, rebondissante et souvent « wobblée » à la croche, qui joue en appels et réponses avec le break. Ce fichier part de la seule étude jump-up du registre (F06-01) et des donks de `house-f06-donk-bouncy.md`, ramenés à 174 BPM. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F06-01 Antidote Audio (Serum 2, DnB), F06-02 Slynk (donk, Serum 1) ;
- `../etudes-pages-dubstep-dnb.md` : F06-14 Samstone (résumé d'agrégateur, sans valeurs) ;
- `house-f06-donk-bouncy.md` (recettes D01-D20) et `dnb-f14-hoover-foghorn.md` (stabs) ;
- `../documentation-basses.md` § 1 (FM) et la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot DnB** : celles de `dnb-f13-neuro.md` (174 BPM, schéma 2-step, sub séparé, octaves, RAND, MONO, resampling, contrôle).
2. **Le knock et le wobble ne touchent pas le sub.** Excursion de hauteur, FM brève, LFO de niveau et distorsion restent dans la couche médium ; le sub ne suit que les fondamentales, sans excursion (règle 1 de `house-f06-donk-bouncy.md`). La source met un SUB à −2 octaves dans le patch [SOURCE F06-01] ; ici, il passe sur sa piste.
3. **Le rebond vient d'un LFO redéclenché** sur le niveau des oscillateurs, à 1/8 [SOURCE F06-01]. Durées à 174 BPM [CALCUL] :
   - 1/4 = 344,8 ms : un rebond par temps ;
   - 1/8 = 172,4 ms : deux rebonds par temps ;
   - 1/8 triolet = 114,9 ms : trois par temps ;
   - 1/16 = 86,2 ms : quatre par temps.

   Sur une note de trois doubles croches (259 ms), un LFO à 1/8 fait 1,5 cycle : la note s'arrête au milieu d'un rebond [CALCUL].
4. **Rapports FM** : ceux de la règle 3 de `house-f06-donk-bouncy.md` (2:1 harmonique, 1:8 creux, 1,41 métallique).
5. **Quatre macros communes** [ORIGINAL], d'après celles des donks :
   - `Rate` : RATE du LFO de rebond ;
   - `Metal` : quantité de FM ou de résonance ;
   - `Body` : decay d'ENV 1 ou niveau du rebond ;
   - `Tone` : coupure du filtre.

   Vérifier le « + » sur chaque destination.
6. **Contrôle propre au jump-up** : le knock ne doit pas doubler l'attaque du kick ; écouter le rebond avec la caisse claire, qu'il ne doit pas masquer.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| JU01 | Jump-up Antidote | référence | Squibble, FM (B) 21 %, Flg L6+, LFO 1/8 sur les niveaux |
| JU02 | Jump-up à la noire | rebond lent | LFO 1/4 |
| JU03 | Jump-up en rafale | rebond serré | LFO 1/16 |
| JU04 | Jump-up en triolets | rebond chaloupé | LFO 1/8 triolet |
| JU05 | Jump-up FM 1:8 | knock métallique | modulateur trois octaves au-dessus, ENV 1 sur la FM |
| JU06 | Donk jump-up | appels | hauteur +12 brève, FM 2:1 brève |
| JU07 | Stab foghorn | ponctuation | foghorn court de `dnb-f14-hoover-foghorn.md` |
| JU08 | Jump-up qui plonge | réponse | chute de hauteur sur chaque note |
| JU09 | Jump-up multicouche | drop chargé | deux instances : FM résonante et peigne |
| JU10 | Jump-up au peigne | knock creux | Combs, transitoire de bruit |
| JU11 | Jump-up à rebond dessiné | « wub-wub » | deux bosses par temps dans le LFO |
| JU12 | Appel et réponse | drop | JU06 en appel, JU01 en réponse |
| JU13 | Jump-up à vélocité | jeu dynamique | vélocité vers le knock et la FM |
| JU14 | Jump-up Odd/Even | octave d'attaque | Odd/Even bref |
| JU15 | Jump-up sync | « dwoink » | warp Sync balayé |
| JU16 | Jump-up ring mod | couleur radio | RM depuis un sinus |
| JU17 | Jump-up distordu par bandes | drop | Splitter L/M/H |
| JU18 | Jump-up « boing » en octaves | sauts d'octave | portamento court |
| JU19 | Jump-up imprimé et rejoué | toutes | resampling, chops |
| JU20 | Jump-up qui accélère | variation avant la frontière | LFO 1/8 → 1/16 → coupure |

## Les vingt recettes

### JU01 Jump-up Antidote — référence du fichier
- **Patch** :
  - **OSC A** : table Serum 2 Digital « Squibble », OCT −2, position de table choisie à l'oreille, RAND 0, PHASE ≈ 101 (dit ; l'écran affiche 180°).
  - **OSC B** : scie (Default Shapes), LEVEL 0 : source de FM. WARP de A en FM (B) : 21 % dit, 22 % à l'écran.
  - **OSC C** : table Serum 1 Digital « Harmonic Subtle », RAND 0, position 256 (tout en haut).
  - **LFO 1** : rampe montée-descente, 1/8, RETRIG → LEVEL de A (vers le bas) et de C.
  - **NOISE** : couleur White (nouvelle dans Serum 2), STEREO 100 ; LFO 2 séparé, 1/8 → niveau du bruit. Filtrer le bruit pour qu'il soit moins grave.
  - **FILTER 1** : Flg L6+ (flanger) ; boutons « vers midi » sauf le DRIVE ; RES ≈ 59 % ; CUTOFF 1 276 Hz pendant le réglage, 893 Hz à la fin ; key track essayé puis retiré ; MIX un peu baissé.
  - MONO. La source garde un SUB à −2 octaves ; **ici, SUB éteint**.
- **ENV 1** : non dite. Attaque 1 ms, decay 200 ms, sustain −6 dB, release 40 ms [ORIGINAL].
- **FX** :
  1. Distortion Tube, filtre de distorsion OFF (Freq 425, Q 1,0 affichés) ; un peu plus de DRIVE en fin de réglage.
  2. Compressor Multiband : −18,1 dB, 4:1, attaque 90,1, release ≈ 90,1, gain 10,7 dB, bandes à 120 et 2 500 Hz ; aigus remontés puis remis.
- **Macros** : `Rate` RATE de LFO 1 (1/4 → 1/16) · `Metal` quantité de FM (B) 10 → 40 % · `Body` profondeur de LFO 1 → LEVEL de A · `Tone` CUTOFF du Flg L6+.
- **Sub associé** : S01, notes longues sous le rebond.
- **Jeu** : bloc « DnB 174 — jump-up en croches bondissantes » ci-dessous.
- **Origine** : [SOURCE F06-01, Antidote Audio, transcription et cinq captures, Serum 2, extrait du pack « Radium » ; petits chiffres lus avec réserve]. D10 de `house-f06-donk-bouncy.md` en est la version à 128 BPM.

### JU02 Jump-up à la noire — rebond lent
- **Patch** : JU01, avec LFO 1 et LFO 2 à 1/4 (344,8 ms).
- **ENV 1** : decay 300 ms, sustain −6 dB.
- **Macros** : celles de JU01.
- **Sub associé** : S01.
- **Jeu** : notes de trois ou quatre doubles croches : un seul rebond par note.
- **Origine** : JU01 [SOURCE F06-01] ; division [ORIGINAL].

### JU03 Jump-up en rafale — LFO à la double croche
- **Patch** : JU01, avec LFO 1 à 1/16 (86,2 ms) ; profondeur sur LEVEL de A réduite de moitié.
- **ENV 1** : decay 150 ms, sustain −12 dB.
- **Macros** : celles de JU01.
- **Sub associé** : S01.
- **Test** : à 1/16, le rebond peut se confondre avec une distorsion ; comparer avec JU01 à niveau égal.
- **Origine** : [ORIGINAL] d'après JU01.

### JU04 Jump-up en triolets — rebond chaloupé
- **Patch** : JU01, avec LFO 1 à 1/8 triolet (114,9 ms), RETRIG.
- **Calcul** : trois rebonds par temps ; une note de deux doubles croches (172 ms) en porte 1,5 [CALCUL].
- **ENV 1** : comme JU01.
- **Macros** : celles de JU01.
- **Sub associé** : S01.
- **Origine** : [ORIGINAL] d'après JU01.

### JU05 Jump-up FM 1:8 — modulateur trois octaves au-dessus
- **Patch** : D02 de `house-f06-donk-bouncy.md` ramené à 174 BPM :
  - OSC A et OSC B en sinus (Basic Shapes) ; A à OCT +1, LEVEL 0 ; B à OCT −2, WARP FM (A) ;
  - ENV 1 → quantité de FM, pas trop haut ;
  - FILTER 1 : MG Low 24, RES 0, un peu de DRIVE, ENV 1 → CUTOFF.
- **ENV 1** (écran de la source, à 128 BPM) : attaque ≈ 71 ms, decay ≈ 319 ms, sustain −∞, release ≈ 424 ms. À 174 BPM, pour garder la même proportion métrique : decay ≈ 235 ms, release ≈ 312 ms (× 128/174) [CALCUL] ; attaque ramenée à 1-5 ms pour un knock net [ORIGINAL].
- **Calcul** : A est trois octaves au-dessus de B, rapport 8:1 ; composantes à 1, 7, 9, 15, 17… × fc, un spectre creux [CALCUL].
- **FX** : Distortion en filtre passe-haut ≈ 200 Hz ; Compressor Multiband ; EQ en coupe-bas vers 170-180 Hz.
- **Macros** : `Rate` — · `Metal` quantité de FM · `Body` decay d'ENV 1 · `Tone` CUTOFF.
- **Sub associé** : S01.
- **Origine** : [SOURCE F06-02, Slynk, Serum 1, House] ; recalage au tempo d'après la règle de `../tempo-mix.md`.

### JU06 Donk jump-up — appels courts
- **Patch** : D01 de `house-f06-donk-bouncy.md` : excursion de hauteur brève (+12 ou +24 demi-tons), FM 2:1 brève, sustain 0.
- **ENV 1** : attaque 0,5 ms, decay 150 ms, sustain −∞, release 30 ms.
- **Macros** : `Rate` — · `Metal` quantité de FM · `Body` decay · `Tone` CUTOFF.
- **Sub associé** : S01, sans excursion.
- **Jeu** : mesure 1 du bloc « DnB 174 — jump-up en appel et réponse » ci-dessous.
- **Origine** : D01 de `house-f06-donk-bouncy.md` ; decay raccourci pour 174 BPM [ORIGINAL].

### JU07 Stab foghorn — ponctuation
- **Patch** : HF15 de `dnb-f14-hoover-foghorn.md` (HF01 ou HF03 avec ENV 1 courte).
- **ENV 1** : attaque 0,5 ms, decay 150 ms, sustain −∞, release 30 ms.
- **Macros** : celles du foghorn (`FM`, `Open`, `Grit`, `Width`).
- **Sub associé** : S01.
- **Jeu** : une note tous les deux temps, sur les contretemps, entre les phrases de JU01.
- **Origine** : foghorns façon Bou [SOURCE F14-01, F14-02] ; usage en stab [ORIGINAL].

### JU08 Jump-up qui plonge — chute de hauteur sur chaque note
- **Patch** : JU01, avec ENV 3 → CRS de A et de C, départ 0, chute de −5 demi-tons en 150 ms, sustain −5 demi-tons [ORIGINAL].
- **ENV 1** : comme JU01.
- **Macros** : `Body` profondeur de la chute (0 → −12 demi-tons) · les autres comme JU01.
- **Sub associé** : S01, **sans** chute.
- **Test** : sur une ligne rapide, la chute peut brouiller la note suivante ; l'essayer sur les fins de phrase seulement.
- **Origine** : [ORIGINAL]. Vérifier dans l'interface que CRS de A et C accepte une modulation ; sinon, ENV 3 → Global › Main Tuning.

### JU09 Jump-up multicouche — FM résonante et peigne
- **Patch** : deux instances de Serum sur deux pistes, même clip MIDI :
  - couche 1 : JU05 (FM et filtre résonant), passe-haut à 150 Hz ;
  - couche 2 : JU10 (peigne et phaser), passe-haut à 400 Hz, niveau −6 dB.
- **ENV 1** : celles des couches.
- **Macros** : par couche ; un Instrument Rack de Live peut regrouper les deux `Metal` sur une seule macro.
- **Sub associé** : S01, troisième piste.
- **Origine** : « basse multicouche, FM et filtres résonants », phaser et comb cités par l'index de l'agrégateur [EXTRAIT F06-14, Samstone, sans valeur] ; couches et niveaux [ORIGINAL].

### JU10 Jump-up au peigne — knock creux
- **Patch** : D04 de `house-f06-donk-bouncy.md` : FILTER 1 en Combs, transitoire de NOISE court à l'attaque ; ENV 1 brève.
- **ENV 1** : attaque 0,5 ms, decay 180 ms, sustain −∞, release 30 ms.
- **Macros** : `Rate` — · `Metal` CUTOFF du peigne · `Body` decay · `Tone` passe-bas final.
- **Sub associé** : S01.
- **Origine** : Comb, « son préféré, surtout avec attaque » ; noise court en transitoire d'attaque [SOURCE F06-02] ; D04 de `house-f06-donk-bouncy.md`.

### JU11 Jump-up à rebond dessiné — deux bosses par temps
- **Patch** : JU01, avec LFO 1 réglé à 1/4 et dessiné en deux bosses inégales (la seconde plus basse) : deux rebonds par temps, le second plus faible.
- **ENV 1** : comme JU01.
- **Macros** : `Rate` RATE de LFO 1 · les autres comme JU01.
- **Sub associé** : S01.
- **Origine** : [ORIGINAL] d'après JU01 ; dessin de LFO [cartographie, § 7.2].

### JU12 Appel et réponse — deux patchs, deux pistes
- **Patch** : JU06 sur une piste (appel), JU01 sur une autre (réponse) ; un seul sub pour les deux.
- **Jeu** : bloc « DnB 174 — jump-up en appel et réponse » ci-dessous : mesure 1 sur la piste de JU06, mesure 2 sur la piste de JU01. Couper les deux clips en deux dans Live.
- **Macros** : celles de chaque patch.
- **Sub associé** : S01, continu.
- **Origine** : [ORIGINAL] ; jeu en appel et réponse de `../motifs.md` (growl en réponse).

### JU13 Jump-up à vélocité — jeu dynamique
- **Patch** : JU01 ou JU06, avec Velo → quantité de FM (+30 %) et Velo → decay d'ENV 1 (+20 %).
- **ENV 1** : comme la recette de départ.
- **Jeu** : vélocités 127 sur les appels, 90 sur les notes de remplissage.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01, sans vélocité (niveau constant).
- **Origine** : D11 de `house-f06-donk-bouncy.md` [ORIGINAL].

### JU14 Jump-up Odd/Even — octave d'attaque
- **Patch** : JU06 avec WARP Odd/Even sur A ; ENV 2 (decay 60 ms) → quantité, de 100 % (paires seules, effet d'octave) vers 50 % (son d'origine).
- **ENV 1** : comme JU06.
- **Macros** : `Metal` quantité d'ENV 2 → Odd/Even · les autres comme JU06.
- **Sub associé** : S01.
- **Origine** : D14 de `house-f06-donk-bouncy.md` ; Odd/Even [cartographie, § 4.1].

### JU15 Jump-up sync — « dwoink »
- **Patch** : JU06 avec WARP Sync sur A ; ENV 2 (decay 120 ms) → quantité de Sync.
- **ENV 1** : comme JU06.
- **Macros** : `Metal` quantité d'ENV 2 → Sync · les autres comme JU06.
- **Sub associé** : S01.
- **Origine** : D15 de `house-f06-donk-bouncy.md` ; Sync [cartographie, § 4.1].

### JU16 Jump-up ring mod — couleur radio
- **Patch** : JU06 avec WARP RM (B) sur A, B en sinus à un rapport non entier (1,41).
- **ENV 1** : comme JU06.
- **Macros** : `Metal` quantité de RM · les autres comme JU06.
- **Sub associé** : S01, indispensable : la RM retire la fondamentale.
- **Origine** : D18 de `house-f06-donk-bouncy.md`.

### JU17 Jump-up distordu par bandes — grave propre
- **Patch** : JU01, puis un Splitter L/M/H : LOWS sans effet ; MIDS Distortion Tube ; HIGHS Distortion Soft Clip et Hyper/Dimension léger.
- **ENV 1** : comme JU01.
- **Macros** : `Tone` fréquence de séparation basse (150 → 400 Hz) · les autres comme JU01.
- **Sub associé** : S01.
- **Origine** : distorsion seulement au-dessus du grave [SOURCE F01-01, F13-02] ; JU01 [SOURCE F06-01] ; découpe [ORIGINAL].

### JU18 Jump-up « boing » en octaves — portamento court
- **Patch** : JU06, MONO + LEGATO, PORTAMENTO 30 ms, SCALED allumé.
- **Calcul** : 30 ms font 0,35 double croche à 174 BPM : le glissé est un « boing », pas une montée [CALCUL].
- **ENV 1** : comme JU06.
- **Jeu** : sauts d'octave en chevauchement d'un quart de double croche.
- **Macros** : `Body` PORTA (10 → 60 ms) · les autres comme JU06.
- **Sub associé** : S01, sans saut d'octave.
- **Origine** : D12 de `house-f06-donk-bouncy.md` ; valeurs [ORIGINAL].

### JU19 Jump-up imprimé et rejoué — chops
- **Patch** :
  1. Imprimer 4 mesures de JU01 sur la ligne du bloc ci-dessous (procédure de `../../../resampling/SKILL.md`).
  2. Découper les rebonds dans un Simpler en mode Slice.
  3. Rejouer les tranches dans un nouvel ordre ; transposer certaines tranches.
- **Macros** : celles du Simpler.
- **Sub associé** : S01, joué par un clip MIDI séparé.
- **Origine** : D20 de `house-f06-donk-bouncy.md` ; Simpler en Slice (`../../../sampling-composition-avancee/references/simpler-synthese.md`).

### JU20 Jump-up qui accélère — variation avant la frontière
- **Patch** : JU01. Dans Live, sur la phrase de 8 mesures :
  - macro `Rate` à 1/8 pendant 7 mesures ;
  - 1/16 sur la mesure 8 ;
  - basse coupée au temps 3 de la mesure 8.
- **ENV 1** : comme JU01.
- **Macros** : celles de JU01.
- **Sub associé** : S01, coupé avec la basse.
- **Jeu** : bloc « DnB 174 — jump-up qui accélère » ci-dessous (mesures 7 et 8).
- **Test** : en mode HOST, le LFO saute pour rester calé sur la mesure quand la division change.
- **Origine** : règle des drops d'`AGENTS.md` ; séquence [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60), notes pour des oscillateurs à OCT 0. DnB à 174 BPM : kick sur les doubles croches 1 et 11, caisse claire sur 5 et 13 (règles communes de `dnb-f13-neuro.md`). Aucune attaque de basse sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dnb-f06-jump-up.md`.

```grille
titre: DnB 174 — jump-up en croches bondissantes (JU01, JU02, JU04)
tempo: 174
accords: Fm7 | Fm7
jump: F1[1:2] F1[1&:2] F1[2&:1] Ab1[2a:1] F1[3:2] F1[3&:1] C2[3a:1] Eb2[4e:1] F1[4&:2] | F1[1:2] F1[1&:2] F1[2&:1] Ab1[2a:1] F1[3:2] Bb1[3&:1] Ab1[3a:1] F1[4e:1] Eb1[4&:2]
sub: F0[1:4] F0[2&:2] F0[3:4] Eb0[4e:3] | F0[1:4] F0[2&:2] F0[3:4] Eb0[4e:3]
```

Notes de une ou deux doubles croches : avec LFO 1 à 1/8, chaque note de deux doubles croches porte un rebond complet. Le si bémol de la mesure 2 est une note de passage vers le la bémol.

```grille
titre: DnB 174 — jump-up en appel et réponse (JU06, JU12)
tempo: 174
accords: Fm7 | Fm7
jump: F1[1:1] F2[1&:1] F1[1a:1] C2[2e:1] Eb2[2&:1] F1[3:1] F1[3&:1] Ab1[3a:1] C2[4e:1] Eb2[4&:1] | F1[1:3] F1[1a:1] Ab1[2e:3] F1[3:3] Eb1[3a:1] C1[4e:3]
sub: F0[1:4] F0[2e:3] F0[3:4] C1[4e:3] | F0[1:4] Ab0[2e:3] F0[3:3] Eb0[3a:1] C1[4e:3]
```

Mesure 1 : appel en stabs d'une double croche (JU06). Mesure 2 : réponse en notes de trois doubles croches (JU01, LFO à 1/8).

```grille
titre: DnB 174 — jump-up qui accélère (JU20)
tempo: 174
accords: Fm7 | Fm7
jump: F1[1:2] F1[1&:2] Ab1[2e:2] F1[2a:1] F1[3:2] C2[3&:2] Eb2[4e:2] | F1[1:1] F1[1e:1] F1[1&:1] F1[1a:1] Ab1[2e:1] C2[2&:1] Eb2[2a:1]
sub: F0[1:4] Ab0[2e:3] F0[3:4] Eb0[4e:3] | F0[1:4] Ab0[2e:3]
```

À placer en mesures 7 et 8 de la phrase : la mesure 8 passe en doubles croches, monte en arpège et s'arrête au temps 3.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 les tables « Squibble » (Digital, Serum 2) et « Harmonic Subtle » (Digital, Serum 1), le filtre Flg L6+, les warps Odd/Even, Sync et RM. Vérifier les destinations des macros.
- Ouvrir le preset gratuit d'Antidote Audio (lien Dropbox de la vidéo F06-01) pour comparer JU01 au patch d'origine.
- Écouter chaque recette avec le sub et le break, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
