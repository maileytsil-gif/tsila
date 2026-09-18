# Patchs chiffrés par genre — bass house et future house

Recherche du 18 septembre 2026, 14 requêtes et une trentaine de pages ouvertes. Fiabilité : **[A]** constructeur · **[B]** magazine ou école · **[C]** blog de vendeur · **[D]** forum ou wiki · `[I]` interprétation.

---

# 0. Le constat à lire en premier

**Il n'existe pas, sur le web écrit, de patch Serum complet et chiffré pour le lead future house.** Recherche menée sous huit angles. Ce qui existe :

- des **vidéos** sans transcription exploitable ;
- des pages de blogs qui ne sont qu'**une coquille de navigation autour d'une vidéo**, vérifié en rendu JavaScript complet : la page « Deep House Organ Bass In Serum » d'ADSR ne contient **aucune valeur** ;
- des **fils de forum vides** : les deux threads KVR sur le lead future house sont des annonces de vidéo, le seul contenu technique étant une phrase d'admiration ;
- une page annoncée sur les leads de Don Diablo et Sikdope qui renvoie un **404**.

**En revanche, l'ancêtre documenté et entièrement chiffré de ce son existe.** C'est sur lui qu'il faut construire.

---

# 1. Ce que les genres sont, avec chiffres

## Future house

`[D]` **Wikipédia** : tempo le plus courant **126 et 128 BPM**, plage 120 à 130. Description du son : « une mélodie étouffée avec un **drop métallique et élastique, et des lignes de basse modulées en fréquence** ». Filiation : **deep house et UK garage**, Royaume-Uni, années 2010.

`[C]` **Blog Native Instruments** : tempo **126 BPM**, tonalité **mi mineur**, progression i–v–VI–VII. Basse en **deux couches**, un patch aigu plus un sub séparé, avec **coupe-bas sur la couche du haut**. Aucune valeur de synthèse donnée : c'est un tutoriel « charge ce preset ».

## Bass house

| Source | Tempo | Tonalité |
|---|---|---|
| EDMProd `[C]` | **128 BPM**, certains jusqu'à 130 | **mi phrygien**, structure par blocs de 8 mesures |
| Preset Drive `[C]` | 125 à 130, extrêmes 120 à 135, cœur **128** | non documentée |
| Attack Magazine `[B]` | **123 à 128 BPM**, **swing 55 à 65 %** | non documentée |

**Aucune source ne documente une tonalité usuelle** pour l'un ou l'autre genre. Les deux seuls exemples chiffrés donnent mi mineur et mi phrygien. **La mineur et fa mineur ne sont contredits par rien.**

---

# 2. L'ancêtre du lead future house, entièrement chiffré

`[C]` **ADSR** écrit la filiation en toutes lettres : la basse future et deep house moderne est « une version moderne d'un son plus ancien de l'UK garage appelé **hollow bass**, créé à l'origine avec **deux ondes sinus et de la synthèse FM** », et « utiliser une onde carrée dans un oscillateur donne ce son creux ».

`[B]` Et **Attack Magazine en donne la version complète**, dans *Synth Secrets: Garage Bass* sur NI Massive :

| Élément | Valeur exacte |
|---|---|
| Osc 1 | wavetable **Sin-Squ**, position **complètement à gauche** donc sinus pur, Pitch **−24,00** |
| Osc 2 | **Sin-Squ**, position à gauche, Pitch **−12,00**, Amp ~2 h |
| Oscillateur de modulation | mode **Phase Modulation** appliqué à Osc 1, Pitch **−12,00** · **variante désaccordée −12,30** |
| Niveau de modulation de phase | juste avant la mi-course, plus **~60 %** de modulation par enveloppe |
| Filtre | **Daft**, Cutoff **~25 %**, **Résonance 0** |
| Enveloppe de filtre | attaque rapide, decay moyen-rapide, **sustain 0**, release court, modulation du cutoff **au maximum** |
| Enveloppe d'ampli | Release **~33 %** |
| Voicing | **mono**, Glide **10 à 15 %**, **Restart via Gate** activé |
| FX 1 | **Classic Tube**, Dry/Wet et Drive tous deux ~10 h |
| FX 2 | **Dimension Expander**, Size 0, Dry/Wet ~10 h |

## Lecture du ratio, et d'où vient le métallique

Porteuse à −24, modulateur à −12 : le modulateur est **une octave au-dessus**, donc un **ratio 2:1 harmonique**. C'est ce qui donne le creux façon carré ou orgue, **pas une cloche**.

**Le métallique apparaît avec la variante −12,30** : le modulateur désaccordé de 30 centièmes de demi-ton rend le spectre légèrement inharmonique et battant. **Ce sont les deux seuls chiffres publiés qui expliquent réellement le métallique du genre.**

## Pour un vrai timbre de cloche

`[C]` Plugin Boutique : porteuse sinus, modulateur en **ratio non entier d'au moins 4 ou 5**. Et le mécanisme : une enveloppe à décroissance rapide **sur le modulateur seul** fait s'effondrer le spectre inharmonique vers la porteuse pure.

**Aucune source ne donne l'index de modulation.** C'est le paramètre à trouver à l'oreille.

## Transposition dans Serum 2 `[I]`

La basse creuse se fait aujourd'hui **dans un seul oscillateur** : warp **FM** sur OSC A avec OSC B comme modulateur, au lieu de l'oscillateur de modulation de Massive. Et le **dual warp** de Serum 2 permet FM **et** distorsion sur la même wavetable, ce qui n'existait pas en Serum 1.

Pour le lead : **monter le patch d'une ou deux octaves**. C'est littéralement ce que le genre a fait historiquement.

---

# 3. Le seul patch Serum chiffré publié par Attack Magazine

*Modulating Serum's FX: Beat-Pulsing Plucks* `[B]`

| | |
|---|---|
| OSC A | **Dist 8Bit Fwap** (dossier Digital), Unison **4**, Detune **0,10** |
| OSC B | **CrushWub** (Digital), Unison **3**, Detune **0,16** |
| Filtre | activé sur A et B, **cutoff, résonance et type non chiffrés** |
| **LFO 1 → Cutoff** | Rate **1/8**, Smooth **50**, **TRIP activé** donc triolets, forme dessinée à la main |
| LFO 2 → position de wavetable de A et B | Rate **1/2** |
| LFO 3 → Level de A et B (sidechain) | Smooth 50, Level ~26 %, Modulation 100, **rate non donné** |
| Env 2 | pilote le **Wet de la reverb**, ADSR non chiffrées |
| FX | Reverb avec coupe-bas sur la reverb, puis EQ, **fréquences non données** |

`[I]` **C'est la meilleure base Serum documentée pour un pluck house rythmique.** Le LFO 1 en **1/8 triolet** sur le cutoff est exactement le mouvement qui fait le bounce future house. À 126 BPM, un 1/8 triolet vaut **159 ms**, cohérent avec un swing de 55 à 62 %.

---

# 4. Trois autres patchs chiffrés, transposables

## Warping Bass (Massive) `[B]`

Osc 1 **Screamer** position ~75 %, Amp 50 %, mode **Bend−/+** · Osc 2 **Squ-Sw1** position 0 %, Pitch **−24,00** · Osc 3 **Sinarmonic I** position ~60 %, Pitch −24,00 · Filtre 1 **Daft** Cutoff ~25 % Res ~25 %, **routage série** · Filtre 2 **Comb** Pitch ~30 % · **LFO 5 → cutoff du filtre 1**, quantité un quart de course, **Sync activé, ratio 3/16** · Mono, **Glide ~30 %**, Restart via Gate · FX 1 Dimension Expander 50 %, FX 2 Small Reverb ~30 % · Post : coupe-bas et **distorsion multibande sur les médiums et aigus seulement**.

`[I]` **Le LFO synchronisé en 3/16 sur le cutoff est directement réutilisable en bass house** : c'est le mouvement qui crée un déphasage rythmique contre un kick en 4/4.

## Wavetable Bassline « ANNA » (Ableton Wavetable) `[B]`

**132 BPM.** Mono, **Glide 25 ms** · Unison **Classic, 2 voix, 3 %** · Osc 1 **Vintage > Logue Saw**, Semi −12, position **57 %** · Osc 2 position **67 %**, Semi −12, Detune **−2 cents** · Sub Gain **−7,5 dB**, Tone **85 %**, octave −1 · Passe-bas **MS2** Cutoff **8,90 kHz** (ramené à 20 Hz au réglage de l'enveloppe), Res 0 % automatisée à 100 % sur les mesures 4 à 8, pente **24 dB**, Drive **6,40 dB** · Passe-haut **PRD** Cutoff **40 Hz**, Res 30 %, Drive 2 dB · **Env 3 → passe-bas** : A **0,18 ms**, D **4 s**, S **40 %**, R **600 ms**, quantité 100 · Boucle de 8 mesures.

`[I]` **C'est le seul patch entièrement chiffré, dans un instrument natif de Live, à un tempo proche.**

## Baddadan Synth Bass (Zebra 2) `[B]`

**174 BPM.** Empilement **0 / +7 / +19 demi-tons** (fondamentale, quinte, quinte à l'octave supérieure), FM pilotée par une enveloppe, filtre LP Vintage, **EQ : coupe 225 Hz, boost 3 kHz**.

`[I]` **L'empilement 0 / +7 / +19 est un truc de largeur harmonique transposable tel quel**, et il ne dépend pas du tempo.

---

# 5. Ce qui distingue une basse bass house d'une basse dubstep

**La réponse est rythmique et spectrale, pas timbrale.**

1. **Le kick reste en 4/4 et ne bouge pas.** `[C]` Preset Drive : le tempo bass house est « la poche où les patterns de kick sur les quatre temps restent verrouillés, tout en permettant de superposer des rythmes de basse en demi-temps issus de l'esthétique dubstep à 140 BPM ». En dubstep la batterie est clairsemée et la basse a tout l'espace. **En bass house, la basse doit cohabiter avec un kick sur tous les temps.**

2. **Le kick bass house est volontairement moins grave.** `[C]` EDMProd, textuellement : le kick doit être « punchy, **mais moins qu'un kick tech house** » et « doit pouvoir **s'écarter du chemin de la basse, donc pas trop de grave** ».

3. **Répartition chiffrée** `[C]` : kick concentré **50 à 80 Hz** plutôt que sous 40 Hz, clic de présence **3 à 5 kHz** · basse coupe-bas **30 à 40 Hz**, nettoyage de boue **200 à 300 Hz** · **growl coupé-bas vers 100 Hz**.

4. **Le growl bass house est donc un mid-bass**, pas un son pleine bande. Il faut un **sub sinus mono séparé** en dessous, en mono sous 120 Hz.

## ⚠ Contradiction non résolue

Preset Drive place le poids du kick à **50 à 80 Hz** et coupe la basse à 30 à 40 Hz, donc la basse garde le sub. EDMProd dit de faire un kick **avec peu de grave** pour laisser la place à la basse. **Directement contradictoire.** Icon Collective ne tranche pas non plus.

`[I]` Les deux ne sont conciliables qu'en **décidant explicitement qui tient le fondamental**, ce qui renvoie à la fiche sur les basses.

---

# 6. OTT — ce qui est réellement documenté

`[B]` **Ce n'est pas « OTT » dans Serum** : c'est le **Compressor avec le bouton Multiband**, qui active « une compression ascendante et descendante combinée sur trois bandes ».

Dans le plug-in autonome : **Depth, Time, In Gain, Out Gain**, trois bandes, plus deux boutons Upward et Downward. **Depth est un dry/wet.** **Time règle les attaques et relâchements de toutes les bandes simultanément.**

**⚠ Aucune source, y compris Production Expert, ne publie les fréquences de coupure entre bandes.** Production Expert dit explicitement ne pas les publier.

Valeurs recommandées, `[C]` **fiabilité faible, seul chiffrage existant** : **15 à 20 % de Depth** pour un travail subtil · **20 à 50 %** pour un son agressif · « je dépasse rarement 50 % ».

`[I]` Pour une basse bass house qui doit laisser passer un kick en 4/4, la fourchette basse, **15 à 25 %**, est cohérente avec le fait que le growl est coupé à 100 Hz et ne porte pas le grave.

---

# 7. Transposition à 120 et 126 BPM

## Ce qui ne bouge jamais

Hauteurs d'oscillateurs, demi-tons, **ratios FM**, unison et detune, cutoff, résonance, pente de filtre, drive, fréquences d'EQ, Depth d'OTT, largeur stéréo. **Aucun de ces réglages n'a besoin d'être ajusté.**

## Ce qui se transpose tout seul

**Toute division synchronisée au tempo** : LFO en 1/8, 1/2, 3/16, TRIP ; release de sidechain en 1/8 ou 1/16 ; delays en mode Sync. Seul le *feel* change, pas le réglage.

## Ce qu'il faut recalculer : tout ce qui est en millisecondes

| Division | 120 BPM | **126 BPM** | 140 BPM |
|---|---|---|---|
| 1 mesure | 2000 ms | **1905 ms** | 1714 ms |
| 1/4 | 500 ms | **476 ms** | 429 ms |
| 1/8 pointée | 375 ms | **357 ms** | 321 ms |
| 1/8 | 250 ms | **238 ms** | 214 ms |
| 1/8 triolet | 167 ms | **159 ms** | 143 ms |
| 1/16 | 125 ms | **119 ms** | 107 ms |
| 1/16 triolet | 83 ms | **79 ms** | 71 ms |
| 1/32 | 62,5 ms | **59,5 ms** | 53,6 ms |

**Facteurs de conversion pour les valeurs en millisecondes** (decay rythmique, glide, pre-delay, temps de reverb) :

| Tempo d'origine | → 126 BPM | → 120 BPM |
|---|---|---|
| 128 | **×1,016**, négligeable | **×1,067** |
| 132 | ×1,048 | ×1,100 |
| 140 | **×1,111** | **×1,167** |
| 174 | ×1,381 | ×1,450 |

## Cas particuliers

**Garage Bass** : rien de chiffré n'est en millisecondes, donc transposable sans réserve. `[I]` À 126 BPM, caler le decay de l'enveloppe de filtre sur **119 ms (1/16)** pour un son staccato, **238 ms (1/8)** pour le bounce future house.

**ANNA, 132 BPM** : glide 25 ms reste 25. Decay 4 s devient **4,2 s**, release 600 ms devient **629 ms**. Cutoff, résonance, drive et passe-haut **inchangés**.

**808 Bass d'Attack** : portamento **300 ms** sans tempo de référence, donc intransposable proprement. À 126 BPM, 300 ms vaut 1,26 croche, ni un 1/8 ni un 1/4. `[I]` Pour un glide musical, viser **238 ms** ou **119 ms**.

**Sidechain** : release en 1/8 ou 1/16 donne **238 ou 119 ms à 126 BPM**, **250 ou 125 ms à 120 BPM**. Ratio 3:1 inchangé.

**Swing** : indépendant du tempo, mais **il s'entend davantage quand le tempo baisse**. À 120 BPM, viser le bas des fourchettes, 55 à 58 %.

---

# 8. Attack Magazine — inventaire honnête

**⚠ *Beat Dissected* n'est pas ce qu'on croit** : c'est **exclusivement de la programmation de batterie**, « une série où nous déconstruisons des patterns de batterie ». **Aucun patch de synthé.** Et **aucun épisode bass house ni future house** : les épisodes house existants sont Big House, Minimal House, et six variantes de tech house.

**Aucun article bass house ni future house** dans *Synth Secrets* non plus. Recherche restreinte au domaine : zéro résultat.

**Un seul article Serum** dans toute la série. Tous les autres portent sur Massive, u-he, ou Ableton Wavetable.

**Qualité inégale du chiffrage** `[I]` : quand c'est un synthé à boutons physiques, Juno ou Repro, ils écrivent « un tiers de course ». Quand c'est un synthé logiciel à afficheur, Massive, Wavetable ou Zebra, ils écrivent les vrais nombres. **Les trois patchs à récupérer sont Garage Bass, Warping Bass et ANNA.**

---

# 9. Contradictions à retenir

1. **Unité du detune.** Attack et Monosounds donnent l'échelle propre de Serum (0,07 à 0,16). Preset Drive, Monosounds ailleurs et Evosounds parlent en **cents** (15 à 30). **Ce ne sont pas les mêmes unités et on ne peut pas taper « 20 cents » dans le bouton Detune de Serum.** Les seules valeurs issues d'un patch Serum publié avec capture sont **0,10 et 0,16**.
2. **Nombre de voix d'unison** : « 2 à 4 » · « 4 à 5 » · « 4 et 3 » · « le detune ne marche vraiment qu'à **2 voix, detune au maximum** ». **Quatre positions incompatibles, aucune mesurée.**
3. **Qui tient le grave en bass house** : voir la section 5, contradiction directe non tranchée.
4. **OTT** : aucune source ne publie les crossovers. Les seuls chiffres de Depth viennent d'un blog de samples.
5. **Tempo bass house** : trois fourchettes différentes, aucune mesure, ce sont des opinions d'auteurs. **126 BPM est dans toutes.**
6. **Tonalité** : aucune source ne documente une tonalité usuelle.

---

# 10. Comment combler le trou du lead future house

Par ordre d'efficacité `[I]` :

1. **Partir de Garage Bass et le monter d'une ou deux octaves.** Ratio FM **2:1**, modulateur désaccordé à **−12,30** pour le métallique, filtre à 25 % piloté à fond par une enveloppe à sustain 0, mono plus glide. Dans Serum 2 : warp FM sur OSC A avec OSC B comme modulateur.
2. **Pour un vrai timbre de cloche** : ratio **non entier ≥ 4 ou 5**, avec enveloppe rapide **sur le modulateur seul**. L'index est à trouver à l'oreille, aucune source ne le donne.
3. **Analyser une référence audio.** Compte tenu de l'état du web écrit sur ce sujet, c'est la seule manière d'obtenir des chiffres fiables, et l'outillage existe déjà dans le skill `synthese-reference`.
