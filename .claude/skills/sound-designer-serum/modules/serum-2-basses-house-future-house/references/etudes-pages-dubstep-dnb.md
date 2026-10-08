# Études des tutoriels écrits : Dubstep et Drum and Bass

Lecture du 05/10/2026, par `curl -sL` puis extraction du texte (titres, paragraphes, listes, légendes, texte alternatif). Identifiants : registre `tutoriels-a-consulter.md` ; documentation de fond : `documentation-basses.md`. Rien n'a été écouté : ni audio intégré, ni vidéo. Les valeurs ci-dessous sont celles que le texte écrit ; ce qui n'est montré qu'en image est signalé comme tel.

Bilan : 12 pages lues sur 13 (dont 3 qui ne sont qu'un chapeau ou un résumé de vidéo), 1 échec (academy.fm).

---

### F08-04 How to Make Dubstep Growls in Serum 2 — Maxim Hetman, Monosounds.studio (Serum 2, 3 juillet 2026)
Titre de l'onglet : « Serum 2 Dubstep Growl Tutorial: My Full Recipe » (c'est celui du registre) ; le titre H1 est celui ci-dessus.
- Statut : page lue le 05/10/2026 (HTTP 200).
- Gestes et réglages écrits, dans l'ordre :
  - Oscillateur A : pas la saw par défaut. Balayer `WT Position` sur les tables d'usine et garder celle qui « parle » déjà sans traitement ; ou enregistrer « yah-woh-yoi », couper, déposer le .wav sur l'osc A (Serum 2 le convertit en wavetable ; une source à hauteur stable se convertit le plus proprement). Départ : unison à 1 pendant la conception (mono : plus de punch, moins de CPU), une octave plus bas, niveau vers 75 %. Premier geste de modulation : un LFO sur `WT Position`.
  - Warp : `Bend` vers 30–50 % (« nasal snarl ») ; le même LFO que `WT Position` envoyé aussi sur la quantité de warp, à la moitié de la profondeur. `FM` : sinus sur l'osc B une octave sous A, warp de A en « FM from B » : 15–25 % = râpe gutturale ; au-delà de 40 % = métallique et criard (bon pour un drop, pénible ailleurs).
  - Filtre : types « formant » de Serum 2 (le cutoff devient un sélecteur de voyelle). LFO lent ou enveloppe sur le cutoff, **petite** amplitude (« oh » → « ah » = un petit mouvement). Résonance 20–40 % ; plus haut, ça siffle.
  - Trois couches de mouvement vocalique (WT Position, warp, formant), chacune pilotée par une source légèrement différente.
  - FX (ordre plus important que les valeurs ; distorsion avant phaser, sinon « fizz ») : 1 Distortion mode Overdrive, drive 40–60 % ; 2 Phaser rate 1/2 sync, feedback 60 %, mix 50 % ; 3 EQ passe-haut 120 Hz, creux de 3 dB vers 400 Hz ; 4 Compressor multibande, calmer la bande 2–5 kHz ; 5 Hyper/Dimension mix 15–25 % pour la largeur. Serum 2 a plusieurs bus FX : les oscillateurs du growl sur leur propre bus, le propre ailleurs. Un LFO sur le feedback du phaser ajoute une couche de « parole ».
  - LFO : forme dessinée, 3 ou 4 marches à hauteurs différentes, chutes courbes, sync 1/2 (dubstep 140–150 BPM en half-time). Second LFO plus rapide à 1/8, faible profondeur, sur le filtre formant (« syllabes dans le mot ») ; grille triolet pour le rebond « yoi yoi ». FAQ : mouvement principal 1/2, syllabes 1/8, rebond 1/4 triolet ; au-delà de 1/16 on n'entend plus de la parole mais une texture. Glisser-déposer l'en-tête du LFO sur WT Position, warp et cutoff du formant, profondeur propre à chaque destination.
  - Resampling : imprimer une note tenue de 2 à 4 mesures, FX compris ; la réinjecter (déposer le .wav sur un oscillateur, découpé en wavetable, ou « Resample to Oscillator ») ; nouveau warp, nouveau formant, nouveaux FX ; 2 à 3 passes (« au moins deux » pour leurs presets). Règle : changer le rythme de modulation à chaque passe, sinon les couches « bavent ».
  - Oscillateur spectral (Serum 2) : couper des groupes de partiels aigus = son creux, guttural ; faire glisser des partiels les uns contre les autres = grain inharmonique ; morpher les frames au LFO = voyelle sans filtre formant. CPU : unison 3–5 plutôt que 16, polyphonie limitée, conception en suréchantillonnage 2x.
- Conseils de jeu ou de mix : le growl vit dans les médiums, 150 Hz–2 kHz ; le sub reste une couche séparée, intacte, **hors de la distorsion**. Growl « maigre » : il manque presque toujours le sub ; passe-haut sur le growl vers 120–150 Hz et sinus propre ou 808 dessous ; si les médiums sont faibles, une passe de resampling de plus. Presets Serum 1 ouverts par Serum 2, bons à resampler.
- Limites : deux infographies (« Talking Rhythm Cheat Sheet », « The Resample Loop ») en image seulement, non lues. Aucune enveloppe d'amplitude, aucune macro, aucune note MIDI. Valeurs en fourchettes. Les noms « Resample to Oscillator » et « Hyper/Dimension » sont ceux de la page, non vérifiés dans Serum 2. Page d'un vendeur de presets (renvois commerciaux). Petite tension : unison 1 « en conception » puis unison 3–5 pour le spectral.
- Utilité pour une recette : la plus chiffrée du lot pour un growl Serum 2 (Bend 30–50 %, FM 15–25 % / >40 %, résonance 20–40 %, chaîne Overdrive → Phaser 1/2 fb 60 % → EQ HP 120 Hz, LFO 1/2 + 1/8) ; base directe de la fiche « growl vocal ».

### F08-17 How to Make a Skrillex Growl in Xfer Serum — ADSR Sounds, vidéo par « Larson from ADSR » (Serum non précisé pour la recette ; date non donnée)
- Statut : page lue le 05/10/2026 (HTTP 200). Vidéo YouTube intégrée (`_e9ARJECJPU`) non visionnée.
- Gestes et réglages écrits, dans l'ordre :
  - Wavetable : table maison construite à partir de plusieurs opérateurs FM (outil non nommé) : opérateur A = forme de base riche en médiums ; B et C modulent A (grain, mouvement) ; D = FM sinus discrète pour équilibrer l'aigu. Alternative : tables Analog ou Digital de Serum, ou table d'un pack.
  - LFO 1 → Wavetable Position, en boucle d'**1 mesure** (« 1 Bar loop »). Second LFO → quantité de FM et cutoff du filtre.
  - Filtre : passe-bande pour centrer les médiums, résonance « modérée », lié au LFO principal (imite un filtre formant).
  - FX : Distortion mode Diode II ; Phaser « réglé vers 50 Hz » (paramètre non précisé) ; EQ : coupe des bas-médiums vers 300 Hz ; compresseur multibande (OTT) ; Dimension Expander (largeur, grave au centre).
  - Sub : Sub Oscillator de Serum en sinus, propre et mono ; éventuellement un peu de bruit ou d'hyper-dimension.
  - Dans le DAW : automatiser cutoff, drive de distorsion, position de table.
  - Section « Serum 2 » : seulement « dual filter routing, granular oscillator modes, expanded modulation », sans réglage.
- Conseils de jeu ou de mix : modulation constante ; EQ à 300 Hz contre la boue ; grave centré.
- Limites : aucune profondeur de modulation, aucune valeur de résonance, de drive ni de mix ; « phaser vers 50 Hz » ambigu ; l'oscillateur modulant de la FM n'est pas nommé ; le Sub Oscillator dans le patch du growl va contre la règle « sub et basse médium dans deux instruments ». Version de Serum non écrite pour la recette (la section 5 présente Serum 2 comme un prolongement) ; si la vidéo est en Serum 1 : à traduire dans Serum 2 (Diode II, Dimension Expander, Sub Oscillator à vérifier dans Serum 2).
- Utilité pour une recette : un repère qualitatif (LFO 1 mesure sur la table, passe-bande résonant, Diode → Phaser → EQ −300 Hz → OTT) ; pas de valeurs à reprendre.

### F08-24 Serum - Make Better Growls in 10 Minutes — Echo Sound Works, page ADSR Sounds (Serum, version non donnée ; date non donnée)
- Statut : page lue le 05/10/2026 (HTTP 200). La page ne contient qu'une phrase et la vidéo intégrée (`e6-sjJq57OY`), non visionnée.
- Gestes et réglages écrits : aucun. Texte intégral : « In this video Echo Sound Works shows you how to make better, richer sounding growls and bass sounds in Serum. »
- Conseils de jeu ou de mix : aucun.
- Limites : tout le contenu est dans la vidéo. Le titre exact, absent du registre, est désormais connu : « Serum - Make Better Growls in 10 Minutes ».
- Utilité pour une recette : nulle sans la vidéo ; corriger le titre dans le registre.

### F14-03 Hoover Bass Design With Serum — ADSR Sounds, auteur non nommé (Serum, version non donnée ; date non donnée, fichiers du projet datés de 2014)
- Statut : page lue le 05/10/2026 (HTTP 200). Vidéo intégrée (`gjZhxJgwM6U`) non visionnée.
- Gestes et réglages écrits :
  - Départ sur une wavetable maison « à frames riches en harmoniques », faite pour les hoovers.
  - Rappel historique : la Hoover (« Dominator ») est un preset du Roland Alpha Juno ; le son d'origine = **trois oscillateurs carrés empilés à l'octave**, forte modulation de largeur d'impulsion (PWM) et chorus. La page dit qu'on la recrée dans Serum « avec plusieurs astuces », sans les décrire.
  - Projet gratuit : `ADSR_SRM_DD_HOV.zip` (lien valide, 206 Ko). Contenu listé, non ouvert : un preset `.fxp`, une table `Table01.wav`, un `.mid`, un projet Ableton ; tous datés de novembre 2014, donc un preset Serum 1.
- Conseils de jeu ou de mix : aucun écrit.
- Limites : aucun réglage Serum dans le texte ; tout est dans la vidéo et le preset. À traduire dans Serum 2 si le preset est repris (fichier Serum 1).
- Utilité pour une recette : la définition d'origine (3 carrés à l'octave + PWM forte + chorus) sert de point de départ d'une hoover ; le preset gratuit est une piste à ouvrir sur le Mac.

### F01-08 How To Make Dubstep (UK/140) in 5 Easy Steps (2025) — Simon Haven, EDMProd (Serum, version non donnée ; 23 mai 2025, captures de 2022 et 2024)
- Statut : page lue le 05/10/2026 (HTTP 200).
- Gestes et réglages écrits, dans l'ordre :
  - Cadre : 140 BPM ; structure par blocs de 8 mesures (intro 8, build 8, drop 1A, 1B, 1C de 8 chacun) ; Mi mineur.
  - Batterie : kick en two-step, clap « sur chaque 3e temps » ; kick pas trop « boomy » car beaucoup de sub en dubstep.
  - Basse « Main Sub » dans Serum : départ « variation d'onde carrée » (table en image) ; filtre `MG Low 24` ; LFO 1 (preset de forme « Dome ») → cutoff du Filter A ; LFO 1 à **1/8 pointée**.
  - FM : osc B allumé, niveau **0**, Oct **+2** ; warp de l'osc A en `FM (FROM B)` ; `Random` à 0 sur les deux oscillateurs (contre les artefacts).
  - FX dans Serum : Hyper Dimension, Distortion, Comb Filter (valeurs en image, non lues). Dans Ableton : saturation, compression multibande, sidechain sur le kick.
  - EQ : coupes étroites entre 100 et 300 Hz (contre le kick et le clap) ; la zone 1–3 kHz est celle qu'on entend le plus : la relever si la basse ne passe pas, surtout sur petits haut-parleurs.
  - Macros : Macro 1 = cutoff Filter A ; Macro 2 = FM FROM B ; Macro 3 = Drive **et** Mix de la distorsion, le Mix en sens inverse (drive monte, mix descend) pour garder un volume à peu près constant. Puis automation des macros au fil du morceau.
  - Mid basses et fills : dupliquer la piste sub, Freeze + Flatten, traiter fort (distorsion Rift) et ne garder que des fragments en fondu, surtout en fin de phrase.
  - Build : kick sur chaque temps sans aigus, volume qui monte ; doubler après 4 mesures, redoubler après 2.
- Conseils de jeu ou de mix : moduler la basse dans le temps parce que le UK dubstep est minimal ; la macro drive/mix inversée pour comparer à niveau égal.
- Limites : version de Serum non écrite ; le vocabulaire (`MG Low 24`, forme « Dome ») et les captures de 2022 sont antérieurs à Serum 2 (déduction) : à traduire dans Serum 2. Table de départ, mélodie et valeurs des FX en image seulement. La « Main Sub » reçoit FM, distorsion et comb : ce n'est pas un sub pur, contraire à la séparation sub / médium demandée.
- Utilité pour une recette : le schéma de macros (cutoff / FM / drive + mix inversé) et la FM « osc B à niveau 0, +2 oct » se reprennent tels quels pour une basse médium à 140 BPM.

### F15-06 How To Make Liquid Drum & Bass: The Ultimate Guide (2025) — Aden Russell, EDMProd (Serum, version non donnée ; 23 mai 2025, captures d'octobre 2022)
- Statut : page lue le 05/10/2026 (HTTP 200).
- Gestes et réglages écrits, dans l'ordre :
  - Cadre : 165–175 BPM, 174 le plus courant ; 4/4 ; Fa mineur le plus fréquent, « les notes autour de F0 sonnent bien sur les systèmes club ».
  - Deux méthodes de basse : « additive » (formes simples + distorsion, FM, FX) ou « soustractive » (grosse basse DnB, passe-bas qui ne laisse presque que le sub) ; l'auteur préfère la soustractive.
  - Preset `BS PWM Sub` (pack de l'article) : carré modulé (PWM) + passe-bas ; réglages en image seulement.
  - Ligne : 4 mesures en Fa mineur (notes en image), dupliquée sur 16 ; une variation (« bass run ») toutes les deux phrases de 4 ; basse coupée 2 temps à la fin de la phrase de 16 ; fader −4 dB (−4,5 dB dans la liste de mix finale).
  - Arrangement : drop 1B sans batterie ni basse pendant ses 4 premières mesures ; automation de filtre sur la basse aux mesures 40 et 56 ; automation de la **Macro 2** du sub à la mesure 60 pour « un petit wobble » ; drop 1C : batterie et basse coupées sur les 2 dernières mesures.
  - Envoi de reverb dédié à la basse : grave coupé, assez brillant, envoi automatisé avec le balayage de filtre (réglages en image).
- Conseils de jeu ou de mix : en liquid, la basse tient plus à la composition qu'au sound design ; passe-haut sur les autres pistes pour laisser kick et sub ; grave du piano coupé contre le sub. Kick build 1/4 → 1/8 → 1/16 avec un gain qui **baisse** pour que le premier kick du drop frappe. Ghost notes −6 à −12 dB.
- Limites : aucun réglage Serum dans le texte (preset, macros, reverb de basse en image). Version de Serum non donnée ; captures de 2022 (Serum 1, déduction) : à traduire dans Serum 2.
- Utilité pour une recette : peu de sound design, mais des gestes d'arrangement de basse réutilisables (coupure de 2 temps en fin de 16, macro de wobble ponctuelle, reverb de basse sans grave).

### F14-09 The Baddadan Synth Bass Sound — Attack Magazine, auteur non nommé dans le texte (méta « ericadmin ») (pas Serum : u-he Zebra 2 ; 5 novembre 2024)
- Statut : page lue le 05/10/2026 (HTTP 200).
- Gestes et réglages écrits, dans l'ordre (unités de Zebra 2) :
  - 174 BPM ; motif MIDI fourni en image ou lecteur intégré, non lu.
  - Init ; GLOBAL : mode poly → **retrigger** (« une basse, pas de polyphonie »).
  - OSC1 saw, volume 32 ; OSC2 accordé **+7 demi-tons** (quinte), volume 32 ; OSC3 **+19 demi-tons** (octave + quinte), volume au maximum.
  - Quatrième oscillateur FMO1 dans une seconde voie, hors du filtre et de la saturation de la première : volume 0 (amené par enveloppe), FM à 10 « pour un léger tranchant » ; il donne un fondamental serré.
  - ENV1 (volume) : release ≈ 40.
  - VCF1 sous OSC1–3 : mode LP Vintage, cutoff ≈ 10 (presque fermé), drive ≈ 15.
  - ENV2 → cutoff VCF1, intensité ≈ 70 ; ENV2 attack ≈ 20 (« 9 heures »), sustain 0, release à midi.
  - Shape1 (distorsion) type Wedge, depth presque au maximum, Edge ≈ 30.
  - ENV3 → volume de FMO1, intensité maximale ; ENV3 attack ≈ 30 (gonflement puis chute rapide) ; bouton de volume de FMO1 à 0.
  - KeyFol → cutoff VCF1 ≈ 35 (filtre fermé dans le grave, plus ouvert dans l'aigu).
  - FX : EQ1 à la place de ModFX1, léger creux vers 225 Hz, légère bosse vers 3 kHz ; puis Drum Bus, Saturator et Limiter d'Ableton.
- Conseils de jeu ou de mix : résultat décrit comme une Reese « grasse », dans les médiums, qui cohabite avec un kick percutant et **un sub constant à part**.
- Limites : pas Serum ; la page dit seulement qu'un utilisateur de Serum ou Vital « peut reproduire » la démarche. Valeurs en échelle Zebra (0–100 ou position d'horloge), sans équivalent Serum donné. À traduire dans Serum 2 : empilement saw 0 / +7 / +19, oscillateur FM séparé hors distorsion, enveloppe de filtre à sustain 0, suivi de clavier ≈ 35 %. Effets natifs de Live en fin de chaîne (contraires à la règle 5 du projet).
- Utilité pour une recette : base d'une basse « horn » DnB : stack saw unisson + quinte + octave-quinte, filtre presque fermé ouvert par enveloppe, distorsion, fondamental FM séparé.

### Hors registre — Drum ‘n’ Bass Foghorn Bass With Wavetable — Adam Douglas, Attack Magazine (pas Serum : Wavetable d'Ableton ; 13 octobre 2021)
L'URL figure dans le registre (ligne 25, « Hors Serum mais transposable ») sans identifiant.
- Statut : page lue le 05/10/2026 (HTTP 200).
- Gestes et réglages écrits, dans l'ordre :
  - Note : F0 très grave. Osc 1 : table `Saw Dual 3`, position vers la moitié ; osc 2 et sub éteints (sub ajouté sur une piste à part, hors distorsion).
  - FM (effet d'oscillateur `Fm`) : tuning **100 %** (= modulant deux octaves au-dessus, selon la page), amount ≈ **30 %**. Astuce : moduler l'amount de FM par une enveloppe ou un LFO one-shot.
  - Filtre : pente 24 dB, cutoff ≈ **200 Hz**, résonance ≈ **25 %**.
  - Enveloppe d'amplitude : attack 0, decay **17 s** (écrit tel quel), sustain −inf dB, release **850 ms**, pente du decay 9 %.
  - Env 2 : attack **23 ms**, decay **4,2 s**, sustain 0, release 600 ms, pente −7 % ; Env 2 → Filter 1 Freq ≈ **30**.
  - Unison mode **Noise**, 3 voix, 30 % (valeurs par défaut conservées).
  - Env 2 → Osc 1 Pos = **15** (départ vers le carré).
  - Distorsion multibande (Waves MultiMod Rack) : grave = Abbey Road Saturator, mix plein, crossover ≈ 200 Hz ; médiums = MDMX Overdrive, gain au maximum, Temperature à 14 h, mix presque plein ; aigus = Abbey Road Saturator « à fond », crossover médium/aigu vers 2 kHz et quelques.
  - Compresseur de Live, preset Brute Compression ramené à seuil **−28,6 dB**, ratio **4,85:1**.
  - EQ Eight : retirer sub et grave, petite bosse vers **4,85 kHz**, étagère qui coupe le haut (place pour la batterie).
  - Largeur : StereoDelta (Mathew Lane) au maximum. Reverb : Valhalla Supermassive (preset SeaBeams modifié) en envoi, filtrée pour laisser passer l'aigu et pas le grave.
  - Fin : baisser un peu le cutoff ; essayer d'autres tables une fois la distorsion en place.
- Conseils de jeu ou de mix : dans le morceau, sinus de sub sur la même note, piste séparée.
- Limites : pas Serum. Le texte donne toutes les valeurs, mais les extraits audio ne sont pas écoutés. Decay de 17 s à vérifier (coquille possible, non tranchée). Les enveloppes « 23 ms / 4,2 s / −7 % » portent sur Wavetable ; la traduction Serum 2 reste à faire. Compresseur et EQ Eight natifs : contraires à la règle 5 du projet, à remplacer par des plug-ins tiers.
- Utilité pour une recette : recette foghorn complète et chiffrée (FM 30 % deux octaves au-dessus, LP24 200 Hz res 25 %, Env 2 → cutoff, distorsion par bandes avec grave peu saturé, sub à part) ; utile pour `bass-house-sound-design` (prototype Wavetable) et pour transposer dans Serum 2.

### F02-14 How to create a tearing neurofunk DnB Reese sound in Xfer Records Serum — Future Music, MusicRadar (Serum 1 d'après la date ; 27 juin 2017)
- Statut : page lue le 05/10/2026 (HTTP 200). Vidéo (lecteur JW) non visionnée.
- Gestes et réglages écrits, dans l'ordre (analyse du preset d'usine `Bs Reese Evolve`) :
  - Mono et Legato actifs, Portamento vers midi : glissés.
  - LFO 1 lent, **non synchronisé** → `WT Pos` de l'osc A (table « gnarly »).
  - Osc B sinus qui module l'amplitude de l'osc A via le warp de A en `AM (from B)` ; une enveloppe à attaque lente augmente ce warp au cours de chaque note (imite le changement de vitesse des wobbles old-school selon la note jouée).
  - FX : compression lourde **après** la reverb (le son gonfle entre les notes), distorsion forte, EQ, élargissement.
  - Oscillateur Noise poussé dans l'étage final de distorsion (le « fizz ») ; Sub oscillator pour le grave ; filtre de type double notch modulé.
  - LFO 1 en mode Off (libre) : chaque note a une modulation différente.
- Conseils de jeu ou de mix : imprimer plusieurs minutes d'un riff en audio et découper les meilleures prises.
- Limites : aucune valeur chiffrée sauf « portamento vers midi » ; détails des FX non écrits. À traduire dans Serum 2 (warp AM from B, mode de LFO, double notch : noms à vérifier). Sub dans le même patch, contraire à la séparation demandée.
- Utilité pour une recette : deux idées nettes pour une Reese : AM par sinus avec enveloppe lente sur le warp, LFO libre puis resampling et sélection des prises.

### F13-11 How to create a neurofunk bass sound in Xfer Records Serum — Computer Music, MusicRadar (Serum 1 d'après la date ; 26 juillet 2016)
- Statut : page lue le 05/10/2026 (HTTP 200). Vidéo non visionnée ; fichiers audio et zip mentionnés, non récupérés.
- Gestes et réglages écrits, dans l'ordre :
  - 174 BPM. MIDI `Bass.mid` : notes courtes une octave au-dessus des notes graves, reliées par portamento. `Mono` actif, Portamento **250 ms**.
  - Osc A : table `Basic_Mdc` ; RandPhase désactivé (écrit « Osc 1 ») pour une attaque identique à chaque note ; Sub oscillator actif, forme `RoundRect`.
  - `WT Pos` = **42** ; LFO 1 → WT Pos, amount **55** ; forme de LFO `Gunshot` ; durée **2 bar** ; `Trig` actif (redémarre à chaque note).
  - Sub : level **100 %**, LFO 1 → level du sub à **−40**.
  - Warp de l'osc A : `Mirror` ; Env 2 → warp à **+100** ; attack d'Env 2 = **1,7 s**.
  - Le traitement est renvoyé à « une autre étape » qui n'est pas sur la page.
- Conseils de jeu ou de mix : impossible d'obtenir une basse à la Noisia, Phace ou Mefjus directement du synthé sans traitement ni resampling ; partir de wavetable, FM ou distorsion de phase ; prévoir un grave solide et constant (sinus ou triangle mêlé, ou sinus séparé dessous) ; moduler position de table ou quantité de FM par LFO ou step sequencer ; modulation légère du cutoff ou de la résonance.
- Limites : article tronqué (6 étapes, pas de FX). À traduire dans Serum 2 (`Basic_Mdc`, `Gunshot`, `RoundRect`, `Mirror` : vérifier qu'ils existent sous ces noms). Incohérence de la page : « Osc A » et « Osc 1 » pour le même oscillateur. Sub dans le patch, avec une modulation de volume à −40 : contraire à un sub stable et séparé.
- Utilité pour une recette : valeurs exactes pour une source neuro (WT 42, LFO 55 sur 2 mesures retrig, Mirror + Env 2 +100 à 1,7 s, glide 250 ms).

### F08-03 Growl Bass Sound Design in Serum 2 for Drum and Bass — DNB Academy, via musicproductiontutorials.co.uk (Serum 2 ; page du 12 septembre 2026)
Titre YouTube d'origine : « How to Make a Heavy Growl Bass in Serum 2 for Drum & Bass » (vidéo `RmFDYc_8-9s`, 2 min 03 s, Ableton Live).
- Statut : page lue le 05/10/2026 (HTTP 200). Résumé écrit d'une vidéo, vidéo non visionnée.
- Gestes et réglages écrits (le résumé, sans valeurs) : oscillateur wavetable, distorsion de phase, distorsions rectify et overdrive, filtres comb et « fusion », LFO sur plusieurs paramètres ; deux oscillateurs superposés ; phaser et reverb à convolution de Serum 2 ; **soft clip en fin de chaîne** ; compression multibande, chorus pour la largeur, passe-haut. Index automatique de l'agrégateur (repères, non vérifiés) : distorsion 12–22 s, filtrage 25–30 s, LFO 33–40 s, overdrive 53–58 s, chorus 56–62 s, passe-haut 58–64 s, comb 60–68 s, phaser 79–86 s, convolution 87–96 s, compresseur 100–107 s, passe-bas 109–116 s, LFO 115–120 s, soft clip 118–120 s.
- Conseils de jeu ou de mix : aucun écrit.
- Limites : aucune valeur ; ordre des gestes déduit de l'index horodaté de l'agrégateur, pas de la vidéo.
- Utilité pour une recette : liste d'ingrédients Serum 2 pour un growl DnB (phase distortion, rectify, comb, fusion, soft clip final) à vérifier en vidéo ; aucune valeur exploitable.

### F06-14 Kanine Style Drum and Bass in Serum — Samstone, via musicproductiontutorials.co.uk (Serum, version non donnée ; 19 juillet 2024)
Titre YouTube d'origine : « MAKING KANINE STYLE DNB 🔥 SERUM DRUM AND BASS TUTORIAL » (vidéo `WqcUX7mKI_M`, 23 min 17 s, FL Studio).
- Statut : page lue le 05/10/2026 (HTTP 200). Résumé écrit d'une vidéo, vidéo non visionnée.
- Gestes et réglages écrits (le résumé, sans valeurs) : DnB lourde « à la Kanine », éléments mélodiques et jump up ; programmation de batterie ; basse multicouche dans Serum, FM et filtres résonants ; traitement de voix ; arrangement du build. Plug-ins listés : Saturation Knob, Trash, OTT, Serum, Pro-R, Little AlterBoy, Kickstart. Index automatique (non vérifié) : FM vers 373 s, LFO 394–405 s, phaser 453–465 s et 632–640 s, comb 603–610 s, sidechain 534–540 s et 722–728 s, layering 743–750 s, balayage de filtre 839–860 s.
- Conseils de jeu ou de mix : aucun écrit.
- Limites : aucune valeur ; version de Serum inconnue ; résumé généré par l'agrégateur.
- Utilité pour une recette : seulement une piste (basse multicouche FM + filtres résonants, OTT, Trash) ; rien à reprendre sans la vidéo.

### F10-03 How To Make A Riddim Bass In Serum — Academy.fm (titre et auteur d'après le registre ; page non lue)
- Statut : **échec**. `curl` : HTTP 530, corps « error code: 1016 » (erreur Cloudflare : le DNS de l'origine ne répond pas), deux essais. WebFetch : domaine bloqué par le proxy de sortie (EGRESS_BLOCKED). Pas d'autre tentative.
- Gestes et réglages écrits : non lus.
- Conseils de jeu ou de mix : non lus.
- Limites : rien n'est connu au-delà de l'extrait du registre (« riddim pas à pas avec un seul oscillateur »).
- Utilité pour une recette : aucune pour l'instant ; réessayer plus tard.

---

## Report dans le registre

Les statuts, le titre de F08-24 et l'échec de F10-03 sont reportés dans `tutoriels-a-consulter.md` (05/10/2026). La page foghorn d'Attack Magazine reste hors registre (synthé Wavetable d'Ableton), citée dans ses « Lacunes ».
