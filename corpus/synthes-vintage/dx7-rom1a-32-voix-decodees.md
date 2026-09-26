---
titre: "Yamaha DX7 ROM1A — les 32 voix d'usine décodées depuis le sysex (BRASS 1-3, E.PIANO 1, BASS 1-2, E.ORGAN 1, CLAV 1…)"
source: https://raw.githubusercontent.com/benny-sparra/fm1-dx7-patch-importer/main/public/dx7-banks/factory/rom1a.syx
recupere_le: 2026-09-24
mode: texte integral (décodage)
langue: en
axe: synthèse FM ; patches d'usine
skills: studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Décodage du fichier sysex (4104 octets, checksum vérifié) par le script decode_dx7.py ci-joint. Rates et levels DX7 sont en unités 0-99, pas en millisecondes.

```
len 4104 header f04300092000 tail 33f7
======================================================================
VOICE 1: 'BRASS   1 '  ALG=22 FB=7 OSC KEY SYNC=1 TRANSPOSE=24 (24=C3)
  PEG rates [84, 95, 95, 60] levels [50, 50, 50, 50]
  LFO speed=37 delay=0 PMD=5 AMD=0 sync=0 wave=SIN PMS=3
  OP6: ratio=1.00 det=+0 OL= 82 | EG R=[49, 99, 28, 68] L=[98, 98, 91, 0] | KS BP=39 LD=54-EXP RD=50-EXP RS=4 | AMS=0 KVS=2
  OP5: ratio=1.00 det=+1 OL= 98 | EG R=[77, 36, 41, 71] L=[99, 98, 98, 0] | KS BP=39 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=2
  OP4: ratio=1.00 det=+0 OL= 99 | EG R=[77, 36, 41, 71] L=[99, 98, 98, 0] | KS BP=39 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=2
  OP3: ratio=1.00 det=-2 OL= 99 | EG R=[77, 76, 82, 71] L=[99, 98, 98, 0] | KS BP=39 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=2
  OP2: ratio=0.50 det=+7 OL= 86 | EG R=[62, 51, 29, 71] L=[82, 95, 96, 0] | KS BP=27 LD=0+LIN RD=7-EXP RS=0 | AMS=0 KVS=0
  OP1: ratio=0.50 det=+7 OL= 98 | EG R=[72, 76, 99, 71] L=[99, 88, 96, 0] | KS BP=39 LD=0+LIN RD=14+LIN RS=0 | AMS=0 KVS=0
======================================================================
VOICE 2: 'BRASS   2 '  ALG=22 FB=7 OSC KEY SYNC=1 TRANSPOSE=24 (24=C3)
  PEG rates [84, 95, 95, 60] levels [50, 50, 50, 50]
  LFO speed=37 delay=0 PMD=0 AMD=0 sync=0 wave=SIN PMS=3
  OP6: ratio=0.50 det=+0 OL= 80 | EG R=[99, 39, 32, 71] L=[99, 98, 88, 0] | KS BP=51 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=0
  OP5: ratio=0.50 det=+1 OL= 99 | EG R=[99, 39, 32, 71] L=[99, 98, 81, 0] | KS BP=39 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=0
  OP4: ratio=0.50 det=-2 OL= 99 | EG R=[99, 39, 32, 71] L=[99, 98, 81, 0] | KS BP=39 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=0
  OP3: ratio=0.50 det=-3 OL= 99 | EG R=[99, 39, 32, 71] L=[99, 98, 81, 0] | KS BP=39 LD=0+LIN RD=0+LIN RS=0 | AMS=0 KVS=0
  OP2: ratio=0.50 det=+7 OL= 84 | EG R=[99, 39, 32, 71] L=[99, 98, 80, 0] | KS BP=51 LD=0+LIN RD=38+LIN RS=0 | AMS=0 KVS=0
  OP1: ratio=0.50 det=+7 OL= 99 | EG R=[99, 39, 32, 71] L=[99, 98, 80, 0] | KS BP=51 LD=0+LIN RD=38+LIN RS=0 | AMS=0 KVS=0
======================================================================
VOICE 3: 'BRASS   3 '  ALG=18 FB=6 OSC KEY SYNC=1 TRANSPOSE=12 (24=C3)
  PEG rates [94, 67, 95, 60] levels [50, 50, 50, 50]
  LFO speed=35 delay=0 PMD=5 AMD=0 sync=0 wave=TRI PMS=3
  OP6: ratio=8.47 det=+0 OL= 79 | EG R=[77, 56, 20, 70] L=[99, 0, 0, 0] | KS BP=0 LD=0-LIN RD=0-LIN RS=7 | AMS=0 KVS=0
  OP5: ratio=3.18 det=-1 OL= 70 | EG R=[48, 55, 22, 50] L=[98, 61, 62, 0] | KS BP=0 LD=0-LIN RD=0-LIN RS=0 | AMS=0 KVS=0
  OP4: ratio=1.00 det=+0 OL= 79 | EG R=[66, 92, 22, 50] L=[53, 61, 62, 0] | KS BP=0 LD=0-LIN RD=0-LIN RS=0 | AMS=0 KVS=0
  OP3: ratio=1.00 det=+0 OL= 77 | EG R=[46, 35, 22, 50] L=[99, 86, 86, 0] | KS BP=0 LD=0-LIN RD=0-LIN RS=1 | AMS=0 KVS=1
  OP2: ratio=1.00 det=+0 OL= 70 | EG R=[37, 34, 15, 70] L=[85, 0, 0, 0] | KS BP=0 LD=0-LIN RD=0-LIN RS=2 | AMS=0 KVS=1
  OP1: ratio=1.00 det=+0 OL= 99 | EG R=[55, 24, 19, 55] L=[99, 86, 86, 0] | KS BP=0 LD=0-LIN RD=0-LIN RS=2 | AMS=0 KVS=2

```

## Script de décodage

```python
import sys
data = open('rom1a.syx','rb').read()
print("len", len(data), "header", data[:6].hex(), "tail", data[-2:].hex())
assert data[0]==0xF0 and data[1]==0x43
body = data[6:6+4096]
def voice(i):
    v = body[i*128:(i+1)*128]
    ops = []
    for o in range(6):
        b = v[o*17:(o+1)*17]
        op = dict(
            num = 6-o,
            R = list(b[0:4]), L = list(b[4:8]),
            BP = b[8], LD = b[9], RD = b[10],
            LC = b[11] & 3, RC = (b[11]>>2)&3,
            RS = b[12] & 7, DET = (b[12]>>3)&15,
            AMS = b[13] & 3, KVS = (b[13]>>2)&7,
            OL = b[14],
            mode = b[15] & 1, coarse = (b[15]>>1)&31,
            fine = b[16],
        )
        ops.append(op)
    g = v[102:]
    peg_R = list(g[0:4]); peg_L = list(g[4:8])
    alg = g[8]+1
    fb = g[9] & 7; oks = (g[9]>>3)&1
    lfs, lfd, lpmd, lamd = g[10], g[11], g[12], g[13]
    lsync = g[14]&1; lwave=(g[14]>>1)&7; pms=(g[14]>>4)&7
    transpose = g[15]
    name = g[16:26].decode('ascii', 'replace')
    return dict(name=name, alg=alg, fb=fb, oks=oks, peg_R=peg_R, peg_L=peg_L,
                lfo=dict(speed=lfs, delay=lfd, pmd=lpmd, amd=lamd, sync=lsync, wave=lwave, pms=pms),
                transpose=transpose, ops=ops)
curves = ['-LIN','-EXP','+EXP','+LIN']
waves = ['TRI','SAW DN','SAW UP','SQU','SIN','S/H']
def ratio(op):
    if op['mode']==0:
        c = 0.5 if op['coarse']==0 else op['coarse']
        return c * (1 + op['fine']/100.0)
    else:
        return None
for idx in [0,1,2]:
    v = voice(idx)
    print("="*70)
    print(f"VOICE {idx+1}: '{v['name']}'  ALG={v['alg']} FB={v['fb']} OSC KEY SYNC={v['oks']} TRANSPOSE={v['transpose']} (24=C3)")
    print(f"  PEG rates {v['peg_R']} levels {v['peg_L']}")
    l = v['lfo']
    print(f"  LFO speed={l['speed']} delay={l['delay']} PMD={l['pmd']} AMD={l['amd']} sync={l['sync']} wave={waves[l['wave']]} PMS={l['pms']}")
    for op in v['ops']:
        r = ratio(op)
        rs = f"ratio={r:.2f}" if r is not None else f"FIXED coarse={op['coarse']} fine={op['fine']}"
        print(f"  OP{op['num']}: {rs} det={op['DET']-7:+d} OL={op['OL']:3d} | EG R={op['R']} L={op['L']} | KS BP={op['BP']} LD={op['LD']}{curves[op['LC']]} RD={op['RD']}{curves[op['RC']]} RS={op['RS']} | AMS={op['AMS']} KVS={op['KVS']}")

```