---
titre: "xferrecords com manual serum 2 docs — Using the Mixer (p. 144-151)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Mixer


<!-- page 144 -->

Serum 2 User Guide
144
Using the Mixer
Serum features an advanced mixer that you can use to blend and balance the principal sound sources
in your patch, including the sub oscillator, the three main oscillators (OSC A, B, and C), and the noise
oscillator. In addition, you can include the output from FILTER 1 and 2 in the mix, together with the
output from two internal Serum busses.
In short, the mixer provides you with precise control over the individual elements of your sound. Using
the Serum mixer, you can create complex, layered sounds with ease, adjusting the volume, pan, and
routing of each component to achieve the perfect sound.
Serum Mixer (MIX)
Exploring the Mixer
Click the MIX tab to access the Serum mixer.
Accessing the Serum Mixer (MIX)

<!-- page 145 -->

﻿
Using the Mixer
Serum 2 User Guide
145
The mixer shows the elements of Serum that you have enabled.
Mixer for the Init Patch
For the Init patch, for instance, only OSC A is enabled and, therefore, this is the only channel enabled in
the mixer. Click the header to enable a channel.
Note that this enables the oscillator or filter throughout
Serum.
Each oscillator channel offers the same
controls.
Use the channel menu to specify the signal
routing.
For example, in the illustration below, the
output of OSC A is currently being routed to
the filter module.
However, you could choose to route the
signal to an alternative destination.
Note that, by default, OSC A routes through
FILTER 1, while the OSC B, OSC C, SUB,
and NOISE oscillators route through the
MAIN output by default.
Hold the Option/Alt key and drag the oscillator channel label to another oscillator label to
copy the oscillator without modulations.
Hold the Shift-Option or Shift-Alt keys and drag the oscillator channel label to another
oscillator label to copy with modulations.
Dragging from one oscillator channel label to another without any keyboard modifiers swaps
the two oscillators (including modulation assignments).
Oscillator Header
Oscillator Channel
Oscillator Channel Menu

<!-- page 146 -->

﻿
Using the Mixer
Serum 2 User Guide
146
The following table describes the signal routing options:
Option
Description
Filter
Route the signal to the filter module. Use the top knob to set how much of
the signal is sent to FILTER 1 and FILTER 2.
Main
Route the signal to the main output. When you choose this option, the
envelope button
 appears near the bottom left of the channel.
When enabled, the oscillator output level is affected by ENV 1.  When
disabled, ENV 1 has no effect on the oscillator output level and it terminates
after the longest release of any of the envelopes. You can use this to make
oscillators appear closer to being free running.
Direct
Route the signal to direct output, bypassing the filter and effects sections,
outputting “clean” along with the main output.
Similar to MAIN, when you choose this option, the envelope button

appears near the bottom left of the channel.
None
Disable the output of the source (the oscillator, for example).
Sending to the Busses
You can send oscillator signals to BUS 1, BUS 2, or both.
To send a signal to either bus, click and drag the
corresponding BUS knob. To set a specific value, double-
click the knob and type the appropriate value in the field
that appears.
Sending a signal through auxiliary effects busses offers multiple advantages, including the following:
•	 Consistent sound and cohesion
Using a shared bus for effects such as reverb or delay can create a more cohesive sound across the
mix. For example, sending multiple tracks to a single reverb bus can make them sound as if they’re
in the same space, creating a sense of depth and unity.
•	 More precise control
Auxiliary busses allow you to control the wet/dry balance more precisely, as you can adjust the
send levels from each track to the effect bus. This flexibility makes it easier to blend the effect
subtly or aggressively, depending on the needs of the mix.
Sending to the Busses

<!-- page 147 -->

﻿
Using the Mixer
Serum 2 User Guide
147
•	 Parallel processing
Aux busses enable parallel processing, where the dry signal and the processed signal run
simultaneously. This is useful for effects like parallel compression, where you maintain the original
dynamics while adding enhanced processing to the signal.
•	 CPU efficiency
Instead of applying the same effect to multiple oscillators individually, you can send them to a
single auxiliary bus. This reduces the CPU load since only one instance of the effect is running.
Setting Pan and Levels
You can set the pan and levels for each oscillator as part of creating a balanced and clear audio
experience.
Click and drag the PAN knob left or right, as appropriate. To set
a specific value, double-click the knob and type the appropriate
value in the field that appears.
Use negative values for left and positive values for right.
Similarly, click and drag the level up or down, as needed. To
set a specific value, double-click the control and type the
appropriate value in the field that appears.
You can use panning to effect the following:
•	 Create a stereo image — Panning places sound elements across the stereo field (left to right), giving
the mix width and spatial dimension.
By positioning elements in different parts of the stereo field, you create a more realistic and
immersive sound, emulating how we naturally hear sounds around us.
•	 Prevent clashing — Panning helps separate elements that occupy similar frequency ranges.
For example, if you have two midrange-heavy sound elements, panning them apart reduces the
likelihood of them competing for space and allows each to be heard more clearly.
•	 Add depth and realism — Proper use of panning mimics the natural placement of sound elements
in a room or on stage. It helps give the listener a sense of depth and positioning, making the mix
feel more dynamic and engaging.
Setting Pan and Levels

<!-- page 148 -->

﻿
Using the Mixer
Serum 2 User Guide
148
You can set the levels to control the following:
•	 Ensure balance — Adjusting levels is essential for achieving a clear and balanced mix.
Setting the volume of each element ensures that the most important parts are prominent while
supporting elements are appropriately audible without overpowering the mix.
•	 Maintain dynamics — Setting levels effectively preserves the dynamic relationships between sound
elements.
This allows you to better manage contrast between elements.
•	 Controls focus — Levels can guide listener focuses.
By raising or lowering the volume of certain elements, you can guide the listener’s attention and
shape the overall feel of the sound, making certain parts stand out more prominently while others
remain in the background.
Mixing Filters
You can control how the filter output
integrates into the overall mix.
Important: Even after enabling a filter (by
clicking in the corresponding header), the
filter appears dimmed until you send an
oscillator signal to the filter.
By default, FILTER 1 and FILTER 2 send
through the MAIN output.
Use the channel menu to specify the signal
routing.
Similar to the filter module, you can graphically adjust the filter cutoff and
resonance (in combination) by clicking and dragging in the filter display.
This is a quick way to experiment with filter settings while mixing!
Filter Channel Menu
Filter Channel Menu
Filter Adjustments

<!-- page 149 -->

﻿
Using the Mixer
Serum 2 User Guide
149
The following table describes the signal routing options from the filters:
Option
Description
Filter 1 or Filter 2
Route the signal to the other filter, either FILTER 1 or FILTER 2.
Main
Route the signal to the main output. When you choose this option, the
envelope button
 appears near the bottom left of the channel.
When enabled, the oscillator output level is affected by ENV 1.  When
disabled, ENV 1 has no effect on the oscillator output level and it terminates
after the longest release of any of the envelopes. You can use this to make
filters appear closer to being free running.
Direct
Route the signal to direct output. Similar to MAIN, when you choose this
option, the envelope button
 appears near the bottom left of the
channel.
None
Disable the output of the source (the filter, for example).
Routing to the Busses
You can route filter signals to BUS 1, BUS 2, or both.
To route a signal to either bus, click and drag the
corresponding BUS knob. To set a specific value, double-
click the knob and type the appropriate value in the field
that appears.
Setting Pan, Mix and Levels
You can set the pan, mix, and levels for each filter. Click and drag the PAN knob left or right, as
appropriate.
To set a specific value, double-click the knob and type the
appropriate value in the field that appears. Use negative
values for left and positive values for right.
Similarly, click and drag the MIX knob to set the dry/wet
blend of the filter mix.
For most filters, the recommended mix setting is 100% (all
the way to the right).
Note: The MIX knob has no effect for Combs-type filters.
Finally, click and drag the level up or down, as needed. To set a specific value, double-click the control
and type the appropriate value in the field that appears.
Routing to the Busses
Setting Pan, MIX and Levels

<!-- page 150 -->

﻿
Using the Mixer
Serum 2 User Guide
150
Mixing the Busses
You can set the routing and overall
levels for the FX busses.
By default, BUS 1 and BUS 2 route
through the MAIN output.
Use the channel menu to specify
the signal routing.
Click the
 button to bypass
the corresponding FX module on
the bus.
When enabled, the button
highlights in red to show that the
FX module is being bypassed.

The following table describes the signal routing options from the busses:
Option
Description
Main
Route the signal to the main output.
Direct
Route the signal to direct output.
Bus 1 or Bus 2
Route the signal to the other bus, either BUS 1 or BUS 2.
Setting Levels
You can set the level for each bus.
Click and drag the level up or down, as appropriate.
To set a specific value, double-click the control and type
the appropriate value in the field that appears.
Mixing Busses
Filter Channel Menu
Setting Levels

<!-- page 151 -->

﻿
Using the Mixer
Serum 2 User Guide
151
Setting the Main and Direct Levels
You can set the MAIN and DIRECT levels for the mix.
Click and drag the levels up or down, as appropriate.
To set a specific value, double-click the control and type the
appropriate value in the field that appears.
Click the
 button to bypass the corresponding FX module
on the main channel.
When enabled, the button highlights in red to show that the FX
module is being bypassed.

Setting Main and Direct Levels