---
titre: "Battery 4 Manual English — 2 Quick Start (p. 11-28)"
source: constructeur/crosstalk-arizona-edu-data-battery-204-20manual-20english-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# 2 Quick Start


<!-- page 11 -->

2
Quick Start

This chapter will walk you through the very basic tasks in your daily work with BATTERY. You'll
also learn how to work with cell parameters, apply effects, layer samples, and use effect buses
in a few simple steps.
This tutorial presumes that you have already installed, registered, and set up BATTERY as
instructed in the separate Setup Guide (see also ↑1.2, What Other Documents Are There?).
2.1
Stand-alone Mode vs. Plug-in Mode

Before you use BATTERY for the first time, it's worth explaining that it has two fundamentally
different modes of operation, stand-alone mode and plug-in mode:
▪
In stand-alone mode, BATTERY runs on its own, behaving like any other software on your
computer. In this mode, you'll use BATTERY as a simple software instrument, but you
won't be able to record your performance in a way that would allow you to sequence it in
sync with other software instruments, or to preserve it for later editing.
▪
In plug-in mode, BATTERY runs as a plug-in within a host application, which is usually a
sequencer or DAW (Digital Audio Workstation) application such as Cubase, Ableton Live,
or MASCHINE. You can then record and sequence your performance synchronized to the
host software's master clock — in sync with other plug-ins — and edit it at a later point.
There is an important technical difference between these modes, concerning the way in which
BATTERY handles MIDI and audio streams:
▪
In stand-alone mode, BATTERY will address your MIDI and audio hardware directly, which
requires you to specify some details about your hardware and drivers in the Audio and
MIDI Settings dialog (see also ↑3.9, Audio and MIDI Settings).
▪
In plug-in mode, audio and MIDI streaming will be handled by the host application.
In this chapter, we will use BATTERY in stand-alone mode. For instructions on how to set up
BATTERY with your audio interface, refer to the separate Setup Guide (see also ↑1.2, What
Other Documents Are There?).
Quick Start
Stand-alone Mode vs. Plug-in Mode

BATTERY 4 - Manual - 11

<!-- page 12 -->

2.2
Basic Operation

1.
Locate the application folder labeled “BATTERY 4” on your computer.
2.
Double-click “BATTERY 4.exe” (Windows) or “BATTERY 4.app” (Mac OS X). Alternative-
ly, you can use the shortcuts created during the installation process in the usual locations
on your operating system.
3.
Check whether your audio interface and MIDI devices are set up correctly in BATTERY's
Audio and MIDI Settings panel (as instructed in the separate Setup Guide; see also ↑1.2,
What Other Documents Are There?).
4.
Click on the magnifying glass symbol button in BATTERY's Header. This button is called
the Sidebar button, and it hides/shows BATTERY's Sidebar. Click on it once to hide the
Sidebar, click again to view it.
Quick Start
Basic Operation

BATTERY 4 - Manual - 12

<!-- page 13 -->

5.
In the Sidebar, click on the Library tab to open the Library Browser. Click on the Kits but-
ton and then on the Factory button to get to the factory Kits. Scroll down to the Boun-
cin Kit entry and double-click on it (or drag and drop it into the Cell Matrix).
→
You have loaded the Bouncin Kit to BATTERY, which will be our exemplary tutorial Kit for
this session.
As you can see, the cells have different colors assigned to them: kicks are red, snares are yel-
low, claps are pink etc. Let's change the cell color of all kicks to green:
Quick Start
Basic Operation

BATTERY 4 - Manual - 13

<!-- page 14 -->

1.
Click on the column header above the first column of cells, which contains half of the
Kit's kicks. The selected cells will be highlighted with an extra frame, which means that
they have been selected for editing.
2.
Press [Ctrl]/[Cmd] on your keyboard, and click on the column header above the second
column of cells, which will add column 2 to the selection.
3.
Right-click (or [Ctrl]-click on Mac OS) on one of the highlighted cells to bring up the con-
text menu.
Quick Start
Basic Operation

BATTERY 4 - Manual - 14

<!-- page 15 -->

4.
In the Cell Color submenu, click on the green square to assign the color to the selected
cells.
→
You have assigned a new cell color to the selected cells.
You can also select rows of cells for editing by clicking on the rows' letter headers, or even
the entire Cell Matrix by clicking on the field where the row and column headers intersect.
For an overview of the default coloring schemes, see ↑7.1, Supported File Types.
As long as multiple cells are selected for editing, any changes made in the context menu
(which you just used for assigning colors), the Quick Access area (the middle portion of the
screen), or in the Edit area (the area filling the lower portion of the screen), will affect all of
Quick Start
Basic Operation

BATTERY 4 - Manual - 15

<!-- page 16 -->

the selected cells; however, only the cell most recently clicked on will be displayed in the
Quick Access area's Waveform Control. Let's use multiple selection and the Mute button to
mute multiple cells at once:
1.
Select the cells containing the kicks, as you already did above.
2.
Click on the right button in the lower left corner of one of the cells. This is the Mute but-
ton.
→
You have muted the selected cells.
►
Click on the button again to unmute the selected cells.
The left button in the lower left corner of a cell is the Solo button.
To see which MIDI note a cell is triggered by, select a cell by clicking on it, and have a look at
the Key Range area on the left side of the Quick Access area (the middle portion of the screen,
where you can see the waveform in the Waveform Control).
The Key Range area displays that the selected cell is triggered from MIDI note C1.
Quick Start
Basic Operation

BATTERY 4 - Manual - 16

<!-- page 17 -->

As you can see in the screenshot above, each cell has a MIDI key range assigned to it; in this
case it is C1 to C1, which simply means that the relevant cell is triggered by the single MIDI
note C1. You can also have multiple MIDI notes trigger one cell (e.g., C1 to D1), AND this also
works the other way round; you can trigger multiple cells with a single MIDI note, which is a
cool way of layering sounds. To do this:
1.
Select two cells from the Kit using [Ctrl]-/[Cmd]-click, e.g., Kick Bouncin 1 and Kick
Bouncin 2.
2.
Click on the MIDI symbol in the Key Range area. This is the MIDI Learn button. It lights
up.
3.
BATTERY is now in MIDI learn mode. Hit a key on your MIDI keyboard (or a pad on your
MIDI controller), e.g., C1. This will set C1 as the lower note of the MIDI key range. Hit
the key again, which will set C1 also as the upper key of the MIDI key range.
→
The MIDI Learn button turns dim. Both cells A1 and A2 are now triggered by MIDI note
C1 from your MIDI controller.
You have just learned one way to layer sounds with BATTERY, which is a very useful technique
for creating drums and for sound design generally. But there's also another way to do this; by
layering multiple sounds in a single cell, which is a vital feature in BATTERY's tool set. To do
this:
1.
Click on a cell, e.g., B1 (Kick Bouncin 3), to select it for editing.
Quick Start
Basic Operation

BATTERY 4 - Manual - 17

<!-- page 18 -->

2.
In the Sidebar, click on the Library tab to open the Library Browser. Click on the Samples
button and then on the Factory button to get to the factory samples. Type ClosedHH
Bouncin 1 in the search box. The sample will appear in the Selection/Results window be-
low.
3.
Open the Editor page in the Edit area. Drag and drop the ClosedHH Bouncin 1 from the
Selection/Results window into the Mapping grid.
→
You have loaded a second sample layer into the cell. When you trigger cell B1 now, you
will hear both the kick sample and the hi-hat sample playing at the same time. (You can
also load sample layers directly from your hard drive via the context menu of a cell using
the Add Sample... entry.)
Quick Start
Basic Operation

BATTERY 4 - Manual - 18

<!-- page 19 -->

►
Now select cell B1 for editing and go back from the Editor to the Main page. The Wave-
form Control in the Quick Access area will now provide an additional drop-down menu,
allowing you to select the cell's individual sample layers for editing.
Be aware that all changes made on the right side of the Quick Access area (Tune, Pan,
Level etc.) affect the whole cell. So when you adjust the panorama setting using the Pan
knob, both sample layers will be positioned in the stereo field in the same way.
For advanced layer editing, you have to open the Editor page in the Edit area again (the lower
portion of the screen). From here, you can edit the parameters individually for each layer, and
you can also influence the trigger behavior of the sample layers within the cell.
Quick Start
Basic Operation

BATTERY 4 - Manual - 19

<!-- page 20 -->

The Editor page in the Edit area. When this page is opened, the Quick Access area above is replaced by a feature-rich Wave-
form and Loop Editor. Below you'll find the Mapping editor, allowing you to set velocity regions for the individual sample
layers. The displays on the right (Tune (st), Pan etc.) affect the individual sample layers.
Let's adjust the velocity region for the hi-hat layer so that it only will be triggered when you hit
the key fairly hard. To do this:
1.
Click on the hi-hat layer's Sample Block in the Mapping Grid to select it for editing.
Quick Start
Basic Operation

BATTERY 4 - Manual - 20

<!-- page 21 -->

2.
Now move the cursor to the lower border of the Sample Block. The cursor changes when
hovering over the border. Click and drag the border up to a velocity value of about 105
(you can also see the value in the Low Vel display on the right side of the Mapping Edi-
tor).
→
The hi-hat layer will now only be triggered upon receiving a velocity value of between 105
and 128. For any value below, only the kick layer will be triggered.
You can layer multiple samples in a cell this way, and have them all being triggered at once, or
only at certain velocity values.
Another handy feature is the Voice Groups module in the Setup page of the Edit area. You can
assign multiple cells to a voice group, limit the voice group's maximum number of voices,
thereby making the cells cut each other off. Let's have a look at how this works:
1.
Trigger two cells with longer samples quickly one after the other, e.g., D10 (SFX Boun-
cin 3) and C10 (SFX Bouncin 2). You'll notice that the sounds of both cells overlap.
2.
Now select them both for editing using [Ctrl]-/[Cmd]-click.
3.
Open the Setup page in the Edit area.
Quick Start
Basic Operation

BATTERY 4 - Manual - 21

<!-- page 22 -->

4.
In the Voice Groups module, open the drop-down menu labeled Kit, and select the entry 1
- <untitled>.
→
You have assigned both cells to voice group 1. The Voices setting should be set to 1 by
default (as depicted above), which means that only one voice is allowed to play at a time
in the voice group created.
You can rename the voice group by clicking on the pencil symbol next to the voice group
drop-down.
►
Now repeat step 1 (trigger both cells one after the other).
→
You'll notice that the cells cut each other off with a fade time as specified in the Fade
(ms) display of the Voice Groups module.
This is a very handy feature, e.g., for programming realistic drum sets, where an open hi-hat
and a closed hi-hat would never play at the same time.
Congratulations! You have learned about BATTERY's basic features. The following section will
explain the use of effects and effect buses in a nutshell.
2.3
Effect Modules and Cell Routing

This section will give you a quick introduction to applying effects, as well as some basic rout-
ing schemes using BATTERY's bus system.
There are two types of effects in BATTERY: individual cell effects and global master effects. The
cell effects can be found on the Main page and on the Effects pages in the Edit area (the lower
portion of the screen). The master effects are situated on the Master page of the Edit area.
To apply a cell effect to a cell:
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 22

<!-- page 23 -->

1.
Click on the cell you want to apply an effect to; e.g., cell C1 (Kick Bouncin 5).
2.
In the Effects page of the Edit area, click on the power button of the Compressor module
to activate it.
3.
Trigger cell C1 by clicking on it.
→
You can now hear the compressor module working.
To assign one effect to multiple cells, simply select multiple cells for editing with [Ctrl]-/
[Cmd]-click, and activate the desired effect module.
The effect chain runs from left to right, i.e., when using the Filter / EQ module and the
Compressor module on a cell, the cell's signal will first be filtered, and then compressed.
You can, however, rearrange the order of effects. To do so, click and drag an effect by its
handle (in the upper right corner of the module), and place it anywhere desired within the
effects chain.
Effects are not only a great tool for making a sound blend in with the mix; they can also be
used for sound design. Let's say you’ve applied a combination of effects to a cell, you like how
it sounds, and you want to use this cell as a basis for further work. You can now render the cell
in place, that is to say, you can convert the cell's sound into a unique copy. To do so:
1.
Right-/[Ctrl]-click on a cell with effects applied to it, e.g., cell C1 (Kick Bouncin 5), as we
have just applied the Compressor module to it.
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 23

<!-- page 24 -->

2.
Select the Render Cell... entry from the menu.
→
The cell's sample will be replaced with a re-sampled version of itself, including the ef-
fects applied to it; all effect modules formerly applied will be deactivated automatically.
This is not only useful for sound design, but it can also help you to reduce CPU usage.
Now let's have a look at the effects on the Master page of the Edit area. As you can see on the
Master page, the Buses module provides five buses: Bus 1, Bus 2, Bus 3, Bus 4, and the Mas-
ter bus.
The Buses module on the Master page of the Edit area with the Master bus selected for editing.
By default, all cells of a Kit are routed to the Master bus. Conversely, this means that any ef-
fect activated on the Master page will be applied to all cells in your Kit. Additionally, you can
use the remaining four buses as effect and submix buses. Here's how you do it:
1.
Click on Bus 1 to select it for editing.

You'll notice that all cells in the Cell Matrix turn into a dim state. This is because only
cells routed to the bus currently selected for editing will remain lit.
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 24

<!-- page 25 -->

2.
Click on the Filter / EQ module's power button to activate the module for Bus 1. In the
module, select the high frequency range (H), and turn the Gain down to apply a high cut.
3.
Now click on the header of row D to select the bottom row of cells for editing.
4.
Click and drag one of the selected cells onto Bus 1.
The dashed line signalizes that you are about to route the selected cells to the bus.
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 25

<!-- page 26 -->

→
The bottom row is now lit, which means that the cells are routed to Bus 1. Any changes
to the effects activated for the bus will affect all cells routed to it.

The signal path of the cells in row D is now cell > Bus 1 > Master > Stereo output pair
1/2.
You can also change routing settings for cells and buses from their context menus (Right-/
[Ctrl]-click).
2.3.1
Effect Presets

Each effect in the Effects and Master pages comes with a set of presets that you can reach by
clicking the drop-down menu to the right of each effect module's title. The Preset menu is
split into two submenus, one for factory content and one where you can save your own presets.
To save the current settings as a preset:
1.
Click the arrow to open the drop-down menu.
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 26

<!-- page 27 -->

2.
Select Save Preset… from the appearing Preset menu:
3.
Enter the name of your preset in the field beneath the label Preset Name:
4.
Click Save to finish the process and close the dialog box.
→
The current settings are saved as a user preset file on your hard disk. The preset will ap-
pear in the User submenu of the current effect module's Preset menu.
To load a preset from the Preset menu:
1.
Click the arrow to open the drop-down menu.
2.
Navigate through the submenus and select a preset to load it.
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 27

<!-- page 28 -->

You are now familiar with the basic concepts of effect usage and routing; however, we’ve only just scratched the surface
here. You can build more complex routing schemes, use effect buses while bypassing the Master bus, and so on. For further
information on this, refer to 3.7.6.
Quick Start
Effect Modules and Cell Routing

BATTERY 4 - Manual - 28