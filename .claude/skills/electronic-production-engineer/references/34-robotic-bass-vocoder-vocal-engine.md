# Robotic bass, vocoder and electronic vocal engine

## Goal
Design intelligible robotic, talking and synthetic timbres without sacrificing low-end stability or vocal articulation.

## Robotic bass architecture
Separate the function of the layers:
- **Sub**: clean, mono-compatible fundamental; minimal modulation.
- **Body**: carries note identity and weight.
- **Articulation/formant layer**: creates talking/robotic motion.
- **Noise/transient layer**: optional edge, click or mechanical attack.

Do not force one patch to do all four jobs when separate layers give cleaner control.

## Serum 2 design routes
### FM / phase distortion route
Use stable carrier pitch plus a modulator at a musically useful ratio. Modulate FM amount rather than only oscillator level. Follow with band-pass/notch/formant-style filtering for speech-like articulation.

### Wavetable/formant route
Use a harmonic or resampled wavetable, then move WT position and filter/formant position from the same macro with different curves. A second modulation source can alter rate or depth for phrase variation.

### Resampled robotic route
Create a simple tone -> automate/filter/distort -> render -> re-import -> scan/resample again. This often produces more distinctive robotic speech than adding more modulators to the original patch.

### Granular/spectral route
Import a vocal, metallic hit or synthetic phrase. Use granular scan or spectral resynthesis for frozen consonant-like textures, machine chatter, metallic vowels and evolving drones.

## Waves vocal tools
### OVox
Use when the voice should become a synth/vocoder or control a carrier.
- Vocal = modulator; synth/instrument = carrier when sidechain carrier mode is used.
- MIDI note control can impose harmony or robotic pitch behavior.
- Add carrier harmonics/drive when intelligibility is weak.
- Resample the result for further chopping or Serum import.

### Vocal Bender
Use for real-time pitch and formant design. The Flatten function is especially useful for intentionally robotic monotone effects. Modulators can create sequenced pitch/formant movement.

### Waves Tune Real-Time
Use for controlled pitch quantization before or after creative processing.
- Slower/more tolerant settings preserve natural singing.
- Fast correction creates deliberate hard-tuned EDM/robotic articulation.
- Use the correct scale/key unless chromatic behavior is intentional.
- Formant correction preserves character when desired; disable/alter character elsewhere if an artificial result is the goal.

### Waves Harmony / OVox layering
Use harmonized voices as carriers, doubles or spectral layers rather than leaving every generated voice full-range.

## Ableton alternatives/complements
- Vocoder: classic modulator/carrier robot voice and drum/synth cross-synthesis.
- Roar: frequency-specific distortion, multiband saturation, feedback and moving nonlinear texture.
- Grain Delay/Beat Repeat/Erosion: glitch and mechanical edge.
- Hybrid Reverb Freeze: turn a vocal or bass fragment into an atmosphere or transition bed.

## Practical chains
### Clean robotic vocal
Tune Real-Time -> corrective EQ -> OVox/Vocoder -> de-ess/soothe if needed -> compression -> delay/reverb sends.

### Aggressive robot chop
Vocal Bender/Flatten -> OVox -> Roar/distortion -> Beat Repeat/stutter -> resample -> Serum Granular/Spectral.

### Talking bass
Serum body/formant layer + separate clean sub -> dynamic EQ/sidechain -> controlled saturation -> peak shaping -> resample selected phrases.

## Label-ready checks
- Speech/formant layer must remain understandable at low playback level.
- Sub should not inherit wide stereo, granular randomness or strong formant modulation.
- Match phrase levels before judging tone.
- Check mono after vocoder, chorus, unison and spectral widening.
- Remove harsh resonances after distortion only where they occur; do not blanket-dull the sound.
