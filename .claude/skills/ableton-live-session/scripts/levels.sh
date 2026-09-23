#!/bin/zsh
# Usage: levels.sh <mesure_depart> [nom_piste ...]   -> crêtes échantillonnées sur 5 s à partir de la mesure, master inclus
# Depuis LOM Bridge 0.6.0 : une seule commande typée (/meters) ; le transport est lancé puis arrêté et le curseur restauré par le bridge.
# ATTENTION : output_meter = post-devices ET post-fader pour une piste (mesuré 15/09/2026), pré-devices du master pour le master ;
# la colonne dB vient de la courbe du fader (0,85 = 0 dB, 0,5 = −14 dB), fiable ±1 dB entre −7 et −16 dB : valeurs RELATIVES seulement
# (avant/après, piste contre piste). Chiffre fiable en absolu = export + analyze_wav.py.
bar="$1"; shift
cd "${LOM_BRIDGE_DIR:-/Volumes/NO NAME/caude/lom-bridge}" || exit 1
python3 lom.py --timeout 25 meters "${bar}|1" 5 "$@"
