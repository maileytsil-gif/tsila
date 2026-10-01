---
titre: "Monosounds — serum 2 supersaw"
source: https://monosounds.studio/serum-2-supersaw/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: cuivres électroniques modernes
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Serum 2 Supersaw Guide: Make It Huge, Not Cheap 

 Skip to content 

 No results 

 Login 

 Sign Up 

 Username or Email Address 

 Password 

 Type in the text displayed above 

 Remember Me 

 Forgot Password? 

 Log In

 Email 

 A link to set a new password will be sent to your email address. 

 Website 

 Your personal data will be used to process your orders, facilitate your experience on the site and for other purposes described in our privacy policy .

 Register

 Username or Email Address 

 Get New Password

 ← Back to login 

 Free download 250+ Serum 2 Presets — Free Pack Bass, leads, keys, 808s, pads and more. Royalty-free, no strings attached. Download Free Pack → 

 At least once a month somebody sends me a “massive” lead that actually sounds like a wasp trapped in a tin can. Thin, fizzy, all sparkle up top and nothing in the chest. Here’s the truth of it: getting a serum 2 supersaw to sound expensive has basically nothing to do with finding a secret wavetable. It comes down to five or six small balance calls that most people make backwards.

 Monosounds has shipped Serum preset packs since 2022, and supersaws remain the patch type customers wreck most often when they start tweaking. The story never changes: detune maxed, blend maxed, width maxed, then a compressor brought in to glue the debris back together.

 So this is the complete recipe. Actual numbers, actual settings, plus the two flavors people request most these days: future rave and eurodance.

## Why Most Supersaws Sound Thin

 Strip it down and a supersaw is nothing but detuned saw copies. The Roland JP-8000 pulled it off with seven voices back in 1996. That much is trivial.

 What everybody overlooks is how detune and blend relate. Detune decides how wide the unison voices fan out in pitch. Blend decides how loud those detuned voices sit against the center voice. Push both to the top and you’ve erased the center voice – and the center voice IS the note. Hence the thin sound: pure shimmer, no fundamental, a fog of pitch where a chord should be.

 Where I start: detune from 0.10 to 0.15, blend near 75%. Blend at 100% leaves no anchor pitch at all. Detune at 0.30 turns your “chord” into nine chords at war with each other.

 Also, drop the unison 16 myth. Beyond seven voices you’re buying CPU load, not size. Serum 2 already runs heavier than Serum 1 on certain patches, so put voices only where they earn their keep.

## The Serum 2 Supersaw Recipe: Two Oscillators, One Octave Apart

 A single oscillator will never sound big, whatever you throw at it. Every serum 2 supersaw I put out rests on two saws spaced an octave apart, occasionally three.

 Begin from a fresh init patch so leftover FX can’t lie to you. Then:

 Oscillator A is the body. Basic Shapes wavetable, saw frame. Unison 7, detune 0.12, blend 75%, width near 80. The chord rides on this layer.

 Oscillator B is the weight. Same saw, dropped an octave (Oct -1). Unison 5, detune 0.08, width 55. Bring its level down until it tucks roughly two thirds beneath Osc A. Hearing Osc B as its own separate note means it’s too loud – the effect should be Osc A growing a chest.

 Oscillator C is optional shimmer. Serum 2 hands you a third oscillator, so make it a +12 layer: unison 5, detune 0.10, width 95, then slam a high-pass on it around 2 kHz. Automate it in for drops only.

 A quick word on CPU: three unison oscillators stack up quickly. Unison 5-7 rather than 16, reasonable polyphony, and 2x oversampling keep most supersaw patches comfortable even under big chords.

## Stereo Width Without Phase Mush

 Width is the graveyard of cheap supersaws. The problem was never width as such – it’s identical width on every layer, with three widening effects piled on for good measure.

 Each layer deserves its own lane. Keep the low octave narrower (width 50-60) so the middle of the mix stays planted. The main layer lives around 75-85. Only the high shimmer earns 95-100. Focused lows under wide highs read as “produced”. Wide everything reads as phase soup.

 Then choose one widener in the FX chain. One. Chorus, or the Dimension-style expander, or a wide reverb – never the whole set. Serum 2’s multiple FX buses keep this tidy: reverb and any widening go on their own bus at my desk, leaving the dry stack punchy underneath. The full routing is broken down in our Serum 2 effects guide .

 Final step, without exception: flip to mono and listen. A 6 dB drop or a smeared chord means your unison width and chorus are cancelling each other out. Narrow the low layers first – nine times out of ten that’s the cure.

## High-Pass the Stack, Layer a Real Sub

 Detuned unison saws are hopeless at low end. Below 150 Hz the spread voices beat against one another and produce wobble instead of weight. So stop asking the stack to do that job at all.

 Run a high-pass over the whole supersaw around 100-150 Hz, 12 or 24 dB per octave. Soloed, yes, it shrinks. In the mix it doubles in size, because the kick and bass now own the bottom rather than fighting unison mud for it.

 Then restore the weight the right way: a dedicated sub layer. Sine or triangle, mono, unison 1, zero detune, playing nothing but the root. A serum 2 supersaw should rule from 150 Hz upward; everything beneath belongs to the sub. Sidechain the pair to the kick and suddenly the drop sounds like a record.

 Prefer to reverse-engineer rather than build? Our free 250+ Serum 2 presets contain finished supersaw leads with matching subs and 808s – load them side by side and inspect the filter and unison settings.

## EQ Notches That Remove the Cheap

 Raw saw stacks dump energy into extremely predictable places. Removing those spots is what buys the expensive sound – not boosting the top.

 My standard notches, all broad and gentle: 2-3 dB gone around 500 Hz (boxiness), 2 dB around 1.5 kHz (honk), 2-3 dB around 3.5 kHz (the harsh ear-poking region). Fizzy top end after that? Shelve down 1-2 dB above 12 kHz rather than chasing individual peaks.

 Cut before you judge. Still dull once the notches are in? Then a modest high shelf up at 10 kHz is fair game. For the complete frequency map behind this, we published our whole EQ blueprint with charts and key frequencies .

## Future Rave and Eurodance Flavors

 One skeleton, wildly different outfits. Here’s how the serum 2 supersaw stack gets re-dressed for the styles I’m asked about most.

 Flavor 
 Core settings 
 Character moves 

 Future rave 
 Unison 5, detune 0.09, LP filter swept 400-900 Hz 
 Dark mids, filter carries the energy, light OTT 

 Eurodance 
 Unison 7, detune 0.14, filter open, fast attack 
 Octave stabs, pitch bend into phrases, bright top 

 Big room / anthem 
 Unison 7 on both saws, detune 0.12, wide +12 layer 
 Long reverb on its own FX bus, huge sidechain 

 Future bass chords 
 Unison 5, detune 0.10, OTT after the stack 
 7th and 9th voicings, LFO on wavetable position 

 Future rave is really a supersaw disguised as a bass. Keep the tone darker: park the low-pass around 600 Hz as home base, then push the cutoff around with an envelope or hand automation until the filter movement is the hook. Less width, more mono punch. Our Modern Future Rave presets follow this template exactly, macros pre-mapped, if you want the finished article.

 Eurodance runs the opposite direction: bright, quick, zero apology. Detune pushed higher (0.14+), filter fully open, amp release short so stabs stay tight at 140-150 BPM, plus the classic pitch bend rising from an octave below into each phrase. That entire sound went into our Eurodance presets for Serum 2 .

 For festival EDM leads sitting between those poles – big, clean, melodic – the Arcadia EDM pack is the reference. And if the softer chord take on this is what you’re after, the same stack with OTT and 9th chords is essentially future bass; that gets a walkthrough in the future bass Serum 2 tutorial .

## Serum 2 Supersaw FAQ

### How many unison voices does a supersaw need?

 Seven per oscillator hits the sweet spot – literally the JP-8000 number. Five does the job when several oscillators are stacked. Sixteen only torches CPU; run a blind test against 7 and hearing the difference inside a mix gets very hard.

### Why does my supersaw disappear in mono?

 Too much width spread across too many places. Voices detuned and panned hard left-right partially cancel when the channels sum. Pull the low octave in to width 50-60, ditch one of the stacked wideners, and hold blend at 75% so the center voice survives the fold-down.

### Can I make supersaws in Serum 1 or Vital instead?

 Yes – the underlying unison math doesn’t change, and Vital’s free tier handles it. That said, Serum 2’s separate FX buses and third oscillator make the wide-top-narrow-bottom routing far easier to pull off. And given that Serum 2 is a free upgrade for Serum 1 owners , staying behind buys you nothing.

### My settings match yours but it still sounds cheap. What now?

 Then the patch probably isn’t the problem. Weak chord voicings, a missing sub layer, or wideners stacked on wideners are the usual culprits – the common ones are collected in Serum 2 beginner mistakes . Start with the voicing: spread the chord across two octaves and the very same patch grows up on the spot.

## Steal the Finished Versions

 All of the above takes maybe twenty minutes once you’ve built it twice. Prefer starting from patches that already work? Grab our free 250+ Serum 2 presets – leads, subs, chords and beyond, royalty-free, no catch. Rip the supersaws open, compare the unison and EQ moves against this article, then bend them into something that’s yours.

 Free forever 

 Ear training · 500 levels 

## Hear the problem before you reach for a plugin.

 A listening game built on our own packs. Guess the boosted band, catch the compression, place the reverb — ten levels in you already hear things you were eyeballing before.

 EQ

 Compression

 Reverb

 Stereo

 Gear quiz

 Start training → No card, no subscription · first 10 levels without an account 

 LEVEL 12 · EQ A / B ? 200 Hz 900 Hz 3 kHz 8 kHz 

 Maxim Hetman Founder, Monosounds.studio I run Monosounds.studio and make the packs myself. Ten-plus years of producing, 97+ releases, 16,000+ downloads. Every Serum 2 preset we ship passes a CPU check on a mid-range laptop and gets used in a real track before release. If it does not survive a mix, it does not go in the pack.
 More about Maxim & the studio → 

 Looking for the packs themselves? Here is all my Serum 2 preset packs — sorted by genre and by sound, with a demo on every one.
 From the Monosounds studio 
### Put this into practice with pro-grade sounds
 Serum 2 presets, sample packs and MIDI — royalty-free, mixed and ready for your next track.
 Browse all packs Start with the free pack 
 Keep reading 

 Sep 23, 2026 · 5 min Serum 2 Glide and Portamento: Mono, Legato, Porta, Always, Scaled 

 Sep 22, 2026 · 5 min Why Your Synth Sounds Thin (7 Fixes in Serum 2) 

 Sep 21, 2026 · 5 min FM Synthesis in Serum 2: How the FM Warp Mode Works (With Screenshots)