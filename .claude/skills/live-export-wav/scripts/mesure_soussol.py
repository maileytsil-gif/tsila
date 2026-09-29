#!/usr/bin/env python3
"""Mesure d'un export de « Sous-Sol » (128 BPM, 4/4, 160 mesures = 300,000 s).

Usage :
  mesure_soussol.py fichier.wav [--bpm 128]
      durée, crête sample, LUFS intégré (BS.1770-4), true peak x4, LRA (EBU 3342), PLR,
      LUFS court terme (3 s) max et moyen par section.
  mesure_soussol.py --kicksub kick.wav sub.wav [--band 30-120] [--lag 15]
      corrélation kick/sub dans la bande 30–120 Hz et énergie sous / au-dessus de 60 Hz
      (délègue à kick-bass-equilibre/scripts/kick_bass_check.py, puis ajoute les énergies en dB).

Code repris de ~/.claude/skills/live-export-wav/scripts/lufs.py (K-weighting RBJ/pyloudnorm,
blocs 400 ms / 3 s, pas 100 ms, portes −70 / −10 / −20, LRA 10–95 %, TP 4x) et analyze_wav.py.
scipy est utilisé s'il est présent ; sinon repli numpy seul (filtre K appliqué dans le domaine
fréquentiel, suréchantillonnage x4 par FFT par blocs) — écarts < 0,05 LU / 0,05 dB en pratique.
Ne touche ni à Live ni au LOM Bridge.
"""
import sys, os, math, wave, runpy
import numpy as np

SECTIONS = [("Intro A", 1), ("Intro B", 17), ("Build 1", 33), ("Drop 1", 49), ("Break", 81),
            ("Build 2", 97), ("Drop 2", 113), ("Outro", 145)]
FIN = 161
SKILLS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # dossier des skills (installé ou dépôt)

try:
    from scipy.signal import lfilter, resample_poly
    HAVE_SCIPY = True
except Exception:
    HAVE_SCIPY = False


def opt(args, k, d):
    return args[args.index(k) + 1] if k in args else d


# ---------- lecture (repris de lufs.py : 24 bits décodés à la main, crêtes exactes) ----------
def read_wav(path):
    try:
        import soundfile as sf
        x, sr = sf.read(path, always_2d=True, dtype="float64")
        return x, sr
    except Exception:
        pass
    w = wave.open(path); sr = w.getframerate(); ch = w.getnchannels(); sw = w.getsampwidth(); n = w.getnframes()
    raw = w.readframes(n); w.close()
    if sw == 3:
        a = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 3)
        x = (a[:, 0].astype(np.int32) | (a[:, 1].astype(np.int32) << 8)
             | (a[:, 2].astype(np.int8).astype(np.int32) << 16)).astype(np.float64) / 2**23
    else:
        x = np.frombuffer(raw, dtype="<i%d" % sw).astype(np.float64) / 2**(8 * sw - 1)
    return x.reshape(-1, ch), sr


# ---------- K-weighting (coefficients identiques à lufs.py) ----------
def shelf(fs):
    f0, G, Q = 1681.974450955533, 3.999843853973347, 0.7071752369554196
    K = np.tan(np.pi * f0 / fs); Vh = 10**(G / 20); Vb = Vh**0.499666774155
    a0 = 1 + K / Q + K * K
    b = [(Vh + Vb * K / Q + K * K) / a0, 2 * (K * K - Vh) / a0, (Vh - Vb * K / Q + K * K) / a0]
    a = [1, 2 * (K * K - 1) / a0, (1 - K / Q + K * K) / a0]
    return b, a


def hp(fs):
    f0, Q = 38.13547087602444, 0.5003270373238773
    K = np.tan(np.pi * f0 / fs)
    a0 = 1 + K / Q + K * K
    b = [1, -2, 1]; a = [1, 2 * (K * K - 1) / a0, (1 - K / Q + K * K) / a0]
    return [bb / a0 for bb in b], a


def kweight(x, sr):
    if HAVE_SCIPY:
        y = x.copy()
        for b, a in (shelf(sr), hp(sr)):
            y = lfilter(b, a, y, axis=0)
        return y
    # repli numpy : réponse exacte des deux biquads appliquée par FFT (1 s de zéros pour la queue)
    n = len(x) + sr
    N = 1 << (n - 1).bit_length()
    z = np.exp(-1j * np.pi * np.arange(N // 2 + 1) / (N // 2))
    H = np.ones(N // 2 + 1, dtype=complex)
    for b, a in (shelf(sr), hp(sr)):
        H *= (b[0] + b[1] * z + b[2] * z**2) / (a[0] + a[1] * z + a[2] * z**2)
    y = np.empty_like(x)
    for c in range(x.shape[1]):
        y[:, c] = np.fft.irfft(np.fft.rfft(x[:, c], N) * H, N)[:len(x)]
    return y


def true_peak_x4(x):
    if HAVE_SCIPY:
        return max(np.abs(resample_poly(x[:, c], 4, 1)).max() for c in range(x.shape[1]))
    # repli numpy : suréchantillonnage x4 par FFT, blocs de 2^18 avec 2 048 échantillons de recouvrement
    B, O = 1 << 18, 2048
    tp = 0.0
    for c in range(x.shape[1]):
        s = x[:, c]
        for st in range(0, len(s), B):
            lo = max(0, st - O); hi = min(len(s), st + B + O)
            seg = s[lo:hi]; n = len(seg)
            S = np.fft.rfft(seg)
            U = np.zeros(2 * n + 1, dtype=complex)  # 4n/2+1
            U[:len(S)] = S
            if n % 2 == 0:
                U[len(S) - 1] *= 0.5
            up = np.fft.irfft(U, 4 * n) * 4
            a = (st - lo) * 4; b = a + (min(st + B, len(s)) - st) * 4
            tp = max(tp, np.abs(up[a:b]).max())
    return tp


def windows(y, sr, dur):
    blk = int(dur * sr); hop = int(0.1 * sr)
    nb = (len(y) - blk) // hop + 1
    idx = np.arange(nb) * hop
    pw = np.zeros(nb)
    for c in range(y.shape[1]):
        cs = np.concatenate([[0], np.cumsum(y[:, c]**2)])
        pw += (cs[idx + blk] - cs[idx]) / blk
    return idx, pw, -0.691 + 10 * np.log10(pw + 1e-20)


def mesure(path, bpm):
    x, sr = read_wav(path)
    n = len(x); dur = n / sr
    y = kweight(x, sr)
    idx, pw, lk = windows(y, sr, 0.4)
    m = lk > -70
    g = -0.691 + 10 * np.log10(pw[m].mean()) - 10
    I = -0.691 + 10 * np.log10(pw[m & (lk > g)].mean())
    idx3, pw3, st = windows(y, sr, 3.0)
    m3 = st > -70; g3 = -0.691 + 10 * np.log10(pw3[m3].mean()) - 20; v = st[m3 & (st > g3)]
    lra = np.percentile(v, 95) - np.percentile(v, 10) if len(v) else 0.0
    tp = 20 * np.log10(true_peak_x4(x))
    peak = 20 * np.log10(np.abs(x).max())
    bar = 4 * 60 / bpm
    print("%s" % os.path.basename(path))
    print("durée %.3f s (attendu %.3f, écart %+.3f) | %d Hz, %d canaux | moteur %s"
          % (dur, (FIN - 1) * bar, dur - (FIN - 1) * bar, sr, x.shape[1], "scipy" if HAVE_SCIPY else "numpy seul"))
    print("intégré %.1f LUFS (%.2f) | true peak x4 %.2f dBTP | crête sample %.2f dBFS | LRA %.1f LU | PLR %.1f | ST max %.1f"
          % (I, I, tp, peak, lra, tp - I, st.max()))
    print("%-8s %-6s %-15s %8s %8s %8s" % ("section", "mes.", "temps", "ST max", "ST moy", "crête"))
    bounds = SECTIONS + [("FIN", FIN)]
    for i, (nm, b0) in enumerate(SECTIONS):
        t0 = (b0 - 1) * bar; t1 = min((bounds[i + 1][1] - 1) * bar, dur)
        sel = (idx3 / sr >= t0) & (idx3 / sr + 3 <= t1 + 1e-9)
        seg = x[int(t0 * sr):int(t1 * sr)]
        print("%-8s %-6s %6.1f-%6.1f s %8.1f %8.1f %8.2f" % (
            nm, "%d-%d" % (b0, bounds[i + 1][1] - 1), t0, t1,
            st[sel].max() if sel.any() else -99, st[sel].mean() if sel.any() else -99,
            20 * np.log10(np.abs(seg).max() + 1e-12)))


def kicksub(args):
    kp, sp = args[0], args[1]
    script = os.path.join(SKILLS, "kick-bass-equilibre/scripts/kick_bass_check.py")
    old = sys.argv
    sys.argv = [script] + args
    try:
        runpy.run_path(script, run_name="__main__")
    finally:
        sys.argv = old
    lo, hi = [float(v) for v in opt(args, "--band", "30-120").split("-")]
    print("Énergie sous / au-dessus de 60 Hz (dans %g–%g Hz, puis 60–400 Hz) :" % (lo, hi))
    for nm, p in (("KICK", kp), ("SUB", sp)):
        x, sr = read_wav(p); s = x.mean(axis=1)
        X = np.abs(np.fft.rfft(s))**2; f = np.fft.rfftfreq(len(s), 1 / sr)
        e_lo = X[(f >= lo) & (f < 60)].sum(); e_hi = X[(f >= 60) & (f <= hi)].sum(); e_hi2 = X[(f >= 60) & (f <= 400)].sum()
        db = lambda e: 10 * math.log10(max(e, 1e-30))
        print("  %-4s : %g–60 Hz vs 60–%g Hz = %+.1f dB (%.0f %% sous 60) | vs 60–400 Hz = %+.1f dB"
              % (nm, lo, hi, db(e_lo) - db(e_hi), 100 * e_lo / max(e_lo + e_hi, 1e-30), db(e_lo) - db(e_hi2)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); raise SystemExit(0 if a else 2)
    if a[0] == "--kicksub":
        if len(a) < 3: raise SystemExit("usage : --kicksub kick.wav sub.wav")
        kicksub(a[1:])
    else:
        if not os.path.exists(a[0]): raise SystemExit("fichier introuvable : " + a[0])
        mesure(a[0], float(opt(a, "--bpm", 128)))
