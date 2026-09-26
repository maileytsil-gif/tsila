# Write safety, automation and reversibility

## Default posture
Discovery is read-only. Any write plan must be explicit about target, operation, magnitude, reason and verification.

## Protected targets
Treat these as protected unless the user specifically asks for them:
- Master output level and limiter ceiling.
- True sub width / mono controls below the chosen mono boundary.
- Track activators that would mute critical content.
- Preset changes on instruments with unsaved sound design.
- Sidechain routing.
- Device deletion, track deletion and destructive clip replacement.

## Parameter state checks
Before writing a DeviceParameter:
- `is_enabled` must allow direct modification.
- inspect `automation_state`.
- if automation is active, do not silently override it. Prefer editing the automation envelope through the appropriate implementation or request/emit an automation-specific plan.
- if automation is overridden, flag it and optionally re-enable automation only when intended.

## live.remote~ warning
`live.remote~` is for realtime remote control. It disables ordinary direct editing/automation of the target while mapped, creates no normal undo steps for the remote stream, and should be released after use. Do not use it as the default persistent edit path.

## Bounded changes
For subjective production changes, start with conservative bounded moves unless the user requests an extreme effect. Express changes in semantic normalized deltas where possible and verify by audio/measurement.

## Transaction pattern
For a multi-action plan:
1. scan and resolve all targets,
2. validate all writes,
3. capture pre-change values,
4. apply one logical group at a time,
5. read back,
6. compare/audition,
7. roll back the logical group if verification fails.

## Human takeover
Hardware movement by APC64, Maschine MK3 or A49 should take priority during active performance. The bridge must avoid fighting a parameter the user is touching. Implementations should use a short takeover lock/debounce window when MIDI/hardware activity is detected.

## Gain-matched decision rule
For processing changes that affect loudness, compare at matched perceived level before deciding the change is better.

## Confidence gate
- HIGH confidence: resolved current path/id plus verified semantic mapping; bounded writes may proceed when authorized.
- MEDIUM confidence: mapping is plausible but one detail is unresolved; prefer a plan, small test move, or visible confirmation.
- LOW confidence: do not write. Inspect or request/perform a verification step first.

## Commit actions
Freeze/flatten, consolidate/overwrite, destructive sample edits, preset replacement and permanent routing rewrites are `commit` actions. Preserve or archive the source and require an explicit rollback path before execution.
