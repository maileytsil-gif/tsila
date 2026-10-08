# Layering professionnel — règles v5

## Principe

Une couche n'est justifiée que si elle remplit une fonction audible différente. Les fonctions standards sont :

- `FUNDAMENTAL` : hauteur/fondation ;
- `BODY` : masse médium et identité ;
- `ATTACK` : transient/clic/pick ;
- `AIR` : information haute fréquence ;
- `TEXTURE` : grain/noise/spectral ;
- `TAIL` : espace/réverbération/delay ;
- `MOVEMENT` : couche dont la fonction principale est l'évolution.

[HEUR] Deux couches qui occupent le même registre, ont la même enveloppe et le même mouvement sont suspectes. Muter l'une puis l'autre et supprimer celle qui ne change pas clairement la fonction du son.

## Serum 2

[DOC] OSC A/B/C peuvent utiliser des moteurs différents. Le routage permet de traiter les sources différemment via filtres, Main, Direct, None et BUS 1/2.

Applications [HEUR] :
- transient → voie plus sèche/directe ;
- corps → filtre principal ;
- air/noise → bus ou filtre distinct ;
- texture granular/spectral → dosage faible et modulation lente ;
- modulator inaudible → route `None` si le rôle est seulement modulation et si la configuration l'exige.

## Ableton Instrument Rack

[DOC] Les chaînes d'un Rack peuvent fonctionner en parallèle et leurs sorties sont sommées. Jusqu'à 16 Macro Controls peuvent piloter plusieurs paramètres et leurs plages peuvent être limitées/inversées.

Applications [HEUR] :
- Chain 1 = CORE ;
- Chain 2 = ATTACK ;
- Chain 3 = TEXTURE/AIR ;
- Chain 4 = TAIL ou coloration parallèle.

Ne pas mettre une longue reverb directement dans toutes les chaînes si une seule queue commune suffit.

## Phase et registre

- Sub/low layer : tester mono, polarité/phase et overlap avec kick.
- Wide layer : high-pass ou réduire l'information stéréo dans le bas selon le rôle.
- Layer transposé +12/+24 : vérifier qu'il apporte de la définition plutôt qu'une dureté supplémentaire.
- Sampled attack : vérifier le point de départ et la cohérence de hauteur si le son doit être tonal.

## CPU

[DOC] Granular et unison/voix multiples peuvent augmenter la charge. [HEUR] Une fois le comportement musical validé, resampler les couches lourdes qui n'ont plus besoin d'être interactives. Conserver le preset/source original.
