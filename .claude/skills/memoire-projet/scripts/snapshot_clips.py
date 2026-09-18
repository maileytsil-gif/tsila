# À lancer dans Live via ableton-live-session/scripts/pyl.sh : instantané JSON de toutes les pistes MIDI
# (clips d'arrangement, notes visibles en temps absolus, faders, envois). Chemin de sortie dans `result`.
import json, os, time
out_dir = os.path.expanduser('~/.claude/snapshots'); os.makedirs(out_dir, exist_ok=True)
snap = {'set': song.name if hasattr(song, 'name') else '', 'date': time.strftime('%Y-%m-%d %H:%M:%S'), 'tracks': {}}
for t in song.tracks:
    m = t.mixer_device
    entry = {'volume': m.volume.str_for_value(m.volume.value), 'sends': [s.str_for_value(s.value) for s in m.sends], 'clips': []}
    if t.has_midi_input:
        for c in sorted(t.arrangement_clips, key=lambda c: c.start_time):
            if not c.is_midi_clip: continue
            vis = [[round(c.start_time + (n.start_time - c.start_marker), 4), round(n.duration, 4), n.pitch, int(n.velocity)] for n in c.get_notes_extended(0, 128, 0, 100000) if c.start_marker <= n.start_time < c.start_marker + (c.end_time - c.start_time)]
            entry['clips'].append({'name': c.name, 'start': c.start_time, 'end': c.end_time, 'notes': sorted(vis)})
    snap['tracks'][t.name] = entry
path = os.path.join(out_dir, time.strftime('snapshot-%Y%m%d-%H%M%S.json'))
json.dump(snap, open(path, 'w'))
result = [path, len(snap['tracks']), sum(len(e['clips']) for e in snap['tracks'].values())]
