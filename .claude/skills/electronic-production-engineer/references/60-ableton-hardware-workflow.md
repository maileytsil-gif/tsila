# Ableton + hardware workflow

## Role separation
- **APC64**: Ableton structure/performance — clips, scenes, touch faders, device/macros, automation, step sequencing.
- **Maschine MK3 / Maschine 3**: drums, sampling, slicing, groove, pattern experimentation, euclidean/probability workflows.
- **Komplete Kontrol keyboard + plugin**: keyboard playing, NKS browsing/mapping, scales/chords/arps and instrument discovery. Model: **Komplete Kontrol A49**, confirmed by the user on 26 Sept 2026 ([native-instruments-control](../../native-instruments-control/SKILL.md) updated). Do not assume S-series features.
- **Ableton Live 12**: source of truth for arrangement, routing, automation, resampling and final mix.
- **AI control**: LOM Bridge (`lom.py`) for state, parameters, notes, loading and arrangement automation; Producer Pal (`ppal-*`) for MIDI, clips and native devices; screen control for menus, plug-in windows and NI software ([61](61-ableton-lom-bridge.md)).

## What the AI can actually reach in this setup
- **Maschine 3.6 and Komplete Kontrol 3.5: no API.** Screen control only, in the foreground (`request_full_control`), one screenshot after each gesture, nothing in the background; coordinates come from the current screenshot, never from memory. What cannot be reached is done by the user.
- In Live, the Maschine, Komplete Kontrol and Battery 4 plug-ins load with `lom.py load` (anti hot-swap); check what they expose with `lom.py params <deviceRef>` (one line = window only) [TEST: not probed yet].
- A software click is not a pad, encoder or key press, and no MIDI-output tool is known in this setup (use one only if it and its protocol are actually available). Guide the user through hardware gestures and never report a hardware test that was not observed.
- **APC64**: nothing in this repository has observed it (control-surface script, mappings, sequencer state) [TEST]. The LOM Bridge itself occupies a Live control-surface slot (Preferences › Link, Tempo & MIDI › Control Surface: `LOMBridge`, input/output None); check that the APC64 has its own slot [TEST]. No tool here reads the APC64's onboard sequencer: commit patterns to Live clips, then read them back with `lom.py notes get` or `ppal-read-clip`.
- The bridge cannot detect hardware movement ([63](63-write-safety-and-automation.md), Human takeover): ask before writing while the user performs.

## Eight performance tracks
Keep the first APC64 bank stable when possible (canonical names for new templates, [62](62-semantic-mapping-contract.md); existing Sets keep their `AUDIO - …` / `BUS - …` names):
1 `T01_KICK`
2 `T02_BASS`
3 `T03_DRUMS`
4 `T04_PERC`
5 `T05_MUSIC`
6 `T06_VOCAL`
7 `T07_FX`
8 `T08_LOOP`

Technical/utility tracks can live in the next bank: extra sub/synth/vocal FX, resample, Maschine, reference, sidechain trigger and print.

## Universal Rack macros 1-8
1 `M01_TONE`
2 `M02_PUNCH`
3 `M03_BODY`
4 `M04_DRIVE`
5 `M05_MOVEMENT`
6 `M06_SPACE`
7 `M07_WIDTH`
8 `M08_LEVEL`

Use macros 9-16 for technical controls (sub level, sidechain depth/release, soothe depth, mono frequency, trim, safety). The same semantic macro names let APC64 and the Bridge control the project without relying on fragile device indices. Adding a Rack is a device insertion: ask first ([62](62-semantic-mapping-contract.md)).

## Returns
Start simple: `A_ROOM`, `B_SPACE`, `C_DELAY`, `D_PARALLEL`. Add only when needed.

## APC64 workflow
Experiment in its step sequencer/probability system, then commit useful patterns to Ableton clips. Use native Ableton Control Surface mapping for core functions; reserve custom MIDI mappings for special Bridge commands. The LOM Bridge runs with MIDI input/output None and has no MIDI handler, so APC64 "Bridge commands" do not exist yet [TEST if built].

## Maschine workflow
Build grooves/samples/patterns, route/bounce into Ableton, then do detailed arrangement and mix in Live. Do not duplicate the same control responsibility on APC64 and MK3 unless performance needs it. As a plug-in, avoid double playback (Maschine's own sequencer plus notes in Live).

## Komplete Kontrol/NKS
Treat NKS as a semantic browsing/mapping layer, not the core automation API. For AI control prefer Ableton-exposed parameters / Live Object Model. NKS helps name and organize meaningful parameters. Read the page and parameter names actually shown before turning an encoder; an index alone does not identify a function.
