#!/usr/bin/env python3
"""Usage: analyze_wav.py fichier.wav [duree_attendue_s] [nom=deb-fin ...]  (sections en secondes, ex. intro=0-48)
Imprime durée, crête max dBFS, RMS et facteur de crête, échantillons >= -0,1 dBFS (écrêtage),
sauts d'échantillon brutaux (clics probables), crête par section, niveau des 20 dernières ms.
Ne mesure ni LUFS ni true peak (Insight 2 / WLM Plus pour cela)."""
import sys, os, subprocess, wave, array, math, tempfile
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 else 2)
src = sys.argv[1]
if not os.path.exists(src): raise SystemExit('fichier introuvable : ' + src)
attendu = float(sys.argv[2]) if len(sys.argv) > 2 and '=' not in sys.argv[2] else None
sections = [a for a in sys.argv[2:] if '=' in a]
tmp = os.path.join(tempfile.gettempdir(), 'ana32i.wav')
subprocess.run(['afconvert', '-f', 'WAVE', '-d', 'LEI32', src, tmp], check=True)   # PCM 32 bits entier : crêtes exactes du 24 bits (le module wave refuse le flottant)
w = wave.open(tmp); n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
a = array.array('i'); a.frombytes(w.readframes(n)); w.close()
db = lambda v: 20 * math.log10(max(abs(v), 1) / 2147483648.0)
step = sr * ch
per = [db(max(max(a[s*step:(s+1)*step]), -min(a[s*step:(s+1)*step]))) for s in range(int(n / sr))]
crete = max(per)
rms = db(math.sqrt(sum((float(v) / 2147483648.0) ** 2 for v in a) / len(a)) * 2147483648.0)
saut = 0; seuil = int(0.35 * 2147483648.0)   # variation d'un échantillon à l'autre > ~0,35 FS = clic probable
for i in range(ch, len(a), ch):
    if abs(a[i] - a[i - ch]) > seuil: saut += 1
print('durée %.3f s%s | crête max %.2f dBFS | RMS %.2f dBFS | facteur de crête %.1f dB | échantillons >= -0.1 dBFS : %d | sauts brutaux (clics ?) : %d' % (
    n / sr, ('' if attendu is None else ' (attendu %.3f, écart %+.3f)' % (attendu, n / sr - attendu)),
    crete, rms, crete - rms, sum(1 for v in a if abs(v) >= 2122779000), saut))
for s in sections:
    nom, plage = s.split('='); x, y = [int(float(t)) for t in plage.split('-')]
    print('  %-10s crête %.1f dBFS' % (nom, max(per[x:y])))
tail = a[-int(0.02 * step):]
print('20 dernières ms : %.1f dBFS | 6 dernières s : %s' % (db(max(max(tail), -min(tail))), ' '.join('%.0f' % v for v in per[-6:])))
print('ni LUFS ni true peak ici : les lire dans Insight 2 (bout de Main) ou WLM Plus.')
