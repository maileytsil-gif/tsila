# Reconstruction du patch

## Choisir un moteur
Quand le choix est libre, ces associations servent d'hypothèses de travail :

| Indices dominants | Moteur à essayer | Première famille de paramètres |
|---|---|---|
| Son soustractif simple, PWM, rondeur analogique | Drift / Analog, ou Serum avec ondes simples | Forme, accordage, filtre, enveloppes |
| Balayage de timbre, table évolutive, couches detunées | Serum ou Wavetable | Table/position, unisson, modulation de timbre |
| Cloche, basse FM, attaque métallique, partiels mobiles | Operator ou fonctions de modulation adaptées de Serum | Rapports, niveau des modulateurs, enveloppes |
| Texture dérivée d'audio, grain ou évolution spectrale complexe | Moteur approprié de Serum 2 | Mode choisi et transformation de la source |
| Reproduction par sample explicitement voulue | Simpler/Sampler ou moteur de sample disponible | Note racine, boucles, enveloppes et mapping |

Ce tableau oriente les essais, sans garantir que ces moteurs sont installés ni que l'architecture d'origine est la même. Vérifier l'édition de Live et les fonctions de l'instance. Le manuel Ableton décrit notamment les moteurs FM, soustractifs et wavetable, dont la disponibilité varie selon l'édition. [Instruments Live](https://www.ableton.com/en/manual/live-instrument-reference/).

## Patch de départ
Utiliser une note MIDI de référence, une durée et une vélocité constantes. Préserver la source et les automations de la piste cible. Initialiser seulement la nouvelle instance ou la copie de travail.

1. **Hauteur et amplitude** : octave, demi-tons/cents, niveau sans surcharge, mono/poly, longueur MIDI, attaque/decay/sustain/release. Éviter un clic ajouté par une enveloppe trop abrupte, sauf s'il fait partie du son voulu.
2. **Sources** : oscillateur principal puis, si nécessaire, sub, deuxième source, bruit/transitoire. Identifier la contribution de chaque couche ; ne pas multiplier les voix pour masquer un mauvais filtre.
3. **Filtre** : type, pente, cutoff, résonance, drive et key tracking présents. Ajuster l'enveloppe de filtre séparément de celle d'amplitude ; relever la quantité et la polarité de modulation.
4. **Mouvement** : detune/unisson, phase/retrigger, modulation de pitch, PWM/FM/position de table selon le moteur. Un LFO doit préciser sa destination, sa profondeur, sa forme, sa vitesse et son mode de redéclenchement.
5. **Jeu** : legato/glide, retrigger et réponses à la vélocité/MPE si nécessaires. Tester plusieurs notes avant d'ajouter l'espace final.

Les rapports, décibels, pourcentages et durées d'un synthé ne se transfèrent pas directement à un autre. Comparer le comportement obtenu plutôt qu'exiger les mêmes chiffres.

## Serum
Identifier Serum 1 ou Serum 2 et sa version. Les fonctions de sample, multisample, granulaire et spectrale documentées pour Serum 2 ne sont pas supposées présentes dans Serum 1. [Architecture Serum 2](https://xferrecords.com/web-manual/serum-2/welcome).

Pour un patch initial classique, utiliser d'abord une source simple, le filtre et l'enveloppe, puis construire les routages à partir de l'interface réelle. Vérifier dans la matrice les modulations ajoutées, leurs montants et les sources de jeu. Distinguer effets de l'oscillateur, effets internes et effets de piste pour éviter une double saturation ou une double reverb.

Une conversion d'audio en wavetable peut aider pour un son harmonique isolé. Dans le workflow documenté de Serum 2, un sample chargé peut être converti via « Switch to Wavetable » puis « Frequency Estimation ». Vérifier que ces options existent dans la version utilisée. Cette conversion ne reproduit pas automatiquement l'enveloppe, le filtre, les effets ou la jouabilité du son original ; les reconstruire et les tester séparément. [Conversion officielle](https://support.xferrecords.com/article/59-converting-samples-to-wavetables).

Pour une resynthèse ou un moteur granulaire/spectral, annoncer la méthode et contrôler stabilité de hauteur, durée et artefacts sur plusieurs notes. Ne pas employer silencieusement le sample original dans un résultat présenté comme un patch entièrement synthétisé.

## Natifs Ableton
Avec Operator, organiser les rôles porteur/modulateur et leurs enveloppes avant de complexifier l'algorithme. Avec Wavetable, ajuster d'abord la table et sa position, puis la modulation et l'unisson. Avec Drift/Analog, travailler formes, battements, filtre et enveloppes. Vérifier les noms et accès réels au lieu de supposer que chaque paramètre est exposé à un connecteur.

Pour une table personnelle dans Wavetable, consulter la procédure de la version installée et conserver la ressource importée avec le projet. [Wavetables personnelles](https://help.ableton.com/hc/en-us/articles/360002719179-User-Wavetables).
