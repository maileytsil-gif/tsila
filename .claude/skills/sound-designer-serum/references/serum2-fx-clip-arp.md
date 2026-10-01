# Serum 2 — effets, routage, clips et arpégiateur

Dépouillement du **manuel officiel Serum 2**, 354 pages. Les numéros de page sont ceux du manuel. Tout ce qui suit est documenté sauf mention `[I]`. Les points marqués **MUET** sont ceux où le manuel ne dit rien : ils ne sont pas comblés.

---

# A. MIXER ET ROUTAGE

## Canaux (p. 144-145)

Le mixer réunit **SUB, OSC A, OSC B, OSC C, NOISE**, les sorties de **FILTER 1** et **FILTER 2**, plus **deux bus internes**. Il n'affiche que les éléments activés : dans le patch Init, seul OSC A apparaît. **Cliquer l'en-tête d'un canal active l'oscillateur ou le filtre dans tout Serum**, pas seulement dans le mixer.

**Valeurs par défaut** : OSC A passe par FILTER 1 ; OSC B, OSC C, SUB et NOISE passent par MAIN.

## Routage d'un oscillateur — quatre options (p. 146)

| Option | Effet |
|---|---|
| **Filter** | Vers le module de filtre. **Le knob du haut règle la répartition entre FILTER 1 et FILTER 2** |
| **Main** | Vers la sortie principale. Fait apparaître un bouton « enveloppe » : activé, le niveau est soumis à ENV 1 ; **désactivé, ENV 1 n'agit plus et l'oscillateur se termine après le release le plus long de toutes les enveloppes**, ce qui le rapproche d'un free-running |
| **Direct** | **Contourne le filtre ET la section d'effets.** Sort propre, en parallèle de MAIN |
| **None** | Coupe la source |

## Filtres (p. 148-149)

Par défaut les deux filtres sortent sur MAIN. Options : **Filter 1 ou Filter 2** (donc chaînage série des deux), Main, Direct, None ; Main et Direct font aussi apparaître le bouton enveloppe (ENV 1) (p. 149).

**Piège documenté** : même après avoir activé un filtre en cliquant son en-tête, **il reste grisé tant qu'aucun signal d'oscillateur ne lui est envoyé** (p. 148).

Réglages de canal filtre : PAN, **MIX** (dry/wet du filtre, recommandé à **100 %** pour la plupart des filtres, **sans effet sur les filtres de type Combs**), niveau.

## Les deux bus auxiliaires (p. 146-147, 149-150)

Oscillateurs et filtres disposent chacun d'un knob d'envoi vers **BUS 1**, **BUS 2** ou **les deux**. Le manuel les présente explicitement comme des **bus auxiliaires d'effets** et donne quatre justifications : cohérence sonore par réverb ou delay partagés, contrôle fin du wet/dry par source, **traitement parallèle** (il cite la compression parallèle), et économie de CPU puisqu'une seule instance de l'effet tourne.

Sortie des bus : Main par défaut, ou Direct, ou **vers l'autre bus**.

`[I]` La combinaison « knob BUS » plus « rack FX propre à chaque bus » constitue le mécanisme de send-retour de Serum 2, et le routage **Direct** est le seul vrai contournement post-FX.

**MUET** : le manuel ne dit nulle part si les envois BUS sont pris avant ou après le fader de niveau du canal. La notion de pre/post fader n'est jamais formulée.

## Glisser-déposer entre oscillateurs (p. 145)

| Geste | Effet |
|---|---|
| **Option/Alt + glisser** l'étiquette d'un canal sur un autre | Copie l'oscillateur **sans les modulations** |
| **Shift-Option / Shift-Alt + glisser** | Copie **avec** les modulations |
| **Glisser sans modificateur** | **Échange** les deux oscillateurs, assignations comprises |

---

# B. LE RACK D'EFFETS

## Structure (p. 152-158)

**13 processeurs différents**, utilisables dans n'importe quel ordre et combinaison, **y compris plusieurs instances du même**. Plus **3 modules splitter**. Trois racks : **MAIN, BUS 1, BUS 2**.

**Le flux du signal va du haut vers le bas** (p. 155). Il n'y a donc aucune notion de send interne à un rack : la structure est série et verticale. Les seuls chemins parallèles sont les **knobs BUS du mixer** et les **splitters**.

**MUET** : le nombre maximal de modules par rack n'est jamais chiffré.

## Gestes (p. 155-158)

- **Ajouter** : bouton « + », ou clic droit dans le rack.
- **Réordonner** : clic-glisser ; **une ligne jaune indique où le module va atterrir**.
- **Copier sans modulations** : Option/Alt-glisser. **Avec modulations** : Shift-Option / Shift-Alt-glisser vers un emplacement vide.
- **Bypass** : bouton par module, **rouge quand actif**. **Option/Alt-clic bascule le bypass de tous les FX du bus**, et cela marche aussi depuis la page MIXER (p. 157).
- Le manuel précise que le bypass est prévu pour un usage **temporaire** ; pour désactiver durablement, il recommande de **retirer** le module.
- **Vue étendue** : **Option-F / Alt-F**.

## Opérations de bus, clic droit sur le fond (p. 158)

Cut / Copy / Paste / Clear FX Bus · **Lock FX Bus** · Lock All FX Busses · Load / Save FX Bus.

**⚠ Piège documenté** : avec **Lock FX Bus**, les modules restent en place au changement de preset, **mais les assignations de modulation vers les paramètres du rack verrouillé sont effacées**.

## Modulation des paramètres d'effet (p. 159) — le point le plus important

« **You can modulate most FX parameters** » : on glisse une enveloppe ou un LFO sur la destination, comme pour les contrôles de synthèse. **MUET** : aucune liste des paramètres modulables ou exclus.

**Avertissement architectural décisif** : le rack FX est un process DSP **qui opère sur la somme de la sortie du moteur de synthèse, pas par voix**. Le manuel donne trois formulations : « les effets sont monophoniques », « les effets sont comme des inserts après Serum », comportement dit **paraphonique**, particulièrement avec l'effet Filter.

**Conséquence explicitement signalée** : sur une partie polyphonique, moduler un contrôle d'effet avec une source **par voix**, donc une enveloppe, fait **re-déclencher la modulation à chaque nouvelle note**.

Exception documentée : les bandes individuelles du COMPRESSOR en mode MULTIBAND acceptent des assignations via la matrice, et le manuel cite l'usage sidechain du bas du spectre pour dégager la place au kick ou à la basse (p. 163).

---

# C. LES 13 MODULES (p. 161-182)

Deux contrôles quasi communs : **MIX** (0 = dry, 100 = wet) et **LEVEL**. Exceptions : l'EQUALIZER n'a **pas** de MIX ; les splitters n'ont **que** LEVEL.

**1. BODE** — frequency shifter (p. 161). SHIFT (clic droit → **Retrig** pour redémarrer à chaque note) · RANGE · **DIR** (au centre, les deux canaux partent en directions opposées) · WIDTH · DELAY · BPM · FEED · BALANCE · BLUR.

**2. CHORUS** — **quatre voix, deux taps à gauche et deux à droite** (p. 162). RATE (**BPM activé : 8 mesures à 1/32 ; désactivé : 0 à 20 Hz**) · DELAY 1 et DELAY 2 (délais des deux paires stéréo) · DEPTH · FEEDBACK · **LPF/HPF** (filtre placé **après** le wet, **clic sur le label pour basculer**).

**3. COMPRESSOR** (p. 162-164). MODE **SINGLE** ou **MULTIBAND** · THRESH (**0 = 0 dB, 100 % = −120 dB**) · **RATIO : au maximum la mention Limit apparaît, et c'est un circuit DSP complètement différent, un vrai true peak limiter** ; l'attaque passe alors sur **0–10 ms** et le makeup sur **0–36 dB** ; clic droit → **Limiter Latency Comp** pour reporter la latence à l'hôte · ATTACK · RELEASE · GAIN (~30 dB en compresseur, 36 dB en limiteur) · en MULTIBAND : **X-LOW**, **BELOW** (ratio **sous** le seuil, donc compression ascendante), **X-HIGH**, **H / M / L**.

**4. CONVOLVE** (p. 164-165). IMPULSE · SIZE · TONE · **ϕ MIN** (phase minimale : **réponse en fréquence inchangée**, supprime l'écho) · PRE-DLY · ATTACK · DECAY · DAMP · IR GAIN. **On peut charger des IR externes par glisser-déposer ou clic droit › Load IR** ; l'option **Embed in Preset** (icône en haut à droite de l'affichage) apparaît alors (p. 165).

**5. DELAY** (p. 165-167). Trois modes : **NORMAL**, **PING-PONG**, **TAP→DELAY** (les deux delays passent en mono et en série). **Deux réglages par canal** : la case du haut est le temps de base, celle du bas un **offset scalaire**. **En glissant la case du bas, Serum affiche « Trip » à 133 % et « Dot » à 150 %** pour poser triolets et pointés. **⚠ Le Q est inversé** : la valeur maximale donne le filtrage minimal. **Double-clic sur l'affichage bascule un overlay de fréquence en temps réel.**

**6. DISTORTION** — **13 types**, dont **deux modes dual-waveshaper** (p. 167-169). OFF/PRE/POST (filtrage désactivé, avant ou après) · TYPE (**glisser pour morpher passe-bas → passe-bande → passe-haut**) · FREQ (clic droit → **Key Track**) · Q · DRIVE, **avec deux exceptions** : en **Downsample**, DRIVE contrôle la réduction de fréquence d'échantillonnage ; en **X-Shaper** et **X-Shaper (Asym)**, DRIVE morphe entre deux waveshapes. Le menu des types s'appelle **MODE** (`kParamMode`) ; TYPE est le fondu du filtre (p. 167-168).
**X-Shaper** : éditeur graphique X-Y, **DRIVE 0 % = forme A, 100 % = forme B**. La version **symétrique** a le silence en bas à gauche ; la version **Asym** a **le silence au milieu du graphe**, et fait ressortir les **harmoniques d'ordre pair** absentes d'une distorsion symétrique.
**MUET** : les 13 types ne sont pas énumérés dans le texte, seulement en image. Nommés au fil du texte : Tube (défaut), Downsample, X-Shaper, X-Shaper (Asym).

**7. EQUALIZER** — **deux bandes** (p. 169-170). Bande gauche : low shelf / peaking / **high pass**. Bande droite : high shelf / peaking / **low pass**. **Le GAIN est sans effet quand High Pass ou Low Pass est sélectionné.** Pas de MIX.

**8. FILTER** (p. 170-172). « Fonctionne exactement comme le filtre de synthèse par voix, mais tourne ici comme effet master. » **MG Low 6 par défaut.** CUTOFF (clic droit → Key Track ; **astuce du manuel : une enveloppe sur ce knob recrée certains comportements paraphoniques de synthés vintage**) · RES · DRIVE (clic droit → **Clean Mode** : pré-gain à **−24 dB** avec **boost de +24 dB après le filtre**) · **knob VAR variable selon le type**, étiquettes possibles : FAT, FREQ, MORPH, LP FRO, HP FRO, HL WID, DB +/−, SPREAD, DAMP, BOEUF, THRU, FORMNT, WIDTH, COMBFRO, SCREAM, STAGES, SMOOTH, PAIN, FRO2 · **PAN** (offset de cutoff entre gauche et droite, **sans effet au défaut de 50 %**).
Affichage : clic droit → trois modes, **Frequency Response**, **Frequency Response & FFT**, **Phase Response & FFT** ; **Option/Alt-clic les fait défiler**.

**9. FLANGER** (p. 172-173). RATE (BPM : 8 mesures à 1/32 ; sinon 0 à 20 Hz) · DEPTH · FEEDBACK · **PHASE** (**0 % = même phase G/D, 50 % = 180 degrés**, le balayage monte à gauche pendant qu'il descend à droite).

**10. HYPER / DIMENSION** (p. 173-174). **HYPER** = chorus à micro-delay, **1 à 7 voix**. **Le manuel recommande explicitement d'utiliser HYPER plutôt que des réglages d'unisson élevés pour économiser du CPU.** RATE · UNISON (**mettre à 0 pour n'utiliser que DIMENSION**) · DETUNE · **RETRIG** (remet toutes les voix à un offset nul, effet « zap laser » à chaque note-on, utile en monophonique).
**DIMENSION** = pseudo-stéréo par **quatre lignes de delay sommées en opposition de phase**, modulées lentement. SIZE.

**11. PHASER** (p. 174-175). RATE · **POLES** (nombre de pôles empilés) · DEPTH · **DEPTH 2** (offset entre étages) · FREQ · FEEDBACK · PHASE.

**12. REVERB** — **version modifiée de l'algorithme Tal Reverb**, **5 types**, **PLATE par défaut** (p. 175-177).
Chaque type a **sa propre** liste (pas de cumul d'un type à l'autre) ; tous commencent par LO CUT · HI CUT · SIZE · PRE-DLY :
- **PLATE** : + DAMP · **WIDTH** (seul type avec WIDTH)
- **HALL** : + DECAY · **SPIN RATE** · **SPIN DEPTH** (ni DAMP ni WIDTH)
- **VINTAGE** : + **ER SIZE** · DECAY · DAMP · **DIFF A** · **DIFF B** · **CHORUS** (valeur du haut = vitesse, valeur du bas = profondeur de pitch) ; ni WIDTH ni SPIN
- **NITROUS** : + FEEDBACK · DIFFUSION · **MODE à 5 valeurs : Space, Marble, Rectangle, Hexagon, Box** · **CHORUS** (haut = vitesse, bas = profondeur)
- **BASIN** : + FEEDBACK · CHORUS

**13. UTILITY** (p. 182). **POLARITY INV sur le canal gauche et le droit séparément** · LPF · HPF · **MONO BASS + FREQ** · WIDTH · PAN.

## Les trois splitters (p. 177-181)

Ce sont les seuls vrais bus parallèles **à l'intérieur** d'un rack.

| Splitter | Racks | Contrôles |
|---|---|---|
| **L/H** | 2 (LOWS, HIGHS) | LOWS · **SPLIT FREQ** · HIGHS · LEVEL |
| **L/M/H** | 3 (LOWS, MIDS, HIGHS) | **deux SPLIT FREQ** · LEVEL |
| **M/S** | 2 (MID, SIDE) | LEVEL seulement, **aucun contrôle de fréquence** |

La vue liste montre **tous** les racks, la vue rack n'affiche **que** le rack sélectionné. **Chaque panneau a son propre bypass.**

---

# D. LE MODULE CLIP (p. 219-243)

## Ce que c'est

Un **clip MIDI interne à Serum**, contenant notes et données de contrôleur, qui joue le patch courant. **12 slots par banque.**

## Réglages globaux (p. 221)

**TRIGGER MODE** : MONO (un clip à la fois) ou POLY. **EDIT ALL** : toute édition s'applique à tous les clips. Raccourci équivalent : **maintenir Option/Alt en éditant**.

## CLIP SETTINGS (p. 233-234)

| Champ | Contenu |
|---|---|
| **LENGTH** | En mesures, temps et doubles-croches |
| **KB SPAN** | **Mono** et **Poly** jouent le clip transposé **relativement à C3** · **Offset** donne un départ de lecture différent par note · **Off** |
| **TRANS** | Transposition |
| **MODE** | **Random** · **Rand.No Dup** · **Rand.Start** · **Rand.End** · **Static** (seuls les événements à la position de départ sont envoyés, la tête ne bouge pas : utile pour déclencher un accord ou un jeu de valeurs de macros). Pour les modes aléatoires, on règle aussi le temps qui découpe le clip en slices |
| **RATE** | Vitesse de lecture |
| **LAUNCH QUANT** | Intervalle de synchronisation au DAW |
| **RETRIG** | Redémarre, ou se recale sur l'horloge |
| **VELO TRIG** | Les vélocités du clip sont mises à l'échelle par la vélocité entrante |
| **NOTE GATE** | Un note-off arrête ou non la lecture |

**MUET** : le manuel écrit « Note the following about the available options » pour MODE, il ne prétend donc pas donner la liste complète. Aucune option « Normal » n'est décrite. Les valeurs de division de RATE et LAUNCH QUANT ne sont pas énumérées.

## Piano roll (p. 224-232)

**Grille 1/16 par défaut.** Double-clic pour ajouter une note, **la dernière ajoutée apparaît en orange**. Double-clic sur une note pour la supprimer.

Sélection de **plage temporelle** : les notes chevauchant le bord sont coupées, et **coller une plage écrase toutes les notes existantes dans la destination**, contrairement au collage de notes.

**Raccourcis** (p. 226-227) : Cut ⌘X · Copy ⌘C · Paste ⌘V · **Duplicate ⌘D** · **Chop ⌘U** · **Conform to Scale ⌘K** · **Legato ⌘L** · **Mute = touche 0** · **Quantize ⌘Q** · **Reverse ⌘R** · **Scale Time 50 % = /** · **Scale Time 200 % = \*** (changent temps et durée **sans changer la longueur du clip**) · **Double Entire clip ⌘E** · Select All ⌘A. Flèches : ↑↓ un demi-ton, **Shift ↑↓ une octave**.

**⚠ Deux conditions pour que les raccourcis marchent** : la grille de notes ou la lane d'automation doit avoir **le focus clavier** (une icône de clavier en haut à droite l'indique), **et** la préférence « Keyboard shortcuts » doit être sur ON dans le volet GLOBAL.

**Fold** (p. 230-231) : replie pour n'afficher que les notes utilisées. **Quand une clé et une gamme sont sélectionnées, le repli ne montre que les notes de la gamme.** **⌘/Ctrl + clic sur fold** affiche gamme **et** notes utilisées, **fond bleu dans la gamme, gris hors gamme**.

**Marqueur de start offset** (p. 232-233), distinct des drapeaux de début et de fin. Menu contextuel : **Wrap Clip to Begin Here** (déplace notes et automation, **tout ce qui précédait est enroulé à la fin**) et **Quantize**.

## Enregistrement (p. 237-238)

**OVERDUB** (boucle, ajout à chaque passage) ou **EXTEND** (étend la timeline), commutables à tout moment. **Les notes jouées apparaissent en rouge**, un bouton commit les valide et elles passent **en vert**. À l'arrêt, tout devient vert **mais le clip continue de jouer** : il faut cliquer le stop du slot.

## Gestion (p. 235-236)

Clic droit : Rename · **Copy Clip** (**impossible d'une instance de Serum à une autre**) · Paste · Erase · **Set as Preview Clip**.
Clavier CLIP : **la touche s'allume en vert**, avec un petit indicateur qui **clignote au rythme des notes**.

## Macros (p. 241-243)

Assignation par **glisser-déposer du sélecteur de macro sur le contrôle** ; **un signe + indique une destination valide**, et **toutes ne le sont pas**. Un chiffre à côté de MACRO 1 indique le nombre de destinations. On peut **enregistrer une automation de macro dans un clip en glissant les knobs**.

## MIDI OUT (p. 239-240)

**Off** (défaut) · **Clip Player** (module CLIP seul, **sans quantification clé/gamme**) · **On** (à travers le module ARP si activé, **avec** quantification).

Page 265 (chapitre ARP) : **On** = « clip player **et** arpégiateur », sans parler de quantification : c'est un résumé de la p. 239, pas une contradiction. L'affichage montre toujours les notes générées ; l'envoi vers une autre piste est possible avec On ou Clip Player, mais seul Logic Pro X est décrit (p. 239-240) : **procédure Live MUET**.

## MUET sur les clips

Le manuel mentionne une « **automation lane** » (p. 227) et « velocity and expression » (p. 233) **sans jamais chiffrer le nombre de lanes d'un clip, ni lister les paramètres automatisables**. Le manuel compte **huit macros** (p. 206) ; parmi les réglages de clip assignables, au moins RATE (« Clip 1 Rate », p. 243), la liste complète reste MUET.

---

# E. L'ARPÉGIATEUR (p. 244-266)

**12 arpégiateurs par banque.** Six volets : GLOBAL, PATTERN, TRANSPOSE, PLAYBACK, RETRIGGER, VELOCITY.

## PATTERN (p. 248)

Le champ **SHAPE** offre « des formes standard up/down ainsi que des formes moins familières comme **Converge** et **Diverge**, plus une collection de formes aléatoires ».

**MUET, et c'est important** : **la liste des SHAPE n'existe que sous forme d'image de menu.** Vérification faite sur les 354 pages, aucune liste textuelle. Les seules formes nommées dans le texte sont Converge, Diverge, Pattern, et les noms de slots par défaut **Up (1/16)** et **Down (1/32)**.

RATE en **BPM ou HZ**, avec deux boutons **TRIP** et **DOT**. Valeurs de division non énumérées.

**Astuce du manuel** pour explorer les formes : activer **LATCH**, jouer un accord, puis faire défiler les shapes en observant le clavier Serum.

## Éditeur de pattern (p. 249-253)

**PATTERN SETTINGS** :

| Champ | Valeurs |
|---|---|
| **LENGTH** | Mesures, temps, doubles-croches |
| **MODE** | **8 valeurs, liste complète** : Normal · Reverse · Pendulum · Random · Rand Start · Rand End · One Shot · Static |
| **TIME** | Pour les modes aléatoires, **de 1/16 de note à 4 mesures** |
| **STEP MODE** | **4 valeurs** : Normal · New Only · **Chord** (déclenche toutes les notes tenues à chaque pas, **le voicing étant déterminé par les numéros de pas**) · Chord (new). Les modes « new » ne déclenchent un pas que si la note entrante arrive **exactement au même instant** |
| **WRAP** | Traitement des pas au-delà du nombre de touches tenues |
| **PITCH** | Transposition du wrap, **0 à 24 demi-tons** |
| **RANGE** | Transposition des pas hors du nombre de touches tenues |

**Lanes nommées dans l'éditeur d'arp** : **ACCENT** (double-clic pour accentuer un événement) et **STRUM** (double-clic pour ajouter du strumming). Le manuel parle aussi d'« automation lanes » au pluriel, **sans en donner ni le nombre ni les destinations**.

**MUET** : le nombre maximal de pas d'un pattern.

## TRANSPOSE — 18 formes, liste complète (p. 254-261)

**SHIFT** est le montant de transposition à chaque répétition, positif ou négatif. **RANGE** est le nombre de répétitions. **Clic droit sur RANGE** pour choisir la forme.

Up · Down · Up/Down · Down/Up · Up+Down · Down+Up · Thumb Up · Thumb UD · Pinky Up · Pinky UD · Converge · Diverge · Con+Diverge · Chord · Random · Rnd.NoDup · Rnd.Drift · Rnd.Once

Précisions : **Up/Down et Down/Up** transposent puis **inversent immédiatement** ; **Up+Down et Down+Up repartent** dans l'autre sens ; **Thumb** rejoue l'arpège original entre chaque transposition ; **Pinky** transpose au maximum puis alterne ; **Chord** joue l'accord au lieu de l'arpège ; **Rnd.Drift** est aléatoire avec biais de dérive ; **Rnd.Once** tire une fois puis conserve le pattern.

**MUET, et contre-intuitif** : **il n'existe aucun paramètre « octaves »** dans l'arpégiateur de Serum 2. `[I]` L'équivalent est le couple SHIFT/RANGE : SHIFT à 12 demi-tons avec RANGE = N donnerait un arpège sur N octaves, mais le manuel ne le formule nulle part.

## PLAYBACK (p. 261-262)

**LATCH** — **⚠ quand l'arp est activé, les messages MIDI CC64 (sustain) contrôlent le latch au lieu du sustain de note normal.**
**THRU** — désactivé, l'arpégiateur consomme l'entrée ; activé, les notes passent et sont jouées.
**OFFSET** · **REPEATS** · **GATE** (longueur des notes, **relative au RATE**) · **CHANCE** (probabilité qu'une note soit jouée ; **clic droit → Pre** applique CHANCE **avant** que le pattern n'avance, ce qui garantit que la note suivante est toujours la suivante de la séquence).

**MUET** : aucune plage numérique pour OFFSET, REPEATS, GATE ni CHANCE.

## RETRIGGER et VELOCITY (p. 262)

RETRIGGER : **LAUNCH** · **RATE** · **NOTE** · **FIRST** (seulement sur la première note entrante, cas d'un accord tenu).
VELOCITY : interrupteur · **RETRIG** · **DECAY** (vitesse de changement) · **TARGET** (vélocité visée). L'ensemble fait monter ou descendre les vélocités de sortie au fil du temps.

## Le swing n'est pas dans l'arpégiateur (p. 269)

**Aucun réglage de swing dans le chapitre arpégiateur**, mais le SWING du clavier agit sur la grille des éditeurs CLIP **et** ARP (p. 25) et sur les LFO en BPM (p. 192). Il se trouve sur la page « Using the Keyboard » : champ **SWING** global, **OFF par défaut**, avec un champ de division qui apparaît dès qu'on quitte OFF.

**La plage de valeurs dépend du DAW hôte** : Serum tente de reproduire la convention de l'hôte. Le manuel cite **Ableton Live : 12,5 % à 87,5 %** et FL Studio : −150 % à 150 %.

## Déclenchement (p. 263-264)

Cliquer un slot le **sélectionne** (bouton play violet) ; au lancement, le bouton change pour montrer l'arp qui joue. **Pour arrêter un arp il faut couper l'entrée MIDI** : relâcher les touches, arrêter un clip, ou désactiver le latch. Sur le clavier ARP, **la touche s'allume en violet** et re-presser la même touche **relance** l'arp, contrairement aux clips où elle l'arrête.

---

# F. Synthèse des chiffres

13 modules FX · 3 splitters · 3 racks (MAIN, BUS 1, BUS 2) · flux série haut vers bas · 2 bus auxiliaires · 4 options de routage par canal · **Direct contourne filtre ET effets** · **les FX opèrent sur la somme, pas par voix** · 12 clips par banque · 12 arps par banque · TRANSPOSE du clavier −24…+24 st (p. 267) · vélocités d'OSC Mapping 1–127 (p. 273) · MIDI Input Trigger Octave : par défaut l'octave MIDI la plus basse lance clips et arps (p. 241, 266) · 8 macros (p. 206) · grille 1/16 par défaut · MODE de pattern : 8 valeurs · STEP MODE : 4 valeurs · formes de transposition : **18** · TIME aléatoire : 1/16 à 4 mesures · PITCH de wrap : 0 à 24 demi-tons · **KB SPAN relatif à C3** · swing Ableton : 12,5 à 87,5 %.
