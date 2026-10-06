# Vingt recettes de kick Serum 2 sous 124 BPM : la signature, le deep, le minimal et l'électro chill

Premier lot de recettes de kicks : le kick de la signature du projet sous 124 BPM, et les kicks ronds et courts du deep, du minimal, de la microhouse et de l'électro chill. La règle « Signature » d'`AGENTS.md` le demande doux, clair et chaleureux. « Solomun feat. Jamie Foxx – Ocean » n'en est que la référence de kick ; aucune recette ne prétend reproduire ce kick, qui n'a jamais été écouté. Rédigé le 05/10/2026. Sources :
- `../kicks-serum-tutoriels.md` (corpus de 46 tutoriels, fiches DM, AF, HC) et sa synthèse `../kicks-serum-synthese.md` ;
- la recette « Kick Serum 2, esprit 808 soft » de `../../../produire-demo-electro-rapide/references/recettes.md` ;
- `../../../kick-bass-equilibre/SKILL.md` (rôles kick et sub, accord, longueur, mesure) ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes :
- [SOURCE xx-nn] : dit dans une vidéo du corpus ;
- [CALCUL] : valeur calculée ;
- [DÉDUCTION] : déduite d'une source ou de la cartographie ;
- [ORIGINAL] : réglage proposé, à juger à l'oreille.

## Règles communes du lot de kicks

Elles valent pour tous les fichiers de `references/kicks/`.

1. **Architecture.** La même revient dans tout le corpus, du deep au hard techno (`../kicks-serum-synthese.md`, « Architecture commune ») :
   - un sinus ;
   - une chute de hauteur unipolaire qui retombe exactement sur la note ;
   - une enveloppe d'amplitude en sustain −∞ ;
   - un clic au choix ;
   - un passe-bas qui s'ouvre puis retombe ;
   - une distorsion sur le transitoire seulement ;
   - un EQ ;
   - l'accord par la note jouée.

   Les styles diffèrent par les doses.
2. **Voicing** : MONO, pour que deux kicks ne se chevauchent pas ; qualité d'oscillateur au maximum [SOURCE DM-01]. RAND à 0 : chaque coup part du même point [SOURCE DM-04, DM-05, AF-01].
3. **Phase de départ** :
   - PHASE 0 : départ sans clic [SOURCE AF-05] ;
   - 90°, au pic de l'onde : un petit clic [SOURCE AF-01, AF-03, DM-05] ;
   - ≈ 122, « à personnaliser » [SOURCE DM-04].
   - Les captures d'AF-01 (MERAKKI, 1:23) et de HC-06 (PML, 3:40) montrent PHASE 180° et RAND 100 % à cet instant ; le « 90° » d'AF-01 ci-dessus n'y est pas confirmé (`../kicks-serum-synthese.md`, section des captures) : à relire dans la vidéo.
4. **Accord et octave.** La fondamentale entendue est la note jouée, décalée par l'OCT de l'oscillateur. Les tutoriels mettent l'oscillateur à OCT −2 et jouent deux octaves plus haut [SOURCE DM-01, DM-02, DM-04]. Les recettes donnent la **fondamentale visée** : avec OCT −2, jouer la note deux octaves plus haut (C3 pour un kick en C1).
   - **Quand le sub tient le fondamental** (deep, minimal, tech house) : corps du kick **au-dessus** du sub, entre 60 et 100 Hz, accordé sur la tonique ou la quinte, une octave au-dessus du sub (`../../../kick-bass-equilibre/SKILL.md` § 1-2).
   - En fa mineur, avec un sub en F0 (43,7 Hz) : kick en C1 (65,4 Hz, la quinte) ou en F1 (87,3 Hz, la tonique) [CALCUL, `theorie.py sub F`].
   - **Quand le kick tient le grave** (électro 808) : kick accordé sur la tonique dans le registre du sub, par exemple F0 (43,7 Hz) ou G0 (49,0 Hz). DM-02 observe une fondamentale entre 40 et 50 Hz et pose une bosse d'EQ vers 47 Hz [SOURCE DM-02].
5. **Longueur.** Le kick finit avant le kick suivant et avant la note de sub suivante (`../../../kick-bass-equilibre/SKILL.md` § 2). DM-03 le limite à une croche [SOURCE DM-03]. Durées [CALCUL] :

   | Tempo | Noire | Croche | Double croche |
   | --- | --- | --- | --- |
   | 112 BPM | 535,7 ms | 267,9 ms | 133,9 ms |
   | 118 BPM | 508,5 ms | 254,2 ms | 127,1 ms |
   | 120 BPM | 500,0 ms | 250,0 ms | 125,0 ms |
   | 123 BPM | 487,8 ms | 243,9 ms | 122,0 ms |

   Avec un sub sur les contretemps, la note de sub suivante arrive une croche après le kick : hold + decay du kick ≈ une croche.
6. **Chute de hauteur unipolaire** (flèche simple dans la matrice, ou Shift+Alt+clic), pour que la hauteur retombe exactement sur la note [SOURCE DM-01, DM-05]. Une chute de 12 demi-tons part une octave au-dessus de la note : de C2 (130,8 Hz) vers C1 (65,4 Hz) pour un kick en C1 [CALCUL]. Les quantités du corpus (« Coarse 20 », « 48 ») ne sont pas vérifiées : lire l'infobulle de la matrice dans Serum 2.
7. **Quatre macros communes**, celles de Londonpatchwork [SOURCE DM-05] :
   - `Pitch Decay` : decay de l'enveloppe de hauteur ;
   - `Cutoff Decay` : decay de l'enveloppe du filtre ;
   - `Click` : résonance ou niveau du clic ;
   - `Release` : release d'ENV 1, ou decay quand la recette n'a pas de release.

   Vérifier le « + » sur chaque destination.
8. **Après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`). Les traitements des vidéos (OTT, Glue Compressor, Saturator, Drum Buss de Live) ne sont pas repris ; la chaîne actuelle de la signature (`../signature.md` : EQ, puis Saturator) garde son Saturator déjà posé, mais un nouveau kick passe par un saturateur tiers (J37, `../../../effets-plugins/references/fiches.md`).
9. **Contrôle par l'utilisateur**, un réglage à la fois, à niveau égal :
   - le kick seul, puis avec le sub, puis dans le groove (clap, hats) ;
   - mono ;
   - faible volume ;
   - accordeur (GTune, cité par DM-06) ou analyseur sur la fin de la note ;
   - mesure kick et sub sur des exports séparés (`kick_bass_check.py`, `../../../kick-bass-equilibre/SKILL.md` § 3) ;
   - A/B contre le kick actuel de la signature et contre KS01.
10. **Validation** : quand l'utilisateur valide un kick à l'écoute, l'inscrire au registre `../signature.md` (chemin du preset, réglages, accord, morceau, date).

## Règles propres à la signature

- **Doux** : peu de chute de hauteur, pas de distorsion forte, clic bas ou absent.
- **Clair** : un peu d'air vers 8-9 kHz et une attaque lisible [SOURCE DM-02].
- **Chaleureux** : un passe-bas qui « finit bas » et une saturation légère [SOURCE DM-05, DM-04].
- **Diagnostic quand le kick « ne va pas »** : un réglage à la fois, dans cet ordre (`../kicks-serum-synthese.md`).
  1. **Trop dur ou trop « clicky »** : baisser la chute de hauteur, puis le clic et la résonance, avant de toucher le corps [SOURCE DM-02].
  2. **Trop mou ou absent à faible volume** : allonger un peu le hold, ouvrir le filtre au départ, ajouter une saturation Tape légère.
  3. **Boueux** : petit creux étroit dans le bas-médium (une petite coupe seulement, sinon on « tue » le kick) [SOURCE DM-02].
  4. **En conflit avec le sub** : raccourcir le decay, accorder kick et sub ensemble, mesurer leur corrélation.
  5. **Faux** : vérifier la note à l'accordeur ; une chute de hauteur longue fait paraître la note plus haute.

  Le tableau de choix ci-dessous donne pour chaque symptôme la recette à essayer.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| KS01 | Kick signature de référence | sous 124 BPM | Analog_BD_Sin, chute de 12 demi-tons, LP qui finit bas |
| KS02 | Kick deep In The Mix | deep house | hold et decay de 100 ms, LP sur la même enveloppe |
| KS03 | Kick rond Jon Audio | deep, électro chill | clic Attacks › Kick n° 11, bosse à 47 Hz |
| KS04 | Kick étouffé SKETIMUSIC | deep | Master Tune, MG Low 18, longueur d'une croche |
| KS05 | Kick sourd Arc Nade | minimal | phase 122, chute courte, Tape |
| KS06 | Kick minimal Londonpatchwork | minimal, microhouse | Low 24 piloté, quatre macros |
| KS07 | Kick essentiel Octocap | toutes | un sinus, hold 50, decay 100 |
| KS08 | Kick « soft » à deux sinus | deep | deux sinus, arrêt avant la distorsion |
| KS09 | Kick clean adouci MERAKKI | deep, organic | fondu d'attaque, Splitter, réverb modulée |
| KS10 | Kick 808 soft de la démo | électro chill, R&B | chute de 30-60 ms, 280-500 ms |
| KS11 | Kick court sous un sub chargé | sub en contretemps | decay d'une double croche |
| KS12 | Kick long qui tient le grave | électro 808 à 112 BPM | accordé sur la tonique, F0 |
| KS13 | Kick accordé à la quinte | toutes | C1 sous une tonique fa |
| KS14 | Kick à hauteur fixe | lignes de sub mobiles | suivi de note coupé |
| KS15 | Kick à clic de second sinus | kick un peu plus clair | sinus deux octaves au-dessus, bref |
| KS16 | Kick à couche acoustique | chaleur, peau | sample « DX » sans son attaque |
| KS17 | Kick à couche foley | microhouse, organic | percussion dans le NOISE, suivie en hauteur |
| KS18 | Kick tape chaud | chaleur | Tape Sat. légère, air à 8,8 kHz |
| KS19 | Kick imprimé | figer un kick validé | impression, Simpler |
| KS20 | Kick qui se retire avant la frontière | variation avant la frontière | dernier temps sans kick |

## Les vingt recettes

### KS01 Kick signature de référence — doux, clair, chaleureux
- **OSC A** : Analog_BD_Sin (table de Serum 1, à retrouver dans Serum 2 ; à défaut, sinus Default), OCT −2, RAND 0, PHASE 0 %.
- **Fondamentale** : C1 (65,4 Hz) pour un morceau en fa mineur, jouée C3 avec OCT −2 [CALCUL, règle 4].
- **Hauteur** : ENV 2 → CRS d'A, unipolaire, chute d'environ 12 demi-tons ; ENV 2 : attaque 0, decay 60-100 ms, sustain 0, courbe concave.
- **Amplitude** : ENV 1 : attaque 1 ms, hold 60-100 ms, decay 150-200 ms, sustain −∞, release 5 ms. Hold + decay ≈ une croche, 250 ms à 120 BPM [CALCUL].
- **Chaleur** : FILTER 1 en Low 24 (ou MG Low 18), RES basse ; ENV 3 → CUTOFF, unipolaire : départ ouvert, fin basse.
- **Clic** : NOISE en one-shot, Attacks › Kick n° 11, niveau bas ; à couper si le kick paraît dur.
- **FX** : Distortion Tape Sat., DRIVE faible ; EQ : petite bosse à la fondamentale, air léger vers 8-9 kHz, petit creux étroit dans le bas-médium.
- **Macros** : `Pitch Decay` decay d'ENV 2 (40 → 150 ms) · `Cutoff Decay` decay d'ENV 3 (60 → 300 ms) · `Click` niveau du NOISE · `Release` decay d'ENV 1 (100 → 300 ms).
- **Sub** : sinus en F0 sur sa piste, en contretemps ; bloc « Deep 120 — kick accordé et sub en contretemps » ci-dessous.
- **Test** : A/B à niveau égal contre le kick actuel (« DR - Kick Minimal », decay 294 ms, `../signature.md`) ; puis le diagnostic des règles propres à la signature.
- **Origine** : fiche « kick signature sous 124 BPM » de `../kicks-serum-synthese.md`, d'après DM-01, DM-02, DM-04, DM-05 et HC-09 ; accord d'après `../../../kick-bass-equilibre/SKILL.md`.

### KS02 Kick deep In The Mix — hold et decay de 100 ms
- **OSC A** : sinus (Analog › Basic Shapes), OCT −2 ; QUALITY au maximum ; MONO.
- **Amplitude** : ENV 1 : hold ≈ 100 ms, decay ≈ 100 ms, sustain −∞.
- **Hauteur** : ENV 2, sustain 0 (forme en triangle) → CRS d'A, unipolaire ; plus de quantité = plus « pitchy », moins = juste un peu d'attaque.
- **Filtre** : passe-bas, la même ENV 2 sur le CUTOFF ; master baissé et DRIVE du filtre monté pour les harmoniques.
- **Clic** : NOISE passé dans le filtre, one-shot, dossier « attack/kick » ; niveau selon le clic voulu.
- **FX** : aucun dans la vidéo. Hors Serum, la vidéo creuse 300-400 Hz, monte l'aigu et ajoute overdrive, transient shaper et compression : à faire avec des plug-ins tiers.
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` quantité d'ENV 2 → CUTOFF · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Origine** : [SOURCE DM-01, In The Mix, Serum 1] ; « that really classic deep electronic punchy kick », accordé sur la tonique (F#) du morceau.

### KS03 Kick rond Jon Audio — clic n° 11, bosse à 47 Hz
- **OSC A** : Analog_BD_Sin, OCT −2.
- **Clic** : NOISE, Attacks › Kick n° 11, one-shot coché, niveau un peu monté.
- **Amplitude** : ENV 1 : attaque ≈ 1,1 ms, hold 0, decay ≈ 200 et quelques ms, sustain au minimum, release ≈ 4 ms ; courbe un peu remontée.
- **Hauteur** : LFO 1 en mode ENVELOPE, rate 1/16, point de gauche tout en haut, grille 12 → Semitone d'A : chute de 12 demi-tons.
- **FX** : EQ puis Compressor, dans Serum. EQ : bosse basse vers 47 Hz (fondamentale observée entre 40 et 50 Hz), légère ; bosse haute vers 8,8 kHz, gain réduit, Q élargi. Compressor : seuil baissé, attaque montée, release un peu plus longue, gain un peu monté.
- **Hors Serum** : creux étroit sur les bas-médiums « boueux », petite coupe seulement, sinon on « tue » le kick ; par un EQ tiers.
- **Calcul** : 1/16 dure 125 ms à 120 BPM : la chute de 12 demi-tons s'étale sur la moitié du kick [CALCUL].
- **Macros** : `Pitch Decay` RATE de LFO 1 (1/32 → 1/8) · `Cutoff Decay` — · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Usage** : ici le kick tient le grave (fondamentale vers 47 Hz) ; avec un sub, préférer KS01 ou KS13.
- **Origine** : [SOURCE DM-02, Jon Audio, Serum 1] ; « réduire le pitch dive s'il est trop marqué » (7:52).

### KS04 Kick étouffé SKETIMUSIC — le deep « plus muffled »
- **OSC A** : Analog_BD_Sin, OCT −1, master à 49 ; la position dans la table change aussi le son.
- **Hauteur** : LFO 1 en ENVELOPE, 1/4 → Global › Master Tune ; forme : descente sur la première double croche, plus lente sur la deuxième, puis queue sur la deuxième croche.
- **Amplitude** : ENV 1 : hold ≈ 125 ms, decay ≈ 125 ms à 125 BPM (une croche). À 120 BPM, pour garder la croche : hold ≈ 130 ms, decay ≈ 130 ms [CALCUL, × 125/120].
- **Clic** : NOISE Bright White, LFO 2 (ENVELOPE, 1/8) en forme très courte sur son niveau : un clic de type hi-hat.
- **Filtre** : MG Low 18, FAT monté, LFO 3 (ENVELOPE, 1/4) → CUTOFF, assez fermé pour le deep.
- **FX** : EQ en creux vers 300 Hz ; Distortion Soft Clip modulée par LFO 3, surtout sur le transitoire.
- **Non repris** : FM par OSC B en triangle à +1 octave (variante plus dure) ; OTT, Glue Compressor en soft clip et EQ d'Ableton (effets natifs).
- **Macros** : `Pitch Decay` profondeur de LFO 1 · `Cutoff Decay` profondeur de LFO 3 → CUTOFF · `Click` niveau du NOISE · `Release` decay d'ENV 1.
- **Origine** : [SOURCE DM-03, SKETIMUSIC, Serum 1, testé à 125 BPM] : « pour la deep house, un kick plus étouffé ».

### KS05 Kick sourd Arc Nade — phase 122, Tape
- **OSC A** : sinus, OCT −2, random phase off, PHASE ≈ 122 ; level monté, master baissé.
- **Amplitude** : ENV 1 : attack, hold, sustain, release au minimum, decay ≈ 80 ms ; courbe modifiée.
- **Hauteur** : ENV 2 → CRS, unipolaire, quantité ≈ 20 ; ENV 2 : decay ≈ 80 ms, le reste à 0.
- **FX** : Distortion Tape (Tube, Soft Clip, Diode, Asym et Stomp Box essayés) ; Compressor ; EQ en passe-bas pour un son plus sourd.
- **Variante** : allonger decay et sustain pour aller vers une 808 [SOURCE].
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` fréquence du passe-bas de l'EQ · `Click` DRIVE de la Tape · `Release` decay d'ENV 1.
- **Test** : 80 ms est court : à 120 BPM, le kick dure moins d'une double croche (125 ms) [CALCUL]. Il laisse beaucoup de place au sub.
- **Origine** : [SOURCE DM-04, Arc Nade, Serum 1].

### KS06 Kick minimal Londonpatchwork — le passe-bas qui finit bas
- **OSC A** : Analog_BD_Sin, random phase 0, PHASE réglée pour partir au pic de l'onde.
- **Hauteur** : ENV 2 → CRS, unipolaire ; sustain au minimum, un peu de release ; attaque ≈ 20 (unité non dite).
- **Filtre** : Low 24, RES basse ; ENV 3 → CUTOFF, unipolaire, release ajoutée, CUTOFF de base bas ; attaque ≈ 20 (unité non dite).
- **Amplitude** : ENV 1, un peu de release.
- **FX** : aucun.
- **Macros** : celles de la source, reprises par tout le lot : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` decay d'ENV 3 · `Click` RES du filtre (plus haut = plus de clic et d'aigu) · `Release` release d'ENV 1.
- **Usage** : minimal et microhouse ; CUTOFF bas et RES faible.
- **Origine** : [SOURCE DM-05, Londonpatchwork, Serum 1, patch gratuit en lien sur le site] ; pattern MIDI 4/4 sur C3.

### KS07 Kick essentiel Octocap — un sinus, hold 50, decay 100
- **OSC A** : sinus, PHASE 0, aucune randomness, OCT −1.
- **Hauteur** : ENV 2 → CRS (ENV 1 sert à l'amplitude du son entier) ; ENV 2 : sustain 0, decay ≈ 100 ms (« je trouve 100 ms plutôt bien »). Trop de chute donne un son de tom, un autre réglage un son de « ballon de basket ».
- **Amplitude** : ENV 1 : attaque au minimum (« frappe mieux »), hold 50 ms, decay 100 ms, sustain 0.
- **FX** : aucun ; après coup, retirer du « bulk » dans le bas-médium change beaucoup la forme d'onde : compenser par compression ou saturation.
- **Macros** : `Pitch Decay` decay d'ENV 2 · `Cutoff Decay` — · `Click` quantité d'ENV 2 → CRS · `Release` decay d'ENV 1.
- **Usage** : base à superposer à des sons organiques (description de la vidéo).
- **Origine** : [SOURCE HC-09 = AF-05, Octocap, Serum 2].

### KS08 Kick « soft » à deux sinus — arrêté avant la distorsion
- **OSC A** : sinus (Basic Shapes), pour l'attaque ; LFO 1 (ENVELOPE, BPM désactivé, rate au maximum, forme en descente) → CRS d'A, unipolaire, « autour de 50 » ; LFO 2 (ENVELOPE, BPM désactivé, rate vers 90 Hz) → volume d'A : il coupe le sinus après l'attaque.
- **OSC B** : sinus, LEVEL ≈ 60, pour le corps ; LFO 3 (ENVELOPE, BPM actif, rate « autour de 2 ») → volume de B : la longueur du kick ; LFO 4 → hauteur de B, bipolaire, ≈ −40 à −50, très rapide.
- **FX** : **aucun**. La vidéo dit qu'à ce stade le kick est « assez soft », puis ajoute un Hard Clip à 100 %, du bruit et du Bend+ : ces étapes ne sont pas reprises pour la signature.
- **Accord** : GTune ; un demi-ton vers le haut ou le bas selon la tonalité.
- **Macros** : `Pitch Decay` RATE de LFO 1 · `Cutoff Decay` — · `Click` profondeur de LFO 2 · `Release` RATE de LFO 3.
- **Test** : la valeur « 2 » de LFO 3 (division ou durée) est à lire à l'écran.
- **Origine** : [SOURCE DM-06 = BH-04, Wildcrow Studio, Serum 1], version arrêtée vers 3:30.

### KS09 Kick clean adouci MERAKKI — fondu, Splitter, réverb modulée
- **OSC A** : sinus, octave baissée au registre sub ; random phase 0, PHASE 90° (petit clic) ; attaque d'enveloppe 0,1 ms.
- **Hauteur** : LFO en ENVELOPE, 1/8, courbe descendante → CRS, unipolaire. Courbe lisse et continue ; le kick se pose sur la note avant la fin. Une seconde chute très rapide fait un petit « tick » ; ne pas aller vers le « laser ».
- **Amplitude** : un second LFO en ENVELOPE sur le volume. Trop de clic : ajouter un point au début pour un léger fondu d'entrée, et le kick devient « beaucoup plus soft ».
- **Clic** : NOISE blanc, LFO ENVELOPE 1/16 en forme très serrée sur son niveau, routé dans un filtre passe-haut (le sinus hors du filtre) : « presque imperceptible ».
- **FX** :
  1. EQ léger : un peu plus vers 120 Hz (« knock »), encoche vers 1 kHz.
  2. Splitter (Frequency Splitter de Serum 2), pour le déphasage de ses filtres de séparation, pas pour traiter : attaque « plus douce, plus organique ».
  3. Reverb (type à vérifier), MIX modulé par un LFO ENVELOPE 1/8 : 0 sur le transitoire, un peu ensuite, puis fondu.
- **Macros** : `Pitch Decay` RATE du LFO de hauteur · `Cutoff Decay` profondeur du LFO sur le MIX de la Reverb · `Click` niveau du NOISE · `Release` dernier point du LFO de volume.
- **Origine** : [SOURCE AF-01 = HC-05, MERAKKI, Serum 2], premier kick seulement ; le second, « thumpy », va au lot tech house.

### KS10 Kick 808 soft de la démo — la recette du dépôt
- **OSC A** : sinus, départ de phase stable (RAND 0).
- **Hauteur** : enveloppe brève, courbe douce, decay de départ 30-60 ms.
- **Amplitude** : sustain −∞, 280-500 ms, toujours plus court que l'écart entre deux kicks (536 ms à 112 BPM, 500 ms à 120) et que l'écart avant la note de sub suivante.
- **Couleur** : une harmonique très modérée par saturation ou drive, pour rester audible à faible niveau.
- **Si le clic devient dur** : réduire la profondeur de hauteur, le bruit et l'aigu avant de couper le corps.
- **Macros** : `Pitch Decay` · `Cutoff Decay` DRIVE · `Click` · `Release`, comme KS01.
- **Test** : régler note et longueur sur plusieurs fondamentales ; ne pas supposer qu'une seule note sert tout le morceau.
- **Origine** : recette « Kick Serum 2, esprit 808 soft » de `../../../produire-demo-electro-rapide/references/recettes.md`.

### KS11 Kick court sous un sub chargé — une double croche
- **Patch** : KS01, avec ENV 1 : hold 30 ms, decay 90 ms (≈ une double croche à 120 BPM, 125 ms) ; chute de hauteur de 8 demi-tons en 50 ms.
- **Usage** : sub en doubles croches ou en contretemps rapprochés.
- **Macros** : celles de KS01.
- **Test** : le kick ne doit pas disparaître à faible volume ; sinon remonter le hold (diagnostic 2).
- **Origine** : règle de longueur de `../../../kick-bass-equilibre/SKILL.md` § 2 ; KS05 [SOURCE DM-04] montre qu'un decay de 80 ms reste un kick ; valeurs [ORIGINAL].

### KS12 Kick long qui tient le grave — électro chill à 112 BPM
- **Patch** : KS01, avec :
  - fondamentale F0 (43,7 Hz) pour un morceau en fa mineur : le kick tient le grave ;
  - ENV 1 : hold 120 ms, decay 300 ms (420 ms au total, sous la noire de 536 ms) [CALCUL] ;
  - chute de 7 demi-tons en 80 ms, courbe concave ;
  - FILTER 1 ouvert plus haut au départ, pour que l'attaque reste claire.
- **Basse** : la basse joue dans les silences ou au-dessus de 80-100 Hz ; bloc « Électro chill 112 — kick long et basse dans les silences » ci-dessous.
- **Macros** : celles de KS01.
- **Test** : jouer toutes les fondamentales de la progression ; le kick accordé sur la tonique peut frotter sur les autres accords.
- **Origine** : rôle « le kick tient le grave » de `../../../kick-bass-equilibre/SKILL.md` § 1 ; longueur de 280-500 ms de KS10 ; valeurs [ORIGINAL].

### KS13 Kick accordé à la quinte — C1 sous une tonique fa
- **Patch** : KS01, joué en C1 (65,4 Hz) pour un morceau en fa ; en F1 (87,3 Hz) si l'on préfère la tonique.
- **Table** (`theorie.py sub <tonique>`) [CALCUL] :

  | Tonique | Sub | Kick sur la quinte | Kick sur la tonique |
  | --- | --- | --- | --- |
  | F | F0, 43,7 Hz | C1, 65,4 Hz | F1, 87,3 Hz |
  | G | G0, 49,0 Hz | D1, 73,4 Hz | G1, 98,0 Hz |

- **Test** : à l'accordeur, la fin de la note doit lire la quinte ; puis `kick_bass_check.py` : le kick et le sub ne doivent pas battre l'un contre l'autre.
- **Macros** : celles de KS01.
- **Origine** : `../../../kick-bass-equilibre/SKILL.md` § 2 et `theorie.py sub` ; accord par la note jouée [SOURCE DM-01, DM-02].

### KS14 Kick à hauteur fixe — suivi de note coupé
- **Patch** : KS01, avec le suivi de hauteur de l'oscillateur coupé : le kick sonne pareil quelle que soit la note MIDI. La hauteur se règle alors par CRS et FINE d'A.
- **Usage** : quand la note du kick doit rester la même sous une ligne de sub qui bouge, ou quand plusieurs pads jouent le même kick.
- **Macros** : celles de KS01 ; une macro sur CRS peut remplacer la note.
- **Test** : vérifier dans Serum 2 où se coupe le suivi de hauteur de l'oscillateur.
- **Origine** : option « couper le pitch tracking pour un kick identique sur toutes les notes » de `../kicks-serum-synthese.md` (« Architecture commune ») ; geste [DÉDUCTION].

### KS15 Kick à clic de second sinus — deux octaves au-dessus
- **Patch** : KS01, plus OSC B en sinus deux octaves au-dessus de la fondamentale, joué un instant : ENV 4 → LEVEL de B, decay 10-20 ms, sustain 0 ; LEVEL de base de B à 0. Pas de NOISE.
- **Calcul** : pour un kick en C1, le second sinus est en C3 (261,6 Hz) [CALCUL].
- **Macros** : `Click` quantité d'ENV 4 → LEVEL de B · les autres comme KS01.
- **Test** : A/B avec KS01 ; un clic tonal est souvent moins dur qu'un clic de bruit (à juger).
- **Origine** : « clic au second sinus deux octaves au-dessus de la fondamentale » [SOURCE BH-02, DM-03, `../kicks-serum-synthese.md`] ; valeurs [ORIGINAL].

### KS16 Kick à couche acoustique — sample « DX » sans son attaque
- **OSC A** : sinus (Basic Shapes), random phase 0, PHASE 90 ; un LFO en ENVELOPE → LEVEL ; un second LFO → Coarse, unipolaire, « autour de 12 % ou 24 » ; oscillateur accordé quelques demi-tons plus bas.
- **OSC B** (transitoire) : LFO 3 → LEVEL, forme très courte ; random phase 0, PHASE ≈ 95 (différente d'A, contre les annulations) ; LFO 3 aussi → Coarse, accordé très haut. Pour la signature, le baisser.
- **OSC C** : mode Sample, One Shot, Factory › Non-tonal › Drum › Kicks › « DX » ; LFO 4 (ENVELOPE) → LEVEL avec un fondu d'entrée, pour sauter l'attaque du sample.
- **FILTER 2** sur C : retirer un peu de grave de la couche acoustique ; couche baissée dans le mix.
- **NOISE** : « Pink Noise Stereo », doux et court, sous un LFO.
- **FX** : EQ (graves relevés, Q augmenté, un peu de haut-médium) ; Compressor simple, attaque rapide.
- **Macros** : `Pitch Decay` quantité du LFO → Coarse (12 plutôt que 24) · `Cutoff Decay` CUTOFF de FILTER 2 · `Click` LEVEL de B · `Release` dernier point du LFO de volume d'A.
- **Origine** : [SOURCE AF-03, DNB Academy, Serum 2] : kick « acousticy, funk ».

### KS17 Kick à couche foley — une percussion dans le NOISE
- **OSC A** : sinus (Basic Shapes), OCT −2 ; ENV 1 : decay 200-300 ms, sustain 0 ; random phase 0.
- **Hauteur** : ENV 1 → Coarse, unipolaire, ≈ 16.
- **SUB** : −2, LEVEL ≈ 55, ENV 1 sur le LEVEL.
- **NOISE** : un sample de percussion (la vidéo prend « tarabooka body » d'un pack foley), One Shot, pitch tracking actif (reste dans la tonalité du kick) ; LEVEL baissé, ENV 1 sur le LEVEL.
- **FX** : Distortion Tube, ENV 1 → DRIVE, DRIVE ≈ 54 (moins pour la signature) ; Compressor simple.
- **Droits** : n'utiliser qu'une percussion enregistrée par l'utilisateur ou un pack dont la licence est vérifiée.
- **Macros** : `Pitch Decay` quantité d'ENV 1 → Coarse · `Cutoff Decay` — · `Click` LEVEL du NOISE · `Release` decay d'ENV 1.
- **Origine** : [SOURCE AF-04, Ghosthack, Serum 1] ; le resampling de la vidéo (FL Studio, Infiltrator, Harmor) n'est pas repris.

### KS18 Kick tape chaud — saturation légère et air
- **Patch** : KS01, avec :
  - Distortion Tape Sat., DRIVE 15-25 %, MIX 100 % ;
  - EQ : air vers 8,8 kHz, gain faible, Q large ; bosse à la fondamentale, légère.
- **Macros** : `Click` DRIVE de la Tape Sat. à la place du NOISE · les autres comme KS01.
- **Test** : la fondamentale ne doit pas baisser quand le DRIVE monte ; à faible volume, le kick doit rester présent (diagnostic 2).
- **Origine** : Tape gardée parmi six distorsions essayées [SOURCE DM-04] ; air vers 8,8 kHz [SOURCE DM-02] ; dosage [ORIGINAL].

### KS19 Kick imprimé — figer un kick validé
- **Méthode** :
  1. Valider un kick à l'écoute, sur la note du morceau.
  2. L'imprimer en audio (procédure de `../../../resampling/SKILL.md`), une note par tonalité utile.
  3. Le rejouer dans un Simpler ou un Drum Rack ; garder le preset Serum à côté.
  4. L'inscrire au registre `../signature.md`.
- **Usage** : figer le résultat, alléger le CPU, retrouver le même kick d'un morceau à l'autre.
- **Origine** : « imprimer le kick en audio et le rejouer en sample, pour figer le résultat » [SOURCE BH-02, HC-02, HC-05, `../kicks-serum-synthese.md`].

### KS20 Kick qui se retire avant la frontière — variation de drop
- **Patch** : KS01, sans changement.
- **Jeu** : sur la dernière mesure d'une phrase de huit, pas de kick sur le temps 4 ; le sub s'arrête aussi. Alterner avec les autres gestes de la règle des drops (fill, roulement, reverse, impact, silence) d'une frontière à l'autre.
- **Variante** : `Release` monté sur le dernier kick de la phrase, pour une queue plus longue avant le silence.
- **Jeu** : bloc « Deep 120 — kick retiré avant la frontière » ci-dessous.
- **Origine** : règle « Drops » d'`AGENTS.md` (retrait de kick) ; séquence [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60) ; les notes de kick sont les **fondamentales visées** (règle 4 du lot). Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/kicks/kicks-signature-sous-124.md`.

```grille
titre: Deep 120 — kick accordé et sub en contretemps (KS01, KS13)
tempo: 120
accords: Fm7 | Fm7
kick: C1[1:2] C1[2:2] C1[3:2] C1[4:2] | C1[1:2] C1[2:2] C1[3:2] C1[4:2]
sub: F0[1&:2] F0[2&:2] F0[3&:2] Ab0[4&:2] | F0[1&:2] F0[2&:2] Eb0[3&:2] F0[4&:2]
```

Kick en C1 (quinte de fa) sur les quatre temps, notes d'une croche (250 ms) ; le sub en F0 attaque sur chaque contretemps, juste quand le kick s'éteint.

```grille
titre: Électro chill 112 — kick long et basse dans les silences (KS12)
tempo: 112
accords: Fm7 | Fm7
kick: F0[1:3] F0[2&:2] F0[3&:3] | F0[1:3] F0[2&:2] F0[4:3]
basse: F1[1a:2] Ab1[3:2] C2[4e:2] | F1[1a:2] Ab1[3:2] C2[3&:2]
```

Le kick en F0 tient le grave ; la basse médium, en F1 et au-dessus, joue entre les coups de kick.

```grille
titre: Deep 120 — kick retiré avant la frontière (KS20)
tempo: 120
accords: Fm7 | Fm7
kick: C1[1:2] C1[2:2] C1[3:2] C1[4:2] | C1[1:2] C1[2:2] C1[3:2]
sub: F0[1&:2] F0[2&:2] F0[3&:2] Ab0[4&:2] | F0[1&:2] F0[2&:2] Eb0[3&:2]
```

Mesures 7 et 8 d'une phrase de huit : au temps 4 de la mesure 8, ni kick ni sub ; le drop suivant repart sur le temps 1.

## Ce qui reste à faire par l'utilisateur

- Dire ce qui ne va pas dans le kick actuel (dur, mou, boueux, en conflit avec le sub, faux, trop long) : le diagnostic des règles propres à la signature donne alors la recette à essayer d'abord.
- Retrouver dans Serum 2 : la table Analog_BD_Sin, le bruit Attacks › Kick n° 11, le sample « DX », le suivi de hauteur de l'oscillateur ; lire à l'écran les valeurs « à vérifier » des fiches DM et AF du corpus.
- Écouter les recettes retenues contre le kick actuel, à niveau égal, avec le sub et le groove ; mesurer kick et sub sur des exports séparés ; inscrire le kick validé au registre `../signature.md` et dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
