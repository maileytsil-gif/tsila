#!/bin/zsh
# Usage: journal.sh <slug-projet> "<texte de l'entrée>"   -> ajoute "- <date> : texte" à memory/projet-<slug>.md
MEM_DIR="${MEM_DIR:-$HOME/.claude/projects/-Volumes-NO-NAME-caude/memory}"
slug="$1"; shift; texte="$*"
f="$MEM_DIR/projet-$slug.md"
[[ -f "$f" ]] || { echo "introuvable : $f" >&2; exit 1; }
d=$(date "+%-d %b %Y %H:%M" | sed 's/Jan/janv./;s/Feb/févr./;s/Mar/mars/;s/Apr/avr./;s/May/mai/;s/Jun/juin/;s/Jul/juil./;s/Aug/août/;s/Sep/sept./;s/Oct/oct./;s/Nov/nov./;s/Dec/déc./')
printf -- "- %s : %s\n" "$d" "$texte" >> "$f" && tail -1 "$f"
