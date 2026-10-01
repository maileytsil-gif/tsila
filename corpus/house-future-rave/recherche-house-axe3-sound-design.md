---
titre: "Rapport de recherche — axe 3 : Recherche axe 3 — Sound design professionnel, recettes chiffrées"
source: recherche web et GitHub, session Claude Code du 2026-09-24 (agent de recherche)
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: sound design professionnel (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: synthèse interne avec étiquettes de preuve ; les sources primaires sont citées dans le texte
---

# Recherche axe 3 — Sound design professionnel, recettes chiffrées
## Future rave · bass house · house de festival et de club (future house, tech house, big room)

Date : 24 septembre 2026. Cible : Ableton Live 12 Suite + Serum 2 (équivalents natifs Wavetable, Operator, Analog, Drift, Simpler/Sampler, Drum Rack), plug-ins FabFilter Pro-Q 4, Waves REQ 6 / API-2500 / L2 / J37 / MetaFlanger / F6, bx_glue, soothe3, iZotope Imager.

### Méthode et limites

- 15 requêtes WebSearch (quota épuisé), aucun site hors GitHub téléchargeable (EGRESS_BLOCKED vérifié sur musicradar.com). Les pages web ne sont donc connues que par leurs **extraits de recherche** ; toutes les valeurs qui en viennent sont marquées **[DOC-EXTRAIT]** et restent à vérifier sur la page (liste dans `urls-axe3.json`).
- 24 documents GitHub lus en entier et archivés dans `corpus/house-future-rave/` (liste en §6). Les plus utiles sont des **compilations secondaires** (dépôt `wgpatrick/dotbeat`, dépôt `mekedron/claude-amen-sessions`) qui résument des tutoriels Attack Magazine, MusicRadar, Sound on Sound, KVR, NI, unison.audio, etc. en citant l'URL de chaque recette : elles sont marquées **[DOC-2]** (document lu, source primaire non lue) avec la source primaire nommée.
- Les fichiers du dépôt déjà chiffrés ont été relus : `patches-genres.md` (Garage Bass, Beat-Pulsing Plucks, Warping Bass, ANNA, OTT, tempo), `basses.md`, `leads-nappes-textures.md` (thèse Szabo), `percussions.md`, `fiches-pratiques.md` 36–37, `serum2-cartographie.md` (noms de paramètres), et dans `corpus/cuivres/` : `monosounds-studio-serum-2-supersaw.md` (qui contient une ligne **future rave**), `amen-sessions-14-iconic-patch-recipes.md`, `jefrob-house-sound-design.md`, `amen-sessions-01-house.md`, `-09-edm-and-future-bass.md`. Marqués **[DOC]**.
- **[HEUR]** = déduction ou pratique, logique donnée ; **[CALC]** = calcul ; **MUET** = aucune source ne le chiffre.

### Constat général, à lire en premier

1. **Aucune page écrite ne chiffre un patch « future rave » de David Guetta / MORTEN.** Les 3 recherches dédiées n'ont sorti que des packs de presets (Vandalism « Shocking Future Rave », 7 Skies « FUTURA », Defrock, EDM People) et un cours vidéo (Sonic Academy, Protoculture, « Kick and Bass » avec Kick 2). Le seul chiffrage direct est la ligne **Future rave** du guide supersaw de Monosounds, déjà dans le corpus : *unison 5, detune 0,09, passe-bas balayé 400–900 Hz, « une supersaw déguisée en basse »*. Tout le reste de la fiche FR-1 est reconstruit à partir de l'ancêtre documenté (hoover Alpha Juno, ±40 cents, −12, enveloppe de pitch 8 st) et du supersaw JP-8000 mesuré (Szabo).
2. **Les basses house / bass house sont, elles, très bien chiffrées** : 10 recettes de basses house (dotbeat `priors/bass-house.md`, sources Attack, MusicRadar, SoundBridge, Splice/Tracey Brakes), 15 de Reese/wobble/808, 16 de stabs et pads, 12 de kicks/claps/hats, plus des **médianes mesurées sur 3 559 patchs Surge** (recherche 141 de dotbeat) qui tranchent plusieurs querelles de tutoriels : attaque d'ampli de basse **3,9 ms** (83 % ≤ 12 ms), decay médian **621 ms**, detune de lead médian **10 cents** (le plus étroit des rôles), decay de pluck médian **867 ms**, attaque de pad médiane **541 ms**, release d'accords **31 ms** (« la queue vient des sends »).
3. **Le Korg M1 se réduit à deux presets pour la house** : I01 *Piano 16* (Black Box « Ride on Time », Snap! « Rhythm Is a Dancer », CeCe Peniston « Finally », Madonna « Vogue ») et I17 *Organ 2* (Robin S « Show Me Love », Crystal Waters « Gypsy Woman », Nightcrawlers « Push the Feeling On »). « Vogue = Organ 2 » est **faux** (c'est Piano 16). Les deux sont des échantillons PCM : la voie fiable est le **multisample** (Serum 2 moteur Multisample, Simpler/Sampler), la synthèse ne donne qu'une approximation.
4. **Erreur à corriger dans `basses.md`** : « modulateur monté de 2 octaves et 7 demi-tons (donc une quinte, rapport 3:1) » — 2 octaves + quinte = 4 × 1,5 = **6:1** [CALC]. 1 octave + quinte = 3:1.

### Conventions Serum 2 (noms exacts, `serum2-cartographie.md` [DOC])

OSC A/B/C : LEVEL, PAN, OCT / SEMI / FINE (cents), CRS, UNISON 1–16, DETUNE 0–1 (course = RANGE, Global, 0–48 st, défaut 2 st), BLEND (défaut 75 %), WIDTH, Stack (12, 12+7, Center-12…), Tuning (Linear · Super · Exp · Inv · Random), WT POS, WARP 1 / WARP 2, PHASE, RAND, Pitch track, mode d'accordage Semitone / Harmonics / Ratio. SUB (6 formes). NOISE (White / Pink / Brown / Geiger, one-shot, key track). FILTER 1 / 2 : TYPE (MG Low 6/12/18/24, French LP, German LP, Formant I/II/III, Comb, Scream LP/BP, Acid Ladder…), CUTOFF (8 Hz – 22,05 kHz), RES 0–100, DRIVE, VAR, MIX, key track. ENV 1–4 : DELAY, ATTACK, HOLD, DECAY, SUSTAIN, RELEASE, BPM. LFO 1–10 : Mode Off / Trig / Env, RATE (BPM : 32 bar → 1/256), DOT, TRIP, SMOOTH, RISE, DELAY, PHASE, MONO. MACRO 1–8, MATRIX (64 slots, aux, courbes). Page MIX : routage Filter / Main / **Direct** (contourne filtre et FX) / None, BUS 1/2. FX : Distortion (TYPE, DRIVE, filtre PRE/POST), Compressor (MULTIBAND = « OTT », THRESH, RATIO, ATTACK, RELEASE, MIX), Hyper/Dimension (UNISON, DETUNE, RATE, SIZE, MIX), Chorus, Delay (MODE, temps L/R, FEEDBACK, FREQ/BW), Reverb (TYPE, LO CUT, HI CUT, SIZE, PRE-DLY, DAMP, WIDTH), Equalizer, Filter, Utility (MONO BASS + FREQ 20–400 Hz, WIDTH), Bode, Convolve, Splitter L/H · L/M/H · M/S. GLOBAL : POLY / MONO / LEGATO, PORTA 0–8 s, CURVE, ALWAYS, SCALED, Pitch bend UP 1–24 / DOWN −1…−12.

### Tempo : divisions en millisecondes [CALC]

| Division | 126 BPM | 128 BPM |
|---|---|---|
| 1 mesure | 1905 ms | 1875 ms |
| 1/4 | 476 | 469 |
| 1/8 | 238 | 234 |
| 1/8 triolet | 159 | 156 |
| 1/16 | 119 | 117 |
| 1/16 triolet | 79 | 78 |
| 1/32 | 60 | 59 |

Ce qui ne bouge pas avec le tempo : hauteurs, ratios FM, unison/detune, cutoff, résonance, drive, EQ. Ce qui se transpose seul : toute division synchronisée (LFO, delays, ENV en mode BPM). Ce qui se recalcule : les millisecondes (decays rythmiques, glide, pre-delay). Voir `patches-genres.md` §7.

---

# 1. Future rave

## FR-1 — Le lead « rave » (saws désaccordées, pitch-bend / portamento, filtre résonant, dimension)

**Cible.** Un lead qui est en réalité une **basse-lead mono, sombre, à filtre résonant** (Monosounds : « une supersaw déguisée en basse »), plus un hoover atténué : pitch qui glisse **vers** la note à chaque attaque, saws désaccordées, chorus/dimension. Description commerciale concordante : « punchy pitched-up techno-style synths and driving basslines » (Cr2), « enormous detuned leads », « extremely powerful supersaws » (Vandalism, EDM People) [DOC-EXTRAIT].

**Moteur.** Serum 2 (unison, deux filtres, Hyper/Dimension, PORTA SCALED). Natif : Wavetable (unison Classic, mode Randomize) + Analog pour le hoover ; Drift pour une version mono chaude.

| Étage | Réglage | Unité / valeur | Source |
|---|---|---|---|
| OSC A (corps) | table Basic Shapes, saw ; UNISON **5** ; DETUNE **0,09** ; BLEND 75 % ; WIDTH 50–60 (couche grave, cf. Monosounds : « pull the low octave in to width 50–60 ») | Serum 0–1 / % | Monosounds, ligne « Future rave » [DOC] |
| OSC B (poids) | même saw, OCT **−1** ; UNISON 5 ; DETUNE **0,08** ; WIDTH **55** ; niveau « aux deux tiers sous A » | | Monosounds, recette générale [DOC] |
| OSC C (option, drops) | saw OCT **+1** ; UNISON 5 ; DETUNE 0,10 ; WIDTH 95 ; **HPF 2 kHz** sur cette couche | | Monosounds [DOC] |
| FILTER 1 | passe-bas (MG Low 24 ou French LP [HEUR]), CUTOFF **≈ 600 Hz** au repos, balayé **400–900 Hz** par ENV 2 ou automation ; « le mouvement de filtre est le hook » ; RES **non chiffrée** (résonant d'après le brief ; 20–35/100 [HEUR], « just a touch » dans les stabs Attack) | Hz | Monosounds [DOC] ; RES [HEUR] |
| ENV 1 (ampli) | A 1–5 ms, D 250 ms, S 60 %, R **31 ms** (release courte : la queue vient des sends) | ms | dotbeat `supersaw-trance-lead` (mesuré, 448 patchs lead : attaque médiane 3,9 ms, release médiane 31 ms) [DOC-2] |
| ENV 2 → CUTOFF | A 2 ms, D 200 ms, S 50 % ; quantité 30 % | ms | idem [DOC-2] |
| Pitch d'attaque (le « rave ») | ENV 3 → CRS de A/B, **+8 st** (hoover Alpha Juno, MusicRadar) ou **−5 à −12 st balayant vers la note en 200–600 ms** (amen) ; unipolaire, decay 60–200 ms [HEUR pour la durée] ; alternative : PORTA 60–120 ms, **SCALED** on, LEGATO on, avec des notes qui se chevauchent | st / ms | MusicRadar hoover via dotbeat [DOC-2] ; amen recipes [DOC-2] |
| Pitch bend | GLOBAL Pitch bend UP **12** : « bend qui monte depuis l'octave inférieure vers chaque phrase » (Monosounds, variante eurodance) | st | Monosounds [DOC] |
| Vibrato | LFO 1 → FINE, **7 Hz**, DELAY 200 ms, RISE 200 ms | Hz / ms | `leads-nappes-textures.md` [DOC] |
| Voicing | MONO ou LEGATO ; « less width, more mono punch » | | Monosounds [DOC] |
| Phase | RAND 100 % (supersaw JP-8000 : phase aléatoire par note, sinon annulation) | % | Szabo via `leads-nappes-textures.md` [DOC] |

**Chaîne d'effets (Serum 2, dans l'ordre).** Distortion Tube ou Soft Clip léger (« light clip-style distortion for aggression », Syntorial) → Compressor MULTIBAND (« light OTT » pour la future rave, Monosounds ; profondeur = MIX **15–25 %**, `patches-genres.md` §6) → **un seul** élargisseur : Hyper/Dimension (Hyper UNISON 0 → Dimension seul, SIZE 0, MIX ~30 % comme le Dimension Expander du Garage Bass d'Attack) ou Chorus → Reverb sur **BUS 1** (pas en insert), HI CUT 8 kHz, LO CUT 500 Hz (Myloops : send band-limité HPF 500 / LPF 8 kHz, départ −12 dB), Delay 1/4 ping-pong feedback 30–40 % sur BUS 2 (départ −15 dB). Hors Serum : **coupe-bas 100–150 Hz 12–24 dB/oct sur toute la pile** (Monosounds) ; EQ soustractive Monosounds : −2/−3 dB à 500 Hz, −2 dB à 1,5 kHz, −2/−3 dB à 3,5 kHz, shelf −1/−2 dB au-dessus de 12 kHz ; **sub séparé** (sinus mono, unison 1, fondamentale seule) ; sidechain 2:1–3:1, attaque 5–10 ms, release 100–150 ms, 2–3 dB de réduction (Myloops) ou, pour l'effet de pompage du genre, ratio 8:1–10:1 release 100–150 ms (Fearvox). Vérification mono obligatoire : « une chute de 6 dB en mono = width et chorus qui s'annulent ; resserrer d'abord la couche grave ».

**Variantes.** *Hoover pur (« Dominator », MusicRadar / ReDominator)* : 3 oscillateurs Pulse-Saw PWM, OSC 1/2 **±40 cents** opposés, OSC 3 **−12 st**, PWM à fond avec rate rapide (~100 sur l'échelle ReDominator), enveloppe de pitch au maximum (≈ 1 octave), VCA partiellement contrôlé (Amount 30) pour garder un côté drone, chorus rate ~60, saturation + HPF ensuite [DOC-2]. En Serum 2 : WARP 1 = **PWM** sur une carrée avec LFO 5 Hz (amen : « PWM LFO ~5 Hz, moderate depth ») ; filtre LP 4–6 kHz, amp A 0–10 ms R 200 ms ; **chorus lourd → phaser → reverb** (« les deux parties non négociables : le balayage de pitch descendant et le chorus »). *Big room / anthem (Monosounds)* : unison 7 sur les deux saws, detune 0,12, couche +12 large, longue reverb sur son propre bus, gros sidechain. *Eurodance* : unison 7, detune 0,14+, filtre ouvert, release courte, pitch bend depuis l'octave inférieure. *Supersaw JP-8000 fidèle* (`leads-nappes-textures.md`) : 7 voix, à mi-course du bouton **≈ ±18 cents**, à fond ≈ ±2 st, voix centrale ~2,5 dB sous les latérales à mix maximum — dans Serum 2, Tuning **Super** [HEUR : nom qui suggère la courbe JP] et BLEND ≈ 75 % (Szabo mesure l'égalisation des amplitudes à mix 0,75 ; le défaut de Serum est 75 %, coïncidence à tester).

**Erreurs fréquentes.** Detune et blend au maximum (« le centre est la note ; plus de centre = brouillard ») ; unison 16 (« au-delà de 7, on paie du CPU, pas de la taille ») ; même width sur toutes les couches ; demander le grave à la pile de saws (en dessous de 150 Hz les voix battent : sub séparé) ; enveloppe de release longue sur l'ampli (la queue appartient aux sends) ; phase fixe (transitoire identique à chaque note) ; vibrato dès l'attaque.

**Sources.** Monosounds *Serum 2 Supersaw Guide* (`corpus/cuivres/monosounds-studio-serum-2-supersaw.md`) [DOC] ; dotbeat `priors/leads.md` (Syntorial, FaderPro, Myloops, MusicRadar hoover ×2, CMUSE) et `recipes-reference.md` [DOC-2] ; amen `08-sound-design-recipes.md`, `14-iconic-patch-recipes.md` [DOC-2] ; `leads-nappes-textures.md` (Szabo) [DOC] ; packs et cours future rave [DOC-EXTRAIT].

## FR-2 — Plucks et arpèges

**Cible.** Pluck court, brillant à l'attaque, sombre ensuite ; arpège 1/16 ou 1/8 qui bouge par polymètre.

**Moteur.** Serum 2 (ENV 2 → CUTOFF, ENV 3 → CRS pour le transitoire, ARP intégré) ; Operator pour un pluck FM (`leads-nappes-textures.md` : ratio 2 = bois, 3,51 = verre).

| Étage | Réglage | Source |
|---|---|---|
| OSC A | saw ou table Digital ; UNISON **3–4**, DETUNE **0,08–0,18** (« les plucks ont besoin de moins d'unison que les leads ») | Cymatics / Ghost Production [DOC-EXTRAIT] |
| Patch Serum publié | OSC A **Dist 8Bit Fwap** unison 4 detune 0,10 ; OSC B **CrushWub** unison 3 detune 0,16 ; LFO 1 → CUTOFF rate **1/8 TRIP**, SMOOTH 50 ; LFO 2 → WT POS 1/2 ; LFO 3 → LEVEL (sidechain interne) ; ENV 2 → Wet de la reverb | Attack *Beat-Pulsing Plucks*, `patches-genres.md` §3 [DOC] |
| ENV 1 (ampli) | A **1–4 ms**, D **160–260 ms**, S 0, R **80–140 ms** | Cymatics [DOC-EXTRAIT] |
| ENV 1, idiome mesuré | A 3,9 ms, S 0,01, **D 867 ms**, R 643 ms (234 patchs pluck : « attaque instantanée, sustain zéro, decay/release longs font tout ») ; IQR decay 250–1282 ms | dotbeat research 141 via `recipes-reference.md` [DOC-2] |
| ENV 2 → CUTOFF | ouvre de **30–50 %** et referme en **100–250 ms** ; enveloppe de filtre **plus rapide que l'ampli** (60–70 % du decay d'ampli, `leads-nappes-textures.md`) | Monosounds plucks [DOC-EXTRAIT] ; [DOC] |
| Filtre de repos | LP 24 dB, 600–800 Hz, pic 3–4 kHz ; RES 20–40 (« filter env 6 kHz → 800 Hz in 80–150 ms, res 20–40 % », pluck trance) | amen recipes [DOC-2] |
| Transitoire | ENV 3 → CRS, **unipolaire**, decay ≈ 20 ms (1/32 ou 1/64 en mode BPM) « pour un transitoire supplémentaire » | Cymatics [DOC-EXTRAIT] |
| Pluck Zebra 3 (ms complets) | env. filtre A **0**, D **1250 ms**, S 31, R **96 ms**, quantité 105 ; env. 2 → overdrive A **40 ms** (le grain arrive derrière le transitoire) ; TZFM ratio 1:2,5, feedback 73 | Attack Zebra 3 via dotbeat [DOC-2] |
| Sous-couche pluck (renfort de hook) | passe-bande **1–3 kHz**, A 0, D **200–300 ms**, S 0, **12–15 dB** sous le lead | Myloops [DOC-2] |

**Arpèges.** Attack *Complex Arps* : arp 1 rate **3/8**, 7 pas, octave 3 ; arp 2 transposé **+12**, octave 1,5, offset 2 pas, rythme 5 pas, **gate ×0,5**, random 35 % ; Soundbox 1/16, **swing 57 %**, **12 pas** contre une grille de 16 — le polymètre 7/5/12 fait le mouvement [DOC-2]. Serum 2 : ARP interne (12 slots, `serum2-fx-clip-arp.md`) ; delay **1/8 pointé** ping-pong feedback 40 % (amen), reverb courte.

**Erreurs.** Decay de filtre égal au decay d'ampli (le pluck « fade » au lieu de « frapper ») ; unison de lead sur un pluck ; oublier le HPF (Attack : coupe-bas sur la reverb du pluck).

## FR-3 — La basse future rave (offbeat / rolling)

**Cible.** Deux rôles à la fois : le **sub** tient la fondamentale, une **basse mid saw filtrée** (la « supersaw déguisée en basse » de FR-1, jouée une ou deux octaves plus bas) fait l'offbeat ou le roulement. Cours Sonic Academy (Protoculture) : kick Kick 2 + sub d'abord [DOC-EXTRAIT].

**Moteur.** Serum 2, une instance : OSC A saw (mid, → FILTER 1), SUB sinus (routé **Direct** : contourne filtre et FX, reste propre — `serum2-cartographie.md` §5). Natif : Wavetable « ANNA » (`patches-genres.md` §4 : 132 BPM, mono glide 25 ms, Logue Saw −12, LP MS2 24 dB drive 6,4 dB, ENV 3 A 0,18 ms D 4 s S 40 % R 600 ms) ou Analog.

| Étage | Réglage | Source |
|---|---|---|
| Sub | sinus, mono, unison 1, sans detune ; ENV A **4 ms** D 300 ms S 95 % R **30 ms** ; LP 90 Hz ; **−6 dB** | dotbeat `rolling-sub-bass` [DOC-2] ; `basses.md` [DOC] |
| Mid | saw + carrée (osc2 8 cents, niveau 0,35), **+12 st** au-dessus du sub ; CUTOFF **350 Hz**, res ≈ 1,2 (échelle dotbeat) ; ENV A 4 ms D **120 ms** S 35 % R 30 ms ; env. filtre → cutoff 55 %, A 2 ms, D **90 ms**, S 0 ; saturation « warm » drive 0,35 mix 0,35 ; **HPF 65 Hz / LPF 350 Hz** ; −9 dB | dotbeat `rolling-sub-bass` d'après Attack *Warehouse Rolling Techno Bass* [DOC-2] |
| Version future rave | même mid, filtre parqué à **600 Hz** balayé 400–900 Hz, unison 5 detune 0,09, mono | Monosounds [DOC] |
| Rythme | offbeat 8ths : notes courtes **60–120 ms** (amen) ; rolling 16ths : **laisser vide le premier 16e de chaque temps** (Attack Warehouse) ; vélocités 0,95 / 0,78 / 0,6 selon la position ; legato pour les 16es | amen `03-bassline-cookbook.md`, dotbeat [DOC-2] |
| Sidechain | attaque la plus rapide possible, hold 20–50 ms, release **1/16 ou 1/8** (117 / 234 ms à 128 BPM), profondeur 3–10 dB (subtil) ou 10–20 dB (pompage) | amen `09-bass.md` [DOC-2] |
| Sidechain « bass house » | seuil −20 dB, **6:1**, attaque 0,5–1 ms, release 150–200 ms (standard) ; −25/−30 dB, **8:1–10:1**, 0,1–0,5 ms, 100–150 ms (dur) | Fearvox [DOC-2] |

**Chaîne.** Saturation (Serum Distortion Tube ou Ableton Saturator Analog Clip, gain-match ensuite) → EQ (−3 dB max vers 200 Hz, rien de plus) → Erosion optionnel → sidechain → EQ finale (ryansavoia, « chaîne combinée de tous les tutoriels ») [DOC-2]. Utility MONO BASS 100–120 Hz.

**Erreurs.** Release d'ampli par défaut trop longue (« 600 ms dans Wavetable : les notes se fondent ») ; polyphonie ; sub stéréo ; pas de vélocité → cutoff.

## FR-4 — Kick long et « toms » de rave

**Cible.** Un kick de techno-house long et accordé (le genre est « techno pitched-up ») et des toms accordés en fills et en hook.

**Moteur.** Échantillon + couches (Drum Rack), ou synthèse : Serum 2 (OSC A sinus, ENV → CRS ; NOISE one-shot pour le clic), Operator, Ableton Kick (Drum Synths), Kick 2 (cité par le cours Protoculture [DOC-EXTRAIT]).

| Élément | Réglage | Source |
|---|---|---|
| Kick house / techno | sinus **50–60 Hz**, decay **300–500 ms** (house, clic doux) ; **55–65 Hz, 400–700 ms**, distordu, long (techno) ; pitch 150 → 50 Hz en 30 ms ; couche punch 80–120 Hz decay 80–150 ms ; clic 2–6 kHz decay 5–15 ms | amen recipes [DOC-2] |
| Kick 909 | sinus **220 → 55 Hz en 15–30 ms**, decay 200–400 ms, clic 2–5 ms à 2–4 kHz, soft clip ; EQ +50–60 Hz, −200–400 Hz, +2–4 kHz | amen drum-machines [DOC-2] (⚠ contredit `percussions.md` : pitch env 909 « 200–500 ms », voir §5) |
| Sub kick synthétisé (Massive) | sinus **−36 st**, env. pitch quantité **60**, decay du pitch juste après 1/4 de course ; ampli A 0, decay ≈ 1/3 ; Classic Tube dry/wet 45–50 % drive 25–30 % ; EQ externe : HP 20 Hz, **boosts 40 et 80 Hz**, creux étroits **127, 167, 209, 564, 750, 940 Hz** | Attack *Slave to the Rhythm* via dotbeat drums [DOC-2] |
| Kick 3 couches (Ableton, Attack) | sub accordé **C1** : A 3,97 ms, decay 60 s, S −inf, R **698 ms** ; transitoire HPF **271 Hz**, A 0, D 347 ms, R 50 ms, −1,5 dB ; hat en couche HPF **2,52 kHz**, D 66 ms, −1,2 dB | idem [DOC-2] |
| Kick long, choix de durée | à 126 BPM une noire = 476 ms : un kick de 250–350 ms laisse respirer la basse, un kick de **800 ms** remplit la mesure et interdit un sub actif | `percussions.md` [DOC] |
| Tom 808 | sinus une ou deux octaves au-dessus du kick, chute de pitch sur **60 ms**, decay **300–600 ms** | amen drum-machines [DOC-2] |
| Tom 909 | **deux triangles à la quinte (7 st)**, enveloppe de pitch 100–200 ms | `percussions.md` [DOC] |
| Tom Simmons (« pew » 80s) | triangle ou sinus, pitch qui descend sur **200–400 ms**, mélangé à du bruit, passe-bas résonant, clic au début | amen [DOC-2] |
| Toms synthétiques, règle | triangles, seuls ou empilés en octaves ; enveloppe de pitch qui « bend » le début ; **ampli plus long que le kick** ; **creuser le grave** pour que ça lise « tom » et non « kick » | MusicRadar *9 ways* [DOC-EXTRAIT] |

**« Toms de rave » [HEUR].** Aucune source ne définit le tom future rave. Logique : c'est le tom 909/Simmons accordé sur la tonique ou la quinte (comme un kick, `percussions.md` §2 : Sol1 = 49,5 Hz natif 808 ; règle Deruty : rester ≥ Mi1 41,2 Hz), decay 300–600 ms, joué en fills de 16es sur le dernier temps de 8 mesures (ryansavoia « PUNKS » P4/P8 : « end punks with a tom hit »), avec pitch env +12 st sur 50–100 ms et une saturation qui donne les harmoniques (Deruty : un son à 5 partiels perd 4,5 dB au lieu de 11,8 dB quand on le descend). En Serum 2 : OSC A sinus, Pitch track **on**, ENV 2 → CRS +12…+24 st decay 40–100 ms, NOISE one-shot decay 5 ms pour le clic, Distortion Tube, Utility MONO BASS.

**Accord et alignement.** Accorder le kick **en dernier, contre la basse** (Attack Deep Tech House) ; kick Dirty Tech House : 3 couches convergeant sur la même classe de hauteur (bass drum −2 st, sub 808 +2 st, kick de syncope +1 octave), chaîne EQ → Saturn multibande → EQ ; polarité : « si les formes d'onde partent dans le même sens, c'est bon » ; **5 ms à 100 Hz = demi-longueur d'onde = annulation complète** (`percussions.md`) ; corrélation +1 visée dans 30–80 Hz. Clipper dur sur le kick à 0 dB et sur le groupe kick + clap (ryansavoia, Max Styler) ; kick sub ≥ −6 dB au spectre, **kick plus fort que la basse dans le sub** ; « le sub doit être aussi fort ou plus fort que l'harmonique » (John Summit's engineer : si 96 Hz > 45 Hz, la puissance manque) [DOC-2].

## FR-5 — Chords sombres

**Cible.** Accords mineurs ou sus courts et sombres, souvent joués par la même pile de saws que FR-1, filtrés bas, sidechainés.

**Moteur.** Serum 2 (pile FR-1, POLY 3–4) ; Wavetable ; Analog.

| Étage | Réglage | Source |
|---|---|---|
| Pile | OSC A saw unison 5–7 detune 0,10–0,12 + OSC B −1 oct ; « supersaw : 3 notes maximum, un accord de 5 notes = 35 saws de boue » | Monosounds [DOC] ; amen [DOC-2] |
| Filtre | LP parqué **500–900 Hz** (Monosounds future rave) ; automation « depuis **50 Hz** montant lentement sur chaque phrase de 4 mesures » (pads techno, Attack) | [DOC] ; [DOC-2] |
| Enveloppe stab | A **5 ms**, D **250 ms**, S 0, R **31 ms** ; env. filtre A 3 ms D 160 ms S 0, quantité 0,8 ; vélocité → filtre 0,35 ; couche corps **−12 st** à −14 dB (78,6 % des patchs « Chords » de Surge sont scindés à l'octave) | dotbeat `house-chord-stab` [DOC-2] |
| Enveloppe pad | A **0,54 s** (médiane de 406 pads ; prose : 1–3 s), D 0,8 s, S 0,9, R **1,8 s** ; osc2 triangle −18 cents, 5 voix, cutoff 2,2 kHz, env. filtre A 0,6 s D 1,2 s ; LFO **1 mesure** → cutoff 0,3 | dotbeat `warm-pad-with-air` [DOC-2] |
| Pad désaccordé (Sylenth1) | A1 5 voix −1 oct detune 4,05, A2 7 voix saw detune 3, amp A 3 s R 7 s, LP ≈ 800 Hz, chorus **16 ms / 0,22 Hz / depth 50 % / mix 60 %**, reverb 30 %, LFO 2 → volume 1/4 (sidechain interne) | Attack *Detuned Pad*, `leads-nappes-textures.md` [DOC] |
| Voicing | m7 / m9 / sus4, jamais de triades nues ; **sans la fondamentale** (la basse la tient, règle Kerri Chandler) ; 3e renversement (7e en bas) ; registre MIDI 55–75 | amen house, Attack Passing Notes via dotbeat [DOC-2] |
| Mouvement | swell d'Expression (CC) de ~50 % au max dans chaque changement d'accord (deux recettes Attack) ; pan modulé par **deux LFO sommés** ; trois vitesses (13 Hz / 0,5 Hz / 12–15 s) | dotbeat chords-pads [DOC-2] ; `leads-nappes-textures.md` [DOC] |

**Chaîne.** HPF 200–300 Hz, creux 400–600 Hz (ryansavoia) ; chorus **puis** reverb (« chaîne de finition par défaut des pads », 5 recettes) ; reverb en send 1,5–3 s, pre-delay 20–40 ms, 25–40 % ; sidechain (Fearvox : les pads pompent aussi) ; compression parallèle −32 dB, 8:1, 4 ms / 120 ms, mix 0,35 (dotbeat). OTT : « multiband upward compression 30–60 % rend les accords denses et finis » (amen future bass) — pour la future rave, rester à 15–25 % [HEUR : le grave doit laisser passer le kick].

**Erreurs.** Cinq notes sur une supersaw ; fondamentale dans l'accord ; largeur identique au lead (« un seul élément large à la fois », `leads-nappes-textures.md`) ; reverb en insert sur un patch polyphonique modulé par enveloppe (fiche 35).

## FR-6 — Risers

| Étage | Réglage | Source |
|---|---|---|
| Patch Serum chiffré | OSC A = **Noise White 100 %**, unison 4, detune 12 cents ; OSC B sinus −1 oct avec **FM 30 % depuis A** ; filtre **Comb 100 % wet, RES 60 %**, CUTOFF automatisé **100 Hz → 12 kHz sur 4 mesures** ; ENV A 0 D 1,2 s S 0 R 0 ; LFO **1/8**, depth 70 %, triangle → cutoff et pan | Brown Noise Radio / SoundBridge [DOC-EXTRAIT] |
| Version simple | bruit blanc, passe-haut ou passe-bande **200 Hz → 8 kHz** (courbe exponentielle), résonance moyenne à forte (30 %, `leads-nappes-textures.md`), volume −∞ → 0 dB sur **8 mesures**, pitch +1 octave sur les 4 dernières (option), pas de pitch synchronisés 1/8 ou 1/16 (« stepped riser ») | amen transitions, Fearvox [DOC-2] |
| Durée | 4 mesures (transition courte) ; **8 ou 16** pour un drop | unison.audio [DOC-EXTRAIT] ; amen : build 16 mesures en big room |
| Riser tonal | saw ou carrée montant **1–3 octaves**, LP qui s'ouvre, vibrato croissant, finir sur une note **hors** de l'accord du drop (demi-ton sous la tonique) | amen [DOC-2] |
| Shepard | 4–6 copies à l'octave, volume en cloche | amen [DOC-2] |
| Filtre de bus | LP 300–500 Hz → 16 kHz sur les 8 mesures avant le drop, res 10–15 % ; HP du mix 20 → 400–800 Hz sur les 4 dernières mesures (la basse disparaît) | Fearvox ; amen drop [DOC-2] |
| Fin | **coupure nette au temps 1** ; reverb « cut dead at the drop » ; dernier temps vide ; queue de reverb du build ne doit pas baver sur la mesure 1 | `leads-nappes-textures.md` fiche 28 [DOC] ; amen [DOC-2] |

Serum 2 : NOISE (White) + FILTER 1 type Comb ou Band 24 ; ENV en mode **BPM** (A = 8 bars) ; LFO Mode **Env** pour un balayage one-shot ; Reverb sur BUS. Empiler **3–5** dispositifs (roll de snare 1/8 → 1/16 → 1/32 → 1/64, riser, HP du mix, reverb send, crowd) et couper tout sur le dernier temps (amen).

## FR-7 — Voix pitchée

**Cible.** Voix courte pitchée (hook « rave »), chops de syllabes, riser vocal.

**Moteur.** Simpler (mode Slicing, Transient / Beat / Region / Manual ; C1 = slice 1), Sampler (formant-preserving), clip audio en **Complex Pro, Formants 100 %** ; Serum 2 moteurs Sample / Multisample / Granular (Pitch track), warps spectraux (`kVocode_NOISE`, `kSpectralPitchShift`).

| Étage | Réglage | Source |
|---|---|---|
| Amplitude du pitch | au-delà de **3–4 demi-tons** sans préservation de formants : artefact audible ; UKG : voix montées de **2–5 st** ; G-house : descendues de **2–4 st** | The Vocal Market [DOC-EXTRAIT] ; amen UKG, JefroB bass house [DOC-2] |
| Stratégies Attack | A : pitcher **avant** de découper (le timing change, pour de longues phrases) ; B : garder la hauteur des slices et transposer l'accompagnement (syllabes) ; exemple 125 BPM sur une voix à 80 BPM | Attack *Vocal Chopping & Pitching* via dotbeat [DOC-2] |
| Riser vocal | délier pitch et timbre ; pas de pitch alignés sur le chop (−quinte, +quinte, retour sur les mesures 2–4) puis montée continue ; delay **1/4, feedback 30 %** (les répétitions héritent du pitch) ; second pitch-shifter descendant sur la queue de reverb | Attack *Creative Vocal Pitch Processing* [DOC-2] |
| Chaîne voix | doubler 65 % (Vocal Doubler) ; EQ **+2 kHz**, **−300 Hz**, coupe dure < 100 Hz ; multibande 3 bandes (< 120 / 120–650 / > 650 Hz) ; compresseur genou large ratio infini puis glue 5 dB ; clipper ; 2 limiteurs ~1 dB ; couche grave dupliquée **−5 st** + auto-pan + chorus | ryansavoia (Max Styler) [DOC-2] |
| Espace | reverb room sur les drops, grande sur les breaks ; delay 1/8 pointé ; lo-cut de la reverb 200–300 Hz | ryansavoia, Fearvox [DOC-2] |

**Erreurs.** Pitcher > 4 st en Re-Pitch (chipmunk) ; formant non préservé ; chop long dans un drop (« call » non résolu = tension, « response » = payoff en fin de 8 mesures).

---

# 2. Bass house

## BH-1 — Sub

| Étage | Réglage | Source |
|---|---|---|
| Source | sinus (ou triangle pour le layering), **mono, unison 1, sans detune, sans chorus** ; un seul oscillateur tient le fondamental | SOS via `basses.md` [DOC] |
| Serum 2 | SUB osc ou OSC A Basic Shapes pos. 0 ; routage **Direct** pour éviter filtre et FX ; MONO ; Utility MONO BASS 100–120 Hz | `serum2-cartographie.md` [DOC] |
| Enveloppe | A **4 ms**, D 300 ms, S 95 %, R **30 ms** ; ou A 3–8 ms, R 20–30 ms (SOS) ; attaque 0 ms = clic (amen : 1–5 ms ou phase 0) | dotbeat, `basses.md`, amen [DOC/DOC-2] |
| Operator natif | Osc A sinus, Coarse **0,5** (une octave sous la note), Ae Sustain 1, Release 200–400 ms, filtre off, mono | ryansavoia [DOC-2] |
| Drift natif | sinus ou triangle, oct −1, filtre MS2, LP 0,15–0,30, Env 1 sustain 0,7–1, Spread 0 % | ryansavoia [DOC-2] |
| Registre | MIDI **28–40** (Mi1–Mi2, 41–82 Hz) ; F1 = 43,65 Hz ok, sous Mi1 41,2 Hz « les enceintes lâchent » (Storch/Deruty) | amen `09-bass.md` [DOC-2] ; `percussions.md` [DOC] |
| Niveau | sub ≥ harmonique ; fondamentale de basse −6 à −12 dB au spectre, kick sub ≥ −6 dB, kick > basse dans le sub | ryansavoia [DOC-2] |
| Glide | 40–80 ms discret ; 80–120 ms (808) ; 300 ms = 1,26 croche à 126 BPM, intransposable | `basses.md`, unison.audio via dotbeat [DOC/DOC-2] |
| Coupe-bas | 20–30 Hz (24 dB/oct) | `basses.md`, unison.audio [DOC/DOC-2] |

**Sidechain.** 5:1, attaque **4 ms** (« la valeur qui évite le clic »), release 60 ms (EDMProd) ; ou 4:1, 5–10 ms, 70–110 ms (unison.audio) ; multibande : ne ducker que sous 100–200 Hz. **Qui tient le grave** (contradiction Preset Drive / EDMProd, `patches-genres.md` §5) : décider explicitement ; en bass house le growl est coupé-bas à 100 Hz et le sub porte le fondamental [HEUR cohérent avec fiche 37].

## BH-2 — Basse métallique FM (« Jauz bass », future house)

**Cible.** Le mid-bass métallique et élastique du genre (« metallic, punchy, aggressive : JAUZ, JOYRYDE, Ephwurd », Fearvox). Recherche « Jauz bass Serum » : uniquement des vidéos (Shark Attack stab, Eptic/Jauz growl, « JAUZ/Donk bass ») [DOC-EXTRAIT]. Deux recettes écrites existent, plus l'ancêtre.

**Moteur.** Serum 2 : OSC A porteuse, **WARP 1 = FM from OSC** (OSC B modulateur, niveau de B à zéro autorisé), mode d'accordage **Ratio** sur B ; dual warp FM + distorsion sur la même table (`serum2-cartographie.md` §4.2). Operator : FM Drive comme cible de modulation (fiche 39).

| Étage | Réglage | Source |
|---|---|---|
| Ancêtre chiffré (Garage Bass, Massive) | porteuse sinus **−24**, second sinus −12 (≈ 14 h), modulateur PM **−12** (ratio **2:1**) ; variante **−12,30** = le métallique (battement inharmonique) ; PM ≈ 45 % + 60 % par enveloppe ; filtre Daft cutoff **25 %** res 0, env. de filtre à fond, sustain 0 ; amp R 33 % ; mono, glide 10–15 % ; Classic Tube ~10 h, Dimension Expander size 0 ~10 h | Attack via `patches-genres.md` §2 [DOC] |
| EDMProd bass house | sinus, **FM depuis OSC B** (routage A>B), modulateur monté « de 2 octaves et 7 demi-tons » = ratio **6:1** [CALC] ; LFO en mode Env sur le cutoff ; LFO 2 → quantité de FM (« ne pas exagérer, ça distord vite ») ; ADSR : sustain baissé, release montée (« plucky ») ; post : OTT, EQ, distorsion, sidechain, largeur ; drop 1B : moduler l'octave du sinus qui fait la FM | EDMProd [DOC-EXTRAIT] + `basses.md` [DOC] |
| FM bass communautaire (Serum) | OSC A sinus ← FM de B ; OSC B sinus avec **env. de pitch +5 st → 0 en 200 ms** ; LP 24 dB cutoff **3 kHz**, env. decay 300 ms ; Distortion Tube drive 2–4 (/10), mix 30–50 % | Fearvox [DOC-2, communautaire] |
| « Thwack » d'attaque | env. de pitch **+12 st → 0 en 50 ms** sur la basse (Subtronics) ; env. 3 → pitch quantité 24, decay court (Attack Techno Reese Massive X) | DUBFORGE, dotbeat basseries [DOC-2] |
| Ratios FM | entiers (2:1, 3:1, 6:1) = harmonique/creux ; **1:3 métallique, 2:5 inharmonique, 3:7 complexe** (Subtronics) ; cloche = non entier ≥ 4–5 + enveloppe rapide sur le modulateur seul | DUBFORGE [DOC-2] ; `patches-genres.md` [DOC] |
| Index (quantité de WARP FM) | **non chiffré par les sources** ; 15–25 % = râle, > 40 % = hurlant (`basses.md`, growls) ; piloter par ENV 2 (decay 150–300 ms) et par une macro | [DOC] / [HEUR] |
| Filtre | MG Low 24, CUTOFF 25 % (~140–200 Hz sur la course log [HEUR]) piloté à fond par ENV 2 sustain 0 (Garage Bass) ; ou 3 kHz décroissant en 300 ms (Fearvox) | [DOC] / [DOC-2] |

**Chaîne.** Distortion Tube (léger) → Compressor MULTIBAND (MIX 15–25 %) → EQ : coupe-bas **100 Hz** sur ce growl (fiche 37), boue −3 dB 200–300 Hz → Hyper/Dimension discret → sidechain. Sub sinus séparé sous 100–120 Hz. Metallique de Jauz [HEUR] : FINE du modulateur +20…+40 cents (la variante −12,30 d'Attack), ou Ratio non entier 2,5–3,5, résonance de filtre modérée et **Warp 2 = Distortion Diode** sur la porteuse.

**Erreurs.** Chercher le métal dans un ratio non entier alors que l'original est entier + désaccord de 30 cents (fiche 36) ; laisser le growl pleine bande (fiche 37) ; oublier le mode Trigger des LFO (fiche 3) ; recettes calées sur 140–150 BPM (fiche 4).

## BH-3 — Talking bass (formant / vowel)

**Moteur.** Serum 2 : FILTER 1 type **Formant I / II / III** (« le cutoff morphe entre voyelles », VAR = FORMNT décalage), FILTER 2 MG Low 24 en série pour la brillance ; ou deux filtres Band 12 aux fréquences F1/F2 ; préset d'usine de départ **« Vox/VOX - I Talk.SerumPreset »** (utilisé tel quel comme base « Formant_Vowel » par DUBFORGE) [DOC-2]. Natif : Wavetable filtre Formant ? (non vérifié) ; Auto Filter n'a pas de formant → Vocoder d'Ableton avec bruit en porteuse (`leads-nappes-textures.md`).

| Voyelle | F1 / F2 (Hz) — amen | F1 / F2 (Hz) — DUBFORGE, « centres adaptés à la basse » |
|---|---|---|
| ee / I | 270 / 2290 | 390 / 1990 |
| eh / E | 530 / 1840 | 660 / 1720 |
| ah / A | **730 / 1090** | 730 / 1090 |
| oh / O | **570 / 840** | 570 / 840 |
| oo / U | 300 / 870 | 440 / 1020 |

3e formant fixe **2500–3000 Hz** « pour le réalisme » (amen). Morph A→E→I→O→U sur **2–4 mesures** (DUBFORGE) ou entre deux voyelles sur 1–2 mesures (amen) ; « de oh à ah c'est un tout petit mouvement de bouton ; balayer toute la course donne une démo de filtre, pas une voix » ; trouver deux positions utiles, moduler lentement entre elles, sans delay d'abord (Monosounds/EDMProd) [DOC-EXTRAIT]. Résonance **20–40 %** pour que les voyelles restent définies, LFO ou enveloppe **de petite plage** sur le cutoff (`basses.md`) ; combiner avec un LFO de cutoff rythmique (1/8, Mode Trig) pour le « parler » (DUBFORGE). Source : saw, growl, ou wavetable de voix (Serum : « custom wavetables from vocals — the formants survive », amen software-instruments).

**Chaîne.** Splitter L/M/H : < 120 Hz propre, 120 Hz – 2 kHz waveshaping lourd (tanh + hard clip), > 2 kHz tube ; OTT ; sub séparé (DUBFORGE) [DOC-2].

## BH-4 — Wobble LFO

| Étage | Réglage | Source |
|---|---|---|
| Recette MusicRadar (dials) | Osc 1 « 2Pulse » PD 25 ; Osc 2 carrée + 2Pulse PD 52, **+19 st**, volume 25 ; filtre LP6 cutoff 45 res 17 ; LFO **1/8 triolet**, triangle, **onset delay 48** (« nécessaire pour l'effet dubstep classique : le wobble entre en fondu ») ; profondeur sur le cutoff : LFO 40, env. 2 **130** (l'enveloppe fait plus que le LFO) ; env. 2 (snappy) A 0, delay 34, S 0, R 17 | dotbeat basseries #8 [DOC-2] |
| SOS Dubstep Secrets (ES2) | filtres en série, filtre 2 LP 24 dB, LFO 2 → cutoff 2 au maximum, rate **1/8** synchro ; amp **release 570 ms** (« les notes sonnent un moment ») ; mono ; sub : osc 1 −24 + osc 2 −12 avec FM « 3 h », plage C2–C3 | dotbeat basseries #7 [DOC-2] |
| Générique | saw ou wavetable ; LP 24 dB, RES **30–60 %** ; LFO synchro 1/4, 1/8, 1/8T, 1/16, 1/32 ; formes : sinus (lisse), saw descendant (rythmique), carrée (gate) ; **changer le rate toutes les 1–2 mesures : c'est la composition** ; sub sinus séparé | amen recipes / dubstep [DOC-2] |
| Bass house | couches sub (sinus 30–60 Hz) + mid (wobble 80–500 Hz, HPF 80 Hz) + top (500 Hz–3 kHz) ; rates 1/4, 1/8, triolet | JefroB bass house [DOC] |
| Tempo | à 126–128 BPM, 1/2 = 952 ms (trop lent) : viser 1/4 (476 ms) ou 1/8 (238 ms) ; 1/8T = 159 ms | `basses.md` fiche 4 [DOC] |

Serum 2 : LFO 1 Mode **Trig** (fiche 3 : sans Trig chaque note attrape le wobble à une phase différente), RATE 1/8, TRIP au besoin, SMOOTH 20–50, **DELAY / RISE** pour l'onset (équivalent du « delay 48 »), ANCHOR pour rester calé à la mesure ; MATRIX LFO 1 → CUTOFF quantité 40 % + ENV 2 → CUTOFF 60–100 % [HEUR : transposition des proportions 40/130]. Distorsion **après** le filtre pour éclaircir (« distortion here brightens/sharpens », MusicRadar) ; « compress to impress ».

## BH-5 — Reese (Matroda, Tchami en bass house)

| Étage | Consensus / valeurs | Source |
|---|---|---|
| Structure | 2 saws (ou 2 sinus) désaccordées, **mono/legato**, LP ; sub sinus **séparé, mono, non désaccordé** ; le detune est un **réglage de vitesse de battement** qui dépend aussi de la note jouée | `basses.md`, dotbeat basseries consensus 1–4 [DOC/DOC-2] |
| Detune | ±27 cents (Attack, sinus) ; ±30 (NI) ; ±55–61 (MusicRadar « Terrorist », 61 = battement calé au BPM) ; −30/+50 asymétrique (Noise Masters) ; ±7 sur un sub séparé (Twin 3) ; 5–10 subtil / 25–50 neuro (Dystopian) ; **médiane mesurée 16,6 cents** (494 patchs basse ≥ 5 voix ; ±61 = 97e centile) → dotbeat encode **17** | dotbeat `reese-bass` [DOC-2] |
| Filtre | LP 24 dB ; 650 Hz res 14 % (NI) ; 600 Hz « Metal » (Twin 3) ; 1–3 kHz res 20–40 % (Dystopian) ; ~4 kHz (MusicRadar) ; dotbeat encode **700 Hz**, res 2,5 (échelle dotbeat), LFO **1 mesure** depth 0,35 (« un Reese statique est un échec ») | [DOC-2] |
| Enveloppe | S 1,0, R **24 ms** (Attack) ; A 4 ms D 400 ms S 0,9 R 24 ms, env. filtre 0,2 D 0,3 S 0,4 (dotbeat) | [DOC-2] |
| Recette la plus complète (Twin 3, Attack « Fred Again ») | osc 1 sinus **−1 oct** 0 dB ; osc 2 saw **−7 cents −8 dB** ; osc 3 saw **+7 cents −8 dB** ; osc 4 saw sync 4,00 −12 dB ; mono, unison 64 voix spread 10 % ; filtre 1 LP **600 Hz** Metal ∥ filtre 2 low shelf 30 Hz ; XLFO 1/16 ; EG2 delay 1714 ms attack 3428 ms ; chorus 60 %, 0,005 Hz, depth 100 %, 30 ms ; Saturn **split 400 Hz** : bas Warm Tube 30 %, haut Warm Tape 65 % ; Pro-Q M/S ; Pro-C « Bass Control » +25 dB ; gain-stager à −14 dB **avant** de distordre | dotbeat basseries #5 [DOC-2] |
| Phase | **reset de phase à chaque note** (« turn phase randomization down », FutureProof ; « note-on reset », MusicRadar) → Serum : RAND 0 % | [DOC-2] |

**Serum 2.** OSC A saw, OSC B saw FINE +17 (ou A unison 2 voix, DETUNE réglé à l'oreille sur la note la plus grave — fiche 2) ; MONO + LEGATO, PORTA 30–60 ms ; FILTER 1 MG Low 24 700 Hz RES 25 ; LFO 1 → CUTOFF, 1 bar ; SUB sinus −1 oct routé **Direct** ; FX : Chorus (DELAY 1 30 ms, RATE ~0 Hz, DEPTH max, MIX 60 %) → Splitter L/H à 400 Hz avec Distortion Tube 30 % en bas et Tape Sat. 65 % en haut → Compressor → Utility MONO BASS 120 Hz. EQ hors Serum : creux étroit **1,6–3,8 kHz −6/−12 dB** (métal), boost large **450–800 Hz** (KVR) ; boost 100–200 Hz (Noise Masters).

**Erreurs.** Reese full-range en rôle de sub (structurellement incompatible, `basses.md`) ; phase libre ; detune réglé sur une note aiguë ; pas de mouvement.

## BH-6 — Growl

**Cible.** Growl bass house = **mid-bass** (coupe-bas ~100 Hz) sur sub séparé, avec un kick 4/4 (fiche 37). Habstrakt, Ghastly : « wavetable, passe-bande avec enveloppe » (Fearvox).

| Étage | Réglage | Source |
|---|---|---|
| Patch mesurable (BassGorilla) | Osc A warp Bend ± 6, Osc B 47 ; filtre **High Notch 12**, cutoff 141 Hz, res 49 ; LFO 1 → cutoff **−74** (inversé), rate 1/2, **mode Trigger** ; distorsion Diode 2 drive 20 ; flanger depth 30 feedback 64 ; pitch bend ±12 | `basses.md` §3 [DOC] |
| Growl Massive (rebuild) | osc 1 : table à forte variation spectrale, position modulée par LFO **20–80 Hz** ou stepper 1/16 ; osc 2 même table **12–20 cents**, position décalée ; sync ou ring mod entre eux ; LP résonant + LFO à pas synchronisé ; distorsion après le filtre ; resampler | amen software-instruments [DOC-2] |
| Générique | WT POS modulée par LFO **10–60 Hz** → distorsion → comb ou phaser → **resample** → repitch, filtre, distord → répéter 2–3 fois → sub propre | amen recipes [DOC-2] |
| Formants | res 20–40 %, warp Bend 30–50 % = nasal, FM 15–25 % = guttural, > 40 % = métallique/hurlant ; unison 1 pendant la conception | Monosounds via `basses.md` [DOC] |
| Traitement | Overdrive 40–60 %, phaser 1/2 feedback 60 % mix 50 %, EQ coupe-bas **120 Hz** et creux −3 dB 400 Hz, compresseur multibande 2–5 kHz | `basses.md` [DOC] |
| Multibande Subtronics | crossover **< 120 / 120–2 k / > 2 kHz** ; sub propre ou tape léger ; mid = **le growl** (tanh + hard clip) ; haut = tube ; puis OTT ; waveshaper en pile : soft clip → tanh → hard clip → tube (« plusieurs étages légers > un étage lourd ») ; OTT **30–50 %** par canal, 15–30 % sur bus ; **3–5 passes** de resampling minimum | DUBFORGE [DOC-2] |
| Presets d'usine Serum 2 de départ | Bass/Hard/**BA - Basilisk** (growl), Bass/Modulated/**MDL - Slippery Snake** (wobble), Bass/Hard/**BA - RM Wub Generator** (riddim), Bass/Reese/**BA - Gnarly Reese**, Lead/**LD - Das EDM** (screech FM) | DUBFORGE `serum2_preset.py` [DOC] |

**Serum 2.** LFO Mode **Trig** obligatoire ; rate transposé (1/2 à 140 BPM → 1/4–1/8 à 126, fiche 4) ; « Resample to Oscillator » (`basses.md`) ; Splitter L/M/H pour le multibande interne ; Compressor MULTIBAND. **Le rythme timbral d'un drop** : quatre gestes différents par cellule de 2 mesures, le vocabulaire se répète, pas la phrase (amen memory *a-timbre-figure-must-not-repeat-exactly*) [DOC-2].

## BH-7 — Basse « Chris Lake » (courte, filtrée, groove)

**Cible.** Pluck de basse court, sombre, avec **résonance** et vélocité → cutoff (« Reso Pluck (acid feel) : square + saw, HIGH resonance, env → cutoff — Chris Lake style », ryansavoia).

| Étage | Réglage | Source |
|---|---|---|
| Filtre | **MG Low 24**, ENV 2 lié au cutoff ; couper au-dessus de 200–300 Hz ou cutoff ≈ **140 Hz** | The Producer School [DOC-EXTRAIT] |
| ENV 1 (ampli) | decay ≈ **1,2 s**, sustain **−10 dB** | idem |
| ENV 2 (filtre) | plus courte que ENV 1 ; agressif : decay **200 ms**, sustain 0 ; → cutoff **5 %**, → résonance **10 %** (Mystic Alankar) | [DOC-EXTRAIT] |
| Vélocité | vélocité → cutoff avec **courbe raide** (seules les notes fortes ouvrent) ; « le secret du bounce, confirmé par 3+ tutoriels » | The Producer School ; ryansavoia [DOC-EXTRAIT/DOC-2] |
| Drive | **20–40 %** (Serum FILTER DRIVE) | The Producer School [DOC-EXTRAIT] |
| Oscillateurs | saw + sinus −1 oct (sub) ; ou carrée + saw, haute résonance | idem ; ryansavoia |
| Variante rolling (Chris Stussy, seconde main **non vérifiée**) | mono, glide 0 ms, MG Low 24 **200 Hz**, res 5–10 %, ENV 2 A 1 ms **D 80 ms** S 30 % R 100 ms, quantité 40 % | dotbeat bass-house (flag « unverified ») [DOC-2] |
| Pattern | offbeat 8ths avec octave-up sur les temps (« Offbeat Variation, the modern standard ») ; call-response sur 2 mesures ; phrases de 4 mesures ; vélocité constante 100–115 sauf accents 120+ ; toute note sur un temps ou un contretemps (grille 1/8) | ryansavoia (Max Styler, Produce School) [DOC-2] |
| Juno-60 house bass (analogique) | saw à fond, carrée 75 %, sub 45 %, PWM 75 % par env. 2 ; cutoff à mi-course, un peu de res, key track ; env. filtre decay 15 % S 0 quantité 75 % ; amp A 0 D ~½ S 25 % R court ; chorus I depth 70 % | Attack via dotbeat [DOC-2] |

**Chaîne.** Saturator (Analog Clip / Hard Clip, gain-match) → EQ (HP 30 Hz, −3 dB max à 200 Hz, high cut) → sidechain (Kickstart/LFO Tool ou compresseur, 4 ms) → EQ finale. Reverb/delay interdits sur le sub, tolérés sur la couche texturée > 250 Hz (ryansavoia). Tech house : « punchy, mid-focused, présence 100–200 Hz, distortion, sidechain fast attack medium release, mono » (JefroB).

## BH-8 — Stabs (bass house, « Shark Attack »)

Le stab de bass house est un **stab de house classique joué par le patch FM/growl** ; le tutoriel Jauz/Megalodon « Shark Attack » n'est disponible qu'en vidéo [DOC-EXTRAIT]. Voir H-3 pour les chiffres d'enveloppe (A 0–5 ms, D 66–250 ms, S 0, R 29–31 ms). Spécifique bass house [HEUR] : mono, une note ou une quinte (Stack **12+7** de Serum 2 empile octave et quinte sans jouer d'accord), WARP FM ou Sync, filtre passe-bande résonant (Attack Techno Stabs variante : bandpass, res poussée), Diode distortion, reverb **avant** la distorsion (chaîne Attack : Reverb → Overdrive 13 % → Saturator 10 dB → Drum Buss 26 %), delay 1/16 feedback court pour doubler l'impact (Attack clap). Coupe-bas **100 Hz** sauf si le stab est la basse (ProducerStack) [DOC].

## BH-9 — Vocal chops (bass house, G-house)

Voir FR-7. Spécifique : voix rap **pitchées vers le bas de 2–4 st**, compression, reverb discrète, 100–300 Hz, en intro/break/entre les drops (JefroB bass house) [DOC] ; chops courts (1–4 mots), pitch/time-stretch/reverse, delay throws, 500 Hz – 5 kHz (JefroB tech house) [DOC] ; Beat Repeat glitch : Interval 1 bar, Gate 7/16, Grid 1/16, filtre 4,20 kHz BW 6,61 (Attack via dotbeat) [DOC-2] ; probabilité MIDI 10 % sur les notes non-ancres, vélocité aléatoire 50–127 [DOC-2].

## BH-10 — Le drop en couches (sub + mid + top)

| Couche | Bande | Contenu et traitement | Source |
|---|---|---|---|
| Sub | 0–100 Hz (LP **90–100 Hz**) ; 30–60 Hz (JefroB) ; < 120 Hz (DUBFORGE) | sinus mono, **aucune saturation, reverb ni LFO**, chemin protégé hors du bus ; −3 dB relatif (MusicRadar) | ProducerHive, MusicRadar via dotbeat layering [DOC-2] |
| Mid / corps | HPF **> 100 Hz** (79 Hz Q 0,7 MusicRadar ; 75 Hz ModeAudio), LP 400–500 Hz ; 80–500 Hz (JefroB, HPF 80) | saw + carrée, saturation chaude, **même LFO que la couche growl** | idem |
| Growl / caractère | 500–2000 Hz (HPF 500) ; 500 Hz – 3 kHz (JefroB) | saws désaccordées 17 cents 3 voix, distorsion, notch −8 dB 2,5 kHz Q 4, boost +3 dB 600 Hz | dotbeat `three-layer-bass-stack` [DOC-2] |
| Air | > 2 kHz | facultatif ; « ajouter une 4e couche = sept sons qui se battent » | dotbeat [DOC-2] |
| Règles | toutes les couches jouent **le même rythme** ; LFO identiques ; glue 3–6 dB de réduction sur le bus sans le sub ; sidechain sur toutes | amen bassline cookbook, ProducerHive, ModeAudio [DOC-2] |
| Piège du coupe-bas | couper le mid **au-dessus de sa propre fondamentale** le rend mince : pour un F2 (87 Hz), HPF à **78 Hz, pas 105** ; le crossover est **sous** la note jouée ; la hauteur perçue est celle de la couche de caractère (jouer F1 plutôt que F2 si ça « sonne haut ») | amen memory *bass-must-keep-its-own-fundamental* [DOC-2] |
| Alternative | scinder **un seul oscillateur** en deux bus (split à 130 Hz) plutôt que poser un second sinus dessous (deux oscillateurs continus à phases non liées s'annulent) | amen memory *one-oscillator-cut-in-half* [DOC-2] |

**Serum 2, une instance.** OSC A sinus → **Direct** (sub) ; OSC B saw+carrée → FILTER 1 (MG Low 24, 480 Hz) ; OSC C saws unison 3 → FILTER 2 (1,8 kHz, res) ; LFO 1 (1 bar ou 1/8 Trig) sur les deux cutoffs ; FX : Splitter L/M/H (120 Hz / 2 kHz) avec Distortion par bande, Compressor MULTIBAND, Utility MONO BASS 120 Hz. Kick bass house : sub sine 40–80 Hz env. 200 → 50 Hz en 100 ms + corps 909 80–200 Hz + clic 2–8 kHz à −15 dB, alignés à l'échantillon (Fearvox) ; « punchy, mais moins qu'en tech house » (EDMProd, fiche 37).

---

# 3. House : future house, tech house, big room

## H-1 — Basse organ / M1 (Korg M1 « Organ 2 »)

**Ce qui est vérifié.** I17 « Organ 2 » = ton d'orgue percussif **à cycle unique** joué **en mono dans le grave** : Robin S « Show Me Love » (littéralement l'Organ 2 d'usine), Crystal Waters « Gypsy Woman », Nightcrawlers « Push the Feeling On » ; « Vogue = Organ 2 » est une confusion (Piano 16) [DOC, zayansalman]. Serum 2 : le son se fait « en échantillonnant la forme d'onde Organ 2 du M1 VST » et en l'important comme wavetable (ADSR) [DOC-EXTRAIT] ; Serum 2 charge aussi des multisamples.

| Approche | Réglage | Source |
|---|---|---|
| Multisample (fidèle) | Serum 2 moteur Multisample / Simpler avec l'échantillon ; ENV A 0–2 ms, D 150–300 ms (stab) ou S 60–80 % R 20 ms (ligne de basse) [HEUR] ; MONO, LEGATO, PORTA 0 | zayansalman [DOC] ; [HEUR] |
| Additif (Operator ou éditeur de table Serum) | sinus aux **harmoniques 1, 2, 3, 4** (« stacked sines/squares at 1, 2, 3, 4× with the **3rd harmonic prominent** ») ; niveaux tirettes B3 88 8000 000 = 16′ (h1) + 5⅓′ (h3) + 8′ (h2) ; key-click = enveloppe de filtre **5–15 ms** | amen iconic recipes ; `leads-nappes-textures.md` §4 [DOC-2/DOC] |
| Subtractif (MusicRadar) | patch init, **un oscillateur triangle/saw mixé à 32′** pour le grondement ; ensuite hall reverb + chorus | MusicRadar M1 organ bass [DOC-EXTRAIT] |
| Forum Ableton (Operator) | sinus accordés en accord mineur / harmoniques, « root + quinte, puis les mêmes une octave au-dessus » ; harmoniques par FM ou oscillateurs supplémentaires | [DOC-EXTRAIT] |
| M1-style (EDMProd) | osc 1 **triangle −2 oct**, osc 2 **carrée +7 st** ; LP « à goût » | dotbeat bass-house #8 [DOC-2] |
| UKG organ bass | carrée filtrée, **stabs courts syncopés, pas tenus** | amen UKG [DOC-2] |
| Registre | MIDI 36–48 ; hollow bass UKG = 2 sinus + FM (ADSR, `patches-genres.md`) | [DOC] |

**Chaîne.** Chorus léger + hall court (MusicRadar) ; saturation tube légère ; EQ HP 30 Hz ; sub sinus séparé si l'orgue est coupé-bas. **Erreurs.** Chercher l'Organ 2 par synthèse pure quand un échantillon existe ; jouer polyphonique ; oublier le clic.

## H-2 — Piano house (Korg M1 « Piano 16 »)

Vérifié : I01 Piano 16 sur « Ride on Time » (le **riff** ; la voix est un sample de Loleatta Holloway), « Rhythm Is a Dancer », « Finally », « Vogue », Beyoncé « Break My Soul » (avec Organ 2) [DOC]. SOS : aucun piano acoustique convaincant par synthèse ; **seuls les échantillons y arrivent** (`leads-nappes-textures.md`) — et le Piano 16 est lui-même un PCM.

| Approche | Réglage | Source |
|---|---|---|
| Échantillons | pack ProducerStack : 732 samples, 12 couches de vélocité, préset **Serum 2 multisample + Rack Live** [DOC-EXTRAIT] ; sinon Simpler/Sampler (« deux fois plus puissants que le M1 », forum Ableton) | [DOC-EXTRAIT] |
| Caractère à reproduire | brillant, attaque dure, **2e et 3e harmoniques fortes, fondamentale faible** ; decay **400–800 ms**, pas de pédale ; EQ HP **200–300 Hz**, boost **1–3 kHz** ; plate **1–1,5 s**, léger chorus, **gate serré** ; stabs courts sur les contretemps (pas 2, 6, 10, 14), accords 7e/9e | amen iconic recipes [DOC-2] |
| Approximation Operator [HEUR] | porteuse ratio 1 + modulateur ratio 1 index décroissant (« DX e-piano » ratio 1:1), attaque 0, decay 600 ms, plus bruit court pour le marteau, vélocité → niveau du modulateur (plus fort = plus brillant) ; regarder le spectre du sample pour caler les harmoniques 2 et 3 | amen recipes DX e-piano ; forum Ableton [DOC-2/DOC-EXTRAIT] |

**Erreurs.** Long release ; fondamentale pleine (« it does not sound like a real piano — that is why it cuts through a club system ») ; jouer les fondamentales (voicings sans tonique, 3e renversement).

## H-3 — Stabs et chords (deep house, tech house, techno)

| Recette | Valeurs | Source |
|---|---|---|
| House chord stab (dotbeat, chiffres mesurés) | 2 saws, osc2 +10 cents, unison 3 width 0,55 ; cutoff **320 Hz** res 1,8 ; amp A **5 ms** D **250 ms** S 0 R **31 ms** ; env. filtre A 3 ms D **160 ms** S 0 R 50 ms, quantité 0,8 ; vélocité → filtre 0,35 ; saturation chaude 0,2 ; couche corps **−12 st** (cutoff 800 Hz) à −14 dB ; sends reverb 0,18 delay 0,12 ; comp −30 dB 8:1 4 ms/100 ms mix 0,35 ; swing 56 % | `recipes-reference.md` [DOC-2] |
| Old-School House Chords (Attack, Zebra) | OSC1 0 st, OSC2 **+3**, OSC3 **+7** (triade mineure dans le patch, jouable d'une touche) ; variante +5/+8 ; OSC1 −12 pour doubler la basse ; unison 2 → 7, detune 5 → 7 (échelle Zebra) ; LP 4 pôles, cutoff ~0 piloté par l'enveloppe (« 2 h ») ; « attaque assez vive, decay plus long » ; reverb puis Dimension Expander | dotbeat chords-pads #1 [DOC-2] |
| Techno Synth Stabs (Attack, Hive) | carrée ; amp A **0** D **66** S 0 R **29** ; filtre A **5** D **48** S 9 R **24** (ms selon `bass-techno.md`, « 0–100 dial » selon `chords-pads.md`, voir §5) ; LP 24 cutoff 52 res 28 env 92 ; variante passe-bande res forte ; Soft Clip → ping-pong ; DAW : **Reverb (pre-delay ≈ 3 ms, decay ≈ 3 ms) → Overdrive 13 % → Saturator 10 dB → Drum Buss 26 %** ; automation du dernier accord de la phrase | [DOC-2] |
| Deep house stab (KVR) | 3 saws/triangles 0/+3/+7 ; **cutoff 250–350 Hz** ; env. filtre sustain 0, decay court (« c'est le decay qui fait le stab ») ; Gm9 voicé A–Bb–D–F | [DOC-2] |
| Sytrus Maj7 en FM | 4 opérateurs carrés, ratios **2,0000 / 2,5198 / 2,9966 / 3,7754** (0/+4/+7/+11 st), master −24 ; ping-pong 5:00 offset 12 ms ; reverb low cut 750–800 Hz decay 5 s ; mono + portamento | [DOC-2] |
| Orgue rave (M1 Organ 2 en stab) | sinus/carrées 1,2,3,4×, 3e harmonique en avant ; A instant, D **150–300 ms**, coupure nette ; mineur ou sus4 sur contretemps ; reverb gated, petit pitch-up à l'attaque | amen iconic [DOC-2] |
| Rhodes resamplé (Attack) | Alchemy : decay **1,2 s**, tube 30 %, BP2 SVF **160 Hz** res > 50 % drive 20 %, reverb 2500 ms 20 %, delay 20–25 % | dotbeat sample-manipulation [DOC-2] |
| Voicings | 3e renversement, **sans la fondamentale**, laisser les temps du kick, varier le voicing d'un même accord ; compression 4–5 dB attaque lente release rapide (non re-confirmé) | Attack Kerri Chandler via dotbeat [DOC-2] |

**Serum 2.** Une touche = accord : OSC A/B/C SEMI 0/+3/+7 (ou Stack 12+7 pour octave+quinte) ; FILTER 1 MG Low 24 CUTOFF 300 Hz, ENV 2 → CUTOFF 80 %, ENV 2 D 160 ms S 0 ; ENV 1 D 250 ms S 0 R 31 ms ; FX Reverb sur BUS (fiche 35 : pas d'enveloppe sur le mix d'une reverb polyphonique), Hyper/Dimension, EQ HP 100 Hz sauf stab-basse (ProducerStack). **Erreurs.** Attaque 10–30 ms (« consensus zéro » : le punch vient du decay) ; triades nues ; fondamentale doublée.

## H-4 — Vocal chops et toplines (house)

Voir FR-7 et BH-9. Ajouts house : chop de disco/soul, « one-shot vocals “yeah”, “come on”, diva » (amen house) ; UKG : syllabes montées **+2 à +5 st**, artefacts de time-stretch assumés, formant séparé du pitch (amen UKG) ; structure call/response dans le drop, hook complet dans le break (ryansavoia) ; Simpler Slicing (Transient) ; « fewer chops » (SOS) : trois slices suffisent pour un groove neuf [DOC-2].

## H-5 — Basse tech house « rolling » (Fisher, Dom Dolla, Chris Stussy)

Le tutoriel « Fisher Losing It » d'Incognet déjà archivé est une coquille sans chiffres ; les tutoriels Dom Dolla / James Hype / Biscits et « Fisher tech house bass » sont des vidéos [DOC-EXTRAIT]. Chiffres écrits disponibles :

| Recette | Valeurs | Source |
|---|---|---|
| SoundBridge (Vital) | osc 1 carrée, osc 2 saw un peu plus bas ; **phase random off** ; LP 24 dB cutoff **150 Hz**, res **0** ; ENV 2 (pluck) → cutoff et cutoff de distorsion, « petite quantité » ; distorsion post-filtre **8 dB** ; multibande une bande, 50 %/50 % ; EQ **+10 dB à 75 Hz** Q ~1–2 | dotbeat bass-house #1 [DOC-2] |
| Rolling, valeurs de départ | A 0, D **150–300 ms**, S 20–40 %, R < 100 ms ; env. filtre A 0, D 150–250 ms (« boing »), 20–30 % sur le cutoff | SoundBridge [DOC-EXTRAIT] |
| Serum (Mystic Alankar / Mind Flux) | ENV 2 D ≈ 200 ms S 0 → cutoff 5 %, résonance 10 % | [DOC-EXTRAIT] |
| Wavetable (Killer Tech House Bassline) | release d'ampli **réduite** (600 ms par défaut = boue) ; Osc 1 saw, position légèrement montée ; filtre **12 dB** (pas 24, garder des harmoniques), petite résonance ; Env 2 → cutoff : sustain à zéro, decay court (« twang ») ; Osc 2 saw, forme → Env 2 ; mono + glide | ryansavoia [DOC-2] |
| Repro-1 (Attack) | Osc A saw + pulse (largeur réduite), Osc B pulse −1 oct, master −12 ; feedback 25 % ; cutoff presque fermé, env. forte, key track léger ; env. filtre decay ~1/3 S ~0 ; amp S < 25 % ; Jaws (Teeth max, F-mod 75 %) → Lyrebird echo 1,26 mix 14,5 → RESQ shelf → Sonic Conditioner | dotbeat [DOC-2] |
| Warehouse (Attack, 3 couches) | sub LP **80 Hz** 12 dB, MDMX Screamer 35 % ; ligne HPF **65** LPF **350**, −100 Hz, +330 Hz ; kick doublé en delay 1/16 100 % wet ; **premier 16e vide** ; sidechain LFO Tool release lente « pour le swing » | dotbeat bass-techno C1 [DOC-2] |
| Chris Stussy 3 notes (non vérifié) | MG Low 24 200 Hz res 5–10 %, ENV 2 A 1 D 80 S 30 % R 100 ms à 40 %, glide 0 | [DOC-2] |
| Patterns | offbeat 8ths / offbeat variation avec octave-up / full 1/8 (sidechain obligatoire) / rolling 16ths legato avec sauts d'octave / 303 legato / sustained + answer ; 4 mesures, seconde moitié syncopée ; « l'octave-up est la technique n°1 pour le drame » | ryansavoia [DOC-2] |

**Consensus des 10 recettes house (dotbeat).** Deux oscillateurs à l'octave (ou octave + quinte) ; LP parqué **80–200 Hz** ouvert par une enveloppe rapide ; sustain nul ou court ; distorsion post-filtre standard ; sidechain obligatoire ; mono/legato. Désaccords : résonance 0 (SoundBridge) contre accordée au 5e harmonique (ModeAudio) ; cutoff 80 Hz contre 913 Hz (Tracey Brakes : High 12, res 22 %, unison 7 detune **0,15**, OCT −3, sur un sub A séparé) — ce sont des couches différentes d'un même son.

## H-6 — Big room lead / pluck

| Étage | Réglage | Source |
|---|---|---|
| Couche principale | saw, UNISON **7**, DETUNE Serum **0,20–0,30** (Myloops, « un quart de la course ») ou **0,12** (Monosounds big room) ; median mesuré 10 cents (leads = detune le plus étroit) ; HPF **200 Hz**, +2/+3 dB à 3 kHz ; spread 60–80 % ; A 4 ms D 250 ms S 0,6 **R 31 ms** ; env. filtre 0,3 | Myloops, Monosounds, dotbeat [DOC-2/DOC] |
| Couche +12 | 3–5 voix, detune plus serré, HPF **500 Hz**, shelf +2,5 dB 8–10 kHz, **6–10 dB sous** la principale (−8 dB encodé) | Myloops, MusicTech [DOC-2] |
| Sous-octave (option) | un oscillateur, unison ≤ 2, mono, LP 800 Hz – 1 kHz, HPF 80 Hz, automatisé in/out | Myloops [DOC-2] |
| Bruit / air | bruit blanc **+4 octaves**, mêmes réglages d'unison, HPF propre, « très audible » (Syntorial) ; Serum : NOISE key track + HPF 3 kHz | [DOC-2] |
| Pluck big room | « woody percussive with lots of gated reverb » ; A 1–4 ms, D 160–260 ms, S 0, R 80–140 ms ; gated reverb 0,5–1 s (électronique) | Cymatics/Ghost Production, SampleFocus [DOC-EXTRAIT/DOC-2] |
| Automation | cutoff qui monte mesure par mesure sur 24 + 8 mesures et s'ouvre pile sur le drop | Myloops [DOC-2] |
| Sidechain lead | 2:1–3:1, 5–10 ms, 100–150 ms, **2–3 dB** ; pads −3 dB 2–4 kHz, kick −2 dB 3–5 kHz, plucks −2 dB 500 Hz–1 kHz pour faire de la place | Myloops [DOC-2] |
| EQ | notch **1,6–3,8 kHz −6/−12 dB** haut Q, boost **450–800 Hz** ; compression ~12 dB sur la bande haute seule (KVR) ; Monosounds : −500 / −1,5 k / −3,5 k, shelf > 12 kHz | [DOC-2/DOC] |
| Drop big room | kick + basse + **un motif de lead** ; « pitched kick » descendant ; 3 notes max ; second drop : +1–2 st, octave-up, un élément de plus | amen EDM, drop-and-buildup [DOC-2] |

Reverb send 3–5 s HPF 500 / LPF 8 kHz (−12 dB), delay 1/4 ping-pong ou pointé feedback 30–40 % BP 500 Hz–5 kHz (−15 dB) ; **un seul** élargisseur ; vérification mono. Table CMUSE (voix / detune externe / largeur) : lead 3–7 voix, 6–18 cents, 25–70 % ; supersaw 7–9, 12–28 cents, 50–100 % ; pad 7–12, 18–40, 70–100 % [DOC-2].

## H-7 — Kick de festival (layering, accord)

| Point | Valeurs | Source |
|---|---|---|
| Big Room House (Attack) | 909 sous **forte compression + saturation bande**, mélangé à un **808 plus profond** ; couche de caractère DR-202 / HR-16 / 707 / LinnDrum / DMX ; hiss vinyle et shaker très bas ; kick long **accordé à la tonalité** ; couper le grave du kick snappy sous **150–250 Hz** | Beat Dissected Big Room House [DOC-EXTRAIT] |
| 3 couches | sub 30–80 Hz (50–80) / corps **100–150 Hz** (punch) / clic 2–5 kHz ; boîte 200–400 et boue 300–500 Hz à couper ; transitoire : compresseur attaque 5–10 ms ; « EQ ne peut pas booster ce qui n'existe pas » ; « ne superposer que pour une raison » | dotbeat layering (Attack, transmissionsamples) [DOC-2] |
| Phase | départs dans le même sens sinon inverser la polarité ; oscillateur synthétique **phase 0° à chaque trigger** (sinon niveau variable d'un coup à l'autre) ; sub synthé **une octave sous** le sample (27,5 Hz sous 55 Hz) ; nudge par pas de 0,1–1 ms | dotbeat, `percussions.md` [DOC-2/DOC] |
| Accord | 808 natif **49,5 Hz = Sol1** ; descendre à Ré1 coûte −11,8 dB (−4,5 dB si 5 partiels) ; rester ≥ Mi1 ; tonique ou quinte (ryansavoia : « 5th works great ») ; ou **éviter** la bande de la basse (position B) — arbitrage, pas règle | `percussions.md` §2, `basses.md` §7 [DOC] |
| Dirty tech house | bass drum −2 st, sub 808 +2 st (même classe), kick de syncope +1 oct ; EQ → Saturn → EQ (shelf aigu réduit) | dotbeat drums #4 [DOC-2] |
| Chaîne | kick à **0 dB** avec clipper dur (Saturator Digital/Hard Clip), clipper sur le groupe kick + clap ; EQ correctif → clip → transient → comp → EQ couleur → mono bass | ryansavoia ; `percussions.md` §9 [DOC-2/DOC] |
| Mesure | facteur de crête bus batterie **12–16 dB** avant master ; corrélation +1 en 30–80 Hz ; glue ~4 dB attaque rapide release auto | `percussions.md` ; dotbeat drums [DOC/DOC-2] |

Serum 2 pour un kick : OSC A sinus, ENV 2 → CRS **+24…+36 st** decay 20–40 ms (909 : 220 → 55 Hz en 15–30 ms), ENV 1 A 0 D 250–500 ms ; NOISE one-shot 5 ms + FILTER 2 HP 2 kHz pour le clic ; Distortion Tube ; Utility MONO BASS. Kick 2 conseillé par le cours Protoculture [DOC-EXTRAIT].

## H-8 — Claps

| Point | Valeurs | Source |
|---|---|---|
| Circuit 808 | bruit → passe-bande **1 kHz** ; 3 bursts de 10 ms + 20 ms (attaques 0 / 7,6 / 15,5 / 23 ms) ; queue « reverb » **100 ms** en parallèle : la réverbe est une seconde enveloppe du circuit | `percussions.md` §4 [DOC] |
| Synthèse | 4 bursts BP 800 Hz – 4 kHz espacés 8/12/16 ms, ~15 ms chacun, corps 100–200 ms, HP 300 Hz | amen recipes [DOC-2] |
| Attack (variante) | HP 12 dB ~30 Hz res 62, shelf 550 Hz, roll-off 19 kHz, **delay 1/16 feedback ~7** pour doubler, comp seuil −20 dB | `percussions.md` [DOC] |
| Placement | identité du clap **1–2 kHz** (balayer un passe-bande) ; HPF **130–140 Hz** ; présence +5–10 kHz ; notch dans la snare là où le clap attaque | KVR via dotbeat drums [DOC-2] |
| Clap + snare | snare pics ~200 Hz et 5–7 kHz, le clap remplit le milieu ; clap **mono**, une seule bonne sample ; snare 2–3 couches, reverb 12 % ; couches « tail » : une large aiguë + une mono grave, attaque rognée | ryansavoia [DOC-2] |
| Layering | même position stéréo, EQ complémentaire, delay stéréo partagé L≠R < 30 % wet ; 5 couches nudgées (Organic Tech-House) ; clap en avance de quelques ms (Dusted Deep House) ; parallèle **8:1** attaque rapide, 20–30 % | Attack, SampleFocus via dotbeat [DOC-2] |
| Reverb | gated **0,5–1 s** (électronique) vs 2–4 s (80s) ; Lexicon hall 10 % (Jackin') ; pitch-shift ≤ 3–4 st | idem |

## H-9 — Hats

| Point | Valeurs | Source |
|---|---|---|
| 808 | **six carrées** aux ratios 1 / 1,34 / 1,61 / 1,99 / 2,44 / 2,79 × ~320 Hz, HP 6–8 kHz, fermé 30–60 ms, ouvert 300–600 ms | amen drum-machines [DOC-2] |
| 909 | échantillons 6 bits (~25 kHz), open hat sur le contretemps = **le** marqueur house ; OH 300–500 ms | amen ; `percussions.md` [DOC-2/DOC] |
| Bruit | BP 6–12 kHz, fermé 20–50 ms, ouvert 200–600 ms ; ≤ 200 ms fermé, ~1000 ms ouvert (`percussions.md`) ; kit dotbeat : hat 50 ms, open 450 ms, tone 6,5 kHz | [DOC-2/DOC] |
| EQ / niveau | HPF 800 Hz (Fearvox) ; 3 kHz deep house (JefroB) ; air 8–12 kHz, HP 400 Hz ; moyenne des hats **−37 à −41 dB** (ryansavoia) ; jackin' : 3 couches (XE8 bruit, MT500 lo-fi, 909 ghosts) | [DOC-2] |
| Vélocité / swing | alternance **~80 / ~100** (tick-TOCK) ; ghost 40–60 % ; swing hats seulement : 52–56 % house, 55–62 % deep, 60–65 % jackin'/deep tech, 50–60 % organic, **70–80 % dusted** ; 15–25 % sur les 16es off (Fearvox) ; choke group ouvert/fermé | amen, SampleFocus, Attack via dotbeat [DOC-2] |

## H-10 — White noise (textures, sweeps, shakers)

Serum 2 NOISE : White / Pink / Brown / Geiger, one-shot, key track ; NOISE comme source de modulation (« vibrato errant »). Bruit de fond : bus dédié, HP ~300 Hz, « senti pas entendu », **hors sidechain et hors compression master** (fiche 29) [DOC]. Shaker = bruit blanc, énergie > 6 kHz, 16es à 40–60 % de vélocité (Fearvox, `percussions.md`). Riser : FR-6. « Multiband : grondement grave + souffle aigu simultanés » (MusicRadar via `leads-nappes-textures.md`). Operator : forme Noise = bruit passe-bande, « la clé des bons hats et snares » (fiche 39). Ryansavoia : riser = Operator noise osc + bandpass automatisé vers le haut [DOC-2].

## H-11 — Impacts

| Couche | Réglage | Source |
|---|---|---|
| Grave | sinus **60 → 30 Hz**, decay 1–2 s ; sub-drop **80 → 25 Hz sur 0,5–2 temps**, saturé, le bas du sweep juste avant le temps 1 | amen transitions [DOC-2] |
| Médium | burst de bruit passe-bas, decay 1–3 s ; ou kick/tom pitché vers le bas | amen ; SOS via `leads-nappes-textures.md` [DOC-2/DOC] |
| Aigu | clic distordu ; crash | idem |
| Avant | queue de reverb **inversée** placée avant le coup | amen |
| Alignement | **points de crête alignés au début** ; compression forte, quasi mono ; reverb longue puis fade pour ne pas manger la mesure 1 | `leads-nappes-textures.md` §6 [DOC] |
| Downbeat du drop | impact + crash + sub-drop + mix complet, tous sur le même échantillon | amen drop-and-buildup [DOC-2] |

## H-12 — Downlifters

Sweep tonal ou de bruit **descendant en hauteur, 1 mesure**, placé sur le **premier temps** de la nouvelle section : il « dépense » l'énergie accumulée (amen) [DOC-2]. Recette (`leads-nappes-textures.md`) : même source que le riser, pitch **−12 à −24 st** sur 1 mesure, LP qui se ferme, send de reverb qui monte ; riser et downlifter doivent se **croiser** sur la dernière mesure [DOC]. Tape stop : lecture de 1,0 à 0,0 en **200–600 ms** avec pitch et volume (amen). Serum 2 : LFO Mode **Env** → CRS −24 st, ENV BPM 1 bar, NOISE Brown pour le grondement. Budget : deux vrais silences par morceau ; « un riser sur chaque transition cesse de fonctionner » (amen).

---

# 4. Conversions Sylenth1 / Spire / Massive → Serum 2

Les recettes publiées sont surtout écrites pour Massive (Attack Synth Secrets), Sylenth1 (trance, Detuned Pad, 303 arp), Diva, Zebra, Hive. Correspondances documentées et heuristiques :

| Massive / Sylenth1 / Spire / autres | Serum 2 (nom exact) | Statut |
|---|---|---|
| Massive « Sin-Squ » position gauche → droite | OSC Basic Shapes, WT POS 0 (sinus) → carrée ; ou table « Sin-Tri-Saw-SQ » (NI) | [HEUR] |
| Massive « Bend−/+ », « Bend+ » | WARP Bend +/− (50 % = neutre), Bend + | [DOC] cartographie §4.1 |
| Massive oscillateur de modulation **Phase Modulation** | WARP 1 = **PD from OSC** (kPD_OSC) ou FM from OSC ; la source doit être active, son niveau peut être 0 | [DOC] §4.2 |
| Massive « Intensity / Position », Performer / Stepper | WT POS ; LFO GRID X/Y avec Shift-clic (séquenceur de marches) | [DOC] |
| Massive filtre **Daft**, **Lowpass 4**, **Scream**, Comb | MG Low 24 ou **French LP** (distordant, VAR Boeuf) [HEUR] ; MG Low 24 ; **Scream LP/BP** (existe) ; Comb ± | [DOC/HEUR] |
| Massive **Classic Tube** | FX Distortion TYPE Tube (filtre PRE/POST) | [DOC] |
| Massive **Dimension Expander** (Size, Dry/Wet) | FX **Hyper/Dimension** : UNISON 0 → Dimension seul, SIZE, MIX propre | [DOC] |
| Massive Unisono « Pitch Cutoff » (demi-tons) | UNISON + DETUNE (0–1) avec **RANGE** en demi-tons (Global, défaut 2 st) ; étalement ≈ DETUNE × RANGE [HEUR, Tuning Linear] — **à mesurer : la course DETUNE n'est pas garantie linéaire, et le sens de RANGE (total ou par côté) est MUET** | [HEUR/TEST] |
| Massive « Restart via Gate », Diva « phase restart » | OSC PHASE 0°, RAND 0 % | [DOC] |
| Massive Glide 10–15 % / 30 % | GLOBAL PORTA en secondes (0–8 s) : 10–15 % ≈ 40–80 ms [HEUR], Diva « one third » ≈ 60–120 ms [HEUR] ; option SCALED | [HEUR] |
| Sylenth1 unison 8 voix / osc, detune 0–10 | UNISON 8 (max 16), DETUNE : Sylenth = « detune max dépend du nombre de voix », Spire « n'arrive pas à reproduire l'écart de Sylenth » → pas de conversion numérique publiée | KVR, Passion for EDM [DOC-EXTRAIT] |
| Sylenth1 Detuned Pad « detune 4,05 / 3 » | valeurs sur l'échelle Sylenth (0–10) ; `leads-nappes-textures.md` les lit en cents : **unité non confirmée** | [⚠] |
| Spire « wide » | WIDTH de l'unison | [HEUR] |
| Serum 1 « OTT » | Compressor MULTIBAND ; Depth = MIX ; crossovers non publiés | `patches-genres.md` §6 [DOC] |
| Hive envelopes (Techno Stabs) | ENV en ms : A 0 / D 66 / S 0 / R 29 ; filtre A 5 / D 48 / S 9 / R 24 — si l'échelle est bien en ms (voir §5) | [DOC-2] |
| Diva Garage Bass filtre « 25 % », env « max » | FILTER 1 CUTOFF 25 % de la course (stocké 0–1, log 8 Hz–22 kHz : ≈ 140–200 Hz [HEUR]), MATRIX ENV 2 → CUTOFF +100 | [HEUR] |
| Unités de detune en circulation | Serum publié : **0,10 / 0,16** (Attack), **0,15** (Tracey Brakes), **0,08–0,15** (Monosounds), **0,20–0,30** (Myloops) ; cents : 10 (médiane leads), 17 (basse), 18 (pads), 20 (plucks), ±27–61 (Reese) ; % de bouton (FaderPro 20 %, 7 %) : **non convertibles entre synthés** | [DOC/DOC-2] |
| JP-8000 (Szabo) | 7 voix, mi-course ≈ ±18 cents, max ≈ ±2 st, centre −2,5 dB ; Serum : UNISON 7, Tuning **Super** [HEUR], BLEND 75 % (Szabo : égalité des amplitudes à mix 0,75), RAND 100 % | [DOC/HEUR] |
| Massive « 2Pulse » PD 25/52 (wobble) | WARP PWM / Bend sur une carrée [HEUR] | [HEUR] |
| dotbeat `resonance` 0,1–9 | échelle du moteur dotbeat (≈ Q), **pas** RES 0–100 de Serum | [⚠] |

Règle générale (fiche 34) : ne pas transposer une recette Serum 1 telle quelle ; qualité/oversampling change les warps FM/PD (Ultra = 4×).

---

# 5. Contradictions

1. **Qui tient le fondamental en bass house** : Preset Drive (kick 50–80 Hz, basse coupée à 30–40 Hz) contre EDMProd (« kick avec peu de grave pour laisser la place à la basse ») — non tranchée, à décider par morceau (`patches-genres.md` §5).
2. **Ratio FM d'EDMProd** : `basses.md` écrit « 2 octaves et 7 demi-tons = rapport 3:1 » ; c'est **6:1** [CALC]. Erratum à porter dans `basses.md`.
3. **Unités du detune** : Serum 0–1 (Attack 0,10/0,16), cents (Reese 7–61), % de bouton (FaderPro), échelle Sylenth (4,05), demi-tons Massive (0,3) — jamais interconvertibles sans mesure ; et la médiane mesurée des leads (10 cents) contredit le folklore « détuner fort le lead ».
4. **Nombre de voix d'unison** : 2–4 / 4–5 / 7 (JP-8000, spike mesuré) / 9 par osc × 3 (Syntorial) / 16 « myth » (Monosounds) — 7 est le centre de masse, 9+ relève de l'empilement d'oscillateurs.
5. **Reese** : detune ±7 à ±61 cents et cutoff 600 Hz à 4 kHz pour « le même » Reese DnB ; « classique = deux sinus » (Attack) alors que l'article construit deux wavetables complexes ; MusicRadar et Noise Masters utilisent des saws.
6. **Wobble** : oscillateurs jamais identiques d'une source à l'autre (2Pulse + carrée +19 st ; saw + carrée ; preset « Escalation II »).
7. **Enveloppe 909** : `percussions.md` (SOS) donne une enveloppe de pitch **200–500 ms** pour la 909 contre 20–70 ms pour la 808 ; amen donne 909 = **220 → 55 Hz en 15–30 ms** (« ce sweep rapide EST la 909 ») et 808 = 100 → 50 Hz en 20–40 ms. Directement opposé sur la durée ; le circuit 808 mesuré (Baratatronix : pic ~130 Hz pendant ~6 ms) est plus proche d'amen. À trancher à l'oreille sur des samples 909.
8. **Enveloppes Hive des Techno Stabs** : `bass-techno.md` les cite en **ms**, `chords-pads.md` « échelle 0–100 » ; même source (Attack). Vérifier sur la page.
9. **Attaque d'ampli des stabs** : consensus « 0 ms » (dotbeat, 85 % ≤ 12 ms) contre le danger de clic à 0 ms (amen timbre : « 1–5 ms ou phase 0 ») — conciliable : 0–4 ms avec PHASE 0 / RAND 0 ; les médianes mesurées sont à 3,9 ms, le plancher machine.
10. **Fréquence de passage en mono** : 100 / 120 / 150 / 200 / 250 Hz selon les sources (`basses.md` §6) ; consensus dotbeat 75–100 Hz pour le crossover sub/mid ; amen memory : le HPF du mid doit être **sous** la note jouée (78 Hz pour F2), ce qui contredit « HP du mid juste au-dessus de 100 Hz » (ProducerHive) pour les notes graves.
11. **Sidechain « agressif »** : 3:1 (MusicRadar), 5:1 (EDMProd), 10:1–20:1 (survey), 8:1–10:1 (Fearvox) ; release 20–80 ms (staccato) vs 200–500 ms (pompage) ; attaque 4 ms est le seul chiffre justifié (anti-clic).
12. **Swing house** : 50–60 % (organic tech), 60–65 % (jackin', deep tech), 70–80 % (dusted) dans la même série Attack ; 52–56 % (amen) ; 15–25 % (Fearvox, autre échelle).
13. **Accorder le kick** : à la tonique/quinte (majorité) contre hors de la bande de la basse (position B) ; Deruty : la 808 est nativement en Sol.
14. **Glide 808** : 80–120 ms (unison.audio) vs ~300 ms (Attack Serum) vs « à mi-course ».
15. **Detune des pads** : 3–4 cents « chaleur » (Attack Zebra), défaut pour SOS (« off-colour »), 7,5+ cents recherché en trance, médiane mesurée 17,7 cents.
16. **Decay de pluck** : 160–260 ms (Cymatics), 200–300 ms (Myloops), 1,25 s (Zebra 3), médiane mesurée 867 ms — c'est une intention de design, pas une erreur ; les plucks house rythmiques sont au bas de la plage.
17. **OTT** : aucun crossover publié ; Depth 15–25 % (`patches-genres.md`) vs 30–60 % (amen future bass) vs 30–50 % canal / 15–30 % bus (Subtronics).
18. **« Vogue » = Organ 2** : lore fausse (Piano 16) ; « Ride on Time » vocal = Loleatta Holloway, pas le M1.
19. **Acid / 303** : NI et Attack disent que le patch statique n'existe pas (geste en temps réel) ; pente 18 (Roland) / 24 (MusicRadar) / 12 dB (Sylenth).
20. **Talking bass** : tables de formants différentes (amen « ee » 270/2290 vs DUBFORGE « I » 390/1990 « adaptées à la basse ») — même voyelle « ah » et « oh » identiques dans les deux.

---

# 6. Sources

## 6.1 Documents GitHub lus en entier et archivés (`corpus/house-future-rave/`, 24 fichiers, ≈ 750 Ko)

`amen-patterns-08-sound-design-recipes.md`, `amen-patterns-03-bassline-cookbook.md`, `amen-instruments-12-software-instruments.md`, `amen-instruments-09-virtual-analog-and-90s.md`, `amen-instruments-08-drum-machines.md`, `amen-foundations-09-bass.md`, `amen-foundations-12-timbre-and-synthesis.md`, `amen-sessions-06-dubstep-and-bass-music.md`, `amen-memories-bass-must-keep-its-own-fundamental.md`, `amen-memories-one-oscillator-cut-in-half-not-two-oscillators.md`, `amen-memories-a-timbre-figure-must-not-repeat-exactly.md` (mekedron, commit ff63fa0) ; `dotbeat-priors-bass-house.md`, `-leads.md`, `-drums.md`, `-layering.md`, `-chords-pads.md`, `-bass-basseries.md`, `-bass-techno.md`, `-sample-manipulation.md`, `-readme.md`, `dotbeat-recipes-reference.md` (wgpatrick/dotbeat, branche main) ; `ryansavoia-ableton-mcp-house-production-skill.md` ; `zayansalman-dance-gear-fingerprints.md` ; `dubforge-subtronics-deep-dive.md`. Déjà archivés par d'autres agents et relus ici : `fearvox-syn-bass-house-structure-research.md`, `jefrob-genre-house-sound-design.md`, `jefrob-genre-house-production-techniques.md`, `amen-patterns-02-drop-and-buildup.md`, `amen-patterns-06-transitions-and-fx.md`, `bitwize-genre-edm-readme.md`. Lus mais non archivés (hors sujet ou hors langue) : `Celian-mrc/serum-mcp` README (outil de génération de presets Serum 2, schéma des paramètres à télécharger), `BITRAGER069/DUBFORGERAGE engine/serum2_preset.py` (noms des presets d'usine, repris en BH-6), Gaku52 dj-skills-guide (japonais), kleer001 music_loom (liste de FLP), nhdxyz/ableton-plugin (audit produit), SJY051 electronic-edm.md (survol de genres).

## 6.2 Pages à télécharger depuis le Mac

`urls-axe3.json` : 127 URL (Attack Magazine Synth Secrets / Beat Dissected / Passing Notes, MusicRadar, The Producer School, SampleFocus, Mystic Alankar, Mind Flux, SoundBridge, Monosounds, EDMProd, Cymatics, ADSR M1, Studio Brootle, ProducerStack, SonicState, Syntorial, FaderPro, Myloops, MusicTech, CMUSE, KVR ×5, NI, Noise Masters, Dystopian Collective, SOS ×2, unison.audio ×2, Brown Noise Radio, Preset Drive, EDM Templates, Sample Market, Aulart, Sonic Academy Protoculture, Cr2, packs future rave, Wikipedia ×3, Splice ×2, ProducerHive, Subaqueous, ModeAudio ×2, transmissionsamples, Ali Jamieson, howtomakeelectronicmusic, Puremix, The Vocal Market, Integraudio, Passion for EDM, serum-mcp PARAMETER_SCHEMA, DUBFORGE serum2_preset.py, JefroB trance, dotbeat transients + research 141).

## 6.3 Ce qui reste muet

- Le patch du lead future rave de Guetta/MORTEN (résonance, quantité de pitch env, portamento) : seuls des presets commerciaux et des vidéos. Voie recommandée : analyser une référence audio avec `synthese-reference` (déjà conseillé par `patches-genres.md` §10).
- Les « toms de rave » : aucune source ; fiche FR-4 = [HEUR] à partir des toms 909/Simmons et de la règle d'accord des kicks.
- L'index de modulation FM (quantité de WARP FM) des basses future house / Jauz : jamais chiffré.
- Le mapping exact DETUNE × RANGE de Serum et la courbe du mode Tuning « Super » : à mesurer (fiche §4).
- Les crossovers de l'OTT / Compressor MULTIBAND.
- Le Jauz « Shark Attack » et les basses Dom Dolla / Fisher : vidéos uniquement ; les chiffres écrits les plus proches sont ceux de The Producer School (Chris Lake) et de SoundBridge.
