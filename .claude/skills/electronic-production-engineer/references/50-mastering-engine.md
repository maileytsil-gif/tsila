# Electronic mastering engine

Tags: [DOC] document read in full; [DOC-2] secondary extract; [COMM] community convention, not a measurement; [HEUR] unsourced practice; [CALC] arithmetic; [TEST] to be measured. Sources (French): `../../house-future-rave-bass-house-production/references/mixage-mastering.md` §1 and §4; `../../mastering-outils/references/waves-mastering.md`.

## Goal
Produce translation, impact and controlled loudness; do not chase a genre LUFS number blindly. **Loudness is decided in the mix.** If the limiter needs more than 4–5 dB of gain reduction, go back to the mix [COMM].

## Pre-master gate
Do not master around unresolved kick/bass conflict, harsh resonances, channel clipping or unstable stereo low end; fix the mix first. Premaster: no final limiter, no normalisation, REF excluded; a peak near −6 dBFS is a convention, not a rule.

## Destination targets (starting points, not quality scores)
The research found no published measurements of commercial masters in these genres; measure 6–10 purchased reference WAVs [TEST].

| Destination | Normalises to | True peak [DOC-2] |
|---|---|---|
| Spotify, YouTube (turn-down only), Tidal, SoundCloud | −14 LUFS | −1 dBTP |
| Apple Music / Deezer | −16 / −15 LUFS | −1 dBTP |
| Amazon Music | −14 LUFS | −2 dBTP |
| Beatport, Bandcamp, club | none | — |

Make two masters from one premaster (repo decision):
- **Club**: −8 to −7 LUFS integrated (big room and future rave down to −6.5).
- **Streaming**: −10 to −11 LUFS, or more dynamic.
- Both at TP −1.0 dBTP (−2 for Amazon or lossy delivery on request). Sources span −6 LUFS short-term (EDMProd) to "never above −10 short-term" (Ian Shepherd) [DOC-2]; hence two masters.

## PLR, LRA, short-term
- **PLR** = true peak − integrated (Music Production Wiki's "crest factor"): 12–14 dB dynamic, < 6 dB brickwall [COMM]; −7 LUFS at −1 dBTP gives 6 dB [CALC]. `analyze_wav.py`'s crest (peak − unweighted RMS) is a different number.
- **LRA** (EBU Tech 3342): spread of short-term loudness; commercial music 4–9 LU, < 4 flat [COMM]. It does not certify punch.
- **Short-term** 3 s, **momentary** 400 ms [DOC]. Club master at −8: drop −7/−6 ST, breakdown −12/−14 ST [HEUR].

## Candidate chain (modular, not mandatory)
Order [DOC-2]: corrective EQ → glue → tonal EQ → stereo → saturation → clipper → true-peak limiter → metering only.
1. Pro-Q 4, F6 or REQ 6: very small tonal correction.
2. soothe3 or F6: only for remaining moving harshness; never stacked with multiband on the same problem.
3. Optional glue or colour: bx_glue 2:1 at 1–2 dB, J37, TG Mastering Chain. TG's "Limit" is not a brickwall.
4. Peak shaving: L4 Clip or a hot J37 input, 1–3 dB on the drop [HEUR]. Never clip the low end; RazorClip is [TEST].
5. Limiter: Waves L2 (validated; its −1.0 dBFS ceiling is sample-peak only) or L4 True Peak once probed. Aim for 2–4 dB of gain reduction on the drop [COMM].
6. Metering: Insight 2 at the end of Main, or WLM Plus as a meter only (Gain 0, no Trim, limiter off). PAZ is not a LUFS/TP meter.

The chain in place is in `../../ableton-live-session/references/mix-chain.md`. A strong mix may need only the limiter.

## Waves L4 role
Installed (V17), not probed in Live. Compare modes at equal loudness; the mode names this pack gave earlier are unverified. Gain Match disables Ceiling [DOC manual]: leave it and switch Delta off before export.

## Club vs streaming
- Club/DJ: protect kick/sub impact and mixability; crushed transients can sound smaller on a big system.
- Streaming: normalisation does not require −14 LUFS; louder masters are just turned down. Keep a TP margin against codec overs.

## QC on the exported file, not the meter
- Insight 2 or WLM Plus: integrated, short-term max/min, TP, LRA.
- `../../live-export-wav/scripts/analyze_wav.py`: sample peak, RMS, near-clip samples, clicks, duration, tail (no LUFS/TP).
- Off-Live, if installed: pyloudnorm gives I and LRA but no TP (`../../../../corpus/house-future-rave/pyloudnorm-readme.md`); `ffmpeg -nostats -i master.wav -filter_complex ebur128=peak=true -f null -` gives all (`../../../../corpus/house-future-rave/ffmpeg-filters-loudnorm-ebur128.md`).
- Also low end, mono, sections, fades, head/tail, format. Measurements support decisions; they do not replace listening. Full checklist: `65-label-ready-qc-export.md`.
