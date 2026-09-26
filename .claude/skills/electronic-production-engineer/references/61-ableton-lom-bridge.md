# Ableton Live Object Model bridge

## Goal
Use Ableton's Live Object Model (LOM) as the primary control plane for AI-assisted production, through a constrained bridge. Screen (GUI) control is the fallback for what Live or the plug-in does not expose; here that already covers plug-in windows exposing nothing, Live's save/export menus and all Native Instruments software ([64](64-plugin-profile-strategy.md), [60](60-ableton-hardware-workflow.md)).

## Control planes in this studio
- **LOM Bridge** 0.8.1: Python Remote Script `LOMBridge` inside Live (UDP 127.0.0.1:7421, token in `~/Library/Application Support/LOMBridge/connection.json`), driven by `python3 lom.py <command>` (Mac: `$LOM_BRIDGE_DIR`, default `/Volumes/NO NAME/caude/lom-bridge`). Protocol: [lom-bridge/README.md](../../../../lom-bridge/README.md); usage: [bridge.md](../../ableton-live-session/references/bridge.md).
- **Producer Pal** (`ppal-*`): MIDI, clips, tracks, native devices in display units, routing, locators; no automation, no save, nothing inside a plug-in window.
- **Screen control** (`app_menu`, `app_screenshot`, `app_click`; `request_full_control`): Live menus (French UI), export, plug-in windows.
- **Max for Live** (`live.object`, `live.remote~`, `live.modulate~`, JS `LiveAPI`…) is not used for writes: its LOM cannot create automation envelopes and each `LiveAPI.set` is its own undo step ([Serum Live Bridge review](../../../../lom-bridge/REVUE-Serum-Live-Bridge-v0.1.md)); `lom-bridge/legacy/` is abandoned. No `live.remote~` device exists, so `performance_remote` is unavailable [TEST if one is built]; such a device disables direct editing/automation of its target while mapped, creates no undo steps and must be released (`id 0`).

## Discovery pass
Before any write, read: bridge/Live version and session; tempo, signature, transport, loop, locators; tracks (kind, mute/solo, volume, pan, sends); devices (ref, name, class, on, count of automated parameters); per target parameter: ref, name, min, max, value, display, quantized, `automation_state` (0 none, 1 automated, 2 overridden). `original_name`, `value_items`, `is_enabled` are readable only through `lom.py get <ref> <property>` [TEST]; the Set file name is not in the LOM (Live window title [TEST]). Only parameters present in the device panel are exposed: an unconfigured Serum 2 shows `Device On` only ([64](64-plugin-profile-strategy.md)).

## Read/write choices
Persistent edits go through typed bridge commands, which read back and journal themselves, or Producer Pal for native devices and clips; never `py`/`set`/`call` ([63](63-write-safety-and-automation.md)). Automation that must stay in the song is written with `apply`, inside arrangement clips. A manual write to an automated parameter overrides its automation.

## Live 12 conveniences
Live 12 copies LOM paths from context menus. From Live 12.4.3, Max for Live can open plug-in editor windows; here use `ppal-select` (`openPluginWindow: true`) or the device title bar's window button.

## Device and preset handling
Load only with `lom.py load "<track>" "<name>" [source] [replace=<device>]`. `browser.load_item` replaces the selected device wherever it is (hot-swap); `load` selects the track's last device (or the `replace=` target) and checks +1 device (same count with `replace=`), nothing replaced, no other track's device count changed. "Serum 2" exists as VST3 and AU: the ambiguous name is refused, give the path. Preset changes are high-impact; a plug-in exposing nothing can only be captured by saving the Set.

## Stable targeting rule
Never identify a target by index. Resolve by: 1) the exact name read in `state --json` / `params` (canonical names when the template uses them, [62](62-semantic-mapping-contract.md)); 2) device class/display name as confirmation; 3) semantic macro name; 4) the `o:<session>:<n>` ref, only as a handle within the same bridge session after the name matched. The bridge matches case-insensitively, exact first, else a unique substring (`E_AMBIGUOUS` otherwise); a digits-only name falls back to an **index**, so never send one. `master`/`main` = master track.

## Verification after every write
Read back: same object (echoed name and ref), parameter still enabled, value/display within tolerance, automation state unchanged unless intended, no protected rule violated. Confirm the bridge's own read-back with an independent read (limits below).

## Implementation in this studio
Checked in `lom.py` / `LOMBridge/__init__.py` 0.8.1; commands are `python3 lom.py …` subcommands. `ppal-*` and screen-control names come from the skills' recorded practice, not from code in this repository. Times: beats from 1|1 or `bar|beat` (`17|3.5`); signature read from Live (`--bpb n` forces it); `notes` windows are clip-relative.

| Stage | Real command / tool |
|---|---|
| Discover | `lom.py ping`; `state --json`; `param "<track>" <device\|mixer> <param>` (mixer: `Volume`, `Pan`, `Send A`); `params <deviceRef> [filter]`; `clips "<track>"`; `locators`; `notes get "<track>" <clipRef\|t> [tA tB]`; `read "<track>" <paramRef> <tA> <tB> --res 0.25`; `ppal-read-live-set`, `ppal-read-device`, `ppal-read-clip`; screenshots |
| Resolve | exact names from `state --json`; `track`/`param` echo name and ref; `solve <paramRef> <display value>` gives raw |
| Snapshot / preflight | `transport` (studio rule: stopped for `read`, `apply`, `notes`, `locator`, [63](63-write-safety-and-automation.md)); `param` for automation state; `snapshot "<track>" [device\|mixer]` → `sN`; `notes get … --json` or `snapshot_clips.py`; `apply spec.json --dry` / `plan` (writes nothing); save: Fichier › Sauver Set Live by screen ("Sauver Set Live sous…" at project start) |
| Execute (one group) | `setparam "<track>" <device\|mixer> <param> <value> [raw] [override]`; `apply spec.json` then `wait`; `notes set\|add "<track>" <clipRef\|t> '<json>' [tA tB]`; `load`; `locator <t> "<name>"`; `ppal-update-device`, `ppal-create-clip`, `ppal-update-clip`; screen control |
| Verify | built in: `set … <before> … <after> … <state>`, `verified <n> <max dev> <tol> exact\|sampled\|interrupted`, note-by-note and device-count checks; independent: `param`, `read`, `notes get`, `state --json` incl. neighbour chains, screenshot; `meters <t> <s> [tracks]` relative only, absolute levels from an export |
| Rollback | automatic undo in `apply`/`clear`/`notes`/`restore` (`E_ROLLED_BACK` = nothing changed); `restore sN` (one undo step, refused on automated parameters unless `override`); previous `apply` spec; notes from a snapshot JSON or `Backup/*.als` (`als_notes.py`) via `notes set`; conditions in [bridge-safety-and-semantics.md](../docs/bridge-safety-and-semantics.md) |
| Journal | `journal [n]` (`~/Library/Application Support/LOMBridge/journal.jsonl`), copied into the project memory ([memoire-projet](../../memoire-projet/SKILL.md)) with snapshot ids and refs |

Error codes: `E_STALE` → re-plan and re-approve; `E_AMBIGUOUS`/`E_NOT_FOUND`/`E_REF` → resolve again; `E_AUTOMATED`/`E_AUTOMATION_OVERRIDDEN` → [63](63-write-safety-and-automation.md); `E_TRANSPORT_PLAYING` → ask the user to stop; `E_NOT_APPLIED`/`E_VERIFY` → stop; `E_ROLLBACK_FAILED` → stop, Cmd+Z only under the [doc](../docs/bridge-safety-and-semantics.md)'s conditions; `E_TIMEOUT` → never resend: `jobs`/`wait`, `journal 3`, fresh read. Codes are derived from message text: read the text too.

## Known limits ([review 0.8.0](../../../../lom-bridge/DOSSIER-REVUE-LOM-Bridge-0.8.md), README)
- `tests/live_suite.py` last passed in Live at 0.4.x (26/26); all-or-nothing writes, read-back, typed commands, `load`, `notes` and the journal (0.5.0–0.8.x) rest on 60 offline tests [TEST in Live].
- `load` checks other tracks by device count only: re-read neighbouring chains.
- `notes set` ignores probability, velocity deviation and release; MPE expressions are not copied.
- Automation exists only inside clips; arrangement clips are rebuilt from Session (fades, note expressions, irreproducible warp need `accept`; looped-stretched clips and take lanes refused; gaps skipped with a warning); keeping existing audio-clip automation samples it, transport stopped (≈ 26 s per 8 bars).
- Audio read-back ends ≈ 0.5 s after the undo step closes: a user action in Live meanwhile would be undone instead.
- Snapshots hold exposed device parameters and mixer volume/pan/sends only, in memory until Live restarts (probably also lost at Set load [TEST]).
- A hot reload is lost at Set load (`ping` warns → relaunch Live); audio engine off → App Nap → timeouts.
