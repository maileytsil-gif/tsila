# Recettes de production House : hypothèses à vérifier à l'oreille

Chaque réglage ci-dessous est un **essai**, pas une plage validée par le fabricant. Lire « piste A → piste B » comme « A prioritaire, plugin sur B, clé A ». Commencer avec un seul plugin sur le problème et désactiver les traitements voisins pour un A/B valide.

| Situation | Routage et traitement de départ | Contrôle et échec typique |
|---|---|---|
| Kick → basse de drop Bass House | Resolve sur bus basse, clé kick ; Sidechain Content Kick, Follow SC On, Dynamic ; isoler les deux zones basses par crossovers, faibles à moyennes intensités. Tester un délai d'attaque court, relâchement musical calé sur la longueur réelle du kick. | Kick gagne en lisibilité sans effacer les notes. Si le mouvement de niveau est insuffisant, ajouter compression sidechain large bande ; si la fondamentale de basse devient instable, réduire Resolve et choisir une autre octave ou enveloppe. |
| Basse → kick grave trop résonnant | Soothe3 sur kick, Soft, profondeur limitée, bande basse ciblant seulement la queue résonante ; ralentir éventuellement l'attaque basse avec Attack Tilt ; Max cut pour protéger l'impact. | Delta ne doit pas emporter le clic ni la fondamentale voulue ; préférer raccourcir l'échantillon ou régler la hauteur si problème fixe. |
| Lead vocal → accord/pad Future Rave | Resolve sur bus accords ou reverb, clé voix ; Dynamic, Follow SC On ; limiter la réduction au corps et à l'intelligibilité réellement en conflit. Essayer M/S avec priorité au Mid seulement après vérification mono. | Les accords doivent revenir entre phrases ; si le pad creuse à chaque consonne, augmenter Attack ou réduire intensité/Precision. |
| Lead de drop rude vers 2–6 kHz | Soothe3 Soft sur lead ou bus, courbe autour de la dureté constatée, Detail modéré, Attack réglé pour préserver l'attaque. Comparer Equator Adaptive à la place, courbe centrée sur la zone gênante. | Delta contient seulement agressivité superflue, pas le caractère rave. Vérifier aussi oscillateur, FM, filtre, saturation et niveau du lead dans Serum 2. |
| Clap et hats dominent dans le drop | Soothe3 Soft sur bus percussions aiguës, limiter 4–12 kHz suivant écoute ; ou Equator Captured sur passage représentatif. | Écouter les attaques : si cymbales deviennent sifflantes ou mates, réduire la profondeur et travailler samples/velocity. |
| Break vers drop | Automatiser l'intensité du traitement du pad/FX lorsque la voix entre, la rendre au pré-drop, puis réévaluer sur le drop ; éviter les changements soudains de timbre sans intention. | A/B pendant 2–4 mesures avant et après transition, vérifier tail de reverb et remplissage spectral. |
| Tech House/Minimal basse et kick | Au besoin Resolve ciblé, faible intensité, comparer à un simple raccourcissement d'enveloppe et à un placement syncopé de notes. | Le groove ne doit pas devenir plat ; si le traitement suit chaque contretemps de manière audible, changer release ou arrangement. |
| Bus ou prémaster | Une seule correction douce soothe3 ou Equator seulement si résonance commune avérée, avec Max cut ou seuil prudent ; EQ tonal AQ seulement si cible artistiquement pertinente. | Bypass à niveau identique sur couplets, breaks et drops ; vérifier transitoires, grave mono, image M/S, crêtes et codec après export. |

## Références YouTube converties en WAV

Comparer d'abord architecture (kick/basse, centres d'énergie, densité, dynamique et largeur) et passages homologues ; niveler le volume perçu et contrôler les crêtes. Une conversion YouTube vers WAV ne recrée ni bandes perdues par compression avec pertes ni master sans altération ; ne pas entraîner AQ/Equator sur la courbe d'une référence compressée comme cible absolue. Pour streaming, tester le rendu après encodage et différents niveaux de lecture ; pour club, tester système puissant et compatibilité mono sans imposer une valeur LUFS universelle. Toujours produire les masters selon les contraintes effectives du distributeur/club demandées au moment de livraison.

## Diagnostic guidé

- Sonne mauvais en solo, varie selon la note → résonance mobile : soothe3 ; Equator si apprendre et modeler la courbe est plus intuitif.
- Sonne bien seul, disparaît quand l'autre joue → Resolve avec source prioritaire en clé ; éventuellement soothe3 sidechain si l'on vise expressément la résonance déclenchée.
- Semble sombre ou maigre tout le temps → AQ ou EQ manuel ; vérifier d'abord niveau et référence.
- Conflit entre fondamentales à chaque note → réécrire basse/accord, transposer, libérer le grave, contrôler phase ; aucun atténuateur spectral ne corrige une composition incohérente.
