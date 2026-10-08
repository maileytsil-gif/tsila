#!/bin/zsh
# Usage: mutopia.sh chercher <compositeur|code> [motif]     -> liste des fichiers ftp/... (ly, mid, pdf)
#        mutopia.sh prendre <chemin ftp/...> [dossier_dest]  -> télécharge (défaut ~/Desktop/1 Project/Partitions)
UA="Mozilla/5.0"; base="https://www.mutopiaproject.org"
case "$1" in
  chercher)
    q="$2"; motif="${3:-}"
    # code Mutopia = Nom + initiale(s) ; on essaie le nom tel quel puis les codes courants
    for code in "$q" "${q}E" "${q}F" "${q}C" "${q}JS" "${q}Lv" "${q}WA" "${q}FF" "${q}R" "${q}G"; do
      html=$(curl -sL -A "$UA" "$base/cgibin/make-table.cgi?Composer=$code"); n=$(echo "$html" | grep -c 'ftp/')
      if [ "$n" -gt 0 ]; then echo "code $code : $n liens"; echo "$html" | grep -o 'ftp/[^"]*\.\(ly\|mid\|pdf\)' | sort -u | grep -i -- "$motif" | head -60; exit 0; fi
    done; echo "aucun résultat pour $q (voir https://www.mutopiaproject.org/browse.html)"; exit 1;;
  prendre)
    p="$2"; d="${3:-$HOME/Desktop/1 Project/Partitions}"; mkdir -p "$d"; f="$d/$(basename "$p")"
    code=$(curl -sL -A "$UA" -o "$f" -w '%{http_code}' "$base/$p"); [ "$code" = "200" ] && { ls -l "$f"; file "$f"; } || { echo "échec $code"; rm -f "$f"; exit 1; };;
  *) echo "usage: mutopia.sh chercher|prendre ..."; exit 2;;
esac
