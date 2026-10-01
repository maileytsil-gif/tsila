---
titre: "xferrecords com manual serum 2 docs — Appendix C: Editing the Serum Preferences File (p. 340-343)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Appendix C: Editing the Serum Preferences File


<!-- page 340 -->

Serum 2 User Guide
340
Appendix C: Editing the Serum Preferences File
Serum stores application preferences in a special file called Serum2Prefs.json. You can find this file
in the following locations:
•	 (macOS) ~/Library/Preferences/
•	 (Windows) %APPDATA%\Xfer\Serum 2\ (use Windows Key + R to access)
This file stores the preferences accessible on the Preferences page, the last known path to the Serum
Presets folder, and (optionally) power user options, among other options.
Serum automatically recreates this file if it is missing, so you can reset your preferences to the
factory defaults simply by deleting this file and restarting Serum.
You probably shouldn’t change many of the settings. However, there are a few power user settings that
you might want to explore.
Important: When editing the JSON file, use a text editor application such as TextEdit (macOS) or
Notepad (Windows). Do not use an application that saves the file in any format other than text (the
standard format for JSON files).
For each preference described below, do the following:
1.	Edit the Serum2Prefs.json file using a text editor.
2.	Make the changes, as described in the corresponding section below.
Very Important: Each line in the configuration file ends with a comma (,). Ensure that you keep the
comma at the end of each line when you edit the file.
3.	Save the file.
Changing the Default Artist Name
You can specify the default artist name for the Init preset. This is the name that appears in the ARTIST
field when you initialize a new preset using the main menu.
Locate the following line:
“Default Author”: “  “,
Type the name you want to use between the quotation marks. For example:
“Default Author”: “Wolfgang A. Mozart”,
Any presets made from scratch will now have the name you specified listed as the artist.

<!-- page 341 -->

﻿
Appendix C: Editing the Serum Preferences File
Serum 2 User Guide
341
Enabling Preset Changes using a MIDI Controller
You can configure Serum to allow you to step through presets using a physical controller (such as a
button on a MIDI keyboard) by mapping the controller’s MIDI CC number to the corresponding preset
selection parameter.
In the Serum preferences file, locate the following line:
“Enable CCForRockers”: 0,
Change the line to the following:
“Enable CCForRockers”: 1,
Next, locate the following lines:
“CCForRocker Preset +”: -1,
“CCForRocker Preset -”: -1,
The first line maps the preset forward arrow (>) to a MIDI CC number; similarly, the second line maps
the preset backward arrow (<) to a MIDI CC number.
Update the -1 values on each line to the appropriate MIDI CC number for your controller (button).
For example, if you would like to assign MIDI CC 21 to the preset forward arrow and MIDI CC 22 to the
preset backward arrow, change the lines to the following:
“CCForRocker Preset +”: 21,
“CCForRocker Preset -”: 22,
For the settings discussed in this section, the value -1 means unassigned.
To remove the MIDI CC assignments that you configured in this section, edit the file and reset
the corresponding values to -1.
A MIDI controller button mapped to a CC typically sends a value of 127 when pressed and
a value of 0 when released. In Serum, a value of 64 or above triggers the action (changes
the preset). Similarly, Serum needs to receive a value below 64 before the action can be
triggered again.

<!-- page 342 -->

﻿
Appendix C: Editing the Serum Preferences File
Serum 2 User Guide
342
Using Notes to Trigger Preset Changes
Alternatively, you can configure Serum to allow you to step through presets using MIDI notes. The
configuration process is very similar to mapping controller MIDI CC numbers, as described in the
previous section.
In the Serum preferences file, locate the following line:
“Enable CCForRockers”: 0,
The value on this line might already be 1 if you followed the procedure in the previous section. Change
the line to the following:
“Enable CCForRockers”: 2,
Next, locate the following lines:
“CCForRocker Preset +”: -1,
“CCForRocker Preset -”: -1,
Again, the values might be different than -1. As before, the first line maps the preset forward arrow (>)
to a MIDI note number; similarly, the second line maps the preset backward arrow (<) to a MIDI note
number.
Update the values on each line to the appropriate MIDI note number.
Enabling Oscillator Preset Changes using a MIDI Controller
You can similarly configure Serum to allow you to step through oscillator presets using a physical
controller by mapping the controller’s MIDI CC value to the corresponding preset selection parameter.
In the Serum config file, locate the following line:
“Enable CCForRockers”: 0,
Change the line to the following:
“Enable CCForRockers”: 1,
Next, locate the following lines:
“CCForRocker OSC A +”: -1,
“CCForRocker OSC A -”: -1,

<!-- page 343 -->

﻿
Appendix C: Editing the Serum Preferences File
Serum 2 User Guide
343
The first line maps the OSC A preset forward arrow (>) to a MIDI CC value; similarly, the second line
maps the OSC A preset backward arrow (<) to a MIDI CC value.
Update the -1 values on each line to the appropriate MIDI CC value for your controller (knob).
For example, if you would like to assign MIDI CC 23 to the OSC A preset forward arrow and MIDI CC
24 to the OSC A preset backward arrow, change the lines to the following:
“CCForRocker OSC A +”: 23,
“CCForRocker OSC A -”: 24,
Remember to include the comma (,) at the end of each line. This is important. Also, recall that you can
reset these settings by changing the values back to -1.
Note that OSC B, OSC C, and OSC N (the noise oscillator) have similar settings in the configuration file.
Use the same procedure to assign those to appropriate MIDI CC values for your controllers (knobs).