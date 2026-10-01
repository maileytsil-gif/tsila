---
titre: "Notes de recherche acoustique — trombone (bespoke-mcp-data-pack)"
source: https://raw.githubusercontent.com/Crack-Pantelimon/bespoke-mcp-data-pack/HEAD/overtone/instruments/brass-instruments/trombone/RESEARCH.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: acoustique ; notes tierces
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Trombone — acoustic research

> **Research method.** Rebuilt 2026-08-16 from JASA papers on trombone shock waves and brass
> nonlinear propagation, plus measured `catalog:phil-trombone:sustain`. `[verified]` = cited literature;
> `[from reference]` = Philharmonia clip.

**Family.** Brass — lip-reed aerophone, **predominantly cylindrical bore** with flared bell.
**Mechanism.** Lip valve → long cylindrical tube (~2.7 m class) → bell. Pitch changed by telescoping
slide (continuous length). At high blowing pressure, **nonlinear wave steepening** in the cylinder
redistributes energy to upper harmonics — the brightest orchestral brass bloom in the section.
**Verdict: MODEL (hand-written).** Steeper amp→spectrum coupling than horn; same render-box constraints
as trumpet.

---

## Why the physics matters here

1. **Cylindrical bore = maximum brassiness potential.** Gilbert & Petiot (2008) and related JASA work
   show brassiness potential is highest for instruments with long cylindrical sections (trumpet,
   trombone) and lower for predominantly conical instruments (horn, flugelhorn). The trombone bore
   is **0.45–0.55 in (11–14 mm)** cylindrical through the slide, expanding only at the bell
   (Wikipedia, *Trombone* — bore dimensions) `[verified]`.

2. **Shock waves at ff.** Hirschberg et al. (1996) measured internal trombone pressures and observed
   shock-front formation at fortissimo — stepwise pressure jumps and strongly enriched high harmonics.
   Campbell (2019) reviews this as the mechanism behind the audible "brassy" / *cuivré* crescendo.

3. **Harmonic selection.** Like other lip-reed brass, the player selects a harmonic of the air-column
   resonance. Philharmonia sustain at A2: **H2 loudest** (0 dB), H1 **−19.4 dB**, centroid **1351 Hz**,
   `f0_energy_share` **0.11** `[from reference]`.

4. **Dynamic bloom — steepest in b2 brass trio.** Falsification requires the largest card
   `centroid-rises-with-amp` slope among horn, trombone, tuba. Committed model: **+102 Hz/dB**
   (horn +60 Hz/dB, trumpet +84 Hz/dB for comparison).

5. **Slide glissando.** Continuous pitch change is idiomatic (Wikipedia; Berio *Sequenza V*). Standard
   generated card does not gliss — falsification uses dynamic pair + spectrum only.

---

## The numbers that decide whether it convinces

| Quantity | Value | Source |
|---|---|---|
| Single/card pitch | A2, MIDI 45 | 7_9 b2 spec |
| Reference centroid | **1351 Hz** | `[from reference]` |
| Reference attack | **46 ms** | `[from reference]` |
| H1 vs peak | **−19.4 dB** | `[from reference]` |
| Bloom slope (committed) | **+102 Hz/dB**, r=0.95 | build measurement |
| Horn contrast @ A2 | Horn centroid **859 Hz** | `[from reference]` |

---

## The thing most trombone patches get wrong

**Fixed spectrum or horn-like conical filtering.** Cylindrical steepening + extreme dynamic bloom are
the identity. A transposed horn or static `blip` with a fader fails `centroid-rises-with-amp`.

---

## How it is actually synthesised

Hand-written `blip` + steeper `amp` and `amp²` terms on harmonic count and bore cutoff than horn.
Msallam-style wave steepening is modelled as **dynamics-keyed spectral tilt** (frequency-domain
approach described in BYU/Msallam trombone steepening literature) rather than literal shock capturing.

---

## Reachable from Overtone on the render box

`blip`, `bpf`, `lpf`, `pink-noise`, `env-gen`.

---

## Falsification checks

- `@check centroid-rises-with-amp true` — steepest in b2 brass trio.
- `@check h1-dominance <0dB`

---

## Build note (2026-08-16)

`trombone.clj` committed: centroid **1.10×** ref, slope **+102 Hz/dB**, level **5.10**, status **ok**.

---

## Bibliography

1. Hirschberg, A.; van Hassel, R.; et al. (1996). "Shock waves in trombones." *JASA* **99**.
   https://doi.org/10.1121/1.414698 `[verified]` — shock formation at ff.

2. Campbell, D. Murray (2019). "To infinity and beyond: The life story of brass instrument shock
   waves." *JASA*. https://doi.org/10.1121/1.5136770 `[verified]` — crescendo spectral evolution.

3. Gilbert, J.; Petiot, J.-F. (2008). "Effects of nonlinear sound propagation on the characteristic
   timbres of brass instruments." *JASA* **123** (and ISMA 2008 brassiness-potential work).
   https://doi.org/10.1121/1.3651093 `[verified]` — trombone highest brassiness in crescendo tests.

4. Msallam, R.; Stronge, W.J.; et al. (2001). Frequency-domain trombone model including wave
   steepening. *JASA* **110**(1). https://physics.byu.edu/docs/publication/1517 `[verified]`.

5. Wikipedia contributors. "Trombone." Cylindrical bore, slide mechanism, bore 11.4–13.9 mm,
   bell 18–22 cm. https://en.wikipedia.org/wiki/Trombone (accessed 2026-08-16).

6. **Local reference:** `catalog:phil-trombone:sustain` (79 regions), band A.

7. **Local models:** `trumpet.clj`, `french-horn.clj` — brightness mechanism chain.
