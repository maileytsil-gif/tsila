# Études : mixage et mastering « pro » pour la musique électronique (6 octobre 2026)

> Fichier remis par l'utilisateur le 06/10/2026 et intégré tel quel au skill `mastering-outils`. L'étude a été faite dans Claude in Chrome sur le Mac, par la lecture des transcriptions ; aucune vidéo n'a été écoutée et les captures d'écran ne sont pas faites. La synthèse utilisable, par thème, avec ses écarts par rapport aux règles du projet, est dans `mix-master-pro-synthese.md`. Les identifiants (CM-01, LO-01, TO-01, MX-01, BA-01, RE-01, PR-01, OU-01) sont ceux de ce fichier. Les vidéos déjà présentes dans `../../mixer-house-professionnel/references/tutoriels-mixage-par-style.md` sont exclues du corpus.

# Études : mixage et mastering « pro » pour la musique électronique

8 thèmes × 6 vidéos, chacune vérifiée sur sa transcription complète par un agent dans le Chrome de l'utilisateur, en privilégiant les ingénieurs et artistes reconnus. Vidéos déjà présentes dans `etudes-mixage.md` exclues. **Son jamais écouté. Captures d'écran pas encore faites.** Valeurs douteuses de la transcription automatique marquées [ASR ?].

| Thème | Vidéos | Qui enseigne (exemples) | Manques |
|---|---|---|---|
| Chaîne de mastering complète | 6 | Incidence Studio (techno, vinyle), Break (DnB), Zen World | pas de master dubstep ni house classique par un ingénieur |
| Loudness, clipping, limiteur | 6 | Warp Academy, Zerotonine, Strob (mesures Skrillex) | pas de cibles club et streaming pour un même titre |
| Équilibre tonal, EQ, mid/side | 6 | Streaky, Alex Zinn (Point Blank), Virtual Riot, PML | peu de réglages multibande sur de vrais masters techno/house |
| Mixdowns commentés par des pros | 6 | Matt Lange, Dom Kane, Kirk Degiorgio, Nik Roos (Noisia) | aucun Chris Lake, Fred again.., ingénieur de Skrillex vérifiable |
| Bas du spectre, du mix au master | 6 | D Ramirez, Streaky, Warp Academy, Projektor | pas de multibande appliqué au seul grave en master |
| Références, traduction, écoute | 6 | Jesco Lohan (Underdog), Incidence Studio, Protoculture | pas de calibration SPL montrée en direct |
| Pré-master, stem mastering | 6 | Luca Pretolesi, Kirk Degiorgio, Protoculture | stem mastering peu « électronique » |
| Outils pros | 6 | Pretolesi (clipping), Ozone 11, Ableton d'origine, SSL | pas de Pro-L 2 complet par un pro ; aucun StandardCLIP / GClip vérifié |

**Doublon** : la vidéo de JC Concato (LUIXtDO4d8s) est à la fois RE-06 et MX-02. Elle couvre les deux thèmes : 47 vidéos différentes au total.


# Chaîne de mastering et loudness

## Chaîne de mastering complète

### CM-01 How I Master Techno — Full Walkthrough (Isabel Soto • 012 Records) — Incidence Studio, 1:06:08, 2025-12-16, DAW/outils : Ableton Live + iZotope RX (De-clip/Waveform stats, Gain), Sonible true:balance, FabFilter Pro-Q 4, Perception AB, Tone Projects Michelangelo, Shadow Hills Mastering Compressor (Class A), Ozone 12 Low End Focus + Exciter, Basslane (Pro), limiteur à curseur clip/limit (« Limit One » [ASR ?]), Utility
URL: https://www.youtube.com/watch?v=A3uyYgjPWN0
Qui : l'ingénieur d'Incidence Studio (studio de mixage/mastering « spécialisé en musique électronique » selon la description, nom non dit). Master réel d'un titre d'Isabel Soto (« Voluta ») sorti sur 012 (« label de Clio PRC » [ASR ?] ; probablement Cleric (interp.)), destiné aussi au vinyle.
Transcription : oui (anglais, auto) ; chapitres dans la description
- 1:55–2:35 RX, module De-clip + stats de forme d'onde : crêtes proches de 0, corps du morceau vers -6 ; « n'importe quel limiteur commence à se casser au-delà d'environ 4 dB de réduction de gain » ; il refuse de dompter ces crêtes au clipper (distorsion harmonique), il veut un master propre et transparent.
- 3:08–4:17 canal droit plus faible (≈0,33 dB d'écart lu) ; Gain dans RX sur le canal gauche « -1.35 » [ASR ?] ; à corriger AVANT les traitements non linéaires (exciter/saturateur réagiraient différemment à gauche et à droite) et à cause du pressage vinyle.
- 4:52–7:17 réduction manuelle des crêtes, à l'échantillon, en « instant process » Gain : crête à -1,28 ramenée vers -7 ; ≈5 dB de headroom propre gagné ; travail de 14 min, destructif (une nouvelle version de mix = tout refaire).
- 11:58 true:balance avec une courbe cible personnelle faite de références techno (les courbes universelle/électronique ne lui conviennent pas).
- 13:41 ordre : d'abord retirer l'indésirable (résonances), avant tout traitement non linéaire.
- 14:50 Perception AB au début et à la fin de chaque chaîne : bypass à niveau compensé, chaque décision écoutée à loudness égale, souvent les yeux fermés.
- 15:00–20:20 Pro-Q 4 : résonance de la mélodie en bas-médium, bande passée en dynamique puis en mode « resonance suppressor » ; comparaison des modes de phase (natural phase retenu) ; gain statique réduit.
- 21:12–25:40 charley : bande dynamique attaque courte, puis attaque longue pour laisser passer les transitoires ; seuil fixé à la main plutôt qu'en auto (l'auto rééquilibre en continu).
- 26:10–29:30 aigus surtout dans le Side : bell en Side seul ; natural phase acceptable pour un M/S léger, phase linéaire sinon ; automation de gain ≈5 dB ; info Side au-dessus de 8 kHz problématique au pressage vinyle ; 30:05 bascule en shelf, plus bas.
- 31:31–33:43 Michelangelo, profil calibré plat (Plugin Doctor), drive retiré sur les graves, bouton Match pour aligner le niveau.
- 33:53–36:30 Shadow Hills version mastering Class A en mode Digital (même chemin G/D, image stéréo préservée), transformateur Steel (Nickel transparent, Iron colore le bas-médium) ; quasiment pas de réduction de gain, « boîte à groove tonale ».
- 36:52–40:40 Ozone Low End Focus en mode Punch placé avant le Shadow Hills : un peu plus de sub, contraste, la queue de kick « respire » sur système club.
- 41:27–48:30 Ozone 12 Exciter toujours en suréchantillonnage, en M/S : bande ≈200–500 Hz sur le Side pour la densité, puis bande dans le Mid ; écoute du Delta.
- 49:59–53:30 Basslane (Pro) pour la corrélation du bas (mono propre pour le vinyle), léger gain de punch sur le kick.
- 53:47–55:40 limiteur final à curseur clip/limit : 100 % = clipping seul (distorsion sur les kicks), 0 % = limiteur seul (modifie le groove) → réglage intermédiaire ; plafond -1 dBFS, gain de sortie 0 ; « minus 78 left » [ASR ?].
- 56:00–1:01:50 Pro-Q 4 : résonance médium (mid + side) traitée en dynamique + automations « pour servir la narration ».
- 1:02:02–1:04:45 Utility : automation -1,5 dB juste avant le drop pour renforcer l'impact, placée APRÈS le limiteur pour ne pas le pousser.
À vérifier à l'écran : 4:03 valeur exacte du Gain RX (−1,35 ?) ; 11:58 courbe cible true:balance ; 34:20 réglages Shadow Hills (ratio/seuil) ; 43:05 bandes/montants de l'Exciter ; 54:18 nom du limiteur et position du curseur clip/limit.

### CM-02 Pro Mastering Session with Break | Part 1 of 2 — Computer Music / Break, 40:44, 2017-10-04, DAW/outils : DAW non nommée ; Mac Pro, RME, convertisseur Ferrofish, Neumann KH 310 [ASR « kh3 tens »], Yamaha HS5, casques ; FabFilter Pro-L, Ozone Maximizer, UAD Precision Limiter, UAD Oxford Limiter, Acustica (modèle Sontec), Dangerous BAX EQ (UAD), UAD Precision De-Esser, multibande, high/low-pass
URL: https://www.youtube.com/watch?v=ARLu4KyjcVY
Qui : Break (Charlie Break, producteur DnB, label Symmetry), ingénieur mastering pour le service de Cygnus Music ; dit avoir assisté à ~100 sessions de mastering à l'époque du vinyle (Stuart à Metropolis, puis « Bo Thomas » à « 1087 » [ASR ?]).
Transcription : oui (anglais, auto). La partie 2 est réservée au magazine (CM249).
- 2:28 ~100 sessions de mastering suivies ; ne masterise pas sa propre musique quand il a le choix (oreille neuve).
- 6:12 leçon du vinyle : aigus extrêmes = problèmes au tour de gravure → mixer plus lisse.
- 8:26–11:50 écoute : KH 310 + HS5 en contrôle + casque ; écoute à niveau modéré, la distorsion s'entend mieux à faible volume.
- 13:37–15:53 démonstration sur son titre « No Idea » (Break & DLR [ASR]) : version « mauvaise » = kick monté, charley monté, sub coupé ; pics d'aigus vers 10–12 kHz à l'analyseur ; conseil : livrer un prémaster un peu terne plutôt que trop brillant.
- 16:13 même Pro-L sur les deux : le bas de la mauvaise version « farte » sous limitation.
- 18:11 si nécessaire, multibande sur le haut pour égaliser, sans trop toucher la dynamique voulue par le producteur.
- 19:21–21:20 portrait des limiteurs : Pro-L rond/lisse (« fluffy »), Ozone Maximizer net et punchy mais « blocky », UAD Precision mou/old-school, Oxford = petite touche de brillance sans gros gain de makeup ; parfois deux limiteurs combinés à des réglages modérés.
- 21:52 met souvent le limiteur EN PREMIER pour se placer au niveau final puis corriger ce que la limitation révèle ; Cygnus propose des masters « dynamic » ou « loud ».
- 23:15–24:59 niveau visé : un master « fort mais pas écrasé » vers « -5 RMS » sur son mètre ; certains titres actuels sont à « -1 RMS » ; la scène recule sur le loudness (les systèmes club limitent déjà).
- 25:22–27:40 mauvaise version : limiteur ~1 dB de réduction ; multibande sur le kick vers « 120 Hz » [ASR « 200 hungry 20 »], puis sur les aigus déséquilibrés.
- 28:45 high-shelf Acustica (modèle Sontec en réponses impulsionnelles).
- 29:40–31:20 passe-haut/passe-bas en début de chaîne, en phase linéaire ; prudent avec le coupe-bas même à 20 Hz en bass music (perte de poids).
- 32:15 Dangerous BAX en M/S : petite remontée du Side, « 1 ou 2 dB ».
- 33:06 multibande en M/S pour contenir les transitoires du Side.
- 33:38–35:20 UAD Precision De-Esser sur le master vers 6–7 kHz quand le high-shelf fait ressortir les hauts-médiums.
- 38:44–40:30 creux vers 5–6 kHz : souvent laissé (choix du producteur, ex. courbe « en sourire » du jungle) ; sur la mauvaise version, creuser vers 140 Hz pour le kick.
À vérifier à l'écran : 16:13 réglages Pro-L ; 23:20 mètre RMS utilisé ; 25:50 bandes/seuils du multibande ; 32:20 positions du BAX ; 34:30 preset/fréquence du De-Esser.

### CM-03 How I Master My Tech House Tracks — Zen World - EvoSounds, 32:32, 2022-05-18, DAW/outils : Ableton Live (Utility) ; Ozone 9 Imager, Exciter et Match EQ, Mastering The Mix BASSROOM, Brainworx bx_digital V3, Gullfoss, compresseur type SSL, 2 × FabFilter Pro-L 2
URL: https://www.youtube.com/watch?v=sGfwQlDEhJk
Qui : Samuel (Zen World), sound designer/producteur (EvoSounds) ; master final d'un titre tech house co-signé avec XY sur Groove Basement [ASR « goof basement »], master accepté par le label. Dit lui-même ne pas être ingénieur mastering.
Transcription : oui (anglais, auto) ; chapitres dans la description
- 1:20 cible annoncée « -6.9 LUFS ».
- 2:11–3:20 prémaster : crêtes vers -6 dB ; break en moyenne entre -12 et -6 ; drop un peu plus fort que le break.
- 3:49–8:40 Ozone 9 Imager en tête : tout sous 200 Hz en mono (« in mono, always »), bandes de plus en plus larges vers l'aigu (« escalier ») ; Stereoize évité (effet Haas).
- 8:57–11:20 BASSROOM avec 2 références (titres cités [ASR]) : ajustement des bandes du bas sur la cible, petits mouvements.
- 11:25–13:58 Ozone Exciter, preset « thick and fuzzy », bande des charleys très basse en mix (trop dur dans les aigus).
- 13:58–16:50 EQ placée APRÈS la saturation ; bx_digital V3 : manque de hauts-médiums 2–5 kHz ; bande Mono sur le clap à 2,49 kHz, cloche large (« booster large, couper étroit ») ; petite remontée du bas ; bande Stéréo intouchée.
- 17:12–19:10 Gullfoss à faible dose (tame/recover), brightness/bias.
- 19:12–23:30 compresseur : attaque 1–3 ms (jusqu'à 10 ms), release auto, ratio 2:1 ou 4:1 (« la plupart du temps 4:1 »), jusqu'à ~4 dB de réduction, aiguille qui revient à 0.
- 23:42–27:30 au-delà de -8 LUFS : deux Pro-L 2 en série ; le 1er en True Peak, suréchantillonnage 4x, lookahead court, bouton 1:1 (unity gain) pour juger sans biais de volume, release courte, attaque assez haute, style Punchy ; le 2e en preset « Bring out the beat (loud) ».
- 27:58 résultat ≈ -7 LUFS (variations -6,8 à -8).
- 28:20–29:25 Utility APRÈS les limiteurs : volume baissé sur les breaks pour que le drop soit plus fort que la montée.
- 29:31–31:20 Ozone Match EQ (avant limiteur), une instance pour le break et une pour le drop, montant réglé à « 19 ».
À vérifier à l'écran : 5:16 largeurs de bandes de l'Imager ; 15:40 Q et gain du bx_digital ; 21:15 seuil/ratio exacts du compresseur ; 26:30 attaque/release du 1er Pro-L 2 ; 27:58 lecture LUFS finale.

### CM-04 I Studied Mastering for 2 Months THIS is what I learned! | Drum and Bass Tutorial — STRANJAH, 30:30, 2021-02-25, DAW/outils : WaveLab ; Beyerdynamic DT 990 Pro 250 Ω ; TBProAudio mvMeter2 ; Ozone 9 Maximizer + Dynamics ; AMEK EQ 200, bx_digital V3, Dangerous BAX EQ, Shadow Hills, compresseur SSL de mastering (Plugin Alliance) ; « Kramer HLS » [ASR « creamer »] ; FabFilter Pro-MB ; clipper
URL: https://www.youtube.com/watch?v=ITok90g_fEA
Qui : STRANJAH (producteur DnB, Deviant Audio), autodidacte qui synthétise ses sources (Ian Shepherd, Glenn Schick, Andrew Scheps, Break…) ; il précise « ne me prenez pas pour une autorité ». Retenu pour la densité de valeurs sur une chaîne DnB complète.
Transcription : oui (anglais, auto)
- 4:21 prémaster en WAV 24 bits, 44,1 kHz.
- 6:12–7:10 VU (mvMeter2) : 0 VU ≈ -18 dBFS ; aiguille autour de 0 (pas au-delà de +3) ; +1 dB en entrée de chaîne.
- 7:36 limiteur posé dès le départ en fin de chaîne (astuce reprise de Break).
- 8:32–9:55 référence mesurée ≈ -8 LUFS ; Ozone 9 Maximizer IRC IV mode Modern, seuil -7 ; plafond -0,1 ou -0,2 dB contre les inter-sample peaks.
- 10:33–12:10 AMEK EQ 200 : high-shelf au-dessus de 3,5 kHz +0,9 dB ; cloche 2,4 kHz +0,7 dB ; boost plus marqué vers 400 Hz ; largeur ≈120 ; mono maker sous 111 Hz ; sortie -0,2 dB pour comparer à niveau égal.
- 13:06–14:00 bx_digital V3 : Presence +1,3, Bass shift +0,3, shelf aigu -1,5 dB (trop pointu), un peu de bas-médium ; sortie -0,6 dB.
- 15:29–17:40 Pro-MB 2 bandes (sub + kick/basse) pour éviter que le bas ne distorde dans le limiteur ; à sauter si on ne maîtrise pas le multibande.
- 18:21 Kramer HLS : sélecteur grave sur 60 Hz sans gain (bosse de la courbe, astuce Scheps) ; sortie baissée.
- 19:25–21:45 Dangerous BAX (astuce de Break) : high-shelf +1,5 dB à partir de ~7,1 kHz, coupe-haut à 70 kHz (ou 28 kHz) ; low-shelf léger à 84 Hz + coupe-bas.
- 21:55 Shadow Hills compression bypassée, simple passage pour la couleur.
- 22:56 compresseur SSL de mastering : 0,5–1 dB de réduction, section analogique active.
- 24:00–25:35 Ozone 9 Dynamics : sidechain passe-haut (le bas ne déclenche pas le compresseur), ratio 2:1, attaque 75 ms, release ≈100 ms, 1–2 dB de réduction, +1,5 dB de makeup.
- 26:00 clipper : viser ≈1 dB de clipping, écoute du Delta.
- 28:21 référence : remix Foreign Concept de son titre, masterisé par Bob Macc (Subvert Central).
- 28:46 export WAV 16 bits / 44,1 kHz.
À vérifier à l'écran : 9:05 réglages du Maximizer (plafond exact) ; 10:40 fréquences/gains AMEK ; 13:40 bx_digital ; 20:25 crans du BAX ; 25:05 Ozone Dynamics (seuil, ratio).

### CM-05 How To Master A Dubstep Track — BassTi, 8:01, 2026-08-17, DAW/outils : Ableton Live (Utility), EQ, processeur stéréo multibande « M stereo processor » [ASR ? — nom à lire], Newfangled Audio Saturate, FabFilter Pro-L 2, MiniMeters, Stereo Tool
URL: https://www.youtube.com/watch?v=fPxYNhWel1k
Qui : BassTi, producteur dubstep (YouTube, sessions de feedback) ; chaîne qu'il dit utiliser « depuis plus d'un an » sur tous ses titres.
Transcription : oui (anglais, auto)
- 0:10–0:50 pendant la production : aucun effet qui modifie le son sur le master, sortie qui clippe tout le temps (assumé en dubstep).
- 1:02–1:30 nouvelle méthode depuis mai de l'an dernier : plus de clipping « technique » sur les bus (seulement pour le son), un seul clipper sur le master.
- 1:32–2:20 contre le multibande sur le master ; « le mastering est surestimé » ; mix aussi propre et fort que possible, sans pousser le drive du clipper.
- 2:26 Utility : largeur automatisée vers ~70 % à la fin de la montée pour que le drop frappe plus fort.
- 3:02–4:30 processeur stéréo : basse en mono, bas-médium un peu plus large, hauts-médiums plus larges, aigus les plus larges ; le Side paraît plus fort ; mode phase linéaire activé (« très important »).
- 4:31–5:15 Saturate (réglages par défaut), soft clipping, pas de drive : tout ce qui dépasse 0 dBFS est coupé, éléments « soudés ».
- 5:19–6:20 Pro-L 2, style Aggressive (preset), facultatif : « 1 % mieux ».
- 6:43 Stereo Tool : centre fort, côtés très larges.
À vérifier à l'écran : 3:10 nom exact et réglages du processeur stéréo ; 4:40 mode et seuil de Saturate ; 5:30 réglages du Pro-L 2 ; 7:00 lecture LUFS (non dite).

### CM-06 Comment je masterise mon titre électro (Collapse Protocol) — Cerky, 24:20, 2026-06-21, DAW/outils : Ableton Live [ASR « dans un bel ton »] + chaîne hybride : sommateur, « color box » (EQ, compresseur optique, module de spatialisation, « Super Silk » pair/impair), compresseur de bus, 2e color box (image stéréo), EQ elysia [ASR « Elizia Music »], convertisseur A/N ; plugins : clippers, multibande en parallèle, Ozone 11 Vintage Limiter + Maximizer, deux autres limiteurs
URL: https://www.youtube.com/watch?v=GpWbSDjZvR4
Qui : Cerky, producteur électro qui propose mixage/mastering (Cerky Studio) ; 3e épisode d'une série (prod, mix, master) sur son propre titre.
Transcription : oui (français, auto). Peu de valeurs chiffrées : surtout l'ordre de la chaîne.
- 0:31 bus de la session éclatés dans un sommateur puis passage dans le hardware analogique ; travail sur la partie la plus chargée (fin du dernier drop).
- 1:23–2:00 clipper à l'entrée : 1 à 2 dB récupérés « sans que ça s'entende ».
- 2:14–4:00 color box : EQ + compresseur optique + spatialisation + Silk (harmoniques paires/impaires) ; « plus ouvert, plus brillant ».
- 4:05–5:15 compresseur de bus : « nettoie vraiment le bas-médium ».
- 5:17–6:25 2e color box : image stéréo légère, attention à l'équilibre Mid/Side.
- 6:28–8:40 EQ elysia : effet audible à gains nuls ; ajout de sub/bas-médium pour compenser le compresseur ; shelf d'air « à partir de 17 » (kHz ? [interp.]).
- 8:44–9:35 retour numérique par le convertisseur ; loudness encore loin de la cible.
- 9:38–11:20 nouveau clipper (≈1 dB) puis multibande en parallèle, utilisé « un peu comme une compression upward » pour remplir les creux.
- 14:31 EQ de la 1re color box : un peu de bas jusqu'à ≈150 Hz.
- 15:09–17:20 multibande : bande médium remontée et compressée à la fois.
- 17:57–18:40 3e clipper avant les limiteurs.
- 18:45–19:25 Ozone 11 Vintage Limiter en mode Modern, très peu de réduction.
- 19:27–20:15 Ozone Maximizer, fonction soft clip, « boost de loudness ».
- 20:18–21:35 limiteur choisi pour sa couleur (contenu dans les médiums) sans gain d'entrée ; 21:37 dernier limiteur, gain modéré.
À vérifier à l'écran : 2:20 modèles exacts du hardware (color box, Silk) ; 8:16 fréquence du shelf d'air ; 10:30 réglages du multibande parallèle ; 19:00 réglages Vintage Limiter/Maximizer ; 22:00 noms des deux derniers limiteurs et LUFS final.

#### Écartés
- mrl7dWilVCA « Mastering House/Dance Music Start To Finish… » (Sluggy Beats, 30:00, Logic) : chaîne house complète avec valeurs (headroom ≈-6 dB, low-cut Side 140 Hz, Buster SE attaque 3 ms, Pro-L 2 plafond -0,03, cible -8 à -9 LUFS, OS 32x), mais méthode à base de presets, producteur et non ingénieur ; doublon de genre avec CM-03.
- hgRlrmgoNSk « How to MASTER Drum & Bass - Start to Finish » (Inverse Audio/5X, 26:18, FL 24) : bonnes valeurs (EQ 2–3 dB max 5, Side coupé sous ~100 Hz, Ozone Maximizer, -6 LUFS minimum, ≈-5 LUFS final, sortie -0,01), écarté pour ne pas avoir 3 vidéos DnB ; remplaçant direct possible.
- ySRGqLnbXeQ « How I Master Dubstep » (Costic, 21:42) : petite chaîne (1k abonnés), « je ne sais pas trop ce que ça fait » ; valeurs extrêmes intéressantes (≈-2,9 LUFS, double limiteur, soft clip Glue).
- xnTpwu0YbU0 et mLvnRRpQsN8 (Warp Academy, ingénieur « Vespers ») : chaînes de mastering très détaillées mais sur des chansons pop/indie (Angus Wilson), hors musique électronique.
- CVwa5wzPtbQ « HOW TO MIX & MASTER TEAROUT DUBSTEP Part 1 » (LE BAWSKI) : pas de micro selon la description, transcription inexploitable.
- Non ouverts car hors cible ou plus faibles d'après le titre ou la chaîne : yOJ-EtjFD34 (Sage Audio, EDM générique), S_GLWBjVIQM / 3FU143Ox6Nw (Julien Earle, presets), gNijycVW5Tg (343 Labs, live de 2 h), E33o9Nb1Vz8 (VOYOU MUSIC). Le Kevin Grainger (8p4GVCkkjgw) a été laissé de côté : il était ouvert dans l'onglet d'un autre agent.

#### Manque
- Aucun walkthrough complet par un ingénieur mastering reconnu en dubstep/bass music (CM-05 est un producteur, chaîne courte) ; rien en house « pure » (deep/classic) fait par un ingénieur reconnu.
- Pas de session « Mix with the Masters » ou d'académie (Point Blank, Pyramind…) avec un vrai titre électronique trouvée dans ces requêtes ; Pyramind 0OVChRhLQAU (Mac Vaughn, 2016) n'a pas été ouvert.
- Côté FR, une seule vidéo exploitable (CM-06), avec peu de valeurs dites à l'oral.

## Loudness, clipping et limiteur

### LO-01 How to Get the PERFECT Loudness for Electronic Music — Warp Academy, 24:28, 2025-05-06, DAW/outils : Fuel (Music Hack) sur stems + master, Voxengo MSED (solo du Side), filtre passe-bas d'écoute
URL: https://www.youtube.com/watch?v=6IiatlpLSN8
Qui : l'ingénieur de Warp Academy (nom non dit dans cette vidéo ; d'autres vidéos de la chaîne le présentent comme « Vespers » (interp.)). Stem-mix + master d'un titre DnB de Ritual X (Liam Shy), « Dial Tone ».
Transcription : oui (anglais, auto) ; la description liste les « signes d'un master trop cuit »
- 0:24 l'autre extrême : des masters à -2, -1 LUFS, voire positifs.
- 1:52–2:25 protocole : même mix rendu de -14 à -2,5 LUFS intégrés (mesure sur le drop), puis tous normalisés au même loudness pour comparer à l'aveugle.
- 5:09–6:30 à écouter : distorsion sur ce qui était propre (sub, voix, pads), dans les parties calmes, sur le Side ; IMD, ex. 808 à 30 Hz → produit à 15 Hz.
- 6:38–7:30 batterie molle (le corps gonfle par rapport au transitoire) ; mesure du crest factor et surtout du PSR (peak to short-term loudness ratio).
- 7:32–9:30 perte de largeur et de profondeur (reverbs du Side distordues) ; perte de poids dans le bas ; dureté aiguë (IMD, aliasing) ; écoute au passe-bas pour vérifier que le bas pulse encore (« saucisse ») ; drop pas plus fort que la montée.
- 11:03–12:30 -14 et -10 : trop polis, pas de « gel » ; le gel apparaît vers -8, mieux à -6 ; -2,5/-3 = « hot garbage ».
- 13:19–14:10 zone idéale pour CE titre : -6 à -4 ; -6 le plus propre (meilleur sur PA) ; DnB plus fort que house/techno/trance ; une partie de la DnB à -4/-3.
- 14:14–16:30 -5 : distorsion plaisante sur le Side de la basse ; -4 : distorsion sur la voix lead → inacceptable.
- 17:07 choix final -5 pour un titre DnB ; 17:25 vérification au Side seul (MSED) : craquements à -4.
- 22:20 il affirme que le titre de Skrillex/Flowdan/Fred again.. récompensé aux Grammy 2024, masterisé par Luca Pretolesi (Studio DMI), est « un peu moins fort que -6 » dans le drop.
À vérifier à l'écran : 2:05 liste des rendus (pas exacts) ; 7:25 lecture PSR ; 17:30 réglage MSED ; 22:25 lecture LUFS citée.

### LO-02 HOW TO MASTER LOUD - INSTANTLY Get FAT, Clean + In Your Face Results — Warp Academy, 16:46, 2024-05-06, DAW/outils : DMG Limitless, Voxengo SPAN (référence en sidechain)
URL: https://www.youtube.com/watch?v=YpbV0INpHgc
Qui : même ingénieur Warp Academy (interp.) ; mix d'artiste comparé à son propre re-mix, même chaîne de mastering. Genre non nommé (morceau avec drops).
Transcription : oui (anglais, auto) ; chapitres dans la description
- 0:18–0:50 thèse : plus de « quelques dB » de réduction au limiteur n'est ni normal ni nécessaire ; zone « loud » visée : -8 à -5 LUFS dans les drops/refrains (pop, hip-hop, électronique).
- 1:06–1:40 à 5–6 dB ou plus de réduction : IMD, aliasing, transitoires ternes, pompage.
- 3:24–4:05 protocole : les deux mix normalisés à 0 dBFS sample peak, chaîne copiée, seuil du limiteur ajusté pour une réduction de gain identique.
- 5:06 avant mastering : mix d'origine ≈-14 LUFS intégrés dans le drop, son re-mix ≈-11.
- 9:15–10:00 ≈3 dB de réduction sur les deux : la version d'origine sort à -8,9 LUFS, la sienne nettement plus fort ; 2–3 dB de limitation = acceptable, sans artefact audible.
- 11:15–14:30 cause : des pics isolés toutes les 4–7 temps, longs de 2–3 échantillons, ≈2 dB au-dessus ; à traiter DANS LE MIX (hard clip, limitation/compression manuelle sur les sons), pas sur le master.
À vérifier à l'écran : 5:10 LUFS des deux mix ; 9:20 réduction de gain et LUFS sur Limitless ; 12:45 zoom sur les pics (dB) ; 7:00 réglages Limitless.

### LO-03 TUTORIAL: Clipping vs. Limiting - What To Use When And Why? — Zerotonine, 36:53, 2020-12-25, DAW/outils : Ableton Live ; Newfangled Audio Saturate (clipper spectral), FabFilter Pro-L 2 (style Aggressive), StandardCLIP (hard clip, OS 8x, mode ratio 2:1)
URL: https://www.youtube.com/watch?v=qusleJDVwSg
Qui : Zerotonine, producteur de musique électronique (bass/EDM) ; démo sur boucles puis cas « réel » de gain staging par clipping.
Transcription : oui (anglais, auto)
- 0:33–2:50 schéma sinus : le limiteur réduit l'amplitude ; le soft clip arrondit le haut ; le hard clip coupe net au-dessus du seuil.
- 3:30–5:05 transitoires (batterie) : le hard clip est souvent le plus transparent, le limiteur ramollit l'attaque ; sons tenus : plutôt le limiteur.
- 5:47–7:10 Saturate = clipper spectral (clippe moins le grave, plus l'aigu) : entre clipper et limiteur.
- 7:33–8:39 StandardCLIP en hard clip ; soft = plus de distorsion ; mode ratio 2:1 (compresse 50 % puis clippe), « certains ingénieurs mastering l'utilisent » ; instance en suréchantillonnage 8x.
- 9:17 les limiteurs avec attaque ont un étage de clip en sortie (ex. Pro-L 2 Aggressive).
- 16:03 / 20:46 basse filtrée ou matériau très grave : la distorsion du clipper s'entend → limiteur ; Saturate bien plus propre que StandardCLIP sur le grave.
- 17:52 suréchantillonnage : plus propre dans le grave.
- 24:04–25:15 musique bass/EDM très forte → garder un crest factor bas dans le mix pour aider le mastering.
- 26:05 2–3 dB de clipping généralement inaudibles ; 27:11 limiteur seul ≈-3,5 dB de réduction.
- 28:23–31:40 clip par piste : kick ≈2 dB de headroom gagné, clap ≈2 dB, synthé ≈4 dB ; clipper de bus +0,5 à 1 dB.
- 31:55–34:40 limiteur final : 2 dB de réduction en moins, kick plus percutant, mix plus focalisé ; 35:52 le limiteur final n'a plus qu'≈3 dB à faire.
À vérifier à l'écran : 7:45 réglages StandardCLIP (seuil, OS) ; 10:30 réglages Pro-L 2 Aggressive ; 27:15 mètre de réduction du limiteur ; 28:45 vumètres par piste.

### LO-04 LA VERITE SUR LE TRUE PEAK - Les facts ! — Strob Studio Mixing & Mastering, 8:15, 2024-03-28, DAW/outils : iZotope RX (Loudness Control, stats hors ligne)
URL: https://www.youtube.com/watch?v=nV-9DnoaL3U
Qui : Strob (Strob Studio, ingé mix/mastering FR, « près de 20 ans dans le game » selon la description). Analyse des fichiers WAV du dernier album de Skrillex (masterisé par Luca Pretolesi, Studio DMI).
Transcription : oui (français, auto). Une partie de la vidéo fait la promo de sa formation.
- 0:00 mythe visé : masters à -14 LUFS et -1 dBTP.
- 0:55–1:45 true peak = estimation de ce que sortira le convertisseur après filtre de reconstruction (« lissage ») ; le fichier, lui, est à 0 dBFS.
- 1:51 la recommandation Spotify de -1 dBTP s'adresse aux distributeurs, pas aux ingénieurs mastering.
- 3:18–4:30 RX Loudness Control sur les titres de Skrillex : true peak +1,6, +1,9, +2,4 (« Joker »), +2,4 (« Ratata ») dB au-dessus de 0.
- 4:59–6:15 limitation true peak (suréchantillonnée) : ne supprime pas tous les dépassements, et limite davantage pour un même loudness → « 99,9 % » des gens ne l'activent pas en électro.
- 6:17–6:45 alternative : baisser de 2,4 dB → TP à 0,0 mais 2,4 dB de loudness perdus.
- 6:58–7:35 garder une marge = master moins fort que les autres ; selon lui, les masters du commerce dépassent 0 dBTP.
À vérifier à l'écran : 4:13–4:30 valeurs RX (TP, LUFS intégrés, PLR) de chaque titre ; 6:35 réglage de gain et nouvelle mesure.

### LO-05 Mastering Loudness: How Loud Should House Tracks Be? — Olean's House, 17:09, 2025-03-06, DAW/outils : Voxengo SPAN (RMS), Youlean Loudness Meter (LUFS)
URL: https://www.youtube.com/watch?v=dQG2Ya_5w6c
Qui : Olean's House (producteur house, chaîne d'enseignement) ; mesures sur des sorties house du commerce et du Bandcamp underground.
Transcription : oui (anglais, auto) ; chapitres dans la description
- 0:23 dilemme : Spotify -14 LUFS contre labels qui demandent -8 LUFS.
- 1:07–2:00 titres house : RMS -10 / ≈-8,8 à -9 LUFS ; -8,55 LUFS / RMS -9,0 ; -10,3 LUFS / RMS -11,2.
- 2:26–3:10 titre « DJ S… » [ASR] : RMS -8 / -6,7 LUFS ; titre de Fisher : RMS -7 / -5,6 LUFS (le plus fort).
- 3:20–4:00 titre underground Bandcamp : -11,7 LUFS / -11,6 RMS → plage du commercial ≈-6 à l'underground ≈-12.
- 4:05 normalisation Spotify : à oublier en dance music (et désactivable).
- 6:48–9:10 Fletcher-Munson ; démo sinus : le LUFS monte avec la fréquence à niveau égal.
- 10:32 titre « chill » : -10 LUFS / -11,5 RMS ; titre avec kick et basse longs : -8,5 LUFS / -10 RMS.
- 11:02 cibles proposées pour une house « bouncy » : -10 RMS et -9 LUFS (moins pour du chill, plus avec beaucoup de basse et des kicks longs).
- 12:19–14:30 le LUFS monte quand voix/synthés entrent ; productions commerciales (Fisher) au spectre plat → plus fortes ; underground en « baignoire ».
- 14:42–16:10 réédition vinyle à -11,8 / -11,7 et autre titre à -13 / -13 : trop faibles ; en club, les crêtes peuvent faire couper le sub par le système → refaire un master (limiteur + EQ) avant de jouer.
À vérifier à l'écran : 1:10–3:10 lectures Youlean (intégré vs short-term) ; 11:00 valeurs des titres cités ; 15:40 réglages limiteur/EQ appliqués.

### LO-06 LOUDNESS, MASTERING, MIX AND STREAMING — Joachim Garraud, 26:29, 2020-11-20, DAW/outils : limiteurs Ozone, FabFilter et DMG ; test de nul (inversion de phase) ; VU-mètre
URL: https://www.youtube.com/watch?v=a0qxyTJwV7A
Qui : Joachim Garraud (DJ/producteur électro français) ; exposé tiré de son émission live du 19/11/2020.
Transcription : oui (français, auto). Plus conférence que tuto : quelques affirmations historiques à vérifier (anecdote Bob Ludwig, cible « -24 »).
- 1:05–2:15 anecdote : Bob Ludwig et une machine de gravure vinyle modifiée pour +16 dB (à vérifier).
- 7:09–8:15 1924 : 60 dB de dynamique, 0,3 % de distorsion ; 1996 : limiteur brickwall numérique → aujourd'hui jusqu'à 20 % de distorsion et ~12 dB de dynamique.
- 9:06–11:10 dynamique tolérée selon le lieu : cinéma 60 dB… avion 12 dB ; la musique actuelle tourne autour de 12 dB.
- 11:48 ≈24 dB d'écart entre une musique de film et un titre rock ; 13:22 cible « -24 dB » de la télévision [à vérifier].
- 14:44 niveau électrique (RMS) ≠ loudness perçue.
- 15:47–18:20 trois limiteurs (Ozone, FabFilter, DMG) sur un reggae ; test de nul : chaque limiteur ajoute sa propre distorsion = sa couleur.
- 19:25–22:00 trois mix (jazz RMS -16 dB, deuxième -9 dB RMS, troisième très compressé) ramenés à -16 RMS (comme une plateforme ; « -14 comme Spotify ») → le plus dynamique paraît le plus fort.
- 23:12–24:20 conseils : de l'air, une forme d'onde qui n'est pas un « pavé » ; les styles EDM/DnB [ASR « le dm, le dr »] utilisent le limiteur de façon artistique.
- 25:09 VU calibré (ex. -12 dB), mixer autour de 0 VU avec une aiguille qui bouge.
À vérifier à l'écran : 13:40 tableau des cibles des plateformes ; 15:50 réglages des trois limiteurs ; 20:10–20:55 lectures RMS ; 25:20 calibrage du VU.

#### Écartés
- 77IZ_ea_me0 (Mike Kalajian, URM, 5:11) : très concret (clip d'abord, +8 dB de gain via le clipper, +3 dB de limitation → ≈-6 LUFS) mais sur du metal, hors genre.
- 1b0TfgnpWzo (Panorama, Nicholas Di Lorenzo, 9:36) : ingénieur mastering, clipper en tête de chaîne, soft clip « Pro » = courbe log 2:1 réglée sur l'écart crête/corps (ex. crête -5,3, corps 5 dB dessous → transfert 2,5 dB). Excellent sur le fond, mais le genre du morceau n'est pas dit → gardé en remplaçant de LO-06.
- 4RMIgKGF2Zg (Matthew Vere, « How Skrillex Uses Limiters and Clippers ») : théorie générique, aucune session de Skrillex, peu de valeurs.
- 6d-zblNLA_4 (woodenhouse studio, FR, 13:55) : clipper/limiteur true peak par bus (kick 1,3 dB, basse 2 dB, ≈-12 LUFS, PLR 10–11), mais sur un groupe d'impro jazz.
- Qyp5q6Ont84 (Hardcore Bob, StandardCLIP) : ton humoristique, morceau trap, peu de méthode.
- Non ouverts (titres génériques/débutants ou Shorts) : vidK3mE5Mn0 (EDM Tips), 5pKbIRxhxIw (Mastering.com, généraliste), APQZdOxM2EU / pw6a4d-YjU0 (Strob, doublon de chaîne avec LO-04), 5sAm7McrkA0 et 7OHRutnSWl8 (Warp Academy, déjà deux vidéos de la chaîne), siopG7VK6mk (Arc Nade DnB).

#### Manque
- Aucune vidéo trouvée où un ingénieur mastering reconnu donne une cible chiffrée « club » et une autre « streaming » pour le même titre électronique (ni deux masters livrés).
- True peak spécifique DnB : seulement LO-04 (Skrillex/dubstep) ; aucune mesure TP sur des masters DnB.
- Pas de contenu d'académie (iZotope, FabFilter, SSL, Sonnox) dédié au gain staging vers le limiteur sur un titre électronique dans ces recherches.
- FR : LO-04 et LO-06 seulement ; LO-06 reste théorique.

# Équilibre tonal et mixdowns de pros

## Équilibre tonal, EQ et mid/side

### TO-01 How To EQ Dance Music — Streaky (Streaky), 14:27, 2026-05-17, DAW/outils : FabFilter Pro-Q 4 (DAW non montré dans la transcription)
URL: https://www.youtube.com/watch?v=hGvJJAyHRyg
Qui : Streaky, ingénieur de mastering britannique (30 ans de métier selon la description ; Metropolis et Battery Studios ; crédits Lily Allen, Shanks & Bigfoot, Groove Armada, Skepta…). Il présente son preset Pro-Q 4 « dance music » sur un morceau house.
Transcription : oui (anglais, piste auto, texte propre)
- 1:12 Coupe-bas **sur le Side uniquement** (stereo placement = Side) vers **80 Hz** à la place d'un mono maker : grave plus serré, et plus facile à graver sur vinyle.
- 2:15 Il travaille du bas vers le haut : si le grave et le bas-médium sont justes, il faut moins d'aigu (« un peu de poussière de fée » plutôt qu'un aigu poussé fort).
- 3:12 Low shelf à **20 Hz, −1 dB**, Q remonté pour créer une petite bosse d'environ **+0,5 dB vers 40 Hz**. Ça retire de l'énergie avant le limiteur, qui peut alors monter plus fort.
- 5:01 EQ dynamique vers **60 Hz** sur le kick, plage dynamique réglée à **+2 dB** : la bande ne monte que quand le kick frappe.
- 6:28 Creux à **160 Hz**, Q étroit, en mode dynamique, **−0,5 à −1 dB** contre la boue après le kick. Règle donnée : « coupes étroites, boosts larges » en mastering.
- 7:56 Boost large et dynamique vers **240 Hz** pour le poids du bas-médium.
- 9:05 High shelf **~1,7 kHz, ~1 dB, sur le Mid seulement**, pente adoucie pour qu'il démarre vers **500 Hz**. Ça recentre l'attention et donne de la présence.
- 10:34 Coupe en **mode spectral**, large, vers **5–8 kHz** contre la sibilance de la voix (plus haut pour des cymbales agressives) ; il le compare à soothe.
- 11:52 Boost dynamique **sur le Side uniquement vers 8–10 kHz** : forme « en tulipe » avec le grave mono et un aigu plus large. Monter le gain élargit le haut du spectre.
- 13:17 Le shelf Mid à 1,7 kHz et l'aigu Side se complètent (interp.).
À vérifier à l'écran : 1:20 (pente et fréquence exactes du coupe-bas Side) ; 3:20 (Q du shelf 20 Hz) ; 5:10 (seuil et plage de la bande 60 Hz) ; 6:40 (valeur du Q à 160 Hz) ; 12:00 (fréquence et gain du boost Side).

### TO-02 why your mixdown is shit - tonal balance, brightness equals loudness — Polarity Music (Polarity), 40:25, 2022-02-23, DAW/outils : Bitwig (EQ+, FX-3, Grid « Reference Level »), Voxengo SPAN, Ozone 8 Match EQ, Peel ; exemple drum & bass
URL: https://www.youtube.com/watch?v=WShnVQ9uOkc
Qui : Polarity, producteur DnB/ambient et formateur Bitwig (chaîne Polarity Music). Ce n'est pas un ingénieur de mastering crédité.
Transcription : oui (anglais, auto)
- 0:00 Thèse : l'équilibre fréquentiel avant le limiteur ou le clipper compte plus pour le niveau perçu et la propreté qu'écraser la dynamique ; l'énergie vers **1 kHz** donne une impression de volume.
- 1:28 Repère visuel : analyseur incliné. **3 dB/oct = bruit rose** (« un peu trop brillant » selon lui), il utilise **4,5 dB/oct** (« tilt 4,5 dB per octave » dans Bitwig). Une courbe plate à l'écran veut dire équilibrée. Le réglage ne touche que l'affichage, pas le son.
- 5:24 Démo à l'oscilloscope : la basse atteint le plafond d'un limiteur large bande avant le reste ; la « porteuse » se déforme et toutes les harmoniques au-dessus avec.
- 8:48 EQ à la main jusqu'à la ligne droite à 4,5 dB/oct : plus fort à pic égal, et le limiteur travaille moins.
- 10:44 Ozone 8 Match EQ : capture, cible bruit rose, **amount 10–15 %**, appliqué en cascade sur le bus drums, le bus DnB puis le master.
- 12:43 Mise en garde contre les mixdowns trop brillants : trouver le juste milieu selon le genre.
- 14:40 Il est passé d'une cible bruit rose à une cible « 6 dB » plus douce dans l'aigu [ASR ? « 60p guide » / « 6 db »].
- 15:29 « Multibande du pauvre » : FX-3 à 3 bandes, un limiteur par bande poussé jusqu'au plafond, puis hard clip sur les drums.
- 19:11 Variante à 10 bandes en passe-bande, chacune avec son outil Reference Level (normaliseur temps réel avec seuil) ; 26:54 version avec Peel, qui donne des artefacts FFT.
- 28:57 Exemple DnB : drums ~**+5 dB** au-dessus de 0 → FX-3 + clipper, drive ~**1–2 dB** ; 31:41 basse au limiteur puis **−3 dB** ; bus DnB : Match EQ puis hard clip ; 38:20 résultat **−4,3 LUFS** [ASR « minus 4.3 loves »] avec seulement drums et basse.
À vérifier à l'écran : 2:01 (réglage de pente dans l'EQ et l'analyseur) ; 11:44 (amount de Match EQ) ; 14:46 (nom exact du guide qui remplace le bruit rose) ; 31:01 (gain du clipper) ; 38:20 (valeur LUFS et type de mesure).

### TO-03 The curve that forever changed my mixdowns — Virtual Riot (Virtual Riot), 7:46, 2025-12-18, DAW/outils : Ableton Live 12.3 (EQ Eight, Envelope Follower, Rack), Serum
URL: https://www.youtube.com/watch?v=oofC3jkmaU8
Qui : Virtual Riot (Christian Valentin Brunn), artiste dubstep et bass music connu, sur sa propre chaîne.
Transcription : oui (anglais, auto)
- 0:17 Fletcher-Munson et courbe d'isosonie ; le bruit rose ou brun n'est qu'un bruit blanc passé dans une EQ tilt, pour paraître équilibré à l'oreille.
- 1:49 Zones de sensibilité maximale : **500–1000 Hz** et surtout **3–5 kHz**. Le sub est très peu perçu.
- 2:44 Ses règles : dureté → regarder **2–4 kHz** ; boue → **~500 Hz** (pour lui plutôt **200–400 Hz**, 4:07). EQ soustractive avant tout.
- 4:17 Sur le master aussi : léger creux **2–4 kHz** quand tout le morceau est un peu dur. C'est la zone qui fatigue l'oreille en premier quand on monte le volume.
- 4:58 Sa multibande de mastering : sub **≤ 110 Hz, ratio 8:1** ; **> 6–7 kHz, ratio 7:1** ; les médiums sont moins compressés parce que l'oreille y perçoit mieux les variations de niveau. Il clippe à la fin.
- 6:12 EQ dynamique maison : EQ Eight en filtre passe-bande raide (pentes ×4) sur **2–5 kHz**, puis Envelope Follower (réglages « 50 » et « 0 ») mappé sur le gain d'une bande en chaîne parallèle. C'est un « mini soothe » (preset gratuit sur son Patreon).
À vérifier à l'écran : 2:59 (courbe d'EQ inspirée de Fletcher-Munson, gains) ; 4:20 (creux sur le master, gain et Q) ; 5:05 (seuils et réglages de la multibande) ; 6:48 (mapping de l'Envelope Follower).

### TO-04 Tonal Balance Control - Mixing & Mastering with OZONE 8 & Ableton 10 — Production Music Live (Guido / Cat and Beets), 14:36, 2018-05-06, DAW/outils : Ableton Live 10, iZotope Tonal Balance Control (Ozone 8)
URL: https://www.youtube.com/watch?v=wR1uaAiW9d0
Qui : Guido (« Cat and Beets »), formateur mixage/mastering de PML (académie). Il compare un template PML « style Joris Voorn » aux sorties de Joris Voorn [ASR : « Yoda's foreign »].
Transcription : oui (anglais, auto)
- 2:44 Setup de référence : groupe « reference » avec solo mappé sur la touche **1**, chaîne de mastering coupée par la même touche. On bascule A/B sans écart de niveau (attention au double limiteur).
- 5:24 D'oreille d'abord : les références ont plus d'aigu et un creux dans le grave ; le template a une bosse dans le grave et un creux dans l'aigu. Il faut donc « inverser » la courbe.
- 6:42 Ne pas prendre les cibles fournies (Bass Heavy, Modern, Orchestral) : construire une **cible personnalisée** à partir des références.
- 8:25 Mieux : consolider (**Cmd+J**) **seulement les drops** des références et en tirer une cible « drops ». Elle est plus serrée et plus pertinente.
- 10:15 Résultat : grave et bas-médium trop forts, haut-médium et aigu trop faibles ; vue **Fine** (11:01) ; alt-clic pour solo une zone et trouver le coupable (hats à monter, clap, lead à baisser).
- 12:04 Hypothèse sur le son de référence : compresseur avec sidechain interne filtré qui laisse le grave tranquille, accent à partir de ~**150 Hz**, attaque lente, release rapide (interp. de l'auteur).
- 13:26 Indicateur **Crest factor** du grave : vers la droite = grave écrasé (« saucisse »), vers la gauche = plus dynamique.
À vérifier à l'écran : 3:20 (mapping des touches) ; 7:10 (création de la cible) ; 10:15 (écarts par bande) ; 11:10 (vue Fine) ; 13:30 (lecture du crest).

### TO-05 Mastering Dance Music in Ableton Live Part 1: Creating a Mid/Side Matrix — pointblank music school (Alex Zinn), 8:35, 2015-07-02, DAW/outils : Ableton Live (Utility, EQ Eight)
URL: https://www.youtube.com/watch?v=t8WaJVYzNTE
Qui : Alex Zinn, ingénieur de mastering à Miami : labels techno Osmosis Audio et Typ3 Records, a travaillé pour Richie Hawtin (ENTER.). Morceau « Gears and Screws » de « Coryu » [ASR ?], sorti sur Osmosis.
Transcription : oui (anglais, auto)
- 0:53 Objectif : sonner au mieux en club. Beaucoup de clubs ont un sub mono, parfois tout le système.
- 1:43 Matrice M/S avec les outils d'Ableton : piste originale + copie passée en mono avec phase inversée dans Utility → sommée = **Sides seulement**, routée vers un « stereo bus ». Une copie mono sans inversion va vers un « mono bus ». Les deux bus vont dans un **sum bus**, et il garde une copie « unprocessed » pour l'A/B.
- 2:31 **Warp désactivé** pour masteriser dans Ableton (sinon artefacts).
- 3:27 À la réception : vérifier le headroom, et qu'il n'y ait ni compression ni brickwall sur le bus master ; sinon demander un nouveau fichier.
- 5:34 Mono bus : coupe-bas **< 30–35 Hz** (inaudible sur les enceintes, souvent filtré en club, et ça mange le headroom). Coupe étroite **200–500 Hz** d'environ **1–2 dB** (balayer avec un boost pour trouver la zone).
- 7:01 Stereo bus : retirer le grave boueux en gardant le « room tone ». À l'A/B, basse plus serrée et image plus large, uniquement à l'EQ.
- Complément même série, même auteur (apQO4kzPevU, Part 3, 10:17) : 0:51 Saturator sur le mono bus pour les petits haut-parleurs ; 4:06 EQ finale : roll-off grave et aigu (aliasing après saturation) ; 6:40 mesure RMS (Simple RMS Meter M4L) : techno entre **−10 et −8 dB RMS**, jamais au-delà de −8 ; ~**3 dB** de réduction de gain ; plafond « minus three, minus four » [ASR ? probablement −0,3/−0,4 dBFS].
À vérifier à l'écran : 1:55 (réglages d'Utility, inversion de phase) ; 5:50 (fréquence et pente du HPF mono) ; 6:55 (fréquence et Q de la coupe 200–500 Hz) ; 7:20 (EQ du stereo bus).

### TO-06 iZotope Ozone 7 Tutorial: Mastering Dance Music Part 2 (EQ and Compression) — pointblank music school (Anthony Chapman), 10:30, 2015-12-04, DAW/outils : iZotope Ozone 7 (Vintage Compressor, Vintage EQ, Imager)
URL: https://www.youtube.com/watch?v=EWogiUlpTrY
Qui : Anthony Chapman, formateur Point Blank (académie). Mastering d'un morceau dance (artiste « Debukas » [ASR ?]).
Transcription : oui (anglais, auto)
- 0:23 Rappel de la partie 1 : tape vintage + Imager, **grave mis en mono** dans l'Imager (cité à 2:16).
- 1:30 Vintage Compressor en **mode M/S** pour rééquilibrer mid et side, les pads ressortent.
- 2:56 Side : gain **+7,6 dB** pour environ **3 dB** de compression ; Mid : **2–2,5 dB** de réduction, **+2 dB** de makeup.
- 3:37 Attaque **24 ms** (défaut), release **~100 ms** des deux côtés ; 3:54 filtre de détection qui coupe le grave pour que le kick ne fasse pas « pomper ».
- 4:56 Makeup à l'oreille : 2 dB de réduction ne veut pas dire 2 dB de makeup.
- 5:30 Vintage EQ (type Pultec/Neve) en M/S : Sides → coupe-bas pour resserrer, creux dans le médium, boost haut-médium, **boost aigu à partir de 8 kHz** ; 7:30 coupe-bas **45 Hz** ; 8:33 Mid → boost très haut perché (« sparkle »), Q ajustable.
- 9:25 En bypass : moins brillant, bas-médium plus épais, et du grave revient dans la stéréo. Le M/S corrige ce point.
À vérifier à l'écran : 3:00 (gains et seuils M et S) ; 3:40 (attaque et release) ; 4:05 (fréquence du filtre de détection) ; 6:50 (bandes du Vintage EQ Side) ; 8:35 (fréquence du boost Mid).

#### Écartés
- 44VRYB4122g « EQ MID/SIDE MASTERING (tips de mastering) », Mixfield (FR, 9:44) : bonnes valeurs (coupe-bas Side 67 Hz, Side +~135 Hz, Mid +1/Side −1 dans 1–3 kHz, aigu dynamique Mid −2 dB) mais sur un morceau rap/808, hors électro.
- _NUXm8pslt0 « Mid Side EQ in EDM Mixing and Mastering », Beat Tweaks (20:29) : méthode claire (MSED, coupe-bas Side jusqu'à ~100 Hz) mais presque aucune valeur dite, auteur peu identifié.
- dqnDCoa2YA8 « MID-SIDE ANALOG MASTERING for BASSLINE JUNKIE », Rob Ryda (27:17, 345 vues) : vrai master M/S analogique d'un morceau jungle/DnB (référence à −4/−5 LUFS baissée de 15 dB, premaster −18 LUFS, Mid +63 Hz, 6,3 kHz, sibilance 8 kHz, transitoires à partir de ~700 Hz, EQ dynamique SSL Bus+). Écarté parce que l'ingénieur est peu reconnu et les valeurs approximatives. Bonne réserve.
- LGfviOcA-w4 « V4lve - Mid/Side Mastering Saturation », Sonic Academy : démo de leur propre plugin, aucune valeur (conseil seulement : saturer le Mid, élargir avec un imager).
- Vus en recherche, non retenus : iZotope « Pro sounding mix with TBC » (QruneruRYsc, générique), Strob Studio TBC2 (dpXCfbAbBMg, FR, non vérifié faute de temps), Matthew Vere « Skrillex M/S » (3:56, pas Skrillex lui-même), Sage Audio EQ dynamique (tvuBplNrYMs, pas spécifique à l'électro).

#### Manque
- Pas de vidéo d'un ingénieur de mastering électro en EQ dynamique ou multibande pure (soothe, Pro-MB) qui donne seuils et ratios sur un vrai master techno ou house : seuls Streaky (EQ dynamique Pro-Q) et Virtual Riot (ratios multibande) donnent des chiffres.
- Pas de source française solide sur l'équilibre tonal en électro (Strob Studio TBC2 à vérifier).
- Mesures précises de largeur au master (corrélation, % de l'Imager) quasi absentes.

## Mixdowns commentés par des pros

### MX-01 Electronic Music Mixing Masterclass with Matt Lange [mau5trap records] — SonicScoop / MixCon (Matt Lange), 55:57, 2018-08-16, DAW/outils : Pro Tools ; DMG Equilibrium, Valhalla VintageVerb, Newfangled Elevate, Manley Massive Passive, Townhouse Bus Comp, Black Box HG-2, bx_digital (mono maker), SSL Brainworx, bx_room, FabFilter Pro-R, Eventide Blackhole, Unfiltered Audio BYOME, Replika, Echoboy, compresseur Avid
URL: https://www.youtube.com/watch?v=HwZaRP-lbzg
Qui : Matt Lange, artiste mau5trap, producteur et mixeur de 30 Seconds to Mars, musique de Counter-Strike: GO. Il commente le mix de son propre morceau techno « Are You, Am I ».
Transcription : oui (anglais, auto)
- 6:04 Voix : recalée en croches (Elastic Audio) ; 6:52 plugin de largeur utilisé seulement pour automatiser le panoramique ; 8:50 VintageVerb preset par défaut, **mix 16 %** ; 9:38 Equilibrium : **HPF 123 Hz**, encoches **~2,6 kHz** et **6 kHz** au lieu d'un de-esser.
- 11:46 Effets imprimés (AudioSuite) en « throws » sur des fins de mots : en techno minimale, chaque effet ponctuel pèse plus en club.
- 14:19 Kick = 2 kicks (« stay kick » court + « Titan sub » modulaire, enregistrés via préamps Neve), **aucune EQ** sur les kicks. Massive Passive pour un léger roll-off aigu, puis Elevate (transitoire + drive) pour souder la superposition.
- 17:39 Chaîne master : Massive Passive (toujours un peu de HP/LP, ajout vers **15 kHz**, retrait vers **200 Hz**) → Townhouse Bus Comp **~2–3 dB** de réduction → Black Box HG-2 (saturation basse, clippe joliment, ressort les sides) → bx_digital **mono maker** sur chaque master, réglé bas [valeur à lire, ASR « a tea »].
- 20:31 Snaps enregistrés, canaux L/R inversés entre deux frappes pour varier ; 22:33 snare : Equilibrium coupe **~2 kHz** pour laisser la place au snap.
- 23:13 Craquement vinyle quantifié en doubles croches, fondu (ducking) à chaque temps fort du kick, coupe-bas.
- 25:20 Hats : un peu d'air (SSL bx), creux vers **1 kHz** ; 28:53 metals : filtre automatisé + bx_room pour les reculer.
- 29:45 Reverb automatisée sur le bus drums dans le break, pour le contraste au drop ; 33:58 le sub disparaît avant le drop (effet psychoacoustique).
- 37:43 Kick/sub : **fondus audio sur le sub, courbe inverse de la décroissance du kick**, à la place du sidechain (technique de producteurs DnB).
- 36:50 Replika : pitch **L +6 / R +4 demi-tons** en ping-pong ; 48:41 granulateur sur un drone, grains **178 ms**, **+1 octave**.
- 40:07 Cordes LA Scoring très filtrées (grave et aigu) pour les éloigner, puis Blackhole.
À vérifier à l'écran : 9:45 (courbe Equilibrium voix) ; 16:50 (réglages d'Elevate) ; 18:30 (réduction du Townhouse) ; 19:50 (fréquence du mono maker bx_digital) ; 38:50 (forme des fondus sur le sub).

### MX-02 Mixing Masterclass: 'Mixing Your Track for the Club' at IMS College Malta — pointblank music school (JC Concato), 48:21, 2017-08-23, DAW/outils : DAW non nommé ; Waves NLS, UAD SSL Bus Comp, Manley Massive Passive, Black Box HG-2, UAD tape, Magic AB, bx mono/width, UAD multipiste 2", Teletronix LA-2A (UAD), API (bus drums), Dimension D
URL: https://www.youtube.com/watch?v=LUIXtDO4d8s
Qui : JC Concato, directeur créatif de Point Blank. Mixe de la dance depuis le début des années 90 sur SSL, remixes pour « Frankie » [ASR] et Sasha. Il mixe le morceau d'un ancien élève signé sur le label de Point Blank (artiste [ASR « regular » / « Ray »]).
Transcription : oui (anglais, auto)
- 1:50 Pour le club, la **compatibilité mono** prime (salles multiples, riff panoramiqué d'un seul côté = riff perdu).
- 5:43 Tout passer en audio (CPU, et engagement pour finir le morceau) ; mix reçu avec tous les faders à **0 dB**, déjà presque prêt.
- 8:59 Il commence par le **bus master** (approche « pré-mastering ») : par exemple **+2 dB à 15 kHz** au master, et on en fait moins sur chaque piste.
- 10:27 Waves NLS (modèles Spike/SSL, Mike Hedges/EMI, Nev/Neve) en premier sur le master.
- 12:25 SSL Bus Comp UAD : **attaque la plus lente, release la plus rapide**, ~**2 dB** de réduction. Ne pas écraser le mix entier.
- 14:13 Massive Passive : petits boosts **~16–18 kHz** et **~60 Hz** (« fréquence chic »).
- 15:22 HG-2 (pentode/triode, air) : distorsion harmonique comme « compression naturelle », niveau perçu plus fort sans dureté ; 19:59 émulation bande sur le master.
- 23:44 Headroom à l'export : « 6 dB » par sécurité, **3 dB** suffisent si rien ne dépasse 0 (true peak) ; mesuré **3,2 dB**. 25:08 corrélation négative = problème de phase (vinyle) ; écoute mono et d'**un seul côté**.
- 28:00 Analyse grave **40/80/120/160 Hz** avec kick et basse coupés, pour voir ce qui encombre.
- 30:47 Kick : EQ avant compression (**+50 Hz**, creux **~200 Hz** sur une résonance), puis compresseur à attaque lente pour faire ressortir l'attaque (démo attaque rapide vs lente).
- 35:34 Clap : attaque rapide, **+1 kHz** (mordant chaud), HPF ; 37:03 bus drums : API léger.
- 39:37 Basse : mono maker réglé haut (**~7** sur le plugin, inhabituel) + largeur sur l'aigu = « triangle inversé » ; 41:53 bande multipiste **15 ips** poussée fort pour égaliser les notes ; 43:51 LA-2A (3 versions essayées) ~**3–4 dB** [ASR « 340 D »] ; 44:44 SSL (VCA) derrière ; 45:46 EQ pour faire revenir l'attaque de la basse dans le mix complet.
- 46:40 Dimension D modes **3+4** en parallèle (aux) sur le pad.
À vérifier à l'écran : 13:00 (réglages du bus comp) ; 14:45 (fréquences du Massive Passive) ; 24:50 (valeurs de headroom et true peak) ; 33:56 (EQ du kick) ; 40:45 (valeur du mono maker et de la largeur sur la basse).

### MX-03 Mixing EDM: A Full 88-Minute Mixing Masterclass — Aubrey Whitfield, 1:28:37, 2026-09-28, DAW/outils : Logic Pro ; Waves CLA-3A, Waves Trigger, iZotope RX 12, Soundtoys Devil-Loc Deluxe, FabFilter Pro-Q 4 et Saturn, UAD 1176 Rev A, oeksound soothe 3, Waves Magma StressBox, Valhalla FutureVerb et Delay, Echoboy
URL: https://www.youtube.com/watch?v=jYOmzSz7IKw
Qui : Aubrey Whitfield, productrice et ingénieure mix/mastering (20 ans d'expérience selon la description). Cours en direct de son diplôme, sur des stems électro dance-pop de Cambridge-MT (Mike Senior).
Transcription : oui (anglais, auto)
- 8:00 Drums livrés en boucles seulement : deux boucles réunies en une.
- 10:13 Compression parallèle : CLA-3A peak reduction au maximum, dosé au send.
- 12:03 Renfort par **Waves Trigger** déclenché par la boucle (kick EDM Splice), détection kick seule, autres pistes coupées.
- 20:32 Faders bas pour les drums dance : elle part en général à **−15 dB**, ici **−12 dB**.
- 21:12 Clic du kick : RX 12 De-click abîme la transitoire, donc refusé ; il faudrait le corriger à la main dans RX.
- 23:18 Saturation parallèle Devil-Loc Deluxe sur la top loop et les percussions.
- 26:11 EQ de la boucle en « sourire » : **pas de coupe-bas en EDM** ; petit boost **~70 Hz sur le Mid** ; creux **~500 Hz** et **~1,2 kHz** (place pour la voix) ; boost **~2,2 kHz** (claps) ; creux **150–250 Hz** (pas de snare).
- 31:39 Saturn preset « drum bus punch » (bande + lampe), en M/S, saturation sur le Mid seulement.
- 40:02 Kick/basse avec l'affichage de masquage du Pro-Q 4 : fondamentale de la basse **40–60 Hz**, du kick **60–80 Hz** ; creux **~50 Hz** sur le bus drums, creux **~70 Hz** sur la basse ; petit boost 60–80 Hz si le kick perd du punch.
- 47:30 Basse : 1176 Rev A **4:1 ou 8:1**, attaque et release rapides à moyennes, **~5 dB** de réduction en général, **~7 dB** pour un son EDM traité.
- 50:12 soothe 3, preset « deboom the bass » (**40–80 Hz**) en M/S ; 52:55 basse resserrée par une coupe raide de l'aigu sur les Sides.
- 55:29 Changer souvent le niveau d'écoute (isosonie) ; astuce : casque très bas pour juger la clarté.
- 57:53 Synthé : HPF **~85 Hz** raide ; long high shelf à partir de **~2 kHz** (pas plus bas à cause de la voix), sur les Sides pour la largeur ; creux **~150 Hz** ; boost **~400 Hz** sur le Mid (puissance) ; creux **~1,2 kHz** (voix).
- 1:01:43 Saturation avant compression ; saturateur Plugin Alliance [nom ASR « Loop Trotter », incertain] en mode digital ; 1:08:25 StressBox, sortie **−2,3 dB** pour égaliser le niveau.
- 1:09:28 FutureVerb sur bus (mix 100 %) ; 1:17:05 automatisation du mix d'un Valhalla Delay (« swell » en fin de phrase) + Echoboy en noire, style « Radio ».
- 1:26:12 Plan pour la voix : 1176 **8:1**, saturation, Maag EQ4 / V-EQ4 pour l'air.
À vérifier à l'écran : 27:00 (courbe EQ de la boucle, gains) ; 42:40 (creux kick/basse dans le Pro-Q 4) ; 48:30 (attaque et release du 1176) ; 51:00 (bandes de soothe 3) ; 58:30 (shelf Side sur le synthé).

### MX-04 Mixing 'Voices In My Head' with Dom Kane - Initial Playthrough Bus Groups and Bass EQ — Sonic Academy (Dom Kane), 20:06, 2019-03-22, DAW/outils : Harrison Mixbus 32C (stems exportés de Bitwig), Waves Q8
URL: https://www.youtube.com/watch?v=kMyp8sfNYmA
Qui : Dom Kane, artiste mau5trap. Il mixe son propre morceau « Voices In My Head » (compilation mau5trap *We Are Friends Vol. 08*). Premier épisode d'un cours Sonic Academy.
Transcription : oui (anglais, auto)
- 0:17 Il mixe dans un DAW qu'il connaît mal (Mixbus) pour séparer la casquette de producteur de celle de mixeur.
- 5:10 Tempo **124 BPM**, tout décalé d'**1 temps** (pour éviter un clic à l'export).
- 6:03 Son gain de canal par défaut dans Bitwig : **−15 ou −10 dB** (« je crois »).
- 6:41 Première écoute écran éteint, notes sur papier.
- 9:21 Diagnostic : la basse gêne les kicks, le grave de l'acid line gêne ; « la basse doit dominer le morceau, pas le mix ».
- 11:04 Bus du template : **1 drums, 2 bass, 3 FX, 4 synths, 5 vocals** ; basse seule sur le bus 2 ; marqueurs au drop.
- 14:56 Q8 sur la basse : balayage avec un boost, résonance trouvée à **~125 Hz**, coupée de **3 à 5 dB** (au-delà, la basse perd sa puissance) ; zone de boue **120–300 Hz**.
- 17:20 Bande 5 balayée en boost de **6–7 dB** pour chercher les harmoniques (« overkill »), bande 4 ajustée plus raide ; la basse perd de l'énergie, il la remontera au niveau plus tard.
À vérifier à l'écran : 11:30 (routage des bus) ; 16:20 (Q et gain de la coupe à 125 Hz) ; 18:00 (réglages des bandes 4 et 5).

### MX-05 14. How To Make Dark Room Techno - Mixing — Sonic Academy (Kirk Degiorgio), 9:05, 2017-12-23, DAW/outils : Ableton Live (Utility, outil stéréo), émulation bande, Neve 33609 (plugin), Vertigo VSC-2 (plugin)
URL: https://www.youtube.com/watch?v=oSf64milubk
Qui : Kirk Degiorgio, producteur techno vétéran, présenté dans la description comme auteur du cours *How To Make Dark Techno*. Il mixe son morceau de cours.
Transcription : oui (anglais, auto)
- 0:15 Faders tous à **0**, niveaux réglés avec un **Utility** sur chaque piste, pour attaquer les plugins (API, etc.) à leur niveau optimal.
- 1:09 Outil stéréo pour contrôler la largeur de la basse ; leçon des graveurs vinyle : ne pas panoramiquer le sub lourd (saut de diamant).
- 1:58 « Mur de son » par petites touches cumulées : émulation bande, puis petites EQ et compressions.
- 2:36 Bus drums sur **Neve 33609** attaqué doucement ; 5:14 toujours en **release auto 1**, sans gain de compensation, **ratio le plus faible**, l'aiguille bouge à peine.
- 3:15 Le bus comp sert aussi à juger les niveaux : hats et shaker trop forts, clap à monter.
- 5:45 Bus synthés sur **Vertigo VSC-2** : filtre sidechain désactivé (il veut contrôler le grave des synthés), ratio doux, attaque plus rapide, release auto, très peu de makeup ; 7:13 le drone déclenchait le compresseur, donc baissé.
À vérifier à l'écran : 0:50 (gains des Utility) ; 3:00 (réglages du 33609) ; 6:20 (seuil, ratio et attaque du VSC-2).

### MX-06 Razer Music | Noisia - Creative Mixing with Nik — Razer (Nik Roos / Noisia), 10:45, 2018-04-25, DAW/outils : DAW non nommé, Serum (bounces), sidechain trigger
URL: https://www.youtube.com/watch?v=Gunhpva0Jho
Qui : Nik Roos, membre de Noisia, dans son studio. Il mixe des boucles préparées pour la vidéo (kick, snare, basse Serum, puis une boucle DnB), **pas un morceau sorti**.
Transcription : oui (anglais, auto)
- 0:19 Départ brut : tout en mono, basse sidechainée sur les drums.
- 1:39 « Signature fréquentielle » d'un son = fondamentale + zone de résonance que l'on met en avant ; dans l'aigu, la fondamentale compte moins.
- 2:31 Au lieu de tout sidechainer : kick plus grave, moins de sub dans la basse, moins d'aigu sur la snare. EQ de basse avec un gros creux et le haut-grave accentué pour séparer.
- 4:12 Stéréo : reverb sur la basse utilisée comme couche musicale ; 5:12 couche « fizz » stéréo pour l'aigu de la basse (sides), bas-médium de reverb dans les sides, médium de la snare au centre.
- 6:36 Une basse pleine bande (jusqu'à **~18 kHz**) permet de creuser de grands trous.
- 8:04 Boucle DnB : drums mono et basse large, ou l'inverse (drums stéréo dans l'aigu, basse mono). Pour le dancefloor, **transitoires mono**.
- 9:38 Un hi-hat en croches qui se heurte aux triolets de la basse passe s'il est panoramiqué large.
À vérifier à l'écran : 3:35 (courbe d'EQ de la basse) ; 5:20 (couche stéréo de l'aigu, réglages) ; 8:30 (mesure Mid/Side de la boucle DnB).

#### Écartés
- cahztwJBn7c Luca Pretolesi, MixCon 2020 (41:48) : pertinent (Major Lazer, Diplo), mais **aucune piste de sous-titres**, donc non vérifiable.
- FLDEWgHQr2A « Mefjus - Particles Studio Insights: Transit with IMANU » (26:28) : vrai morceau, mais surtout production et routage Cubase (couches de snare, chaînes de bus, sends), très peu de mixage chiffré. Réserve si l'on veut un vrai morceau DnB à la place de MX-06.
- JpsdLqS6Rzw « Noisia - Track Breakdown: Running Blind » : inspirations et arrangement, pas de mixage.
- ZQuIa741EwQ Hospital Records « How To Mix Drum & Bass: Advanced » : mix DJ (double drop), hors sujet.
- OBZzW510X80 « BassPro Episode 2 » (chaîne Skepsis, 2014) : surtout production de drop, identité de l'auteur non confirmée.
- aBnnymAH678 Point Blank « DnB Logic Mix Down Pt.1 » (2012) : formateur non nommé, peu de valeurs.
- KdvKdGxhvLM (ingénieur de John Summit) et 0T9EhySSWzU (Virtual Riot, mix/master d'un drop) : déjà vus (deja_vus.txt).
- Non ouverts : ORN2fWyMLpY (Laidback Luke « It's ALL About The Mixdown ») ; la vérification a été coupée par la déconnexion de Chrome.

#### Manque
- Pas trouvé (ou pas pu vérifier) de mixdown commenté par Chris Lake, Eats Everything, Fred again.. ou un ingénieur de Skrillex.
- Rien en français au niveau « pro reconnu ».
- MX-06 porte sur des boucles de démo, pas sur un morceau complet ; MX-05 et MX-04 sont des extraits de cours (un épisode chacun).

# Bas du spectre et références

## Bas du spectre du mix au master

Ordre : du mix (relation kick/basse, phase) vers le master (mono, vinyle, limiteur).

### BA-01 Voilà comment je fais TAPER un KICK BASSE en CLUB (sans compresseur) — Strob Studio Mixing & Mastering, 15:54, 2026-10-02, DAW/outils : DAW non nommé, analyseur de spectre, EQ (shelf + filtre), automation de gain, bounce audio
URL: https://www.youtube.com/watch?v=krVs-m4Qf_g
Qui : le formateur de Strob Studio (« près de 20 ans dans le game » selon la description ; il se présente en fin de vidéo comme « Gor » [ASR ?]). Il travaille sur la session d'un élève de son programme Ascension Pro.
Transcription : oui (français, auto)
- 0:41 À l'analyseur, le kick tape vers −10 et la basse vers −20, soit **10 dB d'écart** dans le bas. Il ne faut pas forcément les aligner au dB près, mais c'est un indice de déséquilibre.
- 1:01–1:42 Une automation de gain raccourcit le kick pour éviter qu'il chevauche la basse. Résultat : on ne garde presque rien du sub du kick. Points à vérifier : la longueur du kick et la transition entre la fin du kick et la remontée du sidechain (ici déjà imprimé dans l'audio).
- 2:03–2:44 Il rallonge le kick : il paraît plus « fat » et plus assis, sans que le niveau crête de la somme change.
- 3:45 Avertissement : la décision se prend à l'oreille. Les outils visuels servent à illustrer ou à compenser une mauvaise écoute du bas.
- 4:27 Sur la basse, la fondamentale et les deux premières harmoniques ont à peu près le même niveau. Pour un son actuel, il vise un niveau décroissant : la fondamentale au-dessus de la 1re harmonique, elle-même au-dessus de la suivante.
- 5:08 Test : remonter toute la basse de **+5 dB** (≈ −15). Ça surcharge la zone au-dessus des basses.
- 5:49–6:54 Il utilise l'EQ comme une balance par fréquence : shelf, puis boost de la fondamentale avec un filtre. Au total **≈ 10 dB de boost**, avec un filtre « bien violent », assumé.
- 7:16 Il remonte un peu la 1re harmonique.
- 8:23 Il supprime le bout de queue de basse qui chevauche l'attaque du kick.
- 10:06–10:47 Piège : un boost combiné à un filtre en phase non linéaire crée du **post-ringing** (résonance visible après bounce), qui déstabilise la transition avec le kick.
- 11:07–11:49 Deux corrections possibles : imprimer en audio puis éditer, ou automation de gain (un sidechain manuel) avec une petite pente en fin de note.
- 12:14 Récap : le kick frappe grosso modo entre **30 et 60 Hz**, et la basse doit vivre dans la même zone. Le kick peut taper plus haut ou plus bas que la basse. À régler : longueur, sidechain, phase.
- 12:55 Si la basse change de note, la relation de phase avec le kick change à chaque note. Il n'existe pas de relation parfaite.
- 13:15–13:56 Astuce d'écoute : filtrer pour n'écouter que la zone grave (« zoomer avec les oreilles »). Avant/après : le kick reste devant, la basse est plus ronde et roule entre les coups.

À vérifier à l'écran : 0:41 (valeurs lues sur l'analyseur kick/basse), 6:34–6:54 (forme et réglages du boost et du filtre), 10:47 (forme d'onde du post-ringing), 11:49 (pente de l'automation de gain).

### BA-02 Sub Bass Science 🤓 Get That Low End Right 🔊 @theravenstudiosmusic — D Ramirez (pour Raven Studios), 25:37, 2025-07-21, DAW/outils : Ableton Live (Operator, Vinyl Distortion, Auto Filter, Utility), FabFilter Pro-Q 4, Kickstart, Voxengo SPAN, Master Plan (simulation téléphone), Roar [ASR ?]
URL: https://www.youtube.com/watch?v=ccwxv5OzwRU
Qui : D Ramirez, producteur house basé à Londres, pour sa plateforme Raven Studios (vidéo d'aperçu ; la version complète est sur le site).
Transcription : oui (anglais, auto)
- 3:06–4:32 Zones : **20–60 Hz** = sub qu'on ressent ; **60–300 Hz** = basse audible. Sous 60 Hz, rien ne passe sur téléphone, enceinte Bluetooth ou écouteurs.
- 5:12–7:42 Sinus d'Operator et note jouée : C3 ≈ 300 Hz, C2 ≈ 120 Hz, C1 ≈ 60 Hz, C0 trop bas. Pour lui, la note optimale est **F** (la « note des producteurs DnB »), et la plage utile va de F à B.
- 8:04–9:27 Traduction n°1 : 2e oscillateur sinus à **+1 octave** (F → 60 + 120 Hz), audible sur petits systèmes.
- 9:27–10:32 Traduction n°2 : mode MS2 d'Operator, Filter Drive (distorsion), puis filtre passe-bas pour garder seulement les harmoniques utiles.
- 10:53–12:22 Autres formes d'onde (triangle, carré, dent de scie) pour ajouter des harmoniques, puis filtrage.
- 15:57 Vinyl Distortion centré vers **158 Hz** : basse distordue stéréo, ensuite filtrée avec Auto Filter.
- 17:01–17:47 Bande dynamique de Pro-Q en sidechain sur le kick : elle n'atténue que la fréquence qui entre en conflit, et seulement quand le kick frappe. Kickstart en plus pour le ducking de volume.
- 18:28–19:30 Niveau sub vs kick avec SPAN sur la sortie : kick autour de **50 Hz à environ −33** (échelle SPAN). La basse ne doit pas dépasser le kick : elle reste **légèrement en dessous**.
- 19:56–20:37 Pas de coupe-bas sur la basse : décalage de phase à la fréquence de coupure, donc problèmes de phase kick/basse. Il fait le coupe-bas sur le master.
- 21:02–22:48 Contrôle avec la simulation téléphone de Master Plan : la basse disparaît. Correctif : ouvrir le filtre (plus d'harmoniques), baisser le sub et booster une cloche plus haut dans Pro-Q 4.
- 23:14 Utility en Bass Mono après Vinyl Distortion. 23:39 Variante : distordre les médiums plutôt que les graves, ce qui donne une basse plus mono.
- 25:02 Conseil : s'appuyer sur la mesure (SPAN) et ne pas faire confiance à ses enceintes si la pièce n'est pas bonne.

À vérifier à l'écran : 7:42 (courbe Pro-Q sur F), 15:57 (réglages Vinyl Distortion), 17:23 (bande dynamique en sidechain dans Pro-Q), 18:49 (niveaux SPAN kick/basse), 22:27 (EQ de compensation).

### BA-03 Everything you NEED to know about Phase Allignment for Kick & Bass! — Projektor, 16:24, 2023-06-02, DAW/outils : Ableton Live, oscilloscope en sidechain (« Cisco/size scope » [ASR ?]), synthé avec éditeur de phase par harmonique, « fpa979 » = Voxengo PHA-979 [ASR ?], LFO Tool, EQ
URL: https://www.youtube.com/watch?v=xYzp27xTNao
Qui : Projektor, producteur bass music (label Eclipse Sound Syndicate d'après la description).
Transcription : oui (anglais, auto)
- 0:27–1:07 Oscilloscope alimenté en sidechain par le kick et la basse, vue « somme » : la forme d'onde saute dans tous les sens.
- 1:28–1:48 Chaîne de basse : LFO sur le cutoff, traitement multibande, EQ, puis LFO Tool pour couper le **post-ringing** de la basse avant le transitoire du kick suivant.
- 2:08 Aléatoire de phase de l'oscillateur à **0** : à proscrire en basse, sinon le point de départ change à chaque note.
- 3:30–4:51 Rappel : une dent de scie est une somme de sinus harmoniques (100/200/300/400 Hz…), chacun avec sa propre phase.
- 5:12 Le kick est essentiellement un sinus. But de l'alignement classique : la fondamentale de la basse doit s'additionner au sinus du kick.
- 6:34 PHA-979 : appliquer les réglages identiquement en L et en R.
- 6:57–7:18 L'alignement doit se faire **après** le traitement, parce que les filtres décalent la phase autour du cutoff. La saturation et la compression ne sont pas en cause.
- 7:38–8:20 Mode layers : aligner les plus gros pics. Exemple : les deux à **90 (°)**. Ne pas recopier ce réglage, il dépend de la basse.
- 8:20 L'alignement ne peut pas être exact, puisque le sinus du kick glisse en pitch.
- 9:02–9:48 L'addition augmente fortement le niveau : il baisse la vélocité de la note de basse.
- 9:48–10:49 Sa méthode : séparer les notes de basse qui chevauchent le kick et retirer leur 1re harmonique.
- 11:09–11:51 Placer le transitoire de la basse sur un passage à zéro du kick.
- 12:36–13:38 Astuce : EQ coupe-bas sur le kick, sans couper, juste pour décaler la phase (dupliquer l'EQ double l'effet). Puis inverser la polarité, par convention (montée puis descente vers la basse).
- 13:58–14:40 Effet secondaire : le kick s'allonge. Le resampler ou le couper avec LFO Tool.
- 15:08 Régler le niveau de la note sur la tranche du mixeur plutôt qu'à la vélocité. 15:28 Objectif annoncé : une meilleure traduction sur d'autres systèmes.

À vérifier à l'écran : 2:08 (paramètre de phase / random), 7:58–8:20 (valeurs PHA-979 et vue layers), 12:57–13:17 (réglage du coupe-bas utilisé comme déphaseur), 15:08 (oscilloscope final).

### BA-04 Is Mono Bass DESTROYING Your Low End? — Warp Academy, 19:26, 2023-05-26, DAW/outils : Ableton Live (Utility Bass Mono, EQ Eight M/S), Voxengo SPAN (M/S), FabFilter Pro-Q 3 (M/S, phase linéaire), Mastering The Mix LEVELS, Plugin Doctor, TDR Nova
URL: https://www.youtube.com/watch?v=8hNtxXu0rOY
Qui : présentateur de Warp Academy (nom non dit dans la transcription). Morceau tech house de DJ IBG (Ian Gallagher, formateur Warp).
Transcription : oui (anglais, auto)
- 0:00–0:46 Constat : beaucoup de titres du top 100 Spotify gardent de l'information dans les côtés du bas du spectre.
- 3:31–4:33 SPAN en M/S : des côtés **sous 100 Hz** sur un stab de basse. Écoute des côtés seuls avec Pro-Q 3 en M/S. En somme mono, la corrélation est excellente et il ne perd rien. Si on filtre les côtés, il perd de l'énergie et de l'ampleur.
- 5:17–5:41 Headroom : crête à **−5,5 dB**. En supprimant les côtés, il ne gagne que **0,1 dB**. 6:23 Même résultat en phase linéaire.
- 6:44–7:05 Utility Bass Mono à **200 Hz** : toujours **+0,1 dB**.
- 7:46–8:07 Sur un autre mix commercial, Bass Mono sous 200 Hz fait passer le titre **presque 2 dB au-dessus** : il clippe.
- 9:12–10:16 Contre-exemple : basse large construite hors phase, qui s'annule en mono. Pour lui, c'est un problème de sound design, pas de mix.
- 10:38–11:43 Une 808 élargie avec un sound design adapté reste solide en mono. On peut garder de la largeur assez bas tout en gardant une corrélation suffisante pour des subs câblés en mono.
- 12:45–13:05 Ce que fait Bass Mono : un passe-haut sur les côtés (démonstration avec EQ Eight en M/S).
- 13:26–14:07 Plugin Doctor : un filtre passe-haut provoque une **forte rotation de phase** à la fréquence de coupure, d'autant plus forte que la pente est raide. Résultat : côtés et mid désalignés, perte de punch.
- 14:07 En phase linéaire, la rotation de phase disparaît presque.
- 14:48–15:50 Alternative en phase minimale : TDR Nova en mode difference (= côtés), **low shelf** négatif, ou **cloche soustractive** en jouant sur le Q (astuce attribuée à un ingénieur de Mixbus TV [ASR ?]).
- 16:31 Bass music : des côtés jusqu'à **35 Hz** dans un titre.
- 16:54 Noisia : les côtés sont coupés agressivement, avec une décroissance dès ≈ **120 Hz** et plus rien vers **55 Hz**. Conclusion : ça dépend du genre, il faut analyser ses références.

À vérifier à l'écran : 3:31 (SPAN M/S, niveau des côtés), 5:17 et 8:07 (lectures de crête dans LEVELS), 13:47 (courbes de phase dans Plugin Doctor), 15:10–15:30 (réglage shelf/cloche dans Nova), 16:54 (SPAN sur le titre de Noisia).

### BA-05 SHOULD I MONO THE BASS? - Streaky.com — Streaky, 6:41, 2019-09-06, DAW/outils : contexte mastering (EQ, largeur stéréo de la SSL Fusion)
URL: https://www.youtube.com/watch?v=G4g4Yp2FrsA
Qui : Streaky, ingénieur mastering britannique (30 ans de métier selon la description ; Metropolis, Battery ; crédits : Shanks & Bigfoot, Groove Armada, Skepta, Lily Allen…).
Transcription : oui (anglais, auto)
- 0:21–0:42 La règle « mono la basse » vient du **vinyle**. Il a appris la gravure avec d'anciens graveurs.
- 1:05 Les principes du vinyle (pas d'aigus agressifs, pas de basse large hors phase) donnent aussi un bon master pour le streaming.
- 1:26–2:07 Mécanique : une basse large et hors phase fait bouger le sillon latéralement/verticalement, et le diamant peut sauter. Une basse mono garde le diamant en place.
- 2:28–2:50 Aujourd'hui, beaucoup de mixes dance arrivent avec la basse déjà mono. En mastering, ajouter de l'EQ grave **sans le monoïser** donne un bas plus « costaud », moins maigre.
- 3:11–4:33 Danger : le point de crossover du mono. En retirant la stéréo trop haut, on amincit les bas-médiums (**≈ 200–400 Hz** : bas de la caisse claire, voix, guitares).
- 4:53 Si on monoïse : **sous ≈ 50 Hz**, puisque la pente remonte vers 80–100 Hz. Souvent, il vaut mieux ne pas monoïser du tout.
- 5:35 Avec la SSL Fusion, ajouter un peu de largeur plutôt qu'en retirer rend parfois le bas plus solide.
- 5:56 La dance garde généralement le grave au centre. Il ne monoïse jamais la basse d'un titre indie/guitare, sauf gros problème de phase.

À vérifier à l'écran : vidéo face caméra, peu à lire. 1:47 (geste illustrant le sillon), 3:32 (schéma gestuel du crossover), 4:53 (valeur 50 Hz dite).

### BA-06 Unf*ck Your Master (Limiters Are KILLING Your Low End) — TheCosmicAcademy, 6:23, 2024-05-29, DAW/outils : iZotope Ozone Maximizer (modes IRC, Character, écoute delta), FabFilter Pro-L, EQ passe-bas, loudness meter
URL: https://www.youtube.com/watch?v=gY2YbQl4icE
Qui : Zack, de TheCosmicAcademy (coaching en production électronique). La description crédite l'inspiration à Panorama Mastering, et il cite un ingénieur « Nick DeLorenzo » [ASR ?] à 2:58.
Transcription : oui (anglais, auto)
- 0:21–0:43 Le limiteur, dernier plugin de la chaîne, monte le titre vers **0 dB**. Dans l'électro, c'est l'énergie du grave qui le fait travailler, et le kick et la basse s'écrasent.
- 0:43–1:05 Bouton **delta** (casque) : on n'entend que ce que le limiteur retire, ici surtout le kick et la basse, même sur un mix équilibré.
- 1:29–2:12 Étape 1 : passer en revue tous les modes (IRC d'Ozone, styles de Pro-L) en écoutant le delta. Ne pas choisir « Modern » simplement à cause du nom.
- 2:37 Étape 2 : se concentrer sur **≈ 100 Hz et en dessous**.
- 3:41 Mise en œuvre : **passe-bas** sur le signal delta (n'importe quel EQ) plus un loudness meter. Utiliser un bon casque ou des enceintes qui descendent bas, faute de sub.
- 4:49 Dans son exemple, **Balanced, Crisp et Clipping** préservent le mieux le grave : leur delta filtré est plus faible à l'oreille et en mesure. **Modern** écrase davantage le grave. (interp. : la transcription dit « higher LUFS values », sans doute une lecture négative moins élevée, à vérifier.)
- 5:11 Affiner ensuite avec le curseur **Character**.
- 5:32 Méthode applicable à n'importe quel limiteur avec plusieurs styles.
- 5:59 Si le résultat reste mauvais, c'est un problème de mix à régler en amont.

À vérifier à l'écran : 1:05 (bouton delta d'Ozone), 3:41 (fréquence du passe-bas sur le delta), 4:04–4:49 (lectures du loudness meter par mode IRC), 5:11 (valeur de Character).

#### Écartés
- I__tWZTk5-Q « Mixing Techno Kick and Bass – Your Guide to the Perfect Low-End » (SINEE Global, Björn Torwellen, 16:03, 21 nov. 2024). Très pertinent (chaîne kick/basse techno : Roar, Weiss EQ, Bass Low Extender, Soothe 2, clipper, limiteur), mais aucune piste de sous-titres, donc aucune valeur vérifiable. À regarder manuellement en priorité.
- -pwS4HGyQDM « Yan Cook: Techno low end with kick and rumble in 5 mins » (Home of Sound, 5:12). Artiste reconnu, mais surtout de la musique. Seules infos : groupe kick + sub en mono, groupe vers −6 dB, compresseur Wolf.
- lXiiBbJP1Bk « Getting Your Low End Right » (Distinct Mastering, Freddy, 11:51). Accordage kick/basse (basse G0 = 48 Hz) ; plus production que mix/master.
- O2mzqlaBZbk « Mixing Low End: The Ultimate Guide » (iZotope, 34:01). Généraliste, exemples country et jazz, pas électro.
- 8p4GVCkkjgw Kevin Grainger (Wired Masters), chaîne de mastering, Audiotent. Excellent, mais c'est une chaîne master complète (thème d'un autre agent), pas le bas du spectre.
- LUIXtDO4d8s (Point Blank) : il couvre aussi la basse mono, avec BX_control. Je l'ai classé dans le thème RE (RE-06).
- Non ouverts : Sage Audio 27ewHn5SAiI, Underdog « Techno Rumble » oUbACkekJZ8, Baphometrix K-eneMG_DVE (1:43:34, phase kick/sub), Streaky XZLOvuTZGhU (saturation de basse).

#### Manque
- Aucune vidéo d'ingénieur mastering sur un **compresseur multibande appliqué au seul grave** d'un master électro avec des valeurs dites.
- Pas de démonstration de **gravure vinyle** (filtre elliptique, mono sous X Hz au tour de gravure) : seul Streaky en parle, à l'oral.
- Pas de **cible chiffrée sub/kick en LUFS ou en dB RMS** au master. Les chiffres disponibles (−33 sur SPAN, −10/−20 sur l'analyseur) dépendent des réglages d'affichage.

## Références, traduction et écoute

### RE-01 COMMENT REFERENCER SON MIX — Strob Studio Mixing & Mastering, 13:07, 2022-06-02, DAW/outils : Process Audio Decibel (plugin + standalone + appli iPad, sponsor), TC Electronic Clarity, analyseur M/S, routage vers sorties d'écoute dédiées
URL: https://www.youtube.com/watch?v=iUfP9Kr6Fv8
Qui : le formateur de Strob Studio (même chaîne que BA-01).
Transcription : oui (français, auto, ASR de mauvaise qualité)
- 0:21–1:04 Pourquoi référencer : remettre ses oreilles à zéro et prendre du recul (« zoom out »).
- 1:04–1:44 C'est surtout utile pour le **grave**, la zone que la pièce rend le plus faussement. Même dans une bonne pièce, il continue de référencer.
- 2:26–2:46 Quoi comparer : spectre, dynamique (le mix tape-t-il autant ?), largeur stéréo, profondeur.
- 3:06–3:48 Règle d'or : **égaliser le loudness**. Le niveau d'écoute change la courbe de réponse de l'oreille.
- 3:48 Des études montrent qu'**0,1 dB** d'écart peut fausser la préférence : on préfère d'emblée le plus fort.
- 4:08–4:29 Ne pas pousser son mix dans un limiteur pour rattraper la référence : **baisser le gain de la référence**, avec un line-up meter.
- 6:31–7:15 Ne pas comparer en loudness intégré. Boucler le passage le plus fort (le drop) et comparer en **short-term** (ou momentary).
- 7:58 Son drop est à ≈ **−6 LUFS short-term**.
- 8:18–8:59 Routage : la piste de référence va **directement vers les sorties d'écoute** (ici 7-8), sans passer par le traitement du master. On bascule ensuite par solo.
- 8:59–9:20 La référence mesure **−5,1**. Il la baisse de **0,9 dB**, et les deux sont à −6.
- 9:41–10:22 Ensuite, comparer à l'oreille. Pour le grave, analyseur en appoint : référence vers **−5 dB**, son mix vers **−3/−4** (lecture sur l'analyseur). Il est dans la zone.
- 10:22–10:43 Ne pas recopier les chiffres : la perception du grave dépend aussi des bas-médiums.
- 11:23–12:44 Pour référencer sur Spotify, Decibel en standalone avec son driver de monitoring : on bascule l'entrée entre le DAW et Spotify.

À vérifier à l'écran : 7:58 (lecture short-term du mix), 8:38 (routage vers les sorties 7-8), 9:20 (gain −0,9 et nouvelle lecture), 10:02 (niveaux sur l'analyseur de spectre).

### RE-02 How To Use Metric AB - Setup and Basic Operation — Sonic Academy, 12:44, 2018-09-21, DAW/outils : Cubase (Control Room), ADPTR Metric AB (Plugin Alliance)
URL: https://www.youtube.com/watch?v=E1wloVMEMOo
Qui : Nate Raubenheimer alias Protoculture (artiste psytrance) pour Sonic Academy.
Transcription : oui (anglais, auto)
- 0:44 La référence sert à retrouver une perspective après de longues heures de mix (fatigue).
- 1:04 Version « gratuite » : glisser les références dans le projet, mais sur un **bus à part qui ne passe pas par le master bus**.
- 2:05–2:46 Dans Cubase, Metric AB va dans les inserts de la **Control Room**. Ailleurs, en **dernier insert du master, post-fader**.
- 4:14 On peut glisser plusieurs fichiers, ou un dossier entier, d'un coup.
- 5:34–7:40 Modes de lecture :
  - Latch : suit le transport.
  - Cue : redémarre au point de repère à chaque bascule A/B.
  - Sync : calé sur la tête de lecture. Pratique en dance, où les arrangements se ressemblent.
  - Manual : lecture lancée à la main, avec boucles.
- 8:01–8:47 Problème : la référence masterisée est bien plus forte, et ce qui est plus fort paraît meilleur.
- 9:08 La fonction **Match** propose **−7,8 (dB)**.
- 9:28 Comparer des sections équivalentes (ici, la section kick + basse).
- 10:08 Refaire le Match selon la section.
- 10:54 Chaque référence a son propre réglage. Il note que les fichiers masterisés tombent à des niveaux très proches.

À vérifier à l'écran : 2:46 (placement dans la Control Room), 6:17 (pose des repères), 9:08 (valeur de Match −7,8), 10:54 (Match de la 2e référence).

### RE-03 Mixing for club systems (ft. Jesco Lohan from Acoustics Insider) — Underdog Electronic Music School, 1:27:44, 2021-09-27, DAW/outils : Ableton Live (Operator, Spectrum), Voxengo SPAN (preset de Jesco en description), interface RME (dim)
URL: https://www.youtube.com/watch?v=CcvxRSFrr3E
Qui : Oscar (Underdog, Bruxelles, ex-DJ techno) interviewe Jesco Lohan (Acoustics Insider), mixeur house/tech house/pop électro. Crédit cité : Ofenbach « Be Mine » (2017, disque de platine).
Transcription : oui (anglais, auto ; « jessica » = Jesco)
- 5:57–9:36 Un titre prêt pour Spotify est en gros prêt pour le club. Mais en DJ set, les titres s'enchaînent et se comparent comme lors d'un référencement, et le DJ n'a que 3 bandes d'EQ et le volume.
- 9:36 Sur un système poussé à sa limite, un excès d'aigus distord tout de suite.
- 13:18–14:49 Anecdote d'Oscar : ses enceintes ne descendaient pas **sous 150 Hz**, et son morceau « fait fondre » la salle. Test conseillé : sinus d'Operator en mode Fixed, balayé vers le bas pour trouver la limite de ses enceintes.
- 16:29–21:18 « La musique vit dans les médiums » : le grave et l'aigu soutiennent seulement. Exemple : Ben Klock « Subzero » reste lui-même sur téléphone.
- 24:00–25:41 Contrôle du grave : passe-bas vers **150 Hz** (ou 100) sur la sortie master. Les références, égalisées en LUFS/RMS sur une section stable, contournent le mix bus et vont directement à la sortie.
- 26:14–27:54 Identifier le couple kick/basse : kick sub (souvent en techno) ou kick haut avec gros sub (tech house). Le kick est souvent l'élément le plus fort, pas toujours.
- 27:54–29:37 Éviter que kick et basse jouent en même temps. Les kicks de sample packs ont rarement le bon decay : viser plus court.
- 29:37–30:07 Les clubs non traités font gonfler le grave : rester compact et sec.
- 30:37 Le « cloakroom check » d'Oscar : écouter comme depuis le vestiaire.
- 35:00–37:45 Courbes isosoniques. Niveau de travail « upwards of 70 », autour de 70–80 dB SPL [ASR ? : « 1780 »], bruit rose, pondération C, slow. Trois niveaux **par paliers** (bas / moyen / fort), sans tourner le bouton en continu. Le cerveau s'adapte au niveau habituel.
- 38:18 Référence d'un titre « qui tue le dancefloor » au même niveau : permet de juger le grave, les médiums et l'agressivité des aigus.
- 40:31–41:32 Minimum : un bon casque. Puis des 2 voies, qui descendent vers **40–60 Hz**. Le 20–30 Hz reste hors de portée.
- 42:06 Des absorbeurs poreux contrôlent jusqu'à ≈ **40 Hz**.
- 43:11 Dans un studio pro récent, **80–90 % du budget acoustique** passe sous 50 Hz.
- 45:22–46:24 Garder le niveau moyen du mix bus constant, sinon le niveau d'écoute dérive.
- 46:54–47:24 Le spectre ne donne qu'un ordre de grandeur. Les derniers **±1–2 dB** sur le sub se décident à l'oreille.
- 49:39 Une fondamentale de kick à **60 Hz** sonne plus légère qu'à **45 Hz**.
- 50:42 Les gros subs de club descendent à **20 Hz** ; les plus petits chutent vers **40 Hz** (encore un peu à 30).
- 51:45 Couper sous **20 Hz** sur les pistes individuelles, pas sur le mix bus.
- 53:49 Coupe-bas : commencer à **12 dB/oct** (6 dB/oct = simple changement tonal), parfois 48.
- 54:20 Ne pas faire reposer l'identité du titre sur le **20–30 Hz**.
- 55:27–57:34 Réglages SPAN : bloc ≈ 8k, vitesse de réaction, courbe max, courbe Side. Il mixe à **−23 LUFS** de moyenne (ou −18 avec de l'analogique).
- 58:41–59:46 Paliers de volume pratiques : marques au feutre sur le potard, crans numériques chez UA, ou bouton dim (RME : deux réglages, dim et standard).
- 1:01:52–1:06:09 En sonorisation, la stéréo n'existe que dans un couloir d'≈ **1 m** au centre. D'où la compatibilité mono : kick, basse, percussions, hats, lead et voix au centre.
- 1:08:46–1:15:08 Loudness : les DJs poussent la table et le système à la limite. Un titre trop dynamique, calé à la même moyenne, dépasse le headroom. Il faut donc rester dans la fourchette des autres titres. Il cite les vidéos de Dan Worrall chez FabFilter.
- 1:16:11 Un drop trop compressé perd son énergie face au break.
- 1:19:32 Un limiteur sur le master bus pendant le mix produit un mix qui ne marche qu'écrasé.

À vérifier à l'écran : 14:19 (sweep d'Operator), 24:00–25:41 (routage des références et passe-bas master), 55:27–57:34 (réglages SPAN et échelle à −23 LUFS), 36:35 (valeur SPL exacte, ASR douteux).

### RE-04 Monitoring Level (SPL) as a Mastering Tool — Incidence Studio, 15:16, 2026-01-28, DAW/outils : sonomètre / niveau SPL, multibande M/S, expandeur multibande sidechainé sur le kick, transient designer, outil Schwabe Digital (« Hiful » [ASR ?])
URL: https://www.youtube.com/watch?v=T5h8qZPeNfM
Qui : l'ingénieur mastering d'Incidence Studio (nom non dit). Il a fait le son au club **Fuse** (8:06).
Transcription : oui (anglais, auto)
- 0:22–1:47 La recommandation courante est **85 dB SPL pondéré A** (ou 83) : compromis entre courbe isosonique plus plate et fatigue. Mais c'est déjà fort pour une journée entière.
- 2:09–3:14 L'essentiel : travailler longtemps **toujours au même niveau**, y compris quand on écoute des références. Le cerveau se calibre.
- 3:35 Une fois le master avancé, l'écouter à plusieurs niveaux.
- 3:55–4:36 Très bas, **50–55 dB SPL** : si le kick et la basse disparaissent, il manque de la traduction dans les médiums. Ajouter de l'harmonique d'ordre 2 (basse à **50 Hz → 100 Hz**, **60 → 120 Hz**).
- 4:58–5:20 À bas niveau, on entend mieux le pompage et les artefacts de compression : c'est là qu'il règle son compresseur de master.
- 5:40 Éventuellement multibande (M/S) dans les médiums.
- 6:01 55 dB, c'est ≈ **25 dB au-dessus de son bruit de fond** : ce chiffre dépend de la pièce.
- 6:44 Il travaille vers **75 dB**, et vérifie à **85 dB** (dureté, agressivité).
- 7:24–7:44 Matt Davis (« Hassenda Mastering » [ASR ?]) : le problème n'est pas que spectral, il vient aussi des transitoires.
- 7:44–8:06 Pour le club (≈ **100 dB LAeq 60 s**), monter brièvement près de 100 dB.
- 8:06–9:11 Ce qu'il a vu au Fuse : les systèmes deviennent piquants vers **6–8 kHz** à cause des transitoires. La zone **4–8 kHz** est délicate ; au-delà de 8 kHz, c'est de l'air.
- 9:33–10:15 Limiteur adaptatif issu de la gravure vinyle (Schwabe Digital) : il agit sur la pente des pics, pas sur leur niveau.
- 10:36–11:19 À fort niveau, **100–200 Hz** devient boueux et décroît plus longtemps.
- 11:39–12:23 Plutôt que d'égaliser en statique (master qui devient cassant), contrôle dynamique **sidechainé par le kick** : expansion à l'impact, puis ça s'efface.
- 12:44–13:26 À fort niveau, vérifier physiquement l'impact du kick contre la basse. Si le kick perd son impact, il est noyé : expansion ou transient designer.
- 13:48–14:29 Bilan : travailler entre **75 et 85 dB**, toujours vérifier beaucoup plus bas et beaucoup plus haut, et itérer.

À vérifier à l'écran : 0:37–1:07 (graphique ISO 226), 3:55 (lecture SPL basse), 7:44 (lecture ≈ 100 dB), 9:33 (interface de l'outil Schwabe Digital), 12:01 (réglage de l'expandeur sidechainé).

### RE-05 HEADPHONES vs SPEAKERS for Mixing? How to Get Sound You Can Trust — Warp Academy, 13:14, 2024-09-26, DAW/outils : Sonarworks SoundID Reference (courbe maison), courbes de réponse de casques, CanOpener (cité), SubPac (cité)
URL: https://www.youtube.com/watch?v=RpFsq9V3JI0
Qui : présentateur de Warp Academy (nom non dit), en collaboration avec Sonarworks (vidéo d'une série officielle Sonarworks, donc **contenu sponsorisé**, mais la méthode est exposée).
Transcription : oui (anglais, auto)
- 1:23–1:44 En fin de mix et de master, il garde toujours le casque comme point de référence, puisque beaucoup d'auditeurs écoutent au casque.
- 2:04 Le casque retire la pièce de l'équation : le grave est plus lisse.
- 3:24–3:45 Courbes de réponse : DT 990 Pro aux aigus accentués (excès **au-dessus de 5 kHz**, donc risque de sous-mixer les aigus) contre HD 650, plus plat.
- 4:07–5:09 Dispersion entre deux exemplaires du même modèle, et écart entre les transducteurs gauche et droit (balance). Ça fausse l'image stéréo.
- 5:29–5:49 Les casques ouverts dynamiques (série HD de Sennheiser) chutent fortement **sous 60 Hz**, la zone critique du kick et de la basse. Les planars (Audeze [ASR ?], HiFiMan) descendent mieux.
- 6:30–7:10 Au casque, le son arrive à 90°. Sur enceintes : triangle équilatéral à 30°, avec diaphonie et ombre de la tête (CanOpener la simule).
- 7:31–8:13 Au casque, le grave décroît plus vite et paraît donc moins fort. Risque : surmixer la basse.
- 8:33–9:34 Son cas : il surmixait la basse au casque. Correctif : **courbe maison SoundID +3 dB** dans le grave, pour retrouver la sensation de sa pièce.
- 9:54 Le tactile manque au casque : le SubPac le compense.
- 10:56–11:16 Il recommande une calibration individuelle de sa paire, réponse et balance L/R.

À vérifier à l'écran : 3:24 (graphes DT 990 vs HD 650), 5:49 (courbe de chute sous 60 Hz), 9:34 (réglage +3 dB de la courbe maison dans SoundID).

### RE-06 Mixing Masterclass: 'Mixing Your Track for the Club' at IMS College Malta — pointblank music school, 48:21, 2017-08-23, DAW/outils : DAW non nommé, Waves NLS, UAD SSL Bus Comp, Manley Massive Passive, Black Box HG-2, UAD tape, Sample Magic Magic AB, Mastering The Mix LEVELS [ASR ?], Bass Space (module de ce même plugin [ASR ?]), Plugin Alliance BX_control, API, Teletronix LA-2A
URL: https://www.youtube.com/watch?v=LUIXtDO4d8s
Qui : JC Concato, directeur créatif de Point Blank. Il mixe de la dance depuis le début des années 90 sur SSL et cite des mixes pour Sasha. Le titre est celui d'un ancien élève, sorti sur le label Point Blank.
Transcription : oui (anglais, auto)
- 0:48 En DnB, le kick est souvent plus fort que la basse.
- 1:56–2:43 En club, la **compatibilité mono** est capitale : plusieurs salles et petits systèmes (bar, etc.), où un riff panoramiqué peut disparaître. Un mix qui sonne en mono sonnera « awesome » en stéréo.
- 9:43–10:04 Il commence par le master bus : par exemple **+2 dB à 15 kHz** sur le master, pour moins traiter chaque piste.
- 12:13–13:48 SSL bus comp (UAD) en attaque lente et release rapide pour préserver le transitoire du kick. Environ **2 dB de réduction**.
- 14:13–14:58 Manley Massive Passive : léger boost vers **16–18 kHz** et à **60 Hz** (fréquence « posh »).
- 16:32–17:17 Black Box HG-2 : harmoniques paires/impaires, pour plus de loudness perçu à crête égale.
- 18:52–19:37 Les systèmes de club varient. Sur un mauvais système, un mix trop brillant devient insupportable : garder chaleur et punch.
- 19:59–21:09 Émulation à bande : compression du grave.
- 22:08–22:49 **Magic AB** (Sample Magic) en fin de master : jusqu'à **9 titres** avec points de repère. A = le mix, B = la référence, pour vérifier s'il est « dans le bon ordre de grandeur ».
- 23:38–24:58 Headroom avant mastering : la règle des 6 dB sert surtout à ne jamais dépasser 0, en sample peak comme en **true peak**. **3 dB** suffisent ; ici, **3,2 dB**.
- 25:20–25:46 Corrélation : si elle passe en négatif, problème de phase, une basse moins ronde et moins punchy, et pas de gravure vinyle possible.
- 26:35–27:37 Écoute mono, et écoute **d'un seul côté en mono** : vérifier que rien ne change radicalement.
- 28:02–29:14 « Bass Space » : on coupe le kick et la basse, puis on vérifie que **40 / 80 / 120 / 160 Hz** ne passent pas dans le rouge (rien d'autre dans la zone).
- 33:50–34:37 Kick : **+50 Hz**, petit creux vers **200 Hz** (résonance qui traduit mal en club), puis compresseur en attaque lente.
- 39:37–41:12 Basse : BX_control, mono maker vers « **7** » (« normalement je ne monterais pas si haut ») et largeur plus grande en haut. Forme en triangle inversé : mono en bas, stéréo en haut.
- 41:53–43:03 Émulation multipiste à bande à **15 IPS**, attaquée fort, pour égaliser les notes de basse.
- 43:45 LA-2A, **3–4 dB** de réduction.

À vérifier à l'écran : 22:08–23:14 (Magic AB, niveaux A/B), 24:58 (lecture de headroom 3,2 dB et true peak), 28:53 (affichage de Bass Space aux fréquences 40–160 Hz), 40:46 (valeur du mono maker de BX_control), 14:33 (bandes du Massive Passive).

#### Écartés
- RE-candidat « Reference Tracks in Mastering | Are You Listening? S2 Ep2 » (iZotope, UTiuavrGvqw) et « Mixing Low End » (iZotope, O2mzqlaBZbk). Pas spécifiques à l'électro ; non retenus.
- « Create Mixes That Translate » (SoundID/Sonarworks, 1tsk5tcC9iI, 47:58) et « motherclass #2: Audio Monitoring » (mothergrid, qiBIJpEXQxk). Non ouverts, faute de temps ; l'orientation électro n'a pas été vérifiée.
- Mastering The Mix « régler parfaitement les niveaux d'écoute » (xorYu60Rt0A, 4:07) et SoundID « calibrer le volume des enceintes » (-M9W3xP90_I, 3:16). Courts, contenus marque/produit ; RE-04 et RE-03 couvrent mieux le sujet.
- Julien Earle « Mixing & Mastering A Track For The Club Definitive Guide » (cf4Uh1PwVFQ) et Joachim Garraud « LOUDNESS, MASTERING, MIX AND STREAMING » (a0qxyTJwV7A). Pas ouverts ; pistes possibles pour le club vs streaming.

#### Manque
- Pas de vidéo où un ingénieur **calibre en direct** ses enceintes à 79–83 dB SPL avec du bruit rose et un sonomètre dans un contexte électro. RE-03 cite la méthode (valeur ASR douteuse) ; RE-04 donne les plages 75/85/100 dB sans montrer la mesure.
- Pas de démonstration **ADPTR Metric AB** par un ingénieur mastering électro sur les modules d'analyse (seulement le setup, RE-02). Rien non plus sur Mastering The Mix REFERENCE.
- Pas de comparaison chiffrée **master club vs master streaming** (deux versions d'un même titre) par un ingénieur reconnu.
- Correction de pièce (Sonarworks) : seule une vidéo sponsorisée (RE-05).

# Pré-master et outils pros

## Pré-master et stem mastering

### PR-01 HOW TO Mastering Levels & Gain Staging | Luca Pretolesi (3x Grammy Engineer) | TUTORIAL — mymixlab / Luca Pretolesi, 18:25, 2021-09-21, DAW/outils : Studio One 5, VU-mètre, compresseur type SSL, EQ
URL: https://www.youtube.com/watch?v=5XOXaxI3PGU
Qui : Luca Pretolesi (Studio DMI, Las Vegas), ingénieur mix/mastering présenté comme « 3x Grammy », EDM / house. Démonstration sur la session mix & master du remix de Diplo « Marea (We've Lost Dancing) » (d'après la description).
Transcription : oui (anglais, manuelle ; pistes auto en/es/pt aussi)
- 1:23 Standard analogique : 0 dB VU = −18 dBFS comme point de départ du gain staging (à 1:41 l'ASR dit « minus 13 » [ASR ?], la valeur cohérente est −18).
- 2:39–2:56 En mastering analogique, il part de 0 dB VU et gagne du niveau étape par étape (compression, EQ), avec parfois un écrêtage volontaire du convertisseur en fin de chaîne.
- 3:21 En 32 bits flottants, la marge est « infinie ». Le gain staging sert désormais à garder la même marge partout pour que les décisions restent cohérentes.
- 3:46 À Studio DMI, chaque projet de mix ou de master passe d'abord par une phase de préparation : tous les stems reçus (trop forts, trop faibles ou au bon niveau) sont recalés.
- 4:06–4:18 VU-mètre réglé pour que 0 VU = −18 dBFS. Objectif : la somme des stems sur la partie la plus forte du morceau doit tomber à 0 VU.
- 4:59–5:11 Session telle que livrée : le VU est saturé et le bus stéréo dépasse 0 dBFS en crête.
- 5:20–5:49 Ne pas baisser les faders : les plugins sont pré-fader et recevraient toujours trop de niveau. Il faut utiliser le gain d'entrée (clip gain / gain knobs).
- 6:12–6:38 Boucle courte sur la partie la plus chargée, puis −10 dB sur tous les stems pour atteindre 0 VU.
- 8:25–8:43 Avec un niveau constant, un preset (ex. compression SSL sur le kick) réagit pareil d'un morceau à l'autre, puisque le seuil voit le même niveau.
- 10:24–10:47 Compression d'environ 5 dB sur le kick, puis make-up gain pour revenir au même niveau de crête au VU : l'enveloppe change, pas le niveau.
- 12:29 Après l'EQ, il baisse la sortie pour revenir à 0 VU. 13:34 Il ne fait pas confiance à l'auto-gain et règle à la main.
- 16:41–17:42 Retour au niveau d'origine (sans les −10 dB) avec les mêmes plugins : la basse est dans le rouge et le bus stéréo dépasse 0. (interp.) Livrer des stems à un niveau raisonnable évite que l'ingé mastering doive tout re-niveler.
À vérifier à l'écran : 4:06 (calibration du VU sur −18), 6:38 (valeur du gain −10 dB sur les stems), 10:24 (réglages du compresseur sur le kick), 17:26–17:42 (niveaux du bus stéréo en rouge).

### PR-02 Understanding Loudness and Metering with Kirk Degiorgio - Pre-Master Level Metering Device — Sonic Academy / Kirk Degiorgio, 9:26, 2018-10-12, DAW/outils : DAW non nommé, VU-mètres, Waves Dorrough Meter
URL: https://www.youtube.com/watch?v=kjcFHo4vnm0
Qui : Kirk Degiorgio, artiste techno (présenté comme « Techno giant » par Sonic Academy), extrait du cours « Loudness and Metering ».
Transcription : oui (anglais, auto)
- 0:03–0:43 Cas du pré-master, le fichier que la plupart des producteurs exportent pour un ingé mastering : il faut lui laisser de la marge pour son matériel analogique.
- 1:26–1:41 Pas de limiteur sur le master bus. Le mètre sert seulement de repère visuel pour livrer un niveau optimal.
- 2:03–2:32 Mix fait « à la VU analogique » avec 3 bus : kick + basse ensemble, drums sans le kick, puis tout le reste (synthés).
- 3:06–3:25 Chaque bus tourne autour de 0 VU, calibré sur −18 dBFS. Le bus kick/basse est le plus fort, comme dans un morceau club.
- 4:24–5:12 Mesure finale au Waves Dorrough (émulation des mètres Dorrough des studios de mastering haut de gamme), référence réglée sur −18 dBFS (−20 possible).
- 5:25–5:44 Environ 40 segments, avec affichage des crêtes consécutives au-dessus de 0 dBFS.
- 6:00–6:21 Quand les ingés mastering demandent « −6 dB », ils veulent environ 6 dB de marge sous le full scale pour pouvoir limiter et clipper.
- 6:30–7:02 Vérifier les crêtes momentanées et les overs sur tout le morceau. Pour la moyenne, viser juste sous ou à l'entrée de la zone rouge de l'échelle type VU.
- 8:21–8:59 La rapidité du Dorrough attrape les crêtes rapides. Il le recommande sur le master bus.
À vérifier à l'écran : 3:06 (VU du bus kick/basse), 4:24–5:07 (réglage de référence du Dorrough sur −18), 6:56 (position de la moyenne sur l'arc), 7:36–7:44 (niveau master à fader 0).

### PR-03 TUTORIAL: Do We Really Need Headroom In Our Pre-master? Debunking MYTHS! — Zerotonine, 15:58, 2020-12-21, DAW/outils : Ableton Live (Utility, export)
URL: https://www.youtube.com/watch?v=-1Dt6IozmE4
Qui : Zerotonine, producteur drum & bass/neurofunk. Il précise à 10:22 qu'il n'est pas ingé mastering.
Transcription : oui (anglais, auto)
- 0:16–0:39 Règle d'or citée : pré-master avec crêtes à −6 dBFS, soit environ 6 dB de marge, encore demandée par les ingés mastering.
- 2:02–3:06 Démonstration : Utility +35 dB sur une piste et −35 dB sur le master. La piste dépasse 0 d'environ 34 dB.
- 3:41–4:28 Export avec le master non compensé, donc écrêté de 35 dB, mais en 32 bits flottants (dans Ableton, « 32 bits » est forcément flottant). Il faut vérifier que le DAW n'exporte pas en 32 bits fixe.
- 4:46–6:20 Le fichier exporté est réimporté, avec inversion de phase L/R contre l'original +35 dB : silence total au master, donc aucune perte.
- 6:52–8:00 Le fichier est rebaissé puis comparé à l'original : nouveau null parfait. L'ASR dit « −75 dB » [ASR ?] alors que la démo applique −35.
- 8:13–8:20 Conclusion : tant qu'on reste en 32 bits flottants, la marge du pré-master n'a pas d'importance, car l'ingé peut simplement baisser le niveau.
- 8:41–9:24 Exception : les plugins d'émulation analogique ont une réponse non linéaire, et pour eux le gain staging reste nécessaire.
- 11:40–13:02 Même export en 24 bits fixe : distorsion audible et pas de null. Le problème est réel hors du flottant.
- 14:06–14:39 Pour l'export, désactiver le warp (ou le mettre en mode haute qualité) et exporter à la fréquence de la session (48 kHz chez lui).
À vérifier à l'écran : 3:02 (mètres à +34 dB), 4:06 (options d'export d'Ableton, bit depth), 5:39 (master silencieux pendant le null test), 14:20 (fréquence d'échantillonnage à l'export).

### PR-04 Mixing into Limiters — Sonic Academy / Protoculture (Nate), 14:16, 2026-02-05, DAW/outils : DAW non nommé (raccourci Option-A pour bypasser), Ozone 12 Maximizer, ADPTR Metric AB
URL: https://www.youtube.com/watch?v=-yuO_A1YP9k
Qui : Nate, alias Protoculture (producteur trance/psytrance), formateur Sonic Academy. Il dit aussi masteriser pour d'autres.
Transcription : oui (anglais, auto)
- 1:06–1:36 Sur le master pendant l'écriture : Ozone 12 Maximizer en mode IRC Low Latency, qui attrape moins de crêtes mais ajoute peu de latence.
- 2:01–2:20 IRC 5 avec emphase transitoire : latence énorme. L'ASR dit « 649 seconds » puis « 300 » [ASR ? probablement ms]. En Low Latency : 7,9.
- 2:29 Option-A désactive le plugin (et la latence). Un simple bypass ne suffit pas.
- 2:40–4:41 Avec Metric AB en gain match, le limiteur rapproche le morceau des références déjà masterisées et aide à rester motivé.
- 5:11–6:21 Inconvénient : le limiteur cache les écrêtages internes et pousse à négliger le gain staging, qu'il faut revérifier.
- 7:19–8:03 Kick ±2 dB sans limiteur : différence nette. Avec limiteur, même 3–4 dB ne s'entendent presque pas. On ne peut pas décider du niveau du kick à travers un limiteur.
- 9:52–11:28 Distinction mix bus / master : sur le mix bus, il garde une compression de bus légère, une saturation à lampes, parfois une coloration extrême qui fait partie du son.
- 11:36–12:07 Erreur fréquente : couper la chaîne de mix bus avant l'envoi au mastering, et « la magie disparaît ». Garder la coloration, enlever seulement le limiteur.
- 12:07–12:21 Pour l'ingé mastering : crêtes à −6 dB maximum, et une moyenne dont l'ASR dit « −5 LS » [ASR ? valeur douteuse].
- 13:10–13:20 La compression de colle sur le bus drums fait aussi partie du mix : ne pas l'enlever.
À vérifier à l'écran : 1:06 (mode et réglages du Maximizer), 2:05 (latence affichée dans la console), 7:19–7:43 (valeurs du fader du kick), 10:46–11:20 (plugins de la chaîne de mix bus), 12:12 (niveau moyen exact conseillé).

### PR-05 Mixing & Mastering from Stems (FFL!) — pointblank music school / Justin Lyndley (avec Declan McGlynn), 49:29, 2015-05-29, DAW/outils : Logic Pro, Waves (API comp, NLS, L3), Maag EQ, Pultec, 1176/LA-2A UAD, transient designers
URL: https://www.youtube.com/watch?v=VZxHNPnuajQ
Qui : Justin Lyndley, formateur mixage Point Blank (crédits dans la description : Bloc Party, Amon Tobin, INXS). Le morceau, fait dans Ableton par un élève (Leo Luchini), est un titre hip-hop/électronique (« a hip-hop track », 37:57).
Transcription : oui (anglais, auto)
- 1:10–1:39 Définition : les stems sont des sous-mixes déjà traités (ex. une piste stéréo de drums). C'est un entre-deux mix/mastering qui donne plus de contrôle qu'un master stéréo et moins d'options qu'un mix complet.
- 4:16–5:18 Stems importés à plat, faders bas : 10 dB de marge sur la sortie.
- 6:00–7:05 Chaîne master : plugin stéréo gratuit avec mono sous un point de crossover (idée héritée du vinyle). Il a commencé à 120 Hz puis est passé à 100 Hz (« 100 Hz or below »).
- 7:19 Coupe-bas très légère à 23 Hz.
- 8:03–8:17 Compresseur API (Waves) avec le preset « modern mastering glue ».
- 9:01–9:27 Clone d'EQ Maag : bande d'air à 40 kHz, shelving très doux qui remonte le haut du spectre.
- 9:47 Pultec utilisé comme « enhancer » sans boost.
- 10:59–11:48 Waves NLS (canal Mike Hedges / EMI), avec drive.
- 12:10–12:34 Waves L3, limiteur multibande qui « n'aspire pas la basse » : environ +7 dB.
- 13:07–13:54 Mesure LUFS : −24 en broadcast US, −23 en Europe. Le morceau est à environ −11 ; −10/−9 évoqués.
- 16:03–16:39 Coupe-bas doux (12 dB/oct, comme les EQ analogiques) plutôt que des pentes raides sur chaque stem.
- 22:56–24:19 Stem drums : bas du kick recentré, très léger élargissement ; shelf large +20 Hz, snare à 3 kHz, shelf −10 kHz sur les cymbales.
- 24:43–25:43 Transient designer : clone SPL de NI contre l'Enveloper de Logic, dont le seuil évite d'accentuer les charlestons.
- 26:16–27:19 Bus parallèle sur les drums : 1176 + EQ API + NLS.
- 29:10–29:46 Extraction de la caisse claire d'un stem drums par gate avec filtre de sidechain, puis envoi dans une reverb à ressort.
- 35:07 Automation de volume des charlestons dans les sections où ils ressortent trop après compression (ce que font aussi certains ingés mastering).
- 35:44–36:28 Problème de bounce : queue coupée à la fin. Corrigé avec un envoi automatisé vers une plate (Space Designer).
- 37:26 Ajouter un peu de silence au début du bounce.
- 43:12–43:26 Conseil : bouncer le mix avec 3 à 6 dB de marge (« six to three dB »), puis masteriser dans un projet séparé.
- 43:32–44:43 Bounce de stems : ne pas les rendre ni très forts ni très faibles, surtout sans écrêter. Ici la somme était trop haute et il a tout baissé pour avoir environ −10 sur le bus ; « −10 n'est pas une mauvaise idée ».
- 45:09–45:42 Sur un compresseur de bus SSL : 4:1, attaque longue pour laisser passer le punch avant le limiteur, release rapide ou Auto.
- 46:08 Moins de 1 dB de réduction de gain sur le compresseur de colle.
- 47:41–47:48 Bilan du gain staging : départ avec 10 dB de marge, petites hausses en route, +7 dB au L3.
- 48:07–48:27 Les plugins UAD sont calés sur un zéro analogique : on les attaque facilement trop fort, donc surveiller les VU.
À vérifier à l'écran : 6:59 (fréquence de crossover mono), 12:29 (réglages du L3), 13:47 (valeur LUFS affichée), 23:30–24:13 (courbe d'EQ du stem drums), 29:21 (réglages du gate et du filtre de sidechain).

### PR-06 Un Stem Mastering de A à Z [Electro-Pop] — MasterByGreg, 1:11:51, 2026-09-19, DAW/outils : Reaper, Distressor, compresseurs, imageur, M/S, impression via chaîne analogique (« machines »)
URL: https://www.youtube.com/watch?v=-kQh_72qGwE
Qui : Greg (MasterByGreg), ingénieur mastering/mixage indépendant (services sur masterbygreg.com). Session client réelle pour l'artiste Augustin, titre entre pop et 2-step (selon la description).
Transcription : oui (français, auto). Beaucoup de passages musicaux ; peu de valeurs chiffrées.
- 0:55–1:18 Méthode en 2 temps : d'abord correction et rééquilibrage des stems, puis passage dans les machines et finalisation.
- 3:13–3:56 Pourquoi un stem master : il avait le mix complet et les stems, mais la voix trop médium et dure ne pouvait plus être corrigée au mix (changement d'ordinateur, plugins manquants).
- 4:01–4:46 Notes de départ : voix à éclaircir avec sa réverbe incluse (bus complet), beaucoup de M/S prévu, synthés qui manquent de présence dans le mid, drums à rendre plus clairs et punchy. Écoute du mid seul via la carte son.
- 5:53 De-esser et dynamique sur la voix.
- 9:05–10:01 Module « impact » sur le groupe du kick : un peu plus de sub et d'attaque.
- 10:48 « gold clip » sur les drums [ASR ? peut-être GClip].
- 13:15–13:35 Sidechain externe : le bas de la basse est compressé par les drums.
- 15:38–15:52 Basse limitée fort avec un petit limiteur : « +10 −10 » (gain d'entrée/sortie) [ASR ? nom du limiteur inaudible].
- 18:58 Distressor sur un stem.
- 24:34–27:34 Voix : piste parallèle (envoi) dé-essée, compressée fort au ReaComp, très large, puis mélangée à l'originale pour l'espace.
- 29:13–31:11 Compression sur les synthés avec un compresseur cité « VM comp de Pulsar » [ASR ?], entrée « dual input ».
- 33:59–34:05 Pas de clipper à ce stade, puisque tout repasse ensuite dans les machines.
- 46:23–46:42 Vérification du mid et des sides, puis contrôle en mono avant l'impression.
- 52:46 Automation de volume sur les refrains, environ « 06 » [ASR ? +0,6 dB ?].
- 54:30–54:36 Gain match pendant le travail, compensation au dernier limiteur.
- 54:50–54:58 Gain cité « 8 dB, au moins 8.4 » [ASR ?].
- 55:07–56:17 Choix du dernier limiteur : preset « punchy » d'un plugin dont le nom est mal transcrit [ASR ?], valeurs « 925 » et « −0.2 » [ASR ? probablement un plafond à −0,2 dB].
- 1:01:49–1:04:42 Retours du client : moins de réverbe et de largeur sur la voix, moins de compression (Distressor allégé). Automation de compression couplets/refrains, valeurs « −40 / −30 » [ASR ?].
- 1:07:42 Gain d'impression noté « 330 en boost » [ASR ?] pour refaire la même chaîne après correction.
À vérifier à l'écran : 15:45 (limiteur sur la basse et ses réglages), 26:25 (réglages du ReaComp en parallèle), 54:50–56:17 (gain et plafond du limiteur final), 1:07:42 (valeur de gain relevée).

#### Écartés
- _9G4eFb6_S4 « Stem Mastering An Electronic Song - Popcorn by Plurthlings » (Mastering The Mix, 45:32) : presque sans parole, aucune valeur dite.
- VFoAz4mhd3o « Top Mastering Engineers Reveal Their Process » (Agartha Podcast, 1:21:55) : compilation générique, intervenants non identifiés dans la description, pas axée électronique.
- D1_X0BmgDMM « Top Signs Your Mix Isn't Ready for Mastering » (iZotope, Jonathan Wyner, 15:17) : excellent et chiffré (crêtes −3/−2/0 dBFS avec RMS −16/−20 = signal d'alerte ; RMS et LUFS momentané à 1–2 dB l'un de l'autre), mais centré sur la voix et pas sur l'électronique. Remplaçant possible.
- Non ouverts, notés en recherche : Strob Studio « COMMENT EXPORTER CORRECTEMENT SON MIX POUR UN MASTERING STEREO » (5SkmVOCYb8o), Streaky « Preparing a track for mastering » (mBVqFyf-rnE), Distinct Mastering « Limiter on master bus: stop » (vYtgMjzaxCs), Dan Worrall « Always Leave 6dB Headroom » (V76L4PRSPFE), Sean Divine « Mastering Stem : quand et pourquoi » (UpmZHfPw4Fc). Pistes de remplacement si besoin.

#### Manque
- Je n'ai trouvé aucun ingé mastering spécialisé techno ou DnB (label) qui détaille de bout en bout des réglages d'export : bit depth, fréquence, dither et format de livraison. Zerotonine couvre le 32 bits flottant et la fréquence ; le dither n'est dit qu'en passant (PML : POW-r 3, voir OU-04).
- Le stem mastering vraiment électronique (house/techno) reste faible : les deux sessions retenues portent sur un titre hip-hop/électronique (Point Blank) et un titre électro-pop/2-step (MasterByGreg).
- Pas de vidéo française d'ingé reconnu sur « préparer son mix pour le mastering » vérifiée par transcription.

## Outils pros

### OU-01 Luca Pretolesi - Drum Buss + Stereo Buss Clipping with Lift 3 — StudioDMI / Luca Pretolesi, 5:30, 2022-03-11, DAW/outils : Acustica Audio Diamond Lift (Lift Mix et Lift Master), DAW non nommé
URL: https://www.youtube.com/watch?v=VAWsxLhRntQ
Qui : Luca Pretolesi (Studio DMI). Vidéo liée à une promo Acustica (prix dans la description), mais la méthode et les valeurs sont données.
Transcription : oui (anglais, auto)
- 0:33–0:47 Lift Mix sur le bus drums (percussions graves, percussions aiguës, kicks) et Lift Master sur le bus stéréo. Objectif : −4 RMS avec seulement deux plugins.
- 1:01–1:09 Sur le bus drums : un peu de saturation, ouverture du haut vers 7–10 kHz.
- 1:09–1:23 Mode 3 de clipping, en mid seulement, pour ne pas détruire les transitoires ni ce qui est hors du mono.
- 1:25–1:33 Entrée +12 dB, saturation 80, clipping 100 sur le mid, sortie baissée.
- 1:43 Objectif : imiter le son d'un convertisseur AD qui écrête.
- 2:14 Le niveau oscille entre −4,5 et −5 RMS.
- 2:38–2:47 Lift drums bypassé : le RMS bouge peu (« f dB » [ASR ? 1 dB ?]), alors que la perception change de 2 à 3 dB.
- 3:08–3:26 Le boost 7–10 kHz qui frappe le clipper mid ramène les crêtes du kick à zéro. Résultat : plus de séparation et de dynamique perçue, RMS inchangé.
- 3:34–3:55 Lift Master en clipping stéréo mode 2, plus doux. On monte le niveau sans aplatir les sides ; ouverture à 2 kHz avec une autre courbe que sur le bus drums.
- 4:39–5:12 Sans le clipper master, les crêtes reviennent. Les deux clippers rasent les crêtes des drums et laissent la musique intacte ; le clipper final sert de plafond « ni hard ni soft ».
À vérifier à l'écran : 1:09 (mode, entrée et réglages Mid du Lift Mix), 1:25 (valeurs saturation/clipping), 2:14 (lecture du RMS), 3:37 (réglages du Lift Master en mode 2).

### OU-02 Kclip & Ableton Live: Transparent Clipping for Louder Mixes — Seed To Stage, 24:34, 2022-05-05, DAW/outils : Ableton Live (Saturator, Glue Compressor, mètres), Kazrog KClip 3, FabFilter Pro-L 2
URL: https://www.youtube.com/watch?v=M1g6cG82_ww
Qui : Seed To Stage, formateur Ableton. Ses liens renvoient à ses projets EarthCry et Papadosio. Démonstration sur un morceau chill bass.
Transcription : oui (anglais, auto)
- 0:07–0:21 Repères donnés : streaming environ −12/−14 LUFS ; Beatport et mixes club environ −8 à −4 LUFS.
- 1:19–2:04 Pro-L 2 pour son mètre LUFS : true peak −1 dBTP, oversampling activé.
- 2:18–2:52 −14 LUFS passe bien ; à −8/−4 LUFS, le Pro-L 2 seul détruit le son. 3:18 Allonger la release et raccourcir l'attaque rend le son « splatty ».
- 4:00–5:30 EQ avant limiteur : coupe du sub inutile, creux sur une bosse résonante du médium, légère hausse du haut-médium et de la présence (tilt). Malgré ça, impossible de dépasser −10 LUFS sans distorsion.
- 5:45–6:52 Une série de clippers activés d'un coup (pistes, bus, juste avant le Pro-L 2). Le limiteur travaille beaucoup moins, ce qui permet moins d'attaque et une release plus courte.
- 9:03–9:31 Mètres d'Ableton déployés : vert clair = RMS, vert foncé = crête.
- 9:53–10:42 Saturator en Analog Clip, +10 dB en entrée et −10 dB en sortie sur le kick : crête de −3,64 à −9,61 dB, soit environ 6 dB gagnés sans différence audible.
- 11:31–12:02 À +15/−15 : environ 10 dB gagnés, mais la saturation s'entend. 12:23 À 13/−13, ça s'entend encore. 13:13 Le Saturator est transparent jusqu'à environ 10 dB.
- 14:36–15:11 KClip 3 avec entrée/sortie liées : transparent à 13/−13 sur le kick, distorsion audible vers 14. Il cite Baphometrix comme référence sur le sujet.
- 15:11–15:41 Algorithmes Crisp et Soft (le soft rend la distorsion plus audible). 15:58 « Wet » pour écouter uniquement la partie écrêtée.
- 16:28–17:31 KClip sur le bus drums à 13/−13 : crête de −11,2 dB, environ 1 dB gagné en plus.
- 17:54–18:45 KClip sur le master avant le limiteur : crête −5,6 dB sans clip, nettement moins avec.
- 18:55–22:40 Contre-exemple, une queue de réverbe : le clipper s'entend. Il passe à la Glue (attaque minimale, seuil vers −12), puis KClip en Crisp à 8/−8, transparent.
- 22:48–23:04 Chaque ajout de son oblige à revérifier les étages de clipping.
- 23:04–24:23 −5 LUFS ne convient pas à ce morceau. La musique qui supporte ces niveaux a déjà de la distorsion harmonique et un spectre penché vers l'aigu.
À vérifier à l'écran : 2:04 (réglages du Pro-L 2 : true peak, oversampling, style), 10:19 (algorithme et Drive du Saturator), 14:52 (KClip : entrée/sortie, oversampling, algorithme), 17:27–17:31 (lectures de crête du bus drums), 18:38 (crête du master).

### OU-03 SSL Buss Comp for House & Techno: AudioScape vs UAD vs Ableton — Rapid Flow, 13:58, 2024-09-20, DAW/outils : Ableton Live (Glue Compressor), UAD SSL G Bus Compressor, AudioScape Buss Compressor (hardware, convertisseurs Prism Orpheus)
URL: https://www.youtube.com/watch?v=CsN-36N9BU0
Qui : producteur house/techno de la chaîne Rapid Flow (la page Facebook en lien est « SetsunaMusic »). Il fait du placement de ses propres templates à 12:01, et le hardware lui a été prêté dans le cadre d'une collaboration avec AudioScape.
Transcription : oui (anglais, auto)
- 0:46–1:20 Technique apprise d'un ingé « Grammy winning » dont il a remixé un titre : dans son projet, le Glue Compressor d'Ableton était en 4:1 et attaqué très fort.
- 1:27–1:36 Réglage « slam » : release la plus rapide, attaque la plus lente, ratio 4:1, sans coupe-bas de sidechain. Effet : plus de médiums, de présence et de drive, sans détruire le kick.
- 2:15–2:22 Le signal est envoyé très fort dans le compresseur pour obtenir beaucoup de réduction de gain.
- 2:28–2:47 Réglage classique : 4:1 (« ce que j'aime pour l'électronique »), release Auto, attaque 30 ms (en dessous, les transitoires du kick s'écrasent). On fait juste « chatouiller » l'aiguille pour la colle et la largeur.
- 3:28–3:56 Le pad gaté paraît panoramiqué 15 à 20 % plus large avec le compresseur.
- 4:35–5:01 Mêmes réglages sur le Glue et le SSL UAD : release la plus rapide, ratio 4, attaque 30 ms, puis on pousse.
- 5:01–5:43 Pousser jusqu'à ce que le bas perde sa vie, revenir en arrière, puis compenser avec le gain.
- 7:04–8:21 Comparaison : le hardware garde plus de poids dans le bas. Les plugins élargissent aussi, mais retirent un peu au signal mono (kick, basse).
- 8:34–8:46 Le coupe-bas de sidechain est laissé désactivé pour cette technique.
- 9:16–10:18 Analyseur L/R : le kick reste parfaitement centré à travers le hardware.
- 10:51–11:08 Un écart de ±1 dB entre 30 et 80 Hz sur un canal décentre le kick, ce qui pose problème en musique électronique.
À vérifier à l'écran : 1:27 (positions des boutons du hardware), 2:28 (réglages conservateurs), 4:53–5:43 (Glue et UAD : seuil, réduction de gain, make-up), 9:59–10:16 (analyseur stéréo).

### OU-04 Mastering - Simple but Effective | Ableton Live 10 (only stock effects) — Production Music Live / Guido (Cat and Beats), 25:32, 2019-09-12, DAW/outils : Ableton Live 10 (Color Limiter, Compressor, Utility, EQ Eight en M/S, Limiter ×2)
URL: https://www.youtube.com/watch?v=RoiqyPM8B5w
Qui : Guido, de la chaîne Cat and Beats, formateur mixage/mastering chez PML.
Transcription : oui (anglais, auto)
- 0:21–0:31 Chaîne : Color Limiter, Compressor, 2 Utility, EQ Eight, Limiter, Limiter.
- 1:11–1:21 Écouter en 4 bandes : grave, bas-médium, haut-médium, aigu. 1:30 Utiliser une référence du même style.
- 1:58–2:30 Sur la partie la plus forte, régler le master pour des crêtes entre −10 et −6 dB, et la référence au même niveau de crête.
- 3:16–3:59 Color Limiter utilisé comme EQ en bascule (tilt) : saturation environ 20, bouton Color pour pencher vers le grave ou l'aigu.
- 6:17–6:26 Démonstration du compresseur volontairement extrême : 10:1, attaque 0, seuil bas.
- 7:01–7:37 Attaque de 5 à 10 ms pour un « tick » (kick techno) ; de 25 à 50 ms, voire 60, pour un son plus épais. 8:12 Il retient environ 20 ms.
- 8:36–8:53 Release passée de 1 (très distordu) à 10 pour faire ressortir l'impact.
- 9:14 Ratio ramené à 2:1.
- 9:50–11:11 Bouton EQ du sidechain interne : en montant la fréquence, la réduction de gain ne réagit plus qu'au haut du spectre (snare, charleston), plus au kick.
- 11:21–11:40 Les deux Utility (mono et side seul) sont mappés en macro (Cmd-K), et l'EQ Eight passe en mode M/S.
- 12:48–13:52 Mid : boue entre 150 et 600 Hz, petite coupe qui libère l'impact du kick, puis léger ajout de bas (« Pultec technique »).
- 14:09 Les mouvements de l'EQ Eight sont petits : 1,36 dB, c'est déjà beaucoup.
- 14:25–14:54 Coupe-bas contre le grondement, oversampling de l'EQ Eight activé.
- 15:05–15:25 Présence entre 1 et 3 kHz.
- 15:47–16:21 Side : coupe-bas prudent pour ne pas perdre la chaleur. 16:43–17:11 Petit boost d'air et de brillance sur les sides.
- 18:23–19:48 Double limiteur. Le premier a un lookahead très court et sert de détecteur : on règle le gain jusqu'à environ 7,5 dB (19:28), puis on recule un peu ; s'il distord, on cherche la cause dans le mix.
- 20:16–21:47 Dernier limiteur avec plafond à −1 dB pour une sortie en ligne, car la conversion en MP3/OGG/AAC ajoute environ 1 dB et peut écrêter.
- 22:12–22:52 Cible RMS dans les mètres d'Ableton : de −9 à −7, en visant environ −7/−8 dans le drop et en comparant à la référence.
- 23:18–23:33 Résultat : environ −2 dB de limitation pour environ −7 RMS.
- 23:41 Dry/Wet de la chaîne pour comparer à un simple limiteur.
- 25:16–25:29 À l'export : 24 ou 16 bits, avec dither POW-r 3.
À vérifier à l'écran : 3:33 (valeurs du Color Limiter), 9:14–10:43 (compresseur : ratio, attaque, release, fréquence de l'EQ de sidechain), 13:20–17:30 (courbes de l'EQ Eight en M/S), 19:28 et 22:45 (gain, lookahead et plafond des deux limiteurs), 25:22 (réglages d'export).

### OU-05 How to Master Drum & Bass With Ozone 11 — Unders - Warrior Sound, 18:17, 2023-09-11, DAW/outils : iZotope Ozone 11 Advanced (Master Assistant, EQ, Master Rebalance, Impact, Imager, Clarity, Stabilizer, Dynamic EQ, Maximizer), DAW non nommé
URL: https://www.youtube.com/watch?v=O4yWTXJL-jE
Qui : Unders (Warrior Sound), producteur liquid drum & bass et formateur. Il masterise son propre titre (« All Night Long »). DistroKid sponsorise la vidéo (2:52).
Transcription : oui (anglais, auto)
- 0:17–0:27 Fichier d'entrée : mix sans crête au-dessus de 0, 44,1 kHz / 24 bits, avec de la marge.
- 0:31–0:46 Fondus d'entrée et de sortie de sécurité.
- 0:51–1:20 Master Assistant : il lui fait écouter la boucle de la partie la plus forte (le drop).
- 1:47–2:01 Bouton de gain match dans la vue Assistant pour comparer honnêtement.
- 2:17–2:39 Le résultat est trop dur. Il charge une courbe cible perso (Custom) et relance l'analyse.
- 3:25–3:43 Passage en mode avancé. Ozone ajoute une remontée sous 20 Hz alors qu'il n'y a rien à cet endroit : supprimée.
- 3:49–4:25 L'EQ de l'Assistant ne bouge qu'environ ±1 dB, et un curseur global en dose l'intensité.
- 4:43–4:59 Shelf grave remplacé par un coupe-bas de 24 dB/oct, voire 12, plutôt que 48.
- 5:18–6:21 Master Rebalance placé avant l'EQ pour tester voix/basse/drums. Pas de changement : la balance est jugée bonne.
- 6:26–7:14 Impact : écoute en solo et en Delta (réglage « 100 ms » cité). Effet minime dans le bas, donc retiré.
- 7:18–8:18 Imager : élargir l'air reste corrélé. Élargir le haut-médium (voix, snare) crée des annulations : à réduire.
- 8:29–8:46 Le grave reste à une corrélation de 1, même sur les basses en balayage, grâce au mix.
- 9:20–10:31 Clarity, une sorte d'EQ dynamique très fin : c'est de là que vient la brillance (charlestons). Il le juge trop dur et le réduit d'environ 5 %.
- 12:19–13:07 Stabilizer : en Delta, il prend la voix et le haut mais dompte le très grave, si bien que le kick perd son poids. Retiré.
- 13:35–14:31 Dynamic EQ : l'Assistant a bien trouvé une résonance et la dureté de la voix. Conservé.
- 14:37–15:06 Gain match désactivé pour régler le niveau final. Mètres en RMS + crête, ou LUFS intégré / court terme.
- 15:42–15:55 −14 LUFS suffirait pour le streaming seul, mais il veut aller plus fort.
- 16:21–16:31 Maximizer : mode IRC (« modern » selon l'ASR [ASR ?]), caractère vers « Fast/Loud », True Peak activé.
- 17:02–17:19 Emphase transitoire remontée jusqu'à environ 50 pour récupérer le kick.
- 17:35–17:53 Plafond à −0,01 dBFS avec true peak. On lui avait appris −0,3 « à l'époque du L2 ».
À vérifier à l'écran : 2:30 (courbe cible custom), 3:43 et 4:51 (EQ : coupe-bas et pente), 10:31 (quantité de Clarity), 16:21–17:19 (Maximizer : IRC, caractère, transient emphasis, true peak), 17:35 (plafond et LUFS affichés).

### OU-06 Fabfilter Pro-MB | How to Sidechain Sub to Kick on a Premaster | Mastering Tutorial — Plugin Boutique / Joshua Casper, 8:09, 2019-04-24, DAW/outils : FabFilter Pro-MB (DAW non nommé)
URL: https://www.youtube.com/watch?v=8Onqmf5OlzU
Qui : Joshua Casper, producteur électronique et formateur, pour Plugin Boutique. Démonstration sur un pré-master tiré d'un pack de samples.
Transcription : oui (anglais, auto)
- 0:21–0:51 Cas typique : on reçoit un pré-master trop chargé en sub, sans sidechain, et le kick ne respire pas. Le Pro-MB permet de corriger sans demander les stems.
- 0:57–1:24 Ajout d'une bande. Tirer le nœud vers le bas en fait un nœud d'EQ ; Ctrl-clic remet à zéro.
- 2:04–2:26 Position sur le sub, seuil baissé. Le range fixe la profondeur de coupe (−30 dB dans l'exemple extrême).
- 2:46–3:08 Onglet Expert : passer le déclenchement de « Band » à « Free ». Une plage de fréquences séparée commande alors le compresseur de la bande.
- 3:08–3:45 « Audition » du déclencheur, à caler sur la fondamentale du kick.
- 4:04–4:27 Version extrême, qui retire trop de sub. Il solote la bande pour écouter ce qui est compressé.
- 4:50–5:23 Pente de la bande portée à 48 dB/oct (valeur tapée au double-clic) pour ne pas mordre sur le kick. Contrairement au Pro-Q 3, le Pro-MB n'a pas de brickwall.
- 5:41–5:47 Limite basse de la bande vers « 36 » [unité non dite, probablement Hz].
- 6:09 Range réduit. 6:23–6:33 Attaque à 0 %, release rapide : le sub n'est creusé que pendant le kick et revient après.
- 6:55–7:11 Lookahead poussé pour une attaque encore plus rapide. La latence n'est pas gênante en mastering.
À vérifier à l'écran : 2:23 (seuil et range), 3:00–3:36 (plage du déclencheur Free), 5:23–5:47 (pente et fréquences de la bande), 6:29 et 7:01 (attaque, release, lookahead, ratio).

#### Écartés
- r4d0F7VaW7E « KClip 3 - Mastering Tutorial » (Kazrog, Shane McPhee, 8:24) : très utile techniquement. Le plafond est un second clipper à 0 dBFS non suréchantillonné ; avec +1,8 dB de crêtes intersample, on baisse la sortie de 2 dB ; démo avec 8,3 dB de clipping ; cible de loudness par défaut −14 LUFS. Mais le genre n'est pas indiqué et le contenu recoupe OU-02. Meilleur remplaçant.
- kV1cWSiNsLA « FabFilter Pro L 2 Mastering 10 Tips » (Reid Stefan, 10:09) : peu de valeurs dites (style Modern, linking juste sous 100 %, attaque doublée par rapport au défaut, oversampling coupé « plus crisp »), aucune cible LUFS chiffrée, pub pour des samples au milieu.
- Repérés en recherche mais non vérifiés : Ruffin Studio « minimal house … mastering with iZotope Ozone 11 » (xcOo4Hf0dks, 30:20), Plugin Boutique « Ozone 10 – Maximizer et Soft Clip avec Bill d'iZotope » (judSF2iv-BQ), Hardcore Bob « How Clipping ACTUALLY works (StandardClip) » (Qyp5q6Ont84), Matthew Vere « How Skrillex uses limiters and clippers » (4RMIgKGF2Zg).

#### Manque
- Je n'ai pas de vidéo dédiée au Pro-L 2 par un ingé mastering électronique avec des réglages complets. Les valeurs Pro-L 2 viennent d'OU-02 (−1 dBTP, oversampling) ; aucune vidéo Pro-Q n'est retenue.
- Pas de StandardCLIP ni de GClip vérifiés par transcription (le « gold clip » de PR-06 est incertain).
- Ozone : une seule session réelle (DnB). Rien en français vérifié, rien sur la house ou la techno.
- Pas d'ingé mastering reconnu (crédité sur des labels) en démonstration directe d'outils, à part Pretolesi (OU-01).
