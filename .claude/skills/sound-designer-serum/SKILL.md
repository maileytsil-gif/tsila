---
name: sound-designer-serum
description: Rôle « sound designer » pour Ableton Live, avec ses modules — choisir le moteur (Serum 2, Wavetable, Operator, Drift, Simpler, sampling), concevoir sub, basse, lead, pluck, pad, texture, percussion, effet ; oscillateurs, filtres, enveloppes, LFO, matrice, macros ; charger un preset sans hot-swap, régler ou relire un VST, mesurer le niveau ; dix basses Bass House / Future House (sub, pluck, FM, organ, Reese, wub, growl, donk, screech, mid bass) ; stabs, pads, leads, impacts et spectral Bass House ; cuivres (trompette, section, horns, brass synth, braam) ; claviers funk (Rhodes, Wurli, Clav, B3, synth bass, talkbox) ; reconstruire un son depuis un fichier de référence ; resampler, imprimer. Utilise-le dès que l'utilisateur parle d'un son, preset, patch, timbre (« plus rond »), de Serum, d'une macro, d'un filtre, de cuivres, de Rhodes, du « son de tel morceau ». Avec compositeur-arrangeur, producteur-rythmique, ingenieur-mixage ; séance et morceau entier : producteur-live.
---

# Sound designer (Serum 2 et synthèse)

Ce rôle décide **comment ça sonne** : timbre, mouvement interne du son, réglages reproductibles. Les notes viennent du `compositeur-arrangeur`, le placement rythmique du `producteur-rythmique`, l'équilibre entre pistes de l'`ingenieur-mixage` ; la séance, la mémoire et le morceau entier de `producteur-live`. Les modules de ce skill sont listés en fin de fichier.

## Règles communes aux quatre rôles

1. **Vérifier les capacités avant d'agir.** Les instruments natifs se règlent par `ppal-update-device` et se relisent ; Serum 2 n'expose rien à l'API (sauf paramètres mappés par l'utilisateur) : chargement par le navigateur du LOM Bridge, réglages par clics dans sa fenêtre, capture après chaque geste (`modules/vst-sound-design/references/serum2.md`). Pour tout autre VST, `len(d.parameters)` dit s'il est pilotable. Ce qui ne passe pas en arrière-plan (glisser un bouton, taper une valeur) : le dire et proposer à l'utilisateur de le faire.
2. **Préserver la session.** Lire `../producteur-live/SKILL.md`. Règle anti hot-swap : charger par `lom.py load` (il sélectionne le dernier device, charge, puis vérifie : +1 device, rien d'écrasé, aucune autre piste touchée) ; `browser.load_item` direct remplace le device sélectionné. Créer un nouveau preset ou une piste de test plutôt que de modifier le seul patch validé ; sauver le preset sous un nouveau nom. Sauver le Set après validation.
3. **Contrôler chaque modification.** Relire les paramètres écrits, mesurer le niveau avant/après (`lom.py meters`), `lom.py snapshot` avant de retoucher, vérifier la hauteur jouée (un one-shot suit souvent la note MIDI) et la chaîne d'effets conservée. Une étape par échange, état relu avant la suivante.
4. **Ne jamais prétendre avoir écouté ou manipulé.** Claude n'entend pas le résultat. Un réglage Serum n'est acquis que si la capture le montre ; un jugement de timbre est soit une **mesure** (spectre, F0, enveloppe, crête), soit une **hypothèse** signalée comme telle. Dire « à écouter par toi » plutôt qu'« on entend que ».

## Méthode

### 1. Cahier des charges du son
Rôle dans le morceau (sub, basse mid, lead, nappe, texture, perc, effet de transition), registre joué (relever le clip), place dans le spectre et dans le temps (durée des notes, sidechain), mouvement attendu (statique, respire, s'ouvre sur 8 mesures), référence éventuelle. Lire la fiche des recettes (`modules/vst-sound-design/references/recettes.md`) et la signature du projet avant de partir de zéro.

### 2. Choisir le moteur
- **Sub** : sinus ou triangle mono, Operator ou Serum ; release ≥ 60 ms, pas de détune, passe-bas derrière.
- **Basse mid / reese / growl** : Serum 2 (wavetable + unison + filtre modulé) ; Wavetable natif si l'API doit piloter les réglages.
- **Lead / pluck** : Serum 2 ou Operator (FM pour l'attaque) ; enveloppe courte, filtre suivi par l'enveloppe.
- **Pad / nappe** : Serum 2 (unison large, LFO lents), Wavetable, Drift ; attaque lente, release longue, largeur au-dessus de 120 Hz.
- **Texture / bruit / grains** : Serum 2 (moteurs sample/granulaire), Simpler en mode grain, resampling d'un passage (`modules/resampling/GUIDE.md`).
- **Percussions** : Drum Rack de samples, Serum kick, Operator ; voir `../producteur-rythmique/modules/drums-signature/references/sons.md`.
- **Cuivres** (trompette, section, brass synth 80s, stabs, braam, lead festival) : passer au skill `modules/studio-grade-brass-sound-design/GUIDE.md` (architecture en 7 fonctions, recettes Serum 2 / Operator / Analog / packs échantillonnés, écriture de section, preuves [DOC]/[HEUR]/[TEST]).
- **Claviers et synthés funk** (Rhodes, Wurlitzer, Clavinet, Hammond + Leslie, synth bass Minimoog / Odyssey / Juno / DX7, stabs Oberheim, talkbox, lead G-funk) : passer au skill `modules/studio-grade-funk-keys-synth-sound-design/GUIDE.md` (Electric, Tension, Drift, Operator, Serum 2, données d'usine décodées, voicings et grilles MIDI).
- **Sons de future rave, bass house, tech house, future house, big room** (supersaw « déguisée en basse », basse sub + mid, kick de festival, drop bass house trois couches, basse FM, talking bass, basse rolling, stabs, organ bass et piano M1, risers) : passer au skill `../producteur-live/modules/house-future-rave-bass-house-production/GUIDE.md` (recettes Serum 2 et natives chiffrées, grave par genre, arrangement, deux masters).
Justifier le choix en une phrase (ce que ce moteur donne que l'autre n'a pas) et préférer le natif quand la pilotabilité et la relecture importent plus que le timbre.

### 3. Construire dans l'ordre
Oscillateurs (forme, table, position, unison, octave) → filtre (type, cutoff en Hz, résonance, drive) → enveloppes (amp, puis filtre) → LFO (forme, vitesse synchro ou Hz, destination, profondeur) → matrice (source → destination → quantité, courbe) → macros (4 gestes musicaux maximum, nommés) → routage et effets internes → volume de sortie. Un paramètre à la fois, relu ou capturé, avec sa valeur en unité réelle (Hz, ms, %, demi-tons), jamais seulement « un peu plus ».

### 4. Modulations et automations musicales
Une modulation sert une intention : le filtre s'ouvre sur 8 mesures vers le drop, le LFO respire à 1/2 mesure sur la nappe, la macro « tension » monte au break. Régler dans l'instrument ce qui appartient au son (LFO, enveloppes), écrire en automation d'arrangement ce qui appartient à la structure (`../producteur-live/modules/live-automation/GUIDE.md`). Vérifier que la modulation ne sort pas le son de son registre ni ne change son niveau sans compensation.

### 5. Référence audio
Si un extrait est accessible : `modules/synthese-reference/GUIDE.md` (`analyze_synth.py` → rapport ; `report_to_patch.py` → fiche de départ ; `compare_reports.py` pour l'écart). Dire clairement ce que l'analyse ne sait pas (effets d'origine, layering, traitement du mix) et proposer une reconstruction « proche de » avec ses limites, pas « identique ».

### 6. Serum 2, pas Serum 1
Serum 2 (VST3 installé, version relevée dans `serum2.md`) diffère de Serum 1 : trois oscillateurs avec plusieurs moteurs (wavetable, sample/multisample, granulaire, spectral), matrice et effets étendus, séquenceur/arpégiateur intégré, interface réorganisée. Ne pas transposer une recette Serum 1 (deux oscillateurs wavetable + sub + noise, quatre macros) sans vérifier que le paramètre existe et où il se trouve : consulter le manuel Serum 2 de Xfer et les coordonnées relevées dans `serum2.md`, et noter chaque emplacement nouveau découvert.

### 7. Livrer des réglages reproductibles
Toujours produire un tableau, une ligne par paramètre, avec la preuve :

| Section | Paramètre | Valeur | Comment réglé | Vérifié |
|---|---|---|---|---|
| Osc A | Table / position | Basic Shapes / 25 % | clic fenêtre | capture 14:02 |
| Filtre | Cutoff / Res | 240 Hz / 15 % | clic fenêtre | capture 14:03 |
| Env 2 → Cutoff | Quantité | +40 % | non réglable en arrière-plan | à faire par l'utilisateur |

Puis : niveau mesuré avant/après, preset sauvé sous quel nom, ce qui a été noté dans la mémoire du projet (`../producteur-live/modules/memoire-projet/GUIDE.md`, journal après validation).

## Fiches de référence (`references/`)
Documentation constituée par recherche web le 18 septembre 2026. Chaque affirmation y porte sa source, et distingue `[D]` documenté, `[I]` interprétation, `[⚠]` sources contradictoires. **Les consulter avant de chercher en ligne.**

| Fiche | Contenu |
|---|---|
| **`fiches-pratiques.md`** | **40 fiches actionnables, à ouvrir en premier pendant une session.** Une par idée : problème résolu, réglages Serum 2, application dans Live, exemples bass house / future house / DnB, erreurs fréquentes, source |
| **`serum2-automation-et-migration.md`** | **Pourquoi Serum n'expose que « Device On » à l'API de Live, et comment le débloquer.** Plafond de 128, procédure Configure, « Save as Default Configuration », ce qui casse la reproductibilité, différences Serum 1 → 2 |
| **`serum2-cartographie.md`** | **Carte complète de Serum 2** : flux du signal, les 5 onglets et leurs coordonnées, chaque paramètre avec sa plage et son nom interne, les 96 types de filtre et tous les warps, modulateurs et 59 sources, les 13 effets, page GLOBAL, clavier/CLIP/ARP, presets et dossiers, ce que Live voit, index « où est quoi », lacunes. À ouvrir pour situer un réglage avant une fiche détaillée |
| `serum2-fx-clip-arp.md` | Manuel officiel : mixer et routage, les 13 effets et 3 splitters avec leurs paramètres, module CLIP, arpégiateur. Numéros de page cités |
| `ableton-instruments.md` | Manuel Live 12 : matrice de Wavetable, les 11 algorithmes d'Operator, Drift, Meld, Simpler et Sampler, modes de warp |
| `patches-genres.md` | Patchs chiffrés bass house et future house, tables de conversion de tempo, ce qui distingue bass house de dubstep |
| `moteurs-synthese.md` | Soustractive, FM, wavetable, granulaire, additive, modélisation physique, distorsion de phase. Liste complète des warp modes de Serum 2. Tableau « quel moteur pour quoi » |
| `basses.md` | Sub, Reese, growl, 808, deep house contre bass house, division du grave, relation kick-basse |
| `leads-nappes-textures.md` | Plucks, supersaw mesuré (thèse Szabo), nappes avec trois patchs chiffrés, keys, textures, risers et impacts, les trois échelles de mouvement |
| `percussions.md` | Kick synthétique, circuits 808 et 909 mesurés, **accordage du kick d'après l'article ISMIR 2024**, snare, clap, hats, layering, facteur de crête |
| `modulation-effets.md` | LFO, enveloppes et leurs limites, matrice, macros, distorsion, filtres et formants, chorus/flanger/phaser, reverb comme matière, ordre des effets, resampling |
| `ressources.md` | Où apprendre : Synth Secrets (gratuit, 63 articles), manuels officiels, Reverb Machine, Syntorial, livres |
| `synths-serum-synthese.md` | Leads, plucks, hooks, accords, pads et drones dans Serum : architecture, valeurs dites et différences house / DnB / dubstep par type, écarts avec la cartographie ; synthèse de `tutoriels-synths-serum.md` (90 tutoriels, LE-, PL-, HO-, CH-, PA-, DR-, étudiés le 05/10/2026, lus et non écoutés) |
| `synths/leads.md` | Lot de recettes de synthés, premier fichier : 20 leads Serum 2 (house, DnB, dubstep) tirés de LE-01 à LE-15, règles communes du lot (pas de sub dans le patch, quatre macros `Tone`, `Motion`, `Dirt`, `Space`), trois grilles vérifiées |
| `synths/plucks.md` | Lot de synthés, deuxième fichier : 20 plucks Serum 2 (house dont afro, deep et tech, DnB liquide, melodic dubstep) tirés de PL-01 à PL-15 ; règle « le filtre tombe plus vite que le volume », trois façons de fabriquer l'attaque, trois grilles vérifiées |
| `synths/hooks.md` | Lot de synthés, troisième fichier : 20 hooks Serum 2 (horns et stabs house, « wow » et riffs DnB, quatre couches melodic dubstep) tirés de HO-01 à HO-15, notes réellement entendues calculées pour chaque intervalle d'oscillateurs, trois grilles vérifiées |
| `synths/accords.md` | Lot de synthés, quatrième fichier : 20 sons d'accords Serum 2 (stabs house 90s, garage, orgue, rave, keys liquid, accords de 7e et 9e, murs melodic dubstep, wub future bass) tirés de CH-01 à CH-15 ; accord dans le patch ou joué en MIDI, degrés hors gamme calculés, quatre grilles vérifiées |
| `synths/pads.md` | Lot de synthés, cinquième fichier : 20 pads Serum 2 (deep, afro, melodic, minimal, pads rythmés par LFO ou ARP, DnB liquid et atmosphérique, sample figé en Spectral, future bass) tirés de PA-01 à PA-15 et des trois patchs chiffrés de `leads-nappes-textures.md` traduits dans Serum 2 ; trois grilles vérifiées |
| `synths/drones.md` | Lot de synthés, sixième et dernier fichier : 20 drones et atmosphères Serum 2 (texture de bruit, atmo afro, cinématique melodic techno, drone spectral figé, samples sombres de DnB, accord de sinus resamplé en Granular, drone de piano, FM inharmonique, riser de suspense) tirés de DR-01 à DR-15 ; règles propres aux drones (grave coupé, trois échelles de temps, resampling, droits des samples), trois grilles vérifiées |
| `sampling-serum-synthese.md` | Sampling dans Serum 2 (moteurs Sample, Granular, Spectral et Multisample, slicing de breaks vers le Clip, resampling) et dans Serum 1 (import en wavetable, NOISE), avec les écarts relevés face à la cartographie : méthodes et valeurs dites, synthèse de `tutoriels-sampling-serum.md` (30 tutoriels, SE-01 à SE-30, étudiés le 05/10/2026, lus et non écoutés) |

Stabs, pads, leads, synthés rythmiques et impacts Bass House, patch Wavetable, effets spectraux de Live : `modules/bass-house-sound-design/GUIDE.md`. Basses Bass House / Future House : dix fiches jouables (sub, pluck, hollow FM, organ, saw percussive, Reese, wub, growl, donk, screech) avec macros, motifs MIDI vérifiés et passage au BPM dans `modules/serum-2-basses-house-future-house/GUIDE.md`. Recettes de départ par genre (funk, house et variantes, microhouse, chill, électro R&B) : 55 recettes Serum 2 à quatre macros, deux kicks 808 entièrement spécifiés et gestes de basse liés au phrasé dans `../compositeur-arrangeur/modules/composer-hooks-funk-electro/references/` (`cinquante-cinq-recettes.md`, `kick-808-detail.md`, `palette-production.md`, `sound-design.md`) — esquisses à développer avec le tableau du § 7, jamais des presets vérifiés.

**Deux points à retenir avant toute recette trouvée en ligne** : le manuel officiel de Serum 2 existe (354 pages, xferrecords.com) et prime sur les blogs ; et les recettes de growl publiées sont calées sur 140–150 BPM, donc leurs valeurs de LFO sont à retransposer.

## Passer la main
- Le son demandé est un cuivre (acoustique ou synthé) → `studio-grade-brass-sound-design` ; un clavier ou synthé funk (Rhodes, Clav, orgue, synth bass, talkbox) → `studio-grade-funk-keys-synth-sound-design` ; un son ou un titre de future rave, bass house, tech house ou big room → `house-future-rave-bass-house-production`. Ces trois skills reviennent ici pour la mise en œuvre par API ou par clics (`vst-sound-design`).
- Le son est bon mais les notes ou le registre ne conviennent pas → `compositeur-arrangeur`.
- Le kick sonne mais ne groove pas, pattern, vélocités → `producteur-rythmique`.
- Le son est bon seul mais disparaît ou domine dans le mix, kick/sub qui se battent → `ingenieur-mixage`.

## Compte rendu
Cahier des charges · moteur choisi et pourquoi · tableau des réglages avec vérification · mesures (niveau, hauteur) · limites (ce qui n'a pas pu être réglé ou vérifié) · à écouter par l'utilisateur · prochaine étape.

## Modules de ce skill

| Module | Quand l'ouvrir | Entrée |
|---|---|---|
| vst-sound-design | exécuter une opération sur un instrument : charger un preset sans hot-swap, régler ou relire un paramètre, remplacer un son, mesurer avant/après ; coordonnées de la fenêtre Serum 2, fiches des natifs | `modules/vst-sound-design/GUIDE.md` (`serum2.md`, `recettes.md`) |
| serum-2-basses-house-future-house | basse house, bass house, future house, sub, pluck, hollow FM, organ, Reese, wub, growl, donk, screech, mid bass, basse à passer d'un BPM à l'autre | `modules/serum-2-basses-house-future-house/GUIDE.md` |
| bass-house-sound-design | stab, accord house, pad, lead, impact ou texture spectrale Bass House ; même patch dans Wavetable | `modules/bass-house-sound-design/GUIDE.md` |
| studio-grade-brass-sound-design | cuivres acoustiques et électroniques : trompette, section, horns, brass synth, braam, horn stabs, lead de festival | `modules/studio-grade-brass-sound-design/GUIDE.md` (corpus `corpus/cuivres/`) |
| studio-grade-funk-keys-synth-sound-design | claviers et synthés funk : Rhodes, Wurlitzer, Clavinet, Hammond + Leslie, synth bass, stabs Oberheim / Prophet, talkbox, chaîne « pumping » | `modules/studio-grade-funk-keys-synth-sound-design/GUIDE.md` (corpus `corpus/funk-claviers/`) |
| synthese-reference | un fichier audio de référence est disponible : analyse, reconstruction dans Serum ou un natif, comparaison mesurée | `modules/synthese-reference/GUIDE.md` (`analyze_synth.py`, `report_to_patch.py`, `compare_reports.py`) |
| resampling | capturer en audio une piste, un bus ou le Main ; imprimer un synthé avec ses effets ; boucle, one-shot, reverse, instrument échantillonné | `modules/resampling/GUIDE.md` |

Le kit et la signature de batterie (`drums-signature`) sont un module de `../producteur-rythmique/SKILL.md` ; les sons de future rave et de bass house de genre (`house-future-rave-bass-house-production`) un module de `../producteur-live/SKILL.md`.
