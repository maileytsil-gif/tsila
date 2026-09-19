# Matrice rôle → moteur → contrôle → test

| Rôle | Moteur de départ | Contrôle prioritaire | Test critique | Risque |
|---|---|---|---|---|
| Sub | Operator/Drift/Serum source simple | amplitude + mono | compatibilité kick/phase | unison/FX grave |
| Mid-bass | Serum/Wavetable/Operator/Meld | articulation + timbre | lisibilité sans FX | trop de mouvement |
| Pluck/stab | Drift/Operator/Serum/Analog | decay + filtre | accord/registre | queue trop longue |
| Lead | Serum/Wavetable/Meld/Drift | contour + expression | mélodie entière | largeur/harshness |
| Pad | Meld/Wavetable/Serum/Analog | mouvement lent | masque du hook | densité/low-mid |
| Riser | Serum/Meld/Granulator III | macro tension | trajectoire | juste « plus fort » |
| Texture | Granulator III/Serum Granular/Spectral/Sampler | position/densité | contexte mix | instabilité/CPU |

Les choix sont [HEUR] ; les capacités des instruments sont [DOC].

## Architecture en couches

Ajouter une couche seulement si elle a une fonction distincte : fondamentale, attaque, corps, hautes harmoniques, bruit/texture ou espace. Si deux couches jouent le même rôle, tester laquelle peut être supprimée.

## Registre

Tester le patch sur la phrase réelle. Un son de bass design peut changer radicalement entre deux notes parce que filtre, wavetable, distortion et résonances ne se déplacent pas toutes de façon perceptuellement uniforme.

## Resampling

Lorsque le patch devient trop complexe/CPU-heavy, resampler une phrase ou un one-shot peut stabiliser le résultat. Conserver le patch source pour l'édition et nommer le rendu avec tonalité/version.
