---
titre: "xferrecords com manual serum 2 docs — Using the Arpeggiator (p. 244-266)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Arpeggiator


<!-- page 244 -->

Serum 2 User Guide
244
Using the Arpeggiator
Serum features a versatile, full-featured arpeggiator designed to effortlessly sequence the notes of a
chord into rhythmic patterns, enabling you to create dynamic, flowing musical phrases with ease.
Serum offers a broad array of patterns, fully customizable through parameters such as transposition,
offsets, repeats, and chance, among others, giving you precise creative freedom.
Using the arpeggiator, you can swiftly craft intricate, evolving musical expressions that transform simple
chords into captivating, complex melodies.
Click the
 button to access the Serum arpeggiator.
Serum Arpeggiator

<!-- page 245 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
245
Exploring the Arpeggiator
The ARP module includes several panes to help you navigate and access the various features.
Arpeggiator Module
Use the GLOBAL pane to set parameters that affect all aspects of the arpeggiator, including the launch
quantization and whether parameter edits affect all arp slots. You can also use the GLOBAL pane to
load arpeggiator presets, create a new arp bank, and save your own arp bank as a user-defined preset.
Use the PATTERN pane to set the shape of the currently-selected arp slot (or all arp slots if you
selected that EDIT ALL option in the GLOBAL pane). You can also use this pane to set the arpeggiator
rate (in either beats per minute or Hertz), and enable triplets and dotted notes.
Use the TRANSPOSE pane to set the transpose shift (positive or negative) and range for the
arpeggiator (which specifies how many times the pattern is transposed by the shift setting). You can also
set the shape of the transpose range, which further expands your creative possibilities.
Use the PLAYBACK pane to specify the playback settings for the arpeggiator, including offsets and
repeats, as well as the length of the gate and the probability of a note being played. You can also enable
a latch to continue playing notes without needing to keep the keys pressed down, as well as pass
incoming notes to the output (similar to a MIDI THRU port on a device) .
Use the RETRIGGER pane to specify how the arpeggiator retriggers the arp shape/pattern. You can set
to retrigger the arp when the slot is launched or on a incoming note (first note or otherwise). You can
also specify the rate at which the arpeggiator is retriggered.
Use the VELOCITY pane to configure the arpeggiator to raise or lower the arpeggiator note output
velocities over time. You can set the speed at which the velocities are changed (decay) as well as the
target velocity towards which the decay setting moves.
The ARP module further features 12 arpeggiators per arp bank. This offers a rich playground in which to
explore and define evolving rhythmic patterns and dynamic musical phrases.

<!-- page 246 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
246
Setting Global Parameters
You can use the GLOBAL pane to set
parameters that affect all aspects of the
arpeggiator.
For example, you can use the GLOBAL
pane to load an arp bank, set the launch
quantization, and configure whether
parameter edits apply to all arp slots.
You can also create a new arp bank and save
your own arp bank as a user-defined preset.
To load a factory-supplied or user-defined
bank, click the BANK field and choose a bank
using the menu that appears.
The bank loads and populates the arpeggiator
slots and associated settings.
Set the LAUNCH QUANT by clicking in the
field and dragging up or down.
This specifies the interval at which a triggered
arp syncs to the clock/DAW.
Enable the EDIT ALL switch
 to have your parameter edits apply to all arp slots.
When disabled, any changes to the arp settings (such as TRANSPOSE or CHANCE) apply only to the
currently-selected arpeggiator slot.
When enabled, changes to any parameter become immediately effective for all arp slots.
Hold the Option (macOS) or Alt (Windows) key when editing an arp parameter to apply the
change to all arps.
Global Arpeggiator Settings
Bank Menu
Launch Quant Setting

<!-- page 247 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
247
Creating a New Arp Bank
In addition to exploring the factory-supplied arp banks, you can initialize the bank and create your own
arpeggiator bank.
Note: Initializing the
arpeggiator bank only affects
arp bank settings. This
does not change any of the
other sound design settings
you’ve configured (including
oscillators, filters, clips, and
so on).
Click the BANK menu and
choose Init in the menu.
This initializes the ARP
module to the default
settings and sets the stage
for you to create a custom
arpeggiator bank.
Saving Arp Banks
After creating a new arp bank, or editing an
existing bank, you can save the entire arpeggiator
configuration as a new preset.
Note that arp bank presets that have been
modified display as asterisk (*) after the name.
Click the BANK field and choose Save Arp Bank in
the menu that appears.
A dialog appears allowing you to type the arp bank
name.
Creating a New Arp Bank
Arp Bank Modified

<!-- page 248 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
248
By default, the arp bank is
saved in a standard location
so that Serum can easily find
it later.
Note that if you try to save
a modified arp bank that has
already been saved, a dialog
appears allowing you to give
your recently-modified arp
bank a new name.
This allows you to freely
experiment with changes,
saving your work in
increments as you progress.
If you would instead prefer to overwrite the existing arp bank, you can choose the existing file name in
the dialog.
Setting the Arp Pattern
You can set the shape of the arp pattern, as well as rate, triplets, and dotted note settings.
In the SHAPE field, click and choose an option using
the menu that appears.
Serum offers a wide range of arpeggiator shapes,
including standard up/down patterns as well as less
familiar shapes such as Converge and Diverge, together
with a collection of random shapes.
To set the arpeggiator rate, begin by selecting either
BPM (beats per minute) or HZ (Hertz). Then click and
drag either the RATE knob or the value field directly to
the right of the knob (both work identically). To set a
specific value, double-click either the knob or the field and type the appropriate value.
Click the TRIP button
 to enable triplets. Click the DOT button
 to enable dotted notes.
Important: The parameters you set in this and the other panes only affect the currently-selected arp
slot unless you enabled EDIT ALL in the GLOBAL pane..
One way to try all the various shapes is to enable the LATCH button (in the PLAYBACK
pane), play a chord on your MIDI controller, and then cycle through all the shapes one by one
to hear the difference. You can also watch the Serum keyboard to get a visual sense of how
the shape arpeggiates the chord.
Saving an Arp Bank
Pattern Settings

<!-- page 249 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
249
Creating a Custom Pattern
You can define a custom arpeggiator using Serum’s
advanced pattern editor.
Choose Pattern in the SHAPE field, and click the

button.
The button highlights
 and the arp editor appears
in the top half of the interface.
Use the left panel to specify the pattern settings and the right panel to configure the arpeggiator graph.
Arp Editor
Loading a Pattern
You can quickly load a factory-supplied
or user-defined pattern.
Click the pattern name (topmost) field
and choose a pattern using the menu
that appears.
The pattern loads and populates the arp
graph and associated settings.
Pattern Option
Creating an Arp Pattern

<!-- page 250 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
250
Creating a New Pattern
You can create a new pattern, or reinitialize the pattern editor, at any time.
Note: Initializing the pattern only affects
current arp pattern settings. This does
not change any of the other arp bank
settings.
Click the pattern name field and choose
Init in the menu.
This initializes the pattern editor to
the default settings and provides an
opportunity for you to create a new
pattern.
Configuring the Pattern Settings
You can use the PATTERN SETTINGS pane to specify
parameters that affect the entire arp pattern.
For example, you can use the pane to set the pattern
length, the mode (normal, reverse, and so on), the step
mode, and the wrap settings.
Creating an Arp Pattern
Pattern Option

<!-- page 251 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
251
The following table describes the parameters you can set:
Field
Description
LENGTH
The pattern length in bars, beats, and 16th notes.
MODE
The mode of the pattern specifying how the playhead moves, from among
the following:
•	 Normal
•	 Reverse
•	 Pendulum
•	 Random
•	 Rand Start
•	 Rand End
•	 One Shot
•	 Static
TIME
For random play modes, specifies how often the playhead jumps to a new
random position. You can choose from values between 1/16th note and four
bars.
STEP MODE
Specifies how each step is played, from among the following:
•	 Normal
•	 New Only
•	 Chord
•	 Chord (new)
The chord triggers all held notes on each step with voicing determined by
step numbers.
Note that new modes trigger a step only if the input note is received exactly
at the same time as the step triggers.
WRAP
Specifies how pattern steps less than, or greater than, the number of held
keys are treated.
PITCH
The wrap transpose, from 0 to 24 semitones.
RANGE
Specifies how pattern steps less than, or great than, the number of held keys
are transposed.

<!-- page 252 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
252
Saving a Pattern
After creating a new pattern, or modifying an
existing pattern, you can save the configuration
as a new pattern.
Note that pattern presets that have been
modified display as asterisk (*) after the name.
Click the pattern name (topmost) field and choose Save Pattern in the menu that appears.
A dialog appears allowing you to type the arp
pattern name.
By default, the pattern is saved in a standard
location so that Serum can easily find it later.
Note that if you try to save a modified pattern that
has already been saved, a dialog appears allowing
you to give your recently-modified arp pattern a
new name.
This allows you to freely experiment with changes,
saving your work in steps as you progress.
If you would instead prefer to overwrite the existing
arp pattern, you can choose the existing file name in the dialog.
Renaming a Pattern
You can rename a pattern, as needed.
Click the pattern name field and choose Rename
Pattern in the menu that appears.
Type the new name of the pattern.
Pattern Modified
Saving a Pattern
Renaming a Pattern

<!-- page 253 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
253
Using the Arp Graph Editor
The pattern editor features an advanced graph editor that you can use to create the arp graph. You can
use the graph editor to interactively create complete patterns in the context of your current patch.
Graph Editor
Click the grid size
 and drag up or down to change the default grid setting.
Scroll the grid up or down by clicking and
dragging in the Step area. You can also scroll
up or down using the mouse wheel.

Double-click to add a new note event in the
arp graph. The latest note event you added
appears in orange.
The arp graph offers capabilities very similarly
to the piano roll in the CLIP module. For
example, you can click and drag across the
graph to select note events, and copy/cut
and paste events to a new area in the graph.
You can also select and move note events
around the graph. See “Working with
the Piano Roll” on page 224 for more
information.
Double-click in the Accent lane to add an
accent to the corresponding note event.

Double-click in the Strum lane to add
strumming to the corresponding area.
Use the automation lanes
 to control various parameters over time. Right-click in various places in
the arp grid to display a context menu for the corresponding element.
Saving a Pattern

<!-- page 254 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
254
Transpose Settings
You can set the transpose shift and range for the
arpeggiator.
Click and drag the SHIFT knob to set the amount that
each repetition of the pattern is transposed. This can
be a positive or negative value.
Click and drag the RANGE knob to specify how many
times the pattern is transposed by the SHIFT setting.
To set the shape of the transpose range, right-click
the RANGE knob and choose an option in the menu
that appears.
Transpose Range Shape Menu
The following table describes the range shape options available. Note that each example uses a SHIFT
setting of 3 and a RANGE setting of 4.
Transpose Settings

<!-- page 255 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
255
Shape
Description
Up
Transpose the arpeggiated notes by the SHIFT setting and repeat the
number of times specified by the RANGE setting.
Down
Transpose the arpeggiated notes by the SHIFT setting and repeat the
number of times specified by the RANGE setting.
Up/Down
Transpose the arpeggiated notes by the SHIFT setting and repeat the
number of times as specified by the RANGE setting.
Then immediately reverse (transpose the arpeggiated notes in the reverse
direction and repeat using the same settings).

<!-- page 256 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
256
Shape
Description
Down/Up
Transpose the arpeggiated notes by the SHIFT setting and repeat the
number of times specified by the RANGE setting.
Then immediately reverse (transpose the arpeggiated notes in the reverse
direction and repeat using the same settings).
Up+Down
Transpose the arpeggiated notes by the SHIFT setting and repeat the
number of times specified by the RANGE setting.
Then start again in the reverse direction.
Down+Up
Transpose the arpeggiated notes by the SHIFT setting and repeat the
number of times specified by the RANGE setting.
Then start again in the reverse direction.

<!-- page 257 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
257
Shape
Description
Thumb Up
Transpose the arpeggiated notes by the SHIFT setting.
After each transposition, play the original arpeggio followed by another
transposition. Repeat the number of times specified by the RANGE setting.
Thumb UD
Transpose the arpeggiated notes by the SHIFT setting.
After each transposition, play the original arpeggio followed by another
transposition. Repeat the number of times specified by the RANGE setting.
Then immediately reverse (transpose the arpeggiated notes in the reverse
direction and repeat using the same settings).

<!-- page 258 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
258
Shape
Description
Pinky Up
Transpose the arpeggiated notes to the maximum (as specified by the
SHIFT and RANGE settings). After each transposition, play the maximum
transposition followed by the original arpeggio transposed.
Repeat the number of times specified by the RANGE setting.
Pinky UD
Transpose the arpeggiated notes to the maximum (as specified by the
SHIFT and RANGE settings). After each transposition, play the maximum
transposition followed by the original arpeggio transposed.
Repeat the number of times specified by the RANGE setting.
Then immediately reverse (transpose the arpeggiated notes in the reverse
direction and repeat using the same settings).

<!-- page 259 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
259
Shape
Description
Converge
Transpose the arpeggiated notes to the maximum (as specified by the SHIFT
and RANGE settings). After each transposition, converge the transpositions
between original to maximum.
Diverge
Transpose the arpeggiated notes as specified by the SHIFT setting. After
each transposition, diverge the transpositions further.
Con+Diverge
Transpose the arpeggiated notes first using the converge pattern followed
by the diverge pattern (see above).

<!-- page 260 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
260
Shape
Description
Chord
Use the SHIFT and RANGE settings to play the chord instead of the
arpeggio.
Random
Randomly transpose the arpeggiated notes based on the SHIFT setting and
repeating the number of times specified by the RANGE setting.
Rnd.NoDup
Randomly transpose the arpeggiated notes (without duplicates) based
on the SHIFT setting and repeating the number of times specified by the
RANGE setting.

<!-- page 261 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
261
Shape
Description
Rnd.Drift
Randomly transpose (with a bias towards drifting) the arpeggiated notes
based on the SHIFT setting and repeating the number of times specified by
the RANGE setting.
Rnd.Once
Randomly transpose the arpeggiated notes once based on the SHIFT setting
and repeating the number of times specified by the RANGE setting. Then
continue using this pattern.
Playback Settings
You can specify the playback settings for the arpeggiator, including offsets and repeats, as well as the
length of the gate and the probability of a note being played.
Click the LATCH  button
 to continue
playing notes without needing to keep the keys
pressed down. The button highlights
 when
enabled.
Click the THRU button
 to pass the
incoming notes to the output (in a conceptually
similar way to a physical MIDI THRU port on a
device).
When this setting is disabled, the arpeggiator
consumes the input; when enabled, the notes are passed through and played.
Playback Settings

<!-- page 262 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
262
Click and drag the following knobs to perform the associated action:
Knob
Description
OFFSET
Offset the order of the arpeggiator notes.
REPEATS
Set the number of times the pattern and transpose range are repeated.
GATE
Set the length of the arpeggiator notes, relative to the RATE setting.
CHANCE
Set the probability of a note being played.
Right-click the knob and choose Pre in the menu to apply the CHANCE
setting before the SHAPE pattern is advanced. You can use this to
guarantee that the next note played is always next in the sequence.
When the arp is enabled, MIDI CC64 sustain messages sent to Serum will control the latch
instead of regular note sustain.
Retrigger Settings
You can specify how the arpeggiator retriggers the arp shape/pattern.
Enable the LAUNCH setting to retrigger the arp when the slot is
launched.
Enable the RATE setting and set an appropriate rate by clicking and
dragging the field. The rate sets the interval at which the arpeggiator is
retriggered.
Enable the NOTE setting to retrigger on an incoming note.
Similarly, enable the FIRST setting to retrigger only on a first incoming
note, as would be the case for held notes in a chord.
Velocity Settings
You can set the arpeggiator to raise or lower the arpeggiator note
output velocities over time. Enable the VELOCITY setting to activate
the velocity settings (in this section).
Enable the RETRIG setting to reset the velocity decay value (back to
incoming velocities) whenever the RETRIGGER feature is activated.
(See the previous section for more information about retrigger settings.)
Click and drag the DECAY knob to set the speed at which the velocities
are changed.
Click and drag the TARGET knob to set the target velocity towards which
the DECAY setting moves.
Retrigger Settings
Velocity Settings

<!-- page 263 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
263
Managing Arpeggiators
The ARP module features 12 arpeggiators per arp bank (similar to the CLIPS module). This makes it easy
and convenient to trigger these arps using either a MIDI keyboard or your computer keyboard.
Arpeggiator Slots
Click an arp slot to select it. The current arpeggiator is highlighted and the play button turns purple. The
arp settings appear in the various sections.
To perform operations on the arpeggiator, right-click the arp
and choose an option in the menu that appears.
The following table describes the available operations:
Operation
Description
Rename Pattern
By default, arpeggiators are named after the pattern shape, such as Up (1/16)
or Down (1/32).
When you define the pattern yourself (by choosing Pattern in the SHAPE
field and then using the pattern editor), you can rename the arp to better
describe the pattern you created.
Right-click in the arp and choose Rename Pattern in the context menu. A
text area appears in the clip header.
Type the new pattern name and press the Enter key.
Copy Pattern
Copy the arp settings to Serum’s internal clipboard.
Right-click the source arp and choose Copy Pattern in the context menu.
Right-click the destination arp and choose Paste Pattern in the menu.
Note that it is not possible to copy a pattern from one instance of Serum to
another.
Paste Pattern
Paste the most-recently copied arp into the target arp.
Erase Pattern
Erase the contents of the selected arp.
Show Pattern Names
Show the arp names in the slots.
Current Arp (Highlighted)

<!-- page 264 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
264
Triggering the Arpeggiator
You can trigger an arpeggiator using the play button or the arpeggiator keyboard.
To trigger an arpeggiator while in ARP mode, click the
 button for the corresponding slot.
The arp starts playing and the button changes

to indicate which arp is currently playing.
To stop an arpeggiator, stop the MIDI input to the
arpeggiator either by releasing the keys, stopping a playing
clip, or disabling the latch (if enabled).
You can make changes to any aspect of the arp while it is playing, including changing patterns,
modifying arp settings, and more. You can also change the underlying sound design as the arp plays,
providing a versatile way to hear your sound evolve, in context.
You can also trigger clips using the ARP keyboard.
This is helpful when you are not in ARP mode and instead
tweaking the oscillators, mixing, applying effects, or adjusting
the modulation matrix.
Notice that the arp slots (in ARP mode) are arranged similar
to a keyboard. This makes it easy to logically map the arp
slots to the ARP keyboard. Press a key to play the corresponding arp. The key highlights in purple.
Press the same key to relaunch the arp, or press another key to launch that arp.
Important: If you launch an arp but don’t hear the sequence that you expect, verify that arp playback is
enabled.

Arpeggiator Slot with Play Button
Arpeggiator Keyboard

<!-- page 265 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
265
Managing MIDI Out
You can specify whether Serum should output
MIDI data from the CLIP player, the ARP
(arpeggiator), or neither.
By default, MIDI OUT is set to Off, which means
that Serum does not output MIDI data to the host
(DAW).
Otherwise, the display shows the corresponding
MIDI data stream.
Right-click the MIDI OUT field to choose an
option using the menu. You can choose from
among the following:
•	 Off — The default. Do not output MIDI data
to the host.
•	 Clip Player — Output MIDI data from only the
CLIP player.
•	 On — Output MIDI data from both the CLIP
player and the arpeggiator.
MIDI Out Pane
MIDI Out Data
MIDI Out Menu

<!-- page 266 -->

﻿
Using the Arpeggiator
Serum 2 User Guide
266
Configuring the Arp Module
You can configure the ARP module using the
main context menu.
The following describes the options:
Operation
Description
Lock Module
Enable this option to lock the entire ARP module, including all arps, when
changing (sound) presets.
MIDI Input Trigger
Octave
Select the octave from which notes trigger arps. Alternatively, set to Off if no
triggering is required.
By default, this is set to the lowest octave of the MIDI note range.
ARP Menu