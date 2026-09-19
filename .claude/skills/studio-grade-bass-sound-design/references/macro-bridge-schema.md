# Macro / Bridge schema

Pour un patch destiné au contrôle IA/bridge, exposer en priorité :

| Macro | Fonction | Plage sûre à déterminer [TEST] |
|---|---|---|
| Tone | cutoff / harmonic tilt | jamais fermer au point de disparaître involontairement |
| Motion | LFO depth / WT position range | garder un groove intelligible |
| Bite | distortion/resonance | éviter feedback runaway |
| Weight | sub/body balance | compensation niveau recommandée |
| Width | upper layer only | sub exclu |
| Space | send/delay/reverb | retour filtré |
| Attack | env/transient | éviter clicks non voulus |
| Variation | fill/end-of-phrase | état par défaut neutre |

Le bridge doit : snapshot → modifier → lire retour → comparer → restaurer si hors plage. Ne pas automatiser un paramètre non exposé/confirmé [TEST].
