# Dix recettes de kick Serum 2 pour la big room, la future house, la future rave et la future bass

Quatrième lot de kicks : les kicks EDM et festival. Ce fichier n'a que dix recettes, parce que la fiche FB du corpus est mince. Neuf de ses quatorze vidéos sont déjà traitées dans les fichiers précédents. Aucun tutoriel ne conçoit un kick « future bass » ou « future rave » dans Serum ; seuls la big room (FB-01, FB-02), le kick EDM « façon Hardwell » (FB-05) et le duo future bass DONKONG (FB-08, FB-09) sont propres au style. Le tableau des renvois indique, pour chaque vidéo déjà traitée, la recette d'un autre fichier qui l'utilise. Rédigé le 05/10/2026. Sources :
- `../kicks-serum-tutoriels.md`, fiche FB, et sa synthèse `../kicks-serum-synthese.md` ;
- `../../../kick-bass-equilibre/SKILL.md` ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `kicks-signature-sous-124.md`.

## Règles

1. **Règles communes du lot de kicks** : celles de `kicks-signature-sous-124.md`.
2. **Un kick big room est un kick et une basse** [SOURCE FB-02] : un punch court, puis une queue tonale qui porte la note. Deux approches [SOURCE FB-05] :
   - queue courte et basse séparée ;
   - queue longue qui porte le sub, « façon Hardwell ».

   La seconde fait tenir le grave au kick (`../../../kick-bass-equilibre/SKILL.md` § 1) : pas de sub séparé sous le kick, ou un sub qui joue seulement entre les kicks.
3. **Le kick se finit tard** : faire un kick de base, produire le morceau, puis affiner le kick vers 75-80 % de la production [SOURCE FB-05].
4. **Pas trop de distorsion**, sinon le « thud » initial devient craquant, mais assez pour que la basse ne se perde pas [SOURCE FB-01, description].
5. **Tempos** : la fiche FB-07 situe la future house et la future rave vers 125-128 BPM ; le projet de DONKONG tourne à 158 BPM [SOURCE FB-08]. À 128 BPM, la croche dure 234,4 ms ; à 158 BPM, 189,9 ms et la double croche 94,9 ms [CALCUL].

## Tableau des renvois

| Vidéo du corpus | Recette qui l'utilise |
| --- | --- |
| FB-03 = BH-01 (W. A. Production, kick EDM punchy) | KH02 de `kicks-house-bass-house.md` |
| FB-04 = BH-04 (Wildcrow, deux sinus, Hard Clip) | KH05 ; version douce KS08 |
| FB-05 = BH-02 (Strob Studio, kick EDM) | KH03 ; ici KF05 et KF06 pour les deux approches de queue |
| FB-06 = BH-05 (Mixup Studio, couche Monster) | KH06 |
| FB-07 = HC-03 (SKETIMUSIC) | KH11 ; ici KF07 recalé à 128 BPM |
| FB-10 = AF-04 (Ghosthack, couche foley) | KS17 de `kicks-signature-sous-124.md` |
| FB-11 = HC-10 (Arc Nade) | KS05 |
| FB-12 = HC-06 (Production Music Live) | KH14 |
| FB-13 = HC-09 (Octocap) | KS07 |
| FB-14 = BH-07 (TURNCLOAK) | KH08 |

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| KF01 | Big room Jinus | big room, future rave | sinus, pitch 25, LFO « bang bang » |
| KF02 | Big room tonal Husman | big room | punch en sample, queue tonale par la table |
| KF03 | Clic en couche dans Serum | big room, EDM | clic en sample sur OSC C, passe-haut à 200 Hz |
| KF04 | Kick tonal qui suit l'harmonie | big room | une note par phrase de 4 ou 8 mesures |
| KF05 | Kick EDM à queue de scie | EDM, future rave | kick court, queue de scie pilotée en sidechain |
| KF06 | Kick sec qui porte le sub | EDM, big room | queue longue, pas de sub dessous |
| KF07 | Kick future house à 128 BPM | future house, future rave | SKETIMUSIC recalé, croche de 234 ms |
| KF08 | Kick future bass DONKONG | future bass | FM brève, courbe médiane, soft clip |
| KF09 | Transitoire adouci par all-pass | future bass | LFO rapide sur le MIX d'un all-pass |
| KF10 | Du kick à la 808 | future bass | table maison, MONO + LEGATO |

## Les dix recettes

### KF01 Big room Jinus — sinus, pitch 25, LFO « bang bang »
- **OSC A** : sinus ; ENV 1 : sustain tout en bas, decay réglé.
- **Hauteur** : une enveloppe → pitch, Option-clic (unipolaire), quantité 25 (« I like it at 25 », unité à lire dans la matrice) ; decay de l'enveloppe un peu baissé.
- **Amplitude et filtre** : LFO 1 dessiné en forme rythmique « bang bang » → LEVEL ; filtre baissé, LFO 1 aussi → CUTOFF.
- **FX** : Distortion Soft Clip légère ; impression en audio.
- **Clic** : un sample de clic par-dessus pour le haut et les médiums, grave coupé jusqu'à ≈ 200 Hz sur le clic (KF03 le fait dans Serum).
- **Après** : saturation au choix (chaleur), puis compression, par plug-ins tiers.
- **Macros** : `Pitch Decay` decay de l'enveloppe de pitch · `Cutoff Decay` profondeur de LFO 1 → CUTOFF · `Click` DRIVE du Soft Clip · `Release` dernier point de LFO 1.
- **Origine** : [SOURCE FB-01, Jinus Music, Serum 1, vidéo de 90 s].

### KF02 Big room tonal Husman — punch en sample, queue tonale
- **Punch** : un kick punchy en sample, raccourci pour coller à la basse (la vidéo le prend dans son pack).
- **Queue tonale** dans Serum : un patch de type « electro trance bass » ; une table à beaucoup de frames, parcourue par WT POS ; ENV 2 → WT POS (du bas vers le haut), quantité réduite.
- **Filtre** : si la table ne s'atténue pas d'elle-même vers la fin, LFO 3 → CUTOFF, du début à la fin de la note.
- **Grave** : SUB de Serum ajouté.
- **Pourquoi dans Serum** : les kicks big room changent de note toutes les 4 ou 8 mesures, sans perte de qualité, alors qu'un sample pitché se dégrade (KF04).
- **Macros** : `Pitch Decay` — · `Cutoff Decay` profondeur de LFO 3 · `Click` niveau du sample de punch · `Release` quantité d'ENV 2 → WT POS.
- **Origine** : [SOURCE FB-02, Husman, Serum 1] : kick big room « façon Hardwell, Dimitri Vegas & Like Mike ».

### KF03 Clic en couche dans Serum — passe-haut à 200 Hz
- **Patch** : KF01 ou KH01 (`kicks-house-bass-house.md`), avec un clic en couche **dans** Serum :
  - OSC C en mode Sample, One Shot, un clic d'usine (Factory › non-tonal › attack) ou un clic dont la licence est vérifiée ;
  - FILTER 2 sur C seul, passe-haut à ≈ 200 Hz ;
  - un LFO en ENVELOPE très court → LEVEL de C.
- **Macros** : `Click` LEVEL de C · les autres comme la recette de départ.
- **Test** : le clic ne doit pas gêner le grave du kick ; le passe-haut sert à cela.
- **Origine** : clic en sample, grave coupé jusqu'à ≈ 200 Hz [SOURCE FB-01] ; sample d'attaque dans OSC C [SOURCE HC-06] ; le faire dans Serum plutôt que sur une piste à part [DÉDUCTION].

### KF04 Kick tonal qui suit l'harmonie — une note par phrase
- **Patch** : KF02 ou KF06.
- **Jeu** : la note du kick suit la fondamentale de l'accord de chaque phrase de 4 ou 8 mesures ; le suivi de hauteur de l'oscillateur reste actif (l'inverse de KS14).
- **Test** : sur chaque note, la queue tonale ne doit pas frotter avec la basse ; vérifier à l'accordeur.
- **Jeu** : bloc « Big room 128 — kick tonal sur la fondamentale de chaque phrase » ci-dessous.
- **Macros** : celles de la recette de départ.
- **Origine** : « les big room kicks changent de note toutes les 4 ou 8 mesures » [SOURCE FB-02] ; écriture [ORIGINAL].

### KF05 Kick EDM à queue de scie — la méthode « plus pro »
- **Kick court** : KH03 de `kicks-house-bass-house.md` (Master Tune, creux d'amplitude, clic de second sinus).
- **Queue** sur un autre oscillateur, ou un second Serum sur une autre piste :
  - une scie (riche en harmoniques paires et impaires, audible sur petits haut-parleurs) routée dans le filtre ;
  - LFO 4 en ENVELOPE, synchronisé, une noire → LEVEL de la queue : il laisse passer le punch puis remplit, « comme un sidechain » ;
  - filtre à pente plus raide pour retirer des harmoniques.
- **Plus de clic** : NOISE, banque d'attaques de kick, One Shot, pitché haut.
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` CUTOFF du filtre de la queue · `Click` niveau du NOISE · `Release` profondeur de LFO 4.
- **Origine** : [SOURCE FB-05 = BH-02, Strob Studio, Serum 1, en français] : « kick court + tail sur un autre oscillateur ».

### KF06 Kick sec qui porte le sub — queue longue, pas de sub dessous
- **Patch** : KF05 sans la queue de scie, avec la queue du sinus allongée : ENV 1 (ou le LFO de volume) tenue jusqu'à la croche suivante ou au-delà.
- **Note** : sur la tonique, dans le registre du sub (45-65 Hz) ; la fondamentale du kick « entre ≈ 45 Hz et 60-65 Hz selon le morceau » [SOURCE FB-05].
- **Grave** : pas de sub séparé sous le kick ; la basse joue au-dessus de 80-100 Hz ou entre les kicks (`../../../kick-bass-equilibre/SKILL.md` § 1).
- **Macros** : `Release` longueur de la queue · les autres comme KF05.
- **Test** : accorder kick et basse ensemble ; mesurer l'énergie sous 60 Hz du kick avec `kick_bass_check.py`.
- **Origine** : « tail long qui porte le sub (façon Hardwell, kick sec) » [SOURCE FB-05, 8:23].

### KF07 Kick future house à 128 BPM — SKETIMUSIC recalé
- **Patch** : KH11 de `kicks-house-bass-house.md` (Analog_BD_Sin, LFO 1 → Master Tune en bipolaire, Multiband, MG Low 18, Soft Clip, FM triangle), avec :
  - longueur d'une croche à 128 BPM : hold ≈ 117 ms, decay ≈ 117 ms [CALCUL, × 125/128] ;
  - forme de LFO 1 : chute dans la première double croche, nouvelle chute dans la deuxième, queue sur la dernière croche [SOURCE FB-07].
- **Macros** : celles de KH11.
- **Usage** : future house et future rave à 126-128 BPM.
- **Origine** : [SOURCE FB-07 = HC-03, SKETIMUSIC, Serum 1, testé à 125 BPM] ; recalage [CALCUL].

### KF08 Kick future bass DONKONG — FM brève, courbe médiane
- **Patch** : KH07 de `kicks-house-bass-house.md` (deux sinus, FM (B) sur A, LFO en ENVELOPE 1/8 → pitch, macro sur la PHASE pour le clic, macro sur la FM, soft clip final).
- **Longueur** : 1/8 ou 1/16 du morceau, à 158 BPM : 189,9 ms ou 94,9 ms [CALCUL].
- **Soft clip** : on peut doser combien de la queue est clippée : punch dur au début, queue propre [SOURCE].
- **Macros** : celles de KH07.
- **Jeu** : bloc « Future bass 158 — du kick à la 808 » ci-dessous.
- **Origine** : [SOURCE FB-08 = BH-06, DONKONG, Serum 1, 158 BPM] : le kick de base que le duo superpose ensuite dans ses morceaux.

### KF09 Transitoire adouci par all-pass — moins « digital »
- **Patch** : KF08, avec :
  - un filtre All-Pass (déphasage) sur le transitoire ;
  - LFO 2, le plus rapide → MIX du filtre : il n'agit que sur les premières millisecondes ;
  - le tout sur la Macro 3 (matrice : LFO 2 → MIX du filtre, quantité réglée par la Macro 3) ;
  - le niveau du NOISE aussi sur la Macro 3 ; bruit « J60 » dans la vidéo.
- **Macros** : `Click` = Macro 3 de la source · les autres comme KH07.
- **Test** : A/B avec KF08 ; le transitoire doit paraître moins « digital ».
- **Origine** : [SOURCE FB-09, DONKONG, Serum 1].

### KF10 Du kick à la 808 — table maison, MONO + LEGATO
- **Patch** : KF08 ou KF09, puis :
  - allonger par LFO 3 (LEVEL) ou en remontant un point de l'enveloppe de volume ; baisser un peu le pitch bend ;
  - table plus riche en harmoniques (« comme un 808 distordu ») ; ou une table maison : Basic Shapes sinus › « Remove all except selected », changer la phase, petits paliers dessinés sur la première frame, plus extrêmes sur la deuxième, puis « Morph Spectral » ;
  - WT POS modulée par un LFO en ENVELOPE de 1 à 2 mesures (mouvement) ;
  - petite attaque, pour que le punch ne sature pas à cause de la table riche ;
  - MONO + LEGATO pour jouer la 808.
- **Macros** : `Release` longueur (LFO 3) · `Cutoff Decay` profondeur du LFO → WT POS · les autres comme KF08.
- **Jeu** : bloc « Future bass 158 — du kick à la 808 » ci-dessous.
- **Origine** : [SOURCE FB-09, DONKONG, Serum 1] : couple kick et 808 du future bass.

## Motifs vérifiés

Numérotation de Live (C3 = 60) ; les notes de kick sont les fondamentales visées. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/kicks/kicks-big-room-future.md`.

```grille
titre: Big room 128 — kick tonal sur la fondamentale de chaque phrase (KF02, KF04)
tempo: 128
accords: Fm | Db
kick: F1[1:3] F1[2:3] F1[3:3] F1[4:3] | Db1[1:3] Db1[2:3] Db1[3:3] Db1[4:3]
```

Deux mesures pour deux phrases : en pratique, une note par phrase de 4 ou 8 mesures. Chaque kick tient trois doubles croches (352 ms à 128 BPM) : le punch, puis la queue tonale.

```grille
titre: Future bass 158 — du kick à la 808 (KF08, KF10)
tempo: 158
accords: Fm7 | Dbmaj7
kick808: F0[1:6] Ab0[2&:4] C1[3&:6] | Db1[1:6] F0[2&:6] Ab0[4&:2]
```

Un seul patch joue le kick et la 808 : chaque note commence par le punch, puis tient la note en MONO + LEGATO. Les notes suivent les accords (Fm7, puis Dbmaj7).

```grille
titre: Future house 128 — kick d'une croche et basse en contretemps (KF07)
tempo: 128
accords: Fm7 | Fm7
kick: C1[1:2] C1[2:2] C1[3:2] C1[4:2] | C1[1:2] C1[2:2] C1[3:2] C1[4:2]
basse: F1[1&:1] F2[2&:1] F1[3&:1] Ab1[3a:1] C2[4&:1] | F1[1&:1] F2[2&:1] F1[3&:1] Eb2[4&:1] C2[4a:1]
```

Le kick dure une croche (234 ms) ; la basse médium joue les contretemps, comme le pluck en octaves de `../../../serum-2-basses-house-future-house/references/motifs.md`.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : la table « electro trance bass » de Husman (ou une table à beaucoup de frames), le bruit « J60 », le filtre All-Pass, la commande « Remove all except selected » et le « Morph Spectral » de l'éditeur de tables.
- Choisir avec l'utilisateur une référence big room, future house ou future rave pour le kick (le corpus n'en donne aucune conçue dans Serum).
- Écouter les recettes dans le morceau, à niveau égal ; mesurer kick et basse sur des exports séparés ; inscrire le kick validé au registre `../signature.md`.
