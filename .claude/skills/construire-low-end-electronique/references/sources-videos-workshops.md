# Sources commentées — consultées le 28 septembre 2026

Les liens ci-dessous mènent aux pages officielles et aux vidéos identifiées. Cette sélection résulte de la consultation des pages et descriptifs disponibles; elle ne prétend pas à un visionnage intégral des vidéos ni à l'accès au contenu payant des cours.

## Documentation et cours

1. [Ableton Live 12, Audio Effect Reference](https://www.ableton.com/en/manual/live-audio-effect-reference/) — Compressor sidechain, EQ Eight, Utility et Spectrum. Vérifier la version installée avant d'appliquer un libellé d'interface.
2. [Ableton, Sidechain Compression Part 2](https://www.ableton.com/en/blog/sidechain-compression-part-2-common-and-uncommon-uses/) — exemple de ducking kick/basse.
3. [FabFilter Pro-Q 4, external side chaining](https://www.fabfilter.com/help/pro-q/support/externalsidechaining) — routage d'un signal externe sur l'EQ dynamique.
4. [FabFilter Pro-C 3, external side chaining](https://www.fabfilter.com/help/pro-c/support/externalsidechaining) — sidechain, écoute du détecteur.
5. [FabFilter, Linear phase EQ](https://www.fabfilter.com/learn/equalization/linear-phase-eq) — pre-ring et latence, cas d'un loop de batterie.
6. [iZotope, How to mix bass](https://www.izotope.com/en/learn/7-tips-for-mixing-bass) — relation kick/basse et traduction.
7. [iZotope, What is phase in audio?](https://www.izotope.com/en/learn/5-ways-to-adjust-phase-after-recording) — problèmes de phase et méthodes de vérification.
8. [iZotope, Producing and mixing house music](https://www.izotope.com/en/learn/9-tips-for-producing-and-mixing-house-music) — rôle du kick en House, à adapter au sous-genre.
9. [Sonarworks, Room modes](https://www.sonarworks.com/blog/learn/room-modes) — limites du jugement du sub dans une petite pièce.
10. [Production Music Live, How to EQ Kick and Bass](https://www.productionmusiclive.com/blogs/news/how-to-eq-kick-and-bass-for-powerful-low-end) — approche de terrain, à tester par A/B et non à suivre comme fréquences obligatoires.

## Vidéos et workshops à étudier en situation

- [FabFilter, catalogue vidéo](https://www.fabfilter.com/learn/videos) — dont *The Philosophy of Bass* ([YouTube](https://www.youtube.com/watch?v=1xPO2Q2QHXk)), cours vidéo de Dan Worrall sur la perception et la gestion du grave; reproduire les expériences dans une session Live, sans transposer les chiffres par défaut.
- [FabFilter, EQ: Linear Phase vs Minimum Phase](https://www.youtube.com/watch?v=efKabAQQsPQ) — vidéo Dan Worrall, utile pour les risques de pre-ring et les comparaisons d'EQ. Identifiant non confirmé par une recherche du 30 sept. 2026 (le titre existe) : vérifier le lien en local.
- [FabFilter, Introduction to Pro-Q 4](https://www.youtube.com/watch?v=IXWkViqU2K8) — vidéo Dan Worrall présentant les outils actuels de l'EQ.
- [Production Music Live, Course: Low End – Kick & Bass Setup](https://www.productionmusiclive.com/products/course-low-end-kick-bass-setup) — workshop/cours Ableton annoncé sur sound design, transitoires, phase et analyseurs. **Contenu payant non consulté** : description publique uniquement.
- [Production Music Live, Jonas Saalbach studio tips](https://www.productionmusiclive.com/blogs/news/10-mixing-tips-from-jonas-saalbach-radikon) — entretien d'artiste et renvoi à une masterclass studio; source d'exemples, pas recette universelle.

## Hiérarchie de preuve

Une documentation officielle démontre une capacité du logiciel; un workshop illustre une méthode possible; un rendu A/B du projet vérifie si cette méthode aide ce morceau. En cas de désaccord, privilégier les mesures et l'écoute contrôlée du projet. Les réglages chiffrés du skill sont des hypothèses de départ établies pour faciliter ce test, pas des citations de ces sources.

## Analyse directe des transcriptions vidéo (mise à jour du 28 septembre 2026)

Transcription horodatée automatique lue par le modèle auteur du pack (28 sept. 2026), **non revérifiée par Claude** ; ni l'audio ni l'image n'ont été examinés. Elle peut mal reconnaître des mots ; les conclusions sont paraphrasées et les repères servent à retrouver la démonstration dans la vidéo.

### [The Philosophy of Bass](https://www.youtube.com/watch?v=1xPO2Q2QHXk), FabFilter / Dan Worrall, 32:49

- 0:52–7:18 : le grave ressenti dépend d'un système d'écoute qui reproduit réellement le sub et d'une pièce qui ne masque pas sa réponse. Les deux paires de casques illustrées mènent à des compensations opposées; ne pas les généraliser à tous les exemplaires.
- 8:38–10:26 : l'auteur distingue « body bass » (fondamentale très présente) et « brain bass » (perception de la fondamentale à partir des harmoniques). Ses deux remèdes initiaux aux conflits kick/basse sont la séparation **spectrale** et **temporelle**, y compris une ligne de basse entre les coups de kick.
- 10:35–14:44 : si kick profond et basse continue se chevauchent, sidechain possible avec Pro-G, Pro-C 2 ou Pro-MB (versions montrées dans cette vidéo). Ducking pleine bande ou bande grave seulement : le choix dépend des harmoniques et du groove; ce n'est pas une hiérarchie universelle. Pro-G et Pro-MB ne sont pas installés (`../../mastering-outils/references/inventaire-local.md`) : transposer vers Pro-C 3 (installé, à prober, en vérifiant son manuel), API-2500 ou le Compressor sidechain déjà en place ; ducking de la seule bande grave : Waves C4/C6/LinMB ou F6 (installés, non probés).
- 14:47–17:25 : pour un 808 hybride, kick d'attaque à hauteur stable + queue synthétique accordée; écouter la polarité et l'effet du passe-haut sur la phase. Le registre de la fondamentale et la tonalité conditionnent la sensation physique du sub; l'exemple G/A autour de 50 Hz est contextuel, pas une tonalité obligatoire.
- 17:26–22:37 : 2e et 3e harmoniques peuvent maintenir la hauteur perçue même quand la fondamentale manque. Une distorsion parallèle subtile crée de la définition; l'exemple EQ avant distorsion (creux vers 100–200 Hz), puis EQ inverse après, limite une couleur trop envahissante. Vérifier par A/B et surveiller la sommation parallèle.
- 23:19–25:55 : passe-haut ciblé pour retirer le contenu bas inutile; son usage sur kick/basse dépend de la fondamentale et peut modifier phase et punch. Le récit d'un filtrage des pistes non graves à 80–100 Hz décrit une configuration de diffusion; éviter d'en faire une fréquence obligatoire dans chaque session.
- 27:22–32:28 : une courbe d'analyse « plate » n'est pas une cible; pente et lissage changent l'affichage. Au club, la diffusion et la pièce peuvent déjà accentuer le sub. Si besoin, multibande doux et release ajusté au ressenti; surveiller surtout la fin des notes de basse.

**Exercice à reproduire dans Ableton** : sur une boucle kick + basse, comparer (A) déplacement de notes, (B) ducking pleine bande, (C) ducking bande grave, (D) layer harmonique parallèle. Niveler les quatre exports, tester mono et petit haut-parleur; consigner les fins de notes et la réaction du sub à la note la plus basse.

### [Introduction to FabFilter Pro-Q 4](https://www.youtube.com/watch?v=IXWkViqU2K8), FabFilter / Dan Worrall, 12:47

Même vidéo que `../../produire-morceau-electronique-de-a-a-z/references/mixage-videos-analysees.md`, qui donne d'autres minutages (instances et collisions 1:50–4:35, bande dynamique 7:03–8:53, spectral 8:56–10:11) : recaler les deux fichiers sur la transcription avant de citer un minutage.

- 4:13–4:36 : affichage de plusieurs instances et détection de collision pour repérer d'éventuels masquages; un indicateur rouge suggère une zone à écouter, pas une coupe automatique.
- 6:54–8:55 : bandes dynamiques avec attaque et relâchement ajustables. Sur l'exemple basse, relâchement grave plus lent et bande haute plus rapide pour moduler définition; adapter le temps au groove plutôt que recopier l'exemple.
- 9:06–10:12 : la bande spectrale est présentée sur un Rhodes, pas comme une solution de sub par défaut. Elle utilise une analyse FFT et entraîne un comportement de phase linéaire pour cette bande ainsi qu'une latence dépendant de la résolution; les autres bandes conservent leur mode choisi. Sur kick/basse, vérifier l'attaque et la compensation de délai après activation.
- 10:13–12:26 : risque de retirer le caractère avec un traitement spectral large; sidechain spectral également possible. Employer uniquement après avoir constaté un problème audible et comparer au bypass nivelé.

La [vidéo sur la phase linéaire et minimale](https://www.youtube.com/watch?v=efKabAQQsPQ) a été ouverte mais aucune transcription n'était disponible dans cet accès. Son titre et sa présentation ont été vérifiés; **aucune démonstration précise de cette vidéo n'est attribuée ici**. Pour la question du pre-ring, lire la [documentation FabFilter sur l'EQ à phase linéaire](https://www.fabfilter.com/learn/equalization/linear-phase-eq).

## Suite à donner

Claude n'entend pas l'audio : il lit une transcription et regarde des captures, l'utilisateur écoute. En local (Claude in Chrome), relire les transcriptions de [The Philosophy of Bass](https://www.youtube.com/watch?v=1xPO2Q2QHXk) et d'[Introduction to FabFilter Pro-Q 4](https://www.youtube.com/watch?v=IXWkViqU2K8), capturer l'écran aux minutages cités (bypass, courbes, réglages visibles), chercher une transcription d'[EQ: Linear Phase vs Minimum Phase](https://www.youtube.com/watch?v=efKabAQQsPQ) ; mettre à jour le statut, ne jamais écrire « entendu ». Les exercices A–D se refont dans Live, mesurés par `kick_bass_check.py` sur exports, jugés à l'oreille par l'utilisateur. Pour chaque vidéo, relever titre, durée, version de plug-in réellement montrée, minutage, état bypass/niveau lors des A/B, ce que l'utilisateur a entendu et limites d'application. Revoir particulièrement 9:41–13:05, 17:26–22:37 et 27:22–32:28 de *Philosophy of Bass*, ainsi que 6:54–10:56 de *Pro-Q 4*. Comparer la vidéo sur la phase à la documentation FabFilter; ses démonstrations n'ont pas encore été relevées ici. Ne pas transformer les réglages montrés en presets universels. Si la lecture n'est pas possible, l'indiquer dans le livrable et utiliser les transcriptions seulement comme preuves textuelles.
