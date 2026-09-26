# Melodic House / Techno DNA

## Four references
- Tale Of Us — Nova: depth, long envelopes, simple motif and spatial tension.
- ARTBAT — Horizon: large lead + club low-end coexistence.
- Stephan Bodzin — Singularity: synth as expressive instrument; automation creates narrative.
- Anyma & Rebūke — Syren: modern spatial sound design and tightly controlled low-end.

## Arrangement DNA
Break is a composition inside the composition: theme exposed -> harmonic/spatial development -> tension -> pre-drop gap -> rhythmic return. The same lead can shift from emotional in the break to rhythmic/physical in the drop.

## Mix priorities
Depth layers, reverb frequency control, automation, low-end headroom and center stability. Preserve contrast between expansive breaks and focused drops.

## Numbers
Evidence tags: `../80-evidence-policy.md`; data caveats: `../10-genre-router.md`.
- **Tempo**: Beatport Melodic House & Techno Top 100: 124 (29 tracks), 125 (15), 122 (13), 126 (10), 123 (8) [DOC WhatBPM 2023]. Anyma, ARTBAT and Tale Of Us originals in the repo's Spotify set: 124–128, mostly 125–127 [DOC, Spotify estimate]. Theory table: melodic techno 120–126, typical 124 [DOC-2]. Default **124** [HEUR].
- **Groove**: straight, no swing. Studio grid: kick v100–108, clap 2 & 4 v62–72, off-beat hats v66–76, hat ghosts on 16th steps 2, 8, 10, 16 at v30–42, perc on steps 6 and 12 [HEUR, studio grid `melodictechno`] — softer than techno.
- **Keys/modes**: minor (A, F, D, C); i–VI–III–VII (Am add9 – Fmaj7 – Cmaj9 – Gsus2, 2 bars per chord = an 8-bar loop), i–III–VII–VI, i–iv–VI–V with V as sus4, or a drone i–i–VI–VI; never bare triads; pads C3–C5 (Live naming); the melody arpeggiates the progression [DOC-2]. Beatport auto-keys for this chart lean "major" (E, D, C): indicative only, check the relative minor by ear [DOC; HEUR].
- **Sections**: genre-specific lengths not verified in repo. Start from 16–32-bar blocks (house/techno DJ scheme) [COMM] and give the break at least 16 bars to state and develop the theme [HEUR]. Mean Beatport length 6:39 [DOC].
- **Low end**: roots under 120 Hz mono; no third below MIDI 48 (C2), no fifth below MIDI 34; kick tuned to the tonic or fifth, sub on the root only [DOC-2]; `theorie.py sub <tonic>` prints the table [CALC].
- **Detail**: `../../../theorie-musicale-electronique/references/genres.md` (Techno › Melodic), `../../../theorie-musicale-electronique/references/harmonie-avancee.md`; `../../../drums-signature/scripts/drum_pattern.py`; motif writing `../../../melodie-composition/SKILL.md`.
