---
titre: "Music Production Wiki — MIDI (vélocité, CC, expression, programmation réaliste)"
source: https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/midi.html
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: MIDI ; mixage ; EQ
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Page HTML du wiki convertie en Markdown (html2text) ; document communautaire [HEUR].

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

The Producer's Bible

Definition How It Works Parameters Quick Ref Tools Signal Chain History How To Use By Genre Hardware vs Plugin Before / After In The Wild Types Verdict Plugins Mistakes Flags Progression FAQ Related

[Home](/)› [The Producer's Bible](/bible/)› MIDI

Production

Beginner

Understand first: [Oscillator](/bible/oscillator) › [Envelope](/bible/envelope) › [Adsr](/bible/adsr)

# MIDI

noun / production tool

_MIDI is the invisible conductor — every note, every velocity, every subtle bend is pure intent before it ever becomes sound._

📅 2026-05-19 ⏲ 31 min read 📚 Producer's Bible

Quick Answer

MIDI (Musical Instrument Digital Interface) is a standardized communication protocol that transmits performance data — including note pitch, velocity, duration, pitch bend, modulation, and control change messages — between electronic instruments, computers, and hardware devices as numeric instructions rather than audio signals. Unlike audio, MIDI carries no sound itself; it is a set of commands that tell a receiving device what to play, how hard, and for how long. Originally ratified in 1983, MIDI 1.0 uses a 5-pin DIN serial connection transmitting at 31,250 baud, while MIDI 2.0 (2020) massively expands resolution, bidirectionality, and expression.

New to MIDI? Start here

Parameters -> Before / After -> Quick Reference -> Common Mistakes

⇓ Download Reference Sheet

✕

⇓

### Get the Free Sheet

Free with The Producer's Briefing.

Get My Free Sheet

No spam. Unsubscribe anytime.

Common Misconception

MIDI is only for recording keyboard performances — if you don't play piano, MIDI isn't really relevant to your workflow.

MIDI is the universal data layer for all programmed music production, not just keyboard performance. Drum programming, sample triggering, automation, hardware control, patch changes, arpeggiators, generative music systems, and DAW remote control all run on MIDI. Every producer who works with virtual instruments, hardware synths, or electronic drum programming is working with MIDI — the keyboard is just one of hundreds of ways to input it.

_MIDI is the invisible conductor — every note, every velocity, every subtle bend is pure intent before it ever becomes sound._

MIDI — Musical Instrument Digital Interface — is the most consequential technical standard in the history of modern music production. Ratified in 1983 by a consortium of competing synthesizer manufacturers who recognized that a universal communication language would benefit the entire industry, MIDI fundamentally redefined what it means to compose, perform, and produce electronic music. At its core, MIDI transmits performance _instructions_ — not audio. When you press a key on a MIDI controller, no sound travels down the cable. Instead, a precisely encoded numeric message describes what note was played, how hard the key was struck, and when the finger was lifted. The receiving device — a synthesizer, a sampler, a virtual instrument running inside a DAW — interprets those instructions and generates audio accordingly. That separation of performance data from sound generation is the foundational concept every serious producer must internalize.

The original MIDI 1.0 specification operates over a 5-pin DIN serial connection, transmitting at 31,250 baud — a deliberately slow but extremely stable data rate chosen to minimize jitter over the cable runs common in live and studio environments of the early 1980s. Every MIDI message is a compact numerical package: a status byte identifying the message type and channel, followed by one or two data bytes carrying the specific values. A Note On message for middle C at full velocity, for example, transmits three bytes: 0x90 (Note On, Channel 1), 0x3C (note number 60, middle C), and 0x7F (velocity 127). The entire message travels in under a millisecond. MIDI 2.0, ratified in 2020, dramatically expands this architecture — moving from 7-bit (0–127) resolution to 32-bit per-note expression, adding bidirectional communication via MIDI-CI (Capability Inquiry), and enabling per-note pitch, pressure, and controller data that makes expressive acoustic instrument modeling far more achievable in the digital domain.

What makes MIDI so powerful from a production standpoint is its editability. Because MIDI is data rather than audio, every parameter of a performance can be modified after the fact without any generational loss. You can transpose a complete orchestral arrangement by pressing a single key. You can correct a single wrong note in a 200-note piano passage without re-recording a single second of audio. You can slow down a breakneck guitar solo to half speed to hear the phrasing clearly, quantize the timing to a grid, humanize it back with random offsets, and then route the same MIDI sequence through ten different virtual instruments simultaneously to audition which timbre serves the track. No other recording technology offers this degree of non-destructive, infinitely malleable compositional control.

Understanding MIDI as a language — not just a recording format — changes how you approach composition and arrangement entirely. MIDI channels allow up to 16 simultaneous independent instrument voices on a single cable. MIDI clock synchronizes drum machines, sequencers, and arpeggiators across an entire studio rig without audio sync tracks. Program Change messages switch synth patches mid-sequence. Continuous Controller (CC) messages automate any parameter on a receiving instrument in real time — filter cutoff, reverb depth, oscillator pitch — with sub-millisecond resolution when running over USB MIDI or modern DAW internal routing. The protocol is simultaneously simple enough that a teenager can learn its basic operations in an afternoon and deep enough that professional composers spend decades mastering its full expressive range.

> "Leave some room for God to walk through the room. Don't fill every space."

— Quincy Jones, Producer (Michael Jackson, Frank Sinatra, Ray Charles) | Q: The Autobiography of Quincy Jones

This principle resonates directly with MIDI composition: the rests in a MIDI sequence, the spaces between note-on events, the velocity dips between phrases — these silences are as intentional as the notes themselves. The most effective MIDI programming is never about maximum density. It is about maximum intent.

MIDI is a performance instruction protocol that transmits note pitch, velocity, duration, and control data as numeric messages — not audio. Its separation of performance data from sound generation makes it the foundational compositional and production tool of modern electronic music.

Every MIDI message begins with a status byte — a single 8-bit value whose upper nibble identifies the message type and whose lower nibble specifies the MIDI channel (1–16). Following the status byte are one or two data bytes carrying the message's payload values, each capped at 7 bits and therefore ranging from 0 to 127. This three-byte structure — status, data1, data2 — covers the vast majority of musical performance messages: Note On, Note Off, Polyphonic Key Pressure (per-note aftertouch), Control Change, Program Change, Channel Pressure (mono aftertouch), and Pitch Bend. System messages — including MIDI Clock, Start, Stop, Continue, and SysEx (System Exclusive) — fall outside the channel structure and are broadcast to all devices on the MIDI bus simultaneously. Understanding this distinction between channel messages and system messages is fundamental to routing MIDI correctly in a complex studio setup.

When a MIDI controller transmits a Note On event, the receiving device looks up the note number in its voice allocation table, assigns an oscillator or sample playback engine to that pitch, scales the amplitude based on the velocity value, and begins generating audio. When the controller transmits the corresponding Note Off message (or a Note On with velocity 0 — the shorthand form), the voice enters its release phase and fades out according to the instrument's envelope settings. Everything between those two events — pitch bend messages, aftertouch data, CC automation, modulation wheel movements — arrives as a continuous stream of additional messages that the instrument processes in real time, modulating its sound accordingly. In a DAW, all of this data is recorded into the MIDI track's event list, creating a complete written score of every performance gesture that can be replayed, edited, and re-rendered through any compatible instrument at any time.

Continuous Controller messages — universally referred to as CCs — are the expressive backbone of sophisticated MIDI programming. CC numbers 0–127 are assigned to specific functions by convention: CC1 is the Modulation Wheel, CC2 is Breath Controller, CC7 is Channel Volume, CC10 is Pan, CC11 is Expression (a scaled sub-volume ideal for crescendo/decrescendo automation), CC64 is the Sustain Pedal, and CC74 is commonly assigned to filter brightness or cutoff. Many of these assignments are defined in the General MIDI standard, but virtual instrument developers frequently remap CC numbers to control any parameter within their instrument — filter resonance, reverb send, oscillator detune, sample layer crossfade. Drawing CC automation lanes in your DAW's piano roll is the equivalent of writing dynamic and articulation markings on a printed score, except these markings actually _perform themselves_ during playback with perfect repeatability. MIDI 2.0 extends CC resolution from 7-bit (128 steps) to 32-bit (over four billion discrete steps), effectively eliminating the audible stepping artifacts that appear when automating filter cutoffs or pitch values at fine resolutions in MIDI 1.0.

MIDI clock operates on a separate logical layer from performance messages. The specification defines 24 MIDI Clock pulses per quarter note — a timing resolution sufficient for synchronizing tempo-dependent devices across an entire rig. When a DAW acts as MIDI clock master, it broadcasts these 24 PPQN pulses over every connected MIDI output, keeping external drum machines, hardware sequencers, arpeggiators, and delay units locked to the project tempo in real time. Song Position Pointer (SPP) messages extend this by encoding the current playback position in 16th-note increments, allowing slaved devices to chase the master timeline when playback begins mid-sequence. For modern productions running entirely inside a DAW, internal MIDI routing eliminates cable timing variance entirely — a significant advantage over external hardware chains where cable length and MIDI interface quality introduce measurable latency that must be compensated with per-device MIDI offset adjustments.

MIDI works by transmitting compact numerical messages — status byte plus data bytes — that encode every performance parameter from note pitch and velocity to continuous controller automation and timing sync, with the receiving instrument generating audio in real time from those instructions.

MIDI's parameter set maps directly onto every dimension of musical expression that can be encoded in real-time performance data. From the basic pitch-and-velocity core through the full CC automation landscape, mastering these parameters is what separates producers who use MIDI as a typing tool from producers who use it as a compositional instrument. The following parameter cards cover the essential values you will work with on every session.

Note Number Range: 0–127 | Middle C = 60

Encodes chromatic pitch across the full piano keyboard range and beyond. Note 21 is the lowest A on an 88-key piano; note 108 is the highest C. Values below 21 and above 108 are valid MIDI but typically outside standard instrument ranges — useful for triggering drum samples mapped across the full 0–127 range on samplers. In piano-roll view, note number maps directly to vertical position on the grid.

Velocity Range: 0–127 | Note Off at 0

Represents the speed at which a key was depressed — the primary dynamic control for MIDI performance. Velocity 1 is the softest audible strike; velocity 127 is the hardest. Most professional virtual instruments map velocity to multiple sample layers (piano forte, piano mezzoforte, pianissimo), to amplitude, and to tonal brightness simultaneously. Programming realistic velocity variation — avoiding flat 100-across-the-board patterns — is the single most impactful humanization technique available in MIDI.

Channel (1–16) Range: 1–16 | Omni Mode receives all

MIDI's polyphonic routing layer. Each of the 16 available channels can carry an independent stream of note and CC data, allowing a single MIDI cable or virtual bus to drive 16 separate instruments simultaneously. In a DAW, each instrument track typically receives on a dedicated channel, though General MIDI devices reserve Channel 10 exclusively for drum and percussion maps. Multi-timbral hardware synths and samplers exploit the full 16-channel capacity to run an entire arrangement from a single module.

Pitch Bend Range: -8192 to +8191 | 14-bit resolution

The only MIDI 1.0 parameter with 14-bit resolution (combining two 7-bit data bytes), giving 16,384 discrete steps of pitch deviation. Pitch bend range is set on the receiving instrument — typically ±2 semitones by default, but commonly extended to ±12 or ±24 semitones for expressive leads and bass lines. Guitar-style bends, vibrato, dive bombs, and portamento effects all live in the pitch bend lane. Drawing precise pitch bend curves in the piano roll creates perfectly repeatable bends that would require exceptional physical control to perform live.

Continuous Controllers (CC) Range: 0–127 per CC | 128 controller slots

The automation backbone of MIDI. CC1 (Mod Wheel) typically routes to vibrato depth or filter modulation; CC11 (Expression) scales output volume for phrase dynamics; CC64 (Sustain) holds notes through their release phase. In orchestral programming, CC11 driving amplitude and CC1 driving vibrato depth — with carefully drawn curves — produces the swelling, breathing quality of live string and brass sections. Every virtual instrument exposes its internal parameters to CC input, making the entire instrument automatable from a single MIDI track.

Aftertouch Channel: single value 0–127 | Poly: per-note 0–127

Pressure applied to a key after it is fully depressed. Channel Aftertouch sends a single pressure value representing the hardest-pressed key across the entire channel — common on most keyboards. Polyphonic Aftertouch sends independent pressure values per note, enabling per-finger expression on instruments that support it. Aftertouch is most powerfully used to add vibrato, increase brightness, or open a filter as playing intensity increases — replicating the natural tonal change that occurs when a wind or string player presses harder into a note. MIDI 2.0's per-note expression capabilities dramatically expand on this concept.

Beyond these core parameters, two additional message types are essential to professional MIDI workflow: Program Change and SysEx. Program Change (values 0–127) instructs a receiving device to switch to a numbered patch or preset, enabling patch changes mid-sequence — critical for live performance rigs where a synth must cycle through multiple sounds during a single song. System Exclusive messages carry manufacturer-specific data in variable-length packets, used for parameter dumps, patch librarian transfers, and deep hardware control that falls outside the standard message set. Any time you use a MIDI librarian application to back up your hardware synth patches or remotely edit filter envelope parameters on a connected unit, you are using SysEx.

Clock and transport messages round out the functional parameter set. MIDI Start (0xFA), Stop (0xFC), and Continue (0xFB) control the playback state of slaved devices. MIDI Time Code (MTC) carries SMPTE-equivalent timing information for synchronization with video and audio workstations. Song Select messages choose between numbered sequences on a connected drum machine or sequencer. Together, these system-level messages make MIDI not just a note transmission protocol but a complete studio synchronization infrastructure capable of coordinating an arbitrarily complex hardware rig with sample-accurate timing relative to a master clock source.

MIDI's parameter set covers note number, velocity, channel routing, pitch bend, continuous controllers, aftertouch, program changes, and clock/sync messages — together encoding every dimension of musical performance with sufficient resolution for professional production work.

127 Maximum MIDI 1.0 value (7-bit resolution)

Every fundamental MIDI 1.0 parameter — note pitch, velocity, CC values, aftertouch — maxes out at 127, a consequence of 7-bit binary encoding. This ceiling means a piano velocity of 127 is the hardest possible hit, CC74 at 127 is a fully open filter, and note 60 is Middle C. Understanding that the entire protocol operates on a 0–127 scale is the mental model that makes MIDI programming intuitive across every instrument and controller.

The following quick reference table maps the most critical MIDI parameters to their operational ranges, typical production applications, and the DAW lane or inspector field where they are accessed and edited. Use this as your session-floor reference for MIDI programming decisions. Last updated 2026-05-19.

Parameter | Range | Resolution | Typical Use | DAW Location | Notes  
---|---|---|---|---|---  
Note Number | 0–127 | 7-bit (128 steps) | Pitch assignment, drum mapping | Piano Roll vertical axis | Middle C = 60 (C3 or C4 depending on DAW)  
Velocity | 1–127 | 7-bit (127 steps) | Dynamics, layer switching, accent | Piano Roll note stems / velocity lane | 0 = Note Off shorthand; avoid flat velocity on melodic parts  
Pitch Bend | -8192 to +8191 | 14-bit (16,384 steps) | Bends, vibrato, portamento, dive bombs | Automation lane / CC lane | Bend range set on receiving instrument; default ±2 semitones  
CC1 (Mod Wheel) | 0–127 | 7-bit | Vibrato depth, filter mod, expression | CC automation lane | Draw curves for natural vibrato onset; avoid step-function shapes  
CC11 (Expression) | 0–127 | 7-bit | Phrase dynamics, crescendo/decrescendo | CC automation lane | Use in conjunction with CC7 (Volume); CC11 for real-time dynamics  
CC64 (Sustain Pedal) | 0 or 127 | Binary (on/off) | Sustain, piano legato, pad holds | CC automation lane | Values 0–63 = off; 64–127 = on; check for stuck sustain on patch change  
Channel Aftertouch | 0–127 | 7-bit | Vibrato, brightness, filter open | Aftertouch lane in piano roll | Poly Aftertouch requires per-note capable keyboard and instrument  
MIDI Channel | 1–16 | 4-bit (16 channels) | Instrument routing, GM drum = Ch.10 | Track inspector / MIDI input filter | Omni mode receives all channels; use for quick testing only  
  
ShareCopy Link[Share on X](https://x.com/intent/tweet?text=MIDI+Quick+Reference+%E2%80%94+%40mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi%23quick-reference)[Reddit](https://reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi%23quick-reference&title=MIDI+Quick+Reference+%E2%80%94+MusicProductionWiki)

Signal chain position of MIDI Controller / Sequencer in music production Songwriter / Composer Musical Idea Melody / Harmony MIDI Controller / Sequencer Performance Data Note / CC / Clock ◀ YOU ARE HERE Virtual Instrument / Sampler Sound Engine Receives MIDI Instrument Track Audio Render DAW Channel EQ / Processing Tone Shaping Pre-Fader Inserts Channel Fader Level Balancing Mix Positioning Bus / Aux Grouping Parallel or Serial Master Output Final Mix Export / Monitor

Songwriter / Composer

Musical Idea · Melody / Harmony

↓

MIDI Controller / Sequencer

Performance Data · Note / CC / Clock

▶ You are here

↓

Virtual Instrument / Sampler

Sound Engine · Receives MIDI

↓

Instrument Track

Audio Render · DAW Channel

↓

EQ / Processing

Tone Shaping · Pre-Fader Inserts

↓

Channel Fader

Level Balancing · Mix Positioning

↓

Bus / Aux

Grouping · Parallel or Serial

↓

Master Output

Final Mix · Export / Monitor

MIDI occupies a unique position in the signal chain because it is not audio — it exists upstream of audio entirely, at the point of performance intent. The MIDI controller or sequencer generates note and CC data that flows into the virtual instrument or sampler, which converts those instructions into an audio signal that then enters the instrument track. From that point forward, the signal follows the standard path through insert processing, channel fader, bus routing, and master output. Understanding this distinction prevents a common beginner error: attempting to process MIDI as if it were audio, or failing to understand why adjusting a fader does not change the MIDI data itself. The MIDI data and the audio it generates are independent layers — you can edit the MIDI performance while the audio processing chain remains untouched, and vice versa. In practice, this means you should finalize your MIDI programming and instrument selection before committing to heavy audio processing, since a timbre change at the instrument level will interact differently with any downstream processing.

#### Interaction Warnings

  * **MIDI Feedback Loops:** Routing a MIDI output back to its own input — common when using software instruments in multi-timbral setups or with external hardware — creates runaway note loops that can freeze a DAW or hang notes indefinitely. Always verify your MIDI routing matrix before enabling record on a new track.
  * **Channel Overlap Conflicts:** Sending Note On messages on the same channel from two separate MIDI tracks simultaneously will cause voice stealing on multi-timbral instruments and unpredictable behavior on hardware synths. Assign each instrument or part to a dedicated MIDI channel.
  * **Stuck Notes:** If a Note Off message is dropped — due to cable interruption, buffer overflow, or an abrupt DAW stop — the receiving instrument sustains the note indefinitely. Use your DAW's "MIDI Panic" or "All Notes Off" (CC123) function to clear hung notes instantly. Most DAWs map this to a keyboard shortcut.
  * **CC Conflicts with DAW Automation:** Writing CC7 (Volume) automation in the MIDI lane simultaneously with DAW channel fader automation creates competing volume commands that produce erratic level behavior. Choose one automation source — MIDI CC or DAW parameter — and commit to it for each parameter.
  * **Clock Jitter on Long MIDI Chains:** Daisy-chaining multiple hardware MIDI devices through THRU ports introduces cumulative latency — approximately 1 ms per device in the chain. For more than three chained devices, use a MIDI Thru box with buffered outputs rather than passive THRU connections to maintain tight clock synchronization.



MIDI CONTROLLER Note / CC / Clock Performance Data DAW SEQUENCER Records + Routes MIDI Track / Piano Roll VIRTUAL INST. Translates MIDI Generates Audio AUDIO CHANNEL EQ / FX / Fader Mix + Export INPUT DATA LAYER CONVERSION AUDIO LAYER CC Automation (CC1, CC7, CC11, Pitch Bend, Aftertouch) Flows alongside Note data → modulates sound engine parameters in real time MIDI SIGNAL FLOW Performance Data → Sound Generation → Audio Processing

The diagram above illustrates the fundamental separation between MIDI data flow and audio signal flow. Notice that MIDI moves horizontally through the first three stages — controller, DAW sequencer, and virtual instrument — as pure numeric data, never touching the audio processing chain. The conversion from data to audio happens exclusively at the virtual instrument stage, after which the signal behaves identically to any other audio source in the mix. The CC automation layer beneath the main flow shows how controller data runs in parallel with note data, continuously updating the sound engine's parameters throughout playback without interrupting the note stream itself.

The critical insight this diagram enforces is that any editing you perform in the MIDI layer — transposing notes, adjusting velocities, drawing CC curves, shifting note timings — happens before any audio exists. This means your EQ, compression, and effects processing on the instrument track hears the result of all those MIDI decisions simultaneously. A velocity increase of 20 across all notes does not just make the instrument louder; it changes the timbre, triggering higher-layer samples, brightening attack transients, and potentially overdriving any saturation plugin in the insert chain. MIDI editing and audio processing are inseparable in their final interaction, even though they occupy entirely separate technical layers.

### 1981–1983: The Summit and the Standard

The story of MIDI begins at a meeting that should not have happened by conventional business logic: competing synthesizer manufacturers sitting in the same room, agreeing to adopt a common technical standard that would benefit each other's customers equally. The key figures were Dave Smith of Sequential Circuits and Ikutaro Kakehashi of Roland, who together drafted the Universal Synthesizer Interface proposal that became the foundation of the MIDI spec. Smith presented the proposal at the October 1981 Audio Engineering Society convention. By 1982, engineers from Roland, Yamaha, Korg, Oberheim, and Sequential Circuits were collaborating on the final specification. The first public demonstration of MIDI occurred at the January 1983 NAMM show, when a Roland Jupiter-6 and a Sequential Circuits Prophet-600 — two competing instruments from two competing companies — played a synchronized sequence over a single cable. The MIDI 1.0 specification was formally published in August 1983. It has not been significantly revised since, which is both a testament to the elegance of the original design and a limitation that MIDI 2.0 addresses four decades later.

### 1983–1990: MIDI Conquers the Studio

The adoption of MIDI in the mid-1980s was one of the fastest technology diffusions in the history of professional audio. Within two years of the 1983 specification, virtually every new synthesizer, drum machine, and electronic keyboard shipped with MIDI ports. The Roland TR-808 and TR-909 drum machines — already culturally significant — gained new utility as MIDI-slaved rhythm generators in sequencer-driven productions. The Yamaha DX7, the best-selling synthesizer of all time, was deeply MIDI-programmable, and its patch librarian software — communicating over SysEx — established the model for all software-based hardware control that followed. Early MIDI sequencers like the Linn 9000, Oberheim DSX, and then the first software sequencers on Apple II and Commodore 64 computers created the compositional workflow that would evolve directly into the modern DAW piano roll. By 1990, the home studio was a reality precisely because MIDI allowed a single musician with a modest keyboard and a computer to drive an entire rack of synthesizers through a single composition interface.

### 1991–2010: Software Takes Over

The 1990s saw MIDI migrate from hardware sequencers to software DAWs with decisive speed. Cubase, Logic (originally Notator on the Atari ST), and later Ableton Live, Pro Tools, and FL Studio established the piano-roll and MIDI track paradigm that defines production workflow today. Virtual Studio Technology — the VST standard introduced by Steinberg in 1996 — allowed software instruments to receive MIDI directly inside the host application, eliminating the need for external hardware synthesizers while maintaining full MIDI compatibility. The General MIDI standard (1991) and its extension GM2 created a universal patch map ensuring that a MIDI file composed on one system would play back with approximately correct timbres on any GM-compatible device — enabling the distribution of interactive music for video games, mobile phones (MIDI ringtones), and web browsers. USB replaced the 5-pin DIN connector as the dominant MIDI physical interface by the early 2000s, simplifying studio cabling while maintaining the original protocol's byte structure entirely intact.

### 2020–Present: MIDI 2.0 and the Expressive Revolution

The MIDI Manufacturers Association ratified MIDI 2.0 in January 2020, the first major revision to the MIDI specification in 37 years. MIDI 2.0 is fully backward compatible with MIDI 1.0 via the MIDI Capability Inquiry (MIDI-CI) handshake system, which allows two connected devices to negotiate their capabilities before exchanging data. The headline improvements are transformative: note-level pitch, expression, and controller data replace the channel-level constraints of MIDI 1.0; 32-bit resolution replaces 7-bit resolution across all parameters; profile-based configuration allows instruments to automatically configure themselves to industry-standard setups; and property exchange enables complete instrument state transfer between devices. Hardware implementations of MIDI 2.0 have begun appearing in flagship synthesizers and controllers, and major DAW developers have been integrating MIDI 2.0 support into their platforms. The MPE (MIDI Polyphonic Expression) standard — an interim extension developed between MIDI 1.0 and 2.0, used by instruments like the ROLI Seaboard and LinnStrument — demonstrated the musical value of per-note expression and served as proof-of-concept for many MIDI 2.0 design decisions. As of the 2026-05-19 revision of this entry, MIDI 2.0 adoption in mainstream production tools is accelerating, with native support confirmed in Logic Pro X, Ableton Live, Bitwig Studio, and several hardware platforms.

> "Oblique strategies exist because the most useful thing you can do when stuck is to change the frame, not push harder."

— Brian Eno, Producer (U2, David Bowie, Talking Heads) | A Year With Swollen Appendices — Brian Eno's Diary

Eno's principle applies directly to the history of MIDI development itself — the MIDI 2.0 committee did not simply add more bits to the original protocol. They changed the frame entirely, moving from a unidirectional broadcast model to a bidirectional negotiation model, from channel-level expression to per-note expression, and from a fixed message set to a profile-based extensible architecture. Every producer working with emerging expressive controllers benefits from understanding this architectural shift.

MIDI was born from a 1983 inter-manufacturer collaboration, conquered the studio within a decade, migrated to software in the 1990s, and was fundamentally re-architected in MIDI 2.0 (2020) with 32-bit resolution, bidirectionality, and per-note expression — the most significant protocol evolution in the standard's four-decade history.

Professional MIDI workflow begins before you touch a controller. The first decision is routing: which MIDI channel receives performance input, which instrument is assigned to that channel, and whether the input is being monitored through the instrument in real time (MIDI Thru active) or recorded silently for later playback. In a DAW session, create a dedicated instrument track for each voice in your arrangement. Set the MIDI input on each track to the appropriate channel or to "All Channels" if you are routing from a single-channel controller and want the DAW to filter channel selection internally. Enable input monitoring on the track you intend to perform on, and confirm that the instrument plugin is loaded and responding before you hit record. This setup step takes sixty seconds and prevents the most common session-killing error: recording into the wrong track while an instrument on another channel makes sound, creating a permanently misrouted take.

Quantization is the single most misunderstood MIDI editing operation at the beginner-to-intermediate level. The reflex to full-quantize every MIDI performance to a 16th-note grid destroys the timing feel that makes a performance musical. Professional technique uses input quantization as a coarse guide — quantizing to the nearest 8th or 16th note to catch egregious timing errors — then applies swing or groove quantization to push or pull notes relative to the grid in a rhythmically intentional way. Most DAWs allow groove templates extracted from existing drum loops to be applied to MIDI note grids, physically aligning the swing feel of a programmed part to a sampled breakbeat. Beyond quantization, manually shifting individual notes by 5–15 milliseconds ahead of or behind the grid — anticipating beats on bass lines, dragging on hi-hats — creates the rhythmic tension and push-pull feel that separates programmed parts from mechanical data entry.

AbletonLogic ProFL StudioPro Tools

1\. Create a new MIDI Track (Cmd+Shift+T on Mac / Ctrl+Shift+T on PC). 2. Drag a virtual instrument (e.g., Ableton Wavetable) onto the track. 3. Click the pencil icon or press Cmd+B to draw MIDI notes directly in the Clip view. 4. Double-click a clip to open the Piano Roll — draw notes on the grid, click and drag up/down to set velocity in the velocity lane at the bottom. 5. Press Cmd+A to select all notes, then use Shift+drag in the velocity lane to scale velocities proportionally. 6. To add CC automation: click the envelope button in the Clip view, choose 'MIDI Ctrl' from the dropdown, select a CC number, and draw curves. 7. For humanization: select all notes, right-click > Humanize, or use the Random MIDI Effect device before the instrument. 8. Set your buffer size to 128 samples in Preferences > Audio for low-latency recording.

1\. Create a Software Instrument track (Option+Cmd+S) and assign a plugin (e.g., ES2, Alchemy, or Kontakt). 2. Record MIDI by pressing R with a MIDI keyboard connected, or draw a region on the track. 3. Double-click the MIDI region to open the Piano Roll editor. 4. Draw notes with the pencil tool (P), select with pointer (T). 5. Enable the Velocity lane at the bottom of the Piano Roll to view and edit per-note dynamics. 6. For CC automation: open the Piano Roll, go to View > Hyper Draw > Other, enter a CC number (e.g., 1 for mod wheel), and draw curves with the pencil. 7. Use Functions > MIDI Transform > Humanize to add velocity and timing variation automatically. 8. Check record latency compensation under Logic > Preferences > Audio > Devices — enable 'Software Monitoring' for best real-time feel.

1\. Open the Channel Rack (F6) and add a VST instrument or FL native plugin (e.g., Sytrus, FLEX). 2. Click the instrument's channel button to open its Piano Roll (F7). 3. Draw notes with the Draw tool (D key), set note length by drag width, velocity by drag height in the velocity lane at the bottom. 4. Right-click in the Piano Roll for quantize options — set grid snap via the snap controls at the top. 5. To add CC automation: in the Piano Roll go to Tools > Riff Machine or use the Event Editor (opened from the channel rack via the right-click > Edit Events menu) to draw CC curves. 6. For humanization: select notes, right-click > Randomize or use the Quick Quantize with a slight humanize percentage. 7. Route MIDI from an external controller by assigning it in Settings > MIDI > Controller and enabling it. 8. Use the Pattern Picker to build song arrangement from MIDI patterns dragged into the Playlist.

1\. Create an Instrument Track (Track > New > Instrument Track) and insert a virtual instrument plugin (e.g., Xpand!2, Structure, or third-party VST3/AAX). 2. Press Cmd+= to open the MIDI Editor, or double-click a MIDI clip on the track. 3. Select the Pencil tool to draw notes on the piano roll grid; use the grabber to select and move notes. 4. The velocity lane appears below the note grid — click individual note velocity stems to adjust, or use Event Operations > Change Velocity to scale selections. 5. For CC data: in the MIDI Editor, choose a controller lane from the Controller Data dropdown below the velocity lane and draw curves with the pencil. 6. Quantize selected notes via Event > Event Operations > Quantize (Option+0) — choose grid value and swing percentage. 7. Humanize via Event Operations > Humanize — set timing and velocity randomness ranges independently. 8. Set MIDI input in Setup > MIDI > Input Devices; manage hardware latency via Setup > Playback Engine buffer size settings.

Velocity editing deserves its own dedicated pass in every MIDI session. After recording or programming a part, open the velocity lane beneath the piano roll and look at the distribution. A flat line of identical velocity values is the most reliable signal that a part sounds programmed rather than performed. The fix is systematic but not complex: reduce velocities on the weaker beats (2 and 4 in a 4/4 bar, the "and" subdivisions), increase them slightly on the downbeats and points of rhythmic emphasis, and introduce occasional peak velocities (120+) on accented notes. Strings and brass programmed with CC11 (Expression) drawing smooth crescendo and decrescendo arcs across phrases — rather than just static velocities — transform from obviously digital to convincingly performed. Drum programming benefits from velocity variation on hi-hats above all other elements: a static 100-velocity 16th-note hi-hat pattern sounds like a click track. Alternating between 75, 85, and 95 with occasional 110 accents on every fourth 16th note creates the ghost-note dynamics that define professional programming.

CC automation is where MIDI programming graduates from competence to artistry. The workflow is to record or draw a first pass of CC data — often CC1 for modulation/vibrato, CC11 for dynamics, and pitch bend for any required interval slides — and then refine the curves in the automation editor. Avoid step-function changes between CC values; smooth interpolated ramps between values always sound more natural. On filter automation, use CC74 (filter brightness/cutoff on most virtual synths) to write filter sweeps that breathe with the arrangement, opening in choruses and closing in verses. This technique — automating filter position rather than relying on static patch settings — is one of the primary tools for creating perceived dynamic range in synthesizer-heavy productions without touching a single audio fader.

Professional MIDI workflow requires deliberate routing setup, surgical quantization that preserves human timing feel, systematic velocity editing that creates dynamic contrast, and CC automation that breathes life into programmed parts — treating MIDI programming as composition rather than data entry.

MIDI's application varies significantly across genres — from the hyper-quantized, grid-locked precision of electronic dance music to the lightly humanized, expressively nuanced piano rolls of contemporary R&B; and cinematic scoring. Understanding how each genre's aesthetic demands translate into specific MIDI programming techniques prevents the category error of applying EDM-style full quantization to a neo-soul production or using jazz-style loose timing in a techno track. The table below maps genre to MIDI programming priorities, typical quantization settings, and the CC parameters most heavily used in each context.

Genre| Ratio| Attack| Release| Threshold| Notes  
---|---|---|---|---|---  
Trap| N/A| 1/64 rolls| Velocity 40–127 swells| 808 pitch bend: ±2 semitones| Hi-hat rolls via rapid MIDI note repeat; 808 slides via pitch bend CC or portamento; quantize to 1/32nd grid with 55–60% swing  
Hip-Hop| N/A| Velocity 60–110 range| Note lengths 40–60% gate| Timing offset ±8–15ms human push| MPC-style 16-pad mapping; deliberate velocity variation per hit; swing at 54–58%; sample chops spread across C2–C5 note range  
House| N/A| Stab length: 1/16–1/8 note| CC74 filter sweep over 8 bars| Velocity 80–100 for stabs, 60–80 for pads| Arpeggiator synced to 1/8th notes; chord stabs with tight gate time; mod wheel automation driving filter cutoff; strict 4/4 quantize with no swing  
Electronic / Techno| N/A| Probability triggers 60–80%| Euclidean rhythm patterns| Pitch pool randomization ±semitone| Generative MIDI with step sequencers; CV-to-MIDI bridge for modular integration; long note sustains with aftertouch to mod wheel LFO routing; CC1 riding filter resonance  
Pop / R&B;| N/A| Velocity 50–115 live feel| Note overlap for legato pads| Pitch bend ±1 semitone for expression| Live keyboard performance recorded and lightly edited; velocity shaped to dynamic arc of the phrase; chord voicings spread 2+ octaves; mod wheel CC1 adding subtle vibrato on held notes  
  
Share Copy Link [Share on X](https://x.com/intent/tweet?text=MIDI+By+Genre+%E2%80%94+%40mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi%23genre-table) [Reddit](https://reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi%23genre-table&title=MIDI+By+Genre+%E2%80%94+MusicProductionWiki)

Across all genres, the guiding principle remains consistent: MIDI programming serves the emotional intent of the track. The technical parameters are tools for emotional precision, not ends in themselves. A perfectly quantized and velocity-calibrated piano part that sounds cold and lifeless has failed its purpose regardless of its technical execution. Conversely, a loosely timed, roughly velocitied sequence that makes the listener feel something has succeeded completely. Develop technical MIDI skills precisely so that execution stops being a barrier between your musical intent and the listener's emotional experience.

The choice between hardware MIDI instruments and software virtual instruments is a defining production decision that affects workflow, latency, tactile feel, and ultimately the character of the sounds you create. Hardware synthesizers and samplers offer the physical immediacy of real knobs, the analog circuits that software models only approximate, and the workflow constraint that some producers find creatively liberating. Software virtual instruments offer infinite polyphony, instant recall of every parameter via DAW automation, zero latency in internal MIDI routing, and access to a depth and variety of sounds that would require an entire room of hardware to replicate. Most professional studios run a hybrid approach — key hardware instruments for their irreplaceable sonic character, software for flexibility and scale.

Aspect | Hardware MIDI Instruments | Software Virtual Instruments  
---|---|---  
Latency | MIDI cable: sub-1ms; audio interface roundtrip adds 5–20ms depending on buffer | Internal MIDI routing: effectively zero; constrained only by audio buffer size  
Tactile Control | Physical knobs, sliders, and buttons with direct parameter access; mod wheel, pitch bend physically present | Mouse/trackpad control by default; requires MIDI controller for real-time CC manipulation  
Recall / Automation | SysEx patch recall; limited real-time MIDI CC automation depending on firmware | Complete parameter automation via DAW; instant snapshot recall; version control via project save  
Polyphony | Fixed voice count (4–128 voices depending on hardware); voice stealing at high note density | Effectively unlimited polyphony constrained only by CPU; scales with host processing power  
Sound Character | Genuine analog circuitry, discrete components, hardware non-linearities not fully software-modelable | Digital precision with optional analog modeling; physically modeled instruments achieving near-hardware accuracy  
MIDI 2.0 Support | Emerging in flagship hardware (2022–present); most vintage hardware MIDI 1.0 only | Native MIDI 2.0 in current-gen DAWs and instruments; 32-bit resolution, per-note expression fully available  
  
Free Tier

MIDI Monitor Snoize

Surge XT Surge Synth Team

Mid Tier

MIDI Guitar 2 Jam Origin

Cthulhu Xfer Records

Pro Tier

Pianoteq 8 Modartt

Max for Live Cycling '74 / Ableton

The practical recommendation for modern productions is to record hardware MIDI instruments in real time via an audio interface — capturing their irreplaceable analog character as audio while keeping the MIDI track active for re-triggering if needed — and to use software virtual instruments for all parts where patch recall, automation depth, and polyphony are the primary requirements. When using hardware, always record the MIDI sequence simultaneously with the audio output, even if you plan to use the audio recording in the final mix. The MIDI backup ensures you can re-trigger the hardware with different patch settings or reroute to a software instrument if the hardware develops issues — a practical necessity for any professional session where recall and reproducibility matter.

Before

Without deliberate MIDI programming, sequences sound mechanical and lifeless — every note hits with identical force, sustains for the same robotic duration, and sits perfectly on a quantized grid that removes all sense of human timing. The result is a technically correct arrangement that feels emotionally inert, like a player-piano roll rather than a performance.

After

With intentional velocity shaping, micro-timing humanization, CC automation for filter and expression, and appropriate gate times, the same MIDI sequence transforms into something that breathes and moves — dynamics swell with the phrase, notes push and pull against the grid like a live player, and the instrument's sample layers open and close with the music's emotional arc.

The transformation from a flat, unanimated MIDI sequence to a fully humanized, CC-automated performance represents one of the most dramatic quality leaps in production workflow. A raw MIDI recording with every note at velocity 100, perfectly quantized to a 16th-note grid, and no CC data, sounds unmistakably digital — the mechanical evenness communicates clearly to any listener that no human actually performed this part. The same sequence after velocity editing (range spread across 65–110 with deliberate accents), light groove quantization (8 ms 16th-note swing offset), CC11 expression curves drawn through each phrase, and CC1 vibrato onset delayed 250ms past the start of long notes transforms into something that communicates performance intention and human feel. The before-state fails the track. The after-state serves it. This transformation requires no additional plugins, no additional recording time, and no additional hardware — it is entirely a MIDI editing discipline applied to data that already exists in the session.

The following tracks represent MIDI programming across a range of genres, eras, and production philosophies. Each demonstrates a specific aspect of MIDI's expressive capability — from the precise velocity layering of electronic dance music to the polyrhythmic complexity of experimental hip-hop to the CC-driven breathing quality of ambient composition. Listen actively to the elements identified in each listening guide; train your ear to hear MIDI programming decisions as compositional choices rather than technical execution.

Daft Punk — One More Time (2000), _Discovery_. Produced by Daft Punk.

The entire intro arpeggio and chord sequence is MIDI-driven synthesizer programming with precise velocity layers giving it that mechanical-yet-musical bounce. Note how the note lengths and spacing create groove that would be impossible to replicate with pure audio editing.

Kanye West — All Falls Down (2004), _The College Dropout_. Produced by Kanye West.

No I.D.'s soul sample is chopped and re-triggered via MIDI note programming in an MPC, with each hit mapped to a different pad pitch to reconstruct the melody. The slight velocity variation between hits is the human feel MIDI quantization preserves rather than destroys when used well.

Justice — D.A.N.C.E. (2007), _Cross_. Produced by Justice.

The synth bass and arpeggiated chord stabs are MIDI sequenced with tight quantization and deliberate note-overlap programming to create legato portamento slides between pitches. Listen for how the pitch bend CC data — not just note-on events — sculpts the filter-sweep feel of the bass line.

Flying Lotus — Zodiac Shit (2010), _Cosmogramma_. Produced by Flying Lotus.

The rhythmic complexity here comes entirely from MIDI note timing — polyrhythmic hi-hat patterns built with precise 32nd-note offsets that a purely loop-based approach could never achieve. Note how modulation wheel CC data is riding through the strings creating that undulating, breathing quality.

Disclosure — Latch (2012), _Settle_. Produced by Disclosure.

The iconic synth progression is pure MIDI piano-roll work — each chord voiced across octaves with velocity humanization that prevents the robotic feel of straight-quantized chords. The slight timing push on the root notes gives the groove its forward momentum.

Aphex Twin — Xtal (1992), _Selected Ambient Works 85–92_. Produced by Aphex Twin.

Richard James was sequencing MIDI at 15 on a heavily customized setup — the melodic counterpoint here is multiple MIDI channels running different synths in precise rhythmic relationship, each with independent filter automation via CC data. The sustained, breathing quality comes from aftertouch and modulation routed to filter cutoff.

Timbaland — Are You That Somebody (1998), _Dr. Dolittle (Soundtrack)_. Produced by Timbaland.

Timbaland's baby-voice percussion and synth bass are all MIDI-triggered samples mapped across a keyboard/MPC grid, with velocity sensitivity creating the loud-soft dynamics in the percussion patterns. The micro-timing shifts between elements — slightly ahead or behind the grid — are deliberate MIDI note offsets, not quantization artifacts.

Burial — Archangel (2007), _Untrue_. Produced by Burial.

Burial famously programmed his tracks in Soundforge rather than a DAW, but the pitched vocal chops function exactly as MIDI-mapped sample playback — each fragment assigned a pitch value and triggered with specific timing. The humanized, slightly rushed feel of the chord pads demonstrates how deliberate detuning of MIDI note pitch and velocity creates emotional warmth.

Across these eight tracks, notice how the most emotionally resonant MIDI programming moments are not the most technically complex ones. The slight velocity variation in Disclosure's "Latch" chords creates more musical warmth than a theoretically perfect voicing played at static velocity. The micro-timing shifts in Timbaland's percussion grid create more rhythmic tension than perfectly quantized 16th notes could achieve. The CC-driven modulation in Aphex Twin's "Xtal" creates more expressive depth than the note data alone. MIDI's power is not in its precision — it is in the producer's intentional control of every parameter that precision makes available.

MIDI vs Audio (WAV/Audio Clip)

See the full comparison: Audio (WAV/Audio Clip)

MIDI vs CV (Control Voltage)

See the full comparison: CV (Control Voltage)

MIDI manifests in several distinct operational forms that serve different production contexts. Understanding the differences between these MIDI types — hardware MIDI, software MIDI, MPE, MIDI 2.0, and OSC (which shares conceptual territory) — determines which tools and workflows are appropriate for each production scenario. The types below represent the primary MIDI implementation categories a working producer encounters regularly.

Classic MIDI 1.0 (5-Pin DIN) Hardware: 5-pin DIN cable, MIDI interface, MIDI merge/thru box

The original 1983 specification transmitted over 5-pin DIN serial cable at 31,250 baud. Channel-based, 7-bit resolution per parameter, unidirectional. Still the universal baseline — every MIDI device manufactured since 1983 implements it. Use classic MIDI 1.0 for all legacy hardware integration: vintage synths, drum machines, hardware samplers, and any studio equipment manufactured before 2019. Its limitations (7-bit CC resolution, 16 channels maximum, channel-level rather than per-note expression) are well-understood and manageable within those constraints.

USB MIDI Hardware: USB MIDI interface, USB-C/B to host, class-compliant controllers

USB MIDI replaces the 5-pin DIN physical connection while preserving the original MIDI 1.0 byte protocol entirely. Class-compliant USB MIDI devices require no driver installation on modern operating systems. USB MIDI supports higher bandwidth than 5-pin DIN, allowing multiple virtual MIDI ports (up to 16 or more) over a single USB connection — effectively multiplying the 16-channel limit by the number of virtual ports. Latency is typically lower than 5-pin DIN in direct DAW connections. The standard physical interface for contemporary MIDI controllers, keyboards, pad controllers, and MIDI-capable audio interfaces.

Internal / Virtual MIDI Software: DAW internal bus, virtual MIDI routing, IAC Driver (macOS), loopMIDI (Windows)

Inside a DAW, MIDI routing between tracks, instruments, and plugins operates entirely in software with effectively zero latency. A MIDI track can route its output to any virtual instrument plugin on any other track, enabling complex generative setups where a single MIDI sequence drives multiple instruments simultaneously. External software can communicate with DAW internal MIDI via virtual MIDI buses — the IAC Driver on macOS or loopMIDI on Windows creates virtual ports that appear to all applications as hardware MIDI interfaces. Use virtual MIDI for: routing generative MIDI from one plugin to another, connecting modular software environments like Max/MSP to a DAW, and building complex MIDI processing chains with arpeggiators and chord generators in series.

MPE (MIDI Polyphonic Expression) Hardware: ROLI Seaboard, Haken Continuum, LinnStrument, Sensel Morph, Expressive E Osmose

MPE is an extension of MIDI 1.0 that assigns each note to its own individual MIDI channel, enabling per-note pitch bend, pressure, and slide data without channel conflicts. By using channels 2–16 for individual notes (channel 1 or 16 as a global channel for shared parameters), MPE allows a performer to bend one note up while holding another note steady, to increase pressure on one finger independently of another, and to slide horizontally on one note while stationary on others. MPE instruments fundamentally change the expressive vocabulary available to MIDI performance, approximating the continuous control of acoustic string and wind instruments. Logic Pro X, Ableton Live, Bitwig Studio, and Reaper all include native MPE support as of 2026.

MIDI 2.0 Hardware: Emerging flagship synthesizers (Yamaha, Roland, ROLI 2020+); Software: Logic Pro X 10.8+, Bitwig 5+

MIDI 2.0 is the complete architectural revision ratified in 2020. It is backward compatible with MIDI 1.0 via MIDI-CI handshaking. Key advances: 32-bit resolution per note (4 billion+ steps versus 128 in MIDI 1.0), per-note pitch bend and expression without MPE's channel assignment workaround, bidirectional communication enabling instruments to report their own capabilities, profile-based auto-configuration, and property exchange for complete parameter transfer between devices. MIDI 2.0 data uses Universal MIDI Packets (UMP) — a new word-aligned message format that is more efficient for USB and network transmission. For producers, the practical implication is that filter automation, pitch bend, and velocity data will be dramatically more smooth and expressive on MIDI 2.0-capable instruments — no more audible stepping on slow filter sweeps.

MIDI over Network (RTP-MIDI / AppleMIDI) Software/Network: macOS/iOS Network MIDI, rtpMIDI (Windows), TouchOSC, class-compliant network interfaces

MIDI over IP (RTP-MIDI) transmits MIDI messages over local area networks with error correction and jitter compensation, enabling wireless MIDI control from iOS/Android devices, remote studio connections, and multi-room studio synchronization without physical cable runs. Apple's built-in Network MIDI in macOS/iOS makes iPad or iPhone apps into wireless MIDI controllers and sound modules with minimal setup. Latency on a local WiFi network is typically 3–10ms — suitable for most studio applications but not ideal for live performance where sub-2ms response is preferable. Use for: iPad as wireless MIDI controller, sending MIDI between computers in the same studio, integrating mobile devices into a DAW session without USB cables.

MIDI exists in six primary operational forms — classic 5-pin DIN, USB, internal/virtual, MPE, MIDI 2.0, and network MIDI — each suited to specific production contexts, with MIDI 2.0 representing the future-facing standard and classic MIDI 1.0 remaining the universal legacy baseline that every serious producer must understand completely.

◆ The Producer's Verdict ◆

_MIDI is not a recording format and not a sound — it is a compositional language. Every producer who treats it as mere data entry is leaving the majority of its expressive power untouched. The producers who dominate with MIDI are the ones who understand that velocity is dynamics, CC automation is phrasing, pitch bend is articulation, and timing offsets are feel. MIDI programming at the professional level is indistinguishable from composition — because it is composition._

Creative Priority Composition First Program the musical idea; choose the sound later

Velocity Discipline Always Varied Flat velocity is the primary signal of amateur programming

Quantization Approach Groove Over Grid Full quantization erases feel; swing and offset create it

CC Automation Essential, Not Optional Unautomated MIDI is a sketch; CC automation is the final painting

MIDI 2.0 Readiness Learn It Now 32-bit resolution and per-note expression will redefine expressiveness

Hardware vs. Software Hybrid Always Hardware character + software flexibility = complete MIDI toolkit

Copy Verdict [Share on X](https://twitter.com/intent/tweet?text=MIDI+Producer%27s+Verdict+%40MusicProductionWiki) [Reddit](https://reddit.com/submit?title=MIDI+Producer%27s+Bible+Entry&url=https://musicproductionwiki.com/bible/midi)

_MIDI has been the invisible infrastructure of modern music for over four decades because it solved the right problem: separating musical intent from sonic execution. Masters of MIDI — from Aphex Twin's teenage polyrhythmic sequencing to Timbaland's velocity-calibrated drum programming to Daft Punk's precision arpeggio architecture — use the same 7-bit protocol that every bedroom producer has access to. The gap between them and everyone else is not the tools. It is the depth of understanding applied to those tools. Treat every MIDI lane as a composition decision. That is where the music actually lives._

MIDI errors are insidious precisely because they hide in plain sight — the session plays back, the notes trigger, the mix appears functional — but subtle programming mistakes accumulate into a cumulative flatness that makes a production sound programmed rather than performed. These are the six MIDI mistakes that appear most consistently in intermediate-level sessions reviewed by professional producers, along with the specific corrections that resolve them.

Uniform Velocity Across All Notes

Recording or drawing every note at the same velocity — most commonly 100 or 127 — is the single most reliable indicator of amateur MIDI programming. Human performances across every instrument category produce velocity variation as a natural consequence of physical movement, musical emphasis, and rhythmic feel. Fix: After recording or programming a part, open the velocity lane and create a deliberate hierarchy — downbeats and melodic peaks at 95–110, passing tones and weak beats at 65–80, ghost notes and off-beat subdivisions at 40–65. This three-tier velocity structure immediately adds musical depth to any part.

Over-Quantizing to Hard 16th-Note Grid

Full-quantizing every performance to a rigid 16th-note grid removes the micro-timing variations that create rhythmic feel. The result is a mechanical evenness that communicates digital origin immediately to trained ears. Fix: Use relative quantization at 75–85% strength rather than 100% to preserve the character of the original performance while tightening obvious errors. Apply groove templates extracted from your drum loop to align the MIDI part's timing feel to the rhythmic source of the track. For programmed parts, manually offset notes ±5–15 ms from the grid on non-accented beats to create natural timing variation.

Ignoring CC Automation Entirely

A MIDI sequence with note and velocity data but no CC automation is a sketch — it communicates the pitches and rough dynamics of the performance but none of its expression, phrasing, or tonal evolution. Orchestral programming without CC11 expression curves sounds like a MIDI demo. Synthesizer bass lines without CC74 filter automation sound static regardless of the patch quality. Fix: As a minimum viable standard, every melodic and harmonic MIDI part should have CC11 (Expression) automation drawn for phrase-level dynamics. String and brass parts should additionally have CC1 (vibrato) onset delayed past the attack of long notes. Filter automation should be present on any synthesizer part where the patch's static filter position does not serve the arrangement context.

Note Length Neglect on Non-Piano Instruments

Copy-pasting piano-style note lengths onto wind, brass, or string MIDI parts produces obviously incorrect articulation. A legato string line requires overlapping notes (note-on before previous note-off) to trigger legato transitions. A staccato brass hit requires note durations of 20–30% of the beat value rather than 80–90%. Synthesizer leads require deliberate legato overlaps or precise gaps depending on whether mono legato or polyphonic portamento is the intended articulation. Fix: After programming any non-piano MIDI part, edit note lengths in the piano roll to match the natural articulation of the target instrument. Most professional sample libraries are scripted to respond correctly to note length — the library does the heavy lifting once your MIDI note durations are accurate.

Stuck Notes and MIDI Panic Dependence

Relying on the DAW's MIDI Panic function to clear stuck notes is a symptomatic fix for a routing or programming problem that needs to be addressed at the source. Stuck notes occur when Note Off messages are dropped — typically due to abrupt DAW stop during playback, buffer overflows on overloaded MIDI interfaces, or routing configurations where a MIDI channel receives Note On messages from two separate sources. Fix: Audit your MIDI routing matrix. Ensure each instrument track receives MIDI from exactly one source. If stuck notes appear consistently on a specific hardware device, check the cable and interface for data integrity issues. Program Note Off messages explicitly in complex sequences rather than relying on DAW note-end inference.

Pitch Bend Left at Center With No Programming

Pitch bend is one of the highest-resolution parameters in MIDI 1.0 (14-bit, 16,384 steps) and one of the most consistently ignored in programmed productions. The default position — center, no movement — leaves an entire dimension of expressive articulation unused on every lead line, bass part, and melodic instrument in the session. Human guitar, violin, and wind performances are characterized by constant subtle pitch movement — vibrato, bends into and out of notes, slides between intervals. Fix: On lead synth lines, draw pitch bend curves for bends into target notes (starting ±1 semitone below or above and resolving over 50–150ms). On bass lines, add ±0.1–0.3 semitone pitch bend wobbles to simulate the natural intonation variation of a live bass player. On long string and brass notes, use pitch bend to add subtle vibrato onset after the attack phase.

The six most damaging MIDI mistakes — uniform velocity, over-quantization, no CC automation, wrong note lengths, stuck notes, and ignored pitch bend — are all editorial disciplines, not technical limitations. Correcting them transforms programmed MIDI from obviously digital to convincingly musical without changing a single audio processing parameter.

#### Red Flags

  * 🔴 Every note is perfectly quantized to the grid with identical velocity — sounds robotic, kills groove, and immediately signals amateur programming to any listener with trained ears.
  * 🔴 Using program change messages mid-session without testing for latency — many hardware synths take 10–50ms to respond, causing audible clicks or missed note-ons during live performance.
  * 🔴 Ignoring MIDI channel assignments and stacking all instruments on Channel 1 — creates routing chaos when using multi-timbral hardware, external synths, or live performance setups.



#### Green Flags

  * 🟢 Velocity humanization applied to all programmed parts — even subtle 5–15 point random variation across repeated notes transforms mechanical sequences into performances.
  * 🟢 MIDI clips organized into clearly labeled, color-coded tracks with descriptive names rather than the default 'MIDI 1, MIDI 2' — indicates a professional workflow that can be revisited months later without confusion.
  * 🟢 Deliberate use of note overlap and legato programming for melodic synths, exploiting the instrument's portamento or legato mode for smoother, more expressive lines.



When working with MIDI in complex multi-instrument sessions, the most important operational discipline is maintaining a clean, documented routing matrix. Label every MIDI track with its channel assignment and target instrument before the session begins. Use color coding in your DAW to distinguish MIDI programming layers — melodic, harmonic, percussive, CC automation — at a glance. Save CC automation data embedded in the MIDI clip rather than as separate DAW automation lanes where possible, so that the MIDI sequence is self-contained and portable across different DAW projects and template setups. For hardware-dependent sessions, document SysEx patch numbers and bank select messages alongside the MIDI routing notes, ensuring that the session can be recalled identically six months later without guesswork about which hardware patch was active on each channel. MIDI is only as reliable as the documentation surrounding it — the protocol itself is lossless and perfectly repeatable, but human memory of which patch was loaded on channel 7 is not.

Developing MIDI proficiency follows a clear progression from foundational understanding through compositional mastery. Each stage builds on the previous — there are no shortcuts that bypass the note-entry and routing fundamentals at the beginner level, just as there is no intermediate CC automation skill without first internalizing the parameter architecture. The three stages below map to practical production competencies with specific milestones at each level.

Beginner

Master the foundational MIDI routing and recording workflow: create instrument tracks, assign MIDI channels, record live performances, and edit notes in the piano roll. Understand the note number/velocity/duration triad at the conceptual and practical level. Learn to quantize intelligently — using partial quantization strength and snap-to-grid settings appropriate for the musical context. Practice selecting, transposing, and lengthening note ranges in the piano roll editor. Learn the MIDI Panic function and understand why stuck notes occur. Begin experimenting with velocity editing by manually adjusting note velocities on drum programming — set hi-hats to alternating velocity values rather than uniform values and hear the immediate improvement in musical feel.

Intermediate

Internalize the CC parameter map — know CC1, CC7, CC10, CC11, CC64, and CC74 by number and function without reference. Develop the habit of drawing CC11 expression automation on every melodic and harmonic MIDI part as a standard workflow step, not an afterthought. Learn groove quantization: extract groove templates from drum loops and apply them to melodic MIDI parts to create rhythmic cohesion across the arrangement. Explore pitch bend programming — draw bends into and out of notes on lead synth lines and bass parts. Begin using MIDI 1.0 routing for hardware integration: connect an external synthesizer or drum machine, configure MIDI channels correctly, and record simultaneous MIDI and audio outputs. Investigate MPE-capable instruments if expressive live performance is part of your workflow.

Advanced

Operate at the compositional level with MIDI: treat every parameter — note timing, velocity, pitch bend, CC automation, aftertouch, note length — as a deliberate compositional decision rather than a default setting. Develop fluency with MIDI-CI and MIDI 2.0 capabilities in your DAW and connected hardware. Build MIDI processing chains using arpeggiators, chord generators, and MIDI effect plugins in series to create generative compositional tools. Master SysEx for complete hardware patch control and recall. Explore polyrhythmic MIDI programming — 5-against-4 and 7-against-4 note patterns in the piano roll that create the metric complexity found in the most sophisticated electronic productions. Use MIDI to drive side-chain relationships, gate triggers, and modular synthesis via CV/Gate conversion, extending MIDI's reach beyond traditional synthesizer control into the full scope of electronic instrument integration.

MIDI proficiency progresses from basic routing and note entry through CC automation and groove quantization to full compositional mastery of all parameters — a progression that ultimately transforms MIDI from a recording convenience into the primary compositional instrument of modern production.

## Tools for This Entry

MusicProductionWiki.com

◆ The Producer's Bible

Gain Reduction Calculator

Calculate exactly how much your compressor attenuates the signal. Enter threshold, ratio, and input level to get gain reduction, output level, and a visual GR meter.

Input (dBFS)

Threshold (dBFS)

Ratio

Makeup Gain (dB)

Gain Reduction

0.0

dB

Over Threshold

+0.0

dB

Output Level

-10.0

dBFS

Final (+ makeup)

-10.0

dBFS

Gain Reduction Meter

0 dB-6 dB -12 dB-20+ dB

Set threshold below your input level to engage compression.

Ratio Presets

1.5 : 1Transparent

2 : 1Glue / bus

4 : 1Classic / vocals

6 : 1Moderate / drums

10 : 1Heavy / limiting

∞ : 1Brick wall

Source Presets

Vocals-18 / +6 / 4:1

Drum bus-24 / +8 / 6:1

Acoustic guitar-20 / +4 / 3:1

Mix bus glue-12 / +3 / 2:1

Limiter stage-10 / +2 / 10:1

Bass / 808-30 / +8 / 4:1

Formula: GR = (Input - Threshold) x (1 - 1/Ratio) when input exceeds threshold. At 4:1 with -10 dBFS input and -18 dB threshold: 8 dB excess = 6 dB GR. Makeup gain restores level without affecting GR.

◆ The Producer's Bible -- MusicProductionWiki.comCopy Link[𝕏 Share](https://x.com/intent/tweet?text=Gain+Reduction+Calculator+%E2%80%94+%40mpwikiofficial&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi%23tools)[Reddit](https://reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi%23tools&title=Gain+Reduction+Calculator)

What level did this entry match?

Beginner Intermediate Advanced

What's missing? (optional)

Send

Thanks — your feedback shapes future entries. ✓

## Related Guides & Tools

[Best MIDI ControllersThe best MIDI controllers of 2026 reviewed — from compact 25-key keyboards to full 88-key…](/articles/best-midi-controllers)

## Also in The Bible

[OscillatorThe oscillator is the sound-generating engine inside a synthesizer that receives MIDI note data and converts pitch numbers into audio waveforms.](/bible/oscillator) [LFOLow Frequency Oscillators are commonly modulated via MIDI CC messages — especially the modulation wheel (CC1) — to add vibrato, tremolo, or filter movement to synth parts.](/bible/lfo) [ADSRThe ADSR envelope shapes how a synthesizer responds to MIDI note-on and note-off messages, determining the attack, decay, sustain, and release of each triggered note.](/bible/adsr) [AutomationDAW automation and MIDI CC automation both control parameters over time, but MIDI CC is embedded within MIDI clips and moves with them, while DAW automation is tied to the timeline.](/bible/automation) [EnvelopeEnvelopes in synthesizers are directly triggered by MIDI note-on events, making MIDI velocity and timing the primary levers for shaping the dynamic contour of programmed sounds.](/bible/envelope) [Wavetable SynthesisWavetable synthesizers use MIDI note data to select and scan through wave tables, with CC and pitch bend messages enabling real-time timbre morphing integral to modern sound design.](/bible/wavetable-synthesis)

#### Contents

Definition How It Works Parameters Quick Ref Tools Signal Chain History How To Use By Genre Hardware vs Plugin Before / After In The Wild Types Plugins Mistakes Flags Progression FAQ Related

### Producer Spotlight

Daft Punk

Producer

Kanye West

Producer

#### Share This Entry

Copy Link [Share on X](https://x.com/intent/tweet?text=MIDI+%E2%80%94+The+Producer%27s+Bible&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi) [Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi&title=MIDI+%E2%80%94+The+Producer%27s+Bible)

#### The Producer's Briefing

Weekly technique + gear intel. Free.

Subscribe Free

The Producer's Briefing

The Producer's Briefing — practical technique, gear intel, no fluff.

Subscribe Free

[◆ The Producer's Bible](/bible/)

MusicProductionWiki.com

The most comprehensive music production reference on the internet.

Share [X](https://x.com/intent/tweet?text=MIDI+%E2%80%94+The+Producer%27s+Bible&url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi) [Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fmusicproductionwiki.com%2Fbible%2Fmidi&title=MIDI+%E2%80%94+The+Producer%27s+Bible)

[Home](/) * [About](/about) * [Producer's Bible](/bible/) * [Techniques](/categories/techniques) * [Reviews](/categories/reviews) * [Comparisons](/categories/comparisons)

(C) 2026 MusicProductionWiki.com -- Built for producers, by producers.

↑
