# Serum 2 — cartographie complète

Carte de tout ce que contient Serum 2 (Xfer Records, VST3/AU/AAX ; version installée ici : VST3 2.1.5, dernier changelog lu : 2.0.24 du 13 novembre 2025) : architecture, flux du signal, chaque page et chaque panneau, chaque paramètre avec sa plage, les listes de menus complètes, les fichiers, et ce que Live voit. Rédigée le 24 septembre 2026 à partir des sources ci-dessous ; les fiches détaillées existantes ne sont pas recopiées mais pointées.

## Étiquettes de preuve

| Étiquette | Sens |
|---|---|
| `[DOC]` | Manuel officiel Serum 2 (354 pages, dépouillé dans `serum2-fx-clip-arp.md`, `moteurs-synthese.md`, `serum2-automation-et-migration.md`), **« What's New in Serum 2 »** (PDF officiel du 17 mars 2025, `../../../../corpus/constructeur/static-xferrecords-com-serum-202-20what-s-20new-pdf-texte.md`), pages du manuel web (`../../../../corpus/constructeur/xferrecords-com-web-manual-serum-2-using-the-serum-keyboard.md`, `…-using-knobs-and-sliders.md`, `…-enabling-pitch-tracking.md`), manuel Serum 1 (`../../../../corpus/constructeur/xfer-serum-1-manuel-1-0-1.md`), changelog Xfer (`../../../../corpus/constructeur/xfer-serum-changelog-2-0-24-a-1-10.md`) |
| `[BIN]` | Lu dans le binaire Serum2.vst3 2.0.23 ou dans le format de fichier : noms internes, plages min/max, défauts, listes de menus (`../../../../corpus/constructeur/pycabbage-flp-extract-fxp-serum2-runtime-tables.md`, `…-serum2-state-format.md`, `../../../../corpus/constructeur/serum2vital-formats-btesser.md`, `../../../../corpus/constructeur/btesser-serum-tables-affichage-filtres-warps-distorsions.md`) |
| `[USINE]` | Statistiques des 626 presets d'usine décodés (`../../../../corpus/cuivres/serum-2-presets-usine-corpus-parametres.md`, `../../../../corpus/constructeur/rich6feet-serum-factory-mining-report.md`) : plages observées, valeurs de menus réellement utilisées |
| `[EXTRAIT]` | Résumé de recherche web (site constructeur ou tutoriel lu par extraits, page non téléchargeable depuis le conteneur) |
| `[LOCAL]` | Constaté dans cette installation, sur ce Mac (`../../vst-sound-design/references/serum2.md`) |
| `[HEUR]` | Déduction ou pratique, à vérifier à l'oreille |
| `[TEST]` | À vérifier dans Serum avant de s'y fier |
| **MUET** | Aucune source ne le dit |

Un nom entre backticks en `kParamXxx` est le nom interne du paramètre dans le fichier `.SerumPreset` `[BIN]` ; il sert à lire un preset, pas à parler à l'utilisateur.

---

## 1. Architecture et flux du signal

```
MIDI in ──► [KEYBOARD : Transpose · Key · Scale · Swing · OSC Mapping]
        ──► [ARP (12 slots)] ──► [CLIP player (12 clips)] ──► voix de synthèse ──► MIDI out (Off / Clip Player / On)

Par voix :
  SUB ─┐                                 ┌─► FILTER 1 ─┐
  OSC A ┤  routage par canal :           │             ├─► FILTER 1→2 (série) ou 1 ∥ 2 (parallèle)
  OSC B ┤  Filter (répartition F1/F2)  ──┤             │
  OSC C ┤  Main · Direct · None          └─► FILTER 2 ─┘
  NOISE ┘        │                                     │
                 │ envois BUS 1 / BUS 2 (par osc et par filtre)
                 ▼                                     ▼
Somme des voix ─► rack FX MAIN ─────────────────────► MASTER VOLUME ─► sortie
                  rack FX BUS 1 ─► Main / Direct / Bus 2
                  rack FX BUS 2 ─► Main / Direct / Bus 1
Direct = contourne filtres ET effets.
```

Faits structurants `[DOC]` : 5 sources par voix (SUB, A, B, C, NOISE) ; A, B et C ont chacun 5 moteurs (Wavetable, Sample, Multisample, Granular, Spectral) ; 2 filtres par voix, série ou parallèle ; 4 enveloppes ; 10 LFO ; 8 macros ; 64 slots de matrice ; 13 effets + 3 splitters sur 3 racks (MAIN, BUS 1, BUS 2), plusieurs instances du même effet possibles, ordre libre. Les effets opèrent sur **la somme des voix**, pas par voix (« paraphonique », manuel p. 159). N'importe quel oscillateur ou filtre peut être **source de modulation** (audio-rate).

Le fichier d'état `[BIN]` reflète exactement cette structure : 162 sections, `Oscillator0..4` (A, B, C, NOISE = 3, SUB = 4), `VoiceFilter0..1`, `Env0..3`, `LFO0..9`, `Macro0..7`, `ModSlot0..63`, `FXRack0..2`, `RoutingSlot0..6` (5 sources + 2 filtres), `Global0`, `VoicePanel0`, `Arp0`, `ArpClip0..11`, `MidiClip0..11`, `ClipPlayer0`, `PitchQuantizer0`, `RetriggerState0`, `LFOPointModBus0..15`.

---

## 2. Interface : fenêtre, onglets, zones fixes

### 2.1 Fenêtre `[LOCAL]` `[DOC]`

- Redimensionnable jusqu'à 200 % (coin ou menu logo) `[EXTRAIT]`. Sur ce Mac, la fenêtre pilotée par clics fait **1190 × 759** ; toutes les coordonnées ci-dessous sont dans cette capture `[LOCAL]`.
- Ce qui passe en arrière-plan depuis Live : **toggles** (SUB, OSC, MONO, LEGATO), **onglets**, **navigateur de presets**, double-clic de preset. Ce qui ne passe pas : saisie d'une valeur (le champ s'ouvre au double-clic mais Entrée n'arrive pas), glisser d'un bouton → le dire à l'utilisateur ou passer en plein écran `[LOCAL]`.
- Undo/redo complet (menu logo) `[EXTRAIT]`. Tooltips au survol, clic droit = menu contextuel sur tout contrôle `[DOC]`.

### 2.2 Les cinq onglets `[DOC]` `[LOCAL]`

| Onglet | Coordonnées (x, y) | Contenu |
|---|---|---|
| **OSC** | (199, 50) | Page principale : SUB, OSC A, OSC B, OSC C, NOISE, FILTER 1, FILTER 2 |
| **MIX** | (266, 50) | Mixer : niveaux, pan, routage de chaque source et filtre, envois BUS 1/2, sorties des bus (§ 5) |
| **FX** | (334, 50) | Trois racks d'effets, 13 modules + 3 splitters (§ 8) |
| **MATRIX** | (403, 50) | Les 64 slots de modulation en liste : source, aux, destination, quantité, courbes (§ 7.4) |
| **GLOBAL** | (470, 50) | Voicing, portamento, qualité, accordage, MPE, préférences, réglages d'unisson et d'oscillateur (§ 9) |

### 2.3 Zones fixes, quel que soit l'onglet

- **Haut** : nom du preset avec flèches ‹ › ; icône liste (1010, 36) ouvre le **navigateur** (arbre Factory › Arp / Bass / Bell / … / Drum, double-clic pour charger) `[LOCAL]` ; menu logo (préférences, redimensionnement, undo, dossier des presets) `[EXTRAIT]`.
- **Bas gauche** : panneau des **enveloppes** (tuiles ENV 1–4 ; lectures ATK / HOLD / DEC / SUS / REL ≈ x 200 / 255 / 308 / 362 / 413, y 593 pour ENV 1) `[LOCAL]`.
- **Bas centre** : panneau des **LFO** (tuiles LFO 1–6 ; **7–10 n'apparaissent qu'après usage du LFO 6**, manuel) `[DOC]`, avec graphe dessinable et ses commandes (§ 7.2).
- **Bas droite** : **MACRO 1–8**, **voicing** (MONO (1058, 627), LEGATO (1058, 653), POLY) et **portamento** (PORTA (1081, 720), curve, Always, Scaled) `[LOCAL]` `[DOC]` ; à côté, le panneau **Velocity/Note** (« more modulation options ») et les **molettes** pitch et mod à l'écran `[DOC, What's New p. 4]`.
- **Clavier** en bas avec ses trois modes d'affichage, KEYBOARD / CLIP / ARP (touches vertes = clips, violettes = arps) et ses réglages Transpose · Key · Scale · Swing · OSC Mapping (§ 10) `[DOC]`.
- Sur la page OSC, interrupteurs marche/arrêt : SUB (11, 101), OSC A (86, 101), OSC B (356, 101), NOISE (896, 101), FILTER 1 (996, 101) `[LOCAL]`. OSC C et FILTER 2 : **MUET** sur leurs coordonnées (à relever sur une capture).

### 2.4 Gestes sur les boutons, menus contextuels, MIDI Learn `[DOC, manuel web « Using Knobs and Sliders »]`

- Glisser vertical ou horizontal ; **Shift** = réglage fin ; molette de la souris = ajustement sans pop-up ; **double-clic** = champ texte pour saisir la valeur exacte ; **⌘-clic** (Ctrl-clic Windows) = **Reset Control** (valeur par défaut).
- **Clic droit** sur presque tout contrôle : choisir une ou plusieurs sources de modulation (ENV 1, LFO 2…), bypass ou retrait d'un modulateur, retrait de tous ; **Reset Control** ; **MIDI Learn** (attend un CC, l'assignation est sauvée avec le preset mais **ne se recharge que si la préférence « Load MIDI Map from Preset » est activée**, désactivée par défaut) ; **Lock Parameter** (la valeur ne change plus au chargement d'un preset, reste réglable à la main).
- Carte MIDI par défaut : menu principal › Save MIDI Map › `Serum 2 Presets/System/MIDI CC Maps/default.SerumMIDIMap`, chargée à chaque nouvelle instance et à Init Preset. Dans une session DAW, les CC sont sauvés et rappelés avec la session.
- **Menu d'un module** (clic droit sur l'étiquette OSC A/B/C, SUB, NOISE, FILTER) : Lock, Initialize, Copy (avec ou sans modulations), **Enable Pitch Tracking**, **Pitch Bend Tracking** `[DOC, sommaire du manuel web]`.
- Navigation rapide des presets : survoler le menu des presets et tourner la molette `[DOC, What's New p. 7]`.

---

## 3. Page OSC : les sources

### 3.1 Paramètres communs à OSC A, B et C `[DOC]` `[BIN]`

| Contrôle | Plage | Défaut | Interne | Notes |
|---|---|---|---|---|
| Marche/arrêt | on/off | A on, B/C off | `kParamEnable` | Un osc éteint ne coûte rien en CPU |
| Moteur | Wavetable · Sample · Multisample · Granular · Spectral | Wavetable | `kParamType` (`kOsc_MultiSample`, `kOsc_Sample`, `kOsc_Granular`, `kOsc_Spectral`) | Menu en tête du panneau |
| LEVEL | 0–100 % (−∞ à 0 dB) | 100 % | `kParamVolume` 0–1 | |
| PAN | −50 … +50 | 0 | `kParamPan` | |
| OCT / SEMI / FINE | −4…+4 / −12…+12 / −100…+100 cents | 0 | `kParamOctave`, `kParamPitch`, `kParamFine` | Séparés pour être modulables un par un |
| CRS (coarse) | −64…+64 demi-tons | 0 | `kParamCoarsePit` | Cible de modulation continue (sirène, LFO sur la hauteur) |
| Pitch track | on/off (clic droit sur l'étiquette › Enable Pitch Tracking) | on | `kParamPitchTrack` | Off : hauteur fixe ; **les oscillateurs Sample, Multisample, Granular et Spectral jouent alors C3 (note 60), le Wavetable joue C-2 (note 0), ce qui en fait un LFO** `[DOC, manuel web]` ; drums, drones, bruit, textures |
| Mode d'accordage (Tuning Modes) | **Semitone · Harmonics · Ratio · Step** (« step modes for octaves and semitones ») `[DOC, What's New p. 7]` | Semitone | `kParamPitchMode` (`Ratio`, `Harmonics`), `kParamPitchRatio` −1…24, `kParamHzOffset` −1000…+500 Hz | Accordage façon opérateur FM ; page « Setting the Octave or Semitone Mode » du manuel |
| UNISON | 1–16 voix | 1 | `kParamUnison` | Nombre magique 7 ; couleur du champ = charge CPU |
| DETUNE | 0–1 | 0 | `kParamDetune` | Course = RANGE (Global, 0–48 st, défaut 2 st) |
| BLEND | 0–100 % | 75 % | `kParamDetuneWid` | Niveau des voix latérales vs centrales, actif au-delà de 2 voix |
| WIDTH (stéréo) | −100…+100 | 0 | `kParamUnisonStereo` | Panoramique des voix d'unisson |
| Stack | Off · 12 (1x/2x/3x) · 12+7 (1x/2x/3x) · Center-12 · Center-24 | Off | `kParamUnisonStack` (`kOctave1..3`, `kOctaveFifth1..3`, `kCenter12/24`) | Octaves et quintes empilées sans jouer d'accord |
| Tuning (mode de détune) | Linear · Super · Exp · Inv · Random | Linear | `kParamDetuneMode` | Répartition des voix autour de la note |
| Uni WT Pos / Uni Warp / Uni Warp 2 | −100…+100 | 0 | `kParamUnisonWTPos`, `kParamUnisonWarp/2` | Étalement par voix (Global dans Serum 1, désormais aussi dans le panneau) |
| Range | 0–48 st | 2 | `kParamUnisonRange` | |
| Key zone min / max | 0–127 | 0 / 127 | `kParamKeyZoneMin/Max` | Cartographie clavier (§ 10, OSC Mapping) `[USINE]` |
| Velocity zone min / max | 1–127 | — | `kParamVelocityZoneMin/Max` | Couches de vélocité `[USINE]` |
| Routage | Filter (F1 ↔ F2) · Main · Direct · None | A → Filter, B/C/SUB/NOISE → Main | `RoutingSlot.kParamRoutingDest` | Réglé sur la page MIX (§ 5) |
| Envois BUS 1 / BUS 2 | 0–100 % | 0 | — | Page MIX |

Gestes `[DOC]` : Option/Alt-glisser l'étiquette d'un osc sur un autre = copie sans modulations ; Shift-Option = copie avec ; glisser sans modificateur = **échange**.

### 3.2 Moteur Wavetable `[DOC]` `[BIN]`

- **Table** : menu (usine 288+ tables, dossiers `S2 Tables/…`, `Analog/…`, `Digital/…`, etc. ; « --- » = table éditée non sauvée, icône disquette pour la sauver, tables utilisateur **toujours embarquées** dans le preset). Jusqu'à **256 frames de 2048 échantillons** (2 Mo). Affichage 2D (une frame, montre le warp) ou 3D (toutes les frames, jaune = frame courante, gris = interpolées). Loupe = éditeur (§ 3.8).
- **WT POS** 1–256 (`kParamTablePos`), la position dans la table ; clic droit → « Smooth Interpretation » (sic, = interpolation lisse : « perfect table transitions without morph tables » `[DOC, What's New p. 7]`). Interpolation entre frames : crossfade ou **spectral morphing**, choisie dans l'éditeur, calculée au chargement.
- **WARP 1 et WARP 2** (dual warp, nouveau) : chaque warp = menu + bouton de quantité 0–1 (`kParamWarp`, `kParamWarp2`) + bouton VAR selon le mode (`kParamWarpVar/2`). Liste complète des modes au § 4.
- **PHASE** 0–360° (`kParamInitialPhase`) : position de départ à chaque note ; 0 % et 50 % sont les passages par zéro d'un sinus (sinon clic avec attaque rapide). **RAND** 0–100 % (`kParamRandomPhase`) : phase aléatoire par voix, supprime le « zap laser » de l'unisson. Mémoire de phase : par voix ou continue (`kParamPhaseMemory` `kPerVoice` / `kContiguous` ; « Mem » dans Serum 1 à 100 %).
- `kParamXfadeMode`, `interpolateAfterLoad` 0–2 : mode d'interpolation embarqué dans le preset `[BIN]`.

### 3.3 Moteur Sample `[DOC]` `[EXTRAIT]` `[BIN]`

Lecteur d'un fichier (glisser-déposer, dossiers `Samples/Factory/…` et `Factory Non-Tonal/…`, FLAC/WAV) avec : **Start / End** (0–100 %, accolade bleue), **Loop Start / End**, **Loop crossfade** (0–63 % observé), **Loop mode** Forward · Ping-Pong · Reverse · Tailed (`kParamLoopMode`), « loop ends at release », **Reverse**, **Random start** (0–100 %), **Rate** (tape-stop, lecture inversée), **Slicing** Manual (Option/Alt-clic pour poser une tranche) · Auto (seuil `kParamAutoSliceThreshold`, note racine `kParamSlicingRootNote`), **Base tempo** (`kParamBaseTempo`, 138–156 observé), base note / gain / trim head-tail stockés avec le fichier, note racine, key tracking, warps (§ 4). Détection de boucle « snap » `[EXTRAIT]`. Officiel `[DOC, What's New p. 8]` : points start/end et loop start/end **modulables**, crossfade aux points de boucle, slicing Auto/Manual « with advanced options », modes de lecture, **« forward-reverse looping tails for real time stretching »**, warps FM et PM ; les mêmes fonctions existent en Granular et en Spectral.

### 3.4 Moteur Multisample `[DOC]` `[BIN]`

Charge un **SFZ** (`sfzPathRelative`, usine `Multisamples/Factory/{Synth, Strings, Keys, Choir, Mallet, Plucked, Winds, Brass…}/*.sfz` ; texte SFZ embarqué dans le preset, 4 à 234 fichiers FLAC par instrument). Contrôles : **enveloppe propre** Delay · Attack · Hold · Decay · Sustain · Release avec **Env Override** (l'enveloppe du multisample remplace ENV 1), **Vel Track** 0–100 % + override, **Random phase**, **Timbre Shift** −18…+64 (décale la couche utilisée, donc le timbre, sans changer la hauteur), warps (§ 4). Vu par la presse comme « un peu gadget », mais c'est le moteur des 155 presets d'usine « Multisample » `[USINE]`.

### 3.5 Moteur Granular `[DOC]` `[BIN]`

Jusqu'à **256 grains**. **SCAN** (vitesse de la tête, ±200 % par défaut, ±400 / ±800 % ; négatif = inversé, 0 = figé ; `kParamScanRate`, `kParamScanRange` ; sync BPM `kParamScanBPMRate/Divide/TempoLock`) · **DENS** (Free en Hz · BPM · Grains ; 0–800 ; `kParamDensity`, `kParamDensityMode`) avec **Jump Start** · **LENGTH** (Free · BPM · Percent ; 0–10 s ; `kParamGrainLength`, `kParamLengthMode`) · **Fenêtre** (manuel : Hann, Welch ; internes `kWindowTukey`, `kWindowExpDec`, `kWindowTriangle`, `kWindowBlackmanHarris`, `kWindowGaussian`) avec AMOUNT · SKEW (−100…+100) · SHAPE · **Randomisation par grain** : Offset, Dir (+ Reverse Grains), Pitch (0–12 st), Gain, Grain length, Pan, Warp 1/2, Window amount/skew · **Unison trig pattern** Random · Exponential · Even · axe Y assignable au volume (`kParamYAxisAssignment`). « Granular synthesis can be CPU intensive » `[DOC]`.

### 3.6 Moteur Spectral `[DOC]` `[EXTRAIT]` `[BIN]`

Resynthèse additive en temps réel d'un sample (ou d'une **image PNG**, 2048 × 256 recommandé). Contrôles : **FREQ LO / HI** (plage retenue, Hz, avec option lissée `kParamLoHiIsSmooth`), **Phase Lock**, **Transients** (détection façon time-stretch avancé), **filtre spectral** (types de série + forme **dessinable** dans une fenêtre ; `kParamSpecFltShift` −100…+100, `kParamSpecFltWetDry`), et des **warps spectraux** propres (§ 4.3).

### 3.7 SUB et NOISE `[DOC]` `[BIN]`

**SUB** (11, 101) : forme Sine · RoundRect · Triangle · Saw · Square · Pulse (`kParamShape` ; 6 entrées dans le binaire), OCTAVE, LEVEL, PAN, PHASE (`kParamInitialPhase`), phase continue (`kParamContiguousPhase`), **coarse modulable** (nouveau Serum 2), routage et envois comme les autres. Un sinus SUB seul, MONO + LEGATO, release ≈ 90 ms : sub validé sur ce Mac (≈ −4 dB avant fader avec Utility à 0) `[LOCAL]`.

**NOISE** (896, 101) : lecteur de sample stéréo haute qualité. Menu de bruits (200+ ; dossiers `Noises/Analog`, `Organics`, `Attacks_Misc`, `S2 Noises`… ; **les bruits utilisateur ne sont pas embarqués dans le preset**), **Type** White · Pink · Brown · Geiger (`kParamNoiseType`), **COLOR** 0–1, **PITCH** (50 % = hauteur d'origine ; avec **Key track** le bouton passe en demi-tons), FINE (cents), PAN, LEVEL, **PHASE** (= point de départ, automatisable en « scratch »), **RAND**, **One-shot / boucle** (flèche ; one-shot = transitoire d'attaque). Champ `sampleFromAudioInput` observé dans deux presets `[BIN]` : **MUET** sur la fonction (échantillonnage de l'entrée audio ?), à tester.

### 3.8 Éditeur de wavetable `[DOC, manuel Serum 1 ; inchangé dans l'esprit]`

Loupe sur la forme d'onde. Vignettes des frames en bas (clic = sélectionner, glisser = réordonner, Shift-clic = plage). Outils de dessin : flat line, slope up/down, sine, half sine (valley/peak), curve up/down, interpolate linear/curved, nudge, noise, sur une grille réglable. **Zone FFT** : dessin des harmoniques (rangée du haut) et de leurs phases (rangée du bas) ; menu : Clear All, Clear HF/LF, Generate Saw, Randomize low X bins (± half), Randomize All, random series gaps, Progressive Fade, Shift Octave Up/Down, Draw Odd/Even only. **Formula parser** (formules mathématiques, presets, fichiers `FormulaUserSingles/Multis.txt`). Menus : Single (frame courante), Process (toutes), Morph (crée/enlève les interpolations, crossfade ou spectral), Add/Remove (Init…), Sort (par propriété spectrale), Import (audio → table, avec « constant frame size (pitch avg) » à essayer en premier ; PNG), Export (.wav avec chunk `clm` `<!>2048 …`). Un fichier importé « raw » : 32 à 9999 échantillons par cycle.

---

## 4. Les modes de warp, liste complète

Chaque oscillateur principal a **deux** slots de warp (WARP 1, WARP 2), chacun avec un menu, un bouton de quantité et, selon le mode, un VAR `[DOC]`. Les noms internes sont ceux des presets `[BIN]` `[USINE]` ; le libellé affiché est celui du manuel quand il est connu.

### 4.1 Warps de forme (hérités de Serum 1, valables sur wavetable) `[DOC]`

| Affiché | Interne | Effet |
|---|---|---|
| Off | `kNoWarp` | — |
| Sync (self sync) | `kHardSync` / `kSync` | La table joue plus vite et redémarre à la période de la note : formant, brillant |
| Sync 1/2 Win. · Sync Window | `kSoftSync`, `kSofterSync` | Idem avec fondu (« windowed sync »), adoucit les discontinuités |
| Bend + · Bend − · Bend +/− | `kBendPos`, `kBendNeg`, `kBendPosNeg` | Pince la forme vers le centre ou les bords ; **+/− : 50 % = neutre** |
| PWM | `kPWM` | Pousse la forme vers la gauche : le PWM classique sur une carrée |
| Asym + · − · +/− | `kASYMPos`, `kASYMNeg`, `kASYMPosNeg` | Comme Bend mais sur toute la forme d'un seul côté |
| Flip | `kFlip` | Inversion de polarité à un point du cycle |
| Mirror | `kDLM` | Miroir de la seconde moitié : qualité « octaviée », jamais neutre |
| Remap 1 · 2 (miroir) · 3 (sinusoïdal) · 4 (×4) | `kRemap_1..4` | Remappage dessiné dans un graphe (loupe) ; Remap 4 « quand on veut quelque chose de méchant » |
| Quantize | `kQuantize` | Réduction de résolution **sur la forme**, l'aliasing suit la hauteur (contrairement à un Redux) |
| Odd/Even (nouveau) | `kEvenOdd` | 50 % = signal d'origine, 0 % = impaires seules, 100 % = paires seules (effet d'octave) |

### 4.2 Warps de modulation croisée, de filtrage et de distorsion `[DOC]` `[BIN]`

- **FM / AM / RM / PD** depuis **OSC** (l'autre osc principal), **OSC2** (le troisième), **SUB**, **NOISE**, **FILT1**, **FILT2** : `kFM_OSC`, `kFM_OSC2`, `kFM_SUB`, `kFM_NOISE`, `kFM_FILT1/2`, `kAM_*`, `kRM_*`, `kPD_*` ; **Self PD** (`kSelfPD`) ; variantes `kFMX_*` et `kFMP_*` observées dans les presets d'usine (FM « modulaire » selon la presse ; libellé exact **MUET**). Dans Serum 1, un seul sens A→B ou B→A à la fois ; Serum 2 a trois oscillateurs et des filtres comme sources. La source doit être activée, son niveau peut être à zéro. PD = distorsion de phase (nouveau).
- **Filter** au niveau de l'oscillateur : LPF, HPF (`kFilterLPF`, `kFilterHPF`).
- **Distortion** par oscillateur : Tube (`kDistTube`), Soft Clip, Hard Clip, Diode 1, Diode 2, Linear Fold, Sine Fold, Zero-Square, Asym, Rectify, Sine Shaper, Stomp Box, Tape Sat., Soft Sat. (`kDistSoftClip`, `kDistHardClip`, `kDistDiode1/2`, `kDistLinFold`, `kDistSinFold`, `kDistZeroSquare`, `kDistAsym`, `kDistRectify`, `kDistSineShaper`, `kDistStompBox`, `kDistTapeSat`, `kDistSoftSat`).

Usage réel `[USINE]` sur 894 presets : PD OSC 138, Sync 118, FM OSC 81, PD SUB 72, Tube 55, FM SUB 53, Bend + 52, PWM 47 ; Remap 1–4 quasi inutilisés (1 chacun).

### 4.3 Warps spectraux (moteur Spectral seulement) `[BIN]` `[EXTRAIT]`

`kSpectralComb` (peigne), `kGate` (coupe sous un seuil), `kAddharmonics`, `kAddsubharmonics`, `kSpread` (étale les partiels), `kSmear`, `kDetune`, `kPeakOctaveUp/Down`, `kPeakHarmUp/Down`, `kShepardFilter`, `kSpectralPitchShift` (**renommé « Pitch Blend » en 2.0.19, un nouveau « Pitch Shift » l'a remplacé** `[DOC changelog]`), `kSpectralShift`, `kSpectralPhaseTwist`, `kMirror`, `kVocode_OSC` / `kVocode_NOISE`, `kMask_OSC` / `kMask_NOISE`, plus les distorsions et FM/PD communs.

---

## 5. Page MIX : le mixer et le routage `[DOC]`

Détail complet dans `serum2-fx-clip-arp.md` § A. L'essentiel :

- Canaux : SUB, OSC A, B, C, NOISE, FILTER 1, FILTER 2, BUS 1, BUS 2 ; seuls les éléments actifs s'affichent ; **cliquer l'en-tête active l'oscillateur ou le filtre dans tout Serum**.
- Par oscillateur : niveau, pan, **routage** Filter (bouton du haut = répartition F1 ↔ F2) · Main (avec bouton « enveloppe » : désactivé, ENV 1 n'agit plus et l'osc s'éteint après le release le plus long) · **Direct** (contourne filtre ET effets) · None ; envois BUS 1 / BUS 2.
- Par filtre : sortie Filter 1 ou 2 (chaînage série), Main, Direct, None ; PAN, MIX (dry/wet, 100 % recommandé, sans effet sur les combs), niveau ; **un filtre activé reste grisé tant qu'aucun osc ne lui est envoyé**.
- BUS 1 / BUS 2 : bus auxiliaires d'effets (réverb ou delay partagés, wet/dry par source, compression parallèle, économie de CPU) ; sortie Main (défaut), Direct, ou vers l'autre bus ; niveaux `kParamFXBus1Vol/2Vol` (0–2), destinations `kParamFXBus1Dest/2Dest`, niveau Direct `kParamDirectVol` `[BIN]`.
- Depuis le mixer on peut aussi **bypasser chaque module FX**, régler les niveaux des canaux BUS et des sorties Main/Direct, et manipuler cutoff et résonance des filtres graphiquement `[DOC, What's New p. 16]`.
- **MUET** : pré/post fader des envois.

---

## 6. Filtres 1 et 2 `[DOC]` `[BIN]`

| Contrôle | Plage | Défaut | Interne |
|---|---|---|---|
| Marche/arrêt (FILTER 1 : (996, 101)) | on/off | F1 off dans Init | `kParamEnable` |
| Type | 96 entrées (liste ci-dessous) | MG Low 12 (Init) | `kParamType` |
| CUTOFF | 8 Hz – 22 050 Hz (stocké 0–1) | — | `kParamFreq` |
| RES | 0–100 | 0 | `kParamReso` |
| DRIVE | 0–100 | 0 | `kParamDrive` ; clic droit → **Clean Mode** (−24 dB avant, +24 dB après) = `kParamPad` |
| VAR | selon le type (étiquette change) | — | `kParamVar` |
| MIX | 0–100 % | 100 | `kParamWet` |
| STEREO / PAN | offset de cutoff G/D, 50 % = aucun | 50 | `kParamStereo` |
| Key track (icône piano) | on/off | off | `kParamKeyTrack` ; une octave MIDI = une octave de cutoff |
| Level | 0–1 | 1 | `kParamLevelOut` |
| X / Y | 0–1 | — | `kParamX/Y` : point du filtre dessinable PZ SVF (`PZs`) |
| Affichage | clic droit : Frequency Response · + FFT · Phase Response & FFT ; **cutoff et résonance se règlent directement à la souris dans le graphe** `[DOC, What's New p. 10]` | | |

**Ce que fait VAR** `[DOC, appendice Serum 1 + manuel Serum 2 p. 170]` : FAT (saturation dans la boucle de résonance, sur MG et SVF : dompte une résonance en ajoutant des harmoniques) · FREQ / FRO2 (cutoff du second filtre des duals) · MORPH (entre les trois états des morphing) · LP FRO / HP FRO / HL WID (filtre de la boucle de feedback des comb/flange/phase) · DB +/− (gain des EQ) · DAMP (Combs, Allpasses, Reverb) · BOEUF (French LP) · THRU (Add Bass, dry déphasé) · FORMNT (décalage de formant) · SPREAD, WIDTH, COMBFRO, SCREAM, STAGES, SMOOTH, PAIN (types Serum 2, étiquettes citées par le manuel sans définition).

### Les 96 types, par famille `[BIN, liste du binaire 2.0.23 ; libellés affichés de Serum 1.3 quand ils existent]`

- **Ladder « MG »** : MG Low 6 / 12 / 18 / 24 (`MgL6..24`).
- **SVF** : Low 6/12/18/24, High 6/12/18/24, Band 12/24, Peak 12/24, Notch 12/24.
- **Duals SVF** (première lettre = principal, seconde = secondaire, résonance liée, VAR = 2e cutoff) : LH 6, LH 12, LB 12, LP 12, LN 12, HB 12, HP 12, HN 12, BP 12, BN 12, PP 12, PN 12, NN 12.
- **Morphing** (VAR = morph) : L/B/H 12 et 24, L/P/H 12 et 24, L/N/H 12 et 24, B/P/N 12 et 24.
- **Comb** ± (et L6, H6, HL6 ±) · **Flanger** ± (idem) · **Phaser** 12 / 24 / 36 / 48 ± (+ 48 L6 / H6 / HL6 ±) · FPhs 12 HL6 ± (flange-phase). Astuce du manuel : pour les Flanges, MIX à 50 %.
- **EQ** : Low EQ 6 / 12, Band EQ 12, High EQ 6 / 12 (VAR = gain).
- **Spéciaux** : Ring Mod, Ring Mod ×2 (`RMT`), SampHold + / − (`SNH1/2`), Combs, Allpasses, Reverb, French LP (distordant, VAR Boeuf), German LP (ZDF propre), Add Bass, Formant I / II / III (le cutoff morphe entre voyelles), Bandreject, Dist.Comb 1 LP / BP, Dist.Comb 2 LP / BP, Scream LP / BP (`Scream`, `Scream3LP/BP`), `ZDF_A`.
- **Nouveaux Serum 2** `[USINE, noms internes]` `[EXTRAIT]` : **MG Ladder** (`LadderMg`), **Acid Ladder** (`LadderAcid`, 303), **EMS Ladder** (`LadderEMS`), **MG Dirty** (`DirtyMg`), **Wasp** (`Wsp`), **Exp** et **Exp BPF** (`Exp`, `ExpBPF`), **Diffuser**, **PZ SVF** (dessinable : plusieurs courbes tracées puis morphées), **DJ Mixer** (`DJMixer`), Comb 2, LNH24/LH12/HP12/L6/… (variantes 6 dB et 24 dB des duals). Selon la presse, MG Ladder et EMS Ladder n'ont pas de distorsion modélisée, Wasp, Exp, Acid Ladder et MG Dirty en ont `[EXTRAIT]`. 57 noms internes restent non affichés dans la statistique d'usine : la liste Serum 2 dépasse 96 entrées, **le nombre exact est MUET**.

---

## 7. Modulateurs : enveloppes, LFO, macros, matrice

### 7.1 ENV 1 à 4 (bas gauche) `[DOC]` `[BIN]`

| Contrôle | Plage | Défaut | Interne |
|---|---|---|---|
| DELAY | 0–32 s, **synchronisable au tempo** | 0 | `kParamDelay` |
| ATTACK | 0–32 s | 0 (Init : quasi 0) | `kParamAttack` |
| HOLD | 0–32 s | 0 | `kParamHold` |
| DECAY | 0–32 s | ≈ 0,32 s (Init ENV 1) | `kParamDecay` |
| SUSTAIN | 0–100 % (ENV 1 affiché en dB, −∞ à 0) | 100 % | `kParamSustain` |
| RELEASE | 0–32 s | ≈ 5 ms (Init) | `kParamRelease` |
| Courbes A / D / R | −100…+100 (50 = linéaire) | 50 / 66,6 / 66,6 | `kParamCurve1/2/3` ; glisser le segment dans le graphe |
| BPM | on/off | off | `kParamBeatSync` : A, D, S, R en divisions de tempo |
| Invert Legato | on/off | off | `kParamLegatoInverted` : redéclenche à chaque note même en legato |
| Start / End | 0–1 | 0 / 1 | `kParamStart`, `kParamEnd` (niveaux de départ et de fin observés) `[USINE]` |
| Voice steal restart | | | `kParamVoiceStealRestart` `[BIN]` |

Officiel `[DOC, What's New p. 14]` : quatre enveloppes, option **BPM** (suit le tempo de l'hôte) et **Invert Legato** (« force an envelope to always trigger at note on, even when legato is enabled »).

ENV 1 est câblée à l'amplitude de chaque voix (sauf routage Main avec bouton « enveloppe » désactivé, § 5) ; ENV 2–4 n'agissent qu'une fois glissées sur une destination. Lecture : les cinq champs numériques sous le graphe ; double-clic ouvre un champ de saisie (mais Entrée n'arrive pas en arrière-plan) `[LOCAL]`. Affichage verrouillé (zoom automatique) ou libre. Option/Alt-glisser une tuile ENV sur une autre : copie.

### 7.2 LFO 1 à 10 (bas centre) `[DOC]` `[BIN]`

| Contrôle | Plage / valeurs | Interne |
|---|---|---|
| Type | **Normal** (courbe dessinée) · **Path** (tracé XY, sortie X et **sortie Y séparée**) · **Chaos Lorenz** · **Chaos Rössler** · **Random S&H** | `kParamType` (`Path`, `Lorenz`, `Rossler`, `RandomSH`) |
| Mode | **Off** (libre, calé sur l'horloge du projet) · **Trig** (redémarre à chaque note) · **Env** (joue une fois ; point de *loopback* pour boucler une portion : Shift-⌘-clic sur un point) | `kParamMode` (`Free`, `Envelope`) |
| RATE | BPM : 32 bar → 1/256 par pas d'octave, défaut 1/4 ; Hz : jusqu'à 1000 Hz avec **×10** | `kParamRate`, `kParamBeatSync`, `kParamRate10x` |
| DOT · TRIP | pointé, triolet (BPM) | `kParamDotted`, `kParamTriplets` |
| ANCHOR | la position saute pour rester calée sur la mesure quand on change le rate | `kParamAnchored` |
| SWING | suit le swing global du clavier | `kParamSwing` |
| HOST | **attention, sémantique changée** : agit désormais aussi BPM désactivé ; LFO vraiment libre = HOST off `[DOC]` | — |
| RISE | 0–4 s (fondu d'entrée de la forme ; en mode Env, fondu vers l'enveloppe) | `kParamRise` |
| DELAY | 0–4 s avant le rise | `kParamDelay` |
| SMOOTH | 0–100, arrondit toutes les marches | `kParamSmooth` |
| PHASE | 0–360°, **modulable**, avec snap | `kParamPhase`, `kParamPhaseSnap` |
| MONO | un seul LFO pour toutes les voix | `kParamMono` |
| Direction | avant / arrière | `kParamDirection` 1–2 |
| GRID X / Y | 4–32 ; Shift-clic dessine des marches (séquenceur) | `kParamGridX/Y` |
| Formes | menu de presets (dossier), Save LFO Shape… ; noms stockés | `curveDisplayName`, `pathDisplayName` |

Officiel `[DOC, What's New p. 14]` : outils de dessin avec éditeur dédié, grille X et Y indépendantes, phase réglable **et modulable**, ×10 jusqu'à 1000 Hz, suivi du swing, lecture directionnelle, presets de formes ; **LFO 7 à 10 apparaissent après assignation du LFO 6**.

Gestes du graphe `[DOC]` : double-clic = ajouter/enlever un point ; Shift-clic = marches à la grille ; Alt-glisser un point = snap ; Alt-glisser un point de courbe = toutes les courbes ; glisser sur le fond = sélection multiple ; ⌘-glisser = déplacement relatif ; clic droit = menu (forme des segments, start/loopback) ; Alt-glisser une tuile LFO sur une autre = copie.

**Modulation des points** (nouveau) `[BIN]` `[EXTRAIT]` : clic droit sur un point → *Modulate X* / *Modulate Y* → choisir un **LFO Bus** (16 bus, `LFOPointModBus0..15`, « LFO Bus 1–16 ») et lui assigner une source : la forme elle-même bouge. 66 presets d'usine l'utilisent (`lfoPointModAssignments`).

### 7.3 MACRO 1 à 8 (bas droite) `[DOC]` `[BIN]`

Valeur 0–100 (`kParamValue`), nom libre (`name` ; noms d'usine les plus fréquents : REVERB, DELAY, CHORUS, NOISE, WIDTH, FILTER, CUTOFF, DRIVE…). Assignation par glisser du sélecteur sur le contrôle (un « + » marque une destination valide, **toutes ne le sont pas**) ; un chiffre à côté du nom = nombre de destinations. **Une macro est aussi destination** (chaînable) et peut servir d'**aux source** ; on peut appliquer et supprimer une macro `[DOC, What's New p. 14]`. Enregistrable en automation dans un clip. Live n'affiche pas toujours le bon nom de macro après chargement d'un Set (contournement 2.0.21) : un script ne doit pas identifier une macro par son nom.

### 7.4 Page MATRIX : les 64 slots `[DOC]` `[BIN]`

Chaque ligne : **Source** · **Aux source** (seconde source qui met la profondeur à l'échelle : même sens, inversée, ou bypass) · **Destination** (module + paramètre) · **Amount** −100…+100 (`kParamAmount`) · **Bipolaire / unipolaire** (`kParamBipolar` ; réglage de la matrice, pas du LFO) · **Curve** d'entrée et de sortie, courbe principale et courbe de l'aux éditables, aux inversable (`kParamCurveIn/Out`, `kParamMainCurveData`, `kParamAuxCurve`, `kParamAuxInverted`) · **Bypass** par ligne (flèche à droite, `kParamBypass`) · **Smooth** rise/fall liés ou non (`kParamSmoothRise/Fall`, `kParamSmoothLink`) · **Delay** avec sync (`kParamDelayOffset`, `kParamDelayBeatSync`) · **Out** 0–100 % (`kParamOut`). Lignes réordonnables par poignées, suppression en un clic, valeurs animées en temps réel, vue étendue, **courbes de source et d'aux source éditables** `[DOC, What's New p. 15]`. Glisser une source sur un bouton crée la ligne ; l'arc autour du bouton règle la profondeur.

**Les 59 sources, dans l'ordre du menu** `[BIN, table du binaire]` : Mod Wheel · Env 1–4 · LFO 1–10 · Velo · Note# · Aftertouch · Poly Aftertouch · Noise OSC (audio) · NoteOn Rand 1, Rand 2 · NoteOn Alt., Alt. 2 · Macro 1–8 · Pitch Bend · Expr X (Pan), Expr Y (Timbre), Expr Z (Press.) (MPE) · Release Velo · Fixed · LFO 1–10 **Y** (sortie Y des LFO Path) · OSC A, OSC B, OSC C, SUB OSC (audio-rate) · Filter 1, Filter 2 (audio-rate) · Active Voices · Voice Mod 1, Voice Mod 2 · Voice Index · NoteOn Rand (Discrete). Usage d'usine `[USINE]` : Macros et Mod Wheel dominent (≈ 1000 slots chacune), LFO 1 (901), Velo (697), Env 2 (567) ; Poly Aftertouch, Pitch Bend, Filter 1/2, Active Voices, Voice Mod : 0.

Destinations : « nearly every knob », y compris la plupart des paramètres d'effets (§ 8, avec la réserve « par voix ») et les macros. Si une destination manque dans le menu, cliquer le contrôle sur la page principale la fait apparaître `[DOC]`.

---

## 8. Page FX : trois racks, 13 modules, 3 splitters

Le détail par module (paramètres, plages, pièges) est dans `serum2-fx-clip-arp.md` § B–C ; ceci est la carte.

| Module | Type interne | Paramètres (libellé → interne) `[DOC]` `[BIN]` |
|---|---|---|
| **Bode** (frequency shifter) | 10 `FXBode` | SHIFT (`kParamShift` −100…+100, clic droit Retrig) · RANGE (`kParamRange` 0,1–3043) · DIR · WIDTH (`kParamOutputWidth`) · DELAY (`kParamDelayTime`) + BPM · FEED (`kParamFeedback`) · BALANCE (`kParamDelayBalance`) · BLUR · mono input · swap A/B · MIX |
| **Chorus** | 3 `FXChorus` | RATE (BPM 8 bar→1/32 ou 0–20 Hz) · DELAY 1 / 2 (0–20 ms) · DEPTH (0–26) · FEEDBACK (0–95) · LPF/HPF après le wet (`kParamFilt` 50–20 000 Hz, `kParamFiltMode`) · MIX ; 4 voix, 2 taps par côté |
| **Compressor** | 5 `FXComp` | MODE Single / Multiband · THRESH (0 = 0 dB, 100 % = −120 dB) · RATIO (1:1 … 32:1, **Limit** = vrai limiteur true-peak, attaque 0–10 ms, makeup 0–36 dB, clic droit Limiter Latency Comp) · ATTACK 0,1–1000 ms · RELEASE · GAIN (≈ 30 dB) · Multiband : X-LOW (`kParamXoverLow`), X-HIGH (`kParamXoverHi`), BELOW (ratio sous le seuil = compression ascendante), H/M/L (`kParamGain0..2`, `kParamRatio0..2`, `kParamRatioBelow0..2`, `kParamThreshUD0..2`) · MIX (`kParamWet`, `kParamCompensatedWetDry`) · sidechain interne par bande via la matrice |
| **Convolve** | 11 `FXConv` | IMPULSE (usine `IR/Factory/{Cab, Short, Medium, Long}/*.flac`, IR externes par glisser, **Embed in Preset**) · SIZE 10–1000 · TONE −100…+100 · ϕ MIN (phase minimale) · PRE-DLY (+ sync) · ATTACK · DECAY (0–40) · DAMP · IR GAIN (`kParamIpTrim` −34…+6 dB) · MIX |
| **Delay** | 4 `FXDelay` | **HQ** (nouveau, **actif par défaut** `[DOC, What's New p. 12]`) · MODE Normal / Ping-Pong / Tap→Delay · temps L/R (`kParamTimeL/R`, sync : fast … 4 bar) + **offset** L/R 0,5–1,5 (« Trip » à 133 %, « Dot » à 150 %) · LINK · FEEDBACK 0–95 · FREQ 40–18 000 Hz + BW 0,75–8,25 (**Q inversé**) · HQ · BPM · MIX ; double-clic sur l'affichage = overlay de fréquence |
| **Distortion** | 0 `FXDistortion` | TYPE (16 : Tube, Soft Clip, Hard Clip, Diode 1, Diode 2, Lin. Fold, Sin Fold, Zero-Square, Downsample, Asym, Rectify, X-Shaper, X-Shaper (Asym), Sine Shaper, Stomp Box, Tape Sat. ; Serum 2 ajoute **Overdrive** et un réglage **DC bias** `[DOC, What's New p. 12]`, plus Soft Sat. `[USINE]`) · DRIVE 0–100 (en Downsample = taux d'échantillonnage, en X-Shaper = morph A→B) · filtre OFF / PRE / POST avec type morphable LP→BP→HP (`kParamLPHP`), FREQ (8–13 290 Hz, clic droit Key Track), Q (`kParamBW`) · stages (`kParamNumStages` 2–16) · MIX |
| **Equalizer** | 7 `FXEQ` | Bande basse : Low Shelf / Peak / **High Pass** ; bande haute : High Shelf / Peak / **Low Pass** (`kParamType1/2`) · FREQ 22–20 000 Hz · GAIN ±24 dB (**sans effet** en HP/LP) · Q (`kParamReso1/2` 0–100) · **pas de MIX** |
| **Filter** | 8 `FXFilter` | Identique au filtre de voix mais sur la somme : TYPE (les 96, MG Low 6 par défaut) · CUTOFF (Key Track) · RES · DRIVE (Clean Mode) · VAR · PAN (offset G/D) · MIX ; astuce du manuel : une enveloppe ici recrée le comportement paraphonique des vintages |
| **Flanger** | 1 `FXFlanger` | RATE (BPM ou 0–20 Hz) · DEPTH · FEEDBACK (20–91) · PHASE (0 % = même phase G/D, 50 % = 180°, `kParamWidth` 0–360) · MIX |
| **Hyper / Dimension** | 9 `FXHyperD` | HYPER = chorus à micro-delay 1–7 voix : RATE · UNISON (0 = Dimension seul) · DETUNE · RETRIG (zap laser à chaque note) ; DIMENSION = pseudo-stéréo par 4 lignes de delay en opposition de phase : SIZE (`kParamDimESize`), MIX propre (`kParamDimEWet`). Le manuel recommande Hyper **plutôt que** beaucoup d'unisson pour économiser le CPU |
| **Phaser** | 2 `FXPhaser` | RATE · POLES 1–18 (`kParamNumPoles`) · DEPTH · DEPTH 2 (offset entre étages) · FREQ 20–18 000 Hz · FEEDBACK · PHASE (`kParamWidth`) · MIX |
| **Reverb** (Tal modifié) | 6 `FXReverb` | TYPE Plate (défaut) · Hall · Vintage · Nitrous · Basin (`kParamType` : Plate = défaut absent, `kHall`, `kVintage`, `kAbyss`, `kSpace` ; **correspondance Nitrous/Basin ↔ kSpace/kAbyss non établie**, `[HEUR]` Nitrous = kSpace puisque son MODE commence par « Space ») · LO CUT / HI CUT (`kParamFreq`, `kParamFreqB`) · SIZE 0–100 · PRE-DLY (0–2,5 s, sync) · DAMP · WIDTH · Hall : DECAY, SPIN RATE, SPIN DEPTH · Vintage : ER SIZE, DIFF A, DIFF B, CHORUS (`kParamVintageScale/B`) · Nitrous : FEEDBACK, DIFFUSION, MODE Space / Marble / Rectangle / Hexagon / Box · Basin : FEEDBACK, CHORUS · MIX |
| **Utility** | 12 `FXUtils` | POLARITY INV gauche et droite séparées · LPF (50–20 000) · HPF (1–400) · MONO BASS + FREQ (`kParamLFMono`, `kParamLFXover` 20–400 Hz) · WIDTH 0–800 · PAN (`kParamBalance`) · MIX |
| **Splitter L/H** | 13 `FXSplit` | SPLIT FREQ (31–3517 Hz) · LOWS · HIGHS · LEVEL ; deux sous-racks |
| **Splitter L/M/H** | 14 `FXSplit3` | 2 × SPLIT FREQ · LEVEL ; trois sous-racks |
| **Splitter M/S** | 15 `FXSplitMS` | LEVEL seul ; sous-racks MID et SIDE |

Structure `[DOC]` `[BIN]` : racks MAIN, BUS 1, BUS 2 ; flux du haut vers le bas ; **jusqu'à 16 slots par rack** (`FX: array[max 16 slots]`) ; chaque module a MIX (sauf EQ) et LEVEL (`kParamLevelOut`, trim de sortie), bouton bypass rouge (Alt-clic = tout le bus), vue étendue Alt-F ; clic droit sur le fond : Cut/Copy/Paste/Clear, **Lock FX Bus** (garde les modules au changement de preset **mais efface les modulations vers ce rack**), Load/Save FX Bus. Presets d'usine et utilisateur **pour les racks et pour les modules**, manipulation directe dans l'affichage graphique `[DOC, What's New p. 11]`. Ordre d'usine Serum 1 : Hyper en premier. Rack par défaut « Serum FX » : Serum 2 existe aussi en **plug-in d'effet** (`product: Serum2FX`, deux presets d'usine « SerumFX - … ») `[USINE]`.

Avertissement architectural `[DOC p. 159]` : les effets travaillent sur la somme des voix ; une enveloppe sur un paramètre d'effet est redéclenchée à chaque note. Exception : les bandes du compresseur multibande acceptent la matrice pour un sidechain interne. Et depuis 2.0.23, le volume master des FX n'a plus de **boost de 1,37 dB** : un patch ne sort pas au même niveau avant et après `[DOC changelog]`.

---

## 9. Page GLOBAL `[DOC]` `[BIN]` `[EXTRAIT]`

Tout est sauvé dans le preset **sauf les Préférences**, vraiment globales.

| Groupe | Contrôles | Interne / plage |
|---|---|---|
| **Voicing** (aussi en bas à droite) | POLY 1–32 · MONO · LEGATO · **Limit same-note polyphony** · Note latch · lecture « voix actives / total » | `kParamPolyCount`, `kParamMonoToggle`, `kParamLegato`, `kParamLimitSameNotePolyphony`, `kParamNoteLatch` |
| **Portamento** | PORTA time 0–8 s · CURVE (convexe : part vite, arrive lentement) · ALWAYS (glisse même sans note tenue) · SCALED (temps proportionnel à l'intervalle, une octave = la valeur du bouton) | `kParamPortaAlways`, `kParamPortaScaled` |
| **Pitch bend** | UP 1–24 · DOWN −1…−12 (S1 : ±24) | `kParamBendRangeUp/Dn` |
| **Master** | MASTER VOLUME (0–100 %, `kParamMasterVolume` 0–0,854) · MOD WHEEL (valeur courante) | |
| **Quality / oversampling** | **Draft = 1×, High = 2×, Ultra = 4×** ; **verrou** (sinon la valeur du preset s'applique) ; n'agit que sur les warps (sync, FM…) ; les warps FM/AM/PD/RM sonnaient différemment selon la qualité avant 2.0.21 | `kParamOversampling` 0–2, `lockOversampling` |
| **S1 Compatibility Mode** | activé automatiquement au chargement d'un preset Serum 1 (« similarité maximale », pas identité) | manuel p. 319 |
| **Disable Smoothing** | supprime le lissage des paramètres (automation précise à l'échantillon) | |
| **Accordage** | Global tuning A = 430–450 Hz (0,5 = 440) · fichiers **.TUN** (A doit rester 440) · **MTS-ESP** natif, sans réglage · verrou d'accordage · .SCL non confirmé | `kParamGlobalTuning`, `tuningData`, `tuningName`, `lockTuning` |
| **MPE** | Enabled · pitch bend range · config ; sources Expr X/Y/Z | `mpeEnabled`, `mpePitchBendRange`, `mpeConfig` |
| **Oscillator settings** | Pitch tracking par osc · Noise fine (cents) | (S1 : en haut à gauche de la page) |
| **Unison settings** | par osc : RANGE 0–48 st (déf. 2) · WIDTH · WARP · WT POS · STACK · TUNING (Linear / Super / Exp / Inv / Random) | § 3.1 |
| **MIDI out** | Off · Clip Player · On (à travers l'ARP, avec quantification clé/gamme ; **contradiction interne du manuel** p. 240 vs 265) | `kParamMidiOut` (`ClipPlayer`, `Synth`) |
| **Bus** | FX BUS 1 / 2 : destination et niveau · DIRECT : niveau | `kParamFXBus1Dest/Vol`, `kParamFXBus2Dest/Vol`, `kParamDirectVol` |
| **Préférences** (globales) | tooltips · cacher le clavier · action du double-clic · **Keyboard shortcuts ON/OFF** (requis pour les raccourcis du piano roll) · **restore locks when host sets state** (2.1.5) · **Ignore VST3 Note IDs** (2.0.24) · Limiter Latency Comp | Serum.cfg |
| Serum 1 seulement | Chaos 1 / Chaos 2 (BPM, Mono) → remplacés par les types Lorenz / Rössler des LFO | |

---

## 10. Clavier, OSC Mapping, CLIP, ARP `[DOC]` `[EXTRAIT]`

Le clavier du bas joue à la souris, montre les notes MIDI, celles du clip player et de l'arpégiateur, et porte les réglages :

- **TRANSPOSE** (demi-tons, toutes notes entrantes et générées, **sur deux octaves** `[DOC, What's New p. 19]`) · **KEY** et **SCALE** (appliqués **à l'entrée MIDI et à la sortie des modules CLIP et ARP** ; les notes hors gamme sont ramenées dans la gamme ; `PitchQuantizer0`) · **SWING** (global, OFF par défaut, division qui apparaît dès qu'on quitte OFF ; plage selon l'hôte : **Live 12,5–87,5 %**, FL −150…+150 %) `[DOC p. 269]`.
- **OSC MAPPING** : éditeur des **plages de notes et de vélocité des oscillateurs et de l'arpégiateur** (« define and limit the range to which both respond ») `[DOC, manuel web et What's New p. 19]` ; par exemple SUB + A dans le grave, B au médium, C au-dessus de C5 ; c'est `kParamKeyZoneMin/Max`, `kParamVelocityZoneMin/Max` par oscillateur `[BIN]`. Tag d'usine « KB-Span » (17 presets).
- Trois modes d'affichage du clavier : KEYBOARD, **CLIP** (touches vertes, indicateur qui clignote au rythme des notes, re-presser arrête) et **ARP** (touches violettes, re-presser relance).

**CLIP** (12 slots par banque, `MidiClip0..11`, `ClipPlayer0`) et **ARP** (12 slots, `Arp0`, `ArpClip0..11`) : tout est détaillé dans `serum2-fx-clip-arp.md` § D–E (LENGTH, KB SPAN relatif à C3, MODE, RATE, LAUNCH QUANT, RETRIG, VELO TRIG, NOTE GATE, piano roll et ses raccourcis ⌘X/C/V/D/U/K/L/Q/R/E/A, enregistrement Overdub/Extend, macros automatisées dans un clip ; arp : PATTERN, éditeur avec MODE 8 valeurs, STEP MODE 4 valeurs, WRAP, PITCH 0–24, lanes ACCENT et STRUM, TRANSPOSE 18 formes, PLAYBACK avec LATCH (**CC64 devient le latch**), THRU, OFFSET, REPEATS, GATE, CHANCE (Pre), RETRIGGER, VELOCITY). Champs internes vus `[BIN]` : `kParamRecordMode` (`Extend`), `kParamMetronomeEnabled`, `kParamRegionOffsetQuantize`, notes avec `expressionEvents` (MPE) et automation `kAutoDest_*` (ex. `kAutoDest_ChanPressure`). Officiel `[DOC, What's New p. 17–18]` : le module CLIP a un bouton « Show CLIP Module », un volume, les macros à portée de main pendant l'enregistrement, une grille réglable, des réglages globaux avec **banques de clips d'usine et utilisateur**, l'enregistrement Overdub ou Extend, un piano roll complet, des marqueurs de boucle et d'offset, la capture d'automation « in multiple lanes », un réglage MIDI Out, et **12 slots par banque** ; l'ARP a Pattern, Transpose (shift et range), Playback (offset, repeats, gate, chance…), Retrigger, Velocity, réglages globaux avec **banques d'arps d'usine et utilisateur**, bouton play par slot, **12 slots par banque**, et son **éditeur de pattern n'est disponible que quand SHAPE = « Pattern »**. Nombre de lanes d'automation d'un clip : 16 selon la presse `[EXTRAIT]`, « multiple » dans le document officiel, chiffre **MUET**.

---

## 11. Presets, fichiers, contenu d'usine

### 11.1 Navigateur `[DOC]` `[LOCAL]` `[USINE]`

Icône liste (1010, 36) ; arbre Factory › Arp / Bass / Bell / Chord / Drum / FX / Keys / Lead / Pad / Pluck / Seq / Synth / Vox … ; recherche par nom et **tags** ; filtres catégorie, genre, tags perso, **notes en étoiles** et filtre par note ; métadonnées affichées et éditables ; menu du navigateur : **Hybridize presets**, auto-play, **rescan database** ; bibliothèque = contenu d'usine, **packs d'artistes** (un pack se crée depuis un dossier de presets), presets utilisateur ; macros réglables pendant la pré-écoute `[DOC, What's New p. 20]` ; **autoplay** d'une mélodie par défaut ou d'un **clip de prévisualisation** fourni par le sound designer (clic droit sur un clip → Set as Preview Clip). Tags stockés dans le fichier : `[badge du moteur (Wavetable / Multisample / Sample / Granular / Spectral), Poly | Mono, catégorie (Arp / Clip / Embedded-Data / KB-Span / Custom-Tuning), Preview]`. Presets utiles sur ce Mac : Drum › « DR - Kick Minimal », Bass › Electric / Sub, Keys / Pad ; banques perso TKNVLT, « Kick Future House Tsila », F Brooks `[LOCAL]`. Verrous : FX bus, oversampling, tuning (état non restauré par l'hôte avant la préférence 2.1.5).

### 11.2 Dossiers `[DOC]` `[LOCAL]` `[USINE]`

- macOS : `/Library/Audio/Presets/Xfer Records/Serum 2 Presets/` (banques perso vues ici dans `Presets/User`) ; Windows : `Documents\Xfer\Serum 2 Presets\`. Menu logo → « Show Serum Presets Folder ».
- Sous-dossiers : `Presets/Factory`, `Presets/User` (sous-dossiers libres, packs `.SerumPack` déposés tels quels), `Tables` (`S2 Tables/…`, `Analog/…`, `Digital/…` ; 288+ tables), `Samples` (`Factory/{Piano, Bass, Flute, Vox, Spatial, Synth, Plucked…}`, `Factory Non-Tonal/{Drum, Noises, SFX}`), `Multisamples` (`Factory/{Synth, Strings, Keys, Choir, Mallet, Plucked, Winds, Brass…}/*.sfz` + FLAC), `Noises` (`Analog`, `Organics`, `Attacks_Misc`, `S2 Noises`), `IR` (`Factory/{Cab, Short, Medium, Long}`), `System` (formules), `Serum.cfg`.
- **Embarqué ou référencé** : tables utilisateur toujours embarquées ; samples, multisamples, IR embarquables (« Embed in Preset », tag Embedded-Data) ; **bruits jamais embarqués**. Un preset non embarqué n'est pas portable.

### 11.3 Formats de fichier `[BIN]`

- **`.SerumPreset`** : en-tête `XferJson\0` + longueur + JSON (fileType, hash md5 du flux, presetName, presetAuthor, presetDescription, product `Serum2` ou `Serum2FX`, productVersion, tags, version 3.0–6.0) + taille + `2` + **flux zstd contenant une carte CBOR** de 175 clés (`Oscillator0`…, `plainParams` = `"default"` ou seulement les paramètres qui diffèrent du défaut, **valeurs en unités réelles** : secondes, Hz, dB, %). L'état VST3 est le même conteneur en deux parties (processor, edit controller, version 9.0).
- **`.fxp`** Serum 1 : 299 paramètres float normalisés 0–1 dans l'ordre VST + blocs (matrice, LFO, switches, ordre des FX) ; s'ouvre dans Serum 2 (mode S1), **jamais l'inverse**.
- **Wavetables** : WAV mono float32 avec chunk `clm` `<!>2048 01000000 wavetable (www.xferrecords.com)`. Les formes de base (Sine, Triangle, Square…) vivent dans le plug-in, pas sur le disque.
- **Pas de compatibilité ascendante** : un preset ou un Set sauvé par une version plus récente se recharge en **Init silencieux** avant 2.0.19, avec message ensuite ; noter la version exacte dans la mémoire de projet.

### 11.4 Contenu d'usine en chiffres `[USINE]`

626 presets (2.0.11–2.0.15) : badges Wavetable 528, Multisample 155, Sample 72, Granular 56, Spectral 43 (un preset peut cumuler) ; Poly 414 / Mono 212 ; Arp 33, Clip 27, KB-Span 17, Custom-Tuning 2 ; 611 avec preview. Sur 894 presets (usine + packs) : basses 189, leads 127, pads 119, plucks 115, keys 41, sfx 38, drums 22, arps 20. Filtres les plus posés : MgL24, LadderEMS, LadderMg, MgL18. Warps : PD OSC, Sync, FM OSC, PD SUB, Tube.

---

## 12. Serum 2 vu depuis Ableton Live `[DOC]` `[LOCAL]` `[FORUM]`

Détail et procédure dans `serum2-automation-et-migration.md` ; l'essentiel :

- **Chargement** : `lom.py load "<piste>" "Serum 2"` (règle anti hot-swap, VST3 et AU coexistent → préciser) ; fenêtre par `ppal-select openPluginWindow: true`, sinon bouton « fenêtre » du device (≈ 29, 479 sur capture 1568 px de Live) `[LOCAL]`.
- **API Live** : `device.parameters` = `[Device On]` tant que rien n'est configuré, parce que Live ne peuple pas le panneau des plug-ins de plus de 64 paramètres. Les pages OSC, filtres, mixer, LFO, enveloppes, matrice sont exposées statiquement ; **les paramètres FX ne le sont qu'après clic droit → Automate** dans Serum (parfois bypass/unbypass du device). Plafond 128 paramètres par instance (`-_PluginAutoPopulateThreshold=128` dans Options.txt, effet sur VST3 non confirmé).
- **Configure** : l'ordre choisi dans le panneau Configure est l'index API ; **« Save as Default Configuration »** rend cet index stable pour toutes les instances futures. Pièges d'index documentés par le changelog (2.0.17, 2.0.18, 2.0.21).
- **Format** : VST3 de préférence (corrections d'abord côté VST3 ; AU a eu ses propres bugs : CC/aftertouch non transmis avant 2.0.19, crash 2.0.23).
- **Reproductibilité** : version exacte, S1 Compatibility, Quality verrouillé ou non, Disable Smoothing, fichiers embarqués, état des verrous.
- **Pilotage par clics** : § 2 ; un preset chargé suit la hauteur (clips KICK en C1 → transposer ou macro Pitch) `[LOCAL]`.

---

## 13. Serum 1 → Serum 2, ce qui change `[DOC]`

| | Serum 1 | Serum 2 |
|---|---|---|
| Oscillateurs principaux | 2 (A, B) | 3 (A, B, C), 5 moteurs chacun |
| Warp | 1 slot, 24 modes | 2 slots, + Odd/Even, filtres, distorsions, PD, sources FILT1/2 et OSC C, warps spectraux |
| Filtres | 1 (A/B/N/S vers le filtre) | 2, série ou parallèle, routage explicite sur la page MIX, ~11 nouveaux types |
| Enveloppes | 3 (AHDSR) | 4 (D-A-H-D-S-R, BPM, Invert Legato) |
| LFO | 4 (+4 cachés à partir de 1.3) | 10, types Path / Chaos / S&H, sortie Y, ×10 jusqu'à 1000 Hz, points modulables (16 bus) |
| Chaos 1/2 | page Global | types de LFO |
| Macros | 4 | 8, chaînables, aux source |
| Matrice | 16 puis 32 slots, 32 sources | 64 slots, 59 sources, aux source avec courbes, bypass par ligne |
| Effets | 10 modules, chaîne unique, un de chaque | 13 modules + 3 splitters, 3 racks, instances multiples, Convolve, Bode, Utility, reverbs Vintage/Nitrous/Basin |
| Séquence | — | CLIP (12) et ARP (12), clavier avec Key/Scale/Swing/OSC Mapping |
| Formats | VST2/VST3/AU/AAX, `.fxp` | VST3/AU/AAX seulement, `.SerumPreset` ; `.fxp` importable, pas l'inverse ; Serum 1 en fin de vie |
| Verrous | par paramètre | par groupe (2.0.21–2.0.22 ont retiré le grain fin) |

---

## 14. Index : où est quoi

| Je cherche… | Page / panneau | Plage utile |
|---|---|---|
| Le moteur d'un oscillateur (wavetable, sample, granulaire…) | OSC › menu en tête du panneau A/B/C | 5 moteurs |
| La table et la position | OSC › WT menu, WT POS | 1–256 |
| Un warp (sync, FM, PWM, distorsion d'osc) | OSC › WARP 1 / WARP 2 | § 4 |
| Unisson, détune, largeur, stack, mode de détune | OSC › bloc unison ; GLOBAL › Unison settings (Range, Width, Warp, WT Pos, Tuning) | 1–16, 0–1, 0–48 st |
| Phase de départ, phase aléatoire | OSC › PHASE, RAND | 0–360°, 0–100 % |
| Hauteur fixe (drums), accord en ratio (FM) | OSC › Pitch track ; mode Ratio/Harmonics | ratio −1…24 |
| Zone de clavier ou de vélocité d'un osc | Clavier › OSC Mapping | 0–127 |
| Le sub, ses formes | OSC › SUB | 6 formes |
| Bruit, couleur, one-shot, key track | OSC › NOISE | White/Pink/Brown/Geiger |
| Qui va dans quel filtre, série/parallèle, Direct | MIX › routage par canal ; MIX › sortie des filtres | Filter/Main/Direct/None |
| Envois d'effets partagés | MIX › BUS 1 / BUS 2 ; FX › racks BUS | |
| Type de filtre, VAR, drive propre, key track | OSC › FILTER 1/2 (ou FX › Filter pour la somme) | 96 types |
| Enveloppe de filtre | ENV 2 → glisser sur CUTOFF ; quantité dans MATRIX | −100…+100 |
| Enveloppe en tempo, delay, hold | ENV › BPM, DELAY, HOLD | 0–32 s |
| LFO libre / redéclenché / one-shot | LFO › Mode Off / Trig / Env | |
| LFO en marches, en chaos, en tracé XY | LFO › Grid + Shift-clic ; Type Lorenz/Rössler ; Type Path (+ sortie Y) | |
| Vibrato retardé | LFO › DELAY + RISE → pitch (FINE ou CRS) | 0–4 s |
| Faire bouger la forme d'un LFO | clic droit sur un point › Modulate X/Y › LFO Bus | 16 bus |
| Vélocité qui module la profondeur d'une modulation | MATRIX › colonne Aux source | |
| Unipolaire / bipolaire, courbe, bypass d'une modulation | MATRIX › ligne | |
| Un oscillateur ou un filtre comme modulateur audio | MATRIX › sources OSC A/B/C, SUB, Filter 1/2 | |
| Macros, leurs noms, chaînage | bas droite MACRO 1–8 ; MATRIX (macro comme destination ou aux) | 0–100 |
| Compresseur multibande avec sidechain interne | FX › Compressor › MULTIBAND + MATRIX sur une bande | |
| Limiteur true-peak | FX › Compressor › RATIO au maximum (Limit) | attaque 0–10 ms |
| Réverb à convolution, IR de cab | FX › Convolve | IR/Factory |
| Frequency shifter | FX › Bode | |
| Traitement bas/haut ou mid/side séparé | FX › Splitter L/H, L/M/H, M/S | |
| Mono sous une fréquence, polarité | FX › Utility › MONO BASS, POLARITY INV | 20–400 Hz |
| Polyphonie, mono, legato, glide | bas droite Voicing / Porta ; GLOBAL | 1–32 voix, 0–8 s |
| Qualité CPU / oversampling | GLOBAL › Quality (Draft/High/Ultra) + verrou | 1×/2×/4× |
| Accordage A = 432, micro-tonal | GLOBAL › Tuning ; .TUN ; MTS-ESP | 430–450 Hz |
| Son Serum 1 fidèle | GLOBAL › S1 Compatibility | |
| Automation rapide exacte | GLOBAL › Disable Smoothing | |
| Gamme, tonalité, swing, transposition globale | Clavier › KEY, SCALE, SWING, TRANSPOSE | swing 12,5–87,5 % dans Live |
| Séquence ou arpège interne | Clavier › CLIP / ARP ; `serum2-fx-clip-arp.md` | 12 + 12 slots |
| Envoyer le MIDI du clip/arp vers Live | GLOBAL › MIDI OUT | Off / Clip Player / On |
| Rendre un paramètre FX automatisable dans Live | clic droit sur le contrôle › Automate, puis Configure | plafond 128 |
| Où sont les presets et les tables | menu logo › Show Serum Presets Folder | § 11.2 |

---

## 15. Lacunes assumées et points à tester

- **MUET dans toutes les sources** : nombre exact de types de filtre de Serum 2 (au-delà des 96 de Serum 1) ; libellés affichés des warps `kFMX_*`, `kFMP_*`, du mode de hauteur Ratio/Harmonics et de `kParamUnisonSpan` ; correspondance Nitrous/Basin ↔ `kSpace`/`kAbyss` ; nombre de lanes d'automation d'un clip et de pas d'un pattern d'arp ; liste textuelle des SHAPE de l'arp ; pré/post fader des envois BUS ; fonction de `sampleFromAudioInput` sur le bruit ; coordonnées d'OSC C et de FILTER 2 dans la capture 1190 × 759.
- **À tester sur ce Mac** `[TEST]` : `-_PluginAutoPopulateThreshold=128` avec le VST3 ; Save as Default Configuration puis relecture des index ; lecture d'une capture de la page GLOBAL pour figer les libellés exacts (Quality, préférences) ; un preset avec OSC Mapping et un clip preview pour vérifier l'export MIDI OUT vers Live.
- **Où compléter** : le manuel officiel (354 pages, https://xferrecords.com/manual/serum-2/docs, servi comme PDF sans extension) est la seule source qui tranche les MUET ; le premier téléchargement depuis le Mac l'a enregistré en texte corrompu, `fetch_sources.py` reconnaît désormais un PDF à son contenu et `pdf_vers_md.py` en fera un fichier par chapitre dans `corpus/constructeur/` ; les pages `using-the-serum-keyboard`, `using-knobs-and-sliders`, `resizing-the-ui` sont listées dans `../../../../corpus/sources-a-telecharger.json` pour le script `fetch_sources.py` du Mac.
