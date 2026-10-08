# v18 Integration Report

## What changed

The package now has a control plane rather than only a collection of specialist prompts. The Director routes by branch; structured contracts separate musical decisions from sound design and DAW execution; a compiler produces an AbletonClipPlan and a capability-gated BridgeActionBatch.

## Safety boundary

Compilation is **not** execution. Real Ableton changes remain `[TEST]` until the bridge discovers support, resolves current Live objects, snapshots state, executes a dry run, performs mutations, reads back, and cleans up.

## End-to-end tests

Three scenarios compile successfully and validate structurally: Afro House, Afro-Cuban-informed House, and Detroit Soulful Techno. MIDI exports parse successfully. This proves the contracts/compiler path, not artistic quality or Live API compatibility on the user's Mac.
