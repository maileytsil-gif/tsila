# Low-end engine

Tags: see `50-mastering-engine.md`. Full method (French): `../../kick-bass-equilibre/SKILL.md`, `../../kick-bass-equilibre/references/roles.md`. Genre sources: `../../house-future-rave-bass-house-production/references/mixage-mastering.md` §2.

## Choose the architecture first
Record the choice in `../../drums-signature/scripts/signature.json`.
1. **Sub holds the fundamental** (deep, minimal and tech house, DnB). Mono sine sub on the tonic; short kick (< 200 ms, body 60–100 Hz). Kick HPF 25–30 Hz, or 40–50 Hz if > 20 % of kick energy is below 60 Hz.
2. **Kick holds the low end** (big room, future rave, 808, techno rumble). Long tuned kick, optional short sub (≈ 50 Hz, < 100 ms) [COMM]. Bass above 80–100 Hz or in the kick's gaps.
3. **Layered bass** (bass house) [COMM]. Sub (25–80 Hz), mid (HPF 80 Hz) and top (HPF 300 Hz), all sidechained. Distort only the mid.

## Diagnose in this order
1. Is the kick sample or patch right, and tuned? Tonic F: sub 43.7 Hz, kick 87.3 Hz or 65.4 Hz [CALC]. Measure pitch on the kick tail.
2. Do kick and bass note lengths or tails overlap unnecessarily?
3. Is the bass note placement musical and intentional?
4. Are related layers aligned in time, polarity and phase?
5. Is broad-band sidechain actually needed?
6. Only then use dynamic EQ, spectral sidechain or static EQ.

## Time before frequency
Envelope or placement often beats a big EQ cut [HEUR]. The kick decays before the next bass note. Sub release is ≥ 60 ms but shorter than the note gap. If the sum cancels, shift the sub by −5 to −10 ms.

## Sidechain
Match the tool to the conflict:
- broad-band compressor when the pump is part of the groove;
- F6 or Pro-Q 4 dynamic band when the conflict is local;
- soothe3 keyed externally when it moves;
- Utility gain automation for precision (LFO Tool, Kickstart and ShaperBox are absent).

| Context | Depth | Attack | Release | Ratio |
|---|---|---|---|---|
| Sub-holds (repo) | 4–8 dB | 0.1–1 ms | 80–120 ms | 4:1 |
| Tech/deep house [COMM] | 2–4 dB | 5–20 ms | 60–100 ms | 4:1 |
| Bass house [COMM] | 4–8 dB | 1–5 ms | 100–150 ms | 8–10:1 |
| Future rave/big room [HEUR] | 6–10 dB | 0.5–1 ms | 150–200 ms | 6:1 |

Release stays ≤ the kick interval (469 ms at 128 BPM [CALC]). Use a detector HPF of 80–100 Hz and link L/R [COMM]. Never key an already-compressed bus or the master. Sources disagree on attack, so test. There are no values for DnB, techno or dubstep. Recipe: `../../house-future-rave-bass-house-production/recipes/sidechain-et-pump.md`.

## Phase: measure, then decide
Align polarity and timing only between related layers; independent signals drift in phase, so do not chase static alignment. Set Serum oscillators to fixed phase and re-check in mono.
1. Export KICK and SUB separately (4–8 drop bars, 24-bit).
2. Run `../../kick-bass-equilibre/scripts/kick_bass_check.py kick.wav sub.wav --band 30-120 --lag 15`. It reports:
   - who holds < 60 Hz;
   - band correlation (> 0.3 reinforce, < −0.3 cancel);
   - best offset and polarity gain.
3. Change one thing, then re-measure.

## Bass translation
Add upper harmonics with MaxxBass (R-Bass: declared only), J37 at 7.5 ips [DOC] or mid saturation. Perceived bass is not more sub.

## Stereo
Keep the sub mono: below ≈ 120 Hz in house (repo chain), 150 Hz in bass house [COMM]; sources go to 200 Hz, and club subs are summed to mono anyway [DOC-2]. Put width in harmonics only. Verify with SPAN correlation and a Utility mono sum.
