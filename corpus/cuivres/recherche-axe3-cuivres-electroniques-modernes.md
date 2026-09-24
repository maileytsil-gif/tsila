---
titre: "Rapport de recherche — axe 3 : cuivres électroniques modernes 2005-2026 (BRAAM, future bass, trap, big room, house, afro, synthwave ; Serum 2, Vital, Surge XT)"
source: rapport de synthèse rédigé dans cette session à partir des sources citées
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: rapport de recherche
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# AXE 3 — Cuivres électroniques modernes (2005-2026) : recherche de recettes

Rapport de recherche pour le skill « sound design des cuivres » (Ableton Live 12 + Serum 2).
Date : 2026-09-24. Rédigé en français. Conventions de tags : voir §0.2.

---

## 0. Lire ceci d'abord : méthode, limite majeure, conventions

### 0.1 Ce qui s'est réellement passé pendant la recherche

- **Toutes les pages web hors GitHub sont bloquées par le proxy sortant de la session** (`EGRESS_BLOCKED`). Ont échoué en lecture : Attack Magazine, ADSR, Production Music Live, EDMProd, Cymatics, Sound On Sound, MusicRadar, Wikipédia, YouTube, KVR, xferrecords.com, support.xferrecords.com, ableton.com, splice.com, monosounds.studio, mysticalankar.com, syntorial.com, ujam.com, glitchmagic.com, macprovideo.com, vi-control.net, professionalcomposers.com, violetrecording.com, morphic.com, blog.native-instruments.com, beatportal.com, gearspace.com, medium.com, landr.com, surge-synthesizer.github.io, web.archive.org, reddit.com. Liste complète en §C.
- **Seuls `github.com` et `raw.githubusercontent.com` sont lisibles.** J'ai donc bâti la recherche sur deux voies :
  1. **Fichiers primaires lus intégralement sur GitHub** : patchs d'usine Surge XT « Brass » (XML dans les .fxp, paramètre par paramètre), presets Vital communautaires « brass/horn » (JSON), synthdefs `braam`/`synth_brass`/`brass_section`/`trumpet`/`trombone` d'un dépôt de DSL audio, le **corpus mesuré des 626 presets d'usine Serum 2** (dépôt `pycabbage/flp-extract-fxp`), et le code source de Surge et de Vital pour convertir les unités (secondes, Hz, cents).
  2. **Extraits de recherche web** (WebSearch renvoie titre, URL et un résumé) pour les tutoriels commerciaux : ces valeurs viennent d'extraits, **pas de pages lues** ; elles sont taguées en conséquence.
- Objectif « 12 à 20 pages réellement lues » : atteint côté GitHub (≈ 45 fichiers lus, dont 25 primaires), **non atteint côté tutoriels commerciaux** (0 page lue). Le rapport est honnête là-dessus : là où seul un extrait existe, c'est écrit.

### 0.2 Conventions de tags (adaptées à cette situation)

- **[DOC]** : valeur lue dans un fichier primaire (preset/patch, code source, corpus mesuré, synthdef), avec URL du fichier brut.
- **[HEUR-lu]** : plage de départ tirée d'une note/fiche de tiers lue intégralement (dépôts GitHub de « recettes »).
- **[HEUR-extrait]** : valeur tirée d'un **extrait** de recherche (page non lue) ; à revérifier avant d'entrer dans le skill.
- **[MÉMOIRE, non vérifié]** : de ma mémoire, aucune page ne l'a confirmé.
- **[TEST]** : à valider dans le Set (mes propositions de transposition vers Serum 2 / Ableton).

### 0.3 Règles de conversion d'unités utilisées (toutes [DOC], code source lu)

- **Vital** (`mtytel/vital`, `src/common/synth_parameters.cpp`) :
  - Enveloppes `attack/decay/release/hold/delay` : échelle **kQuartic** → secondes = valeur_brute⁴ (plage 0..2,378 → 0..32 s ; défauts attack 0,1495 ≈ 0,5 ms, decay 1,0 = 1 s, release 0,5476 ≈ 90 ms).
  - `cutoff` des filtres et fréquences d'EQ : **demi-tons MIDI** 8..136 → Hz = 440·2^((n−69)/12).
  - `unison_detune` : 0..10, **kQuadratic**, affiché en % → % = brut² (défaut 4,472 → 20 %). `unison_voices` 1..16.
  - `level` d'oscillateur : kQuadratic (0,707 → 50 %).
  - `reverb_decay_time`, `chorus_frequency`, `lfo_frequency`, `portamento_time` : kExponential → 2^brut (secondes ou Hz).
  - `distortion_drive` en dB (linéaire) ; `transpose` en demi-tons ±48 ; `tune` ±1 demi-ton.
  - Source : https://raw.githubusercontent.com/mtytel/vital/main/src/common/synth_parameters.cpp
- **Surge XT** (`surge-synthesizer/surge`, `src/common/Parameter.cpp`, `ModulationSource.h`, `SurgeVoice.cpp` ; `sst-filters/FilterConfiguration.h`) :
  - Temps d'enveloppe et de LFO : type `ATwoToTheBx` → secondes (ou Hz) = 2^valeur (plage enveloppe −8..5 → 3,9 ms..32 s).
  - Cutoff (`ct_freq_audible`) : Hz = 440·2^(valeur/12) (−60 = 13,75 Hz ; 70 = 25 kHz ; défaut 3 = 523 Hz).
  - « Unison Detune » des oscillateurs Classic/Wavetable (`ct_oscspread`) : affichage = valeur × 100 **cents**.
  - `env1` = **enveloppe d'amplitude** (`adsr[0]` → `ampEGSource`), `env2` = **enveloppe de filtre** (`adsr[1]` → `filterEGSource`).
  - Sources de modulation (index XML) : 1 vélocité, 2 keytrack, 4 aftertouch, 6 molette, 7 macro 1, 8 macro 2, 16 EG filtre, 17 LFO1, 18 LFO2.
  - Types de filtre : 1 = LP 12 dB, 2 = LP 24 dB, 3 = LP Legacy Ladder. Effets : 1 Delay, 2 Reverb 1, 6 EQ, 9 Chorus.
  - Paramètres oscillateur Classic : p0 Shape, p1 Width 1, p2 Width 2, p3 Sub Mix, p4 Sync, p5 Unison Detune, p6 Unison Voices. Wavetable : p0 Morph, p1 Skew V, p2 Saturate, p3 Formant, p4 Skew H, p5 Unison Detune, p6 Unison Voices.
  - Sources : https://raw.githubusercontent.com/surge-synthesizer/surge/main/src/common/Parameter.cpp ; …/ModulationSource.h ; …/dsp/SurgeVoice.cpp ; …/dsp/oscillators/ClassicOscillator.cpp ; …/WavetableOscillator.cpp ; https://raw.githubusercontent.com/surge-synthesizer/sst-filters/main/include/sst/filters/FilterConfiguration.h
  - Unité de `filter_envmod` (« Env Mod ») : demi-tons [MÉMOIRE, non vérifié] — le nombre est lu, l'unité est de mémoire.

---

## 1. Faits et valeurs chiffrées par famille (livrable a)

### 1.1 BRAAM / cuivre cinématique (« Inception horn »)

**Origine (tous [HEUR-extrait], pages bloquées)**
- Hans Zimmer a créé le son pour satisfaire la didascalie « massive, low-end musical tones, sounding like distant horns » : des cuivres joués **dans un piano à queue, pédale enfoncée, dans une église**, puis « a bit of electronic nonsense ». — extrait de https://en.wikipedia.org/wiki/BRAAAM
- Mike Zarin (teaser du 24 août 2009) : foley enregistré dans le métro (« être dans un train ») puis mixé avec des **samples de cuivres pitch-shiftés** ; Zack Hemsey (bande-annonce du 10 mai 2010, « Mind Heist ») : braam probablement synthétisé, intégré à la musique et non comme effet. — extraits de https://epicstockmedia.com/a-brief-history-of-braaam/ et https://collider.com/inception-trailer-musical-cue/
- Définition de la fiche de scoring lue : « braam = massive detuned brass/synth impact » ; premier braam placé à 0:30-1:00 de la bande-annonce type. [HEUR-lu] https://raw.githubusercontent.com/mekedron/claude-amen-sessions/ff63fa089a89d0c2f6da635dd58db6c0af6ecf55/theory/20-genres/23-film-and-game-score.md

**Construction (extraits de tutoriels, [HEUR-extrait])**
- Ableton (blog) : partir d'un **cuivre grave de banque orchestrale**, enregistrer une **note longue, forte, grave entre C1 et C2**, **empiler plusieurs instances** de cuivres, **automatiser la distorsion** pour créer du mouvement, **descendre le pitch progressivement au pitch wheel** ; couches typiques d'un impact : kick distordu, élément percussif aigu, cymbale traitée, sub, nappe atmosphérique ; grouper et **ajouter une reverb** sur le groupe ; **compresser chaque élément, limiter l'ensemble**, utiliser tout le champ stéréo. — https://www.ableton.com/en/blog/learn-how-to-make-high-impact-sounds-for-movies-and-trailers/
- Professional Composers : ensemble de cuivres graves (tubas, trombones basses, patch « low brass »), **compression lourde et grosse distorsion « obligatoires »**, ajouter une couche de **sirène de bateau** tenue pour l'autorité, exporter en audio pour pouvoir étirer/compresser. — https://professionalcomposers.com/sound-design-how-to-make-trailer-braaam-fx/
- VI-Control (fil « Making Braams ») : cuivres avec beaucoup de « cuivré », **plusieurs niveaux pitch-shiftés superposés** (couches à l'octave), cuivre grave + synthé grave + sub, **simulateur d'ampli guitare** en distorsion, saturation, modulation de dynamique ; Serum avec **position de wavetable modulée par une enveloppe** + iZotope Trash 2 ; automation de dynamique F → FFF. — https://vi-control.net/community/threads/making-braams.121447/
- Richard Pryn : un son grave à attaque rapide (violoncelle, cor) dans une **grande reverb dont on coupe le haut du spectre, queue longue** ; presets « braam » dans Trailer Brass / Keep Forest Devastator. — https://richardpryn.com/braaams/
- Braam Designer (app) : 3 couches, du sub 15 Hz à 500 Hz. — https://apps.apple.com/us/app/braam-designer/id6757111111

**Recettes lisibles paramètre par paramètre : voir §2.1 (synthdef `braam`) et §2.2 (preset Vital « Sci-nema Brass »).**

### 1.2 Future bass « brass » / accords supersaw

- Fiche de recettes lue [HEUR-lu] (https://raw.githubusercontent.com/mekedron/claude-amen-sessions/ff63fa089a89d0c2f6da635dd58db6c0af6ecf55/theory/10-instruments/14-iconic-patch-recipes.md) :
  - **Accord future bass** : supersaw ou wavetable, **voicing haut (MIDI 60-84)**, accords 4-5 sons **maj9/m9/add9** ; **modulation de pitch de tout l'accord ±10-50 cents, LFO ou enveloppe synchro 1/8 ou 1/16** ; sidechain lourd du kick ; **compression multibande vers le haut (OTT) 30-60 %** ; stéréo large, grande reverb, **passe-haut à 250 Hz** ; souvent doublé par un vocal chop formant-shifté.
  - **Supersaw (JP-8000)** : 7 dents de scie, détune (cents) 0, ±10·d, ±22·d, ±38·d pour d∈[0..1] ; **phase de départ aléatoire obligatoire** ; niveau centre 1,0, côtés 0,4-0,8 ; pan ±30/±60/±90 % ; LP 8-14 kHz ; **HPF 200-300 Hz** ; couche carré/sinus une octave sous à 30 % ; attaque 5-20 ms (lead) / 300 ms+ (pad) ; delay 1/8 pointé, grande reverb, sidechain ; **3 notes maximum** (« un accord 5 sons = 35 dents de scie de boue »).
- Fiche de genre lue [HEUR-lu] (…/theory/20-genres/09-edm-and-future-bass.md) : future bass **140-160 BPM (ressenti 70-80)**, −8 à −6 LUFS ; le lead du drop = 3-6 sons en unisson **séparés par bande (sub / corps / air)** ; progressions IV–V–iii–vi, vi–IV–I–V ; « la supersaw à 5 notes = boue, 3 notes ».
- Fiche dubstep/production lue [HEUR-lu] (https://raw.githubusercontent.com/JefroB/Electronic-Music-Genre-Skills/19f8373eccc96b18cf1c19381289be8f82d15134/.agent/skills/genre-dubstep-bass/references/production-techniques.md) : supersaw drop = **7+ voix détunées 20-40 cents**, couches sub + saw médium + saw aigu, **sidechain 4-6 dB**, **OTT sur le bus supersaw**, automation de cutoff sur 16 mesures.
- Guide Ableton Wavetable lu (en japonais) [HEUR-lu] (https://raw.githubusercontent.com/Gaku52/dj-skills-guide/3ae34b88ce1c7af67e527b576c05861fa2a7e722/docs/production/10-bass-melody/lead-synth.md) : supersaw Wavetable = 2 osc Saw, **8 voix chacun (16 au total)** ; filtre LP Clean **3000 Hz, résonance 10-20 %** ; enveloppe de filtre **A 10 ms, D 500 ms, S 60 %, R 300 ms, amount +30 %** ; trance supersaw : **Unison 8, Detune 45 %, Stereo 80 %** ; pour Serum : **Unison 5, Detune 0,30, Blend 0,40** ; **OTT 45 % (« attention à ne pas exagérer »)**.
- Extraits [HEUR-extrait] :
  - PML « 10 supersaw tips » : monter l'unisson de l'osc 1 et baisser le Detune « vers 10 h » pour garder les voix serrées ; effet Hyper/Dimension = unisson supplémentaire. — https://www.productionmusiclive.com/blogs/news/10-supersaw-tips-for-xfer-serum-get-a-big-lush-sound-without-layering
  - Monosounds « Serum 2 Supersaw » : **detune 0,10-0,15, blend ≈ 75 %** ; « unison 7, detune 0,12, blend 75 %, width ≈ 80 » ; au-delà de 7 voix « surtout du CPU » ; Stack « Center-12 » = sub intégré. — https://monosounds.studio/serum-2-supersaw/
  - Monosounds « OSHI » : unisson non-supersaw **5-7 voix, detune 0,15-0,25** ; **OTT 20-30 % sur le bus d'accords, jamais 100 %** ; LFO lent sur position de wavetable / cutoff 5-10 % ; 140-160 BPM, snare sur le 3. — https://monosounds.studio/oshis-samples-xfer-serum-presets-production-tricks-future-bass-magic-tutorial/
  - Unison.audio : supersaw « Flume » **8+ voix, détune 10-20 cents** ; « monter l'unisson à 7 » ; accords 7e/9e/sus ; LFO 1 → cutoff pour le « swell » ; OTT pour le son « écrasé ». — https://unison.audio/how-to-make-future-bass/
  - Dylan Bowes (Medium) : pour un rythme de LFO 1/16 **swingué**, **régler le LFO à 1/8** et dessiner le swing dans la forme ; LFO sur niveau d'oscillateur / volume ou cutoff. **BPM non indiqué dans l'extrait.** — https://medium.com/@OSCILLATR/sound-design-future-bass-chords-with-a-swung-lfo-using-serum-32067dd2f8e8
  - PML « Future bass synth in Serum » : LFO 1 → cutoff du LP pour les accords ; osc B moins détuné que osc A. — https://www.productionmusiclive.com/blogs/news/how-to-make-a-future-bass-synth-in-serum-beginners

### 1.3 Trap / drill brass

- **Correction factuelle** : le hook de « Mask Off » (Future, prod. Metro Boomin, 2017) est une **flûte**, sample de « Prison Song » (Tommy Butler, comédie musicale *Selma*, crédité aussi Carlton Williams, 1976/1978) — pas un cuivre. [HEUR-extrait] https://www.vice.com/en/article/a-brief-history-of-that-kickass-flute-sample-on-futures-mask-off/ ; https://www.whosampled.com/sample/484014/Future-Mask-Off-Carlton-Williams-Prison-Song/ ; https://en.wikipedia.org/wiki/Mask_Off
- Principe trap brass (Glitch Magic, Ableton 11) [HEUR-extrait] : onde complexe type **dent de scie**, **enveloppe qui éclaircit l'attaque**, **détune et modulation de pitch**, puis EQ, distorsion, compression multibande « pour paraître moins synthétique ». — https://glitchmagic.com/blogs/news/how-to-make-trap-style-brass-sounds-ableton-11-sound-design-tutorial
- Mix des stabs trap/EDM (UJAM) [HEUR-extrait] : **transitoire net sur toute la bande** sinon le stab ne passe pas ; **compression attaque courte / release rapide → la queue « flare »**. — https://www.ujam.com/tutorials/the-ultimate-guide-to-edm-trap-swells-and-brass-stabs/
- Mystic Alankar « brass pluck » (Serum) [HEUR-extrait] : osc A wavetable **Hypa** (Digital), osc B **Analog BD Sine** ; ouvrir le cutoff ; **enveloppe en mode Env, courbe descendante, mappée sur Warp des osc A/B et sur le niveau de l'osc A** ; **booster les 3e et 5e harmoniques** pour le nasal cuivré. — https://mysticalankar.com/blogs/blog/how-to-create-a-brass-pluck-sound-in-xfer-serum
- Notes GMS (FL Studio, lu) [HEUR-lu] : « Trap : dent de scie, **4-6 voix**, stéréo modérée, distorsion légère » ; recette « Brass Lead » complète en §2.4. — https://raw.githubusercontent.com/JaZeR-444/fl-studio-master-hub/56bfdb7386552533f78e057a1183bf712b4bb5f5/src/data/plugins/gms/workflow/by-instrument/lead-creation.md
- Fiche trap lue [HEUR-lu] : stab « String/Synth » **sombre 200 Hz-2 kHz**, bibliothèque orchestrale (articulation courte) ou dent de scie à decay rapide, reverb courte, LP. — https://raw.githubusercontent.com/JefroB/Electronic-Music-Genre-Skills/19f8373eccc96b18cf1c19381289be8f82d15134/.agent/skills/genre-hiphop-trap/references/sound-design.md
- Fiche drill lue [HEUR-lu] : 138-145 BPM (UK/NY 140-144) ; palette **cordes pizzicato, piano sombre, cloches, orchestral hits** ; reverb longue et sombre sur le mélodique, aucune sur les drums ; « mix froid : couper 200-400 Hz » ; **aucune mention de cuivres** dans cette fiche. — …/theory/20-genres/11-drill.md
- Fiche trap lue [HEUR-lu] : « **passe-haut pour isoler un horn stab** dans un sample », pitch/time-stretch au tempo. — …/theory/20-genres/10-hiphop-and-trap.md
- Sources sonores (extraits, [HEUR-extrait]) : expansions Nexus « Purple Juice » (22 presets TM88/808 Mafia) et banques Omnisphere StudioTrap (300 patches) contiennent des « brass » ; Splice « UK Drill Melody Stacks » (Komorebi Audio, 227 samples, éléments orchestraux/brass). — https://producergrind.com/blogs/blog/purple-juice-free-nexus-expansion-22-trap-preset-sounds ; https://www.adsrsounds.com/product/presets/studio-trap-omnisphere-bundle-presets/ ; https://splice.com/sounds/packs/komorebi-audio/uk-drill-melody-stacks/samples
- Tutoriels vidéo repérés (titres seulement, non lus) : « How to make a Trap Brass sound - Serum Tutorial [Sancus] » https://www.youtube.com/watch?v=pKCev_9pCfU ; « Main Brass Lead in Like That by Metro Boomin [FL Studio | Serum] » https://www.youtube.com/watch?v=XN2nKoNql1Y ; « Huge Brass / Horn Trap Lead » https://www.youtube.com/watch?v=u06TOaP4UJc ; « Huge Organic Brass Stab Synth (Trap / Future Bass) » https://www.youtube.com/watch?v=GoSmzVFZtEI
- **Recettes lisibles** : presets Vital « Mid Horn » et « Trappy Wub Reverb Horn » (§2.2), « Musinous – Brass Stabs » (§2.2).

### 1.4 Big room / festival brass lead, brass stab EDM, screech hardstyle/rawstyle

- Fiche genre lue [HEUR-lu] : big room **126-132 BPM, mineur, −6 à −5 LUFS** ; le drop = kick + basse + **un seul lead**, souvent une ou deux notes ; hardstyle **148-155**, rawstyle **150-160** ; **screech = « detuned, distorted saw stabs »** ; design du screech : **saws détunées → distorsion → passe-bande résonant → resample → re-pitch → répéter**. — …/20-genres/09-edm-and-future-bass.md ; …/20-genres/08-hardstyle-and-hardcore.md
- GMS (lu) [HEUR-lu] : « Big Room Lead : supersaw 8 voix, flanger + reverb, filtre brillant » ; supersaw classique : 3 saws (0, +7, −7 cents), unisono 6-8 voix, stéréo 75 %, detune 55 %, LP cutoff 85 % res 20 %, amp A 0 % D 25 % S 95 % R 35 %.
- Myloops (lead trance/big room, Serum) [HEUR-extrait] : **osc A saw, unisson 7, detune 0,25-0,30, blend ≈ 0,8 ; osc B saw, unisson 3, detune ≈ 0,15, −1 octave, ≈ −6 dB sous A** (« l'octave basse ancre le pitch quand le haut s'élargit »). — https://www.myloops.net/designing-a-modern-uplifting-trance-supersaw-lead
- Screech House (hardstyle lead, Serum) [HEUR-extrait] : **2 oscillateurs, 16 voix chacun, fortement détunés, le second +1 octave**. — https://screechhouse.com/hardstyle-lead-tutorial-serum-hardstyle-lead-make-hardstyle-lead-fl-studio/
- ADSR (hardstyle screech, Serum) [HEUR-extrait] : init ; wavetable **Basic CJW (dossier Analog)** ; copier A → B, **7 voix chacun**, détune monté ; **LFO 1 → Coarse Pitch des deux osc, BPM sync off, ≈ 20 Hz** (vibrato rapide) ; **LFO 2 en mode Envelope → Master Tune** (rampe de pitch) ; enveloppe de pitch : incliner avec **DEC et AMT** ; filtre **Peak 12** résonance montée, cutoff par LFO 2 ; distorsion : monter **Drive et Fat** progressivement ; astuce : même LFO sur cutoff **et** sur WT POS. **BPM de la source non indiqué dans l'extrait** (LFO 1 non synchro, donc sans conséquence). — https://www.adsrsounds.com/serum-tutorials/hardstyle-screech-sound-design-with-serum/
- Screech House (rawstyle screech, Sylenth1) [HEUR-extrait] : **1-2 osc, 6-8 voix, détune poussé** ; enveloppe de pitch **DEC + AMT (+ un peu d'ATT)** ; **LFO de pitch rapide, attaque courte, AMT à doser** ; distorsion et chorus internes. — https://screechhouse.com/the-ultimate-rawstyle-screech-tutorial-how-to-make-a-hardstyle-screech-in-fl-studio-with-sylenth1/
- Fiches hard dance / hardcore lues [HEUR-lu] : « Stab Synth » = **pile de saws détunées, attaque/decay rapides, sans sustain, 300 Hz-6 kHz**, compression serrée, reverb courte ; « Screech Lead » = **FM 2-3 opérateurs à index élevé, hard sync ou phase distortion, 500 Hz-10 kHz**, distorsion, notches EQ, delay, autopan. — …/genre-hard-dance-happy-hardcore/references/sound-design.md ; …/genre-hardcore-bouncy/references/sound-design.md
- Brass stab EDM (The Producer School) [HEUR-extrait] : partir d'un **sample de cuivre staccato** ; **superposer le même sample une octave plus haut** ; EQ : **léger boost bas-médiums (corps) + un peu d'aigu (présence)** ; chaque couche EQ/traitée séparément ; distorsion, compression, reverb, sidechain. — https://theproducerschool.com/blogs/news/the-ultimate-way-to-make-stabs-for-edm
- Tom Budin : horn stab tech house en < 2 min sur Massive (vidéo, aucune valeur dans l'extrait). — https://www.youtube.com/watch?v=uE3BgBNPdtY

### 1.5 House / disco / French house / UK garage / tech house

- Fiche house lue [HEUR-lu] : **voicings sans fondamentale MIDI 55-75**, stabs sur les contretemps **courts, queue de reverb coupée/gatée** ; swing 52-56 % sur les hats ; palette : Rhodes, samples disco filtrés, pads Juno, **orgue stabs**, 909, **saxophone**. — …/20-genres/01-house.md
- Fiche UKG lue [HEUR-lu] : **130-140 BPM** ; m7, m9, maj7, 7sus4 ; **stabs sur contretemps, courts, filtrés** ; **reverbs courtes et slapback seulement** ; basse « orgue » = carré filtré en stabs syncopés. — …/20-genres/07-uk-garage-and-grime.md
- Fiche UKG (JefroB) lue [HEUR-lu] : « Horn / Synth Stabs » = **samples de trompette ou patch synthé brillant, 500 Hz-5 kHz, staccato, reverb courte, compression** ; « Synth Stabs » saw/carré enveloppe courte **300 Hz-3 kHz**. — …/genre-uk-garage-grime/references/sound-design.md
- Fiche house (JefroB) lue [HEUR-lu] : « Synth Stabs » saw/carré enveloppe rapide **200 Hz-2 kHz**, reverb throw, distorsion, sweep ; « Strings/Horns » = stabs orchestraux disco **samplés (Kontakt ou vinyle)** ; « Orchestral Stabs » (Triton/M1) **200 Hz-6 kHz** ; « Horns : brass stabs occasionnels pour l'énergie ». — …/genre-house/references/sound-design.md ; …/production-techniques.md
- Fiche disco lue [HEUR-lu] : section cuivres **300 Hz-6 kHz**, reverb room, légère compression, **présence 2-4 kHz** ; « Filtered Chords (Disco Stabs) » : LP de **200 Hz fermé → 8 kHz ouvert**, longues automations, sidechain, delay throws. — …/genre-disco-nudisco/references/sound-design.md
- Fiches disco/funk lues [HEUR-lu] : **horn stabs sur les contretemps et fins de phrase**, harmonie réelle 3-4 voix ; « une section de cuivres est une section de percussions avec des hauteurs » ; ne pas masteriser fort. — …/20-genres/29-disco-and-italo.md ; …/20-genres/19-funk-soul-and-rnb.md
- Korg M1 (lu) [HEUR-lu] : « Organ 2 / Universe » = le rave organ stab ; « Brass and orchestral hits » = stabs rave/jungle ; **rebuild du stab M1 : sample brillant à attaque dure, decay 400-800 ms, passe-bande sous 200 Hz, boost 1-3 kHz, stabs courts sur contretemps, plate 1-1,5 s, léger chorus**. — …/10-instruments/07-samplers-and-workstations.md ; …/14-iconic-patch-recipes.md
- Extraits [HEUR-extrait] :
  - French house (Wikipédia) : **filtre et phaser sur des samples disco fin 70s/début 80s** ; « looped and filtered samples of disco strings, rhythm guitars, **horn stabs** » ; sweeps LP, sidechain pompant, hats swinguées ; Frohmage / CamelPhat cités. — https://en.wikipedia.org/wiki/French_house
  - Gearspace (stab recognition) : « **pitched-up EQ'd brass stab with pitch envelope** » depuis de vieux disques funk/soul. — https://gearspace.com/threads/another-house-stab-recognition-thread.1103155/
  - ProducerStack : stabs = hits orchestraux samplés par Detroit/Chicago fin 80s (« Strings of Life », 1987) ; le M1 « partout » dans la rave 91-93. — https://producerstack.com/blogs/the-stack/house-music-stabs-what-they-are-and-how-to-use-them
  - UKG : 130-140 BPM (2-step 130-135) ; stabs **m7/m9 en Am, Cm, Dm**, voicing serré (punch) ou large (chaleur). — https://bpmcalc.com/genres/garage/ ; https://beatkey.app/how-to-make-uk-garage-music
  - Fisher « Losing It » : le « horn » est un synthé ; tutoriels vidéo existants (Incognet ; « The Best FISHER 'Losing It' Horn Tutorial ») — **aucune valeur dans les extraits**. — https://incognetsamples.com/tutorials/how-to-make-fisher-losing-it-oz-synth-tech-house.html ; https://www.youtube.com/watch?v=QMoQo-Irulw
  - Daft Punk : tutoriels « filtered house step-by-step » (vidéo) ; Simpler : changer le point de départ de boucle et traverser le sample. — https://www.youtube.com/watch?v=yxmsP8mDva4

### 1.6 Afro house / amapiano / afrobeats / afrobeat (Fela Kuti)

- Fela Kuti [HEUR-extrait] : section de cuivres typiquement **à trois : saxophone baryton, trompette, saxophone ténor** (sur *Roforofo Fight* : Lekan Animashaun bari, Tunde Williams trompette, Christopher Uwaifor ténor) ; « **driving horn section proclamations** » + solos de sax/trompette/orgue ; **call-and-response** vocal et instrumental ; sections finales = solos de trompette/ténor + voix. — https://progrography.com/fela-kuti/review-fela-the-africa-70-roforofo-fight-1972/ ; https://daily.redbullmusicacademy.com/2012/12/a-guide-to-the-albums-of-fela-kuti/ ; https://en.wikipedia.org/wiki/Stalemate_(Fela_Kuti_album)
- Fiche afro lue [HEUR-lu] : **afrobeat (Fela) 100-130 BPM, « long-form, horns, funk, polyrhythm »** ; highlife : guitare + cuivres ; afrobeats 100-115 ; amapiano 108-118 (log drum = sine/triangle + chute de pitch rapide, accordé) ; afro house 118-125 ; swing 56-60 % inégal ; 10-20 couches de percussions à −18/−25 dB ; **rien sur les cuivres dans les recettes** afrobeats/amapiano de cette fiche. — …/20-genres/26-afrobeats-and-amapiano.md
- Fiche dancehall/afrobeats (JefroB) lue [HEUR-lu] : « Horn Stabs » = **cuivres samplés (sections enregistrées) ou patch synth brass, 500 Hz-6 kHz, compression, reverb courte, boost de présence ; rôle = marqueur de section / énergie des hooks** ; soca : section cuivres **centrale**, 300 Hz-8 kHz, room, présence 2-4 kHz, **stabs staccato, lignes à l'unisson, call-and-response** ; « Synth Stabs » saw attaque rapide decay court 500 Hz-8 kHz « soutient ou remplace les cuivres ». — …/genre-dancehall-afrobeats/references/sound-design.md
- Fiche amapiano/afro tech (JefroB) lue [HEUR-lu] : **aucun cuivre** ; le mélodique = piano stabs Rhodes/Wurli (voicings 7e/9e/shell, staccato, chorus léger, reverb medium), pads, arp. — …/genre-african-latin-electronic/references/sound-design.md
- Afrobeat en FL (Sample Focus blog) [HEUR-extrait] : stabs = **accords courts accentués sur les contretemps** ; **harmoniser en tierces/quartes (ou tierces/sixtes parallèles)** ; FLEX ou Session Horns (trompettes, trombones, sax) ; **petite reverb/delay, slapback court sur les stabs**, éviter les effets lourds. — https://samplefocus.com/blog/make-afrobeat-fl-studio/
- Afro house (Keinemusik/Black Coffee) [HEUR-extrait] : les guides trouvés décrivent toms, shakers, cloches/verre, « éléments savane », piano — **pas de cuivres** ; Afro house **115-125 BPM**. Un template « Trumpet Love – Pablo Fierro & Black Coffee style » (Innovation Sounds) et un pack « House Horns » (Loopmasters, **125 BPM**, sax/trompette, influence balkanique/klezmer) existent. — https://www.productionmusiclive.com/blogs/news/producer-notes-keinemusik-more-love-rampa-me-afro-house-moderat-style-ableton ; https://www.beatportal.com/articles/647491-step-by-step-guide-to-creating-an-afro-house-track-keinemusik-black-coffee-caiiro-alex-wann-style ; https://innovationsounds.com/products/trumpet-love-pablo-fierro-black-coffe-style-ableton-10-afro-deep-house-template ; https://www.loopmasters.com/genres/25-House/products/9861-House-Horns
- Amapiano [HEUR-extrait] : le **saxophone** apparaît (instrumentistes live, « brass band playing amapiano ») mais aucune recette ; « Abalele » (Kabza de Small & DJ Maphorisa, 17 sept. 2021). — https://pan-african-music.com/en/instrumentalists-of-amapiano/ ; https://en.wikipedia.org/wiki/Abalele

### 1.7 Synthwave / retrowave brass

- Fiche synthwave lue [HEUR-lu] : **80-120 BPM** (synthwave 100-118, outrun 110-120) ; −10 à −8 LUFS ; mélodie **MIDI 67-84** sur lead saw + portamento + chorus + delay pointé ; **« chorus sur tout »** ; vibrato appliqué tard ; palette : Juno-106/Jupiter-8, DX7, orchestra hits ; **saxophone** = cliché assumé ; couper au-dessus de 15 kHz. — …/20-genres/16-synthwave-and-retro.md
- Fiche synthés analogiques lue [HEUR-lu] : **OB-Xa/OB-8** = « big, brassy » ; unisson 8 voix ; **le filtre 12 dB donne la qualité « section de cuivres »** ; **rebuild : 6-8 saws sur une note, détune ±15 cents, LPF 12 dB/oct avec enveloppe de filtre rapide et profonde, accords plaqués à attaque forte**. — …/10-instruments/03-analog-polysynths.md
- FM lue [HEUR-lu] : **ratios 3:1 et 4:1 = « bright, brassy »** ; « envelopper l'index, pas un filtre ». — …/10-instruments/05-fm-and-phase-distortion.md
- Fiche synthwave (JefroB) lue [HEUR-lu] : lead 2-3 saws détunées, LP résonance modérée, glide, **500 Hz-6 kHz**, chorus, plate/hall, delay pointé ; sources Prophet-5 « brass-like » ; « Synth Stabs » saw accord enveloppe **10-50 ms**, 300 Hz-3 kHz, distorsion. — …/genre-synthwave-darkwave/references/sound-design.md ; …/production-techniques.md
- Vintage Soundset [HEUR-extrait] : DX7 FM brass = « bright, glassy, slightly metallic » → piles d'opérateurs FM à harmoniques impaires fortes + chorus + plate ; **Juno brass = deux saws détunées + sub, chorus/ensemble, LP doux** ; **OB-Xa brass = large détune entre oscillateurs, légère résonance, drive léger** ; « OB-X = arme analogique de choix pour les cuivres ». — https://www.vintagesoundset.com/post/the-top-80s-synth-brass-presets-iconic-sounds-that-defined-a-decade
- Timecop1983 [HEUR-extrait] : FL Studio + plugins gratuits (Synth1, OB-Xd, TAL U-NO-62), Lush-101, Zebra2 ; hardware Micron, AN1x, Radias, D-50, Alpha Juno, Juno-106 ; lead = **carré PWM (LFO mode, PW 6, rate 5) + saw** ; « On The Run » (Synth Ctrl) : Serum 2 osc saw, **B +1 octave, 6 voix chacun légèrement détunées, env 1 A 0,5 ms D 780 ms R 650 ms**. — https://reverbmachine.com/blog/timecop1983-synth-sounds/ ; https://synthctrl.com/blogs/blog/timecop1983-on-the-run-breakdown
- The Midnight [HEUR-extrait] : le « cuivre » signature est un **saxophone réel**. — https://newretro.net/blogs/main/the-midnight-mixes-synthwave-with-pop-and-saxophone-driven-melodies
- Kavinsky « Nightcall » keys (Syntorial) [HEUR-extrait] : init saw ; **unisson + chorus** ; **sweep de filtre dramatique (attaque brillante → fin ronde)** ; bruit + distorsion pour le grain lo-fi. Pack Tonepusher « Nightcall » (Serum) : 50 presets dont **7 brass**. — https://www.syntorial.com/preset-recipe/kavinsky-nightcall-keys/ ; https://www.adsrsounds.com/product/presets/tonepusher-nightcall-serum-presets/
- **Recettes lisibles** : Surge « OB-8 Jump », « JX-10 Double Brass », « Toto Brass », « Synth Brass 1-3 », « Buggy Brass » (§2.3) ; Vital « 80s Saw Brass » (§2.2) ; synthdef `synth_brass` (§2.1).

### 1.8 Serum 2 spécifiquement

**Corpus mesuré des presets d'usine (fichier lu) [DOC]** — https://raw.githubusercontent.com/pycabbage/flp-extract-fxp/a83908a3e27b16bfc42dc63c5105b5c56e36da80/docs/s2-param-corpus.md (corpus tiers : 626/626 fichiers `.SerumPreset` d'usine décodés, versions 2.0.11-2.0.15, chemin `Documents\Xfer\Serum 2 Presets\Presets\Factory\**`).
- **626 presets d'usine** ; badges de type d'oscillateur dans les tags : **Wavetable 528, Multisample 155, Sample 72, Granular 56, Spectral 43** (un preset peut cumuler) ; voicing Poly 414 / Mono 212 ; catégories de tag : Arp 33, Clip 27, Embedded-Data 23, KB-Span 17, Custom-Tuning 2. **Il n'existe pas de tag « Brass » dans les métadonnées** ; le classement par instrument passe par les dossiers (non listés dans le corpus).
- Nommage des presets d'usine : préfixe de catégorie + tiret, ex. **« ARP - Aardvark » (auteur Audiotent)** ; des sound designers tiers signent des presets d'usine.
- **Contenu d'usine de type cuivre réellement référencé par des presets d'usine** :
  - Oscillateur **Sample** (`samplePathRelative`) : `Factory/Brass/Brass Wall Low.flac`, `Factory/Brass/Trombone Alt.flac`, `Factory/Brass/Trombone.flac`, `Factory/Synth/DX Brass2 C2.flac` → **il existe un dossier de samples d'usine « Brass »** et un sample « DX Brass2 » (cuivre FM type DX, note C2).
  - Oscillateur **Multisample** (SFZ embarqué, 245 presets) : `Factory/Winds/French Horns.sfz`, `Factory/Winds/Trombones Cimbasso LE.sfz`, `Factory/Winds/Trombones Tenor LE.sfz`, `Factory/Winds/Trumpets LE.sfz`, `Factory/Synth/Arp Solina - Horn.sfz` → **les cuivres multisamplés d'usine sont rangés sous « Winds »**, en versions « LE » (allégées).
  - Paramètres exposés par l'oscillateur Multisample : `kParamWarp`, `kParamWarp2`, `kParamTimbreShift`, `kParamEnvDecay/EnvSustain/EnvRelease`.
- Serum 2 : 3 oscillateurs principaux à moteur indépendant (WT / Multisample / Sample / Granular / Spectral) + Noise + Sub ; 2 filtres, 4 enveloppes, 10 LFO, 8 macros, 3 racks d'effets, 64 slots de modulation, arp et clip player. [DOC, même corpus]
- Site Xfer [HEUR-extrait] : « massive, exclusive, and original library of real instruments recorded around the world, including orchestra, choir, pianos, guitars » ; import SFZ. — https://xferrecords.com/products/serum-2
- Tiers [HEUR-extrait] : Monosounds « Unique Brass » (Serum 2) : tuba, trombone, trompette, cor, variantes shimmer/room/frozen-verb, noms « Brass - Small Sax », « Brass - Orchestra » — https://monosounds.studio/product/unique-brass-xfer-serum-presets/ ; Impact Soundworks presets + SFZ pour Serum 2 — https://impactsoundworks.com/products/serum-2-presets-and-sfzs/ ; « Symphony 2 SERUM » : 72 cuivres (cor, trombones stacc/sus, trompettes stacc/sus) ; NKS Library Serum 2 (Freelance Soundlabs, 1000+ presets tagués) — https://freelancesoundlabs.com/product/id:10190/downloads/xfer/nks-library-xfer-serum-2/
- Tutoriels vidéo Serum 2 repérés (titres) : « Serum 2 Tutorial | Huge Brass Bass | Melodic & Progressive House » https://www.youtube.com/watch?v=6P1mCkwgld0 ; « How to Make a DnB Brass Stab in Serum 2 » https://www.youtube.com/watch?v=anvXAGJK19Y ; « Trailer Sound Design with Serum 2: Braams » https://www.youtube.com/watch?v=MzmdS_s1GX0 ; « Making Epic Horn/Braam sounds for Psytrance/Psytech with Serum 2 » https://www.youtube.com/watch?v=wVDVB6xwwOg ; « Serum Brass / Trumpet Lead Tutorial (Serum/Serum 2) » https://www.youtube.com/shorts/Vdk4Hv9ITAk
- Forum Xfer / KVR : **rien de lisible ni d'indexé** sur « brass Serum 2 » (voir §D).

---

## 2. Recettes complètes, paramètre par paramètre (livrable b)

Note sur les BPM : parmi les recettes lues, **aucune ne repose sur un LFO synchronisé au tempo pour le timbre** (les LFO synchro rencontrés sont des vibratos libres en Hz, ou des LFO non routés). Les seules recettes « rythmiques » sont celles des extraits future bass (§1.2 : LFO 1/8 avec swing dessiné, LFO de pitch ±10-50 cents à 1/8 ou 1/16) — **BPM des sources non indiqué**, à retransposer au tempo du Set (le rapport 1/8 = deux croches par temps reste valable à tout BPM).

### 2.1 Synthdefs lisibles (DSL audio, dépôt `trusch/vibelang`) [DOC — fichiers lus]

Ce sont des définitions de synthèse en code (type SuperCollider), donc totalement explicites. Elles ne viennent pas d'un constructeur ; elles constituent une **description formelle** transposable dans n'importe quel synthé.

**`braam` — « Inception-style BRAAM »** — https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/cinematic/braam.vibe
- Fréquence par défaut **55 Hz (A1)**, amp 0,9.
- Oscillateurs : **5 dents de scie** : f×0,99 (×0,20), f (×0,25), f×1,01 (×0,20), **f×2 (×0,15)**, **f×0,5 (×0,20)** → une paire détunée ±1 % autour du centre, une octave au-dessus et une octave en dessous (sub).
- Enveloppe d'amplitude : **perc, attaque 50 ms, decay 2,0 s** (« long, powerful decay »).
- Enveloppe de filtre : **perc, attaque 50 ms, decay 1,5 s**.
- Filtre : LP résonant, **cutoff = 200 Hz + env × 3000 Hz** (donc de 3,2 kHz à 200 Hz sur 1,5 s), **résonance 0,2**.
- Ni distorsion ni reverb dans le synthdef (à ajouter en aval).

**`synth_brass` — « 80s, Synthwave | Punchy, bright, fat »** — https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/synth_brass.vibe
- Fréquence par défaut 220 Hz (A3) ; paramètre `detune` 0..1 (défaut 0,5).
- **5 dents de scie** aux ratios 1−d, 1−d/2, 1, 1+d/2, 1+d avec **d = 0,005 + detune×0,01 = 1 % au défaut** (≈ ±17 cents ext., ±8,6 cents int.), somme ×0,25.
- Enveloppe d'amplitude : **ASR attaque 30 ms, sustain 1, release 100 ms**.
- Enveloppe de filtre : **ASR attaque 10 ms, release 100 ms** ; **cutoff = 600 Hz + env × 3000 Hz** (3,6 kHz tenu), **résonance 0,4**.

**`brass_section` — « Orchestral, Jazz | Powerful, majestic »** — https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/brass_section.vibe
- 3 saws à ±0,4 % (≈ ±7 cents) ×0,35 + **saw à l'octave ×0,3** ; amp **ASR attaque 150 ms (« swell »), release 100 ms** ; filtre LP **800 Hz + env × 2500 Hz, résonance 0,3**, env de filtre attaque **75 ms** ; **vibrato sinus 4,5 Hz, profondeur 0,2 %** (≈ 3,5 cents) sur l'amplitude.

**`trumpet`** — https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/trumpet.vibe
- 2 saws (f et f×1,001 à ×0,5) ; **trois LP « formants » en parallèle : 1200 Hz (Q 0,3), 2500 Hz (Q 0,25, ×0,5), 3800 Hz (Q 0,2, ×0,3×brightness)** ; **transitoire « lip buzz » = bruit blanc, perc 1 ms / 30 ms, ×0,1** ; amp ASR **50 ms / 80 ms** ; vibrato **5,5 Hz, 0,8 %** (défini mais non appliqué au pitch dans le code).

**`trombone`** — https://raw.githubusercontent.com/trusch/vibelang/main/crates/vibelang-std/stdlib/brass/trombone.vibe
- 2 saws (f, f×0,999 ×0,6) ; formants **500 Hz (×0,6), 1200 Hz, 2000 Hz (×0,4)** ; **LP global 3000 Hz** ; amp ASR **100 ms / 150 ms** ; vibrato **4 Hz, 0,6 %**.

### 2.2 Presets Vital lus (JSON) [DOC — fichiers lus, valeurs converties selon §0.3]

Rappel : `Init` est la wavetable par défaut de Vital (dent de scie) [MÉMOIRE, non vérifié] ; « style » de filtre 0/1 = probablement 12/24 dB [MÉMOIRE, non vérifié] ; les LFO synchro utilisent un index de tempo dont la table de noms n'a pas été lue (valeurs brutes citées).

**A. « 80s Saw Brass » — dj.tuBIG/MaliceX (« The Hello World of ROMpler synths »)** — archive Discord Vital, https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/dj.tubigmalicex/80s_Saw_Brass.vital
- OSC1 : Init (saw), **16 voix, détune 7,8 %**, blend 0,8, spread 100 %, niveau 50 %, phase aléatoire.
- Filtre 1 : Analog, style 0, **cutoff 326 Hz, résonance 15 %** ; **vélocité → cutoff 0,99** (le cutoff monte de près de toute la plage avec la vélocité).
- ENV1 (amp) : **A 12 ms, D 482 ms, S 91 %, R 90 ms**.
- ENV2 → **unison detune (amount 1,0)** : **A 0 ms, D 77 ms, S 0** → le détune part au maximum et se resserre en 77 ms : c'est le « blat » d'attaque. Vélocité → decay ENV2 +0,055.
- LFO1 (≈ 1 Hz, triangle) → tune via molette (vibrato à la molette, qui accélère aussi le LFO +0,2).
- Effets : reverb mix 25 %, **decay 1,8 s**, size 0,62 ; delay mix 18 %, feedback 39 %, synchro (style 2).
- Polyphonie 32, pitch bend ±12.

**B. « NavigatorSynthBrass » — Instatetragrammaton** — https://raw.githubusercontent.com/instatetragrammaton/Patches/cb65e685e77cf0d6c26d11ff391136cf01bfd427/Matt%20Tytel%20Vital/v1.5.3/NavigatorSynthBrass.vital (commentaire : remake d'un son de vidéo YouTube)
- OSC1 : saw, **2 voix, détune 6,4 %**, niveau 50 %. OSC2 : saw **−12 st, 2 voix, détune 4,4 %, niveau 5,3 %**.
- Filtre 1 : Digital, style 1, **cutoff 72 Hz, keytrack 100 %, résonance 24 %** ; **ENV2 → cutoff amount 0,76** (≈ +97 demi-tons : le filtre s'ouvre presque à fond puis retombe).
- ENV1 (amp) : **A 19 ms, D 1 s, S 100 %, R 90 ms**. ENV2 (filtre) : **A 106 ms, D 578 ms, S 45 %, R 90 ms**.
- ENV3 (« TWANG », macro 1 → amount 0,07) → transpose : A 0, hold ≈ 0, D 3 ms — micro-scoop de pitch optionnel.
- Chorus : 1 voix, mix 33 %, fréquence 0,21 Hz, depth 0,5. Reverb : mix 15 %, **decay 1,8 s**, size 0,34, pré-delay 0,04.
- Polyphonie 8. Enseignement : **attaque de filtre ≈ 100 ms plus lente que l'attaque d'amplitude ≈ 20 ms** — c'est le geste « cuivre » classique.

**C. « Musinous – Brass Stabs » — Musinous (style SFX)** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/musinous/Musinous_-_Brass_Stabs.vital
- OSC1 : saw **−24 st, 9 voix, détune 4,8 %** ; OSC2 : saw **−24 st, 6 voix, détune 7,3 %** ; OSC3 : saw **−12 st, 10 voix, détune 13,7 %** ; niveaux 50/50/48 %. (Joué deux octaves au-dessus de la hauteur voulue.)
- Filtre 1 : Analog style 0, **cutoff 366 Hz, keytrack 100 %, drive 7,9 dB** ; **ENV2 → cutoff 0,66** ; ENV2 : **A 0, D 457 ms, S 0**.
- **ENV3 → transposition des 3 osc : −0,18 / −0,14 / −0,145 (× ±48 st ≈ −8,6 / −6,7 / −7 st)** avec **A 0, D 83 ms, S 0** : la note attaque ≈ 7-9 demi-tons **sous** la hauteur et remonte en 83 ms (« rip » de cuivre inversé).
- ENV1 (amp) : **A 57 ms, D 1,05 s, S 40 %, R 90 ms**.
- Effets : **distorsion type 0, drive 8,7 dB, mix 100 %** ; **compresseur multibande (OTT) mix 100 %, gains bas 16,3 / médium 11,7 / haut 9,7 dB** ; EQ : low shelf **32 Hz −7,2 dB**, bell **2,45 kHz +9,7 dB** ; **reverb mix 100 %** (!), decay 1 s, size 0,23.

**D. « Sci-nema Brass » — Kyutatsuki (« Stereotype movie trailer sound », style Bass) — recette BRAAM lisible** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/kyutatsuki/Sci-nema_Brass.vital
- OSC1 : saw **−12 st, 16 voix, détune 10,2 %**, blend 0,8, niveau 50 %, warp amount 0,41 (type 0).
- OSC3 : wavetable **« Analog_BD_Sin » (sinus) −12 st, niveau 32 %**, sortie 4, warp type 5 → **couche sub** (macro « SUBBASS » : +0,43 niveau, +0,17 warp, −0,22 gain de l'EQ bas).
- **Sample « White Noise » actif, niveau 100 %** (souffle).
- Filtre 1 : Analog style 1, **cutoff 687 Hz, drive 8,5 dB** ; **molette → cutoff +0,45** (ouverture au geste). Filtre 2 : Comb style 3, 131 Hz, résonance 100 %, keytrack 100 % (résonateur).
- ENV1 (amp) : **A 0,5 ms (macro « ATTACK » jusqu'à ≈ 144 ms), D 2,78 s, S 71 %, R 11 ms**.
- Effets : **compresseur multibande mix 100 %, gains 16,3 / 11,7 / 16,3 dB** ; EQ : **low shelf 98 Hz −11,1 dB, bell 554 Hz −7,8 dB** (le grave passe par le sub, pas par la saw) ; **reverb decay 6 s, size 0,5, mix 0 → macro « REVERB » +0,30** ; delay feedback 0,54 synchro, mix 0 → macro +0,17.
- Lecture : c'est exactement la pile « saw large −1 oct + sinus sub −1 oct + bruit → filtre drivé → OTT → reverb très longue » décrite par les tutoriels de §1.1, avec des chiffres.

**E. « euro brass » — zabir (remake d'un « eurobrass » vu sur une vidéo japonaise)** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/zabir/euro_brass.vital
- OSC1 : saw **+12 st, 4 voix, détune 12,3 %**, niveau 58 % ; OSC2 : saw **+12 st, 4 voix, détune 26 %**, niveau 50 %. **Pas de filtre.**
- ENV1 (amp) : **A 0,5 ms, D 493 ms, S 87 %, R 170 ms**.
- **ENV2 (A 0, D 204 ms, S 0, R 4 ms) → tune +0,22/+0,29 st, → voix d'unisson +3/+4, → détune +0,31/+0,48 (brut)** : l'attaque est plus haute, plus large et plus détunée pendant 200 ms.
- ENV3 (D 211 ms) et LFO1 (sinus synchro) → transpose, amounts quasi nuls (résidus).
- **OTT mix 71 %, gains 0,6 / 21 / 22 dB** ; EQ low shelf 76 Hz −3,6 dB ; reverb mix 19 %, **decay 0,064 s, size 0,13** (micro-pièce), pré-delay 0,065.

**F. « brass 1 » — jazen** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/jazen/017-brass_1.vital
- OSC1 : Init **position 90/256**, **5 voix, détune 4,8 %, blend 0, spread 0** (mono-compatible), niveau 13 % ; OSC3 : Init position 59, **−12 st**, 1 voix, morph type 7 (0,32), niveau 8,4 %.
- Filtre 1 : Digital style 1, **147 Hz, keytrack 39 %** ; ENV2 → cutoff 0,32. Filtre 2 : Analog style 1, 262 Hz, résonance 50 %.
- ENV1 (amp) : **A 127 ms, D 2,6 s, S 46 %, R 1,63 s**. ENV2 (filtre) : **A 130 ms, D 1,04 s, S 61 %, R 2,25 s** ; ENV2 → mix du compresseur +0,91 (la compression s'installe avec la note).
- ENV4 (delay 164 ms, A 233 ms) et ENV3 → niveau OSC1 : gonflement retardé (« swell » à deux étages).
- LFO1 **2,1 Hz → détune OSC2 (0,10)** ; LFO2 **0,45 Hz → tune de voix ±0,096 st et warp OSC1** (dérive lente).
- Chorus mix 30 %, depth 0,7, feedback 0,62 ; EQ : low shelf 24 Hz +1,7 dB, **bell 505 Hz −15 dB**, high shelf **2,3 kHz +6,9 dB** ; reverb mix 46 %, **decay 0,23 s**, size 0,08.

**G. « Hurley Brass » — HurleybirdJr (« Simple brass preset »)** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/hurleybirdjr/Hurley_Brass.vital
- OSC1 : saw, **2 voix, détune 1,4 %**, niveau 2 % ; OSC2 : saw **+20 cents, 3 voix, détune 1,2 %**, niveau 2 % (niveaux poussés par la vélocité → 100 %).
- Filtre 1 : Analog style 0, **cutoff 13 Hz (fermé), résonance 43 %, drive 3,1 dB** ; **ENV2 → cutoff 0,66** ; ENV2 : **A 100 ms, D 1,35 s, S 75 %, R 300 ms**.
- ENV1 (amp) : **A 15 ms, D 300 ms, S 86 %, R 206 ms**.
- Random 1/2 → tune ±0,02-0,03 st (dérive analogique). Reverb mix 25 %, decay 1 s.

**H. « Is it Brass or What » — LydeN** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/lyden/Is_it_Brass_or_What.vital
- OSC1 : saw, 1 voix, niveau 40 % ; filtre Analog style 1 **1 294 Hz** sans enveloppe ; ENV1 **A 22 ms, D 1 s, S 100 %, R 90 ms** ; chorus 4 voix mix 50 % ; **OTT mix 100 % (gain bas −30 dB, médium 11,7, haut 3,8)** ; random → niveau par note (0,7). Recette minimale « saw + chorus + OTT ».

**I. « SR801 – Cairo Brass » — Milisonics** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/milisonics/SR801_-_Cairo_Brass.vital
- OSC1 : Basic Shapes **position 134**, 1 voix, warp type 7 (0,4), niveau 50 % ; OSC2 : Basic Shapes position 39, **−12 st**, niveau 19 %, sortie 1.
- Filtre 1 : Analog style 4, **cutoff 136 Hz, keytrack 100 %** ; ENV2 → cutoff 0,23 (≈ +30 st) ; macro « BRIGHTNESS » → cutoff 0,18. Filtre 2 : Comb 131 Hz, mix 0 → ENV2.
- ENV1 (amp) : **A 54 ms, D 1 s, S 61 %, R 90 ms**. ENV2 : **A 0,5 ms, D 200 ms, S 0**.
- **LFO1 5,5 Hz → tune de voix via molette (jusqu'à 0,42)** : vibrato à la molette.
- Chorus 4 voix (mix via macro « CHORUS » jusqu'à 0,48) ; delay mix 41 %, feedback 18 %, synchro (mode 2) ; reverb mix 41 %, **decay 2,1 s**, **coupe-bas d'entrée 262 Hz** ; EQ bell 830 Hz +3,9 dB, high shelf +3,8 dB.

**J. « Realstic Brass » — MakcTelephones (« Epic brass »)** — https://raw.githubusercontent.com/ArcerionDev/vital_discord_preset_archive/master/makctelephones/Realstic_Brass.vital
- Recette atypique : OSC2 Basic Shapes position 0, **7 voix, détune 0 %**, niveau 100 % ; OSC1 (16 voix, morph spectral 4 à 0,87) au niveau 0 mais **gaté par le LFO1 synchro (index 8) → niveau 0,67** ; filtre 1 **Comb 523 Hz résonance 100 %** (ENV1 → blend transpose), filtre 2 Analog 157 Hz mix 74 % (LFO1 → cutoff 0,55) ; ENV1 **A 116 ms, D 1 s, S 78 %, R 4,5 s** ; vélocité → drive/mix de distorsion ; chorus 4 voix 23 % ; distorsion drive −3,3 dB mix 28 % ; reverb 49 %, 1 s. À considérer comme texture, pas comme référence.

**K. « Mid Horn » — miserlou (style Lead, mono legato) — recette trap/horn** — https://raw.githubusercontent.com/Miserlou/VitalPresets/master/Presets/Mid%20Horn.vital
- OSC1 : saw, **14 voix, détune 24 %**, niveau 14 % ; OSC2 : Basic Shapes position 0, 5 voix, détune 5,2 %, niveau 1,7 % ; **OSC3 : saw +12 st, 13 voix, détune 24 %, niveau 21 %**.
- Filtre 1 : Analog style 0, **942 Hz** ; ENV2 → cutoff +0,12 (≈ +15 st) et → drive de distorsion +0,075 ; ENV2 : **A 0,5 ms, D 1,3 s, S 0**. Filtre 2 : **Comb 262 Hz, résonance 79 %, keytrack 100 %** ; ENV3 (A 14 ms, D 297 ms) → résonance +0,125.
- ENV1 (amp) : **A 6,4 ms, D 156 ms, S 74 %, R 1,61 s**.
- Effets : **distorsion mix 98 % (drive 0 dB, poussé par ENV2)** ; **OTT mix 100 %, gains 11,4 / 23,5 / 14,5 dB** ; EQ low shelf **152 Hz −5,3 dB** ; reverb mix 16 %, **decay 4,3 s**, size 0,52.
- **Mono, legato, portamento 53 ms**.

**L. « Trappy Wub Reverb Horn » — miserlou** — https://raw.githubusercontent.com/Miserlou/VitalPresets/master/Presets/Trappy%20Wub%20Reverb%20Horn.vital
- OSC2 : saw, **1 voix**, warp type 7 à 0,04 (ENV2 → +0,08), sortie 2 ; (OSC1 +24 st au niveau 0).
- Filtre : **Ladder style 1, 221 Hz, résonance 22 %** ; **ENV2 → cutoff 0,43 (≈ +55 st)** ; ENV2 : **A 244 ms, D 133 ms, S 32 %** → « wah » lent à l'attaque.
- ENV1 (amp) : défauts (**A 0,5 ms, D 1 s, S 100 %, R 90 ms**).
- **OTT mix 18 %** ; **reverb mix 68 %, decay 3,7 s, size 0,59** ; mono, portamento 110 ms.

**M. « Faker Shady Horns » — miserlou** — https://raw.githubusercontent.com/Miserlou/VitalPresets/master/Presets/Faker%20Shady%20Horns.vital
- Deux « Basic Shapes » (positions 86 et 111), 1 voix chacun ; filtres fermés (13 Hz rés. 72 %, 36 Hz rés. 64 %) ouverts par la macro 3 ; **LFO1 synchro (index 8) → tune OSC2 ±0,59 st, → drive/résonance de distorsion** ; **distorsion type 1, drive 22 dB, mix 100 %** ; OTT 82 % ; chorus 4 voix 20 % ; delay 24 % ; mono legato, portamento 76 ms. Un « wobble horn » plus qu'un cuivre.

### 2.3 Patchs d'usine Surge XT « Brass » (XML lu) [DOC — fichiers lus]

Dépôt : https://github.com/surge-synthesizer/surge/tree/main/resources/data/patches_factory/Brass — fichiers : Brassy, Buggy Brass, Crisp Noise Brass, JX-10 Double Brass, OB-8 Jump, Plastic Brass, Reso Brassy, Synth Brass 1/2/3, Toto Brass (auteur « Claes » = Claes Johanson, créateur de Surge). Huit lus ; « Buggy Brass », « Crisp Noise Brass », « Plastic Brass » non téléchargés (le fichier `Brassy.fxp` porte en interne le nom « Buggy Brass »).

**« Synth Brass 1 »** — https://raw.githubusercontent.com/surge-synthesizer/surge/main/resources/data/patches_factory/Brass/Synth%20Brass%201.fxp
- OSC1 **Wavetable « Sine »**, Morph 0,003, **Skew Horizontal 0,29** (une sinusoïde « penchée » devient une quasi-dent de scie), unisson 1 voix (détune 20 cents inactif) ; OSC2/3 coupés.
- **Skew H modulé négativement par l'aftertouch (−0,72), l'EG de filtre (−0,93) et la vélocité (−0,51)** : la forme d'onde s'éclaircit à l'attaque puis se calme — brillance par la wavetable, pas seulement par le filtre.
- Filtre 1 : **LP 24 dB, cutoff 315 Hz, résonance 0,10, keytrack 0,91, Env Mod 24,2 ; vélocité → cutoff +42,2**. Feedback de bloc 0,49.
- **Amp (env1) : A 6 ms, D 1 s, S 1,0, R 159 ms. Filtre (env2) : A 4 ms, D 2,09 s, S 0, R 656 ms.**
- Pitch ← LFO1 (sinus 1 Hz) profondeur 0,47 (vibrato/dérive). VCA level +6,7 dB, sensibilité vélocité −17 dB.
- Effets : EQ (fx1), delay (fx5), reverb 1 (fx6).

**« Synth Brass 2 »** — …/Brass/Synth%20Brass%202.fxp
- OSC1 Wavetable, Morph 0,003, **Skew H 1,0** ; **OSC2 Classic (saw) +0,17 st, Sub Mix 0,42, Sync 11,7 st** (le hard sync donne le « cuivré »).
- Filtre 1 : **LP Legacy Ladder, cutoff 328 Hz, résonance 0,59, Env Mod 71,8 (!)** ; molette → cutoff −9,4 et → Env Mod −56 (la molette « assombrit »).
- Amp : A 4 ms, D 1 s, S 1,0, R 31 ms. **Filtre : A 4 ms, D 8,5 s, S 0, R 250 ms** (une longue descente de brillance).
- Pitch ← LFO1 0,30. Effets : **Chorus (fx1)**, delay (fx5).

**« Synth Brass 3 »** — …/Brass/Synth%20Brass%203.fxp
- OSC1 Wavetable **« Saw ATC »**, Morph 0,667 (← keytrack +0,17), Skew H 0,43, unisson 1 voix (détune 24 cents).
- Filtre 1 : LP Legacy Ladder, **cutoff 234 Hz, résonance 0,17, Env Mod 29,3, keytrack 0,66**.
- **Amp : A 4 ms, D 2,5 s, S 0, R 31 ms (stab)** ; **Filtre : A 78 ms, D 4,5 s, S 0, R 250 ms**. VCA +11,3 dB. Pitch ← LFO1 0,30. Effets : delay.

**« Buggy Brass » (fichier `Brassy.fxp`)** — …/Brass/Brassy.fxp
- OSC1 Classic saw, **octave −1, −0,05 st, unisson 2 voix, détune 10,2 cents** ; OSC2 Classic saw **octave −1, 2 voix, détune 3,6 cents** ; OSC3 coupé ; niveaux 0,87 / 1,0.
- Filtre 1 : **LP 24 dB, cutoff 455 Hz, résonance 0, keytrack 0,22, Env Mod 27,3** ; **macro 1 « Cutoff » → +26,5 ; vélocité → cutoff +28,9 et → Env Mod +26,7**.
- **Amp : A 512 ms (← vélocité −4,9 en log2 → ≈ 17 ms à vélocité max), D 250 ms, S 1,0, R 61 ms** ; **Filtre : A 177 ms (← vélocité −1,8 → ≈ 50 ms), D 457 ms, S 0,43, R 250 ms**. Autrement dit : **la vélocité accélère les deux attaques** — c'est le geste « cuivre doux/cuivre fort ».
- **LFO1 7,3 Hz, amplitude 0 ← aftertouch +1 / molette +1 → pitch ±5,7 st (profondeur max)** : vibrato à l'aftertouch ; macro 2 « Vibrato Rate » ; LFO2 sinus 1 Hz → pitch ±0,56 st (dérive).
- Effets : delay (fx1), reverb 1 (fx5).

**Famille « Sawteeth » = « OB-8 Jump », « JX-10 Double Brass », « Toto Brass », « Reso Brassy »** (même patch de base, réglages différents) — …/Brass/OB-8%20Jump.fxp, …/JX-10%20Double%20Brass.fxp, …/Toto%20Brass.fxp, …/Reso%20Brassy.fxp
- Commun : **OSC1 Classic saw, octave −1, unisson 9 voix, détune 12,3 cents** ; **OSC2 Classic saw, octave −1, +0,13 st (OB-8 : +0,075), unisson 8 voix, détune 20 cents** ; OSC3 coupé ; **17 voix au total** ; filtres 1 et 2 **LP 12 dB** ; feedback 0,61 ; **macro 1 → Shape OSC1 (+0,57) et Sub Mix (+0,21)** ; **filtre 1 cutoff ← aftertouch +19,2, ← molette +42,1, ← vélocité +53,4 ; résonance ← vélocité +0,48** ; delay (fx5) + reverb 1 (fx6).
- **OB-8 Jump** : OSC1 −0,11 st ; **filtre 1 cutoff 2,8 kHz, résonance 0, Env Mod 17,3, keytrack 1,0** ; filtre 2 440 Hz Env Mod 19,5 ; **amp A 4 ms, D max (gate), S 1, R 97 ms ; filtre A 4 ms, gate, R 112 ms** → accords plaqués, brillants, ouverts (référence « Jump » de Van Halen, OB-Xa).
- **JX-10 Double Brass** : **octave de scène +1** ; filtre 1 **46 Hz, résonance 0,36, Env Mod 34,3** ; filtre 2 440 Hz Env Mod 22,1 ; **amp A 40 ms, gate, R 97 ms ; filtre A 50 ms, gate, R 112 ms** → attaque plus lente, filtre fermé qui s'ouvre par la vélocité/molette.
- **Toto Brass** : filtre 1 46 Hz, résonance 0,36, Env Mod 15,3 ; **amp A 40 ms ; filtre A 34 ms** ; reste identique.
- **Reso Brassy** : filtre 1 **68 Hz**, résonance 0,36, Env Mod 15,3 ; **amp A 9 ms ; filtre A 512 ms** (montée de brillance lente sur une attaque d'amplitude rapide) ; LFO1 rampe 2,5 Hz (non routé).

### 2.4 Recettes des fiches lues (tiers, texte intégral) [HEUR-lu]

**« Brass Lead / Synth Brass » (GMS, FL Studio ; valeurs en % du plugin)** — https://raw.githubusercontent.com/JaZeR-444/fl-studio-master-hub/56bfdb7386552533f78e057a1183bf712b4bb5f5/src/data/plugins/gms/workflow/by-instrument/lead-creation.md
- OSC1 saw ; **OSC2 carré +7 st** (mix 80 %) ; **OSC3 saw −12 st** (mix 50 %) ; **unisono 4 voix, stéréo 50 %** ; **LP cutoff 75 %, résonance 22 %** ; **amp A 8 %, D 30 %, S 90 %, R 30 %** ; **EG1 → cutoff : A 0 %, D 25 %, amount +35 %** ; **distorsion 20 %**, echo medium. Vibrato conseillé : LFO sinus, rate 25 %, ±8-12 %, retrig off. Mix leads : couper 200-400 Hz, booster 2-4 kHz, air 8-12 kHz ; compression 3-6 dB.

**Rebuild OB-Xa/OB-8** (fiche synthés) : **6-8 saws sur une note, ±15 cents, LPF 12 dB/oct, enveloppe de filtre rapide et profonde, accords plaqués à attaque forte** ; chorus Juno = deux lignes 20-30 ms modulées ≈ 0,5 Hz (I) et ≈ 2 Hz (II), profondeur ≈ 5 ms, 50/50. — …/theory/10-instruments/03-analog-polysynths.md

**Forme d'enveloppe « synth brass »** (Instatetragrammaton) : enveloppe d'amplitude **« Gate » (A 0, D max, S max, R 0) avec l'attaque un peu augmentée**, combinée à une enveloppe de filtre **« Pluck » (A 0, D 50 %, S 0) avec l'attaque légèrement augmentée** ; « 50 % de decay = 1 s dans Serum ». — https://raw.githubusercontent.com/instatetragrammaton/Patches/cb65e685e77cf0d6c26d11ff391136cf01bfd427/Synthesis/Common-Envelope-Shapes.md

**Accord future bass, supersaw JP-8000, stab M1** : voir §1.2 et §1.5 (valeurs déjà données).

**Virus TI (fiche lue)** : « strong filter env amount → punchy synth brass, techno stabs ». — https://raw.githubusercontent.com/nstarke/starkerack/96caf1afb4e4edcd546b5cc2277a4754d416d8fa/create-melodic-components/md/Access_Virus_TI_Snow.md

**Ableton Wavetable (fiche LivePilot lue)** : « Supersaw Lead : deux osc Basic Shapes saw, **unisson Classic 8 voix**, LP ≈ 5 kHz avec enveloppe, drive modéré » ; Analog conseillé pour « les patchs soustractifs classiques : basses, leads, pads, **brass** » ; Drift : unisson 4 voix. — https://raw.githubusercontent.com/dreamrec/LivePilot/f3ec16a59ab719023201c4dc3fb76b10f691c0ed/livepilot/skills/livepilot-core/references/device-atlas/synths-native.md

### 2.5 Recettes tirées d'extraits (à revérifier) [HEUR-extrait]

- **Lead big room / trance (Myloops)** : A saw 7 voix, detune 0,25-0,30, blend 0,8 ; B saw 3 voix, detune 0,15, −1 oct, −6 dB.
- **Screech hardstyle (ADSR, Serum)** : Basic CJW ; A=B, 7 voix, détune haut ; LFO1 → coarse pitch ≈ 20 Hz libre ; LFO2 mode Env → master tune ; pitch env DEC/AMT ; Peak 12 résonant, cutoff ← LFO2 ; Drive + Fat.
- **Lead hardstyle (Screech House)** : 2 osc × 16 voix, détune fort, B +1 octave.
- **Brass stab EDM (Producer School)** : sample staccato + copie à +1 octave, EQ corps/présence, distorsion, compression, reverb, sidechain.
- **Brass pluck (Mystic Alankar)** : A Hypa + B Analog BD Sine, env descendante → Warp A/B + niveau A, boost 3e/5e harmoniques.
- **Future bass (Monosounds/Unison/Bowes)** : 7 voix detune 0,12 blend 75 % ; OTT 20-30 % ; LFO 1/8 dessiné pour un 1/16 swingué.

### 2.6 Propositions de transposition vers Serum 2 et Ableton Live 12 [TEST — mes déductions, à valider dans le Set]

- **Synth brass 80s (d'après Surge « Sawteeth », Vital « 80s Saw Brass », GMS)** : Serum 2 osc A saw unisson 7-9 voix détune ≈ 0,10-0,15 (Serum affiche 0..1 ; 12-20 cents ≈ 0,12-0,20 [MÉMOIRE, non vérifié]), osc B saw unisson 6-8, ±0,1 st, éventuellement −12 st ; filtre **MG Low 12** (12 dB) cutoff 300-500 Hz, résonance 0-15 %, keytrack 100 %, Env 2 → cutoff +40-70 % ; Env 1 A 5-40 ms D 300-500 ms S 85-100 % R 60-160 ms ; Env 2 A 30-100 ms D 400-600 ms S 0-45 % R 100-250 ms ; vélocité → cutoff ; LFO 1 sinus 5-7 Hz → pitch via molette/AT ; chorus + delay + reverb 1-2 s. Registre : accords plaqués **MIDI 48-72**, lead 60-79.
- **Braam (d'après Vital « Sci-nema », synthdef `braam`, extraits)** : 3 pistes Ableton : (1) Serum 2 saw unisson 16 voix détune ≈ 0,10-0,20, joué **C1-C2 (MIDI 24-36)** ; (2) sub sinus −1 oct ; (3) Sample osc ou Simpler avec un sample d'usine `Factory/Brass/Trombone.flac` ou `Brass Wall Low.flac` ; filtre LP 24 drivé 600-700 Hz + enveloppe 1,5 s ; **amp A 50 ms, D 2-3 s** ; Saturator/Amp puis Multiband Dynamics (OTT) puis Reverb decay 5-6 s en groupe ; pitch bend −2 à −12 st sur la queue ; EQ : couper 100 Hz et 500 Hz sur la couche saw, garder le sub propre.
- **Brass stab house/UKG** : Simpler (Classic ou One-Shot) sur une section de cuivres staccato, **transpose ±5-7 st**, filtre LP 200 Hz → 8 kHz automatisé, Auto Filter/phaser pour la french house ; enveloppe amp decay 150-400 ms, reverb courte gatée ; jouer sur les contretemps, voicings MIDI 55-75.
- **Trap horn (d'après Vital « Mid Horn »)** : Serum 2 A saw 14 voix + B saw +12 st 13 voix, LP 24 ≈ 900 Hz + Env 2 courte, **Env 1 A 6 ms D 150 ms S 75 % R 1,5 s**, distorsion + OTT + reverb 4 s, **mono legato porta 50 ms**, registre MIDI 55-70.
- **Accords future bass** : Serum 2 A saw 7 voix détune 0,12 blend 0,75, HPF 250 Hz, OTT 20-45 %, LFO 2 sinus 1/8 → fine pitch ±10-50 cents (retransposer si la source donnait un tempo), sidechain 4-6 dB, voicing MIDI 60-84, 3 notes max par instance.

---

## C. Pages consultées (livrable c)

### C.1 Fichiers réellement lus (intégralement) — tous sur GitHub (raw)

**Primaires (presets, patchs, code, corpus) — [DOC]**
1. Corpus Serum 2 : https://raw.githubusercontent.com/pycabbage/flp-extract-fxp/a83908a3e27b16bfc42dc63c5105b5c56e36da80/docs/s2-param-corpus.md (75 Ko, lu en entier ; index du dossier docs : https://github.com/pycabbage/flp-extract-fxp/tree/main/docs)
2. Surge XT — 8 patchs .fxp du dossier Brass (XML extrait et parsé) : https://github.com/surge-synthesizer/surge/tree/main/resources/data/patches_factory/Brass (Synth Brass 1, 2, 3 ; Brassy [= Buggy Brass] ; OB-8 Jump ; JX-10 Double Brass ; Toto Brass ; Reso Brassy)
3. Surge XT — code : Parameter.cpp, ModulationSource.h, SurgeStorage.h, dsp/SurgeVoice.cpp, dsp/oscillators/ClassicOscillator.cpp, dsp/oscillators/WavetableOscillator.cpp ; sst-filters FilterConfiguration.h (URLs en §0.3)
4. Vital — code : https://raw.githubusercontent.com/mtytel/vital/main/src/common/synth_parameters.cpp
5. Vital — 12 presets JSON : 80s_Saw_Brass, Musinous_-_Brass_Stabs, euro_brass, 017-brass_1, Realstic_Brass, Sci-nema_Brass, Hurley_Brass, Is_it_Brass_or_What, SR801_-_Cairo_Brass (dépôt https://github.com/ArcerionDev/vital_discord_preset_archive) ; NavigatorSynthBrass (https://github.com/instatetragrammaton/Patches) ; Mid Horn, Trappy Wub Reverb Horn, Faker Shady Horns (https://github.com/Miserlou/VitalPresets)
6. vibelang — synthdefs : cinematic/braam.vibe, brass/synth_brass.vibe, brass/brass_section.vibe, brass/trumpet.vibe, brass/trombone.vibe (+ tuba, french_horn, brass_realistic téléchargés, non exploités) : https://github.com/trusch/vibelang/tree/main/crates/vibelang-std/stdlib

**Secondaires (fiches de recettes/genres de tiers) — [HEUR-lu]**
7. mekedron/claude-amen-sessions (ref ff63fa0…) : theory/10-instruments/14-iconic-patch-recipes.md ; 03-analog-polysynths.md ; 05-fm-and-phase-distortion.md ; 07-samplers-and-workstations.md ; 12-software-instruments.md ; theory/20-genres/09-edm-and-future-bass.md ; 01-house.md ; 07-uk-garage-and-grime.md ; 08-hardstyle-and-hardcore.md ; 10-hiphop-and-trap.md ; 11-drill.md ; 16-synthwave-and-retro.md ; 19-funk-soul-and-rnb.md ; 23-film-and-game-score.md ; 26-afrobeats-and-amapiano.md ; 29-disco-and-italo.md ; theory/30-patterns/05-melodic-hooks-and-riffs.md ; 06-transitions-and-fx.md ; 08-sound-design-recipes.md ; 11-signature-techniques.md
8. JefroB/Electronic-Music-Genre-Skills (ref 19f8373…) : .agent/skills/genre-dancehall-afrobeats/references/sound-design.md ; genre-dubstep-bass/references/sound-design.md et production-techniques.md ; genre-synthwave-darkwave/references/sound-design.md et production-techniques.md ; genre-house/references/sound-design.md et production-techniques.md ; genre-hiphop-trap/references/sound-design.md ; genre-uk-garage-grime/references/sound-design.md ; genre-african-latin-electronic/references/sound-design.md ; genre-disco-nudisco/references/sound-design.md ; genre-hard-dance-happy-hardcore/references/sound-design.md ; genre-hardcore-bouncy/references/sound-design.md ; genre-trance/references/sound-design.md
9. JaZeR-444/fl-studio-master-hub : src/data/plugins/gms/workflow/by-instrument/lead-creation.md
10. instatetragrammaton/Patches : Synthesis/Common-Envelope-Shapes.md
11. dreamrec/LivePilot : livepilot/skills/livepilot-core/references/device-atlas/synths-native.md
12. Gaku52/dj-skills-guide : docs/production/10-bass-melody/lead-synth.md
13. nstarke/starkerack : create-melodic-components/md/Access_Virus_TI_Snow.md

### C.2 Pages bloquées par le proxy (EGRESS_BLOCKED ou « unable to fetch »)

professionalcomposers.com (braam) ; vi-control.net (Making Braams) ; violetrecording.com ; morphic.com ; productionmusiclive.com (×3 : supersaw tips, future bass synth, Keinemusik) ; monosounds.studio (×2) ; macprovideo.com ; en.wikipedia.org (BRAAAM) ; attackmagazine.com ; adsrsounds.com (×2) ; ujam.com ; glitchmagic.com ; mysticalankar.com (×2) ; syntorial.com ; blog.native-instruments.com ; beatportal.com ; youtube.com ; reddit.com ; kvraudio.com ; xferrecords.com ; support.xferrecords.com ; ableton.com (manuel) ; splice.com ; soundonsound.com ; edmprod.com ; cymatics.fm ; musicradar.com ; web.archive.org ; surge-synthesizer.github.io ; gearspace.com ; medium.com ; landr.com. Aucun 403/404/410 « réel » n'a pu être observé, le blocage intervenant avant.

### C.3 Pages utilisées uniquement via extraits de recherche (non lues)

Voir les URLs citées en §1 avec le tag [HEUR-extrait] ; principales : Ableton blog (impact sounds), Professional Composers, VI-Control, Richard Pryn, Epic Stock Media, Collider, Vice/WhoSampled (Mask Off), Glitch Magic, UJAM, Mystic Alankar, PML, Monosounds (×3), Unison.audio, Medium/Dylan Bowes, Myloops, Screech House (×2), ADSR (screech), The Producer School, Wikipédia (French house, BRAAAM, Mask Off, Abalele), Gearspace, ProducerStack, bpmcalc/BeatKey, Incognet, Sample Focus blog, Beatportal, Red Bull Music Academy, Progrography, Vintage Soundset, Reverb Machine, Synth Ctrl, Syntorial, Tonepusher/ADSR, NewRetro, xferrecords.com, Impact Soundworks, Freelance Soundlabs, Innovation Sounds, Loopmasters, Splice.

## D. Ce qui n'a pas été trouvé (livrable d)

1. **Aucun tutoriel commercial (Attack Magazine, ADSR, PML, Cymatics, EDMProd, SOS) n'a pu être lu** ; les chiffres qui en viennent sont des extraits à revérifier. Attack Magazine n'apparaît même pas dans les résultats de recherche pour « braam ».
2. **Serum 2** : pas de liste des noms de presets d'usine contenant « Brass » ; pas de tag « Brass » dans les métadonnées ; le forum Xfer et KVR n'ont rien donné. Ce qui est établi : dossier de samples d'usine `Factory/Brass/` (Brass Wall Low, Trombone, Trombone Alt), sample `Factory/Synth/DX Brass2 C2`, multisamples `Factory/Winds/` (French Horns, Trumpets LE, Trombones Tenor LE, Trombones Cimbasso LE) et `Factory/Synth/Arp Solina - Horn`. La table des paramètres d'unisson/détune de Serum 2 (unités affichées) n'a pas été lue.
3. **Braam** : pas de recette Serum/Ableton chiffrée lue dans une source de tutoriel ; les seules recettes chiffrées sont le synthdef `braam` et le preset Vital « Sci-nema Brass ». Les valeurs exactes de pitch drop (demi-tons/secondes) et de durée de reverb des tutoriels restent inconnues.
4. **Trap / drill** : aucune recette Metro Boomin / 808 Mafia chiffrée (vidéos non transcrites) ; « Mask Off » est une flûte ; aucune source ne documente les « orchestral brass hits » du drill autrement que par des packs de samples.
5. **Afro house / amapiano / afrobeats** : aucune recette de cuivres ; les guides Keinemusik/Black Coffee lus en extrait n'en mentionnent pas ; seuls des packs (House Horns 125 BPM, Trumpet Love) et des principes d'arrangement afrobeat (stabs contretemps, tierces/sixtes, slapback) ont été trouvés. Rien sur Black Coffee avec cuivres, rien de précis sur les cuivres en amapiano hors saxophone live.
6. **Big room « brass stab » (Hardwell/Garrix)** : pas de valeurs de synthèse spécifiques (seulement le lead supersaw Myloops et les packs de presets) ; Fisher « Losing It » : tutoriels vidéo non exploitables.
7. **French house / Daft Punk** : pas de recette de découpe chiffrée lue (seulement les principes filtre/phaser/sample de Wikipédia et les fiches de tiers).
8. **Synthwave** : pas de recette « brass » spécifique de The Midnight (saxophone) ni de Timecop1983 (les extraits donnent des leads/basses) ; Kavinsky : recette Syntorial en extrait seulement.
9. **BPM** : aucune des sources à LFO synchronisé ne donne son tempo.
10. **Vital** : la table des noms de tempo synchro (`kSyncedFrequencyNames`) et le sens exact de `filter_style` n'ont pas été lus ; les valeurs brutes sont conservées dans le rapport.
