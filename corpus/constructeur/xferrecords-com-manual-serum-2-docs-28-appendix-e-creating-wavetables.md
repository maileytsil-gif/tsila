---
titre: "xferrecords com manual serum 2 docs — Appendix E: Creating Wavetables (p. 346-347)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Appendix E: Creating Wavetables


<!-- page 346 -->

Serum 2 User Guide
346
Appendix E: Creating Wavetables
This appendix provides additional information about creating wavetables. Refer to “Using the Wavetable
Editor” on page 274 for detailed information about how to create your own wavetables.
What Makes for a Good Wavetable?
Like a good song, creating a good wavetable is about getting that careful balance between consistency
and contrast. Too much consistency or repetition and things won’t feel like much of a journey. Too much
contrast and it’s difficult to draw a connection between random events (like turning the dial on the radio
feels disconnected and hard to comprehend as intentional).
Good wavetables generally have the following basic characteristics:
•	 Contains many correlated frames
This typically is a sound with a lot of frames, but ones that fluidly work together (think of a pluck
string that decays across many cycles). In general, there might be a lot of individual cycles, but they
all go together well and relate nicely with each other.
Another example would be a synthesizer sample. You want many cycles so it doesn’t feel too
“steppy,” however all the frames should feel as part of a collection (a similarity/sweep across them).
•	 Contains few frames
Many of the factory presets in popular wavetable synths contain only four or five cycles. This
provides some variety within the table, but not so many waveforms that it feels disconnected or
crazy.
Table Ordering
It typically makes sense to have the frames progress from dull to bright, or vice-versa. You may have a
situation where you want the spectrum to peak somewhere in the middle, but probably not.
You can drag the thumbnails at the bottom of the Waveform Editor to rearrange them. This way, when
you move the WT POS knob, it feels as if you’re traveling in a straight line, instead of in a zig-zag
fashion (spectrally speaking).

<!-- page 347 -->

﻿
Appendix E: Creating Wavetables
Serum 2 User Guide
347
Interpolation
If you have four frames and automate the WT POS knob, you’ll hear four discrete tones immediately
jumping from one to the next. This is typically undesirable.
In the Wavetable Editor, you can select MORPH > Morph - Crossfade. This is what many wavetable
synths do automatically in every preset wavetable. However, there are times when you might prefer
discrete (non-interpolated) waveforms.
Creating Wavetables from Scratch
There are several ways to create source audio for a wavetable, including the following:
•	 Drawing
The grid size in lower-right determines snapping. Try different sizes such as 6 or 12 to bring out +7
and +19 harmonics.
•	 Drawing in FFT bins
Right-click in the bins for a pop-up menu with more options (including random, among others).
•	 Moving drawings up to FFT bins
Use the curved arrow near the top left and add a new table (using the > button in the lower left).
Then make some adjustments and repeat.
About four frames seem to be a popular number in many other software synthesizers.