---
titre: "Rapport de recherche — axe 6 : Axe 6 — Théorie musicale spécifique : future rave, bass house, house de festival/club (future house, tech house, big room)"
source: recherche web et GitHub, session Claude Code du 2026-09-24 (agent de recherche)
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: théorie spécifique (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: synthèse interne avec étiquettes de preuve ; les sources primaires sont citées dans le texte
---

# Axe 6 — Théorie musicale spécifique : future rave, bass house, house de festival/club (future house, tech house, big room)

Recherche du 2026-09-24 pour le skill `house-future-rave-bass-house-production` (Ableton Live 12, C3 = 60). Exemples en **la mineur** sauf mention ; grilles en 16 pas (`x` attaque, `X` accent, `o` ghost, `.` silence, `|` tous les 4 pas) ; vélocités MIDI 1–127 ; gate = durée de la note en % de sa case.

Étiquettes : **[DOC]** document lu en entier (dépôts GitHub, fichiers de données) · **[DOC-EXTRAIT]** résumé de recherche web (page non téléchargeable, EGRESS_BLOCKED) · **[HEUR-lu]** fiche communautaire GitHub non sourcée, lue en entier · **[HEUR]** heuristique de pratique · **[NON VÉRIFIÉ]** valeur à confirmer (tonalité, progression d'un titre).

Ce que le dépôt sait déjà et que ce rapport **ne répète pas** (à citer) :
- `.claude/skills/theorie-musicale-electronique/references/genres.md` (house, tech/bass house, progressive/big room, trance : conventions harmoniques), `harmonie-avancee.md` (limites d'intervalle dans le grave, voicings, extensions, modulation), `rythme-avance.md` (swing Linn, Groove Pool de Live, euclidiens, syncope LHL, grilles par genre), `forme-tension.md` (tempos, schémas de forme, dispositifs de tension) ; script `scripts/theorie.py` (gamme, accord, progression, sub, syncope).
- `.claude/skills/drums-signature/references/patterns.md` (deep/minimal house 120, tech house 126, techno 130 en notation Producer Pal, vélocités par plage).
- `corpus/cuivres/amen-sessions-01-house.md` (grille house, basse 33–45, voicings rootless 55–75, swing 52–56 % sur les hats), `corpus/funk-claviers/amen-patterns-01-progression-cookbook.md` (progressions en degrés avec jeux MIDI en la mineur), `corpus/funk-claviers/amen-10-drums-and-groove.md` (kit, three-layer principle, four-on-the-floor).
- Déjà écrits par les autres agents dans `corpus/house-future-rave/` (lus, cités) : `jefrob-house-music-theory.md`, `jefrob-house-rhythm-and-groove.md`, `bitwize-genres-{bass-house,tech-house,future-house,edm,progressive-house}.md`, `edm-midi-studio-genres-future-rave-extrait.md`, `tkgally-electronic-and-dance.md`.

Documents ajoutés par cet axe dans `corpus/house-future-rave/` : `whatbpm-beatport-top100-bpm-tonalites-par-genre.md`, `giantsteps-key-dataset-beatport-604-tonalites-par-sous-genre.md`, `spotify-tracks-dataset-114k-readme-tonalites-tempos-par-genre.md`, `loopsmith-edm-midi-studio-basse-hooks-contre-melodie-theory-js.md`.

---

## 1. Tonalités, modes, tempo : ce que disent les données

### 1.1 Trois jeux de données lus en entier

| Source | Nature | Fiabilité de la tonalité |
|---|---|---|
| **WhatBPM** `latest.json` du 2023-07-11 (sergree/whatbpm, gh-pages) [DOC] | Beatport Top 100 par genre (≈ 3300 titres), valeurs pondérées par la position dans le chart ; BPM, fondamentale, tonalité, durée moyenne | Tonalité = annotation automatique Beatport → indicative |
| **GiantSteps key dataset** (Knees, Faraldo et al., ISMIR 2015) `sources.xlsx` [DOC] | 604 extraits Beatport, tonalité **corrigée manuellement**, sous-genre Beatport | Haute ; montre que l'annotation Beatport automatique ne coïncide avec la manuelle que dans **29 %** des cas |
| **Spotify Tracks 114k** (CC0) + **edm_songs.csv** (towenwolf, 21 000 titres) [DOC] | 1000 titres par étiquette Spotify ; champs `key`, `mode`, `tempo` estimés par Spotify | Basse pour le mode (≈ 50 % « mineur » là où l'annotation manuelle donne 85 %) ; correcte pour le tempo médian |

### 1.2 Tempo : cœur et plages

| Genre | Beatport Top 100 (WhatBPM, n par valeur) [DOC] | Spotify / edm_songs (médiane, Q1–Q3) [DOC] | Fiches communautaires [HEUR-lu] | Titres de référence [DOC-EXTRAIT] |
|---|---|---|---|---|
| **Tech house** | **128** (40) · 126 (19) · 125 (11) · 127 (11) · 129 (7) | edm_songs `techhouse` : **125** (124–126), 99 % entre 120 et 132 | bitwize 124–128, majorité 125–127 ; jefrob 124–128 ; Loopsmith 126 | Chris Lake « Turn Off The Lights » 125 ; Dom Dolla « Take It » 123, « Eat Your Man » 125, « Saving Up » 130 |
| **Bass house** | **126** (29) · 128 (27) · 125 (17) · 127 (13) · 130 (6) | — | bitwize 124–130, cœur 126–128, jusqu'à 132 ; amen house 126–130 | Jauz « Feel The Volume » 125 |
| **Mainstage** (contient future rave et big room chez Beatport) | **128** (21) · 130 (15) · 126 (12) · 135 (8) · 140 (6) | Spotify `edm` 123 (105–128) — étiquette trop large | Wikipédia future rave « 126–130 » [DOC-EXTRAIT] ; Loopsmith future rave 126 ; bitwize big room 126–132 | Guetta & MORTEN « Kill Me Slow » 126, « Impossible » 126, « Titanium » FR remix 126 ; Garrix « Animals » 128 |
| **House** | 127 (20) · 125 (15) · 124 (14) · 128 (13) · 126 (13) | Spotify `house` 123 (109–126) ; `chicago-house` 124 (121–126) | amen 118–128 | — |
| **Future house** (pas de genre Beatport séparé) | — | — | bitwize 124–128, parfois 130 ; amen 124–128 | — |
| **Progressive house** | **124** (30) · 122 (20) · 125 (12) · 121 (10) · 123 (10) | Spotify 126 (122–128) | jefrob 124–128 ; Loopsmith 126 | — |
| **Deep house** | 126 (17) · 124 (15) · 122 (13) · 125 (11) · 128 (11) | Spotify 123 (118–125) | — | — |
| Melodic house & techno | 124 (29) · 125 (15) · 122 (13) | — | — | — |
| Techno (peak time) | 132 (15) · 135 (13) · 130 (10) | edm_songs `techno` 128 (126–131) | — | — |

Lecture pratique : **126 BPM** pour le future rave et la bass house, **128** pour le mainstage/big room et le tech house « Beatport 2023 » (le tech house radio/club de Dom Dolla reste à 123–125), **124–126** pour la progressive et la house mélodique. Écart entre WhatBPM (128) et edm_songs (125) pour le tech house : l'un date de 2023 (Top 100, sound plus dur), l'autre de playlists plus anciennes — les deux valeurs sont vraies selon l'époque et la scène [HEUR].

### 1.3 Mode : mineur, à quel point ?

- GiantSteps (annotation manuelle) [DOC] : **85 % de mineur** sur 604 titres ; tech-house **88 %**, deep-house 95 %, electro-house 90 %, house 83 %, progressive-house 76 %, trance 88 %. Tonalités les plus fréquentes tous genres : **F mineur 12 %, G mineur 10 %, A mineur 9 %, C mineur 9 %, E mineur 8 %, D mineur 7 %**.
- GiantSteps-MTG (1486 titres, manuel) [DOC] : 66 % mineur (les « - » et majeurs comptent) ; tête : C mineur 127, F mineur 122, E mineur 94, D mineur 86, C# mineur 85, G mineur 74, A mineur 74.
- Blogs [DOC-EXTRAIT] : « ≈ 65 % des titres dance en mineur ; la mineur et do mineur les plus courants » (House of Tracks) ; « 90 % des titres EDM utilisent l'accord i » (Mixed In Key) ; « la mineur en tête du Top 100 Beatport » (EDMProd). Cohérent avec GiantSteps.
- Spotify [DOC] : `mode` donne ≈ 44–54 % de mineur pour edm/house/techno/trance — **contradiction apparente** avec les 85 % manuels ; explication : l'algorithme attribue souvent la relative majeure (G majeur pour E mineur, C# majeur pour Bb mineur…). On voit d'ailleurs « G maj » en tête du techno (18 %) et du tech house Beatport (10 %), là où GiantSteps ne trouve quasiment que du mineur. **Ne pas utiliser le champ `mode` de Spotify comme statistique de mode** ; la fondamentale (`key`) reste utilisable.

### 1.4 Tonalités réellement utilisées par genre (fondamentale + mode)

| Genre | Données [DOC] | Fiches [HEUR-lu] | Conseil d'écriture |
|---|---|---|---|
| **Tech house** | GiantSteps : **D min 16 %, C min 11 %, Eb min 11 %, F min 10 %, A min 10 %** ; WhatBPM 2023 : fondamentales G, Eb, F, E ; tonalités F min, Eb min, E min, G min, C min | jefrob : la, ré, sol mineur, mi/si mineur (sombre) ; bitwize : sans mention | Fa/mi/ré mineur : la fondamentale de basse F1 = 43,7 Hz, E1 = 41,2 Hz, D1 = 36,7 Hz tient dans un sub club ; en la mineur passer la basse à A1 (55 Hz) plutôt qu'A0 (27,5 Hz) |
| **Bass house** | WhatBPM : fondamentales **E, F#, F, Eb, Ab** ; tonalités E min, F maj (probable relative de D min), Eb min, F# min | jefrob : F, G, A mineur (« sub puissant »), Bb mineur (plus lourd) ; bitwize : sans mention ; Loopsmith (pas de preset bass house) | Mi ou fa mineur : riff mid-bass en E2–E3 (82–165 Hz) sur sub E1 |
| **Mainstage / future rave / big room** | WhatBPM : fondamentales **A, E, Eb, F#, F** ; tonalités **A min, E min, F min, Eb min** ; titres : Kill Me Slow **F# min**, Animals **F min**, Titanium FR remix « A# maj » (= sol mineur relatif ?) [NON VÉRIFIÉ], Impossible « A maj » (= fa# mineur relatif ?) [NON VÉRIFIÉ] | Loopsmith future_rave : `scale: minor` ; jefrob electro house : F, A, D mineur, phrygien et mineur harmonique occasionnels | Fa# mineur / fa mineur / la mineur ; le lead supersaw en octave 5 (A5 = 93) |
| **Future house** | pas de genre Beatport ; Spotify `house` : toniques C#, F#, G, C, B | amen house : mineur par défaut (A, F, G, C, D), dorien courant ; bitwize : « minor-key melodies » pour la variante sombre | Sol/fa mineur ou dorien pour les accords de 7e/9e |
| **Progressive / melodic** | GiantSteps progressive : **A min 14 %, E min 9 %, F min 8 %** ; WhatBPM : E min, F min, C min | jefrob : A, C, F mineur ; Loopsmith progressive/melodic house : minor | La mineur (touches blanches) |

### 1.5 Modes réellement rencontrés

| Mode | Où | Source |
|---|---|---|
| **Mineur naturel (éolien)** | défaut de tout : future rave, big room, tech house, bass house, future house | Loopsmith (`minor` pour house, progressive, future_rave, tech_house, trance) [HEUR-lu] ; jefrob (« Primary » pour tech house, electro house, bass house) [HEUR-lu] ; 85 % de mineur GiantSteps [DOC] |
| **Phrygien** (b2) | bass house et electro house sombres (« dark aggression »), tech house sombre ; riffs de basse b2→1 | jefrob bass house / electro house / tech house « Secondary » [HEUR-lu] ; Loopsmith met le techno en phrygien [HEUR-lu] ; `genres.md` (dubstep, psytrance) |
| **Dorien** (6 majeure) | house, deep/future house « funky » (vamp i7–IV7), tech house « pour les moments groovy » | Loopsmith deep_house et afro_house `dorian` ; jefrob tech house « Secondary » ; amen house « Dorian very common » [HEUR-lu] |
| **Mineur harmonique** (7 majeure) | montées de big room / electro house « dramatique », cadence V7 tenue en build | jefrob electro house « Secondary » [HEUR-lu] ; `forme-tension.md` (dominante tenue sur le build) |
| **Pentatonique mineure / blues** | riffs de basse tech house et bass house, toplines | EDMProd « la plupart des basslines suivent la pentatonique mineure » [DOC-EXTRAIT] ; jefrob bass house « Secondary » |
| Chromatique | riffs de bass house « pas toujours dans une gamme » ; notes d'approche | jefrob [HEUR-lu] ; Loopsmith `approach = nextRoot ± 1` [HEUR-lu] |

La mineur pour tout ce qui suit : A B C D E F G ; en phrygien : A **Bb** C D E F G ; en dorien : A B C D E **F#** G ; en harmonique : A B C D E F **G#**.

---

## 2. Harmonie par genre (degrés → notes en la mineur → MIDI)

Jeux de notes de base (la mineur, octave 3–4, C3 = 60) : i = Am [57 60 64] · III = C [60 64 67] · iv = Dm [62 65 69] · v = Em [64 67 71] · V = E [64 68 71] · VI = F [65 69 72] · VII = G [67 71 74] (mêmes valeurs que `amen-patterns-01-progression-cookbook.md`).

### 2.1 Future rave

| Élément | Contenu | Source |
|---|---|---|
| Nombre d'accords | 1 à 4 ; **quintes à vide et add9/sus4** plutôt que triades pleines ; 1 accord par mesure sur 8 mesures | Loopsmith `future_rave.progressions` : `[i5, iv add9, VI sus4, v5, i5, iv add9, VI sus4, VII5]` et `[i add9, v sus4, VI add9, iv, i add9, v sus4, VI7, VII5]` [HEUR-lu] |
| Progressions typiques | **i–VI–VII** (Am–F–G), **i–VII–VI** (Am–G–F), i–iv–VI–v/VII, ou **i tenu** (drone) sur tout le drop | `genres.md` progressive/big room (le VI « lift ») ; jefrob electro house « i–VI–III–VII, i–VII–VI–V, i seul sur le drop (courant) » [HEUR-lu] ; Loopsmith ci-dessus |
| « Rave chords » | stab court (gate 30–45 %) sur quinte + octave + tierce mineure ou sur m7/add9, joué en **accents syncopés** ; Loopsmith `comp: [[0, 0.45], [1.5, 0.35], [2, 0.45], [3.5, 0.35]]` = temps 1, « et » de 2, temps 3, « et » de 4 (pas 1, 7, 9, 15), vélocités 96 × {1.0, 0.88, 0.95, 0.9} | Loopsmith [HEUR-lu] ; Wikipédia future rave « chunky offbeat stabs » [DOC-EXTRAIT] |
| Accords tenus sombres | pads avec fondamentale doublée à l'octave inférieure (Loopsmith `padVoicing = [v0−12, …]`, vel 62, gate 97 %) ; sus2/sus4/add9 sans tierce nue (voir `harmonie-avancee.md` § 4) | Loopsmith [HEUR-lu] |
| Exemple à écrire (la mineur, 4 mesures × 2) | Stabs : Am(add9) [57 64 69 71] → F(sus4) [53 58 60 65]… ou plus simple i5 [57 64 69] · F5 [53 60 65] · G5 [55 62 67] · E5 [52 59 64] ; pad : mêmes fondamentales −12 en tenue | calcul `theorie.py accord A5 --octave 2` [HEUR] |
| Registre | stabs : fondamentales A2–A3 (57–69), rien sous C2 avec tierce (limite `harmonie-avancee.md` § 5) ; lead octave 5 (Loopsmith `octave: 5, range: 9`) | [DOC] repo + [HEUR-lu] |
| Modulation | rare ; la couleur vient de la relative majeure : Guetta « Don't Leave Me Alone » « choisit une tonalité mineure mais démarre la progression sur l'accord de la relative majeure » | Hack Music Theory [DOC-EXTRAIT] |

### 2.2 Big room / festival (progressive house de festival)

| Élément | Contenu | Source |
|---|---|---|
| Progression reine | **i–VI–III–VII** = Am–F–C–G [57 60 64]–[57 60 65]–[60 64 67]–[59 62 67] (voicing lié : F en 2e renversement A–C–F, G en 1er renv. B–D–G) ; = vi–IV–I–V de la relative majeure | cookbook amen « minor anthem » ; `genres.md` ; jefrob electro house « anthem progression » [HEUR-lu] |
| Variantes | i–VII–VI–VII (Am–G–F–G, « driving, dark »), i–VII–VI–V (Am–G–F–E, cadence andalouse), i–III–VII–VI (« Levels » selon `genres.md`), i–iv–i–V | jefrob progressive/electro [HEUR-lu] ; `genres.md` |
| Titres vérifiés | **« Titanium »** (Guetta) : couplet en Eb majeur **I–V–vi** (Eb–Bb–Cm) ; refrain/breakdown en do mineur **VI–VII–v–i** (Ab–Bb–Gm–Cm) — le refrain ne joue jamais Eb, d'où la remarque de `forme-tension.md` | Hooktheory [DOC-EXTRAIT] |
| | **« Animals »** (Garrix) : fa mineur, 128 BPM ; drop quasi monotonal sur F (riff de lead + kick) ; progression du break i–VI–III–VII [NON VÉRIFIÉ] | Tunebat/Hooktheory pour tonalité et tempo [DOC-EXTRAIT] ; progression non lue |
| | **« Levels »** (Avicii) : do# mineur, 126 BPM [NON VÉRIFIÉ] ; `genres.md` donne i–III–VII–VI, le cookbook amen classe plutôt i–VI–III–VII en « trance/EDM » — à vérifier sur Hooktheory | [NON VÉRIFIÉ] |
| Rythme harmonique | 1 accord par mesure (Loopsmith : 8 accords sur 8 mesures) ou 2 mesures par accord (`genres.md`) ; drops de big room souvent **un seul accord** (jefrob « i only… common ») | [HEUR-lu] |
| Voicing lead/supersaw | triade + octave, fondamentale doublée ; `theory.js` qualité `'5'` = `[0, 4, 7]` en degrés = fondamentale, quinte, octave « power chord + octave — big room sounds » | Loopsmith [HEUR-lu] |

### 2.3 Future house

| Élément | Contenu | Source |
|---|---|---|
| Accords | **m7, m9, maj7, 7sus4, add9 — jamais de triades nues** ; 2–4 accords en boucle ; voicings rootless MIDI 55–75 | amen house [HEUR-lu] ; Audiotent « 9e = 1-3-5-7-9, deep house et future bass construits sur les accords étendus » [DOC-EXTRAIT] |
| Progressions | Loopsmith house : `[i7, VI7, iv9, v7, i7, VI9, iv7, v sus4]` et `[i9, iv7, VI7, v7, i9, iv7, VI9, VII7]` → en la mineur **Am7–Fmaj7–Dm9–Em7** ([57 60 64 67] · [53 57 60 64] · [50 57 60 64 67] · [52 59 62 67]) ; vamp dorien **im7–IVmaj7** (Am7–D7 : [57 60 64 67]–[50 57 60 66]) | Loopsmith [HEUR-lu] ; cookbook amen ; `genres.md` deep house |
| Basse offbeat sous les accords | fondamentale de chaque accord sur les contretemps (voir § 4.4) ; le stab de piano/orgue tombe aussi sur le « et » | amen house « organ/piano stab on the offbeat » [HEUR-lu] |
| Basse FM métallique du drop | joue la **fondamentale et l'octave** de l'accord courant, rarement la tierce (la tierce est dans le stab) | bitwize future house (« FM bass ») [HEUR-lu] + `harmonie-avancee.md` § 5 [HEUR] |

### 2.4 Tech house

| Élément | Contenu | Source |
|---|---|---|
| Harmonie | **« i only » (une note de basse) est le cas le plus fréquent** ; sinon i–iv, i–VII–VI–VII, i–v–iv–i ; changements toutes les 8–16 mesures, ou jamais ; « la basse EST l'harmonie » | jefrob tech house [HEUR-lu] ; `genres.md` ; `forme-tension.md` § 6 |
| Stabs | m7/m9 courts (Loopsmith `comp: [[1.5, 0.18, 0.7], [3.5, 0.18, 0.8]]` = « et » de 2 et « et » de 4, gate ≈ 36 % d'une croche, vel 67–77), power chords A5/D5, sus2/sus4 « tension sans résolution » | Loopsmith [HEUR-lu] ; jefrob [HEUR-lu] |
| Loopsmith `tech_house.progressions` | `[i7, i7, iv7, v7, i7, i7, VI7, v7]` : deux mesures de tonique avant chaque mouvement | [HEUR-lu] |
| Exemple | Am7 stab [64 67 72 76] (sans fondamentale, la basse la tient : Chandler, `genres.md`) sur basse A1 ; Dm7 [65 69 72 77] à la mesure 3 | [HEUR] |

### 2.5 Bass house

| Élément | Contenu | Source |
|---|---|---|
| Drop | **atonal ou monotonal** : le riff de basse définit la tonalité ; pas de pad, pas de progression ; « i only » ; deux accords maximum (i–VII) | jefrob bass house [HEUR-lu] ; bitwize « minimal melodic elements (stabs, chord hits, filtered pads) » [HEUR-lu] |
| Breakdown | progression simple i–VI–VII ou i–VII–VI–VII sur pads/piano (Tchami « Afterlife » : piano et voix) ; retour au riff seul au drop | jefrob « breakdowns may introduce simple chord progression » ; bitwize [HEUR-lu] |
| Intervalles du riff | **2de mineure (chromatisme), 3ce mineure, 5te, octave** ; b2→1 phrygien | jefrob [HEUR-lu] ; `genres.md` tech/bass house |

### 2.6 Voicings pour synthés : rappels chiffrés (repo) et compléments

- Limites du grave (`harmonie-avancee.md` § 5) : pas de tierce sous **C2 (48)**, pas de quinte sous **Bb0 (34)** ; sub en octave 0–1 sur la fondamentale seule.
- Registre des stabs house/tech house : **55–75** (G2–Eb4) rootless (amen house) ; Loopsmith centre le voice leading sur **62** (`voiceLead(raw, prev, 62)`) et double la fondamentale −12 dans les pads.
- Lead future rave/big room : octave 5 Ableton (A5 = 93) avec sauts d'octave au climax (Loopsmith `isClimax → pitch += 12`).
- Sub : A0 = 33 (55 Hz) ou A1 = 45 (110 Hz) ; kick accordé sur la tonique ou la quinte (`theorie.py sub A`).

### 2.7 Modulation et changements de tonalité

- Rares dans les quatre genres ; quand ils existent : **+1/2 ton ou +1 ton au dernier drop** (`forme-tension.md` § 4) ; jefrob progressive « key modulation possible in peak sections (up a semitone or whole tone) » [HEUR-lu].
- Le procédé le plus fréquent n'est pas une modulation mais une **réinterprétation relative** : couplet sur la relative majeure, drop sur le mineur (Titanium Eb majeur → do mineur [DOC-EXTRAIT] ; Guetta « Don't Leave Me Alone » [DOC-EXTRAIT]).

---

## 3. Mélodie et riffs

### 3.1 Leads de future rave et de big room

| Technique | Chiffré | Source |
|---|---|---|
| Motif de **2 mesures répété**, seule la fin change (« repeat a two-bar hook, ornament connectors, place the climax late, then resolve ») | Loopsmith `makeModernLead` : hook A sur mesures impaires, A' sur mesures paires ; mesure 4 = « réponse » (biais −1/0/+1 degré), **mesure 7 = climax** (biais +2/+3/+4 degrés et **+12 sur la note centrale**), mesure 8 = résolution sur 1 ou 5 avec note longue ≥ 1,25 temps | Loopsmith [HEUR-lu] ; Loopsmith README « chord tones as rails… catchy through rhythm + repetition first » [HEUR-lu] |
| Cellule « festival » de Loopsmith (temps, durée, degré relatif à la fondamentale de l'accord) | mesure A : (0, 0.5, 1) (0.5, 0.5, 3) (1.5, 0.5, 5) (2, 0.75, 8) (3, 0.25, 7) (3.25, 0.5, 5) ; mesure B : (0, 0.75, 5) (1, 0.5, 8) (1.75, 0.25, 7) (2, 0.5, 5) (2.75, 0.25, 3) (3, 0.75, 1). En la mineur octave 5 sur Am : **A5 C6 E6 A6 G6 E6 / E6 A6 G6 E6 C6 A5** = MIDI 93 96 100 105 103 100 / 100 105 103 100 96 93 ; les notes sur les temps 1 et 3 ou ≥ 3/4 de temps sont **calées sur une note d'accord** | Loopsmith `MODERN_HOOKS.festival` [HEUR-lu] |
| Notes tenues + **pitch-bend** | jefrob electro house « Bass drops : pitch bends, slides, glides » ; « Big lead melodies (supersaw, wide intervals) … octave hooks » ; en Live : note tenue 2 temps, enveloppe Pitch Bend −2 à 0 demi-tons sur les 1/16 précédant l'attaque [HEUR] | jefrob [HEUR-lu] |
| **Sauts d'octave** et intervalles larges (4te, 5te, 8ve) | jefrob progressive « Wide melodic intervals (4ths, 5ths, octaves) for epic quality » ; Loopsmith `range: 9` (degrés) pour festival | [HEUR-lu] |
| **Syncopes** | cellules Loopsmith : `dot` (noire pointée + double : 0 → 0.75, 0.75 → 0.25), `offbeat` (note sur le « et »), `gallop` (0.5 + 0.25 + 0.25) ; poids future rave `{dot: 3, sustain: 2, two8: 2, rest: 1}` = beaucoup de pointées, peu de silences | Loopsmith `CELLS` [HEUR-lu] |
| Ornement | double-croche d'approche avant le temps 1 (−2 demi-tons en mineur, vel −24), ou note voisine ±1/±2 degrés de 0,18 temps à vel 58 avant une note courte (proba 38 % festival, 20 % tech) | Loopsmith `renderMotif`/`makeModernLead` [HEUR-lu] |

### 3.2 Plucks et arpèges

- Arpège 1/16 « up » sur la triade + octave (Loopsmith `arp: { pattern: 'up', rate: 0.25, octave: 4, span: 2 }` pour future rave et trance ; `updown` pour progressive/melodic), vel **92 sur chaque temps, 72 ailleurs**, gate 80 %. En la mineur : A3 C4 E4 A4 C5 E5 (69 72 76 81 84 88) en boucle de 6 notes sur une grille de 16 → polymètre 6 contre 16 qui se réaligne toutes les 3 mesures (`rythme-avance.md` § 3).
- Pattern 1/8 triolet : 12 notes par mesure ; utile pour la variation du drop 2 (Live : grille 1/8T) [HEUR].
- Progressive/melodic : « arpeggiated synth lines over sustained chords ; melodies evolve gradually (new notes added over repetitions) ; delay-processed melodies create self-harmonization » (jefrob) [HEUR-lu].

### 3.3 Toplines vocales de house et de future house

- **Ambitus étroit**, pentatonique, répétition ; hooks 1–3 notes en tech house (« Rhythm IS the melody ») ; vocal chops = texture rythmique, mots fragmentés ; « call-and-response between vocal and instrumental phrases » (jefrob deep house) [HEUR-lu].
- Future house : « pitched and chopped vocal samples as melodic hooks… breathy female vocals » (bitwize) [HEUR-lu] ; chops repitchés sur les notes de l'accord courant (fondamentale/quinte) [HEUR].
- Intervalles typiques house : 2de majeure, 3ce mineure, 4te juste, 6te majeure (jefrob deep house) [HEUR-lu].

### 3.4 Techniques d'écriture

| Technique | Recette chiffrée | Source |
|---|---|---|
| **Question / réponse** | phrase 1 (mes. 1–2) finit sur 2, 5 ou 7 ; phrase 2 (mes. 3–4) finit sur 1 ou 3 ; Loopsmith : mesure 4 = « answer » avec biais ±1 degré, mesure 8 = résolution sur 1/5 | `harmonie-avancee.md` § 7 ; Loopsmith [HEUR-lu] |
| **Variation au drop 2** | même hook + une couche (contre-mélodie « only enters on the second drop », Loopsmith README) ; ou climax déplacé, ou +12 sur la note centrale ; `forme-tension.md` § 5 (« second drop : pile complète + une couche neuve ») | [HEUR-lu] + repo |
| **Contre-mélodie** | joue **dans les silences** du lead (trous ≥ 3/4 temps), **une octave plus bas**, sur la tierce ou la quinte de l'accord (Loopsmith `makeCounter` : `spec.d + 2 ou + 4`, vel 72, entre 0,25 temps après le début du trou et ≤ 1,2 temps) | Loopsmith [HEUR-lu] ; `harmonie-avancee.md` § 7 (rythme complémentaire, registre distinct) |
| Rails d'accord | notes sur les temps forts = notes d'accord ; passages sur les temps faibles | Loopsmith README (« chord notes as ghost notes/rails ») [HEUR-lu] |

---

## 4. Basse : écriture par genre, grilles 16 pas, vélocités, gate

Convention : pas 1–16 ; fondamentale = A1 (45) pour le « mid-bass », sub A0 (33) tenu ou doublé ; `+12` = octave.

### 4.1 Future rave

```
Offbeat 1/8 (Loopsmith 'offbeat8')          pas :  1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
basse A1                                            . . x . | . . x . | . .  x  .  | .  .  x  .
```
- Vélocités 102 sur les « et » (accent map Loopsmith `[1.0, 0.82, 0.92, 0.78]` par position de double dans le temps → contretemps ≈ 94, ± 5 de jitter) ; **gate 80 %** de la croche (0,4 temps) ; la dernière croche de la mesure devient une **note d'approche chromatique** (±1 demi-ton vers la fondamentale suivante) 40 % du temps.
- Rolling 1/16 sur la fondamentale (Loopsmith 'rumble16', étiqueté techno mais c'est la « rolling bassline » du future rave selon Wikipédia [DOC-EXTRAIT]) :
```
pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
      . x x x | . x x x | . x  x  x  | .  x  x  x        vel 66 (pas pairs) / 86 (pas impairs), gate 80 % (0,2 temps)
```
Le premier 1/16 de chaque temps est **laissé vide pour le kick** — même règle chez Attack (« leaving the first 16th-note of every beat empty to prevent clashing with the kick », basse en octave C2) [DOC-EXTRAIT]. Octaves : doubler la mesure 4 ou 8 à +12 sur les pas 2–4 [HEUR].
- Reese/sub : Loopsmith 'reese' = fondamentale tenue 2,4 temps puis, sur le « et » de 3, note d'approche ou 4te/5te/−2 (vel 104/96) — pour les breaks du future rave.

### 4.2 Bass house

```
Riff croches pointées (tresillo E(3,8), pas 1, 7, 13) — la mesure « G-house » de jefrob : X . . . | X . . . | X . . X | . . . .
Wobble (jefrob) :                                      X ~ ~ x | . X ~ ~ | x . X ~ | ~ x . .
Grilles Loopsmith 'wobble' (temps) : [0, 1, 1.5, 2.5, 3] · [0, 0.75, 1.5, 2, 3, 3.5] · [0, 1.5, 2, 3, 3.75]
   → pas [1, 5, 7, 11, 13] · [1, 4, 7, 9, 13, 15] · [1, 7, 9, 13, 16] ; hauteur = fondamentale + {0, 0, +7, +12, −12, +3} ; durées 0,4 / 0,65 / 0,9 temps ; vel 110
```
- Notes répétées sur une seule hauteur avec **rythme** (EDMProd : « adding rhythm to notes — even playing the same pitch — can create more interest ») [DOC-EXTRAIT] ; « 1/8 et 1/16 courtes, syncopes, accents à contretemps » [DOC-EXTRAIT].
- **Glides** : mode legato/mono, notes qui se chevauchent d'un pas (règle 808 de `harmonie-avancee.md` § 6) ; **chromatismes** : demi-ton sous la cible (G#→A, C#→D en la mineur), b2 phrygien (Bb→A).
- Exemple riff la mineur 2 mesures (pas ; note ; vel ; gate) : 1 A1 118 60 % · 4 A1 96 50 % · 7 C2 110 60 % · 9 A1 100 40 % · 11 G1 90 40 % · 13 A2 118 90 % (glide vers) 15 G#1 80 30 % → mesure 2 identique sauf 13–16 : E2 (+7) tenue 4 pas [HEUR].
- Le pattern se répète souvent sur **2 mesures** ; la variation vient de la vitesse du LFO, pas des notes (jefrob) [HEUR-lu].

### 4.3 Tech house

```
Rolling 1/16 Loopsmith 'rolling' (temps [0, 0.75, 1.5, 2, 2.75, 3.5]) :
pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
      X . . x | . . x . | X .  .  x  | .  .  x  .        vel ≈ 102 × accent (1 → 102, 4 → 80, 7 → 94, 9 → 102, 12 → 80, 15 → 94) ; gate 0,35 temps
      25 % des notes sautent à +12 (vel 84) ; la dernière (pas 15) devient note d'approche chromatique 50 % du temps ; swing 0,55 appliqué
Variante « rolling8 » (Loopsmith) : 8 croches, vel 104/88 alternées, gate 84 % ; 7e croche → +7 (quinte) 50 %, 8e → approche 50 %
```
- Attack, rolling techno/tech house : basse en **octave C2**, première double vide, fills en 16es sur **notes d'accord** entre les fondamentales [DOC-EXTRAIT].
- Dom Dolla (EDM Tips) : « simple bass lines, root note in a minor key ; a bit of shuffle or swing on the bassline to give it that bouncy feel » [DOC-EXTRAIT].
- Ghost notes : pas pairs à vel 40–55 et gate 25 % ; accents sur 1, 7, 9, 15 (grille tresillo décalée) [HEUR] ; **sauts d'octave** au pas 9 ou 15 (`genres.md`).

### 4.4 House / future house

```
Offbeat organ M1 (amen house)   : . . x x | . . x x | . . x x | . . x x   (amen écrit '- - x x' = pas 3–4 de chaque temps, soit une croche à contretemps tenue ; usage courant : pas 3 seul, gate 50–60 %)
Funk-derived (amen house)        : x . x x | . x . x | x . x x | . x . .
Disco walking (`genres.md`)      : fondamentale–octave alternées en croches, ou 1–3–5–6–b7 en montée ; b5 de passage
```
- Vélocités : contretemps 100–110, doubles 70–85 ; gate 50–60 % pour l'organ bass, 90 % pour la walking [HEUR] ; registre MIDI **33–45** (amen house) [HEUR-lu].

---

## 5. Rythme : grilles kick/clap/hats/percs, swing, rides, fills, risers

### 5.1 Swing (convention Live/Linn : 50 % = droit, 66 % = triolet ; `rythme-avance.md` § 4)

| Genre | Valeur | Source |
|---|---|---|
| Future rave / big room / electro house | **50 %** (« straight — no swing », « grid-locked ») ; Loopsmith future_rave `swing: 0`, progressive `0`, trance `0` | jefrob electro house ; Loopsmith [HEUR-lu] |
| Bass house | **50–53 %** ; « le groove vient du LFO de la basse plus que du timing des drums » | jefrob [HEUR-lu] |
| Tech house | **52–55 %** (jefrob) ; Loopsmith `0.55` ; drums-signature `swing(0.04)` ; percussions « swung/shuffled hi-hats » | [HEUR-lu] + repo |
| House / future house | 52–56 % **sur les hats seulement** (amen), Loopsmith house `0.54` | [HEUR-lu] |
| Deep house | 57–62 % (jefrob), Loopsmith `0.57` | [HEUR-lu] |
| Rappel Attack (repo) | techno 50–60 %, broken house 50 %, garage 60–69 % | `rythme-avance.md` |

Loopsmith n'applique le swing **qu'aux positions 2 et 4 de chaque temps** (`swing16` : décale les doubles impaires de `(amount − 0.5) × 0.5` temps), jamais au kick ni au clap — même règle que « swing the hats, not the kick » (amen). En Live : Groove Pool « Swing 16 » à 53–55 % sur hats/percs/basse tech house, Amount 100 %, kick et clap sans groove.

### 5.2 Grilles par genre (16 pas, vélocités)

**Tech house 126–128** (synthèse jefrob + Loopsmith + drums-signature) :
```
kick     X . . . | X . . . | X . . . | X . . .     v112-118 (jefrob : ghost kick possible pas 7 et 15, v70)
clap     . . . . | X . . o | . . . . | X . . o     v96-104 ; ghost pas 8/16 v40 (jefrob « ghost snares ») 
ch-hat   x o x o | x o x o | x o x o | x o x o     v96/52 (Loopsmith 'xoxo…') ; ou 16es v72-80 [v90 v60 v70 v60]
open hat . . x . | . . x . | . . x . | . . x .     v60-70 sur les « et » (Loopsmith, amen) — jefrob place l'open hat sur le « a » (pas 4) : variante, pas la norme
shaker   o x o o | x o o x | o o x o | o x o o     v52/96 (Loopsmith 'oxooxooxooxooxoo' = E(5,16) tourné)
conga    . . . x | . . . . | x . . . | x . . .     v96 (Loopsmith) ; jefrob : . . x . | . x . . | . . x . | x . . .
rim      . . x . | . . . . | . . x . | . . . .     v70-80 ; jefrob rimshot sur pas 4 et 12
ride     . x . x | . x . x | . x . x | . x . x     (jefrob) v60-70, en croches décalées
```
**Bass house 126** : kick droit v118 ; clap 2/4 v104 court ; hats 8es `x . x . | …` v80 sans variation ; **pas de percussion concurrente de la basse** ; le riff de basse (§ 4.2) est la couche rythmique principale (jefrob). Ghost kick « G-house » pas 4 et 11 v70 en variante.

**Future rave / big room 126–128** (Loopsmith future_rave + jefrob electro house) :
```
kick     X . . . | X . . . | X . . . | X . . .     v118, aucune humanisation
clap     . . . . | X . . . | . . . . | X . . .     v104-118, layered ; impact sur le 1 du drop
ch-hat   x . x . | x . x . | x . x . | x . x .     v80-96 (Loopsmith 8es) ; en build passer aux 16es
open hat . . x . | . . x . | . . x . | . . x .     v60
shaker   . . x . | . . x . | . . x . | . . x .     v52 (doublage discret de l'open hat)
rim      . . . . | . . x . | . . . . | . . x .     v50-70
tom      . . . . | . . . . | . . . o | . . . .     v52, pas 12, une mesure sur 4
stabs    X . . . | . . x . | X . . . | . . x .     accords (§ 2.1) — le « groove » du future rave est là, pas dans les hats
```
Le sidechain (release ≈ 1/8–1/4 de temps, tkgally [HEUR-lu]) est **la** composante rythmique : « the pump IS a rhythmic element » (jefrob electro house).

**Future house / house 124–126** : grille amen house (kick 4/4, clap 2/4, open hat « et », closed hat croches, shaker 16es en o, ride « et ») ; swing 52–56 % hats seulement ; **une couche de percussion nouvelle toutes les 16 mesures**.

**Progressive/big room, évolution des hats** (jefrob) : mesure 1 = 16es fermées ; mesure 33 = open hat sur le « a » des temps 1 et 3 ; mesure 65 = sur tous les temps ; ride très discret sur les « a » ; shaker entre en milieu de morceau.

### 5.3 Rides, open hats, fills, risers

- **Ride** : croches ou « et » (tech house jefrob `. x . x`) v60–70 ; big room : ride sur les « et » dans les drops pour la brillance, retiré au break [HEUR].
- **Open hat** : « et » de chaque temps (norme house/tech house/future rave) ; « et » du 4 seulement une mesure sur deux en deep house (drums-signature) ; variante jefrob sur le « a ».
- **Fills** : ratchet sur la dernière double (drums-signature tech house) ; Loopsmith `makeHatRolls` : à partir du « et » de 3, du temps 4 ou du « et » de 4, 4/6/8 notes en 1/32 ou 1/64, vélocité **52 → 98 en rampe** ; electro house : « snare roll accelerating 8ths → 16ths → 32nds » (jefrob) ; `forme-tension.md` § 4 (noires → croches → doubles → triples sur 4 mesures, vel 1 → 127).
- **Rythme des risers** : riser bruit sur 8 mesures puis 4, sweep +1 octave sur 8 mesures (Shepard) ; Loopsmith build = 8 mesures avec `fx` + snare roll ; **1 temps à 1 mesure de silence** avant le drop (tkgally) ; kick et basse retirés sur le build (Solberg via tkgally) [HEUR-lu].

### 5.4 « Groove » : Dom Dolla/Fisher vs Guetta/MORTEN

| | Tech house (Dom Dolla, Fisher, Chris Lake) | Future rave / big room (Guetta, MORTEN, Garrix) |
|---|---|---|
| Kick | four-on-the-floor, ghost kick possible sur « et » de 2/4 | four-on-the-floor rigide, aucune variation |
| Où est le groove | **basse** (rolling 16es avec accents, shuffle 52–55 %, sauts d'octave), **percussions** en 16es syncopées (E(5,16) tourné, congas, rim), vocal chops sur positions inattendues (jefrob) ; « la basse est le groove » (amen house tech house) | **stabs syncopés** (1, « et » de 2, 3, « et » de 4) + **sidechain** + lead pointé ; hats en 8es droites ; swing 0 |
| Vélocités | plages larges (ghosts 40–55, accents 110–118) | plates (96–118), accents par couche (impact, crash) plutôt que par note |
| Densité | 5+ couches de percussion, chacune à identité rythmique distincte (jefrob) | 3 couches (kick, clap, hats) + FX ; « power comes from alignment » (jefrob electro house) |
| Harmonie | 1 note de basse, stabs m7 courts | i–VI–VII ou drone, quintes, supersaw |
| Sources | jefrob tech house [HEUR-lu] ; EDM Tips Dom Dolla [DOC-EXTRAIT] ; bitwize « Bass Tech House : Fisher, Chris Lake, Cloonee, Eli Brown » [HEUR-lu] | jefrob electro house ; Loopsmith future_rave ; Wikipédia future rave [DOC-EXTRAIT] |

---

## 6. Producteurs de référence : tonalités, tempos, progressions

| Producteur | Titre | Tonalité | BPM | Progression | Source / étiquette |
|---|---|---|---|---|---|
| David Guetta | « Titanium » (2011) | Eb majeur (couplet) / do mineur (refrain) | 126 (remix FR) ; original ≈ 126 [NON VÉRIFIÉ] | couplet I–V–vi (Eb–Bb–Cm) ; refrain VI–VII–v–i en do mineur (Ab–Bb–Gm–Cm) | Hooktheory [DOC-EXTRAIT] ; Chordify liste Ab, Bb, Fm, Cm pour le remix [DOC-EXTRAIT] (Fm au lieu de Gm : **contradiction** entre sources) |
| Guetta & MORTEN | « Kill Me Slow » (2020) | **F# mineur** | **126** | [NON VÉRIFIÉ] (probable i–VI–VII : F#m–D–E) | Tunebat/Beatport/Musicstax [DOC-EXTRAIT] |
| Guetta & MORTEN | « Impossible » (John Martin, 2022) | « A majeur » (Tunebat) → fa# mineur relatif probable [NON VÉRIFIÉ] | 126 | [NON VÉRIFIÉ] | Tunebat [DOC-EXTRAIT] |
| Guetta & MORTEN | « Titanium » Future Rave Remix | « A# majeur » (12notez) → sol mineur probable [NON VÉRIFIÉ] | 126 | [NON VÉRIFIÉ] | 12notez [DOC-EXTRAIT] |
| Guetta & MORTEN | « Dreams », « Save My Life », « Alive Again », « Nothing », « Bombardment » | pages Tunebat existantes, valeurs non lues | — | — | [NON VÉRIFIÉ] — URL dans `urls-axe6.json` |
| Guetta | « Don't Leave Me Alone » | mineur, progression démarrant sur la relative majeure | — | [NON VÉRIFIÉ] | Hack Music Theory [DOC-EXTRAIT] |
| Martin Garrix | « Animals » (2013) | **F mineur** (Hooktheory, AudioKeychain ; d'autres bases donnent Db majeur = relative) | **128** | drop monotonal sur F ; break [NON VÉRIFIÉ] | Tunebat/Hooktheory [DOC-EXTRAIT] |
| Martin Garrix | « Tremor », « Wizard », « Turn Up The Speakers » | [NON VÉRIFIÉ] | 128 [NON VÉRIFIÉ] | — | — |
| Chris Lake | « Turn Off The Lights » (2018) | **B mineur** | **125** (Cloonee remix 128) | [NON VÉRIFIÉ] (basse sur la fondamentale) | Tunebat [DOC-EXTRAIT] |
| Chris Lake | « Chemicals », « Operator », « Deceiver » | [NON VÉRIFIÉ] | — | — | bitwize cite « Deceiver » (Green Velvet) [HEUR-lu] |
| Jauz | « Feel The Volume » (2014) | **C mineur** (Tunebat) ; « A# mineur » ailleurs → **contradiction** | **125** | drop = riff de basse monotonal [NON VÉRIFIÉ] | Tunebat/SongBPM [DOC-EXTRAIT] |
| Jauz & Ephwurd | « Rock The Party » (2015) | [NON VÉRIFIÉ] | — | — | bitwize [HEUR-lu] |
| Dom Dolla | « Take It » (2018) | « C majeur » (Tunebat) → la mineur relatif probable [NON VÉRIFIÉ] | **123** | basse fondamentale + shuffle (EDM Tips, style) | Tunebat [DOC-EXTRAIT] |
| Dom Dolla | « Saving Up » (2023) | **Eb mineur** | **130** | [NON VÉRIFIÉ] | Tunebat [DOC-EXTRAIT] |
| Dom Dolla & Nelly Furtado | « Eat Your Man » (2023) | « Ab majeur » → fa mineur relatif ? [NON VÉRIFIÉ] | **125** | [NON VÉRIFIÉ] | SongBPM [DOC-EXTRAIT] |
| Dom Dolla | « San Frandisco », « Define », « girl$ » | pages Tunebat existantes, valeurs non lues | — | — | [NON VÉRIFIÉ] |
| Fisher | « Losing It » (2018) | [NON VÉRIFIÉ] | 125 [NON VÉRIFIÉ] | riff de basse + « I'm losing it » | bitwize [HEUR-lu] |
| Avicii | « Levels » | C# mineur [NON VÉRIFIÉ] | 126 [NON VÉRIFIÉ] | i–III–VII–VI (`genres.md`) ou i–VI–III–VII [NON VÉRIFIÉ] | repo |

Enseignement : sur les tonalités « majeures » de Tunebat/Spotify pour des titres de club, **présumer la relative mineure** tant que l'oreille ou Hooktheory n'a pas tranché (voir § 1.3).

---

## 7. Contradictions relevées

1. **Mode** : Spotify `mode` ≈ 50 % mineur vs annotations manuelles 85 % (GiantSteps) et 65 % (blogs). Cause : détection automatique qui confond relatives. Retenir 80–90 % de mineur pour tech/bass house, 75 % pour la progressive.
2. **Tempo tech house** : 128 (Beatport Top 100 2023) vs 125 (playlists Spotify, Dom Dolla 123–125). Deux scènes : festival/Beatport à 128, club/radio à 124–126.
3. **Open hat** : sur le « et » (pas 3 de chaque temps : amen, Loopsmith, drums-signature, `rythme-avance.md`) vs sur le « a » (pas 4 : jefrob tech house/progressive). La norme est le « et » ; le « a » est une variante de shuffle.
4. **Progression de « Titanium »** : Hooktheory Ab–Bb–Gm–Cm vs Chordify Ab, Bb, Fm, Cm pour le remix future rave. Vérifier sur le titre (Gm = v mineur, Fm = iv).
5. **Tonalité « Feel The Volume »** : do mineur (Tunebat) vs si♭ mineur (autre base). Vérifier à l'oreille.
6. **Swing tech house** : 52–55 % (jefrob) vs 0,55 (Loopsmith) vs 0,04 en décalage relatif (drums-signature) — compatibles (0,04 × 1/16 ≈ 54 % Linn) ; deep house 57–62 % (jefrob) plus haut que les 52–56 % d'amen pour la house générale : swing différent selon sous-genre, pas une contradiction.
7. **« Levels »** : i–III–VII–VI (`genres.md`) vs classification « minor anthem » i–VI–III–VII (cookbook amen) — probablement une rotation de la même boucle ; [NON VÉRIFIÉ].
8. **Phrygien pour le techno** (Loopsmith) : hors sujet mais montre que les fiches communautaires attribuent le phrygien plus largement que les données ne le prouvent ; aucune statistique modale n'existe pour la bass house (les datasets ne distinguent que majeur/mineur).

## 8. Ce qui manque (à télécharger depuis le Mac : `urls-axe6.json`, 57 URL)

- Grilles Attack « Beat Dissected » naughty tech-house / deep tech house / rolling techno (swing et vélocités exactes) ; « 5 tips synth basslines » ; « levelling up chord stabs » ; « deep house chords ».
- Hooktheory : « Animals », « Titanium », page artiste Guetta (progressions exactes, degrés).
- Tunebat : Dreams / Save My Life / Alive Again / Nothing / Bombardment (MORTEN), San Frandisco (Dom Dolla), Animals, Feel The Volume (pour trancher les tonalités).
- EDMProd : bass house guide, bass lines tips, Beatport Top 100 analysis ; Futureproof « 6 EDM chord progressions » ; Hack Music Theory « Don't Leave Me Alone » ; Wikipédia future rave / future house / bass house / big room / tech house.
- Académique : Knees et al. ISMIR 2015 (PDF) ; Zenodo Beatport EDM Key Dataset ; Solberg 2014 ; Smith MTO 2021.
- Données vivantes : WhatBPM `latest.json` (mise à jour quotidienne ; la copie du corpus date du 2023-07-11).

## 9. Sources lues en entier (GitHub) et écrites dans le corpus par cet axe

| Fichier corpus | Source raw | Contenu |
|---|---|---|
| `whatbpm-beatport-top100-bpm-tonalites-par-genre.md` | sergree/whatbpm `README.md` + `gh-pages/latest.json` | README intégral + tableau BPM/fondamentale/tonalité pour les 33 genres Beatport |
| `giantsteps-key-dataset-beatport-604-tonalites-par-sous-genre.md` | GiantSteps/giantsteps-key-dataset `README` + `sources.xlsx` ; giantsteps-mtg-key-dataset `annotations.txt` | README intégral + tonalités manuelles par sous-genre + stats MTG |
| `spotify-tracks-dataset-114k-readme-tonalites-tempos-par-genre.md` | sai-chaitanya-reddy/spotify-tracks-dataset `README.md` + CSV ; towenwolf/genre-classification `edm_songs.csv` | README intégral + tableaux tonalité/mode/tempo pour 20 étiquettes + 7 genres EDM |
| `loopsmith-edm-midi-studio-basse-hooks-contre-melodie-theory-js.md` | KinhkhaTran/edm-midi-studio `lib/generators.js` (suite) + `lib/theory.js` | archétypes de basse, cellules rythmiques, hooks festival/tech, contre-mélodie, voice leading, swing16, grooveVel |

Fichiers de travail (scratchpad `house/axe6/`) : CSV Spotify 19,4 Mo, `edm_songs-master.csv` 6,5 Mo, `whatbpm-latest.json`, `giantsteps-sources.xlsx`, scripts de calcul inclus dans les appels ci-dessus (Python stdlib).
