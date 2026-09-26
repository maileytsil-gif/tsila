# Evidence and source policy

## Source hierarchy
1. Official manuals/documentation and producer/label statements.
2. Official educational videos/demos from Ableton, Native Instruments, Waves, oeksound, FabFilter, Akai, SAE or equivalent.
3. High-quality third-party deconstructions/tutorials.
4. Community discussion as anecdotal evidence only.

## Evidence tags (shared with the studio's French skills)
| Tag | Meaning |
|---|---|
| `[DOC]` | read in full: official manual, dataset, the repo file that cites it (e.g. the Serum 2 map checked against the 354-page manual: `../../sound-designer-serum/references/serum2-cartographie.md`) |
| `[DOC-2]` | secondary compilation read in full, citing its primary source |
| `[DOC-EXTRAIT]` | only a summary/excerpt of a page that could not be read; never quote it word for word |
| `[COMM]` | community convention (forum, genre sheet): a declared habit, not a measurement |
| `[HEUR]` | practice or starting point, with its logic |
| `[CALC]` | arithmetic (e.g. ms = 60000 / BPM × note fraction) |
| `[TEST]` | must be checked in the user's Set, version or files before relying on it |
| `MUET` / `not verified` | no source says it |
These tags qualify facts; `MEASURED / HEARD / INFERRED / STARTING POINT` (`00-operating-principles.md`) qualify statements about the user's own audio. A `[HEUR]` or `[COMM]` range never becomes a rule; an excerpt never becomes a quote.

## Local sources first
Before searching online, read the repo copy: manuals and pages in `../../../../corpus/` (index in `../../../../corpus/INDEX.md`; Serum 2 manual split per chapter in `corpus/constructeur/xferrecords-com-manual-serum-2-docs-NN-*.md`, page markers `<!-- page N -->`). Pages that could not be fetched from the cloud are listed in `corpus/sources-a-telecharger*.json` for `corpus/scripts/fetch_sources.py` on the Mac.

## Audio analysis
When actual audio is available, derive measurements from it where tools allow. When only a commercial release/title is known, keep sonic analysis qualitative and label inferences.

## Video learning
Extract principles and audible before/after effects, not just knob positions. Cross-check surprising technical claims against manuals or another credible source.

## Currentness
Software/hardware versions change. Verify current manuals/version-specific behavior before giving installation, routing or compatibility instructions.
