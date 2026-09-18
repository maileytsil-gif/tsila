# Usage: pyl.sh check_scale.py — liste les notes hors gamme.
# Paramètres : éditer une COPIE dans le scratchpad (ne pas modifier le skill : les deux installations divergeraient),
# ou définir ARGS avant l'appel : ARGS = "F G Ab Bb C Db Eb | HOOK CHORDS | 1 129".
# Hors Live, pour vérifier une progression écrite : ../theorie-musicale-electronique/scripts/theorie.py progression.
GAMME = ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb']
PISTES = ['HOOK', 'CHORDS', 'PAD', 'BASS', 'SUB', 'PIANO']
A, Bm = 1, 129
try:                                  # ARGS optionnel, défini par pyl.sh ou le script appelant
    _g, _p, _b = [x.strip() for x in ARGS.split('|')]
    GAMME = _g.split(); PISTES = _p.split(); A, Bm = [int(x) for x in _b.split()]
except (NameError, ValueError):
    pass
NOMS = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
ok = {NOMS.index(g) for g in GAMME}
by = {t.name: t for t in song.tracks}
B = lambda bar: (bar - 1) * 4.0
out = []
for nm in PISTES:
    if nm not in by: continue
    hors = {}
    for c in by[nm].arrangement_clips:
        for n in c.get_notes_extended(0, 128, 0, 100000):
            ta = c.start_time + (n.start_time - c.start_marker)
            if B(A) <= ta < B(Bm) and c.start_time <= ta < c.end_time and n.pitch % 12 not in ok:
                hors.setdefault(int(ta // 4) + 1, set()).add(NOMS[n.pitch % 12])
    out.append('%s: %s' % (nm, ' '.join('%d[%s]' % (b, ','.join(sorted(s))) for b, s in sorted(hors.items())) or 'tout dans la gamme'))
result = "\n".join(out)
