---
name: modern-pop-electronic-music-theory
description: Théorie musicale appliquée à la Pop moderne et aux musiques électroniques : gammes, degrés, accords, voice leading, mélodie, hooks, basslines, groove, forme, tension/release, topline, drops et workflow Ableton Live 12. Utiliser pour composer, corriger ou expliquer quoi jouer et pourquoi, sans copier une œuvre de référence.
---

# Modern Pop & Electronic Music Theory — v11

Ce skill transforme la théorie en **décisions musicales exécutables**. Il ne cherche pas à rendre un morceau complexe : il cherche à rendre chaque choix **audible, mémorisable, cohérent et utile à l'énergie**.


## Délégation jazz/chill
Pour jazz moderne, jazz-funk, neo-soul, chill-out/downtempo, voicings quartaux/upper-structures ou phrasé 16e laid-back, déléguer les décisions spécialisées à `modern-jazz-chillout-theory`, puis revenir ici pour les éléments Pop/Electro généraux.

## Hiérarchie des preuves

- **[DOC]** : théorie ou comportement Ableton documenté par une source pédagogique/officielle.
- **[ATTRIB]** : méthode ou idée attribuée à un auteur/producteur dans une interview identifiable.
- **[ANALYSIS]** : conclusion tirée de l'étude de morceaux ou de plusieurs sources.
- **[HEUR]** : règle de travail proposée ; utile, mais non universelle.
- **[TEST]** : décision qui doit être écoutée ou vérifiée dans le projet réel.

Toujours distinguer ces niveaux. Ne jamais présenter une heuristique comme une loi musicale.

## Avant toute composition

Lire, selon la tâche :

1. `references/theory-core.md`
2. `references/melody-hook-design.md`
3. `references/harmonic-function-and-loops.md`
4. `references/voice-leading-inversions.md`
5. `references/rhythm-groove-harmonic-rhythm.md`
6. `references/song-form-energy.md`
7. `references/ableton-live12-composition-workflow.md`
8. `references/theory-decision-tree.md` pour diagnostic rapide

Si l'utilisateur cite un artiste ou recherche une direction commerciale, lire `references/composer-corpus.md` et les profils pertinents. Les profils servent à extraire des **principes abstraits**, jamais à reproduire une mélodie, un hook, une progression distinctive ou un arrangement reconnaissable.

## Workflow obligatoire

1. **Intention** — définir émotion, style, BPM, tonalité/centre tonal, public/destination et rôle du morceau.
2. **Centre tonal** — choisir tonique et mode/gamme. Ne pas ajouter de notes « avancées » avant que le centre soit clair.
3. **Harmonie** — écrire les degrés et la fonction de chaque accord avant les noms de notes. Identifier boucle, cadence, pédale ou mouvement modal.
4. **Voice leading** — réduire les sauts inutiles par notes communes et inversions quand cela sert la fluidité.
5. **Bassline** — décider si elle double les fondamentales, anticipe les accords, utilise des notes de passage ou devient un hook autonome.
6. **Mélodie** — créer un motif court ; définir contour, rythme, registre, note cible et relation aux accords.
7. **Hook** — tester mémorisation, répétition, contraste et identité rythmique. Une idée forte vaut mieux que plusieurs idées moyennes.
8. **Énergie** — contrôler densité, registre, rythme harmonique, longueur de notes, silence et orchestration ; ne pas confondre énergie et volume.
9. **Forme** — organiser les sections selon la fonction : exposition, montée, payoff, respiration, variation, retour.
10. **Ableton** — traduire en clips MIDI, notes, durées, vélocités, Scale Mode, Transformations/Generators si utiles.
11. **Validation** — écouter d'abord sans regarder l'écran ; vérifier que le hook, la tension et le contraste restent perceptibles à niveau égal.

## Règles de composition Pop/Electro

- [DOC] Une bassline peut renforcer les accords tout en ayant son propre rythme ; traiter harmonie et groove ensemble.
- [DOC] La forme peut être pensée comme des motifs regroupés en sections ; les blocs de 4/8/16 mesures sont fréquents mais non obligatoires.
- [DOC] Le voice leading gagne en fluidité par notes communes et inversions.
- [HEUR] Réserver le registre ou la note la plus haute à un moment important peut donner plus de valeur au refrain/drop.
- [HEUR] Si le refrain ne semble pas plus grand, modifier d'abord registre, rythme, densité ou contour avant de changer toute la progression.
- [HEUR] Dans l'électronique, le **drop peut fonctionner comme un refrain instrumental** : il doit avoir une identité mémorisable, pas seulement plus de basses.
- [HEUR] Une progression simple avec une mélodie forte est généralement préférable à une progression complexe qui brouille le hook.
- [TEST] La quantité de répétition tolérable dépend du son, du groove, de la durée et du contexte ; décider à l'écoute.

## Originalité et références

Utiliser la méthode Ableton du **catalogue d'attributs** : analyser séparément son, harmonie, mélodie, rythme et forme ; ensuite écarter la référence et composer à partir des attributs abstraits. Ne jamais recopier une séquence mélodique, une bassline distinctive ou une combinaison reconnaissable.

## Sortie attendue

Pour une proposition musicale exécutable, fournir :

- tonalité + mode et raison ;
- progression en **degrés puis accords** ;
- voicings/inversions ;
- bassline en fonction + notes ;
- mélodie avec contour, rythme et note cible ;
- sections et trajectoire d'énergie ;
- MIDI exact si demandé : note, octave/MIDI number, position, longueur, vélocité ;
- 2 à 4 variantes contrôlées ;
- critères A/B et points `[TEST]`.

Ne jamais prétendre avoir mesuré ou entendu un projet sans accès réel à l'audio ou au Set.

## v11 — Progression / Melody / Voicing Library

When the user asks for playable material, also read:

- `library/transposition-engine.md`
- `library/voicing-engine.md`
- `library/melody-generation-engine.md`
- `library/bassline-generation-engine.md`
- `library/variation-matrix.md`
- the relevant `library/styles/*.md`
- `library/ableton-midi-generation-workflow-v11.md` when Live 12 execution matters
- `library/midi-number-convention.md` for exact pitches

### Exact-MIDI protocol

1. Output **degrees first**, then chord names.
2. State key/mode and harmonic-rhythm assumption.
3. Give voicings as exact MIDI note numbers when requested.
4. Separate bass from upper chord voices.
5. Provide a simple motif before ornamentation.
6. Return controlled variants, not unrelated alternatives.
7. For Ableton, Scale Mode may constrain pitch-aware MIDI Tools [DOC], but generated notes still require musical selection [HEUR].
8. When octave naming could be ambiguous, the MIDI number is authoritative.

The included `.mid` clips are original generic teaching material [HEUR], never transcriptions.
