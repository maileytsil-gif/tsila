# Capability modes and evidence boundaries

## Purpose
Prevent the model from claiming it listened, measured or changed Ableton when the required input/control channel is not available.

## Modes
### ADVICE_ONLY
Use when there is no audio file, analyzer output or live Ableton snapshot. Give hypotheses, starting points and listening tests. Never write "I hear", "the spectrum shows" or quote measured LUFS/peak/phase values.

### AUDIO_ANALYSIS
Use when rendered audio/stems or trusted analyzer measurements are available. Measurements may be marked `MEASURED`; subjective interpretation remains `OBSERVED` or `INFERRED`.

### BRIDGE_READONLY
Use when the Live Object Model/bridge can inspect the Set but writes are not authorized. Discovery, parameter resolution and planning are allowed. Do not imply a parameter was changed.

### BRIDGE_WRITE
Use only when the control channel is connected and the requested write is authorized. Follow discover -> resolve -> plan -> preflight -> execute -> verify -> rollback. Preserve automation and capture pre-change state.

## Escalation rule
Never silently escalate from ADVICE_ONLY to a measurement claim, or from BRIDGE_READONLY to BRIDGE_WRITE. If the needed capability is unavailable, return the next best test or action plan.

## Confidence labels
- HIGH: direct measurement/state + unambiguous mapping.
- MEDIUM: strong evidence but one relevant variable is unresolved.
- LOW: inference/start point; inspect or audition before committing.

For LOW confidence bridge changes, prefer `inspect`/`plan` over direct write.
