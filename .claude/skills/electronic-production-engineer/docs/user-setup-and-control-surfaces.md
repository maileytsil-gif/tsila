# User setup and control surfaces

## Ableton Live 12 Suite

Live is the canonical arrangement, mix, render, and archive environment. Use its Live API/LOM only through a constrained Bridge with capability discovery. Save a recovery copy before approved structural changes. Use Collect All and Save when preparing a portable project; Live normally keeps references to source files, so an uncollected Set can break when media moves.

## Hardware roles

- **APC64:** Live clips/scenes, performance, and mapped macros. Keep stable track labels and a clear scene/section map. The APC64's onboard sequencing is an idea source; verify its state and explicitly commit/export patterns into the Set.
- **Maschine MK3 / Maschine 3:** sampling, slicing, groove, patterns, performance FX, and resampling. Keep exported stems/samples and the editable source when practical.
- **Komplete Kontrol A49:** playable composition, browsing, and mapped instrument controls. Record instrument/preset identity and dependencies.

## Instruments and processing

- **Serum 2:** synth role, oscillator/mode choices, modulation intent, and render dependencies belong in sound-design notes. Do not assume generic parameter names match the current plugin build.
- **Waves / FabFilter / soothe3 / Analog Obsession:** products may be installed in different versions and formats. Use only devices discovered in the current Set. Prefer semantically named rack macros for repeatable control; require an explicit mapping table before direct parameter writes.
- **Live devices:** prefer them where they meet the brief and expose clear, stable parameters, while keeping the sound design and signal flow documented.

## Stable naming convention (suggestion)

Use role-bearing names and a stable ID when building a new template: `T01_KICK`, `T02_BASS`, `T03_DRUMS`, `T04_PERC`, `T05_MUSIC`, `T06_VOCAL`, `T07_FX`, `T08_TEXTURE`. Names are suggestions, not a reason to rename an existing project automatically. Proposed Rack macros: `TONE`, `PUNCH`, `BODY`, `DRIVE`, `MOVEMENT`, `SPACE`, `WIDTH`, `LEVEL`. Macro meaning must be documented per rack and range-limited; a shared label alone does not prove identical behavior.

