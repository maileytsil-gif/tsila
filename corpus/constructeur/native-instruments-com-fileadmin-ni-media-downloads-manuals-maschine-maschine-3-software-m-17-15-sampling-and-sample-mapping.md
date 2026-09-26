---
titre: "Maschine Software Manual — 15. Sampling and sample mapping (p. 437-472)"
source: constructeur/native-instruments-com-fileadmin-ni-media-downloads-manuals-maschine-maschine-3-software-m.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# 15. Sampling and sample mapping


<!-- page 437 -->

15. Sampling and sample mapping
Maschine allows you to record internal or external audio signals without having to stop the
sequencer. This is a helpful feature if you want to record your Samples or rearrange loops that
you have created yourself using Maschine.
You can apply various types of destructive processing to the recorded audio or to any Sample you
want to use in a Sound.
The slicing feature allows you to slice loops to make them playable at any tempo without changing
their pitch or timing. It is also useful if you want to quickly extract single Samples from loops (for
example., a snare sound from a drum loop) or rearrange loops by editing or muting their Slices,
changing the order of the Slices, applying a different quantization, or adding Swing.
Last but not least, you can map your Samples to particular Zones, thereby creating multi-sample
Sounds with individual velocity and note ranges, volume, and panning. This is useful to emulate the
behavior of classic instruments and synthesizers and allows for a large number of Samples in only
one Sound.
All this can be done in the Sample Editor.
Before recording an external source please consult the documentation that came with
your audio interface for information on connecting audio devices and instruments.
Opening the Sample Editor
To access the Sample Editor in the software, do the following:
1. In the Sound List left of the Pattern Editor, click the desired Sound to put it under focus. For
more information, refer to Focusing on a Group or a Sound.
2. Click the Sample Editor button on the left of the Pattern Editor to switch to the Sample Editor.
The Sample Editor appears and displays the Sample content of the focused Sound.
3. In the Sample Editor, click the desired tab at the top to access the corresponding page:
•
The Record page allows you to record audio: Recording audio.
•
The Edit page allows you to apply destructive edits to existing Samples: Editing a Sample.
•
The Slice page allows you to create Slices from your existing Samples: Slicing a Sample.
•
The Zone page allows you to assign your Samples to particular note and velocity ranges
(called Zones) in your Sound and to adjust various playback settings for each Zone individually:
Mapping Samples to Zones.
Recording audio
Maschine provides everything you need to record audio.
SAMPLING AND SAMPLE MAPPING 434

<!-- page 438 -->

Opening the Record page
In the software, recording audio is done in the Sample Editor. By default, the Sample Editor is on
the blank Record page and no other tabs are visible. However, the Record tab, plus additional tabs,
will become visible once audio has been recorded.
The Record page looks as follows:
The Record page in the software.
Selecting the source and the recording mode
At the bottom of the Record page, the INPUT section and the RECORDING section allow you to
select which source should be recorded and how the recording should be made.
Adjusting the source and mode of the recording in the software.
Choosing a recording mode
▶Click the MODE selector in the RECORDING section to select from the four available recording
modes:
SAMPLING AND SAMPLE MAPPING 435

<!-- page 439 -->

•
Detect: Select Detect mode to record audio after the set threshold has been exceeded. This is
useful when you want to record audio without the silence before the incoming sound is played.
If the focused Sound Slot contains neither an Audio nor Sampler plug-in, the recorded audio will
automatically be loaded into a Sampler plug-in for the first Take. After that, you must trigger the
Sampler with MIDI Events, such as those in a Pattern, to playback the audio.
•
If Detect is selected, you can set a specific threshold using the level THRESHOLD control
on the right. After clicking Start, any input signal level exceeding this threshold will start the
recording. You can then manually stop the recording by clicking Stop. You can also adjust
the threshold by dragging the slider that appears on the horizontal input level meters above
the RECORDING section: Any input level reaching the slider position will start the recording.
Double-click the slider to reset the threshold to its default value (-12 dB).
•
Sync: Select Sync to start recording audio in time with the Pattern Grid. If the focused Sound
Slot contains neither an Audio nor a Sampler plug-in, the recorded Sample will be loaded
automatically into a Sampler plug-in as the first Take. After that, you must trigger the Sampler
with MIDI Events to playback the audio.
•
When Sync is selected, the recording starts in sync with the sequencer after clicking Start.
The recording will begin at the start of the next bar. The LENGTH control on the right allows
you to choose a length for the recording: either 1, 2, 4, 8, or 16 bars, or choose Free if you do
not want to set a duration limit to the recording. You can click Stop to end recording at any
time, and the recording will stop at the next bar.
•
Loop: Select Loop to record audio that you intend to play back in sync with your Project using
the Audio plug-in. It records audio in the same way as Sync. However, when Loop mode is
selected, an additional parameter appears called Target. In Loop mode, the recording is loaded
into an Audio plug-in so that you can immediately hear the results. The Target parameter
dictates how Maschine loads new recordings into the Audio plug-in:
•
Take: Select this to record each new Take into the focused Sound slot. After a Take is
recorded, it will become visible in the Audio Pool and is automatically selected for playback.
You can review all the Takes you’ve captured in the Audio Pool, and you can also select any
of these Takes to make it the one that actively plays back in the Audio plug-in.
•
Sound: Select this Target to enable a layered workflow similar to that achieved with guitar
loop pedals. When using this mode, each recording that you make will be loaded into an
empty Sound Slot in the current Group and Pattern and will begin playing back. Therefore,
each recording that you make will playback layered on top of all the previous recordings
made in that particular Group and Pattern. By layering each new Take onto a new Sound,
you can quickly build a whole pattern. You can continue this process until all empty Sound
slots in the Group are used up. After that, each additional recording will be recorded as a
new Take into the last Sound of the Group that contains an Audio plug-in (and the previous
Takes will still be preserved if you want to switch back to them).
•
Pattern: Select this Target to record similar to the Sound Target described above, except
that each new recording will also be assigned to a new Pattern. This mode can be helpful
when you want to record different variations of a part and then review the variations quickly
by playing each Pattern. For example, the first recording will be placed into an Audio plug-in
in the first available Sound Slot in the Group, and then a new Pattern will be created where
only this new recording is playing back. Making another recording will result in the recording
being loaded into another unused Sound Slot, and another new Pattern will be made where
only this most recent recording is playing. If you switch back to the previous Pattern,
you’ll hear only the previous recording (the newest will automatically be deactivated in the
previous Pattern).
SAMPLING AND SAMPLE MAPPING 436

<!-- page 440 -->

•
Auto: Select this recording mode if you want to automatically sample an external or internal
synthesizer. After selecting this mode, further options are available for setting the notes' stride
(interval), key range, and velocity. You can also let Maschine Software batch process the
samples to automatically find the best loop points, trim silence from the start and endpoints,
and normalize the sound level. Refer to Auto Sampler.
Selecting the input source to record
▶Click the SOURCE selector in the INPUT section to select the type of source you want to record:
•
To record external audio signals connected to your audio interface, select Ext. Ster. (for stereo
signals) or Ext. Mono (for mono signals).
•
To record audio signals coming from Maschine itself, select Internal.
▶Click the INPUT selector to choose between the available source inputs:
•
Ext. Ster.: Selects either of Maschine’s four external stereo inputs In 1–4.
•
Ext. Mono: Selects either of Maschine’s eight external mono inputs: the left (“L”) or right (“R”)
channel of each input pair In 1–4.
•
Internal: Selects the output of any available Group or the Master.
You can easily record the output of a particular Sound by setting SOURCE to Internal,
soloing this Sound, and selecting its parent Group in the INPUT selector.
You can also set SOURCE to Internal, choose as INPUT a Group with a drum kit
loaded, and record your live improvisations on the pads while playing this drum kit.
You will then have your improvisations recorded as Samples, ready to be used, edited,
sliced, etc., as any other Samples in Maschine.
Monitoring the input signal
Visually controlling the input signal.
The level meters above the RECORDING section show you at any time the level of the selected
audio source. For example, this can come in handy to adjust the appropriate threshold in Detect
mode. For this purpose, in Detect mode, the level meters also provide a fader adjusting the
threshold level for this purpose. This fader is a strict equivalent to the THRESHOLD control
described above. This way, you can easily visualize when the input signal exceeds the current
threshold (and hence, when it would start the recording) and adjust that threshold accordingly.
Monitoring the input signal.
Furthermore, if you have selected an external signal (Ext. Ster. or Ext. Mono selected in SOURCE),
an additional MONITOR section appears on the right. In this section, activate the MONITOR button
to send the input signal to the Cue bus of Maschine, allowing you to hear on a separate channel
(for example, your headphones) the audio source that is about to be recorded.
SAMPLING AND SAMPLE MAPPING 437

<!-- page 441 -->

For more information on using the Cue bus, please refer to section Using the Cue bus.
Arming, starting, and stopping the recording
The Start and Cancel buttons.
▶Click Start to arm the recording.
After the recording has been armed, its behavior will depend on the recording mode you have
selected (via the MODE selector, refer to section Selecting the source and the recording mode
above):
•
When recording in Detect mode:
•
The recording will start as soon as the input signal exceeds the THRESHOLD value. Until
then the Start button turns to a Waiting button and the Waiting for input… message
appears in the information bar above the waveform display. During this waiting phase you
can also start the recording manually by clicking the Waiting button or cancel the recording
by clicking Cancel.
•
Once the recording has started, click Stop to stop the recording (it stops immediately) or
Cancel to cancel the recording (the recorded audio will not be saved).
•
When recording in Sync mode:
•
The recording will start at the next bar. Until then the Start button reads a flashing Waiting
label and the Waiting for the next bar… message appears in the information bar above the
waveform display.
•
Once the recording has started, the audio is recorded for the duration set by the LENGTH
control (refer to Selecting the source and the recording mode above). You can also click
Stop beforehand to stop the recording at the next bar, or Cancel to cancel the recording (in
that case the recorded audio will not be saved).
•
When recording in Loop mode:
•
The recording will start at the beginning of the Pattern. Until then the Start button reads
a flashing Waiting label and the Waiting for end of Pattern… message appears in the
information bar above the waveform display.
•
Once the recording has started, the audio is recorded for the duration set by the LENGTH
control (refer to Selecting the source and the recording mode above). You can also click
Stop beforehand to stop the recording at the next bar, or Cancel to cancel the recording (in
that case the recorded audio will not be saved).
If you want to start and stop the recording manually, you can set the MODE to Detect,
dial the THRESHOLD down to OFF, and start the recording by clicking Start. To stop
recording, click Stop.
In any case the recorded audio will be stored in the Sound that was under focus as you started the
recording.
SAMPLING AND SAMPLE MAPPING 438

<!-- page 442 -->

When Recording is Complete
When the recording is done, the following things happen:
•
Each Take is named and stored as a file on your hard disk (refer to Location and name of your
recorded Samples).
•
Its waveform appears in the waveform display and its name appears in the information bar
above.
•
The recording is automatically appended to the Audio Pool of the Sound and selected (refer to
Checking your recordings below).
•
A Sampler Plug-in is automatically loaded in the first Plug-in slot of the Sound, ready to play
your new recording. All Plug-ins previously loaded in that Sound are removed. However, when
recording in Loop mode, an Audio plug-in will be loaded. If there was already a Sample Plug-in
in the Slot when engaging Loop recording, it will not change the Sampler to an Audio plug-in, it
will remain as a Sampler and you will need to manually change the plug-in to Audio if you wish.
In this case all recorded takes will be preserved.
•
The Sound slot takes the name of your recording.
•
If the Sampler Plug-in was used in Detect mode or Sync mode, the recording is mapped to a
new Zone covering the entire key and velocity ranges in the Zone page, which makes your new
sample directly playable from the pad of its Sound slot (or from all your pads if pads are in
Keyboard mode). Any existing Zones will be replaced. The sample must then be triggered using
MIDI Events in the Pattern Editor. For more information on Zones, refer to section Mapping
Samples to Zones.
•
If the Audio Plug-in was used in Loop mode, the last recorded Take will automatically play back
with the Pattern.
Note that any MIDI Events for that Sound in the current Pattern will remain. As a
consequence, your recording might directly start to play at the pitch defined by the
existing MIDI Events.
Checking your recordings
You can visualize the last recordings you have made in the current Sound:
SAMPLING AND SAMPLE MAPPING 439

<!-- page 443 -->

The waveform display and the information bar displaying a recording.
(1) Waveform display
Shows the waveform of the recording currently selected in the Audio Pool (5) — by default your last
recording:
•
Use the scroll wheel of your mouse to zoom in/out. You can also use the zooming scroll bar (2).
•
When the Sample is played back (e.g., by pressing the pad or by clicking the little play icon in
the information bar (4)), a playhead indicator (white vertical line) shows you the current play
position within the waveform.
•
Right-click (macOS: [Ctrl]-click) anywhere in the waveform to open a context menu with the
following commands:
Command
Description
Open containing
folder
Opens the folder on your hard disk containing the Sample, providing
quick access to the original file.
Save Sample As…
Opens a Save Sample As dialog allowing to save the recorded Sample
under another name and/or to another location on your computer.
(2) Zooming scroll bar
Click the main part of the scroll bar and drag your mouse horizontally to scroll through the
waveform on the horizontal axis (time), or drag it vertically to zoom in/out on the same time axis.
You can also click the left or right handle of the scroll bar and drag it horizontally to zoom in/out
while keeping the opposite border of the display at a fix position in the waveform. Double-click the
main part of the bar to reset the zoom and display the entire waveform. Alternatively you can use
the scroll wheel of your mouse when hovering the waveform display (1) to zoom in/out.
(3) Timeline
Shows the time scale in bars (Sync mode) or seconds (Detect mode).
(4) Information bar
Displays the file name and the length of the recorded Sample. Click and hold the little play icon on
the left to listen to the Sample on the Cue bus (refer to Using the Cue bus for more information).
Click the little circle (or pair of circle) at the far right to switch the waveform display (1) between
single-channel and two-channel display.
SAMPLING AND SAMPLE MAPPING 440

<!-- page 444 -->

(5) Audio Pool
All the takes you have made since you opened the current Project are stored in the Audio Pool and
displayed as mini waveforms under the waveform display. The following actions are available:
•
Click any take to display the recording, you can then further edit this recording via the other
pages of the Sample Editor. When selected, a recording is also automatically mapped to a new
Zone covering the entire key and velocity ranges in the Zone page. Any existing Zones will be
replaced.
•
Click and hold the little play icon in the bottom right corner to listen to the Sample on the Cue
bus without loading it in the waveform nor in the Zone page.
•
Click the little cross at the top right corner of a mini waveform to delete this particular
recording.
•
Drag any mini waveform to another Sound slot to load it in that Sound.
Right-click (macOS: [Ctrl]-click) any mini waveform in the Audio Pool to open a context menu with
the following commands:
Command
Description
Delete
Deletes the displayed take from the Audio Pool. This has the same effect
as clicking the little cross at the top right corner of the selected mini
waveform in the Audio Pool.
Remove unused
recordings
Deletes from the Audio Pool all takes that are not currently mapped to any
Zone in the Zone page.
Map recordings
to zones
Automatically maps all recordings of the Audio Pool to Zones in the Zone
page. The created Zones are put on adjacent keys and cover the entire
velocity range. Any existing Zones will be replaced.
All recordings (takes) in the Audio Pool are saved with the Project. When you close the
current Project, all of your takes are saved as audio files and available for later use in
the Audio Pool, unless you explicitly delete them (via the Maschine software or in your
operating system).
Location and name of your recorded Samples
By default, recorded Samples (takes) are saved in the Recordings subfolder of your Standard
User Directory, as defined on the User pane of the Library page in the Preferences panel (see
Preferences – Library page). If you activate the Prefer Project Folder option on the General page
of the Preferences panel (see Preferences – General page), recorded Samples will be saved
instead in a Recordings subfolder of the folder where your current Project is saved.
Recorded Samples are automatically named using the following scheme:
[YYMMDD]T[HHMMSS].wav
In the name above, [YYMMDD] stands for the current date (year, month, day, all 2-digit numbers)
and [HHMMSS] for the current time (hours, minutes, seconds, all 2-digit numbers).
Auto Sampler
Auto Sampler makes it easy to create sampler instruments that you can use in Maschine Software.
You can create a sampler instrument from a MIDI-capable hardware synthesizer, a software
instrument, or a combination of synthesizers, hardware effects, and effect plug-ins.
SAMPLING AND SAMPLE MAPPING 441

<!-- page 445 -->

Sampling instruments is a great way to capture other instruments and save on CPU resources,
especially when sampling instruments that have effects. Used creatively, you could also turn any
monophonic synthesizer into a polyphonic powerhouse.
Instruments created with Auto Sampler can be saved as a Sound and all its samples. This is a
great way to share your sampled instruments with other Maschine users or between Maschine+
and your desktop.
Using effects when creating a sampler instrument is a creative process but is different
from using effects in real-time in two ways: first, effects are applied to each sampled
note, not on multiple notes or chords; and second, effects parameters cannot be
edited or automated to produce changes in the sound over time.
Before using the Auto Sampler, you must first set up the devices you want to record and access the
Recording mode of the Sampler. Refer to Creating a sampled instrument using Auto Sampler for
more information.
Creating a sampled instrument using Auto Sampler
To create a sampled instrument using Auto Sampler:
1. Click the Sample icon to access the Sampler Editor. Refer to Opening the Sample Editor.
2. Select Auto from the Recording mode field at the bottom of the interface. Refer to Selecting the
source and the recording mode.
Recording an external instrument
▶If you are sampling an external device such as a synthesizer, connect the instrument to your
Maschine (audio and MIDI), then select Input Source to External. Refer to Input.
▶Ensure that Maschine can receive audio input from the external device on the correct audio
input. Refer to Monitor.
Recording an internal instrument
▶If you want to sample a Plug-in, select Input Source to Internal and the Input to Group and
Sound of the plug-in you want the Auto Sampler to capture. Refer to Input.
Once you have set up the Auto Sampler, you can make settings regarding the notes, velocities, and
batch processing you want Auto Sampler to perform. Refer to
Recording
The recording section enables you to set the recording mode, the sample length, and the note
length of the sample you want to record.
Setting
Description
MODE
Sets the recording mode of the Sampler. Select Auto to use Auto-Sampler.
SAMPLE
Sets the length of time Auto-Sampler records samples. For example, choose short
times for percussive sounds or bass stabs, and longer times for strings and
pads. If you want to loop your sound, it is helpful to record for longer to give
Maschine enough material to find the best loop points. For the best results, use
this parameter in conjunction with the NOTE ON parameter.
SAMPLING AND SAMPLE MAPPING 442

<!-- page 446 -->

Setting
Description
NOTE ON
Sets the length of time Auto-Sampler triggers the instrument it is recording. For
the best results, use this parameter in conjunction with the SAMPLE parameter.
Input
The Input section lets you set the source you want to record and select the MIDI device and
channel when triggering external MIDI instruments.
Setting
Description
SOURCE
Ext. Ster.: Selects external stereo inputs as the recording source type.
Ext. Mono: Selects external mono inputs as the recording source type.
Internal: Selects the internal output Maschine as the recording source type.
INPUT
Ext. Mono: Selects either of Maschine’s eight external mono inputs: the left (“L”)
or right (“R”) channel of each input pair In 1–4.
Ext. Ster.: Selects either of Maschine’s four external stereo inputs In 1–4.
Internal: Selects the output of any available Group or the Master channel.
MIDI TO
Sets the MIDI port you want to use when connecting to external MIDI equipment.
All available devices are shown here.
CHANNEL
Sets the MIDI channel to match the MIDI channel of the external equipment
you want to sample. Maschine will use this to trigger the sound when making
recordings.
Note Map
The Note Map section enables you to set the number of notes and the range of the keyboard
covered by each sample.
Setting
Description
STRIDE
Sets the number of notes that each sample will cover. A Stride value of 1 records
every note within the Key Lo and Key Hi range. For example, a Stride of 5 to
accurately capture every note in the Key Lo and Key Hi range. Alternatively, you
could set a higher Stride value, resulting in fewer samples. A value of 12, for
example, would cover 12 notes, meaning one sample would be stretched across a
range of notes. This could result in possible pitch artifacts, but the value you select
depends on the sound you want to achieve.
KEY LO
Sets the lowest note of the sample note range.
KEY HI
Sets the highest note of the sample note range.
EXTEND
Extends the highest and lowest samples to include the whole range of the
keyboard.
SAMPLING AND SAMPLE MAPPING 443

<!-- page 447 -->

Velocity Map
The Velocity Map section lets you set the velocity covered by each sample within the velocity
range.
Setting
Description
STRIDE
Sets the velocity range each sample will cover as the Auto-Sampler triggers
sounds. If, for example, you wanted to capture every nuance of sound, you could
use a Stride value of 1 to record every velocity set within the Vel Lo and Vel Hi
range. Alternatively, you could set a higher Stride value, resulting in fewer samples
for a broader sample of the sound.
VEL LO
Sets the lowest velocity value you want to sample.
VEL HI
Sets the highest velocity you want to sample.
EXTEND
Extends the upper and lower velocity values to include the full velocity range of the
instrument.
Batch Process
The Batch Process section provides a set of time-saving tools that help you by automating the
process of looping, trimming, and normalizing your samples.
Setting
Description
FIND LOOP
Automatically finds the best loop point in your samples. This feature is
useful if you want to create sustained sounds such as pads or strings.
TRIM SILENCE
Automatically removes unwanted silence from the beginning and end of
each sample.
NORMALIZE
Adjusts the level of each sample to the maximum possible value without
clipping. Normalizing audio is useful for making samples more consistent in
volume.
Monitor
The Monitor section enables you to hear the output of the Auto-Sampler.
Setting
Description
MONITOR
Activates the monitor, which enables you to hear the Auto-Sampler as it works
through the process of capturing samples.
Editing a Sample
The Edit page of the Sample Editor in the software and its equivalent the EDIT page of the
Sampling mode on your controller allow you to adjust the start and end points of a Sample or Slice
and to apply various destructive audio processing functions to any part of the Sample.
Sample Editing can only be done in the Sampler plug-in, not using the Audio plug-in. If
you want to edit a Sample in the Audio plug-in, you must first switch it to a Sampler
Plug-in, make the edit, and then switch back to the Audio Plug-in again.
SAMPLING AND SAMPLE MAPPING 444

<!-- page 448 -->

Which Sample is shown in the Edit page?
The Edit page (EDIT page on your controller) always displays the Sample of the Zone currently
selected (refer to Selecting and managing Zones in the Zone List for more information on
selecting Zones), and all your actions in that page will affect this particular Sample. For example:
•
If you have just recorded a Sample, it will directly appear here. If you have recorded more
than one Sample, the Sampled selected in the Recording History (by default the last recorded
Sample) will appear here, refer to section Checking your recordings for more information on
the Recording History.
•
If the Sample in that Sound is already split into Slices, each Slice has its own Zone and the Slice
of the focused Zone will appear here. See section Slicing a Sample for more information on
slicing Samples.
Using the Edit page
▶In the Sample Editor, click the Edit tab at the top to open the Edit page.
The Edit page looks as follows:
The Edit page in the software.
(1) Waveform display
Shows the waveform of the Sample for the focused Zone. The waveform display provides
following tools:
•
Drag any Sample onto the waveform to replace the current Sample for the focused Zone. If
there is no Sample loaded yet, this automatically loads a Sampler Plug-in in the Sound and
creates a Zone over the entire key and velocity ranges for the dragged Sample.
•
Use the scroll wheel of your mouse to zoom in/out. You can also use the zooming scroll bar (4).
•
Play range: The S and E markers indicate the start and end points of the play range,
respectively. Drag them with the mouse to modify the portion of the Sample that will be played
back. This can also be done using the controls in the PLAY RANGE section (5).
SAMPLING AND SAMPLE MAPPING 445

<!-- page 449 -->

•
Loop range: If a loop has been defined in the Sample, it is also indicated on the waveform. You
can then adjust the loop by dragging its borders, and move the entire loop by dragging its title
bar. Loops can be created and adjusted in the Zone page — see section Selecting and editing
Zones in the Map view. Note that the loop will always stay within the play range. Therefore,
when moving the Sample’s start and end points closer to each other, keep in mind that it might
also shrink the loop!
•
Playhead indicator: When the Sample is played back (e.g., by pressing the pad or by clicking the
little play icon in the information bar (2)), a playhead indicator (white vertical line) shows you
the current play position within the waveform.
•
Selection range: Click and drag your mouse to create a selection range. The selection range
defines the portion to which the audio processing functions of the Audio Toolbar (7) will be
applied. Adjust the current selection range by dragging its borders or move it by dragging its top
part. Double-click anywhere in the waveform to set the selection range to the play range (i.e. to
select everything between the S and E markers). You can also select particular ranges via the
context menu (see below) and via the controls in the SELECTION RANGE section (6).
•
Context menu: Right-click (macOS: [Ctrl]-click) anywhere in the waveform to open a context
menu with the following commands:
Command
Description
Deselect
Cancels the current selection range.
Select All
Selects the entire Sample.
Select Play Range
Selects the play range, i.e. the region between the S and E markers. This
is equivalent to double-clicking anywhere in the waveform.
Select Loop
Selects the loop range.
Find in Explorer
Opens the folder on your hard disk containing the Sample, providing
quick access to the original file.
Save Sample As…
Opens a Save Sample As dialog allowing to save the Sample under
another name and/or to another location on your computer.
(2) Information bar
Displays the file name and the length of the recorded Sample. Click and hold the little play icon
on the left to play back the whole Sample on the Cue bus (refer to Using the Cue bus for more
information). Click the little circle (or pair of circle) at the far right to switch the waveform display
(1) between single-channel and two-channel display.
(3) Timeline
Shows the time scale in seconds.
(4) Zooming scroll bar
Click the main part of the scroll bar and drag your mouse horizontally to scroll through the
waveform on the horizontal axis (time), or drag it vertically to zoom in/out on the same time axis.
You can also click the left or right handle of the scroll bar and drag it horizontally to zoom in/out
while keeping the opposite border of the display at a fix position in the waveform. Double-click the
main part of the bar to reset the zoom and display the entire waveform. Alternatively you can use
the scroll wheel of your mouse when hovering the waveform display (1) to zoom in/out.
(5) PLAY RANGE section
Adjusts the range that will be played when you trigger a note. Adjust the play start and end points
in the Sample via the Start and End parameters. You can also do it by dragging the white markers
labeled S and E on the waveform display (1) using the mouse as described above.
SAMPLING AND SAMPLE MAPPING 446

<!-- page 450 -->

(6) SELECTION RANGE section
Adjusts the range to which audio processing functions will be applied. You can also select the
range by dragging your mouse on the waveform display (1) as described above.
(7) Audio Toolbar
Provides a set of destructive audio processing functions to modify your Sample. The functions will
be applied to the current selection range. The available functions are described in section Audio
editing functions below.
You can also edit the play and loop ranges on the Zone page. See section Adjusting
the Zone settings for more information.
Audio editing functions
In the Edit page, the Audio Toolbar provides various audio functions. These will be performed on
the selected region of the Sample, as defined by the Start and End parameters of the SELECTION
RANGE section (refer to Using the Edit page above).
▶To apply any audio function to the selected region in your Sample, click the desired icon in the
Audio Toolbar.
Most of these audio processing functions are destructive, that is, they modify the
audio material in the Sample. However, your original Sample will not be modified: For
each audio function that you perform, a new, distinct copy of the Sample will be saved.
Besides, you can always cancel your last action(s) by pressing [command] + [Z] (Mac)
or [Ctrl] + [Z] (Windows) on your computer keyboard.
The playback settings of the Sample (e.g., tune, amplitude envelope, etc.) can be
adjusted on the Zone page. See section Selecting and editing Zones in the Map view
for more information.
The Audio Toolbar.
The Audio Toolbar provides following audio processing functions:
Command
Description
Truncate
Deletes the part of the Sample that is outside of the selected region.
Norm.
(Normalize)
Adjusts the level of the selected region to the maximum possible value
without clipping.
Reverse
Reverses the selected region of the Sample.
Fade In
Applies a fade in to the selected region of the Sample.
Fade Out
Applies a fade out to the selected region of the Sample.
SAMPLING AND SAMPLE MAPPING 447

<!-- page 451 -->

Command
Description
Correct
Removes the DC offset. DC offset (“Direct Current offset”) is an undesirable
constant shift in the signal level that might be introduced by some audio
processing units. This offset can notably waste some of the available
headroom.
Silence
Silences the selected region of the Sample.
Cut
Deletes the selected region from the Sample and places it into the clipboard
for later use.
Copy
Copies the selected region of the Sample to the clipboard for later use.
Paste
Pastes the cut/copied region of the Sample, replacing the region of the
Sample currently selected.
Dupl.
(Duplicate)
Duplicates the selected region of the Sample. The copy is placed right after
the original region.
Stretch
Allows you to apply time stretching and/or pitch shifting to the selected
region of the Sample. See below for a detailed description.
Stems
Separates the Sample into four distinct components or “stems”: drums and
percussion, bass, other, and vocals. The third stem (“other”) is what remains
in the Sample after removing all other stems, and can vary from Sample
to Sample. When you click Stems, the icon switches to a percentage value
indicating the progress of the stem separation. This processing runs in
the background and you can continue with other work until the separation
has been completed. You can also click Cancel at any time to cancel the
separation process. Upon completion, a new Group will automatically be
created, with its first four Sound slots containing the four stems (drums,
bass, vocals, other) loaded in Sampler modules, ready to be played. The
stems will appear as individual Samples in the user content of your
Maschine library. Their name mirrors that of the original Sample, followed
by the particular component (Drums, Bass, Other, or Vocal).
Only one stem separation process can be started at a time. While a stem
separation process is running, the Stems button of the other Sound slots is
grayed out and not available.
Time stretching / pitch shifting
When you select STRETCH in the Audio Toolbar, the bottom of the Edit page switches to the
following set of controls:
The stretch controls at the bottom of the Edit page.
These controls allow you to adjust the parameters of the time stretching / pitch shifting function
before applying it to the selected region. Pitch shifting and time stretching can be applied
independently.
The following parameters are available:
SAMPLING AND SAMPLE MAPPING 448

<!-- page 452 -->

Parameter
Description
STRETCH section
TUNE
Adjusts the detuning (pitch shifting) to be applied (in semitones and
cents). Leave this value to 0.00 to leave the original pitch untouched.
FORMANT C
(Formant
Correction)
Enables/disables the formant correction. Formant correction allows the
pitch-shifted audio to retain the timbre (or “color”) of the original audio
as much as possible. This is especially useful for melodic instruments.
MODE
Selects between Beat and Free mode:
In Beat mode, the new tempo is defined relative to the time signature
(the beats and bars) of the original audio. This can be useful if you
sampled a loop with a clearly defined rhythm (e.g., a drum loop).
In Free mode, the new tempo is defined independently from the time
signature of the source. This is more suited for non-rhythmic Samples.
In this mode only one parameter is available: SPEED (refer to below).
AUTO DTCT (Auto
Detection, Beat
mode only)
If activated, Maschine automatically detects the tempo of the original
audio.
SRC BPM (Source
BPM, Beat mode
only)
Allows to define the tempo of the original audio (in BPM). This tempo is
defined in different ways according to the AUTO DTCT value:
If AUTO DTCT is activated, you can set the length (in bars) of the
original audio. You can choose between 1/2, 1, and 2 bars. The number
between brackets indicates the resulting tempo (in BPM) derived from
the number of bars you have set and the computed tempo value.
If AUTO DTCT is deactivated, you can directly define the tempo of the
original audio (in BPM).
NEW BPM
(Beat Mode only)
Defines the target tempo of the time-shifted audio (in BPM).
LENGTH (Stretch
Length, Beat mode
with Auto Detection
activated only)
If AUTO DTCT is activated, you can define the length of the target audio
(in bars). Please note that any change to the SRC BPM value (refer
to above) will be automatically mirrored by this LENGTH value. Once
you have set the number of bars in the source audio, you can set here
another number of bars, thereby dividing or multiplying the tempo of
the target audio. Available values are 1/16, 1/8, 1/4, 1/2, 1, 2, 4, and 8
bars, as well as the corresponding triplet values.
SPEED
(Free mode only)
Adjusts the new tempo relative to the original tempo (in percentage).
The minimum value is 10 %.
SAMPLING AND SAMPLE MAPPING 449

<!-- page 453 -->

In Beat mode, if you set a target tempo that is smaller than a tenth of the original
tempo, the Apply button will be deactivated. Set a higher target tempo to enable the
Apply button again!
▶Once you have set the parameters to the desired values, click Apply to apply the pitch shifting
and/or time stretching to the selected region in the Sample, or Cancel to let the Sample
untouched.
Slicing a Sample
Slicing allows you to chop up loops to extract single Sounds (the drum sounds of a drum loop
for example), but it's also good for preparing a loop to be played back at another tempo without
changing its pitch or timing. The resulting Slices can then be exported to different notes of the
same Sound or to different Sounds of the same Group.
The Slice page of the Sample Editor in the software and its equivalent the SLICE page of the
Sampling mode on your controller allow you to slice your Samples in various ways.
The typical workflow for slicing your Samples is as follows:
1. Open the Slice page (SLICE page on the controller): Opening the Slice page.
2. Choose a method for slicing along with a few settings depending on the chosen method:
Adjusting the slicing settings.
3. If you wish, manually adjust the proposed Slices: Manually adjusting your slices.
4. Apply the slicing to your Sample and export the Slices — whether in place or to another Sound/
Group: Applying the slicing.
Opening the Slice page
In the software, slicing a Sample is done in the Slice page of the Sample Editor.
▶In the Sample Editor, click the Slice tab at the top to open the Slice page.
The Slice page looks as follows:
The Slice page in the software.
SAMPLING AND SAMPLE MAPPING 450

<!-- page 454 -->

Adjusting the slicing settings
At the bottom of the Slice page, you can adjust the settings used to define where the various Slices
will be created in the Sample.
Adjust the slicing settings at the bottom of the Slice page.
Any change to these settings will directly affect the number and position of the Slice markers
displayed on the waveform above.
At any time you can audition the proposed Slices on the Cue bus (refer to Using the Cue bus for
more information) by pressing the lit pads or clicking the Slices on the waveform display.
Following parameters are available:
Parameter
Description
SLICER Section
MODE
Here you can select either Split, Grid, Detect or Manual:
Detect mode: The Sample will be sliced according to its transients.
Split mode: The Sample will be sliced into equally spread Slices.
Grid mode: The Sample will be sliced according to note values.
Manual mode: Manually enter slice points using the pads on your
controller, or adjust the start and end points of a slice.
SLICES (Split and
Grid mode only)
When MODE is set to Split (see above), SLICES lets you choose the
amount of Slices: 4, 8, 16 or 32.
When MODE is set to Grid (see above), SLICES lets you choose the length
of the Slices in note values: 4th, 8th,16th or 32nd notes.
AUTO-SNAP
(Manual mode
only)
The Sample Slicer Manual mode Auto-Snap feature automatically aligns
Slice points to the nearest transient as you manually trigger the slicing
from the pads. It can be turned off so that slice points are instead placed
exactly where you trigger them. In order to use Auto-Snap, you must wait
for analysis to be performed on the sample you’re slicing—the analysis is
very quick but will take longer for long audio files.
SENSITIVITY
(Detect mode
only)
When MODE is set to Detect (see above), SENSITIVITY lets you adjust
the sensitivity of the transient detection. Higher values will cause more
Slices to be detected because more transients will be recognized, lower
values will result in less Slices. This parameter should be adjusted until all
the musically significant slices are being detected in the waveform.
APPLY Section
SAMPLING AND SAMPLE MAPPING 451

<!-- page 455 -->

Parameter
Description
MONO
The Sample Slicer Mono option when activated automatically sets the
Voice and Choke Group of all sample slices to 1 when slicing to a Group.
This time saving feature is useful when you don’t want to have lots of
samples triggered or repeating at the same time, for example, when you
slice a drum loop and trigger the individual hits to form a new pattern.
When Mono is selected and the slices are applied to a Group, the sampler
polyphony is automatically set to 1 so only one voice will play at a time.
The Choke Group is also automatically set to 1 so each new pad that
is hit will always take priority over the previous one by cancelling it out.
This behavior can be found on vintage drum machines (typically used
to “choke” the open hi-hat with the closed one), but also in monophonic
synthesizers that are only capable of playing one note at a time.
BPM (BPM
Mode)
Selects how the tempo is defined: If you select Auto, Maschine will
calculate the tempo automatically. If you select Manual, you can enter
the tempo in BPM manually.
ADJUST
If BPM is set to Auto, you can choose between the tempo that Maschine
detected, or half or double of that tempo. If BPM is set to Manual, you
can adjust the tempo manually.
ENGINE Section
(Detect mode only)
ZERO-X (Zero
Crossing, Detect
mode only)
When MODE is set to Detect, activate ZERO-X to force the detected
Slices to be created on the closest locations where the audio signal
crosses the zero value. This can be helpful to avoid clicks when playing
back Slices in another sequence.
Manually adjusting your slices
In addition to the Detect, Split, Grid, and Manual modes that create Slices automatically (refer to
Adjusting the slicing settings above), you can also adjust Slices manually using your mouse, the
waveform display, and the various edit tools at your disposal.
You can directly adjust your Slices manually by selecting Manual in the MODE
selector, or start from Maschine’s proposed Slices as described in section Adjusting
the slicing settings and fine-adjust these Slices manually — in that case the MODE
selector automatically switches to Manual.
SAMPLING AND SAMPLE MAPPING 452

<!-- page 456 -->

Manually adjusting your Slices.
(1) Waveform display
Shows the selected Sample with a couple of spread vertical lines in the waveform: this is where the
Slices are going to be applied (i.e. cut).
•
Hover a Slice with the mouse to select it (it is highlighted). Little “S” and “E” markers appear at
the bottom of the Slice borders to indicate the start and end point of that Slice, respectively.
•
Use the scroll wheel of your mouse to zoom in/out. You can also use the zooming scroll bar (2).
•
When the entire Sample or a particular Slice is played back, a playhead indicator (white vertical
line) shows you the current play position within the waveform.
•
Context menu: Right-click (macOS: [Ctrl]-click) anywhere in a Slice to open a context menu with
the following commands:
Command
Description
Open containing
folder
Opens the folder on your hard disk containing the Sample, providing
quick access to the original file.
Save Sample As…
Opens a Save Sample As dialog allowing to save the Slice under as a
distinct file on your computer.
By default, you can adjust Slices with your mouse as follows:
•
Click inside a Slice (i.e. anywhere between its borders) to play it back on the Cue bus (refer to
Using the Cue bus for more information).
•
Drag the borders of a Slice to adjust them. You have two possibilities:
•
If the end point of the previous Slice and the start point of the next Slice are joined, drag the
border’s vertical line to move both the end point of the previous Slice and the start
point of the next Slice together, so that both Slices stay joined.
•
Drag the little “S” (or “E”) marker at the bottom of the vertical line to move the start (or end)
point of a Slice independently of the end (or start) point of the previous (or next) Slice. If you
want this border to stick again with that of the previous (or next) Slice, drag the vertical
line (instead of the “S”/“E” marker) toward that of the previous (or next) Slice.
SAMPLING AND SAMPLE MAPPING 453

<!-- page 457 -->

By moving the start and end points of Slices independently, you can create
overlapping Slices or gaps between Slices.
These default mouse actions are valid only if the SLICE and REMOVE buttons are deactivated in
the edit tools (5). Enabling any of them provides alternative mouse controls described below.
(2) Zooming scroll bar
Click the main part of the scroll bar and drag your mouse horizontally to scroll through the
waveform on the horizontal axis (time), or drag it vertically to zoom in/out on this time axis. You
can also click the left or right handle of the scroll bar and drag it horizontally to zoom in/out while
keeping the opposite border of the display at a fix position in the waveform. Double-click the main
part of the bar to reset the zoom and display the entire waveform. Alternatively you can use the
scroll wheel of your mouse when hovering the waveform display (1) to zoom in/out.
(3) Timeline
Shows the time scale in seconds.
(4) Information bar
Displays the file name and the length of the selected Sample. Click and hold the little play icon
on the left to play back the whole Sample on the Cue bus (refer to Using the Cue bus for more
information). Click the little circle (or pair of circle) at the far right to switch the waveform display
(1) between single-channel and two-channel display.
(5) Edit tools
The three buttons in the edit tools allow you to add or remove Slices:
•
SLICE: When the SLICE button is activated, the default mouse behavior in the waveform display
is replaced by the following:
•
Click inside a Slice to split it into two Slices at that location.
•
Adjust the borders of existing Slices as described above in the waveform display (1).
•
REMOVE: When the REMOVE button is activated, over the waveform display the mouse pointer
turns into a rubber icon and the default mouse actions are replaced by the following:
•
Click the start border of a Slice to delete that border and merge the Slice with the previous
one.
•
Click inside a Slice (i.e. anywhere between its borders) to remove the entire Slice. The
corresponding part of the Sample is grayed out and won’t be exported as Slice.
•
DELETE ALL: Click the DELETE ALL button to delete all proposed Slices and start slicing from
scratch again.
The SLICE and REMOVE buttons are mutually exclusive.
With SLICE or REMOVE activated, you can still prelisten to your individual Slices by
pressing the corresponding pads on your controller!
SAMPLING AND SAMPLE MAPPING 454

<!-- page 458 -->

Applying the slicing
Once you are satisfied with the proposed and/or manually adjusted Slices (refer to Adjusting the
slicing settings and Manually adjusting your slices), you can apply the slicing in order to actually
cut the original Sample and create the Slices. This is done via the three elements at the bottom
right of the Slice page:
You can apply the slicing in various ways.
(1) Apply button
Exports the Slices to the same Sound. If you click Apply, the Slices will be mapped to individual
notes of this Sound, the Sample Editor will be replaced by the Pattern Editor in Keyboard view, and
the pads of your controller will switch to Keyboard mode so that you can directly play your Slices
on the pads. Additionally, depending on the setting of the Pattern Creation selector (3), some notes
can be automatically created for each Slice (see below).
The Apply button (1) can be seen as a shortcut for dragging the Slice Dragger to the
focused Sound itself.
(2) Slice Dragger
Drag the Slice Dragger to export the Slices to any other Sound or Group:
•
If you drag to a Sound (in the Sound List at the left of the Sample Editor):
•
The Slices will be mapped to individual notes of this Sound, starting with the bottom C
(C-2 in Maschine convention). The base key of the Sound will be set to the bottom C as
well (refer to Adjusting the base key for more information on the base key). Any previous
content in the Sound will be replaced.
•
The Sample Editor will be replaced by the Pattern Editor in Keyboard view.
•
The pads of your controller will switch to Keyboard mode so that you can directly play your
Slices on the pads.
•
Depending on the setting of the Pattern Creation selector (3), notes will be automatically
created for each Slice (see below).
SAMPLING AND SAMPLE MAPPING 455

<!-- page 459 -->

•
If you drag to a Group (in the Group List at the left of the Arranger):
•
The Slices will be mapped to individual Sound slots, replacing their current content (if any).
Only the first 16 Slices will be exported.
•
The Sample Editor will be replaced by the Pattern Editor in Group view.
•
The pads of your controller will switch to Group mode so that you can directly play your
Slices on the pads.
•
Depending on the setting of the Pattern Creation selector (3), notes will be automatically
created for each Slice (see below).
(3) Pattern Creation selector
Selects from three modes controlling the automatic note creation upon Slice export. The mode
selected here will be used both when clicking the Apply button (1) and when using the Slice
Dragger (2). Following options are available:
•
Create Pattern (default setting): Upon Slice export a new Pattern will be created with one note
for each pitch (if Slices are exported to a Sound) or one note for each Sound (if Slices are
exported to a Group) so that the Pattern reproduces the original, unsliced Sample.
•
Replace Pattern: Upon Slice export a sequence of notes will be created in the current Pattern
so that the Pattern reproduces the original, unsliced Sample. If the sequence is shorter than the
current Pattern it will be repeated to fill the Pattern; if the sequence is longer than the Pattern
the Pattern will be extended according to the Pattern Grid and the content of other Sounds will
be repeated.
•
If Slices are exported to a Sound, the sequence of notes will contain one note for each pitch.
Any existing notes for that Sound will be replaced. Notes for other Sounds in the Pattern will
stay untouched.
•
If Slices are exported to a Group the sequence of notes will contain one note for each Sound
containing a Slice. Any existing notes for these Sounds will be replaced. Notes for other
Sounds in the Pattern will stay untouched.
•
No Pattern: No Pattern is created, and the current Pattern is left untouched.
Play around with the slicing feature by removing some of these notes, quantizing or
completely rearranging them.
The notes in the picture above represent the Slices and trigger them in order to play the Sample
with correct timing and pitch. If you change the tempo of your Project, you will hear that the loop
automatically adjusts to the new tempo.
Exporting single Slices
You can also export an individual Slice to another Sound by drag-and-drop:
SAMPLING AND SAMPLE MAPPING 456

<!-- page 460 -->

Dragging an individual Slice to another Sound.
Applying a sliced sample to a Sound
If you drag a Slice to a Group in the Group List (at the left of the Arranger), it will be exported to the
first Sound slot of that Group. Any Sound loaded in that Sound slot will be replaced.
When applying a sliced sample to a Sound in an otherwise empty Group, the root note of the
Sounds in that Group is set to C-2, matching the key zones of the slices.
The root note parameter is shared among all Sounds in a Group. However, when applying slices to
a Sound, these slices will always start at the lowest possible note, to make room for the maximum
number of slices. If you already have Sounds in a Group, the root note is not changed after applying
slices, in order to not change the behavior of the existing Sounds. This will, however, lead to a
mismatch in how you accessed slices across Pads in the Sampling / Slice tab and how they are
laid out in the Sound you applied them to. You will typically play a root note of C3 with Pad 1, while
the lowest slice will start at C-2. To avoid this mismatch, and to access slices on a Sound exactly
as you created them in the Sampling / Slice screen, apply slices to a Sound in a Group where you
have not loaded anything to the other Sounds. This also works when you start by loading a Sample
into a Sound in a Group where you have not yet loaded anything else.
Mapping Samples to Zones
Mapping Samples is a way to create Sounds with more than one Sample across the MIDI keyboard
and with different velocities. You can create and adjust Zones that define a key range (or pitch
range) and a velocity range for each Sample included in the Sound: The Sample will be triggered
only if the played note is within the key range and velocity range of its Zone.
The Zones can overlap, allowing you to trigger different Samples at once or triggering different
Samples depending on how hard you hit the pads. You can adjust various playback settings for the
Sample of each Zone individually. The set of all Zones define the Sample Map (or “Map” for short)
of the Sound.
Opening the Zone page
Mapping is done in the Zone page of the Sample Editor.
▶Select a Sound slot, then open the Sample Editor (by clicking the button with the waveform icon
on the left of the Pattern Editor), and click the Zone tab to show the Zone page.
SAMPLING AND SAMPLE MAPPING 457

<!-- page 461 -->

The Zone page (here for an empty Sound).
Zone page overview
The Zone page provides the following elements:
The Zone page: an overview.
(1) Zone List button: Shows/hides the Zone List (4).
(2) Sample View button: Switches the Zone page between Map view and Sample view (5).
(3) Information bar: Displays the file name and the length of the Sample in the focused Zone. Click
and hold the little play icon on the left to play back the whole Sample on the Cue bus (refer to Using
the Cue bus for more information). Click the little circle (or pair of circle) at the far right to switch
the waveform display (1) between single-channel and two-channel display.
(4) Zone List: Shows all Zones in a list. The Zone List can be shown/hidden by clicking the Zone
List button (1). Click an entry in the list to set the focus to that Zone. You can also select multiple
Zones, move them via drag and drop, and add/delete Zones in the list. See section Selecting and
managing Zones in the Zone List for a complete description of the Zone List.
SAMPLING AND SAMPLE MAPPING 458

<!-- page 462 -->

(5) Map view / Sample view: The Map view is the default view (pictured above). It shows and lets
you edit all Zones contained in your Sound. The Sample view shows the waveform of the Sample
for the focused Zone and lets you edit some of its settings. Click the Sample View button (2) to
switch between the Map view and the Sample view (the Sample view is visible when the Sample
View button is activated). The Map and Sample views are explained in detail in section Selecting
and editing Zones in the Map view and Editing Zones in the Sample view, respectively.
(6) Zone settings: Displays the parameters for the focused Zone. See section Adjusting the Zone
settings for a detailed description of the available parameters.
Selecting and managing Zones in the Zone List
On the left, the Zone List shows all Zones of the focused Sound.
The Zone List in the Zone page.
▶Click the Zone List button next to the Slice tab to show/hide the Zone List.
The Zone List allows you to add, remove, replace, select, and reorder Zones in the list.
You can adjust the width of the Zone List by dragging its right border.
Adding a new Zone to the Zone List
You can add a new Zone to the Zone List in two ways:
▶Drag a Sample from the Browser’s LIBRARY or FILES pane or from your operating system onto
the empty area in the Zone List.
or
1. Click the “+” at the end of the Zone List.
A Load Sample dialog opens up.
SAMPLING AND SAMPLE MAPPING 459

<!-- page 463 -->

2. Navigate to the desired audio file on your operating system and press [Enter] to confirm.
→A new Zone is created at the end of the list containing the dragged or selected Sample.
You can drag and drop several Samples at once, this will create as many new Zones.
You can also add Zones to your Sound by dragging and dropping Samples directly
onto the Sample Map of the Map view. See section Adding Samples to the Sample
Map for more on this.
Replacing the sample of an existing Zone
You can also put a new Sample into an existing Zone, thereby replacing the Sample currently
contained in that Zone. Again, you have two methods at your disposal:
▶Drag a Sample from the Browser’s LIBRARY or FILES pane or from your operating system onto
the desired entry in the Zone List.
or
1. Right-click ([Ctrl]-click on macOS) the desired entry in the Zone List and select Load Sample… in
the menu that opens.
A Load Sample dialog opens up.
2. Navigate to the desired audio file on your operating system and press [Enter] to confirm.
→The dragged or selected Sample replaced the previous Sample in the target Zone.
Selecting a Zone from the list
▶Click any Zone entry in the Zone List to put it under focus.
→The focused Zone gets highlighted in color both in the list and in the Map view (if visible). In
addition:
•
The focused Zone is displayed in the Sample view and its settings appear in the Zone settings
at the bottom of the page. See section Adjusting the Zone settings for more information on
these settings.
•
The focused Zone also appears on the Edit and Slice pages, which allows you to further
process of its contained Sample. For more information on the Edit and Slice pages, please
refer to section Editing a Sample and Slicing a Sample, respectively.
SAMPLING AND SAMPLE MAPPING 460

<!-- page 464 -->

Selecting multiple Zones from the list
You can select several Zones in the list at once using the common methods of your operating
system. The basic rules for multiple selection are the following:
•
The focused Zone is automatically selected. It is highlighted in the color of the Sound and its
waveform and parameters are displayed in the Slice page’s Sample view and Zone settings as
well as on the Edit and Slice pages.
•
The other selected Zones are highlighted in white. Their settings are not displayed anywhere,
however they will be affected by your actions in the Zone List and in the Map view (refer to
Selecting and editing Zones in the Map view for more on this).
Mouse/keyboard action
Command
Multiple selection
Hold [Ctrl] ([Cmd] on macOS) and click
several entries in the list
Selects all clicked Zones. Click a selected Zone to
deselect it (i.e. remove it from the selection).
Hold [Shift] and click two entries
Selects both Zones and all Zones in-between.
Press [Ctrl]+[A] ([Cmd]+[A] on macOS)
Selects/deselects all Zones in the list. When
deselecting, only the focused Zone remains
selected.
Deleting Zones from the list
To remove one or more Zone(s) from the Zone List:
1. Select the Zone(s) you want to remove.
2. Press [Del] or [Backspace] on your computer keyboard.
→The selected Zones are removed from the Zone List and from the Sample Map, and the
corresponding Samples are not used in the Sound anymore.
After you have selected the Zone(s) you want to remove, you can also use the context menu:
1. Select the Zone(s) you want to remove.
2. Right-click ([Ctrl]-click on macOS) any of the selected Zones.A menu opens up.
3. In that menu selects Delete to remove the focused Zone only, or Delete Selected to remove all
selected Zones.
Moving Zones in the list
You can move your Zones across the Zone List via drag and drop:
1. Select the Zone(s) you want to move.
SAMPLING AND SAMPLE MAPPING 461

<!-- page 465 -->

2. Click and hold the mouse button, and drag your mouse vertically.As the mouse pointer moves,
an insertion line appears at various places between the existing entries.
3. When the insertion line indicates the desired location, release the mouse button to drop the
selected Zone(s) to this new place.
Moving Zones allow you to reorder the Zone List. This can come in handy before you
run the Map as Drum Kit command from the Sample Map’s context menu, so that
your Samples are well ordered in the new mapping. See section Selecting and editing
Zones in the Map view for more information on the Sample Map.
Selecting and editing Zones in the Map view
The Map view is visible when the Sample View button (showing a little waveform icon at the right
of the Zone tab) is deactivated.
Disable the Sample View button to see the Map view.
The Map view contains the following elements:
The Map view of the Zone page.
(1) Sample Map
The Sample Map shows all Zones contained in your Sound.
•
The horizontal axis represents keys (or pitches) from C-2 to G8, while the vertical axis
represents velocities from 0 to 127.
SAMPLING AND SAMPLE MAPPING 462

<!-- page 466 -->

•
Each Zone is depicted as a rectangle defining a specific key range (the rectangle’s width) and a
velocity range (the rectangle’s height). Any note played within these key and velocity ranges will
trigger the Sample of that Zone.
•
You can zoom in/out both horizontally and vertically via the zooming scroll bars (3) and (4),
respectively.
•
Each Zone header displays the name of the corresponding Sample.
•
Click a Zone in the Map to put it under focus. The focused Zone is highlighted; its information
and parameters are displayed in the Zone settings at the bottom of the Zone page.
•
You can select multiple Zones at once: All your mouse actions within the Map view (moving,
resizing, etc.) will affect all selected Zones — see the next paragraph for more details on the
available selection and edit commands in the Map.
You can also add a Sample by dragging it directly onto the Sample Map. See section
Adding Samples to the Sample Map for more information.
(2) Virtual keyboard
Below the Mapping view, the virtual keyboard represents the entire key scale. The root note of the
selected Zone is indicated by the colored key. You can drag this key with the mouse to modify the
root key.
(3) Horizontal zooming scroll bar
Click the main part of the scroll bar and drag your mouse horizontally to scroll through the Sample
Map on the horizontal axis (pitch), or drag it vertically to zoom in/out on this pitch axis. You can
also click the left or right handle of the scroll bar and drag it horizontally to zoom in/out while
keeping the opposite border of the display at a fix position in the Sample Map. Double-click the
main part of the bar to reset the zoom and display the entire pitch range.
(4) Vertical zooming scroll bar
Click the main part of the scroll bar and drag your mouse vertically to scroll through the Sample
Map on the vertical axis (velocity), or drag it horizontally to zoom in/out on this velocity axis. You
can also click the top or bottom handle of the scroll bar and drag it vertically to zoom in/out while
keeping the opposite border of the display at a fix position in the Sample Map. Double-click the
main part of the bar to reset the zoom and display the entire velocity range.
Available actions in the Map
You can select and edit Zones with your mouse and your keyboard in the Map. Following actions
are available:
Mouse/keyboard action
Command
Selection commands
Click a Zone
Puts this Zone under focus. The focused Zone is highlighted.
You can edit the focused Zone and the playback settings of
its Sample via the Zone settings at the bottom of the Zone
page, as well as process the Sample’s audio material on the
Edit page and/or slice the Sample on the Slice page.
Hold [Ctrl] ([Cmd] on macOS)
and click several Zones
Selects all clicked Zones. Click a selected Zone to deselect it
(i.e. remove it from the selection).
SAMPLING AND SAMPLE MAPPING 463

<!-- page 467 -->

Mouse/keyboard action
Command
Hold [Shift] and click two
Zones
Selects both Zones and all Zones in-between.
Click and drag a selection
frame in the Sample Map
Selects all Zones within or overlapping the frame.
Press [Ctrl]+[A] ([Cmd]+[A] on
macOS)
Selects/deselects all Zones. When deselecting, only the
focused Zone remains selected.
Edit commands
Drag the left/right border of a
Zone
Adjusts the key range for the selected Zones.
Drag the higher/lower border
of a Zone
Adjusts the velocity range for the selected Zones.
Drag a corner of a Zone
Simultaneously adjusts the lowest/highest note and the
lowest/highest velocity of the selected Zone(s) — depending
on the corner.
Click inside a Zone and drag
Moves the selected Zone(s) across the Sample Map. Note
that the Root Key of each Zone is moved accordingly.
Double-click a Zone
Extends the key and velocity ranges of the Zone so that it
fits the key and velocity limits of the neighbor Zones. This
can be very useful to quickly fill up any key or velocity gap
between Zones.
Right-click ([Cmd]-click on
macOS) a Zone
Opens the Sample Map menu (see below).
Press [Del] or [Backspace]
Removes the selected Zone(s) from the Sample Map.
You can also adjust the key and velocity ranges in the Zone settings at the bottom of
the Zone page. See Adjusting the Zone settings for a detailed description.
For more information on the Edit and Slice pages, please refer to section Editing a
Sample and Slicing a Sample, respectively.
Sample Map menu
The Sample Map menu contains additional editing facilities.
▶Right-click ([Ctrl]-click on macOS) a Zone to open the Sample Map menu.
The commands in the Sample Map menu will affect all selected Zones. The menu provides
following commands:
Command
Description
Delete
Removes the selected Zone(s) from the Sample Map.
SAMPLING AND SAMPLE MAPPING 464

<!-- page 468 -->

Command
Description
Map as Drum
Kit
Reduces the selected Zones to one note over the full velocity range and
puts the Zones next to each other upwards from the middle C (C3). The
actual note assigned to each Zone depends on the Zone position in the
Zone List: The topmost Zone will be mapped to middle C (C3), the Zone
underneath to C#3, etc.
Editing Zones in the Sample view
The Sample view is visible when the Sample View button (showing a little waveform icon at the
right of the Zone tab) is activated.
Enable the Sample View button to see the Sample view.
The Sample view contains the following elements:
The Sample view of the Zone page.
(1) Waveform display
Shows the waveform of the Sample for the focused Zone. The waveform display provides
following tools:
•
Use the scroll wheel of your mouse to zoom in/out. You can also use the zooming scroll bar (3).
•
Play range markers (4) and loop markers (5): See below.
•
Playhead indicator: When the Sample is played back (e.g., by pressing the pad or by clicking the
little play icon in the information bar above the waveform), a playhead indicator (white vertical
line) shows you the current play position within the waveform.
•
Context menu: Right-click (macOS: [Ctrl]-click) anywhere in the waveform to open a context
menu with the following commands:
SAMPLING AND SAMPLE MAPPING 465

<!-- page 469 -->

Command
Description
Open containing
folder
Opens the folder on your hard disk containing the Sample, providing
quick access to the original file.
Save Sample As…
Opens a Save Sample As dialog allowing to save the Sample of the
focused Zone under another name and/or to another location on your
computer.
(2) Timeline
Shows the time scale in seconds.
(3) Zooming scroll bar
Click the main part of the scroll bar and drag your mouse horizontally to scroll through the
waveform on the horizontal axis (time), or drag it vertically to zoom in/out on this time axis. You
can also click the left or right handle of the scroll bar and drag it horizontally to zoom in/out while
keeping the opposite border of the display at a fix position in the waveform. Double-click the main
part of the bar to reset the zoom and display the entire waveform. Alternatively you can use the
scroll wheel of your mouse when hovering the waveform display (1) to zoom in/out.
(4) Play range markers
The S and E markers indicate the start and end points of the play range, respectively. Drag them
with the mouse to modify the portion of the Sample that will be played back. This can also be done
in the PLAY RANGE section of the Zone settings, under the waveform display (refer to Adjusting
the Zone settings).
(5) Loop markers
If a loop has been defined in the Sample, it is also indicated on the waveform. You can then adjust
the loop by dragging its borders, and move the entire loop by dragging its title bar. Loops can
be created and adjusted in the LOOP section of the Zone settings, under the waveform display
(refer to Adjusting the Zone settings). Note that the loop will always stay within the play range.
Therefore, when moving the Sample’s start and end points closer to each other (see above), keep in
mind that it might also shrink the loop!
Adjusting the Zone settings
At the bottom of the Zone page, the Zone settings allow you to adjust how each Zone should be
played back.
The Zone settings in the software.
The various sections always display the values for the focused Zone.
If the Maschine window is not wide enough to display all Zone settings at once, a
horizontal bar appears underneath to scroll to the desired section of parameters.
Following parameters are available:
(1) PLAY RANGE section
The parameters in the PLAY RANGE section allow you to adjust the portion of Sample that will be
played back when the Zone is triggered.
SAMPLING AND SAMPLE MAPPING 466

<!-- page 470 -->

Parameter
Description
START
Adjusts the playback’s start point in the Sample of the focused Zone.
END
Adjusts the playback’s end point in the Sample of the focused Zone.
(2) LOOP section
The parameters in the LOOP section allow you to define and adjust a portion that will play in loop
while the note is held.
Parameter
Description
ACTIVE
Enable this to define a loop in the Sample of the focused Zone. When the
play position reaches the loop, the playback is looped as long as the note
is held. This can be useful to loop either a whole Sample or part of it, e.g.,
to simulate a longer tone. Note: this technique requires that you set the
Sampler’s Type selector to AHD or ADSR on the Pitch / Envelope page
(refer to Page 2: Pitch / Envelope).
START
Adjusts the loop’s start point.
END
Adjusts the loop’s end point.
XFADE
(Crossfade)
Allows you to blend a little of the material near the loop start and end points
in order to get a smoother, less abrupt loop. This is particularly helpful if the
loop is inducing any clicks.
Alternatively you can also adjust the loop’ start and end points by dragging the borders of the loop
in the Sample view, and move the entire loop by dragging its title bar.
By moving the loop’s start and end points closer to each other you can shrink the loop
to very small values on-the-fly, thereby creating very interesting glitch effects in a live
situation.
The loop will always stay within the play range of the Sample. Therefore, when moving
the Sample’s playback start and end points closer to each other, keep in mind that it
might also shrink the loop!
(3) TUNE / MIX section
The TUNE / MIX section contains parameters controlling pitch- and level-related aspects of the
Sample playback.
Parameter
Description
TUNE
Sets the tuning of the focused Zone.
GAIN
Sets the gain of the focused Zone.
PAN
Sets the panorama position of the focused Zone.
ROOT KEY
Adjusts the root key of the focused Zone, that is the key at which the Sample will
be played back at its original pitch. The root key is also indicated by the colored
key on the virtual keyboard; to change it, you can drag it to another note on the
keyboard.
(4) ENVELOPE section
SAMPLING AND SAMPLE MAPPING 467

<!-- page 471 -->

This amplitude envelope can be used to get rid of clicks after slicing; you can either apply it to the
Zone of the whole Sample or to individual Zones for selected Slices.
Parameter
Description
ATTACK
Adjusts how quickly the Sample/Slice reaches full volume after being triggered.
DECAY
Adjusts how fast the Sample/Slice dies down.
(5) MAP section
The MAP section contains the parameters defining the key and velocity ranges of the Zone.
Parameter
Description
KEY LO (Lowest Key)
Sets the lowest note (key) of the focused Zone. Alternatively, you
can drag the left border of the Zone in the Map.
KEY HI (Highest Key)
Set the highest note (key) of the focused Zone. Alternatively, you
can drag the right border of the Zone in the Map.
VEL LO (Lowest
Velocity)
Defines the lowest velocity of the focused Zone. Alternatively, you
can drag the lower border of the Zone in the Map.
VEL HI (Highest
Velocity)
Defines the highest velocity of the focused Zone. Alternatively, you
can drag the higher border of the Zone in the Map.
Adding Samples to the Sample Map
You can add Samples directly to the Map view of the Zone page.
To see the Map view, make sure that the Sample View button is deactivated next to
the Zone tab at the top of the Sample Editor. If this is not the case, click it to disable it.
▶To add a new Sample, select one from the Browser or from your operating system and drag it
onto the Sample Map of the Map view (the biggest part in the middle of the Zone page). Once
your mouse is hovering the Sample Map, and before you release the mouse button:
•
Drag your mouse horizontally to choose the root key of the new Zone.
•
Drag your mouse vertically to adjust the key range: With your mouse in the lower half of the
Sample Map the Zone will cover the root key only; dragging your mouse up in the upper half of
the Sample Map will extend the Zone’s key range up to one octave above the root key; with your
mouse at the top of the Sample Map, the Zone will cover the entire keyboard.
•
As you release the mouse button, the Zone is created.
You can add other Samples to the Sound via this method.
The key range of several Zones can overlap, as can the velocity range.
Adding multiple Samples at once
You can also drag several Samples to the Sample Map at once:
1. Hold [Ctrl] ([Cmd] on macOS) or [Shift] on your computer keyboard and click the desired
Samples in the Browser or in your operating system.
SAMPLING AND SAMPLE MAPPING 468

<!-- page 472 -->

2. Drag the selected Samples to the Sample Map.
→This will create multiple adjacent Zones. The width (i.e. key range) of these Zones will again
depend on where they are dropped in the Sample Map: The higher you drop, the wider each
Zone will be. Dragging to the top part layers all Zones across the entire keyboard.
The placement of the Zones depends on the original Samples’ position in the selection list: The first
Sample selected will get the Zone with the lowest key range, the second Sample selected will get
the Zone just over the previous one, etc.
SAMPLING AND SAMPLE MAPPING 469