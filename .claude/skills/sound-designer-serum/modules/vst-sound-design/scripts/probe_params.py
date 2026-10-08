# Usage: pyl.sh probe_params.py — charge NOMS (VST3) sur la piste vide PISTE_IDX, liste le nombre de paramètres exposés, puis nettoie
NOMS = ['MetaFlanger Stereo']
PISTE_IDX = 36   # une piste audio vide du modèle
b = app.browser
vst3 = [c for c in b.plugins.children if c.name == 'VST3'][0]
found = {}
def walk(it, depth=0):
    for c in it.children:
        if c.name in NOMS: found[c.name] = c
        if c.is_folder and depth < 3: walk(c, depth + 1)
walk(vst3)
t = song.tracks[PISTE_IDX]
song.view.selected_track = t
for nm in NOMS:
    if t.devices: song.view.select_device(t.devices[-1])
    b.load_item(found[nm])
out = ['%s: %d params | %s' % (d.name, len(d.parameters), ' | '.join('%s=%s' % (p.name, p.str_for_value(p.value).strip()) for p in list(d.parameters)[1:25])) for d in t.devices]
for i in range(len(t.devices) - 1, -1, -1): t.delete_device(i)
result = "\n".join(out)
