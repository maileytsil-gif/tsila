# Nappe et gonflement de cuivres (pad, swell, riser de section)

Tenues de section en arrière-plan, gonflements vers un refrain ou un drop, « fanfare » de fin de build. Sources : Juno-106 d'usine (Brass Swell, Brass III, Fanfare) [DOC], recette CS-80 tierce [HEUR], Rimsky-Korsakov (tenues aux trompettes et cors) [DOC], SS25 (swell brass = enveloppe à cinq étages) [DOC].

## Cible
`PAD ou HIT (fanfare) / accords de 3–4 notes 48–72, tenues 2–8 mesures / BRASS IN BACKGROUND (pad) ou BRASS ACCENTS (fanfare)`

## Les régimes d'usine Juno-106 [DOC valeurs, conversions HEUR]
| Patch | Attaque | Filtre freq / res / env / kbd | Sustain | Release | Autres |
|---|---|---|---|---|---|
| A12 Brass Swell | 64 (≈ 500 ms) | 43 / 17 / 26 / 84 | 38 | 37 (≈ 1 s) | 8', sub 70, chorus I |
| A34 Brass III | 58 (≈ 440 ms) | 66 / 24 / 11 / 12 | 94 | 37 | sub 22, chorus I |
| A35 Fanfare | 72 (≈ 600 ms) | 44 / 0 / 32 / 67 | 75 | 49 (≈ 1,2 s) | 16', saw + pulse PWM LFO, sub 50, chorus I |

Lecture : attaque longue, sustain haut, sous-oscillateur, chorus ; l'enveloppe de filtre est faible (le mouvement vient de l'attaque d'ampli).

## Serum 2 [HEUR sauf mention]
- OSC A scie unison 3, detune 0,08, blend 75 %, mode Random [DOC modes] ; OSC B pulse PWM lente (LFO 0,2 Hz → PW) ; Sub carré ou sinus −12 st 20–40 %.
- Filtre MG Low 24 cutoff 400–800 Hz, key 60 % ; Env 2 → cutoff +25 %, A 600 ms, S 80 %.
- Env 1 : **A 400–600 ms**, S 90 %, R 1–1,2 s ; pour un swell à cinq étages (SS25), LFO 3 en mode Env dessiné → volume [DOC mode Env].
- Vibrato : LFO 1 sinus 5 Hz, Delay 600 ms, Rise 800 ms, faible.
- Aftertouch ou CC11 → cutoff (« brass swell » du CS-80 : aftertouch → brillance [HEUR]).
- FX : Chorus (rate lent, mix 50 %) → Hyper 2 voix → Reverb Hall 2–4 s mix 20 % (BUS 1, LO CUT 200 Hz).
- Poly 6 voix ; pas de retrigger nécessaire.

## Live natif
Analog : 2 scies, Filtre LP 4e ordre, Env ampli A 500 ms, Vibrato Delay/Attack, Unison 4 voix Delay court ; Chorus-Ensemble mode Ensemble 1,2 Hz ; ou Wavetable unison Classic 3 + Sub. Tout relisible.

## Écriture et intégration
Tenues à deux ou quatre voix à l'octave (trompettes/cors), le trombone rarement dans les tenues [DOC Rimsky] ; ré-attaquer après 2 mesures, respirer ; monter d'une octave au climax plutôt que de pousser le niveau (« plus haut = plus brillant » [DOC Rimsky]). Fanfare de build : accord plaqué A 600 ms sur la dernière mesure, coupé au downbeat (`../../arrangement-avance/SKILL.md`). Riser de section : macro Brightness automatisée sur 8 mesures + Env 1 A qui raccourcit (`../../live-automation/SKILL.md`).

## Processing [HEUR]
`REQ 6 HP 120 Hz, −2 dB 300 Hz → bx_glue 2:1 30 ms auto → reverb commune` ; largeur par le chorus seulement ; le pad ne possède jamais le médium : −6 à −10 dB sous le hook.

## Tests [TEST]
8 mesures tenues : rien ne fatigue (vibrato, LFO PWM lent) · mono : le sub et le corps tiennent · en présence de la voix : le pad reste sous les mots · niveau stable ±1 dB entre l'attaque et la tenue.
