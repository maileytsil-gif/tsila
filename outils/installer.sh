#!/usr/bin/env bash
# Installe les skills du dépôt pour Claude Code (~/.claude/skills) et Qwen Code (~/.qwen/skills), sur le Mac.
# Usage : bash outils/installer.sh [--claude] [--qwen] [--producer-pal-qwen] [--skill NOM]... [--appliquer]
#   Sans --appliquer : SIMULATION, rien n'est écrit ; la liste de ce qui changerait est affichée.
#   Sans --claude ni --qwen : chaque outil dont le dossier existe (~/.claude, ~/.qwen).
#   --claude            copie chaque skill dans ~/.claude/skills/<nom>
#   --qwen              ~/.qwen/skills/<nom> devient un lien vers la copie Claude (une seule copie à tenir à jour) ;
#                       sans copie Claude, le skill est copié dans ~/.qwen/skills/<nom>
#   --producer-pal-qwen ajoute le serveur MCP Producer Pal à ~/.qwen/settings.json (npx producer-pal@latest), s'il n'y est pas
#   --skill NOM         limiter à ce skill (répétable)
# Une version installée différente est déplacée dans ~/.skills-sauvegardes/<date>/<outil>/, HORS des dossiers de skills
# (une copie laissée à côté serait chargée comme un second skill du même nom). Les données de l'utilisateur rangées
# dans les skills (registre de signature de drums-signature) sont conservées si elles ont changé depuis l'installation.
set -euo pipefail
depot="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
source_skills="$depot/.claude/skills"
[[ -d "$source_skills" ]] || { echo "dossier introuvable : $source_skills" >&2; exit 1; }
# Fichiers que l'utilisateur fait évoluer dans sa copie installée : jamais écrasés.
DONNEES="drums-signature/references/signature.md drums-signature/scripts/signature.json"

claude=0; qwen=0; ppal=0; appliquer=0; choix=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --claude) claude=1 ;;
    --qwen) qwen=1 ;;
    --producer-pal-qwen) ppal=1 ;;
    --appliquer) appliquer=1 ;;
    --skill) shift; [[ $# -gt 0 ]] || { echo "--skill attend un nom" >&2; exit 2; }; choix="$choix $1" ;;
    -h|--help) sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "option inconnue : $1 (--help)" >&2; exit 2 ;;
  esac
  shift
done
if [[ $claude -eq 0 && $qwen -eq 0 && $ppal -eq 0 ]]; then
  [[ -d "$HOME/.claude" ]] && claude=1
  [[ -d "$HOME/.qwen" ]] && qwen=1
  if [[ $claude -eq 0 && $qwen -eq 0 ]]; then
    echo "Ni ~/.claude ni ~/.qwen : préciser --claude et/ou --qwen" >&2; exit 1
  fi
fi

if [[ -z "$choix" ]]; then
  for d in "$source_skills"/*/; do choix="$choix $(basename "$d")"; done
fi
for nom in $choix; do
  [[ -f "$source_skills/$nom/SKILL.md" ]] || { echo "skill inconnu dans le dépôt : $nom" >&2; exit 2; }
done

horodatage="$(date +%Y%m%d-%H%M%S)-$$"   # + numéro de processus : deux lancements dans la même seconde ne se mélangent pas
sauvegardes="$HOME/.skills-sauvegardes/$horodatage"
mode="SIMULATION (ajouter --appliquer pour écrire)"; [[ $appliquer -eq 1 ]] && mode="INSTALLATION"
echo "$mode — depuis $source_skills"
changements=0

faire() {  # affiche l'action, l'exécute seulement avec --appliquer
  echo "  $1"; shift
  changements=$((changements + 1))
  if [[ $appliquer -eq 1 ]]; then "$@"; fi
}

identique() {  # $1 dépôt, $2 installé : même contenu, caches Python et données utilisateur exclus
  diff -rq -x '__pycache__' -x '*.pyc' -x '.DS_Store' -x 'signature.md' -x 'signature.json' "$1" "$2" >/dev/null 2>&1
}

sauvegarder() {  # $1 chemin installé, $2 outil
  mkdir -p "$sauvegardes/$2"
  mv "$1" "$sauvegardes/$2/"
}

copier() {  # $1 nom, $2 dossier de skills cible, $3 outil
  local src="$source_skills/$1" cible="$2/$1" garde=""
  if [[ -L "$cible" ]]; then
    faire "$3 : $1 était un lien ($(readlink "$cible")) → remplacé par une copie (lien sauvegardé)" sauvegarder "$cible" "$3"
  elif [[ -d "$cible" ]]; then
    if identique "$src" "$cible"; then echo "  $3 : $1 à jour"; return; fi
    for f in $DONNEES; do
      case "$f" in "$1"/*)
        local rel="${f#"$1"/}"
        if [[ -f "$cible/$rel" ]] && ! cmp -s "$src/$rel" "$cible/$rel"; then garde="$garde $rel"; fi ;;
      esac
    done
    faire "$3 : $1 mis à jour (ancienne version → $sauvegardes/$3/$1)" sauvegarder "$cible" "$3"
  elif [[ -e "$cible" ]]; then
    echo "  $3 : $cible existe et n'est pas un dossier : laissé tel quel" >&2; return
  fi
  faire "$3 : $1 copié dans $cible" cp -R "$src" "$cible"
  if [[ $appliquer -eq 1 ]]; then
    find "$cible" -name '__pycache__' -type d -prune -exec rm -rf {} +
    find "$cible" \( -name '*.py' -o -name '*.sh' \) -path '*/scripts/*' -exec chmod +x {} +
  fi
  for rel in $garde; do
    faire "$3 : $1/$rel conservé (données de l'utilisateur, différentes du dépôt)" cp -p "$sauvegardes/$3/$1/$rel" "$cible/$rel"
  done
}

if [[ $claude -eq 1 ]]; then
  echo "Claude Code → ~/.claude/skills"
  [[ $appliquer -eq 1 ]] && mkdir -p "$HOME/.claude/skills"
  for nom in $choix; do copier "$nom" "$HOME/.claude/skills" claude; done
fi

if [[ $qwen -eq 1 ]]; then
  echo "Qwen Code → ~/.qwen/skills"
  [[ $appliquer -eq 1 ]] && mkdir -p "$HOME/.qwen/skills"
  for nom in $choix; do
    lien="$HOME/.qwen/skills/$nom"; cible="$HOME/.claude/skills/$nom"
    if [[ -d "$cible" || ( $claude -eq 1 && $appliquer -eq 0 ) ]]; then
      if [[ -L "$lien" && "$(readlink "$lien")" == "$cible" ]]; then echo "  qwen : $nom déjà relié"; continue; fi
      if [[ -e "$lien" || -L "$lien" ]]; then
        faire "qwen : $nom existant sauvegardé ($sauvegardes/qwen/$nom)" sauvegarder "$lien" qwen
      fi
      faire "qwen : $nom → lien vers $cible" ln -s "$cible" "$lien"
    else
      copier "$nom" "$HOME/.qwen/skills" qwen
    fi
  done
fi

if [[ $ppal -eq 1 ]]; then
  reglages="$HOME/.qwen/settings.json"
  if [[ -f "$reglages" ]] && python3 -c 'import json,sys; sys.exit(0 if "producer-pal" in (json.load(open(sys.argv[1])).get("mcpServers") or {}) else 1)' "$reglages" 2>/dev/null; then
    echo "Producer Pal déjà déclaré dans $reglages"
  else
    ajouter_ppal() {
      mkdir -p "$HOME/.qwen"
      if [[ -f "$reglages" ]]; then mkdir -p "$sauvegardes/qwen"; cp -p "$reglages" "$sauvegardes/qwen/settings.json"; fi
      python3 - "$reglages" <<'PY'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1])
data = json.loads(p.read_text()) if p.exists() and p.read_text().strip() else {}
if not isinstance(data, dict): raise SystemExit(f'{p} : objet JSON attendu')
data.setdefault('mcpServers', {})['producer-pal'] = {'command': 'npx', 'args': ['-y', 'producer-pal@latest']}
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
PY
    }
    faire "qwen : serveur MCP producer-pal ajouté à $reglages (Node.js 20+ et le device Producer_Pal.amxd dans Live requis)" ajouter_ppal
  fi
fi

if [[ $changements -eq 0 ]]; then echo "Rien à changer."
elif [[ $appliquer -eq 0 ]]; then echo "$changements changement(s) prévus. Relancer avec --appliquer pour les faire."
else echo "$changements changement(s) faits. Relancer Claude Code / Qwen Code pour recharger les skills."; fi
