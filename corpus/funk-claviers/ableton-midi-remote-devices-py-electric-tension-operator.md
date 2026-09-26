---
titre: "Ableton Live 12 MIDI Remote Scripts — _Generic/Devices.py, extrait : banques LoungeLizard (Electric), StringStudio (Tension) et Operator"
source: https://raw.githubusercontent.com/gluon/AbletonLive12_MIDIRemoteScripts/main/_Generic/Devices.py
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: Ableton Live 12 : Electric, Tension, Operator, Vocoder, packs (documents tiers et miroirs)
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

> Extrait : en-tête, ELC_* (Electric = LoungeLizard), OPR_* (Operator) et TNS_* (Tension = StringStudio) ; les autres devices sont omis.

```python
# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/Devices.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 42603 bytes
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import filter, map, range, str
from past.utils import old_div
from functools import partial
from _Framework.Util import group
RCK_BANK1 = ('Macro 1', 'Macro 2', 'Macro 3', 'Macro 4', 'Macro 5', 'Macro 6', 'Macro 7',
             'Macro 8')
RCK_BANK2 = ('Macro 9', 'Macro 10', 'Macro 11', 'Macro 12', 'Macro 13', 'Macro 14',
             'Macro 15', 'Macro 16')

ELC_BANK1 = ('M Stiffness', 'M Force', 'Noise Pitch', 'Noise Decay', 'Noise Amount',
             'F Tine Color', 'F Tine Decay', 'F Tine Vol')
ELC_BANK2 = ('F Tone Decay', 'F Tone Vol', 'F Release', 'Damp Tone', 'Damp Balance',
             'Damp Amount', '', '')
ELC_BANK3 = ('P Symmetry', 'P Distance', 'P Amp In', 'P Amp Out', 'Pickup Model', '',
             '', '')
ELC_BANK4 = ('M Stiff < Vel', 'M Stiff < Key', 'M Force < Vel', 'M Force < Key', 'Noise < Key',
             'F Tine < Key', 'P Amp < Key', '')
ELC_BANK5 = ('Volume', 'Voices', 'Semitone', 'Detune', 'KB Stretch', 'PB Range', 'Note PB Range',
             '')
ELC_BOB = ('M Stiffness', 'M Force', 'Noise Amount', 'F Tine Vol', 'F Tone Vol', 'F Release',
           'P Symmetry', 'Volume')
ELC_BANKS = (
 ELC_BANK1, ELC_BANK2, ELC_BANK3, ELC_BANK4, ELC_BANK5)
ELC_BOBS = (ELC_BOB,)
ELC_BNK_NAMES = ('Mallet and Tine', 'Tone and Damper', 'Pickup', 'Modulation', 'Global')

OPR_BANK1 = ('Ae Attack', 'Ae Decay', 'Ae Sustain', 'Ae Release', 'A Coarse', 'A Fine',
             'Osc-A Lev < Vel', 'Osc-A Level')
OPR_BANK2 = ('Be Attack', 'Be Decay', 'Be Sustain', 'Be Release', 'B Coarse', 'B Fine',
             'Osc-B Lev < Vel', 'Osc-B Level')
OPR_BANK3 = ('Ce Attack', 'Ce Decay', 'Ce Sustain', 'Ce Release', 'C Coarse', 'C Fine',
             'Osc-C Lev < Vel', 'Osc-C Level')
OPR_BANK4 = ('De Attack', 'De Decay', 'De Sustain', 'De Release', 'D Coarse', 'D Fine',
             'Osc-D Lev < Vel', 'Osc-D Level')
OPR_BANK5 = ('Le Attack', 'Le Decay', 'Le Sustain', 'Le Release', 'LFO Rate', 'LFO Amt',
             'LFO Type', 'LFO R < K')
OPR_BANK6 = ('Fe Attack', 'Fe Decay', 'Fe Sustain', 'Fe Release', 'Filter Freq', 'Filter Res',
             'Fe R < Vel', 'Fe Amount')
OPR_BANK7 = ('Pe Attack', 'Pe Decay', 'Pe Sustain', 'Pe Release', 'Pe Init', 'Glide Time',
             'Pe Amount', 'Spread')
OPR_BANK8 = ('Time < Key', 'Panorama', 'Pan < Key', 'Pan < Rnd', 'Algorithm', 'Time',
             'Tone', 'Volume')
OPR_BOB = ('Filter Freq', 'Filter Res', 'A Coarse', 'A Fine', 'B Coarse', 'B Fine',
           'Osc-B Level', 'Volume')
OPR_BANKS = (
 OPR_BANK1,
 OPR_BANK2,
 OPR_BANK3,
 OPR_BANK4,
 OPR_BANK5,
 OPR_BANK6,
 OPR_BANK7,
 OPR_BANK8)
OPR_BOBS = (
 OPR_BOB,)
OPR_BNK_NAMES = ('Oscillator A', 'Oscillator B', 'Oscillator C', 'Oscillator D', 'LFO',
                 'Filter', 'Pitch Modulation', 'Routing')

TNS_BANK1 = ('Exciter Type', 'String Decay', 'Str Inharmon', 'Str Damping', 'Exc ForceMassProt',
             'Exc FricStiff', 'Exc Velocity', 'E Pos')
TNS_BANK2 = ('Damper On', 'Damper Mass', 'D Stiffness', 'D Velocity', 'Damp Pos', 'D Damping',
             'D Pos < Vel', 'D Pos Abs')
TNS_BANK3 = ('Term On/Off', 'Term Mass', 'Term Fng Stiff', 'Term Fret Stiff', 'Pickup On/Off',
             'Pickup Pos', 'T Mass < Vel', 'T Mass < Key')
TNS_BANK4 = ('Body On/Off', 'Body Type', 'Body Size', 'Body Decay', 'Body Low-Cut',
             'Body High-Cut', 'Body Mix', 'Volume')
TNS_BANK5 = ('Vibrato On/Off', 'Vib Delay', 'Vib Fade-In', 'Vib Speed', 'Vib Amount',
             'Vib < ModWh', 'Vib Error', 'Volume')
TNS_BANK6 = ('Filter On/Off', 'Filter Type', 'Filter Freq', 'Filter Reso', 'Freq < Env',
             'Freq < LFO', 'Reso < Env', 'Reso < LFO')
TNS_BANK7 = ('FEG On/Off', 'FEG Attack', 'FEG Decay', 'FEG Sustain', 'FEG Release',
             'LFO On/Off', 'LFO Shape', 'LFO Speed')
TNS_BANK8 = ('Unison On/Off', 'Uni Detune', 'Porta On/Off', 'Porta Time', 'Voices',
             'Octave', 'Semitone', 'Volume')
TNS_BOB = ('Filter Freq', 'Filter Reso', 'Filter Type', 'Exciter Type', 'E Pos', 'String Decay',
           'Str Damping', 'Volume')
TNS_BANKS = (
 TNS_BANK1,
 TNS_BANK2,
 TNS_BANK3,
 TNS_BANK4,
 TNS_BANK5,
 TNS_BANK6,
 TNS_BANK7,
 TNS_BANK8)
TNS_BOBS = (
 TNS_BOB,)
TNS_BNK_NAMES = ('Exciter and String', 'Damper', 'Termination and Pickup', 'Body',
                 'Vibrato', 'Filter', 'Envelope and LFO', 'Global')
```
