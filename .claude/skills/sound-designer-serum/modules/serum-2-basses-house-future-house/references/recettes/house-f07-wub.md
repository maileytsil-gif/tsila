# Vingt recettes de wub et de wobble pour la House (famille F07)

Sixième lot de recettes House : le wub, une basse dont le filtre (ou le timbre) bat au rythme d'un LFO. On le trouve dans la Bass House, le UK Garage et la Future House ; il vient du dubstep. Rédigé le 05/10/2026. Sources :
- `../etudes-pages-house.md` (F07-01 Monosounds, F07-23 MusicRadar) et `../etudes-pages-dubstep-dnb.md` (F01-08 EDMProd, F02-14 MusicRadar) ;
- `../etudes-captures.md` (F01-08, F08-04) et `../etudes-videos.md` (F07-02, F10-01, F10-02) ;
- le Warping Bass d'Attack Magazine dans `../../../../references/patches-genres.md` ;
- la transcription Antidote Audio de `../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/references/sources-videos.md` ;
- la fiche 7 de `../families.md` et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes aux vingt recettes

1. **Sub indépendant et stable.** Le wobble reste au-dessus de 100 Hz environ ; le sub est un sinus séparé une octave plus bas, sur un oscillateur qui contourne le filtre ou sur sa propre piste [SOURCE F07-01].
   - Ici, sub de `house-f01-sub.md` sur sa piste (S01, ou S10 pour un creux calé sur le kick).
   - Equalizer du wub : passe-haut vers 100 Hz.
2. **LFO** :
   - Mode RETRIG pour un wub reproductible : il redémarre à chaque note, nécessaire pour les riffs courts (fiche 3 de `../../../../references/fiches-pratiques.md`).
   - Mode FREE avec HOST pour les wobbles tenus, calés sur la position du morceau [SOURCE F07-01 ; cartographie, § 7.2].
3. **Divisions** [SOURCE F07-01] : 1/4 pour le « slow lurch », 1/8 pour le « classic wub », 1/16 pour le « talking ».
   - Durées en ms [CALCUL, `../tempo-mix.md`] :
     - 1/4 = 483,9 ms à 124 BPM et 468,8 ms à 128 BPM ;
     - 1/8 = 241,9 ms et 234,4 ms ;
     - 1/8 pointée = 362,9 ms et 351,6 ms ;
     - 1/8 triolet = 161,3 ms et 156,3 ms ;
     - 1/16 = 121,0 ms et 117,2 ms.
4. **Plage du LFO** : du filtre fermé vers 150 Hz jusqu'à 1-2 kHz, plutôt que toute la course [SOURCE F07-01].
   - Forme : montée plus lente que la descente, « swell » puis « snap » ; un cran au milieu de la forme donne un bégaiement dans chaque wub.
5. **Grain** : distorsion **après** le filtre, puis EQ pour tenir 3-5 kHz. Retirer quelques dB vers 300-500 Hz si le son devient « boxy » [SOURCE F07-01].
6. **Quatre macros communes**, celles de la fiche 7 de `../families.md`, avec `Grit` en plus :
   - `Rate` : choix de division ;
   - `Depth` : quantité du LFO vers le filtre ;
   - `Vowel` : couleur (résonance, position de table, formant) ;
   - `Grit` : drive avec MIX en sens inverse.

   Une macro sur le RATE d'un LFO en BPM saute de division en division : c'est voulu. ECKA règle ainsi une macro « Rate » [SOURCE F10-02]. Vérifier le « + » sur chaque destination.
7. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`). Le sidechain de la couche wobble au kick passe par un plug-in tiers ou le creux de S10.
8. **Contrôle par l'utilisateur** :
   - le wub seul, puis avec son sub, puis avec le kick ;
   - mono ;
   - les deux bornes de `Rate` et `Depth` ;
   - une note grave et une aiguë (la plage du filtre doit suivre) ;
   - lecture lancée depuis plusieurs mesures, pour les LFO en FREE ;
   - A/B à niveau égal contre W01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| W01 | Wobble de référence | Bass House | LFO 1/4 sur passe-bas, 150 Hz → 2 kHz |
| W02 | Classic wub et grain FM | Bass House | même LFO sur filtre et FM |
| W03 | Talking 1/16 bégayant | Bass House | cran dans la forme |
| W04 | Wobble à division variable | Bass House, build | macro `Rate` 1/4 → 1/8 → 1/16 |
| W05 | Main Sub UK ramenée en médium | Bass House, UK Bass | carré, 1/8 pointée, peigne |
| W06 | Wubber à l'enveloppe | Bass House | ENV 1 sur la coupure, sans LFO |
| W07 | Wub en triolets | Future House | 1/8 triolet, SMOOTH 50 |
| W08 | Warping Bass 3/16 | Bass House | filtre en série, 1/8 pointée |
| W09 | Wobble AM qui suit la note | Bass House | modulateur à −4 octaves |
| W10 | Wobble morphé d'une mesure | Tech House, Bass House | L/B/H 24, LFO 1 mesure |
| W11 | Wub vocal | Bass House | formant à 1/4 |
| W12 | Wub « yoi » | Bass House | WT POS en 1/4 triolet |
| W13 | Bouche lente | Bass House, breakdown | WT POS en 1/1 |
| W14 | Wobble tenu calé sur le transport | Bass House | FREE + HOST |
| W15 | Wobble UKG | UK Garage, Speed Garage | carrée et scie, 1/8 en marches |
| W16 | Wobble au peigne | Bass House | Cmb HL6− balayé |
| W17 | Wobble en samples | Bass House, DnB | trois oscillateurs Sample |
| W18 | Wobble phaser | Bass House | Phaser synchronisé |
| W19 | Séquence de wubs dessinée | Bass House | LFO d'une mesure en marches |
| W20 | Wobble ressamplé | toutes | 2-3 passes d'impression |

## Les vingt recettes

### W01 Wobble de référence
- **Patch** :
  - OSC A en scie, OCT −1, Unison 1 (option : 2-3 voix), RAND 0.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 200 Hz, RES 15-25 %.
  - LFO 1 → CUTOFF, plage de 200 Hz à 1-2 kHz : BPM, 1/4, RETRIG. Forme : montée lente (70 % du cycle), descente rapide.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60-120 ms.
- **FX** :
  1. Distortion Tube après le filtre, DRIVE 20-40.
  2. Equalizer : passe-haut à 100 Hz, −3 dB vers 3-5 kHz.
- **Macros** : `Rate` RATE de LFO 1, 1/4 → 1/16 · `Depth` LFO 1 → CUTOFF 0 → 100 % · `Vowel` RES 0 → 40 % · `Grit` DRIVE 0 → 60 (MIX en sens inverse).
- **Sub associé** : S01 ou S10.
- **Jeu** : bloc wub de `../motifs.md` (tenues de six doubles croches après le kick).
- **Origine** :
  - scie une octave plus bas, passe-bas vers 200 Hz, LFO 1/4, plage 150 Hz-2 kHz, forme « swell / snap », retrigger, distorsion après filtre, EQ 3-5 kHz [SOURCE F07-01, page] ;
  - type de filtre non nommé par la page : MG Low 24 [ORIGINAL].

### W02 Classic wub et grain FM
- **Patch** : W01, avec un grain FM en plus.
  - OSC B en sinus, une ou deux octaves **sous** A (OCT −2 ou −3), LEVEL 0, `None`.
  - WARP 1 d'OSC A en FM (B), base 5 %.
  - LFO 1 à 1/8 → CUTOFF et → WARP 1 (+20 à +40 %).
- **ENV 1** : comme W01.
- **FX** : comme W01. Passe-haut à 100 Hz, car le modulateur grave ajoute une composante continue (`house-f03-pluck-hollow.md`, règle 3).
- **Macros** : `Rate` 1/8 → 1/16 · `Depth` LFO 1 → CUTOFF · `Vowel` LFO 1 → WARP 1, 0 → 50 % · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - « grain par FM : sinus sur Osc B, une ou deux octaves plus bas, en FM vers A ; le même LFO pilote cutoff et quantité de FM » ; un LFO vers deux ou trois cibles [SOURCE F07-01] ;
  - quantités [ORIGINAL].

### W03 Talking 1/16 bégayant
- **Patch** : W01, avec LFO 1 en 1/16 et une forme à cran : un petit plateau ou une petite remontée au milieu de la descente.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : comme W01, plus Compressor Multiband à gain modéré.
- **Macros** : `Rate` 1/8 → 1/32 · `Depth` · `Vowel` profondeur du cran (point du LFO modulé par un bus de LFO) · `Grit`.
- **Sub associé** : S10.
- **Origine** :
  - 1/16 pour le « talking » ; « un petit cran au milieu de la forme donne un bégaiement dans chaque wub » [SOURCE F07-01] ;
  - modulation des points par bus de LFO [cartographie, § 7.2].

### W04 Wobble à division variable — de 1/4 à 1/16
- **Patch** : W01, plus une macro `Rate` (MACRO 1) assignée au RATE de LFO 1, bornes de 1/4 à 1/16. Dans Live, automatiser la macro sur une phrase : 1/4 pendant deux mesures, 1/8 pendant une, 1/16 sur la dernière.
- **ENV 1** : comme W01.
- **Macros** : `Rate` 1/4 → 1/16 · `Depth` · `Vowel` · `Grit`.
- **Sub associé** : S01.
- **Jeu** : bloc « Bass House 126 — tenues à division variable » ci-dessous.
- **Test** : le saut de division doit tomber sur un temps. Si l'automation passe la frontière en cours de cycle, avec HOST le LFO saute pour rester calé sur la mesure : écouter si le saut gêne.
- **Origine** :
  - automatiser 1/4 → 1/8 → 1/16 sur une phrase [SOURCE F07-01] ;
  - macro « Rate » sur le rate du LFO [SOURCE F10-02] ;
  - comportement de HOST [cartographie, § 7.2].

### W05 Main Sub UK ramenée en médium
- **Patch** :
  - OSC A sur BSOD_Square (table de Serum 1, la « variation de carré » ; à retrouver), OCT 0 (une octave plus haut que la Main Sub d'origine), Unison 1, RAND 0.
  - OSC B en sinus, OCT +2, LEVEL 0 ; WARP 1 d'OSC A en FM (B), base 10 %.
  - FILTER 1 en MG Low 24 (MG Low 12 sur la première capture).
  - LFO 1 → CUTOFF : forme en arche (« Dome »), TRIG, BPM, DOT, 1/8 pointée, trois destinations.
- **ENV 1** : 0,5 ms / 0 / 1,00 s / 0 dB / 20 ms. VOICING MONO + LEGATO.
- **FX** :
  1. Hyper : UNISON 3, MIX ≈ 28 %. Dimension : MIX près de 0.
  2. Distortion Sine Shaper, filtre OFF, DRIVE ≈ 17 % (modulé par la macro 3).
  3. Filter Cmb HL6+, HL WID ≈ 90 %, RES ≈ 33 %.
  4. Equalizer : passe-haut à 100 Hz, creux de 3 dB vers 240 Hz.
- **Macros** (schéma de la source) : `Depth` = MACRO 1 sur CUTOFF · `Vowel` = MACRO 2 sur la FM · `Grit` = MACRO 3 sur le DRIVE **et** le MIX de la distorsion, le MIX en sens inverse pour un volume à peu près constant · `Rate` 1/8 pointée → 1/16.
- **Sub associé** : S01. La Main Sub d'origine porte FM, distorsion et peigne dans le grave, ce que la règle « Grave » interdit : ici le grave passe au sub.
- **Tempo** : la source est à 140 BPM. La 1/8 pointée y dure 321,4 ms ; à 128 BPM, 351,6 ms [CALCUL].
- **Origine** :
  - [SOURCE F01-08, page et captures, Serum 1, dubstep UK] ;
  - l'EQ de la source était l'EQ Eight de Live (effet natif, règle 5) : remplacé par l'Equalizer de Serum.
  - Écran de cet EQ : +3,1 dB à 2,02 kHz ; creux de −10 dB vers 150-160 Hz, rendu inutile par le passe-haut.

### W06 Wubber à l'enveloppe — sans LFO
- **Patch** :
  - OSC A, éditeur de wavetable : un sinus retravaillé (harmoniques 2 à 6 ajoutés à faible niveau).
  - FILTER 1 en MG Low 24, CUTOFF ≈ 20 %.
  - ENV 1 → CUTOFF : +50 à +70 %, attaque 40-120 ms, decay 150-300 ms, sustain 30 %. Chaque note fait un seul « wub » qui s'ouvre puis retombe.
- **ENV 1 (amplitude)** : attaque 5 ms, sustain 100 %, release 80 ms (la même enveloppe module le filtre).
- **FX** : Distortion Tube DRIVE 40, puis Compressor Multiband : ils font ressortir les harmoniques. Puis passe-haut à 100 Hz.
- **Macros** : `Rate` attaque d'ENV 1 20 → 200 ms · `Depth` ENV 1 → CUTOFF 0 → 80 % · `Vowel` niveau des harmoniques (WT POS si plusieurs frames) · `Grit` DRIVE.
- **Sub associé** : S01.
- **Jeu** : question courte, réponse longue : la longueur de la note décide du wub.
- **Origine** :
  - « départ sinus modifié par éditeur d'harmoniques ; distorsion et multibande révèlent les harmoniques ; ENV 1 pilote cutoff et forme le wub » [SOURCE Antidote Audio « Savage Bass House Basses », transcription] ;
  - valeurs [ORIGINAL].

### W07 Wub en triolets — Future House
- **Patch** :
  - OSC A en scie, OCT −1, Unison 2, DETUNE 0,10, RAND 0.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 30 %.
  - LFO 1 → CUTOFF : BPM, 1/8 avec TRIP, SMOOTH 50, RETRIG, forme dessinée (montée rapide, descente lente).
  - LFO 2 → WT POS, 1/2.
- **ENV 1** : attaque 2 ms, decay 400 ms, sustain −4 dB, release 80 ms.
- **FX** : passe-haut à 120 Hz, à cause de l'unison.
- **Macros** : `Rate` 1/8T → 1/16T · `Depth` LFO 1 → CUTOFF · `Vowel` LFO 2 → WT POS · `Grit` DRIVE d'une Distortion Soft Clip.
- **Sub associé** : S10, un creux par noire, sous le rebond en triolets.
- **Origine** : LFO 1 1/8 TRIP SMOOTH 50 → cutoff, LFO 2 1/2 → WT POS [SOURCE Attack Magazine, Beat-Pulsing Plucks, `patches-genres.md`] ; usage en wub [ORIGINAL].

### W08 Warping Bass 3/16 — filtre en série
- **Patch** (transposition de Massive) :
  - OSC A en scie riche, LEVEL 50 %, WARP 1 en Bend +/− modulé lentement.
  - OSC B en carrée-scie, OCT −2.
  - OSC C en sinus, OCT −2, WT POS ≈ 60 % si c'est une table, sinon sinus pur.
  - FILTER 1 en MG Low 24 (le « Daft »), CUTOFF ≈ 25 %, RES ≈ 25 %, sortie vers FILTER 2 (en série).
  - FILTER 2 en Combs, CUTOFF ≈ 30 %.
  - LFO 1 → CUTOFF de FILTER 1 : un quart de course, BPM, 1/8 pointée (= 3/16).
  - VOICING MONO, PORTA ≈ 30 % de la course, RETRIG de chaque note.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 60 ms.
- **FX** : Hyper/Dimension MIX 50 %, Reverb MIX ≈ 30 % avec LO CUT haut ; hors Serum, coupe-bas et distorsion multibande sur médiums et aigus seulement.
- **Registre** : B et C à −2 descendent dans le sub. Monter le patch d'une octave, ou couper C, et laisser le grave à S01.
- **Macros** : `Rate` 3/16 → 3/32 · `Depth` LFO 1 → CUTOFF · `Vowel` CUTOFF du Combs · `Grit` quantité du Bend.
- **Sub associé** : S01.
- **Origine** :
  - Warping Bass : LFO 5 → cutoff du filtre 1, un quart de course, Sync 3/16, routage série, Comb ≈ 30 %, Glide ≈ 30 %, Dimension 50 %, reverb 30 %, distorsion multibande médiums et aigus [SOURCE Attack Magazine, Massive, `patches-genres.md`] ;
  - « le LFO synchronisé en 3/16 crée un déphasage rythmique contre un kick en 4/4 » [ibid., `[I]`].

### W09 Wobble AM qui suit la note
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - OSC B en sinus, OCT −4 (−3 au besoin), LEVEL 0, pitch tracking allumé.
  - WARP 1 d'OSC A en AM (B), 30-60 %. ENV 2 → ce warp, attaque lente (300-800 ms), sustain 100 % : le wobble s'installe au cours de la note.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 50 %.
- **Vitesse** : quatre octaves sous A, B bat à f/16 [CALCUL] :
  - Fa1 (87,3 Hz) → 5,5 Hz ;
  - Fa2 (174,6 Hz) → 10,9 Hz.

  La vitesse du wobble suit la note jouée.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion légère, passe-haut à 100 Hz.
- **Macros** : `Rate` OCT de B −3 → −5 · `Depth` quantité de l'AM 0 → 80 % · `Vowel` attaque d'ENV 2 · `Grit` DRIVE.
- **Sub associé** : S01.
- **Test** : sur deux notes à une octave d'écart, le wobble doit doubler de vitesse ; vérifier qu'il reste musical sur la note la plus aiguë.
- **Origine** :
  - AM par un sinus, enveloppe à attaque lente sur le warp, « imite le changement de vitesse des wobbles old-school selon la note jouée » [SOURCE F02-14, page, Serum 1] ;
  - l'octave −4 pour un battement sous-audio [DÉDUCTION, jamais essayée].

### W10 Wobble morphé d'une mesure
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0. FILTER 1 éteint.
  - Rack FX : Filter en L/B/H 24, CUTOFF ≈ 300 Hz, RES ≈ 50 %, DRIVE et MORPH ≈ 30 %.
  - LFO 1 (1 mesure, RETRIG) → CUTOFF +10 et → MORPH −20.
  - Puis Compressor, attaque et release 50-60 ms, environ 4 dB de réduction.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : après le compresseur, Distortion légère (Tube plutôt que le Downsample de P14), puis passe-haut à 100 Hz.
- **Macros** : `Rate` RATE de LFO 1, 2 mesures → 1/4 · `Depth` LFO 1 → CUTOFF · `Vowel` LFO 1 → MORPH · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - chaîne et quantités [SOURCE F07-23, page MusicRadar, Serum FX] ;
  - P14 de `house-f05-saw-percussive.md` en tire une basse sale ; ici, un wobble lent [ORIGINAL].

### W11 Wub vocal — formant à 1/4
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - FILTER 1 en Formant-II, RES 20-35 %.
  - LFO 1 → CUTOFF (qui morphe entre formants) : BPM, 1/4, RETRIG, forme montée-descente.
  - Variante « bégaiement » : 1/8 avec peu de profondeur.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion après le filtre, Equalizer (creux sur les pics nasaux, passe-haut à 100 Hz).
- **Macros** : `Rate` 1/4 → 1/8 · `Depth` LFO 1 → CUTOFF · `Vowel` VAR (FORMNT) · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - 1/4 « steady syllables » sur la coupure du formant ; 1/8 « fast stutter », faible profondeur [SOURCE F08-04, infographie Monosounds] ;
  - type de formant [ORIGINAL]. Le growl complet relève de F08.

### W12 Wub « yoi » — WT POS en 1/4 triolet
- **Patch** :
  - OSC A sur une table de voyelles (catégorie Vowel de Serum 2) ou une table spectrale, OCT −1, RAND 0.
  - LFO 1 → WT POS : BPM, 1/4 avec TRIP, RETRIG, forme en bosse.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 60 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Diode 2 légère, passe-haut à 100 Hz.
- **Macros** : `Rate` 1/4T → 1/8T · `Depth` LFO 1 → WT POS · `Vowel` WT POS de base · `Grit` DRIVE.
- **Sub associé** : S10.
- **Origine** :
  - « 1/4 triplet : the yoi-yoi bounce », sur WT Position [SOURCE F08-04, infographie] ;
  - table de voyelles (catégorie Vowel) vue dans l'étude de F10-01 [SOURCE F10-01] ;
  - le yoi complet relève de F09 (lot Dubstep).

### W13 Bouche lente — WT POS en 1/1
- **Patch** : W12, avec LFO 1 → WT POS en 1/1, forme en arche, mode FREE avec HOST.
- **ENV 1** : attaque 5 ms, sustain 100 %, release 150 ms.
- **FX** : Reverb Plate (MIX ≤ 10 %, LO CUT haut), passe-haut à 100 Hz.
- **Macros** : `Rate` 1/1 → 1/2 · `Depth` · `Vowel` · `Grit`.
- **Sub associé** : S12 (glissé), dans un breakdown.
- **Origine** : « 1/1 : slow mouth open-close », sur WT Position [SOURCE F08-04, infographie] ; usage en breakdown [ORIGINAL].

### W14 Wobble tenu calé sur le transport
- **Patch** : W01, avec LFO 1 en mode FREE, HOST allumé, MONO allumé (un seul LFO pour toutes les voix).
- **ENV 1** : attaque 2 ms, sustain 100 %, release 120 ms. VOICING MONO + LEGATO : les notes liées ne redémarrent pas le LFO.
- **Macros** : celles de W01.
- **Sub associé** : S10, calé lui aussi sur le transport.
- **Jeu** : notes longues liées sur deux mesures ; le wobble ne repart pas à chaque note.
- **Test** : lancer la lecture à la mesure 1, puis à la mesure 3 : le wobble doit tomber au même endroit de la grille.
- **Origine** :
  - « free-running (ou calé sur la position du morceau) pour les wobbles tenus » [SOURCE F07-01] ;
  - HOST : la phase est recalculée depuis le transport [cartographie, § 7.2].

### W15 Wobble UKG — carrée et scie en marches
- **Patch** :
  - OSC A en carrée, OCT −1, RAND 0. OSC B en scie, même octave, LEVEL 40 %.
  - FILTER 1 sur A et B, MG Low 24, CUTOFF ≈ 25 %, RES 20 %.
  - LFO 1 → CUTOFF : BPM, 1 mesure, RETRIG, forme en marches (Shift-clic, grille 8) qui ouvre le filtre sur certaines croches seulement.
  - SMOOTH 10-20 pour adoucir les marches.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 50 ms.
- **FX** : Distortion Soft Clip, Compressor Single, passe-haut à 100 Hz.
- **Macros** : `Rate` 1 mesure → 1/2 · `Depth` LFO 1 → CUTOFF · `Vowel` RES · `Grit` DRIVE.
- **Sub associé** : S01, en 2-step avec le kick.
- **Jeu** : bloc « UK Garage 132 — wobble en 2-step » ci-dessous.
- **Origine** : [ORIGINAL]. Les tutoriels UKG du registre (F07-06, F07-08) ne sont pas étudiés.

### W16 Wobble au peigne — Cmb HL6− balayé
- **Patch** :
  - OSC A en carrée, OCT −1, RAND 0.
  - Rack FX : Distortion Diode 2 avant le peigne, puis Filter Cmb HL6−, CUTOFF ≈ 110 Hz, RES 40-60 %, HL WID à l'oreille.
  - LFO 2 (1/4, RETRIG) → CUTOFF du peigne ≈ +30 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : passe-haut à 120 Hz après le peigne.
- **Macros** : `Rate` RATE de LFO 2 · `Depth` LFO 2 → CUTOFF du peigne · `Vowel` HL WID · `Grit` DRIVE de la Diode 2.
- **Sub associé** : S01.
- **Origine** :
  - « le plus important » : filtre Cmb HL6−, coupure ≈ 110 Hz, LFO 2 → coupure 30 %, résonance, HL WID à l'oreille, Diode 2 drive au maximum avant [SOURCE F10-01, riddim, Serum 2] ;
  - Cmb HL6+ dans la Main Sub [SOURCE F01-08] ;
  - usage en Bass House [ORIGINAL]. Le riddim complet relève de F10 (lot Dubstep).

### W17 Wobble en samples — trois oscillateurs Sample
- **Patch** :
  - OSC A, B et C en moteur Sample, avec des samples d'usine de Serum 2 : A « True Kora » en one-shot (attaque), B « Brass Wall Low » (couche haute), C « Upright Short » (couche grave, bouclée sur une zone stable avec crossfade).
  - FILTER 1 sur A et B, High 18 (lecture incertaine) : C reste propre.
  - LFO 1 → CUTOFF : RETRIG, forme décroissante, 1/4.
  - NOISE en White ; warp de C en FM (Noise) pour des aigus « craquants ».
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **FX** : Distortion tout de suite, puis Compressor Multiband, puis Filter final pour le mouvement, puis passe-haut à 100 Hz [ORIGINAL].
- **Macros** : `Rate` RATE de LFO 1 · `Depth` LFO 1 → CUTOFF · `Vowel` LEVEL de B · `Grit` DRIVE.
- **Sub associé** : S01. L'auteur dit qu'en pratique il mettrait un sinus en sub sur A.
- **Tempo** : la source est à 174 BPM. À 128, 1/4 = 468,8 ms contre 344,8 ms : le mouvement est plus lent ; essayer 1/8 [CALCUL].
- **Origine** : [SOURCE F07-02, transcription et trois captures, Serum 2, DNB Academy]. Le « wobble » du titre n'y est pas détaillé.

### W18 Wobble phaser
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0. FILTER 1 en MG Low 12, CUTOFF ≈ 45 %, fixe.
  - Rack FX : Phaser, BPM, RATE 1/8, POLES 6-8, FEEDBACK 40-60 %, FREQ 400-800 Hz, MIX 50-70 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Soft Clip avant le Phaser, passe-haut à 100 Hz.
- **Macros** : `Rate` RATE du Phaser 1/8 → 1/16 · `Depth` DEPTH du Phaser · `Vowel` FEEDBACK · `Grit` DRIVE.
- **Sub associé** : S01.
- **Limite** : le module d'effet n'est pas redéclenché par la note (les effets travaillent sur la somme des voix), donc le wobble ne repart pas à chaque note. W01 est mieux pour des riffs courts.
- **Origine** :
  - Phaser (RATE BPM, POLES, FEEDBACK, FREQ) ; « les effets travaillent sur la somme des voix » [cartographie, § 8] ;
  - « 1/16 : buzzy texture, use rarely », sur le rate du phaser [SOURCE F08-04, infographie] ;
  - valeurs [ORIGINAL].

### W19 Séquence de wubs dessinée
- **Patch** :
  - W01, avec LFO 1 → CUTOFF sur 1 mesure, RETRIG, forme dessinée : deux wubs de croche, quatre de double croche, une ouverture longue sur le dernier temps.
  - GRID X 16, outils Ramp Up et Ramp Down (cartographie, § 7.2).
  - SMOOTH 5-15.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **Macros** : `Rate` 2 mesures → 1/2 (la séquence se joue plus lentement ou plus vite) · `Depth` · `Vowel` · `Grit`.
- **Sub associé** : S10.
- **Jeu** : une note tenue d'une mesure : le rythme vient de la forme, pas du MIDI.
- **Origine** : outils de dessin du LFO [cartographie, § 7.2] ; geste [ORIGINAL].

### W20 Wobble ressamplé — deux ou trois passes
- **Patch** :
  1. Construire W01, W05 ou W11, avec ses effets.
  2. Imprimer une note tenue de 2 à 4 mesures, effets compris.
  3. La ramener dans Serum 2 : glisser le WAV sur un oscillateur, ou Resample to.
  4. Retravailler : nouveau warp, nouveau formant, nouveaux effets, autre forme et autre vitesse de LFO à chaque passe.
  5. S'arrêter après 2 ou 3 passes : « more passes add mud, not character ».
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01, jamais ressamplé avec le wobble.
- **Test** : A/B entre la passe 1 et la passe 3 à niveau égal.
- **Origine** :
  - boucle « The Resample Loop » [SOURCE F08-04, infographie Monosounds] ;
  - imprimer plusieurs minutes d'un riff et garder les meilleures prises [SOURCE F02-14] ;
  - procédure d'impression : `../../../resampling/GUIDE.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60). Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f07-wub.md`. Le bloc « Bass House 128 — wub tenu après le kick » de `../motifs.md` complète ces trois motifs.

```grille
titre: Bass House 126 — tenues à division variable (W04, W14)
tempo: 126
accords: Gm7 | Gm7
wub: G1[1&:6] G1[3&:6] | Bb1[1&:6] F1[3&:2] G1[4&:2]
sub: G0[1&:6] G0[3&:6] | Bb0[1&:6] F0[3&:2] G0[4&:2]
```

Automatiser `Rate` : 1/4 sur la mesure 1, 1/8 sur la première moitié de la mesure 2, 1/16 sur la fin. Les tenues recouvrent le kick suivant : creux de S10 ou sidechain par plug-in tiers.

```grille
titre: Bass House 128 — tenues pour la 1/8 pointée (W05, W08)
tempo: 128
accords: Em7 | Em7
wub: E1[1e:7] B1[3e:3] D2[4&:2] | E1[1e:7] G1[3e:3] E1[4&:2]
sub: E0[1e:7] B0[3e:3] D1[4&:2] | E0[1e:7] G0[3e:3] E0[4&:2]
```

Une 1/8 pointée (351,6 ms) tombe deux fois dans la tenue de sept doubles croches (820 ms) : le wub se décale contre le kick, comme le 3/16 du Warping Bass.

```grille
titre: UK Garage 132 — wobble en 2-step (W15)
tempo: 132
accords: Fm7 | Fm7
wob: F1[1:4] Ab1[2&:2] F1[3e:3] Eb1[4&:2] | F1[1:4] C2[2&:2] Ab1[3e:3] Eb1[4&:2]
sub: F0[1:4] Ab0[2&:2] F0[3e:3] Eb0[4&:2] | F0[1:4] C1[2&:2] Ab0[3e:3] Eb0[4&:2]
```

En 2-step, le kick n'est pas sur les quatre temps : la basse attaque avec le kick du temps 1. Recaler les autres attaques sur le vrai pattern de batterie.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : la table BSOD_Square, les samples True Kora, Brass Wall Low et Upright Short, les filtres Cmb HL6+ et HL6−, L/B/H 24 et Formant-II. Vérifier qu'une macro sur le RATE d'un LFO passe bien de division en division.
- Écouter chaque recette avec son sub, puis avec le kick, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
