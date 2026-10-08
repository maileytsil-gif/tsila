# Usage: pyl.sh test_clip.py — crée (ou supprime) un clip MIDI de test hors morceau sur une piste, pour rendre le candidat et l'analyser
# Éditer : PISTE, MESURE (hors arrangement, ex. 131), NOTES (MIDI), SUPPRIMER
PISTE, MESURE, NOTES, SUPPRIMER = 'SUB', 131, [29], False
by = {t.name: t for t in song.tracks}; t = by[PISTE]
B = lambda bar: (bar - 1) * 4.0
if SUPPRIMER:
    for c in list(t.arrangement_clips):
        if c.start_time >= B(MESURE): t.delete_clip(c)
    result = 'clips de test supprimés sur %s à partir de %d' % (PISTE, MESURE)
else:
    # note de 2 s (4 temps) puis 2 s de silence, par note, dans un clip de session temporaire copié en arrangement
    slot = t.clip_slots[0]
    if slot.has_clip: slot.delete_clip()
    slot.create_clip(8.0 * len(NOTES)); c = slot.clip
    import Live
    specs = [Live.Clip.MidiNoteSpecification(pitch=p, start_time=8.0 * i, duration=4.0, velocity=100, mute=False) for i, p in enumerate(NOTES)]
    c.add_new_notes(tuple(specs)); c.name = 'TEST synthese-reference'
    new = t.duplicate_clip_to_arrangement(c, B(MESURE)); slot.delete_clip()
    result = 'clip de test sur %s : mesure %d, notes %s, %g s par note + silence — exporter cette plage (Piste convertie = %s) puis analyze_synth.py' % (PISTE, MESURE, NOTES, 2.0, PISTE)
