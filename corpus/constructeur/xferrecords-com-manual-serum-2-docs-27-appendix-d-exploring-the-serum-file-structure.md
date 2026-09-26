---
titre: "xferrecords com manual serum 2 docs — Appendix D: Exploring the Serum File Structure (p. 344-345)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Appendix D: Exploring the Serum File Structure


<!-- page 344 -->

Serum 2 User Guide
344
Appendix D: Exploring the Serum File Structure
This appendix describes how Serum stores data on your computer drive.
Serum File Structure
The Serum Presets folder contains all the files that Serum reads and writes, except the preferences file.
Serum installs this folder to the following locations by default:
•	 (macOS) /Library/Audio/Presets/Xfer Records/
•	 (Windows) /Documents/Xfer/
The following describes some of the more important folders in the file structure:
Folder
Description
Arp Banks
Contains factory-supplied and user-saved ARP (arpeggiator) banks.
Clip Banks
Contains factory-supplied and user-saved CLIP banks.
Multisamples
Contains factory-supplied and user-saved multisample instruments.

<!-- page 345 -->

﻿
Appendix D: Exploring the Serum File Structure
Serum 2 User Guide
345
Folder
Description
LFO Shapes
Contains LFO shapes (.XferShape files) that are in the same file format
as the shape files used in the LFOTool plug-in. LFO shapes appear in the
following locations:
•	 The LFO section of Serum
•	 The waveshaper (in the FX section, when the X-Shaper effect type is
selected and the waveshaper graph is displayed)
•	 The Remap editor (when WARP mode is set to Remap and the graph is
displayed)
Presets
Contains subfolders holding the presets that you see in the presets browser
and menu. These include the factory presets together with any presets you
save.
Samples
Contains factory-supplied (tonal and non-tonal) and user-saved samples.
System
Contains the four formula files:
•	 FormulaFactoryMultis
•	 FormulaFactorySingles
•	 FormulaUserMultis
•	 FormulaUserSingles
You can edit any of these text files, but the intent and recommendation is
to edit User files and leave Factory files untouched. See “Using the Formula
Parser” on page 304 for more information about formulas.
The System folder also contains a MIDIccMaps folder, which is where any
MIDI CC maps you create are stored. Finally, the User.dat file holds your
registration information.
Tables
Contains subfolders holding the wavetables that you see in Serum. These
include the factory presets along with any wavetables you save. Wavetables
are special Serum-saved WAV files.
You can create your own subfolders in the Tables folder, but Serum does not
scan deeper (no sub-subfolders are scanned).