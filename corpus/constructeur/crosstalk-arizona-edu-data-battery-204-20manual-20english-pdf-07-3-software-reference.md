---
titre: "Battery 4 Manual English — 3 Software Reference (p. 29-114)"
source: constructeur/crosstalk-arizona-edu-data-battery-204-20manual-20english-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# 3 Software Reference


<!-- page 29 -->

3
Software Reference

This chapter is your reference for functional descriptions of every element on BATTERY's user
interface. We'll start with a general overview in ↑3.1, General Overview and then break down
the individual areas and their further sections and elements from ↑3.2, Application Menu Bar
to ↑3.7, Edit Area. In ↑3.8, Preferences, you will find a thorough description of BATTERY's
preferences panel, and an overview of the Audio and MIDI Settings panel will follow in ↑3.9,
Audio and MIDI Settings.
3.1
General Overview

BATTERY 4 has a straightforward and flexible user interface, with designated areas for drum/
sample programming, browsing, automation, modulation, and an effects and routing section.
The user interface.
Software Reference
General Overview

BATTERY 4 - Manual - 29

<!-- page 30 -->

The user interface consists of the following areas:
(1) Application menu bar: The standard application menu bar with file, editing, and viewing
options. See ↑3.2, Application Menu Bar for further information.
(2) Header: The one-stop shop for global settings such as tempo and master output volume.
See ↑3.3, Header for further information.
(3) Sidebar: This is where you browse for Kits and samples, organize BATTERY's Library, and
automate parameters. See ↑3.4, Sidebar for further information.
(4) Cell Matrix: This is the performance section. See ↑3.5, Cell Matrix for further information.
(5) Quick Access area: The most frequently used tools for cell editing in one place. See ↑3.6,
Quick Access Area for further information.
(6) Edit area: Advanced editing, effects, modulation, MIDI features, and routing options are ac-
cessible from this area. See ↑3.7, Edit Area for further information.
3.2
Application Menu Bar

The application menu bar provides access to common file and editing options. You can config-
ure the layout of the Cell Matrix and find your way to BATTERY's documentation resources
from here. It looks slightly different depending on whether you run BATTERY on Windows or
Mac OS.
The application menu bar on Windows.
The application menu bar is not available in plug-in mode, i.e., when you are using BAT-
TERY as a plug-in in a host software application; the audio and MIDI settings will then be
handled by your host software, while all other options can still be accessed from BAT-
TERY's Header section (see also ↑3.3, Header) and other areas of the software.
There are three menus in the application menu bar:
▪
File menu: see ↑3.2.1, File Menu for further information.
▪
Cell Matrix menu: see ↑3.2.2, Cell Matrix Menu for further information.
▪
Help menu: see ↑3.2.3, Help Menu for further information.
Software Reference
Application Menu Bar

BATTERY 4 - Manual - 30

<!-- page 31 -->

3.2.1
File Menu

The File menu provides access to common file-related tasks, and a link to BATTERY's prefer-
ences panel.
The File menu.
The following options are available:
▪
New Kit: Opens a new Kit. (Windows: [Ctrl]+[N] / Mac OS: [Cmd]+[N]).
▪
Open Kit...: Lets you open a BATTERY Kit file from a specific location on your computer.
(Windows: [Ctrl]+[O] / Mac OS: [Cmd]+[O].)
▪
Save Kit: Saves the current Kit under its original name to its original location. (Windows:
[Ctrl]+[S] / Mac OS: [Cmd]+[S].)
▪
Save Kit as...: Lets you save the current Kit under a new name to a specific location on
your computer. (Windows: [Ctrl]+[Shift]+[S] / Mac OS: [Cmd]+ [Shift]+[S].) Furthermore,
there are the following saving options:
◦Patch Only: This option saves the Kit and cell settings along with pointers to where
samples reside on your hard disk. It references samples, but does not include them in
the file, thus, producing a smaller file size than if the samples were included. Select
this option if your file system is unlikely to be changed at a later or point and/or if
your are sure you will not be using the Kit on another computer.
Software Reference
Application Menu Bar

BATTERY 4 - Manual - 31

<!-- page 32 -->

◦Patch and Samples: This option saves the Kit and cell settings, and it lets you specify
a directory into which the samples will be saved. This is a good choice if you want a
transportable patch, e.g., when collaborating with another musician. Specify a sample
folder with the Sample sub-directory menu.
◦Monolith: This option saves the Kit and cell settings and all samples into a single
BATTERY Kit file. This is a good choice if you want a transportable patch, e.g., when
collaborating with another musician.
▪
Preferences...: Launches BATTERY's preferences panel in a new window. Refer to ↑3.8,
Preferences for further information about the preferences panel.
▪
Audio and MIDI Settings...: Launches BATTERY's Audio and MIDI Settings panel in a new
window. Refer to ↑3.9, Audio and MIDI Settings for further information about the Audio
and MIDI Settings panel.
▪
Exit: Shuts down BATTERY. Before shutting down the software, you will be asked if you
wish to save the current Kit.
3.2.2
Cell Matrix Menu

The Edit menu provides access to cell-related tasks, such as copying and pasting cells. Most of
these are also accessible via right-click/[Ctrl]-click on a cell in the Cell Matrix.
The Cell Matrix menu.
The following options are available:
▪
Size: Lets you select a layout preset for the Cell Matrix.
▪
Add Row: Adds a row at the bottom of the Cell Matrix.
▪
Delete Row: Removes a row from the bottom of the Cell Matrix.
Software Reference
Application Menu Bar

BATTERY 4 - Manual - 32

<!-- page 33 -->

▪
Add Column: Adds a column on the right side of the Cell Matrix.
▪
Delete Column: Removes a column from the right side of the Cell Matrix.
3.2.3
Help Menu

The Help menu provides access to BATTERY's documentation and other sources of informa-
tion.
The Help menu.
The following options are available:
▪
Launch Service Center: Launches the Service Center application in a new window. From
there, you can manage your NI software licenses, and download software and documenta-
tion updates.
▪
Open Manual: Opens a submenu with links to various documentation items.
▪
Visit Battery 4 on the web: Opens the BATTERY 4 product homepage in your standard
web browser.
▪
Visit the Knowledge Base: Opens the NI Knowledge Base in your standard web browser.
▪
About...: Launches the About splash screen with version and software licensing informa-
tion. The software credits are also displayed here. Click on the About splash screen again
to close it.
Software Reference
Application Menu Bar

BATTERY 4 - Manual - 33

<!-- page 34 -->

3.3
Header

The Header is BATTERY's control area and tool box for global operations such as Kit manage-
ment, adjusting master levels, tempo, and polyphony/voicing management. It also provides ac-
cess to file, editing, and layout options.
BATTERY's Header.
The controls are:
(1) BATTERY logo: Click on the logo to launch the About splash screen with version and soft-
ware licensing information. The software credits are also displayed here. Click on the About
splash screen again to close it.
(2) Sidebar button: Toggles the visibility of the Sidebar. (For further information about the
Sidebar, refer to ↑3.4, Sidebar).
(3) Application menu button: The application menu button provides access to file, editing, and
layout options (such as the application menu bar, see also ↑3.2, Application Menu Bar), and
links to BATTERY's documentation resources.
The options are:
▪
File: Standard file options and an entry for accessing the preferences panel.
◦New Kit: Opens a new Kit. (Windows: [Ctrl]+[N] / Mac OS: [Cmd]+[N].)
◦Open Kit...: Lets you open a BATTERY Kit file from a specific location on your com-
puter. (Windows: [Ctrl]+[O] / Mac OS: [Cmd]+[O].)
◦Save Kit: Saves the current Kit under its original name to its original location. (Win-
dows: [Ctrl]+[S] / Mac OS: [Cmd]+[S].)
Software Reference
Header

BATTERY 4 - Manual - 34

<!-- page 35 -->

◦Save Kit as...: Lets you save the current Kit under a new name to a specific location
on your computer. (Windows: [Ctrl]+[Shift]+[S] / Mac OS: [Cmd]+ [Shift]+[S].) The
subsequent saving dialog presents you with additional options for saving a Kit. See
↑3.2.1, File Menu for further information.
◦Preferences...: Launches BATTERY's preferences panel in a new window. Refer to
↑3.8, Preferences for further information about the preferences panel.
◦Audio and MIDI Settings...: Launches BATTERY's Audio and MIDI Settings panel in a
new window. Refer to ↑3.9, Audio and MIDI Settings for further information about the
preferences panel.
▪
Cell Matrix: Change the layout of the Cell Matrix with the following menu entries:
◦Size: Lets you select a layout preset for the Cell Matrix.
◦Add Row: Adds a row at the bottom of the Cell Matrix.
◦Delete Row: Removes a row from the bottom of the Cell Matrix.
◦Add Column: Adds a column on the right side of the Cell Matrix.
◦Delete Column: Removes a column from the right side of the Cell Matrix.
▪
Help: This menu provides links to documentation and other sources of information:
◦Launch Service Center: Launches the Service Center application in a new window.
From there, you can manage your NI software licenses, and download software and
documentation updates.
◦Open Manual: Opens a submenu with links to various documentation items.
◦Visit Battery 4 on the web: Opens the BATTERY 4 product homepage in your standard
web browser.
◦Visit the Knowledge Base: Opens the NI Knowledge Base in your standard web brows-
er.
◦About...: Launches the About splash screen with version and software licensing infor-
mation. The software credits are also displayed here. Click on the About splash screen
again to close it.
(4) Kit menu: Displays the name of the currently loaded Kit. The adjacent arrow buttons allow
you to quickly load Kits into BATTERY; this works in two different ways:
Software Reference
Header

BATTERY 4 - Manual - 35

<!-- page 36 -->

▪
In case the current Kit was loaded via the File Browser (see also ↑3.4.2, Files Browser) or
per drag-and-drop, clicking on the arrow buttons will load the next/previous Kit located in
the current Kit's folder.
▪
If the current Kit was loaded via the Library Browser (see also ↑3.4.1, Library Browser),
clicking on the arrow buttons will load the next/previous Kit located in the relevant Library
folder, taking into account the tags you have used to narrow down your selection when
loading the current Kit.
(5) Tempo display/control and Sync button: The Sync button synchronizes the internal clock to
the tempo of a host software application when using BATTERY as a plug-in. When the Sync
button is disabled, BATTERY follows its own tempo; i.e., when you use audio files that contain
embedded timing information (such as REX loops, ACID wav files, and Apple Loop files), the
loop will play back at the tempo set with the tempo control. The tempo display provides three
input methods for setting the tempo: clicking and dragging the tempo; double-clicking and
typing in the value; tapping on the BPM label repeatedly (the label then displays TAP, and acts
as a tap tempo button).
(6) Selection Follows MIDI Input button: With this option enabled, BATTERY switches cell fo-
cus automatically upon receiving MIDI notes. In other words, when you hit a key on your key-
board, not only will the relevant cell be triggered, but the cell focus will also switch to the cell,
and the cell's content will be accessible in the Quick Access area (see also ↑3.6, Quick Access
Area).
(7) Voice monitor/control: Displays the number of currently active voices on the left side, and
the voice limit (maximum number of voices allowed) on the right side. Click and drag the num-
ber on the right side to change the voice limit. This setting will be saved with the Kit.
(8) CPU meter: Monitors BATTERY's CPU usage.
(9) Panic button: Click this button to reset BATTERY's audio engine. This will stop all audio
from playing immediately.
(10) Output level meters / slider: The output level meters display the levels of BATTERY's out-
puts. The slider on top controls the overall levels of all output section channels. To avoid dis-
tortion, you should prevent the meters from going into the red. This setting is not saved with a
Kit; however, it is saved when using BATTERY as a plug-in in a session with a host software,
and will be recalled the next time you load that session.
Software Reference
Header

BATTERY 4 - Manual - 36

<!-- page 37 -->

3.4
Sidebar

The Sidebar contains the Library Browser, the File Browser, and the Automation page:
▪
The Library Browser lets you search for sounds and Kits in BATTERY's Library, and cate-
gorize and organize your samples and Kits (refer to ↑3.4.1, Library Browser for further in-
formation).
▪
The Files Browser lets you search your computer's file structure for sound files and Kits.
You can bookmark your favorite locations and import files to BATTERY's Library from the
Files browser (refer to ↑3.4.2, Files Browser for further information).
▪
The Automation page lets you assign BATTERY's parameter controls to MIDI controllers
and to automation controls in a host software (refer to ↑3.4.3, Automation Page for fur-
ther information).
You can toggle the visibility of the Sidebar on/off with the Sidebar button in the Header.
See also ↑3.3, Header.
3.4.1
Library Browser

The Library Browser provides access to BATTERY's extensive sound library — you can catego-
rize and organize your sound files and Kits from here.
Software Reference
Sidebar

BATTERY 4 - Manual - 37

<!-- page 38 -->

The Library Browser in the Sidebar.
These are the controls:
(1) Kits button and Samples button:
▪
The Kits button lists all BATTERY Kits available in the Library. Narrow down your selec-
tion with the tags in the Category window, and select whether to display factory kits or
your own user Kits with the Factory/User button, respectively.
Software Reference
Sidebar

BATTERY 4 - Manual - 38

<!-- page 39 -->

▪
The Samples button lists all samples available in the Library. Narrow down your selection
with the tags in the Category window, and select whether to display factory samples or
your own user samples with the Factory/User button, respectively.
(2) Factory button and User button:
▪
The Factory button sets the Selection/Results window to display factory content only.
▪
The User button sets the Selection/Results window to display user content only.
(3) Category window: Provides a two-level tag filter system for narrowing down the selection in
the Selection/Results window below. The second category level appears once a tag in the first
level has been clicked.
(4) Search box: Type in a specific term to narrow down the selection in the Selection/Results
window below.
(5) Selection/Results window: Lists Library content according to your selection.
(6) Loop button (circular arrow symbol): When active, the currently previewed sound will be
continuously looped.
(7) Preview button (speaker symbol): Toggles the previewing function on/off. When active, you
will hear a preview of the sample currently selected in the Browser.
(8) Preview Level meter / Preview Level control slider: Displays the output level of the sample
being currently previewed in the Browser. Use the slider on top to adjust the previewing output
level.
(9) Info button: Displays additional information for the item selected in the Selection/Results
window.
(10) Edit button: Opens the Edit panel, where you can edit category tags and add additional
information to the item selected in the Selection/Results window.
▪
Category button: Edit first-level category tags in the left column and second-level category
tags in the right column.
▪
Properties button: Add additional information to your samples/Kits, and assign a color to
the item's list entry from here.
Software Reference
Sidebar

BATTERY 4 - Manual - 39

<!-- page 40 -->

3.4.2
Files Browser

The Files Browser lets you search your computer's file structure for samples and Kits. You can
bookmark your favorite locations and import files to BATTERY's Library from here.
The Files Browser in the Sidebar.
These are the controls:
Software Reference
Sidebar

BATTERY 4 - Manual - 40

<!-- page 41 -->

(1) Favorites bar: Add locations on your hard drive to the Favorites bar by right-clicking an item
in the Selection/Results window, and selecting the Add to Favorites entry.
(2) Navigation bar: Lets you navigate through your computer's file structure.
▪
Go Up button (upwards pointing arrow symbol): Navigates to the parent folder.
▪
Breadcrumbs navigation bar: Displays the folder hierarchy down to the folder that is cur-
rently open in the Selection/Results window.
▪
Recently visited locations (clock symbol): Opens a list of currently visited locations. Click
on an entry to open it in the Selection/Results window.
(3) Selection/Results window: Displays the folder content of the current folder.
(4) Loop button (circular arrow symbol): When active, the currently previewed sample will be
continuously looped.
(5) Preview button (speaker symbol): Toggles the previewing function on/off. When active, you
will hear a preview of the sample currently selected in the Browser.
(6) Preview Level meter / Preview Level control slider: Monitors the level of the sample being
currently previewed in the Browser. Use the slider on top to adjust the output level.
(7) Info button: Displays additional information for the currently selected item in the Selection/
Results window.
(8) Import button: Allows you to import files from your file system to the Library. See ↑4.1,
Importing Files to the Library for a tutorial on importing samples from your file system to the
Library, and how to use the Library's tagging system to tag the files for convenient use.
3.4.3
Automation Page

The Automation page allows you to assign BATTERY's parameter controls (e.g., the output vol-
ume control knob of a specific effect module in BATTERY) to control elements on a MIDI con-
troller, and to automation control IDs in a host application. These destinations are reflected by
the Automation page's Host and MIDI buttons:
▪
The Host button: Assign BATTERY parameter controls to automation control IDs in a host
application from here. You can then automate the parameter from within your host soft-
ware, e.g., to record volume changes of a specific cell throughout a track.
Software Reference
Sidebar

BATTERY 4 - Manual - 41

<!-- page 42 -->

▪
The MIDI button: Assign BATTERY parameter controls to keys, knobs, faders, wheels, or
any other control element on a MIDI controller from here. You can then control the rele-
vant BATTERY parameter control directly from your MIDI controller. This is what you'll
want when using BATTERY in stand-alone mode.
In a host application (that is, in plug-in mode), you'll also be able to record the MIDI data
as automation to a MIDI track. Some hosts even allow you to configure certain MIDI CC
(control change) numbers to be recorded into a separate automation track instead of the
MIDI track, which basically gives you the same results as automating parameters via the
host's automation control IDs (see Host button above); however, the latter are easier to
edit afterwards.
The Automation page in the Sidebar.
These are the controls:
Software Reference
Sidebar

BATTERY 4 - Manual - 42

<!-- page 43 -->

(1) Host button and MIDI button: These buttons select between the two possible types of pa-
rameter control automation (host automation and MIDI automation).
(2) Control mapping entry: When you click on Add New... (5), a new control mapping entry will
be added to the mapping list.
▪
In case of a host mapping, the entry will be labeled Drag to any Knob or Slider.... You can
then drag and drop the selection cross hair (3) onto a parameter control in the user inter-
face. The relevant parameter control will henceforth be addressable for automation from
within your host application. For further instruction, consult the relevant documentation
of your host application.
▪
In case of a MIDI mapping, the entry will first be labeled Use the Controller you would like
to add..., which means you should turn a knob or move a slider on your MIDI controller.
The entry will subsequently be labeled Drag to any Knob or Slider.... You can then drag
and drop the selection cross hair (3) onto a parameter control in the user interface. The
relevant parameter control will henceforth be assigned to the control element on your
MIDI controller.
Note: If BATTERY does not respond to any movement on your MIDI controller, check if
the controller is activated in the MIDI section of the Audio and MIDI Settings dialog (see
also ↑3.9.2, Routing Page), or in the MIDI settings dialog of your host application.
(3) Selection cross hair: Use the selection cross hair to assign BATTERY's parameter controls
to a control mapping entry via drag-and-drop.
(4) Value control limitation scale: Use this scale to set minimum and maximum values for the
parameter controls being addressed by a MIDI controller or your host software. As an example,
this can be helpful when you want to automate a volume slider with a slider on your MIDI key-
board, but you don't want the volume to exceed a certain level after pulling the slider back up.
(5) Add New... entry: See (2).
3.5
Cell Matrix

The Cell Matrix is the heart of BATTERY, the place where everything performance-related takes
place.
Software Reference
Cell Matrix

BATTERY 4 - Manual - 43

<!-- page 44 -->

A 12x4 Cell Matrix layout.
A few facts about the Cell Matrix that you should be aware of:
▪
The Cell Matrix consists of a flexible number of rows and columns.
▪
It can contain up to 128 cells (16x8).
▪
Each cell can hold up to 128 samples (yes, you can load multiple samples into a cell); in
a cell with multiple sample layers, the samples can either be simply layered (i.e., trigger-
ing the cell plays all sample layers at once) or velocity-switched (i.e., different velocity
levels trigger different samples, e.g., to simulate realistic dynamics; see also ↑3.7.5, Edi-
tor Page for further information on editing layers).
▪
You can group cells for editing by multi-selecting them via [Ctrl]-/[Cmd]-click, or by se-
lecting whole rows or columns of cells with the column (1-16) and row (A-H) buttons.
▪
Each cell has an individual Solo and Mute button, but you can also solo and mute whole
rows or columns. The Solo button and the Mute button are situated in the lower left side
of a cell. The Solo button is the left button, lighting up yellow when activated, the Mute
button is the right one, lighting up red.
▪
When you right-click ([Ctrl]-click on Mac OS) a cell, you will be presented with a context
menu, which provides numerous editing options; you can assign colors to cells, route cells
to various destinations, save and load individual cells or groups of cells etc. Refer to
↑3.5.2, The Cell Context Menu for an overview of the cell context menu.
Software Reference
Cell Matrix

BATTERY 4 - Manual - 44

<!-- page 45 -->

▪
Sample editing tools and frequently used cell controls can be found in the Quick Access
area below the Cell Matrix (see ↑3.6, Quick Access Area for further information).
3.5.1
About Cell States

A cell can be in any of the following states: In Focus, Selected for Editing, Triggered, and No
Samples Loaded. Additionally, there are the following visualizations when the Master page of
the Edit area (see also ↑3.7, Edit Area) is opened: In Focus, Routed to Current Bus, Not Routed to
Current Bus, and Routed to Current Bus's Side-chain.
The states are visualized in the following way:
▪
In Focus: When you click on a cell, it gets highlighted with a colored frame (reflecting the
cell's color as assigned in its context menu). The cell is now In Focus (which means the
Quick Access area and the Edit area display parameters specific to that cell), and it is
Selected for Editing (which means any parameter changes made in the Quick Access area
and the Edit area will affect that cell —.see also ↑3.6, Quick Access Area and ↑3.7, Edit
Area, respectively) Multiple cells can be Selected for Editing (see below), but only one cell
can be In Focus.
▪
Selected For Editing: You can select multiple cells for editing by [Ctrl]-clicking ([Cmd]-
click on Mac OS) them one after another. In this case, only the most recently selected
cell will be In Focus (as described above), while the other cells will only be Selected for
Editing. Cells that are only Selected for Editing have a gray frame instead of a colored one.
All cells that are Selected for Editing will be affected by changes made in the Quick Access
area and the Edit area. (See also ↑3.6, Quick Access Area and ↑3.7, Edit Area.)
▪
Triggered: The cell body lights up.
▪
No Samples Loaded: Only the Cell Matrix background is visible.
When the Master page in the Edit area is opened:
▪
In Focus: When the Master page in the Edit area is open, cells in focus have a gray frame
instead of a colored one. The colored frame is preserved for cells that are routed to the
currently selected bus (see below).
▪
Routed to Current Bus: When clicking on one of the buses, all cells routed to that particular
bus will display a colored frame (reflecting the cells' color as assigned via their context
menus). To route a cell to a bus, simply drag-and-drop the cell onto the bus. (See also
Buses section in ↑3.7.6, Master Page).
Software Reference
Cell Matrix

BATTERY 4 - Manual - 45

<!-- page 46 -->

▪
Not Routed to Current Bus: When clicking on one of the buses, all cells that are not routed
to that particular bus will be dimmed.
▪
Routed to Current Bus's Side-chain: When a cell is used to trigger the Master page's Com-
pressor module in side-chain mode, the cell will display SC in its lower right corner. (See
also the Buses and the Compressor Module sections in ↑3.7.6, Master Page for further in-
formation.)
3.5.2
The Cell Context Menu

The context menu provides various cell-related editing options. To open the context menu:
►
Right-click ([Ctrl]-click on Mac OS) on a cell in the Cell Matrix.
The context menu of a cell.
The following options are available:
▪
Add Sample...: Launches the file browser, where you can navigate through your comput-
er's file structure to select and load a file to the cell. You can also load samples to a cell
via drag-and-drop.
▪
Replace Sample...: Launches the file browser, where you can navigate through your com-
puter's file structure to select a file and replace the cell’s current content with it.
Software Reference
Cell Matrix

BATTERY 4 - Manual - 46

<!-- page 47 -->

▪
Render Cell in Place: Selecting this option will re-sample the cell's content, i.e., the cell's
sample(s) will be replaced with a re-sampled version of itself including any effects and
parameters applied to it. This is a handy tool for sound design, or in case you are running
low on CPU power.
▪
Load Cell...: Launches the file browser, where you can navigate through your computer's
file structure to select a BATTERY Cell file (*.nbcl) and load it to the current cell.
▪
Save Cell...: Launches the file browser, where you can navigate through your computer's
file structure to select a folder to save the Cell to. The Cell will be saved as a BATTERY
Cell file (*.nbcl).
▪
Cut Cell: Cuts the cell including its content and settings.
▪
Copy Cell: Copies the cell to the clipboard.
▪
Paste Cell(s): Pastes the content from the clipboard to the currently selected cell(s).
▪
Delete Cell: Empties the cell and resets all cell parameters to a default setting.
▪
Rename Cell: Lets you rename the selected cell.
▪
Cell Color: Opens a submenu where you can assign a color to the cell.
▪
Output: Select an output destination for the cell from here. Available options are Master
(BATTERY's main output), one of BATTERY's effect/submix Buses 1-4, or any of the Di-
rect Out channels, which let you bypass BATTERY's main output completely, and route,
e.g., directly to a mixer channel in your host software.
3.6
Quick Access Area

The Quick Access area is situated below the Cell Matrix. It provides quick access to the most
frequently used tools for cell editing. The Quick Access area consists of the Waveform Control,
the Sample Picker, and the Quick Access controls.
Software Reference
Quick Access Area

BATTERY 4 - Manual - 47

<!-- page 48 -->

The Quick Access area below the Cell Matrix.
The Quick Access area is present at all times, except for when the Editor page or the Master
page is open (refer to ↑3.7.5, Editor Page and ↑3.7.6, Master Page for further information).
These are the sections and controls:
(1) Waveform Control: Adjust the start and end points of a sample, apply envelopes, quick-load
samples, and select sample layers from the cell for editing:
▪
Sample Start/End markers: Adjust the sample's start and end points by clicking and drag-
ging the start (S) and the end markers (E), respectively.
▪
Volume Envelope overlay: Only visible when the Volume Envelope module on the Main
page is active (refer to ↑3.7.1, Main Page for information on how to adjust the volume
envelope settings).
▪
Pitch Envelope overlay: Only visible when the Pitch Envelope module on the Main page is
active (refer to ↑3.7.1, Main Page for information on how to adjust the volume envelope
settings).
▪
Zooming/scrolling: Click and drag up/down anywhere in the waveform to zoom in/out on
the sample, respectively. Click and drag left/right anywhere in the waveform to scroll left/
right in the sample.
(2) Sample Picker: Displays the name of the currently loaded sample / sample layer. The adja-
cent arrow buttons allow you to quick-load other samples into the cell. This works in two ways:
▪
In case the current sample was loaded via the Files Browser (see also ↑3.4.2, Files Brows-
er) or per drag-and-drop, clicking on the arrow buttons will load the next/previous sample
available in the current sample's folder.
Software Reference
Quick Access Area

BATTERY 4 - Manual - 48

<!-- page 49 -->

▪
If the current sample was loaded via the Library Browser (see also ↑3.4.1, Library Brows-
er), clicking on the arrow buttons will load the next/previous sample available in the Library,
taking into account the tags you have used to narrow down your selection when loading
the current sample.
Whenever there is more than one sample layer in a cell, an additional drop-down menu appears
on the left side of the sample name field. From that menu, you can select the sample layer to
be displayed and edited in the Waveform Control.
Keep in mind that the controls on the right side of the Waveform Control (Tune, Pan etc.)
affect the whole cell, not the individual sample layers! Tuning, panning, and volume set-
tings for individual sample layers can be done from the Editor page (see also ↑3.7.5, Editor
Page).
(3) Quick Access controls: This area controls the basic sonic characteristics, and the MIDI key
assignments of the selected cell(s).
▪
Tune knob: Click and drag this knob to change the pitch of the cell (and all sample layers
contained). The range is three octaves up (turning the knob to the right), and three oc-
taves down (turning the knob to the left). [Shift]-click + drag to finely adjust this parame-
ter.
▪
Reverse button: Click this button to reverse playback for the cell (and all sample layers
contained).
▪
Pan knob: Click and drag this knob to position the cell in the stereo field. [Shift]-click +
drag to finely adjust this parameter.
▪
Level meter/slider: Monitors the cell's output level. Click and drag the slider up/down to
adjust the level. [Shift]-click + drag to finely adjust this parameter.
▪
Key Range control: Determines the MIDI note(s) that trigger the cell. For example, a Key
Range of C2 / C2 means that the cell will play only upon receiving data from MIDI note
C2. If you set it to C1 / E1, then all notes in that range will trigger the cell, i.e., C1, C#1,
D1, D#1, and E1.
You can double-click the field and enter an alphanumeric value, or click the Learn button
(the MIDI symbol button) and press two keys on your keyboard, one after the other. Make
sure the Selection Follows MIDI Input button in the Header (see also ↑3.3, Header) is de-
activated when using the Learn button, otherwise the cell focus will switch to another cell
when pressing a key on your keyboard.
Software Reference
Quick Access Area

BATTERY 4 - Manual - 49

<!-- page 50 -->

▪
Phase Invert button: Inverts the phase of the cell.
▪
L/R Swap button: Swaps the stereo channels of the cell.
3.7
Edit Area

The Edit area is where advanced cell and Kit processing takes place: apply effects and enve-
lopes to cells; edit the triggering behavior of sample layers in a cell; modulate your sounds with
a variety of sources; route cells to various destinations (via buses); and apply master effects.
Take your creativity to the max by manipulating samples with anything from subtle to extreme.
The Edit area with the Main page opened.
The Edit area is organized in themed pages, which you will access by clicking on the relevant
tab in the lower portion of the user interface. The following pages are there:
▪
Main page: see ↑3.7.1, Main Page for further information.
▪
Effects page: see ↑3.7.2, Effects Page for further information.
▪
Modulation page: see ↑3.7.3, Modulation Page for further information.
▪
Setup page: see ↑3.7.4, Setup Page for further information.
▪
Editor page: see ↑3.7.5, Editor Page for further information.
▪
Master page: see ↑3.7.6, Master Page for further information.
Software Reference
Edit Area

BATTERY 4 - Manual - 50

<!-- page 51 -->

3.7.1
Main Page

The Main page holds the basic tools for tinkering with the sound of the individual cells of your
Kit; pitch and volume envelope modules, basic filters, a sample engine selection, a one-knob
compressor, and send controls for delay and reverb effects can be found here.
The Main page in the Edit area.
Refer to the following sections for descriptions of the individual modules on the Main page.
Volume Envelope Module
Apply a volume envelope to the currently active cell from here. You can see the envelope shape
against the waveform in the Waveform Control (see also ↑3.6, Quick Access Area) when hover-
ing over this module.
The Volume Envelope module.
The controls are:
▪
Power button: Activates/deactivates the envelope.
Software Reference
Edit Area

BATTERY 4 - Manual - 51

<!-- page 52 -->

▪
Envelope mode selectors: The two envelope symbols on the right side of the section head-
er let you choose between two basic types of volume envelope: AHDSR (Attack, Hold,
Decay, Sustain, Release), which is represented by the left envelope symbol, and AHD
(Attack, Hold, Decay), which is represented by the right envelope symbol. Typically, the
AHDSR envelope is for sustained samples while the AHD envelope is more for “one-shot”
sample playback. AHD mode disables the Sustain and Release controls below.
▪
Attack knob: Determines the time it takes for the envelope to reach its maximum level.
▪
Hold knob: Determines how long the envelope will remain at its maximum level. Set this
to 10-30ms to add punch to the signal.
▪
Decay knob: Determines the time it takes for the envelope to fall from the hold level to
the sustain level.
▪
Sustain knob: Determines the level that will be maintained in the sustain phase as long as
the incoming MIDI note is held. Sustain control is not available in AHD mode (see enve-
lope mode selectors description above).
▪
Release knob: Determines the time it takes to return to zero level after receiving a MIDI
note-off command (i.e., the MIDI trigger ends). Release control is not available in AHD
mode (see envelope mode selectors description above).
In case you selected multiple cells before activating the envelope, the most recently select-
ed cell (with a colored frame) will be displayed in the Waveform Control; however, all se-
lected cells (those with a gray frame) will be affected by the envelope settings.
Pitch Envelope Module
Apply a pitch envelope to the currently active cell from here. You can see the envelope shape
against the waveform in the Waveform Control when hovering over this module.
The Pitch Envelope module.
The controls are:
Software Reference
Edit Area

BATTERY 4 - Manual - 52

<!-- page 53 -->

▪
Power button: Activates/deactivates the envelope.
▪
Envelope mode selectors: The two envelope symbols on the right side of the section head-
er let you choose between two types of pitch envelope: standard mode (with Amount, De-
cay 1, Break, and Decay 2 controls), which is represented by the left envelope symbol,
and easy mode (with only an Amount, and a Decay control), which is represented by the
right envelope symbol.
▪
Amount knob: Sets the degree to which the envelope affects pitch.
▪
Decay 1 knob: Edits the time for the envelope to go from its initial level (as set with the
Amount control) to the level set with the Break knob.
▪
Break knob: This control adjusts the point where the envelope breaks, i.e., the min/max
value from where it moves back towards zero (the pitch can be either higher or lower than
the cell's normal pitch).
▪
Decay 2 knob: This determines how long it takes for the level set with the Break knob to
decay back to zero again.
In case you selected multiple cells before activating the envelope, the most recently select-
ed cell (with a red frame) will be displayed in the Waveform Control; however, all selected
cells (those with a gray frame) will be affected by the envelope settings.
Velocity Module
Lets you adjust how much the input velocity will affect the volume and pitch of the triggered
cell(s).
The Velocity module.
Software Reference
Edit Area

BATTERY 4 - Manual - 53

<!-- page 54 -->

The controls are:
▪
To Volume knob: When set to 0 %, velocity will not affect the volume of the triggered cell,
i.e., no matter how hard you hit the key or pad, the output volume will always be 100% of
the cell's volume setting. Turning the knob all the way to the right will translate the input
velocity to a percentage of the cell’s volume level (with an underlying minimum value of -
inf dB).
▪
To Pitch knob: When set to 0 st., velocity will not affect the pitch of the triggered cell,
i.e., no matter how hard you hit the key or pad, the cell will always play at its original
pitch. Turning the knob to the right will translate the input velocity to semitones (with an
underlying minimum value of 0 st., and a maximum value of +12 st.)
Engine Module
The engine module allows you to select between two basic sampler engine modes: Sampler
mode and Stretch mode. The former has an additional submode that emulates the sound of
two legendary hardware samplers. An additional mode, Beat mode, is available for samples
containing timing information, such as REX files, ACID wav files, and Apple Loop files.
The Engine module.
The controls are:
▪
Sampler: In Sampler mode, BATTERY stores sample data in the system memory, reads it
out from memory, and applies any needed pitch-shifting by re-sampling the audio data.
◦Standard button: Activates BATTERY's standard sampler engine.
Software Reference
Edit Area

BATTERY 4 - Manual - 54

<!-- page 55 -->

◦Vintage button: Activates vintage interpolation modes, which emulate the sonic char-
acteristics of two legendary samplers often used in Hip Hop and electronic music.
With Vintage mode active, you can select one of the sampler emulations from the
drop-down menu below.
▪
Stretch: In Stretch mode, BATTERY uses granular synthesis to alter sample speed while
preserving the original pitch information.
◦Standard button: Activates BATTERY's standard stretch engine, with individual Grain
control (determines the size of the sound particles used for resynthesis); Speed con-
trol (changes the playback rate independently of pitch; the length values are ex-
pressed as percentage, e.g., 100% plays back the sound at the original speed, 200%
doubles the speed, 50% halves the speed etc.; a value of 0 stops playback entirely
and freezes the sound), and Smooth control (adjusts the amount of granular micro-en-
velopes to reduce unwanted artifacts, thus, altering the sonic character of the re-syn-
thesis process; note that small values generally cause a buzzier sound).
◦Pro button: Activates BATTERY's Pro stretch engine. Use the Speed control to change
the length of the sample(s). The length values are expressed as percentage of the orig-
inal length.
▪
Beat: When you load a sample containing timing information (such as a REX file, an ACID
wav file, or an Apple Loop file) into a cell in BATTERY, the Engine module will automati-
cally be set to Beat mode. The individual slices of the sample will play back at the speed
determined by the module's controls, or synchronized to BATTERY's internal clock (or that
of your host application), depending on the module's settings in its Sync menu. These are
the controls:
◦Expand button: Click this button to expand the individual slices of the sample to indi-
vidual cells in BATTERY, starting with the next empty cell. In BATTERY's preferences
(see also ↑3.8.4, Loading Page), there is also a setting to make this the default behav-
ior.
◦Sync menu: Selecting Sync Off uncouples the sample from BATTERY's internal tem-
po, or that of your host software. Selecting one of the note values synchronizes the
sample's slices to the beats of BATTERY's internal clock (or that of your host soft-
ware).
◦Speed button: The Speed knob alters the sample’s playback speed without altering its
pitch.
Software Reference
Edit Area

BATTERY 4 - Manual - 55

<!-- page 56 -->

◦Smooth button: Adjusts the attack and release of the individual slices to prevent
clicks.
Filter Module
A simple high-pass / low-pass filter to be applied to the selected cell(s).
The Filter module.
The controls are:
▪
Power button: Activates/deactivates the filter.
▪
High Cut handle: Sets the frequency above which the signal will be attenuated.
▪
Low Cut handle: Sets the frequency below which the signal will be attenuated.
Compressor Module
A one-knob control feedback compressor to smooth out the audio signal.
Software Reference
Edit Area

BATTERY 4 - Manual - 56

<!-- page 57 -->

The Compressor module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
VU meter: Displays the amount of gain reduction in real-time.
▪
Amount knob: Adjusts the amount of compression.
Sends Module
Contains two knobs that control the amount of the signal to be sent to the delay and reverb
units in the Master page (see also ↑3.7.6, Master Page).
The Sends module.
The controls are:
Software Reference
Edit Area

BATTERY 4 - Manual - 57

<!-- page 58 -->

▪
Delay knob: Determines the amount of signal to be sent to the Delay module on the Mas-
ter page.
▪
Reverb knob: Determines the amount of signal to be sent to the Reverb module on the
Master page.
Refer to ↑3.7.6, Master Page for instructions on adjusting the delay and the reverb module.
3.7.2
Effects Page

The Effects page is where you can apply effects to a cell’s audio output to enhance its sonic
richness or make it blend in with the mix.
The Effects page in the Edit area.
Refer to the following sections for descriptions of the individual modules on the Effects page.
For information on effect presets, see ↑2.3.1, Effect Presets.
Saturation Module
The Saturation module provides expansion/compression/saturation effects for the selected
cell(s). Unlike a standard audio compressor/expander, saturation works on individual sample
bits, not the overall sound. Therefore it can greatly alter the sound of even the shortest sam-
ples.
Software Reference
Edit Area

BATTERY 4 - Manual - 58

<!-- page 59 -->

The Saturation module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Saturation module comes with
the following factory presets:
◦Classic: Classic Distortion
◦Drums: Cranked, Dirty Kick
◦Tape: Aggressive Tape, Warm Tape
▪
Saturation type selection menu: Provides you with three basic types of saturation: Classic,
Drums, and Tape.
▪
Gain knob: Controls the input gain of the effect. This will increase the amount of tape dis-
tortion and compression.
▪
Warmth knob: Controls the low frequency boost/cut of the effect. (Only available in Tape
saturation mode.)
▪
HF knob: Controls the high frequency roll-off starting frequency. Frequencies above this
point will be attenuated. (Only available in Tape saturation mode.)
▪
Output knob: Controls the output gain of the effect.
Software Reference
Edit Area

BATTERY 4 - Manual - 59

<!-- page 60 -->

LoFi Module
The Lo-fi module decreases the quality of the audio signal by lowering the resolution or sample
rate, and by adding noise and coloration to it.
The LoFi module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The LoFi module comes with the fol-
lowing factory presets:
◦8bit Lofi
◦Crackle
◦Dark Bitcrusher
◦Noizy
◦Oldschool
▪
Bits knob: Re-quantizes the signal to an adjustable bit depth. Fractional bit levels (such
as 12.4 bits) are possible and can add considerable grit. Audio CDs have a quantization
depth of 16 bits, old samplers frequently used 8 or 12 bits, and 4 bits evoke memories of
countless irritating children’s toys.
Software Reference
Edit Area

BATTERY 4 - Manual - 60

<!-- page 61 -->

▪
Hertz knob: Re-samples the signal to an adjustable sample rate. The re-sampling is done
without any kind of (usually mandatory) low-pass filtering, which causes all kinds of won-
derful aliasing artifacts. The sample rate goes all the way down to 50 Hz, which will not
leave much of the original signal.
▪
Noise knob: Adds hiss to the audio signal.
▪
Color knob: Adjusts the frequency characteristic of the noise and acts as a low-pass filter.
▪
Output knob: Adjusts the module’s output level.
Filter / EQ Module
The Filter / EQ module changes the frequency characteristics of the signal (cell) passing
through it in various ways. A filter is basically a special kind of amplifier that changes gain on-
ly at specific frequencies of the signal, either boosting or cutting those.
The Filter / EQ module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Filter / EQ module comes with
the following factory presets:
◦Solid G-EQ: Solid G-EQ Loudness
◦3-Band EQ: 3-Band EQ Kick Fattener, 3-Band EQ Telephone Setting
◦Lowpass: 4 Pole Lowpass
Software Reference
Edit Area

BATTERY 4 - Manual - 61

<!-- page 62 -->

◦Highpass: 2 Pole Highpass
◦Bandpass: 4 Pole Bandpass
◦Peak/Notch: Notch Filter
◦Effect: Formant Filter
▪
Filter / EQ type selection menu: There are several filter modes available from the selection
menu, which all affect the sound differently:
◦Solid G-EQ: The Solid G-EQ is modeled on high-quality analog circuitry. It is a 4-band
parametric EQ.
The adjustable filter bands are: L (low frequency band); LM (low-mid frequency band);
HM (high-mid frequency band); and H (high frequency band). They can be selected
with the tab buttons above the controls.
The available controls are: Freq (adjusts the center frequency of the frequency band,
at which the boost or cut will occur); Bell button (toggles the bell shape of the fre-
quency band — only available for L and H bands); Q (as it were, a bandwidth control
— only available for LM and HM); Gain (adjusts the amount of boost or cut at the fre-
quency band); Output (adjusts the module’s output level).
◦3-band EQ: This is a classic 3-band EQ. Each of the three bands has three parameter
knobs: Freq (adjusts the center frequency of the frequency band, at which the boost
or cut will occur), BW (adjusts the range of frequencies over which boosting or cutting
occurs, from narrow to broad), and the Gain (controls the amplitude increase after the
filter, which can be used to compensate for amplitude reduction due to the filter, or to
increase the soft saturation of the effect).
◦Lowpass: This mode contains filters which attenuate signals above the cutoff frequen-
cy, allowing low frequency signals to pass through; hence, the name lowpass.
The available filters are: Ldr 1P (1-pole lowpass which attenuates frequencies above
the cutoff at a rate of -6 dB/octave); Ldr 2P (2-pole lowpass, which attenuates fre-
quencies above the cutoff at a rate of -12 dB/octave); Ldr 4P (4-pole lowpass which
attenuates frequencies above the cutoff at a rate of -24 dB/octave); and Daft (a more
aggressive 2-pole lowpass filter which attenuates frequencies above the cutoff at a
rate of -12 dB/octave). They can be selected with the tab buttons above the controls.
The following controls are available per filter: Cutoff (adjusts the frequency above
which signals will be attenuated.); Reso (with a value greater than 0, this control will
Software Reference
Edit Area

BATTERY 4 - Manual - 62

<!-- page 63 -->

boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect).
◦Highpass: This mode contains filters that attenuate signals below the cutoff frequen-
cy, allowing high frequency signals to pass through, hence, the name highpass.
The available filters are: Ldr 1P (1-pole highpass which attenuates frequencies below
the cutoff at a rate of -6 dB/octave); Ldr 2P (2-pole highpass which attenuates fre-
quencies below the cutoff at a rate of -12 dB/octave); Ldr 4P (4-pole highpass which
attenuates frequencies below the cutoff at a rate of -24 dB/octave); and Daft (a more
aggressive 2-pole highpass filter which attenuates frequencies below the cutoff at a
rate of -12 dB/octave). They can be selected with the tab buttons above the controls.
The following controls are available per filter: Cutoff (adjusts the frequency below
which signals will be attenuated); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect).
◦Bandpass: This mode attenuates signals above and below the cutoff frequency (or
more correctly, the resonant frequency).
The available filters are: Ldr 2P (ladder circuit 2-pole bandpass which attenuates fre-
quencies above and below the cutoff at a rate of -12 dB/octave); Ldr 4P (ladder cir-
cuit 4-pole bandpass which attenuates frequencies above and below the cutoff at a
rate of -24 dB/octave); SV 2P (clean 2-pole bandpass which attenuates frequencies
above and below the cutoff at a rate of -12 dB/octave); and SV 4P (clean 4-pole band-
pass which attenuates frequencies above and below the cutoff at a rate of -24 dB/oc-
tave). They can be selected with the tab buttons above the filter controls.
The following controls are available per filter: Cutoff (adjusts the frequency below
which signals will be attenuated); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect).
◦Peak/Notch: A notch filter removes a specific frequency band from the signal. It can
be thought of as the inverse of a bandpass filter — in fact, it is sometimes referred to
as a "band reject" filter. A peak filter, on the other hand, is quite different - it simply
adds a resonant peak to the signal, without doing much attenuation to the signal.
The available filters are: Ldr Peak (unique filter that accents frequencies at the cut-
Software Reference
Edit Area

BATTERY 4 - Manual - 63

<!-- page 64 -->

off); Ldr Notch (cuts two narrow bands of frequencies at either side of the cutoff); SV
Notch (clean 4-pole notch filter which attenuates frequencies at the cutoff); and SV
BR (band reject filter, which attenuates frequencies at the cutoff). They can be select-
ed with the tab buttons above the filter controls.
The following controls are available per filter: Cutoff (adjusts the frequency below
which signals will be attenuated); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect — this one is
only available for Ldr Peak and Ldr Notch).
◦Effect: Filters in this category don’t match any of the traditional filter characteristics,
and are suited for special effects.
The available filters are: Frm 1 (a formant filter, designed to mimic the frequency re-
sponse of the human vocal tract, which can be used to emulate the talk box effect);
Frm 2 (a formant filter with slightly different characteristics compared to Frm 1, de-
signed to mimic the frequency response of the human vocal tract — it can also be
used to emulate the talk box effect); Vow A (vowel filter that simulates the resonant
frequencies of the human vocal tract); Vow B (vowel filter that simulates the resonant
frequencies of the human vocal tract, like Vow A but with slightly different character-
istics); and Phaser (creates a distinct comb filter effect by using an allpass filter de-
sign that radically alters the phase relations in your signal). They can be selected with
the tab buttons above the filter controls.
The following controls are available for the vowel filters and the phaser: Cutoff (ad-
justs the frequency below which signals will be attenuated); and Reso (with a value
greater than 0, this control will boost a small frequency range around the cutoff fre-
quency).
The formant filters have the following controls: Talk (controls the frequency response
of the filter, which can be used to morph between vowel sounds); and Sharp (increas-
es and decreases the peaks and notches in the response, analogous to the resonance
control of the other filters); Size (controls the center of the frequency response, analo-
gous to the cutoff control of the other filters).
Filters require a fair amount of CPU power, so make sure they are turned off when not
needed.
Software Reference
Edit Area

BATTERY 4 - Manual - 64

<!-- page 65 -->

Compressor Module
Add punch and control dynamics with the compressor module. Compression is a signal proc-
essing technique that is commonly used in recording. It reduces peaks and raises low-level sig-
nals to produce a higher average signal level.
The Compressor module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Compressor module comes with
the following factory presets:
◦Pro: Slammed
◦Solid Bus: Drum Bus, Master Setting, Nice and Punchy, Parallel Compression
▪
Compressor mode selection menu: Lets you select one of the three available compressor
modes Solid Bus Comp, Classic, and Pro.
▪
Thresh knob: Sets the level above which compression begins. E.g., with a threshold of
-10dB, signals below that level will be relatively unaffected, but signals above that level
will be attenuated. The degree of attenuation is set with the Ratio knob.
▪
Ratio knob: Indicates the ratio of input-signal-to-output-signal once a signal exceeds the
threshold. E.g., a ratio of 3:1 means that if a signal is above the threshold, a 3dB in-
crease in input level yields only a 1dB increase in output level.
Software Reference
Edit Area

BATTERY 4 - Manual - 65

<!-- page 66 -->

▪
Attack knob: Determines how long it takes for the compression effect to kick in once the
input signal exceeds the threshold. The higher the value, the more percussive the effect,
with the tradeoff being higher peak levels. Lower values result in a more squashed sound,
but keep peaks to a minimum.
▪
Release knob: Sets how long it takes for the compressor gain to return to normal after the
input signal has gone below the threshold.
▪
Makeup knob: The Makeup knob is only available in Solid Bus Comp mode. It lets you
compensate for the gain reduction during compression. This only affects the processed
signal, so if you turn the Mix knob all the way left (see below), you will hear no difference.
▪
Mix knob: The Mix knob is only available in Solid Bus Comp mode. It lets you adjust the
ratio between mixed and original signal. In other words, if you turn the knob all the way to
the left, you will hear the signal as if the compressor was being bypassed; however, the
Output knob (see below) will still affect the overall output level of the signal. Setting the
knob all the way right, you will hear only the processed signal.
▪
Output knob: Adjusts the output level of the module.
Mysterious compression increases: If it seems like there’s been a sudden increase in com-
pression without increasing the compression amount, the input signal going to the com-
pressor may have increased.
Compression requires a fair amount of CPU power, so make sure the module is turned off
when not needed.
TM (Transient Master) Module
The Transient Master is an easy to use compressor, designed to control the attack and sustain
of a sound. Instead of following the amplitude of the sound like a traditional compressor, it
follows the general envelope and is not as susceptible to changes of input gain. It is best used
on sounds with fast attacks, like percussion, pianos or guitars. The Transient Master can also
be quite extreme in some cases, so use it with caution.
Software Reference
Edit Area

BATTERY 4 - Manual - 66

<!-- page 67 -->

The TM module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The TM module comes with the fol-
lowing factory presets:
◦British Setting
◦No Attack
◦Room Remover
◦Snare Enhancer
◦Tight Kick
▪
Attack knob: Controls the scaling of the attack portion of the input signal’s volume enve-
lope. Increasing this parameter will add more punch and decreasing it will reduce sharp
attacks.
▪
Sustain knob: Controls the scaling of the sustain portion of the input signal’s volume en-
velope. Increasing this parameter will add more body to the sound and decreasing it will
reduce the sound’s tail.
▪
Input knob: Controls the input gain to the effect.
▪
Output knob: Controls the output gain after the effect. For dynamic effects like compres-
sors, this is very important.
Software Reference
Edit Area

BATTERY 4 - Manual - 67

<!-- page 68 -->

3.7.3
Modulation Page

The Modulation page allows you to modulate your sound with a variety of sources, including
LFOs (Low Frequency Oscillators), envelopes, aftertouch, and external MIDI controllers.
The Modulation page in the Edit area.
This can not only add dynamics and color to a patch, but in conjunction with a software se-
quencer host, it can automate functions that add dramatic, real-time changes. Since these
modulation sources can also be MIDI controllers, it’s possible to feed signals from external
hardware MIDI fader boxes and manipulate the sound as a real-time performance. If you record
these signals in a sequencer, you can have the best of both worlds: real-time improvisation and
signal warping, recorded as automation data for later playback.
Refer to the following sections for descriptions of the individual modules on the Modulation
page.
LFO 1 and LFO 2 Modules
The LFOs (Low Frequency Oscillators) provide a periodic modulation effect.
The LFO modules.
Software Reference
Edit Area

BATTERY 4 - Manual - 68

<!-- page 69 -->

The controls are:
▪
Waveform selection menu: Choose from sine, saw, pulse, or random waveform here.
▪
Sync selection menu: This syncs the frequency to BATTERY's internal tempo, or to your
host's tempo when using BATTERY as a plug-in in sync mode (see also "Tempo display/
control and Sync button" in ↑3.3, Header). In the latter case, the Frequency (Freq.) knob
indicates note values rather than an absolute rate.
▪
Retrigger button: When enabled, the LFO cycle is retriggered on each incoming note.
▪
Freq knob: Varies the LFO modulation rate.
▪
Attack knob: Sets the time over which the LFO signal fades in after triggering.
▪
PW knob: The pulse width knob changes the waveform’s duty cycle. For example, it can
continuously vary the square waveform’s width.
Modulation Envelope Module
The envelope adds a modulation signal that varies over time in a non-periodic way.
The Modulation Envelope module.
The controls are:
▪
Envelope mode selection menu: The two envelope symbols on the right side of the module
header let you choose between two basic types of volume envelopes:
◦AHDSR (left): An AHDSR (Attack, Hold, Decay, Sustain, Release) envelope. Typically
the AHDSR envelope is for samples with a significant sustain time (especially when
played from a MIDI keyboard).
◦AHD (right): A simple AHD (Attack, Hold, Decay) envelope. This envelope is well suit-
ed for one-shot sample playback.
▪
Curve knob: Sets the shape of the envelope curves from concave, to linear (0), to convex.
Software Reference
Edit Area

BATTERY 4 - Manual - 69

<!-- page 70 -->

▪
Attack knob: Determines the time it takes for the envelope to reach its maximum level.
▪
Hold knob: Determines how long the envelope will remain at its maximum level. Set this
to 10-30ms to add punch to a signal.
▪
Decay knob: Determines the time it takes for the envelope to fall from the held level to
the sustain level.
▪
Sustain knob: Determines the level that will be maintained in the sustain phase as long as
the incoming MIDI note is held. Sustain control is not available in AHD mode.
▪
Release knob: Determines the time it takes to return to zero level after receiving a MIDI
note-off command (i.e., the MIDI trigger ends). Release control is not available in AHD
mode.
Modulation Slots Module
This module provides up to eight modulation paths on two pages (1 - 4 and 5 - 8), each select-
ed by a corresponding drop-down menu.
The Modulation Slots module.
A modulation path consists of a modulation source and a modulation destination. The amount
slider determines the amount of modulation.
Please note that certain modulation sources cannot be routed to certain targets. These tar-
gets will not be available as an option from the corresponding modulation destination se-
lection menu on the right side.
The controls are:
Software Reference
Edit Area

BATTERY 4 - Manual - 70

<!-- page 71 -->

▪
Modulation Source selection menu: Selects the modulation source. Available modulation
sources are:
◦None (no modulation)
◦Velocity
◦Pitchbend
◦Poly AfterTouch (polyphonic aftertouch)
◦Mono AfterTouch (monophonic channel aftertouch)
◦Key Position
◦MIDI CC (MIDI controllers)
◦Random Unipolar
◦Random Bipolar
◦Constant
◦Release Velocity
◦LFO1
◦LFO2
◦Modulation Envelope
◦Volume Envelope
◦Pitch Envelope
▪
Inv. button: Changes the amount of the Modulation Amount slider into a negative value.
▪
Modulation Amount slider: Determines the depth of the effect on the modulation destina-
tion. The range is from 0% to 100%. If any combination of modulations exceeds an effect
level of 100%, the value will be limited to the maximum value.
▪
Modulation Destination selection menu: Selects the modulation destination. Available
modulation destinations are:
◦None
◦Volume
Software Reference
Edit Area

BATTERY 4 - Manual - 71

<!-- page 72 -->

◦Pan
◦Tune
◦Saturation
◦Lo-Fi: Bits, Hertz, Noise Level.
◦Solid G-EQ: L Frequency, L Gain, LM Frequency, LM Q, LM Gain, HM Frequency, HM
Q, HM Gain, H Frequency, H Gain.
◦3-Band EQ: Band 1 Frequency, Band 1 Bandwidth, Band 1 Gain, Band 2 Frequency,
Band 2 Bandwidth, Band 2 Gain, Band 3 Frequency, Band 3 Bandwidth, Band 3
Gain.
◦Filter: Cutoff, Resonance.
◦Formant Filter: Talk, Sharp, Size.
◦LFO 1: Frequency, Intensity Multiply, Intensity Add.
◦LFO 2: Frequency, Intensity Multiply, Intensity Add.
◦Modulation Envelope: Attack, Hold, Decay, Sustain, Release, Intensity Multiply, Inten-
sity Add.
◦Volume Envelope: Attack, Hold, Decay, Sustain, Release, Intensity Multiply, Intensity
Add.
◦Pitch Envelope: Decay 1, Break, Decay 2.
◦Sample Start
◦Loop Start
◦Loop Length
If for some reason the modulation intensity is not sufficient, you can route several modula-
tion strips to one destination!
Software Reference
Edit Area

BATTERY 4 - Manual - 72

<!-- page 73 -->

3.7.4
Setup Page

The Setup page provides tools specifically designed for drum playing and programming. You
can use them to fine-tune cells/Kits, or create totally new sounds out of the existing library
content. All effects/parameters are cell-based, which means that each cell can have totally dif-
ferent settings.
The Setup page in the Edit area.
Refer to the following sections for descriptions of the individual modules on the Setup page.
MIDI Input Module
The MIDI Input module lets you customize the MIDI channel and velocity response of cells,
and change their trigger behavior.
The MIDI Input module.
Software Reference
Edit Area

BATTERY 4 - Manual - 73

<!-- page 74 -->

The controls are:
▪
Curve: Use the handles to adjust the velocity curve for a cell.
▪
MIDI channel drop-down menu: Specify whether a cell should receive data from all MIDI
channels, or only a specific MIDI channel with this menu.
▪
Key Track button: When activated (lit) and the key range exceeds one note (see also "Key
Range control" in ↑3.6, Quick Access Area), all samples in the current cell will change
pitch in response to the MIDI input. E.g., if the key range is C1-D1 and you play D1 with
Key Track on, the pitch will be two semitones higher than if you had played C1. When
disabled, the cell's pitch will be determined solely by its root key and the Tune knob (see
also ↑3.6, Quick Access Area).
▪
Note Latch button: Activate this button to “latch” incoming notes, i.e., play a note to trig-
ger the sample, play the note again to stop it.
Voice Groups Module
The Voice Groups module allows you to create virtual groups with limited voices. This can be
useful when, e.g., simulating a real drum set, where an open and a closed hi-hat would never
occur at the same time; you'd assign both cells to a voice group and set the Voices setting to
1, which would allow only one of the cells in the voice group to play at a time. But there can
be a number of creative reasons for using voice groups.
The Voice Groups module.
The controls are:
▪
Voice group selection menu: Assign a cell to either no voice group (this is the default Kit
setting), or to any of the 128 available voice groups from here. Use the pencil button to
rename a voice group for more transparency.
▪
Voices display: Set the number of voices allowed for the given voice group (1 to 127) with
this control.
Software Reference
Edit Area

BATTERY 4 - Manual - 74

<!-- page 75 -->

▪
Mode menu: Select a mode to decide which notes to "steal" if the voice group runs out of
voices. You can choose from: Kill Any (any note is removed); Kill Oldest (the earliest note
played is removed); Kill Newest (the last note played is removed); Kill Highest (the high-
est note played is removed); or Kill Lowest (the lowest note is removed). E.g., if the voice
group allows for three simultaneous voices, and you play four notes in a row, the first note
will be muted in order for the fourth note to be audible when you set the Mode to Kill
Oldest.
▪
Fade (ms) display: This sets the time that voices overlap before cutting each other off
completely (i.e., the previously played voice sustains for a while even after a new voice
has been triggered). This prevents an overly abrupt transition between voices. Available
settings are 0 to 999 milliseconds.
▪
Excl menu: This is an advanced programming feature that allows for even more complex
muting schemes; assign multiple voice groups to an exclude group to make the assigned
groups mute each other.
You could assign a “silent” sample (no sound) to a group so that triggering this cell turns
off any loops that are playing, and silences the output.
Take some hi-hat sounds and set them to exclusive voice groups, for example with the open
hi-hat assigned to voice group 1 and the closed hi-hat to voice group 2. Now the open hi-
hat sound can be set to more voices, five for example. This allows some “trails” to be
heard. The second voice group can be set to one voice. Both of these groups should now be
assigned to exclude group 1. With this setup, you obtain the effect of trailing drum sounds
while having a controlled polyphony (voice group 1) and you can still mute that group with
the closed hi-hat.
Cell Activation Module
The Cell Activation module allows you to determine conditions under which a cell is allowed to
be triggered. Usually a cell is triggered upon receiving a MIDI note, which is expressed by the
default settings of Trigger being set to Note On, and Condition being set to Always in this mod-
ule.
Software Reference
Edit Area

BATTERY 4 - Manual - 75

<!-- page 76 -->

The Cell Activation module.
The controls are:
▪
Tabbed pages 1 and 2: The pages provide you with two menus for setting up nested con-
ditions. Page 2 is only available when Condition 1 is not set to Always.
▪
Trigger selection menu: A cell can be triggered either by a Note On command (default set-
ting) or a Note Off command. If you choose Note Off, the cell will be triggered when you
release the key. Velocity and duration will work the same way as with Note On, only after
you release the note. This is important when combining the Note Off trigger with articula-
tions such as Roll or Geiger Counter in the Articulation module.
▪
Condition 1 and 2: The Condition menus provide the following options:
◦Always: Always means that there is no condition to be fulfilled for a cell to be trig-
gered by a MIDI note. This is the default setting.
◦Start on Key: With this function, you can activate a cell with a specific key/pad
(range) on your keyboard. The two key-number fields (Key Min and Key Max) will ap-
pear right next to the menu when this option is selected. Here you can set the specific
key range that will allow the cell to be triggered by incoming MIDI notes. E.g., if cell
A1 is triggered by MIDI note C1 (which you assign with the Key Range controls of the
Quick Access area; see also ↑3.6, Quick Access Area), and the Start On Key condition
is set to C2/C2, then pressing C2 on your keyboard will activate the cell, that is, you
will hear it playing upon pressing C1 on your keyboard. Press C2 again, and the cell
will no longer be triggered by the C1 key.
◦Start on Controller: This function allows cells to be triggered depending on the posi-
tion of a MIDI controller, e.g., on the position of the mod wheel. Choose the controller
number of the controller you want to use for activating a cell (CC), then set the Min
and the Max values in between of which the condition will be fulfilled.
Software Reference
Edit Area

BATTERY 4 - Manual - 76

<!-- page 77 -->

◦Cycle Round Robin: This function allows you to cycle through various cells using only
one key on your keyboard. It’s good to start with an example: select multiple cells and
press the Learn button (the MIDI symbol button) in the Quick Access area (see also
↑3.6, Quick Access Area); then hit a key twice on your MIDI keyboard. You have just
assigned all selected cells to be triggered by that one MIDI note; now back in the Set-
up page, set the cell activation to Cycle Round Robin. You can now assign a Position
in the cycle to each of the selected cells. Let's say you’ve assigned cells A1 through
A6 to be triggered by MIDI note C1, and you have then assigned cells A1 through A6
to the Position numbers 1 to 6 in the cycle; the cells will then play successively when
you hit MIDI note C1 on your controller repeatedly.
Once you get the hang of it, this can turn out to be a very frequently used feature.
Position sets the position of the cell in the cycle; Cycle Nr. is used to set up further
cycles that run simultaneously to the first one; Reset CC is used to assign a MIDI note
to reset the relevant cycle to position 1.
◦Cycle Random: This works the same way the Cycle Round Robin function does, only
you cannot influence the order of the cells being played.
Articulation Module
Use Articulation to add articulation presets to your performance. It is important to note that
each articulation can sound different on different instruments. Also, since many of them alter
velocity, be sure to check the Velocity To Volume modulation settings in the Velocity module
on the Main page (see also ↑3.7.1, Main Page).
The Articulation module.
These are the controls:
Software Reference
Edit Area

BATTERY 4 - Manual - 77

<!-- page 78 -->

▪
Power button: Activates/deactivates the module.
▪
Articulation selection menu: There are ten different articulation presets available in the
articulation selection menu. Depending on the articulation selected, the buttons below
will have different functions. Use them to adjust articulation parameters such as velocity,
speed, or depth of the effect:
◦Alternate Stroke: Produces sounds that slightly vary in character.
◦Release Stroke: Plays the original note and produces a second stroke when you release
your MIDI key.
◦Flam: Plays two notes in rapid succession, the first of which is a grace note.
◦Drag: An exaggerated flam-like effect.
◦3 Stroke Ruff: A nice military-style drum effect.
◦Roll: A continuous drum roll.
◦Buzz: A buzz-like effect.
◦Muted: By quickly fading in and out, this produces a "muted" version of your drum
sound.
◦Speed Roll: A very fast drum roll. The duration of the triggered sample is also short-
ened, so even though many notes are triggered, the voice count is reasonable.
◦Geiger Counter: Produces a random Geiger-like effect.
MIDI Echo Module
The MIDI Echo module can be used to create a variety of tempo-syncable echo effects.
Software Reference
Edit Area

BATTERY 4 - Manual - 78

<!-- page 79 -->

The MIDI Echo module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Tune knob: Use this control to adjust the tuning of the echoes.
▪
Gravity knob: Use this control to adjust the gravity of the echoes. When turned clockwise,
there'll be less gravity and the echoes get slower. When turned counterclockwise, the ech-
oes get faster.
▪
Note value selection menu: Set the echo time to either a tempo-based value (which is
synchronized to BATTERY's tempo control or your host's tempo), or an absolute time-
based value (Sync Off), which is independent of the host tempo.
▪
Time knob: If you select Sync Off from the note value selection menu above, the Time
knob will let you set an absolute echo time value of 10 to 1000 milliseconds. With sync
activated, the value depicted represents the numerator for the note value.
▪
Feedback knob: Set the number of echoes from 1 to 100. If you feel that adjusting this
control has no effect, make sure to check the Velocity To Volume modulation settings in
the Velocity module on the Main page (see also ↑3.7.1, Main Page). With a high modula-
tion amount (near 100), the last echoes might not be audible.
Humanize Module
The Humanize module can be used to add a slight randomization to the sonic characteristics
and the timing of your performance.
Software Reference
Edit Area

BATTERY 4 - Manual - 79

<!-- page 80 -->

The Humanize module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Amount knob: Adjusts the amount of randomization of Sound and Time.
▪
Sound knob: Slightly randomizes the sonic characteristics such as velocity, tune, and vol-
ume.
▪
Time knob: Slightly randomizes the timing of the notes played.
3.7.5
Editor Page

The Editor page contains audio editing tools, a loop editor, and a layer and mapping editor, all
of which provide you with extensive editing features for cells, down to the level of editing indi-
vidual sample layers within a cell.
Software Reference
Edit Area

BATTERY 4 - Manual - 80

<!-- page 81 -->

The Editor page.
When you open the Editor page:
▪
The Quick Access area (see also ↑3.6, Quick Access Area) is converted to a full-blown
Wave and Loop Editor.
▪
The Edit area contains the Mapping Editor.
Refer to the following sections for descriptions of the individual areas.
Wave Editor
The Wave Editor allows you to destructively edit the audio samples within a cell. When there
are multiple sample layers in a cell, you can edit each of the layers individually.
To open the Wave Editor:
►
Click the Wave Editor button below the Waveform Control.
The Wave Editor provides the following controls:
Software Reference
Edit Area

BATTERY 4 - Manual - 81

<!-- page 82 -->

The Wave Editor on the Editor page.
(1) Sample Start/End markers: Adjust the sample's start and end point by clicking and drag-
ging the start (S) and the end marker (E), respectively.
(2) Sample Region selector: Selects the region to edit. You can adjust the size of the region by
clicking and dragging on either side of the Sample Region selector.
(3) Sample Picker: Displays the name of the currently loaded sample / sample layer. The adja-
cent arrow buttons allow you to quick-load other samples into the cell. Whenever there is more
than one sample layer in a cell, an additional drop-down menu appears on the left side of the
sample name field. From that menu, you can select the sample layer to be displayed and edit-
ed in the Waveform Control. Refer to ↑3.6, Quick Access Area for further information on the
Sample Picker.
(4) Wave Editor button: Opens the Wave Editor in the Waveform Control.
(5) Loop Editor button: Opens the Loop Editor in the Waveform Control.
(6) Undo button: Undoes the previous operation performed in the Wave Editor.
(7) Crop button: Removes all audio data before and after the selected region.
(8) Cut button: Cuts out the selected region from the sample.
(9) Copy button: Copies the selected region from the sample.
(10) Paste button: Pastes audio from the clipboard into the selected region of the sample.
(11) Duplicate button: Copies the selected region and appends it at the end of the sample.
Software Reference
Edit Area

BATTERY 4 - Manual - 82

<!-- page 83 -->

(12) Normalize button: This adjusts the volume of the selected region to a standard, optimum
level.
(13) Silence button: Inserts silence in the selected region.
(14) Fade In button: Use this to fade your sample in over a selected region.
(15) Fade Out button: Use this to fade your sample out over a selected region.
(16) DC Correct button: Eliminates DC drifts in the selected region.
(17) Reverse button: Reverses the sample.
(18) Snap button: When enabled, all markers snap to the next location where the waveform
crosses the zero line, or to another marker.
(19) Play Full button: Click the Full button to hear the whole sample, from start to finish,
which means from Start marker (S) to End marker (E).
(20) Play Range button: Click the Range button to hear what's within the Sample Region selec-
tor.
(21) Loop Range button: Loops the audio material within the Sample Region continuously.
Loop Editor
The Loop Editor allows you to create up to four loop regions in a sample. In case there are mul-
tiple sample layers in a cell, you can create loops for each of the sample layers individually.
To open the Wave Editor:
►
Click the Loop Editor button below the Waveform Control.
The Loop Editor provides the following controls:
Software Reference
Edit Area

BATTERY 4 - Manual - 83

<!-- page 84 -->

The Loop Editor above the Mapping Editor.
(1) Sample Start/End markers: Adjust the sample's start and end point by clicking and drag-
ging the start (S) and the end marker (E), respectively.
(2) Loop Region selector: Set the loop region by clicking and dragging on either side of the
Loop Region selector. Click on the x in the upper right corner of the selector to delete the loop.
(3) Add Loop button: Adds a loop to your sample. In case of more than one loop in your sam-
ple, click on an individual Loop Region selector to select it for editing.
(4) Sample Picker and Layer Selector: Displays the name of the currently loaded sample / sam-
ple layer. The adjacent arrow buttons allow you to quick-load other samples into the cell.
Whenever there is more than one sample layer in a cell, an additional drop-down menu appears
on the left side of the sample name field. From that menu, you can select the sample layer to
be displayed and edited in the Waveform Control. Refer to ↑3.6, Quick Access Area for further
information on the Sample Picker.
(5) Wave Editor button: Opens the Wave Editor in the Waveform Control.
(6) Loop Editor button: Opens the Loop Editor in the Waveform Control.
(7) Mode menu: This menu determines whether the loop is played until the volume envelope
has passed its release phase (Loop until End of Envelope), or to the exact moment the key is
released (Loop until Key Release).
Software Reference
Edit Area

BATTERY 4 - Manual - 84

<!-- page 85 -->

(8) Count display: This control determines the number of times the loop will repeat before con-
tinuing to play through the rest of the sample. Possible repetition settings are 0 to 127, and
infinite. If you set it to 0, the loop repeats for as long as the key is held.
(9) Tune display: Each loop can be tuned independently, from an octave down to an octave up.
(10) X-Fade display: The X-Fade function blends some of the end of a loop in with its begin-
ning to create a more seamless loop. The display field shows the length of the section being
mixed in (samples being the unit of length here).
(11) Snap button: When enabled, loop start and end points will snap to the nearest zero cross-
ing in the waveform to prevent unwanted transition noises; however, some sound designers
loop at non-zero-amplitude points to create buzzier sounds. Experiment with snapping to see
what works best for you. This feature is global, i.e., all loops in the sample are affected by it.
(12) Play Full button: Click the Full button to hear the whole sample, from start to finish,
which means from Start marker (S) to End marker (E).
(13) Play Range button: Click the Range button to hear what's inside the selected loop.
(14) Loop Range button: Loops the material within the loop region continuously.
Mapping Editor
The Mapping Editor allows you to edit sample layers, and to define velocity trigger zones for
the sample layers in a cell. In other words, when you drag-and-drop a sample onto a cell, a
velocity zone covering the whole velocity range from 1 to 127 is created in the Mapping Editor,
which means that no matter how hard or soft you hit the key (or pad) assigned to that cell, the
sample will always be triggered. The Mapping Editor allows you to restrict sample layers to be
triggered only within certain velocity zones.
The visual representation of the velocity zone is the Sample Block in the Mapping grid. You
can also adjust things such as transitioning behavior between sample layers with different ve-
locity zones. Furthermore you can set properties such as tuning and panning for individual lay-
ers from the Mapping Editor.
Software Reference
Edit Area

BATTERY 4 - Manual - 85

<!-- page 86 -->

The Mapping Editor.
These are the controls:
(1) Edit menu: The Edit menu provides the following options (be aware that the layer-specific
options affect only the layers currently selected for editing in the Mapping grid):
▪
Add Layer...: Launches the file browser, where you can navigate through your computer's
file structure to select and load a sample layer to the cell. You can also drag-and-drop au-
dio files into the Mapping grid. (Note that when you drag-and-drop an audio file onto a
layer in the grid, the layer will be replaced, however, all layer settings — such as tune,
pan etc. — stay unaffected.)
▪
Cut Layer(s): Cuts the currently selected layer(s) from the cell.
▪
Copy Layer(s): Copies the currently selected layer(s) to the clipboard.
▪
Paste Layer(s): Pastes a layer(s) from the clipboard to the cell.
▪
Delete Layer(s): Deletes the currently selected layer(s) from the cell.
▪
Set Velocity Crossfades: If the velocity range over which a layer is triggered overlaps with
that of another layer, it is possible to crossfade between the layers to provide a smoother
transition. Selecting this menu entry brings up a dotted line in the Sample Block, which
represents the crossfade velocity boundaries of the layer. Use the cursor to adjust these
boundaries for each individual layer.
▪
Remove Velocity Crossfades: Removes any crossfade velocity boundaries from the selected
layers.
Software Reference
Edit Area

BATTERY 4 - Manual - 86

<!-- page 87 -->

▪
Stack Layers: Auto-arranges the cell's layers so that together they span the entire velocity
range of the cell in equal shares.
▪
Reset Stacked Layers: Resets all layers so that each one covers the entire velocity range.
▪
Auto-Spread Layers: Auto-arranges the cell's layers so that together they span the entire
velocity range of the cell, wherein the upper and lower velocity border of neighboring
Sample Blocks meet half way. In case of previously overlapping layers, the borders stay in
place.
▪
Reset Overlapping Layers: Auto-arranges overlapping Sample Blocks, wherein the upper
and lower velocity border of neighboring Sample Blocks meet half way.
(2) Trigger button: When activated, the sample layer is played back when clicking on its Sam-
ple Block in the Mapping grid.
(3) Snap button: When activated, moving velocity limits snaps to velocity limits of neighboring
layers.
(4) Sample Block: A Sample Block is the visual representation of a sample layer and its veloci-
ty range in the cell.
(5) Mapping grid: The Mapping grid allows you to select the individual layers of a cell for edit-
ing by clicking on their Sample Blocks. You can also adjust a layer's velocity limits by clicking
and dragging the Sample Block's lower/upper borders.
(6) Root display: This field sets the original pitch (note center), which usually equals the pitch
at which the sample was recorded. The root key also defines the basis for pitch shifting; for
each semitone (note) that you deviate from the selected root key note, BATTERY will pitch-
shift the selected layer by one semitone. For example, if a layer’s Root key is set to C1, and
you play a D1 note, the sample will be pitched up by two semitones.
(7) Low Vel display: Sets the lower velocity limit of a layer. This is equivalent to clicking and
dragging the lower border of the layer's Sample Block.
(8) High Vel display: Sets the upper velocity limit of a layer. This is equivalent to clicking and
dragging the upper border of the layer's Sample Block.
(9) Tune (st) display: Changes tuning of a layer from –12 up to +12 semitones.
(10) Pan display: Positions the layer in the stereo field: from -100 (fully left); to 0 (center); to
+100 (fully right).
Software Reference
Edit Area

BATTERY 4 - Manual - 87

<!-- page 88 -->

(11) Vol (dB) display: Adjust each layer's volume individually with this control.
3.7.6
Master Page

The Master page provides a range of high-quality effects — just as the Effects page does (with
the exception that the Effects page's LoFi module was exchanged for a Limiter module) — but
they are applied to the entire Kit instead of individual cells: Reverb, Delay, Filter / EQ, Com-
pressor, TM (Transient Master), Saturation, and Limiter modules are available here. There are
also four additional submix/effect buses available on this page, which allow you to group cells
for collective processing before sending them to the main outs.
The Master page in the Edit area.
Refer to the following sections for descriptions of the individual modules on the Master page.
Buses Module
BATTERY provides a main effect / mix bus, and four additional effect/submix buses for proc-
essing multiple cells at once before sending them to the main outputs (via the Master bus);
that way you can, e.g., send one group of percussive elements—let's say kick drums and
snares—through a compressor on Bus 1, and some hi-hats through Bus 2 with a high-pass fil-
ter applied to create a submix within BATTERY.
Software Reference
Edit Area

BATTERY 4 - Manual - 88

<!-- page 89 -->

Additionally, you can also route any cell and/or effect/submix bus directly to one of the addi-
tional direct outs, available via the cells'/buses' context menus (right-click/[Ctrl]-click). The
main output is by default routed to direct outs Stereo 1/2. Use the remaining direct outs to
bypass the Master bus, and to, e.g., address mixer channels in your host application directly.
The Buses module.
The modules are:
▪
Bus 1 - Bus 4: These are the buses for additional effects routing / submixing; click on a
bus to select it, drag-and-drop a cell (or a group of cells) onto a bus to route it through
the bus. When you select a bus, all cells routed through it will be lit, while the cells not
routed through the bus will remain dimmed.
The buses' output level meters display the overall levels of the cells being routed through
them. The slider on top controls the levels. To avoid distortion, you should prevent the
meters from going into the red.
When you right-click on a bus, the subsequent context menu provides you with two op-
tions: Rename FX Bus and Output. The former one is self-explanatory; click on it to re-
name the bus. The Output entry holds a submenu, which lets you select a destination for
the FX bus: route it to the Master bus from here, or bypass BATTERY's main effects en-
gine and select one of the remaining direct outs as destination.
The effects available for each of the four buses are identical to the effects available for
the Master bus; however, the default order of the effects in the effect chain is slightly dif-
ferent. You can change the order of effects in the chain by clicking and dragging the up-
per right corner of the relevant module and positioning it anywhere within the effect sig-
nal chain.
The cell state representations in the Cell Matrix are slightly different depending on whether
the Master page or one of the other pages in the Edit area is opened. For more information
on this, refer to ↑3.5.1, About Cell States.
Software Reference
Edit Area

BATTERY 4 - Manual - 89

<!-- page 90 -->

▪
Master: This is the main effect bus, and all cells are routed through it by default.
The output level meter displays the overall output level of the bus. The slider on top con-
trols the overall output level of the bus. To avoid distortion, you should prevent the meters
from going into the red.
Reverb Module
The Reverb module adds acoustic space to your signal (a reverb simulates the complex reflec-
tions that occur when sounds play in an actual acoustic space).
The Reverb module.
There are two modes available here: standard (algorithmic) and convolution reverb. They are
selectable by clicking on the two symbols on the right side of the module's header; the left
symbol represents the convolution reverb while the right symbol selects the algorithmic mode.
The controls in convolution mode are:
▪
Power button: Activates/deactivates the module.
▪
Size knob: Sets the room size, which affects how long the reverberation lasts. Higher val-
ues are equivalent to larger rooms.
▪
HP knob: High-pass filter (a filter that lets high frequencies pass but filters out lower
ones). Rotate the knob to set the frequency at which the filter starts filtering.
▪
LP knob: Low-pass filter (a filter that lets low frequencies pass but filters out higher
ones). Rotate the knob to set the frequency at which the filter starts filtering.
▪
Convolution display: Click the arrow-shaped buttons next to the display to select one of
the presets for the reverb module. You can also drag and drop samples from the Library
Browser, or .wav files from your desktop directly onto the display to use them as reverber-
ation templates for the convolution reverb.
▪
Reverse button: When this button is activated, the reverb is played back in reverse.
Software Reference
Edit Area

BATTERY 4 - Manual - 90

<!-- page 91 -->

▪
Return slider: Determines the amount of reverb.
The controls in standard (algorithmic) mode are:
▪
Power button: Activates/deactivates the module.
▪
Size knob: Sets the room size, which affects how long the reverberation lasts. Higher val-
ues are equivalent to larger rooms.
▪
Pre-Delay knob: Introduces a short amount of delay (0-180ms) before the reverb takes ef-
fect. This simulates the reverb response in large rooms, where a short time elapses be-
tween the time a signal occurs and when it first bounces off of a room surface.
▪
Color knob: Determines the type of material used to construct the room. Lower values are
softer surfaces (e.g., wood), higher values are harder surfaces (e.g., concrete).
▪
Damp knob: Sets the amount of absorption in the room from drapes, people, acoustic
treatment etc. Higher values simulate more absorption.
▪
Stereo knob: Higher values increase the stereo effect. Use lower values to simulate sitting
closer to the stage, and higher values for sitting further back in the hall.
▪
Return slider: Determines the amount of reverb.
Delay Module
A simple but flexible delay effect to add depth and color to your signal.
The Delay module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Sync selection menu: Sync the delay to your host's tempo with the selected note value.
Software Reference
Edit Area

BATTERY 4 - Manual - 91

<!-- page 92 -->

▪
Feedb knob: This sends a portion of the output back into the input of the delay line,
which creates repeating echoes. A value of 0 produces only one echo, higher values give
multiple echoes.
▪
Time knob: The interval in milliseconds between hearing the clean signal and the first de-
lay of the delayed signal.
▪
Pan knob: Setting a value higher than 0 results in a panning effect where each consecu-
tive echo alternates between the left and right channel. The higher the value, the greater
the stereo spread; at a value of 100 signals alternate between the far left and far right
channels.
▪
Damp knob: Reduces (damps) high frequencies in the delayed signal. Higher values re-
duce the highs further. With feedback applied (described above), each successive echo
has progressively lower high-frequency response.
▪
Return slider: Determines the amount of delay.
Filter / EQ Module
The Filter / EQ module changes the frequency characteristics of the signal (cell) passing
through it in various ways. A filter is basically a special kind of amplifier that changes gain on-
ly at specific frequencies of the signal, either boosting or cutting those. This module is very
similar to the Filter / EQ module on the Effects page (see also ↑3.7.2, Effects Page); however,
different filter modes have different filter bands.
The Filter / EQ module.
The controls are:
Software Reference
Edit Area

BATTERY 4 - Manual - 92

<!-- page 93 -->

▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Filter / EQ module comes with
the following factory presets:
◦Solid G-EQ: Solid G-EQ Loudness
◦3-Band EQ: 3-Band EQ Kick Fattener, 3-Band EQ Telephone Setting
◦Lowpass: 4 Pole Lowpass
◦Highpass: 2 Pole Highpass
◦Bandpass: 4 Pole Bandpass
◦Peak/Notch: Notch Filter
◦Effect: Formant Filter
▪
Filter / EQ type selection menu: There are several filter modes available from the selection
menu, which all affect the sound differently:
◦Solid G-EQ: The Solid G-EQ is modeled on high-quality analogue circuitry. It is a 4-
band parametric EQ.
The adjustable filter bands are: L (low frequency band); LM (low-mid frequency band);
HM (high-mid frequency band); and H (high frequency band). They can be selected
with the tab buttons above the controls.
The available controls are: Freq (adjusts the center frequency of the frequency band,
at which the boost or cut will occur); Bell button (toggles the bell shape of the fre-
quency band — only available for L and H bands); Q (as it were, a bandwidth control
— only available for LM and HM); Gain (adjusts the amount of boost or cut at the fre-
quency band); Output (adjusts the module’s output level).
◦3-band EQ: This is a classic 3-band EQ. Each of the three bands has three parameter
knobs: Freq (adjusts the center frequency of the frequency band, at which the boost
or cut will occur), BW (adjusts the range of frequencies over which boosting or cutting
occurs, from narrow to broad), and the Gain (controls the amplitude increase after the
filter, which can be used to compensate for amplitude reduction due to the filter, or to
increase the soft saturation of the effect).
◦Lowpass: This mode contains filters which attenuate signals above the cutoff frequen-
cy, allowing low frequency signals to pass through; hence, the name lowpass.
The available filters are: Ldr 1P (1-pole lowpass which attenuates frequencies above
Software Reference
Edit Area

BATTERY 4 - Manual - 93

<!-- page 94 -->

the cutoff at a rate of -6 dB/octave); AR 2P (a 2-pole lowpass which attenuates fre-
quencies above the cutoff at a rate of -12 dB/octave.); AR 4P (a 4-pole lowpass which
attenuates frequencies above the cutoff at a rate of -24 dB/octave); and Daft (a more
aggressive 2-pole lowpass filter which attenuates frequencies above the cutoff at a
rate of -12 dB/octave). They can be selected with the tab buttons above the controls.
The following controls are available per filter: Cutoff (adjusts the frequency above
which signals will be attenuated.); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect; not available
for the AR filters).
◦Highpass: This mode contains filters which attenuate signals below the cutoff fre-
quency, allowing high frequency signals to pass through, hence, the name highpass.
The available filters are: Ldr 1P (1-pole highpass which attenuates frequencies below
the cutoff at a rate of -6 dB/octave); AR 2P (2-pole highpass which attenuates fre-
quencies below the cutoff at a rate of -12 dB/octave); AR 4P (4-pole highpass which
attenuates frequencies below the cutoff at a rate of -24 dB/octave); and Daft (a more
aggressive 2-pole highpass filter which attenuates frequencies below the cutoff at a
rate of -12 dB/octave). They can be selected with the tab buttons above the controls.
The following controls are available per filter: Cutoff (adjusts the frequency below
which signals will be attenuated); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect; not available
for the AR filters).
◦Bandpass: This mode attenuates signals above and below the cutoff frequency (or
more correctly, the resonant frequency).
The available filters are: Ldr 2P (ladder circuit 2-pole bandpass which attenuates fre-
quencies above and below the cutoff at a rate of -12 dB/octave); Ldr 4P (ladder cir-
cuit 4-pole bandpass which attenuates frequencies above and below the cutoff at a
rate of -24 dB/octave); AR 2P (2-pole bandpass which attenuates frequencies above
and below the cutoff at a rate of -12 dB/octave); and AR 4P (4-pole bandpass which
attenuates frequencies above and below the cutoff at a rate of -24 dB/octave). They
can be selected with the tab buttons above the filter controls.
The following controls are available per filter: Cutoff (adjusts the frequency below
Software Reference
Edit Area

BATTERY 4 - Manual - 94

<!-- page 95 -->

which signals will be attenuated); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect; not available
for the AR filters).
◦Peak/Notch: A notch filter removes a specific frequency band from the signal. It can
be thought of as the inverse of a bandpass filter — in fact, it is sometimes referred to
as a "band reject" filter. A peak filter, on the other hand, is quite different - it simply
adds a resonant peak to the signal, without doing much attenuation to the signal.
The available filters are: Ldr Peak (unique filter that accents frequencies at the cut-
off); Ldr Notch (cuts two narrow bands of frequencies at either side of the cutoff); SV
Notch (clean 4-pole notch filter which attenuates frequencies at the cutoff); and SV
BR (band reject filter, which attenuates frequencies at the cutoff). They can be select-
ed with the tab buttons above the filter controls.
The following controls are available per filter: Cutoff (adjusts the frequency below
which signals will be attenuated); Reso (with a value greater than 0, this control will
boost a small frequency range around the cutoff frequency); and Gain (controls the
amplitude increase after the filter, which can be used to compensate for amplitude re-
duction due to the filter, or to increase the soft saturation of the effect — this one is
only available for Ldr Peak and Ldr Notch).
◦Effect: Filters in this category don’t match any of the traditional filter characteristics,
and are suited for special effects.
The available filters are: Frm 1 (a formant filter, designed to mimic the frequency re-
sponse of the human vocal tract, which can be used to emulate the talk box effect);
Frm 2 (a formant filter, also designed to mimic the frequency response of the human
vocal tract, and can be used to emulate the talk box effect); Vow A (vowel filter that
simulates the resonant frequencies of the human vocal tract); Vow B (vowel filter that
simulates the resonant frequencies of the human vocal tract, like Vow A but with
slightly different characteristics); and Phaser (creates a distinct comb filter effect by
using an allpass filter design that radically alters the phase relations in your signal).
They can be selected with the tab buttons above the filter controls.
The following controls are available for the vowel filters and the phaser: Cutoff (ad-
justs the frequency below which signals will be attenuated); and Reso (with a value
greater than 0, this control will boost a small frequency range around the cutoff fre-
quency).
Software Reference
Edit Area

BATTERY 4 - Manual - 95

<!-- page 96 -->

The formant filters have the following controls: Talk (controls the frequency response
of the filter, which can be used to morph between vowel sounds); and Sharp (increas-
es and decreases the peaks and notches in the response, analogous to the resonance
control of the other filters); Size (controls the center of the frequency response, analo-
gous to the cutoff control of the other filters).
Compressor Module
Add punch and control dynamics with the compressor module. Compression is a signal proc-
essing technique that is commonly used in recording. It reduces peaks and raises low-level sig-
nals to produce a higher average signal level.
The Compressor module.
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Compressor module comes with
the following factory presets:
◦Pro: Slammed
◦Solid Bus: Drum Bus, Master Setting, Nice and Punchy, Parallel Compression
▪
Compressor mode selection menu: Lets you select from one of the three available com-
pressor modes Solid Bus Comp, Classic, Pro, and SC Bus Comp.
▪
Thresh knob: Sets the level above which compression kicks in. E.g., with a threshold of
-10dB, signals below that level will be relatively unaffected, but signals above that level
will be attenuated. The degree of attenuation is set by the Ratio knob.
Software Reference
Edit Area

BATTERY 4 - Manual - 96

<!-- page 97 -->

▪
Ratio knob: Indicates the ratio of input signal to output signal once a signal exceeds the
threshold. E.g., a ratio of 3:1 means that if a signal is above the threshold, a 3dB in-
crease in input level yields only a 1dB increase in output level.
▪
Attack knob: Determines how long it takes for the compression effect to kick in once the
input signal exceeds the threshold. The higher the value, the more percussive the effect,
with the tradeoff being higher peak levels. Lower values give a more “squashed” sound,
but keep peaks to a minimum.
▪
Release knob: Sets how long it takes for the compressor gain to return to normal after the
input signal has gone below the threshold.
▪
Makeup knob: The Makeup knob is only available in Solid Bus Comp mode. It lets you
compensate for the gain reduction during compression. This only affects the processed
signal, so if you turn the Mix knob all the way left (see below), you will hear no difference.
▪
Mix knob: The Mix knob is only available in Solid Bus Comp mode. It lets you adjust the
ratio between mixed and original signal; that is, if you turn the knob all the way to the
left, you will hear the signal as if the compressor was being bypassed; however, the Out-
put knob (see below) will still affect the overall output level of the signal. Setting the knob
all the way right, you will hear only the processed signal.
▪
Source selection rectangle: Only available in SC Bus Comp mode. Lets you select a source
cell to trigger compression. Drag and drop a cell into the rectangle labeled SC to use it as
the compression trigger. For a tutorial on side-chain compression, refer to ↑4.3, Side-
chain Compression.
▪
Gain knob: Use the Gain knob to make up for the reduced peak level during compression.
A good rule of thumb is to set the gain so that peaks with the compressor on reach the
same level as peaks with the compressor off.
▪
Output knob: Adjusts the output level of the module.
Compression requires a fair amount of CPU power, so make sure they are turned off when
not needed.
Software Reference
Edit Area

BATTERY 4 - Manual - 97

<!-- page 98 -->

TM (Transient Master) Module
The Transient Master is an easy to use compressor designed to control the attack and sustain
of a sound. Instead of following the amplitude of the sound like a traditional compressor, it
follows the general envelope and is not as susceptible to changes of input gain. It is best used
on sounds with fast attacks, like percussion, pianos or guitars. The Transient Master can also
be quite extreme in some cases, so use it with caution.
The TM module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The TM module comes with the fol-
lowing factory presets:
◦British Setting
◦No Attack
◦Room Remover
◦Snare Enhancer
◦Tight Kick
▪
Attack knob: Controls the scaling of the attack portion of the input signal’s volume enve-
lope. Increasing this parameter will add more punch, and decreasing it will reduce sharp
attacks.
Software Reference
Edit Area

BATTERY 4 - Manual - 98

<!-- page 99 -->

▪
Sustain knob: Controls the scaling of the sustain portion of the input signal’s volume en-
velope. Increasing this parameter will add more body to the sound, and decreasing it will
reduce the sound’s tail.
▪
Input knob: Controls the input gain to the effect.
▪
Output knob: Controls the output gain after the effect. For dynamic effects like compres-
sors, this is very important.
Saturation Module
The Saturation module provides expansion/compression/saturation effects. Unlike a standard
audio compressor/expander, saturation works on individual sample bits, not the overall sound.
Therefore it can greatly alter the sound of even the shortest samples.
The Saturation module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Saturation module comes with
the following factory presets:
◦Classic: Classic Distortion
◦Drums: Cranked, Dirty Kick
◦Tape: Aggressive Tape, Warm Tape
▪
Saturation type selection menu: Provides you with three basic types of saturation: Classic,
Drums, and Tape.
Software Reference
Edit Area

BATTERY 4 - Manual - 99

<!-- page 100 -->

▪
Gain knob: Controls the input gain of the effect. This will increase the amount of tape dis-
tortion and compression.
▪
Warmth knob: Controls the low frequency boost/cut of the effect. (Only available in Tape
saturation mode.)
▪
HF knob: Controls the high frequency roll-off starting frequency. Frequencies above this
point will be attenuated. (Only available in Tape saturation mode.)
▪
Output knob: Controls the output gain of the effect.
Limiter Module
A Limiter is a mastering tool that restricts dynamics to an absolute level. It is an extreme form
of compression, useful for making quiet components in a mix louder while restricting loud
components to an optimum level. It can change a relatively meek drum mix into a confident,
polished sound.
The Limiter module.
The controls are:
▪
Power button: Activates/deactivates the module.
▪
Preset menu (arrow button): Opens the Preset menu. The Limiter module comes with the
following factory presets:
◦Basic Limiter
◦No Overs
◦The Pump
Software Reference
Edit Area

BATTERY 4 - Manual - 100

<!-- page 101 -->

▪
In Gain knob: The input level of the limiter.
▪
Release knob: The time required by the limiter to release the effect.
▪
GR meter: The gain reduction meter displays how much compression is currently going
on.
▪
Output knob: Adjusts the output level of the module.
3.8
Preferences

The Preferences panel lets you specify various default settings for BATTERY. To open the Pref-
erences panel:
►
Click on the application menu button in BATTERY's Header, and select the Preferences...
entry from the File menu.
The following pages are available in the Preferences panel:
▪
General: see ↑3.8.1, General Page.
▪
Library: see ↑3.8.2, Library Page.
▪
Engine: see ↑3.8.3, Engine Page.
▪
Loading: see ↑3.8.4, Loading Page.
▪
Cell Rendering: see ↑3.8.5, Cell Rendering Page.
Software Reference
Preferences

BATTERY 4 - Manual - 101

<!-- page 102 -->

3.8.1
General Page

The General page in the Preferences panel.
▪
Cell Matrix section:
◦Warning Before Deleting Cells: Check this option to have a warning displayed before
deleting a cell(s) from the Cell Matrix.
◦Warning Before Deleting Row / Column: Check this option to have a warning displayed
before deleting a row or column of cells from the Cell Matrix.
◦Default Color: Select the default color to be used for cells in the Cell Matrix. All cells
set to Use Default Color in their context menu will use the color specified in this
menu.
▪
Cell Triggering section:
Software Reference
Preferences

BATTERY 4 - Manual - 102

<!-- page 103 -->

◦On Mouse Click: Check this option to trigger cells via mouse click.
◦Velocity: Set the velocity trigger level for cells when triggered via mouse click.
▪
Interface section:
◦Draw Envelope & LFO Curves when Adjusting: When checked, this enables drawing
envelope and LFO curves in the Waveform Control (see also ↑3.6, Quick Access Area).
▪
Transpose section:
◦MIDI Input (oct): Transposes the MIDI input by octaves. This can be helpful when
working with MIDI keyboards of a smaller key range.
3.8.2
Library Page

The Library page in the Preferences panel.
Software Reference
Preferences

BATTERY 4 - Manual - 103

<!-- page 104 -->

▪
Fact. button: Specify the location of BATTERY's Factory Library from here.
▪
User button: Specify the location of your additional user libraries from here. Use the Add
and Remove buttons to add and remove entries.
▪
Rescan button: Rescans the currently highlighted library folder in the list.
3.8.3
Engine Page

The Engine page in the Preferences panel.
▪
Performance section:
◦Multiprocessor Support (Standalone): Select the number of CPUs to be utilized by
BATTERY in stand-alone mode. When using BATTERY as a plug-in, multiprocessor
support will be handled by your host software.
▪
Audio Outputs section:
Software Reference
Preferences

BATTERY 4 - Manual - 104

<!-- page 105 -->

◦Setup for New Instances: Select the kind and amount of outputs each new instance of
BATTERY should be started with. The default setting is a 16 channel stereo output
configuration.
▪
Convolution Reverb section:
◦Sample Rate: Select the sample rate for the convolution reverb mode of the Reverb
module in the Master page. Experiment with the settings to see which ones provide
the best results for you.
◦Latency: Sets the latency for the convolution reverb mode of the Reverb module in the
Master page. Experiment with the settings to see which ones provide the best results
for you.
3.8.4
Loading Page

The Loading page in the Preferences panel.
Software Reference
Preferences

BATTERY 4 - Manual - 105

<!-- page 106 -->

▪
Kits section:
◦Template Kit: Choose a Kit for BATTERY to start each new instance with. You can se-
lect the Factory Default Kit, or the Kit currently loaded to be used as BATTERY's de-
fault Kit.
▪
Samples section:
◦When Loading Multiple Samples: Select whether loading multiple samples at once re-
sults in all samples becoming sample layers of one cell (see also ↑3.7.5, Editor Page),
or if they are being spread out across multiple cells in the Cell Matrix.
◦Expand Loop Slices to Individual Cells: Certain file types (such as REX files, ACID wav
files, and Apple Loop files) contain information about individual loop slices in the file.
Check this option to import each slice to an individual cell when loading a loop file.
◦Load Files Ignoring Original Loop Points: Certain file types (such as REX files, ACID
wav files, and Apple Loop files) contain information about individual loop slices in the
file. Check this option to ignore the loop points upon loading loop files. The files will
then behave like an ordinary audio file, and will not be influenced by BATTERY's or
the host application's tempo.
Software Reference
Preferences

BATTERY 4 - Manual - 106

<!-- page 107 -->

3.8.5
Cell Rendering Page

The Cell Rendering page in the Preferences panel.
▪
MIDI Settings section: This section determines characteristics of the rendered cell based
on the settings of the cell to be rendered during conversion.
◦Note Number: If the Key Range for a given cell is wider than one note (see ↑3.6,
Quick Access Area), and Key Track is activated in the Setup page's MIDI Input mod-
ule (see ↑3.7.4, Setup Page), the rendered cell will be tuned according to this setting;
e.g., when you have a bass sample playing in half note steps from C1 to C2, and the
Note Number is set to Upper, the rendered cell will be tuned according to the tuning
of the bass sample on C2.
◦Note Length: Determines the length of the rendered cell, which happens based on
BATTERY's tempo set during conversion.
Software Reference
Preferences

BATTERY 4 - Manual - 107

<!-- page 108 -->

◦Velocity: Determines the level of the rendered cell based on the velocity of the cell to
be rendered during conversion.
▪
Audio Settings section:
◦File Format: Select the file format for rendered cells from here.
◦Sample Rate: Select the sample rate for rendered cells from here.
◦Bit Depth: Select the bit depth for rendered cells from here.
For a tutorial on rendering cells, refer to ↑2.2, Basic Operation.
3.9
Audio and MIDI Settings

The Audio and MIDI Settings panel allows you to configure the audio and MIDI hardware de-
vice(s) to use with BATTERY, along with the audio routing between your audio device and BAT-
TERY.
►
To open the Audio and MIDI Settings panel, select the Audio and MIDI Settings… entry
from the File menu (in the application menu bar or via the application menu button in
the header).
The Audio and MIDI Settings panel contains three pages. Each page can be displayed by click-
ing on the corresponding tab at the top of the window.
3.9.1
Audio Page

The Audio page holds settings related to your audio interface.
Software Reference
Audio and MIDI Settings

BATTERY 4 - Manual - 108

<!-- page 109 -->

The Audio page of the Audio and MIDI Settings panel.
Setting
Description
Driver
Select your audio driver here.
Device
This allows you to choose from the available devices if you have connected
more than one audio interface.
Status
This shows you whether your audio interface is currently running.
Software Reference
Audio and MIDI Settings

BATTERY 4 - Manual - 109

<!-- page 110 -->

Setting
Description
Sample Rate
The currently selected sample rate of your audio interface. Please restart
BATTERY after changing the sample rate.
Latency
Mac OS X: This slider allows you to adjust the latency of your audio inter-
face in samples. Lower values result in a more immediate playing response
but are heavier on both the CPU and the audio driver, and may result in
audible clicks and pops. Larger values are easier on the CPU, but intro-
duce a larger latency (i.e., there may be a very small delay between when
you hit a pad and when you actually hear it). You should therefore experi-
ment with this setting so that it is as low as possible without overloading
your CPU or introducing any audio artifacts.
Windows: When using an ASIO driver, the Audio and MIDI Settings window
shows an ASIO Config button instead of the Latency slider. Click this but-
ton to open the settings window of the selected ASIO driver.
3.9.2
Routing Page

The Routing page allows you to configure the connections between the virtual outputs of BAT-
TERY and the physical outputs of your audio interface.
Software Reference
Audio and MIDI Settings

BATTERY 4 - Manual - 110

<!-- page 111 -->

The Routing page of the Audio and MIDI Settings panel.
Element
Description
Outputs
In the right column, you can assign BATTERY's outputs to the physical
outs of your audio interface. Click the fields in the right column to select
the desired outputs via a drop-down menu.
3.9.3
MIDI Page

The MIDI page allows you to set up the MIDI input and ouput ports that you want to use with
BATTERY.
Software Reference
Audio and MIDI Settings

BATTERY 4 - Manual - 111

<!-- page 112 -->

The MIDI page of the Audio and MIDI Settings panel (entries may vary on your computer).
Element
Description
Inputs
Clicking Inputs displays a list of all the available MIDI inputs of your sys-
tem. You can activate/deactivate each input by clicking the fields in the
Status column, which displays the current status of the corresponding
port.
Outputs
Clicking Outputs displays a list of all the available MIDI outputs of your
system. You can activate/deactivate each output by clicking the fields in
the Status column, which displays the current status of the corresponding
port.
3.10
The Missing Samples Dialog

The Missing Samples dialog allows you to resolve issues regarding samples that are missing
upon loading Kits. This can happen when you have moved files or folders outside of BATTERY.
In case of missing samples, you will be presented with the following dialog:
Software Reference
The Missing Samples Dialog

BATTERY 4 - Manual - 112

<!-- page 113 -->

The Missing Samples dialog, informing you about the samples missing, and where BATTERY expected to find them.
You have the following options:
▪
Resolve Automatically section:
◦Search Library button: Scans BATTERY's Library for the missing samples.
◦Search File System button: Scans your entire file system for the missing samples.
▪
Resolve Manually section:
◦Point to Folder button: Lets you point to a specific folder on your computer to scan for
the missing samples.
◦Point to Files button: Lets you point directly to the new location of a sample.
▪
Options section:
Software Reference
The Missing Samples Dialog

BATTERY 4 - Manual - 113

<!-- page 114 -->

◦Check for Duplicates checkbox: With this option disabled, BATTERY will automatically
load the first file that matches the file name of a missing sample. When you enable
this option, duplicates will be collected, and another dialog will guide you through se-
lecting the right missing sample for your Kit.
◦Allow Alternative File Types checkbox: Allows to use alternative file types with the
same name (e.g., if you converted a sample to another file type).
◦Apply to other Battery Instances checkbox: Forwards resolved conflicts to other instan-
ces of BATTERY, so you don't have to resolve missing samples issues more than once.
Software Reference
The Missing Samples Dialog

BATTERY 4 - Manual - 114