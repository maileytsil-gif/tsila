# Modulation et macros

## Hiérarchie

1. **Articulation** : enveloppe d'amplitude.
2. **Timbre lié à la note** : enveloppe one-shot ou expression.
3. **Mouvement cyclique** : LFO.
4. **Contrôle de performance** : macro/MPE/velocity.
5. **Évolution de section** : automation DAW ou macro pilotée par le DAW.

Ne pas utiliser un LFO pour corriger un problème qui relève de l'enveloppe, ni une automation de 64 points pour un geste qui pourrait être décrit par une macro.

## Macros bridge-friendly [HEUR]

Créer un petit contrat stable :
- `BITE` — brillance/agressivité ;
- `MOTION` — profondeur de mouvement ;
- `ATTACK` — impact/transient dans une plage sûre ;
- `WIDTH` — largeur uniquement sur les composantes qui la tolèrent ;
- `SPACE` — sends/FX spatiaux ;
- `GROWL` — warp/FM/distortion contrôlée ;
- `AIR` — hautes fréquences/texture ;
- `TENSION` — macro multi-paramètres pour builds.

Une macro doit être musicale sur toute sa plage. Si les extrêmes créent des résonances, du clipping ou un grave stéréo indésirable, réduire la plage de mapping.

## Matrice Serum [DOC]

Utiliser la Matrix pour documenter chaque relation source→destination. Lorsqu'un patch est remis à un bridge ou à un collaborateur, fournir une table : source, destination, profondeur, sens, bipolarité si pertinente, raison musicale.

## Test

Tester chaque macro aux valeurs 0/25/50/75/100 % et pendant un mouvement continu. Écouter le gain perçu : une macro de timbre ne doit pas devenir accidentellement une macro de volume sans que ce soit intentionnel.
