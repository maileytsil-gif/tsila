# Vingt recettes de hoover, foghorn et horn pour la Drum and Bass (famille F14)

Troisième lot DnB : les basses « cuivrées ».
- Le **foghorn** est une note grave et large qui s'ouvre lentement, faite de FM et de distorsion (Bou, Benny L).
- Le **horn** empile scies, quintes et octaves (analyse de « Baddadan » par Attack Magazine).
- Le **hoover** descend de la « Dominator » de l'Alpha Juno : trois carrés à l'octave, une forte PWM et du chorus.

Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F14-01 Antidote Audio (Serum 2), F14-02 MilleniumBE (Serum 1) ;
- `../etudes-pages-dubstep-dnb.md` : F14-03 ADSR Sounds (hoover), F14-09 Attack Magazine (« Baddadan », u-he Zebra 2), et la page foghorn d'Attack Magazine faite avec le Wavetable de Live (hors registre) ;
- `../etudes-captures.md` (F14-09, motif MIDI) ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot DnB** : celles de `dnb-f13-neuro.md` (174 BPM, schéma 2-step, sub séparé, octaves, RAND, MONO et LEGATO, resampling, contrôle).
2. **Le grave du foghorn reste au sub.** Attack Magazine met le sinus de sub « sur la même note, piste séparée » et laisse le sub hors de la distorsion [SOURCE page foghorn ; F14-09 : « un sub constant à part »]. MilleniumBE met un SUB à −1 octave en `Direct` dans le patch [SOURCE F14-02] ; ici, ce rôle passe au sub de sa piste.
3. **Traductions.** Deux sources ne sont pas faites dans Serum : Zebra 2 (F14-09) et le Wavetable de Live (page foghorn). Leurs valeurs sont dans les unités de ces synthés ; leur passage dans Serum 2 est une [DÉDUCTION] à régler à l'oreille. Leurs effets natifs de Live (Drum Buss, Saturator, Limiter, Compressor, EQ Eight) sont remplacés par les effets internes de Serum 2 ou par des plug-ins tiers (règle 6 d'`ableton-live-session`).
4. **Rapports FM du foghorn d'Antidote** [CALCUL] :
   - B à +1 octave et +4 demi-tons (16 demi-tons) est au rapport 2,52, à 13,7 cents de 5:2 : le spectre est presque harmonique, avec un léger frottement ;
   - B à +1 octave et +7 demi-tons (19 demi-tons) est au rapport 2,997, à −1,96 cent de 3:1 : spectre harmonique, plus « cuivre ».
5. **Durées des enveloppes lentes à 174 BPM** [CALCUL] :
   - 2,42 s (ENV 2 de MilleniumBE) = 1,75 mesure ;
   - 4,2 s (Env 2 d'Attack Magazine) = 3,05 mesures ;
   - 850 ms (release d'Attack Magazine) = 2,5 noires.

   Une enveloppe de filtre plus longue que la note n'arrive jamais au bout : le timbre dépend de la longueur jouée.
6. **Quatre macros communes** [ORIGINAL] :
   - `FM` : quantité de FM ou de PD ;
   - `Open` : coupure du filtre ou quantité d'ENV 2 sur la coupure ;
   - `Grit` : drive de la distorsion principale ;
   - `Width` : Hyper/Dimension ou unison, au-dessus du split seulement.

   Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| HF01 | Foghorn Antidote | référence | 3 sinus en chaîne de PD, Comb 2 |
| HF02 | Foghorn Antidote en quinte | variante cuivre | B à +19 demi-tons, rapport 3:1 |
| HF03 | Foghorn MilleniumBE | foghorn façon Bou | PWM DS, unison 7 à largeur 0, FM (B) |
| HF04 | Foghorn Attack Magazine | foghorn lent | FM deux octaves au-dessus, LP 200 Hz |
| HF05 | Horn à la quinte | horn de drop | scies 0, +7, +19, filtre presque fermé |
| HF06 | Hoover Alpha Juno | hoover rave | trois carrés à l'octave, PWM, chorus |
| HF07 | Hoover à l'unison empilé | hoover compact | un carré, STACK 12, PWM |
| HF08 | Hoover qui plonge | attaque de note | chute de hauteur à l'attaque |
| HF09 | Hoover imprimé en table | hoover maison | table faite d'une note imprimée |
| HF10 | Foghorn en Ratio | foghorn accordé | B en mode Ratio, rapports entiers |
| HF11 | Foghorn à enveloppe longue | notes tenues | ENV 2 de 2,42 s sur la coupure |
| HF12 | Foghorn mono | grave net | unison à largeur 0 |
| HF13 | Horn distordu par bandes | drop | Splitter L/M/H, grave peu saturé |
| HF14 | Foghorn à trois LFO | foghorn vivant | FM, désaccord et niveau sur 2 mesures |
| HF15 | Foghorn court | stabs | ENV 1 courte, notes d'une double croche |
| HF16 | Horn à l'unison 12+7 | horn compact | une scie, STACK 12+7 |
| HF17 | Foghorn au peigne accordé | tonique qui tape | Comb 2 réglé sur la tonique |
| HF18 | Foghorn glissé | lignes liées | MONO, LEGATO, portamento |
| HF19 | Foghorn à queue de réverb | fin de phrase | reverb qui monte en fin de note |
| HF20 | Foghorn qui s'ouvre avant la frontière | variation avant la frontière | `FM` et `Open` automatisés |

## Les vingt recettes

### HF01 Foghorn Antidote — référence du fichier
- **Patch** :
  - **OSC A** : sinus (Default Shapes), OCT −2, seul oscillateur audible.
  - **OSC B** : sinus, OCT +1, SEM +4, LEVEL 0 (source de modulation).
  - **OSC C** : sinus, octave en mode Ratio (clic droit sur OCT), rapport 4,000, LEVEL 0.
  - **Chaîne de modulation** « à l'ancienne » : A reçoit de B, B reçoit de C. L'écran montre PD (B) sur A et PD (C) sur B ; la voix dit « frequency modulation ». Garder la PD de l'écran, essayer la FM.
  - **LFO 1** : triangle, RETRIG, 2 mesures → quantité de modulation de A.
  - **Unison 2 sur B**, WIDTH 0 ; LFO 2 (2 mesures, rampe montante puis retour) → DETUNE de B.
  - **LFO 3** : 2 mesures, forme dessinée (montée rapide, plateau descendant, chute) → LEVEL de B ; dernière quantité de modulation vers « 4 ».
  - **FILTER 1** : Comb 2 (type nouveau de Serum 2) ; ses résonances favorisent certaines notes : petit réglage pour que le fa tape.
  - MONO + LEGATO, PORTAMENTO (écran).
- **ENV 1** : non dite. Attaque 2 ms, sustain 100 %, release 120 ms [ORIGINAL].
- **FX** :
  1. Distortion Diode 1 (Diode 2 essayée), filtre de distorsion OFF.
  2. Distortion Stomp Box.
  3. Compressor Multiband : −18,1 dB, 4:1, attaque et release 90,1, gain 9,7, bandes à 128 et 2 500 Hz ; médiums un peu baissés.
  4. Reverb Plate large (LO CUT 45, HI CUT 0).
- **Macros** : `FM` quantité de PD de A · `Open` FRQ2 ou CUTOFF du Comb 2 · `Grit` DRIVE de la Diode 1 · `Width` MIX de la Reverb.
- **Sub associé** : S01, même ligne.
- **Jeu** : bloc « DnB 174 — foghorn en notes longues » ci-dessous.
- **Test** : la tonique doit taper plus fort que les autres notes à cause du Comb 2 ; jouer toute la ligne.
- **Origine** : [SOURCE F14-01, Antidote Audio, transcription et quatre captures, Serum 2]. Le saturateur placé sur le master de la session n'est pas repris.

### HF02 Foghorn Antidote en quinte — B à +19 demi-tons
- **Patch** : HF01, avec OSC B passé de SEM +4 à SEM +7 (OCT +1).
- **Calcul** : 19 demi-tons = rapport 2,997, presque 3:1 ; le spectre devient harmonique, sans le frottement des 16 demi-tons (règle 4) [CALCUL].
- **ENV 1** : comme HF01.
- **Macros** : celles de HF01.
- **Sub associé** : S01.
- **Origine** : « B passé de +4 à +7 demi-tons pour une variante » [SOURCE F14-01, 4:58].

### HF03 Foghorn MilleniumBE — façon Bou
- **Patch** :
  - **OSC A** : table Analog « PWM DS », WT POS 40 (100 au départ), Unison 7, DETUNE et BLEND par défaut, WIDTH d'unison à 0 (mono, contre les problèmes de phase), OCT −1.
  - **OSC B** : sinus (« Analog_BD_Sin »), OCT +2, LEVEL baissé ; WARP de A en FM (B).
  - **NOISE** : « BrightWhite », niveau et PITCH ajustés, pour plus d'aigus.
  - **FILTER 1** : Low 24 sur A et noise, DRIVE, FAT, RES. La source y route aussi un SUB sinus à −1 octave en `Direct` ; **ici, SUB éteint**.
  - **ENV 2** → CUTOFF (écran) : attaque 132 ms, hold 0, decay 2,42 s, sustain 0 %, release 15 ms ; courbe ajustée ; modulation unipolaire ; coupure de base ≈ 30 Hz, quantité montée (« 26 » dit).
- **ENV 1** : non lue ; attaque 2 ms, sustain 100 %, release 100 ms [ORIGINAL].
- **FX** :
  1. Hyper/Dimension, RATE et DETUNE un peu baissés.
  2. Distortion Tube, DRIVE poussé.
  3. Reverb Hall : LO CUT monté, HI CUT baissé, SPIN baissé.
  4. Compressor en mode normal, pas multibande (« garder le grain du grave ») : attaque presque à 0, release un peu montée, gain ≈ 7 dB.
  5. Equalizer : léger boost des aigus (écran : 3,2 dB), Q baissé.
- **Calcul** : 132 ms = 1,5 double croche ; la coupure s'ouvre en 1,75 mesure [CALCUL, règle 5].
- **Macros** : `FM` quantité de FM (B) · `Open` quantité d'ENV 2 → CUTOFF · `Grit` DRIVE de la Tube · `Width` MIX de l'Hyper.
- **Sub associé** : S01.
- **Test** : chercher le bon couple position de table / quantité de FM ; les niveaux des couches s'automatisent à volonté (HF20).
- **Origine** : [SOURCE F14-02, MilleniumBE, transcription et trois captures, Serum 1, FL Studio]. Le post-traitement de FL Studio (Waveshaper, EQ coupe-bas vers 84 Hz, delay) n'est pas repris.

### HF04 Foghorn Attack Magazine — FM deux octaves au-dessus
- **Patch** (traduit du Wavetable de Live) :
  - **OSC A** : table de scie (la source : `Saw Dual 3`, position vers la moitié), OCT 0 ; la note jouée est F0 dans la source, ici F1 à OCT 0 avec un sub à part.
  - **OSC B** : sinus, OCT +2, LEVEL 0 ; WARP de A en FM (B), quantité ≈ 30 % (la source : modulant « 100 % » = deux octaves au-dessus, amount ≈ 30 %).
  - **FILTER 1** : Low 24, CUTOFF ≈ 200 Hz, RES ≈ 25 %.
  - **ENV 2** : attaque 23 ms, decay 4,2 s, sustain 0, release 600 ms → CUTOFF (+30 %) et → WT POS (+15 %, vers le carré).
  - **Unison** : 3 voix, MODE Random, DETUNE ≈ 30 % (la source : mode « Noise » du Wavetable, sans équivalent nommé dans Serum 2) [DÉDUCTION].
- **ENV 1** : attaque 0, decay très long (« 17 s » écrit, coquille possible), sustain −∞, release 850 ms. Dans Serum 2 : attaque 0,5 ms, decay au maximum ou sustain 100 %, release 850 ms [DÉDUCTION].
- **FX** :
  1. Splitter L/M/H, séparations ≈ 200 Hz et ≈ 2 kHz : LOWS Distortion Soft Sat. légère ; MIDS Distortion Overdrive, DRIVE élevé ; HIGHS Distortion Tape Sat. forte.
  2. Compressor : seuil −28,6 dB, ratio ≈ 4,85:1.
  3. Equalizer : grave retiré sous 100 Hz, petite bosse vers 4,85 kHz, étagère qui coupe l'extrême aigu (place pour la batterie).
  4. Hyper/Dimension pour la largeur (la source utilise StereoDelta) ; la reverb (Valhalla Supermassive dans la source) passe en envoi par plug-in tiers.
- **Macros** : `FM` quantité de FM 15 → 45 % · `Open` quantité d'ENV 2 → CUTOFF · `Grit` DRIVE de l'Overdrive des MIDS · `Width` MIX de l'Hyper.
- **Sub associé** : S01, même note, piste séparée [SOURCE].
- **Test** : la page conseille de moduler la FM par une enveloppe ou un LFO one-shot, de baisser un peu la coupure à la fin et d'essayer d'autres tables une fois la distorsion en place.
- **Origine** : [SOURCE page « Drum ‘n’ Bass Foghorn Bass With Wavetable », Attack Magazine, Wavetable de Live, toutes les valeurs écrites] ; traduction dans Serum 2 [DÉDUCTION].

### HF05 Horn à la quinte — d'après l'analyse de « Baddadan »
- **Patch** (traduit de Zebra 2) :
  - **OSC A** : scie, OCT 0, LEVEL ≈ 32 %.
  - **OSC B** : scie, SEM +7 (quinte), LEVEL ≈ 32 %.
  - **OSC C** : scie, SEM +19 (octave et quinte), LEVEL au maximum.
  - **FILTER 1** sur A, B, C : MG Low 24 (la source : LP Vintage), CUTOFF presque fermé (≈ 10 sur 100 dans Zebra ; ici ≈ 150-250 Hz à régler) [DÉDUCTION], DRIVE ≈ 15 %.
  - **ENV 2** → CUTOFF, quantité ≈ 70 % ; attaque courte (« 9 heures »), sustain 0, release à mi-course.
  - **Suivi de clavier** : matrice Note# → CUTOFF ≈ +35 % (filtre fermé dans le grave, plus ouvert dans l'aigu) [DÉDUCTION : KeyFol ≈ 35 de Zebra].
  - **SUB** : sinus, OCT 0, routé `Direct` (hors filtre et hors distorsion), LEVEL 0, ENV 3 → LEVEL au maximum ; ENV 3 avec une attaque de ≈ 30 ms puis une chute rapide : il donne un fondamental serré. Ce SUB joue la hauteur de la note (F2 ≈ 175 Hz dans la source) : ce n'est pas le sub du morceau [DÉDUCTION].
  - VOICING : MONO, LEGATO décoché (la source : « retrigger », « une basse, pas de polyphonie »).
- **ENV 1** : release ≈ 40 (échelle de Zebra) ; ici 40 ms [DÉDUCTION].
- **FX** :
  1. Distortion forte (la source : Shape Wedge, depth presque au maximum, Edge ≈ 30 ; sans équivalent nommé : essayer Diode 2 ou Lin. Fold) [DÉDUCTION].
  2. Equalizer : léger creux vers 225 Hz, légère bosse vers 3 kHz.
  3. Saturation et limiteur par plug-ins tiers (la source finit par Drum Buss, Saturator et Limiter de Live, refusés par la règle 6).
- **Calcul** : +19 demi-tons ≈ 3:1 (règle 4) : la troisième harmonique de la note est renforcée [CALCUL].
- **Macros** : `FM` LEVEL de C (la couche +19) · `Open` quantité d'ENV 2 → CUTOFF · `Grit` DRIVE de la distorsion · `Width` —.
- **Sub associé** : S01, constant, piste séparée [SOURCE : « un sub constant à part »].
- **Jeu** : bloc « DnB 174 — horn en doubles croches » ci-dessous, motif original. Le motif de « Baddadan » relevé dans `../etudes-captures.md` n'est pas reproduit (règle « Référence » d'`AGENTS.md` : ne jamais copier une mélodie).
- **Origine** : [SOURCE F14-09, Attack Magazine, page lue et trois captures, u-he Zebra 2, 174 BPM] ; traduction [DÉDUCTION]. La page décrit le résultat comme « une Reese grasse, dans les médiums ».

### HF06 Hoover Alpha Juno — trois carrés à l'octave
- **Patch** :
  - **OSC A**, **OSC B**, **OSC C** : carrés (Basic Shapes), OCT −1, 0 et +1.
  - **WARP** PWM sur les trois ; LFO 1 (triangle, 1/2, FREE) → quantité de PWM (+60 %), avec un décalage de phase différent par oscillateur.
  - **FILTER 1** : MG Low 12, CUTOFF 2 kHz, RES 10 %.
  - MONO + LEGATO, PORTAMENTO 60 ms.
- **ENV 1** : attaque 5 ms, sustain 100 %, release 150 ms.
- **FX** : Chorus, MIX 50 % ; Distortion Tube légère ; passe-haut à 120 Hz.
- **Macros** : `FM` quantité de PWM · `Open` CUTOFF · `Grit` DRIVE · `Width` MIX du Chorus.
- **Sub associé** : S01.
- **Origine** : définition d'origine de la Hoover (« Dominator » de l'Alpha Juno) : trois oscillateurs carrés empilés à l'octave, forte PWM, chorus [SOURCE F14-03, page ADSR] ; warp PWM [cartographie, § 4.1] ; valeurs [ORIGINAL]. Le preset gratuit d'ADSR (Serum 1, 2014) n'a pas été ouvert.

### HF07 Hoover à l'unison empilé — un seul carré
- **Patch** :
  - **OSC A** : carré, OCT 0, Unison 3, STACK « 12 (1x) » : les voix se répartissent entre la note et l'octave au-dessus.
  - **WARP** PWM, LFO 1 (1/2, FREE) → quantité.
  - **FILTER 1** : MG Low 12, CUTOFF 2 kHz.
- **ENV 1** : comme HF06.
- **FX** : Chorus 50 % ; passe-haut à 120 Hz.
- **Macros** : `FM` quantité de PWM · `Open` CUTOFF · `Grit` DRIVE d'une Tube · `Width` DETUNE d'unison.
- **Sub associé** : S01.
- **Test** : A/B avec HF06 ; STACK 12 « 2x » ajoute l'octave suivante.
- **Origine** : STACK d'unison de Serum 2 (octaves et quintes empilées sans jouer d'accord) [cartographie, § 3.1] ; recette [ORIGINAL] d'après HF06.

### HF08 Hoover qui plonge — chute de hauteur à l'attaque
- **Patch** : HF06, avec ENV 3 → hauteur globale (Main Tuning ou CRS des trois oscillateurs), départ +3 demi-tons, decay 120 ms, sustain 0 : la note tombe sur sa hauteur.
- **ENV 1** : comme HF06.
- **Macros** : celles de HF06 ; `Open` peut piloter la profondeur de la chute (0 → +5 demi-tons).
- **Sub associé** : S01, **sans** chute de hauteur.
- **Test** : la chute ne doit pas brouiller la note sur les attaques rapprochées.
- **Origine** : [ORIGINAL]. Aucun tutoriel étudié ne décrit ce geste ; il reste une proposition.

### HF09 Hoover imprimé en table — la table maison
- **Patch** :
  1. Construire HF06, imprimer une note tenue de 2 mesures (procédure de `../../../resampling/SKILL.md`).
  2. La remettre dans OSC A comme table : chaque frame garde un état de la PWM et du chorus.
  3. LFO 1 → WT POS (2 mesures, RETRIG).
- **ENV 1** : comme HF06.
- **Macros** : `FM` profondeur de LFO 1 → WT POS · `Open` CUTOFF · `Grit` DRIVE · `Width` MIX d'un Chorus.
- **Sub associé** : S01.
- **Origine** : ADSR part d'une wavetable maison « à frames riches en harmoniques », faite pour les hoovers [SOURCE F14-03] ; table imprimée [ORIGINAL], comme DR16 de `dnb-f02-reese.md`.

### HF10 Foghorn en Ratio — rapports entiers
- **Patch** : HF01, avec OSC B aussi en mode Ratio : rapport 3,000 (au lieu de +16 demi-tons) ; OSC C à 4,000.
- **Calcul** : les composantes fc ± n·fm tombent alors sur des harmoniques de la note (rapports entiers) : le foghorn reste accordé quelle que soit la note [CALCUL].
- **ENV 1** : comme HF01.
- **Macros** : celles de HF01 ; `Open` → rapport de B (2,000 → 4,000) pour une variante.
- **Sub associé** : S01.
- **Origine** : mode Ratio de C chez Antidote [SOURCE F14-01] ; étendu à B [ORIGINAL] ; mode Ratio [cartographie, § 3.1].

### HF11 Foghorn à enveloppe longue — le filtre qui s'ouvre
- **Patch** : HF03 ou HF04, avec l'ENV 2 de MilleniumBE → CUTOFF : attaque 132 ms, decay 2,42 s, sustain 0, unipolaire.
- **Calcul** : 2,42 s font 1,75 mesure à 174 BPM [CALCUL]. Une note d'une mesure finit avant que le filtre se referme ; seules les tenues de deux mesures font tout le geste.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 100 ms.
- **Macros** : `Open` decay d'ENV 2 (1 → 3 s) · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Jeu** : tenues d'une à deux mesures.
- **Origine** : [SOURCE F14-02, écran 10:00].

### HF12 Foghorn mono — unison à largeur 0
- **Patch** : HF03 avec WIDTH d'unison à 0 sur A et B, sans Hyper ni Chorus.
- **ENV 1** : comme HF03.
- **Macros** : celles de HF03 ; `Width` —.
- **Sub associé** : S01.
- **Test** : A/B avec HF03 ; si la largeur manque, l'ajouter au-dessus de 200 Hz seulement (HF13).
- **Origine** : « largeur d'unison des osc 1 et 2 à 0 (mono : évite les problèmes de phase) » [SOURCE F14-02] ; variante [ORIGINAL].

### HF13 Horn distordu par bandes — le grave peu saturé
- **Patch** : HF01, HF03 ou HF05, puis le Splitter L/M/H de HF04 :
  - LOWS (sous 200 Hz) : Soft Sat. légère ;
  - MIDS (200 Hz-2 kHz) : Overdrive à fond ;
  - HIGHS (au-dessus de 2 kHz) : Tape Sat.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Grit` DRIVE de l'Overdrive des MIDS · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Origine** : distorsion multibande, grave saturé avec mix plein mais à part, crossover ≈ 200 Hz et ≈ 2 kHz [SOURCE page foghorn d'Attack Magazine, Waves MultiMod Rack] ; transposée dans le Splitter de Serum 2 [DÉDUCTION].

### HF14 Foghorn à trois LFO — FM, désaccord et niveau
- **Patch** : HF01, en gardant ses trois LFO sur 2 mesures, RETRIG :
  - LFO 1 triangle → quantité de modulation de A ;
  - LFO 2 rampe montante puis retour → DETUNE de B ;
  - LFO 3 forme dessinée → LEVEL de B.
- Décaler la phase de départ de LFO 2 d'un quart de cycle (une demi-mesure) pour que les gestes ne culminent pas ensemble [ORIGINAL].
- **ENV 1** : comme HF01.
- **Macros** : `FM` AUX de LFO 1 · `Open` AUX de LFO 3 · `Grit` · `Width` comme HF01.
- **Sub associé** : S01.
- **Origine** : [SOURCE F14-01] ; décalage de phase [ORIGINAL].

### HF15 Foghorn court — stabs
- **Patch** : HF01 ou HF03, avec ENV 1 : attaque 0,5 ms, decay 150 ms, sustain −∞, release 30 ms ; LFO en RETRIG à 1/8.
- **ENV 1** : ci-dessus.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01 en notes longues sous les stabs.
- **Jeu** : bloc « DnB 174 — horn en doubles croches » ci-dessous.
- **Origine** : stabs du jump-up (famille F06 de ce lot) ; variante [ORIGINAL].

### HF16 Horn à l'unison 12+7 — une scie, la quinte comprise
- **Patch** :
  - **OSC A** : scie, OCT 0, Unison 3, STACK « 12+7 (1x) » : note, quinte et octave.
  - FILTER 1, ENV 2 → CUTOFF et MONO comme HF05.
- **ENV 1** : comme HF05.
- **Macros** : `FM` DETUNE d'unison · `Open` quantité d'ENV 2 → CUTOFF · `Grit` DRIVE · `Width` —.
- **Sub associé** : S01.
- **Test** : A/B avec HF05 ; trois oscillateurs donnent des niveaux séparés que le STACK ne donne pas.
- **Origine** : STACK 12+7 [cartographie, § 3.1] ; empilement scie, quinte, octave et quinte [SOURCE F14-09] ; recette [ORIGINAL].

### HF17 Foghorn au peigne accordé — la tonique qui tape
- **Patch** : HF01, avec le CUTOFF du Comb 2 réglé sur une harmonique de la tonique : pour F, 349,2 Hz (F3, MIDI 65, quatrième harmonique de F1).
- **Calcul** : F1 = 87,31 Hz ; 4 × 87,31 = 349,2 Hz [CALCUL]. Les notes dont les harmoniques tombent sur les dents du peigne ressortent, les autres moins.
- **ENV 1** : comme HF01.
- **Macros** : `Open` FRQ2 du Comb 2 · les autres comme HF01.
- **Sub associé** : S01.
- **Test** : jouer la gamme de la ligne et noter les notes qui ressortent ; la valeur exacte du CUTOFF se lit dans Serum.
- **Origine** : « ses résonances favorisent certaines notes : petit réglage pour que le fa tape » [SOURCE F14-01, 3:51] ; accord par le calcul [ORIGINAL].

### HF18 Foghorn glissé — notes liées
- **Patch** : HF03, avec MONO + LEGATO, PORTAMENTO 120 ms, ALWAYS décoché.
- **Calcul** : 120 ms font 1,4 double croche à 174 BPM [CALCUL].
- **ENV 1** : comme HF03.
- **Macros** : `Open` PORTA (60 → 250 ms) à la place de la coupure, au choix.
- **Sub associé** : S01 sans glissé.
- **Jeu** : chevauchements d'un quart de double croche, comme le bloc « neuro glissé à l'octave » de `dnb-f13-neuro.md`.
- **Origine** : mono, legato et portamento [SOURCE F14-01, écran 4:42] ; valeur [ORIGINAL].

### HF19 Foghorn à queue de réverb — la traîne qui arrive
- **Patch** : HF01, avec Reverb Plate, LO CUT 45, MIX sur LFO 4 en mode ENVELOPE, 4 mesures, synchronisé : la réverb monte au cours de la note.
- **ENV 1** : release 300 ms.
- **Macros** : `Width` profondeur de LFO 4 → MIX de la Reverb · les autres comme HF01.
- **Sub associé** : S01, sans réverb.
- **Origine** : « plus de réverb à la fin » [SOURCE F14-01] ; réverb dont le mix monte sous un LFO en mode Envelope de 4 mesures [SOURCE F15-02, ERB N DUB] ; réunion [ORIGINAL].

### HF20 Foghorn qui s'ouvre avant la frontière — variation
- **Patch** : HF03 ou HF04. Dans Live, sur la phrase de 8 mesures :
  - `FM` et `Open` stables pendant 6 mesures ;
  - montée des deux macros sur les mesures 7 et 8 ;
  - montée en arpège sur la mesure 8, arrêt au temps 4.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01, coupé au temps 4 de la mesure 8.
- **Jeu** : bloc « DnB 174 — foghorn qui monte avant la frontière » ci-dessous.
- **Origine** : « niveaux des couches automatisés à volonté ; quantité FM montée » [SOURCE F14-02] ; règle des drops d'`AGENTS.md` ; séquence [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60), notes pour des oscillateurs à OCT 0. DnB à 174 BPM : kick sur les doubles croches 1 et 11, caisse claire sur 5 et 13 (règles communes de `dnb-f13-neuro.md`). Aucune attaque de basse sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dnb-f14-hoover-foghorn.md`.

```grille
titre: DnB 174 — foghorn en notes longues (HF01, HF03, HF11)
tempo: 174
accords: Fm7 | Fm7
foghorn: F1[1:6] F1[2&:2] Ab1[3a:4] | F1[1:6] Eb1[2&:3] C2[3a:3] Eb1[4a:1]
sub: F0[1:8] Ab0[3a:4] | F0[1:6] Eb0[2&:3] C1[3a:3] Eb0[4a:1]
```

Notes longues et reprise de la tonique juste après la caisse claire. Sur une tenue de six doubles croches (517 ms), l'ENV 2 de HF03 a fini son attaque (132 ms) mais n'a parcouru que 16 % de son decay de 2,42 s [CALCUL, decay supposé linéaire] : le filtre reste presque ouvert jusqu'à la note suivante.

```grille
titre: DnB 174 — horn en doubles croches (HF05, HF15)
tempo: 174
accords: Fm7 | Fm7
horn: F2[1e:1] F2[1&:1] Ab2[1a:1] F2[2e:1] Eb2[2&:2] C2[3:1] F2[3&:1] F2[3a:1] Ab2[4e:1] C3[4&:2] | F2[1e:1] F2[1&:1] Ab2[1a:1] F2[2e:1] Eb2[2&:2] Db2[3:1] C2[3&:2] Eb2[4e:1] F2[4&:2]
sub: F0[1:4] F0[2e:3] C1[3:2] F0[3&:2] Ab0[4e:3] | F0[1:4] F0[2e:3] Db1[3:2] C1[3&:2] F0[4e:3]
```

Motif original, joué une octave plus haut que le foghorn, comme le horn de F14-09. Le ré bémol de la mesure 2 est une note de passage vers le do.

```grille
titre: DnB 174 — foghorn qui monte avant la frontière (HF20)
tempo: 174
accords: Fm7 | Fm7
foghorn: F1[1:8] C2[3:2] Eb2[3&:2] | F1[1:4] Ab1[2e:2] C2[2a:1] Eb2[3:1] F2[3e:1] Ab2[3&:1] C3[3a:1]
sub: F0[1:8] C1[3:4] | F0[1:4] Ab0[2e:3] C1[3:4]
```

À placer en mesures 7 et 8 : la seconde mesure monte en arpège de Fm7 et s'arrête au temps 4.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « PWM DS » et « Analog_BD_Sin », le bruit « BrightWhite » ;
  - le filtre Comb 2 ;
  - la distorsion Stomp Box ;
  - le STACK d'unison 12 et 12+7.

  Dire si HF01 sonne mieux en PD (écran) ou en FM (voix). Vérifier les destinations des macros.
- Régler à l'oreille les traductions de Zebra 2 (HF05) et du Wavetable de Live (HF04) ; ouvrir le preset gratuit d'ADSR (F14-03) sur le Mac si l'on veut le hoover d'origine.
- Écouter chaque recette avec le sub et le break, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
