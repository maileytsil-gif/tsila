# Write safety, automation and reversibility

## Default posture
Discovery is read-only. Any write plan must be explicit about target, operation, magnitude, reason and verification, starts in `plan_only`, and waits for approval of that exact plan whatever its confidence. Approval, save points, one step per exchange, verification and rollback conditions are defined once in [docs/bridge-safety-and-semantics.md](../docs/bridge-safety-and-semantics.md); real commands are mapped in [61](61-ableton-lom-bridge.md).

## Protected targets
Denied unless the user asks for that specific target:
- Master output level, limiter ceiling and the master chain (`BUS MASTER 1/2/3`, Main).
- True sub width / mono controls below the chosen mono boundary.
- Track activators, mutes and device On/Off that would silence critical content.
- Preset changes on instruments with unsaved sound design (a Serum 2 sound lives only in the Set or a preset file; no bridge snapshot can capture it).
- Sidechain routing.
- Device, track and clip deletion and destructive clip replacement: denied by default, separate explicit instruction. Never delete a clip to rewrite it (its automation lives on it): rewrite its notes in place (`notes set`); never remove silent clips that carry bus automation.

## Parameter state checks
Right before writing, read `automation_state` with `lom.py param` (0 none, 1 automated, 2 overridden by a manual change).
- 0: `setparam` may write after approval; it reports before/after and the new state.
- 1 or 2: `setparam` refuses (`E_AUTOMATED`) because a manual write overrides the automation. Default: write automation instead (`apply`; a static value = two equal points over the clip range, [live-automation](../../live-automation/SKILL.md)). `override` only with explicit approval naming the parameter; report that Live will show "Re-Enable Automation".
- 2, also: plans that must sample existing automation are refused (`E_AUTOMATION_OVERRIDDEN`). `song.re_enable_automation()` (via `lom.py py`) is Live's global re-enable: it discards every manual override in the Set, not only the target. Ask first, then check the target reads state 1.
- Quantized parameters take integer `raw` values; out-of-range values are refused, never silently clamped; `accept=clamp` needs explicit approval.
- `is_enabled`: read it (`lom.py get <paramRef> is_enabled`) when in doubt [TEST].

## Automation writes
`apply spec.json --dry` first and show the plan (clips, resolved values, gaps, sampling and read-back seconds). Transport must be stopped: ask, never stop it silently. Never `accept=unverified`. `fades`, `expressions`, `warp` only when the plan lists them and the user accepts the loss. `lom.py policy accept=…` is a standing approval: only `expressions` for Sets without MPE, recorded in the project memory; never `unverified` or `clamp`. Ask the user not to act in Live during an audio-clip write (undo window, [61](61-ableton-lom-bridge.md)). Afterwards show a `read --res 0.25` table (one value per bar).

## live.remote~ warning
`live.remote~` is for realtime remote control only: it disables direct editing/automation of the target while mapped, creates no undo steps and must be released after use. Never a persistent edit path; not installed here ([61](61-ableton-lom-bridge.md)).

## Commands outside the contract
`lom.py py`, `set`, `call`, `reload` and `serve --unsafe` bypass validation, read-back, undo grouping and the journal (`/py`, `/set`, `/call` are not journaled). Use `py` only for read-only skill scripts (`pyl.sh`, `snapshot_clips.py`) and the approved `song.re_enable_automation()`, and log that call in the project memory by hand. `lom.py serve` also accepts typed writes over HTTP: it adds no approval layer.

## Bounded changes
For subjective production changes, start with conservative bounded moves unless the user requests an extreme effect. `setparam` has no delta (compute from the `param` reading); an `apply` spec's `unit: "rel"` offsets the current display value. Verify by read-back, relative `meters`, an export and the user's listening; never claim to have heard.

## Transaction pattern
One logical group per exchange (usually one bridge command):
1. scan and resolve all targets (`state --json`, `param`),
2. validate all writes (`apply --dry` / `plan`; schemas),
3. capture pre-change values (`snapshot`, `notes get --json`, archived spec) and save the Set,
4. apply one logical group after approval,
5. read back independently,
6. compare/audition,
7. roll back under the [doc](../docs/bridge-safety-and-semantics.md)'s conditions if verification fails; stop and report either way.

## Human takeover
The real bridge has no MIDI/hardware activity detection and no takeover lock (confirmed in code). Before each write, confirm the user is not performing on APC64, Maschine or the keyboard; writes during playback are audible, say so. The bridge itself refuses a playing transport only for `read`, a new `locator`, `transport pos` and automation writes that must sample; `setparam`, `restore`, `load` and `notes` run during playback. Studio rule (stricter): `read`, `apply`, `notes` and `locator` only with the transport stopped, and ask before stopping it. After the user has touched the Set, re-read before acting.

## Gain-matched decision rule
For processing changes that affect loudness, compare at matched perceived level before deciding the change is better.

## Confidence gate
- HIGH (resolved current name/ref plus verified mapping): may be proposed as an executable plan; still needs approval.
- MEDIUM (one detail unresolved): plan an inspect step, a small test move or a visible confirmation first.
- LOW: do not write. Inspect or request/perform a verification step first.

## Commit actions
Freeze/flatten, consolidate/overwrite, destructive sample edits, preset replacement and permanent routing rewrites are `commit` actions. Preserve or archive the source and require an explicit rollback path before execution; the minimum recovery point is a saved Set (Live keeps a dated copy in the project's `Backup/` folder at each save).
