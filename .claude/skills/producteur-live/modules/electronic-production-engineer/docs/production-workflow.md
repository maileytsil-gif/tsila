# Production workflow: brief to reproducible delivery

Detailed exit gates: `../references/03-end-to-end-production-lifecycle.md` (G0–G10), which also maps these phases onto the studio's eight-step method and project memory. Before any Live action, check where the session runs (`../references/02-capability-modes.md`).

## Phase gates

| Phase | Required artifact | Gate to continue |
|---|---|---|
| Brief / identity | `brief` with references, constraints, target context, delivery list | Unknowns are visible; user agrees on direction |
| Composition | hook, harmony, groove, motif roles | Core idea is recognizable without production polish |
| Sound design | palette with source, method, print/freeze status | Every layer has a role; source versions remain recoverable |
| Arrangement | section map and energy/density curve | Transitions are intentional; length and structure match the brief |
| Spectral / spatial | per-role spectrum, pan, width, depth, mono and collision plan | Low-end ownership and mono policy are explicit |
| Mix | signal-flow map, decisions, reference comparisons | Main elements translate at matched level; no unresolved mix blockers |
| Premaster | premaster export and review notes | Mix approved before loudness/limiting decisions |
| Master | chosen processing rationale and measured render | Master suits delivery and survives translation checks |
| QC | checklist with measurements and file audit | Every requested format passes or has an explicit exception |
| Archive | collected Live project, exports, notes, dependency manifest, hashes | Set opens with media present; archive has a reproducible identity |

## Practical workflow

1. Ask for or inspect the brief. Capture target audience/use, references, genre range, energy, approximate duration, tempo/key if known, vocal/content constraints, and requested delivery formats.
2. Create the musical skeleton before detailed processing: kick/bass interaction, core motif, harmonic center, and groove. Use Maschine MK3 for playable sampling/pattern exploration; APC64 for Live clip/scene and performance control; A49 for playable parts and browsing; Serum 2 or Komplete Kontrol when the sound role calls for them.
3. Print/resample intentionally. Name source and print distinctly; document tuning, tempo, start/end, and processing. Keep an editable instrument source or a duplicate before destructive operations.
4. Arrange using named sections and musical events. State exactly what enters, exits, transforms, or remains. Model build, break, bridge, drop, and outro as functions, not genre stereotypes.
5. Draft the spatial/spectral plan before heavy mix processing. Include frequency role (qualitative or measured), stereo mode, center/side policy, depth, movement, overlap, and mono check for each important element.
6. Inspect routing and gain path. Diagnose source choice, envelope, timing, phase, level, and masking before EQ/dynamics. Use the user's Waves, FabFilter, soothe3, and Analog Obsession tools only if present and mapped (`../references/01-studio-inventory.md`); no new native Ableton effects in mix or master chains (user rule 6).
7. Keep premaster and master renders separate. Compare alternate master approaches at matched loudness. Document actual integrated loudness and true peak after render; do not treat a target as a quality score.
8. Export each requested deliverable with a deterministic name. Re-import or inspect each file for duration, channels, sample rate, bit depth, silence, tails, clipping, and requested loudness/peak constraints.
9. In Live, use Collect All and Save for a portable project copy. Include a manifest for external plug-ins, versions, licenses/dependencies, sample provenance, and render settings. Hash delivered files. Where possible, reopen the collected project and verify missing-media status.

## Definition of done

The work is done only when the brief is represented, the musical and arrangement decisions are documented, the spatial/spectral plan is checked, the premaster/master exports pass QC, and the archive can be identified and reopened with its referenced media. A polished master alone is not a complete delivery.

