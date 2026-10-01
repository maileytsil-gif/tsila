---
titre: "Renaissance EQ User Guide (texte du PDF, 14 pages)"
source: constructeur/assets-wavescdn-com-pdf-plugins-renaissance-equalizer-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

Renaissance EQ
User Guide

<!-- page 2 -->

Renaissance Equalizer / User Guide
1
Contents
Introduction ...................................................................................................................... 2
Components ........................................................................................................................................................... 3
EQ Bands ................................................................................................................................................................ 3
Interface ................................................................................................................................................................. 4
Renaissance EQ Controls .................................................................................................. 5
Filter Types ............................................................................................................................................................. 8
Output Section ..................................................................................................................................................... 10
Real-time Analyzer ............................................................................................................................................... 11
Cursor Coordinates .............................................................................................................................................. 11
Link ....................................................................................................................................................................... 12
Working with Presets.............................................................................................................................................13

<!-- page 3 -->

Renaissance Equalizer / User Guide
2
Introduction
Renaissance EQ is a six-band paragraphic equalizer for professional audio production. It is famous for its remarkedly
musical equalization and its resonant shelves.
Graphic Controls
Cursor frequency
Graphic curve
Band marker
Analyzer display
Analyzer on/off
Parametric Controls
Parametric view selector (top of graph)
Band on/off switch
Filter type selector
Parametric Gain control
Parametric Frequency control
Parametric Q control
Band select tabs
Channel linking controls
Output gain controls and meters
Trim value indicator

<!-- page 4 -->

Renaissance Equalizer / User Guide
3
Components
There are two Renaissance EQ components:
•
REQ mono (2-band, 4-band, 6-band)
•
REQ stereo (2-band, 4-band, 6-band)
 Aside from the number of channels, the components are identical.
EQ Bands
The filter types used in the Renaissance Equalizer are not identical for each band. They are organized to provide a
musical and common-sense way of interacting with the EQ bands, and to enable scalability between all components.
The outside bands (i.e., the highest and lowest) are common to all components of the REQ. If, for example, you
select the 2-band component from your plugin menu, then these two bands will have the same filter options as
bands 1 and 6 from the 6-band version. This behavior is the same when you move presets between different sized
components on different DAW channels.
Bands 1 and 6 have cut filters, resonant shelves, and bell filters (1 is low cut and shelf, 6 is high cut and shelf).
Bands 2, 3, 4, and 5 all have resonant shelves and bell filters (2 and 3 have low shelves, 4 and 5 have high
shelves).

<!-- page 5 -->

Renaissance Equalizer / User Guide
4
Interface
You can view the Renaissance EQ interface in any of three styles.
Select a style with the Skins drop-down menu, on the left side of the WaveSystem Toolbar at the
top of the interface.
•
All three skins have the same controls. When you change skins, the values don’t change.
•
The skin of the current instance sets the default view, so new instances will open with that skin.
Light View
Dark View
Legacy View

<!-- page 6 -->

Renaissance Equalizer / User Guide
5
Renaissance EQ Controls
Renaissance EQ is a paragraphic equalizer, which means that you can adjust it with its parametric controls or with
the graphic display. Either way, the basics are very simple.
PARAMETRIC CONTROLS
•
Band Select: click on a band number tab beneath the parametric controls.
•
Band On or Off: click on the band number button.
•
Filter Type: click on the filter to toggle through types or use the drop-down menu.
•
Q, Frequency, and Gain: click on the control and move the mouse.
GRAPH CONTROLS
•
Band Select: click once on a band marker to select its band.
•
Band On or Off: double-click a band marker.
•
Filter Type: Cmd+click (Mac) on a band marker to toggle through the filter types.
•
Q: Hold Alt while dragging left or right.
•
Frequency: drag a marker left or right.
•
Gain: drag a marker up or down.
To restrict marker movement to one axis (i.e., only up or down, or only left or right), hold Ctrl and then drag
vertically or horizontally. This enables you, for example, to accurately locate a frequency using a very high,
narrow boost, and then turn the boost into a cut without changing the frequency setting.
Set precise values for Q, Freq, and Gain by double-clicking on the control knob, entering a value, and clicking Enter.
You can also select a control knob or a band marker and use the keyboard arrows to increase or decrease a value.

<!-- page 7 -->

Renaissance Equalizer / User Guide
6
SELECTING A BAND
T



Values for the selected band are shown above the parametric controls.
The band that is currently being controlled is the selected band. There are two ways to select
a band:
•
Click on a band marker in the graph (the selected marker is surrounded by a yellow
box).
•
Click on a band tab in the parametric section at the bottom.
The Band On/Off switch indicates the selected band. It is color-coded to match the band
marker.

<!-- page 8 -->

Renaissance Equalizer / User Guide
7
GAIN
Gain can be adjusted in increments of 0.1 dB by using the Gain Value windows
or by dragging the EQ curve up or down. To enter numerical values, double-click
on the parametric control knob.
Range: -18.0 dB to +18.0 dB
FREQ
The Frequency control displays the center frequency for each band when a bell
filter is selected. When in cut or shelf modes, the Freq parameter controls the
corner frequency of the filter.
Frequency control values are adjustable in one-sixteenth tone steps (96 steps
per octave), rounded to the closest integer. The left/right arrow keys may be
used to step the selected Freq value in one-sixteenth tone increments.
Range: 16 Hz to 21,357 Hz
Q
The Q control functions differently for each filter type.
•
Bell
Q corresponds to the width of the frequency range for that band.
•
Shelf Q controls the slope of the “side” of the shelf and the resonant dips and peaks.
•
Cut
(“outside” bands only) Q controls the slope of the cut filter from about 10 dB/oct to 18 dB/oct.
Additionally, it controls the “bump” in the slope.
When Q is set to a higher value (bigger number) the slopes of all filters are generally steeper, bells are narrower,
and cut and shelf filters are more sharply sloped.
Range: Shelf: 0.71–1.41; Pass: 0.71–1.41; Bell: 0.26–6.5

<!-- page 9 -->

Renaissance Equalizer / User Guide
8
Filter Types
CUT/PASS FILTERS
A high-pass filter cuts all the frequencies below the cutoff point. A low-pass filter does just
the opposite; it cuts all frequencies above the cutoff frequency. The slope of the graph line
changes as Q is adjusted. In REQ 6, bands 1 and 6 are third-order filters (equal to 18
dB/octave). When the Q=1.0, the filters are 18 dB/octave.
Range
Frequency: 16 Hz to 21357 Hz
Q: 0.71 to 1.41 dB/octave
SHELF FILERS
A Shelf filter boosts or cuts above or below a specified frequency. Rather than rolling off to
infinity—as with pass filters—the shelf will roll off, or up to, the designated gain indicated in
the shelf and not go beyond this gain. The shelf filter’s cutoff frequency is located in the
middle of the slope. So, if the specified frequency is 1000 Hz and the gain is set to +6 dB,
then the gain at 1000 Hz will be at about +3 dB.
Range
Gain: -18 dB to +18 dB
Frequency: 16 Hz to 21357 Hz
Q: 0.71 to 1.41 dB/octave

<!-- page 10 -->

Renaissance Equalizer / User Guide
9
RESONANT SHELF FILTERS
A resonant shelf uses a cut and boost simultaneously to increase resonance at the cutoff point.
This behavior is found on certain sought-after analog filters (most notably, Pultec). There are
two distinguishing features that resonant shelves:
•
visibly obvious curves of the shelf
•
adjustable Q of the shelf, which shifts the steepness of the slope
Changing Q adjusts the angle of the slope going to the shelf. This yields the characteristic
“bump” in the graph. The overshoot/undershoot on the angle of the slope is quite important to
the sound of these shelves.
BELL FILTERS (PARAMETRIC)
Bell filters are used to boost or cut at specified frequencies, and the Q value sets the bandwidth.
Range
Gain: -18 dB to +18 dB
Frequency: 16 Hz to 21357 Hz
Q: 0.26 to 6.50
Traditional bell filters have symmetrical response characteristics: effective gain is the same when
boosting or cutting a band. But this behavior doesn’t really reflect the way that people use filters.
When we use an equalizer to boost (left), it’s nearly always for tonal correction—making it “sound
better.” When cutting a frequency (right), it’s usually for removing noises or bothersome artifacts.
Therefore, with the same Q setting, an REQ bell filter is wider when gain is positive than when
gain is negative.

<!-- page 11 -->

Renaissance Equalizer / User Guide
10
Output Section
Internal processing is carried out at 48 bits. This provides enough headroom to completely avoid internal clipping in
each band. This same headroom enables the Renaissance EQ to calculate exactly how far “over” a signal goes
beyond 0 dBFS, and lets you correct this precisely.
OUTPUT FADER AND METER
Output mono or stereo meters are logarithmic displays from -60 dBFS to 0 dBFS, with peak hold values shown at the
bottom of each meter. Click on the Peak Hold values (or in the meters themselves) to reset them.
The left and right output meters sit on top of the output meters. The fader value is shown at the top of the meter. Fader
range: -infinity to +12 dB
TRIM
A Trim indicator is shown below the meter. A positive value indicates that headroom is still available and that the output
level can be increased by the indicated amount. A negative value indicates the output is clipping and the output should
be lowered by the specified amount.
•
Click the Trim button once to automatically move the faders by the value shown in the button. Trim will reset
to “12.0,” the maximum positive gain allowed.
•
Click anywhere in the meters or between them to reset the Trim (and the meters) without changing the value
of the faders.
A light above the faders indicates clipping. Reset by clicking on the light.

<!-- page 12 -->

Renaissance Equalizer / User Guide
11
Real-time Analyzer
Renaissance EQ includes a real time equalizer (RTA). It’s used to
identify signal behavior at specific frequencies. The RTA displays
live updates of gain and frequency, which you can use to better
understand what’s happening on the track. The RTA is post-EQ,
so you will see how your EQ choices affect the signal. The
analyzer is calibrated to a pink curve.
Turn the RTA display on or off with the button on the top right. To save host computer DSP, turn off the RTA when
you don’t need it.
Cursor Coordinates
When you hover over the graph, the frequency of the cursor position is displayed. This can help you locate specific
frequencies based on the RTA display.

<!-- page 13 -->

Renaissance Equalizer / User Guide
12
Link
When you’re using the stereo or dual-mono components, you can control the left and right channels
together or independently with the Linking selector. Linking applies to Gain, Frequency, Q, Filter Type,
and In/Out. When Link is On (center button), adjusting any parameter control will equally affect both left
and right channels.
In the image on the left, the Left and Link buttons are selected. When you adjust a control, you are moving the left
channel controls, but adjusting both channels. The opposite is true when Right and Link are selected.
To control left and right EQ separately, deselect the Link button (right image). Activate either the Left or Right button
to adjust only the selected channel.
You can unlink the channels, set them to different gains (even different filter types and Q values), then re-link them.
When you move one channel, the other will track the changes. Any offsets between the channels will be maintained.
If you type in a new gain value, that gain value will be applied to both channels, eliminating any gain offset.
If you drag the band marker or gain value, the gain offset between the bands will be maintained.

<!-- page 14 -->

Renaissance Equalizer / User Guide
13
Linking with Automation
When using automation in your DAW, the Link button is not automated, and its status is not saved as part of a
session. This allows you to load a setup into only one or the other channel for dual-mono use. There is a downside
to this functionality: true dual-mono automation is not possible within an unlinked stereo REQ. The automation
system of most DAWs can control only one channel, so any settings you try to save or automate on the other
channel will not be written into the automation.
If you have complex EQ that requires total-reset automation on each channel (whether dual-mono or L/R mastering),
you should use two completely separate mono REQ processors and automate them independently.
Working with Presets
Renaissance EQ offers a large collection of presets. These are useful starting points for solving problems and
creating effects: load the most relevant preset and go from there. In some cases, a factory preset will give you just
the settings you need.
There are also Artist presets. These were designed by recording, mixing, FOH, and broadcast engineers, so they
capture a personal point of view about sound. They provide a head start with an attitude when you’re creating a
specific sound or making a track sound better.
Use the bar at the top of the plugin to save and load presets, compare settings, undo and redo steps, and resize the
plugin. To learn more, click the icon at the upper-right corner of the window and open the WaveSystem Guide.