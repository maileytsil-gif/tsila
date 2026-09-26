#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "bridge" / "semantic-vocabulary.json",
    ROOT / "schemas" / "ableton-discovery.schema.json",
    ROOT / "schemas" / "ableton-command.schema.json",
    ROOT / "examples" / "bridge-discovery-output.json",
    ROOT / "examples" / "bridge-action-plan.json",
    ROOT / "schemas" / "spatial-plan.schema.json",
    ROOT / "schemas" / "production-lifecycle.schema.json",
    ROOT / "examples" / "spatial-plan-tech-house.json",
    ROOT / "schemas" / "project-lifecycle.schema.json",
    ROOT / "schemas" / "spatial-mix-plan.schema.json",
    ROOT / "schemas" / "semantic-bridge-plan.schema.json",
    ROOT / "examples" / "project-lifecycle-example.json",
    ROOT / "examples" / "spatial-mix-plan-example.json",
    ROOT / "examples" / "semantic-bridge-plan-example.json",
]
for p in required:
    if not p.exists():
        raise SystemExit(f"missing: {p.relative_to(ROOT)}")
    if p.suffix == ".json":
        json.loads(p.read_text())

try:
    import jsonschema
except ImportError:
    jsonschema = None

if jsonschema:
    discovery_schema = json.loads((ROOT / "schemas" / "ableton-discovery.schema.json").read_text())
    command_schema = json.loads((ROOT / "schemas" / "ableton-command.schema.json").read_text())
    discovery = json.loads((ROOT / "examples" / "bridge-discovery-output.json").read_text())
    action = json.loads((ROOT / "examples" / "bridge-action-plan.json").read_text())
    spatial_schema = json.loads((ROOT / "schemas" / "spatial-plan.schema.json").read_text())
    spatial = json.loads((ROOT / "examples" / "spatial-plan-tech-house.json").read_text())
    jsonschema.validate(discovery, discovery_schema)
    jsonschema.validate(action, command_schema)
    jsonschema.validate(spatial, spatial_schema)
    for name in ("project-lifecycle", "spatial-mix-plan", "semantic-bridge-plan"):
        schema = json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.validate(json.loads((ROOT / "examples" / f"{name}-example.json").read_text()), schema)

print("bridge assets: OK")
