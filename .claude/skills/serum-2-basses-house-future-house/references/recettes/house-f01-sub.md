# Vingt recettes de sub pour la House (famille F01)

Premier lot de recettes House : le sub qui tient la fondamentale sous les autres familles (F05 saw percussive, F03 pluck et hollow, F07 wub, F08 growl…). Rédigé le 05/10/2026 à partir des études de `../etudes-pages-house.md`, `../etudes-captures.md` et `../etudes-videos.md`, de `../documentation-basses.md`, de `../../../sound-designer-serum/references/basses.md` et de la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu.** Une recette est un point de départ à régler à l'oreille par l'utilisateur (règle 4 d'`AGENTS.md`). Étiquettes :
- **[SOURCE Fxx-yy]** : geste ou valeur relevés dans l'étude du tutoriel (identifiant du registre `../tutoriels-a-consulter.md`). Une valeur dite « écran » a été lue sur une capture, parfois petite : à confirmer.
- **[CALCUL]** : obtenu par une formule de `../documentation-basses.md`.
- **[DÉDUCTION]** : conséquence tirée de la documentation de Serum 2, jamais essayée.
- **[ORIGINAL]** : réglage proposé ici, sans source.

## Règles communes aux vingt recettes

1. **Une seule source tient la fondamentale** : un oscillateur, sans unison ni désaccord, mono (`basses.md`, règle sur laquelle convergent les sources). Le sub est un instrument à part de la basse médium (règle « Grave » d'`AGENTS.md`).
2. **Départ** : menu principal › Init Preset. VOICING sur MONO. Dans l'Init, seul OSC A est actif et va dans FILTER 1 ; chaque recette dit quelles sources allumer et où les router.
3. **Routage `Direct`** : la source contourne filtres et effets internes. Une recette qui sature le sub le route en `Main` et le dit.
4. **Phase** : PHASE à 0 % (ou 50 %), les deux passages par zéro d'un sinus, et RAND à 0 sur OSC A, B et C. Sinon l'attaque peut cliquer et deux sources peuvent s'annuler (cartographie, § 3.1). Le SUB a un bouton PHASE mais pas de RAND.
5. **Tessiture** : notes de Live (C3 = 60). E0 = 41,2 Hz ; F0 = 43,7 ; G0 = 49,0 ; A0 = 55,0 ; B0 = 61,7 ; C1 = 65,4 ; D1 = 73,4 Hz. La zone F0-A0 (MIDI 29-33), où l'on « sent et entend », est relevée sur le piano roll de Live de F01-13 [SOURCE F01-13, écran]. Sous E0, tous les systèmes ne suivent pas. Si la tonique tombe trop bas, jouer le sub une octave plus haut.
6. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`). Un Compressor de Live déjà en place en sidechain, ou un Utility, sont tolérés (`../tempo-mix.md`). Repères de sidechain du sub au kick : attaque 3-10 ms, release 50-150 ms [SOURCE F01-13]. Le compresseur de la capture était à 4:1, 5 ms, 70 ms et −32,1 dB [SOURCE F01-13, écran].
7. **Quatre macros communes**, pour comparer les recettes avec les mêmes gestes. Chaque recette donne ses bornes ; un « — » signale une macro non utilisée.
   - `Length` : release ou decay d'ENV 1.
   - `Glide` : temps de PORTA.
   - `Weight` : drive de saturation ou niveau de l'harmonique ajoutée, avec compensation de niveau.
   - `Knock` : quantité de l'enveloppe de hauteur, ou chute de hauteur.

   Avant d'assigner une macro, vérifier qu'un « + » apparaît sur la destination : toutes les destinations n'en acceptent pas (cartographie, § 7.3). Sinon, régler la valeur à la main.
8. **Contrôle par l'utilisateur, pour chaque recette**, toujours dans cet ordre :
   - le sub seul, sur trois notes (la tonique, la plus grave, la plus aiguë du morceau) ;
   - puis avec le kick, en mono ;
   - puis à faible volume et sur un petit haut-parleur ;
   - enfin en A/B à niveau égal contre S01.

   Côté Claude : relecture des paramètres et niveaux relatifs (`lom.py meters`). Sur exports séparés, `kick_bass_check.py` de `../../../kick-bass-equilibre/SKILL.md` mesure la corrélation dans les 30-120 Hz. Régler le niveau du sub par pas de 0,5 à 1 dB : dans le grave, quelques décibels changent beaucoup la sonie [CALCUL, ISO 226 dans `../documentation-basses.md`].

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| S01 | Sinus Direct | toute House, référence A/B | fondamentale nue |
| S02 | Sinus à phase continue | lignes roulantes Tech House | pas de saut de phase entre notes |
| S03 | Triangle filtré de layering | sous une saw ou un pluck | quelques impaires, coupées haut |
| S04 | Carré arrondi passe-bas | Future House, Bass House | carrée rendue ronde par un ladder |
| S05 | Octave fantôme | lisibilité sur petit haut-parleur | 2e harmonique dosée |
| S06 | Sinus saturé en parallèle | Bass House, Tech House | Soft Sat. à faible mix |
| S07 | Sub et crête saturée séparés | Bass House chargée | Splitter L/H, distorsion en haut seulement |
| S08 | 808 House à knock | G-House, Tech House | enveloppe de hauteur +24 st |
| S09 | 808 tech à portamento | Tech House 124-126 | table Analog_BD_Sin, chute de hauteur |
| S10 | Sub pulsé sur la grille | Bass House, Future House | LFO calé sur le transport, pas de compresseur |
| S11 | Sub court en contretemps | Tech House | durée donnée par ENV 1 en BPM |
| S12 | Sub glissé Deep House | Deep House, Organic House | portamento court et proportionnel |
| S13 | Sub à attaque ronde | sous 124 BPM, kick long et doux | attaque lente, laisse passer le kick |
| S14 | Sub harmonique animé | morceau sans basse médium | impulsion en morph spectral, LFO 3,9 Hz |
| S15 | Sub carré à « toc » | Future House | ENV 2 bref sur un passe-bas propre |
| S16 | Sinus et clic de sample | Tech House, kick discret | transitoire de moins de 100 ms en OSC B |
| S17 | Triangle et Add Bass | Deep House, Garage | filtre Add Bass, à mesurer |
| S18 | Sub à chute de fin de phrase | toute House, avant une frontière de 8 mesures | macro `Knock` sur CRS du SUB |
| S19 | Sub sensible à la vélocité | Tech House à notes fantômes | vélocité vers niveau et decay |
| S20 | Sinus FM 1:1 | Bass House, sub un peu chaud | FM (Sub) faible, 2e harmonique |

## Les vingt recettes

### S01 Sinus Direct — référence de toute la famille
- **Patch** : OSC A éteint. SUB allumé en Sine, PHASE 0 %, routé `Direct`. VOICING MONO, LEGATO off.
- **ENV 1** : attaque 3 ms, hold 0, sustain 0 dB, release 60 ms. Le decay est sans effet à sustain plein.
- **Release** : 50-100 ms pour des notes espacées, 20-30 ms si elles se suivent de près (`../families.md`, fiche 1 ; `basses.md` § Sub).
- **Macros** : `Length` (release) 20 → 120 ms · `Glide` 0 → 60 ms · `Weight` — · `Knock` —.
- **Jeu** : la ligne du morceau dans F0-A0. Motif de départ : bloc « Bass House 128 » de `../motifs.md`, voix `sub`.
- **Test** : chaque note doit sortir au même niveau. Écouter la fin de queue sans le kick.
- **Origine** : sinus pur et mono [SOURCE F01-02, F01-13] ; valeurs d'enveloppe [ORIGINAL] dans la fourchette de `families.md`.

### S02 Sinus à phase continue — lignes roulantes
- **Patch** : S01, avec un réglage en plus : clic droit sur PHASE du SUB › **Contiguous**. La note reprend la phase de la précédente.
- **ENV 1** : attaque 1-2 ms, release 30 ms.
- **Macros** : `Length` 15 → 60 ms · `Glide` 0 → 30 ms · `Weight` — · `Knock` —.
- **Jeu** : doubles croches serrées autour de la tonique, notes jointives. Motif : bloc « Tech House 124 — sub roulant » ci-dessous.
- **Test** : A/B avec S01 sur la même ligne. S02 doit cliquer moins entre deux notes, mais son attaque varie d'une note à l'autre.
- **Origine** : [DÉDUCTION] de la cartographie (§ 3.7 : Contiguous, phase continue). Sans Contiguous, un départ toujours identique se cale mieux sur le kick : choisir à l'oreille.

### S03 Triangle filtré de layering — sous une saw ou un pluck
- **Patch** :
  - SUB en Triangle, PHASE 0 %, routé vers FILTER 1.
  - FILTER 1 en MG Low 24, CUTOFF 120-150 Hz, RES 0, key track allumé, sortie `Direct`.
- **ENV 1** : attaque 3 ms, release 70 ms.
- **Macros** : `Length` 30 → 120 ms · `Glide` 0 → 60 ms · `Weight` = CUTOFF 90 → 200 Hz · `Knock` —.
- **Jeu** : la même ligne que la basse médium, une octave plus bas.
- **Test** :
  - avec la couche médium coupée sous 100-120 Hz, la somme ne doit pas creuser le grave ;
  - comparer à S01 sur petit haut-parleur.
- **Origine** :
  - triangle préféré pour le layering, « se marie mieux » [`basses.md`, SOS] ;
  - passe-bas raide, départ 120-150 Hz à 24 dB/oct (`basses.md`, point de départ 2, [I]) ;
  - key track obligatoire sur un filtre de sub (`basses.md`, SOS).

### S04 Carré arrondi passe-bas — sub Future House et Bass House
- **Patch** :
  - OSC A sur Basic Shapes, WT POS sur la frame carrée, PHASE 0 %, RAND 0, routé vers FILTER 1.
  - FILTER 1 en MG Low 24, RES ≈ 15 %, DRIVE et VAR (FAT) au minimum, key track allumé, sortie `Main`.
  - CUTOFF à environ deux fois la fondamentale de la note la plus jouée : 110-140 Hz sur F0-A0.
- **ENV 1** : attaque 3 ms, release 80 ms.
- **Macros** : `Length` 30 → 150 ms · `Glide` 0 → 60 ms · `Weight` = CUTOFF 80 → 220 Hz · `Knock` —.
- **Jeu** : notes tenues après le kick (bloc wub de `../motifs.md`, voix `sub`).
- **Test** : il doit paraître plus présent que S01 à faible volume, sans changer de niveau d'une note à l'autre.
- **Origine** :
  - carrée de Basic Shapes dans un MG Low 24 [SOURCE F01-13, écran] ;
  - positions lues sur la capture : CUTOFF ≈ 33-39 %, RES ≈ 17 %, DRIVE et FAT proches du minimum (estimations visuelles) ;
  - la valeur en Hz et le key track sont [ORIGINAL].

### S05 Octave fantôme — lisibilité sur petit haut-parleur
- **Patch** :
  - SUB en Sine, PHASE 0 %, routé `Direct`.
  - OSC A sur Default, position 1 (sinus), une octave au-dessus du SUB, PHASE 0 %, RAND 0, routé `Direct`.
  - Vérifier à l'accordeur que A sonne exactement une octave au-dessus du SUB.
- **ENV 1** : attaque 3 ms, release 60 ms. Elle s'applique aux deux sources.
- **Niveau de A** : le régler à l'analyseur, pic à 2 × f entre −20 et −12 dB sous le pic de la fondamentale.
- **Macros** : `Length` 20 → 120 ms · `Glide` 0 → 60 ms · `Weight` = LEVEL d'OSC A de 0 à la borne trouvée · `Knock` —.
- **Jeu** : comme S01.
- **Test** :
  - sur téléphone ou petit haut-parleur, la ligne doit rester lisible ;
  - sur gros système, elle ne doit pas paraître plus aiguë.
- **Origine** :
  - Default position 1 = sinus [SOURCE F01-02] ;
  - fondamentale manquante sur petit haut-parleur : trouvée, non lue (`../documentation-basses.md` § 6) ;
  - niveaux [ORIGINAL].

### S06 Sinus saturé en parallèle
- **Patch** : SUB en Sine, PHASE 0 %, routé `Main`. Dans le rack FX :
  - Distortion en mode Soft Sat., à défaut Soft Clip, filtre de la distorsion OFF ;
  - DRIVE 20-40, MIX 25-40 % ;
  - LEVEL du module baissé pour compenser.
- **ENV 1** : attaque 3 ms, release 60 ms.
- **Macros** : `Length` 20 → 120 ms · `Glide` 0 → 60 ms · `Weight` = DRIVE 0 → 50 (et LEVEL en sens inverse) · `Knock` —.
- **Jeu** : comme S01.
- **Test** :
  - balayer `Weight` en regardant le pic de la fondamentale : s'il baisse, réduire le drive ou revenir à S07 ;
  - A/B à niveau égal, sinon le plus fort gagne.
- **Origine** :
  - sinus de Basic Shapes, puis Distortion en Soft Clip ; « la fondamentale faiblit avec la distorsion » [SOURCE F01-13] ;
  - la capture montrait un drive haut (≈ 85-90 %, estimation) et un mix plein [SOURCE F01-13, écran]. Ici, mix réduit pour un usage parallèle [ORIGINAL].

### S07 Sub et crête saturée séparés — Bass House chargée
- **Patch** :
  - SUB en Sine, PHASE 0 %, routé `Direct` : il tient seul la fondamentale.
  - OSC A sur Basic Shapes en triangle, à la même octave que le SUB, PHASE 0 %, RAND 0, routé `Main`.
  - Rack FX : Splitter L/H, SPLIT FREQ 120 Hz, LOWS au minimum (le grave d'OSC A est retiré).
  - Dans HIGHS : Distortion en Tube, DRIVE 30-50, MIX 100 %, puis Equalizer, bande haute en Low Pass vers 3-5 kHz.
- **ENV 1** : attaque 3 ms, release 70 ms.
- **Macros** : `Length` 30 → 120 ms · `Glide` 0 → 60 ms · `Weight` = DRIVE de la Distortion 0 → 70 · `Knock` —.
- **Jeu** : sous un growl ou une saw, notes courtes.
- **Test** :
  - couper OSC A : le grave ne doit pas bouger ;
  - le remettre : la ligne doit gagner en présence au-dessus de 120 Hz.
- **Origine** :
  - « split the low high and just put a distortion on the high end », les distorsions de Serum marchant mal dans le grave [SOURCE F01-01] ;
  - saturation séparée à 123 Hz, beaucoup moins de drive en bas, faite dans Saturn [SOURCE F01-06] ;
  - transposition dans le Splitter de Serum 2 [ORIGINAL].

### S08 808 House à knock — G-House, Tech House
- **Patch** :
  - OSC A sur Default, position 1 (sinus), Unison 1, OCT −1, PHASE 0 %, RAND 0, routé `Main`.
  - Hauteur : ENV 2 vers CRS d'OSC A, quantité réglée pour +24 demi-tons au pic (lire l'infobulle), attaque 0, decay 60 ms, sustain 0.
  - Rack FX : Distortion en Overdrive, DRIVE 25 %, MIX 60 %, puis Filter en MG Low 12, CUTOFF 400 Hz, placé après la distorsion.
  - VOICING MONO + LEGATO, PORTA 100 ms.
- **ENV 1 (House)** : attaque 0, decay 400-700 ms, sustain 0 %, release 100 ms. Une 808 de trap tient plutôt 3 s.
- **Macros** : `Length` = decay 250 → 900 ms · `Glide` 0 → 150 ms · `Weight` = DRIVE 0 → 50 · `Knock` = quantité d'ENV 2, de 0 à +24 st.
- **Jeu** : motif « G-House 124 — 808 à glissés » ci-dessous. Les notes qui se chevauchent glissent, les notes séparées redéclenchent.
- **Test** :
  - avec le kick, le knock ne doit pas doubler son attaque ; sinon `Knock` vers +12, ou decay d'ENV 2 à 30 ms ;
  - accorder avec `Knock` à 0 : un clic long fait paraître la note plus haute.
- **Origine** :
  - +24 st / 60 ms, Overdrive 25 % / 60 %, passe-bas vers 400 Hz après la distorsion, Mono + Legato, porta 100 ms [SOURCE F01-02, page et infographie] ;
  - le modèle du passe-bas n'est pas nommé : MG Low 12 est [ORIGINAL] ;
  - decay court pour la House [ORIGINAL] ;
  - au-delà de 50 % de drive avec un mix haut, la page dit qu'on quitte la 808.

### S09 808 tech à portamento — Tech House 124-126
- **Patch** :
  - OSC A sur la table Analog › Analog_BD_Sin (table de Serum 1, à retrouver dans le navigateur de Serum 2), Unison 1, Detune, Blend et RAND au minimum, WT POS ≈ 209.
  - FILTER 1 en MG Low 12 sur A, CUTOFF ≈ 39 %, RES ≈ 17 %, DRIVE ≈ 6 %, FAT ≈ 61 %.
  - Hauteur : ENV 2 vers SEM d'OSC A, chute vers la note. ENV 2 : attaque 0,2 ms, hold 18 ms, decay 192 ms, sustain 0 %, release 512 ms.
  - Rack FX : Splitter L/H à 123 Hz, Distortion Tape Sat. dans les deux bandes, drive nettement plus bas dans LOWS.
  - VOICING MONO, LEGATO off, PORTA ≈ 300 ms, SCALED allumé.
- **ENV 1 lue sur la capture** : 188 ms / 0 / 507 ms / −2,1 dB / 1,98 s. Pour la Tech House, release ramenée à 150-300 ms.
- **Macros** : `Length` = release 100 → 600 ms · `Glide` 0 → 300 ms · `Weight` = drive de la bande HIGHS · `Knock` = quantité d'ENV 2, de 0 à +12 st.
- **Jeu** : notes de deux doubles croches en contretemps, un glissé d'octave par phrase au plus.
- **Test** :
  - le portamento de 300 ms couvre plus d'une croche à 124 BPM (241,9 ms) : vérifier qu'il ne brouille pas la note d'arrivée ;
  - régler `Knock` avec le kick.
- **Origine** :
  - table, porta 300 ms, WT POS 209, Tube avec filtre HP, saturation séparée à 123 Hz [SOURCE F01-06, page] ;
  - ENV 1, ENV 2 et positions du filtre [SOURCE F01-06, écran ; positions = estimations visuelles] ;
  - la quantité d'ENV 2 n'est lisible nulle part : la borne de +12 st est [ORIGINAL] ;
  - Serum 1 ; Splitter et Tape Sat. de Serum 2 à la place de Saturn [ORIGINAL].

### S10 Sub pulsé sur la grille — ducking sans compresseur
- **Patch** : S01, plus LFO 1 sur le niveau du SUB.
  - Type Normal, mode FREE, BPM, RATE 1/4, HOST allumé (phase calée sur le transport), MONO allumé (un seul LFO pour toutes les voix).
  - Forme : 1 au début du cycle, retour à 0 en 20 % du cycle, courbe convexe.
  - Matrice : LFO 1 → LEVEL du SUB, quantité négative. À −100, le sub est muet au coup de kick : vérifier dans l'infobulle.
- **ENV 1** : attaque 3 ms, release 60 ms.
- **Durée du creux** : 20 % d'une noire font 97 ms à 124 BPM (noire de 483,9 ms) et 94 ms à 128 BPM (468,8 ms). Cela tombe dans les 50-150 ms de release du sidechain [CALCUL avec `../tempo-mix.md`].
- **Macros** : `Length` 20 → 120 ms · `Glide` 0 → 60 ms · `Weight` = quantité LFO 1 → LEVEL, de 0 à −100 · `Knock` —.
- **Jeu** : notes tenues qui recouvrent les kicks. Motif : bloc wub de `../motifs.md`, voix `sub`.
- **Test** :
  - lancer la lecture depuis plusieurs points du morceau : le creux doit toujours tomber sur le kick ;
  - comparer à un sidechain par plug-in tiers (Kickstart 2, LFO Tool).
- **Origine** :
  - modes FREE et HOST, LFO MONO [cartographie, § 7.2] ;
  - forme et quantités [ORIGINAL] ;
  - Kickstart 2 [SOURCE F05-03] et LFO Tool [SOURCE F08-01] sont des plug-ins tiers vus dans les études.
- **Limite** : le creux suit la grille, pas le kick réel. Si le kick est décalé ou swingué, revenir à un vrai sidechain.

### S11 Sub court en contretemps — Tech House
- **Patch** : S01, avec ENV 1 en mode BPM.
- **ENV 1** : attaque 2 ms, decay 1/16 à 1/8, sustain 0 % (−∞ dB), release 1/64. La durée vient de l'enveloppe, plus de la longueur de la note MIDI.
- **Macros** : `Length` = decay 1/32 → 1/8 · `Glide` — · `Weight` — · `Knock` —.
- **Jeu** : motif « Tech House 124 — sub en contretemps » ci-dessous.
- **Test** :
  - à 124 BPM, 1/16 = 121 ms et 1/8 = 241,9 ms : le sub doit s'éteindre avant le kick suivant ;
  - aucun clic de fin à release très court ; sinon release 1/32.
- **Origine** : mode BPM des enveloppes [cartographie, § 7.1] ; durées [ORIGINAL] ; jeu en contretemps (`../tempo-mix.md`).

### S12 Sub glissé Deep House — Deep House, Organic House
- **Patch** : S01, avec VOICING MONO + LEGATO.
  - PORTA 40-80 ms, CURVE convexe (part vite, arrive lentement).
  - ALWAYS allumé : glisse même entre notes non liées, donc les notes MIDI n'ont pas à se chevaucher.
  - SCALED allumé : une octave prend la valeur du bouton, un intervalle plus petit glisse plus vite.
- **ENV 1** : attaque 5 ms, release 90 ms.
- **Macros** : `Length` 50 → 150 ms · `Glide` 0 → 120 ms · `Weight` — · `Knock` —.
- **Jeu** : motif « Deep House 122 — sub lié avec glissés » ci-dessous.
- **Test** :
  - à 122 BPM une croche dure 245,9 ms ; 200 ms de glissé l'occuperaient presque entière, d'où 40-80 ms ;
  - écouter si le glissé arrive avant le temps suivant.
- **Origine** :
  - glide de 40-80 ms pour une Deep House discrète, plutôt que 200 ms (`basses.md` § Sub, [I]) ;
  - ALWAYS, SCALED et CURVE [cartographie, § 9, Portamento].

### S13 Sub à attaque ronde — sous 124 BPM, kick long et doux
- **Patch** : S01.
- **ENV 1** : attaque 10-15 ms, courbe d'attaque concave (glisser le segment dans le graphe), release 100 ms.
- **Macros** : `Length` 60 → 160 ms · `Glide` 0 → 60 ms · `Weight` — · `Knock` = ATK d'ENV 1, de 3 à 20 ms (ce n'est pas une hauteur ; c'est le geste « place au kick »).
- **Jeu** : notes posées après le kick, sur le « e » ou le « & ».
- **Test** :
  - avec le kick Serum 2 de la signature (doux, clair, chaleureux, voir `AGENTS.md`), l'attaque du kick doit rester nette sans creux de niveau entre kick et sub ;
  - mesurer la corrélation avec `kick_bass_check.py`.
- **Origine** : [ORIGINAL]. Une période dure 22,9 ms à F0 et 18,2 ms à A0 : une attaque de 10-15 ms reste sous une période [CALCUL].

### S14 Sub harmonique animé — morceau sans basse médium
- **Patch** :
  - OSC A, éditeur de wavetable. Frame 1 : huit pas au maximum puis huit au minimum, ce qui donne un carré. Frame 2 : tous les pas au minimum sauf le premier, ce qui donne une impulsion de 12,5 %.
  - Menu MORPH › Morph - Spectral. WT POS à 1.
  - LFO 1 → WT POS d'OSC A, quantité 8, BPM désactivé, RATE 3,9 Hz.
  - FILTER 1 avec key track, CUTOFF 374 Hz, RES 23 %, DRIVE 10 %. Type non nommé par la source : MG Low 12 [ORIGINAL].
  - VOICING MONO.
- **ENV 1** : attaque 0,8 ms, release 27 ms.
- **Macros** : `Length` 15 → 80 ms · `Glide` 0 → 60 ms · `Weight` = quantité LFO 1 → WT POS, de 0 à 16 · `Knock` —.
- **Jeu** : basse seule dans un breakdown ou une House minimale.
- **Test** :
  - le niveau doit rester stable malgré l'animation ;
  - sur gros système, aucune note ne doit pomper.
- **Origine** :
  - toutes les valeurs [SOURCE F01-12, page, Serum 1] ;
  - Morph - Spectral existe dans le menu MORPH de Serum 2 (cartographie, § 3.8) ;
  - la page le dit : un timbre riche filtré convient quand le grave est libre, un sinus quand il est chargé.
- **Hors règle** : ce sub est animé. Il ne se superpose pas à une basse médium, car la règle exige un sub stable.

### S15 Sub carré à « toc » — Future House
- **Patch** :
  - SUB en Rounded Rect, PHASE 0 %, routé vers FILTER 1.
  - FILTER 1 en German LP (passe-bas propre), CUTOFF 110-180 Hz, RES 0-10 %, key track allumé, sortie `Direct`.
  - ENV 2 → CUTOFF : +1 à +2 octaves au pic, attaque 0, decay 40-80 ms, sustain 0.
- **ENV 1** : attaque 2 ms, release 70 ms.
- **Macros** : `Length` 30 → 120 ms · `Glide` 0 → 40 ms · `Weight` = CUTOFF 90 → 200 Hz · `Knock` = quantité d'ENV 2 → CUTOFF, de 0 à +2 octaves.
- **Jeu** : motif « Future House 126 » de `../motifs.md`, voix `sub`.
- **Test** :
  - avec le pluck ou le hollow au-dessus, le « toc » ne doit pas doubler leur attaque ; sinon `Knock` vers 0 ;
  - comparer à S04.
- **Origine** :
  - Rounded Rect, « entre sinus et carrée » [cartographie, § 3.7] ;
  - German LP, « passe-bas Zero-Delay Feedback (propre) » [cartographie, § 6] ;
  - réglages [ORIGINAL].

### S16 Sinus et clic de sample — Tech House, kick discret
- **Patch** :
  - SUB en Sine, PHASE 0 %, routé `Direct`.
  - OSC B en moteur Sample, avec un transitoire choisi par l'utilisateur (rimshot ou début de kick) de moins de 100 ms.
  - Pitch tracking d'OSC B coupé (clic droit sur l'étiquette) : il joue alors à hauteur fixe. OSC B routé `Main`.
  - Niveau d'OSC B 12-15 dB sous le sinus, mesuré au vumètre.
- **ENV 1** : attaque 2 ms, release 60 ms.
- **Macros** : `Length` 20 → 120 ms · `Glide` 0 → 100 ms · `Weight` = LEVEL d'OSC B de 0 à la borne mesurée · `Knock` —.
- **Jeu** : notes en contretemps ; le clic rend chaque note lisible entre les kicks.
- **Test** :
  - le clic ne doit pas se confondre avec le hat ou le clap ;
  - avec glide, la hauteur doit glisser pendant que le clic reste fixe.
- **Origine** :
  - couche de clic en Sample, transitoire de moins de 100 ms, keytracking off, 12-15 dB sous le sinus, glide intact [SOURCE F01-02] ;
  - Sample et pitch tracking [cartographie, § 3.1, 3.3].
- **Limite** : aucun sample n'est fourni ni supposé : le choix revient à l'utilisateur.

### S17 Triangle et Add Bass — Deep House, Garage
- **Patch** :
  - SUB en Triangle, PHASE 0 %, routé vers FILTER 1.
  - FILTER 1 en Add Bass, CUTOFF 80-120 Hz, VAR (THRU) 0-30 %, DRIVE 0-15, key track allumé, sortie `Direct`.
- **ENV 1** : attaque 3 ms, release 80 ms.
- **Macros** : `Length` 30 → 140 ms · `Glide` 0 → 60 ms · `Weight` = THRU 0 → 40 % · `Knock` —.
- **Jeu** : comme S01.
- **Test** :
  - Add Bass fait tourner la phase : mesurer la corrélation kick/sub avec `kick_bass_check.py` avant de garder ;
  - A/B à niveau égal avec S03.
- **Origine** : « passe-bas à rotation de phase + un peu de drive ; THRU ajoute le dry déphasé » [cartographie, § 6]. Usage sur un sub : [DÉDUCTION], jamais essayé.

### S18 Sub à chute de fin de phrase — variation avant une frontière de 8 mesures
- **Patch** : S01, avec une macro `Knock` en plus.
  - Matrice : MACRO 4 → CRS du SUB, réglée pour que 100 % donne −12 demi-tons (lire l'infobulle). La coarse du SUB est modulable dans Serum 2.
  - Dans Live, automatiser la macro de 0 à 100 % sur la dernière croche avant la frontière, puis la ramener à 0 sur le temps 1.
- **ENV 1** : attaque 3 ms, release 80 ms.
- **Macros** : `Length` 20 → 120 ms · `Glide` 0 → 60 ms · `Weight` — · `Knock` 0 → −12 st (de −5 à −24 selon le morceau).
- **Jeu** : une note tenue sur la dernière demi-mesure de la phrase.
- **Test** :
  - la chute doit finir avant le kick du temps 1 et la macro revenir à 0 avant la note suivante ;
  - alterner avec un autre geste à la frontière suivante (règle des drops d'`AGENTS.md`).
- **Origine** : CRS du SUB modulable [cartographie, § 3.7] ; geste [ORIGINAL] au service de la règle des drops.

### S19 Sub sensible à la vélocité — Tech House à notes fantômes
- **Patch** : S01, plus deux lignes de matrice :
  - Velocity → LEVEL du SUB, réglée pour qu'une vélocité de 60 donne environ −4 dB face à 127 ;
  - Velocity → DEC d'ENV 1, si cette destination accepte la modulation.
- **ENV 1** : attaque 2 ms, decay 300 ms, sustain −6 dB, release 40 ms.
- **Macros** : `Length` 20 → 100 ms · `Glide` — · `Weight` = profondeur Velocity → LEVEL, de 0 à 100 % · `Knock` —.
- **Jeu** : notes principales à 110-127, notes fantômes à 50-70, en doubles croches entre les kicks.
- **Test** :
  - les notes fantômes doivent s'entendre sans faire varier le niveau moyen de la ligne ;
  - contrôler le bus à faible volume.
- **Origine** : la vélocité est sans effet tant qu'elle n'a pas de destination [SOURCE F15-01, page EDMProd] ; réglages [ORIGINAL].

### S20 Sinus FM 1:1 — sub un peu chaud
- **Patch** :
  - OSC A sur Default, position 1 (sinus), PHASE 0 %, RAND 0, routé `Direct`.
  - WARP 1 d'OSC A en FM (Sub), quantité 5-15 %. Préférer le type Linear s'il est proposé : il garde la hauteur, selon le manuel.
  - SUB en Sine, réglé pour sonner exactement à l'unisson d'OSC A : vérifier à l'accordeur avec le niveau du SUB monté le temps du contrôle.
  - Puis LEVEL du SUB à 0, routage `None`. La source d'un warp doit rester allumée, son niveau peut être nul.
  - Rack FX inutile, la sortie étant `Direct`. Contre le continu (voir ci-dessous), un coupe-bas à 15-20 Hz sur la piste, par plug-in tiers.
- **ENV 1** : attaque 3 ms, release 60 ms.
- **Macros** : `Length` 20 → 120 ms · `Glide` 0 → 60 ms · `Weight` = quantité de FM 0 → 20 % · `Knock` —.
- **Jeu** : comme S01 ; utile sous un growl dont le haut est chargé.
- **Test** : à l'analyseur, la 2e harmonique doit monter avec `Weight`, et la fondamentale ne doit pas baisser de plus d'un décibel.
- **Calcul (rapport 1:1)** :
  - toute la série harmonique apparaît, et, à faible indice, surtout la 2e harmonique ;
  - J1(β) / J0(β) vaut −20 dB à β = 0,2 et −11,8 dB à β = 0,5 [CALCUL, Synth Secrets 12-13 dans `../documentation-basses.md`] ;
  - la bande inférieure tombe à 0 Hz : c'est une composante continue, d'où le coupe-bas ;
  - la correspondance entre le pourcentage du warp et β n'est pas documentée.
- **Origine** : source FM à niveau nul et routage `None` (`../families.md`, cartographie § 4.2) ; recette [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Kick supposé sur les quatre temps : aucune attaque ne tombe sur les doubles croches 1, 5, 9, 13. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/house-f01-sub.md`. La notation Producer Pal s'obtient avec `--fichier references/recettes/house-f01-sub.md --titre <titre> --format ppal`, et `--transposer N` donne la tonalité du Set. Les autres motifs (Bass House growl, wub, Future House) sont dans `../motifs.md`.

```grille
titre: Tech House 124 — sub en contretemps (S11, S16)
tempo: 124
accords: Fm7 | Fm7
sub: F0[1&:2] F0[2&:2] F0[3&:2] F0[4&:1] Ab0[4a:1] | F0[1&:2] F0[2&:2] Eb0[3&:2] C1[4&:2]
```

La durée écrite ne compte pas pour S11 : ENV 1 en BPM fixe la longueur. La dernière note (C1, 65,4 Hz) relance la boucle.

```grille
titre: Tech House 124 — sub roulant (S02, S19)
tempo: 124
accords: Fm7 | Fm7
sub: F0[1e:1] F0[1&:1] F0[1a:1] F0[2e:1] F0[2&:1] Ab0[2a:1] F0[3e:1] F0[3&:1] F0[3a:1] Eb0[4e:1] F0[4&:1] C1[4a:1] | F0[1e:1] F0[1&:1] F0[1a:1] F0[2e:1] F0[2&:1] F0[2a:1] Eb0[3e:1] Eb0[3&:1] F0[3a:1] Ab0[4e:1] C1[4&:1] Eb1[4a:1]
```

Pour S19, jouer les doubles croches « e » et « a » en notes fantômes (vélocité 50-70) et les « & » à 110-127. Dans Live, régler les vélocités note par note.

```grille
titre: Deep House 122 — sub lié avec glissés (S12)
tempo: 122
accords: Am7 | Fmaj7
sub: A0[1&:6] G0[3&:2] A0[4&:2] | F0[1&:6] E0[3&:2] C1[4&:2]
```

Le glissé vient de PORTA en ALWAYS : les notes ne se chevauchent pas. E0 (41,2 Hz) est la note la plus grave ; si le système ne la porte pas, transposer le bloc d'un ton vers le haut (`--transposer 2`).

```grille
titre: G-House 124 — 808 à glissés (S08, S09)
tempo: 124
accords: Fm7 | Fm7
sub808: F0[1&:3] F0[2a:1] F1[3&:2] Eb1[4&:1] C1[4a:1] | F0[1&:3] Ab0[2&:2] F0[3&:3] Eb0[4a:1]
```

Pour S08 avec LEGATO, chaque glissé se fait en allongeant dans Live la note de départ jusqu'à chevaucher la suivante : F0 → F1 dans la mesure 1, Ab0 → F0 dans la mesure 2. La grille garde les notes sans chevauchement pour le contrôle.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 les noms marqués « à retrouver » : table Analog_BD_Sin, mode Soft Sat., type Linear de la FM. Vérifier que chaque macro accepte sa destination.
- Écouter chaque recette avec le protocole des règles communes, puis garder trois à cinq subs pour le morceau.
- Consigner le preset retenu et ses macros dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
