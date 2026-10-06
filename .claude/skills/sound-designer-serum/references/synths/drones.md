# Vingt recettes de drones et d'atmosphères dans Serum 2

Sixième et dernier fichier du lot de synthés : drones, textures évolutives, atmosphères de breakdown, risers de suspense. Rédigé le 06/10/2026. Sources :
- l'étude des quinze tutoriels de drones, DR-01 à DR-15, de `../tutoriels-synths-serum.md`, et sa synthèse `../synths-serum-synthese.md` (section Drone) ;
- les trois patchs de nappes et les points de départ de `../leads-nappes-textures.md` (§ 3 et § 5, textures) ;
- la cartographie de Serum 2 (`../serum2-cartographie.md`) : moteurs Sample, Granular et Spectral (§ 3.3 à § 3.6), bruits de couleur (§ 3.7), Splitter M/S (§ 8), LFO (§ 7.2).

**Rien de ce fichier n'a été entendu** (règle 4 d'`AGENTS.md`). Les tutoriels ont été lus sur transcription, son coupé, sans capture d'écran. Étiquettes, comme dans `leads.md` : **[SOURCE DR-nn]**, **[FICHE]**, **[CALCUL]**, **[DÉDUCTION]**, **[ORIGINAL]** ; [ASR ?] signale une transcription douteuse.

**Beaucoup de fiches sources donnent peu de valeurs chiffrées** (DR-01, DR-05, DR-07, DR-13 surtout). Les recettes correspondantes disent ce qui vient de la vidéo et ce qui est proposé ici. Sept vidéos sont en Serum 2 (DR-04, DR-06 à DR-12) ; les autres sont en Serum 1 et sont traduites (règle 3 de `leads.md`).

## Règles

Les dix règles communes au lot sont dans `leads.md`. Ce qui s'ajoute pour les drones :

1. **High Pass à 80-120 Hz.** Un drone d'atmosphère ne descend pas dans le grave : le sub et la basse médium sont dans leurs instruments (règle « Grave » d'`AGENTS.md`). Plusieurs tutoriels coupent beaucoup moins bas (DR-01 laisse LO CUT à 0, DR-02 coupe à 35 Hz) : ici, Equalizer en High Pass à **100 Hz** par défaut, 80 Hz pour les drones sombres de DnB (DN09, DN12), 120 Hz pour les textures de bruit. Deux recettes (DN06, DN15) jouent dans le grave par nature : elles tiennent le médium grave (≥ 80 Hz) et laissent le sub à une recette de `../../../serum-2-basses-house-future-house/references/recettes/`.
2. **Trois échelles de temps** [FICHE] : un mouvement rapide (grain, quelques Hz), un lent (respiration, 1 à 4 mesures), un très lent (8 à 32 mesures, ou une enveloppe de 12 à 19 s). Une recette en a deux ou trois ; chacune dit lesquelles.
3. **Tempos de référence** [CALCUL] : à 122 BPM, une mesure dure 1,97 s, 4 mesures 7,87 s, 8 mesures 15,7 s ; à 124 BPM, 1,94 s, 7,74 s, 15,5 s ; à 140 BPM, 1,71 s, 6,86 s, 13,7 s, et 32 mesures 54,9 s ; à 174 BPM, 1,38 s, 5,52 s, 11,0 s, et 32 mesures 44,1 s.
4. **La reverb est souvent le son** : en insert à MIX élevé, elle appartient au patch et sera resamplée avec lui ; sur un retour à 10-30 %, elle appartient au mix [FICHE]. Chaque fiche dit lequel. ValhallaVintageVerb (inventaire) pour une reverb externe, sur un retour.
5. **Largeur et mono** : les drones sont larges ; pour garder le grave propre, **Splitter M/S** avec un Equalizer en High Pass sur la voie SIDE (DR-04, DR-08), ou Ozone Imager 2 en dessous de 180 Hz [SOURCE PA-02 pour la valeur]. Vérifier en mono.
6. **Resampling** : plusieurs drones sont imprimés puis rechargés dans un moteur Sample, Granular ou Spectral (DR-10, DR-11, DR-14). Capture dans Live : `../../../resampling/SKILL.md` ; dans Serum, l'icône d'onde à gauche du logo exporte la dernière note jouée (cartographie § 2.3).
7. **Droits** : les tutoriels utilisent des samples de packs tiers (DR-08, DR-09, DR-10, DR-14) ; n'utiliser qu'un sample dont la licence est vérifiée, ou un son d'usine de Serum, ou ta propre prise (règle 8 de `leads.md`).
8. **Transition avant une frontière de huit mesures** : le cutoff automatisé en montée est le geste le plus simple (DR-05, DR-06) ; chaque fiche indique la macro à utiliser (règle « Drops » d'`AGENTS.md`).
9. **Notes** : C3 = 60 dans Live ; le numéro MIDI fait foi. MIDI 41 = F1 (87,3 Hz), MIDI 53 = F2 (174,6 Hz), MIDI 65 = F3 (349,2 Hz) [CALCUL].
10. **Référence A/B du fichier** : DN01.

## Tableau de choix

| Id | Recette | Usage | Geste |
| --- | --- | --- | --- |
| DN01 | Texture de bruit seul | Melodic house, intro et breakdown, référence A/B | NOISE filtré et résonant, LFO dessiné de 2 mesures, reverb de 8 s |
| DN02 | Atmo afro en gouttes | Afro house, breakdown | FM B → A, LFO en escalier sur le niveau, LFO qui module les LFO |
| DN03 | Drone analogique à Bend lent | Melodic house | deux tables analogiques, Bend modulé, LFO de 8 mesures sur le niveau de B |
| DN04 | Atmosphère cinématique | Melodic techno, breakdown | FM depuis le Sub muet, trois LFO jusqu'à 32 mesures, Splitter M/S |
| DN05 | Pad de bruit arpégé | Melodic techno, tension avant le drop | une note tenue, ARP de Serum en aléatoire, vélocité vers cutoff et pan |
| DN06 | Drone grave médium | Progressive, intro et breakdown | saws, MG Low 24 résonant, LFO retrig, OSC C et NOISE vers BUS 1 |
| DN07 | Drone à évolution imprévisible | Deep, minimal, longs morceaux | LFO aléatoires sur chaque mouvement, LFO qui module le rate d'un LFO |
| DN08 | Drone spectral figé | Deep, minimal | deux samples en Spectral Manual, Detune, Spread, Gate, crackle |
| DN09 | Drone sombre de samples | DnB sombre, intro | sample à −2 octaves, convolution « Long », couches, notches |
| DN10 | Accord de sinus resamplé | DnB, atmosphère d'intro | sinus sur trois oscillateurs, bounce, Granular en chaos |
| DN11 | Atmosphère rêveuse en Fm7 | DnB liquide, atmosphérique | Bottle Blow, noise en FM, S&H sur FIN, resampling Spectral Manual |
| DN12 | Pad sombre neuro | DnB neuro, hard | saws, Vocal Hum, filtre drivé, LFO de 2 mesures, Vintage |
| DN13 | Fond minimal | Deep dubstep, intro de 8 à 32 mesures | init désaccordée, filtre, un peu de bruit, reverb |
| DN14 | Drone de piano resynthétisé | Melodic dubstep, breakdown | piano en reverb de 30 s chargé en sample, ATK 19 s, Main Tuning à 8 mesures |
| DN15 | Drone FM inharmonique | Intro sombre, dubstep, DnB | sinus en FM à rapport non entier, deux octaves, notch qui balade |
| DN16 | Riser de suspense | DnB sombre, intro | filtre qui s'ouvre sur 8 mesures, Multiband sur les aigus |
| DN17 | Drone à notches aléatoires | DnB sombre, deep | Notch modulé par un LFO S&H, drone tonal |
| DN18 | Drone de bruit coloré | Textures, transitions | Pink, Brown ou Geiger, COLOR et STEREO |
| DN19 | Fond doux sous 124 | Signature sous 124, électro chill | sinus et triangle, bruit rose très bas, reverb de 5 s |
| DN20 | Drone devenu pad jouable | Tous genres | une macro fait passer l'attaque de 19 s à 300 ms |

## Les vingt recettes

### DN01 Texture de bruit seul — référence du fichier
- **Patch** [SOURCE DR-01, Serum 1, transcription automatique] :
  - **Seul l'oscillateur NOISE est actif** ; OSC A éteint. NOISE à **50 %**, un échantillon de goutte d'eau (« Soar Electricity » [ASR ? « store electricity »]), PITCH **18** (unité non dite), suivi de hauteur actif (interprétation).
  - FILTER 1 actif (type non dit), NOISE routé dedans ; CUTOFF, RES et DRIVE à « 20 20 20 » [ASR ?], lus comme CUTOFF, RES et DRIVE à 20 (interprétation).
  - ENV 1 : ATK et REL **1,27** (secondes, interprétation). ENV → RES.
  - LFO 1 dessiné à la main, RATE **2 mesures**, → CUTOFF et RES.
- **Dans Serum 2** : le NOISE sort par défaut vers MAIN. Page MIX, NOISE vers FILTER 1 (interrupteur N du module, cartographie § 5 et § 6). Si le NOISE reste en MAIN, le filtre ne fait rien.
- **Valeurs de départ** [ORIGINAL] : FILTER 1 Band 12, CUTOFF 1,2 kHz, RES 45 %, DRIVE 20 ; ENV 1 1,27 s / 0 / 2 s / 0 dB / 1,27 s ; ENV 2 800 ms / 0 / 3 s / 40 % / 1,5 s → RES 20 % ; LFO 1 en 2 bar, FREE, forme sinueuse dessinée → CUTOFF 30 % et RES 15 %.
- **Durée** [CALCUL] : à 122 BPM, 2 mesures = 3,93 s ; la reverb de 8 s dure 4 mesures.
- **FX** [SOURCE DR-01] : Chorus MIX **15 %** → Delay MIX **≈ 43 %** → Reverb MIX **50 %**, DECAY **8 s**, HI CUT 0, LO CUT 0 ; Equalizer éteint dans la vidéo. **Ici** : Equalizer en High Pass à **120 Hz** après la reverb (règle 1), la vidéo laissant le grave de la reverb ouvert.
- **Reverb** : en insert, elle fait la texture (règle 4).
- **Macros** : `Tone` CUTOFF 0,5 → 3 kHz · `Motion` LFO 1 → CUTOFF et RES 0 → 60 % · `Dirt` DRIVE 0 → 50 · `Space` MIX de la Reverb 20 → 70 %.
- **Jeu** : notes tenues deux à huit mesures, MIDI 55 à 79 ; le suivi de hauteur du NOISE transpose la texture.
- **Test** : sans hauteur nette, vérifier que le bruit ne se bat pas avec les hats dans les aigus ; un High Pass de la reverb à 300 Hz si besoin.

### DN02 Atmo afro en gouttes
- **Patch** [SOURCE DR-02, noté Serum 1 mais cite un « LFO bus » [ASR ?] : version à vérifier] :
  - OSC A : table « Dist Sub » [ASR « disc sub dis »], LEVEL très bas. OSC B : table « Cream » [ASR], LEVEL un peu bas ; UNISON un peu monté, DETUNE baissé, WT POS un peu montée.
  - OSC A, WARP 1 **FM (B)** puis augmenté ; WARP 2 « Symmetry Plus » [ASR] (probablement **Asym +**), « un tout petit peu ».
  - NOISE « Attacks › Misc › Glass Lid 5 » [ASR ?], suivi de hauteur, PITCH et LEVEL montés.
  - SUB sinus, LEVEL 0, +1 octave : modulateur muet.
  - FILTER 1 **MG Low 12** [ASR « mg12 »] sur A et B, CUTOFF un peu baissé, DRIVE monté ; ENV 2 → CUTOFF.
  - ENV 2 → **FM (B)** (agressif), ATK un peu montée, SUS plus bas, REL montée.
- **Mouvements** [SOURCE DR-02] :
  - LFO 1 triangle, **2 mesures**, BPM désactivé et HOST désactivé (« anchor off ») → DETUNE de B (peu) et PAN du NOISE (bipolaire).
  - LFO 2 et LFO 3 **en escalier**, RETRIG, **1/4**.
  - LFO 4 en rampe montante, **4 mesures**, qui module LFO 2 et LFO 3.
  - LFO 2 → LEVEL (pas à 100 %), LFO 3 → LEVEL : de « petits plucks », les gouttes.
- **LFO 4 dans Serum 2** : en assignant LFO 4 au RATE de LFO 2 et de LFO 3 (matrice), ou par un **bus de LFO** (modulation des points, cartographie § 7.2) si l'on veut déformer l'escalier lui-même.
- **Durées** [CALCUL] : à 122 BPM, 1/4 = 491,8 ms, 2 mesures = 3,93 s, 4 mesures = 7,87 s.
- **ENV 1** : ATK très montée avec courbe, SUS un peu baissé, DEC baissé, REL montée [SOURCE DR-02] ; ici 1,5 s / 0 / 1 s / −8 dB / 2,5 s.
- **FX** [SOURCE DR-02] :
  1. Reverb : LO CUT monté, SPIN et DEPTH baissés, MIX monté.
  2. Delay **1/8 et 1/8 pointée**, FEEDBACK baissé, FREQ beaucoup montée, Q baissé, MIX **++**.
  3. Equalizer : coupe-bas ≈ **35 Hz** dans la vidéo, **100 Hz ici** (règle 1), High Shelf monté.
  4. Filter **MG Low 12** modulé par ENV 2.
  5. Compressor **Single**, seuil baissé, **3:1**, attaque et release courts, gain monté ; Chorus, MIX faible.
- **Delay** [CALCUL] : à 122 BPM, 1/8 = 245,9 ms et 1/8 pointée = 368,9 ms.
- **Macros** : `Tone` CUTOFF 20 → 70 % · `Motion` ENV 2 → FM (B) 0 → 40 % · `Dirt` DRIVE du filtre 0 → 50 · `Space` MIX du Delay 20 → 60 %.
- **Jeu** : une note ou deux tenues quatre à huit mesures, MIDI 60 à 76 ; le preset s'appelle « Raindrops » dans la vidéo.
- **Test** : les gouttes ne doivent pas tomber en même temps que les attaques des percussions ; décaler la phase de LFO 3.

### DN03 Drone analogique à Bend lent
- **Patch** [SOURCE DR-03, Serum 1] :
  - FILTER 1 actif, A et B routés dedans (type non dit).
  - OSC A : **+1 octave**, table Analog « BD Sine » [ASR « analog bd sign »], WT POS **≈ 130** ; UNISON **4**, DETUNE **≈ 0,08** ; WARP 1 **Bend +/−**, modulé par un LFO de **≈ 4 mesures** (dit « enveloppe » [ASR ?]).
  - OSC B : table Analog « 4088 » [ASR « 4040 4088 »], WT POS **≈ 214**.
  - LFO 1 → CUTOFF, RATE **1/16** ; ENV 1 → CUTOFF aussi.
  - LFO 3 → LEVEL de B, RATE **8 mesures**.
- **ENV 1** : REL **≈ 2,40 s** [SOURCE DR-03] ; ici 1,2 s / 0 / 2 s / −3 dB / 2,4 s.
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 30 %, ENV 1 → CUTOFF 25 % ; LFO 1 → CUTOFF 10 % ; LFO 2 (Bend) en 4 bar, triangle, ±30 % ; LFO 3 en 8 bar, FREE, sinus, → LEVEL de B 40 %.
- **Durées** [CALCUL] : à 122 BPM, 1/16 = 123 ms (8,1 Hz), 4 mesures = 7,87 s, 8 mesures = 15,7 s.
- **FX** [SOURCE DR-03] : Delay MIX **≈ 38 %**, Ping-Pong → Reverb MIX **≈ 50 %**, DECAY **≈ 8 s**, HI CUT 0 → Equalizer, coupe des basses : le bas est coupé pour laisser la place à un autre pad. Ici, High Pass à 100 Hz.
- **Macros** : `Tone` CUTOFF 15 → 60 % · `Motion` LFO Bend 0 → 60 % · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Reverb 20 → 60 %.
- **Jeu** : une note tenue longtemps, MIDI 53 à 65 ; préparer la place d'un pad qui joue au-dessus.
- **Test** : les trois vitesses sont 8,1 Hz (grain), 7,87 s (Bend) et 15,7 s (niveau de B) ; couper chacune pour en entendre l'apport.

### DN04 Atmosphère cinématique
- **Patch** [SOURCE DR-04, Serum 2] :
  - OSC A : scie par défaut, UNISON un peu monté, DETUNE très baissé, LEVEL baissé, FIN un peu baissé. OSC B : scie, UNISON **4** [ASR ?], DETUNE monté, FIN monté (stéréo), LEVEL très bas.
  - OSC A et B : filtre **passe-haut par oscillateur** (WARP de type Filter › HPF, cartographie § 4.2). Pas de warp sur B.
  - OSC A, WARP 1 **FM (Sub)** : le SUB est une **scie à LEVEL 0**, il ne sert que de modulateur ; sa FM est d'abord à fond en bas, puis modulée.
  - LFO 1 en mode **ENVELOPE**, **2 mesures**, triangle → FM (Sub).
  - ENV 1 : ATK très haute vers une macro (« M2 » [interprétation]), REL montée. ENV 1 → RATE d'un LFO.
  - FILTER 1 sur A et B, CUTOFF baissé. Filtre d'oscillateur **MG Low 18** en fin de vidéo.
  - LFO 2 : **4 mesures**, RETRIG, SMOOTH (devient un sinus) → CUTOFF.
  - LFO 3 : **32 mesures**, **RISE 2 mesures**, **DELAY 1 mesure**, SMOOTH → CUTOFF ; la forme est redessinée.
  - VOICING **MONO**, un peu de PORTA.
- **Durées** [CALCUL] : à 124 BPM, 2 mesures = 3,87 s ; 4 mesures = 7,74 s ; 32 mesures = 61,9 s ; RISE 2 mesures = 3,87 s ; DELAY 1 mesure = 1,94 s.
- **ENV 1** : 2 s / 0 / 3 s / −3 dB / 3 s [ORIGINAL pour les durées].
- **FX** [SOURCE DR-04] :
  1. Hyper/Dimension : MIX d'Hyper « tout en bas », Dimension MIX baissé.
  2. Equalizer : coupe-bas, Peak en coupe (la boue).
  3. Compressor **Single** : seuil très bas, attaque et release plus courts, gain monté.
  4. Reverb **Hall** : LO CUT monté, SIZE montée, DECAY très long, MIX **++**, SPIN DEPTH monté.
  5. Distortion **Tube**, DRIVE haut, MIX baissé.
  6. Delay **Ping-Pong 1/4**, FEEDBACK monté, FREQ montée, Q baissé, MIX **++**.
  7. **Splitter M/S** → Equalizer sur la voie SIDE, coupe-bas **≈ 32** [ASR ?] ; ici 150 Hz sur le SIDE, High Pass à 100 Hz sur la somme.
- **Delay** [CALCUL] : à 124 BPM, 1/4 = 483,9 ms.
- **Macros** : `Tone` CUTOFF 10 → 60 % · `Motion` LFO 1 → FM (Sub) 0 → 50 % · `Dirt` DRIVE du Tube 10 → 60 · `Space` MIX du Delay 20 → 70 %.
- **Jeu** : une note tenue tout le breakdown, MIDI 53 à 65 ; la vidéo le met avant un drop de melodic house ou de techno.
- **Test** : le LFO 3 de 62 s dépasse la durée d'un breakdown de 16 mesures (31 s) : il n'y fait que sa première moitié.

### DN05 Pad de bruit arpégé
- **Patch** [SOURCE DR-05, Serum 1] :
  - **Une seule note tenue**, la fondamentale F ; l'arpégiateur d'Ableton en « random once », RATE libre, automation lent → rapide → lent (effet de roulement). **Ici** : ARP de Serum (cartographie, `../serum2-fx-clip-arp.md` § E), MODE de pattern aléatoire (le nom exact du mode est à lire dans l'interface), pour éviter un effet MIDI de Live.
  - OSC A : « Mellow but Unstable » [ASR « mellow but in stable »], WT POS vers le milieu, LFO bipolaire → WT POS ; UNISON **2**, DETUNE bas, OCT +1 ; WARP 1 **Bend +** modulé par un LFO.
  - OSC B : « Basic CJW » [ASR], WT POS à moitié ; LFO 2 de forme personnalisée **très rapide** → WT POS : le bourdonnement. OSC B **OCT −1**, UNISON 2, DETUNE un peu.
  - FILTER 1 + DRIVE ; NOISE « ARP White » [ASR], PHASE (START) + RAND.
  - ENV 1 : ATK courte, REL assez longue, un peu de SUS. ENV 2 → CUTOFF, forme de pluck (SUS bas, DEC plus court, REL plus longue), peu d'ouverture.
  - Matrice : **Velo → CUTOFF, → LEVEL du NOISE, → PAN de l'oscillateur et du NOISE**.
- **Registre** [CALCUL] : B à OCT −1 : une note jouée à MIDI 53 (174,6 Hz) fait sonner B à 87,3 Hz, sous le High Pass de 100 Hz ; jouer plutôt à partir de MIDI 55 (196 Hz → B à 98 Hz) ou garder le High Pass à 80 Hz.
- **FX** [SOURCE DR-05] : Hyper/Dimension (RATE baissé, MIX monté) → Distortion **Diode 2**, MIX bas → Reverb **Plate** filtrée → Delay **Ping-Pong**.
- **Macro de transition** [SOURCE DR-05] : **MACRO 1 « cutoff » → CUTOFF**, automatisée en montée avant le drop.
- **Valeurs de départ** [ORIGINAL] : ARP 1/16, RATE automatisé de 1/8 à 1/32 ; Velo → CUTOFF 20 %, → LEVEL du NOISE 15 %, → PAN ±20 ; DETUNE 0,1.
- **Macros** : `Tone` = MACRO 1 de la vidéo, CUTOFF 10 → 80 % · `Motion` RATE de l'ARP · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Plate 10 → 40 %.
- **Jeu** : une note, MIDI 55 ; voir la grille melodic techno.
- **Test** : la vidéo place l'automation du rate sur la mesure de tension ; la caler sur huit mesures.

### DN06 Drone grave médium
- **Patch** [SOURCE DR-06, Serum 2] :
  - OSC A : scie, **OCT −2** dans la vidéo. OSC B routé vers le filtre, **OCT −1**, **UNISON 11**. OSC C **OCT 0**, UNISON large. NOISE « Juno Chorus ».
  - FILTER 1 **MG Low 24**, un peu de RES et de DRIVE ; **MONO** ; PORTA en option.
  - ENV 1 : REL courte, ATK un peu montée (un « tick »).
  - LFO → CUTOFF, **2 mesures** puis **1 mesure**, RETRIG, profondeur **55 %** pour la démonstration puis **≈ 6 %** ; « la résonance est la clé ».
  - **OSC C et NOISE** : sortie MAIN coupée, **50 % vers BUS 1**.
- **Registre** (écart avec la vidéo) [CALCUL] : à OCT −2, une note jouée à MIDI 48 sonne à MIDI 24 (32,7 Hz) : c'est du sub, qui doit rester dans son instrument. Ici : A **OCT −1**, B **OCT 0**, C **OCT +1** [ORIGINAL], et on joue de **MIDI 52 à 64** ; A sonne alors de MIDI 40 à 52 (82 à 164 Hz). High Pass à **80 Hz**.
- **FX MAIN** (A et B) [SOURCE DR-06] : Distortion **Diode 1**, RES réduite, MIX.
- **BUS 1** [SOURCE DR-06] : Distortion → Delay **Ping-Pong** (FEEDBACK élevé) → Reverb **Vintage** (SIZE et MIX montés) → Equalizer en High Pass, Q bas, **au-dessus du filtre principal** → Filter **Low 24**.
- **Macro** [SOURCE DR-06] : **MACRO « Filter »** → CUTOFF du filtre principal et du filtre du BUS 1 (une même macro pilote les deux).
- **Valeurs de départ** [ORIGINAL] : MG Low 24, CUTOFF 25 %, RES 40 %, DRIVE 30 ; LFO 1 en 2 bar, RETRIG, sinus → CUTOFF 6 % ; ENV 1 30 ms / 0 / 1 s / −2 dB / 120 ms.
- **Transition** [SOURCE DR-06] : la macro `Tone` automatisée pour les montées ; FEEDBACK et MIX du Delay montés pour la transition.
- **Macros** : `Tone` = MACRO « Filter », 10 → 80 % · `Motion` profondeur du LFO 6 → 55 % · `Dirt` MIX de la Diode 1 0 → 60 % · `Space` niveau de BUS 1 0 → 100 %.
- **Jeu** : une note tenue sous un pad aérien, intro et breakdown, MIDI 52 à 64.
- **Test** : avec un sub joué en même temps sur sa piste, vérifier en mono que la phase du drone ne l'annule pas (`../../../kick-bass-equilibre/SKILL.md`).

### DN07 Drone à évolution imprévisible
- **Méthode** [SOURCE DR-07, Serum 2, peu de valeurs chiffrées] : on met une table en mouvement, puis le filtre, et chaque mouvement est perturbé par un second LFO aléatoire.
- **Patch** :
  - OSC A : « S2 Tables › Analog › at plates » [ASR ? nom incertain].
  - LFO 1 triangle → WT POS, environ **la moitié de la plage**, mode **FREE**, RATE baissé et passé de BPM à **HZ**.
  - LFO 2 : forme **« random curved »** (préréglage de forme), faible profondeur → WT POS, RATE baissé.
  - FILTER 1 (type non dit) : LFO triangle → CUTOFF, profondeur réduite ; un LFO **randomisé** → CUTOFF, vers le bas, faible.
  - Largeur : UNISON ; un LFO neuf → **DETUNE**, sur **≈ 4 mesures**.
  - OSC B : table numérique, **OCT +1**, position balayée par un LFO de **4 mesures** ; routé vers le **même filtre** ; le LFO aléatoire du filtre agit aussi sur B (« delivery »).
  - Un **LFO neuf**, FREE, en HZ, très lent, forme randomisée → **RATE du LFO 1** ; plage réglée dans la matrice.
- **FX** [SOURCE DR-07] : Distortion (saturation), Delay, Reverb ; un **Phaser** monté plus haut dans la chaîne, comme traitement commun.
- **Valeurs de départ** [ORIGINAL] : LFO 1 à 0,05 Hz ; LFO 2 à 0,11 Hz, ±10 % ; LFO 3 à 0,07 Hz ; LFO de rate à 0,02 Hz, ±40 % ; High Pass à 100 Hz.
- **ENV 1** : 3 s / 0 / 4 s / −3 dB / 4 s [ORIGINAL].
- **Pourquoi** [DÉDUCTION] : trois LFO libres de rates premiers entre eux ne repassent jamais par le même état ; l'évolution ne se répète pas sur un long morceau.
- **Macros** : `Tone` CUTOFF 15 → 60 % · `Motion` profondeur des LFO sur WT POS 10 → 60 % · `Dirt` DRIVE de la saturation 0 → 40 · `Space` MIX de la Reverb 20 → 60 %.
- **Jeu** : une note, deux à quatre mesures, ou plus : nappe de fond des longs morceaux minimal et deep.
- **Test** : la vidéo est la seule source et l'étude n'a lu que la narration ; régler la profondeur de chaque LFO à l'oreille, un par un.

### DN08 Drone spectral figé
- **Patch** [SOURCE DR-08, Serum 2] :
  - OSC A : moteur **Spectral**, un sample glissé dedans ; **lecture normale à C3 = MIDI 60** (cartographie § 3.1 : sans suivi, le moteur Spectral joue note 60).
  - Mode de boucle **Manual** : le Spectral devient une « wavetable » figée ; chercher le **sweet spot** de la position.
  - WARP 1 **Detune**, WARP 2 **Spread** (noms internes connus, libellés affichés à lire, cartographie § 4.3).
  - **Gate** spectral (retire les harmoniques faibles) : éteint pour A.
  - OSC B : Spectral, un second sample, Manual, position, **Gate actif**, **OCT −1** ; WARP **Spread**.
  - NOISE « vinyl crackle » (foley).
- **FX** [SOURCE DR-08] :
  1. Delay en **triolet**, Ping-Pong.
  2. Reverb : mode **Nitrous** (« Spin Space » [ASR ?]), MIX **50 %**.
  3. **Splitter M/S** → Equalizer sur la voie SIDE, coupe sous **250 Hz**.
  4. Chorus (préréglage douteux).
  5. Compressor **Multiband** (préréglage d'usine « MB OTT » [ASR « mbot »], non listé dans la cartographie).
  - REL montée ; crackle baissé.
- **Delay en triolet** [CALCUL] : à 122 BPM, 1/8 triolet = 163,9 ms ; à 124 BPM, 161,3 ms.
- **Droits** : le sample de la vidéo est tiré au hasard dans une collection ; un sample libre de droits, ou un son d'usine de Serum, convient ici (règle 7).
- **ENV 1** : 2 s / 0 / 4 s / −2 dB / 3 s [ORIGINAL].
- **Macros** : `Tone` FREQ LO du filtre spectral 80 → 500 Hz · `Motion` position de B 0 → 100 % · `Dirt` MIX du Gate 0 → 100 % · `Space` MIX du Nitrous 30 → 70 %.
- **Jeu** : accord tenu, MIDI 55 à 72 ; le sample figé joue à la hauteur de la note.
- **Test** : un drone tonal propre en stéréo avec un crackle, sans grave, qui laisse le sub du kick tranquille.

### DN09 Drone sombre de samples
- **Patch** [SOURCE DR-09, Serum 2] :
  - Note **E grave**. Moteur **Sample**, sample « spatial » ; PITCH **−2 octaves** puis plus bas.
  - Une grosse **reverb à convolution**, IR « Long » ; **Convolve** dans les effets (cartographie § 8 : IR d'usine `Long`).
  - OSC B en couche : un sample de SFX plus aigu. OSC C : une troisième couche de « noises » sporadiques.
  - Des one-shots passés en **boucle avant et arrière** pour faire des textures.
  - Une note tonale ajoutée.
  - **Filtre** qui s'ouvre dans le temps : riser de suspense (voir DN16).
  - **Filtres notch** modulés par un LFO aléatoire (voir DN17).
- **Registre** [CALCUL] : un E à MIDI 40 (82,4 Hz) joué avec le sample à −2 octaves donne des composantes bien sous 80 Hz ; régler le High Pass à **70 Hz** [ORIGINAL], l'intro n'ayant pas de basse, et ne pas le descendre plus bas pour ne pas masquer le sub de l'entrée.
- **FX** [SOURCE DR-09] : Convolve « Long » → Compressor **Multiband** (boost des aigus pour le riser) → Equalizer en High Pass.
- **Valeurs de départ** [ORIGINAL] : PITCH −24 st puis −36 st ; Convolve IR GAIN −6 dB, MIX 50 % ; ENV 1 2 s / 0 / 5 s / −2 dB / 3 s.
- **Droits** : samples de la suite de DNB Academy dans la vidéo ; utiliser les tiens (règle 7).
- **Macros** : `Tone` CUTOFF 10 → 80 % · `Motion` PITCH de la couche 1 −12 → −36 st · `Dirt` MIX du Multiband 0 → 50 % · `Space` MIX du Convolve 20 → 80 %.
- **Jeu** : intro « droney » de DnB atmosphérique et sombre, qui laisse place au drop ; MIDI 40 à 52.
- **Test** : la valeur exacte du pitch est « à vérifier à l'écran » dans l'étude ; −24 puis −36 sont des départs.

### DN10 Accord de sinus resamplé
- **Patch** [SOURCE DR-10, Serum 2] :
  - Sinus sur les **trois oscillateurs** ; l'accord est construit avec leurs SEM : **quinte (+7)**, **tierce +3** (mineur ; +4 pour un accord majeur), et une **septième sur le troisième oscillateur** ; essai en scie.
  - NOISE « Geiger » [ASR « geer »] : un bruit de couleur de Serum 2 (cartographie § 3.7), « count » monté (la densité des clics).
  - Effets (bus ou master plutôt que par oscillateur), distortion **épaisse et large**.
- **L'accord** [CALCUL, lecture à vérifier] : la vidéo dit quinte, tierce, puis septième sur le troisième oscillateur ; deux lectures :
  - triade mineure : A 0, B +7, C +3 ;
  - mineur 7 sans tierce : A 0, B +7, C +10.
  Écouter les deux et garder celle qui s'accorde avec la basse.
- **Resampling** [SOURCE DR-10] :
  1. **Export** : l'icône à gauche du logo Serum = bounce de la dernière note jouée.
  2. Nouvelle instance : Init, OSC A en **Granular**, le bounce glissé dedans.
  3. Effets granulaires, **« chaos »**, **PAN aléatoire des grains** ; compression pour le niveau ; MONO, ATK montée.
  4. Option : moteur **Spectral**. Re-bounce, itération.
- **Valeurs de départ** [ORIGINAL] : sinus UNISON 1, SEM 0 / +7 / +3 ; Granular DENSITY 60 %, RANDOM 30 %, SCAN 10 % ; Distortion Sine Fold MIX 30 % ; High Pass à 100 Hz.
- **ENV 1** : 2 s / 0 / 4 s / −3 dB / 3 s [ORIGINAL].
- **Macros** : `Tone` Low Pass 3 → 12 kHz · `Motion` SCAN du Granular 0 → 50 % · `Dirt` MIX de la distortion 10 → 60 % · `Space` MIX de la Reverb 20 → 70 %.
- **Jeu** : une note, MIDI 53 à 65 ; le bounce se joue ensuite sur tout le clavier.
- **Test** : le contexte de la vidéo est « ambient » ; dans un morceau DnB, vérifier que la nappe ne remplit pas les 4 kHz du break.

### DN11 Atmosphère rêveuse en Fm7
- **Patch** [SOURCE DR-11, Serum 2] :
  - Table douce **« Bottle Blow »** (sinus + harmoniques) ; accord **fa mineur 7** ; UNISON à **nombre impair** de voix.
  - **NOISE → FM** (noise FM) ; un sample de vinyl crackle étiré (« stretched vinyl »).
  - FX : Chorus, Reverb, Delay, Distortion, Compressor **OTT** (« beaucoup »).
  - LFO **S&H**, SMOOTH au maximum → **FIN**, RATE monté.
- **Resampling** [SOURCE DR-11] :
  1. **Bounce in place** (icône d'export) ; la queue de la reverb est coupée au bounce.
  2. Nouvelle instance de Serum 2, OSC **Spectral**, sample déposé, mode **Manual** : la position est figée, on la balaie.
  3. La note F jouée = la **hauteur d'origine** du sample (« C = −5 demi-tons » : MIDI 60 transpose de −5).
  4. Filtre (retire les aigus) ; **filtre spectral** bas et haut ; UNISON, Distortion, Reverb, Compressor, Delay, Equalizer.
  5. Note tenue aussi longtemps que voulu ; S&H → FIN à nouveau.
- **Idée bonus** [SOURCE DR-11] : poser une **reese en dessous** (`../../../serum-2-basses-house-future-house/references/recettes/dnb-f02-reese.md`) ; n'importe quelle source (samples de pads) convient.
- **Voicing de Fm7** [CALCUL] : F, Ab, C, Eb = MIDI 53, 56, 60, 63 ; la tonique F à 174,6 Hz reste au-dessus du High Pass de 100 Hz.
- **Valeurs de départ** [ORIGINAL] : UNISON 5, DETUNE 0,1 ; LFO S&H à 6 Hz, SMOOTH 100, ±8 cents ; NOISE → FM (B) 15 %.
- **ENV 1** : 1 s / 0 / 4 s / −3 dB / 3 s [ORIGINAL].
- **Macros** : `Tone` CUTOFF 20 → 70 % · `Motion` S&H → FIN 0 → ±15 cents · `Dirt` GAIN du Multiband (OTT interne) 0 → 12 dB · `Space` MIX de la Reverb 20 → 60 %.
- **Jeu** : intro ou breakdown de DnB liquide ; voir la grille.
- **Test** : « beaucoup d'OTT » rend les queues bruyantes ; couper à 20 % de MIX et remonter.

### DN12 Pad sombre neuro
- **Patch** [SOURCE DR-12, Serum 2] :
  - OSC A et B : scie, **OCT −2** (voir le registre), B **SEM +3**, **UNISON 2**, DETUNE bas ; PORTA un peu.
  - OSC C : table S2 « Digital › Vocal Hum », WT POS **230**, **OCT −1**, **SEM +3**.
  - FILTER 1 « Misc › High EQ 6 » [ASR ?] sur tous les oscillateurs, CUTOFF **≈ 26** ; RES montée, DRIVE ; LEVEL du Vocal Hum monté.
  - LFO **2 mesures** → WT POS (vers 0) et → CUTOFF.
  - Filter FX **MG Low**, LFO **1/8** en mode **ENVELOPE** (rampe plate puis montante) → CUTOFF et DRIVE.
  - SUB à −1 octave en **Direct Out** dans la vidéo : ici **éteint** (règle 1) ou sur sa piste.
  - REL d'ENV montée.
- **Registre** [CALCUL] : à OCT −2, une note jouée à MIDI 55 sonne à 31 (49 Hz). **Ici** : OCT −1 pour A et B, OCT 0 pour C [ORIGINAL] ; jouer de MIDI 55 à 67 : A sonne de 98 à 196 Hz. High Pass à 80 Hz.
- **FX** [SOURCE DR-12] :
  1. Chorus par défaut, High Pass actif.
  2. Reverb **Vintage** : SIZE **30 %**, LO CUT ≈ 90, DECAY monté, MIX monté ; SIZE montée ensuite.
  3. Delay **Ping-Pong** subtil, **1/4**.
  4. Compressor **Multiband** (OTT).
- **Durées** [CALCUL] : à 174 BPM, 2 mesures = 2,76 s, 1/8 = 172,4 ms, 1/4 = 344,8 ms.
- **ENV 1** : 600 ms / 0 / 3 s / −2 dB / 2,5 s [ORIGINAL].
- **Macros** : `Tone` CUTOFF 10 → 60 % · `Motion` LFO 2 mesures → WT POS 0 → 70 % · `Dirt` DRIVE du filtre 10 → 60 · `Space` MIX de la Vintage 20 → 60 %.
- **Jeu** : accords tenus dans une atmosphère de DnB neurofunk, MIDI 55 à 67.
- **Test** : la vidéo vise le neurofunk ou la hard DnB (7:28) ; garder le pad derrière la reese.

### DN13 Fond minimal
- **Patch** [SOURCE DR-13, Serum 1, très peu de valeurs] :
  - **Init, désaccordée** (« tune in a bit ») ; un filtre (type non dit) ; ENV : DEC et SUS ; NOISE **très bas** ; **reverb indispensable** pour remplir.
  - Une variante rythmique rapide (« façon Alex Rome » [ASR ?]).
- **Valeurs de départ** [ORIGINAL, aucune valeur dans la vidéo] : OSC A scie, UNISON 3, DETUNE 0,08 ; MG Low 24, CUTOFF 25 % ; ENV 1 3 s / 0 / 4 s / −4 dB / 4 s ; NOISE rose, LEVEL 5 % ; Reverb Hall MIX 50 %, DECAY 6 s ; High Pass à 100 Hz.
- **Durées** [CALCUL] : à 140 BPM, 8 mesures = 13,7 s, 16 mesures = 27,4 s, 32 mesures = 54,9 s.
- **Rôle** [SOURCE DR-13] : bruit de fond d'intro, minimal ; intros de deep dubstep de **8, 16 ou 32 mesures**.
- **Macros** : `Tone` CUTOFF 10 → 50 % · `Motion` DETUNE 0,03 → 0,2 · `Dirt` NOISE 0 → 15 % · `Space` MIX de la Reverb 30 → 70 %.
- **Jeu** : une note ou une quinte tenue toute l'intro, MIDI 53 à 65.
- **Test** : la vidéo est trop courte pour valider les valeurs ; la lecture à l'écran est indispensable (« À vérifier à l'écran » de l'étude).

### DN14 Drone de piano resynthétisé
- **Patch** [SOURCE DR-14, Serum 1] :
  1. **Un piano est échantillonné** en C4 (registre de MIDI 48 à 60 dans Live), vélocité modérée.
  2. Passé dans **ValhallaVintageVerb**, mode **Ambience**, DECAY **≈ 30 s**, MIX **≈ 70** ; **bounce** en audio.
  3. Le WAV est copié dans le dossier de presets de Serum (Noises › User › Ambient) et chargé dans le **NOISE**. **Serum 2** : moteur Sample, ou NOISE › **Load Sample** (cartographie § 3.3 et § 3.7).
  4. NOISE : deux boutons actifs (one-shot et suivi de hauteur, interprétation), PITCH **+12**, LEVEL monté ; un peu de RAND sur la phase.
  5. OSC A : table « basique », **UNISON 7**, DETUNE large ; **LPF simple sur OSC A seulement**, le NOISE n'est pas routé dans le filtre ; ENV → CUTOFF en option.
  - **ENV 1 : ATK ≈ 19 s**, HOLD, REL longue.
  - LFO 1 en rampe légère, **8 mesures** → **Main Tuning** : un petit bend.
- **Durées** [CALCUL] : 19 s = 11,1 mesures à 140 BPM, 9,7 mesures à 122 BPM ; 8 mesures = 13,7 s à 140 BPM.
- **FX** [SOURCE DR-14] : Distortion, Delay, Reverb, Equalizer en High Pass à 100 Hz.
- **Valeurs de départ** [ORIGINAL] : ENV 1 19 s / 2 s / 5 s / −2 dB / 6 s ; UNISON 7, DETUNE 0,2 ; LFO 1 en 8 bar → Main Tuning +0,3 st.
- **Droits** : le piano de la vidéo est un échantillon personnel ; enregistrer ou charger le tien (règle 7).
- **Recette de la vidéo** [SOURCE DR-14] : ne pas trop filtrer le sample.
- **Macros** : `Tone` CUTOFF de A 20 → 80 % · `Motion` LFO 1 → Main Tuning 0 → 1 st · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Reverb 20 → 70 %.
- **Jeu** : tenir la tonique d'un breakdown ; usages cités dans la vidéo : bandes-annonces, dubstep, melodic dubstep, trance.
- **Test** : voir DN20, qui rend ce drone jouable.

### DN15 Drone FM inharmonique
- **Patch** [SOURCE DR-15, en français, Serum 1] :
  - **FM avec des formes quasi sinusoïdales**. OSC A porteuse, OSC B modulateur à **LEVEL 0** : WARP 1 d'A en **FM (B)**.
  - Table maison : un sinus un peu plus riche, une deuxième frame identique **à l'octave**, une troisième légèrement différente : un **morph** entre les frames. Le modulateur est un **sinus pur**.
  - **Rapport FM non entier** (modulateur désaccordé) pour l'inharmonicité ; valeurs dites « −12 et … » [ASR ?], modulateur « −15 +3 » [ASR ?] puis affinage autour de **−12**.
  - ENV 1 : ATK longue, SUS un peu baissé, beaucoup de REL. ENV 2 très longue (attaque longue, release, SUS qui descend) → léger mouvement (cible non dite).
  - Mouvement sur la FM et sur WT POS.
  - FILTER 1 **passe-bande** « BP12 » [ASR « bn 12 »] (Band 12, ou Multi BN, non tranché) : garder le grave et le bas-médium ; DRIVE.
  - Filter FX : un **notch qui se balade dans le bas-médium**, modulé par un LFO puis par « Chaos » [ASR « en carrosse »] : lent.
  - LFO 3 → **Main Tuning**, unipolaire, rampe à mi-chemin, **4 mesures**, profondeur de **quelques demi-tons** : un désaccord lent.
- **Rapport** [CALCUL] : −12 demi-tons donnent un rapport 0,5 (une octave sous) ; −15 donnent 0,42 et −9 donnent 0,59. Un rapport non entier produit des partiels qui ne sont pas des multiples de la fondamentale.
- **Jeu** [SOURCE DR-15] : **2 à 3 octaves plus bas**, **deux notes à l'octave, pas d'accords**. **Ici** : jouer de MIDI 53 à 65 avec l'oscillateur à OCT −1 et un High Pass à **80 Hz** ; le sub vient d'une recette de sub (règle 1).
- **FX** [SOURCE DR-15] : Reverb « indispensable », « autour de 70-80 » (SIZE ou MIX, non tranché : à lire à l'écran) ; **OTT léger** pour remonter les queues ; ne pas trop pousser la FM.
- **Durée** [CALCUL] : à 140 BPM, 4 mesures = 6,86 s.
- **Valeurs de départ** [ORIGINAL] : FM (B) 25 %, SEM de B −12 ; Band 12, CUTOFF 400 Hz, DRIVE 30 ; ENV 1 3 s / 0 / 4 s / −4 dB / 5 s ; LFO 3 en 4 bar, FREE, rampe → Main Tuning +3 st.
- **Macros** : `Tone` CUTOFF du Band 12 200 → 1200 Hz · `Motion` FM (B) 10 → 50 % · `Dirt` DRIVE 10 → 60 · `Space` MIX de la Reverb 30 → 80 %.
- **Contexte** : cinématique, bandes-annonces, horreur (dit à 0:58) ; l'étude l'affecte aux intros sombres de dubstep ou de DnB.
- **Test** : le désaccord à 3 demi-tons sur quatre mesures doit sonner comme un mouvement de bande, pas comme une fausse note.

### DN16 Riser de suspense
- **Patch** [SOURCE DR-09, passages « riser » à 7:01 et 7:45] :
  - Un drone (DN09 ou DN15) dont le **filtre s'ouvre dans le temps** : suspense d'intro.
  - **Compressor Multiband** : boost des aigus pour le riser ; High Pass.
- **Recette** [ORIGINAL pour les valeurs] :
  - ENV 2 → CUTOFF, ATK **8 mesures** (en BPM), SUS 100 %, profondeur 70 % ; ou la macro `Tone` automatisée sur huit mesures.
  - Multiband : bande haute montée de +6 dB, MIX 50 %.
  - Equalizer High Pass dont la FREQ monte de 100 à 600 Hz avec le riser (ENV 2 → FREQ du High Pass).
  - Reverb Hall MIX 40 %.
- **Durées** [CALCUL] : à 174 BPM, 8 mesures = 11,0 s ; à 122 BPM, 15,7 s.
- **Macros** : `Tone` = la montée, CUTOFF 10 → 100 % · `Motion` ENV 2 → CUTOFF 0 → 70 % · `Dirt` MIX du Multiband 0 → 60 % · `Space` MIX de la Reverb 20 → 50 %.
- **Jeu** : une note tenue pendant huit mesures, qui tombe sur le drop ; couper la note et la reverb au drop (queue coupée au bounce, DR-11).
- **Test** : le riser et un impact sur le temps 1 du drop ne doivent pas se superposer dans le grave.

### DN17 Drone à notches aléatoires
- **Patch** [SOURCE DR-09, passage 8:40 à 9:03] : des **filtres notch** modulés par un **LFO aléatoire**.
- **Recette** [ORIGINAL pour les valeurs] :
  - Un drone tonal (DN11, DN15, ou OSC A scie UNISON 3 simple).
  - FILTER 1 **Notch 12** (catégorie Normal) ; LFO 1 de **TYPE S&H**, RATE 2 Hz, SMOOTH 60 → CUTOFF ±35 % ; FILTER 2 **Notch 12** en série, un autre LFO S&H à 3 Hz → CUTOFF ±30 %. Les deux notches se déplacent sans se synchroniser.
  - Un second drone sans notch en parallèle, à LEVEL 30 %, pour garder du corps.
- **Le notch** [DÉDUCTION] : un notch creuse une bande ; son déplacement au hasard fait « respirer » le spectre ; la résonance (RES 20 %) accentue le creux.
- **FX** : Reverb Hall MIX 40 %, High Pass à 100 Hz.
- **Macros** : `Tone` CUTOFF de base 20 → 70 % · `Motion` profondeur des S&H 0 → 50 % · `Dirt` RES 0 → 40 % · `Space` MIX de la Reverb 20 → 60 %.
- **Jeu** : notes tenues dans une intro sombre ; MIDI 52 à 64.
- **Test** : sans source chiffrée, ce n'est qu'une direction ; la vidéo (DR-09) ne donne ni rate ni profondeur.

### DN18 Drone de bruit coloré
- **Recette [ORIGINAL]**, appuyée sur le NOISE de Serum 2 (cartographie § 3.7) et sur DR-10 (« Geiger »).
- **Patch** :
  - NOISE, catégorie **bruits de couleur** : **Pink** (−3 dB/oct), **Brown** (−6 dB/oct) ou **Geiger** (clics aléatoires, « count » = densité) ; ces types affichent **STEREO** (0 = mono, 100 = décorrélé) et **FILTER** (COLOR).
  - NOISE routé vers FILTER 1 ; Band 12, CUTOFF 800 Hz, RES 50 % ; ENV 1 4 s / 0 / 4 s / −4 dB / 4 s.
  - LFO 1 → CUTOFF, RATE 4 mesures, SMOOTH 60 %.
- **Pourquoi** [FICHE pour le bruit comme colle ; DÉDUCTION pour le reste] : un bruit rose a de l'énergie vers le grave ; un High Pass à 120 Hz le nettoie. Geiger apporte des clics à densité réglable.
- **Variante** : DN01 pour un échantillon de goutte, ici pour des types sans échantillon.
- **FX** : Reverb Hall MIX 40 %, Equalizer en High Pass à 120 Hz.
- **Macros** : `Tone` COLOR / FILTER du NOISE 20 → 80 % · `Motion` LFO 1 → CUTOFF 0 → 50 % · `Dirt` densité de Geiger 10 → 60 % · `Space` MIX de la Reverb 20 → 70 %.
- **Jeu** : transitions et textures, sans hauteur ; deux à huit mesures.
- **Test** : le bruit rose de Serum 2 est stéréo à 100 ; vérifier le mono.

### DN19 Fond doux sous 124
- **Recette [ORIGINAL]** pour la règle « Signature sous 124 BPM » d'`AGENTS.md` : un fond qui laisse le kick doux et clair de la signature (`../../../drums-signature/references/signature.md`).
- **Patch** :
  - OSC A : sinus, RAND 0. OSC B : triangle, SEM +7, LEVEL 40 %. NOISE rose, LEVEL 4 %, hors du filtre.
  - FILTER 1 MG Low 12 sur A et B, CUTOFF 35 %. ENV 1 2 s / 0 / 4 s / −6 dB / 3 s.
  - LFO 1 en 4 bar, FREE, sinus → LEVEL de B ±20 % et → CUTOFF ±10 %.
- **FX** : Chorus MIX 20 % → Equalizer en High Pass à 120 Hz → Reverb Plate, MIX 30 %, DECAY 5 s.
- **Durée** [CALCUL] : à 122 BPM, 4 mesures = 7,87 s ; DECAY 5 s = 2,5 mesures.
- **Macros** : `Tone` CUTOFF 15 → 50 % · `Motion` LFO 1 → LEVEL de B 0 → 40 % · `Dirt` NOISE 0 → 10 % · `Space` MIX de la Plate 15 → 45 %.
- **Jeu** : une quinte tenue, MIDI 55 à 67.
- **Test** : sans source vidéo ; à valider avec le kick de la signature.

### DN20 Drone devenu pad jouable
- **Principe** [SOURCE DR-14] : en baissant l'attaque de 19 s, « on obtient un pad jouable ».
- **Patch** : celui de DN14 ou de DN01, avec **MACRO 5 `Attack`** → ATK d'ENV 1 (courbe exponentielle de 300 ms à 19 s) et → ATK d'ENV 2.
- **Recette** [ORIGINAL] :
  - `Attack` à 0 % : ATK 300 ms, REL 800 ms : le patch joue des accords.
  - `Attack` à 100 % : ATK 19 s, REL 6 s : un drone.
  - Automatiser `Attack` sur un breakdown : le pad se fait drone quelques mesures avant le drop, puis revient à 0 % sur le drop.
- **Durées** [CALCUL] : à 124 BPM, 19 s = 9,8 mesures ; 300 ms ≈ une noire (484 ms) moins un tiers.
- **Macros** : `Tone` CUTOFF 20 → 70 % · `Motion` MACRO 5 `Attack` 0 → 100 % · `Dirt` DRIVE 0 → 40 · `Space` MIX de la Reverb 20 → 60 %.
- **Jeu** : accords tenus quand `Attack` est bas ; une note quand `Attack` est haut.
- **Test** : une attaque de 19 s ne démarre une note qu'à la moitié du breakdown ; caler la note sur la frontière de huit mesures précédente.

## Motifs de départ (grilles vérifiées)

Numérotation de Live (C3 = 60). Notes tenues, une voix par ligne ; les voicings sont écrits ici. Vérification, depuis le dossier du skill : `python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/synths/drones.md`. Notation Producer Pal : `--fichier references/synths/drones.md --titre <titre> --format ppal`.

```grille
titre: Melodic techno 124 — une note tenue (DN04, DN05)
tempo: 124
accords: Fm | Fm | Fm | Fm
drone: F3[1:16] | F3[1:16] | F3[1:16] | F3[1:16]
```

```grille
titre: DnB 174 — Fm7 rêveuse (DN11)
tempo: 174
accords: Fm7 | Fm7
haut: Eb4[1:16] | Eb4[1:16]
milieu: C4[1:16] | C4[1:16]
bas: Ab3[1:16] | Ab3[1:16]
tonique: F3[1:16] | F3[1:16]
```

```grille
titre: Dubstep 140 — deux notes à l'octave (DN15)
tempo: 140
accords: Fm | Fm
octave: F3[1:16] | F3[1:16]
tonique: F2[1:16] | F2[1:16]
```

## Ce qui reste à faire par l'utilisateur

- Retrouver dans Serum 2 : « Soar Electricity » [ASR], « Dist Sub » [ASR], « Cream » [ASR], « Glass Lid 5 » [ASR], « Analog_BD_Sin », « 4088 » [ASR], « Mellow but Unstable » [ASR], « Basic CJW » [ASR], « ARP White » [ASR], « Juno Chorus », « at plates » [ASR], « Bottle Blow », « Vocal Hum », « Rain 100 High » (déjà cité dans `pads.md`), « Alpha NZ » ; le préréglage « MB OTT » [ASR] ; l'IR « Long » de Convolve ; les types **Geiger**, **Pink** et **Brown** du NOISE.
- Lire à l'écran : le mode aléatoire de l'ARP de Serum (DN05), le sens de la reverb « 70-80 » (DN15), la cible de ENV 2 (DN15), le sens de l'accord de sinus (DN10).
- Écouter chaque recette (règle 10 de `leads.md`) avec la basse et le sub du morceau, en mono ; garder un ou deux drones par morceau et consigner le preset retenu dans la mémoire du projet (`../../../memoire-projet/SKILL.md`).
- Le lot de synthés est complet : 100 recettes en cinq fichiers (leads, plucks, hooks, accords, pads) plus celui-ci, soit 120.
