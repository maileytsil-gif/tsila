#!/usr/bin/env python3
# Validates this folder as a module of the producteur-live skill (GUIDE.md at the root, no SKILL.md: a nested SKILL.md
# would be loaded as a second skill). Before the regrouping of 8 Oct. 2026 it validated a standalone skill pack.
from pathlib import Path
import sys, json, hashlib
root=Path(__file__).resolve().parents[1]
errs=[]
for bad in list(root.rglob('SKILL.md'))+list(root.rglob('skill.md')):
    errs.append(f'No SKILL.md allowed inside a module (found {bad.relative_to(root)}); the entry file is GUIDE.md')
p=root/'GUIDE.md'
if not p.exists():
    errs.append('Top-level GUIDE.md missing')
else:
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('# '):
        errs.append('GUIDE.md must start with an H1 title')
    if 'Module du skill `producteur-live`' not in txt:
        errs.append('GUIDE.md must state the parent skill (Module du skill `producteur-live`)')
for s in root.glob('schemas/*.json'):
    try:
        json.loads(s.read_text(encoding='utf-8'))
    except Exception as e:
        errs.append(f'Invalid JSON {s.name}: {e}')
for bad in list(root.rglob('__pycache__')) + list(root.rglob('*.pyc')):
    errs.append(f'Compiled/cache artifact should not ship: {bad.relative_to(root)}')
# If a manifest exists, verify every listed file and checksum (python3 outils/regrouper_skills.py --manifest refreshes it).
mf=root/'MANIFEST.json'
if mf.exists():
    try:
        m=json.loads(mf.read_text())
        for item in m.get('files',[]):
            fp=root/item['path']
            if not fp.exists():
                errs.append(f"Manifest missing file: {item['path']}")
                continue
            h=hashlib.sha256(fp.read_bytes()).hexdigest()
            if h != item.get('sha256'):
                errs.append(f"Manifest checksum mismatch: {item['path']}")
    except Exception as e:
        errs.append(f'Invalid manifest: {e}')
if errs:
    print('\n'.join('ERROR: '+e for e in errs))
    sys.exit(1)
print('Module validation OK')
