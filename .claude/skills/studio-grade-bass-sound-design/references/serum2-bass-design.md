# Serum 2 — Bass Design

## Capacités vérifiées [DOC]

- OSC A/B/C : Wavetable, Multisample, Sample, Granular, Spectral.
- Sources supplémentaires SUB et NOISE.
- Deux filtres, routage source → Filter/Main/Direct/None et BUS 1/2.
- Modes de pitch Semitones/Harmonics/Ratio/Step.
- `CRS` = pitch continu utile comme destination de modulation/sweep.
- Huit macros.
- Matrice de modulation avec sources/destinations multiples.

## Clean sub

[HEUR]
- source sine ou forme très pauvre en harmoniques ;
- une voix, unison nul ;
- retrigger/phase cohérente si le pattern exige des attaques identiques [TEST] ;
- route `Direct` si les FX du patch doivent toucher uniquement le mid layer [DOC] ;
- ENV amplitude adaptée au pattern, sans click indésirable.

## Rolling bass

[HEUR]
- OSC A saw/square ou wavetable simple ;
- SUB sine séparé ;
- LP 12/18/24 selon besoin ;
- enveloppe courte sur cutoff et volume ;
- légère saturation ;
- velocity/decay peuvent créer des accents plus musicaux que des notes toutes identiques.

## Reese/growl

[HEUR]
- deux sources harmoniques ou une source + duplication ;
- légère désaccordage/phase pour le body, mais conserver le sub propre ;
- LFO principal sur wavetable/filter/FM/level ;
- filtre notch/band-pass/low-pass selon caractère ;
- distortion avant/après filtre selon objectif ;
- resampler les meilleures phrases pour montage précis.

## FM/metallic

Le mode `Ratio` permet des relations de hauteur adaptées aux constructions FM [DOC].

[HEUR] Tester ratios simples (1:1, 2:1, 3:1, 3:2) avant des rapports complexes. Moduler la profondeur avec une enveloppe ou un LFO court. Plus la modulation est forte, plus le bas peut perdre sa fondamentale : d'où l'intérêt d'un sub séparé.

## Macro map recommandé

- M1 Tone : cutoff + tilt harmonique.
- M2 Motion : profondeur LFO principale.
- M3 Bite : drive + resonance/feedback.
- M4 Weight : balance SUB/BODY.
- M5 Width : unison/pan uniquement haut du spectre.
- M6 Space : sends/FX mix upper layer.
- M7 Attack : attack/decay/filter env.
- M8 Variation : destination spéciale pour fin de phrase.

Pour le bridge : limiter chaque macro à une plage musicalement sûre [TEST].
