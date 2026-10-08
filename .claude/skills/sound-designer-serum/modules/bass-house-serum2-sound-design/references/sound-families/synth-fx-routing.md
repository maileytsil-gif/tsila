# Routage et effets — règles transversales

## Principes documentés
- [DOC] Serum 2 peut router les oscillateurs/filtres vers Filter 1/2, Main, Direct, None et les bus.
- [DOC] Les Racks Ableton permettent des chaînes parallèles et jusqu'à 16 macros.
- [DOC] Auto Filter fournit plusieurs types de filtres, LFO et envelope follower.
- [DOC] Echo fournit deux lignes de delay, modulation, feedback, ducking et reverb intégrée.
- [DOC] Hybrid Reverb combine des moteurs de reverb et permet de façonner la queue.
- [DOC] Roar propose plusieurs routages de saturation ainsi qu'une matrice de modulation.

## Règle pratique [HEUR]
Séparer si possible :
1. **source / articulation** ;
2. **timbre / distortion** ;
3. **mouvement** ;
4. **espace**.
Cela facilite le diagnostic et le mapping au bridge.

## Ordres de départ [HEUR]
- Pluck/Stab/Keys : instrument → EQ correctif → saturation légère → delay/reverb sends.
- Pad/Nappe/Drone : instrument → filtre/tone → mouvement/chorus → EQ de contrôle → espace.
- Riser : source → filtre/pitch/mouvement → saturation/densité → espace automatisé.
- Impact : transient/body → saturation/résonance → EQ/contrôle low-end → tail sur chaîne parallèle.

## Erreurs fréquentes
- mettre la reverb avant d'avoir validé l'enveloppe ;
- élargir le grave ;
- utiliser plusieurs LFO synchronisés identiques qui rendent la texture mécanique ;
- saturer avant de contrôler une résonance extrême ;
- mapper une macro à toute la plage d'un paramètre alors que seule une plage musicale est sûre.
