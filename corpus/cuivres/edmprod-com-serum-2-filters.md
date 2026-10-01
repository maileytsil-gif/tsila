---
titre: "EDMProd — Serum 2 filters"
source: https://www.edmprod.com/serum-2-filters/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Serum 2 Filters: A Practical Guide to Sound Design - EDMProd 

 Skip to content 

# Serum 2 Filters: A Practical Guide to Sound Design

### Bonus material: download our biggest sample pack (700+ samples) for free! 

 Sam Matla 

 September 10, 2026 

 A filter can do much more than make a synth darker. In Serum 2, it can turn a plain saw into a talking bass, add a metallic pitch to a square wave, make a pluck feel rubbery, or give a sustained note movement without changing the oscillator.

 The trick is knowing which filter family gets you close—and which control to move once you get there.

 This guide takes you from everyday low-pass filtering to combs, formants, Diffusor, and the drawable PZ SVF. You’ll hear short examples throughout, see the relevant controls up close, and finish with a few focused exercises you can use in your next patch.

 Free Ableton tools & resources

### Give your next session a head start.
 Open the Ableton Vault for free instruments, effect racks, and project files you can explore in Live.
 Unlock the Free Ableton Vault ↗ 

 Adapted from John’s EDMProd video, Serum 2’s Filters Are Insane (Here’s How to Use Them) . Screenshots, animations, and listening excerpts come from that demonstration. Additional exercises and technical clarifications expand the lesson; they are starting points, not exact preset recreations.

 Before you start: Open Serum 2 in your DAW and load an initialized patch. If the overall interface is new to you, start with our Serum 2 beginner’s guide . This lesson focuses on the synth’s Filter 1 and Filter 2 modules. Serum 1 shares many of the older filter types, but the newer models, dual-filter workflow, and screenshots here use Serum 2.

 Listening note: These are excerpts from a continuous sound-design session, not a controlled, loudness-matched shootout. Notes, settings, routing, and occasional effects change. Start at a comfortable playback level, and use each clip to hear the behavior described beside it.

## 1. Choose a filter by the sound you want

 Don’t begin by auditioning every menu item. Start with a specific job: soften a bright sound, reveal a harmonic, create movement, or change the sound’s texture. Then compare two or three related models with the same oscillator and MIDI phrase.

 What you want 
 Start here 
 First thing to explore 

 Softer highs, a pluck, or a rounded bass 
 Low or MG Low 
 Cutoff, then an envelope 

 A bright layer above a separate sub 
 High 
 Cutoff and source routing 

 A narrow, nasal sound 
 Band 
 Cutoff and resonance 

 A particular harmonic to stand out 
 Peak 
 Cutoff and key tracking 

 Movement inside a sustained bass 
 Notch or a Multi filter 
 Slow cutoff modulation 

 Metallic or hollow coloration 
 Comb, Flanger, or Phaser 
 Cutoff, resonance, and Mix 

 Vowel-like movement 
 Formant or PZ SVF 
 Cutoff or the X/Y position 

 Grainy, digital texture 
 SampHold 
 Cutoff and Mix 

 Smeared or rubbery attacks 
 Reverb or Diffusor 
 Cutoff and the secondary control 

 Resonant acid character 
 French LP or Acid Ladder 
 Resonance and Drive 

 Aggressive feedback 
 Scream or MG Dirty 
 Small changes to Drive and feedback controls 

 The video’s menu groups the filters into Normal, Multi, Flanges, Misc, and S2 Filters. Those categories help you browse, but they aren’t a musical rulebook. A filter from the “Misc” group can be the central ingredient in a bass patch.

 Serum 2’s filter menu groups everyday shapes alongside more specialized sound-design models. Video 0:36 · Enlarge screenshot 

 For a broader explanation of the basic shapes, see our audio filters guide . Here, we’ll concentrate on what to do with them inside Serum.

## 2. Set up the signal path before judging a filter

 A filter only changes the audio that reaches it. If Cutoff seems to do nothing, check routing before choosing a more extreme model.

 Enable one oscillator with a harmonically rich waveform, such as a saw.

 Enable Filter 1.

 Check the oscillator’s routing switch under the filter display. A, B, C, S, and N refer to the three main oscillators, Sub, and Noise.

 Start with Mix fully wet, modest resonance, and low Drive.

 Bypass other effects while you learn the filter’s contribution.

 The source switches determine which oscillators feed the selected filter. Check routing before troubleshooting the sound. Video 6:47 · Enlarge screenshot 

 A saw makes this easier than a sine because it gives the filter more harmonics to reshape. If there’s almost no high-frequency content in the source, opening a low-pass filter won’t suddenly produce a bright sound.

 Serum 2 gives you two filter modules. You can use them to treat different oscillator layers or build a more involved signal path through the mixer. For this lesson, get a useful result from one filter first. Add the second with a clear purpose, such as controlling brightness after a character effect. Check the mixer routing rather than assuming that enabling both automatically creates the chain you intended.

## 3. Understand Cutoff, Resonance, Drive, and Fat

### Cutoff and slope: where the sound changes, and how sharply

 For a low-pass filter, lowering Cutoff reduces more of the upper spectrum. A high-pass works in the other direction, reducing frequencies below its transition region. Neither is a brick wall: the transition has a shape.

 The numbers in names such as Low 6, Low 12, and Low 24 describe the nominal slope in decibels per octave. An octave above a frequency is twice that frequency: 500 Hz to 1 kHz, for example.

 A steeper slope generally separates the passed and reduced frequency regions more strongly. A gentler slope leaves more of the surrounding material audible. That’s why a 6 dB/octave setting can remain relatively bright even when the cutoff is low.

 MG Low 18 shows a steeper response than the gentler 6 and 12 dB/octave options demonstrated earlier. Video 2:18 · Enlarge screenshot 

 Try it: Hold a low saw note and keep Cutoff fixed. Switch between 6, 12, 18, and 24 dB/octave. Listen to the remaining buzz above the note, then adjust Cutoff to make each version musically useful. Don’t assume a steeper setting is automatically better.

 A 12 dB/octave slope isn’t “twice as loud” or “twice as filtered” as a 6 dB/octave slope. The number describes how the response falls away, not a simple perceived-intensity scale.

### Resonance: bring attention to the moving edge

 Resonance makes the filter’s characteristic frequency region stand out. On a low-pass, that often produces the pointed, whistling quality that turns a plain sweep into a squelch.

 Increasing resonance produces a more prominent peak in this low-pass response. Video 2:43 · Enlarge screenshot 

 Listen · 2 seconds

### Resonance adds a pointed sweep
 Listen for the pointed, squelchy tone as the resonant region moves.
 Open audio example Excerpt from the course · Watch in context (2:42) 

 The low end may change as resonance increases, depending on the model. Judge the complete sound: a dramatic resonant peak can feel exciting by itself while leaving a bass too thin underneath.

### Drive: change what enters the circuit

 Drive pushes the filter harder. On models with nonlinear behavior, that changes harmonic content as well as level. Two filters at similar cutoff settings can respond quite differently when driven.

 Drive is part of the filter’s character, so compare it with the output level kept under control. Video 3:46 · Enlarge screenshot 

 Listen · 3 seconds

### Drive on a state-variable low-pass
 A short example of the driven Low filter from the source session.
 Open audio example Excerpt from the course · Watch in context (3:36) 

 Listen · 1 seconds

### Drive on MG Low
 The adjacent MG Low example; compare character, not loudness.
 Open audio example Excerpt from the course · Watch in context (3:45) 

 These adjacent excerpts demonstrate different low-pass models from the source session. They are brief character examples, not a matched test of which model is louder or better.

 When building your own comparison, use the same note, oscillator level, and modulation. After raising Drive, reduce the filter’s output Level if necessary. That makes it easier to hear the tonal difference without simply preferring the louder version.

### Fat: more than a low-end compensation knob

 Fat occupies the variable-control position beneath the filter. Its function changes when you choose another model, so always read the label.

 Fat occupies the same position that becomes Morph, Freq, Damp, and other model-specific controls. Video 4:07 · Enlarge screenshot 

 One useful clarification to the video: for the standard models, Xfer describes Fat as saturation in the resonance path. Treat it as a character control, not automatic gain compensation. It may help you find a fuller result, but use Level to make the final volume adjustment. See the filter section of the official Serum 2 manual for model-specific behavior.

## 4. Make a filter move across the stereo image and keyboard

### Filter Pan offsets the left and right cutoffs

 Serum’s filter Pan is different from the oscillator’s ordinary pan control. Instead of simply placing a sound to one side, it gives the left and right channels different cutoff positions.

 Play Pause demonstration · 5-second GIF Filter Pan separates the left and right cutoff positions, creating a stereo difference in tone. Video 5:01 · Enlarge screenshot 

 Listen · 4 seconds

### Stereo cutoff offset
 Listen on headphones for the left/right difference in tone.
 Open audio example Excerpt from the course · Watch in context (4:59) 

 A centered setting gives you a sensible baseline. Move it gently in either direction while listening on headphones. The effect is a difference in filtering between the channels; it isn’t just a volume pan.

### Add an LFO for motion

 Drag an LFO onto the filter Pan control. Keep the base position centered and use bipolar modulation if you want the movement to travel either side of that setting. Begin slowly with a modest modulation amount.

 Play Pause demonstration · 5-second GIF An LFO moves the stereo cutoff offset while the oscillator continues playing. Video 5:24 · Enlarge screenshot 

 Listen · 6 seconds

### Moving the stereo cutoff with an LFO
 Listen for motion across the stereo image while the note sustains.
 Open audio example Excerpt from the course · Watch in context (5:22) 

 A slow rate gives an obvious traveling movement. Faster motion creates a different texture. Check the patch in mono as well as stereo, especially if it carries the low end of your track.

 You can also lower Mix to blend the filtered signal with the original. This can preserve some of the source’s body while retaining the movement. Because the two paths can interact in phase, a halfway setting is a sound-design choice rather than a guarantee of unchanged bass.

 Listen · 6 seconds

### Blending dry sound with the moving filter
 The original sound is blended with stereo-filtered movement.
 Open audio example Excerpt from the course · Watch in context (6:09) 

### Key tracking keeps the filter related to the notes

 Without key tracking, the cutoff stays at its set frequency as you play different notes. That can make the upper notes in a phrase much duller or quieter than the lower ones.

 Key tracking lets the filter’s frequency follow pitch instead of staying fixed across the keyboard. Video 7:21 · Enlarge screenshot 

 With key tracking enabled, the cutoff moves with pitch. This is especially useful when you tune a Peak or Comb to a particular harmonic and want that relationship to remain recognizable across a melody.

 Test the whole phrase. Key tracking gives you a more consistent relationship to pitch; it doesn’t guarantee equal loudness on every note. Highly resonant or nonlinear filters can still behave differently across the keyboard.

 Master Serum 2

### Build sounds with a clear purpose.
 Explore the full Master Serum 2 course to connect filters with oscillators, modulation, routing, and practical sound design.
 Explore Master Serum 2 ↗ 

## 5. Build useful sounds with the Normal filters

### Low and MG Low: start with an envelope

 Low-pass filters are useful for far more than removing harshness. A short envelope on Cutoff can create the bright attack and darker body of a pluck. A slow envelope can let a pad gradually open.

 Start with a saw, lower Cutoff, then drag an unused envelope onto it. Give that envelope a fast attack, a short decay, and low sustain. Adjust the modulation amount until each note opens enough to speak, then settles back into the darker tone.

 MG Low offers a different character from the Low family. Compare both before adding effects. Sometimes a modest change in the filter model does more than another layer of distortion.

### High: separate an upper layer from the sub

 A high-pass can reduce low-frequency material in a bright layer while a separate oscillator supplies the foundation. In the video, John combines an upper sound with a low sub and uses filtering to separate their roles.

 High-pass filtering shapes the upper layer while routing determines whether the sub is affected. Video 8:40 · Enlarge screenshot 

 The routing matters as much as the cutoff. If you want a steady sub, don’t accidentally send it through the same high-pass. Listen to the layers together: a gap between them can sound hollow, while too much overlap can feel crowded. Our sub-bass guide goes further into giving the low end a clear role.

### Band: isolate a narrow part of the sound

 A band-pass reduces material both above and below its pass region. It’s a useful starting point for a nasal lead, a small radio-like layer, or a moving accent that leaves space around it.

 A band-pass leaves a focused region while reducing material on both sides. Video 9:06 · Enlarge screenshot 

 Sweep through the middle of a rich waveform and notice how quickly the identity changes. If the sound is too small to carry a part, use it as a layer or blend some dry signal back in.

### Peak: make one harmonic part of the identity

 Instead of broadly darkening the sound, a Peak filter can emphasize a particular region. John demonstrates this with a square wave and key tracking.

 Tune a Peak to a useful harmonic, then test key tracking across the notes in your phrase. Video 9:37 · Enlarge screenshot 

 Listen · 4 seconds

### A keytracked peak changes the tone
 Listen for the emphasized overtone as John plays different notes.
 Open audio example Excerpt from the course · Watch in context (9:37) 

 Hold one note, move Cutoff until a useful overtone stands out, and then play the phrase. Enable key tracking and compare. This is a good way to make a simple waveform feel more distinctive without immediately reaching for another oscillator.

### Notch: create movement by taking something away

 A notch removes a region rather than boosting it. Move that gap through a harmonically rich sound and the changing balance creates motion.

 Play Pause demonstration · 5-second GIF A slow notch sweep reshapes the spectrum of a detuned bass without moving its fundamental pitch. Video 10:29 · Enlarge screenshot 

 Listen · 5 seconds

### A moving notch in a detuned bass
 Listen for movement inside the detuned bass rather than a pitch bend.
 Open audio example Excerpt from the course · Watch in context (10:30) 

 For a Reese-style starting point, use a detuned saw sound and a slow LFO on the notch cutoff. Keep the sweep limited at first. Listen for a moving texture inside the bass, then check that the lowest notes still have the weight you need.

## 6. Use Multi filters for two movements at once

 The Multi names tell you which shapes are combined. For example, LP means Low plus Peak in this group, and PP gives you two peaks. Don’t confuse a two-letter combination with the name of an ordinary low-pass filter elsewhere in the menu.

 Play Pause demonstration · 5-second GIF A dual-peak filter exposes a second frequency control so the two peaks can move independently. Video 11:20 · Enlarge screenshot 

 The main Cutoff controls one region; the second frequency control positions the other. You can use separate LFOs to keep those movements from repeating together too quickly.

 Listen · 6 seconds

### Two peaks moving at different rates
 Two moving regions reshape the same sustained sound.
 Open audio example Excerpt from the course · Watch in context (11:22) 

 Start with one slow movement. Once that sounds good, add a second at a different rate and reduce its depth. If both controls sweep across their entire range, the patch can lose its identity.

 The morphing Multi filters offer another approach: blend between different response shapes. Moving Morph can change the kind of filtering as well as its emphasis.

 Play Pause demonstration · 5-second GIF Morph changes the response between the available shapes instead of only moving one cutoff. Video 12:01 · Enlarge screenshot 

 Listen · 2 seconds

### Morphing between filter responses
 Listen for the response changing character during the sweep.
 Open audio example Excerpt from the course · Watch in context (12:04) 

 Try it: Record four bars with a static Morph position, then four with slow modulation. Use the second version only where the arrangement needs extra movement. A filter doesn’t have to move constantly to be useful.

## 7. Explore combs, flangers, and phasers

 These filters are useful when you want a hollow, metallic, sweeping, or strongly colored result. They can change the apparent tone enough that one oscillator feels like a more complicated sound.

### Comb: tune the coloration

 A comb response has repeated peaks and notches. A delayed version of a signal interacting with another path is a common way to create that pattern. Changing the delay relationship changes the spacing of the response.

 Play Pause demonstration · 5-second GIF Comb filtering creates a repeating pattern of emphasis and cancellation across the spectrum. Video 13:15 · Enlarge screenshot 

 Listen · 8 seconds

### A comb filter follows the notes
 Listen for a pitched, hollow coloration across the played notes.
 Open audio example Excerpt from the course · Watch in context (13:13) 

 Find a cutoff position that complements the note, then try key tracking. If the effect feels tuned on one note but odd on the rest, this is one of the first things to check.

 Positive and negative comb variants change the pattern. They aren’t simply “more” and “less” versions of the same effect. Compare them on the actual phrase, at a sensible output level.

 Listen · 4 seconds

### Stereo movement with a comb filter
 A short example of changing stereo coloration with a comb.
 Open audio example Excerpt from the course · Watch in context (13:40) 

### Feedback filtering changes the character

 Some comb, flanger, and phaser variants include low-pass or high-pass filtering in their feedback paths. This shapes the recirculating signal; it isn’t the same as leaving part of the original audio completely unprocessed.

 The extra frequency control shapes the feedback behavior of this comb variant. Video 14:24 · Enlarge screenshot 

 Use a lower feedback low-pass cutoff to explore a less bright result, or the high-pass variant when low-frequency feedback is dominating. Adjust Mix as well as the frequency controls. A partially wet setting can produce a very different response from fully wet.

### Flanger: sweep the harmonic pattern

 Flanging is associated with a moving comb pattern and the familiar jet-like sweep. In Serum, use the selected filter’s controls and modulation to create the movement you want; don’t assume its name means a slow sweep happens automatically.

 Play Pause demonstration · 5-second GIF Moving the Flanger cutoff changes the repeated pattern and can produce a vocal-like coloration. Video 15:54 · Enlarge screenshot 

 Listen · 6 seconds

### A flanger sweep with a vocal-like tone
 Listen for the vowel-like sweep created by the shifting pattern.
 Open audio example Excerpt from the course · Watch in context (15:54) 

 Try a restrained sweep over a sustained midrange layer. Then compare a quicker envelope-driven movement for a short effect or fill. The same filter can sit in the background or become the hook, depending on the modulation.

### Phaser: a different kind of movement

 A phaser uses frequency-dependent phase shifts rather than the same simple delay relationship as a comb. When the affected and dry signals interact, that can create a series of moving cancellations.

 The Phaser response offers another pattern of notches and peaks to move through a sound. Video 16:48 · Enlarge screenshot 

 Listen · 8 seconds

### A phaser changes the harmonic balance
 Listen for the changing hollow and full regions in the tone.
 Open audio example Excerpt from the course · Watch in context (16:33) 

 More complex phaser variants change the pattern, but don’t read their numbers as though they were the slope of Low 24. Start with the less complex option and add complexity only when the result improves.

 Serum also combines phaser and flanger behaviors in some models. Those are worth trying when you want a more obvious texture, but listen in the track before deciding a bigger sweep is the better one.

## 8. Turn the Misc filters into sound-design tools

 This group includes EQ-like shapes, modulation effects, digital distortion, and phase-based textures. The Cutoff knob doesn’t always behave like an ordinary low-pass cutoff here.

### EQ filters: reshape a region

 The Low, Band, and High EQ options offer another way to rebalance a waveform. Use them when you want to bring a region forward or back rather than simply close the top end.

 The EQ models offer a different way to rebalance the oscillator’s spectrum. Video 18:13 · Enlarge screenshot 

 Listen to the whole note after making a change. A resonant shape that looks helpful on a graph can still pull attention away from the musical part. Keep the setting only if it solves an audible problem or adds a useful character.

### Ring Mod: add sidebands and metallic tone

 Ring modulation multiplies signals together. A simple example produces new components at the sum and difference of the input frequencies. With a harmonically rich source, that can create a much more complicated, metallic sound.

 Ring Mod uses Cutoff to control the modulation frequency; Mix helps blend its character with the source. Video 19:37 · Enlarge screenshot 

 Listen · 7 seconds

### Ring modulation blended into a square wave
 Listen for the metallic upper texture mixed with the source.
 Open audio example Excerpt from the course · Watch in context (19:35) 

 Start with a low Mix setting. Raise it until you hear an extra edge, then play a melody. Key tracking can help keep the effect related to the notes. The x2 version adds another modulation stage to explore, so introduce it only after you understand the simpler version.

 A full-wet result can be useful for an atonal hit or effect. If you’re making a pitched bass or lead, check that the musical pitch remains clear enough for its job.

### SampHold: introduce digital grain

 The sample-and-hold model creates a rough, digital texture as its effective sampling rate changes. This is different from simply reducing bit depth, even though both can sound deliberately degraded.

 Play Pause demonstration · 5-second GIF Lowering Cutoff in SampHold creates increasingly obvious digital coloration. Video 21:26 · Enlarge screenshot 

 Listen · 9 seconds

### Reducing the sample-and-hold rate
 Listen for the increasing digital grain as the rate falls.
 Open audio example Excerpt from the course · Watch in context (21:23) 

 Use a simple waveform while learning this one so the new texture is easy to identify. Then try a small amount on a more complex bass. A little grain can help a layer speak; an extreme setting can turn it into an effect.

 SampHold- is the difference variant. It emphasizes what differs between the processed and original signal rather than merely offering a gentler amount. Don’t think of the minus symbol as “less distortion.”

### Combs, Allpasses, and Reverb: reshape the texture over time

 These models are useful for smearing attacks and adding a resonant or spatial impression. The Reverb filter is a sound-design tool inside the synth, not a replacement for every job you might give a room or hall effect.

 The Reverb filter gives the oscillator a smeared, resonant texture before any conventional reverb effect. Video 23:35 · Enlarge screenshot 

 Listen · 6 seconds

### The Reverb filter adds a smeared texture
 Listen for the blurred, resonant texture rather than a conventional long reverb tail.
 Open audio example Excerpt from the course · Watch in context (23:34) 

 An ideal all-pass changes phase without changing its magnitude response. That still matters to transients and to how paths combine. Serum’s more complex combinations, damping, drive, and dry/wet blend can change the result further. A flat-looking amplitude graph doesn’t mean the processing is inaudible.

 Try a short note rather than only a sustained one. The attack can reveal the effect more clearly. Use damping to explore a smoother result if the upper texture becomes too brittle.

### French LP and German LP: choose by character

 French LP is a useful place to explore squelchy, nonlinear filtering. Its secondary resonance control, BOEUF, gives you another interaction to work with alongside the main resonance and Drive.

 French LP combines the main resonance with a second resonance control labeled BOEUF. Video 24:30 · Enlarge screenshot 

 Listen · 4 seconds

### French LP resonance and drive
 Listen to the squelchy interaction of resonance and drive.
 Open audio example Excerpt from the course · Watch in context (24:30) 

 Make small changes to one control at a time. If a setting becomes thin or disappears, back off the interaction rather than immediately turning up the output.

 German LP gives you a different low-pass character to compare on the same phrase.

 German LP provides another low-pass character for basses and leads. Video 25:03 · Enlarge screenshot 

 Listen · 5 seconds

### German LP character
 A short low-pass character example from the same source session.
 Open audio example Excerpt from the course · Watch in context (25:02) 

 The useful question is whether the filter gives your patch the attack, weight, and tone it needs. You don’t need to identify a vintage circuit by ear before making a good choice.

### Add Bass: experiment beyond the name

 John uses Add Bass for an aggressive sound-design example with two sine oscillators at different pitches. The interesting result comes from their interaction with the processing, not just a simple low-frequency boost.

 Play Pause demonstration · 5-second GIF The Add Bass example combines two pitched oscillators with modulation of several filter controls. Video 26:48 · Enlarge screenshot 

 Listen · 6 seconds

### Add Bass with several controls moving
 Listen for the changing distortion as several controls move.
 Open audio example Excerpt from the course · Watch in context (26:47) 

 Begin with the oscillators held steady, then explore Drive. Add movement to one parameter and listen before introducing another. THRU changes the contribution of a phase-rotated dry path, so don’t treat it as interchangeable with the main Mix control.

 Save a useful static version first. That gives you a way back if several moving controls turn an interesting bass into an unpredictable sweep.

### Formant: make the filter talk

 Formant filters emphasize patterns that resemble vowel sounds. A harmonically rich oscillator gives them material to work with, and movement across those patterns creates the talking quality.

 Play Pause demonstration · 5-second GIF Slow formant movement and a short delay turn a simple oscillator into a more animated phrase. Video 27:50 · Enlarge screenshot 

 Listen · 14 seconds

### Formant movement with short ping-pong delay
 Vowel-like filtering with the short ping-pong delay added in the demonstration.
 Open audio example Excerpt from the course · Watch in context (27:39) 

 This excerpt includes the short ping-pong delay added in the video. Listen for the vowel movement, then notice how the delay repeats it in space. The delay is part of this example’s result.

 For your own patch, start without delay. Find two useful vowel positions, then modulate slowly between them. Add the effect only once the dry phrase works. The different Formant models are worth comparing on the same source rather than assuming one works best on every waveform.

### Bandreject: remove a wider region

 Bandreject reduces a band and leaves material either side of it. Use Width to explore the size of the missing region.

 Bandreject carves out a region while leaving frequencies above and below it. Video 28:41 · Enlarge screenshot 

 Listen · 5 seconds

### A band removed from the sound
 Listen for the hollowing effect as a region is removed.
 Open audio example Excerpt from the course · Watch in context (28:38) 

 This can work as an animated texture or a temporary arrangement effect. If the sound suddenly loses its identity, narrow the cut or reduce the sweep range.

### Distorted combs and Scream: use feedback deliberately

 The distorted comb variants combine comb behavior with pass filtering. They’re useful when a cleaner comb is close but doesn’t have enough aggression. Change the comb frequency and main cutoff separately so you can hear what each contributes.

 Scream takes you toward more extreme feedback. Its secondary control affects that feedback behavior, so small moves can make a large difference.

 Scream’s feedback controls can produce dramatic changes, especially with higher Drive. Video 29:24 · Enlarge screenshot 

 Listen · 7 seconds

### Scream feedback changes the tone
 Listen to how quickly the feedback character changes.
 Open audio example Excerpt from the course · Watch in context (29:22) 

 Turn the output down before exploring extremes. Judge the note’s body as well as the scream: a spectacular isolated texture still needs a role in the track. When a setting nearly silences the patch, reduce the feedback interaction and check the routing before adding gain.

 Superknobs · Core Collection

### Find the character. Keep the idea moving.
 Working in Ableton Live? Add a Superknobs audio effect rack after Serum for another layer of movement, space, or distortion. These are Ableton effects, separate from Serum’s internal filters.
 Explore Superknobs ↗ For Ableton Live 11 & 12 Standard and Suite.

## 9. Explore the newer Serum 2 filters

 The newer models give you more starting characters, from restrained filtering to extreme feedback. Learn them with a simple source first, then bring them into your existing patches.

### Wsp: morph the response

 Wsp is useful for a buzzy, characterful sweep. Its morphing behavior moves between low-pass, notch, and high-pass responses.

 Wsp combines a characterful filter with a morphable response. Video 30:47 · Enlarge screenshot 

 Listen · 4 seconds

### Wsp morphing filter
 Listen for the character of the morphing response.
 Open audio example Excerpt from the course · Watch in context (30:47) 

 Try a modest envelope on Cutoff and hold Morph steady. Then switch: hold Cutoff in a useful region and move Morph. Those are two different ways to animate the same patch.

### DJ Mixer: a quick sweep

 DJ Mixer offers a direct high-pass/low-pass style sweep. Reach for it when you want a simple movement across a transition rather than a complicated resonant texture.

 DJ Mixer is a straightforward option for broad filtering gestures. Video 31:13 · Enlarge screenshot 

 Listen · 4 seconds

### DJ Mixer sweep
 A straightforward sweep across the filter range.
 Open audio example Excerpt from the course · Watch in context (31:12) 

 Make the sweep serve the phrase. A brief move at the end of four bars can be more effective than filtering every note.

### Diffusor: change the feel of a pluck

 Diffusor is especially interesting on short notes. Its phase-based processing can give an attack a rubbery, spreading quality, and the stage control lets you explore the intensity.

 Play Pause demonstration · 5-second GIF The Diffusor example combines a short envelope with an arpeggiated pattern. Video 32:15 · Enlarge screenshot 

 Listen · 7 seconds

### Diffusor in a plucked arpeggio
 Listen to the rubbery attacks in this arpeggiated, multi-filter patch.
 Open audio example Excerpt from the course · Watch in context (32:13) 

 The source example uses an arpeggiator and another filter as part of the patch. It demonstrates the finished combination, not an isolated Diffusor A/B. To hear its role in your own patch, bypass only Diffusor while leaving the phrase and other processing unchanged.

 For a rhythm to test it on, follow our Serum 2 arpeggiator guide . Keep the notes short enough to hear how the attacks change.

### MG Ladder, Acid Ladder, and EMS Ladder

 These are related choices in the sense that all can shape a resonant synth part, but they give you different characters to audition. MG Ladder is a useful restrained starting point; Acid Ladder invites a more pointed, resonant phrase; EMS Ladder offers another character to explore with sustained notes or effects.

 MG Ladder is a useful point of comparison before exploring more driven models. Video 32:35 · Enlarge screenshot 

 Acid Ladder gives this example a pronounced resonant character. Video 33:08 · Enlarge screenshot 

 Listen · 6 seconds

### Acid Ladder at high resonance
 Listen for the pronounced resonance in this acid-style phrase.
 Open audio example Excerpt from the course · Watch in context (33:08) 

 The EMS Ladder example adds delay around a resonant phrase. Video 33:37 · Enlarge screenshot 

 Listen · 6 seconds

### EMS Ladder with delay
 A resonant phrase with delay enabled in the source patch.
 Open audio example Excerpt from the course · Watch in context (33:35) 

 The EMS excerpt includes delay. To compare the filters themselves, disable the delay and use identical notes. Don’t infer an exact slope or a perfect hardware match just from how a model’s graph looks.

### MG Dirty: explore the interaction carefully

 MG Dirty goes much further into driven behavior. Treat Drive and PAIN as interacting sound-design controls and approach strong settings gradually.

 MG Dirty adds a PAIN control alongside Drive for much more extreme character. Video 34:05 · Enlarge screenshot 

 Listen · 4 seconds

### MG Dirty driven hard
 Listen to the unstable, driven texture.
 Open audio example Excerpt from the course · Watch in context (34:04) 

 Once you find a useful region, constrain modulation to that region. Mapping an entire knob range can make a playable patch disappear or become much louder midway through a phrase.

### Comb 2 and the Exp filters

 Comb 2 adds another resonant option, with a second frequency control to explore. It’s a good candidate when a bass or effect needs an unusually strong tonal signature.

 Comb 2 exposes a second frequency control for exploring its resonant character. Video 34:48 · Enlarge screenshot 

 Listen · 11 seconds

### Comb 2 resonance
 Listen for the strong resonant tone and changing coloration.
 Open audio example Excerpt from the course · Watch in context (34:31) 

 Exp MM gives you a multimode response to sweep between, while Exp BPF focuses on a band-pass character. Compare them with the everyday shapes before adding modulation.

 Exp MM offers another morphable response to compare with the Normal and Multi families. Video 35:10 · Enlarge screenshot 

 Listen · 3 seconds

### Exp MM changes its response
 Listen for the tone changing as the multimode response blends.
 Open audio example Excerpt from the course · Watch in context (35:10) 

## 10. Draw and morph your own filter with PZ SVF

 PZ SVF is the most open-ended part of the demonstration. You can create different filter shapes and move between them, making the transition itself part of the sound.

 If it initially seems to do nothing, don’t assume it’s broken. Open the editor and inspect what’s loaded. A flat starting response won’t behave like a ready-made low-pass just because you move Cutoff.

### Start with one understandable shape

 Select PZ SVF and open its pencil editor.

 Choose one of the four corner states.

 Add or adjust a filter element in that state.

 Use the element’s context menu to explore its type.

 Listen to that corner before editing the others.

 The PZ SVF editor lets you build a response from editable filter elements. Video 36:21 · Enlarge screenshot 

 Begin with a modest bell or simple pass shape. Make a second state with a noticeably different but still useful tone. Only then add the remaining states.

### Move through useful sounds

 The X/Y position moves between the four states. Your goal is a playable path through them, not merely four interesting corners.

 Play Pause demonstration · 5-second GIF The four-state setup lets the filter change character as its X/Y position moves. Video 36:54 · Enlarge screenshot 

 Listen · 8 seconds

### A hand-drawn PZ SVF combination
 An intentionally exploratory hand-drawn configuration; the response is quite extreme.
 Open audio example Excerpt from the course · Watch in context (37:24) 

 John’s hand-drawn example becomes quite extreme. That’s a useful lesson: combinations need listening and adjustment. Test the center and the edges, and reduce excessive boosts before adding automatic movement.

 Don’t assume that an all-pass element directly boosts bass on its own. Listen to the complete configuration and the way its elements interact.

### Use factory shapes as a starting point

 The editor’s preset menu offers a faster route into usable responses. In the demonstration, Single loads one state, while Multi changes the four-state setup.

 Listen · 3 seconds

### A factory PZ SVF multi preset
 A factory multi configuration provides a more restrained starting point.
 Open audio example Excerpt from the course · Watch in context (37:52) 

 The AEIOU multi preset gives you a clear example of vowel-like movement. It’s a useful starting point for understanding what a well-organized group of states can do.

 Play Pause demonstration · 5-second GIF The AEIOU setup provides a ready-made route through vowel-like filter responses. Video 38:05 · Enlarge screenshot 

 Listen · 5 seconds

### AEIOU vowel movement
 Listen for the vowel movement in the AEIOU multi preset.
 Open audio example Excerpt from the course · Watch in context (38:03) 

 Once the manual sweep sounds good, add slow modulation or a macro. Limit its range to the movement you actually want, and check every note in the part. A small usable region is often more valuable than a full-range sweep.

## 11. Turn the lesson into three useful patches

 These exercises extend the ideas in the video. The settings are starting suggestions, so adjust them to the octave, rhythm, and source you’re using.

### Patch one: a pluck that opens and settles

 Use one saw oscillator and Low or MG Low. Lower Cutoff until the sustained sound is dark, then add an envelope with a fast attack, short decay, and low sustain. Increase the modulation depth until the attack speaks clearly.

 Play a short chord progression. If the upper notes disappear, compare key tracking on and off. Add a little resonance for definition, then compare the patch against the bypassed filter at a similar level.

 Save two versions: one short and bright, one longer and softer. You now have two musical options rather than twenty unfinished filter experiments.

### Patch two: a moving bass with a stable foundation

 Use a detuned saw layer through Notch or a dual-notch Multi filter. Start with slow, shallow modulation. Add a separate sub only if the arrangement needs it, and check that its routing avoids the moving filter.

 Play the actual bass line with the kick. Reduce the sweep if certain notes lose too much body. Check mono playback, then record a phrase so you can compare the moving version against a static one.

### Patch three: a talking phrase

 Start with Formant or a PZ SVF factory multi. Find two vowel positions that work on the same note, then create a restrained movement between them. Use a short MIDI phrase rather than holding one note forever.

 Add a little delay only after the dry sound works. If the repeats blur the rhythm, reduce feedback or shorten the notes. Our Serum 2 Clip Sequencer guide can help you turn the sound into a repeatable pattern.

 For another practical exercise, open a patch from our Serum 2 presets guide , save a copy, and identify what changes when you bypass its filters. Then recreate just that part of the patch from an initialized sound.

 The 7 Day Song Finishing System

### Give that loop a finish line.
 Follow a structured workflow from the first musical idea through arrangement, mixdown, and export—with a clear task for each day.
 Explore the Song Finishing System ↗ 

## 12. Troubleshoot the filter before adding another effect

 Problem 
 What to check first 

 Cutoff does nothing 
 Filter enabled, correct source routing, audible wet Mix, and enough harmonics in the source 

 PZ SVF seems inactive 
 Open the editor and load or draw a non-flat response 

 Upper notes become much quieter 
 Key tracking, cutoff range, and the actual notes in the phrase 

 The bass loses weight 
 High-pass or notch position, resonance, dry/wet interaction, and sub routing 

 One setting suddenly gets loud 
 Resonance, Drive, feedback controls, and output Level 

 Modulation jumps into an unusable sound 
 Reduce depth and constrain the range around a useful base setting 

 It sounds wide alone but weak in mono 
 Stereo cutoff offset, unison, dry/wet blend, and how layers combine 

 A demonstration sounds different from your patch 
 Compare source waveform, octave, routing, envelope, Mix, and any delay or second filter 

### Which Serum 2 filter should I learn first?

 Start with Low or MG Low, then learn Cutoff, Resonance, an envelope, and key tracking. After that, choose one contrasting model—Notch for movement, Formant for vowels, or Diffusor for attack texture—and build a complete sound with it.

### Do I need Serum 2 for every technique here?

 Many basic filtering and modulation ideas also apply to Serum 1 and other synths. The newer filter models and the dual-filter interface shown here require Serum 2. Match the guide to the version you’re actually using.

### Is a filter better than an EQ or an effect?

 Choose by the job. A synth filter can be part of how each note develops; an EQ may be useful for balancing the resulting sound in a mix. Some Serum filter models also create effects-like textures. There’s no need to force one tool to handle every stage.

### Where should I go next?

 Pick one sound from this guide and put it in a track. If you work in Live, our Ableton Workflow Guide helps take an idea into an arrangement. For deeper Serum study, use the official manual alongside the Serum 2 beginner’s guide .

 Master Serum 2

### Make the whole synth work together.
 Take the next step with structured Serum 2 lessons covering sound sources, modulation, routing, and complete patches.
 Explore the course ↗ 

 Source and version notes: Adapted from EDMProd’s linked Serum 2 filter demonstration. Technical checks against Xfer’s Serum 2 User Guide, “Using the Filter Modules,” completed September 10, 2026. Control labels and available models may differ across builds. The source video’s old course-launch announcement has been replaced with current course links. 

#### 
 Sam Matla 

 I'm the founder of EDMProd and co-author of EDM Foundations . Also write over at sammatla.com . Drop me a line on Twitter and follow me on Instagram @sammatla. 

## Produce music you're proud of

 Online courses & tools for electronic music producers. Skip years of trial & error, finish more tracks, and master core skills from sound design to songwriting.

 Trusted by 20,000+ producers 
 
 ★ 
 ★ 
 ★ 
 ★ 
 
 ★ 
 ★ 

 Explore Products

## HEY! WANT A FREE GUIDE ON MAKING ELECTRONIC MUSIC? 👇

 Enter your email below and get the guide (read by over 50,000 producers) along with two bonus resources. 

 DOWNLOAD 

 We’ll also send you awesome electronic music production tips (that you can unsubscribe from at any time). We do not sell or share your information.

## Get instant access to our free video training

 Learn how to master the fundamentals of electronic music production with the best roadmap for new producers

 Email 

 Yes, give me the free video training