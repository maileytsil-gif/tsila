#!/bin/sh
# Lancer Claude Code sur un modèle local Ollama (Qwen…) avec les MÊMES skills, MCP et scripts.
# Usage : docs/claude-ollama.sh [modèle] [arguments Claude Code…]
#   docs/claude-ollama.sh                 # qwen3-coder par défaut
#   docs/claude-ollama.sh qwen3-coder:30b
#   docs/claude-ollama.sh qwen3-vl        # modèle avec vision : peut lire les captures d'écran
# Prérequis : Ollama ≥ 0.14, `ollama pull <modèle>`, contexte serveur ≥ 64k
# (OLLAMA_CONTEXT_LENGTH=65536 ollama serve, ou réglage « Context length » de l'app Ollama).
MODEL="${1:-qwen3-coder}"; [ $# -gt 0 ] && shift
export ANTHROPIC_BASE_URL="${OLLAMA_HOST:-http://localhost:11434}"
export ANTHROPIC_AUTH_TOKEN=ollama          # obligatoire, ignoré par Ollama
unset ANTHROPIC_API_KEY                      # une clé Anthropic présente prendrait le dessus
export ANTHROPIC_MODEL="$MODEL"
export ANTHROPIC_DEFAULT_OPUS_MODEL="$MODEL" ANTHROPIC_DEFAULT_SONNET_MODEL="$MODEL" ANTHROPIC_DEFAULT_HAIKU_MODEL="$MODEL"
export CLAUDE_CODE_SUBAGENT_MODEL="$MODEL"
cd "$(dirname "$0")/.." || exit 1
exec claude --model "$MODEL" "$@"
