# House DNA

## Four reference producers/tracks
- Daft Punk — One More Time: repetition, filtering, density from processing and arrangement economy.
- Kerri Chandler — Bar A Thym: deep groove, microtiming, endurance of a loop.
- Dennis Ferrer — Hey Hey: vocal as hook and rhythmic element; space around bass/vocal.
- Folamour — These Are Just Places To Me Now: warmer/funkier musicality and preserved dynamics.

## Arrangement DNA
Breaks often remove or soften kick/bass while retaining a rhythmic cue, chord, vocal or hat. Bridges/builds rely on filtering, automation, percussion and small tension changes more than giant EDM snare rolls. Drops are often the return of the complete groove rather than a sudden wall of sound.

## Mix priorities
Groove > raw loudness. Preserve musical bass movement, warm mids and timing. Saturation may provide density, but avoid flattening the pocket.

## Numbers
Evidence tags: see `../10-genre-router.md`.
- **Tempo**: Beatport House Top 100 most frequent 127, 125, 124, 128, 126 BPM; Deep House 126, 124, 122 [DOC WhatBPM 2023]. Spotify medians: house 123, deep house 123 (IQR 118–125), Chicago house 124 [DOC]. Default **124** for deep/classic club house, **126** for current Beatport house [HEUR].
- **Swing** (Linn %: 50 straight, 66 triplet): house 52–56 % on hats only [COMM]; deep house 55–62 % [DOC-2]. Never on kick or clap. Studio grid uses `swing(0.03, n/16)` at 120 BPM; the Producer Pal unit is undocumented, read the clip back [TEST].
- **Keys/modes**: manual annotations: house 83 % minor (G, C, A minor lead), deep house 95 % minor (C, B♭, B minor lead) [DOC GiantSteps, n = 47 / 77]. Dorian vamp i7–IV7 (Am7–D7); always 7ths/9ths; the stab omits the root when the bass holds it (Kerri Chandler m9/11) [DOC-2]. A "major" key from Spotify/Tunebat on a club track: presume the relative minor until checked by ear [DOC].
- **Sections** (multiples of 8): additive club house, no drop: drums 16 · +bass 16 · +chords 16 · +vocal 16 · breakdown 16 · build 16 · main 64 · reduced 24 · outro 16 = 200 bars ≈ 6:27 at 124 [COMM; CALC]. DJ intro/outro 16–32; first melodic element not before bar 17 or 33 [DOC-2]. Mean Beatport length: House 6:02, Deep House 6:33 [DOC].
- **Low end**: bass in MIDI 33–45 (55–110 Hz); off-beat organ/M1 bass gate 50–60 %, off-beats v100–110, 16ths v70–85 [COMM]; no third below MIDI 48 (C2 in Live), no fifth below MIDI 34 [DOC-2]; a discreet sub glide is 40–80 ms at 120–126 BPM [HEUR].
- **Detail**: `../../../house-future-rave-bass-house-production/references/theorie-specifique.md` (§4.4 bass grids, §5 swing), `../../../house-future-rave-bass-house-production/references/genres-et-elements.md`, `../../../house-future-rave-bass-house-production/references/arrangement-et-methode.md` §1.1; grid `../../../drums-signature/references/patterns.md` (deep/minimal house); harmony `../../../theorie-musicale-electronique/references/genres.md` (House).
