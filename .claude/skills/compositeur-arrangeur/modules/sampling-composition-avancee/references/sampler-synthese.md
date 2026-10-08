# Sampler d'Ableton Live : synthèse de 30 tutoriels

Synthèse du 05/10/2026 du corpus `tutoriels-sampler.md` (SA-01 à SA-30). L'étude a été faite dans Claude in Chrome sur le Mac. Les transcriptions ont été lues, le son coupé : **rien n'a été entendu**. Ce que le corpus « dit » est marqué [SOURCE SA-xx]. Mon interprétation est marquée (interp.). Une reconnaissance vocale douteuse est marquée [ASR ?]. Les vidéos couvrent Live 9 à Live 12 ; le round robin n'existe que dans Live 12 [SOURCE SA-05, SA-10]. Le corpus voisin sur Simpler est `tutoriels-simpler.md` ; la capture audio est dans `../../../sound-designer-serum/modules/resampling/GUIDE.md` ; les paramètres exposés des instruments natifs sont dans `../../../sound-designer-serum/modules/vst-sound-design/references/instruments-natifs.md`.

## Ce que dit le corpus avant tout

- Sampler sert d'abord à **tenir une note** : boucle de sustain, crossfade, Snap au passage par zéro. Presque tous les tutoriels y passent [SOURCE SA-01, SA-07, SA-20, SA-21, SA-25].
- L'onglet Sample se règle **par sample** ; Pitch/Osc, Filter/Global et Modulation sont **communs** à tout le Sampler [SOURCE SA-10, SA-30]. D'où deux Samplers quand deux couches demandent deux enveloppes [SOURCE SA-09].
- Le point d'entrée habituel : glisser l'audio sur une piste MIDI, ce qui crée un Simpler, puis clic droit > convertir en Sampler [SOURCE SA-22, SA-27, SA-29, SA-30].
- Les vidéos de basse et de pad accordent le sample au Tuner, puis règlent Root Key et Detune. Sans cela, la FM interne sonne faux [SOURCE SA-25, SA-26, SA-27].
- Le **resampling** revient sans cesse : imprimer une variante, la recharger, recommencer [SOURCE SA-06, SA-12, SA-14, SA-15, SA-28].

## Gestes de base

| Geste | Comment | Sources |
|---|---|---|
| Borner la lecture | Drapeaux Sample Start / End ; Snap = calage au passage par zéro contre les clics | SA-01, SA-02, SA-04 |
| Accorder | Root Key = note réelle du sample ; Detune pour finir ; Tuner sur la piste | SA-07, SA-25, SA-27 |
| Key tracking | Scale : 100 % normal, 0 % même hauteur partout, négatif = inversé | SA-02, SA-03, SA-09, SA-23 |
| Boucle de sustain | Sustain Mode Loop (forward) ou Back-and-Forth ; Link colle Sample Start au Loop Start | SA-02, SA-04, SA-13 |
| Boucle de release | Release Mode : seconde boucle après relâchement ; exige un Release d'enveloppe long | SA-01, SA-03, SA-19 |
| Lisser une jonction | Crossfade de boucle ; Detune propre à la boucle | SA-02, SA-03, SA-20 |
| Zones de touches | Key Zone Editor, fondus de zone Lin ou Pow (puissance constante) | SA-01, SA-03, SA-05 |
| Zones de vélocité | Velocity Zone : jouer fort = autre sample | SA-03, SA-09, SA-29 |
| Sample Select | Sélecteur 0–127, comme un Chain Selector ; clic droit > Map to Macro | SA-03, SA-05, SA-15 |
| Répartir les plages | Clic droit > Distribute Ranges Equally ou Around Root Key | SA-07, SA-08, SA-09 |
| Round robin (Live 12) | Modes Forward / Backward / Other / Random ; Reset relance le cycle | SA-05, SA-10 |
| Moduler le départ | LFO 2 ou 3 → Sample Offset, forme Random | SA-06, SA-10, SA-23 |
| Moduler la boucle | Aux Env → Loop Start, LFO Random → Loop Length | SA-14 |
| FM / AM interne | Pitch/Osc : volume de l'oscillateur = profondeur ; Coarse, Fine, Fixed | SA-17, SA-25, SA-26 |
| Enveloppe de hauteur | Pitch Envelope : Amount en demi-tons, Decay | SA-25, SA-28, SA-30 |
| Shaper et filtre | Shaper (Soft/Hard/Sine/4-bit) avant ou après le filtre ; filtre Morph, MS2 | SA-02, SA-05, SA-30 |
| Aux Envelope | Assignable presque partout : Shaper Amount, Filter Morph, Pitch, LFO Rate | SA-06, SA-29, SA-30 |
| Remplacer les samples | Hot-swap ; glisser un .adv sur un Sampler change la carte, garde les réglages | SA-05, SA-29 |
| Preset de slicing | Sampler vide, Voices = 2, filtre off, sauvé en User Library > Slicing | SA-11, SA-12 |

## Valeurs dites

| Paramètre | Valeur | Source |
|---|---|---|
| Pitch Bend Range | 5 demi-tons par défaut, jusqu'à 24 | SA-02 |
| Pitch Bend Range réglé | 12 demi-tons | SA-01, SA-04 |
| Pitch Bend Range pour « whips » | 24 (max) | SA-14 |
| Volume par défaut de Sampler | −12 dB | SA-09, SA-14 |
| Transposition max conseillée | ±7 demi-tons | SA-07 |
| Transposition max conseillée | ±2 demi-tons (un sample tous les 3 demi-tons) | SA-08 |
| Scale | 0 à 200 %, négatif jusqu'à −200 | SA-03 |
| Random Pan | 100 % = totalement aléatoire | SA-04 |
| Velocity Zone exemple | 100–127 | SA-01 |
| Velocity mezzo (cithare) | ≈ 50–104 [ASR ?] | SA-09 |
| Sample Select (fondu) | 40 = un peu d'accord, 104 = surtout accord, 127 = accord seul | SA-03 |
| Couches de vélocité enregistrées | 4 : max, ~100, mezzo, basse | SA-09 |
| Glide 808 | ≈ 120 ms | SA-20 |
| LFO Attack | 1 s ; 3,5 s | SA-02 ; SA-06 |
| LFO Offset | 90 / 180 / 270 degrés | SA-06 |
| LFO 3 → Sample Offset | ~74 % | SA-23 |
| FM Coarse (basse) | 0,25 ou 0,5 | SA-14 |
| FM Coarse | 1 (caractère), 2 (« plus carré »), 0,5 essayé | SA-26 |
| FM Coarse = 1 | ~260 Hz pour C3 (C3 = 60) | SA-10 |
| FM Fixed (kick) | ≈ 340 Hz ; ×10 = 3 400 Hz, trop métallique | SA-30 |
| Pitch Envelope (kick) | +12 demi-tons, essai +48 | SA-30 |
| Pitch Envelope (basse jungle) | ≈ 6 demi-tons | SA-25 |
| Pitch Envelope (neuro) | +12, Decay ≈ 3 s ; puis −100 % ; puis 24 | SA-28 |
| Aux Env → Osc Pitch (riser) | −100 | SA-17 |
| Aux Env → Shaper Amount | 100 %, Sustain 0 | SA-30 |
| Cutoff de base (basse) | ~285 Hz | SA-26 |
| Notch (neuro) | ~1 kHz, 12 dB ; puis 24 dB | SA-28 |
| Drive (circuit OSR) | ≈ 10 | SA-29 |
| Detune des copies de zone (reese) | +9 / −9 cents | SA-26 |
| Voices | 1 (mono) ; 2 (slicing) ; 3 pour 3 samples ; 5 ; 6 | SA-25 ; SA-11 ; SA-26 ; SA-23 ; SA-30 |
| Transpose de clip (riser) | −12 → +12 sur 4 mesures | SA-16 |
| Gain staging des breaks | −18 dB RMS | SA-11, SA-12 |
| Fréquence de « C5 » | 523,25 Hz, soit MIDI 72 = C4 dans Live [CALCUL] : la vidéo nomme en notation scientifique | SA-22 |
| Grain Size (mode Texture) | 32 | SA-12 |

- Le Pitch Bend Range par défaut (5) n'est dit que par SA-02 (interp. : à relire dans Live).
- Les deux limites de transposition (±7 et ±2) se contredisent. Elles visent des usages différents : flûte (SA-07), rendu « fidèle » d'un pad (SA-08).

## Fiches par usage

### Multisampling et round robin
- Geste : glisser tous les samples, régler chaque Root Key, puis Distribute Ranges Around Root Key [SOURCE SA-07, SA-08].
- Couches de vélocité : enregistrer là où le son change, pas 128 vélocités [SOURCE SA-09].
- Après Normalize Volumes, doser Volume < Velocity pour rendre la dynamique [SOURCE SA-09].
- Round robin Random : chaque note d'un accord prend un sample différent [SOURCE SA-10]. Reset toutes les demi-mesures = motif qui recommence [SOURCE SA-05].
- « 128s » : au moins 128 sons répartis, un par touche ou par valeur [SOURCE SA-05].
- Lire d'abord : SA-08 (méthode), SA-09 (acquisition), SA-05 et SA-10 (round robin).

### Breaks
- Geste : traiter, imprimer, Slice to New MIDI Track en « Transient » avec un preset Sampler perso [SOURCE SA-11, SA-12].
- Clip : quantize 1/16, Legato, vélocités au max ; ajuster Start/End de chaque tranche [SOURCE SA-11, SA-12].
- Macros dites : Pitch, Decay, Sustain, Release, Volume [SOURCE SA-11, SA-12].
- Staccato : raccourcir toutes les notes MIDI [SOURCE SA-11].
- Spécifique à Sampler : Sustain Mode par tranche, back-and-forth sur une cymbale [SOURCE SA-11].
- Lire d'abord : SA-11, puis SA-12 (version longue).

### Stutter, glitch, sélecteur
- Stutter vocal : LFO → Volume à 100 %, forme carrée, Rate monté ; boucle back-and-forth [SOURCE SA-13].
- Un nouveau sample garde la modulation mais réinitialise le Sustain Mode [SOURCE SA-13].
- Glitch : boucle très courte + Link, Aux Env → Loop Start, LFO Random → Loop Length [SOURCE SA-14]. Résultat différent à chaque passage : imprimer.
- Sélecteur : ~40 percussions en Sample Select sur une macro, tournée pendant un resampling [SOURCE SA-15].
- Lire d'abord : SA-14, puis SA-13 et SA-15 (couverture faible, voir Limites).

### Risers et transitions
- Riser de basse : queue de reverb figée, bouclée avec crossfade, re-flattenée, Transpose −12 → +12 [SOURCE SA-16].
- Riser tonal : oscillateur Fixed, Aux Env → hauteur de l'oscillateur à −100 [SOURCE SA-17].
- Le riser de SA-17 « garde la tonalité du morceau » (dit, non vérifié).
- Lire d'abord : SA-17, puis SA-16.

### Voix
- Pad de voix : une voyelle par Sampler, boucle back-and-forth + crossfade, Detune pour recentrer sur C [SOURCE SA-18].
- Rack de voyelles : Chain Selector réparti puis mappé sur Macro 1 [SOURCE SA-18].
- Mot bégayé : boucle de sustain sur un mot, boucle de release sur un autre (« want want want ») [SOURCE SA-19].
- Sustain infini : zone à volume et hauteur stables, petite boucle, Snap [SOURCE SA-20].
- Lire d'abord : SA-20 (règles), SA-18, SA-19.

### Pads, textures, oscillateurs
- Une note de piano : boucle dans la partie tenue, crossfade, Attack longue, Release long [SOURCE SA-21].
- Texture accordée : boost très étroit à la fréquence d'une note avant l'import [SOURCE SA-22].
- Pad multicouche : Voices ≥ nombre de couches ; field recordings à Scale 0 % [SOURCE SA-23].
- Oscillateur maison : Start juste avant une montée, boucle de ~3 cycles, Loop End réglé aux flèches [SOURCE SA-24].
- Sur ces cycles courts, le crossfade crée un « wah-wah » : à éviter [SOURCE SA-24].
- Lire d'abord : SA-23, puis SA-24.

### Basses et resampling
- Micro-boucle = forme d'onde « like a wavetable » ; sa position change le timbre [SOURCE SA-26, SA-27].
- FM : samples parfaitement accordés, sinon faux [SOURCE SA-26]. Volume de l'oscillateur = intensité [SOURCE SA-26].
- Basse mono : Voices = 1 [SOURCE SA-25]. Key tracking du filtre à 100 % [SOURCE SA-25].
- Neuro : même fichier dans plusieurs Samplers, Starts différents, Reverse, Pitch Env extrêmes [SOURCE SA-28].
- Clics de boucle : boucle plus courte et Crossfade à zéro a mieux marché [SOURCE SA-25].
- Lire d'abord : SA-25, SA-26, puis SA-14 et SA-28.

### Kick et batterie
- Kick : FM Fixed ≈ 340 Hz, enveloppe très courte ; Pitch Env +12 [SOURCE SA-30].
- Distorsion de l'attaque seule : Aux Env → Shaper Amount 100 %, Sustain 0 [SOURCE SA-30].
- Layering : 3 kicks + une snare dans les zones, Voices au moins égal au nombre de couches [SOURCE SA-30].
- Aligner la montée des formes d'onde contre les problèmes de phase [SOURCE SA-30].
- Limite dite : l'ADSR global est commun à toutes les couches [SOURCE SA-30].
- Pour un kick de signature sous 124 BPM, le projet impose Serum 2 : Sampler sert ici aux couches ou aux tests (interp.).

## Limites

- **Captures non faites** : chaque fiche du corpus liste des points « à vérifier à l'écran ». Aucune capture n'a été prise. Positions de boucle, valeurs de Crossfade et mappings restent à relire dans Live.
- **Transcription automatique** : presque toutes en anglais auto. SA-15 a une ASR française très approximative. SA-17 a été lu via une traduction française. SA-09 n'a été lu que jusqu'à ~38:00, SA-05 jusqu'à ~23:30.
- Points [ASR ?] : « Sylenth1 » et la plage F#3 → D4 (SA-09), « Culprate » (SA-14), le type de filtre « OSR ? » (SA-23), « N O/LP » (SA-28).
- **Versions de Live** : beaucoup de versions sont déduites de la date (interp.). Le round robin est Live 12 seulement. Les circuits de filtre datent de Live 9.7/10 [SOURCE SA-29]. Le menu Interpolation varie selon les vidéos (« Good », « Normal », « Best »).
- **Couverture faible** : stutter dédié à Sampler, risers, vocal chops par découpage, Drum Sampler de Live 12 (aucun retenu).
- **Effets natifs de Live** : le corpus utilise Glue Compressor, Channel EQ, Auto Filter, Reverb, Resonator, Grain Delay, Echo, Erosion, Roar, Drum Buss, Redux. Règle du projet : pas de nouvel effet natif de Live dans les chaînes de mix. Les remplacer par les plug-ins tiers de l'utilisateur. L'instrument Sampler est toléré. Son filtre et son Shaper internes font partie de l'instrument (interp.).
- **Pas d'écoute** : « sounds fat », « smooth », « organique » sont les mots des tutoriels. Les tests d'écoute reviennent à l'utilisateur.
- Numérotation des notes : C3 = 60 (Ableton), le numéro MIDI fait foi. La plupart des noms de notes du corpus semblent suivre Live (interp.), mais pas tous : le « C5 » à 523,25 Hz de SA-22 est le C4 de Live (MIDI 72). Recalculer la note depuis la fréquence quand elle est donnée.
