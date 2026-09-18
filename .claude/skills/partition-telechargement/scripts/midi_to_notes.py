#!/usr/bin/env python3
"""Usage: midi_to_notes.py fichier.mid [--resume] [--json] [--piste N]
Lit un MIDI (format 0/1) sans dépendance : tempo, signature, pistes, notes (mesure, temps en noires depuis le début de mesure, durée en noires, nom scientifique, MIDI, vélocité, piste).
La mesure est calculée avec la première signature rencontrée (les changements de signature sont signalés)."""
import sys, json
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 else 2)

args = sys.argv[1:]; path = args[0]; resume = '--resume' in args; as_json = '--json' in args
piste_sel = int(args[args.index('--piste') + 1]) if '--piste' in args else None
data = open(path, 'rb').read(); pos = 0
def rd(n):
    global pos; b = data[pos:pos + n]; pos += n; return b
def varlen():
    v = 0
    while True:
        b = rd(1)[0]; v = (v << 7) | (b & 0x7F)
        if not b & 0x80: return v
assert rd(4) == b'MThd'; hl = int.from_bytes(rd(4), 'big'); fmt, ntr, div = int.from_bytes(rd(2), 'big'), int.from_bytes(rd(2), 'big'), int.from_bytes(rd(2), 'big'); pos += hl - 6
events = []; tempos = []; sigs = []; names = {}
for ti in range(ntr):
    assert rd(4) == b'MTrk'; ln = int.from_bytes(rd(4), 'big'); end = pos + ln; t = 0; status = 0
    while pos < end:
        t += varlen(); b = data[pos]
        if b == 0xFF:
            pos += 1; typ = data[pos]; pos += 1; L = varlen(); payload = rd(L)
            if typ == 0x51: tempos.append((t, int.from_bytes(payload, 'big')))
            elif typ == 0x58: sigs.append((t, payload[0], 2 ** payload[1]))
            elif typ == 0x03: names[ti] = payload.decode('latin-1', 'ignore')
            continue
        if b in (0xF0, 0xF7): pos += 1; L = varlen(); pos += L; continue
        if b & 0x80: status = b; pos += 1
        hi = status & 0xF0
        if hi in (0x80, 0x90, 0xA0, 0xB0, 0xE0): d1, d2 = data[pos], data[pos + 1]; pos += 2
        else: d1 = data[pos]; pos += 1; d2 = 0
        if hi == 0x90 and d2 > 0: events.append((t, ti, 'on', d1, d2))
        elif hi == 0x80 or (hi == 0x90 and d2 == 0): events.append((t, ti, 'off', d1, 0))
    pos = end
num, den = (sigs[0][1], sigs[0][2]) if sigs else (4, 4); bar_ticks = div * 4 * num / den
tempo_bpm = 60e6 / (tempos[0][1] if tempos else 500000)
NOMS = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
notes = []; on = {}
for t, ti, kind, p, v in sorted(events, key=lambda e: (e[0], e[2] == 'on')):
    if piste_sel is not None and ti != piste_sel: continue
    if kind == 'on': on[(ti, p)] = (t, v)
    elif (ti, p) in on:
        t0, v0 = on.pop((ti, p)); bar = int(t0 // bar_ticks) + 1
        notes.append({'mesure': bar, 'temps': round((t0 - (bar - 1) * bar_ticks) / div, 4), 'duree': round((t - t0) / div, 4), 'note': NOMS[p % 12] + str(p // 12 - 1), 'midi': p, 'vel': v0, 'piste': ti})
if resume or not as_json:
    print('format %d, %d pistes, %d ticks/noire, tempo %.1f BPM, signature %d/%d%s, %d notes, %d mesures' % (fmt, ntr, div, tempo_bpm, num, den, (' (+%d changements)' % (len(sigs) - 1)) if len(sigs) > 1 else '', len(notes), max([n['mesure'] for n in notes] + [0])))
    for k, v in sorted(names.items()): print('  piste %d : %s (%d notes)' % (k, v, sum(1 for n in notes if n['piste'] == k)))
if as_json: print(json.dumps(notes, ensure_ascii=False))
elif not resume:
    for n in notes[:80]: print('m%-3d t=%-6g d=%-6g %-4s midi=%-3d v%-3d piste %d' % (n['mesure'], n['temps'], n['duree'], n['note'], n['midi'], n['vel'], n['piste']))
