---
titre: "xferrecords com manual serum 2 docs — Using the Modulation Matrix (p. 209-214)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Modulation Matrix


<!-- page 209 -->

Serum 2 User Guide
209
Using the Modulation Matrix
Serum features an easy-to-use modulation matrix that shows all configured modulations as a list. This
at-a-glance view allows you to quickly select the routing and amounts for the various modulation
connections.
Note: Serum offers 64 modulation matrix slots in a patch. You can use these slots to modify or scale up
to 64 destination parameters, one per slot, with 49 different modulation sources.
Serum enhances the typical modulation matrix found on many synthesizers by integrating this matrix
with the drag-and-drop style of routing described in “Exploring Sound Modulation”.
Serum Modulation Matrix
Dragging a modulation source to a control/knob causes the routing to automatically appear in the
matrix and vice-versa. This gives you extra flexibility when viewing, configuring, and modifying your
modulation assignments.

<!-- page 210 -->

﻿
Using the Modulation Matrix
Serum 2 User Guide
210
Exploring the Modulation Matrix
Click the MATRIX tab to access the modulation matrix.
Accessing the Modulation Matrix
You can use the modulation matrix to configure the following options:
Option
Description
SOURCE
The modulation source, such as LFO 1 for example.
Note that certain modulation sources are only available to set using the
modulation matrix (it’s not possible to drag the source to the control). These
mod sources include:
•	 Active Voices, derived by dividing the number of active voices by the
maximum number of voices allowed by the POLY count setting.
•	 Note-On Alt. 1/2, which switches between 0 and 1 at each note-on.
The state of Note-On Alt 2 is the inverse of Note-On Alt 1.
•	 Note-On Rand (Discrete). The Note-On Rand 1/2 sources send the
same value to each assigned destination at note-on. Destinations
assigned to Note-On Rand (Discrete) each get a different value at
note-on.
•	 Note-on Rand 1 and 2, which are two separate random numbers
generated on a note on event, in case you need two different random
values for each note on event.
•	 Oscillators, allowing you to use the output of any oscillator (including
NOISE and SUB) as a mod source.
•	 Release Velocity
•	 Voice Index, updated at note-on with a value derived from the current
index of the Voice panel divided by the number of active steps.
•	 Voice Mod 1/2, updated at note-on with the value of the current step
in the Voice panel for Mod 1/2.
•	 Expression/MPE X/Y/Z, which are Note Expression or MIDI Polyphonic
Expression (MPE) axes.
•	 Filters, allowing you to use the output of either filter as a mod source.

<!-- page 211 -->

﻿
Using the Modulation Matrix
Serum 2 User Guide
211
Option
Description
SOURCE (cont.)
•	 Mod Wheel
•	 Aftertouch (channel pressure)
•	 Poly Aftertouch
•	 Pitch Bend
•	 Fixed (not really a modulation source, but you can use this to allow a
modulation assignment to get a fixed value with slider depth control,
should you want that for some reason).
CRV (Curve)
Scale the mod source to respond in a non-linear fashion. A 50% value
indicates a linear setting. When the curve is gray, it is bypassed.
Double-click the curve (or right-click and choose Editable Curve in the
menu) to display a curve editor that you can use to define the remapping
curve. Draw the appropriate curve, and use the RISE and FALL smoothing
controls to act as a slew limiter on the source.
AMOUNT
The modulation depth, set using a bi-directional slider. Moving the slider to
the left sets a negative value, causing the mod source output to be inverted
before heading to its destination.
Cmd-clicking (macOS) or Ctrl-clicking (Windows) resets the value to the
(zero) default.
POL (Polarity)
Specify whether the modulation is unidirectional or bi-directional.
You can achieve similar sonic results with either, it depends on whether you
prefer the destination control (the knob position) to be at the beginning
(unidirectional) or the middle (bi-directional).
DESTINATION
The modulation destination. Use the pop-up menu to select the destination
(the parameter modified by the mod source).
OUT
A graph that shows the shape of the modulation output.
AUX SOURCE
A secondary source to determine the amount of modulation. Use the pop-up
menu to select the aux source.
INV
Invert the auxiliary source signal.
Normally, the two modulation sources are “multiplied” together so that one
is scaling the other.
For instance, if LFO 1 is the SOURCE, and ModWheel is the auxiliary source
(AUX SOURCE), the LFO 1 influence is inaudible unless the ModWheel is
raised above zero. This is the default setting.
When set to inverse, the setting is the same as above except that the
secondary source (AUX SOURCE) is value-inverted.
For instance, in the above example, there would be no modulation if the
ModWheel is at maximum, and there would be full modulation if the
ModWheel is at minimum.

<!-- page 212 -->

﻿
Using the Modulation Matrix
Serum 2 User Guide
212
Option
Description
CRV (Curve)
Scale the auxiliary source to behave in a non-linear fashion. A setting of 50%
designated linear. The curve is bypassed when it is gray.
OUTPUT
Scale the final modulation output, allowing for fine tuning.
Select to bypass this row of the modulation matrix (causing it now to have
no effect).
The button changes
 to show that it is enabled.
Click to remove this row of the modulation matrix. This removes the
modulation assignment from the patch.
Click the
 button (near the top left) to expand the matrix to show more rows. Alternatively, press
Option-F (macOS)/Alt-F (Windows) to expand the view.
Modulation Matrix (Expanded)
Similarly, click the
 button to revert the modulation matrix down to the default size. Similarly, press
Option-F (macOS)/Alt-F (Windows) to revert the view to the original size.

<!-- page 213 -->

﻿
Using the Modulation Matrix
Serum 2 User Guide
213
Moving Modulations in the Matrix
To move a modulation row to another location, click and drag the modulation handle
 to another
location.
Moving a Modulation
Bypassing a Modulation
Every row features a bypass button
 that allows you to easily bypass the modulation.
Clicking the button bypasses the modulation in the signal routing, indicated by the button updating

to show that the row is being bypassed.
Removing a Modulation
You can remove a modulation assignment directly from the modulation matrix. To do so, click the

button for the corresponding modulation.

<!-- page 214 -->

﻿
Using the Modulation Matrix
Serum 2 User Guide
214
Performing Matrix Operations
You can perform a range of additional operations on the modulation matrix including sorting the matrix,
locking the modulations (even when you change presets), and creating specialized new modulation
assignments.
Click the
 button (near the top right) and choose an option in the menu that appears.
Modulation Matrix Menu
The following table describes the operations you can perform:
Operation
Description
Sort by Source
Sort the modulation matrix (ascending) by the SOURCE column.
Sort by Destination
Sort the modulation matrix (ascending) by the DESTINATION column.
Lock Matrix (Keep
Assignments on
Preset Change)
Lock the modulation matrix, which keeps the modulation assignments when
you change presets or initialize a new preset.
Create Vibrato
(Unused LFO->Pitch
via Wheel)
Create a new modulation that maps the next available LFO to “Main Tuning”
using the Mod Wheel.
Create Velo->Amp
Assignment
Create a new modulation that maps VELO to the Amp.
Apply and Delete
Macros
“Bake” the macro adjustments into the current preset.
Specifically, for any parameter assigned to a macro, update the current value
of the parameter to include any offset from the macro. Then remove all
modulation assignments for all macros from the modulation matrix.