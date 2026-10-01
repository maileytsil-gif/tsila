# Modulation et effets comme outils de design — fiche de référence

Recherche web du 18 septembre 2026. `[D]` = documenté. `[I]` = interprétation. `[⚠]` = contradiction ou absence de source.

---

# A. MODULATION

## A1. LFO

### Plage et effets `[D]`

Gordon Reid, *Synth Secrets — Modulation* : le domaine du LFO va de **0,1 Hz à 20 Hz**, et produit trois résultats distincts selon la vitesse appliquée au filtre : **sweeps lents** en bas de la plage, **wah-wah** au milieu, **growl** en haut. Au-delà de ~20 Hz on quitte la modulation et on entre dans l'AM/FM audible : ce n'est plus du mouvement, c'est de la synthèse.

Nomenclature de base : **vibrato** = LFO → pitch ; **tremolo** = LFO → amplitude ; **filter sweep ou growl** = LFO → cutoff. Reid insiste aussi sur la **PWM**, qui « module l'amplitude des harmoniques individuelles à la source », d'où un épaississement de nature différente d'un chorus externe.

### Modes de déclenchement (Serum) `[D]`

Libellés Serum 2 (manuel p. 191) entre parenthèses les noms de Serum 1 :

- **FREE** (Off) : LFO libre, calé sur l'horloge du projet. Idéal pads, aucun rapport avec l'attaque.
- **RETRIG** (Trig) : redémarre la forme à chaque note.
- **ENVELOPE** (Env) : parcourt la forme **une seule fois** — le LFO devient une **enveloppe multi-segments dessinée à la main**.

Serum 2 ajoute **Chaos LFO** (attracteurs de Lorenz et Rössler, dérive non répétitive) et **Path** (tracé 2D avec sorties X et Y séparées, donc deux destinations animées par un seul geste). Les taux montent **jusqu'à 1 kHz**, ce qui permet de s'en servir comme source FM ou AM.

Le paramètre **Rise** donne une attaque au LFO ; en mode Env il agit comme un fondu d'entrée.

### Unipolaire contre bipolaire `[D]`

**C'est un réglage de la matrice, pas du LFO.** « Unipolar pushes one direction; bipolar swings both ways. »

`[I]` **Règle pratique** : bipolaire pour tout ce qui doit osciller **autour** d'un point de repos réglé à l'oreille (pitch, pan, position de wavetable, cutoff d'un pad). Unipolaire pour tout ce qui part d'une valeur posée et ne va que dans un sens (send de reverb, drive, ouverture d'un filtre en build).

**En bipolaire sur un cutoff, la moitié basse du cycle mange le corps du son à chaque tour** — sur une basse en deep house, c'est ce qui la fait disparaître un temps sur deux.

### Ableton Wavetable `[D]`

Loop modes **None / Trigger / Loop**, temps de fade-in, synchro tempo.

---

## A2. Enveloppes

### Le générateur n'est pas l'enveloppe `[D]`

Reid : l'enveloppe réelle d'un son est le produit de **plusieurs modificateurs agissant simultanément**. Il préfère le terme *transient generator* à *envelope generator*.

### Gate contre trigger `[D]`

Le **trigger** est une impulsion brève qui lance le contour. Le **gate** est maintenu tant que la touche est enfoncée, et c'est lui qui dit au synthé de rester en sustain.

Conséquence musicale documentée : l'ARP Odyssey retrigge à chaque note, d'où des passages rapides articulés et punchy ; le Minimoog, sans trigger, **fait perdre le pic initial aux notes qui se chevauchent**.

`[I]` Transposé à Live, c'est exactement le problème du legato involontaire dans un clip MIDI. **Deux notes qui se chevauchent d'un tick sur un pluck et l'attaque du second coup disparaît.** Vérifier les durées avant d'accuser le patch.

### Les neuf limites de l'ADSR `[D]`

Reid, *More About Envelopes* : la tension initiale doit être zéro · l'attaque est toujours positive · **le niveau maximal survient à la fin de l'attaque** · le decay est négatif · le sustain démarre au niveau de decay · le sustain est constant · le release part du sustain · le release est négatif · le release revient à zéro.

Affirmation clé : **« il existe de nombreux sons très courants que les synthétiseurs ne peuvent pas synthétiser »** avec quatre étages. Exemple donné : un cuivre réaliste (bruit d'attaque puis gonflement progressif) est impossible en ADSR, parce que le maximum n'est pas en fin d'attaque.

Solutions historiques recensées : Korg MS-20 (DAR et ADSHR avec Hold), Yamaha GX1 (niveau initial + palier d'attaque sur l'enveloppe de filtre), Roland Alpha Juno (5 étages, trois niveaux programmables). En modulaire, on additionne plusieurs EG dans un mixeur de CV.

`[I]` D'où l'intérêt réel du **mode Env du LFO de Serum** : c'est la parade moderne à cette limite.

### ⚠ Courbes exponentielles contre linéaires

**Aucune source de référence traitant le sujet frontalement n'a été trouvée.** Ce qui est documenté côté outils : Serum expose une zone **`Curve`** dans l'onglet MATRIX qui redéfinit la réponse de chaque enveloppe ou LFO.

`[I]` Un decay linéaire sur un pluck sonne électronique et long ; un decay exponentiel (chute rapide puis traîne) correspond à ce que fait une corde et lit mieux dans un mix dense. Sur un filtre en revanche, une attaque linéaire rend le sweep plus lisible parce que la perception du cutoff est logarithmique. **La linéarité perçue se règle à l'oreille, pas au calcul.**

### Enveloppes synchronisées au tempo `[D]`

Serum 2 synchronise attack, decay, sustain et release au BPM. Donner à Env 2 un decay d'**une noire** plutôt qu'une valeur en millisecondes fait que « le filter pluck reste dans la poche que le projet tourne à 124 ou 174 BPM ».

### Enveloppes de hauteur `[D]`

Routage documenté dans Wavetable : Envelope 3 → Pitch, montant subtil et très court, « transforme une basse en kick ».

---

## A3. Matrice de modulation

### Structure d'une ligne (Serum 2) `[D]`

Source · destination · **bipolaire/unipolaire** · **curve** (remodèle l'intensité de la réponse) · **aux source** (met à l'échelle la modulation par la vélocité ou un autre paramètre).

L'**AUX SOURCE** permet de combiner deux sources : même direction, seconde source inversée, ou bypass.

### Sources MIDI dans Wavetable `[D]`

En plus des 3 enveloppes et 2 LFO : **Velocity, Note pitch, Pitch Bend, Aftertouch, Modwheel**. Astuce documentée : si une destination n'apparaît pas dans la matrice, **cliquer le paramètre sur l'écran principal le fait apparaître**.

`[I]` En deep et minimal house, **la vélocité comme aux source sur le cutoff est le moyen le plus rentable de rendre un stab vivant sans toucher à l'arrangement** : le clip garde ses notes, la variation vient de la couche MIDI.

### Les dix routages documentés `[D]`

| # | Source | Destination | Effet |
|---|---|---|---|
| 1 | Env (Amp) | Amplitude | plucks courts ou pads longs |
| 2 | Env 2 | Cutoff | ouverture progressive du timbre |
| 3 | Env 3 | Pitch | montée courte, basse → kick |
| 4 | LFO sinus | Pitch (~5 %) | vibrato délicat sur pad |
| 5 | LFO 2 | Filter Frequency | **mouvement sur un son statique** |
| 6 | LFO carré | Amplitude | trance gate |
| 7 | LFO Random | Cutoff + Q élevé | sample & hold, sci-fi rétro |
| 8 | LFO sync tempo | Wavetable Position | scan de la table |
| 9 | LFO triangle | FM Amount | transformation radicale du timbre |
| 10 | **LFO 1** | **LFO 2 Rate** | **modulation de la modulation** |

Source : https://www.attackmagazine.com/technique/tutorials/10-common-modulation-routings-using-abletons-wavetable/

---

## A4. Macros

### Documenté

Serum 2 : **huit macros** (MACRO 1–8, manuel p. 206 ; Serum 1 en avait quatre), chacune agrégeant plusieurs destinations **à des profondeurs différentes**.

Critère de choix des paramètres : privilégier ce qui donne **la plus grande amplitude sonore**. Le dry/wet d'une reverb s'entend beaucoup plus qu'un traitement d'entrée ; la fréquence de coupure d'un passe-bas est décrite comme « une machine à morpher le son ».

Côté Live, les **Macro Variations** (Live 11+) mémorisent des états complets de macros : la macro devient un **sélecteur de versions**, pas seulement un potard continu.

### Concevoir une macro qui reste musicale sur toute sa course `[I]`

Quatre règles tirées de la pratique, pas d'un document.

1. **Une seule intention par macro**, verbalisable en trois mots (« plus sale », « plus loin », « plus ouvert »). Si on ne peut pas la nommer, c'est un fourre-tout.
2. **Compenser l'énergie, toujours.** Cutoff qui monte doit s'accompagner d'un gain ou d'un drive qui baisse, sinon la macro est aussi un fader de volume déguisé et on casse son mix en bougeant son timbre.
3. **Plages asymétriques et décalées.** Étaler les assignations sur des portions différentes de la course (drive de 0 à 40 %, send de 30 à 100 %) évite le « tout arrive en même temps » qui rend la fin de course inutilisable.
4. **Tester les trois points 0, 50 et 100 % en contexte**, sur la section la plus dense. Une macro dont seuls les 20 derniers pour cent sont exploitables n'est pas une macro, c'est un interrupteur.

---

## A5. Le mouvement

### Ce qui est documenté

La vitesse détermine la nature perçue : 0,1–20 Hz donne sweep lent, wah-wah, growl. Le routage n°5 énonce la fonction : LFO → filtre pour « ajouter du mouvement à des sons statiques ».

Littérature scientifique : le spectre de modulation d'amplitude se manipule par le taux et la profondeur ; les différences de modulation produisent les percepts « lisse » ou « rugueux » ; des modulations rapides ajoutées à la musique produisent une **activité accrue des réseaux attentionnels** (fMRI) et un couplage stimulus-cerveau plus fort (EEG). https://www.nature.com/articles/s42003-024-07026-3

La **fatigue auditive** au sens des ingénieurs est un phénomène consécutif à une exposition prolongée : les oreilles cessent de saisir les changements de dynamique.

### Hiérarchie des vitesses `[I]` — avis, la littérature ne le dit pas ainsi

Ce qui fatigue n'est pas le mouvement, c'est **le mouvement périodique et parfaitement prévisible dans la bande 2–6 kHz**, là où l'oreille est la plus sensible.

| Échelle | Ce qu'on module | Effet |
|---|---|---|
| **Très lent, 16–64 mesures** | position de wavetable, largeur stéréo, tonalité globale | ne s'entend pas, se remarque quand on coupe |
| **Lent, 2–8 mesures** | cutoff, send de reverb, drive | fait respirer une boucle sans que rien ne se passe |
| **Rythmique, 1/4 à 1/16** | amplitude, pan, filtre à Q élevé | efficace, à réserver à un ou deux éléments |
| **Rapide, > 8 Hz** | — | ce n'est plus du mouvement, c'est du timbre |

**Règle de sécurité : un seul paramètre dominant en mouvement par élément, et jamais deux éléments animés à la même vitesse dans la même bande de fréquences.** C'est là que naît la sensation de brouillard mouvant.

---

# B. LES EFFETS COMME OUTILS DE DESIGN

## B1. Distorsion et saturation

### Harmoniques paires contre impaires `[D]`

Les harmoniques **paires** (2e, 4e, 6e) sonnent chaudes, musicales, consonantes — associées aux lampes. Les **impaires** (3e, 5e, 7e) sonnent plus dures, agressives — associées aux transistors et au hard clipping.

**Lampe** : un étage single-ended a une **courbe de transfert asymétrique** qui privilégie les paires ; les circuits à lampes saturent très progressivement, donc se comportent aussi comme un compresseur doux.

**Bande** : les particules d'oxyde de fer s'alignent sur le champ magnétique ; au-delà d'un certain niveau toutes sont alignées et la bande ne peut plus encaisser. Produit des paires **et** des impaires, mais principalement des paires, d'où la chaleur.

**Transistor** : quand trop de courant traverse le circuit et fait chuter la tension, la saturation génère **plus d'impaires que de paires**, et un écrêtage plus dur.

### Wavefolding `[D]`

Au lieu d'écrêter, le wavefolder **replie** la portion qui dépasse le seuil, en miroir. Le hard clipping produit beaucoup d'harmoniques aiguës, le soft clipping moins d'harmoniques d'ordre élevé mais de l'intermodulation ; le wavefolding, lui, « produit des spectres complexes à partir de formes simples ». Une sinusoïde passée dans un wavefolder ressort avec des harmoniques très inhabituelles.

On peut régler **plusieurs replis**, ce qui rend le son de plus en plus brillant et bruité. **Il fonctionne mieux sur des formes simples** (sinus, triangle). Avertissement documenté : **le wavefolding crée de l'aliasing**, audible comme des fréquences dissonantes, surtout avec beaucoup de folds dans les octaves aiguës.

### FabFilter Saturn 2 `[D]`

Multibande jusqu'à **6 bandes**, **28 styles de distorsion**. Ajouts de la v2 : 4 styles Amplifier, 3 styles Transformer, styles Foldback et Breakdown, et des versions **subtiles de Tube, Tape et Saturation** destinées au mastering. Par bande : type, drive, feedback, dynamics, tone, level, mix. Sources de modulation : XLFO, Envelope Generator, **Envelope Follower**, MIDI, XY controller. Option **phase linéaire**, suréchantillonnage Good / Superb.

`[I]` C'est le multibande **avec modulation par bande** qui en fait un outil de design et non un correctif : saturer uniquement la bande 800 Hz – 3 kHz d'un growl, avec un envelope follower sur le drive, donne une agressivité qui ne bouge que quand la note attaque. Impossible en large bande.

**Précaution non négociable : le drive change le niveau, donc toute comparaison se fait à niveau égalisé**, sinon on entend « mieux » ce qui est simplement « plus fort ».

---

## B2. Filtrage créatif, formants, vocoder

### Résonance `[D]`

La résonance crée un pic autour de la coupure, rendant ces harmoniques **plus fortes que dans le signal d'entrée**. Q faible = pic large, Q élevé = pic de plus en plus prononcé. À Q maximal, **le filtre s'auto-oscille** : « il devient un générateur de sinusoïde à part entière », donc une source sonore.

Reid conclut que **le choix du filtre définit à lui seul le caractère d'un instrument** : le même oscillateur sonne complètement différemment selon le filtre traversé.

### Formants `[D]`

Un formant est une **résonance du conduit vocal**, donc un pic spectral ; le mot vient du latin *formare*, façonner. Point clé : **trois formants suffisent** à distinguer une voyelle. Exemple pour « ee » chez un homme adulte : **270 Hz, 2300 Hz, 3000 Hz**.

Deux architectures : **en série**, plusieurs passe-bande resserrent la réponse globale ; **en parallèle** (plus utile), des fréquences centrales distinctes créent des bosses séparées.

**Ce qui les distingue d'un filtre de synthé : ils ne suivent pas la hauteur.** « La nature exacte des formants statiques rend le timbre d'une famille d'instruments acoustiques cohérent et reconnaissable d'un instrument à l'autre. »

Technique documentée : on peut **simuler un filtre balayable** en déplaçant la fréquence centrale du formant supérieur tout en resserrant le Q du formant inférieur, et **simuler une résonance variable** en jouant uniquement sur l'amplitude du formant supérieur.

`[⚠]` Note de cohérence : l'index de série SOS numérote cet article « Part 25 », le miroir GitHub le numérote « Part 23 ». Contenu identique.

### Vocoder `[D]`

Deux entrées : **carrier** (le son qu'on égalise, typiquement un synthé) et **modulator** (le son dont le spectre pilote les niveaux de bandes, typiquement une voix). Un banc de filtres analyse le modulateur, le découpe en bandes, et le vocodeur monte ou baisse chaque bande du carrier selon les harmoniques du modulateur. Le paramètre **formant / shift** décale les fréquences des filtres. **8 à 12 bandes pour un son vintage**, plus de bandes = plus réaliste.

Len Sasso résume le vocodeur comme **« un processeur d'EQ à deux entrées audio »**, et documente les usages non vocaux dans Live : **self-vocoding** (choisir « Modulator » comme carrier) pour du formant shift et du gating sur des pads ; traiter modulateur et carrier avec des effets **différents** ; router via des pistes de retour.

**Contrainte technique explicite : modulateur et carrier doivent partager des fréquences** pour produire quoi que ce soit.

`[I]` Pour de la minimal house, le vocodeur est plus intéressant en **carrier bruit blanc et modulateur boucle de batterie** qu'en usage vocal : on obtient une couche de hats « parlante » qui suit exactement le groove existant, sans ajouter de transitoire. Et le self-vocoding est le moyen le plus rapide de donner une identité à un pad générique.

---

## B3. Chorus, flanger, phaser — la différence est un mécanisme, pas un réglage

### Flanger `[D]`

Délai court appliqué **uniformément à tout le signal** (~10 ms, les plus musicaux « sous 15 ms »), modulé par un LFO, remélangé au sec. Résultat : un **filtre en peigne à dents nombreuses et régulièrement espacées**, formant une série harmonique linéaire.

### Phaser `[D]`

**Aucun délai.** Le signal passe dans des **filtres all-pass** à réponse de phase non linéaire : toutes les fréquences passent sans changement d'amplitude, mais avec un déphasage qui varie continûment de 0 à 180°. Deux étages chaînés donnent 180° à une fréquence précise, donc **une encoche**.

D'où la règle documentée : **4 étages produisent 2 encoches, 10 étages en produisent 5**. Les encoches sont **peu nombreuses et inégalement espacées, donc non harmoniques**, ce qui explique le caractère creux différent du flanger.

### Feedback `[D]`

Pour les deux : « renforce ou accentue l'effet ». Sur un phaser, il « change la forme des filtres d'encoche », rendant les pics plus aigus et les encoches plus étroites.

### Chorus `[D]`

Délai **plus long** (typiquement ≥ 20 ms), avec variation de temps et de hauteur : plusieurs copies légèrement désynchronisées et désaccordées, imitant plusieurs instrumentistes.

Résumé documenté : « le chorus sonne comme plusieurs instruments, le phaser crée des sweeps lisses, le flanger donne un effet whoosh intense avec une qualité creuse distinctive ».

### Ordre d'utilité en deep house `[I]`

**Phaser** sur un pad ou un rhodes : mouvement non harmonique, ne trahit pas la source, ne détruit pas la mono. **Chorus** sur des nappes et des stabs, avec la réserve que c'est **l'effet le plus destructeur pour la compatibilité mono**. **Flanger** comme événement d'arrangement, une transition ou un fill, rarement comme couleur permanente : ses dents harmoniques régulières deviennent vite une signature envahissante.

Rappel : pour épaissir **sans** casser la mono, moduler la largeur d'impulsion à la source bat le chorus.

---

## B4. Delay et reverb comme matière

### Reverb infinie `[D]`

Documentation Valhalla, la plus précise trouvée : le **Feedback** contrôle la quantité de sortie réinjectée en entrée ; vu comme une ligne à retard, il fixe le nombre de répétitions avant l'inaudible. Avec une **Diffusion de 0,8 à 0,91**, on obtient déjà des décroissances très longues à feedback nul ; en montant le feedback, « le temps de décroissance se rapproche de plus en plus de l'infini ».

### Shimmer `[D]`

Origine : l'effet Eno et Lanois reposait sur un **Lexicon 224 + un pitch shifter AMS**. Recette documentée : **Shift à +12 demi-tons, Feedback ≥ 0,5**. Les algorithmes de ValhallaShimmer ont été conçus **spécifiquement pour bien se comporter avec un feedback pitché**, afin d'autoriser un feedback plus élevé. Modes **Single** (décale la boucle vers le haut ou le bas) et **Dual** (les deux simultanément).

Dans Live, l'équivalent natif est le mode **Shimmer** de la section Algorithm d'**Hybrid Reverb**.

### Gated reverb `[D]`

Signature des années 80. Recette dans Live : piste de retour, **Reverb en preset Long Tail**, puis **Gate** derrière, dont le threshold règle l'effet.

### Reverse reverb `[D]`

Sert à construire une montée **avant** l'arrivée du son, typiquement en pré-drop. Réglage documenté : **56 % de convolution reverse, predelay d'1/16**, envoyé dans un algorithme Prism à 44 %.

### La distinction utile `[I]`

**Reverb espace** = insert court, wet faible, dans le champ. **Reverb matière** = retour dédié, decay très long, filtrée sévèrement en haut et en bas, puis **resamplée** pour devenir une nappe qu'on arrange comme une piste.

Le second usage n'a plus rien à voir avec le mix : c'est de la **synthèse par accumulation**, et c'est là que le feedback proche de 1 devient un instrument plutôt qu'un défaut.

---

## B5. Ordre des effets

### Chaîne de référence `[D]`

source → compression → **overdrive/distorsion** → **modulation** → **delay** → **reverb**.

Raisons documentées :
- **Distorsion tôt**, puis filtres, puis modulation, puis delays.
- **Effets temporels en fin de chaîne** : placer reverb ou delay **avant** une distorsion fait bondir le niveau de l'ambiance dès qu'on ajoute du gain.
- **Delay avant reverb** : chaque répétition porte alors sa propre queue de reverb, ce qui correspond au comportement d'un espace réel.
- **L'inverse est un choix, pas une erreur** : reverb avant saturation donne le lavis shoegaze où les queues sont écrasées par la distorsion. Les sources le disent explicitement : **l'ordre standard est un point de départ, pas une loi.**

### Trois inversions qui paient en électronique `[I]`

**Saturation après filtre** : les harmoniques générées ne sont plus filtrées, le son reste brillant même cutoff baissé. **Saturation avant filtre** : le filtre nettoie la distorsion, résultat plus rond. **Même réglage de drive, deux sons différents.** C'est le levier le plus sous-estimé.

**Reverb → distorsion**, l'inverse du standard : la queue devient un bruit dense et stable, excellent comme couche de fond.

**Delay → filtre à Q élevé dans le feedback** : chaque répétition se colore un peu plus, la ligne se transforme au lieu de s'éteindre.

Corollaire : **l'ordre ne se juge qu'à niveau égalisé**, sinon on choisit toujours la version la plus forte.

---

## B6. Resampling

### Définition `[D]`

Tout traitement destructif d'un son échantillonné — downsampling, bitcrushing, reverse, timestretching, pitchshifting, application de plug-ins — en vue de le redéployer.

### Mise en œuvre dans Live `[D]`

- Nouvelle piste audio, entrée **« Resampling »** : capture tout ce qui passe par le master.
- **Freeze** rend un bounce **pré-fader** de la sortie de la piste, devices et automation compris. **Freeze + Flatten** remplace clips et devices par un fichier audio.
- **Distinction importante : une piste gelée ne peut pas être automatisée, une piste resamplée si.**
- Pour exclure reverb et delay d'une capture, **désactiver ces devices manuellement** avant d'enregistrer.

### Effet d'accumulation `[D]`

Décrit comme l'une des techniques les plus sous-utilisées : chaque étape ajoute un caractère qui s'accumule, et la sortie finale ne ressemble plus du tout à l'original.

`[I]` **Le vrai intérêt du resampling n'est pas le CPU, c'est de fermer une décision.** Tant que la chaîne est vivante, on continue de la régler. Une fois l'audio figé, on traite un objet, ce qui ouvre des gestes impossibles en amont : reverse, warp extrême, découpage au transitoire, réinjection dans Simpler avec une nouvelle enveloppe.

**Discipline : garder l'original désactivé plutôt que supprimé, et nommer le bounce avec l'étape** (`pad_v2_reverb+bitcrush`), sinon la chaîne n'est plus reconstituable.
