# Pluck — sous-types professionnels v5

[DOC] Le principe Ableton Learning Synths : sustain d'amplitude à 0, decay contrôlé et filtre ouvert puis refermé rapidement par une enveloppe est une base robuste pour un caractère pluck.

## 1. Bright House pluck
**Rôle** : hook clair, syncopé, léger.

**Serum** : Wavetable harmonique, Amp Env courte, Filter Env plus rapide, petite layer octave.  
**Ableton** : Drift ou Wavetable.  
**HEUR** : Attack 0–5 ms, Decay 150–700 ms, Sustain 0–10 %, Release 40–250 ms. Delay/reverb sur haut seulement.  
**Macros** : `PLUCK`, `BITE`, `DECAY`, `TONE`, `SPACE`.  
**Test** : pattern 1/16 ; queues contrôlées.

## 2. FM metallic pluck
**Rôle** : attaque métallique/numérique.

**Serum** : Ratio/harmonic relation, modulation depth via ENV courte.  
**Ableton [DOC]** : Operator, enveloppes séparées par oscillateur.  
**HEUR** : modulator decay plus court que carrier pour métal au début et corps tonal ensuite.  
**Macros** : `METAL`, `BITE`, `BODY`, `DECAY`.  
**Test** : notes graves/aiguës ; réduire modulation si pitch devient flou.

## 3. Organic string pluck
**Rôle** : pincé proche corde/harpe/guitare synthétique.

**Serum** : Multisample/Sample ou wavetable douce + noise pick.  
**Ableton [DOC]** : Tension offre exciter Pick, corde, damper et soundboard.  
**HEUR** : vélocité vers attack/brightness ; variation légère entre notes.  
**Macros** : `PICK`, `DAMP`, `BODY`, `BRIGHT`, `SPACE`.  
**Test** : répétitions de même note ; éviter son « copié-collé » si organique recherché.

## 4. Glass / resonant pluck
**Rôle** : verre, mallet, cristallin.

**Serum** : source courte + filtre/resonance/combs ou sample.  
**Ableton [DOC]** : Collision (Mallet/Noise + resonators) ou Corpus après une source.  
**HEUR** : transient court, resonance 0.3–2 s, high-pass de la tail si nécessaire.  
**Macros** : `GLASS`, `TUNE`, `DECAY`, `MATERIAL`, `SPACE`.  
**Test** : accord ; contrôler partiels qui créent des notes parasites.

## 5. Bass pluck
**Rôle** : basse tonale courte, pas mid-bass growl.

**Serum** : source simple + sub mono, envelope filtre, saturation légère.  
**Ableton** : Operator/Drift.  
**HEUR** : decay 100–500 ms, sub plus stable que couche médium ; sidechain selon groove.  
**Macros** : `BITE`, `BODY`, `SUB`, `DECAY`, `EDGE`.  
**Test** : kick + basse ; éviter release qui empiète sur note suivante.

## 6. Release pluck / reversed articulation
**Rôle** : attaque douce et accent en fin/release ou effet de « suction ».

**Serum/Ableton** : envelope/volume shape ou sample reverse; delay/reverb avant gate possible.  
**HEUR** : utiliser comme layer de réponse, pas nécessairement comme source principale.  
**Macros** : `SWELL`, `RELEASE`, `SPACE`, `TONE`.  
**Test** : timing de fin de note ; vérifier que l'effet reste synchronisé quand les durées MIDI changent.

## 7. Bass House call-response pluck
**Rôle** : petit pluck percussif répondant au bass shot/stab.

**Serum/Ableton** : pluck bright ou metallic, registre au-dessus de la mid-bass.  
**HEUR** : decay très court, espace stéréo léger, aucun sub ; variation de cutoff/velocity entre réponses.  
**Macros** : `BITE`, `TONE`, `WIDTH`, `SPACE`.  
**Test** : solo bass + pluck ; vérifier séparation de registre et rythme.
