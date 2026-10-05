# Kicks dans Serum : synthèse de 46 tutoriels

Synthèse du corpus `kicks-serum-tutoriels.md`, rédigée le 05/10/2026. Ce corpus compte 85 fiches pour 46 vidéos différentes, en 8 styles, étudiées dans Claude in Chrome sur le Mac, son coupé. Les identifiants (BH-01, HC-08, DM-02…) renvoient aux fiches du corpus.

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Les valeurs viennent des transcriptions : ce qui est **dit**, parfois mal transcrit (marqué [ASR ?] dans le corpus). Les captures d'écran ne sont pas encore faites : chaque fiche du corpus finit par la liste des minutages « À vérifier à l'écran ».

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

Quand l'utilisateur valide un kick à l'écoute, l'inscrire au registre `signature.md` (chemin du preset, réglages, accord, morceau, date).

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

- Aucune capture d'écran n'est encore faite : les valeurs non dites restent inconnues. La liste « À vérifier à l'écran » de chaque fiche donne les minutages.
- Les fiches sans transcription (HC-11 = DM-07, TE-15, RA-15) n'apportent aucune valeur.
- Les traitements hors Serum cités par les vidéos sont souvent natifs de Live (Glue Compressor, Saturator, OTT d'Ableton, Drum Buss). Dans les chaînes de mix du projet, ils se remplacent par des plug-ins tiers (règle 6 d'`ableton-live-session`).
- Les styles où le corpus est générique (BH, DM, AF, FB) demandent une vraie référence choisie avec l'utilisateur, puis une comparaison à niveau égal.
