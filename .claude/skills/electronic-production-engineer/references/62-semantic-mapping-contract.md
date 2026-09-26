# Semantic mapping contract

## Why
AI instructions should target musical meaning, not fragile plug-in indexes. The bridge translates stable semantic names into the actual Live DeviceParameter objects discovered at runtime.

## Canonical track names
These names are the template for new projects (same list in `bridge/semantic-vocabulary.json`). They are suggestions, never a reason to rename an existing project.

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

## Names in the studio's existing Sets
The Sets actually worked on here use `AUDIO - <ROLE>` tracks → `BUS - <GROUP>` (e.g. `BUS - BATTERIE`, `BUS - BASSES`, `BUS - HARMONIE`, `BUS - CORDES`) → `BUS MASTER 1` → `2` → `3` → Main, with `REF` straight to Main ([ableton-live-session](../../ableton-live-session/SKILL.md), [mix-chain.md](../../ableton-live-session/references/mix-chain.md)). Resolve against these real names, read from `lom.py state --json`, and keep a per-project alias table (canonical role → real name) in the project memory.

## Canonical Rack names
- `RACK_KICK`
- `RACK_BASS`
- `RACK_DRUMS`
- `RACK_PERC`
- `RACK_MUSIC`
- `RACK_VOCAL`
- `RACK_FX`
- `RACK_LOOP`

Inserting a Rack to host macros is a device insertion (high impact) and the Rack is a native Live device, while the user has asked for no new native effects in mix chains: ask before introducing one [TEST whether macro Racks are acceptable as containers]. Whether a renamed macro's custom name is what the bridge's `params` returns is [TEST].

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

A family is only reachable when the parameter is exposed to Live: Serum 2 synth families need Configure first, and soothe3 or Pro-Q 4 families expose nothing in this studio ([64](64-plugin-profile-strategy.md)). Mixer families map to `lom.py param "<track>" mixer Volume|Pan|"Send A"`.

## Resolution strategy
For each semantic target:
1. prefer a canonical Rack macro with exact name,
2. else prefer exact user/plugin parameter mappings stored in a verified profile ([64](64-plugin-profile-strategy.md)),
3. else name normalization/synonyms may only produce candidates for a human to confirm: return `needs_mapping`, never write from a scored guess,
4. if confidence is low or multiple candidates are plausible, return an inspect/clarify action rather than writing.

Pass the full exact name read from `state --json` / `params`. The bridge matches case-insensitively, exact first, else a unique substring (several matches → `E_AMBIGUOUS`); check that the name it echoes back is the intended one. A digits-only name falls back to an index: never send one.

## Never infer from position alone
`parameter[17]` is not a stable semantic identity. Indexes may only be used after the bridge has matched and verified names/ids in the current session. For plug-ins, the index is the order chosen in Live's Configure panel; "Save as Default Configuration" makes it repeatable for new instances, but Serum 2 has shifted FX parameter indexes after reload (fixed in 2.0.18) and shown wrong macro names after Set load (workaround in 2.0.21) ([serum2-automation-et-migration.md](../../sound-designer-serum/references/serum2-automation-et-migration.md)). Confirm name and display value, or a small approved test move, in each session.
