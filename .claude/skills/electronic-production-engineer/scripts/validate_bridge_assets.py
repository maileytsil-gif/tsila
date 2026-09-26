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

print("bridge assets: OK")
