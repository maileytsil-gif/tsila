# Vingt recettes de riddim pour le Dubstep (famille F10)

Premier lot de recettes Dubstep : le riddim, une basse minimale et répétitive. Une table carrée ou vocale y est mise en mouvement, note après note, par des LFO redéclenchés, un filtre en peigne et des OTT empilés. Rédigé le 05/10/2026. Sources :
- `../etudes-videos.md` : F10-01 Konstricta et F10-02 ECKA, les deux études riddim ; pour les gestes voisins, F11-01, F08-01 et F08-02 ;
- `../etudes-pages-dubstep-dnb.md` et `../etudes-captures.md` : F08-04 Monosounds, F01-08 EDMProd ;
- la cartographie de Serum 2 (`../../../../references/serum2-cartographie.md`).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Étiquettes de `house-f01-sub.md` : [SOURCE …], [EXTRAIT …], [CALCUL], [DÉDUCTION], [ORIGINAL].

## Règles communes du lot Dubstep

Elles valent pour tous les fichiers `dubstep-*.md`.

1. **Tempo et grille** : 140 BPM (plage 140-150), joué en half-time. Kick sur le temps 1, caisse claire sur le temps 3 (double croche 9) ; le kick peut se déplacer en 2-step [SOURCE F01-08 : « kick en two-step, clap sur chaque 3e temps »].
   - Durées à 140 BPM [CALCUL] :
     - 1 mesure = 1 714,3 ms ;
     - 1/2 = 857,1 ms ;
     - 1/4 = 428,6 ms ;
     - 1/8 = 214,3 ms ;
     - 1/8 triolet = 142,9 ms ;
     - 1/16 = 107,1 ms.
   - À 150 BPM, une noire dure 400,0 ms.
2. **Sub séparé.** La « Main Sub » des tutoriels porte souvent FM, distorsion et peigne : ce n'est pas un sub pur [SOURCE F01-08, limites].
   - Ici, le grave est un sinus sur sa piste : S01 ou S10 de `house-f01-sub.md`, recalé à 140 BPM. Le fichier de subs Dubstep viendra en fin de lot.
   - La basse médium est coupée vers 100-150 Hz.
3. **Hauteur** : les tutoriels jouent la basse médium à OCT −3, autour de Fa0-Sol0 joués. Garder ce réglage si la note sonne au-dessus du passe-haut ; sinon remonter d'une octave et laisser le grave au sub.
4. **RAND à 0** sur chaque oscillateur : chaque note redémarre pareil [SOURCE F10-01, F08-02].
5. **Effets après Serum** : plug-ins tiers seulement (règle 6 d'`ableton-live-session`).
6. **Contrôle par l'utilisateur** :
   - la basse médium seule, puis avec le sub, puis avec le kick et la caisse claire ;
   - mono ;
   - les deux bornes de chaque macro ;
   - faible volume ;
   - A/B à niveau égal contre la recette de référence du fichier.

## Règles propres au riddim

1. **Le mouvement vient de LFO redéclenchés** (RETRIG ou ENVELOPE) sur WT POS et sur LEVEL, à 1/4 ou 1/2 : chaque note répète le même geste [SOURCE F10-01, F10-02].
2. **Le peigne est « le plus important »** : Filter FX en Cmb HL6−, coupure ≈ 110 Hz, LFO sur la coupure [SOURCE F10-01].
3. **OTT empilés**, gain jusqu'à ce que « ça frappe en restant propre » [SOURCE F10-01].
4. **Quatre macros communes**, d'après les noms des macros d'ECKA [SOURCE F10-02] :
   - `Index` : WT POS de la table principale ;
   - `Rate` : RATE du LFO principal ; ECKA la règle « pour garder une pulsation à la noire » ;
   - `Comb` : coupure du peigne ;
   - `Grit` : drive avec MIX en sens inverse.

   Vérifier le « + » sur chaque destination.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| RD01 | Riddim Konstricta | référence | Dying Square + Vowel, peigne, OTT ×3 |
| RD02 | Riddim tenu | sustain, fin de drop | LFO plats, sans bouclage |
| RD03 | Riddim ECKA | riddim carré | Sync, Hyper statique, Overdrive ×2 |
| RD04 | ECKA à trois tables | riddim texturé | FM (C), macros Index C et Texture C |
| RD05 | Riddim nu | apprentissage, intro | carré, un LFO sur niveau et position |
| RD06 | Riddim à boucle | variation de drop | LFO Envelope à point de bouclage |
| RD07 | Riddim en rafale | gun riddim | ENV 1 courte, rythme MIDI |
| RD08 | Riddim bancal | wonky | Main Tuning et swing du LFO |
| RD09 | Riddim au peigne seul | trench | Cmb HL6− balayé sur 1 mesure |
| RD10 | Riddim vocal | riddim parlant | table Vowel + formant |
| RD11 | Riddim large figé | refrain de drop | Hyper/Dimension RATE 0 |
| RD12 | Riddim sync | riddim brillant | warp Sync redéclenché |
| RD13 | Riddim en triolets | rebond | LFO 1/4 triolet |
| RD14 | Riddim haché | stutter | coupures en croches |
| RD15 | Riddim mâché | half-time chew | LFO 1/2 sur le warp |
| RD16 | Riddim OTT ×3 | drop dense | trois Multiband à gain mesuré |
| RD17 | Riddim au baffle vocal | largeur | Convolve « wide vox » |
| RD18 | Riddim robot | robotique | Quantize et RM |
| RD19 | Riddim ressamplé | toutes | 2-3 passes |
| RD20 | Riddim à vitesses enchaînées | variation avant frontière | macro `Rate` automatisée |

## Les vingt recettes

### RD01 Riddim Konstricta — référence du fichier
- **Patch** :
  - **OSC A** : table Serum 2 « Dying Square », OCT −3, RAND 0, WT POS ≈ 100.
  - **LFO 1** : bosse arrondie, RETRIG, 1/4 → WT POS d'A (≈ 7 %) et → LEVEL d'A (niveau de base un peu baissé).
  - **OSC B** : table de la catégorie Vowel (écran : « OOH_YAH_00 », lecture approximative), OCT −3, RAND 0.
  - **LFO 2** : plusieurs points, 1/2, mode ENVELOPE avec un point de bouclage au milieu (joue le début, puis boucle) → WT POS de B et → warp de B (Asym +). LFO 1 → LEVEL de B.
  - **NOISE** : allumé, LEVEL sur LFO 1, routé `Direct`.
  - **FILTER 1** : passe-haut simple sur A et B, coupure légèrement modulée par LFO 1.
  - **LFO 3** : 1/2, ENVELOPE avec point de bouclage au milieu → Global › Main Tuning, ≈ 10 %, bipolaire.
- **ENV 1** : non dite. Attaque 1 ms, sustain 100 %, release 40 ms [ORIGINAL].
- **FX** :
  1. Convolve, catégorie Short, IR « … WIDE VOX », MIX sur LFO 1 (élargissement).
  2. Distortion Diode 2, DRIVE au maximum, MIX sur LFO 1 (≈ 70 %).
  3. Filter Cmb HL6−, CUTOFF ≈ 110 Hz, LFO 2 → CUTOFF ≈ 30 %, RES, HL WID à l'oreille.
  4. LFO 4 (1 mesure, déclenché en fin de séquence) → CUTOFF du peigne ≈ 12 %.
  5. Trois Compressor Multiband (OTT) empilés, gain jusqu'à ce que ça frappe en restant propre.
  6. Equalizer final, un peu d'aigus.
- **Macros** : `Index` WT POS d'A 80 → 140 · `Rate` RATE de LFO 1, 1/4 → 1/8 · `Comb` CUTOFF du peigne 80 → 200 Hz · `Grit` DRIVE de la Diode 2.
- **Sub associé** : S01. Le NOISE en `Direct` échappe au passe-haut : le garder léger ou le filtrer par sa couleur.
- **Jeu** : bloc « Dubstep 140 — riddim en noires » ci-dessous.
- **Origine** :
  - [SOURCE F10-01, transcription et trois captures, Serum 2] ;
  - riddim façon « Square 4 » (Infekt, Samplifire, MVRDA) sans la table d'origine.

### RD02 Riddim tenu — la variante sustain
- **Patch** : RD01 dupliqué, puis :
  - LFO 1 plat en haut, en mode ENVELOPE ;
  - LFO 2 sans point de bouclage, 1/4 ;
  - LFO 3 sans point de bouclage, 1/4 ;
  - LFO 4 désactivé ou adouci.
- **ENV 1** : attaque 2 ms, sustain 100 %, release 120 ms.
- **Macros** : celles de RD01.
- **Sub associé** : S01.
- **Jeu** : bloc « Dubstep 140 — riddim tenu » ci-dessous, pour la fin d'un drop ou une réponse longue.
- **Origine** : variante sustain dite à 7:37 [SOURCE F10-01].

### RD03 Riddim ECKA — Sync, Hyper statique, Overdrive ×2
- **Patch** :
  - **OSC A** : table Digital « Dying Square », WT POS ≈ 120, Unison 2, WARP en Sync.
  - **LFO 1** : pic puis descente exponentielle, RETRIG, 1/4 → WT POS d'A, avec des variations ajoutées dans la forme.
  - **MACRO 1** « Rate » sur le RATE de LFO 1, réglée pour garder une pulsation à la noire. **MACRO 2** « Index A » sur WT POS d'A, aussi par la matrice.
  - **OSC B** : scie (Default Shapes ; la voix dit « triangle »).
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms [ORIGINAL].
- **FX** :
  1. Hyper/Dimension : RATE 0, SIZE ≈ 65, MIX ≈ 65.
  2. Distortion Overdrive, deux étages.
  3. Equalizer : bande basse en coupe-bas ou shelf à 180 Hz, Q 46, gain 2,5 ; bande haute à 2 041 Hz, Q 60, +2,5.
  4. Compressor Multiband : −11,6 dB, 4:1, attaque 0,1, release 0,1, gain 3,1 dB, bandes à 128 et 2 500 Hz.
  5. Reverb Vintage : LO CUT 0, HI CUT 35, RATE 25, DEPTH 20.
- **Macros** : `Index` = MACRO 2 · `Rate` = MACRO 1 · `Comb` — · `Grit` DRIVE des deux Overdrive.
- **Sub associé** : S01.
- **Origine** : [SOURCE F10-02, transcription et quatre captures, Serum 2, petite chaîne].

### RD04 ECKA à trois tables — FM depuis C
- **Patch** : RD03, plus OSC C.
  - OSC C sur une table utilisateur. ECKA offre sa « frog table » (WT POS 116) par lien externe ; à défaut, une table Spectral d'usine.
  - WARP de A en FM (C).
  - MACRO 3 « Index C » sur WT POS de C, MACRO 4 « Texture C » sur la quantité de FM.
- **ENV 1** : comme RD03.
- **Macros** : `Index` WT POS d'A · `Rate` · `Comb` → « Index C » · `Grit` → « Texture C ». Les quatre macros d'ECKA remplacent ici les noms communs.
- **Sub associé** : S01.
- **Origine** : partie optionnelle dite à 5:58 [SOURCE F10-02]. La table d'ECKA n'est pas téléchargée.

### RD05 Riddim nu — un carré, un LFO
- **Patch** :
  - OSC A sur Dying Square (ou la frame carrée de Basic Shapes), OCT −3, RAND 0.
  - LFO 1 en bosse arrondie, RETRIG, 1/4 → LEVEL d'A (de 0 au maximum) et → WT POS (+7 %).
  - Rien d'autre que le passe-haut à 120 Hz.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 30 ms.
- **FX** : Distortion Diode 2, DRIVE 50 ; un Compressor Multiband.
- **Macros** : `Index` WT POS · `Rate` RATE de LFO 1 · `Comb` — · `Grit` DRIVE.
- **Sub associé** : S01.
- **Test** : ce patch sert à entendre le geste de base. Ajouter ensuite B, le peigne et les OTT un par un, en A/B à niveau égal.
- **Origine** : geste commun à F10-01 et F10-02 (carré Dying Square, LFO redéclenché à 1/4 sur WT POS et LEVEL) [SOURCE] ; réduction [ORIGINAL].

### RD06 Riddim à boucle — le point de loopback
- **Patch** :
  - RD05, avec LFO 1 en mode ENVELOPE, RATE 1/2, et un point de bouclage à la moitié de la forme (clic droit sur un point › Set Loopback Point Here).
  - Première moitié : une attaque en deux bosses. Seconde moitié : une bosse simple qui boucle tant que la note tient.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **Macros** : celles de RD05.
- **Sub associé** : S01.
- **Jeu** : notes de longueurs différentes (une noire, une blanche, une mesure). Chaque note commence pareil et se prolonge en boucle.
- **Origine** :
  - LFO en Envelope avec point de bouclage au milieu [SOURCE F10-01] ;
  - mode ENVELOPE et loopback [cartographie, § 7.2] ;
  - formes [ORIGINAL].

### RD07 Riddim en rafale — l'enveloppe fait le rythme
- **Patch** :
  - RD05, avec ENV 1 : attaque ≈ 0,5 ms, hold 0, decay 116 ms, sustain −∞, release 52 ms.
  - Le rythme se dessine avec les notes MIDI, pas avec un LFO.
  - FILTER 1 en Combs sur A, CUTOFF ≈ 425 Hz, RES ≈ 98, DRIVE au fond, DAMP monté.
- **FX** :
  1. Distortion Tube, MIX 50 %.
  2. Filter Combs, RES haute.
  3. Delay court (LINK, BPM désactivé, ≈ 12,9 ms), MIX monté.
  4. Compressor Multiband.
- **Macros** : `Index` WT POS · `Rate` decay d'ENV 1 60 → 200 ms · `Comb` CUTOFF du Combs · `Grit` DRIVE.
- **Sub associé** : aucun ou S11 (court).
- **Jeu** : doubles croches en rafale, par groupes de 3 à 6.
- **Origine** : « le machine gun vient de l'ENV 1, pas d'un LFO », valeurs à l'écran [SOURCE F11-01, Serum 1].

### RD08 Riddim bancal — Main Tuning et swing
- **Patch** : RD01 ou RD05, puis :
  - LFO 3 → Global › Main Tuning, bipolaire, 10-15 %, 1/2, ENVELOPE avec point de bouclage ;
  - LFO 1 avec le swing activé : en BPM, clic droit sur RATE › Swing. Il suit le swing global du clavier de Serum.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Rate` · `Index` · `Comb` · `Grit` comme la recette de départ, plus la profondeur de Main Tuning sur `Grit` si une macro manque.
- **Sub associé** : S01, sur sa piste. Main Tuning ne bouge que ce patch.
- **Test** : la hauteur qui bouge doit rester musicale contre le sub. Si elle paraît fausse, réduire à 5 %.
- **Origine** :
  - LFO 3 → Main Tuning ≈ 10 %, bipolaire [SOURCE F10-01] ;
  - swing du LFO [cartographie, § 7.2] ;
  - « wonky » [ORIGINAL] : le tutoriel F10-05 n'est pas étudié.

### RD09 Riddim au peigne seul — trench
- **Patch** :
  - OSC A sur Dying Square, OCT −3, RAND 0, sans LFO sur le niveau (note tenue pleine).
  - Rack FX : Distortion Diode 2, DRIVE au maximum, puis Filter Cmb HL6−, CUTOFF ≈ 110 Hz, RES 50-70 %, HL WID à l'oreille.
  - LFO 2 (1/4, RETRIG) → CUTOFF du peigne ≈ 30 %. LFO 4 (1 mesure) → CUTOFF ≈ 12 %.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : trois Compressor Multiband, puis passe-haut à 120 Hz.
- **Macros** : `Index` WT POS · `Rate` RATE de LFO 2 · `Comb` CUTOFF du peigne · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** : peigne « le plus important », Cmb HL6−, coupure ≈ 110 Hz, LFO 2 30 %, LFO 4 12 % [SOURCE F10-01] ; réduction au peigne seul [ORIGINAL].

### RD10 Riddim vocal — table Vowel et formant
- **Patch** :
  - OSC A sur une table de la catégorie Vowel (« OOH_YAH_00 » dans F10-01), OCT −3, RAND 0.
  - LFO 1 (bosse, RETRIG, 1/4) → WT POS ≈ 15 % et → LEVEL.
  - FILTER 1 en Formant-II, RES 25 %. LFO 2 (1/8, faible) → CUTOFF.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Diode 2, Compressor Multiband, passe-haut à 120 Hz.
- **Macros** : `Index` WT POS · `Rate` RATE de LFO 1 · `Comb` CUTOFF du formant · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - table Vowel de F10-01 [SOURCE] ;
  - 1/4 « steady syllables » sur le formant, 1/8 « fast stutter » à faible profondeur [SOURCE F08-04, infographie] ;
  - assemblage [ORIGINAL].

### RD11 Riddim large figé — Hyper RATE 0
- **Patch** :
  - RD03 sans Reverb. Hyper/Dimension en premier : RATE 0 (pas de mouvement de chorus), UNISON 3-5, SIZE ≈ 65, MIX ≈ 65.
  - Utility en fin de chaîne : MONO BASS allumé, FREQ 150 Hz.
- **ENV 1** : comme RD03.
- **Macros** : `Grit` MIX de l'Hyper · les autres comme RD03.
- **Sub associé** : S01.
- **Test** : en mono, le riddim ne doit pas perdre son attaque ni changer de timbre de façon marquée.
- **Origine** :
  - Hyper/Dimension RATE 0, taille ≈ 65, MIX ≈ 65 [SOURCE F10-02] ;
  - Utility MONO BASS [cartographie, § 8].

### RD12 Riddim sync — harmoniques qui balaient
- **Patch** :
  - OSC A sur Dying Square, OCT −3, RAND 0. WARP 1 en Sync.
  - LFO 1 (pic puis descente exponentielle, RETRIG, 1/4) → quantité de Sync +40 % et → WT POS.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Overdrive ×2, Compressor Multiband, passe-haut à 120 Hz.
- **Macros** : `Index` WT POS · `Rate` RATE de LFO 1 · `Comb` quantité de Sync · `Grit` DRIVE.
- **Sub associé** : S01.
- **Origine** :
  - warp Sync sur A et LFO en pic puis descente exponentielle [SOURCE F10-02] ;
  - LFO vers le warp [ORIGINAL].

### RD13 Riddim en triolets — rebond
- **Patch** : RD05, avec LFO 1 en 1/4 avec TRIP (285,7 ms à 140 BPM) au lieu de 1/4 [CALCUL].
- **ENV 1** : comme RD05.
- **Macros** : `Rate` 1/4T → 1/8T · les autres comme RD05.
- **Sub associé** : S01.
- **Jeu** : notes tenues d'une blanche : trois rebonds par blanche contre la caisse claire du temps 3.
- **Origine** : « 1/4 triplet : the yoi-yoi bounce » [SOURCE F08-04, infographie] ; application au riddim [ORIGINAL].

### RD14 Riddim haché — stutter en croches
- **Patch** : RD05, plus LFO 2 en marches (Shift-clic, grille 8) → LEVEL d'A, quantité −100.
  - LFO 2 : 1 mesure, RETRIG, coupures sur certaines croches.
  - SMOOTH 5-10 contre les clics.
- **ENV 1** : comme RD05.
- **Macros** : `Rate` RATE de LFO 2 · `Grit` quantité de LFO 2 → LEVEL · les autres comme RD05.
- **Sub associé** : S10, recalé à 140 BPM.
- **Jeu** : bloc « Dubstep 140 — riddim haché » ci-dessous, ou une note tenue d'une mesure découpée par le LFO.
- **Origine** : outils de dessin et SMOOTH [cartographie, § 7.2] ; geste [ORIGINAL].

### RD15 Riddim mâché — LFO 1/2 sur le warp
- **Patch** :
  - RD05, avec WARP 1 en Bend − ou Asym +.
  - LFO 2 en 1/2, RETRIG, forme en marches courbes → quantité du warp, +30 à +50 %.
- **ENV 1** : comme RD05.
- **Macros** : `Rate` RATE de LFO 2 · `Comb` quantité du warp · les autres comme RD05.
- **Sub associé** : S01.
- **Origine** :
  - « 1/2 : classic half-time chew », sur le Warp amount [SOURCE F08-04, infographie] ;
  - Bend − et Asym + utilisés en riddim et en growl [SOURCE F10-01, F08-02].

### RD16 Riddim OTT ×3 — drop dense
- **Patch** : RD01 ou RD09, avec trois Compressor en Multiband (BELOW actif, effet OTT) :
  1. −18,1 dB, 4:1, attaque 90,1, release 90,1, gain 6-9 dB, bandes à 120 et 2 500 Hz ;
  2. et 3. mêmes réglages, gain réduit de 3 dB chacun.
  - Equalizer après les OTT : passe-haut à 120 Hz, −3 dB vers 3-5 kHz.
- **ENV 1** : comme la recette de départ.
- **Macros** : `Grit` gain du premier OTT 0 → 12 dB · les autres comme la recette de départ.
- **Sub associé** : S01.
- **Test** : A/B à niveau égal, avec et sans les OTT. Les OTT font monter le niveau ; sans compensation, on préfère toujours le plus fort.
- **Origine** :
  - trois OTT empilés [SOURCE F10-01, F08-01, F08-02] ;
  - réglages −18,1 dB, 4:1, 90,1 / 90,1, gain 9,5-13,2, lus sur les captures de F05-02, F06-01 et F08-01 [SOURCE, écran].

### RD17 Riddim au baffle vocal — Convolve « wide vox »
- **Patch** : RD05, plus un Convolve en premier dans les FX : catégorie Short, IR « … WIDE VOX », SIZE réduite, MIX sur LFO 1 (de 0 au maximum).
- **ENV 1** : comme RD05.
- **FX** : Convolve, Distortion Diode 2, Compressor Multiband, passe-haut à 150 Hz (une IR ajoute du grave).
- **Macros** : `Grit` MIX du Convolve · les autres comme RD05.
- **Sub associé** : S01.
- **Test** : en mono, l'élargissement ne doit pas creuser le médium.
- **Origine** :
  - Convolve, catégorie Short, IR « wide vocal », MIX sur LFO 1 [SOURCE F10-01] ;
  - une IR peut ajouter trop de grave [SOURCE F07-02].

### RD18 Riddim robot — Quantize et RM
- **Patch** :
  - OSC A sur Dying Square, OCT −3, RAND 0.
  - WARP 1 en Quantize, 20-50 % : réduction de résolution sur la forme, dont l'aliasing suit la hauteur.
  - WARP 2 en RM (B), avec B en sinus à Ratio 1.5, LEVEL 0.
  - LFO 1 (1/4, RETRIG) → Quantize et → RM.
- **ENV 1** : attaque 1 ms, sustain 100 %, release 40 ms.
- **FX** : Distortion Hard Clip légère, Compressor Multiband, passe-haut à 120 Hz.
- **Macros** : `Index` WT POS · `Rate` RATE de LFO 1 · `Comb` quantité de RM · `Grit` quantité de Quantize.
- **Sub associé** : S01.
- **Origine** :
  - Quantize « façon sample-and-hold sur la forme, l'aliasing suit la hauteur » [cartographie, § 4.1] ;
  - RM « creux, inharmonique, radio » [SOURCE F03-04] ;
  - recette [ORIGINAL]. Le tutoriel « robo riddim » du registre (F10-12) n'est pas étudié.

### RD19 Riddim ressamplé — deux ou trois passes
- **Patch** :
  1. Construire RD01 ou RD03.
  2. Imprimer une note tenue de 2 à 4 mesures, effets compris.
  3. La remettre dans un oscillateur (glisser le WAV ou Resample to).
  4. Nouvelle passe : autre warp, autre forme et autre vitesse de LFO.
  5. S'arrêter après 2 ou 3 passes.
- **Macros** : celles de la dernière passe.
- **Sub associé** : S01, jamais ressamplé avec le riddim.
- **Origine** : boucle de resampling, « more passes add mud, not character » [SOURCE F08-04, infographie] ; procédure : `../../../resampling/GUIDE.md`.

### RD20 Riddim à vitesses enchaînées — variation avant la frontière
- **Patch** : RD01 ou RD03, avec la macro `Rate` automatisée dans Live sur la phrase de 8 mesures :
  - 1/4 pendant 6 mesures ;
  - 1/8 en mesure 7 ;
  - 1/16 sur la première moitié de la mesure 8 ;
  - silence sur la seconde moitié.
- **ENV 1** : comme la recette de départ.
- **Macros** : celles de la recette de départ.
- **Sub associé** : S01, coupé sur la demi-mesure de silence.
- **Test** : avec HOST, le LFO saute pour rester calé sur la mesure quand la division change ; écouter si ce saut gêne.
- **Origine** :
  - macro « Rate » d'ECKA [SOURCE F10-02] ;
  - silence et variation avant chaque frontière de huit mesures (règle des drops d'`AGENTS.md`) ;
  - comportement de HOST [cartographie, § 7.2] ;
  - séquence [ORIGINAL].

## Motifs vérifiés

Numérotation de Live (C3 = 60). Dubstep à 140 BPM en half-time : kick sur la double croche 1, caisse claire sur la double croche 9 (temps 3). Aucune attaque de basse sur la caisse claire. Vérification, depuis le dossier du skill : `python3 ../../../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/recettes/dubstep-f10-riddim.md`.

```grille
titre: Dubstep 140 — riddim en noires (RD01, RD03, RD05)
tempo: 140
accords: Fm7 | Fm7
riddim: F1[1:3] F1[2:3] F1[3e:2] F1[4:3] | F1[1:3] F1[2:3] Ab1[3e:2] Eb1[4:3]
sub: F0[1:3] F0[2:3] F0[3e:2] F0[4:3] | F0[1:3] F0[2:3] Ab0[3e:2] Eb0[4:3]
```

Chaque note dure trois doubles croches (321,4 ms) : un cycle de LFO 1 à 1/4 (428,6 ms) n'a pas le temps de finir. Comparer avec des noires pleines (quatre doubles croches) [CALCUL]. La note du temps 3 est décalée d'une double croche pour laisser passer la caisse claire.

```grille
titre: Dubstep 140 — riddim tenu (RD02, RD06)
tempo: 140
accords: Fm7 | Fm7
riddim: F1[1:8] Ab1[3e:7] | F1[1:6] C2[2a:2] Eb2[3e:3] F1[4&:2]
sub: F0[1:8] Ab0[3e:7] | F0[1:6] C1[2a:2] Eb1[3e:3] F0[4&:2]
```

Tenues d'une demi-mesure : la boucle d'ENVELOPE de RD06 se répète sur la fin de chaque note.

```grille
titre: Dubstep 140 — riddim haché (RD14, RD20)
tempo: 140
accords: Gm7 | Gm7
riddim: G1[1:2] G1[1&:2] G1[2:2] G1[3e:1] G1[3&:2] Bb1[4:2] G1[4&:2] | G1[1:2] G1[1&:2] F1[2:2] D2[3e:1] C2[3&:2] Bb1[4:2] G1[4&:2]
sub: G0[1:4] G0[2:4] G0[3e:3] Bb0[4:2] G0[4&:2] | G0[1:4] F0[2:4] D1[3e:3] Bb0[4:2] G0[4&:2]
```

Croches répétées, avec un trou sur la caisse claire. Le do de la mesure 2 est une note de passage vers le si bémol.

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 :
  - les tables « Dying Square » et « OOH_YAH_00 » (catégorie Vowel) ;
  - l'IR « … WIDE VOX » ;
  - le filtre Cmb HL6− ;
  - le point de bouclage des LFO en ENVELOPE ;
  - le swing des LFO.

  Vérifier les destinations des macros.
- Écouter chaque recette avec le sub, le kick et la caisse claire, et en garder trois à cinq. Consigner le preset retenu dans la mémoire du projet (`../../../../../producteur-live/modules/memoire-projet/GUIDE.md`).
