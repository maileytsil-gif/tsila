---
titre: "soundonsound.com — synthesizing rest hammond organ part 2"
source: https://www.soundonsound.com/techniques/synthesizing-rest-hammond-organ-part-2
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: claviers électromécaniques
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Synthesizing The Rest Of The Hammond Organ: Part 2 

 Skip to main content 

 Set us as a Google preferred source preferred 

 facebook 
 twitter 
 email 
 print 

## You are here
 Home 
 Techniques 

# Synthesizing The Rest Of The Hammond Organ: Part 2

 Synth Secrets 

 Synthesizers > Synth Secrets , Synthesis / Sound Design 
 By Gordon Reid 
 
 Published March 2004 

 We conclude our analysis of the fabulously complex beast that is the Leslie rotary speaker.

 Photo: Richard Ecclestone Last month , we analysed the nature of the 'Leslie' rotating speaker system, and I showed how any signal played through such a device is subjected to frequency modulation, amplitude modulation, tone modulation, and reverberation. I also showed how — in principle — we could use an LFO connected to the pitch modulation input of an oscillator, plus various filters, amplifiers and delay lines, to emulate this effect. But the weak link was the oscillator and LFO. It's all very well modulating the pitch of a signal produced electronically in this fashion, but this method gives us no clue as to how we could modulate any signal, such as that produced by an organ, a guitar, or a human voice. If we fail to find a way to do this, we cannot properly synthesize the rotary speaker. On the other hand, since such effects exist, and existed long before the development of modern digital units, it can't be that hard... can it? After all, many players used analogue rotary speaker effects in the 1970s, even though they weren't particularly convincing.

 Of course, these days, there are plenty of available digital rotary speaker simulators, but as with previous instalments of this series, I'm going to describe the process using analogue principles, as it's easier that way to relate the constituent parts to conventional synthesizer components, and understand how everything works.

 Let's start by returning to what this series was examining way back in SOS August 2000 . That month, I showed how the concepts behind Sample and Hold (or S&H) synth modules are related to those behind analogue-to-digital converters, and thus to all of digital audio. Today, I find myself at the same starting point, and, although it may not be obvious how discussions of S&H circuits and Leslie speakers should be so closely linked, I'll ask that you bear with me because — as always — all should soon become clear.

## A Quick Recap 

 To understand S&H and how it leads to the technology of modulated effects, I'm going to review some of the ground that we covered back in 2000, starting with Figure 1 (below), which I've copied from the previous article. As you can see, this is a remarkably simple circuit, comprising just two components: a capacitor and a switch.
 Figure 1: The simplest representation of a S&H circuit. There's nothing stopping us from presenting an audio signal, an LFO, an envelope, or anything else to the input in Figure 1, as I did back in 2000. However, this month, I'm going to concentrate on presenting audio signals, starting with a simple sine wave.

 Imagine that, just for an instant, the switch in the diagram closes. If the capacitor can react quickly enough, it then charges up (or discharges down) to the voltage at the input, thus 'sampling' that voltage. Then, once the switch has opened again, the voltage across the capacitor cannot change. This is because, on the left-hand side, there is no circuit and, on the right-hand side, the impedance — which is represented by the mathematical symbol 'z' — is infinite (which means that no current can flow). However, although no current flows, you can still measure the voltage across the output.

 That's all there is to it... when the switch is closed, the capacitor 'samples' the input voltage. When the switch is open, the capacitor 'holds' that voltage, allowing other circuits to respond to it as appropriate.

 Figure 2: The output from a Clock Generator. Now, if you were limited to closing the switch in Figure 1 manually, this S&H circuit would not be of much use. So synthesizers have electronic switches that respond to another module that is capable of opening and closing it at high speeds. This 'other module' is a Clock Generator, which provides a stream of pulses that trigger the switch in Figure 1 (see Figure 2). In other words, when the pulse is on, the S&H circuit samples, and when the pulse is off, the S&H holds.

 Figure 3: A simple example of S&H. Given these two modules, we can devise a simple circuit that incorporates the clock and the S&H circuit, as shown in Figure 3. In this case, this shows something akin to a sine wave presented to the signal input of the S&H module. At the same time, the clock provides a stream of pulses that it presents to the S&H's trigger input. The output produced by the S&H circuit is then the 'blocky' waveform shown.

 Figure 4 (below) explains the nature of the output. Each time the S&H module receives a trigger, it measures (or 'samples') the voltage of the input signal (shown in red). It then holds this voltage (the blue line) until it receives the next trigger, at which point it repeats the operation. It 'samples' and then 'holds', just as I've described. Figure 4: Explaining S&H. 

 As I suggested last time, this result would not be very interesting if a sine wave was the only signal you could present to the module's input. Fortunately, the input signal can be anything: a synthesized audio waveform, an external signal such as the output from a turntable or CD player, or even the 'live' sound of an instrument being played. And this is where we begin to diverge from my previous discussion. Whereas traditional synth S&H effects are derived mostly from using a random 'noise' signal as the input, and directing the output to the control inputs of other synthesizer modules, we are now going to concentrate on affecting the actual sound of an instrument being played. But before we do so, we have to convert the S&H circuit into a delay line...

## The Bucket Brigade Device 

 Figure 5: Two S&H circuits in series. Let's place two S&H circuits in series, as shown in Figure 5. The white triangles are 'buffer amplifiers'. They provide the infinite impedances mentioned above, but do not affect the signal in any other way. Consider what happens when Switch 1 and Switch 2 are open, and then Switch 1 closes for a moment, before opening again. When Switch 1 closes, a single sample is taken and held by the first S&H circuit.

 Now imagine that this sequence of events repeats, but that this time it is Switch 2 which closes for a moment, and then re-opens. When Switch 2 closes, the second S&H circuit takes the sample held in the first as its input, samples it, and holds it. In other words, the sample is passed down the line!
 Figure 6: An eight-stage delay line. It takes little imagination to realise that we can extend this idea, adding as many elements to this circuit as we like. Take Figure 6 as an example. This has eight S&H stages. If we open and close all the red switches simultaneously, and all the green switches simultaneously, closing the green when the red are open and vice versa, we can take a continuous stream of audio samples at the input and pass them down the line to the output. If the clock rate is, for the sake of argument, 44,100 pulses per second (the standard CD sampling rate), the length of the delay line is 8/44,100 seconds, which is somewhat less than 0.2 milliseconds... far too short to be of use. But if we extend this to 2048 stages, the length of the line is more than 46ms, which is long enough to create a range of common audio effects. What we have here is a sampler — one that is entirely analogue, too.

 Before moving on, we need to eliminate two problems encountered when sampling and reconstructing a continuous waveform. Just as when sampling digitally, all that stuff about keeping the maximum frequency at less than the sampling rate holds true here, too (for more on this, look back at Part 17 of this series, in SOS September 2000 ).

 Because of this, we need to ensure that the highest frequency presented to the delay line is less than half the sampling frequency. In this case, the sampling frequency is half of the clock frequency, because, as illustrated in Figure 5 earlier, a new sample is taken every two trigger pulses. Anyway, to ensure that the input is suitably band-limited, we need to add a low-pass filter before the signal input. Secondly, we want to eliminate the 'blockiness' from the output waveform shown in Figure 3, and we do so by smoothing the output using a second low-pass filter.

 Putting all of this together, we now have a circuit description for an analogue 'bucket-brigade device' (or BBD) delay line, so-called because its operation is analogous to handing buckets of water, each filled to a different depth, along a line of people (see Figure 7).

 Figure 7: Adding an anti-alias filter and a reconstruction filter to the delay line. 

 By the way, the low-pass filters I have drawn — simple 1-pole devices — are much less powerful than one would normally use for these purposes, so please treat them as representative rather than an exact circuit description. The first of these is called an 'anti-aliasing filter' because it removes high frequencies that lead to aliasing. The second is known as a 'reconstruction filter' because it reconstructs the smooth waveform from the 'blocky' one at the output.

## Clock Modulation & Waveshaping 

 Figure 8: Sampling, delaying and reconstructing the waveform. To properly emulate a Leslie, you need not only to delay the signal passing through it, but also to modulate its frequency. To do this, let's return to the clock that's opening and closing the switches within the delay line. If the speed at which the clock is running remains constant, the signal will be sampled steadily, with each sample passed down the line at a constant speed and then read out with the temporal gaps between the output samples equal to the gaps at the input. If the reconstruction filter does its job correctly, the output waveform should then be identical to the input waveform (see Figure 8).

 But what happens if we modulate the clock so that adjacent samples measured at one rate are presented to the reconstruction filter at a different rate? For the purpose of this discussion, you can think of the delay line as a tape recorder, with a record head at one end and a playback head at the other, and an infinitely long strip of tape running past them. If the speed of the tape is, say, 15ips when a middle 'C' (C3) is recorded at the start, but just 7.5ips when that part of the tape passes the playback head, the note will be replayed as C2, an octave lower. Conversely, if the tape speeds up to 30ips, the note will be raised an octave, and reappear as C4.
 Figure 9: Presenting an audio sine wave to the delay line's input. Of course, we certainly don't have to restrict ourselves only to increasing or decreasing the speed of the tape. If we could modulate the tape speed in some fashion, we could generate pitch modulation, or 'vibrato'. Now, let's return to the delay line, and modulate the clock, so that the relationships between samples are changed slightly...

 Figure 9 shows approximately 24 cycles of a sine wave that, for the sake of argument, I have presented to the input of our delay line. I shall now modulate the clock frequency to obtain Figure 10, which shows that I have increased the wavelength of some cycles, thus lowering the frequency, and decreased the wavelength of others, thus raising the frequency. It should be obvious from this somewhat exaggerated example that this is an extreme example of pitch modulation.

 Figure 10: Modulating the output clock to generate pitch modulation. The great thing about this method of generating vibrato is that, unlike presenting a pitch CV to the modulation input of an oscillator, it allows us to modulate any input signal. It's also interesting to note that, if we increase the speed of the clock modulation, the output waveform will be altered in a more radical fashion. For example, Figure 11 shows how the samples in Figure 8 can be re-timed (without affecting their amplitudes in any way) to turn a sine wave at the input into a triangle wave at the output.

 What I have described here is, of course, the basis of the frequency-modulation synthesis (or FM) used in Yamaha's DX series of synthesizers, and it is very similar to the 'Phase Distortion' (or PD) synthesis used in the Casio CZ series of keyboards. But instead of modulating an oscillator, as we did when investigating FM synthesis earlier in this series (see SOS April 2000 and SOS May 2000 ), we are now frequency-modulating any sound.

 Figure 11: Waveshaping by modifying the clock frequency. 

 It's possible to build a mathematical model of the 'clock distortion' FM synthesis implied by Figures 9, 10 and 11 using a sine-wave oscillator to modulate the frequency of the clock (see Figure 12). There's nothing special about sine-wave modulation in this context — I could use any waveform — it's just that it's simple to implement a sine wave in a model of this nature. Using this, you can generate vibrato when the modulation oscillator is running in the LFO range, and many recognisable 'DX' and 'CZ' waveforms when it runs at audio frequencies.
 Figure 12: Modulating the clock. Figure 13: Modulating the output clock to shape a sine wave into a triangle wave. For example, Figure 13 shows the superb precision obtainable when using the modulator to 'waveshape' a sine wave into a triangle wave. Meanwhile, Figure 14 reveals that we can obtain a more complex-looking and harmonically interesting wave by modulating the clock at a different frequency. What happens when you use a delay line to 'FM' a complex signal such as your guitar playing or singing is, of course, another thing!

## Synthesizing The Leslie 

 Audio-frequency FM and PD synthesis are fascinating topics, but they are not the purpose of this month's Synth Secrets, so we have to leave them behind, return to the Leslie, and now ask what its modulation depth and frequency might be. Surprisingly, the modulation depth created by the doppler effect in a Leslie speaker is quite small — around ±1 percent, which would be no problem for the mechanism in Figure 12 (see earlier).

 Figure 14: Obtaining a more complex wave by altering the LFO frequency in Figure 12. More problematic is the slowest rate at which the modulation occurs. For a Leslie rotor, this can be slower than 1Hz. This means that the modulation depth drops to a fraction of a percent, but the slow modulation frequency means that the delay line has to increase the audio frequency for half a second or more, and then reduce its frequency for half a second or more. This introduces some technical difficulties, often resulting in reduced signal integrity. Nevertheless, the principles of our analysis are correct, so I can draw a mechanism for imitating the doppler effect for any audio signal, as shown in Figure 15. As you can see, the audio is passed through the delay line and its associated filters, with the clock modulated at a low frequency, as discussed. The result is a signal that undergoes pitch modulation, no matter what the nature of the input.

 Figure 15: Simple pitch modulation of any audio signal. The depth and speed of the pitch modulation in Figure 15 are controlled solely by the LFO, and we can affect this by applying control voltages to that module's CV inputs. This leads to a number of interesting effects, one of which is the ability to use two CVs to imitate the Leslie's two rotation speeds, the 'tremolo' and 'chorale' mentioned last month. What's more, we can even control the rate of transition between these speeds by adding a slew generator that smoothes the transitions between the 'fast' and 'slow' CVs, thus emulating the acceleration and deceleration you hear when changing the speed of the physical rotors in the Leslie itself (see Figure 16).

 Figure 16: Providing two modulation speeds. 

 To make this model accurate, we must split the audio signal into two bands — a treble band above 800Hz and a bass band below 800Hz — just as in a real, dual-rotor Leslie speaker. The easiest way to do this is to split the audio into two signal paths and apply appropriate band-splitting EQs to each. We can then duplicate the modules in Figure 16, defining independent 'rotation' speeds and transition speeds within each path, as shown in Figure 17 (which, for pertinence, I have drawn with a keyboard rather than a microphone as the signal source).
 Figure 17: Modulating the upper and lower frequencies independently. 

 Now all we need to do is add the amplitude and tonal modulations discussed last month (see Figure 18) with each 90 degrees out of phase with respect to the LFO 'rotation' rate. I have added small delay lines in each of the control signal paths to generate this delay, but it is far from a complete description because, as the rotation rate changes, the lengths of these delays also need to change. This can be achieved by adjusting the clocks driving the secondary delay lines, but I suspect that you'll forgive me if I don't plumb the details of this.
 Figure 18: Attempting to create a dual-channel Leslie effect using delay lines. 

 Anyway, with all the delay lines, filters, amplifiers, LFOs, EQs, CVs and Slew Generators in place, we now have the glorious, analogue... argghh!! Figure 18 shows just one direct signal path for each rotor, without any of the reflections that occur within or outside the Leslie cabinet. To re-use last month's analogy, we have two roundabouts but no office blocks. Fortunately, a BBD is an appropriate device for creating simple reverberant effects so, in theory, the addition of another couple of delay lines (the fifth and sixth) might help to overcome this. But given the difficulties in getting this far, and the complexities I've just sidestepped regarding the phase relationships of the various modulations, I imagine that it's becoming clear why no analogue emulation of the rotary speaker cabinet was ever fully successful. To be fair, there was one — the Dynacord CLS222 — that was pretty damn good, and the effect on the Korg BX3 organ was useable if you were prepared to open the instrument up and tweak the internal trimmers.

## The Digital Leslie 

 For most people, the dream of a light, portable, inexpensive and authentic-sounding Leslie effect became a reality only with the advent of digital electronics, and the development of algorithms capable of modelling all the above factors successfully. These algorithms can calculate thousands of signal paths, each exhibiting different pitch shifts, different phases and different amplitudes. Sure, it takes a lot of processing power to implement them but, nowadays, that's not a problem.

 Of these, my favourite remains the Korg ToneWorks G4, a combined 'valve overdrive and rotary speaker' emulator. If you hook one of these up to a Juno 60 or the Kawai K3 I discussed a few months ago, the results are magic. The G4's overdrive is more realistic than the distortion imparted by the Juno's VCA, the rotary effect is remarkably authentic, and its speaker simulation gives it, in my opinion, just the right amount of dull woodiness. Connecting everything together, we obtain Figure 19.
 Figure 19: Using a digital Leslie emulator. 

 Of course, the algorithm in the Korg G4 is synthesizable using analogue electronics, and with a wall of filters, clocks, modulation oscillators, delay lines and amplifiers, you could create a convincing electronic recreation of the rotary speaker effect. You would be mad to try, but you could do it.

## Epilogue 

 We have achieved a huge amount this month, learning how closely linked the seemingly disparate technologies of S&H, delay lines, phase-distortion synthesis, and digital converters prove to be. Moreover, armed with our new understanding of BBD delay lines, we could continue to develop our analogue 'Leslie' effect. Alternatively, we could extend some of this month's ideas to create all manner of effects, such as echo, flanging, chorus and ensemble. And that's what we're going to look at next month .

 Find ALL Synth Secrets Parts 

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

 Synthesizing The Rest Of The Hammond Organ: Part 1 February 2004 

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