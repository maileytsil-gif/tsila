---
titre: "xferrecords com manual serum 2 docs — Using the Filter Modules (p. 133-143)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Filter Modules


<!-- page 133 -->

Serum 2 User Guide
133
Using the Filter Modules
Serum features an advanced filter module that offers per-voice filtering of one or more oscillators.
Filters are one of the most powerful tools for shaping and sculpting sound, allowing you to modify the
frequency content of a sound, selectively emphasizing or reducing certain frequencies.
By controlling which parts of the sound’s spectrum are allowed to pass through and which are cut off,
you can use Serum’s filters to drastically alter a sound’s character, making it warmer, brighter, darker, or
even more aggressive.
Serum includes an extensive collection of filters, featuring numerous variations on low-pass, high-pass,
band-pass, notch, comb, and more. Combined with Serum’s extensive modulation capabilities, you can
use the filters to create a range of sounds including rhythmic sweeps, evolving pads, and even vocal-like
formant sounds.
With playful tweaking and clever modulation, you can use the filter module as a creative playground,
exploring endless possibilities for sound manipulation and transformation.
Serum Filter Modules

<!-- page 134 -->

﻿
Using the Filter Modules
Serum 2 User Guide
134
Exploring the Filter Modules
To enable or disable a filter module, click the corresponding power button. This offers you an easy way
to disable a filter entirely, if needed.
Enabling Filter 1 and 2
Filter 1 and 2 Enabled
Routing an Oscillator
To route an oscillator to a specific filter module, select the
corresponding switch:
•	 S - SUB oscillator
•	 A - OSC A
•	 B - OSC B
•	 C - OSC C
•	 N - NOISE oscillator
Filter Routing

<!-- page 135 -->

﻿
Using the Filter Modules
Serum 2 User Guide
135
Filter Type
To choose a filter type, click the current filter setting. A
pop-up menu appears showing a hierarchical collection of
available filter types.
Use the < > arrows to conveniently switch between filter
types without having to open the menu.
Alternatively, hover over the menu and use the mouse wheel
to quickly rotate through menu options.
Filter Types and Var Parameter Functions
The following table describes the available filter types:
Category
Filter Type
Description
Var Function
Normal
MG Low
6/12/18/24
Ladder Low-Pass Filter.
The number represents
the db per octave slope of
the filter.
The topology is based on
filters made famous in
classic Moog synthesizer
designs.
FAT: Add saturation to the
filter resonance signal path.
This has a taming effect on
filter resonance and enriches
the resulting harmonic
content.
Low 6/12/18/24
State-Variable Low-Pass
Filter.
The number represents
the db per octave slope of
the filter.
FAT: Add saturation to the
filter resonance signal path.
This has a taming effect on
filter resonance and enriches
the resulting harmonic
content.
Filter Menu

<!-- page 136 -->

﻿
Using the Filter Modules
Serum 2 User Guide
136
Category
Filter Type
Description
Var Function
Normal (cont.)
High 6/12/18/24
State-Variable High-Pass
Filter.
The number represents
the db per octave slope of
the filter.
FAT: Add saturation to the
filter resonance signal path.
This has a taming effect on
filter resonance and enriches
the resulting harmonic
content.
Band/Peak/Notch
12/24
State-Variable Band/Peak/
Notch Filter.
FAT: Add saturation to the
filter resonance signal path.
This has a taming effect on
filter resonance and enriches
the resulting harmonic
content.
Multi
LH/LB/LP/LN/
HB/HP/HN/BP/
BN/PP/PN/NN
Dual SVF Filters.
The first letter is primary,
the second letter is
secondary (for example,
BP is Band+Peak).
The resonance control
applies equally to both
filters.
FREQ: Set the cutoff
frequency of the second SVF
filter.
LBH/LPH/LNH/
BPN
Morphing SVF filters (for
example, Lowpass <->
Bandpass <-> Highpass)
MORPH: Smoothly transition
between the filter states.
Flanges
Cmb L/Flg L/Phs L
Comb/Flanger/Phaser
with a low-pass filter in
the internal feedback
circuit.
Set the MIX knob to 50%
for best results.
LP FREQ: Set the cutoff
frequency of the low pass
filter affecting the internal
feedback circuit.
Cmb H/Flg H/Phs
H
Comb/Flanger/Phaser
with a high-pass filter
in the internal feedback
circuit.
Set the MIX knob to 50%
for best results.
HP FREQ: Set the cutoff
frequency of the high-pass
filter affecting the internal
feedback circuit.
Cmb HL/Flg HL/
Phs HL
Comb/Flanger/Phaser
with a high pass + low
pass filter in the internal
feedback circuit.
Set the MIX knob to 50%
for best results.
HL WID: Expand the
bandwidth allowed through
the internal feedback circuit
around the filter cutoff
frequency.

<!-- page 137 -->

﻿
Using the Filter Modules
Serum 2 User Guide
137
Category
Filter Type
Description
Var Function
Misc
Low/Band/High
EQ 6/12
Filters with morphable
frequency responses.
The number represents
the db per octave slope
of the filter. Resonance
has no effect on 6 db per
octave variations.
DB +/-: Increase or decrease
gain of the pass band.
Extreme settings morph the
frequency response of the
filter, for example, the Low
EQ 12 filter blends from a
high pass (when db gain is set
to 0) to a low shelf.
Ring Mod/Ring
Modx2
Apply ring modulation
to the input signal at
a frequency set by the
cutoff control.
The x2 variant features a
second ring modulation.
SPREAD (only available in the
x2 filter variant):
Control the distance between
the first and second ring
modulator frequencies.
SampHold/
SampHold-
Apply a sample-and-hold
distortion.
The minus variant
outputs the difference
of the sample-and-hold
distortion and the input
signal.
N/A
Combs/Allpasses/
Reverb
Generate phase smearing
through combinations of
delays and all-pass filters.
DAMP: Soften the feedback
path of the filter.
French LP
Unique distorting low-
pass filter.
The filter responds non-
linearly to input signals.
BOEUF: A secondary
resonance control.
Combinations of the primary
and Boeuf resonance values
produce unique results.
German LP
“Zero-Delay Feedback”
low-pass filter.
N/A
Add Bass
Phase-rotated low pass
filter with a touch of drive.
Not a typical synth filter,
but maybe you’ll find a
use!
THRU: Add a phase-rotated
dry signal.

<!-- page 138 -->

﻿
Using the Filter Modules
Serum 2 User Guide
138
Category
Filter Type
Description
Var Function
Misc (cont.)
Formant-I/II/III
Formant ‘vowel’ filters.
The CUTOFF knob
morphs between various
formants. This is great
for adding vocal-like
characteristics to patches.
FORMNT: Shift the formants
to generate a broader
range of possible filter
permutations.
Bandreject
Attenuate a specific range
to very low levels. It has
the opposite effect of a
band-pass filter.
WIDTH: Adjust the
overall width of the filter’s
attenuated “notch”.
Dist.Comb 1/2 LP/
BP
Combination comb filter
and pass filter.
The comb filter (version
1 is a positive feedback
comb filter; version 2 is a
negative feedback comb
filter) is applied to the
feedback path of the pass
filter.
COMBFRQ: Set the
frequency of the comb filter.
Scream LP/BP
A high-feedback filter
effect that can have a
scream-like quality.
SCREAM: Set the cutoff
frequency for the feedback
circuit.
The DRIVE knob affects
the amount of scream (raise
DRIVE above 50% to hear
the scream).
New
Wsp
Circuit model of a classic
synth filter that buzzes
(and burbles!).
MORPH: Blend between
LPF/Notch/HPF.
DJ Mixer
Xfer freeware DJM filter
plugin.
N/A

<!-- page 139 -->

﻿
Using the Filter Modules
Serum 2 User Guide
139
Category
Filter Type
Description
Var Function
New (cont.)
Diffusor
All-pass diffusor stage
for making things sound
phasey and blurry in a
cool way.
STAGES: Specify how many
APF stages are used.
MG Ladder
Clean circuit model of
classic transistor ladder
VCF.
SMOOTH: Slow the rate
at which the cutoff is
modulated.
Acid Ladder
Circuit model of a diode
ladder VCF ubiquitous in
acid music.
SMOOTH: Slow the rate
at which the cutoff is
modulated.
EMS Ladder
Clean circuit model of the
VCF that makes Dr. Who
sounds.
SMOOTH: Slow the rate
at which the cutoff is
modulated.
MG Dirty
MG Ladder, but all the
distortion is there and you
are overdriving the circuit.
PAIN: How far you’re holding
a lighter from the circuit
board (this is physically
correct; not a joke).
PZ SVF
Drawable filters.
SMOOTH: Slow the rate
at which the cutoff is
modulated.
Comb 2
Comb filter with crazy
resonance and stuff.
FRQ2
Exp MM
Multimode (LPF/Notch/
HPF) output from the
classic synthesizer
expander module.
MIX: blends between LPF/
Notch/HPF.
Exp BPF
BPF output from the
classic synthesizer
expander module.
N/A

<!-- page 140 -->

﻿
Using the Filter Modules
Serum 2 User Guide
140
Filter Display Options
You can set display options for the filter to show
frequency, FFT, and phase information, as needed.
Right-click the filter display and choose an option using
the context menu.
The following table describes the available display options:
Option
Display
Description
Frequency
Response
Shows how the filter affects the amplitude of
different frequencies in the audio spectrum,
visualized as a graph with frequency on
the horizontal axis and amplitude (gain or
attenuation) on the vertical axis.
Use this view to understand which frequencies
are being boosted, attenuated, or left unaffected
by the filter.
Frequency Re­
sponse & FFT
Combines the filter frequency response curve
with a real-time FFT (Fast Fourier Transform)
analysis of the audio input. The FFT displays the
actual frequency content of the signal, overlaid
with the filter’s effect.
Use this view to show a dynamic visualization
of both the audio signal spectrum and how the
filter is shaping it in real time, allowing for more
precise adjustments.
Filter Display Menu

<!-- page 141 -->

﻿
Using the Filter Modules
Serum 2 User Guide
141
Option
Display
Description
Phase Re­
sponse & FFT
Shows how the filter affects the phase of
different frequencies, indicating the degree of
phase shift applied to each frequency in the
signal, alongside the real-time FFT of the audio.
Use this view to understand phase-altering
filters and how they might impact phase-
sensitive tasks like stereo imaging or when
combining multiple signals.
You can quickly cycle through the different display modes by Option-clicking (macOS) or Alt-
clicking (Windows) in the filter display.
Setting Filter Parameters
You can set a range of filter parameters, including the cutoff, resonance, drive, pan, mix, and level. In
addition, different filter types offer a variable parameter depending on context.
Cutoff
Use the CUTOFF knob to set the primary cutoff frequency for the filter (with just a couple exceptions,
such as vowels for formant filters).
Use the
 (keytrack) switch to offset the cutoff using MIDI notes. With most filter types, one
octave of MIDI corresponds to precisely one octave of filter frequency control.
If the keytrack switch is enabled, this tracks the pitch of the first oscillator (OSC A, OSC B,
or OSC C) that has pitch tracking enabled (including portamento).
If none of the oscillators have pitch tracking enabled, the filter tracks the input MIDI note
number.

<!-- page 142 -->

﻿
Using the Filter Modules
Serum 2 User Guide
142
Resonance
Use the RES knob to set the resonance (feedback) of
the filter circuit.
You can graphically adjust the filter cutoff and
resonance (in combination) by clicking and
dragging in the filter display.
This is a quick way to experiment with filter
settings in your sound design.
Drive
Use the DRIVE knob to increase the gain into the filter
circuit and can impart some coloration (mild distortion)
to the sound.
Right-click the knob and choose Clean Mode in the
context menu to have the filter pre-gain stage the filter
input -24 dB (with a +24 dB boost post-filter).
This reduces saturation and input drive in the filter
models.
Fat (and Others)
By default, the FAT knob appears when the filter type is MG Low 6 (as part of the Init preset, for
instance). However, this knob changes based on the filter type you select using the menu.
Refer to the table above for details about the knob that appears here.
Graphical Adjustments
Drive Clean Mode

<!-- page 143 -->

﻿
Using the Filter Modules
Serum 2 User Guide
143
Pan
Use the PAN knob to create a cutoff offset for the left and right signals. At the default setting of 50%
(12 o’clock) this knob has no effect. When turned to the left (counter-clockwise) the left channel cutoff
increases, and the right channel cutoff decreases.
When turned to the right (past 12 o’clock clockwise), the opposite happens; the left cutoff decreases
and the right channel cutoff increases.
Mix
Use the MIX knob to control the wet/dry amount for the filter. The default (100%) means 100% wet.
Level
Use the LEVEL slider to adjust the filter output level (in decibels).