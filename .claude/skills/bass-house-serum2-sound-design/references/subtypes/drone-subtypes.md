# Drone — sous-types professionnels v5

## 1. Drone tonal stable
**Rôle** : fondamentale ou note-pédale clairement accordée.

**Serum 2** : Wavetable simple ; pitch tracking activé si le drone doit suivre les notes, désactivé si une hauteur fixe est voulue [DOC].  
**Ableton** : Drift/Wavetable/Meld.  
**HEUR** : très peu de mouvement de pitch ; mouvement surtout sur filtre/harmoniques.  
**Macros** : `TONE`, `TENSION`, `MOTION`, `SPACE`.  
**Test** : analyse sur 30 s ; la hauteur doit rester perceptible et le niveau stable.

## 2. Drone subharmonic / ominous
**Rôle** : fond grave menaçant, souvent pour break ou intro.

**Serum** : source fondamentale simple + couche harmonique au-dessus ; éviter large stereo dans le bas.  
**Ableton** : Operator/Drift pour core, texture séparée dans Rack.  
**HEUR** : un mouvement très lent de filtre/drive au-dessus du sub donne l'évolution sans faire dériver la fondamentale.  
**Macros** : `LOW`, `RUMBLE`, `TENSION`, `DARKNESS`.  
**Test** : mono, petits haut-parleurs et casque ; si seul le sub est audible, renforcer une harmonique de lecture.

## 3. Drone granular Cloud
**Rôle** : texture soutenue où l'échantillon devient matière.

**Serum [DOC]** : Granular ; pitch tracking peut être désactivé pour drone/statique.  
**Ableton [DOC]** : Granulator III Cloud est explicitement conçu pour drones/textures expérimentales.  
**HEUR** : position et densité bougent lentement ; grain size peut bouger indépendamment.  
**Macros** : `POSITION`, `GRAIN`, `DENSITY`, `MOTION`, `SPACE`.  
**Test** : 32 mesures ; repérer répétitions audibles ou zones de sample trop dominantes.

## 4. Drone spectral evolving
**Rôle** : spectre en transformation lente, science-fiction/ambient.

**Serum [DOC]** : Spectral ; combiner avec une source stable à faible niveau si nécessaire.  
**Ableton** : Meld + resampling/granular/Corpus comme architecture alternative.  
**HEUR** : moduler 2–3 axes maximum à des périodes différentes ; les cycles trop synchrones révèlent la boucle.  
**Macros** : `SPECTRUM`, `SHIFT`, `MOTION`, `WIDTH`, `SPACE`.  
**Test** : vérifier pics de résonance et dérive de niveau.

## 5. Drone industrial / noise machine
**Rôle** : tension, machine, friction, métal.

**Serum** : Noise/Sample/Granular + filtre/ring/comb selon besoin ; routage séparé pour conserver un core.  
**Ableton [DOC]** : Roar feedback peut produire ringing/textures ; Corpus simule des objets résonants.  
**HEUR** : gate/feedback avec limite de gain stricte ; automation lente de couleur.  
**Macros** : `GRIT`, `METAL`, `FEEDBACK`, `FILTER`, `SPACE`.  
**Test** : couper l'entrée ; surveiller si feedback/tail continue indéfiniment.

## 6. Harmonic cluster drone
**Rôle** : accord dense ou cluster tenu plutôt qu'une seule hauteur.

**Serum** : plusieurs oscillateurs/intervalles ou unison contrôlé ; mode Harmonics possible [DOC].  
**Ableton** : Meld/Rack avec 2–3 couches transposées.  
**HEUR** : préférer intervalles intentionnels à un detune aléatoire massif ; contrôler les battements.  
**Macros** : `CLUSTER`, `DETUNE`, `TONE`, `MOTION`.  
**Test** : mono et registre grave ; réduire intervalles/couches si le bas devient instable.
