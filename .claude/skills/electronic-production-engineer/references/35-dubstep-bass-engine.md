# Dubstep / melodic dubstep / robotic bass engine

Evidence tags as defined in `32-sound-design-engine.md`.

## Core distinction
### Melodic dubstep
Emotion and harmony lead. Bass sound design supports the chord/melody arc. Wide supersaws, vocal texture, sub reinforcement and contrast between breakdown and drop are central.

### Robotic / aggressive dubstep
Bass phrasing and timbre are the hook. Call-and-response, resampling, formant movement, metallic partials and silence are central.

A hybrid can use melodic breakdowns with robotic drops; define which DNA owns each section.

Dubstep sits around 140 BPM in half-time, with sparse drums that leave the bass room; bass house borrows those half-time bass rhythms over a four-on-the-floor kick, so its growl must be a mid-bass (high-passed near 100 Hz) over a separate sub `[DOC-2]`.

## Bass design system
1. Write the rhythm before over-designing the patch.
2. Keep sub as a dedicated layer where possible: sine, mono, UNISON 1, no LFO or saturation.
3. Design 2-4 contrasting mid-bass identities rather than one preset repeated everywhere; design each at UNISON 1 (a mono growl hits harder) `[DOC-2]`.
4. Use modulation to articulate phrases, not to make every parameter move constantly.
5. Resample successful gestures and edit them as audio.

## Serum 2 methods
Exact labels: `../../sound-designer-serum/references/serum2-cartographie.md`.
- FM/ratio modulation for metallic or growling spectra: WARP `FM (B)` with OSC B in Ratio mode; repo starting points `[DOC-2]`, low reliability: FM 15–25 % guttural, above 40 % metallic/screaming; Bend +/− 30–50 % nasal.
- Wavetable resampling for custom harmonic movement.
- Band-pass/notch/formant movement for talking vowels: Formant-I/II/III (VAR = FORMNT), RES 20–40 `[DOC]` `[DOC-2]`; comb/Dist.Comb or Scream LP/BP (DRIVE above 50 %) for metal and scream `[DOC p. 138]`.
- Granular/Spectral oscillators for hybrid organic/robotic textures.
- Sample oscillator for one-shot mechanical hits, vocal fragments and tape-stop gestures (SCAN, Reverse).
- LFOs driving a growl run in MODE **RETRIG**, otherwise each note catches a different phase `[DOC-2]`. Growl recipes online assume 140–150 BPM; convert synced divisions by the actual tempo `[DOC-2]`. At 140 BPM, ms = 60000 / 140 × beats: 1/2 = 857, 1/4 = 429, 1/8 = 214, 1/8 T = 143, 1/16 = 107 `[CALC]`; the same 1/2 at 126 BPM lasts 952 ms, too slow for bass house `[CALC]`.
- Macros should expose musical concepts: TALK, METAL, BITE, MOVEMENT, WIDTH, AIR, SUB LEVEL, FX. SUB LEVEL is gain only; WIDTH acts above the sub. Map them to the Rack slots of `62-semantic-mapping-contract.md` (BITE → M04_DRIVE, MOVEMENT/TALK → M05_MOVEMENT, FX → M06_SPACE, WIDTH → M07_WIDTH) `[HEUR]`.

## Au5-style hypergrowl principle
The useful lesson is the process, not copying a patch: generate/resample a simple source into a more complex wavetable, then shape formant-like motion with filtering and controlled modulation. Re-resample if the movement becomes more interesting than the original oscillator. In Serum: main menu › Rendering › **Resample to** (one bar of a note → wavetable) or **Render OSC Warp** (256 frames across 0–100 % WARP) `[DOC p. 324]`. Two or three passes, changing the modulation rhythm each pass, build density no single pass reaches `[DOC-2]`.

## Drop grammar
Call A -> gap -> Response B -> fill -> variation A2 -> contrast response -> turnaround.

The gap is part of the sound. Do not fill every sixteenth with bass.

## Melodic layer strategy
- Separate chords/pads from the heavy bass bus.
- Duck or arrange rather than forcing all layers to win the same midrange.
- Use vocal/lead themes to connect breakdown and drop.
- Let reverb tails live mainly outside the densest bass hits.
- Supersaw starting points: UNISON 5–7, DETUNE ≈ 0.09–0.12, BLEND 75 % (default), RAND 100 % phase; three chord notes at most on a supersaw `[DOC]` `[DOC-2]`; one wide element at a time `[HEUR]`.

## Processing
Typical order is not mandatory: source -> filter/tone -> distortion/saturation -> corrective dynamic control -> stereo shaping above sub -> clip/peak control -> resample.

Serum 2 in one instance `[DOC-2]`: Splitter L/M/H at 120 Hz / 2 kHz (LOWS clean, MIDS Distortion Tube then Hard Clip — several light stages beat one heavy one, HIGHS light Tube); Compressor MULTIBAND MIX 15–25 % on a bass, 30–50 % per band; Utility MONO BASS 120–150 Hz. Growl EQ start: high-pass 120 Hz, −3 dB near 400 Hz `[DOC-2]`.

Use soothe3 only when distortion produces moving harshness that cannot be solved by a better source/filter/drive setting.

## Label-ready criteria
- Bass phrase remains readable on small speakers because useful harmonics exist above sub.
- Sub does not disappear in mono.
- Main snare owns a clear transient window.
- Drop has contrast between bass identities and rests.
- Resampled assets are gain-matched and trimmed to prevent hidden peak accumulation; compare versions at matched loudness.

## Repo resources
- Growl, Reese and bass-house/dubstep split: `../../sound-designer-serum/references/basses.md` § 2–3, `fiches-pratiques.md` (sheets 03, 04, 37), `patches-genres.md` § 5–7 (same folder).
- Three-layer drop and FM bass: `../../house-future-rave-bass-house-production/recipes/drop-bass-house-trois-couches.md`, `basse-fm-metallique-bass-house.md`.
- Supersaw data: `../../sound-designer-serum/references/leads-nappes-textures.md` § 2.
