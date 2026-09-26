# Ableton Bridge: semantic plans and safe execution

This document is the single source for approval, save points, one step per exchange, verification and rollback conditions. [`references/61`](../references/61-ableton-lom-bridge.md)–[`64`](../references/64-plugin-profile-strategy.md) point here; where an older rule there differed, the stricter one below applies. Real commands for each stage: [`references/61`](../references/61-ableton-lom-bridge.md), section "Implementation in this studio".

## Intent vocabulary

Translate requests into a musical intent object before mapping them to Live. Core concepts include `role` (kick, sub, mid-bass, snare, hat, percussion, lead, chord, vocal, FX), `goal` (more/less punch, darker/brighter, narrower/wider, nearer/farther, denser/sparser), `scope` (frequency range, section, time range, stereo component), `amount` (user-provided or explicitly proposed), and `constraints` (preserve mono sub, keep vocal intelligible, don't alter master).

Keep a distinction between:

1. **Observation:** facts read from the current Set, including confidence and timestamp.
2. **Musical intent:** what the user wants to hear/change.
3. **Implementation proposal:** a mapped target and operation, or `needs_mapping`.
4. **Execution:** only exact approved operations.
5. **Verification:** fresh observations compared with expected postconditions.

## Resolve and plan

- Match by stable track/rack/macro labels first; include object IDs as ephemeral evidence, never as the only identity. Bridge refs `o:<session>:<n>` are valid only inside one bridge session (they change when Live restarts or the control surface is re-instantiated).
- Require exactly one target. Ambiguous aliases, duplicated track names, stale IDs, hidden routing, unavailable devices, or unknown parameter units stop execution. The bridge's substring matching is a convenience, not a resolution: send the exact name and check the echoed name.
- Plan the smallest operation that satisfies intent. Prefer a named Rack macro with documented semantics. A guessed plugin parameter mapping is never acceptable, whatever its confidence score.
- State expected result, measurable/observable check, risk, reversibility, and saved-before value.
- Return alternatives when the musical request has multiple valid interpretations. Example: “wider bass” may mean stereo upper harmonics or wider FX; ask or offer a plan that preserves mono sub.

## Approval and execution

All write plans start in `plan_only` and require a user approval record tied to the exact plan hash, whatever the confidence level. Approval does not transfer to a changed plan. Before execution, re-read Set identity, target identity, current values, and automation/clip state. Abort on any mismatch.

High-impact operations need a saved recovery point and explicit approval per operation group: changing notes/arrangement/automation; inserting/replacing devices or presets; replacing samples; changing routes/sends; changing master chain; destructive render/resample; deleting; exporting to a named path; overwriting or archiving a project. Delete and overwrite operations are denied by default and require a separate explicit instruction.

In this studio:
- **Approval** is the user's reply in the conversation. The plan digest is a hash of the exact artefact that will run (e.g. `shasum -a 256 spec.json` for an `apply` spec, or the exact command line); run that artefact unchanged. `E_STALE` or any edit to the spec means a new plan and a new approval.
- **One step per exchange:** announce the whole plan, then execute one approved group, verify, report and stop. The user often edits the Set between exchanges: every exchange starts with a fresh read (`lom.py ping`, `lom.py state --json`, `lom.py transport`).
- **Set identity:** bridge `session` from `ping`, plus the `state --json` fingerprint (track names, device lists, tempo, locators) and the Set name in the Live window title [TEST]. A different session or fingerprint means re-discover.
- **Save before and after:** "Sauver Set Live sous…" under a new name before the first change to a project; Fichier › Sauver Set Live (screen control; neither the bridge nor Producer Pal can save) before each high-impact group and after each validated step. A greyed-out item means nothing to save. Live keeps a dated copy in the project's `Backup/` folder at each save.
- **Never** use `accept=unverified`. `override`, `song.re_enable_automation()` and each `accept` entry (`fades`, `expressions`, `warp`, `clamp`) need explicit approval; a `lom.py policy` entry is a standing approval ([`references/63`](../references/63-write-safety-and-automation.md)). Never run `lom.py serve --unsafe`.

## Verification and recovery

After a write, perform a new read and compare the actual state to the planned postcondition. Do not infer success from a successful API response. The bridge's own read-back lines (`set … before … after`, `verified … exact|sampled`, note-by-note checks) are required but not sufficient: its 0.5.0–0.8.x behaviour has not been replayed in Live yet, so add an independent read (`param`, `read`, `notes get`, `state --json`, a screenshot for window edits). `verified … interrupted` means written but not checked. If a mismatch occurs, stop further edits.

Roll back only the operation that this plan applied and only if the current value still matches that operation's result. If another actor changed the Set, do not overwrite their state; report what changed and the saved snapshot location. With the real tools:
- `lom.py restore <id>` rewrites every value of the snapshot (whole track, device or mixer). Before using it, take a new snapshot and compare: restore only if the differences are exactly this plan's writes; otherwise restore those parameters one by one with `setparam` after approval, or ask. Snapshots vanish when Live restarts: keep original values in the project memory too.
- Cmd+Z and `song.undo()` undo Live's latest step, whoever made it: use them only when nothing else happened since, and tell the user. `E_ROLLED_BACK` means the bridge already undid its step; `E_ROLLBACK_FAILED` means its write is partly applied: Cmd+Z at once if nothing else happened in Live since, telling the user; otherwise decide with the user.
- After `E_TIMEOUT`, never resend a write: check `lom.py jobs` / `wait`, `lom.py journal 3`, then read state.
- Window edits (Serum 2, Pro-Q 4, soothe3) have no bridge snapshot or journal: the saved Set is their recovery point.

## Never infer

- Do not map genre or an adjective directly to a fixed dB/frequency/plugin preset.
- Do not widen sub or kick fundamentals by default.
- Do not insert a device simply because its brand is mentioned.
- Do not flatten/freeze/delete, replace samples, change routing, or write automation without an approved plan.
- Do not claim a parameter is automatable or writable until discovery confirms it for the current Live/API version and device (an unconfigured plug-in with over 64 parameters exposes `Device On` only, [`references/64`](../references/64-plugin-profile-strategy.md)).
- Do not treat an LLM-generated plan as trusted code or pass arbitrary code/paths through a Bridge tool: no `lom.py py`, `set` or `call` for writes, except the approved `song.re_enable_automation()` ([`references/63`](../references/63-write-safety-and-automation.md)).
