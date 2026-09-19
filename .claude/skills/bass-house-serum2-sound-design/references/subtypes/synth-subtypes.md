# Synthé — sous-types professionnels v5

Les capacités des moteurs sont [DOC] ; les architectures et valeurs sont [HEUR].

## 1. Analog moderne / club synth
**Rôle** : synthé tonal propre, chaud, immédiatement jouable ; bon point de départ pour riffs House/Bass House.

**Serum 2** : Wavetable avec formes simples ; 1 source principale + éventuelle source +12 très faible. Filtre LP ou morphable. Mouvement subtil de WT POS ou fine pitch.  
**Ableton** : Drift pour simplicité/CPU ou Analog pour une architecture analogique plus classique.  
**Enveloppe [HEUR]** : Attack 2–20 ms, Decay 0.2–1.2 s, Sustain 35–80 %, Release 50–300 ms selon legato.  
**Traitement** : saturation légère → EQ → chorus/delay si nécessaire.  
**Macros** : `TONE`, `DRIFT`, `EDGE`, `WIDTH`, `SPACE`.  
**Test** : accord + riff mono ; si l'unison est coupé, le son doit rester valable.

## 2. Digital Wavetable / motion synth
**Rôle** : timbre moderne dont la signature vient du mouvement spectral.

**Serum 2 [DOC]** : Wavetable sur OSC A/B/C ; moduler WT POS par enveloppe pour geste par note ou LFO pour mouvement répété.  
**Ableton [DOC]** : Wavetable, deux oscillateurs et matrice de modulation.  
**HEUR** : limiter le balayage à la zone musicalement utile de la table plutôt que 0→100 % par défaut. Ajouter un deuxième mouvement plus lent sur filtre ou warp.  
**Macros** : `MORPH`, `TONE`, `MOTION`, `EDGE`, `SPACE`.  
**Test** : tenir 8 mesures et vérifier qu'aucun point de la table ne produit un pic agressif.

## 3. FM / metallic synth
**Rôle** : attaque dure, caractère métallique, digital ou bell-like.

**Serum 2 [DOC]** : le mode de pitch peut utiliser `Ratio`; Serum propose des relations harmoniques adaptées aux structures FM/ratiométriques. [HEUR] Utiliser une source/modulatrice peu audible et contrôler la profondeur avec une enveloppe rapide.  
**Ableton [DOC]** : Operator combine quatre oscillateurs avec FM/additif/soustractif et enveloppes individuelles.  
**HEUR** : ratios simples pour une hauteur stable ; rapports non entiers ou modulation plus forte pour inharmonicité.  
**Macros** : `METAL`, `BITE`, `BODY`, `DECAY`, `TONE`.  
**Test** : jouer plusieurs notes ; si la sensation de hauteur disparaît, réduire la profondeur FM ou isoler le métal en couche d'attaque.

## 4. Supersaw / stacked synth
**Rôle** : énergie harmonique large pour accords, hooks et layers hauts.

**Serum 2** : Wavetable saw/forme riche, unison mesuré ; deuxième oscillateur octave/intervalle seulement si nécessaire.  
**Ableton** : Wavetable ou Rack de deux couches ; Drift pour une couche plus sobre.  
**HEUR** : largeur dans le haut/médium, centre plus stable ; ne pas surcharger le bas. La densité d'accord remplace souvent plusieurs voix d'unison.  
**Macros** : `STACK`, `DETUNE`, `TONE`, `WIDTH`, `SPACE`.  
**Test** : mono + accords serrés ; si le centre s'effondre, réduire detune/largeur ou créer une couche CORE mono-compatible.

## 5. Hybrid morphing synth
**Rôle** : deux identités timbrales qui se transforment l'une dans l'autre.

**Serum 2 [DOC]** : OSC A/B/C peuvent employer des moteurs différents ; combiner Wavetable CORE + Granular/Spectral TEXTURE. Routage séparé via filtres/bus.  
**Ableton [DOC]** : Meld possède deux moteurs indépendants ; un Instrument Rack peut aussi croiser deux chaînes.  
**HEUR** : une macro `MORPH` doit changer la balance et éventuellement le filtre/FX de chaque couche en sens opposé, pas seulement le volume global.  
**Macros** : `MORPH`, `CORE`, `TEXTURE`, `MOTION`, `SPACE`.  
**Test** : positions 0/25/50/75/100 % ; chacune doit être exploitable et sans saut de niveau.

## 6. Resonant / acid-style synth
**Rôle** : ligne mono expressive dont le filtre est le personnage principal.

**Serum 2** : source simple riche + filtre résonant ; enveloppe courte sur cutoff ; glide si la phrase le demande.  
**Ableton [DOC]** : Drift/Analog + filtre ; Auto Filter peut ajouter un second mouvement, mais éviter de dupliquer inutilement le rôle du filtre de synthèse.  
**HEUR** : le drive avant/après filtre change fortement le caractère ; vérifier gain matching.  
**Macros** : `CUTOFF`, `RESO`, `ENV`, `DRIVE`, `GLIDE`.  
**Test** : notes répétées et legato ; contrôler les pics de résonance.
