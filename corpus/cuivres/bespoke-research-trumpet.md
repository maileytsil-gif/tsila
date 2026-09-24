---
titre: "Notes de recherche acoustique — trompette (bespoke-mcp-data-pack)"
source: https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/HEAD/overtone/instruments/brass-instruments/trumpet/RESEARCH.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: acoustique ; notes tierces
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Trumpet — acoustic research

**Family.** Brass — lip reed, flaring bore.
**Mechanism.** The lips act as an *outward-striking* pressure-controlled valve blowing into a
mouthpiece cup and a flaring bore terminated by a bell.
**Verdict: HYBRID.** Model the lip valve for real lip slurs, bends and misfires; add an explicit
nonlinear stage — or sample — for the brassiness bloom, which a linear waveguide cannot produce.

## The two facts that define brass

**1. The bell and mouthpiece rewrite the mode series.** A cylinder gives 1:3:5:7. The mouthpiece cup
and the bell flare together drag the bore's modes to approximately **2:3:4:5** — the harmonic series
*minus its fundamental*. That is why a trumpet plays a harmonic series on one fingering, and why the
pedal tone is a special case rather than the bottom of the series.

Measured against closed-pipe prediction on a real instrument:

| | mode 1 | … | top mode |
|---|---|---|---|
| predicted | 61.25 Hz | | 1653.75 Hz |
| measured | **233.00 Hz** | | **1617.00 Hz** |

The low modes are shifted enormously; the high modes barely move.

**2. Brassiness is nonlinear propagation, and a linear model cannot fake it.** Internal mouthpiece
SPL in forte measures **166.9 dB (B♭3) / 167.2 dB (B♭4)** — a substantial fraction of an atmosphere.
At that amplitude the wave *steepens toward a shock* as it travels the bore. Over a crescendo, **the
fundamental rises 8 dB while the ninth and higher harmonics rise more than 45 dB.**

This is the single most important thing about synthesising a trumpet. A waveguide with a gain knob
gets louder. A real trumpet gets *radically* brighter, and the ear reads that as loudness. If your
fortissimo is your mezzo-forte turned up, it will never sound like a trumpet.

## The other numbers

1. **Bore ~1.4 m** (LibreTexts) to **1.48 m** (3-D simulation study).
2. **Blowing pressure** from under 1 kPa to ~10 kPa — a very wide dynamic range of drive.
3. **The mouthpiece is a low-Q Helmholtz resonator** giving the brass formant; measured *popping
   frequencies* **745, 790, 820 Hz**. This formant does not track pitch and is a large part of brass
   identity.
4. **Mutes add strong formants in the 1–3 kHz band.**
5. **Bell cutoff:** essentially **no energy is returned from the flare above ~1500 Hz** (Benade, for
   trumpet; UNSW gives the trombone analogue as 700–800 Hz). Above cutoff the bell radiates rather
   than reflecting — which is both why brass is directional and why the model's reflection filter
   should roll off hard there.

## How it is actually synthesised

Waveguide plus a **BiQuad lip filter** — STK's `Brass`, after Cook's TBone/HosePlayer, exposing lip
tension (CC2) and slide length (CC4). The lip filter's resonance is what the player "chooses" when
slurring between harmonics, and modelling it is what buys you lip slurs and cracked notes for free.

For the brassiness, add either a shock-capturing nonlinear propagation stage along the bore, or at
minimum a **dynamics-keyed spectral-tilt stage** so that upper harmonics rise far faster than the
fundamental with drive.

## Reachable from Overtone on the render box

There is **no `stk-brass` binding in Overtone** — sc3-plugins' STK set as bound here covers
`stk-clarinet`, `stk-flute`, `stk-bowed`, `stk-blow-hole`, `stk-saxofony`, `stk-banded-wg`,
`stk-modal-bar`, `stk-shakers`, `stk-mandolin`, `stk-pluck`, `stk-voic-form`, `stk-bee-three`,
`stk-moog`. Brass is not in it.

So: build it, or sample it. Overtone ships **`overtone.inst.sampled-trumpet`** (upstreamed from
`karlthorssen/overtone-trumpet`, EPL-2.0) — one `require` away and a reasonable baseline.

For a built model, the pieces are a delay line with a lowpass reflection rolling off hard above
1.5 kHz, a resonant lip filter (`resonz`/`bpf`) whose centre is the player's chosen harmonic, a fixed
formant around 750–820 Hz for the mouthpiece, and a **drive-dependent waveshaper** for the bloom.
Faust has `brassModel(tubeLength, lipsTension, mute, pressure)` and `brassLipsTable` to read.

## Gestures a naive synth omits

- **Lip slurs** — moving between harmonics on one fingering, with no re-articulation.
- The **crescendo bloom** described above; this is the headline.
- Cracked and split notes when the lip resonance sits between modes.
- Breath attacks vs tongued attacks; the tongue's stop-start is a distinct transient.
- Mute changes as a formant change, not an EQ.

## Falsification checks

- **The crescendo test, and it is the definitive one:** render the same note pp and ff, and measure
  each harmonic's level. The fundamental should move ~8 dB while H9+ moves >45 dB. A linear model
  will move every harmonic by the same amount and fail unambiguously.
- **Mode ratios ≈ 2:3:4:5**, not 1:2:3:4 and not 1:3:5:7.
- **Rolloff above ~1500 Hz** in the reflected (not radiated) path.

## Sources

- [UNSW brass acoustics](https://newt.phys.unsw.edu.au/jw/brassacoustics.html) — mode realignment,
  bell cutoff, mouthpiece Helmholtz behaviour
- [STK Brass class docs](https://ccrma.stanford.edu/software/stk/classstk_1_1Brass.html)
- [3-D trumpet simulation (arXiv)](https://arxiv.org/html/1611.01025) — 1.48 m bore, the
  166.9/167.2 dB mouthpiece SPL figures
- [Faust physmodels](https://faustlibraries.grame.fr/libs/physmodels/) — `brassModel`,
  `brassLipsTable`
- [Philharmonia samples](https://philharmonia.co.uk/resources/sound-samples/) — free trumpet
  recordings across dynamics, which is exactly what you need to calibrate the bloom

*Method and cross-instrument context: `overtone/INSTRUMENT_RESEARCH.md` in the parent repo.*
