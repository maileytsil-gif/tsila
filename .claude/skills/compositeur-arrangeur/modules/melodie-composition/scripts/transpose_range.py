# Usage: pyl.sh transpose_range.py — transpose toutes les notes des PISTES entre A et Bm de DELTA demi-tons
PISTES = ['CHORDS', 'PAD', 'HOOK', 'BASS', 'SUB', 'TEX']
A, Bm, DELTA = 81, 89, 5
by = {t.name: t for t in song.tracks}
B = lambda bar: (bar - 1) * 4.0
out = []
for nm in PISTES:
    nb = 0
    for c in by[nm].arrangement_clips:
        if c.end_time <= B(A) or c.start_time >= B(Bm): continue
        notes = c.get_notes_extended(0, 128, 0, 100000); touche = False
        for n in notes:
            ta = c.start_time + (n.start_time - c.start_marker)
            if B(A) <= ta < B(Bm) and c.start_time <= ta < c.end_time:
                n.pitch = max(0, min(127, n.pitch + DELTA)); touche = True; nb += 1
        if touche: c.apply_note_modifications(notes)
    out.append('%s: %d notes %+d' % (nm, nb, DELTA))
result = "\n".join(out)
