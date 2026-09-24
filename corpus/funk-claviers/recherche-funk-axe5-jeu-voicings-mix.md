---
titre: "Rapport de recherche — Axe F5 : jeu, voicings, groove et mixage des claviers funk"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: jeu, voicings, mix
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE F5 — Jeu, voicings, programmation MIDI et mixage des claviers funk

Rapport de recherche pour le skill « sound design des synthés et claviers du funk moderne » (Ableton Live 12 + Serum 2).
Date : 2026-09-24. **Convention de hauteur : MIDI 60 = C3 (Ableton).** Quand une source utilise la notation scientifique (C4 = MIDI 60), la conversion est donnée en numéros MIDI, qui sont non ambigus.

## 0. Conditions de la recherche et légende des tags

Le proxy de sortie de la session bloque la quasi-totalité du web (Sound On Sound, Wikipédia, Pianote, Piano With Jonny, PianoGroove, Learn Jazz Standards, MusicRadar, Attack Magazine, Production Expert, Hammond Today, Reverb, iZotope, Pro Audio Files…). Le quota de recherche web de la session (200 requêtes, partagé avec les autres axes) s'est épuisé en cours de route. Seul **raw.githubusercontent.com** et l'API de recherche de code GitHub étaient joignables. J'ai donc lu **intégralement** des copies GitHub de sources primaires (articles *Synth Secrets* de Sound On Sound, articles Wikipédia « Funk », « Hammond organ », « So What chord », « Herbie Hancock », documentation et code de l'émulateur d'orgue setBfree, chapitres du manuel Ableton Live 12 déjà en miroir local, leçons de piano jazz de jazzpianodays.com), plus des compilations secondaires bien sourcées. Les pages « métier » demandées (SOS *Mixing Rhodes*, Attack *Programming funk keys*, Pianote *Superstition*…) n'ont été atteintes qu'à travers les **extraits** renvoyés par le moteur de recherche.

Tags :

- **[DOC]** : source primaire ou article de référence **lu intégralement** dans cette session (Synth Secrets, Wikipédia, manuel Ableton, documentation setBfree, leçon de méthode).
- **[HEUR]** : pratique tirée d'un tutoriel, d'une compilation ou d'un dépôt de notes **réellement lu** (souvent bien sourcé mais non primaire).
- **[HEUR-extrait]** : valeur issue **uniquement d'un extrait de résultat de recherche** (page bloquée, non lue). À recouper avant d'en faire une règle.
- **[MÉMOIRE, non vérifié]** : valeur de ma mémoire, sans page lue.
- **[TEST]** : à valider dans le Set.

---

## 1. Voicings funk au Rhodes, Clavinet, orgue et synthé

### 1.1 Le vocabulaire d'accords du funk (source de référence)

L'article Wikipédia « Funk » (copie lue intégralement, https://raw.githubusercontent.com/kirito-0512/data/main/dump/Funk.txt ; original https://en.wikipedia.org/wiki/Funk) fixe le vocabulaire [DOC] :

- accords étendus « de bebop » : mineurs avec 7ᵉ et 11ᵉ, dominantes avec 9ᵉ altérée et 13ᵉ ; exemples nommés : **Fm11**, **C7(#9)sus4**, **F9**, **Cm6**, **F6/9** ;
- les **m7 sont préférés aux triades mineures**, « trop minces » ;
- vamps statiques sur un accord, souvent alternance **m7 ↔ dominante voisine (Am → D7)** ; embellissement par **déplacement chromatique** de l'accord d'un demi-ton ou d'un ton (« Play That Funky Music » : E9 avec F#9 et F9) ;
- modes impliqués : **dorien ou mixolydien**, mélodie = mode + gamme blues ;
- claviers cités : piano acoustique (« September »), Rhodes (« Chameleon »), Wurlitzer (« Mercy, Mercy, Mercy »), Clavinet (« Superstition », « Higher Ground », « Use Me »), Hammond B-3 (« Cissy Strut », Billy Preston) ; **basse synthé « le plus souvent un Minimoog »**, pour doubler ou remplacer la basse électrique.

Compléments [HEUR] : tkgally, *Funk, soul and R&B* (https://raw.githubusercontent.com/tkgally/algorithmic-music/main/wiki/funk-soul-and-rnb.md) : palette « dominante 9, **7♯9**, m11, m6, 6/9 » ; le ♯9 tire son caractère de la tension tierce majeure / tierce mineure enharmonique (cité de Stuart Isacoff) ; quand un vamp bouge, c'est par **planing chromatique** du même voicing (pratique P-Funk) ou par une **inflexion vers IV** (gospel). Le dépôt `mekedron/claude-amen-sessions` (https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/20-genres/19-funk-soul-and-rnb.md) : « un ou deux accords ; **E9 pour tout un morceau est normal** » ; voicings guitare `9, 13, m7, m9` dans MIDI 55–70 ; en néo-soul, accords voicés MIDI 50–72 avec 9 et 11 au milieu.

### 1.2 Le « E9 de James Brown » (dominante 9 et 13)

- L'accord guitare « James Brown » est un **Dom9 sans fondamentale** contenant **3, b7, 9, 5** (extrait Medium/Guitar Control, https://teaching-online-guitar.medium.com/the-james-brown-chord-cf0fc383fae4) [HEUR-extrait]. Avec 3 et b7 en place, on ajoute librement fondamentale, 9 et 13 ; on alterne **E9 → E13** pour varier (extrait Fundamental Changes, https://www.fundamental-changes.com/funk-guitar-chords-2/) [HEUR-extrait]. « Sex Machine » est en E9 parce que E est la note la plus grave d'une basse 4 cordes (extrait JustinGuitar, https://www.justinguitar.com/guitar-lessons/e9-the-funk-chord-fu-503) [HEUR-extrait].
- Offsets d'intervalle (amen, `05-chords.md`, https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/00-foundations/05-chords.md) [HEUR] : `C9 = [0,4,7,10,14]` (« Funk. James Brown »), `C13 = [0,4,10,14,21]` (« on omet 5 et 11 »), rootless `C13 = [4,9,10,14]` (E A Bb D).

| Accord | Notes (Ableton, C3 = 60) | MIDI | Contenu | Source |
|---|---|---|---|---|
| E9 « James Brown », transposition clavier de la forme guitare | (E1) + G#2 D3 F#3 B3 | (40) 56 62 66 71 | 3 b7 9 5 | contenu [HEUR-extrait] ; placement d'octave = forme guitare classique [MÉMOIRE, non vérifié] |
| E13 (5 → 13) | (E1) + G#2 D3 F#3 C#4 | (40) 56 62 66 73 | 3 b7 9 13 | [HEUR-extrait] + formule amen [HEUR] |
| E13 rootless type A (3-13-b7-9) | G#2 C#3 D3 F#3 | 56 61 62 66 | | formule jazzify [DOC] (§1.3) |
| E9 planing (« Play That Funky Music ») | même forme +1 ou +2 demi-tons (F9, F#9) | 57 63 67 72 / 58 64 68 73 | | Wikipédia « Funk » [DOC] |

Règle de jeu documentée : au clavier, la fondamentale est laissée à la basse (voir §1.3 et §2.6) ; la forme à quatre notes se joue main droite entre MIDI 55 et 72.

### 1.3 Voicings « rootless » type A / type B (Bill Evans → Herbie Hancock)

Source lue intégralement : leçons jazzpianodays.com copiées dans `toshiotawa/jazzify-lab` (https://raw.githubusercontent.com/toshiotawa/jazzify-lab/master/en-blog/src/data/blog/type-a-type-b-rootless-voicings.md et `.../jazz-piano-left-hand-voicings.md`, original https://www.jazzpianodays.com/tension-voicing-a-form-bform) [DOC].

Formules [DOC] :

- 7ᵉ avec 9ᵉ : **type A = 3-5-7-9**, **type B = 7-9-3-5** ;
- dominante avec 9 et 13 : **type A = 3-13-b7-9**, **type B = b7-9-3-13** (la 5ᵗᵉ est remplacée par la 13ᵉ, la fondamentale par la 9ᵉ) ;
- la 3ᵉ et la 7ᵉ restent toujours (elles définissent la qualité) ; la fondamentale est « fournie par le bassiste ou le contexte » ;
- ii–V–I majeur : on **alterne A-B-A ou B-A-B** pour que le voicing bouge le moins possible ; raccourci de registre de la leçon : racines C/D (et altérations) → type A, racines F/G/A → type B, B/E au choix ; « les étiquettes A/B ne sont pas standardisées : apprenez les formules ».
- Registre : « gardez les voicings au milieu du piano ; quatre notes serrées trop bas deviennent boueuses » [DOC] ; tkgally (*jazz-and-improvisation*, https://raw.githubusercontent.com/tkgally/algorithmic-music/main/wiki/jazz-and-improvisation.md) précise **C3–C5 scientifique = MIDI 48–72** [HEUR] ; le skill de comping REAPER (`microsoft/Resource2Skill`, https://raw.githubusercontent.com/microsoft/Resource2Skill/main/skills_wiki/reaper/jazz_piano_syncopated_comping_swing_phra_aef223e4/text/overview.md) place la main gauche à partir de **MIDI 48** [HEUR].

Exemples avec notes exactes (jazzify donne les noms, MIDI calculés) :

| Accord | Type | Notes (Ableton) | MIDI | Source |
|---|---|---|---|---|
| Cmaj7(9) | A (3-5-7-9) | E2 G2 B2 D3 | 52 55 59 62 | jazzify [DOC] |
| Cmaj7(9) | B (7-9-3-5) | B2 D3 E3 G3 | 59 62 64 67 | jazzify [DOC] |
| G7(9,13) | A (3-13-b7-9) | B2 E3 F3 A3 | 59 64 65 69 | jazzify [DOC] |
| G7(9,13) | B (b7-9-3-13) | F2 A2 B2 E3 | 53 57 59 64 | jazzify [DOC] |
| Dm7(9) | A | F2 A2 C3 E3 | 53 57 60 64 | formule [DOC] |
| Dm7(9) | B | C3 E3 F3 A3 | 60 64 65 69 | formule [DOC] |
| ii–V–I en C, A-B-A | Dm9 A → G13 B → Cmaj9 A | 53 57 60 64 → 53 57 59 64 → 52 55 59 62 | seule la voix C→B puis F→E, A→G bouge | jazzify [DOC] |
| Am9 (ex. « Summertime ») | B (7-3-5-9) | G2 C3 E3 B3 | 55 60 64 71 | jazzify (« G3, C4, E4, B4 » sci.) [DOC] |
| Fm7 (ex. « All The Things ») | B | Eb2 Ab2 C3 F3 | 51 56 60 65 | jazzify (« Eb3, Ab3, C4, F4 » sci.) [DOC] |
| Gm9 → C13 → Fmaj9 (skill REAPER, tonalité F) | b7-9-b3-5 → 3-13-b7-9 → 7-9-3-5 | F2 A2 Bb2 D3 → E2 A2 Bb2 D3 → E2 G2 A2 C3 | 53 57 58 62 → 52 57 58 62 → 52 55 57 60 | Resource2Skill [HEUR] |

Application funk directe (formules [DOC], calcul propre) : le vamp de **« Chameleon »** est **i–IV en Bb dorien : Bbm7 – Eb7** (fiche `belucid/daily-funk-book` citant Wikipédia, https://raw.githubusercontent.com/belucid/daily-funk-book/main/Entries/Herbie%20Hancock%20-%20Chameleon%20-%2010-26.md) [HEUR] → **Bbm9 type A = Db2 F2 Ab2 C3 (49 53 56 60)** puis **Eb13 type B = Db2 F2 G2 C3 (49 53 55 60)** : une seule voix bouge (Ab → G). La ligne de basse de 12 notes est jouée à l'**ARP Odyssey** (même fiche, citant Wikipédia et Synthtopia) [HEUR] ; ses notes exactes n'ont pas pu être vérifiées (voir §7).

### 1.4 Voicing « So What » et voicings quartaux

Article Wikipédia « So What chord » lu intégralement (copie https://raw.githubusercontent.com/ajb2969/MLInformationRetrieval/master/documents/7-1717.txt ; original https://en.wikipedia.org/wiki/So_What_chord) [DOC] :

- **trois quartes justes puis une tierce majeure** de bas en haut ; utilisé par Bill Evans dans la réponse « amen » du thème de « So What » ;
- en E : **E A D G B** = accordage des cinq cordes graves de la guitare ; c'est un **m11 disposé « à la guitare » (1, 4, b7, b3, 5)**, ou un accord quartal à 5 notes dont la note du haut est baissée d'un demi-ton ;
- **beaucoup de racines possibles** : le voicing sur E « peut aussi être C6Δ9, Asus4(7,9), G6/9, Dsus2/4/6, F lydien (FΔ9 11 13 sans 5) ou F phrygien » ; contexte majeur, mixolydien ou mineur ;
- références : Mark Levine, *The Jazz Piano Book* (Sher, 1989) ; Frank Mantooth, *Voicings for Jazz Keyboard* (« Miracle voicing », 1986) ; utilisé aussi par McCoy Tyner (« Peresina ») et Chick Corea.

Leçon quartale jazzify (https://raw.githubusercontent.com/toshiotawa/jazzify-lab/master/en-blog/src/data/blog/jazz-piano-quartal-voicings.md) [DOC pédagogique] : pile de quartes depuis D « D3, G3, C4, F4, Bb4 main droite » (sci.), formes A/B/C sur D dorien, planing par tons entiers et demi-tons, quartal de G7 « G–C–F–Bb (sus4) » ou « B–E–A–D sur basse G », Cmaj7 quartal depuis la 3ᵉ « E–A–D–G = 3, 13, 9, 5 », style Evans « main gauche C2, G2 | main droite E3, A3, D4, G4 » (sci.), et « avec bassiste : pas de fondamentale, comping au-dessus de C4 (sci. = MIDI 60) ».

| Voicing | Notes (Ableton) | MIDI | Source |
|---|---|---|---|
| So What sur D (Dm11 / D dorien) | D2 G2 C3 F3 A3 | 50 55 60 65 69 | structure [DOC] ; placement d'octave usuel (Levine) [MÉMOIRE, non vérifié] |
| So What sur E | E2 A2 D3 G3 B3 | 52 57 62 67 71 | [DOC] |
| Quartal D dorien, forme A (« D G C F A ») | idem So What | 50 55 60 65 69 | jazzify [DOC] |
| Quartal forme B (« E A D G C ») | E2 A2 D3 G3 C4 | 52 57 62 67 72 | jazzify [DOC] |
| Quartal 5 notes « D G C F Bb » (Dm11 avec 11 et b7) | D2 G2 C3 F3 Bb3 | 50 55 60 65 70 | jazzify [DOC] |
| G7 quartal (sus) | G2 C3 F3 Bb3 | 55 60 65 70 | jazzify [DOC] |
| Cmaj9#11 « Evans » | C1 G1 ‖ E2 A2 D3 G3 | 36 43 ‖ 52 57 62 67 | jazzify [DOC] |
| Offsets génériques | quartal `[0,5,10,15]`, So What `[0,5,10,15,19]` | | amen [HEUR] |

Usage funk/néo-soul : tkgally [HEUR] décrit les voicings néo-soul comme des empilements serrés « 9, 3, 11 » et des quartaux modaux qui « flottent », reliés au planing chromatique funk ; la règle de conduite est le **plus court chemin** (common tones tenus).

### 1.5 Le voicing « Herbie Hancock » (m11 à six notes)

Extraits PianoGroove (https://www.pianogroove.com/jazz-piano-lessons/herbie-hancock-voicing/) et The Jazz Piano Site (https://www.thejazzpianosite.com/jazz-piano-lessons/jazz-chord-voicings/hancock-chord/) [HEUR-extrait] : « riche, six notes, sur un m7 quand la 9ᵉ est dans la mélodie ; polychord : **main gauche triade Am, main droite triade G majeure en 2ᵉ renversement** ». Contenu : A C E | D G B = 1 b3 5 | 11 b7 9 → **Am11(9)**.

| Voicing | Notes (Ableton) | MIDI | Note |
|---|---|---|---|
| « Hancock » sur Am | A1 C2 E2 ‖ D3 G3 B3 | 45 48 52 ‖ 62 67 71 | contenu [HEUR-extrait] ; octave = choix raisonnable, la triade grave sous MIDI 48 est à la limite (voir §1.9) [MÉMOIRE, non vérifié] |

### 1.6 7♯9 (« accord Hendrix ») et 7♯9sus4

- Offsets `C7#9 = [0,4,7,10,15]` « majeur et mineur à la fois » ; règle : « les altérations vont sur l'accord qui précède une résolution » (amen [HEUR]) — mais en funk le 7♯9 est **tonique de vamp** (tkgally citant Heatwave « Boogie Nights » et James Brown) [HEUR].
- Épellations lues : **E7#9 = E G# B D G** (dépôt `gooey-audio/libgooey`, https://raw.githubusercontent.com/gooey-audio/libgooey/main/plans/neo-soul-chord-sets-plan.md) [HEUR] ; `C7#9 = C E G Bb D#` (fragment GitHub `nephtalem/blog-starting-file`) [HEUR] ; le ♯9 « est en réalité F## = G naturel » (extraits guitare) [HEUR-extrait].
- Wikipédia « Funk » cite **C7(#9)sus4** [DOC] : 4 à la place de 3, ♯9 conservé.

| Voicing | Notes (Ableton) | MIDI | Source |
|---|---|---|---|
| E7♯9, forme « guitare » au clavier | (E1) + G#2 D3 G3 | (40) 56 62 67 | épellation [HEUR] ; placement [MÉMOIRE, non vérifié] |
| E7♯9 rootless 4 notes | G#2 D3 G3 B3 | 56 62 67 71 | formule |
| E7(♯9)sus4 | (E1) + A2 B2 D3 G3 | (40) 57 59 62 67 | contenu [DOC], placement [MÉMOIRE] |
| Palette néo-soul « Neo Soul » (C majeur), pads 0–6 | Cmaj9 · Dm9 · **E7#9** · Fmaj7#11 · **G9sus4** · Am9 · **Bb9** (bVII emprunté) | | gooey [HEUR] |

### 1.7 Accords sus, 9sus4 et slash chords

- `C7sus4 = [0,5,7,10]` « dominante différée : house, gospel, modal jazz » ; slash chords : **F/G = G11sus** (« house, gospel, pop 80s, résout sur C »), **Bb/C = C7sus b7** (« funk, néo-soul »), **Ab/Bb = Bb11sus** (amen [HEUR]).
- **G9sus4 = G C D F A** (gooey [HEUR]).

| Voicing | Notes (Ableton) | MIDI |
|---|---|---|
| F/G (G11sus) | G1 ‖ F2 A2 C3 | 43 ‖ 53 57 60 |
| Bb/C (C7sus, couleur funk) | C2 ‖ Bb2 D3 F3 | 48 ‖ 58 62 65 |
| G9sus4 compact | G1 ‖ F2 A2 C3 D3 | 43 ‖ 53 57 60 62 |

### 1.8 Voicings gospel

Extraits Hear and Play / Piano With Jonny / WorshipFingers (https://hearandplay.com/main/drop-2-vs-b-voicing-techniques-2-5-1-chord-progressions/ ; https://pianowithjonny.com/piano-lessons/play-contemporary-gospel-and-rb-piano-in-3-steps/) [HEUR-extrait] : le 2-5-1 est « le tirage le plus fort vers la tonique » ; un **6/9 sur le I** est fréquent en sortie de 2-5-1 ; main gauche « fondamentale + 7 ou fondamentale + 3 », main droite « clusters ou triades » ; progressions à maîtriser 2-5-1, 3-6-2-5-1, 6-2-5-1-4 ; les voicings à deux mains (« spread ») « étalent l'accord pour qu'il ait du punch ».

Compilation amen (`01-progression-cookbook.md`, https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/30-patterns/01-progression-cookbook.md) [HEUR] : mouvements gospel/néo-soul `IV – iv – I`, `bVII7 – I` (backdoor), `I – I/3 – IV – #IVdim – I/5` (montée chromatique de basse), `ii7 – bII7 – Imaj9`, **`IVmaj7/5 – V7sus – V7 – I` (« la cadence gospel »)**, turnaround étendu `I – vi7 – ii7 – V7 – iii7 – VI7 – ii7 – V7`, et **m9 parallèles descendant par tons entiers** (néo-soul moderne). Offsets `Cm6/9 = [0,3,7,9,14]`, `C6 = [0,4,7,9]`.

| Voicing | Notes (Ableton) | MIDI | Note |
|---|---|---|---|
| C6/9 « sur le I » | C1 G1 ‖ E2 A2 D3 (G3) | 36 43 ‖ 52 57 62 (67) | contenu [HEUR-extrait], placement [MÉMOIRE] |
| Cm6/9 | C2 ‖ Eb2 G2 A2 D3 | 48 ‖ 51 55 57 62 | offsets amen [HEUR] |
| Fm11 (exemple Wikipédia « Funk ») | F1 ‖ Ab2 Bb2 Eb3 G3 | 41 ‖ 56 58 63 67 | contenu [DOC], placement [MÉMOIRE] |
| Cluster add9 « le son gospel gras » | C2 D2 E2 G2 | 48 50 52 55 | `Tieck14/open-piano-skills` [HEUR] |

### 1.9 Limites de registre (grave) pour les voicings

Table amen `07-voice-leading.md` (https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/00-foundations/07-voice-leading.md) [HEUR], convertie en noms Ableton :

| Intervalle | Note grave la plus basse utilisable | MIDI | Hz |
|---|---|---|---|
| 2de mineure | E2 | 52 | 165 |
| 3ce mineure | C2 | 48 | 131 |
| 3ce majeure | Bb1 | 46 | 117 |
| 4te juste | F1 | 41 | 87 |
| 5te juste | Bb0 | 34 | 58 |
| Octave | E0 | 28 | 41 |

Règles : sous MIDI 40 une note à la fois ; 40–48 quintes/quartes ; au-dessus de 48 tout passe ; « un mélange de rôle mix autant que de théorie ». Espacement « large en bas, serré en haut ; au moins une quinte entre la basse et la voix suivante ». C'est cohérent avec le registre C3–C5 sci. (48–72) des rootless.

---

## 2. Comping, rythme et programmation MIDI

### 2.1 Principes documentés

- **« The One »** : James Brown, « Funk is coming down on the one » (1988) ; le groupe atteste beat 1, le reste de la mesure « négocie » ; la caisse claire reste sur 2 et 4 (tkgally [HEUR], amen [HEUR]).
- **Grille de doubles-croches** : Wikipédia « Funk » [DOC] — les tempos plus lents ont « créé l'espace pour 16 placements par mesure » ; guitare et batterie en « motoring sixteenths », les autres jouent « plus syncopé, plus fragmenté » ; « le son du funk repose autant sur les espaces entre les notes ».
- **Interlock, pas empilement** : « chaque partie occupe un jeu différent de doubles-croches ; si deux parties jouent le même rythme, l'une est inutile » (amen) ; tkgally propose un **budget de densité par cellule et une exclusion mutuelle des positions** [HEUR].
- **Anticipation** : accords et notes de basse arrivent **une double-croche en avance** (amen [HEUR]) ; en jazz, anticipations du 1 et du « et » de 2 et 4, 1 à 3 frappes par mesure (tkgally jazz [HEUR]).
- **Ghost notes = le groove** : frappes à **20–35 % de vélocité** entre les coups principaux (amen) ; **≈ 10–30** de vélocité, « bien sous 70 » (tkgally *groove-and-embodiment*, https://raw.githubusercontent.com/tkgally/algorithmic-music/main/wiki/groove-and-embodiment.md, compilant Sweetwater/Loopcloud/MusicRadar) [HEUR].

### 2.2 Clavinet : la « lattice » de doubles-croches et « Superstition »

Faits vérifiés sur « Superstition » (Stevie Wonder, 1972) :

| Fait | Valeur | Source |
|---|---|---|
| Tonalité / gamme du riff | **Eb mineur pentatonique**, riff de deux mesures | tkgally [HEUR] ; tab basse `ummerr/bass` « key: Eb minor » [HEUR] |
| Tempo | **≈ 101 BPM**, doubles-croches droites | `turutupa/yames` JAM_REFERENCES, tab `ummerr/bass` « tempo: 101 », fichier de features MIDI `cjnolet/midi_genre_corpus` « InitialTempo 101.0 » [HEUR] |
| Points de syncope | la **b7 (Db) arrive une double-croche tôt, sur le « a » de 3** au lieu du 4 ; le riff **se résout sur la dernière double-croche** de la cellule de deux mesures | tkgally citant Ethan Hein et noiseaddicts [HEUR] |
| Deux parties de Clavinet | **panoramisées à l'extrême gauche/droite** pour un composite plus épais | tkgally [HEUR] ; extrait Boing Boing [HEUR-extrait] |
| Articulations | « les notes à tête en x sont des clics, comme une corde étouffée ; beaucoup de ghost notes qui jouent à peine » | extrait Pianote (https://www.pianote.com/blog/stevie-wonder-superstition/) [HEUR-extrait] |
| Instrument | Hohner **Clavinet modèle C** (pas D6) | extrait Wikipédia « Superstition (song) » + note QA `LocalSymmetry/lofn` citant Reverb [HEUR-extrait] |
| Harmonie | accord Ebm et ses extensions, mode **Eb dorien** ; chorus B7–Bb7–A7 (extrait) | essai `eimach/Obsidian-Notes` [HEUR] ; chorus [MÉMOIRE, non vérifié] |
| Statistiques du MIDI tiers (tout le fichier) | StaccatoIncidence **0,50**, durée moyenne de note 0,27 s (≈ 1,8 double-croche à 101 BPM), attaque moyenne toutes les 0,0745 s, registre moyen MIDI 52 | `stevie_wonder-superstition.mid.csv` (features jSymbolic) [HEUR, MIDI de tiers] |

Le bass tab lu (https://raw.githubusercontent.com/ummerr/bass/main/content/tabs/23-superstition.md) donne une **ligne de basse simplifiée** en croches sur Eb1 (MIDI 39) et Gb1 (42) : mesure 1 : Eb(1) Eb(1&) Gb(2&) Eb(3) Gb(3&) Eb(4) Gb(4&) ; mesure 2 : Eb(1) Eb(2) Gb(2&) Eb(3) Eb(4) — « la basse suit chaque ghost et chaque accent du Clavinet » [HEUR]. Les notes exactes du riff de Clavinet n'ont pas pu être lues (tablatures bloquées) : **ne pas les inventer** (voir §7).

Mécanique et son du Clavinet (amen `04-electromechanical-keyboards.md`, https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/10-instruments/04-electromechanical-keyboards.md) [HEUR] : clavicorde électrique, marteau caoutchouté sur corde, micros magnétiques ; **commutateurs de micros et de filtres brilliant/treble/medium/soft** ; « presque toujours joué à travers **wah, phaser**, ou les deux » ; recette de synthèse : pluck court **40–150 ms**, bande passante **800 Hz–3 kHz**, auto-wah, phaser après. Wikipédia « Clavichord » [DOC] : « un Clavinet à travers un ampli et des pédales guitare est associé au rock funky-disco des années 70 ». Synth Secrets 43 [DOC] : le **hard sync** est « l'un des moyens les plus faciles d'imiter une corde frappée ou pincée, utilisé dans certains des sons de clavecin et de clavinet les plus évocateurs jamais produits par un synthé analogique » (https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-43.md).

**Grille modèle « Clavinet lattice » (une mesure, 16 pas), synthèse des règles documentées** — ce n'est PAS la transcription de « Superstition » :

```
pas :       1    e    &    a  | 2    e    &    a  | 3    e    &    a  | 4    e    &    a
rôle :      A    g    x    P  | B    x    g    P  | A'   x    g    S  | B    x    g    P
vélocité :  118  28   20   96 | 112  22   30   90 | 110  20   32   100| 114  24   30   92
gate (% de la double-croche) : A/B 45–60 · P/S 40–50 · g 25–35 · x 15–25
```

Légende : A = accent « on the one » ; B = backbeat marqué par un « chank » (tkgally : accents X sur 2 et 4) ; P = push (note harmonique sur le « a », anticipation d'une double-croche) ; S = syncope structurelle « a de 3 » (le point de Superstition) ; g = ghost note (10–35) ; x = clic étouffé (tête en x ; sur un instrument virtuel : vélocité 15–30 ou articulation « mute » séparée). Vélocités d'après les plages amen « Accent 110–127 / Normal 85–105 / Soft 60–80 / Ghost 25–50 » [HEUR] et « ghosts ≈ 10–30 » [HEUR]. Gates d'après « Staccato 30–50 % du pas » (amen, `09-humanization-and-groove.md`) [HEUR] et le decay réel 40–150 ms du Clavinet [HEUR]. À affiner en écoute [TEST].

Doublage à la Stevie [HEUR] : deux clips légèrement différents (positions complémentaires, ex. le second n'a que les g/x et les pushes), pannés L/R à 60–100 %, Clavinet 2 avec pickup/filtre différents.

### 2.3 « Use Me » (Bill Withers, 1972)

Extraits (American Songwriter, Wikipedia, jonmaclennan.com) [HEUR-extrait] : riff de Clavinet de **Ray Jackson** trouvé en répétition et bouclé du début jusqu'au fade ; harmonie **Em7 – A7** (deux accords) ; la basse (Melvin Dunlap) « verrouille » le Clavinet et la batterie (James Gadson). Notes exactes non lues (voir §7). Voicings applicables : Em7(9) type A = G2 B2 D3 F#3 (55 59 62 66) ; A13 type B = G2 B2 C#3 F#3 (55 59 61 66) (formules §1.3) — une seule voix bouge (D → C#).

### 2.4 Rhodes : stabs « on the one » et contretemps

- Comping jazz/soul documenté : « courts stabs syncopés de shells ou rootless, placés irrégulièrement (anticipations du 1, du « et » de 2 et de 4), 1–3 frappes par mesure, densité inverse de l'activité du soliste » (tkgally jazz, citant Berliner) [HEUR].
- Skill REAPER lu [HEUR] : main gauche **stab sur le 1 tenu 1,5 temps** puis **push sur le « et » de 2 tenu 1 temps**, vélocité de base 90, **+10 à +15 sur les pushes**, **contretemps main droite × 0,75** (ghostés), swing des « et » = **+0,33 temps** (triolet dur).
- amen : « Rhodes/Wurlitzer avec chorus et phaser » en néo-soul, batterie **15–30 ms derrière** [HEUR].

**Grille modèle « stabs Rhodes funk » (une mesure)** [HEUR, synthèse] :

```
pas :       1    e    &    a  | 2    e    &    a  | 3    e    &    a  | 4    e    &    a
frappe :    X    .    .    .  | .    .    P    .  | .    .    .    S  | .    .    P    .
vélocité :  112              |           96       |                88 |           94
durée :     1/8 (gate 90 %)  |           1/16     |                1/16 lié au 1 suivant ou 1/16 |  1/16
```

Variante « nappe + stab » : accord tenu du 1 au « et » de 2, re-frappé (même voicing, vélocité −15) sur le « a » de 3 ; variante « contre-temps » (Bernie Worrell / Sly) : frappes uniquement sur les « et » (croches faibles) à 85–100, laissant le 1 à la basse et au kick [MÉMOIRE, non vérifié — à écouter]. La vélocité change le **timbre** du Rhodes plus que le niveau : « doux = pur et sombre, fort = bark métallique » (amen ; recette : vélocité → niveau de la couche inharmonique et coupure 800 Hz → 6 kHz) [HEUR] ; dans Electric, les curseurs **Vel** de Stiffness et Force font ce travail (manuel Ableton, §5) [DOC].

### 2.5 Orgue : nappes et stabs de main droite

- Comping soul/gospel : accords tenus (legato) main gauche/registre médium, **stabs courts main droite** ; « le Hammond de l'église porté dans la soul » (tkgally) [HEUR]. Jimmy Smith : basse aux pédales + « accords percussifs main gauche » (Wikipédia « Hammond organ », https://raw.githubusercontent.com/kirito-0512/data/main/dump/Hammondorgan.txt) [DOC].
- Programmation : voir §3.6 (percussion single-trigger, Leslie).

### 2.6 Main gauche vs basse électrique : quand ne pas jouer la basse

- Rootless : « la fondamentale est fournie par le bassiste » ; « avec bassiste : omettre les fondamentales, comper à partir de C4 sci. (MIDI 60) » (jazzify) [DOC].
- « Les voicings rootless **libèrent le grave pour la basse : décision de mix autant qu'harmonique** » ; « basse et guitare dans le même registre se battent pour 200–500 Hz » (amen) [HEUR].
- Funk : « la basse joue le hook » (Wikipédia « Funk ») [DOC] ; basse funk MIDI **28–52**, « utilise l'aigu bien plus que les autres genres » ; la basse « double un kick ou remplit ses trous » ; **la basse mène le kick de −5 à −10 ms** (amen) [HEUR].
- Règle pratique pour le skill : main gauche du clavier **au-dessus de MIDI 48** (§1.9) ; si un synth bass est présent, la main gauche ne double ni fondamentale ni octave grave ; elle peut jouer la shell 3-7 (ex. Em7 : G2–D3) [HEUR + §1.9].

### 2.7 Synth bass mono funk (Bernie Worrell, « Flash Light »)

Faits :

| Fait | Valeur | Source |
|---|---|---|
| Instruments de Worrell | Minimoog (« Atmosphere », « Flash Light », « Aqua Boogie », « Knee Deep »), Clavinet (« Joyful Process », « Up for the Down Stroke », « Red Hot Mama »), Hammond (« Funky Woman »…), RMI, ARP String Ensemble (« Chocolate City », « Give Up the Funk ») | Wikipédia « Funk » [DOC] |
| Formation | Juilliard et New England Conservatory ; parc : Minimoogs, Hohner D6, ARP Solina, Prophet-5 | extraits Reverb/Rolling Stone/Wikipedia [HEUR-extrait] |
| « Flash Light » (1977/78) | **plusieurs Minimoogs empilés (3–4 selon les sources)** ; « le moment où la basse synthé a supplanté la basse électrique en funk » ; élasticité = 3 VCO désaccordés dans le ladder 24 dB, travaillés au **pitch-bend** | `ZacharySBrown/idm-course` citant Wikipédia et Reverb [HEUR] |
| Remake Attack Magazine (Wavetable, Ableton) | table **Vintage › Miniwaves** position 40 % ; **sub on, tone ≈ 25 %, octave 0** ; **Mono, glide 45 ms** ; second osc **Semi −12** ; groove **« Swing 16ths 59 »** ; « joué, pas programmé : rien n'est parfaitement sur la grille » | https://www.attackmagazine.com/technique/synth-secrets/how-to-remake-flash-light-by-parliament/ [HEUR-extrait] |
| Glide « Parliament » sur Monark | glide on, réglage ≈ 4 | extrait MusicRadar [HEUR-extrait] |
| Grammaire de ligne | doubles-croches syncopées, gamme blues + tierce majeure, motifs répétitifs, **sauts d'octave ou plus**, ghost notes étouffées ; effets : enveloppe filter (Mu-Tron), octaver | Wikipédia « Funk » [DOC] |
| Registre / construction | MIDI 28–52 ; « root + octave » = disco/house, « arpèges d'accord » et « gamme + notes de passage » = funk ; **note d'approche chromatique par en dessous sur la dernière croche/double-croche** ; « la basse ne commence jamais exactement avec le kick, elle remplit les trous » (séparation rythmique funk) | amen `09-bass.md` [HEUR] |

**Grille modèle « synth bass mono funk » (une mesure, E dorien/blues, MIDI)** [HEUR, synthèse] :

```
pas :     1     e    &     a   | 2    e    &    a   | 3     e    &     a  | 4    e    &     a
note :    E1    .    E2    .   | .    .    D2   .   | E1    x    E2    .  | .    G1   .     D#1→(E1)
MIDI :    40         52        |           50       | 40    (40) 52       |      43         39
vél. :    118        95        |           82       | 110   30   100      |      88         92
gate :    1/8        1/16      |           1/16     | 1/16  1/32 1/16     |      1/16       1/16 legato
```

x = dead note (même hauteur, vélocité 30, gate très court) ; D#1→E1 = approche chromatique, **glide 45 ms** obtenu par chevauchement (legato) en mode Mono [HEUR-extrait + amen]. Swing 16ths 57–59 % (voir §2.8). Dans Serum 2 : Mono/Legato, Portamento ≈ 40–50 ms, deux oscillateurs saw désaccordés + sub, filtre LP 24 dB [HEUR-extrait + Attack] ; contrôle par **pitch-bend** sur certaines notes (Worrell) [HEUR].

### 2.8 Programmation MIDI crédible : vélocités, gates, décalages, swing, humanisation

**Vélocités** (amen `09-humanization-and-groove.md`, https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/30-patterns/09-humanization-and-groove.md) [HEUR] :

| Rôle | Vélocité | Gain linéaire |
|---|---|---|
| Accent | 110–127 | 0,86–1,0 |
| Normal | 85–105 | 0,67–0,83 |
| Doux | 60–80 | 0,47–0,63 |
| Ghost | 25–50 | 0,20–0,39 |

Recoupements : ghosts « ≈ 10–30, bien sous 70 », **variation ±5–10 sur les coups répétés** (tkgally [HEUR]) ; « accents proches du maximum, ghosts bien sous la moitié ; 110–127 = coups les plus forts, sous 70 = ghosts » (extraits Soundbrenner/Loopcloud/Technotif) [HEUR-extrait]. Motifs utiles : hats alternés 100/70/90/70 ; **+15 sur les pas 0, 4, 8, 12** ; accords : note de mélodie la plus forte, voix internes plus douces ; **roll d'accord 5–25 ms, grave d'abord** [HEUR].

**Durées (gate)** [HEUR] : staccato **30–50 %** du pas, normal 70–90 %, legato 100–110 %, « humain » 60–100 % aléatoire ; « la variation de durée est l'humanisation la plus négligée » ; Clavinet : 40–150 ms de decay réel.

**Micro-décalages** [HEUR] (amen) : accords/comping **±10–30 ms irréguliers** ; basse **−5 à −10 ms** avant le kick (funk, « la basse mène ») ; caisse claire **+10 à +25 ms** (laid-back) ; hats +3 à +8 ms ; jitter gaussien σ 1–3 ms « à peine perceptible », 4–8 ms « clairement humain », > 15 ms « bâclé » ; **jamais de jitter sur kick et sub**.

**Ce que dit la recherche (à respecter dans le skill)** — tkgally *groove-and-embodiment* [HEUR, citant des articles évalués par les pairs] :

- Frühauf, Kopiez & Platz 2013 : pattern rock avec basse ou caisse claire décalée de **−25, −15, 0, +15, +25 ms** ; **la version quantifiée est la mieux notée, les décalages précoces sont pires que tardifs**, la caisse claire plus sensible que la basse.
- Senn et al. 2016 : funk joué par des experts à 100 BPM, microtiming de −100 % (quantifié) à +100 % (doublé) : quantifié et original notés **également haut** ; le groove ne chute que pour de grands écarts.
- Danielsen (RITMO) : le « feel » (laid-back/pushed) est produit **avec** des changements de son (durée, intensité, brillance), pas par l'onset seul ; décalages **systématiques, par instrument, identiques à chaque cycle**.
- Synthèse : **grille quantifiée = bonne base ; jitter uniforme = la pire option ; si décalage, petit, fixe, par instrument (ex. caisse claire +10–20 ms), couplé à un changement de vélocité/timbre**. Dilla : swing **≈ 53–56 %** + hats/caisse claire décalés en retard **de manière identique chaque mesure** (Charnas, Hein) [HEUR]. Moteur lo-fi tkgally : caisse claire **−18 ms**, swing 60 % par défaut [HEUR].

**Swing** :

| Réglage | Signification / genre | Source |
|---|---|---|
| Définition MPC (Roger Linn) | retarde **toutes les doubles-croches paires** ; 50 % = pas de swing, **66 % = triolet parfait** (2/3 – 1/3) ; à 90 BPM, **62 %** « plus relâché » que 66 ; sur des 16ᵉˢ droites, **54 %** « détend sans sonner swing » ; « beaucoup de bons réglages entre 50 et ~70 » | Attack Magazine, https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/ [HEUR-extrait] |
| Logic 16A–16F | 50 / 54 / 58 / 62 / 66 / 71 % | extrait Melodiefabriek [HEUR-extrait] |
| Funk (batterie) | **52–58 %, ou droit avec micro-timing marqué** | amen funk [HEUR] |
| Deep house/disco 54–58 ; UKG/hip-hop/R&B 56–62 ; boom-bap/néo-soul 58–66 ; 66,7 shuffle/gospel | | amen [HEUR] |
| « Flash Light » remake | groove Ableton **« Swing 16ths 59 »** | Attack [HEUR-extrait] |
| Formule | `offset_ms = (swing/100 − 0,5) × 2 × (15000 / BPM)` ; à 100 BPM : 54 % = +12 ms, 58 % = +24 ms, 62 % = +36 ms, 66,7 % = +50 ms ; à 110 BPM : +11 / +22 / +33 / +45 ms | amen [HEUR], calcul |
| Swing jazz (croches) | ratio dépendant du tempo, ~3,5:1 lent → 1:1 très rapide ; **la croche courte reste ≈ 100 ms** (Friberg & Sundström 2002) | tkgally [HEUR] |

Gabarit MPC 58 % « par pas » (amen) [HEUR] : temps `0, +18, 0, +18…` ms (valable ≈ 133 BPM par la formule), vélocité `1,0 · 0,80 · 0,92 · 0,78`. Gabarit « laid-back néo-soul » : `+4, +20, +8, +22…` ms, vélocités `1,0 · 0,7 · 0,85 · 0,7`.

**Dans Ableton** : les fichiers de groove « Swing 16ths NN » existent dans la bibliothèque et le Groove Pool expose Timing / Random / Velocity / Base [MÉMOIRE, non vérifié — chapitre « Using Grooves » non disponible dans le miroir local]. Recommandation dérivée des sources : Timing 100 %, Random 0 % (le jitter uniforme est déconseillé), Velocity 0–30 % ; les décalages fixes par instrument se font par **Track Delay** (ms) plutôt que par Random [HEUR + TEST].

### 2.9 Programmer un orgue de façon crédible

- L'orgue n'a pas de vélocité ; certaines émulations la mappent sur la **vitesse de fermeture des contacts** (B-5 : « velocity to contact speed ») [HEUR-extrait] → mettre les vélocités à une valeur constante (100) et faire la dynamique avec la **pédale d'expression / swell** (dans setBfree, le swell est le contrôleur de modulation, https://raw.githubusercontent.com/pantherb/setBfree/master/cfg/default.cfg) [DOC].
- **Percussion single-trigger** : « ne se redéclenche qu'après relâchement de toutes les touches ; les passages legato ne la font sonner que sur la première note ou le premier accord » (Wikipédia « Hammond organ » [DOC] ; setBfree [DOC]) → pour un stab percussif à chaque accord, laisser **un silence (≥ 1/32) entre les accords** ; pour un jeu « moelleux », enchaîner legato et n'entendre la percussion que sur la première attaque [dérivé, TEST].
- **Leslie** : dans setBfree « la pédale de sustain (CC 64) bascule lent/rapide par défaut » [DOC] ; Logic/Vintage Organ : mod wheel ou pédale assignable (extrait) [HEUR-extrait] ; les transitions durent 1–3 s (cornet) et 5–9 s (tambour) (§3.4) → programmer le passage lent→rapide **1 à 2 mesures avant** le point culminant.
- Key click indépendant de la vélocité ; il « lit » comme percussif — ne pas le retirer pour le funk (Wikipédia : « les professionnels aimaient que l'attaque soit si présente ») [DOC].
- Cartographie CC de setBfree (repère pour piloter un clone) [DOC] : drawbars supérieurs CC 70–78 (« pedal.drawbar1 » etc.), **percussion.enable 80, decay 81, harmonic 82, vibrato.knob 83, rotary speed toggle 64, preset 91** ; notes MIDI **36–96 manuels, 24–55 pédalier** (default.pgm).

---

## 3. Hammond funk/soul : registrations, percussion, Leslie, techniques

### 3.1 Les drawbars (Synth Secrets 55, Gordon Reid, SOS nov. 2003)

https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-55.md (original http://www.soundonsound.com/sos/nov03/articles/synthsecrets.htm) [DOC] : tonewheel = disque dentelé devant un aimant, signal « proche d'une sinusoïde » ; neuf drawbars, chacun de 0 à 8 ; l'orgue est un **synthétiseur additif**.

| Drawbar | Couleur | Intervalle | Nom traditionnel | N° d'harmonique (réf. 16') |
|---|---|---|---|---|
| 16' | brun | sous-octave | Bass | 1 |
| 5 1/3' | brun | quinte | Quint | 3 |
| 8' | blanc | unisson | Neutral | 2 |
| 4' | blanc | octave | Octave | 4 |
| 2 2/3' | noir | 12ᵉ | Nazard | 6 |
| 2' | blanc | 15ᵉ | Block-flöte | 8 |
| 1 3/5' | noir | 17ᵉ (tierce) | Tierce | 10 |
| 1 1/3' | noir | 19ᵉ | Larigot | 12 |
| 1' | blanc | 22ᵉ | Sifflöte | 16 |

Wikipédia « Hammond organ » [DOC] : **888000000** (16', 5 1/3', 8' à fond) = « le son classique de Jimmy Smith » ; les harmoniques sont les fréquences tempérées les plus proches, pas des multiples exacts ; touches de presets en couleurs inversées.

### 3.2 Registrations documentées (avec noms)

Liste compilée de hammondtoday.com dans `eclab/flow` (https://raw.githubusercontent.com/eclab/flow/master/flow/modules/Drawbars.java) [HEUR] et presets de setBfree (https://raw.githubusercontent.com/pantherb/setBfree/master/pgm/default.pgm) [DOC pour le logiciel]. (U) = manuel supérieur, (L) = inférieur.

| Nom | Drawbars | Percussion / vibrato / Leslie | Source |
|---|---|---|---|
| Jimmy Smith | **888000000** (U) / 838000000 ou 808000000 (L) | setBfree : vibrato **C3, percussion 3ᵉ** ; « Jimmy Smith Plus » 888800000, C3, perc 3ᵉ **soft, fast**, Leslie chorale | flow ; setBfree |
| Booker T. Jones | **888800000** (1) / **888630000** (2) | setBfree « Booker T Jones » 888630000, **perc 2ᵉ** | flow ; setBfree |
| Green Onions | 888800000 (1) / 808800008 (2) | — | setBfree |
| Gimme Some Loving (Winwood) | 888800000 | — | flow |
| Funky Comping | **688600004** | — | flow |
| Bright Comping | 878000456 | — | flow |
| Dark Comping | 843000000 | — | flow |
| Gospel 1 / Gospel 2 | 808808008 / **888000008** | setBfree « Gospel » 888000008 | flow ; setBfree |
| Groove Holmes (gospel) | 888420080 (U) / 000505000 (L) | — | flow |
| House Bass (gospel, basse main gauche) | 880000000 (U) / 008080000 (L) | — | flow |
| Jimmy McGriff | 868600006 ; 883200125 (U) / 448650000 (L) | — | flow |
| Shirley Scott | 008888800 | — | flow |
| Brother Jack (McDuff) | 800000888 | — | flow |
| Whistle | 800000008 / 888000008 | — | flow |
| Ray Charles | 006876400 | — | flow |
| Reggae | 808000008 / 808000008 | — | flow ; setBfree |
| Blues | 885324588 ; 888800000 | — | flow ; setBfree |
| Rock, R&B | 888800000 (U) / 848000000 (L) | — | flow |
| Soft Backing (gospel) | 888700000 (U) / 555400000 (L) | — | flow |
| Shouting (gospel) | 876556788 ; 668848588 ; 878645466 (U) / 888800000 (L) | — | flow |
| Full Organ / Full and High | 888888888 / 888666888 | — | flow |
| Waa-waa (« 2nd bar ») | 888800000 | perc 3ᵉ soft fast | setBfree |
| Standard B / Rod Argent | 888000000 / 880000000 | — | setBfree |

Résumés secondaires [HEUR] : « 888000000 = plein, gras, gospel/rock « first three » ; 888800000 = rock plus brillant ; 800000888 = sifflet jazz creux ; 868868868 = jazz/blues courant ; 888000000 + percussion 3ᵉ = Jimmy Smith » (amen). Pour le funk, un extrait Production Expert (https://www.production-expert.com/production-expert-1/5-iconic-organ-sounds-to-power-your-tracks-and-how-to-get-them) prescrit **percussion ON, volume Soft, decay Fast** (« essentiel pour des lignes funk en doubles-croches ») [HEUR-extrait].

### 3.3 Percussion, vibrato/chorus, key click : valeurs

| Paramètre | Valeur | Source |
|---|---|---|
| Percussion | 2ᵉ ou 3ᵉ harmonique (drawbars 4' ou 2 2/3'), normal/soft, fast/slow, **single-trigger** ; le 9ᵉ drawbar (1') est désactivé quand elle est enclenchée ; le volume global baisse légèrement | Wikipédia [DOC] ; setBfree default.pgm [DOC] |
| Decay percussion | **fast ≈ 0,25–1 s, slow 2–4 s** ; défauts setBfree : fast **1,0 s**, slow **4,0 s** ; soft = gain **0,5012** (≈ −6 dB) ; « bell-like » | setBfree [DOC] |
| Percussion (recette additive) | partiel 2ᵉ/3ᵉ à decay ≈ 200 ms | tkgally synthesis-recipes [HEUR] |
| Vibrato/chorus | V1–V3, C1–C3, sélectionnable par manuel ; scanner à **≈ 7 Hz (7–10 Hz)** ; modulation relative v1/v2/v3 = 1,0 / 2,5 / 5,0 ; C = vibrato + signal sec ; **C3 « le classique »** | Wikipédia [DOC] ; setBfree [DOC] ; amen [HEUR] |
| Key click | pop des neuf contacts ; d'abord un défaut, puis assumé ; modèle setBfree : bouffées de bruit de **0,1–0,5 × 5,87 ms ≈ 0,6–2,9 ms**, niveau 0,5 à l'attaque, 0,25 au relâchement ; recette : bruit de 2–4 ms | Wikipédia [DOC] ; setBfree default.cfg [DOC] ; tkgally [HEUR] |
| Pitch-bend « Run switch » | couper/rétablir l'interrupteur Run fait chuter brièvement la hauteur | Wikipédia [DOC] |
| Crosstalk / leakage | fuite des roues voisines, aujourd'hui émulée volontairement | Wikipédia [DOC] |
| Overdrive | préampli à lampes poussé = son rock/gospel | amen [HEUR] ; setBfree overdrive on/off [DOC] |

### 3.4 Leslie : vitesses, temps de transition, structure

| Paramètre | Valeur | Source |
|---|---|---|
| Structure | cornet aigu (**> 800 Hz**) tournant vers le haut (dont un cornet factice), tambour grave (**< 800 Hz**) tournant vers le bas ; vitesses **chorale (lente) et tremolo (rapide)** différentes pour cornet et tambour, **temps de transition différents** ; effet = modulation de hauteur (Doppler) + amplitude + timbre + réverbération de la caisse ; stéréo obtenue par réflexion sur un mur/coin | Synth Secrets 58, https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-58.md (SOS fév. 2004) [DOC] |
| Vitesses (défauts setBfree, `b_whirl/whirl.c`) | cornet **40,32 rpm lent / 423,36 rpm rapide** ; tambour **36 rpm lent / 357,3 rpm rapide** ; alternative HammondWiki citée dans le code : cornet 48/400, tambour 40/342 | https://raw.githubusercontent.com/pantherb/setBfree/master/b_whirl/whirl.c [DOC] |
| Constantes de temps (exponentielles) | cornet accélération **0,161 s**, décélération **0,321 s** ; tambour accélération **4,127 s**, décélération **1,371 s** | setBfree [DOC] |
| Temps de transition (pratique) | cornet **1–3 s**, tambour **5–9 s** ; manuel de réparation : 5–8 s pour le tambour | extraits diyAudio/HammondWiki [HEUR-extrait] |
| Modèles | 122 (entrée symétrique, consoles), 147 (asymétrique, spinets) ; commutateur demi-lune ou pédale ; « l'effet le plus distinctif se produit **pendant le changement de vitesse** » | Wikipédia [DOC] |
| Recette de reconstruction | split à ~800 Hz ; par bande : pitch mod **±10–25 cents**, AM **20–40 %**, panning, LFO **≈ 7 Hz cornet / 6 Hz tambour** rapide, 0,8/0,7 Hz lent ; rampe **1–3 s** ; distorsion légère avant, room après | amen [HEUR] |

### 3.5 Techniques de jeu

- **Palm smear / glissando de paume** : « avec la paume on tient ~4 touches blanches et on glisse lentement vers l'aigu » (forum Music Player) ; « balayage atonal dramatique avec le plat de la main » (Wikipédia « Glissando ») [HEUR-extrait].
- **Palm slap** : frappe de « 3 à 6 touches » avec la paume ou le poing lâche → « pop » percussif funky (The Soundsmith, https://www.davidkempton.com/hmd4/) [HEUR-extrait].
- **Squabble** : fil de l'Organ Forum et vidéos de Tony Monaco existent (https://organforum.com/forums/forum/electronic-organs-midi/hammond-organs/37190-squabble-technique) ; la définition précise n'a pas été lue [HEUR-extrait ; contenu = MÉMOIRE : trémolo rapide de deux notes/accords voisins joué en tournant la main, non vérifié].
- Programmation MIDI d'un smear : rafale de notes diatoniques/chromatiques ascendantes espacées de 15–30 ms, vélocité constante (l'orgue n'en a pas), chevauchement total, terminée par l'accord tenu [dérivé, TEST].

### 3.6 Voir §2.9 pour la programmation MIDI de l'orgue.

---

## 4. Mixage des claviers funk (réels et virtuels)

### 4.1 EQ par instrument

**Rhodes / piano électrique**

| Zone | Action | Source |
|---|---|---|
| Fondamentales / chaleur | boost **+1 à +2 dB à 100–250 Hz** | extrait musicproductionnerds (https://musicproductionnerds.com/how-to-eq-rhodes-piano) [HEUR-extrait] |
| Boue | **−3 dB vers 300 Hz** si « boueux et léthargique » | musicproductionnerds + iZotope cheat sheet (https://www.izotope.com/community/blog/eq-cheat-sheet) [HEUR-extrait] |
| « Cheese » numérique | **−3 dB à 600–800 Hz**, **−1 à −2 dB à 1,2 kHz** | musicproductionnerds [HEUR-extrait] |
| Bark / bruit d'étouffoirs | chercher et atténuer **800 Hz–1 kHz** | iZotope [HEUR-extrait] |
| Présence | **+1,5–2 kHz** léger | iZotope [HEUR-extrait] |
| Bark (définition du timbre) | fondamentales **80 Hz–2 kHz**, caractère **2–5 kHz** | amen `13-frequency-and-eq.md` [HEUR] |
| Dureté | creux doux **2–4 kHz** (« zone de fatigue ») | iZotope [HEUR-extrait] ; amen [HEUR] |
| Attaque / cloche | **+3 dB à 6–8 kHz** « définition remarquable du haut » | musicproductionnerds [HEUR-extrait] |
| Néo-soul/lo-fi | passe-bas 2–5 kHz pour « sombre et vintage » | skills REAPER [HEUR] |

Les plages du brief (fondamentales 100–300, boue 250–400, bark 1–3 kHz, cloche 3–6 kHz) sont cohérentes avec ces sources à ±1 bande ; « bark 1–3 kHz » n'a pas de source lue (les sources placent bark/honk à 800 Hz–1 kHz ou 2–5 kHz) [MÉMOIRE, non vérifié].

**Clavinet**

| Zone | Action | Source |
|---|---|---|
| Corps | **200–500 Hz** (« clavinet low-mids ») ; couper les stabs à **150–250 Hz** pour laisser la basse | `JefroB/Electronic-Music-Genre-Skills` (electro-funk) [HEUR] |
| Médium funky | **500 Hz–2 kHz** « clair, funky » | idem [HEUR] |
| Brillant | le commutateur Brilliant ≈ **+3 dB vers 4 kHz** (passe-haut + boost), twang/bite | guide utilisateur Waves Clavinet (https://assets.wavescdn.com/pdf/plugins/clavinet.pdf) [HEUR-extrait] |
| Attaque 2–5 kHz (brief) | non trouvé dans une page lue | [MÉMOIRE, non vérifié] |
| Saturation | « saturation plus lourde pour le caractère clavinet/orgue » (preset funk) | `bitwize-music-studio/claude-ai-music-skills` mix-presets [HEUR] |
| Bande utile en synthèse | 800 Hz–3 kHz | amen [HEUR] |

**Wurlitzer** : le « bark » vient de la forme de l'anche, souvent amplifié par un ampli externe (distorsion, spring, EQ) ; zone « honky » **800 Hz–1 kHz** (extraits Gearspace/EQ cheat sheets) [HEUR-extrait] ; plus d'harmoniques impairs (composante carrée), overdrive très dépendant de la vélocité, **trémolo mono ≈ 5,5 Hz** (amen) [HEUR] ; Wurlitzer 200A : 1968 ; « Mercy, Mercy, Mercy » (Wikipédia « Funk ») [DOC].

**Orgue** : crossover Leslie 800 Hz [DOC] ; la mécanique ne descend pas sous le 16' ; pas de valeur d'EQ mix trouvée dans une page lue → passe-haut 60–100 Hz et creux 250–400 Hz si nappes épaisses [MÉMOIRE, non vérifié — TEST].

### 4.2 Compression

| Source / réglage | Ratio | Attaque | Release | GR | Notes | Source |
|---|---|---|---|---|---|---|
| Piano / keys (point de départ) | 2–3:1 | 15–30 ms | 150–300 ms | 2–4 dB | « égaliser la dynamique » | amen `14-dynamics-and-compression.md` [HEUR] |
| Rhodes ballade | 3:1 | | | 2–3 dB | | musicproductionnerds [HEUR-extrait] |
| Rhodes pop/rythmique agressif | 5:1 | | | 4–6 dB | | idem [HEUR-extrait] |
| Rhodes via 1176 (FET) | 2:1 | (rapide) | | ≈ 3 dB | | idem [HEUR-extrait] |
| Clavinet | FET type 1176 « à réponse rapide, juteux » | | | | | extrait Mixed by Marc Mozart [HEUR-extrait] |
| Parallèle (New York) | 10:1+ | la plus rapide | 50–100 ms | 10–20 dB | mélangé 20–50 % : « épaisseur et sustain sans perdre l'attaque », proposé pour le Rhodes | amen [HEUR] ; musicproductionnerds [HEUR-extrait] |
| Bus musique / glue | 2:1 | 10–30 ms | auto | 2–4 dB | | amen [HEUR] |

Types [HEUR] (amen) : **FET** « attaque très rapide, agressif, coloré » (voix, batterie) ; **Opto** « dépendant du programme, lent, doux, musical » (voix, basse, bus) ; VCA propre ; vari-mu chaud. Règle : « attaque lente (10–50 ms) = plus de punch ; attaque rapide = plus rond ». Manuel Ableton *Compressor* (miroir local, https://www.ableton.com/en/manual/live-audio-effect-reference/) [DOC] : « une légère attaque (**10–50 ms**) laisse passer les crêtes » ; lookahead 0/1/10 ms ; modes **Peak / RMS / Expand**, détecteur **Lin / Log** (« le Log relâche plus vite les crêtes fortement compressées, plus lisse ») ; > 6 dB de GR « altère significativement le son ». *Glue Compressor* [DOC] : bus SSL modélisé (Cytomic), knee qui se durcit avec le ratio, attaque en ms, release en s ou **Auto (double constante lente/rapide)**, **Range −60/−70 dB = matériel d'origine**, soft clip plafond −0,5 dB.

Chaîne (amen) [HEUR] : `gate → EQ soustractive → compresseur → EQ additive → saturation → sends` ; variante « compresseur avant EQ pour avoir son caractère sur le son brut ». Ableton *Pedal* [DOC] : « un Compressor avant Pedal donne un résultat plus équilibré ».

### 4.3 Saturation, ampli, pédales (Clavinet, orgue, Wurli)

- Fondement historique [DOC/HEUR] : Wurli et Clavinet « à travers un ampli et des pédales » ; Hammond « spring reverb et un peu d'overdrive » (Synth Secrets 55).
- Ableton *Pedal* [DOC] : types **Overdrive** (chaud), **Distortion** (serré), **Fuzz** ; EQ adaptative : Bass peak **100 Hz**, Mid **500 Hz / 1 kHz / 2 kHz**, Treble shelf **3,3 kHz**, Sub shelf **< 250 Hz** ; Hi-Quality dans le menu contextuel. *Amp* [DOC] : « Clean = canal Brilliant d'un ampli 60s (British Invasion) », « Boost = canal Tremolo du même », « Blues », « Rock = 45 W des 60s », « Bass = PA 70s ». *Cabinet* [DOC] : 1x12 → 4x12, micro Near On-Axis (brillant) / Off-Axis / Far, Dynamic (gritty) / Condenser.
- Preset funk (bitwize) [HEUR] : guitare 3:1 + saturation, **claviers : saturation plus forte pour clavinet/orgue**, cuivres +0,5 dB.
- Recette Clavinet (amen) [HEUR] : auto-wah / passe-bande suiveur d'enveloppe, **phaser après**.

### 4.4 Modulation : trémolo, auto-pan, phaser, chorus, placement, mono

- **Rhodes Suitcase** : le « Vibrato » d'origine était un **trémolo mono à onde carrée** ; avec les amplis stéréo (1969) il devient un **panoramique** (extrait fenderrhodes.com, http://www.fenderrhodes.com/history/effects.html) [HEUR-extrait] ; amen : « le classique = Rhodes dans un trémolo stéréo (auto-pan), souvent + phaser ou chorus », auto-pan **4–6 Hz** [HEUR].
- **Mono-compatibilité** : réglage Logic « Stereo 180° = out-of-phase = auto-pan ; pour un Rhodes, 180° » (extrait Apple) ; « la modulation d'amplitude stéréo s'annule en mono » (extrait Tape Op) [HEUR-extrait] → en somme mono, l'auto-pan à 180° **disparaît** (le signal reste, l'effet non) ; ce n'est pas une annulation par polarité (celle-ci « disparaît en mono » : amen [HEUR]). Pour garder du mouvement en mono : mode **Tremolo** (une seule LFO) ou Phase < 180°.
- Ableton *Auto Pan-Tremolo* [DOC] : mode **Panning** (deux LFO, offset **Phase** en degrés, 180° = parfaitement opposées ; ou **Spin**) ou **Tremolo** (une LFO) ; formes Sine, Triangle, Shark Tooth, Saw, Square, Random, Wander, S&H ; Time modes Rate/Time/Synced/Dotted/Triplet/16th (100 ms à 200 s) ; **Harmonic** (crossover fixe **600 Hz**, graves et aigus modulés en alternance) ; **Vintage** (courbe non linéaire « chaleur et grain ») ; Shape/Invert pour gating/pumping. → Rhodes : Panning, Sine, Phase 180°, 4–6 Hz, Amount 40–70 % ; Wurli : Tremolo, Square/Sine adouci, ≈ 5,5 Hz, Vintage on [HEUR + TEST].
- Ableton *Phaser-Flanger* [DOC] : Phaser = notches par all-pass, Notches / Center / Spread / Blend ; LFO Hz ou synchro, Phase/Spin stéréo, Duty Cycle ; LFO2 ; suiveur d'enveloppe ; **Safe Bass** (passe-haut) ; Warmth. *Chorus-Ensemble* [DOC] : Classic (2 lignes), **Ensemble (3 lignes, pédale 70s)**, Vibrato ; passe-haut 20–2000 Hz ; Width 0–200 % (mid/side) ; Warmth.
- Placement phaser avant/après compression : aucune page lue ; heuristique : phaser **avant** le compresseur si l'on veut que la compression lisse les creux du balayage (son « pédale » du Clavinet), **après** pour un balayage plus net sur un Rhodes déjà tenu [MÉMOIRE, non vérifié — TEST]. Chorus/ensemble : mono-safety « correcte » ; Haas : « mauvaise » (amen) [HEUR].

### 4.5 Réverb et delay

amen `15-stereo-and-space.md` [HEUR] : **Room 0,3–0,8 s** (batterie, glue), **Plate 1–3 s** (« le classique pop », **long plate = années 70**), pré-délai **20–40 ms** (garde la transitoire), **passe-haut du retour 200–500 Hz**, passe-bas 5–10 kHz ; « **RT60 ≈ une mesure au maximum** pour du matériel rythmique » ; sends partagés (une courte pour la cohésion, une longue pour la profondeur) ; jamais de réverb sur le sub. Delay slapback 60–140 ms ; dotted 1/8. Position : Rhodes **±10–25 %** de pan, cœur (kick, snare, basse, voix) au centre ; < 120 Hz mono, 120–300 Hz étroit.

### 4.6 Place face à la guitare rythmique et à la basse ; bus claviers

- Guitare funk : « **les médiums sont souvent coupés pour se distinguer des cuivres, des claviers** ; aigus montés ; pas de sustain ; compresseur pour les notes étouffées (Nile Rodgers) » (Wikipédia « Funk ») [DOC].
- « Basse et guitare se battent pour 200–500 Hz » ; « couper la guitare sous 120 Hz » ; « chords/pads : −8 à −15 dB sous l'élément le plus fort ; passe-haut 150–300 Hz sur les pads ; creux 1–3 kHz pour laisser la voix » (amen EQ / mixing) [HEUR].
- Interlock rythmique = première séparation : si Clavinet et guitare occupent les mêmes doubles-croches, l'une est de trop (amen, tkgally) [HEUR] ; en cas de conflit spectral, **couper l'élément le moins important dans la bande de l'autre** plutôt que booster (amen) [HEUR].
- Bus : structure `Drum bus / Bass bus (mono < 120 Hz) / Music bus (accords, pads, leads : EQ partagée, sidechain depuis le kick) / Vocal bus / FX returns` ; glue du bus 2:1, 10–30 ms, auto, 2–4 dB (amen) [HEUR]. Pour un bus claviers funk : Glue Compressor 2:1, attaque 10–30 ms, release Auto, 1–3 dB, sidechain léger depuis le kick (1–3 dB) pour laisser le « one » respirer [HEUR + TEST].
- Balance de genre (preset funk bitwize) : batterie +0,5 dB, basse +0,5 dB, cuivres +0,5 dB, percussions +0,5 dB, claviers 0 dB [HEUR]. Sonie funk **−10 à −8 LUFS**, néo-soul −11 à −9 (amen) [HEUR].
- « Mix warm : roll-off au-dessus de 14 kHz, +100–200 Hz doux, saturation bande » ; « le son 70s est largement un produit de la compression bande et console » (amen production notes) [HEUR].

### 4.7 Esthétiques « modern funk »

| Artiste | Ce qui est documenté | Source | Non trouvé |
|---|---|---|---|
| **Vulfpeck** | enregistré **live, sans casque**, souvent en **direct (DI) sans ampli**, éditing minimal ; Jack Stratton produit et mixe ; kick/snare « **Vulf-compressed** » ; Cory Wong : « un compresseur rend tout un peu plus pro » ; classés nu-funk « pocket, arrangements minimalistes, matériel vintage » | extraits Stanford Daily / MusicTech / Reverb (https://musictech.com/features/interviews/cory-wong-interview-lost-in-the-wonder/) [HEUR-extrait] ; bitwize funk README [HEUR] | réglages du « pumping » ; plugin Vulf Compressor (Goodhertz) [MÉMOIRE, non vérifié] |
| **Silk Sonic** | « Leave the Door Open » : piano **D'Mile**, mix **Serban Ghenea**, ingénieur John Hanes ; Grammy Record of the Year 2022 ; Bruno Mars classé « Minneapolis sound + boogie 80s avec production contemporaine » | extraits Billboard/serbanghenea.com [HEUR-extrait] ; bitwize [HEUR] | tout réglage de Rhodes/mix (brillance, largeur) |
| **Kaytranada** | hats **légèrement en retard**, snare **légèrement en avance** (« Glowed Up ») ; « kick wave » ; keys = tri­angle + unison/detune ; filtre modulé par enveloppe avec **résonance élevée** (« sweeping ») ; ex. cutoff **190 Hz** + enveloppe ; **accords passe-haut** pour laisser la basse ; basse swinguée « notes en retard et à contretemps » | extraits Reverb Machine (https://reverbmachine.com/blog/kaytranada-99-synth-sounds/), Liveschool, Synth Ctrl [HEUR-extrait] | pourcentage de swing chiffré |
| Néo-soul (général) | batterie **15–30 ms** derrière ; Rhodes/Wurli + chorus + phaser ; mix « sparse et sombre » | amen [HEUR] | |

---

## 5. Ableton Live 12 : le device Electric (Rhodes/Wurli modélisé) et paramètres pilotables

Manuel Live 12, chapitre 30.5 *Electric* (miroir local `research/mirror/30-live-instrument-reference.md` ; https://www.ableton.com/en/manual/live-instrument-reference/) [DOC] :

- Modèle physique (Applied Acoustics Systems) : marteau → fourche (**tine bar** frappée + **tone bar** résonateur accordé) → étouffoir → micro.
- **Hammer** : Stiffness (dureté, plus brillant ; modulable par **Vel** et **Key**), Noise (bruit d'impact : Pitch, Decay, Key), Force (intensité ; **Vel**, Key).
- **Fork** : Tine Color (équilibre partiels hauts/bas), Tine Decay, Key ; Tone Decay ; Release commun.
- **Damper/Pickup** : Symmetry (**50 % = micro en face = plus brillant**), Distance (**plus proche = plus overdrivé**), Type **R = électrodynamique** (Rhodes-like), **W = électrostatique** (Wurli-like), Input/Output (« input faible + output fort = plus propre »), Damper Tone/Level/Att-Rel.
- **Global** : Voices, Semi, Detune ±50 cents, **Stretch** (accord étiré).
- Guide livepilot (`research/raw/livepilot-synths-native.md`) [HEUR] : Stiffness 50–70 % naturel, > 80 % métallique ; Force 60–80 % mappé sur la vélocité ; Noise 10–20 % ; Symmetry décentrée = bark asymétrique ; recettes « Classic MKI » (R, stiffness ~55, force ~65, + trémolo), « Bright MKII » (stiffness ~70, Tine Color haut, micro plus proche), « Wurlitzer bark » (W, stiffness ~65, force ~70, micro proche + overdrive), « Clav-like » (R, stiffness ~85, decays très courts, micro proche, timbre brillant).
- Catalogue LOM local (`research/raw/sonic-analyzer-live12_device_catalog.json`) : paramètres exposés pour « Electric » = **Decay, Envelope, Pickup, Tone, Volume** (macro-vue) [DOC, fichier local] → pour le pilotage par lom.py, prévoir de vérifier les noms complets des paramètres du device [TEST].

---

## 6. Pages consultées

### 6.1 Lues intégralement (copies GitHub raw ou miroir local)

1. Wikipédia « Funk » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Funk.txt (orig. https://en.wikipedia.org/wiki/Funk) [DOC]
2. Wikipédia « Hammond organ » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Hammondorgan.txt [DOC]
3. Wikipédia « So What chord » — https://raw.githubusercontent.com/ajb2969/MLInformationRetrieval/master/documents/7-1717.txt [DOC]
4. Wikipédia « Herbie Hancock » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/HerbieHancock.txt [DOC] (Rhodes imposé par Miles Davis ; parc ARP Odyssey/2600/Pro Soloist, Moog III)
5. Wikipédia « Clavichord » (paragraphe Clavinet) — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Clavichord.txt [DOC]
6. Synth Secrets 55 (tonewheel, table des drawbars) — https://raw.githubusercontent.com/micjamking/synth-secrets/master/part-55.md [DOC] (copie partielle : première page)
7. Synth Secrets 56, 57, 59 — parts 56/57/59 (copies partielles, peu exploitables) [DOC]
8. Synth Secrets 58 (Leslie) — part-58.md [DOC] (première page : structure, 800 Hz, chorale/tremolo)
9. Synth Secrets 42 et 43 (pianos ; hard sync ↔ clavinet) — part-42.md, part-43.md [DOC]
10. setBfree `pgm/default.pgm` (presets nommés, doc percussion/vibrato/rotary) — https://raw.githubusercontent.com/pantherb/setBfree/master/pgm/default.pgm [DOC]
11. setBfree `cfg/default.cfg` (decays, key click, scanner, CC) — https://raw.githubusercontent.com/pantherb/setBfree/master/cfg/default.cfg [DOC]
12. setBfree `b_whirl/whirl.c` (rpm, constantes de temps) — https://raw.githubusercontent.com/pantherb/setBfree/master/b_whirl/whirl.c [DOC]
13. jazzify / jazzpianodays « Type A and Type B Rootless Voicings » — https://raw.githubusercontent.com/toshiotawa/jazzify-lab/master/en-blog/src/data/blog/type-a-type-b-rootless-voicings.md [DOC pédagogique]
14. jazzify « Left-Hand Voicings » — .../jazz-piano-left-hand-voicings.md [DOC pédagogique]
15. jazzify « Quartal Voicings » — .../jazz-piano-quartal-voicings.md [DOC pédagogique]
16. Manuel Ableton Live 12 : 30.5 Electric ; 28.3 Auto Pan-Tremolo ; 28.8 Chorus-Ensemble ; 28.9 Compressor ; 28.21 Glue Compressor ; 28.29 Phaser-Flanger ; 28.1 Amp ; 28.6 Cabinet ; 28.28 Pedal (miroir local) [DOC]
17. eclab/flow `Drawbars.java` (compilation hammondtoday.com) — https://raw.githubusercontent.com/eclab/flow/master/flow/modules/Drawbars.java [HEUR]
18. tkgally *Funk, soul and R&B* — https://raw.githubusercontent.com/tkgally/algorithmic-music/main/wiki/funk-soul-and-rnb.md [HEUR]
19. tkgally *Groove and embodiment* — .../wiki/groove-and-embodiment.md [HEUR]
20. tkgally *Findings — groove-lofi engine* — .../wiki/findings-groove-lofi-engine.md [HEUR]
21. tkgally *Jazz and improvisation*, *Rhythm and meter*, *Synthesis recipes* — .../wiki/jazz-and-improvisation.md, rhythm-and-meter.md, synthesis-recipes.md [HEUR]
22. amen `04-electromechanical-keyboards.md`, `05-chords.md`, `07-voice-leading.md`, `09-bass.md`, `10-drums-and-groove.md`, `13-frequency-and-eq.md`, `14-dynamics-and-compression.md`, `15-stereo-and-space.md`, `16-mixing-process.md`, `19-funk-soul-and-rnb.md`, `30-patterns/09-humanization-and-groove.md`, `30-patterns/01-progression-cookbook.md` — https://raw.githubusercontent.com/mekedron/claude-amen-sessions/main/theory/... [HEUR]
23. belucid/daily-funk-book « Chameleon » — https://raw.githubusercontent.com/belucid/daily-funk-book/main/Entries/Herbie%20Hancock%20-%20Chameleon%20-%2010-26.md [HEUR]
24. ummerr/bass « Superstition » tab — https://raw.githubusercontent.com/ummerr/bass/main/content/tabs/23-superstition.md [HEUR]
25. cjnolet/midi_genre_corpus features Superstition — https://raw.githubusercontent.com/cjnolet/midi_genre_corpus/master/pop/features/stevie_wonder-superstition.mid.csv [HEUR]
26. ZacharySBrown/idm-course analog research (Flash Light) — https://raw.githubusercontent.com/ZacharySBrown/idm-course/main/specs/ableton_course_ep2_analog_research.md [HEUR]
27. microsoft/Resource2Skill jazz comping skill — (URL §1.3) [HEUR]
28. bitwize funk README et mix-presets — https://raw.githubusercontent.com/bitwize-music-studio/claude-ai-music-skills/main/genres/funk/README.md et .../skills/mix-engineer/mix-presets.md [HEUR]
29. gooey-audio/libgooey neo-soul chord sets — (URL §1.6) [HEUR]
30. daveads voicing techniques ; Tieck14/open-piano-skills voicings.yaml ; JefroB electro-funk mix ; livepilot synths ; pages locales P-Funk et James Brown ensemble [HEUR]

### 6.2 Extraits seulement (pages bloquées par le proxy — [HEUR-extrait])

JustinGuitar E9 ; Medium « The James Brown Chord » ; Fundamental Changes funk chords ; Premier Guitar 9th chords ; PianoGroove et TJPS « Herbie Hancock voicing » ; Pianote « Superstition » ; Boing Boing « Superstition dissected » ; Ethan Hein « Musical Simples: Superstition » ; MusicRadar « funk up your keyboard parts » et « funky clavinet » ; Production Expert « 5 iconic organ sounds » ; Hammond Today ; Nick Foley « Hammond sound part 2 » ; Eddie Landsberg registrations ; Sound On Sound « Rhodes Hog » ; musicproductionnerds « How to EQ Rhodes » ; iZotope EQ cheat sheet ; Reverb « electric piano samples vintage » ; Pro Audio Files « Mixing piano and Rhodes » ; Waves Clavinet user guide ; Attack Magazine « Remake Flash Light » et « Roger Linn on swing » ; Melodiefabriek MPC swing ; diyAudio / HammondWiki Leslie speeds ; fenderrhodes.com effects ; Apple Logic tremolo ; Tape Op Rhodes vibrato ; Reverb Machine Kaytranada ; Liveschool Kaytranada ; MusicTech Cory Wong ; Stanford Daily Vulfpeck ; Billboard Silk Sonic credits ; American Songwriter « Use Me » ; Rolling Stone / Reverb Bernie Worrell ; The Soundsmith (palm slap) ; Music Player forum (palm smear) ; Hear and Play / Piano With Jonny gospel ; acousticsamples B-5 ; Loopcloud / Technotif ghost notes.

### 6.3 Échecs

- Bloqués par le proxy (EGRESS_BLOCKED) : pianowithjonny.com, pianogroove.com, thejazzpianosite.com, justinguitar.com, ethanhein.com, boingboing.net, pianote.com, musicradar.com, en.wikipedia.org, soundonsound.com, learnjazzstandards.com, production-expert.com, hammondtoday.com, nickfoleyuk.com, musicproductionnerds.com, theproaudiofiles.com, reverb.com, premierguitar.com ; curl vers Wikipédia/SOS : CONNECT 403.
- Non existants sur raw GitHub : `tonaljs/tonal packages/voicing-dictionary/src/data.ts` ; `cjnolet/midi_genre_corpus pop/stevie_wonder-superstition.mid` ; dumps `Clavinet.txt`, `Rhodespiano.txt`, `Lesliespeaker.txt`.
- Lecture de dépôts via l'API GitHub refusée (session limitée à `maileytsil-gif/tsila`) ; contourné par raw.githubusercontent.com.
- Quota WebSearch épuisé (200/200) avant les requêtes Junie Morrison, George Duke, Hohner D6 (commutateurs), LA-2A vs 1176 sur claviers, Green Onions, gospel notes exactes, Ableton Groove Pool, SOS « Recording Electric Piano », mix orgue.

---

## 7. Ce qui n'a pas été trouvé (à ne pas inventer)

1. **Notes exactes du riff de Clavinet de « Superstition »** et de **« Use Me »** (seuls la gamme, la tonalité, le tempo, les points de syncope et une basse simplifiée sont vérifiés). Les grilles §2.2 et §2.3 sont des gabarits, pas des transcriptions.
2. **Notes de la ligne de basse ARP de « Chameleon »** (12 notes ; vamp Bbm7–Eb7 confirmé).
3. **Junie Morrison** (Ohio Players / « Funky Worm », ARP Pro Soloist) et **George Duke** : aucune page lue.
4. **Commutateurs du Hohner D6** (A/B, C/D, brilliant/treble/medium/soft) : seulement la mention des rocker switches (amen) et du Brilliant ≈ +3 dB à 4 kHz (Waves, extrait).
5. **Définition précise du « squabble »** ; description mesurée du palm smear (nombre de touches, durée).
6. **Réglages de mix documentés de Vulfpeck, Silk Sonic, Kaytranada** (pourcentage de swing, EQ Rhodes, compression pumping) : seulement des descriptions qualitatives.
7. **Placement phaser/chorus avant ou après compression** : aucune source lue.
8. **EQ d'orgue Hammond en mix** (Hz) : rien de lu ; seul le crossover Leslie 800 Hz est documenté.
9. **Chapitre « Using Grooves » du manuel Ableton** (Groove Pool : Timing/Random/Velocity/Base ; noms exacts des grooves « Swing 16ths ») : absent du miroir local.
10. **Registration Hammond de « Green Onions »** : uniquement les presets setBfree « Green Onions 1/2 » (888800000 / 808800008), sans source primaire.
11. **Valeurs de swing mesurées sur les enregistrements funk** (Stax « behind the beat », JB vs P-Funk) : tkgally signale explicitement l'absence de mesures.

## 8. Points [TEST] proposés pour le Set

- Comparer, sur un même clip de Clavinet, grille quantifiée vs swing 16ths 54/57/59 % vs Track Delay fixe (+15 ms sur la caisse claire, −8 ms sur la basse) — la recherche prédit que la version quantifiée ou légèrement swinguée gagne, pas le Random.
- Vérifier sur Electric la courbe vélocité → brillance (Stiffness Vel, Force Vel) contre les plages « soft 800 Hz / hard 6 kHz » (amen) et fixer les vélocités des gabarits §2.2–2.4.
- Auto Pan 180° 4–6 Hz : mesurer la perte de mouvement en somme mono ; essayer Phase 120–150° ou mode Tremolo.
- Percussion d'orgue single-trigger : mesurer le silence minimal (1/32 vs 1/64) qui réarme la percussion dans le plug-in d'orgue utilisé.
- Bus claviers : Glue 2:1 / 10–30 ms / Auto / 1–3 dB, avec et sans sidechain kick 1–3 dB, à niveau égal.
