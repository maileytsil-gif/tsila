# Famille — Stab

## Fonction
Accent tonal court, souvent accord ou intervalle, utilisé pour marquer le groove. Un stab doit avoir une identité immédiate : attaque claire, corps bref, queue contrôlée.

## Serum 2
- [DOC] Wavetable/Multisample/Sample sont tous disponibles dans OSC A/B/C ; Sample est particulièrement pratique si le stab part d'un one-shot.
- [DOC] Les filtres et le routage permettent de traiter différemment plusieurs couches.
- [HEUR] Pour un stab synthétique : onde riche + enveloppe d'amplitude courte + enveloppe de filtre encore plus courte ou similaire.

## Ableton Live 12
- [DOC] **Drift/Analog** : architectures soustractives directes pour stabs synthétiques.
- [DOC] **Wavetable** : si le stab doit contenir un mouvement timbral rapide.
- [DOC] **Simpler One-Shot** : lecture monophonique de one-shots ; Trigger permet de laisser jouer le sample indépendamment de la durée de note.
- [DOC] **Sampler** : utile si plusieurs zones/velocities doivent être mappées.

## Profil [HEUR]
- Attack 0–20 ms selon le clic souhaité.
- Decay court à moyen, sustain faible/0 pour un vrai stab ; release court à moyen pour éviter les queues incontrôlées.
- Pour un stab d'accord, ne pas multiplier automatiquement les voix d'unison : l'accord lui-même apporte déjà de la densité.
- Une courte room/plate ou delay peut donner une signature sans détruire le groove.

## Macros
`BITE`, `DECAY`, `TONE`, `CHORD COLOR`, `WIDTH`, `SPACE`.

## Validation
Tester sur croches/contretemps et dans le groove complet. Vérifier que la queue ne chevauche pas le kick suivant et que l'accord reste lisible en mono.

## Sous-types v5
Consulter `../subtypes/stab-subtypes.md` avant de construire une recette détaillée. Utiliser `../subtype-selection-matrix.md`, `../professional-layering.md`, `../macro-templates-v5.md` et `../subtype-validation.md` pour la sélection, le layering, les macros et la validation.
