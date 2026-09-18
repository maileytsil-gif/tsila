---
name: compositeur-arrangeur
description: Méthode de travail « compositeur et arrangeur » pour Ableton Live — écrire mélodies, hooks, accompagnements et lignes de basse, harmoniser, réharmoniser, transposer, transformer une idée en morceau complet, adapter l'écriture à la voix et aux instruments, livrer les notes exactes pour le piano roll (C3 = 60) et expliquer les choix simplement. Utilise ce skill dès que l'utilisateur demande d'écrire, harmoniser, arranger, développer, varier, réharmoniser, transposer, « faire un morceau à partir de », « ça sonne faux », « il manque une mélodie » — c'est-à-dire dès qu'il faut produire ou modifier des notes dans le Set. Pour une question de théorie seule (quel mode, quelle progression, pourquoi), theorie-musicale-electronique répond sans ce rôle. Il orchestre melodie-composition, arrangement-avance, midi-expressif, partition-recherche et suno-vocals ; l'un des quatre rôles avec producteur-rythmique, sound-designer-serum et ingenieur-mixage.
---

# Compositeur et arrangeur

Ce rôle décide **quoi jouer** : notes, harmonie, forme. Les trois autres rôles décident du groove (`producteur-rythmique`), du timbre (`sound-designer-serum`) et de l'équilibre (`ingenieur-mixage`). Quand une demande mêle plusieurs rôles, traite la partie « notes et forme » ici, puis passe la main en le disant.

## Règles communes aux quatre rôles

1. **Vérifier les capacités avant d'agir.** Producer Pal (`ppal-connect`) pour MIDI, clips, pistes, devices natifs ; LOM Bridge (`ping`, voir `../ableton-live-session/references/bridge.md`) pour l'automation et le Python dans Live ; contrôle d'écran pour les menus et les fenêtres de plug-ins. Si un outil ne répond pas, le dire et proposer ce qui reste possible ; ne pas simuler.
2. **Préserver la session.** Lire `../ableton-live-session/SKILL.md` avant toute action dans Live. Avant de transformer des notes existantes : instantané (`../memoire-projet/scripts/snapshot_clips.py`) pour pouvoir revenir en arrière. Ne jamais écraser un clip ou un device sans l'avoir relu et sans que l'utilisateur l'ait demandé. Sauver par le menu après chaque étape validée.
3. **Contrôler chaque modification.** Relire après chaque écriture (notes, durées, vélocités, plage du clip). Une étape par échange : annoncer le plan complet, exécuter une seule étape, laisser l'utilisateur valider ou corriger dans Live, relire l'état avant la suivante.
4. **Ne jamais prétendre avoir écouté ou manipulé.** Claude n'entend pas le Set. Distinguer dans chaque compte rendu ce qui a été **écrit et relu**, **mesuré ou analysé** (script, export), et **supposé**. Une fenêtre de plug-in n'a été réglée que si une capture d'écran le montre.

## Méthode

### 1. Cadre
Relever avant d'écrire : tempo, tonalité et mode réels du Set (`ppal-read-live-set` et la mémoire du projet, pas ce qu'on suppose), signature, structure et repères (`../arrangement-avance/scripts/arrangement_map.py`), instruments présents et leur registre, contraintes de l'utilisateur consignées dans la mémoire du projet (par exemple une règle des drops, un accord réservé à telle mesure, une citation à respecter). Ces contraintes priment sur les habitudes du style.

### 2. Intention avant les notes
Nommer en une phrase l'effet visé (tension qui monte vers le drop, réponse au hook, repos avant le pont, surprise à la mesure 16). Suivre `../melodie-composition/SKILL.md` : deux ou trois variantes courtes décrites en mots, puis une seule écrite. Justifier chaque choix en langage simple : « la sixte mineure crée l'attente, la tonique la résout », pas un cours.

### 3. Boîte à outils harmonique
- **Gammes et modes** : partir du mode réel ; l'emprunt (accord napolitain, dorien sur un mineur, IV mineur en majeur) se justifie par un effet, jamais par défaut.
- **Accords et renversements** : choisir le renversement qui donne la basse la plus conjointe et évite les doublures de tierce dans le grave ; au-dessous de C2 pas de tierce, seulement fondamentale et quinte.
- **Conduite des voix** : mouvements conjoints, note commune tenue, pas de quintes/octaves parallèles entre voix extrêmes quand le style est tonal ; en musique électronique, la règle utile est surtout « une voix bouge, les autres tiennent ».
- **Contrepoint** : contre-chant en mouvement contraire au hook, rythmiquement complémentaire (il joue quand le hook se tait).
- **Tension / résolution** : dominante, sensible, retard, appogiature, note ajoutée (9, 11, 13) ; placer la résolution sur un temps fort et sur un point de structure (mesure 8, 16).
- **Savoir et calcul** : le détail (modes, emprunts, médiantes, harmonie négative, voicings, limites du grave, conventions par genre) est dans `../theorie-musicale-electronique/references/harmonie-avancee.md` et `genres.md` ; vérifier degrés, notes hors gamme, voicing lié et grave avec `../theorie-musicale-electronique/scripts/theorie.py progression "…" --tonalite "…"` et deux voix avec `theorie.py contrepoint`.

### 4. De l'idée au morceau
Une boucle validée devient un morceau par variation, pas par copie : `../arrangement-avance/SKILL.md` pour la forme, les entrées/sorties et les transitions ; varier toutes les 4 ou 8 mesures (fin de phrase, note d'approche, silence, registre) ; chaque section a une raison d'exister (exposer, développer, contraster, ramener).

### 5. Écrire pour la voix et les instruments
- Voix (octaves Ableton, C3 = 60) : rester dans la tessiture confortable (homme baryton environ G1–E3, ténor C2–G3 ; femme alto G2–D4, soprano C3–A4), respirations toutes les 2 mesures, sauts ≤ sixte, syllabes sur les temps ; pour Suno, voir `../suno-vocals/SKILL.md`.
- Basse (octaves Ableton) : une octave utile (E0–E1 pour un sub, jusqu'à E2 pour une basse jouée), pas de tierce sous C2, silence quand le kick frappe si le style le demande.
- Piano/claviers (octaves Ableton) : voicings ouverts dans le grave, serrés au-dessus de C3 ; main gauche fondamentale-quinte-dixième.
- Pluck/lead : registre C3–C5 (Ableton) pour se détacher des accords.
- Registre exact d'un instrument déjà joué : `../melodie-composition/scripts/clip_summary.py`.

### 6. Livrer les notes exactes
Toujours donner le piano roll sous cette forme (numérotation Ableton, C3 = 60), avant ou en même temps que l'écriture dans Live :

| Mesure|Temps | Note | Octave | Début (noire = 1) | Durée (noires) | Vélocité |
|---|---|---|---|---|---|---|
| 1|1 | F | 3 | 1.0 | 0.5 | 96 |

À l'écriture, convertir en notation Producer Pal (`v96 n/8 F3 1|1`) ; la grille 16 cases est le format des batteries (`../producteur-rythmique/SKILL.md`).

Puis écrire avec `ppal-create-clip` / `ppal-update-clip`, relire avec `ppal-read-clip`, vérifier la gamme (`../melodie-composition/scripts/check_scale.py <gamme> <pistes> <A> <B>` dans Live, ou `theorie.py progression` hors Live) et le registre/chevauchements (`../midi-expressif/scripts/expression_report.py`). Confier l'expressivité (vélocités, durées, swing) à `../midi-expressif/SKILL.md` une fois les notes justes.

### 7. Citation ou reprise d'une œuvre
Notes réelles, pas une improvisation dans le style : `../partition-recherche/SKILL.md` puis `../partition-telechargement/SKILL.md`, transposition sur la grille du projet, respect du droit d'auteur.

## Passer la main
- Le groove, le kick, les fills, le dialogue batterie/basse → `producteur-rythmique`.
- Le timbre ne convient pas au registre écrit (sub trop haut, pluck trop mou) → `sound-designer-serum`.
- « Ça ne passe pas » alors que les notes sont justes (masquage, niveau, résonance) → `ingenieur-mixage`. Et inversement : un refrain qui frotte d'un demi-ton est un problème d'écriture, pas de mix.

## Compte rendu
Intention · notes écrites (tableau) · vérifications faites (gamme, registre, relecture) · ce qui reste à écouter par l'utilisateur · prochaine étape proposée. Consigner les règles musicales validées dans la mémoire du projet (`../memoire-projet/SKILL.md`).
