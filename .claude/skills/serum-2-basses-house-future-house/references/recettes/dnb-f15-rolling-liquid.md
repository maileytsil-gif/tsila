# Vingt recettes de rolling, roller et liquid pour la Drum and Bass (famille F15)

Quatrième lot DnB : les basses qui roulent sous le break et celles de la liquid. Ce sont des tables simples, des mouvements longs (LFO lents ou enveloppes lentes) et un grave plein ; la ligne compte autant que le son. En liquid, « la basse tient plus à la composition qu'au sound design » [SOURCE F15-06]. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F15-02 ERB N DUB (roller, Serum 1), F01-01 Art1fact (Serum 2) ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` : F15-06 EDMProd (liquid), F15-01 EDMProd (module Clip de Serum 2) ;
- les extraits du registre `../tutoriels-a-consulter.md` : F15-07 Warrior Sound, F01-11 Warrior Sound ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot DnB** : celles de `dnb-f13-neuro.md` (174 BPM, schéma 2-step, sub séparé, octaves, RAND, MONO et LEGATO, resampling, contrôle).
2. **Tables simples.** « Des tables simples ; une table chargée ne donnera jamais ce poids » [SOURCE F15-02].
3. **Mouvements longs** : « longs mouvements par LFO lents ou enveloppes lentes » [SOURCE F15-02]. Un LFO libre (FREE, non synchronisé) dérive par rapport à la grille : à 1,7 Hz, un cycle dure 588 ms, soit 6,8 doubles croches à 174 BPM [CALCUL, F15-06].
4. **Le grave plein reste au sub.** EDMProd et ERB N DUB gardent le grave dans le patch ; Art1fact pose un sinus et une carrée une octave au-dessus [SOURCE F01-01]. Ici :
   - le sinus va sur la piste du sub (S02, phase continue, pour les lignes qui roulent) ;
   - la couche médium garde le reste, avec un passe-haut vers 80-100 Hz, plus bas que pour le neuro, parce que le roller remplit le bas-médium [DÉDUCTION, F01-01 : la carrée « remplit tout le reste du grave »].

   Un SUB à LEVEL 0 qui ne sert que de modulateur FM (F15-02) reste dans le patch : il ne sonne pas.
5. **Ligne et arrangement liquid** [SOURCE F15-06] :
   - Fa mineur fréquent, notes autour de F0 ;
   - ligne de 4 mesures dupliquée sur 16, variation (« bass run ») toutes les deux phrases de 4 ;
   - basse coupée 2 temps à la fin de la phrase de 16 ;
   - fader de la basse à −4 dB dans le mix final de l'article.

   La ligne relevée à l'écran joue les degrés VI, V et VII (D♭0, C1, E♭0, E♭1), sans la tonique fa [SOURCE F15-06, capture]. Elle n'est pas reproduite ici ; le bloc « liquid sur quatre accords » en reprend seulement l'idée des degrés.
6. **Quatre macros communes**, d'après les noms des sources [SOURCE F15-02 : FM, Bend, Verb ; F15-06 : FILTER, WOBBLE] :
   - `Filter` : coupure ou quantité d'enveloppe sur la coupure ;
   - `Wobble` : profondeur ou vitesse du LFO lent ;
   - `FM` : quantité de FM ;
   - `Verb` : mix de la réverb interne, ou profondeur d'un LFO sur ce mix.

   Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| RL01 | Roller ERB N DUB | référence | sinus et carré arrondi en FM (Sub), MG Low 6 |
| RL02 | Roller nu | apprentissage | deux tables simples désaccordées |
| RL03 | Liquid PWM | liquid | PWM DS sur A et B, LFO libre 1,7 Hz |
| RL04 | Liquid additive | liquid claire | sinus FM depuis un triangle, Sine Shaper |
| RL05 | Liquid soustractive | liquid sombre | carré à l'unison 5, MG Low 24 fermé |
| RL06 | Basse épaisse Art1fact | roller plein | carrée une octave au-dessus du sinus |
| RL07 | Rolling au module Clip | ligne roulante dans Serum | Clip MONO en doubles croches |
| RL08 | Rolling à courbes de hauteur | glissés dessinés | Clip POLY, Trans 24, courbes |
| RL09 | Rolling à Expr X | filtre note par note | couloir Expr X → coupure |
| RL10 | Roller Juno | roller doux | table PWM, unison 3, LFO sur le désaccord |
| RL11 | Roller sans automation | roller qui évolue | deux tables à −1 et −2 octaves |
| RL12 | Liquid au wobble ponctuel | fin de phrase | macro `Wobble` sur une mesure |
| RL13 | Liquid à reverb de basse | liquid aérée | envoi de reverb sans grave |
| RL14 | Roller en croches liées | roller legato | portamento court, notes jointives |
| RL15 | Roller en triolets | rebond | LFO 1/8 triolet |
| RL16 | Liquid tenue | breakdown | tenues de 6 temps, filtre lent |
| RL17 | Roller glissé au pitch bend | lignes expressives | pitch bend +12, portamento |
| RL18 | Liquid filtrée par phrases | arrangement | coupure automatisée sur 16 mesures |
| RL19 | Roller tout dans Serum | impression | chaîne interne, aucun effet externe |
| RL20 | Bass run à l'octave | variation avant la frontière | saut d'octave à la place d'une tenue |

## Les vingt recettes

### RL01 Roller ERB N DUB — référence du fichier
- **Patch** :
  - **OSC A** : « Analog_BD_Sin », sans unison, detune, blend ni random ; position fixe (écran : 256) ; LEVEL 27 % ; OCT −1 ; FIN modulé par la macro 4 ; WARP FM (Sub).
  - **SUB** : LEVEL 0, OCT −1 (écran : « 1 », à confirmer), FIN réglé : il ne sert qu'à moduler.
  - **OSC B** : « SawRoundedToSquare », position 11, OCT −2, FIN +28, phase au milieu, RAND 0, WARP FM (Sub), LEVEL 9 %. A et B désaccordés l'un contre l'autre : un effet proche du Reese.
  - **FILTER 1** : MG Low 6, RES et DRIVE montés, une enveloppe sur CUTOFF et FAT, MIX 91 %.
  - **NOISE** : « AlphaNz », PITCH monté, key track, niveau qui retombe sous ENV 1.
  - **Global** : MONO, un peu de PORTAMENTO, pitch bend +12, largeur d'unison à 0 (« le plus de mono possible »).
- **ENV 1** (écran) : attaque 67 ms, hold 0, decay 946 ms, sustain −4,4 dB, release 343 ms.
- **ENV 2** (écran) → DRIVE de la Diode 1 : attaque 387 ms, decay 1,00 s, sustain 100 %, release 15 ms.
- **FX** :
  1. Distortion Diode 1, MIX 100 %, DRIVE sur ENV 2.
  2. Equalizer en « sourire » (grave et aigus montés), sans modulation.
  3. Hyper, MIX 12, UNISON 3.
  4. Filter MG Low 6, MIX 44 %, CUTOFF ≈ 505 Hz : dompte les aigus.
  5. Reverb Hall, MIX qui monte sous LFO 4 en mode ENVELOPE, synchronisé, 4 mesures : une traîne qui arrive.
- **Calcul** : l'attaque de 67 ms dure 0,78 double croche à 174 BPM ; ENV 2 met 387 ms à monter le drive, plus d'une noire (345 ms) [CALCUL]. Les notes courtes ne reçoivent presque pas de distorsion.
- **Macros** : celles de la source (écran : FM, Bend, Verb, FM) → `Filter` quantité d'enveloppe sur CUTOFF · `Wobble` FIN de A (macro 4 de la source) · `FM` quantité de FM (Sub) · `Verb` profondeur de LFO 4 → MIX de la Reverb.
- **Sub associé** : S02, phase continue, piste séparée. Le patch garde un grave plein (A à OCT −1) : couper la couche médium vers 80-100 Hz, ou garder RL01 sans sub si l'écoute le confirme.
- **Jeu** : bloc « DnB 174 — roller en doubles croches » ci-dessous.
- **Origine** : [SOURCE F15-02, ERB N DUB, transcription et trois captures, Serum 1, patch « BA A Team » du pack Serum Rollers ; « tout dans Serum, pas de traitement externe »].

### RL02 Roller nu — deux tables simples désaccordées
- **Patch** :
  - OSC A : sinus, OCT 0, LEVEL 30 %.
  - OSC B : Saw Rounded to Square (ou une scie arrondie), OCT 0, FIN +28, LEVEL 15 %, RAND 0.
  - FILTER 1 : MG Low 6 sur A et B, CUTOFF 500 Hz, RES 20 %.
  - LFO 1 lent (4 mesures, RETRIG) → CUTOFF (+20 %).
- **ENV 1** : attaque 5 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Diode 1 légère ; passe-haut à 90 Hz.
- **Battement** : B à +28 cents contre A bat à 1,42 Hz sur F1 (87,3 Hz), soit à peu près une blanche (1,45 Hz à 174 BPM) [CALCUL].
- **Macros** : `Filter` CUTOFF · `Wobble` FIN de B (+10 → +40) · `FM` — · `Verb` —.
- **Sub associé** : S02.
- **Origine** : RL01 sans FM ni bruit [ORIGINAL] ; A et B désaccordés « proches du Reese » [SOURCE F15-02].

### RL03 Liquid PWM — « BS PWM Sub »
- **Patch** :
  - **OSC A** : table « PWM DS », OCT 0, Unison 1, WT POS et LEVEL modulés.
  - **OSC B** : table « PWM DS », OCT 0, Unison 2, WT POS et LEVEL modulés.
  - SUB et NOISE éteints.
  - **FILTER 1** : MG Low 24 sur A et B, CUTOFF ≈ 28 % (10 h), RES ≈ 28 %, DRIVE ≈ 45 %, FAT ≈ 8 h, MIX 100 %.
  - **LFO 1** : triangle, mode OFF (libre, sans redéclenchement), BPM décoché, RATE 1,7 Hz, 2 destinations (non lues).
  - **LFO 2** : 1 destination (non lue).
  - MONO + LEGATO, PORTA ≈ 11 h (sans valeur affichée).
- **ENV 1** (écran) : valeurs par défaut, 0,5 ms / 0 ms / 1,00 s / 0,0 dB / 15 ms.
- **FX** : non montrés ; passe-haut à 90 Hz ajouté [ORIGINAL] puisque le sub est à part.
- **Macros** : macro 1 « FILTER » (1 destination), macro 2 « WOBBLE » (3 destinations) → `Filter` · `Wobble` · `FM` — · `Verb` —.
- **Sub associé** : S02. Le preset de l'article porte lui-même le grave ; la PWM ferait varier le niveau de la fondamentale, d'où le sub séparé.
- **Origine** : [SOURCE F15-06, capture « 1.50.14 », Serum 1, preset du pack de l'article].

### RL04 Liquid additive — sinus FM et Sine Shaper
- **Patch** :
  - **OSC A** : « Analog_BD_Sin », OCT 0, Unison 1, WARP FM (B) ≈ 33 % (10 h 30), modulé.
  - **OSC B** : Basic Shapes en triangle, OCT +2, LEVEL au minimum.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : Distortion Sine Shaper, filtre OFF (F 330, Q 2,0 affichés), DRIVE ≈ 28 %, MIX ≈ 100 % ; passe-haut à 90 Hz [ORIGINAL].
- **Calcul** : B deux octaves au-dessus = rapport 4:1 ; la FM ajoute des composantes à fc ± 4·fc, donc des harmoniques de la note (3 et 5 fois la fondamentale) [CALCUL].
- **Macros** : `Filter` — · `Wobble` LFO lent → quantité de FM · `FM` quantité de FM 15 → 50 % · `Verb` DRIVE du Sine Shaper.
- **Sub associé** : S02.
- **Origine** : méthode « additive » (formes simples, puis distorsion, FM, effets) [SOURCE F15-06, captures « 3.37.22 » et « 3.37.27 »].

### RL05 Liquid soustractive — carré à l'unison, filtre fermé
- **Patch** :
  - **OSC A** : « BSOD_Square », OCT 0, Unison 5, DETUNE ≈ 12 h 30, BLEND ≈ 13 h 30, WT POS ≈ 15 h 30.
  - **FILTER 1** : MG Low 24, CUTOFF ≈ 28 %, RES ≈ 11 %, DRIVE ≈ 39 %, FAT ≈ 8 h. La source y route aussi le SUB (A + S) ; **ici, SUB éteint**.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : passe-haut à 90 Hz [ORIGINAL] ; largeur seulement au-dessus de 200 Hz.
- **Macros** : `Filter` CUTOFF 15 → 50 % · `Wobble` LFO lent → CUTOFF · `FM` — · `Verb` —.
- **Sub associé** : S02.
- **Test** : l'unison 5 s'annule en partie en mono ; contrôler avec le sub.
- **Origine** : méthode « soustractive », que l'auteur préfère : un passe-bas qui ne laisse presque que le sub [SOURCE F15-06, capture « 3.39.50 »].

### RL06 Basse épaisse Art1fact — carrée une octave au-dessus
- **Patch** (couche médium seulement ; le sinus va au sub) :
  - **OSC B** : Basic Shapes en position carrée, OCT 0 (une octave au-dessus du sub), unison faible, priorité au centre.
  - **FILTER 1** : passe-bas contre les aigus « quite horrible » de la carrée.
  - **FILTER 2** en série : Bandreject large (Misc), puis un passe-bande « avec une petite crête » (type exact non dit ; peut-être BP de la catégorie Multi).
  - **LFO 1** très lent, « dotted pattern » → CUTOFF de FILTER 1, → LEVEL de la carrée.
  - **OSC A** : sinus, LEVEL 0, une octave sous B : il ne sert qu'à la FM, dans un sens ou dans l'autre (sens final non dit).
  - **WARP** Bend + sur la carrée, modulé.
- **ENV 1** : attaque et release « un peu » montés ; 5 ms et 80 ms [ORIGINAL].
- **FX** : Splitter L/H, Distortion dans la bande haute seulement (« les distorsions de Serum ne marchent pas très bien dans le grave »), FREQ de la distorsion et MIX modulés.
- **Macros** : `Filter` CUTOFF de FILTER 1 · `Wobble` profondeur de LFO 1 · `FM` quantité de FM · `Verb` —.
- **Sub associé** : S02, à la place du sinus de la vidéo. La vidéo place le sub « vers 40 » sur SPAN (unité non dite).
- **Origine** : [SOURCE F01-01, Art1fact, transcription seule, Serum 2] : « un sinus pour le sub, plus une carrée une octave au-dessus qui remplit tout le reste ». Scission en deux instruments imposée par la règle du projet.

### RL07 Rolling au module Clip — la ligne jouée par Serum
- **Patch** : RL02 ou RL01, avec le module CLIP :
  - Trigger Mode MONO ;
  - Length 1 mesure, KB Span Off, Trans 0, Mode Normal ;
  - Rate 1x, BPM coché ;
  - Launch Quant 1/16 ; Retrig, Velo Trig et Note Gate décochés ;
  - grille 1/16 ; vélocités égales (≈ 97 sur l'écran).
- **Jeu** : une note tenue dans Live lance la ligne roulante du Clip ; dessiner dans le Clip le motif du bloc « roller en doubles croches » ci-dessous.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 30 ms.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S02, joué par un clip MIDI de Live, pas par le Clip de Serum : le sub suit les fondamentales.
- **Test** : vérifier que le Clip démarre sur le temps (Launch Quant 1/16 et note de Live quantifiée).
- **Origine** : [SOURCE F15-01, EDMProd, captures, Serum 2] : séquence roulante autour d'une note grave répétée. Le motif de l'article n'est pas repris.

### RL08 Rolling à courbes de hauteur — glissés dessinés
- **Patch** : RL07, avec un Clip 2 :
  - Trigger Mode POLY, Trans 24, Length 1 mesure ;
  - Rate 1t (triolet) ou 1x ; Launch Quant 1/8 ;
  - courbes de hauteur dessinées sur les notes : montée vers la note suivante, longue chute courbe à la fin de la mesure (≈ 9 demi-tons, estimation sur la capture).
- **ENV 1** : comme RL07.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S02, sans courbe de hauteur.
- **Origine** : [SOURCE F15-01, captures « 08 » et « 09 »].

### RL09 Rolling à Expr X — le filtre note par note
- **Patch** : RL07 ; clic droit sur CUTOFF de FILTER 1 › Mod Source › MPE › Expr X (Pan) ; dans le Clip, le couloir Expr X donne une valeur de −100 à +100 par note.
- **ENV 1** : comme RL07.
- **Macros** : `Filter` CUTOFF de base · les autres comme la recette de départ.
- **Sub associé** : S02.
- **Test** : les quantités d'Expr X vers le filtre ne sont pas lisibles sur l'article ; partir de ±20 %.
- **Origine** : [SOURCE F15-01, captures « 03 » et « 09 »].

### RL10 Roller Juno — table PWM, unison 3
- **Patch** :
  - OSC A : table « PWM Juno » (nom Serum 1 ; à défaut « PWM DS »), position 64, Unison 3.
  - LFO 1 calé au tempo → DETUNE d'unison.
  - FILTER 1 : MG Low 24, CUTOFF 600 Hz [ORIGINAL].
- **ENV 1** : attaque 3 ms, sustain 100 %, release 60 ms [ORIGINAL].
- **Macros** : `Filter` CUTOFF · `Wobble` profondeur de LFO 1 → DETUNE · `FM` — · `Verb` —.
- **Sub associé** : S02.
- **Origine** : [EXTRAIT F15-07, Warrior Sound, page non lue] : table « PWM Juno » en position 64, unison 3 sur l'osc 1, LFO 1 sur le detune calé au tempo. Le reste est [ORIGINAL].

### RL11 Roller sans automation — deux tables, deux octaves
- **Patch** :
  - OSC A : « Analog_BD_Sin », OCT −1.
  - OSC B : « Basic MCB » (nom de l'extrait, à retrouver), OCT −2.
  - LFO 1 (2 mesures, FREE) → WT POS de B ; LFO 2 (3 mesures, FREE) → CUTOFF : les deux cycles ne se recalent que toutes les 6 mesures [CALCUL].
- **ENV 1** : attaque 3 ms, sustain 100 %, release 60 ms [ORIGINAL].
- **FX** : passe-haut à 90 Hz [ORIGINAL].
- **Macros** : `Filter` CUTOFF · `Wobble` profondeur de LFO 2 · `FM` — · `Verb` —.
- **Sub associé** : S02 ; l'osc A à −1 octave ne remplace pas le sub.
- **Origine** : [EXTRAIT F01-11, Warrior Sound, page non lue] : osc A Analog BD Sin −1 octave, osc B Basic MCB −2 octaves, « boucle qui évolue sans automation ». Les LFO sont [ORIGINAL].

### RL12 Liquid au wobble ponctuel — une mesure de mouvement
- **Patch** : RL03, avec la macro « WOBBLE » (3 destinations dans la source) : LFO 1 → CUTOFF, → LEVEL de B, → WT POS. Macro à 0 pendant la phrase, montée sur une seule mesure.
- **ENV 1** : comme RL03.
- **Macros** : celles de RL03.
- **Sub associé** : S02, sans wobble.
- **Jeu** : automation de la macro sur la dernière mesure d'une phrase de 8 ou de 16.
- **Origine** : automation de la macro 2 du sub à la mesure 60 pour « un petit wobble » [SOURCE F15-06].

### RL13 Liquid à reverb de basse — envoi sans grave
- **Patch** : RL03 ou RL05, et un envoi de reverb dédié à la basse, par plug-in tiers :
  - grave coupé, assez brillant ;
  - filtre d'entrée de la reverb centré vers 1,36 kHz, large ;
  - envoi automatisé avec le balayage de filtre de la basse.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ ; `Verb` = niveau d'envoi automatisé dans Live.
- **Sub associé** : S02, sans envoi.
- **Origine** : [SOURCE F15-06 et capture « 5.54.59 »]. La source utilise la Reverb native de Live (preset « Bright Room », filtre d'entrée 1,36 kHz, largeur 5,10) : contraire à la règle 6, d'où le plug-in tiers.

### RL14 Roller en croches liées — portamento court
- **Patch** : RL01 ou RL02, MONO + LEGATO, PORTAMENTO 40 ms, ALWAYS décoché.
- **Calcul** : 40 ms font 0,46 double croche à 174 BPM : le glissé reste discret [CALCUL].
- **ENV 1** : attaque 3 ms, sustain 100 %, release 30 ms.
- **Jeu** : croches jointives, chevauchements d'un quart de double croche sur les notes à lier.
- **Macros** : `Wobble` PORTA (0 → 80 ms) · les autres comme la recette de départ.
- **Sub associé** : S02.
- **Origine** : « un peu de portamento » [SOURCE F15-02] ; valeurs [ORIGINAL].

### RL15 Roller en triolets — le rebond
- **Patch** : RL02, avec LFO 1 à 1/8 triolet (114,9 ms), RETRIG → CUTOFF (+25 %).
- **ENV 1** : comme RL02.
- **Calcul** : sur une noire, trois cycles de filtre ; sur une note de trois doubles croches (259 ms), 2,25 cycles [CALCUL].
- **Macros** : `Wobble` profondeur de LFO 1 · les autres comme RL02.
- **Sub associé** : S02.
- **Origine** : [ORIGINAL] ; rebond en triolets du wobble de Future House (`../motifs.md`).

### RL16 Liquid tenue — breakdown
- **Patch** : RL05, avec CUTOFF ≈ 20 %, LFO 1 de 4 mesures (5,5 s) → CUTOFF.
- **ENV 1** : attaque 15 ms, sustain 100 %, release 250 ms.
- **Jeu** : bloc « DnB 174 — liquid sur quatre accords » ci-dessous.
- **Macros** : celles de RL05.
- **Sub associé** : S02.
- **Origine** : tenues de 6 temps de la ligne d'EDMProd [SOURCE F15-06, capture] ; filtre lent [ORIGINAL].

### RL17 Roller glissé au pitch bend — +12
- **Patch** : RL01, avec PITCH BEND RANGE +12 et un peu de PORTAMENTO.
- **Jeu** : courbes de pitch bend dessinées dans Live, montée d'une octave sur la dernière noire d'une phrase.
- **ENV 1** : comme RL01.
- **Macros** : celles de RL01 ; la source a une macro « Bend ».
- **Sub associé** : S02, **sans** pitch bend : le sub de sa piste ne reçoit pas les courbes.
- **Origine** : Global pitch bend +12 et macro « Bend » [SOURCE F15-02].

### RL18 Liquid filtrée par phrases — automation de la coupure
- **Patch** : RL03 ou RL05, sans changement.
- **Jeu** : macro `Filter` automatisée dans Live : fermée au début du drop, ouverture progressive sur 16 mesures, retour au début de la phrase suivante.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S02, sans automation.
- **Origine** : automation de filtre sur la basse aux mesures 40 et 56 [SOURCE F15-06] ; durée [ORIGINAL].

### RL19 Roller tout dans Serum — impression sans effet externe
- **Patch** : RL01 tel quel, chaîne d'effets interne (Diode 1, EQ, Hyper, MG Low 6, Reverb), aucun traitement après Serum.
- **Jeu** : imprimer 8 mesures (procédure de `../../../resampling/SKILL.md`), puis comparer l'impression au patch en direct, à niveau égal.
- **Macros** : celles de RL01.
- **Sub associé** : S02, imprimé séparément.
- **Origine** : « tout dans Serum, pas de traitement externe » [SOURCE F15-02].

### RL20 Bass run à l'octave — variation avant la frontière
- **Patch** : RL03, RL05 ou RL16, sans changement de son.
- **Jeu** : sur la seconde phrase de 4 mesures, remplacer la première tenue longue par un saut d'octave (la note, puis la même une octave au-dessus) ; couper la basse sur les 2 derniers temps de la phrase de 16. Bloc « DnB 174 — bass run à l'octave » ci-dessous.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S02, qui suit la note grave sans sauter d'octave.
- **Origine** : « bass run » où « le saut d'octave remplace la tenue de 6 temps » [SOURCE F15-06, capture « 5.13.49 »] ; règle des drops d'`AGENTS.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60), notes pour des oscillateurs à OCT 0. DnB à 174 BPM : kick sur les doubles croches 1 et 11, caisse claire sur 5 et 13 (règles communes de `dnb-f13-neuro.md`). Aucune attaque de basse sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dnb-f15-rolling-liquid.md`.

```grille
titre: DnB 174 — roller en doubles croches (RL01, RL02, RL07)
tempo: 174
accords: Fm7 | Fm7
roller: F1[1:1] F1[1e:1] C2[1&:1] F1[1a:1] F1[2e:1] Ab1[2&:1] F1[2a:1] F1[3:1] C2[3e:1] F1[3&:1] F2[3a:1] F1[4e:1] Ab1[4&:1] C2[4a:1] | F1[1:1] F1[1e:1] C2[1&:1] F1[1a:1] F1[2e:1] Eb2[2&:1] F1[2a:1] F1[3:1] C2[3e:1] F1[3&:1] Ab1[3a:1] F1[4e:1] Eb1[4&:1] F1[4a:1]
sub: F0[1:4] F0[2e:3] F0[3:4] F0[4e:3] | F0[1:4] F0[2e:3] F0[3:4] Eb0[4e:3]
```

Doubles croches autour de la tonique, avec un trou sur chaque caisse claire. Le sub tient la tonique par groupes de trois ou quatre doubles croches ; avec S02 (Contiguous), les notes jointives ne repartent pas de zéro.

```grille
titre: DnB 174 — liquid sur quatre accords (RL03, RL05, RL16)
tempo: 174
accords: Dbmaj7 | Cm7 | Bbm7 | Eb
liquid: Db1[1:10] C2[3a:2] Ab1[4e:3] | C1[1:10] G1[3a:2] Eb1[4e:3] | Bb0[1:10] F1[3a:2] Db1[4e:3] | Eb1[1:6] Eb2[2&:6] Bb1[4e:3]
sub: Db0[1:16] | C1[1:16] | Bb0[1:16] | Eb0[1:16]
```

Degrés VI, V, IV et VII de fa mineur ; le sub tient la fondamentale de chaque mesure. Db0 (34,6 Hz) et Eb0 (38,9 Hz) sont très graves : les remonter d'une octave si le système ou le kick ne les portent pas. Ligne originale ; seule l'idée des degrés vient de F15-06.

```grille
titre: DnB 174 — bass run à l'octave (RL20)
tempo: 174
accords: Dbmaj7 | Eb
run: Db1[1:6] Db2[2&:6] C2[4e:3] | Eb1[1:6] Eb2[2&:3] Bb1[3a:3] G1[4a:1]
sub: Db0[1:12] C1[4e:3] | Eb0[1:12] G0[4e:3]
```

Le saut d'octave remplace une tenue : la basse médium monte, le sub reste sur la note grave.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « Analog_BD_Sin », « SawRoundedToSquare », « PWM DS », « BSOD_Square », « PWM Juno », « Basic MCB » ;
  - le bruit « AlphaNz » ;
  - le module Clip (Trigger Mode, Launch Quant, courbes de hauteur, couloir Expr X).

  Vérifier les destinations des macros.
- Lire à l'écran les destinations des LFO de RL03 et le type de passe-bande de RL06.
- Écouter chaque recette avec le sub et le break, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
