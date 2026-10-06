# Vingt recettes d'accords dans Serum 2

Quatrième fichier du lot de synthés : stabs, keys et murs d'accords. Rédigé le 05/10/2026. Sources :
- l'étude des quinze tutoriels d'accords, CH-01 à CH-15, de `../tutoriels-synths-serum.md`, sa section « Écartés » (une vidéo de UK garage citée avec ses valeurs) et la synthèse `../synths-serum-synthese.md` (section Accords) ;
- la cartographie de Serum 2 (`../serum2-cartographie.md`).

**Toutes les vidéos sources sont en Serum 1** : aucun tutoriel d'accords en Serum 2 n'avait de réglages commentés. Les noms sont traduits selon la règle 3 de `leads.md`. Le choix des accords relève de `../../../theorie-musicale-electronique/SKILL.md` et du rôle `compositeur-arrangeur` ; ce fichier donne le timbre et dit quand le patch impose déjà un intervalle.

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes : **[SOURCE CH-nn]**, **[CALCUL]**, **[DÉDUCTION]**, **[ORIGINAL]**, comme dans `leads.md`.

## Règles

Les dix règles communes au lot sont dans `leads.md`. Ce qui s'ajoute pour les accords :

1. **Deux voies, à ne pas mélanger.** Soit l'accord est dans le patch : des oscillateurs à des intervalles fixes, une touche donne l'accord (AC01, AC04, AC05, AC12). On joue alors des notes seules ; un accord joué sur un tel patch multiplie les notes et brouille. Soit l'accord est joué en MIDI sur un patch simple (les autres recettes).
2. **Un patch à intervalles fixes joue des accords parallèles.** La même forme sur chaque note sort de la gamme sur certains degrés. C'est la couleur des stabs house des années 90 (CH-01) ; chaque fiche concernée dit sur quels degrés.
3. **High Pass entre 120 et 220 Hz.** Les accords se battent avec la basse médium dans 150-300 Hz ; si la basse joue la fondamentale, retirer la note la plus grave de l'accord (CH-13, CH-11).
4. **Phase aléatoire : le but décide.** RAND à 0 donne une attaque identique à chaque note, « comme un sample » (CH-05, CH-15) ; RAND haut donne un son plus épais qui varie (CH-11). Chaque fiche choisit.
5. **Polyphonie** : POLY 8 suffit pour des accords de quatre notes avec un peu de release ; l'unison multiplie les voix (cartographie, § 9).
6. **Référence A/B du fichier** : AC01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| AC01 | Stab mineur dans une note | House des années 90, référence A/B | OSC A +7, OSC B +3, OSC C racine, German LP, bruit d'attaque |
| AC02 | Stab deep à table FM | Deep, melodic house | scie + FM_Freak, ENV 1 → CUTOFF, Flanger |
| AC03 | Stab garage en sinus | Garage, minimal, tech house | deux sinus à ±1 octave en unison 4, Downsample, petit glissement de hauteur |
| AC04 | Orgue en sinus | Garage, tech house | sinus + sinus à +2 octaves, HOLD 50 ms, harmonique dessinée |
| AC05 | Rave stab à trois oscillateurs | House rave | racine, quinte et septième mineure, phase fixe, hauteur sur une mesure |
| AC06 | Stab melodic à quinte qui dérive | Melodic house et techno | scie + scie à +7 en Bend +/−, LFO lent en Hz, reverb ouverte par l'enveloppe |
| AC07 | Accord future house qui plonge | Future house | unison 9 sur A et B, ENV 3 → CRS ±22, LFO sur le cutoff |
| AC08 | Keys nu disco à pan aléatoire | Nu disco, house | NoteOn Rand → PAN à la place de l'unison, enveloppe de filtre séparée |
| AC09 | Accords qui plient | UK garage, house | sinus unison 5, ENV 2 → Main Tuning ±12, Bend +, Downsample |
| AC10 | Keys afro en FM | Afro house | sinus en FM d'un sinus à l'octave, enveloppe sur la FM |
| AC11 | Stab feutré sous 124 | Signature sous 124, électro chill | scie + sinus, MG Low 24 fermé, attaque de filtre de 15 ms |
| AC12 | Stab FM à quinte dessinée | DnB dancefloor | table de B dessinée (fondamentale, quinte, octaves), LFO de transitoire |
| AC13 | Keys liquid en sinus | DnB liquide | sinus + sinus à l'octave, decay court, delay filtré à 1,7 kHz |
| AC14 | Accords liquid de 7e et 9e | DnB liquide | scie unison 6 + table spectrale, ENV 2 en attaque sur le cutoff |
| AC15 | Stab à formant spectral | DnB dancefloor, neuro mélodique | table Monster 1, passe-bande, distorsion forte |
| AC16 | Accords « chaos saw » | Melodic dubstep | S&H rapide sur CRS, tierce montée d'une octave |
| AC17 | Mur d'accords désaccordé | Melodic dubstep | scie 9 voix, BLEND 75 %, Phaser léger |
| AC18 | Couche d'accords propre | Melodic dubstep | scie 3 voix, DETUNE 0,04, coupe-bas et coupe-haut |
| AC19 | Habillage du mur : sirène et arpège | Melodic dubstep | scie très désaccordée à vibrato 8,2 Hz, arpège pané en 1/4 triolet |
| AC20 | Wub future bass | Future bass | triangle + carré, LFO 1/8 sur les niveaux, FM (B), Multiband |

## Les vingt recettes

### AC01 Stab mineur dans une note — référence du fichier
- **Patch** [SOURCE CH-01] :
  - L'accord est **dans les oscillateurs** : on joue une seule note, le stab sonne comme un accord samplé des années 90.
  - Fondamentale : le SUB en scie dans la vidéo. Ici **OSC C** en scie, SEM 0 [ORIGINAL] : même rôle, au-dessus du High Pass (règle 1 de `leads.md`).
  - OSC A : scie par défaut, SEM **+7** (quinte), **UNISON 5**, petit DETUNE.
  - OSC B : « Basic MG », WT POS montée, LEVEL monté, SEM **+3** (tierce mineure).
  - LFO 1 → WT POS d'OSC B, BPM désactivé, lent.
  - FILTER 1 sur tous les oscillateurs, **German LP** (sans VAR, cartographie § 6). ENV 2 → CUTOFF ; RES et DRIVE montés.
  - ENV 2 : SUS 0, decay court, un peu de release (pluck).
  - NOISE « Bright White », **one-shot**, départ aléatoire ; ENV 2 → LEVEL du NOISE, quantité réduite.
  - FIN **≈ −5** sur un oscillateur et **+5** sur l'autre : la dérive.
- **L'accord** [CALCUL] : 0, +3 et +7 forment une triade mineure. Joué sur toutes les notes de do mineur naturel, il donne Cm, Fm et Gm dans la gamme, mais Dm, Ebm, Abm et Bbm hors gamme (leurs tierces ou quintes sortent du mode). C'est la couleur voulue par la vidéo.
- **Valeurs de départ** [ORIGINAL] : LFO 1 à 0,2 Hz, vers WT POS 15 % ; CUTOFF 25 %, RES 20 %, DRIVE 30 ; ENV 2 0 / 0 / 200 ms / 0 / 100 ms vers CUTOFF 45 %.
- **ENV 1** : SUS un peu baissé, release et decay ajustés [SOURCE CH-01] ; ici 0 ms / 0 / 450 ms / −10 dB / 200 ms.
- **FX** [SOURCE CH-01] : Chorus par défaut, MIX baissé → Distortion **Tape Sat.**, DRIVE **≈ 15 %**, MIX baissé → Delay **1/8**, FEEDBACK bas, **Ping-Pong**, coupe-bas dans le filtre du delay → Reverb **Hall**, SIZE montée, DECAY baissé, LO CUT, MIX **≈ 16 %** → Compressor par défaut, gain monté ; Equalizer en High Pass à 150 Hz [règle 3].
- **Delay** [CALCUL] : à 122 BPM, 1/8 = 245,9 ms.
- **Macros** : `Tone` CUTOFF 15 → 55 % · `Motion` ENV 2 → CUTOFF 20 → 70 % · `Dirt` DRIVE de la Tape Sat. 0 → 40 % · `Space` MIX de la Hall 5 → 30 %.
- **Jeu** : une note par stab, MIDI 60 à 72, rythme syncopé. Voir la grille house de ce fichier.
- **Test** : la vidéo essaie aussi une ATK sur ENV 2 ; une attaque de 5-10 ms adoucit le stab.

### AC02 Stab deep à table FM
- **Patch** [SOURCE CH-02, transcription manuelle] :
  - OSC A : scie par défaut. OSC B : table FM, « FM_Splat » essayée, **« FM_Freak »** retenue.
  - FILTER 1 actif, OSC B routé (A à vérifier) ; DRIVE et FAT ; ENV 1 → CUTOFF (filtre ouvert qui se referme) ; un peu de RES.
  - LFO → CUTOFF, BPM désactivé, quelques Hz, petite quantité : de la vie.
- **ENV 1** : ATK **≈ 10-11 ms**, SUS 0, DEC **≈ 500 ms**, REL ≈ pareil [SOURCE CH-02] ; courbe ajustée.
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 30 %, ENV 1 → CUTOFF 40 % ; LFO 1 à 3 Hz, ±3 %.
- **FX** [SOURCE CH-02] : Flanger, MIX **≈ 1/3** → Chorus discret → Equalizer, bande basse vers **150 Hz**, Q baissé, pour retirer le bas. Reverb et delay en envois dans Live (ici des retours, ValhallaVintageVerb).
- **Hors de Serum** [SOURCE CH-02] : EQ Eight (aigus montés, coupe-bas, creux dans les médiums) et Saturator en Analog Clip (≈ 4 dB, soft clip, MIX 50 %). Ici : Pro-Q 4 ; J37 Tape ou RazorClip à MIX 50 %.
- **Règle 1 du fichier** : la même ENV 1 pilote volume et filtre ; c'est le decay de 500 ms qui fait le stab.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` ENV 1 → CUTOFF 20 → 60 % · `Dirt` DRIVE 0 → 50 · `Space` MIX du Flanger 10 → 50 %.
- **Jeu** : accords joués en MIDI (la vidéo donne un MIDI en description, non repris), MIDI 55 à 76.
- **Test** : le timbre seul est repris de la référence de la vidéo.

### AC03 Stab garage en sinus
- **Patch** [SOURCE CH-03] :
  - OSC A : Basic Shapes, sinus, **OCT −1**, **UNISON 4**, DETUNE **≈ 10**.
  - OSC B : pareil, **OCT +1**, 4 voix, DETUNE ≈ 10.
  - NOISE [ASR « Argan nose », probablement un bruit d'orgue] pour la « poussière » ; A, B et NOISE vers le filtre.
  - CUTOFF **≈ 100 Hz**, ENV 1 → CUTOFF **≈ 40** ; DRIVE monté, RES essayée puis baissée, FAT.
  - Une enveloppe → FIN des deux oscillateurs, courbe tirée vers la gauche : léger glissement de hauteur à l'attaque.
- **ENV 1** : ATK **5 ms**, SUS baissé (pluck), DEC rallongé, un peu de REL [SOURCE CH-03] ; ici 5 ms / 0 / 900 ms / −20 dB / 250 ms. Essais de la vidéo : DEC jusqu'à 2 s.
- **Valeurs de départ** [ORIGINAL] : MG Low 24 ; ENV 3 0 / 0 / 60 ms / 0 / 0 vers FIN −20 cents.
- **Registre** [CALCUL] : les deux oscillateurs sonnent à deux octaves d'écart, une octave sous la note et une octave au-dessus. Pour garder la couche basse au-dessus de 120 Hz, jouer les accords à partir de MIDI 59 environ (la note la plus basse sonne alors à MIDI 47, 123,5 Hz).
- **FX** [SOURCE CH-03] : Hyper/Dimension (Dimension pour élargir) → Distortion **Downsample** avec filtre **PRE**, MIX **≈ 30** → Chorus → Reverb DECAY **≈ 4 s** → Delay synchronisé **1/8**, FEEDBACK baissé.
- **Macros** : `Tone` CUTOFF 60 → 300 Hz · `Motion` ENV 1 → CUTOFF 20 → 60 · `Dirt` DRIVE du Downsample 0 → 40 · `Space` MIX de la Reverb 10 → 40 %.
- **Jeu** : **La mineur 7**, joué avec du swing, vélocité **≈ 80** [SOURCE CH-03]. Voir la grille garage.
- **Test** : la vidéo essaie aussi la table MB Saw ; comparer à niveau égal.

### AC04 Orgue en sinus
- **Patch** [SOURCE CH-04] :
  - OSC A : Basic Shapes, sinus. OSC B : sinus, essayé à +7, puis +1 octave, **+2 octaves** retenu (son « garage »).
  - NOISE en one-shot (bruit d'orgue probable [ASR]), LEVEL baissé ; ENV 1 → LEVEL du NOISE **≈ 10**.
  - FILTER 1 **MG Low 12**, A et B, CUTOFF **≈ 100** (unité non dite), ENV 1 → CUTOFF **≈ 30**, RES **≈ 25**, DRIVE.
  - VOICING **MONO**.
  - Éditeur de tables (additif) : harmonique « 2/3 » montée à **≈ 30**, copiée vers OSC B ; essai de l'harmonique 3 à ≈ 15.
- **ENV 1** : ATK **5 ms**, HOLD **≈ 50 ms**, DEC **1 s**, SUS 0 [SOURCE CH-04] ; DEC raccourci ou allongé (2 s) ensuite, plus du REL.
- **Les tirettes** [DÉDUCTION] : A sur la note et B deux octaves au-dessus correspondent à deux tirettes d'orgue à deux octaves d'écart (8′ et 2′ si A joue le 8′) ; l'harmonique 3 ajoutée dans la table est la quinte de l'octave (2 ⅔′). Comparer avec les registrations de `../../../studio-grade-funk-keys-synth-sound-design/SKILL.md`.
- **MONO** : un orgue en mono ne joue pas d'accord ; ici le stab joue des notes seules, l'harmonie vient des tirettes. Pour des accords, passer en POLY 8.
- **FX** [SOURCE CH-04] : Hyper/Dimension, MIX d'Hyper monté (plus « carré », garage) → Distortion MIX **≈ 25** → Compressor → Chorus → Reverb DECAY **≈ 3 s** (ou 2 s), LO CUT monté.
- **Macros** : `Tone` CUTOFF ± 30 % autour du réglage · `Motion` niveau de l'harmonique 3 (WT POS entre deux frames préparées) 0 → 100 % · `Dirt` MIX de la Distortion 0 → 50 · `Space` MIX de la Reverb 5 → 30 %.
- **Jeu** : notes seules ou accords en POLY, MIDI 57 à 76, stabs courts sur le contretemps.
- **Test** : le HOLD de 50 ms fait le « clac » de l'orgue ; à 0, le son devient un pluck.

### AC05 Rave stab à trois oscillateurs
- **Patch** [SOURCE CH-05, la même vidéo que HO-05] : les rave stabs étaient des accords samplés. La vidéo ajoute un second oscillateur à un intervalle, et propose un troisième avec le SUB. Ici le troisième est **OSC C** [ORIGINAL, règle 1 de `leads.md`].
  - OSC A : table Juno (carré ou DCO), SEM 0. OSC B : même table, SEM **+10** (ou −2). OSC C : même table, SEM **+7** [ORIGINAL].
  - **RAND à 0** : chaque coup identique, comme un sample. Un peu d'unison pour la stéréo.
  - Désaccorder chaque oscillateur à part ; une enveloppe → **Main Tuning**, plage **12**, longueur **une mesure** (synchro BPM), bipolaire, léger mouvement ; attaque rabotée.
  - NOISE (« oldschool »).
  - FILTER 1 **Low 18** (ou MG Low 18, non tranché) ; enveloppe percussive → CUTOFF ; raboter la fondamentale dans le filtre ou l'EQ interne.
- **L'accord** [CALCUL] : 0, +7 et +10 donnent la racine, la quinte et la septième mineure, sans tierce. L'accord n'est ni majeur ni mineur : il passe sur un accord de septième de dominante comme sur un mineur 7. C'est le plus sûr pour un patch à intervalles fixes (règle 2).
- **Valeurs de départ** [ORIGINAL] : ENV 3 en BPM, DEC 1 mesure, vers Main Tuning −2 demi-tons au départ ; ENV 2 0 / 0 / 180 ms / 0 / 80 ms vers CUTOFF 45 %.
- **ENV 1** : 0 ms / 0 / 400 ms / −8 dB / 150 ms [ORIGINAL].
- **FX** [SOURCE CH-05] : Distortion → Filter passe-bas qui enlève les aigus (côté grunge, vintage) → Flanger comme coloration → Equalizer qui rabote les aigus.
- **Macros** : `Tone` CUTOFF 20 → 60 % · `Motion` ENV 3 → Main Tuning 0 → −12 · `Dirt` DRIVE 10 → 60 · `Space` MIX du Flanger 0 → 40 %.
- **Jeu** : notes seules, MIDI 60 à 72 ; la dernière note du motif longue, pour que l'enveloppe d'une mesure s'entende.
- **Test** : HK05 est le même stab à deux oscillateurs ; comparer les deux à niveau égal.

### AC06 Stab melodic à quinte qui dérive
- **Patch** [SOURCE CH-06] :
  - OSC A : scie de l'Init, UNISON un peu monté, DETUNE baissé ; LFO 1 → FIN d'A, très faible, **en Hz**, lent : dérive analogique.
  - OSC B : scie, SEM **+7**, UNISON monté, DETUNE baissé ; WARP 1 **Bend +/−**, LEVEL baissé ; LFO 1 → Bend +/− et → FIN, plus fort.
  - SUB en scie à −1 octave dans la vidéo : ici OSC C en scie, OCT −1, LEVEL 30 % [ORIGINAL], seulement si les accords sont joués au-dessus de MIDI 60 (la couche sonne alors au-dessus de 130,8 Hz [CALCUL]) ; sinon, éteint.
  - NOISE Bright White, LEVEL monté.
  - FILTER 1 sur A, B, C et NOISE, CUTOFF **fermé à fond** ; ENV 2 → CUTOFF, SUS 0, decay un peu baissé ; DRIVE et FAT montés.
- **Valeurs de départ** [ORIGINAL] : LFO 1 à 0,15 Hz ; vers FIN d'A ±3 cents, de B ±6 cents, vers Bend +/− ±10 % ; ENV 2 0 / 0 / 350 ms / 0 / 200 ms vers CUTOFF 60 %.
- **ENV 1** : 0 ms / 0 / 600 ms / −12 dB / 300 ms [ORIGINAL].
- **FX** [SOURCE CH-06] :
  1. Hyper/Dimension : MIX d'Hyper à 0, Dimension monté, SIZE baissée.
  2. Distortion, DRIVE monté, MIX bas.
  3. Chorus, LPF monté, MIX bas.
  4. Delay **1/8 et 1/16**, **Ping-Pong**, FEEDBACK monté, FREQ baissée, Q baissé, MIX bas.
  5. Reverb : SIZE basse, DECAY haut, sans grave, HI CUT monté, SPIN DEPTH monté, **MIX 0 modulé par ENV 2** : la reverb ne s'ouvre qu'avec l'attaque.
- **Delay** [CALCUL] : à 124 BPM, 1/8 = 241,9 ms et 1/16 = 121,0 ms.
- **Hors de Serum** : ShaperBox et EQ dans la vidéo ; ShaperBox 3 est dans l'inventaire.
- **Macros** : `Tone` CUTOFF 0 → 40 % · `Motion` LFO 1 → Bend +/− 0 → 25 % · `Dirt` DRIVE 10 → 60 · `Space` ENV 2 → MIX de la Reverb 0 → 50 %.
- **L'intervalle** [CALCUL] : B ajoute une quinte à chaque note ; un accord joué devient un accord doublé à la quinte. Jouer des triades sans quinte, ou des notes seules (règle 1).
- **Jeu** : MIDI 60 à 76.
- **Test** : la dérive doit rester sous le seuil où l'accord paraît faux.

### AC07 Accord future house qui plonge
- **Patch** [SOURCE CH-07] :
  - OSC A **UNISON 9**, DETUNE baissé ; OSC B pareil.
  - FILTER 1 **MG Low 24** sur A et B.
  - ENV 3, decay court → **CRS** des deux oscillateurs [ASR « correct b »], quantité **−22** : la « chute de hauteur », présentée comme la technique propre à la vidéo.
  - LFO 1 redessiné → CUTOFF à fond ; vitesse réglée pour un effet « wobble » [ASR].
- **Le sens de la glissade** [DÉDUCTION] : avec SUS 0 et une quantité négative, la hauteur part 22 demi-tons **sous** la note et remonte vers elle : une montée, pas une chute. Pour une chute, quantité positive (départ au-dessus). La vidéo dit « chute » : trancher à l'écran.
- **Valeurs de départ** [ORIGINAL] : ENV 3 0 / 0 / 80 ms / 0 / 0 ; LFO 1 en 1/8, RETRIG, forme en dents de scie → CUTOFF 50 % ; CUTOFF 30 %.
- **ENV 1** : 0 ms / 0 / 1 s / −3 dB / 200 ms [ORIGINAL].
- **FX** : aucun commenté dans la vidéo. Ici : Hyper/Dimension (Dimension 30 %) → Compressor Multiband MIX 40 % → Equalizer en High Pass à 180 Hz → Reverb Plate MIX 15 % [ORIGINAL].
- **Macros** : `Tone` CUTOFF 15 → 60 % · `Motion` ENV 3 → CRS 0 → ±24 · `Dirt` DRIVE 0 → 50 · `Space` MIX de la Plate 0 → 30 %.
- **Jeu** : accords écrits en MIDI (début de la vidéo), MIDI 57 à 76 ; deux oscillateurs à 9 voix sur un accord de quatre notes = 72 voix : vérifier la charge.
- **Test** : 22 demi-tons en 80 ms s'entendent comme un « zip » ; en dessous de 40 ms, comme un clic.

### AC08 Keys nu disco à pan aléatoire
- **Patch** [SOURCE CH-08] :
  - OSC A : scie [ASR « moog saw », peut-être « MG Saw »] ; ENV 1 en forme de pluck.
  - **Étalement polyphonique** : matrice, **NoteOn Rand 1 → PAN** d'OSC A, à la place de l'unison. Chaque note d'un accord tombe à un endroit différent.
  - FILTER 1 **Low 24**, avec sa propre enveloppe (decay court, release plus long) → CUTOFF ; la même enveloppe → LEVEL d'un NOISE (bruit personnalisé dans la vidéo ; ici un bruit d'usine au choix).
- **Valeurs de départ** [ORIGINAL] : NoteOn Rand 1 → PAN ±35 ; ENV 2 0 / 0 / 250 ms / 0 / 400 ms → CUTOFF 45 % et → LEVEL du NOISE 20 % ; CUTOFF 30 %.
- **ENV 1** : 0 ms / 0 / 600 ms / −14 dB / 350 ms [ORIGINAL].
- **FX** [SOURCE CH-08] : Hyper/Dimension (Dimension) → Chorus discret → Reverb **Hall**.
- **Hors de Serum** : Decimort et RC-20 dans la vidéo, présence non vérifiée ; ici une Distortion **Downsample** interne à MIX 15 % pour le côté lo-fi [DÉDUCTION].
- **Macros** : `Tone` CUTOFF 15 → 55 % · `Motion` NoteOn Rand 1 → PAN 0 → ±50 · `Dirt` MIX du Downsample 0 → 30 % · `Space` MIX de la Hall 10 → 35 %.
- **Jeu** : accords de quatre notes en croches décalées, MIDI 55 à 79 ; la vidéo automatise CUTOFF et RES sur le morceau.
- **Test** : en mono, le pan aléatoire disparaît sans perte de niveau, contrairement à un unison désaccordé.

### AC09 Accords qui plient
- **Source** : vidéo **écartée** de l'étude, faute de genre prioritaire (LÄMMERFYR, « UK Garage Chords », 0dXHNoi4Lm4), mais citée avec ses valeurs dans la section « Écartés » des accords. Marquée **[SOURCE écartée]**.
- **Patch** [SOURCE écartée] : sinus, **UNISON 5** ; ENV 2 → **Main Tuning**, plage **12 demi-tons** : les accords « plient » ; WARP **Bend +** ; Distortion **Downsample**.
- **Valeurs de départ** [ORIGINAL] : DETUNE 0,1 ; ENV 2 0 / 0 / 120 ms / 0 / 0, vers Main Tuning −3 demi-tons (départ un peu sous la note) ; Bend + 30 % ; Downsample DRIVE 15, MIX 25 %.
- **ENV 1** : 2 ms / 0 / 700 ms / −16 dB / 250 ms [ORIGINAL].
- **FX** : Distortion Downsample → Equalizer en High Pass à 150 Hz → Reverb Plate MIX 15 %.
- **Macros** : `Tone` Bend + 0 → 60 % · `Motion` ENV 2 → Main Tuning 0 → −12 · `Dirt` DRIVE du Downsample 0 → 40 · `Space` MIX de la Plate 0 → 30 %.
- **Jeu** : accords de septième en rythme garage (2-step), MIDI 57 à 76.
- **Test** : une glissade de plus de 3 demi-tons sur un accord entier sonne comme une bande qui ralentit ; doser `Motion`.

### AC10 Keys afro en FM
- **Le corpus n'a aucun tutoriel d'accords afro house** (section « Manque »). Recette **[ORIGINAL]** ; pour un vrai piano électrique, voir `../../../studio-grade-funk-keys-synth-sound-design/SKILL.md`.
- **Patch** :
  - OSC A : sinus. OSC B : sinus, OCT +1, **LEVEL 0**, modulateur.
  - OSC A, WARP 1 **FM (B)** à 0 ; ENV 2 → FM (B) 35 % : 0 / 0 / 250 ms / 10 % / 300 ms. L'attaque est brillante, le corps doux.
  - VOICING POLY 8 ; RAND 0.
- **ENV 1** : 2 ms / 0 / 1,5 s / −18 dB / 400 ms.
- **FX** : Chorus MIX 20 % → Equalizer en High Pass à 140 Hz → Delay 1/8 pointée, MIX 15 % → Reverb Plate MIX 15 %.
- **Delay** [CALCUL] : à 122 BPM, 1/8 pointée = 368,9 ms.
- **Macros** : `Tone` FM (B) de repos 0 → 15 % · `Motion` ENV 2 → FM (B) 15 → 60 % · `Dirt` Distortion Tube DRIVE 0 → 30 · `Space` MIX du Delay 0 → 25 %.
- **Jeu** : accords de septième et neuvième en rythme syncopé, MIDI 57 à 79.
- **Test** : sans source vidéo ; à comparer à AC02 et AC08 à niveau égal.

### AC11 Stab feutré sous 124
- **Recette [ORIGINAL]** pour la règle « Signature sous 124 BPM » d'`AGENTS.md` : un accord doux à côté du kick de la signature (`../../../drums-signature/references/signature.md`).
- **Patch** :
  - OSC A : scie, UNISON 3, DETUNE 0,05, RAND 100. OSC B : sinus, LEVEL 50 %.
  - FILTER 1 **MG Low 24** sur A, CUTOFF 18 %, RES 5 %.
  - ENV 2 → CUTOFF 35 % : ATK **15 ms**, DEC 300 ms, SUS 10 %, REL 300 ms. L'attaque du filtre adoucit le stab sans le rendre mou.
- **ENV 1** : 5 ms / 0 / 800 ms / −12 dB / 350 ms.
- **Règle 1 de `plucks.md`** [CALCUL] : 300 / 800 ms = 38 % ; le filtre tombe bien avant le volume.
- **FX** : Chorus MIX 20 % → Distortion Tape Sat. DRIVE 10, MIX 30 % → Equalizer en High Pass à 160 Hz → Reverb Plate MIX 18 %.
- **Macros** : `Tone` CUTOFF 10 → 40 % · `Motion` ATK d'ENV 2 0 → 40 ms · `Dirt` DRIVE de la Tape Sat. 0 → 30 · `Space` MIX de la Plate 10 → 35 %.
- **Jeu** : accords de neuvième espacés, une à deux attaques par mesure, MIDI 57 à 76.
- **Test** : sans source vidéo ; à valider avec le kick de la signature.

### AC12 Stab FM à quinte dessinée
- **Même vidéo que HK11** (CH-09 = HO-10). La recette complète est dans `hooks.md`, HK11. Ce qui change ici :
  - **Le second LFO** : l'étude des accords le lit sur le **RATE du LFO 1**, celle des hooks sur le CRS (« core speech » [ASR]). Variante AC12 : le second LFO, unipolaire, courbe courte, mode ENVELOPE → RATE du LFO 1 : l'enveloppe de niveau accélère à l'attaque [DÉDUCTION].
  - **L'accord** [CALCUL] : la table de B contient la quinte (harmonique 3) ; chaque note porte déjà sa quinte. Jouer des notes seules ou des tierces, pas des triades complètes (règle 1).
- **Macros** : celles de HK11.
- **Test** : comparer les deux lectures du second LFO à l'écran, puis garder celle de la vidéo.

### AC13 Keys liquid en sinus
- **Patch** [SOURCE CH-10] :
  - OSC A : sinus ; ENV 1 SUS 0, DEC **≈ 108** [ms, ASR], point de courbe monté, un peu d'ATK.
  - OSC B : sinus, **+1 octave**, LEVEL plus bas.
- **ENV 1** : 3 ms / 0 / 108 ms / 0 / 150 ms [SOURCE CH-10 pour DEC, le reste ORIGINAL]. Avec un decay aussi court, la traîne vient du delay et de la reverb.
- **FX** [SOURCE CH-10] : Delay **1/8**, filtre **≈ 1700 Hz**, MIX monté, FEEDBACK pour une traîne plus longue → Reverb « rêveuse ».
- **Valeurs de départ** [ORIGINAL] : Delay FEEDBACK 45 %, MIX 35 % ; Reverb Hall, DECAY 4 s, MIX 30 % ; Equalizer en High Pass à 140 Hz.
- **Delay** [CALCUL] : à 174 BPM, 1/8 = 172,4 ms.
- **Voicing** [SOURCE CH-10] : do mineur 7 ; après quatre mesures, le même accord avec l'octave de la fondamentale en plus ; à la dernière mesure, si bémol avec son octave, en gardant le do comme note de mélodie. [CALCUL] Si bémol avec do au-dessus = Bb add9.
- **Hors de Serum** [SOURCE CH-10] : couche de piano à queue avec beaucoup de reverb ; keys resamplées à −12 demi-tons, inversées, en fin de mesure. Ici : `../../../resampling/SKILL.md` pour la prise et l'inversion.
- **Macros** : `Tone` LEVEL d'OSC B 20 → 70 % · `Motion` DEC d'ENV 1 80 → 300 ms · `Dirt` Distortion Sine Shaper 0 → 25 · `Space` FEEDBACK du Delay 20 → 60 %.
- **Jeu** : voir la grille DnB liquide ; MIDI 60 à 79.
- **Test** : le filtre du delay à 1,7 kHz assombrit les répétitions ; vérifier qu'elles ne brouillent pas le break.

### AC14 Accords liquid de 7e et 9e
- **Patch** [SOURCE CH-11] :
  - OSC A : scie de base, accords calqués sur la basse et joués **deux octaves plus haut**.
  - FILTER 1 passe-bas à plusieurs pôles (plus de pôles = plus rond), un peu de RES, DRIVE, FAT ; MAIN baissé (cinq notes).
  - ENV 2 → CUTOFF avec une **attaque** : balayage montant. LFO 1 → CUTOFF faible, 1/4 ou en Hz.
  - **UNISON ≈ 6** ; **RAND gardé** (plus épais).
  - OSC B : table **spectrale**, routée au filtre, **+2 octaves** (essais +1 / −1).
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 20 %, RES 10 % ; ENV 2 300 ms / 0 / 1 s / 40 % / 600 ms vers CUTOFF 35 % ; LFO 1 en 1/4, ±5 %.
- **ENV 1** : 20 ms / 0 / 2 s / −3 dB / 800 ms [ORIGINAL].
- **Voicing** [SOURCE CH-11] : triades en empilant une touche blanche sur deux, puis la **7e**, puis la **9e** (« le liquid utilise 7e et 9e »). Doubler les fondamentales une octave plus bas ; la quinte doublée en bas a été essayée puis retirée.
- **FX** : Reverb + EQ ; coupe-bas dans EQ Eight à **220 Hz** (ou 110) dans la vidéo. Ici Equalizer interne en High Pass à 220 Hz ; 110 Hz si la basse laisse de la place.
- **Macros** : `Tone` CUTOFF 10 → 50 % · `Motion` ATK d'ENV 2 50 → 800 ms · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Reverb 10 → 40 %.
- **Jeu** : accords de cinq notes, une à deux mesures chacun, MIDI 52 à 79 ; voir la grille.
- **Test** : la doublure de la fondamentale une octave plus bas tombe vers 100-200 Hz ; si elle masque la basse médium, la retirer.

### AC15 Stab à formant spectral
- **Stab mono plutôt qu'accord voicé** (réserve de l'étude, CH-12).
- **Patch** [SOURCE CH-12] :
  - Table spectrale aux harmoniques « étranges », l'une des dernières de « Monster 1 » [ASR ?] : elle fixe le formant.
  - SUS 0 (pluck). LFO → FIN (trop rapide = phasing).
- **Valeurs de départ** [ORIGINAL] : ENV 1 0 / 0 / 250 ms / 0 / 100 ms ; LFO 1 à 0,5 Hz, ±6 cents.
- **FX** [SOURCE CH-12] : Filter **passe-bande** → Distortion **forte** → Chorus → Compressor (gain) → Equalizer qui coupe tout sauf les aigus → Reverb.
- **Valeurs** [ORIGINAL] : Filter Band 12, CUTOFF 1,5 kHz ; Distortion Diode 2, DRIVE 70 ; Equalizer en High Pass à 800 Hz.
- **Macros** : `Tone` CUTOFF du passe-bande 0,8 → 3 kHz · `Motion` WT POS sur les dernières frames 80 → 100 % · `Dirt` DRIVE 40 → 90 · `Space` MIX de la Reverb 0 → 20 %.
- **Jeu** : stabs ponctuels, MIDI 60 à 72.
- **Test** : la première moitié de la vidéo traite du sub ; elle n'est pas reprise.

### AC16 Accords « chaos saw »
- **Méthode** [SOURCE CH-13] : 170 BPM, La majeur, verrou de gamme. Les accords sortent de la basse : une octave plus haut, triades en sautant une note deux fois. **Renversement** : monter la tierce (la note du milieu) d'une octave, plus propre et plus plein. Les notes graves des accords sont coupées : la basse les tient.
- **Patch** [SOURCE CH-13] :
  - Scie (« chaos saw »), UNISON **+5**.
  - Serum 1 : onglet Global, Chaos à rate maximal, mode sample and hold ; Chaos 1 → CRS [ASR « chorus pitch »], quantité **20**. Serum 2 : un LFO de **TYPE S&H**, RATE au maximum en HZ → CRS (cartographie § 7.2 et § 13).
- **Le voicing** [CALCUL] : en La majeur, la triade La-Do♯-Mi devient La-Mi-Do♯ (racine, quinte, dixième) ; l'écart entre racine et tierce passe de 4 à 16 demi-tons.
- **Valeurs de départ** [ORIGINAL] : LFO 1 S&H à 200 Hz (×10 si nécessaire), vers CRS 3 % ; à 20 %, la hauteur se brouille, à vérifier.
- **ENV 1** : 10 ms / 0 / 2 s / −2 dB / 500 ms [ORIGINAL].
- **FX** [SOURCE CH-13] : EQ (coupe-bas, coupe-haut) et un « Wambo combo » [ASR] (EQ + OTT). Ici : Equalizer en High Pass à 200 Hz, Compressor Multiband MIX 40 %.
- **Couches de la vidéo** : un chœur (Sforzando, soundfont Roland) avec OTT, reverb ≈ 35 % et Utility ; une couche médium en carré à −12 demi-tons, filtre passe-haut, attaque lente. Ici, la couche médium : OSC B carré, SEM −12, LEVEL 40 %, ENV 3 en attaque lente sur son LEVEL [DÉDUCTION].
- **Macros** : `Tone` CUTOFF d'un MG Low 24 40 → 90 % · `Motion` S&H → CRS 0 → 10 % · `Dirt` GAIN du Multiband 0 → 10 dB · `Space` Reverb Hall MIX 10 → 40 %.
- **Jeu** : voir la grille melodic dubstep ; changements d'accords un demi-temps en avance (« en contretemps », CH-13).
- **Test** : le S&H sur la hauteur rend l'accord rugueux ; s'il paraît faux, baisser `Motion` avant tout.

### AC17 Mur d'accords désaccordé
- **Méthode** [SOURCE CH-14] : une pile de scies plus un sub est « ennuyeuse » ; empiler des couches (AC17 à AC19), accords voicés larges.
- **Patch** [SOURCE CH-14] : scie **9 voix**, DETUNE **≈ 22** [ASR, peut-être 0,22], **BLEND réglé pour que la voix centrale égale les autres**.
- **BLEND** [DÉDUCTION, cartographie § 3.1] : 75 % = mélange égal des voix centrales et latérales.
- **FX** [SOURCE CH-14] : Phaser (RATE, DEPTH, FREQ et FEEDBACK bas, peu de MIX) pour flouter les harmoniques ; aigus perçants atténués.
- **Valeurs de départ** [ORIGINAL] : DETUNE 0,22 ; Phaser MIX 20 % ; Equalizer, bande haute en High Shelf −4 dB à 6 kHz, bande basse en High Pass à 200 Hz.
- **ENV 1** : 5 ms / 0 / 3 s / −2 dB / 600 ms [ORIGINAL].
- **Macros** : `Tone` High Shelf −8 → 0 dB · `Motion` DETUNE 0,1 → 0,35 · `Dirt` Distortion Soft Clip 0 → 30 · `Space` MIX du Phaser 0 → 40 %.
- **Jeu** : accords larges de quatre à six notes, MIDI 52 à 84.
- **Test** : c'est l'élément large du drop (règle 6 de `leads.md`) ; vérifier en mono.

### AC18 Couche d'accords propre
- **Patch** [SOURCE CH-14] : scie **3 voix**, DETUNE **≈ 0,04**, Phaser, coupe-bas et coupe-haut.
- **Valeurs de départ** [ORIGINAL] : Phaser MIX 15 % ; Equalizer en High Pass à 220 Hz et en Low Pass à 10 kHz.
- **ENV 1** : 5 ms / 0 / 3 s / −2 dB / 600 ms [ORIGINAL], comme AC17.
- **Rôle** : elle donne la justesse que le mur d'AC17 perd en se désaccordant.
- **Macros** : `Tone` Low Pass 6 → 14 kHz · `Motion` DETUNE 0 → 0,1 · `Dirt` Distortion Tape Sat. 0 → 25 · `Space` MIX du Phaser 0 → 30 %.
- **Jeu** : les mêmes accords qu'AC17.
- **Test** : couper AC17 : AC18 seule doit garder l'harmonie lisible.

### AC19 Habillage du mur : sirène et arpège
- **Patch** [SOURCE CH-14] :
  - **Sirène aiguë** : scie très désaccordée, LFO → FIN à **8,2 Hz**, NOISE, DRIVE.
  - **Bruit stéréo** : NOISE pané à gauche, plus un oscillateur en **FM (B)** avec des tables « folles » (+4 octaves, hauteurs impaires) pané à droite.
  - **Arpège** : scie, enveloppe sur le LEVEL, Phaser, LFO → PAN en **1/4 triolet**.
- **Le pan** [CALCUL] : à 150 BPM, un quart de triolet dure 266,7 ms ; à 170 BPM, 235,3 ms.
- **Valeurs de départ** [ORIGINAL] : sirène UNISON 7, DETUNE 0,4, LFO → FIN ±15 cents, LEVEL −12 dB sous AC17 ; arpège ARP 1/16, Up, deux octaves ; LFO → PAN ±40.
- **Hors du patch** : deux instances de Serum (sirène et bruit ; arpège), sur deux pistes.
- **Macros** : `Tone` Low Pass de la sirène 4 → 16 kHz · `Motion` LFO → FIN 0 → ±25 cents · `Dirt` DRIVE 0 → 50 · `Space` LFO → PAN 0 → ±60.
- **Jeu** : la sirène tient la note la plus haute de l'accord ; l'arpège joue les notes de l'accord.
- **Test** : la vidéo conclut qu'il faut laisser de la place à la voix ; couper ces couches sous le chant.

### AC20 Wub future bass
- **Patch** [SOURCE CH-15] :
  - Recréation du preset « Power Saw » du pack Sunset : à n'utiliser qu'avec une licence vérifiée (règle « Droits » de `leads.md`).
  - OSC A : Basic Shapes, triangle. OSC B : Basic Shapes, carré. SUB actif dans la vidéo : ici OSC C, triangle, OCT −1, si l'accord reste au-dessus de MIDI 60 [ORIGINAL] ; sinon éteint.
  - LFO 1, courbe montée → LEVEL d'A, B (et C) : le « wub » de pompage. RATE = vitesse du wub, par exemple **1/8**.
  - NOISE « AC Hum » à bas niveau ; LFO 1 → LEVEL du NOISE ; PITCH du NOISE ajusté.
  - OSC A, WARP 1 **FM (B)** monté.
- **Le wub** [CALCUL] : à 150 BPM, 1/8 = 200 ms ; à 160 BPM, 187,5 ms.
- **ENV 1** : 2 ms / 0 / 2 s / 0 dB / 300 ms [ORIGINAL].
- **FX** [SOURCE CH-15] : Distortion **avant** Hyper/Dimension, DRIVE baissé → Hyper/Dimension (MIX et SIZE baissés, MIX de Dimension un peu monté) → Compressor **Multiband**, gains vers le haut remontés → Reverb (SIZE, LO CUT et HI CUT montés, MIX baissé : la traîne déborde sur le changement d'accord) → Equalizer en **High Pass**, Q baissé, qui coupe le sub.
- **Phase** [SOURCE CH-15] : RAND actif = des variations ; inactif = attaque identique à chaque note.
- **Hors de Serum** : chaîne parallèle « Flume » de la vidéo (EQ mid/side sur les côtés seuls, Utility, Spectral Blur de Live). Spectral Blur est un effet natif : remplacé par une Reverb interne sur BUS 1, en Splitter M/S, côté SIDE seulement [DÉDUCTION].
- **Macros** : `Tone` CUTOFF d'un MG Low 24 30 → 90 % · `Motion` LFO 1 → niveaux 0 → 100 % · `Dirt` FM (B) 0 → 40 % · `Space` MIX de la Reverb 5 → 30 %.
- **Jeu** : accords de quatre notes, une mesure chacun (la vidéo donne un MIDI en description, non repris), MIDI 57 à 79.
- **Test** : le wub doit tomber sur la grille ; LFO en RETRIG et RATE en divisions, jamais en Hz.

## Motifs de départ (grilles vérifiées)

Numérotation de Live (C3 = 60). Progressions et rythmes écrits ici. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/synths/accords.md`. Notation Producer Pal : `--fichier references/synths/accords.md --titre <titre> --format ppal`.

```grille
titre: House 122 — stab mineur dans une note (AC01)
tempo: 122
accords: Cm | Fm
stab: C4[1&:1] C4[2e:1] C4[2a:1] C4[3&:2] C4[4a:1] | F4[1&:1] F4[2e:1] F4[2a:1] F4[3&:2] F4[4a:1]
```

```grille
titre: Garage 124 — sinus en La mineur 7 (AC03)
tempo: 124
accords: Am7 | Dm7
haut: G4[1e:1] G4[2&:1] G4[3e:1] G4[4&:1] | F4[1e:1] F4[2&:1] F4[3e:1] F4[4&:1]
milieu: E4[1e:1] E4[2&:1] E4[3e:1] E4[4&:1] | C4[1e:1] C4[2&:1] C4[3e:1] C4[4&:1]
bas: C4[1:1] C4[2&:1] C4[3e:1] C4[4&:1] | A3[1:1] A3[2&:1] A3[3e:1] A3[4&:1]
```

```grille
titre: DnB liquide 174 — accords de 9e (AC13, AC14)
tempo: 174
accords: Am9 | Fmaj9
haut: B4[1:16] | G4[1:16]
milieu: G4[1:16] | E4[1:16]
bas: C4[1:16] | A3[1:16]
```

```grille
titre: Melodic dubstep 150 — tierce montée d'une octave (AC16)
tempo: 150
accords: A | F#m
haut: C#5[1:16] | A4[1:16]
bas: E4[1:16] | C#4[1:16]
```

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : « FM_Freak », « Basic MG », les tables Juno, le bruit d'orgue [ASR « Argan nose »], les dernières frames de « Monster 1 ». Lire le sens de la glissade d'AC07 et la cible du second LFO d'AC12.
- Vérifier la licence du pack Sunset avant de rapprocher AC20 du preset « Power Saw ».
- Écouter chaque recette (règle 10 de `leads.md`) avec la basse du morceau ; garder un ou deux sons d'accords par morceau et consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
- Fichiers suivants du lot : pads, drones.
