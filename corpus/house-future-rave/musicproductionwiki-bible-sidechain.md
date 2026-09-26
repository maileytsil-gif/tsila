---
titre: "Music Production Wiki — Bible : Sidechain (seuil, attaque, release, ratio, HPF de détection, tableau de départ, release calé au tempo : 128 BPM = 469 ms)"
source: https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/sidechain.html
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

[The Producer's Bible](/bible/) Published by MusicProductionWiki.com 2026 Edition

  1. [Home](https://musicproductionwiki.com)
  2. ›
  3. [The Producer's Bible](https://musicproductionwiki.com/bible/)
  4. ›
  5. Sidechain



Signal Processing noun · dynamic control 2026 Edition

# Sidechain

/ˈsaɪdtʃeɪn/

Quick Answer Definition How It Works Parameters Quick Reference History How To Use It In The Wild Types Mistakes Calculator Related Further Reading FAQ

Sidechain is a secondary audio path that feeds a detector circuit—typically inside a compressor or gate—allowing one signal to control the dynamic processing applied to another signal entirely.

Hear The Difference

Dry vs Processed — Sidechain

🎵 Audio examples coming soon — check back shortly.

Dry Processed

## 01 Definition

The kick drum doesn't just hit—it moves the entire mix out of its way. That's not luck. That's sidechain.

A **sidechain** is a secondary signal path that feeds the detection or control circuit of a dynamic processor—most commonly a compressor, gate, expander, or de-esser—with audio that is separate from the signal actually being processed. In standard compression, the detector circuit that measures level and triggers gain reduction listens to the same audio it's affecting. Sidechain routing breaks that link: the processor still acts on the primary audio path, but it takes its cues from an entirely different source. The result is that signal A can control the dynamic behavior of signal B without ever being heard itself.

The term derives from analog circuit architecture. In early hardware compressors, the gain control element—whether a VCA, optical cell, FET, or vari-mu tube—was driven by a secondary control voltage generated inside a dedicated detection loop. Engineers discovered that by inserting audio into this loop externally, they could make the compressor respond to virtually anything: a vocal triggering gain reduction on a reverb return, a kick drum ducking a bass guitar, a broadcaster's voice automatically lowering background music. This external access point became known as the _sidechain input_ or _key input_ , and the technique of exploiting it became one of the defining tools of professional mixing and sound design.

In modern production, sidechain processing falls into two broad functional categories. The first is **transparency** —using sidechain routing to solve problems the listener should never notice, such as a compressor keyed to a de-essed signal so that only sibilant content triggers gain reduction, or a bass compressor responding to the kick's attack so the low end coheres without masking. The second is **effect** —deliberately audible pumping, breathing, and rhythmic volume modulation that have become foundational textures in electronic music, from French house and techno to modern pop and hip-hop. In both cases, the underlying mechanism is identical: a control signal determines the behavior of a processing chain applied to a different audio signal.

It is important to distinguish the sidechain _input_ from the sidechain _filter_. The sidechain input determines _what_ signal drives the detector. The sidechain filter—also called the high-pass filter or key listen filter—shapes that incoming detector signal before it reaches the level-detection circuit, allowing the producer to make the compressor more or less sensitive to specific frequency bands without changing what is being compressed. Both tools are often present on the same processor, and understanding their interaction is essential for surgical dynamic control at a professional level.

## 02 How It Works

At its core, every dynamic processor contains two signal paths: the **main path** , through which audio travels to be gain-controlled, and the **sidechain path** , through which a detection signal travels to decide how much gain control to apply. In a conventional compressor with the sidechain loop closed internally, both paths carry the same audio. Opening the sidechain—sometimes called breaking the loop or engaging the external key input—replaces the internal detection signal with whatever audio is routed to the sidechain input jack or DAW routing assignment. The compressor's gain computer still measures level, applies the attack and release curves, and outputs a control voltage, but that voltage is now derived from the external source rather than the audio being compressed.

The gain computer inside the detector performs several operations in sequence. First, the sidechain signal is typically passed through a **level detector** —either peak-sensing or RMS-averaging—which converts the audio waveform into a slowly-changing control signal representing its loudness. This control signal is then compared to the **threshold** : when it exceeds the threshold, gain reduction is calculated according to the **ratio** setting. The attack and release time constants govern how quickly the gain reduction ramps in and ramps back out. All of this behavior is dictated by the sidechain audio, but the actual attenuation is applied to the main path signal. This decoupling is what makes sidechain processing so powerful—the timing, character, and spectral content of the trigger can be sculpted independently of the audio being treated.

A **sidechain high-pass filter** (also called the detector HPF or key filter) is placed within the sidechain path before the level detector. Its purpose is to prevent low-frequency energy—particularly sub-bass, kick drum rumble, or excessive low-mid content—from over-triggering the detector. Without this filter, a compressor keyed to a full-range mix bus will pump heavily whenever the kick or bass hits, because those signals carry enormous low-frequency energy. Rolling the sidechain HPF up to 60–120 Hz makes the detector predominantly sensitive to midrange and upper-bass transients, resulting in much more controlled and musical compression. Conversely, narrowing the detector sensitivity with a bandpass or bell filter allows _frequency-selective_ triggering—the concept behind de-essers, which are simply compressors whose sidechain is filtered to only respond to the 5–10 kHz sibilance band.

In DAW environments, sidechain routing is implemented through bus assignments and plugin-specific key input selectors. The triggering signal is typically sent to an auxiliary bus or directly assigned as a sidechain source within the DAW's plugin wrapper. Crucially, the trigger signal is usually kept out of the main mix output—it is routed _only_ to the sidechain input and must not be double-printed to the stereo bus. Latency compensation is handled automatically in most modern DAWs, but in latency-heavy plugin chains producers occasionally need to pre-delay the sidechain trigger or the main audio path to ensure precise rhythmic alignment between the trigger event and the resulting gain reduction.

Understanding sidechain signal flow at this level—from the external key input through the detector HPF, into the level detector, through the gain computer, and finally into the VCA or equivalent gain element on the main path—allows producers to predict exactly what a sidechain compressor will do before they press play, rather than adjusting blindly by ear. This mechanistic fluency is what separates transparent dynamic control from accidental pumping.

Sidechain signal flow diagram: kick drum trigger routes to compressor detector, gain reduction applied to bass guitar main path. Sidechain signal flow: kick trigger controls bass compressorSIDECHAIN SIGNAL FLOWKICK DRUM(trigger source)BASS GUITAR(main path)COMPRESSORmain path inSIDECHAINHPF FILTER60–120 HzLEVEL DETECTORRMS / PEAKthreshold compareGAIN COMPUTERratio · attackrelease · GR outPROCESSEDOUTPUTkey indetectorGR ctrlGR applied— amber = sidechain / control path — teal = main audio path musicproductionwiki.com/bible/sidechain

Diagram — Sidechain: Sidechain signal flow diagram: kick drum trigger routes to compressor detector, gain reduction applied to bass guitar main path.

## 03 The Parameters

Every sidechain — hardware or plugin — operates on the same core parameters. Know these and you can work with any implementation.

THRESHOLD

Level at which sidechain-triggered gain reduction begins

Set relative to the peak level of the sidechain trigger source, not the audio being compressed. For kick-triggered bass ducking, a threshold of −18 to −12 dBFS typically catches every transient without false triggering from bleed. Setting threshold too high means the compressor fires only on the loudest hits, producing irregular pumping; too low and it fires continuously, sounding like slow volume automation rather than rhythmic ducking.

ATTACK

Speed at which gain reduction engages after the sidechain trigger exceeds threshold

For the audible pumping effect common in electronic music, fast attack times of 0.1–1 ms cause the compressor to clamp down immediately on the transient, creating an abrupt dip that listeners perceive as the kick 'pushing' the mix. For transparent ducking—such as music bed under a voiceover—attack times of 5–20 ms allow the trigger's initial transient to pass unaffected, producing a smoother onset. In sidechain de-essing, near-instant attack (0.1 ms) is essential to catch the leading edge of sibilant consonants.

RELEASE

Speed at which gain reduction recovers after the sidechain signal falls below threshold

Release is the most musically critical parameter in sidechain compression. In tempo-locked pumping, setting release to a rhythmic value—such as a dotted eighth note at the session BPM—causes the volume dip to breathe back in sync with the groove. A common calculation: at 128 BPM, one beat = 469 ms; a quarter-note release produces one full pump per kick hit. Release values of 50–150 ms work well for transparent bass ducking. Release times longer than the gap between trigger events cause compressors to stack gain reduction, never fully recovering—a telltale sign of over-compressed sidechain work.

RATIO

Degree of gain reduction applied to the main path per dB above threshold

For obvious pumping effects, ratios of 4:1 to ∞:1 are standard—at 10:1 or higher, the compressor behaves almost like a gate, producing deep, dramatic dips. For transparent ducking—keeping a bass out of the way of a kick while preserving the bass's tone—ratios of 2:1 to 4:1 with careful threshold placement create natural-sounding interplay. In broadcast and podcast music-bed ducking, ratios of 3:1 to 6:1 are typical, producing 6–12 dB of reduction when the voice is present.

SIDECHAIN HPF (KEY FILTER)

High-pass filter applied within the detector path to shape trigger sensitivity

Filtering the sidechain signal before it reaches the level detector changes which frequencies cause the compressor to fire. A 100 Hz HPF on a bus compressor's sidechain prevents kick drum sub-bass from triggering excessive gain reduction while still allowing upper-bass and midrange transients to compress normally—an essential technique for transparent mix-bus compression. For de-essing, a narrow bandpass around 5–8 kHz makes the detector hyper-sensitive to sibilance alone. Many hardware compressors (SSL G Bus, dbx 160, API 2500) and software emulations expose this filter directly; others require an external detector EQ inserted into the key input chain.

MAKEUP GAIN

Output gain applied after gain reduction to restore perceived loudness

Because sidechain compression reduces the level of the main path signal, makeup gain compensates to maintain consistent output levels. For effect-based pumping, makeup gain is often intentionally under-compensated to emphasize the dynamic contrast. For transparent applications, precise makeup gain—often matched with an A/B bypass check—ensures the processed signal sits at the same subjective loudness as the dry signal, making sidechain compression invisible to the listener while still solving frequency-masking and dynamic-clashing problems.

## 04 Quick Reference Card

Session-ready starting points. These values represent common starting points; always verify by A/B comparing bypassed and engaged states at matched loudness.

Copy Table

Parameter| General| Drums| Vocals| Bass / Keys| Bus / Master  
---|---|---|---|---|---  
Threshold| −18 to −12 dBFS| −20 to −14 dBFS| −24 to −18 dBFS| −18 to −10 dBFS| −30 to −20 dBFS  
Attack| 1–10 ms| 0.1–3 ms| 5–15 ms| 1–5 ms| 10–30 ms  
Release| 50–200 ms| 40–120 ms| 80–250 ms| 50–150 ms| 100–400 ms  
Ratio| 3:1–6:1| 6:1–∞:1| 2:1–4:1| 4:1–10:1| 2:1–4:1  
Sidechain HPF| 80–120 Hz| 60–80 Hz| 100–150 Hz| 80–100 Hz| 100–140 Hz  
Gain Reduction| 3–8 dB| 6–18 dB| 2–5 dB| 4–12 dB| 1–4 dB  
  
These values represent common starting points; always verify by A/B comparing bypassed and engaged states at matched loudness.

## 05 History & Origin

The sidechain concept predates the term itself. In the late 1930s and 1940s, broadcast engineers at NBC and CBS used rudimentary automatic gain control (AGC) circuits that incorporated simple level-detection loops separate from the main program path. The architecture of these early AGC systems—a detection branch feeding a gain element on the main signal—was the functional precursor to what we now call sidechain routing. By the 1950s, the dedicated _key input_ began appearing on professional compressor-limiters as engineers realized that controlling gain from an external source opened up a vast range of practical applications impossible with internal detection alone.

The technique entered widespread professional use through two seminal pieces of hardware. The **Fairchild 670** , released in 1959 and used extensively by engineers including Bill Putnam Sr. at Universal Recording in Chicago, featured an external sidechain access point that allowed sophisticated stereo linking and external triggering. More democratically influential was the **dbx 160** (1976), which brought affordable VCA compression with a clearly accessible sidechain insert to studios worldwide. Around the same time, the broadcast industry standardized on sidechain-triggered _ducking_ —the automatic lowering of background music when a presenter spoke—a technique that became codified in radio production throughout the 1970s and remains a foundational broadcast tool.

The audible pumping effect associated with sidechain compression emerged as an intentional aesthetic in the late 1990s French house scene. Producers including **Daft Punk** , **Cassius** , and **Étienne de Crécy** weaponized the rhythmic volume modulation produced by compressors keyed to a four-on-the-floor kick pattern, treating what mixing engineers had previously considered a flaw as a defining groove element. Daft Punk's 1997 album _Homework_ and the 2001 follow-up _Discovery_ brought this texture to international prominence. The technique spread rapidly through electro, progressive house, and eventually mainstream pop, with producers like **Max Martin** , **RedOne** , and **Calvin Harris** deploying it as a rhythmic and textural device throughout the 2000s and 2010s. By 2010, audible sidechain pumping had become one of the most recognizable production signatures in commercial music.

On the software side, the implementation of sidechain routing in digital audio workstations was initially inconsistent. Early versions of Pro Tools in the mid-1990s supported key input on compatible plug-ins, while Ableton Live—which would become the dominant platform for electronic music production—introduced reliable sidechain routing with Live 8 in 2009, a release widely credited with making the pumping effect accessible to bedroom producers globally. Modern DAWs universally support sidechain routing, and the technique has expanded beyond compressors into gates, vocoders, dynamic EQs, and fully custom modulation routings via tools such as Ableton's native LFO-to-sidechain chains, Max for Live devices, and iZotope's Neutron sidechain EQ module.

## 06 How Producers Use It

**Kick and bass cohesion** is the most foundational application in modern production. Routing the kick drum to the sidechain input of a compressor inserted on the bass guitar or bass synth causes the bass to briefly duck each time the kick hits, creating rhythmic space in the critical 60–120 Hz region where both instruments compete. At subtle settings—2–4 dB of gain reduction with a 5–20 ms attack and 60–100 ms release—the effect is barely audible as a volume change but dramatically improves low-end clarity and perceived punch. Many engineers prefer to sidechain the bass to a high-passed version of the kick (filtered above 200 Hz) to avoid over-triggering from kick sub energy, allowing only the kick's attack transient to drive the bass compressor.

**Rhythmic pumping and texture** is the second major use, deployed as an explicitly audible effect rather than a transparent tool. A compressor inserted on a full synthesizer pad, chord stab, or even a submix bus is keyed to a four-on-the-floor kick pattern—or sometimes a ghost pattern of silent MIDI notes triggering a blank audio clip—causing the track to pulse rhythmically in sync with the groove. The character of the pump varies dramatically with attack and release settings: fast attack and short release produces a sharp, clicking dip-and-recovery; slower settings produce the soft breathing associated with progressive house. The source audio need not be the actual kick in the mix—many producers use a dedicated phantom kick routed only to the sidechain bus and muted from the main output, giving complete control over the pumping pattern independently of the live drum arrangement.

**Vocal and dialogue clarity** relies on sidechain ducking to keep music, pads, and reverb returns from competing with the primary vocal or spoken word. In broadcast and podcast production, this is near-universal: a music bed compressor is keyed to the presenter's microphone, automatically reducing music level by 8–15 dB when speech begins and recovering smoothly when speech ends. In music production, the same logic applies to reverb and delay returns—sidechaining a vocal reverb send to the dry vocal signal prevents the reverb from building up during phrases and cluttering the stereo field, a technique used by engineers including Andrew Scheps and Chris Lord-Alge to maintain vocal presence in dense mixes.

**De-essing and frequency-selective compression** represents the most surgical application of sidechain principles. A de-esser is fundamentally a compressor whose sidechain path is filtered to respond only to sibilant frequencies (typically 4–10 kHz). When sibilance peaks, the filtered sidechain triggers compression on the full vocal signal—or, in split-band de-essers, only on the high-frequency band. This approach can be constructed manually using any compressor with an external sidechain input and an EQ in the key input chain, giving the producer full control over the detection frequency, bandwidth, and response curve. Dynamic EQs such as FabFilter Pro-MB and iZotope Neutron's Dynamic EQ expand this concept, applying corrective EQ only when a sidechain-monitored band exceeds a set threshold.

AbletonUse Live's built-in Compressor on the bass track; click the triangle next to "Sidechain" to expand, enable it, and select the kick track from the Audio From dropdown. Set the EQ button to high-pass at 100 Hz for cleaner triggering. For phantom pumping, route a muted kick clip to the compressor's sidechain bus without the kick appearing on the master.

FL StudioFruity Peak Controller is FL's native sidechain tool: insert it on the kick mixer channel, set it to output a control signal, then right-click the Volume knob on the bass channel and link it via "Peak controller." Alternatively, use Parametric EQ 2 or Maximus with sidechain input enabled via the mixer send routing panel.

Logic ProInsert Logic's built-in Compressor on the target track, then select the kick track from the Sidechain dropdown in the plugin header (top right). The Vintage VCA and Platinum Digital compressor models in Logic respond most predictably to sidechain triggering. Enable the HP filter in Logic's compressor for cleaner detection on full-range material.

Pro ToolsSend the kick to an aux bus, then select that bus as the key input on any plug-in that supports sidechain input (look for the "key" button in the plugin header or on supported plug-ins like Avid's stock Dynamics III). Use a pre-fader send to ensure the sidechain level is independent of the kick's fader position in the mix.

ReaperRoute the kick track to the target track using the Routing Matrix (Ctrl+Alt+R), enabling it as a sidechain send (channels 3/4 rather than the main stereo pair). ReaComp's Detector input section then selects "Auxiliary input" to receive the sidechain. This routing model gives Reaper one of the most flexible sidechain implementations of any DAW.

The Producer's Briefing

### Sound better by _Friday._

One email a week. The techniques behind the terms — curated by working producers, not algorithms.

Join Free

No spam · Unsubscribe anytime

## 07 In the Wild

Abstract knowledge becomes practical when you can hear it in music you know. These tracks demonstrate sidechain used intentionally, at specific moments, for specific purposes.

Daft Punk — "One More Time" (2000)

0:00 intro onward · Produced by Daft Punk (Thomas Bangalter & Guy-Manuel de Homem-Christo)

The defining commercial example of audible sidechain pumping. The chord stabs and synth pads duck sharply on every quarter-note kick hit, breathing in rhythmically with the groove. Listen specifically to the sustained string pad underneath the chorus—at roughly 1:20 when the full drum pattern enters, the pad visibly (audibly) pulses in and out of the mix on each kick. The release is calibrated to return just before the next beat, giving the track its perpetual sense of forward motion. The effect here is not incidental; it was engineered as a primary textural element.

Calvin Harris — "Feel So Close" (2011)

0:45 drop onward · Produced by Calvin Harris

A textbook example of modern electronic pop sidechain pumping. When the main drop arrives, the whole mix—chords, pads, even the reverb returns—compresses heavily against the four-on-the-floor kick, creating an almost physical push-pull sensation. Compare the pre-drop verse (0:00–0:44) to the drop itself: the verse sits relatively static, while the drop breathes continuously. Release time here is approximately one quarter note at the track's 128 BPM tempo (~469 ms), which is a standard calculation for tempo-synced pumping.

Kendrick Lamar — "HUMBLE." (2017)

0:00 throughout · Produced by Mike Will Made-It

A contrasting example of transparent, functional sidechain use in rap production rather than effect-based pumping. The 808 kick and bass interact with remarkable low-end clarity despite the extreme sub-bass weight of both elements. Mike Will Made-It uses sidechain ducking between the 808 sub and bass elements to prevent low-frequency masking—an approach you can study by frequency-analyzing the 20–80 Hz band and noting how bass energy briefly dips on every 808 hit. The gain reduction is not audible as pumping but is responsible for the track's unusually defined low end on consumer speakers.

Billie Eilish — "bad guy" (2019)

0:30 verse · Produced by Finneas O'Connell

Demonstrative example of sidechain de-essing and vocal-reverb ducking. Eilish's close-microphone vocal—recorded inches from the capsule—is naturally heavy with sibilance and proximity effect. Finneas applies aggressive de-essing using a sidechain-filtered compressor to tame the 6–8 kHz region while preserving the whispery intimacy of the vocal character. Additionally, the reverb return on the vocal clearly ducks during phrasing and blooms only in the gaps, a classic sidechain reverb technique that prevents the reverb tail from swamping the lyrical clarity.

Listen On Spotify

Billie Eilish — bad guy

Kendrick Lamar — HUMBLE.

## 08 Types & Variants

Transparent Ducking Sidechain

dbx 160A · API 2500

The primary function is frequency-masking prevention rather than audible effect. Typically applied to bass, synth pads, or reverb returns keyed to a kick drum or vocal. Settings favor moderate ratios (2:1–5:1), controlled attack (5–20 ms), and tempo-aware release values. The listener should never identify compression as the source of low-end clarity or mix space—only notice its absence if bypassed.

Rhythmic Pumping Sidechain

Empirical Labs Distressor · Neve 33609

An explicitly audible effect in which the sidechain compressor becomes a rhythmic instrument in its own right. Fast attack, high ratios (8:1 to ∞:1), and release times calibrated to musical note values produce the breathing, pulsing texture central to house, techno, and EDM production. Often triggered by a phantom kick signal not present in the final mix, giving the producer precise rhythmic control independent of the drum arrangement.

Sidechain De-Essing

Urei LA-22 · SPL De-Esser

A frequency-selective application in which the sidechain path is bandpass-filtered to the sibilant range (typically 4–10 kHz) so the compressor triggers only on harsh high-frequency content. In wideband de-essing, the full vocal signal is compressed when sibilance is detected; in split-band designs (used by most modern plug-in de-essers), only the filtered frequency band is attenuated, preserving low and mid frequencies entirely.

Sidechain Gating

Drawmer DS201 · Aphex 612

A noise gate whose detector is fed by an external key input rather than the gated signal itself. The classic application is tightening drum tracks: a snare drum gate is keyed to a click track or clean MIDI-triggered snare so that room ambience and bleed open only when the snare fires, regardless of what else is happening on the snare microphone. A second common use is rhythmically gating sustained instruments—synth strings, organs—to a drum pattern to create chopped stutter effects without editing.

Dynamic EQ Sidechain

GML 8900 · Weiss DS1-MK3

An evolution of the de-esser concept in which EQ curves are applied dynamically, triggered by either the main signal or an external sidechain. A dynamic EQ node at 200 Hz on a bass guitar, keyed to the kick drum, pulls low-mid mud only when the kick occupies that region. Products such as FabFilter Pro-MB, iZotope Neutron, and TDR Nova popularized this approach, which allows frequency-specific sidechain control impossible with traditional broadband compression.

## 09 Common Mistakes

  * ✕

Setting release longer than the gap between trigger events

When release time exceeds the interval between sidechain trigger hits—for example, a 600 ms release on a compressor keyed to a 128 BPM kick at 469 ms per beat—the compressor never fully recovers before the next hit arrives. Gain reduction stacks progressively, creating a permanently over-compressed signal rather than rhythmic pumping. Fix this by calculating the target release from the session BPM and ensuring the release value is comfortably shorter than the shortest gap between trigger events.

  * ✕

Forgetting to mute or remove the sidechain trigger from the main mix output

In DAW routing, the kick or trigger signal used as a sidechain source is sometimes accidentally double-routed to both the sidechain bus and the master output, printing the kick twice at different phase relationships. This typically manifests as low-end smearing, unexpected comb filtering, or a subtle doubling on the kick transient. Always verify that the sidechain send is pre-fader, post-fader only to the key bus, and that the track's main output is assigned correctly—never to the master if it's serving a sidechain-only function.

  * ✕

Using too slow an attack on effect-based pumping

Producers new to sidechain often set attack times of 20–50 ms seeking a 'softer' pump, but slow attack on a rhythmic sidechain compressor allows the initial transient of the kick to pass without triggering full gain reduction, resulting in a weak, unconvincing pump that sounds neither transparent nor intentional. For audible pumping, attack must be fast enough (0.1–5 ms) to clamp down before the listener's ear registers the kick transient. The perceived 'softness' of a pump is controlled primarily by release, not attack.

  * ✕

Applying a pumping sidechain effect to an already-compressed bus

Inserting a sidechain compressor after a bus compressor that is already applying significant gain reduction can cause the two compressors to interact unpredictably: the bus compressor modifies the transient character of the trigger signal before it reaches the sidechain detector, and the dual layers of gain reduction produce an erratic, stuttering result. Insert the sidechain compressor first in the chain, or use a parallel sidechain construction where the dry signal and the sidechain-ducked signal are blended at the bus stage.

  * ✕

Neglecting the sidechain high-pass filter on bus and mix applications

Without a sidechain HPF engaged, a bus compressor keyed to a full-mix or full-range source will be dominated by the enormous low-frequency energy of kick and bass transients, causing heavy and unpredictable gain reduction every time low-end content peaks. Engaging a high-pass filter on the detector path at 80–120 Hz removes this sub-bass influence, allowing the compressor to respond primarily to midrange content—exactly the approach used on the SSL G Bus Compressor's high-pass filter, one of the most discussed mix-bus compressor features in professional audio.

  * ✕

Sidechaining in a way that destroys mono compatibility

When sidechain pumping is applied asymmetrically to stereo material—for example, if the gain reduction differs between left and right channels because the trigger is a mono kick summed unevenly—the stereo image shifts on every pump cycle. This creates stereo width artifacts that collapse badly in mono, a critical problem for streaming, broadcast, and club system compatibility. Always verify sidechain processing in mono, and when applying pumping to a stereo bus, use a compressor that links its left and right gain reduction detectors from the same mono sidechain trigger.


Interactive Tool

BPM Timing Calculator

Enter your project BPM to get musically-synced sidechain times.

BPM

Note Division WholeHalf QuarterEighth SixteenthTriplet quarter Triplet eighthDotted quarter

Calculate Timings

Musically Synced Values

TAP TEMPO Tap 4+ times

## Related Guides & Tools

[Sidechain Compression GuideMaster sidechain compression: kick-to-bass pumping, ghost sidechaining, multiband setups, and…](/articles/sidechain-compression-guide)[Sidechain & Ducking ReferenceFree sidechain and ducking reference. BPM-synced timing diagram: kick pattern, GR envelope,…](/tools/sidechain-ducking-reference)

## 10 Producers Also Look Up

[CompressionThe dynamic processing technique that sidechain routing most commonly controls, with the sidechain determining when and how much gain reduction is applied.](https://musicproductionwiki.com/bible/compression) [Noise GateA processor that opens and closes a signal path based on level thresholds, frequently triggered via sidechain key inputs for rhythmic gating effects.](https://musicproductionwiki.com/bible/noise-gate) [ThresholdThe level at which a dynamic processor begins to act, set relative to the sidechain trigger signal's amplitude rather than the processed audio.](https://musicproductionwiki.com/bible/threshold) [AttackThe parameter governing how quickly gain reduction engages after the sidechain signal exceeds threshold, controlling the character of the pumping onset.](https://musicproductionwiki.com/bible/attack) [ReleaseThe recovery time after gain reduction, which in sidechain applications is typically calibrated to musical tempo values to synchronize pumping with the groove.](https://musicproductionwiki.com/bible/release) [Parallel CompressionA technique often combined with sidechain processing, blending the compressed signal with the dry signal to preserve transients while still achieving tonal shaping.](https://musicproductionwiki.com/bible/parallel-compression)

## 11 Further Reading

These MPW articles put sidechain into practice — specific techniques, real tools, and applied workflows.

[ → How To Sidechain In Ableton ](https://musicproductionwiki.com/articles/how-to-sidechain-in-ableton.html) [ → Sidechain Compression Guide ](https://musicproductionwiki.com/articles/sidechain-compression-guide.html) [ → What Is Sidechain Compression ](sidechain-compression) [ → De Esser Guide ](de-esser) [ → Dynamic Eq Vs Multiband Compression ](https://musicproductionwiki.com/articles/dynamic-eq-vs-multiband-compression.html)

## 12 Frequently Asked Questions

What is sidechain compression in simple terms?+

Sidechain compression means one audio signal controls the volume reduction applied to a different audio signal. For example, a kick drum can trigger a compressor that briefly lowers the bass guitar's volume every time the kick hits. The kick is the 'trigger' and the bass is the 'target'—you hear the bass getting quieter, not the kick doing anything different. It's the mechanism behind the classic pumping sound in dance music as well as the transparent low-end clarity in professional mixes.

Do I need a special plugin to use sidechain compression?+

Most stock compressors included with major DAWs support sidechain input natively—including Ableton's Compressor, Logic's Compressor, and Pro Tools' Dynamics III. You do not need a third-party plugin to start experimenting. That said, dedicated sidechain tools like FabFilter Pro-C 2, Waves SSL G-Master Buss Compressor, and Cytomic The Glue offer more transparent or characterful compression that many producers prefer for specific applications.

What's the difference between a sidechain input and a sidechain filter?+

The sidechain input determines which audio signal drives the compressor's detection circuit—it's the routing decision. The sidechain filter (also called the detector HPF or key filter) shapes that incoming detection signal before it hits the level detector—it's a tonal sculpting decision within that routing. You can filter the internal detection signal (same audio, filtered) without using an external sidechain at all. Both tools are often present on the same compressor and can be used simultaneously for precise control over what triggers gain reduction.

How do I calculate the right release time for tempo-synced pumping?+

Divide 60,000 by your session BPM to get the duration of one quarter note in milliseconds. For example, at 128 BPM: 60,000 ÷ 128 = 469 ms per beat. Set your release to this value for one pump per kick hit, or halve it (234 ms) for a faster double-pump feel. Most modern DAWs allow you to set release time in musical note values directly within the compressor plugin, which auto-calculates the BPM-synced duration and updates dynamically if your tempo changes.

Can I use sidechain on a mix bus or master bus?+

Yes, and it's a foundational professional technique. Using the mix bus compressor's sidechain filter to high-pass the detection signal (typically at 80–120 Hz) prevents the kick and bass from over-triggering the compressor, making bus compression far more transparent and musical. Some engineers also use dynamic sidechain triggering on the master bus for broadcast loudness management. However, heavy audible pumping applied directly to the stereo master is generally avoided in commercial mastering—it compromises mono compatibility and overall dynamics.

What is a 'phantom kick' sidechain and why do producers use it?+

A phantom kick is a silent MIDI-triggered kick drum sample—or simply a muted audio clip on a kick track—routed only to the sidechain bus without appearing in the main mix output. Producers use this technique to decouple the pumping pattern from the actual live kick drum in the arrangement. If the kick drum pattern changes (fills, breaks, dropped hits), the pumping effect remains constant because it's driven by the independent phantom pattern. This gives producers precise rhythmic control over the pumping texture independent of the drum arrangement.

How does sidechain differ from volume automation?+

Volume automation is a static, pre-drawn series of level changes that executes the same way on every playback regardless of what the audio contains. Sidechain compression is dynamic and reactive—it responds in real time to the actual audio level of the trigger signal, including its timing, velocity, and transient character. A kick drum hit played 10 ms late will trigger the sidechain compressor 10 ms late. Volume automation would not notice. This makes sidechain compression far more responsive to performance nuances and essential for live-feel rhythmic interplay, while automation is better for large-scale structural changes that need to be precisely predetermined.

What are advanced techniques for sidechain processing beyond kick-to-bass ducking?+

Advanced applications include: using a filtered sidechain to build a completely custom de-esser by inserting an EQ with a narrow bell boost in the key input chain; sidechaining reverb and delay return buses to the dry vocal to create self-ducking reverb that clears during phrases; using dynamic EQ sidechain (FabFilter Pro-MB, iZotope Neutron) for frequency-specific ducking rather than broadband compression; applying sidechain gating to room microphones keyed to a close-mic snare signal; and using Max for Live or custom routing in Reaper to sidechain non-dynamic processors—such as applying LFO rate modulation driven by an audio sidechain signal—creating hybrid dynamic-modulation effects not possible with traditional compressor routing.

Signal ProcessingCompressionDynamic ControlMixingElectronic Music Production

Last Verified: May 14, 2026 · 2026 Edition · Part of The Producer's Bible

[Share on X](https://twitter.com/intent/tweet?url=https://musicproductionwiki.com/bible/sidechain&text=The+definitive+Sidechain+guide+for+producers) [Share on Reddit](https://www.reddit.com/submit?url=https://musicproductionwiki.com/bible/sidechain) Copy Link

Part of [The Producer's Bible](https://musicproductionwiki.com/bible/) — Every term. Every technique. One place.  
Published by [MusicProductionWiki.com](https://musicproductionwiki.com) · The Reference Standard for Music Production 

The Producer's Bible · MusicProductionWiki.com · 2026 Edition

  * [Home](https://musicproductionwiki.com)
  * [About](/about)
  * [Privacy](/privacy)
  * [Contact](mailto:team@musicproductionwiki.com)



↑
