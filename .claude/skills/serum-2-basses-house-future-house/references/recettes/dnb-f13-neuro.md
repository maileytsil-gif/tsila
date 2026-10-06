# Vingt recettes de neuro pour la Drum and Bass (famille F13)

Premier lot de recettes DnB : le neuro (neurofunk). C'est une basse médium dont le timbre change à l'intérieur de chaque note : position de table, FM ou distorsion de phase, filtres en encoche et distorsion, conduits par un ou deux LFO dessinés sur une ou deux mesures. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F13-01 DNB Academy, F13-02 et F13-03 Art1fact, F08-03 DNB Academy, F01-01 Art1fact ;
- `../etudes-pages-dubstep-dnb.md` : F13-11 Computer Music, F02-14 Future Music, F15-06 EDMProd ;
- la cartographie de Serum 2 (`../../../sound-designer-serum/references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes du lot DnB

Elles valent pour tous les fichiers `dnb-*.md`.

1. **Tempo et grille** : 174 BPM (« 165-175, 174 le plus courant » [SOURCE F15-06] ; F13-03 et F13-11 sont à 174).
   - Schéma de départ des grilles, en 2-step [DÉDUCTION] :
     - kick sur les doubles croches 1 et 11 (temps 1 et 3&) ;
     - caisse claire sur 5 et 13 (temps 2 et 4).
   - Le remplacer par le vrai break du morceau : la basse se réécrit autour de la batterie (`../tempo-mix.md`).
   - En half-time, la caisse claire passe sur le temps 3 seul (double croche 9).
   - Durées à 174 BPM [CALCUL] :
     - 1 mesure = 1 379,3 ms ; 8 mesures = 11,03 s ;
     - 1/2 = 689,7 ms ;
     - 1/4 = 344,8 ms ; 1/4 pointée = 517,2 ms ;
     - 1/8 = 172,4 ms ; 1/8 pointée = 258,6 ms ;
     - 1/8 triolet = 114,9 ms ;
     - 1/16 = 86,2 ms.
   - En fréquence : la noire vaut 2,90 Hz, la mesure 0,725 Hz.
2. **Sub séparé.** Les tutoriels mettent souvent le sub dans le patch :
   - routé dans le filtre « pour un grave plus concis » [SOURCE F02-01] ;
   - modulé en niveau par un LFO à −40 [SOURCE F13-11] ;
   - ou utilisé seulement comme modulateur FM [SOURCE F15-02].

   Ici, le grave est un sinus mono sur sa propre piste : S01 ou S02 (phase continue, pour les lignes roulantes) de `house-f01-sub.md`, recalé à 174 BPM. Le fichier de subs DnB viendra en fin de lot. Computer Music demande lui-même « un grave solide et constant » [SOURCE F13-11, conseil].
   - La basse médium est coupée vers 90-150 Hz selon la note et le kick ; il n'y a pas de valeur universelle (`../tempo-mix.md`).
3. **Tonalité et octave.**
   - Fa mineur est la tonalité la plus fréquente ; « les notes autour de F0 sonnent bien sur les systèmes club » [SOURCE F15-06]. F0 = MIDI 29 = 43,7 Hz.
   - Les grilles donnent les notes MIDI pour des oscillateurs médium à OCT 0. Les tutoriels jouent à OCT −2 ou −3 [SOURCE F13-01, F02-01, F08-03, F13-02, F14-01]. Si l'on garde leur réglage, transposer le clip de +24 ou +36 demi-tons (`grille.py --transposer 24`) : la note entendue reste celle de la grille.
4. **RAND à 0** sur chaque oscillateur, sauf mention contraire :
   - RAND baissé « pour tenir l'image stéréo » [SOURCE F13-01] ;
   - phase aléatoire désactivée « pour une attaque identique à chaque note » [SOURCE F13-11].

   Quand un tutoriel règle des phases différentes (F13-02), il les fixe ; elles ne sont pas aléatoires.
5. **MONO et LEGATO** sur la basse médium [SOURCE F02-01, F14-01, F15-02, F13-11].
6. **Mono puissant, stéréo après** : « garder le mono puissant dans le patch, ajouter la stéréo après » [SOURCE F13-02]. La distorsion va dans la bande haute d'un Splitter L/H, le grave reste propre [SOURCE F13-02, F01-01, F13-03].
7. **Resampling.**
   - « Impossible d'obtenir une basse à la Noisia directement du synthé, sans traitement ni resampling » [SOURCE F13-11, conseil].
   - Imprimer plusieurs prises et garder les meilleures [SOURCE F13-03, F02-14].
   - Procédure : `../../../resampling/SKILL.md`.
8. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
9. **Drops** : une variation de basse ou de batterie avant chaque frontière de huit mesures (règle d'`AGENTS.md`), voir NR20.
10. **Contrôle par l'utilisateur** :
    - la basse médium seule, puis avec le sub, puis avec le break (kick et caisse claire) ;
    - mono ;
    - plusieurs notes : la FM, les peignes et les encoches changent d'une note à l'autre (« ses résonances favorisent certaines notes » [SOURCE F14-01]) ;
    - les deux bornes de chaque macro ;
    - faible volume ;
    - A/B à niveau égal contre NR01.

## Règles propres au neuro

1. **Un LFO conduit tout.**
   - DNB Academy : un seul LFO dessiné sur 1 mesure, en RETRIG, va vers le bruit, la coupure, le drive et le creux d'EQ [SOURCE F13-01].
   - Art1fact : un triangle de 2 mesures en RETRIG sur deux encoches [SOURCE F13-02].
   - Computer Music : forme « Gunshot » de 2 mesures, redéclenchée [SOURCE F13-11].
2. **Le modulateur ne s'entend pas** : l'oscillateur qui module (FM ou PD) reste bas en niveau, et le filtre 1 ne traite que l'oscillateur porteur [SOURCE F13-01].
3. **Filtres caractéristiques** :
   - French LP avec sa seconde résonance BOEUF, puis Add Bass [SOURCE F13-01] ;
   - deux encoches en contre-mouvement [SOURCE F13-02] ;
   - filtre Reverb avant la distorsion [SOURCE F13-03] ;
   - Diffusor [SOURCE F08-03].
4. **Distorsion** :
   - Overdrive à plusieurs étages (« stacks ») [SOURCE F13-01, F13-03, F08-03] ;
   - Soft Clip en warp d'oscillateur [SOURCE F13-01] ou en fin de chaîne [SOURCE F08-03].
5. **Quatre macros communes** [ORIGINAL] :
   - `Motion` : macro en source AUX sur les lignes de LFO 1 de la matrice, ce qui règle la profondeur de tout le mouvement d'un geste ;
   - `FM` : quantité de FM ou de PD ;
   - `Notch` : fréquence de l'encoche ou du creux d'EQ ;
   - `Grit` : drive de l'Overdrive, avec MIX en sens inverse si le grain déborde.

   Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| NR01 | Neuro DNB Academy | référence | carrés −3, PD 50, French LP, un LFO d'une mesure |
| NR02 | Neuro FM croisée | neuro expressif | deux sinus, FM A↔B, deux encoches contraires |
| NR03 | Super Growler | neuro sale | carré, Overdrive à étages, filtre Reverb |
| NR04 | Neuro Computer Music | neuro glissé | WT 42, Gunshot 2 mesures, Mirror sur ENV lente |
| NR05 | Growl DnB DNB Academy | growl de drop | scie −3, PD, Rectify, Diffusor |
| NR06 | Neuro nu | apprentissage, intro | une scie, un sinus en PD, un LFO |
| NR07 | Neuro tenu | fin de phrase | LFO en ENVELOPE, notes de 1 à 2 mesures |
| NR08 | Neuro en rafale | rafales en doubles croches | ENV 1 courte, LFO 1/8 redéclenché |
| NR09 | Neuro parlant | neuro vocal | Formant-II balayé par un LFO Path |
| NR10 | Neuro métallique | neuro froid | FM inharmonique 1,41, Comb 2 |
| NR11 | Neuro à deux warps | neuro compact | PD puis Soft Clip sur le même oscillateur |
| NR12 | Neuro en marches | neuro mécanique | LFO en marches 1/16 sur la table |
| NR13 | Neuro à split mobile | neuro qui s'ouvre | fréquence du Splitter balayée de 200 à 650 Hz |
| NR14 | Neuro glissé à l'octave | lignes à glissés | portamento 250 ms, notes liées |
| NR15 | Neuro half-time | half-time | LFO de 2 mesures, notes longues |
| NR16 | Neuro large | refrain de drop | Bode et Hyper au-dessus du split |
| NR17 | Neuro à accent placé | réponse au kick | bosse étroite de LFO 2 sur Add Bass |
| NR18 | Neuro à trois LFO | longues tenues | trois vitesses, cycle de 3 mesures |
| NR19 | Neuro ressamplé | toutes | prises en LFO libre, découpe |
| NR20 | Neuro à vitesses enchaînées | variation avant la frontière | macro `Motion` et vitesse de LFO automatisées |

## Les vingt recettes

### NR01 Neuro DNB Academy — référence du fichier
- **Patch** :
  - **OSC A** : table Analog « square up and down » (nom incertain ; à défaut, une table de carrés du dossier Analog), OCT −3, RAND bas (0 ici), position « at top » (sens incertain).
  - **OSC B** : table Digital « JF flute » (nom incertain : un sinus légèrement distordu), OCT −2, LEVEL bas : il sert à la FM.
  - **Warp** : PD (B) sur A, à 50 %. Position de table d'un des deux oscillateurs à 54 (lequel n'est pas dit).
  - **Unison** : 2 voix, DETUNE baissé.
  - **Warp 2 de A** (oscillateur non dit, [DÉDUCTION]) : Distortion › Soft Clip, quantité modérée (« we don't really want to destroy the sound »).
  - **NOISE** : couleur White, STEREO, niveau sur LFO 1, passe-haut sur le bruit.
  - **FILTER 1** : routé sur A seul, type French LP, BOEUF et un peu de DRIVE, CUTOFF sur LFO 1 sans mouvement trop brusque.
  - **LFO 1** : forme dessinée avec de petits trous et de petits changements dans la mesure, 1 mesure, RETRIG.
  - **FILTER 2** : Add Bass, routé sur A et B, CUTOFF sur LFO 2 en unipolaire positif.
  - **LFO 2** : bosse étroite vers le milieu de la mesure, 1 mesure, RETRIG.
- **ENV 1** : non dite. Attaque 1 ms, sustain 100 %, release 30 ms [ORIGINAL].
- **FX** :
  1. Hyper/Dimension, un peu de DIMENSION.
  2. Distortion Overdrive, deux étages, LFO 1 → DRIVE.
  3. Chorus léger.
  4. Equalizer : encoche vers 300 Hz, Q élevé, LFO 1 → GAIN et → FREQ.
- **Macros** : `Motion` AUX des lignes de LFO 1 · `FM` quantité de PD 30 → 70 % · `Notch` FREQ de l'encoche 200 → 500 Hz · `Grit` DRIVE de l'Overdrive.
- **Sub associé** : S02, phase continue.
- **Jeu** : bloc « DnB 174 — neuro en appels » ci-dessous.
- **Test** : la position « at top », la table de A et la part de Soft Clip sont à lire à l'écran de la vidéo.
- **Origine** : [SOURCE F13-01, transcription seule, Serum 2]. Valeurs dites : OCT −3 et −2, PD 50, position 54, unison 2, Soft Clip, French LP, LFO d'une mesure en RETRIG, Overdrive à deux étages, encoche vers 300, Add Bass.

### NR02 Neuro FM croisée — « The Waiting Game »
- **Patch** :
  - **OSC A** et **OSC B** : sinus (Default Shapes), A à OCT −2, B à OCT −1, tous deux un peu désaccordés (FIN ≈ 31 sur A, lecture incertaine).
  - **Phases fixes** : ≈ 136° sur A, ≈ 232° sur B. La phase de départ cale le rythme du motif ; le désaccord règle sa vitesse.
  - **Warps doubles** : A en Diode 1 + FM (B) ≈ 20 % ; B en Tube + FM (A) ≈ 15 %. La FM croisée est une nouveauté de Serum 2 ; 21 % donne déjà un autre rythme.
  - **NOISE** : « Paper Bag », PITCH au maximum (bruit granuleux dans l'aigu).
  - **LFO 1** : triangle, RETRIG, 2 mesures.
  - **FILTER 1** : Notch 24 ou Peak 24 (lecture incertaine) dans le bas-médium, avec DRIVE, CUTOFF sur LFO 1.
  - **FILTER 2** : encoche sur une autre zone, CUTOFF sur LFO 1 en sens inverse, MIX baissé. Le contre-mouvement garde le médium plein.
- **Calcul du motif** : avec B une octave au-dessus de A, le motif de FM revient à la fréquence d'écart Δ = f(B) − 2·f(A). Sur la note F, avec B sur F2 (174,6 Hz), un désaccord de B de +7,2 cents donne un motif par mesure à 174 BPM (Δ = 0,725 Hz) ; +14,3 cents donnent deux motifs par mesure [CALCUL]. Comme pour un Reese, le motif accélère d'une octave à l'autre.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms [ORIGINAL].
- **FX** :
  1. Bode : BLUR monté, léger SHIFT, MIX ≈ 20 %.
  2. Hyper/Dimension discret.
  3. Chorus, passe-bas du chorus en mouvement, MIX ≤ 25 %.
  4. Splitter L/H : Overdrive dans la bande haute ; fréquence de séparation sur LFO 1, de ≈ 200 à ≈ 650 Hz (écran : 197 Hz).
  5. Delay ping-pong et Reverb ≈ 10 % chacun : juste une queue au relâchement.
- **Macros** : `Motion` AUX de LFO 1 · `FM` les deux quantités de FM ensemble, 10 → 25 % · `Notch` CUTOFF de FILTER 1 · `Grit` DRIVE de l'Overdrive de la bande haute.
- **Sub associé** : S01 ; les sinus de NR02 ne remplacent pas le sub.
- **Origine** : [SOURCE F13-02, Art1fact, transcription et trois captures, Serum 2]. Le calcul de Δ est une [DÉDUCTION] du principe dit à 0:11.

### NR03 Super Growler — un carré et des étages de distorsion
- **Patch** :
  - **OSC A** : Basic Shapes en position carrée, OCT −2 (lecture avec réserve), unison ≈ 3, DETUNE lent ; WARP Asym +.
  - **LFO 2** : décroissant, RETRIG, 1/4 → WT POS et forme.
  - **NOISE** : table dont le nom commence par « JKB HP… » (illisible ; à défaut, un bruit filtré passe-haut), bas, à travers la distorsion.
  - **FILTER 2** : type Reverb, avant la distorsion, LFO 3 (triangle, 1 mesure) ; un autre LFO baisse son MIX quand le son devient trop aigu.
  - **ENV 2** : attaque ≈ 296 ms (0,86 noire à 174 [CALCUL]), sustain 50 % → passe-bas qui s'ouvre et masque le clic du début.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms [ORIGINAL] ; ENV 1 → MIX et DRIVE de la distorsion contre le clic d'attaque [SOURCE].
- **FX**, dans l'ordre de l'écran :
  1. Distortion Overdrive, étages élevés : les timbres changent beaucoup d'un nombre d'étages à l'autre.
  2. Filter passe-bas sur LFO.
  3. Hyper/Dimension (préféré au Dimension seul).
  4. Filter Bandreject sur l'un des LFO.
  5. Splitter L/H : Convolve « Digital Gated » ≈ 30 % dans la bande haute pour adoucir ; Rectify essayé puis abandonné.
  6. Equalizer : légère bosse dans les médiums « pour l'expression ».
- **Macros** : `Motion` AUX de LFO 2 et LFO 3 · `FM` WARP Asym · `Notch` WIDTH du Bandreject · `Grit` nombre d'étages ou DRIVE de l'Overdrive.
- **Sub associé** : S01.
- **Origine** : [SOURCE F13-03, Art1fact, séance improvisée de 27 min, transcription et trois captures, Serum 2, 174 BPM].

### NR04 Neuro Computer Music — table, Gunshot et Mirror
- **Patch** :
  - **OSC A** : table `Basic_Mdc` (nom Serum 1, à retrouver dans Serum 2), WT POS 42.
  - **LFO 1** : forme `Gunshot` (Serum 1 ; à défaut, une chute rapide puis un plateau), 2 mesures, RETRIG → WT POS, quantité 55.
  - **Warp de A** : Mirror ; ENV 2 → warp, +100, attaque d'ENV 2 = 1,7 s.
  - MONO, PORTAMENTO 250 ms.
  - La source garde un SUB en Rounded Rect, LEVEL 100 %, LFO 1 → LEVEL du sub à −40. **Ici, SUB éteint** : le sub est sur sa piste (règle 2 du lot).
- **Calcul** : 1,7 s font 1,23 mesure à 174 BPM [CALCUL]. Une note d'une noire n'atteint que ≈ 20 % de la course du Mirror ; seules les tenues de plus d'une mesure l'atteignent en entier. Le timbre dépend donc de la longueur des notes.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 50 ms [ORIGINAL].
- **FX** : non donnés (« une autre étape », absente de la page). Proposé [ORIGINAL] : Overdrive dans la bande haute d'un Splitter L/H, puis Compressor Multiband.
- **Macros** : `Motion` quantité LFO 1 → WT POS, 30 → 70 · `FM` quantité de Mirror · `Notch` — · `Grit` DRIVE de l'Overdrive.
- **Sub associé** : S02.
- **Jeu** : bloc « DnB 174 — neuro glissé à l'octave » ; notes courtes une octave au-dessus des notes graves, reliées par le portamento [SOURCE].
- **Origine** : [SOURCE F13-11, page lue, Serum 1, 174 BPM]. Les noms `Basic_Mdc`, `Gunshot`, `RoundRect` et `Mirror` sont à vérifier dans Serum 2 ; Mirror existe dans la liste des warps de Serum 2 [cartographie, § 4].

### NR05 Growl DnB DNB Academy — PD, Rectify, Diffusor
- **Patch** : G05 de `house-f08-growl.md`, recalé pour la DnB :
  - **OSC A** : scie Default Shapes, OCT −3, WARP PD (B), quantité ≈ 35 sous LFO.
  - **OSC B** : Basic Shapes position 3 (triangle à l'écran), unison 3, WARP Distortion Rectify au maximum.
  - **NOISE** : White, STEREO 67.
  - **FILTER 1** : Diffusor, CUTOFF 118, STAGES « 72-75 » (dit « 7275 », lecture incertaine).
  - **LFO** (forme non décrite) sur la PD, l'oscillateur scie et le bruit.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms [ORIGINAL].
- **FX** :
  1. Distortion Overdrive agressive.
  2. Chorus en mode passe-haut, pour la largeur.
  3. Filter Combs, coupure presque au maximum.
  4. Equalizer : creux à 437 Hz, Q 60, −17,6 dB.
  5. Filter Phs 36+, coupure ≈ 57, LFO bipolaire.
  6. Splitter : Convolve sur la bande haute, IR « L90 PLATE - DRUM - TIGHT PLATE ».
  7. Compressor Multiband : −18,1 dB, 4:1, attaque et release 90,1, gain 7,2, X-Low 128.
  8. Filter MG Low 6, LFO 1 sur la coupure.
  9. Distortion Soft Clip en fin de chaîne.
- **Macros** : `Motion` AUX du LFO · `FM` quantité de PD · `Notch` FREQ du creux 437 Hz · `Grit` DRIVE de l'Overdrive.
- **Sub associé** : S01.
- **Origine** : [SOURCE F08-03, transcription et quatre captures, Serum 2, format vertical].

### NR06 Neuro nu — une scie, un sinus, un LFO
- **Patch** :
  - **OSC A** : scie, OCT 0, RAND 0, WARP PD (B) à 40 %.
  - **OSC B** : sinus, OCT 0, LEVEL 0.
  - **FILTER 1** : MG Low 24 routé sur A, CUTOFF 600 Hz, RES 20 %.
  - **LFO 1** : forme dessinée en deux bosses (temps 1 et temps 3), 1 mesure, RETRIG → quantité de PD (+40) et → CUTOFF (+30).
- **ENV 1** : attaque 1 ms, sustain 100 %, release 30 ms.
- **FX** : Splitter L/H à 250 Hz, Overdrive deux étages dans la bande haute.
- **Macros** : `Motion` AUX de LFO 1 · `FM` quantité de PD 0 → 80 % · `Notch` CUTOFF 300 → 1 500 Hz · `Grit` DRIVE.
- **Sub associé** : S01.
- **Test** : écouter le mouvement seul, sans distorsion, puis ajouter l'Overdrive.
- **Origine** : NR01 réduit à ses trois gestes (PD, un LFO d'une mesure en RETRIG, distorsion au-dessus du split) [ORIGINAL] ; split [SOURCE F13-02].

### NR07 Neuro tenu — la variante de fin de phrase
- **Patch** : NR01 dupliqué, puis :
  - LFO 1 en mode ENVELOPE, 2 mesures, sans point de bouclage : le geste se joue une fois par note ;
  - LFO 2 désactivé ;
  - encoche de l'EQ fixe, sans LFO.
- **ENV 1** : attaque 3 ms, sustain 100 %, release 150 ms.
- **Macros** : celles de NR01.
- **Sub associé** : S02.
- **Jeu** : tenues d'une à deux mesures sur la tonique, en fin de phrase de 8.
- **Origine** : mode ENVELOPE des LFO [cartographie, § 7] ; variante [ORIGINAL].

### NR08 Neuro en rafale — doubles croches redéclenchées
- **Patch** :
  - NR01 ou NR06, avec LFO 1 à 1/8, RETRIG : chaque note de 86 ms ne joue que la première moitié du geste (1/8 = 172 ms) [CALCUL].
  - **ENV 1** : attaque 0,5 ms, decay 120 ms, sustain −∞, release 20 ms : chaque note s'éteint seule.
- **FX** : comme la recette de départ ; Compressor Multiband plus serré.
- **Macros** : `Motion` · `FM` · `Notch` · `Grit` de la recette de départ.
- **Sub associé** : S01 en notes longues, jamais en rafale (bloc ci-dessous).
- **Jeu** : bloc « DnB 174 — neuro en rafale » ci-dessous.
- **Origine** : rafales de doubles croches des basses « machine gun » [SOURCE F11-01, Dubstep, transposé] ; recette [ORIGINAL].

### NR09 Neuro parlant — formant balayé
- **Patch** :
  - **OSC A** : NR06, PD (B) à 40 %.
  - **FILTER 1** : Formant-II, CUTOFF qui morphe entre les voyelles, FORMNT au centre.
  - **LFO 1** : type Path, 1 mesure, RETRIG : la sortie X → CUTOFF du formant, la sortie Y → FORMNT. Un tracé en boucle donne une suite de voyelles.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Overdrive dans la bande haute d'un Splitter L/H à 200 Hz ; EQ en creux à 300 Hz.
- **Macros** : `Motion` AUX de LFO 1 · `FM` quantité de PD · `Notch` FORMNT · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** : formants et voyelles du growl (`house-f08-growl.md`, `dubstep-f09-yoi.md`) ; LFO Path à deux sorties [cartographie, § 7] ; recette [ORIGINAL].

### NR10 Neuro métallique — FM inharmonique
- **Patch** :
  - **OSC A** : sinus, OCT 0, WARP FM (B).
  - **OSC B** : sinus en mode Ratio (clic droit sur OCT), rapport 1,41, LEVEL 0.
  - **FILTER 1** : Comb 2 routé sur A, FRQ2 à l'oreille.
  - **LFO 1** : rampe descendante, 1 mesure, RETRIG → quantité de FM (+50).
- **Calcul** : 1,41 ≈ √2, soit 595 cents au-dessus de la porteuse. Les composantes fc ± n·fm ne tombent plus sur les harmoniques de la note : le son devient métallique [CALCUL].
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Lin. Fold à faible DRIVE ; Splitter L/H à 250 Hz ; Compressor Multiband.
- **Macros** : `Motion` AUX de LFO 1 · `FM` quantité de FM 10 → 60 % · `Notch` FRQ2 du Comb 2 · `Grit` DRIVE du Lin. Fold.
- **Sub associé** : S01, indispensable : la FM inharmonique ne porte aucune fondamentale stable.
- **Test** : plusieurs notes ; le Comb 2 favorise certaines notes [SOURCE F14-01].
- **Origine** : rapports FM de `dubstep-f11-tearout-metal.md` ; mode Ratio [cartographie, § 3.1] ; recette [ORIGINAL].

### NR11 Neuro à deux warps — PD puis Soft Clip
- **Patch** :
  - **OSC A** : carré Basic Shapes, OCT 0, WARP 1 PD (B) 50 %, WARP 2 Distortion Soft Clip 40 %.
  - **OSC B** : sinus, OCT +1, LEVEL 0.
  - **LFO 1** : 1 mesure, RETRIG → WARP 1 (+30) et → WARP 2 (+20).
  - **FILTER 1** : French LP sur A, BOEUF à mi-course.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 30 ms.
- **FX** : Overdrive deux étages dans la bande haute d'un Splitter L/H à 220 Hz ; EQ en creux à 300 Hz.
- **Macros** : `Motion` AUX de LFO 1 · `FM` WARP 1 · `Notch` FREQ du creux · `Grit` WARP 2.
- **Sub associé** : S01.
- **Origine** : PD 50 et Soft Clip [SOURCE F13-01] ; warps doubles de Serum 2 [SOURCE F13-02 ; cartographie, § 3.1] ; réunion des deux dans un oscillateur [ORIGINAL].

### NR12 Neuro en marches — table en doubles croches
- **Patch** :
  - NR06, avec une table riche (Analog, carrés ou Basic Shapes).
  - **LFO 2** : marches en doubles croches (grille du LFO, Shift-clic), 1 mesure, RETRIG → WT POS (+100) : seize positions par mesure, une tous les 86 ms [CALCUL].
  - LFO 1 garde la PD et la coupure.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 30 ms.
- **Macros** : `Motion` AUX de LFO 2 · `FM` quantité de PD · `Notch` CUTOFF · `Grit` DRIVE.
- **Sub associé** : S01.
- **Test** : un léger SMOOTH sur le LFO si les marches cliquent.
- **Origine** : « moduler position de table ou quantité de FM par LFO ou step sequencer » [SOURCE F13-11, conseil] ; marches de LFO [cartographie, § 7] ; recette [ORIGINAL].

### NR13 Neuro à split mobile — la distorsion qui descend
- **Patch** : NR06 ou NR01, avec :
  - un Splitter L/H, Overdrive dans la bande haute seulement ;
  - LFO 1 → fréquence de séparation, de ≈ 200 à ≈ 650 Hz.
- **Calcul** : 650/200 = 3,25, soit 1,7 octave de course [CALCUL]. Quand la séparation descend, plus de médium passe dans l'Overdrive.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Motion` AUX de LFO 1 · `FM` · `Notch` borne haute de la séparation · `Grit` DRIVE de l'Overdrive.
- **Sub associé** : S01.
- **Origine** : [SOURCE F13-02, écran « Split Freq 197 Hz » modulé par LFO 1].

### NR14 Neuro glissé à l'octave — notes liées
- **Patch** : NR04 ou NR06, avec MONO, LEGATO, PORTAMENTO 250 ms, ALWAYS décoché : seules les notes qui se chevauchent glissent.
- **Calcul** : 250 ms font 2,9 doubles croches à 174 BPM [CALCUL] : un glissé dure presque toute une note de trois doubles croches.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **Macros** : celles de la recette de départ ; `Motion` peut piloter PORTA (150 → 300 ms) à la place.
- **Sub associé** : S02, **sans glissé** : le sub joue les notes graves seulement.
- **Jeu** : bloc « DnB 174 — neuro glissé à l'octave » ci-dessous ; les chevauchements d'un quart de double croche déclenchent les glissés.
- **Origine** : notes courtes une octave au-dessus des notes graves, reliées par portamento, 250 ms [SOURCE F13-11].

### NR15 Neuro half-time — mouvement sur deux mesures
- **Patch** : NR01, avec LFO 1 et LFO 2 sur 2 mesures.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 80 ms.
- **Jeu** : caisse claire sur le temps 3 ; une note par demi-mesure, la seconde décalée d'une double croche après la caisse claire.
- **Macros** : celles de NR01.
- **Sub associé** : S01.
- **Origine** : half-time DnB annoncé par F13-18 (cours non lu) ; recette [ORIGINAL].

### NR16 Neuro large — la stéréo au-dessus du split
- **Patch** : NR01 ou NR02, puis, dans la bande haute d'un Splitter L/H à 200 Hz :
  - Bode, BLUR monté, SHIFT faible, MIX 20 % ;
  - Hyper/Dimension discret.

  La bande basse reste mono et sans effet de largeur.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ ; `Grit` → MIX du Bode (0 → 30 %).
- **Sub associé** : S01.
- **Test** : en mono, le niveau ne doit pas chuter.
- **Origine** : « le Bode = toute la stéréo » et « mono puissant, stéréo après » [SOURCE F13-02].

### NR17 Neuro à accent placé — une bosse de filtre dans la mesure
- **Patch** : NR01, avec la bosse de LFO 2 placée à la double croche 12, soit 11/16 de la mesure (juste après le kick du 3&, juste avant la caisse claire du 4) → CUTOFF d'Add Bass.
- **Calcul** : 11/16 de 1 379 ms = 948 ms après le début de la note, si la note part sur le temps 1 [CALCUL]. Une note qui part ailleurs déplace l'accent : RETRIG le cale sur la note, pas sur la mesure.
- **ENV 1** : comme NR01.
- **Macros** : celles de NR01.
- **Sub associé** : S02.
- **Test** : choisir la place de la bosse avec le vrai break.
- **Origine** : « another hit of a filter that comes in in the right spot » [SOURCE F13-01] ; placement [ORIGINAL].

### NR18 Neuro à trois LFO — mouvements qui convergent
- **Patch** : NR06, avec :
  - LFO 1 : 1/4, RETRIG → WT POS ;
  - LFO 2 : 1/8 pointée, RETRIG → quantité de PD ;
  - LFO 3 : 1 mesure, triangle, RETRIG → CUTOFF.
- **Calcul** : 4, 3 et 16 doubles croches ont pour plus petit multiple commun 48 doubles croches, soit 3 mesures [CALCUL]. Le motif complet ne revient qu'au bout de 3 mesures ; une note plus courte n'en joue que le début.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 60 ms.
- **Macros** : `Motion` AUX des trois LFO · `FM` · `Notch` · `Grit` de NR06.
- **Sub associé** : S01.
- **Jeu** : tenues longues ; sur un drop haché, garder NR01.
- **Origine** : « la convergence des trois mouvements crée de nouvelles dynamiques » [SOURCE F13-03] ; vitesses [ORIGINAL].

### NR19 Neuro ressamplé — prises en LFO libre
- **Patch** :
  1. Construire NR01, NR02 ou NR03, avec LFO 1 en mode FREE : chaque note reçoit une modulation différente.
  2. Imprimer deux à quatre minutes d'un riff, effets compris.
  3. Découper les meilleures prises ; les remettre dans un Simpler ou dans un oscillateur (Resample to).
  4. S'arrêter après 2 ou 3 passes.
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01, jamais ressamplé avec la basse médium.
- **Origine** :
  - LFO en mode libre, « imprimer plusieurs minutes d'un riff et découper les meilleures prises » [SOURCE F02-14] ;
  - « chaque relance donne un mouvement différent : enregistrer plusieurs prises » [SOURCE F13-03] ;
  - procédure : `../../../resampling/SKILL.md`.

### NR20 Neuro à vitesses enchaînées — variation avant la frontière
- **Patch** : NR01 ou NR06. Dans Live, sur la phrase de 8 mesures (11,03 s) :
  - RATE de LFO 1 : 1 mesure pendant 6 mesures ;
  - 1/2 en mesure 7 ;
  - 1/8 sur la première moitié de la mesure 8 ;
  - silence sur la seconde moitié ;
  - macro `Motion` montée sur les mesures 7 et 8.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01, coupé sur la demi-mesure de silence.
- **Jeu** : la seconde mesure du bloc « DnB 174 — neuro en rafale » montre la coupure.
- **Test** : en mode HOST, le LFO saute pour rester calé sur la mesure quand la division change ; écouter si ce saut gêne.
- **Origine** : RD20 de `dubstep-f10-riddim.md` recalé à 174 ; règle des drops d'`AGENTS.md` ; comportement de HOST [cartographie, § 7.2] ; séquence [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60), notes pour des oscillateurs médium à OCT 0 (règle 3 du lot). DnB à 174 BPM : kick sur les doubles croches 1 et 11, caisse claire sur 5 et 13. Aucune attaque de basse sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dnb-f13-neuro.md`.

```grille
titre: DnB 174 — neuro en appels (NR01, NR02, NR05)
tempo: 174
accords: Fm7 | Fm7
neuro: F1[1:3] F1[1a:1] Ab1[2e:2] F1[3:2] F1[3&:2] C2[4e:2] Eb2[4a:1] | F1[1:3] F1[1a:1] Ab1[2e:2] Bb1[3:2] Ab1[3&:2] F1[4e:3]
sub: F0[1:4] Ab0[2e:3] F0[3:4] C1[4e:3] | F0[1:4] Ab0[2e:3] Bb0[3:2] Ab0[3&:2] F0[4e:3]
```

La basse répond juste après chaque caisse claire (doubles croches 6 et 14). Le si bémol de la mesure 2 est une note de passage vers le la bémol. Les tenues du sub recouvrent le kick du 3& : ducking ou sidechain réglé sur les vrais coups de kick (`../tempo-mix.md`).

```grille
titre: DnB 174 — neuro glissé à l'octave (NR04, NR14)
tempo: 174
accords: Fm7 | Fm7
neuro: F1[1:2.25] F2[1&:1.25] F1[1a:1] Eb1[2e:2.25] Eb2[2a:1] C1[3:2.25] C2[3&:1.25] Eb2[3a:3] | F1[1:2.25] F2[1&:1.25] F1[1a:1] Ab1[2e:2.25] Ab2[2a:1] C2[3:2.25] Bb1[3&:1.25] Ab1[3a:1] F1[4e:3]
sub: F0[1:4] Eb0[2e:3] C1[3:3] Eb0[3a:3] | F0[1:4] Ab0[2e:3] C1[3:2] Bb0[3&:1] Ab0[3a:1] F0[4e:3]
```

Un quart de double croche de chevauchement (21,6 ms) entre deux notes liées déclenche le glissé en LEGATO ; une note détachée repart sans glissé. Le sub ne glisse pas. Le si bémol de la mesure 2 est une note de passage.

```grille
titre: DnB 174 — neuro en rafale et coupure de fin de phrase (NR08, NR20)
tempo: 174
accords: Fm7 | Fm7
neuro: F1[1:1] F1[1e:1] F1[1&:1] Ab1[1a:1] F1[2e:1] F1[2&:1] C2[2a:1] F1[3:1] F1[3e:1] F1[3&:1] Eb2[3a:1] F1[4e:1] F1[4&:1] Ab1[4a:1] | F1[1:1] F1[1e:1] F1[1&:1] Ab1[1a:1] C2[2e:1] Eb2[2&:1] F2[2a:1]
sub: F0[1:4] Ab0[2e:3] F0[3:4] F0[4e:3] | F0[1:4] Ab0[2e:3]
```

Rafale de doubles croches avec un trou sur chaque caisse claire. La seconde mesure monte en arpège (Ab1, C2, Eb2, F2) et s'arrête au temps 3 : c'est la demi-mesure de silence de NR20, à placer en mesure 8 de la phrase.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « square up and down », « JF flute », `Basic_Mdc`, le bruit « Paper Bag » et le bruit « JKB HP… » ;
  - la forme de LFO `Gunshot` ;
  - l'IR « L90 PLATE - DRUM - TIGHT PLATE » et « Digital Gated » ;
  - les filtres Notch 24 / Peak 24, Diffusor, Comb 2, Add Bass, French LP.

  Vérifier les destinations des macros et la source AUX de `Motion`.
- Remplacer le schéma de batterie des grilles par le vrai break et recaler les notes.
- Écouter chaque recette avec le sub et le break, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
