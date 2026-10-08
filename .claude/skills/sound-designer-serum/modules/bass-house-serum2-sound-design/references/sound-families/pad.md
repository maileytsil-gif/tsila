# Famille — Pad

## Fonction
Instrument harmonique polyphonique destiné à soutenir des accords avec attaque et relâchement plutôt souples. Contrairement à la nappe, le pad doit généralement rester jouable et lisible comme instrument harmonique.

## Serum 2
- [DOC] Wavetable permet un timbre évolutif ; Multisample permet des couches instrumentales ; Granular/Spectral peuvent ajouter une couche de texture.
- [DOC] Les oscillateurs A/B/C peuvent utiliser des moteurs différents, ce qui permet une architecture hybride.
- [HEUR] Conserver une couche principale stable et utiliser granular/spectral comme couleur plutôt que comme unique source si le pad doit rester harmonique dans tout le clavier.

## Ableton Live 12
- [DOC] **Wavetable** : deux oscillateurs, deux filtres, enveloppes/LFO/matrice — excellent pour pads modulés.
- [DOC] **Meld** : deux moteurs et filtres indépendants, matrice et MPE — adapté aux pads bi-timbraux/expressifs.
- [DOC] **Analog** : deux oscillateurs, deux filtres, enveloppes/LFO — pad analogique classique.
- [DOC] **Granulator III** : Ableton cite explicitement pads/textures ; idéal en couche.

## Profil [HEUR]
- Polyphonie suffisante pour éviter le voice stealing.
- Attack 20 ms à plusieurs secondes selon fonction ; release calibré à l'harmonie, pas automatiquement très long.
- Mouvements lents de cutoff, wavetable/grain, pan et niveau de couche.
- Contrôler le bas : une large stéréo n'est pas utile sous la zone où le kick/sub dominent.

## Macros
`TONE`, `MOTION`, `ATTACK`, `RELEASE`, `WIDTH`, `SPACE`, `TEXTURE`.

## Validation
Accords serrés et ouverts sur plusieurs octaves, notes répétées rapides, transitions d'accords. Vérifier le voice stealing, le masquage du lead/vocal et l'accumulation de reverb.

## Sous-types v5
Consulter `../subtypes/pad-subtypes.md` avant de construire une recette détaillée. Utiliser `../subtype-selection-matrix.md`, `../professional-layering.md`, `../macro-templates-v5.md` et `../subtype-validation.md` pour la sélection, le layering, les macros et la validation.
