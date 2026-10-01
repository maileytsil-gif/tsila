---
titre: "bespoke-mcp-data-pack — demo afrobeat style.py (section de cuivres, stabs, appel-réponse en code)"
source: https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/master/demos/historical/afrobeat/style.py
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: afrobeat ; écriture de section
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

```python
"""`afrobeat` — the code that builds this demo.

Run it with `uv run python tools/build_demos.py afrobeat`. What the piece is and why
it is that way is in compositional_journal.md beside this file.
"""

from __future__ import annotations

from style_kit import HAT_16THS, comp, hits, kit_voice, orchestra_kit, orchestra_sfz, steps


async def afrobeat(p) -> str:
    """36 bars of afrobeat in G dorian — one chord for most of it, and interlock as the tune.

    THE EPISODE. A courtyard at the back of a club at one in the morning, band already
    playing when you walk in, and it is impossible to tell how long they have been on this.
    Nobody is soloing. The agogo is in threes and the hi-hat is in fours and the two of them
    disagree the whole time. About two thirds of the way through the leader cuts everything
    but the drums and one guitar with a hand signal, holds it for four bars while the room
    gets louder than the band, and then the horns come back in a register they had not used —
    and for two bars, once, the whole harmony moves off the chord it has been sitting on.

    THE COLOUR TRIP.
      static and interlocked (G dorian, one chord, the composite of the parts is the material)
        -> the same chord, but the bass ostinato becomes three bars long against a four-bar
           guitar figure, so nothing repeats in the same place again
          -> the only harmonic move in the piece: two bars of Cm9, once
            -> subtraction — drums and one guitar alone
              -> back, an octave up, and the ostinato truncated to three beats so it walks
                 around the bar

    THE CONSTRAINT. The agogo plays a 12-pulse West African bell against a 16-pulse bar for
    every bar of the piece, and the harmony leaves Gm11 exactly once, for two bars.

    THE ANTI-BRIEF. The obvious version is a 16th hi-hat, a pentatonic guitar riff and a
    conga loop, at 118, for four bars, repeated.

    THE IDIOM. Fela's arrangement rather than Fela's tunes: a tenor guitar with one short
    high figure that never varies, a rhythm guitar chopping the sixteenths between it, a bass
    ostinato that is the actual bass part rather than a root, Philharmonia agogo/cabasa/
    djembe/djundjun and surdo interlocking, an electric piano playing a counter-figure, and
    horns in unison stabs answering nothing in particular.
    """
    p.tempo(116)
    arr = p.arrange(("bell", 4), ("vamp", 8), ("keys", 6), ("horns", 8), ("break", 4), ("shout", 6))

    home = [58, 62, 65, 69]  # Gm11 rootless: Bb D F A
    away = [63, 67, 70, 74]  # Cm9   rootless: Eb G Bb D — the one move, two bars, once
    chart = {bar: home for bar in range(arr.bars)}
    chart[int(arr.bar("horns")) + 4] = away
    chart[int(arr.bar("horns")) + 5] = away

    # -- (1) the kit -----------------------------------------------------------------------
    kit = await p.kit(
        {
            0: "gretsch/013_kick.wav",
            1: "gretsch/020_snare.wav",
            2: "gretsch/005_closedhathard.wav",
            3: "gretsch/017_openhat.wav",
            4: "gretsch/019_ridecymbal.wav",
            5: "gretsch/021_snareghost.wav",
            6: "gretsch/012_hitom.wav",
            7: "gretsch/007_cymbalgrab.wav",
        },
        name="kit",
    )
    await p.drum_loop(kit, steps({0: [0, 6, 10], 1: [4, 12]}, velocity=112), "vamp", "keys", "horns", "break", "shout", name="kick")
    await p.drum_loop(kit, steps({2: HAT_16THS}, velocity=48), *arr.names, name="hats")
    await p.drum_loop(kit, steps({3: [7, 15], 5: [2, 9, 14]}, velocity=54), "keys", "horns", "shout", name="ghosts")
    await p.drum_loop(kit, steps({6: [11, 12], 1: [15]}, velocity=76), "shout", name="tomline")
    await p.part(
        kit,
        hits([(arr.bar("horns"), 7, 96), (arr.bar("shout"), 7, 108)])
        + hits([(arr.bar("shout") - 0.5 + i * 0.125, 6, 66 + 9 * i) for i in range(4)]),
        name="fills",
    )
    await p.gain_stage(kit, 0.85, pan=-0.12)
    await p.at("break", f"{p.gain_of(kit)}~gain", 1.4)
    await p.at("shout", f"{p.gain_of(kit)}~gain", 0.95)

    # -- (2) the percussion, on the Philharmonia kit map ------------------------------------
    perc = await p.sfz(orchestra_kit("philharmonia-percussion"), name="perc")
    agogo = kit_voice("philharmonia-percussion", "agogo-bells")
    cabasa = kit_voice("philharmonia-percussion", "cabasa")
    djembe = kit_voice("philharmonia-percussion", "djembe")
    djundjun = kit_voice("philharmonia-percussion", "djundjun")
    surdo = kit_voice("philharmonia-percussion", "surdo")
    guiro = kit_voice("philharmonia-percussion", "guiro")
    # the standard West African 12-pulse bell: x . x . x x . x . x . x, i.e. pulses
    # 0 2 4 5 7 9 11 of twelve — against a bar the hi-hat is dividing into sixteen
    bell_pulses = [0, 2, 4, 5, 7, 9, 11]
    bell_notes: list[tuple[float, int, int]] = []
    for bar in range(arr.bars):
        for pulse in bell_pulses:
            bell_notes.append((bar + pulse / 12.0, agogo, 88 if pulse in (0, 5) else 68))
    await p.part(perc, hits(bell_notes, length=0.04), name="bellline")
    # the djembe answers the bell on the pulses it leaves empty — the interlock is the tune
    hand_notes: list[tuple[float, int, int]] = []
    for bar in range(int(arr.bar("bell")) + 2, arr.bars):
        for pulse in (1, 3, 6, 8, 10):
            hand_notes.append((bar + pulse / 12.0, djembe, 62 if pulse % 2 else 74))
        hand_notes.append((bar + 0.5, djundjun, 84))
        if bar % 2:
            hand_notes.append((bar + 0.875, surdo, 90))
    await p.part(perc, hits(hand_notes, length=0.05), name="hands")
    shaker_notes = [(bar + step / 16.0, cabasa, 44 + 14 * (step % 4 == 0)) for bar in range(arr.bars) for step in range(16)]
    shaker_notes += [(bar + 0.75, guiro, 60) for bar in range(int(arr.bar("keys")), arr.bars, 2)]
    await p.part(perc, hits(shaker_notes, length=0.04), name="shaker")
    await p.gain_stage(perc, 1.7, pan=0.3)  # loud while it is alone, then it takes its place
    await p.at("vamp", f"{p.gain_of(perc)}~gain", 1.15)
    await p.at("break", f"{p.gain_of(perc)}~gain", 0.45)  # the hand signal
    await p.at("shout", f"{p.gain_of(perc)}~gain", 1.25)

    # -- (3) the bass ostinato: 2 bars, then 3, then truncated to three beats ---------------
    two_bar = [
        [(0.0, 0, 0.11, 112), (0.25, 0, 0.11, 92), (0.375, 3, 0.11, 100), (0.5, 5, 0.11, 96), (0.75, 0, 0.11, 104), (0.875, -2, 0.11, 90)],
        [(0.0, 0, 0.11, 110), (0.25, 7, 0.11, 96), (0.5, 5, 0.11, 100), (0.625, 3, 0.11, 92), (0.875, 0, 0.11, 98)],
    ]
    third_bar = [(0.0, 0, 0.11, 108), (0.1875, 10, 0.11, 88), (0.375, 7, 0.11, 96), (0.625, 5, 0.11, 100), (0.75, 3, 0.16, 94)]
    bass = await p.plugin("Surge XT", preset="bass_rubber", name="bass")
    bass_notes: list[dict] = []
    for bar in range(int(arr.bar("vamp")), arr.bars):
        if arr.bar("break") <= bar < arr.bar("shout"):
            continue  # the bass is one of the things the hand signal cuts
        root = 31 if chart[bar] is home else 36  # G1, and C2 for the two bars it moves
        if bar >= arr.bar("shout"):
            # truncated to three beats: the figure walks a beat earlier every bar
            figure = [(o * 0.75, i, ln, v) for o, i, ln, v in two_bar[0]]
        elif bar >= arr.bar("keys"):
            figure = [two_bar[0], two_bar[1], third_bar][(bar - int(arr.bar("keys"))) % 3]
        else:
            figure = two_bar[bar % 2]
        for offset, interval, length, velocity in figure:
            bass_notes.append(
                {"pitch": root + interval, "start_measure": round(bar + offset, 6), "length_measures": length, "velocity": velocity}
            )
    await p.part(bass, bass_notes, name="ostinato")
    bass_filter = await p.filter_stage(bass, cutoff=600.0, q=1.4)
    await p.gain_stage(bass, 0.5, pan=0.0)

    # -- (4) the two guitars: one figure each, and the interlock is the material ------------
    tenor = await p.sfz(orchestra_sfz("phil-guitar", "sustain"), name="tenor")
    tenor_figure = [(0.1875, 70), (0.25, 74), (0.375, 72), (0.5625, 70), (0.75, 67), (0.8125, 65)]
    tenor_notes = [
        {"pitch": pitch + (12 if bar >= arr.bar("shout") else 0), "start_measure": round(bar + offset, 6),
         "length_measures": 0.09, "velocity": 84 if offset in (0.1875, 0.75) else 70}
        for bar in range(int(arr.bar("vamp")), arr.bars)
        for offset, pitch in tenor_figure
    ]
    await p.part(tenor, tenor_notes, name="tenorguitar")
    await p.gain_stage(tenor, 1.2, pan=-0.45)
    await p.gate(tenor, "vamp", "keys", "horns", "break", "shout")
    await p.delay(tenor, feedback=0.24)

    rhythm = await p.pluck(None)
    await p.set(f"{rhythm}~vol", 0.4)
    await p.set(f"{rhythm}~filter", 0.42)
    await p.part(
        rhythm,
        comp(chart, arr.bar("vamp"), arr.bars, (0.125, 0.1875, 0.375, 0.4375, 0.625, 0.6875, 0.875, 0.9375), 0.05, 62, spread=0.003),
        name="rhythmguitar",
    )
    await p.gain_stage(rhythm, 0.75, pan=0.46)
    await p.gate(rhythm, "vamp", "keys", "horns", "shout", fade_in=0.5)

    # -- (5) the Rhodes counter-figure ------------------------------------------------------
    rhodes = await p.plugin("Dexed", preset="ep_rhodes", name="rhodes")
    rhodes_notes: list[dict] = []
    for bar in range(int(arr.bar("keys")), arr.bars):
        if arr.bar("break") <= bar < arr.bar("shout"):
            continue
        voicing = chart[bar]
        for index, offset in enumerate((0.0625, 0.3125, 0.5625, 0.8125)):
            rhodes_notes.append(
                {"pitch": voicing[(bar + index) % 4], "start_measure": round(bar + offset, 6),
                 "length_measures": 0.16, "velocity": 76 if index % 2 == 0 else 62}
            )
    await p.part(rhodes, rhodes_notes, name="rhodesline")
    rhodes_filter = await p.filter_stage(rhodes, cutoff=2400.0, q=1.0)
    await p.gain_stage(rhodes, 0.55, pan=0.18)
    await p.gate(rhodes, "keys", "horns", "shout", fade_in=1.0)
    await p.reverb(rhodes, wet=0.22, size=0.6)

    # -- (6) the horn section: unison stabs, an octave up for the shout --------------------
    riff = [(0.5, 0, 0.11, 100), (0.625, 3, 0.11, 92), (0.75, 5, 0.11, 96), (0.875, 7, 0.11, 104), (1.0, 10, 0.55, 108)]
    horn_bars = [arr.bar("horns") + o for o in (0, 2, 4, 6)] + [arr.bar("shout") + o for o in (0, 2, 4)]
    sax = await p.plugin("sfizz", preset="sax_tenor", name="sax")
    trumpet = await p.sfz(orchestra_sfz("vsco2-trumpet", "staccato"), name="trumpet")
    bone = await p.sfz(orchestra_sfz("vsco2-oldtrombone", "staccato"), name="bone")
    sax_notes: list[dict] = []
    trumpet_notes: list[dict] = []
    bone_notes: list[dict] = []
    for bar in horn_bars:
        shout = bar >= arr.bar("shout")
        base = 67 + (12 if shout else 0)
        if int(bar) in (int(arr.bar("horns")) + 4,):
            base += 5  # the two bars that move: the riff moves with the chord
        for offset, interval, length, velocity in riff:
            place = round(bar + offset, 6)
            for part, transpose, trim in ((sax_notes, 0, 0), (trumpet_notes, 12, 12), (bone_notes, -12, 6)):
                part.append(
                    {
                        "pitch": base + interval + transpose,
                        "start_measure": place,
                        "length_measures": length,
                        "velocity": velocity - trim,
                    }
                )
    await p.part(sax, sax_notes, name="saxline")
    await p.gain_stage(sax, 0.85, pan=0.24)
    await p.gate(sax, "horns", "shout", fade_in=0.25)
    await p.reverb(sax, wet=0.2, size=0.5)
    await p.part(trumpet, trumpet_notes, name="trumpetline")
    await p.gain_stage(trumpet, 0.8, pan=-0.3)
    await p.gate(trumpet, "horns", "shout", fade_in=0.25)
    await p.part(bone, bone_notes, name="boneline")
    await p.gain_stage(bone, 1.0, pan=0.38)
    await p.gate(bone, "horns", "shout", fade_in=0.25)

    # -- (7) the moves -----------------------------------------------------------------------
    await p.ramp(p.fx(bass_filter, "F"), 420, 800, "vamp", "horns", steps=16)
    await p.at("shout", p.fx(bass_filter, "F"), 1100)
    await p.ramp(p.fx(rhodes_filter, "F"), 1200, 3600, "keys", "break", steps=18, curve=1.4)
    await p.ramp(f"{p.master}~gain", 0.42, 0.58, "bell", "horns", steps=16)
    await p.at("break", f"{p.master}~gain", 0.56)
    await p.at("shout", f"{p.master}~gain", 0.66)
    await p.ramp(f"{p.master}~gain", 0.66, 0.0, "shout+4", arr.bars, steps=16)
    await p.set(f"{p.master}~gain", 0.42)

    return (
        "116 BPM afrobeat over 36 bars in G dorian: a 12-pulse West African bell against a "
        "16-pulse bar for the whole piece, a bass ostinato that goes from two bars to three to "
        "three beats, two guitars whose interlock is the tune, Philharmonia agogo, cabasa, "
        "djembe, djundjun and surdo, a four-bar break down to drums and one guitar, and horns "
        "that move the harmony off Gm11 exactly once."
    )


# What this demo has to prove beyond audible/finite/unclipped, over and above the
# defaults in tools/build_demos.py.
# The bell is a 12-pulse cycle and the hi-hat a 16-pulse one, for every bar of the piece.
# Folding every note-on onto one bar therefore smears by construction — the cross-rhythm
# *is* the music, and bar_concentration cannot see that. Measured 55 % against the 55 %
# default, i.e. it would fail on a slightly different render.
EXPECTATIONS = {"bar_concentration": 0.45}
```
