---
titre: "Music Production Wiki — Bible : Compression (attaque/release chiffrés par source, bus de batterie, mix bus, HPF de sidechain, dépannage)"
source: https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/compression.html
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: mixage et mastering (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Page HTML du wiki convertie en Markdown (html2text) ; document communautaire [HEUR] : valeurs de départ, pas des mesures.

[ MusicProductionWiki ](/)

  * [Articles](/categories/techniques)
  * [Gear](/categories/hardware)
  * [About](/about)
  * [Tools](/tools/)

A MusicProductionWiki Publication [Sound Better →](https://theproducersbriefing.beehiiv.com)

[ ◆ The Producer's Bible ](/bible/)

[Dynamics](/bible/categories/dynamics/) [Frequency](/bible/categories/frequency/) [Time-Based](/bible/categories/time-based/) [Signal Processing](/bible/categories/signal-processing/) [Mixing](/bible/categories/mixing/) [Mastering](/bible/categories/mastering/) [Synthesis](/bible/categories/synthesis/) [Music Theory](/bible/categories/music-theory/) [Production](/bible/categories/production/) [Recording](/bible/categories/recording/) [Tools](/bible/categories/tools/)

[ The Producer's Bible ](/bible/)

Bible Categories

[Dynamics](/bible/categories/dynamics/) [Frequency](/bible/categories/frequency/) [Time-Based](/bible/categories/time-based/) [Signal Proc.](/bible/categories/signal-processing/) [Mixing](/bible/categories/mixing/) [Mastering](/bible/categories/mastering/) [Synthesis](/bible/categories/synthesis/) [Music Theory](/bible/categories/music-theory/) [Production](/bible/categories/production/) [Recording](/bible/categories/recording/) [Tools](/bible/categories/tools/)

Articles

[Techniques](/categories/techniques) [Reviews](/categories/reviews) [Comparisons](/categories/comparisons) [Breakdowns](/categories/breakdowns) [Genres](/genres) [AI Music](/categories/ai-music) [Music Business](/categories/music-business)

Gear

[DAWs](/categories/daws) [Plugins](/categories/plugins) [Hardware](/categories/hardware)

Site

[Tools](/tools/) [About](/about)

[Sound Better →](https://theproducersbriefing.beehiiv.com)

`esc`

Definition How It Works New Producers Parameters Quick Ref Calculator Signal Chain Fix It History How To Use By Genre Topology Hardware vs Plugin Before / After In The Wild Producer DNA Signatures Types Verdict Plugins Mistakes Mix Test Flags Progression FAQ Related

[Home](/)› [The Producer's Bible](/bible/)› [Dynamics](/bible/categories/dynamics)› Compression

Dynamics

Intermediate

Understand first: [Gain Staging](/bible/gain-staging) › [Dynamic Range](/bible/dynamic-range) › [Headroom](/bible/headroom)

# Compression

noun / dynamics processor

_Compression is not a volume tool. It is a time tool -- it decides when the listener hears what they hear. And that invisible control of musical time is why every record you have ever loved sounds the way it does._

📅 Updated 2026-07-01 ⏲ 28 min read 📚 Producer's Bible

Quick Answer

Compression is dynamic range reduction -- it automatically turns down the loudest parts of a signal when they exceed a set threshold, then turns them back up with makeup gain. The result is a more consistent, controlled, and often more present-sounding source. Every professional mix uses it, on almost every element, in ways the listener is never supposed to consciously hear.

⇓ Download Reference Sheet

Common Misconception

More compression makes everything sound louder and more professional.

More compression makes everything sound flatter. The records that sound loud and professional are loud because compression was used to preserve transients and manage headroom intelligently -- not because a high ratio was applied to everything. Heavy-handed compression is one of the fastest ways to make a mix sound amateur. The goal is always 3-6dB of gain reduction at most on individual channels, applied for a specific sonic reason, in a way the listener feels but never hears.

## What Is Compression?

_Compression is not a volume tool. It is a time tool -- it decides when the listener hears what they hear. And that invisible control of musical time is why every record you have ever loved sounds the way it does._

At its most mechanical level, a compressor is simple: when an audio signal rises above a threshold you set, the compressor reduces its gain by a ratio you choose, over a time you control. The signal is turned down when it gets too loud. Makeup gain brings the overall level back up afterward. That is the complete technical description of what a compressor does, and it explains almost nothing about why compression is the most important and most misunderstood tool in music production.

What compression actually does is change the relationship between a sound and the listener's perception of time. The attack of a snare -- the initial crack when the stick hits the head -- arrives at the listener's ear as a transient: a brief, intense spike of energy that the auditory system perceives as the beginning of an event. What follows is the body and the decay, the sustain of the drum shell resonating, the room bleeding in. A compressor with a fast attack setting clamps down on that transient and reduces it, pulling the initial impact back into the mix while letting the body and tail come up relatively louder. A compressor with a slower attack lets the transient pass through untouched before the gain reduction begins, preserving the crack while still controlling the overall level. The producer who understands this is not thinking about volume. They are thinking about shape -- the architecture of the sound event in time.

This is why compression sounds musical when done right and suffocating when done wrong. When a producer compresses a kick drum with a 10ms attack and a 60ms release at 4:1, they are making a precise aesthetic decision about how much punch the listener should feel before the compressor intervenes, and how long the compressor holds before releasing its grip to let the next hit breathe. When a different producer slams the same kick with a 1ms attack and a 20ms release at 10:1, they have removed the punch entirely and replaced it with a kind of energy-bevelled thud. The signal is controlled. The music is gone. Both producers turned the same knobs. Only one understood what the knobs were actually doing.

Compression also performs a function that goes largely undiscussed: it controls the emotional texture of a performance. A vocal that moves between quiet verses and powerful choruses without compression sounds raw and unmanaged -- the performance is honest but the listening experience is work, requiring the listener to mentally adjust their relationship to the sound as the level shifts. The same vocal with two or three dB of gentle compression applied with a slow attack and a musical release becomes more consistent, more controlled, closer to the listener's ear -- not because the performance changed, but because the dynamic swings that pull focus have been softened. The vocal feels more confident, more present, more produced. This is compression as narrative tool: not fixing a problem, but making a choice about what the listener's experience of the performance should be.

> "Compression is the most used and least understood tool in the studio. Every record you've ever loved was shaped by it. Most producers who use it daily couldn't tell you exactly what it's doing -- and that gap between using it and understanding it is exactly what separates a good mix from a great one."

-- Dave Pensado, Mix Engineer (Beyonce, Christina Aguilera, Mary J. Blige) -- Pensado's Place, 2018

◆ Psychoacoustics

What Your Brain Is Actually Doing

Compression works because of how the human auditory system perceives loudness, transients, and time. Understanding these mechanisms explains why the same settings produce radically different results on different sources.

The Loudness-Dynamics Paradox

The ear judges loudness by average energy over time, not peak level. A heavily compressed signal with peaks pulled down but average level raised sounds louder than an uncompressed signal at the same peak level. This is why masters sound loud without exceeding digital ceiling -- and why streaming normalization changed everything._-> Use this: Compress to raise average level with makeup gain. Then A/B at matched loudness. What you hear is the tonal effect of compression, not the level effect._

Transient Perception & Attack

The auditory cortex uses the shape of a transient's onset to identify the source material -- the difference between a piano strike and a string pluck. A compressor's attack setting determines how much of this onset arrives unprocessed. Fast attacks strip the identifying information. Slow attacks preserve it._-> Use this: When something sounds "controlled but flat," the attack is too fast. Open it up by 10ms at a time until the source regains character. The transient is the identity._

The Stapedius Reflex

The stapedius muscle in the middle ear reflexively tightens when exposed to loud sounds, reducing sensitivity to protect the cochlea. This natural compression has an attack of roughly 25ms and a release of 150ms. Hardware compressors with these approximate time constants often sound "musical" because they mirror what the ear does automatically._-> Use this: When seeking "transparent" compression, start at 25ms attack / 150ms release. You are mimicking biology._

Pump and Breathe Perception

When gain reduction is audible -- the mix sinking with the kick, the compressor releasing loudly between hits -- the ear perceives this as rhythmic breathing. In EDM, this is engineered and desired. In most other contexts, it signals a release setting that is too fast for the tempo and material. The ear notices the level fluctuation because it happens faster than the stapedius adapts._-> Use this: If you can hear the compressor breathe and it's unwanted, slow the release by 50ms. Repeat until the gain reduction is felt rather than heard._

Sustained vs. Impulsive Sources

The ear processes sustained tones (strings, pads, vocals) and impulsive transients (drums, plucked strings, percussion) through different perceptual pathways. Attack settings that work beautifully on a sustained vocal destroy the impact of a snare because the perceptual mechanism being addressed is entirely different._-> Use this: The first question before setting a compressor is: does this source have meaningful transients? If yes, attack is the most critical setting. If no, ratio and threshold matter more._

Density and Perceived Proximity

Higher average RMS level (produced by compression) signals proximity to the listener -- the auditory cortex interprets louder as closer. This is why a compressed vocal appears to sit further forward in the mix without physically changing its level. The compressor has changed its perceived distance by reducing the dynamic variation that connotes acoustic space._-> Use this: Compression is a depth tool as well as a dynamics tool. More compression = more forward. Less = further back. Use this alongside reverb to control three-dimensional placement._

_Compression is dynamic range reduction applied in service of three goals: consistency, shape, and perceived proximity. The mechanism is simple. The art is knowing which goal you 're serving with each setting -- and whether that setting is telling the listener something true about the music or something false._

## How Compression Works

Every compressor, regardless of topology or era, performs the same fundamental operation: it monitors the level of the incoming signal through a detector circuit, compares that level against a threshold, and when the signal exceeds the threshold, reduces the output gain by the amount dictated by the ratio setting -- but not instantly, and not permanently. The speed of the response is controlled by attack and release. The amount of response is controlled by ratio. Where the response begins is controlled by threshold. These four parameters, in various combinations, produce every compression sound that has ever existed in recorded music.

The detector circuit is worth understanding in isolation because it determines the compressor's character as much as any other element. In a feedforward design -- which includes most modern digital compressors and many classic hardware units -- the detector reads the incoming signal before it enters the gain reduction stage. The compressor can therefore predict that gain reduction is coming and apply it in advance, which produces a more controlled, modern sound. In a feedback design -- the architecture of vintage units like the Fairchild 670 and most optical compressors -- the detector reads the output signal after gain reduction has occurred. This creates an inherent lag that produces the characteristically "slow to grab" feel of those compressors, where the gain reduction eases in rather than snapping. Neither architecture is superior. They are different sonic answers to the same mechanical question.

Compression signal flow: Input through detector sidechain to gain reduction element to output INPUT Audio Signal SIDECHAIN / DETECTOR THRESHOLD Compares level GAIN REDUCTION Ratio * Attack * Release Knee * Topology MAKEUP GAIN Restore output level OUTPUT Compressed Signal GR Meter −4.2 dB

The gain reduction element itself -- the component that actually reduces the level -- varies by topology and produces the most significant sonic differences between compressor types. A Voltage Controlled Amplifier (VCA) responds in microseconds, producing clean, fast, controllable gain reduction with minimal coloration. A Field Effect Transistor (FET) produces fast gain reduction with a characteristic harmonic edge -- the slight distortion that gives the 1176 its presence and aggression. An optical attenuator responds slowly and non-linearly, because the speed of the control element is physically limited by the time it takes for a light source to illuminate a photoresistive cell -- this produces the "program-dependent" behaviour that makes optical compressors feel musical and unpredictable in the best way. A Variable-Mu tube circuit uses the gain of a tube stage as the gain reduction element, responding even more slowly and producing the warmth and glue associated with mastering compressors. The compressor's topology is not a cosmetic distinction. It is the fundamental character of the device.

The knee setting determines how the compressor transitions from no gain reduction below the threshold to full gain reduction above it. A hard knee applies the full ratio immediately when the signal crosses the threshold -- a sharp, definitive response that can sound clinical or aggressive depending on the material. A soft knee gradually increases the gain reduction ratio as the signal approaches and crosses the threshold, beginning the reduction below the threshold and completing it above, creating a smoother, less noticeable transition into compression. Most program material benefits from a soft knee because the onset of compression is less perceptible, but a hard knee can add impact and definition to percussive sources where the exact point of compression matters sonically.

_Every compressor monitors level through a detector, compares it against a threshold, and applies gain reduction at a speed and amount determined by four parameters. The topology of the gain reduction element -- VCA, FET, optical, or variable-mu -- determines the character of that reduction more than any parameter setting._

## If You Are New to Compression -- Read This First

◆ Before You Touch a Compressor

Every producer serious about compression makes the same three mistakes in their first year. Not some producers -- every producer. They come from the same logical-sounding assumptions that turn out to be wrong once you understand [what compression is actually doing](../articles/what-is-compression-music-production). If you are new to this, read these three before you open another compressor. If you have been producing for a while, read them anyway -- you will recognize at least one in something you mixed last month.

1

Setting ratio before threshold

Why it happens

Ratio is the most visible, most discussed parameter. Producers set it first because it feels like the main decision -- how hard should I compress? But ratio without threshold context is meaningless. A 10:1 ratio with the threshold at 0dBFS does nothing, because the signal never crosses it. A 2:1 ratio with the threshold at −40dBFS destroys everything, because the signal is always far above it and being continuously reduced. The ratio is how hard the compressor grabs. The threshold decides when. You cannot set how hard without first deciding when.

The Fix -- Do This Instead

Set ratio to 4:1 and leave it. Lower the threshold until the GR meter moves 3-6dB on the loudest moments of the performance. Now you have a reference point. Once you can hear what the compressor is doing at 4:1, you have the context to decide whether more or less ratio serves the sound. Threshold first. Always.

2

Setting compression levels in solo

Why it happens

You solo the channel, add compression, adjust until it sounds right, unsolo and move on. This is logical in principle and wrong in practice. A compressed vocal soloed sounds impressive at almost any setting -- dense, controlled, present, close. In a full mix, every other element is also occupying space. The reverb tail that sounded beautiful in solo is now competing with the kick drum for low-mid frequency. The attack setting that felt punchy in solo is now clashing with the guitar transient arriving at the same time. Your compression calibration environment is corrupted the moment you hit solo.

The Fix -- Do This Instead

Set every compression setting with the full mix playing. To calibrate level: mute the compressor output while the mix plays. If the element feels suddenly exposed, naked, or dynamically uncontrolled -- the compression is working. Back off 1dB from the point where muting it feels wrong. That is the correct level. Never calibrate compression in solo.

3

Using compression to fix a bad performance

Why it happens

The vocal performance is inconsistent -- some phrases quiet, some loud, some words buried, some peaking. The instinct is to compress harder to even it out. This makes sense because compression does even out dynamic inconsistency. The problem is that heavy compression evens out level but cannot fix pitch drift, timing issues, or an emotionally disconnected performance. A 10:1 ratio on a mediocre performance produces a consistently mediocre performance, louder and more present than before. The compression has not improved the performance. It has made the performance more audible and less fixable.

The Fix -- Do This Instead

Edit first. Clip-gain the loudest sections down and the quietest sections up before compression touches the signal. Reduce the dynamic range through editing until a gentle 3-4dB of compression at 3:1 is sufficient to control what remains. Compression refines a performance. It does not rescue one. The best-sounding vocals in recorded history were edited before they were compressed.

Share with a producer who needs this

Copy Link[Share on X](https://x.com/intent/tweet?text=The+3+compression+mistakes+every+producer+makes+%E2%80%94+@mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23new-producers)[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23new-producers&title=The+3+compression+mistakes+every+producer+makes+%E2%80%94+@mpwikiofficial)

## Parameters

The six parameters below are universal across every compressor ever built. They exist whether the compressor has knobs, faders, touchscreens, or no visible controls at all. Understanding each parameter in isolation -- what it controls, what it sounds like at its extremes, and what its relationship is to the other parameters -- is what separates producers who can reliably get good compression from producers who occasionally stumble into it.

Threshold

Typical range: −60 to 0 dBFS

The level at which compression begins. When the signal exceeds the threshold, the compressor engages. Below the threshold, the signal passes through unaffected. Lower threshold = more of the signal gets compressed = more gain reduction overall. This is the first parameter to set. All other settings are meaningless without it calibrated to the material. Watch the GR meter, not the threshold number.

Ratio

Typical range: 1:1 (off) to ∞:1 (limiting)

How hard the compressor reduces gain once the signal crosses the threshold. At 4:1, every 4dB the signal goes above threshold, only 1dB comes out the other side. At 2:1, every 2dB above threshold becomes 1dB. At ∞:1 (brick wall), nothing above the threshold passes through -- this is limiting. Start at 4:1 for almost every application. 2:1 for gentle bus control. 8:1+ for aggressive shaping. Above 10:1, you are limiting, not compressing.

Attack

Typical range: 0.1ms to 300ms

How quickly the compressor begins reducing gain after the signal crosses the threshold. Fast attack (1-5ms) clamps immediately, reducing transient impact -- the initial hit is softened. Slow attack (20-100ms) lets the transient pass through before gain reduction engages, preserving the crack and punch of the source. This is the most creative parameter. Start at 10ms. Move slower for more punch, faster for more control.

Release

Typical range: 5ms to 5,000ms (or Auto)

How quickly gain reduction stops after the signal falls back below the threshold. Fast release (20-50ms) snaps back quickly, which can cause audible pumping if too fast -- the gain comes back up noticeably between hits. Slow release (200-500ms) holds the gain reduction longer, producing a smoother, more sustained compression character. Auto release is program-dependent: the compressor calculates release based on the incoming signal. Often the best starting point. Start at 100ms if manual.

Knee

Hard / Soft (or 0-100 on some units)

How the compressor transitions from uncompressed to fully compressed as the signal crosses the threshold. Hard knee: the full ratio applies immediately at the threshold -- an abrupt transition that can sound precise or harsh depending on material. Soft knee: the ratio gradually increases as the signal approaches and crosses the threshold, spreading the compression across a range of levels for a smoother, less audible onset. Use soft knee for vocals and bus processing. Hard knee for drums when impact matters.

Makeup Gain

Typically 0 to +24 dB

Manual gain added after gain reduction to bring the output level back toward the input level. Because compression reduces the loudest moments, the overall average level of the compressed signal is lower than the input -- makeup gain corrects this. Critical rule: always A/B bypass at matched levels. Makeup gain makes compressed signals sound better than uncompressed signals at the same level simply because they are louder. Match levels at bypass to hear the actual effect of the compression.

Lookahead

Typically 0-20ms (limiters)

Allows the compressor to read the incoming signal slightly ahead of time and begin gain reduction before the transient actually arrives, preventing the attack phase from letting any overshoot through. Used primarily in limiters and transparent mastering compressors. The tradeoff is latency -- lookahead introduces a delay equal to its value. Essential for true peak limiting. Not common in mixing compressors, where the transient behaviour of the attack setting is often part of the sound.

The parameters interact in ways that make compression feel complex, but the interaction is predictable once the underlying logic is understood. Ratio and threshold together determine how much gain reduction occurs. Attack and release together determine the shape of that gain reduction in time -- how quickly it grabs and how quickly it lets go. Knee determines how smoothly the transition happens. Makeup gain sets the output level after all of the above have done their work. These are not independent levers. They are a system.

The most important inter-parameter relationship is between attack and release relative to tempo. A release setting that is too short for the tempo causes the compressor to release between every beat, producing audible breathing. A release that is too long causes the compressor to still be holding from the previous hit when the next one arrives, losing definition between events. Matching release to tempo -- approximately 60,000ms divided by your BPM for one beat -- is the fastest way to make a compressor feel musical rather than mechanical. At 120 BPM, one beat is 500ms. A release of 400-600ms on a drum bus will almost always sound right before any further adjustment.

_Six parameters control every compressor. Threshold sets where compression begins. Ratio sets how hard it clamps. Attack sets how fast it grabs. Release sets how fast it lets go. Knee sets how smoothly it transitions. Makeup gain restores output level. They are a system, not independent controls -- and the most important interaction is always between release time and tempo._

4:1 The Universal Starting Ratio

Enough control to hear what the compressor is doing without destroying dynamics. Every ratio decision is a departure from here -- more for control, less for transparency. Set this first, adjust threshold until the GR meter moves 3-6dB, and do not change the ratio until you understand what you are hearing.

The table below is the quick reference you bookmark and return to mid-session. These are not rules -- they are starting points built from production practice across major commercial releases. The goal is to get you in the right neighbourhood in thirty seconds. Your ears take it from there.

Parameter | Kick | Snare | Drum Bus | Vocals | Bass | Guitar | Mix Bus | Parallel  
---|---|---|---|---|---|---|---|---  
Ratio| 4:1-6:1| 4:1-8:1| 4:1-6:1| 2:1-4:1| 4:1-6:1| 2:1-4:1| 2:1-4:1| 8:1-20:1  
Attack| 10-25ms| 5-15ms| 15-40ms| 10-30ms| 30-60ms| 15-40ms| 30-100ms| 1-5ms  
Release| 40-80ms| 40-100ms| 100-300ms| 60-150ms| 60-150ms| 80-200ms| 150-400ms| 60-150ms  
Threshold| −20 dBFS| −18 dBFS| −15 dBFS| −18 dBFS| −18 dBFS| −20 dBFS| −10 dBFS| −30 dBFS  
GR Target| 4-8dB| 4-8dB| 4-8dB| 3-6dB| 3-6dB| 3-5dB| 1-3dB| 8-15dB  
Knee| Hard| Hard| Soft| Soft| Soft| Soft| Soft| Hard  
Character| FET / VCA| FET / VCA| VCA / FET| Optical / VCA| Optical / VCA| VCA / Optical| VCA / Var-Mu| FET / VCA  
  
Share

Copy Link[Share on X](https://x.com/intent/tweet?text=Compression+Quick+Reference+%E2%80%94+@mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23quick-reference)[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23quick-reference&title=Compression+Quick+Reference+%E2%80%94+@mpwikiofficial)

## Gain Reduction Calculator

Enter your compressor settings to calculate exact gain reduction, output level, and final level with makeup gain. Use this mid-session to verify your settings before committing, or to reverse-engineer a target GR amount from a ratio and threshold combination.

MusicProductionWiki.com

Gain Reduction Calculator

Input Level (dBFS)

Threshold (dBFS)

Ratio (x:1)

Makeup Gain (dB)

Excess

+8.0 dB

above threshold

Gain Reduction

-6.0 dB

applied

Output Level

-16.0 dBFS

pre-makeup

Final Level

-10.0 dBFS

with makeup

Signal is 8dB above threshold. At 4:1, 6dB of gain reduction is applied. Output is -16dBFS. With 6dB makeup, final level is -10dBFS -- matching input. Set threshold lower to increase gain reduction, or raise ratio for the same threshold.

Common Starting Points

Drum Bus4:1 / -18

Vocals3:1 / -20

Snare6:1 / -16

Mix Bus2:1 / -12

Bass4:1 / -22

Parallel8:1 / -14

Gain reduction = excess above threshold × (1 − 1/ratio). Makeup gain brings output back toward input level but cannot restore transient peaks removed by compression. Always A/B at matched output levels to hear the actual effect. Source: musicproductionwiki.com/bible/compression

Share this tool

Copy Link[Share on X](https://x.com/intent/tweet?text=Free+Gain+Reduction+Calculator+%E2%80%94+@mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23tools)[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23tools&title=Free+Gain+Reduction+Calculator+%E2%80%94+@mpwikiofficial)

◆ Embed This Tool

Paste this snippet to embed the calculator on your site.

Copy Embed Code

`<iframe src="https://musicproductionwiki.com/bible/compression#tools" width="100%" height="520" style="border:none;border-radius:10px;background:#0d0d0d" title="Gain Reduction Calculator" loading="lazy"></iframe>`

## Signal Chain Position

Signal chain position of Compression in music production Source Instrument / Vocal Clip Gain Pre-fader prep EQ Corrective / creative Compression Dynamics control Gain reduction ◀ YOU ARE HERE Saturation Harmonic color Reverb / Delay Space & time Fader Final level Mix Bus Master output

Source

Instrument / Vocal

↓

Clip Gain

Pre-fader prep

↓

EQ

Corrective / creative

↓

Compression

Dynamics control * Gain reduction

▶ You are here

↓

Saturation

Harmonic color

↓

Reverb / Delay

Space & time

↓

Mix Bus

Compression sits after EQ and before saturation and time-based effects. The order matters in both directions. Placing compression after EQ means the compressor responds to the tonal balance you have already established -- if you have boosted 3kHz on a vocal for presence, that boost will trigger more gain reduction at 3kHz, which the compressor's broadband response then applies to the whole signal. This can be desirable (the presence boost is tamed dynamically) or undesirable (the boost feels inconsistent, present on quiet syllables and reduced on loud ones). Placing EQ after compression gives you clean gain reduction followed by tonal shaping of the compressed result. Both approaches are valid. The rule is to know which you are choosing and why.

Placing compression before saturation produces controlled harmonic distortion -- the saturation stage sees a more consistent, level-controlled signal, which means its harmonic generation is also more consistent. Placing saturation before compression produces dynamic harmonic distortion -- loud transients generate more harmonics, which the compressor then controls alongside the fundamental. Louder passages will sound tonally richer before compression reduces them. This interaction is the basis of the "tape machine before compressor" approach used in many vintage signal chains.

#### Interaction Warnings

  * **Compression + EQ (Order):** EQ before compression means the compressor responds to your tonal decisions. EQ after compression means you shape the compressed sound. Most common approach: corrective EQ before (remove problems), creative EQ after (add character). Never assume one order is always correct -- the question is what you want the compressor to respond to.
  * **Compression + Limiting:** A compressor manages the body of the dynamic range. A limiter handles the peaks that compress past what the compressor can control. They are not the same tool applied twice -- they are two stages addressing different parts of the dynamic problem. The compressor sets the character; the limiter sets the ceiling.
  * **Compression + Saturation (Order):** Compress then saturate for consistent harmonic density. Saturate then compress for dynamic harmonic texture that breathes with the performance. The second approach is how analog tape behaves and why recordings made to tape have a particular quality of "life" that is difficult to replicate in the box.
  * **Compression + Parallel Blend:** When running parallel compression, the dry signal must be phase-aligned with the compressed signal before blending. Most DAWs handle this automatically via delay compensation, but confirm on the plugin level. Phase misalignment at the blend point creates comb filtering that sounds like the kick "hollowed out" rather than widened.
  * **Compression + Sidechain (Low Frequency):** When sidechaining a bass compressor to a kick drum, the kick's full frequency content triggers gain reduction. High-pass the sidechain signal at 80-120Hz to remove the sub frequencies from the detection path -- this allows the fundamental to trigger the compressor without the sub triggering it disproportionately, which causes the bass to duck more than intended.



## Fix It -- What Are You Hearing?

You are in a session. Something is wrong with your compression and you do not have time for theory. Pick the symptom. Get the fix.

◆ Interactive

Compression Diagnostic

Select the symptom you are hearing. The fix appears immediately.

My mix is pumping or breathing The level audibly rises and falls with the music ⌄

Release time too fast. The compressor releases between hits loudly enough you hear the gain coming back up.

Slow release 50ms at a time until breathing stops. Drum bus: 150–300ms. Mix bus: 250–400ms.

`Release: 150–300ms (drum bus) · 250–400ms (mix bus) · Auto if available`

My kick / snare lost its punch The hit sounds dull or thuddy after compression ⌄

Attack too fast. Compressor clamps the transient before the listener hears the initial impact.

Open attack to 10–25ms on individual drums, 15–40ms on drum bus. Transient must pass through before compressor grabs.

`Attack: 10–25ms (individual) · 15–40ms (drum bus) · GR: 4–8dB max`

Everything sounds flat and squashed Louder but lifeless — the mix lost energy ⌄

Over-compression. Peaks that create energy are removed. Makeup gain is lying — louder but lifeless.

A/B bypass at matched levels. Reduce makeup gain when bypassing. If bypassed sounds better: less compression.

`Ratio: 2:1–4:1 · GR: 3–6dB · A/B at matched loudness`

My vocal is still inconsistent Compression is not evening out the performance ⌄

Dynamic range too large for compression alone. Heavy settings crush character without solving the problem.

Edit first: clip-gain loud syllables down, quiet ones up. Reduce DR to 8–12dB, then compress gently.

`Clip-gain first · Then: 3:1 · 15ms attack · Auto release · 3–4dB GR`

My compressed source sounds clicky or distorted An artifact appears on the transient after compression ⌄

Attack too fast creating a gain reduction artifact, or inter-sample peaks hitting a downstream limiter.

Open attack by 2ms increments. Switch to soft knee. Check downstream limiter inter-sample peak protection.

`Attack: increase 2ms at a time · Knee: Soft · Check downstream limiter`

My mix bus compression is muddying the low end The kick and bass feel heavier but less defined ⌄

Bus compressor responding disproportionately to bass energy, over-triggering on low frequencies.

Reduce mix bus GR to 1–2dB. Try sidechain HPF at 80–100Hz to prevent bass from over-triggering.

`GR: 1–2dB max · Attack: 20–30ms · Sidechain HPF: 80–100Hz`

My snare sounds thin after compression Body and ring are gone, only the attack remains ⌄

Release too slow. Compressor still holding when the body tries to come through.

Decrease release by 20ms increments until body returns. Compressor must release fast enough for sustain.

`Release: decrease 20ms at a time · Target: 40–80ms · GR: 4–8dB`

The mix sounds better with compression bypassed Every setting makes it worse, not better ⌄

Three causes: judging at unmatched levels, individual channels already flattened, or wrong topology.

Match output levels before A/B. Bypass channel compressors first. Try a different compressor topology.

`A/B at matched levels · Bypass channels first · Try different topology`

`` <- Different symptom

## History of Compression

Compression was not invented for music. It was invented to prevent radio transmitters from overloading. The fact that the most expressive, most musical, most artistically significant tool in modern music production began as a piece of broadcast protection equipment is one of the great accidents of audio history -- and understanding that origin explains almost everything about why compression sounds the way it does and why its misuse sounds the way it does.

### The Limiter as Broadcast Safety (1930s-1950s)

The first dynamic range compressors were limiters, built to solve a specific engineering problem: radio transmitters could only broadcast within a fixed power range, and a vocalist who moved closer to the microphone or sang louder than calibrated would overload the transmitter, causing audible distortion on the receiver. The Western Electric and RCA broadcast limiters of the 1930s and 1940s were designed entirely around preventing this failure -- not around sounding musical. They clamped hard when the signal got too loud and released when it fell back. That was the complete specification.

What engineers discovered, by accident and then by design, was that these devices changed the character of the compressed sound in ways that were sometimes desirable. Voices sounded more present. Instruments sat more consistently in the mix. The dynamic variation that made individual performances feel natural and live made recordings feel inconsistent and difficult to listen to. The limiter was solving an aesthetic problem no one had explicitly named yet: recorded audio needed to be domesticated.

### The UREI 1176 and the FET Revolution (1967)

Bill Putnam designed the Universal Audio 1176 Peak Limiter in 1967, and it remains the most influential compressor ever built. The 1176 used a Field Effect Transistor as its gain reduction element -- the first compressor to do so -- which allowed it to respond in microseconds, far faster than any previous design. It also introduced the concept of the ratio as a creative parameter rather than a fixed design choice, offering four positions (4:1, 8:1, 12:1, and 20:1) plus the now-legendary "All Buttons In" mode, where all four ratio buttons were engaged simultaneously to produce a distinctive, overdriven sound that is heard on more hit records than any other compressor configuration in history.

The 1176 defined the sound of classic rock, R&B, and soul recording through the late 1960s and 1970s. It is on John Lennon's vocals on Imagine. It is on almost every significant Led Zeppelin recording. It is on Aretha Franklin's I Never Loved a Man the Way I Love You. What these records have in common sonically -- the particular density, the presence, the controlled aggression -- is substantially the 1176's character applied at various settings by engineers who understood what it was doing to the music. The 1176 is not a transparent compressor. It imposes its own aesthetic on the material it processes. The engineers who used it to greatest effect did not fight this character. They composed with it.

### The Optical Era and the LA-2A (1962-Present)

While the 1176 was defining the sound of fast, aggressive compression, Teletronix was building something entirely different. The LA-2A Leveling Amplifier, introduced in 1962, used an electro-optical circuit -- a light-emitting element driving a photoelectric cell -- as its gain reduction element. The physics of the system produced a response that was slow, non-linear, and impossible to fully specify in a parameter sheet: the LA-2A responds differently to different types of audio material, remembers the recent history of gain reduction in ways that pure analog circuits cannot, and produces a warmth and musical smoothness that engineers to this day struggle to explain in technical terms but immediately recognize by ear.

The LA-2A became the definitive vocal compressor of the 1960s and remains so today. Its limitation -- only two controls, Gain and Peak Reduction, with no ratio, attack, or release settings the engineer can directly adjust -- is in practice its greatest asset. The engineer cannot overthink it. They set the threshold, apply the appropriate amount of gain reduction, and the optical circuit handles the musical translation of the dynamic performance into a consistent, intimate signal. The most dangerous compressor for a new producer to own is one with too many parameters. The LA-2A offers the fewest possible and produces the most consistently musical results.

### The Loudness Wars and Their Aftermath (1990s-Present)

The compact disc introduced a clearly defined digital ceiling -- 0dBFS, beyond which nothing could pass. The music industry spent the next twenty years treating this ceiling as a competitive target rather than a safety limit. If a record could be mastered louder than a competitor's record while remaining technically compliant, radio programmers would perceive it as more energetic, consumers would perceive it as better-produced, and it would stand out on listening panels. The mechanism for achieving this was compression: apply enough gain reduction to reduce the peaks, apply enough makeup gain to bring the average level up to the ceiling, repeat until the dynamic range has been reduced from the 12-15dB that sounds natural to the 3-6dB that sounds like every major commercial release from 1999 to 2010.

The Loudness Wars ended not because the industry had an aesthetic revelation, but because streaming normalization made hyper-compression self-defeating. When Spotify began normalizing tracks to −14 LUFS in 2013, a track mastered at −6 LUFS was turned down by 8dB -- leaving only the damage: the flattened transients, the reduced dynamic contrast, the listening fatigue that comes from sustained high average levels. A track mastered at −14 LUFS was played at the same level with all its dynamics intact. The compression arms race had been neutralized by infrastructure. The producers who understood this first began making records with more headroom, more transient impact, and more dynamic range -- and those records sounded better at normalized streaming levels than the compressed ones. Compression returned to its original purpose: not a weapon in a loudness war, but a tool for shaping sound in time.

> "The loudness war is over, and the right side won. Not because anyone had a change of heart -- because streaming normalization made competing in it pointless. The producers who understood that earliest made better records for longer."

-- Bob Katz, Mastering Engineer (Grammy-winner, Digital Domain Mastering) -- AES Convention 133, Stereophile report, 2012

_Compression began as broadcast protection, became a creative tool through the accidents and experiments of analog recording, was weaponized in the Loudness Wars, and emerged on the other side of streaming normalization as what it always should have been: a precision instrument for controlling the relationship between sound and time. Understanding this arc explains why "less is more" is not a conservative philosophy but a technical fact._

## How To Use Compression

The most important thing to understand about applying compression is the order of operations. Producers who get compression wrong almost always do so because they start with the wrong parameter. They open a compressor, see the ratio knob, and start there. Ratio is not the first decision. Threshold is. You cannot make a meaningful ratio decision without first knowing how much of the signal the compressor will be affecting. Set threshold first, every time, without exception.

The complete workflow: play the track. Lower the threshold until the GR meter moves 3-6dB on the loudest moments. Now you have context. The signal is being compressed, and you can hear what the compressor is doing. Set attack to 10ms and release to 100ms as your starting points -- these are not artistic choices yet, they are reference points that let you hear the compression clearly before you begin shaping it. Listen to the result in the full mix. Now make creative decisions: does it need more transient attack (open up the attack)? Does it need more sustain (slow the release)? Is it still too dynamic (lower threshold or increase ratio)? Is it pumping (slow the release)? Every adjustment is now informed by what you are hearing rather than what you think you should be setting.

Ableton Live Logic Pro FL Studio Pro Tools

**Drum bus compression in Ableton Live 11/12:**

Group your drum tracks (Cmd/Ctrl+G). On the Group track, insert **Compressor** from Audio Effects. Set Mode to **Peak**. Lower Threshold until the gain reduction meter reads −5 to −7dB on the loudest hits. Set Ratio to **4:1**. Attack: **15ms**. Release: **Auto** (click the A button -- this is program-dependent release, ideal for drum buses). Apply makeup gain to match the original level, then A/B the Activator button. The kit should sound more unified, with the room ambience coming up between hits and the overall energy more consistent. If it pumps, slow the release manually to 150-200ms.

**Drum bus compression in Logic Pro:**

Create a Summing Stack for your drums (select all drum tracks, Shift+D). On the Stack's channel strip, insert **Compressor**. Set Circuit Type to **VCA** for clean, fast response. Lower Threshold to achieve −5 to −8dB GR on peaks. Ratio: **4:1**. Attack: **15ms**. Release: **Auto**. Knee: **0.5** (soft). Logic's Compressor shows gain reduction in the circular meter and in the gain reduction history bar at the top -- use both to calibrate. Apply makeup gain, then A/B the bypass button at matched loudness (reduce output by the makeup gain amount when bypassing for a true comparison).

**Drum bus compression in FL Studio 21:**

Route your drum mixer tracks to a single bus channel. On the bus channel, insert **Fruity Peak Controller** linked to **Fruity Peak Compressor** , or use the stock **Parametric EQ 2** with the compressor section. For the cleaner workflow: use **Maximus** on the drum bus. Set the Mid band (wideband) with Threshold at −15dB, Ratio at 4.0, Attack at 15ms, Release at 120ms. Alternatively, **FLEX** or a third-party plugin such as [FabFilter Pro-C 2](/articles/fabfilter-pro-c2-review) gives cleaner parameter control. Monitor the gain reduction readout. A/B with the Mute button on the effect chain.

**Drum bus compression in Pro Tools:**

Assign all drum tracks to a Bus, create an Aux Input receiving that Bus. On the Aux, insert **BF-76** (bundle) or **Avid Dynamics III**. For the BF-76: Input at −18dBu equivalent, Ratio at **4** , Attack at **3** (Pro Tools 1176 emulation uses 1-7 scale, 3 ≈ 15ms), Release at **4** (≈ 200ms). Adjust Input level until GR meter shows −5 to −8dB. Output level to unity, then A/B with the Bypass button. In Pro Tools, always confirm your I/O is routing correctly before trusting the GR meter -- a misrouted bus will show GR on signal that is not the bus you think you are compressing.

Session File Breakdown -- Bus Compression from Scratch

Scenario: compressing a trap drum bus for the first time, aiming for energy and cohesion without losing the 808 weight.

1Group kick, snare, hi-hats, claps, and 808 to a single drum bus. Leave the 808 on a separate aux send alongside the bus so you can compress the drums without touching the 808 sub -- 808s are rarely improved by bus compression.

2Insert a VCA-style compressor ([SSL G-Bus](/articles/waves-ssl-e-channel-review), Waves SSL G, API 2500). Set ratio to 4:1. Attack to 30ms (slow enough to let the 808 attack through). Release to Auto. Play the loop.

3Lower threshold until the GR meter reads −4 to −6dB consistently on the loudest moments. You should hear the room start to come up between hits -- this is the compression working, increasing perceived density.

4Apply makeup gain to match the pre-compression level (approximately equal to the average GR). Now A/B bypass at matched loudness. The compressed version should feel tighter and more unified. If it feels the same, threshold is too high. If the 808 is pumping, slow release further or reduce ratio to 3:1.

5Blend the 808 aux back in underneath the compressed drum bus. The 808 sub is now sitting in controlled space alongside compressed upper drums. Check mono compatibility -- sum to mono and verify the kick still hits and the 808 sub still has weight. Sidechain the 808 compressor to the kick if further low-end definition is needed.

> "I compress everything. But I use compression to make things feel natural, not compressed. The moment you can hear a compressor working, you have made it work too hard."

-- Tchad Blake, Mix Engineer (Pearl Jam, Tom Waits, Sheryl Crow) -- Sound On Sound interview, 2014

_The workflow for compression is always the same: set threshold first, establish the amount of gain reduction, then make creative decisions about attack and release based on what you hear in the full mix -- never in solo. The compressor is a finishing tool, not a starting point._

## Compression by Genre

Genre determines context, and context determines everything about how compression should behave. The transparency that defines contemporary R&B compression would be inadequate for the aggressive parallel compression that defines modern metal. The pumping sidechain that characterizes electronic dance music would destroy the natural feel of a singer-songwriter record. These are not preferences -- they are aesthetic conventions that producers and listeners have built into their expectations of each genre, and departing from them without intention reads as a mistake rather than a choice.

Genre

Ratio

Attack

Release

GR Target

Character

Trap / Hip-Hop

Ratio4:1–6:1

Attack10–20ms

Release100–200ms

GR Target4–8dB

CharacterVCA (SSL, API)

Drum bus compressed hard for density. 808 typically uncompressed. Sidechain ducking to kick is genre-defining.

R&B / Neo-Soul

Ratio2:1–3:1

Attack20–40ms

Release150–300ms

GR Target2–4dB

CharacterOptical (LA-2A)

Gentle, transparent. Vocals breathe naturally. Over-compression reads immediately as wrong in this genre.

Pop (Mainstream)

Ratio3:1–4:1

Attack10–25ms

ReleaseAuto / 150ms

GR Target3–6dB

CharacterVCA / Optical

Consistent vocal presence is the primary goal. Parallel compression on drums for punch.

EDM / House

Ratio4:1–∞:1

Attack1–10ms

Release50–150ms

GR Target6–15dB

CharacterVCA (any)

Sidechain pumping to kick is an aesthetic, not a mistake. Release timed to tempo.

Rock / Alt

Ratio4:1–8:1

Attack5–15ms

Release60–150ms

GR Target4–8dB

CharacterFET (1176)

Drums compressed aggressively. Guitars often parallel compressed for density without losing pick attack.

Lo-Fi / Bedroom Pop

Ratio3:1–6:1

Attack10–30ms

Release100–200ms

GR Target4–6dB

CharacterOptical / Vintage

Gentle compression with harmonic character. Tape saturation before compression for texture.

Jazz / Acoustic

Ratio2:1–3:1

Attack30–60ms

Release200–400ms

GR Target1–3dB

CharacterOptical / Var-Mu

Minimal compression. The natural dynamics of the acoustic performance are the aesthetic.

Drill

Ratio4:1–8:1

Attack5–15ms

Release80–150ms

GR Target6–10dB

CharacterVCA (SSL)

Aggressive drum bus compression. Sliding 808 often sidechained to the drum bus compressor.

The single most important column in this table is Character -- not the numbers. An optical compressor set to the same ratio and attack as a FET compressor will sound completely different, because the physics of the gain reduction element produce different temporal and harmonic responses. The parameters are the starting point. The topology is the destination.

Share

Copy Link[Share on X](https://x.com/intent/tweet?text=Compression+by+Genre+%E2%80%94+@mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23genre-table)[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23genre-table&title=Compression+by+Genre+%E2%80%94+@mpwikiofficial)

## Compressor Topology -- The Character Behind the Controls

Two compressors with identical parameter settings will sound different if they use different gain reduction topologies. This is not a subtle distinction. A VCA compressor at 4:1, 10ms attack, and 100ms release and an optical compressor at the same settings produce recognizably different results on the same source material -- different enough that experienced engineers reach for specific topologies for specific jobs without adjusting a single parameter, because the topology itself is the first decision. Understanding the four main topologies is what separates producers who select compressors by reputation from producers who select them by purpose.

VCA -- Voltage Controlled Amplifier

SSL G-Bus, API 2500, dbx 160, Neve 33609, Waves SSL G

Clean * Fast * Precise * Transparent

The gain reduction element is a voltage-controlled amplifier that responds to a control voltage generated by the detector circuit. The VCA can respond in microseconds, producing the fastest, most precise compression available. The sonic character is largely determined by the quality of the VCA chip and the surrounding circuitry -- high-quality VCAs are essentially transparent, adding minimal colour while achieving significant gain reduction. This makes VCA compressors the default choice for situations where control is the primary goal and the source material's character should be preserved: mix bus glue, drum buses, bus processing where cohesion matters more than colour. The SSL G-Bus compressor is the definitive VCA bus compressor -- 2:1 to 4:1, medium attack, auto release, and the mix sounds like a record.

FET -- Field Effect Transistor

UREI 1176, Purple Audio MC77, Warm Audio WA76, UA 1176

Fast * Aggressive * Present * Harmonic Color

The Field Effect Transistor produces gain reduction with a distinctive harmonic signature -- a slight saturation and presence character that adds energy to transients rather than simply reducing them. FET compressors are fast enough to respond to individual transient events while adding a quality of aliveness that purely transparent compressors do not. The 1176 is the defining instrument: its attack times extend down to 0.02ms, faster than the human ear can perceive, which means aggressive attack settings produce a kind of harmonic limiting at the transient onset rather than clean gain reduction. The All-Buttons mode -- engaging all four ratio buttons simultaneously -- creates an aggressive, saturated sound that is technically a malfunction and sonically one of the most used compressor settings in the history of recorded music. Use FET compressors when you want compression to add presence and aggression, not just control.

Optical -- Electro-Optical

Teletronix LA-2A, Tube-Tech CL1B, UA LA-2A, Pendulum OCL-2

Slow * Warm * Musical * Program-Dependent

An optical compressor uses a light-emitting element and a photoresistive cell as the gain reduction mechanism. When the signal exceeds the threshold, the light source illuminates the photocell, which increases its conductance and reduces gain. The physical properties of the system produce a response that is inherently slow, non-linear, and "program-dependent" -- meaning the compressor responds differently to sustained tones than to transients, to quiet passages than to loud ones, in ways that cannot be fully specified by a parameter sheet. It is this unpredictability, combined with the inherent warmth of tube circuitry in most optical designs, that makes the LA-2A the most beloved vocal compressor in history. There are no ratio, attack, or release controls to overthink. There is a threshold and an output level. The optical circuit handles everything else in a way that sounds like music because it responds the way human perception responds.

Variable-Mu -- Tube Compressor

Fairchild 670, Manley Variable Mu, Retro Sta-Level, Cartec EQP-1A

Slow * Warm * Saturated * Mastering Character

Variable-mu compressors use the gain of a vacuum tube stage as the gain reduction element. When a control voltage is applied to the tube's grid, it changes the tube's amplification factor -- its "mu" -- which reduces gain. The response is inherently slow: variable-mu compressors are the slowest of all topologies, with attack times that begin in the milliseconds and release times that can extend to seconds. This makes them unsuitable for transient control but uniquely suited for the slowest, most gentle form of compression -- mastering-level bus processing where the goal is warmth and glue rather than dynamic control. The Fairchild 670 is the historical gold standard: a stereo variable-mu compressor with twelve time constants and a character so distinctive that producers and engineers refer to its sound by name. The Manley Variable Mu has become the contemporary standard for mastering bus work. Variable-mu compressors do not so much control dynamics as they breathe with them.

## Hardware vs Plugin

The debate over hardware versus plugin compression is, in 2026, largely settled: modern plugin emulations are genuinely excellent, and the gap in quality between a well-designed plugin and the hardware it emulates has narrowed to the point where it matters primarily in edge cases and at the highest levels of professional production. What has not narrowed is the gap in character. Hardware compressors age, drift, and respond to temperature in ways that make every unit slightly different from every other unit of the same model -- and often slightly different from itself on different days. Plugin emulations are deterministic. They sound the same every time, on every system, in every session. For producers at most levels, this consistency is an advantage. For producers seeking the specific, unrepeatable character of a 1967 1176 that has had its capacitors drifted for fifty-five years, only the hardware will do.

Aspect| Hardware| Plugin  
---|---|---  
Sonic Character| Physical component aging, temperature drift, transformer saturation, and unit-to-unit variation produce a character that changes subtly over time and between units of the same model| Deterministic and consistent. Character is baked in at design time and does not change between sessions or systems. Some emulations model component aging; none model it dynamically.  
Recall / Repeatability| Manual recall by noting settings. Component drift means two sessions at "the same settings" may not produce identical results. Often considered a feature rather than a bug.| Perfect, instant, total. Parameters save with the project. Open the session six years later on a different computer and the compression sounds identical.  
Cost / Accessibility| Vintage 1176: $2,500-$5,000. LA-2A: $3,000-$6,000. Fairchild 670: $20,000+. Modern boutique hardware: $1,500-$4,000.| UAD 1176 collection: ~$150. Waves SSL G: $30-$60. FabFilter Pro-C 2: $179. Plugin Alliance Vertigo VSC-2: ~$100. Professional results at every price point.  
CPU / Latency| Zero latency. No CPU load. The analog signal path adds no processing delay.| Introduces latency (typically 1-4ms for non-lookahead compressors, compensated automatically by most DAWs). CPU load varies from negligible to significant for complex emulations.  
The Case for Hardware| When the specific physical character of a unit is the creative goal -- not "compression that sounds like an 1176" but specifically "this 1176 in this room with these cables on this day" -- hardware is the only option. Also when tracking live and zero-latency monitoring matters for performer feel.  
  
## Before & After

Before Compression

A drum bus without compression is a collection of individual events. The kick hits hard on beat one and softer on the & of three. The snare at the back of the room is louder in the verse where the guitars are sparse than in the chorus where they fill the space. Each hi-hat has a slightly different velocity. The room mics peak whenever a hit lands and disappear between. The kit sounds live and honest and inconsistent -- which is exactly what a live drum performance is. For many genres, this is the sound you are trying to move away from.

After Compression

With 5-7dB of gain reduction from a VCA compressor at 4:1, 20ms attack, and auto release, the drum bus becomes a unified instrument. The kick hits with consistent weight on every beat. The snare sits at the same level relative to the kick in verse and chorus. The room mics come up between hits, adding ambience and size. The hi-hats stop competing with the snare for dynamic prominence. The kit no longer sounds like a collection of individual drums -- it sounds like one rhythmic statement. This is compression doing exactly what it was designed to do.

The perceptual difference between a compressed and uncompressed drum bus is not primarily about volume. It is about coherence. The compressed bus sounds like a producer made decisions about what should be prominent. The uncompressed bus sounds like the drummer's strength and position in the room made those decisions. Neither is wrong. But in most contemporary recorded music, the former is what listeners expect to hear.

## In The Wild -- Compression You Can Hear

The best way to understand what compression sounds like at its most intentional -- and what it sounds like when it becomes the aesthetic rather than the tool -- is to hear it in context on recordings you already know. These tracks were chosen because the compression is audible, identifiable, and produces a specific emotional and sonic effect that can be studied actively. Find the timestamp. Listen with headphones. Listen to what changes and what doesn't.

Daft Punk -- One More Time (2000), _Discovery_. Produced by Daft Punk. ▶ 0:00

The most famous example of bus compression used as pure aesthetic. The entire mix pumps and breathes audibly with the kick drum -- what would be a catastrophic mix mistake in almost any other context is here the defining rhythmic and emotional character of the record. Every hit of the kick causes the compressor to clamp and release in a way that makes the mix feel like it is physically dancing. The sidechain was routed to an SSL G-Bus compressor with a release time fast enough to produce full pumping on every beat at the track's 124 BPM tempo. The fact that Daft Punk kept it this way is an artistic statement about compression as groove instrument rather than dynamic controller.

Dr. Dre ft. Snoop Dogg -- Still D.R.E. (1999), _2001_. Produced by Dr. Dre, Scott Storch. ▶ 0:00

The kick drum is a masterclass in compression for weight. Parallel compression technique: an uncompressed signal preserves the initial crack and transient impact, while a heavily compressed version adds density, weight, and sustain underneath. The blend is what makes the kick hit with both immediacy and physicality. Every hit is consistent in level and weight. The consistency is not accidental -- it is the result of gate, clip gain editing, and compression applied in sequence to remove the performance variability before any aesthetic decisions were made. Dre's approach: fix the performance first, then compress for sound.

Billie Eilish -- bad guy (2019), _When We All Fall Asleep, Where Do We Go?_. Produced by Finneas O'Connell. ▶ 0:00

A contemporary study in compression restraint. The vocal is compressed enough to be consistently intimate and present, but the breath sounds, the room sound of Finneas's bedroom, and the micro-dynamics of Eilish's performance remain audible and felt. This is optical-character compression at a low ratio -- consistent without being controlled. The bass compression is more obvious: the sub sits in a defined pocket that never moves regardless of what the rest of the track does. In the chorus, where every other element opens up, the bass stays exactly where it was. That stillness is not passive -- it is compressed confidence.

Kendrick Lamar -- HUMBLE. (2017), _DAMN._. Produced by Mike WiLL Made-It. ▶ 0:00

The compression on the snare is almost violent. A tight, aggressive attack captures the transient before releasing almost immediately, creating a characteristic chopped, clapped quality rather than the sustained crack of a natural snare hit. This is not careless compression -- it is intentional design. The snare sounds like a statement, not a drum. The contrast with the kick, which is given slightly more transient by a longer attack, makes the low end feel anchored while the snare feels urgent. The vocal sits in compression that is subtle by comparison -- enough to maintain presence over the aggressive beat without competing with it.

Frank Ocean -- Nights (2016), _Blonde_. Produced by Frank Ocean, Buddy Ross, and others. ▶ 0:32▶ 2:50

Listen at 0:32 for the vocal compression in the first section -- intimate, breathy, the optical character of program-dependent release letting the natural dynamics of Ocean's delivery come through while maintaining presence. Then at 2:50, when the track shifts to the night section: the compression character changes. The vocal feels closer, denser, more controlled. The shift in compression approach is part of the emotional architecture of the record -- the two sections of the song feel physically different partly because the compression changed how close Ocean's voice sounds to the listener's ear. Compression as spatial narrative.

Radiohead -- How to Disappear Completely (2000), _Kid A_. Produced by Radiohead and Nigel Godrich. ▶ 0:00

The counterexample. Listen for what is not there: the album sounds as if almost nothing is compressed at all. Thom Yorke's vocal has the dynamic variation of a live performance -- closer and louder on intensity, quieter and more distant on vulnerability. The strings swell without being leveled. The bass moves dynamically with the song rather than sitting in a defined pocket. This is a deliberate choice by Godrich, who prioritized the emotional truth of the performances over the consistency that compression provides. Kid A is not uncompressed -- it is compressed with exceptional restraint at exactly the points where restraint produces more emotional impact than control.

The Weeknd -- Blinding Lights (2019), _After Hours_. Produced by DaHeala, Oscar Holter, Max Martin. ▶ 0:00

A contemporary example of mix bus compression as genre definition. The entire mix has the dense, slightly pumping quality of a record engineered to sound loud and energetic on streaming at −14 LUFS normalization -- not through hyper-compression but through intelligent use of VCA bus compression that raises the average energy level without crushing the transients. The synth bass hits with consistent weight. The drums are unified without losing impact. The vocal sits confidently in the top of the mix without piercing it. This is professional pop compression -- every choice designed to maximize energy density within the constraints of streaming normalization rather than fighting those constraints.

Aphex Twin -- Windowlicker (1999), _Windowlicker EP_. Produced by Richard D. James. ▶ 0:38

At 0:38, when the beat drops: the sidechained drum compression creates a pumping that is not a groove element -- it is an anxiety element. The release time is set just long enough to create discomfort, a sense of the mix being unable to breathe normally. James used compression here not as a tool for control but as a psychoacoustic weapon, exploiting the listener's unconscious response to audible gain reduction to create unease. This is compression as composition: the settings are determined not by what sounds correct but by what produces the specific emotional effect the producer is seeking.

◆ Two Records, One Question: How Much Should Compression Breathe?

Compression as Aesthetic vs. Compression as Control

One More Time

Daft Punk -- Produced by Daft Punk (2000)

Audible -- Rhythmic -- The Compression Is the Track

The pump is not a side effect. It is the primary sonic event of the record. Every parameter decision -- the release timed to the beat, the sidechain routed to the kick, the ratio high enough to produce full pump -- was made to produce this specific audible compression effect. The compressor is a musical instrument in this mix, not a dynamic controller. Remove the audible pump and you remove what makes the record feel the way it does.

Signal Chain

CompressorSSL G-Bus style Ratio4:1-6:1 AttackFast (1-5ms) ReleaseTimed to tempo (125ms) SidechainKick drum GR8-12dB

VS

How to Disappear Completely

Radiohead -- Produced by Radiohead & Nigel Godrich (2000)

Inaudible -- Preserved -- The Absence of Compression Is the Track

The compression is invisible -- applied with such restraint that the listener perceives no gain reduction, only a performance with natural dynamic range intact. Yorke's vocal moves between quiet and loud without a compressor pulling it back. The strings swell without being leveled. The production philosophy: trust the performance. The compressor's job is to prevent problems, not to impose character. The result sounds live and vulnerable in a way that heavily compressed records cannot achieve. The absence of audible compression is itself a creative statement.

Signal Chain

CompressorOptical / transparent Ratio2:1-3:1 AttackSlow (30-60ms) ReleaseProgram-dependent SidechainNone (full-band) GR1-3dB

◆ What This Comparison Teaches

Both approaches are exactly right for their emotional context. Daft Punk needed the compression to dance. Godrich needed the compression to disappear. The lesson is that "how much compression" is never the right question. The right question is always: "what should compression be doing in this specific record for this specific emotional purpose?" The parameters follow from the answer -- not the other way around.

Share this breakdown

Copy Link[Share on X](https://x.com/intent/tweet?text=Daft+Punk+vs+Radiohead+%E2%80%94+compression+as+aesthetic+vs+control+%E2%80%94+@mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23in-the-wild)[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23in-the-wild&title=Daft+Punk+vs+Radiohead+%E2%80%94+compression+as+aesthetic+vs+control+%E2%80%94+@mpwikiofficial)

## Producer DNA -- Three Philosophies

Three engineers. The same tool. Three completely different worldviews about what compression is for. What follows are not compression tutorials -- they are portraits of how the most significant mixing engineers of the modern era think about dynamics, and what that thinking produces sonically.

◆ Producer DNA

Same Tool, Different Worlds

Three producers. Three philosophies. Three fundamentally different answers to the question: what should compression do to music?

Dr. Dre

Producer -- Snoop Dogg, Eminem, 50 Cent, Kendrick Lamar, 2Pac

Philosophy

Compression as gravity. Every element in the mix has a defined weight and position, and nothing moves from it. The kick drum hits with the same mass on beat one as it does on the last bar of the record. The bass sits in a pocket so defined you could measure it with a ruler. Dre's mixes feel like they were poured into a mold and left to set. The compression does not breathe -- it holds.

"I want everything to feel like it has weight. Like if you dropped it, it would hit the floor hard. That's what compression is for. Not to even things out -- to give everything mass."

Dr. Dre, reported in multiple production retrospectives including Rolling Stone, 2015

Signature SetupSSL G-Bus on drum bus * 4:1-6:1 * 20ms attack * Auto release * 5-8dB GR

◆ Signal Chain Breakdown _⌄_

Kick DrumGate -> EQ -> 1176 (8:1, 5ms attack, 50ms release)

808 / BassMinimal compression. Sidechain to kick only. 2:1 max.

Drum BusSSL G-Bus. 4:1. 20ms attack. Auto release. 5-8dB GR.

VocalsClip gain pre-comp. Then 3:1 optical. 2-4dB GR.

Mix Bus2:1 VCA. 40ms attack. 200ms release. 1-2dB GR only.

Philosophy in Practice

Edit first-> Gate problems-> Compress for weight-> Never compress what should breathe

Dre's critical rule: the 808 and sub bass are almost never compressed on the individual channel. The sub should move freely. Compression on the sub smears the pitch, especially on sliding 808s. The drum bus compressor handles the relationship between kick and bass at the bus level, not the channel level.

Tchad Blake

Mix Engineer -- Pearl Jam, Tom Waits, Sheryl Crow, The Black Keys, Crowded House

Philosophy

Compression as texture. Blake does not use compression primarily for dynamic control -- he uses it for the harmonic and tonal character that different compressor types impose on the signal. An optical compressor on a guitar is not there to even it out. It is there because the optical circuit adds a warmth and a slight saturation to the sustain that sounds like the guitar is alive. The settings are determined by what sounds right, not by what the GR meter says.

"I compress everything, but I use compression to make things feel natural -- not compressed. The moment you can hear a compressor working, you've made it work too hard."

Tchad Blake -- Sound On Sound interview, 2014

Signature SetupOptical compressors throughout * Low GR (1-3dB) * Program-dependent release * Tone first, control second

◆ Signal Chain Breakdown _⌄_

ApproachOptical first, VCA only when speed is essential

VocalsLA-2A or Tube-Tech CL1B. 2:1. 1-3dB GR. Never hard limiting.

GuitarsOptical for sustain character. 2:1. Threshold set for tone, not control.

DrumsOften compressed more creatively than dynamically. Room mics: heavy.

Mix BusVariable-mu (Manley). 1-2dB GR. Glue and warmth only.

Blake's Rule

Choose topology for tone-> Apply minimal GR-> If you hear it: less

Blake's key insight: the compressor's character comes through most clearly at low gain reduction settings. When you apply 8-10dB of GR with an optical compressor, you hear the gain reduction. When you apply 1-2dB, you hear the topology. His mixes have a warmth that comes from the optical character embedded in signals at near-invisible gain reduction levels.

Chris Lord-Alge

Mix Engineer -- Green Day, U2, Muse, Dave Matthews Band, Foo Fighters

Philosophy

Compression as energy. CLA's mixes hit hard, breathe fast, and translate everywhere -- from headphones to car speakers to club systems. His approach is unapologetically aggressive: fast attack FET compressors, significant makeup gain, and a philosophy that the listener should feel the mix as well as hear it. He is not interested in transparency. He is interested in impact.

"I want the music to slap you. It shouldn't sneak up on you. It should announce itself. That's what compression at the right settings does -- it makes the music feel like it means business."

Chris Lord-Alge -- Sound On Sound, Mix Engineer profile, 2007

Signature Setup1176 on everything * 8:1 commonly * All-Buttons occasionally * Heavy makeup gain * SSL G-Bus on mix bus

◆ Signal Chain Breakdown _⌄_

Snare1176\. Ratio: 8 or All-Buttons. Attack: 3 (fastest). Release: 4.

Vocals1176\. Ratio: 4. Attack: 4 (medium). Heavy makeup. Loud in mix.

Drum BusSSL G-Bus. 4:1. 15ms attack. Auto. 6-8dB GR aggressively.

Guitars1176\. Ratio: 4. Pushed hard into the compressor input.

Mix BusSSL G-Bus. 4:1. 30ms attack. Auto. 2-4dB GR. More than most.

CLA's Approach

FET everywhere-> Push into compressor hard-> Heavy makeup-> Make it hit

CLA's key principle: compression and level are not the same thing. He drives the input into the 1176 harder than most engineers, using the compressor's input gain as a pre-compression saturation stage before the gain reduction circuit engages. The result has FET character embedded in the signal before compression even begins. This is the source of the "CLA sound" -- not just what his compressors do, but how hard he pushes the signal into them.

## Signature Sounds

The following five compression sounds are not settings you copy -- they are templates you study. Each one represents a producer or engineer making a specific, intentional decision about what compression should do to a specific source in a specific musical context. Understanding why each one works is more useful than knowing the exact numbers.

The 1176 All-Buttons Snare -- John Bonham, Led Zeppelin

1176 * All Buttons In * Attack: 7 (slowest) * Release: 7 (slowest) * Output: pushed

Bonham's snare on When the Levee Breaks is the most imitated drum sound in rock history. It was recorded in the stairwell of Headley Grange with microphones at the top of the stairs, and that natural compression of the room was then processed through a 1176 in All-Buttons mode -- all four ratio buttons simultaneously engaged, creating an overdriven, unstable gain reduction that saturates the transient. The slowest attack and release settings allow the full transient through before compression engages, then hold the compression long enough that the release becomes audible. What you hear is not a snare hit. It is an event.

The LA-2A Vocal -- Motown, 1960s Soul

LA-2A * Peak Reduction: 50-60% * Gain: to taste * No other settings available

The Motown vocal sound -- intimate, warm, present, consistently close to the listener -- is substantially the LA-2A applied to voices that were already great performances. The optical circuit's program-dependent release means the compressor holds longer on sustained notes and releases faster on consonants, which is exactly what the ear wants from a vocal: vowels controlled, consonants preserved. The unit adds a warmth from its tube output stage that is audible but not identifiable as coloration. Producers of the era did not know why it worked. They knew that it did, which is the only knowledge that matters in a session.

The SSL G-Bus Glue -- Late 1980s and 1990s Commercial Mix Standard

SSL G-Bus * Ratio: 2:1-4:1 * Attack: Medium (30ms) * Release: Auto * GR: 2-4dB

Every mixing engineer working on an SSL console in the 1980s and 1990s ran their mix through the console's stereo bus compressor. The G-Bus compressor at 2-4:1 with the attack medium and release on auto produces a quality of cohesion -- the "glue" that makes a mix sound like one record rather than a collection of separately recorded tracks -- that is largely responsible for the sound of commercial music from 1985 to 2005. It is not a transparent compressor. It imparts a characteristic density and push to anything that runs through it. The entire mix sounds more intentional with 2dB of G-Bus gain reduction than without it.

The New York Parallel Drum Crush -- Hip-Hop, 2000s

FET or VCA on parallel bus * Ratio: 10:1-20:1 * Attack: 1ms * Release: 50ms * Blend: 20-40%

Parallel compression on drums -- blending a heavily compressed version of the drum bus with the uncompressed original -- was codified as a technique in New York studios in the late 1990s and became the foundation of the modern hip-hop drum sound. The crushed parallel bus adds weight, density, and sustain underneath the uncompressed transients. At 20-40% blend, the result has both the crack of unprocessed drums and the density that makes a record feel physical. The key is that the parallel is crushed far beyond what any engineer would apply directly to the drums -- 15dB+ of gain reduction at a fast attack -- because it is never heard alone. It is only heard as an additive underneath the original.

The Sidechain Duck -- Electronic Dance Music, 2000s-Present

Any compressor * Sidechain: kick drum * Ratio: 4:1-∞:1 * Attack: 1-5ms * Release: Timed to tempo

The pumping effect that defines electronic dance music -- where the entire mix ducks and surges with every kick drum hit -- is achieved by routing the kick drum's signal into the sidechain detection path of a compressor processing the rest of the mix, or specifically the pads and sustained elements. When the kick hits, the sidechain triggers gain reduction on everything else, clearing space for the kick's sub frequencies and creating the characteristic forward momentum of the genre. The release timing is the creative decision: set to tempo, it creates a musical pump. Set too fast, it creates an uncontrolled jitter. The technique was popularized by Daft Punk and codified by the commercial EDM era. In 2026, it is so standard that productions without it in certain genres sound wrong to trained ears.

## Types of Compression

Compression describes a family of related dynamic processing techniques that share the same core mechanism -- gain reduction above a threshold -- but apply it in fundamentally different ways for different purposes. Understanding which type of compression serves which creative goal prevents the most common error in dynamic processing: using the right tool wrong because all the tools share a name.

Standard (Downward) Compression

SSL G-Bus, 1176, LA-2A, any standard compressor

The default. Reduces gain when the signal exceeds the threshold. The loudest moments are turned down; makeup gain brings the average level back up. Used on virtually every element in a professional mix in some form. The question is never whether to use it but how much and with what character.

Parallel Compression

Any compressor on a parallel/aux bus

Blends a heavily compressed version of a signal with the uncompressed original. Transients are preserved in the dry signal while density, sustain, and weight come from the compressed signal. The blend ratio controls how much of each is heard. The foundation of modern hip-hop and rock drum sounds.

Sidechain Compression

Any compressor with an external sidechain input

Uses an external signal to trigger gain reduction rather than the compressor's own input. The classic application: a kick drum sidechains a bass compressor, causing the bass to duck every time the kick hits. In electronic music, [sidechain compression](../articles/sidechain-compression-guide) to the kick drum creates the pumping effect that defines the genre.

Multiband Compression

FabFilter Pro-MB, Waves C6, [iZotope Ozone](/articles/izotope-ozone-12-review) Dynamics

Splits the signal into frequency bands and compresses each independently. A loud low-mid build-up in a vocal does not trigger compression on the high frequencies. Used in mastering for surgical dynamic control of specific frequency problems. Misused in mixing when broadband compression fails to solve a problem that requires editing or EQ instead.

Mid-Side Compression

FabFilter Pro-C 2 (M/S mode), any M/S capable compressor

Processes the Mid (mono center) and Side (stereo width) components of a signal independently. Compressing the sides more than the mid narrows the stereo image under loud conditions, keeping the mix centered and mono-compatible. Compressing the mid more aggressively can push elements to the edges. Used primarily in mastering and advanced mix bus processing.

Limiting

FabFilter Pro-L 2, Waves L3, iZotope Ozone Maximizer

Compression at ratios above 10:1 -- effectively a ceiling. Nothing above the threshold passes at full level. True-peak limiting ensures no sample exceeds 0dBFS or −1dBFS. Used as the final stage in mastering to control peaks for streaming delivery. Not a creative tool; a technical safety stage. The loudness of a master is determined by what comes before the limiter, not by how hard you push into it.

Compression vs. Limiting

Compression manages the dynamic range of a performance -- it is a creative and tonal decision. Limiting manages the ceiling of a master -- it is a technical and delivery decision. A compressor at 10:1 can still allow peaks to exceed the threshold by up to 10dB. A limiter allows nothing through. Use compression during mixing to shape sound. Use limiting during mastering to set the final delivery ceiling. They are different jobs.

Compression vs. Saturation

Compression reduces the amplitude of loud signals. Saturation adds harmonic distortion -- overtones at multiples of the fundamental frequency -- which makes signals sound fuller and louder without reducing dynamic range. Both can make things sound "thicker" but through opposite mechanisms. Compression takes away. Saturation adds. The best-sounding mixes typically use both in sequence: compress for consistency, saturate for character. Confusing one for the other produces a mix that is either compressed and thin or saturated and dynamic when neither was the intent.

## The Producer's Verdict

◆ The Producer's Verdict ◆

If you could only remember six things about compression mid-session, remember these. Not because they cover everything -- they do not. Because they cover the decisions that determine whether your compression serves the music or works against it.

Starting Ratio 4:1 Every ratio decision is a departure from 4:1. Move to 2:1 for transparency and glue. Move to 8:1 for control and density. Go above 10:1 only when limiting is the actual goal. The ratio without the threshold context is meaningless -- set threshold first, always.

Starting Attack 10ms Ten milliseconds lets most transients through before compression engages. Faster for more control, less punch. Slower for more punch, less control. On sources with no meaningful transient -- sustained pads, bowed strings -- attack matters less than ratio and threshold. On everything with a transient onset, attack is the most creative parameter you have.

Starting Release Auto or 100ms Auto release is program-dependent and is almost always the best starting point for bus processing. For individual channels, 100ms is a reference point that avoids both pumping (too fast) and smearing (too slow). Adjust toward the tempo: at 120 BPM, one beat is 500ms. A release of 300-500ms on a drum bus will feel musical before any further adjustment.

GR Target 3-6dB Individual channels: 3-6dB of gain reduction is the professional standard for most sources. Mix bus: 1-3dB maximum -- bus compression is glue, not control. Drum bus: 4-8dB is appropriate for aggressive shaping. When gain reduction consistently exceeds 10dB, you are solving a performance problem with a processing solution. Edit first.

Topology First Choose before dialing Two compressors at identical settings sound different if they use different gain reduction topologies. Choose the topology before adjusting parameters: VCA for clean control, FET for presence and aggression, optical for warmth and program-dependent musicality, variable-mu for mastering glue. The topology is the first creative decision. The parameters are refinements of it.

A/B Rule Matched loudness only Compressed signals sound better than uncompressed signals at equal level simply because compression raises average loudness. Always match output level to input level before A/B testing. Reduce the output by the approximate amount of makeup gain when bypassing. If the compressed version still sounds better at matched levels, the compression is working. If not, there is less gain reduction than you need, or more than the material can support.

Compression is not a finishing touch. It is a structural decision made at the same time as every other structural decision in a mix -- level, panning, EQ, space. The producer who approaches it as a polish step is always working from a foundation that would have been stronger if the compression had been set first.

Share the verdict

Copy Verdict[Share on X](https://x.com/intent/tweet?text=Compression+Producer%27s+Verdict+%E2%80%94+@mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23verdict)[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression%23verdict&title=Compression+Producer%27s+Verdict+%E2%80%94+@mpwikiofficial)

## Plugin Recommendations

These are not ranked by price or popularity. They are ranked by the quality of the result relative to the investment, and by the likelihood that a producer who owns them will get consistently professional compression without spending sessions fighting the tool. The free tier will get you to a professional result on any budget. The mid tier adds the character options that separate productions that sound good from productions that sound specific. The pro tier is for producers who know exactly which hardware sound they need and want the most accurate emulation of it available in software.

♦ Free -- No Excuses

Ableton Compressor / Logic Compressor Native DAW The stock compressor in both DAWs is genuinely excellent. Logic's Compressor has switchable circuit types (Platinum Digital, Studio FET, Studio VCA, Vintage FET, Vintage Opto, Vintage VCA) that produce meaningfully different characters. Ableton's Compressor is transparent and fast. Both are professional tools. If you are avoiding them because they are stock, stop. Use them until you hear a specific sonic problem they cannot solve, then upgrade.

TDR Kotelnikov Tokyo Dawn Records A stereo bus compressor of genuinely professional quality at no cost. Transparent, musical, with a well-designed interface. The GE (Gentleman's Edition) paid upgrade adds mastering-grade stereo linking control, but the free version is sufficient for mixing bus work at any level.

DC1A Klanghelm Four knobs. Sounds incredible on vocals, bass, and anything needing a warm, character-rich compression that does not want to announce itself. The simplicity forces good habits. If you find yourself wishing for more control, you probably need less compression, not more knobs.

♦ Mid -- The Working Producer Stack

FabFilter Pro-C 2 FabFilter -- ~$179 The most complete [compressor plugin](/articles/best-compressor-plugins) available. Eight compression styles (Clean, Classic, Opto, Vocal, Mastering, Bus, Punch, Pumping), full M/S mode, a large GR meter, and one of the clearest, most useful interfaces in plugin history. If you are going to own one mid-tier compressor that does everything, this is it. The visual feedback alone teaches compression faster than any tutorial.

Waves SSL G-Master Buss Compressor Waves -- ~$30-60 on sale The SSL G-Bus sound in software. Not perfect hardware emulation, but the compression character is recognizable and the mix bus glue it produces is genuine. Waves perpetually discounts their plugins. Never pay list price. This is the standard mid-price bus compressor for a reason.

Waves CLA-76 Waves -- ~$30-60 on sale The 1176 emulation that most producers reach for first. Two versions: the Blacky (later model, cleaner) and the Bluey (earlier model, more character). The All-Buttons mode is included and sounds close enough to the hardware to be genuinely useful for the snare, vocal, and room mic applications where the 1176 is the standard choice.

♦ Pro -- When You Know What You Need

UAD 1176 Collection Universal Audio -- ~$150 (requires UAD hardware or UA Sphere) The definitive 1176 emulation. Models the Revision A, D, E, and AE variants with component-level accuracy. If your music needs the specific FET character of a 1176 -- and if you work in rock, hip-hop, R&B, or any genre built on the sound of the past sixty years of recording, it probably does -- this is the standard. The All-Buttons mode is the most accurate emulation of the hardware mode available in software.

UAD LA-2A Collection Universal Audio -- ~$150 (requires UAD hardware or UA Sphere) The LA-2A optical emulation that has replaced the hardware in most professional studios that do not own a physical unit. The Silver, Grey, and Blue variants model different production runs with different character. On vocals, it produces the program-dependent optical smoothness of the hardware with enough accuracy that the engineers who know both cannot consistently identify which they are using on a blind test.

Plugin Alliance Vertigo VSC-2 Plugin Alliance -- ~$100 The Vertigo Sound VSC-2 hardware is one of the finest mix bus VCA compressors built in the modern era, used on mastering and mixing sessions at the highest level of the industry. The Plugin Alliance emulation is close enough to serve as the primary bus compressor in sessions where the SSL G-Bus has already been used on the drum bus and something with a different character is needed for the stereo master.

## Common Mistakes

Setting ratio before threshold

The ratio controls how hard the compressor grabs. The threshold controls when it grabs. Ratio without threshold context is meaningless. A 10:1 ratio with a high threshold does almost nothing. A 2:1 ratio with a very low threshold compresses continuously. Set threshold until the GR meter moves 3-6dB on the loudest material. Then decide whether more or less ratio serves the sound. Not before.

Attack too fast on percussive sources

A fast attack -- 1-3ms -- on a kick or snare clamps the transient before the listener hears it. The initial impact that makes the drum hit feel immediate and physical is reduced before it has time to register. The source sounds controlled, flat, and slightly blunt. The fix is almost always to open the attack time: 10-20ms for most drums, 20-30ms for the drum bus. The transient needs to pass through before the compressor grabs it.

Release too fast, causing pumping

When the release is too fast for the tempo and material, the gain reduction releases loudly enough between musical events that the listener hears the gain coming back up. This is pumping. It is not subtle -- once you hear it, you cannot unhear it. The fix is slowing the release by 50ms at a time until the pumping stops. In most mixing applications, 100-200ms of release time prevents pumping without creating the opposite problem of smearing events together.

Judging compression loudness in solo

A compressed signal always sounds impressive in solo -- it is louder, denser, and more present than the uncompressed version. None of these qualities tell you whether the compression is working in the mix. Set every compression parameter with the full mix playing. The only valid A/B test is a bypass at matched loudness in the context of the complete arrangement. Solo compression calibration is noise.

Using compression to fix a performance problem

Compression evens level. It does not fix pitch, timing, or emotional commitment. A vocal with inconsistent dynamics and inconsistent tuning, heavily compressed, becomes a consistently present, consistently out-of-tune vocal. Edit first: clip-gain loud sections down and quiet sections up until the dynamic range is manageable. Then apply gentle compression to refine the result. Compression is a finishing tool. It makes a good performance great. It makes a bad performance louder and more prominent.

Compressing every channel equally

Not every element in a mix needs the same amount of compression -- or any compression at all. Sustained synth pads with programmed dynamics need very little. A live vocal needs significant management. A perfectly recorded acoustic guitar might need nothing. The instinct to insert a compressor on every channel and apply roughly the same settings is not a mixing workflow. It is a ritual that substitutes for listening. Ask what each channel needs before inserting anything on it.

## Compression Translation Test

Compression problems translate differently on different playback systems. A pumping mix bus sounds catastrophic on studio monitors and may go completely unnoticed on earbuds. A vocal that is barely audible on laptop speakers because the compression has flattened its presence against the instrumentation may sound fine on headphones. Use this checklist before sending a mix. Each system reveals a different compression failure mode.

◆ Interactive

Compression Translation Test

Check your mix on each system. Tick every symptom you hear. Get the fix.

🎙 Studio  
Monitors ✓ 💻 Laptop  
Speakers ✓ 📱 Phone  
Speaker ✓ 🎧 Ear­buds ✓ 🚘 Car  
Stereo ✓

What to listen for

Studio monitors reveal the full frequency range including deep sub. They show pumping clearly. They expose attack settings that are too fast or slow. Use monitors for calibrating your compression settings before checking other systems.

Symptoms on Studio Monitors

The mix pumps or breathes audibly with the kick

Fix

Release too fast on the mix bus or drum bus compressor. Slow the release 50ms at a time until the breathing stops being audible. Target 150-300ms on a drum bus, 250-400ms on a mix bus.

Mark Fixed ✓

Kick and snare lost punch -- they hit but do not impact

Fix

Attack too fast on the drum bus or individual drum channels. Open the attack to 15-25ms on the drum bus to let the transient through before compression engages. Check individual channel attack settings as well -- the problem compounds across multiple compressors in the chain.

Mark Fixed ✓

Sub and bass feel heavy but unclear

Fix

Mix bus compressor's slow attack is letting the sub transients through, then clamping the sustain. Alternatively: too much GR on the mix bus is creating an imbalance between compressed and uncompressed frequency energy. Check mix bus GR -- if above 3dB, reduce. Check bass channel compression separately.

Mark Fixed ✓

What to listen for

Laptop speakers have limited low-end reproduction and small drivers that struggle with dynamic range. They reveal whether a compressed mix retains clarity at low loudness levels and whether heavy compression has collapsed the mix into a wall of sound where nothing is distinct.

Symptoms on Laptop Speakers

Kick feels absent or disappears into the mix

Fix

Over-compression on the drum bus or mix bus is collapsing the low-mid click of the kick that small speakers reproduce. On laptop speakers, you hear attack transients more than sub frequencies. Increase attack time to preserve the kick's initial transient. Also check that the kick is present at 80-120Hz where small speakers have some response.

Mark Fixed ✓

Everything sounds equally loud -- no separation

Fix

The mix has been over-compressed to the point where all elements sit at similar dynamic levels. There is no foreground and background, no sense of depth. Reduce gain reduction across multiple channels. The vocal should still be clearly louder than the guitars on a small speaker. If it is not, the compression has eliminated the level differences that create a mix's sense of arrangement.

Mark Fixed ✓

What to listen for

Phone speakers are the final test of vocal clarity and intelligibility. They emphasize midrange and struggle with everything below 200Hz and above 8kHz. A vocal that cannot cut through on a phone speaker will not reach the majority of streaming listeners.

Symptoms on Phone Speaker

Vocal sounds inconsistent or gets buried in choruses

Fix

Insufficient vocal compression for the track density. The vocal needs slightly more consistent gain reduction to maintain presence when the arrangement thickens. Increase compression on the vocal by 1-2dB GR, or apply a second gentle compressor in series. Also check that the vocal compressor's release is not holding too long in the chorus, causing the vocal to sit below the level needed to cut through.

Mark Fixed ✓

Mix sounds suffocating or overly dense

Fix

The limited frequency reproduction of phone speakers makes over-compressed mixes feel claustrophobic. The midrange density that studio monitors spread across the frequency spectrum is collapsed into a narrow band. Reduce mix bus GR to 1dB maximum. Check that individual channels are not all compressing simultaneously, which creates a wall of midrange density rather than a mix with dynamic and spatial depth.

Mark Fixed ✓

What to listen for

Earbuds (especially modern sealed ANC earbuds) have surprisingly good low-end reproduction and excellent transient clarity. They reveal compression artifacts that are masked on larger speakers. They are the most revealing test for attack settings that are too aggressive.

Symptoms on Earbuds

Transients sound clipped or distorted on hits

Fix

A compressor with too-fast an attack is clamping the transient aggressively enough to produce an audible artifact at the onset. On earbuds with good transient resolution, this sounds like a brief distortion or click on drum hits. Open attack time by 5ms increments until the artifact disappears. Also check for inter-sample peaks if a limiter is in the chain -- inter-sample distortion is clearly audible on earbuds.

Mark Fixed ✓

Mix feels suffocating -- hard to listen for more than a few minutes

Fix

Listening fatigue from over-compression. Heavy compression raises average loudness level while removing the dynamic variation that gives the ear periodic rest. On sealed earbuds this is exacerbated. Reduce overall compression across the mix. The mix should not feel like it is working to maintain its own loudness at all times. Some dynamic breathing between sections is not a mistake -- it is what makes extended listening comfortable.

Mark Fixed ✓

What to listen for

A car stereo at road volume is the real world test. Road noise masks detail in the 200-800Hz range. The car's acoustic space emphasizes certain frequencies and masks others. A mix that sounds balanced in a quiet studio can feel bottom-heavy, thin, or vocally unclear at road volume with background noise.

Symptoms in Car

Low end feels uncontrolled or bass overtakes the mix

Fix

The car's acoustic reinforcement of certain low frequencies is exposing under-compression of the bass. The bass has more dynamic variation than the compressed drums, so it feels inconsistent against the controlled kick. Increase bass channel compression slightly -- 4:1, 3-5dB GR -- and consider sidechaining the bass compressor to the kick for tighter kick/bass relationship. Road noise also masks the kick's fundamental, making the bass seem disproportionately loud.

Mark Fixed ✓

Vocal gets buried at moderate volume

Fix

Road noise masks the midrange frequencies where vocal presence lives. The vocal compression that sounded perfect in a quiet studio is insufficient to maintain presence against a noisy background. Add a gentle second compressor on the vocal at 2:1, 2-3dB GR. Alternatively, automate the vocal level up 1-2dB in sections where the arrangement is thickest. The car is the honest test of whether a mix works at the volume and environment most listeners actually use.

Mark Fixed ✓

## Red Flags & Green Flags

#### ▴ Red Flags -- Stop and Reconsider

  * The GR meter is pegged at −10dB or more consistently. You are solving a performance problem with compression and making both worse.
  * You can hear the compressor working on every beat and it was not an intentional creative choice. Release is too fast for the tempo.
  * The mix sounds better when you bypass the mix bus compressor. You have over-compressed individual channels and the bus is exposing it.
  * You are using compression instead of editing. Nothing above 6-8dB of GR is compression doing its job. It is compression masking a problem.
  * The compressed signal sounds better in solo but worse in the mix. You are compressing for solo performance, not mix performance -- wrong context.
  * You are applying the same compression settings to every channel. Drums and vocals and synths have different dynamic profiles. They need different approaches.
  * The mix sounds loud on the meter but flat to the ear. Makeup gain is lying to you. Match levels and listen again.



#### ▼ Green Flags -- You Are On the Right Track

  * The mix sounds slightly looser and less controlled when you bypass the compressor -- not flat, not different, just less settled. That is the correct amount.
  * You can bypass the compressor and only notice it after several seconds of listening -- not immediately. The compression is serving the music, not announcing itself.
  * The GR meter moves 3-6dB on the loudest moments and sits near zero on quiet passages. The compressor is responding to dynamics, not flattening them.
  * The drum bus sounds like one instrument rather than seven separate drums -- unified without losing the individual character of each element.
  * The vocal sits at a consistent distance from the listener throughout the track, close and present without ever feeling pushed or artificial.
  * The mix translates -- sounds essentially the same on headphones, in the car, and on laptop speakers. Not identical, but balanced and intentional on all three.
  * You can explain why every compressor in the mix is there -- what specific dynamic problem it is solving or what specific tonal character it is contributing. If you cannot explain it, bypass it.



## Learning Progression

Beginner

You can insert a compressor, set threshold until the GR meter moves, and apply makeup gain. You are working from the quick reference table and starting at 4:1, 10ms attack, 100ms release for everything. You understand that compressing in solo produces misleading results and you are resisting the habit. You are making one compression decision at a time and A/B-ing each one before moving forward.

Your immediate next step: spend one full mix session compressing only the drum bus and the vocal. Nothing else. Listen to what a single, well-calibrated compressor does to the relationship between those two elements. Every other channel should run through uncompressed until you can consistently explain what those two compressors are doing and why you chose the settings you did.

Intermediate

You make topology decisions before parameter decisions. You reach for an optical compressor on vocals as a default and understand why. You understand the interaction between release time and tempo and you match them before making any other release decision. You are comfortable with parallel compression on drums and you know how to set the blend by ear rather than by number. You have learned that less compression on individual channels means better mix bus compression results.

At this level the biggest remaining gap is usually this: you are still using compression to control dynamics when you should be editing first. A vocal that needs 8dB of compression to sound consistent needs editing. Compress it to 3dB, accept the remaining inconsistency, and automate the fader for what the compressor cannot manage. The mix will sound more alive and the compression will sound more professional.

Advanced

You use compression as a compositional tool alongside automation and arrangement decisions. You make deliberate choices about where compression breathes and where it holds. You use sidechain compression not just as a ducking tool but as a rhythmic element. You understand mid-side compression well enough to use it at the mastering stage and occasionally on wide stereo sources during mixing. You can reverse-engineer a compressor setting from a reference track by ear.

The advanced frontier: frequency-dependent sidechain compression, where the sidechain signal is high-passed or band-passed before hitting the detector, so only specific frequency content triggers gain reduction. A common application is high-passing the sidechain of a drum bus compressor at 80Hz, preventing the kick sub from triggering disproportionate gain reduction at low frequencies while the attack and mid content still triggers normally. This gives the drum bus more control over the mids and highs while the sub moves more freely.

## Frequently Asked Questions

What ratio should I use for compression? +

Start at 4:1 for almost everything. It is enough to hear what the compressor is doing without destroying dynamics. Move to 2:1 for subtle control on bus processing, 6:1-8:1 for heavy drum shaping, and above 10:1 only when limiting is the goal. The ratio is meaningless without the threshold set first -- set threshold until the GR meter moves 3-6dB, then decide whether more or less ratio serves the sound.

What does attack do on a compressor? +

Attack controls how quickly the compressor begins reducing gain after the signal crosses the threshold. A fast attack (1-5ms) catches transients and reduces punch -- the initial hit is softened before the listener hears it fully. A slower attack (10-30ms) lets the initial transient pass through before gain reduction begins, preserving the crack and snap that makes drums feel alive. Start at 10ms and adjust by ear: slower for more punch, faster for more control.

Why does my mix sound pumping or breathing? +

Pumping is caused by a release time that is too fast relative to the tempo. The compressor releases between hits loudly enough that you can hear the gain coming back up. Set release to Auto if available, or manually to 80-150ms as a starting point. On bus compression, try 200-400ms. Also check that ratio is not above 4:1 on the mix bus -- higher ratios make pumping more audible at the same release setting. Slow the release by 50ms increments until the breathing stops being perceptible.

Should I compress before or after EQ? +

Both are valid and produce different results. EQ before compression means the compressor responds to the tonal balance you have established -- a boosted frequency will trigger more gain reduction. EQ after compression means you shape the compressed sound tonally. The most common professional approach: corrective EQ before compression (remove problems), creative EQ after compression (add character). Neither order is categorically correct. The question is which result serves the track.

What is parallel compression? +

Parallel compression blends a heavily compressed version of a signal with the uncompressed original. The uncompressed signal preserves transients and natural dynamics. The compressed signal adds density, sustain, and weight underneath. The blend ratio determines how much of each character comes through. It is the technique behind the full yet punchy drum sound in most modern hip-hop, R&B, and rock production. The parallel bus is often compressed far more aggressively than you would ever apply directly -- 10-20dB of gain reduction at a fast attack -- because it is never heard alone.

What is sidechain compression? +

Sidechain compression uses an external signal to trigger the gain reduction of a compressor rather than the compressor's own input. The most common application: routing a kick drum into the sidechain of a bass compressor so the bass ducks every time the kick hits, clearing low-end space. In EDM and electronic music, the kick sidechain on pads and synths creates the pumping rhythmic effect that defines the genre. The sidechain signal triggers the compression; the source signal receives the gain reduction.

How much gain reduction is too much? +

On individual channels, 3-6dB of gain reduction is the professional standard for most sources. On a mix bus, 1-3dB is enough -- bus compression is about glue, not control. On a drum bus, 4-8dB can be appropriate for aggressive shaping. When gain reduction consistently exceeds 10dB, you are likely solving a performance problem with a processing solution. Edit the performance first: clip-gain loud moments down before compression touches the signal.

Why does my compressed mix sound quiet even with makeup gain? +

Makeup gain is volume, not loudness. After heavy compression, the dynamic peaks that made the mix feel energetic are gone. Adding makeup gain brings the level back but cannot restore the peaks. The mix sounds loud on a meter and flat to the ear. The fix is less compression, not more makeup gain. Aim for 3-6dB GR maximum, use a slower attack to preserve transients, and judge the result at equal loudness by matching levels when bypassing.

## Related Guides & Tools

[Best Compressor PluginsDiscover the best compressor plugins of 2026 — expert reviews of FabFilter Pro-C2, UAD 1176,…](/articles/best-compressor-plugins)[Sidechain Compression DesignerFree sidechain compression designer. Calculate BPM-synced release times, choose between…](/tools/sidechain-compression-designer)[FabFilter Pro-C 2 ReviewFabFilter Pro-C 2 review: eight compression styles, sidechain EQ…](/articles/fabfilter-pro-c2-review)[Waves Renaissance Compressor ReviewWaves Renaissance Compressor review 2026: Opto vs Electro modes, ARC…](/articles/waves-renaissance-compressor-review)

## Also in The Bible

[ Limiting Compression above 10:1 -- what happens when you need a ceiling, not a slope ](/bible/limiting) [ Parallel Compression Blending crushed and dry signals for density without loss of transient impact ](/bible/parallel-compression) [ Sidechain Compression Using an external signal to trigger gain reduction -- kick-to-bass ducking explained ](/bible/sidechain-compression) [ Gain Staging Managing signal level through every stage in the chain -- what you set before compression ](/bible/gain-staging) [ Dynamic Range The distance between the quietest and loudest moments -- what compression reduces ](/bible/dynamic-range) [ Attack & Release The time parameters that determine compression character and musical feel ](/tools/attack-release-calculator) [ Bus Compression Applying compression to a group of instruments simultaneously for cohesion ](/bible/bus-compression) [ Multiband Compression Independent compression per frequency band -- the mastering standard ](/bible/multiband-compression) [ Saturation Harmonic distortion as the alternative to compression for density and warmth ](/bible/saturation) [ Noise Gate Silence below a threshold -- the inverse of compression ](/bible/noise-gate)

Was this entry useful in your session?

👍 Yes -- helped mid-session 👌 Partially [✎ Suggest an improvement](mailto:team@musicproductionwiki.com?subject=Compression+Bible+Entry+Feedback)

Last verified by MusicProductionWiki editorial -- May 2026 * 2026 Edition

#### In This Entry

Definition How It Works New Producers Parameters Quick Reference GR Calculator Signal Chain Fix It History How To Use By Genre Topology Hardware vs Plugin In The Wild Producer DNA Signatures Types Verdict Plugins Mistakes Mix Test Flags Progression FAQ Related Terms

#### The Producer's Briefing

Production technique, gear, and music business -- weekly.

[Sound Better ->](https://theproducersbriefing.beehiiv.com)

### Producer Spotlight

Dr. Dre

Producer, Engineer

Compression as gravity -- every element holds its position

Tchad Blake

Mix Engineer

Optical compression for warmth -- 1-3dB GR, topology as tone

Chris Lord-Alge

Mix Engineer

FET compression for energy -- push hard, make it hit

Quick Start

1\. Set threshold: GR meter moves 3-6dB  
2\. Ratio: start 4:1  
3\. Attack: start 10ms  
4\. Release: Auto or 100ms  
5\. Makeup gain to unity  
6\. A/B bypass at matched levels  
7\. Adjust by ear in full mix only 

#### Share This Entry

Copy Link [Share on X](https://x.com/intent/tweet?text=Compression+%E2%80%94+The+Producer%27s+Bible&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression) [Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression&title=Compression+%E2%80%94+The+Producer%27s+Bible)

[◆ All Bible Entries ->](/bible/)

The Producer's Briefing

Production technique, gear analysis, and music business -- every week.

[Subscribe Free ->](https://theproducersbriefing.beehiiv.com)

◆ Cite This Entry

MusicProductionWiki Citation Reference

For academic papers, course materials, and institutional use. Select your format below.

Last Reviewed

May 27, 2026

DOI

Pending

APA 7th Edition

Copy APA

MusicProductionWiki Editorial Team. (2026). Compression. In _The Producer 's Bible_. MusicProductionWiki. https://musicproductionwiki.com/bible/compression

MLA 9th Edition

Copy MLA

MusicProductionWiki Editorial Team. "Compression." _The Producer 's Bible_, MusicProductionWiki, 27 May 2026, musicproductionwiki.com/bible/compression.

Chicago 17th Edition

Copy Chicago

MusicProductionWiki Editorial Team. "Compression." _The Producer 's Bible_. MusicProductionWiki, May 27, 2026. https://musicproductionwiki.com/bible/compression.

Harvard

Copy Harvard

MusicProductionWiki Editorial Team (2026) 'Compression', _The Producer 's Bible_. MusicProductionWiki. Available at: https://musicproductionwiki.com/bible/compression (Accessed: 27 May 2026).

Institutional Licensing

For use of Bible entries in course materials, curricula, or academic publications, contact [team@musicproductionwiki.com](mailto:team@musicproductionwiki.com). Licensing terms available for educational institutions and DAW companies.

Editorial Standards

All Bible entries are reviewed by the MusicProductionWiki Editorial Team. Producer quotes are cited with source and date. Technical claims are cross-referenced against primary sources. Last reviewed: May 27, 2026.

◆ Structured Learning Path

What to Read Next

Compression sits at the center of dynamics. Reading these in order builds the complete picture.

[ Before You Compress Gain Staging Set levels correctly before compression touches the signal ](/bible/gain-staging) [ Next Level Parallel Compression Density without destroying transients ](/bible/parallel-compression) [ Creative Application Sidechain Compression Kick-to-bass ducking and rhythmic pumping ](/bible/sidechain-compression) [ Final Stage Limiting What happens when compression becomes a ceiling ](/bible/limiting) [ Pairs With EQ Order matters — before or after compression changes everything ](/bible/eq) [ The Alternative Saturation Density and warmth through harmonic addition, not subtraction ](/bible/saturation)

◆ Version History

Changelog

v1.2 May 27, 2026 Major Update

+**Added:** Institutional Citation Block -- APA, MLA, Chicago, and Harvard citations pre-formatted with one-click copy.

+**Added:** What to Read Next -- structured learning path linking to 6 adjacent Bible entries.

+**Added:** 8 strategic share bars across the entry including after New Producers, Calculator, Genre Table, In The Wild, and Verdict.

->**Fixed:** Fix-It diagnostic converted to accordion -- result appears directly under selected symptom, no page jump.

->**Fixed:** Entry nav upgraded to IntersectionObserver with active pill auto-centering. Genre table mobile row height. GR Calculator 4-column grid stacks 2×2 on mobile.

v1.0 May 27, 2026 Initial Build

Compression flagship entry. 25 sections. GR Calculator, Fix-It diagnostic (8 symptoms), Mix Translation Test (5 systems), Producer DNA (Dre, Tchad Blake, CLA), compressor topology grid (VCA/FET/Optical/Variable-Mu), Daft Punk vs Radiohead comparison showcase, 8 In The Wild track analyses, 5 JSON-LD schema blocks.

Changes logged by the MusicProductionWiki Editorial Team. To suggest a correction: [team@musicproductionwiki.com](mailto:team@musicproductionwiki.com)

[◆ The Producer's Bible](/bible/)

MusicProductionWiki.com

The most comprehensive music production reference on the internet.

[Share on X](https://x.com/intent/tweet?text=Compression+%E2%80%94+The+Producer%27s+Bible&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression) [Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fcompression&title=Compression+%E2%80%94+The+Producer%27s+Bible)

[Home](/) * [About](/about) * [Producer's Bible](/bible/) * [Techniques](/categories/techniques)

(C) 2026 MusicProductionWiki.com -- Built for producers, by producers.

↑
