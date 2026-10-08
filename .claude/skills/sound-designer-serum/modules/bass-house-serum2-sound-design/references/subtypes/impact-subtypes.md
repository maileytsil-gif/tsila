# Impact — sous-types professionnels v5

## 1. Club sub impact
**Rôle** : poids grave court sous un crash/hit.

**Serum** : Sample hit + oscillateur/sub simple ; pitch tracking off possible pour percussif [DOC].  
**Ableton [DOC]** : Drum Sampler avec Sub Osc/Pitch Env ou Simpler.  
**HEUR** : sub decay 120–600 ms ; laisser le kick suivant respirer.  
**Macros** : `LOW`, `BODY`, `TAIL`.  
**Test** : phase avec kick et mono.

## 2. Cinematic boom
**Rôle** : impact large, profond, longue sensation de taille.

**Serum** : sample low/body + noise/texture, routes séparées.  
**Ableton** : Simpler + Corpus/Hybrid Reverb. [DOC] Corpus simule des objets résonants ; Hybrid Reverb combine convolution/algorithme.  
**HEUR** : transient sec → body → tail filtrée.  
**Macros** : `HIT`, `SIZE`, `LOW`, `TAIL`, `DISTANCE`.  
**Test** : niveau de queue 2–8 s ; contrôler le grave de la reverb.

## 3. Metallic impact
**Rôle** : clang, plaque, métal, machine.

**Serum** : sample/noise + filtre/ring/combs selon patch ; body tonal séparé si nécessaire.  
**Ableton [DOC]** : Corpus (Beam/Plate/Pipe/etc.) ou Collision.  
**HEUR** : excitation très courte, resonance plus longue ; tune/decay avant reverb.  
**Macros** : `METAL`, `TUNE`, `DECAY`, `SIZE`, `SPACE`.  
**Test** : résonance sur plusieurs notes si impact accordé ; éviter notes parasites.

## 4. Tonal impact
**Rôle** : impact accordé au morceau, souvent fondamentale/quinte/octave.

**Serum** : Wavetable ou Sample accordé + pitch envelope descendante courte.  
**Ableton** : Operator/Drum Sampler Pitch Env.  
**HEUR** : chute 7–24 semitones selon caractère ; fin de chute proche de la fondamentale voulue.  
**Macros** : `PITCH DROP`, `BODY`, `LOW`, `TAIL`.  
**Test** : tuner + contexte harmonique.

## 5. Noise slam / transient impact
**Rôle** : attaque sans note forte, utile quand kick/sub portent déjà le grave.

**Serum** : Noise/Sample, high-pass/band-pass, envelope très courte.  
**Ableton** : Drum Sampler Noise/Punch ou Simpler.  
**HEUR** : transient 5–80 ms + room très courte ; limiter le tail.  
**Macros** : `HIT`, `BITE`, `NOISE`, `ROOM`.  
**Test** : doit rester audible sur téléphone/petit speaker.

## 6. Reverse + impact pair
**Rôle** : aspiration puis hit.

**Architecture** : reverse tail/swell avant temps 1 + impact sec sur temps 1.  
**Serum/Ableton** : Sample/Simpler pour source audio ; automation filtre/volume.  
**HEUR** : la reverse doit libérer le grave juste avant l'impact ; éviter overlap qui réduit le contraste.  
**Macros** : `SUCK`, `HIT`, `TAIL`, `WIDTH`.  
**Test** : couper exactement au transient puis comparer à version overlap.

## 7. Debris / aftershock impact
**Rôle** : événement principal suivi de particules/débris.

**Serum** : main sample + granular/noise bus.  
**Ableton** : Simpler + Granulator III/Delay/Rack.  
**HEUR** : les débris occupent surtout haut/médium et peuvent être randomisés ; ne pas multiplier les subs.  
**Macros** : `DEBRIS`, `DENSITY`, `SPACE`, `TAIL`.  
**Test** : débris audibles sans masquer la première mesure du drop.
