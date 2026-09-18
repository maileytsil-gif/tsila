# Instruments d'Ableton Live 12 — fiche de référence

Dépouillement du **manuel officiel**, chapitre 30 (référence des instruments) et chapitre 9 (modes de warp). Les numéros de section sont ceux du manuel. `[I]` = déduction. **MUET** = le manuel ne dit rien, et je ne comble pas.

---

# 1. WAVETABLE

## Matrice de modulation (§30.13.5)

**Il n'y a pas de liste de destinations, et c'est volontaire.** « Cliquez sur un paramètre dans l'instrument pour le faire apparaître temporairement dans la matrice. Si vous lui appliquez une modulation, il y reste. Sinon il disparaît dès que vous cliquez un autre paramètre. » **N'importe quel paramètre cliquable est donc une destination potentielle.**

Les onglets **Matrix et MIDI partagent les mêmes lignes**.

**Cinq sources internes** : Amp env, Env 2, Env 3, LFO 1, LFO 2.
**Six sources MIDI** : Velocity, **Note**, Pitch Bend, Aftertouch, Modulation Wheel, **Random**.

Deux chiffres à retenir :
- **Note** : la plage est **centrée sur C3**, et assignée à Filter Frequency **à 100 %, le filtre suit exactement la note jouée**. C'est le key tracking parfait.
- **Random** : valeur recalculée **à chaque note déclenchée**.

### Additif contre multiplicatif — distinction rarement connue

| Mode | Comportement | Neutre |
|---|---|---|
| **Additive** | Les sources s'additionnent, la somme s'ajoute à la valeur du paramètre | **0** |
| **Multiplicative** | Les sources se multiplient, le produit multiplie la valeur | **1**, minimum 0 |

Cibles multiplicatives nommées : **Sustain** et **Initial** des enveloppes, **Amount** du LFO, **Amount** global de la matrice, **Volume** global, **Unison Amount**.

`[I]` Conséquence pratique : sur une cible multiplicative, une modulation ne peut que **réduire** la valeur, jamais l'augmenter au-delà du réglage. C'est pour ça qu'un LFO sur Unison Amount ne fait qu'amincir le son, jamais l'élargir.

**Time** (curseur de matrice) : met à l'échelle les temps de tous les modulateurs. **Négatif = plus rapide, positif = plus lent.** Détail subtil : moduler Time avec une enveloppe **n'affecte pas le modulateur assigné**, mais ce modulateur continue de se mettre à l'échelle vers les autres destinations.

## LFO (§30.13.6.1)

Deux LFO, **cinq formes**, avec un curseur **Shape** dont l'effet change selon la forme :

| Forme | Effet de Shape |
|---|---|
| Sine, Saw | pente croissante ou décroissante |
| Triangle | morphe la symétrie, **Ramp → Triangle au centre → Saw** |
| Square | **largeur d'impulsion** |
| Random | distribution des valeurs extrêmes |

**Offset** décale la phase de départ, et **ne peut pas être modulé**. **Attack** est un fade-in après Note On. **Retrigger** remet le LFO à sa phase de départ à chaque note, ce qui « peut créer des formes hybrides si le LFO est retriggé avant d'avoir fini son cycle ».

**⚠ Correction** : les modes de boucle **None / Trigger / Loop** appartiennent aux **enveloppes**, pas aux LFO. Le manuel ne donne **aucun mode de boucle** aux LFO de Wavetable.

## Les trois enveloppes (§30.13.6)

**Amp, Env 2, Env 3.** Trois paramètres n'existent **pas** sur l'enveloppe d'amplitude : **Initial**, **Peak**, **Final**.

**Slopes** : positif = l'enveloppe bouge vite au début puis ralentit · négatif = elle reste plate puis accélère à la fin · zéro = linéaire.

**Modes de boucle** : **None** (tient le sustain jusqu'au Note Off) · **Trigger** (joue tous les segments dès le Note On, **le sustain n'est pas tenu**) · **Loop** (boucle l'enveloppe entière **jusqu'à la fin de la voix**).

## Routage des filtres (§30.13.4)

| Mode | Comportement |
|---|---|
| **Serial** | Tous les oscillateurs vers Filtre 1, puis Filtre 1 vers Filtre 2. **Le Sub est routé vers les deux filtres** |
| **Parallel** | Les deux oscillateurs principaux vers Filtre 1 **et** Filtre 2. Sub vers les deux |
| **Split** | Osc 1 → Filtre 1, Osc 2 → Filtre 2. **Le Sub est coupé en deux.** Si l'un des filtres est éteint, le signal de l'oscillateur correspondant **reste audible** |

**Astuce documentée** : « Si les deux oscillateurs principaux sont désactivés et les deux filtres actifs, **Split permet un traitement supplémentaire du seul Sub**. »

## Tables

**MUET** : aucune liste de catégories, aucun chiffre sur le nombre de tables fournies.

Ce que le manuel dit : import de n'importe quel **WAV ou AIFF** par glisser-déposer sur la visualisation, et les sélecteurs pointent alors vers le **dossier** du sample, ce qui permet d'auditionner tout le dossier aux flèches. Le **Raw mode** désactive le traitement automatique de réduction d'artefacts : « utile pour des fichiers préparés comme wavetable, mais peut aussi être détourné pour des sons imprévisibles, bruités ou glitchés ».

**[Hors manuel, relevé sur le disque]** Les 270 presets d'usine référencent **146 tables distinctes**. Les plus employées : **Basic Shapes dans 100 presets**, Quad Saw et Sines 1 (14), FOF (12), Voice Harmonics (9), Amber, Echoes, VOSM (8). Les familles se lisent dans les noms : émulations (JUN, JUP, JX10, OB6, MG Memo, Logue, Sys8, JN60), formants et voix (FOF, VOSM, Vocal Sines, Harsh Vowel, Stepped Vowels), bruit, sweeps, harmoniques, subs.

## Compléments (§30.13.2, §30.13.8)

- **FM** : Tune à **50 % ou −50 % = une octave**, **100 % ou −100 % = deux octaves** ; entre ces valeurs, **ratios inharmoniques**, « idéal pour créer des harmoniques bruitées ».
- Les valeurs des deux paramètres d'effet **ne changent pas** quand on change de type d'effet, pour comparer FM, Classic et Modern à réglages identiques.
- **Glide n'est actif qu'en Mono** ; Poly Voices n'est actif qu'en Poly.

---

# 2. OPERATOR

## Les 11 algorithmes

**MUET** : le manuel ne les décrit par aucun texte, seulement une image. Ce qui suit est une **lecture de la figure officielle**, donc géométrique et non citée.

Code couleur de l'interface : A jaune, B cyan, C bleu, D orange. Le signal descend, la rangée du bas est audible.

| # | Structure | Lecture |
|---|---|---|
| 1 | D→C→B→A | pile complète, FM la plus profonde, 1 porteuse |
| 2 | (C+D)→B→A | deux modulants sur B |
| 3 | C→B ; (B+D)→A | A modulé par B **et** D |
| 4 | D→(B et C) ; (B+C)→A | modulant partagé, deux modulants sur A |
| 5 | D→C→(B et A) | C module les deux porteuses |
| 6 | D→C→B ; A indépendante | pile de 3 + une porteuse pure |
| 7 | (B+C+D)→A | trois modulants sur une porteuse |
| 8 | B→A ; D→C | deux paires FM parallèles |
| 9 | D→(A, B et C) | un modulant, trois porteuses |
| 10 | D→C ; A et B indépendantes | 3 porteuses, une paire FM |
| 11 | A, B, C, D côte à côte | quatre porteuses = **synthèse additive** |

Le sélecteur d'algorithme est **automatisable et modulable en temps réel**, comme n'importe quel paramètre.

## LFO (§30.9.3, §30.9.10.5)

« Le LFO peut pratiquement être considéré comme un **cinquième oscillateur**. Il tourne à des fréquences audio. »

| Plage | Valeurs |
|---|---|
| **Low** | de **50 secondes à 30 Hz** |
| **Hi** | de **8 Hz à 12 kHz** |
| **Sync** | calé sur le tempo |

**Rate < Key à 100 % : le LFO double sa fréquence par octave**, donc il fonctionne comme un oscillateur normal.

**Dest. A** : boutons on/off vers A, B, C, D et **FIL** (cutoff). **Dest. B** : une destination supplémentaire dans la liste des cibles. **LFO Amount met à l'échelle les deux.**

Formes : classiques + **S&H** + **Noise**, qui est un **bruit filtré passe-bande**. Toutes sont band-limited.

**Conseil du manuel** : « la FM sert à faire d'excellentes percussions, et le LFO en forme Noise est **la clé des bons hi-hats et snares** ».

## Filtre (§30.9.5, §30.9.10.4)

Mêmes types et circuits Cytomic que Wavetable. Quatre sources de modulation du cutoff : **Freq < Vel**, **Freq < Key**, enveloppe, LFO.

Chiffres : **Freq < Key à 100 % = la fréquence double par octave, centre C3**. **Filter Frequency < Envelope à 100 % = environ 9 octaves de déplacement.**

**Play by Key** (menu contextuel du bouton Freq) règle automatiquement **Freq < Key à 100 % et le cutoff à 466 Hz**.

**Waveshaper** après le filtre : sélecteur **Shaper**, **Shp. Drive**, **Dry/Wet**. **À 0 %, le shaper et son drive sont bypassés.**

`[I]` **Filter Q (Legacy)** et **Filter Res** sont deux cibles distinctes, la première pour les anciens types. Utile si un vieux set est rechargé.

## Enveloppe de hauteur (§30.9.4, §30.9.10.3)

**Pitch Env Amount** : **100 % = le changement de hauteur est exactement défini par les niveaux** ; **−100 % inverse le signe**.

Destinations A à D **et LFO**, plus une Dest. B supplémentaire.

**End** : niveau atteint **après** le relâchement, propre aux enveloppes de pitch et de filtre. La vitesse de ce segment est le Release.

**Les pentes ajustables n'existent que sur les enveloppes de filtre et de pitch.** Les enveloppes d'oscillateur ont une attaque linéaire, un decay et un release exponentiels.

**Astuce du manuel, à deux étages** : si l'enveloppe de pitch n'est appliquée qu'au LFO et qu'elle boucle, elle sert de **second LFO** modulant le rate du premier. Et comme l'enveloppe du LFO peut elle-même boucler, elle sert de **troisième LFO** modulant l'intensité du premier.

## Les sept enveloppes et leurs modes (§30.9.4)

Une par oscillateur, plus filtre, pitch et LFO. Chaque enveloppe d'oscillateur a **trois temps et trois niveaux**.

| Mode | Comportement |
|---|---|
| **Loop** | Retrigge si l'enveloppe atteint le sustain alors que la note est tenue. Vitesse = **Loop Time** |
| **Beat** | Redémarre après le temps choisi dans **Repeat**, en fraction musicale, **mais les notes ne sont pas quantifiées** : « si vous jouez un peu à côté, la répétition sera parfaite mais restera à côté » |
| **Sync** | **La première répétition est quantifiée au 16e le plus proche**, donc toutes les suivantes sont calées. **Ne fonctionne que si le morceau joue**, sinon se comporte comme Beat |
| **Trigger** | **Note Off ignoré.** Idéal pour les sons percussifs |

Anti-clic documenté : une enveloppe bouclée **redémarre depuis son niveau réel** et rejoint le Peak au rythme de l'Attack.

**Le Time global ne met pas à l'échelle les valeurs musicales des modes Beat et Sync.**

## Global (§30.9.6, §30.9.8, §30.9.10.1)

- **Voices jusqu'à 32**, mais « un réglage entre **6 et 12** est plus réaliste vu le CPU ». **Voices = 1 fait jouer les voix qui se chevauchent en legato : les enveloppes ne sont pas retriggées**, seule la hauteur change.
- **Interpolation** désactivée : « certains timbres sonnent plus rugueux, **surtout la forme Noise** ».
- **Antialias** activé par défaut sur les nouveaux patchs.
- **Tone** : plus haut = plus brillant **et plus sujet à l'aliasing**.
- **⚠ CPU** : « **éteindre les oscillateurs ne fait PAS économiser de CPU** ». Seuls comptent le filtre, le LFO, Interpolation, Antialias, Spread et le nombre de voix.
- Les cinq sources MIDI peuvent chacune être mappées à **deux destinations**.

## Liste complète des cibles de modulation (§30.9.10.2)

Off · OSC Volume A/B/C/D · OSC Crossfade A/C · OSC Crossfade B/D · **OSC Feedback** (ne s'applique qu'aux oscillateurs non modulés) · OSC Fixed Frequency · **FM Drive** (module le volume de **tous les oscillateurs qui en modulent d'autres**, donc le timbre) · Filter Frequency · Filter Q (Legacy) · Filter Res · Filter Morph · Filter Drive · Filter Envelope Amount · Shaper Drive · LFO Rate · LFO Amount · Pitch Envelope Amount · Volume · Panorama · Tone · Time.

`[I]` **FM Drive est la cible la plus musicale pour un growl** : une seule modulation change la brillance FM de toute la structure sans toucher au filtre.

## Glide et Spread (§30.9.7)

**Glide polyphonique.** Avec Glide activé, **toutes les enveloppes ne sont pas retriggées si les notes sont jouées legato**. Le manuel ne mentionne **pas** de modes Glide et Portamento séparés dans Operator, contrairement à Simpler et Sampler.

**Spread** : deux voix par note, panées et désaccordées. **L'application dépend de la valeur de Spread au moment du Note On**, d'où l'astuce : une séquence où Spread reste à 0 et n'est monté que sur certaines notes fait jouer ces notes en stéréo et les autres en mono. **Très gourmand en CPU.**

**Transpose global affecte les notes déjà en train de jouer.**

---

# 3. DRIFT

## Oscillateurs (§30.3.2)

**Osc 1, sept formes** : Sine, Triangle, **Shark Tooth**, **Saturated**, Saw, Pulse, Rectangle. « Shark Tooth et Saturated sont **propres à Drift** ; Shark Tooth est basée sur une forme analogique Moog classique, **Saturated marche bien pour les basses**. »

**Osc 2, cinq formes** : Sine, Triangle, Saturated, Saw, Rectangle. Oct et Detune.

**Shape**, sur Osc 1 seulement, a un effet « similaire à une modulation de largeur d'impulsion ». **Shape Mod peut introduire de la modulation même si Shape lui-même est à 0 %.**

**Pitch Mod** : deux emplacements source. « En appliquant une modulation de hauteur avec un LFO en **mode Ratio**, il est possible de **générer des sons FM**. »

### Les deux points de saturation, chiffrés

Gain par défaut **−6,0 dB**. « Il y a **deux points de saturation dans les circuits du filtre**, un avant et un après. Le premier s'active quand on **dépasse −6,0 dB**, le second **au-dessus de 0,0 dB** », ce qui produit « une distorsion complexe comparable à celle du hardware analogique ».

Les flèches à droite des gains permettent de **contourner complètement le filtre** par source.

## Filtre (§30.3.3)

**Type I = 12 dB/oct**, filtre **DFM-1** qui « réinjecte davantage de sa propre distorsion ». **Type II = 24 dB/oct**, **Cytomic MS2**, Sallen-Key à soft clipping **limitant la résonance**.

**Key** : **0,00 = aucune influence** de la hauteur ; **1,00 = fréquence plus basse dans le grave, plus haute dans l'aigu**.

## Enveloppe cyclique (§30.3.4)

Env 2 peut devenir une **enveloppe cyclique** : « fonctionne comme une modulation LFO **qui redémarre à chaque note MIDI entrante** ».

**Tilt** déplace le point médian, et **aux valeurs extrêmes affecte aussi les pentes**. **Hold** est la durée pendant laquelle l'enveloppe reste au maximum. **Quatre modes de temps** : Rate (Hz), **Ratio**, Time (ms), Sync.

## LFO (§30.3.5)

Mêmes quatre modes de temps. **Neuf formes** : Sine, Triangle, Saw Up, Saw Down, Square, Sample & Hold, **Wander** (un S&H « avec une forme en S qui **interpole entre deux valeurs** »), **Linear Envelope** et **Exponential Envelope** (decay **one-shot**).

## Matrice (§30.3.6)

**Trois emplacements**, **huit sources**, **onze destinations** — liste exhaustive : Osc 1 Gain, Osc 1 Shape, Osc 2 Gain, Osc 2 Detune, Noise Gain, LP Frequency, LP Resonance, HP Frequency, LFO Rate, Cyc Env Rate, Main Volume.

## Modes de voix, avec leur coût (§30.3.7)

| Mode | Voix par note | Polyphonie à Voices = 32 |
|---|---|---|
| **Poly** | 1 | **32 notes** |
| **Stereo** | 2 | **16 notes** |
| **Mono** | 4 en unisson, une note à la fois | — |
| **Unison** | 4 | **8 notes** |

**Mono Thickness** règle le volume relatif des quatre voix : **à 0, une seule voix est jouée**.

**Le paramètre Drift** : « ajoute une légère variation à chaque voix, affectant hauteur et cutoff. **Chaque voix a une randomisation différente.** À valeurs élevées, les écarts entre oscillateurs et filtre s'élargissent. »

## Comparaison avec Analog et Wavetable

**MUET** : aucune comparaison explicite n'existe dans le manuel.

`[I]` D'après les architectures respectives : Analog a deux oscillateurs plus un générateur de bruit, **deux filtres, deux amplis, trois enveloppes, deux LFO**. Wavetable a deux oscillateurs plus sub, deux filtres, trois enveloppes, deux LFO et une matrice à cibles libres. Drift n'a **qu'un seul chemin de filtre, deux enveloppes, un LFO et une matrice à 3 slots et 11 destinations fixes** — le plus contraint, mais le seul à offrir la **randomisation par voix** et **quatre modes de temps** sur ses modulateurs. Pour du deep ou minimal house, c'est le seul des trois à donner « désaccord vivant plus saturation de filtre » sans empiler de devices.

---

# 4. MELD (§30.8)

## Architecture

**Deux moteurs polyphoniques indépendants**, chacun avec son filtre, ses enveloppes, ses **deux LFO** et sa matrice. Désactiver un moteur désactive aussi son filtre ; l'inverse n'est pas vrai.

Hauteur : **Octaves, Semitones, Cents**. Avec **Use Current Scale**, l'unité passe en **degrés de gamme**.

## 24 types d'oscillateurs, chacun avec deux macros

Basic Shapes · Dual Basic Shapes · Noisy Shapes · Square Sync · Square 5th · Sub · **Swarm Sine / Triangle / Saw / Square** (macros Motion et **Spacing**, qui « fond vers des accords de plus en plus complexes ») · Harmonic Fm · Fold Fm · **Squelch** (Amount = profondeur FM, Feedback) · Simple Fm · Chip · **Shepard's Pi** (Rate : **0 à 49,9 = descendant, 50,1 à 100 = ascendant, 50 = immobile**) · Tarp · Extratone · **Noise Loop** · Filtered Noise · Bitgrunge · **Crackle** · **Rain** · **Bubble** · **Chord** (quatre sawtooth superposées ; avec Use Current Scale les accords suivent la gamme, **sinon majeur avec la note MIDI comme fondamentale**).

**Six sont scale-aware** : Dual Basic Shapes, Swarm Sine, Swarm Triangle, Swarm Saw, Swarm Square, Chip.

## 17 filtres

SVF 12 et 24 dB (macro **L-B-H-N** morphant entre low-pass, band-pass, high-pass et notch) · MS2 (LP et HP) · OSR (**band-pass seulement dans Meld**) · LP Crunch 12 dB · **LP Switched Res** (artefacts de downsampling, macro Lofi) · Filther · Eq Peak · Eq Notch · **Phaser** (six étages, delayless, feedback inversé) · **Redux** · **Vowel** · Comb + et Comb − · **Plate Resonator** (32 premiers modes d'une plaque rectangulaire) · **Membrane Resonator** (32 premiers modes d'une membrane circulaire).

## Modulation

Enveloppes avec **trois modes de boucle** : Trigger, Loop, et **AD Loop** (seules Attack et Decay sont bouclées).

**LFO 1** : six types, plus un panneau **LFO 1 FX** avec deux emplacements offrant chacun **dix-huit types d'effets** appliqués en série. Point clé : **LFO 1 et LFO 1 FX sont deux sources indépendantes** dans la matrice.

**Osc Key Tracking** désactivé fait jouer **un C3 constant** pour toutes les notes, « utile pour les drones ou les sons percussifs ».

**Glide** existe en **Portamento** (continu) et **Glissando** (**par paliers discrets**, en degrés de gamme si scale awareness est actif), et **fonctionne en Mono comme en Poly**.

**Stacked Voices** duplique **les deux moteurs** pour chaque note et « peut créer une charge CPU lourde ».

**⚠ Spread n'a aucun effet s'il n'est pas assigné à une cible dans la matrice.**

---

# 5. SIMPLER ET SAMPLER

## ⚠ Sampler n'a pas de warp (§30.11.7)

« **La fonctionnalité de warping et de slicing de Simpler n'est pas disponible dans Sampler**, et les presets qui les utilisent sonneront et se comporteront très différemment » après conversion.

## Modes de warp (chapitre 9.3)

Préambule : « Les Warp Modes utilisent différentes techniques de **synthèse granulaire** en répétant ou omettant des segments appelés **grains**. »

**Beats** — granulation préservant les transitoires. **Transient Envelope : 100 = aucun fade, 0 = fades longs.** « Valeurs hautes pour lisser les clics, **valeurs basses pour créer des effets de gate rythmique**. » *Loop Back-and-Forth* « donne souvent une qualité élevée, surtout aux **tempos lents** ».

**Tones** — pour l'audio à hauteur définie. Grain Size est **approximatif** : « la taille réelle est déterminée par la **clarté des changements de hauteur** ».

**Texture** — pour les sons sans hauteur claire, nappes, bruit, drones. « Également excellent pour le sound design. » **Différence essentielle avec Tones** : « Grain Size détermine la taille utilisée, mais **contrairement à Tones, les caractéristiques tonales ne sont pas prises en compte** ». C'est vous qui imposez la taille.

**⚠ Le paramètre Flux s'appelle désormais Fluctuation** dans le manuel Live 12 : « introduit de l'aléatoire dans le traitement du sample ». **MUET** sur la plage et l'unité de Grain Size et Fluctuation.

**Re-Pitch** — « doubler la vitesse monte la hauteur d'une octave ». **Les contrôles de transposition du sample sont désactivés dans ce mode.**

**Complex / Complex Pro** — **Formants à 100 %** préserve les formants d'origine, **aucun effet si la transposition n'est pas modifiée**. **Envelope : défaut 128**, valeurs plus basses pour les samples aigus, plus hautes pour les graves. Modes gourmands, le manuel recommande freeze ou resampling.

## Simpler

**Trois modes** : **Classic** (ADSR complet, boucle, polyphonique), **One-Shot** (**strictement monophonique**), **Slicing**.

Classic : Start et Length **en pourcentage** de la région. **Snap** aux zero-crossings est « basé sur le **canal gauche** des samples stéréo — des glitches restent possibles en stéréo malgré Snap ». **Gain** est un étage distinct du Volume, qui est la sortie finale après le filtre.

**Avertissement** : des boucles de sustain assez courtes pour prendre un caractère glitché ou granulaire sont possibles, « mais peuvent provoquer une **charge CPU très élevée**, surtout avec Complex ou Complex Pro ».

Slicing : **maximum 64 tranches** par transitoires. Mode **Thru** : monophonique, mais déclencher une tranche **poursuit la lecture jusqu'à la fin de la région**. **Les tranches créées manuellement sont préservées quelle que soit la Sensitivity.**

LFO : **six formes**, **0,01 à 30 Hz** ou synchro. « Les LFO sont appliqués **individuellement à chaque voix**. » **Offset n'a aucun effet si Retrigger est désactivé.** **Key = 0 fait que tous les LFO des voix ont le même rate et ne diffèrent que par la phase.** Quatre destinations fixes : Volume, Pitch, Pan, Filter.

**Simpler réagit au pitch bend avec une sensibilité fixe de ±5 demi-tons**, non réglable, contrairement à Sampler.

**Crop et Reverse sont non destructifs**, ils travaillent sur une copie. **Le paramètre Fade n'est pas disponible quand le warp est activé.**

CPU : « les samples **stéréo** demandent **le double de traitement** des mono ».

## Sampler

**Waveshaper** avec quatre courbes — Soft, Hard, Sine, 4bit — et surtout un **bouton d'ordre de chaînage** : triangle vers le haut = **shaper puis filtre** ; vers le bas = **filtre puis shaper**.

**Oscillateur de modulation** : un par voix, **21 formes**, **FM ou AM**, avec sa propre enveloppe bouclable. « **Sa sortie n'est jamais entendue directement** ; ce que vous entendez, c'est son effet sur le multisample. »

**LFO 2 et 3** ont un mode stéréo : **Phase** (même vitesse, décalage du canal droit) ou **Spin** (« le canal droit peut tourner **jusqu'à 50 % plus vite** que le gauche »).

**Pitch Bend Range de 0 à 24 demi-tons**, réglable.

**Reverse est global, modulable, et ne génère pas de nouveau fichier.**

**MUET** : les **29 destinations** de l'enveloppe auxiliaire et des LFO 2 et 3 ne sont pas énumérées.

---

# 6. Où le manuel est muet

1. **Wavetable** : aucune liste de destinations (par conception), aucune liste de catégories de tables.
2. **Operator** : les 11 algorithmes ne sont décrits **par aucun texte**, seulement une image.
3. **Operator** : pas de distinction Glide/Portamento comme dans Simpler et Sampler.
4. **Drift** : aucune comparaison avec Analog ou Wavetable, aucune plage chiffrée pour le paramètre Drift.
5. **Meld** : les 18 effets de LFO 1 FX ne sont pas listés.
6. **Sampler** : les 29 destinations ne sont pas énumérées.
7. **Texture** : aucune plage ni unité pour Grain Size et Fluctuation.
