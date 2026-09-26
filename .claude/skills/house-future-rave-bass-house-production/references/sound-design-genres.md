# Sound design professionnel — future rave, bass house, house de festival et de club

Vingt-neuf sons, chiffrés quand une source les chiffre, dans Serum 2 avec les noms exacts de `../../sound-designer-serum/references/serum2-cartographie.md`, et leurs équivalents natifs. Recherche du 24 septembre 2026 (rapport complet, avec toutes les valeurs et sources : `../../../../corpus/house-future-rave/recherche-house-axe3-sound-design.md`). Les recettes prêtes à exécuter sont dans `../recipes/`.

Étiquettes : `[DOC]` document lu en entier ; `[DOC-2]` compilation secondaire lue en entier (dotbeat, amen-sessions) citant sa source primaire ; `[DOC-EXTRAIT]` résumé de page bloquée ; `[HEUR]` déduction avec sa logique ; `[CALC]` calcul ; **MUET** = aucune source ne le chiffre.

Déjà dans le dépôt, cité sans être répété : `../../sound-designer-serum/references/patches-genres.md` (Garage Bass, Beat-Pulsing Plucks, Warping Bass, ANNA, OTT, tempo), `basses.md`, `leads-nappes-textures.md`, `percussions.md`, `fiches-pratiques.md` (fiches 2, 3, 4, 28, 29, 34, 35, 36, 37).

---

## 0. Trois constats avant toute recette

1. **Aucune page écrite ne chiffre un patch future rave de Guetta ou MORTEN** : seulement des packs de presets et des cours vidéo. La seule ligne chiffrée est celle du guide supersaw de Monosounds (`../../../../corpus/cuivres/monosounds-studio-serum-2-supersaw.md`) : *unison 5, detune 0,09, passe-bas balayé 400–900 Hz, « une supersaw déguisée en basse »*. Le reste est reconstruit depuis le hoover Alpha Juno et le supersaw JP-8000 mesuré, et marqué comme tel.
2. **Les basses house et bass house sont très bien chiffrées** (dix recettes house, quinze Reese/wobble/808, seize stabs), avec des **médianes mesurées sur 3 559 patchs Surge** `[DOC-2 dotbeat]` : attaque d'ampli de basse 3,9 ms, decay 621 ms ; detune de lead médian **10 cents** (le plus étroit des rôles) ; decay de pluck 867 ms ; attaque de nappe 541 ms ; release d'accords 31 ms (« la queue vient des sends »).
3. **Le Korg M1 se réduit à deux presets** : I01 *Piano 16* (« Ride On Time », « Rhythm Is A Dancer », « Finally », « Vogue ») et I17 *Organ 2* (« Show Me Love », « Gypsy Woman », « Push The Feeling On »). « Vogue = Organ 2 » est faux. Les deux sont des PCM : la voie fidèle est le **multisample** (Serum 2 Multisample, Simpler, Sampler).

Erratum porté dans `basses.md` : « 2 octaves + 7 demi-tons = 3:1 » → c'est **6:1** `[CALC]` (1 octave + quinte = 3:1).

## 0.1 Tempo en millisecondes `[CALC]`

| Division | 126 BPM | 128 BPM |
|---|---|---|
| 1 mesure | 1905 | 1875 |
| 1/4 | 476 | 469 |
| 1/8 | 238 | 234 |
| 1/8 T | 159 | 156 |
| 1/16 | 119 | 117 |
| 1/32 | 60 | 59 |

Ne bougent pas avec le tempo : hauteurs, ratios FM, unison, cutoff, drive. Se transposent seuls : les divisions synchronisées. Se recalculent : les millisecondes (decays rythmiques, glide, pre-delay).

---

## 1. Future rave

### FR-1 Lead « rave » (recette `../recipes/lead-future-rave-supersaw-basse.md`)
Une basse-lead mono, sombre, à filtre résonant, plus un hoover atténué. OSC A saw UNISON 5 DETUNE 0,09 BLEND 75 WIDTH 50–60 ; OSC B saw OCT −1 UNISON 5 DETUNE 0,08 WIDTH 55 ; OSC C optionnel OCT +1 WIDTH 95 coupé à 2 kHz `[DOC Monosounds]`. FILTER 1 passe-bas, CUTOFF ≈ 600 Hz balayé 400–900 Hz (« le mouvement de filtre est le hook »), RES **MUET** (20–35 `[HEUR]`). ENV 1 A 1–5 ms D 250 S 60 % R 31 ms ; ENV 2 → CUTOFF 30 %, D 200 `[DOC-2]`. Le « rave » : ENV 3 → CRS +8 st (hoover) ou −5 à −12 st balayant vers la note en 200–600 ms, ou PORTA 60–120 ms SCALED + LEGATO ; pitch bend UP 12 ; vibrato LFO 7 Hz DELAY 200 ms ; RAND 100 % ; MONO. Chaîne : Distortion Tube léger → Compressor MULTIBAND MIX 15–25 % → **un seul** élargisseur (Dimension SIZE 0 MIX 30 %) → Reverb sur BUS 1 (HPF 500, LPF 8 k) → Delay 1/4 ping-pong sur BUS 2 ; hors Serum coupe-bas 100–150 Hz et **sub séparé**. Variantes : hoover pur (3 saws-pulse ±40 cents, −12 st, PWM LFO 5 Hz, chorus lourd → phaser → reverb), big room (unison 7, detune 0,12), eurodance (0,14, filtre ouvert). Erreurs : detune et blend au maximum (« plus de centre = brouillard »), unison 16, grave demandé à la pile (sous 150 Hz les voix battent), release longue, phase fixe.

### FR-2 Plucks et arpèges
UNISON 3–4 DETUNE 0,08–0,18 (« moins d'unison qu'un lead ») ; ENV 1 A 1–4 ms D 160–260 S 0 R 80–140 (Cymatics) contre médiane mesurée D 867 ms (intention, pas erreur) ; ENV 2 → CUTOFF ouvre 30–50 % et referme en 100–250 ms, **plus rapide que l'ampli** ; filtre LP 24 600–800 Hz, RES 20–40 ; transitoire ENV 3 → CRS unipolaire decay 20 ms ; sous-couche passe-bande 1–3 kHz 12–15 dB dessous. Patch publié : `patches-genres.md` § 3 (Dist 8Bit Fwap + CrushWub, LFO 1 → CUTOFF 1/8 TRIP). Arpèges : polymètre 7/5/12 pas contre 16, delay 1/8 pointé ping-pong 40 % ; ARP interne 12 slots.

### FR-3 Basse (recette `../recipes/basse-future-rave-sub-et-mid.md`)
Sub sinus routé **Direct**, ENV A 4 ms R 30 ms, LP 90 Hz, −6 dB ; mid saw + carrée +12 st, CUTOFF 350 Hz (Warehouse) ou 600 Hz balayé (future rave), ENV D 120 S 35 R 30, env. filtre D 90 S 0, HPF 65 / LPF 350, saturation 35 % `[DOC-2 Attack]`. Off-beat : notes 60–120 ms ; rolling : première double vide, vélocités 0,95 / 0,78 / 0,6. Sidechain release 1/16 ou 1/8.

### FR-4 Kick long et toms (recette `../recipes/kick-festival-et-future-rave.md`)
Kick techno-house : sinus 50–65 Hz, decay 300–700 ms, pitch 150 → 50 Hz en 30 ms, punch 80–120 Hz 80–150 ms, clic 2–6 kHz 5–15 ms ; à 126 BPM un kick de 800 ms interdit un sub actif. Toms : 808 sinus + chute 60 ms decay 300–600 ; 909 deux triangles à la quinte ; Simmons triangle + bruit, chute 200–400 ms. **« Toms de rave » MUET** : tom 909/Simmons accordé sur tonique ou quinte, decay 300–600, fills de doubles en fin de 8 mesures, ENV → CRS +12 st sur 50–100 ms, saturation `[HEUR]`. Accorder le kick **en dernier, contre la basse** ; corrélation +1 en 30–80 Hz ; 5 ms à 100 Hz = annulation complète.

### FR-5 Accords sombres
Pile FR-1 en POLY 3–4 ; **trois notes maximum sur une supersaw** ; filtre 500–900 Hz, automation depuis 50 Hz sur chaque phrase ; stab A 5 D 250 S 0 R 31 ms, env. filtre D 160, couche corps −12 st à −14 dB (78,6 % des patchs Chords sont scindés à l'octave) ; nappe A 0,54 s R 1,8 s, LFO 1 mesure → cutoff ; voicing m7/m9/sus4 **sans fondamentale**, MIDI 55–75 ; chorus puis reverb ; OTT 15–25 %.

### FR-6 Risers (recette `../recipes/risers-impacts-downlifters.md`)
Patch chiffré : OSC A NOISE White unison 4 ; OSC B sinus −1 oct FM 30 % depuis A ; FILTER Comb 100 % wet RES 60 %, CUTOFF 100 Hz → 12 kHz sur 4 mesures ; LFO 1/8 triangle 70 % → cutoff et pan `[DOC-EXTRAIT]`. Version simple : bruit blanc passe-bande 200 Hz → 8 kHz exponentiel, RES 30 %, 8 mesures ; riser tonal qui finit **hors** de l'accord ; coupure nette au un.

### FR-7 Voix pitchée
Au-delà de 3–4 demi-tons sans préservation de formants, artefact ; UKG +2 à +5 st, G-house −2 à −4 ; Simpler Slicing ou clip Complex Pro Formants 100 % ; Serum 2 Sample/Granular ou warp `kVocode_NOISE` ; riser vocal (pas de pitch −quinte, +quinte, puis montée ; delay 1/4 30 %) ; chaîne : doubler 65 %, +2 kHz, −300 Hz, coupe < 100 Hz, multibande, clipper.

---

## 2. Bass house

### BH-1 Sub
Sinus mono, unison 1, sans detune ni chorus ; SUB osc ou OSC A pos. 0 routé **Direct** ; ENV A 4 ms D 300 S 95 R 30 ; registre MIDI 28–40 (Mi1–Mi2), F1 = 43,65 Hz ok, sous Mi1 « les enceintes lâchent » ; sub ≥ harmonique, kick > basse dans le sub ; glide 40–80 ms ; coupe-bas 20–30 Hz. Sidechain 5:1, attaque **4 ms** (anti-clic), release 60 ms. Operator natif : sinus Coarse 0,5 ; Drift : sinus oct −1 MS2.

### BH-2 Basse FM métallique, « Jauz bass », future house (recette `../recipes/basse-fm-metallique-bass-house.md`)
Serum 2 : OSC A porteuse, WARP 1 = **FM from OSC** (B modulateur, niveau de B à zéro autorisé, accordage Ratio). Ancêtre chiffré (Garage Bass, `patches-genres.md` § 2) : porteuse sinus −24, modulateur −12 (2:1), variante **−12,30** = le métallique ; filtre 25 %, env. à fond S 0 ; amp R 33 % ; mono glide 10–15 %. EDMProd : modulateur 2 octaves + quinte = **6:1** ; LFO Env sur le cutoff ; LFO 2 → quantité de FM. Ratios : entiers = harmonique ; 1:3 métallique, 2:5 inharmonique, 3:7 complexe ; cloche = non entier ≥ 4 + enveloppe rapide sur le modulateur. **Index FM MUET** : 15–25 % = râle, > 40 % = hurlant, piloter par ENV 2 D 150–300 ms et une macro. Thwack : env. de pitch +12 st → 0 en 50 ms. Chaîne : Tube léger → MULTIBAND 15–25 % → coupe-bas 100 Hz → Dimension discret → sidechain ; sub séparé. Métal « Jauz » `[HEUR]` : FINE du modulateur +20…+40 cents, ou ratio 2,5–3,5, WARP 2 = Distortion Diode.

### BH-3 Talking bass (recette `../recipes/talking-bass-formants.md`)
FILTER 1 **Formant I/II/III** (le cutoff morphe entre voyelles, VAR = FORMNT), FILTER 2 MG Low 24 en série ; ou deux Band 12 sur F1/F2 ; preset d'usine de départ « Vox/VOX - I Talk ». Formants : ee 270/2290 (390/1990 « adaptés à la basse »), eh 530/1840, **ah 730/1090**, **oh 570/840**, oo 300/870, F3 fixe 2500–3000 ; morph sur 2–4 mesures ; RES 20–40 ; petite plage de LFO ; « de oh à ah c'est un tout petit mouvement, balayer toute la course donne une démo de filtre ». Splitter L/M/H : < 120 Hz propre, 120 Hz–2 kHz waveshaping, > 2 kHz tube ; OTT ; sub séparé.

### BH-4 Wobble LFO
LFO 1 MODE **RETRIG** (ex-« Trig », fiche 3), RATE 1/8 (TRIP au besoin), SMOOTH 20–50, DELAY/RISE pour l'onset (« le wobble entre en fondu »), **HOST** (ex-« ANCHOR ») ; MATRIX LFO 1 → CUTOFF 40 % + ENV 2 → CUTOFF 60–100 % (l'enveloppe fait plus que le LFO) ; LP 24 RES 30–60 ; formes sinus / saw descendant / carrée ; **changer le rate toutes les 1–2 mesures, c'est la composition** ; à 126–128, 1/2 est trop lent, viser 1/4 ou 1/8 ; distorsion après le filtre.

### BH-5 Reese
Deux saws désaccordées mono/legato, sub sinus séparé non désaccordé ; detune ±27 (Attack) à ±61 (MusicRadar), **médiane mesurée 16,6 cents** → FINE +17 ; LP 24 700 Hz RES 25, LFO 1 mesure 35 % (« un Reese statique est un échec ») ; ENV S 1 R 24 ms ; **RAND 0 %** (reset de phase) ; chorus 30 ms rate ≈ 0 depth max mix 60 % ; Splitter L/H 400 Hz : Tube 30 % en bas, Tape Sat 65 % en haut ; EQ creux 1,6–3,8 kHz, bosse 450–800 Hz. Jamais en rôle de sub.

### BH-6 Growl (recette `../recipes/drop-bass-house-trois-couches.md`)
Mid-bass coupé à 100 Hz sur sub séparé. WT POS modulée par LFO 10–60 Hz ou stepper 1/16 → distorsion → comb ou phaser → **resample** → repitch, filtre, distord → 3–5 passes ; formants RES 20–40, warp Bend 30–50 = nasal, FM 15–25 = guttural, > 40 = hurlant ; unison 1 pendant la conception. Patch mesurable BassGorilla : `basses.md` § 3. Multibande : < 120 / 120–2 k / > 2 kHz, mid = le growl (tanh + hard clip), OTT 30–50 % par canal, 15–30 % sur bus. Presets d'usine Serum 2 de départ : Bass/Hard/**BA - Basilisk**, Bass/Modulated/**MDL - Slippery Snake**, Bass/Hard/**BA - RM Wub Generator**, Bass/Reese/**BA - Gnarly Reese**, Lead/**LD - Das EDM** `[DOC]`. Rythme timbral : quatre gestes différents par cellule de 2 mesures.

### BH-7 Basse « Chris Lake », courte, filtrée (recette `../recipes/basse-tech-house-rolling-chris-lake.md`)
MG Low 24, ENV 2 → cutoff, coupé au-dessus de 200–300 Hz ou cutoff ≈ 140 Hz ; ENV 1 D ≈ 1,2 s S −10 dB ; ENV 2 D 200 ms S 0 → cutoff 5 %, → RES 10 % ; **vélocité → cutoff à courbe raide** (« le secret du bounce, confirmé par trois tutoriels ») ; DRIVE 20–40 % ; saw + sinus −1 oct, ou carrée + saw haute résonance `[DOC-EXTRAIT The Producer School, Mystic Alankar]`. Pattern off-beat avec octave sur les temps, phrases de 4, vélocité 100–115 sauf accents 120+.

### BH-8 Stabs, BH-9 Chops, BH-10 Drop en couches
Stab = stab house (H-3) joué par le patch FM ou growl ; mono, Stack **12+7** ; reverb **avant** la distorsion (Attack : Reverb → Overdrive 13 % → Saturator 10 dB → Drum Buss 26 %). Chops : rap pitché −2/−4 st, 100–300 Hz, intro et builds ; Beat Repeat Interval 1 bar Gate 7/16 Grid 1/16. Drop en couches : sub LP 90–100 Hz sans aucun traitement ; mid HPF > 100 (79 Hz Q 0,7) LP 400–500, saw + carrée ; growl 500 Hz–2 kHz, saws 17 cents 3 voix, notch −8 dB 2,5 kHz, +3 dB 600 Hz ; air > 2 kHz facultatif (« une quatrième couche = sept sons qui se battent ») ; **toutes les couches jouent le même rythme, mêmes LFO** ; le HPF du mid reste **sous** la note jouée (78 Hz pour F2, pas 105) ; alternative : un seul oscillateur scindé à 130 Hz plutôt que deux sinus. Serum 2 en une instance : OSC A sinus → Direct ; OSC B → FILTER 1 480 Hz ; OSC C unison 3 → FILTER 2 1,8 kHz ; LFO 1 sur les deux cutoffs ; Splitter L/M/H 120 Hz / 2 kHz avec Distortion par bande ; Utility MONO BASS 120.

---

## 3. House : future house, tech house, big room

### H-1 Basse organ M1 (recette `../recipes/organ-bass-et-piano-house-m1.md`)
Organ 2 = ton d'orgue percussif à cycle unique joué **mono dans le grave** ; multisample fidèle (ENV A 0–2 ms, D 150–300 stab ou S 60–80 % R 20 ligne) ; additif : sinus aux harmoniques 1, 2, 3, 4 avec la **3e en avant** (tirettes 88 8000 000), key-click 5–15 ms ; EDMProd : triangle −2 oct + carrée +7 st ; registre MIDI 36–48.

### H-2 Piano house M1
Brillant, attaque dure, **2e et 3e harmoniques fortes, fondamentale faible**, decay 400–800 ms, HP 200–300 Hz, +1–3 kHz, plate 1–1,5 s, gate serré ; stabs sur les contretemps (pas 2, 6, 10, 14), accords 7e/9e, voicings sans tonique ; approximation Operator ratio 1:1 index décroissant `[HEUR]`.

### H-3 Stabs et accords (recette `../recipes/stabs-house-et-tech-house.md`)
Dotbeat mesuré : 2 saws +10 cents, unison 3, cutoff 320 Hz, A 5 D 250 S 0 R 31, env. filtre D 160, vélocité → filtre 0,35, couche corps −12 st, swing 56 %. Attack : OSC 0/+3/+7 (triade dans le patch, une touche = accord), LP 4 pôles fermé piloté par l'enveloppe. Techno Stabs (Hive) : A 0 D 66 S 0 R 29, filtre A 5 D 48 S 9 R 24 (unité ms ou 0–100 : contradiction). Deep house KVR : cutoff 250–350, « c'est le decay qui fait le stab ». Serum 2 : SEMI 0/+3/+7 ou Stack 12+7, FILTER 1 MG Low 24 300 Hz, ENV 2 → CUTOFF 80 % D 160 S 0, ENV 1 D 250 R 31, Reverb sur BUS. Erreurs : attaque 10–30 ms (« consensus zéro »), triades nues, fondamentale doublée.

### H-5 Basse tech house rolling (recette `../recipes/basse-tech-house-rolling-chris-lake.md`)
Consensus des dix recettes : deux oscillateurs à l'octave (ou octave + quinte), LP parqué **80–200 Hz** ouvert par une enveloppe rapide, sustain nul ou court, distorsion post-filtre, sidechain obligatoire, mono/legato. SoundBridge : carrée + saw, phase random off, LP 24 150 Hz RES 0, ENV 2 → cutoff « petite quantité », distorsion 8 dB post-filtre, +10 dB à 75 Hz ; A 0 D 150–300 S 20–40 R < 100. Wavetable natif : release réduite (600 ms par défaut = boue), filtre **12 dB**, Env 2 → cutoff decay court. Warehouse (Attack, 3 couches) : sub LP 80 Hz, ligne HPF 65 LPF 350, première double vide, sidechain release lente « pour le swing ». Tracey Brakes Serum 2 : High 12 913 Hz RES 22, unison 7 detune 0,15, OCT −3 sur sub séparé (couche haute du même son).

### H-6 Big room lead (recette `../recipes/lead-big-room-supersaw.md`)
Couche principale saw UNISON 7 DETUNE 0,20–0,30 (Myloops) ou 0,12 (Monosounds), HPF 200 Hz, +2/+3 dB à 3 kHz, WIDTH 60–80, A 4 D 250 S 0,6 R 31 ; couche +12 (3–5 voix, HPF 500, 6–10 dB dessous) ; sous-octave mono LP 1 kHz optionnelle ; air = NOISE +4 octaves, même unisson, HPF 3 kHz ; pluck big room A 1–4 D 160–260 S 0 R 80–140, gated reverb 0,5–1 s ; automation de cutoff sur 24 + 8 mesures qui s'ouvre pile au drop ; sidechain 2–3 dB ; EQ notch 1,6–3,8 kHz, bosse 450–800 ; drop = kick + basse + **un motif** de 3 notes maximum ; second drop +1–2 st ou octave.

### H-7 Kick de festival (recette `../recipes/kick-festival-et-future-rave.md`)
909 sous forte compression + saturation, mêlé à un 808 plus profond, couche de caractère (707, LinnDrum, DMX), kick long accordé, grave du kick snappy coupé sous 150–250 Hz `[DOC-EXTRAIT Attack]` ; trois couches sub 30–80 / corps 100–150 / clic 2–5 kHz ; phase 0° à chaque trigger ; 808 natif 49,5 Hz = Sol1, rester ≥ Mi1 ; tonique ou quinte, ou hors de la bande de la basse (arbitrage) ; clipper dur à 0 dB sur le kick et sur le groupe kick + clap ; facteur de crête du bus batterie 12–16 dB. Serum 2 : OSC A sinus, ENV 2 → CRS +24…+36 st decay 20–40 ms, ENV 1 D 250–500, NOISE one-shot 5 ms + FILTER 2 HP 2 kHz.

### H-8 Claps, H-9 Hats, H-10 Bruit
Clap : bruit → passe-bande 1 kHz, 3–4 bursts espacés 8–16 ms, queue 100 ms, identité 1–2 kHz, HPF 130–140, mono, delay 1/16 feedback 7 pour doubler, gated reverb 0,5–1 s. Hats : 808 = six carrées ratios 1 / 1,34 / 1,61 / 1,99 / 2,44 / 2,79 × 320 Hz HP 6–8 kHz, fermé 30–60 ms, ouvert 300–600 ; 909 open hat sur le contretemps = **le** marqueur house ; HPF 800 Hz (Fearvox) à 3 kHz (deep) ; moyenne des hats −37 à −41 dB ; alternance de vélocité ~80/~100, ghosts 40–60 %, choke group. Bruit de fond : bus dédié, HP 300 Hz, hors sidechain et hors compression master (fiche 29) ; shaker = bruit > 6 kHz en doubles à 40–60 %.

### H-11 Impacts, H-12 Downlifters
Impact = grave sinus 60 → 30 Hz decay 1–2 s + sub-drop 80 → 25 Hz sur 0,5–2 temps + burst médium + clic + crash, **crêtes alignées au début**, quasi mono, reverb inversée avant ; sur le un du drop avec le mix complet. Downlifter = même source que le riser, pitch −12 à −24 st sur 1 mesure, LP qui se ferme, posé sur le **premier temps** de la nouvelle section ; riser et downlifter se croisent sur la dernière mesure ; tape stop 200–600 ms ; Serum 2 LFO Mode Env → CRS −24, ENV BPM 1 bar, NOISE Brown. Deux vrais silences par morceau.

---

## 4. Conversions vers Serum 2

| Massive, Sylenth1, Spire, autres | Serum 2 | Statut |
|---|---|---|
| Massive Sin-Squ position | Basic Shapes WT POS 0 → carrée | `[HEUR]` |
| Massive Bend ± | WARP Bend +/− (50 % neutre) | `[DOC]` |
| Massive oscillateur Phase Modulation | WARP 1 = PD from OSC ou FM from OSC ; source active, niveau 0 autorisé | `[DOC]` |
| Massive Performer / Stepper | LFO GRID + Shift-clic (marches) | `[DOC]` |
| Massive Daft, Lowpass 4, Scream, Comb | MG Low 24 ou French LP `[HEUR]` ; MG Low 24 ; Scream LP/BP ; Comb ± | `[DOC/HEUR]` |
| Massive Classic Tube, Dimension Expander | Distortion Tube ; Hyper/Dimension UNISON 0 + SIZE | `[DOC]` |
| Massive Unisono Pitch Cutoff | UNISON + DETUNE × RANGE (Global) ; course et sens de RANGE **MUET, à mesurer** | `[TEST]` |
| Restart via Gate, phase restart | PHASE 0°, RAND 0 % | `[DOC]` |
| Glide 10–15 % / 30 % | PORTA 40–80 ms / 60–120 ms `[HEUR]`, SCALED | `[HEUR]` |
| Sylenth1 unison 8 / detune 0–10 | UNISON 8 ; pas de conversion numérique publiée (le detune max dépend du nombre de voix) | `[DOC-EXTRAIT]` |
| Serum 1 OTT | Compressor MULTIBAND, Depth = MIX ; crossovers **MUET** | `[DOC]` |
| Diva Garage Bass filtre 25 % | CUTOFF à 25 % de la course ≈ 140–200 Hz `[HEUR]`, ENV 2 → CUTOFF +100 | `[HEUR]` |
| JP-8000 (Szabo) | UNISON 7, Tuning Super `[HEUR]`, BLEND 75, RAND 100 | `[DOC/HEUR]` |
| Unités de detune en circulation | Serum 0,08–0,30 ; cents 10 (leads), 17 (basse), 18 (nappes), 20 (plucks), ±27–61 (Reese) ; % de bouton : **non convertibles** sans mesure | `[DOC-2]` |

Règle (fiche 34) : ne pas transposer une recette Serum 1 telle quelle ; Quality change les warps FM et PD.

## 5. Contradictions notables (vingt dans le rapport)

Qui tient la fondamentale en bass house (trois positions) ; ratio FM EDMProd 6:1 et non 3:1 ; unités de detune ; nombre de voix d'unison (7 est le centre, 9+ = empilement) ; Reese ±7 à ±61 cents ; enveloppe de pitch de la 909 (SOS 200–500 ms contre amen 15–30 ms, le circuit 808 mesuré donne raison à amen : à trancher à l'oreille) ; attaque des stabs 0 ms contre anti-clic (0–4 ms avec PHASE 0) ; mono 100 à 250 Hz (crossover sub/mid 75–100 Hz, HPF du mid sous la note) ; sidechain 3:1 à 20:1 (4 ms d'attaque est le seul chiffre justifié) ; swing house 50–80 % selon le sous-style ; accord du kick tonique/quinte contre hors bande ; glide 808 80–300 ms ; OTT 15–60 % ; « Vogue = Organ 2 » faux ; acid 303 (le patch statique n'existe pas).

## 6. Muet

Le patch du lead future rave de Guetta et MORTEN (résonance, quantité de pitch env, portamento) : analyser une référence avec `../../synthese-reference/SKILL.md` ; les « toms de rave » ; l'index FM des basses Jauz et future house ; le mapping DETUNE × RANGE et la courbe Tuning Super de Serum 2 ; les crossovers de l'OTT ; le tutoriel « Shark Attack » et les basses Dom Dolla et Fisher (vidéos seulement).
