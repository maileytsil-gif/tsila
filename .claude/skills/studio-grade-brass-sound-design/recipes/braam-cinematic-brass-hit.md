# Braam / cuivre cinématique (hit, drone d'impact)

Le « Inception horn » : masse grave, détunée, distordue, à longue queue. Origine par extraits (Zimmer : cuivres joués dans un piano à queue pédale enfoncée, dans une église, puis « electronic nonsense » ; Zarin : foley de métro + cuivres pitch-shiftés) [HEUR-extrait]. Recettes chiffrées lues : synthdef `braam` [DOC] et preset Vital « Sci-nema Brass » [DOC] (`../../../../corpus/cuivres/recherche-axe3-cuivres-electroniques-modernes.md`).

## Cible
`HIT / C1–C2 (MIDI 24–36), parfois A1 (33) / une note ou une quinte / BRASS ACCENTS ; sur une transition, un drop, un impact de trailer`

## Architecture — trois couches, trois pistes
| Couche | Source | Preuve |
|---|---|---|
| CORPS grave | 5 scies : f × 0,99 (20 %), f (25 %), f × 1,01 (20 %), f × 2 (15 %), f × 0,5 (20 %) [DOC synthdef] ; ou une scie unison 16 voix détune ≈ 0,10, −12 st [DOC Vital] | |
| SUB | sinus −12 st, 30 % ; le grave passe par le sub, la scie est coupée sous 100 Hz (EQ −11 dB à 98 Hz) [DOC Vital] | |
| CUIVRE RÉEL | sample d'usine Serum 2 `Factory/Brass/Trombone.flac` ou `Brass Wall Low.flac` [DOC corpus], ou Orchestral Brass low brass, note longue et forte, plusieurs instances empilées [HEUR-extrait] | |
| SOUFFLE | bruit blanc à niveau plein sur le preset Vital [DOC] ; ici 20–40 % [HEUR] | |

## Serum 2 (piste CORPS + SUB)
- OSC A scie, unison 16, detune 0,10–0,20, blend 80 %, −12 st ; Sub sinus −12 st 30 % routé **Direct** (évite filtre et FX) [DOC routage] ; NOISE blanc 20–40 % vers le filtre.
- Filtre 1 MG Low 24 drivé (FAT ou Drive) cutoff ≈ 700 Hz [DOC Vital 687 Hz] ; Env 2 → cutoff : A 50 ms, D 1,5 s, S 0, de 3,2 kHz vers 200 Hz [DOC synthdef].
- Env 1 : **A 50 ms** (macro Attack jusqu'à 150 ms), **D 2–3 s**, S 70 %, R court [DOC synthdef 50 ms / 2 s ; Vital 2,78 s].
- Env 3 → pitch : 0 puis descente −2 à −12 st sur 1–2 s (macro Fall), ou pitch bend joué ; molette → cutoff +45 % [DOC Vital].
- FX : Distortion (drive 8–9 dB) → Compressor MULTIBAND (OTT : gains bas 16, médium 12, haut 16 dB, mix 100 %) → EQ (shelf −11 dB à 98 Hz, cloche −8 dB à 554 Hz) → **Reverb Hall, decay 5–6 s**, mix par macro [DOC Vital].

## Live natif
Analog ou Wavetable pour la scie (unison Classic 4 voix), Operator sinus pour le sub, Simpler pour le sample ; groupe : `Saturator (Analog Clip, Color 400 Hz–4 kHz) → Amp/Cabinet ou Pedal (simulateur d'ampli guitare, cité par les compositeurs [HEUR-extrait]) → Multiband Dynamics OTT → Hybrid Reverb 5–6 s, coupe-haut sur la queue → Glue`. Compresser chaque couche, limiter le groupe, occuper tout le champ stéréo sauf le sub [HEUR-extrait Ableton blog].

## Mouvement
Distorsion automatisée pour créer du mouvement ; dynamique F → FFF sur la couche réelle ; pitch drop progressif au pitch wheel [HEUR-extrait]. Exporter en audio pour pouvoir l'étirer et le re-pitcher (`../../resampling/SKILL.md`).

## Tests [TEST]
Mono : le sub reste, la scie large ne s'annule pas · niveau de crête du groupe avant limiteur · durée totale (attaque + queue) alignée sur le repère de transition · rien sous 30 Hz hors sub · la couche réelle reste identifiable sous la distorsion.

## Variante
Plus « orchestre » : moins de distorsion, cuivre réel dominant, hall avec pré-delay 40 ms. Plus « trailer » : pitch drop −12 st, resample puis time-stretch ×2.
