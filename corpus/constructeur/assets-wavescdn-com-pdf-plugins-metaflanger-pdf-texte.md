---
titre: "MetaFlanger User Manual (texte du PDF, 23 pages)"
source: constructeur/assets-wavescdn-com-pdf-plugins-metaflanger-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

MetaFlanger

<!-- page 2 -->

MetaFlanger Manual 1
Table of Contents
Chapter 1
Introduction
Chapter 2
Quick Start
Flanger effects
Chorus effects
Producing a phaser effect
Chapter 3
More About Flanging
Chapter 4
Controls & Displa ys
Section 1: Mix, Feedback and Filter controls
Section 2: Delay, Rate and Depth controls
Section 3: Waveform, Modulation Display and Stereo controls
Section 4: Output level
Chapter 5
Frequently Asked Questions
Chapter 6
Block Diagram
          Chapter 7.........................................................Tempo Sync in V5.0.............22
2
3
5
5
5
7
11
11
14
16
18
19
20
Section 5: WaveSystem Toolbar
18

<!-- page 3 -->

Chapter 1 - Introduction
Thanks for buying Waves processors.
Thank you for choosing Waves! In order to get the most out of your new Waves plugin, please take a
moment to read this user guide.
To install software and manage your licenses, you need to have a free Waves account. Sign up at
www.waves.com. With a Waves account you can keep track of your products, renew your Waves Update
Plan, participate in bonus programs, and keep up to date with important information.
We suggest that you become familiar with the Waves Support pages: www.waves.com/support. There are
technical articles about installation, troubleshooting, specifications, and more. Plus, you’ll find company
contact information and Waves Support news.
The following pages explain how to use MetaFlanger.
MetaFlanger’s Graphic Interface
MetaFlanger Manual
2

<!-- page 4 -->

Chapter 2 - Quick Start
For mixing, you can use MetaFlanger as a direct insert and control the amount of flanging with the Mix
control. Some applications also offer sends and returns; either way works quite well.
1
When you insert MetaFlanger, it will open with the default settings (click on the Reset button to reload
these!). These settings produce a basic classic flanging effect that’s easily tweaked.
2    Preview your audio signal by clicking the Preview button. If you are using a real-time system (such as
TDM, VST, or MAS), press ‘play’.
You’ll hear the flanged signal. Briefly speaking, a low frequency oscillator (LFO) varies the delay time of the
‘wet’ audio which, when rejoined with the original audio, produces a huge and creative variety of effects and
pleasant harmonic shifts.
3    Click on the ‘Bypass’ button to hear the raw audio, i.e. your audio track without any flanging effect.
The focus of this Quick Start is on the three prime components that allow us to control MetaFlanger’s LFO
element: Delay, Rate and Depth.
Cl i ck on the Re s et but ton and noti ce how the default Mix set ting is 0.5, i . e . 50% of the ori ginal audio is
a f fected by the LFO, or is ‘ wet’. It’s important to rem em ber you need at least a little percen t a ge of Mix to have
a ny flange ef fect at all . For more ef fect , keep the Mix near 50% (equal mixtu re of wet and dry ) . To redu ce the
f l a n ge ef fect , l ower the Mix percen t a ge - if you lower it all the way down to zero, t h ere’ ll be NO ef fect .
Delay
Default setting: 2.2ms (range is 0 to 20.0ms in 0.1ms increments)
The Delay control sets the general sound of the effect. Lower values (0.1 to 0.5ms) are useful for phaser
effects. Delay settings from 0.5 to 3ms are suitable for flanger effects and finally, 3 to 20ms settings can be
used to achieve chorus effects. These are merely general values. In fact, Flanging can actually take place at
many Delay settings (if the Tape button is engaged). This will be discussed later in the manual.
By the way, to change the Delay value, you can either:
* Click and hold on the Delay text box and drag your mouse up and down
* Click once to select the Delay text box and type in a numerical value
All the control buttons feature similar operation (see the WaveSystem Manual for complete details. You’ll
discover many powerful features built-in to all Waves processors,plus you’ll have an edge on the people who
don’t read it).
MetaFlanger Manual 3

<!-- page 5 -->

To hear the effect of changing the Delay setting, you must have sufficient amounts of Mix, Rate and Depth.
Clicking on the Reset button will give you sufficient settings for your experiments.
Rate
Default setting: 0.2Hz (range is from 0.0 to 20.0Hz in 0.1Hz increments)
Increasing the Rate increases the oscillation speed of the flanger. As you increase the Rate, you’ll notice the
indicator in the Modulation display will sweep from side to side at a correspondingly higher rate. As before,
there must be sufficient Mix, Delay and Depth settings in order to hear and see on the display the full effect
of adjusting the Rate. If you set the Rate to zero, you will hear a “fixed” effect (due to the non-modulated
Delay). A good preset to illustrate this is Queenguitar.
F i n a lly, you can link the Ra te para m eter to the Depth para m eter using the ‘ L i n k’ but ton . This keeps the
Met a F l a n ger ef fect rel a tively the same “f l avor ” at any ra te set ting (by keeping the actual pitch shift the same).
Depth
Default setting: 1.0
The Depth control sets how widely the wet signal is shifted in time, which results in small pitch changes.
This controls how powerful the effect is. The “center” of the changing time delay is set using the Delay con-
trol. In other words,if Depth is 0%, the delay is fixed at the value shown. When Depth = 50%, the delay
time will vary by half of its value. The default Depth setting is 100%, so the Delay time (2.2ms) will vary
between 0.0 and 4.4ms.
Notice the green indicator oscillating back and forth in the ‘Modulation’ display (this display is located
under the Waveform control!). If you set the Depth to 1.0, the green indicator will travel right from one end
of the display to the other (at a speed determined by the Rate setting), and you’ll hear your audio swoosh
accordingly! If you set the Depth to 0.1, you’ll see the same green indicator move from side-to-side, barely
changing its horizontal displacement at all,and you’ll hear a much smaller flange-effect. Zero Depth means
no flanging!
Rate and Depth Link
Default setting: unlinked
Click the ‘Link’ indicator ‘on’ in order to keep the flanger on the same tone while you adjust the Rate or
Depth. The linking keeps the relative pitch depth constant.
Please read about the Feedback,Filters, Tape, Waveform, Stereo and Output Gain controls under their indi-
vidual subheadings in the Controls & Displays Chapter.
Hi n t : The default set ti n gs are easily ch a n ged for radical ef fects by simply ch a n ging the status of phase but ton s
and the Ta pe but ton .
MetaFlanger Manual
4

<!-- page 6 -->

Flanger Effects
Cl i cking on the Re s et but ton sets Met a F l a n ger ’s para m eters for a gentle phasing ef fect (see the beginning of t h e
Q u i ck Start ) . Cl i ck the Ta pe but ton for a classic Flanger ef fect . Ex peri m ent with the Depth and Mix con tro l s .
A high er Mix set ting (nearer 50%) produ ces a stron ger flange ef fect . P l aying around with the Feed b ack
con trol and the Mix phase reverse swi tch wi ll yi eld even more intense ef fect s . Use long Del ay times to
emu l a te analog del ay-line flangers (more on that later ) .
There are several flanger presets in the Load menu,and even more in the external file installed into “Waves
Setup Libraries” folder, called “MetaFlanger Presets II”.
Chorus Effects
Load the ‘Chorus medium’ factory preset.
The two main considerations for producing chorus effects are setting:
1 the Mix low
2 the Delay high
The long delay avoids phasing effects while producing a “duplicate” of the input that is slightly delayed and
has a slightly varying pitch. In general, any chorus effect you produce using MetaFlanger is two-voiced. In
other words there’s the original voice and a second voice (wet audio) that runs behind the original accord-
ing to your Delay setting. (However if you have the Stereo control set to a significant value,then there are 2
varying voices, for a total of three).
For chorusing effects, the rate and depth settings are quite a bit lower than those for flanging or phasing are.
Small changes do a lot.
Experiment with the Depth, Delay, and Rate controls.
Producing a Phaser Effect
For ph a s er ef fect s , the Del ay set ting needs to be low to en su re phasing takes place bet ween the signal affected
by the oscill a ting del ay (i.e. the wet) and the ori ginal sign a l . It is this low del ay that makes Met a F l a n ger act as
a ph a s er ra t h er than a flanger.
Load the Up’n’Down Phaser factory preset. Notice that it has a very short delay of only 0.6 milliseconds.
The Mix and Feedback phase inverse switches are also on, giving an effect with much more edge. Notice the
feedback is rather high(70). This yields a thin sound. Less feedback will make the effect more subtle.
P h a s ers were devel oped using all-pass net works inste ad of del ay lines, with very small shifts of the wet sign a l .
( F l a n gers with del ay lines are discussed in the next ch a pter ) . Th ere were several different ph a s er de s i gns and
MetaFlanger Manual 5

<!-- page 7 -->

e ach had va rying con trols (su ch as Inverse phase on the wet sign a l , m odu l a ting the left and ri ght sep a ra tely,
and so fort h ) . Met a F l a n ger has just abo ut all these con trols and more ,a ll owing you to emu l a te nearly any
classic phase module ra t h er cl o s ely.
The rate in this setting is low, but of course there are no rules! Play with the Rate setting and choose for
yourself the value that best suits your taste. Make noise. Have fun.
MetaFlanger Manual
6

<!-- page 8 -->

Chapter 3 - More About Flanging
What is a flanger?
It is a very re a s on a bly - accepted story that the ef fect call ed flanging was pion eered at Abbey Road stu d i o s
by phys i c a lly app lying pre s su re to a tape - s pool ed ge , or ‘f l a n ge’, to slow the machine down . The setup wen t
l i ke this: t wo (usu a lly iden tical) reel - to - reel machines were put into record and fed the same input , and the
o utp uts from their playb ack heads (Repro mode) were fed to the mixing boa rd . One of the tape outp ut s
was som etimes ph a s e - revers ed (just by pressing the phase but ton on the input ch a n n el ) , for stron ger
ef fect . One of the tape spools was peri od i c a lly bra ked and then all owed to speed up aga i n , u su a lly by the
en gi n eer pressing their thumb on the flange . By the time the Beatles got around to using flangi n g, t h ey
were the second band to do so. The first band’s iden ti ty is app a ren t ly ob s c u re , and several people lay cl a i m
to actu a lly inven ting the tech n i qu e . But there’s ra t h er little do u bt it was at Abbey Road !
George Martin took this situation further by apparently using a variable voltage transformer to very slightly
change the speed of one machine up and down, ranging smoothly between just barely faster than the other
machine to barely slower. Some lucky young studio assistant whose name won’t come to mind at this point
actually mentioned this in a recent interview, and they were hired to simply vary the transformers back and
forth to create flanging, chorusing, and other effects well recognized to nearly everyone who knows the
Beatles records! It’s maybe the only time in history that a low-frequency oscillator had to take a lunch break.
Eventually, this function could be performed using analog delay lines (“bucket brigade”) to take the place of
the tape machines, which had to be rewound every 25 minutes or so. Furthermore, the delay line flangers
could be semi-automated by putting a true low-frequency oscillator into the device, and it didn’t require
bathroom breaks. This LFO would change the delay time of one of the delay lines. Some devices had only
one delay line, but in order to fully emulate the tape machine sound and function, two lines were required
so that one line could go faster and slower than the other line. With only one delay line, you can never go
higher than (ahead of) the dry signal, which gives the effect called “thru the null”, wh ere the signals perfect ly
m a tch and on to the “o t h er side”. It’s the aural equ iva l ent of f lying thru the eye of a needle and a Star Trek
(tm) temporal anomaly simultaneously, giving the famous jet engine swoosh. Of course,that’s what the
MetaFlanger “Tape” button is for. It puts two delay lines into the action (so that the dry is also delayed, but
not varied). Another example of flanging in nature,if we can call it that, occurs when short-wave broadcasts
have multipath interference. In this case, the delay lines are the atmosphere and the ionosphere, which is
extremely expensive and won’t fit in an equipment rack.
Th erefore , you can see that “f l a n gi n g” is not nece s s a ri ly on ly a functi on of the Del ay ti m e , but also a functi on
of what you want to emu l a te . It doe s n’t re a lly matter if f l a n gers have very long Del ay times as long as the
Ta pe but ton is en ga ged . If s o, yo u’ ll simply have lon ger and stra n ger Feed b ack ef fects at your fingertips wi t h
these long Del ay ti m e s . ( In fact , we have factory pre s ets that use long del ay times wi t h o ut the Ta pe but ton in
order to make funky little room reverb s ) .
In the digital domain, we can reproduce traditional dual-tape machine flanging effects by delaying both the
MetaFlanger Manual 7

<!-- page 9 -->

wet and dry signals, varying the dry signal up and down very slightly in pitch, then mixing them together.
The block diagram at the end of this manual shows the MetaFlanger’s design; you can see the two Delay
sections that allow for true tape flanging emulation.3
What is an oscillator?
An oscill a tor produ ces a peri odic waveform . Met a F l a n ger ’s oscill a tor lets you sel ect wh i ch type of w aveform
is gen era ted and con trol the waveform’s amplitu de and frequ ency para m eters . You can con trol the amplitu de
and frequ ency of the peri odic waveform using the depth and Ra te con tro l s .
Why a low frequency oscillator (LFO)?
MetaFlanger’s oscillator operates at low frequencies in order to have slowly changing delay times on the wet
signal. This is emulating the original methods used to create flanging. A high frequency oscillator would be
just too fast! However, we have some factory presets that use the darker corners of the device very well for
alternate effects (rapid pitch shifting) that have no relationship to traditional flanging or phasing. That’s
part of the fun of digital emulation. You can push much further than you can with two tape machines.
Why are there two types of waveforms?
MetaFlanger includes two LFO waveforms: sine and triangle. The sine smoothly varies the pitch; the triangle
produces only two pitches during each oscillation. This probably sounds incorrect, but if you listen to the
100% wet signal,the so-called “triangle” actually is a square wave modulation that alternates between two
delay times, causing the delay output to have two pitches. It is this behavior that gives a triangle “sound” to
the actual flanging or phasing (a constant rate of change between two points, with a sudden reversal or
“corner”at the extremes). Conversely, the sine wave is actually a sine wave, and the flange sound moves
faster in the middle of the sweep and slower near the edges, with no corner at the extremes.
What de we mean by Depth?
The Depth control adjusts the range of sweep of the MetaFlanger’s modulator. When you adjust the Depth
value, you are actually changing the amplitude (level) of the LFO. In audio terms, the pitch varies up and
down more.A small depth (say 10%) will cause the modulator to vary the delay over a small range, result-
ing in a small pitch shift, and therefore a small flanging or phasing effect. Increasing the depth will result in
a greater pitch variation and a stronger effect.
What is the frequency response of a flanger?
MetaFlanger Manual
8

<!-- page 10 -->

A flanger has a frequency response similar to the diagram below
Flanger Frequency Response
The varying delay of the wet audio creates a phase difference with the dry. The mixing of the wet send and
the dry original creates a series of notches commonly known as a comb-filter response because, amusingly
enough, the notches in the graph look like comb teeth!
In fact, some fake flangers were actually devices that had comb-filter equalizers in them (a series of notch
filters) and were “moved”up and down in frequency to emulate the frequency response of a true flanging
effect. However, these filters did not maintain a harmonic relationship to each other (which would be: f, 1f,
2f,3f, 4f, ... nf) so they had a funny flavor that didn’t quite sound right. They had a fixed differential rela-
tionship (so if you had 500, 1000, 1500, 2000, 2500, and moved them up 200 Hz, you didn’t have harmonics
anymore (700, 1200, 1700, 2200, 2700). However, these comb-filter faux flangers have just as much chance
to be abused and misused as anything else, and they do have their own character. The MetaFlanger is not
able to emulate such comb-filter devices,as the comb-filtering that is produced by the real dual delay lines
of the MetaFlanger will always have true harmonic relationships. In fact, our filters have no phase shift (they
are FIR filters) so that even with highpass or lowpass filters, the resulting comb filter sound of the
MetaFlanger still has absolutely perfect harmonic relationships. Finally! You have a perfect relationship that
you can brag about to your friends.
MetaFlanger Manual 9

<!-- page 11 -->

The graph below shows the same frequency response for a flanger with half the delay, and the same depth.
Flanger Frequency Response (1/2 the previous Delay)
As you can see,the minimum points appear at larger intervals, and are wider apart.
When you change the delay over time, the resulting frequency response can be imagined as a comb-teeth
spring stretching out as the delay decreases and compressing as it increases. It is the movement of these
‘notch’ filters that creates the flanger-effect. When the Delay control of MetaFlanger is set to a low value (e.g.
0.8ms), the result is a deeper effect on one frequency range (phasing).
MetaFlanger Manual
10

<!-- page 12 -->

Chapter 4 - Controls & Displays
Please refer to the Wave Sys tem manual for a full de s c ri pti on abo ut how to use Waves con tro l s , su ch as
cl i cking and dra gging on text boxe s , typing in nu m erical va lues and so on . We recom m end you invest the
time re ading the Wave Sys tem , as it inclu des many great tips and tri cks on how to get the most from the
s t a n d a rd Waves plug-in con tro l s . Af ter you have re ad it, you can app ly the knowl ed ge acqu i red to all our
p lu g - i n s . It wi ll save you a lot of time and give you power that you can re a lly use everyd ay. Some peop l e
i gn ore this and don’t find out abo ut these po tent fe a tu res of Waves proce s s ors for a long ti m e .
Some of the information regarding the Delay, Rate and Depth controls is repeated here for convenience.
MetaFlanger’s interface is divided into four sections.
1. On the far left you can see the Mix, Feedback and Filter controls.
2. The Delay, Rate and Depth (and rate/depth link) controls and Tape button are in the next section.
3 . Con ti nuing left to the third secti on we have the Waveform but ton and accom p a nying display up top,
a dynamic Modu l a ti on display and Stop but ton in the middl e , and finally a Stereo con trol with its
own display on the bo t tom .
4 . The last secti on of Met a F l a n ger on the far ri ght inclu des the Outp ut fader, l evel displays (left and
ri gh t ) , peak level meters with clip lights (also for left and ri ght - cl i ck on these to re s et them!) and
nu m erical pe a k - l evel displays bel ow the meters .
Mix, Feedback and Filter Controls
MetaFlanger Manual 11

<!-- page 13 -->

Mix
Default setting: 50%, range is from 0 to 100%
To get flanging, you must have a mix of dry and wet signals. When the Mix is set to 50%, it means that there
is an equal balance of dry and wet signals. If there is no feedback, the maximum effect is at 50%. If there is
sufficient Feedback (which is heard only on the wet signal), you can get a stronger effect by raising the Mix
control above 50%. Setting the mix close to 100% will let you hear just the wet signal. There’s lots to explore
in that region that has little to do with flanging or phasing (such as the Reflective Room presets).
To adjust the Mix:
Click and drag your mouse up or down on the Mix button, or click on the Mix button to select it and type
in a new value numerically.
Mix Phase Inverse
Next to the Mix control is its phase button. Click this button to invert the phase of the wet audio. When the
wet signal has its phase inverted,stronger effects occur. The effect is an increased boost or cancellation of
some frequencies according to the flanger’s depth and delay.
Feedback
Default setting: 50%, range is from 0 to 100%.
Wh en the feed b ack is set to 50%, it means fifty percent of the wet signal is fed back to the input . ( F i f ty
percent is 6dB bel ow unity ga i n . To keep just a little sanity at the top en d , you can’t qu i te actu a lly get to
u n i ty gain even though set to 100%.) Raising the percentage of feedback increases the effect, whatever it is
at the time. As you raise the value to seventy or eighty percent feedback, you’ll start hearing longer regener-
ation (as some devices called it, such as the famous MXR gray stomp box Flanger). With long delays, high
feedback produces blurring trails (rapid repeating delays) which, if properly pitch-shifted, can be very satis-
fying. (Try the Blurr or the MXR Gray Stomp Overboard presets.) Of course, a setting of 0% means zero
Feedback! To get an idea of really high feedback levels, try the Massivo Feedbacko, Excite Me, or
Shimmering Heck presets. They can be rather noisy (and loud), so Be Prepared.
Th ere’s a lot more in the ex ternal file call ed “ Met a F l a n ger Setup Libra ry ” because all of t h em simply wo u l d n’t
fit in the Load menu . Use the Load but ton and sel ect Open File; n avi ga te to the Waves fo l der and find the
Waves Setup Libra ries fo l der.
Inv Feedback
Next to the Feed b ack con trol is its phase but ton . Cl i ck this but ton to reverse the phase of the feed b ack sign a l .
Inverting its phase gre a t ly com p l i c a tes the signal (assuming Feed b ack set ti n gs ) , and can re a lly put an ed ge on
a ny setu p.
MetaFlanger Manual
12

<!-- page 14 -->

Filter
Default setting: off,high pass filter at 0.4kHz; each filter has a range from near-0.0 to 20.0kHz.
This control puts an FIR filter into the wet signal path (which affects the feedback signal as well, of course)
so that only part of the signal is affected.
The Filter button is divided into two parts:
1 Filter-type select button (toggles between a low or high pass filter)
2 Frequency setting control (sets the corner frequency of whichever filter is selected)
Filter-Type Select Button
You can choose between a low or high pass filter. Simply click on the Filter button itself to toggle from one
to the other.
Frequency Setting Button
Click and drag your mouse up or down on the Filter button, or click on the Filter button to select it and
type in a new value numerically.
The filter options provide you with accurate, frequency-specific effects.
Remember the filters only affect ‘wet’ audio. You can use the filter selection to either flange higher frequency
signals and leave the lower frequencies alone, or vice versa. As mentioned, the default setting is a high pass
filter set to 1.0kHz (see the screenshot below). If you switch this filter ‘on’, signals below 1.0kHz will not be
flanged. In other words, low frequency signals will not be flanged, such as a bass guitar’s fundamentals,
while still flanging the higher frequency harmonics of the bass guitar. Why would you want to do this? Well,
if you flanged the entire bass guitar, the cancellation notches would affect the fundamental frequency (main
note), so the fat part of the bass would vary in volume, coming and going. By flanging only the higher har-
monics, the bass stays fat, but has a swirling flanged upper texture. Most likely you’ll use the highpass filter
much more than the lowpass, but we don’t want to cramp your style.
High Pass Filter at 1.0kHz
MetaFlanger Manual 13

<!-- page 15 -->

To flange only lower frequencies, click on the filter button to set it to low pass mode (seen below). This
time, signals below the 8kHz point will be flanged, while signals above this setting will be unaffected. This
can be very useful for simply emulating the lack of high-frequency response in vintage delay-line flangers as
well as more obscure effects.
High Pass Filter at 8.0kHz
Delay, Rate and Depth Controls
Delay
Default setting: 2.2ms (range is 0 to 20.0ms in 0.1ms increments).
This control sets the base delay of the effect. The default Delay setting of 2.2ms is useful for general flanging
applications.
Here’s a rather general set of guidelines: 0.1 - 0.5ms for phaser type effects, 0.5 - 3ms for flanging and
3 - 50ms for chorus effects.
The default setting is an average delay time for general flanging applications. You can reduce the delay to
around 0.8ms for a different flanger effect, or raise the Delay up to around 15ms for fuller chorus effects.
The Delay control combines with Rate and Depth to alter the sweep of the modulator. (Again, if you use
the Tape control, everything becomes a flanger for the most part, although you can do “phaser” emulations
with small Depth settings, you just have a long Delay that is relatively unneeded.)
To adjust the Delay:
Click and drag your mouse up or down on the Delay button, or click on the Delay button to select it and
type in a new value numerically.
MetaFlanger Manual
14

<!-- page 16 -->

Tape
Default setting: off
Switching the Tape button ‘on’ (click on the indicator and it lights up green) causes the dry audio to be
delayed equally to the wet delay, so that when modulated, the wet delay time varies shorter and longer than
the dry. As previously stated, this is the only way to get true tape-flanging emulation,and many other
devices (including vintage delay-line flangers) don’t offer this. In the old days, this was purely for monetary
reasons, as delay lines were very expensive. These days, although it is still a resource issue for DSP imple-
mentations, as it uses twice the memory, it’s not a big deal. Without the dual-delay architecture
(Tape mode), the sound would never go “thru the null point”; it only approaches it, then moves away again
(as in the Up and Down Phaser preset). For an example of true tape-flanging sound, load the Total Null or
Ampex 440 factory preset.
Rate
Default setting: 0.2Hz (range is from 0 to 20Hz in 0.1 steps)
This control sets the frequency of the LFO in Hz. Increasing the Rate increases the oscillation speed. As yo u
i n c rease the Ra te , yo u’ ll noti ce the indicator in the Modu l a ti on display wi ll sweep from side to side at a
corre s pon d i n gly high er ra te. You can link the Ra te para m eter to the Depth para m eter using the ‘ L i n k’ but ton .
Ra te can be set all the way to 0.0. You might ask,“ why would I want to do this?” In a way, a Ra te of 0.0 make s
the flanger be stu ck at a fixed poi n t , so you can use the Met a F l a n ger to cre a te a non - m oving ton a l i ty. Try the
Q u eenguitar factory pre s et and put a nice lead rock guitar into it. Th ere’s no way to know ex act ly how Bri a n
May and his en gi n eer got those guitar sounds, but this pre s et at least puts you in that directi on . Load
Q u eenguitar and ex peri m ent with the Del ay or the Depth to con trol the tone of the non - m oving ef fect .
NOTE: There must be sufficient Mix, Delay and Depth settings in order to hear
and see on the display the full effect of adjusting the Rate.
To adjust the Rate:
Click and drag your mouse up or down on the Rate button, or click on the Rate button to select it and type
in a new value numerically.
Depth
Default setting: 1.0
The Depth con trol sets how wi dely the wet signal is shifted in ti m e , wh i ch re sults in small pitch ch a n ge s .
This con trols how powerful the ef fect is. The “cen ter ” of the ch a n ging time del ay is set using the Del ay
con tro l . In other word s , i f Depth is 0%, the del ay is fixed at the va lue shown . Wh en Depth = 50%, t h e
Del ay time wi ll va ry by half of its va lu e . As an ex a m p l e , the default Depth set ting is 0.5 (50%) and the
Del ay 2.2ms, t h erefore the time del ay of the wet audio ch a n ges from 1.1 to 3.3ms. This can be ob s erved
vi su a lly in the ‘ Modu l a ti on’ d i s p l ay.
Ta ke another ex a m p l e . Wh en Del ay = 10ms and the Depth is set to 30% the del ay time wi ll ra n ge from 7 to 13 ms.
MetaFlanger Manual 15

<!-- page 17 -->

Remember that the center of the changing time delay is set using the Delay control. If Depth is set to 0.0,
then the Delay time will be fixed at the displayed value.
To adjust the Depth:
Click and drag your mouse up or down on the Depth button, or click on the Depth button to select it and
type in a new value numerically.
There must be a certain amount of Mix and Delay in order to hear the effect of adjusting the Depth. Finally,
it is possible to link the Depth parameter to the Rate parameter as will be explained in greater detail below.
Rate and Depth Link
Default setting: unlinked
If you want to ad just Ra te and Depth toget h er maintaining the same ra tio bet ween them , cl i ck the ‘ L i n k’
i n d i c a tor ‘on’ (it lights up green ) . Wh en linked , ad ju s ting ei t h er para m eter causes the other to ch a n ge too.
The link curve keeps the flanger ’s ef fect rel a tively constant by keeping the pitch va ri a ti on the same no
m a t ter what ra te set ting you ch oo s e . In other word s , i f you don’t have them linked , and you increase the
ra te , the pitch va ri a ti on wi ll increase (by Dopp l er ef fect ) , and the ef fect yo u’ve caref u lly de s i gn ed becomes more
u nwi el dy. By using the Link con tro l , the ef fect stays ste ady because the actual pitch va ri a ti on is con tro ll ed by an
i nverse rel a ti onship bet ween Ra te and Dept h .
NOTE: the maximum time of the Delay is 50ms, so if you have a very high Delay time, the
Depth control will have an “upper limit” imposed to avoid modulating past the 50ms limit.
Running off the end of a delay line doesn’t sound good at all. Otherwise you might start reading
some memory from a Word document in the background or something (actually, not likely), so
MetaFlanger controls the Depth range automatically.
Waveform, Modulation Display and Stereo Controls
Waveform
Default setting: sine wave
Cl i ck to sel ect ei t h er a sine or tri a n gle LFO wave modu l a ti on . The tri a n gle wave has on ly two pitch e s , while the
sine wave gives you a smooth va ri a ti on from the highest to the lowest pitch . This fact abo ut the tri a n gle wave-
form may sound incorrect , but if you listen to the 100% wet sign a l , the so-call ed “tri a n gl e” actu a lly is a squ a re
w ave modu l a ti on that altern a tes bet ween two del ay ti m e s , causing the del ay outp ut to have two pitch e s . It is this
beh avi or that gives a tri a n gle “s o u n d ”to the actual flanging or phasing (a constant ra te of ch a n ge bet ween two
poi n t s , with a su d den reversal or “corn er ” at the ex trem e s ) . Convers ely, the sine wave is actu a lly a sine wave , a n d
MetaFlanger Manual
16

<!-- page 18 -->

is moving faster in the middle of the sweep and slower near the ed ge s , with no corn er at the ex trem e s .
The Waveform button is accompanied by a graphic display that shows which waveform is selected.
Triangle
Modulation Display
The Modulation display shows you graphically how the LFO parameters dynamically change when you alter
the Rate and Depth settings. Please read more about the Rate and Depth controls in order to understand
how they relate to this display. If for some reason the display annoys you, double click it to make it disap-
pear (double click on it again to make it reappear).
Stop button for modulation
The stop button “freezes” the modulator wherever it is when you click it. As soon as you click it again, it
starts at the same point in the modulation where it stopped. By automating this button, you can decide
exactly where in the flanging sweep you want to start, and as soon as it does,the current value of the Rate
control is resumed. This is ideal for flanging a drum submix or other part of a song that you want to
process very exactly, starting at a certain part of the modulation sweep.
Stereo
Default setting: 0 degrees
Ranging from 0 to 180 degrees, this control does not change the phase of the outputs, but instead, sets the
phase between left and right LFO’s. “Stereo” controls the Left/Right Modulator phase, which can definitely
yield a stereo output. If the value is 180 degrees, then the Left side is flanging down while the Right side is
flanging, up, and so forth. By careful setting of this Mod phase control, (especially at lower values) beautiful
stereo swirls and choruses can be achieved, very nearly providing 3-voice chorusing and other effects.
One classic device that had this feature was the Mutron Biphase.
To adjust the Stereo:
Click and drag your mouse from side to side on the Stereo button, or click on the Stereo button to select it
and type in a new value numerically.
Signal Level Displays & Controls
MetaFlanger Manual 17

<!-- page 19 -->

Signal Level Displays & Controls
In most cases you’ll leave the Gain fader on zero unless you have high-level input signals. However, some
settings with higher Feedback and Inverse phase settings can produce rather large increases in peak values,
so you might have to reduce the Gain even further to avoid clipping. With some settings or high-level
inputs, audible clipping can occur internally even if not indicated on the output clip meters.
To change the value,simply raise or lower the Gain fader by dragging it to the new level. Its range is
f rom -12.0dB to +12.0dB. Th ere are clip meters above the outp ut level meters (on the left and ri gh t
ch a n n el s ) . Th ey tu rn red wh en the signal outp ut clips - cl i ck on these red indicators to re s et . Th ere is
also a nu m erical pe a k - l evel display under the fader that shows the ex act level to one decimal place ; cl i ck
d i rect ly on them to re s et .
MetaFlanger Manual
18
WaveSystem Toolbar
Use the bar at the top of the plugin to save and load presets, compare settings, undo and redo steps, and
resize the plugin. To learn more, click the icon at the upper-right corner of the window and open the
WaveSystem Guide.

<!-- page 20 -->

Chapter 5 - Frequently Asked Questions
What’s the difference between the sine waveform and triangle waveform?
Met a F l a n ger inclu des a low frequ ency oscill a tor. The shape of the waveform of this LFO determines how
the del ay in Met a F l a n ger va ries in re s pect to ti m e . The tri a n gle waveform has on ly two pitches at the
m a x i mum and minimum points of the LFO’s waveform . The sine waveform sweeps the pitch from the
m a x i mum to minimum points in the LFO’s waveform . This fact abo ut the tri a n gle waveform may sound
i n correct , but if you listen to the 100% wet sign a l , the so-call ed “tri a n gl e” actu a lly is a squ a re wave
m odu l a ti on that altern a tes bet ween two del ay ti m e s , causing the del ay outp ut to have two pitch e s . It is
this beh avi or that gives a tri a n gle “s o u n d ” to the actual flanging or phasing (a constant ra te of ch a n ge
bet ween two poi n t s , with a su d den reversal or “corn er ” at the ex trem e s ) . Convers ely, the sine wave is
actu a lly a sine wave , and is moving faster in the middle of the sweep and slower near the ed ge s , with no
corn er at the ex trem e s .
Why does the MetaFlanger distort sometimes, even without the clip meters lighting up?
The clip meters are only for the output, not for internal clipping. Internally there are several other places
clipping can occur and to put meters at every spot would make the plug-in take considerably more power.
Clipping can occur if you have a high-level signal (above -10dBFS) rather easily because of the very nature
of the processor, which adds a copy of the signal onto itself, plus optional phase reversals and time shifts.
This can produce peaks much higher than the original input signal. The best thing to do is lower the input
level to avoid such clipping. It’s the nature of the beast to produce higher peaks.
When I move the Depth or Rate control to get “manual” flanging there is clicking noise
(zipper noise). Why?
Ma nu a lly ch a n ging the Depth or Ra te con trol makes the Del ay time jump in fairly large steps (severa l
m i ll i s econ d s ) . In this case, cl i cking wi ll occ u r. We hope to provi de a way for manual flanging in a futu re
revi s i on that wi ll have smoothing on the Del ay ti m e . Wh en the LFO con trols the Del ay, time shifts are
very smooth so there is no cl i ck i n g. This is why the Stop but ton is there , wh i ch at least all ows you to
pin point ex act ly wh ere the ef fect wi ll start (i.e., up high or down low, etc . ) .
MetaFlanger Manual 19

<!-- page 21 -->

Chapter 6 - MetaFlanger block diagram
Only one channel is shown. Delays are equal when unmodulated.
MetaFlanger Manual
20

<!-- page 22 -->

MetaFlanger Tempo Sync
MetaFlanger can sync to host tempo. This enables it to lock to the host
application’s tempo and link the relevant controls to that externally controlled
tempo.
A new control labeled “Sync” has been added. Sync has two modes: A (Auto) and M
(Manual).
The “Rate” button has been enhanced with a new drop-down menu which enables a
quick selection of some predefined and commonly used subdivisions of the beat
(quarter notes, etc).
If the “Sync” button is in Manual mode, MetaFlanger functions as it did in V4, where
the “Rate” control determines the modulation rate in Hertz (cycles per second).
However, if the “Sync” button is in Auto mode, then MetaFlanger is locked to the
tempo value set by the host application. In this case, the “Rate” button changes its
function from “Rate (Hz)” to “Rate (x/Beat)”. This indicates that the value being set in
the control determines the number of modulation cycles per beat, while the number
of beats per minute (BPM) is determined and controlled by the host application
tempo.

<!-- page 23 -->

For example, if “Rate” is set to 3.00 and the host’s tempo is 120 BPM (or 2 beats per
second) then the modulation rate will be 3 cycles per beat, which in this case will be 6
cycles per second (6Hz).
That's it! Sync MetaFlanger to your latest mix and you're ready to flange to the groove
- with the new Waves MetaFlanger 5.0!