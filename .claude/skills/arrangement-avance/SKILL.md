---
name: arrangement-avance
description: Construire ou remanier la structure d'un morceau dans Ableton Live — transformer une boucle en morceau complet, poser les sections et repères, organiser entrées/sorties des éléments, contrastes de densité, transitions (breaks, ponts, drops, sweeps, coupures), copier/varier des sections, allonger ou raccourcir sans casser automations et repères. Utilise ce skill dès que l'utilisateur parle de structure, d'intro/outro, de drop, de break, de pont, de transition, de « tire la section », « décale », « fais ressembler le drop 2 au drop 1 », ou donne un minutage.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Arrangement avancé dans Live

## Lire avant de toucher
`scripts/arrangement_map.py` (via `pyl.sh`) : tableau piste × sections (clips présents, nombre de notes), repères, durée totale. L'utilisateur édite à la main : reconstruire la carte avant chaque changement de structure.

## Construire une structure
- Grille par genre (house, techno, trance, DnB, dubstep, hip-hop, tempos) : `../theorie-musicale-electronique/references/forme-tension.md`. Exemple deep/minimal house 120 BPM : intro DJ (16–24 mes., pulsation seule puis entrées progressives) · break · drop 16 · pont 8 · break · drop 16 · refrain 8 · pont 8 · drop 16 · outro DJ 16. Chaque section = un repère nommé (`ppal-update-live-set locatorOperation create`), fin d'export = repère « FIN export m:ss ».
- Densité : un élément entre ou sort toutes les 4 ou 8 mesures ; jamais tout en même temps sauf au downbeat d'un drop. Contraste avant un drop : retirer le kick ou le grave sur 4–8 mesures, filtrer (skill `live-automation`), couper net au downbeat.
- Drops « presque statiques » : énergie par le groove, les textures et les automations, changements d'accord seulement aux mesures prévues ; drop 3 = le plus abouti sans être plus fort.
- Outro : retirer les éléments mélodiques, garder kick/hats/percs, queues d'effets éteintes avant la fin exacte.

## Opérations sûres
- **Allonger/raccourcir** : poser la boucle (`song.loop_start/loop_length` en temps), vue Arrangement, Edition › Sélectionner boucle, puis Créer › Insérer Silence (ou Edition › Supprimer Zone temporelle) : clips, automations et repères bougent ensemble. Relire la carte ; la première tentative peut viser 1|1 si la boucle n'était pas posée — vérifier avant d'insérer.
- **Copier une section sur une autre** : `duplicate_clip_to_arrangement(clip, t + N*4)` par piste après suppression des clips de destination ; garder les pistes qui portent l'identité harmonique de la section cible (accords, pad) ; transposer les seules mesures de changement (`apply_note_modifications`).
- **Remplir une extension** : dupliquer les clips de la section voisine (`ppal-duplicate` avec `arrangementStart`), les automations tiennent leur dernière valeur sur le trou.
- Le hook n'apparaît que là où il est attendu (annonce voilée au break 1, refrain clair) ; les réponses vivent dans les silences.
- Après tout : `arrangement_map.py`, sauvegarde, note en mémoire (les ids Producer Pal changent après reconstruction).
