# Liquid Drum & Bass DNA

- Musicality, soul and atmosphere before maximal drum/bass aggression.
- Strong chord progression, vocal or melodic hook can be the primary construction anchor.
- Drums: fast and fluid but should leave room for harmony; break layers add human motion.
- Bass: clean sub and supportive musical movement.
- Sampling: pitch, chorus, delay, reverb and warping can make found material part of the song's identity.
- Breakdowns develop melody/vocal/atmosphere; transitions often use filters, reverbs and tails rather than giant EDM snare ramps.
- Preserve dynamics and emotional contrast at mastering stage.
- Reference anchors (Calibre, Hybrid Minds, LSB, Monrroe, Random Movement, Justin Hawkes): `../36-dnb-engine.md`; no measured data on them in repo.

## Numbers
Evidence tags: `../80-evidence-policy.md`; data caveats: `../10-genre-router.md`. The repo has DnB-wide data, nothing liquid-specific.
- **Tempo**: Beatport Drum & Bass Top 100: 174 (58 tracks), 176 (16), 172 (8) [DOC WhatBPM 2023]; theory table 160–180, typical 174, felt 87 [DOC-2]. Default **174**.
- **Swing**: DnB range 50–60 % [DOC-2, Attack]; studio grid swings the ghost snares only, `swing(0.02, n/16)`, unit undocumented [HEUR; TEST].
- **Grid**: two-step, kick steps 1 and 11, snare 5 and 13, ghost snares 4, 10, 16 at v30–45, 8th-note hats; full grid in `../36-dnb-engine.md` [HEUR].
- **Keys/modes**: manual DnB sample 82 % minor, G minor 32 %, F minor 21 % [DOC GiantSteps, n = 38]; Beatport roots F, D, E♭ [DOC WhatBPM, auto-keys]. The theory text names C minor as most common and D, A, F minor for liquid [DOC-2]: the data favour G/F minor. Liquid chords: maj7, m9 and borrowed chords, e.g. Am9 – Cmaj7 – Em7 – Am9 – Cmaj7sus4/F – E; Am9 and Cmaj7 share notes, only the bass moves; the clean sub follows the chords [DOC-2].
- **Sections**: intro 32 · build 16 · drop 1 64 (two varied halves of 32) · mid 16–32 · breakdown 32 (often drumless) · build 16 · drop 2 64 · outro 32 [COMM]; 32 bars at 174 ≈ 44 s, the whole form (272–288 bars) ≈ 6:15–6:37 [CALC]. Mean Beatport DnB length is only 3:51 [DOC].
- **Low end**: separate mono sine sub (LP 120 Hz, no detune) under any reese or mid layer high-passed near 120 Hz; a soft reese uses ±15 cents, the DnB signature ±27–30 cents [DOC-2].
- **Detail**: `../36-dnb-engine.md`; `../../../sound-designer-serum/references/basses.md` §1–2; `../../../theorie-musicale-electronique/references/forme-tension.md` §3; sample work `../../../sampling-composition-avancee/SKILL.md`.
