---
titre: "xferrecords com manual serum 2 docs — couverture et sommaire (p. 1-12)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->



<!-- page 2 -->

﻿
﻿
Serum 2 User Guide
2
Serum 2
Serum 2 plug-in for Microsoft Windows and Apple macOS
A synthesizer instrument plug-in for VST3, Audio Unit, and AAX hosts
Version 2.0.18
Manual Version: 1.0.3
April 27, 2025
Serum 2 Development Team
Oli Cash
Nick Dowell
Steve Duda
Dave Gamble
Damon Hancock
Lance Thackeray
With special assistance from:
Matt Aimonetti
Laurent de Soras
Andrew Simper
Yan Lhert
Manual: John Jerney
Special thanks to:
Jeff Rona
Joel Zimmerman
David Alexander
Copyright © 2014-2025 Xfer Records, Inc. All rights reserved.
The information contained in this document is subject to change without notice. In no event shall Xfer
Records or the author of this document be liable for any damages arising out of or related to this docu­
ment or the information contained within it. No part of this document may be reproduced or transmit­
ted in any form or for any purpose without the express written consent of Xfer Records.
VST Plugin technology by Steinberg
VST is a trademark of Steinberg Media Technologies GmbH. All other copyrighted trademarks belong to
their respective owners.
W W W . X F E R R E C O R D S . C O M

<!-- page 3 -->

Serum 2 User Guide
3
Table of Contents
Welcome
13
Registering Serum .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 13
Getting in Touch .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
Downloading Serum .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
Installing Serum. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
Installing on macOS and Windows-based PCs .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
Uninstalling Serum on Windows-based PCs. . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Uninstalling Serum on macOS Computers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Exploring Serum
16
Exploring Sound Design in Serum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Getting Started
18
Adding Serum to a Track . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Loading a Serum Preset .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
Creating a New Sound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Saving Changes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
Embedding Content When Saving a Preset .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 22
Dragging Audio to Your DAW .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 22
Exploring Basic Operations .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 23
Displaying Help (Tooltips). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Using the Serum Keyboard .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 25
Using Knobs and Sliders .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 25
Undo and Redo .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 27
Controlling the Main Output Volume .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 27
Using Oscillators and Filters .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 28
Enabling an Oscillator or Filter .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 28
Choosing Oscillator or Filter Options .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 29
Using Pitch Controls .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 29
Routing an Oscillator or Filter .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 31
Accessing the Oscillator or Filter Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 33
Resizing the UI .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 36
Using Wavetable Oscillators
37
What is a Wavetable? .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 38
Anatomy of a Serum Wavetable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

<!-- page 4 -->

Serum 2 User Guide
4
Using Wavetables .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 39
Exploring the Waveform Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Phase .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 41
Randomizing the Phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Setting Phase Memory .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 44
Wavetable Position .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 45
Unison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
Warp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
Using Multisample Instruments
58
Selecting a Multisample Instrument . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
Setting the Multisample Envelope. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Velocity Track .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 62
Random .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 62
Setting Multisample Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
Timbre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Unison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Warp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
Switching the Last Note Played to a Sample .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 67
Using Sample Instruments
68
Selecting the Sampler .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 69
Setting the Sample Start and End .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 71
Performing Sample Operations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
Slicing Samples .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 74
Loop Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 77
Setting the Loop Start and End. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
Setting the Crossfade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
Setting Sample Parameters .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 80
Scan .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 80
Unison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Warp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
Switching a Sample to a Wavetable .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 84

<!-- page 5 -->

Serum 2 User Guide
5
Using Granular Synthesis
85
Selecting Granular Synthesis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
Setting the Sample Start and End .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 87
Performing Granular Operations .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 88
Loop Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 89
Setting the Loop Start and End. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
Setting the Crossfade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
Window Amount .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 91
Unison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
Setting the X|Y Control .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 96
Setting Granular Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
Warp Mode .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 99
Scan .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 99
Density .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 101
Length .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 101
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Setting the Grain Randomization .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 102
Switching a Sample to a Wavetable .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 103
Using Spectral Synthesis
104
Selecting Spectral Synthesis .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 104
Setting the Sample Start and End .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 106
Setting the Sample High and Low Frequencies .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 107
Performing Sample Operations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
Loop Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 109
Setting the Loop Start and End. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Setting the Crossfade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Unison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
Setting the X|Y Control .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 114
Setting Spectral Parameters .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 116
Scan .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 116
Cut. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
Mix. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Setting the Warp Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
Switching a Sample to a Wavetable .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 122

<!-- page 6 -->

Serum 2 User Guide
6
Using the Sub Oscillator
123
Exploring the Sub Oscillator .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 124
Pitch .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 124
Waveform .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 124
Phase .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 127
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Using the Noise Oscillator
128
Exploring the Noise Oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
Loading a Preset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
Loading a Sample .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 130
One Shot/Looping .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 131
Start .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 131
Random .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 131
Pitch .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 132
Fine .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 132
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Using the Filter Modules
133
Exploring the Filter Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
Routing an Oscillator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
Filter Type .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 135
Filter Types and Var Parameter Functions. . . . . . . . . . . . . . . . . . . . . . . . . 135
Filter Display Options .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 140
Setting Filter Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
Cutoff .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 141
Resonance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
Drive. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
Fat (and Others) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
Pan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
Mix. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
Level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
Using the Mixer
144
Exploring the Mixer .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 144
Sending to the Busses .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 146
Setting Pan and Levels .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 147

<!-- page 7 -->

Serum 2 User Guide
7
Mixing Filters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
Routing to the Busses. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Setting Pan, Mix and Levels. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Mixing the Busses .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 150
Setting Levels .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 150
Setting the Main and Direct Levels .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 151
Using Serum FX
152
Using the FX Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
Selecting a Rack .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 153
Loading Rack Presets .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 154
Adding Modules .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 155
Reordering Modules .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 156
Copying a Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
Bypassing a Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
Removing a Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
Saving a Rack as a Preset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
Exploring FX Rack Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
Modulating FX Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
Exploring FX Module Operations .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 160
Exploring Individual FX Modules .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 161
Bode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
Chorus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Compressor .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 162
Convolve .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 164
Distortion .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 167
Equalizer. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
Flanger. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
Hyper/Dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
Phaser .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 174
Reverb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
Splitter L/H .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 177
Splitter L/M/H .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 179
Splitter MS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
Utility .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 182

<!-- page 8 -->

Serum 2 User Guide
8
Exploring Sound Modulation
183
Using Envelopes .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 183
Configuring Envelopes .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 184
Modifying Envelopes .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 186
Assigning an Envelope to a Control .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 187
Using LFOs .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 188
Configuring LFOs .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 188
Drawing an LFO Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
Modifying LFOs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
Assigning an LFO to a Control .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 194
Setting the Modulator Depth .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 195
Setting Negative Modulation Depths .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 196
Copying a Wavetable Shape to an LFO .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 197
Copying an LFO Shape to a Wavetable .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 198
Modulating LFO Points .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 198
Modulating LFO Points Using Menus .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 199
Modulating LFO Points Using Drag and Drop . . . . . . . . . . . . . . . . . . . . . . . . . . 200
Using Context Menus with Controls .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 200
Setting Velocity and Notes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Velocity Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
Note Settings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 204
Using Macros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
Assigning a Macro. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Using Oscillators and Filters as Modulation Sources .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 208
Using the Modulation Matrix
209
Exploring the Modulation Matrix .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 210
Moving Modulations in the Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Bypassing a Modulation .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 213
Removing a Modulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Performing Matrix Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
Setting Voicing and Portamento
215
Voicing Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
Mono .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 216
Legato .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 216
Poly .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 216

<!-- page 9 -->

Serum 2 User Guide
9
Portamento Settings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 217
Porta. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
Curve .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 218
Always . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218
Scaled .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 218
Using Clips
219
Exploring the CLIP Module .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 220
Setting Global Parameters .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 221
Creating a New Clip Bank .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 222
Saving Clip Banks .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 223
Working with the Piano Roll .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 224
Setting the Grid Size .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 228
Zooming the Piano Roll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
Folding the Piano Roll. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
Managing the Clip Length .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 232
Configuring Clip Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
Managing Clips . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
Triggering Clips .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 236
Recording Your Clips .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 237
Managing MIDI Out .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 239
Routing MIDI to Another Instrument .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 239
Configuring the Clip Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
Using Macros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
Using the Arpeggiator
244
Exploring the Arpeggiator .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 245
Setting Global Parameters .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 246
Creating a New Arp Bank. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
Saving Arp Banks .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 247
Setting the Arp Pattern. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
Creating a Custom Pattern. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
Loading a Pattern .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 249
Creating a New Pattern. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
Configuring the Pattern Settings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 250
Saving a Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
Renaming a Pattern .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 252
Using the Arp Graph Editor .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 253
Transpose Settings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 254

<!-- page 10 -->

Serum 2 User Guide
10
Playback Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
Retrigger Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
Velocity Settings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 262
Managing Arpeggiators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
Triggering the Arpeggiator .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 264
Managing MIDI Out .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 265
Configuring the Arp Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
Using the Keyboard
267
Transpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
Setting the Key and Scale .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 268
Setting Swing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
Oscillator Mapping .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 269
Using the Wavetable Editor
274
Using the Thumbnails .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 275
Using the Drawing Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
FFT Area .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 278
Managing Frames (Subtables) .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 281
Exploring Common Frame Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
Copying and Pasting Frames .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 282
Inserting and Removing Frames .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 282
Sorting Frames .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 283
Using the Formula Parser . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
Exploring the Menu Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
Importing a Wavetable .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 285
Exporting a Wavetable .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 285
Single Menu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
All Menu. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
Morph Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 289
Saving Wavetables .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 290
Importing Audio as Wavetables
291
Understanding Multi-cycle Waveforms .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 291
Importing Multi-Cycle Waveforms. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
Advanced Imports .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 294
Text File Overrides for Specific Results (Advanced) .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 295
Importing Single-Cycle Waveforms .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 296
Using the Import Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 298
Creating a Sound Specifically for Serum Import (Advanced) .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 298

<!-- page 11 -->

Serum 2 User Guide
11
Importing an Image File as a Wavetable. . . . . . . . . . . . . . . . . . . . . . . . . . 300
Embedding Wavetables When Saving a Preset .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  302
Using the Formula Parser
304
Basic Functions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
Built-in Binary Operators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305
Constants and Variables .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 306
Exploring the Formula Presets Menu .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 307
Saving Your Own Formulas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
Managing Formula Files Manually (Advanced). . . . . . . . . . . . . . . . . . . . . . . . . . 308
Exploring Formula Parser Examples .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 309
Exploring Global Settings
312
Using the Global Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
Preferences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313
Setting the Voice Control .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 316
Loading a Preset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 316
Creating a New Configuration .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 317
Configuring the Voice Control .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 317
Setting Randomization .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 318
Setting the Scaling .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 318
Saving the Voice Control Settings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 319
Setting the Quality .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 319
Setting the Tuning .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 320
Setting Concert Pitch .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 320
Using a Tuning File .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 320
Using MTS-ESP to Set the Tuning .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 321
Locking the Tuning Configuration .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 321
Checking the Build Version and Date .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 322
Appendix A: Using the Main Menu
323
Appendix B: Using the Presets Browser
327
Navigating the Folders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
Loading a Preset .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 328
Previewing Presets .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 328
Searching Presets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 329
Searching by Name .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 329
Searching by Categories or Tags .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 330
Searching by Ratings .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 330

<!-- page 12 -->

Serum 2 User Guide
12
Managing Your Presets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
Displaying and Editing Preset Metadata .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 331
Specifying the Category .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 332
Rating Presets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 333
Performing Standard Preset Operations. . . . . . . . . . . . . . . . . . . . . . . . . . 334
Creating and Exporting a Pack. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337
Appendix C: Editing the Serum Preferences File
340
Changing the Default Artist Name .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 340
Enabling Preset Changes using a MIDI Controller .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 341
Using Notes to Trigger Preset Changes .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 342
Enabling Oscillator Preset Changes using a MIDI Controller . . . . . . . . . . . . . . . 342
Appendix D: Exploring the Serum File Structure
344
Appendix E: Creating Wavetables
346
What Makes for a Good Wavetable? .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 346
Table Ordering. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 346
Interpolation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347
Creating Wavetables from Scratch .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 347
Appendix F: Optimizing Serum
348
Exploring CPU Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348
Managing Unison .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 348
Appendix G: Keyboard Shortcuts
349
Presets and Presets Browser. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
Controls (Knobs and Sliders) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
Modules (Oscillators and Filters). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
Sample/Granular/Spectral .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 350
Audio .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 350
FX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 350
Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351
LFOs .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 351
Modulation .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 351
Clips. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 352
Clips (Note Movements) .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 352
Clips (Note Operations) .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 353
Wavetable Editor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
Additional Credits
354