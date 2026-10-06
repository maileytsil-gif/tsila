# Captures d'écran des kicks Serum : 39 vidéos (6 octobre 2026)

> Fichier remis par l'utilisateur le 06/10/2026 et intégré tel quel au skill `drums-signature` ; il remplace la version à 12 vidéos (les 12 premières entrées sont inchangées, 27 s'y ajoutent). Les captures sont lues sur l'image, son coupé : **rien n'a été entendu**. Elles complètent 39 des 46 vidéos de `kicks-serum-tutoriels.md` ; les identifiants entre parenthèses (BH-01, AF-05, DM-01…) sont ceux de ce corpus. **Toutes les fiches DM (deep, minimal), base de la fiche du kick signature, sont désormais capturées (DM-01 à DM-07).** Restent sans capture 7 fiches techno et rave : TE-02, TE-03, TE-05, TE-07, TE-11, TE-15 et RA-15. Seules les 12 premières vidéos (PML, MERAKKI, DNB Academy, Ghosthack, Octocap, W. A. Production, Strob, MHA, Wildcrow, Loïc, DONKONG, TURNCLOAK) sont comparées au corpus dans la section « Ce que les captures ont confirmé » de `kicks-serum-synthese.md` ; les 27 autres n'y sont pas encore comparées. Plusieurs vidéos sont lues à basse résolution : leurs entrées signalent les valeurs illisibles ou approximatives.

# Captures d'écran — kicks Serum (lecture de l'image, son coupé)

## vr0DHvuQX8E — PML, Create the PERFECT Kick Drum in Serum 2 (HC-06, TH-04, FB-12, AF-02)
- 3:40 osc A « Default Shapes » sinus, OCT 0, phase 180°, random 100 ; LFO 1 en mode Envelope, forme Custom, 1/4, bulle « LFO 1 → A Level 96 % (−inf dB → −0,7 dB) » : LFO 1 sert d'enveloppe d'amplitude. ENV 1 : 0,5 ms / 0 / 1,00 s / 100 % / 15 ms. Voicing Legato.
- 4:26 LFO 1 rate 3,4 Hz (mode Hz), en Envelope : courbe descendante ; ShaperBox 3 et SPAN sur la piste pour visualiser.
- 6:14 osc B « Default Shapes » carré, OCT +2 ; LFO 3 (triangle, 43,7 Hz) en préparation.
- 7:24 FX : Distortion « Tube », drive 17 %, filtre OFF. LFO 3 Custom, Envelope, 47,0 Hz (enveloppe de pitch très rapide), poly « 0/16 ».
- 9:02 osc C en mode Sample « 3F_KikAtk_30 » (sample d'attaque d'usine), One-shot ; LFO 2 rate 48,5 Hz en Envelope (decay très court) ; spectre : énergie 40–100 Hz.

## -Waj_SV5mlU — MERAKKI, Making Kicks with Serum 2 (AF-01, HC-05, TH-02) — FL Studio, 140 BPM
- 1:23 osc A « Default Shapes » sinus, OCT −1, phase 180°, random 100 ; LFO 1 en Envelope, Custom, 1/8 (courbe d'enveloppe de pitch descendante) ; ENV 1 : 1,0 ms / 0,0 ms / 1,00 s / 0,0 dB / 15 ms.
- 3:03 LFO 1 en Envelope, courbe exponentielle rapide, 1/8.
- 10:03 FX : Equalizer seul ; bande basse 118 Hz (« FX 1 EQ Freq 118 Hz »), Q 60, gain 5,2 ; bande haute ~20 kHz, Q 80, 0,0. LFO 4 en Envelope, 1/16 (pic très court). Voicing poly 0/16.
- 12:13 FX : Equalizer (118 Hz, Q 57, +2,5 ; ~1010 Hz, Q 90, −5,6) → Splitter L/H/M (bandes ~4233 Hz et 1101 Hz) → Convolve (IR « Crisp », taille 40 %). LFO 5 en Retrig, 1/4.
- 20:45 deuxième kick : Distortion « Overdrive », Stack 2, filtre OFF (425 Hz, Q 1,0 par défaut) ; LFO 3 Envelope, 1/16 ; ENV 1 : 0,1 ms / 0 / 1,00 s / 0,0 dB / 15 ms ; poly 0/32.

## oRhBZ6L9rU8 — DNB Academy, Acoustic-Sounding Kick Drums in Serum 2 (AF-03) — image petite, valeurs fines partiellement lisibles
- 1:57 Matrice : LFO 1 → A Level ; LFO 2 → A Coarse Pitch (bulle « LFO 2 → A Coarse Pitch 19 %, range +24 » environ) : enveloppe de pitch par LFO en mode Envelope.
- 2:53 osc A « Basic Shapes » (sinus arrondi), OCT 0 ; osc B « Default Shapes » scie ; LFO 3 triangle (Retrig).
- 4:23 osc C en mode Sample : menu Factory Non-Tonal > Drum > Kick, choix « 909 Kick Low 1 » (liste 505/626/707/808/909 Kick…).
- 5:13 osc C « Kick Deep » (lecture approx.) en One-shot ; LFO 4 → C Level 100 % (enveloppe d'amplitude du sample).
- 8:23 FX : Equalizer seul (bande basse ~200 Hz, 0,0 ; bande haute ~20 kHz) ; LFO 5 en Envelope, pic court.

## VRgyVszcoAI — Ghosthack, kick from scratch in Serum (+ resampling) (AF-04, FB-10) — Serum 1, FL Studio 140 BPM
- 1:36 osc A « Basic Shapes » sinus, OCT −2 ; ENV 1 : 0,5 ms / 0,0 ms / 324 ms / −inf dB / 15 ms ; ENV 1 → A Coarse Pitch : 48 (bulle « Env 1 → A CoarsePit 48 ») ; filtre MG Low 12 inactif.
- 2:19 sub activé, onde sinus, OCT −1 (« SubOscOctave −1 Oct »).
- 3:43 sub OCT −2 ; noise = sample foley « Ghosthack-UFS3_Tarabuka Body_10 » (darbouka), ENV 1 → Noise Level 56.
- 4:36 noise « Tarabuka Body_3 », Noise Pitch 26,00 st (« Noise Pitch 26,39 % »), key track actif.
- 5:58 FX : Distortion « Tube », filtre OFF (330 Hz, Q 1,9 par défaut) ; Compressor (mode simple) avec « CmpGain 12,4 dB ». Voicing mono, poly 3/24.

## lkBXuPiS1Is — Octocap, The PERFECT Kick Drum in Serum 2 (AF-05, FB-13, HC-09, TH-06) — Ableton
- 1:55 osc A « Default Shapes » sinus, OCT −1, phase 0°, random 0 ; ENV 2 → A Coarse Pitch (bulle « Env 2 … Destinations : A Coarse Pitch »).
- 3:12 ENV 1 (amplitude) : 1,0 ms / 50 ms / 97 ms / −inf dB / 15 ms (kick très court).
- 4:21 ENV 2 (pitch) : 0,5 ms / 0,0 ms / 100 ms / – / 15 ms ; EQ Eight après Serum (1,00 kHz, Q 0,71, gain 0) ; ShaperBox 3 en visualisation.
- 5:36 EQ Eight avec un creux dans le bas-médium (courbe en V visible) ; forme d'onde du kick dans ShaperBox : ~8 cycles décroissants.

## UOw9xaG2GG0 — W. A. Production, Punchy EDM / Dubstep KICK in Xfer Serum (BH-01, FB-03) — Serum 1, Ableton 120 BPM
- 1:48 osc A « Analog_BD_Sin », OCT 0 ; ENV 2 : 0,5 ms / 0,0 ms / 1,00 s / 100 % / 15 ms ; LFO 1 triangle par défaut, 1/4 ; filtre MG Low 12 actif sur A.
- 2:13 LFO 1 redessiné en courbe décroissante (pic puis chute rapide) : sert d'enveloppe de pitch.
- 3:31 LFO 1 rate 1/8, courbe exponentielle ; note jouée G0 (clip MIDI) ; poly 0/8.
- 4:32 noise « XF_KikAtk_15 » (transitoire d'attaque) activé ; filtre MG Low 12 : coupure/résonance ajustées sur A, B, N.
- 6:49 FX : Distortion « Tube » (filtre OFF, 330 Hz / Q 1,9), drive monté ; ENV 2 : 0,5 ms / 0,0 ms / 126 ms / 0,00 % / 15 ms (decay court) → modulation de 2 cibles.

## ep-JWElNvLA — Strob Studio, Kick « EDM » dans Xfer Serum (BH-02, FB-05) — Serum 1, Ableton 135 BPM
- 1:26 Matrice : LFO 1 → Master Tune (bipolaire) ; ENV 1 : 0,5 ms / 0,0 ms / 1,00 s / 0,0 dB / 15 ms.
- 2:13 osc A sinus (table par défaut), OCT 0 ; LFO 2 dessiné en courbe décroissante, 1/4.
- 3:54 osc A OCT −2 ; LFO 2 en mode ENV (plateau court puis descente linéaire) → niveau de A.
- 5:02 warp de A « Sync » modulé par LFO 3 en mode ENV, 25,7 Hz (pic très bref = clic d'attaque).
- 10:34 osc B scie, OCT −2, filtre MG sur B seul ; LFO 4 (« L4 ») en ENV, 1/4, forme en cloche → niveau de B.
- 15:28 kick figé (Freeze) dans Ableton puis FabFilter Pro-C 2 (style Clean ; réglages non lisibles).

## pGix2clNzG4 — MHA, How To Make Drum Samples (Serum/Vital) (BH-03) — Serum 1, FL Studio
- 1:24 osc A « Analog_BD_Sin », OCT −2 ; filtre MG Low 12 ; ENV 1 : 0,5 ms / 0,0 ms / 1,00 s / 0,0 dB / 15 ms.
- 2:08 LFO 1 en mode ENV (Anchor), 6,2 Hz, rampe descendante linéaire : enveloppe de pitch.
- 3:13 FX : Distortion « Tube » (filtre OFF) ; ENV 1 : 0,5 ms / 0,0 ms / 763 ms / −inf dB / 15 ms ; LFO 1 redessiné en courbe exponentielle, 6,2 Hz, ENV ; poly 0/16.

## 3lHVhdM83LI — Wildcrow Studio, BEST WAY to MAKE a KICK in SERUM in 5 MINUTES (BH-04, DM-06, FB-04, TH-05) — Serum 1, FL Studio
- 1:48 osc A « Basic Shapes » sinus, OCT 0 ; LFO 2 dessiné en chute rapide (1/4) → niveau de A.
- 2:26 osc B « Basic Shapes » sinus ; LFO 3 en descente progressive → niveau de B.
- 3:05 LFO 4 en forme de cloche (montée rapide, plateau, descente) → niveau de B.
- 3:45 FX : Distortion « Tube » (filtre OFF) ; LFO 4 en mode ENV, 3,6 Hz, montée exponentielle.
- 4:52 ENV 2 : 0,5 ms / 0,0 ms / 65 ms / 0,00 % / 15 ms (enveloppe de pitch courte) ; menu de warp de B ouvert (Sync, Bend, PWM, Asym, Flip, Mirror, Remap…).

## XAsVlnau5Gs — Loïc / Mixup Studio, Créer un Kick Moderne avec SERUM (BH-05, FB-06, TH-07) — Serum 1, FL Studio
- 2:30 osc A « Analog_BD_Sin », OCT 0 ; ENV 2 (pitch) : 0,5 ms / 0,0 ms / 197 ms / 0,00 % / 15 ms.
- 4:26 ENV 1 (amplitude) : 0,5 ms / hold 94 ms / decay 76 ms / −inf dB / 15 ms ; A RandPhase 100 % puis remis à 0 (phase fixe).
- 5:09 osc B « Monster 2 [SL] » (table spectrale) ajouté, OCT 0.
- 6:40 noise « AC hum 1 » activé ; ENV 3 (niveau de B) : 0,5 ms / 0,0 ms / 624 ms / 0,00 % / 15 ms.
- 7:54 noise remplacé par « XF_KikAtk_06 » (transitoire d'attaque), en One-shot ; ENV 2 : decay 91 ms. Voicing poly 0/24.

## jcciPjElopE — DONKONG, Kick Drums From Scratch (BH-06, FB-08) — Serum 1, Logic Pro (ShaperBox après Serum)
- 0:49 osc A et B « Basic Shapes » sinus, OCT 0 ; menu warp de A ouvert → « FM (from B) ».
- 1:40 warp A = FM (from B) ; LFO 1 en mode ENV, 1/8, rampe descendante → 2 cibles ; ENV 1 : 0,5 ms / 0,0 ms / 1,00 s / 0,0 dB / 15 ms.
- 2:27 ENV 1 attaque 0,0 ms ; LFO 1 redessiné en courbe exponentielle.
- 3:19 LFO 2 en ENV, 1/128, rampe descendante → quantité FM, sur macro 1 « CLICK ».
- 4:35 osc B : OCT +1, SEM +7 ; LFO 3 en ENV, 1/8, plateau puis chute (enveloppe de niveau de B) ; macro 2 ajoutée.

## LLbJ1BkpfOc — TURNCLOAK, Make SICK Kicks in Serum 2 (BH-07, FB-14)
- 1:24 osc A « Default Shapes » sinus, OCT 0, phase 0°, random 0 ; noise « BrightWhite » ; LFO 1 en Envelope, Custom, 1/4, courbe pic puis plateau descendant ; ENV 1 : 0,5 ms / 0,0 ms / 1,00 s / 100 % / 15 ms ; analyseur : ~44 Hz (F1).
- 2:50 FX : Distortion « Tube » (filtre OFF, 425 Hz / Q 1,9) ; LFO 2 en Envelope, chute exponentielle, 1/4.
- 3:38 chaîne FX : Equalizer (210 Hz, Q 60, 0,0 ; ~20 kHz) → Distortion Tube → Compressor Single (seuil −32,9 dB, 4:1, attaque 90,1, release 9,7, gain 0) → Distortion.
- 6:09 filtre 1 « MG Low 12 » sur A.
- 8:18 osc B en mode Sample « hat (fun fact) », One-shot, warp « FM (Noise) » ; noise « SH1 Noise » ; filtre 1 « High 18 » ; LFO 4 Envelope, 4,0 Hz.

## JhZU6JGvoHw — In The Mix, Make Your Own Kick Drums (DM-01, HC-07) [Serum dans FL Studio]
- 2:23 ENV 1 : attack 0,5 ms, hold 170 ms, decay 108 ms, sustain −oo dB, release 15 ms ; LFO 1 rampe montante (grid 8)
- 3:38 Matrice : destination « A CoarsePit » (type →, mod *) en cours de création
- 3:53 Matrice : Env 2 → A CoarsePit = 18 ; ENV 2 : chute très courte (pic puis décroissance rapide) ; LFO 1 triangle
- 5:01 Filtre « MG Low 12 », cutoff haut (légère coupure des aigus), drive/fat/mix basses ; EQ paramétrique FL (Fruity Parametric EQ 2) neutre, points 1 et 2 à plat
- 5:49 Noise activé avec sample « XF_KikAtk_28 » (Level moyen, Pitch ~centre), Osc A Basic Shapes sinus unison 1, Osc B Default (dent de scie) désactivé, Sub désactivé
- (le point 5:06 n'a pas été relevé)

## s6e1dFJu-Mc — Serum Kick Drum Sound Design Tutorial (DM-02, HC-08) [Serum ×2 dans FL Studio, tempo 140]
- 2:12 Serum 1 (preset « Jon - Kick Drum 2 ») : Osc A « Analog_BD_Sin » ; Osc B off ; Noise « XF_KikAtk_11 » ; filtre MG Low 12 vide ; ENV 1 attack 1,1 ms, hold 0,0 ms, decay 217 ms, sustain −oo dB, release 4,7 ms ; LFO 1 rampe descendante, mode ENV, grid 12, BPM 1/16. Serum 2 (Init) : mêmes réglages sauf ENV 1 decay 274 ms, LFO 1 grid 8 puis 12, rate 1/4 puis 1/16
- 2:47 Mêmes réglages ; Serum 2 : ENV 1 decay 274 ms, LFO 1 grid 12, rate 1/16
- 4:51 Onglet FX : EQ puis Compresseur (non multibande) dans la chaîne ; réglages EQ/compresseur illisibles à cette image ; infobulle « EQ VolH : 12,0 dB » (Serum 2)
- 5:57 FX : EQ, curseur sur le filtre haut ; réglages EQ illisibles
- 6:21 FX : infobulle « EQ VolH : 8,6 dB » (Serum 2) ; compresseur sans valeurs lisibles

## 4Q_xxaZs0Uo — Making GREAT Kicks in SERUM! (DM-03, FB-07, HC-03, TH-03) [Serum dans Ableton Live, instrument rack]
- 2:30 Init ; ENV 1 : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 mode ENV, rampe descendante, rate 1/4, grid 8 ; matrice vide ; chapitre « Pitch and LFO design »
- 5:03 FX : Compresseur (non multibande) ; LFO 1 courbe exponentielle (chute rapide puis plateau bas) ; chapitre « Filtering and dynamics »
- 9:24 ENV 1 en cours d'édition : courbe en chute, attack 0,5 ms, hold 0,0 ms, decay 1,00 s ; LFO 1 même courbe exponentielle ; compresseur seul dans FX
- 11:51 ENV 1 : attack 0,5 ms, hold 122 ms, decay 125 ms, sustain −oo dB, release 15 ms ; LFO 3 mode ENV, rate 1/4, courbe exponentielle ; FX : Compresseur puis Filtre « MG Low 6 »
- 13:06 FX : Compresseur → Filtre « MG Low 18 » (cutoff réglé) → EQ ; ENV 1 inchangée (hold 122 ms, decay 125 ms)
- 15:41 FX : Distortion « SoftClip » (drive en cours) → Compresseur multibande → Filtre « MG Low 18 » → EQ ; LFO 2 rate 1/8 ; sous Serum : rack Ableton avec OTT (multibande), Glue Compressor, EQ Eight

## -fuuJavALAU — Arc Nade, How To Make A Kick Drum In Serum (DM-04, FB-11, HC-10, TH-08) [Serum x64 dans FL Studio]
- 1:04 Init ; Osc A « Analog_BD_Sin » (OCT −2, SEM 0, FIN 0) ; Osc B off, Noise off, Sub off ; filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100,00 %, release 15 ms ; LFO 1 triangle, mode OFF, rate 1/4, grid 8
- 1:50 ENV 1 réécrite : attack 0,0 ms, hold 0,0 ms, decay 87 ms, sustain −oo dB, release 0,0 ms (pic net puis chute) ; Osc A unison 1
- 2:08 Matrice : tooltip « Env 2 → A CoarsePit : 20 » (le curseur est sur le pitch grossier de l'osc A) ; ENV 2 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100 %, release 15 ms (en cours de réglage)
- 3:01 FX : Distortion type « Tube », filtre interne HP/BP/LP position 330 Hz, Q 1,9, OFF/PRE/POST sur OFF ; ENV 2 attack 0,0, hold 0,0, decay 76 ms, sustain 0,00 %, release 0,0 ms
- 3:58 FX : Distortion « Tape Sat. » → Compresseur (non multibande) → EQ ; ENV 2 inchangée (decay 76 ms) ; valeurs du compresseur et de l'EQ pas encore réglées (knobs à leur position d'origine)
- 4:28 EQ : sélection du type « Peak » sur le filtre bas de l'EQ (tooltip « EQ Typ : Peak ») ; reste identique

## jUKtyFqINdg — Xfer Serum Sound Design – Simple kick drum, Free Patch D/L (DM-05, TH-09) [Serum dans Ableton Live]
- 0:48 Init ; Osc A « Analog_BD_Sin » (OCT 0, SEM 0, FIN 0) ; Osc B off, Noise off, Sub off ; filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle, rate 1/4, grid 8 ; Voicing POLY 16
- 1:47 ENV 2 : courbe en chute exponentielle ; attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,00 %, release 15 ms (réglages en cours)
- 3:12 Osc A CRS (pitch grossier) −26,23 ; ENV 2 décroissance très courte : attack 0,5 ms, hold 0,0 ms, decay 93 ms, sustain 0,00 %, release 2,90 s ; menu des filtres ouvert (liste MG Low 6/12/18/24, Low 6–24, High, Band, Peak, Notch ; « Low 12 » survolé)
- 4:07 Filtre « Low 24 », info-bulle « Fil Reso : 0 % » ; ENV 3 sélectionnée : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100,00 %, release 444 ms (en cours) ; ENV 2 déjà assignée
- 6:33 Filtre « Low 24 » avec cutoff abaissé (courbe en coupure passe-bas) ; ENV 3 : attack 0,0 ms, hold 0,0 ms, decay 241 ms, sustain 0,00 %, release 1,36 s (infobulle « Env3 Dec : 241 ms »)
- 8:08 Panneau MOD : 3 knobs macro nommés « Pitch Decay », « Cutoff Decay », « Click » (et un 4e) assignés (ENV 1/2/3) ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 89 ms ; filtre avec résonance et cutoff réglés

## Ls1e9Br5tPY — Sancus, Serum Tutorial | House, Dubstep, and DnB Kick (DM-07, HC-11) [Serum dans FL Studio, 150 BPM, projet KICKZ]
- 0:23 Serum 1 (Init) : Sub activé (octave −2, forme triangle), Noise activé sample « kick trans 2 », Osc A et B en « Custom » (formes complexes), filtre MG Low 12 vide ; ENV 1 attack 0,0 ms, hold 0,0 ms, decay 94 ms, sustain −oo dB, release 15 ms ; LFO 1 mode ENV, rate 1/4, courbe de chute rapide, grid 8 ; Voicing POLY 8. Chaîne mixer (insert « Serum_x64 ») : OTT_x64 → Fruity parametric EQ 2 → Fruity parametric EQ 2 → Fruity soft clipper → Fruity Limiter
- 2:10 Serum 2 « #2 » Init (Osc A/B sinus-saw Default) : Sub triangle octave −2 ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 mode ENV rate 1/4 courbe de chute ; Serum 1 inchangé (ENV 1 decay 94 ms)
- 3:14 Serum 2 : matrice « LFO 1 → Mast.Tun » (hauteur globale pilotée par le LFO) ; ENV 1 (Serum 1) decay 94 ms, sustain −oo ; Serum 2 ENV 1 decay 1,00 s
- 4:47 Serum 2 : Noise « kick trans 4 » ; ENV 1 attack 0,0 ms, hold 0,0 ms, decay 94 ms, sustain −oo dB, release 15 ms (copie du Serum 1) ; LFO 1 mode ENV rate 1/4
- 6:40 OTT (Xfer) : Depth ≈ 98 %, Time ≈ 1000 %, In Gain ≈ 0,7 dB, Out Gain 0,0 dB, Upwd 100 %, Dnwd 100 % (lecture à faible résolution, valeurs approximatives)
- 8:36 Fruity parametric EQ 2 : courbe avec bosse vers le bas-médium et une autre au médium-aigu, graves relevés ; barre de titre « 2219 Hz » (fréquence en cours de réglage) ; valeurs précises par bande illisibles

## nB72uEMja1Q — Quick Toots, How to create the Big Room Kick with SERUM (FB-01) [Serum dans Ableton Live, 130 BPM]
- 0:33 Serum onglet FX : Distortion « SoftClip », info-bulle « Dist_Drv : 39 % » (lecture à faible résolution, ≈) ; ENV 1 attack 0,0 ms, hold 0,0 ms, decay 201 ms, sustain 0,00 %, release 15 ms ; LFO 1 (mode ENV, rate 1/4, courbe en cloche avec creux) ; piste « Serum » avec EQ Eight en dessous (3 bandes à plat)
- 1:12 Plus de fenêtre Serum : vue Arrangement d'Ableton avec le kick Serum bouncé en audio sur plusieurs pistes (« KICK », « old kick »), clip audio en train d'être étiré/édité ; EQ Eight visible sans valeurs lisibles ; rien de paramétrable lisible à cet instant

## lQVtRzE8pfM — HOW to make a BIGROOM KICK! Tutorial Thursday #2 (FB-02) [Serum seul, preset « BASS - Electro » en départ]
- 1:19 Sub activé (DIRECT OUT, octave −1, forme sinus), Osc A wavetable « MiniBass » (OCT −1, SEM 0, FIN 0), unison 1, WT POS pilotée (Osc A mode « SYNC 1/2 WIN. » = warp), Osc B off, Noise off, filtre MG Low 12 ; ENV 1 attack 0,3 ms, hold 0,0 ms, decay 595 ms, sustain 0,00 %, release 20 ms (courbe triangulaire descendante) ; LFO 3 triangle, rate 1/4, grid 8 ; Voicing POLY 16
- 2:13 Osc A « MiniBass » : WT POS réglée à 136 (info-bulle « A WTPos : 136 ») ; warp « SYNC 1/2 WIN. » ; sub direct out toujours actif ; ENV 2 sélectionnée avec un indicateur « 1 » (assignée)
- 2:52 Même état (Sub direct out octave −1, Osc A MiniBass, WT POS ≈ 136, warp Sync 1/2 Win.) ; forme d'onde affichée = un seul cycle avec ondulation ; ENV 1 en chute linéaire ; LFO 3 sélectionné ; filtre non utilisé

## tqu6VD2uVCs — TUTORIAL: How to Kicks and 808s in Serum? (FB-09) [Serum (skin « Donkong », 6 LFOs) dans Logic Pro, plugin FF Pro-L 2 sur le master]
- 0:20 Init ; Osc A et B « Basic Shapes » sinus ; Osc B SEM +7 puis +1 octave (OCT +1, SEM +7) ; Osc A warp « FM (From B) » ; filtre « Allpasses » (cutoff, damp, mix) ; ENV 1 attack 0,0 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO L1 mode ENV, rate 1/8, courbe de chute ; 4 macros nommés « CLICK », « FM », « ANALOG » (mod 1/3/2)
- 1:06 Même patch ; LFO L2 sélectionné (compteur 5) : mode ENV, rate 1/128, courbe exponentielle ; Osc A FM(from B) ; macros CLICK/FM/ANALOG assignés
- 2:08 Noise vide à ce stade (curseur sur DIRECT OUT du Noise) ; LFO L2 rate 1/128 ; Osc A warp FM(from B)
- 2:34 Noise activé, sample « J 60 » ; LFO L1 sélectionné, mode ENV, rate 1/8 ; Osc A FM(From B) ; ENV 1 inchangée (decay 1,00 s)
- 4:08 Fenêtre « Oscillator A Table Edit » : forme d'onde à un cycle (sinus déformé, deux bosses positives, deux négatives), 256 frames, 3 frames visibles (1, 29, 256), zoom 4x, grid 8 ; spectre : fondamentale forte puis décroissance rapide des harmoniques
- 5:00 Retour sur l'écran OSC : Noise « J 60 » activé, WT POS Osc A pilotée (indicateur d'assignation) ; LFO L5 sélectionné (compteur 1), mode ENV, rate « bar », courbe montante puis descendante lente ; Osc A FM(from B)

## kUkMmFVtu6E — Proper Villains / Sound Collective, 808 Kick Drum | Percussive Sound Design in Serum | 2 of 5 (HC-01) [Serum x64 dans Ableton Live, 120 BPM, avec LFOTool (Xfer)]
- 1:53 Init ; Osc A « Basic Shapes » sinus (OCT 0, SEM 0, FIN 0), Osc B/Noise/Sub off, filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 mode ENV, rate 1/4, grid 8, rampe descendante ; à droite LFOTool (SVF LP) : forme d'onde en oscillation amortie, rate 1/4 (chapitre « Designing the kick core »)
- 3:36 Matrice : LFO 1 → A Vol ; LFO 2 → A CoarsePit, info-bulle « LFO 2 → A CoarsePit : 24 » ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 2 mode ENV, rate 1/4, rampe descendante ; LFOTool : courbe d'enveloppe en rampe descendante (rose), rate 1/4
- 4:21 Matrice : LFO 1 → A Vol et LFO 2 → A CoarsePit avec courbes, curseur de sortie de l'amount 2 déplacé ; LFO 2 : rate 35,5 Hz (cadre rouge), rise 0,0 s, delay 0,0 s, smooth 0,0, mode ENV, courbe exponentielle (chute rapide) ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s
- 5:42 Ableton : piste « 1 Serum x64 » (volume −1,61 dB) ; chaîne Serum x64 → Glue Compressor (threshold −15,2 dB, ratio non lisible, range 70,0 dB, makeup 0,00 dB, dry/wet 100 %) → Saturator (drive 0,00 dB, type « Analog Clip », 100 %, output 0,00 dB) → Spectrum (block 8192, plage −12 à −96 dB)
- 6:44 Glue Compressor : threshold −14,3 dB, makeup 4,44 dB ; Saturator : drive 1,14 dB, type « Soft Sine », output −2,00 dB ; LFOTool ouvert (SVF LP, rate 1/4, snap 8, depth 100, split freq. 632) ; spectre montrant un pic basse fréquence (~60–100 Hz) puis décroissance

## qT5s153nQ58 — Tutoriel | TR-808 KICK / Trap Kicks et Preset Serum Gratuit (HC-02) [Serum dans Ableton Live ; vidéo en basse résolution, valeurs lues à ± incertitude ; tuto en français]
- 4:50 Init ; Osc A et Osc B « Analog_BD_Sin » sinus (Osc B OCT +1), unison 1, filtre « High 24 » (cutoff haut) ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle, rate 1/4, mode OFF, grid 8 ; Voicing POLY 16 ; macro non utilisé
- 5:36 Même patch ; LFO 1 passé en rampe descendante, mode ENV (rate 2,0 Hz, rise 0,0 s, delay 0,0 s, smooth 0,0) ; ENV 1 inchangée
- 6:38 Onglet FX : Distortion type « Tube » (drive et mix réglés mi-course, filtre interne HP/BP/LP) ; LFO 1 courbe de chute exponentielle rapide, rate 2,0 Hz
- 9:33 Pas de fenêtre Serum (vue arrangement Ableton) ; rien de lisible
- 10:18 Noise activé, sample « BrightWhite » ; Osc B unison 2 ; ENV 1 : attack 0,5 ms, hold 0,0 ms, decay ≈ 153 ms, sustain −oo dB, release 15 ms (courbe de chute) ; LFO 1 rate 2,0 Hz, mode ENV, courbe de chute rapide ; filtre High 24 ; Voicing MONO

## Co6bYxpj5_8 — WA Production, How To EDM: 10 Minutes Techno / Tech House Kick In Serum (HC-04, TH-01) [Serum x64 dans Ableton Live, 130 BPM]
- 1:10 Init ; Osc A « Analog_BD_Sin » (OCT 0, SEM 0, FIN 0), Osc B/Noise/Sub off, filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 rampe descendante, mode OFF, rate 1/16, grid 8 ; Voicing POLY 8 (chapitre « Oscillator settings »)
- 1:55 LFO 1 : courbe de chute avec point intermédiaire, mode ENV, rate 1/8 ; ENV 1 inchangée ; Osc A pitch en cours de modulation (indicateur CRS)
- 3:08 Osc A OCT +2 (SEM 0, FIN 0) ; LFO 1 mode ENV, rate 1/8, courbe : plateau haut court puis chute rapide jusqu'à un palier bas (forme de « pitch drop » à 2 étapes) ; ENV 1 inchangée
- 3:49 Même Osc A OCT +2 ; LFO 1 : plateau haut → chute → palier bas ; deuxième point d'inflexion visible
- 5:56 Onglet FX : Compresseur (non réglé, valeurs lues par défaut) puis Distortion type « Tube » (filtre interne : fréquence 330 Hz, Q 1,9, position OFF ; info-bulle « Dist_Freq ») ; LFO 1 inchangé
- 7:44 FX : Compresseur → Distortion « Tube » (filtre POST, fréquence 1260 Hz, Q 0,1) → Filtre « MG Low 6 » (cutoff réglé, fat) → Equalizer ; ENV 1 : attack 0,5 ms, hold 0,0 ms, decay 248 ms, sustain −oo dB, release 63 ms ; LFO 1 rate 1/8

## BP3biVgN2u0 — 909 Techno Kicks in Serum | Space 92, Reinier Zonneveld, Charlotte de Witte (HC-12, RA-01, TE-09) [Serum dans FL Studio, 140 BPM, avec LFOTool (Xfer), projet « 909 Kicks.flp »]
- 1:25 Vue partielle (cadrage serré) : LFO 1 rampe descendante, mode ENV, rate 1/4, grid 8 ; Voicing POLY 8 ; filtre MG Low 12 ; LFOTool (SVF LP) : forme d'onde en oscillation amortie ; mixer FL avec bus « SIDECHAIN MAIN », « Patcher »
- 2:23 Osc A « Analog_BD_Sin » (OCT 0, SEM 0, FIN 0), Osc B/Noise/Sub off ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100,00 %, release 15 ms ; LFO 2 sélectionné, rampe descendante, rate 1/4, mode ENV ; matrice : info-bulle « LFO 2 → A CoarsePit : 21 » (modulation du pitch grossier de l'osc A) ; mixer : bus KICK BUS, KICK 1/2/3, BASS BUS, Sub, Bass, Mid, Top, DRUM BUS, DELAY, AMB REV, WIDER, REVE & REVB
- 3:36 LFO 2 : courbe en 2 segments (chute rapide puis queue) avec points d'édition, rate 1/4, mode ENV ; ENV 1 inchangée (decay 1,00 s, sustain 100,00 %) ; LFOTool (SVF LP, rate 1/4, snap 8, LFO routing cut/res/vol/pan/var, split freq 632)
- 4:52 Osc B actif : table « Dist C2 » (forme d'onde dentelée/déformée), OCT +1, SEM 0, FIN 0 ; Osc A WT POS et level pilotés (indicateur d'assignation) ; LFO 3 sélectionné : courbe exponentielle rate 1/4 ; ENV 1 inchangée
- 6:55 Fenêtre Fruity parametric EQ 2 (7 bandes) sur le master du kick, bandes à plat ; mixer FL ouvert : insert « Master » avec Patcher, Fruity parametric EQ 2, Soft Clipper (?), LFOtool, « Wave Candy » ; Serum partiellement masqué (ENV 1 : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100,00 %, release 15 ms)
- 10:31 Serum « Kick 1 » onglet FX : Distortion type « Tube » (filtre interne PRE, ≈ 67 Hz, Q 1,4, drive réglé ≈ mi-course) → EQ (aucune valeur lisible) ; LFO L4 sélectionné (compteur 1) : courbe exponentielle, rate 1/4 ; ENV 1 inchangée ; Wave Candy en bas à droite montrant la forme d'onde du kick

## 2hX7UeT14Zo — Fare un KICK con SERUM | Tutorial ITA [Sound Design] (HC-13) [Serum x64 dans PreSonus Studio One, 152 BPM ; tuto en italien]
- 1:49 Init ; Osc A « Basic Shapes » sinus (OCT 0, SEM 0, FIN 0), Osc B/Noise/Sub off, filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle, rate 1/4, mode OFF, grid 8 ; Voicing POLY 8 (chapitre « Kick Sound Design con SERUM »)
- 3:58 Matrice : « Env 2 → A CoarsePit » (amount réglé vers le milieu, valeur non lisible) ; ENV 2 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100,00 %, release 15 ms (en cours de réglage) ; LFO 1 triangle rate 1/4
- 4:58 Noise activé : sample « XF_KikAtk_08 » ; filtre « MG Low 12 », info-bulle « Fil Cutoff : 523 Hz (401 Hz) » (cutoff abaissé) ; Osc A « Basic Shapes » ; LFO 1 mode ENV, rate 1/4 ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100,00 % (les enveloppes sont encore à leurs valeurs initiales)
- 5:45 FX : Distortion type « Tube » (filtre interne ≈ 330 Hz, Q 1,9, OFF/PRE/POST sur OFF, drive et mix au milieu) ; ENV 2 : attack 0,5 ms, hold 4,7 ms, decay 34 ms, sustain 0,00 %, release 15 ms (courbe de chute très courte = enveloppe de pitch) ; LFO 1 rampe descendante, rate 1/4
- 6:48 Serum chaîne d'inserts Studio One sur la piste « Kick » : 1 Pro-Q 3 (FabFilter) → 2 DS-10 Drum Shaper → 3 Saturn 2 → 4 FabFilter Pro-L 2 ; Pro-Q 3 : filtre passe-haut vers 20 Hz, bande 2 en cloche « Bell » 532,69 Hz, −0,65 dB, Q 1,000 ; analyseur Pre+Post

## 5g9drwe2kvU — Creating TECHNO Kick Drums from Scratch in Serum | FL Studio Tutorial (RA-02, TE-10) [Serum dans FL Studio, 132 BPM, avec LFOTool (Xfer)]
- 2:25 Init ; Osc A « Analog_BD_Sin » (OCT 0, SEM 0, FIN 0), Osc B/Noise/Sub off, filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 mode OFF, rate 1/4, courbe de chute éditée à plusieurs points ; LFOTool (SVF LP) : oscillation amortie, rate 1/4 (chapitre « Creating Kick With Serum »)
- 3:44 Matrice : « LFO 2 → A CoarsePit : 30 » (info-bulle) ; LFO 2 : chute très rapide (courbe exponentielle), mode OFF, rate 1/4 ; ENV 1 inchangée (decay 1,00 s)
- 5:15 Noise activé, sample « BrightWhite » ; Osc B actif, table « Dist 8bit Fwap » (OCT +1) ; ENV 3 : attack 0,5 ms, hold 0,0 ms, decay 1,14 s, sustain 0,00 %, release 15 ms (courbe de chute), compteur 1 ; LFO 1/2/3 avec compteurs ; LFO 3 rate 1/4, mode OFF
- 7:38 FX vide au chargement (en attente d'affichage) ; ENV 3 sélectionnée ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 56 ms, sustain 0,00 %, release 15 ms ; LFO 3 : rampe descendante, rate 1/4, mode OFF
- 8:37 FX : Distortion type « Asym » (filtre interne ≈ 330 Hz, Q 1,0, OFF/PRE/POST sur OFF, drive réglé ≈ 1/3, mix mi-course) → Filtre « MG Low 6 » (cutoff/res/drive/fat à plat) ; ENV 1 decay 56 ms, sustain 0,00 % ; LFO 2 compteur 2 : chute rapide
- 10:47 Autre plugin : Disperser de Kilohearts (3 bandes : Frequency 1/2/3, Dispersion, Resonance) ouvert sur un insert FL (insert 20) avec LFOTool ; mixer FL ouvert ; valeurs du Disperser non chiffrées (cadrans seuls) — le tuto ajoute de la dispersion de phase pour renforcer le « punch »

## STn2E_tRYzc — INSANE Industrial Techno Kicks in Serum 2 (RA-03, TE-04) [Serum 2 dans FL Studio, patch « Init », artiste TKNVLT]
- 1:02 Osc A en mode WAVETABLE « AT Entity » (OCT 0, SEM 0, FIN 0, phase 180°, RAND 100) ; Osc B/C off, Noise off ; ENV 1 attack 1,0 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 mode ENVELOPE, courbe exponentielle de chute (type « Custom », direction Forward, rate 1/4, grid 8) ; info-bulle sur CRS : « A Coarse Pitch (--) ; Assigned Modulators : LFO 1 » (le LFO 1 module le pitch grossier de l'osc A) ; astuce affichée « SHIFT + ALT + CLICK »
- 2:51 Osc A « AT Entity » avec OCT −3 ; Osc B actif (« Default Shapes », OCT 0) ; Filter 1 actif type « Allpasses » ; LFO 4 sélectionné (compteur 2), courbe en vague avec 3 creux (type « Custom »), mode ENVELOPE, rate 1/4 ; ENV 1 inchangée
- 4:44 Onglet FX, bus « BUS 1 » : chaîne EQUALIZER → DISTORTION → EQUALIZER → DISTORTION → UTILITY ; Equalizer (freq 210, Q 60, gain 0,0 ; second filtre 583 Hz, Q 41, gain 8,2) ; Distortion « SINE SHAPER » (filtre interne PRE/POST off, fréquence 425, Q 1,9) ; Utility ; info-bulle « FX 5 : Utils Level : −7,5 dB » ; LFO 3 : courbe de chute rapide à 3 points (compteur 2), rate 1/4
- 7:44 « BUS 2 » : SPLITTER M/S (MID, SIDE avec EQUALIZER) → EQUALIZER → DISTORTION → EQUALIZER → DISTORTION ; Distortion « SOFT SAT. » (freq 425, Q 1,9, drive moyen) ; Equalizer (210 Hz, Q 60, gain 0,0 ; 387 Hz, Q 32, gain 0,0, filtre passe-bas) ; LFO 3 compteur 3 : chute progressive en 3 segments
- 9:21 Bus « MAIN » : DISTORTION « HARDCLIP » (freq 425, Q 1,9) → COMPRESSOR multibande (thresh 0,0 dB, ratio 4:1, attack 90,1, release 90,1, gain 0,0 ; X-LOW 128, BELOW 0,0000, X-HIGH 2500) ; LFO 5 sélectionné : courbe montante concave puis chute abrupte, mode ENVELOPE
- 11:16 Bus « MAIN » : REVERB (type « VINTAGE », cut LO 0 / HI 35, size, pre-delay, decay, diff A/B), info-bulle « FX 1 : Rev Wet : 35 % » → DISTORTION « HARDCLIP » → COMPRESSOR multibande (thresh 0,0 dB, ratio 4:1, attack 90,1, release 90,1 ; X-LOW 128, BELOW 0,2095, X-HIGH 2500) → EQUALIZER → DISTORTION ; LFO 6 sélectionné (compteur 1) : courbe montante rapide puis plateau et chute lente ; 10 LFO listés, compteurs d'assignation visibles

## poTUNWW6feM — Industrial Techno Kick Using Serum 2 Only (RA-04, TE-08) [Serum 2 dans Ableton Live ; sous-titres incrustés ; chapitre « Kick Foundation »]
- 1:43 Osc A en mode SAMPLE : sample « 909 BD GO 01 » (One-shot, LS 0, LE 100, OCT 0, SEM 0, FIN 0) ; Osc B et C en WAVETABLE (« Default Shapes », éteints) ; Noise éteint ; Filter 1 / Filter 2 off ; ENV 1 attack 1,0 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle, mode RETRIG, rate 1/4 (BPM), grid 8 ; Voicing POLY 8
- 2:25 Onglet FX, bus MAIN : DISTORTION, stack 1, type « OVERDRIVE » (freq 425, Q 1,9, drive à mi-course) ; ENV 1 attack 1,0 ms, hold 0,0 ms, decay 1,00 s ; sous-titre « enable distortion »
- 2:52 Bus MAIN : DISTORTION « DIODE 2 » (freq 425, Q 1,9, drive réglé) → DISTORTION → COMPRESSOR multibande (thresh 0,0 dB, ratio 4:1, attack 90,1, release 1000,0, gain 0,0 ; X-LOW 310, BELOW 0,5013, X-HIGH 1665) → DISTORTION « TUBE » (freq 425, Q 1,9) ; ENV 2 sélectionnée : attack 0,5 ms, hold 0,0 ms, decay 228 ms, sustain —, release 15 ms (chute rapide)
- 4:17 Bus MAIN : EQUALIZER (filtre bas 210 Hz, Q 60 ; filtre haut 3006 Hz, Q 44, gain −3,1 dB) → DELAY (mode NORMAL, L 1/16, R 1/8 pointé, feedback, filtre) → REVERB type « HALL » (cut LO 0 / HI 35, size, pre-delay, decay ; SPIN rate 25 / depth 20) ; menu « + FX » ouvert listant les effets disponibles (Bode, Chorus, Compressor, Convolve, Delay, Distortion, Equalizer, Filter, Flanger, Hyper/Dimension, Phaser, Reverb, Splitter L/H, Splitter L/M/H, Splitter M/S, Utility) ; sous-titre « unique tone »
- 4:40 Plan sur l'intervenant (pas d'écran de réglages) ; sous-titre « and simple » ; rien de lisible à relever

## MuFyVZARsvA — How To Make a Hard Techno Kick in Serum 2 (Free Download) (RA-05, TE-06) [Serum 2 dans Ableton Live, patch artiste « KROSPER » ; vidéo en gros plan sur le plugin]
- 0:40 Osc A WAVETABLE sinus (phase 180°, RAND 0) ; Osc B/C off ; Noise off ; ENV 1 attack 1,0 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 mode ENVELOPE, courbe type « Custom », rate 1/4 (BPM), grid 8 ; Voicing POLY 8 ; sous-titre « FIRST LFO »
- 1:53 Sub activé (octave −2, forme sinus, CRS —) ; Osc A WAVETABLE « Default Shapes » (OCT −2, SEM 0, FIN 0) ; LFO 3 : chute exponentielle, mode ENVELOPE, rate 12,5 Hz (en Hz, pas en BPM) ; ENV 1 attack 1,0 ms, hold 0,0 ms, decay 1,00 s ; LFO 1 et LFO 2 assignés (compteur 1 chacun)
- 3:05 Filter 1 actif « MG Low 12 » (S sélectionné), cutoff/res/drive/fat réglés ; LFO 6 sélectionné : triangle (type « Default »), mode ENVELOPE, rate 1/4 ; LFO 4 compteur 1 ; ENV 1 inchangée
- 4:03 Onglet FX : Filter « Phs 24− » (cutoff réglé) → Distortion « HARDCLIP » (freq 425, Q 1,9, drive à mi-course) → Reverb « BASIN » (cut LO 0 / HI 0, size, pre-delay, feedback, chorus rate 25, depth 20 ; mix) ; LFO 6 : rampe montante lente puis chute (type « Custom »), mode ENVELOPE ; 10 LFO avec compteurs (5 assignés)
- 5:43 Filter « Phs 24+ » → Distortion « DIODE 1 » (PRE, freq 403, Q 0,7) → Compressor multibande (thresh 0,0 dB, ratio 4:1, attack 90,1, release 90,1, gain 0,0 ; X-LOW 128, BELOW 0,3393, X-HIGH 2500 ; niveaux H −5,7 / M −8,3 dB), info-bulle « FX 6 : Comp Gain 2 : −8,3 dB » ; LFO 6 mode ENVELOPE
- 6:16 Distortion « DIODE 2 » (POST off, freq 425, Q 1,9) → Equalizer (210 Hz, Q 60, gain 4,9 ; 203 Hz, Q 54, gain −11,5 dB ; creux visible vers 200 Hz) → Distortion « SOFTCLIP » (freq 425, Q 1,9) ; info-bulle « FX 9 : Dist Level : 2,2 dB » ; LFO 6 compteur 1 ; Voicing POLY 8 (4/16 voix)

## sd7LD8NG4F8 — REVERSE BASS Techno Kick (Creeds, Basswell, Marnik) (RA-06) [Serum dans FL Studio, 160 BPM ; projet « Reverse Bass Like Push Up » ; plugins Teknovault]
- 1:26 Playlist FL : un clip audio « Srm_ - Init » (kick bouncé en échantillon) sur Track 4 ; pas de réglage visible
- 3:23 Serum #5 (Init) : menu de sélection de wavetable ouvert (catégories Analog, Digital, KULTURE – Drum & Bass 01 / Jump Up 01 / Jump Up 1 / Reese 1 / UK Bassline, Spectral, User, Vowel, Wavetables) et liste Analog (4088, Acid, Analog_BD_Sin, Basic Mg/Mini/Shapes, BS2 – Acid/Filthy/Subby Saw, MiniBass, PWM…) ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; filtre MG Low 12 ; LFO 1 sélectionné
- 4:17 Osc A table « BSOD_Square » (OCT −2, SEM 0, FIN 0, forme d'onde irrégulière), Osc B off, filtre MG Low 12 vide ; LFO 1 : courbe en cloche (montée puis descente, points d'édition), mode ENV, rate 1/4, grid 8 ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms
- 4:44 Osc A « BSOD_Square » (OCT −2) ; filtre « German LP » actif (cutoff abaissé, courbe passe-bas) ; LFO 2 sélectionné : montée rapide puis plateau (mode OFF, rate 1/4) ; Osc A level piloté ; tempo FL 160 BPM ; projet « Reverse Bass Like Push Up »
- 6:10 Liste des plugins FL (menu de slot du mixer, insert « KICK BUZZ ») : FabFilter (Pro-C 2, Pro-L 2, Pro-Q 3, Pro-DS, Pro-G, Pro-R, Pro-MB, Saturn 2, Timeless 3, Volcano 3), Fruity (Balance, Compressor, Limiter, Multiband Compressor, Parametric EQ 2, Soft Clipper, Waveshaper…), Oxford, Valhalla, Soundtoys (Decapitator…), iZotope Trash 2, Devastor 2, etc. — le tuto choisit un plugin d'effet sur l'insert « Kick Buzz »
- 7:33 Fruity parametric EQ 2 sur l'insert « KICK BUZZ » (7 bandes quasi à plat, légère bosse vers 600–700 Hz) ; menu contextuel d'automation ouvert (Reset, Edit events, Create automation clip, Link to controller…) ; mixer à 60+ inserts

## EI6GqWOUa-g — How To Make a HARDTEKK Kick in Serum 2 (+ FREE PRESET) (RA-07) [Serum 2 dans Ableton Live, patch artiste « KROSPER » ; vidéo en gros plan ; sous-titres incrustés]
- 0:35 Patch Init : Sub activé (OCT −1, sinus), Osc A/B/C WAVETABLE « Default Shapes » (éteints), Noise « AC hum1 » éteint, Filter 1/2 off ; ENV 1 attack 1,0 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle (type « Default »), mode RETRIG, rate 1/4 ; Voicing POLY 8
- 1:54 Osc A : dent de scie (phase 180°, RAND 0) ; ENV 3 sélectionnée : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100 %, release 15 ms ; LFO 5 : rampe descendante, mode ENVELOPE, rate 1/4 (compteurs d'assignation visibles sur LFO 1-4)
- 2:27 Osc A et Osc B « Default Shapes » sinus (OCT −1, SEM 0, FIN 0 ; unison 1, phase 180°, RAND 0 / 100) ; Osc B activé ; ENV 4 sélectionnée (attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100 %, release 15 ms) ; LFO 6 : chute exponentielle rapide, mode ENVELOPE, rate 1/4 ; Voicing POLY 8 (0/24)
- 3:41 Osc B warp « TUBE » (warp 1) activé, Osc B OCT −1 ; Filter 1 activé, panneau de routage « MAIN » avec 2 cadrans (sorties du filtre) ; ENV 4 ; LFO 7 sélectionné (compteur 1) : plateau haut puis chute brutale (« fenêtre » de gate) en mode ENVELOPE, rate 1/4
- 5:06 Onglet FX, bus BUS 1 : EQUALIZER → DISTORTION « TUBE » (freq 425, Q 1,9, drive à mi-course) → DISTORTION « HARDCLIP » (freq 425, Q 1,9) → EQUALIZER (210 Hz, Q 60, gain 0,0 ; filtre haut 2041 Hz, Q 60, gain 0,0) ; ENV 4 : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100 %, release 15 ms ; LFO 7 compteur 1 ; sous-titre « DISTORTION, »
- 6:09 BUS 2 : DISTORTION « TUBE » (freq 425, Q 1,9) → EQUALIZER (filtre bas 210 Hz, Q 60, gain 0,0 ; filtre haut en passe-bas 12328 Hz, Q 36, gain 2,2 dB) ; LFO 4 sélectionné (compteur 2) : plateau puis chute rapide en courbe, mode ENVELOPE, rate 1/4 ; ENV 4 : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100 %, release 15 ms

## i8_Vfo892oA — This Is How Gated Kicks Are Built in Serum 2 (RA-08) [Serum 2 dans Ableton Live, patch artiste « KROSPER » ; vidéo en gros plan ; kick « gated » = enveloppes LFO + FX]
- 0:35 Osc B « Default Shapes » sinus (OCT −2, SEM 0, FIN 0, unison 1, phase 180°, RAND 0, level piloté par le curseur) ; Osc A/C off ; ENV 4 sélectionnée : attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 100 %, release 15 ms ; LFO 1 mode ENVELOPE, type « Custom », rate 1/4 : courbe quasi plate puis montée verticale (rampe exponentielle) en fin de cycle (compteur 1)
- 1:42 Matrice (3 routages) : LFO 1 → A Level ; LFO 2 → Noise Level ; LFO 3 → A Coarse Pitch (polarité unipolaire bleue sur le 3e), amounts réglés (positions visibles, valeurs non lisibles) ; LFO 3 : courbe de chute ondulée (légère baisse, creux, puis remontée), mode ENVELOPE ; ENV 1 à ENV 4 listées ; artiste KROSPER
- 2:17 Onglet FX, bus MAIN : HYPER/DIMENSION (Hyper : rate, unison 4, detune, retrig off) ; Ableton : liste de l'explorateur de devices à gauche (Wavetable, Utility, Spectrum, Saturator, Simpler…) ; pas de valeurs chiffrées lues sauf unison 4
- 2:52 FX : Dimension (size, mix) puis REVERB type « HALL » (cut LO 100 / HI 35, size, pre-delay, decay ; SPIN rate 25 / depth 20 ; mix ouvert) ; LFO 4 sélectionné (compteur 1) : courbe « Custom » à deux bosses en mode ENVELOPE ; piste Ableton « 4 Serum 2 »
- 3:45 FX : EQUALIZER (bande 1 : ... 242 Hz, Q 47, gain −24,0 dB ; bande 2 : 1128 Hz, Q 50, gain +24,0 dB ; forme en « S » avec creux et pic) → DISTORTION « ASYM » (freq 425, Q 1,9, drive à ≈ 11 h) → COMPRESSOR multibande (thresh −18,1 dB, ratio 4:1, attack 90,1, release 90,1, gain 8,8 ; X-LOW 128, BELOW 0,7518, X-HIGH 2500) ; LFO 4 compteur 1
- 4:09 Noise activé : sample « ARP circuit » (boucle, START 0, RAND 0), Filter 1 « Phs 24− » (cutoff réglé, courbe avec creux profond) ; filtre routé sur A, N sélectionné ; ENV 4 ; LFO 3 compteur 1, LFO 4 actif (compteur 1)

## 5bXTQvDmJY4 — How to Make a HARD TECHNO KICK in Serum 2 (Like FANTASM, I Hate Models & 999999999) + FREE Preset, AKA Sounds (RA-09, TE-14) [Serum 2 dans Ableton Live, patch « Init » ; vidéo très zoomée avec bandeau « www.akasounds.com »]
- 2:03 Osc A en mode sample « ONE-SHOT » (LS 0, LE 100), Osc B (phase 180°, RAND 100), Noise (RAND 0), Filter A actif (cutoff/res/drive/fat) ; ENV 4 ; LFO 1 compteur 1 ; LFO 2 sélectionné : triangle (type « Default »), mode RETRIG, rate 1/4, grid 8/8, forward
- 6:08 Onglet FX : EQUALIZER (freq 210 Hz, Q 51, gain −6,0 dB ; filtre haut 2041 Hz) avec info-bulle « FX 1 : EQ VolL −6,0 dB » ; courbe : creux léger vers 200 Hz
- 10:04 FX : EQUALIZER (deux bandes, creux marqué) → DISTORTION « SINE SHAPER » (PRE, freq 765, Q 1,3, drive réglé ≈ 1/3, mix à fond) ; LFO 3 sélectionné (compteur 2) : courbe type « Custom » en montée concave rapide puis chute brutale, mode RETRIG, rate 1/4 ; LFO 1/2 compteur 1
- 13:28 FX : DISTORTION (freq ..., Q 1,9) → FILTER (courbe en vague, res/drive/stages/pan, mix) → EQUALIZER (874 Hz, Q 40, gain −12,4 dB) ; info-bulle « FX 13 : EQ Q H : 40 % » ; LFO 3 compteur 6 (6 destinations)
- 14:14 FX : FILTER type « Diffusor » (cutoff, res, drive, stages, pan) → EQUALIZER (210 Hz, Q 60, gain 0,0 ; creux léger) → UTILITY (L/R polarity inv, LPF, HPF, MONO BASS actif, freq, width, pan, mix) ; ENV 2 compteur 3, LFO 1 / 2 compteur 1, LFO 3 compteur 6
- 15:29 FX : COMPRESSOR (ratio, attack 4,9, release 885,6, gain 3,8) puis COMPRESSOR multibande (attack 90,1, release 90,1, gain 0,0 ; X-LOW 128, BELOW 0,2701, X-HIGH 2500 ; niveaux H/M/L 0,0), info-bulle « FX 16 : Comp RatioB : 0,2701 » ; LFO 3 compteur 6, courbe d'enveloppe montante concave

## x2W1Z85G9Yc — How I make warehouse kick drums with Serum and Saturn in Ableton 10 (RA-10, TE-13) [Serum x64 + FabFilter Saturn dans Ableton Live 10 Suite, projet « Explosive Techno Kick » ; vidéo en basse résolution : les valeurs fines (decay, EQ, comp) sont ILLISIBLES, seules les structures sont fiables]
- 0:47 Serum Init : Osc A « Basic Shapes » sinus, Osc B/Noise/Sub off, filtre « MG Low 12 » vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay ≈ 100–180 ms (valeur illisible), sustain 0,0 dB, release 15 ms ; LFO 1 triangle (mode OFF), rate 1/4, grid 8 ; Voicing POLY 16, tempo Live ≈ 130 BPM ; clip MIDI de 4 notes
- 1:23 LFO 1 : courbe en chute exponentielle (rampe descendante concave), mode OFF puis ENV ; Osc A sinus ; ENV 1 inchangée
- 2:27 Filtre « MG Low 24 » activé (courbe passe-bas, cutoff abaissé) ; LFO 1 : courbe de chute avec point de cassure vers le milieu, mode ENV, rate 1/4 ; panneau Ableton à gauche passé sur Audio Effects (Utility, Saturator, Glue Compressor, EQ Eight…) ; chaîne de devices en bas : Serum → EQ Eight → FabFilter Saturn → EQ Eight → Glue Compressor → Utility (cadrage non lisible)
- 5:35 LFO 1 : courbe de chute avec 3 points rouges (segments éditables, sélection de points) ; ENV 1 : attack 0,5 ms, hold 0,0 ms, decay ≈ 180 ms ; chaîne de devices (bas) : EQ Eight (passe-haut ≈ 30 Hz, 4 bandes en cloche à plat), FabFilter Saturn « Default Setting », EQ Eight (creux profond étroit vers 150–200 Hz + filtre haut), Glue Compressor (threshold ≈ −8 dB, range 70 dB, dry/wet 100 %), Utility (« Bass Mono » actif)
- 7:14 LFO 1 : même courbe ; filtre MG Low 24 ; vue identique à 5:35
- 7:53 Fenêtre FabFilter Saturn 1 : interface rouge (une bande), menu de types de saturation ouvert (Clean Tube, Warm Tube [coché], Broken Tube, Clean Tape, Warm Tape [coché au 2e niveau], Old Tape, Smooth Amp, Crunchy Amp, Lead Amp, Screaming Amp, Power Amp, Gentle Saturation, Heavy Saturation, Smudge, Rectify, Destroy) ; Drive à fond de course (≈ 75 %), Level ≈ 0 dB, Feedback/Mix visibles

## ctq4msud7mg — Comment faire un KICK TECHNO RUMBLE WHAREHOUSE dans SERUM 2, style Amelie Lens, Charlotte de Witte (RA-11, TE-01) [Serum 2 dans Ableton Live, patch « Init », artiste Igor Chevalier ; tuto en FRANÇAIS ; incrustation webcam + bandeau strobstudio.com]
- 1:17 Osc A en WAVETABLE « Custom » (sinus, phase 180°, RAND 0, OCT 0, SEM 0, FIN 0), Osc B/C off, Noise off, Filter 1/2 off ; ENV 2 sélectionnée vide (attack 0,5 ms, hold 0,0 ms, decay 0,0 ms) ; LFO 1 triangle (type « Default »), mode RETRIG, rate 1/4, grid 8/8 ; Voicing POLY 8 ; clip MIDI en D#4
- 2:13 Osc A « Custom » avec OCT −4 (SEM 0, FIN 0), level piloté ; ENV 3 : attack 0,5 ms, hold 921 ms, decay 755 ms, sustain —, release 15 ms (courbe : plateau haut puis chute) ; ENV 2 compteur 1 ; LFO 1 triangle RETRIG
- 3:14 Osc B en mode SAMPLE : sample « Srm_-Init-_250428103402_E4 » (forme d'onde dense, ONE-SHOT, LS 0, LE 100, OCT 0, SEM 0, FIN 0, Scan sur le knob) — c'est un kick rendu par le patch lui-même ré-échantillonné ; ENV 2 : attack 0,0 ms, hold 0,0 ms, decay 172 ms (chute instantanée), release 15 ms ; infobulle « export rendu » (bouton « Serum 2 » : exporte la dernière note jouée en WAV) ; incrustation « ABONNEZ-VOUS »
- 5:38 Onglet FX, bus MAIN : CONVOLVE (IR « LEGO VERB », size, tone, min, pre-dly, bpm, attack, decay, damp, IR gain ; mix) → COMPRESSOR mode SINGLE (thresh −18,1 dB, ratio 4:1, attack 0,1, release 178,9, gain 0,0) ; ENV 3 : attack 0,5 ms, hold 551 ms, decay 145 ms, sustain 0 %, release 15 ms ; ENV 2/ENV 3 assignées (compteurs 1)
- 7:51 Osc A et Osc B en mode SAMPLE (deux échantillons rendus « Srm_-Init-_..._F4 », ONE-SHOT, LS 0, LE 100, SCAN activé sur les deux, level) ; Osc C wavetable off ; ENV 3 : attack 0,5 ms, hold 551 ms, decay 145 ms, sustain 0 %, release 15 ms ; LFO 1 triangle RETRIG ; POLY 8 (0/16) ; clip MIDI en G4
- 12:44 FX, bus MAIN : COMPRESSOR seul en mode MULTIBANDE (thresh −18,1 dB, ratio 4:1, attack 90,1, release 90,1, gain 0,0 ; X-LOW 128, BELOW 0,0000, X-HIGH 2500 ; niveaux H/M/L 0,0) ; ENV 3 : attack 0,5 ms, hold 0,0 ms, decay 669 ms, sustain 0 %, release 15 ms (chute lente) ; LFO 2 : courbe « Custom » montante concave avec plateau puis chute, mode ENVELOPE, rate 1/4 ; POLY 8 (3/24)

## fB-lBvNKJYg — Comment faire des Kick Tekno/Techno avec Serum (RA-12) [Serum dans Logic Pro, 150 BPM, pistes « Kick » et « Hall » ; tuto en FRANÇAIS ; incrustation webcam]
- 2:30 Serum « Init » : Osc A « Analog_BD_Sin » (OCT 0, SEM 0, FIN 0), Osc B/Noise/Sub off, filtre MG Low 12 vide ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle, mode OFF, rate 1/4, grid 8 ; Voicing POLY 8 ; chaîne Logic de la piste Kick : Serum → Distortion → Channel EQ → Distortion → Channel EQ → Limiter (noms visibles à gauche)
- 3:42 LFO 1 : chute exponentielle, mode ENV, rate 6,2 Hz (en Hz), rise 0,0 s, delay 0,0 s ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; Osc A level piloté (indicateur) ; mode MONO actif (POLY grisé)
- 5:42 Serum : ENV 1 attack 17 ms, hold 0,0 ms, decay 1,93 s, sustain −oo dB, release 1,2 ms (chute) ; LFO 1 mode ENV, rate 3,8 Hz, rise 0,0 s, delay 0,0 s, courbe de chute exponentielle ; MONO actif ; Logic : plugin Distortion (Overdrive) ouvert à gauche : Drive 26,0 dB, tone 20000 Hz
- 8:41 Logic Distortion (premier) : Drive 0,0 dB, Output −0,0 dB, Tone 20000 Hz, Level Compensation OFF, courbe 75 % ; Distortion (second, haut droite) : Drive 4,0 dB, Output −6,0 dB, Tone 20000 Hz ; Channel EQ (8 bandes) : bande 3 : 282 Hz, +1,7 dB, Q 1,30 ; bande 4 : 282 Hz, +1,4 dB, Q 1,50 ; bandes 5–8 : 1040, 2500, 7500, 20000 Hz à 0,0 dB (la dernière en passe-bas 24 dB/oct) ; passe-haut 20 Hz, 12 dB/oct, Q 0,71 ; Gain 0,0 dB
- 17:44 ValhallaVintageVerb (sur le bus « Verb ») : Mix 100,0 %, Predelay 192,55 ms, Decay 0,55 s, mode « Hall1984 », color 1980s, preset « 84 Small Drums » ; Damping : HighFreq 6000 Hz, HighShelf 0,00 dB, BassFreq 140 Hz, BassMult 1,00 X ; Shape : Size 0,0 %, Attack 66,8 % ; Diff : Early 100,0 %, Late 100,0 % ; Mod : Rate 0,10 Hz, Depth 0,0 % ; EQ : HighCut 4180 Hz, LowCut 10 Hz ; en dessous un Channel EQ : bande à +4,5 dB vers 137 Hz, −0,8 dB vers 520 Hz
- 23:15 Serum : ENV 1 attack 0,4 ms, hold 0,0 ms, decay 303 ms, sustain −oo dB, release 0,8 ms ; LFO 1 mode ENV, rate 1,7 Hz, courbe de chute exponentielle ; MONO actif ; chaîne Logic : Serum → Overdrive → Channel EQ → Distortion → Channel EQ → Limiter ; Overdrive : Drive 13,75 dB, Output −0,0 dB, Tone 20000 Hz ; mixer : Verb, Delay, Stereo Out 2, Master (niveaux −2,9 / 0,0 / −0,8 dB)

## ZNjY0Y17MIs — [TUTO #1] Création d'un KICK & BASS Techno (Serum & Samples) (RA-13, TE-12) [Serum dans Ableton Live 10 (interface en FRANÇAIS), 120 BPM ; tuto en FRANÇAIS ; vidéo en BASSE RÉSOLUTION : presque toutes les valeurs chiffrées sont ILLISIBLES, seules les structures sont fiables ; incrustation webcam]
- 2:43 Serum Init : Osc A « Basic Shapes » sinus, Osc B/Noise off, filtre MG Low 12 vide ; ENV 1 attack ≈ 0,5 ms, hold ≈ 0,0 ms, decay ≈ 1,00 s, sustain ≈ 0,0 dB, release ≈ 15 ms (lecture incertaine) ; LFO 1 : rampe descendante simple à 3 points en cours d'édition (chute linéaire vers 1/3), rate 1/8 ; Voicing MONO ; tempo Live 120 BPM ; pistes 1 Serum, 2 Serum, 3 KICKS, 4 KICKS, 5 KICKS, 7 Group, 8 Instrument, 9 Master Perc…
- 3:50 Noise activé : sample « AC hum1 » (puis « XF_KikAtk_12 » plus loin) ; LFO 1 : chute exponentielle plus courbée (plusieurs points), mode ENV ; Osc A sinus ; ENV 1 attack ≈ 0,0 ms ; filtre MG Low 12 vide
- 4:40 Noise « XF_KikAtk_12 » (sample d'attaque de kick), Sub off ; Osc A « Basic Shapes » sinus ; ENV 1 inchangée ; LFO 1 triangle puis LFO 2 sélectionné ; clips MIDI sur les pistes « 2 Serum » / « 3 Serum »
- 5:42 Onglet FX : COMPRESSOR seul activé (preset « Compressor », thresh/ratio/attack/release/gain à leurs positions ; mode monobande/multiband : option « MULTIBAND » visible, valeurs illisibles) ; LFO 3 sélectionné : rampe de chute exponentielle, mode ENV, rate 4,0 Hz ; Ableton : chaîne Serum → Decapitator (Soundtoys)
- 7:00 Noise « XF_KikAtk_12 » actif (à ≈ −8 dB ?), filtre « MG Low 12 » avec cutoff abaissé (courbe passe-bas) ; ENV 1 attack ≈ 0,0 ms, hold ≈ 0,0 ms, decay ≈ 1,00 s ; LFO 1 : chute exponentielle à plusieurs points, rate 1/4 ; chaîne Ableton : Serum → Decapitator
- 7:29 Même patch ; Noise « XF_KikAtk_12 » ; filtre MG Low 12 (cutoff bas) ; infobulle « Enveloppe-Zoom Sliders » (Serum) ; arrangement Live 10 avec clips de kick en rose (3 pistes KICKS) et clips Serum en bleu ; valeurs de decay/cutoff illisibles

## y0_AGmcC7f4 — INDUSTRIAL Techno Kick (Fantasm, DYEN, Vieze Asbak) (RA-14) [Serum dans FL Studio, projet TKNVLT « Youtube 22 – Industria », 155 BPM ; plugin gratuit « Serum FX » (SerumFX) en fin de chaîne]
- 1:04 Serum (Insert 1) Init : Osc A « Analog_BD_Sin » (OCT 0, SEM 0, FIN 0), Osc B/Noise off, filtre MG Low 12 vide ; ENV 3 sélectionnée (compteur 1) : attack 0,5 ms, hold 0,0 ms, decay 835 ms, sustain 0,00 %, release 15 ms (chute exponentielle) ; ENV 2 compteur 1 ; LFO 1 triangle, mode OFF, rate 1/4 ; Voicing POLY 8
- 1:32 Serum #2 (Master) Init : Osc A et Osc B « Default » dent de scie ; Osc B OCT −2 (SEM 0, FIN 0) ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s, sustain 0,0 dB, release 15 ms ; LFO 1 triangle mode OFF rate 1/4 ; POLY 8 (0/16)
- 2:26 Osc A « Default » dent de scie (OCT +1, SEM 0, FIN 0), warp 1 « FM (from B) » ; Osc B table « Dist 8bit Fwap » (OCT −2, SEM 0, FIN 0), warp « BEND + » ; info-bulle « B Warp : 100 % » ; filtre « High 24 » (cutoff réglé) ; macros nommés « CUTOFF 1 », « CUTOFF PUNCH », « CRUNCH », « FM PUNCH » (compteurs 1–2) ; LFO 2 : montée concave rapide vers un plateau, mode ENV, rate 1/4 ; ENV 1 attack 0,5 ms, hold 0,0 ms, decay 1,00 s
- 3:29 Onglet FX : FILTER type « Flg HL6+ » (cutoff, res, drive, HL Wid, pan, mix) → DISTORTION « Diode 2 » (filtre interne ≈ 330 Hz, Q 1,9, drive réglé, mix) → REVERB (plate/hall, size, decay, low cut, high cut, spin, spin depth, mix actif) → COMPRESSOR (multibande coché ; thresh/ratio/attack/release/gain à leurs positions, valeurs non lisibles) ; LFO L5 : rampe montante simple, mode ENV, rate 1/4 ; 6 LFO listés avec compteurs
- 3:47 FL Studio Playlist : un clip audio « Srm_ - Init - _240524195115_G2 » (kick Serum bouncé en échantillon) étendu sur Track 2 avec forme d'onde à longue queue (queue de plus de 4 mesures, enveloppe de chute lente) ; navigateur FL : packs TKNVLT (Hard Techno Production Suite, Bigroom Techno Serum Presets, Hard Techno Serum Presets, Industrial Techno Drum Loops…)
- 12:05 « SerumFX » (version FX du plugin Serum, onglet FX actif) : DISTORTION « Sine Shaper » (filtre interne ≈ 530 Hz, Q 1,9, drive à ≈ 3/4, mix) ; autres modules grisés (Hyper/Dimension, Flanger, Phaser, Chorus, Delay, Compressor, Reverb, EQ, Filter) ; mixer FL, insert « TKNVLT – Youtube 22 – Industria » : chaîne Fruity parametric EQ 2 → SerumFX → Fruity parametric EQ 2 → Decapitator → kHs Transient Shaper → FabFilter Pro-Q 3 → Fruity soft clipper ×2 → Oxford Inflator Native → Edison
