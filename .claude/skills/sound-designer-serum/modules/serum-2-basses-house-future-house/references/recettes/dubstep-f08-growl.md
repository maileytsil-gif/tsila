# Vingt recettes de growl pour le Dubstep (famille F08)

Quatrième lot Dubstep : le growl dans son genre d'origine, à 140-150 BPM en half-time, joué grave (OCT −3), en appel et réponse avec la caisse claire. `house-f08-growl.md` adapte les mêmes tutoriels à la House, en remontant d'une octave. Ici, les réglages d'origine sont gardés, et les recettes ajoutent ce qui est propre au dubstep : rythmes parlants à la demi-mesure, dive de hauteur, fills, polymétrie. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F08-01, F08-02, F08-03, F13-02, F13-03 ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` : F08-04 Monosounds, F08-17 ADSR, F01-08 EDMProd ;
- `../etudes-pages-house.md` : F15-01, Clip de Serum 2 ;
- le § 3 de `../../../../references/basses.md` (patch BassGorilla) ;
- la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot Dubstep** : celles de `dubstep-f10-riddim.md`. **Règles du growl** : celles de `house-f08-growl.md` :
   - médiums de 150 Hz à 2 kHz ;
   - sub hors de la distorsion ;
   - trois couches de voyelle ;
   - distorsion avant phaser ;
   - RAND 0.
2. **Rythmes parlants en half-time** [SOURCE F08-04, infographie « Talking Rhythm Cheat Sheet »] :

   | Vitesse | Effet | Destination | Durée à 140 BPM |
   | --- | --- | --- | --- |
   | 1/1 | bouche lente | WT POS | 1 714,3 ms |
   | 1/2 | « half-time chew » | quantité de warp | 857,1 ms |
   | 1/4 | syllabes régulières | coupure du formant | 428,6 ms |
   | 1/8 | bégaiement dans la note | formant, faible profondeur | 214,3 ms |
   | 1/4 triolet | rebond « yoi » | WT POS | 285,7 ms |
   | 1/16 | texture bourdonnante, rarement | vitesse du phaser | 107,1 ms |

   Les durées sont [CALCUL].
3. **Quatre macros communes**, celles de `house-f08-growl.md` : `Talk`, `Snarl`, `Width`, `Dry`. Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| GD01 | Growl Monosounds à 140 | référence | LFO 1/2 en marches, 1/8 sur le formant |
| GD02 | Growl Konstricta natif | dubstep | LFO à la mesure (1,7 s) |
| GD03 | Chaîne FM à 150 BPM | dubstep lourd | FM C → B → A, très grave |
| GD04 | High Notch et pitch bend | dubstep | bend ±12 dans le clip |
| GD05 | Grille des rythmes parlants | growl complet | quatre LFO, quatre vitesses |
| GD06 | Growl contre la caisse claire | appel et réponse | silence sur le temps 3 |
| GD07 | Growl Skrillex natif | dubstep | WT POS sur une mesure |
| GD08 | Dive | fin de phrase | chute de Main Tuning |
| GD09 | Chaîne FM en mode Ratio | growl métallique | rapports 2, 3, 4 |
| GD10 | Trois mouvements qui convergent | growl vivant | trois LFO à trois vitesses |
| GD11 | Wub-growl | hybride | LFO 1/8 sur formant et filtre |
| GD12 | Fills de mid-bass | fin de phrase | piste dupliquée, fragments |
| GD13 | Diffusor seul | growl « vocodé » | STAGES modulés |
| GD14 | Filtre Reverb avant distorsion | growl creux | filtre Reverb |
| GD15 | Growl flou | refrain de drop | Bode, BLUR |
| GD16 | Sidechain interne | growl dense | bande grave du Multiband ducquée |
| GD17 | Growl granulaire | texture vocale | moteur Granular |
| GD18 | Growl doublé à l'octave | brillance | copie +12 au-dessus de 300 Hz |
| GD19 | Boucle de resampling | toutes | 2-3 passes, rythme changé |
| GD20 | Growl en boucle de 3 temps | polymétrie | module Clip |

## Les vingt recettes

### GD01 Growl Monosounds à 140 — référence
- **Patch** : G01 de `house-f08-growl.md`, avec trois changements.
  - OSC A une octave sous la table d'origine (OCT −1 à −3 selon la table).
  - LFO 1 dessiné en 3 ou 4 marches à hauteurs différentes, chutes courbes, 1/2, RETRIG → WT POS, quantité du Bend (moitié de profondeur) et CUTOFF du formant.
  - LFO 2 en 1/8, faible profondeur → CUTOFF du formant ; grille en triolet pour le rebond.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : Overdrive 40-60 % → Phaser 1/2, FEEDBACK 60 %, MIX 50 % → EQ (passe-haut à 120 Hz, −3 dB vers 400 Hz) → Multiband (2-5 kHz calmé) → Hyper/Dimension 15-25 %.
- **Macros** : celles de G01.
- **Sub associé** : S01 de `house-f01-sub.md`, recalé à 140 BPM.
- **Jeu** : bloc « Dubstep 140 — growl contre la caisse claire » ci-dessous.
- **Origine** : [SOURCE F08-04, page] ; à 140-150 BPM en half-time, mouvement principal 1/2.

### GD02 Growl Konstricta natif — LFO à la mesure
- **Patch** : G03 de `house-f08-growl.md`, avec OSC A et OSC B à OCT −3 comme dans la vidéo, LFO 1, 2 et 3 à 1 mesure.
  - À 140 BPM, chaque LFO dure 1 714,3 ms : le mouvement se répète à l'identique à chaque mesure.
- **ENV 1** : comme G03.
- **FX** : chaîne de G03 (Diffusor → EQ → Hard Clip sous LFO 1 → Chorus/Dimension → Multiband OTT → EQ final sans grave).
- **Macros** : celles de G03.
- **Sub associé** : S01.
- **Jeu** : une note tenue d'une mesure, ou deux blanches : le contour d'amplitude dessiné par LFO 1 fait le rythme.
- **Origine** : [SOURCE F08-02] ; durée [CALCUL].

### GD03 Chaîne FM à 150 BPM — très grave
- **Patch** : G04 de `house-f08-growl.md`, au tempo de la source (150 BPM), joué très grave (E0-G0 dans Live).
  - La source note que les patchs FM à trois étages sonnent autrement dans l'aigu.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : chaîne de G04 : passe-bande 100-600 Hz, Diffusor ×2, OTT ×3 (−18,1 dB, 4:1, bandes 88 / 2 500 Hz), phasers figés à 205 Hz, Chorus HPF à 8 Hz.
- **Macros** : celles de G04 ; MACRO 5 → Global › Main Tuning, bipolaire, ≈ 13 %, pilotée à la mesure (LFO Tool dans la source, LFO 4 interne ici).
- **Sub associé** : S01 sur sa piste. Le passe-bande coupe sous 100 Hz : le sub occupe seul E0-G0 (41-49 Hz).
- **Origine** : [SOURCE F08-01, Holo Rival, 150 BPM].

### GD04 High Notch et pitch bend — le geste dubstep
- **Patch** : G06 de `house-f08-growl.md` (High Notch 12, CUTOFF 141 Hz, RES 49, LFO 1 inversé −74, 1/2, Trigger, Diode 2 drive 20, Flanger depth 30 / feedback 64).
  - Pitch bend : UP +12, DOWN −12.
  - Dans le clip de Live, dessiner un bend d'une octave vers le bas sur la dernière note de la phrase (enveloppe MIDI Ctrl › Pitch Bend).
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **Macros** : celles de G06.
- **Sub associé** : S01, **sans** pitch bend. Le bend ne touche que la piste du growl.
- **Origine** :
  - [SOURCE BassGorilla, `basses.md` § 3, fiabilité faible] : « pitch bend ±12 » ;
  - pitch bend dessiné dans l'enveloppe de clip de Live [SOURCE F05-12].

### GD05 Grille des rythmes parlants — quatre LFO, quatre vitesses
- **Patch** :
  - OSC A sur une table qui « parle », OCT −2, Unison 1, RAND 0.
  - WARP 1 en Bend +/− (30-50 %) ; FILTER 1 en Formant-I, RES 25 %.
  - LFO 1 en 1/1 → WT POS (bouche lente).
  - LFO 2 en 1/2 → quantité du warp (« chew »).
  - LFO 3 en 1/4 → CUTOFF du formant (syllabes).
  - LFO 4 en 1/8, faible → CUTOFF du formant (bégaiement).
  - Tous en RETRIG.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : chaîne de GD01.
- **Macros** : `Talk` profondeur de LFO 3 · `Snarl` profondeur de LFO 2 · `Width` MIX de l'Hyper · `Dry` profondeur de LFO 4.
- **Sub associé** : S01.
- **Test** : couper les LFO un par un pour entendre chaque couche ; au-delà de trois couches actives, le son peut « baver ».
- **Origine** : grille des vitesses et destinations [SOURCE F08-04, infographie] ; assemblage en un seul patch [ORIGINAL].

### GD06 Growl contre la caisse claire — appel et réponse
- **Patch** : GD01 ou GD05, avec LFO 1 en mode ENVELOPE (un cycle par note) pour que chaque réponse soit nette.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −6 dB, release 60 ms.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S11, court.
- **Jeu** :
  - bloc « Dubstep 140 — growl contre la caisse claire » ci-dessous : l'appel sur les temps 1-2, rien sur la caisse claire (temps 3), la réponse sur la fin du temps 3 et le temps 4 ;
  - « laisser un silence avant chaque réponse » (fiche 8 de `../families.md`).
- **Origine** : half-time, caisse claire sur le temps 3 [SOURCE F01-08] ; écriture [ORIGINAL].

### GD07 Growl Skrillex natif — WT POS sur une mesure
- **Patch** : G09 de `house-f08-growl.md`, avec OSC A à OCT −2, LFO 1 → WT POS en boucle d'une mesure (1 714,3 ms à 140 BPM), LFO 2 → FM et CUTOFF du passe-bande.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Diode 2 → Phaser → EQ (−300 Hz) → Multiband → Dimension.
- **Macros** : celles de G09.
- **Sub associé** : S01. La page met le Sub Oscillator dans le patch ; ici il est sur sa piste.
- **Origine** : [SOURCE F08-17, page ADSR, repère qualitatif] ; toutes les valeurs de G09 sont [ORIGINAL].

### GD08 Dive — chute de hauteur en fin de phrase
- **Patch** : GD01 ou GD02, plus LFO 5 en mode ENVELOPE, 1/2, rampe descendante → Global › Main Tuning, de 0 à −12 demi-tons (quantité réglée dans l'infobulle).
  - LFO 5 n'agit que si une macro « Dive » (MACRO 6) est montée.
  - Dans Live, automatiser MACRO 6 à 100 % sur la dernière note de la phrase.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 200 ms.
- **Macros** : `Talk`, `Snarl`, `Width`, `Dry` comme la recette de départ, plus MACRO 6 « Dive » de 0 à 100 %.
- **Sub associé** : S01, sans chute ; le couper sur la note qui plonge.
- **Jeu** : une variation avant la frontière de huit mesures (règle des drops d'`AGENTS.md`).
- **Origine** :
  - LFO → Main Tuning [SOURCE F08-01, F10-01] ;
  - « une macro est aussi destination » (chaînage) [cartographie, § 7.3] ;
  - geste [ORIGINAL].

### GD09 Chaîne FM en mode Ratio — 2, 3, 4
- **Patch** : GD03 avec OSC B et OSC C en mode Ratio :
  - B : Ratio 2.000, SRC = A ;
  - C : Ratio 3.000, SRC = B (sinon SRC = A).

  Trois presets à comparer : (2, 3), (2, 4), (3, 4).
- **ENV 1** : comme GD03.
- **Macros** : celles de GD03 ; MACRO 1 sur les deux quantités de FM.
- **Sub associé** : S01.
- **Test** : la note perçue doit rester la même d'un preset à l'autre ; vérifier à l'accordeur.
- **Origine** :
  - mode Ratio, SRC [cartographie, § 3.1 ; manuel] ;
  - rapports entiers = harmoniques [CALCUL, `../documentation-basses.md` § 1] ;
  - recette [ORIGINAL].

### GD10 Trois mouvements qui convergent
- **Patch** :
  - OSC A en carrée, OCT −2, Unison 3, detune lent. Distortion Overdrive à plusieurs étages.
  - LFO 2 (décroissant, Retrig, 1/4) → WT POS ; LFO 3 (triangle, 1 mesure) → filtre Reverb ; un mouvement aléatoire vient de l'unison à travers l'overdrive.
  - Les trois vitesses convergent et créent « de nouvelles dynamiques ».
  - Un LFO de plus baisse le MIX du filtre quand il devient trop aigu.
- **ENV 1** : ENV 1 → MIX et → DRIVE de la distorsion contre le clic ; ENV 2 (attaque ≈ 296 ms, sustain 50 %) ouvre un passe-bas.
- **FX** : chaîne de T10 de `dubstep-f11-tearout-metal.md`.
- **Macros** : `Talk` LFO 2 · `Snarl` étages de l'Overdrive · `Width` Hyper/Dimension · `Dry` LFO 3.
- **Sub associé** : S01.
- **Origine** : [SOURCE F13-03, Art1fact] : la convergence des trois mouvements crée de nouvelles dynamiques.

### GD11 Wub-growl — hybride
- **Patch** :
  - OSC A sur une table riche, OCT −2, RAND 0.
  - FILTER 1 en Formant-II vers FILTER 2 en MG Low 24 (en série).
  - LFO 1 (RETRIG, 1/8) → CUTOFF du formant (la parole) et → CUTOFF du passe-bas (le wub), même forme « swell / snap ».
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Overdrive après les filtres, Phaser 1/2, passe-haut à 120 Hz.
- **Macros** : `Talk` LFO 1 → formant · `Snarl` DRIVE · `Width` MIX du Phaser · `Dry` LFO 1 → passe-bas.
- **Sub associé** : S01.
- **Origine** :
  - forme « swell puis snap » et plage du wub [SOURCE F07-01] ;
  - LFO 1/8 sur le formant [SOURCE F08-04] ;
  - hybride [ORIGINAL]. Le tutoriel « Kompany growl wub » du registre (F07-21) n'est pas étudié.

### GD12 Fills de mid-bass — fragments en fin de phrase
- **Méthode** :
  1. Dupliquer la piste de basse.
  2. Figer et aplatir la copie (Freeze + Flatten).
  3. La traiter fort avec une distorsion tierce. La source utilise Rift ; le traitement natif de Live est exclu.
  4. Ne garder que des fragments, avec des fondus, surtout en fin de phrase.
- **Macros** : aucune ; travail en audio.
- **Sub associé** : la piste de sub reste intacte, jamais dupliquée dans les fills.
- **Jeu** : bloc « Dubstep 140 — fill de mid-bass » ci-dessous, en mesure 8.
- **Origine** : [SOURCE F01-08, EDMProd] : « mid basses et fills : dupliquer la piste sub, Freeze + Flatten, traiter fort, ne garder que des fragments en fondu ». Ici, on duplique la basse médium, pas le sub.

### GD13 Diffusor seul — growl « vocodé »
- **Patch** :
  - GD03 sans phasers, avec deux Filter Diffusor à la suite.
  - LFO 2 (1/4, RETRIG) → STAGES du premier.
  - Réduire le nombre d'étages si le son devient flou.
- **ENV 1** : comme GD03.
- **Macros** : `Talk` LFO 2 → STAGES · `Snarl` FM · `Width` — · `Dry` MIX du second Diffusor.
- **Sub associé** : S01.
- **Origine** :
  - « secret » : filtre FX de type diffuseur, effet proche du vocoder, dupliqué ; nombre d'étages réduit ensuite [SOURCE F08-01] ;
  - Diffusor, VAR = STAGES [cartographie, § 6].

### GD14 Filtre Reverb avant distorsion — growl creux
- **Patch** :
  - OSC A en carrée ou sur une table riche, OCT −2.
  - FILTER 2 en Reverb (catégorie Misc, VAR = DAMP), **avant** la distorsion.
  - LFO 3 (triangle, 1 mesure) → CUTOFF du filtre Reverb. Un second LFO baisse le MIX de ce filtre quand il devient trop aigu.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Overdrive, puis passe-bas sur LFO, puis Equalizer (passe-haut à 120 Hz).
- **Macros** : `Talk` LFO 3 · `Snarl` DRIVE · `Width` — · `Dry` MIX du filtre Reverb.
- **Sub associé** : S01.
- **Origine** : filtre 2 « Reverb » avant la distorsion, LFO 3 en triangle sur 1 mesure [SOURCE F13-03] ; filtre Reverb, VAR = DAMP [cartographie, § 6].

### GD15 Growl flou — Bode et BLUR
- **Patch** : GD01, plus un Bode en tête des derniers effets : BLUR monté, léger décalage, MIX ≈ 20 %.
  - Hyper/Dimension discret, Chorus avec mouvement sur son passe-bas, MIX ≤ 25 %.
- **ENV 1** : comme GD01.
- **Macros** : `Width` MIX du Bode · les autres comme GD01.
- **Sub associé** : S01.
- **Test** : en mono, le growl doit garder sa force ; le flou ne doit apparaître qu'en stéréo.
- **Origine** : Bode « = toute la stéréo », BLUR, ≈ 20 % ; « garder le mono puissant dans le patch, ajouter la stéréo après » [SOURCE F13-02].

### GD16 Sidechain interne — la bande grave du Multiband
- **Patch** : GD01, avec le Compressor en Multiband. Dans la matrice, LFO 6 (FREE, HOST, 1/2, creux bref au début du cycle) → gain de la bande basse (L) du compresseur.
  - La bande grave du growl s'efface sur le kick du temps 1 sans toucher aux médiums.
- **ENV 1** : comme GD01.
- **Macros** : `Dry` profondeur de LFO 6 · les autres comme GD01.
- **Sub associé** : S10, creux calé sur le kick.
- **Test** : le creux doit tomber sur le kick du temps 1 à chaque relance de la lecture.
- **Origine** :
  - « sidechain interne par bande via la matrice (dégager le grave pour un kick ou une basse) » [cartographie, § 8] ;
  - recette [DÉDUCTION].

### GD17 Growl granulaire — texture vocale
- **Patch** :
  - OSC A en moteur Granular, sur un sample de voix ou de growl imprimé (GD19).
  - DENS en BPM Sync (1/16), Jump Start activé, position de lecture (scan) sous LFO 1 (1/2, RETRIG).
  - OCT −1.
- **ENV 1** : attaque 5 ms, sustain 100 %, release 100 ms.
- **FX** : Distortion Overdrive, Equalizer (passe-haut à 150 Hz), Compressor Multiband.
- **Macros** : `Talk` LFO 1 → position · `Snarl` DRIVE · `Width` SPAWN PATTERN (presets) · `Dry` DENS.
- **Sub associé** : S01.
- **Origine** :
  - moteur Granular : DENS en Free, BPM Sync ou Grains, Jump Start [cartographie, § 3.5] ;
  - recette [DÉDUCTION, jamais essayée].

### GD18 Growl doublé à l'octave — brillance
- **Patch** : GD01, avec OSC C en copie d'OSC A (Shift-Option-glisser l'étiquette dans le mixer : copie avec modulations), OCT +1 par rapport à A, LEVEL 30-50 %.
  - OSC C passe par FILTER 2, en High 12 vers 300 Hz.
- **ENV 1** : comme GD01.
- **Macros** : `Width` LEVEL d'OSC C · les autres comme GD01.
- **Sub associé** : S01.
- **Test** : la copie doit ajouter de la présence sans dédoubler la voyelle. Si elle « parle » en décalé, couper ses LFO propres.
- **Origine** : copie d'oscillateur avec modulations par le mixer [cartographie, § 5] ; geste [ORIGINAL].

### GD19 Boucle de resampling — changer le rythme à chaque passe
- **Patch** : G16 de `house-f08-growl.md` au tempo du morceau dubstep.
  - Une note tenue de 2 à 4 mesures (de 3,4 à 6,9 s à 140 BPM), imprimée, remise dans un oscillateur, retravaillée.
  - Au plus 2-3 passes, avec un autre rythme de LFO à chaque passe.
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01.
- **Origine** : [SOURCE F08-04] ; durées [CALCUL].

### GD20 Growl en boucle de 3 temps — module Clip
- **Patch** :
  - GD01, joué par le module CLIP de Serum 2 : Mono + Bar + Retrig, Rate BPM.
  - Boucle de 3 temps contre la mesure en 4/4 : les accents du growl tournent contre le kick et la caisse claire.
  - Chance réduite sur les notes de passage.
- **ENV 1** : comme GD01.
- **Macros** : celles de GD01.
- **Sub associé** : S01, joué depuis Live sur les temps forts.
- **Test** : au bout de trois mesures, la boucle revient sur le temps 1. Imprimer la ligne ou la recopier dans Live pour garder le sub en phase.
- **Origine** : module Clip, boucle de 3 temps, Mono + Bar + Retrig, chance par note [SOURCE F15-01].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f08-growl.md`.

```grille
titre: Dubstep 140 — growl contre la caisse claire (GD01, GD06)
tempo: 140
accords: Fm7 | Fm7
growl: F1[1:3] F1[1a:1] Ab1[2&:2] Eb1[3e:2] F1[4:2] C2[4&:2] | F1[1:3] F1[1a:1] Ab1[2&:2] F1[3e:3] Eb1[4e:3]
sub: F0[1:3] F0[1a:1] Ab0[2&:2] Eb0[3e:2] F0[4:2] C1[4&:2] | F0[1:3] F0[1a:1] Ab0[2&:2] F0[3e:3] Eb0[4e:3]
```

Appel sur les temps 1-2, silence sur la caisse claire (double croche 9), réponse sur la fin du temps 3 et le temps 4.

```grille
titre: Dubstep 140 — growl tenu à la mesure (GD02, GD05)
tempo: 140
accords: Em7 | Em7
growl: E1[1:16] | E1[1:8] G1[3e:3] D1[4:4]
sub: E0[1:16] | E0[1:8] G0[3e:3] D0[4:4]
```

Une mesure tenue : les LFO à 1/1, 1/2, 1/4 et 1/8 de GD05 s'y entendent tous. La mesure 2 rend la place à la caisse claire.

```grille
titre: Dubstep 140 — fill de mid-bass (GD08, GD12)
tempo: 140
accords: Gm7 | Gm7
mid: G1[1:8] Bb1[3e:3] G1[4:2] | G1[1e:1] G1[1&:1] D2[1a:1] C2[2e:1] Bb1[2&:1] G1[2a:1] F1[3e:1] G1[3&:1] Bb1[3a:1] D2[4:1] G2[4e:3]
sub: G0[1:8] Bb0[3e:3] G0[4:2] | G0[1:8] F0[3e:3] G0[4:2]
```

Mesure 1 : tenue. Mesure 2 : fragments en doubles croches, puis le dive de GD08 sur le dernier sol. Le do est une note de passage vers le si bémol.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les filtres Formant, High Notch 12, Diffusor et Reverb ;
  - le module Bode, le moteur Granular, le mode Ratio et le module Clip ;
  - la modulation du gain des bandes du compresseur par la matrice.

  Vérifier les destinations des macros.
- Écouter chaque recette avec le sub, le kick et la caisse claire à 140 BPM, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
