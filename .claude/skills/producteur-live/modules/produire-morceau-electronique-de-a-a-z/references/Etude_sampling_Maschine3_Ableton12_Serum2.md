# Étude pratique approfondie du sampling
## Maschine 3 · Ableton Live 12 Suite · Serum 2

*Version du 28 septembre 2026. Les valeurs chiffrées des recettes sont des points de départ créatifs, pas des réglages imposés par les fabricants. « Maschine 3 » désigne ici le logiciel, avec le contrôleur Maschine MK3 si disponible.*

## 1. Le sampling comme système de production

Une prise sonore devient une **source**, puis des **événements jouables**, puis une **matière transformable**. Garder les trois niveaux séparés évite de perdre le groove d'origine. Un même break peut fournir : kick/snare isolés, boucle fantôme, texture étirée, bruit de transition et attaque d'impact.

| Besoin | Outil conseillé | Geste central | Livrable |
|---|---|---|---|
| Jouer et réordonner un break aux pads | Maschine 3 Sample Editor → Slice | Détection de transitoires, correction manuelle et assignation | Pattern MIDI avec slices |
| Aligner un loop sur le morceau | Live clip audio, Warp | Repères sur vrais temps forts, choix du mode Warp à l'oreille | Boucle audio cohérente |
| Transformer un extrait en instrument | Simpler ou Sampler | Racine, enveloppe, filtre, zones | Instrument jouable |
| Créer une texture mouvante | Serum 2 Granular ou Spectral | Import d'un fichier audio, modulation de sa lecture | Riser, drone, vocal abstrait |
| Imprimer une transformation | Live Resampling ou enregistrement Maschine | Enregistrer le signal interne traité | Nouveau fichier audio autonome |
| Rythme interrompu en direct | Live Beat Repeat | Activer sur un passage précis, puis imprimer | Stutter reproductible |

**Vocabulaire essentiel.** Slicing : distribuer les morceaux d'un sample sur des notes/pads. Warp : relier temps audio et temps musical. Resampling : enregistrer une nouvelle version du son produit par le projet. Granular : recombiner de très petits fragments audio. Spectral : transformer une représentation fréquentielle du sample. Ces procédés peuvent se cumuler; leur ordre change le résultat.

## 2. Préparer et choisir les samples

1. Créer `Sources_originales`, `Découpes`, `Resamples`, `Exports` dans le dossier du projet; conserver l'original intact. Noms utiles : `source_role_tonalite_bpm_version.wav`, par exemple `voix_hey_Fm_126_v02.wav`.
2. Écouter le début, la fin, le bruit de fond et la queue de réverbération. Placer des fondus très courts sur les découpes si elles claquent. Pour un kick, ne pas gommer son attaque avec un fondu trop long.
3. Repérer la **fonction** avant de choisir l'outil : pulsation (kick), contretemps (hat), ponctuation (vocal), tension (riser), largeur (bruit), fondamentale (sub).
4. Travailler au volume comparable pour chaque version; juger aussi au sein de l'arrangement. Un son isolé impressionnant peut masquer la caisse claire ou le lead.
5. Noter provenance et autorisation d'utilisation si la source est externe. Un stem séparé ne rend pas automatiquement une œuvre libre d'utilisation.

### Trois routages fiables

**Maschine en plugin dans Live** : régler le tempo et la mesure dans Live; construire les slices/patterns dans Maschine; enregistrer le résultat par le routage audio de Live (ou exporter l'audio depuis Maschine puis importer dans Live). Vérifier la latence et la mesure 1 avant d'imprimer. Les sorties multiples de Maschine sont facultatives : elles demandent une configuration séparée.

**Fichier commun** : exporter un WAV propre depuis Maschine et le glisser dans Live ou Serum 2. Cela évite toute hypothèse sur le routage MIDI et les paramètres du plugin.

**Live vers Serum** : créer ou exporter une courte phrase audio dans Live, charger le fichier dans un oscillateur Sample, Granular ou Spectral de Serum 2; enregistrer ensuite Serum sur une piste audio via le routage ou le Resampling de Live. Les contrôles automatisables varient selon le format et la version du plugin : vérifier dans sa propre session.

## 3. Architecture d'un morceau d'essai

**Exemple de session : 126 BPM, Fa mineur, 4/4.** Une noire dure ≈ 476 ms; une croche ≈ 238 ms; une double croche ≈ 119 ms; une triple croche ≈ 60 ms. Ces durées servent à calibrer gates et tails; privilégier les valeurs synchronisées au tempo quand elles existent.

Groupes : `DRUMS` (kick, clap, hats, break), `BASS` (sub, mid), `MUSIC` (stab, lead), `TEXTURES` (vocal, ambiances), `TRANSITIONS` (riser, stutter, impact). Garder le kick et la fondamentale de basse centrés. Sur les transitions, élargir surtout le haut du spectre, puis vérifier la mono compatibilité.

## 4. Recettes approfondies

### A. Break découpé « garage nerveux » dans Maschine 3

**But :** faire respirer un drop Bass House sans superposer deux caisses claires identiques.

1. Choisir un break de 1 à 2 mesures dont le kick et le snare restent lisibles. Dans le Sample Editor, enregistrer/importer, ouvrir **Slice**, commencer par la détection des transitoires; corriger manuellement les faux déclenchements et les ghost notes ignorées; appliquer/exporter les slices vers des notes ou des Sounds.
2. Sur une mesure de 16 doubles croches, commencer par kick aux pas 1 et 9, snare aux pas 5 et 13; placer les petites slices de charleston/ghost autour des pas 4, 7, 12 et 15. Ne garder du break original que les coups qui ajoutent quelque chose au kick et au clap principaux.
3. Raccourcir individuellement les fins de slices si elles chevauchent la suivante. Pour des hats, essayer un décalage de quelques millisecondes et des vélocités alternées ≈ 60/95/70/105; conserver kick/snare forts et stables.
4. Dupliquer le pattern : A = groove sobre; B = variation de fin de phrase, avec répétition de snare aux deux dernières doubles croches ou silence au dernier contretemps. Sur une boucle de 4 mesures, réserver B à la quatrième.
5. Exporter/enregistrer le groupe de batterie; sous Live, filtrer les graves du break parallèle lorsqu'un kick et un sub dédiés prennent la place. Contrôler les transitoires et la phase à l'oreille en mono.

**Variante :** couper complètement les hats sur le premier temps du drop, les ramener au « et » du deuxième temps. Ce trou fait paraître le kick plus grand sans augmenter son niveau.

### B. Extraire le groove d'une percussion et l'appliquer sans écraser l'intention

**But :** transmettre les décalages du break à une ligne de hats et à des stabs.

1. Dans Live, aligner soigneusement un extrait de percussion sur 2 ou 4 mesures avec Warp. Choisir la portion dont les accents sont réguliers; éviter le passage avec fill exceptionnel.
2. **Extract Groove** depuis le clip vers le Groove Pool; appliquer ce groove à un nouveau clip MIDI de hats. Commencer avec un Timing modéré et Velocity plus marqué; les pourcentages exacts dépendent du sample : comparer 0 %, dosage moyen et fort. Pour l'audio, vérifier que Warp est activé.
3. Garder la grosse caisse et le sub calés; appliquer au besoin une quantité plus faible aux stabs qu'aux hats. Faire A/B à volume égal sur 8 mesures, pas sur un seul coup.
4. Si le groove paraît « ivre », réduire Timing, limiter les ghost notes ou choisir une extraction plus courte. Si le pattern paraît mécanique, introduire des accents différents avant d'ajouter du swing.

**Contrôle :** vérifier l'attaque commune kick/sub et les retards volontairement réservés aux éléments légers. Les réglages de groove changent la sensation du beat, pas sa signature rythmique.

### C. Riser organique à partir d'un son non musical dans Serum 2 Granular

**But :** construire 8 mesures de montée à partir d'un souffle, froissement ou vocal tenu.

1. Enregistrer 1–3 secondes de matière. Couper le silence initial et éviter une attaque déjà très forte. Charger ce WAV dans l'oscillateur **Granular** de Serum 2.
2. Jouer une note tenue dans la tonalité du morceau, puis parcourir les paramètres de position de lecture et de densité/taille de grain à l'oreille. La plage et les noms précis des commandes dépendent de l'interface; commencer par une texture lisse puis introduire progressivement plus de mouvement.
3. Automatiser dans Live ou moduler dans Serum : début filtré et discret, ouverture progressive du filtre pendant les mesures 1–6, montée de volume et éventuellement de hauteur surtout pendant 7–8. Ajouter une couche de bruit large à hautes fréquences, sans graves inutiles.
4. Enregistrer le résultat en audio. Faire un fondu entrant de 6–7 mesures; sur la dernière noire, raccourcir la fin du riser et laisser un trou de 1/8 à 1/4 de temps avant le drop si l'impact doit respirer.
5. Filtrer le bas de la texture jusqu'à ne plus gêner le sub. Vérifier que la stéréo se referme proprement dans le drop et qu'aucune queue de réverbération n'avale la première attaque.

**Variante forte :** imprimer trois versions : tonalité fixe, montée de hauteur, reverse. Utiliser une seule version principale et la seconde à bas niveau, pas trois risers au même volume.

### D. Riser spectral « voix vers métal » dans Serum 2

**But :** transformer un fragment vocal ou un accord en tension harmonique étrange.

1. Exporter une voyelle tenue ou un accord de 1–2 secondes avec une attaque douce. Charger le fichier dans l'oscillateur **Spectral** de Serum 2; vérifier la hauteur perçue et la note jouée.
2. Écouter d'abord sans effet et avec modulation neutre; chercher une région qui préserve l'identité du son. Moduler progressivement les contrôles de position/texture et le filtre durant 4 ou 8 mesures. Ajouter une distorsion ou une réverbération en parallèle seulement après avoir trouvé le mouvement spectral utile.
3. Pour renforcer la direction, rendre l'enveloppe plus brillante et augmenter légèrement le niveau sur les deux dernières mesures; sur la dernière double croche, couper le signal ou le figer puis imprimer en audio.
4. Laisser la basse du morceau fournir la note racine. Si le spectral produit des harmoniques ambiguës, filtrer son bas et vérifier la tonalité contre le lead.

**Attention :** le traitement spectral et l'étirement ne garantissent pas une hauteur perceptive stable sur toutes les sources; un bruit ou un accord complexe réclame une validation musicale à l'oreille.

### E. Stutter vocal contrôlé, trois niveaux d'intensité

**But :** annoncer un drop tout en gardant la phrase intelligible.

1. Prendre une syllabe nette (par exemple « hey »), nettoyer les clics et l'importer en audio Live ou en slice Maschine. Placer la syllabe une fois au début de la dernière mesure du break.
2. **Niveau 1 :** répétitions rythmiques manuelles en 1/8 sur le quatrième temps. **Niveau 2 :** 1/8 → 1/16 pendant les deux derniers temps. **Niveau 3 :** 1/8 → 1/16 → 1/32 sur le dernier demi-temps, avec baisse progressive du volume ou montée de hauteur. Ne pas garder une rafale 1/32 pendant toute la mesure.
3. Version Live : insérer **Beat Repeat** sur la piste ou un bus dédié, régler Grid à la valeur musicale désirée, choisir le comportement de sortie approprié, activer seulement sur la fin de transition, puis imprimer pour maîtriser exactement la répétition. Version manuelle : couper et dupliquer le segment audio sur la grille; vérifier les croisements et fondus.
4. Passer la dernière répétition dans un delay court ou une réverbération imprimée puis couper le sec un instant avant le kick. Si l'effet devient aigu et agressif, adoucir 3–8 kHz au cas par cas.

**Contrôle :** vérifier à faible volume que le rythme accélère réellement; si toutes les répétitions ont la même attaque et le même niveau, diminuer légèrement leur vélocité/volume en fin de phrase.

### F. Pont de 8 mesures : énergie suspendue et retour du groove

**But :** relier deux drops sans perdre le motif du morceau.

| Mesures | Action | Espace et spectre |
|---|---|---|
| 1–2 | Retirer kick et basse; conserver un fragment vocal ou stab reconnaissable | Élargir l'ambiance; couper le grave |
| 3–4 | Introduire une percussion découpée et un nouvel accord ou une variation du motif | Panoramique léger des textures, centre réservé |
| 5–6 | Rétablir l'impulsion par un kick filtré ou un tom, ajouter le riser | Monter graduellement médiums et niveau perçu |
| 7 | Doubler le rythme des hats, faire apparaître un snare roll discret | Réduire l'excès de largeur dans le bas |
| 8 | Stutter vocal, coupure brève, impact au retour | Silence partiel sur la fin; kick/sub nets au drop |

**Exécution :** resampler le stab du drop, inverser sa réverbération et placer cette queue avant le premier temps du pont; déclencher ensuite le motif d'origine en version filtrée. Éviter de monter tous les éléments simultanément : choisir un seul signal de montée principal, puis un signal rythmique secondaire.

### G. Impact « trois couches » entièrement resamplé

**But :** faire sentir le premier temps sans écraser le master.

1. **Corps** : kick ou tom grave accordé approximativement à la fondamentale, attaque rapide, queue courte; **attaque** : claquement/bruit bref; **air** : noise ou réverbération inversée/queue large.
2. Aligner les attaques de corps et claquement sur le premier temps; placer la couche d'air légèrement avant ou après selon sa fonction. Contrôler la polarité et l'annulation lorsque plusieurs couches graves coexistent.
3. Filtrer les graves de la couche d'air; raccourcir ou baisser le corps si le kick et le sub du drop jouent déjà. Grouper, équilibrer à volume de mix réel, imprimer puis comparer avant/après.
4. Garder un impact court pour chaque phrase et réserver la version longue à une transition majeure. Si le master réduit fortement son niveau au drop, retirer une couche avant de compresser davantage.

### H. Stab House original dérivé d'un sample vocal, sans Basic Shapes

**But :** obtenir un accord court, mordant et reconnaissable, sans oscillator « Basic Shapes ».

1. Enregistrer une voyelle ou un petit accord joué sur un instrument; charger dans **Serum 2 Sample** (ou **Granular** pour une attaque plus fragmentée). Régler la note racine à l'oreille ou via une information fiable dans le nom du fichier; jouer un accord mineur court, par exemple F3–A♭3–C4.
2. Enveloppe de départ : attaque 0–10 ms, decay 180–350 ms, sustain faible ou nul, release 80–180 ms. Ajuster selon le tempo et la place laissée au snare. Filtre passe haut ou passe bande selon le timbre : enlever le bas inutile sans rendre le stab maigre.
3. Ajouter saturation modérée, puis chorus/delay courts en parallèle. Garder une partie sèche au centre et une queue plus large sur les côtés; ne pas élargir une éventuelle fondamentale grave.
4. Pattern : accords courts sur les contretemps, une réponse décalée avant la quatrième mesure. Resampler chaque version, comparer tonalité, attaque et lisibilité contre la voix et les drums.

**Variante :** exporter une seule note de stab dans Simpler, créer les accords en MIDI et ajuster la durée par note. Cela rend les variations rythmiques plus rapides à programmer.

## 5. Diagnostic de mix et de rythme

| Symptôme | Cause probable | Test et correction |
|---|---|---|
| Break sans punch | Doubles transitoires kick/snare | Mute alterné des couches; recentrer les attaques |
| Loop qui « flotte » | Mauvais premier temps ou mauvais Warp | Écouter clic + loop sur 8 mesures; repositionner repères |
| Stutter brouillon | Fragments trop longs ou tails superposés | Réduire les queues, imprimer et éditer les répétitions |
| Riser qui masque le drop | Trop de bas, trop de réverbération en sortie | Filtrer bas, couper queue, ménager micro-silence |
| Groove absent malgré le swing | Vélocités plates, accents mal placés | Refaire les accents avant d'augmenter Timing |
| Sample de Serum faux | Racine ou harmonie de source incertaine | Jouer note seule contre fondamentale; retuner ou choisir autre source |
| Effet spectaculaire en solo, faible en mix | Conflit fréquentiel et temporalité | A/B à volume égal, retirer une couche concurrente |
| Basse affaiblie en mono | Graves latéraux ou couches déphasées | Écouter en mono; recentrer et simplifier le bas |

**Mesures comparatives utiles :** niveau perçu à volume égal; image stéréo et mono; énergie sub contre kick; dynamique de l'attaque; spectre avant et pendant le drop. SPAN ou l'analyseur d'EQ peuvent confirmer un masque, sans remplacer l'écoute. L'« analyse vectorielle » peut désigner ici la corrélation gauche/droite et le vectorscope stéréo : relever si le haut se diffuse tandis que le grave reste concentré, puis tester le repli mono. Ne pas déduire la qualité d'un seul nombre de corrélation.

## 6. Exercice complet en 45–90 minutes

1. Prélever trois sons : break 2 mesures, syllabe vocale courte, bruit/ambiance 2 secondes.
2. Trancher le break dans Maschine; créer A et B; transférer dans Live.
3. Extraire le groove du break dans Live; l'appliquer aux hats, partiellement aux stabs.
4. Construire un stab dans Serum 2 Sample et un riser avec le même enregistrement passé en Granular ou Spectral.
5. Arranger 8 mesures de break/pont et 8 mesures de drop; placer le stutter uniquement dans la dernière mesure du pont.
6. Imprimer séparément break, riser, stutter et impact. Couper toutes les pistes sources transformées pour vérifier que l'arrangement imprimé est autonome.
7. Faire trois écoutes : faible volume, mono, niveau normal. Comparer le premier temps du drop avec et sans impact.

**Critère de réussite :** reconnaître le motif d'origine, sentir une montée sur 8 mesures, entendre un drop clairement plus stable et plus dense, sans écrêtage audible ni perte de kick en mono.

## 7. Repères documentaires officiels

- Native Instruments, [manuel Maschine Software : sampling et sample mapping](https://docs.native-instruments.com/ni-tech-manuals/maschine-software-manual/en/index-en) et [manuel du contrôleur MK3 : sampling et slicing](https://docs.native-instruments.com/ni-tech-manuals/maschine-mk3-manual/en/sampling-and-sample-mapping). Vérifier les libellés selon l'écran logiciel/contrôleur.
- Ableton, [instruments Live 12 : Simpler/Sampler](https://www.ableton.com/en/manual/live-instrument-reference/), [routage et Resampling](https://www.ableton.com/en/manual/routing-and-i-o/), [Groove Pool et Extract Groove](https://www.ableton.com/en/manual/using-grooves/), [effets audio : Beat Repeat](https://www.ableton.com/en/manual/live-audio-effect-reference/).
- Xfer Records, [guide Serum 2 : sources Sample, Granular et Spectral](https://xferrecords.com/manual/serum-2) et [présentation officielle des moteurs](https://www.xferrecords.com/products/serum-2).

*Portée : synthèse documentaire et propositions de production; aucun projet audio ni vidéo de l'utilisateur n'a été fourni ou écouté pour cette étude. Les interfaces et libellés exacts sont à confirmer sur les versions installées.*
