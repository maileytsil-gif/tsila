---
titre: "xferrecords com manual serum 2 docs — Using Spectral Synthesis (p. 104-122)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using Spectral Synthesis


<!-- page 104 -->

Serum 2 User Guide
104
Using Spectral Synthesis
Serum features a spectral synthesis mode that generates sound by analyzing and manipulating the
frequency spectrum of a sound, breaking it down into its individual frequency components or partials.
Unlike other synthesis methods that operate directly on the waveform, spectral synthesis focuses on the
harmonic and inharmonic content, allowing for precise control over the timbre and evolution of sound.
By altering specific frequency bands, adding or removing harmonics, or even shifting spectral content
over time, this approach can create complex, evolving textures that can range from natural acoustic-like
tones to entirely synthetic soundscapes. In practical use, spectral synthesis opens up unique possibilities
for morphing and transforming sound in ways that are not achievable with other synthesis techniques.
For instance, by isolating and processing specific frequencies, it is possible to create sounds that
gradually shift from one texture to another, or blend multiple sources into a single, coherent output.
Additionally, spectral synthesis allows for dynamic filtering and precise spectral editing.
Note: This method can be CPU intensive but provides unparalleled flexibility in shaping sound at a
fundamental, spectral level.
Selecting Spectral Synthesis
Using OSC A, OSC B, or OSC C, click the header
and choose Spectral in the context menu.
The oscillator switches to spectral mode.
Spectral in the Oscillator Menu

<!-- page 105 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
105
If you already chose a sample in the Sample or
Granular modes, that sample appears in the
spectral display.
Otherwise, the display is empty.
Click the drop-down menu and choose a sample,
as needed.
In addition to tonal and non-tonal factory presets,
you can load Serum wavetables as samples.
You can also load a sample by choosing Load
Sample in the menu and selecting the file using
the dialog that appears.
Note: After loading a sample, you can use
this menu to show the same location on your
computer or reload the sample.
Spectral Synthesis
Spectral Menu

<!-- page 106 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
106
When a sample loads, the spectral representation
appears in the display.
Click and drag up and down in the frequency
spectrum to zoom the display.
You can tell if the display is fully zoomed out by
hovering over the display and checking whether
you can see both the start and end markers.
Setting the Sample Start and End
You can easily set the sample start and end points
directly.
Hover over the sample and drag either (or both) of
the markers that appear (on the left or right).
Spectral Waveform
Setting Sample Start and End

<!-- page 107 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
107
Setting the Sample High and Low Frequencies
You can set the sample high and low frequency
points directly by dragging the markers to the right
of the spectrogram, as needed.
Right-click in the high-low pane to display the
context menu. You can toggle options on and off
using this menu.
The following table describes the options you can choose:
Option
Description
Smooth
Apply a fourth-order Butterworth filter at the low and high frequency
boundaries, for smoother edges.
Post Warp
Apply the low/high filtering after processing spectral warps.
You can drag and drop any modulation
source (envelopes and LFOs) to the high
and low frequency markers to modulate
the respective control.
Setting Sample Hi and Low
Modulating the Low Frequency

<!-- page 108 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
108
Performing Sample Operations
You can perform a range of operations on the
loaded sample.
Right-click the sample and choose an operation
using the context menu.
Most of the operations available in Spectral mode
are also available in Sample mode. See “Performing
Sample Operations” on page 71 for complete
details about these operations.
Showing the Waveform Display
To toggle the display of the waveform directly
below the spectral display, right-click the sample
and choose Show Waveform Display in the
context menu.
Deselect the option to hide the waveform display.
Spectral Context Menu
Waveform Display

<!-- page 109 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
109
Loop Menu
Use the loop menu to specify the loop mode for
the sample.
Most of the loop options available in Spectral
mode are also available in Sample mode. See
“Loop Menu” on page 77 for more information
about these options.
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
Spectral Loop Menu
Manual Mode

<!-- page 110 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
110
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
You can set a crossfade on a sample loop to
create smoother transitions at the loop points
of the audio sample.
Click the
 button and drag up to set the
crossfade amount. A light blue curve shows
the crossfade graphically.
Setting Loop Start and End
Setting a Loop Cross Fade

<!-- page 111 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
111
Unison
Use the UNISON control to set the number of unison voices, effectively “stacking” oscillators in a way
that is similar to playing multiple notes of the same pitch, but slightly detuned.
Click the field and drag to set the appropriate value. You can also double-click the field and type a value.
This is similar to the unison setting for other oscillator modes.
Note: Unison causes Serum to generate multiple voices, raising CPU usage. The color of the UNISON
field changes as you increase the number of unison voices as a reminder of the CPU consumption.
Click the
 button to display the unison
settings.
You can specify the following settings:
Setting
Description
MODE
The detune mode, from among the following:
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
Spectral Unison Settings

<!-- page 112 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
112
Setting
Description
MODE (cont.)
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
The unison stacking.
DETUNE
The tuning offset for the additional voices.
BLEND
The level offset of the unison voices versus the “central” unison voice or
voices (1 if an odd number, 2 if an even number of unison).
You can think of BLEND as a wet/dry mix between a unison (wet) and non-
unison (dry) sound. The default value of 75% is an even blend between all
the voices.
Note that this is only applicable when the number of unison voices is greater
than two.
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

<!-- page 113 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
113
Setting
Description
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
SPAN
Apply a fixed offset to the starting position for each unison voice.
START
Apply a random offset to the starting position for each unison voice.
This creates subtle timing differences, which can make the sound more lively,
complex, and textured.
WARP 1
Spread out the warp amount applied to each voice around the current
WARP 1 knob position.
WARP 2
Spread out the warp amount applied to each voice around the current
WARP 2 knob position.

<!-- page 114 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
114
Setting the X|Y Control
If you choose to show the X|Y Control using the
context menu, a red dot appears in the spectral
display.
In addition, a new menu option appears in the
context menu allowing you to select the Y axis
parameter.
Use the context menu to
choose the Y axis parameter.
X|Y Control
Y Axis Menu

<!-- page 115 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
115
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
The WARP 2 setting.
Spec Flt Cutoff
The spectral filter cutoff.
Spec Flt Wet/Dry
The spectral filter mix (wet/dry).
Freq Lo
The low frequency (near the bottom right of the spectral display).
Freq Hi
The high frequency (near the top right of the spectral display).
After selecting a Y axis parameter
(other than None), an additional
menu option appears.
This allows you to choose
how to modulate the Y axis
parameter.
Select a modulation option, as
appropriate.
Y Axis Modulation Menu

<!-- page 116 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
116
Setting Spectral Parameters
You can set the sample playback, spectral filter
cutoff, and adjust the waveform warp mode.
You can also adjust the pan and level of the signal.
Scan
Use the SCAN knob to set the speed and direction
of the sample playback.
You can adjust the following parameters related to
the scan setting:
•	 Range — Set the range of the scan knob. The
choices are: +/- 200% (default), +/- 400%,
and +/- 800%.
•	 Reverse — Reverse the scan direction. You
can automate and modulate this control to
switch playback direction.
•	 Key Track — Specify how the scan rate
responds to the pitch of the note played.
With Key Track disabled, the scan rate is fixed
regardless of the key played.
With Key Track enabled, the scan rate
changes in proportion to the pitch of the note
played (higher-pitched notes increase the
scan rate).
•	 Lock Scan Rate (to Tempo) — Change the
scan rate when the tempo changes.
•	 Sample Length to BPM — Set the sample
length based on the BPM set in your host
DAW.
The SCAN knob changes to RATE, allowing
you to set the scan rate using beats and bars.
Spectral Parameters
Spectral Scan Menu

<!-- page 117 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
117
Setting the sample length to BPM allows drum loops or samples to sync with the DAW tempo while still
letting you pitch the sample up and down using the keyboard while keeping the tempo consistent.
You can also control the phase lock and transients.
•	 Phase Lock — Adjust the FFT phases to minimize the audible phase change between FFT blocks
This can result in a less “smeared” sound, more faithful to the original sample. Consider using this
with tonal samples.
•	 Transients — Preserves transients that would otherwise be smeared by FFT processing
Consider using this with percussive sounds or drum loops.
Cut
Use the CUT knob to set the cutoff of the spectral filter.
This sets the cutoff point of the spectral filter, determining which frequencies are allowed to pass
through or are filtered out.
By adjusting the CUT knob, you can control the range of frequencies that shape the sound, effectively
removing unwanted high or low spectral content to refine the tone and texture of the output.
Filter
You can create a custom filter curve, choose a filter preset, or choose a wavetable to act as the filter.
Creating a Custom Curve
Click the FILTER display to show the spectral filter
editor.
Filter Display

<!-- page 118 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
118
The spectral filter editor appears in
a dialog.
Modify the filter by adding new
points and dragging curves.
The following table describes operations you can perform when editing the filter:
Operation
Graph
Description
Double-click
Add a new point to the mask or remove an
existing point.
Spectral Filter Mask Editor
Spectral Filter Mask Editor (Modified)

<!-- page 119 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
119
Operation
Graph
Description
Drag a point
Move a point to a new location.
Drag a curve point
Create or modify a curve between points.
Option/Alt drag a point
Move a point to a new location, constrained
to the current grid.
Option/Alt drag a curve
point
Create or modify curves between all points
simultaneously.
Click and drag to select
Select multiple points. This allows you to drag
multiple points simultaneously.
Click and drag in the GRID field to set the number of grid divisions. To set a specific value, double-click
the field and type the appropriate value.

<!-- page 120 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
120
Choosing a Filter Preset
You can choose a factory filter
preset, click the FILTER display to
show the spectral filter editor.
In the filter editor, click the

button and choose a preset
in the context menu.
After the preset loads, you can
modify the filter curve as needed.
Use the menu to save the preset
for future use.
Alternatively, choose Default in
the menu to return to the draft
filter curve.
Choosing a Wavetable
To use a wavetable as a filter, right-click the
FILTER display and choose a curve in the context
menu.
After choosing a preset, a thumbnail of the filter
shows to indicate your selection.
Important: It’s not possible to edit the filter if you
selected a wavetable.
Filter Presets Menu
Filter Menu

<!-- page 121 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
121
To return to creating a custom filter, right-click
the FILTER display and choose Curve Filter in the
menu.
You can then click the FILTER display, as before, to
display the spectral filter editor.
Mix
Use the MIX knob to control the balance between the wet (processed) and dry (unprocessed) signal.
Setting the Warp Mode
Setting the warp allows you to manipulate the playback/sound of the sample.
By default, warp is set to OFF (as displayed next to the corresponding knob). Clicking the current setting
displays a menu from which you can choose from among the available warp modes.
You can also use the < > arrows to conveniently switch between different warp modes without having
to open the menu. After selecting a mode, you can use the knob to set the depth.
See “Exploring the Warp Modes” on page 49 for detailed information about the available warp
modes.
Pan
Use the PAN knob to control the placement of the sample in the stereo field (left to right).
Level
Use the LEVEL knob to control the output volume of the oscillator.
Filter Selected

<!-- page 122 -->

﻿
Using Spectral Synthesis
Serum 2 User Guide
122
Switching a Sample to a Wavetable
You can quickly and easily create a wavetable from a sample in Serum.
With a sample already
loaded, click the
Spectral menu and
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
page 291 for a detailed
description of each option.
Switch to Wavetable Menu