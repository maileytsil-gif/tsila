#!/usr/bin/env python3
"""Génère « LOM Bridge.amxd » (Max MIDI Effect) à partir du gabarit Ableton + patcher udpreceive -> js -> udpsend."""
import json, struct, sys, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
tpl = json.load(open(os.path.join(HERE, 'midi_template.json')))
RX, TX = 7411, 7412
p = tpl['patcher']
p['title'] = 'LOM Bridge'
p['description'] = 'Pont OSC/UDP vers le Live Object Model (automation, get/set/call). In %d / out %d' % (RX, TX)
def box(i, maxclass, text, rect, nin, nout, otypes, **extra):
    b = {"id": f"obj-{i}", "maxclass": maxclass, "numinlets": nin, "numoutlets": nout,
         "patching_rect": rect, "text": text}
    if nout: b["outlettype"] = otypes
    b.update(extra)
    return {"box": b}
boxes = [
    box(1, "newobj", "midiin", [16, 16, 40, 20], 1, 1, ["int"]),
    box(2, "newobj", "midiout", [16, 130, 47, 20], 1, 0, []),
    box(10, "newobj", f"udpreceive {RX}", [120, 40, 200, 20], 1, 1, [""]),
    box(11, "newobj", "js lombridge.js", [120, 80, 110, 20], 1, 2, ["", ""]),
    box(12, "newobj", f"udpsend 127.0.0.1 {TX}", [120, 130, 230, 20], 1, 0, []),
    box(13, "newobj", "live.thisdevice", [240, 16, 90, 20], 1, 3, ["bang", "int", "int"]),
    box(14, "newobj", "print lombridge", [260, 105, 95, 20], 1, 0, []),
    box(15, "comment", f"LOM Bridge v0.1 — OSC in {RX} / out {TX} (localhost). Commandes : /ping /track /param /params /shape /read /clear /get /set /call /js", [16, 150, 340, 18], 1, 0, []),
]
lines = [
    {"patchline": {"source": ["obj-1", 0], "destination": ["obj-2", 0]}},
    {"patchline": {"source": ["obj-10", 0], "destination": ["obj-11", 0]}},
    {"patchline": {"source": ["obj-13", 0], "destination": ["obj-11", 0]}},
    {"patchline": {"source": ["obj-11", 0], "destination": ["obj-12", 0]}},
    {"patchline": {"source": ["obj-11", 1], "destination": ["obj-14", 0]}},
]
p['boxes'] = boxes; p['lines'] = lines
p['dependency_cache'] = [{"name": "lombridge.js", "bootpath": ".", "patcherrelativepath": ".", "type": "TEXT", "implicit": 1}]
js = json.dumps(tpl, indent=1).encode('utf-8')
amxd = b'ampf' + struct.pack('<I', 4) + b'mmmm' + b'meta' + struct.pack('<I', 4) + struct.pack('<I', 0) + b'ptch' + struct.pack('<I', len(js)) + js
out_dir = sys.argv[1] if len(sys.argv) > 1 else HERE
os.makedirs(out_dir, exist_ok=True)
open(os.path.join(out_dir, 'LOM Bridge.amxd'), 'wb').write(amxd)
src_js, dst_js = os.path.join(HERE, 'lombridge.js'), os.path.join(out_dir, 'lombridge.js')
if os.path.abspath(src_js) != os.path.abspath(dst_js): shutil.copy(src_js, dst_js)
print('écrit', os.path.join(out_dir, 'LOM Bridge.amxd'), len(amxd), 'octets')
