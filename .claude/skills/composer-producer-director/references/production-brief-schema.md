# Production Brief Schema

```yaml
project:
  title: optional
  state: idea | loop | arrangement | mix | revision
  destination: club | streaming | dj-set | radio | festival | hybrid
music:
  style: Bass House
  substyle: optional
  bpm: 126
  key: F minor
  emotion: dark / tense / euphoric
  duration_target: optional
  energy: 1-10
  vocal_role: none | chop | topline | full-song
creative:
  hook_type: bass | vocal | synth | chord | rhythm | hybrid
  references: []
  must_keep: []
  avoid: []
  freedom: low | medium | high
low_end:
  ownership: undecided | kick | bass | alternating | kick-rumble
  rumble: false
sound_palette:
  preferred_engines: [Serum 2, Ableton]
  available_plugins: [Waves, FabFilter, iZotope, Native Instruments, Valhalla]
execution:
  ableton_actions_requested: false
  bridge_available: unknown
  destructive_actions_allowed: false
```

The Director may fill missing fields with reversible `[HEUR]` assumptions, but must display them in the output.
