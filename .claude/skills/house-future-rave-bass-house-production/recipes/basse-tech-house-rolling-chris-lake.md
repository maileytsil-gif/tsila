# Basse tech house rolling, courte et filtrée (Chris Lake, Fisher, Dom Dolla)

## Cible
`TECH HOUSE, BASS TECH HOUSE / LA BASSE EST LE GROOVE / 124–128 BPM / ré, do, fa, la mineur / une note et son octave / rolling 1/16 ou off-beat avec octave, swing 52–55 %`

Les tutoriels Fisher, Dom Dolla et James Hype sont des vidéos `[DOC-EXTRAIT]` ; les chiffres écrits viennent de The Producer School (Chris Lake), SoundBridge, Attack Warehouse et du consensus de dix recettes house `[DOC-2 dotbeat]`.

## Moteur
Serum 2 ; Wavetable natif (filtre **12 dB**, release réduite) ; Repro-1 ou Analog pour la version analogique.

## Patch
| Étage | Valeur | Preuve |
|---|---|---|
| Oscillateurs | saw + sinus OCT −1 (sub) ; ou carrée + saw, haute résonance ; phase random **off** (RAND 0) | `[DOC-EXTRAIT]`, `[DOC-2]` |
| FILTER 1 | MG Low 24 (ou 12 dB pour garder des harmoniques) ; CUTOFF parqué **80–200 Hz** (150 Hz SoundBridge, ≈ 140 Hz Producer School) ; RES 0–10 (SoundBridge 0 ; accordée au 5e harmonique chez ModeAudio : désaccord assumé) ; DRIVE 20–40 % | `[DOC-EXTRAIT]`, `[DOC-2]` |
| ENV 1 (ampli) | A 0 · D 150–300 · S 20–40 % · R < 100 ms ; Chris Lake : D ≈ 1,2 s, S −10 dB | `[DOC-EXTRAIT]` |
| ENV 2 → CUTOFF | **plus courte que ENV 1** ; D 200 ms S 0 → cutoff 5 %, → RES 10 % ; « boing » D 150–250 à 20–30 % | `[DOC-EXTRAIT]` |
| Vélocité → CUTOFF | **courbe raide** : seules les notes fortes ouvrent ; « le secret du bounce, confirmé par trois tutoriels » | `[DOC-EXTRAIT]`, `[DOC-2]` |
| Voicing | MONO, LEGATO, PORTA 0 (glide 0 ms) | `[DOC-2]` |
| Distorsion | post-filtre, 8 dB (SoundBridge) ; Tube | `[DOC-2]` |
| EQ | +10 dB à 75 Hz Q 1–2 (SoundBridge) ; HPF 65 / LPF 350 sur la ligne, sub séparé LP 80 Hz (Warehouse) | `[DOC-2]` |

Couche haute optionnelle (Tracey Brakes, Serum 2) : High 12 à 913 Hz RES 22, UNISON 7 DETUNE 0,15, OCT −3, sur un sub A séparé `[DOC-2]`.

## MIDI
```
Rolling 1/16    pas : 1 2 3 4 | 5 6 7 8 | 9 10 11 12 | 13 14 15 16
                      X . . x | . . x . | X .  .  x  | .  .  x  .     vel 102 / 80 / 94 / 102 / 80 / 94 ; gate 0,35 temps
```
25 % des notes à +12 (vel 84) ; pas 15 = note d'approche chromatique 50 % du temps ; ghosts pairs 40–55 à gate 25 % ; **première double de chaque temps vide** ; swing 55 % sur la basse, les hats et les percs (Groove Pool « Swing 16 »), jamais sur le kick ; « l'octave-up est la technique n° 1 pour le drame » ; phrases de 4 mesures, seconde moitié syncopée ; Dom Dolla : « root note in a minor key, a bit of shuffle on the bassline ».

## Chaîne
Distortion interne ou J37 (Saturator interdit) → EQ (HP 30, −3 dB max à 200, high cut) → sidechain rapide 2–4 dB « invisible » (attaque 5–20 ms, release 60–100) → EQ finale ; reverb et delay interdits sur le sub, tolérés sur la couche > 250 Hz ; mono sous 120 Hz.

## Erreurs
Release par défaut (600 ms Wavetable = boue) ; enveloppe de filtre aussi longue que l'ampli (le son « fade » au lieu de « frapper ») ; vélocités plates ; swing sur le kick ; résonance qui siffle.

## Vérification
Boucle de 8 avec kick 909 et hats seuls : ça groove sans rien d'autre, sinon c'est le MIDI ; deux notes extrêmes ; mono ; `kick_bass_check.py`.
