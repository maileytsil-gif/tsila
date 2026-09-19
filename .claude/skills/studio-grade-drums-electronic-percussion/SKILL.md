---
name: studio-grade-drums-electronic-percussion
description: Conception, programmation, traitement et intégration de drums et percussions électroniques pour Minimal House, Tech House, Bass House, Future House, Electro et Techno. Couvre clap/snare, hats, shakers, rides, toms, rims, claves, FM/metallic percussion, zaps/lasers/bleeps, glitch/micro-percussion, tuned percussion, noise percussion, fills et kits hybrides avec Ableton Live 12, Serum 2 et traitements Waves/FabFilter/iZotope/Native Instruments/Valhalla. Utiliser pour créer ou réviser le groove hors kick principal; déléguer le kick/sub au skill kick-low-end.
---

# Studio-Grade Drums & Electronic Percussion — v13

Ce skill traite la batterie comme un **système de rôles rythmiques et timbraux**, pas comme une collection de samples. Il couvre les drums traditionnels électroniques et la **percussion électronique synthétique**.

## Hiérarchie des preuves

- `[DOC]` capacité explicitement documentée par le constructeur.
- `[ANALYSIS]` conclusion de conception tirée de ces capacités et du contexte musical.
- `[HEUR]` point de départ de production, jamais présenté comme une valeur officielle.
- `[TEST]` doit être vérifié dans le Set réel, à niveau égal et dans le contexte du morceau.

## Périmètre

### Drums / percussion standard
- clap / snare / rim / clave ;
- closed/open hats ;
- shaker / tambourine-like ;
- ride / crash / cymbal ;
- toms / electro-toms ;
- fills / rolls / ghost hits ;
- drum bus et room/ambience.

### Percussion électronique
- FM metallic hits ;
- clangs / resonant pings ;
- zaps / lasers / bleeps ;
- clicks / ticks / micro-percussion ;
- glitch / stutter / digital debris ;
- tuned percussion ;
- noise bursts / synthetic shakers ;
- hybrid sample+synth hits ;
- granular/spectral fragments lorsque Serum 2 le justifie.

## Séparation avec les autres skills

- Le **kick principal**, 808, sub-tail et rumble relèvent de `studio-grade-kick-low-end-sound-design`.
- La basse relève de `studio-grade-bass-sound-design`.
- Les impacts/risers cinématiques généraux peuvent relever de `bass-house-serum2-sound-design`.
- Ce skill peut utiliser un mini-kick/tom/percussion tonal comme élément secondaire, mais ne redéfinit pas le low-end ownership du projet.

## Architecture de décision obligatoire

Avant de choisir un synthé ou un plugin, définir pour chaque son :

`ROLE → SLOT → SOURCE → ENVELOPE → SPECTRUM → MOTION → SPACE → VARIATION`.

### ROLE
- `BACKBONE`: clap/snare/hat principal qui explique le groove.
- `TIMEKEEPER`: hat/shaker/ride qui rend le tempo lisible.
- `SYNCOPATION`: percussion qui crée le bounce entre les temps.
- `ACCENT`: hit court qui marque une phrase.
- `MOTION`: élément répétitif/modulé qui anime le pattern.
- `FILL`: événement ponctuel en fin de phrase.
- `EAR-CANDY`: événement rare et distinctif.

### SLOT
Décrire le placement en grille musicale, pas seulement en millisecondes : 1/4, offbeat 1/8, 1/16, ghost, triplet, anticipation, fin de mesure.

## Sources recommandées

### Ableton Live 12
`[DOC]` Drum Sampler est conçu pour les one-shots et fournit start/length, enveloppe AHD, pitch, filtre, modulation et effets de playback. Les Drum Synths/Max for Live couvrent DS Clap, Cymbal, FM, HH, Snare, Tom, etc. Operator, Collision, Wavetable, Meld et Simpler/Sampler peuvent être utilisés lorsque leur moteur correspond mieux au son.

Lire `references/ableton-drum-synthesis.md`.

### Serum 2
`[DOC]` OSC A/B/C peuvent fonctionner en Wavetable, Multisample, Sample, Granular ou Spectral. Le NOISE oscillator est un lecteur de sample stéréo et peut aussi servir de modulateur. Le routing permet Main/Direct/Filter/None et les bus.

Utiliser Serum 2 quand la percussion dépend réellement de modulation, FM/warp, wavetable, granular/spectral, routing ou macros complexes — pas pour remplacer un one-shot simple sans raison.

Lire `references/serum2-electronic-percussion.md`.

## Choix rapide par famille

| Son | Source de départ recommandée | Alternative |
|---|---|---|
| clap électronique | DS Clap / Drum Sampler | Serum noise+impulse |
| snare | DS Snare / Drum Sampler | Serum body+noise |
| hats | DS HH / Drum Sampler | Serum noise / metallic partials |
| cymbal/ride | DS Cymbal | Serum metallic/noise |
| tom | DS Tom / Operator | Serum sine/triangle pitch env |
| rim/clave | Drum Sampler / DS Clang | Operator/Collision |
| FM metallic | DS FM / Operator | Serum FM/warp |
| zap/laser | Operator / Serum | Wavetable/Meld |
| bleep | Operator / Collision | Serum |
| glitch | resample + Drum Sampler | Serum Sample/Granular |
| tuned percussion | Collision / Operator | Serum / sample layer |
| synthetic shaker | filtered noise | sample+noise hybrid |

## Layering

Un layer doit remplir une fonction distincte. Architecture maximale courante :

`TRANSIENT + BODY + TEXTURE + TAIL`.

Ne pas empiler quatre claps complets. Exemples :
- transient très court mono ;
- body principal ;
- texture bruitée filtrée ;
- tail/room séparé.

Aligner phase/polarité et timing à l'oreille et en mono. Si le layer affaiblit le son à niveau égal, le supprimer.

## Percussion électronique — règles de synthèse

### FM / metallic
Utiliser rapports non triviaux, enveloppes courtes et decay contrôlé. Le caractère vient de l'inharmonicité et du mouvement spectral, pas du volume.

### Zap / laser
Pitch envelope très rapide + corps sine/triangle/FM. Le point de départ et la profondeur sont `[HEUR]`; vérifier que le sweep ne concurrence pas le kick ou la basse.

### Click / micro-percussion
Événement de quelques dizaines de millisecondes, souvent high-passed ou band-limited. Le placement rythmique compte plus que la largeur stéréo.

### Glitch
Créer d'abord une source identifiable, puis resampler / couper / inverser / réordonner. Une texture aléatoire permanente n'est pas automatiquement un groove.

### Tuned percussion
Tuner la partie soutenue/tonale, pas nécessairement le bruit initial. Utiliser la gamme ou un degré de tension défini par le skill théorie.

## Traitements tiers — doctrine

Les plugins sont des **outils fonctionnels**, jamais une checklist de marques.

- Waves Smack Attack : attack/sustain des sons percussifs.
- FabFilter Pro-Q 4 : correction/dynamique spectrale ciblée ; Saturn 2 : harmoniques/distorsion multibande ; Pro-C 3 : contrôle dynamique/ducking lorsque nécessaire.
- iZotope Neutron : Transient Shaper, Exciter et outils de sculpture lorsque le problème est précisément celui-ci.
- Native Instruments Transient Master : attaque/sustain rapide ; Battery 4 : sampling, cellules, bus et sound design de kit.
- ValhallaRoom/VintageVerb : rooms/plates/tails ; ValhallaDelay : échos, pitch/reverse/diffusion pour percussion créative.
- Ableton Drum Buss/Saturator/Roar/Auto Filter/EQ Eight/Utility : préférer les outils natifs quand ils résolvent le problème sans complexité supplémentaire.

Lire `references/plugin-role-matrix.md`.

## Groove

Construire d'abord un pattern **sec**. Ajouter ensuite vélocité, microtiming, probabilités/variations et timbre. Le swing ne doit pas être appliqué uniformément au kick, sub et à toutes les percussions.

Pour les styles ciblés, lire `references/style-specifications.md` et les recettes `recipes/*-kit.md`.

## Macros bridge

Exposer de préférence :

- `ATTACK`
- `TONE`
- `DECAY`
- `NOISE`
- `METAL`
- `TUNE`
- `WIDTH`
- `SPACE`
- `MOTION`
- `VARIATION`

Le bridge doit résoudre les paramètres réellement exposés dans Live avant toute écriture.

## Workflow complet

1. Définir rôle et slot de chaque élément.
2. Construire groove avec sons simples.
3. Choisir synthèse ou sample selon la fonction.
4. Designer l'enveloppe avant les effets.
5. Nettoyer overlap et tails inutiles.
6. Ajouter coloration/texture si nécessaire.
7. Ajouter espace sur send ou layer dédié.
8. Créer 2–4 variations mesurées, pas du random continu.
9. Tester mono, faible volume, sans bus processing.
10. Activer bus processing à niveau égal.
11. Tester avec kick/bass/vocal/hook présents.
12. Resampler seulement quand il apporte un gain créatif/CPU/workflow.

## Sortie standard

Pour chaque son ou kit :

1. `Role`
2. `Pattern / Slot`
3. `Engine`
4. `Synthesis / Sample settings`
5. `Envelope`
6. `Pitch/Tuning`
7. `Layering`
8. `Processing chain` avec fonction de chaque plugin
9. `Stereo/Space`
10. `Variation plan`
11. `Bridge macros`
12. `Validation tests`
13. `Evidence tags`

Lire `references/output-schema.md`.

## Interdictions

- ne pas empiler plusieurs transient shapers sans justification ;
- ne pas élargir le bas d'un tom/percussion grave sans test mono ;
- ne pas mettre une grande reverb directement sur tous les hats ;
- ne pas saturer le bus pour compenser un mauvais pattern ;
- ne pas quantifier toutes les micro-percussions de la même façon ;
- ne pas tuner chaque bruit non tonal artificiellement ;
- ne pas inventer qu'un réglage `[HEUR]` vient du constructeur.
