---
titre: "adammonroemusic.com — simulating a leslie speaker"
source: https://adammonroemusic.com/blog/simulating_a_leslie_speaker.html
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: claviers électromécaniques
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Adam Monroe Music - Simulating a Leslie Speaker 

 VIRTUAL INSTRUMENTS 

 Adam Monroe's Honky Tonk Piano 

 Adam Monroe's Beats Drum Sample Library 

 Adam Monroe's Upright Bass 
 
 Adam Monroe's Theremin 

 Adam Monroe's Austrian Grand Piano 

 Adam Monroe's Slap Bass 
 
 Adam Monroe's Upright Piano 

 Adam Monroe's Electric Bass 

 Adam Monroe's Mark 73 Electric Piano 

 Adam Monroe's Tremolo 

 Adam Monroe's Wurlitzer 

 Adam Monroe's Rotary Organ 

 Adam Monroe's Delay 

 MUSIC 
 
 Pond5 
 
 Youtube 

 Soundcloud 

 AudioJungle 

 SHEETS 
 
 Theme From the Munsters 

 Songs My Mother Taught Me (Antonin Dvorak) 

 Adam Monroe - The Hopeless Romantic 

 Adam Monroe - Birth of a Planet in Four Parts 

 Adam Monroe - Smooth Jazz Piano 

 Adam Monroe - The Last Waltz of a Dying Man 

 Adam Monroe - Poor Billy 

 Adam Monroe - This Fleeting Feeling 

 Adam Monroe - The Lover's Lament 

 Adam Monroe - Walking in the Park 

 Adam Monroe - Old Glory 

 Adam Monroe - Moonrise Waltz 

 Adam Monroe - Morning in a Town 

 Adam Monroe - Flying Through the Clouds 

 Adam Monroe - Like Love in the Movies 

 Adam Monroe - Horns of War 

 Adam Monroe - Triumph and Glory 

 CONTACT 

 adammonroe@adammonroemusic.com 

 Twitter 

 Facebook 

 BLOG 
 
 Music Theory Lesson 1: Sound and Tuning Systems 
 
 Music Theory Lesson 2: Scales, Key Signatures, and Chords 

 Simulating a Leslie Speaker? 

 The Best B3 Organ Plugins in 2022 

 The Best Rhodes Plugins in 2022 

 The Best Wurlitzer Plugins in 2022 

 Porting VST2 Plugins to VST3 

Simulating the Leslie Speaker 

 Origins of the Leslie Speaker

 12/17/2015

 For my Hammond B3 Organ plugin, Adam Monroe's Rotary Organ , it was necessary to simulate the famous Leslie Speaker . The Leslie Speaker has become synonymous with the sound of a Hammond B3 Organ , but interestingly, neither Hammond nor Leslie seemed to be particularly fond of one another. Laurens Hammond was heard to say, "I never intended for my organs to sound that way," and Donald Leslie, in reference to Hammond, is purported to have said, "I hate those damn things!" But the two did not outright hate each other, as their business relationship was symbiotic - not unlike the relationship between plugin developers and larger companies like Apple today ;) Simply put, Hammond refused to license or market the Leslie Speaker with his organs and thus Don Leslie was forced into forming an independent company. This is a common story that tends to repeat itself throughout the business world. One example that comes to mind is Nintendo passing on licensing John Carmack's 2D engine and opting to not bring Super Mario to the PC, but i digress... The Leslie Speaker was Donald Leslie's attempt to further enhance the sound of a tonewheel organ to make it more spatial, as the pipes of a church organ occupy a wide physical space. Whether or not he accomplished this is debatable, but he did managed to create one of the most iconic and recognizable organ sounds, and one of the more unique sound modulations, period. 

 Leslie - More Than Just a Speaker

 The Leslie Speaker is much more than just a speaker, it is a cabinet that houses two speakers, two rotating horns powered by motors, and a tube amplifier! An ideal Leslie Speaker simulation will take all of these different components into consideration and approximate them using Digital Signal Processing or DSP . At the heart of every Leslie Speaker lies the rotating drum and the rotating horn. The speakers that produce the sound are mounted perpendicular to the horns, and the horns disperse the sound in a 360 degree motion. This produces several effects that need to be properly simulated. The first and perhaps easiest to simulate is a tremolo effect: the amplitude of the waveform will vary with the directionality of the speaker. This can easily be simulated using an LFO , or Low Frequency Oscillator. LFOs usually sound best when sine waves are used, as sine waves tend to approximate three dimensional oscillation due to their curves. How to implement this is entirely up to the developer and some things should be considered. Both the upper and bottom rotors only allow sound in one direction (one-half of the dual horn of the upper rotor is just a counter-balance and emits no sound). So, how "clean" should the LFO sine wave be? Should it be symmetrical? Should it vary? Should it be a pure sine wave or something more dirty? These are questions worth considering.
 Before we get too ahead of ourselves, let us recognize that we are trying to simulate the effects of TWO horns and TWO speakers . The lower horn (or drum) handles the bass frequencies, well the upper horn handles treble. There is an 800Hz passive crossover that uses inductance and capacitance to filter the signal into two separate output frequency bands . In terms of DSP , this means that we will need a Low-Pass filter and a High-Pass filter centered around 800 HZ in order to digitally split the original signal into the proper bands. However, the crossover point in older Leslie speakers may show frequency drift do to aging components, so it's worth experimenting with this frequency in order to determine what sounds best, but 800 Hz is a good starting point.
 Before we even split our signal, we should examine the Leslie Amplifier . Part of the reason why Leslie Speakers sound good is the built-in amplifier, and the non-linearity of vacuum tubes . I believe this is an often overlooked component of simulating a Leslie Speaker . Tube distortion is an article unto itself, but we can simulate simple non-linear distortion by using an inverse tangent function like arctan . However, as computer processing has gotten more powerful, accurate distortion simulation has begun to move towards things like SPICE Vacuum Tube simulations, which are phenomenological equations that mimic the characteristics of specific vacuum tubes. If you can program these equations into a C++ DSP class , you will have a fairly accurate means of simulating certain amplifiers! Simulating amplifiers is also an article unto itself, but lets at least look at a Leslie 122 schematic to get an idea of what's involved. We see a 12AU7 dual-triode vacuum preamp tube, and two 6550 tetrode output tubes. To get closer to the sound of a true Leslie Speaker , we should aim to replicate the the non-linear characteristics of these tubes. However, distortion is not an exact science and in my plugin I have included a Leslie Amplifier simulation as well as many other tube-sims - we don't need to be accurate so much as we need to trust our ears to determine what sounds best! For our purposes, we will completely ignore the distortion caused by things like the output transformers :)
 Now that we have our signal properly amplified and split into two, we can return to simulating the mechanical aspects of our Leslie . Tremolo is a good start, but in order fully simulate the sound of a rotating speaker, we will need to address the Doppler Effect . The Doppler Effect is the change in perceived frequency as a sound source moves away or towards you, and a rotating speaker certainly fits that description! We perceive sound as shifting up in frequency as it moves towards us and down as it moves away (the frequency actually doesn't change, the sound waves just become more compressed and stretched due to motion). We can simulate the doppler effect through DSP using a vibrato algorithm . Typically, this is implemented as a variable delay line . With DSP , we will need to interpolate some of our sample data, as the current datapoint will typically fall somewhere in between two sample points. I recommend cubic interpolation as it sounds the best and doesn't create too many artifacts. Cosine interpolation is more efficient, but computers are getting fast enough to handle all these real-time DSP algorithms (the real bottleneck with digital sound is increasingly hard drives, but that is yet another article). Our vibrato speed should be closely tied to our tremolo speed , as they are both due to the same effect, the rotating speaker . 
 One important aspect of the Leslie Speaker is the speed of the rotors and how quickly the wind-up and spin-down. Again, we are faced with a mechanical device where the speed of the rotors tend to vary slightly from speaker-to-speaker and model-to-model. For my organ, I've chosen 40/49 RPM for the "chorale" speed and 397/409 RPM for the "tremolo" speed of the lower and upper rotors. I arrived at my numbers through careful listening, tweaking, and readjusting of the speeds, and I would suggest the same process for any attempted simulation, as your ears will tell you what is right. Typically, something between the 40-50 RPM range for the slow speeds and 390-415 RPM for the fast speeds seem to work well. One often overlooked aspect of the rotors is how much longer the bottom rotor takes to accelerate and decelerate . The top rotor can spin-up and slow-down in 1-3 seconds well the bottom rotor can take anywhere from 5-9 seconds (the bottom rotor has more mass and therefore more inertia to overcome). Again, learning to trust your ears comes into play: if you measured many different Leslie Speakers they would all likely have different speeds and ramp-up times, so there really isn't a universal standard.
 Once we have our distortion , tremolo , vibrato , and rotor speeds we can move onto smaller details. We can consider things like panning . When recording a Leslie speaker , stereo microphones are typically used to get a wide stereo image (but we can also record either rotor in mono). In a plugin, we should give the end-user the option of adjusting this stereo width, as well as controlling the volume of each rotor (in order to simulate mic distancing). Returning to the rotors, we should also adjust the directionality of the speakers. As the rotors start to point away from us, the higher-frequencies will naturally be attenuated more than the lower-frequencies. Therefore, we will want to add a variable Lowpass Filter to simulate this effect, at least on the upper horn.
 We should also consider the effect of the cabinet itself. The speakers aren't housed in the open air, they are housed inside of a cabinet, with slots for the sound to escape. This means that a lot of sound will bounce around and reflect inside of the cabinet before escaping. There may be subtle alterations to the frequency do to sound being absorbed or amplified by the wood. In short, there will be a million little nuances inherent to the cabinet that would be difficult to calculate and implement. What are we then to do? My solution was a smoothing algorithm and a mellowing algorithm , and built-in reverb . These all work in conjunction to soften up the overall sound and shape it so that it sounds more like it is emanating from a speaker cabinet. Reverb especially will go a long way towards softening the sound. Again, reverb is another topic, but developing a good reverb algorithm will help make a unique and good sounding Leslie Speaker simulation. If you had access to a real Leslie Speaker and an anechoic chamber, you could of course measure a few control tones with and without the cabinet to see what affect it had and work backwards from there ;) I also spent a lot of time developing EQ curves that can be selected by the user. Again, some of this isn't an exact science, and we must learn to trust our ears in order to determine what sounds best!
 But what about the Organ itself? You essentially have two options; sample an organ or generate tonewheel sine waves . Obviously, I'm a fan of sampling over modeling, but modeling does have it's merits. I sampled my organ from a Hammond M3 - the Green Onions organ - and adjusted the playing range to be the same as that of a B3 Organ . I believe there's something about the dirt and grime in an old mechanical tonewheel that would be hard to model properly, and if you listen closely, you can hear a bit of a pulsating effect on some of the notes. I believe this also adds the the plugin sounding less "digital." Whenever you can, it's a good idea to throw some randomness and disorder into your digital simulations.
 For more about organ plugins and software plugins in general, check out Chris Senner's Blog KeyboardKraze !