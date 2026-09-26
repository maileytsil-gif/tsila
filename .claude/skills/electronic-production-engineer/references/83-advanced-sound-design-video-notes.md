# Advanced sound-design video/document study notes

Use these as technique anchors, not recipes to clone. URLs are in `../SOURCES.md`. Only the manuals below exist as full text in the local corpus; the courses, tutorials and interviews do not, so any number taken from them stays an example to verify by ear or measurement `[TEST]`. Evidence tags as defined in `32-sound-design-engine.md`.

## Serum / bass
- Xfer Serum 2 manual: Sample, Multisample, Granular and Spectral engines extend Serum beyond classic wavetable synthesis `[DOC]`. Local text: `../../../../corpus/constructeur/xferrecords-com-manual-serum-2-docs-06-using-sample-instruments.md` to `-08-using-spectral-synthesis.md`, audio import in `-21-importing-audio-as-wavetables.md`, Resample to / Render OSC Warp in `-24-appendix-a-using-the-main-menu.md`; checked map: `../../sound-designer-serum/references/serum2-cartographie.md`.
- Au5 HyperGrowl tutorials: important lesson is resampling a simple source into a custom wavetable and using formant/filter motion to create expressive growls. Serum 2 tools for it: main menu › Rendering › Resample to, Render OSC Warp, audio import with "Constant framesize (PITCH AVERAGE)" first, Formant-I/II/III filters `[DOC p. 138, 294, 324]`. Repo patterns: two or three resample passes, UNISON 1 while designing, LFO in RETRIG `[DOC-2]`.
- ADSR/Rocket Powered tutorials: useful demonstrations of FM, band-pass/formant-style movement, multiband/distortion and modulation for talking bass; treat exact values as examples only. The repo's written, sourced equivalents: `../../house-future-rave-bass-house-production/recipes/talking-bass-formants.md` (vowel formant table) and `basse-fm-metallique-bass-house.md` (FM ratios) in the same folder.
- Online growl recipes are usually built at 140–150 BPM: convert tempo-synced LFO divisions and millisecond values before reusing them (ms = 60000 / BPM × beats) `[DOC-2]` `[CALC]`; see `../../sound-designer-serum/references/fiches-pratiques.md`, sheet 04.

## Waves electronic vocals
- OVox official tutorials: vocal as modulator, synth/instrument as carrier, MIDI control, vocal-to-synth and sidechain vocoding.
- Vocal Bender: pitch + formant, modulation and Flatten for deliberately robotic voice character.
- Waves Tune Real-Time: transparent-to-hard pitch quantization and low-latency creative tuning.
- None of these manuals is in the local corpus. The documented native fallback is Live's Vocoder (Carrier External, Post FX synth, saw carriers for intelligibility, Unvoiced, Enhance): `../../../../corpus/constructeur/live12-manuel-28-live-audio-effect-reference.md` § 28.42 `[DOC]`. Talk box vs vocoder vs harmoniser history: `../../../../corpus/funk-claviers/bjango-com-articles-daftpunkvocaleffects.md`.

## DnB production
- Producertech / Icicle: spectrum analysis, kick synthesis in Operator, FM snare design, resampled bass and FX risers, then mix/arrangement.
- Producertech / Fracture: Drum Racks, Sampler/Analog, sliced/resequenced breaks, bass construction, arrangement and final mix in Ableton; Maschine course emphasizes tactile sequencing, sliced loops and layered bass groups.
- Producertech / Creatures Liquid D&B: musicality/theory, sampling/sound design, track development and arrangement; samples are integrated with chorus, delay, reverb and pitch processing.
- Producertech / colo[r]: synthetic + acoustic drum layering, sub design, bass automation/resampling, slip editing and vocal-vocoder FX.
- Documented anchors for these techniques: kick/snare circuits, layering and crest factor in `../../sound-designer-serum/references/percussions.md`; Simpler slicing (Transient, Beat, Region, Manual) in `../../../../corpus/constructeur/live12-manuel-30-live-instrument-reference.md` § 30.11; Maschine Slicer (Detect, Split, Grid, Manual) in `../../../../corpus/constructeur/native-instruments-com-fileadmin-ni-media-downloads-manuals-maschine-maschine-3-software-m-17-15-sampling-and-sample-mapping.md` `[DOC]`.

## Scene/artist interviews as decision evidence
- UKF interviews with Alix Perez/Skeptical/DLR emphasize simplicity, drums/bass focus, groove, rim/snare identity, mix refinement and avoiding loudness at the expense of vibe.
- Calibre-related UKF material emphasizes natural flow, soul and the power of simple musical elements.
- US/North-American interviews with Justin Hawkes, Kumarion and REAPER show a broader willingness to hybridize DnB with songwriting, dubstep and bass-music sound design; use this as an optional regional/crossover profile, not a universal rule.
- Interviews are decision evidence about taste and priorities, not parameter sources (source hierarchy: `80-evidence-policy.md`).
