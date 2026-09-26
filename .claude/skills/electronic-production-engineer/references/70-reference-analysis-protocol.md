# Reference-track analysis protocol

## Before analysis
Choose 2-4 references close in function, not only genre. One can be low-end reference, another drum/loudness reference, another arrangement/spatial reference.

## Measure/observe by section
Compare intro-to-intro, break-to-break and drop-to-drop. Log:
- BPM/key only if reliably known or measured.
- section lengths and energy curve,
- kick envelope/weight,
- bass rhythm/register,
- drum density/swing,
- harmonic density,
- vocal/hook role,
- depth/reverb/delay,
- stereo width/correlation,
- peak density/crest,
- integrated + short-term loudness when measured.

## Source/stem limitation
A commercial stereo master does not reveal exact plugin settings or stem levels. Phrase such conclusions as production inference. Do not claim a specific compressor, EQ curve or sidechain value unless documented by the producer/source.

## Four-reference method
For each genre keep four canonical references and identify what each teaches. Do not average them into one recipe; preserve differences within the genre.

## In this studio
- Put each reference on a muted `REF` track warped to the project tempo, level-matched, and mark a locator at every section change: that is how section lengths are obtained without inventing them (procedure in `../../house-future-rave-bass-house-production/references/arrangement-et-methode.md`; verified structures of real tracks from the Harmonix Set in `../../../../corpus/house-future-rave/harmonixset-segments-dance-edm.md`).
- Measure the reference and the user's export with the same tools (`02-capability-modes.md`, tools per mode); log the table in the project memory.
- One sound against a reference sound: `../../synthese-reference/SKILL.md` (`analyze_synth.py` → `report_to_patch.py` → `compare_reports.py`), which states what can and cannot be reconstructed.
- Producer facts (tools, mix engineers, keys, tempos) with their evidence level: `../../house-future-rave-bass-house-production/references/six-producteurs.md` (Guetta, MORTEN, Garrix, Chris Lake, Jauz, Dom Dolla). Spotify/Beatport keys are algorithmic and can miss the mode or relative key.

## A/B
Gain-match. If the user's track loses punch only when matched louder, consider reducing loudness rather than adding restoration processing.
