---
titre: "bespoke-mcp — skill bespoke-jazz (voicings rootless/quartal, walking bass, swing, comping)"
source: https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp/master/.agents/skills/bespoke-jazz/SKILL.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: harmonie ; jazz
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

En-tête d'origine du fichier :

```yaml
name: bespoke-jazz
description: Write jazz in Bespoke Synth at the level the idiom actually works at — rootless and quartal voicings, real changes and reharmonisation, a walking bass that knows each chord, swung eighths written into note positions, and comping that answers the melody instead of doubling it. Use when asked for jazz, bebop, blues changes, swing, a piano trio, modal jazz, fusion or a standard.
```


# Jazz in Bespoke Synth

> **Worked examples under `demos/historical/`.** Some demos this skill cites are frozen for a
> future rebuild batch: the technique they show is sound, but they predate several engine fixes,
> so the exact dB, centroid and level figures quoted from them will move when they are rebuilt.
> Trust the method, re-measure the numbers.

> **If a score already exists, start at [score-handoff](../score-handoff/SKILL.md), not here.**
> A piece composed in score-mcp arrives as a `.mid` plus a brief, and `bespoke_load_score`
> imports it a track per notecanvas with the tempo map, the conductor notes and the mix moves.
> This skill then answers *which instrument and why*; score-handoff answers how to realise, verify
> and stage each one. Composing rather than realising? [score-songwriting](../score-songwriting/SKILL.md).

The worked example is **`genre_jazz`** in `data-packs/demos/historical/genre_jazz/style.py` — a Bird blues in F, 52 bars, five
choruses and no two of them the same changes — with its journal at
[data-packs/demos/historical/genre_jazz/compositional_journal.md](../../../data-packs/demos/historical/genre_jazz/compositional_journal.md). `jazz_swing` (C minor, six-bar A sections, a
So What bridge) and `bossa_nova` are two more.

**Then read the instrument skills for the band you are writing.**
[bespoke-keys](../bespoke-keys/SKILL.md) (voicings, comping, the sustain pedal),
[bespoke-bass](../bespoke-bass/SKILL.md) (walking, the upright maps),
[bespoke-drums](../bespoke-drums/SKILL.md) (ride, brushes, ghosts, per-pad level) and
[bespoke-brass-winds](../bespoke-brass-winds/SKILL.md) (a horn section harmonised from chord
tones) carry the how.

**Then the component skills:** [bespoke-sampling](../bespoke-sampling/SKILL.md) (sfizz and the
SFZ orchestra, which is where every acoustic instrument here comes from),
[bespoke-effects](../bespoke-effects/SKILL.md) (the club room, the EQ) and
[bespoke-mixing-mastering](../bespoke-mixing-mastering/SKILL.md) (a trio has to breathe — watch
the crest factor).

**The bar this skill exists to clear.** The demo it replaced "sounds a little bit like a beginner
blues band". The diagnosis was not the sounds: it was `F7 | B♭7 | F7 | …` — the chart every
beginner learns in their first month — with **no melody at all**, a bass that picked its notes at
random from a pool, and a comp that struck the same voicing on beat 1 and the "and of 2" of every
bar. A jazz patch that plays `Am7 Dm7 G7 Cmaj7` under a Rhodes preset has failed before it
sounds. Read
[docs/Composition_Standard.md](../../../docs/Composition_Standard.md) §7.3.

## Scope — what is tractable, honestly ranked

| Idiom | Verdict |
|---|---|
| **Blues with real substitutions** (Bird blues, minor blues, jazz blues) | **Best target.** Twelve bars is enough room for a chain of ii–Vs, and the form lets you play the *same* twelve bars with different changes five times, which is where the sophistication lives. |
| **Modal** (So What, Impressions) | Easiest harmonically — one or two scales for 8–16 bars, quartal voicings, no functional voice-leading engine needed. Use it as an interlude inside something else rather than as a whole piece. |
| **Piano trio / swing combo** | Very good. Walking bass and comping are near-algorithmic; the parts that are hard are the ones you write by hand anyway. |
| **Rhythm changes / 32-bar AABA** | Good, and more work: 32 bars of changes plus a bridge is a lot of hand-written chart. |
| **Fusion / jazz-funk** | Good. Straight or lightly swung sixteenths, static vamps, `Dexed/ep_rhodes` and a synth lead. Rhythm is funk-adjacent and sequencer-friendly. |
| **Organ trio** | Good and cheap — two instruments. `sfizz/organ_drawbar`, left hand walking in C2–C3 at full gate. |
| **Ballad** | Tractable harmonically, hardest to fake: exposed tempo, rubato, and every attack audible. |
| **Bebop heads at 240+** | Avoid as a goal. Use bebop *devices* at 150–170 instead — that is what `genre_jazz` does at 160. |

## Instruments

| Role | Reach for | Notes |
|---|---|---|
| Piano | `sfizz` preset **`piano_salamander`** | Three velocity layers; keep comping velocities 45–95 with peaks to 110. Half-left. |
| Lo-fi / upright piano | `OneTrick KEYS/clean_upright`, `tape_upright`, `lofi_bedroom` | for the dusty end |
| Rhodes / EP | `Dexed/ep_rhodes`, `Surge XT/keys_ep` | fusion and trip-hop-adjacent; `CHOWTapeModel/warm_glue` after it |
| Upright bass | `vsco2-solo-contrabass` map, articulation **`pizzicato`** (28–59) | the right sound and the right register. **Do not use `OneTrick CHONK` for a jazz bass** — it is silent below MIDI 48 |
| Tenor sax | `sfizz` preset **`sax_tenor`**, or the `vcsl-tenor-saxophone` maps (`sustain` / `staccato` / `vibrato`, 44–88) | overlap notes for legato; place ~20 ms behind the section |
| Trumpet / trombone | `vsco2-trumpet` (`sustain` 53–84), `vsco2-tenor-trombone` (`sustain` 34–65) | for a three-horn shout chorus |
| Clarinet | `phil-clarinet` `sustain` (50–96) | cool/Dixieland colour |
| Guitar | `phil-guitar` `sustain` (40–80) | Freddie Green four-to-the-bar, or doubling the head an octave down |
| Vibraphone | `vcsl-vibraphone` **`soft-mallets`** (53–88) | the ballad instrument; `bowed` exists too and is a texture nothing else can make |
| Organ | `sfizz` presets `organ_drawbar` / `organ_rock`, or `Surge XT/keys_organ` | organ trio: the left hand *is* the bass |
| Drums | `drumplayer` loaded from the **`gretsch/`** folder — `013_kick`, `020_snare`, `022_snarehard`, `021_snareghost`, `019_ridecymbal`, `018_ridebell`, `010_foothat`, `002_brushsnare`, `007_cymbalgrab` | the only acoustic kit in the packs. `OneTrick URCHIN/acoustic_room` is the alternative |
| Room | `Dragonfly Room Reverb/jazz_club` on the master | one room for the whole band |
| Colour | `CHOWTapeModel/warm_glue` (tape-era 2-bus), `ZamPhono/vinyl_playback` (lo-fi only) | |

Gretsch samples differ by up to 36 dB — `003_brushsnareghost` averages −46.7 dBFS. Measure before
building a kit out of two folders. One `drumplayer` is one stereo source, so ride-right /
kick-centre needs a **second** drumplayer.

## Harmony, melody and the idiom

**Read [docs/Genre_Jazz.md](../../../docs/Genre_Jazz.md) first.** It holds the harmonic and melodic
material for jazz — the voicings, the scales, the root movements, the clichés to
avoid — and it is engine-neutral, so the score side and the research side read the same file.
This skill is how that material is played and produced here.

## Rhythm and sequencing

**Swing has to be written into note positions.** The transport's `swing` control warps
*sixteenths* only, and the swing-interval dropdown lives on the transport singleton, which is not
in the module graph. So compute the position yourself:

```python
SWING = 0.635
def sw(bar, eighth):                       # absolute measure position of swung eighth 0..7
    beat, part = divmod(int(eighth), 2)
    return bar + beat * 0.25 + (0.25 * SWING if part else 0.0)
```

Ratio falls with tempo (Friberg & Sundström, measuring Williams, DeJohnette, Watts, Nussbaum):

| tempo | swing % of the beat | ratio |
|---|---|---|
| ≤100 | 72–78 | 2.6–3.5 : 1 |
| 120–140 | 68–71 | 2.2–2.4 : 1 |
| 160–180 | 64–67 | 1.8–2 : 1 |
| 200–240 | 58–62 | 1.4–1.6 : 1 |
| ≥280 | 50–55 | nearly straight |

**Soloists lag.** Horns and the melody sit ~10–30 ms behind the bass and drums; at 160 BPM that
is `+0.013` measures added to every sax and brass note. It is a measured component of swing feel,
not a fudge.

**The kit goes on a `notecanvas`, not a `drumsequencer`** — a 16-step grid cannot place an eighth
at 63.5 % of a beat. `styles.hits([(bar, pad, velocity)])` writes drumplayer notes at any
position, because a pad index *is* its pitch.

- **Ride, spang-a-lang**: eighths 0, 2, 3, 4, 6, 7 at velocities ~92/82/60/90/80/62 — quarter,
  quarter + swung skip, quarter, quarter + swung skip. Accent 2 and 4 slightly.
- **Hi-hat foot on 2 and 4** (eighths 2 and 6), velocity ~68. Non-negotiable.
- **Snare comping is irregular and sparse.** Pick a rhythmic cell per bar from a list of ~12, four
  of which are **empty**; alternate snare and ghost by position. Add a kick "bomb" at the end of a
  four-bar phrase. Never a backbeat.
- **Brushes** are one-shots (`gretsch/002_brushsnare`) — four a bar reads as "quiet kit", not as a
  swirl. That is the honest limit.

**Comping means not playing where the melody is.** Choose 1–3 hits a bar from a set of cells,
hold 0.16–0.24 measures, alternate A and B voicings, rest whole bars — and then **suppress any hit
within ~0.055 measures of a head attack**. That one filter is the difference between a piano that
answers the phrase and one that doubles it, and it costs six lines.

**Walking bass**: root on 1, the chord's *own* third on 2, the fifth on 3, a chromatic approach
into the next root on 4; the fifth instead of the root on the second bar of a two-bar chord.
`styles.walk_changes([(pos, root, tones), …], start, end)` does exactly this. Do **not** use
`styles.walk()` on a real chart — it takes one scale for the whole tune, so its "third" is the
key's, and that is audibly wrong the moment the chart contains both `Dm7` and `D7`. Range 28–55,
quarters at ~80 % gate, and inside a stopped-changes section let it **stop walking** and hold the
root: when the harmonic rhythm collapses the bass has to say so.

## Arrangement

Head–solos–head is the frame, but the frame is not the composition. What makes 52 bars work is
that **each chorus is a different harmonic treatment of the same twelve bars**:

| bars | section | changes | harmonic rhythm |
|---|---|---|---|
| 0–3 | `vamp` | quartal voicings over an F pedal — no chords at all yet, no third anywhere | none |
| 4–15 | `head` | the Bird blues, two chords to the bar | 1.7 / bar |
| 16–27 | `giant` | first four bars replaced by Coltrane substitutions; bars 5–12 revert | 2 / bar |
| 28–35 | `ballad` | the changes stop: B♭m(maj9) four bars, G♭maj7♯11 four | 0.25 / bar |
| 36–47 | `out` | the same head over the chromatic descending bass, three horns harmonised | 1 then 2 / bar |
| 48–51 | `tag` | tritone sub, then F6/9♯11 | 2 / bar |

Sections are scheduled writes: `bespoke_set_control(path, value, at_measure_time=N)` (absolute,
from the last transport reset). Instruments enter and leave by riding their own gain and by
simply having no notes — the piano **lays out for the whole ballad** and the vibraphone owns it,
which is an arrangement decision a fader cannot express. `snapshots` + `songbuilder` are there if
a section differs in twenty controls at once (see **bespoke-arranging**).

Intros: a 4–8 bar vamp on I, or on the last four bars' turnaround. Outros: tag the last four bars
three times, or land on a 6/9 chord that does not resolve.

## Mixing and mastering

**Pan like a stage, narrow.** Bass centre, kit centre, piano half-left (−0.24), tenor
centre-right (+0.16), trumpet −0.18, trombone +0.34, guitar −0.40, vibes −0.30. Nothing hard
panned. `genre_jazz`'s first render was 3.7 dB right-heavy because the only left-hand voice in two
choruses was the piano; check the balance, do not assume it.

**One room for the whole band.** `Dragonfly Room Reverb`, preset `jazz_club`, on the master —
then expose and tame it, because a Dragonfly at its preset width can push channel correlation
negative and fail the mix's own mono check. The values that measured +0.12 correlation and 0.89
width: `width 0.55 · dry 0.92 · late 0.30 · early 0.22 · size 0.30 · decay 0.28`. A short stock
`freeverb` per voice is the fallback if the plugin's named parameters misbehave on your build.

**Almost no compression.** Dynamics are the genre. `Compressor Stereo/bass_gentle` on the bass if
anything; `ZamComp/drum_snap` in parallel on drums at most. A maximiser on the master **flattens
the arrangement and no check will tell you** — `ZaMaximX2/gentle_ceiling` pins the output at
−4.6 dBFS whatever it is fed.

**EQ** (`Parametric Equalizer x16 Stereo/hpf_and_air`, `mud_cut`): high-pass everything except the
bass at 60–100 Hz, cut 200–400 Hz on piano and organ, do not hype the air. A gentle lowpass on the
piano (~5 kHz, opened across the piece as a scheduled ramp) is a cheap, idiomatic arc.

**Character**: `CHOWTapeModel/warm_glue` on the 2-bus at low drive. Loudness −16 to −14 LUFS
integrated, true peak ≤ −1 dBTP; jazz is mastered quiet on purpose.

## Worked example — `genre_jazz`

```
bespoke_set_transport(tempo=160)                     # 4+12+12+8+12+4 = 52 bars

# 1. the kit, on a canvas because the ride is swung eighths
bespoke_spawn_module("drumplayer", name="kit")
bespoke_load_sample("kit", "<...>/gretsch/019_ridecymbal.wav", slot=3)   # + kick, snare, ghost, foothat, bell
bespoke_set_canvas_notes("ridecanvas", replace=True, notes=[
    {"pitch": 3, "start_measure": sw(bar, 0), "length_measures": 0.05, "velocity": 92}, ...])
# hi-hat foot on eighths 2 and 6; snare comping from 12 cells, four of them empty

# 2. piano: rootless A/B voicings, comping only where the head is not
bespoke_load_plugin("piano", "sfizz"); bespoke_plugin_preset("piano", "piano_salamander")
bespoke_set_canvas_notes("pianocanvas", replace=True, notes=[...])   # suppressed within 0.055 of a head attack

# 3. bass: pizzicato contrabass, walk_changes over the chart
bespoke_set_plugin_state("bass", state_with_sfz(state, ".../solo-contrabass_pizzicato.sfz"))

# 4. the tenor: the head at bar 4, a generated bebop chorus at 16, the head again at 36
bespoke_plugin_preset("sax", "sax_tenor")
#    every note +0.013 measures: the horn sits behind the section

# 5. trumpet, trombone and guitar only in the shout chorus, harmonised by chord tone
# 6. vibraphone owns the ballad; the piano has no notes there at all

bespoke_load_plugin("room", "Dragonfly Room Reverb"); bespoke_plugin_preset("room", "jazz_club")
bespoke_expose_plugin_params("room", names=["width","dry","late","early","size","decay"])
bespoke_set_controls([...])                           # width 0.55, dry 0.92

bespoke_set_control("master~gain", 0.41)
bespoke_set_control("master~gain", 0.74, at_measure_time=origin + 30)   # ride *up* into the ballad
bespoke_set_control("master~gain", 0.58, at_measure_time=origin + 36)

bespoke_wait(measures=52)
bespoke_analyze_audio()
bespoke_get_events()
```

Measured on the committed render: 78.0 s, 52 bars, 44 modules, 11 note sources, 2343 notes, peak
−1.89 dBFS, centroid 2115 Hz ("bright"), correlation +0.12, width 0.89, mono-compatible, 35/52
bars distinct, no clipping. Per section (RMS dB / centroid Hz): vamp −30.5/2818 · head −21.2/2558
· giant −21.7/2433 · ballad −25.1/1798 · out −19.7/2698 · tag −23.6/2534.

## Verify

1. **`bespoke_get_events`** — check the head's pitches against the chart bar by bar. The failure
   this catches is a motif transposed to a note the chord underneath does not contain, which is
   precisely the "beginner" sound.
2. **`bespoke_analyze_audio`** — `spectrum.chroma.dominant` should name chord tones of the bars
   you captured; `stereo.mono_compatible` true; `clipped_samples` 0. A jazz mix with six
   transient-heavy voices (piano, pizz bass, kit, guitar) stacks in the shout chorus — the first
   render of `genre_jazz` clipped 708 samples.
3. **Section levels** — the interlude should read as a *dynamic*, not a hole. Eleven dB under the
   shout chorus is a dropout; five is a section.
4. Expect one standing warning: "onsets average ~21 ms off the 16th grid". That is the swing, and
   it is literally true.

Typical failure modes:

- **The bass outlines nothing.** It is picking from a scale instead of from the chord. Use
  `walk_changes`, not `walk`.
- **The comp doubles the melody.** No suppression filter around the head's attacks.
- **Everything lands exactly on the grid.** Swing was set on the transport (which only moves
  sixteenths) instead of being written into positions.
- **A silent bass part.** `OneTrick CHONK` plays nothing below MIDI 48, and its `upright_ish`
  preset invites exactly the register it cannot play — one shipped demo had an inaudible bass for
  a whole batch and passed every check.
- **The horns do not phrase.** Sampled sustains have no scoop, fall or growl; the 20 ms lag and a
  velocity arc are the entire human budget. Do not expect more from them.
- **Twelve bars, repeated.** If every chorus has the same changes, the piece has no harmonic form
  and no amount of extensions will fix it.
