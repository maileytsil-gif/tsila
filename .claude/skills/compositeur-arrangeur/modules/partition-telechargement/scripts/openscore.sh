#!/bin/zsh
# Usage: openscore.sh chercher <fragment> [Lieder|StringQuartets]   -> dossiers/fichiers correspondants (GitHub API)
#        openscore.sh prendre <chemin dans le dépôt> [dépôt] [dossier_dest]
repo="${3:-Lieder}"; api="https://api.github.com/repos/OpenScore/$repo/contents"
case "$1" in
  chercher)
    frag="$2"; dirs=$(curl -sL "$api/scores" | python3 -c "import json,sys; print('\n'.join(x['path'] for x in json.load(sys.stdin) if '$frag'.lower() in x['name'].lower()))")
    [ -z "$dirs" ] && { echo "rien pour '$frag' dans OpenScore/$repo"; exit 1; }
    echo "$dirs" | while read -r d; do curl -sL "$api/$d" | python3 -c "import json,sys
for x in json.load(sys.stdin):
    print(x['path'] + ('/' if x['type']=='dir' else ''))"; done;;
  prendre)
    p="$2"; d="${4:-$HOME/Desktop/1 Project/Partitions}"; mkdir -p "$d"; f="$d/$(basename "$p")"
    code=$(curl -sL -o "$f" -w '%{http_code}' "https://raw.githubusercontent.com/OpenScore/${3:-Lieder}/main/$p"); [ "$code" = "200" ] && { ls -l "$f"; file "$f"; } || { echo "échec $code"; rm -f "$f"; exit 1; };;
  *) echo "usage: openscore.sh chercher|prendre ..."; exit 2;;
esac
