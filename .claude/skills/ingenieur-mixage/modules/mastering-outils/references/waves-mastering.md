# Waves Audio : mastering

## Sélection et chargement
Les bundles listés dans l'inventaire ont été repérés dans les dossiers Waves V16 et V17. Confirmer la version effectivement chargée, le composant stéréo approprié et l'activation. Ne pas mélanger arbitrairement des versions dans un projet existant ni supprimer un WaveShell pour corriger un preset absent.

Le contrôle des paramètres dépend de l'hôte et du composant. Lire noms, plages et unités exposés ; ouvrir l'interface pour les autres commandes. Vérifier chaque valeur après réglage et sauvegarder le preset ou Set pertinent. Ne pas confondre présence du bundle et possibilité de pilotage automatisé.

## L4 Ultramaximizer : limitation finale

Choisir le mode selon le signal, puis régler Threshold et Ceiling. Release adapte le comportement temporel ; Clip change l'allocation de clipping. Ne pas imposer une valeur pour tout morceau. Vérifier Stereo Link, Oversampling et True Peak sur le composant chargé.

Utiliser Gain Match pour comparer le traitement à niveau compensé. **Dans le manuel consulté, Gain Match désactive Ceiling et retire la compensation de gain de sortie** : le quitter et revérifier les réglages de sortie avant l'export. Désactiver Delta pour la livraison. Coordonner le dithering avec l'export ; mesurer le fichier final indépendamment du plafond. Upward Compression modifie les passages plus faibles : l'évaluer sur l'ensemble de la dynamique du morceau, sans l'activer systématiquement. [Manuel L4](https://assets.wavescdn.com/pdf/plugins/l4-ultramaximizer.pdf).

## L1, L2, L3 et L3-16 : choisir le comportement

L2 est une option de limitation large bande ; L3 Multimaximizer travaille en multibande. Une modification des priorités de bandes peut aussi changer l'équilibre spectral. Vérifier la variante exacte (Ultra, Multi, LL, 16) avant de chercher un contrôle ou d'appliquer une recette. Ne pas attribuer automatiquement les fonctions True Peak et LUFS de L4 aux anciennes générations. [L2](https://www.waves.com/1lib/pdf/plugins/l2-ultramaximizer.pdf), [L3 Multimaximizer](https://www.waves.com/plugins/l3-multimaximizer).

Comparer une seule solution de limitation à la fois, à volume cohérent. Cumuler L2, L3 et L4 n'est pas une chaîne par défaut. Le choix d'une ancienne version reste valable si son caractère est souhaité, mais le plafond final doit être contrôlé par une mesure appropriée.

## WLM / WLM Plus : mesure et correction

Pour une **analyse seule**, vérifier le chemin final, le mode de mesure, les canaux et le suivi du transport. Remettre les mesures à zéro et lire le morceau entier, puis relever Long Term, Range et True Peak. Confirmer que le compteur a couvert la durée attendue.

**WLM Plus peut traiter le signal** : son Gain agit avant les mesures, Trim applique une correction et son limiteur true peak peut être actif. Pour mesurer l'état original, laisser Gain à 0, ne pas appliquer Trim et désactiver ce limiteur. Si WLM Plus est choisi comme étage de correction, expliciter son rôle ; le seuil du limiteur dépend de True Peak Max, puis une nouvelle mesure complète est nécessaire. Vérifier indépendamment le fichier exporté. [Manuel WLM/WLM Plus](https://www.waves.com/1lib/pdf/plugins/wlm-plus-loudness-meter.pdf).

Ne pas utiliser PAZ ou un simple affichage de crête comme substitut présumé à la mesure LUFS/true peak.

## Abbey Road TG Mastering Chain : tonalité et caractère

Examiner les modules chargés, leur ordre et les états de bypass. Régler l'entrée avant de juger la couleur, puis les corrections tonales et le comportement dynamique. Vérifier stéréo, sorties et variantes live/standard selon le manuel.

Le mode **Limit** du module dynamique ne constitue pas un limiteur brickwall : des transitoires peuvent passer. Ne pas lui confier à lui seul la garantie d'un plafond final. Si un plafond est nécessaire, prévoir une limitation finale appropriée puis mesurer le rendu. [Manuel TG Mastering Chain](https://assets.wavescdn.com/pdf/plugins/abbey-road-tg-mastering-chain.pdf).

## F6, Q10, Renaissance EQ, Linear Phase EQ

Choisir l'EQ selon la correction nécessaire, pas le nombre de bandes. Dans F6, distinguer gain statique et Range dynamique ; vérifier fréquence, Q, Threshold, Attack, Release et affectation stéréo/M/S. Commencer avec la quantité minimale utile et écouter les passages où la réduction intervient. Un sidechain externe doit être routé et justifié ; ne pas le supposer actif. [Manuel F6](https://www.waves.com/1lib/pdf/plugins/f6.pdf).

Pour Q10 ou Renaissance EQ, confirmer la variante et les bandes actives. Pour LinEQ, consulter son aide et vérifier latence, transitoires et besoin réel de phase linéaire. Ne pas ajouter systématiquement un filtre extrême au grave ou à l'aigu. Après correction, compenser le gain de comparaison et vérifier la mono.

## LinMB, C4, C6 : dynamique par zones

Utiliser une dynamique multibande quand le comportement varie selon la zone fréquentielle. Lire croisements, bandes ciblées, seuils, plages et temps disponibles. Vérifier le signal recombiné autant que les bandes en solo, sans changer toutes les zones pour uniformiser la courbe de réduction. LinMB dispose de croisements à phase linéaire ; ce choix ne dispense pas de contrôler les transitoires et la latence. [Manuel LinMB](https://assets.wavescdn.com/pdf/plugins/linear-phase-multiband-compressor.pdf).

Ne pas confondre compression multibande et limitation de crête finale. Une EQ dynamique plus simple peut suffire pour un seul problème localisé.

## API-2500, SSLComp, PuigChild : compression de caractère

Sur API-2500, vérifier Ratio, Attack, Release, Knee, Thrust, type Old/New et sortie réellement disponibles. Ajuster la détection en fonction du grave et vérifier le gain automatique lors de l'A/B. Lier suffisamment les canaux selon le comportement stéréo recherché. [Guide Waves API-2500](https://www.waves.com/how-to-use-api-2500-compressor-plugin-like-a-pro).

SSLComp et PuigChild sont des alternatives lorsque leur caractère sert le programme. Avant réglage, lire le manuel du composant sélectionné et ne pas transposer les unités ou les positions de boutons d'API-2500. Aucun ratio ou nombre de décibels de réduction n'est obligatoire pour un master.

## Curves AQ / Equator / Resolve

Curves AQ propose une correction d'EQ assistée ; Equator cible notamment les résonances. Vérifier la fonction d'apprentissage, le passage analysé et les quantités appliquées, puis comparer les autres sections. Une suggestion automatique peut corriger un symptôme sans respecter l'intention du mix. [Curves AQ](https://www.waves.com/plugins/curves-aq), [Curves Equator](https://www.waves.com/plugins/curves-equator).

Curves Resolve a été repéré comme bundle. Vérifier son manuel et les contrôles de la version avant usage : ne pas lui attribuer ceux d'AQ ou d'Equator. Éviter d'empiler Curves, soothe3 et EQ spectrale pour le même défaut sans identifier un besoin distinct.

## J37, Kramer Tape, PuigTec, S1 et Center

Employer la couleur ou la largeur seulement si elle améliore le morceau. Vérifier les fonctions exactes dans l'aide intégrée avant action. Pour les traitements de bande, contrôler entrée, sortie, bruit et modulation disponibles : ce qui enrichit une piste peut dégrader un master. Pour PuigTec, vérifier que la correction conserve grave et présence.

Avec S1 ou Center, lire la matrice et les paramètres du composant actuel ; évaluer équilibre gauche/droite, centre, corrélation et mono. Éviter de modifier automatiquement la largeur de toute la bande pour résoudre un seul élément du mix.

## Exemples de chaînes Waves à adapter

- **Correction ciblée** : F6 si nécessaire → L4 → WLM en mesure seule.
- **Couleur** : TG Mastering Chain si utile → limitation finale appropriée → WLM en mesure seule.
- **Dynamique par zones** : LinMB ou C6 si justifié → limiteur choisi → mesure finale.

Ce sont des organisations possibles, pas des presets ni des chaînes à charger entièrement. Vérifier aussi les mesures du fichier exporté, après tout traitement et conversion.
