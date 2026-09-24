---
titre: "KinhkhaTran/edm-midi-studio — lib/generators.js (suite : batterie, accords voice-led, archétypes de basse offbeat8/rolling/rolling8/rumble16/wobble/reese/sub/808, cellules rythmiques de lead, hooks « festival »/« tech »/« melodic », contre-mélodie) + lib/theory.js intégral (gammes, qualités d'accords, voice leading, swing16, grooveVel)"
source: https://raw.githubusercontent.com/KinhkhaTran/edm-midi-studio/main/lib/generators.js (+ https://raw.githubusercontent.com/KinhkhaTran/edm-midi-studio/main/lib/theory.js)
recupere_le: 2026-09-24
mode: texte integral (extrait complémentaire)
langue: en
axe: théorie spécifique (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Complément de `edm-midi-studio-genres-future-rave-extrait.md` (README + bloc GENRES). Code communautaire [HEUR-lu] : les chiffres (vélocités, durées, grilles) sont des choix d'un générateur, pas des mesures sur des titres.

# lib/generators.js — de « Drums » à « Melody » (lignes après le bloc GENRES)

```js
// ---------------------------------------------------------------------------
// Drums
// ---------------------------------------------------------------------------

const VEL = { X: 118, x: 96, o: 52 };

function stepsToNotes(pattern, pitch, barOffset, rng, swing) {
  const notes = [];
  for (let i = 0; i < 16; i++) {
    const c = pattern[i];
    if (c === '.' || c === undefined) continue;
    const start = swing16(barOffset + i * 0.25, swing);
    const vel = Math.max(20, Math.min(127, VEL[c] + Math.floor((rng() - 0.5) * 12)));
    notes.push({ pitch, start, dur: 0.22, vel });
  }
  return notes;
}

function makeDrumStem(stemPatterns, g, bars, rng) {
  const { chance } = rngHelpers(rng);
  const notes = [];
  for (let bar = 0; bar < bars; bar++) {
    const off = bar * 4;
    for (const [inst, pattern] of Object.entries(stemPatterns)) {
      let pat = pattern;
      if (inst !== 'kick' && inst !== 'snare' && chance(0.3)) {
        const i = Math.floor(rng() * 16);
        pat = pat.slice(0, i) + (pat[i] === '.' ? 'o' : '.') + pat.slice(i + 1);
      }
      notes.push(...stepsToNotes(pat, DRUMS[inst], off, rng, g.swing));
    }
  }
  return notes;
}

function makeHatRolls(bars, rng) {
  const { chance, pick } = rngHelpers(rng);
  const notes = [];
  for (let bar = 0; bar < bars; bar++) {
    if (!chance(0.65)) continue;
    const off = bar * 4 + pick([2.5, 3, 3.5]);
    const rate = pick([0.125, 0.125, 0.0625]);
    const count = pick([4, 6, 8]);
    for (let i = 0; i < count; i++) {
      notes.push({ pitch: DRUMS.chh, start: off + i * rate, dur: rate * 0.8, vel: 52 + Math.round((i / count) * 46) });
    }
  }
  return notes;
}

// ---------------------------------------------------------------------------
// Harmony: voice-led chords + pads + sub
// ---------------------------------------------------------------------------

function makeChordLayers(g, ctx) {
  const { root, scale, progression, bars, rng } = ctx;
  const comp = [], pads = [], sub = [];
  let prevVoicing = null;

  for (let bar = 0; bar < bars; bar++) {
    const off = bar * 4;
    const spec = progression[bar % progression.length];
    const raw = chordPitches(root + 24, scale, spec);
    const voicing = voiceLead(raw, prevVoicing, 62);
    prevVoicing = voicing;

    // Comp layer: rhythmic hits.
    for (const [start, dur, velScale] of g.comp) {
      const vel = Math.max(30, Math.min(127, Math.round(96 * velScale + (rng() - 0.5) * 8)));
      for (const p of voicing) comp.push({ pitch: p, start: off + start, dur, vel });
    }
    // Pad layer: sustained, wider (root doubled below), softer.
    if (g.pads) {
      const padVoicing = [voicing[0] - 12, ...voicing];
      for (const p of padVoicing) pads.push({ pitch: p, start: off, dur: 3.9, vel: 62 });
    }
    // Sub: root of each chord, held.
    const subPitch = scalePitch(root - 12, scale, spec.d);
    sub.push({ pitch: Math.max(24, subPitch), start: off, dur: 3.8, vel: 104 });
  }
  return { comp, pads, sub };
}

// ---------------------------------------------------------------------------
// Bass archetypes (with approach notes into the next chord)
// ---------------------------------------------------------------------------

function makeBass(style, ctx) {
  const { root, scale, progression, bars, rng, swing } = ctx;
  const { chance, pick } = rngHelpers(rng);
  const notes = [];
  const rootAt = (bar) => scalePitch(root, scale, progression[bar % progression.length].d);

  for (let bar = 0; bar < bars; bar++) {
    const off = bar * 4;
    const rootPitch = rootAt(bar);
    const nextRoot = rootAt(bar + 1);
    const approach = nextRoot + (nextRoot > rootPitch ? -1 : 1); // chromatic approach

    switch (style) {
      case 'offbeat8':
        for (let b = 0; b < 4; b++) {
          const last = b === 3;
          notes.push({
            pitch: last && chance(0.4) ? approach : rootPitch,
            start: off + b + 0.5, dur: 0.4, vel: grooveVel(b + 0.5, 102, rng),
          });
        }
        break;
      case 'rolling': {
        const grid = [0, 0.75, 1.5, 2, 2.75, 3.5];
        grid.forEach((t, i) => {
          const isLast = i === grid.length - 1;
          const oct = chance(0.25) ? 12 : 0;
          const pitch = isLast && chance(0.5) ? approach : rootPitch + oct;
          notes.push({ pitch, start: swing16(off + t, swing), dur: 0.35, vel: oct ? 84 : grooveVel(t, 102, rng) });
        });
        break;
      }
      case 'rolling8':
        for (let i = 0; i < 8; i++) {
          let pitch = rootPitch;
          if (i === 6 && chance(0.5)) pitch += 7;
          if (i === 7 && chance(0.5)) pitch = approach;
          notes.push({ pitch, start: off + i * 0.5, dur: 0.42, vel: i % 2 ? 88 : 104 });
        }
        break;
      case 'rumble16':
        for (let i = 0; i < 16; i++) {
          if (i % 4 === 0) continue;
          notes.push({ pitch: rootPitch, start: off + i * 0.25, dur: 0.2, vel: i % 2 ? 66 : 86 });
        }
        break;
      case 'wobble': {
        const grid = pick([[0, 1, 1.5, 2.5, 3], [0, 0.75, 1.5, 2, 3, 3.5], [0, 1.5, 2, 3, 3.75]]);
        for (const t of grid) {
          const move = pick([0, 0, 7, 12, -12, 3]);
          notes.push({ pitch: rootPitch + move, start: off + t, dur: pick([0.4, 0.65, 0.9]), vel: 110 });
        }
        break;
      }
      case 'reese':
        notes.push({ pitch: rootPitch, start: off, dur: 2.4, vel: 104 });
        notes.push({ pitch: chance(0.4) ? approach : rootPitch + pick([0, 5, 7, -2]), start: off + 2.5, dur: 1.4, vel: 96 });
        break;
      case 'sub':
        notes.push({ pitch: rootPitch, start: off, dur: 3, vel: 106 });
        if (chance(0.6)) notes.push({ pitch: rootPitch + 12, start: off + 3.25, dur: 0.5, vel: 80 });
        break;
      case '808':
        notes.push({ pitch: rootPitch, start: off, dur: chance(0.5) ? 3.9 : 2.4, vel: 112 });
        if (chance(0.5)) notes.push({ pitch: rootPitch + pick([7, 12, -5, 3]), start: off + 2.5, dur: 1.2, vel: 96 });
        break;
    }
  }
  return notes;
}

// ---------------------------------------------------------------------------
// Arp
// ---------------------------------------------------------------------------

function makeArp(cfg, ctx) {
  const { root, scale, progression, bars } = ctx;
  const notes = [];
  for (let bar = 0; bar < bars; bar++) {
    const off = bar * 4;
    const spec = progression[bar % progression.length];
    const base = chordPitches(root + 12 * (cfg.octave - 1), scale, { d: spec.d, q: 'triad' });
    let seq = [...base, ...base.map(p => p + 12)];
    if (cfg.pattern === 'updown') seq = [...seq, ...seq.slice(1, -1).reverse()];
    const stepsPerBar = Math.round(4 / cfg.rate);
    for (let i = 0; i < stepsPerBar; i++) {
      notes.push({
        pitch: seq[i % seq.length], start: off + i * cfg.rate,
        dur: cfg.rate * 0.8, vel: i % 4 === 0 ? 92 : 72,
      });
    }
  }
  return notes;
}

// ---------------------------------------------------------------------------
// Melody: motif-based phrase construction (A A' B A'' with development)
// ---------------------------------------------------------------------------

// Rhythm cells: one beat each, [offsetInBeat, dur][] — gaps are rests.
const CELLS = {
  sustain: [[0, 1]],
  two8:    [[0, 0.5], [0.5, 0.5]],
  dot:     [[0, 0.75], [0.75, 0.25]],
  gallop:  [[0, 0.5], [0.5, 0.25], [0.75, 0.25]],
  six:     [[0, 0.25], [0.25, 0.25], [0.5, 0.25], [0.75, 0.25]],
  offbeat: [[0.5, 0.5]],
  syncop:  [[0, 0.25], [0.5, 0.25]],
  rest:    [],
};

// Build a 1-bar motif: rhythm from weighted cells + a stepwise contour.
function buildMotif(cfg, rng) {
  const { weighted } = rngHelpers(rng);
  const cellPairs = Object.entries(cfg.cells).map(([k, w]) => [k, w]);
  const slots = [];
  for (let beat = 0; beat < 4; beat++) {
    const cell = CELLS[weighted(cellPairs)] || [];
    for (const [o, d] of cell) slots.push({ beat: beat + o, dur: d });
  }
  // Contour: random walk in scale degrees, small steps, starting on a chord tone.
  const { weighted: w2, pick } = rngHelpers(rng);
  let deg = pick([0, 2, 4]);
  const degs = slots.map((_, i) => {
    if (i > 0) {
      deg += w2([[0, 1.5], [1, 3], [-1, 3], [2, 1.5], [-2, 1.5], [3, 0.6], [-3, 0.6]]);
      deg = Math.max(-3, Math.min(cfg.range, deg));
    }
    return deg;
  });
  return slots.map((s, i) => ({ ...s, deg: degs[i] }));
}

const CHORD_TONE_OFFSETS = [0, 2, 4, 6];

// Render a motif over a specific chord with optional transforms.
function renderMotif(motif, spec, barOffset, cfg, ctx, opts = {}) {
  const { root, scale, rng } = ctx;
  const notes = [];
  const melodyRoot = root + 12 * cfg.octave;
  const bias = opts.bias || 0;

  motif.forEach((slot, i) => {
    if (opts.skipLast && i === motif.length - 1) return;
    let deg = spec.d + slot.deg + bias;
    // Strong beats land on chord tones: snap to the nearest chord-tone offset.
    if (slot.beat % 1 === 0) {
      const rel = slot.deg + bias;
      const nearest = CHORD_TONE_OFFSETS.reduce((a, b) =>
        Math.abs(b - (((rel % 7) + 7) % 7)) < Math.abs(a - (((rel % 7) + 7) % 7)) ? b : a);
      deg = spec.d + Math.floor(rel / 7) * 7 + nearest;
    }
    let pitch = scalePitch(melodyRoot, scale, deg);
    pitch = snapToScale(pitch, root, scale);
    const start = barOffset + slot.beat + (opts.shift || 0);
    let dur = slot.dur;
    // Resolution: final slot of a resolving bar becomes a long chord-root note.
    if (opts.resolve && i === motif.length - 1) {
      pitch = scalePitch(melodyRoot, scale, spec.d + (rngHelpers(rng).chance(0.5) ? 0 : 4));
      dur = Math.max(dur, 1.5);
    }
    const vel = grooveVel(slot.beat, cfg.acid ? 88 : 94, rng);
    notes.push({ pitch, start, dur: dur * 0.92, vel });
    // Ornament: occasional 16th approach note before a beat-1 note.
    if (opts.ornament && slot.beat === 0 && rngHelpers(rng).chance(0.5)) {
      notes.push({ pitch: pitch - (scale === 'major' ? 1 : 2), start: start - 0.25, dur: 0.2, vel: vel - 24 });
    }
  });
  return notes.filter(n => n.start >= barOffset - 0.26);
}

const MODERN_HOOKS = {
  festival: [
    [[0, 0.5, 0], [0.5, 0.5, 2], [1.5, 0.5, 4], [2, 0.75, 7], [3, 0.25, 6], [3.25, 0.5, 4]],
    [[0, 0.75, 4], [1, 0.5, 7], [1.75, 0.25, 6], [2, 0.5, 4], [2.75, 0.25, 2], [3, 0.75, 0]],
  ],
  melodic: [
    [[0, 1.0, 2], [1.25, 0.5, 4], [2, 0.75, 5], [3, 0.75, 4]],
    [[0, 0.75, 0], [1, 0.5, 2], [1.75, 0.25, 4], [2.25, 0.75, 2], [3.25, 0.5, 0]],
  ],
  tech: [
    [[0.5, 0.25, 0], [1, 0.25, 0], [1.5, 0.25, 2], [2.5, 0.25, 0], [3, 0.25, 4], [3.5, 0.25, 2]],
    [[0, 0.25, 0], [0.75, 0.25, 2], [1.5, 0.25, 0], [2, 0.25, 3], [2.75, 0.25, 2], [3.5, 0.25, 0]],
  ],
  organic: [
    [[0, 0.5, 0], [0.75, 0.25, 2], [1.25, 0.75, 4], [2.5, 0.5, 2], [3.25, 0.5, 0]],
    [[0.25, 0.5, 4], [1, 0.5, 5], [1.75, 0.25, 4], [2.25, 0.75, 2], [3.25, 0.5, 0]],
  ],
};

function nearestChordDegree(rel) {
  return CHORD_TONE_OFFSETS.reduce((best, cand) => Math.abs(cand - rel) < Math.abs(best - rel) ? cand : best, CHORD_TONE_OFFSETS[0]);
}

// Modern EDM hook writer learned from production tutorials: write chords first,
// use chord tones as rails, repeat a tiny motif, then change only the ending.
function makeModernLead(cfg, ctx) {
  const { progression, root, scale, rng } = ctx;
  const { pick, chance } = rngHelpers(rng);
  const hooks = MODERN_HOOKS[cfg.hook] || MODERN_HOOKS.melodic;
  const notes = [];
  for (let bar = 0; bar < 8; bar++) {
    const spec = progression[bar % progression.length];
    const base = hooks[bar % 2];
    const isAnswer = bar % 4 === 3;
    const isClimax = bar === 6;
    const isResolve = bar === 7;
    const bias = isClimax ? pick([2, 3, 4]) : isAnswer ? pick([-1, 0, 1]) : 0;
    for (let i = 0; i < base.length; i++) {
      const [beat, dur0, rel0] = base[i];
      let rel = rel0 + bias;
      if (beat === 0 || beat === 2 || dur0 >= 0.75) rel = nearestChordDegree(((rel % 7) + 7) % 7) + Math.floor(rel / 7) * 7;
      if (isResolve && i >= base.length - 2) rel = chance(0.55) ? 0 : 4;
      let pitch = scalePitch(root + 12 * cfg.octave, scale, spec.d + rel);
      if (isClimax && i === Math.floor(base.length / 2)) pitch += 12;
      pitch = snapToScale(pitch, root, scale);
      const start = bar * 4 + beat;
      const dur = isResolve && i === base.length - 1 ? Math.max(1.25, dur0) : dur0 * 0.92;
      notes.push({ pitch, start, dur, vel: grooveVel(beat, cfg.hook === 'tech' ? 92 : 100, rng) });
      if (i > 0 && chance(cfg.hook === 'tech' ? 0.2 : 0.38) && dur0 <= 0.5) {
        notes.push({ pitch: snapToScale(pitch + pick([-2, -1, 1, 2]), root, scale), start: Math.max(bar * 4, start - 0.25), dur: 0.18, vel: 58 });
      }
    }
  }
  return notes.sort((a, b) => a.start - b.start);
}

function makePianoGuide(leadNotes) {
  return leadNotes
    // Strip grace/connectors; keep the actual hook targets a producer would play on piano.
    .filter((n, i) => i === 0 || n.dur >= 0.35 || n.vel >= 94)
    .map(n => {
      let pitch = n.pitch;
      while (pitch > 84) pitch -= 12;
      while (pitch < 48) pitch += 12;
      return { ...n, pitch, dur: Math.max(0.45, n.dur), vel: Math.min(88, Math.max(56, n.vel - 18)) };
    });
}

// 8-bar phrase: A A' B A(resolve) | A A' B climax→resolve
function makeLead(cfg, ctx) {
  if (cfg.hook) return makeModernLead(cfg, ctx);
  const { progression, rng } = ctx;
  const motifA = buildMotif(cfg, rng);
  const motifB = buildMotif(cfg, rng);
  const plan = [
    { m: motifA, opts: {} },
    { m: motifA, opts: { ornament: true } },
    { m: motifB, opts: { bias: cfg.soaring ? 2 : 1 } },
    { m: motifA, opts: { skipLast: true, resolve: true } },
    { m: motifA, opts: {} },
    { m: motifA, opts: { shift: 0, ornament: true } },
    { m: motifB, opts: { bias: cfg.soaring ? 3 : 2 } },      // climax bar
    { m: motifA, opts: { resolve: true } },
  ];
  const notes = [];
  plan.forEach((step, bar) => {
    const spec = progression[bar % progression.length];
    notes.push(...renderMotif(step.m, spec, bar * 4, cfg, ctx, step.opts));
  });
  return notes.sort((a, b) => a.start - b.start);
}

// Counter-melody: answers in the lead's gaps, harmonized a third below, octave down.
function makeCounter(leadNotes, cfg, ctx) {
  const { root, scale, progression, bars, rng } = ctx;
  const { chance } = rngHelpers(rng);
  const notes = [];
  for (let bar = 0; bar < bars; bar++) {
    const off = bar * 4;
    const spec = progression[bar % progression.length];
    const inBar = leadNotes.filter(n => n.start >= off && n.start < off + 4);
    // Find gaps of at least 3/4 beat.
    const gaps = [];
    let cursor = off;
    for (const n of [...inBar].sort((a, b) => a.start - b.start)) {
      if (n.start - cursor >= 0.75) gaps.push([cursor, n.start]);
      cursor = Math.max(cursor, n.start + n.dur);
    }
    if (off + 4 - cursor >= 0.75) gaps.push([cursor, off + 4]);

    for (const [g0, g1] of gaps) {
      if (!chance(0.65)) continue;
      const pitch = snapToScale(
        scalePitch(root + 12 * (cfg.octave - 1), scale, spec.d + (chance(0.5) ? 2 : 4)),
        root, scale,
      );
      notes.push({ pitch, start: g0 + 0.25, dur: Math.min(1.2, g1 - g0 - 0.25), vel: 72 });
    }
  }
  return notes;
}

```

# lib/theory.js (texte intégral)

```js
// Music theory primitives: scales, extended chords, voice-leading, seeded randomness.

export const NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];

export const SCALES = {
  minor:         [0, 2, 3, 5, 7, 8, 10],
  major:         [0, 2, 4, 5, 7, 9, 11],
  dorian:        [0, 2, 3, 5, 7, 9, 10],
  phrygian:      [0, 1, 3, 5, 7, 8, 10],
  harmonicMinor: [0, 2, 3, 5, 7, 8, 11],
  mixolydian:    [0, 2, 4, 5, 7, 9, 10],
  lydian:        [0, 2, 4, 6, 7, 9, 11],
};

export function noteToMidi(name, octave) {
  const idx = NOTE_NAMES.indexOf(name);
  if (idx === -1) throw new Error(`Unknown note name: ${name}`);
  return idx + (octave + 1) * 12;
}

// Scale degree (0-indexed, any integer incl. negative) -> MIDI pitch.
export function scalePitch(rootMidi, scaleName, degree) {
  const scale = SCALES[scaleName] || SCALES.minor;
  const oct = Math.floor(degree / scale.length);
  const idx = ((degree % scale.length) + scale.length) % scale.length;
  return rootMidi + oct * 12 + scale[idx];
}

// Snap an arbitrary MIDI pitch to the nearest scale note.
export function snapToScale(pitch, rootMidi, scaleName) {
  const scale = SCALES[scaleName] || SCALES.minor;
  const rel = ((pitch - rootMidi) % 12 + 12) % 12;
  let best = scale[0], bestDist = 12;
  for (const s of scale) {
    for (const cand of [s, s - 12, s + 12]) {
      const d = Math.abs(cand - rel);
      if (d < bestDist) { bestDist = d; best = cand; }
    }
  }
  return pitch + (best - rel);
}

// ---------------------------------------------------------------------------
// Chords: diatonic stacked thirds + quality-based extensions.
// A chord spec: { degree, quality, borrowed? } where quality picks intervals
// relative to the *diatonic* chord tones, so extensions stay in key.
// ---------------------------------------------------------------------------

// Which stacked-third offsets (in scale degrees above the chord degree) to include.
export const CHORD_QUALITIES = {
  triad:  [0, 2, 4],
  '7':    [0, 2, 4, 6],
  '9':    [0, 2, 4, 6, 8],
  '6':    [0, 2, 4, 5],
  add9:   [0, 2, 4, 8],
  sus2:   [0, 1, 4],
  sus4:   [0, 3, 4],
  '5':    [0, 4, 7],       // power chord + octave — big room sounds
  shell:  [0, 2, 6],       // root, third, seventh — jazzy and open
};

export function chordPitches(rootMidi, scaleName, spec) {
  const degree = typeof spec === 'number' ? spec : spec.degree;
  const quality = (typeof spec === 'object' && spec.quality) || 'triad';
  const offsets = CHORD_QUALITIES[quality] || CHORD_QUALITIES.triad;
  let pitches = offsets.map(o => scalePitch(rootMidi, scaleName, degree + o));
  // Modal interchange: flatten/raise specific chord tones for borrowed color.
  if (typeof spec === 'object' && spec.alter) {
    pitches = pitches.map((p, i) => p + (spec.alter[i] || 0));
  }
  return pitches;
}

// ---------------------------------------------------------------------------
// Voice leading: revoice a chord so each voice moves as little as possible
// from the previous voicing. Keeps progressions smooth instead of jumpy.
// ---------------------------------------------------------------------------

export function voiceLead(pitches, prevVoicing, center = 60) {
  if (!prevVoicing || !prevVoicing.length) {
    // First chord: park the voicing around the center.
    const centroid = pitches.reduce((a, b) => a + b, 0) / pitches.length;
    const shift = Math.round((center - centroid) / 12) * 12;
    return pitches.map(p => p + shift).sort((a, b) => a - b);
  }
  // For each chord tone choose the octave closest to any previous voice,
  // with a soft pull toward the center so voicings don't drift away.
  const voiced = pitches.map(p => {
    let best = p, bestScore = Infinity;
    for (let oct = -2; oct <= 2; oct++) {
      const cand = p + oct * 12;
      const nearest = Math.min(...prevVoicing.map(v => Math.abs(cand - v)));
      const score = nearest + Math.abs(cand - center) * 0.15;
      if (score < bestScore) { bestScore = score; best = cand; }
    }
    return best;
  });
  // Collapse unisons that can appear after octave folding.
  return [...new Set(voiced)].sort((a, b) => a - b);
}

// ---------------------------------------------------------------------------
// Randomness & feel
// ---------------------------------------------------------------------------

export function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export const rngHelpers = (rng) => ({
  pick: (arr) => arr[Math.floor(rng() * arr.length)],
  weighted: (pairs) => { // [[value, weight], ...]
    const total = pairs.reduce((a, [, w]) => a + w, 0);
    let r = rng() * total;
    for (const [v, w] of pairs) { r -= w; if (r <= 0) return v; }
    return pairs[pairs.length - 1][0];
  },
  chance: (p) => rng() < p,
  int: (lo, hi) => lo + Math.floor(rng() * (hi - lo + 1)),
});

// Swing: delay every off-16th. amount 0..1 (0.55-0.62 is a musical MPC-ish zone).
export function swing16(start, amount) {
  if (!amount) return start;
  const pos = start % 0.5;
  return Math.abs(pos - 0.25) < 0.01 ? start + (amount - 0.5) * 0.5 : start;
}

// Velocity accent map for 16th grid positions within a beat (downbeat strongest).
export function grooveVel(start, base, rng) {
  const step = Math.round((start % 1) / 0.25) % 4;
  const accent = [1.0, 0.82, 0.92, 0.78][step];
  const jitter = (rng() - 0.5) * 10;
  return Math.max(20, Math.min(127, Math.round(base * accent + jitter)));
}
```
