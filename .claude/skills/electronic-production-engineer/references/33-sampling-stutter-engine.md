# Sampling, resampling and stutter engine

## Goal
Treat samples as raw synthesis material, not fixed loops. Choose the least-destructive path first, then resample when committing creates a useful new source.

## Source audit
Before processing, identify:
- role: drum, vocal, bass, tonal phrase, texture, field recording, FX;
- transient density and tail length;
- key/root if tonal;
- tempo and warp requirement;
- whether timing or timbre is the main target;
- whether the sample must remain editable or can be committed by resampling.

## Ableton roles
### Simpler
Use for fast one-shot playback, slicing and rhythmic reconstruction.
- Slice by transient for organic chops.
- Slice by beat/grid for predictable retrigger patterns.
- Manual slices for intentional vocal/percussion phrasing.
- Warp when pitch must change without destroying timing, then compare against unwarped pitch-shift for character.
- Move useful slices to a Drum Rack when pad-style performance is preferable.

### Sampler
Use when the source should become a deeper playable instrument: zones, key/velocity mapping, looping, modulation, filters and layered multisample behavior.

### Arrangement micro-editing
Use direct audio edits when the desired result is exact and section-specific: 1/8 -> 1/16 -> 1/32 retriggers, reverses, gaps, slip edits, fades and pre-drop cuts.

### Beat Repeat
Use for controlled or probabilistic repeats. For a guaranteed transition, automate it deterministically; use Chance only when variation is desired.

## Maschine 3 + MK3 roles
Use Maschine when tactile capture and variation are the priority.
- Record or import source -> Detect/Split/Grid/Manual slice -> map to pads -> perform a new phrase.
- Use Live Slicing when cutting by ear while the material plays.
- Use Perform FX Stutter for real-time retrigger, gate, pitch and direction gestures.
- Resample the performed result so the gesture becomes editable audio rather than an unrepeatable live move.

## Serum 2 roles
### Sample oscillator
Use for tuned one-shot playback, looping, slicing, rate/tape-stop motion and sample-based FM/PD/distortion workflows.

### Granular oscillator
Use when micro-time is the sound-design target: freeze-like grains, scan modulation, rhythmic grain size, pitch spread, stereo movement and texture generation.

### Spectral oscillator
Use when the goal is frequency-domain resynthesis rather than ordinary playback: harmonic freeze, time/pitch decoupling, robotic or atmospheric transformations.

### Wavetable resampling
Render a complex gesture and re-import it as wavetable/sample material when the movement itself is the desired oscillator shape.

## Stutter families
1. **Rhythmic retrigger**: fixed 1/8, 1/16, 1/32 or triplet repeats.
2. **Micro-chop**: rearranged tiny slices with gaps and velocity changes.
3. **Pitch stutter**: repeated slice with pitch envelope, rate or formant motion.
4. **Granular stutter**: scan/freeze tiny grains with controlled randomness.
5. **Glitch stutter**: retrigger plus reverse, bit reduction, feedback, spectral or ring-mod processing.

## Genre behavior
- Tech House: short vocal/percussion stutters before transitions; keep them sparse.
- Minimal/Deep Tech: subtle ghost-like micro-stutters and occasional displaced edits.
- Techno: longer repetitive or granular stutters can become a tension device.
- Bass House/Dubstep: use stutters as call-and-response punctuation between bass phrases.
- Liquid DnB: use lightly on vocals, ambience or fills so musical flow remains intact.
- Minimal DnB: micro-edits, gated breaks and clipped silence can be a central groove language.
- Afro House: prefer organic/percussive stutters over obviously digital machine-gun repetition unless stylistically intentional.

## Iterative sound-design loop
Source -> slice -> perform/resequence -> resample -> clean/warp -> process -> resample -> load into Serum Sample/Granular/Spectral -> render new one-shot/loop -> arrange.

Stop iterating when each pass stops adding a clearly useful identity.
