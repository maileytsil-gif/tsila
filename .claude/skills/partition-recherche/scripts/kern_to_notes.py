#!/usr/bin/env python3
"""Usage: kern_to_notes.py fichier.krn [--mesures A-B] [--spine N] [--json]
Extrait (mesure, position en noires depuis le début de la mesure, durée en noires, nom scientifique, MIDI, voix) des spines **kern.
Liaisons [ ] fusionnées (la durée est cumulée sur la première note), notes d'agrément (q) durée 0, silences omis. Mesure 0 = anacrouse."""
import re, sys, json
args = sys.argv[1:]; path = args[0]
mes = None; spine_sel = None; as_json = '--json' in args
if '--mesures' in args: a, b = args[args.index('--mesures') + 1].split('-'); mes = (int(a), int(b))
if '--spine' in args: spine_sel = int(args[args.index('--spine') + 1])
lines = open(path, encoding='utf-8').read().split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('**kern'))
kinds = lines[start].split('\t'); kern_cols = [i for i, k in enumerate(kinds) if k == '**kern']
def dur(tok):
    m = re.match(r'(\d+)(\.*)', re.sub(r'^[\[\]()<>{}~JLKk;:]+', '', tok))
    if not m: return None
    n = int(m.group(1)); base = 8.0 if n == 0 else 4.0 / n; tot = base; add = base
    for _ in m.group(2): add /= 2; tot += add
    return tot
def pitch(tok):
    m = re.search(r'([a-gA-G]+)([#\-n]*)', tok)
    if not m: return None
    L, acc = m.group(1), m.group(2); ch = L[0]
    octv = 4 + len(L) - 1 if ch.islower() else 3 - (len(L) - 1)
    base = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[ch.upper()]
    alt = acc.count('#') - acc.count('-')
    nom = ch.upper() + ('#' * acc.count('#') or 'b' * acc.count('-')) + str(octv)
    return nom, 12 * (octv + 1) + base + alt
out = []; pos = {c: 0.0 for c in kern_cols}; measure = 0; pending = {}  # pending[(col,pitch)] = index dans out (liaison ouverte)
for l in lines[start + 1:]:
    if not l or l.startswith('!') or l.startswith('*'):
        continue
    cols = l.split('\t')
    if cols[0].startswith('='):
        m = re.match(r'=+(\d+)', cols[0]); measure = int(m.group(1)) if m else measure + 1
        if mes and measure > mes[1]: break
        for c in kern_cols: pos[c] = 0.0
        continue
    for vi, c in enumerate(kern_cols, 1):
        if spine_sel and vi != spine_sel: continue
        tok = cols[c] if c < len(cols) else '.'
        if tok in ('.', ''): continue
        subs = tok.split(); d0 = dur(subs[0])
        for sub in subs:
            d = dur(sub)
            if d is None or 'r' in sub: continue
            if 'q' in sub: d = 0.0
            p = pitch(sub)
            if not p: continue
            if ']' in sub and (c, p[1]) in pending:            # fin de liaison : cumuler
                out[pending.pop((c, p[1]))]['duree'] += d
                if '[' in sub: pending[(c, p[1])] = len(out) - 1
                continue
            if mes is None or mes[0] <= measure <= mes[1]:
                out.append({'mesure': measure, 'temps': round(pos[c], 4), 'duree': d, 'note': p[0], 'midi': p[1], 'voix': vi, 'agrement': 'q' in sub})
                if '[' in sub: pending[(c, p[1])] = len(out) - 1
        if d0 is not None and 'q' not in subs[0]: pos[c] += d0
if as_json: print(json.dumps(out, ensure_ascii=False))
else:
    for e in out: print('m%-3d t=%-6g d=%-6g %-5s midi=%-3d voix %d%s' % (e['mesure'], e['temps'], e['duree'], e['note'], e['midi'], e['voix'], ' (agrément)' if e['agrement'] else ''))
