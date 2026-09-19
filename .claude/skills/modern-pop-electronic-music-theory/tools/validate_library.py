#!/usr/bin/env python3
from pathlib import Path
import json
from mido import MidiFile
root=Path(__file__).resolve().parents[1]/'library'
for p in (root/'data').glob('*.json'):
    json.loads(p.read_text())
for p in (root/'midi-clips').rglob('*.mid'):
    mf=MidiFile(p)
    for tr in mf.tracks:
        for msg in tr:
            if hasattr(msg,'note') and not 0 <= msg.note <= 127: raise ValueError((p,msg.note))
print('OK')
