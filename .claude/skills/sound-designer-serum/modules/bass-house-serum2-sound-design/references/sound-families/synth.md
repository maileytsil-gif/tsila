# Famille — Synthé mélodique / tonal

## Fonction
Son synthétique principal ou secondaire, joué comme instrument tonal. Il peut être monophonique ou polyphonique. Le but n'est pas d'imposer une esthétique de lead : il faut d'abord déterminer registre, densité harmonique, articulation et mouvement.

## Moteurs recommandés

### Serum 2
- [DOC] **Wavetable** : adapté quand le mouvement de timbre vient du balayage/morphing de table d'ondes.
- [DOC] **Multisample** : utile pour un synthé hybride dont une partie du caractère vient d'enregistrements multi-échantillonnés.
- [DOC] **Granular / Spectral** : à réserver à une composante texturale ou évolutive lorsque la transformation du matériau audio est centrale.
- [HEUR] Pour un synthé clair et contrôlable, commencer avec un seul moteur principal et ajouter une deuxième couche seulement si elle apporte une fonction différente.

### Ableton Live 12
- [DOC] **Drift** : synthèse soustractive, deux oscillateurs + bruit, filtre, enveloppes, LFO et modulation ; excellent point de départ simple.
- [DOC] **Wavetable** : deux oscillateurs wavetable, deux filtres et modulation ; choix logique pour un timbre spectralement mobile.
- [DOC] **Meld** : deux moteurs indépendants avec filtres, LFO et matrice ; utile pour un son bi-timbral/hybride.
- [DOC] **Operator** : quatre oscillateurs et FM/additif/soustractif ; utile si la relation harmonique/FM définit le timbre.

## Profil de conception [HEUR]
1. Définir une articulation : attaque nette ou souple, sustain stable ou décroissant.
2. Choisir une source suffisamment riche pour le rôle sans ajouter d'unison par réflexe.
3. Utiliser une enveloppe de filtre ou de timbre pour donner une trajectoire à la note.
4. Réserver les LFO aux mouvements répétés ; réserver les enveloppes aux gestes déclenchés par note.
5. Ajouter largeur et espace après validation du timbre en mono/sec.

## Macros suggérées [HEUR]
`TONE`, `MOTION`, `ATTACK`, `WIDTH`, `SPACE`, `EDGE`.

## Validation
- Jouer note courte, note tenue, intervalle d'octave et accord si polyphonique.
- Vérifier que la modulation ne rend pas les notes graves et aiguës incohérentes.
- [TEST] Si contrôle par bridge : découvrir les paramètres réellement exposés par Live avant de mapper les macros.

## Sous-types v5
Consulter `../subtypes/synth-subtypes.md` avant de construire une recette détaillée. Utiliser `../subtype-selection-matrix.md`, `../professional-layering.md`, `../macro-templates-v5.md` et `../subtype-validation.md` pour la sélection, le layering, les macros et la validation.
