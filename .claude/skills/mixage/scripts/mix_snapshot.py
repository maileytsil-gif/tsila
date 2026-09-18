# Usage: pyl.sh mix_snapshot.py — carte du mix : fader, pan, envois, devices, sortie, pour pistes / retours / master
def f(p): return p.str_for_value(p.value).strip()
out = []
for t in list(song.tracks) + list(song.return_tracks) + [song.master_track]:
    m = t.mixer_device
    envs = ' '.join('%s' % f(s) for s in m.sends) if hasattr(m, 'sends') else ''
    try: sortie = t.output_routing_type.display_name
    except Exception: sortie = '-'
    auto = '*' if m.volume.automation_state else ''
    out.append('%-24s vol %7s%s pan %5s | env %s | -> %-15s | %s' % (t.name[:24], f(m.volume), auto, f(m.panning), envs, sortie[:15], ' > '.join(d.name[:14] for d in t.devices) or '(vide)'))
result = "\n".join(out)
