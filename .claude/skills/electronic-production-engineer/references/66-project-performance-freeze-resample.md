# Project performance, latency, freeze and resample policy

## Goal
Keep sound design reversible while preventing CPU/latency problems from corrupting performance, recording or final renders.

## Three states
1. **Design state**: editable synth/sample chain, modulation visible, high-quality modes only where needed.
2. **Print state**: resample/freeze complex or unstable chains once the musical decision is approved; keep the source disabled/archived rather than deleting it.
3. **Delivery state**: deterministic playback with no unnecessary live randomization unless intentionally printed.

## Latency policy
- During live playing/recording, avoid high-latency oversampling/lookahead chains on monitored paths when they harm feel.
- During offline render, enable higher-quality/oversampling modes only after checking that they do not materially change tone/transients unexpectedly.
- Re-check sidechain timing after adding/removing high-latency processors.

## Resampling policy
Resample when it creates a new creative object, reduces CPU, locks a fragile/random process, or simplifies arrangement. Preserve the pre-resample source for important sounds.

## Random/probability systems
For Maschine/APC probability, granular randomization or generative modulation: if repeatability matters for release, print/commit the chosen pass or record the controlling automation/seed where available.

## Bridge implication
The bridge should not freeze, flatten, consolidate or overwrite source material as a hidden optimization. Treat these as destructive/commit actions and require an explicit plan plus rollback/archive path.
