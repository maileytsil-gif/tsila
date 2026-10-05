# Vingt recettes de leads dans Serum 2

Premier fichier du lot de synthés (leads, plucks, hooks, accords, pads, drones). Ses règles communes valent pour tout le lot. Rédigé le 05/10/2026. Sources :
- l'étude des quinze tutoriels de leads, LE-01 à LE-15, de `../tutoriels-synths-serum.md`, et sa synthèse `../synths-serum-synthese.md` (section Lead) ;
- la fiche supersaw et lead mono de `../leads-nappes-textures.md` ;
- la cartographie de Serum 2 (`../serum2-cartographie.md`) et le détail des effets (`../serum2-fx-clip-arp.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Les tutoriels ont été lus sur transcription, son coupé, et sans capture d'écran. Étiquettes, comme dans les recettes de basses :
- **[SOURCE LE-nn]** : valeur ou geste dit dans le tutoriel ; [ASR ?] signale une transcription douteuse ;
- **[FICHE]** : valeur de `../leads-nappes-textures.md` ;
- **[CALCUL]** : valeur obtenue par une formule ;
- **[DÉDUCTION]** : conséquence tirée de la documentation, non essayée ;
- **[ORIGINAL]** : réglage proposé ici, à confirmer à l'oreille.

## Règles communes au lot de synthés

1. **Aucun sub dans un patch de synthé.** Le grave appartient au sub et à la basse médium, chacun dans son instrument (règle « Grave » d'`AGENTS.md`). Sur la page FX, Equalizer en dernier, bande basse en **High Pass** :
   - 150-250 Hz pour un lead ou un hook ;
   - 120-200 Hz pour un pluck ou des accords ;
   - 100-150 Hz pour un pad ou un drone.

   Plusieurs tutoriels gardent un SUB ou un oscillateur à −3 octaves dans le patch (LE-03, LE-12, LE-13). Les recettes l'éteignent ou le changent en simple modulateur à LEVEL 0. Si la partie a besoin d'un grave, il vient d'une recette de `../../../serum-2-basses-house-future-house/references/recettes/house-f01-sub.md`, `dnb-f01-sub.md` ou `dubstep-f01-sub.md`, sur une piste à part.
2. **Départ** : menu principal › Init Preset. Dans l'Init, seul OSC A est actif ; il va dans FILTER 1, qui est éteint et en MG Low 6 (cartographie, § 5 et § 6). Enveloppes notées ATK / HOLD / DEC / SUS / REL.
3. **Noms de Serum 2** pour les tutoriels faits en Serum 1 (cartographie, § 13) :
   - Master Tune devient **Main Tuning** (destination Global) ;
   - FM from B devient **FM (B)** ;
   - les modes de LFO Trig, Env et Off deviennent **RETRIG**, **ENVELOPE** et **FREE** ;
   - 4 macros deviennent 8, un filtre de voix en devient deux.
4. **Quatre macros communes au lot**, sur MACRO 1 à 4. Chaque fiche donne leurs bornes :
   - `Tone` : coupure du filtre principal ;
   - `Motion` : profondeur de la modulation qui fait le caractère (LFO, enveloppe de hauteur, warp) ;
   - `Dirt` : drive de la saturation principale, avec son MIX ou LEVEL en sens inverse si le niveau monte ;
   - `Space` : MIX de la reverb et du delay internes.

   MACRO 5 à 8 restent libres pour un geste propre à la recette (glide, saut d'octave). Vérifier le « + » sur chaque destination avant d'assigner (cartographie, § 7.3). Une macro automatisée peut porter la variation exigée avant chaque frontière de huit mesures (règle « Drops » d'`AGENTS.md`).
5. **Effets.** Les modules internes de Serum restent permis. Après Serum, seulement des plug-ins tiers (règle 6 de `../../../ableton-live-session/SKILL.md`). Dans l'installation, d'après `../../../effets-plugins/references/fiches.md` :
   - ValhallaVintageVerb pour une reverb externe, de préférence sur un retour ;
   - J37 Tape ou RazorClip pour une saturation ou un écrêtage ;
   - Pro-Q 4 pour l'égalisation ;
   - ShaperBox 3 pour une découpe de volume.

   Les effets natifs filmés (Saturator, EQ Eight, Auto Filter…) sont remplacés. Kickstart 2, Neutron, OTT, K-Clip et Sausage Fattener sont des plug-ins tiers dont la présence sur le Mac n'est pas vérifiée ; l'OTT se refait avec le Compressor interne en Multiband.
6. **Un seul élément large à la fois** [FICHE] : un lead en unison 7 et large demande un pad étroit, et inversement. Les recettes larges le disent.
7. **Notes** : C3 = 60, le numéro MIDI fait foi. Chaque fiche donne un registre de jeu en numéros MIDI. Les leads de ce fichier vivent surtout entre MIDI 60 et 84 (261,6 à 1046,5 Hz).
8. **Droits** : plusieurs tutoriels recréent un titre publié (LE-03, LE-08, LE-11, LE-14). On n'en reprend que le timbre ; les mélodies des grilles sont écrites ici.
9. **Sortie** : crêtes vers −6 dBFS par le bouton MAIN, la piste au fader.
10. **Contrôle par l'utilisateur** :
    - le patch seul, puis dans le mix avec la batterie, la basse et les pads ;
    - mono ;
    - les deux bornes de `Motion` et de `Dirt` ;
    - la note la plus grave et la plus aiguë de la partie ;
    - faible volume ;
    - A/B à niveau égal contre la recette de référence du fichier (ici LD01).

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| LD01 | Saw future house en FM | Future house 126, référence A/B | saw unison 7, FM (B) d'un sinus muet, ENV 2 longue sur Low 18, Tube PRE HP |
| LD02 | Whoop afro | Afro house 120-123 | ENV 2 unipolaire vers SEM et Main Tuning |
| LD03 | Lead afro en doubles croches | Afro house, deep | sustain 0, decay 150 ms vers le filtre, vélocité |
| LD04 | Carré afro à vibrato | Afro house, melodic | unison 5, vibrato rapide, Band 12, portamento |
| LD05 | Sync et Diode 2 | Bass house 126-128 | warp Sync sur B, Diode 2, Samp Hold en FX |
| LD06 | Saut d'octave par macro | Bass house | LFO ENVELOPE vers Main Tuning +1 et +24, dosé par macro |
| LD07 | FM et attaque de bruit | Bass house, G-house | FM (B) 53 %, NOISE Kick Attack en one-shot |
| LD08 | Lead qui se transforme | Tech house, bass house | LFO FREE d'une mesure sur detune, decay et Flanger négatif |
| LD09 | Lead riche melodic | Melodic house 120-124 | trois oscillateurs, PD (Noise), Hard Clip, Bend +/−, BUS 1 |
| LD10 | Lead cinématique | Melodic, organic house | dérive de hauteur, couche +1 octave à deux voix, reverb qui monte |
| LD11 | Saw percussive future rave | Future rave 126-128 | unison 16 sans detune, ENV 2 de 50 ms sur le drive, multibande |
| LD12 | Lead mono expressif | Signature sous 124, électro chill | PWM étroit, glide, vibrato retardé de 200 ms |
| LD13 | Supersaw dancefloor | DnB 174 | saw unison 7, REL 200-400 ms, NOISE en passe-haut |
| LD14 | Stab carré rave | DnB 174 | triangle −7 st + carrée +2 oct, Low 24 à 1 kHz, distorsion PRE HP |
| LD15 | Carré émotionnel « 8-bit » | DnB 174 liquide, dancefloor | Basic MG, PD (B), Hard Clip, volume qui respire à la noire |
| LD16 | Lead neuro désaccordé | DnB neuro 172-176 | deux saws en FM 30, DX Brass par FILTER 2, Splitter L/H et Convolve |
| LD17 | Pad sync devenu lead arpégé | DnB liquide | Sync lent sur 2 mesures, LFO « pluck » sur le niveau, ARP |
| LD18 | Melodic dubstep à un LFO | Melodic dubstep 140-150 | un LFO d'une mesure pilote tout, Flanges négatif, vibrato 1/16 |
| LD19 | Brostep à double warp | Dubstep 140-150 | Acid + Sync, Bend −, PD (C) muet, Diode 2 |
| LD20 | Robot lead | Dubstep 140-150 | FM (B) d'une saw muette, filtre Reverb suivi au clavier, delay de 20 ms |

## Les vingt recettes

### LD01 Saw future house en FM — référence du fichier
- **Patch** [SOURCE LE-07] :
  - OSC A : Basic Shapes, frame de la scie, OCT −1, UNISON 7, BLEND baissé (≈ 50 % [ORIGINAL]), RAND 0, PHASE 0.
  - OSC B : sinus (Basic Shapes, frame 1 ; « BD Sine » dit dans la vidéo [ASR ?]), **deux octaves au-dessus de A**, donc OCT +1, LEVEL 0 : il ne sert que de source FM. RAND 0.
  - OSC A, WARP 1 **FM (B)**, quantité ≈ 25 % au départ [ORIGINAL] ; la vidéo dit « au goût ».
  - FILTER 1 sur A, **Low 18**, CUTOFF bas (≈ 20 % [ORIGINAL]), DRIVE et FAT montés (≈ 40 et 30 [ORIGINAL]).
  - ENV 2 → CUTOFF ≈ 45 % [ORIGINAL]. ENV 2 : ATK 0, DEC **≈ 2,6 s**, SUS **≈ 17 %**, REL **≈ 380 ms**, courbes plus raides [SOURCE LE-07].
  - VOICING : POLY 8 ; MONO si la partie est une ligne simple [ORIGINAL].
- **ENV 1** : ATK 0 (« très sèche »), SUS un peu au-dessus de la moitié (≈ −5 dB), REL ≈ 120 ms [SOURCE LE-07 ; valeurs en ms ORIGINAL].
- **FX** :
  1. Hyper/Dimension : MIX d'Hyper bas (≈ 15 %), MIX de Dimension haut (≈ 60 %), SIZE un peu baissée [SOURCE LE-07, chiffres ORIGINAL].
  2. Distortion **Tube**, filtre **PRE** en passe-haut vers **300 Hz**, DRIVE poussé (≈ 60), MIX 100 % [SOURCE LE-07].
  3. Equalizer : bande basse en High Pass à 200 Hz [règle 1].
- **Reverb** : seulement externe dans la vidéo. Ici, ValhallaVintageVerb sur un retour.
- **Macros** : `Tone` CUTOFF 10 → 45 % · `Motion` FM (B) 0 → 50 % · `Dirt` DRIVE du Tube 30 → 80 · `Space` envoi BUS 1 0 → 30 %, avec une Reverb Plate sur BUS 1 [ORIGINAL].
- **Jeu** : MIDI 65 à 84, accords de deux ou trois notes possibles en POLY. Le sustain d'ENV 2 à 17 % garde un filtre entrouvert pendant les tenues.
- **Test** : RAND 0 doit donner la même attaque à chaque note (raison donnée par LE-07) ; si l'attaque claque trop, essayer RAND 100 sur A seulement et comparer.

### LD02 Whoop afro
- **Patch** [SOURCE LE-01] :
  - OSC A : Basic Shapes (« Basic MG ») WT POS assez haut, OCT −1, LEVEL un peu baissé.
  - OSC B : saw d'usine, OCT −2, UNISON 3, DETUNE et BLEND baissés, LEVEL baissé.
  - NOISE « AC Hum », un peu plus fort que le défaut.
  - ENV 2 → **SEM** d'OSC A et d'OSC B en **unipolaire** : c'est le « woo ». Plus, dans la matrice, ENV 2 → **Main Tuning**.
  - ENV 2 : ATK montée, SUS 0, DEC un peu baissé, REL baissé ; courbes tordues.
  - FILTER 1 **MG Low 18**, routé A, B et NOISE (le SUB reste éteint, règle 1). CUTOFF monté. LFO 1 rapide → CUTOFF en petite quantité. ENV 2 → CUTOFF aussi. DRIVE monté, FAT un peu.
  - VOICING : MONO [DÉDUCTION : une glissade par note].
- **Valeurs de départ** [ORIGINAL] : ENV 2 ATK 40 ms, DEC 180 ms, REL 60 ms ; profondeur vers SEM +5 demi-tons, vers Main Tuning +2 ; LFO 1 en HZ à 12 Hz, quantité 5 %.
- **ENV 1** : ATK un peu montée (≈ 8 ms), DEC ≈ 300 ms, SUS 0, REL un peu monté (≈ 150 ms) [SOURCE LE-01, valeurs ORIGINAL].
- **FX** [SOURCE LE-01] : Distortion Tube (MIX baissé, ≈ 30 %) → Equalizer (bande basse High Pass vers 200 Hz, aigus en High Shelf) → Chorus (MIX baissé) → Delay (FEEDBACK baissé, FREQ montée, Q baissé, MIX bas) → Reverb (LO CUT actif, MIX monté).
- **Macros** : `Tone` CUTOFF 30 → 70 % · `Motion` ENV 2 → SEM 0 → +7 demi-tons · `Dirt` DRIVE du filtre 10 → 60 · `Space` MIX de la reverb 10 → 40 %.
- **Jeu** : MIDI 67 à 79, notes isolées avec des silences ; le « woo » vient de chaque attaque, donc pas de legato.
- **Test** : la profondeur de SEM (« à vérifier à l'écran » dans l'étude) se cherche à l'oreille. Au-delà de +7, le whoop devient une sirène.

### LD03 Lead afro en doubles croches
- **Patch** [SOURCE LE-02, style 3] : une saw, VOICING MONO, FILTER 1 avec DRIVE. ENV 2 sans sustain, DEC **≈ 150 ms** → CUTOFF.
  - Filtre [ORIGINAL] : MG Low 12, CUTOFF 30 %, RES 15 %, DRIVE 30 ; ENV 2 → CUTOFF 40 %.
  - Matrice : Velocity → CUTOFF 15 % [ORIGINAL], pour suivre la vélocité aléatoire du MIDI.
- **ENV 1** : 0 ms / 0 / 180 ms / −∞ (SUS 0) / 60 ms [SOURCE LE-02 pour SUS 0, durées ORIGINAL].
- **FX** [SOURCE LE-02] : Distortion légère, Chorus, Equalizer (résonances coupées, bande basse High Pass à 200 Hz), Compressor Single, Reverb.
- **Mod Wheel** → MIX de la reverb, MIX du delay et CUTOFF [SOURCE LE-02] : à automatiser sur la frontière de huit mesures.
- **Macros** : `Tone` CUTOFF 20 → 55 % · `Motion` ENV 2 → CUTOFF 20 → 60 % · `Dirt` DRIVE 10 → 50 · `Space` reverb 5 → 30 %.
- **Jeu** : doubles croches légèrement hors grille, vélocités variées (LE-02) ; MIDI 64 à 76. À 122 BPM, une double croche dure 123 ms [CALCUL] : le DEC de 150 ms déborde un peu sur la suivante, ce qui lie les notes.
- **Test** : à DEC 100 ms la ligne se hache, à 250 ms elle s'empâte.

### LD04 Carré afro à vibrato
- **Patch** [SOURCE LE-02, style 2] :
  - OSC A : carrée, UNISON 5, DETUNE modéré.
  - OSC B : saw, OCT +1, moins de sustain que A [DÉDUCTION : ENV 3 sur le LEVEL de B].
  - LFO 2 → FIN des deux oscillateurs, RATE très élevée. LFO 1 très rapide → Main Tuning, très faible quantité.
  - FILTER 1 en **Band 12**, MIX 90 %.
  - VOICING MONO, PORTA réglé ; NOISE ; Distortion ou multibande ; bas retiré.
- **Valeurs de départ** [ORIGINAL] :
  - LFO 2 en HZ, 6 Hz, ±8 cents ;
  - LFO 1 en HZ, 9 Hz, vers Main Tuning 2 % ;
  - PORTA 60 ms, CURVE convexe ;
  - Band 12 : CUTOFF ≈ 1,2 kHz, RES 20 %.
- **ENV 1** : 5 ms / 0 / 400 ms / −8 dB / 200 ms [ORIGINAL].
- **FX** : Distortion Soft Clip DRIVE 20 → Compressor Multiband (MIX 30 %) → Equalizer, High Pass 220 Hz → Reverb Plate, MIX 20 % [ORIGINAL d'après LE-02].
- **Macros** : `Tone` CUTOFF du Band 12 0,6 → 3 kHz · `Motion` LFO 2 → FIN 0 → ±15 cents · `Dirt` DRIVE 0 → 40 · `Space` reverb 10 → 35 %.
- **Jeu** : boucle d'arpège sixte → quinte (LE-02), MIDI 69 à 81, legato pour que le portamento serve.
- **Test** : le vibrato rapide doit rester une agitation, pas un trille ; au-delà de ±15 cents il fausse la note.

### LD05 Sync et Diode 2 — bass house
- **Patch** [SOURCE LE-03, lead 1] :
  - OSC A : Analog « PWM Mini », SEM **+4**, WT POS ≈ 55, LEVEL baissé.
  - OSC B : Analog Basic Shapes, SEM **+7**, WARP 1 **Sync** ≈ 1,9-2 % (unité affichée à vérifier), LEVEL ≈ 50 %.
  - NOISE Analog « J106 HP ».
  - LFO 1 en 1/4, mode **ENVELOPE** → FILTER 1 **MG Low 6**, sur OSC B seulement.
  - VOICING MONO.
  - Le SUB de la vidéo (OCT −3) reste éteint (règle 1).
- **ENV 1** : ATK **≈ 60 ms**, DEC court, SUS, REL [SOURCE LE-03] ; ici 60 ms / 0 / 200 ms / −6 dB / 100 ms [ORIGINAL pour le reste].
- **FX** [SOURCE LE-03] : Compressor Multiband, puis Distortion **Diode 2** (« le caractère »), puis Filter en **SampHold** (dégradation façon bitcrush), Hyper/Dimension avec Hyper bas, Equalizer, MAIN baissé.
- **Hors de Serum** : la vidéo ajoute Sausage Fattener, un overdrive et Kickstart 2 ; ici RazorClip pour l'écrêtage, ShaperBox 3 pour la découpe de volume.
- **Accord des oscillateurs** [CALCUL] : +4 et +7 demi-tons forment une tierce majeure et une quinte au-dessus de la note jouée. Le patch sonne donc un accord majeur en position de tierce et quinte, sans la fondamentale, qui est jouée par la basse ; sur une harmonie mineure, mettre A sur +3.
- **Macros** : `Tone` CUTOFF du MG Low 6 20 → 70 % · `Motion` Sync 0 → la valeur vue à l'écran ×2 · `Dirt` DRIVE de la Diode 2 20 → 70 · `Space` reverb 0 → 25 %.
- **Jeu** : MIDI 60 à 72, motifs courts qui répondent à la basse.
- **Test** : avec la basse, l'accord intégré ne doit pas contredire l'harmonie ; écouter une note sur l'accord mineur du morceau.

### LD06 Saut d'octave par macro
- **Patch** [SOURCE LE-03, lead 2] :
  - NOISE Analog « Bright White ».
  - OSC B : Basic Shapes, frame de la carrée, OCT −3 dans la vidéo. Ici OCT −1, pour rester au-dessus de 150 Hz [ORIGINAL]. WARP 1 **PWM** monté.
  - LFO 1 en 1/8, mode ENVELOPE → Main Tuning **+1**, unipolaire.
  - LFO 2 en HZ, rapide, mode ENVELOPE → Main Tuning **+24** (deux octaves), unipolaire, avec **Aux Source = MACRO 5**. Le saut ne se produit que si la macro est montée.
  - VOICING MONO.
- **Valeurs de départ** [ORIGINAL] : LFO 2 à 8 Hz, forme descendante d'un seul cycle (le saut part en haut et retombe en 125 ms) ; PWM 40 %.
- **ENV 1** : 0 ms / 0 / 300 ms / −4 dB / 80 ms [ORIGINAL].
- **FX** [SOURCE LE-03] : Distortion DRIVE au maximum, Compressor Multiband, Equalizer (bas coupé, aigus montés), Filter MG Low 24 avec DRIVE, Reverb Hall ; MIX de la reverb et de l'EQ automatisés.
- **Macros** : `Tone` CUTOFF du Filter MG Low 24 25 → 80 % · `Motion` LFO 1 → Main Tuning 0 → +1 · `Dirt` DRIVE 60 → 100 · `Space` MIX de la Hall 0 → 30 % · **MACRO 5 `Jump`** : Aux Source du LFO 2, 0 → 100 %.
- **Jeu** : MIDI 60 à 72. `Jump` monte sur la dernière mesure avant un drop ; c'est un geste de transition (règle « Drops »).
- **Test** : un saut de deux octaves sur une note longue s'entend comme un cri ; régler le RATE de LFO 2 pour qu'il ne dépasse pas une croche.

### LD07 FM et attaque de bruit
- **Patch** [SOURCE LE-03, lead 3] :
  - OSC A : Digital « I Can Has Kick », OCT −3 dans la vidéo ; ici OCT −1 [ORIGINAL, règle 1]. WT POS monté, UNISON 2, DETUNE bas, un peu de FIN.
  - OSC B : Spectral « Monster 1 », SEM **+7**.
  - OSC A, WARP 1 **FM (B)** **53 %**.
  - NOISE « Kick Attack 29 », **one-shot**.
  - ENV 2 → FILTER 1 **MG Low 12** sur A et B. Le SUB saw −2 octaves de la vidéo reste éteint.
  - VOICING MONO. LFO 1 en mode ENVELOPE → WT POS d'OSC A.
- **Valeurs de départ** [ORIGINAL] : ENV 2 0 / 0 / 250 ms / 20 % / 100 ms, profondeur 50 % ; LFO 1 en 1/8, forme descendante, vers WT POS 30 %.
- **ENV 1** : 0 ms / 0 / 350 ms / −6 dB / 90 ms [ORIGINAL].
- **FX** [SOURCE LE-03] : Distortion Tube (DRIVE monté, MIX baissé), Chorus, Delay, Hyper/Dimension, Equalizer. Le Saturator de Live de la vidéo devient une seconde Distortion Soft Clip interne.
- **Macros** : `Tone` CUTOFF 20 → 65 % · `Motion` FM (B) 30 → 70 % · `Dirt` DRIVE du Tube 20 → 70 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : MIDI 60 à 72, notes courtes et répétées : l'attaque de bruit fait le « tchak ».
- **Test** : le bruit d'attaque ne doit pas se doubler avec la caisse claire ; sinon baisser son LEVEL ou changer le Kick Attack.

### LD08 Lead qui se transforme
- **Patch** [SOURCE LE-04] :
  - OSC A : Analog Basic Shapes (« Basic MG »), frame de la scie, OCT +1, UNISON **2** (phasing).
  - OSC B : Digital « Distorted Bass Dropper », UNISON **4 à 6**. DETUNE des deux à peine au-dessus de 0.
  - LFO 1 : rampe montante, mode **FREE**, RATE **1 mesure** (1 bar) ; la forme finit au troisième temps.
  - LFO 1 → DETUNE des deux oscillateurs (jusqu'à mi-course) et → DEC d'ENV 1.
  - FILTER 1 en **Flg** négatif (famille Flanges, variante « − » ; « Negative Flanger » dans Serum 1) sur A et B, RES et DRIVE élevés. LFO 1 → MIX du filtre, en négatif.
- **ENV 1** : SUS 0, courbe de decay moins creusée, DEC réglé pour couper la queue (stab) [SOURCE LE-04] ; ici 0 ms / 0 / 200 ms / −∞ / 40 ms [ORIGINAL].
- **FX** [SOURCE LE-04] :
  1. Distortion **Diode 1**, peu de DRIVE.
  2. Filter Low 12 ou 18, CUTOFF vers 11 h. LFO 1 → CUTOFF à fond ; ENV 2 (SUS 0, DEC court) → CUTOFF, faible quantité.
  3. Flanger (MIX bas à moyen), Chorus, Hyper/Dimension tard dans la chaîne, Compressor léger.
  4. Après Serum : Pro-Q 4 en dynamique, à la place des modules Neutron et Pro-Q 3 de la vidéo.
- **Durée** [CALCUL] : à 126 BPM, trois temps durent 1,43 s ; la mesure entière dure 1,90 s. Ce que fait le quatrième temps (valeur tenue ou retour au départ) dépend de la forme dessinée, à lire à l'écran (LE-04).
- **Macros** : `Tone` CUTOFF du Filter 30 → 70 % · `Motion` profondeur de LFO 1 0 → 100 % · `Dirt` DRIVE de la Diode 1 0 → 40 · `Space` MIX du Chorus 0 → 40 %.
- **Jeu** : la mélodie de basse convertie en doubles croches (LE-04), MIDI 60 à 72.
- **Test** : en mode FREE, le LFO suit l'horloge de l'hôte. Le lancer depuis plusieurs points de l'arrangement et vérifier que la transformation tombe toujours sur les mêmes temps.

### LD09 Lead riche melodic house
- **Patch** [SOURCE LE-05, Serum 2] :
  - OSC A : saw par défaut, UNISON monté, DETUNE haut, LEVEL baissé. WARP 1 **PD (Noise)** ; NOISE actif, « AC Hum », LEVEL et PITCH bas.
  - OSC B : « Saw Drift 303 », WARP 1 **Hard Clip**, RAND 0, PHASE 0.
  - OSC C : Basic Shapes, sinus, LEVEL baissé, WARP 1 **Bend +/−** poussé jusqu'à une forme presque en scie, RAND 0, PHASE 0.
  - FILTER 1 **MG Low 24** sur A, B et C, CUTOFF monté, ENV 1 → CUTOFF en **bipolaire**, DRIVE et FAT montés, RES inchangée.
  - FILTER 1 envoyé à 100 % vers **BUS 1**.
- **Valeurs de départ** [ORIGINAL] : UNISON 5, DETUNE 0,3 ; PD 15 % ; Hard Clip 30 % ; Bend +/− 75 % ; CUTOFF 35 %, ENV 1 → CUTOFF ±25 %.
- **ENV 1** : un peu d'ATK, moins de SUS, moins de DEC, plus de REL [SOURCE LE-05] ; ici 15 ms / 0 / 500 ms / −10 dB / 600 ms [ORIGINAL].
- **BUS 1** [SOURCE LE-05] : Chorus (LPF, DEPTH baissée), Delay **1/8 pointée + 1/8** (FREQ montée, Q baissé), Reverb **Plate** moins brillante, puis Reverb **Hall** plus grande ; LO CUT.
- **MAIN** [SOURCE LE-05] : Equalizer en High Pass, Distortion **Soft Clip** avec ENV 1 → DRIVE, Equalizer en Peak (bosse), Hyper/Dimension (Hyper à 0, SIZE baissée), Compressor.
- **Delay** [CALCUL] : à 122 BPM, 1/8 pointée = 368,9 ms et 1/8 = 245,9 ms ; à 124 BPM, 362,9 et 241,9 ms.
- **Macros** : `Tone` CUTOFF 20 → 60 % · `Motion` PD (Noise) 0 → 40 % · `Dirt` DRIVE du Soft Clip 0 → 50 · `Space` niveau de BUS 1 50 → 120 %. La vidéo met CUTOFF et WIDTH en macros : WIDTH de l'Utility interne en MACRO 5.
- **Jeu** : MIDI 62 à 81, notes longues ; « plus serré » = baisser le DEC (LE-05).
- **Test** : deux reverbs plus un delay remplissent vite. Écouter le lead avec le pad : il faut que l'un des deux soit étroit (règle 6).

### LD10 Lead cinématique
- **Patch** [SOURCE LE-06] :
  - OSC A : « Hyper Digital Saw », UNISON monté, BLEND baissé. LFO lent → FIN, petite quantité : la dérive « de bande ».
  - OSC B : copie de A, OCT +1, **UNISON 2** (deux voix, aucune au centre : couche purement large). Second LFO → FIN : vibrato.
  - FILTER 1 **Low 12**, un peu de RES et de DRIVE, A et B.
  - ENV 2 → CUTOFF, ATK et DEC lents ; ENV 1 avec une ATK plus courte.
  - NOISE « Arp White » **hors du filtre** (routé vers MAIN), avec son enveloppe : ENV 3, ATK douce, DEC plus court. Matrice : ENV 3 → LEVEL du NOISE.
- **Valeurs de départ** [ORIGINAL ; vibrato FICHE] :
  - dérive : LFO 3 en HZ à 0,3 Hz, FREE, ±6 cents ;
  - vibrato : LFO 4 à 7 Hz, DELAY 200 ms, ±10 cents [FICHE] ;
  - ENV 2 400 ms / 0 / 1,5 s / 40 % / 800 ms ;
  - ENV 3 150 ms / 0 / 600 ms / 0 / 300 ms.
- **ENV 1** : 30 ms / 0 / 2 s / −4 dB / 900 ms [ORIGINAL].
- **FX** [SOURCE LE-06] : Hyper/Dimension subtil, Delay subtil **avant** la Reverb. Un LFO en rampe montante, mode ENVELOPE, sur le MIX de la Reverb : plus la note est tenue, plus elle baigne. Distortion **Tape Sat.** avec son filtre interne qui coupe le bas, puis Equalizer en High Pass.
- **Valeurs** [ORIGINAL] : LFO 5 en ENVELOPE, RATE 2 mesures, vers MIX de la Reverb de 10 à 45 %.
- **Macros** : `Tone` CUTOFF 25 → 70 % · `Motion` dérive 0 → ±15 cents · `Dirt` DRIVE de la Tape Sat. 0 → 40 · `Space` profondeur du LFO 5 0 → 40 %.
- **Jeu** : MIDI 60 à 79, notes longues ; le vibrato retardé ne se montre que sur les tenues.
- **Test** : la dérive ne doit pas faire paraître la note fausse contre le pad ; ±6 cents est un départ prudent.

### LD11 Saw percussive future rave
- **Patch** [SOURCE LE-08, en français, transcription très bruitée] :
  - OSC A : Digital « HyPA » [ASR ?] ; à défaut, Basic Shapes en scie [ORIGINAL]. **UNISON 16, RAND 0, DETUNE 0** : les voix identiques n'apportent que du niveau dans le drive.
  - NOISE « Bright » [ASR ?] indispensable, ENV 1 sur son LEVEL, PITCH monté.
  - FILTER 1 **MG Low 18**, peu de RES, coupe légère pour limiter la fondamentale, DRIVE monté, un peu de FAT.
  - ENV 2 très courte, **≈ 50 ms** → DRIVE du filtre : la percussion.
  - LFO en HZ, rapide, mode ENVELOPE → **Main Tuning** : coup de hauteur à l'attaque.
- **Valeurs de départ** [ORIGINAL] : CUTOFF 60 %, DRIVE 40, ENV 2 → DRIVE +50 ; LFO 1 à 20 Hz (un cycle = 50 ms [CALCUL]), forme descendante, vers Main Tuning +7 demi-tons.
- **ENV 1** : 0 ms / 0 / 150 ms / SUS très bas (« ≈ −60 dB ») / 80 ms [SOURCE LE-08 pour SUS ; durées ORIGINAL].
- **FX** [SOURCE LE-08] :
  1. Compressor **Multiband** à la place de l'OTT (« quasi indispensable »). ENV 2 → gains des bandes haute et moyenne, unipolaire.
  2. Equalizer : grosse bosse large en Peak vers 2-3 kHz ; ENV 3, copie plus longue d'ENV 2, → GAIN de cette bande.
  3. En option, Distortion avec filtre en passe-bande sur les médiums.
  4. Reverb.
- **Macros** : `Tone` CUTOFF 40 → 85 % · `Motion` LFO 1 → Main Tuning 0 → +12 · `Dirt` ENV 2 → DRIVE 20 → 80 · `Space` reverb 0 → 20 %.
- **Variante plus ronde** [SOURCE LE-08] : une enveloppe à attaque arrondie sur le LEVEL de l'oscillateur ; le bruit attaque alors en premier.
- **Jeu** : MIDI 60 à 76, notes courtes. Le timbre seul est repris du titre de la vidéo, pas sa mélodie.
- **Test** : UNISON 16 coûte du CPU (cartographie, § 9) ; comparer avec UNISON 4, qui donne presque le même drive.

### LD12 Lead mono expressif — signature sous 124
- **Patch** [FICHE, ORIGINAL] :
  - OSC A : Basic Shapes, frame de la carrée, WARP 1 **PWM** ≈ 60 % : impulsion étroite, son « fin et nasal » qui dégage la zone 1-4 kHz de la voix.
  - OSC B : sinus, OCT 0, LEVEL 30 % : corps sans élargir.
  - FILTER 1 **MG Low 24**, CUTOFF 40 %, RES 10 %. ENV 2 → CUTOFF 25 % : 5 ms / 0 / 600 ms / 30 % / 300 ms.
  - VOICING **MONO + LEGATO**, PORTA 70 ms, SCALED.
  - LFO 1 en HZ à **7 Hz**, DELAY **200 ms** [FICHE], RISE 150 ms [ORIGINAL] → FIN d'A et B, ±10 cents.
- **ENV 1** : 10 ms / 0 / 800 ms / −6 dB / 250 ms [ORIGINAL].
- **FX** : Distortion Tape Sat. DRIVE 20, MIX 40 % → Chorus MIX 15 % → Equalizer en High Pass 180 Hz → Compressor Single ratio 3:1, attaque et release courts (ratio 3-4 [FICHE]) → Delay 1/8 pointée, MIX 12 %.
- **Vibrato** [CALCUL] : à 124 BPM, une croche dure 242 ms et une noire 484 ms. Avec 200 ms de DELAY et 150 ms de RISE, le vibrato commence à peine sur une croche et ne se déploie que sur une noire ou plus, comme chez un chanteur [FICHE].
- **Macros** : `Tone` CUTOFF 25 → 60 % · `Motion` vibrato 0 → ±20 cents · `Dirt` DRIVE 0 → 45 · `Space` MIX du Delay 0 → 25 % · MACRO 5 `Glide` PORTA 0 → 150 ms.
- **Jeu** : MIDI 67 à 84, phrases chantées, intervalles conjoints, glissades sur les notes liées.
- **Test** : avec le kick de la signature (`../../../drums-signature/references/signature.md`), le lead doit rester doux ; s'il durcit, baisser la Tape Sat. avant le CUTOFF.

### LD13 Supersaw dancefloor DnB
- **Patch** [SOURCE LE-10, lead 1] :
  - OSC A : saw, **UNISON 7**, DETUNE baissé, « pas trop ». MODE d'unison **Super** [DÉDUCTION, cartographie § 3.1 : « supersaw »]. RAND 100 [FICHE : phase libre à chaque note].
  - NOISE « Bright White » dans FILTER 1 en **High 12**, LEVEL bas.
  - VOICING POLY 6 [ORIGINAL].
- **ENV 1** : REL **200-400 ms** [SOURCE LE-10] ; ici 2 ms / 0 / 1 s / −3 dB / 300 ms [ORIGINAL pour le reste].
- **FX** [SOURCE LE-10] : Hyper/Dimension, Distortion avec DRIVE monté, Delay, Reverb ; Equalizer en High Pass avec une bosse dans les médiums et les aigus.
- **Valeurs de départ** [ORIGINAL] : DETUNE 0,2 ; Distortion Tube DRIVE 30 ; Delay 1/8, FEEDBACK 25 %, MIX 15 % ; High Pass 250 Hz.
- **Delay** [CALCUL] : à 174 BPM, 1/8 = 172,4 ms et 1/8 pointée = 258,6 ms.
- **Macros** : `Tone` FREQ du High Pass 150 → 400 Hz · `Motion` DETUNE 0,1 → 0,4 · `Dirt` DRIVE 10 → 50 · `Space` MIX de la Reverb 5 → 30 %.
- **Jeu** : croches (LE-10), accords de trois notes, MIDI 64 à 84.
- **Test** : un supersaw en unison 7 est l'élément large ; le pad ou le Reese doit alors être étroit.

### LD14 Stab carré rave
- **Patch** [SOURCE LE-10, lead 2] :
  - OSC A : Basic Shapes, frame du triangle, SEM **−7**.
  - OSC B : Basic Shapes, frame de la carrée, OCT **+2** ; c'est le ton aigu qui prime.
  - FILTER 1 **Low 24** sur A et B, CUTOFF **≈ 1000 Hz**.
  - VOICING POLY 4.
- **Intervalles** [CALCUL] : −7 demi-tons font une quinte juste en dessous de la note jouée. La note obtenue est la quarte de la tonalité (un Do joué donne un Fa grave), d'où le mot « quarte » de la vidéo. La carrée sonne deux octaves au-dessus de la note.
- **ENV 1** : 0 ms / 0 / 250 ms / −12 dB / 120 ms [ORIGINAL].
- **FX** [SOURCE LE-10] : Distortion en mode **PRE** avec passe-haut vers **200-300 Hz**, DRIVE **au maximum** ; Hyper/Dimension en option ; Equalizer, Reverb et Delay.
- **Variantes** [SOURCE LE-10] : Hyper avant la Distortion, plus de REL, niveaux des oscillateurs au maximum pour plus de drive.
- **Macros** : `Tone` CUTOFF 0,5 → 3 kHz · `Motion` ENV 2 → CUTOFF 0 → 40 % (ENV 2 : 0 / 0 / 120 ms / 0 / 50 ms [ORIGINAL]) · `Dirt` LEVEL des oscillateurs 60 → 100 % · `Space` MIX de la Reverb 0 → 25 %.
- **Jeu** : doubles croches (LE-10), MIDI 60 à 72 ; à 174 BPM une double croche dure 86,2 ms [CALCUL].
- **Test** : le DRIVE au maximum peut écraser les accords ; essayer des quintes à vide plutôt que des triades.

### LD15 Carré émotionnel « 8-bit »
- **Patch** [SOURCE LE-11, Serum 2] :
  - OSC A : Analog **Basic MG** [ASR « basic MDC »], WT POS un peu vers le sinus (marge pour la distorsion), octave haute (OCT +1 [DÉDUCTION]).
  - OSC B : sinus, octave basse (OCT 0) ; il sert de source de **PD**.
  - OSC C : sinus, OCT **−2** dans la vidéo ; ici éteint (règle 1) ou à LEVEL 0 [ORIGINAL].
  - OSC A, WARP 1 **PD (B)** : « ce qui s'appelait FM dans l'ancien Serum ». LEVEL de B baissé, d'où un léger vibrato. Plus de PD = plus de grain.
  - LFO 1 → LEVEL de l'OSC A : le volume se creuse puis remonte dans la même noire.
- **Valeurs de départ** [ORIGINAL] : PD 12 % ; LFO 1 en 1/4, RETRIG, forme en V (creux au milieu), profondeur −40 %.
- **Respiration** [CALCUL] : à 174 BPM, une noire dure 344,8 ms ; le creux tombe vers 172 ms.
- **ENV 1** : 2 ms / 0 / 1,5 s / −2 dB / 250 ms [ORIGINAL].
- **FX** [SOURCE LE-11] : Hyper/Dimension large et Chorus, MIX baissés → Distortion **Hard Clip** → Delay court, réglage d'usine « slap delay » [ASR] → Reverb **Plate** → Equalizer en Peak vers **1 kHz** → écrêtage après la reverb.
- **Hors de Serum** : la vidéo met une reverb longue externe et K-Clip après la reverb ; ici ValhallaVintageVerb sur un retour, RazorClip en insert.
- **Macros** : `Tone` WT POS 20 → 60 % · `Motion` profondeur du LFO 1 0 → −60 % · `Dirt` DRIVE du Hard Clip 10 → 50 · `Space` MIX de la Plate 10 → 35 %.
- **Jeu** : MIDI 67 à 84, notes de deux à quatre temps ; la vidéo est en do mineur, la grille de ce fichier aussi, avec une mélodie écrite ici.
- **Test** : la respiration doit suivre la noire du break ; si elle contrarie le groove, passer le LFO en 1/2.

### LD16 Lead neuro désaccordé
- **Patch** [SOURCE LE-12, Serum 2] :
  - OSC A : saw, OCT **−3** dans la vidéo ; ici OCT −1 [ORIGINAL, règle 1]. WARP 1 en **FM**, quantité **30** (« new FM function », source à lire à l'écran) ; variante WARP 2 **Flip**.
  - OSC B : saw, OCT **−1**, SEM **+4** dans la vidéo ; ici OCT +1, SEM +4, pour garder l'écart avec A. Variante WARP 1 **Asym +**.
  - OSC C : Digital « DX Brass 2 », OCT **−1**, WT POS **≈ 35**, **FM (B)** 30, LEVEL baissé.
  - VOICING **MONO**, PORTA avec **ALWAYS** (« Always Legato »).
  - FILTER 1 **MG Low 12** sur A et B. Un LFO à forme régulière → CUTOFF, inversé.
  - FILTER 2 **Wsp** (catégorie New ; VAR = MORPH) sur OSC C seul, même LFO, DRIVE et MORPH montés.
- **Intervalle** [CALCUL] : avec les octaves de la vidéo, B sonne deux octaves et une tierce majeure au-dessus de A. En gardant cet écart (A OCT −1, B OCT +1, SEM +4), la note grave reste au-dessus de 150 Hz pour MIDI ≥ 63.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1/2, RETRIG, triangle ; profondeur −30 % vers les deux CUTOFF ; PORTA 40 ms.
- **ENV 1** : 0 ms / 0 / 1 s / −3 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE LE-12] :
  1. Distortion **Tape Sat.** légère, LFO → DRIVE.
  2. Equalizer : bas coupé, pic dans le haut-médium, même modulation.
  3. Compressor **Multiband**.
  4. **Splitter L/H** vers **500 Hz** ; sur la bande haute, **Convolve** (IR « 10 Amp Box » [ASR ?]), SIZE **30-40**, plus brillant, avec une modulation de son MIX.
  5. Reverb **Plate** avec un MIX modulé.
- **Macros** : `Tone` CUTOFF 20 → 70 % · `Motion` FM 15 → 45 · `Dirt` DRIVE de la Tape Sat. 0 → 50 · `Space` MIX de la Plate 0 → 30 % · MACRO 5 `Flip` WARP 2 0 → 5 % [SOURCE LE-12 : macro vers Flip ≈ 5 %].
- **Jeu** : MIDI 63 à 79, lignes liées pour que le glide se fasse.
- **Test** : la vidéo propose un sub à −3 octaves en Direct Out ; ici, le sub vient de `dnb-f01-sub.md` sur sa piste.

### LD17 Pad sync devenu lead arpégé
- **Patch** [SOURCE LE-09] :
  - OSC A : Basic Shapes, frame de la scie. OSC B : « MB Saw » [ASR ?], OCT **+1**. UNISON monté et DETUNE baissé sur les deux.
  - WARP 1 **Sync** sur A et B ; un LFO lent, **2 mesures**, peu intense → Sync des deux.
  - ENV 1 avec un SUS baissé.
  - Pour le lead : ARP de Serum, accords réduits à trois notes. Un LFO à forme « pluck » → LEVEL d'A et B. FILTER 1 sur A et B, LFO → CUTOFF.
  - En option : une ATK, une couche à la quinte, un peu de REL.
- **Valeurs de départ** [ORIGINAL] :
  - UNISON 4, DETUNE 0,12 ;
  - LFO 1 en 2 bar, FREE, sinus, vers Sync 15 % ;
  - LFO 2 en 1/16, RETRIG, forme descendante raide (montée instantanée, descente en 60 % du pas), vers LEVEL −80 % ;
  - FILTER 1 MG Low 12, CUTOFF 45 %, LFO 2 → CUTOFF 30 % ;
  - ARP : 1/16, Up, une octave.
- **Durées** [CALCUL] : à 174 BPM, deux mesures durent 2,76 s et une double croche 86,2 ms.
- **ENV 1** : 0 ms / 0 / 800 ms / −6 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE LE-09] : Hyper/Dimension (Hyper bas) → Distortion **Downsample**, DRIVE très bas, MIX baissé (« de la saleté dans les aigus ») → Reverb SIZE et DECAY montés, LO CUT, HI CUT au minimum.
- **Pseudo-sidechain** [SOURCE LE-09] : un LFO en mode ENVELOPE, forme montante → MIX de la Reverb. Ici LFO 3 en 1/4, RETRIG, de 0 à 35 % [ORIGINAL].
- **Macros** : `Tone` CUTOFF 30 → 70 % · `Motion` LFO 1 → Sync 0 → 30 % · `Dirt` DRIVE du Downsample 0 → 20 · `Space` MIX de la Reverb 10 → 40 %.
- **Jeu** : accords de trois notes tenus, MIDI 60 à 79 ; l'ARP les découpe.
- **Test** : la vidéo enchaîne un pad et un lead issus du même patch. Garder les deux et alterner sur les frontières de huit mesures.

### LD18 Melodic dubstep à un LFO
- **Patch** [SOURCE LE-13] :
  - OSC A : Analog Basic Shapes (« Basic MG » [ASR « MDC »]). LFO 1 → WT POS **8** et → LEVEL de l'OSC A.
  - LFO 1 : **1 mesure**, forme d'enveloppe, déclenché à chaque note : mode **RETRIG**.
  - FILTER 1 [nom ASR], LFO 1 → CUTOFF et RES ; RES baissée, modulation **≈ 65**, CUTOFF **≈ 72** [ASR], DRIVE vers **14 h**.
  - VOICING **MONO + LEGATO**, PORTA vers **12 h**.
  - NOISE (dossier Organics), PITCH **70**, LEVEL bas, LFO ≈ **15**.
  - Le SUB de la vidéo (LFO 1 → LEVEL 17) reste éteint (règle 1).
- **Choix du filtre** [ORIGINAL] : MG Low 24, puisque le nom dit est illisible.
- **ENV 1** : 0 ms / 0 / 2 s / −2 dB / 200 ms [ORIGINAL].
- **FX** [SOURCE LE-13] :
  1. Hyper/Dimension : les deux MIX et la SIZE à 0, LFO 1 → **20** et **25-30**.
  2. Distortion **Soft Clip**, DRIVE 0, LFO 1 → DRIVE **≈ 55**.
  3. Equalizer : bande basse vers **30 Hz**, LFO → FREQ **50**, GAIN **≈ +12 dB** ; bande haute FREQ au maximum, modulée vers le bas, GAIN **−10** : un effet de formant.
  4. Compressor Multiband, gains ≈ 10 dB [ASR].
  5. Filter **Flg** négatif (« Flange −1 » [ASR]) : CUTOFF **289 Hz**, LFO **7**, RES **64 %**, modulation **70**, DRIVE **25 %**.
- **Vibrato** [SOURCE LE-13] : LFO 2 → Main Tuning, **unipolaire, 1**, RATE **1/16**. À 140 BPM, 1/16 = 107,1 ms, soit 9,3 Hz [CALCUL].
- **Conflit avec la règle 1** [DÉDUCTION] : la bande basse de l'EQ montée de +12 dB vers 30-80 Hz contredit la règle. Ici, bande basse en Peak, de 300 à 800 Hz par le LFO, GAIN +6 dB [ORIGINAL] ; un Equalizer en High Pass à 180 Hz est ajouté en fin de chaîne.
- **Durée** [CALCUL] : à 140 BPM, la mesure de LFO 1 dure 1,71 s ; à 150 BPM, 1,60 s.
- **Macros** : `Tone` CUTOFF 50 → 85 % · `Motion` profondeur générale de LFO 1 (par une macro sur ses destinations) 0 → 100 % · `Dirt` LFO 1 → DRIVE 0 → 70 · `Space` MIX de la Dimension 0 → 40 %.
- **Jeu** : MIDI 60 à 79, une note longue par mesure ou deux ; changer la forme de LFO 1 ou la RES donne des sons robotiques, du côté riddim (LE-13).
- **Test** : une note plus courte qu'une mesure coupe le LFO avant la fin ; c'est voulu ou non selon la phrase.

### LD19 Brostep à double warp
- **Patch** [SOURCE LE-14, Serum 2] :
  - OSC A : Analog « Acid », OCT ±3 [ASR, sens à lire à l'écran], RAND 0, WT POS **≈ 5**. WARP 1 **Sync ≈ 1,10 %** [ASR ?], WARP Var à fond à droite (moins dur).
  - LFO 1 : pente simple, mode **ENVELOPE** → Sync. LEVEL d'OSC A baissé ; LFO 1 → LEVEL **90 %**.
  - OSC B : Basic Shapes, OCT **+1**, RAND 0. WARP 1 **Bend −**, LFO 1 → **60 %**. WARP 2 **PD (C)** **30 %** ; LFO 1 → LEVEL.
  - OSC C : table « JNO » [ASR ?], OCT **−3**, **LEVEL 0** : source de PD seulement. Il ne sort aucun son, donc la règle 1 est tenue.
  - NOISE blanc, LFO 1 → LEVEL du NOISE, un peu.
- **Choix d'octave** [ORIGINAL] : OSC A en OCT 0 tant que l'écran n'a pas tranché ; OCT −3 tomberait sous 150 Hz.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1/4, ENVELOPE, rampe descendante.
- **ENV 1** : 0 ms / 0 / 600 ms / −4 dB / 100 ms [ORIGINAL].
- **FX** [SOURCE LE-14] : Distortion **Diode 2**, DRIVE à mi-course, MIX baissé → Hyper/Dimension subtil → deux Compressor **Multiband** → Equalizer, aigus montés.
- **Macros** : `Tone` WT POS 0 → 40 % · `Motion` LFO 1 → Sync 0 → 100 % · `Dirt` DRIVE de la Diode 2 30 → 80 · `Space` MIX de la Dimension 0 → 30 %.
- **Jeu** : MIDI 55 à 72, notes d'une croche à une noire ; le timbre de « Voltage » est la cible, pas ses notes.
- **Test** : le Sync est l'endroit où les valeurs dites divergent le plus (≈ 2 % en LE-03, ≈ 1,10 % ici, ≈ 140-150 % ailleurs). Lire l'unité affichée avant de fixer la macro.

### LD20 Robot lead
- **Patch** [SOURCE LE-15, en français] :
  - OSC A : OCT **−2** dans la vidéo, ici OCT −1 [ORIGINAL] ; table Digital à identifier [ASR], ou Spectral **Monster 3**.
  - LFO 1, mode RETRIG (« trigger on »), → WT POS et LEVEL de l'OSC A, quantité réduite.
  - WARP 1 **FM (B)** ; OSC B : Analog Basic Shapes, scie, **LEVEL 0**. Un réglage d'OSC B monté (« fréquence plus haute, moins précise ») : SEM ou CRS [interprétation de l'étude].
  - FILTER 1 sur A seul : **Reverb** (catégorie Misc ; variante Combs), **suivi au clavier** (icône piano) pour garder des harmoniques cohérentes d'une note à l'autre. CUTOFF fixe, pas de modulation, un peu de DRIVE.
- **Valeurs de départ** [ORIGINAL] : FM (B) 35 % ; OSC B SEM +7 ; CUTOFF du filtre Reverb 50 %, VAR (DAMP) 40 %, DRIVE 15.
- **ENV 1** : 0 ms / 0 / 300 ms / −10 dB / 60 ms [ORIGINAL].
- **FX** [SOURCE LE-15] :
  1. Compressor **Multiband**, GAIN monté.
  2. Hyper ≈ **30 %**, UNISON **7** ; Dimension ≈ **20 %**.
  3. Delay très court : LINK actif, en MS, **≈ 20 ms**, MIX **≈ 70 %**, FEEDBACK 0.
  4. Reverb en option (DECAY court, SIZE grande) pour ponctuer.
- **Delay de 20 ms** [CALCUL] : mélangé au son sec, il crée un filtre en peigne. Les creux tombent à 25, 75, 125 Hz… (tous les 50 Hz), les bosses à 50, 100, 150 Hz… ; c'est une partie du timbre « robot ».
- **Macros** : `Tone` CUTOFF du filtre Reverb 30 → 70 % · `Motion` FM (B) 10 → 60 % · `Dirt` GAIN du Multiband 0 → 12 dB · `Space` MIX du Delay 40 → 80 %.
- **Jeu** : notes ponctuelles entre les phrases de basse, MIDI 60 à 72.
- **Test** : en changeant le temps du delay de 20 à 15 ou 25 ms, le peigne se déplace ; choisir à l'oreille celui qui ne creuse pas la note jouée.

## Motifs de départ (grilles vérifiées)

Numérotation de Live (C3 = 60). Les mélodies sont écrites ici, aucune n'est reprise d'un titre. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/synths/leads.md`. La notation Producer Pal s'obtient avec `--fichier references/synths/leads.md --titre <titre> --format ppal`, et `--transposer N` donne la tonalité du Set.

```grille
titre: Afro house 122 — lead en doubles croches (LD03)
tempo: 122
accords: Am7 | Fmaj7
lead: A3[1&:1] C4[1a:1] E4[2&:2] D4[3e:1] C4[3&:1] A3[3a:1] G3[4&:2] | A3[1&:1] C4[1a:1] E4[2&:2] F4[3e:1] E4[3&:1] C4[3a:1] A3[4&:2]
```

```grille
titre: Future house 126 — lead FM (LD01)
tempo: 126
accords: Fm | Db
lead: F3[1:2] Ab3[1&:1] C4[1a:2] Bb3[2&:1] Ab3[2a:1] F3[3&:2] Eb3[4:1] F3[4e:2] | F3[1:2] Ab3[1&:1] Db4[1a:2] C4[2&:1] Db4[2a:1] Ab3[3&:2] F3[4:1] Ab3[4e:2]
```

```grille
titre: DnB 174 — carré émotionnel (LD15)
tempo: 174
accords: Cm | Ab
lead: G4[1:4] F4[2:2] Eb4[2&:2] C4[3:4] D4[4:2] Eb4[4&:2] | C5[1:4] Bb4[2:2] Ab4[2&:2] Eb4[3:6] C4[4&:2]
```

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 les tables et bruits dits dans les vidéos : « PWM Mini », « J106 HP », « I Can Has Kick », « Monster 1 » et « Monster 3 », « Kick Attack 29 », « Distorted Bass Dropper », « Saw Drift 303 », « Hyper Digital Saw », « Arp White », « DX Brass 2 », « Acid ». Les noms marqués [ASR] sont à identifier à l'écran.
- Lire l'unité du warp Sync et la valeur de FM « new FM function » de LE-12 avant de fixer les macros.
- Écouter chaque recette selon la règle 10, garder deux ou trois leads par morceau et consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
- Fichiers suivants du lot : plucks, hooks, accords, pads, drones.
