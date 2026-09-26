# Project performance, latency, freeze and resample policy

## Goal
Keep sound design reversible while preventing CPU/latency problems from corrupting performance, recording or final renders. Capture procedure (French): `../../resampling/SKILL.md`.

## Three states
1. **Design state**: editable synth/sample chain, modulation visible, high-quality modes only where needed.
2. **Print state**: resample/freeze complex or unstable chains once the musical decision is approved; keep the source disabled/archived rather than deleting it.
3. **Delivery state**: deterministic playback with no unnecessary live randomization unless intentionally printed.

## Latency policy
- During live playing/recording, avoid high-latency oversampling/lookahead chains on monitored paths when they harm feel.
- During offline render, enable higher-quality/oversampling modes only after checking that they do not change tone/transients unexpectedly.
- Re-check sidechain timing after adding/removing high-latency processors.
- Do not compensate an assumed latency: measure it (best-offset line of `../../kick-bass-equilibre/scripts/kick_bass_check.py`, or print vs source transients).

## Resampling policy
Resample when it creates a new creative object, reduces CPU, locks a fragile/random process, or simplifies arrangement. Preserve the pre-resample source for important sounds.

Capture points: **Pre FX** (before devices; useless for a MIDI instrument), **Post FX**, **Post Mixer**, or **Resampling** (the Main output: check REF, returns and master devices first).

Record into a new named track (`RESAMPLE - source - take 01`), monitoring Off, sends at zero. Do not solo blindly, since sidechains and returns may depend on other tracks. Capture tails beyond the musical range, and never normalise a print.

Once a part is printed with its sidechain (the repo's `AUDIO - X` tracks):
- do not stack a second sidechain; re-bounce from the `.als` backup or fix downstream;
- key such an audio track from Pre FX.

Verify each print with `../../live-export-wav/scripts/analyze_wav.py` (peak, RMS, clipping, tail) and `../../synthese-reference/scripts/analyze_synth.py` (pitch). Freeze, Flatten and bounce commands vary across Live 12 versions: check the installed version rather than assuming one exists.

## Random/probability systems
For Maschine/APC probability, granular randomization or generative modulation: if repeatability matters for release, print/commit the chosen pass or record the controlling automation/seed where available.
- Maschine and Komplete Kontrol have no API (screen control only, `../../native-instruments-control/SKILL.md`). The user or screen control must export their audio or MIDI into the Set.
- Serum oscillators with free-running phase change the kick/sub correlation from note to note. Set retrig or fixed phase before printing the low end.

## Bridge implication
The bridge should not freeze, flatten, consolidate or overwrite source material as a hidden optimization. Treat these as destructive/commit actions and require an explicit plan plus rollback/archive path. In practice: save under a new name, `lom.py snapshot` first (`restore` if rejected), and log the step in the project memory (`../../memoire-projet/SKILL.md`).
