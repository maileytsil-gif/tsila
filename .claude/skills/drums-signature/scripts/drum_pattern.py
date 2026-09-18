#!/usr/bin/env python3
"""Usage: drum_pattern.py <house|techhouse|melodictechno|techno|dnb|electro> [--bars 8] [--variant A|B] [--fixe]
Génère un pattern de batterie en notation Producer Pal (kick C1, clap/snare D1, hat fermé F#1, hat ouvert A#1, perc C2/D2/E2 selon le kit),
avec ghosts, variation toutes les 4 mesures et fill sur la dernière ; imprime aussi la ligne `transforms` (swing).
--variant B : accents déplacés (clap anticipé, open hat sur le 3) pour une seconde version du même pattern.
--fixe : vélocités fixes (une valeur par rôle) au lieu de plages vN-M, conformément à la règle « pas d'humanisation aléatoire »."""
import sys
def opt(k, d): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
if len(sys.argv) < 2 or sys.argv[1].startswith('-'):
    print(__doc__); raise SystemExit(0 if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help') else 2)
g = sys.argv[1]
bars = int(opt('--bars', 8)); variant = opt('--variant', 'A').upper(); fixe = '--fixe' in sys.argv
ALIAS = {'deep': 'house', 'deephouse': 'house', 'minimal': 'house', 'tech': 'techhouse', 'techhouse': 'techhouse',
         'melodic': 'melodictechno', 'melodic-techno': 'melodictechno', 'drumandbass': 'dnb', 'dandb': 'dnb'}
L = []
def v(a, b): return 'v%d' % round((a + b) / 2) if fixe else 'v%d-%d' % (a, b)
G_DOC = 'house, techhouse, melodictechno, techno, dnb, electro'
g = ALIAS.get(g.lower().replace('_', '').replace('-', ''), g.lower())
if variant not in ('A', 'B'):
    raise SystemExit('--variant attend A ou B')
GENRES = {
 'melodictechno': {'kick': ([1, 2, 3, 4], 100, 108), 'clap': ([2, 4], 62, 72), 'hat': ([1.5, 2.5, 3.5, 4.5], 66, 76), 'ghost': ([1.25, 2.75, 3.25, 4.75], 30, 42), 'open': ([4.5], 56, 64), 'swing': 0.0, 'perc': ([2.25, 3.75], 38, 52)},
 'house':     {'kick': ([1, 2, 3, 4], 104, 112), 'clap': ([2, 4], 70, 82), 'hat': ([1.5, 2.5, 3.5, 4.5], 70, 80), 'ghost': ([1.75, 2.75, 3.75], 28, 40), 'open': ([4.5], 58, 66), 'swing': 0.03, 'perc': ([2.5, 4.25], 40, 55)},
 'techhouse': {'kick': ([1, 2, 3, 4], 108, 116), 'clap': ([2, 4], 86, 94), 'hat': ([1.5, 2.5, 3.5, 4.5], 82, 90), 'ghost': ([1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75], 30, 42), 'open': ([4.5], 64, 72), 'swing': 0.04, 'perc': ([1.75, 3.5], 60, 72)},
 'techno':    {'kick': ([1, 2, 3, 4], 110, 118), 'clap': ([2, 4], 88, 96), 'hat': ([1 + i * 0.25 for i in range(16)], 60, 80), 'ghost': ([], 0, 0), 'open': ([1.5, 2.5, 3.5, 4.5], 60, 70), 'swing': 0.0, 'perc': ([], 0, 0)},
 'dnb':       {'kick': ([1, 3.5], 110, 118), 'clap': ([2, 4], 100, 110), 'hat': ([1 + i * 0.5 for i in range(8)], 70, 84), 'ghost': ([1.75, 3.25, 4.75], 30, 45), 'open': ([2.5], 56, 64), 'swing': 0.02, 'perc': ([], 0, 0)},
 'electro':   {'kick': ([1, 2.5, 3.75], 108, 116), 'clap': ([2, 4], 96, 104), 'hat': ([1 + i * 0.25 for i in range(16)], 55, 76), 'ghost': ([], 0, 0), 'open': ([2.5, 4.5], 66, 74), 'swing': 0.0, 'perc': ([3.25], 45, 55)},
}
if g not in GENRES:
    raise SystemExit('genre inconnu : %s (connus : %s)' % (sys.argv[1], G_DOC))
G = {k: (list(vv[0]), vv[1], vv[2]) for k, vv in GENRES[g].items() if k != 'swing'}
G['swing'] = GENRES[g]['swing']
G['kick'] = (list(GENRES[g]['kick'][0]), GENRES[g]['kick'][1], GENRES[g]['kick'][2])
if variant == 'B':                      # seconde version : accents déplacés, pas un tirage au sort
    if G['clap'][0] == [2, 4]: G['clap'] = ([1.75, 4], G['clap'][1], G['clap'][2])   # clap anticipé sur le 2
    if G['open'][0]: G['open'] = ([3.5] if G['open'][0] == [4.5] else G['open'][0], G['open'][1], G['open'][2])
    if G['ghost'][0]: G['ghost'] = (G['ghost'][0][:-1] or G['ghost'][0], G['ghost'][1], G['ghost'][2])
def beats(lst): return ','.join(('%g' % b) for b in lst)
if G['kick'][0]: L.append('%s n/8 C1 1|%s' % (v(*G['kick'][1:]), beats(G['kick'][0])))
if G['clap'][0]: L.append('%s n/16 D1 1|%s' % (v(*G['clap'][1:]), beats(G['clap'][0])))
if G['hat'][0]:
    if g in ('techno', 'electro'): L.append('[v90 v58 v72 v58] n/16 F#1 1|1x16')
    elif g == 'dnb': L.append('%s n/16 F#1 1|1x8@n/8' % v(*G['hat'][1:]))
    else: L.append('%s n/16 F#1 1|%s' % (v(*G['hat'][1:]), beats(G['hat'][0])))
if G['ghost'][0]: L.append('%s n/16 %s 1|%s' % (v(*G['ghost'][1:]), 'D1' if g == 'dnb' else 'F#1', beats(G['ghost'][0])))
if G['open'][0]: L.append('%s n/16 A#1 1|%s' % (v(*G['open'][1:]), beats(G['open'][0])))
if G['perc'][0]: L.append('%s n/16 C2 1|%s' % (v(*G['perc'][1:]), beats(G['perc'][0])))
if g == 'electro': L.append('%s n/8 C1 2|1,2.5,4' % v(*G['kick'][1:])); L.append('@3-%d=1-2' % bars)
else: L.append('@2-%d=1' % bars)
# variations toutes les 4 mesures + fill final
for b in range(4, bars + 1, 4):
    if g in ('house', 'techhouse') and b < bars: L.append('v0 F#1 %d|3.75 v100' % b)           # un ghost en moins
    if g == 'techno' and b < bars: L.append('v0 D1 %d|4 v100' % b)                            # clap retiré
    if g == 'electro' and b < bars: L.append('v0 C1 %d|3.75 v100' % b)                        # silence voulu
if g == 'dnb': L.append('%s n/16 D1 %d|4.25,4.5,4.75' % (v(70, 96), bars))
elif g == 'house': L.append('%s n/16 A#1 %d|4.75' % (v(60, 70), bars))
else: L.append('%s n/16 D1 %d|4.5,4.75' % (v(80, 100), bars))
print('\n'.join(L)); print('--- transforms ---')
print('timing = swing(%g, n/16)' % G['swing'] if G['swing'] else '(pas de swing)')
if g == 'techhouse': print('4|4.75: ratchet(2)')
print('--- note --- genre %s, variante %s, %d mesures, vélocités %s ; kick exact sur les downbeats, relire le clip après création (ppal-read-clip)' % (g, variant, bars, 'fixes' if fixe else 'en plages (tirage de Producer Pal) — --fixe pour un motif répété'))
