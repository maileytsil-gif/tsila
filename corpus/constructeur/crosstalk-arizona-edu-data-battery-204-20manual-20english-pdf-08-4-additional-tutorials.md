---
titre: "Battery 4 Manual English — 4 Additional Tutorials (p. 115-128)"
source: constructeur/crosstalk-arizona-edu-data-battery-204-20manual-20english-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# 4 Additional Tutorials


<!-- page 115 -->

4
Additional Tutorials

Find additional step-by-step instructions for some of the less self-explanatory tasks in this
chapter.
4.1
Importing Files to the Library

In this section, you'll learn how to import your own samples to BATTERY's Library, and how to
use the categorization system to prepare them for convenient use. Here's how you do it:
1.
Open the Files Browser in the Sidebar.
2.
Navigate to a folder containing the samples you'd like to import. For this tutorial, we’ve
prepared a drums folder with our go-to kicks, snares, and hi-hats already presorted in sub-
folders.
3.
Right-click ([Ctrl]-click) on the folder you'd like to import, and select Import to Library
from the context menu.
Additional Tutorials
Importing Files to the Library

BATTERY 4 - Manual - 115

<!-- page 116 -->

4.
The categorization window below now allows you to assign tags to the samples. We’ll cre-
ate two new tags called Kicks and Punchy on tag levels one and two, using the + Add New
button.
5.
Click OK to import your samples to BATTERY's Library using the created tags.
6.
Open the Library Browser in the Sidebar.
7.
Click on Samples and User to navigate to the non-factory samples section of the Library.
Additional Tutorials
Importing Files to the Library

BATTERY 4 - Manual - 116

<!-- page 117 -->

8.
You'll see the first level tag, Kicks, at the top of the category window, and after clicking
on it, the second level category tags (Punchy) will appear right beneath the first level.
Clicking on either one will result in the previously imported samples being listed in the
Selection/Results window below.
→
The new samples were successfully imported to the Library.
4.2
Automation

Automating BATTERY's parameter controls allows you to record modulation of BATTERY's pa-
rameters throughout the course of a track in a host application; e.g., applying a filter sweep to
a snare track, or changing the volume of an entire drum track over time. This is a feature you
don't want to miss out on! To give you a rough idea of what's possible when using automation,
here's a tutorial on automating BATTERY in Steinberg Cubase 6. With a little research, you
should be able to apply the instructions to your host software of choice.
To begin with, there are two ways in which BATTERY can be automated in Cubase 6:
▪
Automation via MIDI CC: In this case, you assign one of BATTERY's parameter controls
(e.g., the High Cut control of the Filter module) to a MIDI controller (e.g., to a slider on
your MIDI keyboard), and record automation via MIDI.
Additional Tutorials
Automation

BATTERY 4 - Manual - 117

<!-- page 118 -->

▪
Automation via host automation ID: In this scenario, you assign one of BATTERY's parameter
controls (e.g., the High Cut control of the Filter module) to a host automation ID in Cu-
base 6, and then address BATTERY from the automation lane of the relevant instrument
track in Cubase.
Automation via MIDI CC
To automate a BATTERY parameter control via MIDI CC in Cubase 6:
1.
Open Cubase.
2.
Open a new session.
3.
Load BATTERY from the VST Instruments Rack ([F11]), and create a MIDI track for it.
4.
Duplicate the MIDI track you have just created.
5.
Load the Bouncin Kit to BATTERY (as explained in ↑2.2, Basic Operation).
6.
Record a simple four-bar drum loop using the Bouncin Kit's cells C2 (Kick Bouncin 6)
and C3 (Snare Bouncin 5).
7.
You should now have a MIDI track containing your drum loop, and another empty MIDI
track in Cubase.
8.
Back in BATTERY, select cell C3 (Snare Bouncin 5) for editing.
Additional Tutorials
Automation

BATTERY 4 - Manual - 118

<!-- page 119 -->

9.
Activate the Filter module in BATTERY's Main page using its power button. This will acti-
vate the Filter module for cell C3 solely.
10. Right-click/[Ctrl]-click on the High Cut control in the Filter module, and select Learn MIDI
CC.
11. Move a control element on your MIDI controller (such as a slider).
12. The High Cut control in BATTERY should instantly pick up the input from the MIDI con-
troller, and you should be able to lower/raise the high-cut filter operating the control ele-
ment now. There also should be a new entry in the MIDI tab of the Sidebar's Automation
page:
Additional Tutorials
Automation

BATTERY 4 - Manual - 119

<!-- page 120 -->

As you can see, the control in BATTERY (Cutoff LP), part of the Filter module earlier acti-
vated for snare cell C3 (C:3), was assigned to MIDI CC #8 (CC #8), which in our case was
a slider on a MIDI keyboard.
If this did not work, please check your MIDI connections and/or refer to the documenta-
tion of your host software.
13. Back in Cubase, select the second — empty — MIDI track, and start recording.
14. Use the MIDI controller to adjust the high-cut filter while recording.
→
The automation data should now be recorded to the second MIDI track, and you should
hear the filter sweep on the snare.
Cubase also allows you to record certain MIDI CC's to a track's automation lane as automa-
tion data instead of writing the automation as MIDI data. This can be configured via the
"MIDI Controller Automation Setup" panel in Cubase. The advantage of automation data is
that it's easier to edit compared to automation as MIDI data.
Additional Tutorials
Automation

BATTERY 4 - Manual - 120

<!-- page 121 -->

Automation via Host Automation ID
To automate a BATTERY parameter control via host automation ID in Cubase 6:
1.
Open Cubase.
2.
Open a new session.
3.
Create a new Instrument track in Cubase.
4.
Select BATTERY as VST instrument for the Instrument track.
5.
Load the Bouncin Kit to BATTERY (as explained in ↑2.2, Basic Operation).
6.
Record a simple four-bar drum loop using the Bouncin Kit's cells C2 (Kick Bouncin 6)
and C3 (Snare Bouncin 5).
7.
You should now have a MIDI track containing your drum loop.
Additional Tutorials
Automation

BATTERY 4 - Manual - 121

<!-- page 122 -->

8.
Back in BATTERY, select cell C3 (Snare Bouncin 5) for editing.
9.
Activate the Filter module in BATTERY's Main page using its power button. This will acti-
vate the Filter module for cell C3 solely.
10. Right-click/[Ctrl]-click on the High Cut control in the Filter module, and select Enable
Host Automation (ID: 0).
Additional Tutorials
Automation

BATTERY 4 - Manual - 122

<!-- page 123 -->

11. There should now be a new entry in the Host tab of the Sidebar's Automation page:

As you can see, the control in BATTERY (Cutoff LP), part of the Filter module earlier acti-
vated for snare cell C3 (C:3), was assigned to host automation ID 0 (#0).
12. Back in Cubase, open the MIDI track's automation lane using the Show/Hide Automation
button.
Additional Tutorials
Automation

BATTERY 4 - Manual - 123

<!-- page 124 -->

13. Within the automation lane, click on the button right to the R and W buttons, and select
More... from the subsequent menu.
Additional Tutorials
Automation

BATTERY 4 - Manual - 124

<!-- page 125 -->

14. A new window opens. There should be a folder labeled Battery 4 in there now. Expand it,
select Cutoff LP from the list, and click OK.
Additional Tutorials
Automation

BATTERY 4 - Manual - 125

<!-- page 126 -->

15. The automation lane now controls the High Cut filter in BATTERY. Click the R button in
the automation lane, and use the cursor to draw in automation data within the automation
lane's track.
16. Start playback.
→
You should now hear the filter sweep on the snare.
4.3
Side-chain Compression

Side-chain compression is a popular technique used in contemporary electronic music, and it
can help you achieve a quite polished sound without even touching the EQs. E.g., bass sam-
ples and kick drums share frequencies in the same frequency range, which can quickly lead to
a muddy mix as both elements interfere with each other. Using side-chain compression, you
can use one sound (e.g., the kick) as a trigger for lowering the volume of another sound (e.g.,
the bass). Let's try this out using our tutorial Kit:
1.
Load the Bouncin Kit to BATTERY as explained in the introduction in ↑2.2, Basic Opera-
tion.
2.
Select cell D1 (Kick Bouncin 7) for editing, and open the Master page in the Edit area.
Additional Tutorials
Side-chain Compression

BATTERY 4 - Manual - 126

<!-- page 127 -->

3.
Drag and drop cell D1 onto Bus 1 in the Buses module.

The cell is now routed to effect/submix bus 1.
4.
With Bus 1 highlighted, activate the Compressor module, and select the SC Bus Comp
mode from the compressor mode selection menu.
Additional Tutorials
Side-chain Compression

BATTERY 4 - Manual - 127

<!-- page 128 -->

5.
Now drag and drop cell B2 (Kick Bouncin 4) into the Compressor module's Source selec-
tion rectangle (the one labeled SC). Make sure that Bus 1 stays highlighted while you do
this.
6.
Set the Compressor module to the following settings: Thresh to 13.0; Ratio to 10; Attack
to 0.1; Release to 200; and Gain to 12.0.
7.
Trigger cell D1. When it is playing, trigger cell B2.
→
You should now see and hear the compressor kicking in each time you trigger cell B2, so
that the bass sound is faded out each time the kick comes into play. The effect will be
even more hearable if you sequence your drums in a host sequencer. Experiment with the
settings to see what works best for the particular situation.
Additional Tutorials
Side-chain Compression

BATTERY 4 - Manual - 128