#!/usr/bin/env python3
"""Usage: notes_to_ppal.py notes.json --src-beats 12 --src-unit 8 --dst-bar 1 [--first-bar 1] [--vel 56] [--transpose 0]
Convertit la sortie JSON de kern_to_notes.py en notation Producer Pal (C3 = 60), en mappant une mesure source sur une mesure 4/4 de destination.
--src-beats/--src-unit : signature source (12/8). Une mesure source = 4 noires de destination (facteur = 4 / (src_beats*4/src_unit)).
--dst-bar : mesure de clip où tombe la mesure source 1 (l'anacrouse, mesure 0, est placée avant). --first-bar : première mesure source à écrire."""
import sys, json
from fractions import Fraction as F
if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 else 2)

a = sys.argv[1:]; notes = json.load(open(a[0]))
def opt(k, d): return a[a.index(k) + 1] if k in a else d
sb, su = int(opt('--src-beats', 4)), int(opt('--src-unit', 4)); dst_bar = int(opt('--dst-bar', 2)); vel = int(opt('--vel', 60)); tr = int(opt('--transpose', 0)); first = int(opt('--first-bar', 0))
src_len = F(sb * 4, su)                # longueur d'une mesure source en noires
fact = F(4) / src_len                  # noires destination par noire source
NOMS = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
def abl(m): return NOMS[m % 12] + str(m // 12 - 2)
def dur_tok(q):                        # q en noires (Fraction) -> n<num>/<den> (fraction de ronde)
    r = q / 4
    return 'n/%d' % r.denominator if r.numerator == 1 else 'n%d/%d' % (r.numerator, r.denominator)
def pos_tok(q):                        # q en noires depuis le début du clip -> bar|beat
    bar = int(q // 4) + 1; beat = q - (bar - 1) * 4 + 1
    return '%d|%s' % (bar, ('%g' % float(beat)) if beat.denominator in (1, 2, 4, 8) else '%d+%s' % (int(beat), dur_tok((beat - int(beat)))))
m0 = [e for e in notes if e['mesure'] == 0 and not e['agrement']]
anacr = max((F(e['temps']).limit_denominator(64) + F(e['duree']).limit_denominator(64)) for e in m0) * fact if m0 else F(0)
decal0 = F(4) - anacr if anacr else F(0)        # l'anacrouse se termine pile sur le premier temps de la mesure 1
lines = []
for e in notes:
    if e['mesure'] < first or e['agrement']: continue
    q = F(dst_bar - 1) * 4 + (F(e['mesure'] - 1) * src_len + F(e['temps']).limit_denominator(64)) * fact
    if e['mesure'] == 0: q = F(dst_bar - 2) * 4 + decal0 + F(e['temps']).limit_denominator(64) * fact
    d = (F(e['duree']).limit_denominator(64) * fact) or F(1, 8)
    lines.append('v%d %s %s %s' % (vel, dur_tok(d), abl(e['midi'] + tr), pos_tok(q)))
print('\n'.join(lines))
