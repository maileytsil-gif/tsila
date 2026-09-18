# Usage: pyl.sh expression_report.py — rapport d'expression d'une piste sur [A, Bm)
PISTE, A, Bm = 'PIANO', 1, 25
REGISTRE = {'PIANO': (21, 108), 'BASS': (28, 60), 'SUB': (24, 48), 'HOOK': (48, 96), 'CHORDS': (48, 84), 'PAD': (36, 84)}
NOMS = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
nom = lambda p: NOMS[p % 12] + str(p // 12 - 2)
t = [x for x in song.tracks if x.name == PISTE][0]
B = lambda bar: (bar - 1) * 4.0
lo, hi = REGISTRE.get(PISTE, (0, 127))
out = []
for c in sorted(t.arrangement_clips, key=lambda c: c.start_time):
    if c.end_time <= B(A) or c.start_time >= B(Bm) or not c.is_midi_clip: continue
    ns = [n for n in c.get_notes_extended(0, 128, 0, 100000)]
    if not ns: continue
    v = [n.velocity for n in ns]; d = [n.duration for n in ns]
    grille8 = sum(1 for n in ns if abs((n.start_time * 2) - round(n.start_time * 2)) < 0.02) / len(ns)
    chev = 0
    par_p = {}
    for n in ns: par_p.setdefault(n.pitch, []).append(n)
    for p, l in par_p.items():
        l.sort(key=lambda n: n.start_time)
        for a, b in zip(l, l[1:]):
            if a.start_time + a.duration > b.start_time + 1e-4: chev += 1
    hors = sorted(set(nom(n.pitch) for n in ns if n.pitch < lo or n.pitch > hi))
    out.append('%s %g-%g : %d notes | vel %d/%.0f/%d | durée %.2f..%.2f (moy %.2f) | sur grille croche %.0f%% | chevauchements même hauteur %d | hors registre %s' % (
        c.name[:28], c.start_time / 4 + 1, c.end_time / 4 + 1, len(ns), min(v), sum(v) / len(v), max(v), min(d), max(d), sum(d) / len(d), grille8 * 100, chev, hors or '-'))
result = "\n".join(out) or 'aucun clip MIDI dans la fenêtre'
