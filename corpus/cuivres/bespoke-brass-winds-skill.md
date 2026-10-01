---
titre: "bespoke-mcp — skill bespoke-brass-winds (tessitures, articulations, écriture de section, stabs, swells)"
source: https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp/master/.agents/skills/bespoke-brass-winds/SKILL.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: écriture de section ; MIDI
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

En-tête d'origine du fichier :

```yaml
name: bespoke-brass-winds
description: Write and produce brass and woodwinds in Bespoke Synth — the nine brass and twenty-four wind maps, their real ranges and the articulations that exist, section writing harmonised from chord tones, stabs and swells, breath and phrasing faked from note data, and the instruments the packs simply do not have. Use when asked for brass, horns, trumpet, trombone, tuba, a horn section, woodwinds, flute, oboe, clarinet, bassoon, sax, a brass band or a shout chorus.
```


# Brass and woodwinds in Bespoke Synth

> **Worked examples under `demos/historical/`.** Some demos this skill cites are frozen for a
> future rebuild batch: the technique they show is sound, but they predate several engine fixes,
> so the exact dB, centroid and level figures quoted from them will move when they are rebuilt.
> Trust the method, re-measure the numbers.

The genre skill decides *what* the wind writing is —
[bespoke-orchestral](../bespoke-orchestral/SKILL.md) (doubling, tutti, seating),
[bespoke-jazz](../bespoke-jazz/SKILL.md) (a shout chorus harmonised from chord tones) — and the
demos add two idioms nothing else covers: **`balkan_brass`** (a Dragačevo band in real aksak,
journal at [data-packs/demos/historical/balkan_brass/compositional_journal.md](../../../data-packs/demos/historical/balkan_brass/compositional_journal.md)) and **`salsa_dura`** (a
four-piece front line whose every hit is on a clave stroke,
[data-packs/demos/historical/salsa_dura/compositional_journal.md](../../../data-packs/demos/historical/salsa_dura/compositional_journal.md)). This skill is how to *play* winds here:
which map, what it can articulate, how to make it breathe, and what is missing.

**And the component skills this leans on:** [bespoke-sampling](../bespoke-sampling/SKILL.md)
(sfizz and the SFZ orchestra), [bespoke-effects](../bespoke-effects/SKILL.md) (saturation instead
of compression, the hall) and [bespoke-mixing-mastering](../bespoke-mixing-mastering/SKILL.md)
(22 dB of spread, and the 2–4 kHz shrillness).

## Brass — the whole inventory is nine maps

All `sfizz`, one instance per instrument *and* articulation; catalogued in
`data-packs/sounds/orchestra.json` under `family: "brass"`. VCSL contributes **no brass at all**
(its only lip aerophone is a didgeridoo, and that is not mapped), so this is everything.

| Map | Articulations | Range | Layers |
|---|---|---|---|
| `vsco2-trumpet` | `sustain` 53–84 · `staccato` 53–84 · `vibrato` 53–84 · `mute` 58–81 | 53–84 | 2–3 |
| `phil-trumpet` | `sustain` only | 51–88 | 2 |
| `vsco2-f-horn` | `sustain` 50–77 · `staccato` 50–77 · `mute` 53–77 | 50–77 | **3–4** |
| `phil-french-horn` | `sustain` 34–74 · `mute` 43–74 · `trill` 37–71 | 34–74 | 2 |
| `vsco2-tenor-trombone` | `sustain` 34–65 · `staccato` 34–65 · `vibrato` 41–63 | 34–65 | 3–4 |
| `vsco2-oldtrombone` | `sustain` 41–67 (**five layers**) · `staccato` 41–65 · `vibrato` 46–65 · **`buzz`** 41–60 | 41–67 | up to 5 |
| `phil-trombone` | `sustain` 40–76 · `vibrato` 47–74 | 40–76 | 2 |
| `vsco2-tuba` | `sustain` 29–62 · `staccato` 34–62 | 29–62 | 2–3 |
| `phil-tuba` | `sustain` 29–65 · `vibrato` 45–63 | 29–65 | 2 |

`vsco2-oldtrombone/sustain` is **the most dynamically capable single map in the orchestra** —
five velocity layers, split at 26/52/77/96/103 — and it is used by nothing. Reach for it when a
brass line needs a real crescendo.

> [!IMPORTANT]
> **Always name the explicit articulation** (`catalog:<key>:<articulation>`). A bare lookup on VSCO 2 brass often resolves to `staccato` (highest region count) rather than `sustain`. See [overtone-reference-selection](../overtone-reference-selection/SKILL.md) for articulation resolution rules.

**`phil-tuba` and `phil-trumpet` have no `staccato`.** For short brass you want the VSCO 2 maps.

## Woodwinds — twenty-four maps, of which eight are orchestral

| Map | Articulations | Range | Layers |
|---|---|---|---|
| `vsco2-flute` | `sustain` 60–96 · `staccato` 69–96 (**4 layers**) · `vibrato` 60–96 | 60–96 | 1–4 |
| `phil-flute` | `sustain` 60–101 · `trill` 63–90 | 60–101 | 2 |
| `vsco2-piccolo` | `sustain` 79–103 · `staccato` 82–106 | 79–106 | 1 |
| `vsco2-oboe` | `sustain` 58–89 · `staccato` 58–89 · `vibrato` 58–89 | 58–89 | 2–3 |
| `phil-oboe` | `sustain` only | 58–92 | 2 |
| `phil-cor-anglais` | `sustain` only | 52–83 | 2 |
| `vsco2-clarinet` | `sustain` 50–86 · `staccato` 50–89 | 50–89 | 3 |
| `phil-clarinet` | `sustain` 50–96 · `trill` 53–89 | 50–96 | **1** |
| `phil-bass-clarinet` | `sustain` only | 37–81 | 2 |
| `vsco2-bassoon` | `sustain` 41–75 · `staccato` 38–72 · `vibrato` 43–72 | 38–75 | 2 |
| `phil-bassoon` | `sustain` 34–76 · `trill` 46–70 | 34–76 | 2 |
| `phil-contrabassoon` | `sustain` only | 26–61 | 2 |
| `vcsl-tenor-saxophone` | `sustain` 44–88 · `staccato` 44–88 · `vibrato` 46–86 | 44–88 | 1–2 |
| `phil-saxophone` | `sustain` 51–89 · `trill` 55–84 | 51–89 | 2 |
| `vcsl-saxello` | `sustain` 58–88 · `staccato` 58–86 · `vibrato` 58–87 | 58–88 | 1–2 |
| `vcsl-baroque-{soprano,alto,tenor,bass}-recorder` | `sustain`, `staccato`, and `vibrato` on alto/tenor/bass | 53–96 across the four (bass 53–77, tenor 60–84, alto 65–88, soprano 72–96) | 1 |
| `vcsl-ocarina-small` / `-typical` | `sustain`, `staccato` / `vibrato` | 69–96 | 1 |
| `vcsl-harmonica-hohner-special20-c` / `-f` / `-super64` | `sustain`, `vibrato`, and on the F: `accented`, `handvib`, `staccato` | 48–101 across the three | 1–2 |

**`phil-clarinet` has one velocity layer and no `staccato`.** Its 50–96 range is the widest
clarinet here, so it is the right map for a *line* and the wrong one for a rhythm part.

**Substitute by family, not by timbre.** Every catalog record carries `family`
(`strings`/`winds`/`brass`/`keys`/`plucked`/`percussion`), and so does the sfizz profile's list of
37 friendly names. There is **no accordion**: the answer is the Hohner harmonica, because it is
the only free-reed instrument in the library.

## Levels — and the level-match table you need before writing a note

One note at velocity 100, rendered. Same test for every map, so the numbers are comparable:

| Map | pitch | RMS | centroid |
|---|---|---|---|
| `vsco2-tuba/sustain` | 40 | **−24.8 dB** | 982 Hz |
| `phil-tuba/sustain` | 40 | −25.1 | 351 |
| `vsco2-bassoon/sustain` | 50 | −26.0 | 1038 |
| `vsco2-trumpet/sustain` | 70 | −26.8 | 2412 |
| `vsco2-f-horn/sustain` | 60 | −27.1 | 753 |
| `phil-bassoon/sustain` | 50 | −28.7 | 1024 |
| `phil-oboe/sustain` | 70 | −28.9 | 1707 |
| `vsco2-tenor-trombone/sustain` | 50 | −30.1 | 1244 |
| `phil-trumpet/sustain` | 70 | −30.2 | 2409 |
| `phil-saxophone/sustain` | 60 | −34.2 | 2504 |
| `phil-french-horn/sustain` | 60 | −36.2 | 1186 |
| `vcsl-tenor-saxophone/sustain` | 60 | −36.2 | 2644 |
| `phil-clarinet/sustain` | 62 | −36.3 | 2002 |
| `phil-flute/sustain` | 79 | −38.2 | 2524 |
| `phil-trombone/sustain` | 50 | −39.3 | 1547 |
| `vsco2-oboe/sustain` | 70 | −41.2 | 2618 |
| `vsco2-flute/sustain` | 79 | −44.1 | 1615 |
| `vsco2-clarinet/sustain` | 62 | **−46.4 dB** | 2568 |

**Twenty-two decibels of spread, and the two trombones are nine decibels apart.** `balkan_brass`
reaches those factors with a `lift()` helper that stacks gain stages —
`lift(tuba, 3.4)`, `lift(trombone, 3.0)`, `lift(clarinet, 3.4)`, `lift(trumpet1, 3.2)`, each
`while factor > 2.0: gain_stage(voice, 2.0); factor /= 2`. A single stage would do: a `gain`
slider shows a maximum of 2.0 and does not enforce it (a write of 8.0 measures +18.06 dB). Do the same, from this table, before
you balance anything by ear.

## Velocity 96 is a dynamic marking, not a fader

Every generated map splits at `lovel=96` and the multi-layer VSCO 2 ones add splits at 43, 86 and
sometimes 26/52/77/103. Measured with an 8-step velocity sweep:

| Map | 8 → 88 | the step at 96 |
|---|---|---|
| `vsco2-trumpet/sustain` | −48.9 → −42.5 dB, smoothly | **+15.0 dB** |
| `phil-french-horn/sustain` | −51.4 → −44.9, smoothly | **+7.1 dB** |
| `vsco2-flute/sustain` | −47.8 → −41.4, smoothly | +3.8 dB |

So on brass, **velocity 95 is *mp* and velocity 96 is *f*, and there is nothing in between.**
Write the whole of a soft passage below 96 and the whole of a loud one above it; get the
*continuous* dynamic from a scheduled gain ramp on the voice's own gain stage. A phrase arc that
wanders across 96 will jump fifteen decibels in the middle of a note-to-note step and read as a
fault.

## Section writing

### Harmonise from the chord, never by interval

A second trumpet is not "the melody minus four semitones"; it is the **next chord tone below**
each melody note, taken from the chord actually sounding under that beat. Parallel intervals put
a major third against a ♭9 the moment the chart has an altered dominant in it.
`genre_jazz`'s `tone_below()` is six lines and it is the difference between a section and a
harmoniser.

`salsa_dura` does the same thing from the other end: each section hit is four voices read out of
the chord's **rootless upper structure** in a fixed order, with the trombone taking its voice an
octave down:

```
CHORDS["Cm9"]["upper"]  = [63, 67, 70, 74]      # tp1, tp2, sax get degrees 3,2,1; tbn gets 0 -12
CHORDS["G7alt"]["upper"] = [62, 65, 71, 73]
```

That guarantees the section is always inside one chord, which is why it never sounds like four
soloists.

### Voicing habits worth having

- **Close-position brass in the middle, open at the bottom.** Nothing closer than a fifth below
  MIDI 48; a major second between two brass in the low register is a growl, not a chord.
- **Four-part close (drop-0) for punch, drop-2 for width.** Drop-2: take a close four-note
  voicing and drop the second-highest an octave — `[60,64,67,71]` → `[55,60,64,71]`.
- **The tuba/trombone is the bass and it should double the bass line or replace it**, not sit
  above it playing thirds. In `balkan_brass` the helicon plays the "bas" on the group starts and
  the tenor horns play the "pah" on every unit that is *not* a group start — the two never
  overlap, which is what makes an oom-pah read as a machine rather than as a pad.
- **Doubling changes the colour, not the notes.** Oboe alone → oboe with flute an octave up
  (brilliance) → violins and flute in unison (warmth) → solo flute (exposure).
- **Contrary motion.** In `genre_orchestral`'s tutti the horns rise `55 + 0,3,5,7,8,10,11` while
  the ground falls. That, and not level, is what stops a tutti sounding like a stack of pads.

### Stabs, swells, pads and falls

| Gesture | How to write it |
|---|---|
| **Stab** | `staccato` map, length 0.03–0.06 measures, velocity ≥ 100 (above the 96 layer), all voices attacking on the *same* sixteenth. In salsa put it on a clave stroke; in funk put it on the "and" |
| **Swell** | `sustain` map, a long note, and a **scheduled gain ramp** on that voice's gain stage — `bespoke_set_control(gain, v, at_measure_time=…)` in 8–16 steps. Velocity cannot do it, because of the 96 cliff |
| **Pad / bed** | `sustain`, re-articulated every one or two bars with a 0.06 overlap, two instruments an octave apart, velocity 70–88 so it stays under the melody's layer |
| **Fall / doit** | a `pitchdive` module: `~start` −4 semitones, `~time` 400 ms gives a real scoop *into* the note (measured: 465 → 478 → 522 → 524 Hz on a sampled sustain). For a fall *out* of a note, put the dive on a short repeated note at the phrase end |
| **Shake / vibrato entry** | a `vibrato` module, `~vibrato` 0.6, `~vibinterval` 3 — the pitch oscillates about ±60 cents. It applies to the whole part, so a passage needing plain *and* vibrato tone needs two instances |
| **Flutter, growl, subtone, half-valve** | **do not exist.** `vsco2-oldtrombone/buzz` is the nearest thing in the library |

## Breath and phrasing, faked from note data

This is most of the difference between a wind part and a synth pad.

1. **Leave gaps.** A wind player breathes. End a phrase 0.03–0.06 measures early and start the
   next one on time; never run a line for eight bars without a hole in it. If two winds are in
   unison, stagger their breaths so the line is continuous and the *players* are not.
2. **Overlap inside a phrase** by 0.06–0.08 measures and start each note `0.015` measures early,
   so the slow sample attack speaks on the beat. That is the only legato these maps have.
3. **Arc every phrase in velocity** — up into the middle, down at the end — but keep the arc on
   one side of 96 (above).
4. **Soloists and sections lag.** Horns and a lead melody sit ~10–30 ms behind the rhythm section;
   at 160 BPM that is `+0.013` measures on every note. `salsa_dura` adds `LAG = 0.006` measures to
   the whole four-piece front line for the same reason. It is a measured component of ensemble
   feel, not a fudge.
5. **Humanise ±10–20 ms and ±8–12 velocity from a seeded RNG**, or use `notehumanizer`
   (`~time ms`, `~velocity`) — but a seeded generator keeps the render reproducible and the
   module does not.
6. **Re-articulate anything longer than about two bars.** The generated maps mostly have no loop
   points, so a long pedal can simply stop mid-note.
7. **A note at `start_measure: 0.0` never fires.** Start at 0.01.

## Idioms with real data

### Balkan brass band (`balkan_brass`)

Eight winds over three percussion layers, in **7/8 (2+2+3) → 9/8 (2+2+2+3) → 7/8 → 11/16
(2+2+3+2+2) → 7/8**, accelerating 108 → 200 BPM. Everything is placed against the *group starts*,
not against beats:

```python
def at(bar, unit):        # one bar is 1.0 measures whatever the meter is
    return bar + unit / meter(bar)[0]      # unit k of a seven sits at k/7 of a bar
```

Roles: helicon (`vsco2-tuba/staccato`) on the group starts plus a second note inside the long
group; tenor horns (`vsco2-f-horn/staccato`) on every unit that is *not* a group start; trumpet 1
(`vsco2-trumpet/sustain`) and 2 (`vsco2-trumpet/staccato`) in the mode's thirds; trumpet 3
(`phil-trumpet/sustain`) answering from across the square, panned −0.72 with `widen −14`;
trombone (`vsco2-tenor-trombone/sustain`) as a countermelody; clarinet (`phil-clarinet/sustain`)
and tenor sax (`vcsl-tenor-saxophone/vibrato`) on the fills.

The constraint, asserted in the builder: **no trumpet phrase ends on a downbeat** — every
phrase's last note begins on the start of the bar's final, long group (4/7, 6/9 or 7/11). The
aksak bar leans forward onto the long beat, and writing the phrase-ends there is what stops a
seven being heard as a four with a three stapled on. It fired once, at bar 19, and the fix was
musical.

**In an odd or changing meter every drum has to be on a `notecanvas`** — a 16-step
`drumsequencer` runs at sixteenths of the transport's bar, so in 7/8 it puts sixteen steps inside
fourteen sixteenths.

### Salsa front line (`salsa_dura`)

Two trumpets, trombone and tenor sax — `vsco2-trumpet/staccato`, `phil-trumpet/sustain`,
`vsco2-tenor-trombone/staccato`, `vcsl-tenor-saxophone/staccato`. Four gestures, and no pads:

- **llamada** — a unison call over the bare clave, on the clave's own strokes, the four voices at
  `+12 / 0 / 0 / −12`.
- **answers in the gaps** — two bars in every four, never under the singer.
- **moña** — the same three-note motif over five different chords, harmonised, on every clave
  stroke.
- **ponche** — two hits in four bars, and the horns are otherwise silent.

The asserted rule is that **every moment where two or more horns attack together is a clave
stroke of its own bar** (sixteenths 0, 6, 12 on the three-side; 4, 8 on the two-side), after
subtracting the section's 6 ms lag. It cost the piece its passing tones — the horns are *voiced*
rather than *arranged* — and it is the honest trade.

### Orchestral

Winds enter *after* the strings and carry the theme from the middle of the piece; brass exist
only in the tutti. In `genre_orchestral` the horns' first note is in bar 21 of 35, and that
entrance is the loudest event in the piece without being the loudest sound.

### Jazz shout chorus

Three horns — tenor (`sax_tenor` preset or `vcsl-tenor-saxophone`), trumpet
(`vsco2-trumpet/sustain`), trombone (`vsco2-tenor-trombone/sustain`) — harmonised from the chart
by chord tone, entering only for the last chorus, every note +0.013 measures behind the section.

## Production

**Seating pan**: horn −0.26, trumpet +0.20, trombone and tuba +0.36, flute −0.06, oboe +0.10,
clarinet +0.05, bassoon +0.24. A brass band is wider and flatter — `balkan_brass` puts the two
lead trumpets at ∓0.42/+0.44 and the answering trumpet at −0.72 with a negative `widen`, which is
how "across the square" is expressed.

**One room, on the master.** `Dragonfly Room Reverb/live_room` for a band, `Dragonfly Hall
Reverb/orchestral_hall` for an orchestra — then expose `width`, `dry`, `late`, `early`, `size`,
`decay`, `predelay` and pull the width in, because at its preset width a Dragonfly takes channel
correlation negative and the mix fails its own mono check.

**EQ**: high-pass brass at 80–120 Hz (tuba excepted), cut 250–400 Hz when a section stacks, and
expect the 2–4 kHz region to be where a trumpet gets shrill — a wide −2 dB there is usually
enough. Use the stock `eq` module (8 bands, 20–20 000 Hz, a real filter at every frequency) or
`Parametric Equalizer x16 Stereo` or the stock `eq`. A `biquad` lowpass above 3000 Hz used to
crossfade back to dry (+9.9 dB at 6200 Hz rather than a cut); that is fixed.

**Saturation instead of compression.** `ZamTube/crunch_rhythm` at low drive on a brass bus gives
the edge that a real fortissimo has and a sample does not. Keep the dynamics — a limiter on the
master took one orchestral piece's crest factor from 21.8 dB to 16.0.

## Worked example — `balkan_brass`

```
bespoke_set_transport(tempo=108, time_sig_top=7, time_sig_bottom=8)
# poziv 4 / kolo 8 / devet 8 / povratak 6 / kopanica 6 / trka 8 = 40 bars

# 1. eight winds, each its own sfizz instance and its own canvas
for name, key, art in (("tuba","vsco2-tuba","staccato"), ("horn","vsco2-f-horn","staccato"),
                       ("tbn","vsco2-tenor-trombone","sustain"), ("tr1","vsco2-trumpet","sustain"),
                       ("tr2","vsco2-trumpet","staccato"),  ("tr3","phil-trumpet","sustain"),
                       ("clar","phil-clarinet","sustain"),  ("sax","vcsl-tenor-saxophone","vibrato")):
    bespoke_spawn_module("plugin", name=name); bespoke_load_plugin(name, "sfizz")
    bespoke_set_plugin_state(name, state_with_sfz(bespoke_get_plugin_state(name),
                                                 orchestra_sfz(key, art)))

# 2. the meter changes are scheduled writes on the transport singleton
bespoke_set_control("transport~timesigtop", 9, at_measure_time=origin + 12)   # devet
bespoke_set_control("transport~timesigtop", 7, at_measure_time=origin + 20)
bespoke_set_control("transport~timesigbottom", 16, at_measure_time=origin + 26)  # kopanica, 11/16
bespoke_set_control("transport~tempo", 158, at_measure_time=origin + 32)      # ...one value per bar

# 3. every part is placed on the group starts of its own bar, not on beats
bespoke_set_canvas_notes("bas",  replace=True, notes=[...])   # tuba on 0, 2, 4 of a seven
bespoke_set_canvas_notes("pah",  notes=[...])                 # horns on 1, 3, 5, 6
bespoke_set_canvas_notes("lead", notes=[...])                 # trumpet phrases END on 4/7

# 4. gains: the maps are 22 dB apart, so stack them
#    lift(tuba, 3.4) · lift(tbn, 3.0) · lift(horn, 2.4) · lift(tr1, 3.2) · lift(tr2, 2.6)
#    lift(tr3, 2.2, widen=-14) · lift(clar, 3.4) · lift(sax, 2.2)
bespoke_load_plugin("square", "Dragonfly Room Reverb"); bespoke_plugin_preset("square", "live_room")

bespoke_wait(measures=40); bespoke_analyze_audio(); bespoke_get_events()
```

Measured on the committed render: 64.0 s, 40 bars, 60 modules, **11 note sources, 3841 notes**,
52 scheduled moves, peak 0.0 dBFS with 29 clipped samples (0.001 %), crest 15.2 dB, centroid
1530 Hz ("warm"), correlation 0.27, width 0.76, mono-compatible, 33/40 bars distinct. Per section
(RMS dB / centroid Hz): poziv −26.7/1295 · kolo −17.2/1683 · devet −19.0/1423 · povratak
−16.2/1566 · kopanica −18.4/2224 · trka −16.9/2053.

**Automating the tempo desynchronises every other scheduled write**, because `at_measure_time`
resolves to a millisecond once, when the write is queued. `Patch.tempo_at` / `meter_at` keep a
bar→seconds map and back-solve it; `offline.render {"measures": N}` has the same bug and has to be
given `ms`.

## Verify

1. **`bespoke_get_events`** — the piano roll shows whether the section is inside one chord and
   whether the phrase ends where you said they would. A harmonisation error is inaudible as a
   *wrong note* and obvious as a pitch set.
2. **`bespoke_analyze_audio`**: `clipped_samples` (a four-voice section stacking on one stab
   clips easily), `stereo.mono_compatible`, and `spectrum.bands` — brass piling into upper-mid
   and presence is what "shrill" means.
3. **Levels per voice**, `bespoke_get_module_levels` read **mid-note** (bar N + 0.2). Three
   instruments read "−60 dBFS, effectively silent" on one cue's first probe and were fine.
4. **Play one note at velocity 95 and again at 96** before writing dynamics on a new map.
5. On dense wind material expect a warning that the onset-derived tempo disagrees with the
   transport. In an aksak meter it always will.

## The honest limits

- **No flutter-tongue, growl, subtone, half-valve, rip, doit, fall or shake as samples.** Falls
  and scoops are a `pitchdive` module; everything else is unavailable.
- **No legato and no true crescendo.** Two velocity layers (five on one trombone map), a hard
  step at 96, and gain ramps for everything in between.
- **Instruments that do not exist anywhere in the packs**: alto and soprano saxophone (there is a
  tenor, a saxello and one unlabelled Philharmonia `saxophone` at 51–89), flugelhorn, cornet,
  euphonium, bass trombone, alto and bass flute, oboe d'amore, basset horn, contrabass clarinet,
  a Wagner tuba, and any brass at all from VCSL.
- **No accordion** — substitute the Hohner harmonica, the only free-reed instrument here.
- **No round-robin.** Repeated identical notes machine-gun; vary velocity and micro-timing, or
  alternate two instances of the same map.
- **A notecanvas carries no pitch bend**, so scoops, falls and vibrato are modules in front of the
  voice and apply to the whole part.
- **`bespoke_get_module_levels` is a live meter, not a per-section fold**, so balancing eight
  winds is render → read the section table → guess → re-render.
