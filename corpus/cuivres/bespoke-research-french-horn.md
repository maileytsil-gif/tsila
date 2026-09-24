---
titre: "Notes de recherche acoustique — cor (bespoke-mcp-data-pack)"
source: https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/HEAD/overtone/instruments/brass-instruments/french-horn/RESEARCH.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: acoustique ; notes tierces
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# French horn — acoustic research

> **Research method.** This file was rebuilt 2026-08-16 from published acoustics literature (JASA
> papers on nonlinear brass propagation, music-acoustics texts, and instrument history sources) plus
> measured numbers from `catalog:phil-french-horn:sustain`. Every parameter in the `.clj` must trace
> to a numbered fact below or to the reference clip. Mark `[verified]` when the figure comes from a
> cited paper or standard text; `[from reference]` when measured on our Philharmonia clip only.

**Family.** Brass — lip-reed aerophone, moderately conical bore (Hornbostel–Sachs 423.232).
**Mechanism.** The lips act as a pressure-controlled valve into a long, mostly conical air column
terminated by a wide, backward-facing bell. Players select **high harmonics** of the bore resonance
rather than the pedal tone — the instrument is long and narrow enough that adjacent upper partials
are close together in frequency.
**Verdict: MODEL (hand-written).** No STK brass on the render box. Nonlinear brightness bloom
(Campbell 2019; Hirschberg et al. 1996) plus horn-specific spectral balance (conical bore, weak
fundamental in the radiated field).

---

## Why the physics matters here

1. **Conical bore and backward bell.** The horn is not a cylindrical trumpet: the bore flares
   continuously to a wide bell, often oriented backward so the direct high-frequency radiation toward
   the audience is reduced — a deliberately subdued, blended orchestral tone compared with trumpet or
   trombone (Wikipedia, *French horn* — bell orientation; Benade, cited in trumpet `RESEARCH.md`
   for conical vs cylindrical brassiness potential).

2. **Harmonic-series playing.** On the natural horn, a long narrow tube places upper partials close
   enough that melodic playing is possible by lip selection alone (Wikipedia — natural horn / hunting
   horn history). Modern double horns in F/B♭ retain this: written notes are upper modes, not the
   bore's lowest resonance. Our Philharmonia sustain at A2 shows **H4 loudest**, H1 **−19 dB**
   below peak, `f0_energy_share` **0.11** `[from reference]`.

3. **Nonlinear crescendo bloom (class H).** Campbell (2019) reviews experiments showing that brass
   timbre at *pp* is rounded while *ff* becomes sharply bright — in trombone, cumulative nonlinear
   distortion can form shock waves (Hirschberg et al. 1996). The same propagation mechanism applies
   to the horn family; the horn's *ff* is famously brassy while *pp* is soft-edged. The rebuilt
   trumpet in this repo measures **+320 Hz/dB** centroid rise; our horn model targets a large
   positive slope (committed **+60 Hz/dB**).

4. **Slow attack.** Lip and air-column onset for horn is slower than trumpet or trombone tonguing.
   Philharmonia sustain at A2: **attack_ms 107** `[from reference]`. Falsification window **40–120 ms**.

5. **Mouthpiece.** Funnel-shaped mouthpiece (vs trumpet cup) couples the embouchure to the conical
   leadpipe; excessive mouthpiece pressure is discouraged because it forces the tone (Wikipedia —
   mouthpiece placement). Not modelled explicitly — captured indirectly via formant/bore filtering.

---

## The numbers that decide whether it convinces

| Quantity | Value | Source |
|---|---|---|
| Written pitch for single/card | A2, MIDI 45, ~110 Hz | 7_9 b2 spec |
| Reference centroid | **859 Hz** | `[from reference]` phil-french-horn:sustain @ A2 |
| Reference attack (−20→−3 dB rise) | **107 ms** | `[from reference]` |
| H1 vs peak harmonic | **−19.1 dB** | `[from reference]` |
| `f0_energy_share` | **0.11** | `[from reference]` |
| `odd_even_db` | **−2.9 dB** (evens slightly louder) | `[from reference]` |
| Dynamic bloom target | Large positive Hz/dB on card bar 1 | Campbell (2019); committed +61 Hz/dB |
| Contrast vs trombone @ A2 | Lower centroid (trombone ref **1351 Hz**) | `[from reference]` |

---

## The thing most horn patches get wrong

**A trumpet model transposed down** — fixed harmonic count, fast tongued attack, and cylindrical-bore
brightness. The horn needs weaker fundamental energy in the radiated spectrum, slower envelope,
and a lower *pp* brightness ceiling that opens with blowing pressure (nonlinear bore propagation),
not a static high shelf.

---

## How it is actually synthesised

Hand-written extended `blip` source + **amp-keyed** harmonic count and bore lowpass (same mechanism
as `trumpet.clj`, following the "dynamics-keyed spectral tilt" minimum recommended when shock-wave
propagation cannot be simulated literally — Gilbert & Petiot 2008, cited in trumpet research).
Upper-partial emphasis via parallel `bpf` paths. STK `Brass` is not available on the render box.

---

## Reachable from Overtone on the render box

`blip`, `bpf`, `lpf`, `pink-noise`, `env-gen` — verified on trumpet/french-horn rebuild.

---

## Gestures a naive synth omits

- **Stopped horn** — right hand in bell raises pitch ~semitone, thins tone (Wikipedia).
- **pp → ff bloom** on one pitch (card bar 1).
- **Muting** — separate instrument (`phil-french-horn:mute`); not this model.

---

## Falsification checks

- `@check centroid-rises-with-amp true`
- `@check attack >40ms` and `@check attack <120ms`
- `@check h1-dominance <0dB`

---

## Build note (2026-08-16)

`french-horn.clj` — hand-written from trumpet brightness mechanism. Committed: centroid **971 Hz**
(1.13× ref), attack **~55–100 ms** (build window), H1 dominance **−7.5 dB**, card slope **+60 Hz/dB**,
level **6.90**, status **ok**.

---

## Bibliography

1. Campbell, D. Murray (2019). "To infinity and beyond: The life story of brass instrument shock
   waves." *Journal of the Acoustical Society of America*. Reviews nonlinear propagation and
   crescendo-driven spectral enrichment in trumpet, trombone, and horn. https://doi.org/10.1121/1.5136770

2. Hirschberg, A.; Gilbert, J.; et al. (1996). "Shock waves in trombones." *Journal of the
   Acoustical Society of America* **99**. Experimental confirmation of nonlinear wave steepening at
   *ff* in cylindrical brass; mechanism generalises across brass family. https://doi.org/10.1121/1.414698

3. Gilbert, J.; Petiot, J.-F. (2008). "Brassiness potential of wind instruments." *Proceedings of
   ISMA 2008*. Defines brassiness potential from bore profile and diameter; cylindrical instruments
   (trumpet, trombone) rank higher than predominantly conical horns and flugelhorns.
   (See also JASA paper on nonlinear propagation: https://doi.org/10.1121/1.3651093)

4. Benade, Arthur H. *Fundamentals of Musical Acoustics* (2nd ed.). Bell cutoff, mouthpiece
   formants, conical vs cylindrical bore — cited throughout repo brass research (`trumpet/RESEARCH.md`).

5. Fletcher, Neville H.; Rossing, Thomas D. *The Physics of Musical Instruments* (2nd ed.).
   Brass instruments, lip reed, bore modes.

6. Wikipedia contributors. "French horn." *Wikipedia*. Natural horn harmonic selection, backward
   bell, funnel mouthpiece, double horn F/B♭. https://en.wikipedia.org/wiki/French_horn (accessed
   2026-08-16).

7. **Local reference:** `catalog:phil-french-horn:sustain` — Philharmonia Orchestra, sustain
   articulation (92 regions), A2 mezzo-forte clip. Band A. Licence: free to use (verify before
   commercial release); 96 kbps MP3 source.

8. **Local model:** `data-packs/overtone/instruments/brass-instruments/trumpet/` — nonlinear brightness implementation
   and measured +320 Hz/dB slope.
