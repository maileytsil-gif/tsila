---
titre: "xferrecords com manual serum 2 docs — Importing Audio as Wavetables (p. 291-303)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Importing Audio as Wavetables


<!-- page 291 -->

Serum 2 User Guide
291
Importing Audio as Wavetables
A great way to obtain high-quality source material for wavetables is by importing audio data. This can be
done using various methods, which can generally be categorized as either single-cycle and multi-cycle
imports.
It’s important to realize that wavetables do not behave like samples in a sampler. When importing
audio to create a wavetable, you shouldn’t expect to create ultra-realistic reproductions of acoustic
instruments. Use Sample mode (in any of the oscillators) to work directly with source samples.
Understanding Multi-cycle Waveforms
Most real sounds you come across (such as speech) consist of multiple waveform cycles. In a human
voice waveform, you can see the repetitive nature of sound, which becomes the pitch we hear. You’ve
likely seen this before when manipulating audio in a DAW.
Samplers typically play audio as a single stream of data. In contrast, when importing a sound into Serum,
it attempts to slice the sound into individual single-cycles. Because of the nature of audio, it’s generally
best to select source sounds that are monophonic (that is, sounds that contain a single pitch). This
means that, in most cases, a single note is better than a chord.
Because these single cycles become the basis of the oscillator, pitch information is effectively removed.
In other words, if you load a sound that has a pitch bend, the pitch bend will no longer exist. However,
wavetables have their own set of advantages, which one could describe as a “solid” or “fixed” sound that
lends itself well to unison and wave manipulation (sync, FM, and more) without sounding flimsy.
Serum therefore does a fantastic job of importing the waveform of other sounds. Fixed-pitch, one-
shot (monophonic) sounds, such as a one-shot sample of a synthesizer, are among the best choices for
importing into Serum. Speech and other complex sounds can however yield some pretty interesting
results if you’re open to some experimentation.
Importing Multi-Cycle Waveforms
To import a multi-cycle WAV file, drag the audio file from the macOS Finder, Windows Explorer, or host
DAW file browser to the waveform display on Serum’s main window.
Note: Dragging files directly from the host arrangement window or “region bins” is not possible in most
hosts, but using the host’s standard file-browser should work. In addition, many hosts are able to show
the (parent) sound file in the host file browser, and you should be able to drag from there.
When importing stereo files as a wavetable, Serum uses the left channel in OSC A and
OSC C, and uses the right channel in OSC B.

<!-- page 292 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
292
Import Audio Options
As you drag the waveform, you’ll see several options appear. The location where you release the
mouse determines the import method. Serum then analyzes the sound and creates a new wavetable in
memory. The analysis specifics depend on the import method you choose.
The following describes the import options:
•	 DYNAMIC PITCH - ZERO SNAP
Serum scans the audio file and builds a pitch map. Serum then attempts to locate zero-crossings
within the pitch map. While this works well with simple sounds, complex sounds typically don’t
adhere to sensible zero crossings, so you’ll end up with at least some glitches at best.
Use this mode when you have a sound with a non-fixed fundamental (pitch bend or vibrato) and
the sound is pretty simple, for example a sawtooth wave with little filter sweep/resonance.
•	 DYNAMIC PITCH - FOLLOW
Similar to the previous option, Serum builds a pitch map and imports a varying-sized segment of
audio for each frame (subtable) based on the analyzed pitch.
Unlike the previous option, pitch follow import does not attempt to locate zero crossings. This
option is therefore better suited for complex sounds, such as a source sample that might have a
touch of chorus/unison, resonance, or background noise/notes.

<!-- page 293 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
293
•	 FREQUENCY ESTIMATION
Serum analyzes the incoming waveform to determine its dominant frequencies and harmonic
content, and uses this information to convert the audio into a wavetable. This involves analyzing
the audio signal to identify the fundamental frequency, and then determining the harmonics
(integer multiples of the fundamental frequency).
By matching the detected fundamental frequency to a musical pitch (for example, C4 or A3), Serum
can align the wavetable content to the correct pitch. Serum then uses the estimated frequencies
to guide the conversion of the audio signal into a series of wavetable frames. This ensures that
the harmonic structure and frequency content of the original audio are preserved within the
wavetable, maintaining the character of the original sound.
Frequency estimation is particularly beneficial for audio samples with well-defined pitches and
harmonic structures. These types of samples allow Serum to accurately extract fundamental
frequencies and harmonics, making it easier to convert the sounds into expressive and playable
wavetables. Examples include monophonic synth leads, bass sounds, vocals with sustained notes,
plucked and struck instruments, and FM (frequency modulation) generated sounds.
•	 Constant framesize (PITCH AVERAGE)
If in doubt, try this one first!
This option is typically the best choice when a sound has a fixed frequency, such as a one-shot
from a synthesizer (in other words you hear it as a perfect or near-perfect constant pitch, with
essentially no pitch bend or vibrato).
In this mode, Serum analyzes the entire file for an average pitch, and then uses this number of
samples as the import length. Because some sounds contain half-cycles, silence, multiple notes,
and other artifacts, Serum might not correctly guess the desired pitch.
Fortunately, Serum displays the number of samples it is using per frame in the Wavetable Editor
formula area and switches over to this “fixed” value found during analysis (unless changed or
cleared from the Formula field).
•	 FFT 256/512/1024/2048
FFT, or Fast Fourier Transform, is a method that converts a signal from the time domain to the
frequency domain, revealing its frequency components. It efficiently breaks down a complex
waveform into individual sinusoidal frequencies, enabling analysis of amplitude and phase at
different frequencies.
Unlike the other import modes, which import and divide (and possibly stretch) chunks of the
original waveform, the FFT modes are a spectral import. This means that these import modes
divide the source audio into small snippets of time, and analyze the spectral content.
One way of thinking of this is a “blurred averaging of the frequency content”. This can be very
useful for sounds such as drum loops, speech, and other material where you want the flavor of the
sound for abstract purposes.

<!-- page 294 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
294
The numbers 256, 512, 1024, and 2048 represent the number of samples used to perform the
FFT analysis. FFT 256, for example, analyzes 256 samples at a time.
Larger FFT sizes, such as 1024 or 2048, provide higher frequency resolution because more
samples are considered during the transform. This means you get a more detailed breakdown of
frequency components, making it better for detecting specific tones and harmonics.
Smaller FFT sizes, including 256 and 512, provide lower frequency resolution, which results in a
broader view of the frequency spectrum. This can be less detailed but faster in terms of processing.
•	 Switch OSC type
You can choose to import the audio as a regular sample, automatically switching to the Sample,
Granular, or Spectral oscillator modes. In these cases, the audio is imported directly without
creating a wavetable.
Advanced Imports
Due to the complex nature of audio signals, using a pitch average might not always be perfect.
Sometimes you might want to specify the exact number of samples for each cycle (that you can measure
yourself in a sample editor).
The Wavetable Editor includes a formula parser (described in the next chapter) featuring a text box with
the placeholder text “(enter formula)”. Although the primary function of this field is to create waveforms
from functions, you can also type the following:
•	 A one to four-digit number (such as 1024) to instruct Serum to split the sound file into segments
with this number of samples.
•	 A MIDI “note name” (such as B0, C#2, D6, and so on).
Serum converts the sound file into the appropriate nearest number of samples (rounding to the
nearest whole number of samples).
This MIDI note/sample conversion assumes a 44,100 Hz source sound file. If your source sound
file is not 44,100 Hz, the number of samples is still held true, but you should disregard the
displayed frequency/note information in the formula text area.
Note: Since musical note frequencies are not often perfectly divisible by a sample rate, many pitches will
have some visible “drift” on import.
When creating a wavetable from imported audio, you might hear undesirable buzz from
subharmonics or other factors caused by the beginning and end of the wave cycle not lining up
perfectly.
Therefore, after importing using one of the above methods, try using a fade command from the
Process menu. For example, X-Fade Edges (16 Samples) or X-Fade Edges (Grid Size) should
give you a less buzzy-sounding result.

<!-- page 295 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
295
Text File Overrides for Specific Results (Advanced)
When dragging an audio file to import, Serum notes the location of the file you dragged and then looks
for a file with the same name but with a .txt file extension containing audio file information.
For example, if your audio file is sound.wav, Serum looks for the sound.txt file. If Serum can’t
find the matching file, Serum then looks for the FolderInfo.txt file in the same folder. The
FolderInfo.txt file contains information that applies to all sounds in the folder; this saves you from
having to duplicate the same text file for every WAV file in the folder.
The format of the text file is very basic.
The first line specifies the number of samples-per-cycle of the audio file (in square brackets). Valid
values are numbers between 32 and 9999. The second line specifies whether  to create intermediate
interpolated tables. The default is yes; use [no interp] to specify the opposite.
The following table shows some examples:
Samples per Second
Description
[512]
Specifies a 512 samples-per-cycle waveform with crossfade interpolation.
[768]
[interp]
Specifies a 786 samples-per-cycle waveform with crossfade interpolation.
Note that the second line is optional, since it is the default.
[1024]
[no interp]
Specifies 1024 samples-per-cycle with no interpolation.
Internally, Serum uses 2048 samples for each single-cycle. This makes 2048 the ideal
number of samples to use as a wave cycle if you plan on generating sounds from
synthesizers, vocoders, and so on, to import into Serum (because no resampling of the
source audio is needed).
This 2048 samples-per-cycle works out to 46.875 Hz at 96000 KHz sampling rate
(96000/2048 = 46.875), which is F#0 +24 cents. Since the octave might differ in various
hosts and synthesizers, render and measure in a program that allows you to select in
samples, such as the freeware sound editor Audacity).
Type 2048 in the Formula field prior to dragging to import. Serum will then not have to
alter the sample data at all.

<!-- page 296 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
296
Importing Single-Cycle Waveforms
To import a single-cycle waveform, (or import a short sound to be interpreted as such), drag an audio file
from the macOS Finder, Windows Explorer, or the host DAW file browser to the corresponding frame
thumbnail in the Wavetable Editor.
Importing a Single-Cycle Waveform
This replaces the waveform in the specific frame; the rest of the wavetable remains untouched.

<!-- page 297 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
297
Single-Cycle Waveform Imported
To import multiple single-cycle waveforms at once, drag them together to the oscillator waveform view.
Serum notices that you dragged multiple files and
treats them as single-cycle waveforms.
This replaces your current wavetable with a new
one that consists of the files you dragged.
Importing Multiple Single-Cycle Waveforms

<!-- page 298 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
298
Using the Import Menu
The Import menu in the Wavetable Editor offers the same import options as the drag-and-drop
operation. Use this method if you prefer a standard file browser dialog instead of dragging and dropping
files.
Importing Audio using the Import Menu
Creating a Sound Specifically for Serum Import (Advanced)
Use this procedure when you want to import a waveform (sound) into Serum with maximum quality
from another synthesizer to use as a wavetable.
Whenever possible, use low-frequency notes. Also, use 2048 samples-per-cycle, which
precludes the need for Serum to interpolate the sound.
Alternatively, use low C at 44,100 Hz (33 Hz, 1349 samples per cycle). This is slightly easier
to set up since no fine tuning of pitch is needed.

<!-- page 299 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
299
The following procedure shows an example of how to export a 2048 samples-per-cycle wave from
another synthesizer and import it into Serum.
1.	Determine the appropriate source note (pitch).
Open the Serum Wavetable Editor and type 2048 into the Formula text box. Serum displays the
following in the field:
split at: 2048 samples (22 Hz, note: F1 and -22 cents)
This suggests that you play a low F with -22 cents to create the proper length of 2048 samples per
cycle.
2.	Render a file playing this pitch from the other synthesizer.
Do the following:
a. Create the F1 note in your host sequencer piano roll on the synthesizer track.
Note that octave naming might be different since, unfortunately, there is no standard. You should
probably use a spectrum analyzer to verify ~22 Hz is the fundamental, not ~11 Hz or ~44 Hz.
As for the duration of the note, since Serum can handle 256 wave cycles, you can render this
22 Hz file for up to 11.6 seconds, which is about 8 bars at 165 BPM. If, on the other hand, the
sound has very little modulation/change, there is no need for such a long note. You can probably
determine by ear when the source sound has stopped changing; there is no need for a longer note.
b. Set the fine tuning to -22 cents.
How you do this varies depending on the synthesizer. Typically, this is set per-oscillator, but some
synths have a global tuning.
If you can’t do this in the source synth, consider adding the appropriate amount of “pitch bend”
down as a MIDI message (22% down if pitch bend range is 1 on the source synth). A=440 to
approximately A=434.5 Hz is another potential option.
c. Render (export) this note from the synth as audio. Alternatively, you can freeze and flatten to
produce the synth note as an audio file.
3.	Drag the rendered audio file into Serum.
If the value 2048 is no longer visible in the Formula text field (for example, if you closed the Serum
window after starting this procedure), type 2048 into the field.
When you release the mouse, the audio is imported. The source audio file (render) is no longer
needed at this point unless you wish to re-import it into Serum with different settings.

<!-- page 300 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
300
Note the following:
•	 You will likely have blank or unnecessary tables at the end of the wavetable.
Using the thumbnails, find the first table you don’t want to include. Click the
 button
and choose Remove: Selected->End in the menu that appears.
•	 You might want to apply fades to the tables (use one of the Fade or X Fade options using the
Wavetable Editor Process menus) to eliminate any buzzing artifacts from frame edges.
If your source sound has no subharmonic content, this shouldn’t be necessary.
•	 Listen to the entire wavetable set by playing a note and dragging the WT POS number box in the
Wavetable Editor (or, similarly using the WT POS knob on the main panel for the oscillator).
Alternatively, for automatic playback, you can use a mod source (for example, an envelope with
long attack or an LFO with an upward saw shape) to modulate the wavetable position.
Importing an Image File as a Wavetable
One of the most experimental ways to create a wavetable in Serum is to import an image file. When
importing the file, Serum automatically maps the pixel luminance to the amplitude, creating largely
unpredictable results that can sometimes lead to happy sonic accidents.
The process is extremely simple.
Drag a PNG file (8-bit depth) from the
Finder (macOS) or Explorer (Windows) to a
wavetable oscillator.
This can be either a color or grayscale image.
The width of the image (in pixels) determines
the number of frames in the wavetable (to a
maximum of 256).

In a grayscale image, black (luminance value
0) represents silence (no amplitude). White
(luminance value 255) represents maximum
amplitude.
Shades of gray interpolate between these
extremes.
In general, gentle gradients create smoother
waveform transitions. Unique shapes produce
genuinely experimental sounds.
Importing a PNG File

<!-- page 301 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
301
The first frame of the wavetable appears in
two dimensions.
As expected, the waveform has no
recognizable relationship to the source image.
Switching to 3D however can sometimes
show a slight semblance.
Open the Wavetable Editor to further
process the wavetable. You can normalize
the frames (to ensure that the frames are
balanced), crossfade edges (to smooth
transitions between frames), and filter the
frames, among other operations.
See “Using the Wavetable Editor” on page
274 for detailed information.
To automate a sweep
through the wavetable,
draw an LFO ramp and
drag the LFO tab to the
WT POS knob.
This modulates the
wavetable position
moving from frame 1 to
256.
Imported Wavetable (2D View)
Imported Wavetable (3D View)
LFO Ramp

<!-- page 302 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
302
Embedding Wavetables When Saving a Preset
When saving a preset that includes a custom wavetable created from imported audio, Serum saves the
file path of the audio sample along with the preset. By default, Serum does not store the audio sample
(and corresponding wavetable) within the preset file itself.
This means that if you move the audio sample to a different location on your drive, Serum will not be
able to locate the file automatically. When you try to load a preset that has missing audio files, Serum
displays a dialog similar to the following:
Missing Files Dialog
You have two options. Do either of the following:
•	 Copy the missing audio file to a folder within the current search path and click the

button.
•	 Click the
 button to include the folder containing the audio file in the search path, then click
.

<!-- page 303 -->

﻿
Importing Audio as Wavetables
Serum 2 User Guide
303
To simplify file management, Serum also allows you to embed the wavetable generated from the
imported audio into the preset when saving.
After importing the audio file and creating the
custom wavetable, close the Wavetable Editor and
return to the oscillator display.
Click the
 button (near the top left of the
oscillator display).
The button becomes enabled.

Alternatively, click the menu and choose Embed in
Preset.
This has the same effect and enables the

button.
Save the preset.
The custom wavetable is now saved with the
preset. You no longer need to manage the location
of the audio file.
Embed in Preset