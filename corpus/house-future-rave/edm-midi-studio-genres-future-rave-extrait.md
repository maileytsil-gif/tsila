---
titre: "KinhkhaTran/edm-midi-studio — README et lib/generators.js (extrait) : définition chiffrée « Future Rave » (126 BPM, mineur, swing 0, accords de quinte/add9/sus4, basse offbeat 8es, arpège 16es, lead « festival ») et voisins house/tech house"
source: https://raw.githubusercontent.com/KinhkhaTran/edm-midi-studio/main/lib/generators.js
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: genres et éléments constitutifs (house, bass house, future rave)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR-lu] (notes non sourcées, dépôt GitHub) : chiffres à recouper avant usage.

# Extrait 1 : README.md du dépôt (moteur de composition « genre-aware », liste des genres dont future rave)

# Loopsmith — EDM MIDI Studio

A local web studio for sketching EDM loops: genre-aware MIDI generation, instant audio
preview in the browser, an AI producer chat that edits your patterns directly, and
`.mid` export that drags straight into Ableton Live.

## Quick start

```sh
npm install
export ANTHROPIC_API_KEY=sk-ant-...   # optional — enables the AI chat panel
npm start
# open http://localhost:3123
```

Without `ANTHROPIC_API_KEY` everything works except the chat panel.

## What it does

- **Composition engine** — house, deep house, techno, trance, progressive, melodic house,
  future rave, tech house, afro/organic house, dubstep, drum & bass, future bass, trap.
  Motif-based melodies (A A' B A'' phrase structure, chord-tone
  targeting, climax placement, resolution), counter-melodies that answer in the lead's gaps,
  extended harmony (7ths/9ths/sus/add9/shell voicings) with real voice leading, bass
  archetypes with chromatic approach notes, swing/groove velocity maps. Seeded RNG: the same
  seed always reproduces the same track.
- **Modern hook generator** — newer style presets write the chords first, use visible chord
  tones as rails for the melody, repeat a two-bar hook, ornament connectors, place the climax
  late, then resolve. Every modern preset also exports a **Piano Hook Guide** stem so you can
  drag a simple piano melody into Ableton even before synth/sound design is finished.
- **Full song arrangement** — intro → build → drop → break → build → drop → outro (72 bars)
  with per-section energy masks, accelerating snare rolls, risers, impacts, downlifters, and
  a counter-melody that only enters on the second drop. Or generate a plain loop.
- **12 stems** — kick, snare/clap, hats, percussion, sub bass, bass, chords, pads, arp, lead,
  counter, FX. Each exports as its own MIDI track.
- **Audio preview with a real mix** — layered synthesis (supersaw stacks, FM plucks, 808 with
  drive, wobble bass with synced filter LFO, sine sub), sidechain pump under every kick,
  reverb/delay sends, and a mastering chain (HP → EQ → glue compressor → saturation →
  limiter). Space bar toggles play; click a section in the timeline to jump there.
- **AI chat** — Claude (Opus 4.8) with tool use. It can change tempo/key/genre, regenerate
  tracks through the engine, read your patterns, and write custom notes directly
  (melodies, chord voicings, fills). Every change lands in the UI immediately.
- **MIDI I/O** — export the whole loop as a multitrack `.mid` or any single track; import
  existing `.mid` files to preview and rework them.

## Neural audio renders (Stable Audio 2.5)

The **✦ Render** button (or asking the AI to "render a produced version") sends your
project's style — genre, BPM, key, arrangement arc, plus any style prompt — to
Stability's official **Stable Audio 2.5** model on Replicate and returns studio-quality
audio (~$0.20 and ~1–2 min per render, up to 190 s).

```sh
export REPLICATE_API_TOKEN=r8_...   # replicate.com/account/api-tokens
```

The render is a produced *interpretation* of your track's style — it won't note-for-note
match the MIDI. The stems remain the editable source of truth for Ableton; the render is
the "how it could sound fully produced" reference.

## Ableton workflow

1. Generate / chat until the loop sounds right.
2. **Export .mid** (whole project) or `⤓ mid` on a single lane.
3. Drag the file into Ableton — each track arrives as its own MIDI clip. Drums use GM
   pitches, so they map cleanly onto a Drum Rack.
4. Start with **Piano Hook Guide** if you only need inspiration: put Ableton Piano/Keys on it,
   then layer the Lead MIDI into Serum/Vital/stock Wavetable once the melody feels right.
5. Swap the sketch synths for your own instruments and arrange.

## Research notes baked into the generator

This pass used current EDM production sources and YouTube transcripts as design constraints:

- **EDM lead writing**: start by laying down the chord progression, then use the chord notes as
  ghost notes/rails for the lead so the melody stays in key while still allowing flashy passing
  notes and connectors. The hook should feel catchy through rhythm + repetition first, not just
  random scale motion.
- **Melodic house**: reference-track structure, 8-bar sections, four-on-the-floor kick, simple
  long-note bass movement, nostalgic extended chords, arps, organic leads, delay/reverb space,
  and percussion that grows after the core idea is established.
- **Progressive/festival EDM**: detuned saw/add9/sus harmony, late-phrase climax notes, call and
  response, and a clear resolution so the exported MIDI points you toward a usable drop lead.

Useful commands:

```sh
npm test       # syntax checks + writes sample Ableton-ready MIDI files to exports/
npm run samples
```

## Architecture

```
server.js          Express: engine endpoints + Claude chat (tool-use loop)
lib/theory.js      scales, chords, voice-leading, seeded RNG
lib/generators.js  genre definitions + drum/bass/chord/arp/lead builders
lib/midi.js        pattern state <-> Standard MIDI File (@tonejs/midi)
public/            UI: canvas piano rolls, Tone.js playback, chat panel
```

Pattern state is plain JSON — notes are `{ pitch, start, dur, vel }` with times in beats —
so it's easy to extend (new genres, new tools for the AI, new export targets).

## Roadmap: driving Ableton directly (MCP)

The natural next step is wiring this to [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp),
an existing MCP server + Ableton Remote Script that exposes Live over a local socket
(create tracks, write clips, load instruments, set tempo). Two integration paths:

1. **Loopsmith as an MCP client** — add a "Send to Ableton" button that pushes the current
   pattern state into Live as clips via the ableton-mcp socket protocol, skipping the
   file drag entirely.
2. **Loopsmith as an MCP server** — expose the genre engine itself as MCP tools
   (`generate_pattern`, `export_midi`) so Claude Desktop / Claude Code can use it alongside
   ableton-mcp in one session: generate here, place into Live there.

Both reuse `lib/generators.js` and `lib/midi.js` unchanged.


---

# Extrait 2 : lib/generators.js — définitions de genres (house, deep house, progressive, melodic house, future_rave, tech_house, afro_house…) : BPM, gamme, swing, progressions, grilles de batterie 16 pas, type de basse, stabs, arpège, lead

```js
// Genre-aware EDM composition engine.
//
// Times are in beats (quarter notes). One bar = 4 beats, one 16th step = 0.25.
// Note shape: { pitch: <midi 0-127>, start: <beats>, dur: <beats>, vel: <1-127> }
//
// How a song is built:
//   1. Generate 8 bars of core *materials* (progression, drum grids, motif-based
//      melody, counter-melody, bass, chords, pads, arp) — this is the hook.
//   2. structure "loop"  -> render just the core materials.
//      structure "song"  -> tile the materials across an arranged energy curve
//      (intro → build → drop → break → build → drop → outro) with per-section
//      stem masks, velocity scaling, snare rolls, risers, impacts and crashes.

import {
  noteToMidi, scalePitch, chordPitches, voiceLead, snapToScale,
  mulberry32, rngHelpers, swing16, grooveVel,
} from './theory.js';

export const DRUMS = {
  kick: 36, rim: 37, snare: 38, clap: 39, chh: 42, tomL: 45, ohh: 46, tomH: 47,
  crash: 49, ride: 51, tamb: 54, congaH: 63, congaL: 64, shaker: 70, clave: 75,
};

export const STEMS = ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'arp', 'lead', 'guide', 'counter', 'fx'];
export const DRUM_STEMS = new Set(['kick', 'snare', 'hats', 'perc', 'drums']);
export const TRACK_TYPES = STEMS;

const CORE_BARS = 8;

// ---------------------------------------------------------------------------
// Genre definitions
// ---------------------------------------------------------------------------
// progression: 8 chord specs {d: degree, q: quality} — one per bar of the core.
// drums: per-stem 16-step strings ('X' accent, 'x' hit, 'o' ghost, '.' rest).
// comp: chord-stab rhythm [start, dur, velScale][]; pads: sustained layer flag.
// lead: rhythm-cell weights + register. swing: 0 = straight, ~0.56 = MPC feel.

export const GENRES = {
  house: {
    label: 'House', bpm: 124, scale: 'minor', bassOct: 2, swing: 0.54,
    progressions: [
      [{ d: 0, q: '7' }, { d: 5, q: '7' }, { d: 3, q: '9' }, { d: 4, q: '7' }, { d: 0, q: '7' }, { d: 5, q: '9' }, { d: 3, q: '7' }, { d: 4, q: 'sus4' }],
      [{ d: 0, q: '9' }, { d: 3, q: '7' }, { d: 5, q: '7' }, { d: 4, q: '7' }, { d: 0, q: '9' }, { d: 3, q: '7' }, { d: 5, q: '9' }, { d: 6, q: '7' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: 'xoxoXoxoxoxoXoxo', ohh: '..x...x...x...x.' },
      perc:  { shaker: 'oxooxooxooxooxoo', congaH: '.......x......x.', rim: '..........x.....' },
    },
    bass: 'offbeat8',
    comp: [[1.5, 0.3, 1.0], [3.5, 0.3, 0.9]],
    pads: true,
    lead: { cells: { two8: 3, dot: 2, offbeat: 2, sustain: 2, rest: 1.5 }, octave: 5, range: 7 },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'lead', 'counter', 'fx'],
  },
  deep_house: {
    label: 'Deep House', bpm: 120, scale: 'dorian', bassOct: 2, swing: 0.57,
    progressions: [
      [{ d: 0, q: '9' }, { d: 3, q: '9' }, { d: 4, q: 'shell' }, { d: 3, q: '9' }, { d: 0, q: '9' }, { d: 6, q: 'shell' }, { d: 3, q: '9' }, { d: 4, q: '7' }],
      [{ d: 1, q: 'shell' }, { d: 4, q: '9' }, { d: 0, q: '9' }, { d: 3, q: '7' }, { d: 1, q: '9' }, { d: 4, q: '9' }, { d: 0, q: '9' }, { d: 4, q: 'sus4' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x..o', snare: '..............o.' },
      hats:  { chh: 'o.oox.ooo.oox.oo', ohh: '..x...x...x...x.' },
      perc:  { shaker: 'xoooxoooxoooxooo', rim: '.......x......x.', congaL: '..o.......o...o.' },
    },
    bass: 'rolling',
    comp: [[0.5, 0.35, 0.85], [2.5, 0.6, 0.95]],
    pads: true,
    lead: { cells: { sustain: 3, dot: 2, two8: 1.5, rest: 2.5 }, octave: 5, range: 6 },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'lead', 'counter', 'fx'],
  },
  techno: {
    label: 'Techno', bpm: 132, scale: 'phrygian', bassOct: 1, swing: 0,
    progressions: [
      [{ d: 0, q: '5' }, { d: 0, q: '5' }, { d: 0, q: '5' }, { d: 1, q: '5' }, { d: 0, q: '5' }, { d: 0, q: '5' }, { d: 5, q: '5' }, { d: 0, q: '5' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: '..x...x...x...x.', ride: 'x.x.x.x.x.x.x.x.' },
      perc:  { tomL: '.......o..o.....', rim: '..o...........o.', clave: '......x.........' },
    },
    bass: 'rumble16',
    comp: [[3.5, 0.25, 0.85]],
    pads: false,
    lead: { cells: { six: 3, two8: 2, offbeat: 1.5, rest: 1 }, octave: 4, range: 5, acid: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'arp', 'lead', 'fx'],
  },
  trance: {
    label: 'Trance', bpm: 138, scale: 'minor', bassOct: 2, swing: 0,
    progressions: [
      [{ d: 0, q: 'triad' }, { d: 5, q: 'add9' }, { d: 2, q: 'triad' }, { d: 6, q: 'triad' }, { d: 0, q: 'triad' }, { d: 5, q: 'add9' }, { d: 3, q: 'add9' }, { d: 4, q: 'sus4' }],
      [{ d: 0, q: 'add9' }, { d: 4, q: 'triad' }, { d: 5, q: 'add9' }, { d: 3, q: 'triad' }, { d: 0, q: 'add9' }, { d: 4, q: 'triad' }, { d: 5, q: 'add9' }, { d: 6, q: 'triad' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: 'xoxoxoxoxoxoxoxo', ohh: '..x...x...x...x.' },
      perc:  { ride: '..x...x...x...x.', tamb: 'x.x.x.x.x.x.x.x.' },
    },
    bass: 'offbeat8',
    comp: [[0, 3.8, 0.8]],
    pads: true,
    arp: { pattern: 'up', rate: 0.25, octave: 4, span: 2 },
    lead: { cells: { sustain: 3, dot: 2.5, two8: 2, rest: 1 }, octave: 5, range: 8, soaring: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'arp', 'lead', 'counter', 'fx'],
  },
  progressive: {
    label: 'Progressive House', bpm: 126, scale: 'minor', bassOct: 2, swing: 0,
    progressions: [
      [{ d: 0, q: 'add9' }, { d: 3, q: '7' }, { d: 5, q: 'add9' }, { d: 4, q: 'sus4' }, { d: 0, q: 'add9' }, { d: 3, q: '7' }, { d: 5, q: 'add9' }, { d: 6, q: '7' }],
      [{ d: 3, q: 'add9' }, { d: 0, q: 'triad' }, { d: 5, q: '9' }, { d: 4, q: 'triad' }, { d: 3, q: 'add9' }, { d: 0, q: 'triad' }, { d: 5, q: '9' }, { d: 4, q: 'sus4' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: 'x.xox.xox.xox.xo', ohh: '..x...x...x...x.' },
      perc:  { shaker: 'oxooxooxooxooxoo', rim: '......x.......x.' },
    },
    bass: 'rolling8',
    comp: [[0.5, 0.25, 0.8], [1.5, 0.25, 0.9], [2.5, 0.25, 0.8], [3.5, 0.25, 0.95]],
    pads: true,
    arp: { pattern: 'updown', rate: 0.25, octave: 4, span: 2 },
    lead: { cells: { dot: 3, sustain: 2, two8: 2, rest: 1.5 }, octave: 5, range: 7 },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'arp', 'lead', 'counter', 'fx'],
  },
  melodic_house: {
    label: 'Melodic House', bpm: 124, scale: 'minor', bassOct: 2, swing: 0.52,
    progressions: [
      [{ d: 0, q: '9' }, { d: 5, q: 'add9' }, { d: 3, q: '9' }, { d: 4, q: 'sus4' }, { d: 0, q: '9' }, { d: 5, q: 'add9' }, { d: 3, q: '7' }, { d: 4, q: 'add9' }],
      [{ d: 0, q: 'add9' }, { d: 3, q: '9' }, { d: 6, q: '7' }, { d: 5, q: 'add9' }, { d: 0, q: 'add9' }, { d: 3, q: '9' }, { d: 4, q: 'sus4' }, { d: 5, q: '7' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: '..x...x...x...x.', ohh: '..x...x...x...x.' },
      perc:  { shaker: 'oxooxooxooxooxoo', tamb: '........x.......', rim: '......x.......x.' },
    },
    bass: 'rolling8',
    comp: [[0, 1.5, 0.62], [2.5, 0.75, 0.82], [3.5, 0.35, 0.72]],
    pads: true,
    arp: { pattern: 'updown', rate: 0.25, octave: 4, span: 2 },
    lead: { hook: 'melodic', cells: { sustain: 3, dot: 2, two8: 1.5, rest: 1.5 }, octave: 5, range: 8, emotional: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'arp', 'lead', 'guide', 'counter', 'fx'],
  },
  future_rave: {
    label: 'Future Rave', bpm: 126, scale: 'minor', bassOct: 2, swing: 0,
    progressions: [
      [{ d: 0, q: '5' }, { d: 3, q: 'add9' }, { d: 5, q: 'sus4' }, { d: 4, q: '5' }, { d: 0, q: '5' }, { d: 3, q: 'add9' }, { d: 5, q: 'sus4' }, { d: 6, q: '5' }],
      [{ d: 0, q: 'add9' }, { d: 4, q: 'sus4' }, { d: 5, q: 'add9' }, { d: 3, q: 'triad' }, { d: 0, q: 'add9' }, { d: 4, q: 'sus4' }, { d: 5, q: '7' }, { d: 6, q: '5' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: 'x.x.x.x.x.x.x.x.', ohh: '..x...x...x...x.' },
      perc:  { shaker: '..x...x...x...x.', tomL: '...........o....', rim: '......x.......x.' },
    },
    bass: 'offbeat8',
    comp: [[0, 0.45, 1.0], [1.5, 0.35, 0.88], [2, 0.45, 0.95], [3.5, 0.35, 0.9]],
    pads: true,
    arp: { pattern: 'up', rate: 0.25, octave: 4, span: 2 },
    lead: { hook: 'festival', cells: { dot: 3, sustain: 2, two8: 2, rest: 1 }, octave: 5, range: 9, soaring: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'arp', 'lead', 'guide', 'counter', 'fx'],
  },
  tech_house: {
    label: 'Tech House', bpm: 126, scale: 'minor', bassOct: 2, swing: 0.55,
    progressions: [
      [{ d: 0, q: '7' }, { d: 0, q: '7' }, { d: 3, q: '7' }, { d: 4, q: '7' }, { d: 0, q: '7' }, { d: 0, q: '7' }, { d: 5, q: '7' }, { d: 4, q: '7' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: 'xoxoxoxoxoxoxoxo', ohh: '..x...x...x...x.' },
      perc:  { shaker: 'oxooxooxooxooxoo', congaH: '...x....x...x...', rim: '..x.......x.....' },
    },
    bass: 'rolling',
    comp: [[1.5, 0.18, 0.7], [3.5, 0.18, 0.8]],
    pads: false,
    lead: { hook: 'tech', cells: { offbeat: 3, six: 2, two8: 2, rest: 1 }, octave: 5, range: 5, acid: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'lead', 'guide', 'fx'],
  },
  afro_house: {
    label: 'Afro / Organic House', bpm: 122, scale: 'dorian', bassOct: 2, swing: 0.58,
    progressions: [
      [{ d: 0, q: '9' }, { d: 6, q: '7' }, { d: 3, q: '9' }, { d: 4, q: 'sus4' }, { d: 0, q: '9' }, { d: 6, q: '7' }, { d: 3, q: '9' }, { d: 4, q: '7' }],
    ],
    drums: {
      kick:  { kick: 'x...x...x...x...' },
      snare: { clap: '....x.......x...' },
      hats:  { chh: 'x.oxx.oxx.oxx.ox', ohh: '..x...x...x...x.' },
      perc:  { shaker: 'xoooxoooxoooxooo', congaH: '..x..o...x..o...', congaL: '....o......o....', tamb: '...x...x...x...x' },
    },
    bass: 'rolling',
    comp: [[0.5, 0.3, 0.72], [1.75, 0.3, 0.86], [2.5, 0.4, 0.78], [3.5, 0.25, 0.7]],
    pads: true,
    arp: { pattern: 'updown', rate: 0.5, octave: 4, span: 1 },
    lead: { hook: 'organic', cells: { dot: 2, sustain: 2, offbeat: 2, rest: 1.5 }, octave: 5, range: 7 },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'arp', 'lead', 'guide', 'counter', 'fx'],
  },
  dubstep: {
    label: 'Dubstep', bpm: 140, scale: 'harmonicMinor', bassOct: 1, swing: 0,
    progressions: [
      [{ d: 0, q: '5' }, { d: 0, q: '5' }, { d: 3, q: '5' }, { d: 4, q: '5' }, { d: 0, q: '5' }, { d: 5, q: '5' }, { d: 3, q: '5' }, { d: 4, q: '5' }],
    ],
    drums: {
      kick:  { kick: 'x.........x.....' },
      snare: { snare: '........x.......' },
      hats:  { chh: 'x..x..x...x..x..', ohh: '..............x.' },
      perc:  { rim: '.....x.......x..', tomL: '...........o....' },
    },
    bass: 'wobble',
    comp: [[0, 2, 0.55]],
    pads: true,
    lead: { cells: { sustain: 3, dot: 2, rest: 2 }, octave: 4, range: 6 },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'lead', 'fx'],
    halftime: true,
  },
  dnb: {
    label: 'Drum & Bass', bpm: 174, scale: 'minor', bassOct: 1, swing: 0,
    progressions: [
      [{ d: 0, q: '9' }, { d: 3, q: '7' }, { d: 5, q: '9' }, { d: 4, q: '7' }, { d: 0, q: '9' }, { d: 3, q: '7' }, { d: 5, q: '9' }, { d: 6, q: 'shell' }],
    ],
    drums: {
      kick:  { kick: 'x.........x.....' },
      snare: { snare: '....x.......x...' },
      hats:  { chh: 'x.xxx.xxx.xxx.xx', ride: '..x...x...x...x.' },
      perc:  { shaker: 'x.x.x.x.x.x.x.x.', rim: '.......x..o.....' },
    },
    bass: 'reese',
    comp: [[0, 4, 0.6]],
    pads: true,
    lead: { cells: { two8: 3, offbeat: 2, dot: 2, rest: 2 }, octave: 5, range: 7 },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'lead', 'counter', 'fx'],
  },
  future_bass: {
    label: 'Future Bass', bpm: 150, scale: 'major', bassOct: 2, swing: 0,
    progressions: [
      [{ d: 3, q: '9' }, { d: 4, q: 'add9' }, { d: 2, q: '7' }, { d: 5, q: '9' }, { d: 3, q: '9' }, { d: 4, q: 'add9' }, { d: 5, q: '9' }, { d: 4, q: 'sus4' }],
      [{ d: 0, q: 'add9' }, { d: 4, q: '9' }, { d: 5, q: '9' }, { d: 3, q: 'add9' }, { d: 0, q: 'add9' }, { d: 4, q: '9' }, { d: 5, q: '9' }, { d: 4, q: '7' }],
    ],
    drums: {
      kick:  { kick: 'x......x..x.....' },
      snare: { snare: '........x.......', clap: '........x.......' },
      hats:  { chh: 'x..x.x..x..x.x..', ohh: '......x.......x.' },
      perc:  { shaker: '..x...x...x...x.', tamb: '........x.......' },
    },
    bass: 'sub',
    comp: [[0, 0.5, 1.0], [0.75, 0.5, 0.85], [1.5, 0.4, 0.9], [2, 0.5, 1.0], [2.75, 0.5, 0.85], [3.5, 0.45, 0.95]],
    pads: true,
    lead: { cells: { two8: 3, dot: 2, sustain: 2, rest: 1 }, octave: 5, range: 6, pentatonic: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'sub', 'bass', 'chords', 'pads', 'lead', 'counter', 'fx'],
    halftime: true,
  },
  trap: {
    label: 'Trap', bpm: 140, scale: 'harmonicMinor', bassOct: 1, swing: 0,
    progressions: [
      [{ d: 0, q: 'triad' }, { d: 0, q: 'triad' }, { d: 3, q: 'shell' }, { d: 4, q: 'triad' }, { d: 0, q: 'triad' }, { d: 5, q: 'shell' }, { d: 3, q: 'shell' }, { d: 4, q: 'triad' }],
    ],
    drums: {
      kick:  { kick: 'x.....x....x....' },
      snare: { snare: '........x.......' },
      hats:  { chh: 'xxxxxxxxxxxxxxxx' },
      perc:  { rim: '......x.......x.', congaL: '...o............' },
    },
    bass: '808',
    comp: [[0, 3.5, 0.5]],
    pads: true,
    lead: { cells: { dot: 3, sustain: 2, offbeat: 1.5, rest: 2.5 }, octave: 5, range: 6, dark: true },
    stems: ['kick', 'snare', 'hats', 'perc', 'bass', 'chords', 'pads', 'lead', 'fx'],
    halftime: true, hatRolls: true,
  },
};
```
