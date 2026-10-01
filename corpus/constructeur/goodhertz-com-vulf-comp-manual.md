---
titre: "goodhertz.com — manual"
source: https://goodhertz.com/vulf-comp/manual/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: funk moderne ; documentation constructeur
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Vulf Compressor by Goodhertz 

# Vulf Compressor

### Beastly compression, by Vulf

 (dictated via notes app)

 It is with great pleasure that I dictate this to you via the notes app on my cellular device please enjoy this plug-in and use it as much is your CPU allows please use it on the master bus try it on individual instruments it’s great on drum brakes and electric bass to add extreme attack please do not treat this like a classic plug-in where they tell you to not use as much bass it save presets save channel strips let this be a part of your mixing thank you.

 – Jack Stratton, Vulfpeck 

# Interface Preview

 Here’s a screenshot of Vulf Compressor in action. Click anywhere on the interface to jump to a control’s definition below.

#### Advanced Controls

# Controls

## Primary Controls

#### 
 
 Input Gain 

 Varies the input gain, pre-compression.

 Input Gain includes a level meter embedded in the slider. This meter shows the peak level of the input signal before Vulf Compressor ’s processing. 

 If the signal peak exceeds or equals 0.0dB the meter color turns red, indicating that clipping could occur. Vulf Compressor will never clip internally, due to its double-precision floating-point processing, but the signal might be clipped at a later stage (by the host/DAW or DAC).

 Default 
 0.0dB 

#### 
 
 Compression Amount 

 Controls the overall compression amount.

 It’s not possible to entirely shut off the compression. Even at 0% , Vulf Compressor still imparts a bit of its signature compressor sound.

 If you do want absolutely no compression, use the Master Mix .

 Default 
 50% 

#### 
 
 Wow/Flutter Amount 

 Controls the depth of the vinyl wow & flutter .

 Wow/Flutter Mix , Wow/Flutter Speed , Wow/Flutter Phase are all controllable in the Advanced Wow/Flutter controls.

 Default 
 15% 

#### 
 
 Lo-Fi Amount 

 Controls overall fidelity. Higher Lo-Fi Amount produces more total harmonic distortion, decreased high frequency resolution, and more noise.

 More precise control for the distortion ( Lo-Fi Crunch ), noise ( Lo-Fi Noise Gain ), & overall lo-fi flavor ( Lo-Fi Type ) are available in the Advanced Noise section.

 Default 
 50% 

#### 
 
 Output Gain 

 Varies the output gain, post-compression.

 Output Gain includes a level meter embedded in the slider. This meter shows the peak level of the output signal after Vulf Compressor ’s processing. 

 If the signal peak exceeds or equals 0.0dB the meter color turns red, indicating that clipping could occur. Vulf Compressor will never clip internally, due to its double-precision floating-point processing, but the signal might be clipped at a later stage (by the host/DAW or DAC).

 Default 
 0.0dB 

#### 
 
 Master Mix 

 Controls the overall impact of Vulf Compressor . At 0% , the Compression Amount , Wow/Flutter Amount , & Lo-Fi Amount processing are fully bypassed.

 The Input Gain & Output Gain are unaffected by the Master Mix setting.

 Default 
 100% 

#### 
 
 Master On/Off 

 Bypasses Vulf Compressor ’s processing.

 We recommend using the Master On/Off instead of your DAW’s plugin bypass to avoid digital artifacts.

 Default 
 On 

## Advanced Controls

 The Advanced section offers more precise control and fine adjustment options.

 To access Vulf Compressor ’s advanced controls, click the ••• icon in the sidebar.

### Advanced Compression

#### 
 
 Comp Attack Time Constant 

 Modifies the speed of Vulf Compressor ’s attack.

 This control is unitless (i.e. not specified in seconds or milliseconds) because Vulf Compressor does not have a traditional fixed attack time (it involves a complex interaction of signal dynamics and feedback). Smaller Comp Attack Time Constant ’s will clamp down quickly, damping transients. Larger Comp Attack Time Constant ’s cause Vulf Compressor to react more slowly, emphasizing the attack and punch of the incoming signal.

 Default 
 1.0x 

#### 
 
 Comp Release Time Constant 

 Modifies the speed of Vulf Compressor ’s release.

 Like Comp Attack Time Constant , this control is unitless (i.e. not specified in seconds or milliseconds). Smaller Comp Release Time Constant ’s cause Vulf Compressor to release more quickly, often sounding louder and causing more audible pumping or even distortion. Larger Comp Release Time Constant ’s cause Vulf Compressor to release more slowly and smoothly.

 Default 
 1.0x 

#### 
 
 Comp Stereo Link 

 Turns the Vulf Compressor stereo link On or Off .

 Options: Off , On 

 When Comp Stereo Link is On , the same amount of compression is applied to each channel. This preserves the existing stereo image.

 When Comp Stereo Link is Off , each channel is compressed separately. This can affect the stereo image when loud sound sources are panned far left or right but can also result in a louder, more powerful overall sound.

 Default 
 On 

### Advanced Wow & Flutter

#### 
 
 Wow/Flutter Mix 

 Overall wow & flutter mix.

 100% is all wow & flutter , no dry signal. 0% is all dry, no wow & flutter .

 Intermediate Wow/Flutter Mix settings will produce some nice flanging effects, which can be just the right thing to spice up a vocal or melodic instrument.

 Default 
 100% 

#### 
 
 Wow/Flutter Phase 

 Controls the stereo phase of the wow & flutter.

 0° produces a monophonic wow & flutter, whereas 180° produces opposite modulation in the left and right channels.

 For some subtle stereo widening, try a Wow/Flutter Phase of 180° with a Wow/Flutter Amount around 10% .

 Default 
 0° 

#### 
 
 Wow/Flutter Speed 

 Speed of the wow & flutter .

 Option 
 
 Discussion 

 33.3 RPM 
 
 Rotational speed for a standard 12-inch vinyl record

 45 RPM 
 
 Rotational speed for 7-inch vinyl records

 78 RPM 
 
 Rotational speed for shellac and 10-inch vinyl

 Default 
 33.3 RPM 

### Advanced LoFi

#### 
 
 Lo-Fi Noise Gain 

 Controls the amount of lo-fi noise.

 You can quickly turn toggle the lo-fi noise On or Off by clicking the small sidebar “noise” icon.

 Default 
 0.0dB 

#### 
 
 Lo-Fi Crunch 

 Amount of total harmonic distortion from moderate: 0% , to crunchy: 100% .

 Default 
 0% 

#### 
 
 Lo-Fi Type 

 Selects the flavor of the lo-fi degradation.

 Option 
 
 Discussion 

 Analog 
 
 Harmonically rich with just the right amount of dirt

 1990's Digital 
 
 Bad 1990’s digital converter with moderate aliasing

 1980's Digital 
 
 Harsh 1980’s digital converter with some nasty aliasing

 Default 
 Analog 

### Sidechain

#### 
 
 Sidechain Listen 

 Listen to the detector signal instead of the output of Vulf Compressor . The detector signal is what Vulf Compressor is “listening” to when calculating gain reduction.

 Sidechain Listen makes it easy to monitor the detector signal and ensure that the sidechain is correctly routed.

 The detector signal will be a blend of the internal and external sidechain inputs, as set by Sidechain External 

 Sidechain Listen includes a small meter that shows the detector signal.

 Default 
 Off 

#### 
 
 Sidechain External 

 Controls how much of the detector signal is from the external sidechain input.

 At 100% , Vulf Compressor ’s gain reduction will be based on the external sidechain input only (the typical use of a sidechain).

 At 0% , the sidechain is fully internal (normal Vulf Compressor operation). At 50% , the detector signal is an even blend of internal and external sources.

 To route to Vulf Compressor ’s external sidechain input, use the host/DAW’s built-in sidechain selection method.

 In Ableton, sidechaining with a 3rd party plugin like Vulf Compressor is different than with a native Ableton plugin. Here’s an Ableton tutorial with more details.

 If you aren’t seeing the option to sidechain with Vulf Compressor , your DAW may not realize that Vulf Compressor now supports an external sidechain. Here’s how to refresh your plugin data in a few popular DAWs:

 Pro Tools 

 Logic 

 Ableton (Follow the step labeled “Rescan plug-ins”) 

 Vulf Compressor ’s makeup gain operates differently for the external sidechain than it does for the internal sidechain. This is due to the high levels of compression that can occur in Vulf Compressor and helps prevent extremely high-level output signals. As a result, sending the same signal to the external sidechain will result in a different output level (and slightly different sound) compared to just sending it to the input.

 This control might seem unconventional (because it is), but it’s very useful for dialing in exactly how much external sidechaining you want.

 Here’s an example: let’s say you have a great sounding mix with Vulf Compressor on the master bus. You’d like Vulf Compressor to compress a bit more when the drums hit, but you don’t want to increase the volume of the drums in the mix. No problem! Just route the drums to Vulf Compressor ’s sidechain (in your DAW) and increase Sidechain External until you’re getting enough additional compression (pumping) from the drums.

 Default 
 0% 

#### 
 
 Sidechain Tilt 

 Adjusts the frequency content of the signal being sent to the sidechain detector.

 Negative values increase bass content in the sidechain, resulting in increased compression sensitivity to the bass frequencies.

 Positive values reduce bass content in the sidechain, resulting in decreased compression sensitivity to the bass frequencies.

 This control functions similarly to a sidechain high-pass filter but with more flexibility! In general, tilting the spectrum of the sidechain towards one direction tends to result in a compressed signal with tonal characteristics of the opposite direction (i.e. more bass in the sidechain means less bass in the output).

 Want big, untamed bass? Try Sidechain Tilt at 100% . Alternatively, if you wanted a tighter, more restrained bass sound with more obvious pumping, try Sidechain Tilt at -100% .

 Listen to the detector signal with Sidechain Listen in order to fine tune the spectral tilt applied to the sidechain.

 Default 
 0% 

#### 
 
 Digital Ref Level 

 Digital Ref Level defines an approximate reference level as seen by the Vulf Compressor input.

 Lowering the Digital Ref Level is equivalent to turning up the Input Gain and turning down the Output Gain by an equal amount. This greatly affects how the signal hits the compressor and lo-fi section, and it should absolutely be used for creative effect.

 For louder sources, ref levels closer to 0.0dB may be most appropriate.

 For the snappiest, attack-heavy compression, try Digital Ref Level at 0.0dB . For crushed & saturated compression, try Digital Ref Level at -36.0dB .

 The Digital Ref Level control has some handy metering with a triangle (▲) indicator that points to Vulf Compressor ’s best guess of the optimal reference level for the current input signal level.

 Default 
 -18.0dB 

#### 
 
 Reset Meters 

 Resets the meter processing. This resets all the metering values across the plugin.

 Options: Off , On 

 Default 
 Off 

#### 
 
 HQ Mode 

 HQ Mode is our no-holds-barred processing mode where super high quality audio is given priority over CPU usage.

 When HQ Mode is turned On , Vulf Compressor uses a higher precision algorithm, providing better spectral resolution at the expense of some added latency (~50 ms) and higher CPU usage.

 Option 
 
 Symbol 

 Off 

 On 

 We recommend using HQ Mode when you need the highest possible quality and don’t mind 2-4x higher CPU usage. An important lead instrument, vocal, or a mastering session is a great place for HQ Mode .

 HQ Mode cannot be MIDI mapped since automating it is not recommended.

 HQ Mode will require more CPU resources and result in a slightly higher processing delay (latency). To ensure proper delay compensation in your host/DAW, automating HQ Mode is not recommended.

 Default 
 Off 

#### 
 
 Preprocess Input Gain 

 Controls the input gain before it hits Vulf Compressor ’s processing.

 Default 
 0.0 

#### 
 
 Postprocess Output Gain 

 Controls the output gain after Vulf Compressor ’s processing.

 Default 
 0.0 

# Specs

### Supported Channel Configurations

 Input Channel # 
 Output Channel # 

 Mono 
 Mono 

 Mono 
 Stereo 

 Stereo 
 Stereo 

# Presets

 The presets are a great way to get to know each plugin. The preset drawer can be accessed at the bottom of each plugin by clicking the current preset name.

#### General

 Default 

#### Vulfmon

 Presets from the spiritual guide behind Vulf Compressor, Vulfmon himself.

 Sad Wurli 
 
 So sad 

 Master Bump 

 Master Hump 

#### COMP

 2-Bus Glue (Parallel) 

 Punch ’n Crunch (Parallel) 

 Lots of Attack 

 Dangerous Attack 

 Slam 

 Crush 

 Heavy Clipping 

 Vacuum Pumped 

 Untamed 26" 
 
 Big, open kick drum a la John Bonham 

 Le Freak Kick 
 
 Reminiscent of disco-era kick drums 

 Accordion Boom 
 
 2002 on Mount Washington 

#### FX

 Old School Crunch 

 Gentle Stereo Wow 

 Mono Flange 

 Max Distortion 

 Bad 1980’s Digital 

 Bad 1990’s Digital 

#### Tiago’s Golden Age of Samplers

 16 Pads Pitch Down 

 1200 Crunch 

 OG 303 VS 

# Acknowledgements

 Annlie Huang 
 / 
 
 Bernard Purdie 
 / 
 
 Chris Conover 
 / 
 
 Diana Zheng 
 / 
 
 James Dewitt Yancey 
 / 
 
 Mushy Krongold 
 / 
 
 Otis Jackson, Jr. 
 / 
 
 Roger Robindore 
 / 
 
 Stephen Ellison 
 / 
 
 TaeHo Park 

# Authors

 Devin Kerr 
 / 
 
 Rob Stenson 
 / 
 
 Jasper Duba 
 / 
 
 Noah Dayan 

# Translators

 TaeHo Park 
 / 
 
 Tiago Frúgoli 
 / 
 
 Gustavo Guzmán 
 / 
 
 Reda Kermach 
 / 
 
 Noah Dayan 
 / 
 
 Gal Cohen 
 / 
 
 Sydney Bolton 
 / 
 
 Enrico Cirene 

# About Goodhertz Plugins

## User Interface

 Goodhertz plugins are made to be workhorse tools that sound amazing. We’ve put a lot of thought and care into the audio quality and plugin usability, and for that reason, we’ve opted for simple and direct controls & interfaces that don’t rely on photorealistic knobs or ornamental screw heads to communicate their meaning.

 We’ve also decided to only include meters and graphs when we feel they will directly lead to a better sonic result. Meters/graphs can consume significant CPU resources, and we firmly believe that if it sounds good, it is good .

 Our meters can be reset at any time using the “Reset Meters” button (in certain plugins) and manually enabled or disabled via the “Enable Metering” User Preference.

## Preset Bar

 Button 
 Action 

 Undo the last parameter change. 

 Redo the last parameter change. 

 Switch to the previous preset. 

 “Preset Name” 
 Opens the preset drawer (Option/Alt + Click to reset all plugin settings to preset). 

 Switch to the next preset. 

 Selects the A settings state. 

 This copies the current settings to the opposite A/B state; i.e. if you’re on the A state, clicking the arrow will copy those settings to the B state. 

 Selects the B settings state. 

## Toolbar

 Introduced in version 3.10, the toolbar at the bottom of the plugin holds a handful of shortcut buttons.

 Icon 
 Action 

 Opens preferences menu 

 Shows diagnostic information 

 Opens plugin manual in your default web browser 

 Opens a URL representation of the current plugin control state (Command/Ctrl + Click to copy the URL to the clipboard) 

 Opens language-selection menu 

 Opens MIDI Learn menu 

 Toggles HQ mode (only in certain plugins) 

 Resets all meters (only in certain plugins) 

 Shrink interface 

 Enlarge interface 

## Keyboard Shortcuts

 Action 
 Keyboard Shortcut 

 Enter New Parameter Value 
 Once you’ve clicked or double-clicked a control, type in a value, then hit Enter , Return , or Tab . Depending on the control type, we support a variety of input values, such as fractions (e.g. 1/4 for 0.25), the kilo suffix (e.g. 4k for 4000), note values for time-based controls (e.g. 1/8T for an eighth note triplet or 1/4D for a dotted quarter note, relative to the current DAW or plugin BPM), and musical notes for frequency controls (e.g. A#5 for 923.33 Hz or Eb2 for 77.78 Hz). 

 Increment Parameter Value 
 ↑ or → arrow keys 

 Decrement Parameter Value 
 ↓ or ← arrow keys 

 Jump to Next Parameter 
 Tab 

 Jump to Previous Parameter 
 Shift + Tab or ` (backtick) 

 Escape Parameter Focus / Close any Open Drawers 
 Esc 

 Tap Tempo 
 t or Click (N.B. For this to work, you must have a BPM or milliseconds control selected.) 

 Save Preset 
 n (N.B. For this to work, the preset panel must be open.) 

 Set Preset as Favorite 
 f (N.B. For this to work, the preset panel must be open.) 

 Edit Preset 
 e (N.B. For this to work, the preset panel must be open.) 

 Update Preset 
 u (N.B. For this to work, the preset panel must be open.) 

 Delete Preset 
 Delete (N.B. For this to work, the preset panel must be open.) 

## Right-Click Actions

 Action 
 Instruction 

 Read about Control in manual 
 Right-Click & select “Show in Plugin Manual” 

 Reset Control to Default 
 Right-Click & select “Reset to Factory Default Value” 

 Lock Control when switching presets 
 Right-Click & select “Lock When Switching Presets” 

 Copy current plugin settings to clipboard 
 Right-Click & select “Copy as URL to Clipboard” 

 Paste all plugin settings from clipboard 
 Right-Click & select “Paste From Clipboard” 

 Reset all plugin settings to Defaults 
 Right-Click & select “Reset All to Defaults” 

 Reset all plugin metering 
 Right-Click & select “Reset Meters” (only available in certain plugins) 

 Reset all plugin settings to Preset 
 Right-Click & select “Reset to [preset] Preset” 

 Update Preset with current plugin settings 
 Right-Click & select “Update [preset] Preset” 

 Create new Preset with current plugin settings 
 Right-Click & select “Create New Preset” 

 Go to the plugin’s manual page 
 Right-Click & select “Read [plugin name] Manual” 

## Right-Click Preferences

 Action 
 Explanation 

 Language 
 Switch the display language of text elements in Goodhertz plugins. We currently support the following languages: English, Spanish, Portuguese, French, Italian, Japanese, Korean, Chinese (Simplified), Chinese (Traditional), and Arabic. 

 Always Open Advanced Pane 
 By default, this is Off — i.e. when the plugins open, they do not show you the advanced controls available by hitting the ••• button in the sidebar. If you’d like to always see the advanced controls, enable this preference. 

 Control Granularity 
 By default, all Goodhertz controls move in small increments when dragged. If you prefer controls to operate with larger increments by default, change this option to Coarse . N.B. This will swap the behavior of the Shift mouse modifier - i.e. Shift-dragging will move a control with standard granularity when set to Coarse . 

 Dark Mode 
 Allows you to choose the color palette used for displaying the interface. If you prefer the look of dark colors (or work in a darker environment) enable this option. The Auto option will automatically adjust the color scheme depending on the system preferences of your machine (Mac only). 

 Enable Hover Markers 
 By default, this is On — i.e. all controls will show markers on hover. If you find this behavior unnecessary, deselect this option and no markers will be shown. 

 Enable Metering 
 By default, this is On — i.e. in normal operation, all audio meters and visualizations available in Goodhertz plugins are enabled and running. If you’d like to turn them off and disable all metering and visualization, deselect this option. And to turn them back on, simply reselect it. N.B. If you’re struggling to use a large number of Goodhertz plugins on an older processor with an integrated GPU, sometimes disabling metering can help. 

 Enable Scroll Input 
 By default, all Goodhertz sliders can be scrolled in addition to dragged. If you find this behavior unnecessary, deselect this option and no scrolling events will be used to control Goodhertz sliders. 

 Enable Tooltips 
 By default, this is On — i.e. all controls will show a tooltip on hover. If you find this behavior unnecessary, deselect this option and no tooltips will be shown. 

 GPU Acceleration 
 By default, this is Enabled — i.e. the GPU will be prioritized whenever possible to improve graphics performance. If your graphics card does not support GPU acceleration, this preference will be automatically set to Reduced . N.B. If you experience graphics issues, disabling this preference may help. 

 Keyboard Focus 
 By default, you can get keyboard focus on any Goodhertz control with a single click. Change this option to ensure keyboard focus only occurs on double clicks. 

 Window Size 
 Enlarge or shrink the Goodhertz plugin window by selecting an option here. This will save your preference for all instances of this plugin. 

 Diagnostics 
 Displays general information about the plugin and the configuration of your system for diagnostic purposes. If you experience any issues with the plugin, it can be helpful to include this information when contacting us. N.B. Clicking this window will copy the contents to the clipboard. 

 MIDI Learn 
 Configure the mapping used to control parameters via MIDI messages. To assign a MIDI number to a control, enable MIDI Learn and send a MIDI message while a control is focused. To remove an assigned mapping, click on a mapping entry in the list or select Clear All to reset the entire mapping. N.B. You can assign different types of MIDI messages including Pitch Bend, Note, and CC messages. 

## Mouse Modifiers

 Action 
 Combination (Mac) 
 Combination (Windows) 

 Reset Parameter to Default Value 
 Option + Click 
 Alt + Click 

 Move Control with Coarse Precision 
 Shift + Drag 
 Shift + Drag 

 Move Control with Fine Precision 
 Command + Drag 
 Ctrl + Drag 

 Move Control with Normal Precision 
 Drag 
 Drag 

## Automation

 Unintentional digital clicks and pops are the worst. They happen for lots of reasons and often end up wasting your time with needless revisions or mastering surgery. When they go unnoticed, they can make their way onto commercial albums and releases.

 Plugin automation is a common cause of clicks and pops. Sweeping an EQ band, changing a delay setting, and even automating a plugin bypass can cause digital artifacts if poorly handled.

 This is not true for Goodhertz plugins. Any parameter in a Goodhertz plugin, even on/off switches, can be automated freely and smoothly without clicks, pops, or zipper noises (unless otherwise noted). You can push them, pull them, LFO them — whatever you do, they’ll handle it gracefully.

 Since our Master On/Off controls won’t create artifacts, we recommend that you use them rather than your DAW-supplied plugin bypass if you want to disable plugin processing.

## Plugin Settings

 Goodhertz plugin settings can be copied and pasted as text urls, which look like this: https://goodhertz.com/vulf-comp/3.0.9?cm=0&wf=0&lf=100&lfc=50 

 To copy and paste, right click anywhere on the plugin interface and select either the copy or the paste option.

 E.g. If you paste “ https://goodhertz.com/vulf-comp/3.0.9?cm=0&wf=0&lf=100&lfc=50 ” into Vulf Compressor it will recall the settings associated with that url. This way you can easily send an exact plugin setting to someone — in an email or a text — without any guesswork or screenshots.

## System Requirements

##### Mac OS X ≥ 10.13

 Audio Unit 64-Bit, VST 64-Bit, VST3 64-Bit, or AAX 64-Bit host

##### Windows ≥ 10

 VST 64-Bit, VST3 64-Bit, or AAX 64-Bit host

## Contact Support

 To send plugin feedback, please e-mail us at feedback@goodhertz.com .

 If you’re having trouble, experiencing a technical issue, or you think you’ve found a bug, please email support@goodhertz.com .

 Find all our contact info & bug-reporting protocol on the contact page .