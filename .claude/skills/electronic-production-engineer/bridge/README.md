# Bridge contract for implementers

This folder defines the semantic layer used by Claude Code, Qwen Code, Qwen/Ollama or another coding agent when building/operating an Ableton bridge. In this studio the bridge exists (`LOMBridge` Remote Script + `lom.py`, [lom-bridge/README.md](../../../../lom-bridge/README.md)) and does not read these schemas: the model validates its plan against them, then runs `lom.py` commands or an `apply` spec.

## Runtime sequence
| Stage | Contract | Real tool (details: [references/61](../references/61-ableton-lom-bridge.md)) |
|---|---|---|
| 1. `discover` | read-only snapshot, validated against `schemas/ableton-discovery.schema.json` | `lom.py ping`, `lom.py state --json`, `param`, `params`, `clips`, `notes get`, `read`; `ppal-read-*` |
| 2. `resolve` | canonical track/Rack/semantic names → real object refs | exact names from `state --json`; `o:<session>:<n>` refs valid for one bridge session |
| 3. `plan` | commands validating against `schemas/ableton-command.schema.json` | `lom.py apply spec.json --dry` / `lom.py plan` (server plan, nothing written) |
| 4. `preflight` | enable/automation/protection state, old values stored | `lom.py transport`, `param` (automation state), `lom.py snapshot`, Set saved by screen control |
| 5. `execute` | one approved logical action group | `setparam`, `apply`, `notes set`, `load`, `locator`; Producer Pal; screen control for windows |
| 6. `verify` | read back, audio/measurement checks when possible | bridge read-back plus an independent read; `meters` (relative only) |
| 7. `rollback` | restore old values if verification fails | `lom.py restore <id>` under the conditions of [bridge-safety-and-semantics.md](../docs/bridge-safety-and-semantics.md) |
| 8. `journal` | record what was written | `lom.py journal [n]` copied into the project memory |

Approval (one group per exchange, save before and after) sits between 4 and 5; the rules are in [docs/bridge-safety-and-semantics.md](../docs/bridge-safety-and-semantics.md).

## Implementation guidance
- Keep discovery and planning separate from execution.
- Never let an LLM write arbitrary Max/Live API calls directly from prose without schema validation: no `lom.py py`, `set`, `call` or `serve --unsafe` for writes, apart from the one approved exception in [references/63](../references/63-write-safety-and-automation.md).
- Use semantic names first and runtime ids second.
- Prefer Rack macros for stable musical controls.
- Use GUI automation only for functions not exposed to LOM; in this studio that includes most Serum 2 edits, Pro-Q 4, soothe3, Live's save/export menus and all Native Instruments software ([references/64](../references/64-plugin-profile-strategy.md)).
