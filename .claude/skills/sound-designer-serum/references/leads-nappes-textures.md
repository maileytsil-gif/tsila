# Leads, plucks, nappes et textures — fiche de référence

Recherche web du 18 septembre 2026. `[D]` = documenté. `[CALC]` = calcul fait à partir des chiffres de la source. `[I]` = interprétation.

**La meilleure source de tout le dossier** : la thèse d'Adam Szabo (KTH, Stockholm, 2010), qui a échantillonné un JP-8000 et un JP-8080 en 44,1 kHz / 32 bits et analysé en FFT 131 072 points. https://www.adamszabo.com/internet/adam_szabo_how_to_emulate_the_super_saw.pdf

---

## 1. Plucks

### Ce qui fait qu'un pluck sonne

`[D]` SOS *Synthesizing Plucked Strings* explique la physique : **la position de pincement détermine les harmoniques manquantes**. Pincer au centre supprime une harmonique sur deux (il ne peut pas y avoir de nœud au point de pincement) ; au 1/3, toutes les multiples de 3 ; au 1/4, toutes les multiples de 4. Déplacer la position produit « le son de flanging caractéristique dû au déplacement des trous dans le spectre harmonique ».

`[D]` Dureté du médiator : un objet mou (le pouce) déforme la corde en profil arrondi et « agit comme un passe-bas, supprimant les harmoniques hautes » ; un objet dur conserve le haut du spectre. C'est exactement ce que fait un filtre piloté par enveloppe.

`[D]` Enveloppe : pincer parallèlement à la table décroît lentement, perpendiculairement donne un niveau initial plus élevé mais une décroissance plus rapide. Le pluck réel mélange les deux.

`[I]` **Traduit en réglage : le rapport attaque/decay n'est pas ce qui fait le pluck.** C'est le **différentiel entre l'enveloppe de filtre et l'enveloppe d'amplitude** : l'harmonicité doit chuter plus vite que l'amplitude. Un decay d'ampli court avec un filtre statique donne un son coupé, pas un pluck.

### Patch réel chiffré `[D]`

Attack Magazine, *Pluck Organ with UVI Falcon* : Decay 3,36 s sur le moteur Pluck, Harmonic Ratio 1,96, Harmonic Damp 39,73 %, 2 cordes, Brightness 70 %. **Couche 2 (« synth tom ») : attaque minimum, decay 26,9 ms, sustain 0, gain −5,90 dB.** Au niveau programme : Diode Clipper drive 12 dB + **passe-haut 139 Hz**, réverb en aux à −11,37 dB, Size 50 %.

`[I]` Le point remarquable : la couche transitoire est un **son séparé**. C'est la méthode la plus fiable pour un pluck qui traverse un mix house.

### FM contre soustractif `[I]`

En **soustractif**, la brillance initiale vient du filtre, donc elle est corrélée au niveau et se perd quand on baisse la piste. En **FM**, elle vient de l'indice de modulation, donc elle reste indépendante du volume — d'où des plucks qui restent lisibles à −20 dB dans un mix minimal.

Pour du deep house, la FM à ratio entier (2:1, 3:1) donne un pluck bois ou marimba ; le ratio non entier donne un pluck verre ou cloche.

### Points de départ

| | Réglage |
|---|---|
| **Pluck deep house soustractif** | Amp A 0 ms, D 180–250 ms, S 0. LP 24 dB, cutoff repos 600–800 Hz. ENV 2 (A 0, D 120–160 ms, S 0) → cutoff, pic vers 3–4 kHz. **Decay de filtre plus court que celui de l'ampli, environ 60–70 %.** |
| **Pluck FM (Operator)** | Algo A←B. B ratio 2 (bois) ou 3,51 (verre). Env B : A 0, D 80–150 ms, S 0. Env A : A 0, D 300–500 ms, S 0. Indice ~1 doux, ~10 inharmonique agressif. |
| **Couche transitoire séparée** | Second oscillateur ou sample, decay ≈ 25–30 ms, gain ≈ −6 dB, passe-haut ≈ 140 Hz pour ne pas manger le kick. |

---

## 2. Leads et supersaw

### Origine `[D]`

Sept oscillateurs sawtooth superposés, réalisés pour la première fois par le **Roland JP-8000 en 1997** selon Szabo (MusicRadar dit 1996 ; divergence de date, la thèse est plus précise sur le reste). Modèles Roland qui l'embarquent : JP-8000, JP-8080, V-Synth, SH-201, Gaia SH-01.

### Structure mesurée — les chiffres qui comptent `[D]`

Sept saws. Un **oscillateur central non affecté par le détune**. Trois au-dessus, trois en dessous.

Note C5 = 523,3572 Hz, détune au maximum :

| Osc | Fréquence | `[CALC]` cents |
|---|---|---|
| 1 | 465,7758 | **−202** |
| 2 | 490,4462 | −112 |
| 3 | 513,1394 | −34 |
| 4 (centre) | 523,3572 | 0 |
| 5 | 533,7784 | +34 |
| 6 | 555,8919 | +104 |
| 7 | 579,5932 | **+177** |

`[CALC]` L'écart maximal atteint donc environ **±2 demi-tons, pas quelques cents**. Et comme les offsets sont symétriques en *rapport de fréquence*, ils sont **asymétriques en cents** : le bas s'écarte plus que le haut.

### La courbe de détune n'est pas linéaire `[D]`

Szabo l'a échantillonnée tous les 8 pas MIDI et approchée par un polynôme d'ordre 11. **À mi-course du bouton, le multiplicateur réel est 0,0967, soit moins de 10 % de l'écart maximum.** La courbe ne monte franchement qu'après 0,5 et explose après 0,9.

`[CALC]` À mi-course, l'oscillateur le plus haut est donc à **≈ +18 cents**. C'est exactement la plage nappe et cordes douce. Szabo : cette courbe « a rendu possible des pads très lisses ».

### Le contrôle Mix `[D]`

**Le manuel Roland est faux.** Mesuré, l'oscillateur central **baisse** linéairement (y = −0,55366·x + 0,99785) et les six latéraux montent en parabole. Les amplitudes s'égalisent à **x = 0,75**, pas au maximum.

`[CALC]` À mix maximum : centre 0,444, latéraux 0,591, donc **le centre est environ 2,5 dB sous chaque latéral**.

### Shape et phase `[D]`

Ce sont de vrais saws **non band-limités**, donc avec aliasing, suivis d'un **passe-haut asservi à la fondamentale**. Szabo : l'aliasing « ajoute une couche de profondeur, rendant le son plus plein et plus aéré » — **le bruit n'est pas un défaut, il fait partie du timbre** — mais doit être coupé sous la fondamentale, sinon il sonne « non naturel et dérangeant ».

Les sept oscillateurs sont **libres, avec une phase aléatoire à chaque déclenchement de note**. Chaque note a donc une forme d'onde différente.

`[I]` **Conséquence directe : un supersaw en phase fixe ne sonnera jamais comme un JP-8000**, parce que le transitoire d'attaque sera identique à chaque note. Mettre `Rand` sur la phase d'oscillateur. Dans Ableton Wavetable, utiliser le mode **Classic** ou **Randomize**, surtout pas **Phase Sync**, qui fige justement la phase.

### Correspondances Serum `[D]`

Unison jusqu'à 16 voix. **Blend** = décalage de niveau des voix par rapport aux voix centrales, défaut 75 %. **Width** = étalement stéréo. **Range** = nombre de demi-tons couverts par Detune. **Warp** avec unison décale le warp entre voix.

`[I]` Blend est l'équivalent conceptuel du Mix du JP-8000 ; la donnée de Szabo suggère qu'un Blend laissant le centre ~2,5 dB sous les latérales reproduit le comportement Roland au maximum.

`[D]` CFA-Sound : régler **Range à 5–7 demi-tons** pour générer un accord directement dans l'oscillateur ; **réduire Width** pour garder le focus stéréo. Le filtre **French lowpass** est recommandé pour plucks et pads.

### Masquage `[D]`

Splice : rétrécir la largeur d'impulsion (PWM) donne un caractère « fin et nasal » qui évite de masquer les fréquences similaires de la voix. Compression finale ratio 3–4, attaque et release courts. Patch en **mono** pour pouvoir utiliser le Glide.

La zone de conflit voix/synthés est **1–4 kHz**. Remède documenté : EQ dynamique déclenchée par la voix en sidechain, plutôt qu'un creux statique qui reste quand la voix est absente. La solution la plus élégante reste l'arrangement : ne pas faire jouer le lead pendant les phrases vocales.

`[I]` Sans voix, le conflit se déplace : le lead se bat avec les pads dans 300 Hz–1 kHz. **Règle : un seul élément large à la fois.** Si le pad est en unison 8 voix width 100 %, le lead doit être étroit, ou l'inverse.

### Vibrato `[D]`

LFO à **~7 Hz** sur le fine tune, avec **200 ms de delay** avant déclenchement.

`[I]` Le delay est le point clé : un vibrato présent dès l'attaque sonne synthétique. Sur des noires à 126 BPM (476 ms), 200 ms de delay font que le vibrato n'apparaît que sur les notes tenues — exactement le comportement d'un chanteur.

### Points de départ

| | Réglage |
|---|---|
| **Supersaw nappe** | 7 voix, écart total ≈ ±18 cents (mi-course du bouton JP-8000). Phase aléatoire par note. Passe-haut suiveur de pitch à la fondamentale. |
| **Supersaw plein** | Écart total ≈ ±2 demi-tons. Voix centrale ~2,5 dB sous les latérales. Width réduite si un pad large joue en même temps. |
| **Lead mono expressif** | Mono + Glide, LFO 7 Hz sur le fine tune avec 200 ms de delay, PWM étroit pour dégager 1–4 kHz, compresseur ratio 3–4 en fin de chaîne. |

---

## 3. Nappes

### Trois patchs réels, chiffres complets `[D]`

**A. Ambient techno (FabFilter Twin 3 + Pro-R 2)** — https://www.attackmagazine.com/technique/synth-secrets/crafting-ambient-techno-pads/

- Osc 1 sinus +2 oct −12 dB · Osc 2 0 oct −11 dB · Osc 3 +1 oct −8 dB · **Osc 4 −1 oct à −∞ dB (silencieux au départ)**
- Enveloppe principale : **A 5 s, D 1,5 s, S −3 dB, R 1 s**
- LP 720 Hz 24 dB · HP 280 Hz 24 dB · low shelf 280 Hz large
- **XLFO 1 : 13 Hz** → Sync Osc 2 et 3, pan filtre 2
- **XLFO 2 : 0,5 Hz** → Sync Osc 1, Filter Frequency Offset
- **EG2 : attaque 12 s** → module la fréquence de XLFO 1
- **EG3 : attaque 15 s** → niveau d'Osc 4
- Delay 50 % mix, 70 % feedback, ping-pong · Pro-R 2 mode Vintage, **mix 100 %**

`[I]` Le patch le plus instructif des trois. Trois échelles de temps coexistent. **L'oscillateur 4 n'apparaît qu'après 15 secondes : c'est de l'arrangement écrit dans le patch.** À 120–126 BPM, 15 s ≈ 7–8 mesures, donc le pad change de timbre pile à la mesure 8.

**B. Ambient pad (u-he Hive 2)** — https://www.attackmagazine.com/technique/synth-secrets/the-ambient-pad-that-holds-it-all-together/

Osc 1 unison 8 voix, detune 20, octave −2, sub +7 demi-tons. Osc 2 unison 8, detune 10, octave −1, +4 demi-tons. Transpose global −16, mode Legato. **AMP 1 : A 1, D 80, S 25, R 50. AMP 2 : A 90, D 50, S 100, R 75.** Matrice : Vélocité → cutoff filtre 1 (35) ; Shape Sequencer 6 pas → position wavetable Osc 2 (25) ; **LFO1 + LFO2 → pan Osc 2 (75)**.

`[I]` Deux enveloppes d'ampli de formes **opposées** (A 1 contre A 90) : le son change de composition spectrale pendant l'attaque sans qu'aucun filtre ne bouge. Et le pan modulé par **deux LFO sommés** évite le mouvement stéréo périodique reconnaissable.

**C. Detuned pad (Sylenth1)** — https://www.attackmagazine.com/technique/synth-secrets/detuned-pad/

Osc A1 5 voix −1 oct **detune 4,05 cents** phase 300°. Osc A2 7 voix saw **detune 3 cents** phase 100°, Inv activé. Amp A 3, R 7, polyphonie 10. LFO 1 → Phase A (mouvement errant). LFO 2 → Volume A, rate 1/4 sync (sidechain intégré au synthé). Filtre LP ≈ 800 Hz, résonance 3, drive 7, passe-haut de contrôle 60 Hz. **Chorus : delay 16 ms, rate 0,22 Hz, depth 50 %, mix 60 %.** Réverb mix 30 %.

`[I]` Detune de 3–4 cents seulement, mais sur 12 voix. Cohérent avec Szabo : **la largeur ne vient pas d'un gros désaccord, elle vient du nombre de voix et de leur phase.** Le chorus à 0,22 Hz (un cycle toutes les 4,5 s) fait plus pour la largeur que le detune.

### La réverb comme partie du son

`[D]` Dans le patch A, Pro-R 2 est à **mix 100 %** : il n'y a plus de signal sec. C'est la définition d'une réverb qui **est** le son.

`[D]` Attack Magazine : privilégier les **départs** pour pouvoir doser ; filtrer le bas sur le départ « pour éviter que les basses fréquences encombrent le bas du mix » ; et pour l'électronique, « le réalisme au diable ».

`[I]` **Distinction opérationnelle** : réverb en **insert à mix élevé (60–100 %)** = elle appartient au patch, elle sera resamplée et automatisée avec. Réverb en **départ à mix faible (10–30 %)** = elle appartient au mix, elle est partagée. Un pad de melodic techno a normalement les deux.

### Points de départ

| | Réglage |
|---|---|
| **Enveloppe** | A 2–5 s, D 1,5 s, S légèrement sous le pic (−3 dB), R 1–2 s. Deux couches avec attaques **opposées** (50 ms et 3 s). |
| **Mouvement à trois vitesses** | LFO rapide ~13 Hz (grain), LFO lent 0,5 Hz (respiration, cycle 2 s), enveloppe 12–15 s (arrivée d'une couche) ≈ 7–8 mesures. |
| **Filtrage et espace** | LP 24 dB vers 700–800 Hz + HP 250–300 Hz pour vider la zone du kick et des voix. Chorus delay 16 ms / rate 0,22 Hz / mix 60 %. |

---

## 4. Keys

### Piano électrique `[D]`

SOS *Synthesizing Pianos* : le DX7 s'est révélé « capable d'imitations remarquables de pianos électriques comme le Fender Rhodes, les Wurlitzer et les Hohner », alors qu'il échouait sur le piano acoustique.

Sur le piano **acoustique** : « il n'y a jamais eu de piano acoustique convaincant produit par synthèse soustractive, additive ou FM. Seuls les échantillons semblent y parvenir. » Raisons : trois cordes par note vibrant hors phase, point de frappe variable du 1/7 au 1/15 de la corde, registres construits différemment.

Comportement documenté : « les notes de piano sont plus brillantes quand on frappe plus fort », et **les notes graves décroissent plus lentement que les aiguës**.

Recette Serum documentée : Osc A sinus, **unison 3 voix, detune quasi nul, Blend ~11 h**, Env 1 → position de wavetable (85–90), **Env 1 decay 1,8–2 s, release 290–300 ms**, **LFO sinus ~1 Hz → fine tune en très petite quantité**, oscillateur de bruit en one-shot pour l'attaque, LP 24 dB, puis compresseur → chorus → EQ.

`[I]` **Les trois briques d'un Rhodes crédible** : une sinus quasi pure pour le corps, une couche de bruit ou cloche très courte pour le marteau sur la tine, et **un léger battement de pitch (LFO ~1 Hz sur le fine tune)** qui simule la tine et la barre tonale jamais parfaitement accordées. Le troisième point est ce que les gens oublient, et c'est ce qui fait la différence entre « sinus avec chorus » et « Rhodes ».

### Orgue `[D]`

SOS *Synthesizing Tonewheel Organs* — les 9 tirettes du B3 :

| Pied | 16′ | 5⅓′ | 8′ | 4′ | 2⅔′ | 2′ | 1⅗′ | 1⅓′ | 1′ |
|---|---|---|---|---|---|---|---|---|---|
| Harmonique | 1 | 3 | 2 | 4 | 6 | 8 | 10 | 12 | 16 |

Chaque roue phonique génère un son « aussi proche que possible d'une sinusoïde ». Le **key-click** est un « spit » percussif au transitoire dû aux défauts des contacts ; il s'aggrave avec l'âge et il est aujourd'hui considéré comme essentiel à l'authenticité. Le générateur présente aussi une **leakage**, mélange de hauteurs et de bruit qui donne le côté guttural.

Réalisation démontrée sur Juno 6 pour la registration **88 8000 000** : pulse 33 % + sub une octave en dessous + filtre en auto-oscillation accordé **19 demi-tons au-dessus** de la fondamentale (donc la 3e harmonique), l'ADSR modulant le cutoff pour créer le key-click.

`[I]` Transposable à Operator : quatre sinus aux ratios 1, 2, 3, 4 avec niveaux indépendants = tirettes. **Le key-click se fait avec une enveloppe de filtre de 5–15 ms, pas avec un sample.**

---

## 5. Textures

### Bruit `[D]`

MusicRadar : blanc = plat sur tout le spectre, sans hauteur définissable ; rose = décroît vers l'aigu. Le bruit est « une matière première très utile qu'on peut tailler avec des filtres et de la modulation d'amplitude ». Le traitement multibande permet un grondement grave et un souffle aigu simultanés. Les enregistrements d'ambiance sont « une source fantastique de texture ». Un bruit à bas niveau « comble les trous autour des autres éléments et contribue à épaissir un mix ».

**Et le bruit blanc filtré peut servir de source de modulation** (pitch ou cutoff) pour un « vibrato errant inhabituel », différent à chaque occurrence.

`[I]` Règle transposable, dérivée de Szabo : **tout bruit de texture superposé à un son tonal doit être filtré au-dessus de la fondamentale de ce son.**

### Bruit de fond comme colle `[D]`

Liveschool (centre de formation certifié Ableton) : **Vinyl Distortion** et son générateur Crackle ; enregistrer des room tones au téléphone (les micros de basse qualité ont une qualité bruitée utile) ; **Erosion** en modes Noise ou Wide Noise ; **Vocoder avec du bruit en source**. Méthode : caler l'enveloppe du sample textural pour qu'il traîne avec le son principal, puis léger EQ pour la cohésion.

MusicRadar : mettre le crackle sur son propre bus, **passe-haut vers 300 Hz**, et doser pour qu'il soit « ressenti plus qu'entendu ». Les producteurs ambient mixent volontairement avec un plancher de bruit plus élevé que nécessaire parce qu'une texture de fond constante tient le morceau ensemble.

`[I]` **Point technique important : ce bruit doit être exclu du sidechain et non compressé par le bus master.** S'il pompe, il cesse d'être un plancher et devient un élément rythmique qui se révèle.

### Granulaire `[D]`

Splice : **Grain Size** contrôle la longueur de boucle — vers la gauche il rallonge (répétition plus lente, ton plus grave), vers la droite il monte le ton. **File Position** est le paramètre clé pour explorer le matériau source. Méthode : étirement via le warp d'Ableton **2× à 8×**, mode **Texture** avec **Flux à zéro**, puis superposition de transitoires nets sur des queues warpées.

Les grains font généralement **moins de 50 ms**. Point de départ cité : mode Cloud, grain size ~80 ms, densité 70 %, balayage lent de la position. Le **traitement granulaire récursif** — réinjecter la sortie dans un second moteur avec d'autres réglages — produit des textures inatteignables en une passe.

### Points de départ

| | Réglage |
|---|---|
| **Plancher de bruit** | Bus dédié, passe-haut ~300 Hz, « senti pas entendu ». `[I]` viser −45 à −55 dBFS RMS. **Hors sidechain, hors compression master.** |
| **Granulaire** | Grains < 50 ms pour la texture fine, ~80 ms / densité 70 % pour le nuage tenu. Warp Texture avec Flux à 0, étirement 2× à 8×. Puis passe récursive. |
| **Bruit intégré au patch** | Couche de bruit dans le synthé, passe-haut **au-dessus de la fondamentale de la note**, enveloppe courte pour l'attaque ou longue pour l'air. Variante : bruit filtré comme **source de modulation** du cutoff. |

---

## 6. Risers, downlifters, impacts

### Méthode complète `[D]`

SOS *Cubase: Creating Risers & Impacts* :
- **Superposer sur tout le spectre** : « pour un impact je pourrais partir d'un gros sample de batterie avec beaucoup de grave, peut-être un synthé ou une guitare avec du médium, et une cymbale avec plus d'aigu ».
- **Inverser** les sons tenus pour que le silence construise vers le pic.
- **Pitch-shift** vers le bas pour épaissir les impacts.
- Enveloppes de pitch, filtre et amplitude sur la piste de sample.
- Réverb et delay généreux en fin de chaîne, **paramètres automatisés**.
- **Aligner les points de crête** : pour un riser le maximum est à la fin, pour un impact au début.
- Partir de samples bruts **longs** pour garder de la latitude.

`[D]` Point Blank : deux approches, synthèse (automation de pitch + balayage de filtre + réverb ; **les formes simples saw ou square répondent le mieux à la modulation**) et sample (prendre une queue distincte, la bouncer, l'inverser, appliquer un fade-in). Le mouvement classique : automater un passe-bas qui s'ouvre, monter le volume jusqu'au temps 1, puis **couper net sur le downbeat** pour que le drop frappe contre le silence soudain.

`[I]` **Le riser ne fonctionne pas par sa montée mais par ce qu'il laisse en partant. La coupure nette sur le temps 1 est plus importante que la montée elle-même.** Deuxième point : riser et downlifter doivent se croiser — le downlifter sur la dernière mesure fait descendre l'attention pendant que le riser la monte, ce qui crée l'ambiguïté qui rend le drop lisible.

### Points de départ

| | Construction |
|---|---|
| **Riser 8 mesures** | Bruit filtré, HP de **200 Hz à 8 kHz** sur 8 mesures, résonance ~30 %. + couche tonale saw avec pitch +12 à +24 demi-tons sur les 2 dernières mesures. + queue de réverb inversée. **Coupure nette au temps 1.** |
| **Downlifter 1 mesure** | Même source tonale, pitch −12 à −24 demi-tons sur 1 mesure, LP qui se ferme, réverb qui monte en send. Sur la dernière mesure ou demi-mesure avant le drop. |
| **Impact** | 3 couches : grave (kick ou tom pitché vers le bas), médium, aigu (crash). **Points de crête alignés au début.** Réverb longue en insert, puis fade pour ne pas manger la mesure 1 du drop. |

---

## 7. Pourquoi un son statique fatigue

### Ce qui est documenté

`[D]` *Rapid Adaptation to the Timbre of Natural Sounds* (Scientific Reports, 2018) : les auditeurs **s'adaptent au timbre** d'une grande variété de sons naturels, l'adaptation produisant des effets consécutifs qui altèrent la perception. https://www.nature.com/articles/s41598-018-32018-9

`[D]` *Auditory adaptation to gradual rise or fall in intensity of a tone* : après un son dont l'intensité monte ou descend progressivement, un son de test stable **semble** se ramollir ou se renforcer. Le système auditif s'adapte aux changements graduels.

`[I]` — donné comme avis, la littérature ne le dit pas ainsi. **Le système auditif normalise rapidement tout stimulus invariant.** Un timbre qui ne change pas cesse de porter de l'information au bout de quelques secondes et devient un fond. Le mouvement ne sert pas à faire joli, il sert à maintenir le son dans la catégorie « événement » plutôt que « fond ».

**Corollaire utile : un pad statique n'est pas forcément un défaut.** Si on *veut* qu'il devienne un fond, c'est exactement le bon outil.

### Les trois échelles de temps `[I]`, dérivé des chiffres des trois patchs

| Échelle | Vitesse | Ce qu'on module | Exemples relevés |
|---|---|---|---|
| **Grain** | 5–20 Hz | Sync d'oscillateur, FM, position de wavetable, pan | XLFO 1 à 13 Hz |
| **Respiration** | 0,1–1 Hz | Cutoff, offset de filtre, phase, chorus | XLFO 2 à 0,5 Hz ; chorus 0,22 Hz ; LFO Rhodes 1 Hz |
| **Arrangement** | 8–20 s | Niveau d'une couche entière, rate d'un autre LFO | EG2 attaque 12 s ; EG3 attaque 15 s |

`[CALC]` À 120 BPM (mesure = 2 s), 15 s ≈ 7,5 mesures. À 126 BPM, ≈ 7,9 mesures. **Les enveloppes de 12–15 s correspondent donc précisément à une phrase de 8 mesures.**

### Trois règles `[I]`

1. **Éviter les périodes rationnelles simples sur les LFO lents.** Un LFO à exactement 1/8 de mesure devient un motif rythmique reconnaissable. À 0,22 Hz ou 0,5 Hz contre 126 BPM, on obtient un déphasage permanent.
2. **Sommer deux LFO** sur une même destination tue la périodicité audible.
3. **Moduler un modulateur** : c'est la seule façon d'obtenir du mouvement qui ne se répète pas sur la durée d'un morceau.

---

## Réserves

Deux pages ont refusé la lecture (HTTP 403) : Point Blank sur les risers, et Perfect Circuit sur l'histoire du supersaw. Leurs informations viennent des extraits de recherche, pas des pages entières.

Les chiffres de plucks Serum (0–5 ms / 200–500 ms / ENV2 250 ms) viennent de snippets de résultats, pas de pages lues intégralement. Statut de preuve plus faible que les patchs Attack Magazine et la thèse Szabo.
