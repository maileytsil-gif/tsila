# Studio inventory and preferred tool roles

Source of truth for what the user owns, reconciled on 2026-09-26 with the repository's tool sheets (French) for the same studio. **Owned is not usable**: a tool counts as usable only once its installed version is confirmed and the current Set exposes it. Load it with the bridge's anti-hot-swap `lom.py load`, then read `len(d.parameters)` (1 = window-only control). Never infer parameters from a product name. Unknown plug-in: probe it with `../../vst-sound-design/scripts/probe_params.py` on an empty track, then add a row to FICHES.

## Status legend
- **P**: probed in Live 12.4.5 (VST3). Exposed parameters are known and a sheet exists.
- **S**: bundle found on disk (VST3 Info.plist and Waves V16/V17 folders, scan of 2026-09-14). Installed, but licence and loading are unproven. The scan was not exhaustive.
- **D**: declared only, in this pack or in a repository task table. Confirm before use.

## Sheet keys (paths relative to this file)
- FICHES: `../../effets-plugins/references/fiches.md` (per plug-in: exposed, window-only, how to verify).
- CHAIN: `../../ableton-live-session/references/mix-chain.md` (values validated on one project, "deep chill minimal house", Sept 2026).
- WIN: `../../ableton-live-session/references/plugins.md` (window techniques).
- TASKS: `../../mixage/references/outils.md` (tool per task).
- WAVESM: `../../mastering-outils/references/waves-mastering.md`. MTOOLS: `../../mastering-outils/references/outils-et-reglages.md`. INV: `../../mastering-outils/references/inventaire-local.md` (disk scan).
- SERUM: `../../vst-sound-design/references/serum2.md` and `../../sound-designer-serum/references/serum2-cartographie.md`. NI: `../../native-instruments-control/SKILL.md`.

## Core platform and control
- Ableton Live 12 Suite (sheets written against 12.4.5): DAW, arrangement, routing, automation, resampling, mix. Control paths are Producer Pal (MIDI, clips, native devices), LOM Bridge `lom.py` (typed and verified writes, `meters`, `snapshot`/`restore`) and screen control for plug-in windows (`../../ableton-live-session/SKILL.md`).
- Mac mini M4 and Focusrite Scarlett 8i8 Mk3 (D, not named in the repo sheets).
- SoundID Reference (D, TASKS): headphone and room correction, standalone on the system output, never in a Set or an export.

## Controllers (no API for NI products: foreground screen control only, NI)
- Akai APC64 (D): session and scene control, clips, step sequencing, touch faders, macros, performance.
- Native Instruments Maschine MK3 hardware (D) and Maschine 3 software (3.6.0, S): drums, groove, sampling, slicing, patterns.
- Komplete Kontrol keyboard: **Komplete Kontrol A49**, confirmed by the user on 26 Sept 2026 (the earlier "S48/S49" note in the NI skill was wrong). A-series: do not assume S-series features (displays, light guide). Komplete Kontrol plug-in 3.5.4 (S).

## Instruments
- Xfer Serum 2 (VST3 2.1.5, P): primary deep synth (Sample, Granular, Spectral, wavetable resampling). Window control only, apart from parameters the user maps; knob drags and typed values fail in the background (SERUM).
- NI Battery 4 (VST3, S; NI). Ableton instruments (Simpler, Sampler, Wavetable, Operator, Drift, Analog) are allowed: rule 6 below covers effects in mix chains.

## Ableton native effects: user rule 6 overrides this pack's earlier preference
No new native effects in mix or master chains (`../../ableton-live-session/SKILL.md`, rule 6). Tolerated natives are Utility (mono, trim, phase), Auto Filter already on MIDI tracks, a sidechain Compressor already in place and Hybrid Reverb on a return. EQ Eight, Glue Compressor, Saturator, Multiband Dynamics, Limiter, Roar and Drum Buss are therefore out of mix chains. The rule does not say whether they are allowed in sound-design or resampling chains, so ask.

## Third-party tools
| Tool (version) | St. | Live control | Role here | Sheet |
|---|---|---|---|---|
| Waves REQ 6 Stereo (17.1) | P | exposed (freq in integer Hz) | first-choice corrective EQ on tracks (HPF plus one declutter bell) | FICHES, CHAIN |
| FabFilter Pro-Q 4 (4.10) | P | window only; typed entry fails; read values by hover | surgical/dynamic/spectral EQ, M/S; master bus 1 | FICHES, WIN, MTOOLS |
| oeksound soothe3 (1.0.5) | P | window only; double-click, type, Enter works | moving resonances, spectral sidechain; never default-on | FICHES, WIN |
| Waves F6 | P | window only | dynamic EQ, M/S, external sidechain | FICHES, WAVESM |
| TDR Nova (2.2.2) | S | window only | dynamic EQ alternative | MTOOLS |
| Waves Q10, SSLEQ / LinEQ, PuigTec, Curves AQ, Equator, Resolve / API-550, 560 | P / S / D | Q10 and SSLEQ exposed; Curves AQ window only | alternative EQs; do not stack Curves with soothe3 | FICHES, WAVESM, TASKS |
| Plugin Alliance bx_glue (1.1.0) | P | exposed | bus glue; Mono Maker on the bass bus | FICHES, CHAIN |
| Waves API-2500 Stereo | P | exposed | parallel density (mix 30–60 %), sidechain | FICHES, CHAIN |
| FabFilter Pro-C 3 (3.00) | S, owned (confirmed by the user, 26 Sept 2026) | parameter exposure not probed ("to probe", TASKS) | track compression, sidechain | MTOOLS |
| Waves SSLComp (SSL G-Master Buss), PuigChild, VComp, LinMB, C4, C6 | S | not probed | character or multiband dynamics | WAVESM |
| Waves CLA-2A/3A/76, dbx-160, H-Comp, C1 comp-sc, Renaissance Compressor, Smack Attack, Trans-X | D | unknown | compression and transient colour | TASKS |
| Waves J37 Tape | P | exposed | one colour stage per chain (master bus 1: 888, sat 2, 15 ips) | FICHES, CHAIN |
| Waves Abbey Road Saturator, KramerTape, Abbey Road TG Mastering Chain | S | not probed | colour; TG "Limit" is not a brickwall | WAVESM |
| RazorClip (1.0.0) | S | unknown | this pack files it under Analog Obsession; the repo documents neither vendor nor controls; read its editor and manual first | INV |
| Analog Obsession TheBus, BUSTERse, FET-style, KONSOL, PREDD, Rare | D | unknown | analog colour, bus dynamics | none |
| Waves NLS, Magma-series; bx_enhancer, Trash | D | unknown | colour | TASKS |
| iZotope Ozone Imager 2 (2.3.0) | P | Width and Stereoize exposed; bands window-only | global width (+8 % on master bus 2) | FICHES, CHAIN |
| Waves S1, Center / MaxxBass / R-Bass, InPhase, Brauer Motion, Doubler | S / S / D | not probed | stereo rotation and M/S; psychoacoustic bass; phase | WAVESM, TASKS |
| Waves MetaFlanger, Reel ADT | P | exposed | automated flanger mix on harmony and string buses | FICHES, CHAIN |
| Hybrid Reverb (native, tolerated on a return; "Dark Hall" on return C) / Valhalla ("to probe"), Abbey Road Plates/Chambers, H-Delay, H-Reverb, CLA EchoSphere, iZotope Aurora | native / D | native exposed / unknown | depth by sends | TASKS |
| Waves L2 Stereo | P | exposed | validated export limiter, end of BUS MASTER 3; ceiling −1.0 dBFS is sample-peak only | FICHES, CHAIN |
| Waves L4 Ultramaximizer (V17) | validated by the user (26 Sept 2026) | parameter exposure and mode names in Live to read once (`[TEST]`) before any bridge write | **primary final limiter** (true peak); L2 stays the validated alternative; Gain Match disables Ceiling, so leave it before export | WAVESM |
| Waves L1, L3 Multi/Ultra/16/LL | S | not probed | alternatives; never stack limiters by default | WAVESM |
| iZotope Ozone 12 Elements (12.1.0); Ozone 11 Elements and EQ | S | not probed | assisted mastering; do not assume Standard/Advanced modules | MTOOLS |
| iZotope Insight 2 (2.6.0) | P | window only | I/S/M/LRA/TP at the end of Main | MTOOLS |
| Waves WLM Plus, WLM, PAZ | S | not probed | WLM Plus as meter only (Gain 0, no Trim, TP limiter off); PAZ is not a LUFS/TP meter | WAVESM |
| Voxengo SPAN (3.23) | P | window only | spectrum and correlation (Avg 4000 ms, block 8192) | WIN |
| iZotope Tonal Balance Control 3 (3.1.1), Audiolens | P / D | window only; replace the instance to reset | tonal comparison against a target | WIN |
| Waves OVox, Vocal Bender, Waves Tune / Tune Real-Time, Harmony | D | unknown | vocoder, formant and pitch design, harmonies | none |

## Waves collection
The user owns the **complete Waves premium collection** (confirmed 26 Sept 2026): any Waves plug-in may be proposed, but check the installed version and whether it loads in the current Set before parameter-level guidance; rows above give the ones already probed or found on disk.

## Explicit exclusions and absences
- FabFilter Pro-L 2: not owned (INV: Pro-L and Pro-MB not found in the standard folders). Use L4 (primary, validated by the user) or L2 (validated alternative). Ableton Limiter is excluded from mix and master chains by rule 6.
- Not on this Mac: LFO Tool, Kickstart, ShaperBox. For their jobs, use sidechain compressors or Utility gain automation (`../../house-future-rave-bass-house-production/recipes/sidechain-et-pump.md`).
- ffmpeg, sox and pyloudnorm were absent at the last check (`../../mastering-outils/references/notes-locales.md`). Read LUFS and TP in Insight 2 or WLM Plus, or install a CLI tool only with the user's consent.

## Conflicts to resolve with the user, not by guessing
1. ~~Keyboard~~ — resolved 26 Sept 2026: Komplete Kontrol A49.
2. `../SKILL.md` (User studio assumptions) says to prefer Live-native devices when a third-party mapping is absent; rule 6 limits mix and master chains to the tolerated natives.
3. ~~Primary limiter~~ — resolved 26 Sept 2026: L4 validated by the user as primary; L2 the alternative. Read L4's exposed parameters once before bridge writes.
4. L2 ceiling: −1.0 dBFS in CHAIN and the notes vs −0.4 in the stale copy `../../effets-plugins/references/chaine-actuelle.md`. Use −1.0, because −0.4 let true peaks above −1 dBTP through.
5. RazorClip vendor and functions (still open). Pro-C 3: owned (confirmed 26 Sept 2026); its parameter exposure in Live is still to probe.
