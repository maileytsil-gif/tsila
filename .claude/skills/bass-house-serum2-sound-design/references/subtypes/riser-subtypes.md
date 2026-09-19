# Riser — sous-types professionnels v5

## 1. Noise riser
**Rôle** : montée non tonale classique.

**Serum** : NOISE/Sample ; pitch tracking off si pertinent [DOC] ; filtre qui s'ouvre + volume/densité.  
**Ableton** : noise/sample + Auto Filter ; Shifter/Echo en option.  
**HEUR** : high-pass progressif ou band-pass mobile pour éviter de remplir tout le spectre.  
**Macros** : `RISE`, `BRIGHTNESS`, `WIDTH`, `SPACE`.  
**Test** : dernier quart ; contrôler harshness et niveau crête.

## 2. Tonal pitch riser
**Rôle** : montée clairement accordée vers l'impact.

**Serum [DOC]** : CRS est conçu pour les sweeps continus de hauteur et comme destination modulation/automation.  
**Ableton** : Drift/Operator + automation pitch ou Shifter sur une source audio.  
**HEUR** : +12/+24 semitones ou trajectoire non linéaire ; si le riser doit « résoudre », viser une note compatible avec l'impact/drop.  
**Macros** : `PITCH`, `RISE`, `TONE`, `SPACE`.  
**Test** : vérifier la hauteur finale et absence de saut au point d'impact.

## 3. Filter resonance riser
**Rôle** : montée par énergie spectrale plutôt que pitch global.

**Serum** : source tenue + cutoff/resonance/drive.  
**Ableton [DOC]** : Auto Filter avec plusieurs types de filtres, LFO et envelope follower ; Drive/circuits pour couleur.  
**HEUR** : augmenter cutoff puis modérément resonance ; éviter de faire grimper niveau et resonance sans compensation.  
**Macros** : `FILTER`, `RESO`, `DRIVE`, `TENSION`.  
**Test** : peak meter + écoute faible volume.

## 4. Granular riser
**Rôle** : densité et désordre croissants à partir d'un sample.

**Serum [DOC]** : Granular.  
**Ableton [DOC]** : Granulator III peut manipuler et boucler des snippets ; Loop/Cloud selon matériau.  
**HEUR** : position monte/avance, grain size/density évolue, pitch seulement en couche secondaire.  
**Macros** : `POSITION`, `GRAIN`, `DENSITY`, `RISE`, `SPACE`.  
**Test** : le riser doit rester directionnel même sans automation de volume.

## 5. Feedback / distortion riser
**Rôle** : build agressif, industriel, Bass House.

**Serum** : source simple + FX; feedback/drive si disponible dans chaîne prévue.  
**Ableton [DOC]** : Roar comporte feedback, filtres et plusieurs routages ; Echo apporte feedback et modulation.  
**HEUR** : automatiser feedback avec plafond sûr ; drive peut augmenter pendant que output est compensé.  
**Macros** : `FEEDBACK`, `DISTORT`, `FILTER`, `TENSION`.  
**Test** : STOP input ; s'assurer que le feedback ne part pas hors contrôle.

## 6. Pulsed / accelerating riser
**Rôle** : sensation d'accélération vers le drop.

**Serum** : LFO/enveloppe one-shot pour amplitude/filter ; rate accéléré par automation ou modulation.  
**Ableton [DOC]** : Drift Cycling Envelope/LFO avec modes Rate/Ratio/Time/Sync.  
**HEUR** : divisions 1/4→1/8→1/16→1/32 ou accélération continue ; ne pas forcément augmenter le volume.  
**Macros** : `PULSE`, `RATE`, `DEPTH`, `TENSION`.  
**Test** : précision rythmique sur 4/8/16 mesures.

## 7. Hybrid cinematic riser
**Rôle** : riser complet à plusieurs axes.

**Architecture [HEUR]** : 1) noise/filter, 2) tonal pitch, 3) texture granular, 4) tail/reverb. Les axes ne doivent pas culminer exactement au même moment ; garder 50–150 ms de marge selon impact.  
**Ableton [DOC]** : Rack permet chaînes parallèles/macros.  
**Macros** : `RISE`, `TENSION`, `DENSITY`, `WIDTH`, `SPACE`, `PULSE`.  
**Test** : mute chaque layer ; chacun doit apporter une fonction identifiable.
