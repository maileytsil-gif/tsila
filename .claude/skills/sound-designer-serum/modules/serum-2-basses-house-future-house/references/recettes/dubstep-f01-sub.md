# Vingt recettes de sub pour le Dubstep (famille F01)

Septième et dernier lot Dubstep : le sub sous les riddims, yois, tearouts, growls, wobbles et screechs des fichiers `dubstep-*.md`. La plupart des patchs viennent de `house-f01-sub.md` ; ce fichier les règle pour le dubstep à 140 BPM en half-time :
- notes longues et espacées ;
- kick sur le temps 1, caisse claire sur le temps 3 ;
- glissés et plongées de fin de phrase ;
- phase à aligner avec une basse médium jouée grave (OCT −3 des tutoriels).

Rédigé le 05/10/2026. Sources :
- `../etudes-pages-house.md` et `../etudes-captures.md` : F01-13 EDMProd sub, F01-02 Monosounds 808 ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` : F01-08 EDMProd dubstep UK ;
- `../../../../references/basses.md` § 1 et `../documentation-basses.md` § 5-6 ;
- la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles

1. **Règles communes du lot Dubstep** : celles de `dubstep-f10-riddim.md`. **Règles du sub** : celles de `house-f01-sub.md` :
   - un oscillateur, sans unison ni désaccord, mono ;
   - PHASE 0 % ;
   - sub sur sa propre piste ;
   - contrôle en mono et à faible volume.
2. **« Beaucoup de sub en dubstep »** : le kick ne doit pas être trop « boomy » [SOURCE F01-08]. Le sub porte le grave, le kick l'attaque (`../../../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`).
3. **Tonalités** :
   - la zone F0-A0 (MIDI 29-33, 43,7-55 Hz) est celle où l'on « sent et entend » [SOURCE F01-13, écran] ;
   - EDMProd écrit son dubstep UK en mi mineur [SOURCE F01-08] : E0 = 41,2 Hz ;
   - choisir la tonique et l'octave du sub avec `../../../../../compositeur-arrangeur/modules/theorie-musicale-electronique/scripts/theorie.py sub <tonique>` (table kick/sub).
4. **Notes espacées** : en half-time, les notes sont longues et séparées. Release de 50 à 100 ms pour des notes espacées, de 20 à 30 ms pour des notes rapprochées (`basses.md` § Sub).
5. **Quatre macros communes**, celles de `house-f01-sub.md` : `Length`, `Glide`, `Weight`, `Knock`.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| SB01 | Sinus Direct en half-time | référence | notes longues, release 100 ms |
| SB02 | Sub ducké sur la grille half-time | drop | creux sur le temps 1 |
| SB03 | Sub sous un growl grave | growl à OCT −3 | phase alignée |
| SB04 | 808 dubstep | trap-dubstep, hybrid | knock, decay long, glide |
| SB05 | Glissé d'octave | drop | PORTA SCALED 150-250 ms |
| SB06 | Plongée de fin de phrase | fin de phrase | CRS −12 sur une noire |
| SB07 | Triangle filtré | sous un riddim | MG Low 24 à 120 Hz |
| SB08 | Octave fantôme | téléphones | 2e harmonique dosée |
| SB09 | Sinus saturé parallèle | sub lourd | Soft Sat. à faible mix |
| SB10 | Main Sub nettoyée | dubstep UK | carré passe-bas, sans FM ni effet |
| SB11 | Sub qui suit le riddim | riddim | même contour d'amplitude |
| SB12 | Silence et retour | avant le drop | coupure d'un temps, clic à l'entrée |
| SB13 | Sub court | rafales | ENV 1 en BPM, 1/16 |
| SB14 | Attaque ronde | kick long | attaque 10-15 ms |
| SB15 | Sinus FM 1:1 | sub chaud | 2e harmonique |
| SB16 | Sub 2-step | UK, 2-step | le sub évite le kick |
| SB17 | Sub accordé au kick | toutes | tonique et octave choisies par calcul |
| SB18 | Fondamentales sous un wobble | wobble | notes de base seulement |
| SB19 | Phase continue | riddim rapide | Contiguous |
| SB20 | Phase alignée avec la médium | médium grave | PHASE 0 ou 180° |

## Les vingt recettes

### SB01 Sinus Direct en half-time — référence
- **Patch** : S01 de `house-f01-sub.md` : SUB en Sine, PHASE 0 %, `Direct`, MONO.
- **ENV 1** : attaque 3 ms, sustain 0 dB, release 100 ms (notes espacées).
- **Macros** : `Length` release 50 → 200 ms · `Glide` 0 → 150 ms · `Weight` — · `Knock` —.
- **Jeu** : bloc « Dubstep 140 — sub half-time » ci-dessous.
- **Test** : chaque note au même niveau ; écouter la fin de queue avant la note suivante.
- **Origine** : S01 [`house-f01-sub.md`] ; release pour notes espacées (`basses.md` § Sub).

### SB02 Sub ducké sur la grille half-time
- **Patch** : S10 de `house-f01-sub.md`, avec LFO 1 en FREE, HOST, MONO, RATE 1/2 (857,1 ms).
  - Forme : 1 au début du cycle, retour à 0 en 10-15 % du cycle (86-129 ms).
  - Le creux tombe sur le temps 1 (kick) et sur le temps 3. Le creux du temps 3 aide si la caisse claire a du grave ; sinon, forme à un seul creux sur 1 mesure.
- **ENV 1** : attaque 3 ms, release 100 ms.
- **Macros** : `Weight` profondeur du creux, de 0 à −100 · les autres comme SB01.
- **Test** : relancer la lecture à plusieurs endroits ; le creux doit toujours tomber sur le kick. Comparer à un sidechain par plug-in tiers.
- **Origine** :
  - S10 [`house-f01-sub.md`] ;
  - release de sidechain de 50 à 150 ms [SOURCE F01-13] ;
  - durées [CALCUL].

### SB03 Sub sous un growl grave — phase alignée
- **Patch** : SB01.
  - Quand la basse médium garde sa fondamentale (OCT −3 des tutoriels, sans passe-haut), aligner la PHASE du SUB sur celle de la médium, sur la même note.
  - Si les deux s'opposent, essayer PHASE 50 % (180°).
- **ENV 1** : comme SB01.
- **Test** : exports séparés du sub et de la médium, puis `kick_bass_check.py` (`../../../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`) ou un analyseur de corrélation. La somme ne doit pas être plus faible que le sub seul.
- **Origine** :
  - « aligner la phase du sub sur la basse qui partage le même fondamental (décalage de 180°, corrigé par la phase de l'oscillateur) » ;
  - capture : « A Phase: 178deg. », pistes Bass et Sub à −6,1 dB en opposition [SOURCE F01-13, page et écran].

### SB04 808 dubstep — knock, decay long, glide
- **Patch** : S08 de `house-f01-sub.md` : sinus, ENV 2 → CRS +24 en 60 ms, Overdrive 25 % / 60 %, passe-bas vers 400 Hz, MONO + LEGATO.
- **ENV 1** : attaque 0, decay 1-2 s, sustain 0, release 200 ms. Plus long qu'en House, la trap tenant ≈ 3 s.
- **Glide** : PORTA 100-250 ms, selon que l'on vise une glissade de trap (60-100 ms) ou de drill (200-300 ms).
- **Macros** : celles de S08.
- **Test** : le knock ne doit pas doubler l'attaque du kick.
- **Origine** :
  - [SOURCE F01-02, page et infographie] : +24 st / 60 ms, Overdrive 25 % / 60 %, LP 400 Hz après distorsion, decay trap ≈ 3 s, drill ≈ 1 s ;
  - durée pour le dubstep [ORIGINAL].

### SB05 Glissé d'octave — PORTA SCALED
- **Patch** : SB01, avec VOICING MONO + LEGATO, PORTA 150-250 ms, ALWAYS et SCALED allumés (une octave = la valeur du bouton), CURVE convexe.
- **ENV 1** : attaque 3 ms, release 120 ms.
- **Macros** : `Glide` 0 → 300 ms · les autres comme SB01.
- **Test** : à 140 BPM, une croche dure 214 ms. Un glissé de 250 ms dépasse la croche : réserver les glissés longs aux notes d'une noire ou plus.
- **Origine** : PORTA, SCALED, CURVE [cartographie, § 9] ; durées [CALCUL].

### SB06 Plongée de fin de phrase — CRS −12 sur une noire
- **Patch** : S18 de `house-f01-sub.md` : MACRO 4 → CRS du SUB, de 0 à −12.
  - Dans Live, automatiser la macro de 0 à 100 % sur la dernière noire de la phrase (428,6 ms), puis à 0 sur le temps 1.
- **ENV 1** : attaque 3 ms, release 150 ms.
- **Macros** : `Knock` 0 → −12 st (jusqu'à −24) · les autres comme SB01.
- **Test** : la plongée doit finir avant le kick du drop et ne pas descendre sous 30 Hz (inaudible sur la plupart des systèmes).
- **Origine** : S18 [`house-f01-sub.md`] ; variation avant la frontière de huit mesures (règle des drops d'`AGENTS.md`).

### SB07 Triangle filtré — sous un riddim
- **Patch** : S03 de `house-f01-sub.md` : SUB en Triangle → FILTER 1 en MG Low 24 à 120-150 Hz, key track, sortie `Direct`.
- **ENV 1** : attaque 3 ms, release 80 ms.
- **Macros** : celles de S03.
- **Origine** : triangle pour le layering (`basses.md`, SOS) ; S03.

### SB08 Octave fantôme — pour les téléphones
- **Patch** : S05 de `house-f01-sub.md` : SUB en sinus `Direct`, plus OSC A en sinus une octave au-dessus, niveau réglé à l'analyseur (pic à 2f entre −20 et −12 dB sous la fondamentale).
- **ENV 1** : comme SB01.
- **Macros** : celles de S05.
- **Test** : sur téléphone, la ligne de sub doit rester lisible.
- **Origine** : S05 [`house-f01-sub.md`].

### SB09 Sinus saturé parallèle — sub lourd
- **Patch** : S06 de `house-f01-sub.md` : Distortion Soft Sat., DRIVE 20-40, MIX 25-40 %, LEVEL compensé.
- **Test** : la fondamentale ne doit pas baisser quand `Weight` monte.
- **Origine** : « la fondamentale faiblit avec la distorsion » [SOURCE F01-13] ; S06.

### SB10 Main Sub nettoyée — carré passe-bas, sans effet
- **Patch** :
  - OSC A sur BSOD_Square (ou la frame carrée de Basic Shapes), OCT 0, Unison 1, RAND 0, PHASE 0 %.
  - FILTER 1 en MG Low 24, CUTOFF 100-140 Hz, RES 15 %, key track allumé.
  - **Pas** de FM, de distorsion, de peigne ni d'Hyper : tout cela va dans la couche médium (WD03 de `dubstep-f07-wobble.md`).
- **ENV 1** : 0,5 ms / 0 / 1,00 s / 0 dB / 20 ms. MONO + LEGATO.
- **Macros** : `Length` release 20 → 120 ms · `Glide` · `Weight` CUTOFF 80 → 200 Hz · `Knock` —.
- **Origine** :
  - Main Sub de F01-08 (BSOD_Square, MG Low 24, ENV 1 0,5 ms / 20 ms, Mono + Legato) [SOURCE F01-08, écran], **sans** FM, Sine Shaper ni Cmb HL6+ ;
  - carré dans un MG Low 24 [SOURCE F01-13].

### SB11 Sub qui suit le riddim — même contour d'amplitude
- **Patch** :
  - SB01, plus LFO 1 avec la même forme, le même mode et la même vitesse que LFO 1 → LEVEL du riddim (bosse arrondie, RETRIG, 1/4 dans RD01).
  - Destination : LEVEL du SUB seulement. Pas de WT POS, pas de filtre : la hauteur et le timbre restent stables.
- **ENV 1** : attaque 2 ms, release 40 ms.
- **Macros** : `Weight` profondeur de LFO 1 → LEVEL, de 0 à 60 % · les autres comme SB01.
- **Test** : le sub doit respirer avec le riddim sans paraître trémoler. Au-delà de 60 %, il pompe.
- **Origine** : LFO 1 sur le niveau du riddim [SOURCE F10-01] ; reprise sur le sub [ORIGINAL]. La règle de stabilité porte sur la hauteur et le désaccord, pas sur l'enveloppe d'amplitude.

### SB12 Silence et retour — avant le drop
- **Arrangement** :
  - Couper le sub sur le dernier temps (ou la dernière demi-mesure) avant le drop.
  - Le faire revenir sur le temps 1 avec la couche de clic de S16 (OSC B en Sample, transitoire de moins de 100 ms, 12-15 dB sous le sinus).
- **Patch** : S16 de `house-f01-sub.md`.
- **Test** : le retour du sub doit coïncider avec le kick du drop, sans le doubler.
- **Origine** :
  - « basse coupée 2 temps à la fin de la phrase de 16 » ; batterie et basse coupées sur les 2 dernières mesures d'un drop [SOURCE F15-06] ;
  - clic de sample [SOURCE F01-02] ;
  - règle des drops d'`AGENTS.md`.

### SB13 Sub court — sous les rafales
- **Patch** : S11 de `house-f01-sub.md`, ENV 1 en BPM : decay 1/16 (107,1 ms à 140 BPM), sustain 0, release 1/64.
- **Jeu** : une note de sub par groupe de rafales, sur le premier coup seulement.
- **Origine** : S11 ; durée [CALCUL].

### SB14 Attaque ronde — sous un kick long
- **Patch** : S13 de `house-f01-sub.md` : attaque 10-15 ms, courbe concave, release 120 ms.
- **Test** : l'attaque du kick doit rester nette, sans creux de niveau entre kick et sub ; mesurer avec `kick_bass_check.py`.
- **Origine** : S13 ; une période dure 24,3 ms à E0 (41,2 Hz) [CALCUL].

### SB15 Sinus FM 1:1 — sub chaud
- **Patch** : S20 de `house-f01-sub.md` : FM (Sub) 5-15 % sur un sinus, SUB à l'unisson en `None`, coupe-bas à 15-20 Hz contre la composante continue.
- **Origine** : rapport 1:1 [CALCUL, Synth Secrets 12-13] ; S20.

### SB16 Sub 2-step — le sub évite le kick
- **Patch** : SB01 ou SB13.
- **Jeu** :
  - bloc « Dubstep 140 — sub 2-step » ci-dessous : kick sur le temps 1 et le « & » du temps 3 (2-step), caisse claire sur le temps 3 ;
  - le sub entre juste après chaque kick ;
  - recaler sur le vrai pattern de batterie.
- **Origine** : « kick en two-step, clap sur chaque 3e temps » [SOURCE F01-08] ; écriture [ORIGINAL].

### SB17 Sub accordé au kick — tonique et octave par le calcul
- **Méthode** :
  1. Lancer `python3 ../../../../../compositeur-arrangeur/modules/theorie-musicale-electronique/scripts/theorie.py sub <tonique>` depuis le dossier de ce fichier (par exemple `sub E` ou `sub F`) pour la table kick/sub de la tonique.
  2. Choisir l'octave du sub pour que la tonique tombe dans F0-A0 si possible, sans descendre sous E0.
  3. Accorder le kick (`../../../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`).
- **Patch** : SB01.
- **Test** : la tonique du sub et la fondamentale du kick ne doivent pas battre l'une contre l'autre ; mesurer sur des exports séparés.
- **Origine** :
  - zone F0-A0 [SOURCE F01-13, écran] ;
  - outils du dépôt (`theorie.py`, `kick_bass_check.py`) ;
  - procédure [ORIGINAL].

### SB18 Fondamentales sous un wobble — notes de base seulement
- **Patch** : SB01.
- **Jeu** :
  - le sub ne joue que les notes de base de la ligne du wobble, en tenues longues, sans les ornements ni les sauts d'octave de la couche médium ;
  - si le wobble glisse, le sub ne glisse pas.
- **Test** : couper le wobble ; la ligne de sub seule doit tenir l'harmonie.
- **Origine** :
  - « le sub reste une couche séparée, intacte » [SOURCE F08-04] ;
  - sub sinus séparé une octave plus bas, wobble au-dessus de 100 Hz [SOURCE F07-01].

### SB19 Phase continue — sous un riddim rapide
- **Patch** : S02 de `house-f01-sub.md` : PHASE du SUB en Contiguous, attaque 1-2 ms, release 30 ms.
- **Test** : A/B avec SB01 sur une ligne en croches liées.
- **Origine** : Contiguous [cartographie, § 3.7] ; S02.

### SB20 Phase alignée avec la médium — PHASE 0 ou 180°
- **Méthode** : quand une couche médium (riddim, growl) joue à OCT −3 et garde une part de fondamentale :
  1. Mettre RAND 0 et PHASE 0 % sur la médium comme sur le sub.
  2. Exporter les deux pistes sur la même note.
  3. Mesurer leur corrélation dans 30-120 Hz.
  4. Si elle est négative, passer la PHASE du SUB à 50 % (180°), ou inverser la polarité d'une piste avec l'Utility de Live (toléré, `../tempo-mix.md`).
- **Test** : la somme mono doit être plus forte que chaque piste seule dans le grave.
- **Origine** : phase alignée, exemple à 180° [SOURCE F01-13] ; mesure : `../../../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`.

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f01-sub.md`.

```grille
titre: Dubstep 140 — sub half-time (SB01, SB02)
tempo: 140
accords: Em7 | Cmaj7
sub: E0[1:7] G0[3e:3] E0[4:3] | C1[1:7] B0[3e:3] E0[4:3]
```

Notes longues, un temps de silence en fin de chaque tenue, rien sur la caisse claire. E0 = 41,2 Hz, C1 = 65,4 Hz.

```grille
titre: Dubstep 140 — sub 2-step (SB16)
tempo: 140
accords: Fm7 | Fm7
sub: F0[1e:5] F0[2&:2] Ab0[3a:3] F0[4a:1] | F0[1e:5] Eb0[2&:2] C1[3a:3] F0[4a:1]
```

Kick supposé sur les doubles croches 1 et 11 (2-step), caisse claire sur 9. Le sub attaque juste après chaque kick (2 et 12).

```grille
titre: Dubstep 140 — plongée de fin de phrase (SB06, SB12)
tempo: 140
accords: Gm7 | Gm7
sub: G0[1:7] Bb0[3e:3] G0[4:3] | G0[1:7] D1[3e:3] G0[4:4]
```

Mesures 7-8 d'une phrase. La dernière note (G0, temps 4 de la mesure 8) porte la plongée de SB06, macro réglée à −5 demi-tons : vers ré 0 (36,7 Hz), pour rester au-dessus de 30 Hz. Puis silence et retour du sub sur le drop (SB12).

## Ce qui reste à faire par l'utilisateur

- Vérifier dans Serum 2 : PHASE et Contiguous du SUB, la modulation de CRS par une macro, la table BSOD_Square.
- Choisir la tonique avec `theorie.py sub`, accorder le kick, mesurer kick et sub sur des exports séparés.
- Écouter chaque recette avec le kick, la caisse claire et la couche médium, en mono et à faible volume, et en garder deux ou trois. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
