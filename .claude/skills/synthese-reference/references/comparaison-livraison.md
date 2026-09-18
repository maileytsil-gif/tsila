# Comparaison, critères d'arrêt et livraison

## Comparaison contrôlée
Employer les mêmes notes, registre, durée et vélocité autant que possible. Ajuster temporairement le volume d'écoute pour éviter que le son le plus fort semble meilleur. Une égalité de crête seule n'égalise pas la sensation de niveau ; vérifier aussi tenue et enveloppe. Sur des sons courts et rares, ne pas appliquer aveuglément des LUFS intégrés.

Aligner grossièrement les attaques sans modifier la vitesse de la référence. Comparer successivement :

1. hauteur et articulation ;
2. attaque et bruit/transitoire ;
3. couleur de la tenue et comportement du filtre ;
4. mouvement, battements, vibrato et stéréo ;
5. effets, queue et réponse au jeu.

Une phase d'oscillateur libre, le drift, l'unisson et les effets aléatoires rendent un test d'annulation exact inadapté. Un faible résidu n'est pas indispensable à un bon résultat auditif ; une petite différence de centroïde ne prouve pas une ressemblance. Les pics spectraux et hypothèses de hauteur servent à guider les réglages, pas à classer automatiquement les presets.

Décrire les écarts prioritaires avec un paramètre candidat : « attaque trop longue → enveloppe amplitude », « tenue trop sourde → cutoff/source », « queue trop nette → diffusion ou feedback ». Changer une famille à la fois, rendre un nouvel extrait et comparer. Ne pas répéter les mêmes essais sans nouvelle information.

Quand la référence contient d'autres instruments ou des traitements de mix indissociables, annoncer la limite et viser les caractéristiques dominantes. Un jugement « proche » exige une écoute comparative ; sans écoute, livrer un candidat technique à valider.

## Jouabilité
Tester note de référence, une note plus basse et une plus haute dans le registre visé, puis au moins une autre vélocité quand elle est pertinente. Vérifier key tracking, plage du filtre, glide, retrigger, polyphonie, voix et charge CPU. Une boucle de sample transposée peut changer de durée ou produire des artefacts : les contrôler si cette méthode est utilisée.

## Livrables
Selon les moyens réellement disponibles :

- **Analyse** : extrait et timecodes, observations, hypothèse de synthèse et limites.
- **Patch** : preset enregistré par le synthé dans son format natif ; version et ressources requises.
- **Chaîne** : rack/preset de l'hôte ou fiche ordonnée avec effets, valeurs et routages.
- **Démonstration** : courte phrase MIDI de test, rendu sec et rendu traité si possible, sans inclure la référence dans le bounce.
- **Comparaison** : améliorations vérifiées, écarts restants et précautions de registre/tempo.

Ne pas fabriquer un fichier de preset en renommant un JSON ou un texte. Si la sauvegarde native est inaccessible, fournir une fiche reproductible et signaler la différence.

Pour Serum 2, l'incorporation de tables ou samples personnels au preset peut faciliter le rappel ; vérifier la fonction « Embed in Preset » sur les ressources utilisées. Le manuel précise que cette option n'est pas disponible pour le contenu d'usine. Après sauvegarde, tester le rappel dans une copie ou instance de travail, en conservant l'état courant. [Sauvegarde des ressources Serum 2](https://xferrecords.com/web-manual/serum-2/embedding-content-when-saving-a-preset).

Pour Live, enregistrer le rack ou le Set demandé et réunir les ressources externes selon les outils disponibles. Vérifier que la chaîne de piste n'est pas perdue en ne sauvegardant que le preset du synthé. Un chargement réussi sans ressource manquante et un rendu de test constituent une vérification concrète ; indiquer ce qui n'a pas pu être effectué.
