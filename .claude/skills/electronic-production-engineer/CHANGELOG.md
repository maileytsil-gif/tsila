# Changelog

## 1.5.0
- Source-level merge of the v1.5.0 Claude handoff onto v1.4.0 (the handoff had been reconstructed without the v1.4.0 files; every v1.4.0 file is kept).
- SKILL.md: production phases brief → archive; Bridge contract rewritten as discover → resolve → plan → preflight → approval → execute → verify → rollback, plan_only by default, approval tied to the exact plan, high-impact operations listed, delete/overwrite denied by default, verification from a fresh read; inventory tools usable only once installed version and Set exposure are confirmed.
- Added `docs/production-workflow.md`, `docs/bridge-safety-and-semantics.md`, `docs/user-setup-and-control-surfaces.md`, `docs/claude-handoff-and-research-index.md`, `adapters/ollama-routing.md`.
- Added schemas `project-lifecycle` (the handoff's `production-lifecycle`, renamed so the v1.4.0 gate schema of that name is kept), `spatial-mix-plan`, `semantic-bridge-plan`, with `examples/*-example.json`; all validated (Draft 2020-12) by `scripts/validate_bridge_assets.py`.
- Ollama runner loads the matching v1.5.0 doc with the LOM bridge, A-to-Z lifecycle and hardware references; router tests extended.
- Not merged: the handoff's `SOURCE_STATUS.md` (obsolete once v1.4.0 was available) and its README (folded into this README).

## 1.4.0
- Reframed the success condition around a fully deliverable track from idea to archive, not only production/mix/master advice.
- Added an end-to-end lifecycle with exit gates for identity, core idea, palette, arrangement, spatial plan, mix prep, mix, pre-master QC, master, delivery QC and archive.
- Added a dedicated Spatial/Spectral/Stereo engine for spectrum roles, pan, width, depth, motion, M/S and mono/correlation verification.
- Added element-placement defaults for kick, sub, bass layers, snare/clap, hats, percussion, vocals, synths, pads, atmospheres, FX, impacts and returns.
- Added machine-readable `spatial-plan` and `production-lifecycle` schemas.
- Expanded label-ready QC to require explicit spatial planning, low-side/phase checks and re-imported deliverables.
- Added router coverage/tests for spatial placement and end-to-end delivery prompts.

## 1.3.0
- Added dedicated Reverse / Pre-FX / Suckback engine.
- Added reverse cymbal/crash, reverse reverb, reverse vocal, reverse impact, reverse kick/snare and reverse-noise workflows.
- Added transition-style reverse bass plus hard-dance/hard-techno rhythmic reverse-bass distinction.
- Added Serum 2 granular reverse and Maschine reverse/grain workflows.
- Added Ollama routing for reverse/pre-FX terminology.

## 1.2.0
- Added advanced sampling/resampling/stutter engine for Ableton, Maschine 3 and Serum 2.
- Added robotic/talking bass, OVox, Vocal Bender and Waves Tune workflows.
- Added melodic/robotic dubstep engine and Serum resampling/formant workflows.
- Added Liquid and Minimal/Deep DnB engines with UK and US/North-American study profiles.
- Added specialist kick, snare, electronic percussion and glitch design.
- Added atmosphere, impact, riser, downlifter and transition-FX engine.
- Added advanced video/document research notes and Ollama routing for the new modules.

## 1.1.0 — 2026-09-25
- Added Ableton Live Object Model Bridge contract.
- Added canonical semantic track/Rack/macro vocabulary.
- Added discovery and command JSON schemas.
- Added write safety, automation-state and rollback rules.
- Added plug-in profile strategy and example profile.
- Added Bridge discovery/action examples.
- Added Bridge asset validator and router tests.
- Improved Ollama routing to distinguish a musical bridge from the Ableton/AI Bridge.

## 1.0.0
- Initial portable multi-model production skill.
