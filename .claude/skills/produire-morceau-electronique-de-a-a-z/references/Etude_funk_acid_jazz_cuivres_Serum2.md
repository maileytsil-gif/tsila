# Funk des années 1970 et acid jazz : composition, cuivres et sound design

*Étude pratique pour Ableton Live 12 et Serum 2 — 23 septembre 2026*

## 1. Périmètre et méthode

Le funk des années 1970 fournit le vocabulaire rythmique, la basse, les guitares et les sections de cuivres. L’acid jazz se développe surtout à la fin des années 1980 et dans les années 1990, avec un dialogue entre jazz funk, soul, jeu de groupe, échantillonneurs, séquenceurs et culture club. Miles Davis des années 1970 sert de référence pour la trompette électrique et les arrangements ouverts ; George Benson sert de référence pour l’articulation de la guitare jazz soul. Ce sont des références de gestes et de timbres, pas des prescriptions pour copier une œuvre. L’histoire publiée par Incognito aide à séparer ces périodes [1–3].

Les valeurs de synthèse et les motifs écrits ci-dessous sont **mes propositions de départ**, à régler à l’oreille ; aucune source ne démontre qu’un patch Serum reproduit exactement une trompette, un saxophone ou un trombone acoustique. Les sources établissent les mécanismes acoustiques, les techniques musicales, les instruments et les fonctions des logiciels. Cette distinction reste valable pour toutes les « recettes ».

## 2. Ce qu’il faut entendre et reconstruire

| Rôle | Vocabulaire années 1970 | Transposition acid jazz | Fonction dans le morceau |
|---|---|---|---|
| Batterie | Caisse claire sur 2 et 4, grosse caisse et charleston en doubles croches, notes fantômes, percussion | Même socle, parfois batterie samplée et breaks | Définir les accents et les espaces |
| Basse | Ligne courte répétée, syncopes, octaves, anticipation | Basse électrique ou échantillonnée, sub discret si besoin | Dialoguer avec la grosse caisse |
| Guitare | Muting, attaques courtes, contretemps, accords partiels | Voicings jazz et chorus/wah occasionnel | Couper le rythme et répondre aux claviers |
| Claviers | Rhodes, Wurlitzer, piano, orgue, clavinet | Rhodes et nappes, séquences et samples | Couleur harmonique et contrechant |
| Cuivres | Riffs brefs, unissons, harmonisations et réponses | Riffs conservés mais pouvant être découpés, filtrés ou rééchantillonnés | Ponctuer les transitions et annoncer les refrains |

Berklee étudie les doubles croches, les cellules déplacées du funk et le travail des accords étouffés à la guitare [4–5]. Son enseignement d’arrangement de cuivres traite séparément les registres, les voicings, les mouvements de voix et les fonds derrière une mélodie [6]. **Conséquence pratique :** écrire d’abord basse + batterie, puis réserver à la guitare, au clavier et aux cuivres des fenêtres rythmiques distinctes ; cette dernière phrase est une recommandation d’arrangement, pas une loi historique.

## 3. Harmonie, gammes et phrasé

### Trois cadres utiles

| Situation | Suite originale, tonalité de concert | Matériau mélodique | Usage |
|---|---|---|---|
| Vamp funk modal | Dm9 → G13, une mesure chacun | D dorien : D E F G A B C ; pentatonique mineure D F G A C ; blues : D F G Ab A C | Un riff qui évolue par rythme et timbre |
| Jazz soul / acid jazz | Dm9 → G13 → Cmaj9 → A7alt, une mesure chacun | D dorien puis G mixolydien, C ionien ; sur A7alt, cibler C# et G avec tensions Bb/C/F | Un cycle ii–V–I–VI ramenant vers Dm |
| Couleur mineure plus sombre | Ebm9 → Ab13 → Dbmaj9 → Bb7alt | Eb dorien sur Ebm9 ; Ab mixolydien sur Ab13 ; gamme altérée à vérifier note par note sur Bb7alt | Couplets souples et retour tendu |

**Contrôle harmonique :** Dm9 = D F A C E ; G13 = G B D F E ; Cmaj9 = C E G B D ; A7alt peut prendre A C# G Bb F (quinte omise). G13 partage F et E avec Dm9, B donne l’éclat dorien. Sur A7alt, ne pas garder C naturel comme tierce stable : la tierce de A7 est C#. Les notes de passage chromatiques résolvent en général sur les tierces, septièmes ou notes du thème. Ces progressions sont des exemples composés pour ce dossier, **pas des transcriptions**.

### Construire un solo qui raconte quelque chose

1. Fixer un motif de deux ou trois notes (par exemple F3–A3–C4, soit MIDI 65–69–72, au-dessus de Dm9).
2. Répéter le motif avec une seule modification : déplacement rythmique, note voisine E3 (64), réponse une octave plus bas.
3. Laisser une respiration de demi-mesure ; faire répondre guitare et sax alternativement.
4. Passer aux arpèges et approches chromatiques seulement quand l’harmonie change ; finir sur une note cible claire.
5. Enregistrer plusieurs prises MIDI ou audio jouées à la main et choisir les intentions, pas une vélocité identique à chaque note.

George Benson dit avoir développé des octaves inspirées de Wes Montgomery en ajoutant une note entre les octaves, et avoir appris à chanter en jouant. Il décrit la ligne chantée comme plus conversationnelle et mélodique [7]. **Exercice original :** jouer F3–A3–C4–A3 (MIDI 65–69–72–69) sur guitare, chanter la même cellule, ensuite remplacer le second A3 par G3 (67) et laisser un silence ; une variante en octaves F2/F3 (53/65) puis G2/G3 (55/67) suffit pour faire entendre le principe sans reproduire un solo connu. Réserver les traits rapides à une réponse, éviter de couvrir la ligne principale.

## 4. Instruments : production vintage et traduction électronique

| Source / technique | Vintage crédible | Adaptation électronique | Point d’écoute |
|---|---|---|---|
| Guitare jazz Benson | Guitare hollowbody, micro manche, timbre arrondi ; attaque des notes nettes, octaves et chant en doublure | Échantillon de vraie guitare puis chorus léger / filtre animé ; pour le rythme, prise de guitare en attaques étouffées | Les cordes coupées et glissés restent difficiles à simuler au clavier |
| Trompette Miles | Souffle, attaque variable, longues notes expressives, sourdine Harmon selon époque | Une prise ou des multisamples de trompette, puis wah commandée au pied, saturation légère et délai | La sourdine acoustique et la wah sont deux transformations distinctes |
| Sax alto / ténor | Anche, attaque avec langue ou air, bruits de clés, growl ponctuel | Multisample avec couches de vélocité et bruit court ; saturation/filtre pour motif club | Différencier notes liées et détachées |
| Trombone | Embouchure et coulisse, glissandi réellement continus, graves arrondis | Échantillons de legato/glissando ; couche synthèse pour appels graves | Une simple molette de pitch ne restitue pas toute la transition acoustique |
| Rhodes / clavier | Tine métallique frappée, pickup ; son doux ou mordant selon attaque | Ableton Electric, multisamples Serum 2, tremolo et ampli ; filtre automation pour version club | Le contraste entre frappes faibles et fortes fait le caractère |

Ibanez décrit la GB10 Benson comme une hollowbody avec micros flottants [8]. L’histoire de la trompette et des sourdines de Miles ainsi que la présence de guitares électriques, Rhodes et traitements sur ses sessions électriques sont documentées par ses archives et par la Philharmonie de Paris [9–11]. Yamaha explique que la trompette part de la vibration des lèvres, le saxophone d’une anche, et le trombone de la vibration des lèvres avec modification de longueur par la coulisse [12–14]. Le Rhodes documente le marteau qui frappe une *tine* métallique, récupérée par un pickup [15].

## 5. Recettes Serum 2 : cuivres acoustiques et synthétiques

### Principes communs

Serum 2 offre notamment oscillateurs wavetable, multisample, sample, granular et spectral ; son moteur multisample peut distribuer des prises selon hauteur et dynamique [16]. Pour un **cuivre vintage crédible**, préparer ses propres prises ou des banques dont les droits permettent cet usage : notes courtes et tenues, piano/forte, quelques attaques, releases et transitions. Charger le multisample dans OSC A, choisir un comportement de vélocité pertinent, assigner la molette ou l’aftertouch au niveau/timbre, et garder des articulations distinctes sur des pistes ou presets différents. Une banque de sons fixes sans transitions ne permettra pas de simuler un legato authentique. Pour un **cuivre électronique**, utiliser un oscillateur synthétique et assumer le timbre de synthé.

Notation des réglages : filtre en Hz, temps en ms, modulation en demi-tons ou pourcentage relatif ; valeurs **expérimentales**. À 100 BPM, une double croche dure 150 ms. Vérifier le niveau de sortie et ajuster les plages des macros selon les samples et la version du plug-in. Aucun de ces chiffres ne provient des fabricants.

### Trompette : trois états dans une même famille

**A. Trompette acoustique / section vintage.** OSC A = multisamples de trompette sans sourdine (plusieurs notes et au moins deux dynamiques). ENV amplitude : attaque 10–25 ms, release 90–180 ms pour les tenues ; version staccato avec release 50–90 ms. La vélocité change **simultanément** volume et couleur (couche forte plus riche) ; molette ouvre légèrement le filtre et augmente le souffle réel de l’enregistrement, si disponible. Vibrato par modulation manuelle progressive après 200–350 ms sur les longues notes, de l’ordre de ±10–25 cents : jamais identique sur chaque note. Mixer un bruit court très discret à l’attaque uniquement si le multisample n’en contient pas. Ne pas coller de reverb large avant d’avoir vérifié la lisibilité des attaques.

**B. Trompette bouchée / évocation Miles.** Prendre une **vraie couche de trompette avec sourdine Harmon** si possible, puis automate de wah : fréquence centrale d’un filtre résonant modulée par pédale/Macro 1 autour de 450 Hz–2,5 kHz en partant d’une excursion plus étroite ; ajuster la résonance pour éviter la sifflante. Saturation douce, délai court peu dosé. Si seule la trompette ouverte est disponible, l’égalisation en bande et le filtre créent une **interprétation stylisée**, pas la résonance exacte d’une Harmon. La période électrique de Miles exploite aussi une trompette au wah, particulièrement documentée autour d’*On the Corner* [10].

**C. Synth brass électronique.** OSC A = wavetable à harmoniques proches de saw ; OSC B = pulse ou saw plus doux à −1 octave, niveau 10–25 % de A ; ENV 1 attaque 8–20 ms, decay 160–300 ms, sustain 45–70 %, release 70–130 ms. Filtre passe-bas 12/24 dB, fréquence initiale environ 800 Hz–1,5 kHz, ENV 2 ouvrant brièvement vers 2–4 kHz au début de note. Macro « souffle » = petite quantité de noise ; macro « wah » = balayage d’un second filtre ; léger désaccord seulement si son de section recherché. Jouer court et laisser du silence.

### Saxophone alto ou ténor

**A. Source vintage.** OSC A = multisamples séparés alto ou ténor, avec attaques soufflées et franches ; ne pas simplement baisser un alto d’une octave pour « fabriquer » un ténor. Enveloppe d’attaque 15–45 ms sur lignes souples, plus rapide pour les détachés ; relâchement 100–220 ms ; vélocité pilote les échantillons ou timbres, et expression pilote le volume d’une note déjà tenue. Bruit d’anche / souffle en entrée de note, très faible et variant par note. Ajouter très peu de clé mécanique si l’enregistrement en comporte réellement. Le **growl** vient chez le saxophoniste d’un chant simultané dans l’instrument [13] : utiliser un sample dédié ou une distorsion modulée avec prudence, plutôt qu’un LFO constant.

**B. Sax électro.** Partir de cette source puis isoler un fragment de 100–400 ms dans OSC Sample ou Granular ; automatiser filtre passe-bande autour de 700 Hz–2,5 kHz, saturation modérée, tremolo synchronisé seulement lors de la réponse. Pour une version pure synthèse : saw filtrée, bruit d’attaque court et formants obtenus par deux bandes résonantes, mais annoncer clairement le résultat comme « sax synthétique ». Doubler une phrase de deux mesures avec une seule octave d’écart dans un passage, couper le doublage au suivant pour conserver de la dynamique.

### Trombone

**A. Source vintage.** Enregistrer/charger notes fortes et douces ainsi que véritables glissandi courts. OSC A multisample pour notes fixes ; piste audio ou instrument séparé pour les glissés. ENV d’amplitude attaque 20–60 ms, release 120–240 ms ; limiter les notes trop graves si elles entrent en collision avec la basse. Jouer les stabs sous la trompette, mais garder le trombone suffisamment présent vers le bas médium. La coulisse modifie physiquement la longueur du tube [14] : un pitch bend de ±2 demi-tons sur le même sample reste une approximation.

**B. Trombone électronique.** OSC A = saw + OSC B triangle à faible niveau, −1 octave facultative ; passe-bas autour de 500 Hz–1,5 kHz, ouverture brève sur l’attaque ; ENV 1 attaque 15–35 ms, decay 200–350 ms, sustain 55–75 %, release 100–180 ms. Pitch bend continu de ±2 demi-tons **seulement pour les effets** ; pour l’impression « groupe de cuivres », empiler trois pistes distinctes (trompette, sax, trombone) plutôt qu’un unique gros preset.

### Contrôle A/B décisif

1. Jouer le même riff avec **samples réalistes**, puis avec **synth brass** ; comparer en volume égal.
2. Couper le bruit d’attaque : s’il n’apporte rien au riff, ne pas le garder.
3. Écouter en solo les changements de note et les silences : les défauts d’articulation s’entendent davantage que le spectre moyen.
4. Remplacer temporairement les cuivres virtuels par trois prises vocales fredonnées : si le riff est faible, corriger composition et placement avant le patch.

Jerry Gates (Berklee) prévient que les cuivres échantillonnés peuvent sembler plus épais et immédiats que des musiciens ; prévoir ce biais au moment d’écrire une section destinée à de vrais instrumentistes [6].

## 6. Section de cuivres : écrire les voix avant le mixage

Pour un trio, placer d’abord une ligne de trompette claire dans l’aigu, une voix de sax dans le médium et un trombone dans le bas. Répartir les notes utiles de l’accord entre les trois plutôt que tripler chaque fondamentale. Exemple de **voicing original en sons de concert**, dans le registre central à adapter aux exécutants :

| Accord | Trombone | Sax ténor | Trompette | Ce que portent les trois voix |
|---|---|---|---|---|
| Dm9 | F2 (53) | A2 (57) | C3 (60) | tierce, quinte, septième |
| G13 | F2 (53) | B2 (59) | E3 (64) | septième, tierce, treizième |
| Cmaj9 | E2 (52) | B2 (59) | D3 (62) | tierce, septième, neuvième |
| A7alt | G2 (55) | C#3 (61) | F3 (65) | septième, tierce, treizième bémol |

Sur G13, l’écart F2–B2 forme un triton tendu voulu ; vérifier à l’écoute et ne pas l’imposer à chaque attaque. Sur la suite entière, conserver les notes communes et bouger les autres par petits intervalles quand cela sert la ligne. Faire alterner accords courts à trois voix, réponses à l’unisson, puis une mesure sans cuivres. Les stabs utiles suivent des motifs de 1 à 3 attaques par mesure et laissent des respirations ; les placer sur les syncopes en écoutant la grosse caisse plutôt qu’en remplissant mécaniquement les temps.

**Transposition :** le tableau est en sons réels pour piano roll Ableton. Pour une partition instrumentale, trompette en Si♭ : écrire un ton au-dessus du son réel ; sax ténor en Si♭ : écrire une neuvième majeure au-dessus ; sax alto en Mi♭ : écrire une sixte majeure au-dessus ; trombone : son réel. Vérifier l’octave et la tessiture au moment de confier les parties à des musiciens. Les noms de notes suivent la numérotation Ableton, C3 = MIDI 60 (le numéro MIDI fait foi ; la version d’origine écrivait en notation scientifique, une octave au-dessus).

## 7. Claviers, guitare et place dans le mix

**Rhodes.** Ableton Electric modélise notamment des caractéristiques de piano électrique à tines ; une prise multisample authentique reste une autre option [15,17]. Commencer avec un son doux et peu compressé : vélocités 55–95, quelques accents 105 ; tremolo lent autour de 3–5 Hz très subtil, saturation légère et reverb courte. La dureté de l’attaque doit faire apparaître le « bark » plutôt que dépendre d’un égaliseur permanent [15]. Main gauche : laisser la basse porter les fondamentales ; main droite : F2–C3–E3 pour Dm9, F2–B2–E3 pour G13, E2–B2–D3 pour Cmaj9. Les octaves réelles sont ajustables.

**Clavinet et orgue.** Clavinet pour figures aiguës coupées et attaques répétées ; orgue pour réponse tenue et tension en fond. Si la guitare joue les doubles croches, confier aux claviers des accords espacés ou une nappe ; si le clavier tient le rythme, simplifier la guitare. C’est un choix d’orchestration proposé, pas un inventaire obligatoire des instruments d’un style.

**Guitare Benson : deux fonctions distinctes.** Pour une ligne lead : hollowbody/micro manche, attaque propre, peu d’effet, phrases chantables, octaves occasionnelles. Pour la guitare rythmique funk : une prise plus courte et percussive, cordes bloquées entre les accords, motif en doubles croches, wah si cela aide la réponse. Le timbre rond de la première fonction et le découpage sec de la seconde peuvent demander **deux prises et deux réglages**. Écarter l’une de l’autre légèrement dans le panorama si elles jouent ensemble ; contrôler le médium autour de la voix et du sax plutôt que creuser aveuglément une fréquence fixée.

**Mix de départ.** Basse et grosse caisse ensemble au centre ; aigus des cuivres contrôlés sur les attaques ; reverb courte commune pour donner une salle sans effacer les silences ; délais ponctuels en fin de phrase. Égaliser après arrangement, en écoutant un extrait de référence à niveau perçu proche. Pour un morceau destiné à la danse, vérifier translation en mono, dynamique du kick/basse, et comparer la version avec et sans traitement final. Il n’existe pas de cible LUFS universelle garantie par le genre.

## 8. Mini-prototype original à construire dans Ableton

**Tempo 104 BPM, 4/4, 16 mesures, Dm9–G13–Cmaj9–A7alt en boucle.** Positions « temps + subdivisions » ci-dessous : `1`, `1&`, `2`, `2&`, `3`, `3&`, `4`, `4&` ; un `a` signifie la dernière double croche du temps. Dans Live, entrer les notes en son réel.

| Mesures | Batterie / basse | Clavier / guitare | Cuivres / mélodie | Évolution |
|---|---|---|---|---|
| 1–4 intro | Kick léger sur 1 et 3&, charley en croches ; basse absente sur 1–2, entre sur 3 | Rhodes accords courts sur 2& et 4& ; guitare coupée une mesure sur deux | Trompette seule : C4 sur 4& mesure 4 | Faire entendre la tonalité avant le riff |
| 5–8 thème A | Kick sur 1, 2&, 3&, 4a selon la mesure ; snare 2 et 4 ; basse D1–A1–C2–D2 (MIDI 38–45–48–50) sur mesures Dm9, G0–D1–F1–G1 (MIDI 31–38–41–43) sur G13 | Guitare attaque étouffée sur 1a, 2&, 3a ; Rhodes sur 1&, 3& | Trio en accord court sur 1& et 3a mesure 5, silence mesure 6, réponse de trompette mesure 7 | Répéter la cellule en changeant une seule note |
| 9–12 thème B | Garder kick/snare ; basse descend vers C1 (36) puis A0 (33) si la tessiture le permet | Rhodes plus présent, guitare passe à une réponse lead | Sax prend le motif, trombone répond en fin de mesure | Ouvrir progressivement les registres |
| 13–16 transition | Couper kick une demi-mesure en 15 ; reprise pleine en 16 | Accord de Rhodes prolongé en 15, guitare en octave en 16 | Unisson très bref en 16 puis silence avant reprise | Créer une relance audible |

**Cellule MIDI originale d’une mesure sur Dm9**, à déplacer si elle gêne la caisse claire : trompette C3 à 1& (durée 1/8), E3 à 2a (1/16), F3 à 3& (1/8) ; sax A2 sur ces trois attaques ; trombone F2 sur les attaques 1& et 3& seulement. Vélocités proposées respectivement 88 / 72 / 98 ; avancer ou retarder à l’oreille certaines attaques de quelques millisecondes **sans décaler toute la section au hasard**. Sur G13, tester trompette E3–F3–E3, sax B2 et trombone F2. Chaque phrase doit laisser une mesure où une autre famille instrumentale répond.

**Développer en morceau entier (96 mesures proposées, soit environ 3 min 42 à 104 BPM)** : 8 intro + 16 couplet instrumental + 16 thème A + 8 break + 16 thème B/solo + 16 retour thème + 8 interlude + 8 outro = 96. Pour l’acid jazz, ajouter une version du riff découpée en sampler sur le break ; pour une approche funk live, conserver la section jouée et varier les fins de phrases. Les choix exacts de structure et de tempo sont des propositions créatives.

## 9. Ce qui est attesté, ce qui reste à tester

- **Attesté par sources primaires / témoignages directs :** fonctions du moteur Serum 2, mécanismes trompette/sax/trombone et Rhodes, technique décrite par Benson, certains instruments et traitements de Miles, enseignement Berklee sur funk et orchestration, histoire d’Incognito et de l’acid jazz [1–17].
- **Propositions vérifiables en session :** valeurs de filtre et d’enveloppe, tableaux de voicings, motifs, degrés de vélocité, dosage des effets et architecture de 96 mesures. Exporter des essais audio et comparer à une prise instrumentale si le réalisme est décisif.
- **Limites :** aucune analyse spectrale de stems isolés ni mesure de l’équipement exact sur chacun des enregistrements cités ; aucune vidéo prétendument visionnée ici. Les interviews sont des propos d’artistes, non des mesures d’acoustique. Pour les articulations expressives, des samples de qualité et le jeu humain sont des variables majeures.

## Sources commentées (liens directs)

1. [Incognito, *About Us*](https://www.incognito.london/incognito) : jazz funk du groupe, cuivres invités et arrivée des séquenceurs.
2. [Incognito, histoire du groupe](https://www.incognito.london/incognito) : continuité entre jazz funk et acid jazz ; pour le contexte des labels, consulter des entretiens directs avec Gilles Peterson.
3. [Miles Davis, *On the Corner*](https://www.milesdavis.com/albums/on-the-corner/) et [*Bitches Brew*](https://www.milesdavis.com/albums/bitches-brew/) : instrumentation et sessions électriques.
4. [Berklee, *Two Cool Rhythmic Devices*](https://www.berklee.edu/berklee-today/fall-2009/the-woodshed/rhythmic-devices) : cellules rythmiques funk.
5. [Berklee Online, *Rhythm and Groove Guitar*](https://online.berklee.edu/courses/rhythm-and-groove-guitar) : accords étouffés et doubles croches.
6. [Berklee Online, entretien avec l’arrangeur Jerry Gates](https://online.berklee.edu/takenote/contemporary-horn-arranging-an-interview-with-jerry-gates/) : orchestration, taille de section, comparaison instruments réels/samplés.
7. [George Benson, entretien MusicRadar](https://www.musicradar.com/news/george-benson-ive-always-been-an-experimenter-when-i-was-young-i-thought-i-was-going-to-be-a-scientist) : octaves, chant en unisson et phrasing selon l’artiste.
8. [Ibanez, GB10](https://www.ibanez.com/usa/products/detail/gb10_00_09.html) : construction et micros de la guitare signature.
9. [Philharmonie de Paris, Miles Davis et la sourdine Harmon](https://collectionsdumusee.philharmoniedeparis.fr/0056008-biographie-miles-davis.aspx?_lg=fr-FR) : objet de collection ; consulter la notice pour le modèle précis.
10. [Miles Davis, *On the Corner*](https://www.milesdavis.com/albums/on-the-corner/) : wah et section électrique.
11. [Miles Davis, *Bitches Brew*](https://www.milesdavis.com/albums/bitches-brew/) : claviers, guitare et basse électriques.
12. [Yamaha, fonctionnement de la trompette](https://www.yamaha.com/en/musical_instrument_guide/trumpet/mechanism/) : vibration des lèvres et embouchure.
13. [Yamaha, fonctionnement du saxophone](https://www.yamaha.com/en/musical_instrument_guide/saxophone/mechanism/) et [growl](https://www.yamaha.com/en/musical_instrument_guide/saxophone/play/play006.html) : anche et effet vocal.
14. [Yamaha, fonctionnement du trombone](https://www.yamaha.com/en/musical_instrument_guide/trombone/mechanism/) : coulisse et hauteur.
15. [Rhodes, manuel V8](https://download.rhodesmusic.com/assets/RHODES-V8PRO/Rhodes%20V8%20Manual%20v3.pdf) : marteau, tine, pickup ; [Rhodes MK8](https://rhodesmusic.com/the-rhodes-mk8-a-masterpiece-of-craftsmanship-and-innovation/) : dynamique de l’attaque.
16. [Xfer Records, manuel Serum 2](https://xferrecords.com/web-manual/serum-2/exploring-sound-design-in-serum) : types d’oscillateurs et multisamples.
17. [Ableton, manuel Live 12, Electric](https://www.ableton.com/en/manual/live-instrument-reference/) : modèle de piano électrique.

## 11. Étude complémentaire : harmonie, basse, cuivres et claviers en interaction

*Ajout du 28 septembre 2026. Les exemples de notes et de rythmes suivants sont des compositions pédagogiques originales en sons réels (concert pitch), et non des transcriptions attribuées à un groupe. Notation d'octave : numérotation Ableton, C3 = MIDI 60 (le numéro MIDI fait foi ; la version d'origine écrivait en notation scientifique, une octave au-dessus); selon l'instrument virtuel, l'étiquette d'octave peut varier. Vérifier la hauteur à l'oreille.*

### 11.1 Deux logiques harmoniques et leur articulation

**Funk de vamp.** On peut rester une, deux ou quatre mesures sur un seul accord : c'est alors l'organisation des attaques de basse, guitare, Rhodes et cuivres qui crée le mouvement. Une dominante statique D7, D9 ou D13 apporte un son plus tendu et bluesy; Dm7 ou Dm9 avec B naturel dans la ligne de basse ou de clavier fait entendre D dorien. Il serait trompeur de dire que tout funk emploie uniquement les accords dominants : majeur, mineur, soul et gospel coexistent selon les morceaux.

**Acid jazz.** Souvent plus de mouvement harmonique : ii–V–I, couleurs m9, maj9, 6/9, 13, sus, accords parallèles et retours chromatiques. L'enrichissement ne signifie pas jouer neuf notes à la fois : basse sur fondamentale, Rhodes sur tierce/septième et tensions, cuivres sur notes du motif. Le choix est rythmique autant qu'harmonique. L'approche de Berklee sur les tensions et le voice leading aide à construire ces voicings ([tensions](https://online.berklee.edu/takenote/simplifying-jazz-harmonic-theory-an-interview-with-suzanna-sifter/), [notes guides](https://online.berklee.edu/takenote/voice-leading-paradigms-for-harmony-in-music-composition/)).

| Cycle original | Notes structurantes | Fonction de la basse | Moment utile |
|---|---|---|---|
| Dm9 durant 4 mesures | D F A C E, B comme couleur dorienne mélodique | D répété, A octave/quinte, C/E comme approche | Couplets et solos construits sur groove |
| Dm9 → G13, 2 mesures chacun | Dm9 : F C E; G13 : B F E | D→G par anticipation, garder F/E dans les claviers | Changement discret mais audible |
| Dm9 → G13 → Cmaj9 → A7alt | F/C/E → B/F/E → E/B/D → C#/G/B♭ | D→G→C→A; C# mène à D | Break/refrain acid jazz sur 4 mesures |
| Dm9 → E♭13 → Dm9 → A7alt | Glissement chromatique E♭ puis retour D | D→E♭→D→A; basse peut tenir les fondamentales | Couleur plus tendue et urbaine |
| Dm9 → B♭maj9 → Gm9 → A7(b9) | Dm9; B♭ D F A C; G B♭ D F A; A C# E G B♭ | Descente harmonique D→B♭→G→A | Refrain soul/jazz avec tension de retour |

**Voicings précis pour une piste Rhodes dont la basse est ailleurs :** Dm9 = main droite F2–C3–E3–A3; G13 = F2–B2–E3–A3 (A est la 9e de G); Cmaj9 = E2–B2–D3–G3; A7(b9) = G2–C#3–E3–B♭3. Ces voicings contiennent parfois une 9e/13e additionnelle et omettent la fondamentale : nommer l'accord selon la **basse jouée**. Si le registre est trop chargé, retirer A3 ou G3 et jouer seulement tierce, septième et une tension. Vérifier la conduite des voix à l'oreille, surtout B♭3→A3 et C#3→D3.

**Rythme d'accord :** sur une grille de 16 doubles croches, essayer Rhodes aux pas 4, 7 et 12, avec durées respectives 1, 2 et 1 pas; éviter le pas 1 lorsqu'une basse forte pose l'accord. Dans une version acid jazz plus détendue, tenir le premier voicing 1/2 mesure puis faire seulement une réponse courte à la fin. Une progression harmonique rapide et des accords très syncopés ensemble peuvent brouiller la lecture : simplifier l'un des deux.

### 11.2 Anatomie de la basse : notes, durées et placement

La basse funk assure simultanément **ancrage** et **élan**. La fondamentale sur le premier temps est une ressource fréquente, mais les autres attaques peuvent tomber entre les temps. La durée est aussi importante que la hauteur : des notes mortes et des notes courtes donnent le mouvement sans remplir constamment le grave. Yamaha décrit précisément cette importance du « one », des ghost notes, des durées et du placement par rapport au kit ([jeu funk](https://hub.yamaha.com/guitars/bass/authentic-bass-playing/), [groove](https://hub.yamaha.com/guitars/bass/getting-your-bass-into-the-groove/)). Berklee traite les syncopes en croches/doubles croches, les fondamentales/quintes et les approches chromatiques en pédagogie de basse R&B ([cours](https://online.berklee.edu/courses/r-b-bass)).

**Hiérarchie des notes sur Dm9 :** D = ancrage; A = quinte stable; C = septième mineure; F = tierce mineure; E = neuvième colorante; G = 11e de passage; B = sixte/note dorienne; C# = approche chromatique vers D, brève et résolue. Sur G13, G est fondamentale, D quinte, F septième, B tierce, E sixte/13e; à l'approche de Cmaj9, B peut anticiper la septième majeure de C, tandis que C prépare la nouvelle fondamentale.

**Mesure originale à 16 pas, Dm9, environ 100 BPM :** un « pas » est une double croche; la longueur indiquée est avant le silence suivant. Des hauteurs exactes sont proposées pour programmer le MIDI, puis adapter le registre à la basse choisie.

| Pas | Position | Note | Durée suggérée | Rôle / articulation |
|---:|---|---|---|---|
| 1 | 1 | D1 (MIDI 38) | 2 pas | Ancrage franc avec ou après le kick |
| 4 | a de 1 | A1 (45) | 1 pas | Quinte courte, relance |
| 6 | e de 2 | C2 (48) | 1 pas | 7e en syncope |
| 7 | & de 2 | note morte | 1 pas | Attaque étouffée, sans hauteur définie |
| 9 | 3 | F1 (41) | 2 pas | Tierce mineure, changer la couleur |
| 12 | a de 3 | A1 (45) | 1 pas | Quinte rebond |
| 14 | e de 4 | C2 (48) | 1 pas | Appel vers la mesure suivante |
| 16 | a de 4 | A♭0 (32) | 1 pas | Approche chromatique de G0 (31), basse de G13 à la mesure 2 |

Cette mesure est **un exercice**, pas une formule universelle. Les ghost notes d'une vraie basse sont des attaques de corde étouffée; sur un plugin, utiliser une articulation dédiée ou un très court échantillon étouffé plutôt que de prétendre qu'une note MIDI très basse imite automatiquement une ghost note.

**Variante à 120 BPM, acid jazz/house en Dm9 :** kick 4/4, D1 (38) au pas 1 (1 pas), A1 (45) au pas 4 (1 pas), C2 au pas 7 (1 pas), D1 au pas 9 (2 pas), E1 (40) au pas 12 (1 pas), A1 au pas 15 (1 pas). Laisser les pas 5 et 13 au clap/snare; sur les quatre mesures, remplacer seulement la dernière note par une approche de l'accord suivant. Sur G13, reprendre l'ossature rythmique avec G0 (31), D1, F1 (41), G0, B0 (35), D1; contrôler l'octave et la tessiture de la banque. Dans la house, raccourcir les notes aux côtés du kick/sidechain à l'oreille : ne pas appliquer aveuglément le même pattern qu'un batteur vivant.

**Façon de jouer :** doigts = attaque ronde, compression naturelle et petits glissés; médiator = attaque nette, pertinent selon esthétique; slap = accent percussif ciblé, pas obligation permanente; note morte = pulsation non tonale; slide vers la tierce/septième = expression; octave = déplacement d'énergie. Sur 4 mesures, varier la dernière croche ou double croche, conserver le même ancrage pour que le public reconnaisse le groove. Pour un jeu crédible dans Kontakt/Maschine, alterner vélocités, durées, articulations et déclenchements légèrement décalés; ne pas « humaniser » le kick et la basse indépendamment au hasard.

### 11.3 Cuivres : accompagnement, réponses et breaks

La section pratique **trompette + sax ténor + trombone** permet trois niveaux : trompette haute pour l'éclat, ténor au milieu pour le corps, trombone plus bas pour la masse. Il s'agit de rôles, pas de tessitures fixes. Écrire d'abord les notes **au diapason/concert pitch**, puis transposer pour les vrais instrumentistes : trompette en Si♭ et ténor en Si♭ exigent des parties écrites transposées; le trombone reste généralement noté en sons réels dans les partitions appropriées. Le sax alto en Mi♭ demande une autre transposition.

**Trois comportements différents :**

1. **Stab d'accompagnement :** accord très court (souvent 1/16 à 1/8), attaques communes mais releases légèrement différents. Éviter de jouer exactement sur chaque accord du Rhodes. En Dm9 : trombone D2, ténor C3, trompette F3 ou E3; variante plus ouverte D2–A2–F3. Ajuster selon l'instrument, car un empilement trop serré dans le bas devient opaque.
2. **Riff mélodique :** trois notes qui se répètent avec un léger changement, p. ex. F3–A3–C4 à unisson/octaves selon le registre, puis réponse E3–F3. Ne pas harmoniser systématiquement toutes les notes rapides; harmoniser l'attaque et la fin suffit parfois.
3. **Fill de break :** ligne montante de 1 ou 2 mesures, puis **silence avant le retour du groove**. Les cuivres peuvent finir plus tôt que la batterie et laisser le pickup de basse annoncer le temps 1.

**Exemple original de réponse sur deux mesures de Dm9, grille 16 pas :** basse pose D au pas 1; Rhodes attaque aux pas 4 et 12; cuivres frappent **ensemble pas 7** (F3–A3–C4, staccato 1 pas) puis **pas 15** (E3–G3–B3, très bref, couleur dorienne à tester). La mesure 2 échange le stab du pas 15 contre un unisson A3–C4 sur les pas 14–15, puis se tait au pas 16 pour laisser entrer la mesure 3. Si cette proposition couvre la voix, placer le second stab une octave plus bas ou le supprimer.

**Break de huit mesures :** mesures 1–2, un seul appel de sax sur une queue de Rhodes; 3–4, retour de deux stabs plus doux; 5–6, montée des trompettes en réponses courtes; 7, ensemble serré en croches; 8, fill d'une demi-mesure, arrêt au plus tard sur le dernier demi-temps, silence puis retour kick+basse. Une autre forme valable garde les cuivres silencieux sur 7–8 et les fait exploser au drop. Pour une esthétique vintage, enregistrer des prises distinctes plutôt que de copier-coller la même attaque MIDI sur trois pistes; pour une esthétique électronique, un chop/filtre de section imprimée peut être assumé comme effet. L'enseignement Berklee d'arrangement traite ces choix de registre, voicings et fonds ([Arranging for Horns](https://online.berklee.edu/store/product?category_id=4&product_id=49830074&usca_p=t)).

### 11.4 Claviers : qui joue quoi, et quand ?

| Instrument | Rôle harmonique | Attaque et temps | Son et traitement de départ |
|---|---|---|---|
| Rhodes | m9, maj9, 13, accords partiels et réponse douce | Accords courts décalés ou tenus avec variation de dynamique | Electric dans Live, saturation douce, tremolo lent; garder les graves libres |
| Clavinet | Tranche rythmique quasi guitare | Doubles croches étouffées, beaucoup de silences | Source échantillonnée crédible, enveloppe brève, éventuellement wah |
| Piano acoustique | Introduction, montée d'accords, accent de break | Attaques plus franches, voicings ouverts | Compression légère si utile; ne pas remplir constamment |
| Orgue | Tenue, réponse et liaison entre sections | Tenues et petites attaques anticipées | Automatiser expression plutôt que multiplier les notes |
| Synthé discret | Lien acid jazz / club | Stab ou nappe qui laisse la voix au premier plan | Serum Sample/Granular, ou Wavetable, couches hautes filtrées |

La documentation du fabricant retrace le rôle du Rhodes dans jazz/funk et acid jazz ([histoire Rhodes](https://rhodesmusic.com/the-history-of-rhodes/)). Pour une production convaincante, différencier les **gestes** : le Rhodes fait une réponse harmonique de deux ou trois notes-guides, le Clavinet joue une grille de silences et d'attaques, le piano expose la progression au break. Trois claviers jouant le même accord au même endroit créent davantage de masque que de richesse.

**Exemple pratique de 4 mesures Dm9 → G13 → Cmaj9 → A7(b9) :** sur chaque changement, laisser la basse jouer la racine sur le pas 1; Rhodes utilise les voicings sans fondamentale ci-dessus aux pas 4 et 12, le second plus faible; piano absent des mesures 1–2, entre sur 3–4 avec une seule attaque tenue au début du break; Clavinet joue 2–3 courtes attaques libres entre basse et Rhodes. Conserver 3e et 7e entre accords par petits mouvements : F de Dm devient F de G7, puis E de Cmaj; C de Dm descend vers B de G7, puis reste B de Cmaj. C'est ce cheminement, autant que les noms d'accords, qui donne la continuité jazz.

### 11.5 Arrangement complet de 16 mesures à produire

| Mesures | Harmonie | Basse | Clavier | Cuivres | Batterie / transition |
|---|---|---|---|---|---|
| 1–4 | Dm9 vamp | Motif D–A–C–F, variation seulement en 4 | Rhodes sur contretemps; Clavinet parcimonieux | Une réponse en mesure 4 | Batterie funk stable, hats en doubles croches variées |
| 5–8 | Dm9 → G13 | Anticipation de G à la fin de 6 ou 7 | Faire entendre B sur G13; éviter doublure de la racine | Stab sur dernière moitié de 8 | Petit fill batterie en 8 |
| 9–12 | Dm9 → G13 → Cmaj9 → A7(b9) | Fondamentales sur 1, approche chromatique aux changements | Rhodes plus tenu; piano expose les changements | Riff court, puis retiré pour aérer | Break allégé au début, tension vers 12 |
| 13–16 | Dm9 → G13 → Cmaj9 → A7(b9) | Retour du motif renforcé, variation à 16 | Rhodes en réponse, Clavinet réintroduit | Stabs en 13–14, fill en 16 | Retour groove complet, silence bref possible avant mesure 17 |

**À valider dans Ableton Live 12 :** écouter basse+batterie seules, puis ajouter Rhodes, puis cuivres. Quantifier les downbeats, garder des décalages intentionnels modestes ailleurs; faire deux versions (Rhodes en avance / Rhodes en retard) et choisir à niveau égal. Écouter en mono : basse, grosse caisse, trombone et main gauche de piano se concurrencent facilement dans le bas médium. Si l'ensemble ne danse pas sans les cuivres, résoudre d'abord le dialogue kick-basse.

### Références supplémentaires

- [Yamaha : bassiste funk, « one », durées et notes mortes](https://hub.yamaha.com/guitars/bass/authentic-bass-playing/).
- [Yamaha : articulation et groove de basse](https://hub.yamaha.com/guitars/bass/getting-your-bass-into-the-groove/).
- [Berklee : croches, doubles croches et caractère funk](https://online.berklee.edu/takenote/basic-funk-for-drums/).
- [Berklee : syncopes, arpèges et approches chromatiques en basse R&B](https://online.berklee.edu/courses/r-b-bass).
- [Berklee : notes-guides et conduite des voix](https://online.berklee.edu/takenote/voice-leading-paradigms-for-harmony-in-music-composition/).
- [Rhodes Music : histoire de l'instrument et acid jazz](https://rhodesmusic.com/the-history-of-rhodes/).

