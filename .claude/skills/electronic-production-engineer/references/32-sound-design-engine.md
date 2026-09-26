# Sound-design engine (Serum 2 reference)

Decision layer for synthesis, resampling and Serum 2. Exact labels, ranges and pages live in the verified map `../../sound-designer-serum/references/serum2-cartographie.md` (checked against the Serum 2 User Guide 1.0.3 / Serum 2.0.18; "§" refers to it). Evidence tags in files 32–39: `[DOC]` manual or repo file citing one · `[DOC-2]` secondary compilation · `[HEUR]` starting point · `[CALC]` arithmetic · `[TEST]` check in the Set · **MUET** no source states it.

## Choose synthesis vs sample/resample
Use synthesis when parameter-level control is the musical advantage (tuning, envelope length against tempo, recall). Use sampling/resampling when texture, speed or transformation is the advantage.

## Serum 2 bass architecture
For heavy bass design think in layers/functions:
- SUB: clean, stable fundamental.
- MID BASS: identity and movement.
- UPPER HARMONICS: audibility/aggression.
- ATTACK/NOISE: transient articulation if needed.
Do not force one patch to solve every role.

## Signal flow (§ 1, § 5)
- Five sources per voice: SUB, OSC A–C, NOISE. Each goes to **Filter** (FILTER 1, 2 or a blend), **Main** (through the MAIN FX rack), **Direct** (bypasses filters *and* FX) or **None** (modulator only) `[DOC p. 31]`.
- Default: OSC A → FILTER 1, but FILTER 1 is off in a new preset; other sources → Main `[DOC p. 31, 145]`.
- FILTER 1 and 2 in series (one output set to the other filter) or parallel; the S · A · B · C · N switches pick each filter's inputs `[DOC p. 134, 149]`.
- BUS 1 / BUS 2: per-source and per-filter sends to two more racks, returning to Main, Direct or the other bus `[DOC p. 146–150]`.
- FX process the **sum of voices**; an envelope on an FX parameter retriggers on every note `[DOC p. 159]`. Per-voice movement belongs in oscillators and filters.

## Oscillator engines (OSC A–C, § 3)
| Engine | Use | Key facts |
|---|---|---|
| Wavetable | basses, leads | ≤ 256 frames × 2048 samples; WT POS; WARP 1 + 2 `[DOC p. 38, 49]` |
| Sample | one-shots, loops, slices, tape-stop | Slice Auto/Manual; loop modes incl. Rev Loop; SCAN with Reverse `[DOC p. 71–80]` |
| Multisample | realistic instruments | SFZ, not SF2 `[DOC p. 58–59]` |
| Granular | textures, freezes | ≤ 256 grains; SCAN 0 = frozen, negative = reversed; DENS, LENGTH, 10 windows; CPU-heavy `[DOC p. 85–103]` |
| Spectral | resynthesis, time/pitch decoupling | Phase Lock, Transients, drawable spectral filter; CPU-heavy `[DOC p. 104–121]` |

Sample, Granular and Spectral share one sample `[DOC p. 69]`. Pitch tracking off (right-click the oscillator label): Sample-type engines play C3 (MIDI 60), Wavetable plays C-2 (MIDI 0, ≈ 8.2 Hz), so retune with OCT/SEM `[DOC p. 35]` `[CALC]`. SUB has six simple shapes (Sine first); NOISE is a sample player with colour noises `[DOC p. 125–132]`.

## Warps (§ 4)
Two slots per oscillator: Sync (WARP Var hard → soft), Alt Warp (Bend +/−, PWM, Asym, Flip, Mirror, Remap 1–4, Quantize, Odd/Even), Filter, Distortion (Tube, Diode 1/2, Linear Fold, Sine Fold…), FM, PD, AM, RM `[DOC p. 50–56]`. Bend +/− and Odd/Even are neutral at 50 %. Labels name the source: on OSC A `FM (B)`, `FM (Sub)`, `FM (Filter 1)`, and `PD (Self)`; the source must be on but may sit at level 0 `[DOC p. 54–56]`. For FM, set the modulator's tuning mode to **Ratio** (right-click OCT or SEM) `[DOC p. 30]`. FM depth scaling is **MUET**; repo starting points: 15–25 % growl, > 40 % screaming `[DOC-2]`.

## Filters for bass and lead (§ 6)
- MG Low 6/12/18/24 (ladder, dB/oct; VAR = FAT tames resonance); MG Low 6 is the Init type `[DOC p. 135, 142]`.
- MG Ladder, EMS Ladder (clean), Acid Ladder (diode), MG Dirty (VAR = PAIN) `[DOC p. 139]`.
- Formant-I/II/III: CUTOFF morphs vowels, VAR = FORMNT `[DOC p. 138]`.
- Scream LP/BP (DRIVE above 50 %), French LP, Dist.Comb, comb/flange types (MIX 50 %), Ring Mod, PZ SVF (drawable) `[DOC p. 136–139]`.
- DRIVE › Clean Mode = −24 dB in, +24 dB out `[DOC p. 142]`. A resonant filter on a sub must key-track `[DOC-2]`.

## Modulation (§ 7)
- **4 ENV**: ATK, HOLD, DEC, SUS, REL; MS/BPM; right-click › Legato Inverted; ENV 1 drives amplitude `[DOC p. 184–187]`.
- **10 LFO** (7–10 appear once LFO 6 is used): TYPE Normal, Path (Y output), `Chaos: Lorenz`, `Chaos: Rossler`, S&H; MODE FREE / RETRIG / ENVELOPE; BPM or HZ (to 1000 Hz with 10x); RISE, DELAY, SMOOTH, MONO; HOST acts even with BPM off `[DOC p. 188–193]`. Growls and wobbles need RETRIG `[DOC-2]`.
- **8 macros**, also destinations and aux sources; Apply and Delete Macros bakes them in `[DOC p. 206–214]`.
- **MATRIX, 64 slots**: SOURCE, CRV, AMOUNT ±100, POL, DESTINATION, AUX SOURCE (scales the source), INV, OUTPUT, bypass `[DOC p. 209–212]`; VELO and NOTE take drawn curves `[DOC p. 201–205]`.

## FX racks (§ 8)
MAIN, BUS 1, BUS 2; 13 modules (Bode, Chorus, Compressor, Convolve, Delay, Distortion, Equalizer, Filter, Flanger, Hyper/Dimension, Phaser, Reverb, Utility) plus Splitter L/H, L/M/H and M/S, any order and count `[DOC p. 152–182]`. Compressor MULTIBAND is Serum's "OTT"; RATIO at maximum = Limit (true-peak) `[DOC p. 162–164]`. Utility MONO BASS sums below FREQ `[DOC p. 182]`.

## Quality and reproducibility (§ 9, § 12)
GLOBAL › QUALITY: Draft 1×, High 2×, Ultra 4× oversampling, lockable; "Use Ultra quality when rendering"; S1 Compatibility Mode; Disable Smoothing `[DOC p. 315, 319–320]`. FM/AM/PD/RM warps changed with Quality before 2.0.21; 2.0.23 removed a 1.37 dB FX master boost `[DOC changelog]`: record the version, compare at matched loudness. Unison: 7 voices is the manual's "magic number"; Hyper/Dimension costs less CPU `[DOC p. 45, 174]`.

## Stable sub, modulated mid/high, one instance
1. SUB Sine (or OSC A sine), UNISON 1, PAN 0 → **Direct**, envelope button on so ENV 1 still shapes it `[DOC p. 31, 146]`.
2. Mid/high → FILTER 1/2 → Main; high-pass the mid *below* the played note (78–79 Hz for F2), low-pass the sub near 90–100 Hz `[DOC-2]`.
3. Drive inside Splitter L/M/H (e.g. 120 Hz / 2 kHz): LOWS clean `[DOC-2]`.
4. Utility MONO BASS ≈ 100–150 Hz at the end of MAIN `[DOC-2]`. The sub is never widened, chorused, granular or LFO-modulated.
5. OSC Mapping › FOLD keeps an oscillator in its note range whatever octave is played `[DOC p. 270–273]`.
Separate tracks meter and sidechain more easily; one instance recalls more easily `[HEUR]`.

## Macro conventions
Map MACRO 1–8 to `62-semantic-mapping-contract.md` (M01_TONE … M08_LEVEL); technical controls (M09_SUB_LEVEL, M14_MONO_FREQ…) go on an Ableton Rack around Serum `[HEUR]`. One intent per macro, level compensated, staggered ranges, tested at 0/50/100 % in the densest section `[HEUR]`; M07_WIDTH never reaches the sub. Scripts must not find macros by name: Live could show wrong names after loading a Set (2.0.21 workaround) `[DOC changelog]`.

## Movement
Map movement to few macros (filter, WT POS, FM/PD amount, drive, LFO rate/depth, formant, FX mix). Time scales: grain 5–20 Hz, breath 0.1–1 Hz, arrangement 8–20 s `[HEUR]`. Movement should support phrase rhythm.

## Distortion chain
Create harmonics first (warp Distortion, Distortion module, Roar, Waves, Analog Obsession), then treat a named harsh resonance only (soothe3/dynamic EQ). The same drive before or after the filter gives two sounds `[HEUR]`; compare at matched loudness.

## Resampling
Design → automate → render → chop/reverse/pitch/stretch → reprocess, two or three passes `[DOC-2]`. In Serum: main menu › Rendering › **Resample to** (one bar of a note, imported as a wavetable) and **Render OSC Warp** (256 frames across 0–100 % WARP) `[DOC p. 324]`; drag the wave icon to a Live audio track for a WAV of the last note `[DOC p. 22–23]`; for audio → wavetable try "Constant framesize (PITCH AVERAGE)" first `[DOC p. 294]`. Capture in Live: `../../resampling/SKILL.md`.

## Komplete Kontrol/NKS
Use for fast sound discovery and stable macro semantics; use the plugin directly when deep parameter access matters more.

## MUET after the manual (§ 15)
Pre/post-fader bus sends; exact filter-type count; FM types Thru-Zero/Exp/Linear versus preset internals; spectral warp labels; Distortion module type names; ENV DELAY (binary only); DETUNE × RANGE curve.

## Repo resources
- `../../sound-designer-serum/references/serum2-cartographie.md`; same folder: `serum2-fx-clip-arp.md`, `serum2-automation-et-migration.md` (automating Serum from Live), `basses.md`, `modulation-effets.md`, `fiches-pratiques.md`.
- Manual text: `../../../../corpus/constructeur/xferrecords-com-manual-serum-2-docs-NN-*.md` (`<!-- page N -->` markers).
- Genre recipes: `../../house-future-rave-bass-house-production/references/sound-design-genres.md`.
