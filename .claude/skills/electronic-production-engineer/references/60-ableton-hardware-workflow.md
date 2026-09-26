# Ableton + hardware workflow

## Role separation
- **APC64**: Ableton structure/performance — clips, scenes, touch faders, device/macros, automation, step sequencing.
- **Maschine MK3 / Maschine 3**: drums, sampling, slicing, groove, pattern experimentation, euclidean/probability workflows.
- **Komplete Kontrol A49 + plugin**: keyboard playing, NKS browsing/mapping, scales/chords/arps and instrument discovery.
- **Ableton Live 12**: source of truth for arrangement, routing, automation, resampling and final mix.
- **AI/LOM Bridge**: semantic control, analysis and automation; GUI control is fallback, not first choice.

## Eight performance tracks
Keep the first APC64 bank stable when possible:
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

Use macros 9-16 for technical controls (sub level, sidechain depth/release, soothe depth, mono frequency, trim, safety). The same semantic macro names let APC64 and the Bridge control the project without relying on fragile device indices.

## Returns
Start simple: `A_ROOM`, `B_SPACE`, `C_DELAY`, `D_PARALLEL`. Add only when needed.

## APC64 workflow
Experiment in its step sequencer/probability system, then commit useful patterns to Ableton clips. Use native Ableton Control Surface mapping for core functions; reserve custom MIDI mappings for special Bridge commands.

## Maschine workflow
Build grooves/samples/patterns, route/bounce into Ableton, then do detailed arrangement and mix in Live. Do not duplicate the same control responsibility on APC64 and MK3 unless performance needs it.

## Komplete Kontrol/NKS
Treat NKS as a semantic browsing/mapping layer, not the core automation API. For AI control prefer Ableton-exposed parameters / Live Object Model. NKS helps name and organize meaningful parameters.
