# Théorie spécifique — future rave, bass house, house de festival et de club

Tonalités et tempos mesurés sur des données, harmonie en degrés et en notes (la mineur, C3 = 60), mélodie et riffs, basse et batterie en grilles de 16 pas avec vélocités et gate, swing, ce qui distingue le groove tech house du four-on-the-floor de la future rave. Recherche du 24 septembre 2026 (rapport : `../../../../corpus/house-future-rave/recherche-house-axe6-theorie.md`). Étiquettes : `[DOC]` jeu de données ou document lu en entier ; `[DOC-EXTRAIT]` résumé de page bloquée ; `[HEUR-lu]` fiche communautaire lue (Loopsmith edm-midi-studio, JefroB, bitwize, amen) ; `[HEUR]` pratique ; `[NON VÉRIFIÉ]` tonalité ou progression jamais lue à la source.

Déjà dans le dépôt, cité sans être répété : `../../theorie-musicale-electronique/references/genres.md` (conventions par genre), `harmonie-avancee.md` (limites du grave, voicings, question/réponse), `rythme-avance.md` (swing, euclidiens), `forme-tension.md` ; script `../../theorie-musicale-electronique/scripts/theorie.py` ; grilles `../../drums-signature/references/patterns.md`.

---

## 1. Ce que disent les données

### 1.1 Tempo `[DOC]`

| Genre | Beatport Top 100 (WhatBPM 2023, nombre de titres) | Spotify / edm_songs (médiane) | Titres de référence `[DOC-EXTRAIT]` | **À prendre** |
|---|---|---|---|---|
| Tech house | **128** (40), 126 (19), 125 (11), 127 (11) | **125** (124–126) | Turn Off The Lights 125 ; Take It 123 ; Eat Your Man 125 ; Saving Up 130 | 128 festival / Beatport, 124–126 club et radio |
| Bass house | **126** (29), 128 (27), 125 (17), 127 (13) | | Feel The Volume 125 ; Rock The Party 128 | 126–128 |
| Mainstage (future rave, big room) | **128** (21), 130 (15), 126 (12) | | Kill Me Slow 126, Detroit 3 AM 125, Dreams 128, Save My Life 128 ; Animals 128 | 126–128 |
| House | 127, 125, 124, 128, 126 | 123 | | 124–127 |
| Progressive | **124** (30), 122 (20) | 126 | | 124–126 |
| Deep house | 126, 124, 122 | 123 | | 122–126 |

### 1.2 Mode et tonalités `[DOC GiantSteps, annotation manuelle de 604 titres]`

- **85 % de mineur** ; tech house 88 %, deep house 95 %, electro house 90 %, progressive 76 %. Tonalités de tête tous genres : F mineur 12 %, G mineur 10 %, A mineur 9 %, C mineur 9 %, E mineur 8 %, D mineur 7 %.
- Tech house : D mineur 16 %, C mineur 11 %, E♭ mineur 11 %, F mineur 10 %, A mineur 10 %. Progressive : A mineur 14 %, E mineur 9 %, F mineur 8 %. Bass house (Beatport 2023) : fondamentales E, F♯, F, E♭. Mainstage : A, E, E♭, F♯, F ; Kill Me Slow **F♯ mineur**, Animals **F mineur**.
- **Le champ `mode` de Spotify est inutilisable** (≈ 50 % de mineur : l'algorithme attribue la relative majeure ; l'annotation Beatport automatique ne coïncide avec la manuelle que dans 29 % des cas). Sur une tonalité « majeure » lue chez Tunebat ou Spotify pour un titre de club, **présumer la relative mineure** tant que l'oreille n'a pas tranché.
- Conseil d'écriture : fa, mi ou ré mineur mettent la fondamentale de basse à F1 = 43,7 Hz, E1 = 41,2, D1 = 36,7, dans la zone d'un sub de club ; en la mineur, basse à A1 (55 Hz) plutôt qu'A0.

### 1.3 Modes rencontrés

| Mode | Où |
|---|---|
| Mineur naturel | défaut de tout |
| Phrygien (♭2) | bass house et electro house sombres, riffs de basse ♭2 → 1 |
| Dorien (6 majeure) | house, future house « funky » (vamp i7–IV7), moments groovy de la tech house |
| Mineur harmonique | montées dramatiques, V7 tenu en build |
| Pentatonique mineure | riffs de basse tech house et bass house, toplines |
| Chromatique | notes d'approche un demi-ton sous la cible |

Aucune statistique modale n'existe dans les données (mineur ou majeur seulement) : les attributions de modes sont `[HEUR-lu]`.

---

## 2. Harmonie par genre (la mineur ; i = Am [57 60 64], III = C [60 64 67], iv = Dm [62 65 69], v = Em [64 67 71], V = E [64 68 71], VI = F [65 69 72], VII = G [67 71 74])

### 2.1 Future rave

- Un à quatre accords ; **quintes à vide, add9, sus4** plutôt que triades pleines ; un accord par mesure sur 8 mesures. Loopsmith : `i5 · iv add9 · VI sus4 · v5 · i5 · iv add9 · VI sus4 · VII5` `[HEUR-lu]`. Progressions : **i–VI–VII** (Am–F–G), **i–VII–VI** (Am–G–F), i–iv–VI–v, ou **i tenu** sur tout le drop.
- **Rave stabs** : accord court (gate 30–45 %) quinte + octave + tierce mineure, ou m7/add9, en **accents syncopés** sur les pas 1, 7, 9, 15 (temps 1, « et » de 2, temps 3, « et » de 4), vélocités 96 × {1, 0,88, 0,95, 0,9}.
- Nappes : fondamentale doublée à l'octave inférieure, vélocité 62, gate 97 % ; jamais de tierce nue sous C2.
- Exemple : stabs i5 [57 64 69] · F5 [53 60 65] · G5 [55 62 67] · E5 [52 59 64] ; nappe = mêmes fondamentales −12 tenues ; lead en octave 5 (A5 = 93). Modulation rare ; la couleur vient de la relative majeure (Guetta « Don't Leave Me Alone » démarre sur la relative majeure `[DOC-EXTRAIT]`).

### 2.2 Big room et festival

- Progression reine **i–VI–III–VII** = Am–F–C–G, voicing lié [57 60 64] · [57 60 65] · [60 64 67] · [59 62 67] (= vi–IV–I–V de la relative majeure). Variantes : i–VII–VI–VII, i–VII–VI–V (cadence andalouse), i–III–VII–VI.
- **Titanium** `[DOC-EXTRAIT Hooktheory]` : couplet en mi♭ majeur I–V–vi (E♭–B♭–Cm) ; refrain en do mineur **VI–VII–v–i** (A♭–B♭–Gm–Cm) ; le refrain ne joue jamais E♭. Chordify donne Fm au lieu de Gm pour le remix : contradiction à trancher à l'oreille.
- **Animals** : fa mineur, 128 ; drop quasi monotonal sur F ; progression du break `[NON VÉRIFIÉ]`.
- Un accord par mesure ou deux mesures par accord ; drops souvent **sur un seul accord**. Lead et supersaw : fondamentale, quinte, octave (« power chord + octave »).

### 2.3 Future house

- **m7, m9, maj7, 7sus4, add9, jamais de triades nues** ; 2–4 accords en boucle ; voicings rootless MIDI 55–75. Loopsmith house : **Am7–Fmaj7–Dm9–Em7** = [57 60 64 67] · [53 57 60 64] · [50 57 60 64 67] · [52 59 62 67] ; vamp dorien im7–IVmaj7 (Am7–D7).
- Basse off-beat sous les accords ; le stab tombe aussi sur le « et ». La basse FM du drop joue **fondamentale et octave**, rarement la tierce (elle est dans le stab).

### 2.4 Tech house

- **« i only »** est le cas le plus fréquent ; sinon i–iv, i–VII–VI–VII, i–v–iv–i ; changements toutes les 8–16 mesures ou jamais ; « la basse est l'harmonie ».
- Stabs m7/m9 courts sur le « et » de 2 et le « et » de 4, gate ≈ 36 % d'une croche, vélocité 67–77 ; power chords A5/D5 ; sus2/sus4 « tension sans résolution ». Exemple : Am7 sans fondamentale [64 67 72 76] sur basse A1 ; Dm7 [65 69 72 77] à la mesure 3.

### 2.5 Bass house

- Drop **atonal ou monotonal** : le riff de basse définit la tonalité ; pas de nappe, pas de progression ; i–VII au plus. Breakdown : i–VI–VII ou i–VII–VI–VII sur nappes ou piano (Tchami « Afterlife »), puis retour au riff seul.
- Intervalles du riff : **seconde mineure (chromatisme), tierce mineure, quinte, octave** ; ♭2 → 1 phrygien.

### 2.6 Registres et modulation

- Pas de tierce sous **C2 (48)**, pas de quinte sous B♭0 (34) ; sub en octave 0–1 sur la fondamentale seule. Stabs 55–75 rootless ; voice leading centré sur 62. Lead future rave et big room en octave 5, sauts d'octave au climax. Sub A0 = 33 (55 Hz) ou A1 = 45 (110 Hz) ; kick accordé sur la tonique ou la quinte (`theorie.py sub A`).
- Modulations rares : +1/2 ou +1 ton au dernier drop ; le procédé fréquent est la **réinterprétation relative** (couplet sur la relative majeure, drop sur le mineur).

---

## 3. Mélodie et riffs

### 3.1 Leads future rave et big room `[HEUR-lu Loopsmith]`

- **Motif de 2 mesures répété**, seule la fin change : hook A sur les mesures impaires, A′ sur les paires ; mesure 4 = réponse (± 1 degré), **mesure 7 = climax** (+2 à +4 degrés et **+12 sur la note centrale**), mesure 8 = résolution sur 1 ou 5 avec une note longue ≥ 1,25 temps.
- Cellule « festival » (temps, durée, degré) : mesure A (0, 0,5, 1) (0,5, 0,5, 3) (1,5, 0,5, 5) (2, 0,75, 8) (3, 0,25, 7) (3,25, 0,5, 5) ; mesure B (0, 0,75, 5) (1, 0,5, 8) (1,75, 0,25, 7) (2, 0,5, 5) (2,75, 0,25, 3) (3, 0,75, 1). En la mineur octave 5 : **A5 C6 E6 A6 G6 E6 / E6 A6 G6 E6 C6 A5** = 93 96 100 105 103 100 / 100 105 103 100 96 93. Les notes sur les temps 1 et 3 ou de ¾ de temps et plus sont **calées sur une note d'accord**.
- Notes tenues + **pitch-bend** : note tenue 2 temps, enveloppe de pitch bend −2 à 0 demi-tons sur les doubles précédant l'attaque `[HEUR]` ; intervalles larges (quarte, quinte, octave) ; syncopes : noire pointée + double, note sur le « et », gallop (0,5 + 0,25 + 0,25) ; peu de silences.
- Ornement : double d'approche avant le temps 1 (−2 demi-tons en mineur, vélocité −24) ou note voisine de 0,18 temps à vélocité 58 avant une note courte.

### 3.2 Plucks et arpèges

Arpège 1/16 « up » sur triade + octave, vélocité **92 sur chaque temps, 72 ailleurs**, gate 80 % ; en la mineur A3 C4 E4 A4 C5 E5 (69 72 76 81 84 88) en boucle de 6 notes sur 16 → polymètre qui se réaligne toutes les 3 mesures ; pattern 1/8 triolet pour la variation du drop 2 ; progressive : arpèges sur accords tenus, mélodie qui gagne des notes à chaque répétition, delay qui auto-harmonise.

### 3.3 Toplines et écriture

- Ambitus étroit, pentatonique, répétition ; hooks de 1–3 notes en tech house (« le rythme est la mélodie ») ; chops = texture rythmique ; future house : chops pitchés sur fondamentale ou quinte de l'accord courant ; intervalles house : seconde majeure, tierce mineure, quarte, sixte majeure.
- **Question / réponse** : phrase 1 (m. 1–2) finit sur 2, 5 ou 7 ; phrase 2 (m. 3–4) sur 1 ou 3. **Drop 2** : même hook + une couche (contre-mélodie qui n'entre qu'au second drop), ou climax déplacé, ou +12 sur la note centrale. **Contre-mélodie** : dans les silences du lead (trous ≥ ¾ temps), une octave plus bas, sur la tierce ou la quinte, vélocité 72.

---

## 4. Basse, grilles 16 pas (fondamentale A1 = 45, sub A0 = 33 ; `+12` = octave)

### 4.1 Future rave

```
Off-beat 1/8       pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
basse A1                 . . x . | . . x . | . .  x  .  | .  .  x  .
```
Vélocité ≈ 102 sur les « et » (± 5), **gate 80 %** de la croche ; la dernière croche devient une **note d'approche chromatique** vers la fondamentale suivante 40 % du temps.

```
Rolling 1/16       pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
                         . x x x | . x x x | . x  x  x  | .  x  x  x     vel 66 pairs / 86 impairs, gate 80 % (0,2 temps)
```
**La première double de chaque temps reste vide pour le kick** (même règle chez Attack, basse en octave C2) `[DOC-EXTRAIT]` ; doubler la mesure 4 ou 8 à +12 sur les pas 2–4 `[HEUR]`. Reese des breaks : fondamentale tenue 2,4 temps puis, sur le « et » de 3, note d'approche, quarte, quinte ou −2 (vélocité 104/96).

### 4.2 Bass house

```
Tresillo (pas 1, 7, 13)   X . . . | . . X . | . . . . X . . .
Wobble (JefroB)           X ~ ~ x | . X ~ ~ | x . X ~ | ~ x . .
Loopsmith 'wobble'        pas [1, 5, 7, 11, 13] · [1, 4, 7, 9, 13, 15] · [1, 7, 9, 13, 16] ; hauteurs fondamentale + {0, 0, +7, +12, −12, +3} ; durées 0,4 / 0,65 / 0,9 temps ; vel 110
```
Notes répétées sur une seule hauteur avec du **rythme** ; croches et doubles courtes, syncopes ; **glides** en mono legato (notes qui se chevauchent d'un pas) ; chromatismes un demi-ton sous la cible et ♭2 phrygien. Exemple 2 mesures en la mineur (pas ; note ; vel ; gate) : 1 A1 118 60 % · 4 A1 96 50 % · 7 C2 110 60 % · 9 A1 100 40 % · 11 G1 90 40 % · 13 A2 118 90 % (glide vers) 15 G♯1 80 30 % ; mesure 2 identique sauf 13–16 : E2 tenu 4 pas `[HEUR]`. Le pattern se répète sur **2 mesures** ; la variation vient de la vitesse du LFO, pas des notes.

### 4.3 Tech house

```
Rolling 1/16 (Loopsmith)  pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
                                X . . x | . . x . | X .  .  x  | .  .  x  .     vel 102 / 80 / 94 / 102 / 80 / 94 ; gate 0,35 temps
```
25 % des notes sautent à +12 (vélocité 84) ; la dernière (pas 15) devient note d'approche 50 % du temps ; swing 55 % appliqué. Variante rolling 1/8 : croches vélocité 104/88 alternées, gate 84 %, 7e croche → quinte 50 %, 8e → approche. Dom Dolla : « simple bass lines, root note in a minor key, a bit of shuffle or swing on the bassline » `[DOC-EXTRAIT]`. Ghost notes sur les pas pairs à 40–55, gate 25 % ; accents 1, 7, 9, 15 ; sauts d'octave au pas 9 ou 15.

### 4.4 House et future house

```
Organ M1 off-beat   . . x . | . . x . | . . x . | . . x .     (gate 50–60 %)
Funk-derived         x . x x | . x . x | x . x x | . x . .
Disco walking        fondamentale et octave alternées en croches, ou 1–3–5–6–♭7 en montée
```
Contretemps 100–110, doubles 70–85 ; registre MIDI 33–45.

---

## 5. Rythme

### 5.1 Swing (50 % = droit, 66 % = triolet)

| Genre | Valeur |
|---|---|
| Future rave, big room, electro house | **50 %**, grille droite |
| Bass house | 50–53 % ; « le groove vient du LFO de la basse » |
| Tech house | **52–55 %** |
| House, future house | 52–56 % **sur les hats seulement** |
| Deep house | 57–62 % |

Le swing ne s'applique qu'aux **positions 2 et 4 de chaque temps**, jamais au kick ni au clap. Dans Live : Groove Pool « Swing 16 » à 53–55 % sur hats, percussions et basse tech house, Amount 100 %, kick et clap sans groove.

### 5.2 Grilles

**Tech house 126–128** `[HEUR-lu JefroB, Loopsmith, drums-signature]`
```
kick      X . . . | X . . . | X . . . | X . . .   v112–118 (ghost kick possible pas 7 et 15, v70)
clap      . . . . | X . . o | . . . . | X . . o   v96–104 ; ghost pas 8/16 v40
ch-hat    x o x o | x o x o | x o x o | x o x o   v96/52, ou doubles [90 60 70 60]
open hat  . . x . | . . x . | . . x . | . . x .   v60–70 sur les « et »
shaker    o x o o | x o o x | o o x o | o x o o   v52/96 (E(5,16) tourné)
conga     . . . x | . . . . | x . . . | x . . .   v96
rim       . . x . | . . . . | . . x . | . . . .   v70–80
ride      . x . x | . x . x | . x . x | . x . x   v60–70
```
**Bass house 126** : kick droit v118 ; clap 2 et 4 v104 court ; hats en croches v80 sans variation ; **pas de percussion concurrente de la basse** ; ghost kick « G-house » pas 4 et 11 v70 en variante.

**Future rave et big room 126–128**
```
kick      X . . . | X . . . | X . . . | X . . .   v118, aucune humanisation
clap      . . . . | X . . . | . . . . | X . . .   v104–118, en couches ; impact sur le un du drop
ch-hat    x . x . | x . x . | x . x . | x . x .   v80–96 ; doubles dans le build
open hat  . . x . | . . x . | . . x . | . . x .   v60
shaker    . . x . | . . x . | . . x . | . . x .   v52
rim       . . . . | . . x . | . . . . | . . x .   v50–70
tom       . . . . | . . . . | . . . o | . . . .   v52, une mesure sur quatre
stabs     X . . . | . . x . | X . . . | . . x .   accords du § 2.1 : le groove est là, pas dans les hats
```
Le sidechain (release ≈ 1/8 à 1/4 de temps) est **la** composante rythmique : « the pump is a rhythmic element ».

**Future house et house 124–126** : grille house classique, swing 52–56 % hats seulement, une couche de percussion nouvelle toutes les 16 mesures. Évolution des hats en progressive et big room : m. 1 doubles fermées ; m. 33 open hat sur le « a » des temps 1 et 3 ; m. 65 sur tous les temps ; ride discret ; shaker à mi-parcours.

### 5.3 Fills et risers

Ratchet sur la dernière double ; rolls de hats à partir du « et » de 3, du temps 4 ou du « et » de 4, 4/6/8 notes en 1/32 ou 1/64, vélocité **52 → 98 en rampe** ; snare roll croches → doubles → triples ; riser bruit sur 8 mesures puis 4, sweep +1 octave sur 8 (Shepard) ; 1 temps à 1 mesure de silence avant le drop ; kick et basse retirés sur le build.

### 5.4 Groove : tech house contre future rave

| | Tech house (Dom Dolla, Fisher, Chris Lake) | Future rave, big room (Guetta, MORTEN, Garrix) |
|---|---|---|
| Kick | four-on-the-floor, ghost kick possible | four-on-the-floor rigide |
| Où est le groove | **basse** (rolling, accents, shuffle 52–55 %, sauts d'octave), percussions en doubles syncopées, chops placés | **stabs syncopés** + **sidechain** + lead pointé ; hats droits, swing 0 |
| Vélocités | larges (ghosts 40–55, accents 110–118) | plates (96–118), accents par couche |
| Densité | cinq couches de percussion et plus | trois (kick, clap, hats) + FX ; « power comes from alignment » |
| Harmonie | une note de basse, stabs m7 courts | i–VI–VII ou drone, quintes, supersaw |

---

## 6. Les six producteurs : tonalités et tempos

| Producteur | Titre | Tonalité | BPM | Progression |
|---|---|---|---|---|
| Guetta | Titanium (2011) | mi♭ majeur couplet / do mineur refrain | 126 | I–V–vi ; VI–VII–v–i `[DOC-EXTRAIT Hooktheory]` |
| Guetta & MORTEN | Kill Me Slow (2020) | **fa♯ mineur** | **126** | `[NON VÉRIFIÉ]`, probable i–VI–VII |
| Guetta & MORTEN | Detroit 3 AM / Never Be Alone / Odyssey | fa♯ mineur (Spotify) | 125–126 | `[NON VÉRIFIÉ]` |
| Guetta & MORTEN | Dreams / Save My Life / Alive Again | la mineur / si mineur / fa majeur (Spotify, Tunebat contredit) | 128 / 128 / 125 | `[NON VÉRIFIÉ]` |
| Garrix | Animals (2013) | **fa mineur** | **128** | drop monotonal sur F |
| Garrix & Dua Lipa | Scared To Be Lonely | do♯ mineur | 138 | |
| Chris Lake | Turn Off The Lights (2018) | **si mineur** | **125** | basse sur la fondamentale |
| Jauz | Feel The Volume (2014) | do mineur (Tunebat) ou si♭ mineur (Spotify) : contradiction | 125 | riff monotonal |
| Jauz & Ephwurd | Rock The Party (2015) | sol mineur | 128 | |
| Dom Dolla | Take It (2018) | « do majeur » → la mineur probable | **123** | fondamentale + shuffle |
| Dom Dolla | San Frandisco (2019) | tonique la | 125 | riff de basse = hook |
| Dom Dolla | Saving Up (2023) | mi♭ mineur (Tunebat) ou la♭ majeur (Beatport) | 130 | |
| MK & Dom Dolla | Rhyme Dust (2023) | sol majeur | 128 | |

Enseignement : sur les tonalités « majeures » des bases automatiques, présumer la relative mineure ; vérifier à l'oreille avant d'écrire dans un compte rendu.

## 7. Contradictions

Mode Spotify contre annotation manuelle (§ 1.2) ; tempo tech house 128 (Beatport 2023) contre 125 (Spotify, Dom Dolla) : deux scènes ; open hat sur le « et » (norme) contre sur le « a » (variante shuffle JefroB) ; Titanium Gm ou Fm au refrain ; Feel The Volume do ou si♭ mineur ; « Levels » i–III–VII–VI ou i–VI–III–VII (rotation de la même boucle, `[NON VÉRIFIÉ]`).
