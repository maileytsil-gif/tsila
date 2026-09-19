# CHANGELOG v18 — Technical Integration

- Director linéaire remplacé par un graphe conditionnel selon le style.
- Ajout de 8 contrats JSON Schema : ProductionBrief, GrooveSpec, BassInterlockSpec, HarmonySpec, SoundSpec, AutomationSpec, AbletonClipPlan, BridgeActionBatch.
- Ajout d'un compiler musical `Specs → AbletonClipPlan → BridgeActionBatch`.
- Ajout de `source-registry.json` et provenance par source_id.
- `patterns.json` migré vers un format event-based avec distinction DOC/HEUR.
- Ajout de timing profiles role-dependent et matrice d'hybridation.
- Bridge enrichi avec `requires_capability` et frontière compiler/executor.
- Trois scénarios end-to-end + export MIDI + validation automatisée.
- Changelogs/validations historiques déplacés sous `/history`; un seul `VALIDATION.json` courant à la racine.
