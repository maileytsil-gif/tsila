# Reverse / Pre-FX / Suckback Engine

## Goal
Use reversed or inward-moving material to *prepare* a transient, note, vocal, drop, fill or section change. Reverse FX should create directional expectation, not constant decoration.

## Core families

### 1. Reverse cymbal / reverse crash
Best for: pre-drop lift, section boundary, phrase ending, gentle rise.

Workflow:
1. Choose a crash/ride/metallic tail whose tone fits the track.
2. Trim silence and unnecessary low end.
3. Reverse the audio.
4. Fade in from silence; shape the end so the peak lands exactly before the target transient.
5. High-pass or shorten if the tail masks the kick/snare on the boundary.
6. Optional: widen the upper band, automate high shelf/filter, then print/resample.

For a less generic result, create the source cymbal from the track's own hats/noise/metallic percussion before reversing.

### 2. Reverse reverb / suckback
Best for: vocal entries, snare entries, synth stabs, impacts, emotional transitions.

Workflow:
1. Isolate the target word/hit/note.
2. Render a long wet reverb or delay+reverb tail.
3. Print/bounce the tail.
4. Reverse the printed tail.
5. Align the end of the reverse exactly to the dry target event.
6. EQ the reverse so it supports rather than masks the target.
7. Duck or fade the last 20-100 ms if the target transient loses definition.

This works especially well with vocals, snares, piano/chords and tonal impacts.

### 3. Reverse impact
Create the impact first, then reverse all or selected layers.

Forward impact roles:
- sub/thump;
- mid body;
- high crack/noise;
- tail/room.

Reverse options:
- reverse only tail for a suck-in;
- reverse body+tail for a stronger vacuum effect;
- keep sub out of the reverse to preserve headroom;
- reverse a filtered version and layer under the dry impact.

### 4. Reverse kick / reverse snare
Use as a pre-hit accent, not a replacement for the main transient.

Reverse kick:
- often high-pass the reversed version so the pre-hit does not build excessive sub;
- shorten so the energy ramps into the real kick;
- use pitch automation or a tonal tail if a key-aware transition is desired.

Reverse snare:
- useful before fills and DnB snare accents;
- render reverb first for a longer, smoother pre-swell;
- for glitch styles, slice the reverse into 1/8-1/32 fragments and retrigger.

### 5. Reverse bass as transition FX
This is a reversed or inward-moving bass gesture used before a drop/phrase.

Method A — reverse rendered bass:
1. Render a short bass stab/growl from the actual drop sound.
2. Remove/attenuate true sub if necessary.
3. Reverse.
4. Automate filter, width and level into the drop.
5. End before the main sub/kick arrives.

Method B — granular/spectral reverse:
- Serum 2 Granular: reverse grain direction and/or reverse scan direction; tempo-lock scan when useful.
- Freeze/scan a recognizable fragment, then automate toward the target boundary.
- Keep a separate clean sub out of the reversed granular layer.

### 6. Reverse bass as a rhythmic/synthesis style
Do not confuse transition reverse-bass with hardstyle/hard-techno reverse-bass design.

For rhythmic reverse-bass:
- build the amplitude shape so energy swells *after* the kick rather than attacking like a normal bass pluck;
- use LFO/envelope movement, distortion and EQ to create the characteristic suction/bounce;
- preserve kick/sub separation;
- resample and re-align phase/timing against the kick;
- treat Serum 2 LFO/pitch/drive movement as sound design, not merely an audio-reverse operation.

Use this only when the genre DNA supports it (hard dance, harder techno hybrids, selected electro/bass contexts).

### 7. Reverse vocal
Two main types:

A. Reverse word/syllable
- duplicate one syllable/word;
- reverse;
- time-stretch/pitch/formant if desired;
- place before the original or use as an independent texture.

B. Reverse vocal reverb/delay
- render H-Delay/R-Verb or another delay/reverb tail;
- reverse and tuck under the phrase;
- emphasize useful mids/highs while cleaning low-end.

For robotic vocals, combine with OVox/Vocal Bender/Waves Tune before rendering the tail, then reverse/resample.

### 8. Reverse noise / downlifter / uplifter
- reverse a downlifter to create an uplifter or vice versa;
- automate filter cutoff, pitch and width;
- add amplitude curvature rather than a linear fade if stronger acceleration is needed;
- resample through Roar/distortion for a more custom timbre.

### 9. Reverse granular / spectral FX
Serum 2 Granular can reverse grain direction and reverse the scan direction. Use this for:
- granular suck-ins;
- metallic reverse clouds;
- vocal-to-texture transitions;
- bass fragments that morph into a drop.

Maschine Grain Delay also provides reverse grain playback; this is useful for resampled ambient/glitch reverse textures.

### 10. Reverse kit / multi-sample gesture in Maschine
Maschine can reverse a Sampler sound at playback and can destructively reverse selected regions in the Sample Editor. Use it to:
- reverse multiple drum samples for a custom pre-fill kit;
- build reversed hats/cymbals/rims;
- reverse a selected slice rather than the whole recording;
- resample the result into a single transition gesture.

## Ableton-native workflow
Live can reverse a clip or an Arrangement selection and creates a new reversed sample copy. Simpler also has a non-destructive Reverse function. This makes Ableton the preferred editor for precise boundary alignment.

Recommended chain for a reverse transition:
source -> print/resample -> reverse -> trim/fades -> EQ -> optional saturation/granular -> automation -> final print

## Timing library
Starting points only:
- 1/4 note: micro suck-in / pre-snare;
- 1/2 note: compact Tech House/Minimal transition;
- 1 bar: common pre-drop reverse cymbal/impact;
- 2 bars: melodic/techno atmospheric swell;
- 4-8 bars: long cinematic/melodic tension only when arrangement supports it.

## Genre routing
- House: musical reverse cymbals, vocal reverb and chord tails; keep them smooth.
- Tech House: short reverse crash/vocal/impact; often 1/2-1 bar; protect the drop transient.
- Minimal/Deep Tech: tiny reverses, rim/perc suckbacks, very little cinematic FX.
- Techno: longer reverse noise, feedback, granular and metallic textures are appropriate.
- Bass House: reverse growls, bass pre-fills, vocal reverses, aggressive impacts.
- Melodic Dubstep: long tonal/vocal reverse reverbs and cinematic suck-ins into drops.
- Liquid DnB: reverse vocals, cymbals, pads and break tails; preserve emotional continuity.
- Minimal/Deep DnB: short reverse snare/cymbal/bass gestures, sparse and precise.
- Afro House: organic cymbal/percussion reverses and vocal reverb; avoid over-digitalizing the groove.

## Label-ready QC
- The reverse must point *to* a target event; if the destination is unclear, remove it.
- Align the terminal peak sample-accurately or intentionally leave a short gap.
- Remove hidden sub from long reverse tails unless low-frequency buildup is deliberate.
- Check mono and low-volume playback.
- Make sure the first kick/snare after the reverse still owns the transient.
- Print complex reverse chains when final timing matters.
- For every repeated transition, vary source, length, filter or timing to avoid template fatigue.
