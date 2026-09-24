---
titre: "xferrecords com manual serum 2 docs — Using the Keyboard (p. 267-273)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Keyboard


<!-- page 267 -->

Serum 2 User Guide
267
Using the Keyboard
Serum features an on-screen keyboard that you can use to play notes as well as set a range of
parameters that affect MIDI input and output.
Serum Keyboard
Use the TRANSPOSE field
 to transpose the keyboard within a range of two octaves (set in
semitones).
Use the KEY and SCALE fields
 to choose appropriate options. Serum offers a very thorough list of
scale options from which to choose.
Use the SWING field
 to set the swing applied to certain notes to add groove.
And finally, use the OSC MAPPING feature
 to edit the note ranges of the oscillators and
arpeggiator.
Transpose
You can transpose the keyboard within a range of -24 to +24 semitones.
Keyboard Transpose
Click the TRANSPOSE field and drag up or down. Alternatively, for even finer control, click the up and
down arrows to adjust the setting by a single semitone.
You can also hover over the field and adjust the setting by 12 semitone increments using the mouse
wheel.

<!-- page 268 -->

﻿
Using the Keyboard
Serum 2 User Guide
268
Setting the Key and Scale
You can set the key and scale within Serum. These settings, together with the TRANSPOSE setting
(described above), are applied to both MIDI input and the output of both the CLIP and ARP modules.
Key and Scale
Serum offers a comprehensive selection of scales.
Scale Options
After selecting the key and scale, the piano roll in the CLIP module highlights the root note of the key.
In addition, notes within the scale are highlighted with a gray background, while notes outside the scale
appear with a darker gray background.

<!-- page 269 -->

﻿
Using the Keyboard
Serum 2 User Guide
269
Setting Swing
You can set the swing applied to certain notes to add groove, thereby imparting a more human feel
instead of a rigid, machine-like rhythm.
Swing
Click the SWING field and drag up or down. The range of swing values depends on the host DAW that
you are using (see the note below). You can also hover over the field and adjust the setting using the
mouse wheel.
By default, swing is set to OFF. As soon as you move
away this setting, a second field appears showing the
swing division.
Click and drag to set the appropriate division. You can also use a mouse wheel or the arrow buttons.
Serum attempts to match the swing value displayed to the convention used in the host
DAW. This means that setting the same values in Serum and the host should result in the
same amount of swing.
For example, when using Ableton Live, swing is displayed as a range between 12.5% and
87.5%. In contrast, FL Studio displays swing with a range of -150% to 150%.
Oscillator Mapping
You can edit the note ranges of the oscillators and arpeggiator to define and limit the range of notes to
which the oscillator or arpeggiator responds.
Oscillator Mapping
Click the OSC MAPPING button. The oscillator mapping dialog appears.

<!-- page 270 -->

﻿
Using the Keyboard
Serum 2 User Guide
270
Oscillator Mapping Editor
To set the key mapping, select KEY in the MAPPING
section (lower left).
Click and drag the left or right edge of the note range for
the corresponding oscillator or arpeggiator.
The current note appears below the cursor, and a highlight
shows the note in the context of the keyboard.
Setting the Note Range
To move a note range, drag the range to the new location.
macOS
Note that the “hand” looks
slightly different when
moving a note range on
macOS and Windows.
Windows
Key Mapping

<!-- page 271 -->

﻿
Using the Keyboard
Serum 2 User Guide
271
The current note boundaries appear below the cursor (hand), and highlights show the note range in the
context of the keyboard.
Moving a Note Range
You can double-click a range to type specific values into the
text box that appears.
Use the same notation that appears on the keyboard below
the ranges.
Use the FOLD checkbox to specify what happens to notes outside the selected range. When
unselected, the notes are ignored. When selected, the notes get “folded” into the selected range. You
can use this, for example, to restrict the range of an oscillator used for sub-bass to a single low octave,
regardless of the octave the incoming note was played.
Select the WARP checkbox to set the corresponding oscillator to warp other oscillators when keys are
played outside of its note range. For example, consider the case when the OSC A warp is set to FM
from B. If you want the warp to apply regardless of the OSC B note ranges, select the WARP checkbox
for OSC B. This allows you to restrict the OSC B note range without losing the warp on OSC A for
notes outside of the OSC B range.
You can define note ranges to do the following:
•	 Create splits and layers
You can assign different oscillators to specific note ranges to create multi-layered sounds or
keyboard splits. For example, you might create bass and lead layers, assigning one oscillator to low
notes for a bass sound and another to high notes for a lead.
Similarly, you could create complex pads by layering different oscillators with unique timbres across
the keyboard range for rich, evolving textures.

<!-- page 272 -->

﻿
Using the Keyboard
Serum 2 User Guide
272
•	 Emulate acoustic instruments
Many acoustic instruments have distinct tonal characteristics across their range. Assigning
oscillators to specific note ranges can mimic this behavior.
For example, you could consider simulating how low strings sound warmer while higher strings
sound brighter on a string instrument.
•	 Add specific harmonic content to note ranges
You could create timbral variation by assigning unique waveforms and effects to different note
ranges. For example, you could consider using a sine wave oscillator in the lower range for pure
bass tones and a saw wave in higher ranges for harmonic richness.
This could thereby enhance expressiveness by varying the oscillator’s contribution based on the
note range.
Mapping Velocity Ranges
You can edit the velocity ranges of the oscillators and arpeggiator to define and limit the range of
velocities that the oscillator or arpeggiator can produce.
Right-click any oscillator header and choose Edit Note
Ranges in the menu. The Mapping Editor appears.
To set the velocity mapping, select VEL in the MAPPING
section (lower left).
Velocity Mapping Editor
Velocity Mapping

<!-- page 273 -->

﻿
Using the Keyboard
Serum 2 User Guide
273
Click and drag the left or right edge of the velocity range for the corresponding oscillator or arpeggiator.
The current velocity appears below the cursor, and a highlight shows the velocity in the context of the
complete range (1 to 127).
Setting the Velocity Range
To move a velocity range, drag the range to the new location.
The current velocity boundaries appear below the cursor (hand), and highlights show the velocity range
in the context of the complete range (1 to 127).
Moving a Velocity Range