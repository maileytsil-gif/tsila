# Resampling Workflow

## Pourquoi resampler
- figer une transformation ;
- transformer un effet en nouveau matériau ;
- simplifier l'automation ;
- recouper précisément un tail ;
- faire plusieurs générations sans chaîne monstrueuse.

## Cycle
`DRY → TRANSFORM → RECORD/RESAMPLE → TRIM → NAME → RE-PITCH/SLICE → SECOND PASS`.

## [DOC] Serum 2
Le dernier accord/note joué peut être exporté en WAV par drag depuis Serum vers le DAW.

## [HEUR] Trois générations max avant contrôle
Après chaque génération : comparer au dry. Si l'identité utile disparaît, revenir à une génération antérieure.

## Versioning
- `VOC-shot_dry.wav`
- `VOC-shot_pitchformant_v01.wav`
- `VOC-shot_grain_v02.wav`
- `VOC-shot_predrop-final.wav`
