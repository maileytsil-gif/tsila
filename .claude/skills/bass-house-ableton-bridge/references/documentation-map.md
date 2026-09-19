# Carte documentaire — Ableton Bridge

| Règle | Type | Source | Conséquence architecture |
|---|---|---|---|
| Tout Live n'est pas exposé par LOM | DOC | Cycling '74 Live API Overview | capability discovery obligatoire |
| IDs LiveAPI dynamiques, ne pas persister | DOC | Cycling '74 JS LiveAPI | rediscovery à chaque contexte/session |
| get/set/call/observe via Live API | DOC | Cycling '74 Live API | lecture/écriture/observation structurées |
| `live.remote~` contrôle DeviceParameter en temps réel | DOC | Cycling '74 `live.remote~` | moteur temps réel séparé du set_value |
| `live.remote~` doit être libéré et n'est pas une automation stockée | DOC | Cycling '74 `live.remote~` | cleanup explicite, pas de faux « automation written » |
| automation absolue ≠ modulation relative | DOC | Ableton Clip Envelopes / M4L Automation | modèle de données distinct |
| Node for Max = processus séparé/asynchrone | DOC | Cycling '74 Node for Max / node.script | request IDs, timeout, lifecycle |
| Plug-in : seuls paramètres publiés peuvent être configurés | DOC | Ableton Working with Instruments/Effects | discovery VST obligatoire |
| Contrôle GUI complet de Serum par LOM | TEST/Non acquis | aucune preuve LOM | ne pas le promettre |
| Écriture automation Arrangement via bridge actuel | TEST | dépend implémentation/version | test réel obligatoire |

## Sources

- https://docs.cycling74.com/userguide/m4l/live_api_overview/
- https://docs.cycling74.com/userguide/m4l/live_api/
- https://docs.cycling74.com/apiref/js/liveapi/
- https://docs.cycling74.com/reference/live.remote~/
- https://docs.cycling74.com/userguide/m4l/device_parameters/
- https://docs.cycling74.com/userguide/m4l/automation_and_storing_data/
- https://docs.cycling74.com/apiref/nodeformax/
- https://docs.cycling74.com/reference/node.script/
- https://www.ableton.com/en/live-manual/12/working-with-instruments-and-effects/
- https://www.ableton.com/en/manual/clip-envelopes/
