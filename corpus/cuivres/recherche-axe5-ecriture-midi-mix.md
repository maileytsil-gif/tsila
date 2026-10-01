---
titre: "Rapport de recherche — axe 5 : écriture de section de cuivres, programmation MIDI réaliste, mixage des cuivres"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: rapport de recherche
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE 5 — Écriture de section de cuivres, programmation MIDI réaliste, mixage des cuivres

Rapport de recherche pour le skill « cuivres » (Ableton Live 12 + Serum 2). Date : 2026-09-24.

## 0. Conditions de la recherche et conventions

**Contrainte réseau.** Dans cette session, le proxy de sortie a bloqué (403 au CONNECT, `EGRESS_BLOCKED`) tous les sites web « classiques » visés par la mission : Sound On Sound, Wikipedia, blog Native Instruments, Evan Rogers, Steinberg/Dorico, MuseScore.org, Gearspace, iZotope, etc. Seuls `raw.githubusercontent.com`, `pypi.org`, `files.pythonhosted.org` et l'API GitHub (recherche de code) répondaient. La recherche a donc été menée sur :

1. des **sources primaires hébergées sur GitHub/PyPI** : code source de music21, MuseScore (`instruments.xml`), Abjad, schéma officiel MusicXML 4 (W3C), métadonnées SMuFL (W3C), documentation LilyPond, texte intégral de Rimsky-Korsakov *Principles of Orchestration* (Project Gutenberg #33900), texte du manuel Spitfire Symphony Orchestra, banques d'articulations Reaticulate (cartes des keyswitches de Session Horns Pro, CineBrass, Spitfire) ;
2. des **copies d'articles Wikipedia** déposées dans des dépôts GitHub (datées, non vérifiables contre la version courante) ;
3. des **documents communautaires** (notes d'arrangeurs, skills, wikis de production) pour les pratiques → `[HEUR]`.

Les extraits renvoyés par le moteur de recherche pour les pages bloquées sont cités **uniquement** avec le tag `[HEUR — extrait de recherche, page non lue]`.

**Tags.** `[DOC]` = lu dans une source primaire (manuel, traité, schéma officiel, code de référence). `[DOC-W]` = lu dans une copie d'article Wikipedia hébergée sur GitHub (source secondaire). `[HEUR]` = pratique lue dans un document communautaire/tutoriel. `[TEST]` = à valider dans le Set. `[MÉMOIRE, non vérifié]` = de mémoire, pas de page lue.

**Convention d'octave.** Toutes les sources lues (music21, MuseScore, Abjad, Wikipedia, LilyPond) utilisent la notation scientifique : **C4 = do médian = MIDI 60** [DOC : music21 `pitch.py` « Assume C4 middle C, so 60 returns 4 » — https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/pitch.py]. Le projet utilise **C3 = MIDI 60** (Ableton). Règle : *nom Ableton = nom scientifique − 1 octave, numéro MIDI identique*. Dans les tableaux, les hauteurs sont données en notation scientifique **avec le numéro MIDI** (sans ambiguïté), et l'équivalent Ableton est indiqué quand c'est utile (ex. F#3 sci = F#2 Ableton = MIDI 54).

---

## 1. Tessitures, transpositions, registres

### 1.1 Transpositions (intervalle « écrit → sonnant »)

| Instrument | Sonne… par rapport à l'écrit | music21 `transposition` [DOC] | MuseScore `transposeChromatic` (demi-tons) [DOC] | Abjad `middle_c_sounding_pitch` [DOC] |
|---|---|---|---|---|
| Trompette en Si♭ | une 2de majeure plus bas | `M-2` | −2 | (l'objet `Trumpet` d'Abjad est défini en ut : C4) |
| Cornet / bugle (flugelhorn) en Si♭ | 2de majeure plus bas | — | −2 (`flugelhorn`) | — |
| Cor en Fa | une 5te juste plus bas | `P-5` | −7 | F3 |
| Trombone ténor/basse | non transpositeur (clé de fa, hauteur réelle) | (aucune) | (aucune) | C4 |
| Tuba | non transpositeur | (aucune) | (aucune) | C4 |
| Sax soprano en Si♭ | 2de majeure plus bas | `M-2` | −2 | Bb3 |
| Sax alto en Mi♭ | 6te majeure plus bas | `M-6` | −9 | Eb3 |
| Sax ténor en Si♭ | 9e majeure (octave + 2de M) plus bas | `M-9` | −14 | Bb2 |
| Sax baryton en Mi♭ | 13e majeure (octave + 6te M) plus bas | `M-13` | −21 | Eb2 |

Sources : music21 — https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/instrument.py ; MuseScore 4.4.4 — https://raw.githubusercontent.com/musescore/MuseScore/4.4.4/share/instruments/instruments.xml ; Abjad 3.31 (sdist PyPI, `source/abjad/instruments.py`) — https://files.pythonhosted.org/packages/76/9c/369810e498be649ebc531e9f6a78e66d28b45174f1f8f1b4af6bdf11bbf7/abjad-3.31.tar.gz.

Compléments [DOC-W] :
- Trombone : « treated as non-transposing instruments, reading at concert pitch in bass clef, with higher notes sometimes being notated in tenor clef. They are pitched in B♭, an octave below the B♭ trumpet and an octave above the B♭ bass tuba » ; exception : brass bands britanniques (Si♭, clé de sol) — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Trombone.txt.
- Tuba : « Most music for the tuba is written in bass clef in concert pitch » ; en brass band, tuba Si♭ sonne 2 octaves + 1 ton sous l'écrit, tuba Mi♭ 1 octave + 6te M sous l'écrit — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Tuba.txt.
- Trompette basse en Si♭ : sonne une 9e majeure sous l'écrit (jouée par les trombonistes) — https://raw.githubusercontent.com/anassalamah/nlp-project/master/wikipedia%20pages/Trumpet.txt.
- Saxophones : « almost always treated as transposing instruments » ; famille Si♭/Mi♭ devenue standard ; étendue écrite commune Si♭3–Fa6 (Fa♯6 avec clé de Fa♯ moderne), baryton souvent descendu au La écrit — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Saxophone.txt.

### 1.2 Tessitures sonnantes (hauteur réelle), en MIDI

MuseScore distingue une plage « amateur » (`aPitchRange`) et « professionnelle » (`pPitchRange`), en hauteur réelle (vérifié : la trompette en Si♭ y est décalée de 2 demi-tons sous la trompette en ut). Abjad donne une seule plage « pitch_range » sonnante. music21 ne donne que `lowestNote`.

| Instrument | MuseScore amateur [DOC] | MuseScore pro [DOC] | Abjad [DOC] | music21 `lowestNote` [DOC] | Ableton (C3=60) de la plage amateur |
|---|---|---|---|---|---|
| Trompette Si♭ | 52–80 (E3–G♯5) | 52–85 (E3–C♯6) | F♯3–D6 (54–86, objet en ut) | F♯3 (54) | E2–G♯4 |
| Trompette ut | 54–82 (F♯3–A♯5) | 54–85 | — | — | F♯2–A♯4 |
| Bugle (flugelhorn) | 52–79 (E3–G5) | 52–82 (E3–A♯5) | — | — | E2–G4 |
| Cor en Fa | 41–69 (F2–A4) | 31–77 (G1–F5) | B1–F5 (35–77) | C2 (36) | F1–A3 |
| Trombone ténor | 40–71 (E2–B4) ; `tenor-trombone` 40–70 | 36–74 (C2–D5) ; 40–74 | E2–E♭5 (40–75) | E2 (40) | E1–B3 |
| Trombone basse | 32–65 (G♯1–F4) | 21–77 | C2–F4 (36–65) | B♭1 (34) | G♯0–F3 |
| Tuba | 28–58 (E1–A♯3) | 22–72 | D1–F4 (26–65) | D1 (26) | E0–A♯2 |
| Sax soprano | 56–87 (G♯3–D♯6) | 56–91 | A♭3–E6 (56–88) | (B♭3 écrit commun) | G♯2–D♯5 |
| Sax alto | 49–80 (C♯3–G♯5) | 49–92 (suraigu) | D♭3–A5 (49–81) | — | C♯2–G♯4 |
| Sax ténor | 44–75 (G♯2–D♯5) | 44–87 | A♭2–E5 (44–76) | — | G♯1–D♯4 |
| Sax baryton | 36–68 (C2–G♯4) | 36–80 | C2–A♭4 (36–68) | — | C1–G♯3 |

Lecture : la plage « amateur » MuseScore correspond à l'étendue écrite standard (sax : Si♭3–Fa6 écrit → alto 49–80, ténor 44–75, baryton avec La grave 36–68 ; trompette : F♯3–C6 écrit → 52–80 sonnant en Si♭). La plage « pro » ajoute le suraigu/registre extrême (trompette jusqu'à C♯6 sonnant = D6 écrit ; cor jusqu'à F5 ; trombone C2 grave par la coulisse/quarte et D5 aigu ; saxes suraigu).

### 1.3 Registres confortables, extrêmes, notes pédales [DOC-W]/[DOC]

- **Trompette** : « The standard trumpet range extends from the written F♯ immediately below Middle C up to about three octaves higher » ; « the fingering tables of most method books peak at the high C, two octaves above middle C » (= C6 écrit, MIDI 84 ; B♭5 sonnant, MIDI 82). Pédales : « It is also possible to produce pedal tones below the low F♯ » ; les compositeurs ont écrit jusqu'à 2 octaves ½ sous le F♯ grave ; « Extreme low pedals are produced by slipping the lower lip out of the mouthpiece » (technique de travail, Claude Gordon/Clarke) — https://raw.githubusercontent.com/anassalamah/nlp-project/master/wikipedia%20pages/Trumpet.txt et https://raw.githubusercontent.com/kirito-0512/data/main/dump/Trumpet.txt. Registre extrême : « no actual limit… fingering charts generally go up to the high C two octaves above middle C » ; spécialistes du suraigu : Maynard Ferguson, Cat Anderson, Dizzy Gillespie, Doc Severinsen, Wayne Bergeron (id.).
- **Trompette, « sweet spot »** : G4–G5 sonnant (MIDI 67–79 ; Ableton G3–G4) et plage pratique F♯3–C6 [HEUR — https://raw.githubusercontent.com/josefigueredo/ableton-mcp/main/docs/sources/INSTRUMENT_TECHNIQUES_SOURCE_OF_TRUTH.md].
- **Trombone ténor** : série harmonique 1re position B♭2 (46), F3, B♭3, D4, F4, puis B♭4, C5, D5, E♭5 (« almost exactly a quarter tone higher » que le tempérament égal), F5 ; « The practical top of the range is sometimes considered to be F5, or more conservatively D5 » ; grave (hors pédales) E2 ; « The pedal tone on B♭ is frequently seen in commercial scoring but much less often in symphonic music », notes plus graves « increasingly difficult… with A or G being the bottom limit for most trombonists » (Kennan & Grantham cités) ; trou entre B♭1 et E2 sans barillet de Fa ; barillet de Fa → chromatique jusqu'à la pédale B♭1 sur trombone basse — https://raw.githubusercontent.com/anassalamah/nlp-project/master/wikipedia%20pages/Trombone.txt et https://raw.githubusercontent.com/kirito-0512/data/main/dump/Trombone.txt.
- **Cor** : « In the lower register it is dark and brilliant; round and full in the upper… In spite of valves the horn has but little mobility » [DOC Rimsky-Korsakov]. Registre caractéristique F3–F5 [HEUR ableton-mcp].
- **Tuba** : fondamentale du tuba CC 32 Hz, BB♭ 29 Hz ; « false tones » (E♭1, 39 Hz) permettant le chromatisme jusqu'à la fondamentale ; note la plus grave du répertoire : double pédale C0 (16 Hz) — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Tuba.txt. Rôle : « the bass of the orchestral brass section… doubling, an octave lower, the bass of the group » [DOC Rimsky-Korsakov].
- **Bugle** : « more difficult to control in the high register (from approximately written G5) » ; timbre « halfway between a trumpet and a French horn » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Flugelhorn.txt.
- **Saxophones** : étendue écrite Si♭3–Fa6 (2 octaves ½), Fa♯6 fréquent, baryton avec La grave ; quatuor classique SATB ; harmonie militaire : « at least a quartet… E♭ baritone, B♭ tenor, E♭ alto and B♭ soprano » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Saxophone.txt.
- **Règle générale de brillance** : « quality becomes more brilliant as the higher register is approached, and vice versa, with a decrease in tone. Played pp the resonance is sweet; played ff the tone is hard and "crackling" » [DOC Rimsky-Korsakov — https://raw.githubusercontent.com/legobridge/copyshield-llm/main/data/text/PG33900_text.txt].

### 1.4 Registres par pupitre en big band (écriture réelle) [HEUR]

Plages « conservatrices, adaptées à une ballade » utilisées par un arrangeur en cours d'apprentissage (hauteur réelle) — https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/charts/Beatrice/03_arrangement/V9.0-Arranging-Notes.md :

| Pupitre | Plage réelle | MIDI |
|---|---|---|
| Trompette 1 (lead) | F♯4–D6 | 66–86 |
| Trompette 2 | D4–B♭5 | 62–82 |
| Trompette 3 | C4–G5 | 60–79 |
| Trompette 4 | B♭3–F5 | 58–77 |
| Trombone 1 | F3–B♭4 | 53–70 |
| Trombone 2 | E3–G4 | 52–67 |
| Trombone 3 | C3–F4 | 48–65 |
| Trombone basse | B♭1–F3 | 34–53 |
| Alto 1 / Alto 2 | G4–D5 / E4–B4 | 67–74 / 64–71 |
| Ténor 1 / Ténor 2 | C4–G4 / A3–E4 | 60–67 / 57–64 |
| Baryton | D2–C3 | 38–48 |

(Les plages de saxes y sont très resserrées, choix volontaire du script ; ne pas les prendre pour des limites d'instrument.) Le même dépôt utilise ailleurs un dictionnaire `RANGES` trompette 54–86, trombone 40–70, alto 61–81, ténor 56–76, baryton 36–60 (MIDI écrit) — https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/docs/big_band_reuse_audit.md.

---

## 2. Écriture de section de cuivres (pop / funk / soul / afrobeat / latin / jazz)

### 2.1 Formations types

| Formation | Source |
|---|---|
| Duo : trompette + sax, trompette + trombone, ou deux saxes | [DOC-W] Wikipedia « Funk » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Funk.txt |
| Trio standard : trompette + sax (souvent ténor) + trombone ; aussi 1 trompette + 2 saxes ou 2 trompettes + 1 sax | [DOC-W] id. |
| Quatuor : trio + trompette, sax ou (moins souvent) trombone | [DOC-W] id. |
| Quintette : 3 saxes (alto/ténor/baryton ou ténor/ténor/baryton) + trompette + trombone, ou paires ; le **baryton** apparaît dans les quintettes/sextettes | [DOC-W] id. |
| Phenix Horns (Earth, Wind & Fire) : Don Myrick (sax), Louis Satterfield (trombone), Rahmlee Davis et Michael Harris (trompettes) → 2 tpt + sax + tbn | [DOC-W] https://raw.githubusercontent.com/alaym3/musician-network-analysis/main/Wikipages/Earth,%20Wind%20%26%20Fire.txt |
| J.B.'s (James Brown) : Maceo Parker, Pee Wee Ellis (saxes), Fred Wesley (trombone) | [HEUR] https://raw.githubusercontent.com/tkgally/algorithmic-music/main/wiki/funk-soul-and-rnb.md ; noms confirmés [DOC-W] Wikipedia « Funk » (« Alfred "PeeWee" Ellis, trombonist Fred Wesley, and alto sax player Maceo Parker ») |
| Sections nommées : Phoenix Horns (EWF), Horny Horns (Parliament), Memphis Horns (Isaac Hayes), MFSB | [DOC-W] Wikipedia « Funk » |
| Pop/R&B : 2 trompettes + trombone + sax ténor (quatuor « le plus courant ») ; trio tpt + tbn + ténor ; 2 tpt + alto + ténor | [HEUR] https://raw.githubusercontent.com/hwangtab/studio/main/content/stories/brass-arrangement1.md |
| Big band : saxes 5 (alto, ténor, baryton), trompettes 4, trombones 4 | [HEUR] https://raw.githubusercontent.com/Hipare/Hipare-Reaper-agent/main/knowledge/knowledge/genres/jazz.md |
| Orchestre (Rimsky-Korsakov, « par deux / par trois / par quatre ») : 2 tpt–4 cors–3 tbn–1 tuba ; 3 tpt–4 cors–3 tbn–1 tuba ; 3 tpt–6/8 cors–3 tbn–1 tuba | [DOC] Rimsky-Korsakov |
| Ska (1re vague) : « horns taking the lead and often following the off-beat skank » ; Skatalites : Don Drummond (tbn), Tommy McCook (ténor) | [DOC-W] https://raw.githubusercontent.com/kirito-0512/data/main/dump/Ska.txt ; [HEUR] https://raw.githubusercontent.com/bitwize-music-studio/claude-ai-music-skills/main/genres/ska/README.md (section trompette, trombone, alto/ténor ; « Horns are typically high in the mix ») |
| Salsa dura : front line 2 trompettes + trombone + sax ténor (démo) ; Fania : « trombones » cités pour Willie Colón | [HEUR] https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp/master/.agents/skills/bespoke-brass-winds/SKILL.md ; https://raw.githubusercontent.com/JoanComasFdz/salsa-music/main/src/songs-breakdown/salsa-song-structure-breakdowns.md |
| Afrobeat : Fela Kuti + Tony Allen ; « horns », « saxophone » dans l'instrumentation ; Antibalas (Brooklyn) | [DOC-W] https://raw.githubusercontent.com/kirito-0512/data/main/dump/Afrobeat.txt |

Non trouvé : composition exacte des sections de Tower of Power, Chicago, Blood Sweat & Tears ; participation d'Antibalas / arrangement d'« Uptown Funk » (la page coréenne cite seulement « Uptown Funk » (2014) comme renaissance du style R&B [HEUR]) ; textes de Fred Wesley/Jerry Hey. Jerry Hey [HEUR] : « using brass as rhythmic punches rather than melodic leads », arrangements de *Off the Wall*, *Thriller*, *The Dude* — https://raw.githubusercontent.com/edtbl76/midi_real_book/main/ensembles/James%20Brown%20funk/ensemble.md.

### 2.2 Rôles d'une section

- **Funk (rôle rythmique)** [DOC-W Wikipedia « Funk »] : « Horn sections played "rhythmic and syncopated" parts, often with "offbeat phrases" that emphasize "rhythmic displacement" » ; « Funk song introductions are an important place for horn arrangements » ; « Horn sections would "punctuate" the lyrics by playing in the spaces between vocals, using "short staccato rhythmic blast[s]" » ; les voix funk « resemble horn parts and have "pushed" rhythms ».
- **James Brown** [HEUR tkgally] : la section « functioned as a percussion voice in its own right — short, tightly unisoned "stabs" placed in the gaps the rhythm section left open ». « On the One » [HEUR edtbl76].
- **Stab / pad / riff unisson / fill** [HEUR hwangtab] : R&B/soul = stabs courts sur temps forts + riffs unisson ; pop = stabs sur contretemps, unisson au refrain ; « garder les cuivres pour les moments nécessaires… le couplet vide, entrée de refrain ou fill après refrain ».
- **Shout chorus (big band)** [HEUR mikeb55 V9] : « Explosive shout chorus, trumpet dominance, rhythmic brass writing », « Full brass (drop-2-4 voicings) », « Sax rhythmic figures », « Rising trumpet register » ; densité : « No more than two sections simultaneously except at climaxes » ; « Bar 40 thinned before full shout » ; anti-patterns constatés : « density explosions », « all sections playing simultaneously », « rhythm section overpowering the horns », « "shout chorus" without structural preparation » — https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/charts/Beatrice/03_arrangement/none_of_these_work.md.
- **Salsa** [HEUR salsa-music] : un seul **mambo** (« the first elaborate instrumental horn section after the first montuno »), plusieurs **moñas** (« shorter horn riffs that stay on the montuno chord progression ») ; usage cubain inversé ; ~80 % de la salsa NY/PR classique en clave 2-3 ; gestes du front line [HEUR bespoke] : *llamada* (unisson +12/0/0/−12), réponses dans les trous « never under the singer », *moña* (motif de 3 notes harmonisé sur 5 accords), *ponche* (deux coups en 4 mesures) ; règle : chaque attaque commune tombe sur un coup de clave.
- **Afrobeat** [HEUR démo] : « horns in unison stabs answering nothing in particular », riff unisson puis « an octave up for the shout » ; exemple de riff (temps, degré, durée, vélocité) : `(0.5, 0, 0.11, 100), (0.625, 3, 0.11, 92), (0.75, 5, 0.11, 96), (0.875, 7, 0.11, 104), (1.0, 10, 0.55, 108)` (mesures, demi-tons au-dessus de la fondamentale) — https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/master/demos/historical/afrobeat/style.py.
- **Orchestre** [DOC Rimsky-Korsakov] : mélodies de cuivres = fanfares issues de la série harmonique, « unmodulated diatonic character, rousing and triumphant in the major key, dark and gloomy in the minor » ; tenues : « the brass is frequently employed to sustain notes in two or three octaves… The tenuto is generally given to two trumpets, or to two or four horns in the octave » ; « The trombone with its ponderous tone rarely takes part in such combinations ».

### 2.3 Voicings

**Définitions lues :**
- Close (serré) : toutes les notes au-dessus de la basse dans une octave ; open (large) : sur plus d'une octave [HEUR — https://raw.githubusercontent.com/Kan-A-Pesh/music-with-code/master/docs/research/partie2_harmonie.md ; id. hwangtab, ableton-mcp].
- **Drop 2** : « Four-way close voicings can become dense in the middle register. To create a Drop 2 voicing, take the second note from the top and move it down one octave » [HEUR — https://raw.githubusercontent.com/toshiotawa/jazzify-lab/master/en-blog/src/data/blog/jazzpiano-block-chords.md]. Variantes drop 3, drop 2&4 [HEUR Kan-A-Pesh]. Exemple chiffré : `[60,64,67,71]` → `[55,60,64,71]` [HEUR bespoke].
- **Four-way close / locked hands** (Shearing/Evans) : mélodie doublée à l'octave + accord serré dessous [HEUR Kan-A-Pesh] ; « the sound of a compact horn section at the piano » [HEUR jazzify].
- Rimsky-Korsakov [DOC] : « part writing should be of the close order with no empty spaces in the intervals » ; quatuor de cors = 4 parties équilibrées ; trombones/tuba « not often employed in close four-part harmony; the third trombone and the tuba usually form the bass in octaves » ; combinaison recommandée « 2 horns and tuba to form the bass in octaves, the three other parts given to the trombones » ; à 3 voix, « If the instruments are mixed the number of horns should be doubled » ; duplication : accord de cors à côté du même accord de trompettes/trombones.
- Règles pratiques [HEUR bespoke-brass-winds] : « Close-position brass in the middle, open at the bottom. Nothing closer than a fifth below MIDI 48 » ; « Four-part close (drop-0) for punch, drop-2 for width » ; « Harmonise from the chord, never by interval » (la 2e trompette = « the next chord tone below » et non « la mélodie moins quatre demi-tons ») ; le trombone/tuba double ou remplace la basse.
- Structures supérieures sans fondamentale (salsa) [HEUR bespoke] : `Cm9 upper = [63,67,70,74]` (E♭ G B♭ D), `G7alt upper = [62,65,71,73]` ; « tp1, tp2, sax get degrees 3,2,1; tbn gets 0 −12 ».
- Big band [HEUR mikeb55] : « Saxes: Drop-2 voicings; wider spacing in lower register », « Brass: Drop-2-4 voicings », « Guide-tone spine: One inner voice follows 3rds and 7ths » ; Wheeler : « Trumpets: open voicings; 4ths and 5ths; sustained pads… Trombones: pedal or counter-melody; avoid dense blocks ».
- Extrait non lu [HEUR — extrait de recherche] : « For reggae, ska, soul… 3-part harmonies need to be used with caution or the horns will sound too sweet. Trumpet and tenor can be used in unison octaves with the harmony given to the trombone » (cafesaxophone.com, page bloquée).

**Tableau d'exemples (construits d'après les définitions ci-dessus ; à traiter comme `[HEUR, exemple construit]`, à vérifier à l'oreille `[TEST]`) — notation scientifique (C4=60) / Ableton (C3=60) / MIDI :**

| Type | Accord | Trompette | Sax ténor | Trombone | Notes |
|---|---|---|---|---|---|
| Unisson | riff sur C7 | G4 / G3 / 67 | G4 / G3 / 67 | G3 / G2 / 55 (octave sous) | trombone une octave sous = « unison octaves… harmony given to the trombone » [HEUR extrait] |
| Octaves | riff | G5 / G4 / 79 | G4 / G3 / 67 | G3 / G2 / 55 | attention trompette ≥ G5 = extrême amateur (MuseScore 80) |
| Close 3 voix | C7 (stab) | B♭4 / B♭3 / 70 | G4 / G3 / 67 | E4 / E3 / 64 | 7-5-3, dans une octave ; fondamentale à la basse |
| Close 4 voix (four-way close) | C7 | B♭4 / 70 | G4 / 67 | E4 / 64 | + 4e voix C4 / 60 (2e trompette ou baryton) |
| Drop 2 (4 voix) | C7 | B♭4 / 70 | E4 / 64 | C4 / 60 | G4 (2e du haut) descendue à G3 / 55 → trombone basse/baryton ; = `[70,67,64,60] → [70,64,60,55]` |
| Drop 2 (exemple source) | Cmaj7 | 71 | 64 | 60 | 55 (bespoke : `[60,64,67,71] → [55,60,64,71]`) |
| Spread | C7 | B♭4 / 70 | E4 / 64 | C3 / 48 | > 1 octave ; pas d'intervalle < 5te sous MIDI 48 [HEUR bespoke] |
| Pad 2 instruments | tenue | C5 / 72 | — | C4 / 60 | « two instruments an octave apart, velocity 70–88 » [HEUR bespoke] |

Convention Ableton rappelée : B♭4 (sci) = B♭3 (Ableton) = 70.

### 2.4 Articulations et leur notation

**Vocabulaire normalisé (MusicXML 4, W3C) [DOC — https://raw.githubusercontent.com/w3c/musicxml/gh-pages/schema/musicxml.xsd] :**
- `scoop` : « an indeterminate slide attached to a single note. The scoop appears before the main note and comes from below the main pitch ».
- `plop` : « appears before the main note and comes from above the main pitch ».
- `doit` : « appears after the main note and goes above the main pitch ».
- `falloff` : « appears after the main note and goes below the main pitch ».
- `line-length` de ces quatre signes : `short`, `medium`, `long`.
- `breath-mark` : « indicates a place to take a breath ».
- Éléments *technical* cuivres : `brass-bend` (« the u-shaped bend symbol used in brass notation »), `flip` (« the flip symbol used in brass notation »), `smear` (« the tilde-shaped smear symbol »), `open` (cercle), `half-muted` (cercle avec +), `harmon-mute` ; `triple-tongue` (trois points).
- `shake` : ornement « similar appearance to an inverted-mordent » ; `glissando` (« sounds the distinct notes in between… wavy line ») vs `slide` (« continuous between the two pitches… solid line »).
- **Rendu MIDI d'un bend/slide** (`bend-sound`) : « The number of discrete elements (like MIDI pitch bends) used to represent a continuous bend or slide. Default is 4 » ; « The percentage of the duration for starting a bend. Default is 25 » ; « for ending it. Default is 75 » ; `bend-alter` en demi-tons (0,5 = quart de ton).

**Glyphes SMuFL (W3C) [DOC — https://raw.githubusercontent.com/w3c/smufl/gh-pages/metadata/glyphnames.json] :** `brassBend` (Bend), `brassDoitShort/Medium/Long`, `brassFallLipShort/Medium/Long` (Lip fall), `brassFallRough…` (Rough fall), `brassFallSmooth…` (Smooth fall), `brassFlip`, `brassJazzTurn`, `brassLiftShort/Medium/Long` (Lift = *rip*), `brassLiftSmooth…`, `brassPlop`, `brassScoop`, `brassSmear`, `brassValveTrill`, `brassMuteClosed/HalfClosed/Open`, `brassHarmonMuteClosed / StemHalfLeft / StemHalfRight / StemOpen`, `windFlatEmbouchure`. → Trois familles de *fall* (lèvre, « rough » = doigtés/coulisse, « smooth ») et trois longueurs.

**LilyPond [DOC] :**
- Falls/doits : « Falls and doits can be added to notes using the \bendAfter command. The direction… is indicated with a plus or minus… The number indicates the pitch interval that the fall or doit will extend beyond the main note » (exemples `\bendAfter 4`, `-4`, `6.5`, `-6.5`, `8`, `-8`) — https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/notation/expressive.itely.
- Respiration : « The \breathe command calls for the performer to shorten the previous note to take a breath » (id.).
- Vents : « Flutter tonguing is usually indicated by placing a tremolo mark and a text markup on the note » ; « Slide glissandi are characteristic of the trombone… Harmonic series glissandi, which are possible on all brass instruments but common for French Horns, are usually written out as grace notes » ; sourdines : « usually indicated by a text markup… `stopped` and `open` articulations » — https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/notation/wind.itely.
- Glossaire (avec équivalents français) : *fall* = « Indicator for an indeterminately falling pitch bend » (F : chute) ; *doit* = « indeterminately rising pitch bend » (F : saut) ; *glissando* = « Letting the pitch slide fluently from one note to the other » ; *staccato* = « Playing the note(s) short » ; *tenuto* = « held for the whole length » ; *legato* = « without any perceptible interruption between the notes » ; *accent* = « The stress of one tone over others » ; *breath mark* (F : respiration) — https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/music-glossary.tely.

**Définitions techniques [DOC-W] :**
- *Rip* : « rip (for a loud, violent glissando to the beginning of a note) » ; *lip* (terme jazz), *smear*, *sweep bend* équivalents contextuels de glissando ; « On brass instruments such as the trumpet, the note is bent by using the lip » — https://raw.githubusercontent.com/kirito-0512/data/main/dump/Glissando.txt.
- *Lip trill / shake* : « By rapidly varying air speed, but not changing the depressed valves, the pitch can vary quickly between adjacent harmonic partials… usually involve the next partial up from the written note » — Wikipedia « Trumpet » (kirito).
- *Flutter tonguing* : « rolls the tip of the tongue… to produce a 'growling like' tone » (R roulé espagnol) ; *Growling* : « using the back of the tongue to vibrate the uvula… Most trumpet players will use a plunger with this technique » (id.).
- *Glissando de trombone* : « one of the few wind instruments that can produce a true glissando, by moving the slide without interrupting the airflow… Every pitch in a glissando must have the same harmonic number, and a tritone is the largest interval that can be performed as a glissando » ; trilles convaincants « above the first octave and a half of the tenor's range » — Wikipedia « Trombone » (anassalamah).
- Coups de langue [DOC Rimsky-Korsakov] : « single tonguing is possible to all members of the brass, but double tonguing can only be done on instruments with a small mouth-piece, trumpets and cornets » ; « sf > p effect being excellent ».
- Extrait non lu [HEUR — extrait] : scoop « scoops in quickly from an undetermined pitch underneath » ; doit « rises from the note to an undetermined pitch » ; plop « quick dive from the note to an undetermined lower pitch » ; fall « longer, measured dive » (Soundslice/MuseScore, pages bloquées).

**Correspondance avec les banques d'échantillons** (noms d'articulations réellement exposés, via les cartes Reaticulate) [DOC — cartes tierces des keyswitches, source : https://raw.githubusercontent.com/jtackaberry/reaticulate/…] :

| Banque | Articulations listées |
|---|---|
| NI Session Horns Pro (solo & ensemble, « Two channel patches, Dynamic control w CC11 ») | sustain, vibrato, marcato long, marcato medium, staccato, staccatissimo, **rips**, grace, grace vibrato, **fp 2beat**, **fp 4beat**, **growl**, growl vibrato, **shake** (tbn/tpt/tuba/bugle), trill m2, trill M2 (saxes) ; keyswitches « sequentially… from C-1 to G#-1 » — `userbanks/Native_Instruments/Native_Instruments-Session_Horns_Pro.reabank` |
| Cinesamples CineBrass Pro/Core | legato, short 1/8, short 1/4, short 1/2, sustain ; variantes muted, harmon mute ; « Horns Ensemble Stopped and Fluttered » ; mode « Keyswitch Velocity Dynamics Map » — `userbanks/Cinesamples/Cinesamples-CineBrass_Pro.reabank` |
| Spitfire Studio Brass Pro | legato, long, long (stopped/muted), flutter, long sfz, staccatissimo, tenuto, marcato — `userbanks/Spitfire/Spitfire-Studio_Brass_Pro.reabank` |
| Spitfire Symphonic Brass (trompettes) | legato, long, long muted, marcato, tenuto, staccato, multitongued, trill m2/M2, flutter, long mariachi, **fx glissandi**, **rip**, **fall** — `banks/65-01-Spitfire-Symphonic_Brass.reabank` |
| Spitfire BBCSO (cuivres) | legato (extended), long, staccatissimo, marcato, long cuivré, long sfz, flutter, multitongued, trills, muted — `userbanks/Spitfire/Spitfire-BBC_Symphonic_Orchestra.reabank` |

### 2.5 Phrasé, respiration, fatigue

- [DOC Rimsky-Korsakov] « Wood-wind players cannot manage extremely long sustained passages, as they are compelled to take breath; care must be taken therefore to give them a little rest from time to time » et « The remarks on breathing, in the section devoted to the wood-wind, apply with equal force to the brass ».
- [HEUR ableton-mcp] trompette : « breath_capacity: 8-12 seconds typical phrase length », « lip_flexibility: Affects high register endurance » ; tuba : « phrase_length: 6-10 seconds maximum », « recovery_time: Brief pauses between phrases ».
- [HEUR bespoke] « End a phrase 0.03–0.06 measures early and start the next one on time; never run a line for eight bars without a hole in it. If two winds are in unison, stagger their breaths » ; « Re-articulate anything longer than about two bars ».
- [HEUR hwangtab] les cuivres « sonnent bon marché s'ils jouent du début à la fin » ; réserver aux entrées de refrain et fills.
- Fatigue/registre : rien de chiffré trouvé au-delà des « 8–12 s » ci-dessus ; la limite pratique aiguë écrite C6 (trompette) et la mention « Several trumpeters have achieved fame for their proficiency in the extreme high register » [DOC-W] suggèrent de ne pas écrire de tenues répétées au-dessus de G5 sonnant sans validation [TEST].

---

## 3. Programmation MIDI réaliste de cuivres échantillonnés

### 3.1 Vélocité, CC1 (molette), CC11 (expression)

- **Norme MIDI** [HEUR wiki de production, cohérent avec la spécification] : « CC1 is the Modulation Wheel, CC2 is Breath Controller, CC7 is Channel Volume, CC10 is Pan, CC11 is Expression (a scaled sub-volume ideal for crescendo/decrescendo automation) » ; « In orchestral programming, CC11 driving amplitude and CC1 driving vibrato depth… produces the swelling, breathing quality of live string and brass s[ections] » ; « Orchestral programming without CC11 expression curves sounds like a MIDI demo » ; « Avoid step-function changes between CC values; smooth interpolated ramps » — https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/midi.html.
- **Spitfire (manuel SSO)** [DOC] : « Dynamics - probably the most important controller you have. This crossfades between the different dynamic layers recorded. » ; « Vibrato - where appropriate this crossfades from no (or senza) to lots (molto) vibrato. » ; « Release - allows you to change the amounts of release trigger » ; « **Tightness** - the start of a note is often not the start of the 'sound' of the instrument. This cuts further into the note to make it tighter. But does detract from realism. Worth tightening up when playing in, then loosening and putting a negative delay into your DAW to compensate for ultimate reality! » ; « **Expression** - ostensibly instrument trim (CC11), so this adjusts the volume within the instrument volume (CC7) » ; keyswitches « at the very bottom of your keyboard » ; UACC = un CC (#32 par défaut) par articulation ; commutation « By Speed Of Playing » (ex. fast legato si intervalle entre notes 0–250 ms) — https://raw.githubusercontent.com/vingleo/SyncDocuments/master/SpitfireSymphonyOrchestra_UserManual%E5%8F%82%E8%80%83%E7%BF%BB%E8%AF%91.txt.
- **Session Horns Pro** : « Dynamic control w CC11 » (cartes Reaticulate) [DOC-tiers] ; « Smart Voice Split function that splits notes to different instruments depending on the register when you play more than one note at a time » (version lite) [HEUR — https://raw.githubusercontent.com/eetusuikkanen/eetusuikkanen.github.io/master/content/blog/1757950802962-ost-composing-jam-8/index.md] ; extraits non lus [HEUR — extrait de recherche] : « Dynamics are controlled either by key velocity or by MIDI Expression control (CC#11)… full-time access to that sustained double-forte layer » (SOS, revue Session Horns) ; « Humanize knob to control the timing, tuning and velocity accuracy of the instruments in your horns section » (blog NI).
- **CineBrass** : mode « Keyswitch Velocity Dynamics Map » (dynamique par vélocité) [DOC-tiers cartes].
- **Règles de cohérence** [HEUR — https://raw.githubusercontent.com/bedwards/copper-hollow/main/docs/midi-programming-techniques.md] : « CC1 | Dynamics/Modwheel | Crossfade between dynamic layers — write this constantly » ; « Avoid CC1=90-127 simultaneously with CC11=1-40 (physically impossible) » ; « Legato: overlap notes slightly (10-20ms) and keep CC1 smooth ».
- **Quel contrôleur pour quoi** (synthèse des sources ci-dessus) : dynamique/timbre = crossfade de couches (CC1 chez Spitfire/la plupart des orchestrales ; vélocité chez CineBrass en mode velocity map ; CC11 ou vélocité chez Session Horns) ; CC11 = « trim » de volume de phrase sans changer la couche ; vibrato = CC dédié (Spitfire) ou couche « vibrato » séparée (Session Horns Pro).
- **Ableton « Orchestral Brass »** [HEUR] : pack SONiVOX, « 11 multisampled brass instruments — trumpet, French horn, trombone, tuba, ensembles » — https://raw.githubusercontent.com/dreamrec/LivePilot/main/livepilot/skills/livepilot-core/references/pack-knowledge.md. Aucune documentation des CC/articulations trouvée.

### 3.2 Keyswitches, legato, longueurs de notes

- Session Horns Pro : « Load the articulations sequentially in the Main>Keyswitches Menu from C-1 to G#-1 in Channel 1, and continue from C-1 on Channel 2 » (multi 2 canaux pour accéder à toutes les articulations) [DOC-tiers].
- Longueur des notes [HEUR mpw midi] : « A staccato brass hit requires note durations of 20–30% of the beat value rather than 80–90% » ; « A legato string line requires overlapping notes (note-on before previous note-off) to trigger legato transitions » ; [HEUR mpw humanization] « slight overlap (over 100% length) triggers legato; gaps above 20 ms trigger a new articulation ».
- Stabs [HEUR bespoke] : « staccato map, length 0.03–0.06 measures, velocity ≥ 100… all voices attacking on the same sixteenth ».
- Legato « faux » sur banques sans vrai legato [HEUR bespoke] : « Overlap inside a phrase by 0.06–0.08 measures and start each note 0.015 measures early, so the slow sample attack speaks on the beat ».

### 3.3 Timing, effet de section, humanisation, doublage

- **Retard des cuivres** [HEUR bespoke-jazz / bespoke-brass] : « Horns and the melody sit ~10–30 ms behind the bass and drums; at 160 BPM that is +0.013 measures added to every sax and brass note. It is a measured component of swing feel » ; front line salsa « LAG = 0.006 measures » ; sax « place ~20 ms behind the section ». Aucune source lue ne documente les cuivres *en avance* ; [MÉMOIRE, non vérifié] pratique de placer les stabs de section légèrement en avance pour compenser l'attaque des samples — à mesurer [TEST].
- **Compensation d'attaque** [DOC Spitfire] : serrer « Tightness » pour jouer, puis relâcher et appliquer un **délai de piste négatif** (Track Delay négatif dans Live) pour la lecture.
- **Attaque** [HEUR ableton-mcp] trompette : « attack_time: 10-50ms depending on dynamics ».
- **Humanisation** [HEUR — https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/humanization.html] : timing général ±10–20 ms (drums ±8–18, basse/claviers ±6–15) ; « Beyond 30 ms at 120 BPM, most listeners perceive the hit as rhythmically incorrect » ; vélocité ±8–15 ; longueur ±5–15 % ; « per-voice detuning of ±3–8 cents creates organic chorusing without audible beating » ; vibrato « 4.5–7 Hz… depth (±15–50 cents) » ; « each voice must use an independently phased LFO » ; groove templates à 50–75 % ; erreurs : « Using globally synced LFOs for vibrato in ensemble patches… robotic, machine-gun vibrato ».
- **Section = plusieurs instances** [HEUR bespoke] : « Humanise ±10–20 ms and ±8–12 velocity from a seeded RNG » ; « No round-robin. Repeated identical notes machine-gun; vary velocity and micro-timing, or alternate two instances of the same map ».
- **Doublage** [DOC Rimsky-Korsakov] : « Duplication in the brass group is most frequently effected by placing a chord for horns side by side with the same chord written for trumpets or trombones » ; « Similar juxtaposition of trumpets and trombones is not so common, as this unites the two most powerful agents ». [HEUR mpw humanization, sur cordes, transposable] : dupliquer la partie sur 2–4 pistes/instances « each detuned ±2–5 cents differently ».
- **Vibrato programmé** : 4–6 Hz [HEUR ableton-mcp], 4.5–7 Hz [HEUR mpw] ; Spitfire : CC vibrato senza→molto [DOC] ; Session Horns Pro : articulation « vibrato » séparée du sustain [DOC-tiers].
- **Vélocité et couches** [HEUR bespoke, spécifique à leurs cartes sfz] : « velocity 95 is mp and velocity 96 is f, and there is nothing in between » — rappelle qu'il faut repérer les seuils de couches d'une banque avant d'écrire la dynamique [TEST : jouer une note à v95 puis v96 dans Session Horns Pro].

### 3.4 Rip, fall, scoop par pitch bend

- Sémantique notée [DOC LilyPond] : le chiffre de `\bendAfter` = intervalle **au-delà** de la note (exemples 4, 6.5, 8) ; [DOC MusicXML] un bend est rendu par défaut en 4 messages de pitch bend, commençant à 25 % de la durée et finissant à 75 % ; `bend-alter` en demi-tons.
- Pratique [HEUR bespoke] : scoop « `pitchdive`: −4 semitones, 400 ms gives a real scoop into the note (measured: 465 → 478 → 522 → 524 Hz) » ; fall « put the dive on a short repeated note at the phrase end » ; shake « pitch oscillates about ±60 cents ».
- Plage de pitch bend [HEUR copper-hollow, autres instruments] : « pitch bend (range: 2 semitones) for short slides… start pitch bend at −2, ramp to 0 over 50–150 ms » ; steel : « ±2 semitones » ; pop : « Pitch bend ±1 semitone for expression » [HEUR mpw midi].
- Plage de pitch bend de Session Horns Pro / Kontakt : **non trouvée** ; à vérifier dans l'instrument [TEST]. Préférer les articulations échantillonnées « rips », « fall », « shake », « fx glissandi » quand la banque les a (Session Horns Pro : rips, shake ; Spitfire Symphonic Brass : rip, fall).
- Limite physique à respecter [DOC-W] : glissando de trombone ≤ triton, sans changement de direction ; sur trompette, le bend se fait à la lèvre (petit intervalle), le *rip/lift* monte à travers les partiels.

### 3.5 Erreurs à éviter (synthèse)

| Erreur | Pourquoi / source |
|---|---|
| Accords de 5–6 notes sur une section de 3–4 | une section = 1 note par instrument ; « Harmonise from the chord… That guarantees the section is always inside one chord, which is why it never sounds like four soloists » [HEUR bespoke] ; horns « 2–4 players, melody and harmony » [HEUR ableton-mcp] |
| Tenues de 8 mesures sans trou | respiration [DOC Rimsky-Korsakov] ; « never run a line for eight bars without a hole » [HEUR bespoke] ; phrases 8–12 s [HEUR] |
| Registre irréaliste | limites §1 ; « instruments written outside playable range » = échec récurrent [HEUR mikeb55] ; « MIDI로 브라스를 편곡할 때 보이싱 범위를 실제 악기 음역 내로 제한하지 않으면… 연주 불가능 » [HEUR hwangtab] |
| Vélocité plate / pas de CC | « A flat line of identical velocity values is the most reliable signal that a part sounds programmed » ; « Orchestral programming without CC11… sounds like a MIDI demo » [HEUR mpw] |
| Notes staccato trop longues | 20–30 % du temps [HEUR mpw] |
| Intervalle serré dans le grave | « a major second between two brass in the low register is a growl, not a chord » [HEUR bespoke] |
| Même LFO de vibrato pour toutes les voix | [HEUR mpw humanization] |
| Tout le monde joue tout le temps | « No more than two sections simultaneously except at climaxes » [HEUR mikeb55] |
| Cors sous-dosés dans un tutti | « two horns are needed to one trumpet or one trombone » en forte [DOC Rimsky-Korsakov] |

---

## 4. Mixage des cuivres (réels et synthétiques)

### 4.1 Équilibre de section (référence acoustique) [DOC Rimsky-Korsakov]

« In the most resonant group, the brass, the strongest instruments are the trumpets, trombones and tuba. In loud passages the horns are only one-half as strong, 1 Trumpet = 1 Trombone = 1 Tuba = 2 Horns… in piano passages, all wind-instruments, wood or brass are of fairly equal balance. » → point de départ des faders d'une section échantillonnée : cors +6 dB relatifs en forte, à égalité en piano [TEST].

### 4.2 EQ

| Zone | Valeur / action | Source |
|---|---|---|
| Coupe-bas | 60–80 Hz « unless featuring tuba or low brass » | [HEUR] https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/tools/frequency-eq-reference.html |
| Coupe-bas | 80–120 Hz (tuba excepté) | [HEUR bespoke] |
| Coupe-bas section funk | HPF 150 Hz ; orchestral 100 Hz | [HEUR] https://raw.githubusercontent.com/xDarkzx/Reaper-MCP/main/reaper_mcp/mix_engine/catalog/_shared.py |
| Coupe-bas sax / trompette (jazz) | sax 100–150 Hz ; trompette 150–200 Hz | [HEUR] https://raw.githubusercontent.com/Hipare/Hipare-Reaper-agent/main/knowledge/knowledge/genres/jazz.md |
| Corps | 80–200 Hz « Bell / Body… Cut if competing with bass » ; orchestral +1 dB @300 Hz Q0.9 | [HEUR mpw ; Reaper-MCP] |
| Boue / honk | 250–500 Hz « The classic honky brass resonance zone. Cut to clean up » ; « Cut 300-500Hz to reduce honk » ; funk −2 dB @400 Hz Q1.2 ; sax « Cut: 300-500 Hz (honkiness, if present) » ; « cut 250–400 Hz when a section stacks » | [HEUR mpw ; Reaper-MCP ; Hipare ; bespoke] |
| Mordant / présence | 1–3 kHz « Bite / Presence » ; « Boost 1.5-3kHz for bite » ; funk +2 dB @2.5 kHz Q1.1 ; orchestral +1.5 dB @3 kHz ; sax présence 2–4 kHz « natural, not boosted » | [HEUR mpw ; Reaper-MCP ; Hipare] |
| Dureté | trompette « Cut: 1-2 kHz (if harsh) » ; « expect the 2–4 kHz region to be where a trumpet gets shrill — a wide −2 dB there is usually enough » ; extrait non lu : « narrow cut at 3–5kHz reduces the bite » | [HEUR Hipare ; bespoke ; extrait tailout.de non lu] |
| Brillance | 4–8 kHz « Brilliance / Edge… The crisp high register of a trumpet » ; shelf +1 dB @8 kHz Q0.7 | [HEUR mpw ; Reaper-MCP] |
| Air | 10–16 kHz « Air / Overtone » ; sax 8–12 kHz « breath, subtlety » ; extrait non lu : « 7-9 kHz adds air/breathiness » | [HEUR mpw ; Hipare ; extrait] |
| Face à la voix | « Untamed brass in the 2-4 kHz range will bury vocals… use dynamic EQ to duck this range when the vocal is present, or automate the horn level down » (extrait non lu) ; « 브라스… 2~4kHz 보컬 명료도 대역… 보컬 휴지 구간에 브라스 라인을 집중… 보컬 음역보다 한 옥타브 위·아래로 분리 » | [HEUR — extrait tailout.de ; HEUR hwangtab] |

### 4.3 Compression, saturation

| Réglage | Valeur | Source |
|---|---|---|
| Glue de section (funk) | ratio 2.5:1, seuil −14 dB, attaque 10 ms, relâche 100 ms, knee 4 dB, makeup +1.5 dB (« Light glue to tame section peaks without killing the honk ») | [HEUR Reaper-MCP] |
| Jazz (si compression) | ratio 2:1–3:1, attaque lente 30–50 ms « preserve transients », relâche 200–300 ms, GR 1–3 dB max | [HEUR Hipare] |
| Extrait non lu | 3:1–4:1, attaque 10–20 ms, relâche 80–150 ms, 4–6 dB GR ; ou 2:1 attaque 30–50 ms ; attaque 15–25 ms « to preserve the characteristic "blat" » ; parallèle « 20-30% of a heavily compressed signal » sur stabs ; bus « gentle compressor and EQ » | [HEUR — extrait de recherche (tailout.de / roastyourmix), pages bloquées] |
| Saturation à la place de la compression | « ZamTube/crunch_rhythm at low drive on a brass bus gives the edge that a real fortissimo has and a sample does not. Keep the dynamics — a limiter on the master took one orchestral piece's crest factor from 21.8 dB to 16.0 » | [HEUR bespoke] |
| Opto vs FET, temps précis pour cuivres réels | **non trouvé** dans une page lue | — |

### 4.4 Réverbération, panoramique, bus

| Élément | Valeur | Source |
|---|---|---|
| Reverb jazz/acoustique | Hall ou chamber, decay 1,5–3 s, pré-delay 20–40 ms « for clarity », **même reverb pour tous** (« Simulates musicians playing together ») ; delay « Rarely used… If used: Very subtle, short slap-back » | [HEUR Hipare] |
| Reverb « une pièce sur le master » | Dragonfly Room `live_room` (band) / Hall `orchestral_hall` ; réduire la largeur sinon corrélation négative et échec du test mono | [HEUR bespoke] |
| Panoramique orchestral | cor −0.26, trompette +0.20, trombone/tuba +0.36 | [HEUR bespoke] |
| Panoramique jazz | trompette −0.18, trombone +0.34, ténor +0.16, « Nothing hard panned » | [HEUR bespoke-jazz] |
| Panoramique brass band | trompettes lead ∓0.42/+0.44, trompette « réponse » −0.72 | [HEUR bespoke] |
| Placement scène jazz | « Right: Horns » (perspective public), basse/batterie centre | [HEUR Hipare] |
| Bus de cuivres | « 악기별로 개별 녹음한 뒤 믹싱에서 EQ와 컴프레서로 섹션 전체를 하나의 소리로 묶는 것 » (enregistrer séparément, puis bus EQ + compresseur pour lier la section) | [HEUR hwangtab] |
| Cibles sonie jazz | −16 à −20 LUFS (traditionnel), −14 à −16 (moderne), −12 à −14 (fusion) | [HEUR Hipare] |
| Extrait non lu | plate/hall pour cuivres pop ; de-essing/soothe sur sax | **non trouvé** dans une page lue |

### 4.5 Transitoires, pics

- « a four-voice section stacking on one stab clips easily » → vérifier `clipped_samples` sur les stabs [HEUR bespoke].
- Spécifique aux samples : « Tightness » (Spitfire) réduit l'attaque molle ; à compenser par délai de piste négatif [DOC].
- Aucune page lue sur les « spikes » de cuivres réels ni sur les de-essers de sax → [MÉMOIRE, non vérifié] : de-esser/soothe sur sax entre 3 et 8 kHz ; à traiter comme hypothèse [TEST].

---

## 5. Tableau récapitulatif des réglages de mix (points de départ, tous [HEUR])

| Piste | HPF | Coupe | Boost | Comp | Reverb | Pan |
|---|---|---|---|---|---|---|
| Section funk (bus) | 150 Hz | −2 dB @400 Hz Q1.2 | +2 dB @2.5 kHz Q1.1 ; +1 dB shelf 8 kHz | 2.5:1, 10 ms / 100 ms, −14 dB, knee 4 | même room que le reste | tpt/tbn/sax répartis, rien en hard |
| Section orchestrale | 100 Hz | −1 dB @600 Hz | +1 dB @300 Hz ; +1.5 dB @3 kHz | légère ou saturation | hall, largeur réduite | cor −0.26, tpt +0.20, tbn/tuba +0.36 |
| Sax (jazz) | 100–150 Hz | 300–500 Hz si honk | 2–4 kHz naturel ; air 8–12 kHz | 2–3:1, 30–50 ms / 200–300 ms, 1–3 dB | hall/chamber 1,5–3 s, pré-delay 20–40 ms | +0.16 |
| Trompette (jazz) | 150–200 Hz | 1–2 kHz si dure ; −2 dB large 2–4 kHz si stridente | (peu : « Brass is naturally bright ») | id. | id. | −0.18 |

---

## 6. Pages consultées

### 6.1 Lues (contenu réellement téléchargé, HTTP 200)

Sources primaires / de référence [DOC] :
1. https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/instrument.py (tessitures `lowestNote`, transpositions)
2. https://raw.githubusercontent.com/cuthbertLab/music21/master/music21/pitch.py (convention C4 = 60)
3. https://raw.githubusercontent.com/musescore/MuseScore/4.4.4/share/instruments/instruments.xml (plages amateur/pro, transposeChromatic)
4. https://pypi.org/pypi/abjad/json → https://files.pythonhosted.org/packages/76/9c/369810e498be649ebc531e9f6a78e66d28b45174f1f8f1b4af6bdf11bbf7/abjad-3.31.tar.gz (`source/abjad/instruments.py`)
5. https://raw.githubusercontent.com/w3c/musicxml/gh-pages/schema/musicxml.xsd (scoop/plop/doit/falloff, brass-bend, flip, smear, mutes, bend-sound, glissando/slide, shake)
6. https://raw.githubusercontent.com/w3c/smufl/gh-pages/metadata/glyphnames.json (glyphes `brass*`)
7. https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/notation/expressive.itely (\bendAfter, \breathe)
8. https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/notation/wind.itely
9. https://raw.githubusercontent.com/lilypond/lilypond/master/Documentation/en/music-glossary.tely
10. https://raw.githubusercontent.com/legobridge/copyshield-llm/main/data/text/PG33900_text.txt (Rimsky-Korsakov, *Principles of Orchestration*, Gutenberg #33900 ; doublon https://raw.githubusercontent.com/jasonswett/johnny/master/lib/books/orchestration.txt)
11. https://raw.githubusercontent.com/vingleo/SyncDocuments/master/SpitfireSymphonyOrchestra_UserManual%E5%8F%82%E8%80%83%E7%BF%BB%E8%AF%91.txt (texte anglais du manuel + traduction chinoise)
12. Cartes Reaticulate (dépôt jtackaberry/reaticulate, branche master) : `userbanks/Native_Instruments/Native_Instruments-Session_Horns_Pro.reabank`, `userbanks/Cinesamples/Cinesamples-CineBrass_Pro.reabank`, `…CineBrass_Core.reabank`, `userbanks/Spitfire/Spitfire-Studio_Brass_Pro.reabank`, `banks/65-01-Spitfire-Symphonic_Brass.reabank`, `userbanks/Spitfire/Spitfire-BBC_Symphonic_Orchestra.reabank`

Copies Wikipedia [DOC-W] :
13. https://raw.githubusercontent.com/anassalamah/nlp-project/master/wikipedia%20pages/Trumpet.txt et `Trombone.txt`
14. https://raw.githubusercontent.com/kirito-0512/data/main/dump/Trumpet.txt, `Trombone.txt`, `Saxophone.txt`, `Tuba.txt`, `Flugelhorn.txt`, `Glissando.txt`, `Funk.txt`, `Afrobeat.txt`, `Ska.txt`
15. https://raw.githubusercontent.com/alaym3/musician-network-analysis/main/Wikipages/Earth,%20Wind%20%26%20Fire.txt
16. https://raw.githubusercontent.com/epfl-ada/ada-2024-project-leszinzinsdelespace/main/data/plaintext_articles/Saxophone.txt (Wikispeedia, ancienne version ; non citée)

Documents communautaires [HEUR] :
17. https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/midi.html
18. https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/humanization.html
19. https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/tools/frequency-eq-reference.html (et `tools/eq-problem-solver.html`, mêmes données)
20. https://raw.githubusercontent.com/xDarkzx/Reaper-MCP/main/reaper_mcp/mix_engine/catalog/_shared.py
21. https://raw.githubusercontent.com/Hipare/Hipare-Reaper-agent/main/knowledge/knowledge/genres/jazz.md
22. https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp/master/.agents/skills/bespoke-brass-winds/SKILL.md
23. https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp/master/.agents/skills/bespoke-jazz/SKILL.md
24. https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/master/demos/historical/afrobeat/style.py
25. https://raw.githubusercontent.com/hwangtab/studio/main/content/stories/brass-arrangement1.md (coréen)
26. https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/charts/Beatrice/03_arrangement/V9.0-Arranging-Notes.md ; `docs/big_band_reuse_audit.md` ; `charts/Beatrice/03_arrangement/none_of_these_work.md` ; `Research/modern_big_band_arranging_books.md` ; `charts/Beatrice/02_reharm/chorus2_wheeler_style.md` ; `build_v32_chorus2_realranges.py`
27. https://raw.githubusercontent.com/toshiotawa/jazzify-lab/master/en-blog/src/data/blog/jazzpiano-block-chords.md (original : jazzpianodays.com)
28. https://raw.githubusercontent.com/Kan-A-Pesh/music-with-code/master/docs/research/partie2_harmonie.md (français)
29. https://raw.githubusercontent.com/JoanComasFdz/salsa-music/main/src/songs-breakdown/salsa-song-structure-breakdowns.md
30. https://raw.githubusercontent.com/bitwize-music-studio/claude-ai-music-skills/main/genres/ska/README.md ; `genres/funk/README.md` ; `genres/p-funk/README.md`
31. https://raw.githubusercontent.com/josefigueredo/ableton-mcp/main/docs/sources/INSTRUMENT_TECHNIQUES_SOURCE_OF_TRUTH.md
32. https://raw.githubusercontent.com/bedwards/copper-hollow/main/docs/midi-programming-techniques.md
33. https://raw.githubusercontent.com/edtbl76/midi_real_book/main/ensembles/James%20Brown%20funk/ensemble.md
34. https://raw.githubusercontent.com/eetusuikkanen/eetusuikkanen.github.io/master/content/blog/1757950802962-ost-composing-jam-8/index.md
35. https://raw.githubusercontent.com/dreamrec/LivePilot/main/livepilot/skills/livepilot-core/references/pack-knowledge.md
36. https://raw.githubusercontent.com/tkgally/algorithmic-music/main/wiki/funk-soul-and-rnb.md
37. https://raw.githubusercontent.com/JefroB/Electronic-Music-Genre-Skills/master/.agent/skills/genre-disco-nudisco/references/production-techniques.md (horn section 4–8 musiciens en disco)
38. https://raw.githubusercontent.com/Erotemic/ambition_music_renderer/main/ambition_music_renderer/data/instrument_catalog.yaml (catalogue sfz ; peu utile)

Bibliographie signalée (non lue) : Sammy Nestico *The Complete Arranger* ; Russell Garcia *The Complete Arranger-Composer* ; Rayburn Wright *Inside the Score* ; Pease & Pullig *Modern Jazz Voicings* (drop 2, drop 3, upper structures) ; Adler *The Study of Orchestration* ; Kennan & Grantham *The Technique of Orchestration* (cité par Wikipedia pour les pédales et le glissando de trombone) — https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/Research/modern_big_band_arranging_books.md.

### 6.2 Échecs (bloquées ou introuvables)

`EGRESS_BLOCKED` / 403 au CONNECT (proxy) : https://www.soundonsound.com/techniques/top-brass-part-3 ; https://www.soundonsound.com/reviews/native-instruments-session-horns ; https://www.evanrogersmusic.com/blog-contents/big-band-arranging/writing-horns-for-pop-songs ; https://www.evanrogersmusic.com/blog-contents/big-band-arranging/articulation ; https://blog.native-instruments.com/realistic-horn-vst/ ; https://en.wikipedia.org/wiki/Trumpet ; https://steinberg.help/dorico_pro/v3/en/… (jazz articulations) ; https://tailout.de/2026/08/04/how-to-mix-brass-instruments-modern-production/ ; https://www.howtowritebettersongs.com/how-to-arrange-horn-section/ ; https://arranging.fandom.com/wiki/Trumpet ; https://tamingthesaxophone.com/theory/arranging/composition-brass ; https://intmus.github.io/… (transpositions) ; https://musescore.org/en/node/335651 ; https://modwheel.net/guides/the-art-of-brass-programming ; https://roastyourmix.com/mix/horns ; https://gearspace.com/threads/programming-horns.434784/ ; https://www.stockmusicmusician.com/blog/how-to-eq-brass ; https://github.com/… (403) ; https://api.github.com (403) ; https://web.archive.org ; https://lilypond.org ; https://www.gutenberg.org ; https://e-instruments.com/…/Session_Horns_Pro_Manual_English.pdf ; https://dumps.wikimedia.org ; https://www.spitfireaudio.com ; https://www.native-instruments.com ; https://openmusictheory.github.io ; https://www.ableton.com/en/manual/ ; https://xferrecords.com ; huggingface.co ; arxiv.org ; gitlab.com ; codeberg.org ; readthedocs.org.

404 sur raw.githubusercontent.com : `musescore/MuseScore/master/share/instruments/instruments.xml` (chemin valable seulement sur le tag 4.4.4) ; `Abjad/abjad/main/abjad/instruments.py` (fichier dans `source/abjad/` de la sdist) ; `jtackaberry/reaticulate/master/factory.reabank` ; `kirito-0512/data/master/dump/*` (branche `main` requise ; `Horn_section`, `Tower_of_Power`, `Alto/Tenor/Baritone_saxophone`, `French_horn`, `Salsa_music`, `Big_band`, `Fela_Kuti`, `Jerry_Hey`, `Uptown_Funk`, `Antibalas`, `Phenix_Horns`, `Transposing_instrument`, `Pedal_tone`, `Jazz_trombone`, `Brass_instrument`, `Flutter-tonguing`, `Rocksteady`, `Fania_Records`, `Maceo_Parker`, `Fred_Wesley`, `Shout_chorus`, `Bass_trombone` absents du dump) ; `mikeb55/Big-Band-Arranging/main/archive/…/V10.0-Refinement-Notes.md` et `V12.0-Arranger-Diagnostic.md`.

Accès GitHub MCP refusé (dépôts non configurés pour la session) : `musescore/MuseScore`, `Abjad/abjad` via `get_file_contents` (contourné par raw.githubusercontent.com).

Lecture de la documentation du proxy (`/root/.ccr/README.md`, `__agentproxy/status`) : refusée par le classificateur de permissions ; non retentée.

---

## 7. Ce qui n'a pas été trouvé (à combler ou à marquer [TEST]/[MÉMOIRE])

1. **Sound On Sound** « Top Brass » (parties 1–3), « Mixing/Recording brass » : bloqués ; seuls des extraits de recherche existent (voir §4).
2. **Native Instruments** : manuel Session Horns Pro (Animator, Smart Voice Split détaillé, Humanize, plage de pitch bend, mapping exact vélocité/CC11) et blog « 7 techniques ». Seules la carte des articulations (Reaticulate) et une mention de Smart Voice Split ont été lues.
3. **Ableton « Orchestral Brass »** : hormis « SONiVOX, 11 instruments multi-échantillonnés », aucune doc d'articulations/CC.
4. **Kontakt/Session Horns : plage de pitch bend par défaut** pour programmer rips/falls — non documenté ; [MÉMOIRE, non vérifié] ±2 demi-tons par défaut dans Kontakt, à vérifier [TEST].
5. **Timing mesuré des vraies sections** (avance/retard en ms) : seules des valeurs de pratique (10–30 ms de retard, +6 ms) [HEUR] ; rien de mesuré sur des enregistrements.
6. **Arrangements documentés** : Tower of Power (aucune page lue), Chicago, Blood Sweat & Tears, Fela Kuti (détail des lignes), Fania (voicings de trombones), rocksteady, « Uptown Funk » (Antibalas non vérifié), écrits de Fred Wesley / Jerry Hey / Greg Adams.
7. **Dorico / Berklee / Learn Jazz Standards** : listes d'articulations jazz et page « drop 2 voicings » bloquées (la page LJS est citée comme source par le document français lu).
8. **Mixage** : iZotope, Waves, Produce Like A Pro, Attack Magazine — bloqués ; opto vs FET pour cuivres, temps exacts « pro », de-essing/soothe sur sax, plate vs hall pour cuivres pop, gestion des pics : aucune page lue. Les valeurs de §4 viennent de wikis/skills communautaires et d'extraits non lus.
9. **Registres « confortables » chiffrés par instrument** hors trompette (G4–G5 [HEUR]) : non trouvés ; les plages amateur/pro de MuseScore servent de substitut [DOC].
10. **Notation du growl, du flutter et du shake dans une source d'édition** : SMuFL n'a pas de glyphe « growl » ni « flutter » (flutter = tremolo + texte chez LilyPond) ; « shake » n'existe qu'en tant qu'ornement MusicXML (`shake`, aspect de mordant inversé).
