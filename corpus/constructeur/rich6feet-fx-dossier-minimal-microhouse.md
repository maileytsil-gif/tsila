---
titre: "FX dossier — effets, routage et chaînes pour minimal / microhouse / deep, avec table de correspondance rack FX Serum et devices Live (rich6feet/serum)"
source: https://raw.githubusercontent.com/rich6feet/serum/main/docs/fx_dossier.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur ; Serum 2 ; format de preset et paramètres (rétro-ingénierie tierce)
skills: sound-designer-serum, vst-sound-design, studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# FX DOSSIER

**Effects, Routing, and Preset Logic for Minimal / Microhouse / Deep-House Production**

*Drawn from a workflow lineage influenced by Ricardo Villalobos, Sonja Moonear, Levon Vincent, and the broader Perlon / Cocoon / Novel Sound aesthetic.*

---

## 0. How to Read This Document

This dossier is structured to be both human-readable and machine-parseable. Sections 1–7 are the philosophical and engineering substance; Sections 8–10 are formal schemas and mapping tables intended to be consumed by an LLM (Cursor / Claude Code / a downstream agent) to instantiate presets on any target — Eventide H9000, Bitwig Grid, Serum FX, Ableton Audio Effect Racks, Reaktor, hardware pedals, etc.

When extending this document, **preserve the field names** in the schema (Section 8). The agent layer downstream is expected to map `node.type` and `param` keys to platform-specific equivalents.

---

## 1. Foreword — The Operating Philosophy

The records that defined this scene weren't made by people chasing "presets." They were made by people who treated the studio as one large, slow, *misbehaving* instrument. Effects in this world are not things you put on at the end. They are the composition. A Villalobos record is largely a feedback path with a kick drum poking through it. A Sonja Moonear record is reverb tails making harmonic decisions. A Levon Vincent record is the difference between a perfectly dry kick and a flooded synth, sitting next to each other and refusing to blend.

A few principles you will see repeated below:

- **Negative space is an effect.** Ducking, gating, and silence are processed elements. They are not the absence of processing.
- **Drift is a feature.** Pitched-pitched-stable signals sound dead. Everything benefits from sub-cent wander, sub-Hz LFOs, or analog-style instability.
- **Feedback is the instrument.** A delay's feedback knob is more important than its time knob. A reverb's send return into another reverb's send is where the record actually lives.
- **Order of operations is non-negotiable.** Saturation → comp ≠ Comp → saturation. Reverb → distortion ≠ Distortion → reverb. The chain is the sound.
- **Not everything should be in time.** Free-running LFOs, tempo-independent delay ratios (e.g. 437 ms at 124 BPM), and slightly-wrong swing values are how a track stops sounding like a grid.
- **Headroom and safety first.** Most of what's described here involves feedback paths and resonance. Without limiters in the right place, you'll lose tweeters.

---

## 2. The Aesthetic Pillars

Before listing effects, name the targets. Every preset/chain in this dossier is in service of one or more of these pillars.

| Pillar | Description | Sonic Indicator |
|---|---|---|
| **Depth** | The sense that the mix has a back wall 40m away | Long pre-delays, dark reverb tails, sends-into-sends |
| **Drift** | Nothing sits perfectly still | Slow detune, micro-pitch, wow/flutter, sub-audio LFOs |
| **Dub Space** | Elements appear and dissolve, not start and stop | Feedback delays with EQ in the loop, ducked reverbs |
| **Grit** | Analog character without obvious distortion | Tape sat, transformer color, low-level hiss/hum, bit-floor noise |
| **Air** | Top-end shimmer that isn't harsh | High-shelf saturation, plate verbs HPFed at 2k, micro-pitch up |
| **Restraint** | The effect is *barely* audible until removed | Send levels at –20 to –30 dB, dry-only A/B reveals what was there |
| **Off-Grid Pulse** | Rhythmic life that resists quantization | Free-running tempo-unsynced delays, polyrhythmic LFOs, swing not on the grid |

Any preset's intent should reference one or more of these.

---

## 3. The Effect Taxonomy

Each subsection lists the effect, what it is *actually doing* in this scene, key parameters, and the less-obvious knowledge.

### 3.1 Spatial — Reverbs

#### 3.1.1 Dark Hall (the "Echospace" reverb)
- **Use:** Stems sit *inside* the room, not in front of it. Used on chords, vocal phrases, hats.
- **Key params:** Decay 6–14s, Pre-delay 60–120 ms, Damping high (top end rolls off in the tail), Diffusion >80%.
- **Engineering:** Always HPF the *input* at 150–200 Hz. Always HPF the *return* at 200–300 Hz. The low end is for kicks, not for tails.
- **Less obvious:** Modulate the damping with a slow LFO (0.05 Hz, ±10%). The room appears to "breathe."
- **Hardware ref:** Lexicon 480L "Random Hall," Bricasti M7 "Dark Hall," Eventide Blackhole, Valhalla VintageVerb (Concert Hall, dark mode).

#### 3.1.2 Plate (the "Levon" plate)
- **Use:** On synths and snares for size without smear. The Vincent move is dry kick, *huge* plate snare or stab.
- **Key params:** Decay 2.5–4s, Pre-delay 20–40 ms, top boost around 8–10k, low cut at 250 Hz.
- **Engineering:** Plates eat top end. To recover air, parallel-saturate the wet return with a high-shelf tape model.
- **Less obvious:** A plate sidechained *to itself* (compressor on the wet return keyed by the wet signal) creates a self-ducking shimmer — sounds nothing like a normal plate.
- **Hardware ref:** EMT 140, AMS RMX16 "Plate," UAD EMT 140, Valhalla Plate.

#### 3.1.3 Spring (the "Sonja" tactile reverb)
- **Use:** On percussion and field-recording elements. Adds physicality, twang, and a sense that air is moving.
- **Key params:** Decay 1–2s, drive medium, tension/twang to taste.
- **Engineering:** Spring reverbs distort musically when hit hard. Send a transient-rich signal at +3–6 dB into the spring, then pad the return down. The clang character is the point.
- **Less obvious:** Run a spring after a granular processor — the spring softens the digital edges of granular artifacts.

#### 3.1.4 Convolution with Non-IR Sources
- **Use:** Use a single drum hit, a vocal vowel, or a piece of room tone *as the impulse response*. The reverb takes on the harmonic content of the IR.
- **Key params:** IR length 200ms–4s, predelay variable, wet-only return.
- **Engineering:** Normalize and HPF your custom IR before loading. Long IRs eat CPU; freeze the return when not editing.
- **Less obvious:** A loop of a closed hi-hat used as an IR turns any sustained sound into a rhythmic, breathing texture. This is one of the cleanest "Villalobos-flavor" moves.

#### 3.1.5 Ducked Reverb (Sidechain Verb)
- **Use:** The reverb only blooms in the gaps between hits. Critical for keeping mixes clean while still huge.
- **Routing:** Reverb on a return bus → compressor on the return, sidechained from the dry source (or from the kick).
- **Key params:** Comp ratio 4:1–10:1, attack fast (5–15 ms), release tuned to the gap (often 1/8 dotted at the BPM).
- **Less obvious:** Sidechain only the *low and low-mid bands* of the reverb return (multiband / dynamic EQ). The high air keeps shimmering even while the body ducks.

---

### 3.2 Spatial — Delays

#### 3.2.1 The Dub Chamber
This is *the* signature routing of the entire scene. Build it once as a return; use it on everything.

- **Topology:**
  ```
  Send → [HPF 200Hz] → [Tape Delay (analog model)] → [Resonant LPF in feedback loop]
                              ↓ (wet tap)
                              → [Spring or Plate Reverb] → Return
  Feedback path: from delay's wet output, EQed, back into delay input.
  ```
- **Key params:**
  - Delay time: 1/4 dotted, 3/8, or *unsynced* at e.g. 412 ms
  - Feedback: 55–75% (with limiter safety, see §6)
  - In-loop LPF: cutoff 2–4 kHz, resonance at the edge of self-oscillation
  - In-loop HPF: 180–250 Hz, prevents low-end buildup
- **Engineering:** Put a brickwall limiter at –1 dBFS on the return *outside* the feedback loop. Inside the loop, a soft-clipper or tape sat keeps things from squealing without sterilizing the feedback character.
- **Less obvious:** Modulating the delay time with a 0.05–0.2 Hz LFO at ±2–8% creates a tape-warble shimmer that turns mechanical loops into living tissue. *This is a Villalobos hallmark.*

#### 3.2.2 Multitap Polyrhythm
- **Use:** Six to twelve taps with non-musical spacings to create textural rhythms from a single hit. UltraTap-style.
- **Key params:** Taps 8–12, slope (energy distribution) front- or back-loaded depending on intent, predelay 0–100 ms, tap pan random.
- **Less obvious:** The "slope" parameter is more important than the tap count. Front-loaded slopes feel like rooms; back-loaded slopes feel like reverse reverbs. Mid-loaded slopes sound like granular clouds.
- **Hardware ref:** Eventide UltraTap (H9, H9000 algorithm).

#### 3.2.3 Cross-Stereo Ping-Pong (with decorrelation)
- **Use:** Mono source, stereo result, but *not* obvious ping-pong. The taps are slightly different durations on each side and pass through different filters.
- **Key params:** Left tap = T, Right tap = T × 1.013 (or any slight irrational ratio), each side filtered differently.
- **Less obvious:** The decorrelation is what makes this not sound like a cliché. Identical taps on both sides = phasey. Slightly different taps = wide and natural.

#### 3.2.4 Frozen Delay / Looper
- **Use:** Capture a snippet, hold it, modulate it. Often used to bridge sections.
- **Engineering:** When freeze is engaged, the input is muted into the loop but the loop continues. Always have a kill switch on the bus.
- **Less obvious:** A frozen delay run *into a reverb* is functionally a granular pad. You can make whole chord progressions out of one captured note plus a slow micro-pitch shifter inside the frozen loop.

---

### 3.3 Modulation

#### 3.3.1 Micro-Pitch (Detune Doubler)
- **Use:** Width and life on mono signals. ±5–15 cents.
- **Key params:** Two voices, detuned ±7 cents typical, panned hard L/R, mixed at –9 to –12 dB under dry.
- **Less obvious:** Modulate the detune *amount* (not just the pitch) with a slow LFO. The width breathes. This is the "H3000 micropitch" trick — universally useful on pads, chords, vocals.
- **Hardware ref:** Eventide H3000 MicroPitch, Soundtoys MicroShift, Valhalla UberMod (mod-only).

#### 3.3.2 Frequency Shifter (NOT Pitch Shifter)
- **Use:** Non-harmonic shifting destroys the harmonic series, which is exactly what you want on percussive metallics. A snare shifted +37 Hz becomes an alien artifact.
- **Key params:** Shift in Hz (not cents): ±5 to ±100 Hz typical. Often used in feedback paths.
- **Engineering:** A frequency shifter inside a delay feedback loop creates Bode-shifter-style barber-pole effects. Each repeat shifts further from the original until inaudible. Tame with the in-loop LPF.
- **Less obvious:** Shift +0.1 Hz is essentially a chorus that never repeats. Shift +0.5 Hz is a slow shimmer. Shift +5 Hz is animation. Above 20 Hz becomes obvious dissonance.

#### 3.3.3 Comb Filter (Resonant Tuned)
- **Use:** Pitch a noisy or unpitched source. Tune the comb to the song's key.
- **Key params:** Frequency = 1/(target_freq), feedback 60–90%, mix wet-heavy.
- **Less obvious:** Combs at sub-audio rates (very long delay times, e.g. 100 ms) become flangers. At very short delays (sub-1ms) they become pitched resonators. Sweep between the two with a slow envelope and you have a "Karplus-Strong" pluck on any source.

#### 3.3.4 Phaser through Delay
- **Use:** A phaser placed *before* a long delay turns each repeat into a different harmonic state. The repeats dissolve up the spectrum.
- **Routing:** Source → Phaser (slow rate, deep, high feedback) → Delay (long, high feedback) → Reverb.
- **Less obvious:** Reverse the order (delay before phaser) and the phaser modulates the entire decaying tail — different effect, also useful, more aggressive.

#### 3.3.5 Ring Modulator (Restrained)
- **Use:** On a single percussion element, ring mod at 80–250 Hz adds a metallic, bell-like tone. Used sparingly, it's the difference between "drum loop" and "object."
- **Engineering:** Always parallel-blend (10–25% wet). Full wet ring mod is a 1990s sound effect.
- **Less obvious:** Modulate the carrier frequency with an envelope follower keyed by the source. The ring mod tone *follows the dynamics* of the input. This is one of the most under-used techniques in this aesthetic.

---

### 3.4 Saturation, Distortion, Coloration

#### 3.4.1 Tape Saturation (Bus-Wide)
- **Use:** Glue, low-end softening, top-end taming, tiny wow/flutter for life.
- **Key params:** Drive moderate (so peaks compress 1–2 dB), bias to taste, wow ~0.05 Hz at ±0.05%, flutter ~6 Hz at ±0.02%.
- **Engineering:** Tape is non-linear; it changes the spectrum *and* the dynamics. If you A/B with a static gain match, you may not hear the change — disable the wow/flutter for the A/B, then re-enable.
- **Less obvious:** Tape saturation on a *send return only* keeps the dry signal pristine. Send drum bus to a tape return, blend –10 dB. Drums get the tape grit on transients without losing attack on the dry path.

#### 3.4.2 Transformer Color
- **Use:** Adds even-order harmonics, particularly on the low end. Low-frequency content gets a subtle weight without volume.
- **Key params:** Drive 0–6 dB into the transformer model, output normalized.
- **Less obvious:** Transformer on the *mid* of an M/S split is rounder; on the *side* it brings out air. Two instances, one per M and S, with different drives, is a finishing trick.

#### 3.4.3 Bitcrush as Texture (not Lo-Fi)
- **Use:** *Subtle* bitcrushing — 12–14 bits, often paralleled at –18 dB — adds a faint grit-floor that sits under everything. Most listeners don't hear it consciously, but A/B reveals a flatter, deader mix without it.
- **Engineering:** Always pair with an LPF post-crush to tame the aliasing.
- **Less obvious:** Bitcrush + analog modeling LPF is the classic "Roland TR-909 sample memory" character. Useful on hats and shakers.

#### 3.4.4 Soft-Clip / Saturation in Feedback Loops
- **Use:** Inside delay/reverb feedback paths to keep them from running away while preserving character. Replaces the "hard limiter" approach which sounds sterile.
- **Engineering:** Place a low-distortion soft-clipper (e.g. tanh, or a transformer model) inside the feedback path. Set it so peaks just *kiss* the clip ceiling at maximum feedback.

---

### 3.5 Dynamics

#### 3.5.1 Sidechain Compression (the "breath")
- **Use:** The pumping that defines the genre's groove. Not just on the bass — on pads, hats, reverb returns, and the master.
- **Key params:** Ratio 4:1–8:1, threshold to taste, attack 1–10 ms, release tuned to the off-beat (typically 80–180 ms at 124–128 BPM).
- **Less obvious:** Use a *muted ghost kick* (kick MIDI, but the kick is bypassed) as the sidechain trigger. The pump exists even in passages where the kick doesn't. Levon Vincent uses this constantly.

#### 3.5.2 Dynamic EQ as Multiband Sidechain
- **Use:** Duck only the frequency range that's clashing. The kick triggers a 60–120 Hz cut on the bass, leaving the mids of the bass alone.
- **Engineering:** This is cleaner than full-band sidechain compression and preserves the perceived loudness of the bass. Modern de facto standard, but underused in older minimal templates.

#### 3.5.3 Transient Designer (Subtractive)
- **Use:** Pull *down* attack on overly clicky drum samples to make them sit. Or pull *up* sustain on closed hats to give them body without changing pitch.
- **Less obvious:** Transient design on a *reverb return* — pulling down attack on the wet — makes the reverb feel like it starts late, even with zero predelay. Strange and beautiful.

#### 3.5.4 Gate as Creative Tool
- **Use:** Aggressive gating on a sustained pad creates rhythmic stutters tied to a sidechain key.
- **Routing:** Pad → Gate (sidechained from a hi-hat or shaker pattern) → Reverb (post, so the gated pad blooms in the gaps).
- **Less obvious:** A gate keyed by a *different* musical element creates polyrhythmic life. Pad gated by hat = pad-as-rhythm.

---

### 3.6 Spectral and Time-Domain

#### 3.6.1 Spectral Freeze
- **Use:** Capture the instantaneous spectrum of a sound and hold it. Used as a pad source from a percussion hit.
- **Engineering:** Most spectral freezes phase-invert randomly between bins; this is the signature "metallic" character. Some allow phase-locked freeze for cleaner pads.
- **Less obvious:** Freeze a hi-hat. Pitch the freeze down two octaves. You now have a pad that nobody can identify the source of.

#### 3.6.2 Granular (Texture, not "Granular Synth")
- **Use:** Source elements (recordings, drum loops, vocal phrases) as raw material for atmospheric beds. Grain size 30–200 ms, density 5–40 grains/sec, scatter and pitch jitter.
- **Engineering:** Granular CPU costs scale with density × polyphony. Freeze return when not editing.
- **Less obvious:** A granular processor with grain pitch tuned to song key + scatter at low values = an in-key wash that follows the source's amplitude envelope. Use this on a vocal sample for "ghost choir."

#### 3.6.3 Phase Vocoder Time-Stretch (as Effect)
- **Use:** 4×–16× stretches of percussion produce evolving textures. The artifacts ARE the sound — embrace them.
- **Less obvious:** Stretch a kick 32× → low rumble bed. Stretch a snare 16× → metallic pad. Both layer beautifully under the original un-stretched element.

---

### 3.7 Stereo / Spatial Imaging

#### 3.7.1 Haas (sub-30ms delay one side)
- **Use:** Mono → stereo width on synths and vocals.
- **Key params:** 8–25 ms one side, level matched.
- **Engineering:** *Always* check mono compatibility. Haas in mono = comb filter cancellation. Use a mono-correlated check or a "sides only" listen to verify.
- **Less obvious:** Haas with the delayed side passed through a *different* filter or saturator (rather than a clean copy) survives mono summing better.

#### 3.6.2 Mid/Side Processing
- **Mid:** Kicks, bass, lead vocal — the spine.
- **Side:** Reverbs, pads, hi-hats — the air.
- **Trick:** Compress the mid only. Saturate the side only. Two different chains on M and S of the same bus.

#### 3.7.3 Auto-Pan (with non-LFO source)
- **Use:** Pan controlled by an envelope follower from a *different* track creates rhythmic stereo movement that isn't a simple sine wave.
- **Less obvious:** Auto-pan a hat with the kick's envelope as the pan source — the hats move *away* from center on each kick hit.

---

## 4. Signature Chains (Drop-In Racks)

Each entry below is a complete preset spec. They reference Section 3 nodes and are written in the schema from Section 8. Treat each as a starting point.

### 4.1 "Dub Chamber Classic" — universal send return

```yaml
name: dub_chamber_classic
intent: [Depth, Dub Space, Drift]
type: send_return
signal_chain:
  - node: hpf
    params: { freq_hz: 220, slope: 12 }
  - node: tape_delay
    params:
      time_ms: 412         # unsynced; or 3/8 dotted
      feedback: 0.62
      wow_hz: 0.07
      wow_depth_pct: 4
      flutter_hz: 6.0
      flutter_depth_pct: 0.3
    feedback_loop:
      - node: hpf
        params: { freq_hz: 240 }
      - node: lpf
        params: { freq_hz: 3200, resonance: 0.35 }
      - node: soft_clip
        params: { ceiling_dbfs: -3 }
  - node: spring_reverb
    params: { decay_s: 1.6, drive: 0.4, mix: 0.35 }
modulation:
  - source: lfo_1
    rate_hz: 0.07
    target: tape_delay.time_ms
    depth: ±2.5%
    shape: triangle
  - source: lfo_2
    rate_hz: 0.05
    target: dub_chamber.lpf.freq_hz
    depth: ±300 hz
safety:
  - { type: brickwall_limiter, position: post_chain, ceiling_dbfs: -1 }
hardware_equivalents:
  h9000: ModEchoVerb + UltraTap with feedback EQ, OR custom FX chain
  serum_fx: Distortion(soft) → Filter(LP, in feedback) → Delay → Reverb(spring)
  ableton: Audio Effect Rack: Utility → EQ8 → Delay (Echo, with mod) → Reverb
  bitwig: FX chain in Pre-FX bus, modulators on time and filter
notes: |
  The single most important send in this aesthetic.
  Build it once, keep it loaded on every project, send everything to it
  at -20 to -30 dB and it'll do 60% of the spatial work.
```

### 4.2 "Self-Ducking Plate" — Levon Vincent–flavor snare/stab

```yaml
name: self_ducking_plate
intent: [Depth, Air, Restraint]
type: send_return
signal_chain:
  - node: plate_reverb
    params: { decay_s: 3.2, predelay_ms: 28, low_cut_hz: 280, high_boost_db: 3, high_boost_freq_hz: 9000 }
  - node: dynamic_eq
    bands:
      - { freq_hz: 400, q: 0.9, mode: dynamic_cut, threshold_dbfs: -22, ratio: 6, attack_ms: 5, release_ms: 180,
          sidechain: self }
  - node: high_shelf_saturation
    params: { freq_hz: 6000, drive: 0.25 }
notes: |
  The plate ducks itself. The wet output triggers a dynamic cut
  in the body (around 400 Hz) on its own input.
  Result: shimmery on tail, never muddy on attack.
```

### 4.3 "Granular Ghost" — pad from any percussion hit

```yaml
name: granular_ghost
intent: [Drift, Air]
type: insert_or_resampler
signal_chain:
  - node: granular
    params:
      grain_size_ms: 120
      density_per_sec: 22
      pitch_jitter_cents: 8
      position_jitter_pct: 6
      grain_pitch_offset_semitones: -12
      mix: 1.0   # wet only, will be paralleled in bus
  - node: hpf
    params: { freq_hz: 180 }
  - node: micro_pitch
    params:
      voices: 2
      detune_cents: [-7, +7]
      pan: [-1, +1]
  - node: convolution_reverb
    params: { ir: dark_hall, decay_s: 8, predelay_ms: 80, mix: 0.5 }
modulation:
  - source: lfo
    rate_hz: 0.04
    target: granular.position_jitter_pct
    depth: ±3
notes: |
  Source: a single closed hi-hat or shaker.
  Output: an evolving pad that sits in the key without being playable.
  Use as a textural bed; automate density up during build sections.
```

### 4.4 "Off-Grid Pulse" — the unsynced delay rhythm

```yaml
name: off_grid_pulse
intent: [Off-Grid Pulse, Drift]
type: insert
signal_chain:
  - node: ducker
    sidechain: kick_bus
    params: { ratio: 4, threshold_dbfs: -30, attack_ms: 1, release_ms: 140 }
  - node: multitap_delay
    params:
      tap_count: 8
      tap_times_ms: [137, 211, 289, 367, 449, 521, 599, 677]   # all prime, no grid relation
      tap_levels_db: [-3, -6, -9, -12, -10, -14, -16, -18]
      tap_pans: [-0.6, +0.4, -0.8, +0.2, +0.7, -0.3, +0.5, -0.1]
  - node: comb_filter
    params: { tuned_freq_hz: 110.0, feedback: 0.4, mix: 0.3 }   # tune to song key (A2 = 110 Hz)
notes: |
  Apply to a single percussion element (clave, rim, glitch).
  The prime-number tap times never align with the grid; the comb tunes them
  to the song key. Result: rhythmic life that sounds like an analog generative system.
key_dependent: true
```

### 4.5 "Frozen Bloom" — capture-and-evolve

```yaml
name: frozen_bloom
intent: [Depth, Drift, Air]
type: insert_with_freeze_control
signal_chain:
  - node: looper_delay
    params: { time_ms: 750, feedback: 0.99, freeze_capable: true }
  - node: freq_shifter
    params: { shift_hz: +0.3 }
  - node: lpf
    params: { freq_hz: 4000, resonance: 0.2 }
  - node: convolution_reverb
    params: { ir: dark_hall, decay_s: 14, mix: 0.6 }
control:
  - { name: freeze_toggle, target: looper_delay.freeze, default: false }
modulation:
  - source: lfo
    rate_hz: 0.03
    target: freq_shifter.shift_hz
    depth: ±0.8 hz
notes: |
  Play a chord. Freeze. Walk away. The shifter creates a barber-pole-like
  evolution; the reverb softens digital edges. Use as a transition pad.
  Hard rule: post-chain limiter at -1 dBFS.
```

### 4.6 "Ghost Kick Pump" — sidechain even when the kick is silent

```yaml
name: ghost_kick_pump
intent: [Off-Grid Pulse]
type: bus_setup
routing:
  ghost_track:
    - kick_sample (muted output, sent to sidechain bus only)
  pumped_bus:
    - all pads, all reverb returns
    - compressor: { ratio: 5, attack_ms: 3, release_ms: 110, threshold: tuned to ~6dB GR }
    - sidechain_input: ghost_track
notes: |
  In breakdowns where the audible kick drops out, the muted ghost kick
  still pumps the pads and reverbs. The breath of the track survives the drop.
  Vincent does this constantly.
```

### 4.7 "Air Layer" — finishing top-end

```yaml
name: air_layer
intent: [Air, Restraint]
type: master_or_pre_master_send
signal_chain:
  - node: ms_split
  - node: side_chain:
      - high_shelf_saturation: { freq_hz: 8000, drive: 0.15, mix: 0.4 }
  - node: mid_chain:
      - transformer_saturation: { drive: 0.1 }
  - node: ms_recombine
notes: |
  Subtle. A/B with this off should sound flatter and smaller.
  Use late in the mix process; do not stack with another wide-band saturator on master.
```

---

## 5. Modulation as an Instrument

Modulation is *how this music stays alive over 12 minutes*. The rules:

1. **Always have at least one modulator running below 0.1 Hz.** Something must move on a 30-second-or-longer cycle. Reverb damping, delay time, filter cutoff, anything.
2. **Use multiple unsynced LFOs** at irrational rate ratios (e.g. 0.07 Hz, 0.13 Hz, 0.31 Hz). Phase relationships never repeat → the track never loops in feel.
3. **Envelope followers > LFOs** when the goal is musicality. Tie a filter cutoff to the kick's envelope rather than to a tempo-synced LFO.
4. **Sample & Hold at 1/8 or 1/16** on a low-Q resonance is the "Villalobos chirp" texture. Subtle, always there, never the focus.
5. **Modulate the modulator.** A slow LFO on the rate of a fast LFO produces non-static, naturally-evolving wobble.

A typical project will have 8–20 active modulators at once, most contributing ±3% changes that nobody can name individually but everybody hears collectively.

---

## 6. Engineering & Safety

### 6.1 Feedback Path Rules

Any chain with feedback ≥ 60% requires:
- **Soft clip or saturator inside the loop** (tames runaway gracefully)
- **LPF inside the loop** (prevents resonance ladder from exploding)
- **HPF inside the loop** (prevents subsonic buildup)
- **Brickwall limiter outside the loop, on the return** (last line of defense, –1 dBFS)
- **Mute / kill switch on the bus** (mapped to a controller key for live use)

### 6.2 Gain Staging

- Sends should leave the source at –6 to –12 dB headroom on the source bus.
- Returns should be metered with peaks below –6 dBFS to allow further mix work.
- Master bus headroom: peaks below –3 dBFS pre-master, with final limiting elsewhere.

### 6.3 Order-of-Operations Defaults

| Goal | Order |
|---|---|
| Glue + space | Sat → Comp → Reverb |
| Aggressive character | Comp → Sat → Delay → Reverb |
| Ambient pad creation | Granular → Reverb → Sat (subtle) → LPF |
| Bus polish | EQ (subtractive) → Comp → EQ (additive) → Sat → Limit |
| Dub vocal | Comp → Delay (dub chamber) → Reverb (plate) → HPF on return |

### 6.4 Mono Compatibility

Anything stereo-widening (Haas, M/S, micro-pitch, ping-pong) MUST be checked in mono:
- A/B with a Utility mono switch on the master.
- If a sound vanishes or thins drastically, decorrelate the two sides further (different filtering, different saturation, different delay times).

### 6.5 CPU and Freezing

Convolution and granular nodes are expensive. Freeze return tracks when not actively editing them. If running on hardware (H9000 etc.), commit chains to clip when finalizing.

---

## 7. Less Obvious Wisdom

Things that don't fit neatly into the taxonomy but matter.

- **Reverb on the trigger, not the source.** Sometimes the move is to put the reverb on the *kick* that sidechains the pad, not on the pad itself. The pad ducks to a wet kick → the pad swells through a "shape" of reverb. It's haunted.
- **Bus tape sat across the entire mix vs. only on returns.** Mix tape on the master compresses the dynamic range. Tape only on FX returns adds character without flattening the dry. You usually want the latter for this scene.
- **Reverbs love EQ in the return, not on the input.** Sculpt the wet, not the dry.
- **A delay's first repeat is the most important parameter.** If the first repeat is too loud, the listener counts it. If it's –6 dB or lower, the repeats become ambience.
- **Hum is not noise; it's life.** A 50 or 60 Hz hum at –65 dB across the master (use a noise generator, not actual hum) glues digital sources together. This is a Villalobos-floor trick.
- **Detune everything by a tiny amount.** Drum samples at –3 cents. Kick fundamental at +1 cent. You won't hear it; the mix will feel less rigid.
- **Reverse reverb on the *exit*, not the *entry* of a sound.** Place the reverse swell *after* a hit fades, leading into the next hit. It implies anticipation rather than echo.
- **Muting is composition.** A track of muted samples that you un-mute for two bars is just as much a compositional act as writing a melody. The dub aesthetic is largely about which mutes you pull when.
- **Test mixes on bone-conduction headphones or a phone speaker.** If the groove survives a phone speaker, it survives a club. Mids are king.
- **Don't use a soft synth's built-in FX for the spatial work.** Use raw oscillators, route to bus FX. The reason: portability of the FX chain across instruments. One dub chamber serves twelve sources.

---

## 8. Preset Schema (Machine-Readable)

The canonical schema for an LLM agent to instantiate a preset on any platform.

```yaml
preset:
  name: string                          # snake_case, unique
  intent: [Pillar]                      # one or more from Section 2
  type: enum[insert, send_return, bus_setup, master_chain]
  bpm_dependent: bool
  key_dependent: bool

  signal_chain: [Node]                  # ordered

  routing:                              # for bus_setup or non-linear chains
    sends: [{ from, to, level_db }]
    returns: [{ id, source }]
    feedback_loops: [{ from_node, to_node, gain }]

  modulation:
    - source: enum[lfo, env_follower, sample_hold, sequencer, audio_rate_mod]
      rate_hz: number | string  # e.g. "1/4 dotted"
      shape: enum[sine, triangle, square, ramp, random]
      target: "node_id.param"
      depth: signed_value_or_percent
      phase_offset_deg: number

  control:                              # macro / user-facing knobs
    - name: string
      target: "node_id.param"
      range: [min, max]
      default: number

  safety:
    - type: enum[brickwall_limiter, soft_clip, dc_filter, kill_switch]
      position: enum[pre_chain, post_chain, in_feedback_loop]
      params: {}

  hardware_equivalents:                 # mapping hints for the agent
    h9000: string                       # algorithm name(s) and chain
    serum_fx: string                    # ordered list using Serum's FX rack
    ableton: string                     # device chain
    bitwig: string
    logic_pro: string
    reaktor: string
    eurorack: string                    # module list

Node:
  node: string                          # canonical type, see §9 mapping
  id: string?                           # optional, for cross-references
  params: { key: value }
  feedback_loop: [Node]?                # nodes inside this node's FB path
  bypass: bool?
```

### 8.1 Canonical Node Types

The agent layer must recognize these as the primitives:

```
hpf, lpf, bpf, notch, parametric_eq, dynamic_eq, shelf_eq,
comp, multiband_comp, ducker, limiter, soft_clip, hard_clip,
gate, transient_designer,
tape_delay, digital_delay, multitap_delay, looper_delay, comb_filter,
spring_reverb, plate_reverb, hall_reverb, room_reverb, convolution_reverb,
chorus, flanger, phaser, micro_pitch, freq_shifter, ring_mod, vocoder,
granular, spectral_freeze, phase_vocoder_stretch,
tape_sat, tube_sat, transformer_sat, bitcrush, high_shelf_saturation,
ms_split, ms_recombine, mid_chain, side_chain, utility_gain, pan,
auto_pan, haas
```

Each platform mapping (Section 9) translates these to native devices.

---

## 9. Hardware / Software Mapping Tables

### 9.1 Eventide H9000

| Canonical | H9000 Algorithm |
|---|---|
| dub_chamber_classic | ModEchoVerb + UltraTap, with FX-in-FX feedback EQ |
| multitap_delay | UltraTap |
| convolution_reverb | (Not native; use ModEchoVerb dark hall as substitute) |
| micro_pitch | MicroPitch (H3000 algorithm) |
| freq_shifter | Instant Phaser / Crystals (use Crystals for harmonic shift, native freq shifter via custom algo) |
| spring_reverb | Use SP2016 / custom Tverb |
| plate_reverb | SP2016 Plate, Blackhole (dark variant) |
| spectral_freeze | Resonator / Crystals reverse |
| granular | (Not native; use multi-tap with extreme density as approximation) |
| tape_sat | Tape modeling via send to outboard recommended |

### 9.2 Serum FX Rack (within Serum 2 / Pro version)

| Canonical | Serum FX Slot |
|---|---|
| hpf, lpf | Filter |
| comp | Comp |
| tape_sat | Distortion (Tube/Tape mode) |
| chorus, flanger, phaser | Chorus / Flanger / Phaser |
| delay | Delay |
| reverb | Reverb (Hall/Plate switchable) |
| micro_pitch | Use Chorus with very low rate, or external |

For anything outside the rack (granular, freq shift, convolution): pre-route audio out of Serum into a host insert chain.

### 9.3 Ableton Live

Build everything as Audio Effect Racks. Macro-mapped to the user-facing controls in Section 8 `control:`.

| Canonical | Ableton Device |
|---|---|
| dub_chamber_classic | Rack: EQ Eight → Echo (with mod) → Reverb |
| convolution_reverb | Convolution Reverb Pro (Max for Live) |
| granular | Granulator III (M4L) |
| micro_pitch | Frequency Shifter (in shift mode w/ low value) or third-party (Soundtoys MicroShift) |
| spectral_freeze | Spectral Resonator / Spectral Time |
| dynamic_eq | EQ Eight in dynamic mode (Live 12+) |
| ms_split | Utility (Width 0 / 200) + Multiband or M4L M/S devices |

### 9.4 Bitwig Studio

Bitwig's Grid + nested FX chains map this dossier almost 1:1.
- Pre-FX / Post-FX chains for parallel routing
- Modulators panel for the LFO/env-follower architecture
- The Grid for custom feedback loops with safety nodes inline

### 9.5 Eurorack / Hardware Modular

| Canonical | Module Class |
|---|---|
| dub_chamber_classic | Tape echo (e.g. Strymon Volante, OTO BIM/BAM, Mood) → Spring (Erica Pico DSP) |
| freq_shifter | Doepfer A-126, Make Noise Echophon (shift mode) |
| ring_mod | Doepfer A-114 |
| spectral_freeze | Mutable Clouds / Beads (freeze mode) |
| granular | Mutable Beads, Make Noise Morphagene |
| filter (in feedback) | Any high-quality state-variable filter |

---

## 10. LLM Agent Notes (Closing)

When passing this dossier to an LLM agent for preset generation:

1. **Treat each preset block in Section 4 as a complete spec.** The agent should be able to take one and produce native-platform equivalents using the mappings in Section 9.
2. **For platforms missing a primitive** (e.g. no granular in Serum FX), the agent should substitute with the closest available primitive *and flag the substitution in a comment*. Do not silently degrade.
3. **Always include safety nodes from Section 6.1** in feedback chains. This is non-negotiable for production use.
4. **Modulation depth defaults to subtle.** When in doubt, the agent should choose smaller depth values. Over-modulation is the obvious "AI preset" tell.
5. **bpm_dependent and key_dependent flags** should be honored by the agent: pull tempo from host clock, pull key from a user-supplied parameter or scene metadata.
6. **The `control:` macro section is what the user sees.** Keep these to 4–8 macros per preset. More macros = harder to play live.
7. **Naming convention:** `<aesthetic>_<role>_<variant>` — e.g. `villalobos_dub_send_v2`, `levon_plate_dry_kick`, `moonear_spring_perc`.

---

*End of dossier. Extensions (new chains, new primitives, new platform mappings) should append to Sections 4, 8.1, and 9 respectively, preserving schema field names.*
