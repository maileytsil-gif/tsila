# Drones, effets et glitches : étude et atelier Serum 2 / Ableton Sampler

*Production House, Bass House, Future Rave, Tech House et Minimal · 28 septembre 2026.*

## 1. Résumé des recherches et limites

Serum 2 réunit oscillateurs wavetable, échantillon, granular et spectral : il peut prolonger une texture, la décomposer en grains et dissocier partiellement évolution temporelle et hauteur. Sampler de Live 12 joue un échantillon avec boucles de sustain et de release, modulation de début et de boucle, LFO, enveloppes et FM/AM ; c'est un outil formidable pour les microboucles, mais **ce n'est pas un moteur granulaire**. Pour un vrai nuage de grains natif Ableton, Granulator III constitue le complément adéquat, s'il est présent dans l'installation. Dans les recettes ci-dessous, les nombres sont des **points de départ à l'oreille**, pas des presets garantis ; les libellés et plages exactes doivent être vérifiés dans la version de Serum installée. Les formes d’onde par défaut de Serum, dont « Basic Shapes » et les simples sinus/scie prêts à l’emploi, ne sont pas privilégiées dans les recettes. Elles restent possibles si une fonction précise le justifie, mais la création part ici de sources originales, de tables importées et de transformations qui apportent une identité propre.

### Cartographie du design

| Objet | Temps | Hauteur | Répartition spatiale | Fonction musicale |
|---|---|---|---|---|
| Drone tonal | Continu, modulation lente | Fondamentale, quinte ou notes d'accord | Centre étroit pour fondamental ; largeur surtout dans les harmoniques | Ancre harmonique de break |
| Drone bruité | Long, impulsions irrégulières | Partiel ou atonal | Stéréo mouvante et filtrée | Attente, profondeur, tension |
| Riser | Évolution dirigée sur 4–16 mesures | Montée réelle ou brillance croissante | S'ouvre vers transition | Prépare le changement de section |
| Downlifter | Descente et dissipation | Chute de pitch ou filtre | Large puis disparition | Dégage le premier temps |
| Glitch | 1/32–1/4, ruptures ponctuelles | Pitch stable ou sauts contrôlés | Souvent placement ponctuel | Surprise, remplissage, ponctuation |

La hausse de hauteur et la hausse d'énergie aiguë sont **deux phénomènes différents** : ouvrir un filtre ne transpose pas la fondamentale. Utiliser un mouvement réellement ascendant si le riser doit annoncer la tonalité du drop.

### Palette de sources hors formes par défaut

| Besoin | Source de départ | Transformation utile |
|---|---|---|
| Drone tonal | Enregistrement de piano tenu, cordes, voix, carillon ou feedback accordé | Extraire une zone stable, Granular ou Spectral ; garder la fondamentale contrôlée |
| Texture industrielle | Frottement de métal, ventilation enregistrée, bruit mécanique autorisé | Sample/Granular, filtres et mouvements lents de position |
| Glitch organique | Consonne vocale, clic buccal, percussion maison | Découpage, microboucle, changement de départ, resampling |
| Riser signature | Souffle, papier, field recording ou queue d’impact personnelle | Densité, hauteur réelle, filtre et espace automatisés séparément |
| Wavetable unique | Table créée à partir d’un échantillon original ou transformée dans l’éditeur de tables de Serum | Parcours lent de table, distorsion contrôlée, comparaison avec la source brute |

Cette préférence ne signifie pas que les formes simples sont mauvaises : elles sont parfois idéales pour un sub pur ou pour une modulation. Pour les drones et les FX recherchés ici, partir systématiquement d’un preset par défaut ferait perdre l’identité des sources enregistrées.

## 2. Méthode d'enregistrement et préparation

1. Enregistrer 10–30 secondes d'une source originale : frottement métallique, souffle, verre frotté, moteur, phrase vocale autorisée ou queue de reverb d'un accord. Capturer du silence de part et d'autre, vérifier les droits du matériau utilisé. Un source riche mais non saturée offre plus de points à révéler.
2. Nettoyer clics indésirables, retirer un grave parasite, régler la fondamentale de l'accord si le matériau doit être tonal. Préserver aussi une copie brute pour resampling. Importer une version mono pour le centre et une stéréo pour les textures.
3. Fixer la fonction du son **avant** de programmer : drone sous voix, transition 8 mesures, fill de dernière demi-mesure ou effet d'impact. Garder des registres libres pour voix et basse.
4. Créer une version sèche, puis traiter en trois étages : mouvement interne, effets, arrangement. Resampler l'idée en audio pour éditer précisément son entrée et sa sortie.
5. Vérifier à volume faible, en mono, et en contexte avec kick, basse et voix ; éviter que la queue du drone masque le premier temps du drop.

## 3. Recettes Serum 2

### A. Drone harmonique sombre, break Future Rave en fa mineur

- **Source** : enregistrer un accord Fm joué au piano ou un bruit de corde grave accordé ; charger dans l'oscillateur **Granular**. Ne pas supposer qu'un preset d'usine impose la bonne hauteur : contrôler à l'oreille avec une note F2/F3.
- **Grains** : commencer par des grains suffisamment longs et recouvrants pour éviter un crépitement involontaire ; stabiliser la position sur la partie soutenue ; ajouter lent mouvement de position par LFO irrégulier à faible amplitude. Ajuster la densité avant d'ajouter unison pour limiter la charge CPU.
- **Couleur** : filtrer les aigus progressivement ; faire respirer le filtre sur 8 mesures avec faible modulation. Un second oscillateur **Sample ou Spectral** à partir d'une autre prise fournit la couche aérienne ; couper le grave de cette couche.
- **Enveloppe** : attaque de plusieurs centaines de millisecondes à quelques secondes, release contrôlée ; changer la note F→C ou F→Ab très rarement. Un drone à F/C donne la stabilité ; la tierce Ab clarifie le mode mineur, mais peut gêner si l'accord change.
- **Espace** : réverbération en envoi, decay long, retour filtré et automatisé ; delay discret. Garder le F grave centré, créer la largeur dans la couche haute. Exclure subgrave de la réverbération.
- **Arrangement** : installer de mesure 1 à 8 du break ; dans les deux dernières mesures, ouvrir le filtre ou densifier les grains ; couper ou réduire la queue juste avant le kick du drop. Exporter 8 ou 16 mesures en audio.
- **Contrôle** : écouter sans reverb ; si le son n'a pas d'identité, changer la source plutôt que compenser avec plus d'effets.

### B. Drone spectral gelé puis désaccordé

- Charger un fragment vocal tenu, un piano résonant ou un gong dans l'oscillateur **Spectral**. Choisir une zone où le contenu harmonique reste intéressant même étiré ; explorer le déplacement temporel lent et la transformation du spectre en suivant l'interface installée.
- Composer un bourdon F/C : la racine reste sur F tandis qu'une seconde couche se déplace jusqu'à C ; microvariation lente du timbre, pas de vibrato ample sur la fondamentale. Relever le volume des aigus seulement à l'approche du drop.
- Rééchantillonner deux versions, stable et tendue ; alterner plutôt que charger simultanément plusieurs couches spectrales coûteuses. Le mode spectral peut sonner artificiel : c'est intéressant pour effet, moins pour préserver une diction intelligible.

### C. Riser de 8 mesures à partir d'un bruit concret

- Granular de souffle/rail/feuille froissée ; point de départ sombre, filtre qui s'ouvre de mesures 1 à 7. Programmer densité et mouvement plus rapides à partir de mesure 5. Pour une **vraie montée**, augmenter progressivement la hauteur de l'oscillateur sur une étendue choisie à l'oreille et vérifier que l'arrivée sert la tonalité.
- Ajouter un layer distinct de bruit filtré ; éviter de doubler un sub grave. Automatiser largeur et send reverb à la hausse, puis muter ou gater la queue sur le quart ou huitième précédant le drop. Un impact court sur le premier temps remplace la masse du riser.
- Variantes : 4 mesures de tension légère pour Tech House ; 16 mesures avec étapes de densité toutes les 4 mesures pour Future Rave ; rendu audio puis reverse d'une portion pour accent final.

### D. Glitch robotique vocal en Serum

- Enregistrer une syllabe personnelle autorisée et l'importer dans Sample ou Granular. Jouer des événements courts sur 1/16 et 1/32, avec variation de position et un petit nombre de hauteurs musicales (F, Ab, C pour fa mineur). Rendre en audio et déplacer les attaques au besoin.
- Moduler position par séquence LFO synchronisée uniquement aux événements déclenchés ; utiliser une enveloppe brève avec attack très court **mais non nul si clics non désirés**. Les clics voulus peuvent être conservés dans une couche dédiée, filtrée.
- Parallèle : signal sec centré + retour delay ping-pong filtré. Automatiser la quantité de la couche stéréo, vérifier mono. Varier 3 paramètres au plus (position, hauteur, densité), sinon le motif perd sa signature.

### E. Impact hybride du drop

- Fabriquer trois couches distinctes : attaque 10–60 ms (transitoire métallique ou clap), corps court (note grave accordée), queue large (bruit réverbéré, filtré). Serum génère corps et queue via Sample/Granular ; Sampler peut déclencher l'attaque.
- Ajuster phase et timing en audio : le corps doit soutenir le kick sans faire monter inutilement le pic ; un impact accordé ne doit pas déformer la basse. Couper les fréquences graves de la queue. Version sèche DJ et version cinématique break possibles.

## 4. Recettes Ableton Sampler

### F. Drone continu en microboucle sans moteur granulaire

- Charger une note réelle soutenue ou une queue d'instrument. Dans **Sample**, définir Root Key ; isoler une région homogène puis activer **Sustain Loop**. Tester boucle avant/arrière et crossfade, activer Snap aux passages par zéro quand cela aide ; une boucle inaudible prime sur un chiffre précis.
- Enveloppe volume : attaque douce, release adaptée au break ; modulation lente de Loop Start (petite profondeur) et filtre avec l'un des trois LFO. Si la boucle se met à cliquer, réduire modulation, agrandir la région, déplacer bornes ou augmenter crossfade.
- Garder une seule source autour de la fondamentale ; pour texture haute, dupliquer Sampler en Rack, transposer ou filtrer la copie, appliquer chorus/réverbération seulement à cette branche. Mapper « tension » à filtre, niveau de la couche aiguë et send, avec plages limitées.

### G. Glitch contrôlé sur phrase ou break

- Charger une phrase, une percussion ou un fill dans Sampler ; découper plusieurs portions de l'échantillon par plages clavier ou velocity. Programmer le motif en MIDI : 1/8 initialement, 1/16 dans la dernière mesure, 1/32 uniquement en ponctuation. Les variations de vitesse et de silence font autant que les répétitions.
- LFO Sample & Hold vers Loop Start ou Sample Start, synchronisé, profondeur courte ; assigner variation de hauteur à quelques notes ponctuelles. Créer une voie avec boucle courte ; éviter la modulation aléatoire permanente sur chaque occurrence si la reconnaissance du motif importe.
- Après Sampler : **Beat Repeat** seulement dans le fill, puis **Erosion**, Delay/Echo ou Redux avec parcimonie ; resampler en audio et choisir les prises. Pour du découpage déclenché par tranches, **Simpler Slicing** est souvent plus rapide que Sampler.

### H. Reverse swell puis stutter

- Sampler peut inverser globalement la lecture. Choisir une cymbale, respiration ou queue de clap, activer Reverse et régler le début du swell. Rendre 2 mesures en audio, aligner la fin sur la dernière double croche avant l'impact.
- Dupliquer la dernière 1/8 sur deux ou quatre attaques de 1/32 ; appliquer des fades de quelques millisecondes lorsque les clics ne sont pas le but. Réduire le send reverb avant l'impact pour obtenir un vide net.

### I. Circuit resampling en trois générations

- Génération 1 : voix courte → Sampler microboucle. Génération 2 : traitement Roar ou saturateur modéré, filtre animé, reverb → enregistrer. Génération 3 : charger le résultat dans Serum Granular, moduler la position sur 8 mesures puis réenregistrer. Sélectionner les meilleurs fragments et supprimer le reste.
- Garder la source d'origine et le nom des rendus (`voix_Fm_g1`, `voix_Fm_g2`, etc.). Faire attention à la réverbération cumulée et au bruit de fond amplifié par les générations.

## 5. Construction dans le morceau

**Break 16 mesures Future Rave** : mesures 1–4 drone F/C + voix ; 5–8 ouverture lente et premiers fragments glitch ; 9–12 ajout d'un pulse 1/8 et riser ; 13–15 accélération vers 1/16, hauteurs restreintes et retrait progressif de la basse ; mesure 16 stutter court, demi-temps ou temps de silence, impact ; drop avec kick et basse lisibles. Le silence pré-drop peut être 1/8, 1/4 ou davantage selon phrase, sans recette fixe.

**Tech House / Minimal** : drone discret filtré sur fin de phrase de 8 mesures ; un fill glitch bien placé sur la dernière 1/2 mesure ; éviter un grand riser à chaque bloc. Le même bruit d'ambiance traité différemment sert d'identité tout le morceau.

**Bass House** : déplacer le glitch de la voix vers le rythme des silences du riff de basse ; 1/16 syncopées avec kick intact ; downlifter après premier coup du drop, plutôt qu'une longue queue sous tous les kicks.

## 6. Spatialisation, dynamique et livraison

- Distribuer par fonction : fondamental mono/centre, drone tonal plutôt en arrière, bruit et détails aigus potentiellement larges. Vérifier le corrélomètre et le mono pendant les effets de Haas, chorus et delay.
- Garder 30–80 Hz du kick et de la basse dégagé par filtrage des layers d'effets selon écoute ; ce sont des repères de région, pas une prescription de filtre à 80 Hz sur tout son. Les filtres à forte pente peuvent altérer transitoires et phase.
- Ne pas limiter le master pour rendre les FX impressionnants : égaliser niveau, couper la queue superflue, piloter send et dynamique sur la piste FX. Mesurer le pic de chaque transition et l'entrée du drop ; écouter codec streaming et système de club si disponible.
- Serum 2 Granular/Spectral, longs releases, polyphonie et unison peuvent coûter cher en CPU ; figer/resampler les longues textures pour sécuriser la session.

## 7. Parcours de cours et vidéos

| Niveau | Support accessible | Exercice concret |
|---|---|---|
| Bases Serum 2 | [Guide officiel Xfer](https://xferrecords.com/web-manual/serum-2/welcome) et [page de synthèse](https://xferrecords.com/web-manual/serum-2/exploring-sound-design-in-serum) | Importer une prise personnelle dans Sample puis Granular ; comparer continuité et mouvement. |
| Sampler en détail | [Manuel Ableton Live 12 : Sampler, section 31.10](https://www.ableton.com/en/manual/live-instrument-reference/) | Créer trois boucles sustain à partir de la même source, comparer les clics et les fondus. |
| Drone et pensée musicale | [Drone Lab et entretiens Ableton](https://www.ableton.com/en/blog/drone-lab-creating-sustained-sounds-in-live-11/) | Fabriquer 16 mesures de F/C qui n'empiètent pas sur la voix. |
| Vidéo granulaires | [Atelier Granulator III avec dnksaus](https://www.ableton.com/en/blog/sound-design-with-granulator-iii/) | Recréer le mouvement de position/glide avec Serum Granular ; comparer au moteur M4L. |
| Vidéo glitch rythmique | [Ned Rush : programmation complexe](https://www.ableton.com/en/blog/complex-drum-programming-with-ned-rush/) | Réaliser huit fills de fin de phrase avec Chance, modulation et Beat Repeat, garder les deux meilleurs. |
| Vidéo un seul échantillon | [Ned Rush : Drum Sampler](https://www.ableton.com/fr/blog/drum-sampler-exploring-live-121s-new-device-with-ned-rush/) | Tirer kick, snare, hats et son mélodique d'un vocal d'une seconde. |
| Vidéo FX en morceau | [Ableton/Side Brain : accords et FX](https://www.ableton.com/en/blog/step-by-step-guide-for-sub-bass-chords-and-fx/) | Intégrer un glitch dans une progression et réécouter le break entier. |

Les pages officielles, leurs descriptions et les sections du manuel ont été consultées. Les vidéos signalées sont des **supports recommandés** ; leurs démonstrations audio n'ont pas été visionnées/écoutées directement ici. Ne pas leur attribuer des réglages précis qu'elles n'exposent pas dans la description.

## 8. Atelier de validation, une heure

- 0–10 min : enregistrer trois sources et marquer leur hauteur éventuelle.
- 10–25 min : fabriquer drone Serum et variante Sampler de la même source ; comparer solo et dans break.
- 25–40 min : fabriquer riser et deux fills, rendre en audio ; choisir la meilleure prise.
- 40–50 min : monter 16 mesures break → drop avec retrait de la queue et impact.
- 50–60 min : mono, niveau égalisé, volume faible, contrôle grave, corriger une seule chose audible à la fois. Sauver presets et audio nommés.

**Critère de réussite** : identifier à l'aveugle l'intention du break et sentir l'impact du premier kick sans perte de basse, de voix ou de groove. Le plugin employé est secondaire par rapport à ce résultat.
