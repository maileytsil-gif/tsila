---
titre: "xferrecords com manual serum 2 docs — Using Serum FX (p. 152-182)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using Serum FX


<!-- page 152 -->

Serum 2 User Guide
152
Using Serum FX
Serum features an effects section with 13 different FX processors that you can use in any order or
combination, including multiple instances of the same processor. There are also three types of splitter
modules that allow FX processing to be applied to a particular part of the signal.
Serum Effects (FX)
Using the FX Module
Click the FX tab to access the effects module.
Accessing Serum FX (Effects)
An empty rack appears that you can populate with any of the 13 effects modules, in any order.
Click the
 button (near the top left) to expand the FX rack and list view. Alternatively, press
Option-F (macOS)/Alt-F (Windows) to expand the view.

<!-- page 153 -->

﻿
Using Serum FX
Serum 2 User Guide
153
This provides more rack space to display modules without scrolling.
FX Rack and List Views (Expanded)
Click the
 button to revert the FX rack (and list view) back to its original size. Similarly, press
Option-F (macOS)/Alt-F (Windows) to revert the view to the original size.
Selecting a Rack
Serum offers three FX racks: MAIN, BUS 1,
and BUS 2. Each FX rack processes the audio
signal on the corresponding channel.
Click one of the tabs to select the
corresponding FX rack.
Serum FX Racks

<!-- page 154 -->

﻿
Using Serum FX
Serum 2 User Guide
154
Loading Rack Presets
A quick way to get started is to
load rack presets, available using
the presets drop-down menu.
The preset populates the rack
(including the list view on the left).
At any time, you can initialize an
FX rack by choosing Init as the
factory preset.
The following shows an example FX preset:
Acid Dist Delay Rack Preset
FX Presets Menu

<!-- page 155 -->

﻿
Using Serum FX
Serum 2 User Guide
155
Adding Modules
Click the
 button and choose a module in the list
that appears.
Alternatively, you can add a module to the rack by right-
clicking in the rack, choosing Add FX Module, and then
choosing the FX module in the menu that appears.
The module appears in the rack.
After you place an FX module in the rack, all audio
routed to MAIN passes through the module (and then
to the master volume and output).
Note that the signal flow is top to bottom through the
rack.
Module Added to the Rack
Adding an FX Module

<!-- page 156 -->

﻿
Using Serum FX
Serum 2 User Guide
156
Reordering Modules
To reorder effects, click and drag an effect to the new location in the list view (on the left) or in the rack
view (on the right). A yellow line indicates where the module will land.
Reordering Modules
Copying a Module
You can copy an FX module to create a duplicate of the module on a rack, with or without assigned
modulations.
To copy a module without modulations, Option-drag (macOS) or Alt-drag (Windows) an existing module
to the appropriate location on the rack. A yellow line indicates where the module will land, which is
helpful when placing a module between two existing modules.
Copying a Module
To copy a module with assigned modulations, Shift-Option-drag (macOS) or Shift-Alt-drag (Windows) an
existing module to an empty location on the rack.

<!-- page 157 -->

﻿
Using Serum FX
Serum 2 User Guide
157
Bypassing a Module
Every FX module features a bypass button
 that allows you to easily bypass the module. This
button appears to the right of the module both in the list and rack view.
Clicking the button bypasses the module in the signal routing. When enabled, the button highlights in
red
 to show that the module is being bypassed.
Bypass Effect Button
Bypassing a module is really intended for temporary use. For example, you can use bypass to hear your
sound with and without a given FX (without having to set the MIX knob to 100% dry).
Option-clicking (macOS) or Alt-clicking (Windows) on a bypass button toggles bypass for all FX
on the bus. This also works with the FX bypass buttons on the MIXER page.
Removing a Module
To deactivate an effect, you should generally
remove the module from the rack (you can always
add it back later).
Click the
 button for the corresponding module
in the list view (on the left).
Remove an FX Module

<!-- page 158 -->

﻿
Using Serum FX
Serum 2 User Guide
158
Saving a Rack as a Preset
After creating a new custom rack, or modifying an existing rack, you can save the rack as a new preset
Click the
 button. A dialog appears allowing you to type the rack preset name. By default, the preset
is saved in a standard user location so that Serum can easily find it later.
Exploring FX Rack Operations
Serum makes it easy to manage your FX racks by offering a series of operations that you can quickly
access by right-clicking in the background of the rack.
The following table describes the operations you can perform:
Operation
Description
<Select a module>
Add a module to the rack.
Cut FX Bus
Cut (remove) all modules from the current rack. You can then paste the
modules into another rack.
Use this when you want to move all modules from one rack (such as MAIN)
to another rack (such as BUS 1).
Copy FX Bus
Copy all modules from the current rack. You can then paste the modules
into another rack.
Use this when you want to duplicate all modules in one rack (such as MAIN)
in another rack (such as BUS 1).
Paste FX Bus
Paste the contents of the rack clipboard (after a cut or copy operation) to
the currently-selected rack.
Clear FX Bus
Clear the currently-selected rack. This removes all modules from the rack.
Lock FX Bus
Enable this option to have the modules in the selected rack remain in place
when changing presets (no modules will be loaded to that rack).
Note that modulation assignments to module parameters in the locked rack
are cleared when changing presets.
Lock All FX Busses
As the name implies, locks all FX busses (in the manner described above).
Load FX Bus
Load a user preset rack. Serum displays a dialog allowing you to choose the
appropriate rack.
Save FX Bus
Save the current rack as a user preset.

<!-- page 159 -->

﻿
Using Serum FX
Serum 2 User Guide
159
Modulating FX Parameters
You can modulate most FX parameters, similar to the way you can modulate standard Serum synth
controls.
Click and drag an envelope (ENV) or LFO to the modulation destination.
Assigning to Modulation to an FX Module
The FX rack is a DSP process that operates on the sum output of the synth engine
(rather than per voice). You can think of this as “the effects are monophonic” or “the
effects are like plug-in inserts after Serum.” This is sometimes referred to as paraphonic
behavior, especially in conjunction with the filter effect.
Therefore when playing polyphonic synth parts (strummed chords, for example) keep
in mind that automating FX controls with per-voice mod sources (such as an envelope)
results in the effect parameter modulation being modulated/retriggered by each new
note.

<!-- page 160 -->

﻿
Using Serum FX
Serum 2 User Guide
160
Exploring FX Module Operations
When working with individual modules in an FX rack, you can load presets, save your current module
settings as a preset, as well as duplicate or remove a module.
Click the
 button to display the module menu. Note that the color of the button varies depending on
the color of the module. A drop-down menu appears.
Module Menu
The following table describes the operations you can perform:
Operation
Description
Factory
Load a factory preset for the FX module.
Save FX Preset
Save the module configuration as a user preset.
Save as Default Preset
Set the current module configuration as the default preset when
adding the same type of module to an FX rack.
Duplicate FX Module
Duplicate the module on the rack (with the current module settings).
Remove FX Module
Remove the module from the rack.

<!-- page 161 -->

﻿
Using Serum FX
Serum 2 User Guide
161
Exploring Individual FX Modules
This section describes the controls available of each FX module.
Bode
The BODE module offers an implementation of the Bode frequency shifter, a device that shifts the
frequency of an audio signal by a fixed amount, resulting in a unique sound effect.
Named after electronic music and audio signal processing pioneer Harald Bode, this frequency shifting
can create dissonance, phasing effects, or a sense of movement in sound, which you can creatively
apply to your sound design.
Bode Module
The BODE module offers the following controls:
Control
Description
MONO INPUT
Enable to route mono input to the module.
SHIFT
The percentage of the range to which to apply the pitch shift.
Right-click the knob and choose Retrig in the context menu to have the
module restart the effect for each new note.
RANGE
The range of the bode shift.
DIR
The direction of the bode shift. Setting to the center causes both channels
to go in opposite directions.
WIDTH
Used in conjunction with the DIR knob, WIDTH specifies whether both
Bode channels (up and down) are used, or if only a single channel is used.
DELAY
The delay time.
BPM
Specifies whether the delay time is synced to the BPM or measured in
Hertz (Hz).
FEED
The amount of delay fed back into the Bode shifter, which can produce
pitched delays.
BALANCE
The delay input mix between a down and up shifted signal.
BLUR
Use to create chorus and wow/flutter effects.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).

<!-- page 162 -->

﻿
Using Serum FX
Serum 2 User Guide
162
Chorus
The CHORUS module offers a four-voice chorus effect, with two left and two right chorus taps.
Chorus Module
The CHORUS module offers the following controls:
Control
Description
RATE
The rate of the chorus. The units depend on the BPM setting. When BPM is
on, the RATE knob snaps to musical time (from 8 bars to 1/32nd note).
When BPM is off, the RATE knob is in Hertz (Hz), between 0 Hz and 20 Hz.
BPM
Specify whether the chorus is synced to the host BPM. See the RATE knob
(above) for more information.
DELAY 1
The amount of delay (in milliseconds) between the dry signal and the first
stereo pair of chorus voices.
DELAY 2
The amount of delay (in milliseconds) between the dry signal and the second
pair of chorus voices.
DEPTH
Specifies how much the chorus LFO modulates the delay times described
above (how much pitch warble occurs).
FEEDBACK
The feedback amount of the chorus voices (how much of the chorus voice
output appears back at the input of the chorus module). This creates a more
pronounced “ringing” to the chorus.
LPF/HPF
The cutoff frequency in Hertz (Hz) of the low pass/high pass filter after the
chorus wet effect. This is useful for a more (or less) “warm doubling” of the
signal. Click the label to toggle between LPF and HPF.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
Compressor
The COMPRESSOR module reduces the volume of loud sounds or amplifies quiet sounds, thereby
reducing or compressing the dynamic range of an audio signal.
Compressor Module

<!-- page 163 -->

﻿
Using Serum FX
Serum 2 User Guide
163
The COMPRESSOR module offers the following controls:
Control
Description
MODE
The compressor mode, either SINGLE or MULTIBAND. The mode
determines how the compressor processes audio signals.
SINGLE — Select to configure the module as a single-band compressor. This
causes the compressor to affect the entire frequency spectrum of the audio
signal as one unified band. In other words, it applies compression uniformly
across all frequencies.
Single-band compressors are often used for overall dynamic control of a
track or mix. They are simpler and more straightforward, making them ideal
for general-purpose compression.
However, when a single-band compressor is triggered by a loud frequency, it
compresses the entire signal. This can cause other frequencies, such as mids
and highs, to be compressed as well, even if they don’t need it, leading to
less precise dynamic control.
MULTIBAND — A multiband compressor divides the audio signal
into multiple frequency bands, allowing you to compress each band
independently. This provides more precise control over the dynamics of
different parts of the frequency spectrum.
Select this option to make the compressor become a multiband upwards/
downwards compressor. This is an extreme setting, but you may find a use
for it.
The individual bands are separately user-adjustable, and you can assign
modulations using the modulation matrix. This is useful for side-chaining just
the low end out of the way of a kick or bass.
THRESH
The threshold (in dB) for the compression to start engaging. A setting of 0
equals 0 dB (no compression, unless the input signal is overloaded); a setting
of 100% equals -120 dB (almost always compressing).
Typically, you would set this to around the middle of the range (for example,
around -12 dB), but the setting is dependent on your input signal strength
and the amount of compression you want.
RATIO
The strength of the gain reduction. Typical compression is between 2:1 and
4:1. If you set the compression knob to maximum, Limit appears.
This offers a completely different DSP circuit (a true peak limiter and not
a compressor); therefore, the other controls behave differently when the
limiter is engaged. Specifically, the attack time range changes to 0-10ms and
the makeup gain range changes to 0-36dB.
Note: Setting the ratio to Limit can introduce latency. Right-click the knob
and choose Limiter Latency Comp in the context menu to have the module
report this latency to the host.

<!-- page 164 -->

﻿
Using Serum FX
Serum 2 User Guide
164
Control
Description
ATTACK
The amount of time in milliseconds for the gain reduction to engage.
A longer (slow) attack is useful for letting some signal through before the
gain reduction takes place, resulting in a “punch,” “snap,” or “bite” (sounds are
hard to describe using language!).
A shorter/faster attack tames peaks more completely.
RELEASE
The amount of time for the gain reduction to be removed.
GAIN
The amount of makeup gain. This is a good way to boost quiet signals. The
control allows for approximately 30dB of boost for the compressor and
36dB for the limiter so be careful (that’s a large amount of gain). Basically, a
little can go a long way.
X-LOW
(Enabled when MULTIBAND is selected) Sets the low crossover for the
multiband split.
BELOW
(Enabled when MULTIBAND is selected) Sets the compression ratio below
the threshold.
X-HIGH
(Enabled when MULTIBAND is selected) Sets the high crossover for the
multiband split.
H
(Enabled when MULTIBAND is selected) Sets the high band gain.
M
(Enabled when MULTIBAND is selected) Sets the mid band gain.
L
(Enabled when MULTIBAND is selected) Sets the low band gain.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
Convolve
The CONVOLVE module allows you to apply the impulse response of a signal you select (representing
the characteristics of a room’s reverb or a specific filter) to your sound design.
The most common use is to create a convolution reverb, where the impulse response of a real acoustic
space (such as a concert hall) is convoluted with your audio signal to simulate how that signal would
sound if played in that space. This allows for highly realistic and complex reverb effects.
You can also use the CONVOLVE module to blend sounds in unique ways, applying an effect that alters
your sound in a manner different from simple filtering or other modulation techniques.
Convolve Module

<!-- page 165 -->

﻿
Using Serum FX
Serum 2 User Guide
165
The CONVOLVE module offers the following controls:
Control
Description
IMPULSE
Click to choose from a menu of impulse responses. Use the < > arrows to
advance through the modes without having to open the menu.
You can load impulse responses from outside the Serum 2 Presets
folder by dragging and dropping the files on the IR display or selecting Load
IR from the context menu.
If you do this, the option to Embed in Preset appears in the menu, and an
embed icon appears at the top right of the IR display. This allows you to
embed the impulse response into the preset, similar to what you can do with
oscillators.
SIZE
The size with which to stretch or contract the impulse.
TONE
Use to filter the impulse.
ϕ MIN
The convolution minimum phase. This converts the IR to a minimum-phase
representation, keeping the frequency response unchanged and eliminating
echoing.
PRE-DLY
The convolution pre-delay. This offsets the impulse in time.
BPM
Specifies whether the pre-delay is synced (BPM or millisecond based.
ATTACK
The convolution attack. Use this to fade in the impulse.
DECAY
The convolution decay. Use to shorten the impulse.
DAMP
Use to shorten the high frequency of the impulse.
IR GAIN
The impulse volume.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
Delay
The DELAY module records an input signal and then plays it back after a period of time. The delayed
signal may be played back multiple times, or fed back into the recording, to create the sound of a
repeating, decaying echo.
Delay Module

<!-- page 166 -->

﻿
Using Serum FX
Serum 2 User Guide
166
The DELAY module offers the following controls:
Control
Description
MODE
The type of delay, from among the following:
NORMAL — Specifies a standard stereo delay with independent left and
right channels/times.
PING-PONG — Sets the outputs of the left and right delays to feed into one
another.
TAP-> DELAY — Sets both delays to mono and in series, causing the
left signal to fire once with no feedback (tap) followed by the right signal
operating as a typical delay (feedback is applied here).
Select the High Quality option to render the output of the module in higher
quality.
Delay Times
The delay times.
There are two settings available for both the left and right channels. The
upper input is the base delay time for the channel. The lower box is a (scalar)
offset for the delay time you set above.
For instance, a value of 1.1 means that the corresponding delay time sounds
at 110% of its value. Dragging the lower inputs displays Trip or Dot when
you reach 133% (1.333) and 150% (1.5) respectively. This allows you to
quickly set triplet or dotted values for the delay times.
BPM/MS
Specifies whether the delay times are in tempo-based units (quarter note,
for example) or in milliseconds.
LINK
Enable to have the right-channel delay times link with (kept the same as) the
left channel delay times.
FEEDBACK
The amount of the delayed signal appearing back at the input of the delay.
This is useful for controlling how many delay repeats are audible.
FREQ (Frequency)
The filter cutoff frequency (in Hertz) for the delay filter.
Q (Resonance)
The bandwidth for the delay filter (how much low pass and high pass are
applied).
Technically, this is the opposite of a standard Q control, where a larger Q
value typically signifies a narrow filter bandwidth. However, in this case, a
maximum value means minimum filtering/maximum bandwidth.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).

<!-- page 167 -->

﻿
Using Serum FX
Serum 2 User Guide
167
Manipulating the Delay Filter
In addition to using the FREQ and Q knobs, you can manipulate the delay filter using your mouse.
By default, the delay filter appears like this.
Click the drag in the display to set the frequency
and Q simultaneously.
Double-click the display to toggle a real-time
frequency overlay.
Distortion
The DISTORTION module offers 13 types of distortion, including two dual-waveshaper modes that
allow you to create your own custom distortion.
Distortion Module

<!-- page 168 -->

﻿
Using Serum FX
Serum 2 User Guide
168
The DISTORTION module offers the following controls:
Control
Description
MODE
Click to choose from a menu of distortion types (Tube, by default). You can
use the < > arrows to advance through the modes without having to open
the menu.
OFF/PRE/POST
A switch to enable filtering, which you can set to either pre-distortion (PRE)
or post-distortion (POST).
TYPE
The filter type for the distortion module. Drag the red control between left
and right to morph from low pass to bandpass to high pass.
FREQ
The cutoff frequency for the filter (when the filter is enabled). Double-click
the field to display a text box, allowing you to enter a frequency value.
Right-click the knob and choose Key Track in the context menu to have
frequency respond to the pitch of the note played. With Key Track disabled,
the frequency is fixed regardless of the key played.
With Key Track enabled, the frequency changes in proportion to the pitch
of the note played (higher-pitched notes increase the frequency).
Q
The resonance for the filter (when the filter is enabled). Double-click the
field to display a text box, allowing you to enter a resonance value.
You can set a high value to create squelchy feedback. Typically, lower values
are more common.
DRIVE
Generally, the gain boost for the distortion, with the following exceptions:
•	 With Downsample filter type, the DRIVE knob controls the sample rate
reduction amount.
•	 With X-Shaper and X-Shaper (Asym) modes, the DRIVE knob affects a
morph between the two waveshapes.
You can also set the drive by dragging up or
down in the graphic display.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).

<!-- page 169 -->

﻿
Using Serum FX
Serum 2 User Guide
169
Understanding X-Shaper (Dual Waveshaper) FX Modes
The X-Shaper is a dual crossfading waveshaper. Selecting X-Shaper in the distortion menu causes Edit
A and Edit B buttons to appear directly below the menu.
Clicking either button displays a pop-up “X-Y” graph editor for the respective waveshaper. In both cases,
the X (horizontal) axis represents the input level, and the Y (vertical) axis represents the corresponding
remapped output level for an input level.
The DRIVE knob, described above, controls the blend between the two waveshaping graphs (the
DRIVE knob at 0% presents waveshaper A while 100% presents waveshaper B).
Note that X-Shaper is a symmetric waveshaper, with the lower-left point on the graph representing
silence (-INF dB for input and output). Similarly, the top-right point represents the highest level (0 dB for
input and output).
In contrast, X-shaper (Asym) is an asymmetric waveshaper. In this case, the middle of the graph
represents silence (-INF dB input and output), the top-right represents the highest positive value to the
signal, and the lower-left represents the highest possible negative value.
Asymmetric distortion allows you to bring out even-order harmonics that are not typically found in a
standard symmetric distortion (such as clipping). This is often the case in guitar amps; one pole distorts
(for example, fatline) while the other pole remains relatively undistorted.
Equalizer
The EQUALIZER module offers two-band parametric control.
Equalizer Module
You can set the type of each of the two bands using the corresponding three-state switches. The left
band offers low-frequency (LF) adjustment and enables low shelf, peaking, or high pass filtering. The
right band offers high-frequency (HF) adjustment and enables high shelf, peaking, or low pass filtering.
The EQUALIZER module offers the following controls:
Control
Description
FREQ (L)
The frequency (in Hz) for the low EQ band.
Q (L)
The Q (resonance) for the low EQ band.
GAIN (L)
The gain boost/cut (in dB) for the low EQ band. This knob has no effect if
you selected High Pass as the low EQ band type.

<!-- page 170 -->

﻿
Using Serum FX
Serum 2 User Guide
170
Control
Description
FILTER TYPE
Click the icons to select a Shelf, Peak, or High Pass filter type (on the left)
and Shelf, Peak, or Low Pass filter type (on the right).
FREQ (R)
The frequency (in Hz) for the high EQ band.
Q (R)
The Q (resonance) for the high EQ band.
GAIN (R)
The gain boost/cut (in dB) for the high EQ band. This knob has no effect if
you selected Lowpass as the high EQ band type.
LEVEL
The output level of the module (in decibels).
Filter
The FILTER module operates identically to the per-voice synth filter found on the main OSC tab, except
that in this case, it runs as a master effect.
Filter Module
The FILTER module offers the following controls:
Control
Description
TYPE
Click to choose from a menu of filter types (MG Low 6, by default). You can
use the < > arrows to advance through the filter types without having to
open the menu.
See “Filter Types and Var Parameter Functions” for more information about
the available filter types.
CUTOFF
The primary cutoff frequency for the filter (with just a couple exceptions,
such as vowels for formant filters).
TIP: You can recreate certain paraphonic vintage synth behaviors by
applying an envelope to this knob.
Right-click the knob and choose Key Track in the context menu to have
cutoff frequency respond to the pitch of the note played. With Key Track
disabled, the cutoff frequency is fixed regardless of the key played.
With Key Track enabled, the cutoff frequency changes in proportion to the
pitch of the note played (higher-pitched notes increase the cutoff frequency.
RES
The resonance (feedback) of the filter circuit.

<!-- page 171 -->

﻿
Using Serum FX
Serum 2 User Guide
171
Control
Description
DRIVE
The gain into the filter circuit. The setting can impart some coloration (mild
distortion) to the sound.
Right-click the knob and choose Clean Mode in the context menu to have
the filter pre-gain stage the filter input -24 dB (with a +24 dB boost post-
filter).
FAT/FREQ/MORPH/
LP FRO/HP FRO/
HL WID/LP FRO/
DB +/-/SPREAD/
DAMP/BOEUF/
THRU/FORMNT/
WIDTH/COMBFRO/
SCREAM/STAGES/
SMOOTH/PAIN/
FRO2
This is a variable knob with different functions depending on the selected
filter type.
For instance, with “dual” filters, the VAR knob controls the second filter
cutoff frequency.
PAN
A cutoff offset for the left and right signals. At the default setting of 50% (12
o’clock) this knob has no effect. When turned to the left (counter-clockwise)
the left channel cutoff increases, and the right channel cutoff decreases.
When turned to the right (past 12 o’clock clockwise), the opposite happens;
the left cutoff decreases and the right channel cutoff increases.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
You can graphically adjust the filter cutoff and resonance (in
combination) by clicking and dragging in the filter display.
This is a quick way to experiment with filter settings in your sound
design.
Right-click in the display to access a menu allowing you to choose
display options for the filter.
The following table describes the available display options.
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
Graphical Adjustments

<!-- page 172 -->

﻿
Using Serum FX
Serum 2 User Guide
172
Option
Display
Description
Frequency
Response
& FFT
Combines the filter frequency response curve
with a real-time FFT (Fast Fourier Transform)
analysis of the audio input.
The FFT displays the actual frequency content
of the signal, overlaid with the filter’s effect.
Phase
Response
& FFT
Shows how the filter affects the phase of
different frequencies, indicating the degree of
phase shift applied to each frequency in the
signal, alongside the real-time FFT of the audio.
You can quickly cycle through the different display modes by Option-clicking (macOS) or Alt-
clicking (Windows) in the filter display.
Flanger
The FLANGER module works by cyclically varying phase shift into one of two identical copies of a signal
and then recombining them.
Flanger Module
The FLANGER module offers the following controls:
Control
Description
RATE
The rate of the flanger. The units depend on the BPM setting. When BPM
is on, the RATE knob snaps to musical time (from 8 bars to 1/32nd note).
When BPM is off, the RATE knob is in Hertz (Hz), between 0 Hz and 20 Hz.
BPM
Specifies whether the flanger sweep is synced to the host BPM. See the
RATE knob (above) for more information.
DEPTH
Specifies how much the flanger LFO influences the sound, in other words,
how much (or deep) the flanger operates.
FEEDBACK
The feedback amount of the flanger circuit, which makes the effect more
pronounced (“ringing”).

<!-- page 173 -->

﻿
Using Serum FX
Serum 2 User Guide
173
Control
Description
PHASE
The stereo phase offset for the LFO influence over the flanger (the left
flange and right flange offset). A setting of 0% sets both left and right to the
same frequency.
A setting of 50% represents 180 degrees, meaning that the left and right
have opposite frequencies. In this case, the flanger sweep “rises” on the left
while “falling” on the right, or vice versa.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
Hyper/Dimension
The HYPER/DIMENSION module is a micro-delay chorus with a variable number of voices (1-7). In
addition you can configure the Hyper/Dimension effect to retrigger on every MIDI note, which adds to
the potential simulation of a unison.
To conserve CPU, consider using the HYPER effect as an alternative to high unison settings.
Hyper/Dimension Module
The HYPER module offers the following controls:
Control
Description
RATE
The speed at which the various hyper voices oscillate sharp/fat in pitch.
UNISON
The number of chorus voices. If you only want to use the DIMENSION
effect and not the HYPER effect, set the UNISON to 0.
DETUNE
The amount/depth of the hyper voice oscillations (sharp/fat in pitch).
RETRIG
When turned on, resets all hyper voices to start over from a zeroed-pitch
offset.
This provides a laser-like zap effect for each note-on event. You might use
this on certain monophonic patches, for example.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).

<!-- page 174 -->

﻿
Using Serum FX
Serum 2 User Guide
174
The DIMENSION effect is a pseudo-stereo effect consisting of four delay lines summed out-of-phase
and slowly amplitude-modulated to provide a subtle amount of motion to the effect. This is useful for
adding a perceived width to an otherwise mono signal.
The DIMENSION module offers the following controls:
Control
Description
SIZE
Adds an extra layer of phased delays.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
Phaser
The PHASER module filters a signal by creating a series of peaks and troughs in the frequency
spectrum.
Phaser Module
The PHASER module offers the following controls:
Control
Description
RATE
The rate of the phaser. The units depend on the BPM setting. When BPM
is on, the RATE knob snaps to musical time (from 8 bars to 1/32nd note).
When BPM is off, the RATE knob is in Hertz (Hz), between 0 Hz and 20 Hz.
BPM
Specifies whether the phaser sweep is synced to the host BPM. See the
RATE knob (above) for more information.
POLES
The number of stacked phaser poles.
DEPTH
Specifies how much the phaser LFO influences the sound.
DEPTH 2
The offset between phaser stages.
FREQ
The base frequency for the phaser effect.
FEEDBACK
The feedback amount of the phaser circuit. A higher setting makes the effect
more pronounced (“ringing”).
PHASE
The stereo phase offset for the LFO influence over the phaser (left flange
and right flange offset). A setting of 0% sets both left and right to the same
frequency.
A setting of 50% represents 180 degrees, with left and right at opposite
frequencies (in other words, the phaser sweep “rises” on the left while
“falling” on the right, or vice versa.

<!-- page 175 -->

﻿
Using Serum FX
Serum 2 User Guide
175
Control
Description
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).
Reverb
The REVERB module offers a plate and hall reverb, using a modified version of the Tal Reverb algorithm
(courtesy of Togu Audio Line).
Reverb Module
The REVERB module offers the following controls:
Style
Control
Description
TYPE
Click to choose from a menu of reverb types (PLATE, by default).
You can use the < > arrows to advance through the reverb types
without having to open the menu.
PLATE
LO CUT
Suppress low frequencies from the reverb. 0% means no effect
on lows, 100% means no lows at all.
HI CUT
Suppress high frequencies from the reverb. 0% means no effect
on highs, 100% means no high frequencies at all.
SIZE
The length of the reverb.
PRE-DLY
The offset time for the reverb.
DAMP
An additional high-frequency cut for the reverb.
The knob controls how fast this high-frequency attenuation
occurs. 0% mean no damping, 100% means maximum damping.
WIDTH
Expand or collapse the stereo width of the reverb. 100% means
maximum width.
HALL
LO CUT
Suppress low frequencies from the reverb. 0% means no effect
on lows, 100% means no lows at all.
HI CUT
Suppress high frequencies from the reverb. 0% means no effect
on highs, 100% means no high frequencies at all.
SIZE
The room size (reverb time + dimension).

<!-- page 176 -->

﻿
Using Serum FX
Serum 2 User Guide
176
Style
Control
Description
PRE-DLY
The amount of time (in milliseconds) before reverberation
occurs. Using pre-delay allows you to give the impression that a
sound is close to you but in a large room.
You can also use it to separate your transient from the reverb or
create a delay-like echo.
DECAY
The amount of decay (in milliseconds).
SPIN RATE
Set the speed of the LFO used to modulate time differences.
HALL (cont.)
SPIN DEPTH
Modulate time differences with an LFO to create a sense of
movement within the reverb.
VINTAGE
LO CUT
Suppress low frequencies from the reverb. 0% means no effect
on lows, 100% means no lows at all.
HI CUT
Suppress high frequencies from the reverb. 0% means no effect
on highs, 100% means no high frequencies at all.
SIZE
The length of the reverb.
PRE-DLY
The amount of time (in milliseconds) before reverberation
occurs. Using pre-delay allows you to give the impression that a
sound is close to you but in a large room.
You can also use it to separate your transient from the reverb or
create a delay-like echo.
ER SIZE
The length of the early reflection part of the reverb.
DECAY
The amount of decay (in milliseconds).
DAMP
The speed at which high frequencies decay.
DIFF A
The diffusion of the reverb.
DIFF B
Dampen the diffusion stage of the reverb.
CHORUS
The top value sets the speed that the reverb is modulated.
The bottom value sets the pitch depth that the reverb is
modulated.
NITROUS
LO CUT
Suppress low frequencies from the reverb. 0% means no effect
on lows, 100% means no lows at all.
HI CUT
Suppress high frequencies from the reverb. 0% means no effect
on highs, 100% means no high frequencies at all.
SIZE
The length of the reverb.
PRE-DLY
The offset time for the reverb.
FEEDBACK
The amount of reverb fed back into the input signal.
DIFFUSION
The diffusion of the reverb.

<!-- page 177 -->

﻿
Using Serum FX
Serum 2 User Guide
177
Style
Control
Description
MODE
The nitrous mode, from among the following:
•	 Space
•	 Marble
•	 Rectangle
•	 Hexagon
•	 Box
NITROUS
(cont.)
CHORUS
The top value sets the speed that the reverb is modulated.
The bottom value sets the pitch depth that the reverb is
modulated.
BASIN
LO CUT
Suppress low frequencies from the reverb. 0% means no effect
on lows, 100% means no lows at all.
HI CUT
Suppress high frequencies from the reverb. 0% means no effect
on highs, 100% means no high frequencies at all.
SIZE
The length of the reverb.
PRE-DLY
The offset time for the reverb.
FEEDBACK
The amount of reverb fed back into the input signal.
CHORUS
The top value sets the speed that the reverb is modulated.
The bottom value sets the pitch depth that the reverb is
modulated.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100
(100% wet).
LEVEL
The output level of the module (in decibels).
Splitter L/H
The SPLITTER L/H module divides the audio signal into distinct low and high-frequency bands,
enabling you to design and apply dedicated FX racks for each band independently.
This setup provides precise control over your sound, allowing for tailored processing that enhances both
the low-end punch and high-end clarity.
Splitter L/H Module

<!-- page 178 -->

﻿
Using Serum FX
Serum 2 User Guide
178
When using this module, you can build two separate racks, one to handle the LOWS and another to
process the HIGHS. The list view (on the left) shows both racks. The rack view, however, only shows the
currently-selected rack. Click the LOWS or HIGHS panel to display the corresponding rack.
Splitter L/H Module Example
The SPLITTER L/H module offers the following controls:
Control
Description
LOWS
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the low-end rack.
Each time you add a module, it appears below the SPLITTER L/H main
module.
Note the bypass button in the LOWS panel. Enabling this bypasses the low-
end rack.
SPLIT FREQ
The crossover frequency for the low and high bands.
HIGHS
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the high-end rack.
Each time you add a module, it appears below the SPLITTER L/H main
module.
Note the bypass button in the HIGHS panel. Enabling this bypasses the
high-end rack.
LEVEL
The output level of the module (in decibels).

<!-- page 179 -->

﻿
Using Serum FX
Serum 2 User Guide
179
Splitter L/M/H
The SPLITTER L/M/H module divides the audio signal into low, mid, and high-frequency bands,
offering even greater flexibility than the SPLITTER L/H module. This configuration enables you to
design and apply dedicated FX racks for each band independently, allowing for fine-tuned control over
your sound.
With the addition of the MIDS panel, you gain the ability to shape and process the critical midrange
frequencies separately, ensuring that elements like vocals, guitars, and synths stand out or blend
seamlessly. This setup provides precise control, enhancing the low-end punch, midrange presence, and
high-end clarity, for a more refined and impactful mix.
Splitter L/M/H Module
When using this module, you can build three distinct racks, one to handle the LOWS, one for the MIDS,
and another to process the HIGHS. The list view (on the left) shows all three racks. The rack view,
however, only shows the currently-selected rack. Click the LOWS, MIDS, or HIGHS panel to display the
corresponding rack.
Splitter L/M/H Module Example
The SPLITTER L/M/H module offers the following controls:
Control
Description
LOWS
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the low-end rack.
Each time you add a module, it appears below the SPLITTER L/M/H main
module.
Note the bypass button in the LOWS panel. Enabling this bypasses the low-
end rack.

<!-- page 180 -->

﻿
Using Serum FX
Serum 2 User Guide
180
Control
Description
SPLIT FREQ
The crossover frequency for the low and mid bands.
MIDS
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the low-end rack.
Each time you add a module, it appears below the SPLITTER L/M/H main
module.
Note the bypass button in the MIDS panel. Enabling this bypasses the mid-
end rack.
SPLIT FREQ
The crossover frequency for the mid and high bands.
HIGHS
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the high-end rack.
Each time you add a module, it appears below the SPLITTER L/M/H main
module.
Note the bypass button in the HIGHS panel. Enabling this bypasses the
high-end rack.
LEVEL
The output level of the module (in decibels).
Splitter MS
The SPLITTER M/S module divides the audio signal into mid and side bands. This configuration enables
you to design and apply dedicated FX racks for each band independently, allowing for precise control
over the central and spatial elements of your sound.
Use it to enhance focus and presence by processing the mid channel, or to control depth and width by
processing the side channel, giving you a powerful tool for shaping your mix.
Splitter M/S Module
When using this module, you can build two separate racks, one to handle the MID band and another to
process the SIDE band. The list view (on the left) shows both racks. The rack view, however, only shows
the currently-selected rack. Click the MID or SIDE panel to display the corresponding rack.

<!-- page 181 -->

﻿
Using Serum FX
Serum 2 User Guide
181
Splitter M/S Module Example
The SPLITTER M/S module offers the following controls:
Control
Description
MID
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the mid-band rack.
Each time you add a module, it appears below the SPLITTER M/S main
module.
Note the bypass button in the MID panel. Enabling this bypasses the mid-
band rack.
SIDE
Right-click in the panel and choose an FX module to add using the menu
that appears. Continue doing this until you finish building the side-band
rack.
Each time you add a module, it appears below the SPLITTER M/S main
module.
Note the bypass button in the SIDE panel. Enabling this bypasses the side-
band rack.
LEVEL
The output level of the module (in decibels).

<!-- page 182 -->

﻿
Using Serum FX
Serum 2 User Guide
182
Utility
The UTILITY module offers a series of “utility” functions including polarity inversion, basic low and high
pass filters, stereo width and balance, and more.
Utility Module
The UTILITY module offers the following controls:
Control
Description
POLARITY INV
Invert the polarity of the audio signal on the left and right channel of the
signal respectively.
LPF
The low pass filter.
HPF
The high pass filter.
MONO BASS/FREQ
Enable for mono bass, which forces frequencies below the threshold (set
using the FREQ control) to be monophonic.
WIDTH
The stereo width.
PAN
The stereo balance.
MIX
The wet/dry amount for the effect, from 0 (100% dry) to 100 (100% wet).
LEVEL
The output level of the module (in decibels).