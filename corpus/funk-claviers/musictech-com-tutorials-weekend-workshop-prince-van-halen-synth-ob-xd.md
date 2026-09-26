---
titre: "musictech.com — weekend workshop prince van halen synth ob xd"
source: https://musictech.com/tutorials/weekend-workshop-prince-van-halen-synth-ob-xd/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: synth funk historique
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Weekend Workshop: Create Prince and Van Halen synth sounds with OB-Xd | MusicTech 

 by Dee Jordan 
 January 08, 2021  

 discoDSP TAL Valhalla 
 # Freeware # Weekend Workshop 

 When you purchase through affiliate links on MusicTech.com, you may contribute to our site through commissions. Learn more 

##### Featured Deal
 
 Sony MDR-M1 Closed Monitor Headphones – $40 off for a limited time
 View 

 Tutorials 

# Weekend Workshop: Create Prince and Van Halen synth sounds with OB-Xd
 Build patches inspired by classic 80s synth tracks with this free Oberheim OB-X emulation.

 by Dee Jordan 
 January 08, 2021  

 When you purchase through affiliate links on MusicTech.com, you may contribute to our site through commissions. Learn more 

 Released in 1979, the Oberheim OB-X is a massive-sounding polysynth that shaped the sound of the 80s. With notable uses by Madonna, Prince, Van Halen, Queen and Depeche Mode, the OB-X’s sweet sound was ubiquitous. And although Oberheim tried to improve the OB-X’s winning formula with the OB-Xa and OB-8, for many, the OB-X’s tone still reigns supreme.
 The dicsoDSP OB-Xd is a software plug-in based on the OB-X. It recreates the sound of the original Oberheim hardware while adding new functionality. Notably, OB-Xd uses micro random detuning, a big part of the lush, analogue OB-X sound.
 There are no built-in effects in this synth so we will add chorus in our DAW channel strip. Chorus is a classic synth effect that yields a thicker sound with a wide stereo image. To add space, we will use Supermassive from Valhalla , a reverb capable of otherworldly delays.
 Follow along with this tutorial, where we will re-create several classic OB-X sounds as a starting point for building your own presets.

## What you’ll need:
 OB-Xd from discoDSP, available here . OB-Xd is free for non-commercial use.
 A DAW
 TAL-Chorus, available here 
 Valhalla Supermassive, available here 
 
## 1. Get to know OB-Xd
 
 To create the classic sounds in this workshop, we will not use all OB-Xd’s features; we’ll only cover a few key elements to inspire your sounds.

 For more tutorials on using OB-Xd , visit our archive. 
 Load an initialised preset, by right-clicking anywhere in the plug-in and choose the J3PO factory bank. Right-click again, select programs and choose a default preset. This will give us a good starting point to build our sounds. Play a few notes and listen to the default sound. We are already off to a good start!
 
 An intriguing feature to explore later is X-MOD in the oscillator section. Increasing the x-mod amount will cause OSC1 to modulate OSC2 for bright metallic ring modulation sounds. This, in combination with oscillator Sync, can create a wide variety of timbres.

 This clip is using Cross Modulation to create a sharp metallic sound.
 
 The Voice Variation section lets you dial in eight pan positions for each note trigger, giving you a wide, enveloping sound. There is also a ‘slop’ control to introduce analogue-style unpredictability for the filter, glide and envelope parameters.
 This clip is using Voice Variation to modulate OB-Xd.
 
 Unison mode, in combination with the spread control, can yield very thick sounds. MIDI mapping of external controllers is supported as well. We won’t go into depth here, but it’s worth investigating further in the OB-Xd manual .
 Now that we have covered a few key features, we will move on to re-creating a famous OB-X sound in the next section.

## 2. Van Halen-style Pads
 
 The first sound we’ll make is a punchy pad sound inspired by Van Halen’s Jump from 1983.
 It comprises two detuned sawtooth waveforms with a punchy envelope. Start by loading the default preset. Both sawtooth waveforms are enabled in the default preset, and it is already pretty close to the well-known OB-X sound. We only need to make a few minor tweaks.
 Open the filter to get a brighter sound by turning the cutoff in the filter section fully clockwise. It needs a little more movement, though. We can get that by increasing OSC2 detune past the halfway mark to about two o’clock. The loudness envelope already is set to a fast Attack and short Release, so we are set.
 Here’s what we have so far.

 Now to thicken up the sound, add the TAL-Chorus plug-in to your DAW channel strip. Pull back the dry/wet mix to about 11 o’clock to reduce the intensity slightly. Reduce the stereo width parameter to about three o’clock to make it a little more focused.
 Try it out to make a thicker sound; it should sound similar to this clip.

 The last element in this patch is reverb to give it a small amount of space. Add the Valhalla Supermassive plug-in to your DAW channel strip after the chorus. Supermassive can create wild sounds, but we will create a typical reverb with a short decay by making a few adjustments. Switch the mode to Capricorn for a medium-density reverb. Change the delay amount to 40ms and the Warp amount to 60 per cent. Next, increase feedback to 75 per cent and the density to 100%. Now reduce the mix to about 30 per cent to add more direct signal, so we are not lost in reverb. Give that a listen and adjust as needed.
 This is our final sound. Now you can start jamming with some familiar chords and have something that sounds like this clip.
 
 This is a great synth sound, simple to create, and loads of fun to play. Save your new preset in OB-Xd, and we will move on to the next classic sound.

## 3. Prince’s 1999 Brassy Stabs
 
 In this section, we will create a bright and responsive sound inspired by Prince’s 1999 . It has a similar core as the Jump pad, but we can get a very different sound with a few tweaks.
 Start with a clean slate by loading the default preset again. This sound is made from two detuned sawtooth waveforms, but this time, we will increase one oscillator’s frequency to add more harmonics to the sound. When you enable step mode in the oscillator section, the frequency control moves in semitone increments instead of continuously. Now, adjust the OSC2 frequency to 24 semitones, which is at the 12 o’clock position. You may have to change it by ear to get the right setting.
 Now that we have OSC2 set to a higher frequency, reduce OSC 2 Mix level to the two o’clock position to tame the upper harmonics. Adjust the OSC2 detune control to nine o’clock for an even cleaner sound.
 To brighten the sound open the filter up by turning cutoff to its most open position. This helps pads and stabs stand out in a mix. Don’t worry if this sounds bright when soloed, the chorus we’ll add later will soften that up.
 Listen to the basic sound in this clip.

 Let’s add a subtle amount of vibrato to give our sound some movement. The way to do this is by using the LFO to modulate the frequency of OSC1 and OSC2. Go to the LFO section and increase the rate to the halfway point. Select the sine waveform for the LFO. Enable OSC1 and OSC2 below the frequency knob to make sure the LFO modulates both oscillators. Here’s the part that makes the biggest difference, adjust the LFO Depth to about the seven o’clock position. You can play with this setting to make it more noticeable.
 Here’s a clip with LFO enabled.

 Next, thicken the sound by adding the TAL-Chorus plug-in. Reduce the level to 11 o’clock and pull back the stereo width to two o’clock, so it is not too wide. Enable Mode I and Mode II simultaneously to get a more serious chorus effect.

 A bit of reverb will bring this sound together nicely. Add Valhalla Supermassive next in your plug-in chain. The settings will be the same as we used for the last sound except for the mix. We don’t need a lot of reverb here so reduce the mix to just eight per cent.
 
 Adding some drums and jamming on a few chords, we get this clip.
 
 Now it should be clear why the OB-X has such legendary status. OB-Xd is an impressive emulation by discoDSP. While the plug-in is available for free, you can also purchase it to support the developer.
 Try using these patches as jumping-off points for your sonics meanderings, and spend some time tweaking patches in the OB-X universe.
 Happy exploring!
 Share your results and tell us what tutorials you’d like to see in the MusicTech Creator Community on Facebook. 
 Check out more Weekend Workshops here. 

 discoDSP TAL Valhalla 
 # Freeware # Weekend Workshop 

## Get the MusicTech newsletter
 Get the latest news, reviews and tutorials to your inbox.
 Subscribe 

### Trending Now
 
### 1 Best DAWs for producers, songwriters, engineers and DJs right now 

### 2 Sendy Audio’s Apollo Pro offers class, comfort and smooth tones 

### 3 Serum 2 vs Vital: Do you need to pay for pro-grade synthesis? 

### 4 My Forever Studio: Nick Hakim has your gear on long-term loan 

 Join Our Mailing List & Get Exclusive Deals Sign Up Now