# Install / use the same skill everywhere

## Claude Code
Claude Code supports Agent Skills directories. Copy this whole folder to either:
- personal: `~/.claude/skills/electronic-production-engineer/`
- project: `.claude/skills/electronic-production-engineer/`
Then invoke `/electronic-production-engineer` or ask a matching production question and let Claude load it automatically.

## Qwen Code
Copy this whole folder to:
- personal: `~/.qwen/skills/electronic-production-engineer/`
- project: `.qwen/skills/electronic-production-engineer/`
Then invoke `/electronic-production-engineer` or use `/skills`.

## ChatGPT / OpenAI Agent Skills
The folder follows the Agent Skills layout (`SKILL.md` + supporting resources). Where Skills upload is available, upload the ZIP/folder. Otherwise attach the folder/ZIP or relevant references to the conversation/project. The same `SKILL.md` remains the canonical playbook.

## Ollama + Qwen
Ollama does not use Agent Skills directory discovery by itself. Use `ollama/run_skill.py` in this pack. It loads the canonical `SKILL.md`, selects only relevant reference files, and calls the local Ollama chat API.

Examples:
`python3 ollama/run_skill.py --model qwen3:8b "Analyse mon kick et ma basse Tech House"`

`python3 ollama/run_skill.py --model qwen3:14b --all "Fais un audit complet de ce plan de mastering"`

The runner expects Ollama at `http://localhost:11434` unless `OLLAMA_HOST` is set.


## Bridge-focused use
For code agents, ask the model to read `bridge/README.md`, then the four `references/61-64` files before editing any existing Ableton bridge. Machine-generated discovery snapshots should validate against `schemas/ableton-discovery.schema.json`; write plans should validate against `schemas/ableton-command.schema.json`.
