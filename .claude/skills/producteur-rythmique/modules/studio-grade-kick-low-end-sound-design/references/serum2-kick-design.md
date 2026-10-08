# Serum 2 — conception kick/808

## Capacités vérifiées [DOC]

Serum 2 propose sur OSC A/B/C cinq moteurs : Wavetable, Multisample, Sample, Granular et Spectral. Il permet aussi un routage vers filtres/Main/Direct/None et bus. Le pitch tracking peut être désactivé pour des usages de percussions/FX selon le moteur.

## Architecture recommandée [HEUR]

### Corps
- OSC A : wavetable simple proche sine ou source très pauvre en harmoniques.
- Unison : 1 pour le sub/body.
- Retrigger/phase : privilégier un comportement reproductible si l'attaque doit être identique [TEST selon paramètre/version].

### Pitch
- ENV pitch rapide : point de départ selon `genre-specifications.md`.
- Courbe : exponentielle/snappy pour Bass House ; plus douce pour Minimal/Techno [HEUR].

### Amplitude
- Attack 0–2 ms.
- Sustain 0 pour kick one-shot synthétique.
- Decay/tail selon style.
- Release court afin d'éviter clicks de Note Off si la note MIDI est courte [HEUR].

### Click
Choisir une seule méthode :
- NOISE très court ;
- sample transient court ;
- oscillateur supplémentaire haut-perché ;
- layer externe Ableton.

### Body/harmonics
Ajouter progressivement : waveshaping, filter drive, distortion interne ou traitement externe. Comparer au même niveau.

## Macros bridge-friendly
- `ATTACK` : niveau click + pitch amount dans plage sûre.
- `TAIL` : decay amp.
- `BODY` : drive/harmonics sans modifier brutalement le sub.
- `TONE` : filtre/EQ doux.

Ne pas mapper directement une macro de performance à une plage capable de doubler le niveau de sortie ou d'envoyer un feedback instable [HEUR].
