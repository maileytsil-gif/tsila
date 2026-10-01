---
titre: "javelinart com fm synthesis of real instruments pdf (texte du PDF, 51 pages)"
source: cuivres/javelinart-com-fm-synthesis-of-real-instruments-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

FM Synthesis of Real Instruments (and any other type)


1. An Introduction to FM   (Frequency Modulation)



 By  Thor Zollinger   2016
2. FM Basics








        Thor276@Yahoo.com
3. Instrument Duplication






        Copyright 2016
4. Spectrum Analysis
5. Single-Stack Operators
6. ADSR Envelopes - Clarinet
7. Double-Stack Algorithms


18.  Performance Voices
8. Spacing Harmonics Over 2 Apart

19.  4-OP to 6-OP Patch Conversion Chart
9. Triple-Stack Algorithms


20.  Montage FM-X and the FS1R
10. Fan Overlap -Interference Patterns

21.  Formants Anyone?  The FS1R
11. ADSR Envelopes – Saxophone


22.  FS1R Tips & Tricks
12. Four-Stack Algorithms


23.  Afterward
13. Complex Waveforms – DX11



14. Analog Waveform Patches

APPENDIX A.  DX11 Instrument Patch Examples (4-OP)
15. Troubleshooting Patches

APPENDIX B.  DX7 Instrument Patch Examples (Converted 4-OP Patches)
16. Adjusting Note Registers

APPENDIX C.  Montage and FS1R FM Instrument Patch Examples (8-OP)
17. Balancing Voices


APPENDIX D.  FS1R Formant Instrument Patch Examples (FS + 8-OP)

<!-- page 2 -->

1.  An Introduction to FM
Back in the early 70’s in an electronic audio lab at Stanford University John Chowning was experimenting with the
university’s analog synthesizers.  He noticed something odd occurring while playing with vibrato on the instrument.
When he turned the vibrato speed way up the sound stabilized and produced a set of harmonic tones around the main
note.  At specific settings the sound was harmonic and clean.  He realized this was a way to produce very complex
sounds using only two oscillators.  Prior to this it took dozens of oscillators to do the same thing.  Frequency Modulation
Synthesis was born.  He went deeply into the theory and developed the mathematics needed to produce the sounds
digitally, and in 1973 he published his famous article on Frequency Modulation.  In 1977 Yamaha licensed the technology
and came out with the first programmable FM synthesizers in 1983, including the infamous DX7 which took the music
industry by storm.

The DX7 sold over 200,000 units and is still considered the most iconic FM synthesizer in existence.  In recent years it’s
been replicated on computers in VST’s and is in the hands of millions of users.  Despite over 30 years of use, the
techniques used to program FM are still a mystery to most people.  Yamaha surveyed DX7 owners and found that only
about a hundred of those original DX7 users could program an instrument patch from scratch.  Even the original Yamaha
factory patches are a bit lacking.  I own a DX11 which came out in 1987 and an FS1R from 1998, and only a hand full of
the factory patches are very accurate to the real instruments they’re named after.  The user generated patch libraries
aren’t any better.  Very few of the patches actually sound like the instruments they’re meant to duplicate.
Searching the Internet for tutorials on how to program FM is also fruitless.  There are plenty of primers explaining the
basics of FM, but none go beyond that point to explain how to use FM to duplicate a real instrument.  The only
conclusion you can come to is that very few people understand how Frequency Modulation really works.  Most users
simply tweak an existing patch without ever really understanding what’s really going on under the hood.
Is FM really so complicated that nobody can figure it out?
No, it’s not!  And we’re going to prove it!

<!-- page 3 -->

2.  FM Basics
Frequency Modulation is really just vibrato on steroids.  You start with a Carrier oscillator which determines the pitch of
the note that is heard.  The Carrier is altered by applying very high speed vibrato (modulation) using a Modulation
oscillator.  The result is that you hear multiple harmonics popping up on both sides of the main note.  Increasing the
amplitude of the vibrato increases the effect, creating more and more harmonics in the sound.
When you use modulation frequencies that are integer multiples of the Carrier frequency, you get melodic harmonics
that work well together in duplicating the sounds of instruments like a flute or a violin.  If you use a modulation
frequency that is a fractional multiple of the Carrier you get inharmonic sounds which can be used to duplicate bells or
to create dissonant sounds.  Slightly inharmonic ratios are used to detune parts of the sound to replicate the timbre of a
piano or a sitar.  If you want to get fancy you can stack on more modulators to really complicate the harmonic structure,
and you can add together multiple sets of carriers and modulators to further increase the complexity of the sound.
In FM the frequencies of the Carrier (Fc) and Modulator (Fm) are represented by the ratio of their frequency to the
fundamental frequency of the note being played.  In most of our examples at least one carrier will be set to a frequency
ratio of 1.00, meaning the carrier is at the frequency of the key being pressed on the piano keyboard.  In the graphs
below, our modulator will be at a frequency ratio of 1.00 which spaces out the harmonics by multiples of the
fundamental frequency.  The first, second, third, and fourth harmonic frequencies (shown below) can be calculated by
adding the frequency of the modulator to multiples of the carrier frequency.
F1 = Fc
The Fundamental Harmonic, #1
F2 = Fc + Fm
(and also F2 = Fc - Fm for the lower side band)
F3 = Fc + 2*Fm
F4 = Fc + 3*Fm

The graphs below show what happens to the output of the Carrier Operator as you increase the volume of the
Modulator.  The Carrier frequency in our example below is in the middle of the blue peaks at harmonic 9.00.  The
Modulator causes frequency spikes to form to the sides of the Carrier frequency as you increase the volume of the
modulator.  The spacing between the harmonics is equal to the Modulation frequency.  The modulator is set to 1.00
below, spacing the spikes 1.00 apart.  If this sounds confusing, just be patient and we’ll clear all this up in a few more
minutes.

<!-- page 4 -->

Volume=DX11(DX7)
   Figure 1.  Frequency Modulation of a Carrier
On the plots in Figure 1 you can also see that as we increase the volume of the Modulator the center Carrier frequency
spike gets shorter and shorter, along with the ones right next to it.  So far the Operations we’ve discussed are done using
sine waves.  We’re going to leave it there and pick up other wave shapes later to avoid too much complication.
The Index (I) on the plots above refers to the work of John Chowning, the inventor of Frequency Modulation Synthesis.
He came up with the definition of a Modulation Index which is what the ‘I=’ terms refer to on the chart.  On a DX
synthesizer the Index (I) is adjusted using the volume of the modulator.  The values for Volume on DX synths are in the
right-most column of Figure 1,  DX11(DX7).  In the rest of our discussion we’re mostly going to use the right half of the
modulator/carrier plots.  The left side will fall below 0 hz where it doesn’t affect us much.  Well, it does affect us
somewhat, but let’s just keep things simple for now and ignore the left half of the patterns.
This is the point where most tutorials stop.  They give you a very brief intro, then drop the ball or lose you in a detailed
explanation of the mathematics involved.  We don’t really want to know how to do the math, what we really want to
know is how to USE the stuff.

3.  Instrument Duplication
There are a couple of reasons why I chose real instruments as the target for this guide.  The first is that there are lots of
recordings out there of real instruments like the violin playing single notes, so there are lots of recordings for you to
practice making instrument patches on.  The second is that there are very few high quality FM instrument patches out
there for these instruments.  Why not fill in the gap?  I do realize most people like FM because it allows you the freedom

<!-- page 5 -->

to create custom instruments.  And, I know a lot of those people want strange new sounds, but not everyone wants to
create a space-zombie pad with a trance beat to it.  Some of us like to modify real instruments instead.
The method we’re going to use to replicate a real instrument is not such a mystery after you’ve done it a few times, so
that’s what we’re going to do.  We’re going to go step by step through a number of examples, and hopefully by the time
we’re done you’ll know how to do it yourself.  This technique applies to more than just real instruments and voices, you
can replicate just about anything you can get a clean recording of.
In short, you start with a recording of the instrument (or sound) you want to duplicate playing a single note all by itself,
then you load the sound sample into a spectrum analyzer like ‘Audacity’ (free on the internet) so you can get a good look
at the instrument’s harmonic structure.  Using the harmonic spectrum plot, you formulate a plan of attack knowing the
tools FM provides you with, selecting one of the algorithms on your synthesizer.  This will get you in the ball park.  You
then listen to the results and make adjustments by ear to your instrument patch by comparing the synthesized sound
with the recording over and over.  You can also use a real-time spectrum analyzer like ‘Visual Analyzer’ (free on the
internet) to assist in this, allowing you to compare the synthesized sound with the spectrum plot so you can see visually
where to make changes in the settings.  I’ve actually had more success at creating a better patch by listening as I make
the adjustments, using a spectrum analyzer visually all by itself doesn’t work out that well.
The process is basically the same for all FM synthesizers.  Our examples are going to go over three families of synths, the
DX11 family which includes DX21, DX27, DX11, TX81Z, FB01, YS100, YS200, Reface-DX, and all other four Operator VST
synths, and the DX7 family which includes the DX1, DX5, DX9, TX802, TX816, SY77, TG77, SY99 and a growing number of
six Operator VST synths.  The third synth family we’ll cover includes the eight Operator FS1R’s and the new Montage FM-
X engine.  FM-X really expands on the capabilities of FM with some very useful harmonic waveforms.  You Montage guys
might want to skip ahead to that section, then come back to cover the basics of FM afterwards.  I have a DX11 and an
FS1R with FM-X.  I don’t have a DX7, but the FS1R can duplicate anything the DX7 can do so don’t get too concerned if
your synth is based on the DX7.
Tools you need:
Audacity:

https://www.audacityteam.org/
Mac and Windows



https://sourceforge.net/projects/audacity/
Visual Analyzer:
http://www.sillanumsoft.org/
Windows
iSpectrum:

https://dogparksoftware.com/iSpectrum.html#:~:text=iSpectrum%20%2D%20Macintosh%20Audio%20Spectru
m%20Analyzer,and%20save%20images%20to%20disk.
Mac
I use two different spectrum analyzer programs, at times so I can have them both open at the same time.  I use Audacity
to open a recording and display a spectrogram to work from, then Visual Analyzer to watch the notes as I play them on
the synthesizer.  You can compare the live spectrum plot to the static one and make adjustments while listening to the
sound until you get it close.  Audacity has a tendency to average out the higher frequency parts of the sound, so be
aware of that failing.
You can also create static spectrograms using Visual Analyzer which are much more detailed than Audacity.  On the main
interface, look at the mini control panel and find the “Main” tab, then look for the “Hold” checkbox.  Just below it is a
setting for averaging the plot over several samples.  I like to use 2 or 3 averaged samples to sharpen the peaks in the plot.
Check the “Hold” box then play a note on your input keyboard to trigger the spectrogram.  Screen-capture the plot so
you can use it later.  To clear the plot, uncheck the “Hold” box.  The problem here is figuring out how to route the sound

<!-- page 6 -->

you want to analyze into Visual Analyzer, it only likes live input channels.  It’s easy to route in a synthesizer in your studio,
but it takes more thinking (possibly another computer or loop-back device) to play recordings and route them in your
main computer for analysis.

4.  Spectrum Analysis
The method we’re going to use to replicate an instrument is based on replicating the harmonic structure.  We start the
process by obtaining several recordings of the instrument in question.  There are numerous places on the internet
where you can find recordings of real instruments playing single notes.  If you are duplicating another type of instrument
or sound, you just need to find a good clean recording to work from.  I found some nice collections of instrument
recordings on the following websites:
http://www.philharmonia.co.uk/explore/make_music
http://theremin.music.uiowa.edu/MIS.html
http://www.compositiontoday.com/sound_bank/default.asp
Another source of high quality recordings is in the synthesizer next to you.  The samples in my Motif-XF are superb, and
it’s simple to pipe the sound into my computer into the spectrum analyzer.
Select a sample where the instrument plays one or more clear notes all by itself.  Select a note to model somewhere in
the middle of the voice range of the instrument.  Instruments with a resonating body like a Violin or Bassoon are harder
to model, so it’s best to start in the middle of the voice range.  We’ll talk about this in more detail in the section on
Formants.  If the recording is muddled on the spectrum analyzer and doesn’t show clear-cut frequency spikes, select a
different recording to work from.
After attempting this several times, you’ll realize that it doesn’t always work out using the very first recorded sound
sample or strategy.  There can be dramatic differences between sound samples… and even between different notes in
the same sound sample. Sometimes it takes several attempts before you capture the essence of the instrument. Having
more than one sound sample to work from is essential if you want to succeed at replicating a specific instrument.  You
can also cheat and start from the patches I put together in the Appendix.
The next step is to spectrum analyze the sound.  Open the recording up in a sound editing program like ‘Audacity’,
highlight one note in the sound sample, and open it up in the spectrum analyzer (menu item  Analyze/PlotSpectrum).
You may need to increase the resolution of the sample in order to see the frequency spikes clearly.  I use sample Size:
2048.  Stretch the window out horizontally as far as possible so you can see the individual peaks on the left side of the
plot easier.
As you move the cursor across the plot a vertical line will snap from peak to peak.  In the numbers below the plot you
can read off the numerical value for each frequency spike.  On the chart below I’ve used a green arrow to show the
cursor line and circled the frequency of the peak it’s pointing to.
On the Clarinet plot below I’ve labeled the peaks 1, 2, 3, 4, etc. according to which harmonic it represents.  Peak number
four will be 4 times the frequency of peak number one, and so on.  We’ll be using these ratios when we program the
synthesizer in a few minutes.  On a ‘Linear Frequency’ plot like the one below all of the harmonics will be equally spaced,
the same distance apart as peak 1 is from the left edge of the plot (half of a grid square).  I picked a Clarinet here on
purpose so you could see an example where one of the harmonics is so low (#2) that you almost can’t see it.  The sound

<!-- page 7 -->

of the Clarinet comes primarily from the loudest frequency spikes, 1, 3, 5, and number 7.  Pay attention to the even
spacing!

Figure 2.  Clarinet Harmonic Spectrum
On the plot above, the scale on the left side is in decibels (db) which is logarithmic.  The volume scaling in our
instruments is also logarithmic, so it’s reasonable to assume we can scale the volumes of each harmonic off the chart
above.  Place the tallest peak #1 at a setting of 99 (the maximum volume).  Peak #3 is at about 80% of full scale so scale
it to a volume of 80, and so on.  The drop in volume between peak #1 to peak #5 is about 10 db, which means harmonic
#5 sounds about half the volume of harmonic #1 to your ears.  Peak #10 is down about 25 db from peak #1 so it sounds
less than 1/4 as loud as peak #1.  Played in the background along with harmonics 1, 3, 5 and 7 you can just hear #10.
Peaks with an amplitude lower than about -70 db can be ignored since they can’t really be heard anyway.
To get the sound exactly right we would need to duplicate harmonics 4, 6, 9, and 10 as well.  We haven’t got enough
capability to do this on a 4-operator synth, but we should be able to do it on a 6 or 8-operator synth.  A 4-operator synth
like the DX11 can get 90% of the way there, which actually sounds pretty good.

5.  Single-Stack Operators
Selecting an Algorithm is the next step in the process.  Below are pictured the algorithms for the DX11 family 4-operator
synths.  You will find similar algorithms in the algorithm charts for the DX7 and FM-X engines, there are a whopping 32
and 88 of them to choose from.   We’re going to start from the simpler chart for the DX11 family, which has an
abbreviated set of 8 algorithms.  The additional algorithms for the 6-OP and 8-OP synths are just expansions on these.  If
you are using a different synth like the Reface-DX, find a similar algorithm for your synth and use that one instead.

<!-- page 8 -->

Figure 3.  Yamaha 4-Operator DX Synthesizer Algorithms
The algorithms represent pictorially how the Operators are arranged in the synthesizer.  In algorithm #1 above, Operator
1 is the Carrier.  The carrier is the Operator you hear, the one that plays the note you press on the keyboard.  It has a
stack of three Modulators on top of it, Operators 2, 3, and 4.  Modulators alter the carrier creating additional harmonics
in the sound.  Operator number four has a line going around it which represents a feedback loop.  The feedback loop
creates additional harmonics for just Operator number four, essentially creating a set of harmonics that mimic a triangle
wave.  It brightens the sound produced by the stack, increasing the number of harmonics the algorithm produces.  With
feedback turned off, Operator 4 produces a simple sine wave like all the others.  Feedback is useful in modeling Brass
instruments.
In algorithm #2 Operators 3 and 4 are both modulating Operator 2, which modulates Operator 1 as the carrier.
In algorithm #8 we have four carriers and no modulators at all.
We’re going to start with the easiest algorithm to understand, number 8.  Algorithm #8 simply adds the output of four
Operators to form the sound you hear.  We can set up a Clarinet by setting our Operators up to mimic the four loudest
harmonics in the sound.  (Use Algorithm #32 on the DX7 and #1 on the Montage.)
Operator
Freq
Vol
Op1

1.00
99
Four individual sine waves
OP2

3.00
80
Op3

5.00
78
Op4

7.00
76
Now go in and adjust the volumes of the four Operators a bit by ear, and it should sound close to a Clarinet.  Adjusting
the volume of each individual harmonic is a bit difficult to do by ear, which is the downside of using algorithm #8.  It’s a
good thing we can estimate the volumes off of the spectrum chart.  This method is called Additive Synthesis, which
doesn’t really use any of the advantages of FM.  It would take eight sine wave Operators used like this to match what FM
can do with just two or three.  Algorithm #8 sounds a bit thin, so we’ll try another algorithm to improve on it, but first
let’s set up the envelope generators.  It’s easier to get the harmonics right when the envelopes are set up so the shape
of the sound is closer to the sound of the actual instrument we’re working on.

6.  ADSR Envelopes - Clarinet
The next step is to set up the way the synthesizer plays each note.  ADSR stands for Attack-Decay-Sustain-Release.  The
Attack rate sets how fast the synth gets from silence up to full volume for the note.  A fast attack rate of 31 on the DX11
(99 on a DX7) means it hits the note hard.  A medium attack rate 15 (55) means it raises the volume of the note slower
and eases into the note smoothly.  A slow attack rate of 2 (16) means it’s going to take several seconds to get the note

<!-- page 9 -->

fully going.  I usually start with a medium 15 (55) and bump it up or down depending upon what the instrument is like.  A
trumpet hits the note harder and faster, a Clarinet takes a bit longer so we’ll try 13 (49).
The conversion chart to convert patches from 4-OP to 6-OP synths is included later in this book for reference.   From
now on I’ll abbreviate the numbers giving the DX11 value first, then the DX7 value in parenthesis.  DX11 (DX7)
If you have an FS1R or a Montage, the envelope rates are expressed as a time and are inverted to the DX7.
Use 99 – DX7Value = MontageValue.
The levels don’t need to be converted on the Montage, they are exactly the same as the DX7.





Figure 4.  An ADSR Envelope

   Figure 5.  Clarinet Note Envelope
Set the envelopes up on all of the Operators the same to start with.  Otherwise, you won’t be able to tell what you’ve
got, the fastest, hardest one will overpower the others.  The envelopes on the modulators need to match the carriers for
now.  For most instruments the harmonics turn on as the note begins, matching the increase in volume as the note
begins to sound.  Setting the Modulator envelopes to match the volume envelope on the Carrier does this quite nicely.
You can make adjustments to the modulator envelopes later, after we get the shape of the notes closer to the actual
instrument.
In reality, a Clarinet has a more rounded envelope (seen in the Figure 5 to the right above) which we approximate with a
rectangular shaped envelope.  We set the Attack to medium 13 (49) the Decay rate to 15 (doesn’t matter right now) the
Sustain rate to 0 (0 and flat) and the Release to 8 (58).  The next button over on the DX11 sets the Sustain Level, which
we set to the max of 15 (99).  This gives us an envelope like the one below.  It isn’t exactly like the real thing above, but
it’s close enough.  If you have a Montage you will find FM-X patches similar to these in Appendix C with the envelope
values laid out in the chart.
Attack Decay Sustain Release
Sustain Level
13(49) 15(55)   0(0)
8(58)

15(99)

DX11(DX7)

                        Figure 6.  Clarinet ADSR Settings
If we wanted to punch the start of the note like you might on a trumpet, one technique would be to lower the Sustain
Level a bit to 12 (46) putting the sharp peak back onto the start of the envelope, and set the Decay rate to 15 (55)
causing the note to drop smoothly to the sustain level, as shown in the ADSR Figure 7 below.  If you set this up on the
modulator only, you get kind of a fast ‘wow’ sound like a Trumpet on the first part of the note.  Modulators, remember,
modify the timbre of the sound, not the volume.
Note:  Setting the Release rate lower than 8 (58) can be used to simulate reverb on the older DX instruments.

<!-- page 10 -->

As another enhancement, I like to set the sustain rate to a slow 2 or 3 (16 to 19) on one modulator and lower the sustain
level a little, then the instrument note will soften and change timbre slightly as it plays a long note, enhancing the sound.
This works great on an expressive instrument like a stringed instrument or a saxophone.
Attack Decay Sustain Release
Sustain Level
13(49) 15(55)  2(16) 8(58)

12(46)

                        Figure 7.  Saxophone ADSR Settings

7.  Double-Stack Algorithms - Clarinet
Example 1……………………………………………………………………………………….
To improve the sound of our Clarinet and go over the types of double-stacked FM algorithms, we’ll start out using
Algorithm #7 which uses one FM carrier/modulator pair and two single Operators.
  (Use #31 on the DX7)
On the Clarinet spectrum plot in Figure 2 the strongest peak is at harmonic #1, the fundamental harmonic.  On a DX
synthesizer we use ratios instead of frequencies, so we will set Operator 3 to a ratio of 1.00.  1.00 means the Operator
frequency is set equal to the fundamental harmonic frequency of the synthesizer, the one you hear when you press
down on one of the keys.  The spacing between the frequency spikes on this plot is twice the fundamental frequency (i.e.
the spacing between peaks 1, 3, 5, and 7 are all 2) so we will set Op4 to a ratio of 2.00.  Listen to how it sounds and raise
and lower the volume of Op4 until it sounds right to your ear.
Operator
Freq
Vol
Op3(5)
1.00
99
Sets the center frequency of the pattern to harmonic 1, all the way to the left
Op4(6)
2.00
69(77) Sets the spacing of the spikes to 2, the volume sets the pattern shape


 The volume of Op4 is set to about I=2.5 here from Figure 1

We will now back fill the slots where the lower peaks occur in the middle of the FM plot (the left two on the mini chart
for 1:2 just above).  We should be somewhere between I=2 and I=3 on the FM graphs above, so we need to boost the
amplitude of harmonics 1 and 3.  Set Op1 to a frequency of 1.00 and set Op2 to 3.00, then adjust their volumes.  The

<!-- page 11 -->

graph for single Operators like Op1 and Op2 look like the graph above where I=0, a single spike.  The sound should now
be much closer to the mellow Clarinet recording we started from.  See the plot below.
Operator
Freq
Vol
Op1(3)
1.00
80
Two individual sine waves, the red and green spikes below
Op2(4)
3.00
80

Example 2……………………………………………………………………………………….
Now let’s switch to Algorithm #5 and fill in the center frequencies a different way, leaving Op3 and Op4 set the way they
are.  Instead of filling the gap with two individual sine waves, we can fill in the gap using another FM modulator/carrier
pair.  We can set up Op1 to the fundamental frequency 1.00, then modulate it to create the side bands and pick up
harmonic #3 using a lower volume on Op2.  Remember the peaks are 2.00 apart, so we lower Op2 to a frequency
spacing of 2.00.
 (#5)
Operator
Freq
Vol
Op1(3)
1.00
99
The center of the FM pattern, the first red peak on the left
Op2(4)
2.00
60(68) The spacing of the red spikes to the right of #1, about I=1.5 in fig 1.

Example 3……………………………………………………………………………………….
The bottom carrier Operators in both of our FM pairs are at the same frequency, 1.00, and the same volume.  We could
use one less Operator if we combined our two modulators Op2 and Op4 onto one carrier.  Looking at the other
algorithms we have to choose from, there are two other algorithms that do this for us, algorithms 3 and 4.  We can save
algorithm 5 for another time.

We’ll pick Algorithm #3 and set the output volume for the top Operator Op3 to 0.0 since we don’t need it.  The result
sounds exactly the same as our previous set up.  We now have two modulators, one set to about I=2.5, the other set to
about I=1.5, and we’re using only one carrier now.

 (#8)
Operator
Freq
Vol
Op1(3)
1.00
99
Carrier

<!-- page 12 -->

Op2(5)
2.00
69(77) Modulator #1
Op3(6)
1.00
 0
Not Used
Op4(4)
2.00
60(68) Modulator #2 (lower volume/Index than Op2)
Example 4……………………………………………………………………………………….
In addition to the three double-stacked algorithms we’ve tried, there is also another variant we can use.  Algorithm #6
provides an entirely different way to combine our modulators.  It uses three carriers and modulates all three using the
same modulator.
 (#22)
Looking at the Clarinet spectrum chart again, all of the even and odd harmonics are separated by the same spacing of
1.00.  In a lot of cases all of the double-stacked algorithms tend to use modulators set to 1.00, hence algorithm 6.  Using
Algorithm #6, we could construct the Clarinet patch by targeting harmonics 1, 3, and 5 and pick up the even harmonics 2,
4, 6, and 8 in between by modulating the three carriers, which is what we’ve done below.  You don’t have the Option of
different modulator volumes, but that isn’t always needed.
Operator
Freq
Vol
Op1(3)
1.00
99
Carrier #1 in blue, far left
OP2(4)
3.00
80
Carrier #2 in blue, middle
Op3(5)
5.00
75
Carrier #3 in blue, right side
Op4(6)
1.00
65(73) Sets the spacing of all the added harmonics in red

The sound is a bit lacking without the 7th harmonic, but I think you get the idea.  We can fix it a little by using the
Feedback feature of Op4, which we haven’t used yet.  Raise the Feedback up to 5 (out of a maximum of 7) to brighten up
the sound a little.  Like we mentioned before, feeding back a sine wave Operator back onto itself forms a triangle wave
which is brighter in timbre than the original sine wave.  It adds more harmonics when used as a modulator this way.

Example 5……………………………………………………………………………………….
Let’s do one more double-stack algorithm example, let’s go back to Algorithm #5 and try something a bit more creative.
We can set up one FM pair to target harmonics 1, 3, and 5, and set up the second FM pair to target harmonics 5, 7, and 9,
with the second carrier centered on harmonic #7.  (Initially I tried 4,7,10 off the plot but it didn’t sound right.)
 (#5)
Operator
Freq
Vol
Op1(3)
1.00
99
Carrier #1
Op2(4)
2.00
69(77) Creates harmonics 1, 3, 5 in Blue
Op3(5)
7.00
60
Carrier #2

<!-- page 13 -->

Op4(6)
2.00
75(83) Creates harmonics 5, 7, 9 in Red


This combination sounds really close to the original Clarinet recording, it’s probably the best one in the bunch.  You can
also start to see that you can get the same type of sound out of several different algorithms.  The algorithm you use has
little to do with the sound that results, it’s how you use the algorithm that matters.  There are actually only a small
handful of algorithms that get used all the time, the rest are mostly ignored.  The number of algorithms doesn’t really
matter all that much, most of the algorithms are there simply because the Yamaha design engineers wanted every
possible combination covered.

8.  Spacing Harmonics Over 2 Apart
Up until now we’ve limited the harmonic spacing to just 1 or 2 when modulating.  It gets more complicated when you go
to 3 or higher… FM doesn’t behave quite like you expect it to, half the time it adds in a few extra harmonics in a
repeating pattern, and half the time it doesn’t.  This is somewhat confusing, so skip over this section if you’d rather.
If you use a large frequency carrier and a smaller modulator (like a 5:1 combination) FM works like you expect it to.  But,
when you have a small carrier and a larger modulator (like a 1:5) it adds in a few extra harmonics.  The extras are
predictable in location for combinations with a 1 in them (the most common combination you will use).  The extra
harmonics get added in between each of the ones you expect to see, they lag the expected ones by two.  So, if you
expect the 6th harmonic, you also get the 4th (see below).  In the 1:5 plot below we expect to see the harmonics 1, 6, and
11, but we also get the 4th and 9th harmonics as extras.  The extras are the result of harmonics in the pattern reflecting
across the 0.0 axis, but it’s a bit difficult explain why that occurs.

Figure 8.  Extra Harmonics 4 & 9

Using other ratios of harmonics with numbers greater than 1 as the lowest one, results in unpredictable extra harmonics.
There are charts out there that show the locations of the extra harmonics, but every combination seems to be different.
Just be aware of this.  We’ll try to ignore the extra harmonics for now in our discussions, just don’t be surprised if you
see a few more harmonics than you bargained for on a live spectrum analyzer plot.

<!-- page 14 -->

9.  Triple-Stack Algorithms - Saxophone
Now that you’ve seen some of the basic concepts, let’s try something a bit more complicated and try out a few
algorithms with a stack of three Operators.  I picked the Saxophone because every single recording I loaded of a
Saxophone was different.  The Saxophone is very expressive, with a lot of variations between individual instruments.
I’ve made some number notations on the plot below to show the harmonics used to construct the patch.  This is just one
way to approach a Saxophone.  You can probably see a better way to model this from the plot below, but I picked this
method for demonstration purposes even though it doesn’t sound all that great.  We’ll switch to a better method in a
minute.
Example 1……………………………………………………………………………………….
Looking at the frequency spectrum chart, there are a series of peaks in the harmonics that are all about three apart
(ignore the blue circles for now) peaks 2, 5, 8, and 11.  We’re going to model these and the harmonics in between using
a three-stack algorithm, Algorithm #3.  First, we pick a base harmonic (peak #2) to center our pattern on, setting Op1 to
2.00.  The spacing between the green numbered harmonic peaks is 3, so we set Op2 to 3.00.  Now we’re going to fan the
harmonics out around each of the peaks we’ve created using our third Operator Op3.  We’ll set the spacing of the fan to
1.00 in Op3 and set the volume on Op3 so it creates just one to two smaller peaks on either side of the center one.  You
can see this much more clearly in the mini plots below.

Figure 9.  The Saxophone Harmonic Spectrum
To help pick up the fundamental harmonic #1 we’ll also use Op4.  Using it to modulate Op1, it will add more volume to
harmonics 1 and 2 if we use a low volume for Op4.  We’ll go over this one step at a time now.
 (#8)
Operator
Freq
Vol
Op1(3)
2.00
99
Main Carrier, the left-most blue peak below
OP2(5)
3.00
70(78) Creates harmonics 2, 5, and 8 in blue
Op3(6)
1.00
65(73) Adds the harmonics in between in red
Op4(4)
1.00
50(58) Helps pick up a little more of the fundamental, shown in green

<!-- page 15 -->

Set up the frequencies in the table above, turn off Op3 and Op4, then listen to the result while varying the volume of
Op2.  These are the harmonics shown above in blue.  Now turn on Op3 and adjust it’s volume, it adds in all the
harmonics in between the others (1,   3,4,   6,7,   9, 10,   12,13) all the red ones.  Adjust the volumes of Op2 and Op3
until you’re satisfied, then go on to Op4.  When you get done it should sound similar to one type of Saxophone.  Not
close enough, though.  We need try something else.  In hind sight, we should almost always choose 1.00 for the
frequency of the Carrier, Op1, it just sounds better overall and is easier to fix if it doesn’t.

Example 2……………………………………………………………………………………….
Ok. So let’s try a totally different method of using the same 3 stack algorithm, but this time we’ll use a big number to
modulate Op2 with Op3 instead of a small one.  Using a large number for Op3 will take the base pattern we create with
the first two Operators, copying the whole thing over to the right.  If you look at the saxophone plot again you will notice
at the bottom of the chart (marked with blue circles) are rounded clusters of harmonics centered around 1, 6 and 11.
We’re going to model these clusters.  For future reference, these clusters are formants which the FS1R can target.
First we create a fan of harmonics around the fundamental #1, then we’re going to copy it over to the location of
harmonic 6 and also to 11 (both are spaced by 5’s to the right).  First, set Op1 to 1.00 and Op2 to 1.00 creating the basic
harmonic pattern around #1, shown in blue below.  Then set Op3 to 5.00 and listen to what it gives you, while adjusting
the volume.
It sounds good, but we can fill in some of the lower harmonics using Op4.  For some reason it sounded better to me
when Op4 was set to 2.00 than 1.00, it needed more of harmonic 3 than it did of harmonic 2.  Remember, the modulator
sets the spacing in between the added harmonics.
 (#8)
Operator
Freq
Vol
Op1(3)
1.00
99
Main Carrier, the left-most blue spike
OP2(5)
1.00
65(73) Creates harmonics 1,2,3 in blue
Op3(6)
5.00
60(68) Copies the base pattern 5 and 10 units to the right in red
Op4(4)
2.00
72(80) Helps pick up more of harmonics 1 & 3 (not shown)

<!-- page 16 -->

Some of you may be wondering if the order of Operations makes a difference, does a 1:1:5 sound the same as a 1:5:1?
Can you swap settings for Op2 and Op3 and get the same sound?  Actually you can, and after listening to both, 1:5:1
sounds a bit brighter and more resonant than 1:1:5 because of the different order of Operations.  Remember the extra
harmonics we mentioned in section 8?  However, with some adjustments to the volumes they will sound about the
same.  Compare the plots above and below.

  Same end result, different order of Operations
Looking at the results on the spectrum analyzer reveals an interesting story.  Below an Index of 1.0 everything behaves
fairly close to our model.  However, if you crank the modulation volumes way up to an Index of 3.0 or greater, the order
of Operations makes a huge difference in the results.  The 1:1:5 construct is filled in near the center and creates a denser,
closer-in fan of harmonics.  The 1:5:1 construct creates a wider fan, with an empty spot in near the center by harmonic 1
and less dense patterns outwards.  In FM-X you can bypass Figure 1 altogether if you want to, using the new waveforms.
There are many other ways to set up a Saxophone patch we could try.  For example, we could go back to double-stack
Algorithm #5 and set up two pairs of FM carrier/modulators.  Use one FM pair to model harmonics 1, 4, and 7, and the
second FM pair to model harmonics 2, 5, and 8.  I’ll leave you to try that one out on your own.
Example 3……………………………………………………………………………………….
What about Algorithm #2?  How do you suppose having two modulators on Op2 could be used in this algorithm?
 (#14)
Looking at the layout of algorithm 2, the additional Operator Op3 is added on top in parallel to Op4.  The intent of this
layout is to give you the ability to widen the frequency fan out.  If you use a 1:5:1 like we did before, you can now
modulate the top harmonic fans using two different modulator volumes.  Set Op3 and Op4 both to 1.00, then set Op3 to
an Index of about 3.0 creating a wide fan, and Op4 to a lower Index of 0.8 creating a narrow fan emphasizing the peaks
in nearer the center.  This is essentially what we did up on the Clarinet the first time we used algorithm 5, remember?
Another Option would be to use different spacings on the two modulators, maybe set one to 1.00 and the other to 3.00.
The algorithms are stacks of building blocks to construct a set of harmonics with.  Be creative and you’ll find you can
model just about any instrument using these basic building blocks.

<!-- page 17 -->

Another 3-Stack Trick
I recently ran across another trick you can use on a stack of three Operators.  If the top-most Operator uses a fixed
frequency rather than a ratio (such as 7.98 hz at a loud volume) you get an explosion of high frequency harmonics.  This
is used in the ‘UprightPiano’ patch on the FS1R.  It adds in a burst of harmonics to model the plural nature of slightly out-
of-tune piano strings, which was then filtered back down into submission so it would sound like a piano.
I’ve also seen fixed frequency Operators used to model the mechanical thunk in a piano when the hammer hits the
strings.  Yamaha used a fixed Carrier frequency of 1.0 hz modulated by a fixed frequency modulator at 94.06 hz.  It
sounded exactly like the action of a mechanical piano in the background behind the main piano harmonics.

10.  Fan Overlap -Interference Patterns
Stacking three or more Operators introduces a new difficulty into the mix.  If the added harmonic fans are wide enough,
the fans can overlap each other.  In the zones where they overlap you get an interference pattern, just like the way
ripples in a pond intermingle.   The pattern is somewhat random, you get a different pattern in the overlap every time
you play a new note.  This changes the timbre of the notes, making a slightly different sound for each note.  If this is
something you want, then great!  You’ve achieved your goal.  If it’s not, you need to correct this by reducing the volume
of the correct moderator.  This type of rolling dissonance is used in creating Piano patches by Yamaha on the FS1R.
Let’s take a look at an example for clarity, a 1:5:1 pattern of harmonics.  We’ll start with a 1:5 pair, pictured below,
which creates three base harmonics, 1, 6, and 11 in blue.  In our 1:5 pattern you can see below that we have four empty
slots in between each harmonic.  If our added fan only had two peaks on each side, the added fan would fit without
interfering with the one next to it.  Instead, we’re going to add a wide fan using a third Operator at an Index of 3.0.  Can
you see how the added fans are too wide to fit without overlapping each other?  (See below.)
The areas where the fans overlap will result in interference, causing a random interference pattern to form.  The
interference pattern causes the peaks in these areas to form at random heights.  Random changes will occur in the
harmonics each time you press a new key to play a new note, sounding slightly different each time.  You can correct this
by reducing the Index value to 1.0 or below on the third Operator by lowering the volume, narrowing the fans added on
by the third Operator in the stack.

What if you were working on a 1:1:5 stack of Operators, which Operator do you think needs the Index value adjusted
this time?  You adjust the middle 1.0 Operator this time.  As a rule, you adjust the modulator with the smallest
frequency ratio, the one that adds on the closest-spaced fan of harmonics to the stack.

<!-- page 18 -->

11.  ADSR Envelopes - Saxophone
We’re going to start with the same basic envelope shape as we did before, the Clarinet and Saxophone are both wind
instruments after all.  After messing around with the envelopes I finally settled on a slightly different approach for
shaping the Saxophone notes.

I used Op2 (a modulator) to shape the timbre of the notes when they are held for longer periods of time, using a Decay
of 4 and Sustain Level of 12.  See below.  This alters the timbre of the sound slowly when a note is held on to.  The slow
rate of 4 lowers the level slowly from 15 down to the lower sustain level of 12.  I also used sustain rates of 2 on all of the
Operators to reduce the volume slightly over time.
Operator
Attack Decay Sustain Release
Sustain Level
Op1(3)
13(49) 31(99) 2(16)
8(34)

15(55)
Op2(5)
13
4(22)
2
8

12(46)
Op3(6)
13
31
2
8

15
Op4(4)
13
31
2
8

15
I’ve found it’s very useful to have two different envelopes per voice, one for the Carriers and another for the Modulators.
One set of envelopes controls the shape of the notes, the other controls the timbre.  Take a look at the instrument setup
charts at the end of this book and you’ll see a large number of examples.

It can also be effective to use a different envelope for each set of modulators for multi-stack algorithms.  On multi-stack
algorithms, it is commonly set up with one stack modeling the instrument attack, and the second stack modeling the
sustain portion of the sound.  You can use one set of envelopes for the note attack, and a second set for the sustain level
when modeling an instrument.

I’ve also seen an Operator stack split used on an FS1R to model different instrument registers.  One stack was used to
model a piano over almost all of the range, and the second stack was used to enhance just the bottom two octaves.  Use
your imagination.  I’m sure you’ll come up with some very interesting patches.

12.  Four-Stack Algorithms
Algorithm #1 on our chart has all four Operators stacked, modulators modulating modulators modulating modulators.  A
number of the DX7 algorithms use this same construct.  What goal would you have in stacking four (or more) Operators,
possibly a wider set of harmonics?  A lot of people seem to like using the 1:1:1:1 stack for some reason in the patch
database I have for the DX11.  I played around with this in a spreadsheet and figured out that a stack of 1:1:1:1 doesn’t
get you anywhere fast.  After the first 1:1 you have to mix in some larger numbers if you want to expand the harmonics
by more than one or two.  A better way to create a wide fan of harmonics would be to use a stack like 1:1:3:6 or 1:1:4:10.
 (#1)
In evaluating all of the four-stack instrument patches I could find, I did find people using stacks of four Operators.  A lot
of them could have been accomplished with a simpler three stack if they adjusted the modulator volumes a bit.  A few of

<!-- page 19 -->

the others mixed in different wave forms into the modulators, like w1:w2:w4:w1.  Using different wave forms changed
the sounds produced.  You just have to use a little more creative thinking when using additional stacked modulators.
Stacking four Operators usually gets too complicated to explain or follow easily.  The fourth modulator expands the
number of harmonics exponentially, creating a real mess to try and use.  For myself, I’ll be sticking to simpler two and
three stack algorithms most of the time.  Dr. Chowning mentioned in one of his interviews that using too many stacked
Operators would eventually get you into trouble since the increased complexity of the harmonic structure would start to
sound more like high-pitched noise than anything useful.  I’ve found that having several sets of two and three stack
Operators are more useful and can model just about anything, especially with additional waveforms like on the DX11,
FS1R, and FM-X on the Montage.
There are a number of four, five and six stack algorithms on the FS1R and in FM-X.  I found one factory four-stack
algorithm used on the FS1R where the top-most modulator was a formant, used to introduce a small amount of fuzzy
dissonance into a piano patch to model the out-of-tune nature of piano strings.  Growl in a Saxophone also looks like this
on the spectrum analyzer.  I have also found a great use though, for multiple stacked operators for complex harmonics
in the Piano and Saxophone.  These instruments have ripples on ripples on ripples in the harmonics, lots of strings equals
lots of sub-resonances (see below).

Looking at the Piano spectrum above you can see there are dominant harmonic groups about 14 harmonics apart, with
more ripples in between.  These can be modeled using a complex stack like a 1:13:4:1.  Note that this combination will
leave a blank spot between the 1st and 14th harmonic when the Modulator volumes are turned up high, you have to fill in
the missing harmonics with a second stack of Operators.  The FS1R with 16 Operators per voice and multiple waveforms
has the advantage here, while the Montage at 8 Operators and multiple waveforms is a close second.  You can also
achieve this second stack by layering two patches into a performance, playing them simultaneously.  Some 6-Operator
VST’s have this feature, giving you 12, 18, or even 24 Operators to work with.
Another detail to pay attention to on the Piano is that below middle C (C3) the second harmonic is dominant (see above).
Above C3 the first harmonic is dominant.  On the FS1R the factory Piano patch layers two patches into a performance to
achieve a high-quality Piano.  One patch adds in the deeper resonance required from C0 up to C3, and the second patch
is active from C0 all the way up to C6.  It’s the best FM acoustic Piano patch I’ve found.

<!-- page 20 -->

13.  Complex Waveforms – DX11 & V2
On the DX11 and TX81Z you can increase the capability of your tools by adding in a set of eight different waveforms.
The additional waveforms are essentially a way to more efficiently use the four Operators you have to work with.  The
waveforms duplicate specific combinations of FM pairs, which can be used to replace similar combinations in your
constructs.  Most of them duplicate 1:1 pairs of Operators.  The different waveforms available are tabulated below, and
are actually arranged in order of increasing brightness.  I was able to create a much more convincing 4-OP Bassoon patch
using the 1:2 W2 waveform, look at the examples in spreadsheet at the end of this book.  You’ll see several patches that
use these different waveforms for the DX11.  The DX7 doesn’t give you this Option.

Wave Description

Carr:Mod
Amplitude

W1
Sine Wave

W2
Odd Partials 1,3,5,7
1:2

I=0.5
V=12

W3
Even Partials 1,2,4,6
1:1

I=0.5
V=12

W4
Partials 1,2,3

1:1

I=1.0
V=32

W5
Partials 1,2,3,5
1:1

I=1.5
V=65

W6
Partials 1,2,3,5
1:1

I=1.7
V=75

W7
Partials 1,3,4,5
1:1

I=3.7
V=85

W8
Partials 1,3,4,5
1:1

I=4.0
V=87

The V2 (in Japan) became the DX11

Complex Waveforms - SY77, TG77, and SY99
These synths also have a set of more complex waveforms, a set of 16 which are very similar in nature to the ones on the
DX11.  The waveforms duplicate specific combinations of FM pairs, 8 that are duplicates of the DX11 waveforms and 8
new ones with similar characteristics.  The graphs in the manual are pretty hard to read, and since I don’t have access to
these synths I’ll leave that up to you guys to dissect.

<!-- page 21 -->

14.  Analog Waveform Patches  - DX7
You might have wondered how to replicate Analog synth patches using FM.  It’s not difficult.  You just have to start with
an FM waveform similar to the Analog ones you want to match.
Triangle Wave:

A Triangle wave sounds pretty close to a Sine^2 Wave.
Operator
Freq
Vol
Op1

1.00
99
Carrier
OP2

2.00
50
Modulator

Square Wave:

Changing Op4 Volume up or down simulates a Filter change.





The Modulation Index (Op4 Volume) controls the Pulse Width.
Operator
Freq
Vol
Op3

1.00
99
Carrier
OP4

2.00
75
Modulator, Feedback = 7

Sawtooth Wave #1:


There are several ways to create a Sawtooth, this is the simplest.






Turn Modulation down to reduce the brightness.
Operator
Freq
Vol
Op3

1.00
99
Carrier
OP4

1.00
75
Modulator, Feedback = 7

Sawtooth Wave #2:


This creates a better Sawtooth, but it uses one more operator.
Operator
Freq
Vol
Op1

1.00
85
Carrier
Op3

1.00
99
Carrier
OP4

1.00
75
Modulator, Feedback = 7

Sawtooth Wave #3:


This one doesn’t require feedback.

<!-- page 22 -->

Operator
Freq
Vol
Op1

1.00
99
Carrier
Op2

1.00
70
Modulator
OP3

1.00
60
Modulator

Sawtooth on the FS1R or Montage:
Use an ODD1 waveform, skirt set to 3 to 6.
This gives you a warm 40% Pulse wave.
Use an ODD2 waveform, skirt set to about 4.
This gives you a brighter 25% Pulse wave.
On the Montage there are also several AWM waveforms that are Sawtooths, Pulses, Triangles, etc.

15.  Troubleshooting Patches
Once you have a patch initially set up, it’s time to make adjustments.  There are a few basic methods of adjusting a
patch to match the recording you are working from.  Below are a few of the most common adjustments.
A. The patch sounds terrible, it’s not even close to the recording even after adjusting the modulators:  You have
something wrong with the frequencies you’ve chosen for the patch.  Go back to the original spectrum chart and
check the frequencies you’ve entered for each of the Operators.  You can check it on a spectrum analyzer too.
B. The patch sounds like it’s higher in frequency than the recording:  Adjust the volumes of the carrier Operators to
make the lower frequency carriers louder.  Or vice versa.
C. The patch sounds like it is thinner in frequency content than the recording:  Adjust the volume of the different
modulator Operators to increase their volume, adding more harmonics into the sound.
D. The patch sounds too smooth and mellow compared to the recording:  Add some variation into the patch by
detuning the Operators.  Detune the Operators by +- 1 to 3 units randomly until you get sufficient variation in
the sound.  The Yamaha Piano patches are detuned this way.
E. The vowel sound of the patch is wrong, it has an ‘mmm’ sound rather than the ‘ah’ sound you want:  This is
caused by formants in the actual instrument and can be difficult to fix if you don’t have an FS1R.  Part of the
problem may be that you targeted a low note in the recording when a more middle-register note would work
better.  You might also have a problem with the modulator volumes.  Sometimes you can change the vowel
sound of the patch by adjusting the volumes of the modulators.  With the FS1R you can change the formant
filter frequencies using Figure 25 and select the vowel sound you want.
After doing this dozens times I’ve noticed a couple of things in adjusting patches.  First, you really need to get the
amplitudes of the first 3 to 5 harmonics correct relative to each other for the patch to sound right.  These harmonics
shape most of the tone of the sound and have to be correctly balanced in order for the patch to sound right. For the
higher harmonics, this doesn’t seem to be as critical.  The second thing I’ve noticed is that matching the spectrum chart
doesn’t quite give you the sound you want, it always seems to be duller than the recording.  This may be the result of
the spectrum analyzer not working quite right.  I always end up boosting the amplitudes of the higher frequency
components to fix it.  I recommend doing this right from the start, if you can hear it.

<!-- page 23 -->

16.  Adjusting Note Registers
We also have to compensate for changes in an instrument’s timbre as it plays higher notes, which was one of the main
points John Chowning made in his original paper back in 1973.  The DX FM synths allow you to adjust this with the
Keyboard Scaling settings.  I’ve found that setting the Level Scaling for modulators helps imitate a real instrument closer.
On the Saxophone I’ve set the Operators on the DX11 to the following, 0:39:0:60 for algorithm 5 (two sets of
carrier/modulator pairs). Using these settings, the two modulators lose intensity as you play up the keyboard lessening
the harmonics generated.  In most real instruments higher notes have fewer harmonics.  It should work the same way
on the DX7.
Brass instruments are the Opposite, they tend to get brassier as the notes get higher and also as the volume increases.
You can model both of these characteristics on your keyboard.  Leave the keyboard scaling set to 0:0:0:0 on the DX11 to
keep the notes brassy as you play up the keyboard. To adjust the volume effect, use the Key Velocity Sensitivity setting
on your modulators.  Raise the setting for the modulators up to a 3 or 6 on a DX11 on your brass instrument patches to
make them brassier as you hit the keys harder.
Another trick I like is to set up the LFO for vibrato with a long delay, so the vibrato doesn’t start until the next measure
of the piece.  That gives you an instrument with no vibrato until you hold the note for an entire measure.  I like to set up
flute patches this way.

17.  Balancing Voices
Once you get all of your patches set up, you need to test them out with a piece of music.  You need to listen to your
patches side by side with others so you can check their volume levels and balance them.  When I set up my first string
ensemble piece to test my string patches, the Bass Viol was way too loud.  It overpowered all of the other instruments
and I had to lower the carrier volumes so it would blend well with the other patches when set to the same volume in a
midi file.  I also found my Flute patch disappeared in a wind ensemble.  I had to increase the Flute’s volume and
shrillness by increasing the volume of the modulators so it could be heard along with all the other wind instruments.
I’ve noticed using the factory patches on several DX keyboards that very few of the patches are balanced with one
another.  It’s not as important here because these keyboards are mainly used as solo instruments.  The Yamaha MU-
series tone generators are much better at balancing voices, since one of their original design goals was to play back
multi-track midi files.  I’ve got an MU-2000 to play with.
Another anomaly that occurred had to do with the Bass Viol patch on the DX11.  I started with a slower Attack on the
notes (an 11 or 12) to allow the instrument to resonate and come up to speed as the note progressed, just like the real
instrument did in the recordings.  However, when played in an ensemble the slow attack sounded like the Bass Viol was
coming in an 1/8 note late on all of the faster notes, which was very disconcerting.  It reminded me of practicing in the
university orchestra when the conductor would stop and criticize the Basses for coming in late.  Playing by themselves it
sounded fine.  Playing with the rest of the orchestra they sounded like they we coming in late.  In hindsight, it was the
note attack.  They weren’t bowing hard enough on the fast notes, the same problem I was having with the Bass Viol
patch.  I shortened the attack timing in the ADSR envelope to fix the problem.

<!-- page 24 -->

18.  Performance Voices
After attempting to match a number of real instruments on a 4-operator synth you may find you still can’t get it quite
right.  Something is missing in the sound you just can’t seem to compensate for.  We have one more trick up our sleeve
that might help.  (This works on the 6-OP and 8-OP synths as well.)  On the DX11 and the other multi-timbral synths you
can set up a Performance where the synth will play more than one patch at a time.  You can double the number of
Operators you have available, turning your 4-OP synthesizer into an 8 Operator synth, by splitting a voice up between
two different patches and playing them together using a custom Performance.  You set the midi input for both
Performance voices to the same channel so they both play from the keyboard at the same time when you play the
custom Performance.  The DX11 can actually play up to 8 different single note patches at the same time.
Editing the two halves of the voice can be tricky.  It’s a bit difficult to anticipate what you’re going to get since you have
to edit each half separately, but you can really increase the capability of your instrument this way.  On the DX11 layering
two voices reduces the number of notes you can play down to 4 at a time, but it allows you to emulate any of the DX7
patches which all use 6 Operators to make up a voice.  Basically this increases your synthesizer up to an 8 Operator FM
synth.  For a good solo patch you really only need two note capability, so you could even increase this up to 16
Operators if you want to.  I don’t recommend going higher than this, though.  The DX11 has a rather chopped note
transition when you play a second note before releasing the first one if you play all eight voices at the same time.
Experiment and see what you come up with.
It’s a bit more complicated to set up, but if there is a DX7 patch you just can’t live without on your 4-Operator synth, this
is one method of getting at it without buying another synthesizer.

<!-- page 25 -->

19.  4-OP to 6-OP Patch Conversion Chart
You can use the following chart to convert backwards, from a 6-OP synth to a 4-OP.  It’s a bit difficult, but it can be done.
You just have to test each portion of the 6-OP patch to determine which part is the most important.  I’ve found by
previewing DX7 patches on the FS1R that many of the patches have one column of 3 or 4 Operators that are doing most
of the work.  The other Operators are redundant, turned off, or don’t contribute much the sound.  I found this
conversion chart online and added a few more details into it.  If you are working on an FS1R or a Montage you can
import DX7 patches directly, there is no need to convert them manually.
Converting 4-OP Patches to 6-OP Synths:

All comparisons were done by ear, between a DX100 and a DX7S.

ALGORITHM: Use the obvious mappings. Two cautions: pay attention when copying
parameters, since you will be mapping Operators 1/2/3/4 to 3/4/5/6.
Also, watch out where the feedback loop is.

DX100
DX7
Operators____
1
1
1234  3456
2
14
1234  3456
3
8
1234     3564  (This one is different…)
4
7
1234  3456
5
5
1234  3456
6
22
1234  3456
7
31
1234  3456
8
32
1234  3456

FEEDBACK LEVEL: Same, although the 4-OP has slightly more "bite" at the same
level. That is, at FBL=7 the 4-OP has more "bite" than the 6-OP does at 7, but the 4-OP
at FBL=6 has less of a "bite" than the 6-OP at 7. You may want to try adding 1 to the
original FBL, and see how it sounds.

FREQ RATIO: Same. All of the 4-OP ratios can be achieved by a 6-OP synth. Of
course, the 6-OP synth should be set for Frequency(Ratio).

DETUNE: Same. Well, almost. 1,2,3 on the 4-OP really come out as 1.5, 2.5, 3.5 on the 6-
OP, but it doesn't have those so you'll have to make do with 1,2,3.  Incidentally, I
don't know about the old DX7, but the DX7S is never in tune on all keys with the DX100.
The variations are all less than 0.2 Hz, but quite audible when you beat sine waves
together. Wasn't this what made the Minimoog sound so good? :-)

OSC. WAVE: If you don’t have a DX11 or TX81Z and this isn't set to 1, sorry. I'd
guess that as long as no more than two Operators use a Wave other than 1, you
could come pretty close by using additional modulators.

ENVELOPE GENERATOR: The 4-OP synth gives you control over four rates (range 0
to 31 on the first three, 0 to 15 on the last) and one level (range 0 to 15).
The 6-OP gives you control over four rates and four levels, all range 0 to 99.

4-OP
      6-OP
  AR  corresponds to  R1
 D1R  corresponds to  R2
 D2R  corresponds to  R3, which defaults to 0 on 4-OP and 10 on 6-OP
  RR  corresponds to  R4


       L1  must be set to  99
 D1L  corresponds to  L2  use the table below


       L3  is set to L2-R3

<!-- page 26 -->

L4  must be set to  0

To convert AR, D1R, and D2R to R1, R2, and R3, multiply by 3 and add 10.
To convert RR to R4, multiply by 6 and add 10.
No, this doesn't quite work out as you approach maximum; you'll have to fudge it a bit.
A value of zero should be set to zero, since this means an infinite time.

The relationship between D1L an L2 is audibly non-linear. Refer to the table below:
  D1L  15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0
  L2   99  96  92  87  82  78  74  70  66  63  60  56  53  50  47   0

 DX100
 DX7

OUTPUT LEVEL: Range 0 to 99 on both, but slightly offset. The 6-OP level is
equal to the 4-OP level plus 8. Yes, this means that 4-OP levels greater than
91 cannot be reproduced by the 6-OP synth. On a carrier, this is easy to deal
with; on a modulator, it is not. Sorry about that. Fortunately, most of the patches I
wanted to convert used a modulator Output Level less than 90.
Of course, the Output Level of the unused Operators should be set to 0.

KEYBOARD RATE SCALING: The 4-OP has a bit of rate scaling even when KRS=0. And on the
DX100 (at least), rate scaling has discontinuities in it, which makes it a tough call to
get *exactly* the same. But this is close:
 4-OP KRS   0  1  2  3
 6-OP KRS   1  2  5  7

KEYBOARD LEVEL SCALING: Start by setting the 6-OP level scaling parameters as
follows: Break Point = A1; L-Curve = -LIN; R-Curve = -EXP; L-Depth = 0. Then
set the R-Depth to 90% of the 4-OP KLS. 99 becomes 90, 50 becomes 45, etc.
This is almost perfect, but not quite; I'd like to hear from anyone who has
refined it. I tried moving the break point and fiddling with the left curve;
it didn't sound any better, and was harder to program.
_______________________________________________________________________________________
There you have it. Following these rules, I converted a variety of the factory presets
from a DX100 to a DX7S; the two were virtually indistinguishable, except that the
DX7S sounded much cleaner.

The LFO, AMS, PWS, AMD, PMD, velocity curve, and pitch envelope are left as an exercise
for the reader. :-) Seriously, I find most of the factory settings for these pretty
wretched, and they are easy to reset by ear.

<!-- page 27 -->

20.  Montage FM-X and the FS1R
One of the biggest improvements in the capabilities of FM instruments is the additional of some really broad harmonic
waveforms.  These synthesizers have a set of waveforms with an almost infinite number of harmonics in them.  Basically,
you can use one Operator all by itself to model an entire stack of DX7 sine wave Operators.
The only place where you can find plots of these waveforms are in an article by Michał Wiernowolski, outlining the
technical details of the FS1R.  The waveforms aren’t even shown on the Yamaha website.  After our previous discussions,
the advantages of these waveforms should be quite apparent (see the plots below).  The details of using these
waveforms are not explained in any of the Yamaha Montage manuals either.

<!-- page 28 -->

Notes on using these waveforms……………………………………………………………………………………….
In these waveforms, the spacing of the harmonics in the ALL1, ALL2, RES1, and RES2 waveforms are determined by the
ratio you select.  A ratio of 4.0 anchors the sound on the 4th harmonic and spaces the harmonics out by four times the
fundamental. It equals a 4:4 FM pair, but with a more controlled set of harmonics.
ALL1 and ALL2 when used as modulators to a sine wave (at a low volume below 60) give you a very high center spike
with a much lower skirt of harmonics.  The skirt rises as the modulation volume rises.  Use these waveforms for modern
pads and sweep patches.
In the RES1 and RES2 waveforms the center point of the filter is selected by the Resonance setting which matches the
number of the peak it’s set to plus one.  Set the Resonance to 4 and it moves the filter maximum to the 5th peak in the
set.  In the plot above, it’s set to 21+1=22nd peak.  Modulating with these waveforms gets messy, you get a continuously
morphing set of harmonics for some reason.  These are best used as additive carriers, for reed and string instruments.
In the ODD1 and ODD2 waveforms the harmonics are spaced by twice the fundamental ratio you select.  Selecting a
ratio of 1.0 anchors the sound on the 1st harmonic and spaces the harmonics out by 2.0.  Selecting a ratio of 3.0 anchors
the sound on the 3rd harmonic and spaces the harmonics out by six.  Used as a modulator at a low volume (just like ALL1
and ALL2) both of these waveforms give you a high center spike with a low fan of harmonics.  These give you a Clarinet
reed sound.
The width of the harmonic fans are determined by the ‘Skirt’ setting.  A Skirt setting of 0 gives you a sine wave.  A Skirt
setting of 1 gives you three harmonics, the center fundamental harmonic and one on either side of it.  The higher the
Skirt setting, the higher the number of harmonics it creates.  The harmonics in these waveforms are also uniform, which
is an advantage over an FM pair like you see in Figure 1.  You get a lot more harmonics with FM-X and much greater
control over them.
For the Formant waveform, the harmonics are always anchored on the 1st harmonic and spaced by 1.0.  The center
maximum of the filter is adjustable to a fixed position determined by the frequency (in hertz) set in the editor.  You can
make the formant move, but that’s a pretty advanced topic.  The Formant waveform is for modeling instruments with a
resonating body like a Violin or Bassoon. However, this waveform is only available on the FS1R, it’s not on the Montage
series of synths.  We’ll address Formants in the next section.
Use the plots above to remind you of the harmonic spectrum each waveform produces.  I’ve found I really haven’t used
the All1/2 or Odd1/2 waveforms very much in modeling acoustic instruments.  The high harmonic content seems to be
better suited to making more modern synthesizer tones with harmonic sweeps, pads, and effects rather than reed, brass,
or string instruments.  You can get some nice harpsichord, organ, and guitar sounds out of them, though.  The ones I’ve
found the most useful are the RES1, RES2, and Formant waveforms, which work well in modeling reed and string
instruments, and instruments with resonating bodies.
Bear in mind I put these patches together on an FS1R using the software editor, which is why the settings graphics below
are what they are.
Example 1………………………………………………………………………………………. English Horn
The waveforms that seem to be the easiest to use for reed instruments are RES1 and RES2.  They form either a triangular
or an arched set of harmonics which you can center by selecting the resonance harmonic.  This’s exactly what’s needed
to match the harmonic structure of lots of instruments quickly.  We’ll use these two waveforms first to model an English
Horn.  Select a recording of a note in the middle of the instrument’s range to match and capture the harmonic spectrum
in Audacity (shown below).

<!-- page 29 -->

The Fundamental harmonic is pretty strong, so we’ll pick it up using Op1 as a Sine wave.  The second group of harmonics
are in a triangular pattern around the 4th harmonic, so we’ll make Op2 a RES1 waveform.  You center it on the 4th
harmonic by setting the Resonance value to 3 (remember the center is actually at Res+1). For the rest of the harmonic
arches, we’ll use the RES2 waveform at harmonics 8, 13, 20, and 29.  Adjust the widths of the harmonic patterns using
the Skirt setting by watching the results on the spectrum analyzer and adjust the amplitudes to match the size of the
amplitude drops on the chart below.  You can almost set the whole patch up without listening to it, it’s that easy.

Figure 10.  The English Horn Harmonic Spectrum
Operator
Type
Freq
Res
Skirt
Vol
Op1

Sine
1.00


85
Fundamental Harmonic #1
Op2

RES1
1.00
3
3
99
Creates a triangle of harmonics at #4
OP3

RES2
1.00
7
2
85
Creates an arch of harmonics at #8
Op4

RES2
1.00
12
7
65
Creates an arch of harmonics at #13
OP5

RES2
1.00
19
2
57
Creates an arch of harmonics at #20
Op6

RES2
1.00
28
7
50
Creates an arch of harmonics at #29


Figure 11.  Algorithm #1 and the Operator Envelopes
Once you get the harmonics and the envelopes set up, listen to the recording and your patch, one right after the other,
to determine what it needs most.  Make changes as necessary to correct the patch.  While listening to a different patch,
the Oboe patch, it sounded a bit thin and needed more of the lowest two harmonics.  I added in another RES2 Operator
targeting the 2nd harmonic to add some volume to harmonics 1 & 2 to richen up the patch.  You can see this patch in the
table in Appendix C in the back.
For the English Horn, it took a few minutes of messing with the envelopes to make it sound more like the recording.  It
still isn’t quite perfect, but the RES1/RES2 method doesn’t allow you to modify the harmonics as the notes develop so
there wasn’t much more I could do.  A better method would be to use Algorithm #6.  Set up a Sine wave at the harmonic

<!-- page 30 -->

you want to target, then modulate it so you can control the harmonic fan.  Do this for the first two groups of harmonics
so you can use an envelope to modify them as the note progresses, then go back to the simpler RES1/RES2 method for
the rest of the harmonics.
Example 2………………………………………………………………………………………. French Horn
Let’s model a Brass instrument this time, the French Horn.  Unfortunately the easy RES1/RES2 method we used last time
doesn’t work at all, it ended up sounding like an artificial organ patch.  I tried a second time using a mixture of methods
and it came out sounding more like a violin, too many high frequency harmonics.  I went after a third audio spectrum
chart with a clear note higher up in the instrument’s register. I also went back to a more traditional FM method, which
requires feedback on one pair of the Operators to get a brassy sound out of it.  That one worked.

Figure 12.  The French Horn Harmonic Spectrum
Most brass instruments can be modeled with a single FM pair, with feedback on the modulator.  We’ll use most of
Algorithm 81 this time.  Op2 will be the main carrier set at 2.0 to match the highest green peak on the chart above, then
it will be modulated with Op1 set to 1.0 with a Feedback level of 6 to create the harmonic fan on the spectrum chart
above in Blue.  Adjust the Feedback up and down so you can hear what it contributes, it adds the brassiness into the
sound.
 Algorithm #81
Operator
Type
Freq
Res
Skirt
Vol
Op2

Sine
2.00


99
Main Carrier in Green
Op1

Sine
1.00


75
Creates harmonics 1,2,3,4,5,6,7 in Blue, Fbk=6
OP5

Sine
9.00


45
Anchors the set on Harmonic #9
Op4

Sine
3.00


80
Creates harmonics 9,12,15 in Magenta
OP3

Sine
1.00


80
Fills harmonics in between 9,12,15
Op6





0
Op7





0
Op8

RES2
1.00
19
4
40
Creates an arch of harmonics at #20 in Red

<!-- page 31 -->

Set up the second set of harmonics next, to catch the small high frequency peaks around 9, 12, and 15 using the Op3-4-5
stack.  These don’t contribute much to the patch, just a few high frequency overtones.  You could skip these and you
wouldn’t even notice the difference much.  I also threw in Op8 to create the last arch of very high frequency harmonics
just for demonstration purposes, but you can’t really hear them, not at -75 db.  Turn Op5 and Op8 on and off to hear the
difference.


   Figure 13.  Carrier Envelopes         Modulator Envelopes
As a slight enhancement, add in a little pitch slide at the beginning of the notes, starting from an Lv0 of -2, and sliding up
to a Lv1 of 0 in a Time1 of 49 with the Pitch Envelope Generator (PEG).  Vibrato helps too, as does a sensitivity of 4 on
the AmpVelocity of the carriers.
To create a Trumpet patch, lower Op2 to 1.0, raise the Feedback to 7, and you’re done.
Example 3………………………………………………………………………………………. Saxophone (ver 2)
Now, let’s attempt the second hardest instrument to model there is, the Saxophone (the most difficult is the Piano).  It
took me forever to get this one figured out, but in the end I think I got it close.  I reworked this one quite a bit to fix it.
The part everyone seems to miss is the high frequency rasp in the instrument’s voice.  Without the raspiness, it just
doesn’t sound right no matter what you do.  It needs a LOT more of the high frequency harmonics than any other
instrument.  The envelopes are critical too, the sound takes time to develop as the reed works up to full vibration.  For
this patch, start with the frequency spectrum chart below and match the harmonics as closely as possible graphically
before trying to tune the sound by ear.

Figure 13.  The Saxophone Harmonic Spectrum Revisited

<!-- page 32 -->

Algorithm #8
First, we’ll model the first three harmonics using a standard FM technique and Algorithm #8.  The first three harmonics
in green and blue we’ll model using a 1:1 FM pair using Op1 and Op2 both at a ratio of 1.0.  Adjust the output volume of
the Synthesizer so that harmonic #1 hits -12 db in the spectrum analyzer with the Operator set to an output volume of
about 94.  This makes matching the rest of the amplitudes off the chart above a bit easier.  Now adjust the volume of
Op1 to get the pattern close to the first three harmonics above in blue on the chart.
Operator
Type
Freq
Vol
Op2

Sine
1.00
94
Main Carrier for the Fundamental #1
Op1

Sine
1.00
71
Creates harmonics 1, 2 & 3
Following that, we’ll use the RES1 and RES2 waveforms to match the rest of the harmonics.  The final values are
tabulated below.  Set the peaks for each center harmonic so you can form a triangle or arch of harmonics at each
location (tabulated below).  Until you add the highest frequency groups in the patch doesn’t sound like a Saxophone at
all.  The higher harmonics add in the growl of the reed.  I also boosted their volume after initially setting them up to
increase the growl so it would sound more like a Saxophone.
Operator
Type
Freq
Res
Skirt
Vol
Op3

RES1
1.00
4
0
88
Creates a triangle of harmonics at #5
OP4

RES1
1.00
8
3
84
Creates a triangle of harmonics at #9
Op5

RES2
1.00
11
0
68
Creates an arch of harmonics at #12
Op6

RES2
1.00
17
2
75
Creates a triangle of harmonics at #18
Op7

RES2
1.00
26
4
68
Creates an arch of harmonics at #27
Op8

RES2
1.00
32
4
59
Creates an arch of harmonics at #33
I used three different envelope shapes for the Saxophone patch, one for the Op1, another for the Op2, and a third for
the high frequency groups of harmonics created by Operators 3, 4, 5, 6, 7 & 8.  The objective was to try and model the
hesitation in the reed vibration at the start of each note.



Figure 14.    Op1 Envelope

Op2 Envelope

Op3, 4, 5, 6, 7, 8 Envelopes

<!-- page 33 -->

I also added a pitch slide into the notes using the PitchEG.  It starts from an Lv0 of -4, then slides quickly with a Time1 of
56 up to a Lv1 of 0.  This helps the realism of the model, since the Saxophone recordings have a bit of pitch uncertainty
at the start of each note.  It would also be great to add in After-Touch control to the patch, allowing you to change the
timbre of the notes and the volume as you change the pressure on the keys to add to the expressiveness of your playing.
The Saxophone is notoriously difficult to model with FM.  There aren’t any decent FM Saxophone patches out there, not
that I could find.  Overall I think the patch sounds OK, especially the lowest notes on the keyboard.  It makes a great bass
Saxophone!  But like all of the patches, it could still use more work.  None of our patches are perfect, but you can get
pretty close if you put some effort into it.
Example 4………………………………………………………………………………………. Violin
Let’s do one more just for good measure.  When I ran the recording of a Violin through the spectrum analyzer I noticed
the formants were moving to the right as the Violin played up the scales, very unlike a wood bodied instrument.  Later I
realized it must be a recording of an electric violin, which doesn’t have a resonating body.  Electric violins have pickups
like an electric guitar mounted near the base of the bridge, or sometimes in the bridge itself.  The result is, FM can
model the electric violin very closely since the harmonics follow the pitch of the note.  You can tell the difference
between different types of Violins using spectrum analysis, which is quite interesting.
The tactic we’ll use this time is a little different, but not by much.  I hope you’re seeing there are a lot of different ways
to combine our building blocks to construct instrument patches.  This time we’re going to use simple sine waves for the
first two harmonics, then we’ll use arches of harmonics created by the Res2 waveform to model the rest of the structure
you see below.  This is basically the same technique we used on the English Horn.
Algorithm #1

Figure 15.  Violin Harmonic Spectrum Chart
Operator
Type
Freq
Res
Skirt
Vol
Op1

Sine
1.00


87
Fundamental Harmonic #1 in Green
Op2

Sine
2.00


87
Harmonic #2 in Green
OP3

RES2
1.00
4
2
99
Creates an arch of harmonics at #5
Op4

RES2
1.00
11
2
70
Creates an arch of harmonics at #12

<!-- page 34 -->

OP5

RES2
1.00
16
2
55
Creates an arch of harmonics at #17
OP5

RES2
1.00
23
2
52
Creates an arch of harmonics at #24
Op7

RES2
1.00
32
2
48
Creates an arch of harmonics at #33
I had to reduce the volume of the first two Sine waves a bit after adding in Op3, since Op3 was maxed out at 99.  A pure
Sine wave has more volume than the arch of harmonics created by Op3 and they needed about the same amplitude in
order to sound right.  Add in the other arches of harmonics next, then adjust their amplitude visually using the spectrum
analyzer.  As a note, Op7 at harmonic #33 is off the chart to the right and is the highest frequency set of harmonics
we’ve used so far.  The Violin has a high frequency raspiness to it that needed to be added in.  On the FS1R I would have
used one of the un-voiced operators which are variable frequency noise generators, but FM-X doesn’t have that option.


   Figure 16.  Violin Envelopes
       Pitch Envelope
The volume envelopes for all of the Operators are the same this time, and a slight pitch slide was set up on the first part
of each note to match the sound of a Violin player.
That wasn’t too hard, was it?  I realize you don’t really need to model any of these instruments on the Montage
keyboards since the AWM2 patches are so precise, but it is useful to know how to match a stringed instrument if a
custom string patch is what you’re after.  You can use a patch like this one to springboard off of, to create something
completely unique.  Your own custom sound is the goal, right?  Customization is the name of the game with FM.

21.  Formants Anyone?  The FS1R
Trying to create a high quality Bassoon patch was driving me up the wall.  I could get a good Bassoon sound for about
one octave with FM, but it kept falling apart outside that narrow range of notes.  I suppose you could set up a different
patch for each octave and set up a Performance to manage them, but there is a much better way to handle it on the
FS1R.  When you spectrum analyze the sound of a Bassoon playing different notes up a scale, you can see that a
different harmonic is dominant on every other note up the scale.  The harmonics move right and widen apart as the
notes increase in frequency, but the amplitude groupings stay in the same place/frequency at the same width.  How do
you model that?  Well, that’s exactly what a formant does.
But first, let’s discuss two major classes of instruments for a minute.  We’re going to divide instruments up into two
categories, instruments without resonating bodies like a pipe organ or piano, and a second class with resonating bodies
for instruments like the violin.  Instruments without resonating bodies include the organ, piano, marimba, the brass
instruments, the electric guitar, and the clarinet, saxophone and the flute fit into this category.  These instruments have

<!-- page 35 -->

a tone generator that changes dimensions for each and every note they play.  On a marimba the wooden keys change
size for each note.  On a pipe organ, there is a different length pipe for each note.  On the electric guitar, the strings
change length for each note as you move your fingers.  On a flute, the tube changes it’s effective length for every finger
hole.  Frequency Modulation works great on these instruments since FM creates a harmonic structure that follows each
note.
The second class of instruments are those with resonating bodies.  Violins, violas, cellos, and basses all have a wooden
body that is fixed in size, it doesn’t change size for each note.  Bassoons and a few other reed instruments are the same,
using a fixed resonating body.  The acoustic guitar is also in this category, along with the human voice tract.  You can also
see formants in the lowest registers of some of the Brass instruments.  FM doesn’t work all that well on most of these
instruments.  You can match the character of the instrument over about one octave with FM, but the match falls apart
as you get further and further away from the center of the patch.  That’s because FM moves the harmonic structure
around with the notes, it doesn’t model the fixed nature of the resonating body.  For that hat trick you need to use
Formants.


So what are Formants you ask?  Well, the simple answer is a Formant is a custom waveform.  It’s created by using a
waveform like the ALL1 waveform which has all of the harmonics in it, then you add a band pass filter to it with a fixed
center frequency.  The fixed frequency filter mimics the resonance of the cavity, like you have with a cello.  The cavity is
a fixed size, hence the fixed frequency of the band pass filter.  The sound going through it, the vibrations from the strings
of the cello, resonate in the cavity.  The cavity resonance gives the instrument it’s unique sound.  When you mix four or
five Formants together at the right set of frequencies and amplitudes you get the signature sound of a Cello, the
Bassoon, or the vowel sounds of speech.
The FS1R has this unique capability, which most people seem to overlook and don’t understand.  It has Formants built
right in!  Yamaha really came up with a powerful combination with this innovation.  By combining Formants with FM the
FS1R can model almost every possible type of instrument there is.  Personally, I think integrating formants is the single
biggest innovation in FM in decades.  Yamaha really hit the ball out of the park with this one!
It surprises me that Yamaha didn’t include many formant patches in the factory set to model real acoustic instruments.
Almost all of the formant patches are synthesizer sounds, vox patches and sweeps.  In fact, most of the factory patches
came up from the DX7 and use only standard FM.  We can fix that.

Free FS1R Editor (the one I’m using):

http://synth-voice.sakura.ne.jp/fs1r_editor_english.html

An Improved Commercial Editor (42 Euros):
http://zeeedit.free.fr/
Example 1………………………………………………………………………………………. Bassoon
The Bassoon is one of the harder instruments to model, so let’s start with that one. We can put together an FS1R patch
using the formants obtained from the frequency spectrum chart from the Bassoon shown in Figure 17 below.  Using the

<!-- page 36 -->

cursor in Audacity, map out the peaks of harmonic groups in the spectrum, both the center frequencies and the
amplitudes for the formant groups.  The formants form the arches in the spectrum chart below.  These arches are fixed
on the harmonic spectrum chart.  As the instrument plays up a scale the little harmonic spikes spread out and move, but
the overall shapes and arches stay in the same place.  That’s the behavior of a Formant.

Figure 17.  The Bassoon Harmonic Spectrum, Formants in Green
Select Algorithm 1 next and we’ll get started building our patch.  We want to add all of the formants together to get our
sound, so we’ll use Algorithm 1 which does this for us on the FS1R.  Note that I ended up shifting the patch down one
octave so I could hit some even lower notes on my keyboard by using a NoteShift of -12 (see below).
 Algorithm #1
I came up with the following set of frequency groupings off the spectrum chart in Figure 17.  The location of each
formant group is labeled in green on the chart.  F7 would have been too quiet at -78 db and too high pitched to hear so I
skipped it.

Formant
Frequency
Amplitude
Adjusted

BandWidth

F1

197

-35 db
86   (121-35=86)
30

F2

462

-22

99   (121-22=99)
40  (or swap to a Skirt of 3 instead)

F3

1192

-42

79   (121-42=79)
40
F4

1984

-57

64   (121-57=64)
60
F5

2645

-72

44  (turned off)
35
F6

3176

-71

50  (turned off)
40

‘Adjust’ the amplitudes by adding a larger number to them (121 in this example) so the highest number in the adjusted
set hits 99 so they can be used to set up the synthesizer.  These will become the volumes we will start from for each of
the formants we’re going to define.  Now select ‘frmt’ as the wave form for six of the voiced Operators, setting the
frequency near the frequencies in the table above using both the coarse and fine sliders in the editor.  Set the volumes
to the ‘Adjusted’ values in our table.

<!-- page 37 -->

Next, you have to go through each one, one at a time, and listen while trying out different band widths.  The band
widths I found that worked the best are listed in the table above.  Too low/narrow and you hear some nasty metallic
resonances, too high/wide and the tone changes from a nice ‘ah’ sound to and higher toned ‘ee’ sound.  The Bassoon
has a low ‘ah’ sound to it.  Adjust these, one voiced Operator at a time, by muting the others momentarily while you
make adjustments.  F5 and F6 didn’t contribute much that was audible, so I turned them off by setting the output
volume to 0.  You can also set the BandWidths by watching the results in the spectrum analyzer.  You will also have to
re-adjust the volumes for each Formant now that the BandWidths have changed them on you.
Making adjustments to the shape of the Formant waveform is done using two different parameters, the BandWidth and
the Skirt setting.  The BandWidth parameter creates an arch-shaped group of harmonics.  The higher the bandwidth, the
wider the rounded arch gets.  The Skirt setting creates a triangle-shaped group of harmonics.  The higher the number
the wider the triangle gets.  Use the Skirt setting for emphasizing the center harmonics if they stick out prominently like
they do on F2 since the BandWidth setting can round them off too much.  When you combine the BandWidth with Skirt
at the same time, you get an arched top with triangular flares on the sides.  We’ve used just the BandWidth setting for
our Bassoon.
The sound envelopes are next.  Go in and set up the EG Shapes for each Operator, setting all of them up the same.  I
used the values below.  These settings mimic a reed instrument like the Bassoon.


Figure 18.  LFO1 and Envelope Generator Settings
For keyboard control, for each carrier Operator set the AmpVelocity to +4, the AmpMod = 4, and the PitchMod = 4,
which are located just to the right of the Envelope Generator panel in the free software editor.  For vibrato, set LFO1 up
like I did in the figure above.  We’re going to create a vibrato using both the pitch and amplitude of the sound.  The
delay is set long so vibrato will start in the second measure of a piece, giving us a flat Bassoon sound until a very long
note is held.  Adjust these to your liking.  You can also trigger vibrato using the Modulation Wheel on the ‘Performance
Control’ panel on the FS1R, but we won’t go over that.  You can play with that on your own.
Pretty stellar Bassoon patch isn’t it, all done using formants!  You could also add in a little bit of air hiss noise at the start
of the notes using a couple of the Unvoiced Operators just for fun.  You could also modify the envelopes for a few of the
formants like we did the modulators on the 4-OP synth patches to add more character to the patch.  Make sure you save
your patch in one of the Internal Voice slots so you don’t lose your work.
Another nice effect you can create is to use mixes of instruments, taking on qualities of each to create something brand
new.  Mix the new Bassoon patch in a Performance with the DX-Clari 2 (H-88) voice patch which is much throatier in the
lower registers to get a new reed instrument with a unique sound.  Layering similar instruments in a Performance can
really increase the depth of the sound.

<!-- page 38 -->

Example 2………………………………………………………………………………………. Cello
For round 2, let’s try a Cello.  I also play the Cello, by the way.  Something interesting showed up in the spectrum
analyzer when comparing the Cello to the Violin and Viola, the Cello harmonics are muted somewhat.  Now why would
that be?  Well, think about how the Cello is held, it’s gripped between the knees and held into the chest.  This damps
some of the harmonics the wood body of the instrument is capable of compared to a Violin or Viola.  If the musician
were to let go of the instrument it would ring more freely, brightening up the tone of the instrument.  Something you
cellists should think about.
This patch was more difficult to zero in on, it took a lot of fiddling with the bandwidths before it started to sound like it
should.  I should have started it visually using the real-time spectrum analyzer.  After reviewing the patch, several of the
chart formants proved to be very soft when soloed by themselves, so F5, F6, F7 and F8 could be turned off.  On second
thought, they may need to be left on since they come more into play when the Cello plays high notes.  We should
probably turn the two formants in the Bassoon patch back on as well.

Figure 19.  The Cello Harmonic Spectrum, Formants in Green
  Algorithm #1

Formant
Frequency
Amplitude
Adjusted

BandWidth

F1

262

-19

99  (118-19=99)
60

F2

589

-24

94  (118-24=94)
47

F3

1371

-45

73


50
F4

1635

-52

66


66
F5

2024

-67

51


35
F6

2606

-61

57


55
F7

3758

-71

42


55
F8

4869

-76

40


55

After doing a few more Formant patches I’ve noticed that the Adjusted volumes are not quite correct.  The fundamental
frequency formant on the left of the chart needs to be boosted some in volume, so I’ve been adding in another Formant
at the same frequency using a Skirt setting of about 3 to boost the volume of the loudest harmonics.  Also, the high
frequency Formants on the right are too loud sometimes and need the volume reduced a bit.  These adjustments are

<!-- page 39 -->

best made using a real-time spectrum analyzer, comparing the differences in amplitude of the real-time peaks to the
recording plot.  Calculate the db drop between a main peak and the next one down, then adjust the volumes to get the
correct difference in db.  On the chart of the recording above, the F2 peak is at -24 db and the F3 peak is at -48 db.  The
difference is a drop of 24 db, which is what you target on the spectrum analyzer to adjust the volume of F3.  Got it?
You might have noticed that the Cello patch sounds a bit too clean.  It’s too nice and neat, it doesn’t have enough
variation in it to match the recording of the real instrument quite like we want it to.  To fix this, go into a few of the
Operators and detune them to add some variation into the patch.  You can leave the two main formants alone, but
detune the higher pitched ones a couple of units up or down.
The envelope settings are shown below, along with the LFO1 vibrato settings.


Figure 20.  LFO1 and Envelope Generator Settings
Example 3………………………………………………………………………………………. Soprano “Hoo”
For round 3, let’s try something completely different and set up a voice/vox patch.  This is what formants were mainly
developed for, modeling human speech.
When most of us sing we select the pitch with our vocal chords and that’s it.  To sing louder we increase the air volume
which is more akin to screaming.  Listen to rock singer like Axel Rose or the lead singer from AC/DC Brian Johnson, this is
the result of too much air flow on the vocal chords.  A trained singer like Luciano Pavorotti or Christina Aguilera however,
tune the cavities in their vocal tract in addition to selecting a note with their vocal chords.  They achieve a quality of note
far and above the rest of us and much more volume.  The harmonic resonances pop out well above the background
formants creating a clear, pure tone.
Looking at the spectrum chart for our female singer patch below, you can see the main harmonic spikes are very
prominent over the formant shapes.  The harmonics on the plot are harmonics of the note she is singing, with the set
being the spikes at F1, F2, F4, F5, and so on, all evenly spaced.  We’ll model these using a 1:1 FM pair like we’ve done
before in previous sections.
For the second part of the patch, we’ll model the formants underneath using the FS1R formant waveforms. The
formants shape the sound underneath, at F1, maybe F2, and under F3.  The formant under F5 is so weak you’ll never
hear it.  There may also be a formant around 3000 hz which is called the “singer’s formant” but I didn’t keep it in the
patch.  The patch sounded cleaner without it.  For a more realistic, raspier voice, leave the 3000 hz formant in the patch.
You can’t really hear it much, not at -78db, but you could increase the volume on purpose to add some character into
the patch.  As it is now, it comes out sounding very flute like.  First we’re going to select Algorithm 6 to test with.

<!-- page 40 -->

Figure 21.  LFO1 Settings
        Algorithm #6 Selection

Figure 22.  The Soprano Harmonic Spectrum, Singing ‘Hoo’
Operator
Wave Freq

Vol
VOp2
Sine
1.00

99
Main Carrier, at F1
VOP1
Sine
1.00

65
Modulator, Creates the harmonics F1, F2, F4, F5
VOp5
frmt
300 hz
99
Voice Formant 1 near F1
VOp6
frmt
700 hz
80
Voice Formant 2 near F2
VOp7
frmt
1100 hz
50
Voice Formant at F3


Figure 23.  Pitch EG and Voiced Operator Envelope Generator Settings

<!-- page 41 -->

The Pitch Envelope Generator (PEG) in Figure 21 is set up to give some variability to the first part of each note, much like
a singer uses to correct the pitch as she sings a note.  I also used the exact same pitch slide on my Trombone patch,
which worked quite well.  It enhances my string patches a bit too, using an LV0 of -2 or -3.
Let’s discuss the human voice for a minute.  The vocal tract is shaped by the lips, jaw, tongue, and throat to form
chambers that alter/filter the sound produced.  These chambers are simulated like we did the fixed body shape of the
Cello using a formant.  Voice formants create different vowel sounds, which are outlined in the table below in Figure 25.
Vowels can be distinguished by using just the first two voice formants (out of five) which is really fascinating when you
think about it.  You can change the frequencies of voice formants 1 and 2 allowing you to change which vowel sound the
patch sings, which is what I did above.  I selected the formant frequencies for a strong ‘oo’ sound off the chart below,
300 hz and 700 hz.  Voice Formants move as you articulate speech, which we’re going to ignore for now.
Vowel sounds seem to be shaped more by the difference between the first two formants, which is 400 hz in this case
(700-300=400).  A third formant was selected at 1100 hz in order to reinforce the 400 hz difference, and to possibly
clarify the vowel enunciation some.  Your voice box can’t do this, but we can on our synthesizers.  This seemed to work.


           Figure 24.  Unvoiced Operator Envelope          Figure 25.  Formant Vowel Sound Settings
Two additional features that are used to enhance most of the Yamaha factory vox patches are vibrato and a slight pitch
change on the first part of the note, which we discussed above.  The settings for LFO1 and the PEG are shown in the
figures above.  We’re also going to add a bit of breath noise to the patch, using two Unvoiced Operators.  The envelopes
for the Unvoiced Operators are shown in Figure 24 above.
Operator
Freq

Vol
UOp1
552 hz
69
Breath Noise, “H” in the word Who
UOP2
880 hz
42


For a male voice patch, listen to the ‘Man_Eh’ patch which is Voice Preset B-92 on your FS1R synth.  It has a fantastic
male bass voice in the lower register.  Like the Soprano patch we developed, it works well over about two octaves, which
is pretty wide for a singer.  Christina Aguilera has about a 2-1/2 octave voice range, which is exceptional.
Playing with just this one aspect of the FS1R will keep you busy for a while.  Try changing the vowel to an ‘ah’ or an ‘e’
just for fun by changing the frequencies for the F1, F2, and F3 voice formants.

<!-- page 42 -->

Example 4………………………………………………………………………………………. Christina1
The last voice patch wasn’t really all that convincing was it, it lacks realism.  After a number of tries on the FS1R to model
voices, I finally bought a Yamaha PLG100-SG card so I could learn how Yamaha sets up life-like voice patches on it.  That
worked.  I learned a lot by analyzing the voices on the SG card, and was able to improve on them with the FS1R.  The SG
card voices have a kind of tinny sound to them though, and only sound good over a very narrow range of notes.  Similar
patches on the FS1R are much better behaved, and sound cleaner and more realistic.  This patch is one I developed, I
analyzed the voice of Christina Aguilera and selected her lower voice register as a model for this patch.  It doesn’t sound
exactly like her, but it is a very high quality voice patch.  I think you’ll like it.  Here’s a link to a Jazz piece using the
Christina1 patch.
https://www.youtube.com/watch?v=IvKTYFWN2Uk


Figure 26.  Christina1 Spectrum Chart


      Figure 27.  LFO1 Vibrato Settings
Operator
Wave Freq

Vol
BandWidth
VOp1
frmt
180 hz
85
20

Lowest Voice Formant F1
VOp2
frmt
485 hz
83
30

Voice Formant F2
VOp3
frmt
1008 hz
61
41

Voice Formant at F3
VOp1
frmt
2961 hz
23
40

Voice Formant at F4
VOp2
frmt
3840 hz
20
20

Voice Formant at F5
VOp3
frmt
5827 hz
20
50

Voice Formant at F6



Figure 27.  Voiced Operator Envelopes and Un-Voiced Operator Envelopes, and PitchEG Settings

<!-- page 43 -->

Realistic voices are much more difficult than you think.  The key seems to be in the control characteristics of the patch
more than the timbre of the formants.  It requires a LOT of Portamento.  Turn the Portamento ON, select ‘mono’ for the
playing mode, set the level to about 75, and select ‘fingerd’ so it only triggers a Portamento slide when you play
connected notes.  The notes need to overlap in the midi file in order for this to work.  Leave in a gap where you want to
start a new musical phrase (with no Portamento).
The patch also requires quite a bit of reverb, I set the send level to 80 and used ‘Hall1’.
To add in some air hiss to the voice, use the Un-Voiced Operators.  Set them all to ‘LinkFF’ so the white noise is in the
same frequency bands as the Formants are.  Set the levels all to around 15 and leave the bandwidths all at 20.  You can
go through each one and fine tune the volumes to further tune the breath noise.

22.  FS1R Tips & Tricks
Trick 1………………………………………………………………………………………. Formant Sequences
When you get tired of fixed tone formants, the FS1R has a few more tricks up it’s sleeve.  The biggest one is that it can
play back entire formant sequences where every aspect of the formants in the synth can be scripted.  It can simulate
speech or sing phrases this way.  Download and test out the FSeqEdit programs available on the web, which can take a
recording and turn it into a formant sequence you can play back on the synth.  They can also turn recordings of more
modern, changing instrument patches like sweeps and morphing pads into FSeq’s as well, with interesting results.  There
is also a Flash FSeq Creator I found on the web which allows you to hear your scripted sequences as you edit them,
before you go to the trouble of exporting them to the FS1R.  I recommend the Fseq Editor I programmed, it has better
tonal quality than the others.  It’s only on Windows, though.  Sorry Apple users.

Thor’s FS1R Fseq Editor:
http://javelinart.com/fs1r-fseq-editor.html

Nifterick’s FS1R FSeq Editor:
https://niff.home.xs4all.nl/fs1r/

Flash FSeq Creator:

http://blog.zacharcher.com/2011/03/14/a-formant-sequence-editor-in-flash/
Trick 2………………………………………………………………………………………. Modulation Bite
The FS1R has less bite when modulating FM Algorithms, not as much growl as the older instruments.  A volume of 99 on
the FS1R is only equal to about 91 on a DX7, and only about 83 on a DX100.  To increase the modulation bite, double up
on modulators.  Use two modulators in parallel to modulate one carrier.  This increases the amount of modulation (the
modulation Index) substantially.
In place of
 use this:

Trick 3………………………………………………………………………………………. Unvoiced Operators as Oscillators
Unvoiced Operators on the FS1R can be used as additional voiced operators if you get the settings right.  This provides
you with 8 more Sine wave oscillators to use in Additive Synthesis, for a total of 16!  Select an Unvoiced Oscillator, set
the Bandwidth to 1 and the Resonance to 7 to stabilize the tone, then increase the volume so you can hear it.  Set the
frequency to 261.6 hz for the Fundamental Harmonic or select a frequency off the chart below.  You now have a fixed
frequency oscillator.  To get the oscillator to follow the keys as you play, increase the FreqScaling up to 99.  On the

<!-- page 44 -->

spectrum analyzer this looks just like a 1.0 ratio Sine wave.  Tuning the oscillator to the harmonic you want it to follow is
a bit trickier than simply selecting a ratio, use the chart below to tune your oscillators to the correct harmonic.

I use this trick all the time on complex patches.  I run out of Operators and need more harmonics to accomplish my goal
without resorting to layering in a second patch in a performance.  Sometimes I start by using these as sine wave
Operators right from the start, knowing I’m going to run out of Operators later on.

23.  Afterward
We covered a lot of ground in this guide, hopefully we didn’t go too fast.  I put in lots of examples to try and illustrate
the concepts of programming an FM synth, and you’ll find a lot more in the appendix to work with.  I hope you find this
instruction book useful, I know I learned a lot of things I didn’t know while putting this together.  Hopefully you didn’t
get too confused as I rattled on.  Learning how to construct a patch from scratch all by yourself is a major
accomplishment.  Pat yourself on the back!  You are now one of a small, select handful of people who actually know how
to program an FM synth!

The FM-X / FS1R Saxophone Patch

<!-- page 45 -->

I thought about putting together a section on special effects, the effects you use to get sweeps and to morph your
patches to add trajectories into the sounds.  The problem with that is it’s very hardware specific.  It’s accomplished
differently on every synthesizer due to the hardware.  This guide is meant to be broader in scope than just one
synthesizer, so I decided to leave that out of this guide to keep it more general.  I hope you don’t mind.
Maybe I’ll write an Advanced FM manual for the FS1R later on.  I tried duplicating the Yamaha VP1 patches on the FS1R,
which was really stretching the envelope.  The timbre of the VP1 changes dramatically as you go up the keyboard and is
really making me think.  For example, on the low end the ResoMetal patch has a plucked Piano tone which turns into an
Asian bell sound like a Gamelan above C3.  Morphing the harmonics this dramatically as you go up and down the
keyboard is quite a challenge.
Have fun!
Best Regards,
Thor Z.
Thor276@Yahoo.com

<!-- page 46 -->

APPENDIX A.  DX11 Instrument Patch Examples (4-OP)
Name:
Alg
F1
F2
F3
F4
Fbk
vol1
vol2
vol3
vol4
W1
W2
W3
W4
AR
D1R
D1L
D2R
RR

ZBassoon
5
5
1
2
1
4
99
76
94
71
1
2
2
1
14
31
15
2
9
Carr.




14
31
15
0
8
Mod.
ZClarinet
5
3
2
1
2
4
90
75
99
69
1
1
1
1
13
15
14
2
9
Carr.




13
15
15
0
8
Mod.
ZFlute
5
2
2

99
73
0
0
1
1
13
13
14
2
9
Carr.




12
13
14
7
8
Mod.
ZFluteWood
3
1
1
1
3

90
65
50
20
1
1
1
1
12
15
15
0
9
Carr.




31
10
14
2
8
Mod.
ZEnglHrn
5
4
1
1
1
4
99
78
94
85
1
1
1
1
14
31
15
2
9
Carr.




14
31
15
0
8
Mod.
ZOboe
1
2
3
1
1
4
99
69
67
68
1
1
1
1
15
31
15
0
9
Carr.




15
31
15
2
5
Mod.
ZSaxophone
3
1
4
1
2
5
92
66
73
66
1
1
1
1
13
31
15
2
9
Carr.




14
4
12
0
8
Mod.
ZTuba
3
1
1
1
1

99
69
54
99
1
1
1
1
15
31
15
0
8
OP123




31
23
0
0
8
Op4
ZTrombone
3
2
1
1
1

99
66
67
60
1
1
1
1
14
31
15
1
8
OP123




31
16
10
1
8
Op4
ZFrenchHrn
3
2
1
1
1

99
66
58
50
1
1
1
1
16
31
15
1
8
OP123




31
15
8
1
8
Op4
ZTrumpet
3
1
1
1
1

99
80
60
99
1
1
1
1
16
31
15
0
8
OP123




31
23
0
0
8
Op4
ZBassBowed
3
2
6
1
1
1
99
72
62
65
1
1
1
1
14
31
15
2
8
Carr.




14
31
15
0
8
Mod.
ZBassPizz
3
2
6
1
1
1
99
60
69
69
1
1
1
2
25
15
15
13
9
OP13




11
14
12
0
8
OP24
ZCelloViola
3
1
7
1
1
1
99
46
78
78
1
1
2
2
14
31
15
2
8
OP13




15
31
15
2
6
OP24
ZCelloPizz
5
1
1
2
1
1
99
64
75
67
1
4
1
2
25
22
15
15
8
OP13




11
21
15
13
6
OP24
ZViolin
3
1
4
1
1
1
99
73
50
74
1
1
2
1
14
31
15
2
8
OP13




15
31
15
2
6
OP24

<!-- page 47 -->

APPENDIX B.  DX7 Instrument Patch Examples (6-OP / Converted 4-OP Patches)
Name:
Alg
F
1
F
2
F
3
F
4
F
5
F
6
Fbk
Vol
1
Vol
2
Vol
3
Vol
4
Vol
5
Vol
6
R1
R2
R3
R4
L1
L2
   L3
    L4

ZBassoon
3
5
1
2
2
2
1
4
99
84
60
94
60
79
52
99
16
64
99
99
91
0
Carrier



52
99
10
58
99
99
94
0
Modul
ZClarinet
5

3
2
1
2
4
0
0
90
83
99
77
49
55
16
64
99
96
88
0
Carr.



49
55
10
58
99
99
94
0
Mod.
ZFlute
5

2
2

0
0
99
81
0
0
49
49
16
64
99
96
88
0
Carr.



46
49
31
58
99
96
80.5
0
Mod.
ZFluteWood
8

1
3
1
1

0
0
90
28
73
58
46
55
10
64
99
99
94
0
Carr.



99
40
16
58
99
96
88
0
Mod.
ZEnglHrn
5

4
1
1
1
4
0
0
99
86
94
93
52
99
16
64
99
99
91
0
Carr.



52
99
10
58
99
99
94
0
Mod.
ZOboe
1

2
3
1
1
4
0
0
99
77
75
76
55
99
10
64
99
99
94
0
Carr.



55
99
16
40
99
99
91
0
Mod.
ZSaxophone
8

1
2
4
1
5
0
0
92
74
74
81
49
99
16
64
99
99
91
0
Carr.



52
22
10
58
99
87
82
0
Mod.
ZTuba
8

1
1
1
1

0
0
99
107
77
62
55
99
10
58
99
99
94
0
OP345



99
79
10
58
99
0
0
0
Op6
ZTrombone
8

2
1
1
1

0
0
99
68
74
75
52
99
13
58
99
99
92.5
0
OP345



99
58
13
58
99
78
71.5
0
Op6
ZFrenchHrn
8

2
1
1
1

0
0
99
58
74
66
58
99
13
58
99
99
92.5
0
OP345



99
55
13
58
99
70
63.5
0
Op6
ZTrumpet
8

1
1
1
1

0
0
99
107
88
68
58
99
10
58
99
99
94
0
OP345



99
79
10
58
99
0
0
0
Op6
ZBassBowed
8

2
1
6
1
1
0
0
99
73
80
70
52
99
16
58
99
99
91
0
Carr.



52
99
10
58
99
99
94
0
Mod.
ZBassPizz
8

2
1
6
1
1
0
0
99
77
68
77
85
55
49
64
99
99
74.5
0
OP35



43
52
10
58
99
87
82
0
OP46
ZCelloViola
16
1
1
7
1
2
1
99
0
86
54
86
60
52
99
16
58
99
99
91
0
OP14



55
99
16
46
99
99
91
0
OP356
ZCelloPizz
5

1
1
2
1
1
0
0
99
72
75
75
85
76
55
58
99
99
71.5
0
OP35



43
73
49
46
99
99
74.5
0
OP46
ZViolin
8

1
1
4
1
1
0
0
99
82
81
58
52
99
16
58
99
99
91
0
OP35



55
99
16
46
99
99
91
0
OP46

<!-- page 48 -->

APPENDIX C.  Montage and FS1R FM Instrument Patch Examples (8-OP)
Name:
Alg
F1
F2
F3
F4
F5
F6
F7
F8
Fbk/Shft
vol1
vol2
vol3
vol4
vol5
vol6
vol7
vol8
ZBassoon
1
1
1
1
1
1
1

99
70
64
60
43
40
Res1
Res1
Res2
Res2
Res2
Res2


ZClarinet
8
1
1

45
99

Odd2


ZFlute
8
1
1

87
99



ZEnglHorn
1
1
1
1
1
1
1

85
99
85
65
57
50

Res1
Res2
Res2
Res2
Res2


ZOboe
1
1
1
1
1

83
99
70
45
Res1
Res1
Res1
Res1


ZSaxophone
8
1
1
1
1
1
1
1
1

71
94
88
84
68
75
59
68

Res1
Res1
Res2
Res2
Res2
Res2





ZTuba
6
1
1
1
4
1
6/-12
80
99
48
60
99



ZTrombone
6
1
2
1
4
7/-12
77
99
60
72



ZFrenchHrn
81
1
2
1
3
9
1
6
75
99
80
80
45
40

Res2


ZTrumpet
81
1
1
1
3
9
1
7
75
99
80
80
45
40

Res2


ZBassBowed
58

1
1
6
2
7/-12

80
62
72
99



ZBassPizz
58

1
1
6
2
7/-12

75
62
72
99






Zcello
6
1
1
1
6
1
1
1
3

75
99
70
80
65
52
99
80

All2
Res2
Res1
All1


Zviola
6
1
1
1
5
4
1
1
1

82
99
55
90
91
80
61
60
All2
Res1
Res2
Res2


ZStringPizz
6
1
5
1
8
1
2
3

62
65
75
45
75
95
50



ZViolin
1
1
2
1
1
1
1
1

87
87
99
70
55
52
48

Res2
Res2
Res2
Res2
Res2

<!-- page 49 -->

Resonance/Skirt
Name:
RS1
RS2
RS3
RS4
RS5
RS6
RS7
RS8
hld
Tm1
Lv1
Tm2
Lv2
Tm3
Lv3
Tm4
Lv4
Op
ZBassoon
3/2
7/1
10/1
15/2
19/2
26/3
0
30
73
25
93
25
99
30
0




ZClarinet

/2
0
30
84
25
99
25
99
30
0




ZFlute

0
8
99
0
99
60
80
33
0
1

0
38
99
0
99
65
99
33
0
2
ZEnglHrn

3/2
7/2
12/2
19/4
28/4
0
30
80
25
99
25
99
30
0




ZOboe
1/1
3/1
7/2
13/2
0
30
80
25
99
25
99
30
0




ZSaxophone

4/0
8/3
11/0
17/2
35/4
26/4
0
5
99
18
99
75
90
30
0
1

0
35
99
0
99
46
95
30
0
2

0
45
99
0
99
46
95
30
0
3-8
ZTuba

0
30
99
20
95
67
90
40
0
1-4

0
10
99
0
99
0
99
25
0
5
ZTrombone

0
40
99
64
98
60
97
40
0
1

0
30
99
20
99
67
91
40
0
2-4
ZFrenchHrn

19/4
0
30
99
20
99
70
90
40
0
2,5,8

0
40
99
30
99
50
97
40
0
1,3,4
ZTrumpet

19/4
0
30
99
20
99
70
90
40
0
2,5

0
40
99
30
99
50
97
40
0
1,3,4
ZBassBowed

0
45
99
20
99
20
99
40
0
6,7

0
35
99
20
99
60
90
45
0
4,8
ZBassPizz

0
13
99
20
99
60
60
40
0
4

0
13
99
20
99
20
99
40
0
6,7

0
13
99
9
99
58
23
40
0
8
ZCelloViola

/0
11/2
15/0
/0
0
35
99
20
99
20
99
40
0




Zviola
/0
9/2
13/2
18/3
0
35
99
20
99
20
99
40
0




ZStringPizz

0
8
98
20
92
45
0
35
0
1-4,7

0
8
98
20
92
50
0
35
0
5,6
ZViolin

4/2
11/2
16/2
23/2
32/3
0
35
99
20
99
20
99
40
0

<!-- page 50 -->

APPENDIX D.  FS1R Formant Instrument Patch Examples (FS + 8-OP)
Name:
Alg
F1
F2
F3
F4
F5
F6
F7
F8
Fbk/Shft
vol1
vol2
vol3
vol4
vol5
vol6
vol7
vol8
FBassoon
1
188
462
1192
1983
2643
3177
4
86
99
79
64
44
50



FEnglHorn
1
294
1179
2359
3010
3840
5891
6782

85
99
78
69
59
55
30



FOboe
1
1070
2082
3010
2657

99
73
75
54



FFrenchHrn
6
1.0
2.0
482
1849
7
80
99
99
62






FTrumpet
6
1.0
2.0
1365
7
80
99
90






FBassBowed
1
302
150
302
532
1205
2005
2805
/-12
80
99
98
91
71
69
40



Fcello
1
261
589
1372
1761
2027
2600
3758
4874

99
94
73
66
35
55
42
40



Fviola
1
440
440
752
1951
3010
4010

90
99
86
74
51
44



FViolin
1
440
520
2082
5008
7807

99
99
91
65
42



Soprano
6
1.0
1.0
301
709
1105

65
99
99
70
50



Christina1
1
180
485
1008
2961
3840
5827

85
83
61
23
20
20

<!-- page 51 -->

Bandwith/Skirt
Name:
Bw1
Bw2
Bw3
Bw4
Bw5
Bw6
Bw7
Bw8
hld
Tm1
Lv1
Tm2
Lv2
Tm3
Lv3
Tm4
Lv4
Op
FBassoon
30
40
40
60
60
70
0
27
99
0
99
46
95
30
0




FEnglHrn
45/2
0/3
60
60
50/2
70
50
0
40
99
0
99
99
85
36
0
1-4

0
48
99
0
99
90
97
36
0
5-7
FOboe
40/3
20/2
65/2
60
0
30
99
0
99
90
95
36
0




FFrenchHrn

/4
/3
0
8
99
66
92
60
90
40
0
1

0
30
99
20
99
67
81
40
0
2

0
25
99
0
99
0
99
30
0
5,6
FTrumpet

/3
0
8
99
68
95
60
94
40
0
1

0
30
99
20
99
67
81
40
0
2

0
25
99
0
99
0
99
30
0
6
FBassBowed
/2
40
40
40
45
45
45
0
50
99
0
99
0
99
42
0
2-7


1
Fcello
60
47
50
70
99
70
56
67
0
48
99
0
99
0
99
42
0




Fviola
/4
50
47
50
50
50
0
45
99
47
99
51
92
40
0
1

0
45
99
0
99
0
99
42
0
2-6
FViolin
/2
60
60
60
60
0
45
99
0
99
0
99
42
0




Soprano
60
47
50
70
65
0
35
82
40
92
80
99
40
0
1,2

0
35
92
66
75
99
80
40
0
5-7
Christina1
20
30
41
40
20
50
0
40
95
75
99
80
93
38
0
1-6