# Synthés dans Serum : synthèse de 90 tutoriels (lead, pluck, hook, accords, pad, drone)

Cette page résume `tutoriels-synths-serum.md` : six types de synthés, quinze vidéos chacun. Lead (LE-01 à LE-15), Pluck (PL-), Hook (HO-), Accords (CH-), Pad (PA-), Drone (DR-). Priorité house, puis drum and bass, puis dubstep.
L'étude a été faite le 05/10/2026 dans Claude in Chrome sur le Mac, son coupé. Les transcriptions YouTube et les descriptions ont été lues. **Rien n'a été entendu** : un timbre décrit ici est le mot du présentateur, jamais une écoute.
[SOURCE XX-nn] = dit dans la vidéo. (interp.) = interprétation de l'étude ou de cette synthèse. [ASR ?] = passage douteux de la reconnaissance vocale.
Versions : 19 vidéos sont en Serum 2 (LE-05, LE-11, LE-12, LE-14, PL-02, PL-03, HO-04, HO-07, PA-04, PA-10, PA-14, DR-04, DR-06 à DR-12). La version n'est pas sûre pour LE-02, HO-05 et PA-08. Les 68 autres sont en Serum 1, dit ou déduit de l'interface. Aucune fiche d'accords n'est en Serum 2.
Doublons : 90 fiches, 87 vidéos. HO-05 = CH-05, HO-10 = CH-09, CH-11 = PA-09 (même URL).
Les noms de contrôle ont été comparés à `serum2-cartographie.md` (§ 3.1, § 4, § 6, § 7, § 8, § 13). Les écarts sont listés à la fin de chaque section. Notes : C3 = 60, le numéro MIDI fait foi.

## Ce que dit le corpus avant tout

- **L'enveloppe fait le type.** Pluck, stab et hook : sustain à 0 et decay court, sur l'ampli et sur le cutoff [SOURCE PL-05, PL-07, CH-01, CH-06, HO-05]. Pad et drone : attaque lente, release long [SOURCE PA-07, PA-11, DR-14].
- **Le rythme peut venir d'un LFO, pas du MIDI.** Accords tenus et LFO en Trig sur le cutoff [SOURCE PL-06] ; LFO « pluck » en Hz piloté par macro [SOURCE PL-03, PL-14] ; pad à LFO 1/16 [SOURCE PA-04, PA-06].
- **Un coup de pitch à l'attaque.** Enveloppe ou LFO très court vers le Master Tune ou le coarse [SOURCE PL-01, PL-04, PL-11, HO-10, LE-08]. Variante : un bruit en one-shot (Kick Attack, Guitar Mute 2) [SOURCE PL-05, PL-15, PA-15].
- **Un oscillateur muet comme modulateur.** Level à 0, il ne sert qu'à la FM ou à la PD [SOURCE LE-07, LE-14, LE-15, PL-05, HO-10, DR-15]. La cartographie le confirme : la source doit être active, son niveau peut être à zéro (§ 4.2).
- **Centre étroit, couche large.** Osc A à une voix, osc B une octave au-dessus en unison 7 [SOURCE PL-12, PL-13, LE-06] ; unison impair pour garder une voix centrale juste [SOURCE PL-10, DR-11]. Sub à part en Direct Out [SOURCE PL-11, LE-12, DR-12, PA-15]. (interp.) Compatible avec la règle du projet : sub mono dans un instrument séparé.
- **Les effets internes font une grande part du son.** Hyper/Dimension, distortion, multiband ou OTT et reverb filtrée reviennent presque partout. Le mix de la reverb est souvent modulé par une enveloppe ou un LFO [SOURCE LE-06, LE-09, CH-06, PA-15].

## Lead

- **Oscillateurs** : saw en unison 7 [SOURCE LE-07, LE-10], ou deux tables à des intervalles : +4 / +7 st [SOURCE LE-03], −3 oct / −1 oct +4 st [SOURCE LE-12]. Couche +1 octave en unison 2 pour la seule largeur [SOURCE LE-06].
- **Warps** : Sync [SOURCE LE-03, LE-09, LE-14] ; FM depuis un osc muet [SOURCE LE-07, LE-15] ; PD [SOURCE LE-05, LE-11, LE-14] ; Bend [SOURCE LE-05, LE-14].
- **Filtre** : MG Low 24 [SOURCE LE-05], Low 18 [SOURCE LE-07] ou MG Low 18 [SOURCE LE-08], ouvert par une enveloppe, drive et Fat montés. Autres : Flanger négatif [SOURCE LE-04], Misc Reverb keytracké [SOURCE LE-15].
- **Enveloppes** : ENV2 → semitones et Master Tune, en unipolaire, pour le « whoop » afro [SOURCE LE-01] ; ENV2 très courte → drive pour la percussion [SOURCE LE-08].
- **LFO** : mode Envelope → Master Tune pour un punch ou un saut d'octaves [SOURCE LE-03, LE-08] ; un LFO d'une mesure qui fait tout bouger [SOURCE LE-04, LE-13] ; vibrato vers fine ou Master Tune [SOURCE LE-06, LE-13].
- **Voicing** : mono, souvent legato [SOURCE LE-02, LE-03, LE-12, LE-13].
- **FX** : distortion (Diode 2, Tube pre-HP, Soft Clip, Hard Clip), Hyper/Dimension, multiband, delay avant reverb ; reverb qui monte pendant la tenue [SOURCE LE-06, LE-09].

| Paramètre | Valeur | Source |
|---|---|---|
| Saw future house | unison 7, random phase 0 sur A et B | LE-07 |
| ENV2 → cutoff (Low 18) | decay ≈ 2,6 s, sustain ≈ 17 %, release ≈ 380 ms | LE-07 |
| Tube en pré-filtre | passe-haut ≈ 300 Hz, drive poussé, mix plein | LE-07 |
| Saw future rave | unison 16, random 0, detune 0 ; ENV2 ≈ 50 ms → drive | LE-08 |
| Bass house, lead 1 | osc A +4 st, WT ≈ 55 ; osc B +7 st, Sync ≈ 1,9–2 % ; ENV1 attack ≈ 60 ms | LE-03 |
| Bass house, pitch | LFO1 → Master Tune +1 ; LFO2 → +24 (2 octaves) dosé par Macro 1 | LE-03 |
| Bass house, lead 3 | FM from B 53 % ; noise « Kick Attack 29 » one-shot | LE-03 |
| LFO de transformation | rampe, 1 bar, forme qui finit à 3 temps | LE-04 |
| Lead afro 1/16 | sustain 0, mono ; decay ≈ 150 ms → cutoff | LE-02 |
| Supersaw DnB | unison 7 ; release 200–400 ms ; MIDI en croches | LE-10 |
| Stab carré DnB | triangle −7 st + square +2 oct ; Low 24 ≈ 1000 Hz ; distortion PRE HP 200–300 Hz | LE-10 |
| Lead neuro | FM 30 ; DX Brass 2 −1 oct, WT ≈ 35 ; Splitter ≈ 500 Hz ; Convolve size 30–40 ; Flip ≈ 5 % | LE-12 |
| Melodic dubstep, LFO1 | 1 bar, trigger ; → WT 8, → level sub 17, → drive ≈ 55 | LE-13 |
| Flange −1 (filtre FX) | cutoff 289 Hz, res 64 %, drive 25 %, mod 70 ; vibrato LFO2 → Master Tune 1, 1/16 | LE-13 |
| Brostep | Sync ≈ 1,10 % [ASR ?] ; LFO1 → level 90 %, → Bend− 60 % ; PD from C 30 % | LE-14 |
| Robot lead | Hyper ≈ 30 %, unison 7 ; Dimension ≈ 20 % ; delay ≈ 20 ms, mix ≈ 70 %, sans feedback | LE-15 |
| Delay melodic house | 1/8 pointée + 1/8 | LE-05 |

- **House** : afro = whoop par enveloppe de pitch, leads rythmiques mono [SOURCE LE-01, LE-02] ; bass et tech house = sync ou FM, Diode, mi-basse mi-lead [SOURCE LE-03, LE-04] ; future house et future rave = saw large dans un filtre drivé [SOURCE LE-07, LE-08] ; melodic = dérive de pitch, reverb modulée [SOURCE LE-05, LE-06].
- **DnB** : supersaw et stab carré [SOURCE LE-10] ; square « 8-bit » dont le volume respire à la noire [SOURCE LE-11] ; lead neuro désaccordé, legato, Splitter [SOURCE LE-12].
- **Dubstep** : un LFO d'une mesure pilote tout [SOURCE LE-13, LE-14] ; filtre Reverb keytracké et delay de 20 ms [SOURCE LE-15].
- Lire d'abord : LE-07, LE-03, LE-05, LE-13.
- Écarts : « Global Master Tune » de Serum 1 = **Main Tuning** (Global) en Serum 2 ; vaut pour tout ce document (§ 3.1, § 7.4). « FM from B » = **FM (B)** (§ 4.2). LE-11 dit que la PD « s'appelait FM » dans Serum 1 : la cartographie garde FM et PD comme deux modes, la PD est nouvelle.
- Écarts : modes de LFO Serum 1 « Trig », « Env », « Off » = **RETRIG**, **ENVELOPE**, **FREE** (§ 7.2). « Negative Flanger » (LE-04) et « Flange −1 » [ASR ?] (LE-13) = famille Flanges, variante « − » (§ 6). « WSP » (LE-12) = **Wsp**, type New, VAR = MORPH : cohérent avec le « morph » dit. « Tape » (LE-12) = **Tape Sat.**
- Contradiction : valeurs de Sync dites en % très éloignées (≈ 2 % LE-03, ≈ 1,10 % LE-14, ≈ 140–150 % HO-15). La cartographie donne un bouton 0–1 (§ 3.2) : unité affichée à vérifier. La « section du dessous » de LE-14 serait le fader WARP Var, douceur du sync (§ 4.1) (interp.).

## Pluck

- **Oscillateurs** : saw par défaut ou Basic Shapes ; sinus propre pour les plucks marimba [SOURCE PL-04, PL-05, PL-09, PL-15]. Deux couches : centre à une voix + octave en unison 7 [SOURCE PL-12, PL-13].
- **Enveloppes** : sustain 0 ou bas, decay de quelques centaines de ms ; même forme (ou ENV2) sur le cutoff [SOURCE PL-05, PL-07, PL-10].
- **Filtre** : MG Low 24 fermé avec drive [SOURCE PL-01, PL-03, PL-05, PL-12, PL-13] ; MG Low 18 [SOURCE PL-07] ; MG Low 12 [SOURCE PL-14].
- **Attaque** : ENV3 ultra-courte → Master Tune [SOURCE PL-01, PL-04, PL-07] ; LFO2 descendant en mode Envelope → Master Tune [SOURCE PL-11] ; noise one-shot [SOURCE PL-05, PL-15].
- **LFO moteur** : rampe descendante en Hz → levels + cutoff [SOURCE PL-03] ; LFO Trig sur le cutoff [SOURCE PL-06] ; LFO « en aile » → levels, cutoff, drive [SOURCE PL-14].
- **Expression** : vélocité → cutoff ou en aux source, notes douces plus sombres [SOURCE PL-01, PL-02, PL-07] ; macros automatisées contre le son statique [SOURCE PL-02, PL-03, PL-07, PL-13].
- **FX** : multiband « qui ajoute du clic » [SOURCE PL-05], Hyper/Dimension, delay, reverb à low cut [SOURCE PL-10, PL-12].

| Paramètre | Valeur | Source |
|---|---|---|
| Osc deep house | A : BD Sine −5 st, FM (Sub) 18 %, level 63 ; B : square −5 st, unison 2, FM 36 % | PL-05 |
| MG Low 24 | cutoff au minimum, res 0, drive 37 % | PL-05 |
| ENV1 / ENV2 | decay 433 / 298 ms ; release 320 / 220 ms ; ENV2 → cutoff 75 | PL-05 |
| ENV3 → noise ; LFO1 « knock » | decay 65 ms, release 13 ms, quantité 68 ; LFO1 → coarse A et B 45, → cutoff 100 | PL-05 |
| Reverb Hall | size 34, decay 3,4 s, low cut 30, high cut 63, mix 22 | PL-05 |
| ENV1 melodic house | decay 840 ms, sustain −9,5 dB, release 542 ms | PL-07 |
| MG Low 18 | cutoff 138 Hz, res 0, drive 29 ; ENV2 → cutoff 72 | PL-07 |
| Delay / reverb | 1/8 – 1/8, 816 Hz, Q 0,8, mix 36 % / size 37 %, decay 5,4 s, wet 41 % | PL-07 |
| ENV3 → Master Tune (marimba) | decay ≈ 20 ms, sustain 0, release 0 | PL-04 |
| LFO pluck afro | saw pos 2 + square pos 4, niveaux ≈ 30 % ; B unison 8, detune ≈ 27 ; cutoff ≈ 280 Hz ; rate ≈ 0,8 Hz [ASR ?] | PL-03 |
| Reverb du LFO pluck | Hall, decay ≈ 7 s, size ≈ 50 %, low cut ≈ 80 Hz ; EQ low shelf −7 dB | PL-03 |
| Trémolo afro | LFO1 → fine, 1/128 ; dosé par Macro 2 | PL-02 |
| LFO WT afro | 0,7 Hz, Trig ON ; WT ≈ 52 | PL-08 |
| Pluck liquid | unison 9 ; Low 24 ≈ 142 Hz, quantité 46 | PL-10 |
| Pluck-basse liquid | distortion PRE, passe-haut ≈ 400 Hz | PL-11 |
| Pluck repeater | 5,6–5,7 Hz (croche), 3,8 (croche pointée), 2,8 (noire) ; attack ≈ 5 ms ; pitch bend +2 st | PL-14 |
| Pluck Au5 | Bend+ ≈ 20 ; Downsample drive 22, mix ≈ 30 ; B unison 7, detune ≈ 0,04 | PL-15 |
| Pluck future bass | attack ≈ 3,8 ms [ASR ?] ; compresseur 4:1, ≈ −12,7 dB | PL-13 |

(interp.) PL-14 ne dit pas le tempo. 5,67 Hz pour une croche correspond à ≈ 170 BPM (croche : Hz = BPM ÷ 30).

- **House** : deep sombre, noise et Note On Rand [SOURCE PL-01, PL-05] ; afro avec Clip, triolets, LFO pluck [SOURCE PL-02, PL-03, PL-08] ; melodic et progressive très automatisés [SOURCE PL-06, PL-07] ; future house en sinus marimba [SOURCE PL-04].
- **DnB** : WT dessinée et morph [SOURCE PL-09] ; EQ dont la fréquence suit la note [SOURCE PL-10] ; plucks-basses graves, à la limite de la catégorie [SOURCE PL-11, PL-14].
- **Dubstep** : couche centrale + octave large [SOURCE PL-12, PL-13] ; Downsample dosé au point près [SOURCE PL-15]. Aucun pluck riddim.
- Lire d'abord : PL-05, PL-07, PL-03, PL-10.
- Contradiction : PL-13 juge le 24 dB meilleur que le 12 dB ; PL-14 prend MG Low 12 ; PL-07 corrige 24 en 18.
- Écarts : PL-02 utilise le **Clip** de Serum 2 (§ 10, `serum2-fx-clip-arp.md`) ; « KB span mono » [ASR ?] = KB Span et peut-être Trigger Mode Mono (interp.). PL-03 bascule le LFO en **HZ** (§ 7.2). PL-04 « Square-ify » : aucun warp de ce nom (§ 4.1). PL-01 « band (B+) » [ASR ?] : Bend + probable (interp.). PL-09 « Sine Shaper » existe en FX Distortion (§ 8).

## Hook

- **Intervalle** : deux oscillateurs à un intervalle, accord de deux notes [SOURCE HO-05, HO-06, HO-08].
- **Caractère** : Sync ou FM modulés par une enveloppe ou un LFO en mode Envelope [SOURCE HO-02, HO-04, HO-12, HO-15].
- **Filtres** : MG Low 12 très fermé, Fat haut [SOURCE HO-01] ; Low 12 résonant keytracké [SOURCE HO-03] ; Multi Band + Notch croisés [SOURCE HO-09] ; Misc Reverb keytracké [SOURCE HO-11, HO-13].
- **Pitch** : ENV → Master Tune, range 12, sur une mesure [SOURCE HO-05] ; LFO raide → coarse −10 pour le « wow » [SOURCE HO-09] ; départ à −12 st [SOURCE HO-07].
- **Voicing** : mono, legato, portamento [SOURCE HO-04, HO-11, HO-14, HO-15].
- **FX** : distortion forte (Asym à fond, Tube, Diode PRE), multiband ou OTT doublé, Hyper après la distortion [SOURCE HO-03, HO-08, HO-12].

| Paramètre | Valeur | Source |
|---|---|---|
| Horn Fisher, osc | A unison 7, detune ≈ 0,08, level 0 ; B unison 7, detune ≈ 0,41 ; random au max ; noise 35 | HO-01 |
| Horn Fisher, filtre | MG Low 12, cutoff ≈ 40 Hz, res 0, drive ≈ 30 %, Fat 92 % | HO-01 |
| Horn Fisher, EQ interne | 155 Hz, Q ≈ 35 %, +8,1 dB ; 2939 Hz, Q 46 %, +1,7 dB | HO-01 |
| Horn Fisher, autre recette | unison A 8, B 6 ; LFO1 Envelope 1/4 | HO-02 |
| Sync funky | ENV2 → Sync A 27 %, B 15 % ; ENV1 release ≈ 7 ms ; reverb ≈ 5 % ; chorus ≈ 20 % | HO-04 |
| Rave stab | ENV → Master Tune range 12, 1 mesure, bipolaire ; intervalle « −2 / +10 » ; LP 18 | HO-05 |
| Screech bass house | level B ≈ 37 % ; LFO Trig 1/2 ; Hyper ≈ 9 %, Dimension size ≈ 2 %, mix 68 → 46 | HO-03 |
| Lead tech house | saw −1 oct −7 st + square +1 oct ; Distortion Asym drive max | HO-08 |
| Lead tech house | LFO2 → fine 1/64 ; pitch de départ −12 st | HO-07 |
| « Wow » DnB | unison 16 et 8 ; LFO → coarse −10, unipolaire | HO-09 |
| Hook d'intro DnB | unison 14 ; attack ≈ 140 ms, release ≈ 3 s ; WT par voix ≈ 30 ; porta ≈ 100 ms ; filtre Reverb ≈ 100 Hz | HO-11 |
| Hook d'intro, pitch | LFO2 → Master Tune 1, bipolaire, 2 bars, Envelope ; reverb ≈ 50 % | HO-11 |
| Jump up | 175 BPM ; oct −2, WT 2, Sync ≈ 8 ; Diode 1 PRE + passe-haut | HO-12 |
| Spirit lead | porta ≈ 31 ms ; Low 24 ≈ 9 kHz ; noise → coarse ≈ 25 % ; LFO1 → level −45, 1/16 ; vibrato 2 % | HO-14 |
| Spirit lead, FX | multiband −10 / −13 dB, 1:4 ; EQ passe-haut 600 Hz ; reverb Plate mix 50 % | HO-14 |
| Sync lent | porta ≈ 80 ; Sync ≈ 140–150 % ; LFO ≈ 20–25 % ; distortion ≈ 75 % ; multiband ≈ 5 dB, ≈ −12 dB | HO-15 |
| Stab DnB | EQ boost ≈ 500 Hz, Q bas | HO-10 |

- **House** : horns tech house, distortion forte, OTT [SOURCE HO-01, HO-02, HO-06, HO-08] ; rave stab avec pitch sur une mesure [SOURCE HO-05] ; screech bass house keytracké [SOURCE HO-03] ; sync funky [SOURCE HO-04].
- **DnB** : pitch et filtre croisés pour le « wow » [SOURCE HO-09] ; FM sinus, harmoniques dessinées, couche de percussion [SOURCE HO-10] ; hook d'intro large et descendant [SOURCE HO-11] ; riff jump up médium-grave [SOURCE HO-12].
- **Dubstep** : quatre couches, lead sec devant, pluck réverbéré, couche legato, ring mod [SOURCE HO-13] (170 BPM, La majeur) ; cri par Noise OSC → coarse [SOURCE HO-14] ; Sync lent [SOURCE HO-15].
- Lire d'abord : HO-02, HO-05, HO-09, HO-13.
- Contradiction : HO-10 et CH-09 sont la même vidéo. Le 2e LFO va au coarse pitch (HO-10) ou au rate du LFO1 (CH-09) : « core speech » [ASR ?]. À trancher à l'écran.
- Écarts : HO-14 met la distortion « avant Hyper/Dimension (défaut) » ; la cartographie dit que l'ordre d'usine de Serum 1 met Hyper en premier (§ 8). HO-11 règle l'étalement de WT par voix dans l'onglet Global (Serum 1) : en Serum 2, **WT POS** des réglages d'unison du panneau d'osc (§ 3.1).
- Écarts : HO-04, « curseur qui lisse les bords de la wavetable » : fader **WARP Var** du Sync (§ 4.1) ou « Smooth Interpretation » de WT POS (§ 3.2) (interp.). HO-09 « BN » = Multi BN, 2e cutoff = **VAR FREQ** (§ 6) : cohérent avec « même LFO inversé ». HO-13 « Ring Mod 2 » = **Ring Modx2** (§ 6). HO-14 « Create Vibrato » existe dans le menu de la matrice (§ 7.4).

## Accords

- **Deux voies.** L'accord est dans le patch, une touche suffit : osc à +3 et +7 st [SOURCE CH-01], intervalle entre deux osc [SOURCE CH-05], quinte et octaves dans l'éditeur de WT [SOURCE CH-09], sinus empilés pour l'orgue [SOURCE CH-04]. Ou bien l'accord est joué en MIDI sur un patch simple [SOURCE CH-02, CH-03, CH-08, CH-10, CH-11].
- **Oscillateurs** : saw, sinus, FM (FM_Freak) [SOURCE CH-02] ; sub saw comme fondamentale [SOURCE CH-01, CH-06].
- **Filtre** : fermé, ouvert par une enveloppe courte pour le stab [SOURCE CH-01, CH-03, CH-06] ; attack d'enveloppe pour un balayage montant en liquid [SOURCE CH-11].
- **Pitch et dérive** : ENV → fine, petit glissement [SOURCE CH-03] ; ENV3 → coarse −22 [SOURCE CH-07] ; fine opposés ≈ −5 / +5 [SOURCE CH-01] ; LFO lent en Hz sur fine et Bend [SOURCE CH-06].
- **Largeur** : unison, ou pan aléatoire par note (Note-On Random → pan) à la place de l'unison [SOURCE CH-08].
- **FX** : chorus, distortion légère (Tape, Downsample), delay 1/8, reverb courte ou dont le mix suit ENV2 [SOURCE CH-01, CH-03, CH-06].

| Paramètre | Valeur | Source |
|---|---|---|
| Stab 90s, osc | sub saw ; osc A +7 st ; osc B +3 st ; A unison 5 ; fine ≈ −5 / +5 | CH-01 |
| Stab 90s, FX | Tape drive ≈ 15 % ; delay 1/8 ping-pong ; reverb Hall mix ≈ 16 % | CH-01 |
| Stab deep house | ENV1 attack ≈ 10–11 ms, sustain 0, decay ≈ 500 ms ; flanger ≈ 1/3 ; EQ ≈ 150 Hz | CH-02 |
| Stab garage / minimal | sinus −1 / +1 oct, unison 4, detune ≈ 10 ; cutoff ≈ 100 Hz, ENV1 ≈ 40 ; attack 5 ms | CH-03 |
| Stab garage, FX | Downsample avant le filtre, mix ≈ 30 ; reverb ≈ 4 s ; delay 1/8 ; Am7, vélocité ≈ 80 | CH-03 |
| Orgue M1 | osc B +2 oct ; attack 5 ms, hold ≈ 50 ms, decay 1 s, sustain 0 | CH-04 |
| Orgue, filtre et WT | MG Low 12 cutoff ≈ 100, ENV1 ≈ 30, res ≈ 25 ; distortion ≈ 25 ; reverb ≈ 3 s ; harmonique 2/3 ≈ 30 | CH-04 |
| Stab melodic house | osc B +7 st, warp Bend +/− ; sub saw −1 oct ; delay 1/8 et 1/16 ping-pong | CH-06 |
| Accord future house | unison 9 sur A et B ; MG Low 24 ; ENV3 → coarse −22 | CH-07 |
| Keys liquid | sinus + sinus +1 oct ; decay ≈ 108 [ASR ?] ; delay 1/8, filtre ≈ 1700 Hz | CH-10 |
| Accords liquid | saw +2 oct ; unison ≈ 6 ; low cut 220 Hz (ou 110) | CH-11 |
| Melodic dubstep | 170 BPM, La majeur ; Chaos1 → coarse 20 ; unison +5 ; reverb ≈ 35 % | CH-13 |
| Mur d'accords | saw 9 voix, detune ≈ 22 [ASR ?] ; saw 3 voix, detune ≈ 0,04 ; sirène LFO → fine 8,2 Hz | CH-14 |
| Wub future bass | LFO1 → levels A, B, sub ; rate ex. 1/8 | CH-15 |

- **House** : stab mineur dans une note, accords hors gamme assumés [SOURCE CH-01] ; deep à attaque douce [SOURCE CH-02] ; garage et minimal en sinus, accord swingué [SOURCE CH-03, CH-04] ; melodic à dérive [SOURCE CH-06] ; future house à chute de pitch [SOURCE CH-07] ; nu disco à pan aléatoire [SOURCE CH-08].
- **DnB** : FM sinus et WT dessinée [SOURCE CH-09] ; keys sinus, Cm7 puis Si bémol [SOURCE CH-10] ; 7e et 9e tirées de la basse [SOURCE CH-11] ; stab mono à formant, pas un accord voicé [SOURCE CH-12].
- **Dubstep / future bass** : accords tirés de la basse, tierce montée d'une octave [SOURCE CH-13] ; mur de couches [SOURCE CH-14] ; wub par LFO sur les niveaux [SOURCE CH-15].
- Lire d'abord : CH-01, CH-03, CH-06, CH-11.
- Contradiction sur la phase aléatoire : à 0 pour une attaque identique, « comme un sample » [SOURCE CH-05, LE-07] ; au maximum [SOURCE HO-01] ; laissée haute, plus épais [SOURCE CH-11] ; on = variations, off = attaque identique [SOURCE CH-15]. Le but décide.
- Écarts : toutes les fiches sont en Serum 1. Chaos de la page Global (CH-13 : « chaos rate au maximum, sample & hold ») : en Serum 2, Chaos et S&H sont des types de LFO (§ 7.2, § 13). « German LP (MK) » (CH-01) = German LP, Misc, sans VAR (§ 6). « Low Pass 18 » (CH-05) : Low 18 ou MG Low 18, non tranché. « Sine fold » (CH-14) = **Sin Fold** (§ 8).

## Pad

- **Oscillateurs** : saw ou table « Juno » en unison 5 à 9, copie à +1 oct [SOURCE PA-01, PA-02, PA-06, PA-12] ; sinus + table en unison 9 et 12 [SOURCE PA-03] ; table spectrale « glassy » [SOURCE PA-13] ; sample figé en Spectral Manual [SOURCE PA-14].
- **Enveloppes** : attack long, release long ; ENV2 lente → cutoff [SOURCE PA-05, PA-07, PA-11].
- **Filtre** : LP 12 à 24 ou MG Low 18, keytrack [SOURCE PA-03, PA-11].
- **Mouvement** : LFO → fine (vibrato) et level (trémolo) [SOURCE PA-01, PA-02] ; un LFO qui ralentit un autre LFO [SOURCE PA-01, PA-02] ; LFO lent sur la WT pos [SOURCE PA-03, PA-08] ; Chaos → Master Tune pour la dérive [SOURCE PA-07].
- **Pads rythmés** : LFO 1/16 sur le cutoff [SOURCE PA-06] ; Arp en mode chord sur un ladder fermé [SOURCE PA-04] ; Auto Pan en trémolo ou en ducking [SOURCE PA-08, PA-12].
- **FX** : chorus, phaser lent, delay avant la reverb, Hall, EQ low cut [SOURCE PA-01, PA-02, PA-05].

| Paramètre | Valeur | Source |
|---|---|---|
| ENV1 | decay ≈ 2–2,5 s, release ≈ 360 ms | PA-02 |
| Osc et LFO | unison 5 sur A et B, B +1 oct ; LFO2 → rate LFO1, montant ≈ 20, rate ≈ 2,5 non sync | PA-02 |
| FX | phaser ≈ 25 % ; chorus ≈ 40 % ; low cut ≈ 170 Hz ; Ozone Imager mono sous 180 Hz | PA-02 |
| Pad Selected, osc | A : WT max, Bend +/− −32 %, level 67 ; B : unison 3, detune 0,06, FM depuis A 39 %, level 73 | PA-05 |
| Pad Selected, filtre | MG Low 18, 469 Hz, res 22 %, drive 22 % ; noise level 22 | PA-05 |
| ENV1 | attack 41 ms, decay 1,76 s, sustain −5,7 dB, release 1,20 s | PA-05 |
| ENV2 → cutoff | A 25 ms, D 1,79 s, S 65 %, R 632 ms ; montant 15 | PA-05 |
| FX Selected | ENV3 → drive 39 ; Diode 1 drive 52 %, mix 34 % ; Dimension 9, mix 20 ; Hall mix 61 % | PA-05 |
| Pad OCULA | WT ≈ 18 et 8 ; detune 0,03 ; attack 9 ms, release ≈ 350 ms ; LFO1 1/16 ; LFO2 → fine 13 ; porta ≈ 50–55 ms | PA-06 |
| Pad analogique | attack ≈ 500–570 ms [ASR ?], release ≈ 960–970 ms ; ENV2 attack 900 ms ; Chaos 1 → Master Tune ≈ 4 | PA-07 |
| Pad afro | sinus unison 9, table unison 12 ; delay 1/8, feedback ≈ 40 [ASR ?] ; EQ ≈ 700 Hz | PA-03 |
| Pad Serum 2 | tables −4 et −3 oct ; Splitter grave / aigu ≈ 300 Hz | PA-10 |
| Trémolo liquid | Auto Pan amount 100, phase 0, 1/16, offset 180 | PA-12 |
| Liquid sombre | unison 6 ; sub saw −2 oct ; LFO1 Envelope 1/4 → Master Tune −12 (ou −5 / −9) | PA-13 |
| Future bass | unison 4 ; sub triangle −1 oct ; ENV2 → mix reverb, delay 800 ms, sustain 100 % | PA-15 |
| Accords dits | Cm (+ F add11), Bbm7 ; m → m7 → m9 → m11 | PA-08, PA-11 |

- **House** : deep Juno [SOURCE PA-01, PA-02] ; Selected chiffré [SOURCE PA-05] ; afro à noise panoramiqué [SOURCE PA-03] ; melodic rythmé par LFO [SOURCE PA-04, PA-06] ; analogique dérivant [SOURCE PA-07] ; minimal à LFO de 4 mesures [SOURCE PA-08].
- **DnB** : accords étendus [SOURCE PA-09, PA-11] ; LP 24, LFO 2 mesures, trémolo [SOURCE PA-12] ; glissé de pitch à l'attaque [SOURCE PA-13] ; trois couches dont une granulaire [SOURCE PA-10].
- **Dubstep** : aucun pad melodic dubstep fait dans Serum. PA-14 n'a pas de genre dit ; PA-15 est de la future bass.
- Lire d'abord : PA-05, PA-02, PA-07, PA-14.
- Écarts : PA-04 « MS ladder » [ASR ?] : **MG Ladder**, type New, VAR = SMOOTH, probable (interp.) (§ 6) ; « shader » absent de la cartographie. PA-07 « Chaos 1 » : type de LFO en Serum 2 (§ 13). PA-14 met Phase Lock au clic droit sur la position ; la cartographie en fait un contrôle du moteur Spectral (§ 3.6). PA-14 « stack 12 » = STACK « 12 (1-3x) » (§ 3.1). PA-10 « Rain 100 High » : dossier S2 Noises, nom non listé (§ 3.7).

## Drone

- **Sources** : noise seul, filtré et résonant [SOURCE DR-01] ; deux tables analog, warp Bend lent [SOURCE DR-03, DR-05] ; saws faibles en FM depuis le Sub [SOURCE DR-04] ; saws −2 / −1 oct en mono [SOURCE DR-06] ; samples en Sample ou Spectral Manual [SOURCE DR-08, DR-09, DR-11] ; accord de sinus sur les trois osc [SOURCE DR-10] ; FM à ratio non entier [SOURCE DR-15].
- **Évolution** : LFO de 2 à 32 mesures sur cutoff, niveau, WT pos [SOURCE DR-03, DR-04, DR-06] ; un LFO qui module le rate d'un autre [SOURCE DR-02, DR-07] ; formes aléatoires [SOURCE DR-07, DR-09] ; S&H lissé sur le fine [SOURCE DR-11].
- **Enveloppes** : attack très longue, release long [SOURCE DR-01, DR-14, DR-15].
- **Routage** : osc C et noise vers Bus 1 en parallèle [SOURCE DR-06] ; Splitter M/S, low cut sur le Side [SOURCE DR-04, DR-08].
- **Resampling** : bounce dans Serum, puis Granular ou Spectral [SOURCE DR-10, DR-11] ; piano rendu puis chargé dans le Noise [SOURCE DR-14].
- **FX** : reverb longue et forte, delay ping-pong, OTT pour remonter les queues [SOURCE DR-01, DR-03, DR-15].

| Paramètre | Valeur | Source |
|---|---|---|
| Texture de noise | noise 50 %, pitch 18 ; ENV1 1,27 (s ?) ; LFO1 2 bars → cutoff + résonance | DR-01 |
| FX de la texture | chorus 15 %, delay ≈ 43 %, reverb 50 %, decay 8 s | DR-01 |
| Drone analog | release ≈ 2,40 s ; unison 4, detune ≈ 0,08 ; WT ≈ 130 et ≈ 214 | DR-03 |
| LFO et FX | LFO1 → cutoff 1/16 ; LFO3 → level B 8 bars ; delay ≈ 38 % ; reverb ≈ 50 %, decay ≈ 8 s | DR-03 |
| Atmo afro | LFO1 triangle 2 bars ; LFO2 et 3 en escalier, 1/4, trig ; LFO4 rampe 4 bars ; compresseur 3:1 ; low cut ≈ 35 Hz | DR-02 |
| Atmo melodic techno | LFO2 4 bars ; LFO3 32 bars, rise 2 bars, delay 1 bar ; delay ping-pong 1/4 | DR-04 |
| Drone de basse | A −2 oct, B −1 oct unison 11, C 0 oct ; LFO → cutoff 2 puis 1 bar, 55 % puis ≈ 6 % ; 50 % vers Bus 1 | DR-06 |
| Drone spectral | Splitter M/S, Side coupé sous 250 Hz ; reverb Nitrous 50 % | DR-08 |
| Drone sombre DnB | note E grave ; sample −2 oct puis plus bas | DR-09 |
| Accord de sinus | +7 (quinte) ; +3 mineur ou +4 majeur ; 7e sur le 3e osc | DR-10 |
| Atmo DnB | Fm7 ; unison impair ; note F = hauteur d'origine (C = −5 st) | DR-11 |
| Pad sombre neuro | A + B −2 oct, B +3 st, unison 2 ; Vocal Hum WT 230, −1 oct, +3 st ; cutoff ≈ 26 ; reverb size 30 % | DR-12 |
| Drone ambient | ENV1 attack ≈ 19 s ; VintageVerb decay ≈ 30 s, mix ≈ 70 ; noise pitch +12 ; unison 7 ; LFO1 8 bars → Master Tune | DR-14 |
| Drone FM sombre | 2 à 3 octaves plus bas, deux notes à l'octave ; LFO3 → Master Tune, 4 bars, quelques demi-tons | DR-15 |
| Intro deep dubstep | 8, 16 ou 32 mesures | DR-13 |

- **House** : textures de breakdown melodic [SOURCE DR-01, DR-03] ; atmo afro en « gouttes » [SOURCE DR-02] ; melodic techno, tension avant le drop [SOURCE DR-04, DR-05]. DR-03, DR-06, DR-07 et DR-08 : genre attribué par l'étude, pas dit.
- **DnB** : samples très bas et convolution [SOURCE DR-09] ; resampling granulaire ou spectral [SOURCE DR-10, DR-11] ; pad sombre neuro, sub en Direct Out [SOURCE DR-12].
- **Dubstep** : intro deep dubstep minimale [SOURCE DR-13] ; resynthèse d'un piano [SOURCE DR-14] ; drone FM inharmonique, vidéo française [SOURCE DR-15]. DR-14 cite le dubstep parmi d'autres usages ; DR-15 est une affectation de l'étude.
- Lire d'abord : DR-04, DR-06, DR-15, DR-11.
- Contradiction : DR-02 est noté Serum 1 mais parle d'un « LFO bus » [ASR ?]. Les bus de LFO n'existent qu'en Serum 2 (§ 7.2). Version à vérifier.
- Écarts : DR-02 « Symmetry Plus » [ASR ?] : aucun warp de ce nom, Asym + probable (interp.) (§ 4.1) ; « anchor off » = **HOST** en Serum 2 (§ 7.2). DR-12 « High EQ 6 » [ASR ?] existe, Misc, VAR = DB +/− (§ 6). DR-15 « BP12 » [ASR ?] : Band 12 ou Multi BN, non tranché.
- Écarts : DR-08, warps Detune, Spread, Gate : noms internes connus, libellés affichés MUET (§ 4.3) ; Nitrous et son mode Space sont confirmés (§ 8) ; preset « MB OTT » [ASR ?] non listé. DR-10 « Geiger » = bruit de couleur de Serum 2 (§ 3.7). DR-14 (Serum 1) charge un sample dans le Noise ; en Serum 2, le moteur Sample le fait (§ 3.3) (interp.). L'export de DR-10 se fait en glissant l'icône d'onde (§ 2.3).

## Où ces sons rejoignent le projet

- **Stabs, pads et leads Bass House** : `../../bass-house-sound-design/SKILL.md`. Fiches proches : LE-03, LE-04, HO-03, CH-01, CH-04, CH-05.
- **Basses** : `../../serum-2-basses-house-future-house/SKILL.md`. Débordent sur la basse : PL-11, PL-14 (plucks-basses), HO-12 (riff jump up), DR-06 (drone de basse). Règle du projet : sub et basse médium dans deux instruments, sub mono. LE-03 duplique le patch pour la couche sub : (interp.) la mettre dans un instrument à part.
- **Hooks** : `../../composer-hooks-funk-electro/SKILL.md` pour la cellule et les notes. Ce corpus donne le timbre : HO-, CH-05, CH-06.
- **Cuivres** : le « horn » de Fisher (HO-01, HO-02) et la table DX Brass 2 (LE-12) → `../../studio-grade-brass-sound-design/SKILL.md`.
- **Orgue et keys** : orgue M1 (CH-04), keys (CH-08, CH-10) → `../../studio-grade-funk-keys-synth-sound-design/SKILL.md`.
- **Imprimer** : DR-10, DR-11, DR-14 et CH-10 rendent le son puis le retravaillent. Capture dans Live : `../../resampling/SKILL.md`. Sampling dans Serum : `sampling-serum-synthese.md`.
- **Drops** (interp.) : la variation exigée avant chaque frontière de huit mesures peut passer par une macro automatisée : cutoff avant le drop (DR-05), rate d'un LFO pluck (PL-03), feedback du delay (DR-06).
- **Émotions** (interp.) : drones et pads servent intros et breaks ; leviers dans `../../composer-trajectoire-emotionnelle/SKILL.md`.
- **Exécution dans Live** : `../../vst-sound-design/SKILL.md` (chargement sans hot-swap, réglage par clics).

## Limites

- **Captures non faites.** Chaque fiche liste ses points « À vérifier à l'écran ». Aucun n'a été vérifié : ni position, ni nom de table, ni ADSR lue.
- **Transcription automatique** partout, sauf CH-02 et HO-14 (manuelles) et CH-15 (d'apparence manuelle). LE-08 est très bruitée ; HO-15 et PL-04 sont médiocres. Noms de tables douteux : « Basic MDC / CGV / CJW / MCB » (LE-11, LE-13, PL-15, DR-05, PA-05), « HyPA » (LE-08), « JNO » (LE-14), « at plates » (DR-07), « Solid Phase 1 » (PA-13).
- **Serum 1 à traduire** (68 fiches) : Master Tune → Main Tuning ; FM from B → FM (B) ; LFO Trig / Env / Off → RETRIG / ENVELOPE / FREE ; Chaos de la page Global → types de LFO ; étalement de WT de l'onglet Global → réglages d'unison ; noise utilisé comme sampler → moteur Sample ; 4 macros → 8 ; un filtre → deux. Voir `serum2-cartographie.md` § 13.
- **Effets natifs de Live filmés** : Saturator (LE-03, CH-02, HO-13), Reverb et Delay en envoi (CH-02), EQ Eight (HO-01, HO-02, CH-02, CH-11, PA-09), Auto Filter et delay (HO-01), Utility (HO-02, HO-04, PL-13, CH-13, CH-15), Pedal (HO-02), Overdrive et Erosion (HO-10, CH-09), Reverb et OTT en groupe (HO-13), Chorus-Ensemble en alternative (HO-13), Hybrid Reverb (CH-13), Spectral Blur et EQ mid/side (CH-15), Auto Pan (PA-08, PA-12), Delay (PA-11), EQ et compresseur (PA-15), Audio Effect Rack (PL-09). Effets MIDI : Chord et Scale (PL-04, PA-13), Arpeggiator (DR-05).
- **Règle du projet** (règle 6 de `../../ableton-live-session/SKILL.md`) : pas de nouvel effet natif de Live dans les chaînes de mix ; passer par des plug-ins tiers (`../../effets-plugins/references/fiches.md`). Les effets internes de Serum restent permis. Tolérés : instruments natifs, Utility, Compressor en sidechain déjà en place, Auto Filter déjà posé sur une piste MIDI, Hybrid Reverb sur un retour. Chord, Scale et Arpeggiator sont des effets MIDI, pas des traitements de mix (interp., à confirmer avec l'utilisateur).
- **Plug-ins tiers filmés**, présence sur le Mac non vérifiée : Kickstart 2, Sausage Fattener, Neutron 3, Pro-Q 3, iZotope Trash, Decimort 2, RBass, Camel Crusher, Pro-L, Ozone Imager, soothe, ShaperBox, RC-20, Kilohearts, Valhalla VintageVerb, Pro-R, K-Clip.
- **Droits.** Beaucoup de fiches recréent des titres publiés (LE-08, LE-14, HO-01, HO-02, HO-04, HO-08, HO-09, HO-10, HO-11, PL-07…) et donnent parfois leur MIDI (HO-06, CH-02). Ne reprendre que le timbre, jamais la mélodie ni les paroles (règle « Référence » d'AGENTS.md). Les presets de packs, gratuits ou payants (CH-15 « Power Saw » du pack Sunset, PL-05, HO-01, PA-08), ne s'utilisent qu'avec une licence vérifiée. Samples de DR-09, PA-10, PA-14 : packs tiers, droits à vérifier.
- **Notes.** C3 = 60 dans Live ; le numéro MIDI fait foi. PL-14 joue « C0–C1 », soit MIDI 24 à 36 si la vidéo suit la même convention (interp.). DR-14 sample en « C4 » sans dire sa convention. DR-08 : « C3 = lecture normale », cohérent avec la cartographie (osc Sample sans pitch tracking = note 60, § 3.1).
- **Manques du corpus.** Lead : 2 tutos français, 4 Serum 2 sûrs. Pluck : pas de pluck tech house ; DnB surtout DNB Academy ; 2 Serum 2. Hook : DnB difficile (HO-11 d'intro, HO-12 médium-grave) ; 1 français ; 2 Serum 2. Accords : tout en Serum 1 ; pas d'accords afro ni tech house ; le 3e dubstep est de la future bass. Pad : aucun pad melodic dubstep fait dans Serum ; aucun français. Drone : genres souvent attribués par l'étude ; DnB = DNB Academy seulement ; aucun drone tech house, bass house ou minimal.
- **Pas d'écoute.** « Funky », « glassy », « creepy », « wow » sont les mots des vidéos. Les tests d'écoute reviennent à l'utilisateur.
