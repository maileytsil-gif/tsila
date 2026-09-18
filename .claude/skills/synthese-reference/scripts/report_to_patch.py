#!/usr/bin/env python3
"""Usage: report_to_patch.py rapport.json [--tempo BPM]
Transforme le rapport JSON d'analyze_synth.py en FICHE DE DÉPART pour un patch (hypothèses chiffrées, à tester) :
enveloppe (attaque/decay/sustain/relâchement estimés sur la RMS 10 ms), profil harmonique (pair/impair, pente) → forme d'onde
candidate, centroïde vs f0 → cutoff de départ, side/mid → unisson/largeur, périodicité → stabilité de hauteur.
Chaque valeur est une hypothèse : la référence est traitée (filtre, compression, reverb) et l'ADSR audio n'est pas l'ADSR du synthé."""
import sys, json, math
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 else 2)

d = json.load(open(sys.argv[1])); tempo = float(sys.argv[sys.argv.index('--tempo') + 1]) if '--tempo' in sys.argv else None
out = []
# --- hauteur
ph = d.get('pitch_hints') or []
f0 = None
if ph:
    fs = [p['frequency_hz'] for p in ph if p.get('frequency_hz')]
    if fs:
        f0 = sorted(fs)[len(fs) // 2]; spread = max(fs) - min(fs)
        out.append('Hauteur : f0 ≈ %.1f Hz (%s Ableton), périodicité médiane %.2f, dispersion %.1f Hz → %s' % (
            f0, ph[0].get('note_ableton_C3_equals_60', '?'), sorted(p['periodicity'] for p in ph)[len(ph) // 2], spread,
            'note stable (pas de vibrato marqué)' if spread < f0 * 0.01 else 'hauteur mobile : vibrato, glide ou notes successives — vérifier'))
# --- enveloppe
env = d.get('envelope_10ms') or []
if env:
    r = [e['rms_dbfs'] for e in env if e['rms_dbfs'] is not None]; t = [e['time_relative_s'] for e in env if e['rms_dbfs'] is not None]
    if r:
        mx = max(r); i_mx = r.index(mx)
        i_a = next((i for i in range(i_mx + 1) if r[i] >= mx - 1.0), i_mx)
        att = t[i_a] - t[0]
        # sustain = médiane après le maximum jusqu'au dernier point > mx-30
        tail = [(ti, ri) for ti, ri in zip(t[i_mx:], r[i_mx:]) if ri > mx - 30]
        sus = sorted(ri for _, ri in tail)[len(tail) // 2] if tail else mx
        i_dec = next((i for i in range(i_mx, len(r)) if r[i] <= sus + 1.0), i_mx); dec = t[i_dec] - t[i_mx]
        i_end = max((i for i in range(len(r)) if r[i] > mx - 30), default=len(r) - 1); rel = t[-1] - t[i_end]
        out.append("Enveloppe RMS : attaque ≈ %.0f ms (jusqu'à -1 dB du max), decay ≈ %.0f ms, sustain ≈ %.1f dB sous le max, fin/queue ≈ %.0f ms avant la fin de l'extrait%s" % (
            att * 1000, dec * 1000, mx - sus, rel * 1000, '' if rel > 0.02 else " (la note tient jusqu'au bout : release non observable)"))
        out.append('  → départ ampli : A %d ms, D %d ms, S %d %%, R %s' % (max(1, round(att * 1000 * 0.8)), max(20, round(dec * 1000)), round(100 * 10 ** (-(mx - sus) / 20)), ('%d ms' % round(rel * 1000)) if rel > 0.02 else '80–300 ms (à choisir)'))
# --- spectre
sp = d.get('spectrum') or {}
peaks = sp.get('strongest_peaks') or []
if f0 and peaks:
    harm = {}
    for p in peaks:
        n = p['bin_frequency_hz'] / f0
        k = round(n)
        if k >= 1 and abs(n - k) < 0.12: harm.setdefault(k, p['relative_power_db'])
    if harm:
        ks = sorted(harm); odd = [harm[k] for k in ks if k % 2 == 1 and k > 1]; even = [harm[k] for k in ks if k % 2 == 0]
        prof = ' '.join('H%d %.0f' % (k, harm[k]) for k in ks[:8])
        if len(ks) <= 2: forme = "sinus/sub (presque pas d'harmoniques)"
        elif even and (not odd or sum(even) / len(even) > sum(odd) / len(odd) + 6): forme = 'pairs dominants : dent-de-scie filtrée ou FM douce'
        elif odd and (not even or sum(odd) / len(odd) > sum(even) / len(even) + 6): forme = 'impairs dominants : carré / pulse (ou triangle si pente forte)'
        else: forme = 'série complète : dent-de-scie (ou table riche) filtrée'
        pente = (harm[ks[-1]] - harm[ks[0]]) / max(1, math.log2(ks[-1] / ks[0])) if len(ks) > 1 else 0
        out.append('Harmoniques (dB rel.) : %s → %s ; pente ≈ %.0f dB/octave' % (prof, forme, pente))
        inh = [p for p in peaks if abs(p['bin_frequency_hz'] / f0 - round(p['bin_frequency_hz'] / f0)) >= 0.12 and p['bin_frequency_hz'] > f0 * 1.5]
        if inh: out.append('  partiels non harmoniques : %s → FM, inharmonicité ou bruit/seconde source' % ', '.join('%.0f Hz' % p['bin_frequency_hz'] for p in inh[:4]))
if sp.get('centroid_hz'):
    c = sp['centroid_hz']; ro = sp.get('rolloff_95_hz')
    cut = ro * 1.3 if ro else c * 2
    out.append("Centroïde %.0f Hz, 95 %% de l'énergie sous %s Hz → cutoff passe-bas de départ ≈ %.0f Hz%s" % (c, ('%.0f' % ro) if ro else '?', cut, (' (%.1f octaves au-dessus de f0)' % math.log2(cut / f0)) if f0 else ''))
# --- stéréo
st = d.get('stereo') or {}
if st.get('side_to_mid_db') is not None:
    s2m = st['side_to_mid_db']; corr = st.get('correlation')
    out.append('Stéréo : side/mid %.1f dB, corrélation %.2f → %s' % (s2m, corr if corr is not None else float('nan'),
        "mono : 1 voix, pas d'unisson ni de chorus" if s2m < -25 else 'largeur modérée : unisson 2–3 voix ou chorus léger' if s2m < -10 else 'large : unisson 4+ voix, detune, chorus/doublage — vérifier la tenue en mono'))
# --- niveaux
ch = d.get('channels') or []
if ch: out.append('Niveau extrait : crête %.1f dBFS, RMS %.1f dBFS (canal 1) — viser le même RMS lors de la comparaison' % (ch[0]['sample_peak_dbfs'], ch[0]['rms_dbfs']))
if tempo: out.append('Tempo %g BPM : noire %.0f ms, croche %.0f ms, double %.0f ms (pour delay/LFO synchronisés)' % (tempo, 60000 / tempo, 30000 / tempo, 15000 / tempo))
out.append("Rappel : hypothèses issues d'un extrait traité — un changement de famille à la fois, puis nouveau rapport et compare_reports.py.")
print('\n'.join(out))
