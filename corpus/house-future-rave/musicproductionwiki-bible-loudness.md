---
titre: "Music Production Wiki — Bible : Loudness (LUFS intégré/short-term/momentary, true peak, crest factor, LRA, cibles plateformes, exemples mesurés)"
source: https://raw.githubusercontent.com/musicproductionwiki/musicproductionwiki/master/bible/loudness.html
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
  5. Loudness



Levels & Headroom noun · perceptual & measured audio intensity 2026 Edition

# Loudness

/ˈlaʊdnəs/

Quick Answer Definition How It Works Parameters Quick Reference History How To Use It In The Wild Types Mistakes Calculator Related Further Reading FAQ

Loudness is the perceived intensity of a sound, measured in LUFS (Loudness Units relative to Full Scale). It governs mastering targets, streaming normalization, and how energetic a mix feels to listeners.

Hear The Difference

Dry vs Processed — Loudness

🎵 Audio examples coming soon — check back shortly.

Dry Processed

## 01 Definition

Every producer has crushed a mix into a brick wall chasing loudness — and every one of them has watched it die on a streaming platform that quietly turned it back down. Understanding loudness means never making that trade again.

Loudness is the subjective perception of how intense a sound is, shaped by amplitude, frequency content, duration, and the nonlinear response of human hearing. It is distinct from level — a sine wave at −6 dBFS and a spectrally dense mix at −6 dBFS will not sound equally loud, because the ear integrates energy across time and weights different frequency bands unequally. This gap between digital level and perceived loudness is what drove the loudness war of the 1990s–2010s and what makes LUFS metering indispensable in contemporary production.

The modern standard unit for measuring loudness is LUFS — Loudness Units relative to Full Scale — defined by the ITU-R BS.1770 specification and its derivatives. An integrated LUFS measurement averages the loudness of an entire program, while short-term LUFS captures a three-second window and momentary LUFS reflects a 400-millisecond snapshot. These measurements model human auditory perception through a K-weighting filter: a gentle high-shelf boost above 2 kHz combined with a high-pass below 60 Hz, reflecting the ear's greater sensitivity to mid and high frequencies and its attenuation of deep low-end. True Peak measurement accompanies LUFS to catch inter-sample peaks that exceed 0 dBFS during D/A conversion, a common artifact of peak-normalized masters.

Streaming platforms have fundamentally redefined what loudness means in practice. Spotify normalizes playback to −14 LUFS integrated, Apple Music and Tidal to −16 LUFS, and YouTube to −14 LUFS. Masters louder than these targets are turned down in gain; masters quieter are left as-is or, on some platforms, turned up. This normalization architecture means that a master slammed to −7 LUFS integrated does not arrive at the listener louder than one at −14 LUFS — it arrives with roughly 7 dB of dynamic range destroyed and no competitive advantage. The incentive to over-limit has structurally collapsed. Producers and mastering engineers who understand this deliver masters with headroom, transient punch, and natural dynamic contrast that survive normalization and translate with authority.

Loudness interacts with every stage of the signal chain. At the tracking stage, consistent gain staging prevents accumulated distortion and gives processors the headroom they need to behave predictably. During mixing, loudness balance between elements — kick versus bass, vocal versus guitars — is the craft of level management and spectral carving. At mastering, integrated loudness is the final deliverable spec, alongside True Peak ceiling (typically −1 dBTP for streaming, −2 dBTP when encoding to lossy formats). A mastering engineer working to a brief of −14 LUFS integrated with a −1 dBTP ceiling has a concrete, measurable target, not an aesthetic judgment about whether something sounds loud enough.

Perceived loudness is also a compositional and arrangement tool. A track that sits at −16 LUFS with consistent energy and minimal dynamic variation may feel louder than a −14 LUFS track with large macro-dynamic swings between verse and chorus, because the brain adapts to the average intensity level. The relationship between statistical loudness (LUFS), peak level (dBFS), crest factor (the difference between the two), and perceived density is what separates engineers who understand loudness from those who simply chase numbers on a meter.

## 02 How It Works

Loudness measurement under ITU-R BS.1770 begins with a K-weighting filter applied to each audio channel before energy summation. K-weighting consists of two stages: a high-shelf pre-filter with approximately +4 dB gain above 1.5 kHz (modeling the acoustic effect of the head on the eardrum) and a high-pass RLB filter rolling off below roughly 60 Hz. After K-weighting, the mean square of each channel is computed, channels are summed with a loudness coefficient (center and LFE channels receive different weights in multichannel formats), and the result is expressed on a logarithmic scale relative to full scale. Integrated LUFS applies a gating mechanism: blocks of audio more than 10 LU below the ungated average are excluded, preventing silent passages from dragging the measurement downward and giving a truer picture of the audible program material.

True Peak measurement addresses a specific failure mode of peak metering: inter-sample peaks. When a PCM signal is converted back to analog, the reconstruction filter interpolates between sample values. It is entirely possible for the interpolated waveform between two samples to exceed 0 dBFS even when no individual sample does — an inter-sample peak. This is particularly common in content with significant high-frequency energy and after lossy encoding (AAC, MP3), where codec artifacts can add 1–3 dB of transient energy. True Peak meters oversample the signal (typically 4× to 8×) to detect and display these intersample excursions. A True Peak ceiling of −1 dBTP gives 1 dB of margin for codec-induced overshoot; −2 dBTP is conservative and appropriate for maximum streaming platform safety.

The relationship between LUFS and perceived loudness involves several psychoacoustic effects beyond pure amplitude. The Fletcher-Munson equal-loudness contours (updated as ISO 226:2003) show that human hearing is most sensitive between approximately 2 kHz and 5 kHz, and significantly less sensitive at low frequencies at moderate listening levels. A mix with substantial energy in the 2–5 kHz presence region will measure louder perceptually than its LUFS reading might suggest relative to a bass-heavy mix at the same integrated measurement. Spectral loudness balance — the distribution of energy across the frequency spectrum — is therefore as important as the aggregate loudness number. Producers mastering for electronic music, where sub-bass content is heavy, may find that hitting −14 LUFS integrated while maintaining low-end power requires more aggressive high-frequency limiting control or multiband management than a guitar-forward mix at the same target.

Dynamic range and loudness are inversely related by the physics of headroom. A signal with a crest factor of 14 dB (the difference between its True Peak and its integrated loudness) has significant transient headroom and will sound punchy and three-dimensional. Reducing crest factor to 6 dB through hard limiting raises integrated loudness while compressing micro-dynamic detail. Modern loudness-normalized streaming environments reward higher crest factors: a master at −14 LUFS with a 12 dB crest factor and a master at −7 LUFS with a 5 dB crest factor will be played back at nearly identical perceived volumes, but the former preserves transient character that translates to listener engagement, emotional punch, and, critically, better performance in A/B comparisons on high-resolution playback systems.

Short-term and momentary LUFS readings are the working tools of a mix session, not just mastering. Momentary LUFS on individual buses — kick, bass, vocals — shows relative contribution to the mix's overall loudness in real time. Engineers targeting a final integrated master of −14 LUFS typically work with a mix that peaks short-term between −12 and −10 LUFS at its loudest passages, leaving 2–4 LU of mastering headroom for limiting and saturation without over-compression. This working headroom is the practical link between mix loudness management and the final deliverable specification.

Diagram comparing an over-limited brick-wall master versus a dynamic master at the same streaming playback level, showing crest factor, LUFS targets, and True Peak ceiling. Brick-wall vs dynamic master at equal streaming loudness, with LUFS and True Peak markersLOUDNESS — BRICK-WALL VS DYNAMIC MASTER (EQUAL LUFS AFTER NORMALIZATION)0 dBTP−1 dBTP−14 LUFS−∞BRICK-WALL MASTER−7 LUFS int / 4 dB crestHIGH DENSITYLOW DYNAMIC RANGEcrushed transientsDYNAMIC MASTER−14 LUFS int / 12 dB crestpeak −1 dBTPavg ≈ −14 LUFSstreaming normalizesboth to −14 LUFSbrick wall getsturned DOWN 7 dB

Diagram — Loudness: Diagram comparing an over-limited brick-wall master versus a dynamic master at the same streaming playback level, showing crest factor, LUFS targets, and True Peak ceiling.

## 03 The Parameters

Every loudness — hardware or plugin — operates on the same core parameters. Know these and you can work with any implementation.

INTEGRATED LUFS

Average loudness over the full program duration

Integrated LUFS is the primary deliverable specification for mastering to streaming platforms. It time-averages K-weighted loudness across the entire track, excluding gated (near-silent) passages. Target −14 LUFS for Spotify and YouTube, −16 LUFS for Apple Music and Tidal, −23 LUFS for broadcast (EBU R128). Submitting a master at −7 LUFS integrated results in roughly 7 dB of gain reduction on playback — identical loudness, destroyed dynamics.

TRUE PEAK (dBTP)

Inter-sample peak ceiling after oversampled reconstruction

True Peak detects amplitude excursions between PCM samples by oversampling (typically 4×–8×) the signal and examining the reconstructed waveform. The standard ceiling for streaming is −1 dBTP; for lossy codec delivery (MP3, AAC) use −2 dBTP to absorb encoder-induced overshoot of 0.5–1.5 dB. Exceeding 0 dBTP causes clipping in the D/A converter and audible distortion on consumer playback, even when no individual PCM sample clips.

SHORT-TERM LUFS

3-second rolling loudness window for section-level monitoring

Short-term LUFS measures the K-weighted loudness of the most recent 3 seconds, updating every 100 ms. It reveals loudness variation between sections — verse, chorus, breakdown — and is the most useful meter for real-time mix work. A well-structured mix targeting −14 LUFS integrated typically shows short-term values of −10 to −12 LUFS at the loudest chorus and −18 to −20 LUFS in quiet intros, providing macro-dynamic contrast that survives normalization.

MOMENTARY LUFS

400 ms loudness snapshot for transient and element monitoring

Momentary LUFS uses a 400 ms integration window, fast enough to track individual elements like kick drum hits and vocal phrases. It is not gated. Use momentary readings on individual channel buses to understand each element's contribution to mix loudness in perceptual terms. A kick drum with momentary peaks of −10 LUFS while the mix sits at −18 LUFS short-term will dominate perceived loudness; identifying this allows surgical gain or dynamic correction rather than blanket level adjustment.

CREST FACTOR

Difference between True Peak and integrated loudness — a dynamic range proxy

Crest factor is calculated as True Peak (dBTP) minus integrated loudness (LUFS), expressed in LU or dB. A crest factor of 12–14 LU indicates a dynamic, punchy master. Values below 6 LU characterize heavily limited, brick-wall masters typical of the loudness war era. In a streaming environment where loudness is normalized, maximizing crest factor within your LUFS target is the single most impactful technique for preserving transient energy, depth, and emotional dynamics.

LOUDNESS RANGE (LRA)

Statistical spread of loudness variation — macro-dynamic descriptor

Loudness Range (EBU Tech 3342) describes the statistical spread of short-term loudness values over a program, expressed in LU. Commercial music typically measures LRA 4–9 LU; classical recordings may reach 20+ LU. An LRA below 4 LU signals a flat, over-compressed master regardless of its LUFS reading. Broadcast specifications (EBU R128) often specify maximum LRA alongside target integrated loudness to prevent both over-compression and excessive dynamics.

## 04 Quick Reference Card

Session-ready starting points. Values assume streaming delivery (Spotify, YouTube, Apple Music); broadcast targets differ significantly — use EBU R128 (−23 LUFS) for television and podcast distribution.

Copy Table

Parameter| General| Drums| Vocals| Bass / Keys| Bus / Master  
---|---|---|---|---|---  
Target Integrated LUFS| −14 LUFS| −14 LUFS| −16 LUFS| −14 LUFS| −14 to −16 LUFS  
True Peak Ceiling| −1 dBTP| −1 dBTP| −2 dBTP| −1 dBTP| −1 dBTP  
Typical Short-Term LUFS (loud section)| −10 to −12 LUFS| −9 to −11 LUFS| −12 to −14 LUFS| −11 to −13 LUFS| −10 to −12 LUFS  
Recommended Crest Factor| 8–14 LU| 10–16 LU| 10–18 LU| 8–14 LU| 8–12 LU  
Loudness Range (LRA) target| 5–9 LU| 4–8 LU| 6–10 LU| 4–7 LU| 5–9 LU  
Mix headroom before mastering| −6 to −3 dBFS peak| −6 to −4 dBFS peak| −6 to −3 dBFS peak| −6 to −4 dBFS peak| −6 to −3 dBFS peak  
Gain reduction on [limiter](/articles/best-limiter-plugins) at master| 2–4 dB GR| 1–3 dB GR| 2–5 dB GR| 2–4 dB GR| 2–5 dB GR  
  
Values assume streaming delivery (Spotify, YouTube, Apple Music); broadcast targets differ significantly — use EBU R128 (−23 LUFS) for television and podcast distribution.

## 05 History & Origin

The story of loudness in recorded music is inseparable from the history of vinyl mastering. From the late 1940s through the 1970s, loudness was a physical constraint: the wider and deeper a groove was cut, the louder the pressing, but wider grooves took up more space on the disc and limited playing time. Engineers like Bob Clearmountain and Bob Ludwig worked within strict mechanical limits. The RIAA equalization curve, standardized in 1954, defined the playback characteristic and required complementary pre-emphasis at cutting — another factor shaping what loud could mean on wax. These constraints naturally preserved dynamic range, because the medium demanded it.

The arrival of the Compact Disc in 1982 removed the physical ceiling. With 16-bit PCM offering a theoretical 96 dB of dynamic range and a fixed digital ceiling at 0 dBFS, there was no groove depth or tape saturation to limit ambition. Initially, engineers were conservative — early CD masters often sounded quieter than vinyl equivalents. But by the late 1980s, mastering engineers including Bob Ludwig, Ted Jensen at Sterling Sound, and Greg Calbi began discovering that limiters and multiband compressors could raise the average level of a CD master without exceeding 0 dBFS, making it sound louder than competing releases on first impression. Radio programmers and A&R; executives interpreted this perceived loudness as energy and commercial viability, and the arms race began.

The loudness war accelerated dramatically through the 1990s and 2000s. Oasis's 1995 album (What's the Story) Morning Glory? was mastered at levels that drew comment from engineers at the time. By 2008, Metallica's Death Magnetic — mastered by Ted Jensen under label pressure — became a cultural flashpoint: the Guitar Hero rip of the same songs, which had not been hard-limited, sounded dramatically better, and an online petition gathered tens of thousands of signatures demanding a remaster. Researcher and audio engineer Bob Katz had been documenting the trend since the late 1990s, publishing loudness data showing that average integrated loudness of pop masters had climbed from roughly −20 LUFS in the early CD era to −8 LUFS by the late 2000s — a 12 LU increase in perceived intensity bought entirely through dynamic range destruction.

The regulatory and technical response came through broadcast first. The EBU (European Broadcasting Union) published EBU R128 in 2010, standardizing integrated loudness for broadcast at −23 LUFS with a True Peak ceiling of −1 dBTP and a maximum LRA. The ITU-R BS.1770 measurement standard, revised through versions BS.1770-3 and BS.1770-4, formalized the K-weighting algorithm and gating methodology that underpins all modern loudness measurement. The United States followed with the CALM Act (Commercial Advertisement Loudness Mitigation Act), signed into law in 2010 and enforced from 2012, requiring television broadcasters to match advertisement loudness to program loudness. These regulatory actions established the measurement infrastructure that streaming platforms would later adopt.

Streaming normalization changed the commercial incentive structure permanently. Apple's SoundCheck feature, present in iTunes since 2001, was an early implementation of playback-level normalization but had limited adoption. Spotify introduced loudness normalization in 2013, initially at −11 LUFS, and revised its target to −14 LUFS in 2017 following lobbying from mastering engineers including Ian Shepherd and Thomas Lund, who had been publicly advocating for dynamic-friendly targets. Apple Music, YouTube, TIDAL, and Amazon Music all followed with their own normalization implementations, all clustering between −14 and −16 LUFS integrated. By the early 2020s, the loudness war was effectively over for streaming delivery. The remaining battleground is sync licensing and physical media, where some clients still request louder masters — though even here, attitudes have shifted markedly among engineers who understand the psychoacoustics.

## 06 How Producers Use It

In the mix session, loudness management begins at gain staging. The goal is to keep individual channels, buses, and the stereo sum at consistent operating levels — typically with the stereo mix bus peaking between −6 and −3 dBFS — so that the mix's perceived loudness is controlled by deliberate level and dynamic decisions, not by accumulated gain from poorly trimmed channels. Checking the mix's short-term LUFS reading at the loudest section gives an immediate sense of how much headroom remains for mastering. If the loudest chorus already reads −9 LUFS short-term with peaks at −1 dBFS, the master is going to require significant limiting to reach −14 LUFS integrated, and that limiting will cost dynamic range. Building the mix with 3–5 dB more headroom — peaks at −4 to −6 dBFS, loudest section short-term around −12 LUFS — gives the mastering stage room to breathe.

Drum and percussion production has a direct relationship with loudness management. Kick and snare transients are the primary source of a mix's crest factor: a tight, punchy kick that hits −6 dBFS peak while the mix idles around −18 LUFS short-term gives a crest factor close to 12 LU. Transient shapers, parallel compression, and attack/release tuning on bus compression all interact with how much of this crest factor survives into the master. A drum bus running −3 to −4 dB of gain reduction on a Neve-style compressor (API 2500, SSL G-Comp, or plugin equivalents) is shaping the loudness profile of the entire mix; the kick-to-mix relationship is a loudness relationship as much as a level one.

Vocal loudness is perceived disproportionately because the ear is most sensitive in the 2–5 kHz presence range where vocals dominate. A vocal that measures the same LUFS as the drums will be perceived as louder because of its spectral placement. Engineers working in pop and R&B; typically ride vocals using automation to keep short-term loudness consistent within ±2 LU through the song, then use a combination of optical and VCA compression (UA LA-2A, SSL channel compressor, or their plugin equivalents) to catch dynamic variation that automation doesn't address. The goal is a vocal that sits consistently in the loudness hierarchy of the mix without requiring constant level automation.

Bass and low-end management affects both the measured and perceived loudness of a master in complex ways. Sub-bass below 60 Hz is largely attenuated by K-weighting, meaning heavy sub-bass energy contributes relatively little to LUFS readings. This creates a trap: a mix with massive sub content may measure at −14 LUFS integrated but sound dramatically louder on systems with good bass extension, and significantly quieter on small speakers. High-passing the sub-bass at 30–40 Hz and using multiband limiting to control the 60–120 Hz region allows the low end to hit hard on capable systems while keeping the loudness measurement honest and predictable. On the master bus, limiting the sub-bass separately from the mid-range prevents low-end transients (kick, bass) from triggering gain reduction that compresses the entire mix.

AbletonPlace the stock Loudness Meter (Audio Effects → Meters → Loudness Meter) on the master bus and monitor integrated LUFS in real time. Use Limiter with a ceiling of −1 dB on the master for True Peak control, but rely on the Loudness Meter's integrated reading — not the Limiter's gain reduction — as your mastering target indicator. For mix bus glue before mastering, Glue Compressor with 1.5–2:1 ratio and slow attack (30–50 ms) preserves transient character while managing loudness density.

FL StudioUse the Parametric EQ 2 with spectrum analyzer on the master to visualize spectral loudness balance, and route the master through Maximus for loudness-targeted multiband limiting. Set Maximus's master output to −1 dB and use the integrated LUFS display in Fruity Peak Controller or an external VST meter (TT Dynamic Range Meter is free and accurate) to monitor integrated loudness during export. FL Studio's mixer master defaults to 0 dB; trim the master fader to −3 to −6 dB to maintain headroom before limiting.

Logic ProLogic's Loudness Meter plugin (available in the Metering category since Logic Pro X 10.6) provides integrated, short-term, and momentary LUFS alongside True Peak and LRA — use it on the stereo output. The stock Adaptive Limiter in Loudness mode targets broadcast standards automatically; for streaming work, set Out Ceiling to −1 dBTP and target an integrated reading of −14 to −16 LUFS using the Loudness Meter to confirm. Logic's Gain plugin inserted before the Adaptive Limiter is the cleanest way to trim mix level before limiting without altering bus processing.

Pro ToolsIn Pro Tools, the Avid Master Meter (bundled with Pro Tools Ultimate) provides EBU R128 and ATSC A/85 loudness monitoring with integrated, short-term, and momentary LUFS. For mastering sessions, insert the Master Meter on an Aux input feeding the master output and use it to set loudness before rendering. The stock Maxim limiter provides a ceiling control suitable for True Peak limiting; set Output Ceiling to −1 dB. For more transparent True Peak control in critical mastering, third-party limiters (Fabfilter Pro-L 2, Waves L2) are standard in Pro Tools mastering suites.

ReaperReaper includes the free JS: Loudness Meter - EBU R128 plugin (found in the JS Effects library) which provides full ITU-R BS.1770 compliant integrated LUFS, LRA, and True Peak metering with a resettable measurement window — place it last on the master chain. For True Peak limiting, the stock ReaLimit is capable and lightweight; set its ceiling to −1 dBTP. Reaper's signal flow is highly customizable: use a dual-master-bus setup with one bus for reference metering and one for render to monitor loudness without inadvertently affecting the rendered file.

The Producer's Briefing

### Sound better by _Friday._

One email a week. The techniques behind the terms — curated by working producers, not algorithms.

Join Free

No spam · Unsubscribe anytime

## 07 In the Wild

Abstract knowledge becomes practical when you can hear it in music you know. These tracks demonstrate loudness used intentionally, at specific moments, for specific purposes.

Daft Punk — "Get Lucky" (2013)

0:00–0:30 intro, full chorus at 2:20 · Produced by Daft Punk, Thomas Bangalter & Guy-Manuel de Homem-Christo

Get Lucky measures approximately −11 LUFS integrated — moderately loud by 2013 standards but with a noticeably higher crest factor than its contemporaries, around 10–11 LU. The interplay of Nile Rodgers's Stratocaster and the tightly compressed live drums creates a mix whose perceived density is achieved through arrangement and spectral balance rather than peak limiting. Listen at the chorus entry (2:20): despite substantial energy, individual transients — the snare, the guitar stabs — remain distinct and punchy. This was the mastering aesthetic of Chilly Gonzales and the Columbia/Sony mastering team honoring the dynamic range of the Wendy Carlos/Quincy Jones-influenced production rather than flattening it for radio competition.

Billie Eilish — "bad guy" (2019)

Drop at 1:06, sub-bass swell at 1:30 · Produced by Finneas O'Connell

Bad guy was widely noted at release for its unusually restrained loudness — approximately −14 LUFS integrated — at a time when most pop masters were pushing −7 to −9 LUFS. Finneas mixed and mastered primarily on Yamaha HS5 nearfields and Apple AirPods, prioritizing translation across small speakers. The production's psychoacoustic loudness comes from extreme spectral contrast: sub-bass energy below 80 Hz, near-silence in the upper-bass and low-mids, and sharp presence in the vocal 3–5 kHz range. On streaming platforms, where normalization plays it at its native level, the track's perception of intimacy and menacing density demonstrates that measured loudness and perceived impact are separable creative dimensions.

Kendrick Lamar — "HUMBLE." (2017)

0:00 piano intro vs. drop at 0:18 · Produced by Mike WiLL Made-It

HUMBLE. opens with a brief classical piano passage before the beat drops — a deliberate macro-dynamic contrast that demonstrates loudness as an arrangement tool. The track's integrated LUFS is approximately −8 to −9 LUFS, reflecting the aggressive limiting typical of hip-hop masters of the era, but the opening 17 seconds creates a perceived loudness differential of 12+ LU that makes the drop physically impactful beyond what the limiting alone achieves. This technique — using brief quiet sections to reset the listener's loudness adaptation before a dense drop — is a compositional loudness strategy that works independently of metered values. At the 0:18 drop, monitor the sub-bass bloom and the 808 transient against the snare for the crest factor relationship that defines the track's punch.

The Weeknd — "Blinding Lights" (2019)

Pre-chorus at 0:47, chorus peak at 1:03 · Produced by Oscar Holter, Max Martin, DaHeala

Blinding Lights measures approximately −7 to −8 LUFS integrated — a hard-limited master that sacrifices approximately 6–7 LU of crest factor for competitive loudness in the CD and terrestrial radio context. On streaming platforms that normalize to −14 LUFS, it is turned down 6–7 dB, arriving at the listener with compressed transients but a densely saturated spectral texture. The mastering, handled at Metropolis Studios London, uses the extreme low-end tightness and midrange saturation of the synthwave influence to maintain perceived energy even after normalization gain reduction. It is instructive to A/B this track against Billie Eilish's output — both normalize to the same playback level, but the Weeknd's crest factor compression is audible in transient smear on the snare and the flattened depth of the synthesizer pad reverb tails.

Listen On Spotify

Billie Eilish — bad guy

Daft Punk — Get Lucky

Kendrick Lamar — HUMBLE.

## 08 Types & Variants

Integrated Loudness (Program Loudness)

TC Electronic LM2n · Dorrough Loudness Monitor 280-A

Integrated loudness is the time-averaged, K-weighted loudness measurement across the full duration of a program with gating applied. It is the primary deliverable metric for streaming and broadcast mastering. Hardware meters like the TC Electronic LM2n display integrated LUFS in real time and are standard in broadcast mastering facilities; the Dorrough 280-A was widely used in broadcast production suites during the transition from peak to loudness-based standards. Integrated loudness answers the question: how loud is this program overall?

Short-Term Loudness

Nugen Audio VisLM · Waves WLM Plus

Short-term loudness uses a 3-second integration window to show loudness variation across sections of a program, updated every 100 ms. It is the most practical meter for mix work, revealing verse-to-chorus dynamics, the loudness contribution of individual sections, and the headroom available for mastering. The Nugen Audio VisLM has been a standard in post-production and mastering for its graphical history display of short-term, momentary, and integrated values simultaneously.

Momentary Loudness

iZotope Insight 2 · Fabfilter Pro-L 2 (metering display)

Momentary loudness integrates over 400 ms without gating, capturing the loudness of individual musical events — a kick drum, a vocal phrase, a snare hit. It is fast enough to be useful on individual channel inserts for balancing elements by perceived loudness rather than peak level. iZotope Insight 2 displays momentary LUFS alongside a loudness histogram and spectrogram, making it a comprehensive monitoring solution for both mix and mastering engineers who need to correlate spectral content with loudness readings.

Perceived / Psychoacoustic Loudness

Orban Loudness Processor · CBS Loudness Controller (vintage broadcast)

Perceived loudness is the subjective experience of intensity shaped by spectral content, temporal integration, and auditory masking — it cannot be captured by any single meter value. Equal-loudness contours, Fletcher-Munson curves, and psychoacoustic models inform how engineers make mixes feel loud by boosting presence frequencies (2–5 kHz), controlling dynamic variation, and using saturation to increase spectral density without raising peak levels. The Orban loudness processors used in broadcast since the 1980s model aspects of perceived loudness through multiband processing that optimizes subjective impact within technical limits.

True Peak Loudness

TC Electronic Clarity M · Tektronix WFM2300 (broadcast QC)

True Peak is not loudness in the psychoacoustic sense but the essential technical companion to LUFS measurement — the ceiling that prevents clipping during D/A conversion and codec processing. True Peak meters oversample the digital signal at 4× to 8× and detect inter-sample excursions. The TC Electronic Clarity M hardware meter is used in broadcast and streaming QC workflows for its simultaneous display of integrated LUFS and True Peak with delivery-spec compliance indicators.

## 09 Common Mistakes

  * ✕

Targeting LUFS without checking crest factor

Reaching −14 LUFS integrated by aggressively limiting a dynamic mix destroys crest factor and produces a flat, fatiguing master that sounds worse than a less-limited competitor at the same normalization level. Always check crest factor alongside LUFS: aim for a minimum of 8 LU difference between True Peak and integrated loudness. If hitting your LUFS target requires more than 4–5 dB of limiter gain reduction, the mix needs to be louder before mastering, not more limited.

  * ✕

Checking loudness only at the loudest section

Integrated LUFS averages the entire program, including intros, outros, breakdowns, and verses. Measuring only the loudest chorus can lead to a master that measures −10 LUFS integrated even though the chorus reads −14 LUFS short-term, triggering heavy gain reduction on streaming platforms. Always measure integrated LUFS from fade-in to fade-out and confirm it against your target before export. Reset your meter and run the entire track for an accurate reading.

  * ✕

Ignoring True Peak during lossy codec delivery

A master that peaks at exactly −1 dBTP may clip when encoded to 128 kbps MP3 or 256 kbps AAC, because codec processing introduces inter-sample overshoots of 0.5–2 dB. When delivering for any lossy format — including streaming platforms that transcode to AAC or Ogg Vorbis — use a −2 dBTP ceiling. The 1 dB difference is inaudible; the clipping artifacts introduced by codec-induced overshoot are not.

  * ✕

Confusing dBFS peak metering with loudness

A master peaking at −3 dBFS with a dense, limited spectrum can be 8–10 LUFS louder than a sparse mix peaking at 0 dBFS with high crest factor. Peak meters show headroom to clipping; they say nothing about perceived intensity or LUFS. Producers who set mix levels by watching a peak meter and targeting −6 dBFS without checking integrated LUFS are making loudness decisions without loudness data. Install a calibrated LUFS meter on your master bus as permanent infrastructure.

  * ✕

Using the same loudness target for all delivery formats

Streaming (−14 LUFS), broadcast (−23 LUFS), cinema (−24 LKFS per SMPTE), podcast (−16 LUFS per Apple Podcasts), and vinyl transfer each have different loudness targets with different technical implications. Sending a −14 LUFS streaming master to broadcast results in 9 LU of further attenuation; sending a −23 LUFS broadcast mix to streaming results in 9 LU of gain and potential True Peak violations. Maintain separate masters for each delivery format, at minimum a streaming master and a broadcast/other master.

  * ✕

Over-compressing during mixing, then blaming the master for lack of dynamics

Dynamic range is lost incrementally across the signal chain: excessive channel compression, over-driven bus compression, parallel compression that adds density, and then a limiter at mastering. By the time the master receives the mix, the crest factor may already be below 6 LU with a short-term loudness ceiling of −11 LUFS, leaving no room for the mastering engineer to hit −14 LUFS integrated without heavy limiting. Discipline at each stage of dynamic processing during mixing preserves the headroom and crest factor that mastering requires.


Interactive Tool

Loudness Calculator

Calculate gain reduction, makeup gain, and output level for any loudness setting.

Input Level (dBFS)

Threshold (dBFS)

Ratio (X:1)

Makeup Gain (dB)

Calculate

Result

## Related Guides & Tools

[Loudness Penalty CalculatorEnter your master's integrated LUFS and see exactly how much Spotify, Apple Music, YouTube,…](/tools/loudness-penalty)[Best Limiter PluginsDiscover the best limiter plugins of 2026 for mastering and mixing. Expert…](/articles/best-limiter-plugins)

## 10 Producers Also Look Up

[LimitingThe primary tool for controlling True Peak and raising integrated loudness at the mastering stage.](https://musicproductionwiki.com/bible/limiting) [CompressionDynamic range reduction that shapes mix density and crest factor upstream of loudness metering.](https://musicproductionwiki.com/bible/compression) [Gain StagingThe practice of managing levels at every stage of the signal chain to preserve headroom for loudness management.](https://musicproductionwiki.com/bible/gain-staging) [HeadroomThe buffer between operating level and the digital ceiling — the space that determines how much loudness can be achieved without distortion.](https://musicproductionwiki.com/bible/headroom) [LUFSThe ITU-R BS.1770 unit of loudness measurement central to all modern mastering and streaming delivery specifications.](https://musicproductionwiki.com/bible/lufs) [Dynamic RangeThe difference between the quietest and loudest parts of a signal — the inverse relationship to loudness density.](https://musicproductionwiki.com/bible/dynamic-range)

## 11 Further Reading

These MPW articles put loudness into practice — specific techniques, real tools, and applied workflows.

[ → What Is Lufs ](lufs) [ → How To Use A Limiter ](https://musicproductionwiki.com/articles/how-to-use-a-limiter.html) [ → Gain Staging Guide ](gain-staging) [ → True Peak Explained ](true-peak) [ → How To Master A Song ](https://musicproductionwiki.com/articles/how-to-master-a-song.html)

## 12 Frequently Asked Questions

What is the difference between loudness and volume?+

Volume is a physical property — the amplitude of a signal expressed in dB. Loudness is the subjective perception of that amplitude as experienced by human hearing, shaped by frequency content, duration, and the ear's nonlinear sensitivity curve. A signal at −6 dBFS does not produce a fixed loudness experience: a dense, high-energy mix at −6 dBFS will sound dramatically louder than a sparse recording at the same peak level. LUFS metering models this perceptual difference using K-weighting, giving producers a measurement that correlates with how loud something actually sounds rather than just how much headroom it uses.

What LUFS should I target when mastering for Spotify?+

Spotify normalizes playback to −14 LUFS integrated. Submit a master at or around −14 LUFS integrated with a True Peak ceiling of −1 dBTP. Masters louder than −14 LUFS will be turned down in gain; masters quieter will be left at their natural level or turned up on Spotify Loud playback mode. There is no benefit to submitting above −14 LUFS — the extra loudness is silently removed. Focus instead on maximizing crest factor and dynamic interest within the −14 LUFS target.

What does True Peak mean and why does it matter?+

True Peak measures the amplitude of the audio signal after it has been reconstructed by a D/A converter, including the values that exist between PCM samples — inter-sample peaks. It is possible for a digital file with no sample exceeding 0 dBFS to produce an analog waveform that clips during playback. True Peak meters oversample the signal at 4×–8× to detect these excursions. For streaming delivery, keep True Peak at or below −1 dBTP. For lossy formats (AAC, MP3), use −2 dBTP to account for 0.5–1.5 dB of codec-induced overshoot.

What is the loudness war and is it still happening?+

The loudness war was a multi-decade escalation in which record labels and engineers pushed mastering loudness progressively higher — from roughly −20 LUFS in the early CD era to −7 LUFS by the late 2000s — by removing dynamic range through hard limiting. The goal was to sound louder than competing releases on radio and in stores. Streaming normalization effectively ended the commercial advantage of over-limiting around 2013–2017, because platforms like Spotify and Apple Music normalize all content to a common loudness level. The loudness war is structurally over for streaming; some physical and broadcast work still reflects older habits, but modern mastering practice strongly favors dynamic-aware targets.

How do I make my mix sound loud without over-limiting?+

Perceived loudness is built in the mix, not at the limiter. Use saturation on individual elements to increase spectral density and harmonic content — this raises loudness perception without touching peak levels. Control the low end tightly (high-pass filters, sub limiting) so bass transients don't trigger gain reduction on the full mix. Add excitement and presence in the 2–5 kHz range where the ear is most sensitive. Use parallel compression on drums and buses to increase average density while preserving transient peaks. When you reach mastering, a well-prepared mix needs only 2–4 dB of limiting to hit −14 LUFS integrated — leaving the crest factor and dynamics largely intact.

What is K-weighting and why is it used for LUFS measurement?+

K-weighting is a two-stage filter applied to audio before loudness measurement under ITU-R BS.1770. The first stage is a high-shelf pre-filter that boosts frequencies above approximately 1.5 kHz by about 4 dB, modeling the acoustic effect of the human head on the eardrum (the head-related transfer function). The second is a high-pass filter rolling off below roughly 60 Hz, reflecting the ear's reduced sensitivity to deep bass at normal listening levels. Together, K-weighting makes LUFS measurements correlate with perceived loudness more accurately than unweighted RMS or peak measurements — it explains why a bass-heavy mix and a presence-heavy mix can read the same dBFS level but sound very different in loudness.

Should I deliver the same master to all streaming platforms or create separate masters?+

The ideal workflow is platform-specific masters, at minimum two: a streaming master (−14 LUFS integrated, −1 dBTP) for Spotify, YouTube, and Amazon Music, and a separate master (−16 LUFS integrated, −1 dBTP) for Apple Music and Tidal, which normalize at −16 LUFS and will gain-up a −14 LUFS master. For broadcast delivery (TV, podcast), create a −23 LUFS or −16 LUFS master per the relevant spec. Practically, many mastering engineers deliver a single −14 LUFS integrated streaming master and note that Apple Music's gain-up from −14 to −16 LUFS is 2 dB and unlikely to cause True Peak violations on a well-constructed master. The critical distinction is never to submit a brick-wall master above −11 LUFS to any streaming platform.

How does loudness interact with multiband compression at mastering?+

Multiband compression at mastering shapes the loudness contribution of individual frequency bands independently, allowing engineers to raise integrated LUFS by reducing crest factor only in problem bands — typically the sub-bass (20–80 Hz) where individual kicks and bass notes cause the highest peaks — without applying as much limiting to the mid and high frequencies where transient detail matters most for perceived punch. A multiband limiter set to apply 4–6 dB of gain reduction only to the 20–80 Hz band while the full-band limiter applies 1–2 dB can achieve the same integrated LUFS target with 2–3 LU better crest factor on the full-range signal. The risk is phase and transient artifacts at crossover frequencies; use gentle slopes (24 dB/octave or lower) and match gain carefully across bands to avoid spectral pumping.

Levels & HeadroomMasteringMeteringStreaming DeliveryDynamic Range

Last Verified: May 14, 2026 · 2026 Edition · Part of The Producer's Bible

[Share on X](https://twitter.com/intent/tweet?url=https://musicproductionwiki.com/bible/loudness&text=The+definitive+Loudness+guide+for+producers) [Share on Reddit](https://www.reddit.com/submit?url=https://musicproductionwiki.com/bible/loudness) Copy Link

Part of [The Producer's Bible](https://musicproductionwiki.com/bible/) — Every term. Every technique. One place.  
Published by [MusicProductionWiki.com](https://musicproductionwiki.com) · The Reference Standard for Music Production 

The Producer's Bible · MusicProductionWiki.com · 2026 Edition

  * [Home](https://musicproductionwiki.com)
  * [About](/about)
  * [Privacy](/privacy)
  * [Contact](mailto:team@musicproductionwiki.com)



↑
