#!/usr/bin/env python3
"""Usage: compare_reports.py reference.json candidat.json
Compare deux rapports d'analyze_synth.py à niveau égalisé (RMS) : hauteur, harmoniques (H1–H8), centroïde (octaves), enveloppe (attaque, decay), stéréo, et
propose les écarts prioritaires avec le paramètre candidat. Un faible écart chiffré n'est pas une ressemblance auditive : c'est un guide de réglage."""
import sys, json, math
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 else 2)

A, B = (json.load(open(p)) for p in sys.argv[1:3])
def f0(d):
    ph = [p['frequency_hz'] for p in (d.get('pitch_hints') or []) if p.get('frequency_hz')]
    return sorted(ph)[len(ph) // 2] if ph else None
def harm(d, f):
    h = {}
    for p in (d.get('spectrum') or {}).get('strongest_peaks') or []:
        n = p['bin_frequency_hz'] / f; k = round(n)
        if k >= 1 and abs(n - k) < 0.12: h.setdefault(k, p['relative_power_db'])
    return h
def env(d):
    e = [(x['time_relative_s'], x['rms_dbfs']) for x in (d.get('envelope_10ms') or []) if x['rms_dbfs'] is not None]
    if not e: return None
    mx = max(r for _, r in e); i = next(i for i, (_, r) in enumerate(e) if r >= mx - 1.0)
    tail = [r for _, r in e[i:] if r > mx - 30]; sus = sorted(tail)[len(tail) // 2]
    j = next((k for k in range(i, len(e)) if e[k][1] <= sus + 1.0), i)
    return {'att': e[i][0] - e[0][0], 'dec': e[j][0] - e[i][0], 'sus': mx - sus}
ecarts = []
fa, fb = f0(A), f0(B)
if fa and fb:
    c = 1200 * math.log2(fb / fa); ecarts.append((abs(c) / 25, 'Hauteur : %+.0f cents → %s' % (c, 'accordage/octave' if abs(c) > 15 else 'ok')))
ca, cb = [(d.get('spectrum') or {}).get('centroid_hz') for d in (A, B)]
if ca and cb:
    o = math.log2(cb / ca); ecarts.append((abs(o) * 2, 'Centroïde : %+.2f octave → %s' % (o, 'cutoff / brillance de la source (plus sombre)' if o < -0.15 else 'cutoff / brillance (plus brillant)' if o > 0.15 else 'ok')))
if fa and fb:
    ha, hb = harm(A, fa), harm(B, fb); diffs = []
    for k in range(2, 9):
        if k in ha and k in hb: diffs.append((k, hb[k] - ha[k]))
    if diffs:
        worst = max(diffs, key=lambda x: abs(x[1]))
        ecarts.append((abs(worst[1]) / 4, 'Harmoniques : ' + ' '.join('H%d %+.0f' % (k, v) for k, v in diffs) + ' dB → %s' % ("forme d'onde / drive / pente du filtre (H%d)" % worst[0] if abs(worst[1]) > 4 else 'ok')))
ea, eb = env(A), env(B)
if ea and eb:
    da = (eb['att'] - ea['att']) * 1000; dd = (eb['dec'] - ea['dec']) * 1000; ds = eb['sus'] - ea['sus']
    ecarts.append((abs(da) / 15, 'Attaque : %+.0f ms → %s' % (da, 'enveloppe ampli/filtre (attack)' if abs(da) > 10 else 'ok')))
    ecarts.append((abs(dd) / 60, 'Decay : %+.0f ms → %s' % (dd, 'enveloppe (decay) ou compression' if abs(dd) > 40 else 'ok')))
    ecarts.append((abs(ds) / 3, 'Sustain : %+.1f dB → %s' % (ds, 'sustain / compression / release trop courte' if abs(ds) > 2 else 'ok')))
sa, sb = [(d.get('stereo') or {}).get('side_to_mid_db') for d in (A, B)]
if sa is not None and sb is not None:
    ecarts.append((abs(sb - sa) / 5, 'Largeur (side/mid) : %+.1f dB → %s' % (sb - sa, 'unisson / chorus / largeur' if abs(sb - sa) > 4 else 'ok')))
ra, rb = [(d.get('channels') or [{}])[0].get('rms_dbfs') for d in (A, B)]
if ra is not None and rb is not None: print('Niveau : candidat %+.1f dB RMS par rapport à la référence (comparer après compensation)' % (rb - ra))
for score, txt in sorted(ecarts, key=lambda x: -x[0]): print(('!! ' if score >= 1 else '   ') + txt)
print('Ordre de correction : hauteur → attaque/bruit → tenue (cutoff, forme) → mouvement/stéréo → effets/queue. Un seul changement par cycle.')
