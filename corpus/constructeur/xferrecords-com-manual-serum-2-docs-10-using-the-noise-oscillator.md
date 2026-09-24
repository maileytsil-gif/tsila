---
titre: "xferrecords com manual serum 2 docs — Using the Noise Oscillator (p. 128-132)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Noise Oscillator


<!-- page 128 -->

Serum 2 User Guide
128
Using the Noise Oscillator
Serum features a dedicated noise oscillator that offers a wide range of factory-supplied noise samples
that you can use to add depth, texture, realism, and expressiveness to your sound design.
Since the noise oscillator is actually a stereo sample player featuring high-quality playback, you can also
use it to load your own samples for even greater versatility.
For example, you could use the noise oscillator as a modulation source for many parameters (though the
results can, admittedly, be chaotic). Samples like drum loops, for example, can lead to very interesting
results.
The noise oscillator also appears in the WARP section of all three wavetable oscillators, allowing you to
apply frequency, phase, amplitude, and ring modulation (using the sampler as the modulator).
Noise Oscillator
When using the noise oscillator as a modulator, you should turn down the volume of the
noise oscillator (to just take advantage of the modulation effect).

<!-- page 129 -->

﻿
Using the Noise Oscillator
Serum 2 User Guide
129
Exploring the Noise Oscillator
To enable the noise oscillator, click the header (with the oscillator name and power button). When
enabled, the button turns green.
Loading a Preset
To load a noise preset, click the current sample name and
choose an option in the menu that appears.
After choosing a preset, you can use the < > arrows to
conveniently switch between noise samples without having
to open the menu.
Note that there is a separate category for noises named after
colors.
If you choose one of the noise color modes, a
STEREO control becomes available.
At a setting of 0, the noise is mono; at 100, there is
no correlation between left and right signals.
In addition, a FILTER knob is available to high or
low pass the signal offering you further control.
Enabling the Noise Osc
Noise Osc Enabled
Noise Menu

<!-- page 130 -->

﻿
Using the Noise Oscillator
Serum 2 User Guide
130
The following table offers a brief description of the difference between these different noises:
Noise Color
Description
White
White noise has equal energy at all frequencies, meaning it covers the entire
audible spectrum (20 Hz to 20 kHz) with equal intensity.
It sounds like a constant hiss or the static between radio stations.
Because of its equal distribution across frequencies, white noise has a bright,
harsh sound.
Pink
Pink noise has equal energy per octave, which means the energy decreases
as the frequency increases. Specifically, it has 3 dB less energy per octave as
the frequency doubles.
It has a warmer, less harsh sound compared to white noise, with more
emphasis on lower frequencies.
Brown
Brown noise, also called Brownian noise or red noise, has energy that
decreases even more rapidly than pink noise, at 6 dB per octave.
It has a deep, rumbling sound, with much more emphasis on lower
frequencies and very little high-frequency content.
Geiger
Geiger noise doesn’t have a uniform frequency spectrum like the others.
Instead, it is chaotic, consisting of random clicks or bursts that are not evenly
distributed across time or frequency.
It sounds like the clicks of a Geiger counter, hence the name. The noise is
made up of sporadic, random bursts with unpredictable intervals between
them.
Loading a Sample
Noise oscillator sounds are simply mono or stereo WAV files. This means that you can use your own
samples as noise sounds.
To load your own sample in the noise oscillator, click the current sample name to display the NOISE
menu and choose Load Sample. A dialog appears allowing you to locate the sample on your computer.
Alternatively, drag a sample from the Finder (macOS) or Explorer (Windows) to the oscillator waveform
pane.
Embedding the Sample in the Preset
You can embed a noise sample into your preset (when saving the preset) by displaying the NOISE menu
and choosing Embed in Preset.
This allows you to streamline your presets by packaging your noise samples together with the Serum
settings.

<!-- page 131 -->

﻿
Using the Noise Oscillator
Serum 2 User Guide
131
Noise oscillator playback uses high-quality real time interpolation. This is because with
noise sounds, the high-frequencies are important. Serum strives to offer the best quality
whenever possible, even at the expense of additional CPU usage (although this feature is
heavily optimized with both SSE2 and pre-calculations when a file loads).
Since high-quality playback does require more CPU processing, it is worth noting that
mono sounds do use slightly less CPU resources (one channel instead of two can add up
with chords). The main consideration here is that if you have a mono noise source, don’t
export it as a stereo file for Serum since you will be wasting both disk space and CPU
resources (on playback).
One Shot/Looping
By default, the noise oscillator is set to loop samples.
This is indicated by the highlighted looping button.
Select the
 (one shot) switch to have the sample (noise) stop when playback reaches the end
of the sound file.
The button highlights to show that it’s enabled.
Looping is typically good with noise sounds, but one-shot mode is useful for attack sounds (to add a
percussive punch/attack transient to a sound, for instance).
Start
Use the START control to set the phase start (as a percentage). Click and drag in the field to set the
value. Alternatively, double-click the field and type the appropriate value.
This setting for the noise oscillator is similar to the phase controls in other parts of Serum. However,
since a noise sound is a lot longer than an oscillator waveform, it might be easier to think of this as
“sample start.”
You can also automate the control, which results in a sort of lo-fi “scratching” effect.
Random
Use the RAND control to randomize the start phase. This prevents the noise from being identical each
time you press a note.
Holding a chord is a good example of when you would likely want to add randomness, otherwise the
same noise sounds for all the notes.

<!-- page 132 -->

﻿
Using the Noise Oscillator
Serum 2 User Guide
132
Pitch
Use the PITCH knob to specify the base pitch/frequency for the noise oscillator. The default (50%) is
nominal pitch, that is, the original pitch of the sound file (assuming that the keytrack switch is off).
Fine
Use the FINE knob to fine tune the pitch setting.
Pan
Use the PAN knob to control the placement of the noise in the stereo field (left to right).
Level
Use the LEVEL knob to control the output volume of the noise oscillator.