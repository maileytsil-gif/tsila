# Transposition engine — degrees first, notes second

## Mandatory order
1. Store the progression as **scale degrees / Roman numerals**.
2. Resolve the active key/mode.
3. Convert degrees to pitch classes.
4. Build chord quality from the selected scale or an explicitly declared borrowed/harmonic-minor chord.
5. Choose inversions by voice-leading, not by root-position habit.
6. Place the independent bass in the register required by the sound.
7. Output exact MIDI numbers.

## Guardrails
- Do not silently replace a modal degree with a major/minor functional equivalent.
- When a progression uses a non-diatonic chord, label it: `borrowed`, `secondary/altered dominant`, `modal interchange`, or `chromatic color` when known.
- If a requested key pushes a bass note below the useful register, octave-shift the bass **without changing the degree**.
- Preserve melodic contour during transposition; then re-check singability/playability.

## Variation axes
A progression can be varied without changing its identity by changing:
- inversion;
- top note;
- chord extension/add note;
- harmonic rhythm;
- bass inversion/pedal;
- anticipation/delay;
- octave/register;
- articulation.

[HEUR] Prefer changing one or two axes at a time so the A/B comparison teaches something.
