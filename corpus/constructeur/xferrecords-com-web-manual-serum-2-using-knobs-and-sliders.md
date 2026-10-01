---
titre: "Manuel Serum 2 — Using knobs and sliders"
source: https://xferrecords.com/web-manual/serum-2/using-knobs-and-sliders
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

XferRecords.com | Home of the Xfer Records VST Suite

###### Serum 2 Manual

 Welcome 

 └ Registering Serum 
 └ Getting in Touch 
 └ Downloading Serum 
 └ Installing Serum 
 Exploring Serum 

 └ Exploring Sound Design in Serum 
 Getting Started 

 └ Adding Serum to a Track 
 └ Loading a Serum Preset 
 └ Creating a New Sound 
 └ Saving Changes 
 
 └ Embedding Content When Saving a Preset 

 └ Dragging Audio to Your DAW 
 └ Exploring Basic Operations 
 
 └ Displaying Help (Tooltips) 
 └ Using the Serum Keyboard 
 └ Using Knobs and Sliders 
 └ Undo and Redo 
 └ Controlling the Main Output Volume 

 └ Using Oscillators and Filters 
 
 └ Enabling an Oscillator or Filter 
 └ Choosing Oscillator or Filter Options 
 └ Using Pitch Controls 
 └ Setting the Octave or Semitone Mode 
 └ Routing an Oscillator or Filter 
 └ Accessing the Oscillator or Filter Menu 
 
 └ Locking a Module └ Initializing a Module └ Copying a Module └ Enabling Pitch Tracking └ Pitch Bend Tracking 

 └ Resizing the UI 

### Using Knobs and Sliders

 To adjust a knob or slider, click and drag either up and down or left and right. A pop-up displays the current value allowing you to dial in a specific setting. Hold the Shift key to fine tune the adjustment.

 If your mouse has a scroll wheel, you can also use it to adjust values up and down (without displaying the current value in a pop-up).

 Double-click a knob or slider to display a text box showing the current value. Enter a new value for precise adjustments.

 Click-Dragging a Knob 

 Double-click a knob or slider to display a text box showing the current value. Enter a new value for precise adjustments.

 See “Exploring Global Settings” for more information.

 Right-click a knob or slider to open a context menu that displays the settings and operations available for that control.

 ou can use the menu to choose one or more modulation sources (such as ENV 1 or LFO 2 ) for the control. 

 You’ll read about modulating parameters later in this guide.

 You can also choose to bypass or remove a modulator, or remove all modulators assigned to the control.

 Note: Some controls offer additional menu options, depending on the context. You’ll learn about these options in relevant sections of this guide.

 Right-Click Context Menu 

 You’ll also see the following options available on nearly all knob and slider menus:

 Reset Control — Resets the control to the default value.

 This is the same as Cmd-clicking (macOS) or Ctrl-clicking (Windows) the control.

 MIDI Learn — Activates MIDI learn mode. When enabled, Serum waits for an incoming MIDI CC value. 

 After Serum receives a MIDI CC value, MIDI learn mode is deactivated and the CC# is assigned to the knob or slider. Note that the assignment is saved with the preset (patch).

 When enabled, locks the control setting (preventing a value change) when loading presets. You can, however, continue to adjust the control manually.

 The Reset Control and Lock Parameter options appear in the context menu of almost every control in Serum.

 In all cases, you can use these options to reset the control to the default value and lock a control parameter to prevent it from changing when loading presets, respectively.

 When saving a DAW session, MIDI CC assignments are saved and recalled with the session. 

 When saving a preset, MIDI CC assignments are saved with the preset, but are only loaded if the Load MIDI Map from Preset preference is enabled on the Global page (this setting is disabled by default).

 See “Preferences” for more information about setting global preferences.

 You can set the current MIDI CC assignments to load by default by choosing Save MIDI Map in the main menu and saving the MIDI map as default.SerumMIDIMap in the 
 Serum 2 Presets/System/MIDI CC Maps folder.

 This map then loads automatically when creating a new instance of Serum or choosing Init Preset in the main menu. The map also automatically loads when selecting a preset if the Load MIDI Map from Preset preference is disabled.

 Last updated: May 01, 2025