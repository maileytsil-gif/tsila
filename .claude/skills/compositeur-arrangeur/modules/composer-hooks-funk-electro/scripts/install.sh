#!/usr/bin/env bash
# Installe le skill compositeur-arrangeur (dont ce module composer-hooks-funk-electro est un dossier de modules/)
# pour Claude Code (~/.claude/skills), Codex CLI (~/.codex/skills) et le lanceur Qwen/Ollama (~/.local/bin/qwen-musique).
# Usage : bash scripts/install.sh [--claude] [--codex] [--qwen] [--tout]
#   sans option : chaque outil présent (dossier ~/.claude, dossier ~/.codex, commande ollama).
# Une version déjà installée est déplacée dans ~/.skills-sauvegardes/, HORS des dossiers de skills :
# une copie laissée à côté (même « name: ») serait chargée comme un second skill. Pour Claude Code et Qwen Code,
# outils/installer.sh à la racine du dépôt installe les cinq skills d'un coup ; ce script sert surtout à Codex et Ollama.
set -euo pipefail
module_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
skill_dir="$(cd "$module_dir/../.." && pwd -P)"
name="compositeur-arrangeur"
module="composer-hooks-funk-electro"
[[ -f "$module_dir/GUIDE.md" && -f "$skill_dir/SKILL.md" && "$(basename "$skill_dir")" == "$name" ]] \
  || { echo "arborescence inattendue : $module_dir doit être $name/modules/$module" >&2; exit 1; }

claude=0; codex=0; qwen=0
if [[ $# -eq 0 ]]; then
  [[ -d "$HOME/.claude" ]] && claude=1
  [[ -d "$HOME/.codex" ]] && codex=1
  command -v ollama >/dev/null 2>&1 && qwen=1
fi
for arg in "$@"; do
  case "$arg" in
    --claude) claude=1 ;;
    --codex) codex=1 ;;
    --qwen) qwen=1 ;;
    --tout) claude=1; codex=1; qwen=1 ;;
    -h|--help) sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "option inconnue : $arg (--claude, --codex, --qwen, --tout)" >&2; exit 2 ;;
  esac
done
if [[ $((claude + codex + qwen)) -eq 0 ]]; then
  echo "Aucun outil détecté (~/.claude, ~/.codex, ollama) : préciser --claude, --codex, --qwen ou --tout" >&2; exit 1
fi

sauvegardes="$HOME/.skills-sauvegardes"
installe=""
install_to() {  # $1 = dossier de skills, $2 = étiquette
  local cible="$1/$name"
  mkdir -p "$1"
  if [[ -d "$cible" && "$(cd "$cible" && pwd -P)" == "$skill_dir" ]]; then
    echo "$2 : déjà installé depuis ce dossier ($cible)"; installe="${installe:-$cible}"; return
  fi
  if [[ -e "$cible" || -L "$cible" ]]; then
    mkdir -p "$sauvegardes"
    local sauvegarde="$sauvegardes/$name.$2.$(date +%Y%m%d%H%M%S)"
    mv "$cible" "$sauvegarde"
    echo "$2 : ancienne version conservée dans $sauvegarde"
  fi
  cp -R "$skill_dir" "$cible"
  find "$cible" -name '__pycache__' -type d -prune -exec rm -rf {} +
  find "$cible" \( -name '*.py' -o -name '*.sh' \) -path '*/scripts/*' -exec chmod +x {} +
  echo "$2 : installé dans $cible (skill $name, module $module compris)"
  installe="${installe:-$cible}"
}
[[ $claude -eq 1 ]] && install_to "$HOME/.claude/skills" claude
[[ $codex -eq 1 ]] && install_to "$HOME/.codex/skills" codex

if [[ $qwen -eq 1 ]]; then
  source_qwen="${installe:-$skill_dir}/modules/$module/scripts/qwen-musique.py"
  mkdir -p "$HOME/.local/bin"
  ln -sf "$source_qwen" "$HOME/.local/bin/qwen-musique"
  chmod +x "$source_qwen"
  echo "qwen : ~/.local/bin/qwen-musique → $source_qwen"
  echo '      qwen-musique --model NOM_DE_ollama_list "votre demande"   (--dry-run pour voir les références choisies)'
  case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) echo "      ~/.local/bin n'est pas dans le PATH : l'y ajouter ou appeler le chemin complet" ;; esac
fi
