# Robotic bass, vocoder and electronic vocal engine

Evidence tags as defined in `32-sound-design-engine.md`.

## Goal
Design intelligible robotic, talking and synthetic timbres without sacrificing low-end stability or vocal articulation.

## Robotic bass architecture
Separate the function of the layers:
- **Sub**: clean, mono-compatible fundamental; minimal modulation.
- **Body**: carries note identity and weight.
- **Articulation/formant layer**: creates talking/robotic motion.
- **Noise/transient layer**: optional edge, click or mechanical attack.

Do not force one patch to do all four jobs when separate layers give cleaner control. Starting split: sub low-passed near 90–100 Hz and routed Direct in Serum; formant/growl layers high-passed near 100 Hz; everything mono below 100–150 Hz `[DOC-2]`.

## Serum 2 design routes
Exact labels: `../../sound-designer-serum/references/serum2-cartographie.md` § 4 and § 6.

### FM / phase distortion route
Use stable carrier pitch plus a modulator at a musically useful ratio: OSC A sine carrier, WARP 1 = `FM (B)`, OSC B sine in **Ratio** tuning mode (its level may be 0) `[DOC p. 30, 54–56]`. 2:1 gives the hollow garage/future-house tone; detuning the modulator by about 30 cents (the "−12.30" variant) makes it metallic while the ratio stays integer; two octaves plus a fifth is 6:1 `[DOC-2]` `[CALC]`. FM depth is **MUET**: start near 45 % with ENV 2 → WARP 1 amount, DEC 150–300 ms, SUS 0 `[HEUR]`; a "thwack" is ENV 3 → CRS +12 st falling to 0 in 50 ms `[DOC-2]`. `PD (Self)` under an envelope brightens like an opening filter without resonance `[HEUR]`. Modulate FM amount rather than only oscillator level, lock QUALITY (FM/PD warps changed with it before 2.0.21 `[DOC changelog]`), then follow with band-pass/notch/formant filtering.

### Wavetable/formant route
Use a harmonic or resampled wavetable, then move WT POS and filter/formant position from the same macro with different matrix curves (CRV). A second source can alter rate or depth for phrase variation.
- FILTER 1 **Formant-I/II/III**: CUTOFF morphs between vowels, VAR = FORMNT `[DOC p. 138]`; RES 20–40 keeps vowels defined `[DOC-2]`; FILTER 2 MG Low 24 at 3–5 kHz in series removes fizz `[HEUR]`. Alternative: two Band 12 filters on F1 and F2.
- Vowel formants F1/F2 in Hz `[DOC-2]`: ah 730/1090 · oh 570/840 · ee 270/2290 · eh 530/1840 · oo 300/870; F3 fixed near 2500–3000.
- Oh → ah is a small knob move: find two positions and modulate slowly between them (LFO over 2–4 bars or a macro), plus a small LFO in RETRIG at 1/8 for the "talk"; sweeping the whole range sounds like a filter demo `[DOC-2]`. Factory start: Vox › VOX - I Talk `[DOC-2]`.

### Resampled robotic route
Create a simple tone → automate/filter/distort → render → re-import (main menu › Rendering › **Resample to**, or drag the audio onto the wave display) → scan/resample again `[DOC p. 292–294, 324]`. This often produces more distinctive robotic speech than adding more modulators to the original patch.

### Granular/spectral route
Import a vocal, metallic hit or synthetic phrase. Use granular scan (SCAN 0 = frozen) or spectral resynthesis (Phase Lock for tonal material, Transients for percussive material) for frozen consonant-like textures, machine chatter, metallic vowels and evolving drones `[DOC p. 99, 117]`. The Spectral engine also carries vocode/mask warps (preset internals `kVocode_*`, `kMask_*`) whose on-screen labels are **MUET** in the manual `[TEST]`.

## Waves vocal tools
Not documented in the local corpus (sources in `../SOURCES.md`): treat the notes below as qualitative until checked in the plug-in `[TEST]`.

### OVox
Use when the voice should become a synth/vocoder or control a carrier.
- Vocal = modulator; synth/instrument = carrier when sidechain carrier mode is used.
- MIDI note control can impose harmony or robotic pitch behavior.
- Add carrier harmonics/drive when intelligibility is weak.
- Resample the result for further chopping or Serum import.

### Vocal Bender
Use for real-time pitch and formant design. The Flatten function is especially useful for intentionally robotic monotone effects. Modulators can create sequenced pitch/formant movement.

### Waves Tune Real-Time
Use for controlled pitch quantization before or after creative processing.
- Slower/more tolerant settings preserve natural singing.
- Fast correction creates deliberate hard-tuned EDM/robotic articulation.
- Use the correct scale/key unless chromatic behavior is intentional.
- Formant correction preserves character when desired; disable/alter character elsewhere if an artificial result is the goal.

### Waves Harmony / OVox layering
Use harmonized voices as carriers, doubles or spectral layers rather than leaving every generated voice full-range.

## Ableton alternatives/complements
- **Vocoder** `[DOC Live 12 manual 28.42]`: insert on the modulator (voice) track. Carrier **Noise**, **External**, **Modulator** or **Pitch Tracking**; for a robot voice use External with Audio From = the synth track, Post FX. Saw-based carriers improve intelligibility; **Enhance** restores brightness; **Unvoiced** (with Sens.) resynthesizes "s"/"f"; more **Bands** = more accurate, more CPU; **BW** 100 % is the most accurate; **Depth** 100 % = classic vocoding; **Formant** shifts the carrier filterbank; Precise or Retro filter behaviour. Carrier = Modulator + Depth 100 % + Enhance turns it into a formant shifter.
- Talkbox emulation: Unvoiced low, then low-pass around 5–6 kHz `[HEUR]`; noise carrier with a drum-loop modulator gives "talking" hats that follow the groove `[HEUR]`.
- **Roar**: seven routing modes (Single, Serial, Parallel, Multi Band, Mid Side, Feedback, Delay); Feedback Mode **Note** tunes the ringing to a pitch `[DOC 28.33]`.
- Grain Delay/Beat Repeat/Erosion: glitch and mechanical edge.
- **Hybrid Reverb** Freeze (infinite tail) and Freeze In (keeps adding input) turn a vocal or bass fragment into an atmosphere or transition bed `[DOC 28.23]`.

## Practical chains
### Clean robotic vocal
Tune Real-Time → corrective EQ → OVox/Vocoder → de-ess/soothe if needed → compression → delay/reverb sends.

### Aggressive robot chop
Vocal Bender/Flatten → OVox → Roar/distortion → Beat Repeat/stutter → resample → Serum Granular/Spectral.

### Talking bass
Serum body/formant layer + separate clean sub (Direct) → Splitter L/M/H: below 120 Hz clean, 120 Hz–2 kHz waveshaping (Tube then Hard Clip), above 2 kHz light Tube `[DOC-2]` → dynamic EQ/sidechain → peak shaping → resample selected phrases.

## Label-ready checks
- Speech/formant layer must remain understandable at low playback level: two vowels identifiable on the drop loop, checked at 0, 50 and 100 % of the vowel macro `[DOC-2]`.
- Sub should not inherit wide stereo, granular randomness or strong formant modulation.
- Match phrase levels before judging tone; do not claim intelligibility without listening or a measurement.
- Check mono after vocoder, chorus, unison and spectral widening.
- Remove harsh resonances after distortion only where they occur; do not blanket-dull the sound.

## Repo resources
- `../../house-future-rave-bass-house-production/recipes/talking-bass-formants.md`, `basse-fm-metallique-bass-house.md` (same folder).
- Talkbox/vocoder: `../../studio-grade-funk-keys-synth-sound-design/recipes/talkbox-zapp-modern.md`; formants and vocoder background: `../../sound-designer-serum/references/modulation-effets.md` § B2.
- Local manual: `../../../../corpus/constructeur/live12-manuel-28-live-audio-effect-reference.md`; vocoder vs talk box history: `../../../../corpus/funk-claviers/bjango-com-articles-daftpunkvocaleffects.md`.
