#!/usr/bin/env python3
from pathlib import Path
import sys, json, hashlib
root=Path(__file__).resolve().parents[1]
errs=[]
skills=list(root.rglob('SKILL.md'))+list(root.rglob('skill.md'))
uniq={str(p).lower():p for p in skills}
if len(uniq)!=1:
    errs.append(f"Expected exactly one SKILL.md, found {len(uniq)}")
p=root/'SKILL.md'
if not p.exists():
    errs.append('Top-level SKILL.md missing')
else:
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('---\n'):
        errs.append('Missing YAML frontmatter start')
    if 'name: electronic-production-engineer' not in txt:
        errs.append('Canonical name missing')
    if 'description:' not in txt:
        errs.append('Description missing')
for s in root.glob('schemas/*.json'):
    try:
        json.loads(s.read_text(encoding='utf-8'))
    except Exception as e:
        errs.append(f'Invalid JSON {s.name}: {e}')
for bad in list(root.rglob('__pycache__')) + list(root.rglob('*.pyc')):
    errs.append(f'Compiled/cache artifact should not ship: {bad.relative_to(root)}')
# If a manifest exists, verify every listed file and checksum.
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
print('Skill pack validation OK')
