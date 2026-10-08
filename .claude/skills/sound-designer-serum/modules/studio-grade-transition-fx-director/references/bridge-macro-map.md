# Bridge Macro Map — Transitions

Conserver les 8 macros du système :

| Macro | Transition mapping |
|---|---|
| TONE | filter cutoff/brightness |
| MOTION | LFO/stutter/grain rate |
| BITE | resonance/drive/bit depth |
| WEIGHT | body/sub contribution |
| WIDTH | stereo spread |
| SPACE | reverb/delay wet/send |
| ATTACK | impact transient / gate snap |
| VARIATION | fill density / gesture intensity |

## Handoff
Une requête bridge doit spécifier : durée en mesures, courbe, valeur initiale, valeur finale, reset, cible résolue et test rollback.

Ne jamais supposer qu'un paramètre Serum est contrôlable tant qu'il n'est pas réellement exposé à Live `[TEST]`.
