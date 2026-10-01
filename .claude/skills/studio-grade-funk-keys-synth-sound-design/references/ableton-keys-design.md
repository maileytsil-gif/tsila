# Instruments et effets natifs de Live 12 pour les claviers et synthés funk

Faits constructeur : texte du manuel Live 12 (ch. 28 effets, ch. 30 instruments, version ≥ 12.3) lu sur copie intégrale et recoupé mot pour mot avec les extraits officiels (`../../../../corpus/constructeur/`). Tous les paramètres sont pilotables et relisibles par `ppal-update-device` / `ppal-read-device` avec les noms API relevés dans le Set (`../../vst-sound-design/references/instruments-natifs.md`) — c'est l'argument décisif pour le natif.

## Quel instrument pour quel clavier

| Clavier | Premier choix | Alternative | Ce que dit le manuel [DOC sauf mention] |
|---|---|---|---|
| Rhodes | **Electric** (modèle physique AAS, « aucun sample ») avec Pickup **R** | pack **Electric Pianos** (Rhodes Stage 73 + Wurlitzer 200A samplés, 70 racks, 120 clips joués) [DOC-EXTRAIT] ; Serum 2 Multisample « Elec.Piano Suitcase » | R = « electro-dynamic pickups » ; Rhodes/Wurlitzer nommés seulement sur la page du pack Electric |
| Wurlitzer | **Electric** Pickup **W** (« electro-static model ») | pack Electric Pianos ; NI Scarbee A-200 | W = électrostatique, exactement la non-linéarité capacitive du 200A [DOC openwurli] |
| Clavinet | pack **Clav** (Hohner D6 samplé « avec toutes ses nuances funky ») [DOC-EXTRAIT] | **Tension** (Plectrum ou Hammer, Damper Gated, Pickup) [HEUR : le manuel ne cite jamais le Clavinet] ; NI Scarbee Clavinet | Tension : exciteurs Bow/Hammer/Hammer bouncing/Plectrum, Damper (Mass, Stiffness, Velocity, Gated, Position), String (Decay, Inharm, Damping), Termination, Pickup (Position : bas = brillant et fin), Body ; « très facile de produire aucun son ou un son extrêmement fort » |
| Hammond | pack **Electric Keyboards** (2 pianos électromécaniques + **1 orgue tonewheel**) [DOC-EXTRAIT] | **Operator** additif (onde User, partiels 1-2-3-4-6-8-10-12-16 aux niveaux des drawbars) [HEUR] ; NI Vintage Organs | Operator : édition de 16/32/64 harmoniques, Normalize, export .ams |
| Synth bass mono | **Drift** (Mono + Legato + Glide, Mono Thickness, filtre Type I 12 dB / Type II 24 dB) | **Analog** (Voices 1, Legato, Glide Const/Prop, Sub, Drive Asym) | Drift : « Mono … rendu par quatre voix, unisson selon Mono Thickness » ; « Legato : une nouvelle voix change la hauteur sans remettre les enveloppes à zéro » |
| Poly analogique (Juno, Prophet, Oberheim) | **Analog** (2 osc saw/rect avec PWM par LFO, Sync, Sub, filtres 2e/4e ordre dont **formant**, Legato, Vibrato Delay/Attack/Error/Amt < MW, Unison 2/4) | Wavetable (unison Classic, filtres OSR/MS2/PRD/SMP) | Wavetable : circuits « OSR : monosynth britannique rare », « MS2 : semi-modulaire japonais », « PRD : ladder, dual-osc monosynth américain » |
| DX7 (E.PIANO 1, BASS 1, KOTO…) | **Operator** (4 opérateurs, 11 algorithmes, Feedback sur osc non modulé, Fixed, Voices = 1 → legato, Spread) | Serum 2 FM from B | « conçu par amour des vieux FM matériels : SY77, TX81Z, Synclavier II » ; recettes dans `dx7-fm-keys-bass.md` |
| Talkbox | **Vocoder** carrier External (piste synthé scie), Unvoiced, Enhance, Formant | Auto Filter **Vowel**, Meld filtre **Vowel** | « essayez des patches à base de dent de scie pour l'intelligibilité » |
| Marimba, cloches | Operator (MARIMBA ROM1A), **Collision** (mallet + résonateurs) | — | Collision : « garder les niveaux bas » |

## Electric — paramètres et noms API [DOC]
- **Hammer** : Stiffness (+ Vel, Key) « plus haut = plus brillant » ; Noise (Pitch, Decay, Key) ; Force (+ Vel, Key) « intensité de l'impact ».
- **Fork** : Tine (Color = équilibre partiels haut/bas, Decay, Key), Tone (résonance secondaire = tonebar, Decay), Release commun.
- **Pickup** : Symmetry (50 % = en face du tine = plus brillant ; autres valeurs = dessous/dessus), Distance (« plus proche = plus overdrivé »), Type R/W, Input (quantité de distorsion), Output.
- **Damper** : Tone (dureté), Level, Att/Rel (−100 = bruit à l'attaque seule, +100 = au relâchement seul).
- **Global** : Voices, Semi, Detune ±50 cents, **Stretch** (0 % = tempérament égal), Stretch Center (page manquante [TEST]).
- API (classe LoungeLizard) : `M Stiffness, M Stiff < Vel/Key, M Force, M Force < Vel/Key, Noise Pitch/Decay/Amount, Noise < Key, F Tine Color/Decay/Vol, F Tine < Key, F Tone Decay/Vol, F Release, P Symmetry, P Distance, Pickup Model, P Amp In, P Amp Out, P Amp < Key, Damp Tone/Amount/Balance, Volume, Voices, Semitone, Detune, KB Stretch, PB Range`.
- Plages de départ tierces [HEUR] : Stiffness 50–70 % naturel, > 80 % métallique ; Noise 10–20 % ; Tine Decay court = « clav-like ». Aucune valeur de preset lue : recettes [TEST] dans `../recipes/`.

## Effets natifs qui font le funk [DOC]
- **Auto Filter** (12.2+) : dix types dont **Vowel** (Pitch, Formant a-e-i-o-u, Morph), DJ, Comb, Notch + LP ; **envelope follower** Attack (« inertie »), Hold, Release, S&H ; quantité bipolaire ; circuits SVF/DFM/MS2/PRD ; Drive ; Clip ; sidechain mono. = Mu-Tron III / envelope filter.
- **Phaser-Flanger** : Phaser (Notches, Center, Spread, Blend), Flanger, Doubler ; LFO dont **Triangle Analog** (rectangle filtré) ; suiveur d'enveloppe ; **Safe Bass** ; Warmth. = Small Stone / Phase 90.
- **Chorus-Ensemble** : Classic (2 lignes), **Ensemble** (3 lignes, « pédale 70s », conseil 1–1,8 Hz à 100 %), Vibrato ; High-Pass ; Width 0–200 %. = chorus Juno / Dimension D / Dyno stéréo.
- **Auto Pan-Tremolo** (12.3) : **Panning** (deux LFO, Phase 180° = opposition, Spin) = trémolo panoramique Suitcase ; **Tremolo** (une LFO, options **Harmonic** crossover 600 Hz et **Vintage** courbe non linéaire) = Wurlitzer, ampli Fender ; formes dont Square et Shark Tooth ; Shape/Invert = gating/pumping.
- **Pedal** : Overdrive (« chaud »), Distortion, Fuzz ; EQ Bass 100 Hz, Mid 500 Hz/1 kHz/2 kHz, Treble 3,3 kHz, Sub < 250 Hz ; « un Compressor avant Pedal donne un résultat plus équilibré ». **Amp** (Softube, 7 amplis : Clean = canal Brilliant 60s, Boost, Blues, Rock, Bass, …) + **Cabinet** (1×12 → 4×12, micro Near On/Off-Axis, Far, Dynamic/Condenser) = Twin repiqué au SM57.
- **Compressor** : Peak/RMS/Expand, Lin/Log, Lookahead 0/1/10 ms, knee ; « des releases courts provoquent le pumping ». **Glue** : bus SSL (Cytomic), Auto Release à deux constantes, Range −60/−70 dB = matériel, Soft clip. **Saturator** : Analog Clip, Soft Sine, Bass Shaper, …, Color. **Redux** (Rate, Jitter, Bits, Shape, DC Shift), **Vinyl Distortion** (Tracing, Pinch, Soft « dub plate »/Hard, Crackle), **Erosion**, **Drum Buss** (Comp fixe, Crunch, Transients) = grain SP-303/SP-1200.
- **Vocoder** : Carrier Noise/External/Modulator/Pitch Tracking ; Bands, Range, BW, Precise/Retro, Depth, Formant, Unvoiced.
- **Multiband Dynamics** : compression ascendante/descendante sur 3 bandes ; preset « OTT » non décrit par le manuel [HEUR].
- **Spectral Resonator**, **Shifter** (Ring < 20 Hz = trémolo) : effets créatifs.

## Ce que le natif ne fait pas
Pas de Leslie dédié : le construire dans un Audio Effect Rack à deux bandes (EQ à 800 Hz) avec Auto Pan-Tremolo (horn 0,67/7,06 Hz, tambour 0,60/5,96 Hz), Chorus-Ensemble Vibrato pour le Doppler ±1 %, Cabinet, rampes automatisées différentes [HEUR, valeurs DOC setBfree]. Pas de wow/flutter natif (Chorus-Ensemble Vibrato à 0,5–1,3 Hz en approximation [TEST]). Sampler : formats REX/ACID/Soundtrack seulement ; Kontakt/EXS non cités en Live 12. Le manuel ne donne aucune recette Rhodes, Clavinet, DX7.
