# Mastering et mesures du fichier final

## Sonie et traitement
Déterminer l'usage : streaming, fichier d'écoute, club, vidéo, CD ou livraison avec spécifications. Vérifier les exigences actuelles de la destination lorsqu'elles sont nécessaires. Ne pas traiter une valeur de normalisation de plateforme comme une obligation artistique ou de livraison. Sans cible fournie, préserver d'abord punch et équilibre, puis expliciter la cible retenue plutôt qu'imposer −14 LUFS à tous les styles.

EQ global, compression, saturation, traitement multibande et limiteur sont des options selon le diagnostic, pas une chaîne obligatoire. Utiliser une limitation compatible avec l'objectif de true peak et vérifier le fichier rendu : le plafond affiché ne remplace pas la mesure. Un limiteur de sample peaks ne garantit pas un plafond en dBTP.

## Mesurer correctement
- **dBFS sample peak** : maximum des échantillons du fichier.
- **dBTP true peak** : estimation des crêtes inter-échantillons par un outil adapté ; ne pas la déduire des sample peaks.
- **LUFS intégrés** : mesure du programme entier ; compléter avec sonie à court terme pour comparer les sections. Ne pas déduire les LUFS des seuls RMS.
- **LRA** : indication de variation de sonie ; ne prouve pas à elle seule la qualité des transitoires ou l'absence de compression excessive.

Les vu-mètres interrogés dans Live ne suffisent pas à certifier l'export. Analyser le fichier exact livré, sur sa durée entière, avec un mesureur approprié. Vérifier le point de mesure dans la chaîne.

Ne pas convertir le fichier en 16 bits pour certifier les crêtes de l'original. Un compte d'échantillons proches du plafond n'est pas une preuve d'écrêtage. Distinguer proximité du plafond, dépassements numériques, true peaks et distorsion audible.


## Analyse sans modifier le fichier
**Sur ce Mac, FFmpeg est absent** (voir `notes-locales.md`) : LUFS et true peak par Insight 2 ou WLM Plus ; ce qui suit ne s'applique que si un binaire est installé un jour.

Si FFmpeg est disponible et comprend le filtre ebur128, utiliser ce filtre en analyse seule. Vérifier le binaire et ses filtres au préalable. Exemple, en remplaçant le chemin par celui du fichier réel et en citant correctement les arguments :

```sh
ffmpeg -hide_banner -nostats -i '/chemin/master.wav' -map 0:a:0 -af 'ebur128=peak=true' -f null -
```

La sortie contient les mesures de sonie et de crête vraie ; conserver le résumé final. Si le filtre ou la mesure de true peak manque, employer un mesureur disponible, ou signaler la mesure indisponible. Ne pas fabriquer de valeur ni installer un outil sans nécessité.

Documentation primaire : [FFmpeg, filtre ebur128](https://www.ffmpeg.org/ffmpeg-filters.html#ebur128). Le filtre permet l'analyse de sonie et une mesure de true peak ; consulter sa documentation pour les options de la version utilisée.

## Formats et contrôle de fin
Vérifier durée, canaux, fréquence, résolution et intégrité. Conserver la fréquence source sauf besoin de livraison explicite. Lors d'une réduction finale vers un format PCM entier, décider du dithering à cette étape et éviter de le cumuler dans le limiteur puis à l'export. Ne pas ditherer les intermédiaires flottants par défaut.

Examiner début, fin, silences et queues, puis écouter les passages sensibles si possible. En cas de conversion avec pertes demandée, contrôler aussi ce fichier converti : ses crêtes peuvent différer. Un rapport de mesure doit nommer le fichier analysé et distinguer résultat mesuré, objectif et jugement auditif.
