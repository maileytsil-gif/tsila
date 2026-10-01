# Label-ready QC and export

Tags: see `50-mastering-engine.md`. Repo procedures (French):
- `../../live-export-wav/SKILL.md`: export dialog and file check.
- `../../live-mix-mastering/references/mastering-mesures.md`: dBFS vs dBTP vs LUFS vs LRA.
- `../../ingenieur-mixage/SKILL.md` §5: QC list.

## Meaning of label-ready
A quality-control target, not a promise of label acceptance. The track should have a deliberate identity, coherent arrangement, controlled low end/transients, reference-competitive translation and technically clean deliverables.

## Creative/arrangement gate
- Hook/identity is recognizable without relying on mastering loudness.
- Break/build/drop logic fits the genre DNA rather than a generic EDM template.
- Repetition contains intentional micro-variation where the genre needs it.
- No section exists only because a template says it should.

## Mix gate
- A spatial/spectral plan exists for all important elements: center anchors, left/right distribution, depth, width/motion and collision priorities.
- Kick/sub relationship survives mono and low-volume listening.
  - Kick/sub correlation in 30–120 Hz is ≥ 0, measured on separate exports with `../../kick-bass-equilibre/scripts/kick_bass_check.py`.
- No accidental clipping before intended clipping stages.
- Harshness, masking and excessive low-mid buildup are solved at source/group level when practical.
- Stereo width is deliberate; panning is not confused with widening; true sub is not widened by default.
- Important stereo sources are checked for correlation/mono translation, and low-frequency side energy is intentional.
- Reference comparisons are level-matched and section-matched: REF goes to Main outside the limiter, gain-matched within ±0.5 dB.

## Master/QC gate: measured on the exported file
A limiter ceiling or a Live meter is not a measurement. Every value is reported with its tool and the file measured.

| Check | Pass condition (starting point) | Tool |
|---|---|---|
| Integrated loudness | within the chosen destination range (`50-mastering-engine.md`); chosen by equal-loudness comparison | Insight 2 at the end of Main, WLM Plus as a meter only |
| True peak | ≤ −1.0 dBTP; ≤ −2 dBTP for Amazon [DOC-2] or lossy delivery [COMM] | same; L2's ceiling is sample-peak only |
| Limiter gain reduction, loudest section | ≤ 4–5 dB, otherwise back to the mix [COMM] | limiter display |
| PLR, LRA, short-term drop vs breakdown | recorded; LRA below 4 LU = flatness alert [COMM] | Insight 2; pyloudnorm or ffmpeg if installed |
| Sample peak and overs | no unintended overs. A count of samples ≥ −0.1 dBFS is not proof of clipping | `../../live-export-wav/scripts/analyze_wav.py` |
| Clicks, dropouts | every abrupt sample jump the script flags is located and inspected; DC and dropouts go to listening | same, plus user listening |
| Duration, head, tail | exact length; last 20 ms near silence; fades and reverb/delay tails intentional | `analyze_wav.py <file> <expected s> [name=start-end]` |
| Mono | the mono sum keeps kick, sub and hook | Utility mono (tolerated), SPAN correlation |
| Lossy copy, if requested | re-measured separately, because its peaks can differ | same meters |

- Check headphones, small speaker/phone and a bass-capable system where possible. These are listening checks; report them only if the user did them.
- Rendered automation mistakes are listening checks too.
- There are no published measurements of commercial masters in these genres to compare against. Measure purchased references with the same tools (`../../house-future-rave-bass-house-production/references/mixage-mastering.md` §1.4).

## Sample and rights hygiene
For commercial/label delivery, keep provenance for third-party samples, vocals and loops: source, license/pack, date/version if relevant, and transformation notes. "Royalty-free" is not the same as public domain; follow the source license. Do not treat this checklist as legal advice.

## Export hygiene
- Use the label/distributor's requested sample rate, bit depth and format when specified.
- Without a spec, use the repo default, a Live export:
  - Rendered Track Main, start 1.1.1, exact length (export loop ending on the last bar + 1);
  - Normalize Off, sample rate = project (44.1 kHz on the current project), PCM WAV 24-bit, MP3 off;
  - REF muted and the Set saved first;
  - wait until the file stops growing.
- Avoid unnecessary sample-rate conversion stages.
- Dither only when reducing word length, and only once at the final relevant conversion.
  - No dither at 24-bit.
  - TPDF once for a 16-bit final (L2 IDR, or export dither, never both).
- Keep an undithered high-resolution archive/pre-master when useful.
- Render a main master plus instrumental/clean/extended/stems only when the project or recipient needs them.
- Re-import the final render and verify start, end, peak behavior, channel count and audible integrity.

## Delivery package gate
- Before calling the project deliverable, confirm every requested file actually exists and has been re-imported and auditioned.
- Typical package candidates: main master, extended/DJ version, instrumental, clean edit, pre-master, stems, artwork/metadata sheet only when requested. Do not generate unnecessary versions.
- Name club and streaming masters distinctly, for example `Artist_Title_ClubMaster_128_Fm_Date` and `…_StreamMaster_…` (repo convention).
- Report each master with its file name, format, sample rate, bit depth, duration, integrated LUFS, true peak and LRA.
  - State the analyser and mark anything not measured.
  - Separate measured, listened (by whom) and assumed.
  - Never declare "ready to release" from a limiter ceiling alone.

## Archive
Keep the Ableton Set, used samples, critical presets/racks, source MIDI/audio and printed/resampled versions needed to reproduce the release. Include a short release note with tempo/key if measured/verified, master version/date, sample provenance status and known external dependencies.
