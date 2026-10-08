# Famille — Impact

## Fonction
Événement de transition à énergie initiale forte. Un impact peut combiner transient, corps grave, couche médium/metal/noise et queue spatiale.

## Serum 2
- [DOC] Le moteur **Sample** permet de déclencher et transformer un one-shot ; Sample/Granular/Spectral peuvent fonctionner sans pitch tracking pour les sons percussifs/impacts.
- [DOC] Les sources peuvent être routées séparément vers filtres/Main/Direct/bus, utile pour garder une couche de transient plus sèche qu'une queue.
- [HEUR] Une couche sub synthétique doit rester simple et courte si elle accompagne déjà un kick.

## Ableton Live 12
- [DOC] **Drum Sampler** est conçu pour les one-shots et possède AHD, pitch, filtre et neuf playback effects dont Pitch Env, Punch, FM, Ring Mod, Sub Osc et Noise.
- [DOC] **Simpler One-Shot** est adapté aux impacts audio.
- [DOC] **Corpus** peut ajouter une résonance physique ; son niveau peut devenir important, donc contrôler le gain.
- [DOC] **Hybrid Reverb/Reverb** fournissent la queue spatiale ; **Roar** peut ajouter harmonique/densité.

## Construction par couches [HEUR]
- `TRANSIENT` : clic/crack très court.
- `BODY` : 80–300 ms, tonal ou bruité.
- `LOW` : éventuelle chute sub/pitch très contrôlée.
- `TAIL` : reverb, reverse, texture ou debris.
Ne pas exiger les quatre couches : supprimer toute couche qui n'apporte pas une fonction audible.

## Macros
`HIT`, `BODY`, `LOW`, `METAL`, `TAIL`, `SIZE`, `DISTORT`.

## Validation
Comparer dans le contexte du kick suivant. Contrôler le pic, le sub, la phase et la longueur de queue. Tester à faible volume : l'impact doit rester perceptible sans dépendre uniquement d'un énorme grave.

## Sous-types v5
Consulter `../subtypes/impact-subtypes.md` avant de construire une recette détaillée. Utiliser `../subtype-selection-matrix.md`, `../professional-layering.md`, `../macro-templates-v5.md` et `../subtype-validation.md` pour la sélection, le layering, les macros et la validation.
