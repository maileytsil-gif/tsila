---
titre: "API-2500 User Manual (texte du PDF, 17 pages)"
source: constructeur/assets-wavescdn-com-pdf-plugins-api-2500-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

Waves API 2500

User Manual

<!-- page 2 -->

Waves API 2500 User Manual
- 2 -


TABLE OF CONTENTS
CHAPTER 1 – INTRODUCTION .............................................................................................................................. 3
1.1 WELCOME ............................................................................................................................................................................................... 3
1.2 PRODUCT OVERVIEW ........................................................................................................................................................................... 4
1.3 CONCEPTS AND TERMINOLOGY ......................................................................................................................................................... 5
1.4 COMPONENTS ........................................................................................................................................................................................ 8
CHAPTER 2 – QUICKSTART GUIDE ...................................................................................................................... 9
CHAPTER 3 – CONTROLS AND INTERFACE ..................................................................................................... 10
3.1 COMPRESSOR SECTION .................................................................................................................................................................... 10
3.2 TONE SECTION ..................................................................................................................................................................................... 12
3.3 LINK SECTION ....................................................................................................................................................................................... 13
3.4 METER DISPLAY ................................................................................................................................................................................... 14
3.5 OUTPUT SECTION ................................................................................................................................................................................ 15
3.6 WAVESYSTEM TOOLBAR .............................................................................................................................................. 16
APPENDIX A – API 2500 CONTROLS ................................................................................................................... 17

<!-- page 3 -->

Waves API 2500 User Manual
- 3 -

Chapter 1 – Introduction

1.1 Welcome

Thank you for choosing Waves! In order to get the most out of your new Waves plugin, please take a
moment to read this user guide.

To install software and manage your licenses, you need to have a free Waves account. Sign up at
www.waves.com. With a Waves account you can keep track of your products, renew your Waves
Update Plan, participate in bonus programs, and keep up to date with important information.

We suggest that you become familiar with the Waves Support pages: www.waves.com/support. There
are technical articles about installation, troubleshooting, specifications, and more. Plus, you’ll find
company contact information and Waves Support news.

<!-- page 4 -->

Waves API 2500 User Manual
- 4 -

1.2 Product Overview


The API 2500 is a versatile dynamics processor that lets you shape the punch and tone of mixes with
absolute accuracy. Its dual channel design lets the 2500 also function as two separate mono channels
via a single compression setting. Using auto-makeup gain, you can adjust Threshold or Ratio while
automatically maintaining a constant output level. With both Feed Back and Feed Forward compression
types, the API 2500 boasts a wide range of incredibly musical parameters which have made it a favorite
of engineers the world over.

<!-- page 5 -->

Waves API 2500 User Manual
- 5 -

1.3 Concepts and Terminology
There are 3 main parameters that set the API 2500 from other compressors: Thrust, Compression
Type, and its adjustable Knee. When used in conjunction with one another, these parameters give the
API 2500 unprecedented flexibility.

Knee
Sets the knee, the manner in which the compressor begins to reduce the gain of the signal.


•
In the Hard position, gain reduction begins immediately at the set ratio.

•
In the Med position, there is a slight fade-in to the set ratio.

•
In the Soft position, there is an even more gradual fade-in to the set ratio.

<!-- page 6 -->

Waves API 2500 User Manual
- 6 -


Thrust
Sets the Thrust, a proprietary process that inserts a High Pass Filter at the RMS detector input, limiting
compression response to lower frequencies while applying additional compression to higher
frequencies.


•
In Norm mode, there is no filter and the 2500 functions like a normal compressor.

•
In Med mode, there is a slight attenuation of the low frequencies and a slight boost of the high
frequencies, with a flat mid range affecting the signal into the RMS detector. This reduces
pumping caused by low frequencies and increases the RMS detectors’ sensitivity to higher
frequencies, affecting higher frequency signal peaks.

•
In Loud mode, a gradual linear filter attenuates level by 15dB at 20hz and increases level by
15dB at 20khz. This decreases low frequency pumping while increasing higher frequency
compression.

<!-- page 7 -->

Waves API 2500 User Manual
- 7 -



Type
Sets the Compression type, which determines the signal source being fed to the RMS detector.

•
In New (Feed Forward) mode, the compressor works like newer VCA-based compressors. The
RMS detector sends a signal to the VCA that is an exact ratio of the desired compression, set
by the ratio control.

•
In Old (Feed Back) mode, the RMS detector receives a signal from the VCA output, and then
feeds the VCA a signal based on the set signal ratio.

<!-- page 8 -->

Waves API 2500 User Manual
- 8 -



1.4 Components

WaveShell technology enables us to split Waves processors into smaller plug-ins, which we call
components. Having a choice of components for a particular processor gives you the flexibility to
choose a configuration suitable for your material.

The API 2500 has two component processors:

API 2500 Stereo – A stereo compressor that may also be used as two parallel mono processors.

API 2500 Mono – A mono compressor with an external sidechain option.

<!-- page 9 -->

Waves API 2500 User Manual
- 9 -

Chapter 2 – Quick Start Guide
For those of you who are experienced users of audio signal processing tools, we recommend that you
approach the API 2500 as you would any compressor which you are already familiar. Keep in mind that
its Thrust, Compression Type, and Knee parameters offer capabilities that transcend other, more
conventional, processors.

Newer users should explore the API 2500’s preset library and use its presets as starting points for their
own experimentation. These presets also serve as a valuable introduction to compression techniques in
general, and offer a glimpse into the workflow of professional audio engineers.

We encourage all users to experiment with the API 2500’s settings in order to better understand its
unique processing power.

<!-- page 10 -->

Waves API 2500 User Manual
- 10 -
Chapter 3 – Controls and Interface
3.1 Compressor Section
Tone Section
Link Section
Output Section
Compressor
Section
WaveSystem
Toolbar
Meter Section
Clip LED

<!-- page 11 -->

Waves API 2500 User Manual
- 11 -

Threshold
Sets the point at which compression begins. Threshold for each stereo channel is set independently,
since each channel has its own RMS detector, even in Link mode. In Auto Gain Make-up mode, the
Threshold also affects the gain. Threshold is a continuous control.


Range
+10dBu to -20dBu
(-12dBFS to -42dBFS)
Default
+10dBu


Attack
Sets the attack time of each channel.

Range
.03ms, .1ms, .3ms, 1ms, 3ms, 10ms, 30ms
Default
1ms


Ratio
Sets the compression ratio of each channel. In Auto Gain Make-up mode, Ratio also affects the gain.
Range
1.5:1, 2:1, 3:1, 4:1, 6:1, 10:1, inf:1
Default
4:1


Release
Sets the Release time of the compressor. When set to Variable, Release time is controlled by the
Variable Release control, located to the right of the Release control.

Range
.05sec, .1sec, .2sec, .5sec, 1sec, 2sec, Variable
Default
Variable


Variable Release
Controls the release time with a continuously variable knob. (Please note: Release control must be set
to Variable.)
Range
.05 seconds to 3 seconds in steps of 0.01ms
Default
.5sec

<!-- page 12 -->

Waves API 2500 User Manual
- 12 -
3.2 Tone Section
Knee
Sets the Knee, the manner in which the compressor begins to reduce the signal gain.
Range
Hard, Med, Soft
Default
Hard
Thrust
Sets the Thrust, a proprietary process that inserts a High Pass Filter at the RMS detector input, limiting
compression response to lower frequencies while applying additional compression to higher
frequencies.
Range
Loud, Med, Norm
Default
Norm
Type
Sets the Compression type, which determines the signal source being fed to the RMS detector.
Range
Feed Back, Feed Forward
Default
Feed Forward

<!-- page 13 -->

Waves API 2500 User Manual
- 13 -

A note about Sidechain:
Sidechain lets you trigger the compressor using an external source, which is fed into the RMS detector
and controls the compression of the input signal. Sidechain may only be used in New (Feed Forward)
mode. An external sidechain trigger cannot be used in Old (Feed Back) mode; attempting to do so
automatically switches the compressor to New (Feed Forward) mode.



3.3 Link Section


L/R Link
Sets the percentage of linkage between the left and right channels. While in Link mode, each channel
is still controlled by its own RMS detector, which prevents loading and slaving from either side.

Range
IND, 50%, 60%,70%,80%,90%,100%
Default
100%

Shape
Uses HP and LP filters to adjust the shape of L/R linking. This enables you to remove particularly
high or low frequencies when adjusting the linking. Shape can be used, for example, to prevent
percussive instruments on one channel from coupling and causing unwanted compression on the
other channel. When HP and LP are both selected, a band pass filter is used to determine the
shaping of L/R linking. Click on the Shape button to cycle between the four filter options.

Range
HP, LP, BP (band pass), Off
Default
Off

<!-- page 14 -->

Waves API 2500 User Manual
- 14 -


3.4 Meter Display
Meters
The API 2500’s Meters display dBFS. The Gain scale displays the amount of gain reduction during
compression with the 0 point located at the far the right, which allows higher gain reduction scale
resolution.. The API 2500 is capable of up to 30dB of reduction.

Range
0dB to -24dB (Gain Reduction mode)
-24dB to 0dB (Input and Output modes)


Switchable Display Modes
Range
GR, Out, In
Default
GR


Clip LED
Between the two Meters is a Clip LED which indicates input or output clipping. Since the LED shows
both input and output clipping, you must determine which of the two levels is excessive. The Clip LED
can be reset by clicking on it.

<!-- page 15 -->

Waves API 2500 User Manual
- 15 -



3.5 Output Section



Analog
Turns the Analog modeling on and off.

Range
On/Off
Default
On

Output
Controls the makeup gain.
Range
+/-24dB
Default
0dB

<!-- page 16 -->

Waves API 2500 User Manual
- 16 -
Make-Up
Turns Auto Make-Up Gain on and off.
Range
Auto, Manual
Default
Auto
In
Acts as a master bypass for the entire compression chain. When set to Out, all compressor functions
are bypassed.
Range
In/Out
Default
In
Mix
Controls the balance between the compressed and the uncompressed signal.
Range:
0% to 100% (0.1% increments)
Default:
100%
Trim
Sets the output level of the plugin.
Range: -18 to +18 dB (in 0.1 dB steps)
Initial Value: 0
Reset Value: 0
3.6 WaveSystem Toolbar
Use the bar at the top of the plugin to save and load presets, compare settings, undo and redo steps,
and resize the plugin. To learn more, click the icon at the upper-right corner of the window and open
the WaveSystem Guide.

<!-- page 17 -->

Waves API 2500 User Manual
- 17 -

Appendix A – API 2500 Controls

Control
Range
Default
Threshold
+10dBu to -20dBu
0dBu
Attack
.03ms, .1ms, .3ms, 1ms, 3ms, 10ms, 30ms
1ms
Ratio
1.5:1, 2:1, 3:1 4:1 6:1 10:1 inf:1
4:1
Release
.05sec, .1sec, .2sec, .5sec, 1sec, 2sec, Var
.5sec
Release Variable
.05 to3sec in steps of 0.01ms
.5sec
Knee
Hard, Med, Soft
Hard
Thrust
Loud, Med, Norm
Norm
Type
FeedBack, Feed forwards
Feed Forwards
L/R Link
IND, 50%,60%,70%,80%,90%,100%
100%
Link Filter
Off, HP, LP, BP
Off
Make-up
Auto, Manual
Auto
Meter
GR, OUT, IN
GR
Analog
On/Off
0deg
In
In/Out
In
Output
+/-24dB
0dB
Mix
0–100%
100%
Trim
-18 dB to +18 dB
0dB