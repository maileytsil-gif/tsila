# Études des tutoriels écrits : House, Future House et général

Identifiants (`F01-02`…) : registre `tutoriels-a-consulter.md`. Documentation de fond : `documentation-basses.md`. Ces relevés servent de matière aux recettes ; chaque valeur est celle que la page écrit, à régler ensuite à l'oreille de l'utilisateur.

Relevé du 05/10/2026, en session cloud, par un sous-agent de Claude Code. Chaque page a été récupérée par `curl`, puis son texte extrait (titres, paragraphes, listes, tableaux, légendes, texte alternatif). Pour les pages de musicproductiontutorials.co.uk, le texte vient des données JSON intégrées à la page (application Inertia) : description, chapitres, plug-ins et étiquettes minutées.

Conventions de ce relevé :
- Les noms de contrôles Serum sont laissés en anglais, tels que la page les écrit.
- « Valeur en image, non lue » : la page renvoie à une capture sans donner le chiffre dans le texte.
- Aucune vidéo n'a été visionnée et aucun audio n'a été écouté (règle 4 d'`AGENTS.md`).
- Hauteurs : plusieurs pages emploient la notation scientifique (C1 = 32,7 Hz = MIDI 24), que Live affiche **C0** (C3 = 60). Il faut convertir avant d'écrire une note dans Live.

---

### F01-02 How to Make Hard-Hitting 808s in Serum 2 — Maxim Hetman, Monosounds.studio (Serum 2, 02/07/2026, modifiée le 18/08/2026)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Titre de l'onglet : « Serum 2 808 Tutorial: Hard-Hitting 808s From Init ».
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : Init. Osc A sur la table Default, position 1 (sinus pur). Unison = 1. Triangle en variante, pour plus de présence sur petit haut-parleur. Osc A en Oct -1. Voicing mono, une note à la fois.
  - Enveloppe de hauteur (le « knock ») : Env 2 glissée sur le coarse pitch d'Osc A, avec attack 0 ms, decay 60 ms et sustain 0. Quantité **+24 demi-tons** : la note part deux octaves au-dessus et redescend en 60 ms. Les variantes sont +36 demi-tons (attaque plus dure, plus de clic) et un decay proche de 120 ms (chute « lazy, booming », bien à 130-140 BPM, « mud » plus vite).
  - FX : Distortion en mode **Overdrive** (« arrivé avec la version 2 », selon la page), drive près de **25 %**, mix **50-70 %** (la FAQ dit 60 %). La page la place sur un bus FX à part dans Serum 2. Elle est suivie d'un passe-bas vers **400 Hz** pris parmi les modèles « analog-style » (modèle précis non nommé, renvoi à un autre guide). Au-delà de 50 % de drive avec un mix haut, on quitte l'808 pour de la « bass design ».
  - Glide : Mono on, Legato on, Portamento près de **100 ms**. Les notes qui se chevauchent glissent, les notes séparées redéclenchent. Valeurs : 60-100 ms pour la trap, **200-300 ms** pour des glissés de drill sur une octave (250 ms dans la FAQ).
  - Accord : mettre la quantité de l'enveloppe de hauteur à zéro, jouer C1 contre un accordeur ou un sinus de référence, corriger au fine tune. Un decay de clic long fait paraître la note plus haute.
  - Tableau des tessitures : A0 27,5 Hz (club seulement), C1 32,7 Hz (défaut classique), E1 41,2 Hz (zone sûre), G1 49,0 Hz (lisible sur portable), A1 55,0 Hz (plus tonal), C2 65,4 Hz (plus de knock que de sub, phonk). Si la tonique tombe sous B0, monter d'une octave.
  - Enveloppe d'amplitude, trap : Env 1 avec A 0, D ≈ 3 s, S 0 %, R 300 ms.
  - Enveloppe d'amplitude, drill : S 80-100 %, D ≈ 1 s, R 150 ms.
  - Couche de clic : Osc B en moteur **Sample**, transitoire de kick ou rimshot de moins de **100 ms**, keytracking off, **12-15 dB sous le sinus**. Le glide continue de marcher parce que le sub porte la hauteur.
- **Conseils de jeu ou de mix** :
  - Le piano roll décide des glissés, par chevauchement ou par trou.
  - Pour tester, écouter en mono à bas volume.
  - Les 808 se jouent entre C1 et G1 en notation scientifique, soit C0-G0 dans Live.
  - Les presets Serum 1 s'ouvrent dans Serum 2.
- **Limites** :
  - Deux images sont des aide-mémoire (« 808 From Init in 6 Steps », « Trap vs Drill 808 Cheat Sheet ») : valeur en image, non lue.
  - La page ne nomme pas le modèle de filtre analogique.
  - Elle vise la trap et la drill, pas la house.
  - Le glide est donné à « près de 100 ms » dans le texte et à « 250 ms » dans la FAQ pour la drill : pas de contradiction, ce sont deux usages.
- **Utilité pour une recette** : recette chiffrée d'un 808 ou d'un sub à knock dans Serum 2 (+24 demi-tons / 60 ms, Overdrive 25 % / 60 %, clic par Sample à −12/−15 dB), transposable à une basse house en raccourcissant Env 1.

### GEN-06 How to Make a Bass in Serum 2 (Step by Step, With Screenshots) — Maxim Hetman, Monosounds.studio (Serum 2, 06/09/2026)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Titre de l'onglet : « How to Make a Bass in Serum 2: Step-by-Step Tutorial (2026) ».
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : MENU › Init Preset. Osc A sur Basic Shapes, **WT POS sur la frame 2** (scie), **OCT -1**.
  - Sub : SUB activé, sinus, OCT -1, laissé en sortie directe hors filtres (« filtrer le sub ne fait que le rendre plus faible »).
  - Filtre : FILTER 1 activé. Selon la page, Serum 2 propose MG Low 12 par défaut ; l'auteur passe en **MG Low 24**, CUTOFF ≈ **40 %**, RES **15-20 %** (18 % dans le tableau récapitulatif). Vérifier que le bouton de routage **A** (rangée S, A, B, C, N) est allumé.
  - Env 1 (amplitude) : ATK **2 ms**, DEC ≈ **350 ms**, SUS ≈ **−5 dB**, REL **120 ms**.
  - Env 2 vers le filtre : ATK **1 ms**, DEC ≈ **220 ms**, SUS 0, REL **150 ms**, glissée sur CUTOFF avec une profondeur d'environ **30 %**.
  - Matrice : VELO → CUTOFF ≈ **10 %**. L'onglet MATRIX montre « Env 2 » et « Velo » vers « Filter 1 Freq ».
  - FX, dans l'ordre :
    1. Distortion en mode **Tape Sat**, drive ≈ **28**, mix **45 %** (rester sous la moitié).
    2. Equalizer : bande 1 en passe-haut à **32 Hz** ; bande 2 en coupe douce de **−3 dB vers 2,8 kHz**.
    3. Compressor : threshold ≈ **−20 dB**, ratio **4:1**, attack **8 ms**, release **110 ms**, un peu de makeup gain.
  - Sortie : crêtes vers **−6 dBFS** en sortie de Serum, réglées par le bouton MAIN et non par les niveaux d'oscillateurs.
- **Conseils de jeu ou de mix** :
  - Pas d'unison sur le sub : sous 100 Hz, les voix désaccordées s'annulent. La largeur se met sur Osc A, et sa partie large passe par un passe-haut.
  - Pas de réverb sur la basse. Si besoin, réverb en envoi, avec un passe-haut à **200 Hz** sur le retour.
  - Au-delà de 30 % de résonance sur un filtre ladder, le fondamental baisse.
  - Activer MONO dans VOICING, puis LEGATO et un peu de portamento pour les glissés.
  - Variantes de la page :
    - carré au lieu de la scie : basse plus ronde, « 80s » ;
    - distortion mix 80 % et un second filtre dans le rack FX : territoire Reese ;
    - cutoff 25 % sans distortion : basse façon 808 ;
    - Ladder Acid : couleur plus agressive.
- **Limites** :
  - Toutes les captures sont des images, mais les valeurs sont aussi écrites dans le texte et le tableau.
  - Unités mêlées : le cutoff est donné en %, pas en Hz.
  - La page affirme que MG Low 12 est le défaut de Serum 2 : à vérifier dans l'interface.
  - Le sub est **dans le même patch** que la basse médium, alors que la règle du projet veut deux instruments séparés.
- **Utilité pour une recette** : patron complet et chiffré d'une basse « pluck » house dans Serum 2, de l'oscillateur au compresseur. C'est la meilleure base de départ du lot.

### F03-04 FM Synthesis in Serum 2: How the FM Warp Mode Works (With Screenshots) — Maxim Hetman, Monosounds.studio (Serum 2, 21/09/2026)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Titre de l'onglet : « Serum 2 FM Synthesis Tutorial: FM, RM, AM Warp Modes Explained ».
- **Gestes et réglages écrits, dans l'ordre** :
  - Menu warp : sous chaque oscillateur, deux boutons WARP avec chacun un menu. Le menu contient Off, Sync, Alt Warp, Filter, Distortion, FM, PD, AM, RM et Swap Warps.
  - Sources de FM : les deux autres oscillateurs, le noise, le sub, Filter 1 et Filter 2. Une option Thru-Zero existe, qui garde la FM profonde « lisse ».
  - Règle de routage : le modulateur doit être **activé**. Le mettre à LEVEL 0 pour ne pas l'entendre.
  - Patch de base : Osc A en sinus (porteuse). Osc B en sinus, LEVEL 0, OCT +1. WARP 1 d'Osc A sur FM, source B ; l'étiquette affiche « FM (B) ».
  - Lecture du bouton WARP 1 :
    - 0 : sinus ;
    - **20 %** : piano électrique ;
    - **50 %** : cloche ;
    - au-delà de **70 %** : « metallic mess ».
  - Rapport de hauteur : B à +1 octave donne un son harmonique ; B à **+7 demi-tons** donne un son inharmonique ; quelques cents de désaccord donnent un battement lent.
  - Mouvement : ENV 2 → WARP 1 ≈ **40 %**, attaque rapide, decay ≈ une demi-seconde, sustain 0. Vélocité → WARP 1 **15 %**.
  - Recette « FM bass » : porteuse en **scie**, modulateur en sinus **une octave plus bas**, WARP 1 FM (B) **30 %**, ENV 2 à **50 %** de profondeur avec un decay de **150 ms**, puis un filtre **MG Low 24**.
  - Autres recettes :
    - e-piano : WARP 18 %, ENV 2 35 %, decay 600 ms, vélocité 20 %, chorus lent ;
    - cloche : modulateur à +19 demi-tons, WARP 45 %, release longue, Plate reverb.
  - Modes voisins : PD est plus doux (« CZ-style ») ; AM donne un trémolo ou du grain ; RM donne un son creux, inharmonique, « radio ».
  - Autres moteurs : le menu warp marche aussi sur Sample, Multisample, Granular et Spectral. La FM depuis le noise ajoute du « fizz » pour growl et neuro.
- **Conseils de jeu ou de mix** : l'enveloppe sur la quantité de FM est « la partie la plus importante de tout patch FM ». La FM donne à l'attaque un claquement qu'une enveloppe de filtre seule ne fait pas.
- **Limites** :
  - Captures en image, mais les valeurs sont écrites dans le texte.
  - Pas de réglage d'enveloppe d'amplitude pour la FM bass.
  - Le modulateur de la FM bass est réglé une octave plus bas (dans le patch de base, il est une octave plus haut) : les deux réglages sont écrits.
- **Utilité pour une recette** : la fiche « hollow FM » et la variante FM bass Future House peuvent reprendre directement FM (B) 30 %, ENV 2 50 % / 150 ms et MG Low 24.

### F07-01 Wobble Bass in Serum 2: LFO Basics That Still Slap — Maxim Hetman, Monosounds.studio (Serum 2, 03/08/2026)
- **Statut** : page lue le 05/10/2026 (HTTP 200).
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : Init, scie sur Osc A, une voix au départ (unison en option), une octave plus bas.
  - Filtre : passe-bas, cutoff vers **200 Hz**.
  - LFO : LFO 1 glissé sur le cutoff avec une quantité généreuse (du sombre au brillant), tempo-synchronisé à **1/4**.
  - Vitesses : **1/4** pour le « slow dubstep lurch », **1/8** pour le « classic wub », **1/16** pour le « talking ». On peut automatiser 1/4 → 1/8 → 1/16 sur une phrase.
  - Forme du LFO : montée plus lente que la descente (« swell » puis « snap »), plus « vocale ». Un petit cran au milieu de la forme donne un bégaiement dans chaque wub.
  - Plage : du LFO de **≈150 Hz à 1-2 kHz**, plutôt que toute la course du filtre.
  - Retrigger : retrigger pour les riffs courts et les stabs « riddim » ; free-running (ou calé sur la position du morceau) pour les wobbles tenus.
  - Grain par FM : sinus sur Osc B, une ou deux octaves plus bas, en FM vers A. Le même LFO pilote cutoff et quantité de FM. Le pack « Skrillex-inspired » de l'auteur envoie un LFO vers deux ou trois cibles : cutoff, FM, WT position.
  - Grain par distortion : distortion après le filtre, puis EQ dans la chaîne pour maîtriser **3-5 kHz**.
  - Sub : sinus séparé une octave plus bas, soit sur un oscillateur qui contourne le filtre, soit sur sa propre piste. Le wobble reste au-dessus de **≈100 Hz**.
- **Conseils de jeu ou de mix** :
  - Sidechain de la couche wobble au kick.
  - Retirer quelques dB vers **300-500 Hz** si le son devient « boxy ».
  - Écrire le rythme du wobble contre la batterie, pas sur elle.
  - En slap house et en bass house, le même geste se fait plus vite, plus serré, avec plus de sidechain (affirmation de la page : « every professional bass house record is built this way » pour la séparation du sub).
- **Limites** :
  - Aucune valeur de quantité de LFO ni de résonance.
  - Le type de filtre n'est pas nommé.
  - Les exemples audio sont des presets du vendeur (non écoutés).
- **Utilité pour une recette** : divisions de LFO et plage 150 Hz-2 kHz pour la fiche wub ; la règle « sub hors du LFO » confirme la séparation sub / mid.

### F02-02 How to Create a Reese Bass in Xfer Serum – Sound Design Techniques — ADSR Sounds, auteur non nommé (Serum 2 dans le texte, date non donnée)
- **Statut** : page lue le 05/10/2026 (HTTP 200). L'adresse garde l'ancien slug « how-to-make-a-reese-bass-more-unique-in-serum ».
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : Init, scie sur Osc A, une ou deux octaves plus bas selon la tonalité.
  - Unison : **5, 7 ou 9** voix (impair, pour qu'une voix reste au centre), Detune **10-14 %**, Mono et un peu de glide.
  - LFO : LFO 1 module légèrement le cutoff et le detune, BPM sync **off**, vitesses lentes.
  - Couches :
    - Osc B en scie ou en table « fifth harmonic », une octave plus bas, niveau à doser ;
    - Sub Oscillator activé et **routé dans le même passe-bas** ;
    - en option, Noise (vinyle, vent, field recording).
  - Filtre : MG Low 12 ou 24, Drive et Fat pour l'épaisseur, un peu de résonance. Le « dual-filter » de Serum 2 permet par exemple un sub propre sur Filter A et un mid sale sur Filter B.
  - FX :
    1. Distortion Tube ou Diode.
    2. Compressor en mode Multiband.
    3. Chorus ou Dimension pour la largeur, « en gardant la basse mono sous 120 Hz ».
    4. EQ : accentuation **80-120 Hz**, creux vers **250 Hz**.
  - Ressampler le son et le réimporter comme wavetable.
- **Conseils de jeu ou de mix** : unison impair, moduler warp ou position de table, combiner FM from B et sub pour le poids.
- **Limites** :
  - Le titre H1 dit « Xfer Serum », le texte dit « Serum 2 ». L'image d'illustration date de 2019/02 : la page a probablement été réécrite.
  - Aucune quantité de LFO, de drive ni de mix.
  - Le moyen de garder le mono sous 120 Hz n'est pas expliqué.
  - **Contradiction** : le sub passe dans le filtre ici, alors que F04-01 et GEN-06 le sortent en direct.
  - Texte générique, sans capture ni audio.
- **Utilité pour une recette** : seuls repères chiffrés pour le Reese : unison 5/7/9 et detune 10-14 %. Le reste est à valider.

### F04-01 Deep House Organ Bass In Serum — Echo Sound Works, publiée par ADSR Sounds (Serum 1 d'après la date, non dite ; image d'illustration déposée en 2015/06)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo intégrée (YouTube `_ls-4YZkIv0`) non visionnée.
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : choisir des wavetables « pas trop agressives », sans quoi le son tourne à la basse électro. La wavetable de l'auteur est proposée en lien Dropbox (« ACVSTI Bad Signs.wav »), non téléchargée.
  - Sub : sous-oscillateur sur la sortie **DIRECT OUT**, hors filtre et hors FX.
  - Filtre : cutoff modulé par une enveloppe, pour que le son « respire » sans trop d'aigus. Filtre « multi stage » (passe-bas et peak) pour ajouter des harmoniques.
- **Conseils de jeu ou de mix** : aucun au-delà de ce qui précède.
- **Limites** : aucune valeur dans le texte, tout est dans la vidéo. **À traduire dans Serum 2** : nom du filtre « multi stage » et sortie directe du sub, à vérifier dans l'interface.
- **Utilité pour une recette** : principe d'organ bass deep house (table douce, sub en direct, enveloppe sur le cutoff), sans chiffres.

### F04-02 Korg M1 Bass (Robin S "Show Me Love" Bass) — ADSR Sounds, auteur non nommé (Serum 1 d'après la date, non dite ; image déposée en 2015/04)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo intégrée (YouTube `IU_FhNGu62A`) non visionnée. Fichiers du projet en zip (`ADSR_SRM_DD_SML.zip`), non téléchargés.
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : wavetable personnalisée, échantillonnée sur la forme d'onde **« Organ 2 »** du Korg M1, prise dans la version VST du M1. Selon la page, le son original est cette forme d'onde « practically unprocessed ».
  - Macros : une macro transforme le son en « horn pluck » de « Rattle » (Bingo Players). La valeur et les cibles ne sont pas écrites.
- **Conseils de jeu ou de mix** : aucun.
- **Limites** :
  - Aucun réglage chiffré.
  - La table dépend d'un fichier à télécharger.
  - **À traduire dans Serum 2.**
- **Utilité pour une recette** : confirme la source du timbre (M1 Organ 2 presque brut) pour la fiche organ bass. La recette elle-même reste dans la vidéo ou le zip.

### F03-06 Modern future house bass — ADSR Sounds, auteur non nommé (Serum 1 d'après la date, non dite ; image déposée en 2015/04)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Elle intègre la vidéo YouTube **`QXJIHAtlnP8`**, celle que `sources.md` recense déjà : l'hypothèse du registre est **confirmée**. Zip du projet (`ADSR_SRM_DD_FHB.zip`) non téléchargé.
- **Gestes et réglages écrits, dans l'ordre** :
  - Contexte : la basse Future House ou Deep House descend de la « hollow bass » du UK Garage. Le son original : **deux sinus en FM**.
  - Oscillateurs : un oscillateur en **carré** pour le creux ; l'autre avec une onde riche, pour la superposition et comme **source de FM**. Deux tables personnalisées de l'auteur : une « hollow », une riche en harmoniques.
- **Conseils de jeu ou de mix** : préparer le patch avec soin pour qu'il reste « flexible ». Pas de détail.
- **Limites** : aucune valeur. **À traduire dans Serum 2.**
- **Utilité pour une recette** : architecture de la fiche hollow : carré pour le creux, second oscillateur comme modulateur FM.

### F05-14 Self sync warp mode to make a thick saw bass — ADSR Sounds, auteur non nommé (Serum 1 d'après la date, non dite ; image déposée en 2015/04)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo intégrée (YouTube `0Ss-SkWqUVg`) non visionnée.
- **Gestes et réglages écrits** :
  - C'est le premier épisode d'une série de quatre : scie épaisse par synchronisation d'oscillateur (warp Sync), puis conversion du son en « wave frame » réimportée dans Serum.
  - Deux types de « thick saw bass » sont distingués :
    - la scie multi-voix **non redéclenchée** ;
    - la scie dont le **fondamental est renforcé par un sinus**.
  - L'épisode suivant traite le warp Sync.
- **Conseils de jeu ou de mix** : aucun.
- **Limites** :
  - Aucune valeur.
  - La page est en partie une annonce de masterclass.
  - **À traduire dans Serum 2** : nom du mode Sync (F03-04 liste « Sync » dans le menu warp de Serum 2).
- **Utilité pour une recette** : typologie utile pour la fiche « saw percussive » (multi-voix libre contre scie et sinus), sans réglages.

### F11-17 Huge Sounds With FM Warp Mode In Serum — Echo Sound Works, publiée par ADSR Sounds (Serum 1 d'après la date, non dite ; image déposée en 2015/04)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo intégrée (YouTube `vX9JnDhaFx0`) non visionnée.
- **Gestes et réglages écrits** : de grosses basses faites sans quitter la section oscillateurs, par le warp FM. Selon la page, le warp FM fait entrer « n'importe quelle basse » dans le dubstep, l'electro ou la complextro.
- **Conseils de jeu ou de mix** : aucun.
- **Limites** : deux phrases seulement, aucune valeur. **À traduire dans Serum 2** (voir F03-04 pour le menu FM de Serum 2).
- **Utilité pour une recette** : nulle sans la vidéo.

### F05-12 How to Make Bass House: The Ultimate Guide for Producers (2025) — Simon Haven, EDMProd (Serum, version non dite ; publiée le 09/08/2024, mise à jour le 23/05/2025)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo YouTube `tJ-us3FCW94` non visionnée.
- **Gestes et réglages écrits, dans l'ordre** :
  - Cadre : bass house entre **125 et 130 BPM**, réglée à **128**. Morceau de référence : « NRG » (Julian Jordan, Eleganto, feat. Kota).
  - Structure par blocs de **8 mesures** : Intro 8, Intro développée 8, Breakdown hook 8, Build 8, Drop 1A 8, 1B 8, 1C 8, Interlude 2, Breakdown 8, Build 8, Drop 2A 8, 2B 8, 2C 8, Outro 16.
  - Batterie :
    - kick « punchy, mais moins qu'un kick tech house », avec peu de grave ;
    - deux couches de kick alignées en phase, passées dans le clipper KClip Zero, puis ressamplées sur un temps ;
    - léger fondu d'entrée si le kick claque trop ;
    - clap en deux ou trois couches, dont une légèrement retardée ;
    - hat ouvert à sustain 0 dans Simpler.
  - Écriture : pattern écrit d'abord sur un sinus simple, en **E phrygien**.
  - Enveloppe : sustain baissé, release allongée, pour un son « plucky ».
  - Filtre : LFO 1 en mode **Envelope** glissé sur le cutoff de « Filter A ». Forme, cutoff, drive et résonance sont à régler à l'oreille.
  - FM : Osc B en Basic Shapes, niveau à zéro. Sur Osc A, « FM from B » est monté. LFO 2 → quantité de FM, avec modération.
  - Modulateur monté de **2 octaves et 7 demi-tons**.
  - Boutons « Rand » à **zéro** pour un son constant.
  - Post-traitement : OTT, EQ, distortion, sidechain, largeur (sans valeurs).
  - Variante du Drop 1B : l'octave du sinus modulateur passe de **2 à 3 octaves**.
- **Conseils de jeu ou de mix** :
  - Combler les trous du pattern par d'autres basses (presets Splice, « laser »), en appel et réponse.
  - Pitch bend dessiné dans l'enveloppe de clip de Live (MIDI Ctrl › Pitch Bend) pour donner de l'attaque à la première note d'un motif.
- **Limites** :
  - Le vocabulaire est celui de Serum 1 (« FM from B », « Filter A », « Rand ») : **à traduire dans Serum 2** (F03-04 décrit le menu warp FM de Serum 2, étiquette « FM (B) »).
  - Valeurs du filtre et de l'enveloppe en image, non lues.
  - La page renvoie à la vidéo pour les étapes sautées.
  - Le registre annonçait « des presets Serum » : la page propose un téléchargement gratuit du projet Live et des presets Serum, non fait.
- **Utilité pour une recette** : la FM « osc B à +2 oct +7 demi-tons, niveau 0, passée à +3 oct au drop B » est le geste bass house chiffré ; structure par blocs de 8 mesures.

### F01-13 Sub-Bass: How To Get Thick Low-End In Your Music — Aden Russell, EDMProd (Serum, version non dite ; publiée le 17/11/2021, mise à jour le 02/05/2023)
- **Statut** : page lue le 05/10/2026 (HTTP 200).
- **Gestes et réglages écrits, dans l'ordre** :
  - Plage du sub : **25-80 Hz**.
  - « Power Zone » : notes **F0-A0**, où l'on « sent ET entend ». D'où les tonalités de fa mineur, fa dièse mineur et sol mineur. Plus bas (C0-E0), tous les subwoofers ne suivent pas.
  - Sub sinus propre : un simple sinus.
  - Sub saturé, première méthode : sinus Basic Shapes, puis Distortion en mode **Soft Clip**.
  - Sub saturé, seconde méthode : frame **carré** de Basic Shapes dans le passe-bas, cutoff et résonance à l'oreille (réglage final en image, non lu).
  - Attention : le fondamental faiblit avec la distorsion. Réduire le drive ou ajouter un second sub propre.
  - Sidechain du sub au kick par compresseur : attack **3-10 ms** (plus court, cela clique si l'attaque est plus brève qu'un cycle), release **50-150 ms**.
  - Phase : aligner la phase du sub sur la basse qui partage le même fondamental (exemple d'un décalage de 180°, corrigé par la phase de l'oscillateur dans Serum).
  - Vérifier les notes une ou deux octaves plus haut, puis redescendre.
  - Passe-haut sur les autres pistes.
- **Conseils de jeu ou de mix** : voir ci-dessus. Plug-ins cités : SubLab, SubBoomBass, X-Sub.
- **Limites** :
  - La convention d'octave n'est pas précisée et aucun Hz n'est donné pour F0-A0. En notation Live (C3 = 60), F0-A0 = 43,7-55 Hz. En notation scientifique, 21,8-27,5 Hz, ce qui sort en partie de la plage 25-80 Hz annoncée. La lecture Live est la plus cohérente, mais **à confirmer**.
  - Le registre annonçait « sous-oscillateur de Serum : sinus, triangle, rectangle arrondi » : **ce passage n'apparaît pas** dans le texte lu.
  - Toutes les captures Serum et compresseur sont en image.
  - Vocabulaire Serum 1 (Basic Shapes, Soft Clip) : **à traduire dans Serum 2.**
- **Utilité pour une recette** : chiffres de sidechain sub (3-10 ms / 50-150 ms) et règle de vérification à l'octave pour la fiche sub.

### F15-01 Serum 2 Clip Sequencer: The Complete Guide — Sam Matla (texte adapté de la vidéo de « John », EDMProd) (Serum 2, 05/09/2026)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo YouTube `AbsBTo2l500` non visionnée. Les captures portent le minutage de la vidéo.
- **Gestes et réglages écrits, dans l'ordre** :
  - Module Clip : piano roll en bas de Serum 2. La lecture suit la position du transport du DAW.
  - Exemple : pattern « roulant » autour d'une note grave répétée, avec quelques notes plus hautes.
  - Length de 1 à 2 mesures, duplication (Cmd+D).
  - **Boucle de 3 temps** contre un kick en 4/4 : les accents de la basse tournent contre le kick (2:00).
  - Expression X : dessinée par note, puis clic droit sur le paramètre du filtre › Mod Source › MPE › Expression X, et réglage de la quantité (2:45).
  - Vélocité : sans effet tant qu'elle n'a pas de destination. L'auteur la route vers le niveau de l'oscillateur (10:18).
  - Chance : par note (10:43).
  - Variations par Option-glisser vers un autre emplacement (3:06). Edit All s'applique à tous les clips.
  - Launch Quantization en 1/16 ou Bar (4:41). Retrig fait repartir le clip au début (5:51). Note Gate fait jouer le clip tant que la touche est tenue.
  - Réglage de départ conseillé : **Mono + Bar + Retrig**, Note Gate off.
  - Rate : BPM on pour suivre le tempo, triolet ou pointé (6:32).
  - Mode Poly : deux clips ensemble, le second transposé de **+24 demi-tons** (8:06).
  - Courbes de hauteur dessinées entre les notes, Option pour courber (8:43). Avec la scie du tutoriel, cela donne un « acid-like character ».
  - MIDI Input Trigger Octave : passé de −2 à −1 (9:36).
  - Record, puis Quantize (Cmd+Q) après avoir choisi la grille, en croches dans l'exemple (13:49-14:50). Overdub et Extend.
  - Lock Module pour garder la séquence en changeant de preset (11:39). Set as Preview Clip.
- **Conseils de jeu ou de mix** : peu de glissés, entourés de notes stables. Garder fiables les notes d'ancrage et baisser la chance des notes de passage. Changer un réglage à la fois.
- **Limites** : aucun réglage de son (le patch « Big Wobber Bass » n'est pas détaillé). Valeurs de quantité et de courbe en image, non lues.
- **Utilité pour une recette** : faire une basse roulante polymétrique (boucle de 3 temps) et des glissés dessinés dans Serum 2 sans toucher au clip Live ; Lock Module pour comparer des presets sur la même ligne.

### GEN-07 Serum 2 Arpeggiator: The Complete Guide to Patterns, Expression & Glide — Sam Matla (texte adapté de la vidéo de « John », EDMProd) (Serum 2, 06/09/2026)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Vidéo YouTube `6QrKPPZkWRc` non visionnée.
- **Gestes et réglages écrits, dans l'ordre** :
  - Module ARP : bouton d'alimentation, Shape (Up, Down, Up/Down, Converge/Diverge, Played, Chord, Random, Random sans répétition, Pattern). Selon la page, l'ARP n'existe pas dans Serum 1.
  - Rate en BPM ou en Hz. Exemple : projet à 140 BPM, pattern à **1/2x**, soit 70 BPM de pattern (7:10).
  - Pattern : les rangées sont des **index** des notes tenues (0 = la plus basse), pas des touches.
  - Grille fine en **1/32** (9:56). Length passée de 1 à 4 mesures. Notes empilées pour faire des accords.
  - Accent : agit sur la vélocité, sans effet sans routage. VELO → niveau d'oscillateur (5:01) ou VELO → cutoff du filtre, pour une couleur acid (5:20).
  - Expression X par pas → cutoff (5:56-6:15), puis → **Decay** de l'enveloppe d'amplitude.
  - Courbes de hauteur par note (7:20).
  - Strum : il faut des notes empilées. Save Pattern…
  - Mode : Normal, Reverse, Pendulum, aléatoire, One Shot, Static.
  - Step Mode : Normal, Chord, et modes « new ». « New Only » demande une nouvelle note entrante au moment du pas (renvoi au Serum 2 User Guide, p. 251).
  - Wrap :
    - Range 0 : C1 E♭1 G1 C1 E♭1 G1 ;
    - **Range 1, Pitch 12** : C1 E♭1 G1 C2 E♭2 G2 ;
    - Pitch 24 : deux octaves.
  - Transpose : Shift 12 / Range 1, puis Range 2 (13:37).
  - Boucle de **six doubles croches** (14:03).
  - Launch Quant sur la mesure, Edit All, Latch.
  - Playback : Offset, Repeats, Gate, Chance.
  - **Gate 200 %** : notes deux fois plus longues, qui se chevauchent. Avec **Porta**, le glide relie les notes (17:08-17:25).
  - Chance globale **50 %** (17:49).
- **Conseils de jeu ou de mix** :
  - Commencer avec un son simple et une release courte.
  - Un seul système de hauteur à la fois.
  - Avec un patch mono, les notes empilées ne sonnent pas en accord, ce qui peut servir une ligne de basse.
- **Limites** :
  - Les octaves suivent l'affichage de Serum, et la page prévient que le DAW peut numéroter autrement.
  - Pas de patch de basse détaillé.
  - Page centrée sur le jeu plutôt que sur le son.
- **Utilité pour une recette** : « Gate > 100 % + Porta » pour une basse arpégée glissante, et vélocité → cutoff pour des accents acid.

### Hors registre (edmprod.com/ott-plugin/) OTT Plugin: Why Does It Sound SO Good? + Free Download — Aden Russell, EDMProd (pas un tutoriel Serum : plug-in OTT de Xfer, « version 2022 », et préréglage OTT de Multiband Dynamics d'Ableton ; 05/07/2023)
- **Statut** : page lue le 05/10/2026 (HTTP 200). URL **hors registre**.
- **Gestes et réglages écrits, dans l'ordre** :
  - Préréglage OTT de Multiband Dynamics (Live) :
    - crossover bas/médium à **88,3 Hz** (au lieu de 250 Hz par défaut) ;
    - gain d'entrée **+5,2 dB** par bande ;
    - bandes « above » : Highs à **∞:1** ; Mids et Lows écrits « **1:66.7** » (sic), présentés comme une forte limitation ;
    - bandes « below » à **4:1** ;
    - seuils très bas ;
    - gains de sortie : **+10,3 dB** en grave et en aigu, **+5,7 dB** en médium.
  - Plug-in OTT :
    - Depth (dry/wet), Time (attack et release des trois bandes), In/Out gain ;
    - bandes fixes : Lows sous **88,3 Hz**, Mids de 88,3 Hz à **2,5 kHz**, Highs au-dessus de 2,5 kHz ;
    - boutons Upward et Downward (exemple : Downward à 62 %) ;
    - Ctrl+clic sur une bande pour la désactiver, par exemple pour laisser le grave intact.
  - Usages :
    - batterie à 30 % ;
    - guitare à 39 % ;
    - foley à 100 % ;
    - master : pas plus de **20 %**, ≈10 % d'habitude, 16 % dans l'exemple.
- **Conseils de jeu ou de mix** :
  - Sur les leads et les basses, l'OTT amplifie le mouvement (sweeps, hauteur, volume) : prévoir ce mouvement dans le patch.
  - Baisser l'Out pour comparer à niveau égal.
  - Mélanger avec Depth.
- **Limites** :
  - « 1:66.7 » est écrit tel quel (probablement 66,7:1).
  - Plusieurs réglages sont en capture.
  - Multiband Dynamics est un **effet natif de Live** : la règle 5 d'`AGENTS.md` exclut d'en ajouter dans une chaîne de mix, il faut passer par le plug-in OTT de Xfer.
- **Utilité pour une recette** : la bande basse s'arrête à 88,3 Hz. Pour une basse médium en OTT, désactiver ou doser la bande basse pour ne pas pomper le sub.

### F01-06 808 Bass with Saturation — Attack Magazine, série Synth Secrets, auteur non nommé (le compte technique est « ericadmin ») (Serum 1 d'après la date, non dite ; 23/06/2017, modifiée le 10/07/2020)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Les extraits audio MP3 n'ont pas été écoutés.
- **Gestes et réglages écrits, dans l'ordre** :
  - Oscillateurs : Init, Osc A sur **Analog › Analog_BD_Sin**. Detune, Blend et Rand à fond à gauche.
  - Env 1 : attaque un peu lente contre les clics, release assez longue. Valeur en image, non lue.
  - Env 2 vers le **Semitone** d'Osc A : chute de hauteur vers la note. Valeurs en image, non lues ; d'après les commentaires, la capture d'Env 2 était fausse et a été corrigée le 03/07/2017.
  - Voicing **mono**, portamento **≈300 ms**.
  - Filtre : on retire des aigus et on épaissit avec **FAT** et **DRIVE**, « to taste ». Type non nommé.
  - FX : Distortion **Tube**, avec son filtre **HP** pour épargner le sub, Q baissé, DRIVE et MIX légers. Valeurs en image, non lues.
  - WT POS d'Osc A vers **209**.
  - Hors Serum : FabFilter Saturn multibande séparé à **123 Hz**, Warm Tape sur les deux bandes, beaucoup moins de drive en bas. Puis EQ UAD Neve 31102 « assez extrême » (valeurs en image).
- **Conseils de jeu ou de mix** : un son qui prend beaucoup de place, à mixer avec le kick ; un peu de sidechain s'il envahit le grave.
- **Limites** :
  - Les enveloppes, le filtre et la distortion ne sont chiffrés qu'en image.
  - Pas de notes MIDI (un lecteur les réclame dans les commentaires).
  - **À traduire dans Serum 2** : table Analog_BD_Sin, mode Tube et filtre HP de la distortion, FAT, à vérifier.
- **Utilité pour une recette** : 808 tech house : table Analog_BD_Sin, porta 300 ms, WT POS 209, puis saturation séparée à 123 Hz ; repère pour une basse « tech » sous 124 BPM.

### F07-23 How to use Serum's effects to boost a bass sound — Computer Music, MusicRadar (Serum 1 : plug-in **Serum FX**, non le synthé ; 25/06/2020)
- **Statut** : page lue le 05/10/2026 (HTTP 200).
- **Gestes et réglages écrits, dans l'ordre** :
  1. **Serum FX** sur la piste de basse, et une piste MIDI routée vers lui pour déclencher la modulation. Filter en type **L/B/H24**.
  2. Cutoff ≈ **300 Hz**, Resonance ≈ **50 %**, Drive et Morph ≈ **30 %**, ce qui retire un peu de sub.
  3. **Note Latch** on. LFO 1 → cutoff à **+10**, Rate LFO 1 à **1 bar**, LFO 1 → Morph à **−20**.
  4. Compressor **après** le filtre : attack et release ≈ **50-60 ms**, seuil réglé pour ≈ **4 dB** de réduction, ≈ **1 dB** de makeup.
  5. Distortion après le compresseur, mode **Downsample**, mix **50 %**. LFO 1 → Drive, en sens inverse (le drive baisse quand le LFO monte).
  6. Velocity → Resonance **+40**, Velocity → Drive **+20**. Macro 1 sur le Wet/Dry de chaque effet.
- **Conseils de jeu ou de mix** : le compresseur rattrape la dynamique « imprévisible » créée par la modulation.
- **Limites** :
  - Captures en image.
  - Les unités « +10 », « −20 », « +40 » sont des quantités de matrice sans échelle précisée.
  - Il s'agit de **Serum FX** sur de l'audio : **à traduire dans Serum 2**, nom du filtre multimode et du mode Downsample à vérifier.
  - Le registre classait cette page en wub (F07). C'est plutôt un traitement d'une basse existante.
- **Utilité pour une recette** : chaîne filtre → compresseur → downsample chiffrée, pour salir une basse médium en gardant un sub séparé.

### F01-12 How to create a huge sub bass sound — Future Music, MusicRadar (Serum 1 d'après la date, non dite ; 07/05/2015)
- **Statut** : page lue le 05/10/2026 (HTTP 200). Les étapes 3 à 6 sont dans le HTML hors du flux principal ; elles ont été relevées.
- **Gestes et réglages écrits, dans l'ordre** :
  1. Éditeur de wavetable d'Osc A : huit pas au maximum, huit au minimum, ce qui donne un **carré**.
  2. Nouvelle frame : tous les pas au minimum sauf le premier, ce qui donne une **impulsion de 12,5 %**. Morph › **Morph - Spectral**.
  3. WT POS d'Osc A à **1**. Matrice : LFO 1 → Osc A › A WTPos.
  4. Amount **8**, « pas trop mince mais en mouvement ». LFO 1 : BPM désactivé, Rate **3,9 Hz**.
  5. Filtre activé avec **keytracking** (icône clavier), Cutoff **374 Hz**, Res **23 %**, Drive **10 %**.
  6. **Mono**. Env 1 : Attack **0,8 ms**, Release **27 ms**, contre les clics.
- **Conseils de jeu ou de mix** : un sub sinus convient quand le grave est déjà chargé ; s'il reste de la place, un timbre riche filtré donne plus de poids.
- **Limites** :
  - Pas d'indication de niveau ni de type de filtre.
  - **À traduire dans Serum 2** : éditeur de table, Morph - Spectral, keytracking du filtre.
  - Ce sub est **animé**, à l'opposé du sub mono stable que demande la règle du projet : à réserver à un sub seul sans basse médium.
- **Utilité pour une recette** : recette de sub « harmonique » entièrement chiffrée (carré → impulsion 12,5 % en morph spectral, LFO 3,9 Hz à 8, cutoff 374 Hz keytracké).

### F05-02 This Slept-On Effect Makes Tech House Bass Sound Filthy (titre enrichi : « Gritty Tech House Bass Design in Serum 2 ») — Zen World, page de musicproductiontutorials.co.uk (Serum 2 d'après le titre enrichi ; page du 14/09/2026, vidéo de 11:10)
- **Statut** : page lue le 05/10/2026 (HTTP 200). **Résumé écrit d'une vidéo, vidéo non visionnée** (YouTube `UxXCeAcmO7g`).
- **Ce que la page écrit** :
  - Une scie simple rendue « gritty » et agressive par une **réverb à convolution** et de la **distortion** dans Serum 2. Puis synthèse soustractive, compression multibande par **OTT**, bitcrush par **sample-and-hold**, transitoire par enveloppe. Inspiration revendiquée : l'approche « punk » de Julian Jordan.
  - Plug-ins et minutage : Serum (0:00), iZotope **Trash** (2:31), Xfer **OTT** (3:02).
  - Étiquettes minutées :
    - convolution 1:14 et 5:54 ;
    - distortion 2:29 et 6:52 ;
    - OTT 3:02 et 7:43 ;
    - bitcrushing 4:02 et 8:41 ;
    - passe-bas 5:16 ;
    - soustractive 5:22 ;
    - enveloppe 5:27 et 9:56 ;
    - EQ 7:14 ;
    - automation 8:10.
  - Genres : House, Tech House, Progressive House. DAW : Ableton Live.
- **Conseils de jeu ou de mix** : aucun au-delà du résumé.
- **Limites** : aucune valeur. Les étiquettes sont produites par l'agrégateur, sans doute à partir de la transcription. Trash est un plug-in tiers, peut-être absent du Mac.
- **Utilité pour une recette** : ordre des gestes à vérifier dans la vidéo (convolution → distortion → OTT → S&H → enveloppe). Minutages prêts pour l'étude.

### F05-06 How to Make Chris Lorenzo "Hell Yeah" Bass in Serum 2 (titre enrichi : « Chris Lorenzo "Hell Yeah" Bass Sound Design in Serum 2 ») — Sam Smyers, page de musicproductiontutorials.co.uk (Serum 2 ; page du 13/02/2026, vidéo de 7:34)
- **Statut** : page lue le 05/10/2026 (HTTP 200). **Résumé écrit d'une vidéo, vidéo non visionnée** (YouTube `PKbxm5mjgOY`).
- **Ce que la page écrit** :
  - Basse « gritty » de « Hell Yeah », construite de zéro dans Serum 2, avec l'accent sur la **saturation**. Superposition, puis sidechain par **Kickstart** (Nicky Romero).
  - Morceau : « Hell Yeah », **130 BPM** selon la page.
  - Chapitres : Intro (0:00), Verse Bass (0:51), Chorus Bass Pluck (2:27), Chorus Bass Stab (3:44), **Using Per Voice Phase** (4:59).
  - Plug-ins : Serum (0:00), **Kontakt** (1:32), Kickstart (2:35).
  - Étiquettes :
    - soustractive 0:46 et 3:00 ;
    - sampling 0:56 ;
    - EQ et passe-bas 2:04 ;
    - filtrage 3:18 et 4:24 ;
    - soft clipping 3:30 et 4:39 ;
    - stabs 3:42 ;
    - unison et detune 4:12, 4:22 et 5:06 ;
    - passe-haut 4:44 ;
    - réverb Hall 4:47 ;
    - compatibilité mono 4:49 ;
    - ressampling 5:32 et 7:06 ;
    - LFO 6:03.
- **Conseils de jeu ou de mix** : sidechain par Kickstart (sans valeur).
- **Limites** : aucune valeur. Le rôle de Kontakt (couche échantillonnée ?) n'est pas expliqué. Kickstart n'est peut-être pas installé.
- **Utilité pour une recette** : trois basses distinctes (couplet, pluck de refrain, stab) et un chapitre sur la phase par voix à regarder en priorité.

### F05-03 The Secret Behind Mau P's Groovy Basslines | "Just a Little Bit More" Tutorial (titre enrichi : « Mau P Groovy Bassline Technique in Serum ») — Sam Smyers, page de musicproductiontutorials.co.uk (Serum, version non dite ; page du 04/09/2026, vidéo de 13:50)
- **Statut** : page lue le 05/10/2026 (HTTP 200). **Résumé écrit d'une vidéo, vidéo non visionnée** (YouTube **`KUzOJprH6nc`**).
- **Ce que la page écrit** :
  - La ligne glissante de Mau P vient de notes **legato qui se chevauchent** combinées au **portamento**. Patch Serum : modulation de wavetable, enveloppe, distortion **Tube**, et **Kickstart** utilisé pour **retirer les transitoires d'attaque**.
  - Chapitres :
    - Intro (0:00) ;
    - Melodyne tips (0:37) ;
    - Synth tuning rant (2:30) ;
    - Overlapping notes in MIDI (4:05) ;
    - Importance of Legato (4:59) ;
    - décomposition de la basse de « Just a Little Bit » dans Serum (6:17) ;
    - basse de « Neck » (8:30) ;
    - basse de « Like I Like It » (10:20).
  - Plug-ins : Melodyne (1:05), Serum (1:46), Kickstart (1:56).
  - Morceaux : « Neck » **129 BPM**, « Like I Like It » **128 BPM**, « Just a Little Bit More » (tempo non donné).
  - Techniques étiquetées : automation, chorus, distortion, EQ, superposition, sidechain.
- **Conseils de jeu ou de mix** : chevaucher les notes MIDI et activer legato et portamento ; Kickstart pour adoucir l'attaque.
- **Limites** :
  - Aucune valeur de portamento ni de patch.
  - **Contradiction avec le registre** : le registre pointe vers la vidéo `uOFNjMxiwkU` (titre « I Cracked That Mau P Bass — Just A Little Bit More »), alors que cette page intègre `KUzOJprH6nc` avec un autre titre. C'est peut-être une autre vidéo du même auteur : à vérifier avant de reporter dans `sources.md`.
- **Utilité pour une recette** : confirme le geste « chevauchement + legato + portamento » (même mécanisme que F01-02) pour une basse tech house groovy à 128-129 BPM.

### F03-01 How To Make a Future House Bass Patch in Serum — Academy.fm (Dan Larsson selon le registre)
- **Statut** : **échec**.
  - `curl` renvoie HTTP **530**, avec le corps « error code: **1016** » (Cloudflare, erreur DNS de l'origine), deux fois à quelques minutes d'intervalle. `academy.fm/` renvoie aussi 530.
  - WebFetch est refusé par le proxy (« EGRESS_BLOCKED »).
  - Aucun contournement tenté.
- **Gestes et réglages écrits** : aucun (page non lue).
- **Limites** : tout reste à lire. Réessayer plus tard ou sur le Mac.
- **Utilité pour une recette** : aucune pour l'instant.
