---
titre: "xferrecords com manual serum 2 docs — Using Multisample Instruments (p. 58-67)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using Multisample Instruments


<!-- page 58 -->

Serum 2 User Guide
58
Using Multisample Instruments
Serum features the ability to set any of the oscillators to function as a multisample instrument that
utilizes an array of samples—recordings of an actual instrument—played across a range of pitches,
intensities, and articulations.
With a multisample instrument, individual notes are recorded at different velocities (soft to loud) and
sometimes with various playing techniques, such as plucking, bowing, or using different mallets.
When using a multisample instrument, Serum accurately selects the appropriate sample based on the
MIDI input—evaluating both the pitch and velocity of the note—ensuring that the output sound mimics
the real instrument’s response as closely as possible. For example, playing softly might trigger a sample
of a gently played note, while pressing hard would trigger a sample of the same note played with force.
Layering multiple distinct samples achieves the effect of rich, lifelike audio textures that respond
accurately to different playing styles. This can capture the nuanced tonal variations and expressive
characteristics of the original instrument, allowing for a highly realistic and responsive musical
experience.
Selecting a Multisample Instrument
Using OSC A, OSC B, or OSC C, click the header
and choose Multisample in the menu that
appears.
Multisample in the Oscillator Menu

<!-- page 59 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
59
The oscillator switches to multisample mode.
Initially, the waveform display is empty since no
instrument has been loaded.
Click the drop-down menu and choose a
multisample instrument.
You can also load a multisample instrument using
a .sfz file. Using the menu, choose Load SFZ and
select the file using the dialog that appears.
SFZ files are text-based files that describe how
audio samples (such as WAV files) should be
played by a sampler.
The files map audio samples to specific notes,
velocities, or other MIDI parameters. SFZ files can
also include instructions for dynamic layers, key
switches, round robins, and other articulations.
Furthermore, Serum supports SFZ envelope
parameters to help shape the sound.
Serum does not natively support
SoundFont 2 (SF2) files. There are,
however, multiple open source
applications that can convert files from
SF2 to SFZ file formats.
Multisample Instrument
Multisample Instrument Menu

<!-- page 60 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
60
After loading an instrument, the display shows the
multisamples that comprise the instrument.
Playing a note highlights the specific sample,
representing the corresponding pitch and velocity.
Clicking in the display displays the waveform of
the last note played.
Multisample Instrument Loaded
Multisample Instrument (Note Played)

<!-- page 61 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
61
Setting the Multisample Envelope
You can modify the envelope by clicking the
 button. The envelope pane appears, initially disabled.
SFZ files contain envelope information for
playback. This can be per note, per group, or
global.
Click the OVERRIDE button to activate the
envelope display and override the envelope
configuration from the SFZ file.
Use the knobs to adjust the envelope shape.
The following table describes the available controls:
Knob
Description
DELAY
The time (in milliseconds) before the envelope begins after a note is
triggered, allowing you to introduce a pause before the attack phase starts.
This is useful for creating rhythmic effects or gradual sound layering, giving
more control over how and when the envelope affects the sound.
Right-click the DELAY knob and choose BPM Sync in the context menu to
synchronize the delay with the musical tempo. When selected, you can set
the delay in beats and bars.
A (Attack)
The time it takes for the sound to reach its maximum level after a note is
triggered. This shapes the initial onset of the sound, allowing for smooth
fades or sharp, immediate beginnings depending on the setting.
H (Hold)
The amount of time the sound remains at its peak level after the attack
phase is completed.
This allows the sound to sustain momentarily before moving into the decay
phase, adding emphasis and length to the peak of the sound.
D (Decay)
The time it takes for the sound to transition from its maximum level after the
attack phase to the sustain level.
This shapes the gradual reduction in volume, allowing you to create more
natural fades or sharp drops in sound intensity depending on the setting.
Multisample Envelope Pane

<!-- page 62 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
62
Knob
Description
S (Sustain)
The steady level the sound maintains after the decay phase, as long as the
note is held.
Unlike other stages, the sustain level lasts indefinitely until the note
is released, allowing for either continuous sound or a softer presence
depending on the setting.
R (Release)
The time it takes for the sound to fade out after the note is released.
This shapes the tail of the sound, allowing for smooth, gradual decays or
quick cutoffs depending on the chosen release time.
You can also adjust the envelope by clicking and dragging each point directly on the graph. The cursor
changes to indicate whether the point can be moved horizontally or freely in all directions, providing
visual feedback for precise control.
Velocity Track
Use the VEL TRACK control to adjust the sensitivity of the note velocity. After enabling velocity
tracking, click and drag in the field to modify the setting.
Random
Use the RAND control to randomize the initial phase of the sample. This is similar to the random setting
for other oscillator modes. Click and drag in the field to modify the value.
Setting Multisample Parameters
You can set the timbre, unison (including detune
and blend), and adjust the waveform warp for the
multisample instrument.
You can also adjust the pan and level of the signal.
Multisample Parameters

<!-- page 63 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
63
Timbre
Use the TIMBRE knob to adjust the multisample timbre.
For multisamples with zone mapping, this control inversely adjusts mapped samples to pitch. This alters
how the samples respond to changes in pitch across different key zones.
Normally, as you play higher notes, the pitch of the sample increases, and as you play lower notes, it
decreases. When you inversely adjust the mapped samples to pitch, the opposite happens: higher notes
trigger samples that are mapped to lower pitches, and lower notes trigger samples mapped to higher
pitches.
This creates an unusual or experimental timbral effect, as the relationship between pitch and sample
playback is reversed, potentially adding unique tonal qualities to the sound.
Unison
Use the UNISON control to set the number of unison voices, effectively “stacking” oscillators in a way
that is similar to playing multiple notes of the same pitch, but slightly detuned.
Click the field and drag to set the appropriate value. You can also double-click the field and type a value.
This is similar to the unison setting for other oscillator modes.
Note: Unison causes Serum to generate multiple
voices, raising CPU usage. The color of the
UNISON field changes as you increase the
number of unison voices as a reminder of the CPU
consumption.
Click the
 button to display the unison
settings.
Multisample Unison Settings

<!-- page 64 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
64
You can specify the following settings:
Setting
Description
MODE
Set the detune mode, from among the following:
•	 Linear — The detuning between each additional voice increases in a
consistent, linear fashion. This means that the pitch of each voice is
spaced evenly in terms of frequency, creating a smooth spread that
retains an even distribution.
This mode can sound very controlled and smooth, giving a thick and
coherent texture.
•	 Super — Multiple voices are slightly detuned from each other but with a
special emphasis on creating a dense and powerful sound, often with a
slight stereo spread.
Use this mode to create a lush, wide sound, especially with supersaw
sounds, where the detuned voices give a rich, full sonic character.
•	 Exp — The detuning between voices increases exponentially as
you move away from the central pitch. This means that the spacing
between voices gets wider more quickly as you move outward, creating
a more dramatic spread compared to linear.
This mode can create unique, rich textures, especially for sounds that
need to be more aggressive or have a strong presence in a mix.
•	 Inv — The detuning behavior is inverted, with lower voices detuned
more sharply compared to higher ones.
Use this mode to create interesting phasing effects or to produce
sounds with a less conventional detuning profile.
•	 Random — Introduces a random element to the detuning of each voice.
Instead of being evenly spaced, the voices are detuned unpredictably.
This can create a more organic or chaotic sound, ideal for achieving
textures that are less polished and more natural or experimental.
STACK
Set the unison stacking.

<!-- page 65 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
65
Setting
Description
WIDTH
The extent to which the unison voices are spread out across the stereo field,
determining how wide or narrow the resulting sound feels in a stereo mix.
When you increase the width parameter, the unison voices are spread
farther apart in the stereo spectrum, placing some voices more to the left
and others more to the right. This creates a sense of space and a wider,
more immersive sound.
Conversely, decreasing the width narrows the stereo spread, making the
sound more centered and focused. This can be useful for sounds that need
to be more direct or fit better in a dense mix without dominating the stereo
field.
RANGE
The extent or range of detuning applied to the unison voices, determining
how far apart in pitch the individual voices are spread around the central
frequency of the original sound.
When the range is set to a low value, the detuning between the unison
voices is minimal. The voices remain relatively close in pitch to the original
frequency, creating a subtle and smooth chorusing effect. This can add
warmth and a slight thickness to the sound without drastically changing its
character.
When the range is increased, the detuning becomes more pronounced,
and the unison voices are spread further apart in pitch. This creates a more
dramatic and sometimes more chaotic or dissonant effect, which can be
useful for creating lush, wide textures or aggressive, detuned leads.
WARP 1
Spread out the warp amount applied to each voice around the current
WARP 1 knob position.
WARP 2
Spread out the warp amount applied to each voice around the current
WARP 2 knob position.
You can further adjust the unison setting using the DETUNE and BLEND knobs.

<!-- page 66 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
66
Unison Detune
Use the DETUNE knob to specify the tuning offset +/- for the additional voices. This is only applicable
when unison is enabled (set to a value above 1).
Unison Blend
Use the BLEND knob to specify the level offset of the unison voices versus the “central” unison voice or
voices (1 if an odd number, 2 if an even number of unison).
You can think of BLEND as a wet/dry mix between a unison (wet) and non-unison (dry) sound. The
default value of 75% is an even blend between all the voices. Note that this is only applicable when the
number of unison voices is greater than two.
Warp
Setting the warp allows you to manipulate the playback/sound of the wavetable oscillator.
By default, warp is set to OFF (as displayed next to the corresponding knob). Clicking the current setting
displays a menu from which you can choose from among the available warp modes.
You can also use the < > arrows to conveniently switch between different warp modes without having
to open the menu. After selecting a mode, you can use the knob to set the depth.
See “Exploring the Warp Modes” on page 49 for detailed information about the available warp
modes.
Pan
Use the PAN knob to control the placement of the waveform in the stereo field (left to right).
Level
Use the LEVEL knob to control the output volume of the oscillator.

<!-- page 67 -->

﻿
Using Multisample Instruments
Serum 2 User Guide
67
Switching the Last Note Played to a Sample
You can quickly switch the last multisample note
that you played to a single sample. You might do
this if you like a single sound but don’t need the
entire multisample.
Then later, if needed, you can also just as easily
create a wavetable from that sample.
Begin by loading a multisample into an oscillator.
After playing a note, click the Multisample menu
and choose Switch to Single Sample in the menu.
The oscillator switches to Sample mode with the
last-played note loaded as the sample.
To convert the sample to a wavetable, click
the Sample menu and hover over Switch to
Wavetable in the menu.

The menu of import options
appear. These are the same
options that appear when
you import audio as a
wavetable in other areas of
Serum.
Choose one of the menu
options.
The oscillator switches to
Wavetable mode with the
converted wavetable loaded.
See “Importing Multi-Cycle
Waveforms” on page 291
for a detailed description of
each option.
Multisample Instrument (Note Played)
Switch to Wavetable Menu