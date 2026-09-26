# Local model routing contract (Qwen / Ollama)

## Selection flow

1. Classify the request into phases: `brief`, `composition`, `sound_design`, `arrangement`, `spatial_mix_plan`, `mix`, `master`, `qc_export`, `archive`, `bridge_discovery`, or `bridge_plan`.
2. Load `SKILL.md`, the matching workflow section, and only the needed reference module. Do not inject the whole archive by default.
3. For Bridge discovery, use a read-only tool and return observed facts with freshness. For all edits, generate a schema-valid `semantic-bridge-plan` with `mode: plan_only`.
4. Validate model output as untrusted JSON: reject extra properties, unknown operation types, paths outside the configured project root, non-finite numbers, unresolved targets, stale Set IDs, and plans missing risk/verification/rollback details.
5. Execution is disabled unless a separately configured trusted Bridge adapter exposes a narrow allowlist. Require user approval of the exact plan digest and run preflight again immediately before execution.

## Suggested routing hints

- Composition/harmony → `docs/production-workflow.md` + user brief; keep musical suggestion separate from MIDI mutation.
- Genre arrangement → section/energy plan only; do not assume stock bar counts or fixed build/drop behavior.
- Serum/Maschine/Simpler sampling → `docs/user-setup-and-control-surfaces.md`; request version/device discovery before parameter-specific guidance.
- Stereo/spectrum/mix → `examples/example-spatial-mix-plan.json` + bridge semantics; protect low-end and require mono/correlation checks.
- Export/archive → production workflow + official Ableton source index; ask for exact export format and destination before render/write.
- Ableton “do this” request → discovery, semantic mapping, plan, approval, execute, verify. Never jump directly from a natural-language prompt to raw LOM calls.

## Local command integration

An Ollama client may retrieve files and call a model, but this handoff does not include a privileged Bridge client or credentials. Model APIs should return proposals only. Connect an execution tool only after implementing authentication, capability allowlists, path scoping, audit logs, preflight, and postcondition checks.

