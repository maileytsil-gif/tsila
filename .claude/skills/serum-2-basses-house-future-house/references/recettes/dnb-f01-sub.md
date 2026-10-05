# Vingt recettes de sub pour la Drum and Bass (famille F01)

Sixième et dernier lot DnB : le sub sous les neuros, Reese, foghorns, rollers, liquids et jump-ups des fichiers `dnb-*.md`. La plupart des patchs viennent de `house-f01-sub.md` et de `dubstep-f01-sub.md` ; ce fichier les règle pour la DnB à 174 BPM :
- notes rapprochées et lignes qui roulent ;
- kick en 2-step (temps 1 et 3&), caisse claire sur 2 et 4 ;
- couches médium qui gardent souvent un grave plein dans les tutoriels ;
- coupures et plongées de fin de phrase.

Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F01-01 Art1fact, F02-01 DNB Academy, F14-02 MilleniumBE, F15-02 ERB N DUB ;
- `../etudes-pages-dubstep-dnb.md` : F15-06 EDMProd (liquid), F14-09 et la page foghorn d'Attack Magazine, F13-11 Computer Music ;
- `../etudes-pages-house.md` et `../etudes-captures.md` : F01-02 Monosounds (808), F01-13 EDMProd (sub) ;
- l'extrait du registre F01-10 Beatportal ;
- `../../../sound-designer-serum/references/basses.md` § 1 et la cartographie de Serum 2.

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot DnB** : celles de `dnb-f13-neuro.md`. **Règles du sub** : celles de `house-f01-sub.md` :
   - un oscillateur, sans unison ni désaccord, mono ;
   - PHASE 0 % ;
   - sub sur sa propre piste ;
   - contrôle en mono et à faible volume.
2. **Ce que font les tutoriels, et ce qu'on en garde.**
   - Sub routé dans le filtre de la basse [SOURCE F02-01] ; sub modulé en niveau par un LFO à −40 [SOURCE F13-11] ; SUB à −1 octave en `Direct` dans le patch [SOURCE F14-02] : ces rôles passent ici au sub de sa piste.
   - « Sub sinus pur, mono, passe-bas vers 80 Hz, couche médium séparée » [EXTRAIT F01-10, Beatportal, page non lue] et « un sub constant à part » [SOURCE F14-09] : c'est l'architecture retenue.
   - Un SUB à LEVEL 0 qui ne sert que de modulateur FM (F15-02) reste dans son patch : il ne sonne pas.
3. **Tonalité** : Fa mineur fréquent, « notes autour de F0 » [SOURCE F15-06] ; F0 = 43,7 Hz, E0 = 41,2 Hz. Art1fact place son sub « vers 40 » sur l'analyseur (unité non dite, Hz probable) [SOURCE F01-01]. Choisir la tonique et l'octave avec `../../../theorie-musicale-electronique/scripts/theorie.py sub <tonique>`.
4. **Notes rapprochées** : release de 20 à 30 ms pour des notes rapprochées, de 50 à 100 ms pour des notes espacées (`basses.md` § Sub). À 174 BPM, une double croche dure 86,2 ms et une croche 172,4 ms [CALCUL].
5. **Quatre macros communes**, celles de `house-f01-sub.md` : `Length`, `Glide`, `Weight`, `Knock`.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| DS01 | Sinus Direct DnB | référence | release 30 ms |
| DS02 | Phase continue | rollers, lignes roulantes | Contiguous |
| DS03 | Sub ducké en 2-step | drop | creux sur 1 et 3& |
| DS04 | Sinus pur passe-bas | toutes | LP 80 Hz après la saturation |
| DS05 | Sub constant sous le foghorn | foghorn, horn | même note, aucun mouvement |
| DS06 | Sub sous le neuro | neuro | fondamentales seulement, sans glissé |
| DS07 | Sub sous le Reese | Reese | même ligne une octave plus bas |
| DS08 | Sub liquid tenu | liquid | attaque ronde, release long |
| DS09 | Sub vers 40 Hz | toutes | tonique et octave choisies |
| DS10 | Octave fantôme | téléphones | 2e harmonique dosée |
| DS11 | Sinus saturé parallèle | sub lourd | Soft Sat. à faible mix |
| DS12 | Sub court | jump-up, rafales | decay d'une double croche |
| DS13 | 808 DnB | jump-up, crossover | knock +24, decay court |
| DS14 | Glissé d'octave | lignes à glissés | PORTA SCALED 80-120 ms |
| DS15 | Plongée de fin de phrase | fin de phrase | CRS −5 sur la dernière note |
| DS16 | Silence et retour | avant le drop | coupure de deux temps |
| DS17 | Sub accordé au kick | toutes | tonique et octave par le calcul |
| DS18 | Petit wobble ponctuel | fin de phrase liquid | niveau sur une mesure |
| DS19 | Phase alignée avec la médium | médium à grave plein | PHASE 0 ou 180° |
| DS20 | Sinus FM 1:1 | sub chaud | 2e harmonique |

## Les vingt recettes

### DS01 Sinus Direct DnB — référence
- **Patch** : S01 de `house-f01-sub.md` : SUB en Sine, PHASE 0 %, `Direct`, MONO.
- **ENV 1** : attaque 2 ms, sustain 0 dB, release 30 ms (notes rapprochées).
- **Macros** : `Length` release 15 → 80 ms · `Glide` 0 → 60 ms · `Weight` — · `Knock` —.
- **Jeu** : bloc « DnB 174 — sub 2-step » ci-dessous.
- **Test** : chaque note au même niveau ; écouter la fin de queue avant la note suivante.
- **Origine** : S01 [`house-f01-sub.md`] ; release pour notes rapprochées (`basses.md` § Sub).

### DS02 Phase continue — sous un roller
- **Patch** : S02 de `house-f01-sub.md` : PHASE du SUB en Contiguous, attaque 1-2 ms, release 30 ms.
- **Jeu** : bloc « DnB 174 — sub roulant à phase continue » ci-dessous.
- **Test** : A/B avec DS01 sur une ligne en croches jointives : DS02 doit cliquer moins entre deux notes, mais son attaque varie.
- **Macros** : celles de S02.
- **Origine** : Contiguous [cartographie, § 3.7] ; S02 ; sous RL01 à RL20 de `dnb-f15-rolling-liquid.md`.

### DS03 Sub ducké en 2-step — creux sur le kick
- **Patch** : S10 de `house-f01-sub.md`, avec LFO 1 en FREE, HOST, MONO, RATE 1 mesure (1 379,3 ms).
  - Forme : deux creux, l'un au début (kick du temps 1), l'autre à 10/16 de la mesure (kick du 3&).
  - Chaque creux revient à 1 en ≈ 86 ms (une double croche, 6,25 % de la mesure) [CALCUL].
- **ENV 1** : attaque 2 ms, release 30 ms.
- **Macros** : `Weight` profondeur des creux, 0 → −100 · les autres comme DS01.
- **Test** : relancer la lecture à plusieurs endroits ; les creux doivent tomber sur les kicks. Sur un break qui ne suit pas le schéma, préférer un sidechain par plug-in tiers déclenché par le vrai kick.
- **Origine** : S10 [`house-f01-sub.md`] ; SB02 de `dubstep-f01-sub.md` ; schéma 2-step des règles communes [DÉDUCTION].

### DS04 Sinus pur passe-bas — après la saturation
- **Patch** : DS01, avec FILTER 1 en MG Low 24 sur le SUB, CUTOFF 80 Hz, key track éteint, sortie du filtre en `Direct`.
- **ENV 1** : comme DS01.
- **Macros** : `Weight` CUTOFF 60 → 120 Hz · les autres comme DS01.
- **Test** : un sinus pur n'a pas d'harmoniques à couper ; le passe-bas sert après une saturation (DS11) ou pour une note haute de la ligne.
- **Origine** : « sub sinus pur, mono, passe-bas vers 80 Hz, couche médium séparée » [EXTRAIT F01-10, Beatportal, page non lue].

### DS05 Sub constant sous le foghorn — aucun mouvement
- **Patch** : DS01, sans LFO, sans glissé.
- **ENV 1** : attaque 3 ms, release 100 ms (notes longues du foghorn).
- **Jeu** : même note que le foghorn, une octave plus bas si le foghorn joue F1 ; même octave si la page d'Attack Magazine est suivie (F0 dans les deux) : dans ce cas, couper le foghorn sous 100 Hz.
- **Macros** : celles de DS01.
- **Origine** : « sinus de sub sur la même note, piste séparée », sub hors de la distorsion [SOURCE page foghorn d'Attack Magazine] ; « un sub constant à part » [SOURCE F14-09].

### DS06 Sub sous le neuro — fondamentales seulement
- **Patch** : DS01 ou DS02.
- **Jeu** : le sub ne joue que les notes graves de la ligne, en tenues de trois ou quatre doubles croches ; il ne suit ni les rafales (NR08), ni les notes à l'octave, ni les glissés (NR14).
- **ENV 1** : attaque 2 ms, release 40 ms.
- **Macros** : celles de DS01.
- **Test** : couper le neuro ; la ligne de sub seule doit tenir l'harmonie.
- **Origine** : « un grave solide et constant (sinus ou triangle mêlé, ou sinus séparé dessous) » [SOURCE F13-11, conseil] ; SB18 de `dubstep-f01-sub.md`.

### DS07 Sub sous le Reese — même ligne, une octave plus bas
- **Patch** : DS01.
- **Jeu** : même ligne MIDI que le Reese, une octave plus bas ; le Reese est coupé vers 100-120 Hz.
- **ENV 1** : attaque 2 ms, release 60 ms.
- **Macros** : celles de DS01.
- **Test** : en mono, le niveau du grave ne doit pas fluctuer au vumètre ; s'il fluctue, le Reese descend encore trop bas.
- **Origine** : « jouer la fondamentale sinus avec un synthé séparé » [SOURCE LANDR, `basses.md` § 2] ; règle 1 de `house-f02-reese.md`.

### DS08 Sub liquid tenu — attaque ronde
- **Patch** : S13 de `house-f01-sub.md` : attaque 10-15 ms, courbe concave, release 150 ms.
- **Jeu** : bloc « DnB 174 — liquid sur quatre accords » de `dnb-f15-rolling-liquid.md` (voix `sub`).
- **Macros** : `Length` release 80 → 300 ms · les autres comme DS01.
- **Test** : l'attaque du kick reste nette, sans creux de niveau entre kick et sub ; mesurer avec `kick_bass_check.py` (`../../../kick-bass-equilibre/SKILL.md`).
- **Origine** : S13 ; tenues de 6 temps de la ligne liquid [SOURCE F15-06, capture].

### DS09 Sub vers 40 Hz — tonique et octave choisies
- **Patch** : DS01.
- **Méthode** : choisir la tonique pour que les notes principales tombent entre E0 (41,2 Hz) et A0 (55 Hz) ; F0 (43,7 Hz) pour Fa mineur.
- **Test** : sur l'analyseur, le pic principal du sub doit se lire « vers 40 » Hz comme chez Art1fact ; les notes sous E0 se remontent d'une octave si le système ne les porte pas.
- **Macros** : celles de DS01.
- **Origine** : « vers 40 » sur SPAN [SOURCE F01-01] ; notes autour de F0 [SOURCE F15-06] ; zone F0-A0 [SOURCE F01-13, écran].

### DS10 Octave fantôme — pour les téléphones
- **Patch** : S05 de `house-f01-sub.md` : SUB en sinus `Direct`, plus OSC A en sinus une octave au-dessus, niveau réglé à l'analyseur (pic à 2f entre −20 et −12 dB sous la fondamentale).
- **ENV 1** : comme DS01.
- **Macros** : celles de S05.
- **Test** : sur téléphone, la ligne de sub doit rester lisible quand la couche médium est coupée.
- **Origine** : S05 [`house-f01-sub.md`].

### DS11 Sinus saturé parallèle — sub lourd
- **Patch** : S06 de `house-f01-sub.md` : Distortion Soft Sat., DRIVE 20-40, MIX 25-40 %, LEVEL compensé ; puis le passe-bas de DS04.
- **Test** : la fondamentale ne doit pas baisser quand `Weight` monte.
- **Macros** : celles de S06.
- **Origine** : « la fondamentale faiblit avec la distorsion » [SOURCE F01-13] ; S06 ; « les distorsions de Serum ne marchent pas très bien dans le grave » [SOURCE F01-01].

### DS12 Sub court — sous le jump-up
- **Patch** : S11 de `house-f01-sub.md`, ENV 1 en BPM : decay 1/16 (86,2 ms à 174 BPM), sustain 0, release 1/64.
- **Jeu** : une note de sub par groupe de rebonds, sur le premier coup seulement.
- **Macros** : `Length` decay 1/32 → 1/8 · les autres comme DS01.
- **Origine** : S11 ; SB13 de `dubstep-f01-sub.md` ; durée [CALCUL].

### DS13 808 DnB — knock et decay court
- **Patch** : S08 de `house-f01-sub.md` : sinus, ENV 2 → CRS +24 en 60 ms, Overdrive 25 % / 60 %, passe-bas vers 400 Hz, MONO + LEGATO.
- **ENV 1** : attaque 0, decay 300-500 ms, sustain 0, release 60 ms, soit 0,9 à 1,45 noire à 174 BPM [ORIGINAL ; durée en CALCUL].
- **Glide** : PORTA 60-100 ms.
- **Macros** : celles de S08.
- **Test** : le knock ne doit pas doubler l'attaque du kick.
- **Origine** : [SOURCE F01-02, page et infographie] : +24 demi-tons / 60 ms, Overdrive 25 % / 60 %, LP 400 Hz après distorsion ; durées pour la DnB [ORIGINAL]. Le tutoriel « 808 façon LSB » du registre (F01-09) n'est pas étudié.

### DS14 Glissé d'octave — PORTA SCALED
- **Patch** : DS01, avec MONO + LEGATO, PORTA 80-120 ms, ALWAYS et SCALED allumés, CURVE convexe.
- **Test** : à 174 BPM, une croche dure 172,4 ms ; un glissé de 120 ms en occupe 70 % [CALCUL]. Réserver les glissés plus longs aux notes d'une noire.
- **Macros** : `Glide` 0 → 150 ms · les autres comme DS01.
- **Origine** : PORTA, SCALED, CURVE [cartographie, § 9] ; SB05 de `dubstep-f01-sub.md`.

### DS15 Plongée de fin de phrase — CRS −5 sur la dernière note
- **Patch** : S18 de `house-f01-sub.md` : MACRO 4 → CRS du SUB, de 0 à −12.
  - Dans Live, automatiser la macro jusqu'à −5 demi-tons sur la dernière note de la phrase, puis la remettre à 0 sur le temps 1.
- **Calcul** : F0 − 5 demi-tons = C0, 32,7 Hz, au-dessus de 30 Hz [CALCUL]. Une plongée sur la dernière noire dure 344,8 ms.
- **ENV 1** : attaque 2 ms, release 80 ms.
- **Macros** : `Knock` 0 → −12 demi-tons · les autres comme DS01.
- **Jeu** : bloc « DnB 174 — plongée de fin de phrase » ci-dessous.
- **Origine** : S18 ; SB06 de `dubstep-f01-sub.md` ; règle des drops d'`AGENTS.md`.

### DS16 Silence et retour — avant le drop
- **Arrangement** :
  - couper le sub sur les 2 derniers temps de la phrase de 16, avec la couche médium ;
  - le faire revenir sur le temps 1 du drop, avec la couche de clic de S16 si le kick du drop est doux.
- **Patch** : DS01, ou S16 de `house-f01-sub.md`.
- **Test** : le retour du sub coïncide avec le kick du drop, sans le doubler.
- **Origine** : « basse coupée 2 temps à la fin de la phrase de 16 » ; batterie et basse coupées sur les 2 dernières mesures d'un drop [SOURCE F15-06] ; SB12 de `dubstep-f01-sub.md`.

### DS17 Sub accordé au kick — tonique et octave par le calcul
- **Méthode** :
  1. Lancer `python3 ../../../theorie-musicale-electronique/scripts/theorie.py sub <tonique>` depuis le dossier de ce fichier (par exemple `sub F`).
  2. Choisir l'octave du sub pour que la tonique tombe dans F0-A0 si possible, sans descendre sous E0.
  3. Accorder le kick (`../../../kick-bass-equilibre/SKILL.md`).
- **Patch** : DS01.
- **Test** : la tonique du sub et la fondamentale du kick ne doivent pas battre l'une contre l'autre ; mesurer sur des exports séparés.
- **Origine** : SB17 de `dubstep-f01-sub.md` ; outils du dépôt.

### DS18 Petit wobble ponctuel — une mesure, en niveau seulement
- **Patch** : DS01, avec LFO 1 (1/4, RETRIG) → LEVEL du SUB, profondeur sur MACRO 3 (`Weight`), à 0 par défaut.
- **Jeu** : macro montée sur une seule mesure, en fin de phrase liquid.
- **Test** : jamais de modulation de hauteur ni de filtre sur le sub ; au-delà de 40 % de profondeur, le sub pompe.
- **Origine** : automation de la macro 2 du sub « pour un petit wobble » à la mesure 60 [SOURCE F15-06]. Dans l'article, cette macro agit sur un preset plein (« BS PWM Sub », RL03 de `dnb-f15-rolling-liquid.md`) ; sur un sinus seul, la réduire au niveau est une [DÉDUCTION].

### DS19 Phase alignée avec la médium — PHASE 0 ou 180°
- **Méthode** : quand une couche médium garde une part de fondamentale (RL01, DR02 à OCT −3, foghorn à OCT −2) :
  1. Mettre RAND 0 et PHASE 0 % sur la médium comme sur le sub.
  2. Exporter les deux pistes sur la même note.
  3. Mesurer leur corrélation dans 30-120 Hz.
  4. Si elle est négative, passer la PHASE du SUB à 50 % (180°), ou inverser la polarité d'une piste avec l'Utility de Live (toléré, `../tempo-mix.md`).
- **Test** : la somme mono doit être plus forte que chaque piste seule dans le grave.
- **Origine** : SB20 de `dubstep-f01-sub.md` ; phase alignée, exemple à 180° [SOURCE F01-13].

### DS20 Sinus FM 1:1 — sub chaud
- **Patch** : S20 de `house-f01-sub.md` : FM (Sub) 5-15 % sur un sinus, SUB à l'unisson en `None`, coupe-bas à 15-20 Hz contre la composante continue.
- **Macros** : `Weight` quantité de FM · les autres comme DS01.
- **Test** : A/B avec DS01 sur téléphone ; la deuxième harmonique doit rendre la ligne lisible sans brouiller le grave.
- **Origine** : rapport 1:1 [CALCUL, Synth Secrets 12-13] ; S20.

## Motifs vérifiés

Numérotation de Live (C3 = 60). DnB à 174 BPM : kick sur les doubles croches 1 et 11, caisse claire sur 5 et 13 (règles communes de `dnb-f13-neuro.md`). Aucune attaque de sub sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dnb-f01-sub.md`.

```grille
titre: DnB 174 — sub 2-step (DS01, DS03)
tempo: 174
accords: Fm7 | Fm7
sub: F0[1e:7] F0[3a:5] | Ab0[1e:7] Eb0[3a:4] F0[4a:1]
```

Le sub attaque juste après chaque kick (doubles croches 2 et 12) : la variante sans ducking de DS03. Recaler sur le vrai break.

```grille
titre: DnB 174 — sub roulant à phase continue (DS02)
tempo: 174
accords: Fm7 | Fm7
sub: F0[1:3] F0[1a:3] Ab0[2&:2] F0[3:3] F0[3a:3] Eb0[4&:2] | F0[1:3] F0[1a:3] C1[2&:2] Bb0[3:3] Ab0[3a:3] F0[4&:2]
```

Notes jointives de deux ou trois doubles croches ; avec Contiguous, la phase passe d'une note à l'autre. Le si bémol de la mesure 2 est une note de passage.

```grille
titre: DnB 174 — plongée de fin de phrase (DS15, DS16)
tempo: 174
accords: Fm7 | Fm7
sub: F0[1:10] Ab0[3a:5] | F0[1:8] Eb0[3:3] F0[3a:1] F0[4e:3]
```

Mesures 7-8 d'une phrase de 8. La dernière note (F0 sur la double croche 14, 259 ms) porte la plongée de DS15, jusqu'à C0 (32,7 Hz). En fin de phrase de 16, remplacer la mesure 8 par la coupure de deux temps de DS16.

## Ce qui reste à faire par l'utilisateur

- Vérifier dans Serum 2 : PHASE et Contiguous du SUB, la modulation de CRS par une macro, le LFO à deux creux de DS03.
- Choisir la tonique avec `theorie.py sub`, accorder le kick, mesurer kick et sub sur des exports séparés.
- Écouter chaque recette avec le break et la couche médium, en mono et à faible volume, et en garder deux ou trois. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
