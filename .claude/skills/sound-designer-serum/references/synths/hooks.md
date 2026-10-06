# Vingt recettes de hooks dans Serum 2

Troisième fichier du lot de synthés : le son qui porte le riff du drop ou le thème d'intro. Rédigé le 05/10/2026. Sources :
- l'étude des quinze tutoriels de hooks, HO-01 à HO-15, de `../tutoriels-synths-serum.md`, et sa synthèse `../synths-serum-synthese.md` (section Hook) ;
- la cartographie de Serum 2 (`../serum2-cartographie.md`) et `../serum2-fx-clip-arp.md`.

Ce fichier donne le **timbre**. La cellule et les notes du hook s'écrivent avec `../../../composer-hooks-funk-electro/SKILL.md` ; les cuivres de type « horn » se comparent à `../../../studio-grade-brass-sound-design/SKILL.md`.

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes : **[SOURCE HO-nn]**, **[CALCUL]**, **[DÉDUCTION]**, **[ORIGINAL]**, comme dans `leads.md`.

## Règles

Les dix règles communes au lot sont dans `leads.md`. Ce qui s'ajoute pour les hooks :

1. **Le hook est souvent médium-grave.** Plusieurs hooks de drop (horn de tech house, riff jump-up) vivent entre 100 et 400 Hz. Le High Pass final descend alors à 90-120 Hz, jamais plus bas ; sous cette limite, c'est le sub, sur sa piste. Chaque fiche donne la fréquence de la note la plus grave jouée.
2. **Deux oscillateurs à un intervalle font un accord de deux notes** (HO-05, HO-06, HO-08). Chaque fiche calcule les notes réellement entendues pour une note jouée, pour vérifier qu'elles s'accordent avec l'harmonie du morceau.
3. **Le caractère vient d'un warp modulé** (Sync ou FM) par une enveloppe ou un LFO en mode ENVELOPE. La macro `Motion` porte cette profondeur.
4. **Distorsion forte, puis élargissement** : Hyper/Dimension se place après la distorsion (HO-03) ; sinon la distorsion écrase la largeur.
5. **Droits** : sept tutoriels recréent un titre publié (HO-01, HO-02, HO-04, HO-08, HO-09, HO-10, HO-11). Seul le timbre est repris ; les cellules des grilles sont écrites ici. Les presets de packs (HO-01) ne s'utilisent qu'avec une licence vérifiée.
6. **Référence A/B du fichier** : HK01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| HK01 | Horn par LFO de niveau | Tech house, référence A/B | deux unisons à 7 voix, LFO « double aileron » sur les niveaux, MG Low 12 FAT 92 % |
| HK02 | Horn par FM et Sync | Tech house | deux tables analogiques, FM (B) et Sync, LFO ENVELOPE en 1/4, éclaircissement sur la mesure |
| HK03 | Screech suivi au clavier | Bass house | triangle en FM d'un carré, Low 12 résonant suivi au clavier, Tube |
| HK04 | Sync funky | Tech house brésilienne, nu-disco | carré et scie à OCT −1, ENV 2 sur le Sync, mono |
| HK05 | Rave stab en quatre clés | House rave, UK rave | deux oscillateurs à un intervalle, phase fixe, pitch sur une mesure, Low 18 |
| HK06 | Hook à deux voix en quinte | Tech house | A et B à une quinte, mono legato, Dimension sans Hyper |
| HK07 | Hook qui part d'une octave en dessous | Tech house groovy | scies douces, LFO 1/64 sur FIN, départ à −12 |
| HK08 | Scie et carré écrasés | Tech house | scie à −19 st, carré à +12 st, Asym au maximum |
| HK09 | Hook parlant | Bass house | filtre Formant balayé par une enveloppe |
| HK10 | « Wow » à filtres croisés | DnB dancefloor | Multi BN dont les deux fréquences se croisent, LFO sur CRS |
| HK11 | Stab FM à harmoniques dessinées | DnB dancefloor | sinus en FM d'une table dessinée, LFO de transitoire, couche de percussion |
| HK12 | Hook d'intro qui retombe | DnB, intro | unison 14 étalé, filtre Reverb suivi au clavier, LFO de 2 mesures sur Main Tuning |
| HK13 | Riff jump-up | DnB jump-up 175 | scie en Sync, LFO RETRIG sur MG Low 12, Diode 1 PRE |
| HK14 | Lead principal sec | Melodic dubstep, première couche | scie unison 3, sans reverb, devant |
| HK15 | Couche pluck réverbérée | Melodic dubstep, deuxième couche | BS2 Filthy, ENV 1 très courte, reverb |
| HK16 | Couche legato au filtre Reverb | Melodic dubstep, troisième couche | sustain au maximum, filtre Reverb, Hyper/Dimension |
| HK17 | Couche en Ring Mod | Melodic dubstep, quatrième couche | copie de HK16, MS Saw, Ring Modx2 |
| HK18 | Spirit lead | Melodic dubstep, future bass | carré Low 24, NOISE qui module la hauteur, vibratos sur macro |
| HK19 | Sync lent | Melodic dubstep | Sync poussé, LFO très lent, glide |
| HK20 | Hook doux à deux voix | Signature sous 124, électro chill | sinus et triangle à la tierce, attaque de bruit discrète |

## Les vingt recettes

### HK01 Horn par LFO de niveau — référence du fichier
- **Patch** [SOURCE HO-01] :
  - OSC A : init, **UNISON 7**, DETUNE **≈ 0,08**, PHASE identique, **RAND au maximum**, **LEVEL 0** (ouvert par le LFO).
  - OSC B : init, **UNISON 7**, DETUNE **≈ 0,41**, RAND au maximum, LEVEL baissé ; octave relevée, FIN **−15** [ASR ? sur la suite].
  - NOISE « Bright White » [ASR ?], LEVEL **35**.
  - LFO 1 dessiné en **« double aileron »** (deux bosses à attaque raide) → LEVEL d'A, de B et du NOISE (≈ au maximum chacun). LFO 1 passé en mode **ENVELOPE**.
  - FILTER 1 **MG Low 12**, CUTOFF **≈ 40 Hz**, RES 0, DRIVE **≈ 30 %**, **FAT 92 %**, MIX au maximum ; LFO 1 → CUTOFF.
  - LFO 1 → FIN aussi, bipolaire, **≈ 37** : le son rebondit.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1/4, deux bosses par cycle ; LFO 1 → CUTOFF 55 % ; OSC B OCT +1.
- **ENV 1** : 2 ms / 0 / 400 ms / −3 dB / 120 ms [ORIGINAL].
- **FX** [SOURCE HO-01] :
  1. Equalizer : bande basse en **Peak à 155 Hz**, Q ≈ 35 %, **+8,1 dB** (« petite bosse dans le médium ») ; bande haute en Peak à **2939 Hz**, Q 46 %, **+1,7 dB**.
  2. Filter **MG Low 6**, CUTOFF **714 Hz**, RES, DRIVE et FAT à 0.
- **Hors de Serum** [SOURCE HO-01] : deux OTT, deux EQ (creux vers **310 Hz**, « là où est la boue »), deux Auto Filter et un delay automatisés. Ici [DÉDUCTION] : Compressor **Multiband** interne pour chaque OTT (bandes moyenne et haute montées, MIX 55 % puis 43 %) ; le creux à 310 Hz et le coupe-bas dans Pro-Q 4 ; les deux Auto Filter de la vidéo deviennent le Filter interne automatisé par `Tone`.
- **Règle 1** : la bosse de 155 Hz est le corps du horn. High Pass à **110 Hz** seulement, dans Pro-Q 4. La basse du morceau de référence est une guitare et un sub, d'après la vidéo : ici, le sub sur sa piste.
- **Macros** : `Tone` CUTOFF du Filter MG Low 6 400 → 2000 Hz · `Motion` LFO 1 → CUTOFF 30 → 80 % · `Dirt` GAIN de la bosse à 155 Hz 0 → +9 dB · `Space` MIX d'un Delay 1/8 pointée 0 → 20 %.
- **Jeu** : MIDI 55 à 70 ; la note la plus grave (55) sonne à 196 Hz, une octave plus haut pour OSC B [CALCUL].
- **Test** : le son doit « parler » à chaque note ; si la double bosse du LFO tombe à contretemps de la cellule, raccourcir ou allonger le cycle.

### HK02 Horn par FM et Sync
- **Patch** [SOURCE HO-02] :
  - OSC A : table analogique « BS Subies » [ASR ?] ; OSC B : « BS Filthy ». UNISON **8** sur A, **6** sur B ; DETUNE baissé ; LEVEL de B baissé.
  - OSC A : WARP 1 **FM (B)** et WARP 2 **Sync**, « juste un peu ».
  - FILTER 1 sur A et B, **MG Low 6**, DRIVE monté, RES baissée, un peu de FAT, CUTOFF bas ; ENV 1 → CUTOFF.
  - LFO 1 en mode **ENVELOPE**, RATE **1/4** ; ENV 1 → WT POS en négatif ; LFO 1 → WT POS et → FM (B) : du grain au début de chaque note.
  - LFO 2 en mode ENVELOPE, RATE d'une mesure → CUTOFF : le son s'éclaircit pendant la tenue.
- **ENV 1** : attaque lente « comme un cor », plus du release [SOURCE HO-02] ; ici 60 ms / 0 / 1 s / −4 dB / 250 ms [ORIGINAL].
- **Valeurs de départ** [ORIGINAL] : FM (B) 20 %, Sync 10 % ; LFO 1 → FM (B) +25 %, → WT POS +20 % ; LFO 2 → CUTOFF +35 %.
- **Durées** [CALCUL] : à 124 BPM, le LFO 1 en 1/4 dure 484 ms et le LFO 2 en une mesure 1,94 s ; à 126 BPM, 476 ms et 1,90 s.
- **FX** [SOURCE HO-02] : Distortion (DRIVE monté) → Chorus (LPF du chorus coupé, DEPTH un peu baissée) → Reverb avec LO CUT → Equalizer en coupe-bas.
- **Hors de Serum** : la vidéo met Utility (graves en mono), la Pedal de Live en Overdrive et EQ Eight. Ici : Utility toléré pour le mono ; la Pedal devient une seconde Distortion interne en **Stomp Box** ; l'EQ anti-brillance dans Pro-Q 4.
- **Macros** : `Tone` CUTOFF 10 → 50 % · `Motion` LFO 1 → FM (B) 0 → 50 % · `Dirt` DRIVE de la Stomp Box 20 → 80 · `Space` MIX de la Reverb 0 → 20 %.
- **Jeu** : MIDI 55 à 70, notes de un à deux temps pour laisser l'éclaircissement se faire.
- **Test** : comparer avec HK01 à niveau égal ; c'est le même horn par une autre voie.

### HK03 Screech suivi au clavier
- **Patch** [SOURCE HO-03] :
  - OSC A : Basic Shapes, **triangle** ; WARP 1 **FM (B)**.
  - OSC B : Basic Shapes, **carré**, LEVEL **≈ 37 %**.
  - Modulation d'amplitude dessinée : LFO 1 en **RETRIG** (« Trigger »), RATE **1/2** → LEVEL (interprétation de l'étude).
  - FILTER 1 **Low 12**, **RES haute** (tons stridents), **suivi au clavier** (icône piano), CUTOFF accordé à l'oreille.
- **Valeurs de départ** [ORIGINAL] : FM (B) 40 % ; RES 75 % ; CUTOFF réglé pour que la résonance tombe sur l'octave ou la quinte de la note ; LFO 1 → LEVEL d'A −50 %.
- **ENV 1** : 0 ms / 0 / 600 ms / −2 dB / 80 ms [ORIGINAL] ; VOICING MONO.
- **FX** [SOURCE HO-03] : Distortion **Tube** (sans elle, la résonance ne ressort pas) → Hyper/Dimension **après** la distorsion : Hyper **≈ 9 %**, Dimension SIZE **≈ 2 %**, MIX 68 puis **46** → Reverb, MIX bas.
- **Accord de la résonance** [CALCUL] : avec le suivi au clavier, la résonance garde le même intervalle avec chaque note. Pour la placer sur l'octave, le CUTOFF doit valoir deux fois la fréquence de la note de réglage ; pour la quinte de l'octave, trois fois.
- **Macros** : `Tone` CUTOFF ± une quinte autour du réglage · `Motion` FM (B) 20 → 70 % · `Dirt` DRIVE du Tube 30 → 90 · `Space` MIX de la Dimension 20 → 60 %.
- **Jeu** : riff principal du drop, MIDI 57 à 72 ; la vidéo l'appelle « main bass » : c'est un riff médium, avec un sub sur sa piste (règle 1).
- **Test** : variantes de la vidéo, Sync à la place de la FM, autres formes d'onde ; comparer à niveau égal.

### HK04 Sync funky
- **Patch** [SOURCE HO-04, Serum 2] :
  - VOICING **MONO**.
  - OSC A : carré, **OCT −1** ; WARP 1 **Sync**. Le fader **WARP Var** sous le menu lisse les bords (moins = plus agressif) [DÉDUCTION : cartographie § 4.1].
  - OSC B : scie, OCT −1, FIN légèrement décalé ; WARP 1 Sync ; niveaux différents.
  - ENV 2 → Sync d'A **27 %**, → Sync de B **15 %** ; « fondu du warp » désactivé ; DEC d'ENV 2 long.
- **ENV 1** : REL **≈ 7 ms** [SOURCE HO-04] ; ici 0 ms / 0 / 1 s / −2 dB / 7 ms.
- **Valeurs de départ** [ORIGINAL] : ENV 2 0 / 0 / 700 ms / 0 / 100 ms ; FIN de B +8 cents.
- **FX** [SOURCE HO-04] : Chorus, MIX **≈ 20 %** ; Reverb **≈ 5 %**. Pour un style électro des années 80 : plus de Chorus, de Flanger ou de Phaser.
- **Hors de Serum** [SOURCE HO-04] : un Utility en panoramique automatique **avant** la reverb (sinon la reverb est aussi pannée), puis Kickstart. Ici : la reverb sur un retour, le panoramique par un LFO interne sur le PAN de l'Utility interne de Serum, ou par l'Utility natif toléré ; ShaperBox 3 pour le sidechain.
- **Macros** : `Tone` WARP Var 0 → 100 % · `Motion` ENV 2 → Sync d'A 10 → 45 % · `Dirt` Distortion Soft Clip 0 → 40 · `Space` MIX du Chorus 10 → 40 %.
- **Jeu** : MIDI 60 à 72 (sonne une octave plus bas, 130,8 à 261,6 Hz [CALCUL]), notes courtes et staccato.
- **Test** : un release de 7 ms coupe net ; écouter qu'il ne claque pas sur les notes graves.

### HK05 Rave stab en quatre clés
- **Patch** [SOURCE HO-05, en français] :
  - **Clé 1, l'accord** : un second oscillateur ; son écart avec la note racine, essayé à **−2 ou +10** demi-tons, se choisit selon la basse.
  - Tables : celles du Juno (carré Juno, DCO), au goût. **RAND à 0** : même son à chaque note, comme un sample ; un peu d'unison pour la stéréo, en compromis.
  - **Clé 2, la hauteur** : DETUNE indépendant par oscillateur, puis une enveloppe → **Main Tuning**, plage **12** (une octave), en mode **une mesure** (elle agit sur la note longue de fin de motif), bipolaire, léger mouvement au début ; attaque un peu adoucie.
  - **Clé 3, le bruit** : NOISE, « indispensable pour le côté old school ».
  - **Clé 4, le filtre** : **Low 18**, enveloppe percussive → CUTOFF ; limer la fondamentale dans le filtre plutôt qu'avec un EQ.
- **L'intervalle** [CALCUL] : −2 et +10 demi-tons donnent la même note à l'octave près, la septième mineure de la racine (un do joué ajoute un si bémol). Le stab sonne donc une racine et sa septième mineure : il colle à un accord de septième de dominante ou mineur 7, pas à un accord majeur 7.
- **Valeurs de départ** [ORIGINAL] : ENV 3 en BPM, ATK 1/64, DEC 1 mesure, SUS 0, vers Main Tuning ±12 (quantité faible, −2 demi-tons au départ) ; ENV 2 0 / 0 / 180 ms / 0 / 80 ms vers CUTOFF 45 % ; NOISE LEVEL 25 %.
- **ENV 1** : 0 ms / 0 / 400 ms / −8 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE HO-05] : Distortion → Filter qui coupe les aigus (côté grunge, vintage) → Flanger pour colorer → petit Equalizer.
- **Macros** : `Tone` CUTOFF 20 → 60 % · `Motion` ENV 3 → Main Tuning 0 → −12 · `Dirt` DRIVE 10 → 60 · `Space` MIX du Flanger 0 → 40 %.
- **Jeu** : motif de stabs en doubles croches, la dernière note longue ; MIDI 60 à 72.
- **Test** : la vidéo met un sidechain au gain dès le départ, pour juger le stab dans son contexte ; faire de même avant de régler le filtre.

### HK06 Hook à deux voix en quinte
- **Patch** [SOURCE HO-06] :
  - OSC A **OCT −2** ; OSC B **OCT −1**, SEM **−5** (« ajouter une septième » dit à l'oral, incohérent avec le réglage).
  - FILTER 1 sur A et B, une enveloppe → CUTOFF, enveloppe façonnée, release ; VOICING **MONO + LEGATO** ; un peu plus de RES.
- **L'intervalle** [CALCUL] : A sonne à −24 demi-tons, B à −17. B est donc **une quinte au-dessus de A** : le patch sonne la racine et sa quinte, deux octaves sous la note jouée pour A.
- **Registre** [ORIGINAL, règle 1] : OCT −2 placerait A sous 100 Hz pour la plupart des notes. Ici A en OCT −1 et B en OCT 0, SEM −5 : même quinte, une octave plus haut.
- **Valeurs de départ** [ORIGINAL] : MG Low 18, CUTOFF 25 %, RES 25 % ; ENV 2 5 ms / 0 / 350 ms / 15 % / 200 ms vers CUTOFF 40 %.
- **ENV 1** : 2 ms / 0 / 600 ms / −4 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE HO-06] : **Dimension seule**, Hyper coupé (« sinon digital ») → Equalizer (aigus coupés ; les graves boostés de la vidéo deviennent un High Pass à 110 Hz, règle 1) → Delay **Ping-Pong** (« 18 » [ASR ?]) → Reverb **Plate** élargie.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` ENV 2 → CUTOFF 20 → 60 % · `Dirt` DRIVE du filtre 0 → 50 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : MIDI 57 à 72, cellule courte et liée ; la note jouée sonne une octave plus bas (A) et une quarte plus bas (B) [CALCUL].
- **Test** : le synthé d'origine serait un Roland (dit dans la vidéo) ; on ne cherche que la couleur.

### HK07 Hook qui part d'une octave en dessous
- **Patch** [SOURCE HO-07, Serum 2] :
  - Un oscillateur une octave plus bas en scie (le SUB dans la vidéo) : ici **éteint** (règle 1 de `leads.md`).
  - OSC A : scie « plus douce », UNISON **2** ; OSC B : scie (« 80 mother » [ASR ?]) ; NOISE actif.
  - FILTER 1 sur A, B et C, CUTOFF ouvert, DRIVE.
  - LFO 2 → FIN d'OSC A, RATE **1/64** : modulation rapide.
  - LFO 1 → **Main Tuning** (matrice) ; la hauteur part de **−12 demi-tons**.
  - VOICING MONO, un peu de REL.
- **Le 1/64** [CALCUL] : à 126 BPM, 1/64 = 29,8 ms, soit 33,6 Hz : plus un grain qu'un vibrato.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en mode ENVELOPE, 1/8, rampe montante de −12 à 0 ; LFO 2 → FIN ±5 cents.
- **ENV 1** : 2 ms / 0 / 500 ms / −3 dB / 120 ms [ORIGINAL].
- **FX** [SOURCE HO-07] : Equalizer en coupe-bas (110 Hz, règle 1) → Compressor **Multiband** → Delay → Reverb.
- **Macros** : `Tone` CUTOFF 40 → 90 % · `Motion` profondeur de LFO 1 (−12 → 0 demi-ton) · `Dirt` DRIVE 10 → 50 · `Space` MIX de la Reverb 0 → 20 %.
- **Jeu** : MIDI 60 à 72, notes détachées ; chaque note monte d'une octave en une croche.
- **Test** : une glissade d'une octave sur chaque note lasse vite ; réduire `Motion` sur les notes répétées.

### HK08 Scie et carré écrasés
- **Patch** [SOURCE HO-08] :
  - OSC A : Basic Shapes, scie, **OCT −1, SEM −7**. OSC B : Basic Shapes analogique, carré, **OCT +1**.
- **Les notes entendues** [CALCUL] : A sonne 19 demi-tons sous la note jouée, B 12 au-dessus. Joué MIDI 72 (C4), le patch donne MIDI 53 (F2) et 84 (C5) : la note jouée est la quinte de la note grave. Le hook sonne donc en quintes ouvertes, un registre écarté de deux octaves et demie.
- **Registre** [CALCUL, règle 1] : la note grave d'A ne descend sous 110 Hz qu'en dessous de MIDI 64 (jouée) ; jouer de 64 à 76.
- **ENV 1** : 0 ms / 0 / 500 ms / −4 dB / 100 ms [ORIGINAL].
- **FX** [SOURCE HO-08] : Distortion **Asym**, **DRIVE au maximum** → Equalizer qui coupe les graves → Compressor **Multiband** → Reverb repoussée, « très mono ».
- **Hors de Serum** : iZotope Trash (preset « Crunchy Taco ») dans la vidéo, présence sur le Mac non vérifiée ; ici RazorClip, puis un EQ qui arrondit les aigus dans Pro-Q 4.
- **Macros** : `Tone` Equalizer, bande haute en Low Pass 3 → 12 kHz · `Motion` LEVEL de B 30 → 100 % · `Dirt` MIX de l'Asym 50 → 100 % · `Space` MIX de la Reverb 0 → 15 %.
- **Jeu** : cellule de trois à cinq notes répétée, MIDI 64 à 76.
- **Test** : les quintes ouvertes s'accordent avec tous les accords qui contiennent cette quinte ; vérifier sur la progression du morceau.

### HK09 Hook parlant
- **Aucun tutoriel du corpus** ne fait un hook à voyelles ; recette **[ORIGINAL]** sur les filtres de Serum 2 (cartographie § 6 : Formant-I/II/III, CUTOFF qui morphe entre formants, VAR = FORMNT).
- **Patch** :
  - OSC A : Basic Shapes, scie, UNISON 3, DETUNE 0,06, RAND 0.
  - OSC B : Basic Shapes, carré, SEM +12, LEVEL 40 %.
  - FILTER 1 **Formant-II** sur A et B, CUTOFF 20 %, VAR (FORMNT) 50 %, DRIVE 30.
  - ENV 2 → CUTOFF 50 % : 10 ms / 0 / 250 ms / 20 % / 150 ms : la voyelle passe d'un « o » à un « a » (à vérifier à l'oreille, l'ordre des voyelles n'est pas documenté).
  - VOICING MONO, PORTA 30 ms.
- **ENV 1** : 2 ms / 0 / 400 ms / −4 dB / 100 ms.
- **FX** : Distortion **Diode 2**, DRIVE 40, MIX 60 % → Compressor Multiband, MIX 40 % → Equalizer en High Pass à 120 Hz.
- **Macros** : `Tone` VAR (FORMNT) 20 → 80 % · `Motion` ENV 2 → CUTOFF 20 → 80 % · `Dirt` DRIVE de la Diode 2 20 → 80 · `Space` Delay 1/16, MIX 0 → 20 %.
- **Jeu** : MIDI 55 à 67, cellules rapides de deux à quatre notes.
- **Test** : sans source vidéo ; comparer à HK03 à niveau égal avant de le garder.

### HK10 « Wow » à filtres croisés
- **Patch** [SOURCE HO-09] :
  - OSC A et OSC B : Basic Shapes, scie (versions numériques, les plus riches). NOISE « AC Hum » à bas niveau, pour la chaleur.
  - A et B légèrement différents, l'un pané à gauche, l'autre à droite ; UNISON **16** sur A, **8** sur B ; DETUNE bas et différents ; FIN d'A vers le haut, de B vers le bas.
  - Un LFO raide → **CRS** d'A et B, unipolaire, **−10** : le son monte en « wow » ; pente rendue plus raide ensuite.
  - FILTER 1 **Multi BN** (Band + Notch) : un LFO → CUTOFF (la bande), **le même LFO inversé → VAR (FREQ)**, la fréquence du notch. Les deux bosses doivent presque se toucher ; un peu de RES. Filtre activé aussi sur B ; MIX réglé pour garder un peu d'aigus.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en mode ENVELOPE, 1/8, rampe montante raide vers CRS −10 → 0 ; LFO 2 en mode ENVELOPE, 1/4, rampe montante → CUTOFF +40 %, → VAR −40 % ; RES 20 %.
- **ENV 1** : 2 ms / 0 / 800 ms / −3 dB / 200 ms [ORIGINAL].
- **FX** [SOURCE HO-09] :
  1. Distortion **Stomp Box**, DRIVE modulé par le LFO (il monte au fil de la note).
  2. Compressor (gain monté).
  3. Reverb prudente, LO CUT.
  4. Equalizer : bande en Peak dont la FREQ est balayée par le LFO, des graves vers les médiums ; bande haute en High Shelf au goût.
  5. Delay avec des temps différents à gauche et à droite, filtré dans les médiums.
- **Durées** [CALCUL] : à 174 BPM, 1/8 = 172,4 ms et 1/4 = 344,8 ms.
- **Macros** : `Tone` MIX du filtre 60 → 100 % · `Motion` LFO 1 → CRS 0 → −14 · `Dirt` LFO → DRIVE de la Stomp Box 0 → 60 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : notes de deux à quatre temps, MIDI 60 à 79 ; voir la grille DnB.
- **Test** : l'astuce de la vidéo (Serum FX en Note Latch sur du bruit, pour voir la courbe du filtre double « PP12 ») sert à recopier une forme ; ici, observer la courbe dans le graphe du filtre (clic droit › Frequency Response & FFT).

### HK11 Stab FM à harmoniques dessinées
- **Patch** [SOURCE HO-10] :
  - OSC A : sinus. OSC B : sinus, **LEVEL 0** ; OSC A, WARP 1 **FM (B)** monté ; octave de B relevée.
  - Table de B dessinée dans l'éditeur : **fondamentale + quinte + troisième octave + quatrième octave**.
  - LFO 1 dessiné, mode ENVELOPE → LEVEL d'A. NOISE Bright White.
  - Un second LFO, unipolaire, courbe très courte, mode ENVELOPE → **CRS** (« core speech » [ASR ?] ; la même vidéo, lue comme CH-09, dit le RATE du LFO 1 : à trancher à l'écran) : le transitoire.
  - FILTER 1, CUTOFF modulé par un LFO séparé, unipolaire, forme de pluck.
- **Harmoniques** [DÉDUCTION] : une table d'un cycle ne contient que des harmoniques entières. La « quinte » est donc l'harmonique 3 (une octave et une quinte au-dessus). « Troisième et quatrième octave » : harmoniques 4 et 8 si la fondamentale compte comme première octave, 8 et 16 sinon ; à lire à l'écran.
- **Valeurs de départ** [ORIGINAL] : OSC B OCT +1 ; FM (B) 35 % ; LFO 1 0 → 100 % en 250 ms ; LFO 2 → CRS +12 en 15 ms ; LFO 3 → CUTOFF 50 % en 150 ms.
- **ENV 1** : 0 ms / 0 / 1 s / 0 dB / 120 ms [ORIGINAL] : les LFO font la forme.
- **FX** [SOURCE HO-10] : Distortion → Chorus (LPF monté) → Compressor (seuil bas, GAIN au maximum) → Equalizer, bosse vers **500 Hz**, Q bas.
- **Hors de Serum** [SOURCE HO-10] : reverb courte → EQ → Overdrive de Live → EQ → Erosion de Live → reverb. Ici : Overdrive et Erosion remplacés par une seconde Distortion interne (Diode 1) et un Filter **SampHold** discret sur les aigus [DÉDUCTION] ; reverbs sur un retour.
- **Couche de percussion** [SOURCE HO-10] : un transitoire seul sur une autre piste, même chaîne, EQ coupe-bas, reverb plus courte, hauteur ajustée.
- **Macros** : `Tone` CUTOFF 20 → 70 % · `Motion` FM (B) 15 → 60 % · `Dirt` GAIN du Compressor 0 → 18 dB · `Space` MIX de la Reverb 0 → 20 %.
- **Jeu** : stabs de drop, MIDI 60 à 72, rythme serré sur la caisse claire.
- **Test** : la couche de percussion et le transitoire de hauteur font double emploi si les deux sont forts ; garder l'un des deux dominant.

### HK12 Hook d'intro qui retombe
- **Patch** [SOURCE HO-11] :
  - OSC A : « MB Saw » (analogique), WT POS légèrement avancée ; **UNISON 14**, DETUNE bas, dosé par une macro.
  - LFO 1 (en HZ, rapide) → WT POS un peu. Étalement de WT POS par voix d'unison **≈ 30** : chaque voix lit une position différente. En Serum 1 c'était dans l'onglet Global ; en Serum 2, **WT POS** des réglages d'unison du panneau d'oscillateur (cartographie § 3.1).
  - VOICING **MONO**, PORTA **≈ 100 ms**, **ALWAYS**.
  - FILTER 1 **Reverb** (Misc), CUTOFF **≈ 100 Hz**, **suivi au clavier**, MIX baissé, DRIVE monté, un peu de RES.
  - LFO 2 à deux points → **Main Tuning**, quantité **1**, bipolaire, **2 mesures**, mode ENVELOPE : un coup de hauteur à chaque note, puis une descente sur les notes longues. SMOOTH ajouté.
- **ENV 1** : ATK **≈ 140 ms**, REL **≈ 3 s** [SOURCE HO-11] ; ici 140 ms / 0 / 2 s / −2 dB / 3 s.
- **Durées** [CALCUL] : à 174 BPM, deux mesures = 2,76 s ; l'attaque de 140 ms dépasse une double croche (86 ms) : le hook joue des notes longues.
- **FX** [SOURCE HO-11] : Distortion **Asym**, DRIVE modulé par LFO 1, MIX baissé → Reverb MIX **≈ 50 %**, SIZE montée → Chorus MIX ≈ 30 % → Compressor (seuil bas, gain monté) → Equalizer (High Shelf) → Hyper/Dimension **en fin de chaîne, après la reverb**, MIX, RATE et DETUNE baissés, SIZE de Dimension très basse.
- **Macros** : `Tone` CUTOFF du filtre Reverb 80 → 300 Hz · `Motion` DETUNE 0,05 → 0,3 · `Dirt` MIX de l'Asym 0 → 50 % · `Space` MIX de la Reverb 30 → 70 %.
- **Jeu** : intro et break, MIDI 64 à 81, notes de deux à quatre temps liées.
- **Test** : unison 14 sur un patch mono coûte peu de voix ; avec 50 % de reverb, vérifier que le hook ne noie pas la caisse claire quand la batterie entre.

### HK13 Riff jump-up
- **Registre médium-grave** : le « lead » jump-up est le riff du drop (HO-12). Il touche à la basse ; voir aussi `../../../serum-2-basses-house-future-house/references/recettes/dnb-f06-jump-up.md`. Le grave vient d'un sub sur sa piste.
- **Patch** [SOURCE HO-12] :
  - Tempo 175. OSC A : Basic Shapes, **OCT −2**, RAND désactivé, WT POS **2** ; WARP 1 **Sync ≈ 8** ; LEVEL au maximum.
  - LFO en RETRIG dessiné (cible : LEVEL ou WT POS, interprétation de l'étude).
  - FILTER 1 **MG Low 12**, CUTOFF tout en bas, LFO → CUTOFF (pluck en scie) ; DRIVE monté.
  - Le SUB à −2 octaves, modulé en niveau par un LFO : ici **éteint** (règle 1 de `leads.md`).
- **Registre** [CALCUL] : à OCT −2, une note jouée à MIDI 60 sonne à 36 (65,4 Hz). Ici OCT −1 et High Pass à 90 Hz : jouée entre MIDI 55 et 67, elle sonne de 98 à 196 Hz.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 1/16, RETRIG, descente raide, → CUTOFF 70 % et → Sync +20 %.
- **ENV 1** : 0 ms / 0 / 1 s / 0 dB / 40 ms [ORIGINAL].
- **FX** [SOURCE HO-12] : Distortion **Diode 1 à fond**, mode **PRE** avec passe-haut → Filter **Low 18**, LFO → CUTOFF et DRIVE.
- **Hors de Serum** [SOURCE HO-12] : deux OTT (DEPTH et TIME baissés), Decimort 2, RBass Mono, Camel Crusher, Pro-L, sidechain ; aucun n'est vérifié sur le Mac. Ici : deux Compressor **Multiband** internes, RazorClip, ShaperBox 3 pour le sidechain.
- **Macros** : `Tone` CUTOFF du Filter Low 18 20 → 70 % · `Motion` Sync 0 → 20 · `Dirt` passe-haut de la Diode 1 200 → 600 Hz · `Space` aucun : MIX d'une reverb très courte 0 → 10 %.
- **Jeu** : riff de doubles croches, MIDI 55 à 67 ; à 175 BPM, une double croche dure 85,7 ms [CALCUL].
- **Test** : le riff et le sub doivent sonner comme un seul instrument en mono.

### HK14 Lead principal sec — première couche
- **Méthode** [SOURCE HO-13] : le hook se construit d'abord en ostinato (un motif court répété qui revient sur une note), puis en **quatre couches** Serum (HK14 à HK17). Tempo de la vidéo : 170 ; La majeur, verrou de gamme dans Live.
- **Patch** [SOURCE HO-13, couche 1] :
  - OSC A : scie de l'Init, **UNISON 3**, DETUNE modéré.
  - LFO 2 → LEVEL du NOISE : petite retombée. LFO 2 → CUTOFF d'un FILTER **MG Low**.
  - **Pas de reverb** : le lead reste devant.
- **Valeurs de départ** [ORIGINAL ; valeurs « à l'écran » dans la vidéo] : DETUNE 0,1 ; MG Low 24, CUTOFF 55 % ; LFO 2 en mode ENVELOPE, 1/4, descente → CUTOFF −20 % et → LEVEL du NOISE (NOISE Bright White à 20 %).
- **ENV 1** : 2 ms / 0 / 1 s / −2 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE HO-13] : Distortion → Compressor → Filter. Après Serum : EQ des graves et des aigus, OTT modifié. Ici : Equalizer en High Pass à 180 Hz, Compressor Multiband à MIX 40 %.
- **Macros** : `Tone` CUTOFF 35 → 80 % · `Motion` LFO 2 → CUTOFF 0 → −40 % · `Dirt` DRIVE de la Distortion 10 → 60 · `Space` aucune reverb : MACRO 4 sur le niveau d'envoi au groupe des quatre couches.
- **Jeu** : l'ostinato, MIDI 64 à 81. Grille du fichier.
- **Test** : la couche seule doit déjà porter la mélodie ; les trois suivantes l'habillent.

### HK15 Couche pluck réverbérée — deuxième couche
- **Patch** [SOURCE HO-13, couche 2] : table **« BS2 Filthy »** (analogique), DETUNE 0, **ENV 1 très courte**, passe-haut ; EQ + OTT (« Wombo Combo ») et reverb sur cette couche placée derrière.
- **Valeurs de départ** [ORIGINAL] : ENV 1 0 ms / 0 / 180 ms / 0 / 120 ms ; Equalizer en High Pass à 250 Hz ; Compressor Multiband MIX 50 % ; Reverb Hall, MIX 35 %, SIZE 60.
- **Macros** : `Tone` WT POS 0 → 60 % · `Motion` DEC d'ENV 1 100 → 300 ms · `Dirt` GAIN du Multiband 0 → 10 dB · `Space` MIX de la Hall 20 → 50 %.
- **Jeu** : les mêmes notes que HK14, une octave au-dessus si la couche se perd.
- **Test** : couper HK14 : on doit encore entendre le rythme du hook, en plus lointain.

### HK16 Couche legato au filtre Reverb — troisième couche
- **Patch** [SOURCE HO-13, couche 3] :
  - Table « Distorted Sub DKS » [ASR ?] (numérique). ENV 1 avec **SUS au maximum** ; VOICING **MONO + LEGATO**.
  - FILTER 1 **Reverb** (Misc), **MIX au maximum** ; ENV 2 → CUTOFF, très faible.
  - Hyper/Dimension MIX **≈ 50** (alternative de la vidéo : Chorus-Ensemble de Live, remplacé ici par le Chorus interne).
- **Valeurs de départ** [ORIGINAL] : ENV 2 10 ms / 0 / 600 ms / 0 / 200 ms → CUTOFF 8 % ; PORTA 60 ms ; Equalizer en High Pass à 200 Hz.
- **ENV 1** : 20 ms / 0 / 1 s / 0 dB / 400 ms [ORIGINAL].
- **Macros** : `Tone` CUTOFF du filtre Reverb 30 → 70 % · `Motion` VAR (DAMP) 20 → 80 % · `Dirt` DRIVE du filtre 0 → 40 · `Space` MIX d'Hyper/Dimension 30 → 70 %.
- **Jeu** : les mêmes notes que HK14, liées.
- **Test** : la couche doit lier les notes de l'ostinato sans s'entendre comme une voix séparée.

### HK17 Couche en Ring Mod — quatrième couche
- **Patch** [SOURCE HO-13, couche 4, la « sauce secrète »] : copie de HK16, table **« MS Saw »** [ASR ?], filtre **Ring Mod 2**, c'est-à-dire **Ring Modx2** (cartographie § 6), Compressor (OTT) et Chorus.
- **Valeurs de départ** [ORIGINAL] : Ring Modx2, CUTOFF 40 % (fréquence de modulation), VAR (SPREAD) 20 %, MIX 50 % ; Compressor Multiband MIX 40 % ; Chorus MIX 25 %.
- **Ce que fait le Ring Mod** [DÉDUCTION] : il ajoute la somme et la différence de chaque partiel avec la fréquence du CUTOFF ; ces partiels ne suivent pas la note. D'où un grain inharmonique, à doser bas sous les trois autres couches.
- **Macros** : `Tone` CUTOFF du Ring Modx2 20 → 70 % · `Motion` VAR (SPREAD) 0 → 50 % · `Dirt` MIX du Ring Modx2 20 → 80 % · `Space` MIX du Chorus 10 → 40 %.
- **Jeu** : les mêmes notes que HK14.
- **Test** : couper et remettre la couche : le hook doit gagner en éclat sans paraître faux.
- **Groupe des quatre couches** [SOURCE HO-13] : OTT, Saturator, Reverb, EQ dans Live. Ici : un retour ValhallaVintageVerb, J37 Tape à la place du Saturator, Pro-Q 4 ; l'OTT par un Compressor Multiband dans l'une des couches, ou par Pro-C 3 sur le groupe.

### HK18 Spirit lead
- **Patch** [SOURCE HO-14, transcription manuelle] :
  - OSC A : Basic Shapes, **carré** ; FILTER 1 actif ; VOICING **MONO**, PORTA **≈ 31 ms**.
  - FILTER 1 **Low 24**, CUTOFF **≈ 9 kHz**, FAT monté, un peu de RES.
  - NOISE « Alpha NZ », **LEVEL 0** ; matrice : **Noise OSC → CRS** d'OSC A, **≈ 25 %** : un léger cri.
  - LFO 1 → LEVEL **−45**, RATE **1/16** : vibrato d'amplitude.
  - Menu de la matrice › **Create Vibrato** : un LFO → Main Tuning **2 %**, bipolaire ; son Aux Source passe de la Mod Wheel à une **MACRO 5 « Vibrato »**, réglée à 50 %.
- **Le vibrato d'amplitude** [CALCUL] : à 150 BPM, 1/16 = 100 ms, soit 10 Hz.
- **ENV 1** : 2 ms / 0 / 1 s / −2 dB / 300 ms [ORIGINAL].
- **FX** [SOURCE HO-14] :
  1. Distortion **Asym avant** Hyper/Dimension, filtre post vers **13 kHz**, DRIVE au maximum.
  2. Compressor **Multiband**, seuils −10 / −13 dB, ratio 4:1.
  3. Equalizer : bande basse vers **600 Hz**, Q 45 %, **−4 à −5 dB** (shelf, interprétation) ; Peak à Q 60 % sur une résonance.
  4. Reverb **Plate**, LO CUT 21 %, HI CUT, WIDTH au maximum, MIX **50 %**.
- **Hors de Serum** [SOURCE HO-14] : EQ (sous 650 Hz et au-dessus de 16,5 kHz), Ozone Imager ≈ 50 % (vers le mono, le son était trop phasé), Blood Overdrive de FL Studio, OTT ≈ 25 %, compresseur (attaque 0,1 ms, gain 4 dB), soothe (résonance vers 1 kHz). Ici : Pro-Q 4, Ozone Imager 2, J37 Tape, Pro-C 3, soothe3 ; tous présents dans l'inventaire.
- **Macros** : `Tone` CUTOFF 4 → 12 kHz · `Motion` Noise OSC → CRS 0 → 40 % · `Dirt` DRIVE de l'Asym 50 → 100 · `Space` MIX de la Plate 20 → 60 % · MACRO 5 `Vibrato`.
- **Jeu** : MIDI 67 à 88, phrases chantées avec glissades.
- **Test** : le cri doit rester un timbre, pas une fausse note ; au-delà de 40 % de Noise OSC → CRS, la hauteur se brouille.

### HK19 Sync lent
- **Patch** [SOURCE HO-15, transcription médiocre] :
  - Écrire d'abord la mélodie, avec des glissades. VOICING **MONO**, PORTA **≈ 80** (unité non dite).
  - OSC A : Basic Shapes (analogique), WT POS **à mi-chemin entre scie et carré**.
  - WARP 1 **Sync ≈ 140-150 %** ; LFO 1, RATE abaissé : un modulateur **très lent** du Sync, profondeur **≈ 20-25 %**.
- **Unité du Sync** : la cartographie donne un bouton de 0 à 1 (§ 3.2) ; « 140-150 % » se lit peut-être comme un rapport de fréquence. À lire à l'écran, comme pour LD05 et LD19.
- **Valeurs de départ** [ORIGINAL] : LFO 1 en 4 bar, FREE, sinus ; PORTA 80 ms.
- **ENV 1** : 5 ms / 0 / 1 s / −2 dB / 250 ms [ORIGINAL].
- **FX** [SOURCE HO-15] : Hyper/Dimension (réglages à l'écran) → Distortion **≈ 75 %** → Compressor **Multiband**, gain ≈ **5 dB**, seuil ≈ **−12 dB** → Reverb ≈ 10 % → Delay ≈ 2 % [ASR ?].
- **Durée** [CALCUL] : à 150 BPM, quatre mesures durent 6,4 s : le timbre change d'une phrase à l'autre, pas d'une note à l'autre.
- **Macros** : `Tone` WT POS 30 → 70 % · `Motion` LFO 1 → Sync 0 → 40 % · `Dirt` DRIVE de la Distortion 40 → 90 · `Space` MIX de la Reverb 0 → 25 %.
- **Jeu** : MIDI 64 à 84, mélodie de drop avec glissades.
- **Test** : la vidéo est la seule source ; un LFO aussi lent peut sonner statique sur une phrase courte.

### HK20 Hook doux à deux voix — signature sous 124
- **Recette [ORIGINAL]**, pour la règle « Signature sous 124 BPM » d'`AGENTS.md` : un hook qui reste doux à côté du kick de la signature (`../../../drums-signature/references/signature.md`).
- **Patch** :
  - OSC A : Basic Shapes, sinus, RAND 0.
  - OSC B : Basic Shapes, triangle, SEM **+4** (tierce majeure ; **+3** pour une tierce mineure), LEVEL 45 %.
  - NOISE « Kick Attack » (au choix), **one-shot**, LEVEL 15 %, pour une attaque discrète [principe de la couche transitoire, `../leads-nappes-textures.md`].
  - FILTER 1 **MG Low 12** sur B, CUTOFF 45 %, ENV 2 0 / 0 / 200 ms / 0 / 100 ms → CUTOFF 20 %.
  - VOICING MONO + LEGATO, PORTA 40 ms.
- **ENV 1** : 4 ms / 0 / 600 ms / −8 dB / 200 ms.
- **FX** : Distortion **Tape Sat.**, DRIVE 15, MIX 30 % → Chorus MIX 15 % → Equalizer en High Pass à 150 Hz → Delay 1/8 pointée, MIX 12 %.
- **Delay** [CALCUL] : à 122 BPM, 1/8 pointée = 368,9 ms.
- **L'intervalle** : SEM +4 est fixe ; sur un degré où la tierce est mineure, la seconde voix sonne faux. Jouer la cellule sur des notes dont la tierce majeure est dans la gamme, ou passer `Tone` sur SEM de B.
- **Macros** : `Tone` SEM de B +3 / +4 (deux crans) · `Motion` ENV 2 → CUTOFF 0 → 40 % · `Dirt` DRIVE de la Tape Sat. 0 → 35 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : MIDI 64 à 79, cellule de trois à cinq attaques et un silence (méthode de `composer-hooks-funk-electro`).
- **Test** : sans source vidéo ; à valider à l'oreille avec le kick et la basse de la signature.

## Motifs de départ (grilles vérifiées)

Numérotation de Live (C3 = 60). Cellules écrites ici, aucune n'est reprise d'un titre. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/synths/hooks.md`. Notation Producer Pal : `--fichier references/synths/hooks.md --titre <titre> --format ppal`.

```grille
titre: Tech house 126 — horn (HK01, HK02)
tempo: 126
accords: Gm7 | Ebmaj7
hook: G3[1:2] Bb3[1&:1] G3[2:1] F3[2&:2] D3[3&:1] | G3[1:2] Bb3[1&:1] G3[2:1] F3[2&:2] Eb3[3&:2]
```

```grille
titre: DnB 174 — wow (HK10)
tempo: 174
accords: Am | F
hook: A4[1:3] C5[1a:1] A4[2&:2] E4[3:6] | F4[1:3] A4[1a:1] C5[2&:2] A4[3:6]
```

```grille
titre: Melodic dubstep 150 — ostinato en quatre couches (HK14 à HK17)
tempo: 150
accords: A | E
hook: E4[1:2] A4[1&:2] B4[2:2] C#5[2&:4] B4[3a:2] A4[4&:2] | E4[1:2] G#4[1&:2] B4[2:2] C#5[2&:4] B4[3a:2] G#4[4&:2]
```

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : « BS Subies » [ASR], « BS Filthy », « BS2 Filthy », les tables Juno, « MB Saw », « MS Saw » et « Distorted Sub DKS » [ASR], « Alpha NZ », « AC Hum ». Lire la forme du LFO « double aileron » de HK01 et la cible du second LFO de HK11.
- Lire l'unité du Sync de HK19 et le temps du delay de HK06.
- Écouter chaque recette (règle 10 de `leads.md`) dans le contexte du drop, avec le sidechain ; garder un ou deux hooks par morceau et consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
- Fichiers suivants du lot : accords, pads, drones.
