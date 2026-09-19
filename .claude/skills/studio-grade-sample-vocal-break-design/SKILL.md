---
name: studio-grade-sample-vocal-break-design
description: Design et transformation de samples, time-stretching, slicing, vocal shots, vocal chops, resampling, break FX et transitions pour Pop/Electro/Minimal House/Tech House/Bass House/Future House/Techno. Utilise Ableton Live 12, Serum 2 et, quand leur fonction est justifiée, Waves, FabFilter, iZotope, Native Instruments et Valhalla. Sépare strictement [DOC], [ANALYSIS], [HEUR] et [TEST].
---

# Sample / Time-Stretch / Vocal Shot / Break Design — v14

Ce skill transforme un sample en **fonction musicale**. Il ne traite jamais le sample comme une décoration arbitraire : chaque découpe, stretch, reverse, pitch, formant, delay, reverb ou stutter doit servir une intention d'arrangement.

## Hiérarchie de preuve

- `[DOC]` comportement confirmé par documentation constructeur.
- `[ANALYSIS]` conclusion issue de l'analyse d'un morceau/projet.
- `[HEUR]` règle de travail ou point de départ de production.
- `[TEST]` décision qui doit être validée dans le vrai Set.

## Intake minimum

Déterminer :
- type de source : vocal shot / phrase vocale / loop drum / texture / FX / instrument / full-mix ;
- BPM source si connu ;
- tonalité/note si tonale ;
- fonction : hook / pickup / break anchor / transition / texture / fill / ambience / impact ;
- section : intro / break / build / drop / outro ;
- durée cible ;
- niveau d'intelligibilité voulu : clair / stylisé / abstrait ;
- degré de transformation : subtil / moyen / extrême ;
- droits/licence de la source si elle n'est pas créée par l'utilisateur.

## Pipeline obligatoire

### 1. Source triage

Classer le sample :
`RHYTHMIC`, `MONOPHONIC_TONAL`, `POLYPHONIC/FULL-MIX`, `TEXTURE/NOISE`, `ONE-SHOT`, `SPOKEN/VOCAL`.

Lire `references/sample-selection-and-prep.md`.

### 2. Warp / stretch decision

Ne pas activer Warp par réflexe.
- one-shot sans besoin de synchro : Warp off est souvent la solution la plus propre `[DOC+HEUR]` ;
- drum loop : Beats est la première option à tester `[DOC]` ;
- vocal/mono tonal : Tones est conçu pour les sources à hauteur claire `[DOC]` ;
- texture/noise : Texture `[DOC]` ;
- effet vitesse/platine : Re-Pitch `[DOC]` ;
- source complexe/polyphonique : Complex / Complex Pro `[DOC]` ;
- forte transposition vocale : tester Complex Pro et son contrôle Formants `[DOC+TEST]`.

Toujours A/B au tempo final. Lire `references/ableton-warp-and-stretch.md`.

### 3. Edit before FX

Avant tout plugin :
1. start/end ;
2. fades ;
3. warp markers ;
4. timing ;
5. pitch/transposition ;
6. gain ;
7. reverse/crop si nécessaire ;
8. slicing si la source contient plusieurs événements.

### 4. Choose engine

- **Audio Clip** : édition directe, warping, clip envelopes, reverse, timing précis.
- **Simpler One-Shot** : vocal shot ou phrase courte déclenchable.
- **Simpler Slicing** : chops, breakbeats, rearrangement de transients ; jusqu'à 64 slices automatiques `[DOC]`.
- **Serum 2 Sample** : playback, loop, slicing, Rate/tape-stop et transformation par modulation `[DOC]`.
- **Serum 2 Granular** : étirement/texturation, scan manuel, grains et boucles `[DOC]`.
- **Serum 2 Spectral** : resynthèse et séparation créative du comportement temps/pitch `[DOC]`.
- **Maschine / Kontakt / Guitar Rig** : choisir uniquement si une fonction spécifique est utile (stretch indépendant, formant correction, granular buffer, etc.).

### 5. Vocal shot design

Lire `references/vocal-shot-design.md`.

Un vocal shot dans un break doit jouer l'un de ces rôles :
`ANCHOR`, `PICKUP`, `ANSWER`, `MOTIF`, `TENSION_MARKER`, `TEXTURE`, `PAYOFF_CUE`.

Ne pas empiler plusieurs shots qui disent tous la même chose. En général, un break gagne à avoir **un motif vocal reconnaissable + une variation de fin de phrase** plutôt qu'une suite de chops aléatoires `[HEUR]`.

### 6. Break architecture

Lire `references/break-architecture.md`.

Construire un break en couches :
`FOCUS → SPACE → MOTION → LIFT → PRE-DROP VACUUM`.

- FOCUS : vocal shot, topline, motif ou texture dominante.
- SPACE : reverb/delay contrôlés.
- MOTION : filtre, pitch, grain, pan, stutter ou automation.
- LIFT : densité/registre/tension augmentent vers le build.
- VACUUM : retirer du bas et/ou des tails juste avant le retour du drop.

### 7. Creative FX selection

Lire `references/creative-fx-matrix.md` et `references/third-party-tools.md`.

Règle : **un effet = une fonction**. Exemple :
- Vocal Bender : pitch/formant créatif ;
- Timeless 3 : delay, pitch feedback, freeze, lo-fi/diffusion ;
- Volcano 3 : filtre modulé ;
- Stutter Edit 2 : buffer/stutter/gestures de transition ;
- ValhallaDelay : pitch/reverse/duck delay ;
- Supermassive : longues queues ou espaces extrêmes ;
- Guitar Rig Transpose Stretch / Grain Delay : stretch granular, freeze, reverse et pitch ;
- Ableton Beat Repeat / Grain Delay / Echo / Hybrid Reverb / Vocoder : solutions natives.

Ne pas charger un plugin tiers si l'effet natif fait déjà le travail avec moins de complexité.

### 8. Resample checkpoint

Après transformation importante :
- imprimer une version audio ;
- conserver la source dry ;
- nommer BPM/key/fonction ;
- recouper le rendu ;
- poursuivre le traitement à partir du resample seulement si cela simplifie réellement le flux.

Lire `references/resampling-workflow.md`.

### 9. Validation

Obligatoire :
- timing au tempo final ;
- phase/mono si couche large ;
- intelligibilité du vocal si nécessaire ;
- absence de clicks aux edits ;
- tails propres avant le drop ;
- pitch en accord avec le morceau lorsque le shot est tonal ;
- comparaison dry/processed level-matchée ;
- écouter le break sans regarder l'écran.

## Sortie standard

Toujours fournir :
1. `Source Role`
2. `Warp/Stretch Choice`
3. `Edit Plan`
4. `Engine Choice`
5. `Pitch/Formant Plan`
6. `FX Chain with Reasons`
7. `Automation/Performance Plan`
8. `Resample Point`
9. `Break Placement`
10. `Validation Tests`

## Interdictions

- Ne pas prétendre qu'un warp mode est universellement « meilleur ».
- Ne pas préserver les formants si le but est précisément de créer une voix non naturelle.
- Ne pas faire durer une reverb au-dessus du downbeat du drop sans raison musicale.
- Ne pas quantifier un vocal humain au point de supprimer toute intention si le groove fonctionne déjà.
- Ne pas transformer un sample protégé en prétendant que l'édition annule les droits d'auteur.
