---
titre: "xferrecords com manual serum 2 docs — Using Granular Synthesis (p. 85-103)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using Granular Synthesis


<!-- page 85 -->

Serum 2 User Guide
85
Using Granular Synthesis
Serum features an easy-to-use granular synthesis mode that manipulates audio samples by breaking
them down into tiny segments called grains, and then recombining them in various ways to create new
textures and sounds. Each grain typically lasts only a few milliseconds and can be individually controlled
in terms of pitch, shape, duration, and playback speed.
By layering, overlapping, and modifying these grains, you can create complex and evolving soundscapes,
offering a high degree of flexibility and experimentation beyond traditional synthesis methods.
One of the key strengths of granular synthesis is its ability to transform audio in real-time, whether
stretching sounds, altering pitch without affecting duration, or creating rich, atmospheric textures from
even the simplest of recordings. Using the granular mode, you can create everything from shimmering,
ethereal pads to glitchy, fragmented effects, offering limitless possibilities for sonic exploration.
Note: Granular synthesis can be CPU intensive, especially when compared to Wavetable, Sample, or
Multisample modes.
Selecting Granular Synthesis
Using OSC A, OSC B, or OSC C, click the header
and choose Granular in the context menu.
The oscillator switches to granular mode.

Granular in the Oscillator Menu

<!-- page 86 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
86
If you already chose a sample in the Sample
or Spectral modes, that sample appears in the
waveform display.
Otherwise, the display is empty.
Click the drop-down menu and choose a sample
from the list of presets.
In addition to tonal and non-tonal factory presets,
you can load Serum wavetables as samples.
You can also load a sample by choosing Load
Sample in the menu and selecting the file using
the dialog that appears.
Note: After loading a sample, you can use
this menu to show the same location on your
computer or reload the sample.
Granular Synthesis
Granular Menu

<!-- page 87 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
87
When a sample loads, the waveform appears in
the display.
Setting the Sample Start and End
You can easily set the sample start and end points
directly.
Hover over the sample and drag either (or both) of
the markers that appear (on the left or right).
Granular Sample Loaded
Setting Sample Start and End

<!-- page 88 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
88
Performing Granular Operations
You can perform a range of operations on the
loaded sample.
Right-click the sample and choose an operation
using the context menu.
Most of the operations available in Granular mode
are also available in Sample mode. See “Performing
Sample Operations” on page 71 for complete
details about these operations.
Granular Operations Menu

<!-- page 89 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
89
Loop Menu
Use the loop menu to specify the loop mode for
the sample.
Most of the loop options available in Granular
mode are also available in Sample mode. See
“Loop Menu” on page 77 for more information
about these options.
Setting Loop Grains
You can select Loop Grains using the Loop menu.
This sets the grain playback to respect loop
markers.
Setting Manual Mode
You can select Manual mode using the loop menu.
When enabled, the playhead is replaced by a red
X|Y dot and the SCAN knob changes to control
the horizontal position of the dot.
When a note is played, the sample does not scan.
Instead, you can freely automate or modulate the
playback position.
You can do this by dragging any mod source to
the X|Y dot to modulate either the position or the
parameter that you assigned to the Y axis (if any).
Note that slicing is not available when Manual is
selected.
Granular Loop Menu
Manual Mode

<!-- page 90 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
90
Setting the Loop Start and End
You can set the loop start and end points either
by dragging markers or by setting values in the LS
(loop start) and LE (loop end) fields.
To drag markers, hover over the top of the sample
display and drag either of the blue markers that
appear, or between them to drag both together.
Alternatively, click and drag in the LS and LE
fields to move the respective markers. To set a
specific value, double-click the field and type the
appropriate value.
You can move the loop start and end markers
while the note is looping to help you find the best
setting.
Use the default modifier (Cmd/Ctrl-click or double-click, depending on GLOBAL setting) between the
markers to reset the loop points to the playback start/end marker positions.
It is not possible to drag the loop markers outside the playback start/end markers.
You can, however, drag, automate, or modulate the markers so that the loop end marker is
before the loop start marker. In this case, the loop direction is reversed.
Setting the Crossfade
You can set a crossfade to individual grain
playback.
Click the
 button and drag up to set the
crossfade amount. A light blue curve shows
the crossfade graphically.
Note that since crossfade is applied to grain
playback, you need to enable Loop Grains in
the loop menu to have this take effect.
Setting Loop Start and End
Setting a Loop Cross Fade

<!-- page 91 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
91
Window Amount
Click the
 button to access the grain amplitude
window settings.
The display changes to show the information you
can set.
Option-click (macOS) or Alt-click
(Windows) and drag the button to
quickly change the window amount
and skew without having to access the
window settings.
The following table describes the settings you can specify:
Setting
Description
AMOUNT
Set the influence of the window curve. You can also set the per-grain
randomization for the amount.
Click the corresponding field and drag to set the appropriate value. You can
also double-click the field and type a value.
SKEW
Set the window skew. You can also set the per-grain randomization for the
skew.
Click the corresponding field and drag to set the appropriate value. You can
also double-click the field and type a value.
SHAPE
Set the grain window shape. A representation of the corresponding shape
appears on the left.
The shape of each grain determines how its volume evolves over time, affecting the attack and decay
characteristics of the sound. By selecting different grain shapes, such as smooth fades or abrupt cuts,
you can dramatically alter the articulation and texture of the sound.
The following table describes the available grain window shapes:
Shape
Description
Hann
Apply a smooth, symmetrical fade-in and fade-out to each grain, using a
cosine-shaped envelope to taper the volume.
This creates a soft, natural sound with gradual attacks and decays, reducing
any harsh transitions between grains for a more cohesive texture.
Grain Amplitude Window Settings

<!-- page 92 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
92
Shape
Description
Welch
Shape each grain using a smooth parabolic curve.
This creates a rounded, more focused sound with a strong central emphasis,
producing a natural yet distinct grain structure.
Gaussian
Shape each grain using a bell curve, where the volume increases to a peak in
the center and then symmetrically decreases.
This results in a smooth, gentle grain with soft transitions, producing a
natural, rounded sound ideal for creating fluid textures.
Blackman-Harris
Apply a windowing function with steep slopes and a smooth central peak,
offering a strong attenuation of the grain’s edges.
This results in grains with a well-defined central focus and minimized
spectral leakage, producing a cleaner, more controlled sound with less
interference between overlapping grains.
Sinc
Shape each grain with a distinctive oscillating pattern that gradually fades
out, resembling the sinc function used in signal processing.
This creates a grain with a sharp, precise center and oscillating tails,
producing a unique texture that can add complexity and harmonic richness
to the sound.
Tukey
Apply a shape that combines characteristics of both a rectangular and a
tapered window, with a flat center portion and smoothly tapered edges.
This allows for flexible control over the grain’s attack and decay, offering a
balance between sharp transitions and gradual fades, making it useful for
adjusting the grain’s prominence and blending.
Triangle
Shape each grain with a linear rise to a central peak followed by a symmetric
linear decay, creating a simple, pointed envelope.
This results in a grain with a clear, sharp attack and a smooth, evenly
tapered release, providing a clean and minimal texture with straightforward
transitions.
Trapezoid
Shape each grain with a gradual linear rise, followed by a flat, sustained
middle section, and then a gradual linear decay.
This creates a grain with a more extended, even body, allowing for a
balanced sound that can blend sharp attacks with sustained tones for
smoother transitions and consistent energy.
ExpDec
Shape each grain with an exponential decay, where the sound starts at full
volume and quickly fades out in a curved, nonlinear fashion.
This creates a grain with a sharp, pronounced attack followed by a rapid,
smooth decay, useful for producing sharp, percussive textures or gradually
fading sound effects.

<!-- page 93 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
93
Shape
Description
Exp Dec Rev
Shape each grain with a reversed exponential decay, where the grain starts
at a low volume and rapidly rises to full volume in a curved, nonlinear
fashion.
This creates a grain with a smooth, swelling attack followed by a sharp peak,
ideal for building tension or creating atmospheric effects with a gradual
onset.
Unison
Use the UNISON control to set the number of unison voices, effectively “stacking” granular oscillators in
a way that is similar to playing multiple notes of the same pitch, but slightly detuned.
Click the field and drag to set the appropriate value. You can also double-click the field and type a value.
This is similar to the unison setting for other oscillator modes.
Note: Unison causes Serum to generate multiple voices, raising CPU usage. The color of the UNISON
field changes as you increase the number of unison voices as a reminder of the CPU consumption.
Click the
 button to display the unison
settings.
You can specify the following settings:
Granular Unison Settings

<!-- page 94 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
94
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
DETUNE
Specify the tuning offset for the additional voices.
BLEND
Specify the level offset of the unison voices versus the “central” unison voice
or voices (1 if an odd number, 2 if an even number of unison).
You can think of BLEND as a wet/dry mix between a unison (wet) and non-
unison (dry) sound. The default value of 75% is an even blend between all
the voices.
Note that this is only applicable when the number of unison voices is greater
than two.

<!-- page 95 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
95
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
START
Apply a random offset to the starting position for each unison voice.
This creates subtle timing differences, which can make the sound more lively,
complex, and textured.
SPAN
Apply a fixed offset to the starting position for each unison voice.
SPAWN PATTERN
The timing offset at which unison grain voices are spawned.
With Together (default), all unison grain voices spawn at the same time.
With the other options, the spawning of unison grain voices are offset into
the period before the next spawn, as follows:
•	 Even — The timing of unison grain voices is spread out evenly
•	 Exp — The timing between unison grain voices increases over the
period before the next spawn
•	 Random — The timing between unison grain voices is randomly
distributed over the period before the next spawn

<!-- page 96 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
96
Setting the X|Y Control
If you choose to show the X|Y Control using the
context menu, a red dot appears in the display.
In addition, a new menu option appears in the
context menu allowing you to select the Y axis
parameter.
Use the context menu to
choose the Y axis parameter.
X|Y Control
Y Axis Menu

<!-- page 97 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
97
The following table describes the available Y axis options:
Option
Description
None
No Y axis target.
Level
The oscillator level.
Warp
The WARP 1 setting.
Warp 2
The WARP B setting.
Density
The density of the grain cloud.
Grain Length
The duration of each grain.
Window Amt
The window amount for the sample. Sets the influence of the window curve.
Window Skew
The window skew.
Rand Offset
The per-grain randomization of the offset.
Rand Dir
The per-grain randomization of the direction.
Rand Pitch
The per-grain pitch randomization.
Rand Length
The per-grain length randomization.
Rand Pan
The per-grain randomization of the pan setting.
Rand Gain
The per-grain level randomization.
Rand Window
The window amount randomization.
Rand Skew
The window skew randomization.
Rand Warp
The WARP A randomization.
Rand Warp 2
The WARP B randomization.

<!-- page 98 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
98
After selecting a Y axis
parameter (other than None),
an additional menu option
appears.
This allows you to choose
how to modulate the Y axis
parameter.
Select a modulation option,
as appropriate.
Setting Granular Parameters
You can set the scan rate, density, and length,
as well as adjust the warp mode, among other
settings.
You can also adjust the pan and level of the signal.
Y Axis Modulation Menu
Granular Parameters

<!-- page 99 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
99
Warp Mode
Setting the warp allows you to manipulate the
playback/sound of the sample.
Click the
 button to display the warp settings.
Click the
 button to hide the settings.
By default, warp is set to OFF (as displayed next
to the corresponding knob). Clicking the current
setting displays a menu from which you can
choose from among the available warp modes.
You can also use the < > arrows to conveniently switch between different warp modes without having
to open the menu. After selecting a mode, you can use the knob to set the depth.
See “Exploring the Warp Modes” on page 49 for detailed information about the available warp
modes.
Scan
Use the SCAN knob to set the scan rate. The scan rate controls how quickly the Serum moves through
the audio sample to generate grains.
Granular synthesis involves breaking an audio sample into tiny pieces called grains (usually lasting a few
milliseconds) and then recombining them to create new sounds. Serum determines the playback start
position of a grain by the current playhead position.
The scan rate specifies how quickly the playhead moves through the sample. Setting the scan rate
higher spreads the start positions of grains out along the sample more, resulting in less overlap between
grains.
Setting the scan rate lower causes movement through the sample to slow down. This can produce a
more stretched, evolving, or drone-like sound.
In summary, a higher scan rate can be used to maintain rhythmic accuracy or to create fast-paced,
glitch-like effects. A slower scan rate allows for dramatic time-stretching effects, creating elongated and
ambient textures.
Setting the scan rate to a negative value reverses the direction of the playhead. Alternatively,
setting the scan rate to 0 stops the playhead from moving.
Granular Warp Settings

<!-- page 100 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
100
You can adjust the following parameters
related to the scan setting:
•	 Range — Set the range of the scan knob.
The choices are: +/- 200% (default), +/-
400%, and +/- 800%.
•	 Reverse — Reverse the scan direction.
You can automate and modulate this
control to switch playback direction.
•	 Key Track — Specify how the scan
rate responds to the pitch of the note
played.
With Key Track disabled, the scan rate is
fixed regardless of the key played.
With Key Track enabled, the scan rate
changes in proportion to the pitch of
the note played (higher-pitched notes
increase the scan rate).
•	 Lock Scan Rate (to Tempo) — Change
the scan rate when the tempo changes.
•	 Sample Length to BPM — Set the
sample length based on the BPM set in
your host DAW.
The SCAN knob changes to RATE,
allowing you to set the scan rate using
beats and bars.
Granular Scan Menu

<!-- page 101 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
101
Density
Use the DENS knob to set the density of the grain cloud.
Density defines the rate at which grains are spawned, according to one of three options that you can
specify by right-clicking the knob and choosing from the context menu. The options are:
•	 Free — Grains are spawned at a rate defined in Hz
•	 BPM Sync — Grains are spawned at a bar/beat division of host tempo
When selected, the context menu offers Triplet and Dotted as additional options, allowing you to
specify whether triplet or dotted divisions can be selected with the knob.
•	 Grains — The spawn rate is calculated as a function of grain length such that a consistent number
of grains, as set by the control, is playing at any given time
You can additionally specify two more options using the DENSITY knob context menu.
•	 Jump Start — Enable this option to have multiple grains spawn at note start so that the full density
is heard immediately.
When disabled, there is only a single spawning at note start and the sound builds to full density
over subsequent spawnings, giving the note a softer start.
•	 Max Grains — Set to place a limit on the maximum number of grains that can play at any one time,
including unison grain voices.
Many grains playing simultaneously can consume a lot of CPU. Use this option to help reduce this
consumption. If the oscillator tries to spawn a grain when the maximum number is playing, it will
skip and wait until one has stopped playing before it spawns again.
Length
Use the LENGTH knob to set the duration of each grain.
Setting the duration of each grain allows you to control how long each sound fragment lasts, influencing
the overall character of the resulting texture. Shorter grains can produce sharper, more rhythmic sounds,
while longer grains create smoother, more sustained tones.

<!-- page 102 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
102
You can specify how the length is determined by right-clicking the LENGTH knob and choosing one of
three options from the context menu:
•	 Free — Gain length can be set in seconds or milliseconds
•	 BPM Sync — Grain length can be set to a bar/beat division of host tempo
When selected, the context menu offers Triplet and Dotted as additional options, allowing you to
specify whether triplet or dotted divisions can be selected with the knob.
•	 Percent — Grain length is set to a percent of the density period. Note that this option is not
available if you select the Grains option with the DENSITY knob.
Pan
Use the PAN knob to control the placement of the sample in the stereo field (left to right).
Level
Use the LEVEL knob to control the output volume of the oscillator.
Setting the Grain Randomization
You can set the grain randomization parameters by
adjusting the lower row of knobs.
The following table describes the available knobs:
Knob
Description
OFFSET
Set the per-grain randomization of the offset.
DIR
Set the per-grain randomization of the direction.
PITCH
Set the per-grain pitch randomization.
RAND (LENGTH)
Set the per-grain length randomization.
RAND (PAN)
Set the per-grain randomization of the pan setting.
RAND (LEVEL)
Set the per-grain level randomization.
Grain Randomization

<!-- page 103 -->

﻿
Using Granular Synthesis
Serum 2 User Guide
103
Reversing the Grain Playback Direction Randomization
You can reverse grains as part of the per-grain
direction randomization.
Right-click the DIR knob and choose Reverse
Grains in the context menu to toggle the reverse
grains feature on or off.
You can automate and modulate this setting to
switch playback direction of all grains at once.
Switching a Sample to a Wavetable
You can quickly and easily create a wavetable from a sample in Serum.
With a sample already
loaded, click the
Granular menu and
hover over Switch to
Wavetable in the menu.
The menu of import
options appears. These
are the same options
that appear when
you import audio as a
wavetable in other areas
of Serum.
Choose one of the
menu options.
The oscillator switches
to Wavetable mode
with the converted
wavetable loaded.
See “Importing Multi-
Cycle Waveforms” on
page 291 for a detailed description of each option.
Grain Randomization
Switch to Wavetable Menu