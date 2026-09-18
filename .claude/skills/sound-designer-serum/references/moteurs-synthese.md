# Moteurs de synthèse — fiche de référence

Recherche web du 18 septembre 2026. `[D]` = documenté par la source citée. `[I]` = interprétation, à vérifier à l'oreille.

**Le manuel officiel de Serum 2 existe et fait 354 pages** : https://xferrecords.com/manual/serum-2/docs (version web : https://xferrecords.com/web-manual/serum-2/welcome). Deux autres recherches avaient conclu qu'il était introuvable — il ne l'est pas. À consulter en premier avant tout blog.

---

## 1. Soustractive

### Contenu harmonique des formes d'onde `[D]`

| Forme | Harmoniques | Amplitude du n-ième |
|---|---|---|
| Sinus | fondamentale seule | — |
| Dent de scie | toutes | 1/n |
| Carrée | impaires seulement | 1/n |
| Triangle | impaires seulement | 1/n² |

Sources : SOS *What's In A Sound?* (https://www.soundonsound.com/techniques/whats-sound), till.com *A Palette of Static Audio Waveforms* (https://till.com/articles/wavepalette/).

`[I]` La scie perce parce qu'elle apporte pairs et impairs. La carrée, privée des pairs, sonne creuse et nasale : un lead qui doit exister sans encombrer les octaves. Le triangle en 1/n² est un sinus légèrement peigné, donc un sub qui garde un peu de grain.

**Operator nomme ses ondes par le nombre d'harmoniques resynthétisées** (`Saw 32`, `Square 6`) `[D]`. Sur un pluck aigu, passer de Saw 32 à Saw 8 supprime l'aliasing sans toucher au filtre.

### Filtres `[D]`

SOS *Of Responses & Resonance* : quatre familles, pentes 6 / 12 / 24 dB/oct, Q faible = pic large, Q élevé = pic prononcé, et au Q maximal le filtre auto-oscille et devient un oscillateur.

La topologie compte autant que la pente (Attack Magazine). Moog 24 dB crémeux et auto-oscillant, Prophet-5 OTA lisse pour nappes, MS-20 très résonant, SEM state-variable **sans** auto-oscillation, TB-303 diode ladder à pic marqué **sans** auto-oscillation.

**Ce qui est disponible ici** :
- **Drift** : Type I = 12 dB/oct (DFM-1, réinjecte de la distorsion), Type II = 24 dB/oct (Cytomic MS2, Sallen-Key, écrêtage doux qui limite la résonance). `Key` de 0 à 1. HP séparé.
- **Wavetable** : LP/HP/BP/notch + filtre **Morph** qui balaie LP → BP → HP → notch. 12 ou 24 dB. Cinq circuits : *Clean*, *OSR*, *MS2*, *SMP*, *PRD* (ladder, **sans limitation de résonance**, donc le plus prompt à auto-osciller). Routage Serial / Parallel / Split.
- **Serum 2** : `MG Low 6/12/18/24` (ladder Moog), `Low`/`High 6/12/18/24` (state-variable), `Band/Peak/Notch`, plus `MG Ladder`, `Acid Ladder`, `EMS Ladder`, `MG Dirty`. Le paramètre **`FAT`** ajoute de la saturation dans le chemin de résonance : il apaise la résonance **en enrichissant** le contenu harmonique.

`[I]` `FAT` est le bon levier quand une résonance à 12 dB siffle dans les 2–4 kHz : il la dompte en ajoutant des harmoniques, là où un EQ creuserait.

### Enveloppes `[D]`

A, D, R sont des **temps**, S est un **niveau**. L'attaque détermine le caractère percussif, le decay le temps de chute vers le sustain.

Serum 2 ajoute **DELAY** et **HOLD** (DAHDSR), le DELAY étant synchronisable au tempo.

**Piège documenté par Xfer** : avec une onde lisse et une attaque très rapide, un clic se produit si `PHASE` n'est pas sur un passage par zéro (0 % ou 50 % pour un sinus). Le contrôle `RAND` randomise la phase à chaque note, ce qui supprime l'effet « laser zap » mais introduit une variation de timbre par annulation entre oscillateurs.

### Points de départ `[I]`

**Sub de fondation (deep house 120 BPM)** — une onde, sinus ou triangle, mono, unison off. LP 24 dB à 300 Hz, résonance 0, `Key` 0.00 pour un timbre constant sur toute la tessiture. Amp A 2 ms, S 100 %, R 80–120 ms. Jamais de résonance dans le grave : elle crée des bosses qui tuent la lisibilité.

**Pluck house (126 BPM)** — scie, LP 24 dB, `Key` 0.5–0.7. Enveloppe de **filtre** A 0, D 120–180 ms, S 0, coupure de 6 kHz vers 500 Hz. Enveloppe d'**amplitude** plus longue (D ≈ 250 ms) pour que la queue s'assombrisse au lieu de se couper. Résonance 15–25 % maximum.

---

## 2. FM

### Le mécanisme, chiffré `[D]`

SOS *An Introduction To Frequency Modulation* :
- l'AM crée deux bandes latérales, la **FM en crée une série infinie**, aux fréquences ωc ± n·ωm ;
- **indice de modulation β = Δωc / ωm**, donc proportionnel à l'amplitude du modulateur et **inversement** proportionnel à sa fréquence ;
- largeur de bande ≈ **B = 2·ωm·(1 + β)** ;
- β ≈ 0,1 donne un résultat proche d'une AM ; β ≈ 5 donne un spectre bien plus complexe ;
- l'**amplitude** de chaque composante dépend de β (fonctions de Bessel), la **position** ne dépend que de la fréquence du modulateur.

`[I]` L'indice est le seul bouton de brillance de la FM. Un modulateur avec sa propre enveloppe **est** un filtre passe-bas dynamique, sans filtre.

### Rapports entiers et non entiers `[D]`

SOS *More On Frequency Modulation* :
- **1:1** → série harmonique quel que soit le carrier ;
- **1:2** → harmoniques impaires seulement, « sonne comme une carrée filtrée » ;
- **1:3** → approche le spectre d'une pulse à 33 % ; **1:4** approche une carrée ;
- rapport non entier (ex. 1:1,2138754) → complètement inharmonique, **et le carrier n'est plus la fréquence la plus basse du spectre**.

Mécanisme : si ωm est un multiple entier de ωc, toutes les bandes latérales retombent **sur** des harmoniques et l'oreille les fusionne en une hauteur unique. Sinon elles tombent **entre** les harmoniques, la fusion échoue, on entend du métal. C'est la physique des cloches.

**Operator** dit la même chose en une phrase : `Coarse` fixe le rapport en nombres entiers (relation **harmonique**), `Fine` en fractions (relation **inharmonique**). Le bouton `Q (Quantize)` force la fréquence à ne bouger que par entiers.

Autres faits Operator `[D]` : 4 opérateurs, 11 algorithmes ; mode **Fixed** où l'oscillateur ignore la hauteur de note et descend à 0,1 Hz, « utile pour des sons de batterie » ; `Feedback` sur tout oscillateur non modulé ; avertissement explicite sur l'aliasing, auquel « la FM est particulièrement sujette ».

**Serum 2** implémente la FM en warp mode, trois variantes `[D]` :
- **Linear** : garde la hauteur globale même très modulé, « propre, musical, idéal cloches et pads » ;
- **Exp** : plus brillant ou plus dur ;
- **Thru-Zero** : quand la modulation pousse la porteuse sous zéro, l'oscillateur **inverse sa phase** au lieu de s'arrêter. C'est la différence technique majeure avec une FM analogique.

### ⚠ Contradiction relevée

Le *FM Synthesis Cookbook* de Plugin Boutique prescrit pour une cloche un « ratio **non entier** (4:1 ou plus) ». **4:1 est entier**, et SOS établit qu'un rapport entier donne un spectre harmonique. L'article se contredit. Pour une cloche il faut un rapport franchement non entier : 1:1,41 · 1:3,14 · 2:2,73. **Suivre SOS.**

### Points de départ `[I]`

**Basse FM bass house (126 BPM)** — 2 opérateurs en série. Carrier sinus Coarse 1, modulateur sinus Coarse 1 (donc 1:1, spectre de type scie). Level du modulateur piloté par une enveloppe D ≈ 90 ms, S ≈ 20 % : attaque brillante, corps quasi sinusoïdal. Feedback 8–15 %. LP 24 dB à 1,2 kHz en sécurité. Pour growler : LFO sync 1/8 sur le Level du modulateur, 30 %.

**Pluck métallique** — rapport 1:3,5 ou 1:7, indice faible (Level modulateur ~25 %), enveloppe du modulateur A 0 / D 60 ms / S 0, enveloppe d'ampli A 0 / D 400 ms / S 0.

**Percussion de transition** — Operator en mode **Fixed**, carrier 200 Hz, modulateur 283 Hz (≈ ×1,414), indice moyen, decay 1,5–3 s. Dans Serum, même chose avec le warp **Thru-Zero**.

---

## 3. Wavetable

### Ce que c'est réellement `[D]`

Serum 2 : « une petite quantité d'audio numérique lue en boucle ». Jusqu'à **256 frames de 2048 échantillons** en 32 bits, soit un fichier maximal de **2 Mo exactement**.

Ableton : « la vraie puissance vient du déplacement entre les échantillons pendant que la note joue ».

`[I]` **La différence avec un oscillateur classique** : un VCO produit une forme d'onde au spectre figé ; une wavetable produit une **trajectoire dans un espace de spectres**, indexée par un paramètre modulable. Un oscillateur classique a besoin d'un filtre pour évoluer, une wavetable évolue sans filtre. Corollaire moins dit : la wavetable ne modifie pas un spectre, elle en **remplace** un par un autre, d'où des sauts quand la table est mal interpolée.

### Interpolation `[D]`

Xfer : une bonne wavetable peut ne comporter que quelques frames, les autres sont **interpolées** par **crossfading (mix blend)** ou par **spectral morphing (frequency + phase blend)**. Elles sont calculées au chargement ; Serum embarque le *type* d'interpolation, pas les formes interpolées.

`[I]` Deux tables identiques frame par frame peuvent se comporter très différemment au balayage de `WT POS` selon l'interpolation : un crossfade produit des annulations de phase (effet flanger), un morphing spectral reste lisse. **Si un balayage de WT POS produit des creux de volume, c'est l'interpolation, pas la table.**

### Unison `[D]`

Serum 2 : jusqu'à **16 voix**, mais « cela peut donner un son plus *cloudy* ; **le nombre magique classique pour l'unison est 7** ». Le gain est compensé automatiquement.

- **MODE** : Linear (dense et puissant, idéal supersaw), Exp (espacement croissant), Inv (voix graves plus désaccordées, effets de phasing), Random (organique ou chaotique).
- **STACK** : Off / 12 (1-3x) octaves / 12+7 (1-3x) quintes + octaves / Center-12 / Center-24.
- **BLEND** : offset de niveau des voix d'unison par rapport aux voix centrales, **défaut 75 %**, ne s'applique qu'au-delà de 2 voix.
- **WIDTH**, **RANGE**, **WT POS** (étalement par voix), **WARP 1 / 2** (étalement du warp par voix).

Ableton Wavetable, six modes : *Classic*, *Shimmer*, *Noise* (idem Shimmer mais beaucoup plus rapide, textures soufflées), *Phase Sync* (phases synchronisées à la note, fort effet phaser), *Position spread*, *Random note*.

### Warp modes de Serum 2 — liste documentée `[D]`

**Sync** — synchronise sur un oscillateur interne ; harmonieux quand les deux sont dans un rapport en nombres entiers.

**Alt Warp** — `Bend +` / `Bend −` / `Bend +/−` (**50 % = neutre**), `PWM`, `Asym ±`, `Flip`, `Mirror` (qualité octaviée, toujours audible), `Remap 1–4` (remapping dessinable ; Remap 4 « quand on veut quelque chose de méchant »), `Quantize` (réduction de résolution **sur la forme d'onde**, donc **l'aliasing suit parfaitement la hauteur**, contrairement à un Redux), `Odd/Even` (**50 % = signal d'origine, 0 % = impaires seules, 100 % = paires seules**, ce qui crée un effet d'octave puisque la fondamentale disparaît).

**Filter** — `LPF`, `HPF` au niveau de l'oscillateur.

**Distortion** — `Tube`, `Soft/Hard Clip`, `Diode 1/2`, `Linear Fold`, `Sine Fold`, `Zero-Square`, `Asym`, `Rectify`, `Sine Shaper`, `Stomp Box`, `Tape Sat.`, `Soft Sat.`

**FM / PD / AM / RM** — depuis l'oscillateur B ou C, le Noise, le Sub, le Filter 1 ou 2.

Ableton Wavetable n'a que trois familles : **FM** (`Amt` + `Tune` ; **50 % ou −50 % = une octave, 100 % ou −100 % = deux octaves, entre ces valeurs rapports inharmoniques**), **Classic** (`PW` applicable à **toutes** les wavetables, pas seulement aux carrées, et `Sync`), **Modern** (`Warp` et `Fold`).

### Deux pièges Ableton `[D]`

Les oscillateurs de Wavetable sont **band-limités et sans aliasing à n'importe quelle hauteur — tant qu'aucune modulation n'est appliquée**. La restriction est explicite dans le manuel et omise par la plupart des tutoriels.

Le mode **Hi-Quality** est **désactivé par défaut depuis Live 11.1** sur les nouvelles instances, mais **activé** sur les sets antérieurs. Si un preset sonne différemment d'un morceau à l'autre, c'est probablement ça. Désactivé, la modulation est calculée tous les 32 échantillons et économise jusqu'à 25 % de CPU.

### Points de départ `[I]`

**Lead large** — unison **7**, MODE Linear, DETUNE 0,15–0,22, BLEND 75 %, WIDTH 60–70 %. `WT POS` modulé par ENV 2 sur **15–20 % seulement** : au-delà le timbre change trop et la note perd son identité. **Fondamentale en mono obligatoire.**

**Nappe évolutive (120 BPM)** — unison **3**, MODE Random, DETUNE 0,08, STACK 12+7 pour empiler quinte et octave sans jouer d'accord. `WT POS` modulé par un LFO sync 8 mesures, 40 %. Warp `Bend +/−` à 50 % (neutre) puis modulé ±10 % par un second LFO désynchronisé du premier.

**Sub mono avec du grain** — sinus, unison **1**, `WARP` = `Odd/Even` à 30 % ou `Sine Shaper` faible. Le grain vient du warp, pas du detune. **C'est la seule façon d'avoir de la matière sous 120 Hz sans casser le mono.**

---

## 4. Granulaire

### Paramètres `[D]`

SOS : un grain dure « généralement entre un centième et un dixième de seconde » (10–100 ms). Chaque grain est fondu en entrée et sortie par une enveloppe, le *smoothing*, sans quoi on n'entend que des clics. Propriété fondatrice : **vitesse, hauteur et formants s'ajustent indépendamment**.

Serum 2 (p. 98–103) :
- **SCAN** = vitesse de la tête de lecture. Élevé → départs de grains étalés, **moins de recouvrement** ; bas → son étiré, drone. **Négatif = lecture inversée, 0 = tête figée.** Range ±200 % (défaut) / ±400 % / ±800 %.
- **DENS** = cadence, en **Free (Hz)**, **BPM Sync**, ou **Grains** (taux calculé pour qu'un nombre constant de grains joue en permanence). `Jump Start` déclenche plusieurs grains à l'attaque ; **désactivé, l'attaque est plus douce**.
- **LENGTH** = durée d'un grain, en Free / BPM Sync / Percent. Grains courts = nets et rythmiques, longs = tenues lisses.
- **Fenêtres** : `Hann` (fondu symétrique lisse, texture cohésive), `Welch` (parabolique). Réglables par `AMOUNT`, `SKEW`, `SHAPE`.
- Randomisation par grain : `OFFSET`, `DIR` (avec *Reverse Grains*), `PITCH`, `RAND` sur length / pan / level.
- Avertissement explicite : **« Granular synthesis can be CPU intensive ».**

**Granulator III** (Live 12 Suite, Robert Henke) : grains de **2 ms à 2 s**. Trois modes : *Classic*, *Looping*, *Cloud*. `Shape` **sous 50 met l'emphase sur les transitoires**, donc plus percussif. Neuf filtres.

### ⚠ Contradiction relevée

SOS dit 10–100 ms, Xfer dit « quelques millisecondes », Granulator III va de 2 ms à 2 s. **Il n'existe pas de définition normalisée.**

`[I]` Le seuil qui compte perceptivement est **~50 ms** : en dessous, la cadence de répétition entre dans la bande audio et le grain produit une **hauteur propre** indépendante de celle du sample. Au-dessus, on entend le sample.

### Limites `[I]`

Le granulaire a une **hauteur floue**, donc il est inutilisable pour une ligne mélodique ou une basse. Et un sample mal choisi reste reconnaissable : le granulaire ne désidentifie pas magiquement.

### Points de départ `[I]`

**Nappe de fond** — source : un bounce de son propre pad. LENGTH 120 ms, DENS en mode Grains à 8–12 grains simultanés, SCAN 0,05 (quasi figé), fenêtre Hann, PITCH rand ±6 cents, RAND (PAN) 60 %, `Jump Start` **désactivé**. Puis LP 12 dB à 4 kHz et reverb longue.

**Texture rythmique** — LENGTH en BPM Sync 1/32, DENS en BPM Sync 1/16, SCAN ±150 %, DIR rand 30 % avec *Reverse Grains* modulé par un LFO carré 1 mesure, `SKEW` fort. `Jump Start` activé.

**Riser organique** — SCAN automatisé de 0 à +400 % sur 4 mesures, LENGTH automatisé de 300 ms à 15 ms en parallèle : le son passe d'un drone à un bourdonnement tonal à mesure que la longueur de grain descend sous le seuil audio.

---

## 5. Additive et modélisation physique

### Additive `[D]`

*Synth Secrets* part 14 : somme de sinus aux multiples entiers de la fondamentale. Le point crucial n'est pas la somme mais **l'enveloppe d'amplitude indépendante de chaque harmonique**. Sur une corde pincée les aigus décroissent plus vite, d'où l'assombrissement. **« Tout timbre sonnera statique et organ-like s'il ne change pas dans le temps. »**

Coût : un oscillateur + un EG + un VCA **par harmonique**, d'où une mise en œuvre toujours numérique. L'orgue Hammond est un synthé additif : 91 roues phoniques, 9 drawbars à 9 niveaux.

**Limite documentée** : les instruments réels contiennent un **résidu de bruit** que la décomposition harmonique laisse de côté. Il faut ajouter filtre et générateur de bruit — c'est la *Spectral Modelling Synthesis*.

Disponible ici : l'**éditeur d'harmoniques d'Operator** (mode `User`, 16 / 32 / 64 partiels) et le **mode Spectral de Serum 2**, qui décompose un son en partiels individuels et permet de glisser d'une texture à une autre. Avertissement Xfer : **CPU intensive**.

`[I]` **Le meilleur usage en électro n'est pas d'en faire un moteur principal mais un fabricant de wavetables.** Dessiner 8 harmoniques dans Operator, resampler, importer dans Serum : on obtient une table dont on connaît exactement le spectre, ce qu'aucune table factory ne donne.

### Modélisation physique `[D]`

**Karplus-Strong** (Stanford, fin des années 70) : bruit blanc passé dans une boucle de réaction filtrée récursive, effet de filtre en peigne ; en changeant les paramètres on change les propriétés physiques perçues. Évolution : les **guides d'ondes numériques**, lignes à retard modélisant la géométrie. Premier synthé commercial : **Yamaha VL1, 1994**.

**Limite documentée** : exige une technique de jeu maîtrisée, courbe d'apprentissage plus raide qu'un synthé classique. La technologie n'a jamais supplanté l'échantillonnage.

**Collision** (Ableton × Applied Acoustics) : excitateurs `Mallet` (`Stiffness` bas = maillet mou, impact long, moins d'aigus) et `Noise`, puis deux résonateurs avec 7 types : Beam, Marimba, String, Membrane, Plate, Pipe, Tube. Le paramètre le plus important est **`Material`** : valeurs basses = les graves décroissent plus lentement (bois, caoutchouc, nylon), valeurs hautes = les aiguës décroissent plus lentement (verre, métal). Le menu `Quality` **réduit le nombre d'harmoniques calculées** : c'est un compromis CPU, pas un réglage neutre.

**Analog** est aussi de la modélisation physique, mais **de circuits**, pas d'objets. **Tension** modélise les cordes ; Ableton avertit qu'« il est très facile de trouver des combinaisons qui ne produisent aucun son » et « très facile de créer des sons extrêmement forts ».

`[I]` Utile pour des percussions accordées qui suivent la tonalité, et comme résonateur en insert pour donner un corps accordé à une percussion sèche. **Inutile pour des basses ou des leads de bass house** : cher en CPU et difficile à faire sonner produit.

---

## 6. Distorsion de phase et waveshaping

### Distorsion de phase `[D]`

Introduite en **1984** par Casio sur la série **CZ**, par l'ingénieur Mark Fukuda. Principe : l'accumulateur de phase suit une **fonction non linéaire** au lieu d'un incrément linéaire, ce qui déforme la sortie et modifie les harmoniques. Le paramètre **DCW** dose la déformation : « le sinus peut être gauchi en carrée ou en dent de scie », et le résultat est « très similaire à ce qu'on entend en jouant avec la coupure d'un filtre — **alors qu'il n'y a aucun filtre dans un synthé PD classique** ».

Relation avec la FM : la PD est « essentiellement un cas particulier de la modulation de phase », la différence étant que le modulateur PD tourne à la fréquence du carrier ou à de simples multiples.

Précision utile : **les formes d'onde « résonantes » des CZ ne sont pas produites par la distorsion de phase** mais par une synchronisation fenêtrée, technique distincte.

Dans Serum 2, la PD est une catégorie de warp : `PD (B)`, `PD (C)`, `PD (Noise)`, `PD (Sub)`, `PD (Filter 1/2)` et **`PD (Self)`**.

`[I]` La PD donne une montée de brillance très proche d'une ouverture de filtre, **sans résonance, sans le coût d'un filtre, et parfaitement stable en hauteur** (contrairement à la FM exponentielle). Sur un pad qui doit s'ouvrir sans le grain « filtre », `PD (Self)` piloté par une enveloppe est une piste que peu de gens empruntent.

### Waveshaping `[D]`

Serum 2 : **`Linear Fold`** replie la forme d'onde dès qu'elle dépasse un seuil, caractère « métallique ou dur ». **`Sine Fold`** replie sur une sinusoïde, « lisse mais dynamique, de chaleureux à agressif ». `Rectify` retourne ou supprime une moitié. `Asym` applique des distorsions différentes aux alternances positive et négative.

`[I]` **Différence entre wavefolding et saturation** : la saturation ajoute des harmoniques **dans l'ordre** (2e, 3e, 4e) et reste chaude ; le wavefolding en ajoute **par paquets non monotones**, d'où le timbre métallique du modulaire ouest-côtier. Le fold est donc un moyen d'obtenir un contenu quasi-inharmonique **sans FM et sans désaccorder la fondamentale**.

---

## 7. Quel moteur pour quoi

| Moteur | Excelle à | Limite principale | CPU |
|---|---|---|---|
| Soustractive | corps, chaleur, filtre lisible, subs | statique sans modulation | faible |
| FM | attaques dures, cloches, plucks, growl | non intuitive, aliasing | faible |
| Wavetable | évolution sans filtre, supersaw, basses | sauts si interpolation inadaptée | moyen |
| Granulaire | textures, time-stretch extrême | hauteur floue, CPU | élevé |
| Additive / Spectral | spectres sur mesure, morphing | pas de bruit résiduel, lourd | élevé |
| Modélisation physique | percussions accordées, résonances | jeu exigeant, peu adapté aux basses | moyen-élevé |
| PD / Waveshaping | brillance « façon filtre » sans filtre | moins de contrôle que la FM | très faible |

---

## 8. Ce qui est chiffré dans une doc constructeur, et rien d'autre

Les seules valeurs issues d'une documentation officielle : unison max 16 et nombre magique 7 · BLEND défaut 75 % · Odd/Even 50 % = neutre · Bend +/− 50 % = neutre · FM d'Ableton 50 % = une octave, 100 % = deux octaves · Scan range ±200/400/800 % · 2048 échantillons × 256 frames · Fixed jusqu'à 0,1 Hz · 16/32/64 partiels · −25 % de CPU en Hi-Quality off.

**Tout le reste des chiffres vient de tutoriels ou d'interprétation.** Les traiter comme des points de départ, pas comme des références.

Coquille du manuel Serum 2 : le menu contextuel de `WT POS` s'appelle « Smooth **Interpretation** », presque certainement pour *Interpolation*. Ne pas y chercher un sens caché.
