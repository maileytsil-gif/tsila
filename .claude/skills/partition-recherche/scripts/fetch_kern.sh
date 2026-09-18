#!/bin/zsh
# Usage: fetch_kern.sh <dépôt craigsapp> <fichier.krn> [destination]   ex: fetch_kern.sh beethoven-piano-sonatas sonata23-1.krn
repo="$1"; f="$2"; dest="${3:-./$2}"
for br in master main; do
  code=$(curl -sL -o "$dest" -w '%{http_code}' "https://raw.githubusercontent.com/craigsapp/$repo/$br/kern/$f")
  if [ "$code" = "200" ] && grep -q '\*\*kern' "$dest"; then echo "OK $dest ($(grep -m1 '^!!!OTL' "$dest" | cut -c8-) ; $(grep -m1 '^\*M' "$dest" | tr -d '*'))"; exit 0; fi
done
echo "introuvable : $repo/$f"; rm -f "$dest"; exit 1
