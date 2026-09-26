---
titre: "soundonsound.com — synthesizing hammond organ effects"
source: https://www.soundonsound.com/techniques/synthesizing-hammond-organ-effects
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: claviers électromécaniques
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Synthesizing Hammond Organ Effects 

 Skip to main content 

 Set us as a Google preferred source preferred 

 facebook 
 twitter 
 email 
 print 

## You are here
 Home 
 Techniques 

# Synthesizing Hammond Organ Effects

 Synth Secrets 

 Synthesizers > Synth Secrets , Synthesis / Sound Design 
 By Gordon Reid 
 
 Published January 2004 

 Photo: Richard Ecclestone 

 So, you can synthesize a Hammond's tonewheel generator — but what about its all-important effects? This month, we look at recreating the Hammond's percussion, vibrato, overdrive, and reverb — and find that it's harder than you might think...

 I find that my relationships with my synths can be much like any other romantic entanglements... fun and frustration in turns. When you're lucky, everything comes naturally, and you attain what you crave both easily and quickly. On other occasions, you have to work hard at things, and sometimes you just have to give up, pretending that you weren't that interested in the first place.

 For the past two months, I think that it's fair to say that this series has been dishing up a good deal of the former, with the basis for some fine tonewheel organ patches being produced on some unlikely synths. But, as I wrote when I left you last time, what these have all lacked is the excitement introduced by the Hammond's effects and side-effects; percussion, chorus/vibrato, leakage, and overdrive. So now, we're going to attempt to spice things up still further. Unfortunately, as in real life, some relationships start out as fun, but lead to frustration, although you usually learn some important lessons on the way. In this case, even though we don't necessarily achieve everything we set out to do, there's plenty to be learned about how a tonewheel organ creates its distinctive sound along the way.

## Matching Registrations 

 Just across the room from where I'm writing, there sits one of greatest organs ever crafted by human hands: a Hammond A100, an instrument every bit the equal of the B3 and C3. If you're unacquainted with Hammond genealogy, let me explain...

 For many decades, the company had a policy that its 'spinet' organs (those with four-octave keyboards) had built-in speaker systems, while the larger 'console' organs (those with five-octave keyboards) required external speakers, or 'tone cabinets'. Sometime after the launch of the B3 and C3 in 1955, Hammond's customers made it clear that they wanted a self-contained organ with the wonderful sound of the new flagships, but also the reverb and internal speakers of the less expensive spinets. Thus was the A100 born: a B3/C3 tonewheel generator and controls mounted inside a smaller case that nonetheless includes a spring reverb, dual valve amplifiers and three chunky speakers.

 So close is the relationship between the B3, C3 and A100 that there is nothing to stop you from sliding the tonewheel generator out of one and wiring it into the others (well, nothing other than a few hundred wires!). This means that the A100 is the superior of the three organs, because it sacrifices nothing, but takes up less room and adds the reverb and speaker system. This superiority is not borne out by the second-hand prices of these models, which baffles me, but there it is.
 Figure 1: Returning to the Juno 6 Hammond patch. 

 Anyway, having the Hammond sitting just a few feet from my Juno 60 makes it simple to investigate and resynthesize each of the Hammond's effects. So, to start, I'm going to match the sounds of the two instruments such that applying the same effect to each should yield the same result.
 Figure 2: The Juno patch lacks the depth of 88 8000 000, lying closer to 67 8000 000. I do this by switching off the percussion and chorus/vibrato effects on the A100, limiting the volume somewhat, and making sure that I don't play the result through the attached Leslie rotary-speaker system. Now, if I play the Juno patch that I developed two months ago (see Figure 1 above) through a high-quality amplifier/speaker combo, while simultaneously playing the Hammond through its own speakers, the similarity is almost uncanny, provided that I match the Hammond's registration to imitate the Juno. This is necessary because — despite my best efforts in the November 2003 installment  — the synthesizer patch is not quite a true emulation of 88 8000 000.

 Most obviously, the amplitudes of the three primary harmonics lie closer to a Hammond registration of 67 8000 000, with the 8' pitch most audible, and lesser contributions from the 5 2/3' and 16' pitches, as shown in Figure 2 (above). Figure 3: Increasing the resonance of most filters reduces the low-frequency amplitudes of low-frequency signals passing through them. 

 This result suggests that, by using the filter to synthesize the 5 2/3' drawbar, we are sacrificing some of the amplitude of the sub-oscillator. This is not altogether surprising. In fact, it is exactly what we would expect from most analogue filters, because high filter resonance usually suppresses lower frequencies, as shown in Figure 3, above.
 Figure 4: The registration 67 8321 000 is much like the Juno patch. Listening more closely reveals that the Juno not only lacks the low-frequency 'oomph' of the Hammond's 88 8000 000 registration, but is also a tad brighter. As a result, a touch of the next two or three Hammond drawbars makes the two instruments sound even more similar. After a few minutes' comparison, I found the registration 67 8321 000 to be about right (see Figure 4).

 Again, this is not surprising. After all, we would not expect the Juno filter to eliminate everything above the cutoff frequency, even when oscillating. This explains the need for the low-level signals injected by the 4', 2 2/3' and 2' drawbars.

 Figure 5: The percussive 'blip'. Anyway, having matched the sounds of the two instruments, we're now in a position to move on to...

## Hammond Effects — Percussion 

 A Hammond's percussion has nothing to do built-in rhythm units. That is, there are Hammonds with such units built in, but when I say Hammond percussion, I'm not talking about them. No, the four percussion controls on an A100 allow you to add a greater or lesser amount of either the second or third harmonic of the 8' pitch — ie. of the 4' or 2 2/3' drawbar — as an accent at the start of the note. The amplitude 'shape' of the result is therefore as shown in Figure 5.

 Figure 6: Creating second-harmonic and third-harmonic percussion using modules. It's worth pointing out that adding percussion also reduces the loudness of the sustained part of the note, but we're going to overlook this. Likewise, Hammond percussion is polyphonic, but of the single-triggering variety, so if a previous note is held, the percussion does not sound. Again, we'll overlook this, because trying to recreate it would take us into areas best not trodden in an article of this length.

 Returning to the four percussion controls on the A100, the On/Off switch is self-explanatory, as is the Second/Third selector. This leaves just the Normal/Soft and Fast/Slow switches that control the loudness and decay rate of the effect. Simple though these seem, to emulate all their combinations would stress the resources of any analogue synth. Nonetheless, if we had the resources of a suitably expansive synth to hand, we could set up a patch to produce just one organ note, imitating the percussion by diverting part of the 4' or 2 2/3' signal through a VCA controlled by an AD contour generator.

 Figure 7: Adding a percussive shape to the amplitude contour. I have shown a stylised representation of this (using 88 8000 000 as the basic registration and omitting unused footages) in Figure 6, above. Complex, isn't it?

 Unfortunately, the Juno does not offer the complexity needed to imitate the structure in the diagram. Faced with these limitations, many synth programmers attempt to give the impression of percussion by modulating the audio VCA to create the amplitude blip shown in Figure 5. On the Juno, you would obtain this by flipping the VCA switch from 'Gate' to 'Env', and by adding a little Decay to the ADSR contour. I have shown these changes in Figure 7.

 Figure 8: Using the ADSR to create a blip at the start of the note. Figure 9: The Hammond percussion sound. 

 This creates the audio effect shown in Figure 8, which is far removed from the true percussion effect represented by Figure 9. What's more, the patch in Figure 1 creates key-click by using the ADSR to modulate the VCF cutoff frequency. The extended decay in Figure 7 changes this click into a completely un-Hammond-like soggy squelch. So, if we want to use this idea, we must disconnect the filter from the envelope generator and retune the cutoff frequency so that it again gives us the 5 2/3' drawbar pitch (see Figure 10).
 Figure 10: A usable percussion patch — but it won't fool you. Figure 11: Using one of the Prophet 10's filters to create a far more accurate percussion sound. Of course, our failure to synthesize even a basic percussion effect is not indicative of a limitation of analogue synthesis in general, and things are much more promising if we move away from the Juno, and consider a more complex synth with multiple signal paths.

 You may remember that the Sequential Prophet 10 introduced last month offers two paths that we could use to generate any four drawbar footages of our choosing. For example, we could use the Lower synth to produce the 16' and 2 2/3' pitches, and the Upper synth to produce the 8' and 5 2/3' pitches. This allows us to use the Lower filter to create a percussive 'blip' at the front of notes, controlling the loudness of the 2 2/3' pitch without affecting the amplitude of the other pitches (see Figure 11).

 Figure 12: Creating a percussive 'blip' using the Upper filter envelope. 

 Figures 12 and 13 demonstrate why this works so well; the 5 2/3' and 8' pitches are not passing through the Lower filter, and the 16' pitch is far enough removed from the cutoff frequency to be unaffected by the changes. OK, I'm cheating, because the Prophet 10 cannot produce the sine waves needed to make this picture strictly accurate, but the result nonetheless sounds surprisingly authentic. Neat, huh?

## Hammond Effects — Chorus/Vibrato 

 Figure 13: Hammond percussion recreated on the Prophet 10. Given that there's no way to emulate the Prophet's percussion settings on the Juno, let's now ignore this effect, throw a temper tantrum, and — as suggested at the start of this article — decide that we never wanted it, anyway. Instead, let's move on to the wonderful chorus/vibrato provided on the larger Hammond organs.

 Chorus was not a feature of Laurens Hammond's earliest instruments, but he soon decided that the sound of his tonewheel generator was too pure, and that it needed something to impart life and movement. Some of his earliest production organs used two ranks of tonewheels detuned by a small amount to create what was possibly the world's first example of 'polyphonic oscillator detune', while some of his 'X-series' speaker cabinets had a rotor at the top of the assembly that added amplitude modulation. But Hammond wanted something with more animation, and in 1945 he designed an electromechanical device that created the pitch modulation he wanted. He called it a 'scanner' vibrato.
 Figure 14: Three levels of simple vibrato. This uses a tapped delay line which, if we look closely at the electronics, is a type of phase-shifter constructed from low-pass filters. The signal generated by the tonewheels is applied to the input of the delay line, and a rotating pickup driven by the tonewheel generator picks the signal off the delay line at each of the tap points, one at a time. The scanner is wired so that it moves from one end of the delay line to the other, and back again, during each rotation. As it does so, the pitch shifts up and down... which is, of course, vibrato. Careful analysis shows there is also a small amount of amplitude modulation as the scanner sweeps round the taps, but we should be able to ignore this.

 If you select one of the 'V' settings on the Hammond, all of the audio is routed through the scanner, and the signal suffers unadulterated pitch modulation at one of three depths called V-1, V-2 and V-3 (see Figure 14). If you select a 'C' setting (C-1, C-2 or C-3), the output from the scanner unit is mixed with the unaffected output from the tonewheel generator, and the result is what we call 'chorus' (see Figure 15). This is the key to the best Hammond sounds yet, despite its apparent simplicity, only a couple of Hammond emulators manage to get it right.

 Figure 15: Three levels of chorus. So, what hope do we have of getting the Juno's onboard chorus unit to imitate the C-3 setting favoured by many organists? None, I'm afraid. The Hammond chorus mixes the straight-through signal with just a single instance of the pitch-modulated signal, so the Roland's three-stage chorus/ensemble is far too lush.

 It's little consolation that we can use the Juno's LFO to create vibrato of an appropriate depth and speed... it doesn't sound the same as the Hammond's. If you want to try this, you must select the LFO rate very carefully — I find that 'six and a bit' is correct on my Juno 60 — and set the LFO depth in the DCO to create the correct amount of modulation. But this is only half the story. The 5 2/3' pitch is being generated by the VCF, so you must also raise the LFO depth in the filter section, and try to ensure that identical amounts of modulation are applied to the DCO and the VCF. If you don't, the 16' and 8' pitches will deviate more (or less) than the 5 2/3' pitch, which leads to some very unconvincing effects. I have shown the modified parts of the patch in Figure 16.

 Figure 16: Adding 'Hammondesque' vibrato. 

 To be honest, I think that these changes have turned my original Hammond patch from prime steak into dairy produce. In other words, a patch that was previously meaty now sounds cheesy. It may be theoretically accurate, but that doesn't mean that I have to like it. In fact, I never use any of my A100's 'V' settings, so I'm going to abandon the changes in Figure 16 and return, yet again, to Figure 1.

## Hammond Effects — Leakage 

 Another characteristic of the tonewheel generator (which, like key-click, Laurens Hammond considered to be a fault) is 'leakage', a mixture of drawbar pitches and noise that gives the A100 a characteristic, throaty quality.

 On some synths, adding the tiniest amount of noise helps to create this impression. On the Juno, however, the noise passes through the self-oscillating filter, and emerges tuned to the 5 2/3' pitch. Bah!

 Because its filters are not oscillating (indeed, have zero resonance), adding noise works far better on the Prophet 10. But on consideration, I think that I'll leave well alone. Back to square one (or, to be precise, Figure 1) again!

## Hammond Effects — Overdrive & Compression 

 The next thing we need to consider is overdrive; our ability to cause the valve preamplifier and amplifier(s) in the Hammond to distort. Laurens Hammond was an engineer, not a musician, and reputedly tone-deaf. Yet he had very strong views regarding the tone that he wanted from his organs, and gave explicit instructions to his factory and service centres that the amplifiers were to be adjusted so that there was no overdrive or distortion. Nowadays, we think that Hammond was wrong, and overdrive and distortion have become invaluable in all forms of non-classical music. To be fair to Mr Hammond, it was only in the 1950s that keyboard players and guitarists started to experiment with overdrive seriously, and it took another decade for distortion to emerge as a fundamental building block of modern popular music.
 Figure 17: Adding distortion. Nowadays, many synths feature digital overdrive/distortion effects, but the Juno predates such enhancements. Nonetheless, all is not lost, because with the high internal signal levels generated by the DCO, the sub-oscillator and the self-oscillating filter, it is easy to overdrive the Juno's VCA by raising its Level toward +5 (see Figure 17). The result can be anything from a mild distortion to a full-throated crackle. It's not the same as the warm burr of a 30-year-old valve on the edge of break-up, but produces some very useable results, plus an unexpected side-benefit. A Hammond exhibits mild compression when you add notes to a chord and, coincidentally, an overdriven VCA exhibits exactly the same quality when you exceed the limit of its abilities to amplify and drive it into clipping distortion.

 Unfortunately, you can't employ this trick on many synths, because the majority are factory-calibrated to stop you from clipping the signal. This is understandable; for most sounds, the results would be inappropriate and unpleasant. Still, it would be nice if the option existed, as on the Juno.

## Hammond Effects — Reverb 

 In some low-cost Hammonds, the next element in the signal path is a spring reverb unit. You would think that it would be a doddle to imitate this... why not just plug a suitable spring reverb or digital imitation between the Juno and the amplifier/speaker system, as shown in Figure 18?

 Figure 18: The conventional use of a reverb unit. 

 However, this is not quite right, because the overdrive generated by the overdriven VCA occurs before the reverb unit, and this is the opposite of what happens in the Hammond. Nonetheless, many modern reverb units offer suitable effects, provided that you disable all the extra stuff that they tend to offer.
 Figure 19: A simplified schematic of the Hammond A100. 

 Things become more complex when you consider the A100, which has a separate amplifier and speaker to handle the output from the reverb unit (see Figure 19). However, this is easily recreated, because many digital reverb units allow you to send a treated signal to one channel while directing the original to another. This means that I can draw Figure 20, with a modified Juno patch providing optional vibrato and overdrive, played through two channels; one clean, the other reverberated.
 Figure 20: The affected Juno 60 'Hammond' patch. 

 So... how does it all sound? The truth is, not great. I don't like the vibrato effect, we've been unable to synthesize percussion or chorus, and while the distortion effect is quite pleasing, sticking a digital reverb after a patch doesn't count as 'real' synthesis. Sure, we've learned a great deal simply by attempting to recreate the Hammond effects, but it would have been nice to achieve something more satisfying. Fortunately, this isn't the end of the story, because I've left the most important — and by far the best — organ effect out of this discussion. I'm referring, of course, to that generated by the rotary speaker or 'Leslie' attached to almost all A-, B- and C-series Hammonds. So, next month , we're going to wrap up our synthesis of the Hammond organ by getting ourselves into a bit of a spin.

 Previous article Next article 

## In this Series 

 What's In A Sound? 

 The Physics Of Percussion 

 Modifiers & Controllers 

 Of Filters & Phase Relationships 

 Further With Filters 

 Of Responses & Resonance 

 Envelopes, Gates & Triggers 

 More About Envelopes 

 An Introduction To VCAs 

 Modulation 

 Amplitude Modulation 

 An Introduction To Frequency Modulation 

 More On Frequency Modulation 

 An Introduction To Additive Synthesis 

 An Introduction To ESPs & Vocoders 

 From Sample & Hold To Sample-rate Converters (1) 

 From Sample & Hold To Sample-rate Converters (2) 

 Priorities & Triggers 

 Duophony 

 Introducing Polyphony 

 From Polyphony To Digital Synths 

 From Springs, Plates & Buckets To Physical Modelling 

 Formant Synthesis 

 Synthesizing Wind Instruments 

 Synthesizing Brass Instruments 

 Brass Synthesis On A Minimoog 

 Roland SH101 & ARP Axxe Brass Synthesis 

 Synthesizing Plucked Strings 

 The Theoretical Acoustic Guitar Patch 

 A Final Attempt To Synthesize Guitars 

 Synthesizing Percussion 

 Practical Percussion Synthesis: Timpani 

 Synthesizing Drums: The Bass Drum 

 Practical Bass Drum Synthesis 

 Synthesizing Drums: The Snare Drum 

 Practical Snare Drum Synthesis 

 Analysing Metallic Percussion 

 Synthesizing Realistic Cymbals 

 Practical Cymbal Synthesis 

 Synthesizing Bells 

 Synthesizing Cowbells & Claves 

 Synthesizing Pianos 

 Synthesizing Acoustic Pianos On The Roland JX10 [Part 1] 

 Synthesizing Acoustic Pianos On The Roland JX10 [Part 2] 

 Synthesizing Acoustic Pianos On The Roland JX10 [Part 3] 

 Synthesizing Strings: String Machines 

 Synthesizing Strings: PWM & String Sounds 

 Synthesizing Bowed Strings: The Violin Family 

 Practical Bowed-string Synthesis 

 Practical Bowed-string Synthesis (continued) 

 Articulation & Bowed-string Synthesis 

 Synthesizing Pan Pipes 

 Synthesizing Simple Flutes 

 Practical Flute Synthesis 

 Synthesizing Tonewheel Organs: Part 1 

 Synthesizing Tonewheel Organs: Part 2 

 Synthesizing Hammond Organ Effects

 Synthesizing The Rest Of The Hammond Organ: Part 1 

 Synthesizing The Rest Of The Hammond Organ: Part 2 

 From Analogue To Digital Effects 

 Creative Synthesis With Delays 

 More Creative Synthesis With Delays 

 The Secret Of The Big Red Button 

## SOS Competitions 

## On the same subject 

 The Secret Of The Big Red Button July 2004 

 More Creative Synthesis With Delays June 2004 

 Creative Synthesis With Delays May 2004 

 From Analogue To Digital Effects April 2004 

 Synthesizing The Rest Of The Hammond Organ: Part 2 March 2004 

## From the same manufacturer 

 Hammond SK Pro 73 October 2022 

 Hammond SKX Pro August 2022 

 Hammond SKX May 2019 

 Hammond XK-5 January 2018 

 Hammond XK3 / XLK3 & Leslie 2121/2101 July 2005 

 Sign Up TO

 SOS Newsletters 

## Latest SOS Videos 

 What Is Wavetable Synthesis | Podcast 

 Designing The Focusrite ISA C8X Audio Interface 

 Trinnov NOVA User Report - PresentDayProduction 

## New forum posts 

 Re: Mac Mini and External SSD/Hubs 

 Luke W > 
 24 Sep 2026, 09:40 Mac Music 

 Re: AI Tools 

 The Elf > 
 24 Sep 2026, 09:36 Music Theory | Songwriting | Composition 

 Re: Fender, the Strat body and application of copyright 

 arkieboy > 
 24 Sep 2026, 09:30 Guitar Technology 

 Re: AI Tools 

 RichardT > 
 24 Sep 2026, 09:12 Music Theory | Songwriting | Composition 

 Re: Fender, the Strat body and application of copyright 

 ajay_m > 
 24 Sep 2026, 09:12 Guitar Technology 

## Active topics 

 SM58 - Dodgy XLR connection. 

 Mac Mini and External SSD/Hubs 

 Be Quiet! 135mm fans that do not exist, eh ? 

 Yamaha DM3 Phantom Power Risk 

 Where is my October magazine pls?!? 

 iPad mic stand clamps, again. 

 Neutrik and the Crappy Snake 

 Cubase issue: Import/Convert Rack Instrument as Track Instrument (or easy workaround) 

 FSP Mixdown - No Sound Exported to Computer 

 Plugin Availability for Older Macs 

## Recently active forums 

 Recording: Gear+Techniques 

 Mixing | Mastering | Post Production 

 Keyboards+Synthesizers 

 Guitar Technology 

 NEW PRODUCTS [Paid Posts Only] 

 Windows Music 

 Mac Music 

 Apps | Other Computers/OS 

 Live Sound | Performance 

 DIY | Electronics | Studio Design 

 Music Business 

 Music Theory | Songwriting | Composition 

 User Reviews 

 Remote Collaboration 

 Self-Promotion 

 Feedback 

 SOS Support Forum 

## Login 

 You may login with either your assigned username or your e-mail address.

 The password field is case sensitive.

 Request new password 
 Create an account