# Atmospheres, impacts, risers and transition FX engine

Evidence tags as defined in `32-sound-design-engine.md`.

## Goal
Transitions should explain a structural change, not decorate every boundary. Build a small family of reusable but custom-rendered FX from the track's own material. Budget: three to five devices per seam and about two real silences per track; a riser on every transition stops working `[DOC-2]`.

## Atmospheres
Sources: vocal fragments, field recordings, sustained synths, cymbals, metallic hits, reverb tails, granular/spectral renders.

Methods:
- Hybrid Reverb **Freeze** (infinite tail, input cut) or **Freeze In** (input keeps building) to turn a short source into a bed `[DOC Live 28.23]`; Spectral Time's Freezer for rhythmic freezes `[DOC Live 28.37]`.
- Serum Granular/Spectral for evolving textures. Granular bed start: the track's own pad bounced, LENGTH 120 ms, DENS Grains 8–12, SCAN ≈ 5 %, Hann, Jump Start off `[HEUR]`.
- Roar feedback for resonant or degrading atmospheres (Feedback Mode Note sets the ring pitch) `[DOC Live 28.33]`.
- Filter movement plus slow pitch/formant drift.

Keep sub content controlled; atmospheres should not quietly consume low-end headroom. A noise floor sits on its own bus, high-passed near 300 Hz, outside the sidechain and master compression `[DOC-2]`; noise layered on a tonal sound is filtered above that sound's fundamental `[HEUR]`.

## Risers
### Noise riser
Filtered noise + volume curve + widening + optional pitch/frequency motion. Start: white noise band-passed 200 Hz → 8 kHz (exponential) over 8 bars, RES ≈ 30 % `[DOC-2]`; the risers recipe also gives a Serum 2 comb-filter version. 8 bars at 128 BPM = 15 s (ms = 60000 / BPM × beats) `[CALC]`.

### Tonal riser
Sine/saw/sample pitched upward 1–3 octaves, preferably related to track key or target interval; ending off the drop chord (e.g. a semitone under the root) keeps tension `[DOC-2]`. Shepard version: 4–6 octave-spaced copies with bell-shaped levels `[DOC-2]`. For a one-shot sweep inside Serum, use an LFO in MODE **ENVELOPE** or an ENV in BPM mode.

### Resampled riser
Render a synth/vocal/drum gesture, reverse or stretch it, then automate pitch/filter/reverb. Granular version: SCAN range ±400 %, SCAN 0 → +400 % and LENGTH 300 → 15 ms over 4 bars, so the drone turns into a tonal buzz as grains drop below audio-rate length `[HEUR]`.

### Rhythmic riser
Accelerating repeats/stutters, percussion density or gated noise can create tension without a continuous sweep (snare roll 1/8 → 1/16 → 1/32) `[DOC-2]`.

### The build around it
Bus filter: low-pass 300–500 Hz → 16 kHz over the last 8 bars, then high-pass 20 → 400–800 Hz over the last 4 so the bass disappears; automate on a bus `[DOC-2]`. The riser works through what it leaves: cut hard on beat 1 of the drop, reverb tails included `[HEUR]`.

## Impacts
Use 2-4 role layers max when possible:
- low thump/sub impact: sine 60 → 30 Hz, decay 1–2 s, or a sub-drop 80 → 25 Hz over 0.5–2 beats `[DOC-2]`;
- mid transient/body;
- high/noise crack;
- tail/reverb/texture.

Align every layer's peak at the start, keep it near mono, and land it on the same sample as the drop's first hit `[DOC-2]`. High-pass or shorten the tail if it masks the first beat of the new section.

## Downlifters / reverses
Reverse cymbal, vocal, reverb or rendered impact into the boundary. Use fades to avoid clicks and automate stereo/brightness so the target transient still wins. Downlifter: same source as the riser, pitch −12 to −24 st over one bar, low-pass closing, reverb send rising, placed on beat 1 of the new section; riser and downlifter can cross in the last bar `[DOC-2]`. Tape stop: 200–600 ms; in Serum, LFO MODE ENVELOPE → CRS −24 st `[DOC-2]`.

## Glitch transitions
Use Beat Repeat, Maschine Stutter, micro-slices, pitch drops, reverse, Roar feedback, Granular freeze and spectral movement. Render the gesture to audio if exact recall matters.

## Genre routing
- Tech House: brief, clean, often 1-2 beat or 1-bar FX (repo build: filter over 2–4 bars, short riser) `[DOC-2]`; leave a gap before drop.
- Minimal/Deep Tech: micro-fills, delays, small reverses, filtered percussion; avoid oversized cinematic FX.
- Techno: long filters, noise, feedback, reverb freeze and timbral tension arcs are appropriate.
- Bass House/Dubstep: strong impacts, bass fills, stutters and contrast-heavy pre-drop edits.
- Liquid DnB: atmospheres, vocal tails, filtered breaks and tonal FX; preserve musical continuity.
- Minimal DnB: short sub impacts, gated breaks, sparse atmospheres and precise silence.
- Melodic: tonal risers, reverb tails, motif fragments and harmonic tension.
- Afro House: percussion and organic FX should usually lead; digital FX are supporting accents.

## Label-ready QC
- Every FX must have a structural purpose.
- No hidden low-frequency buildup across stacked risers/impacts.
- Check the exact transition at low volume and in mono.
- Ensure the first kick/snare after the transition is not masked by the FX tail.

## Repo resources
- `../../house-future-rave-bass-house-production/recipes/risers-impacts-downlifters.md`; build tables in `arrangement-tech-house-dj-tool.md`, `arrangement-bass-house-160.md`, `arrangement-future-rave-club-mix.md` (same folder).
- `../../sound-designer-serum/references/leads-nappes-textures.md` § 5–6, `moteurs-synthese.md` § 4; bus automation: `../../live-automation/SKILL.md`.
- Local manual: `../../../../corpus/constructeur/live12-manuel-28-live-audio-effect-reference.md`.
