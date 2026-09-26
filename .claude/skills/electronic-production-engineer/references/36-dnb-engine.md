# Drum & Bass engine: liquid, minimal/deep, UK and US/North-American variants

## General frame
DnB is a high-tempo framework, not one sound. Treat the drum/bass relationship as the foundation and route the musical layer according to subgenre. Avoid assuming that louder or more complex equals more professional.

## Numbers, grid and structure
Evidence tags: `80-evidence-policy.md`. The repo holds DnB-wide data only; nothing liquid-, minimal- or US-specific is measured.
- **Tempo**: Beatport Drum & Bass Top 100: 174 (58 tracks), 176 (16), 172 (8) [DOC WhatBPM 2023]; theory table 160–180, typical 174, felt 87 in half-time [DOC-2]. Mean Beatport length 3:51 [DOC].
- **Keys**: manual annotations 82 % minor, G minor 32 %, F minor 21 % (n = 38) [DOC GiantSteps]; Beatport roots F, D, E♭ [DOC WhatBPM, auto-keys]. The theory compilation's "C minor most common" [DOC-2] is not supported by these data.
- **Swing**: 50–60 % [DOC-2, Attack]; the studio grid swings the ghost snares only, `swing(0.02, n/16)`, whose unit is undocumented: read the clip back [HEUR; TEST].

Two-step starting grid, 174 BPM (`../../drums-signature/references/patterns.md`, `../../drums-signature/scripts/drum_pattern.py` dnb) [HEUR]:
```
            1 e & a 2 e & a 3 e & a 4 e & a
kick        X . . . . . . . . . X . . . . .   v110–118 (variant: step 8 instead of 11)
snare       . . . . X . . . . . . . X . . .   v100–110
ghost snare . . . o . . . . . o . . . . . o   v30–45, swing on these only
hat 1/8     x . x . x . x . x . x . x . x .   v70–84 (or 16ths at v50 as ghosts)
open hat    . . . . . . x . . . . . . . . .   v56–64
```
Fill every 8 bars: snare on steps 14, 15, 16 rising (v70–96). Layer a sliced break (Amen, Think) high-passed at 200 Hz at ghost level so the programmed kick and sub own the bottom [HEUR]. Amen grid and half-time/double-time notes: `../../theorie-musicale-electronique/references/rythme-avance.md` §5 [DOC-2].

- **Structure**: intro 32 · build 16 · drop 1 64 (two varied halves of 32) · mid 16–32 · breakdown 32 (often drumless) · build 16 · drop 2 64 (harder) · outro 32 [COMM]. 32 bars at 174 ≈ 44 s; the whole form (272–288 bars) ≈ 6:15–6:37 [CALC].
- **Bass architecture**: one source owns the fundamental — a mono sine sub, unison 1, no detune, low-passed near 120 Hz; reese or growl mids high-passed near 120 Hz above it [DOC-2]. Reese start: 2 saws at ±27–30 cents (±15 = slow and soft), mono/legato, LP 24 dB ≈ 650 Hz, resonance ≈ 14 %, light overdrive [DOC-2]. The beat rate changes with the note, so set the detune on the lowest note [HEUR]. Neuro/growl chain: filter movement → distortion → compression → EQ clean-up, LFO in trigger mode, resample at least twice [DOC-2, low-reliability preset-vendor sources].
- **Detail**: `../../sound-designer-serum/references/basses.md` §1–3; `../../theorie-musicale-electronique/references/forme-tension.md` §1, §3; `../../theorie-musicale-electronique/references/genres.md` (Drum & bass / jungle); groove method `../../producteur-rythmique/SKILL.md`.

## Liquid DnB DNA
Priority: musicality, emotion, clean sub, fluent drums, atmosphere and long-form development.
- Start from chords, hook, vocal or atmosphere when that is the emotional core.
- Samples can provide authenticity and glue; pitch, chorus, delay and reverb should place them in the same world rather than merely decorate them.
- Drums can be comparatively restrained when harmony/vocal carries the track.
- Breakdowns should develop musical material, not only mute drums.

### Reference anchors
- Calibre: simplicity, soul, natural flow and restraint.
- Hybrid Minds / LSB / Monrroe: modern melodic/liquid reference family.
- Random Movement: US soulful/liquid reference with jazzy/deep writing.
- Justin Hawkes (formerly Flite): US DnB with strong songwriting and cross-genre range.

## Minimal / deep DnB DNA
Priority: drum/bass funk, negative space, precision, texture and small numbers of strong sounds.
- Kick/snare/rim choice matters more because fewer layers hide them.
- Bass phrases can be extremely simple; movement comes from envelope, timbre, small automation and groove.
- Use textures, reverb and sparse stabs to create depth without clouding the core.
- Gated/resequenced breaks and micro-edits can create funk without extra notes.

### UK reference anchors
- Alix Perez: deep low-end, emotional restraint, high mix discipline.
- Skeptical: effective simplicity, rim/snare identity, drum patterns, low/mid manipulation.
- DLR: raw funk, drums/bass focus and strict minimal arrangement.
- Break: clean, powerful drum/bass mix and strong groove benchmark.

## US / North-American DnB profile
This is not a separate rulebook, but current US-facing production often blends DnB with dubstep/bass-music songwriting and sound design more openly than traditional UK minimal aesthetics.
- Justin Hawkes: songwriting plus technically polished DnB.
- Kumarion: DnB sound-design discipline mixed with broader bass-music freedom.
- REAPER: aggressive 170-BPM hybrid, dubstep influence, heavy bass and vocal-driven songwriting.
- Random Movement: soulful US liquid lineage.

Use the profile only when the user explicitly wants a US/American crossover aesthetic; do not stereotype all US DnB as heavy.

## Drum construction
### Kick
Short enough to leave space for sub unless long-tail character is intentional. Combine synthesized low body and an acoustic/electronic transient only when each layer has a clear role.

### Snare
DnB snares often benefit from explicit layer roles:
- transient/crack;
- tonal body;
- noise/air;
- optional room/tail.

FM synthesis is a valid route for a crisp electronic body; resample the result once it responds musically.

### Breaks
Layer programmed one-shots with sliced/resequenced breaks for movement. Remove low-frequency mud from break layers when the dedicated kick/sub should own the bottom.

## Bass
- Keep a clean sub path separate from complex mids when possible.
- For minimal/deep: fewer notes, stronger envelope/timbre.
- For liquid: sub should support harmony and not distract from chords/vocal.
- For aggressive US hybrid/neuro-influenced work: complex FM/wavetable resampling can be central, but phrase clarity still beats constant density.

## Arrangement
### Liquid
16-bar musical idea -> gradual drum/bass introduction -> main section -> melodic breakdown -> developed return. Filters, reverbs, delays and samples carry transitions.

### Minimal/deep
Main groove -> 2/4/8-bar disruption -> groove return with one meaningful variation. Micro-edits and drum/bass changes often matter more than giant EDM builds.

### Aggressive/hybrid
Clear tension ramp -> impact/gap -> drop with bass call-and-response -> mid-drop switch/fill -> breakdown/song section -> second drop with a genuine variation.

## Mix/QC
- Compare at level-matched loudness.
- Preserve kick/snare transient identity at the target density.
- Check whether the sub is stable through every bass phrase.
- Avoid widening the fundamental low-end.
- At high BPM, long reverb tails can mask multiple subsequent hits; shorten, duck or frequency-limit them deliberately.
