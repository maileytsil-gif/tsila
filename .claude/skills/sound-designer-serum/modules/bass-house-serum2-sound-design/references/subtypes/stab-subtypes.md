# Stab — sous-types professionnels v5

## 1. House chord stab
**Rôle** : accord court sur contretemps ou syncope.

**Serum** : Wavetable/saw+square, enveloppe amp courte, enveloppe filtre encore plus rapide.  
**Ableton** : Drift ou Analog.  
**HEUR** : Attack 0–15 ms, Decay 120–600 ms, Sustain 0–20 %, Release 30–250 ms. Courte room/plate.  
**Macros** : `BITE`, `DECAY`, `TONE`, `WIDTH`, `SPACE`.  
**Test** : 1/8 offbeat ; la queue ne doit pas masquer le kick suivant.

## 2. Bass House metallic stab
**Rôle** : stab médium agressif qui dialogue avec la basse.

**Serum** : Wavetable + rapport/harmoniques ou modulation rapide ; noise d'attaque possible.  
**Ableton** : Operator pour métal/FM, puis Roar léger si besoin.  
**HEUR** : garder le sub hors de ce layer ; high-pass selon arrangement. Envelope timbre très courte pour le « clang ».  
**Macros** : `METAL`, `BITE`, `BODY`, `EDGE`, `SPACE`.  
**Test** : avec mid-bass ; si les deux se confondent, changer registre/enveloppe plutôt qu'empiler EQ.

## 3. Organ / rave stab
**Rôle** : timbre à harmoniques stables, sustain court, attaque franche.

**Serum [DOC]** : mode Harmonics pour relations de hauteur ; Wavetable possible.  
**Ableton [DOC]** : Operator/additif ou Analog.  
**HEUR** : empilement 1x/2x/3x/4x contrôlé ; peu de detune. Chorus ou short delay pour couleur.  
**Macros** : `HARMONICS`, `DECAY`, `TONE`, `CHORUS`.  
**Test** : accords majeurs/minor7 ; éviter intermodulation désagréable avec saturation forte.

## 4. Sampled chord stab
**Rôle** : caractère immédiat venant d'un one-shot ou d'un ancien synth/sample.

**Serum [DOC]** : Sample/Multisample.  
**Ableton [DOC]** : Simpler One-Shot ou Sampler.  
**HEUR** : corriger start point, tune et tail avant tout autre traitement. Si le sample contient déjà reverb, éviter de doubler la queue.  
**Macros** : `START`, `TONE`, `DECAY`, `PITCH`, `SPACE`.  
**Test** : transpositions ±5/±12 semitones ; vérifier artefacts et durée.

## 5. Filter punch stab
**Rôle** : stab dont l'impact vient d'une ouverture/fermeture de filtre exagérée.

**Serum** : source riche, cutoff bas, ENV courte vers cutoff/resonance modérée.  
**Ableton** : Drift + Env 2/Cycling Envelope ou Analog.  
**HEUR** : filtre peut fermer plus vite que volume. Drive contrôlé avant filtre pour densifier l'attaque.  
**Macros** : `PUNCH`, `FILTER`, `RESO`, `DRIVE`, `DECAY`.  
**Test** : écouter le clic de filtre à faible niveau ; éviter les pics de résonance.

## 6. Wide top stab
**Rôle** : couche aiguë de stab, à combiner avec un core plus centré.

**Serum/Ableton** : layer +12/+24, high-pass, width/chorus/delay court.  
**HEUR** : le top doit pouvoir être coupé sans perdre l'accord ; il apporte largeur et brillance, pas la fonction harmonique principale.  
**Macros** : `AIR`, `WIDTH`, `EDGE`, `SPACE`.  
**Test** : mono ; la couche peut réduire mais le core doit rester intact.
