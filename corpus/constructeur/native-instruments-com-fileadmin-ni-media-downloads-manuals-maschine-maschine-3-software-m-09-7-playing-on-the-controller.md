---
titre: "Maschine Software Manual — 7. Playing on the controller (p. 121-140)"
source: constructeur/native-instruments-com-fileadmin-ni-media-downloads-manuals-maschine-maschine-3-software-m.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# 7. Playing on the controller


<!-- page 121 -->

7. Playing on the controller
This chapter describes the numerous features available in Maschine to adjust and enhance your
playing on the controller, both during live performances and when recording Patterns.
Adjusting the pads
You can optimize and fine-tune the way the pads of your controller react to your playing:
•
Choose a pad mode that best fits your playing needs: ???.
•
Adjust the base key to set the pitch of the notes played by your pads: Adjusting the base key.
•
Set Choke groups to selectively cancel Sounds when other Sounds are triggered: Using Choke
groups.
•
Create Link groups to trigger several Sounds by pressing only one pad: Using Link groups.
The Pad view in the software
In the software the settings for your pads are available in the Pad view, which is activated via the
Pad View button above the Sound List in the Pattern Editor:
The Pad View button.
▶Click the Pad View button to show or hide the Pad view.
When the Pad View button is activated, the Pad view replaces the Sound List below:
The Pad view replaces the Sound List.
At the top of the Pad view, the grid of pads gives you access to all Sound slots of the current
Group. The focused pad is fully lit; other pads containing a Sound are dim-lit; pads without any
Sound are off. The following actions are available in the grid:
•
Click any pad to select the corresponding Sound slot. Upon selection, the parameters
underneath, as well as the Control area above are updated accordingly.
•
Drag and drop a pad to move it to another location in the grid. This is strictly equivalent to
moving Sound slots in the Sound List. For more information, refer to Moving Sounds.
PLAYING ON THE CONTROLLER 118

<!-- page 122 -->

•
Right-click ([Ctrl]-click on macOS) any pad to open the same context menu as in the Sound List.
For more information, refer to Managing Sounds.
You can select multiple pads in the grid of pads as you can in the Sound List,
and adjust parameters in the Pad view and in the Control area for all of them
simultaneously. For more information on multiple selection, refer to section Selecting
multiple Sounds or Groups.
Under the grid of pads, you find the following parameters:
Parameter
Description
Key
Adjusts the base key for the selected pad. For more information, refer to
Adjusting the base key.
Choke
Configures the Choke Group for the selected pad. For more information, refer to
Using Choke groups.
Link
Configures Pad Link for the selected pad. For more information, refer to Using
Link groups.
Adjusting the base key
With the pads in Group mode, the base key defines the key (or pitch) at which each Sound will be
played when its pad is pressed. With the pads in Keyboard mode, it defines the key played by pad 1
on your controller; pads 2–16 will then play keys included in the current scalerelatively to the base
key .
The base key also affects the pitch of events created via the step sequencer. See
section ??? for more information on this.
Adjusting the base key only affects the notes played by the pads of your controller.
It does not affect the notes recorded in your Patterns. For more information on
adjusting the key of notes in Patterns, refer to Editing events.
You can select multiple pads and quickly change the base key for all of them at once.
Refer to Selecting multiple Sounds or Groups for more information.
Adjusting the base key in the software
By default, the base key of every Sound slot is C3 (i.e. middle C in the Maschine convention). To
change the base key of the selected pad(s) / Sound slot(s) in the software:
1. Click the Pad View button above the Sound List in the Pattern Editor to show the Pad view for
the focused Group.
2. Click the Key value and drag your mouse vertically, or double-click it, enter a new value on your
computer keyboard, and press [Enter] to confirm.
PLAYING ON THE CONTROLLER 119

<!-- page 123 -->

Using Choke groups
When your pads are in Group mode, Choke groups allow you to build sets of “mutually exclusive”
pads: A Choke group lets you force each newly triggered Sound to cancel out all other Sounds still
playing — in other terms, these Sounds would never play together, the newer Sound automatically
“killing” the audio of the older one. This is a behavior you can find in vintage drum machines
(typically used to “choke” the open hi-hat with the closed one), but also in monophonic synthesizers
that are only capable of playing one note at a time.
Within a Group, each pad can be assigned to one of eight Choke groups. When you assign a pad to
a Choke group, the pad may be set as a Send or Receive in the Choke group:
•
If the pad is set to Send (default setting) it will kill the Sounds of other pads in the same Choke
group.
•
If the pad is set to Receive it will not kill any other pad of the Choke group — but it will be killed
by pads set to Send within the same Choke group.
You may set more than one pad as Send or Receive within the same group.
Choke groups affect not only the notes you play on the pads and the notes triggered
by the Patterns, but also the MIDI notes controlling your Sounds.
You can select multiple Sounds and quickly assign them all to a particular Choke
group at once.
To assign the selected Sound slot(s) to a Choke group and set its/their Choke mode (Send or
Receive), do the following:
1. Click the Pad View button above the Sound List in the Pattern Editor to show the Pad view for
the focused Group.
2. In the Choke section click the Group value (left value) and select the desired group 1–8 from
the list, or choose None (default setting) to remove the Sound from its current Choke group.
3. In the same Choke section click the Mode value (right value) to switch the Sound between
Send (default setting) and Receive mode.
4. Repeat the steps above to assign other pads to the same Choke group.
The Hi-hat is an ideal candidate for making use of Choke groups: By setting the closed
and open hi-hat Sounds to the same Choke group with the closed hi-hat set to Send
mode, any sounding open hi-hat will be interrupted by the next closed hi-hat, as on a
real drum set.
Using Link groups
When your pads are in Group mode, Link groups allow you to link pads with each other: this can be
used to trigger multiple Sounds when pressing only one pad. Each pad of a Group can be assigned
to one of eight Link groups. A pad may be set as a Send or Receive in the Link group:
•
If the pad is set to Send (default setting) it will trigger other pads in the same Link group.
•
If the pad is set to Receive it will only trigger its own Sound, even if it is part of a Link group —
but it will be triggered by pads set to Send within the same Link group.
PLAYING ON THE CONTROLLER 120

<!-- page 124 -->

You may set more than one pad as Send or Receive within the same group.
Link groups affect not only the notes you play on the pads and the notes triggered by
the Patterns, but also the MIDI notes controlling your Sounds.
Link groups are a “live” feature: They only affect the note triggers. In Record mode, Link
groups don’t affect the notes recorded in your Patterns — in other terms notes will
not be recorded for the linked pads. Notably, this allow you to modify your Link group
assignments after recording. If you want to copy the notes from a Sound to another
Sound in Patterns, please refer to section Editing events.
You can select multiple Sound slots and quickly assign them all to a particular Link
group at once.
To assign the selected Sound(s) to a Link group and set its/their Link mode (Send or Receive), do
the following:
1. Click the Pad View button above the Sound List in the Pattern Editor to show the Pad view for
the focused Group.
2. In the Link section click the Group value (left value) and select the desired group 1–8 from the
list, or choose None (default setting) to remove the Sound from its current Link group.
3. In the same Link section click the Mode value (right value) to switch the Sound between Send
(default setting) and Receive mode.
A Link group makes sense only if more than one pad/Sound are assigned to it.
Adjusting the Key, Choke, and Link parameters for multiple Sounds
In the software, if you select multiple Sounds with different Key, Choke and/or Link values, the
corresponding parameters in Pad view display MULTI. On your controller with PAD MODE active,
the corresponding parameters now display (MULTI).
You can adjust these parameters for the selected Sounds as described below.
Adjusting the base key for multiple Sounds with different Key values
▶Click and drag the MULTI label next to Key to transpose the base key of all selected Sounds.
While dragging, the field displays a +/-x value indicating the transposition that will apply to all
Sounds as you release the mouse button.
PLAYING ON THE CONTROLLER 121

<!-- page 125 -->

Sound slots 1 to 4 are selected. If they have different Key values, a MULTI label appears (left). When you drag it (middle), a
transpose value appears (right) that will be applied to all selected Sounds when you will release the mouse button.
This is also true when adjusting the parameter from your controller.
Adjusting the Choke or Link group for multiple Sounds with different
Choke or Link groups
▶Click the MULTI label next to Choke or Link and select the desired value from the list to set
all selected Sounds to that same Choke or Link group, respectively. This also applies to the
Send/Receive setting next to it.
Sound slots 1 to 4 are selected. If they have different Choke values, a MULTI label appears (left). When you click it and select a
new Choke or Link group from the list (middle), this new group is applied to all selected Sounds.
This is also true when adjusting the parameter from your controller.
Playing tools
On top of the various pad settings available (see Adjusting the pads), Maschine also offers you a
series of intuitive playing tools particularly useful when playing live:
•
Mute and Solo allow you to selectively mute and solo Sounds and Groups: Mute and Solo.
•
Groove allows you to give a shuffling flair to individual Sounds/Groups or to your entire Project:
Groove.
PLAYING ON THE CONTROLLER 122

<!-- page 126 -->

Mute and Solo
Muting is used to silence a Sound or a Group, whereas Solo is pretty much the opposite: Soloing
a Sound or a Group mutes all other Sounds in that Group or all other Groups, respectively, so that
you can listen to the selected Sound or Group alone. The combination of both is a useful means to
play live and to test different sequences together.
When used on Sounds, the Solo only applies to the current Group: The Sounds in other Groups
won’t be affected.
Audio mute vs. trigger mute
At the Group level, the Mute function is an audio mute: The whole audio output of the muted Group
will be bypassed. At the Sound level, the Mute function is by default a trigger mute: the Pattern
content (the events) for the muted Sound will not be triggered — but any audio remaining from
past events for this Sound will still be audible until it fades away. You can change this behavior
by enabling the Audio Mute button in the Audio page of the Sound’s Output properties (refer to
Configuring the main output of Sounds and Groups) as well as in Solo and Mute mode on your
controller: Activating the audio mute for Sounds will ensure that not only the events are muted, but
any remaining audio as well.
Mute and Solo in the software
We describe here how to mute/solo Groups and Sounds in the Arrange view of the
software, but you can also do this from Mix view via the Mute button available in each
channel strip of the Mixer. See section Adjusting settings in the channel strips for
more information.
Soloing a Sound
1. To solo a Sound, right-click (on macOS: [Ctrl]-click) the number on the left side of the Sound slot
in the Pattern Editor.
Soloing the first kick Sound.
2. To unsolo a Sound, right-click (on macOS: [Ctrl]-click) the number again.
PLAYING ON THE CONTROLLER 123

<!-- page 127 -->

Soloing a Group
1. To solo a Group, right-click (on macOS: [Ctrl]-click) the Group index (letter + number) on the left
side of the Group in the Arranger:
Soloing a Group.
2. To unsolo a Group, right-click (on macOS: [Ctrl]-click) the Group index again.
Muting a Sound
1. To mute a Sound, click the number on the left side of the Sound slot in the Pattern Editor.
Muting a Sound.
2. To unmute the Sound, click the number again.
By default, the Mute on Sounds is an trigger mute: events for muted Sounds are not
triggered, but the audio coming from previous events might still be audible (reverb tail,
etc.). You can also activate audio mute for Sounds to mute both events and audio —
see the beginning of this section for more information.
Muting a Group
1. To mute a Group, click the Group index (letter + number) on the left side of the Group in the
Arranger:
Muting a Group.
PLAYING ON THE CONTROLLER 124

<!-- page 128 -->

2. To unmute the Group, click the Group index again.
Groove
The groove controls the swing, that is the rhythmic relationship between events in the selected
channel (Sound, Group, or Master). By shifting some of the events, you can e.g. give a shuffling,
ternary touch to your Patterns.
The groove can be adjusted for each channel individually via its Groove properties.
A groove configured for a channel affects all its contained channels:
•
The Groove properties of a Sound only affect that particular Sound.
•
The Groove properties of a Group affect all Sounds in that Group: The Group’s swing is added to
the swing of each individual Sound (as defined in its own Groove properties).
•
At the Master level, the Groove properties affect all Sounds of all Groups. The Master’s swing
is added to the swing of each individual Group and Sound (as defined in its own Groove
properties).
The Groove properties have a single Parameter page: Swing.
Please refer to section Navigating Channel properties, Plug-ins, and Parameter pages
to know how to display and navigate sets of Channel properties.
The Groove properties for a Sound in the software.
Control
Description
Swing
section
Amount
Adjusts the amount of swing, i.e. the amount by which some events are
shifted. At 0 % events are not shifted. Raise the Amount value to increase the
strength of the swing.
Cycle
Determines on what musical resolution the groove is applied. This directly
affects which events will be shifted. Values are measured in fractions of a
whole note.
Invert
Allows you to invert the groove so that instead of being delayed in the Pattern,
events will be triggered ahead of time.
How groove affects the rhythm: an example
Take a simple, regular one-bar rhythm with a hit on each eighth note. We set the Cycle parameter
to 1/2, which is one half note, that is two beats.
The following picture shows you how this rhythm would sound with the following settings:
•
Top: Amount at 0.0 % (no groove).
•
Middle: Amount at 100.0 % and Invert off.
PLAYING ON THE CONTROLLER 125

<!-- page 129 -->

•
Bottom: Amount at 100.0 % and Invert activated.
This is how the same regular rhythm would be heard with various groove settings.
The picture above only illustrates how the groove function affects the sound —
adjusting the Groove properties will not effectively move events in the Pattern Editor.
Perform features
The Perform features of Maschine are inspired by similar features available in Komplete Kontrol
and on the Kontrol S-Series keyboards, offering a familiar and seamless workflow.
Overview of the Perform features
The Perform features include the following engines:
•
The Scale and Chords engine allows you to assign the pads to notes within specific scales,
and to play chords according to the selected scale by hitting single pads.
•
The Arp engine allows you to create arpeggios and repeated notes based on the pads you
press or the chord currently triggered.
Designed to enrich the melodic content of your Projects, these engines are available when your
pads are in Keyboard mode. Furthermore, they are designed to be used live and, as such, they are
available only from your hardware controller (like Note Repeat).
When your pads are in Pad Mode, you can use the Note Repeat engine, Choke groups, and Link
groups as in previous Maschine versions.
Control signal flow with pads in Keyboard mode
The following diagram illustrates Maschine’s signal flow between your hits on the pads in Keyboard
mode and the resulting sounds:
PLAYING ON THE CONTROLLER 126

<!-- page 130 -->

The signal flow including the new Perform features (Scale, Chord, and Arp) when your pads are in Keyboard mode.
In this picture, blue cells represent modules sending “control” signals, i.e. triggering messages (e.g.,
the note messages sent by the pads as you press them), whereas red cells represent modules
sending audio signals (e.g., the sounds produced by the Instrument loaded in the Sound slot as it
receives the aforementioned note messages).
In this diagram you will notice the following:
•
The Scale and Chord modules can feed the Arp module, the Scale module can also affect the
Chord module, as we will see later.
•
The notes played on your pads are first sent to the Perform features (Scale, Chord, and Arp
engines), which send the resulting notes to the Pattern Editor. In other terms, you can record
the generated scales, chords or arpeggiated notes into your Patterns. However, the Perform
features do not process the content of your Patterns.
Control signal flow with pads in Group mode
The following diagram illustrates signal flow between your hits on the pads in Group mode and the
resulting sounds:
PLAYING ON THE CONTROLLER 127

<!-- page 131 -->

The signal flow including the Perform features (Note Repeat, Choke Group, and Link Group) when your pads are in Group
mode.
In this picture you will notice the following:
•
Note Repeat takes the place of the Scale, Chord, and Arp modules between the live input on the
pads and the Pattern Editor. In other terms, Note Repeat won’t process your Patterns but you
can record its output into a Pattern.
•
The Choke Group and Link Group modules affect both your hits on the pads and the content of
your Patterns, but their result cannot be recorded into Patterns.
Selecting a scale and creating chords
Maschine comes equipped with a vast amount of scales and chords that you can select and use to
play your Sounds. This opens up possibilities to play an instrument such as a piano according to,
for example, the minor pentatonic scale without hitting a “false” pad (note) on your controller, or to
play chords that always fit by hitting single pads.
The Scale and Chord engine is available only when your pads are in Chord mode.
This section provides a hands-on introduction to the use of scales and chords from your controller.
The corresponding parameters will be described in detail in section Scale and Chord parameters.
Scale and Chord parameters
This section describes the Scale and Chord engine and its parameters. It also provides a list of all
scales and chords available on your controller.
General notes on scales and chords
•
The Scale and Chord parameters are the same for all Sound slots in a particular Group. You can
have different Scale and Chord parameters for each Group. The Scale and Chord parameters of
each Group are saved with the Project. However, when you save a Group, the Scale and Chord
parameters are not saved with the Group.
PLAYING ON THE CONTROLLER 128

<!-- page 132 -->

•
The Scale and Chord engine processes live input from the pads of your controller only. The
Scale and Chord engine do not process input from third-party MIDI controllers and data
recorded in the Pattern Editor.
•
The Scale and Chord engine output is recorded into the Pattern Editor.
•
The Scale and Chord parameters cannot be modulated nor automated in Maschine.
•
If a Sound slot contains a Komplete instrument providing control notes (e.g., key switches) on
particular keys, these notes will not be triggered by the Scale and Chord engine.
Scales
The Scale engine is controlled via two parameters:
•
Root Note (C3 by default): Defines both the root note of the scale and the particular key
triggered by pad 1. As a direct consequence, pad 1 always triggers the root note of the selected
scale.
•
Scale Type (Chromatic by default): Selects the scale pattern whose notes will be mapped onto
the pads of your controller: The Root Note is on pad 1, the 2nd note of the selected Scale
Type is on pad 2, etc. Once all notes are mapped, the next pad triggers the root note in the
next octave. The Root Note and its octaves are indicated by fully lit pads, while other pads are
dimmed.
The following scale types are available:
Main scales
Scale
Bank
Type
Degree formula
Chromatic
Main
Chrom
1 ♭2 2 ♭3 3 4 ♭5 5 ♭6 6 ♭7 7
Major
Main
Major
1 2 3 4 5 6 7
Minor
Main
Minor
1 2 ♭3 4 5 ♭6 ♭7
Harm Min
Main
Harm Min
1 2 ♭3 4 5 ♭6 7
Maj Pent
Main
Maj Pent
1 2 3 5 6
Min Pent
Main
Min Pent
1 ♭3 4 5 ♭7
Blues
Main
Blues
1 ♭3 4 ♯4 5 ♭7
Japanese
Main
Japanese
1 2 ♭3 5 ♭6
Freygish
Main
Freygish
1 ♭2 3 4 5 ♭6 ♭7
Gypsy
Main
Gypsy
1 2 ♭3 ♯4 5 ♭6 7
Arabic
Main
Arabic
1 ♭2 3 4 5 ♭6 7
Altered
Main
Altered
1 ♭2 ♯2 3 ♯4 ♭6 ♭7
Whole Tone
Main
WH Tone
1 2 3 ♯4 ♯5 ♭7
H-W Dim
Main
H-W Dim
1 ♭2 ♯2 3 ♯4 5 6 ♭7
W-H Dim
Main
W-H Dim
1 2 ♭3 4 ♯4 ♯5 6 7
Modes scales:
Scale
Bank
Type
Degree formula
Ionian
Modes
Ionian
1 2 3 4 5 6 7
Dorian
Modes
Dorian
1 2 ♭3 4 5 6 ♭7
PLAYING ON THE CONTROLLER 129

<!-- page 133 -->

Scale
Bank
Type
Degree formula
Phrygian
Modes
Phrygian
1 ♭2 ♭3 4 5 ♭6 ♭7
Lydian
Modes
Lydian
1 2 3 ♯4 5 6 7
Mixolydian
Modes
Mixolyd
1 2 3 4 5 6 ♭7
Aeolian
Modes
Aeolian
1 2 ♭3 4 5 ♭6 ♭7
Locrian
Modes
Locrian
1 ♭2 ♭3 4 ♭5 ♭6 ♭7
Ionian b2
Modes
Ion b2
1 ♭2 3 4 5 6 7
Dorian b5
Modes
Dor b5
1 2 ♭3 4 ♭5 6 ♭7
Harm Phryg
Modes
Har Phry
1 ♭2 ♭3 4 5 ♭6 7
Phryg Major
Modes
Phry Maj
1 ♭2 ♭3 4 5 6 7
Lydian b3
Modes
Lyd b3
1 2 ♭3 ♯4 5 6 7
Major Locrian
Modes
Maj Loc
1 2 3 4 ♭5 ♭6 ♭7
Minor Locrian
Modes
Min Loc
1 2 ♭3 4 ♭5 ♭6 ♭7
Super Locrian
Modes
Sup Loc
1 ♭2 ♭3 ♭4 ♭5 ♭6 ♭7
Jazz scales
Scale
Bank
Type
Degree formula
Lydian ♭7
Jazz
Lyd ♭7
1 2 3 ♯4 5 6 ♭7
Altered
Jazz
Altered
1 ♭2 ♯2 3 ♯4 ♭6 ♭7
Diminished
Jazz
Diminshd
1 ♭2 ♯2 3 ♯4 5 6 ♭7
Mixo b13
Jazz
Mix b13
1 2 3 4 5 ♭6 ♭7
Mixo b9 b13
Jazz
Mixb9b13
1 ♭2 3 4 5 ♭6 ♭7
Lydian ♭7 b2
Jazz
Lyd ♭7b2
1 ♭2 3 ♯4 5 6 ♭7
Bebop
Jazz
Bebop
1 2 3 4 5 6 ♭7 7
Whole Tone
Jazz
Whole Tn
1 2 3 ♯4 ♯5 ♭7
Blues Maj
Jazz
Blues Ma
1 2 ♭3 3 5 6
Blues Min
Jazz
Blues Mi
1 ♭3 4 ♯4 5 ♭7
Blues Combined
Jazz
BluesCmb
1 2 ♭3 3 4 ♯4 5 6 ♭7
Lydian #5
Jazz
Lyd #5
1 2 3 ♯4 ♯5 6 7
Jazz Minor
Jazz
Jazz Mi
1 2 ♭3 4 5 6 7
Half Dim
Jazz
Half Dim
1 2 ♭3 4 ♭5 ♭6 ♭7
Augmented
Jazz
Augmentd
1 ♭3 3 5 ♯5 7
World scales
Scale
Bank
Type
Degree formula
Hungarian Min
World
Hung Min
1 2 ♭3 ♯4 5 ♭6 7
Hungarian Maj
World
Hung Maj
1 ♯2 3 ♯4 5 6 ♭7
Neapolitan
World
Neapoltn
1 ♭2 ♭3 4 5 ♭6 7
Spanish
World
Spanish
1 ♭2 ♭3 3 4 5 ♭6 ♭7
PLAYING ON THE CONTROLLER 130

<!-- page 134 -->

Scale
Bank
Type
Degree formula
Greek
World
Greek
1 2 ♭3 ♭4 5 ♭6 ♭7
Jewish 1
World
Jewish 1
1 ♭2 3 4 5 ♭6 ♭7
Jewish 2
World
Jewish 2
1 2 ♭3 ♯4 5 6 ♭7
Indian 1
World
Indian 1
1 ♭2 ♭3 ♯4 5 ♭6 7
Indian 2
World
Indian 2
1 2 ♭3 ♯4 5 6 7
Indian 3
World
Indian 3
1 ♭2 2 4 5 ♭6 6
Indian 4
World
Indian 4
1 ♯2 3 4 5 ♯6 7
Mid East 1
World
M East 1
1 ♭2 3 4 5 ♭6 7
Mid East 2
World
M East 2
1 ♭2 3 4 ♭5 ♭6 7
Mid East 3
World
M East 3
1 ♭2 ♭3 4 ♭5 6 ♭7
Mid East 4
World
M East 4
1 ♭2 3 4 ♭5 6 ♭7
5-Tone scales
Scale
Bank
Type
Degree formula
Penta I
5-Tone
Pent I
1 2 3 5 6
Penta II
5-Tone
Pent II
1 2 4 5 ♭7
Penta III
5-Tone
Pent III
1 ♭3 4 ♭6 ♭7
Penta IV
5-Tone
Pent IV
1 2 4 5 6
Penta V
5-Tone
Pent V
1 ♭3 4 5 ♭7
Hirajoshi
5-Tone
Hira
1 2 ♭3 5 b6
Insen
5-Tone
Insen
1 ♭2 4 5 ♭7
Kokin Joshi
5-Tone
Kokin
1 2 4 5 b6
Akebono
5-Tone
Akebono
1 2 ♭3 5 6
Ryukuan
5-Tone
Ryukuan
1 3 4 5 7
Abhogi
5-Tone
Abhogi
1 2 ♭3 4 6
Bhupkali
5-Tone
Bhupkali
1 2 3 5 b6
Hindolam
5-Tone
Hindolam
1 ♭3 4 ♭6 ♭7
Bhupalam
5-Tone
Bhupalam
1 ♭2 ♭3 5 b6
Amritavarshini
5-Tone
Amrita
1 3 ♯4 5 7
Modern scales
Scale
Bank
Type
Degree formula
Octatonic
Modern
Octatonc
1 2 ♭3 4 ♯4 ♯5 6 7
Acoustic
Modern
Acoustic
1 2 3 ♯4 5 6 ♭7
Augmented
Modern
Augmentd
1 ♭3 3 5 ♯5 7
Tritone
Modern
Tritone
1 ♭2 3 ♭5 5 ♭7
Leading Wh Tone
Modern
Lead Wh
1 2 3 ♯4 ♯5 ♯6 7
Enigmatic
Modern
Enigmatc
1 ♭2 3 ♯4 ♯5 ♯6 7
PLAYING ON THE CONTROLLER 131

<!-- page 135 -->

Scale
Bank
Type
Degree formula
Scriabin
Modern
Scriabin
1 2 3 ♯4 6 ♭7
Tcherepnin
Modern
Tcherepn
1 ♯1 ♯2 3 4 5 ♯5 6 7
Messiaen I
Modern
Mes I
1 2 3 ♯4 ♯5 #6
Messiaen II
Modern
Mes II
1 ♭2 ♯2 3 ♯4 5 6 ♭7
Messiaen III
Modern
Mes III
1 2 ♭3 3 ♯4 5 ♭6 ♭7 7
Messiaen IV
Modern
Mes IV
1 ♭2 2 4 ♯4 5 ♭6 7
Messiaen V
Modern
Mes V
1 ♭2 4 ♯4 5 7
Messiaen VI
Modern
Mes VI
1 2 3 4 ♯4 ♯5 ♯6 7
Messiaen VII
Modern
Mes VII
1 ♭2 2 ♭3 4 ♯4 5 ♭6 6 7
Major scales
Scale
Bank
Type
Degree formula
Natural
Major
Natural
1 2 3 4 5 6 7
Lydian
Major
Lydian
1 2 3 ♯4 5 6 7
Mixolydian
Major
Mixolyd
1 2 3 4 5 6 ♭7
Major Minor
Major
Maj Min
1 2 3 4 5 ♭6 ♭7
Harmonic Major
Major
Har Maj
1 2 3 4 5 ♭6 7
Dbl Har Major
Major
Dbl Maj
1 ♭2 3 4 5 ♭6 7
Neapolitan Maj
Major
Nea Maj
1 ♭2 3 4 5 6 7
Major Locrian
Major
Maj Loc
1 2 3 4 ♭5 ♭6 ♭7
Blues Major
Major
Blues Ma
1 2 ♭3 3 5 6
Bebop Major
Major
Bebop Ma
1 2 3 4 5 ♯5 6 7
Hexa 1
Major
Hexa 1
1 2 3 5 6 7
Hexa 2
Major
Hexa 2
1 2 3 4 5 6
Penta 1
Major
Penta 1
1 2 3 5 6
Penta 2
Major
Penta 2
1 3 4 5 7
Penta 3
Major
Penta 3
1 3 5 6 7
Minor scales
Scale
Bank
Type
Degree formula
Natural
Minor
Natural
1 2 ♭3 4 5 ♭6 ♭7
Dorian
Minor
Dorian
1 2 ♭3 4 5 6 ♭7
Phrygian
Minor
Phrygian
1 ♭2 ♭3 4 5 ♭6 ♭7
Minor Major
Minor
Min Maj
1 2 ♭3 4 5 6 7
Harmonic Minor
Minor
Har Min
1 2 ♭3 4 5 ♭6 7
Dbl Har Minor
Minor
Dbl Min
1 2 ♭3 ♯4 5 ♭6 7
Neapolitan Min
Minor
Nea Min
1 ♭2 ♭3 4 5 ♭6 7
Minor Locrian
Minor
Min Loc
1 2 ♭3 4 ♭5 ♭6 ♭7
PLAYING ON THE CONTROLLER 132

<!-- page 136 -->

Scale
Bank
Type
Degree formula
Blues Min
Minor
Blues Mi
1 ♭3 4 ♯4 5 ♭7
Bebop Minor
Minor
Bebop Mi
1 2 ♭3 4 5 ♭6 ♭7 7
Hexa 1
Minor
Hexa 1
1 2 ♭3 5 ♭6 ♭7
Hexa 2
Minor
Hexa 2
1 2 ♭3 4 5 b6
Penta 1
Minor
Penta 1
1 2 ♭3 5 b6
Penta 2
Minor
Penta 2
1 ♭3 4 5 ♭7
Penta 3
Minor
Penta 3
1 ♭3 5 ♭6 ♭7
By default, the Chromatic scale is selected — in other terms, by default your pads play every
semitone, however, the last selected Scale is automatically assigned when a new Group is created.
The Scale Type parameter is not available if the Chord Mode parameter is set to Chord
Set.
Available chords
The Chord engine can automatically generate chords depending on the selected scale and the
pads you press. The Chord engine is controlled using the following parameters:
•
Chord Mode (Off by default): Selects from three different modes for generating chords:
•
Off: No chords will be generated. Only the notes corresponding to the pads that you hit will
be played.
•
Harmonizer: Generates chords based on the pads you hit and uses notes from the selected
scale, as specified by the Root Note and Scale Type parameters (see above). Use the Chord
Type parameter to choose the particular notes to be used in the chord (see below). As the
chord is triggered, pads of all included notes flash.
•
Chord Set: This special mode maps a set of chords onto the first 12 pads of your controller.
These chords are not bound to any scale type, and they are only affected by the selected
Root Note. Use the Chord Type parameter to choose a particular set of chords to be
mapped onto the pads (see below). In this mode, only the pad you actuate flashes.
•
Chord Type: Selects which chords will be mapped to your pads. The available chord types
depend on the selected Chord Mode and Scale Type:
•
Harmonizer: Offers different chords depending on whether Scale Type is set to Chromatic
or to any other scale. All available chords are listed in the tables below.
•
Chord Set: Provides 16 different sets of 12 chords each (8 major sets and 8 minor sets):
Major 1, Major 2, …, Major 8, and Minor 1, Minor 2, …, Minor 8. The 12 chords are mapped
onto the first 12 pads. Pads 13–16 are deactivated.
•
Position: Spreads the notes of a chord generated from a single note to aid a more musical
transition between chords. Refer to Position.
•
Fixed Velocity: Sets the value for the fixed velocity function, activated using the FIXED VEL
button.
When Chord Mode is set to Harmonizer and Scale Type is set to Chromatic, all semitones are
included in the scale, and therefore chords can use any of them. Chord Type offers the following
chords:
PLAYING ON THE CONTROLLER 133

<!-- page 137 -->

Chord Type
Semitones added above played note
Octave
12
Perfect 4
5
Perfect 5
7
Major
4 and 7
Minor
3 and 7
Suspended 4
5 and 7
Major 7
4, 7, and 11
Minor 7
3, 7, and 10
Dominant 7
4, 7, and 10
Dominant 9
4, 7, 10, and 14
Minor 7♭5
3, 6, and 10
Diminished 7
3, 6, and 9
Augmented
4 and 8
Quartal
5, 10, and 15
Trichord
5 and 11
When Chord Mode is set to Harmonizer and Scale Type is set to any other scale than Chromatic,
the chords are bound to the particular notes included in the specified scale. Chord Type offers the
following chords:
Chord Type
Notes added to played note
Octave
Octave
1-3
3rd
1-5
5th
1-3-5
3rd and 5th
1-4-5
4th and 5th
1-3-5-7
3rd, 5th, and 7th
1-4-7
4th and 7th
Position
If all chords are played in their root position, they can sound quite choppy, especially if you play
chords with large distances between each other in the scale. However, the Position parameter
changes the order and spreads the notes of a chord generated from a single note to create chord
inversions. These inversions create a more pleasing and musical transition between chords, with
the Auto option providing the best results.
The Position parameter contains the following options:
Position
Description
Root
The root position of the selected chord is always played.
-1 to -8
Decreasing Position with negative values moves the highest note of the current
chord down by an octave. This inverts the chord to a lower position in the selected
scale.
PLAYING ON THE CONTROLLER 134

<!-- page 138 -->

Position
Description
+1 to +8
Increasing Position with positive values moves the lowest note of the current
chord up by an octave. This inverts the chord to a higher position in the selected
scale.
Auto
This provides a more human feel in the transition from one chord to another. The
notes used to form each chord are automatically selected to provide the best
inversion.
Scales and Chords: visual feedback on the pads
When scales and/or chords are activated, the LEDs of the pads keep you informed at any time on
the current scale and chord configuration. The default lighting behavior of your pads is modified by
the Scale and Chord engine as follows:
When Chord Mode is set to Off or Harmonizer, pads of root notes are fully lit:
Type of pad (for selected scale)
LED in default state
LED when pad triggered
Root notes
Fully lit
Flash
Other pads
Dimly lit
Flash
Note that if Chord Mode is set to Harmonizer, pads triggered as part of the chord will also flash.
When Chord Mode is set to Chord Set, pad 1 is fully lit:
Type of pad
LED in default state
LED when pad triggered
Pad 1
Fully lit
Flash
Pads 2–12
Dimly lit
Flash
Pads 13–16
Off (pad inactive)
Enharmonic spelling of the root note
On your controller, depending on the Scale Type, Chord Mode, and Chord Type you have selected,
the enharmonic spelling of the Root Note will vary to optimize the spelling of the entire scale/chord
set:
Condition
Enharmonic
spelling
Scale
Type is
set to
Chromatic
All Keys
C
C#
D
D#
E
F
F#
G
G#
A
A#
Scale
Type is
not set to
Chromatic
C
C#
D
E♭
E
F
F#
G
A♭
A
B♭
B
PLAYING ON THE CONTROLLER 135

<!-- page 139 -->

Condition
Enharmonic
spelling
Chord
Mode is
set to
Chord Set
and Chord
Type is
set to
Major 1-8
C
D♭
D
E♭
E
F
F#
G
A♭
A
B♭
B
Chord
Mode is
set to
Chord Set
and Chord
Type is
set to
Minor 1-8
C
C#
D
D#
E
F
F#
G
G#
A
B♭
B
Erasing notes
When erasing notes from your controller, the Chord Mode determines which notes are deleted.
These options include:
•
Off: Notes with the pitch corresponding to the pressed pad are deleted.
•
Harmonizer: Only the notes with the pitch of the pressed pad are deleted. The other notes in
the triggered chord are˝ not deleted.
•
Chord Set: No notes are deleted, in other words erasing is deactivated.
Creating arpeggios and repeated notes
Maschine includes a flexible and versatile Arp engine, an arpeggiator that effectively lets you play
your Sounds in note sequences. The arpeggios are created according to both the pads you hold
and the chords configured with the Scale and Chord engine (refer to Selecting a scale and creating
chords).
If you have activated chords, you can even press more than one pad to include the
notes of all corresponding chords into your arpeggio.
Like the Scale and Chord engine, the Arp engine is dedicated to Keyboard mode.
The Arp engine can be seen as a melodic extension of the Note Repeat: Arp replaces and extends
Note Repeat in Keyboard mode. Instead of playing repeated notes at a constant pitch you can play
sequences of notes at different pitches.
Arp and Note Repeat have similar modes on your controller: Depending on whether your pads are
in Pad Mode or Keyboard mode, pressing NOTE REPEAT on your controller will switch to Note
Repeat mode or Arp mode, respectively. Arp mode simply adds a few parameters to those found in
Note Repeat mode.
PLAYING ON THE CONTROLLER 136

<!-- page 140 -->

General notes on the Note Repeat and Arp engine
•
The Note Repeat / Arp parameters are the same for all Sound slots in all Groups of your
Project. These parameters are saved with the Project.
•
The Note Repeat / Arp engine processes live input from the pads of your controller only. Input
from third-party MIDI controllers and data recorded in the Pattern Editor is not processed by the
Scale and Chord engine.
•
The Note Repeat / Arp engine detects and makes use of any changes in the pressure you apply
on every single pad you hold (Polyphonic Aftertouch). This allows you to generate arpeggios
and repeated notes with varying velocities!
•
The output of the Note Repeat / Arp engine is recorded into the Pattern Editor.
•
The Note Repeat / Arp parameters cannot be modulated nor automated in Maschine.
•
You can use Note Repeat and Arp even if the transport is not running: In this case, the Note
Repeat / Arp engine will use its own central clock. This clock will be reset as soon as you start
the playback.
Kontrol S-Series owners: The central clock is shared by all connected devices so that
e.g. repeated notes triggered from your Maschine controller and arpeggios triggered
from your Kontrol S-Series keyboard will be synchronized even if the transport is not
running.
Swing on Note Repeat / Arp output
The Swing engines (at the Master, Group, and Sound levels) process notes coming from the
Pattern Editor and from the Arp engine (pads in Keyboard mode) or Note Repeat engine (pads
in Group mode). In other terms, the swing is applied not only to your Patterns but also to any live
sequence generated by the Arp or Note Repeat engine.
The applied swing is not recorded in the Pattern Editor. For an overview of the signal
flow starting from your pads, have a look at the diagrams in Overview of the Perform
features.
For example, when you play live beats on top of a running Pattern, you can use Note Repeat
without destroying the Pattern’s groove: the repeated notes will be processed using the same
swing parameters as the playing Pattern.
When the playback is not running, the swing is still applied to the output of Arp (pads
in Keyboard mode) or Note Repeat (pads in Group mode). If you press PLAY on your
controller, the playback starts immediately and the swing cycle is reset.
PLAYING ON THE CONTROLLER 137