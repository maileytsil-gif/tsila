#!/usr/bin/env python3
"""Usage: kit_builder.py [signature.json] [famille]  -> imprime les params JSON pour ppal-create-device (Drum Rack) d'une famille, ou toutes.
Copier le tableau dans `params` de ppal-create-device (deviceName "Drum Rack", path "tN"), puis régler gain/pan de chaîne avec ppal-update-device (path tN/d0/pXX)."""
import sys, json, os
p = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].endswith('.json') else os.path.join(os.path.dirname(__file__), 'signature.json')
fam = next((a for a in sys.argv[1:] if not a.endswith('.json')), None)
sig = json.load(open(p))
for nom, f in sig['familles'].items():
    if fam and fam.lower() not in nom.lower(): continue
    if f.get('type') != 'drum-rack':
        print('%s : %s — %s (pas un Drum Rack ; voir vst-sound-design)' % (nom, f.get('type'), f.get('preset'))); continue
    params = []
    for pad in f['pads']:
        params.append({'name': '%s/d0/sample' % pad['pad'], 'value': pad['sample']})
    print('== %s ==  ppal-create-device deviceName="Drum Rack" name="%s" params=' % (nom, nom)); print(json.dumps(params, ensure_ascii=False, indent=1))
    print('puis gains/pans de chaîne : ' + ' ; '.join('ppal-update-device path=tN/d0/%s gainDb=%s pan=%s' % (pad['pad'], pad['gainDb'], pad['pan']) for pad in f['pads']))
    print('chaîne : %s | niveau cible avant fader %s dB' % (f.get('chaine'), f.get('niveau_pre_fader_db')))
