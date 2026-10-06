# Vingt recettes de growl pour la House (famille F08)

Septième lot de recettes House : le growl, une basse médium qui « parle » par ses voyelles, son grain FM et sa distorsion. En Bass House il répond au kick et au stab ; le genre l'a pris au dubstep et à la DnB, d'où viennent la plupart des tutoriels. Rédigé le 05/10/2026. Sources :
- `../etudes-pages-dubstep-dnb.md` (F08-04 Monosounds, F08-17 ADSR) ;
- `../etudes-captures.md` (F08-04) et `../etudes-videos.md` (F08-01 Holo Rival, F08-02 Konstricta, F08-03 DNB Academy, F13-02 Art1fact) ;
- la talking bass du corpus `../../../house-future-rave-bass-house-production/recipes/talking-bass-formants.md` ;
- le § 3 « Neuro / growl » de `../../../sound-designer-serum/references/basses.md` ;
- la transcription Sam Smyers de `../../../composer-hooks-funk-electro/references/sources-videos.md` ;
- la fiche 8 de `../families.md`, `../documentation-basses.md` § 2 (formants) et la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes aux vingt recettes

1. **Le growl vit dans les médiums, de 150 Hz à 2 kHz.** Le sub reste une couche séparée, intacte, **hors de la distorsion**.
   - Passe-haut du growl vers 120-150 Hz.
   - Un growl « maigre » manque presque toujours de son sub [SOURCE F08-04].
   - Sub de `house-f01-sub.md` sur sa piste : S01, S07 ou S10.
2. **Hauteur** : la plupart des tutoriels jouent à OCT −3 en dubstep à 140-150 BPM. En Bass House, monter d'une octave (−2) pour que la fondamentale du growl tombe au-dessus du passe-haut, et laisser le grave au sub.
3. **Trois couches de mouvement vocalique**, chacune avec sa propre source [SOURCE F08-04] :
   - WT POS ;
   - warp : Bend 30-50 % pour un « nasal snarl », FM 15-25 % pour une râpe gutturale, au-delà de 40 % métallique et criard ;
   - filtre formant, résonance 20-40 % (plus haut, ça siffle), petite amplitude : « oh » → « ah » est un petit mouvement.
4. **Rythmes des LFO** [SOURCE F08-04, page et infographie] :
   - 1/2 : mouvement principal ;
   - 1/8 : syllabes, faible profondeur ;
   - 1/4 triolet : rebond « yoi » ;
   - 1/16 : texture, plus de parole.
   - Mode Trigger (RETRIG) pour un growl reproductible (fiche 3 de `../../../sound-designer-serum/references/fiches-pratiques.md`).
5. **Ordre des effets** : mouvement de filtre → distorsion → compression → EQ → phaser ou flanger. Distorsion **avant** phaser, sinon « fizz » [SOURCE F08-04 ; `basses.md` § 3].
6. **RAND à 0** sur chaque oscillateur, « so it stays consistent » [SOURCE F08-02].
7. **Quatre macros communes**, celles de la fiche 8 de `../families.md` :
   - `Talk` : formant ou WT POS ;
   - `Snarl` : FM ou drive ;
   - `Width` : effets de largeur ;
   - `Dry` : mix général des effets.

   Vérifier le « + » sur chaque destination.
8. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
9. **Contrôle par l'utilisateur** :
   - le growl seul, puis avec son sub, puis avec le kick et le stab ;
   - mono ;
   - les deux bornes de `Talk` et `Snarl` ;
   - la note la plus aiguë (le repliement des FM fortes s'y entend d'abord, `../documentation-basses.md` § 4) ;
   - faible volume ;
   - A/B à niveau égal contre G01.
   - En Bass House, laisser un silence avant chaque réponse (fiche 8 de `../families.md`).

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| G01 | Growl Monosounds | Bass House, référence A/B | Bend, FM 1:0,5, formant, Overdrive → Phaser |
| G02 | Trois voyelles décalées | Bass House | LFO à 1/2, 1/8 et 1/4 triolet |
| G03 | Growl Konstricta | Bass House, dubstep | trois oscillateurs, LFO à la mesure, High Notch 12 |
| G04 | Chaîne FM de sinus | Bass House lourde | FM C → B → A, Diffusor, OTT ×3 |
| G05 | Growl DNB Academy | Bass House, DnB | PD (B), Rectify, Diffusor, Phs 36+ |
| G06 | Patch BassGorilla | Bass House | High Notch 12 à 141 Hz, LFO inversé |
| G07 | Talking bass | Bass House | Formant I entre « oh » et « ah » |
| G08 | Growl Sam Smyers | Deep Bass House | unison 7, multibande puis Tube |
| G09 | Growl façon Skrillex | Bass House | WT POS sur une mesure, passe-bande |
| G10 | Growl en réponse | Bass House | LFO Envelope, silence avant |
| G11 | Râpe FM | Bass House | FM 15-25 % depuis une octave plus bas |
| G12 | Growl spectral | Bass House | partiels coupés et glissés |
| G13 | Growl de sa propre voix | Bass House | WAV « yah-woh-yoi » en table |
| G14 | Double warp | Bass House | FM (B) + Diode sur la même table |
| G15 | Phaser qui parle | Bass House | LFO sur le feedback du phaser |
| G16 | Growl ressamplé | toutes | 2-3 passes, rythme changé |
| G17 | Growl métallique au peigne | Bass House | Combs + Diode |
| G18 | Growl à hauteur mouvante | Bass House | LFO sur Main Tuning |
| G19 | Growl en LFO Path | Bass House | sorties X et Y d'un même tracé |
| G20 | Growl mono, largeur en post | toutes | Splitter M/S, côtés au-dessus de 300 Hz |

## Les vingt recettes

### G01 Growl Monosounds — référence de la famille
- **Patch** :
  - OSC A : table d'usine qui « parle » déjà sans traitement (balayer WT POS), OCT −2, Unison 1, LEVEL ≈ 75 %, RAND 0.
  - WARP 1 en Bend +/−, 30-50 %.
  - OSC B en sinus, une octave sous A, LEVEL 0, `None`. WARP 2 d'OSC A en FM (B), 15-25 %.
  - FILTER 1 en Formant-I (ou II, III), RES 20-40 %.
  - LFO 1 : forme dessinée, 3-4 marches à hauteurs différentes, chutes courbes, 1/2, RETRIG. Il va vers WT POS, vers la quantité du Bend (à la moitié de la profondeur) et vers le CUTOFF du formant (petite plage).
  - LFO 2 en 1/8, faible profondeur, → CUTOFF du formant.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms. La page n'en donne pas : [ORIGINAL].
- **FX, dans l'ordre** :
  1. Distortion Overdrive, DRIVE 40-60 %.
  2. Phaser, RATE 1/2 synchronisé, FEEDBACK 60 %, MIX 50 %.
  3. Equalizer : passe-haut à 120 Hz, creux de 3 dB vers 400 Hz.
  4. Compressor Multiband, bande 2-5 kHz calmée.
  5. Hyper/Dimension, MIX 15-25 %.
- **Macros** : `Talk` LFO 1 → CUTOFF du formant 0 → 30 % · `Snarl` WARP 2 (FM) 10 → 45 % · `Width` MIX de l'Hyper 0 → 30 % · `Dry` MIX de la Distortion 50 → 100 %.
- **Sub associé** : S01 ou S10.
- **Jeu** : bloc « Bass House 128 — stab et growl en réponse » de `../motifs.md`.
- **Origine** : toutes les valeurs [SOURCE F08-04, page, Serum 2] ; « la plus chiffrée du lot pour un growl Serum 2 ».

### G02 Trois voyelles décalées
- **Patch** : G01, avec trois LFO distincts, chacun en RETRIG :
  - LFO 1 en 1/2 → WT POS (mouvement principal) ;
  - LFO 2 en 1/8, faible profondeur → CUTOFF du formant (syllabes) ;
  - LFO 3 en 1/4 avec TRIP → quantité du Bend (rebond « yoi »).
- **ENV 1** : comme G01.
- **Macros** : `Talk` profondeur de LFO 2 · `Snarl` profondeur de LFO 3 · `Width` · `Dry`, comme G01.
- **Sub associé** : S10.
- **Test** : les trois mouvements doivent se distinguer. Si le son « bave », baisser LFO 3 en premier.
- **Origine** : « trois couches de mouvement vocalique, chacune pilotée par une source légèrement différente » ; FAQ 1/2, 1/8, 1/4 triolet [SOURCE F08-04].

### G03 Growl Konstricta — trois oscillateurs à la mesure
- **Patch** :
  - **OSC A** : table propre pour la FM (« BAS plug », nom incertain, à retrouver), OCT −3 (−2 en House), RAND 0.
    - LEVEL à 0 %, et LFO 1 → LEVEL : les pentes dessinées font le contour d'amplitude de A dans la mesure.
    - WARP 1 en Bend −, LFO 2 dessus. WARP 2 en PD (B), LFO 3 dessus.
  - **OSC B** : table « Monster » d'usine, OCT −3 (−2), RAND 0, WT POS au milieu, LFO 3 → WT POS. Warp Asym −, LFO 2 dessus.
  - **OSC C** : table vocale (« softest growl », nom incertain), RAND 0, LFO 1 → WT POS. Warp Asym +/−, LFO 2 dessus. LEVEL bas et LFO 1 → LEVEL (« about 80 % », cible incertaine).
  - **NOISE** : bruit d'usine, routé `Direct`, LFO 1 → LEVEL.
  - **LFO** : LFO 1 « slopes », LFO 2 forme d'usine (« oval », nom incertain), LFO 3 « mini triangle ». Tous à 1 mesure.
  - **FILTER 1** en High Notch 12 (Multi HN) sur A et C, DRIVE, RES et VAR (FREQ) montés, LFO 1 → CUTOFF.
- **ENV 1** : non dite par la vidéo. Attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX, dans l'ordre dit** :
  1. Filter Diffusor (VAR = STAGES).
  2. Plusieurs Equalizer en encoches, aigus montés sur le premier.
  3. Distortion Hard Clip, LFO 1 → MIX.
  4. Chorus et Dimension.
  5. Compressor Multiband (« three of them »), gain jusqu'à un niveau fort.
  6. Equalizer final : grave retiré, aigus montés.
- **Macros** : `Talk` profondeur de LFO 2 · `Snarl` WARP 2 (PD) · `Width` MIX du Chorus · `Dry` MIX du Hard Clip.
- **Sub associé** : S01. Le NOISE en `Direct` ne passe pas par le passe-haut final : le couper sous 120 Hz par sa couleur, ou le garder léger.
- **Origine** :
  - [SOURCE F08-02, transcription seule, Serum 2 de mars 2025] ;
  - toutes les profondeurs sont non dites ; noms de tables et de formes incertains.

### G04 Chaîne FM de sinus — growl lourd
- **Patch** :
  - OSC A, B et C en sinus (Basic Shapes). B et C muets.
  - Chaîne FM C → B → A : WARP de A en FM (B), WARP de B en FM (C).
  - MACRO 1 sur les deux quantités de FM.
  - FILTER 1 en Band 24, zone 100-600 Hz, un peu de RES.
  - Jouer très grave : un patch FM à trois étages sonne autrement dans l'aigu.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX, dans l'ordre vu à l'écran** :
  1. Distortion légère, puis Equalizer calé sur le pic du passe-bande, aigus fortement limités.
  2. Deux Filter de type diffuseur (Diffusor).
  3. Trois Compressor en Multiband (réglage d'usine « Multiband OTT ») : −18,1 dB, 4:1, attaque 90,1, release ≈ 99,1, gain 13,2 / 12,5 dB, bandes à 88 et 2 500 Hz.
  4. Deux Phaser figés : RATE au minimum, DEPTH 0, FREQ ≈ 205 Hz, 4 pôles, seul le FEEDBACK règle le timbre.
  5. Equalizer avec une encoche aiguë.
  6. Chorus en mode passe-haut, délais coupés, RATE 8 Hz, DEPTH et FEEDBACK bas.
  7. Compressor simple à la fin.
- **Macros** : `Talk` FREQ des phasers figés · `Snarl` MACRO 1 (FM) · `Width` MIX du Chorus · `Dry` gain des OTT.
- **Sub associé** : S01. Le passe-bande coupe déjà sous 100 Hz ; ajouter un passe-haut à 120 Hz.
- **Origine** :
  - [SOURCE F08-01, transcription et quatre captures, Serum 2, 150 BPM] ;
  - « du crunch, pas du désordre » sur la FM ; l'EQ change beaucoup le croquant.

### G05 Growl DNB Academy — PD et Rectify
- **Patch** :
  - OSC A en scie (Default Shapes), OCT −3 (−2 en House).
  - OSC B sur Basic Shapes, position triangle, Unison 3. Warp de B en Rectify au maximum.
  - WARP de A en PD (B), ≈ 35 % sous un LFO.
  - NOISE en White, STEREO 67.
  - FILTER 1 en Diffusor, CUTOFF 118, STAGES 72-75 (dit « 7275 »).
  - Un LFO (forme non décrite) sur la quantité de PD, la scie, le bruit.
- **ENV 1** : non dite. Attaque 1 ms, sustain 100 %, release 60 ms [ORIGINAL].
- **FX** :
  1. Distortion Overdrive agressive.
  2. Chorus en mode passe-haut.
  3. Filter Combs, CUTOFF presque au maximum.
  4. Equalizer : creux à 437 Hz, Q 60, −17,6 dB.
  5. Filter Phs 36+, CUTOFF ≈ 57, LFO bipolaire.
  6. Splitter : Convolve sur la bande haute (IR « L90 PLATE - DRUM - TIGHT PLATE »).
  7. Compressor Multiband : −18,1 dB, 4:1, 90,1 / 90,1, gain 7,2 dB, X-LOW 128 Hz.
  8. Filter MG Low 6 avec LFO 1 sur la coupure, puis Distortion Soft Clip.
- **Macros** : `Talk` LFO → PD · `Snarl` DRIVE de l'Overdrive · `Width` MIX du Chorus · `Dry` MIX du Convolve.
- **Sub associé** : S01.
- **Tempo** : 174 BPM dans la source ; recaler les LFO synchronisés au tempo House [`../tempo-mix.md`].
- **Origine** : [SOURCE F08-03, transcription et quatre captures, Serum 2, format vertical sans voix-off détaillée].

### G06 Patch BassGorilla — High Notch 12
- **Patch** :
  - OSC A, warp Bend +/− = 6. OSC B à 47 (paramètre non précisé par la source).
  - FILTER 1 en High Notch 12, CUTOFF 141 Hz, RES 49.
  - LFO 1 → CUTOFF en modulation inversée (−74), RATE 1/2, mode Trigger.
  - Pitch bend ±12.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** : Distortion Diode 2, DRIVE 20 ; Flanger, DEPTH 30, FEEDBACK 64 ; passe-haut à 120 Hz [ORIGINAL].
- **Macros** : `Talk` profondeur de LFO 1 · `Snarl` DRIVE · `Width` MIX du Flanger · `Dry` MIX de la Distortion.
- **Sub associé** : S01.
- **Origine** : [SOURCE BassGorilla, dans `basses.md` § 3]. Fiabilité faible : blog de vendeur, chiffres non vérifiés ; « Osc B = 47 » ne dit pas quel contrôle.

### G07 Talking bass — entre « oh » et « ah »
- **Patch** :
  - OSC A en scie (ou un growl de ce fichier), OCT −1.
  - FILTER 1 en Formant-I, RES 20-40, VAR (FORMNT) = décalage global. Sortie vers FILTER 2 en MG Low 24, CUTOFF 3-5 kHz (en série).
  - Trouver deux positions de CUTOFF, « oh » et « ah ». MACRO 1 ou un LFO lent (2 à 4 mesures) passe de l'une à l'autre.
  - LFO 2 en Trigger, 1/8, petite plage sur CUTOFF : le « parler ».
- **Formants visés** : « oh » F1 570 Hz / F2 840 Hz ; « ah » F1 730 / F2 1 090 Hz. F3 fixe vers 2 500-3 000 Hz.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** :
  1. Splitter L/M/H : sous 120 Hz propre ; de 120 Hz à 2 kHz, Tube puis Hard Clip ; au-dessus de 2 kHz, Tube.
  2. Compressor Multiband.
  3. Coupe-bas à 100 Hz.
- **Macros** : `Talk` MACRO 1 « oh » → « ah » · `Snarl` DRIVE de la bande médiane · `Width` — · `Dry` MIX de la bande médiane.
- **Sub associé** : S01, en `Direct`, sur sa piste.
- **Test** : à 0, 50 et 100 % de `Talk`, deux voyelles doivent s'identifier sur la boucle du drop, sans delay ni reverb posés.
- **Origine** :
  - [SOURCE talking bass du corpus] : formants « amen » et DUBFORGE, qui coïncident sur ah et oh ;
  - « de oh à ah c'est un tout petit mouvement de bouton ».

### G08 Growl Sam Smyers — Deep Bass House
- **Patch** :
  - OSC A en scie, OCT −1 (−2 dans la source), Unison 7, DETUNE réduit. VOICING MONO.
  - FILTER 1 en MG Low 12, puis Low 24 ; ENV 1 → CUTOFF ; RES modérée.
- **ENV 1** : attaque 2 ms, decay 400 ms, sustain −6 dB, release 100 ms [ORIGINAL].
- **FX** : Compressor Multiband, **puis** Distortion Tube, puis passe-haut à 150 Hz (l'unison s'annule sous 100 Hz). Un delay à la croche pointée est essayé puis retiré dans la source, pour une version plus propre.
- **Macros** : `Talk` ENV 1 → CUTOFF · `Snarl` DRIVE · `Width` DETUNE de l'unison · `Dry` MIX d'un Delay en croche pointée, 0 → 25 %.
- **Sub associé** : S01.
- **Origine** :
  - geste dit : −2 octaves, unison 7 avec detune réduit, mono, multibande puis Tube, MG Low 12 puis 24, ENV 1 vers cutoff, résonance, delay pointé retiré [SOURCE Sam Smyers « 5 Deep House Basses », transcription, Serum 1] ;
  - valeurs [ORIGINAL].

### G09 Growl façon Skrillex — passe-bande et table à la mesure
- **Patch** :
  - OSC A sur une table riche en médiums (Analog ou Digital d'usine).
  - LFO 1 → WT POS, boucle d'une mesure.
  - OSC B en sinus, LEVEL 0 ; WARP 1 de A en FM (B).
  - LFO 2 → quantité de FM et → CUTOFF.
  - FILTER 1 en Band 12, RES modérée (20-30 %), lié au LFO principal.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms [ORIGINAL].
- **FX** :
  1. Distortion Diode 2.
  2. Phaser.
  3. Equalizer : coupe vers 300 Hz.
  4. Compressor Multiband.
  5. Hyper/Dimension, grave au centre.
- **Macros** : `Talk` LFO 1 → WT POS · `Snarl` LFO 2 → FM · `Width` MIX de la Dimension · `Dry` MIX de la Diode.
- **Sub associé** : S01. La page met le sub dans le patch ; ici il est sur sa piste.
- **Origine** :
  - repère qualitatif : LFO d'une mesure sur la table, passe-bande résonant, Diode → Phaser → EQ −300 Hz → OTT → Dimension [SOURCE F08-17, page ADSR] ;
  - toutes les valeurs [ORIGINAL] : « pas de valeurs à reprendre ».

### G10 Growl en réponse — LFO Envelope, silence avant
- **Patch** :
  - G01, avec LFO 1 en mode ENVELOPE (un cycle par note), 1/4, sur le CUTOFF du formant.
  - Une forme qui ouvre la bouche sur la première moitié et la referme sur la seconde.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 60 ms : la réponse se termine nettement.
- **Macros** : celles de G01.
- **Sub associé** : S11, en contretemps.
- **Jeu** : bloc « Bass House 126 — growl en réponse » ci-dessous : silence, puis réponse de deux à quatre notes.
- **Test** : le stab et le growl ne doivent jamais parler en même temps.
- **Origine** :
  - « laisser un silence avant chaque réponse » ; Formant, LFO 1 en mode Envelope ou Trigger [`../families.md`, fiche 8] ;
  - mode ENVELOPE [cartographie, § 7.2].

### G11 Râpe FM — 15-25 % depuis une octave plus bas
- **Patch** :
  - OSC A en scie ou sur une table riche, OCT −2, RAND 0.
  - OSC B en sinus, OCT −3 (une octave sous A), LEVEL 0.
  - WARP 1 de A en FM (B), 15-25 %. LFO 1 (1/2, RETRIG) → WARP 1 ±10 %.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 50 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Overdrive, puis Equalizer (passe-haut à 150 Hz : le modulateur grave crée une composante continue), puis Compressor Multiband.
- **Macros** : `Talk` CUTOFF · `Snarl` WARP 1, 10 → 50 % (au-delà de 40 %, métallique) · `Width` — · `Dry` MIX de la Distortion.
- **Sub associé** : S01.
- **Test** : la note perçue peut paraître une octave plus grave. La vérifier à l'accordeur.
- **Origine** :
  - FM depuis un sinus une octave sous A, 15-25 % = râpe gutturale [SOURCE F08-04] ;
  - effet du modulateur grave [CALCUL, `../documentation-basses.md` § 1].

### G12 Growl spectral — partiels coupés et glissés
- **Patch** :
  - OSC A en moteur Spectral, sur une table ou un sample riche.
  - Couper des groupes de partiels aigus : son creux, guttural.
  - Faire glisser des partiels les uns contre les autres : grain inharmonique.
  - Morpher les frames au LFO (1/2) : voyelle sans filtre formant.
  - Unison 3-5 plutôt que 16, polyphonie limitée, conception en suréchantillonnage 2× (QUALITY sur High).
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Overdrive, puis passe-haut à 150 Hz.
- **Macros** : `Talk` morph des frames · `Snarl` profondeur du glissement de partiels · `Width` STACK de l'unison · `Dry` MIX de la Distortion.
- **Sub associé** : S01.
- **Origine** :
  - [SOURCE F08-04, section « oscillateur spectral »] ;
  - warps spectraux du moteur [cartographie, § 4.3 : libellés affichés non documentés, à lire dans l'interface].

### G13 Growl de sa propre voix
- **Patch** :
  1. Enregistrer « yah-woh-yoi » d'une voix stable en hauteur, couper le WAV.
  2. Le déposer sur OSC A : Serum 2 le convertit en wavetable. Une source à hauteur stable se convertit le plus proprement.
  3. Unison 1, OCT −1, LEVEL 75 %. LFO 1 (1/2) → WT POS : les voyelles enregistrées défilent.
  4. FILTER 1 en MG Low 12, CUTOFF ≈ 60 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : chaîne de G01.
- **Macros** : `Talk` LFO 1 → WT POS · `Snarl` DRIVE · `Width` · `Dry`, comme G01.
- **Sub associé** : S01.
- **Droits** : la voix de l'utilisateur ne pose pas de problème ; une voix tierce demande une licence (`AGENTS.md`, règle Référence).
- **Origine** :
  - [SOURCE F08-04] ;
  - « custom wavetables from vocals — the formants survive » [SOURCE talking bass du corpus, `[DOC-2]`].

### G14 Double warp — FM et Diode sur la même table
- **Patch** :
  - OSC A sur une table riche, OCT −2, RAND 0.
  - WARP 1 en FM (B), 15-30 %, avec B en sinus à OCT −2 (rapport 1:1), LEVEL 0.
  - WARP 2 en Distortion Diode 1, 20-50 %.
  - LFO 1 (1/2, RETRIG) → WARP 1 ; LFO 2 (1/8) → WARP 2, faible profondeur.
  - FILTER 1 en Formant-II, RES 25 %.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Compressor Multiband, puis passe-haut à 150 Hz. Pas de distorsion supplémentaire : elle est dans le warp.
- **Macros** : `Talk` CUTOFF du formant · `Snarl` WARP 2 · `Width` — · `Dry` WARP 1.
- **Sub associé** : S07.
- **Origine** :
  - deux warps par oscillateur dans Serum 2 [cartographie, § 4] ;
  - « le dual warp de Serum 2 permet FM et distorsion sur la même wavetable » [`patches-genres.md` § 2, `[I]`] ;
  - recette [ORIGINAL].

### G15 Phaser qui parle
- **Patch** : G01, plus deux modulations du Phaser :
  - LFO 3 (1/4, RETRIG) → FEEDBACK du Phaser, de 40 à 75 % ;
  - un second Phaser figé (RATE minimum, DEPTH 0) dont seule la FREQ bouge sous LFO 2 (1/8).
- **ENV 1** : comme G01.
- **Macros** : `Talk` LFO 3 → FEEDBACK · `Snarl` comme G01 · `Width` · `Dry` MIX des phasers.
- **Sub associé** : S10.
- **Origine** :
  - « un LFO sur le feedback du phaser ajoute une couche de “parole” » [SOURCE F08-04] ;
  - phasers figés (seules fréquence et feedback) [SOURCE F08-01].

### G16 Growl ressamplé — changer le rythme à chaque passe
- **Patch** :
  1. Construire G01, G03 ou G04.
  2. Imprimer une note tenue de 2 à 4 mesures, effets compris.
  3. La remettre dans un oscillateur (glisser le WAV ou Resample to).
  4. Nouveau warp, nouveau formant, nouveaux effets, et surtout un autre rythme de LFO à chaque passe ; sinon les couches « bavent ».
  5. S'arrêter après 2 ou 3 passes : « more passes add mud, not character ».
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01, jamais ressamplé avec le growl.
- **Origine** :
  - boucle de resampling [SOURCE F08-04, page et infographie] ;
  - imprimer plusieurs prises et garder les meilleures [SOURCE F02-14] ;
  - procédure : `../../../resampling/SKILL.md`.

### G17 Growl métallique au peigne
- **Patch** :
  - OSC A en scie, OCT −2, RAND 0.
  - OSC B en sinus, Ratio 2.000 (SRC = A), FIN −30 cents, LEVEL 0 ; WARP 1 de A en FM (B), 20 %.
  - FILTER 1 en Combs, key track allumé, VAR (DAMP) 30 %.
  - LFO 1 (1/2, RETRIG) → CUTOFF du peigne ±1 octave.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **FX** : Distortion Diode 1, puis Equalizer (passe-haut à 150 Hz, −3 dB vers 2-5 kHz), puis Compressor Multiband.
- **Macros** : `Talk` LFO 1 → CUTOFF · `Snarl` FIN de B, 0 → −40 cents · `Width` — · `Dry` MIX de la Diode.
- **Sub associé** : S01.
- **Origine** :
  - Combs en FX [SOURCE F08-03] ;
  - métal par FM 2:1 désaccordée de 30 cents [SOURCE Attack Magazine, Garage Bass, `patches-genres.md`] ;
  - assemblage [ORIGINAL]. Les tutoriels Jauz et Eptic du registre (F08-09, F08-10) ne sont pas étudiés.

### G18 Growl à hauteur mouvante — Main Tuning
- **Patch** :
  - G01, plus LFO 4 (1 mesure, RETRIG) → Global › Main Tuning, bipolaire, ≈ 10-13 %.
  - Forme : une chute et une remontée par mesure.
- **ENV 1** : comme G01.
- **Macros** : `Talk` comme G01 · `Snarl` profondeur de LFO 4 vers Main Tuning · `Width` · `Dry`.
- **Sub associé** : S01, **sur sa piste** : Main Tuning ne bouge que le patch de Serum où il est réglé, donc le sub reste juste.
- **Test** : la hauteur qui bouge ne doit pas faire paraître la ligne fausse contre le stab.
- **Origine** :
  - macro 5 → Global Main Tuning, bipolaire, ≈ 13 %, pilotée à 1 mesure par LFO Tool [SOURCE F08-01] ;
  - LFO 3 → Main Tuning ≈ 10 %, bipolaire [SOURCE F10-01] ;
  - ici un LFO interne remplace le plug-in [ORIGINAL] ;
  - « séparer le sub si le pitch global est automatisé » [`../families.md`, fiche 8].

### G19 Growl en LFO Path — deux voyelles d'un même tracé
- **Patch** :
  - G01, avec LFO 1 de type Path : un tracé XY dessiné, 1/2, RETRIG.
  - Sortie X → CUTOFF du formant ; sortie Y → WT POS.
  - Un seul tracé fait bouger deux voyelles de façon liée, mais pas identique.
- **ENV 1** : comme G01.
- **Macros** : `Talk` profondeur de X · `Snarl` profondeur de Y · `Width` · `Dry`.
- **Sub associé** : S10.
- **Origine** :
  - type Path, sortie X et sortie Y séparée [cartographie, § 7.2] ;
  - Konstricta présente le nouvel éditeur de LFO Path sans dire s'il l'utilise [SOURCE F08-02] ;
  - recette [ORIGINAL].

### G20 Growl mono, largeur en post
- **Patch** : n'importe quel growl de ce fichier, en mono : Unison 1, pas d'Hyper ni de Chorus dans la chaîne principale. Ensuite :
  - Rack FX : Splitter M/S en fin de chaîne.
  - Sous-rack MID : rien.
  - Sous-rack SIDE : Equalizer (passe-haut à 300 Hz), puis Chorus ou Bode (frequency shifter) avec MIX ≈ 20 %.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Width` LEVEL du sous-rack SIDE · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Test** : en mono, le growl doit garder sa force ; la largeur n'apparaît qu'au-dessus de 300 Hz.
- **Origine** :
  - « garder le mono puissant dans le patch, ajouter la stéréo après » ; Bode, MIX ≈ 20 % [SOURCE F13-02, Art1fact] ;
  - « unison à 1 pendant la conception : un growl mono frappe plus fort » [`basses.md` § 3] ;
  - Splitter M/S [cartographie, § 8].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Kick supposé sur les quatre temps (doubles croches 1, 5, 9, 13). Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f08-growl.md`. Le bloc « Bass House 128 — stab et growl en réponse, sub séparé » de `../motifs.md` complète ces trois motifs.

```grille
titre: Bass House 126 — growl en réponse (G10)
tempo: 126
accords: Fm7 | Fm7
growl: F1[2&:1] F1[2a:1] Ab1[3&:2] | F1[1&:2] C2[2&:1] Ab1[2a:1] F1[3&:3] Eb1[4a:1]
sub: F0[2&:1] F0[2a:1] Ab0[3&:2] | F0[1&:2] C1[2&:1] Ab0[2a:1] F0[3&:3] Eb0[4a:1]
```

Mesure 1 : question courte, laissée en partie au stab (silence sur le premier temps et sur la fin). Mesure 2 : réponse longue.

```grille
titre: Bass House 128 — talking en syllabes (G02, G07)
tempo: 128
accords: Gm7 | Gm7
talk: G1[1e:3] G1[2e:3] Bb1[3e:3] F1[4e:3] | G1[1e:7] D2[3e:3] C2[4e:2] Bb1[4a:1]
sub: G0[1e:3] G0[2e:3] Bb0[3e:3] F0[4e:3] | G0[1e:7] D1[3e:3] C1[4e:2] Bb0[4a:1]
```

Avec le LFO à 1/8 (234,4 ms à 128 BPM), une tenue de trois doubles croches (351,6 ms) porte une syllabe et demie, et la tenue de sept doubles croches de la mesure 2 en porte trois et demie [CALCUL]. Pour une syllabe entière par note, raccourcir les tenues à deux doubles croches.

```grille
titre: Bass House 128 — growl de fin de phrase (G01, G04)
tempo: 128
accords: Em7 | Em7
growl: E1[4&:2] | E1[1e:2] G1[1a:1] E1[2&:2] B1[3e:2] D2[3a:1] E2[4e:3]
sub: E0[4&:2] | E0[1e:2] E0[2&:2] B0[3e:2] E1[4e:3]
```

Deux mesures à placer en mesures 7-8 d'une phrase : le growl n'entre que sur la fin de la mesure 7 et remplit la mesure 8. C'est l'une des variations à faire avant chaque frontière de huit mesures (règle des drops d'`AGENTS.md`).

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « BAS plug », « Monster » et « softest growl » de G03 ;
  - les filtres High Notch 12, Diffusor, Formant-I/II/III, Combs et Phs 36+ ;
  - le réglage d'usine « Multiband OTT » ;
  - le LFO de type Path.

  Vérifier les destinations des macros.
- Écouter chaque recette avec son sub, puis avec le kick et le stab, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
