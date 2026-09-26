# Kick, snare, electronic percussion and transient design

Evidence tags as defined in `32-sound-design-engine.md`.

## Principle
A label-ready drum sound is a role-balanced transient, body and tail that works in context. Do not judge a kick or snare only in solo.

## Kick design
### Components
- Transient/click: timing and translation; 2–6 kHz, 5–15 ms `[DOC-2]`.
- Tonal body: note and weight; punch near 100–150 Hz `[DOC-2]`.
- Sub/tail: depth, fundamental usable ≈ 40–60 Hz; competes with bass if too long `[DOC-2]`.

### Synthesis route
Sine/triangle body + fast downward pitch envelope + amplitude envelope. Start: sine 45–50 Hz, pitch envelope +24 to +36 st over 20–40 ms, amp A 0, D 250–500 ms `[DOC-2]`. Serum 2: OSC A sine with ENV 2 → CRS; NOISE one-shot (≈ 5 ms) through a high-pass near 2 kHz for the click; RAND 0 % (same start phase each hit) `[DOC-2]`. With pitch tracking off, a Wavetable oscillator sits at MIDI 0 (≈ 8.2 Hz): OCT +2, SEM +7 gives MIDI 31 ≈ 49 Hz `[DOC p. 35]` `[CALC]`. Sources disagree on a 909-style sweep (15–30 ms vs 200–500 ms): decide by ear `[TEST]`. Add a click only when articulation is missing. Resample once the envelope behaves, then edit waveform/fades directly if simpler.

At 126 BPM a quarter note is 476 ms: a 250–350 ms kick leaves room for the bass, 800 ms excludes an active sub `[CALC]` `[HEUR]`.

Tuning: the 808 kick sits near 49.5 Hz (G1 scientific, G0 in Live naming); stay at or above E1 (41.2 Hz); G1 → D1 costs ≈ −11.8 dB on a pure fundamental, ≈ −4.5 dB on a 5-partial (saturated) kick `[DOC]` (modelled). Tune last, against the bass.

### Layering rules
- One layer owns low body; one layer may own transient (high-passed near 140–150 Hz).
- Avoid several full-spectrum kicks stacked without phase/time checks: 5 ms is half a period at 100 Hz, a full cancellation `[CALC]`.
- Check polarity, then nudge by 0.1–1 ms toward correlation near +1 in 30–80 Hz `[DOC-2]`. A kick that gets louder when a layer is muted has a cancelling layer.
- Align by sound and summed result, not by visual waveform alone.

## Snare design
### Components
- Crack/transient.
- Tonal body: the 808 uses two resonators near 180 and 330 Hz; a single sine/triangle near 160 Hz, decay 250–350 ms, is a starting point `[DOC-2]`.
- Noise band for width and air, on its own envelope (decay 100–600 ms) `[DOC-2]`.
- Optional clap/room/tail. 808 clap: noise → band-pass ≈ 1 kHz, three ~10 ms bursts, a ~20 ms burst, then a ~100 ms tail that is a second envelope, not a reverb `[DOC-2]`.

### FM/electronic route
FM or ring-modulated oscillators can create metallic/robotic bodies. Follow with shaped noise, short envelope and resampling. Icicle's documented DnB workflow is a useful precedent for synthesizing the body rather than relying only on a sample.

### Layering
Tune or pitch-shift body layers until they reinforce rather than flam; a clap under a snare sits 6–8 dB lower `[DOC-2]`. Use micro-delay only deliberately. Width usually belongs more safely to noise/room than to the core transient/body.

## Electronic percussion
Generate percussion from FM/ring modulation, filtered noise, resonant filters, short metallic samples, pitch envelopes, Roar feedback (Feedback Mode Note tunes the ring `[DOC Live 28.33]`) and resampled glitch fragments. Hats: six detuned squares (808 ratios 1 / 1.34 / 1.61 / 1.99 / 2.44 / 2.79 × 320 Hz) or noise, high-passed 6–8 kHz; closed 40–80 ms, open 400–800 ms; closed and open share a choke group `[DOC-2]`.

Then vary velocity, decay, pitch and timing before adding more layers.

## Glitch percussion
Start with a clean hit or loop -> slice/retrigger -> reverse/microfade -> pitch/formant/bit/noise change -> resample -> re-sequence. Keep at least one stable rhythmic anchor while the glitch layer moves.

## Processing order choices
Envelope/transient edit -> tone/EQ -> saturation/clip -> dynamic control -> room/space. Compression is optional, not mandatory. Drum Buss **Transients** acts only above 100 Hz: it cannot fix a kick's sub `[DOC Live 28.12]`.

## QC
- Kick and snare should remain identifiable at low monitoring level.
- Check mono and polarity of layered drums.
- Clip/limit only enough to improve peak-to-body ratio; stop if crack or punch collapses. Crest factor: raw drums ≈ 16–18 dB, drum bus 12–16 dB before the master `[DOC-2]`; measure before and after each processor.
- Compare against references at matched loudness and similar section density.

## Repo resources
- `../../sound-designer-serum/references/percussions.md`; `../../house-future-rave-bass-house-production/recipes/kick-festival-et-future-rave.md`.
- Kits and signature: `../../drums-signature/SKILL.md`; kick vs bass: `../../kick-bass-equilibre/SKILL.md`.
