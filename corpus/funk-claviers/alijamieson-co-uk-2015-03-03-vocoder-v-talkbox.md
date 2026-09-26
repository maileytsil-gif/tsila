---
titre: "alijamieson.co.uk — vocoder v talkbox"
source: https://alijamieson.co.uk/2015/03/03/vocoder-v-talkbox/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: synth funk historique
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Talking Synths: Using Vocoders and Talkboxes in your DAW - Ali Jamieson 

 Skip to content 

 Home 
 2015 
 March 
 3 
 Talking Synths: Using Vocoders and Talkboxes in your DAW 

 Vocoders and Talkboxes are often confused in that both sound like synthetic voices and are often created using synths; they also require pretty much zero singing ability to use, which is great if you want to add lyrics to your track without being able to hold a tune. However, that’s where the similarity ends.

 I’m going to explain the difference between the two and demonstrate how you can get both of them working in Ableton and Logic.

## Vocoder

 The vocoder (a portmanteau for voice encoder ) has been around since the 1930s, though the sound is synonymous with music from the 70s and 80s onwards.

 A subtle but well-known example is the intro to Kraftwerk’s 1974 single, Autobahn . It can be heard around 13 seconds in:

 In principle we have two signals: a carrier and a modulator. The carrier’s signal is divided into frequency bands, and the amplitude (volume) of each band is modulated by the corresponding band in the modulator signal.

 The Roland SVC-350. 

 Most commonly this is heard with a synthesiser as a carrier and a voice as the modulator, in effect making the synth ‘talk’ and mapping the harmonic characteristics to the voice. This is one of the most common uses for vocoding, and can be more clearly heard in Giorgio Moroder’s E=MC²  (1979) , Devo’s Beautiful World   (1981)  and Kleeer’s Tonight  (1984) .

## The Science Bit

 Let’s take a brief look at what’s happening under the hood. The carrier signal is analyzed by the vocoder and divided into a number of bands using a band-pass filter. A band-pass filter isolates a frequency ㅡ you can imagine it like a high-pass filter and a low-pass filter stuck together.

 The number of bands is normally somewhere between 6 and 20. Older vocoders typically had fewer bands while while modern ones can have up to 32, and are therefore more detailed.

 You can imagine a vocoder to be a little bit like a Graphic Equaliser but instead of manually amplifying or attenuating each band, it’s actually controlled by the corresponding band in the modulator signal. This is how the characteristics of the modulator are translated to the carrier’s timbre.

 SoundOnSound  has created this handy diagram demonstrating a 10-band vocoder. The amplitude of the modulator signal generates an envelope which is mapped to the same band in the carrier signal. Envelopes create rises and falls in voltage that can control parameters such as amplitude, pitch and filter cutoff frequency etc. In this instance, they control a VCA  (voltage controlled amplifier) of the band. In essence, the amplitude of a band present in the modulator controls the amplitude of the same band in the carrier.

 Image © SoundOnSound 

 How many bands the vocoder has generally determines the quality of the modulator’s signal. Some Vocoders work as an insert effect, needing a carrier to be fed into them, while others are built into a synthesizer that provides that side already. Still others can be synthesizers with the option to take an external line input for the carrier.

 Here are some other tracks that famously use vocoding.

 The ever excellent Ethan Hein has recently compiled this slide show which I think perfectly encapsulates some of the simplicity of the vocoder as well as going into some extra added detail (and discussing auto-tune!)

 The Vocoder, Auto-Tune, Pitch Standardization, and Vocal Virtuosity from Ethan Hein 

## Talkbox

 The talkbox works differently to the vocoder. Some of the most famous incarnations have been of guitarists in the late seventies such as Peter Frampton, for example his song, Show Me The Way from  1975 . The talkbox is exclusively an insert effect, traditionally placed between the guitar’s head and cabinet.

 The talkbox itself is almost like a small amp cone that projects the incoming signal through a thin tube and into the performer’s mouth; making vowel shapes produces the wah-wah like effect it’s famous for. It’s similar to using an electric toothbrush and changing the shape of your mouth.

 Perhaps the first recorded example of the talkbox is from 1974, with Rufus and Chaka Khan’s Tell Me Something Good .

 The talkbox became the signature sound of eighties boogie artist Terry “Zapp” & Roger Troutman: here’s their 1985 16-bit ballad Computer Love  and 2Pac’s interpolated California Love  from 1996, that Roger himself performed on.

 Two other songs that use the talkbox as the main idea (if not a prevalent one) that have had a huge impact on modern music are Bon Jovi’s Livin’ on a Prayer  and Daft Punk’s  Around The World  from 1986 and 1997, respectively.

## Vocoding in Ableton

 Ableton Live comes bundled with a very useable vocoder. I’m using a vocal from an unreleased project with singer Raff . Here’s the vocal in isolation, with just some compression and gating:

 I’ve added a MIDI track ( shift + cmd + t ) and name it Carrier. I’ve added Live’s Analog synth  and drawn some MIDI notes. Here’s our synth sound soloed:

 I’m going to add Live’s Vocoder to the vocal track and, in the Carrier Type drop down menu, select External and select Carrier (or whatever you named the MIDI track) in the External Source dropdown menu.

 Now if we hit play we hear the synths and the vocoded output.

 However we don’t really want to hear the synth, so disable the channel output –Live will cleverly still route it to the vocoder despite it not going to our master output.

 We can embellish the sound a little bit. I’m going to switch Analog to Mono in the Voices panel and turn on the Glide. Now if I extend certain MIDI notes so that they overlap, we get a bend effect in the pitch as they change between notes.

 I’m also going to enable the Noise oscillator and turn it down to -14dB. White noise can help the intelligibility of vocoders as it contains a lot of high frequencies that are present in the human voice. Finally I’m going to enable Oscillator 2 and tune it down one octave and bring the volume down to -4dB.

 In the Vocoder, you can tweak the dry/wet balance to get some of the original vocal mixed in and reduce the number of bands (as mentioned earlier, fewer bands is going to sound more ‘vintage’).

## Vocoding in Logic

 Similarly to Live, Logic comes bundled with a perfectly competent Vocoder, the EVOC 20 Poly Synth , however the setup of it is slightly different. In Ableton, we add the vocoder as an insert to the modulator; in Logic, the vocoder is an instrument and it provides the carrier signal.

 I’ve imported the same vocal used in the previous example in Logic and disabled the output. Notice that even though the track’s meter has signal present, the master is silent.

 Now I’m going to draw some MIDI notes on to my vocoder track. This instrument can function as synth or a vocoder, the default patch being the former.

 To get this working as a vocoder, change the Side Chain dropdown menu to our vocal track and just underneath that where it says Signal, switch that to Voc.

 Some trouble you may run into when using vocals in a vocoding context is that certain syllables (Ss and Ts in particular) can trigger a nasty explosive burst in the upper frequencies, so consider de-essing your vocal.

 In addition, it’s good practice to ensure you’ve gated out any unnecessary breathes, clicks or pops. Low-end can be troublesome, so drastic EQ curves are sometimes appropriate. Finally, you may need to compress your vocal quite heavily to ensure all of it is triggering the Side Chain analysis input. I’ve found a combination of multi-band compression and the above signal path plugins sufficient to getting a great sound.

 The best sound I’ve found is by combining vocoders, e.g using two of EVOC, one providing a solid monophonic bass part and the other an airier pad, or mixing my outboard FAT PCP330  with a more clinical, digital sounding vocoder. There are other vocoder plugins available, too; most noteworthy is the TAL Vocoder  which is free but sadly not compatible with 64-bit for Mac.

 For my final example, I’ve used Logic’s Vocoder in this track Push The Night , chopping up the modulator signal and using a staccato synth pattern for the carrier, sounding something like a malfunctioning speak and spell. The heavy gating on the modulator contributes towards the pseudo glitchy nature. The vocoder patch can be downloaded here .

## Talkboxing in your DAW

 Using a talkbox inside Logic or Ableton is very similar for both, so I’ll condense the two of them into one example. This doesn’t really require any plugins per se (as a guitar/external keyboard can be used) but for simplicity I’m going to use a synth native to Live.

 Firstly, I’m going to create a MIDI clip in Live and add the Analog, but any synth capable of creating good monophonic lead sounds will do (the ES1 in Logic for example). I’ve added a compressor and limiter after the synth to keep it chunky and consistent in volume. Here’s a lead line vaguely based around Heatwave’s 1982 The Big Guns .

 The signal path for this is a little complicated as talkboxes were designed to be used with instrument level  devices and computers send out a much hotter signal. This is how I’ve achieved the best results with my Dunlop Heil Talkbox .

 Next you’ll need to route the audio out of your computer, so you’ll need a soundcard with multiple outputs. I’m using my Avid Digidesign Digi 003 and going out on output 7. In Logic you can set the output to external in the track inspector or in the mixer section, it works just the same.

 Here’s where it gets a little complicated. The talkbox needs to have the signal amplified, but the signal straight out of the computer is too loud for my amp head, so first it needs to run into something to step the signal down. I’m using a Radial ProRMP Reamp  (which I love and have two of).

 This signal is then running into an amp, in my case a Marshall MG100DFX, which then runs into my talkbox. The signal is now being projected out of the talkboxes tube. To get this back into Live, I need to setup a microphone and record it to a new audio track ( cmd + t ).

 And there we have it! A little bit of high-pass filter and some compression to narrow the dynamic range and it’s there. Similarly to the vocoded examples above, it’s worth either gating or manually cutting out any gaps between phrases.

 Vowels are much easier to enunciate with a talkbox (due to the shape of your mouth being open) whereas consonants require more closed mouth shapes that make it far harder to make your talkbox sound intelligible. Mayhem Gets Funky  has a really good YouTube series on how to Talk Talkbox, definitely worth checking out.

### About The Author

#### 
 Ali Jamieson 

 See author's posts 

### Like this:
 Like Loading… 

### Related posts:

 The Ones: Flawless (Logic Recreation) 
 
 Masters at Work: Channel Strip Mastering in your DAW 
 
 The 8 Most Important Synths in the Development of Hip Hop 
 
 Kicks from Scratch: Customising, Sampling and Layering Drums 
 
 NAIVES: Horizon (Ali Jamieson Remix) 
 
 Compress Yourself: Parallel Processing in Ableton Live 
 
 Queens of the Stone Age in your DAW 
 
 Using External Hardware with Ableton and Logic 
 
 Modular How-To: The Expert Sleepers ES-8, Kenton Solo, Poly2 and Malekko Sync 
 
 Measure Once, Cut Twice: EQ Basics 

## 
 4 thoughts on “ Talking Synths: Using Vocoders and Talkboxes in your DAW ” 

 Pingback: NAIVES - Horizon (Ali Jamieson Remix) - Zeroes and Ones 

 are there any vocoder recommendations you have that maybe possibly wouldn’t entirely break the whole bank?

 Loading... 

 Reply 

 Logic and Live both have Vocoders (the EVOP20 and Vocoder respectively) but as for free options there’s a 32-bit vocoder by TAL ( https://tal-software.com/products/tal-vocoder ) it’s a bit fiddly to set up. Outside of that maybe check this link:

 https://bassgorilla.com/7-premium-free-vocoder-vst-plug-ins 

 Loading... 

 Reply 

 Pingback: The Best 15 eBay Synth and FX Finds - Zeroes and Ones 

### Leave a Reply Cancel reply 

 This site uses Akismet to reduce spam. Learn how your comment data is processed. 

## 
 
 Related Stories 

 5 min read 

 Ableton

 Logic

 Modular

### 
 Modular How-To: The Expert Sleepers ES-8, Kenton Solo, Poly2 and Malekko Sync 

 Ali Jamieson 

 16/01/2022 

 17 min read 

 Synthesis

### 
 Forgive me Lord, For I have Synth: A Guide to Subtractive Synthesis 

 Ali Jamieson 

 19/12/2021 

 24 

 5 min read 

 Case study

 Logic

 Production

 Replay

 Sampling

### 
 Chord of the Day: Get Down Saturday Night 

 Ali Jamieson 

 16/12/2021 

## 
 
 Latest 

 9 min read 

 Modular

### 
 Boolean Logic Gates for Eurorack Modular 

 Ali Jamieson 

 13/01/2025 

 10 min read 

 Hardware

 Modular

 Reaktor

### 
 Rebel Technology Open Sound Module & Reaktor 6 

 Ali Jamieson 

 09/01/2025 

 6 min read 

 Case study

 Drums

 Production

### 
 Drums like Block Rockin’ Beats 

 Ali Jamieson 

 08/01/2025 

 17 min read 

 Meta

### 
 A Belated 10 year anniversary post: The past, present and future of Zeroes and Ones 

 Ali Jamieson 

 22/12/2024 

## Discover more from Ali Jamieson

 Subscribe now to keep reading and get access to the full archive.

 Type your email… 

 Subscribe 

 Continue reading 

 %d