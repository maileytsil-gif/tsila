---
name: memoire-projet
description: Mémoire de travail d'un morceau Ableton entre deux échanges, deux sessions et deux compactages — quoi noter, quand, où, et comment revenir en arrière. Utilise ce skill au DÉBUT de toute session Live (« on reprend », « on continue », ouverture d'un Set), à la FIN (« on reprend plus tard », « on continue demain »), après CHAQUE étape validée et sauvegardée, avant toute transformation de notes ou d'automation (pour pouvoir annuler), et dès que l'utilisateur dit « garde ça en mémoire », « note », « souviens-toi », « remets comme avant », « annule ». Il complète ableton-live-session : celui-là dit comment agir dans Live, celui-ci dit comment ne rien perdre de ce qui a été décidé, mesuré ou appris.
---

# Mémoire de projet (Ableton)

## Pourquoi c'est vital ici
- L'utilisateur **modifie le Set lui-même** entre deux échanges et écoute souvent pendant que je travaille : l'état réel diverge de ce que je crois savoir.
- Les conversations sont **compactées** : ce qui n'est pas écrit dans la mémoire ou dans un fichier est perdu (valeurs exactes, refs de paramètres, questions restées sans réponse).
- « Remets comme avant » arrive régulièrement : il faut pouvoir **revenir en arrière sans undo**, à partir d'une sauvegarde (.als) ou d'un instantané JSON.

## Où va quoi
| Contenu | Destination |
|---|---|
| État du morceau, décisions de l'utilisateur, valeurs écrites, ce qui reste à faire | `memory/projet-<nom>.md` (une ligne datée par étape, en-tête **REPRISE** tenu à jour) |
| Piège technique réutilisable (API, bridge, plug-in, mesure) | `references/` du skill concerné (`../ableton-live-session/references/bridge.md`, `plugins.md`, `../effets-plugins/references/fiches.md`) — pas dans la mémoire projet |
| Consigne de méthode donnée par l'utilisateur (« une étape par échange », « plus de natifs ») | mémoire `feedback` (fichier dédié + ligne dans `MEMORY.md`) |
| Instantanés de notes / spécifications d'automation | fichiers JSON (scratchpad pendant la session, `~/.claude/snapshots/` pour ce qui doit survivre) |

## Trois moments

### 1. Début de session (« on reprend »)
1. `scripts/reprise.sh <slug>` : affiche l'en-tête REPRISE et les 12 dernières entrées de la mémoire projet.
2. **Relire l'état réel** avant d'agir : `lom.py state --json` (pistes, devices, paramètres automatisés, repères, transport) puis carte des clips (`../arrangement-avance/scripts/arrangement_map.py`) ou `scripts/snapshot_clips.py` ; comparer avec la mémoire, noter les écarts (« l'utilisateur a dupliqué le hook sur 13–17 et 21–25 »). `lom.py journal 10` montre ce que le bridge a écrit depuis la dernière entrée de la mémoire (y compris dans une séance compactée).
3. Vérifier `lom.py transport` (lecture en cours ?) et l'heure du dernier `.als` sauvé.
4. Si une **question était restée sans réponse** (entrée « question posée »), la reposer en une phrase avant toute chose.

### 2. Pendant (après chaque étape validée)
- Écrire une entrée **avant** de passer à la suite : `scripts/journal.sh <slug> "<texte>"` (date ajoutée automatiquement). Voir `references/format.md` pour le gabarit : quoi / où (mesures, pistes, clips) / valeurs exactes (dB, Hz, MIDI, refs `o:…`) / relecture faite / ce qui reste.
- Avant toute transformation de notes (re-voicing, transposition, réécriture) : `scripts/snapshot_clips.py` via `pyl.sh` → JSON daté (ou `lom.py notes get "<piste>" <t> --json` par clip) ; après : `scripts/diff_snapshot.py avant.json apres.json` pour vérifier que seules les pistes visées ont bougé. Écrire avec `lom.py notes set` : relu note à note, défait si Live n'a pas écrit ce qui était demandé.
- Avant tout réglage à la main (fader, envoi, paramètre de device) : `lom.py snapshot "<piste>" [device|mixer]` — noter l'id dans l'entrée de journal ; `lom.py restore <id>` remet tout en une étape (perdu au redémarrage de Live : les valeurs d'origine vont aussi dans la mémoire).
- Ne jamais identifier des accords ou des motifs sur un **résultat intermédiaire** : partir des notes d'origine (instantané ou `.als` sauvé). C'est ainsi qu'une passe « jazzy » a cascadé en erreurs et a dû être annulée.
- Quand l'utilisateur tranche entre plusieurs options, noter **l'option retenue et celles refusées** (il revient parfois dessus : « non, remets le piano comme c'était »).
- Un « remets comme avant » : dire précisément quel « avant » est restauré (heure du .als, instantané), et le noter.

### 3. Fin de session (« on reprend plus tard », « on continue demain »)
1. Sauver le Set (Fichier › Sauver Set Live) et noter l'heure du fichier. `lom.py journal 20` : toute écriture du bridge non encore dans la mémoire y est recopiée (commande, valeurs, relecture, code d'erreur).
2. Réécrire l'en-tête **REPRISE** de la mémoire projet : état en 3 lignes, en attente (fichiers, réponses de l'utilisateur), prochaines étapes proposées dans l'ordre.
3. Mettre à jour `MEMORY.md` si le résumé d'une ligne a changé (numéro de version, durée, tonalité).

## Revenir en arrière
- Live écrit une copie horodatée à chaque sauvegarde dans `<dossier projet>/Backup/<Set> [AAAA-MM-JJ HHMMSS].als`. `scripts/als_notes.py <fichier.als> <sortie.json> [PISTE …]` extrait les notes visibles des clips d'arrangement (temps absolus) — sans ouvrir le Set. Réinjecter avec `lom.py notes set "<piste>" <t> '<json>'` dans le clip existant (relu, défait sur écart ; ne pas supprimer le clip : l'automation y est attachée).
- Pour les réglages : `lom.py restore <id>` d'un snapshot pris avant l'essai (même séance de Live).
- Comparer l'état courant à l'instantané avec `diff_snapshot.py` avant d'annoncer « restauré ».
- Pour l'automation : les specs JSON `apply` du bridge sont la mémoire — les garder (scratchpad puis snapshots) pour réappliquer une version antérieure.

## Ce qu'il faut absolument écrire (liste des oublis qui ont coûté cher)
- Valeurs exactes d'origine **avant** de les changer (fader, envoi, fréquence) — sinon impossible de « remettre comme avant ».
- Les refs de paramètres du bridge (`o:494615:36`) et l'unité utilisée (`disp`/`raw`).
- Les pièges de mesure (vu-mètres non linéaires, pré-fader) — dans `references/pieges.md` de ce skill, puis dans le skill technique concerné.
- Les consignes du type « sauf clap et rim », « conserve les mélodies des hooks », « hook absent avant 41 » — et leur **levée** quand l'utilisateur change d'avis.
