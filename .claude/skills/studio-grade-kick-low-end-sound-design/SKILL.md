---
name: studio-grade-kick-low-end-sound-design
description: Concevoir, traiter et intégrer des kicks 808/club, sub tails et rumbles pour Minimal House, Tech House, Bass House, Future House et Techno avec Serum 2, Ableton Live 12 et, lorsque pertinent, Waves, FabFilter, iZotope, Native Instruments et Valhalla DSP. Utiliser pour créer un kick de zéro, adapter un kick au style, choisir une chaîne de traitement, résoudre un conflit kick/basse ou préparer un patch contrôlable par macros/bridge.
---

# Studio-Grade Kick & Low-End Sound Design — v8

Ce skill vise un résultat **reproductible, mesurable et musical**, sans prétendre à une affiliation avec un studio, label ou ingénieur particulier.

## À lire avant d'agir

Lire dans cet ordre :
1. `references/source-authority.md`
2. `references/kick-architecture.md`
3. `references/genre-specifications.md`
4. `references/plugin-role-matrix.md`
5. `references/serum2-kick-design.md` ou `references/ableton-kick-design.md` selon le moteur
6. `references/low-end-integration.md`
7. la recette de style dans `recipes/`
8. `references/validation-protocol.md`

Consulter les fichiers marque uniquement lorsqu'un processeur de cette marque est réellement utile. Ne pas empiler des plugins pour « faire professionnel ».

## Système de preuve

- **[DOC]** : fonction/capacité explicitement documentée par le fabricant.
- **[HEUR]** : plage de départ, pratique de studio ou décision artistique. À valider à l'écoute.
- **[TEST]** : dépend de la source audio, du tempo, de la tonalité, du Set, de la version ou de l'interaction réelle kick/basse.

Une valeur chiffrée de recette n'est jamais présentée comme une spécification constructeur.

## Principe directeur

Un kick club moderne peut être décomposé en cinq fonctions :

1. **CLICK/TRANSIENT** — localisation temporelle et lisibilité sur petits haut-parleurs.
2. **PUNCH** — énergie courte du bas-médium / grave supérieur.
3. **BODY** — sensation de masse et caractère.
4. **SUB TAIL** — fondamentale qui décroît après l'attaque.
5. **SPACE/RUMBLE** — uniquement si le style le demande ; de préférence séparé du kick sec.

Chaque couche doit justifier une fonction. Deux couches qui font la même chose doivent être simplifiées ou supprimées.

## Routage du moteur

### Serum 2
Utiliser Serum 2 quand il faut : pitch-drop précis, phase/retrigger contrôlable, layering oscillateur/sample/noise, modulation complexe, macros et rendu très reproductible. Les oscillateurs A/B/C peuvent être Wavetable, Multisample, Sample, Granular ou Spectral [DOC]. Pour un kick synthétique pur, commencer simple : source sinusoïdale/onde simple + enveloppe de pitch + enveloppe d'amplitude ; ajouter seulement ensuite le transient et les harmoniques.

### Ableton Live 12
Utiliser **Operator** pour une architecture synthétique minimale : oscillateur sinusoïdal, enveloppes individuelles et pitch envelope [DOC]. Utiliser **Drum Sampler/Simpler** lorsqu'un one-shot existant est la meilleure source. Utiliser les effets Live seulement pour une fonction clairement définie : EQ, saturation, transient, contrôle de largeur, ducking ou rumble.

## Décision 808 vs kick court

- **Minimal House** : un tail tonal modéré peut participer au groove [HEUR].
- **Tech House** : préférer un kick compact et réserver de l'espace à la bassline [HEUR].
- **Bass House** : priorité au transient/punch ; le sub musical vient souvent d'une basse séparée [HEUR].
- **Future House** : kick court/solide et bassline accordée séparée dans la plupart des arrangements chargés [HEUR].
- **Techno** : kick sec + rumble séparé est généralement plus contrôlable qu'un seul kick extrêmement long [HEUR].

Ne pas « accorder » obsessionnellement les premiers millisecondes du pitch-drop. Si le tail est assez long pour être entendu comme une note, alors sa relation avec la tonalité devient importante [HEUR].

## Ordre de travail obligatoire

1. Définir style, BPM, tonalité et rôle du kick.
2. Décider si le kick porte le sub ou si la basse le porte.
3. Concevoir **amplitude + pitch** avant toute saturation.
4. Ajuster le transient/click à volume modéré.
5. Ajouter les harmoniques nécessaires à la traduction sur petits systèmes.
6. Égaliser uniquement ce qui gêne réellement.
7. Vérifier kick seul, kick+basse, puis mix complet.
8. Tester mono/stéréo et polarité/phase.
9. Faire un A/B à niveau égal avant de conserver un plugin.
10. Rendre/resampler si une chaîne créative devient trop fragile ou trop lourde.

## Politique des plugins tiers

Choisir le **minimum** de processeurs nécessaires. Un exemple de chaîne acceptable :

`Serum 2/Operator → saturation légère → EQ corrective → transient/clip si nécessaire → Utility/mono check`

Une chaîne de six plugins n'est pas meilleure qu'une chaîne de deux. Chaque plugin doit avoir une raison écrite.

### Waves
- **Renaissance Bass** : utiliser pour générer des harmoniques psychoacoustiques qui améliorent la perception du grave sur petits systèmes ; il ne génère pas de sous-harmoniques [DOC].
- **CLA-76** : FET très rapide, utile sur click/punch ou en parallèle pour renforcer l'attaque et la coloration ; éviter d'écraser automatiquement le sub tail [DOC/HEUR].
- **H-Comp** : compression hybride avec caractère analogique ; utile si le kick a besoin de densité ou de mouvement, mais pas obligatoire [DOC/HEUR].
- **J37** : saturation/couleur bande ; favoriser une utilisation légère ou parallèle sur body/upper harmonics [DOC/HEUR].

### FabFilter
- **Pro-Q 4** : correction, dynamique/spectral dynamics et diagnostic fréquentiel [DOC]. Éviter les coupes arbitraires « parce que c'est un kick ».
- **Pro-C 3** : sidechain/ducking et contrôle dynamique ; le panneau sidechain permet de choisir/filtrer le signal de détection [DOC].
- **Saturn 2** : saturation multibande, feedback/dynamics/tone par bande ; garder le sous-grave plus propre que les bandes supérieures lorsque l'objectif est la stabilité [DOC/HEUR]. Activer HQ si l'aliasing devient problématique [DOC].
- **Pro-L 2** : limiteur de sécurité/bus ou print, pas générateur de kick. True Peak et oversampling sont surtout des contrôles de sortie [DOC].

### iZotope
- **Trash** : distorsion + Convolve avec multiband ; excellent pour générer body, grit, click industriel ou rumble texturé [DOC]. Éviter de détruire la bande sub si elle doit rester stable [HEUR].
- **Neutron 5 Transient Shaper** : contrôle attack/sustain par bandes et modes M/S [DOC].
- **Neutron 5 Exciter** : saturation multibande avec types blendables et oversampling [DOC].
- **Neutron 5 Phase** : utiliser comme outil de résolution lorsqu'il existe un problème phase kick/basse, pas comme effet systématique [DOC/HEUR].

### Native Instruments
- **Transient Master** : modifie attack/sustain d'après l'enveloppe plutôt que le niveau absolu ; adapté aux sources percussives [DOC].
- **Supercharger GT** : compression + saturation/caractère ; peut donner du body, de la densité ou une attaque différente [DOC].
- **Massive X** : moteur alternatif de synthèse si demandé ; ne pas le substituer à Serum 2 sans raison [DOC].

### Valhalla DSP
Utiliser les reverbs/delays surtout pour **space, tail, rumble et FX**, généralement sur une piste/send séparé :
- **ValhallaRoom** : espace naturel/room/large ambience, avec Lo Cut disponible [DOC].
- **VintageVerb** : couleurs de reverbs numériques, utile pour tails colorés [DOC].
- **Supermassive** : delays/reverbs à feedback très long, utile pour drones/rumbles/FX, pas par défaut sur le kick direct [DOC].
- **ValhallaDelay** : delay avec diffusion et ducking, utile pour rumble ou répétitions texturées [DOC].

Le low end d'une reverb de rumble doit être contrôlé afin de ne pas masquer le kick sec [HEUR].

## Intégration kick/basse

Le skill doit explicitement choisir l'un de ces modèles :

- **A — Kick owns sub** : kick plus long, basse coupée/duckée davantage dans le sous-grave.
- **B — Bass owns sub** : kick plus court, sub/bassline porte la fondamentale principale.
- **C — Alternating ownership** : kick et basse occupent le même registre à des instants différents grâce au groove/ducking.
- **D — Techno kick + rumble** : kick sec central + rumble séparé et filtré.

Pour tout sidechain : mesurer la récupération en contexte et ne pas caler le release uniquement à une formule. Une division du beat peut servir de point de départ [HEUR], l'écoute décide [TEST].

## Exigences de sortie

Toute réponse utilisant ce skill doit fournir :
- style + rôle choisi ;
- architecture `CLICK/PUNCH/BODY/SUB/SPACE` ;
- moteur Serum 2 ou Ableton et justification ;
- paramètres de départ marqués [HEUR] ;
- chaîne de traitement avec **raison de chaque plugin** ;
- stratégie kick/basse ;
- 3 tests minimum : solo, kick+basse, mix/mono ;
- ce qui doit être mesuré ou testé sur le vrai projet [TEST].

Ne jamais déclarer un kick « pro », « parfait » ou « master-ready » sans écoute du rendu dans le morceau.
