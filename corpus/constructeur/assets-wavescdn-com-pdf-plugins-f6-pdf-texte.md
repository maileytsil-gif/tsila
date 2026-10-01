---
titre: "Waves F6 Floating-Band Dynamic EQ User Guide (texte du PDF, 16 pages)"
source: constructeur/assets-wavescdn-com-pdf-plugins-f6-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

Floating-Band Dynamic EQ
User Guide
Waves F6

<!-- page 2 -->

F6 Floating-Band Dynamic Equalizer / User Guide

2
Contents
Introduction ............................................................................................................3
About the F6 Floating-Band Dynamic Equalizer ...................................................3
Waves F6 Real Time Equalizer (RTA) ..................................................................4
Why Use a Dynamic EQ? .....................................................................................4
Components ..........................................................................................................6
F6 Interface ...........................................................................................................6
Graph ................................................................................................................................. 7
Band Selectors Row .......................................................................................................... 8
Band Controls .................................................................................................................... 9
Output Section ................................................................................................................. 12
F6 in Use ............................................................................................................ 13
F6 Real Time Analyzer ....................................................................................... 14
WaveSystem Toolbar ......................................................................................... 16

<!-- page 3 -->

F6 Floating-Band Dynamic Equalizer / User Guide

3
Introduction
Thank you for choosing Waves! In order to get the most out of your new Waves plugin, please take a moment to read
this user guide.
To install software and manage your licenses, you need to have a free Waves account. Sign up at www.waves.com.
With a Waves account you can keep track of your products, renew your Waves Update Plan, participate in bonus
programs, and keep up to date with important information.
We suggest that you become familiar with the Waves Support pages: www.waves.com/support. There are technical
articles about installation, troubleshooting, specifications, and more. Plus, you’ll find company contact information and
Waves Support news.
About the F6 Floating-Band Dynamic Equalizer
F6 is a dynamic equalizer that features six floating, fully-adjustable parametric filters with dynamics, as well as HP and
LP filters. It provides multiband compression, equalization, expansion, and de-essing in one interface.
Plugin highlights include:
•
M/S band mode for mid/side processing
•
Compression and expansion
•
Split/Wide side chain modes for processing flexibility
•
Internal and external side chain
•
Low CPU consumption
•
Zero latency
•
Parallel processing
•
Side chain solo
•
Smooth: no artifacts when adjusting parameters
•
Simple interface: well suited for touch displays

<!-- page 4 -->

F6 Floating-Band Dynamic Equalizer / User Guide

4
Waves F6 Real Time Equalizer (RTA)
To increase F6’s precision and ease of use, we added a simple-to-use, feature-rich Real Time Analyzer (RTA) that
creates a real-time visual map of your audio. This provides a fast and accurate way to interpret the signal and set F6
parameters. It also gives you immediate feedback about how your settings are affecting the sound. RTA is highly
adjustable and all of its controls are visible at all times on a toolbar; you can easily change how the sound is being
interpreted, in real time.

Why Use a Dynamic EQ?
EQs have been used for about a hundred years to change the color of a signal. They increase or decrease the gain at selected
frequencies. They can affect a wide range of frequencies or very specific ones, and they usually offer a choice of curves. EQs can
precisely boost or cut a sound, or smoothly color a track. While they work, the difficulty is that once you set the gain, Q, and
frequency, an EQ is “deaf” to what’s going on in the music and it affects everything at the selected frequency. So a high-frequency
notch intended to tame a screechy violin string will simultaneously remove the detail and overtones of the instrument when lower
notes are played.
Multiband compressors, such as Waves C4, address this problem by dividing the frequency spectrum into segments that are
defined by crossover points. Dynamic processing takes place between these crossovers and each includes the traditional dynamics
controls: threshold, gain, range, attack, and release. It’s like having a number of dynamics processors working on one signal at
designated frequencies. Because multiband processors are based on crossovers, rather than specific frequency bands, they are
smooth across all of the signal’s frequencies. Hence, they are useful in shaping a mix and coloring an instrument. But this
smoothness may not be what you want when carving an instrument out from a busy mix, or pushing it back so it blends better.
This is where a dynamic EQ, such as the Waves F6, comes in. Like a multiband EQ—say the classic Q10—it has free-floating
bands that can be set to any frequency, EQ type, gain, and Q. A dynamic EQ can do all of this, but it can also be set to act only
when the signal moves beyond a defined threshold at the chosen frequency. Specific instruments, or specific sounds of an
instrument, can be isolated and manipulated. Guitar plucks can be controlled with respect to the tonal sounds without dulling the
strings. A dark kick can be enhanced without affecting the rest of the mix. An inarticulate instrument can be made solid, without
making the mix brittle. Each band offers all of the standard controls of a dynamics processor.

<!-- page 5 -->

F6 Floating-Band Dynamic Equalizer / User Guide

5
Each band of the F6 can process a signal in left/right stereo or in M/S (mid/side). This lets you control EQ for the center of a mix—
the singer, for example—without affecting the color or shape of the overall stereo image. For further control, a side chain signal is
sent to each band, so you can choose if that band’s frequency and its dynamics processing are triggered internally or externally.
Dynamic EQs are precision tools that let you control specific instruments or an entire mix in a very precise manner; reach for them
when your static EQ is effective but is causing damage to the overall color of the sound. Use a dynamic EQ when compressors,
limiters, or de-essers step on too much of the sound. Use the F6 when you need to selectively control an instrument’s sound or its
place in the space of the mix.

<!-- page 6 -->

F6 Floating-Band Dynamic Equalizer / User Guide

6
Components
There are four F6 components:
(1) Mono
(2) Mono RTA (includes real-time analyzer)
(3) Stereo
(4) Stereo RTA (includes real-time analyzer)

Mono and stereo interfaces are identical, except that the mono component does not include the Band Mode switch.


F6 Interface

<!-- page 7 -->

F6 Floating-Band Dynamic Equalizer / User Guide

7
Graph










The Graph displays filters (Band Markers) and shows the effects of dynamic processing. Frequency is shown on the
horizontal scale and amplitude on the vertical scale. The Total Curve Line provides a summary of the filters and
dynamics for all bands.
Each band is represented by a Band Marker with its own number and color. Click on a band to select it. Selecting a Band
Marker will display all available band controls in the Band Controls section. You can also select a band by choosing a
filter in the Band Selectors row. Double-click on a marker to turn its band on or off. You can drag Band Markers 1–6 to
any place on the graph, whereas HP and LF filters can move only on the frequency (horizontal) scale. Many Band
Marker functions can be controlled with modifier keys.
Key/Movement Combination
Action
Command + Click on Band Marker
Switches filter types
Hold Alt+move marker horizontally
Changes Q width
Hold Ctrl+move marker horizontally
Movement on horizontal axis only, vertical axis is locked.
Hold Ctrl+move marker vertically
Movement on vertical axis only, horizontal axis is locked.

<!-- page 8 -->

F6 Floating-Band Dynamic Equalizer / User Guide

8
In the stereo component, a filter can be applied to the stereo or mid or side channels using the Band Mode switch. This
assignment is indicated on the Band Marker with a small letter: M (mid), S (side) or no letter (Stereo). Band Type is
selected in the Band Controls row.

Band Selectors Row



When you choose a band in the Band Selector row, all available band controls will appear. These controls enable you to
adjust processing parameters without touching the Graph, so it’s useful for precise, delicate control. Double-click on a
band selector to turn the band on and off. Only one band is selected at a time.

<!-- page 9 -->

F6 Floating-Band Dynamic Equalizer / User Guide

9
Band Controls
Bands 1-6
These controls are available for the selected band. The value of a continuous control is indicated on its knob.



Control
Range
Action
Band On/Off
On or Off
Turns off processing for selected band
Band Mode
(Stereo component only)
ST, M, S
Sets what the filter affects: stereo, mid, or side channel
Band Type
Low shelf, Bell, or High shelf.
Sets EQ type
Frequency
16 Hz to 21,000 Hz
Sets band frequency
Q
0.4 to 60
Sets band width
Gain
-18 dB to +18 dB
Sets band gain
Range
-18 dB to +18 dB
Dial negative range for compression and positive range for
expansion
Threshold
-60 dB to 0 dB
Center knob sets the level at which dynamic processing
begins.
SC Input Meter
(surrounds Threshold
knob)
-60 dB to 0 dB
Displays the band’s SC input. Since the input to a band is
always internal or external SC, this meter effectively indicates
the band’s input.
Attack
0.5 ms to 500 ms
Sets attack for dynamic process of selected band

<!-- page 10 -->

F6 Floating-Band Dynamic Equalizer / User Guide

10
Control
Range
Action
Release
5 ms to 5000 ms
Sets the release time for dynamic processing of the selected
band. Actual release time depends on the amount of gain
reduction/expansion applied. A greater gain reduction/
expansion setting will result in a longer actual release time
than set here.
Side Chain Solo*
On or Off
Auditions the band’s SC source
Side Chain Source
Internal or External
SC source select
Side Chain Mode
Split or Wide
In Split Mode, filtered audio will affect dynamics of the
selected band. In Wide Mode, Full Range audio will affect
dynamics of the selected band.

*Side Chain Solo can be activated by clicking on the Solo toggle in the Band Controls row. The solo toggles off when you
select another band. Solo can also be activated by right-clicking and holding a band marker. Move the marker while
holding right-click and you can solo other frequencies.

What you hear when soloing a band depends on Band SC Source and SC Mode.

<!-- page 11 -->

F6 Floating-Band Dynamic Equalizer / User Guide

11
HPF/LPF
High pass and Low pass filters can be applied to a signal.

Control
Range
Action
Band On/Off

On or Off
Turns off HP and LP filters for the band
Band Mode
(Stereo
Component only)
Stereo, Mid, or Side
Select what the filter is applied to
Frequency
16 Hz to 21,000 Hz

HP/LP filter frequency settings
Q
6 dB, 12 dB, 18 dB, 24
dB per octave
Sets steepness of filter
Solo
On or Off
Solos the selected filter

<!-- page 12 -->

F6 Floating-Band Dynamic Equalizer / User Guide

12
Global Controls



Control
Range
Action
Global Release
Automatic Release Control (ARC)
or Manual
Sets the type of release for dynamics processing.
When Global Release is set to ARC, the ARC engine will
calculate the shortest possible release time based on the
signal’s envelope. This value will always be shorter than the
Release setting for the band.
Global Arrows
Up/Down arrows
Range depends on the control
Use these arrows to link certain controls on all bands,
regardless of which band is selected. Move the arrows up and
down to adjust the control above it.
Controls that can be linked: Gain, Range, Threshold, Attack,
and Release

Output Section



Control
Range
Action
Mix
0: unprocessed sound
100: fully processed sound
Controls the mix between processed and
unprocessed audio (also called parallel
processing)
Out
-18 to +18
Controls plugin’s output gain
Output Meter
-40 to 0 dBfs
Displays output level

<!-- page 13 -->

F6 Floating-Band Dynamic Equalizer / User Guide

13
F6 in Use
The F6 Floating-Band Dynamic EQ is very flexible since the frequency, width, sidechain mode, and EQ type of each
band can be set independently of others. This lets you assign separate EQ and dynamic processes to different frequency
bands of a signal. With the M/S mode, you can control dynamic EQ processing in different parts of the sound image. This
opens many opportunities. Here’s one example:

Let’s say that the instruments and the lead vocal are competing with each other for the same space in a mix. This is, of
course, pretty common. You can use F6 to carve out a spot for the lead vocal without affecting the stereo width of your
mix while maximizing the blend (glue) between the instruments and the lead vocal.
Here’s a way to sort it out:
1. Group the instruments to a stereo buss.
2. Insert the F6 stereo component on this buss.
3. Route the lead vocal to the F6 as an external side chain.
4. In this example, we’ll use Band 4 for processing as follows:
a. Switch Band 4 Mode to M (Mid Channel)
b. Switch Band 4 SC Source to EXT
c. Set Band 4 Frequency to 1600 Hz
d. Widen the Q to 0.6
e. Set Range to -2.5 dB
5. Now play your audio (instrument and lead vocal together).
6. The lead vocal’s input level is indicated on the Threshold SC Meter. The positon indicator on the Threshold knob
indicates whether Band 4’s Threshold is above or below the lead vocal’s input level.
7. Slowly lower the Threshold level. When Threshold falls below the level of the lead singer, the band’s compressor
will begin to attenuate the mid channel. The amount of attenuation is indicated by the Total Curve on the Graph.
8. Adjust parameters per your liking.

<!-- page 14 -->

F6 Floating-Band Dynamic Equalizer / User Guide

14
F6 Real Time Analyzer
The F6 Real Time Analyzer is feature-rich tool that provides a visual map of your audio. It offers several methods of
interpreting the contents of your audio signal. This enables a faster and more accurate way to set F6 parameters. It also
provides immediate feedback about how your settings are affecting the sound.
The F6 Real Time Analyzer is based on tried and true FFT (Fast Fourier Transform) technology.









View
Determines how frequency information is displayed. It does not affect the performance of
RTA.

Filled shows the analysis chart as a solid area.

Bar shows the chart as bars. Bars/octave defined with the Banding control.








Response
Sets how RTA reacts to audio: Peak Mode or RMS Mode
Filled View
Bar View

<!-- page 15 -->

F6 Floating-Band Dynamic Equalizer / User Guide

15

Slope
Sets how RTA displays energy:

Pink Slope shows RTA as equal energy per Octave

White Slope shows RTA as equal energy per Frequency

Banding
Sets the display frequency resolution (spectral resolution): shown as bars/octave

1/24, 1/12, 1/6, 1/3, and octave

Averaging
Sets the speed at which RTA reacts to the signal:

Fast, Medium, Slow, and Slowest

MA
(moving average)
Displays a line that represents the average level









MAX
Displays a line that represents the peak curve

<!-- page 16 -->

F6 Floating-Band Dynamic Equalizer / User Guide

16

Source
Toggle through RTA monitoring modes (Stereo Component only):

L only, R only, L+R (mid), and Sides (L-R)

RTA
Four states:

Pre EQ, Post EQ, Side Chain, and Off

RTA On/Off
Turns RTA processing on or off. Hides RTA display.

Coordinates
Mouse/Cursor coordinates are displayed to indicate Frequency/Note with RTA’s dB
value.



WaveSystem Toolbar
Use the bar at the top of the plugin to save and load presets, compare settings, undo and redo steps, and resize the
plugin. To learn more, click the icon at the upper-right corner of the window and open the WaveSystem Guide.