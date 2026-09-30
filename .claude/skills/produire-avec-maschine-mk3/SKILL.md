---
name: produire-avec-maschine-mk3
description: Concevoir grooves, kits, samples, patterns, scènes et performances sur contrôleur Maschine MK3 et logiciel Maschine 3, puis intégrer MIDI et audio dans Ableton Live 12. Utiliser pour Beatmaking Bass House, Future House, électro/R&B, DnB/Jungle, routage multi-sorties, Perform FX, variations et collaboration avec Serum 2 dans les projets VIBRAAXIS, VIBRAVECTOR ou VIBRAMOTIVE. Utiliser quand l'utilisateur travaille avec Maschine (demande explicite ou son d'une expansion NI) ; sinon producteur-rythmique programme dans Live.
---

# Produire avec Maschine MK3

Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

## Cadrer le projet

Identifier la version effective de Maschine 3, du contrôleur MK3, de Live 12, du plugin VST3/AU, du Mac et des sorties audio. Vérifier les fonctions dans l'installation réelle avant d'agir. Choisir avec l'utilisateur au moins une référence musicale correspondant au style; relever groove, densité, palette, évolution et placement du kick, sans copier mélodie, sample ou enregistrement. Indiquer si VIBRAAXIS, VIBRAVECTOR ou VIBRAMOTIVE est visé. Ici : Maschine 3.6.0 (VST3/AU repérés le 14 sept. 2026), aucune API : contrôle d'écran au premier plan (`request_full_control`), capture après chaque geste, gestes matériels faits par l'utilisateur (`../native-instruments-control/SKILL.md`).

Lire [references/production.md](references/production.md) pour le jeu, les patterns et le sampling, et [references/routage.md](references/routage.md) pour l'intégration Live et la décision Perform FX. Appeler `composer-hooks-funk-electro` et `theorie-musicale-electronique` (hook, théorie), `sound-designer-serum` (Serum 2), `kick-bass-equilibre` (grave), `ingenieur-mixage` (mix) ; `produire-demo-electro-rapide` structure les étapes, `produire-morceau-electronique-de-a-a-z` prend le relais après la démo.

## Construire le groove

Créer des Groups lisibles : batterie principale, percussions, chops/texture et FX. Nommer chaque Sound et vérifier la source des samples. Créer trois Patterns de 4 à 8 mesures avec différentes densités, accents et silences. Jouer les accents aux pads; corriger le timing intentionnellement. Pas d'humanisation aléatoire (`../producteur-rythmique/SKILL.md` §3) : vélocités en motif répété, micro-décalage par couche ; Variation/Humanize seulement à la demande de l'utilisateur, résultat relu puis figé ; kick et sub stables. Faire comparer les trois grooves à la référence à niveau comparable, puis faire choisir l'utilisateur à l'écoute.

Développer des Scenes intro, drop, break et variante; organiser les Sections en Song view ou transférer les pistes vers Live. Prévoir dès le départ **Original Mix** et **Extended Mix** : patterns d'intro/outro DJ disponibles sans affaiblir la version courte. Les répétitions de Pattern peuvent référencer la même source : rendre unique ou utiliser un Clip pour un fill local lorsque nécessaire.

Dans chaque drop, préparer une variation de drum en fin de chaque phrase de 8 mesures. Créer des Patterns ou Clips locaux pour fills de snare/tom, retrait de kick, hats, reverse cymbal et impact; alterner les combinaisons selon la tension. Si un Pattern est partagé, rendre le fill unique pour qu'il ne se répète pas involontairement. Faire écouter à l'utilisateur l'arrivée du temps 1 suivant avec le kick et le sub.

## Concevoir les sons et les basses

Employer Maschine pour pads, groove, sampling, slicing, chops, resampling et jeu en direct. Concevoir par défaut kick, sub, basse médium et synthés dans Serum 2 selon le skill de sound design; conserver sub et basse médium dans deux instruments distincts. Serum peut être chargé dans Maschine si l'édition, le rappel et le routage sont réellement vérifiés. Dans le workflow Ableton, privilégier deux pistes Serum séparées pour les basses afin de préserver édition, sidechain et contrôle mono. Kick : soit piste Serum 2 dans Live (sidechain et mono contrôlés, sans Perform FX Maschine), soit Sound Maschine (Perform FX possible par le Master) ; choisir, le noter dans `projet-<nom>.md`, ne jamais jouer les deux.

## Choisir le chemin audio avant les effets

Respecter la contrainte de cette installation : un Sound/Group envoyé directement à une sortie externe de Maschine ne profite pas du Perform FX placé sur le Master principal. Pour chaque élément, choisir explicitement :

- **Perform FX voulu** : router par le Master principal de Maschine, enregistrer ou exporter la performance, puis travailler l'audio imprimé dans Live si une piste séparée est nécessaire.
- **Sortie individuelle voulue** : router vers une sortie externe dédiée du plugin (Ext. 2 à 16 ; Ext. 1 est la sortie par défaut du Master), traiter dans Live par plug-ins tiers (règle 6 de `../ableton-live-session/SKILL.md`), piste `AUDIO - <SON>` → `BUS - BATTERIE`, sans compter sur le Perform FX du Master.

Ne pas additionner le retour Master et une sortie externe du même signal. L'utilisateur joue la Smart Strip (geste matériel) ; Claude vérifie le chemin par `lom.py meters` sur les pistes Live concernées (chiffres relatifs : seule la piste prévue bouge) et par capture de la page de routage de Maschine. Distinguer un Perform FX inséré ailleurs du Perform FX Master; toute autre configuration exige un test réel avant d'être promise. Garder une prise dry si le retour arrière est important.

## Transférer vers Live et vérifier

Choisir par élément MIDI éditable, audio rendu, sortie multi-out ou performance imprimée. Sauver le projet Maschine avec samples sous un nouveau nom et le Set par « Sauver Set Live sous… » ; une étape par échange ; « Sauver Set Live » et `../memoire-projet/scripts/journal.sh` après chaque étape validée ; documenter BPM, longueur, origine mesure 1, canal, sortie et éventuels effets imprimés. Vérifier alignement des transitoires, latence, phase kick/sub (`../kick-bass-equilibre/SKILL.md`, `kick_bass_check.py`), sommation mono, niveaux et rappel à la réouverture. Ne pas annoncer un .mxprj, .als, stem ou une écoute comme testé sans l'avoir ouvert et contrôlé. Ouvrir par `lom.py ping` puis `lom.py state --json` ; aucune fonction VST ou de routage n'est présumée.

## Livrer

Fournir référence validée, kit/Groups/Sounds, trois variantes et motif retenu, Scenes/Sections pour Original Mix et Extended Mix, tableau des sorties et de Perform FX, clips MIDI/audio réellement créés, instructions de rappel et trois corrections prioritaires. Vérifier séparément les deux exports et les performances FX imprimées. Qualifier le résultat de démo tant que les exports entiers n'ont pas été écoutés et vérifiés.

## Dans ce workflow

Pilotage par écran, sans API : `../native-instruments-control/SKILL.md` + `../native-instruments-control/references/maschine.md` · groove sans aléatoire : `../producteur-rythmique/SKILL.md` · chargement anti hot-swap, règle 6, sauvegarde : `../ableton-live-session/SKILL.md` · prise wet Perform FX : `../resampling/SKILL.md` · phase kick/sub : `../kick-bass-equilibre/SKILL.md` · étude sampling Maschine 3 : `../produire-morceau-electronique-de-a-a-z/references/Etude_sampling_Maschine3_Ableton12_Serum2.md`.
