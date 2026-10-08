# Vingt recettes d'organ bass pour la House (famille F04)

Quatrième lot de recettes House : la basse d'orgue, des années 90 (Korg M1 « Organ 2 ») à la Deep House et au UK Garage. Rédigé le 05/10/2026. Sources :
- `../etudes-pages-house.md` (F04-01, F04-02) ;
- la recette du corpus `../../../../../producteur-live/modules/house-future-rave-bass-house-production/recipes/organ-bass-et-piano-house-m1.md`, désignée plus bas par « recette M1 » ;
- les tirettes, registrations, percussion, key click et Leslie de `../../../studio-grade-funk-keys-synth-sound-design/references/electromechanical-keys.md`, désigné par « fiche Hammond » ;
- la fiche 4 de `../families.md` et la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes aux vingt recettes

1. **Le 16′ est le sub.** Une organ bass empile des harmoniques sur une fondamentale. Ici, la fondamentale (tirette 16′) est jouée par un sub de `house-f01-sub.md`, S01 de préférence, sur sa piste. Le patch d'orgue garde les autres harmoniques.
   - Equalizer de la couche d'orgue : passe-haut juste sous sa première harmonique gardée, vers 1,5 fois la fondamentale de la note la plus grave.
   - Deux recettes gardent le 16′ dans le patch (O03 et O13) et le disent.
2. **Tessiture** : organ bass jouée en MIDI 36-48 (C1-C2, 65-131 Hz), mono [SOURCE recette M1]. Dans Serum, régler l'octave pour que la note jouée sonne à cette hauteur.
3. **Tirettes et harmoniques** [SOURCE fiche Hammond] :
   - les neuf tirettes donnent les harmoniques 1 (16′), 3 (5⅓′), 2 (8′), 4 (4′), 6 (2⅔′), 8 (2′), 10 (1⅗′), 12 (1⅓′) et 16 (1′) du 16′ ;
   - chaque cran vaut 3 dB : 8 = 0 dB, 7 = −3, 6 = −6, 5 = −9, 4 = −12, 3 = −15, 2 = −18, 1 = −21 dB, 0 = éteint ;
   - une registration s'écrit de gauche à droite, par exemple 888 000 000 = 16′, 5⅓′ et 8′ à fond.
4. **Mode Harmonics de Serum 2** : clic droit sur OCT ou SEM › Harmonics. La fréquence de base est multipliée par un harmonique entier (manuel, « Setting the Octave or Semitone Mode » ; cartographie, § 3.1). Trois oscillateurs plus le SUB font quatre tirettes, sans dessiner de table [DÉDUCTION].
5. **Niveaux en dB** : LEVEL des oscillateurs va de 0 à 100 % (−∞ à 0 dB), sans correspondance documentée. Régler les écarts de la registration à l'analyseur, d'après la hauteur des pics, plutôt qu'au pourcentage.
6. **Phase** : PHASE 0 % et RAND 0 sur tous les oscillateurs. Des harmoniques en phase fixe donnent la même attaque à chaque note, comme les roues phoniques d'un orgue toujours en rotation [DÉDUCTION].
7. **Quatre macros communes**, reprises de la fiche 4 de `../families.md` avec `Click` en plus :
   - `Drawbars` : équilibre des harmoniques ;
   - `Gate` : decay ou release d'ENV 1 ;
   - `Air` : coupure du filtre ;
   - `Click` : attaque percussive (key click ou percussion).
8. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
9. **Contrôle par l'utilisateur** :
   - l'orgue seul, puis avec son sub, puis avec le kick (909 dans la recette M1) ;
   - le contretemps doit porter ;
   - mono ;
   - la note la plus grave et la plus aiguë de la ligne ;
   - A/B à niveau égal contre O01.
   - Erreurs relevées par la recette M1 : release longue, fondamentale trop pleine, organ bass polyphonique.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| O01 | Orgue additif 888 en mode Harmonics | House 90s, Tech House | trois oscillateurs = trois tirettes |
| O02 | Orgue dessiné à l'éditeur d'harmoniques | toute House | une seule table, harmoniques 1-4 |
| O03 | Organ 2 en multisample | House 90s fidèle | échantillon, enveloppe de stab |
| O04 | Orgue façon Juno-6 | House 90s, Garage | impulsion à 33 %, filtre auto-oscillant |
| O05 | Triangle et carrée à la quinte | Bass House, Tech House | deux oscillateurs à +7 demi-tons |
| O06 | Orgue grondant au 32′ | Deep House sombre | sub une octave plus bas |
| O07 | Carrée filtrée de Garage | UK Garage, Speed Garage | stabs courts syncopés |
| O08 | Orgue deep qui respire | Deep House | table douce, LP + Peak |
| O09 | Percussion de Hammond | House 90s | attaque de la 2e ou 3e percussion |
| O10 | Key click | toutes | bouffée de bruit de 1-3 ms |
| O11 | Leslie lent au-dessus de 800 Hz | Deep House, Garage | modulation sur les aigus seulement |
| O12 | Vibrato scanner | Deep House | 7 Hz, très peu de profondeur |
| O13 | Registration « House Bass » | House 90s | 880 000 000 |
| O14 | Orgue en ligne tenue | Deep House, Garage | sustain 60-80 %, release 20 ms |
| O15 | Registration carrée | Garage, Nu-disco | harmoniques impairs du 8′ |
| O16 | Registration scie | Tech House | 83 4211 100 dessinée |
| O17 | Orgue saturé avant la réverb | Tech House, Bass House | overdrive puis réverb |
| O18 | Horn pluck | House 2010s | macro de l'orgue vers un pluck |
| O19 | Orgue filtré sur la mesure | Tech House | LFO d'une mesure sur la coupure |
| O20 | Orgue imprimé en table | toutes | Resample to, libère B et C |

## Les vingt recettes

### O01 Orgue additif 888 en mode Harmonics — référence de la famille
- **Patch** (registration 888 000 000 : 16′, 5⅓′, 8′ à fond) :
  - 16′ (harmonique 1) : sub S01 sur sa piste.
  - OSC A en sinus (Default, position 1), mode Harmonics = 2 : le 8′, à 0 dB.
  - OSC B en sinus, mode Harmonics = 3 : le 5⅓′, à 0 dB (même hauteur de pic que A).
  - OSC C éteint.
  - PHASE 0 %, RAND 0 partout. Pas de filtre.
- **ENV 1** : attaque 1 ms, decay 200 ms, sustain −12 dB, release 20 ms (stab de la recette M1 : D 150-300 ms).
- **FX** : Equalizer en passe-haut à 1,5 × la fondamentale de la note la plus grave, par exemple 98 Hz pour C1.
- **Macros** : `Drawbars` LEVEL d'OSC B de −∞ à 0 dB · `Gate` decay d'ENV 1 100 → 400 ms · `Air` — (pas de filtre) · `Click` voir O10.
- **Sub associé** : S01, même ligne, même enveloppe courte (S11 pour un sub en contretemps).
- **Jeu** : motif « Classic House 124 — orgue en contretemps » ci-dessous.
- **Origine** :
  - registration 888 000 000 [SOURCE fiche Hammond, setBfree « Jimmy Smith »] ;
  - mode Harmonics [DOC, manuel] ;
  - « 16′ = sub » [ORIGINAL], au service de la règle « Grave » d'`AGENTS.md`.

### O02 Orgue dessiné à l'éditeur d'harmoniques — une seule table
- **Patch** :
  - OSC A, éditeur de wavetable, harmoniques 2, 3 et 4 dessinés (88 8000 000 sans le 16′) : harmonique 3 en avant, 2 et 4 à −3 dB.
  - OSC B en sinus, une octave au-dessus de A, niveau réduit (fiche 4 de `../families.md`) : en option, pour la brillance.
  - PHASE 0 %, RAND 0. FILTER 1 en MG Low 12 très ouvert (≈ 70 %).
- **ENV 1** : attaque 2 ms, decay 250 ms, sustain −10 dB, release 25 ms.
- **FX** : passe-haut à 1,5 × la fondamentale la plus grave.
- **Macros** : `Drawbars` LEVEL d'OSC B 0 → 40 % · `Gate` decay 120 → 400 ms · `Air` CUTOFF 40 → 100 % · `Click` voir O10.
- **Sub associé** : S01.
- **Origine** :
  - additif aux harmoniques 1, 2, 3, 4, la 3e en avant (tirettes 88 8000 000) [SOURCE recette M1, `[DOC-2]`] ;
  - éditeur d'harmoniques de la table (`../families.md`, fiche 4) ;
  - le « mode harmonique Serum 2 » cité par l'ancienne fiche reste à vérifier : O01 utilise le mode Harmonics du manuel.

### O03 Organ 2 en multisample — la voie fidèle
- **Patch** :
  - OSC A en moteur Multisample (ou Sample), chargé avec un échantillon de l'Organ 2 du Korg M1 que l'utilisateur a le droit d'utiliser (M1 logiciel qu'il possède, pack sous licence).
  - MONO, LEGATO, PORTA 0.
- **ENV 1** :
  - stab : attaque 0-2 ms, decay 150-300 ms, sustain 0 ;
  - ligne : sustain 60-80 %, release 20 ms (voir O14).
- **FX** : aucun dans le patch (le son d'origine est « practically unprocessed », selon F04-02). Hors Serum, dans la recette M1 : hall court et chorus léger, mono sous 120 Hz, sidechain 2-4 dB.
- **Grave** : l'échantillon contient sa fondamentale. Garder le patch seul (sans sub), ou passe-haut à 90 Hz et S01 dessous. Comparer les deux à niveau égal.
- **Macros** : `Drawbars` — · `Gate` decay 100 → 400 ms · `Air` Filter FX MG Low 12 de 2 à 12 kHz · `Click` attaque 0 → 5 ms (inversée : plus d'attaque = moins de clic).
- **Sub associé** : aucun, ou S01.
- **Origine** :
  - l'Organ 2 (I17) est le son de « Show Me Love », « Gypsy Woman », « Push The Feeling On » ; « Vogue = Organ 2 » est faux ; c'est un son PCM, donc le multisample est la voie fidèle [SOURCE recette M1] ;
  - table échantillonnée sur l'Organ 2, « practically unprocessed » [SOURCE F04-02, page].
- **Droits** : ne pas reprendre la ligne de basse d'un morceau existant ni un échantillon sans licence (`AGENTS.md`, règle Référence).

### O04 Orgue façon Juno-6 — 888 000 000 en soustractif
- **Patch** :
  - OSC A en carrée (Basic Shapes), WARP 1 en PWM réglé pour une impulsion de 33 % : vérifier en vue 2D qu'un tiers du cycle est haut. Une impulsion à 33 % supprime un harmonique sur trois.
  - SUB en Square, une octave sous A, LEVEL au maximum : il joue le 16′ dans ce patch.
  - FILTER 1 sur A et SUB : Low 24, RES ≈ 100 % (auto-oscillation), key track allumé, CUTOFF accordé 19 demi-tons au-dessus du SUB (le 5⅓′).
  - Pour accorder : jouer une note, couper A et SUB, monter la résonance jusqu'à entendre le filtre siffler, l'accorder à l'accordeur, puis baisser un peu la résonance.
  - ENV 2 → CUTOFF, instantanée (attaque 0, decay 2-5 ms, sustain 0) : c'est le clic.
- **ENV 1** : en porte (attaque 0, sustain 100 %, release 10 ms) ; la note dure ce que dure le MIDI.
- **Grave** : le SUB carré traverse le filtre. Pour respecter la séparation, passe-haut à 90 Hz sur la sortie et S01 sur sa piste, ou bien patch seul (choix à faire à l'écoute).
- **Macros** : `Drawbars` RES 70 → 100 % · `Gate` release 5 → 60 ms · `Air` CUTOFF ± 2 demi-tons · `Click` ENV 2 → CUTOFF 0 → 100 %.
- **Sub associé** : S01, si la couche est filtrée.
- **Origine** :
  - recette Juno-6 « 888 000 000 » : pulse 33,3 %, sub carré −1 octave à fond, VCF à résonance 100 % auto-oscillant 19 demi-tons au-dessus du sub, VCA en porte, clic par une enveloppe de filtre instantanée [SOURCE fiche Hammond, Synth Secrets 55-56] ;
  - limite dite : « réaliste pour 888 000 000 seulement ».

### O05 Triangle et carrée à la quinte — Bass House, Tech House
- **Patch** :
  - OSC A en triangle (Basic Shapes), OCT −2 par rapport au réglage d'origine.
  - OSC B en carrée, SEM +7 (une quinte au-dessus), LEVEL 40-60 %.
  - FILTER 1 sur A et B, MG Low 12, CUTOFF ≈ 40 %, réglé à l'oreille.
  - PHASE 0 %, RAND 0.
- **ENV 1** : attaque 1 ms, decay 220 ms, sustain −12 dB, release 25 ms.
- **FX** : Distortion Tube légère, puis passe-haut à 90 Hz.
- **Registre** : régler l'octave de A pour que la note sonne en C1-C2.
- **Macros** : `Drawbars` LEVEL d'OSC B 0 → 70 % · `Gate` decay 100 → 400 ms · `Air` CUTOFF 20 → 70 % · `Click` voir O10.
- **Sub associé** : S01.
- **Origine** :
  - « EDMProd : triangle −2 oct + carrée +7 st, LP à goût » [EXTRAIT, cité par la recette M1 en `[DOC-EXTRAIT]`/`[DOC-2]`, page EDMProd non lue dans ce lot] ;
  - valeurs [ORIGINAL].

### O06 Orgue grondant au 32′ — Deep House sombre
- **Patch** : O01, avec deux changements.
  - Le sub joue une octave sous l'orgue (le « 32′ ») au lieu de la même octave.
  - OSC C en triangle ou en scie filtrée, à la hauteur du 16′, LEVEL bas : le « grondement ».
- **Registre** : orgue en C2-C3, sub en C1-C2. Le sub ne descend donc pas sous 65 Hz.
- **ENV 1** : attaque 2 ms, decay 400 ms, sustain −6 dB, release 40 ms.
- **FX** : Reverb Hall courte (SIZE 20-30 %, MIX ≤ 10 %, LO CUT haut) et Chorus léger, puis passe-haut sous la première harmonique gardée.
- **Macros** : `Drawbars` LEVEL d'OSC C 0 → 50 % · `Gate` decay 200 → 700 ms · `Air` Filter FX MG Low 12 · `Click` voir O10.
- **Sub associé** : S01 une octave plus bas que l'orgue, ou S13 sous 124 BPM.
- **Origine** :
  - « triangle ou saw mêlé à 32′ pour le grondement » ; « hall court + chorus léger » [EXTRAIT MusicRadar, cité par la recette M1 en `[DOC-EXTRAIT]`] ;
  - transposition [ORIGINAL].

### O07 Carrée filtrée de Garage — stabs courts syncopés
- **Patch** :
  - OSC A en carrée (Basic Shapes), PHASE 0 %, RAND 0.
  - FILTER 1 en MG Low 24, CUTOFF ≈ 30 %, RES 10 %. ENV 2 → CUTOFF +40 %, decay 80 ms.
- **ENV 1** : attaque 0,5 ms, decay 120 ms, sustain −∞, release 15 ms.
- **FX** : passe-haut à 90 Hz, puis Compressor Single 3:1.
- **Macros** : `Drawbars` WT POS de la carrée vers la scie · `Gate` decay 60 → 250 ms · `Air` CUTOFF 15 → 50 % · `Click` ENV 2 → CUTOFF 0 → 70 %.
- **Sub associé** : S11.
- **Jeu** : motif « UK Garage 130 — stabs d'orgue en 2-step » ci-dessous.
- **Origine** : « UKG : carrée filtrée en stabs courts syncopés » [SOURCE recette M1, `[DOC-2]`] ; valeurs [ORIGINAL].

### O08 Orgue deep qui respire — Deep House
- **Patch** :
  - OSC A sur une table douce : Analog (Basic Shapes entre sinus et triangle). La table de l'auteur (« ACVSTI Bad Signs ») n'est pas téléchargée.
  - FILTER 1 en LP (dual Low + Peak, catégorie Multi), CUTOFF ≈ 35 %, VAR (FREQ du Peak) une octave et demie au-dessus, RES 20 %.
  - ENV 2 → CUTOFF +25 %, attaque 10 ms, decay 400 ms, sustain 30 % : le son « respire » sans trop d'aigus.
- **ENV 1** : attaque 3 ms, decay 500 ms, sustain −4 dB, release 60 ms.
- **FX** : passe-haut à 90 Hz.
- **Macros** : `Drawbars` VAR (FREQ du Peak) · `Gate` decay 200 → 800 ms · `Air` CUTOFF 20 → 60 % · `Click` attaque d'ENV 2 0 → 30 ms (inversée).
- **Sub associé** : S01. Selon la page, le sous-oscillateur sort en DIRECT OUT : ici, sur sa piste.
- **Origine** :
  - tables « pas trop agressives », sub en DIRECT OUT, enveloppe sur la coupure pour que le son « respire », filtre « multi stage » passe-bas + peak [SOURCE F04-01, page ; vidéo non visionnée] ;
  - choix du type LP de Serum 2 et valeurs [ORIGINAL].

### O09 Percussion de Hammond — l'accent d'attaque
- **Patch** : O01, plus un oscillateur de percussion.
  - OSC C en sinus, mode Harmonics = 4 (percussion « 2nd », le 4′) ou = 6 (« 3rd », le 2⅔′).
  - ENV 3 → LEVEL d'OSC C : attaque 0, decay 150-400 ms (réglage « fast » raccourci pour une basse), sustain 0.
  - VOICING MONO + LEGATO : comme sur l'orgue, la percussion ne se déclenche pas sur une note liée.
  - Pour qu'ENV 3 suive cette règle, ne pas cocher Legato Inverted.
- **ENV 1** : comme O01.
- **Macros** : `Drawbars` LEVEL d'OSC B · `Gate` decay d'ENV 1 · `Air` — · `Click` decay d'ENV 3 → LEVEL de C, 0 → 400 ms.
- **Sub associé** : S01.
- **Test** : sur une ligne en partie liée, seules les notes détachées doivent porter l'accent.
- **Origine** :
  - percussion 2nd (4′) ou 3rd (2⅔′) en accent d'attaque, single-trigger (pas de percussion si une note est déjà tenue), Fast/Slow = 1 s / 4 s dans setBfree [SOURCE fiche Hammond] ;
  - decay plus court pour une basse [ORIGINAL] ; Legato Inverted [cartographie, § 7.1].

### O10 Key click — la bouffée de l'attaque
- **Patch** : n'importe quelle recette d'orgue de ce fichier, plus le NOISE.
  - NOISE allumé, couleur White ou Pink, STEREO 0, routé `Main`.
  - ENV 4 → LEVEL du NOISE : attaque 0, decay 1-3 ms, sustain 0, release 1 ms.
  - Variante : ENV 2 instantanée sur la coupure (voir O04), ou attaque d'ENV 1 à 0 avec PHASE non nulle.
- **Macros** : `Click` quantité d'ENV 4 → LEVEL du NOISE, de 0 à −6 dB sous le pic de l'orgue.
- **Test** : le clic doit se percevoir comme une attaque, pas comme un hat. À couper si le kick et le hat suffisent.
- **Origine** :
  - key click : bouffée de 0,6-2,9 ms, niveau 0,5 à l'attaque, 0,25 au relâchement dans setBfree ; « défaut de conception devenu signature » [SOURCE fiche Hammond] ;
  - key click de 5-15 ms par enveloppe de filtre [SOURCE recette M1] ;
  - mise en œuvre par le NOISE [ORIGINAL].

### O11 Leslie lent au-dessus de 800 Hz — Deep House, Garage
- **Patch** : O01 ou O02, avec un Leslie limité aux aigus.
  - Rack FX : Splitter L/H, SPLIT FREQ 800 Hz.
  - LOWS : rien (pas de modulation dans le grave).
  - HIGHS : Chorus RATE 0,67 Hz, DEPTH bas, MIX 30-50 %, puis Utility WIDTH ≤ 120.
- **Macros** : `Drawbars` comme la recette de départ · `Gate` decay d'ENV 1 · `Air` MIX du Chorus 0 → 60 % · `Click` voir O10.
- **Sub associé** : S01, qui reste fixe.
- **Test** : en mono, la modulation ne doit pas creuser le niveau ; dans le drop, elle ne doit pas brouiller le contretemps.
- **Origine** :
  - Leslie : crossover 800 Hz, horn lent à 0,67 Hz (40,3 rpm), tambour lent à 0,60 Hz, Doppler ±1 % [SOURCE fiche Hammond] ;
  - Leslie limité aux aigus pour une basse, et Chorus comme imitation [DÉDUCTION] : ce n'est pas une simulation de Leslie.

### O12 Vibrato scanner — Deep House
- **Patch** : O01, plus un vibrato.
  - LFO 1 en sinus, HZ, RATE 7 Hz, mode FREE, MONO allumé.
  - LFO 1 → FIN d'OSC A et d'OSC B, ±3 à ±8 cents (profondeur V1 de l'orgue).
  - LFO 1 DELAY 0,2 s, RISE 0,3 s : les notes courtes restent stables.
  - Le sub S01 ne reçoit pas de vibrato.
- **Macros** : `Drawbars` LEVEL d'OSC B · `Gate` decay d'ENV 1 · `Air` profondeur du vibrato 0 → ±10 cents · `Click` voir O10.
- **Sub associé** : S01.
- **Test** : sur une note tenue, la couche doit onduler sans désaccorder le grave. Si le battement avec le sub gêne, réduire la profondeur.
- **Origine** :
  - scanner ≈ 7 Hz ; V1/V2/V3 = profondeurs 1 / 2,5 / 5 ; « le chorus Hammond ne mélange qu'une seule instance modulée » [SOURCE fiche Hammond] ;
  - la conversion en cents [ORIGINAL] : la profondeur V1 n'est pas donnée en cents.

### O13 Registration « House Bass » — 880 000 000
- **Patch** (16′ et 5⅓′ seuls) :
  - Version séparée : sub S01 pour le 16′ ; OSC A en sinus, Harmonics = 3, à 0 dB. Passe-haut à 2,5 × la fondamentale la plus grave.
  - Version tout-en-un (le patch garde le 16′) : OSC A en sinus, Harmonics = 1, routé `Direct` ; OSC B en sinus, Harmonics = 3, routé `Main`.
  - Dans les deux cas, PHASE 0 % et RAND 0.
- **ENV 1** : attaque 1 ms, decay 250 ms, sustain −10 dB, release 20 ms.
- **Macros** : `Drawbars` LEVEL de l'harmonique 3, de −9 à 0 dB · `Gate` decay 120 → 400 ms · `Air` — · `Click` voir O10.
- **Sub associé** : S01 (version séparée).
- **Main gauche** : la registration associée, L : 008 080 000 (8′ et 2⅔′), pour un accord d'accompagnement sur une autre piste.
- **Origine** : registration « House Bass 880 000 000 (L : 008 080 000) » de setBfree `default.pgm` [SOURCE fiche Hammond].

### O14 Orgue en ligne tenue — Deep House, Garage
- **Patch** : O01 ou O02, avec VOICING MONO + LEGATO, PORTA 0.
- **ENV 1** : attaque 1 ms, decay 300 ms, sustain −2 à −4 dB (≈ 60-80 %), release 20 ms.
- **FX** : comme la recette de départ.
- **Macros** : `Drawbars` · `Gate` release 10 → 60 ms · `Air` · `Click`, comme la recette de départ.
- **Sub associé** : S02, à phase continue, pour les notes liées.
- **Jeu** : motif « Deep House 122 — orgue tenu » ci-dessous.
- **Origine** : enveloppe de ligne « S 60-80 % R 20 ms », MONO, LEGATO, PORTA 0 [SOURCE recette M1] ; correspondance en dB [ORIGINAL].

### O15 Registration carrée — 00 8030 200
- **Patch** (harmoniques impairs du 8′) :
  - OSC A en sinus, Harmonics = 1 : le 8′, qui devient la fondamentale. Jouer une octave plus haut qu'O01.
  - OSC B en sinus, Harmonics = 3 : le 2⅔′ à 3, soit −15 dB sous A.
  - OSC C en sinus, Harmonics = 5 : le 1⅗′ à 2, soit −18 dB sous A.
  - PHASE 0 %, RAND 0.
- **ENV 1** : attaque 1 ms, decay 200 ms, sustain −12 dB, release 20 ms.
- **FX** : passe-haut sous la fondamentale de A, sub dessous.
- **Macros** : `Drawbars` LEVEL de B et C ensemble · `Gate` decay 100 → 400 ms · `Air` — · `Click` voir O10.
- **Sub associé** : S01, à la hauteur du 8′, c'est-à-dire de la note jouée.
- **Origine** :
  - « 00 8030 200 ≈ carré » [SOURCE fiche Hammond] ;
  - harmoniques 2, 6 et 10 du 16′ = 1, 3 et 5 du 8′ ; niveaux à 3 dB par cran [CALCUL].

### O16 Registration scie — 83 4211 100
- **Patch** :
  - OSC A, éditeur de wavetable : dessiner la registration 83 4211 100 sans le 16′, puisque le sub le joue. Harmoniques du 16′ :
    - 3 (5⅓′) à −15 dB ;
    - 2 (8′) à −12 dB ;
    - 4 (4′) à −18 dB ;
    - 6 (2⅔′), 8 (2′) et 10 (1⅗′) à −21 dB.
  - FILTER 1 en MG Low 12, CUTOFF ≈ 50 %, ENV 2 → CUTOFF +30 %, decay 150 ms.
  - PHASE 0 %, RAND 0.
- **Niveaux** : relatifs au 16′ (8 = 0 dB). Sans le 16′, l'ensemble est plus faible : compenser au LEVEL.
- **ENV 1** : attaque 1 ms, decay 250 ms, sustain −10 dB, release 25 ms.
- **FX** : Distortion Tape Sat. légère, passe-haut à 1,5 × la fondamentale la plus grave.
- **Macros** : `Drawbars` WT POS si plusieurs registrations sont dessinées en frames · `Gate` decay 100 → 400 ms · `Air` CUTOFF 30 → 80 % · `Click` ENV 2 → CUTOFF 0 → 50 %.
- **Sub associé** : S01 (le 16′ à 8).
- **Origine** : « 83 4211 100 ≈ dent de scie » et 3 dB par cran [SOURCE fiche Hammond] ; niveaux [CALCUL].

### O17 Orgue saturé avant la réverb — Tech House, Bass House
- **Patch** : O01, O02 ou O16, avec une chaîne FX dans cet ordre :
  1. Distortion Overdrive (ou Tube), DRIVE 25-45, MIX 70-100 %.
  2. Equalizer : creux de 2-3 dB vers 300 Hz si le son devient « boxy », passe-haut sous la première harmonique gardée.
  3. Reverb Plate, SIZE 20 %, MIX ≤ 8 %, LO CUT haut.
- **ENV 1** : attaque 1 ms, decay 200 ms, sustain −12 dB, release 20 ms.
- **Macros** : `Drawbars` · `Gate` comme la recette de départ · `Air` DRIVE 0 → 60 · `Click` voir O10.
- **Sub associé** : S01. La saturation reste dans la couche d'orgue.
- **Origine** :
  - « overdrive avant reverb » dans la chaîne Hammond/Leslie [SOURCE fiche Hammond] ;
  - creux vers 300-500 Hz contre le son « boxy » [SOURCE F07-01, page] ;
  - valeurs [ORIGINAL].

### O18 Horn pluck — de l'orgue au pluck de cuivre
- **Patch** : O02, plus un passage vers le pluck piloté par une seule macro, `Click`.
  - OSC B en scie, même octave que A, LEVEL de 0 à 50 %.
  - FILTER 1 en MG Low 24 : CUTOFF de 70 à 30 %, ENV 2 → CUTOFF de 0 à +50 % avec decay 120 ms.
  - Decay d'ENV 1 de 250 à 150 ms.
- **ENV 1** : comme O02, avec un decay plus court au maximum de la macro.
- **Macros** : `Drawbars` LEVEL d'OSC A · `Gate` decay d'ENV 1 · `Air` CUTOFF de base · `Click` passage orgue → horn pluck, 0 → 100 %.
- **Sub associé** : S01.
- **Origine** :
  - une macro transforme l'orgue M1 en « horn pluck » de « Rattle » (Bingo Players) ; valeurs et cibles non écrites [SOURCE F04-02, page] ;
  - cibles et bornes [ORIGINAL] ;
  - pour les vrais cuivres : `../../../studio-grade-brass-sound-design/GUIDE.md`.

### O19 Orgue filtré sur la mesure — Tech House
- **Patch** : O02 ou O16.
  - LFO 1 → CUTOFF de FILTER 1 (MG Low 12), BPM, RATE 1 bar, mode FREE, HOST allumé : le filtre s'ouvre et se ferme sur chaque mesure, calé sur le transport.
  - Forme : montée lente sur trois temps, retombée sur le quatrième.
  - Quantité +20 à +40 %.
- **ENV 1** : attaque 1 ms, decay 200 ms, sustain −12 dB, release 20 ms.
- **Macros** : `Drawbars` · `Gate` comme la recette de départ · `Air` quantité LFO 1 → CUTOFF 0 → 50 % · `Click` voir O10.
- **Sub associé** : S11 ; le filtre ne touche pas le sub.
- **Test** : relancer la lecture depuis plusieurs mesures : l'ouverture doit toujours tomber au même temps.
- **Origine** : HOST et modes de LFO [cartographie, § 7.2] ; geste [ORIGINAL].

### O20 Orgue imprimé en table — libère OSC B et C
- **Patch** :
  1. Construire O01, O13 ou O15 en mode Harmonics.
  2. Menu principal › Resample to : Serum joue une note pendant une mesure et l'importe comme wavetable dans l'oscillateur choisi.
  3. Couper les autres oscillateurs. Rejouer et comparer.
  4. OSC B et C sont libres pour un key click par le moteur Sample, une percussion (O09) ou un horn pluck (O18).
- **ENV 1** : comme le patch d'origine.
- **Macros** : celles du patch d'origine, avec `Drawbars` sur WT POS si plusieurs registrations ont été imprimées.
- **Sub associé** : S01.
- **Test** : A/B entre l'original et la version imprimée, sur trois notes. Le Resample prend une seule note : vérifier que la table suit bien les autres hauteurs.
- **Origine** : Resample to [cartographie, § 9, menu principal] ; usage [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Contretemps sur le troisième pas de chaque temps, gate de 50 à 60 % de la croche, fondamentale et octave [SOURCE recette M1, `[HEUR-lu]`]. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f04-organ-bass.md`.

```grille
titre: Classic House 124 — orgue en contretemps (O01, O03, O13)
tempo: 124
accords: Am7 | Fmaj7
organ: A1[1&:1] A1[2&:1] A2[2a:1] A1[3&:1] G1[4&:1] A1[4a:1] | F1[1&:1] F1[2&:1] F2[2a:1] F1[3&:1] G1![4&:1] E1[4a:1]
sub: A0[1&:1] A0[2&:1] A0[3&:1] G0[4&:1] | F0[1&:1] F0[2&:1] F0[3&:1] E0[4&:1]
```

Ligne originale, sans reprise d'un morceau existant. Notes d'une double croche sur le « & » : environ 50 % de la croche. Le sol de la mesure 2 est une note de passage voulue vers le mi.

```grille
titre: Deep House 122 — orgue tenu (O08, O14)
tempo: 122
accords: Cm7 | Abmaj7
organ: C2[1&:3] Eb2[2a:2] G1[3a:3] Bb1[4a:1] | Ab1[1&:3] C2[2a:2] Eb2[3a:3] G1[4a:1]
sub: C1[1&:3] C1[2a:2] G0[3a:3] Bb0[4a:1] | Ab0[1&:3] Ab0[2a:2] Eb1[3a:3] G0[4a:1]
```

Aucune attaque sur un kick. Les tenues de trois doubles croches recouvrent le kick suivant : régler la release du sub (S02) ou un sidechain de 2-4 dB.

```grille
titre: UK Garage 130 — stabs d'orgue en 2-step (O07)
tempo: 130
accords: Fm7 | Fm7
organ: F1[1:1] F1[1a:1] Ab1[2&:1] F1[3e:1] C2[3a:1] Eb2[4&:1] | F1[1:1] F1[1a:1] Ab1[2&:1] F1[3e:1] Eb1[4:1] C1[4a:1]
```

En 2-step, le kick n'est pas sur les quatre temps. Le stab attaque avec le kick du temps 1 ; recaler les autres sur le vrai pattern de batterie.

## Ce qui reste à faire par l'utilisateur

- Vérifier dans Serum 2 le mode Harmonics (clic droit sur OCT ou SEM), le menu Resample to, le type de filtre LP (Low + Peak) et les destinations des macros.
- Pour O03 : choisir un échantillon d'Organ 2 dont il a les droits.
- Lire sur le Mac la page EDMProd citée par O05, si l'on veut les vrais réglages.
- Écouter chaque recette avec son sub, puis avec le kick, et en garder trois à cinq pour le morceau. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
