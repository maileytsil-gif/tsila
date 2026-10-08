#!/usr/bin/env python3
"""Compare deux instantanés (snapshot_clips.py ou als_notes.py) : pistes/clips ajoutés, retirés, notes modifiées.
Usage : diff_snapshot.py avant.json apres.json"""
import json, sys
def charge(p):
    d = json.load(open(p)); d = d.get('tracks', d)
    return {t: {(round(c['start'], 3), round(c['end'], 3)): c for c in (v['clips'] if isinstance(v, dict) else v)} for t, v in d.items()}
a, b = charge(sys.argv[1]), charge(sys.argv[2]); bar = lambda x: '%g' % (x / 4 + 1)
for t in sorted(set(a) | set(b)):
    ca, cb = a.get(t, {}), b.get(t, {})
    for k in sorted(set(ca) | set(cb)):
        if k not in ca: print('%s : clip AJOUTÉ %s-%s (%d notes)' % (t, bar(k[0]), bar(k[1]), len(cb[k]['notes'])))
        elif k not in cb: print('%s : clip RETIRÉ %s-%s (%d notes)' % (t, bar(k[0]), bar(k[1]), len(ca[k]['notes'])))
        elif ca[k]['notes'] != cb[k]['notes']:
            sa, sb = set(map(tuple, ca[k]['notes'])), set(map(tuple, cb[k]['notes']))
            print('%s : clip %s-%s MODIFIÉ : %d notes → %d (−%d, +%d)' % (t, bar(k[0]), bar(k[1]), len(sa), len(sb), len(sa - sb), len(sb - sa)))
print('comparaison terminée')
