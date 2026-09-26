---
titre: "xferrecords com manual serum 2 docs — Getting Started (p. 18-36)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Getting Started


<!-- page 18 -->

Serum 2 User Guide
18
Getting Started
Getting started with Serum is quick and easy. This section provides a short overview to help you
understand some common basic operations.
Adding Serum to a Track
You can add Serum to an instrument (MIDI) track in your DAW using the same procedure that you use
with any software instrument. At this point, sending MIDI notes to Serum should trigger the default
sawtooth sound.
Similarly, you should hear the sawtooth sound if you click any of the piano keys at the bottom of the
Serum user interface (UI).
Note: If you are not sure how to add an instrument to a track, refer to the documentation that came
with your DAW.
Loading a Serum Preset
Serum lets you create amazing sounds from scratch. However, a good place to start is browsing and
loading presets. To select a preset, click - Init - to display the Serum presets menu.
Serum Presets Menu
Navigate the menu to choose a preset.
After choosing a preset, you can click the < > arrows (to the right of the preset name) to navigate
through a particular preset subfolder without having to repeatedly display the presets menu.
You can also choose a preset by clicking the
 button (next to the main menu near the top right) to
access the presets browser.
Click an entry in the list to load the corresponding preset. Most presets load immediately; presets with
larger embedded samples, such as multisampled instruments, display a small green progress bar (directly
beneath the preset name) when loading.

<!-- page 19 -->

﻿
Getting Started
Serum 2 User Guide
19
Serum Presets Browser
You can preview presets to help you quickly find the right sound.
Click the
 (play) button to preview the
corresponding preset.
Serum plays an embedded preview clip (MIDI sequence)
if the preset designer specified one. Otherwise, Serum
plays a “fallback” clip to give you a sense of the preset.
You can choose the fallback clip from among three standard options. Serum also allows you to auto-
preview clips. See “Performing Standard Preset Operations” on page 334 for more information.
Click another play button to preview the corresponding
preset.
Click the
 button to stop the preview.
Presets Showing Play Buttons
Preset Playing

<!-- page 20 -->

﻿
Getting Started
Serum 2 User Guide
20
Creating a New Sound
In addition to exploring Serum’s rich set of factory presets, you can use Serum to create your own
sounds from scratch.
If you just added Serum to a track, you will see the - Init - preset, which has a single wavetable oscillator
enabled (OSC A) together with basic envelope and LFO modulators defined. This is a perfect blank slate
from which to craft and evolve your sound.
Note: If you’ve already loaded a preset or made other changes and would like to start over, click the
main menu and choose Init Preset in the context menu.
This initializes Serum to the default
settings and sets the stage for you to
work on your new sound.
For more information about all the
options available in the main menu, see
“Appendix A: Using the Main Menu” on
page 323.
Choose Init Preset from the Main Menu

<!-- page 21 -->

﻿
Getting Started
Serum 2 User Guide
21
Saving Changes
After crafting a new sound or modifying an existing preset, you can save the configuration as a new
preset (that you can load later).
1.	(Optional) Before saving a preset, add metadata to the preset.
a. Double-click the ARTIST field directly below the preset name and type the artist name.
b. Double-click the DESC field and add any relevant information related to the preset.
You can add any type of information that you consider helpful or informative.
Preset Metadata (Artist and Description)
2.	Click the
 (disk) button to the left of the preset name.
Save (Disk) Button
A dialog appears allowing you to specify the file name and choose the location. Note that this file
name becomes the preset name in Serum.
3.	Click the Save button.
After you’ve already saved a preset and made modifications, click the
 (disk) button to save
your changes. A dialog appears allowing you to type a new file name or overwrite your existing
preset file.
If you already know that you want to use the same file name (and overwrite the existing preset
file), Option-click (macOS)/Alt-click (Windows) the disk button. The preset saves using the
same file name without displaying the dialog.

<!-- page 22 -->

﻿
Getting Started
Serum 2 User Guide
22
Embedding Content When Saving a Preset
You can embed a wavetable or sample into
your preset when saving by clicking the

button.
After clicking, the button changes
 to
show that the feature is enabled.
Note: Alternatively, you can click the name of
the wavetable or sample and choose Embed
in Preset in the context menu.
In general, you should only consider
doing this if you intend to share your
preset with someone else.
Note that the option to embed a wavetable
or sample into a preset is not available for
factory-supplied content.
Dragging Audio to Your DAW
You can quickly export the last played note or chord (in
WAV format) to your DAW.
Hover over the left of the Serum logo, and drag the wave
icon that appears to an audio track in your DAW.
Embed Indicator
Exporting Audio by Dragging

<!-- page 23 -->

﻿
Getting Started
Serum 2 User Guide
23
Serum silently plays the note or
chord using the corresponding
pitch, velocity, and duration.
In addition to inserting the
audio on to the track, Serum also
captures the exported audio as
a WAV-format file (stored in the
Serum Presets > Renders
folder).
Option-click (macOS)/Alt-click (Windows) the wave icon to open the Renders folder. Shift-
drag the wave icon to copy the current (saved) preset to the macOS Finder/Windows Explorer.
Exploring Basic Operations
Serum includes a set of elements and on-screen controls designed to closely replicate the experience of
using a hardware synthesizer, while also providing all the benefits of a digital computer.
This section describes common operations when using the on-screen controls, including options
that you can use with most knobs and sliders. Subsequent chapters will describe specific options for
individual controls and other elements of the interface.
Dragging Audio to Your DAW

<!-- page 24 -->

﻿
Getting Started
Serum 2 User Guide
24
Displaying Help (Tooltips)
You can display help for any control (such as
a knob) by hovering the mouse pointer over
the control and pausing for a moment.
For example, hovering over a regular control
displays a tooltip similar to the one shown
here.
This allows you to see information about a
particular control or feature without having to
open this manual.
Important: The Help tooltips global
preference needs to be set to SHOW for
tooltips to appear. Tooltips are enabled by
default when you first install Serum.
Refer to “Exploring Global Settings” on page
312 for more information about modifying
global preferences.
Hovering the mouse pointer over a control
that has modulation assigned displays the
modulation sources.
For example, hovering the mouse over the
CUTOFF knob shows that LFO 3 and ENV 2
are assigned to modulate the filter cutoff.
Tooltip Help
Tooltip Showing Modulation Sources

<!-- page 25 -->

﻿
Getting Started
Serum 2 User Guide
25
Using the Serum Keyboard
Serum features an on-screen keyboard that you can use to directly play notes using your mouse, or
monitor the notes being played on an external MIDI or computer keyboard. The on-screen keyboard
also indicates which notes are being played through the Serum clip player and arpeggiator.
Serum Keyboard
You can also use the keyboard to specify basic settings including the following:
•	 TRANSPOSE — The number of semitones (positive or negative) to transpose all incoming and
generated MIDI notes.
•	 KEY — The key to use throughout Serum, most notably in the CLIP and ARP modules.
•	 SCALE — The scale to use. Notes outside the scale automatically conform to the selected scale.
•	 SWING — Use to swing or shuffle the timing of the grid in the CLIP and ARP editors.
•	 OSC MAPPING — Edit the note and velocity ranges of the oscillators and arpeggiator.
Using Knobs and Sliders
To adjust a knob or slider, click and drag either
up and down or left and right. A pop-up displays
the current value allowing you to dial in a specific
setting. Hold the Shift key to fine tune the
adjustment.
If your mouse has a scroll wheel, you can also use
it to adjust values up and down (without displaying
the current value in a pop-up).
Double-click a knob or slider to display a text box
showing the current value. Enter a new value for
precise adjustments.
You can change the behavior of double-
clicking a knob or slider to have Serum
reset the control to its default setting, if
you prefer.
See “Exploring Global Settings” on page
312 for more information.
Click-Dragging a Knob

<!-- page 26 -->

﻿
Getting Started
Serum 2 User Guide
26
Right-click a knob or slider to open a context menu
that displays the settings and operations available
for that control.
You can use the menu to choose one or more
modulation sources (such as ENV 1 or LFO 2) for
the control.
You’ll read about modulating parameters later in
this guide.
You can also choose to bypass or remove a
modulator, or remove all modulators assigned to
the control.
Note: Some controls offer additional menu
options, depending on the context. You’ll learn
about these options in relevant sections of this
guide.
You’ll also see the following options available on nearly all knob and slider menus:
•	 Reset Control — Resets the control to the default value.
This is the same as Cmd-clicking (macOS) or Ctrl-clicking (Windows) the control.
•	 MIDI Learn — Activates MIDI learn mode. When enabled, Serum waits for an incoming MIDI CC
value.
After Serum receives a MIDI CC value, MIDI learn mode is deactivated and the CC# is assigned to
the knob or slider. Note that the assignment is saved with the preset (patch).
•	 Lock Parameter — When enabled, locks the control setting (preventing a value change) when
loading presets. You can, however, continue to adjust the control manually.
The Reset Control and Lock Parameter options appear in the context menu of almost every
control in Serum.
In all cases, you can use these options to reset the control to the default value and lock a
control parameter to prevent it from changing when loading presets, respectively.
Right-Click Context Menu

<!-- page 27 -->

﻿
Getting Started
Serum 2 User Guide
27
When saving a DAW session, MIDI CC assignments are saved and recalled with the
session.
When saving a preset, MIDI CC assignments are saved with the preset, but are only loaded
if the Load MIDI Map from Preset preference is enabled on the Global page (this setting is
disabled by default).
See “Preferences” on page 313 for more information about setting global preferences.
You can set the current MIDI CC assignments to load by default by choosing Save MIDI
Map in the main menu and saving the MIDI map as default.SerumMIDIMap in the
Serum 2 Presets/System/MIDI CC Maps folder.
This map then loads automatically when creating a new instance of Serum or choosing Init
Preset in the main menu.  The map also automatically loads when selecting a preset if the
Load MIDI Map from Preset preference is disabled.
Undo and Redo
You can undo and redo just about any operation in Serum, encouraging you to effortlessly experiment in
your sound design.
You can access the undo and redo buttons in the Serum header, near the top right.
Undo and Redo Buttons
Click the
 button to undo your last operation (such as a change to a knob or an LFO shape,
among others).
Click the
 button to redo the last undo operation. This allows you to quickly compare and evaluate
changes to your sounds side by side.
Controlling the Main Output Volume
You can control the main output volume of Serum using the
MAIN knob (near the top right).
The stereo volume appears as a meter next to the knob.
Main Volume

<!-- page 28 -->

﻿
Getting Started
Serum 2 User Guide
28
Using Oscillators and Filters
Serum generates sound using a set of oscillators, powered by a range of techniques that use both
wavetables and samples. Serum then uses filters to sculpt the sound generated by the oscillators.
Each oscillator type features specific settings and parameters that you’ll read about later in this guide.
This section describes a series of operations that are common across most oscillator and filter types.
Enabling an Oscillator or Filter
You can enable an oscillator by clicking the label (containing the oscillator name and enable button).
When enabled, the button turns green.
Enabling OSC B
OSC B Enabled
You can also use the power button to mute (disable) an oscillator to either solo the other oscillators or
free up CPU, as needed. Notice that when an oscillator is off, the entire panel is dimmed.
Enabling a filter is very similar, except that you need to click the power button directly.
Enabling Filter 1
Filter 1 Enabled

<!-- page 29 -->

﻿
Getting Started
Serum 2 User Guide
29
Choosing Oscillator or Filter Options
You can choose an oscillator or filter option using
the associated drop-down menu.
Oscillator options accessible using the drop-down
menu include wavetables, samples, multisamples,
and more.
In the case of filters, you can choose the type of
filter using the drop-down menu.
Click the < > arrows to quickly navigate to the
previous and next menu option.
Alternatively, hover over the menu and use the
mouse wheel to quickly rotate through menu
options.
Using Pitch Controls
You can alter the pitch of the waveform using the
OCT (octave), SEM (semitone), FIN (fine tuning in
cents), and CRS (coarse) controls.
The CRS setting controls the pitch transpose that
tunes or detunes continuous (no snap) semitones.
CRS is most useful as a modulation destination or
automation parameter for wide sweeps.
Serum uses separate controls for the four settings to facilitate automation and modulation (rather than a
combined value such as 36.04).
It’s often handy to assign an LFO to the octave setting, for instance, without having to count in 12
semitones.
Choosing a Wavetable
Oscillator Pitch Controls

<!-- page 30 -->

﻿
Getting Started
Serum 2 User Guide
30
There are times, however, when you might want to have an LFO control an oscillator pitch in a more
coarse manner (a siren-type sound might require an LFO to modulate an oscillator pitch smoothly across
an octave or more).
You can do this by modulating the CRS setting. (You’ll read about modulating controls later in this guide.)
Use the Global > Main Tuning modulation destination to have all oscillators follow a coarse
pitch change.
Setting the Octave or Semitone Mode
Serum further allows you to specify the
mode for the OCT and SEM controls.
Right-click either control and choose
the mode in the context menu.
You can select from the following
options:
•	 Semitones — Adjust the pitch in
semitones, which are the intervals
between two adjacent keys on
a piano tuned to 12-tone equal
temperament used in American/
European musical tradition.
This allows for fine-tuning,
transposing, or creating intervals
such as minor/major thirds, fifths,
and more.
•	 Harmonics — Change the pitch by multiplying the base frequency using whole number harmonics.
This generates pitches based on the harmonic series, which is useful for creating overtone-rich
sounds, like organ tones or harmonic layers.
•	 Ratio — Set the pitch of the oscillator in relation to the base frequency using ratios, which is
common in FM synthesis.
In this case, the oscillator is tuned to a specific ratio relative to another oscillator to create complex
timbres. When you select this mode, you can then set the specific source (SRC) and ratio.
•	 Step — Adjust the pitch up or down in periods and steps, as defined by the active MTS-ESP tuning.
This option only appears when you are using microtuning and have an MTS-ESP tuning source
available.
Selecting the Mode

<!-- page 31 -->

﻿
Getting Started
Serum 2 User Guide
31
Routing an Oscillator or Filter
You can route the signal from any oscillator (OSC A, OSC B, OSC C, SUB, and NOISE) or any filters
(FILTER 1 and FILTER 2) to a range of targets.
The following table describes the routing targets:
Target
Description
Filter
Route the signal to either FILTER 1, FILTER 2, or by varying degrees to both.
Main
Route the signal to the main output, passing through the effects section.
Direct
Route the signal to bypass the filter and effects section and play “clean”
along with the main output.
None
Route the signal to no output path. You can use this setting when you
want to use an oscillator as a modulation source without having the sound
included as part of the output signal.
You can access the routing options by clicking the button near the top right of an oscillator or filter.
When you click, a set of controls
appear that are relevant to the routing
path.
For example, in the case of routing to
the Serum filters, you have the option
of routing the signal completely to
FILTER 1 (knob turned far left),
completely to FILTER 2 (knob turned
far right), or to some combination
of both (knob set somewhere in
between).
By default, OSC A is automatically
routed to FILTER 1, though FILTER 1
is not enabled in new presets.
The other oscillators and filters are
automatically routed to the Main
output. You can change the routing at
any time.
Accessing the Signal Routing Settings

<!-- page 32 -->

﻿
Getting Started
Serum 2 User Guide
32
You can also send the signal to the Serum busses
(BUS 1 and BUS 2) by adjusting the corresponding
knobs.
To change the signal routing, click the
 button
and choose another option, as appropriate.
Filter Routing and Busses
Routing Menu

<!-- page 33 -->

﻿
Getting Started
Serum 2 User Guide
33
Accessing the Oscillator or Filter Menu
You can use the oscillator or filter menu to
perform the most common operations related
to the module.
These operations include locking the module,
initializing the module, copying and pasting a
module (with or without modulations), and
enabling pitch tracking (in the case of oscillators).
Right-click the module label to access the
context menu.
The next sections describe the specific operations
you can perform.
Locking a Module
You can lock a module by right-clicking the module label and choosing Lock Module in the context
menu (see the Oscillator Menu above). This causes the parameters (settings) of the oscillator module to
remain unchanged (locked) as you change presets.
For example, if you lock OSC A, the module remains the same even when you load a preset (that would
normally change the oscillator module).
After locking a module, you can unlock individual controls (such as the WT POS knob, for
example), as needed.
Note: This does not apply when you initialize the entire preset (by choosing Init Preset using the main
menu). This initializes all settings and removes any module locks that you might have set.
Oscillator Menu

<!-- page 34 -->

﻿
Getting Started
Serum 2 User Guide
34
Initializing a Module
After making changes to an oscillator or filter, you can return the module to an initialized state without
affecting any other Serum setting.
Right-click the module label and choose Init Module in the context menu. The oscillator returns to initial
settings (including removing all modulators assigned to the module).
Copying a Module
You can copy an oscillator or filter (with or without modulations) and paste it to another (similar) module.
This works when copying and pasting modules in the same preset, as well as when you want to copy
and paste between presets.
For example, consider the case where you configure an oscillator module with specific wavetable,
unison, detune, and warp settings. In addition, you have LFO 1 modulating the wavetable position
(WT POS knob).
Right-clicking the oscillator label and choosing Copy in the menu copies the module to Serum’s
internal clipboard. Right-clicking another oscillator module and choosing Paste in the menu pastes the
configuration (all settings except the WT POS modulation) to the corresponding module.
To copy and paste a module configuration including modulations, right-click the oscillator label and
choose Copy (w/mods) in the menu. Pasting to a new module now includes the WT POS modulation
from the earlier example.
As mentioned, this copy and paste operation works even after changing or initializing a preset. In
addition, the module configuration stays on Serum’s internal clipboard after pasting, allowing you to
quickly paste the same configuration to multiple modules as needed. It is not possible, however, to copy
a module from one instance of Serum to another.
Hold the Option/Alt key and drag the module label (next to the power button) to another
(similar) module to copy the module without modulations.
Hold the Shift-Option or Shift-Alt keys and drag the module label to another module to copy
with modulations.
Dragging from one module label to another without any keyboard modifiers swaps the two
modules (including modulation assignments).

<!-- page 35 -->

﻿
Getting Started
Serum 2 User Guide
35
Enabling Pitch Tracking
Pitch tracking instructs the oscillator to adjust its pitch in response to the MIDI note or key being
played. This ensures that the oscillator’s frequency corresponds to the desired musical pitch. Pitch
tracking is typically used with melodic and harmonic sounds, where the pitch needs to follow the
keyboard.
Pitch tracking is enabled by default.
You can choose to disable pitch tracking by right-clicking the oscillator label and toggling Enable Pitch
Tracking off in the context menu.
You might choose to disable pitch tracking with the following types of sounds:
•	 Drones or static sounds
This produces a constant, unchanging pitch regardless of the notes played. This is common with
ambient soundscapes that don’t need pitch variation. This is also useful for layering a static tonal
element beneath a dynamic lead or pad.
•	 Percussive sounds
These sounds often don’t rely on pitch tracking since their character is defined more by their
transient and timbral qualities than specific pitch. You can use this with a variety of drum sounds,
such as kick drums, snares, or hi-hats, as well as metallic or inharmonic percussive textures.
•	 Noise-based effects
Noise signals (white, pink, or custom noise) aren’t inherently pitched, so pitch tracking is irrelevant.
You can also use this with wind, rain, or static effects, in addition to risers, sweeps, and impacts.
•	 Experimental sounds
Disabling pitch tracking can lead to unexpected and unique sonic results. This can be helpful for
creating unconventional or dissonant sounds. This can more easily allow you to explore textures
where the focus is on timbre and modulation rather than pitch accuracy.
You can also disable pitch tracking to add layers without harmonic conflicts. A non-pitch-tracked
oscillator can add texture or depth without interfering with the harmonic structure (such as a static sub-
bass tone underneath a harmonic element).
When pitch tracking is disabled, the Multisample, Sample, Granular, and Spectral
oscillators play C3 (MIDI note 60), whereas the Wavetable oscillator plays C-2
(MIDI note 0), allowing it to be used as an LFO.

<!-- page 36 -->

﻿
Getting Started
Serum 2 User Guide
36
Pitch Bend Tracking
Pitch bend tracking determines whether MIDI
pitch bend affects the frequency of an oscillator
when pitch tracking is disabled.
The option appears on the Oscillator context menu
only when Enable Pitch Tracking is disabled, and is
only available for Sample, Granular, and Spectral
oscillator types. Pitch bend tracking is enabled by
default.
You might choose to disable pitch bend tracking
for static, drone, or noise-based sounds so that
they remain at a constant pitch, even when moving
the pitch bend wheel.
Note that Wavetable and Multisample oscillator
types always track pitch bend when pitch tracking
is disabled.
Resizing the UI
You can resize the Serum user interface to make it fit appropriately
within your work environment.
The easiest way to resize the interface is to click and drag the lower
right corner of the UI (similar to how you would resize most other
windows using your computer).
For more precise control, click the Serum 2 logo (near the top left)
and choose a resize option in the menu that appears. The window
resizes to match your selection.
After resizing, you can make this size the default setting by clicking
the Serum 2 logo again and choosing Set x% as Default, where x is
the current setting.
To return to the default setting of 100%, click the Serum 2 logo and
choose Default (100%) using the menu.
Pitch Bend Tracking Enabled
Resize Menu