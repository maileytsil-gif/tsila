# End-to-end production lifecycle

## Goal
The success condition is not "good advice" or "a loud master". The success condition is a reproducible, technically checked, musically coherent track that can be delivered to a label, distributor, DJ, client or archive in the requested format.

## How this maps to the studio's method
The user's own eight-step method (`../../ableton-live-session/SKILL.md`: frame → instruments → central 8 bars → arrangement → mix → automation → vocals → export) runs inside these gates: G0–G1 = step 1 (Save As, tempo, key, locators, energy curve before any note), G2 = step 2, G1/G3 = steps 3–4, G5–G6 = steps 5–6, vocals = step 7, G7–G10 = step 8. One step per exchange; the project memory (`../../memoire-projet/SKILL.md`: REPRISE header, dated journal, snapshots) records every gate result, and `../../chef-de-projet/SKILL.md` tracks several tracks at once. For the house family (house, tech house, bass house, future house, future rave, big room) the French skill `../../house-future-rave-bass-house-production/SKILL.md` holds the verified numbers, recipes and two-master targets used at G3–G8.

## Lifecycle and gates
Do not skip a gate because the track already sounds exciting. Move forward only when the current gate is good enough for the genre/reference and intended destination.

### G0 — Brief / identity
Define: primary + secondary genre DNA, tempo/key if known, emotional intent, DJ/streaming/club destination, 2–4 reference tracks, expected duration/version(s), and any vocal/sample rights constraints.
Exit when: the track has a clear identity and comparison target.

### G1 — Core idea / hook
Create the minimum recognizable idea: groove, bass motif, chord/melody/vocal hook, or timbral signature.
Exit when: the idea remains identifiable at moderate/low playback level without master loudness.

### G2 — Palette / source design
Lock the main sonic roles: kick, sub/bass architecture, snare/clap, tops/percussion, main musical layer, vocal, FX/atmosphere. Decide which parts are synthesis vs samples vs resampling.
Exit when: no critical element is still a placeholder unless deliberately marked.

### G3 — Arrangement
Map intro, groove, bridge/pont, break, build, drop(s), transitions and outro using genre-specific section logic. Create intentional changes at appropriate 4/8/16/32-bar scales.
Exit when: the full track plays end-to-end without relying on later mixing to create interest.

### G4 — Spatial/spectral plan
Read `41-spatial-spectrum-stereo-engine.md`. Assign every important element a spectral role, horizontal position, depth, width/motion policy and mono policy. Identify collisions before adding processors.
Exit when: the mix has a deliberate center, deliberate side field, protected low end and a depth hierarchy.

### G5 — Mix prep / gain / routing
Clean edits, fades, phase issues, clip gain, routing, groups, returns, sidechains, reference track and monitoring level. Confirm sample-rate/project settings and latency-sensitive recording paths.
Exit when: static balance can be judged without corrective master processing.

### G6 — Mix
Work root-cause first: arrangement/source/timing/envelope -> balance -> low-end/phase -> masking -> dynamics -> space/stereo -> color. Level-match processing decisions.
Exit when: the track translates in mono, low volume, headphones and at least one small speaker; reference comparisons are section- and level-matched.

### G7 — Pre-master QC
Bypass master loudness and inspect mix integrity: headroom, accidental clipping, DC/clicks, tails, low-end stability, harshness, stereo/mono behavior, automation and section transitions.
Exit when: the mix does not depend on the limiter to hide balance or transient problems.

### G8 — Master
Use only needed stages. In this studio Waves L4 is the primary final limiter (validated by the user) and L2 the validated alternative (`01-studio-inventory.md`); Pro-L 2 is not owned. Keep a premaster file before any master processing. Choose loudness by equal-loudness comparison, not a fixed target.
Exit when: louder is not audibly worse, low-end punch survives, true-peak/export requirements are met on the exported file (`50-mastering-engine.md`, `65-label-ready-qc-export.md`), and the master translates. If reaching the target needs more than 4–5 dB of limiting, go back to the mix.

### G9 — Delivery QC
Read `65-label-ready-qc-export.md`. Render required versions; re-import and audition the actual files. Verify start/end, tails, fades, channel count, metadata/file naming, bit depth/sample rate, sample provenance and requested stems.
Exit when: every requested deliverable passes technical and audible checks.

### G10 — Reproducible archive
Collect the Ableton Set, critical samples, MIDI, presets/racks, source and printed/resampled versions, notes on non-default hardware/software dependencies, and sample/license provenance.
Exit when: the release can be reopened and meaningfully reconstructed later.

## Status language
Use: NOT_STARTED / IN_PROGRESS / BLOCKED / PASS_WITH_NOTES / PASS.
Never label a stage PASS when required evidence is missing; use BLOCKED or PASS_WITH_NOTES.

## A-to-Z default response
When asked to build or finish a track from scratch, return:
1. current gate,
2. next concrete actions,
3. exit criteria,
4. files/measurements needed,
5. next gate only after the current one is satisfied.
