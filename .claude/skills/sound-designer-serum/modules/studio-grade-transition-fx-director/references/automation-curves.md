# Automation Curves

Toute automation doit préciser : `START → SHAPE → END → RESET`.

## Formes [HEUR]
- **Linear** : mécanique, prévisible, bon pour largeur ou send simple.
- **Exponential-in** : tension qui s'accélère ; très utile pour cutoff/pitch.
- **Log-like** : changement perceptible tôt puis stabilisation.
- **S-curve** : départ calme, accélération, arrivée douce.
- **Stepped** : tension rythmique, stutter, rate divisions.
- **Pulse** : coupures/portes synchronisées.
- **Random/jitter** : uniquement si le rôle est texture/instabilité.

## Reset discipline
Chaque paramètre automatisé doit avoir un état de sortie explicite. Éviter un feedback, width ou wet amount qui reste accidentellement ouvert après la transition.
