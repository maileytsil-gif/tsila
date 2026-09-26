---
titre: "Rapport de recherche — axe 4 : documentation constructeur appliquée aux cuivres (Serum 2, Live 12, Native Instruments, Waves, FabFilter, iZotope, oeksound, SFZ)"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: rapport de recherche
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE 4 — Documentation constructeur des outils installés, appliquée aux cuivres

Recherche du 24 septembre 2026. Rapport destiné au skill « cuivres » (Ableton Live 12.4 + Serum 2 2.1.x), sur le modèle du skill basses.

## 0. Conditions de la recherche et légende des preuves

**Contrainte réseau, à lire avant tout.** La politique réseau de cet environnement a refusé l'accès à tous les domaines constructeurs pendant la séance : `xferrecords.com` (et `www.`, `static.`, `support.`), `ableton.com` (et `help.`, `cdn-resources.`), `native-instruments.com` (et `docs.`, `support.`), `oeksound.com`, `fabfilter.com`, `waves.com` et `assets.wavescdn.com`, `plugin-alliance.com` et `files.plugin-alliance.com`, `izotope.com`, ainsi que tous les hôtes miroirs de manuels essayés (archive.org, manuals.plus, device.report, manualslib, synthmanuals, promusic.cz, av-iq, bhphotovideo, cloudfront Ableton/Spitfire, equipboard) et les sites de tutoriels (edmprod, monosounds, production-expert, tapeop, soundonsound, dubspot, kvraudio, wikipedia). Un `curl` direct renvoie `CONNECT tunnel failed, response 403`. Pour relire ces pages, l'accès réseau de l'environnement doit être élargi (menu de l'environnement cloud › Edit › Network access) ou les domaines ci-dessus ajoutés à la liste autorisée.

Seuls `github.com`, `raw.githubusercontent.com`, `gist.github.com` et deux buckets S3 (`izotopedownloads`, `decembercymatics`) ont répondu. La recherche web (moteur) fonctionne mais ne rend que des extraits.

En conséquence, les tags de ce rapport sont plus fins que les trois tags du skill basses :

| Tag | Sens |
|---|---|
| **[DOC]** | Document constructeur lu intégralement aujourd'hui (texte primaire), avec l'URL exacte lue. Quand la lecture s'est faite sur une **copie GitHub** du texte officiel, c'est dit explicitement. |
| **[DOC-LOCAL]** | Fait tiré du **dépouillement local du manuel officiel Serum 2 (354 pages)** déjà présent dans le dépôt de l'utilisateur (`sound-designer-serum/references/serum2-fx-clip-arp.md`, `moteurs-synthese.md`, `modulation-effets.md`), avec numéro de page du manuel. Le manuel n'a pas pu être relu aujourd'hui. |
| **[DOC-EXTRAIT]** | Extrait d'une **page officielle** renvoyé par le moteur de recherche ; la page elle-même n'a pas pu être ouverte. À requalifier en [DOC] après relecture sur un réseau non filtré. |
| **[HEUR]** | Tutoriel, revue, dépôt tiers, ou déduction. |
| **[MÉMOIRE, non vérifié]** | Vient de ma mémoire, aucune page lue ne le confirme. |
| **[TEST]** | À valider dans le Set. |

Le rapport ne contient aucun chiffre inventé : là où une valeur manque, c'est écrit.

---

## 1. Xfer Serum 2 (2.1.x)

### 1.1 Ce que dit Xfer de l'architecture (extraits officiels)

- [DOC-EXTRAIT] Web-manual, page « Exploring Serum » (`https://xferrecords.com/web-manual/serum-2/exploring-serum`) : « Serum 2 is an advanced virtual synthesizer that offers a unique blend of sound generation methods together with a powerful modulation system. Serum combines wavetable, subtractive, multi-sampled, sampled, granular, and spectral synthesis into an intuitive and cohesive workflow. »
- [DOC-EXTRAIT] Page produit (`https://xferrecords.com/products/serum-2`) : « Serum 2 features three main oscillators where you can choose from Wavetable, Multisample, Sample, Granular, and Spectral modes. »
- [HEUR] Dossier de recherche tiers lu sur GitHub (`https://raw.githubusercontent.com/srobinson/mdx/HEAD/research/synth-daw-ui-drag-mod-racks-graphs-vendor-docs-2026.md`), qui cite le manuel : « OSC A/B/C plus dedicated Sub and Noise, dual filters, mixer, FX, LFO/envelope strip, and a matrix » ; « Routing is a popover on the module, sending to Filter 1/2, Main, Direct, None, or Bus 1/2 » ; « LFOs (up to 10) and envelopes (4) use a drawable editor » ; « Four macros exist ». Ce dossier donne les slugs exacts du web-manual : `/routing-an-oscillator-or-filter`, `/copying-a-module`, `/using-knobs-and-sliders`, `/undo-and-redo` ; d'autres slugs relevés dans les résultats : `/welcome`, `/getting-started`, `/exploring-serum`, `/using-the-serum-keyboard`, `/enabling-pitch-tracking`, `/displaying-help-tooltips`.
- Index du manuel PDF : `https://www.xferrecords.com/manual/serum-2/docs` (354 pages, déjà dépouillé localement).

**Ce qui est Serum 2 et pas Serum 1** (le manuel Serum 1.0.1 a été lu intégralement aujourd'hui : `https://s3.amazonaws.com/decembercymatics/Serum_Manual.pdf`, texte extrait du PDF) :
- [DOC] Serum 1 : « There are 3 Envelopes in Serum. The first envelope, ENV1, is "special" as it is dedicated for Amp » ; 4 LFO (« LFO 1 … LFO 4 » dans le manuel 1.0.1, 8 dans les versions ultérieures [MÉMOIRE, non vérifié]). Serum 2 : 4 enveloppes [HEUR, convergent], jusqu'à 10 LFO [HEUR].
- [DOC] Serum 1 n'a que des oscillateurs wavetable + Sub + Noise (samples WAV dans `Serum Presets/Noises`). Les modes **Multisample, Sample, Granular, Spectral** sont propres à Serum 2 [DOC-EXTRAIT].
- [DOC] Serum 1, effets : Reverb « Plate reverb algorithm courtesy of Togu Audio Line » **uniquement** ; Compressor avec commutateur « Multiband: … The individual bands are not user-adjustable separately » ; Chorus « 4-voice chorus effect, with 2 L and 2 R chorus taps » ; Hyper « micro-delay chorus effect with a variable number of voices (1-7) » ; Distortion « 13 different distortion types, including 2 dual-waveshaper modes ». Serum 2 : reverb à 5 types, compresseur multibande à bandes réglables, racks d'effets (voir 1.10).
- [DOC] Serum 1, LFO : « LFO Mode (Trig / Env / Off) … Env : similar to Trig, except the LFO will stop once it reaches the right-edge of the graph (plays once, like an envelope) » ; **Rise, Delay et Smooth existent déjà dans Serum 1** (voir 1.5). Donc le vibrato retardé n'est pas une nouveauté Serum 2 ; ce qui est nouveau, ce sont les modes Chaos/Path et la synchro BPM des Delay/Rise [HEUR].
- [DOC] Serum 1, voicing : Mono, Legato, Poly, Porta, Porta Curve, 'Always', 'Scaled' — tous déjà présents (voir 1.12).

### 1.2 Moteur Multisample

- [DOC-EXTRAIT] Page produit : « The multi-sample oscillator mode uses the open SFZ format, which is also supported by many other tools and is easily editable. Serum 2 ships with a massive, exclusive library of real instruments recorded around the world, and you can create or import your own from multisample recordings using the sfz file format. » Une autre formulation officielle relevée : « a massive, exclusive, and original library of real instruments recorded around the world, including orchestra, choir, pianos, guitars, and much more ».
- **Cuivres dans le contenu d'usine : non vérifié.** Aucun résultat ne liste les multisamples d'usine ; « orchestra » laisse supposer des cuivres d'orchestre, mais rien ne le documente. [TEST] : ouvrir le navigateur du Multisample dans Serum 2.1.5 et relever les dossiers (Brass ? Horns ?).
- **Formats acceptés** : le format déclaré est SFZ (fichier texte) + samples. Le manuel n'a pas pu être lu ; un extrait de recherche d'origine non officielle (agrégateur de changelog) mentionne pour 2.1.5 un correctif « loop endpoints being off by one when loading SFZ/WAV/FLAC files », ce qui indique la lecture de **WAV et FLAC** [HEUR, à confirmer sur le changelog officiel].
- **Procédure d'import** [HEUR — manuels d'éditeurs tiers Impact Soundworks et DiViNe Samples, cités par le moteur de recherche, pages bloquées] : « select the MULTISAMPLE type on your chosen oscillator, click Load SFZ and select the .sfz file, or drag and drop the .sfz file onto the Serum 2 oscillator. You can also drop the unzipped instrument folder into the Serum 2 Presets\Multisamples\User folder and rescan the folders for the instrument to be recognized. » Le README du convertisseur `sf2-to-sfz` (lu sur `https://github.com/bashexplode/sf2-to-sfz`) confirme le chemin Windows : « copy the folder it outputs directly into your `Documents\Xfer\Serum 2 Presets\Multisamples\User` folder ». Sur le Mac de l'utilisateur, le dossier de presets relevé localement est `/Library/Audio/Presets/Xfer Records/Serum 2 Presets/Presets/User` [DOC-LOCAL, `vst-sound-design/references/serum2.md`] ; le sous-dossier `Multisamples/User` reste à vérifier [TEST].
- **Zones** : ce que Serum 2 lit exactement dans un SFZ (couches de vélocité, round robins `seq_position`, keyswitches `sw_*`, `trigger=legato`, crossfades `xfin/xfout`) **n'a pas pu être vérifié** : aucun résultat officiel ne le liste. Un extrait de forum indique seulement que « current Serum 2 does not import loop points that are embedded in wav files » [HEUR].
- **Le format SFZ lui-même** est documenté et a été lu sur la source du site officiel (`https://raw.githubusercontent.com/sfzformat/sfzformat.github.io/source/docs/index.md`, `.../tutorials/basics.md`, `.../tutorials/sustained_note_basics.md`, `.../tutorials/legato.md`, `.../tutorials/vibrato.md`) [DOC] :
  - « The SFZ format is a file format to define how a collection of samples are arranged for performance » ; le fichier ne contient pas l'audio.
  - Hiérarchie `<global>`, `<group>`, `<region>` ; opcodes de base `sample=`, `lokey/hikey` (ou `key`), `pitch_keycenter`, `lovel/hivel`, `volume`, `ampeg_release` (« accomplishes this », pour éviter les coupures sèches).
  - Couches de dynamique tenues : `xfin_loccN/xfin_hiccN` et `xfout_loccN/xfout_hiccN` permettent de « vary the dynamic level while a note is being sustained » (crossfade piloté par CC1) ; `loccN/hiccN` sélectionne une articulation selon un CC (« which sample is triggered for a particular note depends on the value of a MIDI CC »).
  - Legato : « the trigger opcode is used to separate regions into initial and legato » ; `group=1 off_by=1 off_mode=normal` pour qu'« only one be played at a time » ; `sw_previous` choisit le sample de transition. Réserve documentée : « the portamento is very obviously fake for slow glides across long intervals, but as long as the interval is no more than a third or fourth, it can be convincing ».
  - Vibrato SFZ 2 : `lfo01_freq=2`, `lfo01_pitch_oncc111=35`, `lfo01_delay_oncc115=0.500`, `lfo01_fade_oncc116=0.500` (« The examples here use SFZ 2 spec numbered LFOs, rather than the dedicated pitch, volume and filter LFOs and envelopes of SFZ 1 »).
  - **Application cuivres** : un multisample perso « trompette » minimal = régions `lokey/hikey/pitch_keycenter` + 2 à 3 couches `lovel/hivel`. Tout ce qui dépasse (crossfade CC1, legato `trigger`, keyswitch `sw_*`) est [TEST] dans Serum 2 : construire un SFZ de 4 régions et vérifier une opcode à la fois.

### 1.3 Moteur Spectral (resynthèse d'une trompette)

- [DOC-EXTRAIT] Page produit : « The Spectral Oscillator allows for realtime resynthesis of samples at the harmonic level, and transient detection processing similar to that found in advanced timestretching algorithms enables you to shape time and frequencies in radical ways. »
- [DOC] Changelog officiel Xfer, lu sur sa copie gist (`https://gist.github.com/0xdevalias/a537a59d1389d5aed3bc63b544c70c8d`) : 2.0.19 « Added new improved Spectral 'Pitch Shift' warp mode, the old one has been renamed to 'Pitch Blend' » ; 2.0.17 « Fixed Spectral Osc sometimes filling FFT buffer from wrong side of loop when playhead changes direction ».
- [DOC-LOCAL] `moteurs-synthese.md` : le mode Spectral « décompose un son en partiels individuels et permet de glisser d'une texture à une autre » ; avertissement Xfer « CPU intensive ».
- [HEUR] Pour une trompette : charger une note tenue, freezer la position de lecture pour obtenir une tenue infinie sans boucle, puis appliquer l'enveloppe et le vibrato de Serum. Les paramètres exacts (nom du contrôle de position, warp spectral) n'ont pas été lus : [TEST].

### 1.4 Moteur Sample

- [DOC-EXTRAIT] Page produit : « The sample oscillator offers looping with snap loop detection, flexible loop modulation, a Rate control for 'tape stop' effects and similar, sample slicing with realtime score extraction / playback and tails mode, and more. »
- [HEUR] Extrait de tutoriel : « the sample engine allows drag-and-drop one-shots ». Pour un stab de cuivre one-shot, c'est l'oscillateur à préférer au Multisample (un seul sample, pas de mapping) ; pour une ligne jouée sur deux octaves, le Multisample.

### 1.5 LFO — vibrato retardé

- [DOC] Manuel Serum 1 (mêmes contrôles présents dans Serum 2 d'après les captures locales) : « Rise this is the amount of time taken for the LFO graph shape to have influence over the LFO output … the LFO will begin with a "fixed" output … and slowly (based on the Rise time) becoming the shape of the visible graph. » « Delay this is the amount of time before the rise begins. » « Smooth this smooths the LFO output. » « LFO Rate is in beat-synced units by default (BPM switch on) but can also be made free to a Hz value. » Modes « Trig / Env / Off ».
- [HEUR] Les extraits de tutoriels Serum 2 nomment les modes **FREE, RETRIG, ENVELOPE** et disent que « DELAY and RISE are measured in note divisions when BPM sync is on ». Le nom exact des modes dans 2.1.5 est à relever à l'écran [TEST].
- [DOC-LOCAL] `modulation-effets.md` : Serum 2 ajoute **Chaos** (Lorenz, Rössler) et **Path** (tracé 2D, sorties X/Y) ; taux jusqu'à 1 kHz ; le choix unipolaire/bipolaire est dans la matrice, pas dans le LFO.
- [DOC] Changelog 2.0.22 : « Added 'Lock Module' options for envs, LFOs, note and velo curves » — utile pour garder un vibrato réglé en changeant de preset.
- **Recette cuivre** [HEUR] : LFO sinus 5–6 Hz → Pitch (profondeur faible, bipolaire), **Delay ≈ 300–500 ms puis Rise ≈ 300–600 ms**, mode Trig ; la profondeur sur la molette (CC1) comme aux source. Le protocole local de validation impose « vibrato audible dès le début de la note » comme condition d'arrêt [DOC-LOCAL, `validation-protocol.md`].

### 1.6 Enveloppes — scoop de hauteur

- [DOC-LOCAL] `moteurs-synthese.md` : Serum 2 ajoute **DELAY et HOLD** (DAHDSR), le DELAY synchronisable au tempo ; les enveloppes sont synchronisables au BPM ; une zone **Curve** dans MATRIX redéfinit la réponse.
- [HEUR] Extraits convergents : « four envelopes, with Env 1 permanently assigned to the amp » ; « BPM sync, inverse legato settings, and fully editable modulation remap curves » ; « you can double-click any envelope stage and type a beat division ».
- **Scoop** [HEUR] : Env 2 → Pitch de l'oscillateur, Attack 0, Decay 40–120 ms, Sustain 0, montant −1 à −3 demi-tons (donc départ sous la note et arrivée sur la note) ; sur un stab, Env 3 → cutoff avec un decay différent pour découpler brillance et hauteur. Valeurs = points de départ, à mesurer [TEST].

### 1.7 Matrice — sources

- [DOC] Manuel Serum 1 : « Some mod sources only exist in the Mod Matrix (no 'drag source' tile): Aftertouch (aka Channel Pressure), Chaos 1 and 2, Note-On Random 1 and 2, Noise Osc ». Velocity, Note, Mod Wheel, Pitch Bend existent comme tuiles [MÉMOIRE, non vérifié pour le libellé exact].
- [DOC-LOCAL] `modulation-effets.md` : ligne de matrice Serum 2 = source · destination · bipolaire/unipolaire · curve · **aux source** (« An aux source is a second source that scales the first one—the textbook example is velocity deciding how far an envelope opens the filter »).
- [DOC-EXTRAIT] Page produit : « Serum 2 is MIDI Polyphonic Expression (MPE) compatible … per-note pitch bends, slides, pressure ».
- [DOC] Changelog 2.1.5 (extrait non officiel) : « expression and mono aftertouch values not updating during mono legato playback » corrigé — signe que l'aftertouch est une source utilisable en mono legato [HEUR].
- **Recette cuivre** : Velocity → cutoff (unipolaire) et → montant de l'Env de filtre (aux) ; Mod Wheel → profondeur du vibrato et → drive ; Aftertouch → cutoff + niveau de souffle ; Note → cutoff en key-tracking. [HEUR]

### 1.8 Filtres utiles

- [DOC-LOCAL] `moteurs-synthese.md` : `MG Low 6/12/18/24` (ladder Moog), `Low/High 6/12/18/24`, `Band/Peak/Notch`, `MG Ladder`, `Acid Ladder`, `EMS Ladder`, `MG Dirty` ; paramètre **FAT** = saturation dans le chemin de résonance.
- [DOC-EXTRAIT] Web-manual (extrait) : « Filter Type is chosen with a menu at the top of the filter module … "MG Low 12" in the picture » ; « Each of the formant filters are optimized for different vowel transitions when adjusting the cutoff parameter. »
- [DOC] Manuel Serum 1 (liste toujours valable en 2 pour les combs/formants, à confirmer [TEST]) : « Formant 1-3 Formant 'vowel' filters. Cutoff knob morphs between the formants » ; « CombL / FlangeL / PhaseL : Comb/Flanger/Phaser with a Lowpass filter in the internal feedback circuit ».
- [DOC-LOCAL] `serum2-fx-clip-arp.md` (manuel p. 170-172) : le module FX **Filter** « fonctionne exactement comme le filtre de synthèse par voix, mais tourne ici comme effet master » ; MG Low 6 par défaut ; knob VAR dont les étiquettes possibles incluent **FORMNT**, FAT, MORPH, COMBFRO, SCREAM, PAIN ; clic droit → Clean Mode (−24 dB puis +24 dB).
- **Application** : corps de cuivre = MG Low 12 ou 24 avec FAT modéré, key-track partiel ; « formant » de pavillon = un filtre Formant/Vowel en Filter 2 en parallèle, MIX bas, ou un Peak à Q modéré vers 1–2 kHz [HEUR].

### 1.9 FM from B/C, Warp modes, Noise

- [DOC-LOCAL] `moteurs-synthese.md` : FM en warp mode, trois variantes **Linear** (garde la hauteur), **Exp**, **Thru-Zero** ; source B, C, Noise, Sub, Filter 1/2 ; PD (Self/B/C/Noise/Sub/Filter) ; Alt Warp (Bend ±, PWM, Asym, Flip, Mirror, Remap 1-4, Quantize, Odd/Even) ; Distortion (Tube, Soft/Hard Clip, Diode 1/2, Linear/Sine Fold, …).
- [DOC-EXTRAIT] Page produit : « New Warp Modes include Serum 1's iconic PD (Phase Distortion) plus new true modular-style FM, dual-warp mode, and timbre-shifting warp types. »
- [DOC-EXTRAIT] Noise : « The noise oscillator has been expanded with new modes for typical noise colors: white, pink, brown, and Geiger ». Un tutoriel indique qu'on peut key-tracker le Noise [HEUR].
- **Souffle** : Noise pink ou brown, filtré passe-bande 1–4 kHz dans Filter 2, enveloppe courte à l'attaque puis niveau bas sur l'aftertouch/molette (macro « Breath » du schéma local) [HEUR]. **Brillance FM** : FM Linear from B (B en sinus, ratio 1:1 ou 1:2), index piloté par vélocité et Env 2, ce qui donne la « lèvre » d'un cuivre sans filtre [HEUR ; le manuel Live confirme le principe pour Operator, voir 2.1].

### 1.10 Effets (rack Serum 2)

[DOC-LOCAL] `serum2-fx-clip-arp.md`, pages du manuel entre parenthèses :
- 13 processeurs + 3 splitters, trois racks (MAIN, BUS 1, BUS 2), flux série du haut vers le bas (p. 152-158) ; « les effets sont monophoniques … comme des inserts après Serum » (p. 159) ; **une enveloppe sur un paramètre FX se re-déclenche à chaque note** en polyphonie.
- **CHORUS** : « quatre voix, deux taps à gauche et deux à droite » ; RATE 0–20 Hz ou synchro ; DELAY 1/2 ; LPF/HPF après le wet (p. 162).
- **COMPRESSOR** : SINGLE/MULTIBAND ; THRESH 0 % = 0 dB, 100 % = −120 dB ; RATIO max = « Limit », vrai true-peak limiter ; en MULTIBAND : X-LOW, X-HIGH, BELOW (compression ascendante), H/M/L ; les bandes acceptent des assignations de matrice, usage sidechain cité (p. 162-164).
- **REVERB** : « version modifiée de l'algorithme Tal Reverb », 5 types **PLATE, HALL, VINTAGE, NITROUS, BASIN** (p. 175-177).
- **DISTORTION** : 13 types, X-Shaper, filtre OFF/PRE/POST avec Key Track (p. 167-169).
- **HYPER/DIMENSION** : « le manuel recommande explicitement d'utiliser HYPER plutôt que des réglages d'unisson élevés pour économiser du CPU » (p. 173-174).
- [DOC] Changelog 2.0.17 : « Added Key Track option to Filter and Distortion FX freq right-click menus ».
- **Application** : section de cuivres = Chorus court (Delay ≈ 5–8 ms, Depth faible) ou Hyper 2-3 voix plutôt qu'unisson ; Compressor Single ratio 3:1 pour tenir les stabs ; Reverb Hall ou Vintage sur BUS 1 avec LO CUT [HEUR].

### 1.11 CLIP et ARP

[DOC-LOCAL] `serum2-fx-clip-arp.md` : CLIP = clip MIDI interne, 12 slots par banque, TRIGGER MODE Mono/Poly, KB SPAN Mono/Poly/Offset relatif à C3, MODE Random/Rand.No Dup/Rand.Start/Rand.End/Static (p. 219-243) ; ARP = 12 par banque, PATTERN MODE 8 valeurs, STEP MODE Normal/New Only/Chord/Chord (new), TRANSPOSE 18 formes, **pas de paramètre « octaves »**, LATCH piloté par CC64, GATE relatif au RATE, CHANCE (p. 244-266) ; swing global sur la page clavier, plage Ableton 12,5–87,5 % (p. 269). [DOC-EXTRAIT] web-manual `/using-the-serum-keyboard` : « the on-screen keyboard indicates which notes are being played through the Serum clip player and arpeggiator ». Pour des riffs de cuivres : Step Mode **Chord** joue toutes les notes tenues à chaque pas (stabs d'accord rythmés) [HEUR].

### 1.12 Mono / Legato / Portamento

- [DOC] Manuel Serum 1 (contrôles identiques observés dans Serum 2.1.5, boutons MONO/LEGATO/PORTA relevés à l'écran [DOC-LOCAL `serum2.md`]) : « Legato is only audible with Mono switch is enabled. When a mono voice is interrupted, the state of the Legato switch determines whether or not the Envelopes/LFO's will re-trigger. When Legato is enabled, the envelopes do not re-trigger » ; « 'Always' switch — When activated, the portamento will occur on a new note even if no note is currently playing. When Off, a note must be held for portamento to take place on the (2nd) note » ; « 'Scaled' switch … the portamento rate is adjusted based on the distance of transversal between the source and destination pitches » ; « Porta Curve … If set convex (typical use) … the note pitch will depart the beginning pitch quickly and slow down as it nears the note destination ».
- [HEUR] Extrait tutoriel Serum 2 : « The ALWAYS option above the PORTAMENTO will make the lead glide even if the MIDI notes don't overlap. »
- **Application** : solo de trompette = MONO + LEGATO, Porta court (30–60 ms), **Always off** (glisse seulement sur les notes liées), Scaled on ; enveloppes non retriggées en legato → l'attaque « langue » vient du MIDI (notes séparées) [HEUR].

### 1.13 Unison

- [DOC] Manuel Serum 1 : « The classic "magic number" for unison is 7. Serum will allow you to stack up to 16 voices … as you stack more voices the resulting sound becomes more "cloudy" » ; « Unison Blend … the amount of level offset of the unison voices versus the 'central' unison voice or voices … "wet/dry" blend » ; Stack « 12 (1x) … every 2nd unison voice will play up an octave ».
- [DOC-LOCAL] `moteurs-synthese.md` (Serum 2) : MODE Linear/Exp/Inv/Random ; STACK Off / 12 (1-3x) / 12+7 (1-3x) / Center-12 / Center-24 ; BLEND défaut 75 % ; WIDTH, RANGE, WT POS, WARP 1/2 par voix.
- **Application** : « section » de cuivres = unison 3 (Random, detune faible) ou 2 avec Blend 50 % ; passer le test mono du protocole local ; préférer Hyper pour le CPU [HEUR]. Une trompette solo = unison 1.

---

## 2. Ableton Live 12 (manuel de référence)

**Source lue** : le texte du manuel officiel Live 12, chapitres 24 (« Instrument, Drum and Effect Racks »), 28 (« Live Audio Effect Reference ») et 30 (« Live Instrument Reference »), lu **intégralement** sur une copie fidèle hébergée sur GitHub (`https://raw.githubusercontent.com/djaboxx/iron-static/HEAD/docs/api/ableton/30-live-instrument-reference.md`, `.../28-live-audio-effect-reference.md`, `.../24-instrument-drum-and-effect-racks.md`, 250 Ko, 240 Ko et 31 Ko, numéros de page du PDF conservés). L'URL officielle correspondante est `https://www.ableton.com/en/manual/live-instrument-reference/` (bloquée aujourd'hui). Tag : **[DOC, via copie GitHub]** ; les citations ci-dessous sont textuelles.

### 2.1 Operator — cuivres FM

- « Operator offers eleven predefined algorithms that determine how the oscillators are connected … Signals will flow from top to bottom between the oscillators shown in an algorithm icon. The algorithm selector can be mapped to a MIDI controller, automated, or modulated in real time. »
- « Any oscillator that is not modulated by another oscillator can modulate itself, via the Feedback parameter in its display. »
- « Operator has seven envelopes: one for each oscillator, a filter envelope, a pitch envelope and an envelope for the LFO. All envelopes feature some special looping modes. Additionally, the filter and pitch envelopes have adjustable slopes. » « Each oscillator's volume envelope is defined by six parameters: three rates and three levels. » « The envelopes can also be modified by note velocity and note pitch with the Vel and Key parameters. »
- Pitch envelope : « The pitch envelope can be turned on or off for each individual oscillator and for the LFO using the Destination A-D and LFO buttons … The pitch and filter envelopes each have an additional parameter called End, which determines the level the envelope will move to after the key is released. » « Pitch Envelope Amount … A value of 100% means that the pitch change is exactly defined by the pitch envelope's levels. A value of -100% inverts the sign. »
- Glide : « Operator includes a polyphonic glide function. When this function is activated, new notes will start with the pitch of the last note played and then slide gradually to their own played pitch. » « Glide (G) — … Note that all envelopes are not retriggered in this case if notes are being played legato. » Mono : « If Voices is set to 1, another effect occurs: Overlapping voices will be played legato, which means that the envelopes will not be retriggered from voice to voice, and only pitch will change. »
- LFO : « The LFO in Operator can practically be thought of as a fifth oscillator. It runs at audio rates, and it modulates the frequency of the other oscillators. It is possible to switch LFO modulation on or off for each individual oscillator (and the filter) … The LFO offers a choice of classic LFO waveforms, sample and hold (S&H), and noise. » « The LFO's intensity is also affected by its envelope. » (l'enveloppe du LFO donne donc un vibrato retardé natif.)
- Sources MIDI : « The MIDI controllers Velocity, Key, Aftertouch, Pitch Bend and Mod Wheel can be mapped to two destinations each. »
- Filtre : « low-pass, high-pass, band-pass, notch, and a special Morph filter. Each filter can be switched between 12 and 24 dB slopes as well as a selection of analog-modeled circuit behaviors developed in conjunction with Cytomic » (Clean, OSR, MS2, SMP, PRD) ; « "Play by Key" … setting Freq < Key to 100% and setting the cutoff to 466 Hz ».
- Aliasing : « FM synthesis is especially likely to produce this kind of effect … Operator minimizes aliasing by working in a high-quality Antialias mode. »
- **Recette cuivre FM** [HEUR] : algorithme 2 opérateurs en série (B→A), A et B sinus, B Coarse 1 (rapport 1:1, spectre de type scie), niveau de B = enveloppe A 30–80 ms / D 300 ms / S 60 % et « Lev < Vel » élevé ; Feedback sur B 10–20 % ; Pitch Env : Initial −2 st, Attack 40–80 ms vers 0 ; LFO sinus 5,5 Hz → Osc A/B avec enveloppe de LFO en attaque 400 ms (vibrato retardé) ; Voices 1 pour la trompette solo, Spread 0.

### 2.2 Analog — synth brass analogique

- Oscillateurs : « two oscillators and a noise generator … can be independently routed to two different multi-mode filters » ; « The Shape chooser selects the oscillator's waveform. The choices are sine, sawtooth, rectangular and white noise. When rectangular is selected, the Pulse Width parameter is enabled … At 100%, the waveform is a perfect square … The pulse width can also be modulated by an LFO. » « When the Mode chooser is set to Sync, the oscillator's waveform is restarted by an internal oscillator whose frequency is set by the Ratio slider. » « The Pitch Env settings apply a ramp that modulates the oscillator's pitch over time. Initial sets the starting pitch … while Time adjusts how long it will take for the pitch to glide to its final value » (scoop natif par oscillateur).
- Filtres : « 2nd and 4th order low-pass, band-pass, notch, high-pass and formant filters ».
- Enveloppes : « Each envelope is a standard ADSR … The Slope switches toggle the shape of the envelope segments between linear and exponential. » « With Legato enabled, a new note that is played while another note is already depressed will use the first note's envelope, at its current position. » « Enabling the Free switch causes the envelope to bypass its sustain phase » ; Loop Off/AD-R/ADR-R/ADS-R.
- LFO : « The Delay slider sets how long it will take for the LFO to start after the note begins, while Attack sets how long it takes the LFO to reach its full amplitude. »
- Vibrato : « Analog's vibrato effect is essentially an additional LFO, but is hardwired to the pitch of both oscillators … The Delay slider sets how long it will take for the vibrato to start after the note begins, while Attack sets how long it takes for the vibrato to reach full intensity. The Error slider adds a certain amount of random deviation … The Amt < MW slider adjusts how much the modulation wheel will affect the vibrato intensity. »
- Unison : « The Voices chooser selects between two or four stacked voices, while the Delay slider increases the lag time before each stacked voice is activated. » Glide : « With Legato enabled, the sliding will only occur if the second note is played before the first note is released » ; modes Const / Prop.
- **Recette synth brass** [HEUR] : Osc 1 scie, Osc 2 scie Detune +8 cents (ou rectangle PW 45 % + LFO lent sur la largeur), filtre LP 4e ordre cutoff 900 Hz, Env filtre A 60 ms D 250 ms S 55 % avec Env < Vel, Amp A 30 ms, Vibrato Delay 0,4 s Attack 0,5 s Amt < MW, Unison 2 voix Detune faible, Glide Legato/Prop. Le formant filter d'Analog en Filter 2 parallèle donne le « pavillon » [TEST].

### 2.3 Wavetable

- Unison : six modes « Classic: The oscillators are detuned with equal spacing and panned to alternating stereo channels. Shimmer: The oscillator pitches are jittered at random intervals … Noise: … at a much faster rate, resulting in noisy breathy textures … Phase Sync: … the phases are synced when a note is started giving a strong sweeping phaser-style effect. Position spread … Random note ». « The Voices slider sets the number of simultaneously running oscillators per wavetable oscillator. »
- Sub : (30.13.3, résumé du dossier tiers lu : « sine with selectable octave, and an Additional Harmonics control ») [HEUR pour la formule exacte].
- MIDI/Matrice : « When Velocity is assigned … When Note is assigned … The pitch modulation range is centered around C3. This means when it is assigned to Filter Frequency with the modulation amount set to 100%, the filter will precisely track the played note. » « Pitch Bend, Aftertouch and Modulation Wheel … When Random is assigned … » Enveloppes Amp/Env 2/Env 3 avec Initial/Peak/Sustain/Final et Slopes ; LFO « Attack slider to adjust the time the LFO takes to fade in ».
- Mono/Glide : « The Poly/Mono toggle switches the instrument between a single voice with legato envelopes (Mono) and a polyphonic instrument (Poly). » « Glide … only active when … Mono. »
- MPE : le dossier tiers affirme « Live 10+ Wavetable is MPE-aware — per-note pressure, slide, and glide all route through the modulation matrix » [HEUR] ; le texte 30.13 lu ne contient pas le mot MPE (Analog, Collision, Drift, Meld l'ont explicitement).
- « As long as no modulation is applied, the raw output of the oscillators is perfectly band-limited » ; Hi-Quality off par défaut depuis 11.1, jusqu'à 25 % de CPU en moins.
- Application : « Noise » unison = texture soufflée d'ensemble ; Env 3 → Pitch pour le scoop ; Note → cutoff 100 % = key-tracking exact [HEUR].

### 2.4 Meld — y a-t-il un moteur cuivre/formant ?

- « Engines A and B each have a selection of twenty-four oscillator types to choose from, including six scale aware oscillators. » Liste lue dans 30.8.3 : Basic Shapes, Dual Basic Shapes, Noisy Shapes, Square Sync, Square 5th, Sub, Swarm Sine/Triangle/Saw/Square, Harmonic Fm, Fold Fm, Squelch, Simple Fm, Chip, Shepard's Pi, Tarp, Extratone, Noise Loop, Filtered Noise, Bitgrunge, Crackle, Rain, Bubble, Chord. **Aucun oscillateur nommé Brass, Wind, Voice ou Formant.**
- Filtres (17) : « The Vowel filter is a formant filter that mimics the characteristics of vowels being pronounced, with various configurations that can be morphed through using the filter's Morph macro knob. » Aussi SVF 12/24, MS2 LP/HP, OSR BP, LP Crunch, LP Switched Res, Filther, Eq Peak/Notch, Phaser, Redux, Comb +/−, Plate Resonator, Membrane Resonator.
- Glide : « two glide modes, Portamento (Porta) and Glissando (Gliss) … Glide is active in both Mono and Poly modes. » Legato : « When Mono is activated, the Legato switch can be toggled … the new note will use the original note's envelope ». Limiteur par voix.
- Conclusion : pour un cuivre, Meld = Swarm Saw (Motion/Spacing) ou Harmonic Fm en A, filtre Vowel ou Eq Peak en B pour le formant ; c'est une construction, pas un preset dédié [HEUR].

### 2.5 Drift

- Formes : Sine, Triangle, Shark Tooth, Saturated, Saw, Pulse, Rectangle [DOC-EXTRAIT + dossier tiers] ; filtres « Type I (12 dB/octave) and Type II (24 dB/octave) » [DOC].
- Voice modes lus : « Poly … up to 32 voices », « Mono … rendered using four voices to produce a unison effect depending on the Mono Thickness value », « Stereo uses two voices per note », « Unison slightly detunes the four voices ». « When the Voice Mode is set to Mono, you can enable the Legato switch so that triggering a new voice will change its pitch without resetting its envelopes. The Glide slider … »
- Drift est le choix le plus simple pour un synth brass mono rapide (Saw + Shark Tooth, Mono Thickness, Legato) [HEUR].

### 2.6 Sampler et Simpler

- Sampler : « handle multi-gigabyte instrument libraries with ease, and it imports most common library formats » ; Zone Editor « three types of ranges — the Key Zone, the Velocity Zone and Sample Select Editors » ; « Velocity zones determine the range of MIDI Note On velocities (1-127) that each sample will respond to » ; crossfades : « Zones can also be faded over a number of semitones at either end … The Lin and Pow boxes … linear or exponential » ; **Round Robin** : « Forward / Backward / Other / Random » avec « Reset Interval ».
- Glide : « Glide — The global Glide mode … 'Glide' is a standard monophonic glide, while 'Portamento' works polyphonically. » Voix : « up to 32 simultaneous voices … Retrigger button (R) ». **Aucun commutateur Legato n'est documenté dans Sampler** (le mot n'apparaît pas dans 30.10) ; **aucun keyswitch natif** : le mot n'apparaît pas dans le chapitre. Le MIDI tab mappe « Key, Velocity, Release Velocity, Aftertouch, Modulation Wheel, Foot Controller and Pitch Bend … to two destinations each ».
- Sample Select : « Sample Select zones are very similar to the Chain Select Zones found in Racks » — c'est le mécanisme pour changer d'articulation par un paramètre continu (macro), pas par une note.
- Import tiers : « Sampler can use the following third-party sample formats: REX files … ACID Loops, Soundtrack Loops » (le SFZ n'est pas cité ; l'import « most common library formats » n'est pas détaillé — [MÉMOIRE, non vérifié] : Live 12 ne lit pas les .sfz nativement).
- Simpler : « three playback modes » Classic / One-Shot / Slicing ; « Two glide modes are available: Glide, which works monophonically, and Portamento, which works polyphonically » ; Spread « two voices per note » ; Pitch Bend ±5 st.
- Keyswitch dans Live = racks (2.7).

### 2.7 Racks : chain select comme « keyswitch »

- « The three types of zones … are Key, Velocity, and Chain Select. » « The chain select zone is a data filter just like the other zones; … only those with chain select zones that overlap the current value of the Chain selector can be addressed. » « If the zone ends in a fade range, the chain's output volume is attenuated to zero while the Chain selector is outside of the zone. If the zone had no fade range, the output volume is not attenuated, allowing the chain's effects (like long reverb tails or delays) to fade out. »
- [DOC-EXTRAIT] help.ableton.com « Using the chain selector in a Rack » : le Chain selector se mappe sur une macro puis sur un contrôleur. Un vrai keyswitch (par note MIDI) exige un outil tiers (ex. éditeur KeySwitch de swub, [HEUR]) ou une automation de la macro.
- C'est exactement le mécanisme des packs Ableton (« all articulations switchable via a single macro control », 2.8).

### 2.8 Packs et bibliothèques avec cuivres réels

Pages `ableton.com/en/packs/...` bloquées ; extraits officiels :
- **Orchestral Brass** (`https://www.ableton.com/en/packs/orchestral-brass/`) [DOC-EXTRAIT] : « a thorough set of vivid and colorful brass instruments … solo and ensemble French horn, trombone, trumpet and tuba, with a unique set of articulations in multiple section sizes » ; « created in cooperation with SONiVOX » ; « special Rack versions of each instrument, with all articulations switchable via a single macro control in real time for maximum playability » ; « All instruments take advantage of SmartPriming, Live's new resource-efficient sample engine » ; « Instruments are loaded via Simpler ». Inclus dans Live 12 Suite avec Orchestral Strings/Woodwinds/Mallets [DOC-EXTRAIT, page « Packs by Ableton »]. **Taille et liste d'articulations : non trouvées.**
- **Brass Quartet** (`https://www.ableton.com/en/packs/brass-quartet/`) [DOC-EXTRAIT] : « created in collaboration with Spitfire Audio … trumpet, flugelhorn, tenor horn and trombone … performance techniques including staccatissimo, vibrato, pitch bend, hollow and flutter, with these playing styles being blendable and changeable on the fly using the technique Macro » ; manuel PDF officiel repéré : `https://d3a0bdvj9eysmp.cloudfront.net/ableton/Brass_Quartet_by_Spitfire_Audio.pdf` (bloqué) dont les extraits disent : « Short Staccatissimo is … even shorter than a Staccato », « Long Hollow is a gentle and round playing style with as few overtones as possible », « Long Flutter involves the player rolling a silent 'R' », « The Technique control was inspired by subtractive synths and changes the timbre by crossfading between different playing techniques » ; « included in Live 11 Suite ».
- **Orchestral Ensemble Essentials / 2** (ProjectSAM, Symphobia) [DOC-EXTRAIT] : « close-mic string, brass and woodwind ensemble sounds and one-shot orchestral effects » ; « brass, string, woodwind and full-orchestra sections … Symphobia series … Lumina ».
- **Session Drums** : sans objet (batterie).
- **Core Library « Brass »** : aucune page ne documente un instrument « Brass » du Core Library ; à relever dans le navigateur de Live [TEST].

### 2.9 Effets natifs utiles

- **Multiband Dynamics / OTT** : « allows for upward and downward compression and expansion of up to three independent frequency bands » ; « a single instance of Multiband Dynamics can provide six types of dynamics processing simultaneously » ; « The Amount knob adjusts the intensity of the compression or expansion applied to all bands. At 0%, each compressor/expander has an effective ratio of 1 » ; conseil de-essing : « enabling only the upper band and setting its crossover frequency to around 5 kHz … fairly fast attack and release times » (transposable à la dureté d'une trompette). Le nom du preset OTT n'est pas dans le manuel ; sa nature (compression ascendante + descendante sur 3 bandes) est celle décrite [DOC-EXTRAIT tutoriels].
- **Chorus-Ensemble** : « Classic mode … two time-modulated delayed signals » ; « Ensemble mode is inspired by a thick three-delay line chorus pedal used in the '70s … three delayed signals with evenly split modulation phase offsets » ; « Vibrato mode applies stronger modulation than a chorus to create pitch variation » ; high-pass 20–2000 Hz ; Width 0–200 % ; astuce « Ensemble mode at a rate between 1 Hz and 1.8 Hz and 100% Amount ».
- **Saturator** : huit courbes « Analog Clip, Soft Sine, Bass Shaper, Medium Curve, Hard Curve, Sinoid Fold, Digital Clip, and Waveshaper » ; filtres Color « remove bass frequencies before the shaper, so that only mid/high frequencies are saturated ». Pour un cuivre : Soft Sine ou Analog Clip, Drive faible, Color pour ne saturer que 800 Hz–4 kHz [HEUR].
- **Vocoder** (formants) : « The frequencies of the carrier's filterbank can be shifted up or down via the Formant knob » ; carrier « Noise / External / Modulator / Pitch Tracking » ; « Modulator uses the modulator itself as the carrier … resynthesized version » ; « Bands chooser … more bands results in a more accurate analysis » ; « Precise/Retro » ; « Depth … 100% results in "classic" vocoding ». Self-vocoding d'une section de cuivres + Formant = changement de « taille » de pavillon [HEUR].
- **Corpus** : résonateurs « Beam, Marimba, String, Membrane, Plate, Pipe, Tube » ; « Pipe simulates a cylindrical tube that is fully open at one end and has a variable opening at the other (adjusted with the Opening parameter). Tube simulates a cylindrical tube that is fully open at both ends. » ; « Radius … As the radius increases, the decay time and high frequency sustain both increase » ; sidechain MIDI « Frequency and/or Off Decay ». Pipe/Tube en insert à Dry/Wet faible = corps de tuyau accordé sur la note MIDI [HEUR].
- **Spectral Resonator** : « applying tuned resonances to its spectrum … Similar to a vocoder, you can use the MIDI input to place the resonances in key … playing the effect polyphonically with up to 16 voices » ; « Stretch … At 100%, only odd harmonics are produced » ; modulation « None, Chorus, Wander, or Granular » ; Unison + Uni. Amt.
- **Auto Filter** : dix types « Low-pass, High-pass, Band-pass, Notch, Morph, DJ, Comb, Resampling, Notch + LP, and Vowel » ; « The Vowel filter shapes the sound to resemble the human voice by emphasizing certain formants » ; circuits SVF, DFM, MS2, PRD ; envelope follower avec Attack/Release et sidechain externe.
- **Glue Compressor** : « based on the classic bus compressor from a famous 80's mixing console » ; « the knee becomes more sharp as the ratio increases » ; Auto Release « uses two times » ; Range « Values between about -60 and -70 dB emulate the original hardware » ; Soft clip « not a transparent limiter ».

---

## 3. Native Instruments

Toutes les pages NI ont été bloquées (`www.`, `docs.`, `support.native-instruments.com` ; `www.cdn.native-instruments.com` ne résout pas). Faits = [DOC-EXTRAIT] sauf mention.

### 3.1 Session Horns / Session Horns Pro
- Session Horns (`https://www.native-instruments.com/en/products/komplete/cinematic/session-horns/`) : « a trombone, tenor sax and two trumpets » ; « a tight, 4-piece brass section sampled in pristine quality ».
- Session Horns Pro (`https://www.native-instruments.com/en/products/komplete/cinematic/session-horns-pro/` et `/articulations/`) : « The 30 GB sound library in SESSIONS HORNS PRO is ten times larger than the one in SESSION HORNS. 34 articulations, up to four round robins, up to four velocity layers, and true vibrato samples » ; « three saxophones, two trombones, three trumpets, tuba, and flugelhorn » ; « Smart Voice Split automatically allocates each note of a chord to the corresponding brass instrument … Press two keys, and the instruments split into lower and higher ranges – trumpets at the top and sax and trombone at the bottom. Play three keys, and the trombone is automatically mapped to the lowest note » ; « Legato Mode mimics real world performance technique » ; Animator « over 200 ready-to-play, expertly-arranged riffs … trigger up to six phrases at a time via keyswitch » ; « requires Kontakt 6 or later (full version) or the free Kontakt Player ». Articulations citées par une revue [HEUR, Sound on Sound] : « straight sustained, staccatissimo and marcato multisamples with grace notes, jazzy rips, shakes, 'doits', falls and … 'fp crescendos' ». La liste des 34 et les notes de keyswitch n'ont pas été lues.
- Inclusion : « Session Horns Pro is included in Komplete 15 » (édition non précisée dans l'extrait) ; Komplete 15 Select : trois éditions Beats/Band/Electronic « each … 13 products » ; Beats inclut Massive X, Battery 4, Transient Master ; Band inclut Studio Drummer — **aucun extrait ne place Session Horns (ni Pro) dans une édition Select**. Page de référence : `https://support.native-instruments.com/hc/en-us/articles/27921019942045-Which-products-are-included-in-Komplete-15` (bloquée).

### 3.2 Kontakt Factory Library 2 — cuivres
- (`https://docs.native-instruments.com/ni-tech-manuals/kontakt-factory-library-manual/en/orchestral-collection`) : « The Orchestral collection comprises string, woodwind, brass and percussion sections from Orchestral Tools' flagship Berlin Series … recorded … on the Teldex Scoring Stage in Berlin » ; « Instruments in the Orchestral collection feature different sets of parameters that enable you to explore sound variations and create a variety of articulations » ; « 43 GB & 900 Instruments » [HEUR, revendeur]. La liste exacte des patches de cuivres (trompettes, cors, trombones, tuba ; ensembles/solo ; keyswitches) **n'a pas pu être lue**. Un extrait « A brass ensemble comprises four eight-player sections: Trumpets, Horns, Trombones and Tubas » est apparu dans les résultats, mais son origine (KFL2 ou Symphony Series) est incertaine.

### 3.3 Symphony Series Brass
- (`https://www.native-instruments.com/en/products/komplete/cinematic/symphony-series-brass/feature-details/`) : Brass Ensemble « 46 GB of sample content (27 GB after lossless ncw compression), 25,752 samples, and 183 total articulations » ; Brass Solo « 31 GB … (17 GB …), 19,420 samples, and 120 total articulations » ; groupes : « Sustains with real-time dynamic layer control and simulated legato, True legato sustains for each section, Staccatos with single, double, and triple-tongue options with round robins … up to 8 round-robin variations and pp/ff dynamic layering, Expressions … Effects including aleatoric, stingers, clusters, sweeps, falls, stabs, valves, and breaths » ; versions « Symphony Essentials » plus compactes.

### 3.4 Gratuit / Komplete Start
- (`https://www.native-instruments.com/products/komplete-start` et `https://blog.native-instruments.com/komplete-start/`) : « Komplete Start includes Kontakt 8 Player with Kontakt Factory Selection 2 » ; « Komplete Start is completely free ». **Aucun cuivre dédié n'est documenté dans Komplete Start** ; Session Horns n'y figure pas d'après les résultats (absence, pas preuve). Kontakt Player gratuit lit Session Horns Pro s'il est acheté ou inclus dans un Komplete possédé.

### 3.5 Synth brass : Massive X, FM8, Straylight
- Massive X : inclus dans Komplete 15 Standard et dans Select Beats [DOC-EXTRAIT] ; FM8 « listed in official product documentation » de Komplete 15 [DOC-EXTRAIT faible] ; Straylight : rien de lu → [MÉMOIRE, non vérifié] (Straylight est une bibliothèque Kontakt granulaire orientée textures, pas cuivres). Aucune page produit ne documente de preset « brass » ; à chercher par tag NKS.

### 3.6 Komplete Kontrol / NKS — tag « Brass »
- (`https://docs.native-instruments.com/ni-tech-manuals/komplete-kontrol-manual/en/browser-and-presets`) : « Filters enable you to search for sounds using NKS tags and Library tiles, and the search engine considers the preset name, author, Brand / Character / Sound Type tags, product and bank name » ; sur clavier : « turn Knob 5–7 to select Sound Type, Subtype and Character tags » ; « The "Modes" tag section is now called "Characters" » (article support NKS FX). Que « Brass » soit un **Sound Type** NKS avec sous-types (Trumpet, Horn, Trombone…) : [MÉMOIRE, non vérifié] — à confirmer dans le navigateur (KK 3.5) [TEST]. Rappel local : KK 3.5 et Maschine 3.6 n'ont aucune API, contrôle d'écran seulement [DOC-LOCAL `native-instruments-control/SKILL.md`].

---

## 4. Traitement des cuivres avec les plug-ins installés

### 4.1 oeksound soothe3 (manuel `https://oeksound.com/manuals/soothe3/`, bloqué)
- [DOC-EXTRAIT] « soothe3 is a dynamic resonance suppressor that adaptively detects resonant peaks in the incoming signal and reduces them with a dynamic filter that updates in real time » ; « can be used on individual channels to tame harshness and boominess in instruments and vocals, and … on buses ».
- [DOC-EXTRAIT/HEUR, annonce et revues] : « The new Detail parameter consolidates Soothe2's separate sharpness and selectivity controls into a single control » ; « You can now scale Detail, Attack, and Release frequency-dependently using the tilt system » ; « Soft mode offers adaptive threshold resonance suppression designed for transparency across dynamic sources, particularly acoustic and orchestral instruments. Hard mode follows the Soothe2 approach with a fixed threshold » ; « eight different band shapes – including bandpass and tilt » ; « Low latency mode adds zero samples of latency at base sample rates » ; « Enable the sidechain by clicking on the SC button ».
- Contexte local [DOC-LOCAL `effets-plugins/references/fiches.md`] : soothe3 1.0.5, rien d'exposé à l'API Live, fenêtre pilotable (double-clic + saisie) ; réglage doux relevé : « depth 4, nœud 357 Hz q 1,5 ».
- **Cuivres** [HEUR] : mode Soft, nœud 2–5 kHz (dureté de trompette), depth faible, Detail moyen, attack rapide/release moyenne ; comparer à niveau égal (delta).

### 4.2 FabFilter Pro-Q 4 (aide `https://www.fabfilter.com/help/pro-q/using/spectral-dynamics`, bloquée)
- [DOC-EXTRAIT] « In Spectral mode, Pro-Q 4 doesn't change the gain of the whole band, but triggers on specific frequencies within that band when it exceeds the threshold, leaving other frequencies untouched » ; « great for treating harshness and problem frequencies » ; « You can enable Spectral dynamics by adding a shelving- or bell curve, choosing a dynamic range, and then clicking the Spectral icon » ; collision : « The spectral display of the other instances of Pro-Q4 will have a red glow in the areas of conflicts » ; « Character mode button chooses between Clean, or the new Subtle or Warm ».
- [HEUR] Notes tierces lues sur GitHub (`https://raw.githubusercontent.com/Blankenship-Daniel/ship-studios/HEAD/docs/vst/fabfilter-pro-q-4.md`) : « 24 bands, 10 shapes », « dynamic-range ring (−30…+30 dB; negative compresses, positive expands) », attack/release manuels et « free side-chain filtering per band » nouveaux en 4, « Spectral Density = selectivity ».
- Local : rien d'exposé à l'API ; clic droit → Make Dynamic / Make Spectral [DOC-LOCAL].
- **Cuivres** [HEUR] : bell dynamique −3 à −6 dB de range vers 2,5–4 kHz en Spectral, threshold auto ; HP 80–120 Hz ; collision contre la voix.

### 4.3 Waves API-2500 (manuel : `https://assets.wavescdn.com/pdf/plugins/api-2500.pdf` et miroirs, tous bloqués)
- [DOC-EXTRAIT, texte du manuel] : Knee « In the Hard position, gain reduction begins immediately at the set ratio. In the Med position, there is a slight fade-in … Soft … even more gradual » ; Thrust « inserts a High Pass Filter at the RMS detector input, limiting compression response to lower frequencies while applying additional compression to higher frequencies. In Norm mode, there is no filter » ; Type « New (Feed Forward) … Old (Feed Back) mode, the RMS detector receives a signal from the VCA output ».
- Local [DOC-LOCAL] : paramètres exposés à Live : Thresh, Ratio ('1.5:1'…'10:1'), Attack ('0.03 ms'…'30 ms'), Release ('Var s' + Release Variable), Knee, Thrust (Norm/Med/Loud), Type (Old/New), Analog, Mix, Makeup, Output.
- **Cuivres** [HEUR] : bus de section, Ratio 3:1, Attack 10 ms (garde l'attaque), Release 0,1–0,3 s, Knee Med, Thrust Med (le grave ne pompe pas), Type Old pour le liant.

### 4.4 Waves REQ 6 (manuel `https://assets.wavescdn.com/pdf/plugins/renaissance-equalizer.pdf`, bloqué)
- [DOC-EXTRAIT] « a 6-band audiophile equalizer … choice of 6, 4, or 2-band operation » ; « Bands 1 and 6 have cut filters, resonant shelves, and bell filters (1 is low cut and shelf, 6 is high cut and shelf). Bands 2, 3, 4, and 5 all have resonant shelves and bell filters » ; « Shelf Q controls the slope of the "side" of the shelf and the resonant dips and peaks. Michael Gerzon proposed the idea of a resonant shelf … in 1994 ».
- Local [DOC-LOCAL] : `BandN Type` ('Hi-Pass','Bell','Hi-Shelf','Hi-RShelv','Low-Pass'), Frq, Gain, Q 0,26–6,5, tout exposé à l'API.
- **Cuivres** [HEUR] : Band 1 Hi-Pass 90 Hz ; bell −2 dB Q 1,5 à 500 Hz si boueux ; Hi-RShelv +1,5 dB à 8 kHz pour l'air.

### 4.5 Waves J37 Tape (manuel `https://assets.wavescdn.com/pdf/plugins/j37-tape.pdf`, bloqué)
- [DOC-EXTRAIT] « choose between the EMI 888, 811, and 815 formulas, where the 815 offers the best quality, and the 888 is the lowest » ; « EMI TAPE 888 (early '60s), EMI TAPE 811 (mid to late '60s) and EMI TAPE 815 (early '70s) » ; « BIAS … Nominal, +3 dB Over Bias, +5 dB Over Bias » ; « WOW DEPTH … default setting being the average wow measured on the original J37 ».
- Local [DOC-LOCAL] : Formula, Speed, Bias, Saturation, Wow/Flutter, Noise, In/Out Level, Delay exposés.
- **Cuivres** [HEUR] : 815, 15 ips, Saturation modérée, Bias nominal, Wow/Flutter à 0 sur une section (sinon détune audible sur les tenues).

### 4.6 Waves F6 (manuel `https://assets.wavescdn.com/pdf/plugins/f6.pdf`, bloqué)
- [DOC-EXTRAIT] « six floating, fully-adjustable parametric filters with dynamics, as well as HP and LP filters, providing multiband compression, equalization, expansion, and de-essing » ; « the frequency, width, sidechain mode, and EQ type of each band can be set independently » ; RTA intégré. Rien d'exposé à l'API [DOC-LOCAL]. Usage cuivres : équivalent « dynamique classique » de Pro-Q 4 ; à réserver au cas où Pro-Q 4 n'est pas déjà sur la piste [HEUR].

### 4.7 Waves MetaFlanger (page `https://www.waves.com/plugins/metaflanger`, manuel `https://assets.wavescdn.com/pdf/plugins/metaflanger.pdf`, bloqués)
- [DOC-EXTRAIT] « MetaFlanger can mimic both the tape-based and bucket-brigade flangers of the past, but it can also produce phasing, chorusing and even some kinds of reverb » ; revue SOS [HEUR] : « a single stereo delay line, with delay variable from 0.1 to 50 ms … modulated by a single LFO at anywhere between 0 and 20 Hz ».
- Local [DOC-LOCAL] : Mix, Depth, Rate, FeedBack, WaveForm, Filter exposés ; automation `disp`.
- **Cuivres** [HEUR] : en mode chorus (delay 10–20 ms, rate 0,3 Hz, depth faible, feedback 0) pour épaissir une section ; jamais sur un solo.

### 4.8 Plugin Alliance bx_glue (manuel `https://files.plugin-alliance.com/products/bx_glue/bx_glue_manual.pdf`, bloqué)
- [DOC-EXTRAIT, page produit] « a versatile dual-band VCA bus compressor » ; « XL saturation from subtle to intense and a selection of Classic or Dirty THD mode » ; « Stereo Width with Mono Maker function » ; « Advanced sidechain with the ability to blend external and internal key sources » ; « Inspired by classic British VCA bus compressors ».
- Local [DOC-LOCAL] : Threshold, Ratio ('2:1','4:1','10:1'), Attack (crans 0,1–30), Auto Release, Output Gain, Sidechain HPF, Mono Maker Frequency, Mix, XL Saturation exposés.
- **Cuivres** [HEUR] : bus section 4:1, Attack 10–30, Auto Release, SC HPF 100 Hz, Mix 60 % (parallèle), XL bas.

### 4.9 iZotope Ozone Imager 2
- [DOC] Aide officielle du module Imager d'Ozone 9 (`https://s3.amazonaws.com/izotopedownloads/docs/ozone9/en/imager/index.html`, lue) : Width « Adjusts the amount of gain applied to side channel content. Positive values will increase perceived stereo width » ; Stereoize I « Haas Effect-based decorrelation processing », II « newly developed alternative to the classic stereoize mode » ; « The Stereoize effect is completely mono compatible. Even if you add width to audio, it can still be played back in mono » ; corrélation « indicates the degree of similarity (or correlation) between the left and right channels ».
- [DOC-EXTRAIT] Page Ozone Imager (`https://www.izotope.com/products/ozone-imager`) : plug-in gratuit, « Stereoize II mode for subtle enhancement, or Stereoize I for a colorful phasing effect », vectorscope + correlation meter.
- Local [DOC-LOCAL] : Width et Stereoize exposés (Width global seulement).
- **Cuivres** [HEUR] : Stereoize II léger sur un stab mono échantillonné ; Width < 120 % ; vérifier corrélation > 0.

### 4.10 Battery 4 — stabs de cuivres one-shot (manuel `https://docs.native-instruments.com/pdf-guides/BATTERY_4_Manual_15_12_2021.pdf`, bloqué)
- [DOC-EXTRAIT] « The Cell Matrix is BATTERY's central interface for viewing and editing the content of a Kit » ; « The Editor page contains audio editing tools, a loop editor, and a layer and mapping editor … down to the level of editing individual sample layers within a cell » ; support NI : « Battery 4 is set by default to Expand Over Multiple Cells when multiple samples are loaded. To change the behaviour so Battery loads multiple samples into a single Cell, select the option Merge in One Cell » ; « The AHDSR envelope is for sustained samples, while the AHD envelope is more for "one-shot" sample playback » ; « If a cell contains multiple samples, they can either be layered and played at once, or assigned to different velocity layers » ; « Voice Groups simulate real-world drum behavior by grouping cells with limited voices ».
- **Application** [HEUR] : 3 stabs (court, moyen, fall) dans 3 cellules d'une même Voice Group (choke), ou 3 couches de vélocité d'un stab dans une cellule (Merge in One Cell), enveloppe AHD, Reverse pour un stab inversé de transition. Battery 4 en VST3 se charge dans Live par le navigateur du bridge, `len(d.parameters)` à vérifier [DOC-LOCAL].

### 4.11 Maschine 3.6 — sampling
- [DOC-EXTRAIT, manuel Maschine, page « Sampling and sample mapping »] : trois modes d'enregistrement « Detect, Sync and Loop » ; « When Sync is selected, the recording starts in sync with the sequencer … The LENGTH control … 1, 2, 4, 8, or 16 bars, or … Free » ; « the recording is mapped to a new Zone covering the entire key and velocity ranges in the Zone page, which makes your new sample directly playable from the pad » ; slicing manuel : « press the SAMPLING button … select SLICE … turn Knob 1 to select Manual mode … press Pad 2 to add the second slice point ».
- **Application** [HEUR] : resampler une phrase de cuivres jouée dans Live (ou Session Horns Pro), la découper en slices sur les pads, puis remonter des stabs ; le contrôle d'écran est la seule voie (aucune API) [DOC-LOCAL].

---

## 5. Synthèse « cuivres » — chaînes de départ (tout [HEUR] sauf mention)

1. **Trompette solo émulée (Serum 2)** : OSC A Multisample (trompette perso SFZ 3 couches) ou Spectral (note tenue) + OSC B sinus en FM Linear faible piloté par vélocité ; Filter 1 MG Low 12, key-track 50 %, FAT bas ; Env 2 → Pitch scoop −2 st / 60 ms ; LFO 1 sinus 5,5 Hz → Pitch, Delay 0,4 s, Rise 0,5 s, profondeur sur CC1 ; Noise pink en Filter 2 passe-bande 2 kHz, niveau sur aftertouch ; MONO + LEGATO, Porta 40 ms, Always off, Scaled on ; FX : Compressor 3:1, Reverb Hall sur BUS 1. Validation : protocole local (registre, vélocités, tenue, legato, mono).
2. **Section synth brass (Analog ou Drift)** : Analog 2 scies détunées + PW LFO, LP 4e ordre, Env filtre A 60 ms avec Env < Vel, Vibrato Delay/Attack/Amt < MW, Unison 2 ; ou Drift Saw + Shark Tooth, Mono Thickness, Legato. Chaîne : Saturator Soft Sine + Color, Chorus-Ensemble Ensemble 1,2 Hz faible, Glue 4:1 sur le bus.
3. **Cuivres FM (Operator)** : B→A sinus 1:1, index par enveloppe + Lev < Vel, Feedback 10–20 %, Pitch Env Initial −2 st, LFO avec enveloppe (vibrato retardé), Voices 1 pour solo.
4. **Cuivres réels** : Orchestral Brass / Brass Quartet (Live Suite, macro Technique) ; Session Horns Pro dans Kontakt Player si possédé (Smart Voice Split pour les voicings d'accords) ; articulations et dynamique **dans le MIDI** (keyswitches, CC1/CC11), pas dans le son [DOC-LOCAL `macro-bridge-schema.md`].
5. **Mix** : Pro-Q 4 (HP + bell dynamique/spectral 2,5–4 kHz) → soothe3 Soft si encore dur → API-2500 ou bx_glue sur le bus → J37 815 léger → Imager Stereoize II sur stabs mono → contrôle Insight 2 / SPAN [DOC-LOCAL pour l'exposition API de chaque plug-in].

---

## 6. Pages consultées

### 6.1 Lues intégralement (texte primaire) — [DOC]
1. `https://raw.githubusercontent.com/djaboxx/iron-static/HEAD/docs/api/ableton/30-live-instrument-reference.md` — copie du ch. 30 du manuel Live 12 (Analog, Collision, Drift, Drum Sampler, Electric, External Instrument, Impulse, Meld, Operator, Sampler, Simpler, Tension, Wavetable).
2. `https://raw.githubusercontent.com/djaboxx/iron-static/HEAD/docs/api/ableton/28-live-audio-effect-reference.md` — ch. 28 (Auto Filter, Chorus-Ensemble, Corpus, Glue Compressor, Multiband Dynamics, Saturator, Spectral Resonator, Vocoder lus).
3. `https://raw.githubusercontent.com/djaboxx/iron-static/HEAD/docs/api/ableton/24-instrument-drum-and-effect-racks.md` — ch. 24 (Zones, Chain Select).
4. `https://github.com/djaboxx/iron-static/tree/HEAD/docs/api/ableton` — listing (45 fichiers = chapitres 01-42 du manuel).
5. `https://s3.amazonaws.com/decembercymatics/Serum_Manual.pdf` — manuel Serum 1.0.1 (octobre 2014), texte extrait localement (`scratchpad/research/serum1_manual_text.txt`).
6. `https://gist.github.com/0xdevalias/a537a59d1389d5aed3bc63b544c70c8d` — copie du changelog officiel Xfer Serum (2.0.17 → 2.0.22).
7. `https://s3.amazonaws.com/izotopedownloads/docs/ozone9/en/imager/index.html` — aide officielle iZotope, module Imager d'Ozone 9.
8. `https://raw.githubusercontent.com/sfzformat/sfzformat.github.io/source/docs/index.md`, `.../docs/tutorials/basics.md`, `.../sustained_note_basics.md`, `.../legato.md`, `.../vibrato.md` — source du site officiel sfzformat.com ; listing `https://github.com/sfzformat/sfzformat.github.io/tree/source/docs/tutorials` et racine du dépôt.

### 6.2 Lues, sources tierces — [HEUR]
9. `https://raw.githubusercontent.com/srobinson/mdx/HEAD/research/synth-daw-ui-drag-mod-racks-graphs-vendor-docs-2026.md` (Serum 2, cite le web-manual).
10. `https://raw.githubusercontent.com/wgpatrick/dotbeat/HEAD/docs/research/49-ableton-instrument-reference.md` (résumé du ch. 30, pages 665-784).
11. `https://raw.githubusercontent.com/colfitt/arlo-genesis/HEAD/arlo/corpus/daw/ableton/devices/wavetable-drift-meld-synths.md`.
12. `https://raw.githubusercontent.com/Blankenship-Daniel/ship-studios/HEAD/docs/vst/fabfilter-pro-q-4.md`.
13. `https://github.com/bashexplode/sf2-to-sfz` (README, chemin `Multisamples\User`).
14. `https://github.com/lostsync/mooloop/issues/18` (rien sur Serum 2).

### 6.3 Fichiers locaux du dépôt lus (dépouillements antérieurs) — [DOC-LOCAL]
`.claude/skills/sound-designer-serum/references/serum2-fx-clip-arp.md`, `moteurs-synthese.md`, `modulation-effets.md`, `ressources.md` ; `vst-sound-design/references/serum2.md`, `instruments-natifs.md` ; `effets-plugins/references/fiches.md` ; `ableton-live-session/references/plugins.md` ; `native-instruments-control/SKILL.md` ; `studio-grade-brass-sound-design/references/validation-protocol.md`, `output-schema.md`, `macro-bridge-schema.md` ; `sound-designer-serum/references/basses.md` (en-tête).

### 6.4 Bloquées par le proxy (EGRESS_BLOCKED) — contenu connu seulement par extraits
- Xfer : `https://xferrecords.com/web-manual/serum-2/welcome`, `https://www.xferrecords.com/manual/serum-2/docs`, `https://static.xferrecords.com/Serum%202%20What's%20New.pdf`, `https://support.xferrecords.com/article/59-converting-samples-to-wavetables`, `https://images.equipboard.com/uploads/item/manual/127411/xfer-records-serum-2-advanced-wavetable-synthesizer-manual.pdf` (miroir du What's New).
- Ableton : `https://www.ableton.com/en/manual/live-instrument-reference/`, `https://www.ableton.com/en/packs/orchestral-brass/`, `https://help.ableton.com/hc/en-us/articles/360000318184-Orchestral-Brass`, `https://cdn-resources.ableton.com/resources/packs/pallas/pallas_manual.pdf`, `https://d3a0bdvj9eysmp.cloudfront.net/ableton/Brass_Quartet_by_Spitfire_Audio.pdf`, `https://docs.cycling74.com/reference/abl.dsp.meldosc~`.
- NI : `https://www.native-instruments.com/en/products/komplete/cinematic/session-horns-pro/`, `https://docs.native-instruments.com/ni-tech-manuals/kontakt-factory-library-manual/en/orchestral-collection`, `https://support.native-instruments.com/support/solutions/articles/69000879171-which-products-are-included-in-komplete-15-`, `https://www.cdn.native-instruments.com/...` (DNS ENOTFOUND), `http://crosstalk.arizona.edu/Data/Battery%204%20Manual%20English.pdf`, `https://www.manualslib.com/manual/2499395/Native-Instruments-Battery-4.html`.
- oeksound : `https://oeksound.com/manuals/soothe3/`. FabFilter : `https://www.fabfilter.com/help/pro-q/using/spectral-dynamics`.
- Waves : `https://assets.wavescdn.com/pdf/plugins/renaissance-equalizer.pdf`, `https://www.waves.com/plugins/metaflanger`, `https://archive.org/stream/API_2500_owners_manual/...`, `https://manuals.plus/waves/api-2500-manual`, `https://manuals.plus/waves/j37-tape-saturation-plugin-manual`, `https://device.report/manual/531985`, `https://www.promusic.cz/sites/default/files/product/field_files/f6.pdf`, `https://cdn-docs.av-iq.com/other/F6%20Floating-Band%20Dynamic%20EQ_User%20Guide.pdf`, `https://www.synthmanuals.com/manuals/waves_audio/f6_floating-band_dynamic_eq/user_guide/f6.pdf`, `https://www.bhphotovideo.com/lit_files/90360.pdf`.
- Plugin Alliance : `https://www.plugin-alliance.com/en/products/bx_glue.html`, `https://files.plugin-alliance.com/products/bx_glue/bx_glue_manual.pdf`. iZotope : `https://www.izotope.com/en/products/ozone-imager.html`.
- Tiers : `https://www.soundonsound.com/reviews/ni-session-horns-pro`, `https://blog.dubspot.com/xfer-records-releases-serum-2`, `https://en.wikipedia.org/wiki/Ableton_Live`, `https://monosounds.studio/serum-2-unison-explained/`, `https://www.edmprod.com/serum-2-filters/`, `https://www.divinesamples.com/help/user/export/sfz-serum`, `https://www.impactsoundworks.com/manuals/Shou%20Drum%20-%20Serum%202-SFZ-WAV%20Manual.pdf`, `https://www.kvraudio.com/product/serum-2-by-xfer-records`, `https://www.production-expert.com/...` (soothe3, Pro-Q 4), `https://www.tapeop.com/reviews/gear/166/fabfilter-pro-q-4-plug-in`, `https://mixinggpt.com/...`, `https://waveinformer.com/...`, `https://www.formationmaoetdj.com/...`.
- 404 : `https://github.com/sfztools/sfz`, `https://raw.githubusercontent.com/sfzformat/sfzformat.github.io/master/README.md` (branche = `source`).

### 6.5 Requêtes de recherche (extraits officiels exploités)
Une trentaine de requêtes ; les URL citées en [DOC-EXTRAIT] proviennent des résultats : `xferrecords.com/products/serum-2`, `xferrecords.com/web-manual/serum-2/{exploring-serum,using-the-serum-keyboard,using-knobs-and-sliders,enabling-pitch-tracking,getting-started}`, `ableton.com/en/packs/{orchestral-brass,brass-quartet,orchestral-ensemble-essentials,orchestral-ensemble-essentials-2,by/ableton}`, `help.ableton.com/.../Using-the-chain-selector-in-a-Rack`, `native-instruments.com/.../{session-horns,session-horns-pro,session-horns-pro/articulations,symphony-series-brass/feature-details,komplete-15-select}`, `docs.native-instruments.com/.../{kontakt-factory-library-manual/en/orchestral-collection,komplete-kontrol-manual/en/browser-and-presets,maschine-mk3-manual/en/sampling-and-sample-mapping,battery-manual}`, `support.native-instruments.com/.../How-to-Load-Multiple-Samples-into-One-Battery-Cell`, `oeksound.com/manuals/soothe3/`, `fabfilter.com/help/pro-q/using/spectral-dynamics`, `assets.wavescdn.com/pdf/plugins/{renaissance-equalizer,api-2500,j37-tape,f6,metaflanger}.pdf`, `plugin-alliance.com/products/bx_glue`, `izotope.com/products/ozone-imager`.

---

## 7. Non trouvé ou non vérifié

1. **Serum 2 — contenu d'usine Multisample** : aucune liste ; présence de cuivres inconnue. Relever dans le navigateur [TEST].
2. **Serum 2 — sous-ensemble SFZ lu** (vélocité, round robin, keyswitch, legato, crossfades CC, FLAC) : non documenté dans ce qui était accessible. Tester avec un SFZ minimal [TEST].
3. **Serum 2 — pages du web-manual** sur Multisample, Spectral, Sample, LFO, Enveloppes, Matrice, Filtres, Noise, Global : slugs inconnus, contenu non lu ; les faits reposent sur le manuel Serum 1, le dépouillement local du manuel Serum 2 et des extraits.
4. **Serum 2 — libellés exacts des modes de LFO en 2.1.5** (Trig/Env/Off vs Free/Retrig/Envelope) et **nombre exact de LFO** (10 ?) : à relever à l'écran.
5. **Ableton Orchestral Brass** : taille, liste d'articulations, tailles de sections ; **Brass Quartet** : manuel repéré mais non lu ; **Core Library « Brass »** : rien.
6. **Ableton Sampler** : aucune mention de keyswitch ni de commutateur Legato dans le ch. 30 ; l'import SFZ natif n'est pas documenté (seuls REX/ACID/Soundtrack sont cités).
7. **Wavetable et MPE** : non confirmé par le texte du ch. 30.13 lu.
8. **NI** : liste des 34 articulations et notes de keyswitch de Session Horns Pro ; patches de cuivres de Kontakt Factory Library 2 ; contenu exact de Komplete 15 Select/Standard (Session Horns, Symphony Essentials Brass, Straylight, FM8) ; Komplete Start (cuivres) ; taxonomie NKS « Brass ».
9. **Manuels Waves, bx_glue, soothe3, Pro-Q 4, Battery 4, Maschine** : aucun lu en entier ; seules les phrases citées en [DOC-EXTRAIT] sont sûres.
10. **Ozone Imager 2** (autonome) : documenté indirectement par l'aide du module Ozone 9 et un extrait de page produit ; l'aide dédiée d'Imager 2 n'a pas été trouvée.
11. **Chiffres de réglage** : tous les ms/Hz/dB des recettes sont [HEUR] ; aucun chiffre de réglage « cuivre » n'existe dans les documents constructeurs lus.

Prochaine étape recommandée : relancer les lectures marquées [DOC-EXTRAIT] depuis un environnement dont la politique réseau autorise `xferrecords.com`, `ableton.com`, `native-instruments.com`, `oeksound.com`, `fabfilter.com`, `assets.wavescdn.com`, `files.plugin-alliance.com`, `izotope.com` ; les URL exactes sont listées en 6.4-6.5.
