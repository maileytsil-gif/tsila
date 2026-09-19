# Compiler v18

`compile_project.py` transforme les contrats musicaux en `AbletonClipPlan`, puis en `BridgeActionBatch` conceptuel.

Exemple :
```bash
python core/compiler/compile_project.py --project-id demo --groove groove-spec.json --bass bass-interlock-spec.json --harmony harmony-spec.json --sound sound-spec.json --automation automation-spec.json --out-dir build
```

Les actions `ensure_track/create_clip/replace_notes/...` sont soumises à la Capability Matrix du bridge. Une action compilée ne prouve pas qu'elle est supportée dans l'instance Live courante.
