#!/usr/bin/env python3
"""grave_kick.py kick.wav [--sub sub.wav] [--mes 49 --n 8] [--ref ancien_kick.wav] [--ref-sub ancien_sub.wav] [--ref-mes M]
Analyse du grave d'un kick (coup moyen, un kick par temps) — fichiers WAV locaux uniquement.
Filtres : Butterworth ordre 4 appliqués en magnitude dans le domaine FFT (phase nulle, pas de retard)."""
import sys, argparse, wave, numpy as np

BPM = 128.0; SPB = 60.0 / BPM
BANDS = [(30,45),(45,60),(60,80),(80,100),(100,130),(130,200)]
NOTES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def read24(p):
    w = wave.open(p); n = w.getnframes(); ch = w.getnchannels(); sr = w.getframerate(); sw = w.getsampwidth()
    b = w.readframes(n)
    if sw == 3:
        a = np.frombuffer(b, dtype=np.uint8).reshape(-1,3)
        x = (a[:,0].astype(np.int32) | (a[:,1].astype(np.int32)<<8) | (a[:,2].astype(np.int32)<<16))
        x = np.where(x >= 1<<23, x-(1<<24), x) / float(1<<23)
    elif sw == 2:
        x = np.frombuffer(b, dtype='<i2') / 32768.0
    else:
        raise SystemExit('format non géré (%d octets)' % sw)
    return x.reshape(-1,ch).mean(1), sr   # mono (grave = mono)

db  = lambda v: 20*np.log10(max(float(v),1e-12))
dbp = lambda p: 10*np.log10(max(float(p),1e-24))
def note(f):
    if not f or f <= 0: return '—'
    m = 69 + 12*np.log2(f/440.0); r = int(round(m))
    return '%s%d%+.0fc' % (NOTES[r%12], r//12-2, (m-r)*100)   # C3 = 60 (convention Live)

class Band:
    """filtrage passe-bande zéro-phase par FFT, mis en cache par segment"""
    def __init__(self, x, sr):
        self.sr = sr; self.N = 1 << int(np.ceil(np.log2(len(x)+sr)))
        self.X = np.fft.rfft(x, self.N); self.f = np.fft.rfftfreq(self.N, 1/sr); self.n = len(x)
    def __call__(self, lo, hi, order=4):
        f = np.maximum(self.f, 1e-6)
        H = 1/np.sqrt(1+(lo/f)**(2*order)) / np.sqrt(1+(f/hi)**(2*order))
        return np.fft.irfft(self.X*H, self.N)[:self.n]

def load_segment(path, mes, n):
    x, sr = read24(path)
    t0 = (mes-1)*4*SPB; t1 = t0 + n*4*SPB
    pad = int(0.5*sr)
    a = int(t0*sr); b = min(int(t1*sr), len(x))
    if a >= len(x): raise SystemExit('%s : plage hors fichier' % path)
    s0 = max(a-pad,0); seg = x[s0:min(b+pad,len(x))]
    return seg, sr, a-s0, b-s0   # segment avec marges, index début/fin de plage

def onsets(seg, sr, i0, i1):
    """attaque par temps : 1er échantillon > 20 % du max local, fenêtre temps −30/+60 ms"""
    k = max(int(sr*0.001),1); env = np.convolve(np.abs(seg), np.ones(k)/k, 'same')
    gmax = env[i0:i1].max(); out = []
    nb = int(round((i1-i0)/sr/SPB))
    for i in range(nb):
        g = i0 + int(round(i*SPB*sr)); a = max(g-int(0.03*sr),0); b = g+int(0.06*sr)
        w = env[a:b]
        if len(w) == 0 or w.max() < gmax*10**(-20/20): continue   # pas de kick sur ce temps
        out.append(a + int(np.argmax(w > 0.2*w.max())))
    return np.array(out)

def slices_rms(sig, ons, sr, t_from, t_to, step=0.01):
    """RMS (moyenne des puissances sur les coups) par tranches, en dBFS"""
    res = []
    for t in np.arange(t_from, t_to-1e-9, step):
        p = []
        for o in ons:
            a = o+int(t*sr); b = o+int((t+step)*sr)
            if a >= 0 and b <= len(sig): p.append(np.mean(sig[a:b]**2))
        res.append((t, dbp(np.mean(p)) if p else np.nan))
    return res

def win_rms(sig, ons, sr, t_from, t_to):
    p = [np.mean(sig[o+int(t_from*sr):o+int(t_to*sr)]**2) for o in ons if o+int(t_to*sr) <= len(sig)]
    return dbp(np.mean(p))

def zc_pitch(h, sr, a_ms, b_ms):
    zc = np.where(np.diff(np.signbit(h)))[0]
    z = zc[(zc >= a_ms*sr/1000) & (zc < b_ms*sr/1000)]
    if len(z) < 3: return None
    return sr/(2*np.mean(np.diff(z)))

def analyse(path, mes, n, sub=None, label=''):
    seg, sr, i0, i1 = load_segment(path, mes, n)
    if np.sqrt(np.mean(seg[i0:i1]**2)) < 1e-5:
        raise SystemExit('%s : plage mesures %d–%d silencieuse (< -100 dBFS) — choisir une autre plage (--mes / --ref-mes)' % (path, mes, mes+n))
    ons = onsets(seg, sr, i0, i1)
    L = int(0.4*sr)
    ons = ons[ons+L <= len(seg)]
    R = {'label': label, 'path': path, 'nhits': len(ons)}
    bf = Band(seg, sr)
    # coup moyen cohérent (kick identique d'un temps à l'autre)
    hits = np.array([seg[o:o+L] for o in ons]); h = hits.mean(0)
    R['peak'] = db(np.abs(h).max())
    # 1. énergie par bande : dB relatif (spectre du coup 0–400 ms, rapporté au total 20 Hz–20 kHz) + dBFS RMS 0–150 ms
    S = (np.abs(np.fft.rfft(hits*np.hanning(L), axis=1))**2).mean(0); f = np.fft.rfftfreq(L, 1/sr)
    tot = S[(f>=20)&(f<20000)].sum()
    R['bands'] = []
    for lo, hi in BANDS:
        rel = 10*np.log10(S[(f>=lo)&(f<hi)].sum()/tot)
        R['bands'].append((lo, hi, rel, win_rms(bf(lo,hi), ons, sr, 0, 0.15)))
    R['full150'] = win_rms(seg, ons, sr, 0, 0.15)
    # 2. courbes d'amplitude 30–60 et 60–100 Hz, 10 ms, 0–250 ms
    R['c1'] = slices_rms(bf(30,60), ons, sr, 0, 0.25); R['c2'] = slices_rms(bf(60,100), ons, sr, 0, 0.25)
    # 3. hauteur
    R['pitch'] = [(a,b,zc_pitch(h, sr, a, b)) for a,b in [(0,10),(10,20),(20,40),(40,80),(80,150)]]
    tail = h[int(0.08*sr):int(0.35*sr)]
    Nf = 1<<18; Sp = np.abs(np.fft.rfft(tail*np.hanning(len(tail)), Nf)); ff = np.fft.rfftfreq(Nf, 1/sr)
    m = (ff>25)&(ff<200); R['rest_fft'] = ff[m][np.argmax(Sp[m])]
    R['rest_zc'] = zc_pitch(h, sr, 150, 300)
    # 4. grave ressenti
    R['felt'] = win_rms(bf(35,90), ons, sr, 0, 0.2)
    # 5. somme kick + sub
    if sub:
        s2, sr2, j0, j1 = load_segment(sub, mes, n)
        m_ = min(len(seg), len(s2)); tot_ = seg[:m_] + s2[:m_]
        bs = Band(tot_, sr); bk = bf(30,100)[:m_]; bsub = Band(s2[:m_], sr)(30,100); bsum = bs(30,100)
        onz = ons[(ons-int(0.05*sr) >= 0) & (ons+int(0.25*sr) <= m_)]
        R['sum'] = list(zip(slices_rms(bsum, onz, sr, -0.05, 0.25), slices_rms(bk, onz, sr, -0.05, 0.25),
                            slices_rms(bsub, onz, sr, -0.05, 0.25)))
        # plateau du sub entre les coups : sub seul sur la fin du temps (+300..+450 ms)
        R['sub_plateau'] = win_rms(bsub, onz[onz+int(0.45*sr) <= m_], sr, 0.30, 0.45)
        R['sum_plateau'] = win_rms(bsum, onz[onz+int(0.45*sr) <= m_], sr, 0.30, 0.45)
        R['felt_sum'] = win_rms(bs(35,90), onz, sr, 0, 0.2)
        R['felt_sum_beat'] = win_rms(bs(35,90), onz[onz+int(SPB*sr) <= m_], sr, 0, SPB)
        R['corr'] = float(np.sum(bk*bsub)/np.sqrt(np.sum(bk**2)*np.sum(bsub**2)+1e-24))
        # trou : niveau de la somme avant le coup (−50..−20 ms, sub non ducké) = référence ;
        # trou = tranches 0..+250 ms sous référence −3 dB ; profondeur = référence − minimum
        vals = np.array([x[0][1] for x in R['sum']]); ts = np.array([x[0][0] for x in R['sum']])
        kv = np.array([x[1][1] for x in R['sum']]); sv = np.array([x[2][1] for x in R['sum']])
        pre = ts < -0.015; post = ts >= -0.001
        R['pre'] = dbp(np.mean(10**(vals[pre]/10)))
        imin = np.argmin(np.where(post, vals, 999)); R['hole_min'] = (ts[imin], vals[imin])
        ipk = np.argmax(np.where(post, vals, -999)); R['sum_peak'] = (ts[ipk], vals[ipk])
        below = post & (vals < R['pre']-3)
        R['hole_ms'] = int(below.sum()*10)
        R['hole_span'] = (ts[below].min()*1000, ts[below].max()*1000+10) if below.any() else None
        ik = np.argmax(np.where(post, kv, -999))
        R['kick_vs_sub'] = (ts[ik], kv[ik], sv[ik])   # au max du kick : kick vs sub ducké
    return R

def show(R):
    print('\n=== %s : %s' % (R['label'], R['path'].split('/')[-1]))
    print('coups analysés : %d   crête coup moyen : %.1f dBFS   RMS large bande 0–150 ms : %.1f dBFS' % (R['nhits'], R['peak'], R['full150']))
    print('1. Bandes (dB rel. = part du spectre 0–400 ms ; dBFS = RMS 0–150 ms)')
    for lo, hi, rel, a in R['bands']: print('   %3d–%3d Hz : %6.1f dB rel.  %6.1f dBFS' % (lo, hi, rel, a))
    print('2. Amplitude dBFS par 10 ms      30–60 Hz   60–100 Hz')
    for (t, a), (_, b) in zip(R['c1'], R['c2']):
        print('   %3d–%3d ms                  %6.1f     %6.1f  %s' % (t*1000, t*1000+10, a, b, '#'*max(0,int((a+60)/2))))
    print('3. Hauteur instantanée')
    for a, b, p in R['pitch']: print('   %3d–%3d ms : %s' % (a, b, ('%.0f Hz (%s)' % (p, note(p))) if p else '—'))
    print('   repos : pic FFT 80–350 ms %.1f Hz (%s) ; passages à zéro 150–300 ms %s' % (
        R['rest_fft'], note(R['rest_fft']), ('%.1f Hz' % R['rest_zc']) if R['rest_zc'] else '—'))
    print('4. GRAVE RESSENTI (RMS 35–90 Hz, 0–200 ms) : %.1f dBFS' % R['felt'])
    if 'sum' in R:
        print('5. Somme kick+sub 30–100 Hz (dBFS/10 ms)   somme   kick    sub')
        for (t, s), (_, k), (_, u) in R['sum']:
            print('   %+4d ms                             %6.1f  %6.1f  %6.1f' % (t*1000, s, k, u))
        print('   plateau fin de temps (+300..+450 ms) : somme %.1f dBFS, sub %.1f dBFS' % (R['sum_plateau'], R['sub_plateau']))
        print('   avant coup (−50..−20 ms) somme %.1f dBFS ; pic %.1f à %+d ms ; creux %.1f à %+d ms → profondeur %.1f dB sous l\'avant-coup' % (
            R['pre'], R['sum_peak'][1], R['sum_peak'][0]*1000, R['hole_min'][1], R['hole_min'][0]*1000, R['pre']-R['hole_min'][1]))
        print('   TROU (somme < avant-coup −3 dB) : %d ms %s' % (R['hole_ms'], ('(tranches %+d→%+d ms)' % R['hole_span']) if R['hole_span'] else ''))
        t, k, u = R['kick_vs_sub']
        print('   au max du kick (%+d ms) : kick %.1f dBFS vs sub ducké %.1f dBFS → kick %+.1f dB par rapport au sub' % (t*1000, k, u, k-u))
        print('   grave ressenti somme 35–90 Hz : 0–200 ms %.1f dBFS ; temps entier %.1f dBFS ; corrélation kick/sub 30–100 Hz %+.2f' % (
            R['felt_sum'], R['felt_sum_beat'], R['corr']))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('kick'); ap.add_argument('--sub'); ap.add_argument('--mes', type=int, default=49)
    ap.add_argument('--n', type=int, default=8); ap.add_argument('--ref'); ap.add_argument('--ref-sub')
    ap.add_argument('--ref-mes', type=int, help='1re mesure pour la référence (défaut = --mes)')
    a = ap.parse_args()
    A = analyse(a.kick, a.mes, a.n, a.sub, 'ACTUEL (mes. %d)' % a.mes); show(A)
    if a.ref:
        B = analyse(a.ref, a.ref_mes or a.mes, a.n, a.ref_sub, 'RÉFÉRENCE (mes. %d)' % (a.ref_mes or a.mes)); show(B)
        print('\n=== ÉCARTS actuel − référence (dB)')
        for (lo, hi, r1, d1), (_, _, r2, d2) in zip(A['bands'], B['bands']):
            print('   %3d–%3d Hz : rel. %+5.1f   dBFS %+5.1f' % (lo, hi, r1-r2, d1-d2))
        print('   crête coup %+.1f ; RMS 0–150 ms %+.1f ; GRAVE RESSENTI %+.1f dB' % (A['peak']-B['peak'], A['full150']-B['full150'], A['felt']-B['felt']))
        print('   repos %.1f Hz vs %.1f Hz' % (A['rest_fft'], B['rest_fft']))
        print('   30–60 Hz par 10 ms (act − réf) : ' + ' '.join('%+.0f' % (x[1]-y[1]) for x, y in zip(A['c1'], B['c1'])))
        print('   60–100 Hz par 10 ms (act − réf) : ' + ' '.join('%+.0f' % (x[1]-y[1]) for x, y in zip(A['c2'], B['c2'])))
        if 'sum' in A and 'sum' in B:
            print('   somme 35–90 Hz 0–200 ms %+.1f ; temps entier %+.1f ; trou %d vs %d ms' % (
                A['felt_sum']-B['felt_sum'], A['felt_sum_beat']-B['felt_sum_beat'], A['hole_ms'], B['hole_ms']))
            print('   kick − sub au max du kick : %+.1f vs %+.1f dB' % (A['kick_vs_sub'][1]-A['kick_vs_sub'][2], B['kick_vs_sub'][1]-B['kick_vs_sub'][2]))

if __name__ == '__main__':
    main()
