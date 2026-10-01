---
titre: "mikeb55 Big-Band-Arranging — build_v32_chorus2_realranges.py : tessitures réelles par pupitre (music21)"
source: https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/build_v32_chorus2_realranges.py
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: big band ; tessitures
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

```python
#!/usr/bin/env python3
"""
V32 Beatrice - Chorus 2 Real Ranges, Real Melody
Idiomatic wind ranges, one singable melody always, lyrical counterlines,
restrained ballad texture. No fake full-band occupation.
"""
import xml.etree.ElementTree as ET
from pathlib import Path
from music21 import (
    converter, stream, note, chord, harmony, expressions, articulations,
    pitch, instrument, tempo, metadata, clef
)

BASE = Path(__file__).resolve().parent
OUT_PATH = BASE / "session 6" / "Beatrice w Bora Assistance" / "V32-Beatrice-Chorus-2-RealRanges-RealMelody.musicxml"
MELODY_PATH = BASE / "Session 2" / "Assignment Session 2" / "V4.6-Beatrice-Session2-Reharm-3-Choruses.musicxml"

CHORD_MAP = {
    1: "Fmaj7", 2: "G-maj7", 3: "Fmaj7", 4: "E-maj7",
    5: "Dm7", 6: "G-7", 7: "Dm7", 8: "B-m7",
    9: "Am7", 10: "G-maj7", 11: "A7", 12: "Dm7",
    13: "Gm7", 14: "C7", 15: "Fm7", 16: "G-maj7",
    17: "Fmaj7", 18: "G-maj7", 19: "Fmaj7", 20: "E-maj7",
    21: "Dm7", 22: "G-7", 23: "Dm7", 24: "B-m7",
    25: "Am7", 26: "G-maj7", 27: "A7", 28: "Dm7",
    29: "Gm7", 30: "G-7", 31: "Fm7", 32: "G-maj7",
}

# Conservative, ballad-appropriate ranges (written pitch MIDI)
# Alto: comfortable mid, avoid palm keys. Tenor: warm middle. Bari: low grounding only.
# Trumpet: middle, lyrical. Trombone: singing register.
RANGES = {
    "Alto1": (60, 74), "Alto2": (60, 74),
    "Ten1": (55, 70), "Ten2": (55, 70),
    "Bari": (36, 50),
    "Tpt1": (58, 74), "Tpt2": (58, 74), "Tpt3": (55, 72), "Tpt4": (55, 70),
    "Tbn1": (45, 65), "Tbn2": (45, 63), "Tbn3": (43, 60), "TbnBass": (34, 50),
}

def clamp(p, lo, hi):
    m = p.midi
    return pitch.Pitch(lo if m < lo else (hi if m > hi else m))

def c2bb(p): return p.transpose(2)
def c2alto(p): return p.transpose(-9)
def c2tenor(p): return p.transpose(-14)
def c2bari(p): return p.transpose(-21)

def chord_to_pitches(cs):
    fallback = [pitch.Pitch("F4"), pitch.Pitch("A4"), pitch.Pitch("C5"), pitch.Pitch("E5")]
    if not cs:
        return fallback
    s = str(cs).replace("G-", "Gb").replace("E-", "Eb").replace("B-", "Bb").replace("A-", "Ab")
    s = s.replace("Em7b5", "E-7b5").replace("Eø", "E-7b5")
    for old, new in [("ø", "7b5"), ("half-diminished", "7b5")]:
        s = s.replace(old, new)
    try:
        p = list(chord.Chord(s).pitches)
        if len(p) >= 4:
            return p
    except Exception:
        pass
    return fallback

def half_note_bass(root, next_root):
    r = pitch.Pitch(root.midi)
    r.octave = 2
    nxt = pitch.Pitch(next_root.midi) if next_root else r
    nxt.octave = 2
    return [r, nxt]

def walking_bass(root, next_root):
    r = pitch.Pitch(root.midi)
    r.octave = 2
    notes = [r, r, r, r]
    if next_root:
        nxt = pitch.Pitch(next_root.midi)
        nxt.octave = 2
        if abs(nxt.midi - r.midi) <= 5:
            approach = pitch.Pitch(nxt.midi - 1 if nxt.midi > r.midi else nxt.midi + 1)
            approach.octave = 2
            notes[3] = approach
    return notes

def get_melody():
    mel = {}
    try:
        score = converter.parse(str(MELODY_PATH))
        for m in score.parts[0].getElementsByClass(stream.Measure):
            if 17 <= m.measureNumber <= 32:
                notes = []
                for n in m.notesAndRests:
                    if not n.isRest and hasattr(n, 'pitch') and n.pitch:
                        off = float(n.offset)
                        notes.append((off, note.Note(n.pitch)))
                    elif hasattr(n, 'pitches') and n.pitches:
                        off = float(n.offset)
                        notes.append((off, note.Note(n.pitches[-1])))
                mel[m.measureNumber] = notes
    except Exception:
        pass
    return mel

def tbn1_lyrical_counterline(bar, r, t, f, s):
    """Trombone 1: slow half notes, stepwise, opposite contour to trumpet. Bars 5-8 only."""
    def ok(pt):
        if pt.midi < 45:
            return pt.transpose(12)
        if pt.midi > 65:
            return pt.transpose(-12)
        return pt
    if bar == 5:
        return [(0, ok(s.transpose(12)), 2), (2, ok(t.transpose(12)), 2)]
    if bar == 6:
        return [(0, ok(t.transpose(12)), 2), (2, ok(r.transpose(12)), 2)]
    if bar == 7:
        return [(0, ok(r.transpose(12)), 2), (2, ok(t), 2)]
    if bar == 8:
        return [(0, ok(t), 2), (2, ok(s), 2)]
    return None

def create_score():
    melody = get_melody()

    part_config = [
        ("P1", "Alto Saxophone", "Alto Sax.", instrument.AltoSaxophone(), c2alto, "Alto1"),
        ("P2", "Alto Saxophone", "Alto Sax.", instrument.AltoSaxophone(), c2alto, "Alto2"),
        ("P3", "Tenor Saxophone", "Ten. Sax.", instrument.TenorSaxophone(), c2tenor, "Ten1"),
        ("P4", "Tenor Saxophone", "Ten. Sax.", instrument.TenorSaxophone(), c2tenor, "Ten2"),
        ("P5", "Baritone Saxophone", "Bari. Sax.", instrument.BaritoneSaxophone(), c2bari, "Bari"),
        ("P6", "Trumpet in Bb", "Tpt.", instrument.Trumpet(), c2bb, "Tpt1"),
        ("P7", "Trumpet in Bb", "Tpt.", instrument.Trumpet(), c2bb, "Tpt2"),
        ("P8", "Trumpet in Bb", "Tpt.", instrument.Trumpet(), c2bb, "Tpt3"),
        ("P9", "Trumpet in Bb", "Tpt.", instrument.Trumpet(), c2bb, "Tpt4"),
        ("P10", "Trombone", "Tbn.", instrument.Trombone(), lambda p: p, "Tbn1"),
        ("P11", "Trombone", "Tbn.", instrument.Trombone(), lambda p: p, "Tbn2"),
        ("P12", "Trombone", "Tbn.", instrument.Trombone(), lambda p: p, "Tbn3"),
        ("P13", "Bass Trombone", "B. Tbn.", instrument.BassTrombone(), lambda p: p, "TbnBass"),
        ("P14", "Piano", "Pno.", instrument.Piano(), lambda p: p, None),
        ("P15", "Acoustic Bass", "A. Bass", instrument.AcousticBass(), lambda p: p, None),
        ("P16", "Drum Set", "Dr.", instrument.Percussion(), lambda p: p, None),
    ]

    parts = {}
    for pid, pname, pabbr, inst, trans_fn, rng_key in part_config:
        p = stream.Part(id=pid)
        p.partName = pname
        p.partAbbreviation = pabbr
        p.insert(0, inst)
        if pid == "P16":
            p.insert(0, clef.PercussionClef())
        parts[pid] = (p, trans_fn, rng_key)

    for bar in range(1, 33):
        bn = bar + 16
        cs = CHORD_MAP.get(bar, "Fmaj7")
        next_cs = CHORD_MAP.get(bar + 1, "Fmaj7") if bar < 32 else None
        pitches = chord_to_pitches(cs)
        next_pitches = chord_to_pitches(next_cs) if next_cs else None
        mel_notes = melody.get(bn, [])
        r, t, f, s = pitches[0], pitches[1], pitches[2], pitches[3]

        for pid, (part, trans_fn, rng_key) in parts.items():
            mg = stream.Measure(number=bar)
            if bar == 1:
                mg.insert(0, expressions.RehearsalMark("Chorus 2"))
                mg.insert(0, tempo.MetronomeMark(number=72))
            mg.insert(0, harmony.ChordSymbol(cs))

            idx = list(parts.keys()).index(pid)
            is_alto1, is_alto2 = idx == 0, idx == 1
            is_ten1, is_ten2 = idx == 2, idx == 3
            is_bari = idx == 4
            is_sax = idx < 5
            is_tpt1, is_tpt2 = idx == 5, idx == 6
            is_trumpet = 5 <= idx < 9
            is_tbn1 = idx == 9
            is_trombone = 9 <= idx < 13
            is_piano = idx == 13
            is_bass = idx == 14
            is_drums = idx == 15

            def add_piano_chord():
                rp, tp, fp, sp = pitch.Pitch(r.midi), pitch.Pitch(t.midi), pitch.Pitch(f.midi), pitch.Pitch(s.midi)
                rp.octave = 3
                sp.octave = 3
                tp.octave = 4
                fp.octave = 4
                mg.append(chord.Chord([rp, sp, tp, fp], quarterLength=4))

            def add_bass():
                if bar <= 8 or bar >= 13:
                    for i, pt in enumerate(half_note_bass(r, next_pitches[0] if next_pitches else None)):
                        mg.insert(i * 2, note.Note(pt, quarterLength=2))
                else:
                    for i, bn in enumerate(walking_bass(r, next_pitches[0] if next_pitches else None)):
                        mg.insert(i, note.Note(bn, quarterLength=1))

            # BARS 1-2: Alto melody + rhythm only
            if 1 <= bar <= 2:
                if is_alto1:
                    if mel_notes:
                        for off, n in mel_notes:
                            p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                            mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                    else:
                        p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                        mg.append(note.Note(p, quarterLength=4))
                elif is_sax or is_trumpet or is_trombone:
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BARS 3-4: Add light sax support + one trombone counterline
            elif 3 <= bar <= 4:
                if is_alto1:
                    if mel_notes:
                        for off, n in mel_notes:
                            p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                            mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                    else:
                        p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                        mg.append(note.Note(p, quarterLength=4))
                elif is_alto2:
                    p = clamp(trans_fn(t.transpose(12)), RANGES["Alto2"][0], RANGES["Alto2"][1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_tbn1:
                    pt = clamp(t.transpose(12) if t.transpose(12).midi >= 45 else t.transpose(24), RANGES["Tbn1"][0], RANGES["Tbn1"][1])
                    mg.insert(0, note.Note(pt, quarterLength=2))
                    pt2 = clamp(s.transpose(12), RANGES["Tbn1"][0], RANGES["Tbn1"][1])
                    mg.insert(2, note.Note(pt2, quarterLength=2))
                elif is_sax or is_trumpet or is_trombone:
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BARS 5-6: Trumpet 2 melody + Trombone 1 lyrical answer
            elif 5 <= bar <= 6:
                if is_tpt2:
                    if mel_notes:
                        for off, n in mel_notes:
                            p = clamp(c2bb(n.pitch), RANGES["Tpt2"][0], RANGES["Tpt2"][1])
                            mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                    else:
                        p = clamp(c2bb(f.transpose(12)), RANGES["Tpt2"][0], RANGES["Tpt2"][1])
                        mg.append(note.Note(p, quarterLength=4))
                elif is_tbn1:
                    ctr = tbn1_lyrical_counterline(bar, r, t, f, s)
                    if ctr:
                        for off, pt, ql in ctr:
                            p = clamp(pt, RANGES["Tbn1"][0], RANGES["Tbn1"][1])
                            nn = note.Note(p, quarterLength=ql)
                            nn.articulations.append(articulations.Tenuto())
                            mg.insert(off, nn)
                    else:
                        mg.append(note.Rest(quarterLength=4))
                elif is_sax or (is_trumpet and not is_tpt2) or (is_trombone and not is_tbn1):
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BARS 7-8: Trumpet melody continues, trombones pad softly, saxes out
            elif 7 <= bar <= 8:
                if is_tpt2:
                    if mel_notes:
                        for off, n in mel_notes:
                            p = clamp(c2bb(n.pitch), RANGES["Tpt2"][0], RANGES["Tpt2"][1])
                            mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                    else:
                        p = clamp(c2bb(f.transpose(12)), RANGES["Tpt2"][0], RANGES["Tpt2"][1])
                        mg.append(note.Note(p, quarterLength=4))
                elif is_tbn1:
                    ctr = tbn1_lyrical_counterline(bar, r, t, f, s)
                    if ctr:
                        for off, pt, ql in ctr:
                            p = clamp(pt, RANGES["Tbn1"][0], RANGES["Tbn1"][1])
                            nn = note.Note(p, quarterLength=ql)
                            nn.articulations.append(articulations.Tenuto())
                            mg.insert(off, nn)
                    else:
                        mg.append(note.Rest(quarterLength=4))
                elif is_trombone and not is_tbn1:
                    tb = [s.transpose(12), f.transpose(12), t.transpose(12), r]
                    for i, pt in enumerate(tb):
                        if pt.midi < 43:
                            tb[i] = pt.transpose(12)
                        elif pt.midi > 65:
                            tb[i] = pt.transpose(-12)
                    rng = [RANGES["Tbn2"], RANGES["Tbn3"], RANGES["TbnBass"]][idx - 10]
                    p = clamp(tb[idx - 9], rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_sax or is_trumpet:
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BARS 9-10: Tenor or Alto melody + muted trumpet response
            elif 9 <= bar <= 10:
                if is_ten1:
                    if mel_notes:
                        for off, n in mel_notes:
                            p = clamp(trans_fn(n.pitch), RANGES["Ten1"][0], RANGES["Ten1"][1])
                            mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                    else:
                        p = clamp(trans_fn(f.transpose(12)), RANGES["Ten1"][0], RANGES["Ten1"][1])
                        mg.append(note.Note(p, quarterLength=4))
                elif is_tpt1:
                    p = clamp(c2bb(s.transpose(12)), RANGES["Tpt1"][0], RANGES["Tpt1"][1])
                    mg.insert(2, note.Note(p, quarterLength=2))
                    mg.insert(0, note.Rest(quarterLength=2))
                elif is_sax and not is_ten1:
                    mg.append(note.Rest(quarterLength=4))
                elif is_trumpet and not is_tpt1:
                    mg.append(note.Rest(quarterLength=4))
                elif is_trombone:
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BARS 11-12: Small sax choir, very light brass halo
            elif 11 <= bar <= 12:
                if is_alto1 and mel_notes:
                    for off, n in mel_notes:
                        p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                        mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                elif is_alto1:
                    p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                    mg.append(note.Note(p, quarterLength=4))
                elif is_alto2 or is_ten2 or is_ten1:
                    inner = t.transpose(12) if is_alto2 else (s.transpose(12) if is_ten1 else s.transpose(12))
                    rng = RANGES["Alto2"] if is_alto2 else (RANGES["Ten1"] if is_ten1 else RANGES["Ten2"])
                    p = clamp(trans_fn(inner), rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_bari:
                    p = clamp(c2bari(r), RANGES["Bari"][0], RANGES["Bari"][1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_ten1:
                    p = clamp(trans_fn(s.transpose(12)), RANGES["Ten1"][0], RANGES["Ten1"][1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trumpet and bar == 12:
                    p = clamp(c2bb(f.transpose(12)), RANGES["Tpt3"][0], RANGES["Tpt3"][1])
                    mg.insert(2, note.Note(p, quarterLength=2))
                    mg.insert(0, note.Rest(quarterLength=2))
                elif is_trumpet or is_trombone:
                    if is_trombone and bar == 12:
                        p = clamp(s.transpose(12) if s.transpose(12).midi >= 45 else s.transpose(24), RANGES["Tbn1"][0], RANGES["Tbn1"][1])
                        nn = note.Note(p, quarterLength=4)
                        nn.articulations.append(articulations.Tenuto())
                        mg.append(nn)
                    else:
                        mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BAR 13: Sax melody + brass pad
            elif bar == 13:
                if is_alto1 and mel_notes:
                    for off, n in mel_notes:
                        p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                        mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                elif is_alto1:
                    p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                    mg.append(note.Note(p, quarterLength=4))
                elif is_sax and not is_alto1:
                    voicing = [f.transpose(12), s.transpose(12), r.transpose(12), t, r]
                    rng = [RANGES["Alto2"], RANGES["Ten1"], RANGES["Ten2"], RANGES["Bari"]][idx - 1]
                    p = clamp(trans_fn(voicing[idx - 1]), rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trombone:
                    tb = [s.transpose(12), f.transpose(12), t.transpose(12), r]
                    for i, pt in enumerate(tb):
                        if pt.midi < 43:
                            tb[i] = pt.transpose(12)
                        elif pt.midi > 65:
                            tb[i] = pt.transpose(-12)
                    rng = [RANGES["Tbn1"], RANGES["Tbn2"], RANGES["Tbn3"], RANGES["TbnBass"]][idx - 9]
                    p = clamp(tb[idx - 9], rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trumpet:
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BAR 14: Add trumpets softly
            elif bar == 14:
                if is_alto1 and mel_notes:
                    for off, n in mel_notes:
                        p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                        mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                elif is_alto1:
                    p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                    mg.append(note.Note(p, quarterLength=4))
                elif is_sax and not is_alto1:
                    voicing = [f.transpose(12), s.transpose(12), r.transpose(12), t, r]
                    rng = [RANGES["Alto2"], RANGES["Ten1"], RANGES["Ten2"], RANGES["Bari"]][idx - 1]
                    p = clamp(trans_fn(voicing[idx - 1]), rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trumpet:
                    tb = [s.transpose(12), f.transpose(12), t.transpose(12), r.transpose(12)]
                    rng = [RANGES["Tpt1"], RANGES["Tpt2"], RANGES["Tpt3"], RANGES["Tpt4"]][idx - 5]
                    p = clamp(c2bb(tb[idx - 5]), rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trombone:
                    tb = [s.transpose(12), f.transpose(12), t.transpose(12), r]
                    for i, pt in enumerate(tb):
                        if pt.midi < 43:
                            tb[i] = pt.transpose(12)
                        elif pt.midi > 65:
                            tb[i] = pt.transpose(-12)
                    rng = [RANGES["Tbn1"], RANGES["Tbn2"], RANGES["Tbn3"], RANGES["TbnBass"]][idx - 9]
                    p = clamp(tb[idx - 9], rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BAR 15: Single controlled full-band swell
            elif bar == 15:
                if is_sax:
                    voicing = [f.transpose(12), s.transpose(12), r.transpose(12), t, r]
                    rng = [RANGES["Alto1"], RANGES["Alto2"], RANGES["Ten1"], RANGES["Ten2"], RANGES["Bari"]][idx]
                    p = clamp(trans_fn(voicing[idx]), rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trumpet:
                    tb = [s.transpose(12), f.transpose(12), t.transpose(12), r.transpose(12)]
                    rng = [RANGES["Tpt1"], RANGES["Tpt2"], RANGES["Tpt3"], RANGES["Tpt4"]][idx - 5]
                    p = clamp(c2bb(tb[idx - 5]), rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                elif is_trombone:
                    tb = [s.transpose(12), f.transpose(12), t.transpose(12), r]
                    for i, pt in enumerate(tb):
                        if pt.midi < 43:
                            tb[i] = pt.transpose(12)
                        elif pt.midi > 65:
                            tb[i] = pt.transpose(-12)
                    rng = [RANGES["Tbn1"], RANGES["Tbn2"], RANGES["Tbn3"], RANGES["TbnBass"]][idx - 9]
                    p = clamp(tb[idx - 9], rng[0], rng[1])
                    nn = note.Note(p, quarterLength=4)
                    nn.articulations.append(articulations.Tenuto())
                    mg.append(nn)
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BAR 16: Release to Alto or Tenor + rhythm only
            elif bar == 16:
                if is_alto1:
                    if mel_notes:
                        for off, n in mel_notes:
                            p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                            mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                    else:
                        p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                        mg.insert(0, note.Note(p, quarterLength=2))
                        mg.insert(2, note.Rest(quarterLength=2))
                elif is_sax or is_trumpet or is_trombone:
                    mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            # BARS 17-32: Repeat texture plan (abbreviated - same logic)
            else:
                if 17 <= bar <= 18:
                    if is_alto1:
                        if mel_notes:
                            for off, n in mel_notes:
                                p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                                mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                        else:
                            p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                            mg.append(note.Note(p, quarterLength=4))
                    elif is_sax or is_trumpet or is_trombone:
                        mg.append(note.Rest(quarterLength=4))
                elif 19 <= bar <= 20:
                    if is_tpt2:
                        if mel_notes:
                            for off, n in mel_notes:
                                p = clamp(c2bb(n.pitch), RANGES["Tpt2"][0], RANGES["Tpt2"][1])
                                mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                        else:
                            p = clamp(c2bb(f.transpose(12)), RANGES["Tpt2"][0], RANGES["Tpt2"][1])
                            mg.append(note.Note(p, quarterLength=4))
                    elif is_tbn1:
                        ctr = tbn1_lyrical_counterline(((bar - 1) % 4) + 5, r, t, f, s) if 19 <= bar <= 22 else None
                        if ctr:
                            for off, pt, ql in ctr:
                                p = clamp(pt, RANGES["Tbn1"][0], RANGES["Tbn1"][1])
                                nn = note.Note(p, quarterLength=ql)
                                nn.articulations.append(articulations.Tenuto())
                                mg.insert(off, nn)
                        else:
                            mg.append(note.Rest(quarterLength=4))
                    elif is_sax or (is_trumpet and not is_tpt2) or (is_trombone and not is_tbn1):
                        mg.append(note.Rest(quarterLength=4))
                elif 21 <= bar <= 24:
                    if is_ten1 and bar in (21, 22):
                        if mel_notes:
                            for off, n in mel_notes:
                                p = clamp(trans_fn(n.pitch), RANGES["Ten1"][0], RANGES["Ten1"][1])
                                mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                        else:
                            p = clamp(trans_fn(f.transpose(12)), RANGES["Ten1"][0], RANGES["Ten1"][1])
                            mg.append(note.Note(p, quarterLength=4))
                    elif is_alto1 and bar in (23, 24):
                        if mel_notes:
                            for off, n in mel_notes:
                                p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                                mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                        else:
                            p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                            mg.append(note.Note(p, quarterLength=4))
                    elif is_sax and not ((is_ten1 and bar in (21, 22)) or (is_alto1 and bar in (23, 24))):
                        if bar in (22, 24) and (is_alto2 or is_ten2):
                            inner = t.transpose(12) if is_alto2 else s.transpose(12)
                            rng = RANGES["Alto2"] if is_alto2 else RANGES["Ten2"]
                            p = clamp(trans_fn(inner), rng[0], rng[1])
                            nn = note.Note(p, quarterLength=4)
                            nn.articulations.append(articulations.Tenuto())
                            mg.append(nn)
                        else:
                            mg.append(note.Rest(quarterLength=4))
                    elif is_trumpet or is_trombone:
                        mg.append(note.Rest(quarterLength=4))
                elif 25 <= bar <= 28:
                    if is_sax:
                        voicing = [f.transpose(12), s.transpose(12), r.transpose(12), t, r]
                        rng = [RANGES["Alto1"], RANGES["Alto2"], RANGES["Ten1"], RANGES["Ten2"], RANGES["Bari"]][idx]
                        p = clamp(trans_fn(voicing[idx]), rng[0], rng[1])
                        nn = note.Note(p, quarterLength=4)
                        nn.articulations.append(articulations.Tenuto())
                        mg.append(nn)
                    elif is_trumpet:
                        tb = [s.transpose(12), f.transpose(12), t.transpose(12), r.transpose(12)]
                        rng = [RANGES["Tpt1"], RANGES["Tpt2"], RANGES["Tpt3"], RANGES["Tpt4"]][idx - 5]
                        p = clamp(c2bb(tb[idx - 5]), rng[0], rng[1])
                        nn = note.Note(p, quarterLength=4)
                        nn.articulations.append(articulations.Tenuto())
                        mg.append(nn)
                    elif is_trombone:
                        tb = [s.transpose(12), f.transpose(12), t.transpose(12), r]
                        for i, pt in enumerate(tb):
                            if pt.midi < 43:
                                tb[i] = pt.transpose(12)
                            elif pt.midi > 65:
                                tb[i] = pt.transpose(-12)
                        rng = [RANGES["Tbn1"], RANGES["Tbn2"], RANGES["Tbn3"], RANGES["TbnBass"]][idx - 9]
                        p = clamp(tb[idx - 9], rng[0], rng[1])
                        nn = note.Note(p, quarterLength=4)
                        nn.articulations.append(articulations.Tenuto())
                        mg.append(nn)
                else:
                    if is_alto1:
                        if mel_notes:
                            for off, n in mel_notes:
                                p = clamp(trans_fn(n.pitch), RANGES["Alto1"][0], RANGES["Alto1"][1])
                                mg.insert(off, note.Note(p, quarterLength=n.quarterLength))
                        else:
                            p = clamp(trans_fn(f.transpose(12)), RANGES["Alto1"][0], RANGES["Alto1"][1])
                            mg.insert(0, note.Note(p, quarterLength=2))
                            mg.insert(2, note.Rest(quarterLength=2))
                    elif is_sax or is_trumpet or is_trombone:
                        mg.append(note.Rest(quarterLength=4))
                if is_piano:
                    add_piano_chord()
                if is_bass:
                    add_bass()
                if is_drums:
                    mg.append(note.Rest(quarterLength=4))

            if len(mg.notesAndRests) == 0:
                mg.append(note.Rest(quarterLength=4))
            part.append(mg)

    score = stream.Score()
    for pid in ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12", "P13", "P14", "P15", "P16"]:
        score.append(parts[pid][0])

    score.metadata = metadata.Metadata()
    score.metadata.title = "V32 Beatrice - Chorus 2 Real Ranges, Real Melody"
    score.metadata.composer = "Sam Rivers"
    score.metadata.arranger = "Mike Bryant"
    return score

def add_drum_notation(root):
    parts = root.findall('part')
    drum_part = None
    for p in parts:
        for sp in root.iter('score-part'):
            if sp.get('id') == p.get('id'):
                pn = sp.find('part-name')
                if pn is not None and pn.text and 'Drum' in pn.text:
                    drum_part = p
                    break
        if drum_part:
            break
    if drum_part is None:
        drum_part = parts[-1] if parts else None
    if drum_part is None:
        return
    divs = 10080
    q_dur = divs
    for meas in drum_part.findall('measure'):
        to_remove = []
        for n in meas.findall('note'):
            if n.find('rest') is not None:
                dur = n.find('duration')
                if dur is not None and int(dur.text or 0) >= divs * 3:
                    to_remove.append(n)
        for n in to_remove:
            meas.remove(n)
        for i in range(4):
            if i in (1, 3):
                note_el = ET.SubElement(meas, 'note')
                unp = ET.SubElement(note_el, 'unpitched')
                ET.SubElement(unp, 'display-step').text = 'F'
                ET.SubElement(unp, 'display-octave').text = '5'
                ET.SubElement(note_el, 'duration').text = str(q_dur)
                ET.SubElement(note_el, 'type').text = 'quarter'
                ET.SubElement(note_el, 'voice').text = '1'
            else:
                rest_el = ET.SubElement(meas, 'note')
                ET.SubElement(rest_el, 'rest')
                ET.SubElement(rest_el, 'duration').text = str(q_dur)
                ET.SubElement(rest_el, 'type').text = 'quarter'
                ET.SubElement(rest_el, 'voice').text = '1'

def inject_landscape(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for el in root.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]

    add_drum_notation(root)

    defaults = root.find('defaults')
    if defaults is not None:
        pl = defaults.find('page-layout')
        if pl is not None:
            defaults.remove(pl)
        pl = ET.SubElement(defaults, 'page-layout')
        ET.SubElement(pl, 'page-height').text = '2475'
        ET.SubElement(pl, 'page-width').text = '3500'
        pm = ET.SubElement(pl, 'page-margins')
        pm.set('type', 'both')
        ET.SubElement(pm, 'left-margin').text = '124'
        ET.SubElement(pm, 'right-margin').text = '124'
        ET.SubElement(pm, 'top-margin').text = '124'
        ET.SubElement(pm, 'bottom-margin').text = '124'
        sl = ET.SubElement(defaults, 'system-layout')
        sm = ET.SubElement(sl, 'system-margins')
        ET.SubElement(sm, 'left-margin').text = '115'
        ET.SubElement(sm, 'right-margin').text = '0'
        ET.SubElement(sl, 'system-distance').text = '120'

    for wt in root.iter('work-title'):
        if wt.text:
            wt.text = 'V32 Beatrice - Chorus 2 Real Ranges, Real Melody'
    for mt in root.iter('movement-title'):
        if mt.text:
            mt.text = 'V32 Beatrice - Chorus 2 Real Ranges, Real Melody'

    import io
    buf = io.StringIO()
    tree.write(buf, encoding='unicode', default_namespace='', method='xml')
    xml_str = buf.getvalue()
    if 'encoding="cp1252"' in xml_str:
        xml_str = xml_str.replace('encoding="cp1252"', 'encoding="UTF-8"')
    if not xml_str.strip().startswith('<?xml'):
        xml_str = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + xml_str
    if '<!DOCTYPE' not in xml_str:
        xml_str = xml_str.replace(
            '<score-partwise',
            '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\n<score-partwise',
            1
        )
    Path(xml_path).write_text(xml_str, encoding='utf-8')

def main():
    print("Building V32 Beatrice Chorus 2 Real Ranges, Real Melody...")
    score = create_score()
    score.write("musicxml", fp=OUT_PATH)
    inject_landscape(OUT_PATH)
    print(f"Written: {OUT_PATH}")

if __name__ == "__main__":
    main()
```
