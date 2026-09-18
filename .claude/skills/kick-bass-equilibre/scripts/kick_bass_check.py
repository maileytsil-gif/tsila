#!/usr/bin/env python3
"""Usage: kick_bass_check.py kick.wav sub.wav [--band 30-120] [--lag 15]
Mesure la relation kick/sub dans la bande grave : niveaux, pic spectral, énergie < 60 Hz, corrélation, gain de la somme,
meilleur décalage (ms) et effet d'une inversion de polarité, masquage de l'attaque. Dépendances : numpy, soundfile.
À lire, pas à appliquer tel quel : l'accord se mesure sur la QUEUE du kick (le pic de l'attaque descend en pitch),
et le facteur de crête d'une somme baisse mécaniquement, donc « attaque masquée » est une alerte à vérifier."""
import sys, os, math, numpy as np, soundfile as sf
a = sys.argv[1:]
if len(a) < 2 or a[0] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if a and a[0] in ('-h', '--help') else 2)
kp, sp = a[0], a[1]
for f in (kp, sp):
    if not os.path.exists(f): raise SystemExit('fichier introuvable : ' + f)
def opt(k, d): return a[a.index(k) + 1] if k in a else d
lo, hi = [float(x) for x in opt('--band', '30-120').split('-')]; lagmax = float(opt('--lag', 15))
def load(p):
    x, sr = sf.read(p, always_2d=True); return x.mean(axis=1), sr
k, sr = load(kp); s, sr2 = load(sp); assert sr == sr2, 'fréquences différentes'
n = min(len(k), len(s)); k, s = k[:n], s[:n]
def bandpass(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / sr); X[(f < lo) | (f > hi)] = 0; return np.fft.irfft(X, len(x))
def db(v): return 20 * math.log10(max(v, 1e-9))
def rms(x): return float(np.sqrt(np.mean(x ** 2)))
def peak_hz(x):
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)))); f = np.fft.rfftfreq(len(x), 1 / sr); m = (f >= 20) & (f <= 400); return float(f[m][np.argmax(X[m])])
def below(x, fc=60):
    X = np.abs(np.fft.rfft(x)) ** 2; f = np.fft.rfftfreq(len(x), 1 / sr); tot = X[(f >= 20) & (f <= 400)].sum(); return float(X[(f >= 20) & (f < fc)].sum() / tot) if tot > 0 else 0
kb, sb = bandpass(k, lo, hi), bandpass(s, lo, hi)
print('KICK : crête %.1f dBFS, RMS %.1f, pic %.0f Hz, énergie < 60 Hz : %.0f %% (bande 20–400)' % (db(np.max(np.abs(k))), db(rms(k)), peak_hz(k), 100 * below(k)))
print('SUB  : crête %.1f dBFS, RMS %.1f, pic %.0f Hz, énergie < 60 Hz : %.0f %%' % (db(np.max(np.abs(s))), db(rms(s)), peak_hz(s), 100 * below(s)))
r = float(np.corrcoef(kb, sb)[0, 1]) if rms(kb) > 0 and rms(sb) > 0 else 0.0
somme = rms(kb + sb); attendu = math.sqrt(rms(kb) ** 2 + rms(sb) ** 2)
print('Bande %g–%g Hz : corrélation %.2f | somme %.1f dB vs %.1f dB attendus (indépendants) → %+.1f dB (%s)' % (lo, hi, r, db(somme), db(attendu), db(somme) - db(attendu),
      'annulation partielle' if db(somme) - db(attendu) < -1 else 'renforcement' if db(somme) - db(attendu) > 1 else 'neutre'))
# décalage et polarité
L = int(sr * lagmax / 1000); best = (0, db(somme))
for lag in range(-L, L + 1, max(1, L // 60)):
    sh = np.roll(sb, lag); v = db(rms(kb + sh))
    if v > best[1]: best = (lag, v)
inv = db(rms(kb - sb))
print('Meilleur décalage du sub : %+.1f ms → somme %.1f dB | polarité inversée : %.1f dB' % (best[0] * 1000 / sr, best[1], inv))
reco = []
if inv > db(somme) + 1: reco.append('inverser la polarité de l\'un des deux (+%.1f dB de somme)' % (inv - db(somme)))
if abs(best[0]) > sr * 0.001 and best[1] > db(somme) + 0.8: reco.append('décaler le sub de %+.1f ms (+%.1f dB)' % (best[0] * 1000 / sr, best[1] - db(somme)))
bk, bs = below(k), below(s)
reco.append('rôle observé : %s tient le fondamental (< 60 Hz : kick %.0f %%, sub %.0f %%)' % ('le SUB' if bs >= bk else 'le KICK', 100 * bk, 100 * bs))
pk_seul = db(np.max(np.abs(k))) - db(rms(k)); pk_somme = db(np.max(np.abs(k + s))) - db(rms(k + s))
reco.append('attaque du kick : crête/RMS %.1f dB seul, %.1f dB dans la somme → %s' % (pk_seul, pk_somme, 'masquée par le sub (sidechain plus profond ou sub plus court)' if pk_somme < pk_seul - 3 else 'préservée'))
fk, fs_ = peak_hz(k), peak_hz(s)
if fs_ > 0:
    ratio = fk / fs_; cents = 1200 * math.log2(ratio) % 1200
    reco.append('accord : kick %.0f Hz vs sub %.0f Hz → %.0f cents au-dessus (modulo octave) : %s' % (fk, fs_, cents, 'octave/unisson' if cents < 40 or cents > 1160 else 'quinte' if 660 < cents < 740 else 'à vérifier (battements possibles)'))
print('Recommandations :'); [print('  -', x) for x in reco]
