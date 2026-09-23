#!/bin/zsh
# Usage: apply_verify.sh spec.json "<piste>" "<device>" "<param>" <tA> <tB>   -> dry, écriture tout ou rien + relecture du bridge, relecture 1 point/mesure
spec="$1"; piste="$2"; dev="$3"; par="$4"; ta="$5"; tb="$6"
cd "${LOM_BRIDGE_DIR:-/Volumes/NO NAME/caude/lom-bridge}" || exit 1
[ "$(python3 lom.py transport 2>&1 | tail -1 | awk '{print $2}')" = "0" ] || { echo "TRANSPORT EN LECTURE : rien écrit"; exit 2; }
echo "=== DRY ==="; python3 lom.py --timeout 120 apply "$spec" --dry 2>&1 | grep -E "^(DRY|ERR)|ERREUR|relecture|clips:|avertissement" | cut -c1-160
echo "=== ECRITURE ==="; python3 lom.py --timeout 280 apply "$spec" 2>&1 | grep -E "^(OK|ERR)|relecture|avertissement|\[E_" | cut -c1-160
python3 lom.py wait >/dev/null 2>&1
r=$(python3 lom.py param "$piste" "$dev" "$par" 2>&1 | tail -1 | awk '{print $1}')
echo "=== RELECTURE ($r) ==="; python3 lom.py --timeout 120 read "$piste" "$r" "$ta" "$tb" 0.25 2>&1 | awk '$1 ~ /\|1$/ {printf "%s=%s%s ", $1, $4, $5} END{print ""}'
echo "=== JOURNAL ==="; python3 lom.py journal 1 2>&1 | head -1 | cut -c1-200
