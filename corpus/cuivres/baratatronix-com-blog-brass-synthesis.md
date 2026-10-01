---
titre: "Baratatronix — Brass synthesis"
source: https://www.baratatronix.com/blog/brass-synthesis
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: acoustique des cuivres et synthèse classique
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Brass Synthesis — Baratatronix 

 0 

# Brass Synthesis

 Synthesis Techniques Brass 

 Dec 17 
 
 Written By Peter Barata 

 View fullsize 

 A truly authentic brass sound is probably impossible with a subtractive synth. But you can get something with the right flavour. Experimentation and fine-tuning are key—adjust parameters to suit the specific sound you’re after.

### Brief Summary 
 Build a brass patch by combining a selection of the following techniques:
 Use a sawtooth waveform. 

 Only use one waveform. 

 Use a sub-oscillator for a trombone or a tuba. 

 Simulate a note’s initial raspiness with: 
 A burst envelope modulating either pitch, or filter cutoff. 

 A fast LFO shaped by an envelope, modulating either pitch, or filter cutoff. 

 Bring Vibrato in only on sustained notes. 
 Combine a fast and slow LFO. 

 Modulate LFO rate with an envelope, then use the envelope to modulate either pitch, or filter cutoff. This will simulate bot, the initial raspiness and the vibrato. 

 Amp envelope attack = fast but not instantaneous. 

 Amp envelope sustain = moderately high. 

 Amp envelope release = moderately fast. 

 Use amp envelop velocity. 

 Filter envelope attack = slower than amp envelope attack. 

 Filter envelope sustain = high. 

 Use filter envelope velocity. 

 Modulate filter attack time with velocity. 

 Use a low pass filter, either 24db or 12db. 

 Use allow initial filter cutoff. 

 Use low resonance. 

 Raise resonance subtly with either pitch or velocity. 

 Set keyboard track somewhere between 50% to 75%. 

 Make keyboard tracking velocity sensitive. 

 When making an 80’s style synth brass patch, follow the above, but also: 
 Use multiple sawtooth envelopes 

 Ensure the envelopes are detuned just enough to create a chorusing effect. 

 Use a fast envelope to create a blast of detuning on one of the oscillators. 

### 1 How do brass instruments work? 
 1-1 The basics: 
 Brass instruments produce sound when the player buzzes their lips into the mouthpiece. This buzzing creates vibrations that travel through the instrument’s tubing. To make different pitches, players change the tightness of their lips. Faster vibrations make higher pitches, while slower vibrations make lower pitches.
 Additionally, the length of the tube determines the fundamental frequency (pitch) of the note. To play higher notes, the musician can use valves or slides to shorten the effective length of the tube. Higher-pitched notes require shorter tubes, while lower-pitched notes require longer tubes. This is due to the relationship between tube length and wavelength. Longer tubes produce lower pitched notes because they support longer wavelengths. Shorter tubes produce higher pitches because they only support shorter wavelengths.

 1-2 Standing Waves: 
 The vibration of the player’s lips against the mouthpiece creates standing waves within the instrument’s air column. This vibration excites the air column, generating a rich spectrum of harmonics due to the instrument’s shape and the way sound waves reflect inside it.
 A standing wave is a wave pattern that appears to be remaining in one place, rather than moving. This occurs when two waves of the same frequency and amplitude travel in opposite directions and interfere with each other, creating the illusion of a stationary wave.
 Standing waves form when the outgoing sound waves reflect back off the ends of the instrument and interfere with the incoming waves. At certain frequencies, the reflected waves align with the incoming waves and reinforce each other, creating standing waves. These reinforced frequencies are the harmonics/overtones of the instrument. The blending of harmonics produced by an instrument affects its tone / colour / timbre, creating its distinct sound.
 Standing waves have points of no vibration (nodes) and points of maximum vibration (antinodes). The number of nodes and antinodes increases up the harmonic series. The fundamental note (1st harmonic) of a standing wave has two nodes, and one antinode. One node at each end, and one antinode in the middle. The second harmonic has three nodes, and two antinodes: one node at each end and one the middle, and one antinode between each node. The third harmonic has four nodes and three antinodes, and so on.
 1-3 The Full Harmonic Series (Odd and Even): 
 Brass instruments produce a rich sound containing many harmonics. Even harmonics are frequencies that are multiples of 2 of the fundamental frequency (f2, f4, f6, f8, …). Because they are octaves and fifths relative to the fundamental frequency, they blend harmoniously with the sound.
 Odd harmonics are frequencies that are odd-numbered multiples of the fundamental frequency (f1, f3, f5, f7, …). Odd harmonics add a sharp and edgy quality to the sound because the multiples don’t align as neatly with the fundamental.
 The shape of the instrument’s bore (the tube or column) significantly affects which harmonics it produces and their relative strengths. The sound waves inside a wind instrument are reflected back and forth. Where the wave’s crests and troughs align perfectly, they reinforce each other. Where they are opposite, they cancel out.
 In a straight (cylindrical bore) tube, the air abruptly bounces back and forth. This reinforces some vibrations (odd multiples) while canceling out others (even multiples). 
 The gradual widening of a brass instrument’s conical tube facilitates the full harmonic series because there are no abrupt changes or fixed points that limit the vibrations. It allows the air column inside the instrument to vibrate in a way that doesn’t restrict the formation of standing waves at any harmonic frequency that is an integer (whole number) multiple of the basic pitch (both odd and even).

### 2: The Foundation: Sawtooth Waves 
 2-1 Why not a sine wave? 
 A sine wave is the purest form of sound and contains only the fundamental frequency with no harmonics. It is smooth with no corners or abrupt changes that would require additional harmonics to describe its shape. Brass instrument, however, have a complex harmonic structure. A sine wave cannot capture the harmonic richness of brass sounds.
 2-2 Why not a square wave? 
 A square wave contains only odd harmonics due to its symmetrical shape. Alternating between positive and negative levels results in the cancelation of even harmonics. The result is a hollow or nasal sound, which is uncharacteristic of brass instruments. While this provides more complexity than a sine wave, it lacks the even harmonics essential for replicating the full harmonic series produced by brass instruments.
 2-3 Use a Sawtooth 
 A sawtooth wave is ideal for synthesizing brass sounds because it includes both odd and even harmonics. Its sharp, asymmetrical shape requires all harmonics to fully describe. The underlying explanation involves complex Fourier mathematics that are beyond me.

### 3: Use One Oscillator 
 Brass instruments produce a consistent, stable tone from a single source—the vibrating air column shaped by the player’s lips and the instrument’s tube. Using one oscillator can replicate this. Multiple oscillators can introduce beating or chorus-like effects not characteristic of a brass instrument’s clean, steady tone.

### 4: Add a Sub-Oscillator (Optional) 
 For lower brass instruments like trombones and tubas, adding a sub-oscillator an octave below enriches the sound by reinforcing lower frequencies. This adds depth, fullness, and a powerful presence. The sub-oscillator thickens the overall sound and enhances the fundamental frequency’s robustness.

### 5: Introduce an Initial Raspiness as the Standing Wave Stabilizes 
 5-1 What is the Source of the Raspiness? 
 Brass instruments initially sound raspy because, when the player first buzzes their lips into the mouthpiece, the vibrations are irregular and rough before the air column inside the instrument stabilizes. It takes a moment for the standing waves to fully form and “lock in.” During this brief moment, extra high frequencies and random turbulence are created, giving the sound a raspy or buzzing quality.
 5-2: How to Simulate the Raspiness 
 To emulate this effect on a synthesizer, use rapid modulation to add harmonics and simulate the turbulence of a brass instrument. Modulate the filter, or apple frequency modulation (FM) to the oscillator with a quick burst of a fast LFO. This creates the effect of extra harmonics and turbulence which fades quickly.

### 6: Add Vibrato 
 Brass players often add vibrato after the note has begun. To simulate this, implement a delayed vibrato. Use an envelope with a slow attack to modulate the amplitude of an LFO. Then use the LFO to modulate either the filter or the pitch. Keep it subtle. The vibrato should increase gradually after the note begins, mimicking a player adding expression to sustained notes.
 Slight variations in the vibrato rate and depth can make the effect sound more realistic. Try modulating the faster LFO rate with another slower LFO.
 Try modulating the rate of an LFO with a fast envelope and then using the LFO to modulate either filter cutoff or oscillator pitch. When the envelope is high, you will get high frequency modulation at the start of the note. When the envelope is low, you will get vibrato on the sustain. This allows you to simulate the raspiness and vibrato with a single modulation.

### 7: Shape the Amp Envelope 
 Brass instruments produce sound rapidly, hold their volume, and stop abruptly. They produce a sound that is quickly loud and full, but also have a dynamic evolving timbre. The amplitude envelope controls the volume over time, while the filter envelope controls the brightness. Ensure that the changes in volume and timbre work together naturally.
 7-1 Amp Envelope Attack 
 Brass sounds reach full volume quickly but with a slight buildup, so the envelope should have a fast but not instantaneous attack. This mirrors the time it takes for the player’s breath and lip vibrations to stabilize.
 7-2 Amp Envelope Sustain 
 Once the note is established, brass instruments are capable of holding a steady volume as long as the player continues blowing. Use a relatively high sustain level.
 7-3 Amp Envelope Release 
 Use a short release time. Brass instruments cease producing sound abruptly after the player stops blowing.
 7-4: Use Amp Envelope Velocity 
 Velocity adds expressiveness that mimics the way a brass player can create swells in brightness and dynamics.

### 8: Shape the Filter Envelope 
 8-1 Filter Envelope Attack 
 A brass instrument’s tone gets brighter as the player continues to blow. The harmonics build up over time. It takes a moment for the standing wave to stabilize inside the air column. Set the filter envelope’s attack time slightly longer than the amplitude envelope’s attack. The note should reach full volume before it reaches full brightness.
 8-2: Modulate the Filter Envelope Attack Time with Velocity 
 In real brass instruments, blowing harder establishes a brighter sound more quickly because the higher energy brings out the harmonics faster, while softer playing results in a gentler, gradual build in brightness.
 To simulate this, make the filter envelope attack time velocity sensitive. Soft playing will have longer attack times, resulting in a gradual increase in brightness. Hard playing will have shorter attack times leading to a quicker onset of brightness. This modulation creates a more expressive and responsive patch that closely mirrors the dynamics of a real brass performance.
 8-3: Use Filter Envelope Velocity 
 When synthesizing brass sounds, making the brightness respond to how hard you play is key to achieving realism and expressiveness. Brass instruments have a dynamic timbre that changes over time. Blowing harder increases both volume and brightness.
 When a brass player plays louder, they increase air pressure and lip tension, causing their lips to vibrate with greater energy and complexity. This results in stronger and more complex vibrations within the air column, producing additional and more pronounced harmonics. The extra energy emphasizes higher frequencies, contributing to a brighter, more brilliant sound.

### 9 Fine-Tune the Filter Settings 
 9-1 Filter Type 
 Use a low-pass filter. Use a 24db filter for a smoother, more mellow sound. Use a 12db filter for a harsher, more vibrant sound.
 9-2 Cutoff Level 
 Set the initial cutoff frequency low enough to produce a warm, dark and mellow tone for the lowest notes you want to play. Brass instruments produce sounds rich in harmonics, but the prominence of these harmonics evolves over time. Attenuate the filter to gradually introduce harmonics as needed.
 9-3 Resonance 
 Use resonance sparingly and avoid harshness. A small amount of resonance can emphasize key harmonics around the cutoff frequency. However, excessive resonance can introduce unwanted harshness or shrillness that is uncharacteristic of brass instruments.

### 10 Employ Keyboard Tracking 
 10-1 Higher Notes Are Brighter 
 On a brass instrument, brightness increases with pitch, but the increase is not linear. Brightness becomes more noticeably at mid-to-high pitches but tapers off at the extremes. Higher notes naturally produce more high-frequency overtones, but they don’t increase evenly—they become weaker and more closely spaced together. Also, the bell (the flared end) radiates higher frequencies more efficiently than lower ones, although this effect diminishes at very highest pitches.
 To simulate this, use keyboard tracking to increase the filter cutoff, but set the tracking between 50% to 75%. This range mirrors the nonlinear increase in brightness on real brass instruments.
 10-2 Combine Filter Tracking and Velocity 
 On brass instruments, playing louder generates disproportionately more upper harmonics, which makes the brightness increase more pronounced at higher velocities.
 Modulate pitch with velocity, then route it to the filter. This will allow louder, high-pitch notes to be brighter than softer high pitch notes.
 Keep resonance under control. Monitor resonance levels at higher pitches. Excessive resonance can make the sound overly sharp or piercing. Adjust accordingly to maintain a natural brass timbre across the keyboard range.

### 11 Increase Resonance with Velocity (Subtly) 
 11-1 Why do Louder Notes Have More Resonance? 
 Playing louder introduces more energy into the instrument, which can enhance the resonance of specific frequencies, especially higher harmonics, contributing to the brilliance and richness of louder brass notes.
 11-2 Implementing Resonance Modulation 
 Send velocity to filter resonance. Subtly increase resonance as velocity increases. But use it sparingly. Adjust resonance modulation carefully to avoid making the sound harsh or unnatural. The goal is to achieve a nuanced enhancement, not an extreme effect.

### 12: Create an 80’s Style Synth Brass Ensemble 
 12-1 Use Multiple Oscillators 
 Use multiple sawtooth oscillators. Detune the oscillators slightly to create a chorus-like effect, to simulate multiple instruments playing together. Adjust the mix to ensure a cohesive sound ensuring on oscillator overpowers the others.
 12-2 Detune One Oscillator with a Burst of FM 
 Send a fast envelope to only one oscillator’s pitch FM. Set the envelope with an immediate attack, and a quick decay. It should be just a fast blast. This creates a slight detuning on the initial burst, which quickly corrects itself.

### Thanks for Reading 
 I’m neither a brass player nor a physicist. I’m sure the above is riddled with errors. Correct me where I’m wrong!

### Further Reading
 Synthesizing Wind Instruments 
 Gordon Reid delves into the fundamentals of synthesizing wind instruments, explaining the similarities between vibrating strings and air columns in pipes, and how to recreate them.

 Synthesizing Brass Instruments 
 The article explains the principles of synthesizing brass instruments, emphasizing the importance of amplitude, tone, and pitch contours, while using subtractive synthesis methods to recreate realistic trumpet-like sounds.

 Roland SH101 & ARP Axxe Brass Synthesis 
 How to synthesize brass sounds on simple monosynths like the Roland SH101 and ARP Axxe by adapting idealized brass patches to suit their more limited capabilities.

 Brass Synthesis On A Minimoog 
 Gordon Reid demonstrates how to create brass patches on the Minimoog, despite its lack of advanced features.

 Porcaro synthesize analog brass 
 A YouTube video where Steve Porcaro demonstrates how to synthesize a synth brass lead by focusing on shaping the attack using sharp, transient "blip" envelopes on one oscillator.

 Brass 

 Peter Barata 

 Previous

 Previous

## 808 Clave Synthesis

 Next

 Next

## 808 Clap Synthesis