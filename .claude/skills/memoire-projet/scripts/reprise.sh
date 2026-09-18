#!/bin/zsh
# Usage: reprise.sh <slug-projet> [N]   -> en-tête REPRISE + consignes + N dernières entrées (défaut 12)
MEM_DIR="${MEM_DIR:-$HOME/.claude/projects/-Volumes-NO-NAME-caude/memory}"
f="$MEM_DIR/projet-$1.md"; n="${2:-12}"
[[ -f "$f" ]] || { echo "introuvable : $f" >&2; exit 1; }
echo "== description"; grep -m1 '^description:' "$f" | cut -c1-300
echo "== REPRISE (en-tête du fichier)"; awk '/^\*\*REPRISE\*\*/{on=1} on{print substr($0,1,400); n++} n>12{exit}' "$f"
echo "== questions sans réponse"; grep -n -i 'question posée' "$f" | tail -3 | cut -c1-300
echo "== $n dernières entrées (le journal est en tête : les plus récentes sont les premières)"; grep '^- ' "$f" | head -"$n" | cut -c1-400
pat=$(echo "$1" | tr -d '-')
echo "== .als du projet (motif « $1 » ou « $pat »)"
ls -t "/Volumes/Seagate Portable Drive/abl proj/1 Project/"*.als 2>/dev/null | grep -iE "$1|$pat" | head -3 | while read -r x; do ls -la "$x" | awk '{print "  ", $6, $7, $8, substr($0, index($0,$9))}'; done
echo "== .als le plus récent, TOUS projets (peut appartenir à un autre morceau)"
ls -t "/Volumes/Seagate Portable Drive/abl proj/1 Project/"*.als 2>/dev/null | head -1 | xargs -I{} ls -la {} | awk '{print "  ", $6, $7, $8, substr($0, index($0,$9))}'
