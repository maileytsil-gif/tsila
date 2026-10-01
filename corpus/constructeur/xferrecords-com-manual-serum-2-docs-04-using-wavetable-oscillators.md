---
titre: "xferrecords com manual serum 2 docs — Using Wavetable Oscillators (p. 37-57)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using Wavetable Oscillators


<!-- page 37 -->

Serum 2 User Guide
37
Using Wavetable Oscillators
As with the original Serum, wavetable oscillators remain at the heart of sound generation in Serum 2.
Unlike many wavetable synthesizers, however, Serum tables are multi-cycle, offering a greater variety of
sounds.
Serum oscillator playback has been carefully constructed to give you a high-frequency representation to
the limits of the human ear, without the audible aliasing artifacts (Nyquist reflection) commonly found
on most wavetable synthesizers.
While this requires more CPU during both load and run-time, Serum’s advanced SSE (Streaming SIMD
Extensions) optimizations effectively help to minimize the CPU expense. We think you’ll agree that the
benefits in sound purity make it worthwhile.
Oscillator Panel (with 2D Waveform)

<!-- page 38 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
38
What is a Wavetable?
A wavetable is a small amount of digital audio (sample data or waveform) that is played back in a looping
fashion.
The frequency (pitch) of the resulting note is determined by the rate (the speed between the repeats)
at which the waveform is played. The tone (timbre and harmonics) of the sound is determined by the
content of the waveform.
Anatomy of a Serum Wavetable
Wavetables in Serum consist of up to 256 subtables, or single-cycle waves (referred to hereafter as
frames). You can think of this as (up to) 256 discrete waveforms joined together end-to-end in the
parent file on disk.
In normal circumstances, you can hear one of
these 256 frames at a time. However, if you assign
automation to the WT POS knob, the sound
starts to glide through the various frames, thereby
becoming animated.
The wavetable in the illustration contains six
frames, with yellow highlighting the current frame
and green showing the five other frames.
If you increase the number of unison voices and
turn up the unison WT POS control (in the unison
settings), you’ll hear multiple frames (subtables)
playing back simultaneously.
Strictly speaking, when Serum loads a wavetable, it uses 2048 samples for a frame
(subtable) of the wavetable set. This means that the maximum file size is 2048 (samples) x
256 (frames) x 32 (bits), which is exactly 2 megabytes.
However, most wavetable files will not be this large. A good sounding wavetable can consist
of just a few frames. The remaining frames can be interpolated (in the Wavetable Editor) to
allow for smooth-sounding transitions.
These interpolated frames are generated through crossfading (mix blend) or spectral
morphing (frequency + phase blend). These frames are computed at load time; Serum
embeds the interpolation type rather than the interpolated waveforms (reducing disk
space).
Wavetable Frames

<!-- page 39 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
39
Using Wavetables
Serum features three multi-purpose oscillator
modules, as well as dedicated NOISE and SUB
oscillators (discussed separately later).
You can use any or all of the three oscillators in
wavetable mode, taking advantage of advanced
display and editing capabilities to help you get the
greatest sonic possibilities.
This section describes how to use wavetables in
Serum.
Exploring the Waveform Display
OSC A, OSC B, and OSC C all display a green
waveform area with two viewing options: 2D and
3D.
Clicking on the waveform toggles between the
two views.
In 2D mode, you see a single-cycle (frame) of the
selected wavetable. You can use this view to see
the warp feature in real-time (described later in
this chapter).
The 3D view, in contrast, displays all frames
(subtables) at-a-glance, with each frame
represented by a green horizontal waveform,
interpolated frames in gray, and the currently-
selected frame in yellow.
Notice that the current frame number (wavetable
position) appears in the lower left of the waveform
area.
OSC A in 2D View
OSC A in 3D View (with wavetable position
number)

<!-- page 40 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
40
Choosing a New Wavetable
You can load a new wavetable by clicking the drop-
down menu and choosing an option.
Click the < > arrows to quickly navigate to the
previous and next wavetable respectively.
Alternatively, hover over the menu and use the
mouse wheel to quickly rotate through wavetable
options.
Editing a Waveform
You can take a closer look at a wavetable by hovering over the top-right corner of the waveform display
and clicking the
 button.
Note that the button is initially dimmed
 until
you hover directly over it.
Doing so opens the Wavetable Editor, presenting
you with a rich set of tools to modify and
manipulate the wavetable in multiple ways.
Click the
 button to close the Wavetable
Editor.
You’ll learn all about the Wavetable Editor and its
many features in “Using the Wavetable Editor” on
page 274.
Choosing a Wavetable
Wavetable Editor Button

<!-- page 41 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
41
Wavetable Editor
Phase
Use the PHASE control to specify where the
oscillator begins playing back when a note is
triggered.
It is the same concept as sample start on a sampler
(except the “sample” is a very small waveform).
Since oscillators tend to be reasonably high
frequency, you may not notice a difference when
changing this knob.
In particular, if the adjacent RAND control is up
considerably, you probably won’t hear a difference
when adjusting the phase (because RAND alters
the phase on each new note).
Oscillator Phase Control

<!-- page 42 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
42
Having said that, the effect can be very pronounced in the following scenarios:
•	 With a smooth waveform and fast-attack envelope
If your wavetable is a sine wave, for instance, and the ENV 1 attack is very fast (set to a small
value), you will hear a click at the beginning of the sound if the PHASE control is set to a non-zero
crossing (0% or 50% represent the zero crossings in a default sine wave).
•	 Using two or more oscillators with the RAND setting off
The interaction between two or more oscillators can be very noticeable due to phase cancellation.
Adjusting the start time of one of the oscillators results in a different tone.
If the oscillator waveform display is in 2D (single table view), moving the PHASE control causes a
yellow line to appear indicating where the note onset will occur.
Randomizing the Phase
Use the RAND (random) control to alter the PHASE knob value by a random amount for each new
voice.
You might want to randomize the start phase of an
oscillator for the following reasons:
•	 To provide a different start or click/thump to
each note
•	 To provide a random tone to each note (when
layering multiple oscillators), as the phase
cancellation between the oscillators varies
with each new note
•	 To reduce or remove the “laser zap” effect
when unison (slightly detuned) notes are
triggered
Oscillator Random Control

<!-- page 43 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
43
For example, do the following to hear the effects of the RAND control:
1.	Set PHASE to 0 degrees.
2.	Set RAND to 0 percent.
3.	Raise the UNISON number to a high value, such as 8.
4.	Lower the DETUNE slightly, for instance, to 10 o’clock (a value of 0.10).
At this point, you should hear a “laser zap” phasing sound resulting from the unison oscillators all
starting together in phase, and slowly drifting apart from their detune.
Every time you trigger the note, you’ll hear the same laser zap sound since the voice phases are
restarting. While this can sometimes be cool, generally this is undesirable as the sweeping sound can be
distracting.
As you raise the RAND control, notice how the effect becomes less pronounced as a random phase
offset is introduced into each voice separately. By the time you reach 100% using the RAND control,
you will no longer hear the “zap” sound.
Phase Legato
In the case of the “laser zap” phasing sound produced in the previous section, the default behavior is
that when Legato is disabled (in the VOICING section) and a voice is stolen, the wavetable oscillator
phase does not reset at note on. Therefore, you won’t hear that “laser zap”.
Also, in cases when Legato is enabled and Serum is playing polyphonically (including when not stealing
a voice), the wavetable oscillator phase does reset at note on. This results in you hearing the zap even
though legato is enabled and you want a smooth transition between notes.
The default behavior is how Serum 1 works, and is intended to avoid clicks at note on, which would be
particularly evident with a simple sine wave.
However, with the above settings, we want the opposite behavior. You can toggle this by right-clicking
the PHASE control and choose Phase Legato in the context menu.

<!-- page 44 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
44
Setting Phase Memory
You can set the phase memory for the wavetable using the phase memory drop-down menu. The phase
memory specifies how phase and phase randomization should be determined for new notes.
Phase Memory Menu
The following table describes the options:
Option
Description
All Voices
New notes use the PHASE and RAND control settings for all voices. This is
the default setting.
Contiguous
New notes continue with the phase of the previous note.
Per Voice
New notes start with the same editable phase each time.
If you set phase memory to Per Voice while one or more notes are sounding, Serum captures
the current phase from the most-recently sounded note.

<!-- page 45 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
45
Wavetable Position
Use the WT POS knob to set the position within
the wavetable. In other words, the knob selects
the frame (subtable) that is currently audible.
Setting the WT POS knob to the minimum setting
of 1 selects the first frame (highlighted in yellow).
Remember, yellow always indicates the currently-
selected (audible) frame.
Right-click the WT POS knob and choose Smooth
Interpretation in the menu to allow smoother
waveform transitions without being destructive.
This helps keep the wavetable intact while
morphing smoothly between positions.
Unison
Use the UNISON control to set the number of unison voices, effectively “stacking” oscillators in a way
that is similar to playing multiple notes of the same pitch, but slightly detuned.
Click the field and drag to set the appropriate
value. You can also double-click the field and type
a value.
Serum allows you to stack up to 16 voices in
unison, but doing so can result in a more “cloudy”
sound and less like distinct voices. The classic
magic number for unison is 7.
Serum has a special capability that keeps the level
increase in check as you increase the number of
unison voices, effectively maintaining the volume
at the same level.
Note: Unison causes Serum to generate multiple
voices, raising CPU usage. The color of the
UNISON field changes as you increase the
number of unison voices as a reminder of the CPU
consumption.
Oscillator WT POS Control
Wavetable Unison Control

<!-- page 46 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
46
Click the
 button to display the unison
settings.
The wavetable unison settings appear.
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
•	 Super — Multiple voices are slightly detuned from each other but with
a special emphasis on creating a dense and powerful sound, often with
a slight stereo spread.
Use this mode to create a lush, wide sound, especially with supersaw
sounds, where the detuned voices give a rich, full sonic character.
•	 Exp — The detuning between voices increases exponentially as
you move away from the central pitch. This means that the spacing
between voices gets wider more quickly as you move outward,
creating a more dramatic spread compared to linear.
This mode can create unique, rich textures, especially for sounds that
need to be more aggressive or have a strong presence in a mix.
Wavetable Unison Settings

<!-- page 47 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
47
Setting
Description
MODE (cont.)
•	 Inv — The detuning behavior is inverted, with lower voices detuned
more sharply compared to higher ones.
Use this mode to create interesting phasing effects or to produce
sounds with a less conventional detuning profile.
•	 Random — Introduces a random element to the detuning of each
voice. Instead of being evenly spaced, the voices are detuned
unpredictably.
This can create a more organic or chaotic sound, ideal for achieving
textures that are less polished and more natural or experimental.
STACK
The unison stacking, which instructs Serum to not just duplicate the unison
voices at the same pitch but instead transpose or harmonically adjust the
voices.
You can choose from among the following options:
•	 Off — Do not stack the unison voices
•	 12 (1-3x) — Distribute voices between the original pitch and octave
transpositions, with a range 1-3 octaves higher
•	 12+7 (1-3x) — Distribute voices between the original pitch, fifth, and
octave transpositions, with a range 1-3 octaves higher
•	 Center-12 — Transpose the center voices down one octave
•	 Center-24 — Transpose the center voices down two octaves
WIDTH
The extent to which the unison voices are spread out across the stereo
field, determining how wide or narrow the resulting sound feels in a stereo
mix.
When you increase the width parameter, the unison voices are spread
farther apart in the stereo spectrum, placing some voices more to the left
and others more to the right. This creates a sense of space and a wider,
more immersive sound.
Conversely, decreasing the width narrows the stereo spread, making the
sound more centered and focused. This can be useful for sounds that need
to be more direct or fit better in a dense mix without dominating the stereo
field.

<!-- page 48 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
48
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
WT POS
The wavetable frame that the unison voice plays at a particular moment.
By modulating this position, you can morph through different waveforms,
creating dynamic, evolving sounds.
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
voices (1 if unison is set to an odd number of voices and 2 if set to an even number).
You can think of BLEND as a wet/dry mix between a unison (wet) and non-unison (dry) sound. The
default value of 75% is an even blend between all the voices. Note that this is only applicable when the
number of unison voices is greater than two.

<!-- page 49 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
49
Warp
Setting the warp allows you to manipulate the
playback (and sound) of the wavetable oscillator.
By default, warp is set to OFF (as displayed next
to the corresponding knob). Clicking the current
setting displays a menu from which you can
choose from among the available warp modes.
You can also use the < > arrows to conveniently
switch between different warp modes without
having to open the menu. After selecting a mode,
you can use the corresponding knob to set the
depth.
Note that if the waveform is in 2D view (with a
single frame visible), you can see how the warp
mode affects the waveform for Sync, Alt Warp,
and Distortion modes.
Exploring the Warp Modes
Serum offers an extensive set of warp modes.
As with many parts of Serum, the best way to
learn about them is through experimentation.
Wavetable Warp Control
Wavetable Warp Menu

<!-- page 50 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
50
The following table describes the available warp modes:
Category
Warp Mode
Description
Off
The warp function is turned off.
Sync
Synchronize wavetable playback to an internal oscillator that
restarts in sync with the original oscillator phase.
The warp control sets the pitch of the internal oscillator; when
increased, the harmonic content shifts upwards while retaining
the pitch of the original oscillator.
This can create a harmonious effect when the original and
internal oscillator relate by a whole-number ratio (1:2, 1:5, and
so on). Pitches outside of these values can cause a saw-wave
to form at the end of each cycle.
When you select Sync mode, a WARP Var fader control
appears directly below the menu. Use this to adjust the
smoothness of the sync from traditional “hard sync” to a
very soft “soft sync.”
Alt Warp
Bend +
Pinch (bend) the waveform inwards (towards the middle of the
wave cycle).
Bend -
Pull (bend) the waveform outward (towards the edges of the
wave cycle).
Bend +/-
Allow for both of the above, depending on WARP knob value.
A setting of 12 o’clock on the WARP knob (50%) represents
no change to the sound.
PWM
Push the entire waveform to the left. This is useful with square
wave type sounds, especially for the classic PWM sound (but
useful with other waveforms as well).
Asym +
Similar to Bend, but in this case bend the entire waveform to
the right instead of both halves of the duty cycle separately.
Asym -
Bend the entire waveform to the left.
Asym +/-
Bend the entire waveform to the left or right.
Flip
Create an instantaneous polarity flip (often called phase
inversion) on the waveform. The WARP knob determines
where in the duty cycle the flip occurs.

<!-- page 51 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
51
Category
Warp Mode
Description
Alt Warp
(cont.)
Mirror
Create a mirror-image of the waveform for the second half of
the duty cycle.
This has an “octaved” type of quality to the sound due to the
doubling of the waveform into both halves of the wave cycle.
For this setting, the WARP knob behaves similarly to the Asym
+/- mode, except on both halves independently.
Due to the mirroring of the waveform, this mode always has
an audible effect.
Remap 1
Custom remapping of the wave cycle. When you select this
option, a pencil button appears that you can use to open a
graph showing the way your waveform will remap.
A diagonal line from bottom-left to top-right indicates no
change to the waveform (y=x). The WARP knob determines
the strength of the remap, from 0 (y=x) to 100% (what you see
on the graph).
Remap 2
Represents mirrored remapping.
This is the same as Remap 1 but applies the graph to each
half the waveform independently. This allows for symmetric
remapping without the need to draw symmetric shapes on the
graph.
Remap 3
Represents sinusoidal remapping.
This is another remapping option that saves you from having
to draw fancy curves.
Remap 4
Represents a 4x remapping.
This is similar to Remap 2 (mirrored) but in this case the graph
applies four times. This creates a more busy sound, and can be
helpful when you want something nasty.
Quantize
Similar to sample-and-hold, that is, a sample rate reduction.
Compared to an SR Redux effect, this applies to the waveform
itself.
This causes the aliasing sound to follow the pitch perfectly
(instead of having that “same ringing pitch on all notes” quality
that a redux effect creates).
Odd/Even
Proportionally vertically scale the waveform. Use this to emit
only the odd or even harmonics from the signal or a mixture of
the two.
At 50%, you have the original signal. At 0%, you hear only the
odd harmonics. At 100%, you hear only the even harmonics
(which creates an octaving effect since the first harmonic is
missing).

<!-- page 52 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
52
Category
Warp Mode
Description
Filter
LPF
Apply a low pass filter.
HPF
Apply a high pass filter.
Distortion
Tube
Emulate the characteristics of analog tube amplification.
The signal is subjected to nonlinearities that mimic the
behavior of vacuum tubes, producing a warm, harmonically
rich, and often smooth-sounding distortion.
Soft Clip
Apply gentle, nonlinear compression to the signal, creating a
smoother, less aggressive distortion compared to hard clipping.
Use this to add warmth and character to a sound without
introducing harsh or unpleasant artifacts.
Hard Clip
Create a type of distortion that aggressively limits the signal
by abruptly cutting off its peaks after it exceeds a certain
threshold.
This results in a sharp, harsh form of distortion that creates a
more aggressive and intense sound compared to softer forms
of clipping.
Diode 1
Create a type of distortion that emulates the sound
characteristics of analog diode clipping circuits, often found in
classic guitar pedals and analog equipment.
This mode adds a unique type of distortion that is both warm
and aggressive, with specific tonal characteristics derived from
the behavior of diodes in the signal path.
Diode 2
Apply a sinusoidal transfer curve with increased hard clipping
as drive is increased.
Linear Fold
Create a type of wavefolding distortion that produces
a distinctive and often aggressive sound by folding the
waveform back on itself whenever it exceeds a certain
amplitude threshold.
This folding effect adds rich harmonic content and introduces
a complex, metallic, or harsh character to the sound.
Sine Fold
Create a type of wavefolding distortion effect that shapes the
input waveform using a sine-based folding process.
This effect introduces complex harmonic content and adds a
smooth but dynamic character to the sound, often resulting in
rich, evolving timbres that can range from warm and musical to
intense and aggressive.

<!-- page 53 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
53
Category
Warp Mode
Description
Distortion
(cont.)
Zero-Square
Modify the waveform in such a way that any part of the signal
below a certain amplitude threshold is forced to zero, while
parts of the waveform above the threshold are squared or
otherwise drastically altered.
This creates a sharp, abrupt change in the shape of the
waveform, leading to a sound that is both harsh and
harmonically rich.
Asym
Create an asymmetric effect that applies different distortion
characteristics to the positive and negative halves of an audio
waveform.
This type of waveshaping introduces a unique harmonic profile
by treating one side of the waveform differently from the
other, resulting in a sound that can range from subtle warmth
to highly complex and rich overtones.
Rectify
Create a type of waveshaping effect that modifies the signal
by altering or “rectifying” the waveform, typically by flipping or
removing one half of the waveform.
This creates a distinct, harmonically rich, and sometimes harsh
or metallic sound, often associated with aggressive or synthetic
timbres.
Sine Shaper
Create a type of waveshaping distortion that shapes the audio
signal using a sine function.
This type of distortion applies a nonlinear transformation
to the input signal, resulting in a smoother, more rounded
distortion that introduces harmonics in a musical and often
warm manner.
Stomp Box
Create a distortion effect that emulates the sound of classic
distortion or overdrive pedals used by guitarists (stomp boxes).
This effect reproduces the gritty, crunchy, and saturated tones
characteristic of analog guitar pedals, bringing warmth, edge,
and intensity to a wide range of sounds.
Tape Sat.
Create a distortion effect that emulates the warm, rich sound
characteristics of analog tape recording.
Tape saturation is a form of soft-clipping distortion that occurs
naturally when audio signals are recorded to magnetic tape,
especially at higher levels.
This effect is highly valued for its ability to add warmth,
harmonic richness, and a sense of vintage character to an
audio signal.

<!-- page 54 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
54
Category
Warp Mode
Description
Distortion
(cont.)
Soft Sat.
Create a distortion effect that introduces subtle, smooth,
and musical saturation to the signal. It is designed to gently
enhance the harmonic content of the sound without
introducing harsh or aggressive distortion.
Soft saturation is often used to add warmth, fullness, and a
natural, analog-like character to audio, making it a popular
choice for enhancing digital recordings.
FM
FM (from other
oscillator)
For example, FM
(B)
Perform frequency modulation using the other oscillator or
filter.
The other oscillator or filter must be enabled for this to work,
however, you can turn down the volume of the other oscillator
if you want to use the other oscillator simply as a modulation
source.
FM (from other
oscillator)
For example, FM
(C)
FM (Noise)
FM (Sub)
FM (Filter 1)
FM (Filter 2)
Thru-Zero
Cause the carrier oscillator (the one producing the sound)
to continue to oscillate correctly even when its frequency is
modulated into negative values by the modulator oscillator.
Normally, if the modulation drives the carrier oscillator’s
frequency below zero, it either clamps at zero (stops
oscillating) or reflects back to a positive value (causing a
discontinuity).
With Thru-Zero, when the frequency modulation drives the
carrier frequency below zero, the carrier oscillator doesn’t stop
or reflect; instead, it inverts its phase and continues oscillating.
This allows for smooth and continuous modulation, resulting in
a more natural and harmonically rich sound.
The inversion of phase (caused by negative frequencies) adds
new harmonic characteristics, making Thru-Zero especially
useful for lush, metallic, or bell-like tones.

<!-- page 55 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
55
Category
Warp Mode
Description
FM (cont.)
Exp
Use an exponential scaling curve. This means small changes
in the modulator’s amplitude can cause dramatic changes
in the carrier frequency, especially as the modulation depth
increases.
Compared to linear FM, exponential FM produces a broader
and more pronounced harmonic spectrum. It is often described
as brighter or harsher due to the rapid frequency sweeps
caused by the exponential relationship.
Linear
Use a linear scaling curve. This means that the modulation
source (modulator oscillator) affects the frequency of the
carrier oscillator in a direct, proportional manner.
This ensures that the carrier oscillator maintains its overall
pitch, even when modulated heavily. This makes it particularly
useful in musical contexts, as it allows for predictable harmonic
and inharmonic spectra without drastically detuning the base
pitch.
Linear is often described as smooth, clean, and more “musical”
compared to other FM types such as exponential FM. This
makes it great for bell-like tones, pads, and other complex but
stable timbres.
Note that linear FM is thru-zero but with a clamp at zero. This
allows you to do the traditional “can’t do thru-zero” FM.
PD
PD (from other
oscillator)
For example, PD
(B)
Perform phase distortion using the other oscillator or filter.
The other oscillator or filter must be enabled for this to work,
however, you can turn down the volume of the other oscillator
if you want to use the other oscillator simply as a modulation
source.
This is similar to FM except that the phase is modulated
instead of the frequency.
PD (from other
oscillator)
For example, PD
(C)
PD (Noise)
PD (Sub)
PD (Filter 1)
PD (Filter 2)
PD (Self)

<!-- page 56 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
56
Category
Warp Mode
Description
AM
AM (from other
oscillator)
For example, AM
(B)
Perform amplitude modulation using the other oscillator or
filter.
The other oscillator or filter must be enabled for this to work,
however, you can turn down the volume of the other oscillator
if you want to use the other oscillator simply as a modulation
source.
This is similar to FM except that the amplitude is modulated
instead of the frequency.
AM (from other
oscillator)
For example, AM
(C)
AM (Noise)
AM (Sub)
AM (Filter 1)
AM (Filter 2)
RM
RM (from other
oscillator)
For example, RM
(B)
Perform ring modulation using the other oscillator or filter.
The other oscillator or filter must be enabled for this to work,
however, you can turn down the volume of the other oscillator
if you want to use the other oscillator simply as a modulation
source.
RM (from other
oscillator)
For example, RM
(C)
RM (Noise)
RM (Sub)
RM (Filter 1)
RM (Filter 2)
Swap Warps
Swap the WARP 1 mode (on the left) with WARP 2 mode (on
the right).

<!-- page 57 -->

﻿
Using Wavetable Oscillators
Serum 2 User Guide
57
Pan
Use the PAN knob to control the placement of the
waveform in the stereo field (left to right).
Level
Use the LEVEL knob to control the output volume
of the oscillator.
Wavetable Pan Control
Wavetable Level Control