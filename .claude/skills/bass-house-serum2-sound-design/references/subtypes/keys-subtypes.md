# Keys — sous-types professionnels v5

## 1. Electric piano / EP
**Rôle** : clavier expressif, chaleureux, attaque + corps + tremolo/chorus possible.

**Serum** : Multisample si un instrument enregistré adapté est disponible.  
**Ableton [DOC]** : Electric est un piano électrique modélisé physiquement.  
**HEUR** : vélocité agit sur hardness/brightness autant que volume ; chorus/tremolo léger.  
**Macros** : `SOFT↔HARD`, `BODY`, `TONE`, `TREMOLO`, `SPACE`.  
**Test** : vélocités 30/70/110 et accords.

## 2. FM digital keys
**Rôle** : claviers brillants, bell-keys, digital 80s/modern.

**Serum** : Ratio/Harmonics + envelope séparant attaque métallique et corps.  
**Ableton [DOC]** : Operator.  
**HEUR** : carrier soutenu, modulator plus court ; velocity vers modulation depth.  
**Macros** : `BELL`, `BITE`, `BODY`, `DECAY`, `TONE`.  
**Test** : registre 2–3 octaves ; éviter agressivité dans aigus.

## 3. Organ keys
**Rôle** : sustain stable, harmoniques fixes, jeu d'accords.

**Serum [DOC]** : mode Harmonics peut produire des multiples entiers.  
**Ableton** : Operator/additif ou Analog.  
**HEUR** : faible évolution d'enveloppe ; ajouter key click/noise en layer très court si souhaité.  
**Macros** : `DRAWBARS/HARMONICS`, `CLICK`, `TONE`, `CHORUS`.  
**Test** : accords denses ; contrôler intermodulation si distortion.

## 4. House piano / sampled key
**Rôle** : attaque piano franche et accords House.

**Serum [DOC]** : Multisample pour instruments enregistrés sur plusieurs notes/dynamiques.  
**Ableton** : Sampler/Simpler avec multisample/preset adapté.  
**HEUR** : conserver transient ; réduire release dans patterns rapides ; room courte et éventuellement layer high.  
**Macros** : `ATTACK`, `BODY`, `BRIGHT`, `RELEASE`, `ROOM`.  
**Test** : staccato vs accords tenus, velocity forte.

## 5. Mallet / bell key
**Rôle** : note percussive résonante.

**Serum** : Sample/Multisample ou FM/Ratio.  
**Ableton [DOC]** : Collision est conçu autour de Mallet/Noise + resonators.  
**HEUR** : transient court, resonator decay 0.2–3 s selon tempo ; velocity vers exciter et brightness.  
**Macros** : `MALLET`, `MATERIAL`, `DECAY`, `TUNE`, `SPACE`.  
**Test** : accords ; contrôler partiels inharmoniques.

## 6. Synth key
**Rôle** : clavier synthétique plus défini qu'un pad, plus soutenu qu'un pluck.

**Serum** : Wavetable, amp envelope moyen, filter envelope modérée.  
**Ableton** : Drift/Wavetable.  
**HEUR** : Attack 3–30 ms, Decay 0.3–1.5 s, Sustain 30–80 %, Release 80–600 ms.  
**Macros** : `TONE`, `BITE`, `BODY`, `WIDTH`, `SPACE`.  
**Test** : accords syncopés ; tails propres.

## 7. Plucked key / clav-like
**Rôle** : clavier percussif funky/house, entre key et pluck.

**Serum** : wavetable/square + filter envelope très courte.  
**Ableton** : Tension/Drift/Operator selon timbre.  
**HEUR** : sustain faible mais pas forcément zéro ; release très court. Velocity vers cutoff.  
**Macros** : `CLAV`, `BITE`, `DECAY`, `TONE`.  
**Test** : patterns 1/16 ; articulation doit rester nette sans compresseur excessif.

## 8. Hybrid sampled + synth key
**Rôle** : réalisme d'attaque + sustain synthétique contrôlable.

**Serum** : Multisample/Sample ATTACK + Wavetable BODY, routes séparées.  
**Ableton [DOC]** : Instrument Rack avec Sampler/Electric + Wavetable/Drift.  
**HEUR** : sample dominate 0–150 ms, synth prend ensuite ; crossfade par enveloppes.  
**Macros** : `ATTACK SAMPLE`, `SYNTH BODY`, `TONE`, `WIDTH`, `SPACE`.  
**Test** : jouer notes tenues puis très courtes ; transition sample→synth ne doit pas s'entendre comme deux sons collés.
