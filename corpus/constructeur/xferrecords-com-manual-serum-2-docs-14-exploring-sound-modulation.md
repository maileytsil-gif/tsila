---
titre: "xferrecords com manual serum 2 docs — Exploring Sound Modulation (p. 183-208)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Exploring Sound Modulation


<!-- page 183 -->

Serum 2 User Guide
183
Exploring Sound Modulation
Serum offers advanced options for sound modulation, allowing you to create dynamic sounds with
motion. Modulating sound in Serum principally involves working in the following three areas:
1.	Envelopes
2.	LFOs
3.	Modulation Matrix
Serum Sound Modulation
Using Envelopes
The Envelopes module offers four modulation sources, labeled ENV 1, ENV 2, ENV 3, and ENV 4. The
following shows the Envelopes area of Serum.

<!-- page 184 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
184
Serum Envelopes
Configuring Envelopes
Select an envelope
 by clicking the
corresponding envelope tab.
Modify the envelope directly using your
mouse.

Alternatively, adjust the ATK (attack),
HOLD, DEC (decay), SUS (sustain), and
REL (release) knobs to change the envelope
parameters.

Click the
 (lock) button
 to auto-
normalize the zoom.
Alternatively, drag the mouse through the
zoom slider to manually zoom the envelope
display.
Envelope Operations

<!-- page 185 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
185
Lock Button
Description
Locked
The envelope always zooms to perfectly fill the display area. This means that
adjusting envelope times simply changes how much time is represented on
the ruler scaling below the envelope.
Unlocked
Allows you to zoom in and out of the envelope by dragging up and down in
the zoom area directly below the Lock button.
See “Modifying Envelopes” later in this chapter for details about changing envelope shapes.
You can use all four envelopes, though ENV 1 is considered special within Serum because it is
used with the amplifier, controlling the output volume of each voice. You can still use ENV 1,
however, assigning it to any parameter as you would the other envelopes.
When you select ENV 2, ENV 3, or ENV 4, the envelope of ENV 1 is faintly visible (in gray) in
the background.
Inverting the Legato Setting
When the main LEGATO switch is enabled, envelopes do not retrigger if a second note is played while
a first note is still held. You can invert this option to force an envelope to always trigger at note on, even
when legato is enabled.
To do this, right-click the envelope graph and choose Legato Inverted in the context menu.
Setting Envelope Parameter Units
You can choose to alter values in milliseconds or in subdivisions of a note by clicking
 (MS or
BPM).
When you switch from MS to BPM, Serum calculates the nearest subdivision to the millisecond value
for each control based on host tempo.
Setting the Envelope Verticals
You can select whether the vertical lines that appear in the graph background are placed at time (ms) or
beat intervals.
Right-click on the graph and select either Time or Beats in the Grid sub-menu.

<!-- page 186 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
186
Modifying Envelopes
You can modify envelope shapes either by setting values using the knobs in the envelope window, or by
manipulating the envelope waveform directly.
To modify an envelope directly, click the
corresponding envelope tab, such as ENV 2,
ENV 3, or ENV 4 and graphically adjust the
envelope points using your mouse.
Alternatively, adjust the respective knob
settings using your mouse.
Important: Remember that ENV 1 is a special
envelope in Serum (it controls the output
volume) and is therefore always active.
You can modify the following envelope parameters using the knobs and directly on the graph:
Control
Description
ATK
Attack. The time for the initial run-up from start to peak, beginning with the
note on event.
HOLD
Hold. The time that the envelope stays at full volume before entering the
decay phase.
DEC
Decay. The time for the subsequent run-down from the attack level to the
designated sustain level.
SUS
Sustain. The level during the main sequence of the sound’s duration, until
the note off event.
REL
Release. The time for the level to decay from the sustain level to zero after
the note off event occurs.
You can modify the following parameters
directly using your mouse (only).
•	 Attack curve
•	 Decay curve
•	 Release curve
Graphical Envelope Edits
Curve Adjustments

<!-- page 187 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
187
Assigning an Envelope to a Control
You can assign an envelope
to a control (such as a knob),
causing the envelope to
modulate the control.
For example, you might
choose to have an envelope
modulate the wavetable
position (WT POS) setting of
OSC A.
To do this, click and drag the
ENV 1 tab to the WT POS
knob in the OSC A panel.
As you are dragging, notice
that an ENV 1 label hovers
next to the mouse pointer.
The pointer adds a + sign as
you hover over an assignable
knob (in this case, the WT
POS knob).
The + sign indicates that
you are over a valid mod
destination.
When you release the mouse
button, Serum automatically
makes the connection causing ENV 1 to now affect the OSC A wavetable position.
Right-click an envelope tab to bypass and
remove destinations assigned to the
envelope.
Assigning ENV 1 to WT POS
Bypass and Remove Assignments

<!-- page 188 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
188
Using LFOs
Serum offers ten low frequency oscillators (LFO) that each feature a set of independent controls. The
following shows the LFO area of Serum.
Serum LFOs
Note: When you initialize a patch, only LFO 1 to LFO 6 are visible. LFO 7 to LFO 10 becomes visible
after you use (assign) LFO 6.
Configuring LFOs
Select an LFO
 by clicking
the corresponding LFO tile.
Modify the LFO graph
directly
 using your mouse.
Change tools
 to get
different drawing results.
Fine-tune using the LFO
Editor, if needed.

Adjust knobs and controls

to change various parameters.
LFO Operations

<!-- page 189 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
189
Note that the settings are independent for each LFO.
To copy all LFO settings from one LFO to another, Option-click-drag (macOS) or Alt-click-drag
(Windows) an LFO title to another.
For example, to copy all the LFO 1 settings to LFO 2, Option/Alt-click-drag the LFO 1 tab to
LFO 2.
Drawing an LFO Graph
Serum offers a set of tools to help you create LFO graphs using your mouse.
LFO Graph Tools
Note that each tool relies on the current grid setting. The following table describes the LFO drawing
tools available:
Type
Tool
Use to ...
Point
Manipulate points in the graph, including adding new points,
moving points, deleting points, and adjusting curves (between
main points).
Flat
1
Add flat lines between points, based on the current grid size.
Ramp Up
Add ramp ups between points, based on the current grid size.
Ramp Down
Add ramp downs between points, based on the current grid size.

<!-- page 190 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
190
Modifying LFOs
When modifying points on an LFO graph, you can do the following:
Action
Task
Double-click
Add or remove points.
Shift-click
Draw steps at the grid size (step sequencer).
Option-click-drag a point (macOS)
Alt-click-drag a point (Windows)
Snap the point to the grid size.
Option-click-drag any curve point
(macOS)
Alt-click-drag any curve point
(Windows)
Move all curve points at once.
Click-drag on the background
Select multiple points.
Cmd-click-drag a point (macOS)
Ctrl-click-drag a point (Windows)
Select multiple points for relative movement. Rainbow
colors appear on the points.
Dragging them makes closer points move more, and
further points move less.
Ctrl-click (macOS)
Right-click (Windows)
Display a context menu showing additional features,
such as setting the segment shape for Shift-click,
removing all selected points, or assigning the start or
loopback points.
Shift-Cmd-click (macOS)
Shift-Ctrl-click (Windows) on a point
(in Envelope mode)
Set the point as the loopback position (or the very last
point if you intend no loopback position).
This is simply a shortcut to avoid the menu.

<!-- page 191 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
191
Modifying LFO Controls
The LFO module features a complete set of controls that you can use to set the LFO type, LFO mode,
BPM, grid size, and other options. The following table explains each of the LFO controls:
Control
Description
TYPE
The LFO type, from among the following:
•	 Normal
•	 Path
•	 Chaos: Lorenz
•	 Chaos: Rossler
•	 S&H
MODE (Retrig)
Specifies how the LFO behaves when a new note is played.
•	 FREE — The LFO follows the host clock and ignores note timing.
•	 RETRIG — Retriggers the LFO, causing the LFO to start with a new
note.
Use this setting when you want the LFO to always have the same
timing with new notes.
•	 ENVELOPE — Similar to RETRIG however the LFO plays through a
single cycle before stopping.
It’s possible to loop a segment of the LFO while in envelope mode
using the loopback point, accessible by Ctrl-clicking (macOS) or right-
clicking (Windows) a point and choosing Set Loopback Point Here.
This causes the LFO to play through, then cycle back to the selected
loopback point.
MONO
Select whether the LFO is monophonic or polyphonic.
By default, LFOs are polyphonic allow independent modulation for each
voice. With MONO enabled, the same modulation is applied to all voices.
SHAPE
Displays a pop-up menu allowing you to load an LFO preset.
Note that this overwrites the current LFO graph. The menu also offers the
ability to save the current LFO graph as a user-defined preset.
DIRECTION
The direction of the LFO, from among the following:
•	 Forward
•	 Reverse
•	 Ping Pong

<!-- page 192 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
192
Control
Description
GRID
The grid size of the LFO graph. The visual grid background in the LFO graph
changes as you adjust this setting.
Double-click the horizontal or vertical grid box and specify a number to set a
corresponding grid.
The grid is helpful when Alt-clicking (to snap points) or Shift-clicking (to draw
step segments) on the LFO graph. This  allows you to align modulation to
the rhythm of your production, or create arpeggiator-like pitch modulations.
HOST
Specifies whether the LFO is always synced to the global song position.
When BPM is enabled, the HOST switch determines whether the LFO
playback position “jumps” if you change the LFO rate.
When HOST is enabled, the phase is “anchored” to the host transport
position. For example, when changing the rate from ¼ note to 1 bar, the
phase may jump to have the playback properly fixed to the bar cycle.
BPM/HZ
Set the time value to snap to song tempo-based units (1/4 note, 1/8 note,
and so on) or Hertz (free time).
RATE
The playback speed of the LFO. This determines the amount of time
represented on the LFO graph area.
The LFO rate is in beat-synced units by default (when BPM is enabled) but
can also be set to a frequency in Hertz (when HZ is enabled).
When BPM is selected (see above), right-click the RATE knob and choose
Swing in the context menu to add swing to the LFO (using the SWING
setting above the keyboard).
When HZ is selected, right-click the RATE knob and choose 10x in the
menu to have the range of the rate control (in Hz) multiplied by a factor of
10, allowing for faster LFO rates.
TRIP/DOT
Set triplet and dotted time on the rate control respectively.
These are useful for avoiding triplet or dotted times when automating the
LFO rate, that is, for avoiding dotted and triplet times when you know you
want evenly beat-divisible time.
RISE
The amount of time for the LFO graph shape to have influence over the
LFO output.
The LFO begins with a fixed output (imagine the LFO graph as a fat
horizontal line, with the value of the left-most point of the LFOTool graph)
and slowly (based on the rise time) becoming the shape of the visible graph.
This knob is useful for having the LFO slowly influence your sound.

<!-- page 193 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
193
Control
Description
DELAY
The amount of time before the rise begins. The LFO has a fixed output, as
described above. After the delay time period, the rise begins.
SMOOTH
Smooth the LFO output. This is useful for avoiding abrupt jumps in the LFO
output, without having to draw ramps on every segment of the LFO graph.
PHASE
Sets the start position of the LFO phase.
Right-click the PHASE knob and choose Snap to Grid in the context menu
to have the phase value snap to the vertical grid lines (as defined by the grid
parameter at the bottom right of the LFO display).
Unlike Serum 1, the HOST switch now has an effect when BPM is disabled.
With BPM disabled, the HOST switch determines whether phase is calculated from the
host transport sample position on retriggering an LFO. One reason to enable the HOST
switch is to ensure that, even though an LFO is set to FREE, it plays back exactly the same
every time a song is played through.
Conversely, a reason to disable the HOST switch is to allow a truly free-running LFO. Each
time playback of a song starts from the beginning, the LFO phase will continue as if it had
been free-running since the last time playback started.
Using the LFO Editor
Click the
 button to access a dedicated LFO Editor featuring a larger canvas.
LFO Editor
You can use the same range of tools in the LFO Editor, with the advantage of being able to make finer
adjustments using the larger canvas.

<!-- page 194 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
194
Assigning an LFO to a Control
You can assign an LFO to a control (knob), causing the LFO to modulate the control. For instance, to
assign LFO 2 to the DETUNE knob in OSC C, click and drag from the LFO 2 tab to the DETUNE knob
in the OSC C panel.
As you are dragging, notice that an LFO 2 label hovers next to the mouse pointer The pointer adds a +
sign as you hover over an assignable knob (in this case, the DETUNE knob).
Assigning LFO 2 to DETUNE
The + sign indicates that you are over a valid mod destination.
When you release the mouse button, Serum
automatically makes the connection causing LFO 2
to now affect the OSC C detune.
After setting this modulation, notice that a number
1 now appears next to LFO 2.
This indicates that LFO 2 has one destination.
Mod Source with One Destination Assigned

<!-- page 195 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
195
Hover the mouse pointer over the mod source to
display a tooltip showing the destinations.
In this case, LFO 2 displays C Unison Detune as the
assigned destination.
Right-click an LFO tab
to bypass and remove
destinations assigned to the
LFO.
Setting the Modulator Depth
When you connect a modulation source with a destination,
such as LFO 2 with OSC C DETUNE, a blue halo appears
around the knob (in this case, the DETUNE knob).
This indicates the LFO 2 depth on the DETUNE knob,
defining how much influence the LFO has over the control
(knob) position.
A smaller blue halo appears to the top left of the knob. Hovering over this small halo displays an Up/
Down arrow control.
Click and drag the arrow control to change the modulation
depth amount.
As you drag the arrow, notice how the halo shrinks or
expands to show the range of modulation.
Hovering to Show Destinations
Bypass and Remove Assignments
DETUNE Modulator Depth at 100%
Setting Modulator Depth

<!-- page 196 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
196
Alternatively, as a shortcut, you can also Option/Alt-click and drag on the main knob (the
DETUNE knob itself, for example) to change the modulation depth.
Similar to the smaller blue halo, a gray halo appears to the top left of controls that also have a modulator
assigned, but when the modulator source is not currently selected.
To adjust the modulator depth in this case, simply click the corresponding mod source tab and adjust
the depth using the halo.
Alternatively, you can also adjust the depth using the Modulation
Matrix. See “Using the Modulation Matrix” on page 209 for
complete details.
When creating modulations by dragging-and-dropping, the default
type assigned depends on whether the control is centered. For
instance, if you drag to a DETUNE knob, which is centered, Serum
assumes you want the mod source to pan both left and right so bidirectional is chosen.
If you drag to a control that is not centered, such as the filter resonance (the RES knob), Serum assumes
you want the modulation to add value only, and unidirectional is used.
You can change the type setting without visiting the modulation matrix window by Shift-
Option-clicking (macOS) or Shift-Alt-clicking (Windows) on the knob with a visible (blue/
yellow) modulation assignment.
Setting Negative Modulation Depths
As described in the previous section, a blue halo around a control indicates the modulation depth of
the corresponding mod source. The blue color indicates a positive value. You can also set the depth to a
negative value using the same Click-drag operation.
When the value becomes negative, the color of the halo changes to a lighter blue. This indicates that
the depth amount is inverted (as the LFO output goes up, the influence on the control goes down).
Modulator Deselected

<!-- page 197 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
197
Copying a Wavetable Shape to an LFO
You can copy the current wavetable shape from any of the main oscillators (OSC A, OSC B, OSC C) to
an LFO, making it quick and easy to define complex LFO shapes.
To do so, load the appropriate wavetable in the oscillator and use the corresponding WT POS knob to
select the appropriate frame.
Copying a Wavetable to an LFO
Next, select the LFO tab to which you want to copy the wavetable shape, and click the Default menu.
Choose Wavetable A to LFO to copy the currently-selected frame in OSC A to the LFO. The same
applies for oscillators B and C.

<!-- page 198 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
198
Copying an LFO Shape to a Wavetable
You can similarly copy the current
LFO shape to an oscillator.
Choose or draw the appropriate
shape in an LFO and then
Option-drag (macOS)/Alt-drag
(Windows) the corresponding LFO
tab to the wavetable display for
either OSC A, OSC B, or OSC C.
Modulating LFO Points
You can modulate one or more LFO points (or curves) on an LFO graph, allowing you to create dynamic
or evolving modulations.
LFO point modulation works using LFO busses. Busing allows multiple point modulation by a single
source without requiring you to define duplicate assignments.
You can assign modulation to an LFO point using:
•	 Bus menus
•	 Drag and drop
Copying an LFO Shape to a Wavetable

<!-- page 199 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
199
Modulating LFO Points Using Menus
You can quickly define LFO point modulation using LFO bus menus.
In the LFO display, right-click (Ctrl-click on macOS) a point and choose Modulate X or Modulate Y in
the menu that appears.
LFO Point Bus Menu
Select an LFO bus (initially only LFO Bus 1 appears) and choose a modulation source. The modulation
source you choose will control the LFO point movement. The LFO graph updates to show a shaded bar
representing the modulation range (from minimum to maximum).
You can optionally drag to select multiple points in the LFO graph and configure modulation
for these points in a single assignment.

<!-- page 200 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
200
Modulating LFO Points Using Drag and Drop
You can also specify a modulation source by dragging the source, such as ENV 2, over an LFO point and
dropping on the X or Y button that appears.
Modulating by Dragging a Source
This allows you to modulate the point either horizontally (X) or vertically (Y), adding the source using the
next available LFO bus.
Using Context Menus with Controls
Each control has a context menu that gives you quick access to useful functions. You can access the
context menu by Ctrl-clicking (macOS) or right-clicking (Windows) the control.
The context menu that appears offers the following options:
Menu Option
Description
Mod Source
(submenu)
Display all possible modulation sources for the control/knob. Use this
menu to quickly configure a connection without having to drag from the
modulation source or visiting the Modulation Matrix window.
Aux Source (submenu)
Display all possible auxiliary sources for the control/knob.
Edit Custom Curve
Open a curve editor to define a custom mapping applied to the mod source.
Bypass Modulator
Bypass the current modulation connection (between the currently-selected
modulation source, such as LFO 1, and the control/knob).
After selecting the option, a check mark appears next to the menu item and
the halo around the control/knob turns gray indicating that the modulation
connection is bypassed. You can reverse this by selecting the menu item
again (uncheck the option).
You can also bypass a modulator by right-clicking the source tile (such as
LFO 1) and choosing the corresponding option.

<!-- page 201 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
201
Menu Option
Description
Remove Modulator
Remove the connection between the modulation source and the control/
knob.
Remove All
Modulators
Remove all connections to the control/knob from all modulation sources.
Reset Control
Reset the control/knob to the default value. This is the same as Cmd-clicking
(macOS) or Ctrl-clicking (Windows) the control.
MIDI Learn
Activate MIDI learn mode. When enabled, Serum waits for an incoming
MIDI CC value. After Serum receives a MIDI CC value, MIDI learn mode is
deactivated and the CC# is assigned to the control/knob.
The assignment is saved with the preset (patch).
Remove MIDI cc
Remove the MIDI CC# assignment, if any.
Lock Parameter
When enabled, lock the parameter (or module) setting (preventing a value
change) when loading presets.
Setting Velocity and Notes
You can use the MIDI velocity and note values, customized through a user-defined graph (curve), to
modulate the full range of parameters available in Serum. By mapping these MIDI inputs to specific
modulation targets using a graph, you gain precise control over how velocity and note data affect
various aspects of the sound.
For example, velocity can dynamically influence parameters like volume, filter cutoff, or even the
brightness of the timbre, enabling nuanced expression that responds directly to your playing intensity.

Similarly, you can map note values to parameters such as oscillator pitch, filter resonance, or effects
settings, allowing the sound to evolve based on the pitch being played. With the flexibility to design and
shape the response curve, you can fine-tune how each parameter behaves across the velocity range or
note spectrum.
This approach not only enhances the expressiveness of your sounds but also opens up creative
possibilities for crafting unique, dynamic, and musically responsive presets.

<!-- page 202 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
202
Serum Velocity and Notes
Velocity Settings
You can use the velocity tab to define the MIDI velocity graph that
you can later use to modulate the range of Serum parameters.
Click to select the VELO tab, if necessary.
Draw the graph using the tools and operations described in the next
section.
Then modulate one or more Serum controls (such as the filter cutoff,
for instance) using the procedure described later in this section.
Right-click the VELO tab and enable Legato (Portamento Time) in
the context menu to have portamento applied to the velocity curve
when a note is triggered and another is already held.
Using the same context menu, choose Init Graph to remove all added points and reset the graph to a
straight diagonal line.
Velocity Graph

<!-- page 203 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
203
Drawing the Graph
You can modify the velocity graph by manipulating the graph
directly, adding new points and dragging curves as needed using
your mouse.
Begin by ensuring that the VELO tab is selected.
The following table describes operations you can perform when editing the graph:
Operation
Display
Description
Double-click
Add a new point to the mask or remove an existing
point.
Drag a point
Move a point to a new location.
Drag a curve point
Create or modify a curve between points.
Option/Alt drag a
curve point
Create or modify curves between all points
simultaneously.
Modified Velocity Graph

<!-- page 204 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
204
Modulating a Control
You can assign the velocity graph to a control (such as a
knob), causing the graph to modulate the control.
For example, you might choose to have the velocity
graph modulate the filter cutoff (CUTOFF) setting of
FILTER 1.
To do this, click and drag the VELO tab to the CUTOFF
knob in the FILTER 1 panel.
As you are dragging, notice that an VELO label hovers
next to the mouse pointer. The pointer adds a + sign
as you hover over an assignable knob (in this case, the
CUTOFF knob).
The + sign indicates that you are over a valid mod
destination. When you release the mouse button,
Serum automatically makes the connection causing
VELO to now affect the FILTER 1 cutoff setting.
Note Settings
You can use the note tab to define the MIDI note graph that you
can later use to modulate Serum parameters.
Click to select the NOTE tab, if necessary.
Draw the graph using the tools and operations described in the
next section.
Then modulate one or more Serum controls (such as the filter
resonance, for instance) using the procedure described later in this
section.
Right-click the NOTE tab and enable Legato (Portamento Time) in the
context menu to have portamento applied to the note curve when a note is triggered and another is
already held.
Using the same context menu, choose Init Graph to remove all added points and reset the graph to a
straight diagonal line.
Velocity Modulating Cutoff
Note Graph

<!-- page 205 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
205
Drawing the Graph
You can modify the note graph by manipulating the graph directly,
adding new points and dragging curves as needed using your
mouse.
Begin by ensuring that the NOTE tab is selected. Then use your
mouse to adjust the graph.
Refer to the table in the “Velocity Settings” on page 202 section
for details about the various drawing operations available.
Modulating a Control
Similar to the VELO graph, you can assign the NOTE
graph to a control (such as a knob), causing the graph to
modulate the control. For example, you might choose to
have the note graph modulate the filter resonance (RES)
setting of FILTER 1.
To do this, click and drag the NOTE tab to the RES
knob in the FILTER 1 panel.
As you are dragging, notice that an NOTE label hovers
next to the mouse pointer. The pointer adds a + sign as
you hover over an assignable knob (in this case, the RES
knob).
The + sign indicates that you are over a valid mod
destination. When you release the mouse button,
Serum automatically makes the connection causing
NOTE to now affect the FILTER 1 resonance value.
Modified Note Graph
Note Modulating Resonance

<!-- page 206 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
206
Using Macros
Serum features eight macros that you can use to simplify the control of multiple parameters
simultaneously. Macros provide an efficient way to design, perform, and tweak sounds without having
to manually adjust numerous parameters one by one.
Macros Pane
For example, instead of adjusting filter cutoff, resonance, and pan individually, you can assign these
parameters to a single macro.
Macros are great for experimenting with sound because small changes to a macro setting can result in
complex shifts across multiple sound elements. Macros are also powerful in live performance setups,
where fast and intuitive control is essential.
In addition to being a modulation source, macros can also serve as a destination. This offers
incredible flexibility when setting up modulation.
For example, consider the case where you want a second aux source to modulate a
destination. You could set a macro as an aux source and then modulate it with another entry
in the modulation matrix, using both a main and aux source.

<!-- page 207 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
207
Assigning a Macro
You can assign a macro to a control by dragging and dropping the macro selector to the appropriate
control. As you are dragging, notice that a label hovers next to the mouse pointer The pointer adds a +
sign as you hover over an assignable knob (in this case, the DETUNE knob).
The + sign indicates that you are over a valid
mod destination.
When you release the mouse button, Serum
automatically makes the connection causing
the macro to now affect the OSC A detune.
After setting the macro, notice that
a number 1 now appears next to
MACRO 1.
This indicates that MACRO 1 has one
destination.
Assigning a Macro to a Control
Macro with One Destination Assigned

<!-- page 208 -->

﻿
Exploring Sound Modulation
Serum 2 User Guide
208
Hover the mouse pointer over the macro to display a small tooltip showing the destinations.
In this case, MACRO 1 displays A Unison Detune as the
assigned destination.
You can repeat this process and assign the same macro to
multiple controls.
You can then manipulate the macro (perhaps assigned to a knob
or slider on a physical controller) as you would a mod wheel.
Note: As with other modulators, you can set the modulator
depth to offer even finer control over the destination. See
“Setting the Modulator Depth” for more information.
To swap macros, drag and drop a macro over another
macro.
For example, if MACRO 1 is assigned to the WT POS
knob and MACRO 2 is assigned to the PAN knob,
dragging and dropping either macro to the other macro
swaps the assignments.
Using Oscillators and Filters as Modulation Sources
You can use the output of any oscillator or filter as a modulation source.
Drag the module label to a
control to create the modulation
assignment.
At this point, the control is
modulated by the output of the
corresponding oscillator or filter.
Hovering to Show Destinations
Using an Oscillator as a Modulator