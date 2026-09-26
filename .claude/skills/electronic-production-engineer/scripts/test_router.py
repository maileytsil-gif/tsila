#!/usr/bin/env python3
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / "ollama" / "run_skill.py"
spec = importlib.util.spec_from_file_location("runner", p)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

cases = [
    ("Augmente le drive de la bass via le bridge LOM sans casser automation", ["references/61-ableton-lom-bridge.md"], ["references/20-arrangement-engine.md"]),
    ("Construis un bridge de 8 mesures Tech House", ["references/20-arrangement-engine.md", "references/genres/tech-house.md"], ["references/61-ableton-lom-bridge.md"]),
    ("Break Afro House avec congas et shakers", ["references/genres/afro-house.md", "references/20-arrangement-engine.md"], []),
    ("Mastering Tech House avec Waves L4", ["references/50-mastering-engine.md", "references/genres/tech-house.md"], []),
    ("Crée une bass robotique avec OVox, Serum 2 et stutter", ["references/34-robotic-bass-vocoder-vocal-engine.md", "references/32-sound-design-engine.md"], []),
    ("Liquid drum and bass UK avec sampling vocal", ["references/genres/liquid-dnb.md", "references/33-sampling-stutter-engine.md"], []),
    ("Minimal DnB Alix Perez snare design", ["references/genres/minimal-deep-dnb.md", "references/37-drum-transient-design.md"], []),
    ("Sound design impact riser glitch avant drop", ["references/38-fx-atmos-transitions.md", "references/20-arrangement-engine.md"], []),
    ("Reverse cymbale avant le drop", ["references/39-reverse-pre-fx-engine.md"], []),
    ("Reverse cymban avant drop", ["references/39-reverse-pre-fx-engine.md"], []),
    ("Afro House + Melodic Techno hybrid", ["references/genres/afro-house.md", "references/genres/melodic-house-techno.md"], []),
    ("Prépare les stems label-ready et vérifie le dither", ["references/65-label-ready-qc-export.md", "references/66-project-performance-freeze-resample.md"], []),
    ("Réduire la latence CPU puis freeze la chaîne Serum", ["references/66-project-performance-freeze-resample.md"], []),
    ("Positionnement spatial de chaque élément, panning, largeur stereo et profondeur", ["references/41-spatial-spectrum-stereo-engine.md", "references/40-mix-engine.md"], []),
    ("Je veux un morceau livrable de A à Z pour label", ["references/03-end-to-end-production-lifecycle.md", "references/65-label-ready-qc-export.md"], []),
    ("Garde le sub mono et place les hats dans le champ stereo", ["references/41-spatial-spectrum-stereo-engine.md"], []),
]
for prompt, musts, must_nots in cases:
    refs = runner.select_refs(prompt)
    for must in musts:
        assert must in refs, (prompt, must, refs)
    for must_not in must_nots:
        assert must_not not in refs, (prompt, must_not, refs)

# False positives that v1.3 could trigger via substring matching.
false_positive_cases = [
    ("warehouse ambience for a film scene", "references/genres/house.md"),
    ("make only minimal changes to the volume", "references/genres/minimal-deep-tech.md"),
    ("housekeeping notes for the project", "references/genres/house.md"),
    ("remix metadata only", "references/40-mix-engine.md"),
]
for prompt, forbidden in false_positive_cases:
    refs = runner.select_refs(prompt)
    assert forbidden not in refs, (prompt, forbidden, refs)

print("router tests: OK")
