# Drum/Percussion Macro Schema

Macros stables à préférer :

- `ATTACK`: transient prominence / envelope attack shape
- `TONE`: brightness/filter center
- `DECAY`: envelope/tail length
- `NOISE`: noise layer amount
- `METAL`: FM/inharmonic layer amount
- `TUNE`: tonal body pitch
- `WIDTH`: upper layer / tail width, not sub
- `SPACE`: send/reverb/delay amount
- `MOTION`: modulation depth/rate composite
- `VARIATION`: alternate layer/sample/modulation state

Le bridge doit mapper ces macros à des paramètres réels après discovery. Ne pas stocker des index de paramètres comme vérité permanente.
