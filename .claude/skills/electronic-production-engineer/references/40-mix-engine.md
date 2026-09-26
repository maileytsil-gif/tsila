# Mix engine

Tags: see `50-mastering-engine.md`. Repo procedure (French): `../../mixage/SKILL.md`, `../../mixage/references/diagnostics.md` (symptom → measurement → remedy) and `../../mixage/references/outils.md` (tool per task).

## Mix sequence
1. static balance/gain staging,
2. kick/bass relationship (`30-low-end-engine.md`),
3. drum hierarchy and transients,
4. masking/tonal balance,
5. spatial/spectral plan and depth/sends,
6. stereo/mono stability,
7. buses/color,
8. automation,
9. reference comparison,
10. pre-master readiness.

Each processor must solve a named problem. Make one change at a time and compare at matched loudness.

## Gain staging and meters
Map the mix first with `lom.py state --json` and `../../mixage/scripts/mix_snapshot.py`. Balance on the densest section.

`lom.py meters` and `../../ableton-live-session/scripts/levels.sh` are **relative** only. On a track they read post-fader; on the master they read before its devices. They also miss peaks.

Take absolute peaks from the exported file (`../../live-export-wav/scripts/analyze_wav.py`). Pre-limiter peaks of about −6 to −4 dBFS are a repo convention, not a rule.

## EQ
- Stable problems get static EQ: REQ 6 first, since its parameters are exposed; Pro-Q 4 is window-only.
- Level-dependent problems get F6, Pro-Q 4 dynamic/spectral or TDR Nova.
- First places to look:
  - muddy: 200–400 Hz summed across tracks;
  - harsh: 3–8 kHz.
- High-pass values in `../../ableton-live-session/references/mix-chain.md` are validated on one project only.
- Avoid carving every track just to make analyser plots look separated.

## soothe3
Best for moving resonances, harshness and spectral sidechain, at the source or on a group bus. Use Delta listening to confirm it is not eating the sound's identity. Be especially conservative on the master. A validated gentle setting on a harmony bus: soft, depth 4, node at 357 Hz.

## Compression
- Choose by goal: level control, transient shape, groove/pumping, glue or colour.
- Probed and exposed: bx_glue (glue) and API-2500 (parallel, mix 30–60 %).
- Not yet probed: Pro-C 3, SSLComp, CLA and dbx (`01-studio-inventory.md`).
- Starting points [COMM]:
  - mix-bus glue: 2:1–3:1, attack 30–60 ms, 1–2 dB of gain reduction;
  - drum bus: 3–6 dB (`../../house-future-rave-bass-house-production/references/mixage-mastering.md` §4.2).
- Calibrate by comparing the bus active and bypassed on a drop loop. Aim for 1–2 dB on the body and keep the transients.
- If the compressor makes the kick smaller at equal loudness, question whether it belongs.

## Saturation / clipping
Saturation adds harmonics and colour; clipping limits peaks and may also colour. They are related but not interchangeable.

Use one colour stage per chain (J37, bx_glue XL). Roar and Saturator are native and excluded from mix chains by rule 6. RazorClip is undocumented, so treat it as [TEST]; the L4 Clip control or a hot J37 input are the alternatives.

Do not clip the low end. Re-check aliasing, harshness and transients afterwards.

## Stereo and spatial planning
Read `41-spatial-spectrum-stereo-engine.md` for element-by-element placement. Keep center authority. Distinguish panning from width, and depth from reverb amount. Spread supporting percussion, textures, reverbs and upper harmonics as appropriate.

Mid/Side is a diagnostic/processing domain, not a mandatory widening trick. The repo mix widens only above 120 Hz. After widening, verify correlation in SPAN; Imager does not measure it.

## Space
Use shared returns for coherent depth, with post-fader sends automated by section. High-pass the returns at 150–200 Hz and duck them under the dry signal [COMM]. Hybrid Reverb on a return is tolerated; Valhalla and H-Delay must be probed first.

## Reference and report
Route REF to Main outside the limiter, gain-matched within ±0.5 dB. Compare equal sections with Tonal Balance Control 3 or SPAN (4 s average).

Report every change as measured, listened (only if the user said so) or assumed (`../../ingenieur-mixage/SKILL.md`).
