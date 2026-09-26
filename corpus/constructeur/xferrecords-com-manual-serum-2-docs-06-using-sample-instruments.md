---
titre: "xferrecords com manual serum 2 docs — Using Sample Instruments (p. 68-84)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using Sample Instruments


<!-- page 68 -->

Serum 2 User Guide
68
Using Sample Instruments
Serum features a versatile and intuitive sampler, designed for creatively manipulating and playing
back audio samples. You can load a wide range of audio, from instrument sounds and vocals to field
recordings, offering endless possibilities for sound design and musical experimentation.
In addition to the standard features you would expect in a sampler, Serum includes powerful slicing
tools that are integrated with the CLIP mode within Serum, giving you even greater flexibility to
rearrange and reimagine almost any type of audio source.
You can also quickly and easily convert samples to wavetables, offering even more creative possibilities.
When loading a sample, Serum assumes all samples to be tuned to C3 by default (following
the standard that MIDI Note 69 is A3 at 440 Hz).
You can instruct Serum to assume a different tuning by adding the note name at the end of
the file name. For example, naming a sample file Morning Bass F2.flac tells Serum to
set F2 as the root of your sample, removing the need for you to manually adjust the pitch.
By informing Serum about the root note, Serum can now correctly map the sample. When
you trigger F2, the sample will now play at its original pitch, while playing other notes (such
as G2 or E2) will result in Serum pitch-shifting the sample accordingly.
Similarly, you can include flats and sharps in the file name. This means that naming a sample
file Ashes Piano Eb3.flac or Ashes Piano D#3.flac produces the same result; the
choice is yours whether to use flats or sharps.
Important: The note name (appearing at the end of the file name) must be preceded by a
space or underscore character. No other separators are supported.
Serum additionally refers to pitch data embedded in the instrument chunk of a WAV file.

<!-- page 69 -->

﻿
Using Sample Instruments
Serum 2 User Guide
69
Selecting the Sampler
Using OSC A, OSC B, or OSC C, click the header
and choose Sample in the context menu.
The oscillator switches to sample mode.
If you already chose a sample in the Granular
or Spectral modes, that sample appears in the
waveform display.
Otherwise, the display is empty.
Sample in the Oscillator Menu
Sample Instrument

<!-- page 70 -->

﻿
Using Sample Instruments
Serum 2 User Guide
70
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
When a sample loads, the waveform appears in
the display.
Sample Menu
Sample Instrument Loaded

<!-- page 71 -->

﻿
Using Sample Instruments
Serum 2 User Guide
71
Setting the Sample Start and End
You can easily set the sample start and end points
directly.
Hover over the sample and drag either (or both) of
the markers that appear (on the left or right).
Performing Sample Operations
You can perform a range of operations on the
loaded sample.
Right-click the sample and choose an operation
using the context menu.
All operations available in Sample mode
are also available when working in
Granular and Spectral modes.
It’s helpful to become familiar with these
operations in Sample mode before
switching to the other modes.
Setting Sample Start and End
Sample Operations Menu

<!-- page 72 -->

﻿
Using Sample Instruments
Serum 2 User Guide
72
The following describes the operations you can perform:
Operation
Description
Show Marker
Animation
Enable to have the start, end, loop start and loop end markers animate to
show the effect of any assigned modulation. Note that dragging the markers
is not allowed when this option is enabled.
Zoom to Start and
End
Reset the display zoom setting to the default showing both the start and end
markers.
By default, when this setting is disabled (no check mark present), you can
click-drag up and down in the waveform to zoom in and out, and drag left
and right to pan the waveform left and right.
When enabled (showing a check mark), the waveform maintains a consistent
display showing the entire waveform from start to end, without the ability to
zoom or pan using your mouse.
Important: Selecting this option toggles the setting; you need to deselect
this option to allow you to zoom the display again.
Snap Off
The next four menu items relate to how the sample playback start and end
points or loop points are adjusted.

With Snap Off, no snapping is applied. You can place the start and end, or
loop points freely along the waveform, without any restrictions or alignment
to specific reference points.
This provides full flexibility when working with waveforms but requires
careful manual placement to avoid clicks, pops, or timing issues.
Snap to Zero
Start, end, or loop points snap to the nearest zero-crossing in the waveform.
A zero-crossing is a point where the waveform amplitude is zero.
This prevents audio clicks or pops when the playback starts, ends, or loops,
as abrupt transitions between non-zero amplitudes can create artifacts. This
is ideal for ensuring smooth playback and transitions in the waveform.
Snap to Beats
Start, end, or loop points align to the nearest beat grid, based on the tempo
of your track.
This ensures that the waveform points or loops are musically synchronized
with the track tempo. This is useful for rhythmic or tempo-synced loops,
where precise timing is essential.

<!-- page 73 -->

﻿
Using Sample Instruments
Serum 2 User Guide
73
Operation
Description
Snap to Loop
The start or end points snap to the nearest pre-defined loop points in the
waveform.
This keeps the points aligned with the loop structure, ensuring seamless
looping without unintended offsets. This is helpful when working on a pre-
looped sample or creating a loop that must align perfectly.
Fade Edges
Apply a fade-in and fade-out at the start and end of the sample. You can
choose a setting from 1ms to 128ms as well as None.
This helps  smooth out any abrupt changes in amplitude that could cause
unwanted artifacts such as clicks or pops when the sample is triggered or
looped.
Normalize
Normalize the sample by adjusting its overall volume to maximize the peak
loudness without introducing distortion. This ensures consistent volume
levels while preserving the original dynamics of the sample.
Reverse
Reverse the audio sample.
Trim
Trim the sample to the current start and end markers.
Slicing Off
See “Slicing Samples” below.
Slice Auto
Slice Manual
The Fade Edges, Normalize, Reverse, and Trim operations are non-destructive to the original
sample file.
You can therefore easily undo and redo the operations using the
 and
 button
buttons respectively.
In addition, you can choose Reload Sample in the sample menu if you need to clear all
operations and return to the original sample.

<!-- page 74 -->

﻿
Using Sample Instruments
Serum 2 User Guide
74
Slicing Samples
Serum can help you slice audio samples into smaller segments, making it easier to trigger specific parts
individually. You can use this technique to create new rhythmic patterns, isolate key elements, or remix a
sample to fit a new sonic context.
Serum offers three slicing options:
•	 Slicing Off — Turn slicing off
•	 Slice Auto — Automatically slice the sample using a user-configurable threshold (sensitivity)
•	 Slice Manual — Automatically slice the sample, and then allow you to manually adjust the slices
The process for slicing samples is identical in Sample, Granular, and Spectral modes.
Auto Slicing
Right-click the sample and choose Slice Auto in
the context menu. Serum automatically slices the
sample.
Notice the yellow horizontal line. This indicates the
slicing threshold (sensitivity). You can move this
line to adjust the slicing threshold.
Dragging the line down decreases the slicing
threshold, producing more slices. Dragging the line
up increases the threshold, resulting in less slices.
After setting a threshold, hover the mouse over
the slices. Serum displays the note assigned to the
particular slice.
In this example, the highlighted slice is playable
using A1.
Auto Slicing
Adjusting the threshold

<!-- page 75 -->

﻿
Using Sample Instruments
Serum 2 User Guide
75
Click and drag down and up to zoom in and out of
the slices. You can also zoom in and out using the
mouse wheel.
When you are zoomed in, you can drag left and
right to pan the display.
Manual Slicing
Right-click the sample and choose Slice Manual in
the menu. Serum automatically slices the sample
and then gives you the option to manually adjust
the slices.
Zoom into the slices using your mouse wheel.
Note that zooming using click and drag is disabled
when manual slicing enabled.
Grab a slice handle and move it to the new
location. Continue adjusting other slices, as
needed.
Option-click (macOS) or Alt-click (Windows) to add
a slice. When the cursor is positioned over an
existing slice, Option- or Alt-clicking removes the slice.
Zooming In and Out
Manually Adjusting Slices

<!-- page 76 -->

﻿
Using Sample Instruments
Serum 2 User Guide
76
Slicing Options
If you select one of the slicing options (auto or
manual), the following additional options appear in
the context menu.
The following describes the options:
•	 Play Slice to End — Toggle this option to play
from the triggered slice to the end of the
sample.
Otherwise playback stops at the next slice
marker.
•	 Play Single Slice — Toggle this option to have
Serum play just one of the slices whenever
any note is triggered.
The playback rate of the slice changes based
on the trigger note (faster rate for notes
higher in the register).  You can assign a mod
source to the “single slice” destination to
control which slice is played.
You can use this option in combination with
Play Slice to End to play the entire sample
using any note, with the playback rate
increasing as you move up the register.
•	 Root Note — Set the note designated to play
the first slice. You can choose any C note
from C-1 to C8.
•	 Send to Selected Clip (x) — Send the slices to
the currently-selected clip (by default, Clip 1)
in the CLIP module, with each slice assigned
to the corresponding trigger note.
For example, if you select C3 as the root note, choosing this option assigns the slices to successive
notes in the currently-selected clip, starting at C3.
•	 Auto-Sync to Clip — Similar to the previous option in that the slices are sent to the currently-
selected clip, with each slice assigned to the corresponding trigger note. However, when you
modify the slices (by changing the slice threshold), the clip is automatically modified to reflect the
new slices.
Extra Slicing Options

<!-- page 77 -->

﻿
Using Sample Instruments
Serum 2 User Guide
77
Loop Menu
Use the loop menu to specify the loop mode for
the sample.
Similar to the sample operations
(described in the previous section),
the loop menu options available in
Sample mode are also available when
working in Granular and Spectral modes.
You can choose from among the following options:
Option
Description
One-shot
The sample plays forward for the duration of the note.
This technique is commonly used for sounds like drums, percussion hits, or
sound effects, where the full duration of the sample is essential.
Fwd Loop
The sample plays from the start marker to the loop end marker, and then
loops back to the loop start marker. This allows you to play the onset of the
audio and then stay sustained in the loop.
This method is ideal for sustaining sounds, such as a held violin note or a
drone, where you want the sample to maintain a consistent, ongoing tone.
Hover over the sample display and set the loop start and end by dragging
the corresponding blue markers. Click and drag to move the loop to a new
location.
Sample Loop Menu

<!-- page 78 -->

﻿
Using Sample Instruments
Serum 2 User Guide
78
Option
Description
Rev Loop
The sample plays from the start marker to the loop end marker and then
reverses playback direction to loop back to loop start, which then loops
backwards to the loop end.
This creates a unique effect where the sound appears to play in reverse
repeatedly, which can add an interesting, unconventional texture to the
music.
Hover over the sample display and set the loop start and end by dragging
the corresponding blue markers. Click and drag to move the loop to a new
location.
Fwd/Rwd Loop
The sample plays in a forward/reverse loop for the duration of the note.
Note that the sample plays from the start marker uninterrupted until you
reach the loop.
This creates a seamless, ping-pong-like effect where the sound alternates
between playing forward and in reverse, providing a smooth and
uninterrupted looping experience.
This type of playback is especially useful for creating evolving and dynamic
textures, as it helps avoid the abrupt transitions or potential clicks that can
occur with traditional forward-only looping.
Hover over the sample display and set the loop start and end by dragging
the corresponding blue markers. Click and drag to move the loop to a new
location.
Tailed
The sample plays forward from halfway through the sample to the end (the
tail) and then loops the tail of the sample as the amplitude decays.
This allows the sound to fade out naturally rather than cutting off abruptly.
Relative Loop
The looped section of the sample changes dynamically based on the
playback start position.
Rather than always looping between fixed start and end points, the loop
moves relative to the playback start marker.
This can be useful when automating or modulating the start position.
Link Loop Length
The loop end marker moves relative to the loop start marker, keeping the
loop length consistent.
This can be useful when automating or modulating the loop start position.
Exit Loop on Release
When a key is released and the amplitude envelope is in the release phase,
playback exits the loop and plays to the end of the sample.

<!-- page 79 -->

﻿
Using Sample Instruments
Serum 2 User Guide
79
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
Without a crossfade, loops can sometimes
result in abrupt or noticeable clicks, pops, or
tonal inconsistencies, especially when the
end and start of the loop have mismatched
waveforms.
Crossfading helps address this by blending
the overlapping regions at the loop
boundaries.
Click the
 button and drag up to set the
crossfade amount. A light blue curve shows
the crossfade graphically.
Setting Loop Start and End
Setting a Loop Cross Fade

<!-- page 80 -->

﻿
Using Sample Instruments
Serum 2 User Guide
80
Setting Sample Parameters
You can set the crossfade, unison (including
detune and blend), and adjust the waveform warp
mode.
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
•	 Lock Scan Rate (to Tempo) — Change the
scan rate when the tempo changes.
•	 Sample Length to BPM — Set the sample
length based on the BPM set in your host
DAW.
The SCAN knob changes to RATE, allowing
you to set the scan rate using beats and bars.
Sample Parameters
Sample Scan Menu

<!-- page 81 -->

﻿
Using Sample Instruments
Serum 2 User Guide
81
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
Sample Unison Settings

<!-- page 82 -->

﻿
Using Sample Instruments
Serum 2 User Guide
82
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
Set the unison stacking.
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

<!-- page 83 -->

﻿
Using Sample Instruments
Serum 2 User Guide
83
Setting
Description
START
Apply a random offset to the starting position for each unison voice.
This creates subtle timing differences, which can make the sound more lively,
complex, and textured.
SPAN
Apply a fixed offset to the starting position for each unison voice.
WARP 1
Spread out the warp amount applied to each voice around the current
WARP 1 knob position.
WARP 2
Spread out the warp amount applied to each voice around the current
WARP 2 knob position.
You can further adjust the unison setting using the DETUNE and BLEND knobs.
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

<!-- page 84 -->

﻿
Using Sample Instruments
Serum 2 User Guide
84
Pan
Use the PAN knob to control the placement of the waveform in the stereo field (left to right).
Level
Use the LEVEL knob to control the output volume of the oscillator.
Switching a Sample to a Wavetable
You can quickly and easily create a wavetable from a sample in Serum.
With a sample already
loaded, click the Sample
menu and hover over
Switch to Wavetable in
the menu.
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
Switch to Wavetable Menu