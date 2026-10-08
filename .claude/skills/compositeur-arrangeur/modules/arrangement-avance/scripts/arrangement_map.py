# Usage: pyl.sh arrangement_map.py — carte piste x sections (clips, notes), repères, durée
reps = sorted([(c.time, c.name) for c in song.cue_points])
bornes = [t for t, _ in reps]
out = ['REPÈRES: ' + ', '.join('%s@%g' % (n, t / 4 + 1) for t, n in reps)]
fin = max([c.end_time for t in song.tracks for c in t.arrangement_clips] + [0])
out.append('dernier clip: mesure %g  (%.2f s à %g BPM)' % (fin / 4 + 1, fin * 60 / song.tempo, song.tempo))
for t in song.tracks:
    cl = sorted(t.arrangement_clips, key=lambda c: c.start_time)
    if not cl: continue
    cells = []
    for i, deb in enumerate(bornes):
        finb = bornes[i + 1] if i + 1 < len(bornes) else 1e9
        k = [c for c in cl if c.start_time < finb and c.end_time > deb]
        if not k: cells.append('.'); continue
        nn = sum(len(c.get_notes_extended(0, 128, 0, 100000)) for c in k if c.is_midi_clip)
        cells.append('%d%s' % (len(k), ('/%dn' % nn) if nn else ''))
    out.append('%-24s ' % t.name[:24] + ' '.join('%6s' % c for c in cells))
result = "\n".join(out)
