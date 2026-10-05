# Sampling avec Maschine : synthèse de 30 tutoriels

Synthèse du corpus `tutoriels-sampling-maschine.md` (MA-01 à MA-30), rédigée le 05/10/2026. L'étude a été faite dans Claude in Chrome sur le Mac : transcriptions, descriptions et chapitres lus, son coupé. **Rien n'a été entendu** : aucun résultat sonore n'est confirmé ici, seulement ce que les vidéos disent. [SOURCE MA-xx] marque ce qui est dit ; (interp.) marque une interprétation ; [ASR ?] une transcription automatique douteuse. Versions : 6 vidéos sont explicitement sur Maschine 3 (MA-01 à MA-05, MA-25) ; MA-17 l'est probablement ; les autres sont sur Maschine 2 ou l'OS Maschine+. Matériel filmé : MK3, Maschine+, logiciel seul ; MA-24 date de 2017 (avant la MK3) ; aucune vidéo sur Mikro. L'installation du projet est Maschine 3.6.0 avec MK3 : tout chemin se vérifie à l'écran avant d'être suivi.

## Ce que dit le corpus avant tout

- Le flux est le même d'une version à l'autre : bouton **Sampling**, puis pages Record, Edit, Slice et Zone [SOURCE MA-01, MA-16]. Le corpus le note lui-même pour Maschine 2, Maschine+ et Maschine 3.
- Deux modules, deux rôles. **Audio** : boucles synchronisées au tempo, time-stretch en temps réel, pas de découpe. **Sampler** : slice, Zone, enveloppes, mais plus de synchro [SOURCE MA-14, MA-16, MA-18]. Passer d'Audio à Sampler perd le stretch ; le Tune devient un re-pitch [SOURCE MA-18].
- **Polyphony = 1** et **Choke group** reviennent dans presque chaque tutoriel de chop. Sans eux, les slices se superposent jusqu'à 8 fois [SOURCE MA-04, MA-07, MA-08, MA-19, MA-23, MA-30].
- L'édition de la page Edit est **destructive** : elle crée de nouveaux fichiers numérotés ; le slicing n'en crée pas [SOURCE MA-17]. Copier le sample sur un autre slot avant d'agir [SOURCE MA-06].
- Maschine 3 sépare un fichier en **4 stems** (vocals, drums, bass, other) placés dans un nouveau groupe [SOURCE MA-02, MA-04, MA-25]. Le module d'arrivée varie : Sampler ou Audio selon le point de départ [SOURCE MA-05].

## Gestes de base

| Geste | Comment | Sources |
|---|---|---|
| Ouvrir le sampler (logiciel) | Icône forme d'onde à gauche, sur un slot de Sound vide | MA-01 |
| Choisir l'entrée | Source « Internal Master » pour le master, ou entrée externe mono (« One Left » [ASR ?] = 1 L) ; activer **Monitor** | MA-01, MA-15 |
| Vérifier une entrée externe | Sound vide → Channel/MIDI → Input « In 1 L » ; regarder le niveau en Sampling ; remettre Input sur None ensuite (sinon son doublé) | MA-28 |
| Modes d'enregistrement | **Sync** : démarre avec le séquenceur ; **Detect** : démarre au-dessus d'un seuil ; **Loop** : boucle calée sur le morceau, attend la mesure suivante | MA-01, MA-13, MA-15, MA-26 |
| Choisir la plage en Loop | **Shift** + bouton : mesure de départ et durée | MA-26 |
| Resampling interne | Sampling → Source **Internal** → un groupe ou le Master ; pad vide sélectionné d'abord ; Start | MA-13, MA-16, MA-26 |
| Bounce par glisser | Glisser l'icône audio / forme d'onde (en haut à droite) sur un pad → nouveau module Audio, fichier imprimé | MA-05, MA-13, MA-18, MA-25 |
| Charger un fichier | Glisser dans une zone vide → nouveau slot ; MP3, WAV, FLAC, OGG en Maschine 3 ; Shift + Mute coupe la lecture | MA-04 |
| Audio → Sampler | Logiciel : petite flèche → Internal → Sampler. MK3 : Plug-in → encodeur → Instruments → Internal → Sampler. Aussi : **Shift + Browser** | MA-09, MA-14, MA-16, MA-26, MA-30 |
| Sampler → Audio | **Shift + Browser** → Audio → Load | MA-22 |
| Édition | Sampling → **Edit** : Truncate (start/end + Apply), Normalize, Reverse, Fade in/out | MA-01, MA-08, MA-15, MA-17 |
| Plages d'édition | Pages **Play range**, **Selection range**, **Loop range** ; molette 5 = zoom, molettes 1/2 = start/end | MA-17, MA-19 |
| Time-stretch imprimé | Edit → **Stretch** → Settings : Tune, Formant on/off, mode Beat (BPM) ou Free (%), Auto detect, Source BPM → New BPM, longueur → Apply | MA-06, MA-14, MA-16, MA-17, MA-18 |
| Plug-in Audio | Playback **Loop** ou **Gate** ; moteur Re-Pitch / Stretch / Formant (« Raw Pitch » par défaut dans MA-16, (interp.) même mode) ; Tune ; **Length** | MA-14, MA-16, MA-18, MA-22 |
| Slice : modes | Sampling → **Slice** : Manual (frapper les pads, Auto snap), Grid (valeur de note + BPM), Split (parts égales), Detect (sensitivity) | MA-09, MA-19, MA-23 |
| Slice : corrections | **Remove** (trop courte), **Split** (trop longue), **Delete all** ; flèche droite = page start/end par slice ; annuler : Cmd+Z ou Shift + pad 1 | MA-19, MA-16 |
| Apply | Dernière page : **Mono** (polyphonie 1 + choke 1), **Pattern** None / Create / Replace, **Single** ; vers un pad (Keyboard) ou un groupe (lettre clignotante) | MA-05, MA-09, MA-16, MA-19, MA-30 |
| Choke et voix en masse | Pad mode → maintenir **Select** → **All** → Choke group ; Plug-in → **Voices = 1** (ou Legato) | MA-08, MA-23 |
| Chop par duplication | **Duplicate** le pad, puis start/end différents sur chaque copie | MA-09, MA-21 |
| Page **Zone** | Zones mappées sur les notes ; tout sélectionner et déplacer ; étirer une zone sur plusieurs notes ; tune, gain, pan, start/end par zone | MA-14, MA-16 |
| Boucle interne | Sampling ou Zone page 2 → **Loop**, start au passage par zéro, **X-Fade** si clic ; seulement en enveloppe **ADSR** | MA-03, MA-14, MA-16 |
| Séparation de stems | Logiciel : bouton **Stems** sous la forme d'onde du Sampler. Matériel : Sampling → Edit → Stems → **Apply** ; progression affichée, on peut continuer à travailler | MA-02, MA-04, MA-05, MA-25 |
| Retrouver le WAV | Clic droit sur la forme d'onde → « Find in Finder » | MA-02 |
| Auto-sampler | Sampling page 1 → **Mode = Auto** (Maschine 2.15 / Maschine+ OS 1.4) : durée de note, durée de sample, source, canal MIDI, plage, vélocité, Auto loop | MA-28 |

## Valeurs dites

| Paramètre | Valeur | Source |
|---|---|---|
| Longueur d'enregistrement en Loop | 8 mesures | MA-01 |
| Resampling Sync | 4 bars | MA-13, MA-16 |
| Resampling Sync d'une boucle | 1 bar | MA-20 |
| Resampling Loop | à partir de la mesure 4, durée 4 bars | MA-26 |
| Split | 4 / 8 / 16 / 32 slices ; 16 retenu (MA-03, MA-05, MA-16), 8 (MA-07) | MA-09, MA-16, MA-19 |
| Grid | 1/4, 1/8, 1/16, 1/32 ; 1/16 pour garder les doubles-croches | MA-09, MA-19, MA-20 |
| Grid, BPM auto | 75 → x2 150 ou /2 37.5 | MA-09 |
| Detect, sensitivity | défaut 50 % ; 0 = aucun transitoire, 100 = tous | MA-09 |
| Detect, sensitivity choisie | 80 (break) ; ~70 % (boucle mélodique) ; 0,90 (a cappella, vidéo de 2017 : (interp.) autre échelle d'affichage) | MA-07, MA-14, MA-24 |
| Polyphony | 8 par défaut → 1 | MA-08, MA-14, MA-30 |
| Stretch boucle mélodique | Source 98 → New 140 BPM, Tune -5, Formant off, Beat, 8 mesures | MA-14 |
| Stretch boucle de voix | 100 → 108 BPM, Tune +3, Formant off, Beat, 2 mesures | MA-16 |
| Stretch vinyle | 79.3 → 90 BPM, Formant on | MA-15 |
| Stretch break | 84 → 74 BPM, Formant on | MA-06 |
| Stretch, BPM source corrigé | 112 détecté → 84 ; New BPM 82 ; Tune -5 | MA-17 |
| Stretch imprimé | New BPM 80, 4 mesures, Beat, Tune +7 | MA-18 |
| Stretch, BPM source faux | mode Free, 100 %, Tune -2 | MA-18 |
| Pads transposés à tempo constant | +1 et -2 demi-tons (un Stretch par pad) | MA-18 |
| Length du plug-in Audio | 16 = tempo normal ; 32 = moitié ; valeur en temps | MA-18 |
| Tune de chops | +3 (MA-04, MA-16, MA-24) ; +8 en Keyboard (MA-04) ; -2 (MA-13) ; +12 (MA-16) | voir colonne |
| Première slice en Keyboard | C-2 (notation Maschine ; MA-16 [ASR ?]) | MA-14, MA-16 |
| Ride resamplée | ADSR, sustain 0, decay 2.3 s ; +1 demi-ton | MA-07 |
| Decimort sur le master | bit depth 12 | MA-07 |
| Beat Delay | 1/16, mix 3–4 % (MA-14) ; 2/16 [ASR ?] (MA-16) | MA-14, MA-16 |
| Filtres de groupe | low-pass ~2000 Hz ; second filtre ~3 400 Hz (type [ASR ?]) | MA-03 |
| Kicks détunés | +4 ; +25 [ASR ?] | MA-03 |
| LFO du Sampler | Speed 38 [ASR ?], Sync « lock » [ASR ?], sur Pitch | MA-03 |
| 808 | polyphonie « A » [ASR ?] ; hold [valeur ASR ?] | MA-03 |
| EQ de groupe | coupe-bas 100 Hz, -20 dB [tel que dit] | MA-15 |
| Normalize | ~0 dB | MA-15, MA-28 |
| Auto-sampler | note 2 s ; sample 3 s (au lieu de 5 s) ; C2 à C4 ; pas d'1 demi-ton (« strike » [ASR ?]) ; vélocité 127 ; canal 1 | MA-28 |
| Note Repeat sur une snare | 1/128 triolet → son proche d'une basse | MA-29 |
| Grille en Gate | 1 bar → 1/2 → 1/16 → 1/32 → 1/64, jusqu'à 1/128 ; raccourcis 1 à 6 | MA-27 |
| Stems | 4 stems ; tempo monté à 140 | MA-02, MA-04 |
| Break pour la technique jungle | plus lent que le morceau (projet à 86 BPM), sans stretch ni pitch | MA-07 |

## Fiches par usage

### Enregistrer une source
- Choisir l'entrée et activer Monitor avant Start [SOURCE MA-01, MA-15].
- Vinyle ou source à silence : mode **Detect** sur seuil [SOURCE MA-15]. Phrase calée sur le morceau : mode **Loop** [SOURCE MA-01].
- Enregistrement en retard : déplacer le start dans l'éditeur [SOURCE MA-01].
- Synthé externe joué en MIDI : Auto-sampler, puis page Zone et sauvegarde en Sound avec samples [SOURCE MA-28].
- À lire d'abord : MA-01, MA-15, MA-28 ; méthode générale : `production.md`.

### Chops et slicing (voix, boucle mélodique)
- Passer la boucle d'Audio à Sampler avant de chopper [SOURCE MA-09, MA-30].
- Normalize si le niveau est bas ; Truncate pour isoler une phrase [SOURCE MA-24, MA-30].
- Detect pour une voix ou des transitoires nets ; Manual pour des sons tenus [SOURCE MA-23, MA-24].
- Apply vers un pad = un Sampler, jeu en Keyboard ; vers un groupe = un Sampler par slice, FX par slice [SOURCE MA-14, MA-30].
- Pattern sur **None** ou supprimer le pattern créé ; Polyphony 1 [SOURCE MA-05, MA-15, MA-30].
- À lire d'abord : MA-14 (le plus complet), MA-19, MA-30.

### Breaks de batterie
- Vérifier le BPM détecté dans Stretch/Settings ; une traîne de fin peut le fausser [SOURCE MA-06].
- Ralentir beaucoup un break crée des artefacts ; l'accélérer non [SOURCE MA-06].
- Technique jungle : break plus lent que le morceau, Detect à 80 avec « plus patterns », puis bounce, Split 8, Polyphony 1 et choke [SOURCE MA-07].
- Kick, snare, hats isolés par duplication et start/end, puis fade out de chaque coup [SOURCE MA-21].
- Ghost notes à la main : vélocité basse, légèrement hors grille [SOURCE MA-07]. Règle du projet : pas d'humanisation aléatoire (`../SKILL.md`).
- À lire d'abord : MA-06, MA-07, MA-21.

### Time-stretch et pitch
- En temps réel : plug-in Audio, moteur Stretch (défaut), Formant pour voix et mélodies, Re-Pitch façon vinyle [SOURCE MA-18, MA-22].
- Une boucle qui ne commence pas sur le 1 ne se cale pas : Truncate en Sampler d'abord, puis retour en Audio [SOURCE MA-22].
- Graver : Edit → Stretch, tempo et pitch indépendants [SOURCE MA-18].
- Transposer à tempo constant : un pad dupliqué par hauteur, un Stretch chacun [SOURCE MA-18].
- À lire d'abord : MA-18, MA-22.

### Beat à partir d'un sample
- Sample détuné, accéléré, resamplé, puis Split 16 et choke [SOURCE MA-03].
- Chaîne de groupe dite : LP ~2000 Hz, second filtre ~3 400 Hz, Cabinet, EQ, Phaser [SOURCE MA-03].
- 808 bouclée : Loop au passage par zéro, X-Fade si clic [SOURCE MA-03].
- Drums détunés pour suivre la mélodie ; Link pour déclencher deux pads ensemble [SOURCE MA-03].
- À lire d'abord : MA-03, MA-08.

### Stems (Maschine 3)
- Logiciel : bouton Stems ; matériel : Sampling → Edit → Stems → Apply [SOURCE MA-02, MA-04].
- Polyphony 1 sur tous les stems [SOURCE MA-04, MA-05].
- Chopper le stem « other » ou « vocals » en Slice Manual, Apply à partir du pad 1 [SOURCE MA-04].
- Stems synchronisés au tempo du morceau [SOURCE MA-02]. Stem drums : reprogrammer kick et snare en suivant son rythme [SOURCE MA-25].
- À lire d'abord : MA-04, MA-02, MA-25. Droits : voir Limites.

### Resampling
- Source Internal → groupe ou Master ; Sync donne un Sampler, Loop donne un Audio [SOURCE MA-16, MA-26].
- Raisons dites : libérer le CPU, fusionner couches et instruments en un sample [SOURCE MA-13, MA-26]. Supprimer ensuite le groupe source [SOURCE MA-16].
- Un synthé ou un Note Repeat rapide devient matière à chopper [SOURCE MA-20, MA-29].
- Procédure côté Live : `../../resampling/SKILL.md`.
- À lire d'abord : MA-13, MA-16, MA-26.

### Glitch, stutter et risers
- Perform FX **Stutter** inséré sur un **groupe** de drums ; MK3 : bouton Perform FX, Smart Strip ; Shift + Auto pour l'automation [SOURCE MA-12, MA-16].
- Glitch vocal : Audio en Gate, notes de 1/16 à 1/128 [SOURCE MA-27].
- Stutter d'intro : pattern raccourci à un temps (1.2), Shift pour passer la grille [SOURCE MA-10].
- Reverse cymbal : Reverse en page Pitch/Envelope du Sampler, ou module Audio inversé dans l'éditeur et placé grille désactivée [SOURCE MA-11].
- À lire d'abord : MA-11, MA-12, MA-27.

### Transfert vers Ableton Live
- Le corpus dit peu : clic droit → Find in Finder, puis glisser les WAV dans le DAW [SOURCE MA-02].
- Le bounce par glisser crée un fichier audio imprimé au tempo voulu [SOURCE MA-18].
- Ranger les fichiers : Edit crée de nouveaux fichiers numérotés [SOURCE MA-17].
- Multi-sorties, MIDI et choix Perform FX : `routage.md` et `../../native-instruments-control/references/maschine.md` (le corpus n'en parle pas).

## Limites

- Aucune capture d'écran n'a été faite. Chaque fiche du corpus liste ses minutes « À vérifier à l'écran » : menus, valeurs et chemins restent à confirmer.
- 27 transcriptions sur 30 ont été lues en version automatique ; MA-03 est très bruitée.
- Seules MA-01, MA-02 et MA-06 ont une transcription manuelle dans leur langue ; les sous-titres anglais manuels de MA-24 sont une traduction.
- Versions : 23 vidéos sont sur Maschine 2 ou l'OS Maschine+. Les chemins matériels de la Maschine+ peuvent différer sur MK3 + Maschine 3.6.0. MA-24 est antérieure à la MK3.
- Les résultats sonores (« plus propre », « proche d'une basse », « grimy ») sont des affirmations des vidéos. Le test d'écoute revient à l'utilisateur.
- Droits : les vidéos samplent vinyles, a cappella, un morceau hip-hop, des boucles Splice ou d'Expansion. Séparer en stems un morceau publié ne règle pas ses droits (interp.). MA-13 présente le resampling de ses propres compositions comme sans problème de droits. Règle du projet : ne jamais copier mélodie, paroles ni enregistrement ; pas d'audio de référence dans une sortie sans droits.
- Perform FX : le corpus l'insère sur un groupe [SOURCE MA-12, MA-16], jamais sur le Master. Règle du projet : un Sound ou Group envoyé directement vers une sortie externe de Maschine contourne le Perform FX du Master (`routage.md`).
- Resampling « Internal Master » [SOURCE MA-01, MA-26] : il capte ce qui passe par le Master (interp.). Un élément routé en sortie externe directe n'y serait ni traité par le Perform FX du Master ni capté (interp., à tester dans la session réelle).
- Notation des notes : « C-2 », « C2 » sont des libellés Maschine. Le numéro MIDI fait foi (règle C3 = 60 du projet) ; le relire avant tout transfert (interp.).
- Lacunes dites par le corpus : un seul tutoriel de risers (MA-11), pas de tutoriel dédié au retrigger, aucun tutoriel Maschine 3 officiel en français sur les stems.
