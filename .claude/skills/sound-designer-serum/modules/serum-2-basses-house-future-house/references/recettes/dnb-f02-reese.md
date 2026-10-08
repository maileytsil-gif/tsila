# Vingt recettes de Reese pour la Drum and Bass (famille F02)

Deuxième lot DnB : le Reese, la basse de deux scies (ou plus) désaccordées dont le battement fait bouger la note. Né en 1988 sur un Casio CZ (Kevin Saunderson), il est passé à la jungle en 1994, quand Renegade et Ray Keith l'ont samplé sur *Terrorist* (`basses.md` § 2). C'est la basse médium historique de la DnB. Ce fichier part des recettes de `house-f02-reese.md` et les règle pour 174 BPM, les octaves des tutoriels DnB et le break. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F02-01 DNB Academy, F02-03 Strob Studio, F13-02 Art1fact ;
- `../etudes-pages-dubstep-dnb.md` : F02-14 Future Music, F15-06 EDMProd ;
- le § 2 « Reese » de `../../../../references/basses.md` (Attack Magazine, Native Instruments, LANDR, Toolroom) ;
- `../documentation-basses.md` § 3 (battements) et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot DnB** : celles de `dnb-f13-neuro.md` (174 BPM, schéma 2-step, sub séparé, octaves, RAND, MONO et LEGATO, resampling, contrôle). **Règles du Reese** : celles de `house-f02-reese.md` :
   - le Reese n'est jamais le sub : passe-haut vers 100-120 Hz, sub sinus mono sur sa piste ;
   - le désaccord règle un tempo, pas une largeur ;
   - un Reese statique est un échec : un LFO lent sur la coupure.
2. **Battement à 174 BPM.** Battement = f × (2^(c/1200) − 1), où c est l'écart **total** entre les deux voix [CALCUL, `../documentation-basses.md` § 3]. Écart qui donne un battement à la noire (2,90 Hz) ou à la mesure (0,725 Hz) [CALCUL] :

   | Note (MIDI) | Fréquence | Écart pour la noire | Écart pour la mesure | Battement à ±28 cents |
   | --- | --- | --- | --- | --- |
   | F0 (29) | 43,7 Hz | 111 cents | 28,5 cents | 1,44 Hz |
   | F1 (41) | 87,3 Hz | 56,6 cents | 14,3 cents | 2,87 Hz |
   | Ab1 (44) | 103,8 Hz | 47,7 cents | 12,0 cents | 3,41 Hz |
   | C2 (48) | 130,8 Hz | 38,0 cents | 9,6 cents | 4,30 Hz |
   | F2 (53) | 174,6 Hz | 28,5 cents | 7,2 cents | 5,74 Hz |

   La « signature DnB » de ±27 à ±30 cents (Attack Magazine et Native Instruments, `basses.md` § 2) bat presque exactement à la noire sur F1 à 174 BPM. Ce rapprochement est un calcul, pas un fait rapporté par les sources.
3. **Octave des tutoriels** : OCT −3 sur les scies chez DNB Academy [SOURCE F02-01], OCT 0 chez Strob Studio [SOURCE F02-03]. Les grilles donnent les notes à OCT 0 (règle 3 du lot).
4. **Quatre macros communes**, celles de `house-f02-reese.md` :
   - `Beat` : désaccord ;
   - `Motion` : profondeur du LFO sur la coupure ;
   - `Grit` : drive ;
   - `Width` : chorus, Hyper ou unison, au-dessus du passe-haut seulement.

   Vérifier le « + » sur chaque destination.
5. **Contrôle propre au Reese** : en mono, le niveau ne doit pas fluctuer au vumètre plus que voulu ; jouer la note la plus grave et la plus aiguë de la ligne, puisque le battement double à chaque octave.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| DR01 | Reese DnB de référence | toutes | 2 scies ±28, LP 650 Hz, Overdrive |
| DR02 | Reese lourd DNB Academy | drop lourd | 3 oscillateurs, Combs, PD, OCT −3 |
| DR03 | Reese Strob Studio | jungle, DnB | ±20, Phs 36+, désaccord selon la note |
| DR04 | Reese AM déchirant | neurofunk | AM qui s'installe, LFO libre |
| DR05 | Reese jungle lissé | jungle | LP 650 Hz, encoche balayée |
| DR06 | Reese à la noire | DnB calée | écart choisi pour battre à la noire |
| DR07 | Reese à battement constant | lignes à sauts d'octave | Note → désaccord |
| DR08 | Sinus qui respire | liquid, breakdown | 2 sinus ±27, une octave au-dessus du sub |
| DR09 | Reese unison impair | drop | unison 5 ou 7, Hyper au-dessus du split |
| DR10 | Reese à la Casio | old school | PD, deux oscillateurs |
| DR11 | Reese au peigne | DnB sombre | Combs seul, LFO de 2 mesures |
| DR12 | Reese à encoches contraires | neurofunk, liquid | deux encoches en sens opposé |
| DR13 | Reese glissé | lignes à glissés | portamento 250 ms, notes liées |
| DR14 | Reese sombre | liquid, minimal | LP 225 Hz, chorus 50 % |
| DR15 | Reese half-time | half-time | LFO de 4 mesures, tenues de 2 temps |
| DR16 | Reese imprimé en table | toutes | battement calé sur le tempo |
| DR17 | Reese ressamplé | neurofunk | prises en LFO libre |
| DR18 | Reese distordu par bandes | drop | Splitter L/M/H, grave propre |
| DR19 | Reese à l'Hyper | refrain de drop | Hyper au lieu de l'unison |
| DR20 | Reese à coupure de fin de phrase | variation avant la frontière | deux temps de silence |

## Les vingt recettes

### DR01 Reese DnB de référence — deux scies, ±28 cents
- **Patch** :
  - OSC A et OSC B en scie (Default Shapes), OCT 0, FIN −28 et +28 (56 cents d'écart), RAND 0.
  - FILTER 1 sur A et B : MG Low 24, CUTOFF ≈ 650 Hz, RES ≈ 14 %.
  - LFO 1 : triangle, 2 mesures, RETRIG → CUTOFF (+25 %).
  - MONO + LEGATO.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion Overdrive légère ; Equalizer en passe-haut à 120 Hz.
- **Battement** : 2,87 Hz sur F1, soit presque une noire à 174 BPM [CALCUL].
- **Macros** : `Beat` FIN ±15 → ±35 · `Motion` LFO 1 → CUTOFF · `Grit` DRIVE · `Width` MIX d'un Chorus au-dessus de 200 Hz.
- **Sub associé** : S01, même ligne MIDI une octave plus bas.
- **Jeu** : bloc « DnB 174 — Reese long avec trous » ci-dessous.
- **Origine** : point de départ « Reese médium » de `basses.md` § 2 (deux scies, ±28 cents, LP 24 dB ≈ 650 Hz, résonance ≈ 14 %, coupe-bas 120 Hz, overdrive léger), qui réunit Native Instruments et Attack Magazine ; R01 de `house-f02-reese.md`, recalé à 174 BPM.

### DR02 Reese lourd DNB Academy — trois oscillateurs, Combs, PD
- **Patch** :
  - OSC A et OSC B en scie (Default Shapes), OCT −3, FIN −38 et +38 (dit ; l'écran montre −38 et −28).
  - OSC C sur la table Analog « DM - Oscar », SEM +7 (une quinte), LEVEL réduit : l'aigu bizarre est assumé, puis filtré.
  - NOISE allumé (un des bruits blancs de Serum 2, écran « HP12 …sreo », START 3).
  - FILTER 1 sur A, B, C et noise : Misc › Combs, CUTOFF ≈ 30-31, VAR ≈ 50 %. La source y route aussi le sub (case S) ; ici, SUB éteint.
  - MONO + LEGATO.
  - Warp de A en PD (B) « pour fondre les couches » : 73-74 dit, 64 % à l'écran.
  - LFO 1 : RETRIG, montée rapide puis descente lente, 2 mesures → CUTOFF ≈ 45 %.
- **ENV 1** : non lue ; attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** :
  1. Distortion Overdrive, deux modules.
  2. Chorus.
  3. Filter MG Low 6 (la voix dit « low cut », l'écran montre un passe-bas).
  4. Compressor Multiband : −18,1 dB, 4:1, attaque et release 90,1, gain 4,2, bandes à 128 et 2 500 Hz.
  5. Equalizer : 210 Hz, Q 80, 0 dB ; creux à 484 Hz, Q 80, −15,6 dB.
  6. Passe-haut à 120 Hz ajouté [ORIGINAL].
- **Réglage final** : réintroduire la table Oscar, 2 voix d'unison.
- **Battement** : 76 cents d'écart battent à 3,9 Hz sur F1, plus vite que la noire [CALCUL] : un Reese nerveux.
- **Macros** : `Beat` FIN ±20 → ±40 · `Motion` LFO 1 → CUTOFF · `Grit` quantité de PD 40 → 80 % · `Width` MIX du Chorus.
- **Sub associé** : S01. La source route le sub dans le filtre 1 « pour un grave plus concis » ; ici il est sur sa piste.
- **Origine** : [SOURCE F02-01, transcription et quatre captures, Serum 2, DnB] ; R10 de `house-f02-reese.md`, ici à l'octave et au tempo de la source.

### DR03 Reese Strob Studio — Phs 36+, désaccord selon la note
- **Patch** :
  - OSC A et OSC B en scie, OCT 0, FIN −20 et +20 (« 22 de chaque côté » dit, 20-21 à l'écran), RAND 0. Mieux vaut désaccorder les deux en sens opposés qu'un seul de 40.
  - FILTER 1 sur A et B : Phs 36+ (le « phaser positif »), un peu de DRIVE.
  - LFO 1 : triangle, 4 mesures → CUTOFF.
  - Matrice : source Note → FIN : les notes aiguës battent plus vite.
  - MONO + LEGATO, un peu de PORTAMENTO.
  - La source garde un SUB en triangle, `Direct`, hors du filtre. **Ici, SUB éteint.**
- **ENV 1** (écran) : attaque 0,5 ms, hold 0, decay 1,00 s, sustain 0,0 dB, release 15 ms.
- **FX** : Distortion Tube, MIX ≈ 50 % pour garder un grave propre ; OTT (Compressor Multiband) pour un son plus moderne.
- **Battement** : 40 cents d'écart battent à 2,04 Hz sur F1 et 4,08 Hz sur F2 [CALCUL].
- **Macros** : `Beat` FIN ±12 → ±30 · `Motion` LFO 1 → CUTOFF · `Grit` DRIVE de la Tube · `Width` —.
- **Sub associé** : S01.
- **Origine** : [SOURCE F02-03, transcription française et trois captures, Serum 1]. Sa méthode préférée est une distorsion multibande après le design, en plug-in externe (Saturn, Trash 2) : voir DR18. R03 de `house-f02-reese.md`.

### DR04 Reese AM déchirant — l'analyse de « Bs Reese Evolve »
- **Patch** :
  - OSC A sur une table « gnarly » (Digital), OCT 0.
  - LFO 1 en mode FREE, lent, non synchronisé → WT POS : chaque note bouge autrement.
  - OSC B en sinus, LEVEL 0. WARP 1 d'OSC A en AM (B).
  - ENV 2 → ce warp, attaque lente (400-800 ms ; 1,2 à 2,3 noires à 174 BPM [CALCUL]), sustain 100 % : l'AM s'installe au cours de la note.
  - NOISE poussé dans la distorsion finale (le « fizz »).
  - FILTER 1 : double encoche modulée (dans Serum 2, NN 12 de la catégorie Multi, ou Notch 24).
  - MONO + LEGATO, PORTAMENTO vers midi.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : Reverb, puis compression lourde **après** la reverb (le son gonfle entre les notes), Distortion forte, Equalizer avec passe-haut à 120 Hz, élargissement au-dessus de 300 Hz.
- **Macros** : `Beat` attaque d'ENV 2 · `Motion` LFO 1 → WT POS · `Grit` DRIVE · `Width` largeur.
- **Sub associé** : S01. Le preset d'origine garde un sub dans le patch.
- **Origine** : [SOURCE F02-14, page MusicRadar, Serum 1, aucune valeur chiffrée sauf le portamento] ; R11 de `house-f02-reese.md`.

### DR05 Reese jungle lissé — passe-bas et encoche balayée
- **Patch** :
  - DR01, avec FILTER 1 en MG Low 24, CUTOFF 650 Hz, RES 14 %.
  - FILTER 2 en série : Notch 24, CUTOFF balayé de 300 Hz à 1,5 kHz par LFO 2 (2 mesures, RETRIG) ou par la macro automatisée dans Live.
- **ENV 1** : comme DR01.
- **FX** : Distortion Overdrive **après** les filtres ; passe-haut à 120 Hz.
- **Macros** : `Beat` · `Motion` LFO 2 → encoche · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Jeu** : jungle à 160-170 BPM ou DnB à 174 ; bloc « DnB 174 — Reese en appels » ci-dessous.
- **Origine** : « passe-bas cutoff ≈ 650 Hz, résonance ≈ 14 % pour le son jungle lissé, puis overdrive et filtre à encoche balayé automatisé » [SOURCE Native Instruments, `basses.md` § 2] ; R09 de `house-f02-reese.md`.

### DR06 Reese à la noire — écart choisi par le calcul
- **Patch** : DR01, avec l'écart réglé sur la note la plus jouée de la ligne, d'après la table de la règle 2 :
  - sur F1 : ±28,3 cents (56,6 cents d'écart) ;
  - sur Ab1 : ±23,9 cents ;
  - sur C2 : ±19,0 cents.
- **Variante à la mesure** : ±7,2 cents sur F1 : un seul cycle de battement par mesure, très lent [CALCUL].
- **ENV 1** : comme DR01.
- **Macros** : `Beat` FIN, bornes resserrées autour de la valeur calculée (±5 cents) · les autres comme DR01.
- **Sub associé** : S01.
- **Test** : avec RAND 0, le battement repart du même point à chaque note. Écouter s'il « tombe » avec la caisse claire ; sinon décaler la PHASE de B.
- **Origine** : formule du battement (`../documentation-basses.md` § 3) ; « le tempo peut être contrôlé en ajustant l'accord fin » [SOURCE Attack Magazine, `basses.md` § 2] ; valeurs [CALCUL].

### DR07 Reese à battement constant — Note → désaccord
- **Patch** : DR01, avec FIN de A et B pilotés par la source Note (matrice, quantité négative) : le désaccord diminue de moitié par octave montée. Exemple : ±28 cents sur F1, ±14 sur F2.
- **Calcul** : si f double et c est divisé par deux, le battement reste ≈ 2,9 Hz [CALCUL].
- **ENV 1** : comme DR01.
- **Macros** : `Beat` désaccord de base · les autres comme DR01.
- **Sub associé** : S01.
- **Test** : sur une ligne qui saute d'une octave, le battement garde sa vitesse ; comparer avec DR01, où il double.
- **Origine** : R12 de `house-f02-reese.md` ; Strob module le désaccord par la note dans l'autre sens (DR03). L'échelle de la source Note dans la matrice est à régler dans l'interface.

### DR08 Sinus qui respire — deux sinus, une octave au-dessus du sub
- **Patch** :
  - OSC A et OSC B en sinus, OCT 0, FIN −27 et +27, RAND 0.
  - Pas de filtre ; MONO + LEGATO.
  - LFO 1 lent (4 mesures) → LEVEL de B (−20 %) pour faire varier la profondeur du battement.
- **ENV 1** : attaque 10 ms, sustain 100 %, release 150 ms.
- **FX** : Distortion Soft Sat. légère pour faire entendre le battement sur petit haut-parleur ; passe-haut à 100 Hz.
- **Battement** : 54 cents d'écart battent à 2,77 Hz sur F1 [CALCUL].
- **Macros** : `Beat` FIN · `Motion` LFO 1 → LEVEL · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01, **une octave sous** la ligne : deux sinus désaccordés à la hauteur du sub feraient fluctuer le grave.
- **Jeu** : liquid, breakdown, intro.
- **Origine** : Attack Magazine construit avec deux sinus à ±27 cents, « un sub qui respire » [SOURCE `basses.md` § 2] ; placement une octave au-dessus [ORIGINAL] ; R04 de `house-f02-reese.md`.

### DR09 Reese unison impair — et largeur au-dessus du split
- **Patch** :
  - OSC A en scie, OCT 0, Unison 5 ou 7 (impair : une voix reste au centre), DETUNE 10-14 %.
  - FILTER 1 : MG Low 24, CUTOFF 800 Hz, LFO 1 (2 mesures) → CUTOFF.
  - Réglages d'unison : WIDTH à 0 sous le split, ou largeur ajoutée seulement après (Hyper dans HIGHS).
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **FX** : Splitter L/H à 200 Hz ; Overdrive et Hyper/Dimension dans HIGHS ; passe-haut à 120 Hz.
- **Macros** : `Beat` DETUNE · `Motion` LFO 1 → CUTOFF · `Grit` DRIVE · `Width` MIX de l'Hyper.
- **Sub associé** : S01.
- **Origine** : R05 de `house-f02-reese.md` ; « garder le mono puissant dans le patch, ajouter la stéréo après » [SOURCE F13-02].

### DR10 Reese à la Casio — distorsion de phase
- **Patch** :
  - OSC A en sinus, OCT 0, WARP PD (Self) ou PD (B).
  - OSC C identique, FIN −14 et +14 entre A et C.
  - LFO 1 (2 mesures, RETRIG) → quantité de PD (+30).
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion Tube légère ; passe-haut à 120 Hz.
- **Macros** : `Beat` FIN · `Motion` LFO 1 → PD · `Grit` quantité de PD · `Width` —.
- **Sub associé** : S01.
- **Test** : A/B avec DR01 à niveau égal ; le son garde un battement, avec une couleur plus douce que les scies.
- **Origine** : le Reese d'origine vient d'un Casio CZ-5000, donc d'une distorsion de phase ; les deux scies sont la reconstruction moderne [SOURCE `basses.md` § 2] ; PD de Serum 2 à rapprocher du CZ sans le supposer identique ; R15 de `house-f02-reese.md`, recette [DÉDUCTION].

### DR11 Reese au peigne — Combs seul
- **Patch** :
  - DR01 sans le MG Low 24 : FILTER 1 en Misc › Combs, CUTOFF ≈ 30 %, VAR (DAMP) ≈ 50 %.
  - LFO 1 : montée rapide puis descente lente, 2 mesures, RETRIG → CUTOFF (≈ 45 %).
- **ENV 1** : comme DR01.
- **FX** : Overdrive ; Filter MG Low 6 pour dompter l'aigu ; passe-haut à 120 Hz.
- **Macros** : `Beat` · `Motion` LFO 1 → CUTOFF · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Test** : le peigne change de couleur avec la note jouée ; vérifier la note la plus grave et la plus aiguë.
- **Origine** : DR02 réduit au peigne et au LFO [SOURCE F02-01] ; MIX sans effet sur les Combs [cartographie, § 6] ; variante [ORIGINAL].

### DR12 Reese à encoches contraires — le médium reste plein
- **Patch** :
  - DR01, avec FILTER 1 en Notch 24 dans le bas-médium et FILTER 2 en Notch 24 plus haut.
  - LFO 1 : triangle, 2 mesures, RETRIG → CUTOFF de FILTER 1 (+) et de FILTER 2 (−) : les deux encoches bougent en sens opposé.
  - MIX de FILTER 2 baissé.
- **ENV 1** : comme DR01.
- **Macros** : `Beat` · `Motion` LFO 1 · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Origine** : contre-mouvement de deux encoches [SOURCE F13-02, neurofunk] appliqué au Reese [ORIGINAL].

### DR13 Reese glissé — legato, portamento 250 ms
- **Patch** : DR01, avec MONO + LEGATO, PORTA 250 ms, ALWAYS décoché, RAND 0.
- **Tempo** : 250 ms font 2,9 doubles croches à 174 BPM [CALCUL]. Sur une note de deux doubles croches, le glissé ne finit pas : le réduire à 120-170 ms.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **Macros** : `Beat` FIN · `Motion` PORTA 80 → 250 ms · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01 sans glissé ; il ne suit que les notes graves.
- **Jeu** : bloc « DnB 174 — neuro glissé à l'octave » de `dnb-f13-neuro.md`.
- **Origine** : « notes courtes une octave au-dessus des notes graves, reliées par portamento ; Mono, Portamento 250 ms ; RandPhase désactivé » [SOURCE F13-11, neurofunk à 174 BPM] ; R20 de `house-f02-reese.md`.

### DR14 Reese sombre — passe-bas bas, chorus
- **Patch** :
  - DR01, avec CUTOFF ≈ 225 Hz et RES 10 %.
  - FIN ±15 : lent et doux.
- **ENV 1** : attaque 5 ms, sustain 100 %, release 100 ms.
- **FX** : Chorus MIX ≈ 50 % au-dessus de 150 Hz (dans HIGHS d'un Splitter L/H) ; passe-haut à 90 Hz.
- **Calcul** : entre le passe-haut à 90 Hz et le passe-bas à 225 Hz, il reste 1,3 octave : surtout la fondamentale F1 et la seconde harmonique [CALCUL].
- **Macros** : `Beat` FIN · `Motion` CUTOFF 150 → 500 Hz · `Grit` DRIVE · `Width` MIX du Chorus.
- **Sub associé** : S02, phase continue.
- **Jeu** : liquid, minimal ; la basse tient plus à la composition qu'au sound design en liquid [SOURCE F15-06].
- **Origine** : « passe-bas entre 116 et 225 Hz, chorus à ≈ 50 % » [SOURCE LANDR, `basses.md` § 2], appliqué à la seule couche médium [ORIGINAL] ; R08 de `house-f02-reese.md`.

### DR15 Reese half-time — mouvement sur quatre mesures
- **Patch** : DR01 ou DR03, avec LFO 1 sur 4 mesures (5,5 s à 174 BPM [CALCUL]), FIN ±20.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 120 ms.
- **Jeu** : caisse claire sur le temps 3 ; tenues de deux temps ou plus, une note par demi-mesure.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01.
- **Origine** : LFO de 4 mesures de Strob Studio [SOURCE F02-03, écran] ; half-time [ORIGINAL].

### DR16 Reese imprimé en table — battement calé sur le tempo
- **Patch** :
  1. Construire DR01, imprimer une note tenue de 2 mesures (2,76 s à 174 BPM), procédure de `../../../resampling/GUIDE.md`.
  2. La remettre dans OSC A (glisser le WAV ou Resample to) : le battement devient une suite de frames.
  3. LFO 1 → WT POS en BPM (1 ou 2 mesures) : le battement suit le tempo, plus la note.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **Macros** : `Beat` RATE de LFO 1 · `Motion` profondeur de LFO 1 → WT POS · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Origine** : R19 de `house-f02-reese.md` [DÉDUCTION, jamais essayée] ; « ressampler le son et le réimporter comme wavetable » [SOURCE F02-02].

### DR17 Reese ressamplé — prises en LFO libre
- **Patch** :
  1. DR04, avec LFO 1 en FREE : chaque note reçoit une modulation différente.
  2. Imprimer plusieurs minutes d'un riff, effets compris.
  3. Découper les meilleures prises et les remettre dans un Simpler ou un oscillateur.
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01, jamais ressamplé avec le Reese.
- **Origine** : « imprimer plusieurs minutes d'un riff en audio et découper les meilleures prises » [SOURCE F02-14] ; procédure : `../../../resampling/GUIDE.md`.

### DR18 Reese distordu par bandes — grave propre
- **Patch** : DR01 ou DR03, puis un Splitter L/M/H :
  - LOWS (sous 150 Hz) : rien ;
  - MIDS (150 Hz-2 kHz) : Distortion Overdrive, DRIVE élevé ;
  - HIGHS (au-dessus de 2 kHz) : Distortion Tube, MIX 50 %.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Beat` · `Motion` · `Grit` DRIVE de l'Overdrive · `Width` MIX d'un Chorus dans HIGHS.
- **Sub associé** : S01.
- **Origine** : « distorsion multibande hors du sub » ; « distorsion avec mix vers 50 % pour garder un sub propre » [SOURCE F02-03] ; distorsion seulement dans les aigus [SOURCE F01-01, F13-02] ; découpe en trois bandes [ORIGINAL].

### DR19 Reese à l'Hyper — moins de voix, autant de largeur
- **Patch** :
  - DR01 avec Unison 1.
  - Splitter L/H à 200 Hz ; dans HIGHS, Hyper/Dimension : UNISON 4-7, DETUNE 20-30 %, MIX 30-50 %, SIZE de Dimension 0.
- **ENV 1** : comme DR01.
- **Macros** : `Width` MIX de l'Hyper · les autres comme DR01.
- **Sub associé** : S01.
- **Test** : en mono, la largeur disparaît sans faire varier le niveau du grave.
- **Origine** : le manuel recommande Hyper plutôt que beaucoup d'unisson [cartographie, § 8-9] ; R16 de `house-f02-reese.md`.

### DR20 Reese à coupure de fin de phrase — variation avant la frontière
- **Patch** : DR01 ou DR05, sans changement de son.
- **Jeu** :
  - phrase de 4 mesures dupliquée sur 16 ;
  - une variation de ligne (« bass run ») toutes les deux phrases de 4 ;
  - basse coupée sur les 2 derniers temps de la phrase de 16 ;
  - bloc « DnB 174 — Reese à coupure de deux temps » ci-dessous.
- **Variante** : macro `Motion` montée sur la mesure 8, puis LFO 1 passé à 1/4 sur la mesure 8 seulement.
- **Sub associé** : S01, coupé en même temps que le Reese.
- **Origine** : ligne de 4 mesures, « bass run » toutes les deux phrases, basse coupée 2 temps à la fin de la phrase de 16 [SOURCE F15-06, liquid] ; règle des drops d'`AGENTS.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60), notes pour des oscillateurs à OCT 0. DnB à 174 BPM : kick sur les doubles croches 1 et 11, caisse claire sur 5 et 13 (règles communes de `dnb-f13-neuro.md`). Aucune attaque de basse sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dnb-f02-reese.md`.

```grille
titre: DnB 174 — Reese long avec trous (DR01, DR02, DR06)
tempo: 174
accords: Fm7 | Fm7
reese: F1[1:10] Ab1[3a:3] Eb1[4a:1] | F1[1:6] Eb1[2&:4] C2[4e:3]
sub: F0[1:10] Ab0[3a:3] Eb0[4a:1] | F0[1:6] Eb0[2&:4] C1[4e:3]
```

Une tenue de dix doubles croches dure 862 ms : à 2,87 Hz (DR01 sur F1), elle porte deux battements et demi [CALCUL]. Le motif reprend celui de `../motifs.md`, avec le do remonté d'une octave et décalé après la caisse claire.

```grille
titre: DnB 174 — Reese en appels (DR03, DR05)
tempo: 174
accords: Fm7 | Fm7
reese: F1[1:2] F1[2e:3] Eb1[3:2] F1[3&:1] Ab1[3a:1] C2[4e:3] | F1[1:2] F1[2e:3] Ab1[3:2] G1[3&:1] F1[3a:1] Eb1[4e:3]
sub: F0[1:4] F0[2e:3] Eb0[3:2] F0[3&:2] C1[4e:3] | F0[1:4] F0[2e:3] Ab0[3:2] G0[3&:1] F0[3a:1] Eb0[4e:3]
```

Notes courtes : le battement s'entend peu ; c'est le filtre (Phs 36+ ou encoche) qui porte le mouvement. Le sol de la mesure 2 est une note de passage vers le fa.

```grille
titre: DnB 174 — Reese à coupure de deux temps (DR20)
tempo: 174
accords: Fm7 | Fm7
reese: F1[1:6] Ab1[2&:6] Eb1[4e:3] | F1[1:6] C2[2&:2]
sub: F0[1:6] Ab0[2&:6] Eb0[4e:3] | F0[1:6] C1[2&:2]
```

À placer en mesures 15 et 16 d'une phrase de 16 : la basse s'arrête au temps 3 de la dernière mesure, le drop suivant repart sur le temps 1.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : la table « DM - Oscar », une table « gnarly », le bruit « HP12 …sreo », les filtres Phs 36+, Combs, NN 12 et Notch 24, l'échelle de la source Note dans la matrice. Vérifier les destinations des macros.
- Trancher à l'oreille la lecture de « ±28 » (par voix ou écart total) avec la table de la règle 2, sur la note la plus jouée.
- Écouter chaque recette avec le sub, puis avec le break, en mono, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
