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

## Where the session runs (check first)
- **Cloud session** (claude.ai container, e.g. a web or mobile session): it sees the repository, the corpus and files the user uploads, and can run the analysis scripts on those files; it **cannot reach the user's Mac**, so Live, Producer Pal, `lom.py`, plug-in windows, Maschine and Komplete Kontrol are out of reach. Highest possible mode: `AUDIO_ANALYSIS` on uploaded renders, otherwise `ADVICE_ONLY`. Say so in one line and point the user to a session on the Mac: Claude Desktop opened on `~/tsila`, or `cd ~/tsila && git pull && claude remote-control` (the session then appears in the Claude Code app). Hand over through a project memory file (`../../memoire-projet/SKILL.md`; example: `../../../../docs/projets/projet-test-basse-future-house.md`) so nothing is lost.
- **Local session on the Mac** (Claude Code CLI, Desktop or Remote Control): all modes below are possible, each only once its channel is verified.

## Tools per mode in this studio
| Mode | Channel | Verify with |
|---|---|---|
| `AUDIO_ANALYSIS` | exported WAV + `../../live-export-wav/scripts/analyze_wav.py` (duration, peaks, clipping, tails), `../../kick-bass-equilibre/scripts/kick_bass_check.py` (kick/sub correlation 30–120 Hz), `../../synthese-reference/scripts/analyze_synth.py` (one sound vs a reference); LUFS/true peak on the exported file with WLM Plus or Insight in Live, or pyloudnorm / ffmpeg `ebur128` where installed (`01-studio-inventory.md` lists what is absent) | the report of the script, never a meter glance |
| `BRIDGE_READONLY` | Producer Pal read tools (`ppal-read-*`), `lom.py state`, `lom.py snapshot`, `../../arrangement-avance/scripts/arrangement_map.py`, `../../mixage/scripts/mix_snapshot.py` | a fresh read with timestamp |
| `BRIDGE_WRITE` | Producer Pal writes for MIDI, clips and native devices; `lom.py` typed writes and automation; save before and after | re-read after every write (`61-ableton-lom-bridge.md`, `63-write-safety-and-automation.md`) |
| `SCREEN_CONTROL` | clicks in plug-in windows (Serum 2 edits beyond what Live exposes, Maschine, Komplete Kontrol: no API) | a screenshot or a parameter read after each change; say what could not be verified |

`lom.py meters` and `levels.sh` values are relative indications, not calibrated measurements: absolute peaks and loudness come from the exported file.

## Escalation rule
Never silently escalate from ADVICE_ONLY to a measurement claim, from BRIDGE_READONLY to BRIDGE_WRITE, or from a cloud session to any claim about the user's Live Set. If the needed capability is unavailable, return the next best test or action plan.

## Confidence labels
- HIGH: direct measurement/state + unambiguous mapping.
- MEDIUM: strong evidence but one relevant variable is unresolved.
- LOW: inference/start point; inspect or audition before committing.

For LOW confidence bridge changes, prefer `inspect`/`plan` over direct write.
