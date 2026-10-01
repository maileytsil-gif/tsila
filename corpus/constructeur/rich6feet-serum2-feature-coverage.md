---
titre: "Serum 2 — couverture des fonctions par un générateur de presets (chemins de paramètres vérifiés) (rich6feet/serum)"
source: https://raw.githubusercontent.com/rich6feet/serum/main/docs/serum2-feature-coverage.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur ; Serum 2 ; format de preset et paramètres (rétro-ingénierie tierce)
skills: sound-designer-serum, vst-sound-design, studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Serum 2 Feature Coverage

A snapshot of which Serum 2 features the prompt-driven preset generator
currently supports, mapped against the Serum 2 User Guide (March 2025) and
the binary format documented by `node-serum2-preset-packager`. This is the
"what we know we don't do yet" reference — useful both for the LLM system
prompt (so the model knows what to emit) and for prioritizing future work.

## Currently supported

These flow end-to-end from prompt → trait inference → semantic mapper →
JSON preset → `.SerumPreset` binary export.


| Area                      | Notes                                                                                                                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5 oscillator source modes | wavetable, sample, granular, multisample, spectral. Spectral pulls from `Samples/`.                                                                                                                       |
| OSC A/B/C + Sub + Noise   | level, position, detune, unison, octave, pan, warp (with calibrated `kParamWarp`/`kParamWarpMenu`), enabled.                                                                                              |
| Granular sub-controls     | density, grainLength, randomPitch, randomGain, randomLength, randomPan, randomDir, scanRate. All calibrated against `cal_oscA.granular_*` captures.                                                       |
| Spectral sub-controls     | filterShift (-1..1, calibrated), mix (0..1, calibrated). Modulation of these knobs from the matrix is not yet calibrated.                                                                                 |
| Multi-rack FX             | optional `fxRacks` (max 3 racks × 5 FX). Legacy `fx.rack` mirrors `fxRacks[0]` so single-rack callers keep working.                                                                                       |
| Filter 1 + Filter 2       | type (string-enum), cutoff (Hz), resonance, drive, routing, enabled. Mapped to verified Serum filter strings (`L12`, `MG Ladder`, `BandReject`, etc.).                                                    |
| ADSR envelopes            | amp / mod1 / mod2 / mod3 with attack / decay / sustain / release / **hold** (optional). Mod1-3 entries derived structurally from amp (Env0) calibration.                                                  |
| LFOs                      | up to 10 (lfo1..lfo10). Per-LFO: rate, shape (`sine`/`triangle`/`square`/`saw`/`sample-hold`), phase (aliased from `rise`), trigger flag. Sample-hold maps to `RandomSH` with `Mode=Free`. lfo2-10 entries derived structurally from lfo1 calibration.   |
| FX rack                   | chorus, phaser, delay, reverb, distortion, bitcrush, tapeSat, hyper, dimension, multibandComp, flanger, eq, compressor. Routed through `FXRack0`. Reverb types restricted to factory-mined `kHall`/`kVintage`/`kAbyss`/`kSpace`.                                  |
| Mod matrix                | up to 64 slots; source list includes envs, LFOs 1-5, velocity (calibrated `[16, 0]`), LFO sources `[6, N]`. `kParamAmount` is now correctly written as `clamp(amount,-1,1) * 100`. Polarity is **inferred** from sign of amount, with **explicit `bipolar` override** as of this revision. |
| Macros                    | up to 8 per preset; semantic mapper now generates 4 per archetype (was 1-2).                                                                                                                              |
| Global                    | voices, glide (portamento time), pitchBend.                                                                                                                                                               |
| Content fallback          | tag-scored substitution → fuzzy basename → first-of-kind → downgrade to wavetable, with `contentWarnings`.                                                                                                |


## Missing — easy and safe to add (good next-PR candidates)

Each of these is a single field that the binary exporter could honor with
a verified parameter path. The schema can grow without breaking existing
presets because every addition is optional.


| Feature                                      | Where in Serum 2                                                                                                                   | Cost                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Voicing `mono` switch                        | `Global0.plainParams.kParamMono` (verify via calibration)                                                                          | one boolean           |
| Voicing `legato` switch                      | `Global0.plainParams.kParamLegato` (verify via calibration)                                                                        | one boolean           |
| Sub osc `phase`                              | `Oscillator3.SubOsc3.plainParams.kParamPhase` (verify)                                                                             | one number            |
| Filter `mix` knob                            | `VoiceFilter{N}.plainParams.kParamMix` (verify)                                                                                    | one number per filter |
| LFO `mode` enum (`free`/`retrig`/`envelope`) | `LFO{N}.plainParams.kParamMode` — we already write `Free` for sample-hold; need calibration to confirm strings for the other modes | one enum per LFO      |
| Macros 1-8 → Filter1Cutoff matrix            | source IDs 25-32 (mining shows these are the most-used factory routes)                                                              | 8 single-state captures |
| modwheel / notenumber / aftertouch sources   | currently `[4, N]` guesses; suspect now that velocity moved to `[16, 0]`                                                            | 3 single-state captures |
| MPE flag                                     | top-level `data.mpeEnabled` + `data.mpePitchBendRange` (the npm packager confirms these)                                           | one boolean + one int |


The recommended workflow per the existing calibration discipline (see
`docs/serum2-calibration-presets-needed.md`) is:

1. Save a Serum 2 init preset.
2. Save a second preset that toggles only the target parameter.
3. Run `npm run analyze:serum2-diff` against the pair.
4. Run `npm run analyze:serum2-map-entry` to add a controlled mapping.

## Missing — risky or large

These either change behavior in non-obvious ways or require substantial new
abstractions. None of them are blockers for the current "sound design from
a prompt" workflow.


| Feature                                              | Why deferred                                                                                                                                                                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FX racks 2 and 3 (`FXRack1`, `FXRack2`) routing      | Schema and writer accept up to 3 racks but the inter-rack routing graph is uncalibrated; today rack 1/2 chains write FX entries without setting the rack-bus routing. Adding routing blind would silently double up effects.   |
| Granular X/Y, window-amount                          | The 8 calibrated controls (density / grainLength / randomPitch / randomGain / randomLength / randomPan / randomDir / scanRate) cover the workhorse params. X/Y and window-amount remain uncalibrated.         |
| Sample slicing                                       | Distinct workflow (slice points, slice→note mappings) that doesn't fit the trait-based mapping cleanly.                                                                                                       |
| Modulating spectral filterShift / spectral mix / warp amount via the matrix | No `destModule*` encoding for these destinations in any current diff. Routes can be specified on the schema side but the binary writer would silently drop them.                                              |
| Pitch quantizer (`PitchQuantizer0` with named scale) | Powerful for melodic prompts ("dorian arp") but changes pitch behavior; safer to leave alone until prompts can carry "scale: dorian" intent end-to-end.                                                       |
| Arpeggiator + MIDI clips (12 each)                   | Whole new content type. Out of scope for prompt-to-preset.                                                                                                                                                    |
| LFO point modulation busses (16 of them)             | Advanced modulation routing. Defer until basic mod matrix is fully exercised.                                                                                                                                 |
| Voice control panel                                  | Per-voice randomization tables. Niche performance feature.                                                                                                                                                    |
| Tuning files (`.tun` / `.scl` / `.kbm` / MTS-ESP)    | Microtuning is orthogonal to sound design from prompts.                                                                                                                                                       |
| Convolve impulse responses                           | Requires shipping IRs; covered by the existing reverb until users specifically ask.                                                                                                                           |
| Equalizer / Bode / Splitter / Utility FX             | Useful but each one needs its own verified param map.                                                                                                                                                         |
| X-Shaper distortion                                  | Custom waveshaper graphs are too unconstrained for trait-based generation.                                                                                                                                    |
| Formula parser, Wavetable editor, Image-to-WT        | Advanced creation tools, not preset-generation primitives.                                                                                                                                                    |


## Not relevant right now

- Wavetable editor and image-to-wavetable import (creation, not preset generation).
- Preset browser / metadata management (the host app, not us).
- DAW-side clip and arp playback (host responsibility).
- MIDI controller assignment (host responsibility).

## What changed in this revision

- **Macros**: heuristic now fills 4 per archetype instead of 1-2 (Serum supports 8).
- **Matrix `bipolar` override**: optional explicit field on `matrix[i]`. When set, the binary exporter writes `kParamBipolar` from the override. When absent, behavior is unchanged (negative amount → bipolar, positive → unipolar).
- **Matrix `kParamAmount` writer fix**: the previous revision wrote source/destination/bipolar but silently *omitted* `kParamAmount`, leaving every matrix slot at the seed default (zero). Routes are now written as `clamp(amount, -1, 1) * 100`, matching the encoding used by `verify_presets.py`. This is the most consequential fix in this revision — every preset's modulation matrix that previously produced no audible motion now does.
- **Source-ID corrections (calibration)**: `lfo1` moved from guessed `[1, 0]` to verified `[6, 0]`; `velocity` moved from guessed `[4, 0]` to verified `[16, 0]`. lfo2..lfo5 generalized to `[6, N-1]`.
- **Granular controls**: all 8 calibrated and wired through the schema, validator, semantic mapper, and binary writer.
- **Spectral controls**: filterShift and mix calibrated and wired.
- **Multi-rack FX**: optional `fxRacks` (max 3 × 5). Legacy `fx.rack` mirrors `fxRacks[0]`.
- **Warp menu**: `kParamWarp` and `kParamWarpMenu` calibrated. Only `kSync` is calibration-verified; other strings pass through with a validator warning.
- **ADSR `hold` stage**: optional, default 0. Backward-compat — older presets behave identically.
- **Reverb types**: restricted to factory-mined `kHall` / `kVintage` / `kAbyss` / `kSpace`. `kPlate` / `kRoom` / `kCathedral` are Serum 1 names and were never seen in the Serum 2 factory tree.
- **MPE warning**: still surfaced in `metadata.unsupportedFeatures` because the data flag exists in the binary format but we have not calibrated end-to-end behavior. See "easy and safe" above.