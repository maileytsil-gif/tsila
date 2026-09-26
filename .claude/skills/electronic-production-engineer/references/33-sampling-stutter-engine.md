# Sampling, resampling and stutter engine

Evidence tags as defined in `32-sound-design-engine.md`.

## Goal
Treat samples as raw synthesis material, not fixed loops. Choose the least-destructive path first, then resample when committing creates a useful new source.

## Source audit
Before processing, identify:
- role: drum, vocal, bass, tonal phrase, texture, field recording, FX;
- transient density and tail length;
- key/root if tonal (measure it, e.g. `../../synthese-reference/scripts/analyze_synth.py`, rather than trusting a file name);
- tempo and warp requirement;
- whether timing or timbre is the main target;
- whether the sample must remain editable or can be committed by resampling.

## Ableton roles
### Simpler
Use for fast one-shot playback, slicing and rhythmic reconstruction. Slicing mode, **Slice By** `[DOC Live 12 manual 30.11.1.3]`:
- **Transient** for organic chops (Sensitivity; up to 64 slices).
- **Beat** (Division) for predictable retrigger patterns; **Region** for N equal slices.
- **Manual** (double-click the waveform) for intentional vocal/percussion phrasing.
- Playback Mono / Poly / Thru decides whether slices cut each other or run on.
- Warp when pitch must change without destroying timing, then compare against unwarped pitch-shift for character.
- **Slice to Drum Rack** (or Slice to New MIDI Track) when pad-style performance is preferable. Crop and Reverse work on a copy of the sample `[DOC]`.

### Sampler
Use when the source should become a deeper playable instrument: zones, key/velocity mapping, looping, modulation, filters and layered multisample behavior.

### Arrangement micro-editing
Use direct audio edits when the result must be exact and section-specific: 1/8 → 1/16 → 1/32 retriggers, reverses, gaps, slip edits, fades and pre-drop cuts. Retrigger lengths, ms = 60000 / BPM × beats (quarter note = 1 beat) `[CALC]`:

| BPM | 1/8 | 1/16 | 1/16 T | 1/32 |
|---|---|---|---|---|
| 124 | 242 | 121 | 81 | 60 |
| 128 | 234 | 117 | 78 | 59 |
| 140 | 214 | 107 | 71 | 54 |
| 174 | 172 | 86 | 57 | 43 |

Clip Fade (Session clips) applies 0–4 ms edge fades; in Arrangement, fades are drawn per clip `[DOC Live 8.4.4]`. Reverse an Arrangement selection with Reverse Clip(s) (R) `[DOC Live 8.4.2]`.

### Beat Repeat
Use for controlled or probabilistic repeats `[DOC Live 28.5]`: Interval (1/32 to 4 bars) and Offset set when material is captured, Grid sets slice size, Gate sets total repeat length in sixteenths, Pitch and Pitch Decay drop each repeat, Mix / Insert / Gate modes (Gate suits a return track). For a guaranteed transition keep Chance at 100 % or automate the Repeat button; use Chance below 100 % only when variation is wanted. Repo example: Interval 1 bar, Gate 7/16, Grid 1/16 on vocal chops `[DOC-2]`.

## Maschine 3 + MK3 roles
Use Maschine when tactile capture and variation are the priority `[DOC Maschine manual ch. 15, ch. 13]`.
- Record or import source → Slicer MODE **Detect** (transients, Sensitivity), **Split** (4, 8, 16 or 32 equal slices), **Grid** (4th to 32nd notes) or **Manual** → map to pads → perform a new phrase.
- To cut by ear while the material plays, use **Manual** mode and tap slice points on the pads; Auto-Snap moves them to the nearest transient (turn it off for exact taps).
- **Stutter** Perform FX: Gate (100 % = no gating), Pitch, Direction Forward / Reverse / Both, Quantize (keeps reverse loops on time).
- Resample the performed result so the gesture becomes editable audio rather than an unrepeatable live move.

## Serum 2 roles
Labels and pages: `../../sound-designer-serum/references/serum2-cartographie.md` § 3.3–3.6.

### Sample oscillator
Tuned one-shots, loops and slices. Slice Auto (yellow threshold line) or Slice Manual; **Send to Selected Clip** / **Auto-Sync to Clip** write one note per slice into Serum's CLIP module; Play Single Slice. **SCAN** (formerly Rate) sets speed and direction for tape-stop motion: Range ±200/400/800 %, Reverse, Lock Scan Rate (to Tempo), Sample Length to BPM `[DOC p. 74–80]`. Warps (FM, PD, Distortion) also apply to samples.

### Granular oscillator
Use when micro-time is the target: SCAN 0 = frozen, negative = reversed; DENS in Free, BPM Sync or Grains; LENGTH in Free, BPM Sync or Percent; windows such as ExpDec (percussive) or Exp Dec Rev (swell); DIR › Reverse Grains; Jump Start off for a softer attack; Max Grains caps CPU `[DOC p. 89–103]`. Grains shorter than about 50 ms start to produce their own pitch `[HEUR]`. Rhythmic starting point: LENGTH 1/32, DENS 1/16 (BPM Sync), SCAN ±150 % `[HEUR]`.

### Spectral oscillator
Use for frequency-domain resynthesis rather than playback: **Phase Lock** for tonal sources, **Transients** for drums; Sample Length to BPM keeps a drum loop on the host tempo while the keyboard transposes it `[DOC p. 116–117]`. CPU-heavy.

### Wavetable resampling
Render a complex gesture and re-import it as wavetable or sample material when the movement itself is the desired oscillator shape: main menu › Rendering › **Resample to**, or drag audio onto the wave display ("Constant framesize (PITCH AVERAGE)" first; "Switch OSC type" keeps it as Sample/Granular/Spectral) `[DOC p. 292–294, 324]`.

## Stutter families
1. **Rhythmic retrigger**: fixed 1/8, 1/16, 1/32 or triplet repeats (table above).
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
Source → slice → perform/resequence → resample → clean/warp → process → resample → load into Serum Sample/Granular/Spectral → render new one-shot/loop → arrange.

Each pass: keep the original disabled, name the bounce with its step (`pad_v2_reverb+bitcrush`), and gain-match before judging `[DOC-2]`. Stop iterating when a pass no longer adds a clearly useful identity.

## Repo resources
- Capture procedure: `../../resampling/SKILL.md`; slicing/granular background: `../../sound-designer-serum/references/moteurs-synthese.md` § 4, `modulation-effets.md` § B6.
- Local manuals: `../../../../corpus/constructeur/live12-manuel-30-live-instrument-reference.md` (Simpler), `live12-manuel-28-live-audio-effect-reference.md` (Beat Repeat), `live12-manuel-08-clip-view.md` (reverse, fades), `native-instruments-com-fileadmin-ni-media-downloads-manuals-maschine-maschine-3-software-m-17-15-sampling-and-sample-mapping.md` and `native-instruments-com-fileadmin-ni-media-downloads-manuals-maschine-maschine-3-software-m-15-13-effect-reference.md` (Maschine), `xferrecords-com-manual-serum-2-docs-06-using-sample-instruments.md`, `xferrecords-com-manual-serum-2-docs-07-using-granular-synthesis.md`, `xferrecords-com-manual-serum-2-docs-08-using-spectral-synthesis.md` (Serum 2), all in that folder.
