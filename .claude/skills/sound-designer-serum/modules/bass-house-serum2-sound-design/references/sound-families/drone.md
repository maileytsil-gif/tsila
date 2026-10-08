# Famille — Drone

## Fonction
Son soutenu sur une hauteur fixe ou quasi fixe, ou texture continue non nécessairement jouée comme un instrument traditionnel. Le mouvement interne compte plus que la succession de notes.

## Serum 2
- [DOC] **Pitch Tracking peut être désactivé**. Xfer cite explicitement les drones, sons statiques, effets de bruit, risers et impacts comme cas d'usage.
- [DOC] Quand le pitch tracking est désactivé, Sample/Granular/Spectral jouent C3 (MIDI 60) tandis que Wavetable joue C-2 (MIDI 0), donc ne jamais supposer un comportement identique entre moteurs.
- [DOC] Granular convient à des soundscapes complexes et évolutifs ; Spectral permet des transformations de temps/fréquence.
- [HEUR] Pour un drone tonal, garder au moins une référence de hauteur claire ; pour un drone de texture, désactiver le tracking peut éviter des changements indésirables.

## Ableton Live 12
- [DOC] **Granulator III Cloud** est explicitement destiné aux drones et textures expérimentales.
- [DOC] **Wavetable/Meld** permettent des modulations lentes et poly/mono selon le besoin.
- [HEUR] Un Rack peut réunir une fondamentale stable, une texture granulaire et une queue spatiale avec macros communes.

## Profil de conception [HEUR]
- Sustain très long ou continu ; éviter un transient trop marqué sauf intention.
- Mouvement lent sur timbre, pan, largeur ou densité plutôt que sur le niveau global uniquement.
- Introduire de petites dérives indépendantes plutôt qu'un seul LFO parfaitement cyclique.
- Garder une limite de niveau stricte : les résonances longues peuvent s'accumuler.

## Macros
`TENSION`, `MOTION`, `DENSITY`, `TONE`, `WIDTH`, `SPACE`, `NOISE`.

## Validation
Tenir 16–32 mesures. Chercher accumulation de fréquences, battements indésirables, dérive de niveau et fatigue. [TEST] Vérifier que les modulations/paramètres choisis sont exposés si le drone doit être piloté par bridge.

## Sous-types v5
Consulter `../subtypes/drone-subtypes.md` avant de construire une recette détaillée. Utiliser `../subtype-selection-matrix.md`, `../professional-layering.md`, `../macro-templates-v5.md` et `../subtype-validation.md` pour la sélection, le layering, les macros et la validation.
