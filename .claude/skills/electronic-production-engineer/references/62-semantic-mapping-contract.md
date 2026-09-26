# Semantic mapping contract

## Why
AI instructions should target musical meaning, not fragile plug-in indexes. The bridge translates stable semantic names into the actual Live DeviceParameter objects discovered at runtime.

## Canonical track names
Performance bank:
- `T01_KICK`
- `T02_BASS`
- `T03_DRUMS`
- `T04_PERC`
- `T05_MUSIC`
- `T06_VOCAL`
- `T07_FX`
- `T08_LOOP`

Utility bank may include:
- `T09_SUB_EXTRA`
- `T10_SYNTH_2`
- `T11_VOCAL_FX`
- `T12_RESAMPLE`
- `T13_MASCHINE`
- `T14_REFERENCE`
- `T15_SIDECHAIN`
- `T16_PRINT`

## Canonical Rack names
- `RACK_KICK`
- `RACK_BASS`
- `RACK_DRUMS`
- `RACK_PERC`
- `RACK_MUSIC`
- `RACK_VOCAL`
- `RACK_FX`
- `RACK_LOOP`

## Performance macros 1-8
- `M01_TONE`
- `M02_PUNCH`
- `M03_BODY`
- `M04_DRIVE`
- `M05_MOVEMENT`
- `M06_SPACE`
- `M07_WIDTH`
- `M08_LEVEL`

## Technical macros 9-16
Names may vary by Rack but should remain explicit and stable, for example:
- `M09_SUB_LEVEL`
- `M10_SC_DEPTH`
- `M11_SC_RELEASE`
- `M12_SOOTHE_DEPTH`
- `M13_SAT_AMOUNT`
- `M14_MONO_FREQ`
- `M15_OUTPUT_TRIM`
- `M16_SAFETY`

## Semantic parameter vocabulary
Map plug-in-specific names into these families when possible:
- `FILTER_CUTOFF`, `FILTER_RESONANCE`, `FILTER_DRIVE`
- `AMP_ATTACK`, `AMP_DECAY`, `AMP_SUSTAIN`, `AMP_RELEASE`
- `OSC_POSITION`, `OSC_BLEND`, `DETUNE`, `SUB_LEVEL`
- `LFO_RATE`, `LFO_DEPTH`, `MOVEMENT_AMOUNT`
- `TRANSIENT_ATTACK`, `TRANSIENT_SUSTAIN`
- `COMP_THRESHOLD`, `COMP_RATIO`, `COMP_ATTACK`, `COMP_RELEASE`, `COMP_MIX`
- `SIDECHAIN_DEPTH`, `SIDECHAIN_RELEASE`
- `SATURATION_DRIVE`, `CLIP_AMOUNT`
- `SOOTHE_DEPTH`, `DYNAMIC_EQ_AMOUNT`
- `REVERB_SEND`, `DELAY_SEND`, `FX_MIX`
- `STEREO_WIDTH`, `MONO_CUTOFF`
- `OUTPUT_LEVEL`, `OUTPUT_TRIM`

## Resolution strategy
For each semantic target:
1. prefer a canonical Rack macro with exact name,
2. else prefer exact user/plugin parameter mappings stored in a verified profile,
3. else use name normalization/synonyms and score candidates,
4. if confidence is low or multiple candidates are plausible, return an inspect/clarify action rather than writing.

## Never infer from position alone
`parameter[17]` is not a stable semantic identity. Indexes may only be used after the bridge has matched and verified names/ids in the current session.
