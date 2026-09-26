# Electronic Production Engineer — portable skill pack

One canonical Agent Skill for electronic music production in Ableton Live, designed to be reused by ChatGPT/OpenAI Agent Skills, Claude Code, Qwen Code and Qwen models running locally through Ollama.

The skill covers House, Tech House, Minimal/Deep Tech, Techno, Bass House, Melodic House/Techno, Afro House, Melodic Dubstep, Liquid DnB and Minimal/Deep DnB; full A-to-Z production gates, arrangement (break/bridge/build/drop), sampling/resampling/stutter, robotic bass/vocoder vocals, specialist kick/snare/percussion design, atmospheres/risers/impacts/transitions, spatial/spectral/stereo placement, groove, low-end, mixing, mastering, delivery QC, references and the studio hardware/plugin workflow.

Start with `adapters/INSTALL.md`.

Version: 1.5.0 (2026-09-26)


## v1.1 Bridge layer
Adds a Live Object Model control contract, semantic track/Rack/macro vocabulary, read-only discovery snapshot schema, validated command schema, write/automation safety rules, plug-in profile strategy, examples and validation assets.


## v1.2 focus
Adds advanced sampling/stutter, robotic bass and vocoder vocals, melodic dubstep, Liquid/Minimal DnB (UK + US crossover profiles), kick/snare/percussion synthesis and transition-FX design.

## v1.3 focus
Adds reverse/pre-FX/suckback sound design: reverse bass, reverse cymbal/crash, reverse kick/snare, reverse reverb/vocal, reverse impacts/noise, granular reverse and hard-dance-style reverse-bass routing.


## v1.4 focus
Turns the skill into an end-to-end release workflow with explicit production gates from brief to reproducible archive. Adds a dedicated spatial/spectral/stereo engine covering element-by-element frequency role, panning, width, depth, motion, M/S, mono/correlation checks, and machine-readable spatial/lifecycle schemas.

## v1.5 focus
Merges the v1.5.0 Claude handoff (reconstructed without the v1.4.0 files) onto v1.4.0 at source level: nothing from v1.4.0 was removed. Adds the phase gates and definition of done (`docs/production-workflow.md`), a stricter plan_only Bridge contract with approval tied to the exact plan (`docs/bridge-safety-and-semantics.md`), user setup, control-surface roles and naming/macro conventions (`docs/user-setup-and-control-surfaces.md`), an official manuals/tutorial index (`docs/claude-handoff-and-research-index.md`), the local Qwen/Ollama trust boundary (`adapters/ollama-routing.md`), and three schemas with validated examples (`project-lifecycle`, `spatial-mix-plan`, `semantic-bridge-plan`).

