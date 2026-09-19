# Ableton Live 12 — MIDI generation workflow v11

[DOC] Live 12 separates **Transformations** (operate on existing notes) from **Generators** (create material). With Scale Mode enabled, pitch-related controls use the active scale/degrees.

## Chords
1. Set clip scale.
2. Start with the library progression by degree.
3. Use **Stacks** to explore alternate chord shapes if desired.
4. Rewrite/select the useful version; do not accept generated voicings automatically.
5. Use **Strum** only when temporal spreading supports the instrument.

## Melody
1. Write a 1–2 bar motif manually or use Seed/Shape for raw material.
2. Restrict pitch range.
3. Convert the best fragment into a motif.
4. Use Recombine sparingly to rotate pitch/rhythm/velocity relationships.
5. Use Connect only when the phrase needs interpolation; delete excess notes.

## Bass
1. Begin from chord degrees or a modal pedal.
2. Use Rhythm to explore placement while holding one pitch if groove is the unknown variable.
3. Add pitch changes only after the rhythm works.
4. Keep note ends under control; low-end overlap is musical and technical.

## Humanization
- Quantize Amount can move notes partway toward the grid [DOC].
- Velocity Shaper can impose a controlled velocity contour [DOC].
- Humanization is not randomization: preserve the groove's strong/weak hierarchy [HEUR].

## Rule
Every generated result must pass: `motif recognition → harmonic fit → register → groove → section function → originality`.
