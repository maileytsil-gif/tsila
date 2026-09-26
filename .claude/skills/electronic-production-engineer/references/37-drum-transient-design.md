# Kick, snare, electronic percussion and transient design

## Principle
A label-ready drum sound is a role-balanced transient, body and tail that works in context. Do not judge a kick or snare only in solo.

## Kick design
### Components
- Transient/click: establishes timing and translation.
- Tonal body: carries the perceived note/weight.
- Sub/tail: supplies depth but competes with bass if too long.

### Synthesis route
Sine/triangle body + fast downward pitch envelope + amplitude envelope. Add a short noise/click layer only when articulation is missing. Resample once the envelope behaves correctly, then edit the waveform/fades directly if simpler.

### Layering rules
- One layer owns low body.
- One layer may own transient.
- Avoid several full-spectrum kicks stacked without phase/time checks.
- Align by sound and summed result, not by visual waveform alone.

## Snare design
### Components
- Crack/transient.
- Tonal body (often lower-mid; exact frequency depends on tuning/source).
- Noise band for width and air.
- Optional clap/room/tail.

### FM/electronic route
FM or ring-modulated oscillators can create metallic/robotic bodies. Follow with shaped noise, short envelope and resampling. Icicle's documented DnB workflow is a useful precedent for synthesizing the body rather than relying only on a sample.

### Layering
Tune or pitch-shift body layers until they reinforce rather than flam. Use micro-delay only deliberately. Width usually belongs more safely to noise/room than to the core transient/body.

## Electronic percussion
Generate percussion from:
- FM/ring modulation;
- filtered noise;
- resonant filters;
- short metallic samples;
- pitch envelopes;
- Roar feedback/resonance;
- resampled glitch fragments.

Then vary velocity, decay, pitch and timing before adding more layers.

## Glitch percussion
Start with a clean hit or loop -> slice/retrigger -> reverse/microfade -> pitch/formant/bit/noise change -> resample -> re-sequence. Keep at least one stable rhythmic anchor while the glitch layer moves.

## Processing order choices
Envelope/transient edit -> tone/EQ -> saturation/clip -> dynamic control -> room/space. Compression is optional, not mandatory.

## QC
- Kick and snare should remain identifiable at low monitoring level.
- Check mono and polarity of layered drums.
- Clip/limit only enough to improve peak-to-body ratio; stop if crack or punch collapses.
- Compare against references at matched loudness and similar section density.
