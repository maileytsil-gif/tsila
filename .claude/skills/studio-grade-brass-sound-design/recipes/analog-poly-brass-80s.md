# Synth brass polyphonique années 80 (Juno, Jupiter, Oberheim « Jump », JX-3P)

Le cuivre de section synthétique : stabs, accords tenus, riffs. Données d'usine Roland décodées [DOC] (`../../../../corpus/synthes-vintage/roland-juno-60-chartes-usine-phosphor.md`, `roland-juno-106-patches-usine-amy.md`), presets OB-Xd communautaires [HEUR] (`obxd-preset-*.md`), synthèse dans `../../../../corpus/cuivres/recherche-axe2-synth-brass-vintage-fm.md`.

## Cible
`STAB, HOOK ou PAD / accords de 3–4 notes entre C2 et C5 / BRASS ACCENTS ou BRASS OWNS HOOK`

## Les trois régimes documentés (Juno-106 d'usine) [DOC valeurs 0–127, conversions AMY [HEUR]]
| Régime | Patch | Attaque | Filtre (freq / res / env / kbd) | Sustain | Release | Particularités |
|---|---|---|---|---|---|---|
| **Stab** | A11 Brass Set 1 | 3 (≈ 30 ms) | 35 (≈ 130 Hz) / 13 / 58 / 86 | 45 | 32 (≈ 800 ms) | 16', chorus I, HPF 1 |
| **Stab gate** | B31 Brass | 3 | **0 / 0 / 94 / 127** | 51 | 11 (≈ 80 ms) | VCA en **gate**, PWM LFO 73, chorus I — l'astuce SH-101 de Reid |
| **Swell / pad** | A12 Brass Swell, A34 Brass III | 64–72 (≈ 500–600 ms) | 43–66 / 17–24 / 11–26 / 12–84 | 38–94 | 37 (≈ 1 s) | sub 22–70, chorus I |
| **Lead** | A13 Trumpet | 5 | 55 (≈ 460 Hz) / 34 / 24 / 59 | 48 | 16 (≈ 240 ms) | 8', **vibrato retardé** (DCO-LFO 8, delay 45), HPF 2, pas de chorus |

Juno-60 « 17 BRASS » (chartes Roland) : scie seule, cutoff **0**, env → filtre **0,85**, résonance ≈ 0, tracking 0,41, ENV 0,26 / 0,40 / 0,62 / 0,22, LFO → DCO 0,17 avec **delay 0,67**, chorus I [DOC]. C'est le cuivre de section Juno canonique.

## Serum 2 (stab de section) [HEUR sauf mention]
- OSC A scie, unison **2–4**, detune 0,06–0,12, blend 75 %, width 40 % ; OSC B off ou pulse PWM lente (LFO 0,3 Hz → PW) pour le « Phase Brass » Juno-60 (pulse + PWM par enveloppe) [DOC charte 18].
- Sub (carré ou sinus −12) 20–30 % uniquement pour les tenues [DOC Juno swell].
- Filtre MG Low 24 ou Low 12 (l'OB-Xa en 12 dB donne la couleur « section » [HEUR tiers]), cutoff 100–150 Hz, résonance ≤ 15 %, key 40–90 %.
- Env 1 : A 25–35 ms, S 45–60 %, R 80–300 ms. Env 2 → cutoff +80–95 % : A 20–40 ms, D 300–500 ms, S 45–55 %, R comme l'ampli.
- Vélocité → quantité Env 2 (aux source) ; molette → cutoff.
- LFO 1 sinus 4–5 Hz → pitch ±5 cents, Rise/Delay 500–700 ms (vibrato retardé Juno) [DOC principe].
- FX : **Chorus** (le « I » Juno : rate lent, depth modérée, mix 50 %) → Compressor → Reverb plate 1,4 s 12 %.
- Mode Poly, 4–6 voix ; retrigger sur chaque note (stabs).

## Wavetable / Analog natifs
Wavetable : Osc 1 Basic Shapes saw, unison Classic 3 voix [DOC modes d'unison], Sub à 0 sauf tenues ; Filtre 1 LP 24 ; Env 2 → Flt 1 Freq via la matrice avec Velocity en amount [DOC matrice] ; LFO 1 → Osc 1 Transp avec Attack Time 500 ms (retard du vibrato) [DOC LFO Attack Time]. Chorus-Ensemble natif derrière. Tout est lisible par `ppal-read-device`.

## Variante « Jump » (Van Halen) [HEUR — aucune source primaire lue ; OB-X ou OB-Xa non tranché]
Presets OB-Xd lus : deux scies, osc 2 désaccordé (0,40–0,44 en unités OB-Xd), filtre 2 pôles, key follow 100 %, quantité d'enveloppe de filtre élevée, ampli A 0 / S 100 %, filtre A ≈ 0,16–0,28 / D ≈ 0,27–0,28 / S 0–0,5, résonance basse (0,1 ; la valeur 0,89 d'un preset est douteuse), vibrato sinus léger. Dans Serum 2 : 2 scies + unison 4, detune ≈ 0,15, filtre **Low 12**, Env 2 → cutoff +90 % A 15 ms D 250 ms S 20 %, accords plaqués à 4 notes, Chorus + légère saturation. Le fameux « accord de Jump » est un jeu, pas un patch.

## Variante « Axel F » stabs (JX-3P) [HEUR]
Scie + désaccord ≈ 6 cents, chorus I/II déterminant, filtre A 5 ms / D 400 ms / S 70 %, stabs courts et secs (spec tierce, `../../../../corpus/synthes-vintage/axel-f-synth-spec-lukemosse.md`).

## Processing et intégration
`Chorus dans le patch, pas sur le bus` · `bx_glue 2:1, 10 ms, auto → cohésion des stabs → 1–2 dB` · `REQ 6 coupe-bas 150–200 Hz, cloche −2 dB 300–400 Hz si boue` · sidechain léger au kick si les stabs tombent sur les temps [HEUR]. Panoramique : section centrée, largeur par le chorus seulement ; vérifier en mono.

## Tests [TEST]
Accord de 4 notes staccato : attaques nettes, pas d'empilement de release · même accord tenu 2 mesures : vibrato retardé audible, pas de battement désagréable (réduire le detune) · mono : niveau stable à ±1 dB · macro Brightness min/max musicale.
