# Sampling dans Xfer Serum : 30 tutoriels YouTube étudiés

> Fichier remis par l'utilisateur le 05/10/2026 et intégré tel quel au skill `sound-designer-serum`. L'étude a été faite dans Claude in Chrome sur le Mac, par la lecture des transcriptions ; aucune vidéo n'a été écoutée. La synthèse utilisable (méthodes, valeurs dites, recettes adaptées au projet) est dans `sampling-serum-synthese.md`. Les identifiants SE-01 à SE-30 sont ceux de ce fichier.


Recherche faite le 2026-10-05 dans Chrome (onglet dédié, son coupé). 30 vidéos ont été retenues. Pour chacune, j'ai lu la transcription complète (sous-titres YouTube) et la description.
Titres = titres originaux (videoDetails), pas les traductions automatiques de YouTube. Les dates sont les dates de publication.
Conventions : « (interp.) » = mon interprétation ; [ASR ?] = passage douteux de la reconnaissance vocale ; les valeurs sans marque sont dites dans la vidéo.

Classement par thème : A. Serum 2 Sample (breaks, clips, slicing), B. Granular, C. Vocal, D. Spectral et basses à partir de samples, E. Multisample, F. Serum 1 (import audio en wavetable, noise oscillator, resampling).

---

# A. Serum 2 : oscillateur Sample, slicing, breaks, Clip, Arp, stutter

## SE-01 Serum 2: The Complete Guide - Sampling — Synth Designer, 13:59, 2025-04-15, Serum 2
URL: https://www.youtube.com/watch?v=se8YWEM8hxQ
Technique(s) : vue d'ensemble du mode Sample, boucles et crossfade, drone à partir d'un sample, slicing auto/manuel, clip, resampling caché (drag de la sortie)
Transcription : oui (anglais, auto)
- 0:45 Modes d'oscillateur : wavetable, multisample, sample, granular, spectral. Le sujet ici est le mode sample.
- 2:34 Choisir « Sample » dans l'oscillateur à partir de l'init preset. Les catégories factory et « factory non-tonal » contiennent les drums, loops et noises (2:44). On peut aussi charger une wavetable comme sample (3:04).
- 4:16 Glisser-déposer son propre sample (saxophone).
- 4:45 Clic droit sur la forme d'onde → options de snap (manuel p. 73).
- 5:29 Mode one-shot par défaut. En forward loop, un marqueur de boucle apparaît et le sample boucle plus vite dans les aigus (5:39).
- 6:34 Boucle forward-reverse. Le clic s'entend, on le supprime avec le bouton crossfade monté progressivement (7:00).
- 7:27 FX reverb Hall poussée au maximum, decay long : drone obtenu à partir d'une seule note de sax (7:47-8:03).
- 8:48 Clic droit → « fade edges ». Puis « slice auto » : seule la note C1 joue. Clic droit → root note C2, puis on tire la ligne de seuil vers le bas pour voir les slices C#2, D… (9:06-9:41).
- 10:36 « Slice manual » : on peut déplacer les marqueurs créés automatiquement.
- 10:55 Activer Clip ouvre un piano roll. À 120 BPM, grille en 1/8, on enregistre des notes (11:06-11:27). Le clip se glisse dans la playlist du DAW (11:56).
- 12:06 Barres début/fin du sample déplaçables à la souris.
- 12:36 « Fonction cachée » : la petite zone à côté du logo Serum 2 permet de glisser la sortie qu'on vient de jouer vers la playlist (13:06), puis de la remettre dans Serum comme sample (13:24).
À vérifier à l'écran : 4:45 (menu snap) ; 7:00 (bouton crossfade) ; 9:17-9:30 (root note et ligne de seuil) ; 11:06 (grille du clip) ; 12:46-13:06 (emplacement de la zone de drag)

## SE-02 Break Beats Chopping and Sample Slicing in Serum 2 — Dash Glitch, 10:38, 2025-03-28, Serum 2
URL: https://www.youtube.com/watch?v=A9JUzNKFfYU
Technique(s) : breaks, slicing, clip en mode random, stutter / retrigger par relative loop, resampling dans Serum
Transcription : oui (anglais, auto)
- 0:44 Déposer une boucle dans l'oscillateur Sample, la découper et jouer les slices au clavier.
- 0:56 « Slice auto » se règle en tirant le seuil, qui se base sur le volume. « Slice manual » permet d'éditer chaque slice une à une (1:13).
- 1:39 Dessiner un beat dans la section Clip.
- 1:54 Clip en « random » avec une valeur 1/8 : le clip découpe en tranches de 1/8 et les joue dans un ordre aléatoire.
- 2:32 Copy clip / paste clip : un clip reste random, l'autre repasse en normal.
- 3:07 Le paramètre Scan time-stretche chaque slice individuellement en one-shot, sans décalage de timing. On peut le moduler avec un LFO (3:26).
- 4:03 « Relative loop » : une macro va dans la matrice sur « loop mode » pour passer de one-shot à forward loop, avec une courbe remap (4:25-5:07).
- 5:16 Avec relative loop, la boucle se cale sur chaque slice, ce qui produit un retrigger par slice (5:35).
- 5:45 Descendre loop end et le moduler à rebours jusqu'à 0. Un autre LFO ajoute des glitches aléatoires (6:08).
- 7:31 Filtre comb pour un effet résonant.
- 8:14 Resampling : faire un son séquencé d'une mesure (squelch), le glisser hors de Serum et le redéposer comme sample (8:52).
- 9:12 Normalize, slice auto, nouvelle séquence dans le clip, puis glitch par relative loop (9:47).
À vérifier à l'écran : 1:04 (seuil de slicing) ; 2:21 (réglage random 1/8 du clip) ; 4:35 (courbe remap loop mode dans la matrice) ; 5:45-6:08 (LFO sur loop end) ; 8:52 (glisser-déposer de la sortie)

## SE-03 Why Serum 2 Is a Beast for Breakbeat Producers 🎛️ — STRANJAH, 23:59, 2025-04-10, Serum 2
URL: https://www.youtube.com/watch?v=3H6aOK2rTdM
Technique(s) : breaks (jungle/DnB), slicing, tail, warp sur break, stutter via LE et relative loop, gate par LFO, bus FX sur la caisse claire, spectral sur break
Transcription : oui (anglais, auto). Promo de son pack « Vaults » au début.
- 1:20 Osc A en mode sampler, on dépose le « FU break ».
- 1:49 Clic droit → slice auto, première frappe sur C1. La ligne horizontale règle la sensibilité : plus elle est haute, moins il y a de slices (1:59).
- 2:07 En slice manual, on déplace les lignes. Clic droit → snap to zero (2:28). Alt+clic ajoute une slice (2:40).
- 3:00 Mode clip (en bas à gauche), vue clip, longueur 2 mesures (3:19). Zoom avec Alt+molette, copie avec Ctrl+D (3:47).
- 4:03 Le bouton scan change la vitesse de lecture, donc la hauteur.
- 4:34 Menu one-shot → « tailed » : ajoute une queue à chaque slice pour éviter les coupures quand on pitche vers le haut.
- 5:01 Deux warp modes : filtres, distorsion, true FM / old FM (PD). Osc B à level 0 sert de modulateur FM/PD (5:34).
- 6:01 Unison sur le break avec un peu de detune pour épaissir (6:11).
- 6:23 Stutter : forward loop, paramètre LE (loop length), « relative loop », puis valeurs de LE réduites. Macro 1 sur LE, à automatiser (6:47).
- 7:11 Deux filtres F1/F2 en parallèle ou en série (DJ mix, diffuser, formant) (7:23-8:33).
- 8:50 LFO2 en mode « path » (XY) : X sur le cutoff du filtre 2, Y sur le formant. Rate 2 mesures, mode free (9:41).
- 10:01 Noise oscillator en mode white + filtre. LFO1 court en 1/4 sur le level du noise (level à 0, modulation au maximum) donne un hi-hat (10:35).
- 11:03 LFO1 sur le level du sampler donne un gate saccadé, plus haché en 1/8 (11:21). LFO1 sur le cutoff avec résonance, puis filtre « acid ladder » (11:34-11:57).
- 12:32 Distorsion en FX, drive modulé par LFO1. Bode (frequency shifter) avec width à 0 (13:14). Convolve avec l'IR « bits motion », attention au mix (13:27-14:16).
- 14:45 Bus 1 avec reverb Basin, mix 100. LFO4 en mode horizontal sur les coups de caisse claire, rate 1 mesure, free. Dans la matrice, LFO4 → routing bus 1 (15:05).
- 15:44 Flanger dont le cutoff est piloté par LFO5 en mode envelope sur 1 mesure (15:54).
- 16:37 Spectral sur le break : transients médiocres. Scan négatif = lecture à l'envers (17:10). Warp spectral « harmonics » (17:32). Filtre spectral dessiné (passe-haut) (18:21).
- 18:48 Osc B en sub, « oscillator mapping » pour séparer les plages de touches (19:00). LFO3 sur coarse pitch, 1 mesure (19:53). Sine en direct out (20:23).
- 22:06 Automation de macros dans le clip.
À vérifier à l'écran : 2:40 (Alt+clic pour ajouter une slice) ; 4:44 (option tailed) ; 6:36-6:47 (LE et relative loop) ; 15:05 (matrice LFO4 → bus 1) ; 19:00 (mapping des oscillateurs)

## SE-04 Serum 2's Sample Oscillator Explained (Full Tutorial) — EDMProd, 12:39, 2026-03-26, Serum 2
URL: https://www.youtube.com/watch?v=0BS5UVu-7jE
Technique(s) : breaks, slicing, arpégiateur sur slices (glitch), slices granulaires sur voix, couche texture
Transcription : oui (anglais, auto)
- 0:10 Charger un break dans l'oscillateur Sample.
- 0:34 Clic droit sur la forme d'onde → slice auto / manual. Une slice par transitoire, la première sur C1 (0:43-1:12).
- 1:32 La ligne jaune horizontale règle la sensibilité : plus haut = moins de slices. Réglée à mi-hauteur (1:59).
- 2:22 Clic droit → root note de C1 à C2 : on joue une octave plus haut sans changer la hauteur.
- 2:50 Octave, warp et unison/detune restent actifs. Scan baissé = plus grave et plus lent.
- 3:11 « Play slice to end ». 3:27 « Play single slice » transpose la première slice.
- 3:36 « Send to selected clip » : la séquence de slices va dans le clip. Raccourcir le clip à la moitié change le pattern (3:58).
- 4:17 Arp ON (root note revenue en bas) : tenir un accord déclenche des slices, effet « breakbeat glitch » façon Aphex Twin (4:33). Pattern et rate (4:48).
- 5:11 Shift et range de l'arp : shift 3 demi-tons ; range 8 avec shift 2 = huit transpositions de 2 demi-tons (5:45).
- 6:46 Passer l'oscillateur en granular conserve le slicing. Scan bas, density haute, random (7:11).
- 7:25 Long a cappella : sensibilité baissée, clic droit « zoom to start and end » (7:44).
- 8:04 Couche granular au-dessus d'un Reese sur osc B (width et detune baissés).
- 8:38 Normalize, warp tube (8:52). Scan 0 % pour que le grain tienne (9:00). Accord −1 demi-ton (9:22). Play single slice (9:31).
- 9:45 Unison, pan aléatoire, direction au milieu = 50 % avant/arrière (9:57).
- 10:11 « Osc mapping » : osc B verrouillé sur C3 avec « fold » (10:45).
- 11:03 Granular envoyé sur bus 1 avec reverb. Osc B sur bus 2 avec filtre notch et LFO lent (11:19).
À vérifier à l'écran : 1:32 (ligne de sensibilité) ; 3:36 (menu send to selected clip) ; 5:11-5:45 (shift et range de l'arp) ; 7:11 (réglages granular) ; 10:34 (mapping et fold)

## SE-05 Serum 2 as Sampler: 808, Chop Breakbeat & Granular Chords | Experimental Beats — Sample Focus, 9:37, 2025-07-01, Serum 2
URL: https://www.youtube.com/watch?v=rU89SF3Ri0k
Technique(s) : 808 en sample, breakbeat découpé, accords granulaires à partir d'un morceau entier
Transcription : oui (anglais, auto). Promo samplefocus.com à la fin.
- 0:25 Les nouveaux types d'oscillateur (sample, granular, spectral) fonctionnent tous avec des samples.
- 0:50 808 en sample. FX splitter low/high (1:11), distorsion sur les aigus seulement (1:27), filtre après la distorsion (1:58), ring mod (2:19).
- 3:16 Mode sample (marche aussi en granular/spectral) : on dépose le break, clic droit → slice auto (3:26).
- 3:34 Augmenter le release pour que la slice joue en entier. Mono ON pour éviter les slices qui se chevauchent (3:43).
- 3:53 Clip 1 : dessiner le pattern, baisser le pitch pour caler le tempo (4:01).
- 4:24 Passer de sample à granular garde les slices. Le scan donne des résultats abstraits (4:49).
- 5:46 Glisser le clip dans le DAW puis désactiver le clip dans Serum (5:53).
- 6:14 On peut charger un morceau entier, mais pas en MP3 (« MP3 doesn't work »). Exemple : OST d'Ecco the Dolphin, granular + slice auto (6:23).
- 6:44 LFO sur filtre. Longueur des grains (7:04). Random length, pan, level, direction (7:19). OTT (7:44).
À vérifier à l'écran : 1:18 (bandes du splitter) ; 3:26 (slicing du break) ; 4:01 (pitch du clip) ; 7:04-7:34 (paramètres granular)

## SE-06 Slicing My Sample with Serum 2 — KelSounds, 4:57, 2025-03-21, Serum 2
URL: https://www.youtube.com/watch?v=natkcaPAWlM
Technique(s) : boucle de batterie découpée, snap to beats, clip, compression parallèle via bus
Transcription : oui (anglais, auto). Chapitres : 0:34 snap & slicing auto, 1:50 clip, 3:15 compression parallèle.
- 0:17 Sample → déposer une boucle de batterie.
- 0:28 « Snap to beats » : les points start, end et loop s'aimantent à la grille du tempo (0:37-0:56).
- 0:56 Ligne de seuil : tirée complètement vers le bas pour beaucoup de coupes (1:03). Au survol, la note s'affiche (C2) (1:11).
- 1:47 Clip / piano roll en boucle.
- 2:01 Warp distortion « tube ». Routage osc → filtre 1 → filtre 2, comb « minus » avec réglage du mix (2:12-2:21).
- 2:46 Passe-bande automatisé, résonance et drive. Modulateur « sample & hold » (2:54).
- 3:16 Compression parallèle : filtre 1 envoyé au bus 1, compresseur threshold −50, ratio 8, release rapide (3:38). Bouton send (3:58).
À vérifier à l'écran : 0:37 (option snap to beats) ; 2:12 (routage des filtres) ; 3:38 (réglages du compresseur de bus)

## SE-07 How Serum 2 Clip View Will Change Jungle Production Forever — STRANJAH, 18:35, 2025-09-18, Serum 2
URL: https://www.youtube.com/watch?v=d5CxuSHX7gI
Technique(s) : breaks et Clip view en profondeur (play modes, KB span offset, déclenchement des clips sur l'octave 0, start point en macro, scan sur pitch bend)
Transcription : oui (anglais manuel + auto). Promo « Jungleism » de 9:25 à 11:09 et à 17:12.
- 0:45 Slice auto (curseur) ou manual. Zoom à la molette, snap to zero, slices au début des transitoires. Alt+clic pour ajouter/retirer (1:11).
- 1:36 One-shot → « tail », utile quand le break joue plus lent que l'original.
- 1:59 Clic droit → envoyer le pattern au clip 1. Ne marche que si le break fait des mesures exactes (son amen a 1,5 temps de trop).
- 2:21 Dessiner le pattern, dupliquer avec Ctrl/Cmd+D, Shift+flèches. Nommer, copier vers d'autres pads, start point sur la caisse claire.
- 2:49 Notes à partir de C1. « Retrig » ON. Launch quantize 1/8. « Edit all » (3:14-3:40).
- 3:40 Play modes : normal, reverse, pendulum, random (4:05). On enregistre le random pour obtenir de nouveaux patterns d'amen. « Random no duplicates » (4:34), random start. Rate double/half, triolet/pointé (5:00).
- 5:30 KB span = « offset » : chaque segment du pattern est mappé sur une touche selon la quantize (clic droit en haut à droite du key roll : 1/8) (5:54). En 1/4, cycle de 4 segments qui se répète (6:21).
- 6:51 KB span OFF : les pads de clip sont mappés sur l'octave 0 (C0, C#0…) et se déclenchent en live (7:16-7:40).
- 8:10 Launch quantize 1/8 (ou 1/16, 1/32). Trigger mode mono (pas poly) (8:35). Six patterns dont offset, stutter, stutter rapide, crash (8:59).
- 11:09 Clic droit → mapper le start point du clip sur une macro ou la mod wheel (11:30). 1/8 sonne plus fluide que 1/16 (12:24).
- 12:44 Scan : 100 = normal, sous 100 = ralenti, négatif = reverse. Scan mappé sur le pitch bend : range de pitch à 0, scan à 0 %, courbe de la matrice avec un point posé en Alt+glisser (13:14-13:38).
- 14:02 FX sur macros. Lignes d'automation de macros dans le clip (macro 5 pitch, distorsion, EQ, reverb) (14:30). Amen 1 et Amen 2 = même sample avec des macros différentes (14:54). MIDI learn (15:17). Mod wheel → filtre (15:46).
À vérifier à l'écran : 2:49 (retrig et launch quantize) ; 5:54 (KB span offset) ; 7:16 (correspondance pads/touches) ; 11:30 (menu start point → macro) ; 13:38 (courbe de la matrice)

## SE-08 How to Turn Serum 2 Into a Jungle Powerhouse — STRANJAH, 14:18, 2026-07-28, Serum 2
URL: https://www.youtube.com/watch?v=vcWST8mqp4Q
Technique(s) : breaks, clips de STUTTER (1/16 → 1/32), flag de sample offset sur macro, reverse au pitch wheel, scan range 800 %
Transcription : oui (anglais, auto). Promo de packs à 0:23 et de 3:29 à 5:00.
- 0:50 Sélecteur de moteur (5 types) → sample. Déposer le break, slice auto avec le curseur de sensibilité, ou manual (1:00-1:44). Mappé depuis C1.
- 2:08 Clic droit sur le sample → « send to selected clip » (clip 1).
- 2:19 One-shot → « tail », pour les slices pitchées vers le haut (2:29). Forward/reverse pour un glitch (2:43).
- 2:54 Clic droit → range du scan jusqu'à 800 % pour des breaks pitchés et glitchés (3:19).
- 5:11 Patterns : copier la partie qui commence sur la caisse claire dans le clip 2. Pattern « Apache » (Ctrl+clic+glisser copie les notes) (5:20). Pattern « stomp » sans double kick (5:36-6:00).
- 6:12 Les clips sont mappés sur l'octave −2 du contrôleur. Les réglages sont propres à chaque clip, d'où « edit all » (6:47). Retrigger ON. Launch quantize 1/8 (6:58-7:13).
- 7:27 Clip de stutter : caisse claire répétée, Ctrl+D (7:37). Stutter plus rapide avec la grille en 1/32 (7:51-8:05).
- 8:21 Filtre low-pass 24 avec drive, mod wheel → cutoff, résonance (8:33). Drive de distorsion sur macro (8:49).
- 9:16 Matrice : pitch bend → scan rate de l'osc A, au maximum, bipolaire. Vers le bas, la hauteur baisse puis les frappes s'inversent (reverse) (9:49).
- 10:04 Drapeaux du clip : le flag de sample offset fait démarrer le pattern sur la caisse claire (10:16). Clic droit → macro 2 « sample offset » (10:28). Quantize 1/8 ou 1/4, car 1/16 donne des glitches et des silences (10:40).
- 11:48 Automation par clip (bouton +) : rampe de drive sur macro 1, mod wheel (12:00-12:15). Attention aux automations intégrées au clip (12:27-12:49). MIDI learn (12:49).
À vérifier à l'écran : 2:54 (menu range du scan) ; 6:47 (edit all et retrigger) ; 8:05 (grille 1/32) ; 9:26 (matrice pitch bend → scan) ; 10:16-10:28 (drapeau sample offset)

## SE-09 SERUM 2 - Import clips — sonfx, 14:45, 2025-03-24, Serum 2
URL: https://www.youtube.com/watch?v=P326dRksMJI
Technique(s) : clips MIDI importés pilotant des moteurs à samples (spectral pad, basse multisample, rompler « box », drums multisample 808/505), vélocité → start, granular
Transcription : oui (anglais, auto). Vidéo en anglais même si le titre apparaissait en français dans les résultats.
- 0:00 On glisse ses propres clips MIDI dans Serum 2 : drums, pad, séquence.
- 0:25 Clip de pad dans le moteur spectral, enveloppe, −2 octaves (0:41-1:00). Shift+sélection de notes pour baisser leur « chance » (1:22).
- 1:33 FM depuis B, oscillateur chaos. Filtre spectral dessiné, ouvert par l'enveloppe d'amplitude (2:12-2:27).
- 3:11 Basse à partir du même clip dans le moteur multisample « Jaguar bass tape wounds », monophonique (3:27). Notes du haut supprimées, −2 octaves. « Note expression » : pitch bend de −3 demi-tons sur la dernière note (4:02).
- 5:12 Sons « box » de la banque de samples (groovebox rompler), clip de 16 pas (5:27). Vélocité → pan (5:41). Couche de noise (6:13).
- 7:16 Drums en multisample « electronic drums 808 ». Waveshaping, source changée pour 505/626 (8:25). Reverb, compression (9:08).
- 9:24 Vélocité → start du sample (position de la tête de lecture).
- 10:02 Hats en kit acoustique : mono = effet de choke group (10:28). Random pan, play mode pendulum (11:04).
- 11:46 Granular sur des notes tenues de pad, boucle et randoms (12:11-13:30).
- 13:58 Limite : il n'a pas trouvé comment enchaîner les clips dans Serum.
À vérifier à l'écran : 0:25 (dépôt du clip) ; 3:27 (preset multisample) ; 9:37 (vélocité → start dans la matrice) ; 10:28 (mono / choke)

## SE-10 SERUM 2 Tutorial | Making INSANE Glitch FX — The Sound Design Channel, 13:45, 2025-04-17, Serum 2
URL: https://www.youtube.com/watch?v=g3VV3S__l7A
Technique(s) : glitch / stutter aléatoire avec des samples (noise osc « radio glitch » + granular « tiger growl ») et S&H partout
Transcription : oui (anglais, auto). Chapitres : 0:55 osc, 1:18 Chaos Lorenz, 2:55 granular, 6:00 LFO et filtre, 7:31 FX, 13:20 résultat. Tuteur : Leo Lauretti (Abstract Music Lab). Promo de pack de presets.
- 0:53 Saw à octave −1, FM depuis le sub (sub à level 0) (1:05).
- 1:22 LFO1 « Chaos Lorenz » (X) : free, 1/8, mono, attack et release montés (1:46-2:01).
- 2:13 Noise osc avec le sample Serum 2 « radio glitch » : level monté, pitch baissé. LFO2 en S&H free → pitch du noise (2:35).
- 2:51 Osc B en granular, sample factory « tiger growl », +2 octaves, forward loop (3:15). Bornes de boucle resserrées (3:24).
- 3:47 Crossfade ON, ce qui élargit la stéréo. Scan de 100 % à 40 % (3:54-4:02). Density montée.
- 4:21 Level à 0, puis LFO3 S&H free 1/8 sur le level, ce qui donne le glitch. Offset, direction, random length/pan/level (4:43-5:20). Warp tube.
- 5:55 LFO4 S&H free 1/16 avec smoothing → FM du warp A (6:07).
- 6:22 Filtre 1 MG12 sur A+B avec cutoff par LFO3. Filtre 2 sur A+noise avec LFO2 sur le cutoff, résonance et drive forts (6:57).
- 7:30 Convolve « long digital chamber » : taille et ton baissés, damping monté, mix modulé par LFO5 (retrig, host BPM 2 mesures) en rafales (8:18).
- 8:59 Compresseur multibande. EQ low shelf et bell (9:56). Ping-pong 1/4 et 1/4 pointé (10:26). Utility bass mono (10:35).
- 10:56 Filtre « DJ mixer » avec LFO6 sur 1,5 mesure pointée (11:36). LFO saw down 1/16 retrig → level du filtre en unipolaire (Alt+Shift) (12:22).
- 12:47 Reverb hall avec mix à 0 + LFO3 pour des déclenchements aléatoires.
À vérifier à l'écran : 2:13 (choix du sample radio glitch) ; 3:24-4:02 (boucle et scan 40 %) ; 4:21 (LFO3 S&H sur le level) ; 8:18 (forme de LFO5) ; 11:36 (DJ mixer)

---

# B. Granular : textures, pads, risers

## SE-11 Serum 2: The Complete Guide - Granular Mode — Synth Designer, 14:58, 2025-04-29, Serum 2
URL: https://www.youtube.com/watch?v=PUk6qzR4Hog
Technique(s) : granular de base, pad/drone, pluck, basse « guitare » à partir d'un même sample factory
Transcription : oui (anglais, auto)
- 1:03 Définition tirée du manuel : les grains durent quelques millisecondes.
- 2:00 Factory « breathy pianoish » comparé en wavetable, sample et granular (2:24).
- 2:59 Panneau d'enveloppe des grains. One-shot par défaut, passage en forward-reverse loop (3:52) avec une petite zone de boucle (4:18).
- 5:04 Unison très désaccordé, on baisse le detune. Reverb, puis filtre pour couper le souffle (5:25-5:49).
- 6:17 Scan. Density (plus de grains = plus de CPU) (6:44-7:06). Pitch (7:34). Longueur des grains : son de cloche (7:45-7:58).
- 8:47 Random length, level et pan. Forme d'enveloppe et crossfade (9:42).
- 10:46 Autre sample factory. Octave en bas pour une basse (11:02). Enveloppe pluck (11:27). Basse « guitare » (13:03).
- 14:11 Longueur, densité et enveloppe changées : la même source devient un pad.
À vérifier à l'écran : 2:59 (panneau d'enveloppe) ; 4:18 (zone de boucle) ; 6:44 (density) ; 7:45 (length) ; 14:11 (réglages du pad final)

## SE-12 Serum 2 Granular Mode Explained — Dash Glitch, 19:36, 2025-03-18, Serum 2
URL: https://www.youtube.com/watch?v=ozKVAP2gRmw
Technique(s) : granular complet, pads graves à partir d'un sample médium, accordage d'un sample perso, mode manual (scrub), grains très courts rendus tonals par key track
Transcription : oui (anglais, auto)
- 2:34 One-shot par défaut, puis forward loop, puis on dessine les marqueurs de boucle (2:42).
- 3:16 Enveloppe de grain (rampe, triangle, pluck). Random shape (3:50). Crossfade contre les clics (4:36).
- 4:44 Les boutons vont par paires (valeur + random) : length, pan… Direction = sens aléatoire (5:42), offset = position aléatoire (5:58). Random pitch à doses minimes seulement (6:25).
- 7:01 Transposé de plusieurs octaves vers le bas sans time-stretch : pad grave tiré d'un piano médium.
- 8:02 Samples perso : il bounce des sons du projet et les met en granular. Flûte tirée de son pack « Fragments » (8:39).
- 9:25 Accordage : sample en D, root en C, donc semitones −2, vérifié au tuner (9:45). Un sample en G demande +5 (10:07).
- 11:13 Scan = vitesse de la tête de lecture. Density = nombre de grains : 0 ne laisse que le transitoire, 1 à 10 en usage courant (11:43). Length courte = glitch, longue = pad (11:53).
- 13:26 Mode manual : on ne scrubbe qu'avec la position, idéal pour des ambiances horrifiques, avec position et pitch modulés (13:45).
- 14:10 Length très courte : le son devient tonal. Clic droit sur length → key track, fine tune, valeur 56 (14:33-15:29). Mono legato + glide.
- 16:11 Pratique pour rendre tonal un son percussif ou riche en transitoires.
- 17:10 Deux warp modes (spectral clipping). FM d'un sinus wavetable vers le granular (17:42).
À vérifier à l'écran : 3:26 (formes de fenêtre) ; 9:45 (tuner et semitones) ; 11:43 (compteur de voix) ; 14:33 (menu key track) ; 15:29 (valeur 56)

## SE-13 Serum 2 Has a Hidden Sound Engine (and It's Incredible) — EDMProd, 21:10, 2026-02-18, Serum 2
URL: https://www.youtube.com/watch?v=Rw1Aw69mtjA
Technique(s) : granular, guide de chaque paramètre, fenêtres, boucles, spawn pattern de l'unison, density et length synchronisées au BPM (grains rythmiques)
Transcription : oui (anglais, auto)
- 0:18 Menu wavetable → granular, valable pour A, B ou C. Rien ne sonne tant qu'aucun sample n'est chargé (2:59). Factory tonal / non-tonal / wavetables (3:07).
- 3:31 Scan = vitesse de la tête de lecture à hauteur constante. Scan 0 (4:02). Grain length haute + density basse = boucle lente (4:24).
- 4:39 Density ≈ 1 donne une ligne blanche, ≈ 2 en donne deux, et ainsi de suite.
- 5:24 Random pan, random length (6:06). Random pitch de 0 à 12 demi-tons ; vers 1/4 de demi-ton avec length et density hautes, effet inquiétant (7:10). Random direction = % de chance de lecture à l'envers (7:24). Ligne jaune = start (7:51). Random offset (8:08).
- 8:32 « Load sample » pour charger son propre fichier (arp du pack EDMProd). Offset donne des nuages de grains. Scan jusqu'à 200 % (9:51).
- 10:54 Fenêtre de grain : Hann par défaut, Welch, Gaussian (clic), Blackman-Harris, Sinc (espace entre grains) (10:54-11:52). Amount, random, skew. Option+glisser pour éditer sans ouvrir la fenêtre (12:32).
- 12:51 Forward loop, reverse, forward-reverse, tailed (14:12-14:38). Relative loop (15:02). Manual : scan devient position (15:14). Link loop length, exit loop on release (15:46). « Loop grains » (15:55).
- 16:24 Spawn pattern de l'unison : together, even, exponential, random (17:46).
- 17:57 Clic droit sur density → BPM sync (1/4, 1/8, 1 mesure). Clic droit sur length → BPM sync (1/2 note avec density sur 1 mesure) (19:16). LFO d'une mesure sur density = rythme (19:40).
- 19:55 Basse glissée-déposée, grain length 100 %.
À vérifier à l'écran : 4:51 (lignes de grains) ; 10:54-11:52 (fenêtres) ; 16:46-17:46 (spawn pattern) ; 18:08 (BPM sync de density) ; 19:40 (LFO sur density)

## SE-14 Granular Risers in Serum 2 — adrenakrohm, 10:21, 2026-01-02, Serum 2
URL: https://www.youtube.com/watch?v=s7mwwP-TNvo
Technique(s) : RISER granulaire à partir d'une cymbale inversée
Transcription : oui (anglais, auto)
- 0:40 Baisser d'abord le level (sortie forte). Factory « 505 cymbal crash » (0:52).
- 1:09 Clic droit → reverse.
- 1:30 Trop court : octaves en bas (plus lent). Start avancé, scan baissé de 100 % à une valeur très faible (1:48-2:01). Grain length baissé (2:01).
- 2:30 LFO1 → pitch en unipolaire, 48 demi-tons, rampe, mode envelope, 2 mesures (2:43).
- 2:43 Filtre 24 dB sur LFO1 en unipolaire + drive. LFO1 aussi sur length. Random length et random pitch (3:04-3:38). Reverb avec coupe des graves.
- 5:02 Autre « cymbal crash » inversée. Density baissée = son qui se désagrège.
- 6:02 Flanger, distorsion légère (6:49), hyper dimension, chorus avant le flanger, passe-haut (7:17). Riser sur 4 mesures.
- 8:06 Scan trop bas : une petite partie seulement du sample est jouée, on remonte le scan (8:22).
- 9:14 Pour finir pile sur la mesure, le plus précis est de rendre en audio, couper et ajouter un fade in (9:25-9:41).
À vérifier à l'écran : 1:48-2:01 (valeur du scan) ; 2:30-2:43 (LFO1 ramp et 48 st) ; 3:04 (cibles de LFO1) ; 8:22 (scan relevé)

---

# C. Voix : vocal chops et textures vocales

## SE-15 Creative Vocal Edits in Serum 2 (Unique FX & Textures) — DNB Academy, 10:45, 2025-05-14, Serum 2
URL: https://www.youtube.com/watch?v=D-H4co2OdgY
Technique(s) : vocal chops granulaires, textures vocales, arp aléatoire sur slices, spectral
Transcription : oui (anglais, auto). Présentateur : Tomic.
- 0:28 Granular, forward-reverse loop (ou one-shot), voix déposée. Clic droit → slice auto (ou manual) (0:36). Voix de Caroline (VOE) sur « Not Thinking Straight » (Liquicity) (0:54).
- 1:15 Density. Scan baissé, density basse puis haute = gouttelettes de grains (1:43). Random pitch léger = chorus/unisson (2:09). Random length et direction (passages à l'envers) (2:23).
- 2:53 Scan 100, density par défaut, randoms à 0 : on retrouve des vocal chops normaux.
- 3:28 Reverb, delay, convolve (IR medium) (3:42-4:13). Density haute et scan très bas, pitch (4:34).
- 4:34 Filtre band-pass normal 12, compression forte avant le filtre. LFO avec preset « sidechain » sur 2 mesures → volume (5:12-5:23).
- 6:33 Voix en F mineur transposée de −4 demi-tons (C# mineur) : tout reste dans la tonalité quelle que soit la note (6:47).
- 7:07 Arp ON, random, rate 1, gate 50 %, 1 mesure : chops atmosphériques différents à chaque répétition (7:26-8:13). Une valeur « 3 » est dite à 7:43 sans paramètre clair [ASR ?].
- 8:13 Même chose en spectral : scan, filtre spectral qui garde les médiums (8:40), modulation sur scan, FM, distorsion (9:15-9:31).
À vérifier à l'écran : 1:15-1:43 (density et scan) ; 4:34 (filtre BP 12) ; 5:12 (preset sidechain du LFO) ; 7:26-8:13 (réglages de l'arp)

## SE-16 Why SERUM 2 Is AMAZING for VOCLAS (make ambeints, vocal loops and more) — Slooply, 3:00, 2025-04-25, Serum 2
URL: https://www.youtube.com/watch?v=y1LdZUmm5tU
Technique(s) : ambiance vocale granulaire, accords et pluck vocal, arp en mode chord
Transcription : oui (anglais, auto). Promo slooply à la fin.
- 0:10 Voix déposée dans la section granular, auto slice : la voix se joue au clavier.
- 0:20 Release un peu monté. Scan à 0 % pour boucler (0:32). Density pour épaissir (0:53), offset pour un rendu naturel, length au goût. Randomness pour la largeur (1:11).
- 1:25 Enveloppe 2 → filtre. Unison avec un peu de detune (1:45).
- 1:45 Auto slice OFF et sélection manuelle de la région : on peut jouer des accords (2:04). Enveloppe courte = pluck (2:04).
- 2:14 Arp, choix de la gamme en bas, mode chord (2:26).
À vérifier à l'écran : 0:32 (scan 0 %) ; 1:11 (valeurs random) ; 2:04 (région manuelle) ; 2:26 (gamme / chord mode de l'arp)

## SE-17 Wait... Fred again Uses Serum 2 for vocal chops? — The Preset Bros, 8:11, 2025-08-14, Serum 2
URL: https://www.youtube.com/watch?v=nokM3nhzxKI
Technique(s) : vocal chops (façon Fred again.. / Skrillex / Flume) avec le mode Sample et une mélodie au piano roll
Transcription : oui (anglais, auto). Chapitres : 1:11 chargement, 2:50 mélodie, 4:20 FX, 6:00 bonus, 7:47 voix. Présentateur : Josh.
- 1:06 Osc A → Sample (1:18). Voix : clic droit dans le DAW → « show in browser », puis glisser dans Serum (1:46-1:59).
- 2:11 Clic droit → slice auto. Ligne vers le bas = plus de slices, vers le haut = moins (2:20). Slice manual pour déplacer les lignes (2:30).
- 2:48 Piano roll : trouver une note qui sonne bien, boucler la section, jouer au clavier MIDI ou aux pads (2:58-3:12). Déplacer les notes pour trouver d'autres chops (3:31).
- 4:26 Distorsion : pour de l'EDM, diode 1/2 ou sine shaper avec coupes haute et basse (style Jackǖ/Skrillex). Ici, version chill en soft clip (4:57).
- 5:07 Compression multibande. Reverb (5:28).
- 6:05 Bonus : macro → mix de la reverb pour un « wash out », plus une EQ qui coupe les graves (6:31). Macro automatisée en fin de phrase (7:19-7:39).
À vérifier à l'écran : 2:20 (seuil des slices) ; 3:12 (pattern MIDI) ; 4:37 (type de distorsion) ; 6:21 (assignations de la macro)

---

# D. Spectral, resynthèse et basses à partir de samples (Serum 2)

## SE-18 Realistic Instrument Resynthesis with Serum 2 Spectral Oscillator — Dash Glitch, 18:36, 2025-04-18, Serum 2
URL: https://www.youtube.com/watch?v=yp9V_FbcbCU
Technique(s) : enregistrer un vrai instrument (flûte), le resynthétiser en spectral, séparer fondamentale et harmoniques, positions pilotées par enveloppes
Transcription : oui (anglais, auto)
- 0:15 Flûte « style sud-américain » achetée en friperie. Enregistrer une note legato longue avec ses variations harmoniques (overblow) (1:28-2:26).
- 2:43 Nettoyage avec iZotope RX spectral de-noise.
- 3:13 Glisser dans l'oscillateur spectral, ou mieux : copier le sample dans le dossier Serum 2 Presets/Samples/User avec la root note à la fin du nom de fichier, ce qui active l'auto key-track (3:23-4:00). Supprimer le suffixe « bounce » de Bitwig.
- 4:09 Init, osc en spectral, choix du sample. Affichage des harmoniques (5:04).
- 5:32 Mode manual : des enveloppes déplacent la position. L'enveloppe initiale fait l'overblow, l'aftertouch pilote la position (5:44-6:05).
- 6:27 Filtre spectral (avec lecture des valeurs) en low-cut sur la fondamentale : il ne reste que les harmoniques (6:36-7:01).
- 7:31 Sinus wavetable pour remplacer la fondamentale. Env 2 sur le level du sinus avec de l'attaque : la fondamentale arrive en retard (8:01-8:10).
- 8:35 LFO1 en random « Rossler » sur la position (8:47). Dans la matrice, LFO1 → position mis à l'échelle par env 2 (9:12-9:31). Enveloppe sur la position avec decay ; vélocité/random sur le decay (9:58). Attack et decay liés, environ 750 ms (10:32).
- 11:24 Legato : mono legato, portamento, courbe vers le bas (11:53-12:05).
- 12:42 Macro 1 → position (harmoniques d'overblow). LFO en Hz, la macro ramène son rate vers 0,001 (13:03-13:25). Delay avant la reverb.
- 14:58 Enveloppe de la fondamentale en « legato inverted » (15:12).
- 15:45 Deuxième sample : ajuster le cutoff. « Copy with mods / paste » de l'oscillateur une octave au-dessus (16:15-16:32). LFO random (Y) sur le level pour un flutter (16:44).
À vérifier à l'écran : 3:52-4:00 (nom de fichier avec root note) ; 6:36-7:01 (forme du filtre spectral) ; 9:31 (matrice LFO1/env2) ; 10:32 (750 ms) ; 15:12 (mode legato inverted)

## SE-19 How to Use Serum 2's Spectral Engine (Sound Design Tutorial) — EDMProd, 15:51, 2026-02-26, Serum 2
URL: https://www.youtube.com/watch?v=HlgerquD7bw
Technique(s) : moteur spectral complet (scan, filtre spectral, warps spectraux, boucles, phase lock, option transients pour les boucles de batterie)
Transcription : oui (anglais, auto)
- 0:36 Menu wavetable → spectral. Il faut un sample (0:44). Factory, wavetables ou fichier perso (1:00). Exemple avec une voix.
- 1:53 Scan à 100 % = normal. Plus bas = plus lent à hauteur constante, grain audible. Négatif = à l'envers. Jusqu'à 200 % (2:34). Réglé vers 50 %.
- 2:42 Éditeur du filtre spectral : couper la fondamentale (2:59), quasi passe-haut (3:07), courbes (3:28), bouton cutoff (3:37). Démonstration sur un bruit de Korg MS-20 déposé (4:03). Presets de filtre et mix (4:31-4:41).
- 4:57 Warps spectraux : peak follow (5:15), gate (5:33), comb (5:46).
- 6:08 Forward loop (boîte bleue) avec le start (ligne jaune) avant la boucle (6:32). Pad + reverb (6:52). Reverse loop, forward-reverse (7:15). « Tailed » boucle la seconde moitié jusqu'à la fin du release (7:32-8:00).
- 8:10 Manual : scan devient position. Relative loop (8:48-9:09). Link loop length. « Exit loop on release » (9:25). Crossfade, meilleur en forward-reverse (9:52). Sample end (10:32).
- 10:47 Roue dentée de l'unison : width, range, span, blend.
- 11:34 Barre latérale = coupure brick-wall basse et haute du spectre (11:43-12:08).
- 12:16 Clic droit sur scan : reverse, key track (12:35), range jusqu'à 800 % (13:00), phase lock pour moins de flou (13:12-14:06).
- 14:14 Option « transients » pour les drums : boucle top DnB, scan proche de 100, transients ON (15:06).
À vérifier à l'écran : 2:42-3:28 (éditeur du filtre spectral) ; 5:15-5:46 (warps spectraux) ; 11:43 (barre brick-wall) ; 13:12 (phase lock) ; 15:06 (option transients)

## SE-20 SERUM 2: I MADE AN ENTIRE DROP FROM 1 SAMPLE... IT'S EASY — oddprophet, 11:18, 2025-03-22, Serum 2
URL: https://www.youtube.com/watch?v=vmm9Xgpp98U
Technique(s) : basse dubstep à partir d'un stab de cuivre en spectral, variations par warp « shift » et mode manual
Transcription : oui (anglais, auto). Promo de presets dans la description.
- 1:09 Osc A en sub, octave en bas. Osc B en spectral avec le stab de cuivre Splice « evil brass » (1:25-1:56).
- 2:05 Overdrive. Splitter : convolve « rock plate 2 » sur les aigus, IR gain monté, decay baissé (2:11-2:36). Compresseur multibande (2:47), seconde distorsion, EQ du bas (3:11).
- 3:21 Warp spectral « harmonics » : prolonge les partiels vers le haut, plus brillant. Un LFO fait le son de « gun » (4:05).
- 5:09 Tempo 145. Warp « shift » (frequency shift) automatisé (5:38).
- 6:41 Patch cloné, scan passé de one-shot à manual : la position est déplacée par LFO/enveloppe pour contrôler la longueur (6:49-7:12). Enveloppe → main tuning pour les pitch bends (7:23).
- 8:04 « N'importe quel son tonal » dans le spectral + warps. Position fixe = son tenu (9:01). Un stab de kick fonctionne moins bien (9:34-9:44).
À vérifier à l'écran : 1:56 (sample et réglages spectraux) ; 2:19-2:36 (splitter et convolve) ; 3:21-4:05 (LFO sur harmonics) ; 6:49 (mode manual et position)

## SE-21 SERUM 2: HOW TO TURN ANY SAMPLE INTO A HEAVY DUBSTEP BASS — oddprophet, 11:01, 2025-03-18, Serum 2
URL: https://www.youtube.com/watch?v=LRQFCUXqXr4
Technique(s) : basse tearout à partir d'une percussion tonale (ride) en spectral, samples interchangeables
Transcription : oui (anglais, auto). Promo de preset.
- 1:36 Déposer un petit sample tonal et le remplacer à volonté pour obtenir « un sample pack entier ».
- 3:53 Sub sinus. Osc B en spectral avec une ride (percussion tonale), une octave en bas (4:12-4:25).
- 4:52 Overdrives empilés. Splitter : convolve « rock plate » sur les aigus, decay et IR gain (5:09-5:41). Distorsion après le splitter, compresseur multibande (5:51).
- 6:01 LFO2 → « main tuning » (anciennement master tuning) pour les pitch bends.
- 6:47 Scan = vitesse et sens de lecture. Filtre band-pass « notch » : il faut router l'osc spectral vers le filtre (7:08-7:21).
- 8:06 Warp modes appliqués au spectral.
- 9:06 Essais avec des samples reggae et percussifs (pack Diatic) (9:20).
À vérifier à l'écran : 4:12-4:25 (osc spectral et sample de ride) ; 5:09-5:41 (splitter et IR) ; 6:11 (main tuning) ; 7:21 (routage vers le filtre)

## SE-22 Turn Any Sample Into INSANE Serum 2 Presets! — SoundKiller, 14:39, 2025-07-26, Serum 2
URL: https://www.youtube.com/watch?v=q1k2uxn_Bws
Technique(s) : one-shot de basse importé en wavetable (import « dynamic pitch average »), nettoyage, puis basses et growls
Transcription : oui (anglais, auto). Sponsorisé par Black Lotus Audio (pack « Knights ») de 1:06 à 1:25 et à 9:28.
- 0:40 One-shot de basse glissé sur l'option d'import « dynamic pitch average » : il devient une wavetable (0:51).
- 1:43 LFO glissé sur la position de la wavetable (interp.) : le sample devient un synthé jouable sur toutes les touches (2:02).
- 2:13 Nettoyage : normalize each gain separately, remove DC offset, shift to horizontal (aléatoire) (2:22-2:34). Phases mises au milieu à 50 % (2:45).
- 3:10 Morph « crossfade » (adapté aux samples). « Spectral zero phase » (3:20).
- 3:41 Filtre. LFO ralenti : contrebasse (5:14). Warp (5:43). Unison, car l'import est mono (6:04-6:31).
- 9:50 Autres samples : tearout, growl (10:05-10:56). FM (12:08). Snare transformée en wavetable (13:18).
- 13:50 Fonctionne aussi dans Serum 1, Vital, Phase Plant et Pigments.
À vérifier à l'écran : 0:51 (zones d'import au survol) ; 2:13-2:45 (menu process) ; 3:10-3:20 (menu morph) ; 6:04 (réglages unison)

---

# E. Multisample (Serum 2)

## SE-23 Serum 2 Xfer Records Gratuit Les clés de la composition Oscillateurs instruments multi-échantillons — Tutoriels MAO, 10:41, 2025-10-29, Serum 2
URL: https://www.youtube.com/watch?v=LHGXJfqZt8M
Technique(s) : mode Multisample (SFZ, zones de vélocité, enveloppe override, timbre inversé)
Transcription : oui (français, auto). Lecture commentée du manuel. Promo d'un cours sur bijoustudiomusic.fr.
- 0:16 Principe : des échantillons par hauteur, vélocité et articulation.
- 1:38 En-tête de l'osc A/B/C → « Multisample ». Menu : librairie d'usine ou fichiers SFZ (2:04). Basse d'usine (2:17).
- 2:29 SFZ = fichier texte qui associe samples, notes, vélocités, couches et round robin. SF2 n'est pas supporté, il faut le convertir en SFZ (3:06).
- 3:19 Les zones utilisées s'affichent selon la note et la vélocité jouées (3:34).
- 4:03 Icône d'enveloppe → « override » (4:16) : delay, attack, hold, decay, sustain, release. Clic droit sur le delay → synchro au tempo (1/16, 1/8, triolet, pointé) (5:11-5:25).
- 7:53 « Vel track ». Random = phase initiale aléatoire (8:08-8:22).
- 8:35 Timbre, unisson (désaccord, mix), warp, pan, level (9:01). Le timbre inverse le mapping des zones : les notes aiguës déclenchent les samples graves (9:14-9:47).
À vérifier à l'écran : 1:52 (en-tête Multisample) ; 3:34 (zones de vélocité) ; 4:16 (bouton override) ; 9:14 (bouton timbre)

---

# F. Serum 1 (et techniques valables dans les deux versions) : audio importé en wavetable, noise oscillator, resampling

## SE-24 Creating wavetables in Serum using samples with Virtual Riot | Xfer Records Serum — Splice, 4:45, 2018-12-21, Serum 1
URL: https://www.youtube.com/watch?v=oDft0ubBa9U
Technique(s) : fill de batterie importé en wavetable (dynamic pitch follow), sélection de frames, morph crossfade, import d'un kick en « single cycle », basse dubstep
Transcription : oui (anglais, auto). Présentateur : Virtual Riot.
- 0:11 Fill de batterie tiré d'un pack Splice (« crane pack » [ASR ?]) glissé dans la fenêtre de l'oscillateur.
- 0:26 Modes d'import : « dynamic pitch follow » donne les meilleurs résultats (0:36).
- 0:49 Crayon = mode édition. On choisit quelques frames qui sonnent bien, ici la caisse claire (1:03-1:15), puis « remove all except selected frames » (1:29).
- 1:43 Morph → crossfade entre frames. Normalize all au maximum (1:53).
- 2:17 Warp modes pour adoucir. Un LFO sur la position de la wavetable, un autre sur le warp (2:32).
- 3:25 Kick importé en mode « single cycle » : tout le kick tient dans une frame (3:47). Warp → son « bubbly », plus sub osc et filtre = basse dubstep (3:58-4:11).
À vérifier à l'écran : 0:26-0:36 (zones d'import) ; 1:15-1:29 (sélection de frames) ; 1:43-1:53 (menu morph / normalize) ; 3:25 (mode single cycle)

## SE-25 Using Serum as a Sampler | Chris Gear — Pyramind, 9:33, 2017-10-11, Serum 1
URL: https://www.youtube.com/watch?v=JwAEkVGfV7E
Technique(s) : noise oscillator utilisé comme sampler (key track, one-shot, couche avec un osc), voix longue importée en wavetable, comparaison des modes d'import FFT
Transcription : oui (anglais, auto). Présentateur : Chris Gear.
- 0:18 Le noise oscillator est un sampler. Oscillateurs coupés, noise ON, on dépose un one-shot percussif. Au survol du nom, un « + » vert indique qu'on peut déposer (1:00).
- 1:15 Par défaut il n'y a pas de key tracking : on l'active.
- 1:45 Couche : osc carré −2 octaves, enveloppe ajustée, ce qui renforce le transitoire (1:55-2:39). Pour un son long, enveloppe séparée sur le level du noise (2:49).
- 3:14 Voix longue (« do you feel », très réverbérée) dans l'osc wavetable.
- 3:57 Modes d'import : dynamic pitch zero snap, dynamic pitch follow sans recherche du passage par zéro (4:17-4:32), fixed frame size (4:50), FFT/additif de 256 à 2048 (5:09). 256 = meilleure résolution mais moins d'échantillons (5:47).
- 6:14 Enveloppe/LFO qui balaie la position, 1 mesure, octave en bas (6:30). Essais en 1024, puis plus court (7:16-7:54).
- 8:03 Noise osc en mode one-shot. Un audio sec donne une relecture plus claire (8:24).
À vérifier à l'écran : 1:00 (icône +) ; 1:15 (bouton key track) ; 3:57-5:09 (menu des modes d'import) ; 6:30 (LFO sur la position)

## SE-26 Creating A Hybrid Sampler In Serum (Importing Audio to Wavetables!) — Official AHEE, 11:12, 2020-08-01, Serum 1
URL: https://www.youtube.com/watch?v=uMpzFbokMFo
Technique(s) : « hybrid sampling » : import guidé par la note (formule F2), x-fade des bords, sample brut en couche dans le noise osc
Transcription : oui (anglais, auto). Promo de racks Ableton après 7:54.
- 0:19 Sample mélodique court dont on connaît la tonalité : pluck de kalimba en F (0:28).
- 0:41 Éditeur de wavetable → « enter formula » : taper F2, ce qui prépare l'algorithme à chercher cette fréquence (0:54-1:05). Import.
- 1:05 LFO1 → position sur toute la course, mode envelope, BPM OFF, rate 0,6 (1:17-1:25).
- 1:39 Clic au départ : process, grid size de 8 à 64 sur les deux grilles, « x-fade from edges (grid size) » (1:49-2:09).
- 2:22 Noise osc avec la même kalimba : moteur wavetable + sample brut. Clavier affiché, pitch ajusté (2:30-2:38).
- 2:52 Menu : « copy osc A to B with mods ». Unison 8, octave +1 (3:05-3:13). Delay, reverb, compression, low cut, ping-pong (3:33).
- 3:55 Importé en F3, c'est plus bruité : il faut tester les octaves (4:32).
- 5:01 Orgue en E : E2 affreux, E1 souffle, E0 propre (5:14-6:12). LFO2 sur le level, enveloppe pluck (6:12).
- 6:58 Noise osc en mode one-shot (7:07). Copie A→B avec mods, unison (7:22).
À vérifier à l'écran : 0:54 (champ de formule) ; 1:17-1:25 (LFO1, rate 0,6) ; 1:49-2:09 (grid 64 et x-fade) ; 6:12 (import en E0)

## SE-27 How To Make Vocal Synths In Serum | Importing Audio — Reid Stefan, 16:59, 2019-12-12, Serum 1
URL: https://www.youtube.com/watch?v=C2XW0JPzFt4
Technique(s) : voix importées en wavetable (synthé vocal, plucks, voix parlée en FFT 256), point de loopback, voix brute en couche dans le noise osc
Transcription : oui (anglais, auto). Promo « Kara for Serum » / Whole Loops de 7:44 à 8:22 et vers 14:12.
- 0:28 Quatre samples de voix (Kara, iPhone) passés dans le tuner d'Ableton (la hauteur servira plus tard).
- 0:54 Note tenue : import « constant frame size pitch average » [ASR ?]. LFO1 en mode envelope pour faire défiler, rate 1 seconde, BPM OFF (1:05-1:24).
- 1:24 Éditeur : supprimer les frames vides du début (touche moins) (1:36). Normalize each gain separately (1:54).
- 2:16 Boucle : clic droit sur un point de l'enveloppe/LFO (interp.) → « loop back point ». Utiliser la ligne du milieu comme point de retournement, loopback et point final alignés (2:30-2:44).
- 3:20 Le même sample dans le noise osc (key track, boucle). Filtrer le bourdonnement aigu (3:38). Macro 1 « natural » = level du noise osc (3:53).
- 4:07 Hyperdimension. Vibrato : LFO2 → global master tuning en dose minime, aux = macro 2 (4:22). Macro 3 → filtre/warp.
- 5:06 Deuxième sample : process « zero fundamental phase » [ASR ?], on indique la note D3 (5:23-5:48). Reverb longue + distorsion. Enveloppe sur le drive pour créer un clic de transitoire (6:06-6:22). Compression parallèle, high shelf piloté par env 2 (6:35), passe-haut sous 90 Hz (7:10).
- 9:26 Voix parlée : seul l'import FFT 256 garde les mots, environ 2 s max. Env 1 en BPM, sustain bas (one-shot). OTT, low cut (9:40-10:02).
- 11:11 Note chantée en D, import constant, D4. Enveloppe en boucle avec loopback (11:28-11:42). Start du sample retardé, glide (12:19).
À vérifier à l'écran : 0:54 (mode d'import exact) ; 1:36 (suppression des frames) ; 2:30-2:44 (points de loopback) ; 5:23 (champ de note D3) ; 9:40 (import FFT 256)

## SE-28 Une astuce pour avoir 3 oscillateur dans Serum, ou transformer un sampler en synthétiseur — JB Bouchard - Sound & Life Style, 12:51, 2019-12-21, Serum 1
URL: https://www.youtube.com/watch?v=nUzfbHTkJGc
Technique(s) : cycle d'onde échantillonné et ajouté au dossier Noises, noise osc utilisé comme 3e oscillateur et comme source de modulation
Transcription : oui (français, auto)
- 1:21 Principe : couper un cycle exact. Do4 = 261,63 Hz (1:38). × 60 = 15 697,8 cycles/min, à diviser par 2 plusieurs fois → tempo de 245,28 BPM (2:00-2:24). La formule est dans la description.
- 2:35 Sinus d'Operator enregistré sur piste audio : chaque temps tombe au même point du cycle (3:06). Isoler un cycle, vérifier qu'il boucle, consolider (Ctrl+J) (3:18-3:34).
- 3:48 Copier le fichier dans Documents/Xfer/Serum Presets/Noises, dans un nouveau dossier « custom oscillators » (3:58-4:08).
- 4:08 Noise osc avec key track. Pitch en % : 1 % = 1 demi-ton, 12 % = une octave (4:22-4:33). Accordé à l'osc A parce que l'enregistrement est un Do (4:45).
- 4:59 Warp de l'osc A : clic droit → « mod source » = noise osc (5:14). Quantité réglée par macro 1 via la matrice (5:23-5:36). Level du noise baissé (5:46).
- 5:58 Même principe sur la fréquence du phaser, le chorus, la saturation (6:06-7:03). Onde carrée (7:41). Enveloppe sur le mix d'effet (7:57).
- 8:30 Le même cycle bouclé dans un sampler (Simpler) : le sampler devient un synthé (8:41-9:08). Capturer un cycle d'un son Serum enregistré (9:16-9:49). Un cycle enregistré sur un Do sonnera toujours Do (10:13).
À vérifier à l'écran : 2:24 (tempo 245,28 BPM) ; 3:58 (chemin du dossier Noises) ; 4:22-4:33 (pitch en %) ; 5:14 (mod source du warp)

## SE-29 TUTORIEL XFER SERUM - Le SECRET pour faire des sons ORGANIQUES — Strob Studio Mixing & Mastering, 12:39, 2020-06-14, Serum 1
URL: https://www.youtube.com/watch?v=6rIsJc4gwTk
Technique(s) : import d'instruments acoustiques en wavetable avec la note tapée dans la barre de formule (taille de cycle), nettoyage des frames, morph
Transcription : oui (français, auto, très bruitée : beaucoup de termes déformés)
- 0:07 Importer des sons organiques : basse acoustique, violon, piano. Les modes FFT sont gardés pour une autre vidéo (0:50).
- 1:23 La barre de formule sert à dire à Serum à quelle taille découper.
- 2:13 Connaître la hauteur du sample : basse en F, on tape « F1 » et Serum affiche 505 samples par cycle (2:21-2:45). Valeur en Hz mal transcrite [ASR ?].
- 3:13 Au glisser-déposer, il n'y a plus de choix de mode : découpe à 505 samples.
- 3:42 Avant l'import, enlever le silence du début et raccourcir le sample en gardant l'attaque, fade de fin, consolider (3:50-4:47). Réimport en F1 : cycle stable (4:58).
- 5:16 Supprimer les frames de fin qui se ressemblent (en garder environ 100 sur 149) (5:29-5:43).
- 5:51 LFO en rampe → position. Ajuster la vitesse pour retrouver le timbre original (6:00). Octave en dessous (6:21).
- 6:42 Morph spectral, puis process x-fade / crossfade (grid size) (6:54-7:07).
- 7:38 Violon : hauteur B3, on tape B3. Enlever le silence jusqu'à la frame ~31 (8:02). Morph zero-phase / crossfade / spectral (8:40-9:00).
- 9:16 Piano en B4. Astuce : taper B2 au lieu de B4 donne 4 cycles par frame, donc un autre résultat (9:45-10:18). Morph zero fundamental phase / crossfade (10:41-11:10).
À vérifier à l'écran : 2:21-2:45 (note tapée et nombre de samples) ; 5:29-5:43 (frames supprimées) ; 6:54-7:07 (menu process) ; 9:45-10:18 (import en B2 contre B4)

## SE-30 Tutoriel XFER SERUM - Resampling et Render Modes - [Tuto FR] — Strob Studio Mixing & Mastering, 12:52, 2020-06-07, Serum 1
URL: https://www.youtube.com/watch?v=XdMmQLR0cSU
Technique(s) : RESAMPLING interne (« Resample to osc A », « A+B » stéréo), rendu du warp en wavetable, nouvelle wavetable tirée d'un preset
Transcription : oui (français, auto, bruitée)
- 1:38 Menu : « Render osc A warp » / « osc B warp » créent 256 frames à partir du balayage du warp mode, par exemple sync (1:48-2:11). On peut empiler (mirror…) (2:23-2:48). La frame courante est figée (3:14-3:35). Sauvegarde de la wavetable (4:05).
- 4:16 « Resample to osc A » : rend 1 mesure de la sortie complète de Serum (osc + filtre + FX) en nouvelle wavetable (4:28-4:54).
- 5:11 Exemple avec un preset pluck. Init des modulations, filtre, osc B et sub coupés (5:33-5:43). LFO en rampe sur 1 mesure → position (5:52-6:03).
- 6:48 Deuxième exemple : basse sinus + warp bend + enveloppe de filtre + distorsion → resample. Gain à remonter, warp OFF (6:48-8:12). Sauvegarde en wavetable perso (8:34).
- 9:05 Stéréo : « Resample to A+B » garde gauche et droite (osc A à gauche, osc B à droite, pan à fond) (9:22-10:12). Rampe d'une mesure en mode envelope sur les deux positions (10:33).
- 11:09 Cadenas « lock FX » pour garder la chaîne d'effets en changeant de preset.
À vérifier à l'écran : 1:48 (libellés exacts du menu render) ; 4:16 (resample to osc A) ; 5:52-6:03 (rampe 1 mesure) ; 9:22-10:12 (A+B et pans) ; 11:09 (cadenas)

---

## Écartés
- IU9yAzvJ0nE (BOZNER, « Create Stunning Stutter Effect In Serum 2 ») : stutter fait par un LFO en Hz sur le cutoff, accords wavetable, aucun sample.
- NBHHHp6xWhc (Projektor, « Making Interesting Risers & downlifters in Serum 2!!! ») : riser wavetable + noise + FX, aucun sample importé.
- xEqcK10ApFs (MERAKKI, « How I make Risers for Psytrance/Psytech with Serum 2 ») : sweep de noise, comb, saw, freq shifter, aucun sample.
- WQf_SyPKviM (EDMProd, « How to Resample in Serum 2 for Endless Creative Sounds ») : patch « mudpie » enregistré et découpé dans Ableton. Le retour dans le granular/sampler de Serum est annoncé pour une vidéo suivante (28:49), que je n'ai pas trouvée.
- mVH0fMXmKG8 (Dadda, « Serum 2 Granular Engine Is Great For Psytrance! ») : moteur granular alimenté par une wavetable, pas par un sample audio.
- Écartés sur titre ou métadonnées, sans ouvrir la transcription : Shorts de moins d'une minute (Ur5vZRZDfgY, TDPC3VAXbIw, bFb7jdyL0Lg, o-MnU11cv_Q, sumawwmcnm0, m8aBGDol_pY, 9vPfBer3_zs…), annonces de packs (QhrsZRdyDdU, yEPPdUhdono, kBYVM3wfFxA), tutoriels Ableton Simpler/MPC (8kreWKsu0tg, SMbu3Igd_30, rZc1IQsTDUE…).
- Non vérifiés faute de temps, mais pertinents d'après le titre : vanIYzmwNYI (Selik Sounds, multisample perso), mIK8VyksCVw (Marula Music, multi-sampling), l0Rht7q4ugA (Synth Designer, multisample), Jgg-dOhBLqk / Z55OQxV6zfA (Zen World, EP2 et EP3), OqkwbDZn8ec (Taim Moor, granular sur field recordings), 1sqmwfsSQSQ (Splice, granulizing vocals), m1iZan7IYVg (MERAKKI, ambient pad), GpbsQ9G6g88 (Strob, wavetables from audio, EN), obMMZSS27NA (ADSR, custom noise piano), GAqdYurE6VU (Synth Designer, 4 ways noise osc), 7QDz69-bNYA (MERAKKI, glitch Serum 2).

## Manque
- Trouvés : 30 sur 30, tous vérifiés par la transcription.
- Répartition par version :
  - 23 vidéos Serum 2 : SE-01 à 23.
  - 7 vidéos Serum 1 : SE-24 à 30.
- Répartition par langue :
  - 26 vidéos en anglais.
  - 4 vidéos en français : SE-23, SE-28, SE-29, SE-30. Les trois dernières portent sur Serum 1. Il n'y a qu'un seul tutoriel français sur Serum 2, et il traite du multisample. Je n'ai pas trouvé de tuto français sur le slicing de breaks ou le granular en Serum 2.
- Thèmes encore faibles :
  - RISERS à partir de samples : 1 seul vrai (SE-14). Les autres risers trouvés sont de la synthèse pure.
  - Downlifter sur sample : aucun.
  - Stutter par samples : couvert via relative loop (SE-02, SE-03) et les clips de stutter (SE-07, SE-08). Aucune vidéo n'est entièrement consacrée au stutter sur sample.
- Diversité des chaînes :
  - STRANJAH : 3 vidéos.
  - EDMProd : 3 vidéos.
  - Dash Glitch : 3 vidéos.
  - oddprophet : 2 vidéos.
  - Synth Designer : 2 vidéos.
  - Strob Studio : 2 vidéos.
