# Harmonie, classes de hauteurs et transformations

## Choisir un modèle utile

- **Tonal fonctionnel** : distinguer fonction de repos, préparation et dominante ; suivre tonicisations, cadence et rythme harmonique.
- **Modal / pédale** : repérer le centre, les degrés caractéristiques et l'évolution au-dessus d'une basse tenue ; ne pas forcer une lecture dominante-tonique.
- **Non fonctionnel / chromatique** : décrire notes communes, mouvement des voix et collections de hauteurs avant de chercher un nom d'accord sophistiqué.
- **Hauteurs instables ou inharmoniques** : privilégier registre, densité et tension spectrale. Ne pas imposer une classe de hauteur exacte à un bruit ou une texture sans hauteur stable.

Les calculs modulo 12 ci-dessous supposent le tempérament égal à douze sons. Un sample désaccordé, un vibrato ou une intonation expressive demande une analyse en cents et des tolérances adaptées ; ne pas corriger automatiquement ce qui fait son caractère.

## Transposition et compatibilité

Coder les classes de hauteurs par C=0, C#=1, …, B=11. Pour un ensemble S, une transposition donne `T_n(S) = {(p+n) mod 12}`. Elle conserve la structure intervallique : un accord majeur transposé reste majeur.

Examiner les transpositions candidates selon : notes structurelles compatibles avec l'harmonie cible, conduite de la voix supérieure, basse existante, registre et artefacts. Une simple appartenance à la gamme ne garantit pas une bonne conduite des voix. Pondérer les notes selon leur durée, accent, position de phrase et statut de résolution ; ne pas traiter une note de passage comme une fondamentale tenue.

Pour les matériaux ambigus, un ensemble de classes décrit le contenu sans prétendre fixer sa fonction. Il perd cependant l'ordre, le registre et les doublures : conserver ces données séparément. Une proximité entre ensembles ne suffit pas à prédire la perception.

## Reharmoniser par la basse

Un même fragment peut changer de fonction au-dessus d'une autre basse, si le grave déjà imprimé et le contexte le permettent.

Exemple original : fragment E–G–B, sans basse grave dominante.
- Au-dessus de C : notes de Cmaj7, avec tierce E, quinte G et septième B.
- Au-dessus de A : quinte E, septième G et neuvième B ; compatible avec Am9 sans tierce, mais le caractère mineur ne peut pas être confirmé sans C ou contexte supplémentaire.
- Au-dessus de E : triade de Em.

Les notes du sample restent identiques ; la fonction change. Vérifier la basse réelle, les doublures et la résolution de B dans le contexte choisi. Ne pas présenter l'une de ces lectures comme certaine hors contexte.

## Conduite des voix et contrepoint harmonique

Suivre les hauteurs dans leur registre, pas seulement les noms d'accords. Chercher des notes communes et des déplacements courts quand l'intention est la continuité ; employer des sauts pour une rupture choisie. Contrôler croisements, parallélismes et espacements selon le style, sans interdire universellement les quintes parallèles.

Exemple de reconstruction : C–E–G → C–E–A produit Am/C avec deux notes communes ; seule G monte vers A. Cette opération n'est pas réalisable en transposant globalement un sample contenant C–E–G : elle exige une voix isolable, un autre sample ou une reconstruction.

Avec des fragments polyphoniques indivisibles, traiter la conduite des voix comme une contrainte de sélection entre prises et renversements disponibles. Ne pas prétendre piloter chaque note interne d'un fichier mixé.

## Emprunts, dominantes et modulation

- **Emprunt modal** : importer une couleur d'un mode parallèle avec une direction claire. En C majeur, F mineur introduit Ab ; une résolution Ab→G peut rendre le retour perceptible.
- **Dominante secondaire** : préparer une cible locale. En C majeur, D7→G introduit F# ; vérifier qu'une queue contenant F naturel ne crée pas un conflit involontaire.
- **Substitution tritonique**, si le langage convient : Db7 peut remplacer G7 vers C grâce aux notes guides enharmoniquement communes F et B/Cb. Contrôler les autres notes réellement présentes ; un sample chargé d'extensions n'est pas interchangeable automatiquement.
- **Modulation** : choisir un point d'arrivée puis une articulation par accord pivot, note commune ou rupture assumée. Une transposition passagère ne suffit pas à établir un nouveau centre ; la basse et la phrase doivent le rendre perceptible.

Une seconde mineure, un triton ou une extension tenue n'est pas une erreur en soi. Qualifier sa fonction, son registre et sa durée ; résoudre si le langage ou la demande le réclame.

## Transformations avancées du motif

Distinguer :
- **Transposition chromatique** : même intervalle pour toutes les notes.
- **Séquence diatonique** : déplacement de degrés pouvant modifier les intervalles ; nécessite souvent des notes isolées.
- **Renversement d'accord** : changement de la note à la basse, sans changer nécessairement les classes de hauteurs.
- **Inversion intervallique** : réflexion des hauteurs autour d'un axe. En classes, `I_n(p) = (n-p) mod 12` ; le registre doit ensuite être choisi.
- **Rétrograde** : ordre des événements inversé ; choisir explicitement ce qui arrive aux durées et aux silences.

Exemple calculé : C–E–G, soit {0,4,7}, sous I_7 donne {7,3,0}, soit les classes de C mineur. Cela décrit une transformation de partition, pas un réglage unique applicable à un accord audio mélangé. Employer ce modèle pour sélectionner ou reconstruire du matériau, pas pour promettre un traitement audio inexistant.

## Sources théoriques

- [Open Music Theory : ensembles et transformations](https://viva.pressbooks.pub/openmusictheory/chapter/pc-sets-normal-order-and-transformations/).
- [Open Music Theory : emprunts modaux](https://viva.pressbooks.pub/openmusictheory/chapter/modal-mixture/).
- Les exemples de notes ci-dessus sont des illustrations de travail ; vérifier leur réalisation dans le contexte réel.
