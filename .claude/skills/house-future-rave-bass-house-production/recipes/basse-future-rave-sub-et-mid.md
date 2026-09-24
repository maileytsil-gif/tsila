# Basse future rave : sub sinus + mid saw filtrée, off-beat ou roulante

## Cible
`FUTURE RAVE, BIG ROOM, TECHNO-HOUSE / SUB + BASSE MID / 126–128 BPM / sub MIDI 28–40, mid +12 / off-beat 1/8 (notes 60–120 ms) ou rolling 1/16 première double vide`

## Moteur
Serum 2 en une instance : OSC A saw (mid, → FILTER 1), SUB sinus routé **Direct** (contourne filtre et FX, reste propre). Natif : Wavetable « ANNA » (`../../sound-designer-serum/references/patches-genres.md` § 4) ou Analog.

## Patch
| Étage | Valeur | Preuve |
|---|---|---|
| SUB | sinus, mono, unison 1, sans detune ; ENV A 4 ms · D 300 · S 95 % · R 30 ms ; LP 90 Hz ; −6 dB | `[DOC-2]`, `basses.md` |
| OSC A (mid) | saw + carrée (WARP ou OSC B carrée FINE +8 cents niveau 0,35), **+12 st** au-dessus du sub | `[DOC-2 Attack Warehouse]` |
| FILTER 1 | MG Low 24 ; CUTOFF **350 Hz**, RES ≈ 12 ; version future rave : parqué à **600 Hz**, balayé 400–900 Hz, UNISON 5 DETUNE 0,09 | `[DOC-2]` ; `[DOC Monosounds]` |
| ENV 1 (mid) | A 4 ms · D 120 · S 35 % · R 30 ms | `[DOC-2]` |
| ENV 2 → CUTOFF | A 2 ms · D 90 · S 0 ; quantité 55 % ; vélocité → cutoff 30 % | `[DOC-2]` |
| Saturation | Distortion Tube drive 35 %, mix 35 % (sur la mid seulement) | `[DOC-2]` |
| EQ | HPF 65 Hz / LPF 350 Hz sur la mid ; −9 dB relatif | `[DOC-2]` |
| Voicing | MONO, LEGATO pour les doubles ; PORTA 0–25 ms | `[DOC]` |

## MIDI
```
Off-beat 1/8     pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
                       . . x . | . . x . | . .  x  .  | .  .  x  .     vel ≈ 102, gate 80 % de la croche ; dernière croche = approche chromatique 40 % du temps
Rolling 1/16           . x x x | . x x x | . x  x  x  | .  x  x  x     vel 66 pairs / 86 impairs, gate 80 % ; première double vide pour le kick
```
Octave à +12 sur les pas 2–4 de la mesure 4 ou 8 `[HEUR]`. Le sub tient la fondamentale du riff, la mid joue le rythme.

## Sidechain
Attaque la plus rapide, hold 20–50 ms, release **1/16 ou 1/8** (117 ou 234 ms à 128), profondeur 3–10 dB (subtil) ou 10–20 dB (pompage) `[DOC-2 amen]` ; « standard » seuil −20 dB 6:1 attaque 0,5–1 ms release 150–200 ms `[DOC-2 Fearvox]`. Sur ce Mac : Compressor natif toléré, bx_glue Ext + HPF, API-2500 S/C (`sidechain-et-pump.md`).

## Chaîne hors Serum
Saturator interdit → J37 ou Distortion interne ; EQ −3 dB au plus vers 200 Hz ; sidechain ; EQ finale ; Utility MONO BASS 100–120 Hz (bx_glue Mono Maker sur le bus BASSES).

## Erreurs
Release d'ampli par défaut trop longue (600 ms dans Wavetable : les notes se fondent) ; polyphonie ; sub stéréo ou saturé ; pas de vélocité → cutoff ; mid coupée au-dessus de sa propre fondamentale (le HPF reste sous la note jouée).

## Vérification
`kick_bass_check.py` : corrélation 30–120 Hz positive ; sub seul en mono ; kick plus fort que la basse dans le sub ; la mid disparaît sans le sub et le sub sans la mid n'a pas de rythme : les deux ensemble seulement.
