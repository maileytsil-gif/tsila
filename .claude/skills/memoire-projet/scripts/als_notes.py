#!/usr/bin/env python3
"""Extrait les notes visibles des clips d'arrangement d'un Set sauvegardé (.als, gzip XML), sans ouvrir Live.
Usage : als_notes.py <fichier.als> <sortie.json> [PISTE ...]   (défaut : toutes les pistes MIDI)
Sortie : {piste: [{start, end, notes: [[temps_absolu, durée, pitch, vélocité], ...]}, ...]}  — temps en beats (mesure = temps/4 + 1)."""
import gzip, sys, json, xml.etree.ElementTree as ET
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 else 2)

als, out = sys.argv[1], sys.argv[2]; voulues = set(sys.argv[3:])
root = ET.fromstring(gzip.open(als).read()); res = {}
for tr in root.iter('MidiTrack'):
    name = tr.find('Name/EffectiveName').get('Value')
    if voulues and name not in voulues: continue
    clips = []
    for mc in tr.iter('MidiClip'):
        if mc.find('CurrentStart') is None: continue
        cs = float(mc.find('CurrentStart').get('Value')); ce = float(mc.find('CurrentEnd').get('Value')); ls = float(mc.find('Loop/LoopStart').get('Value'))
        notes = []
        for kt in mc.iter('KeyTrack'):
            p = int(kt.find('MidiKey').get('Value'))
            for ev in kt.iter('MidiNoteEvent'):
                t = float(ev.get('Time'))
                if ls <= t < ls + (ce - cs) and ev.get('IsEnabled', 'true') == 'true':
                    notes.append([round(cs + (t - ls), 4), round(float(ev.get('Duration')), 4), p, int(float(ev.get('Velocity')))])
        notes.sort(); clips.append({'name': (mc.find('Name').get('Value') if mc.find('Name') is not None else ''), 'start': cs, 'end': ce, 'notes': notes})
    clips.sort(key=lambda c: c['start']); res[name] = clips
json.dump(res, open(out, 'w'))
for k, v in res.items(): print('%s : %d clips, %d notes' % (k, len(v), sum(len(c['notes']) for c in v)))
