# Lead future rave : la « supersaw déguisée en basse », avec pitch-bend et filtre résonant

## Cible
`FUTURE RAVE / LEAD ou BASSE-LEAD / 126–128 BPM / fa♯, fa ou la mineur / MIDI 45–69 (basse-lead) ou 72–88 (lead aigu) / notes pointées, motif de 2 mesures, climax mesure 7`

Aucune source ne chiffre le patch de Guetta et MORTEN ; cette recette suit la seule ligne chiffrée (Monosounds `[DOC]`) et l'ancêtre hoover `[DOC-2]`. Tout ce qui est `[HEUR]` se règle à l'oreille contre une référence dans REF.

## Moteur
Serum 2 (unisson, deux filtres, Hyper/Dimension, PORTA SCALED). Natif : Wavetable (unison Classic) + Analog pour le hoover ; Drift en version mono chaude.

## Patch
| Étage | Valeur | Preuve |
|---|---|---|
| OSC A | Basic Shapes saw ; UNISON 5 ; DETUNE 0,09 ; BLEND 75 % ; WIDTH 50–60 | `[DOC]` |
| OSC B | saw OCT −1 ; UNISON 5 ; DETUNE 0,08 ; WIDTH 55 ; niveau aux deux tiers d'A | `[DOC]` |
| OSC C (drops seulement) | saw OCT +1 ; UNISON 5 ; DETUNE 0,10 ; WIDTH 95 ; coupé à 2 kHz | `[DOC]` |
| PHASE / RAND | RAND 100 % (sinon « zap » identique à chaque note) | `[DOC Szabo]` |
| FILTER 1 | MG Low 24 (ou French LP) ; CUTOFF ≈ 600 Hz au repos, balayé 400–900 Hz par ENV 2 ou automation ; RES 20–35 | `[DOC]` cutoff ; RES `[HEUR]` |
| ENV 1 (ampli) | A 1–5 ms · D 250 · S 60 % · R 31 ms | `[DOC-2 mesuré]` |
| ENV 2 → CUTOFF | A 2 ms · D 200 · S 50 % ; quantité 30 % | `[DOC-2]` |
| Le « rave » (choisir une des trois) | ENV 3 → CRS de A et B **+8 st**, unipolaire, decay 60–200 ms (hoover) · ou ENV 3 → CRS **−5 à −12 st** montant vers la note en 200–600 ms · ou PORTA 60–120 ms, **SCALED** on, LEGATO on avec notes qui se chevauchent | `[DOC-2]` ; durées `[HEUR]` |
| Pitch bend | GLOBAL Pitch bend UP 12 : montée depuis l'octave inférieure au début de chaque phrase | `[DOC]` |
| Vibrato | LFO 1 → FINE, 7 Hz, DELAY 200 ms, RISE 200 ms | `[DOC]` |
| Voicing | MONO ou LEGATO ; POLY 3 seulement pour les accords sombres (trois notes maximum) | `[DOC]` |

## Chaîne (Serum 2, dans l'ordre)
Distortion Tube ou Soft Clip léger → Compressor MULTIBAND MIX 15–25 % → **un seul** élargisseur : Hyper/Dimension avec UNISON 0 (Dimension seul), SIZE 0, MIX ≈ 30 % → Reverb sur **BUS 1** (HI CUT 8 kHz, LO CUT 500 Hz, départ −12 dB) → Delay 1/4 ping-pong feedback 30–40 % sur BUS 2 (départ −15 dB). Hors Serum : coupe-bas 100–150 Hz 12–24 dB/oct sur toute la pile (REQ 6 ou Pro-Q 4) ; EQ soustractive −2/−3 dB à 500 Hz, −2 dB à 1,5 kHz, −2/−3 dB à 3,5 kHz, shelf −1/−2 dB au-dessus de 12 kHz ; **sub séparé** (`basse-future-rave-sub-et-mid.md`) ; sidechain audible 6–10 dB `[HEUR]` (`sidechain-et-pump.md`).

## Variantes
- **Hoover pur** : trois saws-pulse, OSC A/B ±40 cents opposés, OSC C −12 st, WARP 1 = PWM sur une carrée avec LFO 5 Hz, enveloppe de pitch ≈ 1 octave, LP 4–6 kHz, amp A 0–10 R 200 ; chorus lourd → phaser → reverb ; « les deux parties non négociables : le balayage descendant et le chorus » `[DOC-2]`.
- **Big room** : unison 7 sur les deux saws, detune 0,12, couche +12 large, reverb longue sur son bus, gros sidechain.
- **Eurodance** : unison 7, detune 0,14 et plus, filtre ouvert, release courte.

## MIDI
Motif de 2 mesures répété, climax mesure 7 (+12 sur la note centrale), résolution mesure 8 sur 1 ou 5 ; notes pointées et sur les « et » ; en la mineur octave 5 : A5 C6 E6 A6 G6 E6 / E6 A6 G6 E6 C6 A5 (`../references/theorie-specifique.md` § 3.1).

## Erreurs
Detune et blend au maximum ; unison 16 ; grave demandé à la pile (sous 150 Hz les voix battent : sub séparé) ; release d'ampli longue (la queue vient des sends) ; phase fixe ; vibrato dès l'attaque ; cinq notes d'accord sur une supersaw.

## Vérification
Seul puis avec kick, sub et stabs ; mono ; deux notes extrêmes du riff ; macro « filtre » musicale de 0 à 100 % ; preset sauvé, capture, version de Serum 2 notée. Analyse d'une référence par `../../synthese-reference/SKILL.md` si l'utilisateur fournit un extrait.
