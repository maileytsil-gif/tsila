---
name: melodie-composition
description: Composer dans Ableton Live (via Producer Pal) à partir d'une intention musicale — tension, résolution, surprise, dialogue entre instruments — des mélodies, hooks, contre-chants, arpèges, lignes de basse, voicings, modulations et échanges modaux, en proposant des variantes puis en vérifiant la cohérence harmonique et rythmique note à note. Utilise ce skill dès que l'utilisateur demande une mélodie, un motif, un thème, un riff, une réponse, une variation, une reharmonisation, une modulation, une citation (Beethoven…), ou dit qu'une partie « ne passe pas », même en deux mots (« rajoute une mélodie », « change l'harmonie »).
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Composition à partir de l'intention

## 1. Nommer l'intention avant les notes
Traduire la demande en trois choses : **l'effet** voulu (tension qui monte, repos, surprise, dialogue, nostalgie), **le rôle** de la ligne (hook, réponse, contre-chant, nappe, basse), **la contrainte** (tonalité et emprunts admis, registre libre, hook fixe, règle des drops, ce que l'utilisateur a déjà écrit — lire avec `scripts/clip_summary.py`). Si l'effet n'est pas clair, proposer deux lectures en une phrase chacune plutôt que d'accumuler des notes.

## 2. Proposer 2–3 variantes courtes, puis en écrire une
Chaque variante = un moyen différent d'obtenir l'effet : par la **mélodie** (appogiature, saut résolu, note tenue), par l'**harmonie** (extension, échange modal, napolitaine, dominante empruntée), par le **rythme** (anticipation, silence, hémiole), par le **dialogue** (réponse dans les silences, mouvement contraire). Décrire chacune en deux lignes avec les notes clés ; écrire celle que l'utilisateur choisit (ou la plus sobre s'il dit « choisis »). Méthode détaillée : `references/methode.md`.

## 3. Écrire (Producer Pal) et vérifier
- Notation `v n pitch bar|beat`, C3 = 60, triolets `+n/12`, brackets, copies `@5-8=1-4`, transformations. Générer par script les longues répétitions.
- **Vérification obligatoire**, à montrer : `scripts/clip_summary.py` (accords par temps, mélodie par mesure), `scripts/check_scale.py` (notes hors gamme par mesure — chaque emprunt doit être voulu et nommé), frottements de demi-ton tenus entre voix (le premier suspect d'un « ça ne passe pas »), doublures de hauteur avec une autre voix, tessiture, chevauchements même hauteur, cohérence rythmique avec la basse (les accents tombent-ils ensemble ou se répondent-ils ?).
- Sauver ; noter en mémoire l'harmonie retenue.

## Modifier l'existant sans casser
- Transposer une section (tout sauf batterie) : `scripts/transpose_range.py`.
- Reharmoniser : remapper hauteurs par mesure et classe de note (`apply_note_modifications`) ; MIDI Ableton : Db3 = 61, F3 = 65, Ab3 = 68, C4 = 72.
- « La basse suit l'accord » : garder le rythme, assigner les degrés lus dans CHORDS (fondamentale = note la plus grave), sub −12.
- Copier un drop sur un autre : dupliquer +N mesures, transposer les seules mesures de changement.
