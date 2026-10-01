---
titre: "xferrecords com manual serum 2 docs — Appendix A: Using the Main Menu (p. 323-326)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Appendix A: Using the Main Menu


<!-- page 323 -->

Serum 2 User Guide
323
Appendix A: Using the Main Menu
You can use the main menu to complete operations that affect the overall performance and capabilities
of Serum. These operations include managing presets, initializing modules, rendering waveforms,
configuring MPE settings, and more.
You can access the main menu
 near the top right of the Serum window.
Serum Main Menu

<!-- page 324 -->

﻿
Appendix A: Using the Main Menu
Serum 2 User Guide
324
The following table describes each menu item:
Category
Options
Description
General
About
Display Serum release information.
Read the manual
Display this manual, the Serum User Guide (PDF).
Check for updates
Display whether an update is available, with a link to
the website.
Initialization
Init Preset
Initialize Serum to allow you to create a new patch.
Init LFOs + LFO Mods
Initialize just the LFOs and LFO modulations
Init Modulations
Initialize just the modulation assignments, leaving
everything else untouched (including the LFOs).
Presets
Load Preset
Load a preset from storage. A system dialog appears
allowing you to locate the preset file.
Revert to Saved
After loading a preset and making changes, revert to
the saved preset.
Save as Default Preset
Save the current preset to the following file:
Serum 2 Presets/Presets/User/
default.SerumPreset
Note that if you are running the Serum FX version,
this saves to the defaultFX.SerumPreset
file. This allows you to configure different default
configurations for Serum and Serum FX.
When you load Serum FX, it will look for the
defaultFX.SerumPreset file. If the file isn’t
found, Serum FX instead looks for the
default.SerumPreset file.
Import
Import Preset Pack
Import a Serum preset pack. A system dialog appears
allowing you to locate the preset pack.
Rendering
Render OSC Warp
Use the current wavetable frame of the selected
oscillator and create 256 frames (subtables) spanning
0 to 100% of the WARP knob.
Resample to
Play a note of the preset for one bar and capture
(render and import) the result as a wavetable in the
selected oscillator (or OSC A and OSC B).
Folders
Open Serum 2 Presets
Folder
Display the Serum 2 Presets folder using the Finder
(macOS) or Explorer (Windows).
Rescan Folders on
Disk
Rescan the Serum 2 Presets folder.
Do this when you make changes to the folders
outside of Serum (using the Finder or Explorer).

<!-- page 325 -->

﻿
Appendix A: Using the Main Menu
Serum 2 User Guide
325
Category
Options
Description
MIDI/Tuning
Load MIDI Map
Load a saved MIDI CC map from storage.
Save MIDI Map
Save a MIDI CC map to storage. By default, MIDI
maps are stored in the Serum 2 Presets > System>
MIDI CC Maps folder.
Saving a MIDI map as default.SerumMIDIMap in the
default folder instructs Serum to load that MIDI map
every time you add an instance of Serum or you load
a preset.
Load Tuning (.tun)
Load a tuning file for the current instance of Serum. A
dialog appears allowing you to locate the appropriate
tuning (.tun) file.
See “Using a Tuning File” for more information.
MPE
MPE Enabled
Enable support for MIDI Polyphonic Expression
(MPE).
When enabled, Serum responds to MPE messages,
allowing for more expressive and nuanced musical
performances using compatible MPE controllers.
Important: In the VST3 version of Serum (not the AU
or AAX versions), when MPE is disabled, Serum will
respond to VST3 Note Expression in cases when the
host DAW supports this feature (this includes hosts
such as Bitwig, Cubase, and Nuendo).
This means that main menu options to map note
expressions to macros remain available and applicable
even when MPE is disabled. However, the MPE Bend
Range option is not available since VST3 pitch note
expression has a fixed range of +/-120 semitones.
MPE: XYZ -> Macro
1,2,3
Map the X, Y, and Z axes of an MPE-compatible
controller to Serum macros 1, 2, and 3 respectively.
In this context, the x, y, and z axes represent the three
dimensions of touch-sensitive control associated with
MPE.
Specifically:
•	 X-axis: Horizontal movement, often used to
control pitch bending.
•	 Y-axis: Vertical movement, often assigned to
parameters like filter cutoff or modulation depth.
•	 Z-axis: Pressure or aftertouch, controlling
intensity-related effects like volume or timbre.

<!-- page 326 -->

﻿
Appendix A: Using the Main Menu
Serum 2 User Guide
326
Category
Options
Description
MPE (cont.)
MPE: YZ -> Macro 1,2
Map the X and Y axes of an MPE-compatible
controller to Serum macros 1 and 2 respectively.
MPE: Y -> Mod Wheel
Map the Y-axis movement of an MPE controller to the
Modulation Wheel (Mod Wheel) control.
MPE Bend Range: 48
The pitch bend range for MPE controllers, specified as
the number of semitones above or below the original
pitch.
Choose this menu option to display a dialog allowing
you change the current value. You can set any value
from 1 to 96 semitones.
A wider range allows for more expressive pitch
variations and glides across the tonal spectrum.