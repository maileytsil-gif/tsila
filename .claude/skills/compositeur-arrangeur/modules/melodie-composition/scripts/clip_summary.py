# Usage: pyl.sh clip_summary.py  (éditer PISTES/A/B en tête) — résumé lisible des notes par mesure (accords regroupés par temps)
PISTES = ['CHORDS', 'HOOK', 'BASS']   # noms de pistes
A, Bm = 81, 89                          # mesures [A, B)
NOMS = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
by = {t.name: t for t in song.tracks}
B = lambda bar: (bar - 1) * 4.0
def nom(p): return NOMS[p % 12] + str(p // 12 - 2)
out = []
for nm in PISTES:
    t = by[nm]; par = {}
    for c in t.arrangement_clips:
        if c.end_time <= B(A) or c.start_time >= B(Bm): continue
        for n in c.get_notes_extended(0, 128, 0, 100000):
            ta = c.start_time + (n.start_time - c.start_marker)
            if B(A) <= ta < B(Bm) and c.start_time <= ta < c.end_time:
                bar = int(ta // 4) + 1
                par.setdefault(bar, {}).setdefault(round(ta - B(bar), 2), []).append((nom(n.pitch), n.velocity))
    out.append('== %s ==' % nm)
    for bar in sorted(par):
        out.append('%d: ' % bar + ' ; '.join('%g[%s]' % (t0, ' '.join(p for p, v in sorted(v_))) for t0, v_ in sorted(par[bar].items())))
result = "\n".join(out)
