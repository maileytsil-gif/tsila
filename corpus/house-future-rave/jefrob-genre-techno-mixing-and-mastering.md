---
titre: "JefroB Electronic-Music-Genre-Skills — Techno : mixing-and-mastering.md (peak time / hard / industrial / minimal / acid / dub : LUFS, plage dynamique, glue, EQ du kick — voisinage de la future rave)"
source: https://raw.githubusercontent.com/JefroB/Electronic-Music-Genre-Skills/master/.agent/skills/genre-techno/references/mixing-and-mastering.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: mixage et mastering (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Fiche de genre écrite pour agents IA (dépôt communautaire) ; les cibles LUFS et les réglages sont des conventions déclarées [HEUR], pas des mesures de masters commerciaux.

# Mixing & Mastering Benchmarks

## Peak Time Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–50 Hz | Kick sub fundamental | Strong, controlled |
| 50–100 Hz | Kick body | DOMINANT |
| 100–300 Hz | Kick upper body, bass harmonics | Moderate, clean |
| 300 Hz–1 kHz | Synth stabs lower mids | Present, no mud |
| 1–4 kHz | Synth stabs, clap presence, hat body | Bright, aggressive |
| 4–8 kHz | Hat shimmer, percussion transients | Bright |
| 8–16 kHz | Hat air, noise textures | Present |
| 16–20 kHz | Air | Subtle |

### Stereo Field
- **Mono center**: Kick, sub bass, synth stab fundamental
- **Narrow stereo (±20%)**: Clap, main percussion
- **Wide stereo (±50–80%)**: Hi-hats, rides, reverb returns, noise textures
- **Overall width**: Moderate-wide — punch in center, energy in sides
- **Mono compatibility**: Critical for festival PAs

### Dynamics & Loudness
- **Target LUFS (club master)**: -7 to -9 LUFS integrated
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 5–8 dB (compressed for impact)
- **Bus compression**: Medium-heavy (4–6 dB GR), fast attack, medium release
- **Limiter**: Working moderately (2–4 dB GR)
- **Philosophy**: Loud and punchy — the kick must hit hard on big systems

### EQ Signature Moves
- High-pass everything except kick at 80–120 Hz
- Kick: boost 50–60 Hz (sub), boost 3–4 kHz (click), cut 200–400 Hz (boxiness)
- Synth stabs: cut 200–300 Hz (clear mud), boost 2–4 kHz (presence)
- Hi-hats: HPF at 6–8 kHz, gentle boost at 10–12 kHz (shimmer)
- Master: gentle shelf boost above 8 kHz for air, cut 200–300 Hz if muddy

### Reference Tracks for Mixing
- Adam Beyer — "Teach Me" (punchy, loud, clear low end)
- Sam Paganini — "Rave" (aggressive, balanced)
- Amelie Lens — "Hypra" (modern peak time reference)

### Common Mix Mistakes
- Kick and synth stab competing at 100–300 Hz (sidechain or EQ split)
- Too much reverb (kills punch and definition)
- Over-limiting destroying transient punch
- Not enough low-end mono focus (phase issues on club PA)
- Hi-hats too loud/harsh (fatigue on extended listening)

---

## Hard Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–50 Hz | Kick sub (reduced) | Moderate |
| 50–150 Hz | Kick body, distortion fundamentals | Strong |
| 150–500 Hz | Distortion harmonics, bass energy | DOMINANT |
| 500 Hz–2 kHz | Synth stabs, noise body | Very present |
| 2–6 kHz | Distortion harmonics, transients | Aggressive |
| 6–12 kHz | Hat harmonics, noise upper | Bright, harsh |
| 12–20 kHz | Air, distortion artifacts | Present |

### Stereo Field
- **Mono center**: Kick, primary bass/distortion
- **Narrow stereo**: Clap/snare, main noise hits
- **Wide stereo**: Noise textures, reverb returns, secondary hits
- **Overall width**: Moderate — aggression from center, chaos from sides
- **Mono compatibility**: Important (warehouse PAs are often mono)

### Dynamics & Loudness
- **Target LUFS (club)**: -6 to -8 LUFS integrated
- **Target LUFS (streaming)**: -14 LUFS (will be normalized)
- **Dynamic range**: 4–6 dB (intentionally compressed/crushed)
- **Bus compression**: Heavy (6–10 dB GR), fast attack
- **Limiter**: Working hard (3–6 dB GR) — loudness is aesthetic choice
- **Philosophy**: LOUD — distortion and compression are the genre's texture

### EQ Signature Moves
- HPF on kick at 40–60 Hz (less sub than peak time — more punch)
- Boost 150–300 Hz on kick for distorted body
- Synths: cut below 200 Hz aggressively (all low end to kick)
- Master: accept harshness at 2–6 kHz — it's intentional
- No de-essing — harshness is genre-appropriate

### Reference Tracks for Mixing
- FJAAK — "Mess" (aggressive, well-mixed hard techno)
- 999999999 — live recordings (raw analog power)
- Dax J — "Offending Public Morality" (balanced aggression)

---

## Industrial Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub, drone | Strong, felt |
| 60–200 Hz | Kick body, EBM bass | Strong |
| 200–500 Hz | Bass harmonics, metallic resonances | Present |
| 500 Hz–2 kHz | Metallic percussion, EBM harmonics | DOMINANT |
| 2–6 kHz | Metal transients, noise | Aggressive |
| 6–12 kHz | Noise, harshness | Present |
| 12–20 kHz | Noise artifacts | Variable |

### Stereo Field
- **Mono center**: Kick, bass/EBM, primary metallic hit
- **Narrow stereo**: Secondary percussion, noise hits
- **Wide stereo**: Noise textures, reverb, atmospheric drones
- **Overall width**: Wide-ish — noise fills stereo field, rhythm in center
- **Note**: Some industrial is mixed narrow/mono for claustrophobic effect

### Dynamics & Loudness
- **Target LUFS (club)**: -7 to -9 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 5–8 dB (variable — some preserve dynamics)
- **Bus compression**: Medium (3–5 dB GR)
- **Limiter**: Moderate — preserve transient impact of metallic hits
- **Philosophy**: Impact over loudness — metallic transients need dynamics

### EQ Signature Moves
- Metallic hits: surgical notch at resonant frequencies (ring at specific Hz)
- EBM bass: scoop 200–400 Hz for clarity alongside kick
- Noise: shape with HPF/LPF to fill specific spectral gaps
- Master: accept uneven frequency response — industrial isn't "balanced"
- Drone: HPF at 30 Hz, LPF at 80 Hz — keep sub-bass clean

### Reference Tracks for Mixing
- Perc — "Look What Your Love Has Done to Me" (balanced industrial)
- Blawan — "Why They Hide Their Bodies..." (raw but clear)
- Paula Temple — "Colonized" (powerful industrial mix)

---

## Minimal Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub | Clean, precise |
| 60–150 Hz | Kick body | Moderate (not dominant) |
| 150–500 Hz | Bass hint, micro-sample body | Sparse |
| 500 Hz–2 kHz | Rimshot, micro-samples | Clear, detailed |
| 2–6 kHz | Click transients, rimshot presence | Precise |
| 6–12 kHz | Shaker, hat, micro-details | Delicate |
| 12–20 kHz | Air, subtle shimmer | Light |

### Stereo Field
- **Mono center**: Kick, bass, rimshot
- **Narrow stereo (±15%)**: Micro-percussion, clicks
- **Wide stereo (±40–70%)**: Shaker, atmospheric textures, reverb
- **Overall width**: Moderate — precise center, subtle width
- **Mono compatibility**: Critical (minimal needs to work on any system)

### Dynamics & Loudness
- **Target LUFS (club)**: -9 to -11 LUFS integrated
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 8–12 dB (PRESERVED — groove needs dynamics)
- **Bus compression**: Light (2–3 dB GR), slow attack to preserve transients
- **Limiter**: Gentle (1–2 dB GR max)
- **Philosophy**: Dynamics ARE the groove — DO NOT crush minimal techno

### EQ Signature Moves
- Kick: precise 50–60 Hz boost, 2–4 kHz click boost, surgical cut at any ring
- Rimshot: presence boost at 3–5 kHz, HPF at 400 Hz
- Everything else: surgical HPF/LPF to give each element its own band
- Master: minimal processing — maybe gentle HPF at 25 Hz, nothing more
- LESS IS MORE: fewer EQ moves = better in minimal

### Reference Tracks for Mixing
- Richie Hawtin — "Minus" series (clean, precise, dynamic)
- Ricardo Villalobos — "Enfants" (spacious, groovy, detailed)
- Robert Hood — "Minimal Nation" (the OG reference)

### Common Mix Mistakes
- Over-compression killing groove dynamics
- Too many elements (if you can count more than 5 sounds, reduce)
- Low end too loud (minimal should be balanced, not bass-heavy)
- Reverb too obvious (should be subliminal)
- Over-EQing — minimal sounds shouldn't be hyper-polished

---

## Acid Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub, 303 sub (when filter open) | Strong |
| 60–200 Hz | Kick body, 303 fundamental | Strong |
| 200–800 Hz | 303 resonance region | DOMINANT (filter-dependent) |
| 800 Hz–3 kHz | 303 harmonics, resonant peaks | Very present |
| 3–8 kHz | 303 squelch harmonics, hi-hat | Bright, resonant |
| 8–16 kHz | Hat air, noise artifacts | Present |
| 16–20 kHz | Self-oscillation harmonics | Variable |

### Stereo Field
- **Mono center**: Kick, primary 303 line, bass
- **Narrow stereo**: Clap, secondary 303 (if dual)
- **Wide stereo**: Hi-hats, reverb returns, noise textures
- **Overall width**: Narrow-moderate — acid is punchy and centered
- **303**: ALWAYS mono (hardware is mono, emulations should be too)

### Dynamics & Loudness
- **Target LUFS (club)**: -8 to -10 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 6–9 dB (303 filter sweeps create natural dynamics)
- **Bus compression**: Medium (3–5 dB GR), medium attack
- **Limiter**: Moderate — don't squash the 303's dynamics
- **Philosophy**: The 303's filter IS the dynamics — preserve its movement

### EQ Signature Moves
- 303: DON'T over-EQ — the filter does the work
- 303 mud control: gentle dip at 200–300 Hz when filter fully open
- Kick vs 303: sidechain the 303 to kick (fast, subtle, 3–4 dB)
- Hi-hats: HPF at 8 kHz for classic 909 character
- Master: tame any harsh resonance peaks at 1–3 kHz from 303 resonance

### Reference Tracks for Mixing
- Hardfloor — "Acperience 1" (perfect 303 balance)
- Plastikman — "Spastik" (minimal acid mixing)
- Tin Man — "Acid Test" series (modern acid reference)

---

## Dub Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–50 Hz | Kick sub | Warm, deep |
| 50–120 Hz | Kick body, bass | Warm, full |
| 120–300 Hz | Bass upper harmonics, chord stab lows | Moderate |
| 300 Hz–1.5 kHz | Chord stab body | Warm, present |
| 1.5–4 kHz | Chord stab presence, delay artifacts | Moderate |
| 4–8 kHz | Hat, percussion air | Soft, warm |
| 8–16 kHz | Reverb shimmer, air | Soft, rolled-off |
| 16–20 kHz | Minimal | Rolled off |

### Stereo Field
- **Mono center**: Kick, bass, chord stab dry signal
- **Narrow stereo**: Rimshot, clap
- **Wide stereo**: Delay returns, reverb returns, hi-hats, pads
- **Overall width**: WIDE — dub techno should feel immersive
- **Key**: Reverb/delay returns are the widest elements — creates "space"

### Dynamics & Loudness
- **Target LUFS (club)**: -10 to -12 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 10–14 dB (WIDE — must breathe)
- **Bus compression**: Very light (1–2 dB GR) or none
- **Limiter**: Minimal (0.5–1 dB GR)
- **Philosophy**: SPACE and DEPTH over loudness — dub techno must breathe

### EQ Signature Moves
- Chord stab: HPF at 200 Hz (let kick own the lows)
- Reverb return: LPF at 4–6 kHz (dark, warm reverb — never bright)
- Delay return: HPF 300 Hz + LPF 4 kHz (filtered, lo-fi repeats)
- Kick: gentle presence at 60 Hz, cut at 200 Hz (avoid mud)
- Master: gentle LPF slope above 10 kHz (warm, not bright)

### Reference Tracks for Mixing
- Basic Channel — "Phylyps Trak II" (warm, deep, spacious)
- Deepchord — "Vantage Isle" (lush, immersive)
- Fluxion — "Vibrant" (crystalline clarity)

### Common Mix Mistakes
- Reverb too bright (should be dark, warm — LPF the returns)
- Too loud (dub techno at -7 LUFS loses all depth and space)
- Not enough stereo width (this genre needs immersion)
- Bass too present (should be subtle, warm, not dominant)
- Chord stab too dry (the processing IS the sound)

---

## Detroit Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub, bass fundamental | Warm, round |
| 60–200 Hz | Kick body, bass harmonics | Full, warm |
| 200–500 Hz | Pad low-mids, bass upper harmonics | Warm (not muddy) |
| 500 Hz–2 kHz | Pad body, sequence, strings | Present, soulful |
| 2–5 kHz | Sequence presence, vocal clarity | Clear |
| 5–10 kHz | Hat air, pad shimmer, string harmonics | Smooth |
| 10–20 kHz | Air, cymbal shimmer | Gentle |

### Stereo Field
- **Mono center**: Kick, bass, lead sequence
- **Narrow stereo (±20%)**: Clap, main percussion
- **Wide stereo (±50–80%)**: String pads, reverb returns, chorus effects
- **Overall width**: Wide and immersive — pads fill the space
- **Character**: Warm, enveloping — like being inside the music

### Dynamics & Loudness
- **Target LUFS (club)**: -9 to -11 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 8–12 dB (preserve musical dynamics)
- **Bus compression**: Light-medium (2–4 dB GR), slow attack
- **Limiter**: Gentle (1–3 dB GR)
- **Philosophy**: Musical, warm, dynamic — NOT hyper-compressed

### EQ Signature Moves
- Pads: gentle cut at 200–300 Hz (prevent mud with bass), boost at 2–4 kHz (presence)
- Bass: LPF at 200–300 Hz, gentle boost at 80 Hz for warmth
- 909 drums: minimal EQ — sound is in the character, not processing
- Master: tape saturation/analog warmth on bus (harmonic color)
- Overall: warm spectrum tilt (more lows/low-mids, gently rolled highs)

### Reference Tracks for Mixing
- Derrick May — "Strings of Life" (warm, full, emotional)
- Jeff Mills — "The Bells" (clean, precise, dynamic)
- Carl Craig — "Bug in the Bass Bin" (deep, immersive)

### Common Mix Mistakes
- Too clinical/cold (Detroit should be WARM — add analog character)
- Pads too quiet (they're the soul — they should be present)
- Over-compression killing the soulful dynamics
- Mixing like European techno (too aggressive, too bright)
- Not enough midrange warmth

---

## Hypnotic Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub | Deep, physical |
| 60–150 Hz | Kick body | Strong, present |
| 150–400 Hz | Bass hint, percussion body | Moderate |
| 400 Hz–2 kHz | Percussion loop, rimshot | Balanced |
| 2–5 kHz | Percussion transients | Clear, detailed |
| 5–10 kHz | Hi-hat (if present) | Subtle |
| 10–20 kHz | Air, texture | Minimal |

### Stereo Field
- **Mono center**: Kick, bass, main percussion hit
- **Narrow stereo**: Secondary percussion, rimshot
- **Wide stereo**: Atmospheric texture, delay returns
- **Overall width**: Moderate — not extremely wide or narrow
- **Character**: Focused, deep — width used for subtle depth, not spectacle

### Dynamics & Loudness
- **Target LUFS (club)**: -8 to -10 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 6–9 dB (controlled but alive)
- **Bus compression**: Medium (3–5 dB GR), preserving groove
- **Limiter**: Moderate
- **Philosophy**: Consistent power — not loud, not quiet, just RELENTLESS

### EQ Signature Moves
- Kick: emphasis on 50–60 Hz sub, controlled 100–200 Hz
- Percussion loop: surgical EQ per hit (each sound in its own band)
- Atmospheric elements: aggressive LPF (< 3 kHz) to keep them subliminal
- Master: flat, balanced — no genre needs less master EQ than hypnotic
- Key: DON'T over-EQ — the simplicity is the point

### Reference Tracks for Mixing
- Ben Klock — "Subzero" (deep, physical, relentless)
- Marcel Dettmann — "Seduction" (rolling, balanced)
- Rødhåd — "1984" (dark, focused)

---

## Raw Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub (imperfect) | Present, slightly uncontrolled |
| 60–200 Hz | Kick/bass body | Present |
| 200–800 Hz | Distortion body, noise | Uneven (intentional) |
| 800 Hz–3 kHz | Distortion harmonics | Variable, unpredictable |
| 3–8 kHz | Noise, artifacts | Gritty |
| 8–16 kHz | Noise, aliasing | Lo-fi character |
| 16–20 kHz | Reduced (lo-fi) | Rolled off |

### Stereo Field
- **Mono center**: Kick, bass
- **Variable stereo**: Everything else — placement may be imprecise
- **Overall width**: Variable (sometimes mono, sometimes wide — not controlled)
- **Philosophy**: Stereo image is NOT perfectly crafted — imperfection is OK
- **Mono compatibility**: Check but don't obsess

### Dynamics & Loudness
- **Target LUFS (club)**: -9 to -12 LUFS (NOT hyper-loud)
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 8–14 dB (PRESERVE dynamics, reject loudness war)
- **Bus compression**: Light or none — raw means raw dynamics
- **Limiter**: Minimal (0–2 dB GR)
- **Philosophy**: Anti-loudness-war — dynamics and transients over volume

### EQ Signature Moves
- Minimal EQ — "raw" means not over-processed
- Accept frequency conflicts as character (muddy low-mids can be intentional)
- HPF at 25–30 Hz only (rumble protection)
- Don't brighten — lo-fi means darker spectrum
- Tape saturation on master for cohesive warmth

### Reference Tracks for Mixing
- Blawan — "Getting Me Down" (raw but coherent)
- Shed — "The Killer" (lo-fi energy)
- Skee Mask — "50 Euro to Break Boost" (textural, dynamic)

---

## Schranz

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–50 Hz | Reduced sub (less than peak time) | Controlled |
| 50–150 Hz | Kick body | Present |
| 150–500 Hz | Kick distortion harmonics | Strong |
| 500 Hz–2 kHz | Distortion, metallic percussion | DOMINANT |
| 2–6 kHz | Schranz "crack", distortion upper harmonics | Very present |
| 6–12 kHz | Hi-hat, noise | Harsh |
| 12–20 kHz | Distortion artifacts | Present |

### Stereo Field
- **Mono center**: Kick, primary percussion
- **Narrow stereo**: Additional noise/percussion hits
- **Overall width**: NARROW — schranz is centered, mono-focused
- **Philosophy**: Everything in your face, no spatial tricks
- **Club translation**: Designed for mono PA systems

### Dynamics & Loudness
- **Target LUFS (club)**: -5 to -7 LUFS (INTENTIONALLY LOUD)
- **Target LUFS (streaming)**: -14 LUFS (normalized anyway)
- **Dynamic range**: 3–5 dB (extremely compressed — by design)
- **Bus compression**: Extreme (6–10 dB GR, fast attack)
- **Limiter**: Heavy (4–6 dB GR)
- **Philosophy**: MAXIMUM LOUDNESS — no dynamics, no breathing, relentless

### EQ Signature Moves
- Kick: boost 100–200 Hz for distorted body, boost 2–4 kHz for "crack"
- HPF on kick at 60–80 Hz (less sub than other techno — mid-focused)
- Everything HPF at 100+ Hz except kick (kick owns ALL low end)
- No mud control needed — distortion fills everything intentionally
- Master: accept full-spectrum distortion presence

### Reference Tracks for Mixing
- Chris Liebing — early CLR releases (loud, distorted, relentless)
- Sven Wittekind — "Frankfurt Style" (pure schranz reference)
- DJ Rush — "Motherfucker" (aggressive, loud)

---

## Ghettotech

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | 808 sub bass | Present but short |
| 60–150 Hz | 808/909 kick body | Strong |
| 150–400 Hz | Bass harmonics, vocal body | Present |
| 400 Hz–2 kHz | Vocal chops, synth stabs | DOMINANT |
| 2–5 kHz | Vocal presence, hat body | Very present |
| 5–10 kHz | Hat air, vocal sibilance | Bright |
| 10–20 kHz | Air | Moderate |

### Stereo Field
- **Mono center**: Kick, 808 sub, primary vocal
- **Narrow stereo**: Clap, secondary vocal chops
- **Wide stereo**: Hi-hats, synth stabs, background noise
- **Overall width**: Moderate — vocal and bass centered, hats wide
- **Character**: In-your-face, immediate — not spatial/immersive

### Dynamics & Loudness
- **Target LUFS (club)**: -7 to -9 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 5–8 dB (punchy, energetic)
- **Bus compression**: Medium (3–5 dB GR)
- **Limiter**: Moderate-heavy (2–4 dB GR)
- **Philosophy**: Punchy and loud — party music, needs to hit hard

### EQ Signature Moves
- 808 kick: boost at 60 Hz, cut at 200 Hz (tight, punchy)
- Vocal chops: presence boost at 2–4 kHz, de-ess above 6 kHz
- Hi-hats: HPF at 5 kHz, slight boost at 10 kHz
- Synth stabs: mid-focused (cut lows below 300 Hz, boost 1–3 kHz)
- Master: slight lo-fi character (bit-crush or tape sat for SP-1200 feel)

### Reference Tracks for Mixing
- DJ Assault — "Ass N Titties" (the reference, period)
- DJ Godfather — "Freak-a-Zoid" (balanced ghettotech)
- DJ Funk — "Booty House" (raw, punchy)

---

## Hardgroove

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–60 Hz | Kick sub | Clean, controlled |
| 60–150 Hz | Kick body, bass | Moderate |
| 150–400 Hz | Conga body, tom resonance | Present |
| 400 Hz–2 kHz | Percussion body (djembe, congas) | DOMINANT |
| 2–6 kHz | Percussion transients, slaps | Very present, CLEAN |
| 6–12 kHz | Shaker, bongo air | Bright, clean |
| 12–20 kHz | Air | Clean, open |

### Stereo Field
- **Mono center**: Kick, bass (if present)
- **Narrow stereo (±20%)**: Low conga, clap
- **Wide stereo (±50–90%)**: High congas, bongos, shakers, djembe
- **Overall width**: WIDE — percussion spread across stereo field
- **Character**: Immersive percussion bath — surround-sound energy

### Dynamics & Loudness
- **Target LUFS (club)**: -8 to -10 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 8–11 dB (preserve percussion transients!)
- **Bus compression**: Light (2–3 dB GR) — parallel compression for weight
- **Limiter**: Light (1–2 dB GR) — DO NOT squash transients
- **Philosophy**: TRANSIENTS ARE EVERYTHING — clean, punchy, dynamic percussion

### EQ Signature Moves
- Kick: boost 50–60 Hz, cut 200 Hz (clean, not boomy)
- Congas: each voice EQ'd differently (low=200–400 Hz, high=1–3 kHz)
- Djembe: bass tone boost at 150 Hz, slap boost at 3–4 kHz
- Shakers: HPF at 4 kHz, gentle boost at 8–10 kHz
- Master: CLEAN — no saturation, no coloration, transparency

### Reference Tracks for Mixing
- Ben Sims — "Manipulated" (wide percussion, clean transients)
- Truncate — "Concentrate" (punchy, groovy)
- Steve Bicknell — "Lost" series (tribal power)

### Common Mix Mistakes
- Distortion on percussion (hardgroove must be CLEAN)
- Percussion too compressed (kills transient life)
- Not enough stereo spread (percussion should be immersive)
- Kick too dominant (should be EQUAL with percussion, not above it)
- Missing low percussion body (congas need 200–400 Hz warmth)

---

## Birmingham Techno

### Frequency Spectrum Profile
| Range | Content | Level |
|-------|---------|-------|
| 20–50 Hz | Sub drone (subliminal) | Very low, felt |
| 50–120 Hz | Kick sub, low body | Present, cold |
| 120–300 Hz | Kick upper body | Moderate |
| 300 Hz–1.5 kHz | Metallic percussion body | Present |
| 1.5–4 kHz | Click transients, metallic hits | Precise |
| 4–8 kHz | Very minimal content | Subdued |
| 8–20 kHz | Rolled off | Minimal/absent |

### Stereo Field
- **Mono center**: Kick, sub drone, primary percussion
- **Narrow stereo**: Secondary metallic hits
- **Overall width**: NARROW — claustrophobic, enclosed
- **Character**: Intentionally narrow — creates oppressive feeling
- **Philosophy**: Anti-immersive — Birmingham techno confines, it doesn't expand

### Dynamics & Loudness
- **Target LUFS (club)**: -9 to -11 LUFS
- **Target LUFS (streaming)**: -14 LUFS
- **Dynamic range**: 6–9 dB (controlled, consistent)
- **Bus compression**: Medium (3–4 dB GR), consistent energy
- **Limiter**: Moderate
- **Philosophy**: Consistent, cold, relentless — narrow dynamic band (like the genre itself)

### EQ Signature Moves
- AGGRESSIVE LPF: Everything below 6–8 kHz (NO brightness, NO air)
- Kick: cold character — less sub boost than other techno, more click at 3 kHz
- Metallic hits: surgical resonance notches (tame ring, keep attack)
- Sub drone: HPF at 25 Hz, LPF at 60 Hz (felt only)
- Master: dark overall character — gentle high-shelf CUT above 6 kHz

### Reference Tracks for Mixing
- Surgeon — "La Real" (cold, precise, minimal)
- Regis — "Speak to Me" (dark, industrial, narrow)
- British Murder Boys — "Follow Me" (extreme, claustrophobic)

### Common Mix Mistakes
- Too bright (Birmingham must be DARK — no high-frequency content)
- Too wide (should feel enclosed, claustrophobic)
- Adding warmth (this should be COLD — no tape saturation, no analog warmth)
- Too much sub (sub drone should be subliminal, not dominant)
- Energy dynamics too wide (should be narrow band, consistent)
