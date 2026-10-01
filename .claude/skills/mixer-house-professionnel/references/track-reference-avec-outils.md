# Utiliser plusieurs titres de référence avec les outils possédés

## 1. Choix des titres

Demander si l'utilisateur a des fichiers obtenus légalement; ne pas télécharger des morceaux sans autorisation. Sélectionner idéalement 2–3 références correspondant chacune à une question distincte : **grave/groove**, **voix et médiums**, **break/drop/espace**. Prendre des versions comparables (club, radio, streaming ou pre-master) et noter leur provenance; des masters différents peuvent conduire à de mauvaises conclusions. Ne pas promettre que la cible doit copier chaque spectre.

## 2. Routage sûr dans Live 12

*Dans ce workflow*, le routage existe déjà : pistes → BUS → `BUS MASTER 1 → 2 → 3` → Main, et REF → Main hors limiteur (`../../mixage/SKILL.md` § Ordre de travail, étape 7) ; ne pas créer de groupe `MIX BUS` : son rôle est tenu par les BUS MASTER, et les pistes REF existantes servent de références. Méthode générale pour un autre projet : créer un groupe `MIX BUS` recevant **toutes les pistes et retours du morceau** qui doivent traverser le traitement du mix; vérifier les sorties de Maschine et les retours qui pourraient échapper au groupe. Mettre sur `MIX BUS` les traitements à comparer; router sa sortie vers `Main`. Créer des pistes audio `REF 1`, `REF 2`, `REF 3` directement vers `Main`, **sans passer par MIX BUS**. Sur `Main`, garder uniquement du monitoring commun aux deux chemins, idéalement aucun traitement qui modifierait la référence, et maintenir les niveaux de sortie sans clip. Utiliser Solo ou des boutons de mute pour basculer entre `MIX BUS` et une seule référence, jamais les jouer ensemble pendant l'A/B. Si le projet possède déjà une chaîne complexe sur `Main`, en conserver une copie et reconfigurer avec prudence pour éviter changement involontaire du mix; contrôler le routing dans [Ableton Mixing](https://www.ableton.com/en/manual/mixing/) et [Routing and I/O](https://www.ableton.com/en/manual/routing-and-i-o/).

**Gain matching.** Baisser le clip gain ou le fader de la référence masterisée afin que mix et référence semblent proches en intensité sur passages équivalents. Ne pas relever le mix uniquement pour rejoindre un master limité. Faire l'A/B très rapidement à volume d'écoute constant, puis revérifier à faible niveau. Si un meter LUFS fiable est installé, mesurer les passages choisis et noter l'écart; sinon utiliser les meters et l'oreille, sans inventer des chiffres. Le gain d'analyse n'est pas une correction du morceau.

## 3. Comparaisons ciblées

| Question | Passage à comparer | Outils possédés | Décision attendue |
|---|---|---|---|
| Kick/sub | 8–16 mesures de groove/drop similaires | Utility mono, SPAN, Pro-Q 4 pour observer le spectre | Durée et présence relative, pas copie d'une courbe |
| Bass mid / stab | Phrase avec motif comparable | Mute rapide des couches, Pro-Q 4 analyzers | Ajuster timbre/registre/temps, puis EQ local si besoin |
| Voix / lead | Refrains de densité comparable | Utility à faible volume, Pro-Q 4 sur pistes | Identifier les consonnes et fréquences réellement masquées |
| Break/drop | Dernières 4 mesures du break + premières 4 du drop | Clip markers Live, mesure de niveaux accessible, écoute | Contraste de densité et gestion des tails |
| Stéréo / mono | Même passage en stéréo et en mono | Utility, SPAN Mid/Side; outil de corrélation si effectivement possédé | Préserver le centre et les informations perdues en mono |

Placer un Pro-Q 4 sur `MIX BUS` et un autre sur chaque piste référence si l'on souhaite observer les spectres : son analyseur peut afficher un autre **spectre d'instance** dans la même interface, selon la [documentation FabFilter](https://www.fabfilter.com/help/pro-q/using/analyzer). Ne pas enclencher un EQ Match et appliquer automatiquement sa courbe au mix : considérer l'écart comme une question d'écoute; tenir compte de l'arrangement, du timbre et de la différence de loudness. SPAN offre des vues stéréo, mono et Mid/Side d'après [Voxengo](https://www.voxengo.com/product/span/). Utiliser des réglages d'analyse identiques, même longueur de passage et niveau comparable; lissage FFT et fenêtres peuvent changer l'image.

## 4. Outils et limites précis

- **Live Utility** : mono, largeur et niveau d'écoute. N'imprimer ni mono ni baisse de gain sur le fichier final sauf choix délibéré; placer Utility de monitoring en fin de chaîne, après les groupes, puis le neutraliser avant export si nécessaire.
- **FabFilter Pro-Q 4** : superposer un spectre externe d'une autre instance; observer masque potentiel. Utiliser EQ dynamique uniquement si le conflit varie selon les phrases; vérifier son routage sidechain s'il est externe.
- **FabFilter Pro-C 3** : comparer le comportement du sub ou de la reverb de lead lorsque kick/voix déclenchent le compresseur; surveiller la réduction réelle, pas le seul affichage de seuil.
- **SPAN** : regarder le contenu par bande et Mid/Side; ne pas lire un graphique comme une mesure de « qualité professionnelle ».
- **iZotope, soothe3, Waves, Valhalla** : n'utiliser un module que si sa version est présente. soothe3 pour une dureté variable démontrée, Valhalla pour profondeur et queues contrôlées, Waves si un traitement déjà présent a un rôle clair; iZotope selon les modules réellement installés.

## 5. Fiche de référence réutilisable

Pour chaque référence et pour **une section donnée**, noter : fichier/version, BPM approximatif vérifié, section, durée, niveau d'écoute de comparaison, priorité kick/basse, densité des bass mid, présence de voix, largeur ressentie, longueur des queues et une seule correction de mix à essayer. Ensuite écrire le résultat de l'A/B (« voix plus lisible », « kick trop long », etc.). Ne pas attribuer à la référence un plugin, preset, coupe d'EQ ou LUFS exact non mesuré.
