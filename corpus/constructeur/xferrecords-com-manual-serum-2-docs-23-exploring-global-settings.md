---
titre: "xferrecords com manual serum 2 docs — Exploring Global Settings (p. 312-322)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Exploring Global Settings


<!-- page 312 -->

Serum 2 User Guide
312
Exploring Global Settings
You can use the GLOBAL module to configure global settings in Serum.
There are two types of global settings: those saved with your preset, song, or patch, and those saved as
part of Serum, accessible to all presets.
Serum Global Settings
Using the Global Module
Click the GLOBAL tab to access the module.
Accessing Serum Global Settings
The global settings page appears.

<!-- page 313 -->

﻿
Exploring Global Settings
Serum 2 User Guide
313
The page is divided into the following panes to help you quickly find the appropriate settings:
•	 Preferences — Specify global preferences including user interface and MPE settings
•	 Voice Control — Define the behavior of each voice across the available oscillators
•	 Quality — Set the render quality and Serum 1 compatibility
•	 Tuning — Set the concert pitch and manage Serum tuning
The settings page also displays the current Serum version and build date.
Preferences
Use the PREFERENCES pane
to configure your global
preferences in Serum.
This includes default
waveform display, user
interface options, and
double-click
behavior, among other
settings.
The following table describes the preferences you can set.
Category
Preference
Description
User Interface
Help Tooltips
Display tooltips after hovering the mouse
pointer over a control for a moment.
Param value tooltips
Display numeric values (as a small pop-up)
when modifying a control.
Double-click params
Specify whether double-clicking a control
resets the control to the default (init) value
or whether double-clicking displays a pop-up
text box allowing you to type a specific value.
Serum Global Preferences

<!-- page 314 -->

﻿
Exploring Global Settings
Serum 2 User Guide
314
Category
Preference
Description
User Interface
(cont.)
Mouse wheel param control
By default, moving the mouse wheel adjusts
the knob that the cursor is currently hovering
over. If you don’t want this capability, enable
this setting to deactivate the feature.
Keyboard shortcuts
Set whether Serum should respond to input
from the computer keyboard. Disable this to
prevent Serum from stealing keyboard focus
from your DAW.
Default waveform view
The default waveform view in the OSC
panels, either 2D (default) or 3D.
MPE
MPE enabled by default
Specify whether MPE mode is enabled when
a new instance of Serum is added to your
project.
MPE Pitch Bend (also)
maps to Expr X
By default, Serum maps MIDI pitch bend
messages to per-note pitch bend and CC10
(pan) messages to note expression X.
Some MPE controllers use the X axis (left/
right movements) to control pitch and will
therefore transmit pitch bend messages.
Select this option to have these gestures
mapped to note expression X in Serum, as
well as to per-note pitch bend.
MPE Expr Y acts
bi-directional
Specify whether note expression Y is treated
as unipolar or bipolar. This allows you to
match how your DAW or MPE controller
treats note expression Y.
General
Limit Mod depth on drop
(based on knob value)
When a modulator source is dropped on a
knob, reduce the range amount (if needed)
so that the modulation does not exceed the
maximum value for the range.
For instance, if you drag a modulator to
an oscillator LEVEL knob set at 75%, the
assigned modulation depth will only be 25%
(so that a maximum modulator will have
volume reach exactly 100%).

<!-- page 315 -->

﻿
Exploring Global Settings
Serum 2 User Guide
315
Category
Preference
Description
General (cont.)
Mod Wheel -> WT Pos
(when WT Editor is open)
When the Wavetable Editor is active, the
mod wheel scans the indices from 1-256.
Silence note + FX tails when
host transport stops
Mute effects and any sustaining notes when
the host DAW is stopped.
Load MIDI Map from
Presets
Normally, Serum loads a default MIDI CC
map if the Serum 2 Presets/System/
MIDI CC Maps/Default.SerumMIDIMap is
found, in the following cases:
•	 When creating a new instance of Serum
•	 When selecting the Init preset
•	 When loading a preset
When the Load MIDI Map from Presets
option is enabled, loading a preset causes
Serum to load the MIDI CC mapping that
was saved with the preset instead of the
default.
You might want to enable this option if you
have a specific mapping for FX parameters
that you want to recall, for instance.
Use Ultra quality when
rendering
Instruct Serum to perform an offline render
(bounce) using ultra quality mode. This
results in the highest quality playback of the
rendered sound.
Since the rendering is performed offline, the
performance trade off in using ultra quality
mode for renders generally makes sense.
Automatically check for
updates
Enable to ensure that you are notified when
new versions of Serum become available.

<!-- page 316 -->

﻿
Exploring Global Settings
Serum 2 User Guide
316
Setting the Voice Control
You can specify voice control
settings for Serum to define the
behavior of each voice across the
available oscillators.
Select the oscillators to which the
voice control settings apply. By
default, all oscillators are selected
(green).
Select the Oscillators
Loading a Preset
You can optionally load a factory
supplied or user-defined preset.
Click the voice control (topmost)
field and choose a preset using the
menu that appears.
The configuration loads and
populates the relevant settings.
Voice Control Settings
Voice Control Menu

<!-- page 317 -->

﻿
Exploring Global Settings
Serum 2 User Guide
317
Creating a New Configuration
You can create a new configuration, or reinitialize the voice control, at any time.
Click the voice control field and
choose Init in the menu.
This initializes the voice control to
the default settings and provides
an opportunity for you to create a
new configuration.
Configuring the Voice Control
Click one of the numbers, from 1
to 8, to set the sequence length.
Select one of the SEQ controls and
adjust the per voice settings.
Continue setting the other
controls, as appropriate.
Initializing the Configuration
Per Voice Settings

<!-- page 318 -->

﻿
Exploring Global Settings
Serum 2 User Guide
318
Setting Randomization
You can set the randomization for
the PAN, DETUNE, CUTOFF, and
ENVS (envelopes).
Click the corresponding RANDOM
field and drag to set the value. You
can also double-click the field and
type a value.
The following table outlines the randomization effect:
Field
Description
PAN
Randomizes the stereo position, per voice (as a percentage).
DETUNE
Randomizes the tuning offset, per voice (in cents).
CUTOFF
Randomizes the filter cutoff, per voice (as a percentage).
ENVS
Randomizes the envelope offset, per voice (as a percentage).
Setting the Scaling
You can set the scaling for all
envelopes and LFOs.
To set the scaling for all envelopes,
click the field and drag up or down.
You can use the arrow keys to fine tune the setting. You can also double-click the field and type a value.
This is useful if you change the BPM (beats per minute).
To set the LFO scaling, click the field and drag up or down. You can use the arrow keys to fine tune the
setting. You can also double-click the field and type a value. Choose to set by percentage or rate.
This is helpful for creating many simultaneous pattern changes.
Setting Randomization
Scaling Settings

<!-- page 319 -->

﻿
Exploring Global Settings
Serum 2 User Guide
319
Saving the Voice Control Settings
Click the
 button to save the voice control settings. A dialog appears allowing you to specify a
name.
Setting the Quality
You can specify the quality
(oversampling) in Serum.
You can further disable smoothing, as
needed, and enable Serum 1 preset
compatibility.
Choose the oversampling quality settings
using the drop-down menu.
Draft quality sets 1x oversampling (no
oversampling). High quality sets 2x
oversampling, while Ultra results in 4x
oversampling.
Click the
 button to lock the
quality settings, even when you load a
new preset.
This means that when locked, Serum
ignores the quality configuration in the
preset and uses the settings that you
have locked.
You can also set the following quality settings:
Setting
Description
S1 Compatibility
Mode
Serum 2 features a completely rebuilt sound engine. However, when you
load a Serum 1 preset, this option is automatically enabled to preserve
maximum sonic similarity with Serum 1.
Disable this option if you prefer that Serum 1 presets instead take advantage
of the DSP updates available in the Serum 2 sound engine.
Quality Settings
Quality Settings

<!-- page 320 -->

﻿
Exploring Global Settings
Serum 2 User Guide
320
Setting
Description
Disable Smoothing
Disable automation parameter smoothing.
While Serum is built to try to avoid clicks and jumps in the signal, there are
times when you might want precision over parameter changes (for instance,
during fast rhythmic automation). In this case, you can choose to disable
smoothing (Serum supports sample-accurate automation).
Note: Smoothing also applies to parameter changes effected through mouse
actions on on-screen controls.
Setting the Tuning
You can specify the tuning for Serum, including setting the concert pitch and managing tuning using a
tuning file.
Setting Concert Pitch
Concert pitch is the standard reference
pitch used to tune musical instruments.
The most widely accepted concert
pitch is A4 at 440 Hz, where the A4
refers to the A above middle C (the
fourth A key on a piano).
To set the concert pitch for Serum, click the left field and drag up or down. You can use the arrow keys
to fine tune the setting. You can also double-click the field and type a value.
Using a Tuning File
You can also set the tuning using
a tuning file. Serum offers two
options.
You can load a tuning file for the
current instance of Serum, or you
can have the Serum instance
follow the tuning specified
elsewhere in your project using
MTS-ESP.
To set the tuning file for the Serum
instance, click the TUN FILE field
and choose Load Tuning in the
menu that appears. A dialog appears allowing you to locate the appropriate tuning (.tun) file. To clear the
tuning file, use the same menu and choose Clear Tuning in the menu.
Tuning Settings
Tuning Menu

<!-- page 321 -->

﻿
Exploring Global Settings
Serum 2 User Guide
321
Using MTS-ESP to Set the Tuning
You can load a separate tuning file for each instance of Serum (using the procedure described in the
previous section). However, if you would like to use a single main tuning file across all instances, Serum
supports the MTS-ESP microtuning system developed by ODDSOUND (www.oddsound.com).
Using the free MTS-ESP MINI plugin, you can load .scl, .kbm or .tun files and automatically retune
all connected MTS-ESP clients (including Serum). This allows you to retune any number of supported
virtual instruments from a central location without requiring you to tune each instrument separately.
MTS-ESP support is enabled in Serum by default. You can disable this feature by unchecking the Enable
MTS-ESP menu option.
Enable the MTS-ESP Note-On Only option to have the tuning set on Note-On MIDI events. This
ensures that the tuning of a note will not change during its duration, even if the global MTS-ESP tuning
updates.
Note the following about using MTS-ESP:
•	 Loading a .tun file always takes precedence over MTS-ESP. This allows you to tune any Serum
instance differently from the global MTS-ESP tuning.
•	 If the oscillator pitch mode is set to Steps (set by right-clicking an oscillator OCT or SEM control),
you can pitch oscillators up or down in “periods” and “steps” as defined by the active MTS-ESP
tuning, rather than in octaves or semitones.
In addition to the free MTS-ESP MINI plugin, you can choose from among the following additional
MTS-ESP plugin options:
•	 Wilsonic MTS-ESP
•	 Surge XT
•	 Entonal Studio
•	 Infinitone
Locking the Tuning Configuration
Click the
 button to lock the tuning configuration, even when you load a new preset.
This means that when locked, Serum ignores the TUN file and the concert pitch setting in any new
preset that you load.

<!-- page 322 -->

﻿
Exploring Global Settings
Serum 2 User Guide
322
Checking the Build Version and Date
You can quickly check the version of
Serum that you’re running using the
Xfer pane.
Be sure to refer to this version number
if you reach out to Xfer Records for
technical support.
Serum Build and Date