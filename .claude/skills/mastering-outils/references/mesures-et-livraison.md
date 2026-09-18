# Mesure, comparaison et export

## Avant/après
Mesurer source et master avec la même méthode, la même étendue et des paramètres comparables. Pour l'écoute A/B, compenser le niveau sans modifier le fichier original et éviter une double lecture. Distinguer une comparaison de passages similaires d'une mesure de sonie intégrée sur le morceau entier.

## Chiffres
- **Sample peak en dBFS** : crête des échantillons stockés.
- **True peak en dBTP** : estimation des crêtes du signal reconstruit ; elle nécessite un mesureur adapté.
- **LUFS intégrés** : sonie mesurée sur l'ensemble du programme, avec le mode de mesure documenté.
- **Short-term / momentary** : suivi des variations de sonie sur leurs fenêtres d'analyse.
- **LRA** : variation de sonie ; cette valeur ne certifie pas à elle seule le punch ou la qualité de la compression.

Fixer les objectifs selon la destination demandée et vérifier ses spécifications actuelles lorsqu'elles conditionnent la livraison. Sans destination précisée, expliquer le compromis de sonie retenu et préserver la dynamique pertinente. Ne pas annoncer un standard streaming universel.

Les sondages de vu-mètres dans Live peuvent manquer des crêtes et mesurer à un autre endroit que la sortie finale. Un plafond de limiteur n'est pas une mesure du rendu ; analyser le fichier livré. Un compte d'échantillons proches de 0 dBFS ne démontre pas à lui seul un écrêtage. Ne pas convertir l'original en 16 bits pour en certifier les crêtes.

## Analyse de fichier avec FFmpeg, si disponible

Vérifier que FFmpeg est réellement accessible dans l'environnement de Claude et que son filtre ebur128 supporte les options utilisées. La commande suivante lit le fichier sans produire une version audio traitée :

```sh
ffmpeg -hide_banner -nostats -i '/chemin/master.wav' -map 0:a:0 -af 'ebur128=peak=true' -f null -
```

Lire le résumé final et contrôler que l'analyse a couvert le fichier entier sans erreur. Ne pas assimiler une valeur limite de mesure sur du silence à une sonie musicale exploitable. En l'absence de FFmpeg, utiliser un autre mesureur adapté disponible ou indiquer les données non mesurées. Ce skill n'inclut pas le binaire FFmpeg. [Documentation du filtre ebur128](https://www.ffmpeg.org/ffmpeg-filters.html#ebur128).

## Export
Vérifier source de rendu, bornes et queues d'effets. La référence doit être exclue. Conserver la fréquence du projet sauf raison de conversion ; choisir la résolution selon l'usage. Pour un WAV d'écoute sans autre spécification, 24 bits sans normalisation est un point de départ, pas une norme universelle. Les intermédiaires flottants peuvent être préférables pour poursuivre le travail.

Si un dithering est nécessaire lors de la conversion finale vers un PCM entier, le coordonner avec le limiteur et l'export afin de ne pas le cumuler. Un fichier destiné à un traitement ultérieur n'a pas automatiquement besoin d'un dithering à chaque étape.

Après export, vérifier fichier, canaux, format, durée, début/fin, LUFS et true peak. Écouter les sections sensibles et les transitions si l'accès audio le permet. Si une version avec pertes est demandée, vérifier aussi cette version, dont les crêtes peuvent changer. Livrer des versions nommées sans écraser l'original.

Pour un album ou EP, comparer cohérence d'écoute, transitions, écarts de niveau voulus et fins de pistes. Ne pas forcer tous les titres à des LUFS identiques. Ne pas produire de DDP ou de métadonnées de livraison spécifiques sans outils et spécifications adaptés.
