# Ableton Bridge: semantic plans and safe execution

## Intent vocabulary

Translate requests into a musical intent object before mapping them to Live. Core concepts include `role` (kick, sub, mid-bass, snare, hat, percussion, lead, chord, vocal, FX), `goal` (more/less punch, darker/brighter, narrower/wider, nearer/farther, denser/sparser), `scope` (frequency range, section, time range, stereo component), `amount` (user-provided or explicitly proposed), and `constraints` (preserve mono sub, keep vocal intelligible, don't alter master).

Keep a distinction between:

1. **Observation:** facts read from the current Set, including confidence and timestamp.
2. **Musical intent:** what the user wants to hear/change.
3. **Implementation proposal:** a mapped target and operation, or `needs_mapping`.
4. **Execution:** only exact approved operations.
5. **Verification:** fresh observations compared with expected postconditions.

## Resolve and plan

- Match by stable track/rack/macro labels first; include object IDs as ephemeral evidence, never as the only identity.
- Require exactly one target. Ambiguous aliases, duplicated track names, stale IDs, hidden routing, unavailable devices, or unknown parameter units stop execution.
- Plan the smallest operation that satisfies intent. Prefer a named Rack macro with documented semantics. A guessed plugin parameter mapping is never acceptable.
- State expected result, measurable/observable check, risk, reversibility, and saved-before value.
- Return alternatives when the musical request has multiple valid interpretations. Example: “wider bass” may mean stereo upper harmonics or wider FX; ask or offer a plan that preserves mono sub.

## Approval and execution

All write plans start in `plan_only` and require a user approval record tied to the exact plan hash. Approval does not transfer to a changed plan. Before execution, re-read Set identity, target identity, current values, and automation/clip state. Abort on any mismatch.

High-impact operations need a saved recovery point and explicit approval per operation group: changing notes/arrangement/automation; inserting/replacing devices or presets; replacing samples; changing routes/sends; changing master chain; destructive render/resample; deleting; exporting to a named path; overwriting or archiving a project. Delete and overwrite operations are denied by default and require a separate explicit instruction.

## Verification and recovery

After a write, perform a new read and compare the actual state to the planned postcondition. Do not infer success from a successful API response. If a mismatch occurs, stop further edits. Roll back only the operation that this plan applied and only if the current value still matches that operation's result. If another actor changed the Set, do not overwrite their state; report what changed and the saved snapshot location.

## Never infer

- Do not map genre or an adjective directly to a fixed dB/frequency/plugin preset.
- Do not widen sub or kick fundamentals by default.
- Do not insert a device simply because its brand is mentioned.
- Do not flatten/freeze/delete, replace samples, change routing, or write automation without an approved plan.
- Do not claim a parameter is automatable or writable until discovery confirms it for the current Live/API version and device.
- Do not treat an LLM-generated plan as trusted code or pass arbitrary code/paths through a Bridge tool.

