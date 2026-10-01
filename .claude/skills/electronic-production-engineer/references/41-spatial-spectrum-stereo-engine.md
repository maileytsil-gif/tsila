# Spatial, spectral and stereo placement engine

## Purpose
Plan where every important element lives before solving collisions with plugin stacking. Treat placement as four linked axes:
1. **Spectrum** — which frequency region carries the element's identity and which region must stay clear.
2. **Horizontal position** — center / left / right / distributed.
3. **Depth** — front / middle / back using level, transient definition, HF content, pre-delay, reverb/delay and early reflections.
4. **Width / motion** — mono, narrow, stereo, widened, or moving over time.

Tags: see `50-mastering-engine.md`. Repo sources (French): `../../house-future-rave-bass-house-production/references/mixage-mastering.md` §3, `../../../../corpus/house-future-rave/musicproductionwiki-tools-stereo-width-ms.md`.

This is a planning system, not a rigid frequency-allocation chart. Never carve fixed EQ holes just because a table says two sources should not overlap. Musical overlap is allowed when masking and translation remain controlled.

## Core laws
- Protect a stable center for kick, true sub, critical snare impact and primary lead/vocal focus unless the arrangement intentionally breaks this rule.
- Do not widen true sub by default. If a bass needs width, separate the low fundamental from upper harmonics and widen only the appropriate layer/range.
- Panning is not the same as stereo width. A stereo source can be rotated/positioned without collapsing it; a mono source can be panned without becoming stereo.
- Width above 100% or phase-derived widening requires mono/correlation verification.
- Depth is created by multiple cues, not reverb alone: level, transient sharpness, HF roll-off, direct/reverb ratio, pre-delay and early reflections all matter.
- Preserve transients of front-positioned drums. If stereo modulation is used on a percussion source, consider keeping the onset more centered and moving the sustain.
- Mid/Side processing is a correction/creative tool, not a default mastering ritual.

## Planning matrix — default starting roles
These are starting intents. Override by genre/reference and the actual source.

| Element | Spectrum role | Horizontal | Width | Depth | Mono policy / risk |
|---|---|---|---|---|---|
| Kick | sub/low + attack presence | center | mono/narrow | front | keep fundamental stable; phase check with bass |
| True sub | sub | center | mono | front-middle | mono; avoid stereo modulation |
| Mid-bass / growl | low-mid to high-mid identity | center core + optional stereo upper layer | narrow→wide by layer | front-middle | protect low crossover; check M/S cancellation |
| Snare main | body + crack/presence | center or near-center | narrow core | front | stereo room/noise can surround core |
| Clap layer | mid/high transient | slight offset or stereo layer | medium | front-middle | check summed transient in mono |
| Closed hat | high-mid/air | offset L/R | narrow/medium | front-middle | use alternating positions; avoid all hats hard-wide |
| Open hat / ride | high/air | offset/opposite supporting hat | medium/wide | middle | mono check; harsh side build-up risk |
| Shaker | upper-mid/high rhythm | L/R or moving | medium | middle | micro-motion okay; keep groove readable in mono |
| Conga/tom/perc | low-mid/mid transient | distributed by role | narrow/medium | middle | avoid excessive low-end stereo on low drums |
| Lead synth | mid/presence identity | center core | mono core + stereo FX/layers | front | keep hook readable in mono |
| Chords/stabs | low-mid/mid/harmonic bed | distributed | medium/wide | middle | leave center space when vocal/lead owns it |
| Pad | low-mid→air bed | stereo | wide | back | high-pass/side control as needed; phase check |
| Lead vocal | mid/presence intelligibility | center | narrow core | front | stereo doubles/FX around core, not instead of core |
| Backing vocal | mid/high support | L/R distributed | medium/wide | middle/back | timing/pitch spread must survive mono |
| Atmosphere | broadband/air/texture | stereo | wide/moving | back | keep low end filtered/controlled when necessary |
| Impact | low/body + high transient | center low + stereo high | medium | front | avoid wide sub impact |
| Riser/reverse | mid/high motion | movement allowed | medium/wide | moves toward front | automate width/pan only if transition stays mono-safe |
| Reverb return | source-dependent | stereo field | medium/wide | back | bass mono/HPF where appropriate; check side build-up |
| Delay return | source-dependent | stereo/alternating | medium/wide | middle/back | automate ducking/feedback; mono check |

## Frequency-role planning
Do not assign an element one narrow band. Assign three roles instead:
- **Fundamental/body zone**: where the element gains weight or pitch identity.
- **Definition zone**: where it becomes recognizable in the mix.
- **Optional air/texture zone**: where stereo width and ambience may live.

For each element, record:
- what must remain audible,
- what can be sacrificed,
- what it collides with,
- which source should win in that collision,
- whether separation should be timing, level, envelope, arrangement, EQ, dynamic EQ, sidechain or stereo placement.

## Horizontal field strategy
### Center anchors
Usually: kick, sub, main snare body, primary vocal/lead, essential bass core.

### Supporting distribution
Use hats, percussion, doubles, textures, chord layers and FX to create asymmetry and width. Avoid perfectly symmetric static placement when the genre/reference benefits from organic movement.

### Stereo sources
Before using the DAW pan control on an already-stereo source, decide whether the goal is:
- **rotation/relocation** of the complete stereo image,
- **narrowing** then panning,
- **split-stereo panning** of L/R channels,
- or a creative imbalance.
Use Waves S1 rotation (installed, not yet probed) or Live's Split Stereo pan mode (a mixer mode, not a device) when the goal is to move the stereo image without unintentionally collapsing it.

## Width strategy
Use three zones conceptually:
- **Foundation**: mono or very narrow.
- **Identity**: controlled stereo; keep important mid information.
- **Decoration/air**: widest permissible zone, usually safest place for motion and ambience.

Ableton Utility (a tolerated native) can narrow or widen, sum to mono, and Bass Mono can mono low frequencies with an adjustable cutoff. Treat the cutoff as source-dependent, not a universal 120 Hz rule: repo starting points are 120 Hz in house (bx_glue Mono Maker on the bass bus) and 150 Hz in bass house, and sources go up to 200 Hz [DOC-2].

Width-by-band starting points [COMM]: below 150 Hz mono; 150 Hz–2 kHz 0–60 %; above 2 kHz 60–200 %. House: claps/percs ±20 %, hats/rides/returns ±50–80 %, narrower intros/outros for DJs.

## Depth strategy
### Front
More direct level, sharper transient, less reverb, longer pre-delay when reverb is used, more presence/HF detail.

### Middle
Moderate direct/reverb balance, softened transients if appropriate, shorter pre-delay or stronger early reflections than a front source.

### Back
Lower direct level, more wet/early reflections, softer transient, more HF attenuation, and sometimes longer diffuse tail. Avoid making every "back" element simply louder in reverb.

## Motion strategy
Use motion to create life, not instability.
- Slow auto-pan: pads, textures, noise, long percussion tails (mixer pan automation, `../../live-automation/SKILL.md`).
- Tempo-synced alternating pan: hats, percs, delays.
- One-shot automation: risers, reverse FX, transitions.
- Keep critical onset centered while moving sustain when punch must remain stable.

## Mid/Side rules
Use M/S when the source is genuinely stereo and the problem is better expressed as center-vs-side rather than left-vs-right.
Examples:
- remove low-frequency side energy while keeping mid bass intact,
- tame harsh cymbal information mainly in Side,
- control a wide pad's low-mid sides to open the center,
- preserve center lead while shaping side ambience.
Do not assume linear phase is always required; use it when channel-specific EQ phase interactions would otherwise create unwanted shifts and latency/pre-ringing are acceptable.

## Genre tendencies
### House / Tech House
Strong center low end; hats/percs create lateral groove. Keep vocal/hook focus clear. Short rooms and delays can build depth without washing the drop; high-pass returns at 150–200 Hz and duck them under the dry signal [COMM].

### Minimal / Deep Tech
Use sparse lateral detail and micro-motion. A few tiny pan/depth moves can carry more interest than broad constant widening.

### Techno
Center kick/rumble foundation; stereo motion lives mainly in upper percussion, synth modulation, noise, reverbs and transition FX. Wide rumble is a special effect, not a default.

### Bass House / Dubstep
Separate sub/core (mono below about 150 Hz [COMM]) from wide mid/high growl layers. Call/response can also alternate lateral position, but preserve a stable impact anchor.

### Liquid DnB
Center kick/snare/sub; width often comes from breaks/tops, pads, keys, vocal FX and atmospheres. Keep snare impact coherent in mono.

### Minimal/Deep DnB
Center is highly disciplined. Use small stereo details and controlled room/ambience; avoid filling every gap with width.

### Afro House
Center kick/bass; distribute organic percussion with human asymmetry and depth. Reverbs/rooms may create a natural ensemble image rather than exaggerated artificial width.

## Verification protocol
1. Static mono check: does any essential element disappear or lose unreasonable body?
2. Correlation/vector check when using widening/phase manipulation: +1 = mono-identical, 0 = uncorrelated, negative = cancellation; keep the mix above 0, ideally above +0.5 [COMM]. SPAN shows correlation; Imager does not.
3. Low-frequency side audit: solo Side or use M/S analyzer; verify sub stability. For kick/sub, measure 30–120 Hz correlation on separate exports with `../../kick-bass-equilibre/scripts/kick_bass_check.py` (see `30-low-end-engine.md`).
4. Low-volume check: center hierarchy should remain understandable.
5. Headphone check: no distracting hard-pan fatigue or artificial phase halo.
6. Speaker check: stereo stage should not collapse unpredictably.
7. Reference comparison: level-match and compare section-to-section, not whole-song averages.

## Preferred tools in this studio
Status and sheets: `01-studio-inventory.md`.
- Ableton Utility (tolerated): Width, Mid/Side, Mono, Bass Mono, phase, gain.
- Mixer pan / Split Stereo pan mode; pan automation for movement (Auto Pan-Tremolo is a native effect outside rule 6's tolerated list: ask).
- bx_glue Mono Maker on the bass bus (exposed).
- iZotope Ozone Imager 2: global Width exposed (+8 % on master bus 2 in the repo chain); bands window-only.
- FabFilter Pro-Q 4 (window-only): L/R or M/S frequency-specific placement.
- FabFilter Pro-C 3 (not yet probed): linked/unlinked or Mid/Side dynamics when justified.
- Waves S1 (not yet probed): stereo image width/rotation and stereo-source positioning.
- soothe3: dynamic resonance control; use stereo/M/S only when the actual issue is moving/side-specific harshness.
- Voxengo SPAN: correlation and spectrum (Avg 4000 ms, block 8192).
- Returns: Hybrid Reverb on a return (tolerated); Valhalla and H-Delay to probe. Use shared returns for depth rather than a different large reverb on every track.

## Machine-readable spatial plan
When a project needs explicit placement, use `../schemas/spatial-plan.schema.json`. Do not invent measured frequency values; mark them as intended/estimated until analyzer/audio evidence exists.
