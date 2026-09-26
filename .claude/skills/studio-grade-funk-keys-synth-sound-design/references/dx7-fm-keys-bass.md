# Yamaha DX7 dans le funk : patches d'usine décodés et transposition dans Operator

Données lues **directement dans la cartouche ROM1A** (sysex, checksum vérifié) et ROM1B (table C), formats vérifiés dans `parse-rom.js`, temps estimés par le générateur d'enveloppe de Dexed (±20 %) — tout `[DOC]` sauf les ms `[HEUR]` et les transpositions `[TEST]`. Fichiers : `../../../../corpus/synthes-vintage/dx7-rom1a-32-voix-decodees.md`, `../../../../corpus/funk-claviers/`.

Conversions utiles [DOC Dexed] : detune ±7 ≈ ±6–9 cents ; LFO speed 30 ≈ 4,8 Hz, 34 ≈ 5,4 Hz, 35 ≈ 5,6 Hz, 37 ≈ 5,95 Hz ; rates 0–99 ne sont pas des ms.

## E.PIANO 1 (ROM1A #11) — le « DX7 Rhodes »
Algorithme **5** (trois piles de deux : OP2→OP1, OP4→OP3, OP6→OP5), **feedback 6** sur OP6, Osc Key Sync off, LFO sinus 5,4 Hz delay 33 PMD/AMD 0 (vibrato à la molette seulement).

| OP | Rôle | Ratio | Detune | Niveau | KVS | Temps à C3 [HEUR] |
|---|---|---|---|---|---|---|
| 1 | porteuse « cloche » | 1,00 | +3 | 99 | 2 | A 1 ms, D ≈ 2,2 s vers 75 %, R ≈ 74 ms |
| 2 | modulateur « tine » | **14,00** | 0 | **58** | **7** | D ≈ 140 ms puis 1,8 s, R 9 ms |
| 3 | porteuse corps | 1,00 | 0 | 99 | 2 | D 0,75 s vers 95 %, R 0,57 s |
| 4 | modulateur corps | 1,00 | 0 | 89 | 6 | D 250 ms, R 0,5 s |
| 5 | porteuse corps 2 | 1,00 | **−7** | 99 | 0 | comme 3 |
| 6 | modulateur + feedback 6 | 1,00 | **+7** | 79 | 6 | D 250 ms, R 0,44 s ; level scaling −LIN au-dessus de E3 (bp 41, prof. 19) |

Lecture : la pile 14:1 avec **KVS 7** est le **bark FM** (les harmoniques hautes n'apparaissent qu'en jeu fort et s'éteignent en ≈ 140 ms) ; deux piles 1:1 donnent le corps, dont l'une désaccordée ±7 (≈ 12 cents d'écart → battement lent) avec feedback 6 qui « sale » ; OP6 s'atténue dans l'aigu.

**Operator** [TEST] : algorithme « deux paires parallèles » (B→A, D→C ; n° 8 selon la lecture locale de la figure) — il manque la 3e pile : Spread léger ou seconde instance dans un Rack. A : Sine Coarse 1, A 1 ms, D 2–4 s, S 0, R 300 ms ; **B : Coarse 14, Level −30 à −18 dB (58/99 non convertible sans table), `Lev < Vel` 80–100 %, D 300–500 ms, S −12 dB, R 10 ms** ; C : Sine Coarse 1, −3 dB ; D : Coarse 1, **Feedback 40–70 %**, Fine +6 cents ou Spread, Level −12 à −6 dB, `Lev < Vel` 85 %, `Lev < Key` négatif au-dessus de E3. Ratio 18 = variante plus dure [HEUR-extrait]. Recette FM documentée alternative : STK `Rhodey` (algorithme 5 TX81Z, base 2×f, ratios 1/0,5/1/15, modulateur cloche à 0,25 s de decay) [DOC].

## BASS 1 (ROM1A #15) — le slap FM (« Take On Me » [HEUR-extrait])
Algorithme **16** (une porteuse OP1 ; OP2, OP3←OP4, OP5←OP6), feedback 7 (OP6), **Osc Key Sync ON**, transpose −12.
| OP | Ratio | Niveau | KVS | Rate scaling | Temps [HEUR] |
|---|---|---|---|---|---|
| 1 porteuse | 0,50 | 99 | 0 | **7** | A 1 ms, D 4 ms → 95 %, R ≈ 45 ms |
| 2 mod. grave | 0,50 | 80 | 0 | 7 | decay long |
| 3 mod. corps | 0,50 | 99 | 3 | 6 | D2 ≈ 1,6 s |
| 4 « slap » | **5,00** | 93 | **5** | 5 | D ≈ 470 ms |
| 5 mod. tenu | 0,50 | 62 | 3 | 7 | tenu |
| 6 « clic » + fb 7 | **9,00** | 85 | **7** | 1 | D ≈ 370 ms |
Lecture : brillance percussive = ratios 5 et 9 très sensibles à la vélocité, éteints en 400–500 ms ; corps « saw-like » par les 1:1 ; rate scaling 7 raccourcit l'aigu ; release 45 ms = sec. **Operator** [TEST] : algorithme 7 (B+C+D → A) : A Coarse 0,5 (ou 1 avec Transpose −12) ; B 0,5 −2 dB ; C **Coarse 5** −1 dB, Lev < Vel 70 %, D 470 ms S −inf ; D **Coarse 9**, −2 dB, Feedback 100 %, Lev < Vel 100 %, D 370 ms ; A : A 1 ms, D 4 ms, S −0,4 dB, R 45 ms ; **Osc Retrig ON** partout ; Time < Key positif ; Chorus-Ensemble derrière (le chorus est dans « Take On Me »).
BASS 2 (#16) : algorithme 17, attaques ≈ 0,8–0,9 s sur OP2/OP6 : basse 80s ronde qui gonfle.

## KOTO (ROM1A #23) — « When Doves Cry » [HEUR-extrait pour l'attribution]
Algorithme 2, feedback 7 (OP2 ratio 4), Osc Key Sync ON, **LFO sinus 4,8 Hz delay 40 PMD 17 AMD 15 sync ON** (vibrato + trémolo retardés intégrés), **pitch EG L1 49** (léger creux d'attaque = pincement). Ratios 1 / 4 / 1 / 1 / 4 / 3. Operator [TEST] : algorithme 8, A 1 + B 4 Feedback 100 % ; C 1 + D 3–4 ; pitch env −1 % decay 20 ms ; LFO 4,8 Hz delay 0,5 s vers pitch (faible) et niveaux.

## MARIMBA (#22), CLAV 1 (#20), SYN-LEAD 1 (#14), CALIOPE (ROM1B #20)
- MARIMBA : algorithme 7, feedback 0, ratios 0,5 / 3 / 0,5 / 5 / 0,75 / **4,52** (inharmonique), level scaling qui atténue les modulateurs dans l'aigu ; decays porteuses 110–225 ms puis ≈ 1 s. Operator : algorithme 8, A 0,5 / B 3, C 0,5 / D 5, decays de modulateurs 30 ms, Lev < Key négatif.
- CLAV 1 (pour un « Superstition » FM) : algorithme 3, feedback 5, piles 6→0,5→0,5 et 8→0,5→2 ; modulateurs hauts (6 et 8) à **decay 6 ms** = le clic ; porteuses decay 3 ms vers 90 % puis tenue, release ≈ 110 ms ; KVS 6–7.
- SYN-LEAD 1 : algorithme 18, feedback 7, transpose +12, LFO 6 Hz delay 42 **AMD 99** (trémolo profond retardé/molette) ; ratios 1/1/1/2/3/**17** ; lead « square-like ». Operator : algorithme 7, A 1, B 1 Feedback 100 %, C 2, D 3 bas.
- CALIOPE (orthographe d'usine) : algorithme 16, feedback 5, ratios 1 / 4,6 / 2,02 / 2 / 2 / 7,04, attaque porteuse ≈ 30 ms avec léger gonflement ; aucun usage funk documenté.
- BRASS 1 : voir le skill cuivres.

## Talkbox DX100
Roger Troutman : Golden Throat + Minimoog puis **Yamaha DX100** (portable) ; patch « SAWPULSE » d'après un témoignage anonyme [HEUR-extrait] ; Chromeo : DX100 avec les patches de la famille Troutman → Rocktron Banshee 2 → « un peu d'EQ et de compression » [DOC-EXTRAIT] ; Mr Talkbox (24K Magic) : DX100 → MXR M222 [DOC-EXTRAIT/HEUR-extrait]. Émulation : `../recipes/talkbox-zapp-modern.md`.
