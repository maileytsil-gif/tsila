---
titre: "Monosounds — Serum 2 unison explained"
source: https://monosounds.studio/serum-2-unison-explained/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Serum 2 Unison Explained: Detune, Blend, Width, Stack, and Modes 

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

 Unison is the most used and least understood control in Serum 2. Everyone drags the number up to 7. Almost nobody opens the panel behind the gear button, and that is where the interesting settings live.

 This is a tour of all of it, with screenshots, plus the numbers I use for different kinds of sounds. I have spent a lot of hours measuring what these knobs really do while building preset packs, and some of it is not what the labels suggest.

## The Three Controls on the Front Panel

 Each oscillator has a UNISON field with a DETUNE knob and a BLEND knob next to it.

 OSC A with 7 voices. UNISON, DETUNE and BLEND are the three controls you see first. 
 UNISON is the voice count, from 1 to 16. Click and drag it, or double-click and type. The field changes color as the count climbs, which is a CPU warning. Every voice is a full oscillator.

 DETUNE spreads the voices apart in pitch. Low values chorus, high values smear. The scale is not linear. The first quarter of the knob covers the range most sounds use, and the top half is for effects.

 BLEND is the mix between the center voice and the detuned voices. At zero you only hear the center voice, so unison does nothing. At 100 the detuned voices are as loud as the center. I usually park it around 75 for leads and much lower for bass.

 Click the UNISON field and the wavetable display shows the voices as vertical lines spread across the width of the detune. It is the quickest way to understand what the detune knob is doing.

 Click the UNISON field and the display shows where the seven voices sit. 

## The Unison Panel

 Click the small gear button to the left of the voice count. The wavetable display is replaced by a panel with six more settings.

 The unison panel: MODE, STACK, WIDTH, RANGE, WT POS, and two WARP spreads. 
 MODE picks how the voices are spaced. Five options.

 Mode 
 What it does 
 Use it for 

 Linear 
 Even spacing between voices 
 Smooth, controlled thickness. My default. 

 Super 
 Denser cluster with more emphasis on power and a slight stereo spread 
 Supersaws, trance leads, anything that must feel huge 

 Exp 
 Spacing grows as voices move away from the center 
 Aggressive leads that need to cut 

 Inv 
 Lower voices detuned more than higher ones 
 Phasing effects, unusual textures 

 Random 
 Voices detuned unpredictably 
 Organic pads, tape-like drift 

 STACK transposes some of the voices instead of only detuning them. Off keeps everything at the same pitch. The 12 options spread voices across octaves, 12+7 adds fifths, and the Center options drop the center voices one or two octaves. Center-12 on a lead gives you a built-in sub layer with no second oscillator.

 WIDTH is the stereo spread of the voices. 100 is fully wide. Zero puts every voice in the center, which turns unison into a pure chorus with no stereo. This is the control to pull down on a bass.

 RANGE scales how far the detune knob can go. Think of it as the maximum spread that DETUNE at 100 percent reaches.

 WT POS gives each voice a different wavetable position. Even a small amount makes a stack of saws feel less like copies of each other.

 WARP 1 and WARP 2 do the same for the warp knobs. Combine a little WARP spread with a bend warp mode and the voices stop sounding cloned.

## Two Things the Labels Do Not Tell You

 Width is not blend. People turn BLEND down expecting the sound to get narrower. It gets quieter and more centered, but the remaining detuned voices are still spread. If you want narrow, the WIDTH control in the panel is the one.

 Unison is not level neutral. Serum 2 compensates for the volume increase as you add voices, but it is not perfect. In my measurements the output wanders by several dB between 1 and 16 voices, and not in a straight line. If you level-match a bank of presets and then change the voice count on one, re-check its level.

## Settings I Use

 Sound 
 Voices 
 Detune 
 Blend 
 Width 
 Mode 

 Sub bass 
 1 
 0 
 0 
 0 
 Off 

 Mid bass 
 3 
 8 to 12% 
 50 
 40 
 Linear 

 Lead 
 7 
 18 to 25% 
 75 
 100 
 Linear or Super 

 Supersaw 
 7 to 9 
 25 to 35% 
 85 
 100 
 Super 

 Pad 
 5 to 7 
 10 to 15% 
 70 
 100 
 Random 

 Pluck 
 1 to 3 
 5 to 10% 
 50 
 60 
 Linear 

 The bass rows are the ones people get wrong. Detuned voices below about 100 Hz cancel each other, and the result is a low end that changes level from note to note. Keep the sub at one voice. If the mid bass needs width, keep WIDTH modest and high-pass the wide part.

## Unison and CPU

 Voices are the biggest CPU cost in Serum 2. A patch with three oscillators at 7 voices and 8-note polyphony is 168 oscillators running at once. If a preset is heavy, this is the first place to look, before you blame the effects. The Serum 2 CPU guide has the rest of the checklist.

 Two cheap fixes: lower the POLY count in the VOICING panel, and drop unison on the oscillators that do not need it. The sub and any oscillator running an octave down rarely need more than one voice.

## Unison on the Other Engines

 Unison is not only for wavetables. The Sample, Multisample, Granular and Spectral engines all have the same UNISON, DETUNE and BLEND controls and the same panel behind the gear button. Unison on a sampled choir or string multisample is a quick way to get a section sound. Unison on the granular engine multiplies grains, which is why it can get expensive fast. I cover each engine in Serum 2 oscillator types .

 All of the leads and pads in the free Serum 2 preset pack use the settings from the table above, so you can open one and see the numbers in context. If you want more, the Serum 2 presets catalog is sorted by genre, and the bundles are the cheapest way to get a lot of them.

## FAQ

### What is the best unison setting in Serum 2?

 Seven voices, detune around 20 percent, blend around 75, for a lead. Serum’s own manual calls 7 the classic number. Bass and plucks want fewer voices, pads want lower detune.

### What does blend do in Serum 2 unison?

 Blend sets how loud the detuned voices are compared with the center voice. It changes the thickness of the sound, not its stereo width. Width is a separate control in the unison panel.

### How do I make unison wider in Serum 2?

 Open the unison panel with the gear button and raise WIDTH to 100. If it still feels narrow, add a little WT POS or WARP spread so the voices differ from each other.

### Why does unison make my bass sound weak?

 Detuned voices at low frequencies cancel each other and the fundamental drops. Use one voice on the sub, and keep detune under 12 percent and width low on any bass oscillator that has unison.

### Does unison use a lot of CPU?

 Yes. Every unison voice is a full oscillator. The UNISON field changes color as a warning. Reduce voices on oscillators that do not need them and lower the POLY count if the patch is heavy.

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

 From the Monosounds studio 
### Put this into practice with pro-grade sounds
 Serum 2 presets, sample packs and MIDI — royalty-free, mixed and ready for your next track.
 Browse all packs Start with the free pack 
 Keep reading 

 Sep 23, 2026 · 5 min Serum 2 Glide and Portamento: Mono, Legato, Porta, Always, Scaled 

 Sep 22, 2026 · 5 min Why Your Synth Sounds Thin (7 Fixes in Serum 2) 

 Sep 21, 2026 · 5 min FM Synthesis in Serum 2: How the FM Warp Mode Works (With Screenshots) 

## Leave a Reply Cancel Reply 
 Your email address will not be published. Required fields are marked * 
 
 Name  * 

 Email  * 

 Website 

 Add Comment  * 

 Type in the text displayed above 

 Post Comment