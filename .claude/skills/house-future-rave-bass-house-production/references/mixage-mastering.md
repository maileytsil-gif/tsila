# Mixage et mastering — future rave, bass house, house de festival et de club

Cibles, grave, spectre, bus et master, avec les outils de ce Mac. Recherche du 24 septembre 2026 (rapport : `../../../../corpus/house-future-rave/recherche-house-axe5-mix-mastering.md`). Étiquettes : `[DOC]` manuel constructeur ou document lu en entier ; `[COMM]` fiche communautaire lue en entier (JefroB, bitwize, Music Production Wiki) : conventions **déclarées**, pas des mesures de masters ; `[DOC-EXTRAIT]` résumé de page bloquée ; `[CALC]` arithmétique ; `[HEUR]` pratique sans source ; `[TEST]` à mesurer dans le Set.

Ce qui est déjà dans le dépôt et n'est pas répété : outils par tâche et diagnostics `../../mixage/references/outils.md`, `../../mixage/references/diagnostics.md` ; rôles sub/kick, accord, corrélation `../../kick-bass-equilibre/references/roles.md` ; phases, mesures, chaîne en place `../../live-mix-mastering/SKILL.md`, `../../mastering-outils/SKILL.md` ; chaîne éprouvée sur le projet « deep chill minimal house » `../../effets-plugins/references/chaine-actuelle.md`.

**Constat de départ** : aucune source accessible ne publie de mesures de masters commerciaux de ces genres (LUFS, PLR, short-term drop contre breakdown). Tout ce qui suit est une cible déclarée ; les chiffres du genre viennent des mesures locales du § 1.4.

---

## 1. Cibles de sonie

### 1.1 Plateformes (2026) `[DOC-EXTRAIT]`

| Destination | Intégré | True peak | Remarque |
|---|---|---|---|
| Spotify, YouTube, Tidal, Amazon, SoundCloud | −14 LUFS | −1 dBTP (Amazon −2) | YouTube ne fait que baisser |
| Apple Music | −16 LUFS | −1 dBTP | |
| Deezer | −15 LUFS | −1 dBTP | |
| **Beatport, Bandcamp, club, DJ** | **aucune normalisation** | | c'est la destination qui justifie les masters forts |

### 1.2 Ce que visent les pros pour le club et le festival

| Source | Cible | |
|---|---|---|
| EDMProd | −6 LUFS short-term ; −8 ST si on veut −2 dBTP ; ceiling −1,0 dBTP | `[DOC-EXTRAIT]` |
| iZotope | EDM ≈ −7,5 LUFS intégrés ; ceiling −1, ou −0,6/−0,8 avant conversion mp3/aac | `[DOC-EXTRAIT]` |
| Mastering The Mix | club EDM −9 à −7 intégrés ; « la sonie se décide dans le mix, pas au limiteur » | `[DOC-EXTRAIT]` |
| Ian Shepherd | **jamais au-delà de −10 LUFS short-term**, TP ≤ −1 ; EDM à −10 ST tout du long donne −10/−11 intégrés | `[DOC-EXTRAIT]` |
| Masters Beatport observés | ≈ −8 intégrés, parfois plus | `[DOC-EXTRAIT]` |
| Music Production Wiki, ligne House | −10 à −9 ; vérifier le kick en mono | `[COMM]` |
| JefroB par genre | tech house −8/−9 ; bass house −7/−9 (4–6 dB de réduction sur le bus basse) ; electro/big room −6/−8, « clipping avant limiting » ; peak-time techno −7/−9 ; streaming −14 partout | `[COMM]` |

**Contradiction assumée** : −6 ST (EDMProd) contre −10 ST maximum (Shepherd), quatre unités d'écart pour deux destinations. **Décision du skill : deux masters.**

| Master | Intégré | TP | PLR `[CALC]` | Pour |
|---|---|---|---|---|
| **Club / Beatport** | −8 à −7 (big room et future rave jusqu'à −6,5) | −1,0 | 6–7 dB | DJ, festival, promo |
| **Streaming** | −10 à −11 (ou plus dynamique) | −1,0 (−2 si Amazon ou YouTube l'exigent) | 9–10 dB | plateformes normalisées : rien à gagner au-delà, tout à perdre en transitoires |

### 1.3 Dynamique dans le titre

- Crest 12–14 LU = master dynamique, < 6 LU = brickwall ; LRA de la musique commerciale 4–9 LU, < 4 = plat ; « si le LUFS demandé exige plus de 4–5 dB de réduction au limiteur, c'est le mix qu'il faut remonter » `[COMM]`.
- Un master club à −7 avec TP −1 signifie que clipper et limiteur portent 4–8 dB sur le drop `[CALC]` : d'où le clipping du § 4.3.
- Proposition de départ pour un master club à −8 intégrés `[HEUR]` : drop −7/−6 ST, breakdown −12/−14 ST (écart 5–7 LU), LRA 4–7 LU. En streaming, un breakdown trop faible se fait avaler par la normalisation : contraste voulu mais borné.

### 1.4 Mesurer soi-même `[TEST]`

Insight 2 en bout de Main et WLM Plus en mesure seule ; hors Live, `pip install pyloudnorm` ou ffmpeg `ebur128=peak=true` (docs dans `../../../../corpus/house-future-rave/pyloudnorm-readme.md` et `ffmpeg-filters-loudnorm-ebur128.md`). Protocole : six à dix références WAV Beatport par genre → intégré, TP, LRA, ST max (drop), ST min hors intro (breakdown), PLR = TP − I ; consigner le tableau dans la mémoire du projet ; recontrôler sur le fichier exporté, jamais sur le vu-mètre.

---

## 2. Le grave

### 2.1 Qui tient quoi

| Genre | Kick | Sub et basse | Fondamentale tenue par |
|---|---|---|---|
| Tech house | sub 50–70 Hz, corps 100, clic 3–5 kHz, HPF 30 ; « pas assez de clic » est l'erreur classique | basse 60–200 Hz, saturation, sidechain rapide, mono, coupe 200–300 | le kick (sub court) et la basse au-dessus ; ou le sub tenu si la basse est un sinus (`roles.md`) `[COMM]` |
| Bass house | couper 80–100 Hz **seulement** si conflit avec le sub ; clic 2–6 kHz | **trois couches** : sub HPF 25 / LPF 80 ; mid « wobble » HPF 80, 100–500 Hz ; top HPF 300 ; toutes sidechainées ; mono < 150 ; 4–6 dB de réduction sur le bus basse | le **sub**, couche dédiée `[COMM]` |
| Big room | centré 50–60 Hz, court, transitoire en couche, clipping doux ; **accordé à la tonique ou à la quinte** ; queue 200–350 ms | sub sinus ≈ 50 Hz, < 100 ms, en renfort ; « sidechain everything » | le **kick** `[COMM, DOC-EXTRAIT]` |
| Future rave (par voisinage techno peak-time et trance) | sinus 50–60 + punch saturé 100–200 + clic 3–5 kHz ; enveloppe de pitch de 200 Hz vers la fondamentale en moins de 20 ms ; boost 50–60 et 3–4 kHz, creux 200–400 ; tout le reste HPF 80–120 | reese ou rolling bass 200 Hz–4 kHz au-dessus du kick, saturation parallèle, sidechain ; sub séparé mono | le **kick** `[COMM]` |
| Future house | 40–80 Hz | basse FM métallique au-dessus, sub sinus séparé `[HEUR]` | le sub |

Règle nouvelle par rapport au dépôt : **big room et future rave = kick porteur** avec sub court de renfort ; la deep et la tech house gardent le sub tenu. Vérifier la queue du kick contre la remontée du sidechain : un demi-temps vaut 234 ms à 128 BPM `[CALC]`.

### 2.2 Sidechain, valeurs de départ `[COMM Music Production Wiki]`

| Paramètre | Kick → basse | Bus |
|---|---|---|
| Seuil | −18 à −10 dBFS sous la crête du déclencheur | −30 à −20 |
| Attaque | **1–5 ms** (pompage audible 0,1–1 ms ; transparent 5–20) | 10–30 ms |
| Release | **50–150 ms** ; jamais plus que l'intervalle entre kicks : 469 ms par noire à 128 BPM, 234 par croche `[CALC]` | 100–400 |
| Ratio | 4:1 à 10:1 | 2:1 à 4:1 |
| HPF de détection | 80–100 Hz | 100–140 Hz |
| Réduction | 4–12 dB ; « invisible » 2–4 dB | 1–4 dB |

Par genre : deep house 2–3 dB ; tech house rapide et court ; bass house et big room « tight ducking » sur toutes les couches ; french touch 8–12 dB sur tout ; future rave et big room, leads et nappes pompés audiblement, 6–10 dB `[HEUR]`. Kick fantôme (clip muet routé vers le sidechain) pour garder le pump pendant les fills. Lier L/R sur un déclencheur mono. **Jamais de sidechain sur un bus déjà compressé ni sur le master.** Outils absents de ce Mac (LFO Tool, Kickstart, ShaperBox) : équivalent = Compressor natif déjà toléré, bx_glue avec Ext + HPF, API-2500 S/C, Pro-C 3 ; courbe dessinée = automation de gain Utility (`../../live-automation/SKILL.md`), creux −6 à −12 dB, retour en 60–70 % du temps `[HEUR]`.

### 2.3 Mono, saturation, couches de kick

- Mono sous **120 Hz** (house, réglage bx_glue Mono Maker du dépôt), **150 Hz** en bass house, 200 Hz est la valeur haute contradictoire des sources ; les subs des clubs sont sommés mono de toute façon `[DOC-EXTRAIT]`.
- Saturation du grave : soft clip 5–15 % de drive donne du 100–800 Hz audible sur petites enceintes ; **J37 à 7,5 ips** pour le matériel grave, entrée = quantité de saturation, formule 888 la plus sale, 815 la plus plate `[DOC manuel J37]` ; bx_glue XL. En bass house on ne sature **pas** le sinus sub, la distorsion vit sur la couche mid.
- Couches de kick : sinus 50–60 + punch 100–200 saturé + clic 3–5 kHz (techno) ; big room : kick court + transitoire 2–4 kHz + sub ≈ 50 Hz < 100 ms ; deuxième couche = transitoire seul.

---

## 3. Spectre et densité

### 3.1 Carte fréquentielle du drop `[COMM, DOC iZotope EQ cheat sheet]`

| Élément | Bande utile | Coupe | Boost | Image |
|---|---|---|---|---|
| Kick | sub 50–60 (future rave, big room) ou 50–70 (tech house) ; corps 80–120 ; clic 3–5 kHz | HPF 30 ; 200–400 (carton) ; 80–100 si conflit sub (bass house) | 50–60 ; 3–5 kHz | mono |
| Sub | 25–80 | HPF 25–30, LPF 80–100 | | mono |
| Basse mid / wobble / reese | 80–500 (bass house), 200 Hz–4 kHz (rolling techno), 60–250 (funky) | HPF 80–100 ; 200–300 (boue) | 100–200 | mono sous 120–150, large au-dessus |
| Lead supersaw | 200 Hz–5 kHz, dominant 500 Hz–2 kHz | HPF 150–200 ; **200–400** ; dip 2 kHz sur les nappes | 500 Hz–2 kHz ; 2–4 kHz | corps centré + couche large ; trop large s'effondre en mono |
| Stabs, accords | 300 Hz–1 kHz, présence 1–4 kHz | 200–300 | 2–4 kHz | étroit |
| Nappes | 200–500, air 2–8 kHz | scoop 200–400 ; HPF 150–200 | 8–12 kHz | large |
| Vocal chops | 500 Hz–2 kHz, présence 2–5 kHz | HPF 200 ; notch 500 Hz–1 kHz | 2–4 kHz | principal au centre, secondaires larges |
| Clap / snare | 200 corps, 3–4 kHz crack, 5–8 kHz snap | 400–600 ; HPF 300–500 sur les percs | 3–4 kHz | ± 20 % |
| Hats, rides, shakers | 6–12 kHz | HPF 3 (house), 6–8 kHz (techno) ; shelf −1,5 dB à 12 kHz si fatigant | 10–12 kHz | ± 50–80 % |
| FX, retours | noise 200 Hz–10 kHz | HPF 150–200 sur les retours, LPF 6–8 kHz | | large |
| Master | | 200–300 si boueux ; < 20 Hz | shelf +1–2 dB > 8 kHz | |

### 3.2 Par famille

- **Leads future rave et big room** : 5–7 dents de scie ± 10–30 cents ; « saturé mais contrôlé » ; largeur maximale au drop, plus étroite en intro et outro pour le DJ ; retours de reverb et delay coupés à 150–200 Hz et ducked par le signal sec ; 200–400 Hz en dynamique (soothe3, Pro-Q 4 dynamique) plutôt qu'en statique quand le lead joue des accords `[HEUR]`.
- **Basses bass house** : trois couches, distorsion sur la mid seulement, multibande 60–120 Hz avec lookahead ; « kick perdu derrière la basse » se règle par sidechain et EQ, pas par le volume.
- **Vocals** : chops = texture en tech house ; reverb throw = envoi automatisé sur le dernier mot, retour sidechainé par la voix sèche ; présence 2–4 kHz, HPF 200.
- **Hats et claps** : attaque de compresseur lente (10–25 ms par piste, 15–40 sur bus) pour garder les transitoires ; F6 bande dynamique 6–7 kHz au master si agressif (`diagnostics.md`).

### 3.3 Densité

- Les fiches ne donnent pas de nombre d'éléments. Règle du skill `[HEUR]` : **un seul porteur par bande** au drop (sub, kick, basse mid, lead, stab ou accords, voix, hats, FX), soit six à huit familles ; une couche de lead supplémentaire **remplace** du spectre (couche large coupée à 300 Hz, couche centrale sans air) au lieu de s'y ajouter.
- « Gros sans boue » : HPF de tout sauf kick et basse à 80–120 Hz ; creux 200–400 sur nappes et supersaws ; sidechain de chaque élément au kick avec des profondeurs différentes ; densité par compression **parallèle** (API-2500 30–60 %, valeur du dépôt) plutôt qu'en série.
- Largeur par bande : centre = kick, sub, fondamentale des stabs ; ± 20 % claps et percs ; ± 50–80 % hats, rides, retours ; élargir au mix **et** au master sans contrôle mono donne un master creux sur enceinte mono.
- Par section : largeur réduite en intro et outro ; short-term −18/−20 en intro contre −10/−12 en section forte pour un master streaming `[COMM]` ; corrections par section en automation (`live-automation`).

---

## 4. Bus et master

### 4.1 Ordre de chaîne (consensus)

`HPF < 20 Hz → EQ correctif → glue → EQ tonal → stéréo (M/S) → saturation → clipper → limiteur true peak → mesure`. Rien après le limiteur sauf la mesure. La chaîne du dépôt suit déjà cet ordre sur trois bus (Pro-Q 4 → bx_glue → J37 → API-2500 parallèle → Imager → TBC/SPAN → L2).

### 4.2 Réglages de départ

| Étage | Valeur | Source |
|---|---|---|
| Glue de mix bus | 2:1 à 3:1, attaque 30–60 ms, release 200–400 ms ou auto, **1–2 dB**, HPF de détection 80–100 Hz | `[COMM]` |
| Bus batterie | attaque 15–40 ms, release 150–300 ms ; tech house 3–4 dB + parallèle ; electro et big room 4–6 dB ; techno peak-time 4–6 dB attaque rapide | `[COMM]` |
| Bus basse (bass house) | 4–6 dB ; multibande ou limiteur 4–6 dB **seulement 20–80 Hz** au master si les crêtes viennent du sub | `[COMM]` |
| Multibande master | seulement si le comportement varie par zone ; ne pas empiler EQ dynamique, soothe et multibande (`waves-mastering.md`) | dépôt |
| Clipper | après EQ, avant limiteur ; hard clip convient à l'EDM ; **ne pas clipper le grave** (HPF avant, ou par bande) ; 1–3 dB sur le drop `[HEUR]` ; but : le limiteur travaille moins, le kick garde son punch | `[DOC-EXTRAIT]` |
| Limiteur | ceiling −1,0 dBTP ; **2–4 dB** sur le drop ; au-delà de 4–5 dB, remonter le mix ; mode true peak | `[COMM, DOC-EXTRAIT]` |
| Dither | aucun en 24 bits ; TPDF une seule fois pour un 16 bits final (IDR du L2) | dépôt |
| Export | 24 bits, sans normalisation (`live-export-wav`) | dépôt |

### 4.3 Clipping contre limiting

Toutes les sources convergent : le clipper rase les transitoires du kick et de la snare sans pompage, le limiteur gère le reste ; ordre clipper puis limiteur ; risque = grave écrêté. Aucune valeur publiée fiable de « dB de clip ». Outils locaux : pas de clipper dédié ; **L4** a un contrôle Clip d'allocation ; J37 en entrée forte agit en soft clip ; RazorClip repéré dans l'inventaire mais non documenté `[TEST]`.

### 4.4 Qui masterise les six producteurs

**Non documenté** par les sources accessibles (SoundBetter, Wikipédia, EDM.com ne nomment personne). La seule interview d'ingénierie identifiée, Sound On Sound « Martin Garrix: Superstar DJ », est dans la liste à télécharger depuis le Mac. Ne rien affirmer dans un compte rendu sans les crédits Tidal, Apple ou Discogs du titre.

### 4.5 Référence et contrôle mono

A/B à sonie égale (REF vers Main hors limiteur, TBC 3, Gain Match du L4 qui désactive le ceiling : le quitter avant export) ; kick vérifié en mono ; corrélation SPAN ; sidechain lié L/R.

---

## 5. Correspondance avec les outils de ce Mac

| Tâche | Natif Live (statut de la règle 6) | Tiers de la liste | Départ |
|---|---|---|---|
| Coupe-bas et EQ correctif | EQ Eight (interdit) | **REQ 6** (par API), Pro-Q 4 (fenêtre) | kick HPF 30 (40–50 si le sub tient le grave) ; sub 25 / 80 ; basse mid HPF 80 ; top de basse HPF 300 ; supersaw HPF 150–200 + creux 200–400 ; hats HPF 3–8 kHz ; le reste HPF 80–120 |
| Résonances et boue dynamiques | | **soothe3**, Pro-Q 4 dynamique, **F6** (six bandes flottantes, M/S, sidechain externe), TDR Nova | 200–400 Hz, −2 à −4 dB dynamiques sur supersaws et nappes |
| Sidechain kick → sub, basse, lead | Compressor natif déjà en place (toléré) ; Shaper et LFO M4L = nouveaux natifs, hors règle | **bx_glue** (Ext, Int Gain, HPF), **API-2500** S/C, **Pro-C 3** | § 2.2 |
| Volume shaper | Utility (toléré) + automation de gain | | creux −6 à −12 dB, retour en 60–70 % du temps `[HEUR]` |
| Mono du grave | Utility (toléré) | **bx_glue Mono Maker** (bus BASSES), Imager 2 par bande, Center/S1 | 120 Hz ; 150 bass house |
| Saturation du grave | Saturator (interdit) | **J37** 7,5 ips, 815 → 888 ; bx_glue XL ; Abbey Road Saturator | couche mid seulement |
| Multibande basse ou master | Multiband Dynamics (interdit) | **F6**, L3 Multi, LinMB / C4 / C6 (à prober) | 20–80 Hz : 4–6 dB seulement si les crêtes viennent du sub |
| Glue de bus | Glue Compressor (interdit) | **bx_glue** (2:1, 30 ms, auto, SC HP 99 Hz), **API-2500** (Thrust = HPF du détecteur) | 1–2 dB mix bus ; 3–6 dB batterie |
| Parallèle | | **API-2500** mix 30–60 %, Thrust Med ou Loud | 10:1, 1 ms, Hard, 30 % sur la batterie (dépôt) |
| Clipper | Saturator (interdit) | **L4** Clip, RazorClip (à prober), J37 en entrée forte | 1–3 dB sur le drop `[HEUR]` |
| Limiteur | Limiter (interdit) | **L2**, **L4** (true peak, Gain Match), Ozone Elements Maximizer, WLM Plus | ceiling −1,0 ; 2–4 dB sur le drop ; club −8/−7, streaming −10/−11 |
| Largeur | Utility width (toléré) | **Imager 2** (Width global par API), S1 | +8 % global (dépôt) ; leads et hats élargis, jamais sous 120 Hz ; intro et outro plus étroits |
| Mesure | | **Insight 2**, **WLM Plus** (mesure seule) ; pyloudnorm, ffmpeg hors Live | I, ST max, ST min, TP, LRA, PLR |
| Équilibre tonal | | **TBC 3** avec courbe cible, SPAN Avg 4000 ms | tonalité avant dynamique |
| Couleur master | | **TG Mastering Chain** (Limit n'est pas un brickwall), J37 | après EQ, avant limiteur |

## 6. Manques

Mesures réelles du genre (§ 1.4) ; ingénieurs de mastering des six producteurs (§ 4.4) ; réglages exacts de LFO Tool, Kickstart, ShaperBox (outils absents) ; modules réels d'Ozone Elements 12.1 à confirmer avant de lui attribuer une fonction ; les pages de blog à vérifier sont dans `../../../../corpus/sources-a-telecharger-house.json`.
