# Vingt recettes de kick Serum 2 pour la DnB et le dubstep

Cinquième lot de kicks : la DnB à 174 BPM et le dubstep à 140 BPM en half-time, pour aller sous les basses des lots `dnb-*` et `dubstep-*` du skill de basses. Le corpus des 46 tutoriels n'a **aucun** kick de ces styles conçu dans Serum. Ce fichier s'appuie donc sur d'autres documents du dépôt, cités un par un, et sur les recettes déjà écrites. La part de [DÉDUCTION] et d'[ORIGINAL] y est plus grande que dans les autres fichiers. Rédigé le 05/10/2026. Sources :
- `../../../../../producteur-live/modules/electronic-production-engineer/references/37-drum-transient-design.md` (conception du kick ; étiquettes d'origine DOC-2, CALC, HEUR), `36-dnb-engine.md` et `30-low-end-engine.md` du même dossier ;
- `../patterns.md` (grilles DnB) et `../sons.md` (choix des sons) ;
- l'étude dubstep de JefroB, `../../../../../../../corpus/cuivres/jefrob-dubstep-bass-sound-design.md` (fiche communautaire, « à recouper avant usage ») ;
- `../../../../../../../corpus/house-future-rave/amen-sessions-06-dubstep-and-bass-music.md` (grille et notes dubstep) ;
- la page EDMProd F01-08 lue pour le skill de basses (`../../../../../sound-designer-serum/modules/serum-2-basses-house-future-house/references/etudes-pages-dubstep-dnb.md`) ;
- le corpus de kicks (`../kicks-serum-tutoriels.md`) pour les rares fiches utiles ici (BH-01, AF-03, et la vidéo ARTFX écartée du style DM).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `kicks-signature-sous-124.md`.

## Règles

1. **Règles communes du lot de kicks** : celles de `kicks-signature-sous-124.md`. **Règles communes des lots de basses** : celles de `dnb-f13-neuro.md` (DnB) et `dubstep-f10-riddim.md` (dubstep), dans `../../../../../sound-designer-serum/modules/serum-2-basses-house-future-house/references/recettes/`.
2. **En DnB, le sub tient le fondamental** : sub sinus mono à la tonique, kick court (moins de 200 ms), corps entre 60 et 100 Hz, coupe-bas du kick à 25-30 Hz, ou à 40-50 Hz si plus de 20 % de l'énergie du kick est sous 60 Hz [SOURCE `30-low-end-engine.md`]. « Sample court et pointu (couche transitoire + corps), HP 40 Hz, laisse le sub seul sous 60 Hz » (`../sons.md`).
3. **En dubstep, « beaucoup de sub »** : le kick ne doit pas être trop « boomy » [SOURCE F01-08]. Le kick dubstep « se sent plus qu'il ne s'entend » : rond, attaque minimale, 40-150 Hz, peu de traitement, HPF à 25 Hz ; le kick riddim est court et punchy pour traverser les basses [SOURCE JefroB, fiche communautaire].
4. **Conception de départ** [SOURCE `37-drum-transient-design.md`] :
   - transitoire 2-6 kHz, 5-15 ms ; corps vers 100-150 Hz ; fondamentale utile vers 40-60 Hz ;
   - sinus de 45-50 Hz, chute de hauteur de +24 à +36 demi-tons en 20-40 ms, amplitude A 0, D 250-500 ms ;
   - dans Serum 2 : OSC A sinus, ENV 2 → CRS ; NOISE en one-shot (≈ 5 ms) dans un passe-haut vers 2 kHz pour le clic ; RAND 0 %.
   - Pour la DnB, raccourcir la décroissance sous 200 ms (règle 2).
5. **Grilles** :
   - DnB 2-step : kick sur les doubles croches 1 et 11, variante 1 et 8 ; caisse claire sur 5 et 13 (`../patterns.md`, `36-dnb-engine.md`).
   - Dubstep half-time : kick sur 1, caisse claire sur 3 (double croche 9) ; variante de kick sur 1, 7 et 15 [SOURCE `amen-sessions-06`] ; kick en two-step et clap sur le 3e temps [SOURCE F01-08].
6. **Durées** [CALCUL] :

   | Tempo | Noire | Croche | Double croche |
   | --- | --- | --- | --- |
   | 140 BPM | 428,6 ms | 214,3 ms | 107,1 ms |
   | 174 BPM | 344,8 ms | 172,4 ms | 86,2 ms |

7. **Breaks** : un break samplé (Amen, Think) découpé, filtré en passe-haut à 200 Hz, au niveau des ghosts, pour que le kick et le sub programmés tiennent le grave [SOURCE `36-dnb-engine.md`, `../patterns.md`].

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| KD01 | Kick DnB de référence | DnB | court, corps au-dessus du sub, clic à 2 kHz |
| KD02 | Kick d'une double croche en E0 | DnB | 86 ms, couches de bruit stéréo |
| KD03 | Kick DnB en deux couches | DnB | corps et transitoire, alignés en phase |
| KD04 | Kick acoustique DnB | DnB, liquid, jungle | couche « DX » de Serum 2 |
| KD05 | Kick sous un break | DnB, jungle | kick et sub tiennent le grave sous le break filtré |
| KD06 | Kick liquid | liquid | rond, attaque douce |
| KD07 | Kick neuro ou jump-up | neuro, jump-up | transitoire distordu |
| KD08 | Kick minimal DnB | minimal, deep DnB | un seul son, très défini |
| KD09 | Kick à hauteur fixe | DnB, dubstep | suivi coupé, OCT +2 et SEM +7 |
| KD10 | Kick qui laisse rouler la caisse claire | DnB | pas de second kick dans la mesure du fill |
| KD11 | Kick dubstep de référence | dubstep | rond, attaque minimale, HPF 25 Hz |
| KD12 | Kick riddim | riddim | sous-couche sinus, clic, corps, saturation parallèle |
| KD13 | Kick EDM-dubstep punchy | brostep, tearout | KH02 recalé à 140 BPM |
| KD14 | Kick dubstep en 2-step | dubstep UK | kick sur 1, 7 et 15 |
| KD15 | Kick dubstep accordé au-dessus du sub | dubstep | tonique ou quinte, une octave au-dessus |
| KD16 | Kick deep dubstep | deep dubstep | plus long, sous la noire |
| KD17 | Kick à clic de hi-hat | riddim, tearout | sample de hi-hat en transitoire |
| KD18 | Kick du build dubstep | build | sans aigus, noires puis croches puis doubles croches |
| KD19 | Kick qui se tait avant le drop | dubstep, DnB | un temps de silence |
| KD20 | Kick imprimé et accordé | toutes | impression, Simpler, une note par tonalité |

## Les vingt recettes

### KD01 Kick DnB de référence — court, au-dessus du sub
- **OSC A** : sinus (ou Analog_BD_Sin), RAND 0, PHASE 0.
- **Fondamentale** : C1 (65,4 Hz) ou F1 (87,3 Hz) au-dessus d'un sub en F0 [CALCUL, `theorie.py sub F`].
- **Hauteur** : ENV 2 → CRS, unipolaire, +24 demi-tons, decay 30 ms, sustain 0.
- **Amplitude** : ENV 1 : attaque 0, hold 30 ms, decay 120 ms, sustain −∞ : 150 ms au total, sous les 200 ms de la règle 2 [CALCUL].
- **Clic** : NOISE en one-shot (≈ 5 ms) dans FILTER 2 en passe-haut vers 2 kHz.
- **EQ** (Serum) : coupe-bas à 40 Hz.
- **Macros** : `Pitch Decay` decay d'ENV 2 (15 → 60 ms) · `Cutoff Decay` — · `Click` niveau du NOISE · `Release` decay d'ENV 1 (60 → 200 ms).
- **Sub associé** : DS01 de `dnb-f01-sub.md`.
- **Jeu** : bloc « DnB 174 — kick en 2-step et sub » ci-dessous.
- **Origine** : conception de départ [SOURCE `37-drum-transient-design.md`] ; longueur, corps et coupe-bas [SOURCE `30-low-end-engine.md`, `../sons.md`] ; valeurs [ORIGINAL].

### KD02 Kick d'une double croche en E0 — avec des couches de bruit stéréo
- **Patch** : KD01, avec :
  - fondamentale E0 (41,2 Hz) : le kick descend dans le registre du sub, mais très brièvement ;
  - ENV 1 : decay d'une double croche (86 ms à 174 BPM, 87 ms à 172 BPM) [CALCUL] ;
  - NOISE stéréo en couche (par exemple « HP12 White Noise (Stereo) » de Serum 2), enveloppe courte.
- **Macros** : celles de KD01.
- **Test** : mesurer la corrélation kick-sub ; si le kick et le sub sont tous deux en E, accorder les deux ensemble (`../../../kick-bass-equilibre/GUIDE.md`).
- **Origine** : la vidéo ARTFX « Making kicks from scratch using synthesis - a DEEP DIVE into DNB DRUMS », écartée du style DM du corpus, en donne seulement ces trois faits : DnB à 172 BPM, kick d'une double croche en E0, couches de bruit stéréo [EXTRAIT, `../kicks-serum-tutoriels.md`, « Écartés » du style DM]. Le reste est [ORIGINAL].

### KD03 Kick DnB en deux couches — corps et transitoire
- **Couche corps** : KD01 sans clic.
- **Couche transitoire** : OSC B (ou un second Serum) avec un clic ou un sample d'attaque ; FILTER 2 en passe-haut vers 140-150 Hz sur cette couche seule.
- **Alignement** : polarité d'abord, puis décalage de 0,1 à 1 ms vers une corrélation proche de +1 dans 30-80 Hz ; 5 ms font une demi-période à 100 Hz, donc une annulation complète.
- **Test** : un kick qui devient plus fort quand on coupe une couche a une couche qui annule l'autre.
- **Macros** : `Click` LEVEL de la couche transitoire · les autres comme KD01.
- **Origine** : règles de superposition [SOURCE `37-drum-transient-design.md`] ; « combiner un corps synthétisé et un transitoire seulement quand chaque couche a un rôle clair » [SOURCE `36-dnb-engine.md`].

### KD04 Kick acoustique DnB — la couche « DX »
- **Patch** : KS16 de `kicks-signature-sous-124.md` (OSC A sinus, OSC B transitoire, OSC C sample « DX » de Factory › Non-tonal › Drum › Kicks avec fondu d'entrée, FILTER 2 sur C, NOISE « Pink Noise Stereo »), avec :
  - transitoire d'OSC B gardé présent ;
  - longueur totale sous 200 ms.
- **Macros** : celles de KS16.
- **Usage** : liquid, jungle, DnB à couleur acoustique.
- **Origine** : [SOURCE AF-03, DNB Academy, Serum 2] : kick « acousticy, funk », fait dans une chaîne DnB.

### KD05 Kick sous un break — le grave au kick et au sub
- **Patch** : KD01 ou KD03.
- **Jeu** :
  - le break samplé (Amen, Think) est découpé, filtré en passe-haut à 200 Hz et joué au niveau des ghosts ;
  - le kick programmé tombe sur les kicks du break ; il porte le grave avec le sub.
- **Droits** : un break célèbre n'a pas de droits pour une sortie ; prendre un break enregistré par l'utilisateur ou sous licence vérifiée.
- **Macros** : celles de la recette de départ.
- **Origine** : [SOURCE `36-dnb-engine.md`, `../patterns.md`] ; règle « Référence » d'`AGENTS.md` pour les droits.

### KD06 Kick liquid — rond, attaque douce
- **Patch** : KS01 de `kicks-signature-sous-124.md` (Analog_BD_Sin, chute de 12 demi-tons, LP qui finit bas, clic bas), avec :
  - ENV 1 : hold 40 ms, decay 130 ms (170 ms, sous les 200 ms) ;
  - ENV 2 : decay 50 ms.
- **Macros** : celles de KS01.
- **Usage** : liquid, quand l'harmonie ou la voix portent le morceau et que la batterie se retient [SOURCE `36-dnb-engine.md`, « Liquid DnB DNA »].
- **Origine** : KS01 recalé à 174 BPM [ORIGINAL].

### KD07 Kick neuro ou jump-up — transitoire distordu
- **Patch** : KH18 de `kicks-house-bass-house.md` (ENV 3 courte → DRIVE, pré-filtre passe-haut au-dessus de la fondamentale), avec ENV 1 : hold 30 ms, decay 100 ms.
- **Macros** : celles de KH18.
- **Test** : sous un neuro ou un jump-up chargés, le kick doit garder son attaque ; sinon monter le clic plutôt que la longueur.
- **Origine** : KH18 [SOURCE BH-01, HC-02, HC-06, HC-12] ; recalage à 174 BPM [ORIGINAL].

### KD08 Kick minimal DnB — un seul son, très défini
- **Patch** : KD01 avec un seul oscillateur, sans couche ni NOISE ; le clic vient de la PHASE (90°) et d'une chute de hauteur plus courte (20 ms).
- **Macros** : `Click` PHASE (0 → 90°) · les autres comme KD01.
- **Usage** : minimal et deep DnB, où le choix du kick, de la caisse claire et du rim compte plus, parce que moins de couches les cachent [SOURCE `36-dnb-engine.md`].
- **Origine** : phase au pic pour un petit clic [SOURCE AF-01, DM-05] ; recette [ORIGINAL].

### KD09 Kick à hauteur fixe — suivi coupé, OCT +2 et SEM +7
- **Patch** : KD01 ou KD11, suivi de hauteur de l'oscillateur coupé : l'oscillateur Wavetable se place alors sur MIDI 0 (≈ 8,2 Hz) ; OCT +2 et SEM +7 donnent MIDI 31, ≈ 49 Hz (G0 dans la numérotation de Live).
- **Usage** : jouer le kick depuis n'importe quelle note (pad de Drum Rack, break découpé) sans changer sa hauteur.
- **Test** : vérifier à l'accordeur que la fin de la note lit G0 ; pour une autre tonalité, changer SEM.
- **Origine** : [SOURCE `37-drum-transient-design.md`, d'après le manuel de Serum 2 p. 35] ; hauteur fixe aussi chez W. A. Production [SOURCE HC-04].

### KD10 Kick qui laisse rouler la caisse claire — fill toutes les 8 mesures
- **Patch** : KD01.
- **Jeu** : dans la mesure 8, pas de kick sur la double croche 11 ; la caisse claire roule sur 14, 15 et 16 en montant ; le sub s'arrête avec le kick.
- **Macros** : celles de KD01.
- **Origine** : fill toutes les 8 mesures, caisse claire sur 14, 15 et 16 [SOURCE `36-dnb-engine.md`, `../patterns.md`] ; retrait du kick [ORIGINAL], règle « Drops » d'`AGENTS.md`.

### KD11 Kick dubstep de référence — rond, attaque minimale
- **OSC A** : sinus, RAND 0, PHASE 0.
- **Hauteur** : ENV 2 → CRS, chute modérée, +12 demi-tons, decay 50 ms.
- **Amplitude** : ENV 1 : attaque 1 ms, hold 60 ms, decay 200 ms, sustain −∞ (260 ms, sous la croche pointée à 140 BPM, 321 ms) [CALCUL].
- **Corps** : une légère couche de corps (OSC B en sinus une octave au-dessus, niveau bas, même enveloppe).
- **FX** : saturation douce ou rien ; EQ en coupe-bas à 25 Hz.
- **Accord** : voir KD15.
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` — · `Click` LEVEL d'OSC B · `Release` decay d'ENV 1.
- **Sub associé** : SB01 de `dubstep-f01-sub.md`.
- **Jeu** : bloc « Dubstep 140 — kick en 2-step et sub » ci-dessous.
- **Origine** : « Dubstep Kick : deep, round, minimal attack ; sine with moderate pitch envelope + light body layer ; 40-150 Hz ; gentle saturation, HPF at 25 Hz » [SOURCE JefroB, fiche communautaire] ; « pas trop boomy » [SOURCE F01-08] ; valeurs [ORIGINAL].

### KD12 Kick riddim — sous-couche sinus, clic, corps
- **OSC A** : sinus avec enveloppe de hauteur, pour la sous-couche (50-60 Hz).
- **OSC B** ou **OSC C** : sample de corps (100-200 Hz) ; **NOISE** ou sample de clic (3-6 kHz).
- **Amplitude** : decay court, ENV 1 : hold 20 ms, decay 90 ms.
- **FX** : transitoire au maximum (plug-in tiers de transient shaping) ; distorsion en parallèle (Splitter, ou MIX de la Distortion à 30-50 %).
- **Rôle** : il doit traverser les stabs de basse sans leur disputer le grave.
- **Macros** : `Pitch Decay` decay de l'enveloppe de hauteur · `Cutoff Decay` — · `Click` niveau du clic · `Release` decay d'ENV 1.
- **Origine** : « Riddim Kick : short, punchy, clicks through dense bass ; layered sine sub (pitch envelope) + click sample + body sample ; sub 50-60 Hz, click 3-6 kHz, body 100-200 Hz ; transient shaping, short decay, parallel distortion » [SOURCE JefroB, fiche communautaire] ; valeurs d'enveloppe [ORIGINAL].

### KD13 Kick EDM-dubstep punchy — KH02 à 140 BPM
- **Patch** : KH02 de `kicks-house-bass-house.md` (LFO 4 multipoint, Coarse ≈ 25, clic n° 2, Monster 4 en FM, ENV 2 → DRIVE, coupe à 500 Hz).
- **Tempo** : à 140 BPM, la croche dure 214 ms ; garder hold + decay sous cette valeur [CALCUL].
- **Macros** : celles de KH02.
- **Usage** : brostep, tearout, dubstep chargé.
- **Origine** : [SOURCE BH-01, W. A. Production, « Punchy EDM / Dubstep KICK », Serum 1].

### KD14 Kick dubstep en 2-step — kick sur 1, 7 et 15
- **Patch** : KD11 ou KD12.
- **Jeu** : kick sur les doubles croches 1, 7 et 15 de la mesure, caisse claire sur 9 ; le sub attaque juste après le kick.
- **Macros** : celles de la recette de départ.
- **Jeu** : bloc « Dubstep 140 — kick en 2-step et sub » ci-dessous.
- **Origine** : variante de grille [SOURCE `amen-sessions-06`] ; « kick en two-step » [SOURCE F01-08].

### KD15 Kick dubstep accordé au-dessus du sub — tonique ou quinte
- **Patch** : KD11.
- **Accord** : sub en E0 (41,2 Hz, mi mineur d'EDMProd) → kick en B0 (61,7 Hz, la quinte) ou E1 (82,4 Hz) ; sub en F0 → kick en C1 (65,4 Hz) ou F1 (87,3 Hz) [CALCUL, `theorie.py sub`].
- **Test** : à l'accordeur, la fin de la note du kick ; puis `kick_bass_check.py` sur des exports séparés.
- **Macros** : celles de KD11.
- **Origine** : `../../../kick-bass-equilibre/GUIDE.md` § 2 ; tonalité de mi mineur [SOURCE F01-08].

### KD16 Kick deep dubstep — plus long, sous la noire
- **Patch** : KD11 avec ENV 1 : hold 80 ms, decay 280 ms (360 ms, sous la noire de 429 ms) [CALCUL] ; chute de hauteur de 7 demi-tons en 60 ms.
- **Usage** : deep dubstep à 138-140 BPM, kick « felt more than heard ».
- **Test** : le kick ne doit pas recouvrir l'attaque du sub suivant ; sinon le raccourcir.
- **Macros** : celles de KD11.
- **Origine** : deep dubstep à 138-140 BPM, sous-genre « sparse, dubby, sub-focused » [SOURCE `amen-sessions-06`, JefroB] ; valeurs [ORIGINAL].

### KD17 Kick à clic de hi-hat — pour traverser les basses
- **Patch** : KD12, avec le clic remplacé par un sample de hi-hat très court chargé dans un oscillateur en mode Sample, enveloppe de niveau courte ; FM depuis le NOISE en option.
- **Macros** : `Click` LEVEL de l'oscillateur de hi-hat · les autres comme KD12.
- **Usage** : riddim, tearout, quand les basses masquent le clic.
- **Origine** : sample de hi-hat comme transitoire [SOURCE BH-07, TURNCLOAK, Serum 2] ; usage en dubstep [DÉDUCTION].

### KD18 Kick du build dubstep — sans aigus, puis de plus en plus serré
- **Patch** : KD11, avec FILTER 1 en passe-bas fermé (CUTOFF ≈ 200 Hz) sur une macro `Cutoff Decay`.
- **Jeu** : kick sur chaque temps pendant 4 mesures, en croches pendant 2 mesures, en doubles croches pendant 2 mesures ; volume qui monte ; filtre qui s'ouvre sur la dernière mesure.
- **Jeu** : bloc « Dubstep 140 — kick du build » ci-dessous (les deux premiers paliers).
- **Origine** : « Build : kick sur chaque temps sans aigus, volume qui monte ; doubler après 4 mesures, redoubler après 2 » [SOURCE F01-08] ; filtre [ORIGINAL].

### KD19 Kick qui se tait avant le drop — un temps de silence
- **Patch** : KD11 ou KD01.
- **Jeu** : un temps de silence (batterie et sub coupés) juste avant le drop ; le kick revient sur le temps 1.
- **Usage** : alterner avec le build (KD18) et le fill (KD10) d'une frontière à l'autre.
- **Origine** : « the one-beat silence before the drop is structural, not decorative » [SOURCE `amen-sessions-06`] ; règle « Drops » d'`AGENTS.md`.

### KD20 Kick imprimé et accordé — une note par tonalité
- **Méthode** :
  1. Valider le kick à l'écoute sur la note du morceau.
  2. L'imprimer en audio, une note par tonalité utile (procédure de `../../../../../sound-designer-serum/modules/resampling/GUIDE.md`).
  3. Le rejouer dans un Simpler ou un Drum Rack ; accorder par la transposition du Simpler.
  4. L'inscrire au registre `../signature.md`.
- **Origine** : « resample once the envelope behaves » [SOURCE `37-drum-transient-design.md`] ; impression [SOURCE BH-02, HC-02, HC-05] ; KS19.

## Motifs vérifiés

Numérotation de Live (C3 = 60) ; les notes de kick sont les fondamentales visées. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/kicks/kicks-dnb-dubstep.md`.

```grille
titre: DnB 174 — kick en 2-step et sub (KD01, KD03)
tempo: 174
accords: Fm7 | Fm7
kick: C1[1:2] C1[3&:2] | C1[1:2] C1[3&:2]
sub: F0[1e:7] F0[3a:5] | Ab0[1e:7] Eb0[3a:4] F0[4a:1]
```

Kick sur les doubles croches 1 et 11 (2 doubles croches, 172 ms) ; le sub attaque juste après chaque kick, comme le bloc « DnB 174 — sub 2-step » de `dnb-f01-sub.md`.

```grille
titre: Dubstep 140 — kick en 2-step et sub (KD11, KD14)
tempo: 140
accords: Fm7 | Fm7
kick: C1[1:2] C1[2&:2] C1[4&:2] | C1[1:2] C1[4&:2]
sub: F0[1e:5] Ab0[3e:5] F0[4a:1] | F0[1e:5] Eb0[3e:5] C1[4a:1]
```

Kick sur 1, 7 et 15, puis sur 1 et 15 ; rien sur la caisse claire du temps 3 ; le sub tient les espaces.

```grille
titre: Dubstep 140 — kick du build (KD18)
tempo: 140
accords: Fm | Fm
kick: C1[1:2] C1[2:2] C1[3:2] C1[4:2] | C1[1:1] C1[1&:1] C1[2:1] C1[2&:1] C1[3:1] C1[3&:1] C1[4:1] C1[4&:1]
```

Mesure 1 : le palier en noires (4 mesures) ; mesure 2 : le palier en croches (2 mesures). Le palier en doubles croches suit sur 2 mesures.

## Ce qui reste à faire par l'utilisateur

- Choisir avec l'utilisateur une référence DnB ou dubstep pour le kick : aucun tutoriel du corpus n'en conçoit un dans Serum, et ce fichier repose surtout sur des compilations et des fiches communautaires.
- Vérifier dans Serum 2 : le suivi de hauteur coupé et la hauteur obtenue avec OCT +2 et SEM +7 (KD09), le bruit « HP12 White Noise (Stereo) », le sample « DX ».
- Écouter sous les basses des lots DnB et dubstep, avec le break ou la caisse claire, à niveau égal ; mesurer kick et sub sur des exports séparés ; inscrire le kick validé au registre `../signature.md`.
