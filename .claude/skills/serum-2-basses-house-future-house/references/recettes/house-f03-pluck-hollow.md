# Vingt recettes de pluck rond, hollow FM, Future House et G-House (famille F03)

Troisième lot de recettes House. La basse qui rebondit : pluck rond, « hollow » hérité du UK Garage, basse FM de Future House, pluck grave de G-House. Rédigé le 05/10/2026. Sources :
- les études de `../etudes-pages-house.md` (F03-04, F03-06, GEN-06), `../etudes-captures.md` (F03-04) et `../etudes-videos.md` (F03-03) ;
- les patchs chiffrés de `../../../sound-designer-serum/references/patches-genres.md` (Garage Bass et Beat-Pulsing Plucks d'Attack Magazine) ;
- la transcription Sam Smyers de `../../../composer-hooks-funk-electro/references/sources-videos.md` ;
- `../documentation-basses.md` § 1 (FM) et la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` :
- **[SOURCE …]** : valeur tirée d'une étude ;
- **[EXTRAIT …]** : indice tiré d'un résultat de recherche dont la page n'a pas été lue ;
- **[CALCUL]**, **[DÉDUCTION]**, **[ORIGINAL]** : comme dans `house-f01-sub.md`.

## Règles communes aux vingt recettes

1. **Couche médium, sub à part.** Chaque fiche propose un sub de `house-f01-sub.md`.
   - Equalizer de Serum 2 : bande basse en High Pass vers 90 Hz.
   - Jouer la couche pour que sa fondamentale tombe entre 80 et 200 Hz, en Mi1-Sol2 (82-196 Hz).
   - Plusieurs patchs d'origine descendent au registre du sub (Garage Bass à −24) : les fiches le signalent.
2. **FM dans Serum 2** : WARP 1 d'OSC A en FM (B), FM (C) ou FM (Sub).
   - Le modulateur doit être allumé ; son LEVEL peut être à 0 et son routage à `None` (cartographie, § 4.2).
   - RAND à 0 et PHASE fixe sur porteuse et modulateur : sinon le timbre FM change à chaque note.
3. **Rapport des hauteurs**, porteuse:modulateur [CALCUL, `../documentation-basses.md` § 1] :
   - 1:2 (modulateur une octave au-dessus) : harmoniques impairs seuls, le son « hollow » proche du carré ;
   - 1:3 : proche d'une impulsion à 33 % ;
   - 1:4 : impairs aussi ;
   - rapport non entier : son inharmonique, métallique ;
   - modulateur une octave **sous** la porteuse : une octave perçue plus grave et une composante continue.

   Le mode Ratio de Serum 2 (clic droit sur OCT ou SEM › Ratio, source SRC) règle ce rapport directement (cartographie, § 3.1).
4. **L'enveloppe sur la quantité de FM est « la partie la plus importante de tout patch FM »** [SOURCE F03-04]. La FM donne à l'attaque un claquement qu'une enveloppe de filtre seule ne donne pas.
5. **Quatre macros communes** :
   - `Hollow` : quantité de FM, de PD ou de creux ;
   - `Snap` : quantité de l'enveloppe d'attaque (sur la FM ou sur le filtre) ;
   - `Length` : decay d'ENV 1 ou de l'enveloppe principale ;
   - `Round` : coupure du filtre.

   Vérifier le « + » sur chaque destination avant d'assigner.
6. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
7. **Contrôle par l'utilisateur** :
   - la couche seule, puis avec son sub, puis avec le kick ;
   - mono ;
   - la note la plus aiguë et la plus grave de la ligne : en FM le timbre change avec la hauteur ;
   - les deux bornes de `Hollow` ;
   - faible volume ;
   - A/B à niveau égal contre H01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| H01 | Pluck rond de référence | Future House, Deep House | ENV 2 sur un passe-bas doux |
| H02 | Hollow Garage | Future House, UK Garage | modulation de phase 2:1, filtre fermé |
| H03 | Hollow Garage désaccordé | Future House métallique | modulateur à −30 cents |
| H04 | FM bass Monosounds | Future House | scie modulée par un sinus grave |
| H05 | Carré hollow | Future House | carré + FM d'une onde riche |
| H06 | Bounce Mesto | Future House 128 | SawRoundedToSquare, ENV 2 longue |
| H07 | Bounce en triolets | Future House 126 | LFO 1/8 triolet sur le filtre |
| H08 | G-House grave | G-House | sinus modulé, décroissance courte |
| H09 | FM pluck Sam Smyers | Deep House, G-House | ENV 2 sur la FM |
| H10 | Hollow Odd/Even | Future House | scie rendue carrée par le warp |
| H11 | Hollow FM 1:2 pur | Future House | modulateur à +12 |
| H12 | Hollow en mode Ratio | Future House, métallique | rapport 2, 3 ou décalé |
| H13 | Hollow PD | Deep House, Future House | distorsion de phase, plus douce |
| H14 | Pluck dynamique | Deep House | vélocité et key track |
| H15 | Hollow élastique | Future House drop | chute de hauteur du modulateur |
| H16 | Pluck au flanger | Future House métallique | filtre Flg L suivant la note |
| H17 | Pluck deep chaud | Deep House, Organic | Tape Sat. et chorus HPF |
| H18 | Hollow « wah » | Future House | filtre formant balayé |
| H19 | Pluck laser | Future House, Bass House | Hyper en RETRIG |
| H20 | Hollow imprimé en table | toutes | Render OSC Warp puis WT POS |

## Les vingt recettes

### H01 Pluck rond de référence
- **Patch** :
  - OSC A sur Basic Shapes, entre scie et carrée (WT POS au milieu), OCT −1, RAND 0.
  - FILTER 1 en MG Low 12, CUTOFF 200-500 Hz, RES 5-10 %, key track allumé.
  - ENV 2 → CUTOFF +2 à +3 octaves : attaque 0-5 ms, decay 120-280 ms, sustain 0-20 %.
- **ENV 1** : attaque 2 ms, decay 200-450 ms, sustain 0-40 %, release 80 ms.
- **FX** : Distortion Tape Sat. DRIVE 15-25, MIX 40 % ; Equalizer en passe-haut à 90 Hz.
- **Macros** : `Hollow` WT POS de la scie à la carrée · `Snap` ENV 2 → CUTOFF 0 → 70 % · `Length` decay d'ENV 1 120 → 500 ms · `Round` CUTOFF 150 → 800 Hz.
- **Sub associé** : S01 ou S15.
- **Jeu** : staccato en contretemps, vélocité variable (`../motifs.md`, bloc Future House 126).
- **Origine** :
  - fourchettes de la fiche 2 de `../families.md` [ORIGINAL, reprises] ;
  - key track contre les sauts d'octave (même fiche) ; Tape Sat. comme dans GEN-06.

### H02 Hollow Garage — l'ancêtre chiffré
- **Patch** (transposition de Massive vers Serum 2) :
  - OSC A en sinus (Basic Shapes, position sinus), OCT −2 : c'est la porteuse.
  - OSC B en sinus, OCT −1, LEVEL 0, routé `None` : c'est le modulateur, une octave au-dessus de A, rapport 1:2.
  - OSC C en sinus, OCT −1, LEVEL ≈ 70 % : la couche audible de l'Osc 2 d'origine.
  - WARP 1 d'OSC A en PD (B) (modulation de phase), ≈ 45 %. ENV 2 → ce warp +60 %.
- **Filtre** : FILTER 1 sur A et C, MG Low 24 (le « Daft » de Massive n'existe pas), CUTOFF ≈ 25 %, RES 0. ENV 2 → CUTOFF au maximum : attaque rapide, decay moyen-rapide (120-240 ms), sustain 0, release court.
- **ENV 1** : attaque 1 ms, sustain 100 %, release ≈ 33 % de la course (≈ 150-250 ms).
- **Voicing** : MONO, PORTA 10-15 % de la course (≈ 30-60 ms), LEGATO off, pour que chaque note redéclenche comme « Restart via Gate ».
- **FX** : Distortion Tube DRIVE et MIX ≈ 28 % (le « ~10 h » de la source) ; Hyper/Dimension, UNISON 0, SIZE 0, MIX ≈ 28 % ; Equalizer en passe-haut à 90 Hz.
- **Registre** : A à −2 octaves descend au niveau du sub. Jouer la ligne une octave plus haut que le sub, ou garder ce patch seul s'il n'y a pas de sub.
- **Macros** : `Hollow` quantité du warp PD 0 → 70 % · `Snap` ENV 2 → warp 0 → 80 % · `Length` decay d'ENV 2 60 → 300 ms · `Round` CUTOFF 10 → 50 %.
- **Sub associé** : S01.
- **Jeu** : motif « UK Garage 130 — hollow en 2-step » ci-dessous, ou bloc Future House de `../motifs.md`.
- **Origine** :
  - toutes les valeurs [SOURCE Attack Magazine « Synth Secrets: Garage Bass », Massive, dans `patches-genres.md`] ;
  - le rapport 2:1 donne « le creux façon carré ou orgue, pas une cloche » ;
  - PD (B) pour la « Phase Modulation » de Massive, et durées en ms [ORIGINAL].

### H03 Hollow Garage désaccordé — le métallique du genre
- **Patch** : H02, avec un réglage en plus : FIN d'OSC B à −30 cents (le « −12,30 » de la source).
- **Macros** : celles de H02, plus `Hollow` sur FIN d'OSC B de 0 à −40 cents si la destination l'accepte.
- **Test** :
  - comparer H02 et H03 sur la même note ;
  - le battement doit rester lent sur la note la plus grave et ne pas devenir désagréable sur la plus aiguë, puisque l'écart en Hz double à chaque octave.
- **Origine** : « le métallique apparaît avec la variante −12,30 : le modulateur désaccordé de 30 centièmes rend le spectre légèrement inharmonique et battant » [SOURCE Attack Magazine, `patches-genres.md`].

### H04 FM bass Monosounds — Future House
- **Patch** :
  - OSC A en scie (Basic Shapes), la porteuse, OCT −1, RAND 0.
  - OSC B en sinus une octave **sous** A (OCT −2), LEVEL 0, `None`.
  - WARP 1 d'OSC A en FM (B), 30 %. ENV 2 → ce warp 50 %, decay 150 ms, sustain 0.
  - FILTER 1 en MG Low 24, CUTOFF 40-60 %.
  - Matrice : Velocity → WARP 1, 15 %.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −8 dB, release 120 ms. La page n'en donne pas : [ORIGINAL].
- **FX** : Equalizer, passe-haut à 90 Hz, utile ici à cause de la composante continue (règle 3).
- **Macros** : `Hollow` WARP 1 10 → 45 % · `Snap` ENV 2 → warp 0 → 70 % · `Length` decay d'ENV 2 80 → 300 ms · `Round` CUTOFF 25 → 70 %.
- **Sub associé** : S01.
- **Test** : la note perçue peut sembler une octave plus grave que la note jouée. Vérifier à l'accordeur sur la note la plus jouée, puis comparer avec B à +12.
- **Origine** :
  - « FM bass » : porteuse scie, modulateur sinus une octave plus bas, FM (B) 30 %, ENV 2 50 % / 150 ms, MG Low 24 ; vélocité → warp 15 % [SOURCE F03-04, page] ;
  - effet du modulateur grave [CALCUL, règle 3].

### H05 Carré hollow — architecture ADSR
- **Patch** :
  - OSC A sur la frame carrée de Basic Shapes, OCT −1, RAND 0 : le creux.
  - OSC B en scie, même octave, LEVEL 20-40 % : couche riche et source FM.
  - WARP 1 d'OSC A en FM (B), 5-15 %. ENV 2 → warp +20 %, decay 120 ms.
  - FILTER 1 sur A et B, MG Low 24, CUTOFF ≈ 35 %. ENV 3 → CUTOFF +40 %, decay 200 ms.
- **ENV 1** : attaque 1 ms, decay 350 ms, sustain −10 dB, release 90 ms.
- **FX** : Distortion Soft Clip DRIVE 15, puis passe-haut à 90 Hz.
- **Macros** : `Hollow` LEVEL d'OSC B 0 → 60 % · `Snap` ENV 3 → CUTOFF 0 → 60 % · `Length` decay d'ENV 1 150 → 500 ms · `Round` CUTOFF 20 → 60 %.
- **Sub associé** : S04 ou S15.
- **Origine** :
  - architecture « un carré pour le creux, l'autre oscillateur riche pour la superposition et comme source de FM » [SOURCE F03-06, page] ;
  - les deux tables de l'auteur ne sont pas accessibles ; valeurs [ORIGINAL].

### H06 Bounce Mesto — Future House 128
- **Patch** :
  - OSC A sur la table SawRoundedToSquare (table de Serum 1, à retrouver dans le navigateur de Serum 2), position carrée, OCT −1, Unison 1.
  - WT POS modulée : la bulle « A WTPos 17 » ne dit pas par quelle source ; ENV 2 [ORIGINAL].
  - FILTER 1 en MG Low 12. ENV 2 → CUTOFF 42.
  - ENV 2 : 0,5 ms / 0 / 966 ms / 38,24 % / 308 ms.
- **ENV 1** : 0,5 ms / 0 / 1,00 s / 100 % / 15 ms. C'est l'Init : la note dure ce que dure le MIDI.
- **FX** :
  1. Distortion Tube, filtre PRE en passe-bas ≈ 2 893 Hz, Q 0,1.
  2. Compressor Single.
  3. Equalizer, bande basse en Peak ; passe-haut à 90 Hz ajouté [ORIGINAL].
- **Voicing** : MONO + LEGATO.
- **Macros** : `Hollow` ENV 2 → WT POS 0 → 30 · `Snap` ENV 2 → CUTOFF 0 → 60 · `Length` decay d'ENV 2 300 ms → 1,2 s · `Round` CUTOFF 15 → 60 %.
- **Sub associé** : S04.
- **Jeu** : motif « Future House 128 — bounce en octaves » ci-dessous ; notes courtes, puisque ENV 1 tient tant que la note est tenue.
- **Origine** :
  - [SOURCE F03-03, quatre captures, Serum 1, vidéo sans voix à 128 BPM] ;
  - drive, seuil et gains d'EQ illisibles sur les captures.

### H07 Bounce en triolets — Future House 126
- **Patch** :
  - OSC A, table Dist 8Bit Fwap (Digital), Unison 4, DETUNE 0,10.
  - OSC B, table CrushWub (Digital), Unison 3, DETUNE 0,16.
  - Ce sont des tables de Serum 1 : à retrouver dans Serum 2, sinon deux scies à unison léger.
  - FILTER 1 sur A et B (type non chiffré par la source : MG Low 12 [ORIGINAL]).
  - LFO 1 → CUTOFF : RATE 1/8 avec TRIP, SMOOTH 50, forme dessinée à la main (montée rapide, descente lente [ORIGINAL]).
  - LFO 2 → WT POS de A et B, RATE 1/2.
  - LFO 3 → LEVEL de A et B (sidechain interne), SMOOTH 50, ≈ 26 %.
- **ENV 1** : attaque 1 ms, decay 400 ms, sustain −6 dB, release 100 ms [ORIGINAL].
- **FX** : Reverb avec coupe-bas sur la reverb, ENV 2 → MIX de la Reverb ; Equalizer en passe-haut à 120 Hz, à cause de l'unison.
- **Macros** : `Hollow` LFO 2 → WT POS 0 → 50 % · `Snap` LFO 1 → CUTOFF 0 → 60 % · `Length` decay d'ENV 1 150 → 600 ms · `Round` CUTOFF 20 → 60 %.
- **Sub associé** : S10 (creux à la noire), sous le rebond en triolets.
- **Tempo** : un 1/8 triolet dure 158,7 ms à 126 BPM et 156,3 ms à 128 BPM [CALCUL].
- **Origine** : [SOURCE Attack Magazine « Modulating Serum's FX: Beat-Pulsing Plucks », dans `patches-genres.md`] ; « la meilleure base Serum documentée pour un pluck house rythmique ».

### H08 G-House grave — façon Malaa et Tchami
- **Patch** :
  - OSC A en sinus, OCT −1, RAND 0.
  - OSC B sur une table riche, LEVEL 0. L'extrait cite « Allophone », à retrouver dans le navigateur ; à défaut, une scie.
  - WARP 1 d'OSC A en FM (B), 15-30 %. ENV 2 → warp +40 %, attaque 0, decay 80-150 ms, sustain 0.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 45 %.
- **ENV 1** : attaque 1 ms, decay 220 ms, sustain −∞, release 60 ms.
- **FX** : Distortion Tube DRIVE 20-35, Compressor Single 4:1, passe-haut à 90 Hz.
- **Macros** : `Hollow` WARP 1 5 → 45 % · `Snap` ENV 2 → warp 0 → 70 % · `Length` decay d'ENV 1 120 → 400 ms · `Round` CUTOFF 25 → 65 %.
- **Sub associé** : S11 ou S16.
- **Jeu** : motif « G-House 124 — pluck grave clairsemé » ci-dessous.
- **Origine** :
  - « sinus en A, Allophone en B, FM par le warp de A » [EXTRAIT F03-02, page EvoSounds non lue] ;
  - valeurs [ORIGINAL]. Indice faible : à confirmer en lisant la page sur le Mac.

### H09 FM pluck Sam Smyers — Deep House, G-House
- **Patch** :
  - OSC A en sinus, OCT −1 (−2 dans la source, remonté parce que la couche est médium).
  - OSC B quasi inaudible (LEVEL 0-5 %), même octave.
  - WARP 1 d'OSC A en FM (B), base 10 %.
  - ENV 2 → warp +50 %, attaque 0, decay 100-200 ms, sustain 0. Variante : LFO 3 en mode Envelope, RATE 1/32, sur le même warp, pour une attaque encore plus courte.
  - VOICING MONO.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −12 dB, release 80 ms.
- **FX** : Compressor Single 3:1, puis passe-haut à 90 Hz.
- **Macros** : `Hollow` WARP 1 base 0 → 30 % · `Snap` ENV 2 → warp 0 → 80 % · `Length` decay d'ENV 2 50 → 300 ms · `Round` — (pas de filtre).
- **Sub associé** : S01.
- **Test** : comparer ENV 2 et LFO Envelope sur l'attaque, à niveau égal.
- **Origine** :
  - geste dit : A sinus à −2, B quasi inaudible, FM from B, ENV 2 vers la quantité de FM, option LFO en mode enveloppe très rapide, mono et compresseur [SOURCE Sam Smyers « 5 Deep House Basses », transcription, Serum 1] ;
  - valeurs [ORIGINAL] : la vidéo ne les dit pas.

### H10 Hollow Odd/Even — une scie rendue carrée
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - WARP 1 en Odd/Even, base 50 % (signal d'origine). ENV 2 → ce warp −40 à −50 %, attaque 0, decay 150 ms, sustain 0 : l'attaque part creuse, puis revient à la scie.
  - Variante inverse : warp fixé à 10-20 % (presque carré) et ENV 2 positive.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 45 %, ENV 3 → CUTOFF +30 %.
- **ENV 1** : attaque 1 ms, decay 350 ms, sustain −8 dB, release 90 ms.
- **FX** : Distortion Soft Sat. légère, passe-haut à 90 Hz.
- **Macros** : `Hollow` Odd/Even 50 → 0 % · `Snap` ENV 2 → warp 0 → −50 % · `Length` decay d'ENV 1 150 → 500 ms · `Round` CUTOFF 20 → 65 %.
- **Sub associé** : S04.
- **Origine** :
  - Odd/Even : « 50 % = signal d'origine, 0 % = impaires seules, 100 % = paires seules » [cartographie, § 4.1] ;
  - une scie réduite à ses impairs garde des amplitudes en 1/n, le spectre d'un carré [DÉDUCTION, jamais essayée].
- **Limite** : à 100 %, la fondamentale manque : ne pas pousser la macro dans ce sens.

### H11 Hollow FM 1:2 pur
- **Patch** :
  - OSC A en sinus, OCT −1, RAND 0, PHASE 0 %.
  - OSC B en sinus, OCT 0 (+12 demi-tons sur A), LEVEL 0, `None`, RAND 0, PHASE 0 %.
  - WARP 1 d'OSC A en FM (B), 10-25 %. ENV 2 → warp +30 %, decay 100-250 ms, sustain 0.
  - FILTER 1 en Band 12 ou MG Low 12, modéré.
- **ENV 1** : pluck, attaque 1 ms, decay 150-350 ms, sustain 0, release 60 ms.
- **FX** : passe-haut à 90 Hz.
- **Macros** : `Hollow` WARP 1 5 → 30 % · `Snap` ENV 2 → warp 0 → 50 % · `Length` decay d'ENV 1 100 → 400 ms · `Round` CUTOFF 30 → 70 %.
- **Sub associé** : S01.
- **Variante** : B en OCT +1 (+24, 1:4), qui donne aussi les impairs.
- **Origine** :
  - fiche 3 de `../families.md` : B à +12 ou +24, FM 5-20 %, ENV 2 vers la FM 100-250 ms ;
  - rapport 1:2 → harmoniques impairs seuls, « hollow » proche du carré [CALCUL, Synth Secrets 13 dans `../documentation-basses.md`].

### H12 Hollow en mode Ratio — 2, 3 ou décalé
- **Patch** :
  - H11, avec OSC B en mode Ratio : clic droit sur OCT › Ratio, SRC = A.
  - Trois réglages à comparer :
    - **2,000** : impairs seuls, hollow ;
    - **3,000** : proche d'une impulsion à 33 %, plus nasal ;
    - **3,059** : 34 cents au-dessus de l'harmonique 3, inharmonique et métallique.
- **Macros** : celles de H11. Pour passer d'un ratio à l'autre, préparer trois presets plutôt qu'une macro.
- **Test** : à 3,059, le décalage des composantes vaut ≈ 3 Hz sur La0 et ≈ 6 Hz sur La1. Écouter la note la plus aiguë de la ligne.
- **Origine** :
  - mode Ratio [cartographie, § 3.1 ; manuel, « Setting the Octave or Semitone Mode »] ;
  - effets des rapports [CALCUL, `../documentation-basses.md` § 1] ;
  - 3,059 : 12 × log2(3,059) = 19,36 demi-tons [CALCUL].

### H13 Hollow PD — plus doux que la FM
- **Patch** :
  - OSC A en sinus, OCT −1, RAND 0.
  - WARP 1 en PD (Self), 10-40 %. ENV 2 → warp +40 %, decay 120-200 ms, sustain 0.
  - Variante : PD (B) avec B en sinus à +12, LEVEL 0.
  - FILTER 1 éteint ou MG Low 12 très ouvert.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −10 dB, release 80 ms.
- **FX** : Distortion Tape Sat. légère, passe-haut à 90 Hz.
- **Macros** : `Hollow` quantité de PD 0 → 60 % · `Snap` ENV 2 → warp 0 → 60 % · `Length` decay d'ENV 1 150 → 500 ms · `Round` — ou CUTOFF.
- **Sub associé** : S03.
- **Origine** :
  - « PD est plus doux (“CZ-style”) » que la FM [SOURCE F03-04] ;
  - PD (Self) [cartographie, § 4.2] ;
  - lien avec la distorsion de phase des Casio CZ, sans supposer l'identité [`../documentation-basses.md` § 1] ;
  - valeurs [ORIGINAL].

### H14 Pluck dynamique — Deep House
- **Patch** :
  - H01, avec deux lignes de matrice en plus :
    - Velocity → CUTOFF ≈ 10 % ;
    - Velocity → ENV 2 → CUTOFF, si cette destination accepte la modulation.
  - Key track du filtre allumé.
- **ENV 1** : comme H01.
- **Macros** : celles de H01.
- **Sub associé** : S19, sensible à la vélocité aussi.
- **Jeu** : notes principales à 110-127, réponses à 70-90.
- **Test** : un saut d'une octave ne doit pas changer la brillance relative de la note. Couper le key track pour comparer.
- **Origine** : Velo → Filter 1 Freq ≈ 10 % [SOURCE GEN-06, page et écran] ; key track sur un pluck (fiche 2 de `../families.md`).

### H15 Hollow élastique — drop Future House
- **Patch** :
  - H11, avec ENV 3 → CRS d'OSC B (le modulateur) : +12 demi-tons au pic, attaque 0, decay 60-120 ms, sustain 0.
  - Le rapport passe de 1:4 à 1:2 au début de chaque note.
- **ENV 1** : attaque 1 ms, decay 250 ms, sustain −12 dB, release 70 ms.
- **Macros** : `Hollow` WARP 1 5 → 35 % · `Snap` ENV 3 → CRS de B 0 → +12 · `Length` decay d'ENV 3 30 → 200 ms · `Round` CUTOFF 30 → 70 %.
- **Sub associé** : S01. La hauteur de la porteuse ne bouge pas, donc rien ne gêne le sub.
- **Test** : le « boing » doit rester un mouvement de timbre, sans changer la note perçue.
- **Origine** :
  - la Future House est décrite comme « un drop métallique et élastique, des lignes de basse modulées en fréquence » [SOURCE Wikipédia, dans `patches-genres.md`] ;
  - geste [ORIGINAL] ; rapports [CALCUL].

### H16 Pluck au flanger — Future House métallique
- **Patch** :
  - OSC A en scie, OCT −1, RAND 0.
  - FILTER 1 en Flg L6+ (flanger avec passe-bas dans la boucle), CUTOFF ≈ 50 %, RES 40-60 %, key track allumé, MIX ≈ 50 % (le mix recommandé pour ces types).
  - ENV 2 → CUTOFF +20 %, decay 150 ms.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −10 dB, release 80 ms.
- **FX** : Distortion Tube légère, passe-haut à 100 Hz.
- **Macros** : `Hollow` RES 0 → 70 % · `Snap` ENV 2 → CUTOFF 0 → 40 % · `Length` decay d'ENV 1 150 → 500 ms · `Round` VAR (LP FREQ) du flanger.
- **Sub associé** : S01.
- **Test** : avec le key track, chaque note doit garder la même couleur. Sans lui, certaines notes résonnent plus que d'autres.
- **Origine** :
  - types Flg L et MIX à 50 % [cartographie, § 6] ;
  - type « Flg L6+ » réglé par Antidote Audio sur une basse jump-up, avec key track essayé [SOURCE F06-01] ;
  - transposition à la House [ORIGINAL].

### H17 Pluck deep chaud — Deep House, Organic House
- **Patch** :
  - OSC A en carré arrondi (Basic Shapes, WT POS entre scie et carrée), OCT −1, RAND 0.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 30 %, RES 10 %, VAR (FAT) 20 %.
  - ENV 2 → CUTOFF +35 %, decay 250 ms.
  - VOICING MONO + LEGATO, PORTA 40-60 ms, SCALED.
- **ENV 1** : attaque 3 ms, decay 500 ms, sustain −6 dB, release 120 ms.
- **FX** : Distortion Tape Sat. DRIVE 20, MIX 45 % ; Chorus en mode HPF, MIX 10-15 % ; passe-haut à 90 Hz.
- **Macros** : `Hollow` WT POS · `Snap` ENV 2 → CUTOFF 0 → 50 % · `Length` decay d'ENV 1 200 → 800 ms · `Round` CUTOFF 15 → 50 %.
- **Sub associé** : S12 (glissé Deep House) ou S13 sous 124 BPM.
- **Origine** :
  - Tape Sat. à mix inférieur à 50 % [SOURCE GEN-06] ;
  - Chorus en mode passe-haut, qui élargit seulement le haut [SOURCE F08-01, F12-02] ;
  - patch [ORIGINAL]. Les tutoriels deep house du registre (F03-08, F03-09) ne sont pas étudiés.

### H18 Hollow « wah » — filtre formant
- **Patch** :
  - H11, avec FILTER 1 en Formant-II.
  - ENV 2 → CUTOFF (qui morphe entre formants) : départ « oo », arrivée vers « a ». Decay 150-250 ms, sustain 0.
  - RES 20-35 %.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −10 dB, release 80 ms.
- **FX** : Equalizer, creux étroit sur le pic nasal s'il apparaît, puis passe-haut à 90 Hz.
- **Macros** : `Hollow` WARP 1 5 → 25 % · `Snap` ENV 2 → CUTOFF 0 → 60 % · `Length` decay d'ENV 2 80 → 400 ms · `Round` VAR (FORMNT).
- **Sub associé** : S01.
- **Test** : la voyelle se lit sur la note la plus jouée ; un formant fixe ne suit pas la note.
- **Origine** :
  - Formant-I/II/III, CUTOFF qui morphe entre formants, VAR = FORMNT [cartographie, § 6] ;
  - « oo » F2 870 Hz, « a » (lap) F2 1 700 Hz [SOURCE Synth Secrets 23 dans `../documentation-basses.md` § 2] ;
  - geste [ORIGINAL]. Le growl complet relève de F08.

### H19 Pluck laser — Future House, Bass House
- **Patch** :
  - H01 ou H11.
  - FX : Hyper/Dimension, RETRIG allumé (« zap laser à chaque note »), UNISON 3-5, DETUNE 20-40 %, MIX 15-30 %, SIZE de Dimension 0.
  - Passe-haut à 120 Hz après l'Hyper.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ, et `Snap` sur le MIX de l'Hyper 0 → 40 %.
- **Sub associé** : S01. L'Hyper reste au-dessus du passe-haut.
- **Jeu** : en réponse, sur les trous de la ligne principale (« laser » en appel et réponse).
- **Origine** :
  - Hyper RETRIG [cartographie, § 8] ;
  - basses « laser » en appel et réponse [SOURCE F05-12, sans valeurs] ;
  - réglages [ORIGINAL].

### H20 Hollow imprimé en table — moins de CPU, plus de contrôle
- **Patch** :
  1. Construire H11 ou H05.
  2. Menu principal › Render OSC Warp : 256 frames du warp de 0 à 100 %, à partir de la frame courante.
  3. Couper le warp. Le creux se joue désormais par WT POS.
  4. ENV 2 → WT POS : départ haut (riche), descente vers le bas (rond), decay 150-250 ms.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −10 dB, release 80 ms.
- **Macros** : `Hollow` WT POS de base · `Snap` ENV 2 → WT POS 0 → 100 % · `Length` decay d'ENV 1 · `Round` CUTOFF.
- **Sub associé** : S01.
- **Test** : A/B avec le patch d'origine. Le Render se fait sur la frame courante, sans les enveloppes : l'animation se recrée ensuite par WT POS.
- **Origine** :
  - Render OSC Warp [cartographie, § 9, menu principal] ;
  - ressampler et réimporter comme wavetable [SOURCE F02-02, Reese] ;
  - application au hollow [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f03-pluck-hollow.md`. Le bloc « Future House 126 — pluck en octaves » de `../motifs.md` complète ces trois motifs.

```grille
titre: Future House 128 — bounce en octaves (H06, H07)
tempo: 128
accords: Em7 | Em7
pluck: E1[1&:1] E2[1a:1] E1[2e:1] E1[2&:1] G1[3e:1] E2[3&:1] B1[4e:1] D2[4&:1] | E1[1&:1] E2[1a:1] E1[2e:1] E1[2&:1] B1[3&:2] A1[4&:1] G1[4a:1]
sub: E0[1&:2] E0[2&:2] E0[3&:2] B0[4&:2] | E0[1&:2] E0[2&:2] B0[3&:2] G0[4&:2]
```

Aucune attaque sur les doubles croches 1, 5, 9, 13 (kick). Le sub ne prend que les contretemps ; le rebond vient des octaves et de l'enveloppe, pas de notes en plus.

```grille
titre: G-House 124 — pluck grave clairsemé (H08, H09)
tempo: 124
accords: Gm7 | Gm7
pluck: G1[1&:2] G1[2a:1] Bb1[3&:1] G1[4e:1] F1[4&:2] | G1[1&:2] G1[2a:1] D2[3&:2] C2[4&:1] Bb1[4a:1]
sub: G0[1&:2] G0[2a:1] Bb0[3&:1] G0[4e:1] F0[4&:2] | G0[1&:2] G0[2a:1] D1[3&:2] C1[4&:1] Bb0[4a:1]
```

Peu de notes et des silences longs : la G-House laisse le kick et le clap respirer. Le sub suit la même ligne une octave plus bas.

```grille
titre: UK Garage 130 — hollow en 2-step (H02, H03)
tempo: 130
accords: Fm7 | Fm7
hollow: F1[1:3] F1[2&:1] Ab1[3e:2] F1[4&:2] | Eb1[1:3] Eb1[2&:1] C1[3e:2] Eb1[4&:2]
```

En 2-step, le kick n'est pas sur les quatre temps : la basse attaque avec le kick du temps 1. Recaler les autres attaques sur le vrai pattern de batterie. Le patch H02 descend au registre du sub : sans sub séparé, ce bloc se joue seul.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : les tables SawRoundedToSquare, Dist 8Bit Fwap, CrushWub et Allophone, et le type Flg L6+. Vérifier les destinations des macros.
- Lire sur le Mac la page EvoSounds (F03-02) pour confirmer ou corriger H08.
- Écouter chaque recette avec son sub, puis avec le kick, et en garder trois à cinq pour le morceau. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
