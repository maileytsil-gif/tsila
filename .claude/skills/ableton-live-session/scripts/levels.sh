#!/bin/zsh
# Usage: levels.sh <mesure_depart> [nom_piste ...]   -> crêtes (dB) échantillonnées sur ~5 s, master inclus
bar="$1"; shift; pistes="$*"
cd "/Volumes/NO NAME/caude/lom-bridge" || exit 1
py(){ python3 lom.py --timeout 25 py "$1" 2>&1 | tail -1; }
py "song.stop_playing(); song.start_playing(); 'go'" >/dev/null
py "song.current_song_time=($bar-1)*4.0; 'jump'" >/dev/null; sleep 0.8
for k in $(seq 1 20); do
  py "import math
# ATTENTION : output_meter = post-devices ET post-fader (mesuré 15/09/2026), échelle du fader (0,85 = 0 dB, 0,5 = −14 dB) : convertir via volume.str_for_value. Les 20·log10 ci-dessous ne valent qu'en RELATIF
# (avant/après, piste contre piste), jamais en dBFS absolus. Chiffre fiable = export + analyze_wav.py.
f=lambda t:(lambda v: round(20*math.log10(v),1) if v>0 else -99)(max(t.output_meter_left,t.output_meter_right))
by={t.name:t for t in song.tracks}
noms='$pistes'.split() if '$pistes' else []
result=[(n, f(by[n])) for n in noms if n in by] + [('MASTER(pre-devices)', f(song.master_track)), ('mes', round(song.current_song_time/4+1,1))]"
  sleep 0.25
done | sort -u | tail -6
py "song.stop_playing(); 'stop'" >/dev/null; sleep 0.4; py "song.current_song_time=0.0; int(song.is_playing)" >/dev/null
