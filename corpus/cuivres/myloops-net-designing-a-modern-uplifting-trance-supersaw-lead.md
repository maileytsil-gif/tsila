---
titre: "Myloops — designing a modern uplifting trance supersaw lead"
source: https://www.myloops.net/designing-a-modern-uplifting-trance-supersaw-lead
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: cuivres électroniques modernes
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

How to Design a Modern Uplifting Trance Supersaw Lead That Cuts Through the Mix - Myloops 

 Home / Production Tips & Tutorials 
 Return to Previous Page 
 
# How to Design a Modern Uplifting Trance Supersaw Lead That Cuts Through the Mix 

 Your lead sounds enormous in solo. Then you unmute the kick, bass and pluck, and it shrinks into a smear behind the drums. That gap between “huge alone” and “huge in the mix” is what separates a bedroom supersaw from the leads Ferry Corsten, Bryan Kearney or Ruben de Ronde ride into a drop — and closing it has almost nothing to do with finding a better preset. It’s layering, restrained detune, and a bus chain that’s been carved around the kick and bass rather than on top of them.

 TL;DR 

 Two layers minimum: a wide, detuned saw stack for size, plus a narrower “core” saw that holds the melody’s pitch around 1–3 kHz.

 Detune less than feels right in solo. Over-detuned supersaws lose their fundamental the moment a bassline joins them.

 High-pass at 250–300 Hz and cut the 300–500 Hz honk zone before you even think about boosting anything.

 Reverb and delay live on returns with their own EQ and kick-triggered sidechain, not on the lead’s insert chain.

 Duck the lead itself into the kick — gently, 2–3 dB — for headroom without an audible pump.

## Build the stack, forget the preset browser 

 Open Serum, Sylenth1, Diva or Vital and start on an init patch. A single 7-voice supersaw with detune slammed to the top is the beginner move — fat in isolation, undefined mush in context. What you want is a small internal stack inside one patch, before you even think about layering a second synth on top.

 In Serum, set Osc A to a saw, unison to 7 voices, detune around 0.25–0.30, and unison blend around 0.8. Enable Osc B, same saw, unison 3 voices, detune ~0.15, and tune it down one octave. Drop Osc B about 6 dB below Osc A. The top oscillator gives you air and spread; the octave-down layer anchors the pitch when the top spreads out and stops the whole thing from floating away.

 Under Osc A’s unison, push the phase randomisation (“Rand”) to full so each retriggered note doesn’t start with an identical comb-filter zap on the transient. In Sylenth1 this is handled internally, but if you’re stacking two Sylenth instances, use different unison voice counts (say 7 and 5) so their interference patterns don’t lock together.

 Add a sub — Serum’s Sub Osc, or a third saw at -12 with no unison — at a level you can barely hear. Most of it will be high-passed out later, but its harmonic series keeps the lead feeling like a real instrument instead of a chorused pad.

 Amp envelope: attack 2–5 ms, no decay, full sustain, release ~200 ms. Uplifting leads have to bite instantly; any softness on the attack and 16th-note gate patterns turn to porridge. Skip the filter — leave it wide open, or set a gentle low-pass around 15 kHz just to shave the top harmonics. Tone is coming from EQ and saturation on the bus, not from the synth.

## The detune trap 

 Nothing wrecks a supersaw lead faster than too much detune. Push Serum’s unison detune past ~0.4, or Sylenth1’s past halfway, and the patch will sound enormous soloed and then vanish under the bassline, because there’s no clear fundamental left for the ear to lock onto.

 Modern uplifting leads live in a narrower zone than you’d expect: Serum unison detune around 0.20–0.30, Sylenth1 detune around 4.5–5.5 on its 0–10 slider. If the sound feels “not quite fat enough” in solo, you’re probably exactly right — width is going to arrive later from a second layer, stereo saturation and reverb.

 The test that matters: play the lead over the drop’s kick and bass. If you can still hum the melody back, the detune is where it should be. If it sounds like a slowly-modulating chord where you can’t identify individual notes, pull it down.

## Two layers, two jobs 

 No single patch — however well programmed — will sound like a modern festival lead. You need two layers doing genuinely different jobs, not two variations of the same thing.

 Layer 1, the wide layer: the stack you just built. Its territory is the upper mids and highs. This is what listeners feel .

 Layer 2, the core layer: radically simpler. One saw, 3-voice unison, minimal detune (Serum ~0.10, Sylenth1 ~3), no octave stacking, narrow stereo image. Its job is a clearly pitched 1–3 kHz centre that punches through the kick and bass. This is what listeners hear as the melody.

 Route both to a group. Sit the wide layer 3–6 dB below the core — yes, below. Get this balance wrong and the tune becomes a wash of pretty width with no discernible melody.

## Reference: settings that get you 80% there 

 Element Wide Layer Core Layer Notes 
 Waveform Saw Saw Saws are the sound. Don’t overthink it. 
 Unison voices 7 3 More voices = more smear. 
 Detune Serum ~0.25 / Sylenth ~5 Serum ~0.10 / Sylenth ~3 Set by ear over the mix, not in solo. 
 Octaves Osc A + Osc B at -12 Single octave Sub-octave anchors the pitch. 
 Stereo width Wide (unison blend ~0.8) Narrow (~0.2) Contrast is the point. 
 Amp attack 2–5 ms 2–5 ms Fast, or gates lose bite. 
 Level relative to core -3 to -6 dB below Reference Core carries the tune. 
 High-pass 250–300 Hz ~200 Hz Vacate the bass region. 

## EQ: three cuts before any boost 

 Put a clean digital EQ (Pro-Q 3, Bitwig EQ+, TDR Nova) on the lead group. Three subtractive moves come first, and if the sound isn’t already close to finished after them, the problem is the patch, not the EQ.

 1. High-pass around 280 Hz, 24 dB/oct. Nothing useful lives below the third harmonic of your highest bass note. Everything under that is just fighting the kick tail and the reese.

 2. Narrow bell cut in the 300–500 Hz honk zone. Supersaws pile up here badly. Sweep a narrow +6 dB boost, find the ugliest resonance, then flip it into a 3–5 dB cut with a Q around 2. This single move opens more space than any boost ever will.

 3. Gentle wide dip at 2–4 kHz. Detuned saws stack harshly right in the ear-fatigue band. A -2 to -3 dB dip around 3 kHz with a wide Q keeps the sound listenable at drop volume. If you need air on top, add a small +1–2 dB shelf at 10 kHz — never boost 5–8 kHz to make the lead “cut,” because that band belongs to hats and crashes and boosting it turns the mix to broken glass.

 Browse Uplifting Trance packs at Myloops → 

## Saturation is the glue 

 A well-EQ’d stack still sounds sterile. Saturation is what fuses two layers into one instrument and gives the lead the perceived loudness that makes it feel like it’s leaning into the speakers.

 After the subtractive EQ, insert something tape or tube-flavoured — Saturn 2, Softube Saturation Knob, Ableton’s Saturator on Analog Clip, Kilohearts Faturator. Avoid fuzz and bitcrush; you want harmonics, not distortion character. Push it until a spectrum analyser shows a couple of dB of new content above 5 kHz, then pull back a hair. Your ears will tell you before the meter does: as soon as the top starts to hiss rather than sing, you’re too far.

 For richer harmonic content without brittleness, split the saturation in parallel. Send the lead group to a return, hit that return with heavy saturation and a low-pass around 6 kHz, and blend it in around -9 to -12 dB under the dry group. You get warmth and glue without the top-end fizz.

 Follow the saturator with a soft clipper — KClip, StandardClip, or the soft-clip button on Ableton’s utility — catching just the peaks that would otherwise force you to pull the whole lead down. Aim to shave 2–3 dB off the loudest transients. Any more and you’re squashing musicality out of the gates.

## Reverb on a return, not the insert 

 Reverb on the lead’s insert chain is the shortcut to a 2004-sounding record (and not in the good way). It has to live on a return where you can EQ, sidechain and automate it independently.

 Load a plate or hall on a stereo aux — Valhalla VintageVerb’s Concert Hall or a bright plate is the reliable choice — with decay between 2.5 and 4 seconds and pre-delay of 20–40 ms so the dry lead speaks first. On the return, high-pass at 400–500 Hz (reverb below there is pure mud) and low-pass around 8–10 kHz so the tail doesn’t compete with hats and cymbals.

 Then the important move: put a compressor on the return, sidechained to the kick, ratio around 4:1, fast attack, release opening back up over 300–400 ms. The reverb ducks out of the kick’s way, then blooms between hits. Without this, your tails smear across every downbeat and eat all the low-mid clarity you fought for with EQ.

 Send level around -12 to -18 dB from the lead group. Tails audible, dry lead unmistakably in front.

## Delay: one, tempo-synced, muffled 

 One delay. On a return. Synced to 1/4 dotted or 1/8 dotted. Ping-pong or stereo. Feedback 30–40% so it dies out over three or four repeats. Anything more elaborate and the delay stops being an effect and starts being a second arrangement.

 On the return, high-pass harder than the reverb — 600–800 Hz — and low-pass around 6 kHz. Muffled delays sit further back, which is what you want; a bright delay competes with the dry lead for attention.

 Sidechain this return to the kick as well. Otherwise the delay taps drop straight onto kick hits and undo all the space you built with the high-pass.

 Automate the send. Trance leads breathe when delay comes in on the long notes and drops out during 16th-note gating. A static send level is a dead giveaway that the mix hasn’t been finished.

## Sidechain the lead itself — quietly 

 Even after a clean high-pass, the lead’s low harmonics still bump the kick’s punch region around 100–150 Hz. Put a compressor or LFOTool on the lead group, sidechained to the kick, but nowhere near as aggressive as you’d duck a bass.

 Target 2–3 dB of gain reduction per kick. Compressor: ratio 4:1, attack ~1 ms, release 150–200 ms so it’s fully open before the next hit. If you’re using LFOTool or Kickstart, choose a soft curve that only pulls the level down 20–30% at its deepest point rather than the full-duck shape you’d use on a bass.

 Done right, the lead never audibly pumps — but you get 2–3 dB of extra headroom to spend on loudness, and the kick’s transient stays sharp instead of getting swallowed by the sustained saw wall.

## Perform the MIDI 

 A supersaw played as flat quarter notes is dead on arrival. Uplifting leads live and die by rhythmic gating and expression, and this is the part almost nobody spends enough time on.

 Program in 16ths, but vary note lengths — some staccato at 30–50% gate, some held across two or three steps. This is the “chopped” feel that defines the genre.

 Add small pitch scoops on key phrase notes: a downward bend of a semitone or two, resolving over ~60 ms into the target pitch. Use the pitch wheel or automate osc coarse; either works.

 Vary velocity between roughly 90 and 127 and route it to filter cutoff or amp level with a modest amount. A 2 dB velocity swing per note is the difference between “programmed” and “played”.

 Nudge note lengths across repeated phrases. An 8-bar hook repeated four times should never be four identical copies — subtle gate-length changes each pass keep the ear engaged.

 If you’re starting from a sample-pack MIDI, don’t just drop it in and print. Spend fifteen minutes humanising gate lengths and velocities. It’s the cheapest upgrade in the entire chain.

 Browse Uplifting Trance packs at Myloops → 

## The bottom line 

 A modern uplifting trance lead isn’t a patch — it’s a system. Conservative supersaw stack, narrower core layer stacked beneath it, a bus with carving EQ and glue saturation, reverb and delay on their own kick-ducked returns, and a MIDI performance that actually breathes. Miss any one of those and you get a lead that’s fine in solo and gone in the mix.

 The core mistake almost every producer makes is treating the lead as a solo instrument. It isn’t. It’s the top voice in an arrangement that already contains a kick, a bass, a pluck and a pad, and its job is to sit above all of them without stepping on any. Which means fewer solo-listening decisions, less detune, more subtractive EQ, and every effect decision made with the drop playing.

 Build one lead this way — from scratch, no preset — and save the whole chain as a template: the two-layer group, the pre-carved EQ, the sidechained reverb and delay returns, the gentle kick-duck on the group. Every future track starts from that skeleton. From there you’re only writing melodies and tuning decay times.

### Related posts 
 More details 

###### Production Tips & Tutorials 

### Compression for Trance: A Full Signal-Chain Guide from Kick to Master 
 
 September 24, 2026 at 9:42 am by Jonathan B. / 0 

 Stage-by-stage compression settings for trance kicks, bass, leads, pads and the master bus — with attack, release and ratio starting points that work.

 More details 

###### Production Tips & Tutorials 

### Reverb and Delay Techniques for Emotional Trance That Actually Work 
 
 September 23, 2026 at 9:13 am by Jonathan B. / 0 

 Pre-delay, ducked returns, delay throws and send automation — the reverb and delay techniques that make emotional trance breakdowns actually hit.

 More details 

###### Production Tips & Tutorials 

### Mastering Uplifting Trance: A Loudness Chain That Keeps the Supersaw Alive 
 
 September 20, 2026 at 9:35 am by Jonathan B. / 0 

 A step-by-step mastering chain for uplifting trance that hits club loudness without smashing the supersaw, kick punch, or breakdown dynamics.

 More details 

###### Production Tips & Tutorials 

### Trance EQ: Cutting Mud From Leads, Pads and Basslines Without Killing the Vibe 
 
 September 18, 2026 at 11:53 am by Jonathan B. / 0 

 Practical EQ moves for trance leads, pads and basslines — where to cut, where to boost, and how to keep the low end tight and the top alive.

 More details 

###### Production Tips & Tutorials 

### Sidechain Compression for Trance: 9 Techniques That Make the Kick Breathe 
 
 September 15, 2026 at 7:22 am by Jonathan B. / 0 

 Nine sidechain compression techniques for trance, from ghost-kick triggers and split sub/mid bass ducking to reverb returns and breakdown automation.

### Leave a reply Cancel reply 
 Comment 
 I have read and accept the Privacy Policy Name * 

 Email * 

 Website 

 Table of Contents

 🎁 
 
### Download 12 Free Packs – 5GB + 9 Genres

 Trance · Techno · Progressive · Psy · Melodic · EDM...

 Used by 30,000+ producers · No spam · Unsubscribe anytime

 © 2026 Myloops – All Rights Reserved · Terms & Conditions · Privacy Policy 

 SSL secured payments · Instant download · 24 hour support 

### Search engine

 Use this form to find things you need on this site 

 Search 

 × 
 
### Login 

 Username or email * 

 Password * 

 Lost Password? 
 Create Account 

### Cart 

 We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept”, you consent to the use of ALL the cookies.
 Cookie settings ACCEPT 

 Manage consent 

 Close 

#### Privacy Overview
 
 This website uses cookies to improve your experience while you navigate through the website. Out of these, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may affect your browsing experience.

 Necessary 

 Necessary 

 Always Enabled 

 Necessary cookies are absolutely essential for the website to function properly. These cookies ensure basic functionalities and security features of the website, anonymously.
 Cookie Duration Description 
 cookielawinfo-checbox-analytics 11 months This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Analytics". 
 cookielawinfo-checbox-functional 11 months The cookie is set by GDPR cookie consent to record the user consent for the cookies in the category "Functional". 
 cookielawinfo-checbox-others 11 months This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Other. 
 cookielawinfo-checkbox-necessary 11 months This cookie is set by GDPR Cookie Consent plugin. The cookies is used to store the user consent for the cookies in the category "Necessary". 
 cookielawinfo-checkbox-performance 11 months This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Performance". 
 viewed_cookie_policy 11 months The cookie is set by the GDPR Cookie Consent plugin and is used to store whether or not user has consented to the use of cookies. It does not store any personal data. 

 Functional 

 Functional 

 Functional cookies help to perform certain functionalities like sharing the content of the website on social media platforms, collect feedbacks, and other third-party features.

 Performance 

 Performance 

 Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors.

 Analytics 

 Analytics 

 Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics the number of visitors, bounce rate, traffic source, etc.

 Advertisement 

 Advertisement 

 Advertisement cookies are used to provide visitors with relevant ads and marketing campaigns. These cookies track visitors across websites and collect information to provide customized ads.

 Others 

 Others 

 Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.

 SAVE & ACCEPT 

 🔥 Flash Sale! 70% Off Senses Trance Soundbank 🔥

 Shop Now 

 X 

 close