# Rythme, contrepoint et forme à partir de fragments

## Trois couches temporelles

Distinguer grille métrique, rythme des événements et microtiming d'interprétation. Un sample porte son propre placement interne ; décaler son déclenchement déplace l'ensemble sans corriger les attaques internes.

Identifier temps forts, contretemps, anacrouses et accents hérités avant de découper. Conserver certains écarts expressifs ; ne pas cumuler aveuglément swing du sample, groove appliqué et notes MIDI décalées. Une vélocité MIDI ne change le niveau ou le timbre que si le sampleur est réglé pour y répondre.

## Procédés et calculs

- **Rotation** : déplacer cycliquement une cellule, en conservant son contour rythmique ; vérifier où tombent ses accents dans la mesure.
- **Augmentation / diminution** : multiplier / diviser durées et intervalles entre attaques. Préciser si les samples eux-mêmes sont étirés ou si seuls leurs déclenchements changent.
- **Groupement additif** : 3+3+2 croches remplit huit croches ; il peut fonctionner dans une mesure de 4/4 sans changement de métrique.
- **Polyrythmie 3:2** : trois attaques régulièrement espacées contre deux sur une même durée D. Positions : {0,D/3,2D/3} et {0,D/2}. Si D vaut une blanche, cela oppose un triolet de noires à deux noires.
- **Cycles de longueurs différentes** : un motif de cinq doubles croches contre un cycle de seize se réaligne après PPCM(5,16)=80 doubles croches, soit cinq mesures de 4/4. Parler de cycles asynchrones ; réserver « polymétrie » aux couches avec organisations métriques distinctes.

Les unités doivent être exactes et explicites. Une répétition tous les trois pas n'est pas automatiquement un triolet. Des cycles indépendants ne doivent pas produire un raccord accidentel : prévoir leur réinitialisation ou laisser leur déphasage se poursuivre intentionnellement.

## Contrepoint de fragments

Faire dialoguer des gestes : une attaque courte peut répondre à une queue longue ; un motif ascendant peut recevoir une réponse descendante ; une voix dense peut laisser place à une cellule espacée.

Choisir une hiérarchie entre voix principale et secondaire. Vérifier les accords réellement produits lorsque leurs samples se chevauchent. Une ligne indépendante rythmiquement peut rester incompatible harmoniquement ; inversement, une harmonie compatible peut être illisible par surcharge d'attaques ou de registre.

Pour un canon, préciser délai d'entrée, transposition et durée de chevauchement. Calculer les simultanéités aux attaques et aux changements d'accords. Le simple décalage d'une boucle entière n'assure pas un contrepoint cohérent.

## Développement motivique et forme

Conserver un invariant reconnaissable : cellule d'intervalles, dessin d'accents, syllabe, attaque ou contour. Faire évoluer une ou deux dimensions à la fois quand la lisibilité est recherchée. Pour une esthétique fragmentaire, choisir plutôt des contrastes explicites et des points de retour.

Construire la tension avec plusieurs moyens possibles : raccourcir les fragments, rapprocher les attaques, déplacer le registre, densifier les chevauchements, accélérer le rythme harmonique ou retarder la résolution. Ne pas confondre tension musicale et volume.

Exemple de trajectoire, à adapter :
1. Exposer une phrase et ses silences.
2. Répondre avec un autre ordre des mêmes fragments.
3. Développer par séquence ou déplacement d'accent.
4. Fragmenter et accroître la tension.
5. Revenir au noyau avec une basse ou une texture renouvelée.

Aucune obligation de quatre ou huit mesures par étape. Relever l'hypermètre, c'est-à-dire les appuis à l'échelle des groupes de mesures, si cela aide à placer attente, rupture et retour.

## Timbre et resampling comme orchestration

Attribuer les rôles avant de superposer : attaque, corps harmonique, réponse, texture ou transition. Une nappe granulaire peut prolonger la couleur d'un fragment sans en conserver une hauteur stable ; la vérifier avant de la compter comme accord.

Le repitch modifie rythme et spectre ensemble lorsque le Warp est désactivé ; l'étirement permet d'autres relations mais peut transformer les attaques. Choisir les artefacts pour leur effet perceptible, pas pour cocher une technique.

Créer éventuellement une génération de resampling après une transformation utile, puis sélectionner les passages qui servent la composition. Garder la source et le rendu précédent ; contrôler les queues, l'accordage et le gain à chaque génération. Appliquer le skill resampling pour la capture effective.

## Vérification musicale

- Le motif reste-t-il identifiable lorsqu'il doit l'être ?
- Les accents internes s'accordent-ils avec le placement des déclenchements ?
- Les notes qui débordent créent-elles une tension voulue ?
- Les cycles se rejoignent-ils à l'endroit calculé ?
- La section évolue-t-elle autrement que par ajout de couches ?

Utiliser ces questions pour corriger le résultat, sans imposer leur restitution sous forme de checklist à l'utilisateur.

## Sources

- [Ableton : boucles asynchrones](https://makingmusic.ableton.com/asynchronous-or-polyrhythmic-loops), pour les cycles et leur déphasage. La terminologie métrique peut varier ; ce skill explicite toujours les durées et subdivisions.
- [Ableton : instruments et sampleurs](https://www.ableton.com/en/manual/live-instrument-reference/), pour vérifier les fonctions présentes dans l'instrument utilisé.
