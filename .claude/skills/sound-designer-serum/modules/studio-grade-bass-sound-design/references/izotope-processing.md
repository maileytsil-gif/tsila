# iZotope — traitement des basses

## Neutron 5 [DOC]
- **Exciter** : saturation/distortion multibande avec 4x oversampling et types blendables.
- **Transient Shaper** : contrôle de l'impact, multibande, différents contours.
- **Clipper** : jusqu'à trois bandes, M/S et transient/sustain, 4x oversampling.
- **Density** : upward compression pour renforcer poids/détail.
- **Phase** : analyse asymétrie et problèmes de phase entre pistes.
- **Unmask/EQ/Compressor** : outils de séparation et dynamique.

Usage [HEUR] :
- Exciter sur upper bass ;
- Clipper pour contrôler des pics d'une basse percussive ;
- Density avec parcimonie si le body manque de continuité ;
- Phase quand kick+basse semblent faibles malgré des niveaux corrects.

## Trash [DOC]
La génération actuelle combine un moteur `Trash` de distortion et `Convolve` par impulse responses. Les versions anciennes de Trash ont une autre architecture ; confirmer la version installée [TEST].

Usage [HEUR] : parallel destruction, growls, metallic/body, resampling. Garder une copie dry/clean sub.
