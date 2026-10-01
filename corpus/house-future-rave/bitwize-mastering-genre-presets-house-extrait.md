---
titre: "bitwize claude-ai-music-skills — mastering-engineer/genre-presets.md, extrait : cibles LUFS, dynamique et EQ pour EDM, tech house, deep house, progressive, future house, bass house, rave, vocal house, afro house"
source: https://raw.githubusercontent.com/bitwize-music-studio/claude-ai-music-skills/main/skills/mastering-engineer/genre-presets.md
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: genres et éléments constitutifs (house, bass house, future rave)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR-lu] (notes non sourcées, dépôt GitHub) : chiffres à recouper avant usage.

# Extrait : presets de mastering par genre (skill mastering-engineer) — sections house / EDM

### Electronic / EDM
**LUFS target**: -10 to -12 LUFS (can go louder)
**Dynamics**: Heavy compression, consistent energy
**EQ focus**: Sub-bass (30-50 Hz), sparkle on top (10+ kHz)
**MCP command**: `master_audio(album_slug, genre="edm")`

**Characteristics**:
- Massive bass
- Sustained energy
- Bright, polished highs


### Tech House
**LUFS target**: -14 LUFS
**Dynamics**: Moderate compression; preserve the rolling groove and percussive dynamics that define the genre; over-compression flattens the subtle interplay between kick, bass, and layered percussion that makes tech house work on the dancefloor
**EQ focus**: Kick punch and definition (50-80 Hz), rolling bassline presence (80-200 Hz), percussion clarity (2-5 kHz), gentle high-mid cut to tame crisp hi-hat brightness without losing groove detail (3-5 kHz)
**MCP command**: `master_audio(album_slug, genre="tech-house")`

**Characteristics**:
- The 909-style kick drum must be tight, punchy, and well-defined at 50-80 Hz; it drives the entire track and must cut through sub-bass content cleanly
- Rolling basslines (often mid-range, 80-200 Hz) are the harmonic backbone; keep them warm and defined without muddying the kick drum
- Layered percussion (congas, shakers, rim shots, claps) creates the polyrhythmic groove; preserve transient clarity in the 2-5 kHz range
- Sidechain compression pumping between kick and bass is intentional and defines the genre's rhythmic feel; preserve the breathing effect
- Vocal chops and spoken samples are rhythmic elements, not melodic features; they should sit inside the mix, not on top of it
- Sub-bass content should be controlled and tight, not boomy; tech house favors mid-bass punch over deep sub-bass weight
- Minimal tech house variants: slightly wider dynamics, more space in the mix; bass-heavy festival variants: tighter compression, stronger low end acceptable
- Extended DJ intros and outros should maintain consistent level with the body of the track


### Tech House
**LUFS target**: -14 LUFS
**Dynamics**: Moderate compression; preserve the rolling groove and percussive dynamics that define the genre; over-compression flattens the subtle interplay between kick, bass, and layered percussion that makes tech house work on the dancefloor
**EQ focus**: Kick punch and definition (50-80 Hz), rolling bassline presence (80-200 Hz), percussion clarity (2-5 kHz), gentle high-mid cut to tame crisp hi-hat brightness without losing groove detail (3-5 kHz)
**MCP command**: `master_audio(album_slug, genre="tech-house")`

**Characteristics**:
- The 909-style kick drum must be tight, punchy, and well-defined at 50-80 Hz; it drives the entire track and must cut through sub-bass content cleanly
- Rolling basslines (often mid-range, 80-200 Hz) are the harmonic backbone; keep them warm and defined without muddying the kick drum
- Layered percussion (congas, shakers, rim shots, claps) creates the polyrhythmic groove; preserve transient clarity in the 2-5 kHz range
- Sidechain compression pumping between kick and bass is intentional and defines the genre's rhythmic feel; preserve the breathing effect
- Vocal chops and spoken samples are rhythmic elements, not melodic features; they should sit inside the mix, not on top of it
- Sub-bass content should be controlled and tight, not boomy; tech house favors mid-bass punch over deep sub-bass weight
- Minimal tech house variants: slightly wider dynamics, more space in the mix; bass-heavy festival variants: tighter compression, stronger low end acceptable
- Extended DJ intros and outros should maintain consistent level with the body of the track


### Deep House
**LUFS target**: -14 LUFS
**Dynamics**: Light-to-moderate compression; preserve the warm, open groove and subtle dynamic shifts; deep house lives in its spaciousness -- over-compression kills the late-night intimacy and hypnotic feel
**EQ focus**: Sub-bass warmth (40-80 Hz), Rhodes/keys presence (200-500 Hz), vocal sample clarity (2-4 kHz), gentle high-mid cut at 3.5 kHz to tame hi-hat harshness, airy top-end for reverb tails (10+ kHz)
**MCP command**: `master_audio(album_slug, genre="deep-house")`

**Characteristics**:
- Sub-bass should be warm and round, not aggressive or punchy -- deep house bass is felt more than heard, sitting lower than tech house or mainroom house
- Kick drum has a softer attack than peak-time house; preserve the pillowy, warm character rather than pushing for maximum transient impact
- Rhodes, Wurlitzer, and jazz guitar samples sit in the 200-500 Hz range; keep them warm and defined without muddiness
- Reverb and delay are integral to the spatial atmosphere -- mastering should preserve the depth and width of the mix; avoid limiting that flattens the stereo image
- Soulful vocal samples and spoken word elements need warmth and intimacy at 2-4 kHz; avoid harshness that breaks the dreamy quality
- Shuffled hi-hats and subtle percussion (shakers, rim clicks) at 8-12 kHz drive the groove; preserve their crisp detail without brightness fatigue over long listening sessions
- Afro deep house variants may have more percussive energy; organic house variants should be treated even more gently with wider dynamics


### Progressive House
**LUFS target**: -14 LUFS (deep progressive: -15 LUFS)
**Dynamics**: Light-to-moderate compression; preserve the gradual builds and extended dynamic arcs that define the genre; progressive house lives in the tension between quiet breakdowns and euphoric peaks -- over-compression destroys this emotional architecture
**EQ focus**: Pad warmth and body (200-600 Hz), synth lead clarity (1-4 kHz), sub-bass definition (40-80 Hz), gentle high-mid cut to tame bright synth harmonics without losing shimmer (3-5 kHz)
**MCP command**: `master_audio(album_slug, genre="progressive-house")`

**Characteristics**:
- Extended builds (32-64 bars) rely on gradual dynamic increase -- over-limiting flattens the arc and removes the emotional payoff at the climax
- Layered pads and atmospheric textures occupy the mid-range (200 Hz-2 kHz); preserve their warmth and spatial depth without muddiness
- Four-on-the-floor kick must remain consistent and punchy (60-80 Hz) but not dominate; it anchors the groove while melodies carry the emotion
- Reverb tails, delay trails, and filtered sweeps are compositional elements -- over-compression collapses the spatial depth that defines the genre
- Deep progressive (Guy J, Hernan Cattaneo style): target -15 LUFS, wider dynamics, more spacious and hypnotic; minimal compression to preserve subtle textural shifts
- Big room progressive (festival variant): can push to -14 LUFS with tighter compression; punchier kick, brighter leads, less subtlety acceptable
- Sidechain compression pumping on pads is intentional and genre-defining; preserve the rhythmic breathing effect
- Melodic progressive (Eric Prydz, deadmau5 style): synth leads in the 1-4 kHz range need clarity and emotional presence without harshness


### Future House
**LUFS target**: -14 LUFS
**Dynamics**: Moderate compression; preserve the sidechain pumping effect and dynamic contrast between breakdowns and drops; the genre's groove depends on the rhythmic push-pull between kick and bass
**EQ focus**: FM bass clarity and body (80-300 Hz), vocal chop presence (2-6 kHz), kick definition (40-80 Hz), hi-hat crispness (8-12 kHz), synth pluck brightness (1-4 kHz)
**MCP command**: `master_audio(album_slug, genre="future-house")`

**Characteristics**:
- The FM/frequency-modulated bassline is the genre's signature sound -- metallic, elastic, and rubbery; preserve its tonal character and movement without muddiness
- Sidechain compression pumping is a compositional element, not a mixing artifact; the rhythmic ducking of the bass against the kick must remain pronounced and groovy
- Pitched vocal chops function as melodic hooks; they need clarity and presence in the 2-6 kHz range without harshness
- Oliver Heldens-style: brighter, poppier, more melodic; Tchami-style: darker, funkier, heavier bass
- Builds and drops define the energy arc; preserve the contrast between stripped breakdowns and full drops
- Clean, polished production is expected; the genre rewards a precise, modern-sounding master over warmth or analog character


### Bass House
**LUFS target**: -14 LUFS
**Dynamics**: Moderate-to-heavy compression; sustain the energy and impact of the bass drop while preserving the four-on-the-floor groove; the distorted bass must feel heavy and physical without losing definition against the kick drum
**EQ focus**: Sub-bass weight (30-60 Hz), distorted mid-bass presence and definition (80-400 Hz), kick drum punch (60-100 Hz), hi-hat and percussion crispness (8-12 kHz), gentle high-mid cut to tame synth harshness in the bass design (3-5 kHz)
**MCP command**: `master_audio(album_slug, genre="bass-house")`

**Characteristics**:
- The distorted bassline is the genre's centerpiece -- it must be heavy, present, and felt physically; preserve the saturation and harmonic content that gives bass house its gritty character
- Kick and bass must coexist cleanly despite occupying overlapping frequency ranges; tight sidechain compression between kick and bass is essential to maintain the pumping groove
- Sub-bass (30-60 Hz) provides the foundation beneath the distorted mid-bass (80-400 Hz); careful layering separation prevents mud without thinning the combined impact
- Vocal chops and samples are production elements, not lead vocals; keep them punchy and defined but not competing with the bass for attention
- Festival-ready variants (Jauz, Habstrakt style): can push slightly louder, more aggressive limiting; underground/Night Bass style: slightly more dynamic, groove-focused
- Builds and breakdowns create tension-release arcs; preserve the contrast between stripped-back sections and full bass drops
- Hi-hats and percussion should remain crisp and swung; over-compression flattens the groove feel that distinguishes bass house from straight EDM


### Rave
**LUFS target**: -12 LUFS
**Dynamics**: Heavy compression; aggressive, high-energy production designed for massive sound systems; the genre demands loudness and physical impact
**EQ focus**: Kick punch (40-80 Hz), synth stab energy (1-4 kHz), vocal/MC sample presence (2-5 kHz), hi-hat and breakbeat energy (6-12 kHz), sub-bass weight (30-60 Hz)
**MCP command**: `master_audio(file, genre="rave")`

**Characteristics**:
- Breakbeats, piano stabs, and vocal samples define the classic rave sound; all need energy and presence
- Bass must be heavy and physically felt; massive sub-bass for large sound systems
- The Prodigy/SL2-style: aggressive, breakbeat-driven; piano house rave: euphoric, more melodic
- Hoover synths and rave stabs are signature sounds; preserve their aggressive, cutting quality
- The genre expects maximum energy and loudness; push to -12 LUFS or louder
- Dynamic restraint is not the goal; controlled aggression with clear transients


### Vocal House
**LUFS target**: -14 LUFS
**Dynamics**: Moderate compression; preserve the vocal performance dynamics alongside the four-on-the-floor groove; vocals are the genre's emotional center
**EQ focus**: Vocal clarity and warmth (2-5 kHz), kick punch (40-80 Hz), bass groove (60-150 Hz), pad warmth (200-500 Hz), hi-hat crispness (8-12 kHz)
**MCP command**: `master_audio(file, genre="vocal-house")`

**Characteristics**:
- Diva vocals are the genre's centerpiece; powerful, clear, and emotionally delivered
- Four-on-the-floor kick must be punchy and driving; the dance-floor foundation
- Bass is warm and groovy; supports the vocal without competing
- Synth pads and strings add emotional depth; lush but behind the vocal
- Classic vocal house (Frankie Knuckles, Larry Levan): warmer, more soulful; modern: cleaner, more produced
- The genre demands a polished master that serves the vocal while maintaining dancefloor energy


### Afro-House
**LUFS target**: -14 LUFS
**Dynamics**: Moderate compression; preserve the organic percussion layers and deep groove; the genre blends African rhythmic traditions with house music structure
**EQ focus**: Percussion clarity (3-8 kHz), bass warmth (60-150 Hz), vocal chant presence (2-5 kHz), synth pad warmth (200-500 Hz), kick definition (40-80 Hz)
**MCP command**: `master_audio(file, genre="afro-house")`

**Characteristics**:
- Layered African percussion creates polyrhythmic complexity; preserve transient clarity and rhythmic interplay
- Bass is warm and groovy; supports the dance groove without overwhelming the percussion
- Black Coffee/Culoe De Song-style: deeper, more minimal; festival Afro-house: more energetic, bigger builds
- Vocal chants and melodic elements add African musical identity; keep them prominent and warm
- The genre's organic feel sets it apart from mainstream house; do not over-process
- A warm, spacious master preserves the genre's cultural and rhythmic richness
