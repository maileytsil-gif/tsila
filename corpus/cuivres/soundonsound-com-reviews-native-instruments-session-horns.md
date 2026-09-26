---
titre: "Sound On Sound — test NI Session Horns"
source: https://www.soundonsound.com/reviews/native-instruments-session-horns
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: écriture de section, MIDI réaliste, mixage des cuivres
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Native Instruments Session Horns 

 Skip to main content 

 Set us as a Google preferred source preferred 

 facebook 
 twitter 
 email 
 print 

## You are here
 Home 
 Reviews 

# Native Instruments Session Horns

 Virtual Brass Instrument 

 Sample Libraries 
 By Nick Magnus 
 
 Published March 2013 

 NI's Session Horns forsakes the cinematic to focus on a real-world brass section that's well suited to pop and rock music.

 If you need to virtually recreate large-scale orchestral and cinematic brass, you can pretty much pick and choose from a variety of sample libraries. Less well catered for, however, are small-scale brass ensembles suitable for pop and rock applications, where tight, finger-snapping cool and funkiness are more in keeping than Wagnerian bombast. Session Horns (SH), the third of Native Instruments' Kontakt library collaborations with Hamburg company e-instruments (their first two being Session Strings and its larger Pro sibling) aims to fit that niche. It's a 4.88GB library based around a four-piece brass section comprising a trombone, a tenor saxophone and two trumpets, the sort of line-up typically used in soul, funk, reggae, Latin and many other modern pop styles. 

 Sound-wise, if you're after a tight, bright, controlled brass section, SH's core samples provide the ideal raw material. Although recorded very dry, the sound is not entirely anechoic; there's just enough subtle room reflection to give a sense of the recording space. The overall tone is bright and zippy, suggesting close miking with an AKG 414 or something similar, although the mics used are not listed. Most of the high-frequency 'zip' comes from the trumpets and trombone, while the tenor sax provides an element of warmth. As you'd expect from NI, the 44.1kHz, 24-bit samples are very clean and well recorded.

## Brass Onesie 

 Rather than providing each section instrument as separate NKI (Native Kontakt Instrument) patches, the SH patch library consists of just two Kontakt NKIs: Performance and Single Articulation. The Performance patch is the most memory intensive, with all articulations for all four instruments loaded into this single patch. It's up to the user to select which instruments will sound, and how the notes played are distributed amongst them. To this end, SH features a number of playing modes and arrangement tools for achieving this in a live performance. The majority of performance options are found on the Main screen tab, so we'll begin our tour here.

 The Performance Patch main tab, showing the Animator's control panel. Section Setup, velocity switched articulation, Voicing Assistant modes and Octave Drop options are all selected from here. 

 The Performance patch's default setting is the full four-piece section, in polyphonic mode, i.e. all notes played will each sound all four instruments playing a sustained articulation in unison. This has four velocity-switched dynamic layers, the highest layer being a forte/piano/crescendo articulation, 'FoPiCre', a strongly accented note that subsides very quickly and swells back to a zippy crescendo. This can also be effective for playing very short, accented notes. When held a fraction longer and released just before the crescendo begins, it provides a natural-sounding timbral decay for non-marcato short notes. A number of alternative highest-velocity articulations are selectable from a drop-down menu, with a choice of rips (flurried slurs up to a sustained note); grace notes (short, semitone upward slurs); shakes (energetic, 'jazz hand' trills); staccatissimo (very short stabs); marcato (emphatic notes of around one beat in length); and 'FoPiCre Time', a variation of FoPiCre that syncs the sample length to the host DAW's tempo. These alternative articulations can be disabled, in which case the sustained articulation plays an additional double-forte sustained layer at the highest velocities. However, only one of the high-velocity articulations can be active at a time, since none of SH's drop-down menu choices can be selected via MIDI control. There are plenty of unused keys at the low end of the keyboard layout, so the decision not to make them selectable via keyswitches is an odd one. Doits and falls are also possible, but these are accessed by a different method, discussed later.

 If the full four-piece section is not required in your arrangement, the Section Setup menu offers all the practical combinations of two or three instruments, although, oddly, there's no 'solo' option for any instrument. This is a missed opportunity, as I discovered after diving 'under the hood' and doing a bit of tweaking. Editing the group volumes of one of the trumpets in the 'Tpt 1/Tpt 2' setup to zero revealed a beautifully soulful solo trumpet — which is especially expressive when dynamics are controlled by CC#11 instead of velocity. The mod wheel also adds just the right amount of tasteful vibrato. Perhaps a future update should include solo instruments amongst the setup options, particularly for those using the Kontakt Player, which doesn't allow patch editing.

## Voicing Assistant 

 A common problem with sampled instrument sections such as brass and strings is that each additional note of polyphony creates an artificial increase in 'players', which wouldn't happen in real life. Arranging for a four-piece section therefore requires splitting the polyphony between the individual instruments. In a traditional sampling scenario, this would involve loading separate patches for each solo instrument and building the arrangement one instrument part at a time. The Voicing Assistant in Session Horns, though, has a Smart Voice Split mode, designed to manage the assignment of parts between instruments for you. Play a four-note chord and SH automatically gives the lowest note to the trombone and the next up to the sax, while each of the two trumpets plays the highest two notes. A three-note chord assigns the highest note to both trumpets; a two-note chord assigns the top note to both trumpets and the bottom one to the trombone and sax, while single notes play all four instruments in unison. This system does work, although I found you have to be really careful to play cleanly and precisely. Sloppiness of timing or overlapping notes (amounting to a total of more than four) causes parts to be grabbed by the wrong instrument, resulting in unexpected inversions and jumping around the stereo field — especially with the trumpets, which are panned quite hard left and right. Alternating between chords and single notes is also best avoided, as the perceived volume of all four instruments in unison on a single note is greater than when playing chordally. Nevertheless, with careful part writing, sequencing and editing of note lengths, the results can be quite effective.

 Voicing Assistant provides additional playing modes: Legato renders SH monophonic, inserting naturalistic sampled note transitions between consecutive overlapped notes, creating a fluid effect that works well for melodic lines. The transition samples are at a fixed speed, so wide legato intervals played too quickly can give the impression that the players are unable to keep up!

 Chord + Legato mode fuses the standard polyphonic mode with legato, so once a chord is voiced, an additional legato line can be played on top. This mode can be fairly tricky to control, as the scripting often gets confused when distinguishing between what are meant to be internal chord movements and lines intended to be legato, so the timing and precise placement of notes is critical. Because of this mode's 'stacked unison' nature, economic two- or three-note chord voicings sound the most realistic.

 Further variations to the voicing are available via the Drop Voice feature. Specific instruments can be lowered by one octave: Drop 1st lowers the trombone, Drop 2nd lowers the sax, and Drop 3rd lowers trumpet 2, working from bottom to top. This works in all Voice Assistant modes and section setups, and helps to broaden the sound nicely. Drop 1st + Drop 2nd with the full section is particularly pleasing, with both the trombone and sax sounding an octave below the trumpets.

## Animatronics 

 The final Voicing Assistant mode is the Animator, an entirely different beast to the similarly named rhythmic arpeggiator of Session Strings. Occupying the lower half of the Performance GUI, this Animator is a phrase generator, offering 174 pre-programmed phrases sub-divided into five musical styles; RnB/Soul, Pop, Nu-Jazz/Funk, Latin and Reggae. Each musical style consists of a number of 'songs' of six phrases each; just select a style, then a song within that style, play a note within the playable range, and out pops a fully-formed phrase, complete with correct part voicings, internal dynamics and articulation changes, rooted to that note, and in sync with your host tempo. The six phrases that make up a song are selected via keyswitches C1–A1.

 Choose between controlling dynamics by key velocity or CC#11 on the Control tab panel, along with Pitch wheel options for doit/fall triggering, and Same Note Legato or momentary Animator switch functions for the sustain pedal. 

 Although the concept of pre-formed phrases might seem to limit its flexibility and long-term usefulness, Animator provides plenty of scope for customisation. At the simplest level, phrases can be retriggered before they finish, or they can be swapped in mid-run — so you could start with one, change to a second, finish with a third, and so on. Melodic variations can be made by changing notes in a legato fashion (so as not to retrigger the phrase from the beginning) while a phrase is running. Phrases can be triggered not only from single notes, but from chords too (it works rather like the auto-arranger facility found in home keyboards). For example, playing C+Eb revoices a C-major phrase to C-minor. If a major seventh is present in the phrase, playing C+Bb changes it to a flattened 7th.

 The manual makes no mention of which chord variations are possible, but so far I've discovered major, major/flat 7th, minor, minor 7th, diminished and minor 6th, depending, of course, on whether a phrase includes the appropriate notes to modify. Chord voicings can also be changed in mid-phrase, so already there are a lot of ways to customise phrases to fit your track. However, there are a handful of caveats among the chording rules which take a little getting used to. For example, the phrases E1-A1 in the song 'Uplift' in the Pop category play major 7th or minor 7th riffs, but without the root note in the phrase, so they appear to play in E-minor or Eb-major if you press a C or C+Eb. To have those phrases play in C-major, you have to add an A... yes, it's confusing if you're trying to remember that in the heat of a live gig!

 Rhythm Mode allows a more free-form approach, ignoring the programmed note pitches from the phrase sequences and playing only their rhythms and articulation changes. Any notes or chords played on the keyboard take on this rhythm, whilst the scripting attempts to takes care of the voicing automatically. I say attempts, because instruments don't necessarily follow the line you want them to, and tend to jump around unexpectedly, but the results can be perfectly usable.

 In normal use, phrases loop round for as long as keys are held down. With One Shot mode engaged, you only need to play a note or chord briefly and the current phrase plays once to the end, then stops. The usefulness of this becomes apparent when you discover that the Animator can be momentarily engaged via the sustain pedal from any of the other playing modes. So you can stomp on the pedal, trigger a phrase, release the pedal, and continue playing on top in the previous mode with both hands, while the phrase carries on playing to its end underneath. You can also do this without One Shot engaged, although you'd need to keep holding the phrased chord with one hand to keep it going.

 To add further spice, phrases that play 'straight' can be swung, and the timing between the instruments can be adjusted from robotically super-tight to woefully under-rehearsed. The default timing setting of 30 sounds very natural. There is also an option to double or halve the tempo relative to the host, to enable phrases to be useful over a wide tempo range.

 The last Animator parameter is Link Sound Preset. When this is engaged, each song calls up an instrument mix and set of Master effects specifically tailored to that song. When deactivated, the last selected Sound Preset remains, regardless of the selected song or style.

 The control panel for the Sound tab. Section Mix presets and Master FX Chain presets are selected here, and there are controls for detuning, stereo width and convolution reverb settings. 

## Sound Options Tab 
 The Sound Presets referred to above are combinations of Section Mix and Master FX, providing a number of ready-made 'production setups'. Section Mix offers 29 different instrument mix presets, while the Master FX section provides 35 presets garnered from Kontakt's arsenal of effects. These range from subtle EQ, delay and compression to not-so-subtle distortion and lo-fi treatments. While these treatments are intended to complement typical brass-section musical styles, and they do the job reasonably well, a little more freedom of choice might have been nice — how about a little mixer, for instance, to balance the four instruments exactly to personal taste? Similarly, an additional tab where the Master FX parameters could be adjusted would be useful; the pre-programmed delay levels may sound OK in isolation, but they tend to be swallowed up in the context of a full mix.
 The Detune parameter, as expected, introduces increasing amounts of random tuning incompetence with high settings. When it's used in conjunction with the Animator's Timing control at maximum, the fantasy of the Portsmouth Sinfonia forming a jazz funk ensemble comes one step closer to reality.
 The Reverb offers a wide choice of 28 convolution impulses, mostly concentrating on the kind of small to medium spaces and short ambiences that suit this type of brass ensemble well. Some larger spaces are included, as are a few sci-fi effects, for good measure. The section's stereo width can also be adjusted from super-wide to mono, though this has no effect on the Reverb effect, which remains in stereo.

## Control Options Tab 
 Dynamics are controlled either by key velocity or by MIDI Expression control (CC#11). Using the latter has two distinct advantages: naturalistic real-time control over the tone and volume of sustained notes, and full-time access (via CC#11) to that sustained double-forte layer that's otherwise hidden when a velocity switched articulation is active and the dynamics are under velocity control. The pitch wheel's three modes determine whether it functions as a traditional pitch-bend or as a trigger for the doit and fall articulations mentioned earlier. When triggering doits or falls, upward movement selects doits, while downward movement selects falls; the two triggering options are note-on and note release. The falls also have two speeds, depending on how far you move the pitch wheel downwards. Lastly, the sustain pedal can act either as a momentary Animator switch, or in Same Note Legato mode — to all intents, the 'normal' sustain pedal function, but in legato mode it allows for same-note note repetitions with the sustain pedal down, but without the polyphony piling up.

## The Single Articulation Patch 
 This patch, although simpler than the Performance patch, is intended for detailed sequencer composition where multiple articulations are required, each spread across multiple MIDI tracks. Consider it as a workaround to the limited articulations available at one time in the Performance patch. The main differences are that it has no Animator, and each instance of the Single patch can contain just one of the 12 possible articulations; there's no velocity switching here, apart from dynamics. The idea is that you load as many instances of this patch as necessary, each one responding to its own MIDI channel and containing an articulation you need. They could even have different instrument setups or Voicing assistant settings. This is clearly a more intensive, time-consuming pursuit, but it does allow for unfettered access to the full range of articulations and instrument setups — as long as you have the patience!

## Conclusion 
 Session Horns brings a bright, lively four-piece brass ensemble to a keyboard near you. With care and consideration, it's capable of producing very believable results, using just one instance of the Performance patch, and the surprisingly flexible Animator certainly helps to add a touch of realism when you don't have the time or inclination to flesh out authentic arrangements yourself. Although an instrument in this price range won't cover every conceivable articulation and playing technique, it offers enough expressivity to do the job convincingly well, and represents very fair value for money.  
 
## Alternatives 
 In my search for other sampled brass libraries that have the same pop/funk/soul remit as Session Horns, and which also offer a small-scale ensemble, two significant contenders emerged. The first, Chris Hein Horns Pro Complete, includes a very respectable range of brass and woodwind instruments with many articulations, and allows the user to vary the ensemble size from solo instruments all the way up to big-band proportions. The other, Vir2's Mojo Horn Section, covers the subject in equally comprehensive detail. The greater scope offered by both these libraries explains why they also cost around four to five times as much as Session Horns.

## Download & Installation 
 Session Horns is provided as a 3.7GB download; NI's NKX compressed sample format represents 4.88GB of 44.1kHz, 24-bit uncompressed data. In accordance with NI's new regime, an app specific to the product must be downloaded first. When run, the app handles downloading and installation of the product directly to your studio computer. It also allows for the installation file to be transferred to a different computer, if your studio machine is not connected to the Internet.

## Memory Savings 
 The Performance patch eats up a not inconsiderable 1.32GB RAM, which may make adding Session Horns to an already RAM-hungry project something of an issue for those still working in 32-bit land. Kontakt's on-the-fly sample loading becomes very useful in these circumstances. To take advantage of this, first prepare an 'empty' version by loading the Performance patch and then removing all the samples using Kontakt's Purge function. Resave this as a new patch. Now you have a empty, RAM-friendly version you can load up at any point. Kontakt will simultaneously load and play notes on demand (or do its best to comply), so only the samples actually needed take up any memory.

## Recommended Specs 
 Windows 7, Mac OS 10.6 or higher.
 Kontakt 5 or Kontakt 5 Player, version 5.0.3 or higher, compatible with all the standard plug-in formats. Although not officially supported by NI, Kontakt is also compatible with Windows XP.

### Pros
 Well recorded, with a bright, lively sound.
 Covers a dynamic range from mp to ff.
 Lots of 'ready-to-go' sound presets to suit different musical applications.
 Realistic Animator phrases that can be harmonically re-voiced to fit your tracks.
 Smart Voice Split mode.

### Cons
 Performance patch's alternative articulations not keyswitchable.
 No solo instrument setups, though they're possible by tweaking under the hood.
 Chord+Legato mode can be tricky to keep under control.

### Summary
 No more cobbling together individual sampled brass instruments from disparate sources to make up a small section — Session Horns brings together a well-sampled, cohesive, four-piece brass ensemble well suited to modern pop recordings. Its pre-programmed Animator phrases are harmonically flexible, and the Voicing Assistant provides different playing modes to aid arranging and live performance, and all at an affordable price.

### information
 €99 including VAT. Native Instruments +49 30 6110 350
 www.native-instruments.com 

 $119. Native Instruments +1 866 556 6487.
 www.native-instruments.com 

 Buy PDF version 

 Previous article Next article 

## In this article... 

 Introduction 

 Brass Onesie 

 Voicing Assistant 

 Animatronics 

 Sound Options Tab 

 Control Options Tab 

 The Single Articulation Patch 

 Conclusion 

 Alternatives 

 Download & Installation 

 Memory Savings 

 Recommended Specs 

## SOS Competitions 

## On the same subject 

 Fracture Sounds Trails 2 October 2026 

 Audiomodern Voxmotive 2 October 2026 

 Musical Sampling Midnight Tenor Sax & Midnight Alto Sax October 2026 

 Emergence Audio Envoy September 2026 

 Handcrafted Audio Handcrafted Mallets September 2026 

## From the same manufacturer 

 Native Instruments Absynth 6 July 2026 

 Native Instruments Moments: Vocal Clouds June 2026 

 Native Instruments Circular October 2025 

 Native Instruments Scene: Nightshade October 2025 

 Composing With Chance August 2025 

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