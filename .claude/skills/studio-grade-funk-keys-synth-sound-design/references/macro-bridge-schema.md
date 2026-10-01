# Macros et schéma de pilotage par le bridge

Les natifs (Electric, Analog, Tension, Drift, Operator, Wavetable, effets) sont pilotés et relus par `ppal-update-device` / `ppal-read-device` avec leurs noms API (`../../vst-sound-design/references/instruments-natifs.md`) ; Serum 2 et Kontakt par la fenêtre. Pour un Rack ou un patch destiné à l'IA, exposer en priorité :

| Macro | Fonction | Plage sûre à déterminer [TEST] |
|---|---|---|
| Bark / Bite | Electric : P Distance, P Amp In, M Force < Vel ; synth : cutoff + drive | ne jamais pousser au point de saturer à faible vélocité |
| Tone | Electric : F Tine Color, F Tine Vol / F Tone Vol ; Hammond : drawbars 8'/4' ; synth : cutoff | garder le corps |
| Tremolo / Pan | Auto Pan-Tremolo Amount (Rate fixée dans le patch : 5,6 Hz Wurli, 3–7 Hz Rhodes) | mono vérifié |
| Wah | Auto Filter Envelope amount et Frequency | pas de résonance qui siffle |
| Leslie | vitesse chorale ↔ tremolo (deux rampes différentes, horn et tambour) | automatisée, jamais instantanée |
| Glide | temps de portamento du synth bass / lead | 0 = aucun ; legato dans le patch |
| Drive | Saturator, J37, Pedal | niveau compensé |
| Space | envoi reverb/delay court | retour filtré |

Le bridge doit : `snapshot` → modifier → relire → comparer → `restore` si hors plage. Ce qui appartient au MIDI : vélocité par note, muting du Clav (durée), ghost notes, swing (`../../midi-expressif/SKILL.md`, `../../producteur-rythmique/SKILL.md`).
