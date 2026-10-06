# Kicks dans Serum : synthèse de 46 tutoriels

Synthèse du corpus `kicks-serum-tutoriels.md`, rédigée le 05/10/2026. Ce corpus compte 85 fiches pour 46 vidéos différentes, en 8 styles, étudiées dans Claude in Chrome sur le Mac, son coupé. Les identifiants (BH-01, HC-08, DM-02…) renvoient aux fiches du corpus.

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Les valeurs viennent des transcriptions : ce qui est **dit**, parfois mal transcrit (marqué [ASR ?] dans le corpus). Les captures d'écran de **12 vidéos sur 46** sont faites (`kicks-serum-captures.md`, 06/10/2026) ; pour les 34 autres, chaque fiche du corpus finit par la liste des minutages « À vérifier à l'écran ».

Presque toutes les vidéos montrent Serum 1 : traduire les gestes dans Serum 2 et vérifier les noms de contrôle. Les fiches en Serum 2 : BH-07, HC-05, HC-06, HC-09, TE-01, TE-04 à TE-08, TE-14, RA-03 à RA-05, RA-07 à RA-09, RA-11, AF-01 à AF-03, AF-05.

## Ce que dit le corpus avant tout

- **Peu de tutoriels conçoivent un kick dans Serum pour un style précis.**
  - Hors techno et rave techno, les fiches sont surtout des tutoriels génériques, classés dans le style qui correspond le mieux à leur rendu.
  - Il n'y a aucun tutoriel « kick bass house », « kick deep house / minimal », « kick afro house », « kick future bass » ni « kick future rave » fait dans Serum.
  - Les vidéos de ces genres prennent un sample, Operator, Kick 2 ou Vital.
- **La même architecture revient partout**, du deep house au hard techno. Les styles diffèrent par les doses : longueur, profondeur de la chute de hauteur, clic, distorsion.

## Architecture commune

| Étape | Geste | Sources |
| --- | --- | --- |
| Source | sinus : Default, Basic Shapes, ou **Analog_BD_Sin** (sinus aux légères harmoniques, table de Serum 1), une ou deux octaves plus bas (registre sub) | BH-01, BH-03, HC-02, HC-03, HC-08, DM-01 à DM-05 |
| Voicing | MONO, pas de kicks qui se chevauchent ; qualité d'oscillateur au maximum (onglet Global) | DM-01, HC-07, HC-13 |
| Phase | RAND à 0 : départ toujours au même endroit. PHASE choisie : 0 (sans clic), au pic de l'onde (90°) pour plus d'attaque, ou autour de 120-156 | BH-01, BH-05, HC-04, HC-05, DM-04, DM-05 |
| Chute de hauteur | ENV 2, ou un LFO en mode Envelope (plusieurs points possibles) → CRS (coarse) de l'oscillateur, ou Global › Master Tune quand plusieurs oscillateurs doivent suivre ; modulation **unipolaire** (flèche simple dans la matrice, Shift+Alt+clic), pour que la hauteur retombe exactement sur la note | BH-01, BH-02, BH-03, HC-01, HC-03, DM-01, DM-04, DM-05 |
| Amplitude | ENV 1 en sustain −∞ : hold pour tenir le corps, decay pour la queue ; ou un LFO en Envelope sur le niveau | DM-01, DM-03, HC-09, HC-01, HC-06 |
| Clic | au choix : NOISE en one-shot sur la catégorie d'usine Attacks › Kick (numéros cités : 2, 6, 11, 15) ; un second sinus deux octaves au-dessus, joué un instant ; une FM brève ; un sample de hi-hat | BH-01, BH-02, BH-04, HC-01, DM-02, BH-07 |
| Corps | filtre passe-bas ouvert par une enveloppe qui retombe (Low 24, MG Low 18), drive du filtre pour les harmoniques | DM-01, DM-03, DM-05, HC-07 |
| Distorsion | sur le transitoire seulement : une enveloppe ou un LFO court → DRIVE (et MIX) ; pré-filtre de la distorsion en passe-haut pour épargner le sub | BH-01, HC-02, HC-06, HC-12 |
| EQ | creux dans le bas-médium (300 à 500 Hz), légère bosse à la fondamentale, air vers 8-9 kHz | HC-08, DM-02, DM-03, HC-03, HC-13 |
| Accord | la note MIDI jouée accorde le kick (G0, F1, F#, D…) ; vérifier à l'accordeur (GTune) ou à l'analyseur ; option : couper le pitch tracking pour un kick identique sur toutes les notes | BH-01, BH-04, HC-04, HC-06, DM-01, DM-04 |
| Impression | imprimer le kick en audio et le rejouer en sample, pour figer le résultat | BH-02, HC-02, HC-05 |

## Valeurs dites, à confirmer à l'écran

| Paramètre | Valeurs | Sources |
| --- | --- | --- |
| ENV 1, kick deep ou house | hold ≈ 100 ms, decay ≈ 100 ms, sustain −∞ | DM-01 (HC-07) |
| ENV 1, kick rond | attaque ≈ 1,1 ms, hold 0, decay ≈ 200 et quelques ms, sustain minimum, release ≈ 4 ms | DM-02 (HC-08) |
| ENV 1, longueur au tempo | une croche : à 125 BPM ≈ 250 ms, soit hold ≈ 125 ms et decay ≈ 125 ms | DM-03 (HC-03) |
| ENV 1, kick court | decay ≈ 80 ms, le reste au minimum | DM-04 (HC-10) |
| ENV 1, essentiel | hold 50, decay 100 | HC-09 |
| ENV 1, 808 long | sustain coupé, decay « une seconde et demie » | HC-02 |
| Chute de hauteur, douce | 12 demi-tons sur 1/16 (LFO 1 en Envelope → Semitone) | DM-02 |
| Chute de hauteur, courte | ENV 2 → Coarse ≈ 20, decay ≈ 80 ms | DM-04 |
| Chute de hauteur, decay | « 100 milliseconds is pretty good » | HC-09 |
| Chute de hauteur, forte | Coarse ≈ 25 (BH-01), ≈ 50 (BH-04), 48 puis réduit (HC-02) | BH-01, BH-04, HC-02 |
| Clic au second sinus | deux octaves au-dessus de la fondamentale | BH-02, DM-03 |
| EQ | bosse vers 47 Hz (fondamentale observée entre 40 et 50 Hz), air vers 8,8 kHz, creux étroit dans le bas-médium | DM-02 |
| EQ | creux vers 300 Hz (Serum), puis vers 500 Hz (post) | DM-03 |
| Tempo et longueur | le kick ne dépasse pas une demi-mesure | HC-12 |

Les unités de la quantité de modulation (« Coarse 20 », « 48 = 4 octaves ») ne sont pas vérifiées : lire l'infobulle de la matrice dans Serum 2.

## Fiche : le kick signature sous 124 BPM (doux, clair, chaleureux)

La signature demandée par l'utilisateur sous 124 BPM est un kick Serum 2 doux, clair et chaleureux. « Solomun feat. Jamie Foxx – Ocean » n'en est que la référence de kick (`AGENTS.md`). La recette de départ du dépôt est dans `../../produire-demo-electro-rapide/references/recettes.md` (« Kick Serum 2, esprit 808 soft »).

Les fiches DM du corpus, les kicks génériques au rendu rond, donnent de quoi la préciser. Ce sont des points de départ, à régler à l'oreille de l'utilisateur, en contexte.

| Section | Réglage de départ | D'après |
| --- | --- | --- |
| OSC A | Analog_BD_Sin, position de départ (à retrouver dans Serum 2), ou sinus Default ; OCT −2 ; RAND 0 ; PHASE 0 % (départ sans clic) | DM-02, DM-04, DM-05 |
| Voicing | MONO ; QUALITY au maximum | DM-01 |
| Hauteur | ENV 2 → CRS, unipolaire, chute d'environ 12 demi-tons ; ENV 2 : attaque 0, decay 60-100 ms, sustain 0 ; courbe concave pour une chute douce | DM-02, DM-04, HC-09 |
| Amplitude | ENV 1 : attaque 1 ms, hold 50-100 ms, decay 150-250 ms, sustain −∞, release 5 ms. Le kick reste plus court que l'écart entre deux kicks (500 ms à 120 BPM) | DM-01, DM-02, HC-09 ; recette du dépôt |
| Chaleur | FILTER 1 en Low 24 (ou MG Low 18), RES basse, ENV 3 → CUTOFF qui « finit bas » : l'attaque est claire, la queue ronde | DM-03, DM-05 |
| Clic | NOISE en one-shot, Attacks › Kick (le n° 11 de DM-02 en premier essai), niveau bas ; à couper si le kick paraît dur | DM-02, DM-01 |
| Saturation | Distortion Tape Sat., faible, ou rien | DM-04 |
| EQ (Serum) | petite bosse à la fondamentale (vers 47 Hz pour un kick en fa ou sol grave), air léger vers 8-9 kHz, petit creux étroit dans le bas-médium | DM-02 |
| Macros | `Pitch Decay` (decay d'ENV 2), `Cutoff Decay` (decay d'ENV 3), `Click` (résonance ou niveau du NOISE), `Release` (release d'ENV 1) | DM-05 |
| Accord | note MIDI à la tonique ou à la quinte du morceau ; mesure avec `../../kick-bass-equilibre/SKILL.md` | DM-01, DM-04 |

**Diagnostic quand le kick « ne va pas »** : un réglage à la fois, à niveau égal (A/B).
1. **Trop dur ou trop « clicky »** : baisser la chute de hauteur (DM-02 : « réduire le pitch dive s'il est trop marqué »), le clic du NOISE et la résonance, avant de toucher le corps.
2. **Trop mou ou absent à faible volume** : allonger un peu le hold, ouvrir le filtre au départ, ajouter une saturation Tape légère.
3. **Boueux** : petit creux étroit dans le bas-médium (DM-02 : une petite coupe seulement, sinon on « tue » le kick).
4. **En conflit avec le sub** : raccourcir le decay, accorder le kick et le sub ensemble, mesurer leur corrélation sur des exports séparés (`../../kick-bass-equilibre/SKILL.md`).
5. **Faux** : vérifier la note jouée à l'accordeur. Une chute de hauteur longue fait paraître la note plus haute (F01-02 du skill de basses, `../../serum-2-basses-house-future-house/references/etudes-pages-house.md`).

Vingt variantes de ce kick, avec le diagnostic relié à des recettes : `kicks/kicks-signature-sous-124.md`.

Quand l'utilisateur valide un kick à l'écoute, l'inscrire au registre `signature.md` (chemin du preset, réglages, accord, morceau, date).

## Ce que les captures ont confirmé

Source : `kicks-serum-captures.md`, 12 vidéos lues sur l'image : PML (HC-06), MERAKKI (HC-05, AF-01), DNB Academy (AF-03), Ghosthack (AF-04), Octocap (HC-09, AF-05), W. A. Production (BH-01), Strob (BH-02), MHA (BH-03), Wildcrow (BH-04), Loïc (BH-05), DONKONG (BH-06) et TURNCLOAK (BH-07). **Aucune vidéo DM n'est capturée** : la fiche du kick signature ci-dessus (DM-01 à DM-05) reste donc sur des valeurs dites, non lues à l'écran. Les valeurs sont celles affichées au minutage indiqué : un réglage peut changer plus tard dans la vidéo.

**Confirmé**

| Point | Ce que montre l'écran | Vidéos |
| --- | --- | --- |
| Chute de hauteur par ENV 2 | decay **65 ms** (Wildcrow), **100 ms** (Octocap, « 100 ms is pretty good » de HC-09 confirmé), **126 ms** (W. A. Production), **197 ms** puis **91 ms** (Loïc), sustain 0 | BH-04, HC-09, BH-01, BH-05 |
| Longueur du kick en ENV 1 | **1 ms / 50 ms / 97 ms / −∞ / 15 ms** (Octocap : un kick de 150 ms au total) ; **0,5 ms / hold 94 ms / decay 76 ms** (Loïc) ; decay **324 ms** (Ghosthack, avec une chute de hauteur de 48) ; decay **763 ms** (MHA, kick long) | HC-09, BH-05, AF-04, BH-03 |
| Chute de hauteur par un LFO en mode Envelope | LFO en **ENVELOPE**, forme descendante, → CRS ou Main Tuning : RATE **6,2 Hz** (MHA), **3,4 Hz** (PML), ou en divisions 1/4, 1/8, 1/16 (MERAKKI, DONKONG, Wildcrow, Strob) | BH-03, HC-06, AF-01, BH-06 |
| Clic d'attaque par un NOISE de l'usine | échantillons nommés **KikAtk** : « 3F_KikAtk_30 » (PML, one-shot), « XF_KikAtk_15 » (W. A.), « XF_KikAtk_06 » (Loïc, one-shot) ; c'est la catégorie Attacks › Kick de la fiche signature | HC-06, BH-01, BH-05 |
| Clic par un LFO très court | LFO en ENVELOPE à **47,0 Hz** (« enveloppe de pitch très rapide », PML) et **48,5 Hz** (decay très court, PML) ; **25,7 Hz** sur le warp Sync (Strob) ; un LFO à 43,7 Hz est seulement « en préparation » à 6:14 | HC-06, BH-02 |
| Distorsion | **Tube**, filtre de la distorsion OFF, dans 6 des 12 vidéos ; un second kick de MERAKKI utilise **Overdrive** | HC-06, BH-01, BH-03, BH-04, BH-07, AF-04 ; HC-05 (Overdrive) |
| Phase | **PHASE 0°, RAND 0** (Octocap, TURNCLOAK) ; Loïc passe de RAND 100 % à 0 (phase fixe) | HC-09, BH-07, BH-05 |

**Durées déduites** [CALCUL, en supposant qu'un LFO en ENVELOPE joue un seul cycle à la fréquence affichée] : 6,2 Hz = 161 ms ; 3,4 Hz = 294 ms ; 43,7 Hz = 22,9 ms ; 47,0 Hz = 21,3 ms ; 48,5 Hz = 20,6 ms ; 25,7 Hz = 38,9 ms. À 140 BPM, 1/8 = 214 ms et 1/16 = 107 ms ; à 120 BPM, 1/4 = 500 ms, 1/8 = 250 ms, 1/16 = 125 ms.

**Conséquence pour la signature** (`signature.md`, réglage du 5 octobre : ENV 2 → CRS +24 demi-tons, decay 40 ms ; ENV 1 hold 70 ms ; clic NOISE niveau 20). Le hold de 70 ms est dans la plage des captures (50 ms chez Octocap, 94 ms chez Loïc). Le **decay de 40 ms d'ENV 2 est plus court que les chutes de hauteur capturées (65 à 197 ms)** et proche de la durée des clics (21 à 39 ms) : c'est un réglage de chute brève, du côté « clic ». Aucune capture ne donne le niveau du NOISE. Rien de cela n'est une écoute : le réglage a été validé à l'écoute par l'utilisateur, pas par ces valeurs.

**Nuancé ou contredit**

- **ENV 1 est souvent à ses valeurs d'usine** (0,5 ms / 0 / 1,00 s / 100 % ou 0,0 dB / 15 ms, MERAKKI à 1,0 ms) à l'instant capturé dans 6 vidéos : HC-06, AF-01, BH-02, BH-03 (1:24, avant de passer à 763 ms), BH-06 et BH-07. Dans trois d'entre elles, l'amplitude est portée par **un LFO en ENVELOPE sur le niveau de l'oscillateur** : PML (LFO 1 → A Level), Strob (LFO 2 → niveau de A, 3:54) et Wildcrow (LFO 2 → niveau de A). Pour les autres, la cible du LFO n'est pas lisible. Les valeurs « hold / decay » de l'architecture commune (ENV 1) décrivent l'autre voie : n'en choisir qu'une par kick.
- **Phase de MERAKKI et de PML.** À 1:23 (AF-01, HC-05) et 3:40 (HC-06, AF-02), l'écran montre **PHASE 180°, RAND 100 %**. Le corpus écrit « 90°, au pic de l'onde, RAND 0 » pour AF-01 (`kicks/kicks-signature-sous-124.md`, règle 3). La capture n'est qu'un instant (valeurs peut-être d'Init avant réglage) : **non tranché, à relire dans la vidéo avant de recopier cette phase**. Un RAND à 100 donne un clic et un timbre différents à chaque note, contraire à l'idée de kick identique à chaque coup.
- **Unité de la chute de hauteur.** Les infobulles montrent des formes différentes : « Env 1 → A CoarsePit **48** » (Ghosthack, Serum 1), « LFO 2 → A Coarse Pitch **19 %, range +24** » (DNB Academy, Serum 2). La quantité se lit donc en demi-tons ou en pourcentage de la plage selon la version : lire l'infobulle de Serum 2, ne pas recopier le nombre.
- **Octave de la note jouée.** W. A. Production joue « G0 » (clip MIDI) : en nomenclature de Live (C3 = 60), G0 = MIDI 31, soit 49,0 Hz [CALCUL]. TURNCLOAK affiche **≈ 44 Hz (F1)** à l'analyseur : nomenclature scientifique, F1 = 43,65 Hz = MIDI 29, que Live nomme F0 [CALCUL]. Le numéro MIDI fait foi (règle 3 d'`AGENTS.md`).
- **Chaîne TURNCLOAK** (BH-07, Serum 2) : Equalizer (210 Hz, Q 60) → Distortion Tube → **Compressor Single** (seuil −32,9 dB, 4:1, attaque 90,1, release 9,7, gain 0) → Distortion. Une chaîne de deux distorsions autour d'un compresseur : à n'essayer qu'avec le sub séparé.
- **Hors Serum** : DONKONG ajoute ShaperBox 3 (présent dans l'inventaire) ; Octocap, EQ Eight et ShaperBox pour visualiser ; Strob, Pro-C 2 (non vérifié sur le Mac) ; Ableton Freeze. Dans les chaînes de mix du projet, les natifs se remplacent par des plug-ins tiers (règle 6 d'`ableton-live-session`).

**Encore non lu à l'écran** : les 34 autres vidéos du corpus, dont toutes les fiches DM (DM-01 à DM-06) et la plupart des fiches TE et RA.

## Par style

| Style | Ce qui est propre au style dans le corpus | Fiches à lire d'abord |
| --- | --- | --- |
| Bass house (BH) | aucun tutoriel propre au style ; kicks EDM punchy et saturés : distorsion sur le transitoire par ENV 2 → DRIVE (BH-01), Hard Clip à 100 % + Bend+ (BH-04), couche « Monster » distordue (BH-05) | BH-01, BH-04, BH-05 |
| House classique (HC) | 808 court pour house ou techno (HC-01), recréation TR-808 (HC-02), longueur d'une croche à 125 BPM (HC-03), base 909 sans distorsion jusqu'à 5:59 (HC-12) | HC-01, HC-03, HC-08, HC-12 |
| Tech house (TH) | 3 tutoriels seulement nomment la tech house ou la house (TH-01 à TH-03) ; distorsion à mix réduit pour garder un sub propre | TH-01, TH-02, TH-03 |
| Techno (TE) | le style le mieux couvert (15 vidéos) : rumble, warehouse, industriel, hard techno, 909 ; plusieurs en Serum 2 | TE-01, TE-04, TE-05, TE-06 |
| Rave (RA) | surtout rave techno (909 distordue, warehouse, industriel, reverse bass, tekno, hardtekk) ; aucun UK rave ni acid rave | RA-01, RA-06, RA-08 |
| Future bass, future rave (FB) | kicks big room et EDM (FB-01, FB-02, FB-05) ; aucun kick future bass ou future rave fait dans Serum | FB-01, FB-02, FB-05 |
| Deep, minimal, microhouse (DM) | kicks génériques au rendu rond, court, peu distordu, filtrés ; base de la fiche signature ci-dessus | DM-01 à DM-05 |
| Afro house (AF) | aucun kick afro fait dans Serum (les tutoriels afro prennent un sample) ; kicks ronds à couche organique, 4 sur 5 en Serum 2 | AF-01 à AF-05 |

## Limites

- Les captures d'écran ne couvrent que **12 des 46 vidéos** (`kicks-serum-captures.md`) et aucune fiche DM : pour les autres, les valeurs non dites restent inconnues. La liste « À vérifier à l'écran » de chaque fiche donne les minutages.
- Les fiches sans transcription (HC-11 = DM-07, TE-15, RA-15) n'apportent aucune valeur.
- Les traitements hors Serum cités par les vidéos sont souvent natifs de Live (Glue Compressor, Saturator, OTT d'Ableton, Drum Buss). Dans les chaînes de mix du projet, ils se remplacent par des plug-ins tiers (règle 6 d'`ableton-live-session`).
- Les styles où le corpus est générique (BH, DM, AF, FB) demandent une vraie référence choisie avec l'utilisateur, puis une comparaison à niveau égal.
