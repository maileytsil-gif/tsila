# v14 research additions — Sample / Vocal / Break FX

Sources officielles consultées : Ableton Live 12 Clip View/Warp modes/Simpler/Clip Envelopes/Audio Effects ; Xfer Serum 2 Sample/Granular/Spectral/routing ; Waves Vocal Bender/H-Delay ; FabFilter Timeless 3/Volcano 3/Pro-R 2 ; iZotope Stutter Edit 2/VocalSynth 2 ; Native Instruments Maschine Stretch/Kontakt Time Machine Pro/Guitar Rig Transpose Stretch & Grain Delay ; ValhallaDelay/Supermassive. Les comportements constructeur sont `[DOC]`; les recettes et chaînes sont `[HEUR]`; les choix sonores finaux restent `[TEST]`.

# Registre de recherche — v5 familles et sous-types professionnels

Révision : 2026-09-19. Objectif : documenter et transformer en règles opérationnelles les familles **synthé, nappe, drone, stab, riser, impact, pluck, pad et keys**, avec Serum 2 ou Ableton Live 12.

## Xfer Records — Serum 2

### Moteurs de synthèse
Consulté : le manuel décrit pour OSC A/B/C les moteurs Wavetable, Multisample, Sample, Granular et Spectral. Cette architecture sert maintenant à choisir le moteur selon la fonction sonore plutôt que d'utiliser Wavetable par défaut.

Sources :
- https://xferrecords.com/web-manual/serum-2/exploring-sound-design-in-serum
- https://xferrecords.com/manual/serum-2/docs
- https://www.xferrecords.com/products/serum-2

### Routing
Consulté : les oscillateurs et filtres peuvent être routés vers Filter 1/2, Main, Direct, None et vers les bus. La v4 transforme cela en règle de séparation entre couche sèche, texture et traitement spatial.

Source :
- https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter

### Pitch tracking
Consulté : Xfer cite les drones/sons statiques, percussions, noise effects, risers, sweeps et impacts comme usages possibles du pitch tracking désactivé. Le manuel documente aussi une note de référence différente selon le moteur lorsque le tracking est coupé.

Sources :
- https://xferrecords.com/web-manual/serum-2/enabling-pitch-tracking
- https://xferrecords.com/web-manual/serum-2/pitch-bend-tracking

### Granular / Spectral / Sample
Consulté : granular découpe le matériau en grains et vise notamment textures/pads ; Spectral resynthétise/analyse le spectre et offre des contrôles de temps/fréquence ; Sample permet lecture, loop et transformations. Ces capacités alimentent directement les règles nappe/drone/riser/impact.

Source principale :
- https://xferrecords.com/manual/serum-2/docs

## Ableton Live 12 — instruments

### Drift
Consulté : architecture soustractive, deux oscillateurs + bruit, deux enveloppes, Cycling Envelope, LFO avec formes dont Saw Up/Down et enveloppes one-shot, modulation et voice modes. Utilisé pour synthé, stab, pluck et riser.

### Wavetable
Consulté : deux oscillateurs wavetable, sub, deux filtres, Matrix, enveloppes/LFO/MIDI et unison. Utilisé pour synthé, pad et nappe.

### Meld
Consulté : deux moteurs polyphoniques, macros dépendantes des moteurs, filtres, LFO et matrices. Utilisé pour pads/nappes/hybrides.

### Operator
Consulté : quatre oscillateurs avec FM/additif/soustractif, sept enveloppes et pitch envelope. Utilisé pour pluck, keys et synthé digital.

### Analog
Consulté : deux oscillateurs + bruit, deux filtres et amplis, ADSR et LFO. Utilisé pour stabs/pads/synthés classiques.

### Electric / Collision / Tension
Consulté : Electric modélise le piano électrique ; Collision combine mallet/noise et resonators ; Tension modélise une corde avec exciter/damper/body. Utilisés pour keys et plucks organiques.

### Simpler / Sampler / Drum Sampler
Consulté : Simpler One-Shot, Sampler multisampling et modulation, Drum Sampler avec AHD, filtre et neuf playback effects dont Pitch Env, Punch, FM, Ring Mod, Sub Osc et Noise. Utilisés pour stabs/impacts/keys.

Source commune :
- https://www.ableton.com/en/manual/live-instrument-reference/

## Granulator III

Consulté : Ableton décrit Granulator III comme un instrument granular Live 12 avec capture audio, MPE et trois modes de lecture ; le mode Cloud vise les drones/textures expérimentales et la synthèse granulaire se prête aux pads/textures.

Source :
- https://www.ableton.com/en/packs/granulator-iii/

## Ableton Live 12 — Racks et effets

Consulté : Racks à chaînes parallèles et jusqu'à 16 macros ; Auto Filter avec filtres/LFO/envelope follower ; Echo avec deux delay lines, modulation, feedback et reverb ; Hybrid Reverb/Reverb pour les queues ; Roar pour saturation/routages/modulation. Ces fonctions structurent la couche FX de chaque famille.

Sources :
- https://www.ableton.com/en/manual/instrument-drum-and-effect-racks/
- https://www.ableton.com/en/manual/live-audio-effect-reference/

## Ableton Learning Synths

Consulté : fondements envelopes/LFO/oscillators/filters, ainsi que la recette Plucked Bass montrant une amplitude à sustain nul avec decay et un filtre modulé rapidement par enveloppe pour créer l'articulation pluck. La v4 l'utilise comme principe documenté, sans recopier ses réglages comme recette universelle.

Sources :
- https://learningsynths.ableton.com/
- https://learningsynths.ableton.com/en/envelopes/synthesizer-envelopes
- https://learningsynths.ableton.com/recipes/plucked-bass

## Ce qui reste [TEST]

La recherche documentaire ne valide pas :
- le numéro exact de la version Serum 2 installée ;
- le format VST3/AU utilisé ;
- les paramètres réellement exposés à Live ;
- la stabilité/charge CPU du patch final ;
- le fonctionnement de chaque mapping via le bridge LOM/MCP.

Ces points doivent être testés sur la machine avant qu'un skill ne les présente comme opérationnels.


# Extension de recherche v5 — sous-types professionnels

## Serum 2 — pitch, ratios et morphing
Consulté : le manuel Xfer précise que `CRS` est adapté aux sweeps continus et à la modulation/automation de hauteur, et que les modes de pitch incluent Semitones, Harmonics et Ratio. Ces éléments sont utilisés pour les risers tonaux, organ/harmonic stabs et architectures FM/ratiométriques.

Sources :
- https://xferrecords.com/web-manual/serum-2/using-pitch-controls
- https://xferrecords.com/web-manual/serum-2/setting-the-octave-or-semitone-mode

## Serum 2 — macros/modulation
Consulté : Serum 2 dispose de huit macros et le système de modulation a été étendu. La v5 convertit ces capacités en macros d'intention (`TONE`, `MOTION`, `TENSION`, etc.) plutôt qu'en noms de paramètres techniques.

Sources :
- https://xferrecords.com/manual/serum-2/docs
- https://static.xferrecords.com/Serum%202%20What%27s%20New.pdf

## Ableton — sous-types et modélisation physique
Consulté : Collision = mallet/noise + resonators ; Electric = piano électrique modélisé ; Tension = modèle de corde avec exciters/damper/body ; Operator = quatre oscillateurs FM/additif/soustractif. Ces capacités servent directement aux sous-types glass pluck, organic string pluck, electric-piano keys et FM keys.

Source :
- https://www.ableton.com/en/manual/live-instrument-reference/

## Ableton — effets comme moteurs de sound design
Consulté : Auto Filter offre types de filtres, LFO, envelope follower et drive ; Corpus fournit sept modèles de résonateurs ; Echo offre feedback/modulation ; Hybrid Reverb combine convolution et algorithmes ; Roar possède plusieurs étages/routages et feedback. La v5 les utilise comme fonctions précises pour risers, impacts, drones et textures.

Source :
- https://www.ableton.com/en/manual/live-audio-effect-reference/

## Granulator III — Cloud et texture
Consulté : Ableton indique que Granulator III peut capturer l'audio en temps réel, propose Classic/Loop/Cloud, et que Cloud vise les drones et textures expérimentales. La v5 crée des sous-types granular Cloud, cinematic nappe/pad et granular riser à partir de ces capacités.

Source :
- https://www.ableton.com/en/packs/granulator-iii/

## Racks — layering/morphing
Consulté : les chaînes d'Instrument Rack sont parallèles et les Racks offrent jusqu'à 16 macros, avec plages Min/Max et mapping de plusieurs paramètres. La v5 formalise les rôles CORE/BODY/ATTACK/AIR/TEXTURE/TAIL et les morphs entre couches.

Source :
- https://www.ableton.com/en/manual/instrument-drum-and-effect-racks/


## v6 — Producer Intelligence (2026-09-19)

Recherche éditoriale et interviews sur David Guetta, Martin Garrix, Calvin Harris, Tiësto, Skrillex, FISHER, Oliver Heldens, Don Diablo, John Summit et Dom Dolla. Les déclarations directes sont [DOC]. Les conclusions de style sont [ANALYSIS], les transpositions Serum/Ableton [HEUR], et les métriques non inspectées [TEST]. Voir `producer-intelligence/SOURCES.md`.


## v7 — Deep Track Intelligence (19-09-2026)

Ajout de 15 références avec métadonnées de versions vérifiées sur Beatport. Les analyses de structure, groove et sound design sont explicitement marquées [ANALYSIS]/[HEUR] et ne sont pas présentées comme des observations de stems ou de projets originaux. Voir `producer-intelligence/SOURCES-v7.md`, `deep-track-analysis-method.md` et `deep-tracks/`.


## v8 — Kick / 808 / Low-End — recherche fabricants (19-09-2026)

Sources officielles consultées : Serum 2 manual (oscillateurs, routage, pitch tracking), Ableton Live 12 manual (Operator, Drum Buss, Roar, Compressor, Utility), FabFilter help (Pro-Q 4, Pro-C 3, Saturn 2, Pro-L 2), Waves product/manual pages (Renaissance Bass, CLA-76, H-Comp, J37), iZotope Neutron 5 et Trash, Native Instruments Transient Master / Supercharger GT / Massive X, ValhallaRoom / VintageVerb / Supermassive / Delay.

Décision méthodologique : aucun temps de decay, fréquence fondamentale, plage de pitch-drop ou quantité de drive n'est attribué aux fabricants. Ces valeurs sont rangées `[HEUR]` et doivent être ajustées au BPM, à la tonalité, au groove et à la bassline. Les fonctions de plugins explicitement décrites par les fabricants sont `[DOC]`.


## v9 — Bass Design Intelligence — 19 septembre 2026

Sources officielles consultées : Xfer Records Serum 2 web manual (sound generators, routing, pitch modes, pitch controls, filters, modulation/macros), Ableton Live 12 manual (Operator/Wavetable/Meld, Saturator/Roar/Utility/sidechain), FabFilter online help (Saturn 2, Pro-Q 4, Pro-C 3), Waves manuals/pages (Renaissance Bass, MaxxBass, Smack Attack), iZotope Neutron 5 + Trash documentation, Native Instruments Massive X/Transient Master/Supercharger GT manuals, Valhalla Delay/Supermassive documentation.

Les paramètres créatifs chiffrés des recettes sont marqués `[HEUR]`. Les capacités de produit sont `[DOC]`. Les résultats kick/bass, mono, phase, translation et bridge sont `[TEST]`.


## v10 — Modern Pop & Electronic Music Theory — 19 septembre 2026

Sources documentaires consultées : Ableton Learning Music (notes/scales, chords, basslines, song structure), Ableton Making Music (Catalog of Attributes), Live 12 Manual/Help (Scale Awareness, MIDI Transformations/Generators, MIDI Effects), Berklee Online (songwriting tools/prosody, voice leading, hooks, chord progressions), Recording Academy/GRAMMY (Amy Allen 2025, Daniel Nigro 2025, Cirkut 2026, Jack Antonoff historique, interviews de FINNEAS, Dan Nigro, Ryan Tedder, Romy/Fred again..), ainsi que des interviews spécialisées MusicRadar, Sound On Sound, Music Week et Rolling Stone UK.

Décision méthodologique : le corpus de créateurs n'est pas un classement des « meilleurs ». Les récompenses et informations de carrière sont `[DOC]`, les propos explicitement attribués `[ATTRIB]`, les conclusions stylistiques `[ANALYSIS]`, les règles de composition proposées `[HEUR]` et les choix à valider dans le projet `[TEST]`.

Voir `modern-pop-electronic-music-theory/references/sources.md`.


# v11 research update

## Official/educational sources verified
- Ableton Live 12 Manual — MIDI Tools: Transform vs Generate, scale-aware pitch controls, Stacks/Rhythm/Seed/Shape and transformations.
- Ableton Live Concepts / Clip View — Scale Mode, Fold/Highlight Scale and pitch-aware tools.
- Ableton Making Music — Catalog of Attributes for extracting abstract features rather than copying.
- Berklee Online — voice-leading via common tones/economic motion and inversions.
- Berklee Online — harmonic progressions can remain simple; contrast can also come from harmonic rhythm or a single changed chord.
- Berklee Online — melody design through motif, repetition and contrast; hooks benefit from contrast and repetition.

## v11 interpretation
All progression lists, voicings, motif cells, bass cells and MIDI clips were created as original teaching templates. They are not claims about what any named producer uses.


# v12 — Composer / Producer Director

La v12 n'ajoute pas de nouvelle affirmation constructeur : elle orchestre les preuves et règles déjà documentées dans les skills v3–v11. Les comportements Ableton/Serum/plugins restent gouvernés par leurs `documentation-map`, `source-authority` et fichiers sources respectifs. Le Director ajoute des règles d'orchestration `[HEUR]`, des gates et des blueprints originaux.


# v13 — Drums & Electronic Percussion

## Ableton
- Drum Sampler: one-shot playback, AHD, pitch, filter, modulation, playback effects. `[DOC]`
- Drum Synths / Max for Live: DS Clang, Clap, Cymbal, FM, HH, Snare, Tom. `[DOC]`
- Drum Buss: body/character/glue, compression/distortion/drive. `[DOC]`
- Collision: physical-modeling percussion/mallet source. `[DOC]`

## Serum 2
- OSC A/B/C: Wavetable, Multisample, Sample, Granular, Spectral. `[DOC]`
- Noise oscillator as stereo sample player/modulator. `[DOC]`
- Main/Direct/Filter/None + buses routing. `[DOC]`

## Third-party
- Waves Smack Attack: attack/sustain transient shaping for percussive material. `[DOC]`
- FabFilter Pro-Q 4 dynamic/spectral EQ, Saturn 2 multiband distortion/modulation, Pro-C 3 dynamics. `[DOC]`
- iZotope Neutron Transient Shaper/Exciter/Sculptor capabilities. `[DOC]`
- NI Battery 4 sampling/routing/effects and Transient Master attack/sustain. `[DOC]`
- ValhallaRoom/VintageVerb/Delay for rooms, plates, digital tails, pitch/reverse/diffusion. `[DOC]`

Genre values and recipes remain `[HEUR]`; all contextual balance/timing decisions are `[TEST]`.


# v15 — Transitions & FX Director — 19 septembre 2026

## Ableton Live 12 [DOC]
Audio Effect Reference consultée pour Auto Filter, Beat Repeat, Echo, Grain Delay, Hybrid Reverb, Redux, Roar, Shifter et Spectral Time. Ces appareils sont assignés à des fonctions spécifiques de transition, jamais utilisés comme simple décoration.
Source : https://www.ableton.com/en/manual/live-audio-effect-reference/

## Serum 2 [DOC]
Documentation Xfer consultée pour les moteurs Wavetable/Multisample/Sample/Granular/Spectral, LFO/envelopes, désactivation du pitch tracking sur risers/sweeps/impacts/noise FX et routing Filter/Main/Direct/None.
Sources : https://xferrecords.com/web-manual/serum-2/exploring-sound-design-in-serum ; https://xferrecords.com/web-manual/serum-2/enabling-pitch-tracking ; https://xferrecords.com/web-manual/serum-2/routing-an-oscillator-or-filter

## FabFilter [DOC]
Timeless 3 : Freeze modulable, Tape/Stretch read modes, pitch feedback, diffusion/lo-fi/dynamics et modulation. Volcano 3 : XLFO/EG/EF/MIDI/XY. Pro-R 2 : Freeze, Ducking, Auto Gate, predelay sync et Decay Rate EQ.

## Waves [DOC]
MetaFilter : LFO, 1–16 step sequencer, envelope/sidechain, delay, saturation/bitcrush. H-Delay : ping-pong/feedback/filter/tempo sync ; feedback >100% peut construire le niveau. SoundShifter : time scaling et pitch indépendants.

## iZotope / NI / Valhalla [DOC]
Stutter Edit 2 : Buffer/Stutter/Gestures/quantized rate. Guitar Rig Transpose Stretch : granular stretch/pitch jusqu'au freeze. ValhallaDelay : reverse pitch/ducking/diffusion ; Supermassive : attack/density/decay/warp variables.

Toutes les recettes de durée, densité, pitch range, vacuum et layering sont `[HEUR]` et doivent être validées `[TEST]` dans le vrai morceau.

## v16 — Modern Jazz / Chill-Out / Jazz-Funk
Sources principales vérifiées : Berklee Harmony, Berklee voicing/modal harmony/tension-resolution/improvisation/rhythmic phrasing/funk drums/R&B bass/Funk-R&B soloing ; Ableton Groove Pool et Live 12 Humanize ; interviews/pages de référence Herbie Hancock, Robert Glasper, Michael League. Les paramètres de timing et recettes stylistiques restent `[HEUR]`/`[TEST]`.


# v17 — Afro / Caribbean / Latin / Detroit

Sources consultées : Berklee PULSE/Online pour clave, montuno, tumbao et piano latin ; Smithsonian Folkways pour bell patterns, bomba/plena, Jamaica, calypso, merengue, samba/carimbó et cumbia/Colombia ; Beatportal/Beatport pour Afro House/Amapiano/house-scene context ; Detroit Historical Society, Red Bull Music Academy et Smithsonian pour Detroit techno, Belleville Three, Carl Craig et Drexciya.

Décision méthodologique : aucune recette MIDI électronique n'est présentée comme transcription traditionnelle. Les guides clave/tresillo sont distingués des adaptations `[HEUR]`.


## v18 Technical Integration
Aucune nouvelle affirmation musicologique majeure ajoutée. La v18 transforme les connaissances documentées existantes en contrats structurés et conserve leur provenance via source IDs. Les nouveaux microtimings, exemples et plans sont `[HEUR]`/`[TEST]` sauf indication contraire.
