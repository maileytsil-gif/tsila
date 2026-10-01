---
titre: "colfitt/arlo-genesis — fiche Wavetable, Drift, Meld (paramètres, usages)"
source: https://raw.githubusercontent.com/colfitt/arlo-genesis/HEAD/arlo/corpus/daw/ableton/devices/wavetable-drift-meld-synths.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: Ableton Live 12 ; instruments ; notes tierces
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

# Wavetable, Drift, and Meld — Live's Modern Synth Family

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Wavetable, Drift, Meld; Ableton blog — The New Wave (Wavetable, Live 10), Drift (Live 11.3), Meld (Live 12); Sound on Sound *Ableton Live Drift Synthesizer*, *Ableton Live: Meld*
**Tags:** `daw-ableton`, `live-12`, `device`, `wavetable`, `drift`, `meld`, `mpe`, `synthesis`

---

## The version lineage matters

These three synths arrived in three different Live versions and they are *not* interchangeable. **Wavetable** [shipped with Live 10 in November 2017](https://www.ableton.com/en/blog/new-wave-depth-look-wavetable/) and got iterative additions through Live 10.1 and 11 (user wavetables, MPE). **Drift** arrived in [Live 11.3](https://www.ableton.com/en/blog/drift-exploring-the-new-synth-in-live-113/) (mid-2023) and ships with all editions of Live (including the free Intro), continuing into Live 12 unchanged. **Meld** is the Live 12 newcomer — it ships with Live 12 Suite only and represents the most expressive of the three. The DAW-stream prompt row lumps them as "Live's modern synth family" but the version-stamping rule of the stream means: if a tutorial calls Drift "Live 12's new synth," it's wrong (Drift is Live 11.3); if it calls Meld a Live 11 device, it's wrong (Meld is Live 12). Wavetable is the only one of the three that's been around long enough that pre-Live-12 tutorials still describe it accurately.

## Wavetable — what's under the hood

[Wavetable](https://www.ableton.com/en/manual/live-instrument-reference/) has two main oscillators plus a dedicated sub-oscillator. Each main oscillator scans through a wavetable (a stored sequence of single-cycle waveforms) via a **Position** knob — automating Position is the headline wavetable move. Each oscillator has a Mode chooser with three options: **Classic** (the wavetable plays as-is), **Modern** (a more digital, "harder" filter on the scan), and **FM** (the oscillator's frequency is modulated by a hidden auxiliary oscillator with a tunable Amount and Tuning). Wavetable ships with hundreds of factory wavetables organized by category (Bass, Pad, Synth, Vocal, etc.) — drag a sample onto the oscillator window in Live 10.1+ to create a user wavetable from any audio source. The sub-oscillator offers a sine with selectable octave, and an Additional Harmonics control for adding low-end body. Live 10+ Wavetable is MPE-aware — per-note pressure, slide, and glide all route through the modulation matrix.

## Wavetable's filter, envelopes, and modulation matrix

Wavetable features [two filter slots, each with five circuit models](https://performodule.com/2019/03/07/abletons-auto-filter-comparing-circuit-models/): **Clean** (digital, transparent), **OSR** (Oxford OSCar state-variable), **MS2** (Korg MS-20 Sallen-Key, soft-clipping), **SMP** (custom Sallen-Key hybrid), and **PRD** (Moog Prodigy ladder, "pokey" resonance). Each filter can be 12 dB or 24 dB slope, type-selectable (LP, HP, BP, notch, morph). Three envelopes and two LFOs drive the **modulation matrix** — click on almost any parameter to add it as a modulation target. The matrix is destination-based: you choose what to modulate, then pick a source for that destination. The third envelope is the killer — assign it to Oscillator 1 Position and you have wavetable scan as a programmed evolution per note. Live 12's Tuning Systems and project Scale are respected by Wavetable for microtonal and scale-aware playback.

## Wavetable patch-design starting points

**Wobble bass:** Oscillator 1 a "Bass" or "Pulse" wavetable, Position 0, scan modulated by LFO1 (tempo-synced 1/8 or 1/16). Oscillator 2 off, sub-oscillator at -1 octave. Filter 1 LP 24 dB, MS2 model, cutoff modulated by LFO1 in tandem with Position (lockstep wobble). Voices = 1, Glide ~20 ms. The classic Wavetable bass patch.

**Pad:** Oscillator 1 a "Pad" or "Vocal" wavetable, Position modulated by Envelope 3 over 5–10 seconds (slow evolution). Oscillator 2 detuned (Coarse +12), different wavetable for layered movement. Filter 1 LP 24 dB, PRD or Clean, cutoff modulated by LFO at 0.3 Hz. Long attack, long release. Voices 8, Unison on.

**Lead:** Oscillator 1 saw or "Synth" wavetable. Oscillator 2 same, detuned ~+15 cents. Filter 1 LP 24 dB at ~1.5 kHz. Envelope 1 → Filter cutoff with quick attack and decay. Mono mode with Glide 40 ms.

**Pluck:** Oscillator 1 a percussive wavetable (Plucked Strings category), Mode = Classic. Sub-oscillator off. Envelope 1 fast attack, fast decay, no sustain. Filter LP at 5 kHz with envelope-driven cutoff.

## Drift — the lightweight modern subtractive

[Drift](https://www.soundonsound.com/techniques/ableton-live-drift-synthesizer) (Live 11.3+, included with all Live editions) is a small two-oscillator subtractive synth optimized for low CPU and friendly Push-style graphics. Oscillator 1 has multiple modes where the **Shape** control behaves differently per mode: wave folding on sine/triangle, sync sweep on saw/pulse, pulse-width modulation on square, progressive clipping on a hybrid mode. The synth includes a low-pass filter with selectable 12 or 24 dB slope plus tonal modelling, alongside a high-pass filter. Notable: the resonance behavior is dynamic — at high input levels resonance diminishes, at lower levels it becomes more pronounced and can self-oscillate. Two envelopes and one LFO drive modulation; Envelope 2 can enter looping mode and become a function-generator-style modulator with Tilt, Hold, and Ratio shape controls. The **Drift** control — the device's namesake — introduces analog-style instability altering pitch and tone of each voice. Voice modes are **Poly, Mono, Stereo, Unison**; Mono with Amount above 0% blends sub-oscillators for fatness.

## Drift patch-design starting points

**Sub bass / 808:** Oscillator 1 sine, Mode 1. Envelope 2 routed to filter cutoff (default routing). Filter LP 24 dB at 200 Hz, mild resonance. Voice mode Mono with Amount ~30% for sub blend. Drift ~10% for warmth. Pitch envelope on the attack for an 808-style downward sweep.

**Lead:** Oscillator 1 saw, Oscillator 2 saw +12 semitones. Filter LP 12 dB at ~1 kHz, resonance ~50%. LFO → filter cutoff at ~4 Hz, depth ~20%. Voice mode Mono, Glide 30 ms, Drift ~15% for analog drift on sustained notes.

**Pad:** Oscillator 1 saw, Oscillator 2 triangle one octave up. Voice mode Stereo with Drift ~25% — this is where Drift shines as a pad synth, the stereo voice spread plus per-voice instability gives organic motion. LFO slow on cutoff. Long attack and release.

**Pluck:** Oscillator 1 saw, Mode with progressive clipping for harmonic richness on the attack. Filter HP 12 dB ~80 Hz to clear sub. Envelope 1 fast attack, 200 ms decay, no sustain. Key-tracking on filter cutoff for consistent tone across the keyboard.

## Meld — the Live 12 macro-oscillator synth

[Meld](https://www.ableton.com/en/blog/meld-a-look-at-live-12s-new-bi-timbral-synth/) is bi-timbral — two complete synths (Synth A and Synth B) in one device, each with its own oscillator, filter, envelopes, LFOs, and modulation matrix. The "meld" happens when modulations are patched from Synth A to Synth B (or vice versa), creating cross-modulation. Each engine has **24 oscillator types** chosen from a Mode chooser, including basic waveforms, harmonic FM oscillators, granular, fizzy folded FM, Bitgrunge, Shepard's Pi, and six **scale-aware** oscillators that quantize their output to the current Live 12 project Scale. Each engine has **two macro knobs** that change behavior based on the oscillator type loaded — e.g., the Basic oscillator's macros are Shape (morphs sine through triangle, ramp, square) and Tone (pulse-width); the Harmonic FM oscillator's macros are Amount and Ratio. This per-oscillator macro design is what makes Meld friendly: you don't tweak twenty parameters, you tweak two that already mean something for the sound.

## Meld's modulation matrix and MPE

The Meld modulation matrix opens above the main panel via a toggle button. Modulation sources include LFOs, envelopes, MIDI controls, and a full set of **MPE** controls (Slide and Press for per-note expressivity on MPE-capable controllers like Push 3 or LinnStrument). Cross-modulation between Synth A and Synth B is a first-class workflow — patch a slow LFO in A to modulate B's filter cutoff for evolving textures, or patch Synth A's envelope to Synth B's oscillator macro for "trigger one voice with another" character. Meld also has scale-aware modulation: pitch modulation can be quantized to Live 12's project Scale, producing in-key glissandi rather than chromatic sweeps. The **Spread** function can be used as a modulator across multiple parameters simultaneously.

## Meld patch-design starting points

**Textural pad:** Synth A oscillator = "Bitgrunge" or "Folded FM," Synth B = a granular oscillator. Cross-modulate A's LFO to B's filter. Voice mode Poly, slow attack, long release. Slide (MPE) routed to A's filter cutoff for expressive per-note tone.

**Drone / scale-aware sequence:** Synth A on a scale-aware oscillator, Synth B off. LFO modulating pitch with quantized output — produces in-key arpeggiation without a MIDI sequence. Cross-link to Live 12's per-project Scale (set in the toolbar) for harmonic consistency.

**Bass:** Synth A on a Basic oscillator with Shape morphed toward square, Tone at 30%. Synth B off. Filter LP 24 dB at 250 Hz with envelope-driven cutoff. Voice mode Mono, Glide 20 ms. Macro mapping puts everything on the front panel.

**Lead:** Synth A on Harmonic FM oscillator, macros set Amount ~50%, Ratio at integer values. Synth B saw +12. Filter LP at 2 kHz with LFO modulation. MPE Slide → filter cutoff, MPE Press → modulation depth.

## When to reach for which

A working decision tree:

- Need a fat analog bass or pad with minimal CPU → **Drift**.
- Need wavetable scanning, morphing timbres, or modern bass design → **Wavetable**.
- Need expressive MPE performance with rich textural variety → **Meld**.
- Already on Live Standard / Lite (no Suite) → **Drift** is your only modern subtractive synth (Operator/Analog/Wavetable/Meld are Suite-only).
- Need to lay down a quick sketch with Push's macro knobs → **Drift** (designed for Push graphics) or **Meld** (macro-per-engine design).
- Working with scale-aware MIDI generators and want the synth to respect Scale → **Meld** (scale-aware oscillators) or **Drift** (just respects MIDI input).
- Patch needs to evolve over many seconds → **Wavetable** (Envelope 3 → Position) or **Meld** (A→B cross-mod).

## CPU and freezing

Drift is the cheapest of the three by a meaningful margin — Ableton designed it explicitly for low-CPU usage and it's the only modern stock synth that runs comfortably in dozens of instances. Wavetable is mid-cost; Meld is the most expensive (24 oscillator types per engine, two engines, cross-modulation). For Meld-heavy sessions, freeze any committed Meld tracks; for Wavetable patches with active third-envelope Position modulation, freeze if the modulation is finalized. Drift rarely needs freezing for CPU reasons. All three respect Bounce in Place (Live 12) for non-destructive commit.

## MPE quick reference

Wavetable, Drift, and Meld are all MPE-aware in Live 12. To enable: right-click an instrument's title bar → MPE / MIDI options. With an MPE controller (Push 3, LinnStrument, Roli Seaboard, etc.) the per-note pressure (Press), per-note pitch (Slide), and per-note y-axis controls become available modulation sources. In Wavetable and Meld, drag the MPE source into the modulation matrix and pick a destination (e.g., Press → Oscillator 1 Position for per-note timbre control). Drift exposes MPE as a target via Envelope 2 looping mode and LFO routing. MPE in Live 12 also supports per-note editing in the MIDI editor — automate Slide / Pressure / Y per note in a clip.

## Cited Retrieval Topics

- "what's new in meld synth ableton live 12"
- "how do i use drift synth in ableton"
- "wavetable bass patch ableton tutorial"
- "what version of live did drift come out in"
- "wavetable vs meld vs drift when to use which"
- "mpe synth in ableton live 12"
- "scale aware oscillators meld ableton"
- "how to make an evolving pad in wavetable ableton"
- "cpu cost of ableton stock synths"
- "ableton drift mono bass patch"

## Sources

- [Live Instrument Reference — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/live-instrument-reference/)
- [Ableton blog — The New Wave: An In-Depth Look at Live 10's Wavetable](https://www.ableton.com/en/blog/new-wave-depth-look-wavetable/)
- [Ableton blog — Drift: Exploring Live's New Synth (Live 11.3)](https://www.ableton.com/en/blog/drift-exploring-the-new-synth-in-live-113/)
- [Ableton blog — Meld: A Look at Live 12's New Bi-Timbral Synth](https://www.ableton.com/en/blog/meld-a-look-at-live-12s-new-bi-timbral-synth/)
- [Sound on Sound — Ableton Live Drift Synthesizer](https://www.soundonsound.com/techniques/ableton-live-drift-synthesizer)
- [Sound on Sound — Ableton Live: Meld](https://www.soundonsound.com/techniques/ableton-live-meld)
- [MusicRadar — The ultimate guide to Meld, Ableton Live 12's new synth](https://www.musicradar.com/news/ableton-live-12-ultimate-guide-to-meld)
- [PerforModule — Ableton's Auto Filter: Comparing Circuit Models](https://performodule.com/2019/03/07/abletons-auto-filter-comparing-circuit-models/)
- [Production Music Live — Wavetable Synth in Ableton 10 Explained](https://www.productionmusiclive.com/blogs/news/live-10-s-new-wavetable-synth-explained)

See also: `corpus/synthesis/subtractive-synthesis-fundamentals.md`, `corpus/synthesis/fm-and-wavetable-synthesis.md`, `corpus/synthesis/patch-design-vocabulary.md`, `corpus/daw/ableton/devices/operator-analog-synths.md`, `corpus/daw/ableton/timeless/wavetable-mpe-workflow.md` (planned)
