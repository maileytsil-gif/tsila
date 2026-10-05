# Vingt recettes de pads dans Serum 2

Cinquième fichier du lot de synthés : nappes tenues, pads rythmés par LFO, pads de samples figés. Rédigé le 05/10/2026. Sources :
- l'étude des quinze tutoriels de pads, PA-01 à PA-15, de `../tutoriels-synths-serum.md`, et sa synthèse `../synths-serum-synthese.md` (section Pad) ;
- les trois patchs chiffrés et les points de départ de `../leads-nappes-textures.md` (§ 3, nappes), traduits ici dans Serum 2 ;
- la cartographie de Serum 2 (`../serum2-cartographie.md`) et `../serum2-fx-clip-arp.md`.

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes : **[SOURCE PA-nn]**, **[FICHE]**, **[CALCUL]**, **[DÉDUCTION]**, **[ORIGINAL]**, comme dans `leads.md`.

## Règles

Les dix règles communes au lot sont dans `leads.md`. Ce qui s'ajoute pour les pads :

1. **High Pass entre 100 et 280 Hz.** La fiche propose LP 700-800 Hz et HP 250-300 Hz pour vider la zone du kick et des voix [FICHE] ; un pad seul en intro peut descendre à 100 Hz. Le SUB de Serum peut servir de quatrième oscillateur s'il sonne au-dessus du High Pass (règle 1 de `leads.md` : elle vise la fonction de sub, pas le module).
2. **Trois vitesses de mouvement** [FICHE] : un mouvement rapide (grain, ≈ 13 Hz), un lent (respiration, ≈ 0,5 Hz), une enveloppe très longue (12-15 s) qui fait entrer une couche. À 122 BPM, 15 s valent 7,6 mesures [CALCUL] : le pad change de timbre vers la huitième mesure, sur la frontière exigée par la règle « Drops ».
3. **Un LFO qui ralentit un autre LFO** (PA-01, PA-02) : une enveloppe ou un LFO en mode ENVELOPE sur le RATE du LFO principal. Le mouvement change de vitesse pendant la note.
4. **La reverb fait partie du son ou du mix** [FICHE] : en insert à MIX 60-100 %, elle appartient au patch et sera resamplée avec lui ; en retour à 10-30 %, elle appartient au mix. Chaque fiche dit lequel.
5. **Le pad cède la largeur** : si le lead ou les accords sont larges, le pad se resserre (règle 6 de `leads.md`). Le pad le plus large du morceau se vérifie en mono.
6. **Polyphonie** : POLY 8 à 16 pour des accords étendus (PA-11 met la polyphonie au maximum) ; l'unison multiplie les voix.
7. **Référence A/B du fichier** : PD01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| PD01 | Pad deep chiffré | Deep house, référence A/B | sinus plié + table en FM (A), MG Low 18 à 469 Hz, trois enveloppes, Diode 1, Hall 61 % |
| PD02 | Pad Juno | Deep house | scie Juno unison 5, copie à l'octave, LFO qui ralentit |
| PD03 | Pad aux dix astuces | Deep, melodic, garage house | unison 5 × 2, bruit en one-shot, LFO sur le rate d'un LFO, Phaser, Chorus |
| PD04 | Pad afro à bruit pané | Afro house | sinus unison 9 + table unison 12, LFO d'une mesure sur WT POS, bruit pané |
| PD05 | Pad rythmé par l'arpégiateur | Progressive, melodic house | ARP en accords, MG Ladder fermé, LFO en marches sur l'octave, deux bus |
| PD06 | Pad rythmé par LFO | Melodic house | deux scies arrondies, LFO 1/16 avec RISE sur le cutoff, portamento |
| PD07 | Pad analogique qui dérive | Melodic house et techno | oscillateurs pannés, deux enveloppes lentes, Chaos sur Main Tuning |
| PD08 | Pad minimal à LFO de quatre mesures | Minimal, deep house | scie MB Saw, LFO de 4 mesures sur WT POS et warp |
| PD09 | Pad à trois vitesses | Melodic, ambient techno | quatre sinus, Sync à 13 Hz, couche qui entre après 15 s |
| PD10 | Pad à enveloppes opposées | Deep, melodic | deux couches d'attaques 5 ms et 3 s, pan par deux LFO |
| PD11 | Pad désaccordé de quelques cents | Deep house | 12 voix à 3-4 cents, phases fixées, Chorus à 0,22 Hz |
| PD12 | Pad liquid de 7e et 9e | DnB liquide | variante pad d'AC14, attaque lente |
| PD13 | Pad Serum 2 à trois couches | DnB liquide, ambient | table d'accords, oscillateur granulaire inversé, bruit Rain, Splitter |
| PD14 | Pad atmosphérique en sept points | DnB atmosphérique | polyphonie maximale, ADSR longues, Low suivi au clavier, accords jusqu'au m11 |
| PD15 | Pad liquid à trémolo | DnB liquide | sinus × 2 en unison, LP 24, LFO de 2 mesures, trémolo 1/16 |
| PD16 | Pad liquid sombre | DnB liquide sombre | table spectrale « glassy », glissé de hauteur à l'attaque |
| PD17 | Pad de sample figé | Melodic bass, ambient | moteur Spectral en Manual, S&H lissé sur la position |
| PD18 | Pad d'accords future bass | Future bass | scies unison, clic d'attaque, German LP, « wawa » en 1/4 triolet, reverb retardée |
| PD19 | Pad de drop melodic dubstep | Melodic dubstep | trois couches à l'octave, filtre Reverb, Dimension, reverb en insert |
| PD20 | Pad qui est sa reverb | Breaks, intros | reverb à 100 % en insert, filtrée, resamplée |

## Les vingt recettes

### PD01 Pad deep chiffré — référence du fichier
- **Patch** [SOURCE PA-05, le tutoriel le plus chiffré du lot] :
  - OSC A : Analog « BD Sine » [ASR ?], WT POS au maximum, WARP 1 **Bend +/−** **−32 %**, LEVEL **67**.
  - OSC B : « Basic MCB » [ASR ?], WT POS au maximum, **UNISON 3**, DETUNE **0,06**, WARP 1 **FM (A)** **39 %**, LEVEL **73**.
  - NOISE « J106 High Pass » [ASR ?], LEVEL **22**.
  - FILTER 1 **MG Low 18** sur A, B et NOISE, CUTOFF **469 Hz**, RES **22 %**, DRIVE **22 %**.
  - ENV 2 → CUTOFF **15** : ATK **25 ms**, DEC **1,79 s**, SUS **65 %**, REL **632 ms**.
  - ENV 3 → DRIVE de la Distortion **39**.
  - LFO 1 → FIN d'A, **≈ 20** ; LFO 2 → LEVEL.
- **Bend +/− à −32 %** [DÉDUCTION] : sur Bend +/−, 50 % est neutre (cartographie § 4.1) ; une valeur négative suppose un affichage bipolaire. Lire l'affichage avant de recopier.
- **ENV 1** : ATK **41 ms** (dit « release » par erreur [ASR ?]), DEC **1,76 s**, SUS **−5,7 dB**, REL **1,20 s** [SOURCE PA-05].
- **Valeurs de départ** [ORIGINAL, non chiffrées dans la vidéo] : ENV 3 0 / 0 / 800 ms / 0 / 300 ms ; LFO 1 à 0,3 Hz, FREE ; LFO 2 à 0,2 Hz, vers LEVEL de B ±10 %.
- **FX** [SOURCE PA-05] :
  1. Hyper/Dimension : MIX d'Hyper **16** [ASR ?], Dimension **9**, MIX **20**.
  2. Distortion **Diode 1**, filtre PRE (passe-haut probable), DRIVE **52 %**, MIX **34 %**.
  3. Equalizer : graves atténués et un creux (la vidéo suggère un LFO sur sa fréquence).
  4. Chorus ; Filter placé après la distorsion.
  5. Reverb **Hall**, MIX **61 %** : en insert, elle fait partie du son (règle 4).
- **Avant la reverb externe** : la vidéo coupe fort le grave avant une reverb externe (Respace, interprétation). Ici, High Pass à 150 Hz dans Serum.
- **Macros** : `Tone` CUTOFF 250 → 1200 Hz · `Motion` FM (A) de B 20 → 60 % · `Dirt` ENV 3 → DRIVE 0 → 60 · `Space` MIX de la Hall 30 → 70 %.
- **Jeu** : accords de quatre notes tenus une à deux mesures, MIDI 55 à 79. Voir la grille deep.
- **Test** : avec 61 % de Hall en insert, le pad occupe beaucoup d'espace ; à comparer avec la reverb sur un retour.

### PD02 Pad Juno
- **Patch** [SOURCE PA-01] :
  - OSC A : scie « Juno », **UNISON 5**. OSC B : copie de A, **+1 octave**.
  - LFO 1 → FIN (vibrato) et → LEVEL d'OSC B (trémolo), légers.
  - LFO 2 en mode ENVELOPE, décroissant sur **2 mesures** → RATE du LFO 1 : le mouvement ralentit pendant la note (règle 3).
  - FILTER 1 **Low 12** ; une enveloppe lente → CUTOFF ; une enveloppe plus courte → RES.
- **Aucune valeur chiffrée** n'est dite, à part l'unison : tout le reste est [ORIGINAL].
  - DETUNE 0,12 ; LFO 1 à 4 Hz → FIN ±5 cents, → LEVEL de B ±15 % ; LFO 2 de +100 % à 0 sur 2 bar, vers RATE du LFO 1 (+3 Hz au départ).
  - ENV 2 800 ms / 0 / 2 s / 40 % / 1 s → CUTOFF 30 % ; ENV 3 0 / 0 / 400 ms / 0 / 200 ms → RES 20 %.
- **ENV 1** : attaque douce, decay long [SOURCE PA-01] ; ici 400 ms / 0 / 3 s / −4 dB / 1,2 s.
- **FX** [SOURCE PA-01] : Equalizer en High Pass (150 Hz) → Chorus (LPF interne ouvert) → Delay court **avant** la Reverb → Reverb, DECAY baissé.
- **Durée** [CALCUL] : à 122 BPM, deux mesures durent 3,93 s.
- **Macros** : `Tone` CUTOFF 20 → 60 % · `Motion` LFO 1 → FIN 0 → ±12 cents · `Dirt` Distortion Tape Sat. 0 → 30 · `Space` MIX de la Reverb 10 → 40 %.
- **Jeu** : accords de septième, MIDI 55 à 76.
- **Test** : le vibrato qui ralentit doit s'entendre comme un instrument qui se pose ; s'il s'entend comme une fausse note, baisser la profondeur vers FIN.

### PD03 Pad aux dix astuces
- **Patch** [SOURCE PA-02] :
  1. ENV 1 : attaque à pente adoucie, DEC **≈ 2-2,5 s**, REL **≈ 360 ms**.
  2. FILTER 1 **MG Low 12**, ENV 1 → CUTOFF.
  3. OSC A et B désaccordés, **UNISON 5** chacun, B **+1 octave**.
  4. NOISE (« air can one » [ASR ?]), **one-shot**, suivi de hauteur, ≈ +24 demi-tons (interprétation), dans le filtre.
  5. LFO 1 (non synchronisé, lent, lissé) → FIN de B (négatif), → LEVEL de B, → LEVEL du NOISE.
  6. LFO 2 en mode ENVELOPE → RATE du LFO 1, quantité **≈ 20**, RATE du LFO 2 **≈ 2,5** (non synchronisé).
  7. SUB en **triangle, +2 octaves**, dans le filtre ; LFO 1 → LEVEL du SUB. À +2 octaves, il ne joue pas de grave (règle 1).
  8. Phaser, RATE très lent, MIX **≈ 25 %**.
  9. Chorus, MIX **≈ 40 %**, RATE baissé.
  10. Equalizer : coupe-bas **≈ 170 Hz**, Q baissé.
- **Hors de Serum** [SOURCE PA-02] : Ozone Imager, mono sous **180 Hz**, médiums resserrés, aigus élargis ; RC-20 en bonus. Ici : Ozone Imager 2 (inventaire) ; RC-20 non vérifié.
- **Valeurs de départ** [ORIGINAL] : ENV 1 300 ms / 0 / 2,2 s / −6 dB / 360 ms ; LFO 1 à 0,4 Hz, SMOOTH 50, vers FIN de B −6 cents ; DETUNE 0,1.
- **Macros** : `Tone` CUTOFF 20 → 60 % · `Motion` LFO 2 → RATE du LFO 1 0 → 40 · `Dirt` DRIVE du filtre 0 → 40 · `Space` MIX du Chorus 20 → 60 %.
- **Jeu** : accords de neuvième, MIDI 55 à 79.
- **Test** : la vidéo empile dix gestes ; les couper un par un et ne garder que ceux qui s'entendent.

### PD04 Pad afro à bruit pané
- **Patch** [SOURCE PA-03] :
  - OSC A : Basic Shapes, sinus, **UNISON 9**, DETUNE un peu baissé.
  - OSC B : « Basic Weird −1 » [ASR ?], **UNISON 12**, DETUNE baissé, WT POS vers une forme proche de la scie.
  - LFO 1 → WT POS de B, synchronisé à **une mesure** (oscillation lente).
  - NOISE « Inharm 5 » [ASR ?], LEVEL 0 ; ENV 2 → LEVEL du NOISE (attaque longue, release long).
  - LFO 2 triangle en BPM → **PAN du NOISE**, bipolaire.
  - FILTER 1 **MG Low 18** sur A, B et NOISE, CUTOFF bas, RES et DRIVE un peu montés ; Note# → CUTOFF, petite quantité.
- **ENV 1** : attaque longue avec courbe, SUS baissé, REL monté [SOURCE PA-03] ; ici 600 ms / 0 / 3 s / −8 dB / 1,5 s [ORIGINAL].
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1 bar → WT POS 20 % ; ENV 2 1,5 s / 0 / 2 s / 60 % / 2 s → LEVEL du NOISE 40 % ; LFO 2 en 2 bar → PAN ±40 ; CUTOFF 25 %.
- **FX** [SOURCE PA-03] : Compressor **Multiband** (release et gain montés, MIX bas) → Delay **1/8** des deux côtés, FEEDBACK **≈ 40** [ASR ?], MIX monté → Reverb (MIX et DECAY montés, LO CUT, SPIN et DEPTH montés) → Equalizer (coupe-bas presque total, Peak vers **700 Hz** en coupe, Q ≈ 59 [ASR ?]).
- **Delay** [CALCUL] : à 122 BPM, 1/8 = 245,9 ms.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` LFO 1 → WT POS 0 → 40 % · `Dirt` DRIVE du filtre 0 → 40 · `Space` MIX du Delay 10 → 40 %.
- **Jeu** : accords tenus, écoutés avec le sidechain comme dans la vidéo ; MIDI 57 à 79.
- **Test** : 9 + 12 voix par note font 84 voix sur un accord de quatre notes ; vérifier la charge.

### PD05 Pad rythmé par l'arpégiateur
- **Patch** [SOURCE PA-04, Serum 2] :
  - ARP en mode accord (« chord »), 1/16 (défaut).
  - OSC A : « Serum Analog Mother » [ASR ?], volume baissé.
  - FILTER 1 ladder (« MS ladder » [ASR ?] : **MG Ladder** probable, VAR = SMOOTH) sur A, CUTOFF tout en bas.
  - LFO 1 → CUTOFF, grille 3 [ASR ?], RATE **1/2**, forme dessinée.
  - LFO 2 en scie descendante, mode ENVELOPE, **1/16** → CUTOFF.
  - LFO 3 en BPM **1/2**, forme en marches (Shift-clic) → **OCT** d'OSC A, unipolaire, petite quantité.
  - RES et DRIVE montés, pas de SMOOTH.
  - Envois vers **BUS 1** et **BUS 2**.
- **BUS 2** [SOURCE PA-04] : Delay à 100 % humide, Ping-Pong, « 1/32 » [ASR ?], FEEDBACK monté, puis coupes à l'EQ.
- **BUS 1** [SOURCE PA-04] : **Convolve**, réponse d'usine « Weird › Moon reflection », MIX 100 %, IR GAIN baissé, EQ.
- **MAIN** [SOURCE PA-04] : Equalizer en coupe-bas → Distortion **Tube**, MIX bas → Reverb **Hall** (DECAY monté, LO CUT et HI CUT) → Equalizer (coupe-bas et Peak) → Compressor (gain).
- **Durées** [CALCUL] : à 122 BPM, 1/32 = 61,5 ms ; 1/2 = 983,6 ms.
- **Valeurs de départ** [ORIGINAL] : LFO 1 → CUTOFF 35 % ; LFO 2 → CUTOFF 30 % ; LFO 3 → OCT +1 sur une marche sur deux ; envois BUS 1 30 %, BUS 2 25 %.
- **ENV 1** : 2 ms / 0 / 600 ms / −6 dB / 300 ms [ORIGINAL] ; le rythme vient de l'ARP.
- **Macros** : `Tone` CUTOFF de repos 0 → 30 % · `Motion` LFO 3 → OCT 0 → 100 % · `Dirt` RES 20 → 60 % · `Space` niveau de BUS 1 0 → 100 %.
- **Jeu** : accords tenus d'une à deux mesures ; l'ARP les découpe en doubles croches.
- **Test** : le « shader » désactivé au début de la vidéo n'est pas dans la cartographie ; ignorer.

### PD06 Pad rythmé par LFO
- **Patch** [SOURCE PA-06] :
  - FILTER 1 sur A et B (type non dit).
  - OSC A : « Analog Saw Rounded » [ASR ?], WT POS **≈ 18**.
  - OSC B : même table, **+1 octave**, DETUNE d'unison **0,03**, WT POS **8**, LEVEL **50 %**.
  - LFO 1 → CUTOFF, RATE **1/16**, avec **RISE** (montée progressive).
  - LFO 2 → FIN d'A et B, **13** (vibrato).
  - LFO 3 → WT POS de B, RATE **1/2**.
  - PORTA **≈ 50-55 ms**.
- **ENV 1** : ATK **9 ms**, REL **≈ 350 ms** [SOURCE PA-06] ; ici 9 ms / 0 / 3 s / −2 dB / 350 ms.
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 25 % ; LFO 1 forme descendante, RETRIG, RISE 1 s, → CUTOFF 40 % ; UNISON de B 3.
- **Durée** [CALCUL] : à 124 BPM, 1/16 = 121,0 ms.
- **FX** [SOURCE PA-06] : coupes à l'EQ (High Pass 160 Hz) → Reverb.
- **Macros** : `Tone` CUTOFF 10 → 50 % · `Motion` LFO 1 → CUTOFF 0 → 60 % · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Reverb 10 → 40 %.
- **Jeu** : accords tenus, MIDI 57 à 79 ; le portamento ne joue que sur les voix qui changent, en POLY.
- **Test** : le RISE fait entrer la pulsation après l'attaque ; vérifier que le premier temps reste net.

### PD07 Pad analogique qui dérive
- **Patch** [SOURCE PA-07] :
  - FILTER 1 sur A, B, NOISE et SUB (type non dit), DRIVE **≈ 15 %**, RES **0 %**.
  - OSC A : Analog › Basic Shapes [ASR ?], WT POS **≈ 4**, PAN **10 à droite**, LEVEL **≈ 30 %**.
  - OSC B : **+1 octave**, PAN 10 à droite, LEVEL ≈ 30 %.
  - SUB en scie, PAN **−10**. Ici : SUB en scie à OCT 0 [ORIGINAL], pour rester au-dessus du High Pass (règle 1).
  - NOISE Analog › « White » [ASR ?].
  - ENV 2 → CUTOFF : ATK **900 ms**, REL **≈ 670 ms**.
  - Serum 1 : Chaos 1 → Master Tune **≈ 4**. Serum 2 : un LFO de **TYPE Chaos: Lorenz** → **Main Tuning**, quantité ≈ 4 (cartographie § 7.2 et § 13).
- **ENV 1** : ATK **≈ 500-570 ms** [ASR ? « 500 and 7D »], REL **≈ 960-970 ms** [SOURCE PA-07] ; ici 550 ms / 0 / 3 s / −3 dB / 965 ms.
- **FX** [SOURCE PA-07] : Chorus MIX **≈ 30 %** → Reverb SIZE **60 %**, MIX **≈ 36 %** (ou 30), HI CUT **50 %**, LO CUT **≈ 30 %** → Filter en FX, LFO → CUTOFF, RATE **une mesure**.
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 25 % ; ENV 2 → CUTOFF 35 % ; Filter FX MG Low 12, LFO 2 en 1 bar → CUTOFF ±15 %.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` Chaos → Main Tuning 0 → 8 · `Dirt` DRIVE 0 → 40 % · `Space` MIX de la Reverb 15 → 50 %.
- **Jeu** : accords tenus, MIDI 55 à 76 ; les panoramiques opposés font la largeur sans unison.
- **Test** : la dérive de hauteur doit rester sous le seuil où l'accord bat ; ≈ 4 est la valeur de la vidéo.

### PD08 Pad minimal à LFO de quatre mesures
- **Patch** [SOURCE PA-08 ; Serum 2 probable] :
  - Pad 1 : scie, UNISON 16 comparé à 7 (7 retenu, interprétation), DETUNE et BLEND ; Phaser qui transforme le son.
  - Pad 2 : « MB Saw » [ASR ?], UNISON et DETUNE ; une enveloppe lente (montée et chute) → CUTOFF ; un LFO de **4 mesures** → WT POS et WARP.
- **Recette** : le pad 2, avec le Phaser du pad 1 [DÉDUCTION].
- **Valeurs de départ** [ORIGINAL] : UNISON 7, DETUNE 0,15 ; ENV 2 1,5 s / 0 / 3 s / 30 % / 2 s → CUTOFF 30 % ; LFO 1 en 4 bar, FREE, triangle → WT POS 30 %, → WARP 1 (Bend +) 20 % ; Phaser MIX 30 %.
- **Durée** [CALCUL] : à 122 BPM, quatre mesures durent 7,87 s.
- **ENV 1** : attaque courte, decay et release plus longs [SOURCE PA-08] ; ici 20 ms / 0 / 4 s / −6 dB / 2 s.
- **FX** [SOURCE PA-08] : Phaser → Delay → Filter qui coupe les aigus → grande Reverb (SIZE et DECAY) → Equalizer (High Pass 150 Hz).
- **Hors de Serum** : la vidéo utilise Auto Pan comme ducking à la place d'un sidechain ; ici ShaperBox 3.
- **Macros** : `Tone` Filter FX 2 → 10 kHz · `Motion` LFO 1 → WT POS 0 → 60 % · `Dirt` DETUNE 0,05 → 0,3 · `Space` MIX de la Reverb 15 → 50 %.
- **Jeu** : accords dits dans la vidéo : do mineur (+ fa add11) et si bémol mineur 7 ; la grille minimal reprend ces accords avec un voicing écrit ici.
- **Test** : le LFO libre de quatre mesures ne repart pas au même point à chaque lecture ; HOST l'ancre au transport (cartographie § 7.2).

### PD09 Pad à trois vitesses
- **Traduction dans Serum 2** du patch A de la fiche (FabFilter Twin 3 et Pro-R 2, Attack Magazine) [FICHE pour les valeurs, ORIGINAL pour la traduction].
- **Patch** :
  - OSC A : sinus, **OCT +2**, LEVEL −12 dB. OSC B : sinus, **OCT 0**, −11 dB. OSC C : sinus, **OCT +1**, −8 dB.
  - SUB : sinus, **OCT −1**, LEVEL 0 au départ ; **ENV 3 → LEVEL du SUB**, ATK **15 s** : la couche n'arrive qu'après quinze secondes. Jouer au-dessus de MIDI 60 pour que le SUB sonne au-dessus de 130,8 Hz (règle 1).
  - WARP 1 **Sync** sur B et C ; LFO 1 en HZ, **13 Hz** → Sync de B et C (le grain).
  - WARP 1 Sync sur A ; LFO 2 en HZ, **0,5 Hz** → Sync d'A et → CUTOFF (la respiration).
  - **ENV 2, ATK 12 s** → RATE du LFO 1 : le grain accélère sur douze secondes.
  - FILTER 1 **MG Low 24** à **720 Hz** ; sortie de FILTER 1 vers FILTER 2 (chaînage série, cartographie § 5) ; FILTER 2 **High 24** à **280 Hz**.
- **ENV 1** : ATK **5 s**, DEC **1,5 s**, SUS **−3 dB**, REL **1 s** [FICHE].
- **FX** : Delay **Ping-Pong**, MIX **50 %**, FEEDBACK **70 %** → Reverb **Vintage**, MIX **100 %** [FICHE ; Pro-R 2 en mode Vintage dans l'original] → Equalizer, Low Shelf large à 280 Hz.
- **Durées** [CALCUL] : à 122 BPM, 15 s = 7,6 mesures ; à 126 BPM, 7,9 mesures. La couche du SUB arrive juste avant la huitième mesure.
- **Macros** : `Tone` CUTOFF de FILTER 1 400 → 1500 Hz · `Motion` LFO 1 → Sync 0 → 40 % · `Dirt` DRIVE de FILTER 1 0 → 40 · `Space` MIX du Delay 20 → 60 %.
- **Jeu** : un accord tenu au moins huit mesures, MIDI 60 à 84.
- **Test** : un pad qui change à 15 s change toujours au même endroit si la note démarre sur une mesure ; caler l'entrée du pad sur la frontière voulue.

### PD10 Pad à enveloppes opposées
- **Traduction dans Serum 2** du patch B de la fiche (u-he Hive 2) [FICHE pour l'architecture, ORIGINAL pour les valeurs].
- **Patch** :
  - OSC A : scie, **UNISON 8**, DETUNE 0,2 (detune 20 dans Hive). OSC B : scie, **UNISON 8**, DETUNE 0,1, **OCT +1, SEM +4** : l'écart de l'original (osc 1 à −2 octaves, osc 2 à −1 octave +4) [CALCUL : 16 demi-tons, une octave et une tierce majeure].
  - ENV 1 plate (0 / 0 / 0 / 0 dB / 1,5 s) ; **ENV 2 → LEVEL d'A** : ATK 5 ms, DEC 1,5 s, SUS 25 %, REL 1 s ; **ENV 3 → LEVEL de B** : ATK 3 s, DEC 1 s, SUS 100 %, REL 1,5 s. Le son change de composition pendant l'attaque sans qu'aucun filtre bouge [FICHE].
  - Velo → CUTOFF de FILTER 1 (MG Low 24, CUTOFF 40 %), 35 %.
  - LFO 3 en 6 marches (grille X 6, Shift-clic) → WT POS de B 25 % (le Shape Sequencer de Hive).
  - **LFO 1 + LFO 2 → PAN de B**, deux LFO de vitesses différentes (0,13 Hz et 0,31 Hz [ORIGINAL]) sommés : le mouvement stéréo ne se répète pas de façon reconnaissable [FICHE].
  - VOICING LEGATO (paraphonique sans MONO, cartographie § 9) [DÉDUCTION : le mode Legato de Hive].
- **FX** : Chorus MIX 30 % → Equalizer en High Pass à 200 Hz → Reverb Hall MIX 25 % [ORIGINAL].
- **Macros** : `Tone` CUTOFF 20 → 70 % · `Motion` ATK d'ENV 3 1 → 6 s · `Dirt` Distortion Soft Clip 0 → 25 · `Space` MIX de la Hall 10 → 40 %.
- **Jeu** : accords tenus deux mesures ou plus, MIDI 55 à 79.
- **Test** : LEGATO sans MONO rend ENV 2 et ENV 3 paraphoniques ; si les changements d'accords ne relancent pas les attaques, désactiver LEGATO.

### PD11 Pad désaccordé de quelques cents
- **Traduction dans Serum 2** du patch C de la fiche (Sylenth1) [FICHE pour les valeurs].
- **Patch** :
  - OSC A : scie, **UNISON 5**, **OCT −1**, désaccord **4,05 cents**, **PHASE 300°**.
  - OSC B : scie, **UNISON 7**, désaccord **3 cents**, **PHASE 100°**, MODE d'unison **Inv** (« Inv activé » dans Sylenth1, cartographie § 3.1).
  - LFO 1 → PHASE d'A : mouvement errant. LFO 2 → LEVEL, **1/4** synchronisé : un sidechain dans le synthé.
  - FILTER 1 Low 24 à **≈ 800 Hz**, RES 3, DRIVE 7 ; FILTER 2 High 12 à **60 Hz** (contrôle).
  - POLY 10.
- **Le désaccord** [CALCUL] : DETUNE va de 0 à 1 sur la course RANGE (2 demi-tons par défaut, soit 200 cents). 4 cents ≈ DETUNE 0,02 et 3 cents ≈ 0,015 si la course est linéaire ; elle ne l'est sans doute pas (MODE Linear, Super… changent la répartition) : régler en lisant l'affichage des cents, s'il existe, sinon à l'oreille.
- **ENV 1** : ATK court (A 3 dans Sylenth1), REL moyen (R 7) ; ici 30 ms / 0 / 0 / 0 dB / 700 ms [ORIGINAL].
- **FX** : Chorus : DELAY **16 ms**, RATE **0,22 Hz**, DEPTH à mi-course (50 % dans l'original ; DEPTH de Serum va de 0 à 26, donc 13), MIX **60 %** → Reverb, MIX **30 %** [FICHE].
- **Le chorus** [CALCUL] : 0,22 Hz = un cycle toutes les 4,5 s ; la fiche note qu'il élargit plus que le désaccord.
- **Macros** : `Tone` CUTOFF 500 → 1500 Hz · `Motion` LFO 1 → PHASE 0 → 50 % · `Dirt` DRIVE 0 → 30 · `Space` MIX du Chorus 30 → 80 %.
- **Jeu** : accords de neuvième, MIDI 55 à 79 ; LFO 2 en 1/4 joue déjà le rôle du sidechain : ne pas en ajouter un second.
- **Test** : la largeur vient du nombre de voix et de leur phase [FICHE] ; comparer en mono avec PD02.

### PD12 Pad liquid de 7e et 9e
- **Même vidéo qu'AC14** (PA-09 = CH-11). La recette complète, le voicing (triade, 7e, 9e) et la doublure des fondamentales sont dans `accords.md`, AC14. En pad :
  - ENV 1 avec une attaque lente : 600 ms / 0 / 3 s / −2 dB / 1,5 s [ORIGINAL].
  - LFO 1 → CUTOFF, 1/4 puis BPM désactivé [SOURCE PA-09] : à 0,4 Hz [ORIGINAL], le balayage ne bat plus avec le break.
  - Comparaison des formes d'onde dans la vidéo : la scie est préférée au sinus, au triangle et au carré.
- **Macros** : celles d'AC14.
- **Test** : en pad, la doublure de la fondamentale en bas pèse plus longtemps ; la couper si la basse joue.

### PD13 Pad Serum 2 à trois couches
- **Patch** [SOURCE PA-10, Serum 2] :
  - OSC A : tables S2 › Digital › « Chords » [ASR ? « code »], **OCT −4**. OSC B : même table, OCT −3 puis SEM −12, niveaux ajustés, UNISON sur B, DETUNE baissé.
  - OSC C : moteur **Granular**, sample (de la suite DNB Academy dans la vidéo ; ici un sample libre de droits), zone de lecture réduite, **boucle inversée**, octave haute, X-FADE, RANDOM, SCAN, DENSITY, PAN aléatoire.
  - FILTER 1 sur A et B, RES ; FILTER 2 sur C, RES.
  - NOISE **« Rain 100 High »** (nouveau dans Serum 2, dossier S2 Noises), LEVEL ajusté, pas en one-shot.
- **L'octave des tables d'accords** [DÉDUCTION] : OCT −4 sur une table nommée « Chords » laisse penser que la table contient déjà un accord, dans un registre haut. Lire la hauteur réelle au clavier avant de jouer des accords dessus (règle 1 d'`accords.md`).
- **ENV 1** : attaque longue, SUS haut, REL long [SOURCE PA-10] ; ici 1,2 s / 0 / 2 s / −1 dB / 2,5 s [ORIGINAL].
- **FX** [SOURCE PA-10] : **Convolve** → Chorus, MIX baissé → **Splitter L/H vers 300 Hz** (bande basse : légère distorsion ; bande haute : Delay et courbe), MIX baissé → Equalizer en coupe-bas.
- **Macros** [SOURCE PA-10, rangées ici] : `Tone` = MACRO 2 de la vidéo, CUTOFF de FILTER 1 + RES · `Motion` = MACRO 1 de la vidéo, CUTOFF de FILTER 2 (la couche granulaire) · `Dirt` DRIVE de la bande basse 0 → 40 · `Space` MIX du Convolve 10 → 50 %.
- **Jeu** : une note ou deux à la fois si la table contient un accord ; accords en MIDI sinon.
- **Test** : la couche granulaire inversée doit rester derrière ; si elle attire l'oreille, baisser son niveau avant `Motion`.

### PD14 Pad atmosphérique en sept points
- **Patch** [SOURCE PA-11, partie Serum 0:49-5:42] :
  1. Polyphonie au maximum, pour les accords étendus.
  2. Enveloppe d'ampli : attaque et release longs.
  3. Scie par défaut.
  4. Filtre passe-bas, **suivi au clavier**.
  5. ENV 2 → CUTOFF : attaque, decay et release très longs (balayage).
  6. RES montée.
  7. UNISON et DETUNE pour la largeur.
- **Valeurs de départ** [ORIGINAL] : POLY 16 ; ENV 1 2 s / 0 / 4 s / −2 dB / 3 s ; Low 24, CUTOFF 20 % ; ENV 2 3 s / 0 / 6 s / 30 % / 4 s → CUTOFF 40 % ; RES 25 % ; UNISON 4, DETUNE 0,1.
- **Hors de Serum** [SOURCE PA-11] : Delay de Live et FabFilter Pro-R. Ici : Delay interne de Serum et ValhallaVintageVerb sur un retour.
- **Idées en plus** [SOURCE PA-11] : un LFO sur le cutoff, un Phaser.
- **Durée** [CALCUL] : à 174 BPM, une mesure dure 1,38 s ; une attaque de 2 s s'étend sur une mesure et demie.
- **Macros** : `Tone` CUTOFF 10 → 45 % · `Motion` ATK d'ENV 2 1 → 6 s · `Dirt` RES 10 → 50 % · `Space` MIX du Delay 0 → 30 %.
- **Jeu** : progression m → m7 → m9 → m11 [SOURCE PA-11], une ou deux mesures chacune ; voir la grille DnB.
- **Test** : avec le suivi au clavier, les voix aiguës des accords étendus sont plus ouvertes ; vérifier que le m11 ne siffle pas.

### PD15 Pad liquid à trémolo
- **Patch** [SOURCE PA-12] :
  - Init, accord **mi mineur 7** ; SUB actif dans la vidéo, ici **éteint** (règle 1 de `leads.md`).
  - OSC A : sinus (interprétation [ASR « soundwave »]) ; OSC B pareil, **+1 octave** ; beaucoup d'unison sur les deux.
  - FILTER 1 **Low 24** sur tout, volume baissé.
  - LFO → CUTOFF, RATE **2 mesures** [ASR ? « toolbars »], forme lisse dessinée.
- **Valeurs de départ** [ORIGINAL] : UNISON 7, DETUNE 0,15 ; CUTOFF 30 % ; LFO 1 en 2 bar → CUTOFF ±20 %.
- **ENV 1** : 400 ms / 0 / 3 s / −2 dB / 1,5 s [ORIGINAL].
- **FX** [SOURCE PA-12] : Hyper/Dimension → Equalizer (Peak en hausse, Q baissé, fréquence modulée par une source non nommée ; second Peak qui monte les aigus) → Phaser, fréquence tout en bas → Chorus → Compressor **Multiband** (release et gain montés) → Reverb.
- **Trémolo** [SOURCE PA-12] : Auto Pan de Live (AMOUNT 100, PHASE 0, **1/16**, OFFSET 180, MIX baissé). Avec PHASE 0, les deux canaux bougent ensemble : c'est un trémolo, pas un panoramique [DÉDUCTION]. Ici : LFO 2 en 1/16, RETRIG → LEVEL de l'Utility interne, ou ShaperBox 3.
- **Durées** [CALCUL] : à 174 BPM, 2 mesures = 2,76 s ; 1/16 = 86,2 ms (11,6 Hz).
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` profondeur du trémolo 0 → 60 % · `Dirt` GAIN du Multiband 0 → 8 dB · `Space` MIX de la Reverb 10 → 40 %.
- **Jeu** : accords de septième tenus, MIDI 52 à 76.
- **Test** : un trémolo en 1/16 à 174 BPM approche de l'audio ; le doser bas, il doit faire vibrer, pas hacher.

### PD16 Pad liquid sombre
- **Patch** [SOURCE PA-13] :
  - Triade mineure (effet MIDI Chord de Live dans la vidéo ; ici l'accord écrit dans le clip).
  - OSC A : table **spectrale** « glassy », « Solid Phase 1 » [ASR ?], WT POS ajustée ; **UNISON 6**, DETUNE baissé.
  - OSC B : même table, **−1 octave**, unison.
  - SUB à −2 octaves en scie dans la vidéo : ici **éteint** (règle 1).
  - LFO 1 en mode **ENVELOPE**, **1/4**, forme du milieu vers le bas → **Main Tuning −12** (ou −5 / −9) : glissé de hauteur **vers le haut** à l'attaque.
- **Le glissé** [DÉDUCTION] : une forme qui part du milieu et descend, appliquée à −12, fait partir la note sous sa hauteur et y remonter en une noire ; −5 et −9 donnent une quarte ou une sixte de départ.
- **Durée** [CALCUL] : à 174 BPM, une noire dure 344,8 ms.
- **ENV 1** : une ATK [SOURCE PA-13] ; ici 300 ms / 0 / 3 s / −2 dB / 1,2 s [ORIGINAL].
- **FX** [SOURCE PA-13] : Hyper/Dimension (**RETRIG** actif, RATE et DETUNE baissés, MIX de Dimension monté) → Chorus (RATE lent, delay court, LPF ouvert, FEEDBACK et MIX montés) → Equalizer (Low Shelf ou coupe des graves, Low Pass résonant sur les aigus) → Reverb (MIX monté, LO CUT, SIZE et DECAY).
- **Macros** : `Tone` Low Pass de l'Equalizer 3 → 12 kHz · `Motion` LFO 1 → Main Tuning 0 → −12 · `Dirt` MIX de Dimension 20 → 60 % · `Space` MIX de la Reverb 15 → 45 %.
- **Jeu** : triades mineures tenues, MIDI 55 à 76.
- **Test** : le glissé à chaque accord doit rester un geste ; sur des accords rapprochés, le réduire à −5.

### PD17 Pad de sample figé
- **Patch** [SOURCE PA-14, Serum 2] :
  - OSC A : moteur **Spectral**, une boucle mélodique glissée dedans ; mode de boucle **Manual** : la tête de lecture devient un point X|Y, **SCAN** règle sa position, l'audio est figé (cartographie § 3.6).
  - Position calée sur un accord ; filtre spectral (FREQ LO) pour couper les graves trop forts.
  - OSC B : un second sample en Manual, même tonalité, aigus filtrés.
  - LFO 1 → position : **S&H**, lissé (SMOOTH), rapide, faible profondeur : effet granulaire.
  - Une enveloppe → position, de la fin vers le début, avec une enveloppe d'ampli qui retombe.
  - **Phase Lock** sur l'oscillateur : son plus net.
  - UNISON **3**, DETUNE baissé, **STACK 12** (une voix à +1 octave).
- **Variantes** [SOURCE PA-14] : S&H plus lent et plus fort ; forme dessinée sur la position ; LFO lent sur la position = une progression d'accords ; violoncelle et piano d'usine en Spectral ; trois samples empilés avec des LFO aléatoires pour le flutter.
- **Valeurs de départ** [ORIGINAL] : LFO 1 S&H à 8 Hz, SMOOTH 60, profondeur 3 % ; ENV 2 2 s / 0 / 4 s / 0 / 2 s → position −20 %.
- **ENV 1** : 1 s / 0 / 4 s / −4 dB / 2 s [ORIGINAL].
- **FX** [SOURCE PA-14] : Compressor → Delay → Reverb ; Equalizer en High Pass à 150 Hz.
- **Droits** : les samples de la vidéo viennent de packs tiers (song starter stacks) ; n'utiliser qu'un sample dont la licence est vérifiée, ou un son d'usine de Serum (règle 8 de `leads.md`).
- **Macros** : `Tone` FREQ LO du filtre spectral 100 → 600 Hz · `Motion` LFO 1 → position 0 → 10 % · `Dirt` Distortion Tape Sat. 0 → 30 · `Space` MIX de la Reverb 15 → 50 %.
- **Jeu** : une note tenue joue l'accord figé ; transposer au clavier change la hauteur de tout l'accord.
- **Test** : le genre n'est pas dit dans la vidéo (rattaché au dubstep par l'artiste seulement) ; tester dans un break.

### PD18 Pad d'accords future bass
- **Patch** [SOURCE PA-15] :
  - OSC A et B : « M saw » [ASR ?] ; OSC B : Digital « long Grease » [ASR ?], WT POS au maximum ou position 3, volume baissé (saturation).
  - Un oscillateur à **+1 octave** ; **UNISON 4** sur A, DETUNE et BLEND par défaut ; unison sur B.
  - SUB à −1 octave en triangle, en Direct Out dans la vidéo : ici **éteint**, ou sur une piste à part (règle 1).
  - NOISE « Attack Kick 13 » [ASR ?] : clic à l'attaque.
  - FILTER 1 **German LP** sur A et B, un peu de DRIVE, CUTOFF bas, RES montée ; MACRO « Cutoff » → CUTOFF.
  - LFO 1 dessiné (montée lisse), RATE **1/4 triolet** [ASR ?], mode **ENVELOPE** → LEVEL d'OSC A en **négatif** : le « wawa ».
  - ENV 2 → MIX de la Reverb : **DELAY 800 ms** (le paramètre DELAY d'ENV, cartographie § 7.1), DEC monté, **SUS 100 %** : la reverb ne s'ouvre qu'après 800 ms.
- **Durée** [CALCUL] : à 150 BPM, 1/4 triolet = 266,7 ms ; 800 ms = deux temps.
- **ENV 1** : 10 ms / 0 / 3 s / −2 dB / 600 ms [ORIGINAL].
- **FX** [SOURCE PA-15] : Chorus (MIX baissé) → Reverb → Compressor → Equalizer (High Shelf monté) ; coupe-bas dans Live, ici Equalizer en High Pass à 180 Hz.
- **Macros** : `Tone` = MACRO « Cutoff » de la vidéo, CUTOFF 10 → 60 % · `Motion` LFO 1 → LEVEL d'A 0 → −80 % · `Dirt` DRIVE 0 → 40 · `Space` ENV 2 → MIX de la Reverb 0 → 50 %.
- **Jeu** : accords de quatre notes tenus une mesure, MIDI 57 à 79.
- **Test** : le clic d'attaque et le kick tombent ensemble sur le premier temps ; vérifier qu'ils ne se doublent pas.

### PD19 Pad de drop melodic dubstep
- **Le corpus n'a aucun pad melodic dubstep fait dans Serum** (section « Manque »). Recette **[DÉDUCTION]** qui réunit la couche legato au filtre Reverb (HK16), le mur propre (AC18) et la reverb retardée de PD18.
- **Patch** :
  - OSC A : scie, UNISON 3, DETUNE 0,05. OSC B : scie, OCT +1, UNISON 7, DETUNE 0,15, LEVEL 60 %. OSC C : sinus, OCT 0, LEVEL 40 %.
  - FILTER 1 **Reverb** (Misc) sur A et B, CUTOFF 50 %, suivi au clavier, MIX 60 %.
  - FILTER 2 **MG Low 24** sur C, CUTOFF 40 %.
  - ENV 2 → MIX d'une Reverb Hall : DELAY 1 temps, DEC 2 s, SUS 100 %.
  - POLY 8.
- **Le retard** [CALCUL] : à 150 BPM, un temps = 400 ms ; à 140 BPM, 428,6 ms.
- **ENV 1** : 150 ms / 0 / 4 s / −1 dB / 1,5 s.
- **FX** : Hyper/Dimension (Dimension MIX 40 %) → Compressor Multiband MIX 30 % → Equalizer en High Pass à 200 Hz → Reverb Hall, SIZE 70, MIX piloté par ENV 2.
- **Macros** : `Tone` CUTOFF du filtre Reverb 30 → 70 % · `Motion` DETUNE de B 0,05 → 0,3 · `Dirt` GAIN du Multiband 0 → 8 dB · `Space` ENV 2 → MIX de la Hall 0 → 50 %.
- **Jeu** : accords larges tenus une ou deux mesures sous le hook (HK14 à HK17), MIDI 55 à 84.
- **Test** : sans source vidéo ; avec le mur d'AC17 et AC18, un seul des deux doit être large.

### PD20 Pad qui est sa reverb
- **Recette [DÉDUCTION]** sur la distinction de la fiche : une reverb en insert à MIX 100 % n'a plus de son sec, elle **est** le son [FICHE].
- **Patch** :
  - OSC A : Basic Shapes, scie, UNISON 3. OSC B : sinus, OCT +1, LEVEL 40 %.
  - FILTER 1 MG Low 12, CUTOFF 35 %.
  - ENV 1 : 5 ms / 0 / 300 ms / 0 / 200 ms : un pluck court qui nourrit la reverb.
- **FX** : Equalizer en High Pass à 250 Hz (avant la reverb, pour ne pas la remplir de grave [FICHE]) → Reverb **Hall**, SIZE 90, DECAY long, **MIX 100 %** → Equalizer (Low Pass à 6 kHz) → Compressor Single 3:1, pour tenir la queue.
- **Resampling** : imprimer le pad (`../../../resampling/SKILL.md`), puis le traiter en audio : inversion, étirement, découpe sur la grille. L'insert à 100 % est fait pour être resamplé [FICHE].
- **Macros** : `Tone` Low Pass 2 → 12 kHz · `Motion` DECAY de la Hall · `Dirt` Distortion Soft Clip avant la Hall 0 → 30 · `Space` SIZE de la Hall 40 → 100.
- **Jeu** : notes ou accords courts, espacés ; la queue fait le pad.
- **Test** : aucune source vidéo ; c'est un procédé, à juger sur la prise imprimée.

## Motifs de départ (grilles vérifiées)

Numérotation de Live (C3 = 60). Voicings écrits ici ; la basse tient la fondamentale. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/synths/pads.md`. Notation Producer Pal : `--fichier references/synths/pads.md --titre <titre> --format ppal`.

```grille
titre: Deep house 122 — pad chiffré (PD01)
tempo: 122
accords: Cm9 | Abmaj7
haut: D5[1:16] | C5[1:16]
milieu: Bb4[1:16] | G4[1:16]
bas: Eb4[1:16] | Eb4[1:16]
```

```grille
titre: Minimal 122 — pad de quatre mesures (PD08)
tempo: 122
accords: Cm | Bbm7
haut: G4[1:16] | F4[1:16]
milieu: Eb4[1:16] | Db4[1:16]
bas: C4[1:16] | Bb3[1:16]
```

```grille
titre: DnB atmosphérique 174 — m, m7, m9, m11 (PD14)
tempo: 174
accords: Am | Am7 | Am9 | Am11
haut: E4[1:16] | G4[1:16] | B4[1:16] | D5[1:16]
milieu: C4[1:16] | E4[1:16] | G4[1:16] | B4[1:16]
bas: A3[1:16] | C4[1:16] | E4[1:16] | G4[1:16]
```

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : « BD Sine », « Basic MCB », « J106 High Pass », « Basic Weird −1 », « Inharm 5 », « Serum Analog Mother », « Analog Saw Rounded », « MB Saw », « Chords », « Solid Phase 1 », « M saw », « long Grease », « Attack Kick 13 » (beaucoup marqués [ASR]) ; la réponse « Weird › Moon reflection » de Convolve ; le bruit « Rain 100 High ».
- Lire l'affichage du Bend +/− de PD01 et le désaccord en cents de PD11.
- Écouter chaque recette (règle 10 de `leads.md`) avec le lead et les accords du morceau, en mono pour le pad le plus large ; consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
- Dernier fichier du lot : drones.
