# Percussions — fiche de référence

Recherche web du 18 septembre 2026, 20 pages lues dont des analyses de circuits. `[D]` = documenté. `[I]` = interprétation. `[⚠]` = sources contradictoires.

---

## 1. Kick synthétique

### Structure `[D]`

Un oscillateur sinus + une enveloppe de hauteur + une enveloppe d'amplitude sur un VCA. Au déclenchement les deux enveloppes partent ensemble : l'une fait monter brièvement la hauteur puis la laisse retomber vers la fondamentale, l'autre sculpte le volume. SOS formule pareil : composantes graves + balayage de fréquence descendant + click haute fréquence à l'attaque.

### Plage utile `[D]`

**Fondamentale utile 40–60 Hz**, plage exploitable ~35–65 Hz. En dessous de ~35 Hz la plupart des systèmes coupent ; au-dessus de ~65 Hz le son perd son caractère de kick. La zone jouable est donc ≈ **Mi1 (41,2 Hz) → Si1 (61,7 Hz)** en notation scientifique.

### 808 contre 909 — la différence tient à une seule chose `[D]`

| | 808 | 909 |
|---|---|---|
| Forme | sinus 40–50 Hz | triangle 40–50 Hz |
| Filtre | aucun | passe-bas très bas, modulé par l'enveloppe de pitch |
| **Enveloppe de pitch** | **20–70 ms** | **200–500 ms** |
| Ampli | decay long, effet drone | plus court |

Plus de modulation de pitch et des enveloppes courtes donnent une 909 ; moins et un release long donnent une 808. Profondeur de modulation : 20–40 % d'amount fonctionne bien.

### Le circuit 808, mesuré `[D]`

Analyse du circuit de grosse caisse (Baratatronix, https://www.baratatronix.com/blog/808-bd-synthesis) :

| Grandeur | Valeur |
|---|---|
| Impulsion de déclenchement | **1 ms** (3,5 V, jusqu'à 13,5 V avec accent) |
| Pic de hauteur à l'attaque | **~130 Hz pendant ~6 ms** |
| Résonateur bridged-T | **49,4 Hz** (manuel de service : 56 Hz ; machines réelles 48–56 Hz) |
| Decay réglable | **50 à 800 ms**, 300 ms au centre du potentiomètre |
| Sortie | passe-haut 6,7 Hz (offset DC) + passe-bas passif (potard *Tone*) |

`[I]` Ordre de grandeur à retenir : **click de 1 à 6 ms**, sweep qui part vers 100–150 Hz et retombe en quelques millisecondes, corps de 150 à 500 ms selon le genre. À 126 BPM une noire fait 476 ms : un kick de 250–350 ms laisse respirer la basse, un kick de 800 ms remplit la mesure et interdit un sub actif.

### Saturation et clipping `[D]`

**Écrêtage numérique** = harmoniques impaires fortes **+ repliement (aliasing)**. **Écrêtage analogique** = harmoniques impaires sans aliasing grâce aux filtres anti-repliement. SOS recommande donc un **clipper dédié avec filtrage anti-alias**, et note que le clipping marche surtout sur les sons à **forte composante de bruit et faible information de hauteur** — caisse claire, hats, cymbales, en phase d'attaque.

`[I]` **Sound on Sound est nettement plus prudent que les blogs sur ce point : il n'encourage pas à clipper massivement un kick sinus pur.**

**Drum Buss d'Ableton** `[D]` : `Drive` = quantité ; `Crunch` = distorsion en sinus appliquée **aux médiums-aigus** ; `Boom` = renforcement du grave par filtre résonant ; **`Transients` accentue ou atténue les transitoires des fréquences au-dessus de 100 Hz seulement**. Ce détail explique pourquoi **Drum Buss n'aidera jamais sur le sub d'un kick**.

### Points de départ

1. Sinus 45–50 Hz, pitch env +2 à +3 octaves avec decay 20–40 ms, amp env A 0 / D 250 ms.
2. Couche *click* séparée : bruit ou impulsion passée en passe-haut, decay 5–10 ms, 6 à 12 dB sous le corps.
3. Saturation douce sur une copie parallèle filtrée **au-dessus de 100 Hz**, pour l'audibilité sur petite enceinte sans toucher au sub.

---

## 2. L'accordage du kick 808 — le fond scientifique

**Source primaire** : Emmanuel Deruty, *Harmonic and Transposition Constraints Arising from the Use of the Roland TR-808 Bass Drum*, Sony Computer Science Laboratories Paris et Aalborg University. **ISMIR 2024, p. 78–85.** https://arxiv.org/abs/2502.07524 · DOI 10.5281/zenodo.14877286

### La question posée

En 2007, le producteur Scott Storch recommande **l'inverse de la pratique courante** : au lieu d'accorder la grosse caisse à la tonalité, **transposer tout le morceau — toutes les pistes sauf le kick — pour l'ajuster à la 808**. L'article cherche à expliquer pourquoi cette manœuvre coûteuse serait rationnelle.

### La 808 mesurée `[D]`

| Grandeur | Valeur |
|---|---|
| f₀ médiane, presets non saturés | **49,48 Hz, soit un Sol1** |
| Pic secondaire, presets « short » | 51,05 Hz |
| Presets saturés (« driven ») | f₀ **plus hautes**, non chiffrées |
| Balayage de hauteur initial | amplitude médiane **≈ un demi-ton**, descendante |
| Durée de la phase avec harmoniques | **≈ 0,4 s**, après quoi le sample long se réduit à **une seule sinusoïde grave** |

Repères de sub-basse repris de la littérature : **boom ≈ 30 Hz, thump ≈ 50 Hz, punch ≈ 80 Hz**. La 808 occupe le **thump**.

### Le coût de la descente `[D]`

Cas modélisé : descendre la 808 d'une **quarte juste**, de 49,5 Hz (Sol1) à 37 Hz (Ré1).

| Source de perte | Perte |
|---|---|
| Réponse médiane de **36 moniteurs de proximité** | −6,3 dB |
| Sensibilité de l'oreille à 60 phones (ISO 226-2003) | −5,5 dB |
| **Total sur la fondamentale** | **≈ −11,8 dB** |

**Et le résultat le plus utile** : pour un son **complexe à 5 partiels** (donc une 808 saturée), la même transposition ne coûte que **−4,5 dB**. La perte diminue à chaque harmonique et devient quasi nulle au 5ᵉ. Le problème concerne donc **spécifiquement l'audibilité des partiels les plus bas**.

### Trois conclusions pratiques `[D]`

1. **La tonalité naturelle de la 808 est Sol.** C'est là qu'elle sonne telle qu'elle a été conçue.
2. **La hauteur perçue ne bouge pas quand on perd le fondamental**, par le phénomène de la fondamentale manquante. **Seul le timbre est affecté.** C'est un problème de son, pas de justesse. Et la perte affecte aussi la **sensation corporelle** : le thump est ressenti dans l'estomac, le boom dans le ventre, le punch dans la poitrine.
3. **Seuil énoncé par Storch** : en dessous d'**un mi grave (Mi1 ≈ 41,2 Hz)**, « les enceintes ne vont pas vous laisser monter le niveau ».

Conséquence d'écriture que l'auteur tire explicitement : Storch dit rester « dans la zone de confort de l'enceinte, pour ne pas avoir les volumes qui sautent selon les notes ». Donc **la hauteur des parties de 808 doit rester largement statique, ce qui limite mécaniquement la variété des accords**. « La stabilité de sonie peut prendre le pas sur la complexité harmonique. »

### Ce que ça implique pour les deux projets

`[I]` **L'article ne parle ni de fa mineur ni de la mineur.** Ce qui suit est un calcul, avec les fréquences du tempérament égal à La4 = 440 Hz.

**« el21 », la mineur — situation favorable.** La1 = 55,0 Hz, donc **au-dessus** du Sol1 natif de 2 demi-tons, et nettement au-dessus du seuil de Storch. C'est le sens *montant* de la transposition, celui qui gagne du niveau au lieu d'en perdre. 55 Hz reste dans la région du thump. **Aucun arbitrage à faire.**

**« deep chill minimal house », fa mineur — situation intermédiaire, gérable.** Fa1 = 43,65 Hz, donc 2 demi-tons **sous** le natif, dans le sens coûteux, mais **encore au-dessus du seuil de 41,2 Hz** et très loin du Ré1 qui coûte 11,8 dB. **Fa mineur n'est pas une tonalité à problème au sens de l'article.** L'article ne chiffre pas −2 demi-tons ; la perte est strictement entre 0 et 11,8 dB et bien plus près de 0, la pente s'accentuant en descendant.

Trois options par ordre de préférence :
1. **Donner des harmoniques au kick.** Un peu de saturation et le coût passe du régime −11,8 dB au régime −4,5 dB. Directement actionnable, et cohérent avec la logique de `kick-bass-equilibre` : qui tient le sub, qui tient l'attaque.
2. Monter le morceau en sol mineur. Recommandation littérale de Storch, mais inutile à 43,65 Hz.
3. Ne rien faire. Toute l'argumentation porte sur la 808 **tonale**, qui tient la ligne de basse. Si le kick est court, l'argument s'applique faiblement.

### ⚠ Piège de nomenclature

L'article utilise la **notation scientifique** (Do1 = 32,7 Hz). Ableton est en **Do3 = 60**. Donc :

| Note de l'article | MIDI | Affiché dans le piano roll |
|---|---|---|
| Sol1 (808 native) | 31 | **G0** |
| Fa1 | 29 | **F0** |
| La1 | 33 | **A0** |

**Ne pas se tromper d'octave en reportant ces valeurs.**

### Limites, dont une majeure

L'article **n'a pas de section limitations**. Les réserves ci-dessous sont des observations, sauf une : l'auteur présente lui-même la primauté des formants spectraux sur la hauteur comme **une piste de recherche, pas un résultat établi**.

- **Aucune mesure sur machine réelle.** Tous les samples viennent d'**une seule bibliothèque gratuite**. Aucune TR-808 physique n'a été mesurée, donc **aucune dispersion entre exemplaires** n'est donnée. Le vieillissement des composants, les tolérances et la dérive en température ne sont pas abordés.
- **La plage du potentiomètre Tune n'est jamais mesurée ni mentionnée.** Quand l'abstract parle de « plage de hauteur utilisable limitée », il s'agit d'une contrainte **psychoacoustique et électroacoustique**, pas de la course mécanique du réglage. Pour la course réelle du Tune, il faut chercher ailleurs.
- **Aucun test d'écoute.** Les −11,8 et −4,5 dB sont **modélisés**, jamais validés auprès d'auditeurs.
- Le choix des 60 phones n'est pas justifié, or les courbes isosoniques se redressent fortement selon le niveau.
- La réponse médiane de 36 moniteurs **masque une dispersion importante** : sur des enceintes données, le −6,3 dB peut être sensiblement différent.
- Base empirique de la pratique très mince : un entretien de 2007, plus des échanges informels avec **une seule** société de production.

### ⚠ Tension non résolue dans l'article

La section 5 utilise le **Ré** comme exemple du cas coûteux (−11,8 dB), alors que la section 6 rapporte que les producteurs interrogés choisissent souvent **Ré ou Mi♭**. L'auteur juxtapose les deux sans les articuler.

---

## 3. Boîtes à rythmes historiques `[D]`

| Machine | Année | Génération du son |
|---|---|---|
| **TR-808** | 1980, 1 195 $ | **100 % analogique.** Kick = oscillateur sinus (réseau bridged-T) + passe-bas + VCA. Transistors volontairement défectueux achetés pour obtenir le grésillement caractéristique |
| **TR-909** | 1983, ~10 000 unités, arrêtée après un an | **Hybride** : kick, snare, toms, clap, rimshot analogiques ; **crash, ride, hats en échantillons PCM 6 bits** (~18 kHz), enregistrés sur un vrai kit, sans EQ ni compression |
| **TR-606** | 1981–1984 | Analogique, 7 sons **non éditables**, conçue comme compagne du TB-303 |
| **Linn LM-1** | 1980, 5 000 $, ~500 unités | **Premier usage d'échantillons de vraies batteries**, PCM 8 bits à 28 kHz, 12 sons accordables. **Pas de cymbales** : les échantillons longs coûtaient trop cher. Premier *Timing Correct* et premier *Swing* |

`[I]` **La leçon** : 808 = sub long et tenu, qui **occupe** le grave. 909 = attaque et médium, qui **laisse** le grave à la basse. 606 = petit, sec, bruité, parfait en couche secondaire. LM-1 = grain 8 bits, couleur et non fondation.

---

## 4. Snare et clap

### Snare `[D]`

Physique (SOS) : neuf fréquences issues des sept premiers modes ; les **deux composantes du mode (0,1) autour de 180 Hz et 330 Hz** dominent et **décroissent plus de deux fois plus vite** que les autres partiels, d'où deux enveloppes distinctes. Partie bruit : générateur → passe-bas dont la coupure est contrôlée par la vélocité, plus des filtres coupe-bande pour reproduire les trous spectraux.

Circuit 808 : **deux oscillateurs bridged-T à 180 Hz et 330 Hz**, chacun avec son VCA et son contour, plus une source de bruit contourée. Le potard **Snappy** règle l'amplitude de l'impulsion envoyée aux oscillateurs **et** l'enveloppe du bruit.

Recettes : *808 snare* sinus **160 Hz (Mi2)**, attaque instantanée, decay 250–350 ms ; bruit avec sa propre enveloppe, decay 100–600 ms. *909 snare* triangle 160 Hz, enveloppe de pitch 100–200 ms, « compresser généreusement ».

### Clap — le point essentiel `[D]`

Circuit 808 : bruit blanc → **passe-bande centré à 1 000 Hz**. Une impulsion de 30 ms déclenche une enveloppe en dents de scie qui produit **3 cycles rapides de 10 ms chacun**, suivis d'une décharge finale de **20 ms** — quatre mains successives. **En parallèle**, un second VCA piloté par une enveloppe dite « Reverb » de **100 ms** génère la queue. Les deux chemins sont mixés.

**La réverbe du clap n'est pas un effet ajouté, c'est une seconde enveloppe dans le circuit.** D'où la règle « réverbe courte comme partie du son ».

Implémentation logicielle citée : attaques à **0 / 7,6 / 15,5 / 23,0 ms**.

Recette depuis zéro : bruit blanc, passe-bande 800 Hz – 1,5 kHz avec résonance, decay 450–800 ms. Variante Attack Magazine : passe-haut 12 dB/oct à ~30 Hz résonance ~62, EQ final shelf vers 550 Hz et roll-off à 19 kHz, **delay 1/16 avec feedback ~7 pour doubler les impacts**, compresseur seuil −20 dB.

### Points de départ clap

1. Bruit blanc, passe-bande ~1 kHz, 3 bursts de 10 ms espacés de 10 ms + un dernier de 20 ms, puis queue de 100 ms.
2. Si le sampler ne fait pas de bursts : delay 1/64 ou 1/32 avec 3 répétitions à feedback court, **en série avant** l'enveloppe de queue.
3. Réverbe courte (decay 150–300 ms, pre-delay 0) **imprimée** sur le sample, puis re-shapée à l'enveloppe.

---

## 5. Hi-hats

### Méthode 808 `[D]`

**Six oscillateurs à trigger de Schmitt produisant des carrés désaccordés**, mixés puis passe-bande → passe-haut → enveloppe de volume. Les carrés sont accordés de façon quasi aléatoire, **environ entre 2 000 et 5 000 Hz** ; deux d'entre eux sont réglés en usine à 800 Hz et 540 Hz dans la section cymbale.

### Modèle FM à deux opérateurs `[D]`

SOS *Synthesizing Realistic Cymbals* : modulateur pulse ~**1 kHz**, porteuse carrée ~**2,5 kHz**, FM à amplitude maximale → « des centaines de partiels sur toute la bande ». Puis deux chemins : un passe-bande 24 dB/oct centré ~1 kHz balayé vers le bas en **0,2 s** (le « ping »), et un passe-haut 12 dB/oct à **2,64 kHz** avec enveloppe s'ouvrant en ~200 ms et se refermant en **3,7 s** (la queue). Enveloppe globale : attaque quasi nulle, decay ~0,75 s.

### Durées `[D]`

Bruit blanc, passe-haut 12–24 dB/oct à 2 kHz ou plus. **Hat fermé ≤ 200 ms de decay, hat ouvert ~1 000 ms.** Groupe exclusif pour le choke.

### Choke group — documentation officielle `[D]`

**Ableton** : « Le sélecteur Choke permet d'assigner une chaîne à l'un des **seize groupes de choke**. Toutes les chaînes du même groupe se coupent mutuellement au déclenchement. » Si *All Notes* est choisi dans *Receive*, les sélecteurs *Play* et *Choke* sont désactivés.

**Battery 4** : deux voies documentées par NI — soit le module **Voice Groups** avec *Voices* = 1 pour un groupe contenant hat ouvert et fermé ; soit les **Exclusive groups**, qui permettent d'assigner plusieurs voice groups à un *exclude group*, tout en gardant plus de voix sur le hat ouvert.

### Points de départ

1. Bruit + passe-haut 24 dB/oct à 6–8 kHz, decay 40–80 ms fermé / 400–800 ms ouvert.
2. Version métallique : 4 à 6 carrés entre 2 et 5 kHz, désaccordés **sans relation harmonique**, passe-bande ~1 kHz puis passe-haut ~2,6 kHz.
3. Choke group 1 pour la paire ouvert/fermé, et `[I]` un second choke group pour shaker et hat s'ils jouent le même rôle rythmique.

---

## 6. Percussions

### Synthèse `[D]`

**Cowbell 808** : le manuel de service donne 540 Hz et 800 Hz ; SOS propose 587 et 845 Hz (rapport 1:1,44) ; une autre analyse relève **quatre pulses simultanés à 555, 835, 1370 et 1940 Hz, decay ~600 ms, sans filtrage**.

**Cowbell réaliste** : triangle (plus terne que la pulse), contour en deux temps — impact court de forte amplitude puis queue étendue —, passe-bande résonant 2,64 kHz 12 dB/oct, un peu de bruit rosé **pendant l'impact seulement**, puis un **ring modulator** en fin de chaîne pour le métal.

**Congas et bongos** : « on peut souvent utiliser les mêmes réglages, simplement en jouant le son quelques octaves plus bas ».

**Claves** : un seul triangle, decay encore plus court, passe-bande sans résonance, 1,5–3,5 kHz, decay 150–250 ms. **Pas d'enveloppe de pitch à ces fréquences.**

**Toms** : *808* = sinus une ou deux octaves au-dessus du kick, structure voisine du snare avec un peu de bruit, decay court à moyen. *909* = **deux triangles accordés à la quinte (7 demi-tons)**, enveloppe de pitch 100–200 ms.

**Toms Simmons** : une rampe unique pilotant simultanément pitch, filtre et amplitude, plus une seconde enveloppe de pitch à decay quasi nul pour le click.

### Placement spectral `[D, sources de moindre autorité]`

Shakers : l'essentiel de l'énergie **au-dessus de ~6 kHz**, tout ce qui est sous 100 Hz est du bruit inutile. Tambourin : passe-haut jusqu'à 500 Hz sans dommage. Congas : 100 Hz – 12 kHz, tons ouverts vers 500 Hz – 1 kHz, slap 800 Hz – 10 kHz. Repères de praticiens, pas des mesures normalisées.

### Usage en deep house `[D]`

Attack Magazine, *Beat Dissected — Rolling Deep House* : **125 BPM, swing 60–70**, kick 909 saturé légèrement à la bande ; **le shaker prend le rôle du hat fermé** et doit travailler « sympathiquement » avec lui ; tom 909 sur les divisions 3, 9 et 11 pour renforcer le shuffle ; percussion additionnelle sur 2 et 10, **accordée relativement au tom** ; « sons délibérément courts, pas de chevauchements ».

### Points de départ

1. `[I]` **Un seul élément haut actif à la fois** (hat OU shaker) dans une même bande, sinon ils s'annulent perceptivement.
2. Congas et toms : passe-haut à 120–150 Hz pour libérer le kick, corps entre 150 et 400 Hz, slap au-dessus de 1 kHz.
3. Accorder les percussions tonales sur des degrés de la tonalité, exactement comme le kick.

---

## 7. Layering

### Règles documentées `[D]`

- **Ne superposer que s'il y a une raison.** L'exemple type combine « l'énergie percussive grave de la caisse claire et le bruit qui remplit le spectre du clap ».
- **Phase** : vérification en zoomant sur le début des formes d'onde ; si les deux partent dans le même sens c'est bon, sinon inversion de polarité.
- **EQ bracketing** : couper dans chaque son ce que l'autre apporte. Exemple : 808 layée avec une batterie live → enlever l'aigu du 808 et le grave du live.
- **Transitoires** : aligner, ou décaler volontairement en allongeant l'attaque avec un transient designer.
- Exemple chiffré : clap baissé de **−8 dB** sous la caisse claire, transposition de **−1 demi-ton** pour la cohésion.

### Le chiffre qui compte `[D]`

**« À 100 Hz, 5 ms représentent une demi-longueur d'onde — annulation complète. »**

Procédure : superposer les formes d'onde, tester l'inversion de polarité, garder la version qui a le plus de grave, puis **déplacer une couche par pas de 0,1 à 1 ms** jusqu'à maximiser le grave. Viser une **corrélation proche de +1 dans la bande 30–80 Hz**. Les problèmes de phase sont les pires **sous 200 Hz** et s'entendent surtout **en mono**. Un kick hardstyle typique fait 3 à 5 couches.

**Test de diagnostic** : insérer un corrélamètre, écouter en mono, comparer le bus avec chaque couche coupée tour à tour. **Si le kick devient plus fort quand on enlève une couche, cette couche annule de l'énergie utile.**

`[I]` C'est exactement ce que fait le script `kick_bass_check.py`, qui mesure la corrélation de Pearson entre 30 et 120 Hz. La bande recommandée ici est un peu plus resserrée.

### Points de départ

1. **Deux couches maximum** sur le kick : attaque (passe-haut ~150 Hz) + corps/sub (passe-bas ~150 Hz), même point de départ à l'échantillon près.
2. Vérifier la polarité puis nudger ±0,1–1 ms en regardant un analyseur sur 40–80 Hz.
3. Clap + snare : clap −6 à −8 dB, décalé de 5–15 ms pour l'effet foule, aligné pour un seul impact.

---

## 8. Transitoires et punch

### Le punch, mesurablement `[D]`

Le **facteur de crête** = différence en dB entre crête et niveau moyen, soit 20·log10(peak/RMS).

| Signal | Facteur de crête |
|---|---|
| Batterie non traitée | **16–18 dB** |
| Master bien équilibré | **8–12 dB** |
| Pop et EDM contemporaines | parfois **3–5 dB** |

Une compression rapide en attaque et release réduit le facteur de crête ; des temps plus longs le préservent. **Sous 9–10 dB sur un master, on est généralement en surcompression.**

`[I]` **C'est la métrique à suivre**, mesurable avec Insight ou SPAN, donc utilisable sans écoute. Mesurer le facteur de crête du bus batterie avant et après chaque traitement. Gagner en volume perçu en perdant 4 dB de crête, c'est échanger le punch contre de la sonie.

### Transient shapers `[D]`

SOS *Using Transient Processors* :
- ils fonctionnent par **suiveurs d'enveloppe détectant la vitesse de variation du niveau**, pas par seuil : « la vitesse de variation étant indépendante du niveau absolu, les transitoires sont traités de la même façon qu'ils soient forts ou faibles ». **C'est la différence de fond avec un compresseur.**
- *Attack* suffit dans « au moins la moitié » des usages ;
- réglages d'enveloppe rapides = pointe d'attaque plus acérée, **lents = meilleure sensation de poids dans le grave** ;
- **avertissements** : remonter l'attaque augmente les crêtes et peut faire écrêter en aval ; les transient shapers standards **ne savent pas accentuer sélectivement les transitoires graves** — pour un kick maigre il faut du parallèle avec EQ ou du multibande ;
- pour renforcer le *sustain*, SOS préfère explicitement la **compression parallèle**, « musicalement plus appropriée ».

### Compression `[D]`

SOS *Drum Compression* :
- attaque rapide = transitoire écrasé, sustain mis en avant ; attaque lente = transitoire préservé ;
- homogénéiser : **ratio 5:1, 4–5 dB de réduction**, attaque rapide, release moyen ;
- pompage et énergie : **ratio 8:1**, réduction franche, attaque et release rapides ;
- principe structurant : **empiler plusieurs étages de 3–4 dB** plutôt qu'une grosse réduction unique ;
- « la compression parallèle est souvent inutile si l'on a d'abord compressé les pistes individuelles de façon ciblée ».

`[⚠]` Le chiffre « Attack +14 / Sustain −12 mélangé à 25–35 % » circule sur des blogs SEO. **Aucune source de référence ne le corrobore.** À traiter comme un point de départ arbitraire.

### Points de départ

1. Mesurer le facteur de crête du bus batterie ; cible **12–16 dB avant le master**.
2. Transient shaper : *Attack* seul, +2 à +4 dB, enveloppe **lente sur le kick** (poids) et **rapide sur le clap** (claquement).
3. Parallèle : copie du bus, 8:1, attaque 10–30 ms, 6–10 dB de réduction, remontée jusqu'à ce que le facteur de crête baisse de **2 dB maximum**.

---

## 9. EQ, grave, mono

### Bandes de référence `[D]`

iZotope : sub 20–60 Hz · corps 60–200 Hz · boue 200–400 Hz · présence 700 Hz – 2 kHz · **zone de conflit kick/basse 50–100 Hz**. Courbe type : creuser 200–300 Hz, remonter en cloche 750 Hz – 2 kHz.

Pour le conflit kick/basse : **EQ dynamique en sidechain** déclenchée par le kick, la basse ne baissant que dans la bande problématique. Et avant d'ajouter du grave à l'EQ, essayer la **distorsion harmonique**, qui crée les harmoniques sans « tubbiness ».

### Mono dans le grave `[D]`

Origine technique : l'**égaliseur elliptique** somme le grave en mono pour éviter les modulations verticales excessives du sillon vinyle. Ces appareils vont de 20 à 700 Hz, et **régler à 100 Hz est déjà jugé excessif par beaucoup de graveurs**.

Pratique courante : tout **sous ~100 Hz en mono**, élargir librement au-dessus de 100–150 Hz. Image « en rose » : étroite en bas, de plus en plus large vers l'aigu.

**Ableton** : le device **Utility a un bouton Bass Mono avec fréquence de crossover réglable**, depuis Live 10.

`[I]` Utility en fin de chaîne du bus batterie ou du Main, Bass Mono à **120 Hz**. 100 Hz est le réglage sûr universel, 150 Hz plus conservateur et adapté au club, où le grave est de toute façon diffusé par des caissons mono.

### Ordre de chaîne `[I]`

EQ correctif (passe-haut, coupes) → saturation ou clipping → transient shaper → compression → EQ de couleur → mono bass.

Placer le clipper **après** l'EQ correctif, sinon on écrête de l'énergie qu'on va enlever, et **avant** la compression parallèle, pour que les deux chemins partent du même signal.

---

## 10. Ce qui est solide et ce qui ne l'est pas

**Solidement documenté** : les circuits Roland (valeurs, fréquences, temps de decay) ; les spécifications des machines historiques ; le fonctionnement des transient shapers ; les valeurs de facteur de crête ; le manuel Ableton (16 choke groups, Drum Buss Transients au-dessus de 100 Hz) ; le choke dans Battery 4 ; l'article ISMIR sur l'accordage.

**Convention de métier sans mesure formelle** : l'accord du kick à la tonalité (±3 demi-tons, intervalles parfaits), le mono sous 100–150 Hz (l'origine vinyle est documentée, la généralisation au numérique ne l'est pas), les réglages types de compression parallèle.

**À ignorer comme référence** : les chiffres précis de transient shaping qui circulent sur les blogs SEO, les articles « quick tip » sur le clipping qui ne donnent aucune valeur.

**Introuvable** : l'article SOS *Practical Percussion Synthesis* renvoie un HTTP 410, il a été retiré.
