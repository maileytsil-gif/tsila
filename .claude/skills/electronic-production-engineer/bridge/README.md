# Bridge contract for implementers

This folder defines the semantic layer used by Claude Code, Qwen Code, Qwen/Ollama or another coding agent when building/operating an Ableton bridge.

## Runtime sequence
1. `discover`: obtain a read-only LOM snapshot and validate it against `schemas/ableton-discovery.schema.json`.
2. `resolve`: map canonical track/Rack/semantic names to real object ids/paths.
3. `plan`: produce commands that validate against `schemas/ableton-command.schema.json`.
4. `preflight`: check enable/automation/protection state and store old values.
5. `execute`: apply one logical action group.
6. `verify`: read back and, when possible, perform audio/measurement checks.
7. `rollback`: restore old values if verification fails.

## Implementation guidance
- Keep discovery and planning separate from execution.
- Never let an LLM write arbitrary Max/Live API calls directly from prose without schema validation.
- Use semantic names first and runtime ids second.
- Prefer Rack macros for stable musical controls.
- Use GUI automation only for functions not exposed to LOM.
