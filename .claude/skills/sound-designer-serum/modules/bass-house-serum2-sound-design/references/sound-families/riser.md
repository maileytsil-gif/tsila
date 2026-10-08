# Famille — Riser

## Fonction
Effet de transition dont l'énergie perçue augmente vers un point d'arrivée. La montée peut venir de la hauteur, du filtre, de la densité, de la largeur, du bruit, du rythme, de la reverb ou de plusieurs axes combinés.

## Serum 2
- [DOC] Xfer cite explicitement les risers/sweeps parmi les usages où le pitch tracking peut être désactivé.
- [DOC] Wavetable, Sample, Granular et Spectral permettent différentes formes de montée ; le moteur Sample possède des fonctions de lecture/loop/rate utiles pour transformer un matériau audio.
- [DOC] Granular permet d'étirer et modifier le matériau en temps réel.
- [HEUR] Utiliser une enveloppe one-shot ou une automation DAW pour la trajectoire principale ; garder un LFO séparé pour les pulsations secondaires.

## Ableton Live 12
- [DOC] **Drift** possède un Cycling Envelope et des formes LFO dont Saw Up, Linear Envelope et Exponential Envelope, utiles pour des montées contrôlées.
- [DOC] **Granulator III** peut produire textures montantes à partir d'un sample.
- [DOC] **Auto Filter** possède LFO/envelope follower et filtres multiples.
- [DOC] **Echo** possède modulation, feedback et reverb intégrée ; utile pour augmenter la densité.
- [DOC] **Roar** offre saturation/routages et matrice de modulation pour une intensification progressive.

## Profil de conception [HEUR]
Construire 2 à 4 axes indépendants :
1. hauteur ou registre ;
2. ouverture spectrale ;
3. densité/feedback/distorsion ;
4. largeur/espace.
Ne pas faire monter tous les paramètres linéairement : une courbe accélérée en fin de build crée souvent plus de tension.

## Macros
`RISE`, `TENSION`, `BRIGHTNESS`, `DENSITY`, `WIDTH`, `SPACE`, `PULSE`.

## Validation
Tester sur 1, 2, 4, 8 et 16 mesures. Le dernier quart doit fonctionner sans clipper. Couper le riser exactement à l'impact et comparer avec une version qui laisse une queue : choisir selon l'arrangement, pas par habitude.

## Sous-types v5
Consulter `../subtypes/riser-subtypes.md` avant de construire une recette détaillée. Utiliser `../subtype-selection-matrix.md`, `../professional-layering.md`, `../macro-templates-v5.md` et `../subtype-validation.md` pour la sélection, le layering, les macros et la validation.
