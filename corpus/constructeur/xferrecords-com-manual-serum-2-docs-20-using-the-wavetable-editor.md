---
titre: "xferrecords com manual serum 2 docs — Using the Wavetable Editor (p. 274-290)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Wavetable Editor


<!-- page 274 -->

Serum 2 User Guide
274
Using the Wavetable Editor
Serum features an advanced Wavetable Editor
that makes it fun and easy to create and edit
wavetables.
To access the Wavetable Editor, click the

button in the OSC A, OSC B, or OSC C pane.
The Wavetable Editor appears.
Wavetable Editor
Accessing the Editor

<!-- page 275 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
275
Using the Thumbnails
Thumbnails appear along the bottom of the Wavetable Editor.
Wavetable Editor Thumbnails
Thumbnail overviews provide an easy way to view, select, and reorder the subtables that make up a
wavetable.
You can use the thumbnails to perform a variety of functions:
Thumbnail Action
Description
Click
View and edit the specific frame (subtable).
Click-drag
Move a frame to a new location. As you drag left or right, a yellow vertical
cursor appears showing where the frame will relocate after you release the
mouse.
Shift-click
Select a range of frames. After selecting a range, you can perform operations
such as Remove: Multiselection and Remove All (Except Selected), among
others.

<!-- page 276 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
276
Using the Drawing Tools
The Wavetable Editor offers a toolbar that you can use to draw in the main display. Each tool operates
in relation to the grid size (set in the lower-right corner of the main waveform).
Wavetable Editor Toolbar and Grid Size
Tool
Name
Description
Flat Line
The default tool. Draw a flat line in the grid step.
Sine
Draw a sine wave. This is useful for adding a pure
harmonic at the grid size.
For example, if the grid is set to 4, this tool adds an
overtone two octaves above the fundamental.

<!-- page 277 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
277
Tool
Name
Description
Slope Up
Draw a diagonal line upwards. This is useful for drawing
small saws to give your waveform a buzz.
Slope Down
Draw a diagonal line downwards. This is useful for drawing
small saws to give your waveform a buzz.
Curve up
Draw a quarter-sine waveform.
Curve down
Draw a quarter-sine waveform.
Half sine (peak)
Draw a half-sine waveform.
Half sine (valley)
Draw a half-sine waveform.
Interpolate linear
Rather than drawing, this tool connects endpoints to draw
a straight line across the grid segment.
This can be useful for smoothing out a waveform (LPF).
Interpolate curved
Similar to interpolate linear, however with a more gradual
transition (not as much harmonics as linear; even more
low pass/smoothed).
Nudge
Move a portion of the waveform up or down. Use this for
clipping (if you click-drag vertically far enough, the audio
begins to clip/flat-line).
Noise
Add noise to the waveform. Dragging vertically up adds
noise, while dragging down reduces noise.
Mirror
Create a symmetrical wavetable drawing by mirroring from
the center.

<!-- page 278 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
278
FFT Area
Use the FFT area to draw the waveform harmonics and their relative phases to one another.
Wavetable Editor FFT Area
The top section shows the frequency bins. The left-most bin represents the fundamental or single sine
wave at the oscillator’s base frequency (the note you play).
The vertical bars to the right represent the harmonics that make up the sound, (2:1 is the octave, 3:1 is
+19 semitones, 4:1 equals 24 semitones, and so on).
The bottom section shows the phase offset for each harmonic. Right-click to display the context menu.
Shift-Cmd-click (macOS) or Shift-Ctrl-click (Windows) in the bottom section to nudge the
phase offset to the right.

<!-- page 279 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
279
Wavetable Editor FFT Menu
There is a separate menu for the frequency and phase bins.
Menu Item
Description
Clear All
Zero out all bins (silence).
Clear HF (Bin 0 to
End)
Zero all bins (silence) to the right of the clicked bin. Since the high harmonics
are silenced, you can think of this as a low-pass filter.
Clear LF (Start to 0)
Zero all bins (silence) to the left of the clicked bin. Since the low harmonics
are silenced, you can think of this as a high-pass filter
Generate Saw
Set all harmonic bins to relative amplitudes creating a standard saw
waveform.
Randomize Low x Bins
Insert random values for the left-most number of bins. This changes the
base tone of the sound while leaving the higher-frequencies (“buzz”) intact.

<!-- page 280 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
280
Menu Item
Description
Randomize Low x Bins
(with Half)
Insert random values for the left-most number of bins, but allows 50%
amplitude for harmonics. This provides more tonal options.
Randomize All
Randomize all bins. This results in a noisy/buzzy tone. This is useful as
a starting point for further destruction with FFT drawing or other menu
commands.
Create Random Series
Gaps
Randomly remove harmonics.
Progressive Fade
Reduce the high frequency content gradually. This is useful for bringing back
a natural-sounding tonal balance to an overly bright or buzzy wavetable
without resorting to removing the highs altogether.
Shift Octave Up
Spread all bins (1->2, 2->4, and so on) so that the resultant waveform is
doubled in frequency.
Shift Octave Down
Same as above, but in reverse.
Repeat Bin Group
(Start to Cursor Pos)
Create copies of the harmonics from the start to the current cursor location,
repeating all the way through the spectrum.
Draw Even Harmonics
Only
Prevent the mouse from operating on odd-numbered bins.
Draw Odd Harmonics
Only
Prevent the mouse from operating on even-numbered bins.
Snap Vertical Draw to
Quarters
Snap vertical mouse drawing to exactly 0%, 25%, 50%, 75% and 100%.
Scale Freq Values by
Bin Index
Amplitude draw/react proportionally to the selected bin, exaggerating higher
harmonics visually. Using this feature, a proper sawtooth will be a horizontal
line draw instead of an exponential curve across the harmonics.

<!-- page 281 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
281
Managing Frames (Subtables)
You can use the Wavetable Editor to perform a wide range of operations on frames within a wavetable.
Managing Frame (Subtables)
Exploring Common Frame Operations
You can access the most commonly used frame operations through a series of buttons and menus
directly below the frame display.
Frame (Subtable) Buttons and Menus

<!-- page 282 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
282
Copying and Pasting Frames
You can copy one or more frames and paste the contents to a new location in the wavetable.
Start by selecting the frames you want to copy. You can click to select a frame, and Shift-click to extend
your selection. Your selection needs to be contiguous.
Selecting Frames to Copy
Click the COPY button.
Select the starting frame of the destination and click the PASTE button.
The frames appear starting in the target frame.
Pasting Frames into the Wavetable
Inserting and Removing Frames
You can use the REMOVE menu to insert or delete frames. You can also initialize all frames using this
menu.
Click the
 button and choose an option using the menu that appears. The following table
describes the menu options:
Menu Item
Description
Init All (Default)
Clear all frames/interpolations. The wavetable is brought to its default state
(a single saw frame).

<!-- page 283 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
283
Menu Item
Description
Insert (at current
index)
Add an additional frame to the wavetable set, inserted after the currently-
selected frame. This has the same effect as pressing the + button below the
waveform.
Remove (current
index)
Remove the currently selected frame. This is the same function as pressing
the - button (below the waveform).
Remove:
multiselection
Remove multi-selected frames (Shift-click in the thumbnail area to multi-
select a range of frames).
Remove: beginning->
selected
Remove the frames from the beginning (1) through the selected frame.
Remove: selected->
end
Remove the frames from the selected frame through to the end.
Remove All (except
Selected)
A “crop” feature, useful when you decide that a single frame or certain range
(multiselect) is all you want to keep.
Reduce to
Thins the number of frames; helpful to easily keep only every nth frame.
Sorting Frames
You can use the SORT menu to reorder existing frames based on a spectral property. Keep in mind that
you can also manually sort frames by dragging the frames left and right within the thumbnail display.
Click the
 button and choose an option using the menu that appears. The following table
describes the menu options:
Menu Item
Description
Sort by spectrum
(Peak Spect)
Sort frames based on which frame has the highest peak frequency bin.
Sort by spectrum
(Average Spect)
Sort frames based on where the average spectral content exists (sum of all
frequencies).
Sort by spectrum
(Peak Amount)
Sort frames by the highest overall peak (concentrated frequency energy).
Sort by spectrum (
Num w/Spect)
Sort frames by how many frequency bins contain energy (spectral
complexity).
Sort by spectrum
(Highest w/Spect)
Sort frames by the highest frequency bin to contain spectra. This should
work well for filter sweeps, for instance.
Sort by spectrum
(Fundamental Amt.)
Sort frames by the amount of energy in the fundamental. When in doubt, try
this sort first.
Sort Randomize
Randomize the order of the table indices.
Reverse Entire Table
Order
Reverse all frames in the table. This is useful if you decide that you want the
table order to become bright-to-dull instead of dull-to-bright, for instance.

<!-- page 284 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
284
Using the Formula Parser
Use the formula parser to generate a wavetable (single frame or entire wavetable set) from a
mathematical formula. You can use the Formula presets menu containing multiple examples to get you
started.
See “Using the Formula Parser” chapter for more information.
Exploring the Menu Commands
The Wavetable Editor features a set of menus that allow you to quickly and easily manipulate the
waveforms.
Wavetable Editor Menu

<!-- page 285 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
285
Importing a Wavetable
You can import a wavetable into the Wavetable Editor.
Click the
 button, and choose an import option in the menu that appears.
A dialog appears allowing you to select a file to load (which overwrites the wavetable set you are
currently editing). Refer to the “Importing Audio” chapter for a detailed description of the options in this
menu.
Keep in mind that you can also drag-and-drop waveforms directly from the macOS Finder or Windows
Explorer. This is often a more convenient way to import sounds.
Exporting a Wavetable
You can export a wavetable from the Wavetable Editor.
Click the
 button, and choose an export option in the menu that appears.
The following table describes the available options:
Menu Item
Description
Export All As 8-bit
(.256)
Export the wavetable in 8-bit format. This saves the wavetable using a file
format compatible with certain hardware modular synthesizers (such as
Wiard and Piston Honda).
Export All As 16-bit
(.wav)
Export the wavetable in 16-bit format. This saves the file in WAV format,
mono, 16-bit, 44100 Hz, 2048 samples per subtable.
Note that additional header information for interpolation mode and
interpolation tables are not saved as part of the WAV data.
Export All As 32-bit
(.wav)
Export the wavetable in 32-bit format. This saves the file in WAV file format,
mono, 32-bit, 44100 Hz, 2048 samples per subtable.
Note that additional header information for interpolation mode and
interpolation tables are not saved as part of the WAV data.
Export All As Single-
Cycle Waves
Export the wavetable as a set of individual single-cycle WAV files.
Export Selection
Export and save a wavetable using the Serum file format (a WAV file with
extra header information). This is similar to the other save commands, except
that only the selected frames are included in the file.
If you don’t see a format compatible with your needs, you can convert WAV files to an alternate format
using a third party application or utility.

<!-- page 286 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
286
Single Menu
The SINGLE menu contains process functions that alter the currently selected (visible) frames.
Menu Item
Description
Normalize
Adjust the waveform to maximum-scale amplitude.
Remove DC Offset
Remove any DC (up/down bias to the waveform). This is typically not
needed.
Flip Vertical (Polarity
Invert)
Perform a polarity invert operation (often somewhat mistakenly called
“phase invert”).
Flip Horizontal
(Reverse)
Reverse the audio. As a short looping wave, it probably won’t sound
reversed in most situations.
Shift Horizontal to
Zero Crossing
Nudges/wrap the wave so the edges fall on  a zero crossing. This isn’t
essential, but might be useful for applying fades or matching phase among
multiple waveforms.
Init (Silence)
Replace the current table with silence.
Fade Edges (Grid Size)
Create a fade in at the left edge and a fade out at the right edge based on
the width of the horizontal grid size (set in the lower right).
X-Fade Edges (Grid
Size)
Similar to above, but instead of fading to the center line, the edges fade to
each other.
Filter (Grid Size)
Completely remove upper harmonics using a low pass filter. A lower grid
size means more low pass filtering. You can achieve the same low pass filter
effect using the FFT area (Ctrl/right-click > Clear HF).
Since this uses FFT, it is infinitely steep; you might notice some DC shift as
all DC offset is removed.
Sample Redux at Grid
Size
Perform a sample rate reduction for a lofi sound.
The grid size is not used in a literal way but as a means for specifying an
amount (larger number offers more sample redux).
Send to Noise
Oscillator
Convert the currently selected frame to a single cycle waveform and import
the waveform into the noise oscillator.

<!-- page 287 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
287
All Menu
The ALL menu offers process functions, similar to the SINGLE menu, but applying to all frames (1-256)
in the wavetable.
Menu Item
Description
Normalize Each
(Gained Separately)
Individually normalize every frame to its own peak maximum.
Normalize Same (Max
From All Frames)
The entire wavetable set is scanned for a peak level, and the same gain
amount is applied to each frame.
Remove DC Offset
Remove any DC (up/down bias to the waveform). Noet that this is typically
not needed.
Flip Vertical (Polarity
Invert)
Perform a polarity invert operation (often somewhat mistakenly called
“phase invert”).
Flip Horizontal
(Reverse)
Reverse the audio. As a short looping wave, it probably won’t sound
reversed in most situations.
Fade Edges (Grid Size)
Create a fade in at the left edge and a fade out at the right edge based on
the width of the horizontal grid size (set in the lower right).
X-Fade Edges (Grid
Size)
Similar to above, but instead of fading to the center line, the edges fade to
each other.
X-Fade Edges (16
Samples)
Same as above, but only a micro-fade on the edges (16 samples is small!).
Filter (Grid Size)
Completely remove upper harmonics using a low pass filter. A lower grid
size means more low pass filtering. You can achieve the same low pass filter
effect using the FFT area (Ctrl/right-click > Clear HF).
Since this uses FFT, it is infinitely steep; you might notice some DC shift as
all DC offset is removed.
Remove Fundamental
(HPF)
Remove the lowest frequency (pitch), effectively akin to zeroing the top-left
bar of the FFT display (fundamental) but for all tables.
The formula “z=(q>1)?in:0” would also yield the same result, or simply
“(q>1)?in:0” if you want to only apply to the currently visible frame.
Remove Low Spectra
(Grid Size)
Remove the lowest frequency bins, somewhat similar to a high-pass-filter.
Remove Low Phases
(Grid Size)
Zero the phases on the lowest frequency bins.
Sample Redux at Grid
Size
Perform a sample rate reduction for a lo-fi sound.
The grid size is not used in a literal way but as a means for specifying an
amount (larger number offers more sample redux).

<!-- page 288 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
288
Menu Item
Description
Resize Tables to be
Half (2x Total
Number)
Divide every frame in half to become two frames. This doubles the number
of frames (so you shouldn’t use this if you have more than 128 frames).
Resize Tables to be
Double (½ Total
Number)
Every frame is grouped with the following frame. This is useful if you notice
every second frame similar after a WAV import (the frequency was detected
an octave too high).
Create PWM from
This Table to All
Remove all frames except the current frame and create a PWM shift across
all 256 frames.
There is a real time PWM effect using the WARP knob (main panel), but this
way you can perform pulse width modulation and use another warp effect.
Nudge All Phases for
Fundamental to 50%
Preserve the phase of the lowest frequency (fundamental) across various
waveforms.
Set Spectra (This
Frame to All)
Apply FFT bins (spectrum) from the current frame to all frames.
Set Phases (This
Frame to All)
Apply the FFT phase information from the current frame to all frames. This
is useful to make all frames match in phases beyond just the fundamentals,
for example, solid/consistent sound during morphing.
Set Spectra from
Other Osc
Remove the relative amount of harmonic content contained in the other
oscillator.
Set Phases from
Other Osc
Apply the FFT phase information from the other oscillator frames (A<>B) to
the frames of the visible oscillator.
Subtract Spectra from
Other Osc
Subtract harmonic content based on the harmonic content of the other
oscillator’s wavetable.
Blur Spectra -
Adjacent Bins
(Grid Size)
Interpolate (smooth) the harmonic content between adjacent harmonics. The
grid size value determines how many neighboring harmonics are factored
into the smooth operation.
Blur Phases -
Adjacent Bins
(Grid Size)
Interpolate (smooth) the phase content between adjacent harmonics. The
grid size value determines how many neighboring harmonics are factored
into the smooth operation.
Blur Spectra -
Adjacent Frames
(Grid Size)
Interpolate (smooth) the frequency content between adjacent frames. The
grid size value determines how many neighboring harmonics are factored
into the smooth operation.
Blur Phases -
Adjacent Frames
(Grid Size)
Interpolate (smooth) the phase content between adjacent frames. The grid
size value determines how many neighboring harmonics are factored into
the smooth operation.
Shift Horizontal to
Zero-Crossing
Move the audio data to the right to have the left edge of the frame begin
at a zero crossing (where the waveform polarity changes from negative to
positive).

<!-- page 289 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
289
Morph Menu
Use the MORPH menu to create or remove interpolation frames between existing frames. Note that
you must have more than 1 and less than 256 frames.
After selecting a morph item from the menu, you’ll notice that there are now 256 frames in the WT
POS selector. This is because all empty wavetable slots are now filled with interpolated (blended)
waveforms of the neighboring tables.
You’ll also notice that the thumbnails no longer display “1, 2, 3”, and so on, but rather “1, 17, 33” (or
similar). This is because the intermediate tables (for example, 2-16 in this example) contain the newly-
created morph tables.
You’ll see these intermediate tables in the waveform area as WT POS is adjusted, but they don’t exist as
thumbnails.
After you exit the Wavetable Editor and return to the main panel, you’ll also notice the interpolated
frames appear gray in the 3D wave overview (whereas green shows the “real” frames, and yellow shows
the currently-selected frame).
Menu Item
Description
Morph - Crossfade
Create interpolated frames by crossfading the neighboring frames together.
This is the recommended default, and what traditional wavetable synths do.
Morph - Spectral
Use the spectral and phase content of neighboring frames to re-synthesize
the interpolated frames. This is what additive synthesizers do.
Morph – Spectral
(Zero Fund. Phase)
Same as Morph - Spectral, but the phase content of the fundamental is
zeroed for all source frames. This way the lowest frequency does not shift/
rotate between frames.
Morph – Spectral
(Zero All Phases)
Same as Morph - Spectral, but all phase content is discarded. This might alter
the sound of the source content drastically, and therefore can sometimes be
undesirable.
However this option also creates the smoothest transitions between frames
since no frequencies need to shift phase.
Remove Morph Tables
Revert back to how things were before interpolation was applied.
Note that clicking “Undo” might be the better choice for reversing the morph
since, in the case of the spectral (zero-phase) modes, the two zero-phase
choices destructively alter the source tables.

<!-- page 290 -->

﻿
Using the Wavetable Editor
Serum 2 User Guide
290
Saving Wavetables
If you have modified one or more frames in the Wavetable Editor, the wavetable name changes to a
tinted background indicating that the wavetable has been modified but not yet saved to storage.
Wavetable Modified
Right-click Custom and choose Save Table in the menu that appears.
Choose the file name and location in the dialog that appears.
Save your wavetables in the User folder and, if at all
possible, do not overwrite factory wavetables (or else the
presets may sound different). Also, when in doubt, always
pick a new name.
Note that you do not need to save your wavetables explicitly. Serum
always saves changes you make to wavetable data inside a preset (your
song) unless it is a factory wavetable. This uses some hard disk space
— how much depends on how many frames you use in the wavetable,
from 8k to 4 Megabytes
The benefit, however, is that you can exchange presets with others, or
open your song in the future, without having to worry about table file
management. The only reason to explicitly save a wavetable is to have it
appear in the Wavetable menu.
Saving a Wavetable