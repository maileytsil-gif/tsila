---
name: partition-recherche
description: Retrouver en ligne une partition fiable d'un morceau connu (classique, jazz standard, traditionnel, chanson) sous une forme exploitable — encodage Humdrum kern, MusicXML, MIDI, LilyPond, ou PDF lu visuellement — puis en extraire les notes exactes (hauteurs, rythme, mesures d'origine) et les transposer sur la grille du projet Ableton (tempo, mesure, triolets), en respectant le droit d'auteur. Utilise ce skill dès que l'utilisateur veut citer, reprendre, réinterpréter ou vérifier « les vraies notes » d'une œuvre existante (Beethoven, Bach, Chopin, Satie, un thème de film, un standard…), ou dit « retrouve la partition », « pas une improvisation dans son style ».
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Partition d'un morceau connu → notes exactes dans Live

## 1. Droit d'auteur d'abord
- **Domaine public** (compositeur mort depuis plus de 70 ans en Europe — Beethoven, Bach, Chopin, Debussy, Satie…) : reproduction intégrale possible.
- **Œuvre protégée** (jazz après ~1930 selon les auteurs, chansons, musiques de film) : ne pas reproduire la mélodie ni les paroles dans le projet ; se limiter à l'analyse (structure harmonique, degrés) et à une courte référence, et le dire à l'utilisateur. L'édition d'une partition récente d'une œuvre ancienne peut elle-même être protégée (gravure, doigtés) : préférer les encodages libres.

## 2. Sources, dans l'ordre de fiabilité et de facilité (`references/sources.md`)
1. **Encodages textuels sur GitHub** (Humdrum `**kern`, dépôts de Craig Sapp / KernScores : sonates de Beethoven, Mozart, Haydn, Chopin, Bach…) : `curl` direct, notes et rythmes exacts, mesures numérotées. `scripts/fetch_kern.sh <dépôt> <fichier>`.
2. **MusicXML / MIDI libres** : OpenScore (domaine public) et Mutopia (LilyPond + MIDI) se téléchargent par script (`../partition-telechargement/scripts/openscore.sh`, `mutopia.sh`) ; Wikimedia Commons, Kunst der Fuge (abonnement).
3. **IMSLP** (PDF scannés, domaine public) : téléchargement direct bloqué ; passer par le Chrome de l'utilisateur vers `~/Downloads` puis lire le PDF page par page, ou lire la partition à l'écran (`../partition-telechargement/SKILL.md`). Fiable mais lent : réserver aux œuvres absentes des encodages.
4. Sites de partitions commerciaux, tablatures, vidéos YouTube : indices seulement, à recouper.
Toujours **recouper deux sources** ou vérifier la cohérence interne (durées par mesure = signature).

## 3. Extraire et convertir
- `scripts/kern_to_notes.py fichier.krn --mesures 1-4 [--spine 2]` : liste (mesure, temps en noires, durée, hauteur scientifique, MIDI) par voix, avec liaisons résolues et notes d'agrément signalées.
- `scripts/notes_to_ppal.py` : convertit en notation Producer Pal (C3 = 60 !), avec **mapping de mesure** : 12/8 → 4/4 (une croche = triolet `n/12`, une mesure = une mesure), 3/4 → 4/4 (choix explicite : ajouter un temps de silence ou compresser), tempo du projet ; positions en `bar|beat` décimales ou `+n/12`, durées `n5/24` etc.
- Nommer le clip avec les **mesures d'origine** (« orig. mes. 1-4 ») pour ne jamais les confondre avec celles de l'arrangement ; noter la source (URL, fichier) dans la mémoire du projet.

## 4. Réinterpréter sans trahir
Garder hauteurs et rythme relatifs ; adapter registre (éviter le grave du kick/sub), vélocités (pp → v40–60, sfz → accents), silences originaux (ils font partie de la citation), et expliquer les notes hors gamme héritées (ex. mi♮ et si♮ de l'Appassionata en fa mineur). Vérifier après écriture (skill `melodie-composition` : `clip_summary.py`, `check_scale.py`).
