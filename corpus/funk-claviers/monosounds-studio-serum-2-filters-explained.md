---
titre: "monosounds.studio — serum 2 filters explained"
source: https://monosounds.studio/serum-2-filters-explained/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: synth funk historique
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Serum 2 Filters Explained: Types, Routing, Best Picks 

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

 Most of my presets live or die in the Serum 2 filters. Not in the wavetable. Not in the effects chain. In which filter type I picked and how I routed it.

 I’ve built Serum packs at Monosounds since 2022, and the March 2025 Serum 2 update roughly doubled how useful the filter menu is. Two filter slots where there used to be one. Eleven new types, among them analog-style emulations that genuinely saturate like hardware. Routing per oscillator.

 It’s also a lot of menu to dig through at 2 a.m. So this is the map I could have used back then: what each category actually sounds like, how the dual routing works, and the exact filters I reach for on acid bass, smooth pads, and vocal-ish formant leads.

## What Changed in the Filter Section

 One filter. That was Serum 1’s entire offer. Needed a high pass behind your low pass? Off to the FX chain to burn the single filter slot there.

 Serum 2 hands you two filter slots running serial or parallel, and any of the three oscillators can go to filter 1, filter 2, both, or neither. Honestly, that routing changed my bass patches more than any of the new filter types did.

 The controls themselves feel familiar: cutoff, resonance, drive, mix. All of it accepts drag-and-drop modulation, like everywhere else in the synth. Still hazy on modulation routing? The whole system gets unpacked in my Serum 2 modulation guide .

## Serum 2 Filters by Category

 The menu doesn’t group them quite this way, but three years of preset work later, this is the mental model I actually use for the serum 2 filters:

 Clean digital filters. Low, high, band, peak and notch flavors at 6, 12, 18 and 24 dB per octave. Surgical, colorless. Perfect when the oscillator is meant to carry the sound.

 Multi filters. Morphing types that travel from low pass through band pass to high pass on a single knob. Drop one LFO on that morph and you get motion no static filter can produce.

 Analog-style emulations. The headline act of the update. They saturate, and their resonance goes nonlinear the way a hardware ladder filter does. More below.

 Formant filters. Vowel shapes. Quickest path to talky leads and vocal-ish textures.

 Comb, flange and phase filters. Resonator land. Metallic, hollow, pitched artifacts. Use sparingly.

 The weird bin. Ring mod, sample-and-hold flavors, downsampling types. Twice a year you’ll need one, and both times it’ll rescue the patch.

## The New Analog-Style Filters

 Serum 1’s filters were famously clean, which was exactly the complaint: turn up resonance on a digital 24 dB low pass and the low end goes thin while the resonant peak gets nasty.

 Those 11 new types in Serum 2 exist to fix precisely that. Crank resonance and the bottom stays fat. Crank drive and the filter itself starts distorting rather than merely getting louder. Cutoff and drive talk to each other, so identical knob positions sound different depending on input level. That’s the hardware behavior people used to stack third-party plugins to imitate.

 My standard test for a new filter: identical patch, identical cutoff, A/B a clean Low 24 against an analog-style type. On a saw bass with 40% resonance, the clean filter comes off like a demo and the analog one comes off like a record. The gap is not subtle.

 The honest downside: they burn more CPU than the clean types. Not brutally, but you notice once big unison enters the picture. Workarounds are at the end.

## Dual Filter Routing: Serial vs Parallel

 Serial runs filter 1 into filter 2. That’s my choice when one filter shapes the tone and the other tidies up afterwards. The classic version: formant filter feeding a low pass, keeping the vowel character while the fizzy top gets rounded off.

 Parallel splits the signal, sends it through both filters, then sums it back. Welcome to Reese and neuro territory: driven band pass on one branch, low pass on the other, and the phase interaction between them handles half your sound design.

 And then there’s per-oscillator assignment, quietly the best feature of the bunch. Oscillator A into filter 1, oscillator B into filter 2, and suddenly one preset contains a split-band bass. The sub stays pristine while the top layer gets filtered and driven. No second synth instance, no DAW bus routing.

 Worth knowing: the FX section carries filter modules too, and since Serum 2 runs multiple FX buses, each bus can be filtered on its own. Different job though — that’s post-processing, not synthesis. When to use which is covered in the Serum 2 effects guide .

## Which Filter for Which Sound

 My cheat sheet. All of these come from presets I’ve actually shipped, and none of them are gospel. Push the numbers around until your track agrees.

 Sound 
 Filter pick 
 Starting settings 

 Acid bass 
 Analog ladder 24 dB 
 Res 65%, drive up, fast env on cutoff 

 Smooth pad 
 Clean Low 12 
 Res 10%, zero drive, slow LFO on cutoff 

 Formant vocal lead 
 Formant type 
 LFO or macro on vowel morph 

 Pluck 
 Clean Low 24 
 Env decay 250 ms, env amount 60% 

 Reese / neuro bass 
 Parallel LP + BP 
 Drive on the BP side only 

 Techno stab 
 Analog Low 12 
 Res 30%, drive 3 o’clock, short env 

 Metallic texture 
 Comb 
 Key tracking on, mix 40% 

### Acid Bass

 Forty years on, the 303 recipe is unchanged: a 24 dB ladder-style low pass, resonance high enough to sing (60 to 70%), and an envelope hammering the cutoff on each note. In Serum 2 that means grabbing one of the analog ladder types and adding drive, because the filter distortion is the line between acid and a merely squelchy saw.

 Envelope decay somewhere from 120 to 200 ms depending on tempo, envelope amount near 50%, and resonance on a macro so you can ride it live. Most acid patches in our Technocraft techno collection follow this exact build, so open one up if you’d like to see the routing in the wild.

### Smooth Pads

 Pads are the sound people over-filter. No resonance needed, no drive needed. What you want is a gentle 12 dB slope that lets harmonics fade away rather than getting lopped off.

 My default setup: clean Low 12, cutoff sitting around 800 Hz to 1.5 kHz, resonance below 15%, and a slow LFO on cutoff at roughly 0.1 Hz, or a synced 8-bar rate at 120 BPM. You should feel the movement, not hear it. A pad that breathes audibly needs its LFO amount cut in half.

### Formant and Vocal Sounds

 Formant types imitate the resonances of a human mouth. The key move is modulating the vowel position, since a static vowel is just a band pass with an accent.

 Assign an LFO to the formant morph for talking rhythms, or park it on a macro and ride it through the drop. This is where serial routing earns its keep: formant filter first, then a clean low pass near 4 kHz to control the sibilant fizz these filters throw off up top.

### Bass for Club Genres

 In tech house and techno, the filter carries the groove: short envelope stabs, cutoff on key tracking so higher notes open naturally. There’s a complete patch walkthrough in my tech house bass guide for Serum 2 , plus a deeper preset roundup in the techno bass presets guide if starting from finished patches suits you better.

 Free reference material exists too: the 250+ patches in our free Serum 2 preset pack touch every category on this page, basses, pads and formant leads included. Load them and check which filter got picked and why.

## Keeping the CPU in Check

 Analog types plus 16-voice unison plus both filter slots will spike any laptop you own. My rules: unison from 3 to 7 handles nearly everything, oversampling stays at 2x rather than 4x while writing, and one analog-style filter per patch unless the sound truly earns a second.

 Still glitching? Xfer’s support page publishes official CPU guidelines, and freezing finished tracks costs nothing. The clean digital filters run noticeably lighter, so lean on them wherever the analog color isn’t the point.

## FAQ: Serum 2 Filters

### Are the Serum 1 filter types still in Serum 2?

 Yes. Serum 1 presets open in Serum 2 with filters intact, and every classic type remains in the menu. The 11 new types just sit next to them, so old patches stay identical until you choose to swap.

### What’s the difference between serial and parallel routing?

 Serial feeds filter 1 into filter 2, meaning the second filter works on an already-filtered signal. Parallel splits the signal, runs the filters side by side, and sums the results. Reach for serial when it’s shaping plus cleanup, parallel for split-band builds and phase interaction.

### Which Serum 2 filter is best for bass?

 Aggressive, driven bass wants one of the analog ladder types with the drive up. Clean sub-heavy bass wants the sub oscillator bypassing the filters completely, with only the top layer filtered. There is no single winner; how you route matters more than what you pick.

### Do the analog-style filters use more CPU?

 Yes, moderately so. On my machine an analog type runs about half again the cost of its clean equivalent. Trim unison before touching the filter though: going from 16 voices to 7 saves far more than any filter swap.

## Start From Patches, Not From Zero

 There’s a ceiling on what reading about filters can teach you. Reverse-engineering working presets and watching what the filter section does is the fastest way to make it stick.

 Want the shortcut? Take our 250+ free Serum 2 presets , no strings attached. Pull the patches apart, swap filter types around, and hear what each one really does to a sound you already like.

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

 Looking for the packs themselves? Here is the full Serum 2 preset catalogue — sorted by genre and by sound, with a demo on every one.
 From the Monosounds studio 
### Put this into practice with pro-grade sounds
 Serum 2 presets, sample packs and MIDI — royalty-free, mixed and ready for your next track.
 Browse all packs Start with the free pack 
 Keep reading 

 Sep 23, 2026 · 5 min Serum 2 Glide and Portamento: Mono, Legato, Porta, Always, Scaled 

 Sep 22, 2026 · 5 min Why Your Synth Sounds Thin (7 Fixes in Serum 2) 

 Sep 21, 2026 · 5 min FM Synthesis in Serum 2: How the FM Warp Mode Works (With Screenshots)