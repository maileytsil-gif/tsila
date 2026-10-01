---
titre: "Clavinet User Guide (texte du PDF, 20 pages)"
source: constructeur/assets-wavescdn-com-pdf-plugins-clavinet-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

CLAVINET
USER GUIDE

<!-- page 2 -->

Clavinet / User Guide

2
CONTENTS
CHAPTER 1  INTRODUCTION ........................................................................................... 3
1.1 Product Overview ......................................................................................................................................... 4
1.2 Concepts and Terminology ........................................................................................................................... 5
1.3 Components ................................................................................................................................................. 5
1.4 Functional Block/Flow Diagram .................................................................................................................... 6
1.5 Opening Clavinet .......................................................................................................................................... 6
CHAPTER 3 INTERFACE AND CONTROLS ...................................................................... 7
3.1 Interface ........................................................................................................................................................ 7
3.2 Controls ........................................................................................................................................................ 8
Keyboard Control ................................................................................................................................ 8
Keys Section ....................................................................................................................................... 8
Mix Section ......................................................................................................................................... 9
Comp ................................................................................................................................................ 10
Amp Section ...................................................................................................................................... 10
Tone Section ..................................................................................................................................... 11
FX Section ........................................................................................................................................ 12
Output ............................................................................................................................................... 17
3.3 WaveSystem Toolbar Controls ................................................................................................................... 18
CHAPTER 4 Clavinet Standalone Application ................................................................... 20

<!-- page 3 -->

Clavinet / User Guide

3
CHAPTER 1  INTRODUCTION
Thank you for choosing Waves! In order to get the most out of your new Waves plugin, please take a moment to read
this user guide.
To install software and manage your licenses, you need to have a free Waves account. Sign up at www.waves.com. With
a Waves account you can keep track of your products, renew your Waves Update Plan, participate in bonus programs,
and keep up to date with other important information.
We suggest that you become familiar with the Waves Support pages: www.waves.com/support. There are technical
articles about installation, troubleshooting, specifications, and more. Plus, you’ll find company contact information and
Waves Support news.



Acknowledgement
The Clavinet samples library was recorded and produced by Yoad Nevo at NevoSound Studios in London.
To contact Yoad Nevo, visit: http://www.yoadnevo.com

<!-- page 4 -->

Clavinet / User Guide

4
1.1 Product Overview
The Clavinet is a keyboard instrument that uses strings, keys, and electromagnetic pickups to produce a unique, funky
sound. Many musical hits, such as “Higher Ground” and “Superstition” by Stevie Wonder and “Outta Space” by Billy
Preston, fused the Clavinet sound with funky music. By the 1970s, it became a classic element when making funky disco
bass lines and choppy stabs.
The Clavinet is essentially an electrified version of a clavichord – an instrument popular from the Renaissance through
the Classical period. The clavichord was famously quiet, so it was not suited for performances with ensembles and
orchestras. When the Clavinet was introduced in the 1960s, it addressed the issue of amplification and opened the way
for numerous sounds and effects. It was manufactured in Germany until the ‘80s.
The Clavinet consists of sixty keys. It uses electromagnetic pickups to turn sound into electrical signals, ready to be
amplified. The overall sound of the Clavinet is a staccato pluck, followed by a rather quick decay. It features a damper
that shortens the decay (a mode we call “Mute”), or lets it die out naturally (“Unmute”). This produces a sound that is a bit
more open and bright, especially in its decay.
The Waves Clavinet is a virtual instrument, sampled from an original Hohner Clavinet D6 in both its Mute and Unmute
modes. We added some sound-shaping tools and effects, such as EQ and Compression. There is also an AutoWah
effect and (as with other Waves classic keyboard instruments) there is a phaser, chorus, and reverb.

<!-- page 5 -->

Clavinet / User Guide

5
1.2 Concepts and Terminology
• In the case of the Clavinet, the term “Mute” does not describe a full mute of the sound. Instead, it refers to
the action of a fader-like lever to the right of the Clavinet’s keys that mechanically chokes the sustain and
introduces a faster decay and mellower tone.
• The tuning of the Clavinet is equal tempered. Equal temper means that an octave is divided to 12 equal ½
tone or semitone intervals of 100 cents each. This is contrary to the Justonic or other temperaments.
• The reference tuning for the actual sampled instrument was the normative middle A=440 Hz. The Clavinet’s
top toolbar features a global tune control that allows setting of the overall tuning one semitone up or down.
For users looking to adhere to a 432 Hz reference, the tuning should be set to -31 cents.

Waves Clavinet is powered by the Waves Sampler Engine (WSE): a state-of-the-art multi-sample engine,
designed to deliver solid, high-quality performance.

1.3 Components
The Waves Clavinet has one component: Clavinet Stereo.
Clavinet is a virtual instrument plugin and will appear under the related selection menus for virtual instruments in all
supported DAW host applications.
Waves Clavinet also has a standalone application. It uses ASIO (Windows) or Core Audio (Mac) drivers to enable play
through any audio device of choice. Clavinet receives MIDI data to trigger notes and control changes.

<!-- page 6 -->

Clavinet / User Guide

6
1.4 Functional Block/Flow Diagram




1.5 Starting Clavinet
Insert the Clavinet plugin on an instrument track in your DAW, or launch the standalone application. The plugin will load
its default settings and will be ready to use.
Before getting started, use the Velocity Curve control to adjust your keyboard to get the feel you like. Once you’re happy
with the touch, you can uncheck the VEL (velocity) box in the top bar. This prevents the velocity setting from changing
when a preset is loaded.

<!-- page 7 -->

Clavinet / User Guide

7
CHAPTER 3 INTERFACE AND CONTROLS
3.1 Interface

<!-- page 8 -->

Clavinet / User Guide

8
3.2 Controls
Keyboard Control















A virtual keyboard enables you to preview the sound of a note when a keyboard controller is not available. Use a mouse
or similar input device to play a note. This control cannot be automated, although it will follow any MIDI input device.
Keys Section






Vel Curve
The Vel Curve control changes the curve of the velocity response from logarithmic to exponential. Use it to adjust the feel of
your MIDI keyboard.
When the control is set to 0, the curve of the velocity response is linear.
Range: -50 to +50
Initial Value: 0
Reset Value: 0
Continuous control
Formant
The Formant control changes the sound character, but not the pitch. Each step is equal to a half tone. This means that when
this control is set to -12, the piano sound character will be lower by one octave, while the pitch will not change.
Range: -12 to +12
Initial Value: 0
Reset Value: 0

<!-- page 9 -->

Clavinet / User Guide

9
Discrete control, 25 steps
Mix Section









Main
Main controls the sampled sound of the Clavinet without the mechanics and the release keys sounds. It controls the Main
samples level in the overall mix.
Range: 0% – 100%
Initial Value: 90%
Reset Value: 90%
Continuous control

Key Up
Key Up controls the sound of the keys while releasing. It controls the Key Up samples level in the overall mix.
Range: 0% – 100%
Initial Value: 12%
Reset Value: 0%
Continuous control

Mechanics
Mechanics controls the sampled sound of the Clavinet mechanics without the Main or Key Up sounds. It controls the
Mechanics (thump) samples level in the overall mix.
Range: 0% – 100%
Initial Value: 12%
Reset Value: 0%
Continuous control

<!-- page 10 -->

Clavinet / User Guide

10
Comp






The Comp control influences the mix of the internal compressor. Turning the knob clockwise increases the level.
Range: 0% – 100%
Initial Value: 25%
Reset Value: 0%
Continuous control
Amp Section





Amp On/Off
The Amp button turns the Amp section On or Off.
Range: Off or On

Initial Value: Off
Switch: Off or On
Reset Value: None
Alt+click does not affect the current mode of this switch.

Drive
Controls the level of the amplifier overdrive.
Range: 0–100
Initial Value: 0
Reset Value: 0

<!-- page 11 -->

Clavinet / User Guide

11
Continuous control

Type
There are two microphone options in front of the amplifier: Condenser and Dynamic.
Range: Dyn or Cond
Initial Value: Cond
Reset Value: Cond
Two-state switch

Tone Section







Bass
The Bass control is a bell filter at 100Hz, which can be increased or decreased by up to +/-18 dB.
Range: -50 – +50 (+50 = +18 dB)
Initial Value: 0
Reset Value: 0
Continuous control

Mid
The Mid control is a bell filter at 380Hz, which can be increased or decreased by up to +/-18 dB.
Range: -50 – +50
Initial Value: 0
Reset Value: 0
Continuous control

Treble
The Treble control is a high-shelf filter at 7.5KHz, which can be increased or decreased by up to +/-18 dB.

<!-- page 12 -->

Clavinet / User Guide

12
Range: -50 – +50
Initial Value: 18
Reset Value: 0
Continuous control

FX Section





FX On/Off
The FX button turns the FX On or Off.
Range: Off or On
Initial Value: On
Switch: Off/On
Reset Value: None. Alt+click does not affect the current mode of this switch.

AutoWah On/Off
The AutoWah button turns AutoWah On or Off.
Range: Off or On
Initial Value: Off
Toggle Switch
Reset Value: None. Alt+click does not affect the current mode of this switch.


Sens
Sens controls the sensitivity of the Wah effects envelope detector.
Range: 0 – 100
Initial Value: 80
Reset Value: 80
Continuous control

<!-- page 13 -->

Clavinet / User Guide

13

Speed
Speed controls the speed of Wah filter movement.
Range: 0 – 100
Initial Value: 60
Reset Value: 60
Continuous control

Range
Range controls the center frequency of the Wah filter.
Range: 0 – 100
Initial Value: 30
Reset Value: 30
Continuous control

Direction
The Direction switch flips the movement direction of the Wah filter.
Range: Up or Down
Initial Value: Up
Toggle Switch
Reset Value: None. Alt+click does not affect the current mode of this switch

<!-- page 14 -->

Clavinet / User Guide

14
Phaser







Phaser On/Off
The Phaser button turns the Phaser section On or Off.
Range: Off or On
Initial Value: On
Toggle Switch
Reset Value: None. Alt+click does not affect the current mode of this switch.

Phaser Mix
Phaser Mix controls the level of the Phaser effect.
Range: 0% – 100%
Initial Value:  50%
Reset Value: 0%
Continuous control

Phaser Rate
Phaser Rate provides control over Sync rates that relate to the host (such as ¼), or Free rates (in Hz) that can be set
independent of the host BPM, using the same knob. The middle position (i.e. 12 o’clock) is the slowest Free value. Turning
the knob clockwise from this position increases the rate from 0.01 Hz to 22 Hz.
When the knob setting is less than 12 o’clock, values are defined with respect to the host. Turning the knob
counterclockwise increases the Phaser Rate through music note duration values related to the host’s BPM: 1/32T, 1/32,
1/32D, 1/16T, 1/16, 1/16D, 1/8T, 1/8, 1/8D, 1/4T, 1/4, 1/4D, 1/2, 1/2D, 1, 2/1.
2/1 equals one cycle in two bars.
Scaling: Custom.
Range: Sync 1/32T – 2/1 / Free 0.01 Hz – 22 Hz
Initial Value: 1 Bar Sync rate
Reset Value: 0.1 Hz Free rate
Continuous control.

<!-- page 15 -->

Clavinet / User Guide

15
Phaser Depth
Phaser Depth controls the Phaser feedback.
Range: 0 – 100
Initial Value: 15
Reset Value: 0
Continuous control

Chorus





Chorus On/Off
The Chorus button turns the Chorus section On or Off.
Range: Off or On
Toggle Switch
Reset Value: None. Alt+click does not affect the current mode of this switch.

Depth
The Depth control influences the dry/wet mix of the signal into the chorus and determines how much the module oscillator
will influence the delay. The chorus engine contains four delays and four oscillators.
Range: 0 – 100
Initial Value:  34
Reset Value: 0
Continuous control

<!-- page 16 -->

Clavinet / User Guide

16
Reverb






Reverb Mix
Reverb Mix controls the balance between the dry and wet signal. It also controls the amount of reverb added.
Range: 0% (dry) to 100% (wet)
Initial Value: 20%
Reset Value: 0% (dry)
Continuous control

Reverb Predelay
Reverb Predelay controls the amount of the delay between the dry and wet signals.
Range:  20 ms – 400 ms
Initial Value: 20 ms
Reset Value: 55 ms
Continuous control

Reverb Time
This controls the reverb time.
Range: 0.4sec – 6 sec
Initial Value: 1.3 sec.
Reset Value: 2 sec
Continuous control

Reverb Damp
The Reverb Damp control increases the level of the high frequencies during the decay.
Initial Value: 0.4
Reset Value: 0.1
Continuous control

<!-- page 17 -->

Clavinet / User Guide

17
Output















Volume
Volume controls the output gain level after plugin processing.
Range: 0 –10
Initial Value: 7
Reset Value: 7
Continuous control
Limit
The Limit control confines the instrument’s output with respect to full scale. When Limit is active, the clip LED pulses to
reflect limiter gain adjustment activity. The limiter is especially useful when using the standalone application.
Range: On or Off
Initial Value: Off
Reset Value: Off
Discrete Off or On control

Meter Scale
Peak meter: -48 dB to 0 dB (shown as -30 dB to +18 dB)
VU meter scale calibrated for 18 dB of headroom (0 dBVU = -18 dBFS).

<!-- page 18 -->

Clavinet / User Guide

18
Split Meters
Separate left and right meter indicators.
Black = Left
Green = Right
3.3 WaveSystem Toolbar Controls
Use the bar at the top of the plugin to save and load presets, load sample libraries, compare settings, undo and redo
steps, and resize the plugin. To learn more, click the icon at the upper-right corner of the window and open the
WaveSystem Guide.
Samples
Clavinet loads the default sample library when the plugin is instantiated or the application is launched. Click on the
Samples button to navigate to another sample library folder. This library will become the default until you load another
library. The folder must contain valid Waves sampled instrument files, otherwise the OK button will be grayed out. You can
download Waves sample libraries from the Waves download page
http://www.waves.com/downloads/sample-libraries

<!-- page 19 -->

Clavinet / User Guide

19
Tune
Allows global fine tuning of the instrument.
Range: -100 – 100 cents
Initial Value: 0
Reset Value: 0
Continuous control
Velocity (Load with preset)
When the Velocity button is checked, the Velocity setting does not change when a preset is loaded. When the box is
unchecked, the velocity setting loads to the value specified by the preset.

<!-- page 20 -->

Clavinet / User Guide

20
CHAPTER 4 Clavinet Standalone Application
The Clavinet application can be used as a standalone instrument. It requires ASIO drivers for Windows or Core Audio for
macOS. Clavinet.exe (Win) or Clavinet.app (Mac) loads the Clavinet instrument and configuration preferences dialogs.
Set up the standalone application from its File menu:
• All Notes Off

Sends an All-Notes-Off MIDI command to the Clavinet synthesizer. This is useful in
cases of “stuck” sustaining notes.
• Preferences
Displays the Preferences dialog for the Audio, MIDI, and User Choices configurations.
PREFERENCES
Output displays the audio devices available on the system.
Test plays a sound if the outputs are configured correctly.
Active Output Channels allows selection of audio outputs
from the selected device.
Sample Rate displays and sets the sample rate.*
Audio Buffer Size displays and sets the buffer size, which
influences latency.*
*In Windows, sample rate and buffer size cannot be changed
from this panel. To modify these settings: close the
application, adjust sample rate and buffer size with your
driver's control panel (link shown below), and then relaunch.


(Windows Only)

Active MIDI Inputs displays a list of available MIDI input devices on the current
system. Select the MIDI device for receiving MIDI data.
Tempo: Sets the tempo for all relevant plugins. By default, tempo-based Waves
plugins are in a “tempo listen” state. Their tempo rates will fix to this value.