---
name: midi-expressif
description: Rendre une partie MIDI vivante et jouable dans Ableton Live — vélocités, durées, articulations (legato/staccato), accents, ghost notes, swing et micro-décalages adaptés à l'instrument (piano, cordes, basse, batterie, pluck), et corriger chevauchements, tessiture et notes hors registre. Utilise ce skill dès que l'utilisateur dit « plus expressif », « plus humain », « trop mécanique », « plus de groove », « swing », « trop fort/faible », « les notes se chevauchent », ou demande d'humaniser ou de nettoyer un clip.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Écriture MIDI expressive

## Diagnostic d'abord
`scripts/expression_report.py` (via `pyl.sh`, éditer PISTE/A/B) : par clip, vélocité min/moy/max, durées, notes qui se chevauchent à même hauteur, tessiture et notes hors registre de l'instrument, grille (pourcentage de notes sur la grille de croche/double). Montrer le rapport avant de toucher.

## Ce que veut chaque instrument
- **Piano feutré / cordes** : vélocités douces (40–70) avec une courbe par phrase (crescendo vers le sommet mélodique, decrescendo en fin), accords légèrement arpégés (la basse d'abord, décalage de `n/64` à `n/32` entre voix via `timing` — Producer Pal n'a pas d'unité en ms), legato réel (durée = jusqu'à la note suivante −5 %), respirations (silences) entre phrases.
- **Basse / sub** : vélocités stables (accents +10 sur les temps 1 et 3), notes courtes sur les syncopes, jamais deux notes de même hauteur qui se chevauchent (Live tronque), release dans le synthé plutôt que notes longues.
- **Hats / percussions** : `[v100 v60 v60 v60]` sur les doubles, swing 16e 0,02–0,04, ghost notes v25–40, une variation toutes les 4 mesures (note en moins, ratchet sur la dernière double).
- **Pluck / hook** : vélocités 70–100, longueurs 1/8–1/4, accent sur la première note du motif, delay en envoi plutôt que répétitions écrites.
- **Pad** : attaques anticipées de 30–60 ms avant le temps (`timing -= n/64`), vélocité liée au filtre.

## Outils Producer Pal (update-clip)
`transforms` : `velocity = ramp(48, 72)` sur une plage ; `where(note.start % 1 == 0): velocity += 10` (accents) ; `timing = swing(0.03, n/16)` (unité non documentée : relire les positions après application et noter la correspondance ici) ; pas de `rand()` sur le timing ni la vélocité (règle « pas d'humanisation aléatoire » : chaque écart est un motif répété) ; `duration = legato(0.05)` ; `C1: ratchet(2)` ; `vA-B` pour une plage aléatoire. Toujours relire (`ppal-read-clip include notes`) et refaire le rapport.

## Corrections
- Chevauchements même hauteur → raccourcir la première (`duration = legato()` sur la hauteur) ou supprimer le doublon.
- Hors tessiture → transposer d'une octave la note fautive seule (`where(note.pitch > 84): pitch -= 12`).
- Trop mécanique → varier vélocités ET durées, pas seulement le timing ; garder les downbeats exacts sur la batterie.
