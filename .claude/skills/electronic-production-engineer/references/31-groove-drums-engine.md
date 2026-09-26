# Groove and drums engine

## Groove variables
Timing, velocity, probability, note length, accent, swing, pan, sample variation, filter, send level and silence.

## Starting grids [HEUR]
Studio grids (`../../drums-signature/references/patterns.md`, `../../drums-signature/scripts/drum_pattern.py`); 16 steps, 5 = beat 2, 3/7/11/15 = "and"; DnB: `36-dnb-engine.md`.
- **Deep/minimal house 120**: kick 1,5,9,13 v104–112 · clap 5,13 v70–82 · hats 3,7,11,15 v70–80 · ghosts 4,8,12 v28–40 · `swing(0.03)`.
- **Tech house 126**: clap v90 · rim 4,11 · hats 3,7,11,15 v85, 16th ghosts v35 · open 15 · ratchet fill on 16 · `swing(0.04)`.
- **Techno 130**: kick v110–118 · clap v88–96, out 1 bar in 8 · 16ths accented 90/60/70/60 · open 3,7,11,15 · no swing.
- **Melodic techno**: kick v100–108 · clap v62–72 · hats 3,7,11,15 · ghosts 2,8,10,16 v30–42 · no swing.

## Swing
Producer Pal's `swing()` unit is undocumented; read clips back [TEST]. In % (50 straight, 66 triplet): house 52–56, tech house 52–55 [COMM]; deep 55–62, deep tech 60–65, techno/DnB 50–60 [DOC-2]. Swing only 16ths 2 and 4 of a beat, never kick/clap; one value for hats/percs. Method: `../../producteur-rythmique/SKILL.md`.

## Minimal/Tech House
Use ghost percussion and micro-variation rather than constant new layers. Maschine/APC64 probability and euclidean tools are ideal for generating variation; commit promising patterns to Ableton for editing and safety.

## Afro House
Build interlocking parts rather than one dense loop. Assign each percussion layer a rhythmic role and depth plane. Humanization should be intentional: not random timing on every hit. Cells: son clave 3-2 = 1,4,7,11,13; 4/4 bell = 1,4,7,8,11,13,16; E(7,12) (`../../theorie-musicale-electronique/references/rythme-avance.md`) [DOC-2].

## Transient choice
Before compression, ask whether attack/sustain should simply be reshaped. Smack Attack, Drum Buss transient control or clip-envelope editing may be cleaner.

## Drum-bus processing
Glue only when it improves cohesion at matched loudness. API 2500 / SSL / TheBus can add character; RazorClip can shave peaks. Avoid flattening groove for numerical loudness.

## Fills
Fills announce structural information. Keep most fills short and section-specific. In Bass House they can be aggressive edits; in Minimal a single missing kick or delay throw may be enough.
