# Model-specific guidance

## Claude Code
Let the skill route to supporting files; avoid pasting all references into CLAUDE.md. Claude Code loads skill bodies on demand, which is more context-efficient. For bridge/code implementation, ask Claude to inspect existing files before changing them.

## Qwen Code
Use the same SKILL.md. Qwen Code can model-invoke skills or run them explicitly. For local providers, larger Qwen Coder/Qwen3 variants will follow the multi-file workflow more reliably than very small models.

## Qwen via Ollama
Keep prompts concrete. The included runner loads a compact set of references based on the request. Use `--all` only for broad architecture/review tasks. If the model supports thinking, use it for analysis-heavy tasks but keep final actions concise.

## Cross-model rule
The canonical knowledge is in this folder. Do not maintain separate rewritten copies for each model; adapter prompts should only explain loading/tool mechanics.


## Bridge mode
For all models: discovery and planning are separate from execution. Do not turn a natural-language production request directly into raw LOM writes. Resolve semantic names from the active discovery snapshot, check automation and enabled state, then validate the command object before execution.
