# FabFilter — traitement des basses

## Saturn 2 [DOC]
- multiband ;
- style, drive, mix, feedback, dynamics, tone et level par bande ;
- modulation via XLFO, EG, envelope follower, MIDI, XY ;
- High Quality réduit l'aliasing via oversampling.

Workflow [HEUR] :
1. préserver la bande sub ou la traiter plus doucement ;
2. saturer davantage BODY/MID ;
3. moduler drive/feedback/tone pour une basse évolutive ;
4. activer HQ si distortion forte et CPU acceptable.

## Pro-Q 4 [DOC]
Dynamic EQ : gain de bande varie avec niveau. Spectral Dynamics : agit sur des fréquences spécifiques à l'intérieur de la bande plutôt que toute la bande.

Usage [HEUR] : calmer une résonance qui n'apparaît que sur certaines notes/LFO positions, plutôt qu'un notch fixe agressif.

## Pro-C 3 [DOC]
Sidechain externe dans Ableton, Host Sync et MIDI trigger disponibles.

Usage [HEUR] :
- ducking au kick ;
- Host Sync pour mouvement régulier sans audio trigger ;
- MIDI trigger pour pattern de ducking indépendant du kick audio.

Toujours vérifier que le sidechain libère la fenêtre temporelle nécessaire sans faire disparaître le groove [TEST].
