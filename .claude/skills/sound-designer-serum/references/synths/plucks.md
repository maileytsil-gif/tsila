# Vingt recettes de plucks dans Serum 2

Deuxième fichier du lot de synthés. Rédigé le 05/10/2026. Sources :
- l'étude des quinze tutoriels de plucks, PL-01 à PL-15, de `../tutoriels-synths-serum.md`, et sa synthèse `../synths-serum-synthese.md` (section Pluck) ;
- la fiche pluck de `../leads-nappes-textures.md` (§ 1 : physique de la corde, patch chiffré, FM contre soustractif) ;
- la cartographie de Serum 2 (`../serum2-cartographie.md`), le Clip et l'arpégiateur (`../serum2-fx-clip-arp.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes : **[SOURCE PL-nn]**, **[FICHE]**, **[CALCUL]**, **[DÉDUCTION]**, **[ORIGINAL]**, comme dans `leads.md`.

## Règles

Les dix règles communes au lot sont dans `leads.md` : pas de sub dans le patch, Init Preset, noms de Serum 2, macros `Tone`, `Motion`, `Dirt`, `Space`, plug-ins tiers après Serum, un seul élément large, C3 = 60, droits, sortie à −6 dBFS, contrôle par l'utilisateur. Ce qui s'ajoute pour les plucks :

1. **Le filtre tombe plus vite que le volume** [FICHE]. Ce qui fait un pluck, c'est que les harmoniques disparaissent avant le son. Decay de l'enveloppe du filtre ≈ 60-70 % de celui d'ENV 1. Un decay d'ampli court sur un filtre fixe donne un son coupé, pas un pluck.
2. **High Pass entre 120 et 200 Hz** en fin de chaîne. Deux recettes jouent dans le médium grave (PK15, PK16, « plucks-basses ») : elles gardent le High Pass vers 120 Hz, et le grave vient d'un sub sur sa piste (`../../modules/serum-2-basses-house-future-house/references/recettes/dnb-f01-sub.md`).
3. **L'attaque se fabrique** par l'un de trois gestes, chaque fiche dit lequel :
   - une enveloppe très courte (≈ 20 ms) vers **Main Tuning** ;
   - un bruit d'attaque en **one-shot** (NOISE) ;
   - une couche transitoire séparée [FICHE] : decay ≈ 25-30 ms, gain ≈ −6 dB, passe-haut ≈ 140 Hz pour ne pas manger le kick.
4. **La vélocité ouvre le filtre** : notes douces plus sombres (PL-01, PL-02, PL-07). Matrice : Velo → CUTOFF, ou Velo en Aux Source de la ligne ENV 2 → CUTOFF.
5. **Un pluck statique lasse** : chaque recette désigne une macro à automatiser sur la durée (decay, cutoff ou rate du LFO). C'est le geste naturel pour varier avant une frontière de huit mesures (règle « Drops »).
6. **Référence A/B du fichier** : PK01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| PK01 | Bambou creux | Deep house, tropical, référence A/B | sinus et carrée à −5 st, FM (Sub), LFO « knock » sur CRS, valeurs dictées |
| PK02 | Pluck melodic automatisé | Melodic, progressive house | saw + sinus, MG Low 18 à 138 Hz, deux macros jouées note à note |
| PK03 | Pluck « marble » | Deep house sombre | deux tables Digital, ENV 2 sur cinq cibles, NoteOn Rand sur la résonance |
| PK04 | LFO pluck | Melodic et afro house | rampe descendante en Hz sur niveaux et cutoff, macro `Rate` |
| PK05 | Pluck joué par le Clip | Afro house mélodique | motif du Clip de Serum 2, trémolo granuleux 1/128 |
| PK06 | Saw afro et bruit | Afro house | saw, enveloppe de filtre, Bright White par macro |
| PK07 | Afro à table mouvante | Afro house | LFO 0,7 Hz RETRIG sur WT POS, seconde couche large |
| PK08 | Marimba sinus | Future house, deep | sinus propre, clic de 20 ms sur Main Tuning, accord à la dixième |
| PK09 | Accords rythmés par LFO | Progressive house | accords tenus, LFO RETRIG sur le cutoff |
| PK10 | Deep soustractif chiffré | Deep house, minimal | filtre à 60-70 % du decay d'ampli |
| PK11 | Pluck FM bois ou verre | Deep, minimal | FM (B) à rapport 2:1 ou 3,51:1, ENV 2 sur la quantité |
| PK12 | Pluck tech house sec | Tech house | couche transitoire séparée, Acid Ladder court |
| PK13 | Pluck à table dessinée | DnB liquide | deux frames (sinus, carré) en morph Spectral, LFO sur WT POS |
| PK14 | Pluck liquide qui suit la note | DnB liquide | unison 9, Low 24 à 142 Hz, EQ dont la fréquence suit Note# |
| PK15 | Pluck-basse dancefloor | DnB dancefloor | deux carrées à la quinte, LFO ENVELOPE, distorsion PRE HP 400 Hz |
| PK16 | Pluck répété par LFO | DnB moderne | LFO RETRIG en Hz automatisé, coup de pitch bend final |
| PK17 | Progressif à deux couches | Melodic dubstep, progressive | centre à une voix, octave en unison 7, MG Low 24 drivé |
| PK18 | Arp future bass | Future bass, melodic dubstep | saw + octave unison 7, macro de cutoff en cloche |
| PK19 | Pluck Au5 | Melodic dubstep | sinus Bend +, Downsample au point près, Guitar Mute en one-shot |
| PK20 | Accords pulsés en triolets | Melodic dubstep, future bass | accords tenus, LFO RETRIG en 1/8 triolet |

## Les vingt recettes

### PK01 Bambou creux — référence du fichier
- **Patch** [SOURCE PL-05, valeurs dictées] :
  - OSC A : Analog « BD Sine », SEM **−5**, WT POS 0, WARP 1 **FM (Sub)** **18 %**, LEVEL **63**.
  - OSC B : Basic Shapes, frame de la carrée (« 4 »), SEM **−5**, UNISON **2**, **FM (Sub)** **36 %**.
  - SUB : sinus, OCT 0, **LEVEL 0** : il ne sert que de modulateur FM, il ne sort aucun son (règle 1 de `leads.md` tenue).
  - NOISE « Kick Attack » [ASR ? « kick attack 25 »], PHASE (START) 17, LEVEL 0 ; ENV 3 → LEVEL du NOISE **68**.
  - OSC B → FILTER 1 **MG Low 24**, CUTOFF au minimum, RES 0, DRIVE **37 %**.
  - ENV 2 → CUTOFF **75**. ENV 2 : DEC **298 ms**, SUS ≈ 0, REL **220 ms**.
  - ENV 3 : DEC **65 ms**, SUS 0, REL **13 ms**.
  - LFO 1, forme « pluck » dessinée → **CRS** d'OSC A et d'OSC B **45**, → CUTOFF **100** : c'est le « knock ».
  - VOICING **MONO**.
- **ENV 1** : DEC **433 ms**, SUS ≈ 0, REL **320 ms** [SOURCE PL-05].
- **Contrôle de la règle du filtre** [CALCUL] : 298 ms / 433 ms = 69 % ; le patch dicté tombe dans la plage de la fiche.
- **LFO 1** [ORIGINAL, la forme est « à vérifier à l'écran »] : mode ENVELOPE, une descente raide en 1/16. Combien de demi-tons donne « 45 » vers CRS (course −64…+64) ne se déduit pas de la transcription : lire la valeur au survol du bouton et la noter.
- **FX** [SOURCE PL-05] : Compressor **Multiband** (« ajoute du clic ») → Hyper/Dimension (Hyper MIX 15, Dimension SIZE 14, MIX 14) → Equalizer, aigus retirés vers **6 kHz**, bande basse en High Pass à 150 Hz [règle 2] → Reverb **Hall** : SIZE **34**, DECAY **3,4 s**, LO CUT **30**, HI CUT **63**, MIX **22**.
- **Macros** : `Tone` CUTOFF 0 → 30 % · `Motion` LFO 1 → CRS 20 → 60 · `Dirt` DRIVE 20 → 60 % · `Space` MIX de la Hall 10 → 35 %. Macro à automatiser : `Motion`.
- **Jeu** : MIDI 62 à 79. Les deux oscillateurs à −5 demi-tons : le patch sonne une quarte sous la note jouée [CALCUL] ; écrire la ligne une quarte au-dessus de la hauteur voulue, ou mettre SEM 0 sur les deux.
- **Test** : le knock doit s'entendre comme un coup de bois, pas comme une glissade ; si on entend la glissade, raccourcir le LFO 1.

### PK02 Pluck melodic automatisé
- **Patch** [SOURCE PL-07, valeurs dictées] :
  - OSC A : table par défaut (saw), LEVEL **47 %**. OSC B : sinus, LEVEL **79 %**. NOISE actif, LEVEL 0 ; ENV 1 → LEVEL du NOISE **60**.
  - FILTER 1 **MG Low 18** (corrigé dans la vidéo, pas 24), sur tout, CUTOFF **138 Hz**, RES 0, DRIVE **29**.
  - ENV 2 → CUTOFF **72**. ENV 2 : DEC **1,05 s** [ASR ?], SUS 63 [unité douteuse], REL **486 ms**.
  - ENV 3 : DEC 1,64 s [ASR ?], SUS 0, courbe tirée au milieu ; ENV 3 → CUTOFF (probable) **10** : petite attaque.
  - Matrice : Velo en **Aux Source** de la ligne ENV 2 → CUTOFF.
- **ENV 1** : DEC **840 ms**, SUS **−9,5 dB**, REL **542 ms** [SOURCE PL-07].
- **FX** [SOURCE PL-07] :
  1. Filter **MG Low 18** : CUTOFF 35, une enveloppe à 35 [ASR ?], RES 4 [ASR ?], DRIVE 0, FAT 19 %.
  2. Reverb : SIZE **37 %**, DECAY **5,4 s**, LO CUT **35**, HI CUT **24**, SPIN et SPIN DEPTH 0, MIX **41 %**.
  3. Equalizer : bande basse en **High Pass** à **538 Hz**, Q 44 ; bande haute en **High Shelf** à **2055 Hz**, Q 44, **+4 dB**.
  4. Delay **1/8 – 1/8**, FREQ **816 Hz**, Q **0,8**, MIX **36 %**.
  - MAIN **76 %**.
- **Delay** [CALCUL] : à 122 BPM, 1/8 = 245,9 ms ; à 124 BPM, 241,9 ms.
- **Contrôle de la règle du filtre** [DÉDUCTION] : ici le filtre décroît plus lentement (1,05 s) que le volume (840 ms). Le pluck vient alors du SUS d'ENV 1 à −9,5 dB et de l'EQ qui coupe sous 538 Hz ; c'est un pluck long, presque un lead.
- **Macros de la vidéo** [SOURCE PL-07], toutes deux automatisées note à note :
  - MACRO 1 → LEVEL d'OSC A 40 [ASR ? « 240 »], DEC d'ENV 1 38, DEC d'ENV 2 17, CUTOFF 39 ;
  - MACRO 2 → ATK d'ENV 1 20, DEC d'ENV 1 20, ATK d'ENV 2 30, ATK d'ENV 3 30.

  Ici, MACRO 1 de la vidéo devient MACRO 5 `Length` et MACRO 2 devient MACRO 6 `Soft` [ORIGINAL], pour garder les quatre macros communes.
- **Macros communes** : `Tone` CUTOFF 0 → 25 % · `Motion` ENV 2 → CUTOFF 40 → 90 · `Dirt` DRIVE 0 → 50 · `Space` MIX de la Reverb 20 → 50 %.
- **Jeu** : MIDI 60 à 84, mélodie arpégée ; automatiser `Length` et `Soft` pour que deux notes voisines ne sonnent jamais pareil.
- **Test** : le timbre seul est repris du titre de la vidéo, pas sa mélodie.

### PK03 Pluck « marble » deep
- **Patch** [SOURCE PL-01] :
  - OSC A : Digital « Bottle Blow », OCT −1, UNISON 3, DETUNE 0, RAND 0 ; WARP 1 **Bend +** **50 %**.
  - OSC B : Digital « Harmonic Morph », une voix ; WARP 1 **Flip** **50**.
  - NOISE « Glass Glits 5 » [ASR ? « Glass Glitch »] (Attacks/Misc), suivi au clavier, LEVEL 0.
  - ENV 2 → LEVEL du NOISE, WT POS d'A (presque au maximum) et de B, CUTOFF, MIX de la distorsion. Forme : petite attaque, SUS 0, decay rapide, courbe creusée, un peu de release.
  - LFO 1 dessiné en triangle inversé, **4 mesures**, → WARP 1 (Bend +) d'OSC A, bipolaire, faible.
  - Velo → WT POS d'A (négatif) et de B (plus négatif).
  - ENV 3 : ATK 0, DEC très court, SUS 0, REL 0 → **Main Tuning** : petit clic de hauteur.
  - FILTER 1 **MG Low 24** sur A, B et NOISE, CUTOFF presque fermé ; ENV 2 et Velo → CUTOFF. Matrice : **NoteOn Rand 1** → RES ; RES baissée, un peu de DRIVE et de FAT.
- **Valeurs de départ** [ORIGINAL] : ENV 2 3 ms / 0 / 180 ms / 0 / 120 ms ; ENV 3 0 / 0 / 15 ms / 0 / 0, vers Main Tuning +12 ; NoteOn Rand 1 → RES ±10 %.
- **ENV 1** : ATK minime, DEC très court, SUS bas mais pas nul, un peu plus de REL [SOURCE PL-01] ; ici 1 ms / 0 / 260 ms / −18 dB / 200 ms [ORIGINAL]. Le filtre (180 ms) tombe à 69 % du volume [CALCUL].
- **FX** [SOURCE PL-01] : Hyper/Dimension (Hyper MIX 0, Dimension SIZE baissée, un peu de MIX) → Distortion **Diode 2**, MIX 0, ENV 2 → MIX un peu → Compressor (seuil bas, release court, gain monté) → Reverb (SIZE presque 0, DECAY bas, LO CUT monté, HI CUT haut, SPIN 0, MIX un peu monté).
- **Options** [SOURCE PL-01] : Filter **MG Low 18** en FX pour retirer le grain aigu ; la vidéo met aussi un SUB en saw dans le filtre : ici, il reste éteint (règle 1).
- **Macros** : `Tone` CUTOFF 5 → 35 % · `Motion` profondeur d'ENV 2 vers les WT POS 30 → 90 % · `Dirt` ENV 2 → MIX de la Diode 2 0 → 40 % · `Space` MIX de la Reverb 5 → 30 %.
- **Jeu** : MIDI 60 à 76, mélodie courte et sombre ; la vélocité fait bouger les tables, donc varier les vélocités.
- **Test** : la résonance aléatoire doit donner un léger relief, pas un sifflement ; plafonner à ±10 %.

### PK04 LFO pluck
- **Patch** [SOURCE PL-03, Serum 2] : il n'y a **pas d'enveloppe percussive**. Un LFO en rampe descendante hache les niveaux et le cutoff.
  - OSC A : Analog › Basic Shapes, WT POS **2** (scie). OSC B : Basic Shapes, WT POS **4** (carrée). LEVEL d'A et B ≈ **30 %**.
  - OSC B : UNISON **8**, DETUNE ≈ **27**.
  - FILTER 1 **MG Low 24** sur A et B ; NOISE « AC Hum 1 » à **60 %**, routé au filtre ; CUTOFF **≈ 280 Hz**.
  - LFO 1 en pente descendante → LEVEL d'A, LEVEL de B (≈ 30 %), CUTOFF (≈ 22-25 %).
  - LFO 1 en **HZ**, RATE ≈ 0,8 [ASR ?] ; **MACRO 5 `Rate`** → RATE du LFO 1, de 70 % à 25 %.
  - MAIN ≈ 50-59 %.
- **Le rate** [CALCUL] : à 122 BPM, une croche vaut 4,07 Hz et une noire 2,03 Hz. Le « 0,8 » dit se lit mal : 0,8 Hz donne une pulsation toutes les 1,25 s, soit environ deux temps et demi, ce qui n'est pas calé. Régler `Rate` à l'oreille jusqu'à tomber sur la croche ou la noire ; en BPM, le LFO serait calé mais la vidéo veut le glissement continu du Hz.
- **ENV 1** : 0 ms / 0 / 1 s / 0 dB / 300 ms [ORIGINAL] : c'est le LFO qui fait le pluck.
- **FX** [SOURCE PL-03] :
  1. Compressor **Multiband**, gains de bandes montés, « smile » (haut et bas ≈ 44-46), release ≈ 530 ms [unité supposée].
  2. Reverb **Hall**, MIX monté, DECAY **≈ 7 s**, SIZE **≈ 50 %**, LO CUT **≈ 80 Hz**, HI CUT haut [ASR ?].
  3. Equalizer : bande basse en Low Shelf **−7 dB** ; un second Equalizer en High Pass à 150 Hz [règle 2].
- **Macros** : `Tone` **MACRO 4 « Filter » de la vidéo** → CUTOFF, ramené à 35 % ; RES de 10 % à 0 [SOURCE PL-03] · `Motion` profondeur de LFO 1 vers les niveaux 0 → 60 % · `Dirt` DRIVE du filtre 0 → 40 · `Space` MIX de la Hall 15 → 45 % · MACRO 5 `Rate`.
- **Jeu** : accords ou notes tenus, MIDI 57 à 76. Automatisations de la vidéo : `Rate` qui descend puis remonte, `Tone` qui s'ouvre, se ferme puis s'ouvre en grand.
- **Test** : sept secondes de Hall sur un pluck haché remplissent tout ; vérifier avec le kick que le grave reste propre (LO CUT et Low Shelf).

### PK05 Pluck joué par le Clip
- **Patch** [SOURCE PL-02, Serum 2] :
  - Init (saw). ENV 1 « pluck » : SUS 0, un peu plus de REL.
  - ENV 2 → CUTOFF, quantité adoucie ; Velo → CUTOFF.
  - **Clip** de Serum 2 : TRIGGER MODE **MONO**, KB SPAN **Mono** (« KB span mono » [ASR ?], clip transposé relativement à C3) ; motif dessiné sur deux mesures, avec des notes fantômes à basse vélocité. Une note **tenue** lance le motif.
  - LFO 1 → **FIN**, RATE **1/128** ; **MACRO 2** en Aux Source de cette ligne : intensité du trémolo, gardée assez haute pour le grain.
  - Distortion (type non dit). NOISE (type non dit) : NoteOn Rand 1 → START, NoteOn Rand 2 → LEVEL, quantités réduites.
- **Le trémolo** [CALCUL] : à 122 BPM, 1/128 = 15,4 ms, soit 65 Hz. C'est une modulation presque audio : elle ajoute du grain plus qu'un vibrato.
- **Valeurs de départ** [ORIGINAL] : MG Low 12, CUTOFF 30 % ; ENV 2 0 / 0 / 200 ms / 0 / 100 ms vers CUTOFF 35 % ; ENV 1 0 / 0 / 300 ms / 0 / 150 ms ; LFO 1 → FIN ±6 cents ; Distortion Tube DRIVE 20.
- **FX** [SOURCE PL-02] : Distortion, Reverb et Delay à MIX 0, ouverts par **MACRO 1 « Wet »** (intensité maximale réduite), à automatiser.
- **Macros** [SOURCE PL-02, rangées ici] : `Space` = « Wet » de la vidéo, MIX de Reverb et Delay 0 → 35 % · `Motion` = MACRO 2 de la vidéo, trémolo 0 → 100 % de la ligne · `Tone` CUTOFF 15 → 50 %, automatisé toutes les deux mesures · `Dirt` DRIVE 0 → 40 · MACRO 5 `Decay` → DEC d'ENV 1, automatisé « up and down ».
- **Jeu** : une note tenue par accord, dans l'octave qui lance le Clip (MIDI Input Trigger Octave : la plus basse par défaut, `../serum2-fx-clip-arp.md`). Second motif de la vidéo en triolets sur une mesure.
- **Test** : le motif est dans le preset, pas dans le clip de Live ; noter le Clip retenu dans la mémoire du projet. Sidechain : la vidéo le copie depuis la basse.

### PK06 Saw afro et bruit
- **Patch** [SOURCE PL-08, pluck 1] :
  - OSC A : Basic Shapes, WT POS **2** (scie).
  - FILTER 1 et ENV 2 → CUTOFF.
  - NOISE « Bright White », LEVEL bas ; ENV 2 → LEVEL du NOISE, ou **MACRO 5** → LEVEL du NOISE, à monter pendant un build.
  - Largeur : UNISON (effet flanger) ou une seconde saw routée au filtre.
- **ENV 1** : « plucky », un peu de SUS et de REL [SOURCE PL-08] ; ici 0 ms / 0 / 260 ms / −20 dB / 180 ms [ORIGINAL]. « Sustain bas = la note disparaît même tenue » (PL-08).
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 25 %, RES 15 % ; ENV 2 0 / 0 / 170 ms / 0 / 120 ms vers CUTOFF 45 % (65 % du decay d'ampli [CALCUL], règle 1).
- **FX** [SOURCE PL-08] : Chorus, Delay, Reverb (« ce qui fait vivre le pluck ») ; Equalizer en High Pass ; un peu d'Hyper/Dimension. Le type de filtre change le caractère : essayer MG Low 24, Low 18 et Acid Ladder.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` ENV 2 → CUTOFF 20 → 70 % · `Dirt` DRIVE 0 → 40 · `Space` MIX du Delay 0 → 35 %, monté au fil du morceau (PL-08) · MACRO 5 `Air` niveau du NOISE.
- **Jeu** : doubles croches syncopées sur un groove kick, percussions et shaker, MIDI 64 à 81. Voir la grille afro de ce fichier.
- **Test** : `Air` monté pendant un build ne doit pas masquer les shakers.

### PK07 Afro à table mouvante
- **Patch** [SOURCE PL-08, pluck 2] :
  - OSC A : Analog « Basic MG » [ASR ?], WT POS ≈ **52**.
  - ENV 2 → CUTOFF en **unipolaire**, petite attaque ; NOISE Bright White.
  - LFO 1 dessiné, **BPM désactivé**, RATE **0,7 Hz**, → WT POS ; mode **RETRIG** (« Trig ON »). CUTOFF plus ouvert qu'en PK06.
  - OSC B : même table, LEVEL plus bas, UNISON plus haut, routé au filtre.
- **Valeurs de départ** [ORIGINAL] : OSC B UNISON 5, DETUNE 0,15, LEVEL 50 % ; LFO 1 → WT POS 25 % ; ENV 2 3 ms / 0 / 180 ms / 0 / 120 ms vers CUTOFF 35 %.
- **Le rate** [CALCUL] : 0,7 Hz = un cycle de 1,43 s. En RETRIG, chaque note repart du même point ; une note courte n'entend que le début du cycle, la table bouge donc surtout sur les notes longues.
- **ENV 1** : 0 ms / 0 / 300 ms / −18 dB / 200 ms [ORIGINAL].
- **FX** [SOURCE PL-08] : Chorus, Delay, Reverb ; Hyper/Dimension « un tout petit peu » ; Equalizer en High Pass à 160 Hz.
- **Macros** : `Tone` CUTOFF 25 → 60 % · `Motion` LFO 1 → WT POS 0 → 50 % · `Dirt` DRIVE 0 → 35 · `Space` MIX de la Reverb 10 → 35 %.
- **Jeu** : MIDI 60 à 79, mêmes motifs que PK06 avec des notes plus longues en fin de phrase.
- **Test** : la couche B large fait de ce pluck l'élément large ; voir la règle 6 de `leads.md`.

### PK08 Marimba sinus
- **Patch** [SOURCE PL-04] :
  - OSC A : Analog, sinus **propre** (préféré au sinus « analog » plus sale) ; enveloppe d'ampli courte.
  - ENV 3 : DEC **≈ 20 ms**, SUS 0, REL 0 → **Main Tuning** par la matrice : l'attaque synthétique, un « transient designer » interne.
- **Valeurs de départ** [ORIGINAL] : ENV 3 → Main Tuning +12 à +24 demi-tons (la quantité est « à vérifier à l'écran ») ; ENV 1 0 ms / 0 / 220 ms / 0 / 120 ms.
- **L'accord** [SOURCE PL-04] : la vidéo transforme une note en accord avec les effets MIDI Chord (+15 demi-tons) et Scale (ré mineur) de Live. Ici [DÉDUCTION] : écrire les deux notes dans le clip, la note et sa dixième (+15 ou +16 selon le degré), pour éviter deux effets MIDI natifs dont le statut reste à confirmer (`../synths-serum-synthese.md`, Limites).
- **Pas de filtre** [DÉDUCTION] : un sinus n'a pas d'harmoniques à fermer. Le « pluck » vient de l'attaque de hauteur et du decay d'ampli ; la règle 1 du fichier ne s'applique pas ici.
- **FX** : Equalizer en High Pass à 150 Hz → Reverb Plate, SIZE 20, MIX 15 % [ORIGINAL ; la vidéo met une petite room hors de Serum].
- **Hors de Serum** : un transient designer tiers dans la vidéo (Schaack [ASR ?]) ; ici ShaperBox 3 si l'attaque manque, sinon rien.
- **Macros** : `Tone` Equalizer, bande haute en High Shelf 0 → +6 dB à 3 kHz · `Motion` ENV 3 → Main Tuning +6 → +24 · `Dirt` Distortion Sine Shaper 0 → 30 · `Space` MIX de la Plate 0 → 30 %.
- **Jeu** : MIDI 62 à 86, accords à la dixième en doubles croches.
- **Test** : un coup de hauteur de 20 ms se perçoit comme un clic, pas comme une note ; s'il devient audible comme glissade, raccourcir à 10 ms.

### PK09 Accords rythmés par LFO
- **Patch** [SOURCE PL-06, en français] :
  - Le MIDI est une suite d'**accords tenus** ; le rythme vient d'un LFO qui boucle.
  - FILTER 1 activé (MG Low 12 par défaut dans Serum 1 ; ici MG Low 12 aussi [DÉDUCTION]), CUTOFF un peu baissé ; LFO 1 → CUTOFF « un peu mais pas trop ».
  - LFO 1 redessiné en pente percussive, mode **RETRIG** (« déclencher à chaque nouvelle note ») pour rester calé.
  - UNISON **4** voix, léger DETUNE.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1/8, forme montée instantanée puis descente en 70 % du pas ; CUTOFF 30 %, LFO 1 → CUTOFF 35 % ; DETUNE 0,1 ; POLY 8.
- **ENV 1** : 0 ms / 0 / 2 s / 0 dB / 300 ms [ORIGINAL] : le volume tient, le filtre fait le rythme.
- **FX** [SOURCE PL-06] : un peu de Reverb et de Delay ; réglages finaux sur CUTOFF, quantité du LFO et DRIVE du filtre.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` LFO 1 → CUTOFF 10 → 60 % · `Dirt` DRIVE 0 → 40 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : accords de trois ou quatre notes, une mesure chacun, MIDI 57 à 76.
- **Test** : en RETRIG, un accord qui change en cours de mesure relance le motif ; c'est le comportement attendu, à vérifier sur les changements d'accords décalés.

### PK10 Deep soustractif chiffré
- **Patch** [FICHE, valeurs de la table « Points de départ »] :
  - OSC A : Basic Shapes, scie, RAND 100.
  - FILTER 1 **MG Low 24**, CUTOFF de repos **600-800 Hz**.
  - ENV 2 → CUTOFF, pic vers **3-4 kHz** : ATK 0, DEC **120-160 ms**, SUS 0.
  - VOICING POLY 6.
- **ENV 1** : ATK 0, DEC **180-250 ms**, SUS 0 [FICHE] ; REL 100 ms [ORIGINAL].
- **Contrôle de la règle 1** [CALCUL] : DEC d'ENV 2 140 ms pour 210 ms d'ENV 1 = 67 %.
- **Quantité d'ENV 2** [DÉDUCTION] : la course de CUTOFF n'est pas linéaire en Hz ; régler la profondeur en lisant la fréquence affichée au sommet (3-4 kHz).
- **FX** : Distortion Tape Sat. DRIVE 15, MIX 30 % → Equalizer en High Pass à **139 Hz** [FICHE : passe-haut du patch Attack Magazine] → Reverb Plate, MIX 12 % [ORIGINAL].
- **Macros** : `Tone` CUTOFF de repos 400 → 1200 Hz · `Motion` DEC d'ENV 2 80 → 200 ms · `Dirt` DRIVE de la Tape Sat. 0 → 40 · `Space` MIX de la Plate 0 → 30 %.
- **Jeu** : accords de septième en croches décalées, MIDI 57 à 74.
- **Test** : baisser la piste de 10 dB ; un pluck soustractif perd sa brillance avec le volume [FICHE]. S'il disparaît dans un mix minimal, passer à PK11.

### PK11 Pluck FM bois ou verre
- **Patch** [FICHE pour les rapports et les durées ; ORIGINAL pour la traduction dans Serum] :
  - OSC A : sinus (Basic Shapes, frame 1), porteuse.
  - OSC B : sinus, **LEVEL 0**, modulateur. Rapport **2:1** (bois) : OCT +1. Rapport **3,51:1** (verre) : OCT +1, SEM +9, FIN +74 [CALCUL : 12 × log2(3,51) = 21,74 demi-tons]. Le mode **Ratio** de Serum 2 (clic droit sur OCT ou SEM) peut donner ces rapports directement, à vérifier.
  - OSC A, WARP 1 **FM (B)** à 0 ; ENV 2 → FM (B) : ATK 0, DEC **80-150 ms**, SUS 0. C'est l'enveloppe du modulateur de la fiche.
- **ENV 1** : ATK 0, DEC **300-500 ms**, SUS 0 [FICHE] ; REL 150 ms [ORIGINAL].
- **Pourquoi la FM** [FICHE] : la brillance vient de l'indice de modulation, pas du filtre ; elle ne baisse pas quand on baisse la piste, et le pluck reste lisible à −20 dB dans un mix minimal.
- **Quantité** [ORIGINAL] : ENV 2 → FM (B) 25 % pour un pluck doux, 60 % pour un pluck dur ; l'indice exact de la fiche (≈ 1 doux, ≈ 10 inharmonique) ne se lit pas sur le bouton de Serum.
- **FX** : Equalizer en High Pass à 140 Hz → Compressor Single 3:1 → Reverb Plate, MIX 15 % [ORIGINAL].
- **Macros** : `Tone` rapport de B entre bois et verre (SEM de B, 0 → +9) · `Motion` ENV 2 → FM (B) 10 → 70 % · `Dirt` Distortion Soft Clip 0 → 30 · `Space` MIX de la Plate 0 → 30 %.
- **Jeu** : MIDI 60 à 84, notes isolées ou intervalles de quinte.
- **Test** : à 3,51:1 les partiels ne sont plus harmoniques ; garder ce pluck pour des notes longues espacées, où la couleur de cloche ne fausse pas l'harmonie.

### PK12 Pluck tech house sec
- **Le corpus n'a aucun pluck tech house fait dans Serum** (section « Manque » de l'étude). Recette **[ORIGINAL]** construite sur la fiche (couche transitoire séparée) et sur les filtres de Serum 2.
- **Patch** :
  - OSC A : Basic Shapes, scie, OCT 0, RAND 0, PHASE 0 (même attaque à chaque note).
  - FILTER 1 **Acid Ladder**, CUTOFF 20 %, RES 35 %, DRIVE 30 ; ENV 2 0 / 0 / 90 ms / 0 / 40 ms → CUTOFF 50 %.
  - NOISE « Kick Attack » (n'importe quel numéro, à choisir), **one-shot**, LEVEL 40 %, hors du filtre.
  - VOICING MONO.
- **Couche transitoire** [FICHE] : le NOISE en one-shot joue ce rôle ; le garder sous la scie d'environ 6 dB et le couper sous 140 Hz par le High Pass final.
- **ENV 1** : 0 ms / 0 / 140 ms / 0 / 30 ms. Contrôle de la règle 1 [CALCUL] : 90 / 140 = 64 %.
- **FX** : Distortion **Diode 1**, DRIVE 25, MIX 50 % → Equalizer en High Pass à 180 Hz → Delay 1/16, FEEDBACK 15 %, MIX 10 %.
- **Delay** [CALCUL] : à 126 BPM, 1/16 = 119,0 ms.
- **Macros** : `Tone` CUTOFF 10 → 45 % · `Motion` ENV 2 → CUTOFF 20 → 80 % · `Dirt` DRIVE de la Diode 1 0 → 60 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : notes répétées sur les contretemps de doubles croches, une ou deux hauteurs, MIDI 60 à 72.
- **Test** : ce pluck n'a aucune source vidéo ; le comparer à PK01 à niveau égal avant de le garder.

### PK13 Pluck à table dessinée
- **Patch** [SOURCE PL-09] :
  - OSC A : sinus. Dans l'éditeur de tables, une **seconde frame** : un sinus « équarri » à la main en équilibrant les harmoniques (onde presque carrée).
  - Interpolation **Spectral** (morph) entre les deux frames (choisie dans l'éditeur, cartographie § 3.2).
  - Un LFO à forme de pluck → WT POS : c'est le transitoire du pluck.
  - UNISON ajoutée, DETUNE baissé puis modulé par le même LFO ; RAND à 0, modulé aussi [ASR ? « round face »].
- **Valeurs de départ** [ORIGINAL] : LFO 1 en mode ENVELOPE, montée instantanée puis descente en 120 ms, vers WT POS 100 % depuis la frame 1 ; UNISON 3, DETUNE 0,05, LFO 1 → DETUNE 0,05 ; LFO 1 → RAND 20 %.
- **Harmoniques de la frame 2** [DÉDUCTION] : un carré n'a que des harmoniques impaires, d'amplitude 1/n (3e à 1/3, 5e à 1/5…). Les régler ainsi donne le « sinus équarri » ; en garder quatre ou cinq le laisse rond.
- **ENV 1** : 0 ms / 0 / 600 ms / −12 dB / 300 ms [ORIGINAL].
- **FX** [SOURCE PL-09] : Compressor, avec un LFO de même forme → GAIN du compresseur : un gros pic à l'attaque puis un niveau moyen bas, qui nourrit la distorsion.
- **Hors de Serum** : la vidéo met une distorsion Kilohearts « sine shaper » ; dans Serum, Distortion **Sine Shaper**, puis baisser le niveau [SOURCE PL-09]. La vidéo sépare ensuite le son sec (petit passe-haut) et une reverb 100 % humide, longue, filtrée, dans un Audio Effect Rack de Live. Ici [DÉDUCTION] : envoyer FILTER ou OSC A vers **BUS 1** à 100 %, Reverb Hall à MIX 100 % puis Equalizer sur BUS 1 ; ou ValhallaVintageVerb sur un retour.
- **Macros** : `Tone` WT POS de repos 0 → 40 % · `Motion` LFO 1 → WT POS 30 → 100 % · `Dirt` DRIVE du Sine Shaper 0 → 50 · `Space` niveau de BUS 1 0 → 100 %.
- **Jeu** : intro DnB, MIDI 64 à 84, notes espacées, souvent sans batterie.
- **Test** : le transitoire doit venir de la table ; si on l'entend comme un balayage de filtre, raccourcir la descente du LFO.

### PK14 Pluck liquide qui suit la note
- **Patch** [SOURCE PL-10] :
  - Init, scie ; **UNISON 9** (nombre impair : une voix centrale juste).
  - FILTER 1 **Low 24** ; une enveloppe (ENV 2) → CUTOFF, forme pluck dessinée, courbe modulée [ASR ?].
  - CUTOFF **≈ 142 Hz**, quantité de modulation **46** : « sinon trop fou ».
- **Valeurs de départ** [ORIGINAL] : DETUNE 0,12 ; ENV 2 0 / 0 / 200 ms / 0 / 150 ms ; ENV 1 0 / 0 / 320 ms / −24 dB / 250 ms. Contrôle de la règle 1 [CALCUL] : 200 / 320 = 63 %.
- **FX** [SOURCE PL-10] : Hyper/Dimension → Reverb → **Equalizer avant le Compressor** : une bande en Peak dont la FREQ est modulée par **Note#** (une résonance qui suit la mélodie) → Compressor **Multiband** → Delay.
- **Valeurs de l'EQ** [ORIGINAL] : Peak à 1,2 kHz, GAIN +6 dB, Q 40 ; Note# → FREQ, quantité réglée pour qu'une octave jouée déplace la bosse d'environ une octave (à mesurer en jouant deux do).
- **Macros** : `Tone` CUTOFF 100 → 300 Hz · `Motion` quantité ENV 2 → CUTOFF 30 → 60 · `Dirt` GAIN du Peak 0 → +9 dB · `Space` MIX de la Reverb 10 → 35 %.
- **Jeu** : MIDI 60 à 84, mélodies liquides en croches ; voir la grille DnB de ce fichier.
- **Test** : les trois réglages qui comptent (PL-10) : la tension du filtre, l'expression de l'EQ, la plage de modulation.

### PK15 Pluck-basse dancefloor
- **À la limite de la catégorie** : PL-11 joue un riff bas-médium. Ici, couche médium seulement ; le grave vient d'un sub de `dnb-f01-sub.md` (règle 2).
- **Patch** [SOURCE PL-11] :
  - OSC A : carrée, OCT −1. OSC B : carrée, OCT −1, SEM **+7** (ou −5).
  - SUB en Direct Out dans la vidéo : ici **éteint**.
  - UNISON ajoutée, DETUNE baissé ; couche grave moins forte, quinte remontée.
  - FILTER 1 (type non dit) sur A et B. LFO 1 → CUTOFF, mode **ENVELOPE** (un seul passage), forme de pluck dessinée ; RATE vers **1/2 mesure** [ASR ?] pour garder une queue. Modulation en **unipolaire**, courbe abaissée ; RES au goût.
  - LFO 2 en mode ENVELOPE, forme descendante, unipolaire → **Main Tuning**, quantité forte puis baissée : le clic d'attaque.
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 15 % ; LFO 1 → CUTOFF 50 % ; LFO 2 en HZ à 25 Hz (un passage de 40 ms [CALCUL]), vers Main Tuning +12 ; UNISON 3, DETUNE 0,08.
- **ENV 1** : 0 ms / 0 / 700 ms / −10 dB / 120 ms [ORIGINAL].
- **FX** [SOURCE PL-11] : Distortion en mode **PRE**, filtre passe-haut **≈ 400 Hz** (seul le haut sature), MIX baissé → Compressor **Multiband**, release au maximum → Reverb légère → Equalizer (bas-médium remonté) ; High Pass à 120 Hz en fin de chaîne [règle 2].
- **Macros** : `Tone` CUTOFF 5 → 40 % · `Motion` LFO 1 → CUTOFF 20 → 70 % · `Dirt` DRIVE de la Distortion 20 → 70 · `Space` MIX de la Reverb 0 → 15 %.
- **Jeu** : riff de croches et doubles croches, joué entre MIDI 60 et 72. Les oscillateurs étant à OCT −1, une note jouée à 60 sonne à 48 (130,8 Hz) et reste au-dessus du High Pass ; jouée plus bas, sa fondamentale est coupée [CALCUL].
- **Test** : avec le sub, la quinte de B ne doit pas brouiller le grave ; si oui, passer B à −5 (quarte en dessous) ou baisser son niveau.

### PK16 Pluck répété par LFO
- **Registre** : PL-14 joue « C0-C1 », soit MIDI 24 à 36 si la vidéo suit la convention de Live (interp. de la synthèse) : c'est une basse. La recette garde le geste et le remonte dans le médium (MIDI 48 à 64) ; le grave vient d'un sub (règle 2).
- **Patch** [SOURCE PL-14] :
  - OSC A : « Saw Rounded », WT POS montée. OSC B : « Square Saw » [ASR ?], OCT **+2**, SEM **+7** (quinte).
  - LFO 1 dessiné « en aile » (attaque dure, chute rapide, un peu de maintien au début) → LEVEL d'A et B (niveaux bas, quantité haute : pluck plus marqué).
  - LFO 1 en **RETRIG**, **BPM désactivé** (rate libre, transitions douces).
  - FILTER 1 **MG Low 12** sur A et B, CUTOFF baissé, LFO 1 → CUTOFF.
- **Les rates** [SOURCE PL-14 ; CALCUL] : la vidéo dit 5,6-5,7 Hz pour la croche, 3,8 pour la croche pointée, 2,8 pour la noire. En Hz, croche = BPM ÷ 30 : ces valeurs correspondent à environ 170 BPM. À **174 BPM** : croche **5,80 Hz**, croche pointée **3,87 Hz**, noire **2,90 Hz**.
- **ENV 1** : ATK ≈ **5 ms** si clic [SOURCE PL-14] ; ici 5 ms / 0 / 2 s / 0 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE PL-14] : Distortion, DRIVE ≈ 80 % puis réduit, LFO 1 → DRIVE (attaque plus dure) ; Reverb avec un LO CUT fort et un MIX bas. La vidéo dit qu'un partage haut/bas vaudrait mieux : Splitter L/H vers 300 Hz, Reverb sur la bande haute seulement [DÉDUCTION].
- **Automation** [SOURCE PL-14] : dans Live, le RATE du LFO 1 part rapide (≈ 5,8) puis ralentit ; il accélère sur la seconde moitié d'une note longue. Ici : **MACRO 5 `Rate`** → RATE du LFO 1, automatisée sur la piste.
- **Pitch bend** [SOURCE PL-14] : +2 demi-tons en fin de note (plage ±2 ; 12 essayé, trop fort).
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` LFO 1 → LEVEL 40 → 100 % · `Dirt` DRIVE 30 → 80 · `Space` MIX de la Reverb 0 → 15 % · MACRO 5 `Rate`.
- **Test** : un LFO non synchronisé dérive par rapport à la grille sur les notes longues ; c'est voulu ici, mais vérifier que la première répétition tombe juste.

### PK17 Progressif à deux couches
- **Patch** [SOURCE PL-12] :
  - OSC A : scie (par défaut), octave d'origine, **une voix** : le centre mono, solide.
  - OSC B : **+1 octave**, **UNISON 7**, DETUNE un peu baissé : la couche large.
  - FILTER 1 **MG Low 24**, CUTOFF au minimum, A, B et NOISE routés ; NOISE « JP106 High Pass » [ASR ?] (sans bas mou).
  - ENV 1 → CUTOFF, quantité un peu réduite. DRIVE du filtre poussé : saturation « analogique » ; baisser le MAIN ensuite.
- **ENV 1** : SUS un peu baissé, DEC plus court, ATK légèrement montée, REL **≈ 150 ms** [SOURCE PL-12] ; ici 4 ms / 0 / 350 ms / −14 dB / 150 ms [ORIGINAL pour le reste].
- **Filtre et volume** [DÉDUCTION] : la même ENV 1 pilote les deux ; la règle 1 n'est donc pas tenue. Pour la tenir, mettre ENV 2 sur le CUTOFF à 230 ms de DEC (66 %) [CALCUL] et comparer.
- **FX** [SOURCE PL-12] : Hyper/Dimension, MIX baissé ; Reverb SIZE montée, MIX réduit, HI CUT et LO CUT un peu remontés ; Equalizer en High Pass à 180 Hz.
- **Macros** : `Tone` CUTOFF 0 → 35 % · `Motion` ENV → CUTOFF 30 → 70 % · `Dirt` DRIVE 30 → 80 · `Space` MIX de la Reverb 10 → 35 %.
- **Jeu** : MIDI 60 à 84, arpèges d'intro et de break.
- **Test** : en mono, la couche B en unison 7 s'effondre ; le centre A doit suffire à porter la mélodie.

### PK18 Arp future bass
- **Patch** [SOURCE PL-13] :
  - OSC A : scie, peu touchée. OSC B : scie, **UNISON ≈ 7**, DETUNE ajusté, **+1 octave** (interp. de l'étude).
  - FILTER 1 sur B et NOISE, **MG Low 24** (le 12 dB sonne moins bien selon la vidéo) ; ENV 1 → CUTOFF, CUTOFF assez bas.
  - MACRO → CUTOFF, pour l'automation.
- **ENV 1** : ATK **≈ 3,8 ms** [ASR ?], un peu de SUS, DEC et REL ajustés [SOURCE PL-13] ; ici 3,8 ms / 0 / 300 ms / −16 dB / 200 ms [ORIGINAL pour le reste].
- **FX** [SOURCE PL-13] : Hyper/Dimension, Reverb en option ; après Serum, OTT en option, Equalizer (coupe-bas vers les centaines de Hz, léger retrait des aigus), compresseur **4:1**, attaque et release rapides, seuil **≈ −12,7 dB**, puis un Utility automatisé pour tenir le volume quand le filtre s'ouvre.
- **Dans l'installation** : le Compressor Single interne à 4:1 remplace le compresseur de la vidéo ; l'Utility natif est toléré pour le volume.
- **Automation** [SOURCE PL-13] : `Tone` en **cloche** (monte puis redescend), courbe adoucie avec Alt/Option dans Live.
- **Macros** : `Tone` CUTOFF 10 → 70 % · `Motion` ENV 1 → CUTOFF 20 → 60 % · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Reverb 0 → 30 %.
- **Jeu** : arpèges de doubles croches, MIDI 60 à 88 ; ARP de Serum possible (1/16, Up) sur des accords tenus.
- **Test** : le niveau monte quand le filtre s'ouvre ; c'est la raison du compresseur et de l'Utility de la vidéo.

### PK19 Pluck Au5
- **Patch** [SOURCE PL-15] :
  - OSC A : « Basic CGV » [ASR ?] (≈ sinus) ; LFO 1 → WARP 1 en **Bend +**, plage **≈ 20** : mouvement discret.
  - NOISE : Attacks › Misc › **« Guitar Mute 2 »**, **one-shot**, suivi de hauteur actif : le transitoire, à la place d'une enveloppe de hauteur.
  - OSC B : scie, **UNISON 7**, DETUNE **≈ 0,04** ; FILTER 1 sur B seulement, CUTOFF ≈ moitié.
  - Enveloppe de volume en décroissance douce.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1 bar, FREE, sinus ; ENV 1 2 ms / 0 / 900 ms / −20 dB / 400 ms ; FILTER 1 MG Low 18 ; LEVEL du NOISE 50 %.
- **FX** [SOURCE PL-15] : Distortion **Downsample**, DRIVE **exactement 22**, MIX **≈ 30** (« 1 % de différence change beaucoup ») → Equalizer en **High Pass** → Delay **Ping-Pong** ; EQ retouché pour coller à la cible.
- **Valeurs du delay** [ORIGINAL] : 1/8 pointée, FEEDBACK 30 %, MIX 20 % ; à 150 BPM, 1/8 pointée = 300 ms [CALCUL].
- **Macros** : `Tone` CUTOFF de B 30 → 70 % · `Motion` LFO 1 → Bend + 0 → 40 · `Dirt` DRIVE du Downsample 18 → 26 (plage étroite, d'après la vidéo) · `Space` MIX du Delay 0 → 35 %.
- **Jeu** : MIDI 64 à 88, phrase d'avant-break.
- **Test** : la macro `Dirt` a volontairement une course courte ; vérifier qu'à 26 le Downsample ne crache pas.

### PK20 Accords pulsés en triolets
- **Recette [DÉDUCTION]** : le geste de PK09 (accords tenus, LFO RETRIG sur le cutoff) avec les couches de PK17 et PK18, calé sur le tempo melodic dubstep. Aucune vidéo du corpus ne la fait telle quelle.
- **Patch** :
  - OSC A : scie, une voix. OSC B : scie, +1 octave, UNISON 7, DETUNE 0,15.
  - FILTER 1 **MG Low 24** sur A et B, CUTOFF 20 %, DRIVE 30.
  - LFO 1 en **1/8 triolet** (TRIP actif), RETRIG, montée instantanée puis descente en 70 % du pas → CUTOFF 45 % et → LEVEL de B −50 %.
  - VOICING POLY 8.
- **Le pas** [CALCUL] : à 150 BPM, une croche de triolet dure 133,3 ms ; à 140 BPM, 142,9 ms.
- **ENV 1** : 2 ms / 0 / 3 s / −2 dB / 400 ms [ORIGINAL].
- **FX** : Hyper/Dimension (Dimension MIX 30 %) → Compressor Multiband, MIX 40 % → Equalizer en High Pass à 180 Hz → Reverb Hall, MIX 20 % [ORIGINAL].
- **Macros** : `Tone` CUTOFF 10 → 50 % · `Motion` LFO 1 → CUTOFF 15 → 70 % · `Dirt` DRIVE 10 → 60 · `Space` MIX de la Hall 10 → 35 %.
- **Jeu** : accords de quatre notes, deux temps ou une mesure chacun, MIDI 55 à 79, sur un break en demi-temps.
- **Test** : les triolets contre une caisse claire au troisième temps doivent se sentir ; si le pluck brouille le groove, passer en 1/16.

## Motifs de départ (grilles vérifiées)

Numérotation de Live (C3 = 60). Mélodies écrites ici. Vérification, depuis le dossier du skill : `python3 ../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/synths/plucks.md`. Notation Producer Pal : `--fichier references/synths/plucks.md --titre <titre> --format ppal`.

```grille
titre: Deep house 122 — bambou (PK01, PK10)
tempo: 122
accords: Dm7 | Bbmaj7
pluck: D4[1&:1] A3[1a:1] C4[2e:1] F4[2&:2] E4[3e:1] D4[3&:1] A3[4:1] C4[4&:1] | D4[1&:1] A3[1a:1] Bb3[2e:1] F4[2&:2] D4[3&:1] Bb3[3a:1] A3[4&:2]
```

```grille
titre: Afro house 122 — saw et bruit (PK06, PK07)
tempo: 122
accords: Am7 | Em7
pluck: E4[1e:1] G4[1a:1] A4[2&:1] G4[3e:1] E4[3&:1] C4[3a:1] D4[4&:1] E4[4a:1] | E4[1e:1] G4[1a:1] B4[2&:1] A4[3e:1] G4[3&:1] E4[3a:1] D4[4&:1] B3[4a:1]
```

```grille
titre: DnB liquide 174 — pluck qui suit la note (PK14)
tempo: 174
accords: Fmaj7 | Em7
pluck: C5[1:2] A4[1&:2] E4[2:2] F4[2&:2] G4[3:2] A4[3&:2] C5[4:2] E5[4&:2] | B4[1:2] G4[1&:2] D4[2:2] E4[2&:2] F#4[3:2] G4[3&:2] B4[4:2] D5[4&:2]
```

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : « BD Sine », « Kick Attack » (numéro), « Bottle Blow », « Harmonic Morph », « Glass Glits 5 » [ASR], « AC Hum 1 », « Basic MG » et « Basic CGV » [ASR], « Saw Rounded », « Square Saw » [ASR], « JP106 High Pass » [ASR], « Guitar Mute 2 ». Vérifier le mode Ratio de l'oscillateur pour PK11.
- Lire à l'écran la forme du LFO « knock » de PK01 et la valeur du rate de PK04.
- Écouter chaque recette (règle 10 de `leads.md`), garder deux ou trois plucks par morceau et consigner le preset retenu dans la mémoire du projet (`../../../producteur-live/modules/memoire-projet/GUIDE.md`).
- Fichiers suivants du lot : hooks, accords, pads, drones.
