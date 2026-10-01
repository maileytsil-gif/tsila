---
titre: "music-with-code (Kan-A-Pesh) — Partie II Harmonie : notes de recherche (voicings, drop 2, tensions) — français"
source: https://raw.githubusercontent.com/Kan-A-Pesh/music-with-code/master/docs/research/partie2_harmonie.md
recupere_le: 2026-09-24
mode: texte integral
langue: fr
axe: harmonie ; voicings
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

# Partie II — Harmonie : Notes de recherche

> Notes de recherche factuelles pour la librairie pédagogique **music-by-code**.
> Objectif : **zéro approximation théorique fausse**. Tous les chiffres sont vérifiés contre des sources fiables (Wikipedia EN, musictheory.net / Open Music Theory, pressbooks de théorie, CCRMA/SFU, etc.).
> Les valeurs en cents sont arrondies au dixième sauf indication contraire.

---

## 1. Intervalles & accordage

### 1.1 Les cents et le 12-TET

Un **cent** est l'unité logarithmique standard de mesure des intervalles. Par définition :

$$\text{cents} = 1200 \cdot \log_2\!\left(\frac{f_2}{f_1}\right)$$

- L'octave (ratio 2:1) vaut exactement $1200 \cdot \log_2(2) = 1200$ cents.
- Le 12-TET (12-tone equal temperament) divise l'octave en **12 demi-tons égaux**, donc chaque demi-ton vaut $1200/12 = 100$ cents.
- **C'est pourquoi 100 cents = 1 demi-ton** : le cent est défini comme 1/100 de demi-ton tempéré, et 12 demi-tons × 100 = 1200 cents = 1 octave.

Le ratio de fréquence d'un demi-ton tempéré est donc :

$$r_{1/2} = 2^{1/12} \approx 1{,}059463$$

Un intervalle de $n$ demi-tons tempérés a le ratio $2^{n/12}$ et vaut $100 \cdot n$ cents.

**Formule inverse** (cents → ratio) : $\dfrac{f_2}{f_1} = 2^{\,\text{cents}/1200}$.

### 1.2 Just intonation : ratios purs

L'intonation juste (just intonation) construit les intervalles à partir de **rapports d'entiers simples**. Les harmonies sont d'autant plus consonantes que les entiers sont petits. Table 5-limit (premiers 2, 3, 5) :

| Intervalle | Ratio juste | Cents (juste) | Cents (12-TET) | Écart |
|---|---|---|---|---|
| Unisson | 1/1 | 0 | 0 | 0 |
| Seconde mineure | 16/15 | 111,7 | 100 | +11,7 |
| Seconde majeure | 9/8 | 203,9 | 200 | +3,9 |
| **Tierce mineure** | **6/5** | **315,6** | 300 | **+15,6** |
| **Tierce majeure** | **5/4** | **386,3** | 400 | **−13,7** |
| **Quarte juste** | **4/3** | **498,0** | 500 | −2,0 |
| Triton | 45/32 (ou 7/5) | ~590 | 600 | ~−10 |
| **Quinte juste** | **3/2** | **702,0** | 700 | **+2,0** |
| Sixte mineure | 8/5 | 813,7 | 800 | +13,7 |
| Sixte majeure | 5/3 | 884,4 | 900 | −15,6 |
| Septième mineure | 9/5 (ou 16/9) | 1017,6 | 1000 | +17,6 |
| Septième majeure | 15/8 | 1088,3 | 1100 | −11,7 |
| **Octave** | **2/1** | **1200** | 1200 | 0 |

Ratios canoniques à retenir : octave **2:1**, quinte **3:2**, quarte **4:3**, tierce majeure **5:4**, tierce mineure **6:5**, sixte majeure **5:3**.

### 1.3 Le comma et pourquoi le tempérament égal est un compromis

Le problème fondamental : **on ne peut pas empiler des quintes pures (3:2) et retomber sur une octave pure (2:1)**. Concaténer des intervalles = multiplier leurs ratios ; aucun nombre fini de quintes pures ne donne une puissance exacte de 2.

- **Comma pythagoricien** : 12 quintes pures (3:2)¹² ≈ 7 octaves, mais l'écart vaut $\left(\frac{3}{2}\right)^{12} / 2^7 = 531441/524288 \approx$ **23,46 cents**.
- **Comma syntonique** (comma de Didyme) : ratio **81/80 ≈ 21,5 cents**. C'est la différence entre la tierce majeure pythagoricienne (81/64 ≈ 407,8 cents) et la tierce majeure juste (5/4 ≈ 386,3 cents).

Le 12-TET **répartit ces commas** : il sacrifie la pureté de tous les intervalles (sauf l'octave) pour rendre toutes les tonalités également jouables et la modulation libre. La quinte tempérée (700 c) est très proche de la juste (702 c, écart +2 c, quasi inaudible), mais les tierces sont nettement décalées.

### 1.4 Battements (beating)

Quand deux sinusoïdes de fréquences proches $f_1$ et $f_2$ sonnent ensemble, l'amplitude résultante oscille à la **fréquence de battement** :

$$f_{\text{batt}} = |f_1 - f_2|$$

La hauteur perçue est la moyenne $(f_1+f_2)/2$, modulée en amplitude à $|f_1-f_2|$.

Régimes perceptifs (source SFU/UNSW) :
- **< ~10 Hz** : une seule hauteur, volume qui « ondule » (battement audible, utilisé pour accorder).
- **~10–60 Hz** : zone de rugosité, désagréable (trop rapide pour compter, trop lent pour fusionner).
- **> ~60 Hz** : le cerveau distingue deux hauteurs séparées.

Usage pratique : pour accorder à l'unisson/à la quinte, on minimise le nombre de battements/seconde.

### 1.5 Consonance / dissonance (Helmholtz, rugosité)

Théorie de Helmholtz puis Plomp & Levelt : la **dissonance sensorielle** (rugosité) provient des battements entre les **harmoniques** des deux sons quand ces harmoniques tombent dans la **même bande critique** de la membrane basilaire.

- Helmholtz : rugosité maximale ~33 Hz de battement (valeur fixe, dépassée depuis).
- Plomp & Levelt : la rugosité maximale survient à **~1/4 de la largeur de bande critique**, donc **dépend de la fréquence** (33 Hz ≈ 1/4 de bande critique seulement autour de 600 Hz).
- Des ratios simples (2:1, 3:2) font coïncider de nombreuses harmoniques → peu de battements → consonance. Des ratios complexes → harmoniques voisines mais non confondues → rugosité → dissonance.

### 1.6 Piège pédagogique clé : tierce juste vs tierce tempérée

- Tierce majeure juste 5:4 = **386,3 cents**
- Tierce majeure tempérée = **400 cents**
- Écart ≈ **13,7 cents** → **audible** (un musicien entraîné perçoit ~5–6 cents). Les tierces du piano tempéré « battent » légèrement par rapport aux tierces pures (chœurs a cappella, quatuors à cordes tendent vers la tierce juste).

⚠ **Divergence** : la septième mineure juste a deux conventions concurrentes — **16/9 ≈ 996,1 c** (mineure pythagoricienne) ou **9/5 ≈ 1017,6 c** (5-limit). La harmonique naturelle (7e harmonique, « blue note ») est encore différente : **7/4 ≈ 968,8 c**. Préciser le contexte dans les notebooks.

⚠ **Divergence** : le triton juste n'a pas de ratio unique — **45/32 ≈ 590 c**, **64/45 ≈ 610 c**, ou **7/5 ≈ 583 c** selon la dérivation.

### Sources (§1)
- Equal temperament — https://en.wikipedia.org/wiki/Equal_temperament
- Five-limit tuning — https://en.wikipedia.org/wiki/Five-limit_tuning
- Syntonic comma — https://en.wikipedia.org/wiki/Syntonic_comma
- Pythagorean comma — https://en.wikipedia.org/wiki/Pythagorean_comma
- Cent (music) — https://en.wikipedia.org/wiki/Cent_(music)
- Beat (acoustics) — https://en.wikipedia.org/wiki/Beat_(acoustics)
- Consonance and dissonance — https://en.wikipedia.org/wiki/Consonance_and_dissonance
- SFU Sonic Handbook (Beats / Consonance) — https://www.sfu.ca/sonic-studio-webdav/handbook/Beats.html
- Just Intonation Explained (Kyle Gann) — https://www.kylegann.com/tuning.html

---

## 2. Gammes & modes

### 2.1 Les 7 modes de la gamme majeure

Tous dérivés de la gamme majeure (mêmes notes, tonique différente). Sur **Do majeur** (notes blanches), chaque mode commence sur un degré.

| Mode | Départ (Do maj) | Pattern (T=ton, ½=demi-ton) | Altérations vs majeur | **Degré caractéristique** | Couleur |
|---|---|---|---|---|---|
| **Ionien** | Do (I) | T-T-½-T-T-T-½ | — (majeur) | — | clair, stable |
| **Dorien** | Ré (II) | T-½-T-T-T-½-T | ♭3, ♭7 | **♮6** (sixte majeure sur mode mineur) | mineur « jazzy », pas triste |
| **Phrygien** | Mi (III) | ½-T-T-T-½-T-T | ♭2,♭3,♭6,♭7 | **♭2** | sombre, tension espagnole/flamenco |
| **Lydien** | Fa (IV) | T-T-T-½-T-T-½ | ♯4 | **♯4** | très lumineux, « rêveur », flottant |
| **Mixolydien** | Sol (V) | T-T-½-T-T-½-T | ♭7 | **♭7** | majeur « bluesy »/dominante, rock |
| **Éolien** | La (VI) | T-½-T-T-½-T-T | ♭3,♭6,♭7 | **♭6** (vs dorien) | mineur naturel, triste |
| **Locrien** | Si (VII) | ½-T-T-½-T-T-T | ♭2,♭3,♭5,♭6,♭7 | **♭5** (quinte diminuée) | instable, dissonant (tonique = accord dim) |

**Spectre de luminosité** (du plus clair au plus sombre) :
**Lydien → Ionien → Mixolydien → Dorien → Éolien → Phrygien → Locrien.**
Chaque cran descend correspond à abaisser un degré d'un demi-ton (cycle des quintes des toniques).

**Degré caractéristique** = la note qui, à elle seule, distingue le mode de son voisin majeur/mineur :
- Lydien : **♯4** (ex : *The Simpsons* thème, Joe Satriani « Flying in a Blue Dream »).
- Mixolydien : **♭7** (ex : « Sweet Home Alabama », « Sweet Child o' Mine » riff, beaucoup de rock/folk).
- Dorien : **♮6** (ex : « Scarborough Fair », « So What » Miles Davis, « Mad World »).
- Phrygien : **♭2** (ex : métal, flamenco ; « Wherever I May Roam » Metallica).
- Locrien : **♭5** (rare en tant que tonalité ; couleurs ponctuelles).

### 2.2 Pentatoniques

- **Pentatonique majeure** : 1-2-3-5-6 (ex Do : Do-Ré-Mi-Sol-La). Pas de demi-tons → aucune dissonance, « universelle ».
- **Pentatonique mineure** : 1-♭3-4-5-♭7 (ex La : La-Do-Ré-Mi-Sol). Base du blues/rock.
- **Blues scale** = pentatonique mineure + **♭5** (« blue note ») de passage.
- La pentatonique majeure de Do et la pentatonique mineure de La contiennent **les mêmes notes** (relatives).

### 2.3 Gammes mineures : pourquoi trois formes ?

| Forme | Construction | Notes (La) | Raison d'être |
|---|---|---|---|
| **Mineure naturelle** (éolien) | 1-2-♭3-4-5-♭6-♭7 | La-Si-Do-Ré-Mi-Fa-Sol | mode mineur de base, mais **pas de sensible** (♭7 à 1 ton sous la tonique) |
| **Mineure harmonique** | naturelle avec **♮7** (7 haussée) | La-Si-Do-Ré-Mi-Fa-**Sol♯** | crée la **sensible** (½ ton sous la tonique) → permet une vraie dominante V7 et la cadence parfaite en mineur |
| **Mineure mélodique** | naturelle avec **♮6 et ♮7** (montant) | La-Si-Do-Ré-Mi-**Fa♯-Sol♯** (montant) | corrige le défaut de l'harmonique |

**Le problème de la seconde augmentée** : en mineure harmonique, hausser le 7e degré crée un intervalle de **seconde augmentée** (3 demi-tons) entre ♭6 et ♮7 (Fa→Sol♯). Cet intervalle « saute » et sonne exotique/maladroit dans une ligne mélodique fluide — c'est à la fois la signature et la limite de l'harmonique.

**Solution mélodique** : on hausse aussi le 6e degré (♮6) **en montant** pour lisser le pas vers la sensible. ⚠ **Convention classique** : en **descendant**, la mélodique redevient identique à la **mineure naturelle** (6 et 7 rabaissés), car la sensible n'est pas nécessaire pour descendre.
⚠ **Divergence** : en **jazz**, la « melodic minor » est souvent utilisée **identique montant ET descendant** (forme « jazz minor »). Préciser le contexte.

**Logique de la sensible (leading tone)** : la sensible à un demi-ton sous la tonique crée une forte attraction vers le repos (résolution ½ ton ascendant). La ♭7 de l'éolien (1 ton) n'a pas cette force, d'où la nécessité de l'harmonique pour les cadences fortes en mineur.

### Sources (§2)
- Mode (music) — https://en.wikipedia.org/wiki/Mode_(music)
- Minor scale — https://en.wikipedia.org/wiki/Minor_scale
- Harmonic minor scale — https://en.wikipedia.org/wiki/Harmonic_minor_scale
- Pentatonic scale — https://en.wikipedia.org/wiki/Pentatonic_scale
- muted.io Modal Scales — https://muted.io/modal-scales/
- Open Music Theory — https://openmusictheory.github.io/

---

## 3. Accords & harmonie

### 3.1 Construction par tierces empilées (tertian harmony)

Les accords occidentaux se construisent en **empilant des tierces** (majeures ≈ 4 demi-tons, mineures ≈ 3 demi-tons) à partir d'une fondamentale.
- 3 notes (1-3-5) = **triade**
- 4 notes (1-3-5-7) = accord de **septième**
- + tierces = 9, 11, 13 (extensions).

### 3.2 Triades

| Triade | Intervalles (demi-tons) | Structure | Symbole | Son |
|---|---|---|---|---|
| **Majeure** | 4 + 3 (3M puis 3m) | 1-3-5 | C, Cmaj | stable, « heureux » |
| **Mineure** | 3 + 4 (3m puis 3M) | 1-♭3-5 | Cm, Cmin, C− | stable, « triste » |
| **Diminuée** | 3 + 3 | 1-♭3-♭5 | C°, Cdim | tendu, instable (triton 1-♭5) |
| **Augmentée** | 4 + 4 | 1-3-♯5 | C+, Caug | flottant, irrésolu (symétrique) |

### 3.3 Accords de septième

| Accord | Triade + 7e | Demi-tons (cumulés) | Symbole | Usage typique |
|---|---|---|---|---|
| **Majeur 7** | maj + 7M | 0-4-7-11 | Cmaj7, CΔ | I et IV (jazz), doux |
| **Mineur 7** | min + 7m | 0-3-7-10 | Cm7, C−7 | ii, iii, vi |
| **Dominante 7** | maj + 7m | 0-4-7-10 | C7 | V → tension, veut résoudre |
| **Demi-diminué (m7♭5)** | dim + 7m | 0-3-6-10 | Cm7♭5, Cø7 | ii° en mineur, sombre |
| **Diminué 7 (dim7)** | dim + 7dim | 0-3-6-9 | C°7, Cdim7 | passage, symétrique |

**Symétrie du dim7** : toutes les notes espacées de 3 demi-tons (tierce mineure). Il n'existe que **3 accords dim7 distincts** ; chaque renversement reproduit un autre dim7. Idéal pour moduler vers n'importe où.

### 3.4 Renversements (inversions)

L'ordre des notes change ; la **basse** (note la plus grave) détermine le renversement :
- **État fondamental** : fondamentale à la basse.
- **1er renversement** : la **tierce** à la basse (chiffrage figuré **6** pour triade, **6/5** pour 7e).
- **2e renversement** : la **quinte** à la basse (**6/4** ; **4/3** pour 7e).
- **3e renversement** (septièmes seulement) : la **septième** à la basse (**4/2** ou **2**).

Effet : même accord, mais basse différente → mouvement de basse plus fluide, couleur changée. Le **6/4** (2e renv. triade) est instable et traité avec règles (cadentiel, de passage, broderie).

### 3.5 Notation chiffrée / symboles d'accords

- **Chiffres romains** : degré + qualité. Majuscule = majeur (I, IV, V), minuscule = mineur (ii, iii, vi), ° = diminué (vii°), + = augmenté. Septièmes : V7, ii7, viiø7.
- **Basse chiffrée (figured bass)** : chiffres arabes indiquant les intervalles au-dessus de la basse (voir renversements ci-dessus).
- **Symboles d'accords (jazz/pop)** : nom de note + qualité (Cm7, G7, Fmaj9, Dm7♭5/F pour slash chord avec basse imposée).

### 3.6 Extensions / tensions (9, 11, 13)

Au-delà de l'octave : 9 = seconde +8ve, 11 = quarte +8ve, 13 = sixte +8ve.
- **9** : 1-3-5-7-9 (Cmaj9, C9, Cm9). Couleur enrichie.
- **11** : sur accords mineurs ou en ♯11 (lydien) sur majeurs ; le 11 juste sur un accord majeur frotte avec la 3ce (à éviter ou à hausser en ♯11).
- **13** : sommet de l'empilement de tierces (7 notes = toute la gamme).
- On omet souvent la 5te (peu d'info) et parfois la fondamentale (jouée par la basse) dans les voicings jazz.

### 3.7 Pourquoi V7 « veut » résoudre (le triton)

L'accord de dominante (V7) contient deux **notes d'attraction (tendency tones)** : le **degré 7 (sensible)** et le **degré 4** de la tonalité. En Do : V7 = G-B-D-**F**, la sensible **B** (3ce de l'accord) et **F** (7e de l'accord).
- B et F forment un **triton** (quinte diminuée / quarte augmentée, 6 demi-tons) → dissonance instable.
- Résolution vers I (C-E-G) :
  - **B → C** : la sensible monte d'½ ton vers la tonique.
  - **F → E** : la 7e descend d'½ ton vers la tierce de I.
- Le triton se résout par **mouvement contraire vers l'intérieur** (B↑, F↓ → intervalle de tierce) ou vers l'extérieur. Cette résolution crée le sentiment de « gravité » et de retour à la maison (tension → détente).

C'est aussi la base de la **substitution tritonique** (jazz) : D♭7 partage le même triton (F/C♭=B) que G7, donc peut le remplacer.

### Sources (§3)
- Dominant seventh chord — https://en.wikipedia.org/wiki/Dominant_seventh_chord
- Seventh chord — https://en.wikipedia.org/wiki/Seventh_chord
- Triad (music) — https://en.wikipedia.org/wiki/Triad_(music)
- Figured bass — https://en.wikipedia.org/wiki/Figured_bass
- Fundamentals/Function/Form, ch. 19 (The Dominant Seventh) — https://milnepublishing.geneseo.edu/fundamentals-function-form/chapter/19-the-dominant-seventh-chord/

---

## 4. Progressions & cadences

### 4.1 Fonctions harmoniques

Trois fonctions principales (modèle tonal) :
- **Tonique (T)** : I (et vi, iii) — repos, stabilité, « maison ».
- **Sous-dominante / pré-dominante (S/PD)** : IV (et ii) — éloignement, prépare la dominante.
- **Dominante (D)** : V (et vii°) — tension maximale, exige résolution vers T.

Cycle fonctionnel typique : **T → S → D → T** (ex : I–IV–V–I).

### 4.2 Cadences

| Cadence | Accords | Effet | Détail |
|---|---|---|---|
| **Parfaite / authentique (PAC)** | V → I | conclusion forte, finalité | V et I à l'état fondamental + tonique au soprano (sinon **IAC**, imparfaite) |
| **Plagale** | IV → I | résolution douce (« Amen ») | pas de sensible dans IV → moins directionnelle |
| **Demi-cadence (HC)** | … → V | suspension, question ouverte | finit **sur** la dominante |
| **Rompue / évitée (DC)** | V → vi | surprise, prolonge | V ne résout pas vers I mais vers vi (déceptive) |

⚠ **Divergence terminologique** : « cadence parfaite » (FR) = *Perfect Authentic Cadence* (EN). La distinction PAC vs IAC (imparfaite) dépend de l'état fondamental ET de la note au soprano. La cadence sur vii°→I est parfois classée IAC.

### 4.3 Le cercle des quintes

Cercle ordonnant les 12 notes par intervalle de quinte juste (sens horaire +5te / −quinte ↔ +4te anti-horaire). Sert à :
- visualiser les armatures (chaque pas horaire = +1 ♯, anti-horaire = +1 ♭),
- expliquer la force des progressions descendant par quinte (V→I, ii→V→I = quintes descendantes successives).

### 4.4 Progressions emblématiques

| Nom | Degrés | Contexte | Exemple |
|---|---|---|---|
| **« Axis » / pop** | I–V–vi–IV | pop universelle | « Let It Be », « With or Without You », d'innombrables hits |
| **ii–V–I** | ii7–V7–Imaj7 | **jazz** (~80–90 % des standards) | mouvement de basse par quintes descendantes |
| **12-bar blues** | I–IV–I–V–I (schéma type : I I I I / IV IV I I / V IV I V) | blues, rock'n'roll | trois accords (souvent dominantes 7) |
| **Anatole / Rhythm changes** | I–vi–ii–V (A) + III7–VI7–II7–V7 (B) | jazz, forme AABA 32 mes. | d'après « I Got Rhythm » (Gershwin) |
| **Cadence andalouse** | i–♭VII–♭VI–V | flamenco, rock, pop | « Stray Cat Strut », « Hit the Road Jack », « Sultans of Swing » |

⚠ **Divergence** : la cadence andalouse s'écrit **i–♭VII–♭VI–V** (relatif éolien/mineur) OU **iv–III–II–I** (relatif phrygien) — deux lectures du même tétracorde phrygien descendant. L'accord final V est **majeur** (♯3 = sensible empruntée), d'où sa couleur « espagnole » (mode phrygien dominant).

### 4.5 Pourquoi certaines progressions « marchent »

- **Mouvement de basse par quarte/quinte** = progression « forte » (root motion). V→I (quinte descendante) est la plus forte ; ii→V→I enchaîne deux quintes descendantes.
- Mouvement par **tierce** = doux (notes communes, ex I→vi).
- Mouvement par **seconde** = « fort » mais sans note commune (ex IV→V, déceptive V→vi).
- Les **notes communes** entre accords lissent la transition ; les **tendency tones** (sensible, 7es) dirigent l'oreille.

### Sources (§4)
- Cadence — https://en.wikipedia.org/wiki/Cadence
- ii–V–I progression — https://en.wikipedia.org/wiki/Ii%E2%80%93V%E2%80%93I_progression
- Rhythm changes — https://en.wikipedia.org/wiki/Rhythm_changes
- Twelve-bar blues — https://en.wikipedia.org/wiki/Twelve-bar_blues
- Andalusian cadence — https://en.wikipedia.org/wiki/Andalusian_cadence
- Circle of fifths — https://en.wikipedia.org/wiki/Circle_of_fifths
- musictheory.pugetsound.edu, Standard Chord Progressions — https://musictheory.pugetsound.edu/mt21c/StandardChordProgressions.html

---

## 5. Voice leading (conduite des voix)

### 5.1 Règles classiques (style choral à 4 voix)

1. **Mouvement le plus court (rule of the shortest way)** : chaque voix se déplace vers la note la plus proche de l'accord suivant ; éviter les grands sauts.
2. **Garder les notes communes** : une note commune à deux accords successifs reste dans la même voix (ex G partagé entre C et G).
3. **Résoudre la sensible** : la sensible (degré 7) monte vers la tonique, surtout aux voix extrêmes (soprano/basse).
4. **Résoudre la septième** : la 7e d'un accord descend par degré conjoint.
5. **Éviter quintes et octaves parallèles** (interdites entre deux voix quelconques).
6. **Éviter les unissons parallèles**.
7. **Éviter les croisements (voice crossing)** et chevauchements (overlapping) de voix.
8. **Privilégier le mouvement contraire** entre basse et soprano.

### 5.2 Pourquoi les quintes (et octaves) parallèles sont « interdites »

Deux voix qui montent/descendent en gardant le même intervalle de **quinte juste** (ou octave) **perdent leur indépendance** : l'oreille les fusionne en une seule voix (la quinte/octave renforce un seul timbre par coïncidence d'harmoniques). Le but de l'écriture à plusieurs voix étant l'**indépendance des lignes**, les parallèles 5/8 « collapsent » la polyphonie. Le mouvement **contraire** ou **oblique** maximise au contraire l'indépendance perçue.

> Note : il s'agit d'une convention **stylistique** (contrepoint tonal / chorals de Bach), pas d'une loi acoustique. Le rock, la musique modale, l'impressionnisme (Debussy) utilisent délibérément les quintes parallèles pour leur couleur.

### 5.3 Types de mouvement (rappel)

- **Parallèle** : même direction, même intervalle.
- **Similaire (direct)** : même direction, intervalle différent.
- **Oblique** : une voix bouge, l'autre tient.
- **Contraire** : directions opposées (le plus indépendant).

### 5.4 Voicings au piano

- **Position serrée (close position)** : toutes les notes (au-dessus de la basse) **dans une octave**. Son compact, dense.
- **Position large (open position)** : notes étalées **sur plus d'une octave**. Son ouvert, aéré.
- **Drop 2** : on prend un voicing serré (4 notes) et on **descend la 2e note la plus aiguë d'une octave**. Transforme un close en open ; voicing de référence en jazz (guitare, piano main gauche, sections de cuivres). Variantes : drop 3, drop 2&4.
- **Four-way close / locked hands** (Shearing/Evans) : mélodie doublée à l'octave + accord serré dessous.

### Sources (§5)
- Voice leading — https://en.wikipedia.org/wiki/Voice_leading
- Consecutive fifths — https://en.wikipedia.org/wiki/Consecutive_fifths
- Contrapuntal motion — https://en.wikipedia.org/wiki/Contrapuntal_motion
- musictheory.pugetsound.edu, Avoiding Objectionable Parallels — https://musictheory.pugetsound.edu/mt21c/AvoidingObjectionableParallels.html
- Open Music Theory, Types of contrapuntal motion — https://openmusictheory.github.io/motionTypes.html
- Learn Jazz Standards, Drop 2 Voicings — https://www.learnjazzstandards.com/blog/drop-2-voicings/

---

## Récapitulatif des divergences signalées

1. **Septième mineure juste** : 16/9 (~996 c) vs 9/5 (~1018 c) vs harmonique 7/4 (~969 c). (§1.6)
2. **Triton juste** : 45/32 (~590 c) vs 64/45 (~610 c) vs 7/5 (~583 c). (§1.6)
3. **Mineure mélodique** : forme classique (descendante = naturelle) vs forme jazz (identique aux deux sens). (§2.3)
4. **PAC vs IAC** : critères variables selon les manuels (état fondamental, soprano, vii°). (§4.2)
5. **Cadence andalouse** : notation i–♭VII–♭VI–V (éolien) vs iv–III–II–I (phrygien) ; le V final est majoré. (§4.4)
6. **Quintes parallèles** : « interdiction » stylistique (contrepoint tonal) et non acoustique. (§5.2)
