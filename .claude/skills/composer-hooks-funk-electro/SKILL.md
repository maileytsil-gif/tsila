---
name: composer-hooks-funk-electro
description: Atelier de genre pour écrire un hook ou un thème instrumental mémorable — funk, acid jazz, pop, house, tech house, afro house, bass house, microhouse/minimal, chill out, électro chill, jazz chill, électro R&B — de la cellule rythmique (3 à 6 attaques et un silence) à l'orchestration par instrument (basse funk, clav, Rhodes, cuivres, lead, chops), avec grilles MIDI vérifiées (C3 = 60, `grille.py` → tableau et notation Producer Pal), 55 recettes Serum 2 de départ à quatre macros, deux kicks 808, sampling, transitions de groupe, vocoder et corpus de références sourcées. Utilise ce skill dès que l'utilisateur demande un hook, un riff, un thème « qui reste en tête », un groove funk ou acid jazz, la même idée en version house / tech / afro / bass house, une ambiance chill ou jazz chill, un morceau microhouse, une couleur électro R&B, ou parle de Rhodes, clav, cuivres, vocoder ou 808 pour composer. C'est la bibliothèque de genre des rôles compositeur-arrangeur (notes) et sound-designer-serum (recettes) : pour agir dans Live il passe par eux et par la discipline d'ableton-live-session.
---

# Composer un hook jouable (funk → électro)

Ce skill dit **quoi écrire dans ces genres** et donne des points de départ de timbre. Il n'écrit pas seul dans Live : l'écriture de notes suit `../compositeur-arrangeur/SKILL.md`, le timbre `../sound-designer-serum/SKILL.md`, le groove `../producteur-rythmique/SKILL.md`, et toute action dans Live la discipline de `../ableton-live-session/SKILL.md`. Hors Claude Code (Codex, Qwen), ces liens ne pointent vers rien : appliquer les règles ci-dessous, qui en sont le résumé.

## Règles du workflow qui priment sur les références

1. **C3 = 60 partout** (numérotation Ableton) ; le numéro MIDI fait foi. Toutes les grilles de `references/` sont en C3 = 60. Une note venue d'ailleurs (notation scientifique C4 = 60, autre modèle, livre) se convertit : octave Ableton = octave scientifique − 1 (`scripts/grille.py --source scientifique`).
2. **Lire avant d'écrire.** Tempo, tonalité, repères et contraintes de la mémoire du projet (`../memoire-projet/SKILL.md`) priment sur les exemples, qui sont des exercices originaux à transposer (`grille.py --transposer`).
3. **Une étape par échange.** Annoncer le programme (cellule → question/réponse → orchestration → timbre → tests), n'exécuter qu'une étape, faire valider la cellule avant tout développement.
4. **Jamais « entendu ».** Claude ne fredonne ni n'écoute : les tests de mémorisation reviennent à l'utilisateur ; Claude livre les contrôles mesurables (`grille.py`, relecture du clip, `check_scale.py`, `theorie.py`).
5. **Effets natifs.** La règle 6 d'`ableton-live-session` exclut tout nouvel effet natif des chaînes de mix. Les chaînes des références qui en citent se transposent avec `references/effets-groupes-vocoder.md` § Dans ce workflow (REQ 6, MetaFlanger, bx_glue, J37, édition, resampling) ; sinon demander l'exception.
6. **Recettes = points de départ**, jamais « label ready ». Sources : distinguer documenté, transcription lue, flux réellement visionné, hypothèse (`references/sources-videos.md`).

## Méthode

1. **Cadre.** Fonction du thème, tempo, mesure, progression, registre, instrument vedette, durée (2, 4 ou 8 mesures), lus dans le Set et la mémoire. Brief incomplet : poser une hypothèse, la dire, avancer.
2. **Cellule.** 3 à 6 attaques avec au moins un silence caractéristique, écrites dans la grille de doubles croches (notation ci-dessous), hauteurs relatives et articulation. Proposer deux ou trois cellules en mots (`../melodie-composition/SKILL.md` § 2), en écrire une. Mesurer la syncope : `grille.py` imprime la ligne d'attaques à passer à `../theorie-musicale-electronique/scripts/theorie.py syncope`.
3. **Harmonie.** Notes d'accord sur les accents voulus ; approche chromatique et tensions sur les autres attaques, en disant où chaque tension résout. `grille.py --accords` nomme le degré de chaque note et signale toute note hors accord non résolue (marquer `!` une tension voulue).
4. **Question, réponse, répétition, variation.** Garder au moins deux traits fixes parmi rythme, contour, intervalle, timbre et placement ; changer un trait à la fois.
5. **Orchestrer.** Registre, attaques, silences, notes tenues ou mortes et rôle de réponse de chaque instrument : `references/phrases-par-instrument.md` (zones utiles en C3 = 60).
6. **Programmer.** Grille exacte → `scripts/grille.py` → tableau du rôle compositeur-arrangeur et notation Producer Pal → `ppal-create-clip` / `ppal-update-clip` → relecture `ppal-read-clip`, `check_scale.py` et `expression_report.py` dans Live. Deux thèmes complets vérifiés : `references/atelier-themes.md`. Vélocités, swing et durées fines : `../midi-expressif/SKILL.md`, une fois les notes justes.
7. **Timbre.** Choisir un son qui rend le phrasé lisible : `references/sound-design.md` (basses, temps en ms selon le BPM), `references/palette-production.md` (méthode, macros), `references/cinquante-cinq-recettes.md` (cinq recettes Serum 2 par famille), `references/kick-808-detail.md`. Réalisation par sound-designer-serum → `../vst-sound-design/SKILL.md` (chargement sans hot-swap, tableau paramètre / valeur / preuve). Distinguer le preset de la composition.
8. **Tester.** Mesurable (Claude) : `grille.py` sans ⚠ non voulu, `theorie.py contrepoint` entre lead et basse, relecture Live, niveaux relatifs. Écoute (utilisateur) : fredonner le thème après une écoute ; le retrouver après huit mesures sans piste principale ; comparer sa silhouette avec basse et batterie seules. Si le thème échoue, retirer des attaques ou renforcer un silence, un accent ou une répétition avant d'empiler des effets.

## Notation de grille

```
Ab3[1&:2] C4[2a:1] Eb4[3&:2] C4[4&:1] | % | F3+Ab3+C4[1:4] Bb3![3a:1:110]
```
Positions `1 e & a 2 e & a 3 e & a 4 e & a` (4/4) ; durée en doubles croches ; `|` sépare les mesures, `%` répète la précédente, `+` fait un accord, `!` marque une tension voulue, un troisième champ fixe la vélocité. Dans un fichier, un bloc ` ```grille ` réunit `titre:`, `tempo:`, `accords: Fm9 | Fm9 | Bb13 | Bb13` et une ligne par voix (`lead:`, `basse:`…).

```bash
python3 scripts/grille.py "Ab3[1&:2] C4[2a:1] Eb4[3&:2] C4[4&:1]" --accords "Fm9"      # rapport complet
python3 scripts/grille.py --fichier references/atelier-themes.md --titre funk --transposer -3 --format ppal
python3 scripts/grille.py --verifier references/*.md                                    # contrôle des références
```

## Par genre ou par demande

| Demande | Lire |
|---|---|
| Hook funk house, acid jazz / pop | `atelier-themes.md`, `phrases-par-instrument.md` |
| Même cellule en house, tech house, afro house, bass house, electro house | `phrases-par-instrument.md` § Traduire entre styles, `palette-production.md` § Vérification par style |
| Microhouse, minimal house | `microhouse-complet.md` |
| Chill out, électro chill, jazz chill | `chill-electro-jazz.md` |
| Électro R&B récent | `electro-rnb-2021-2026.md` |
| Samples, chops, riser, impact | `sampling-arrangement.md` → `../resampling/SKILL.md`, `../sampling-composition-avancee/SKILL.md` |
| Transition de groupe, sweep, flanger, coupe-coupe, vocoder | `effets-groupes-vocoder.md` → `../live-automation/SKILL.md`, `../effets-plugins/SKILL.md` |
| Recettes Serum 2, kicks | `palette-production.md`, `cinquante-cinq-recettes.md`, `kick-808-detail.md`, `sound-design.md` |
| Artistes, crédits, études | `producteurs-exemples.md` (et les études de `../produire-morceau-electronique-de-a-a-z/references/`) |
| Vidéos, tutoriels, statut des sources | `sources-videos.md` |

Pour situer un son dans des productions réelles : distinguer déclarations directes, descriptions éditoriales et transpositions proposées vers Serum 2 ; ne pas attribuer un preset inventé à un artiste. Pour une vidéo : URL, créateur, statut (flux visionné, transcription complète, extrait, description seulement), timecodes vérifiés, observation, application ; si YouTube bloque, demander le fichier ou une transcription. Ne pas présenter un sample commercial non autorisé comme publiable.

## Livrer, une étape à la fois

Cellule (grille + intention) → grille de 4 à 8 mesures avec rôle de chaque piste et rapport du thème aux accords → patch de départ → variante A/B. Morceau complet seulement après validation de la cellule centrale (`../arrangement-avance/SKILL.md` ; morceau entier : `../produire-morceau-electronique-de-a-a-z/SKILL.md`). Pour adapter la cellule aux versions house, tech house, afro house et bass house, garder deux traits identitaires et préciser ce qui change dans percussion, basse, articulation, timbre et densité ; ne pas réduire un style à un pattern universel.

**Compte rendu** : intention · grille et tableau des notes · contrôles faits (`grille.py`, relecture, gamme) · ce qui reste à écouter par l'utilisateur · prochaine étape. Consigner la cellule validée et ses deux traits identitaires dans la mémoire du projet.

## Portabilité (Codex, Qwen)

`scripts/install.sh` installe ce dossier pour Claude Code et Codex et le lanceur `qwen-musique` ; `scripts/qwen-musique.py` donne le skill à un modèle Ollama avec une fenêtre de contexte explicite. Mode d'emploi et limites : `references/portabilite.md`.
