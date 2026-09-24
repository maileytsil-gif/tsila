---
titre: "Maschine Software Manual — 12. Using effects (p. 341-356)"
source: constructeur/native-instruments-com-fileadmin-ni-media-downloads-manuals-maschine-maschine-3-software-m.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# 12. Using effects


<!-- page 341 -->

12. Using effects
At each Project level (Sound, Group and Master) you can add effects in the form of Plug-ins. Each
Sound, each Group, and the Master can have an unlimited number of insert effects loaded in their
Plug-ins slots. In each Plug-in slot, you can load an Internal, Native Instruments or External Effect
Plug-in.
The processing order is always from top to bottom, both in the Plug-in List of the Control area (in
Ideas view and Song view) and in the channel strip of the Mixer (in Mix view). In the Plug-in Strip of
the Mix view, the processing order is from left to right.
For Sounds, the first Plug-in slot is often hosting an Instrument Plug-in (Sampler, Drum
Synth, Native Instruments or External Plug-in), allowing the Sound to generate its own
audio. If you load instead an effect into the first Plug-in slot of a Sound, this Sound will
act as a bussing point for other Sounds and Groups, and you will find this Sound in the
various Dest. selectors in the Output properties of other the Sounds and Groups. See
section Creating a send effect below for more information.
Most of the features used in the procedures mentioned in this chapter have been already described
in chapter Working with Plug-ins — in Maschine, effects are just a certain type of Plug-ins.
Nevertheless, we illustrate them here with various effect-oriented examples. Furthermore, from
time to time we will use the Mix view instead of the default Arrange view: Indeed, the intuitive
routing facilities of the Mixer make it particularly well suited for quickly setting up advanced effect
routings.
Applying effects to a Sound, a Group, or the Master
The procedures for applying an effect at the Sound, Group, and Master levels are very similar.
Adding an effect
Let us add an Effect Plug-in somewhere in the Project. We first describe the detailed procedure in
Arrange view, then we will show the equivalent procedure in Mix view.
Choosing the channel for the effect
1. If you want to apply the effect to the Master (to process the audio of the whole Project), click
the MASTER tab in the top left corner of the Control area.
USING EFFECTS 338

<!-- page 342 -->

2. If you want to apply the effect to a Group (to process the audio of the whole Group), click the
desired Group on the left of the Arranger, and click the GROUP tab in the top left corner of the
Control area.
3. If you want to apply the effect to a Sound, click its parent Group in the Group List (on the left
of the Arranger), click the desired Sound slot in the Sound List (on the left of the Pattern Editor),
and click the SOUND tab in the top left corner of the Control area.
Loading the effect in a new Plug-in slot
1. At the far left of the Control area, click the little Plug-in icon to display the Plug-ins of the
selected channel:
The icon lights up. The Plug-in List appears nearby, showing a stack of all Plug-ins already
loaded in the channel:
In the Plug-in List, each Plug-in has its own slot.
USING EFFECTS 339

<!-- page 343 -->

2. Click the “+” icon under the last Plug-in in the list (or at the top if the list is empty).
The Plug-in menu opens and shows a list of all available Effect Plug-ins.
If you have selected a Sound and its Plug-in List is empty, the Plug-in menu also shows all
available Instrument Plug-ins.
3. Click the desired entry in the list. If you have VST/AU effect plug-ins installed you may also load
them from the menu by selecting the Native Instruments (for Native Instruments products) or
External (for third-party products) submenu at the top of the list.
→Upon your selection, the effect is loaded in a new Plug-in slot at the end of the list and
directly starts to process the audio of the channel. The effect parameters are displayed in the
Parameter area on the right (in the example underneath we selected the Phaser effect in the
Plug-in menu).
Notes and hints on loading effects in the software
•
Instead of clicking the “+” icon to load the effect in a new slot, you can also click the down-
pointing arrow on the right of an existing slot to open the Plug-in menu: The effect selected in
the menu will replace the Plug-in currently loaded in that slot.
USING EFFECTS 340

<!-- page 344 -->

•
Instead of using the Plug-in menu, you can also use the Browser to load a particular preset
for an effect. In particular, this can come in handy to insert a new effect between two existing
Plug-ins in the Plug-in List. For more information, refer to Searching and loading files from the
Library. Alternatively, you can use Quick Browse to recall the search query that was used to load
a particular Plug-in preset, for more information refer to Using Quick Browse.
•
For all details on the parameters for each Maschine effect, refer to Effect reference.
•
For additional, specific information on VST/AU plug-ins, refer to Using Native Instruments and
External Plug-ins.
•
If you created a nice effect setting, you can put it to further use by saving it as a Plug-in preset.
For more information, refer to Saving and recalling Plug-in presets.
Adding an effect in Mix view
You can also load effects in Mix view. The procedure is quite similar to that in Arrange view (see
above).
Reminder: To switch the Mixer display between all Groups of your Project and all
Sound slots in a particular Group, double-click the background of any Group header at
the top of the Mixer. For more information, refer to Displaying Groups or Sounds.
First, display the Plug-in List in Mix view:
1. Click the Mix View button (showing three little faders) at the left of the Arranger to switch from
Arrange view to Mix view:
2. If it is not already open, open the extended view of the Mixer by clicking the down-pointing
arrow at the left of the Mixer:
3. Check that the Plug-in icon is active at the left of the Mixer. If not, click it to display the Plug-in
List in each channel strip.
Then you can put the focus onto the channel (Master, Group or Sound) in which you want to load
the effect:
USING EFFECTS 341

<!-- page 345 -->

1. To set the focus onto the Master channel: In the top right corner of the Mixer, click in the blank
space above the Master label and headphones icon to set the focus to the Master/Cue channel
strip.
If necessary, click Master in that header to switch from the Cue channel to the Master channel.
2. To set the focus onto a Group channel: If the Mixer is currently displaying the Group channel
strips, click the header of the desired Group at the top of the Mixer. If the Mixer is currently
displaying Sound channel strips, double-click the header of the desired Group at the top of the
Mixer.
3. To set the focus onto a Sound channel: If the Mixer is currently displaying the Group channel
strips, in the Mixer’s top row double-click the blank space in the header of the Group containing
the desired Sound, then click the header of the desired Sound in the row below. If the Mixer
is currently displaying Sound channel strips, in the top row click the header of the Group
containing the desired Sound, then click the header of this Sound in the row below.
Finally, load the effect in the focused channel strip:
▶In the Plug-in List of the focused channel, click the little “+” to append the effect to the list,
or right-click ([Ctrl]-click on macOS) an existing Plug-in slot to replace its current Plug-in, and
select the desired effect in the Plug-in menu that opens.
→The effect is loaded and starts to process the audio of the channel. The effect also appears in
the Plug-in Strip under the Mixer, allowing you to adjust its parameters.
In fact, you don’t need to explicitly put the focus on the channel in which you want to
load the effect: You only have to make that channel visible in the Mixer! You can then
directly click the “+” symbol or right-click ([Ctrl]-click on macOS) an existing Plug-in
slot to load the effect in that channel. Nevertheless, setting the focus on the channel
has the advantage of displaying the new effect in the Plug-in Strip under the Mixer for
adjusting its parameters, you can do this afterward.
For more information on the Mixer and the Mix view in Maschine, refer to section Mix
view basics.
Other operations on effects
You can manipulate effects like any other Plug-in loaded in a Plug-in slot. This notably includes
adjusting the effect parameters, removing effects, moving effects to different Plug-in slots, saving
and recalling effect presets, etc.
USING EFFECTS 342

<!-- page 346 -->

We provide here a reminder of every operation available on the effects in both Arrange view and
Mix view.
Concerning the procedures listed below, the only difference between Arrange view
and Mix view is the way to open the Plug-in menu: In Arrange view you open it by
clicking the Plug-in slot’s down-pointing arrow, whereas in Mix view you open it by
right-clicking ([Ctrl]-clicking on macOS) the effect name in the Plug-in List.
Action
Procedure
All effects
Insert an effect after an
existing Plug-in
From the Browser or from your operating system, drag and drop
the desired effect preset between two existing Plug-in slots.
Replace an effect
Open the Plug-in menu, and select another effect from the menu.
Remove an effect
Open the Plug-in menu, and select None from the menu.
Move an effect within the
Plug-in List
Click and hold the effect in the Plug-in List, drag your mouse to
the desired location (an insertion line appears where the effect
will be dropped), and release the mouse button.
Move an effect to another
channel (Sound, Group, or
Master)
First, open the source slot’s Plug-in menu and select Cut. Then
open the Plug-in menu of the desired slot in the target channel
(Sound, Group, or Master) and select Paste.
Duplicate an effect
First, open the source slot’s Plug-in menu and select Copy. Then
open the Plug-in menu of the desired slot in the target channel
(Sound, Group, or Master) and select Paste.
Bypass an effect
Click the FX icon (in Arrange view) or the little square (in Mix
view) at the left of the effect name in the Plug-in List. Click again
to re-enable the effect.
Save the current effect
settings as preset
Open the Plug-in menu, and select Save As… at the bottom of
the menu.
Recall an effect preset
Use the Browser (see chapter Browser), or open the Plug-in
menu and select Open… at the bottom of the menu.
Native Instruments and
External effects
Open/close the effect
window
Arrange view: Click the little window icon in the top left corner of
the Parameter area (at the left of the first page tab).
Mix view: In the Plug-in Strip under the Mixer, click the little arrow
in the top left corner of the effect panel.
Save the current settings
as default preset for this
effect
Open the Plug-in menu, and select Save As Default… at the
bottom of the menu.
For detailed information on these topics, please refer to Plug-in overview. For more details on
the specific operations available for Native Instruments and External Effects, refer to Using Native
Instruments and External Plug-ins.
USING EFFECTS 343

<!-- page 347 -->

Using the side-chain input
For certain Plug-ins, Maschine allows you to use a side-chain input to control how the effects
process the audio.
What is a side-chain input?
If we consider an effect unit that processes the signal incoming at its main input, side-chaining
means using a secondary signal (the “side-chain signal”) fed into a secondary input of the unit
(the “side-chain input”) to control the behavior of the processing. Usually, the amplitude of the
side-chain signal will determine how much the main signal will be processed by the unit.
In music production, the side-chain signal is most of the time another audio track of the project. A
common example is the use of the kick drum track as a side-chain for the compression of the bass
track: on each kick the compressor will compress the bass more, resulting in a typical pumping
effect between kick and bass that can be heard in various styles of dance music.
The side-chain Parameter page
The following Internal, Native Instruments, and External Plug-ins support side-chaining:
•
Internal Plug-ins: Compressor, Maximizer, Limiter, Gate, Filter.
•
AU plug-ins (Native Instruments and External): Any AU plug-in with side-chain input.
•
VST plug-ins (Native Instruments and External): Any VST plug-in with multiple inputs.
When you load one of these Plug-ins into a Sound or a Group, a Side-Chain Input Parameter page
appears at the end of the page list.
Side-chaining is not possible at the Master level (that is if the Plug-in is loaded in a
Plug-in slot of the Master).
The Side-Chain Input page of the Compressor Plug-in in the Control area.
To learn how to access Parameter pages, refer to Navigating Channel properties,
Plug-ins, and Parameter pages.
The parameters of the side-chain input are not available in the Plug-in panel of the
Plug-in Strip (Mix view).
Parameter
Description
Input section
USING EFFECTS 344

<!-- page 348 -->

Parameter
Description
Source
Selects the audio signal you want to use as a side-chain signal to control the
Plug-in. Available options are None (side-chain deactivated, default setting),
the outputs of all (other) Sounds, and the outputs of all (other) Groups.
In the menu these outputs are labeled as follows:
For Groups: [Group name] (e.g., Drums)
For Sounds: [Group name]: [Sound name] (e.g., Drums: Kick)
In the selector display these outputs are labeled as follows:
For Groups: [Group name] (e.g., Drums)
For Sounds: [Group letter+number]:S[Sound number] (e.g., A1:S4 for the
Sound 4 of Group A1)
Gain
Adjusts the input level of the side-chain signal fed into the Plug-in.
Filter section
Filter
Activates a filter on the side-chain input. This filter can be useful to select only
a specific frequency range of the side-chain signal to control the Plug-in.
Center Freq
Adjusts the center frequency of the filter.
Width
Adjusts the bandwidth of the filter.
On your controller, the outputs available in the Source parameter are labeled as in the
display of the Source selector described above.
Note that the settings of the Side-Chain Input page stay in place when you switch
to another Plug-in supporting side-chain. This notably allows you to try different
compressors or different compression presets without losing your side-chain setup.
Applying effects to external audio
Maschine’s flexible routing facilities allow you to apply effects to external audio as well. This
external audio can come from the inputs of your audio interface if Maschine is used in stand-alone
mode, or from your DAW if Maschine is used as a plug-in.
This is done by configuring a Sound accordingly using the Audio page of its Input properties.
Step 1: configure the Maschine audio inputs
You can configure Maschine’s audio inputs in the software only. Furthermore, this configuration is
necessary only if you are using Maschine as a stand-alone application.
USING EFFECTS 345

<!-- page 349 -->

If you are using Maschine as a plug-in in a DAW, Maschine can receive audio from
your DAW on any of its sixteen mono virtual inputs. To know how to route audio
in your DAW to the virtual inputs of the Maschine plug-in, please refer to your DAW
documentation. When this is done, go directly to Step 2: set up a Sound to receive the
external input.
Maschine in stand-alone mode
Please make sure that you have connected an external audio signal source to your audio interface
and that the audio interface's inputs are activated. To do this:
1. Select the Preferences… entry from the File submenu of the Maschine menu to open the
Preferences panel.
2. On the Audio page, click the Input button, activate the desired inputs by clicking their field in the
Port column, selecting a physical input from the drop-down menu, and clicking Close.
→Audio signals coming from external sources plugged in the inputs selected here will now be
routed to the Maschine inputs shown in the first column.
USING EFFECTS 346

<!-- page 350 -->

See Preferences – Audio page for more information on the Audio page of the
Preferences panel.
Maschine in plug-in mode
If Maschine is running as a plug-in in a host environment, the Maschine plug-in can receive audio
from the host only. Please refer to your host documentation to find out how to route audio
channels to the virtual audio inputs of the Maschine plug-in.
In this example, we will assume that you routed some audio channels of your host to the first
virtual input pair of Maschine.
USING EFFECTS 347

<!-- page 351 -->

Step 2: set up a Sound to receive the external input
We describe here the procedure in Arrange view. You can also do this in Mix view, as
described in Sending external audio to Sounds.
•
Now the external audio is routed to your Sound! You can adjust the level of the incoming signal
via the Gain knob.
You will find a detailed reference of the Audio page of the Sounds’ Input properties in
section Sending external audio to Sounds.
Step 3: load an effect to process the input
We describe here the procedure in Arrange view. You can also do this in Mix view, as
described in Adding an effect.
You can now insert an Effect Plug-in into this Sound to let it process the incoming audio.
1. At the far left of the Control area, click the Plug-in icon to display the Plug-ins of the Sound:
The icon lights up. The Plug-in List appears nearby. Since we have chosen an empty Sound in
section Step 2: set up a Sound to receive the external input above, the Plug-in List should be
empty:
2. Click the “+” icon at the top of the Plug-in List. The Plug-in menu opens and shows a list of all
available Instrument and Effect Plug-ins.
USING EFFECTS 348

<!-- page 352 -->

3. Click the desired effect in the list. If you have VST/AU effect plug-ins installed you may also
load them from the menu by selecting the Native Instruments (Native Instruments products) or
External (third-party products) submenu at the top of the list.
→Upon your selection the effect is loaded in a new Plug-in slot and directly starts to process your
external audio!
Creating a send effect
Sometimes you may want to have a classic send effect, for example, a reverb which can be shared
by multiple sound sources. To make use of a send effect, you need to:
•
Step 1: set up a Sound or Group as send effect. This is done by loading an effect into its first
Plug-in slot: Step 1: set Up a Sound or Group as send effect.
•
Step 2: route a portion of the desired audio signals from their original Sounds and Groups to
that send effect. This is done in the Output properties of the corresponding Sounds and Groups:
Step 2: route audio to the send effect.
Step 1: set Up a Sound or Group as send effect
The procedure to set up a Sound or Group as a send effect is straightforward: You just need to load
an effect into its first Plug-in slot — Maschine will take care of the rest and make it available as a
destination for other channels of your Project.
We describe here the procedure in Arrange view. You can also do this in Mix view, as
described in Adding an effect.
In this example we will use an empty Sound:
1. Choose the empty Sound you want to use as send effect: On the left of the Arranger click the
Group containing that Sound, on the left of the Pattern Editor click the desired Sound slot, and
click the SOUND tab in the top left corner of the Control area.
2. At the far left of the Control area, click the Plug-in icon to display the Plug-ins of the Sound:
The icon lights up. The Plug-in List appears. Since we have chosen an empty Sound, the Plug-in
List should be empty:
USING EFFECTS 349

<!-- page 353 -->

3. Click the “+” icon at the top of the Plug-in List.
The Plug-in menu opens and shows a list of all available Instrument and Effect Plug-ins.
4. Click Internal and select the desired Maschine effect from the submenu. If you have VST/AU
effect plug-ins installed you may also load them by using the dedicated submenu (for example,
the VST3 submenu) and choosing a vendor submenu.
→Upon selection, the effect is loaded and its parameters are displayed in the Parameter area.
When you load an effect into the first Plug-in slot of a Sound, Maschine automatically
configures the Sound’s input to receive any signal(s) coming from other Sounds and Groups in
your Project and sends them through its own Plug-in slots, in other words, you now have a send
effect.
You could also load an effect preset from the Browser instead of using the Plug-in
menu. For more information on how to load effect presets, refer to Searching and
loading files from the Library.
Now that the effect is loaded, we suggest that you rename the Sound slot to the Plug-in name: this
will be of great help when routing other signals to that send effect in the next step (refer to Step 2:
route audio to the send effect). To rename the Sound slot:
1. Double-click the name of the Sound slot in the Sound List. The name becomes highlighted,
ready to be edited.
2. Type the name of the Plug-in, and press [Enter] on your computer keyboard to confirm.
→The Sound slot now mirrors the Plug-in name.
For more information on renaming Sound slots, refer to Renaming Sound slots.
Step 2: route audio to the send effect
Once you have configured a Sound or Group as send effect (refer to Step 1: set Up a Sound or
Group as send effect), you can send the output of any other Sounds and Groups to that Sound or
Group. For this purpose, each Sound and each Group is equipped with an additional two auxiliary
outputs available in its Output properties.
USING EFFECTS 350

<!-- page 354 -->

We describe here the procedure in Arrange view. You can also do this in Mix view, as
described in Configuring the main output of Sounds and Groups.
You can repeat the process to route more Sounds/Groups to the same send effect, or route the
same Sound/Group to an additional send effect send using AUX 2.
A few notes on send effects
When working with send effects, please keep in mind the following:
•
You cannot send the Master output to send effects.
•
You cannot send a send effect’s output to itself, nor the output of a Group to one of its own
Sounds.
However, you can:
•
Chain several Sounds configured as send effects by sending the output of a send effect into
another send effect using the method described above (refer to Step 2: route audio to the send
effect).
•
Use the Effect Plug-ins loaded in a Group to simultaneously process its own Sounds and other
Sounds/Groups sent to it.
This opens up virtually endless routing possibilities.
When setting up complex routings, please take care to avoid feedback loops!
In addition, the following points are worth noting:
•
CPU load: Send effects can be of great help to save CPU power. Using one reverb for many
Sounds and Groups instead of loading another reverb in each Sound/Group makes a big
difference on the CPU load. You can adjust at which extent the reverb must be applied to each
Sound/Group via the Level control in their respective Output properties.
•
MIDI control: As any other Sounds, Sounds used as send effects can be controlled via MIDI.
This is not only true for all effect parameters (refer to Controlling parameters via MIDI and
host automation), but also for effects requiring incoming notes (for example, a vocoder). See
Triggering Sounds via MIDI notes for more information.
•
Use Patterns: You can create Patterns for your send effects to make them more lively. Simply
record some modulation in Control or Step mode for the desired effect parameters, or even
record notes for effects requiring incoming notes (like the vocoder).
Creating multi-effects
Creating a multi-effect unit is the same thing as creating a series of Sounds as send effects within
a Group and arrange them as you see fit. Following the procedure described in the previous section
Creating a send effect, in every Sound of the Group you can set up a send effect containing any
number of effects, the only limit being the processing power of your computer! You can route
Sounds within the Group to your liking: You can chain them all, keep them as separate effects to be
used in parallel, build any combination of both, etc.
USING EFFECTS 351

<!-- page 355 -->

Organizing your effects across several sounds
If you plan to build multi-effects containing more than a few Effect Plug-ins in series, you have
many ways at your disposal. Since you can have any number of Effect Plug-ins in each Sound,
you can set up the whole sequence of effects in series into one single Sound. However, it might
be judicious to split your sequence of effects across several Sounds whose outputs are sent into
the inputs of the next Sound (thereby re-building an equivalent sequence of effects). Doing this can
have several advantages, for example:
•
The Sound List helps you keep a better overview of your effect sequence than the tiny Plug-in
List in a single Sound.
•
You can rename and colorize each Sound individually according to the effect(s) it contains.
•
You have better control of your whole effect sequence from your controller.
•
You can easily re-arrange your effect sequence by changing the routing between your Sounds.
To use several Sounds plugged in series, use the procedure described in the previous section
Creating a send effect to send the output of each Sound to the input of the next one in the
sequence.
Which output to use?
Each Sound provides three distinct outputs: Main, Aux 1, and Aux 2. If you want to build a series
of effects split across several Sounds, for each Sound in the series you have to send one of these
outputs to the input of the next Sound. For this, we recommend you to use the main output of
the Sound rather tha an auxiliary output because it provides a few useful additional features not
available on the auxiliary outputs:
•
Cue switch: You can send the Main output of any Sound to the Cue bus and pre-listen the
channel on a distinct Maschine output (typically your headphones). Note that enabling the Cue
switch automatically mutes both Aux 1 and Aux 2 outputs as well, but it doesn’t send them to
the Cue bus!
•
Hardware control: Your controller provides various shortcuts allowing a quicker and easier
control of your Sounds’ Main output.
These can be of great help when building complex multi-effects.
Saving your multi-effects
You can then save the whole multi-effect Group for later use. This can be useful if you like a certain
combination of effects for your live setup or in the studio. Although this might sound overkill, you
can still add more effects to the multi-effect Group itself afterwards: Imagine for example distinct
send effects in different Sounds, but all of them being further processed by the same set of effects
at the Group level.
However, take the time to name the multi-effect Group and every of its Sounds based on the
inserted effect(s), and possibly prepend or append a text string (for example "FX_") that will
later help you recognize it as an effect. Remember that you will be choosing this effect from a
potentially large list in your user library. In the Maschine Library there are already a number of
multi-effect Groups tagged Multi FX. Don’t hesitate to reuse this tag or to create a custom tag for
your own multi-effect Groups.
USING EFFECTS 352

<!-- page 356 -->

Groups of the Multi FX type in the LIBRARY pane.
USING EFFECTS 353