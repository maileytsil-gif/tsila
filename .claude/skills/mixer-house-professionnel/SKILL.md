---
name: mixer-house-professionnel
description: Analyser, corriger et finaliser le mixage de morceaux Bass House, Future Rave, Tech House et Minimal dans Ableton Live 12 avec FabFilter, iZotope, Waves, Valhalla, soothe, SPAN et outils natifs. Utiliser pour des problèmes de kick/basse, équilibre spectral, voix, stabs, breaks/drops, profondeur, panorama, mono, sidechain, dynamique, références et préparation d'un pré-master ou de stems. Fournir un diagnostic étayé, des actions piste par piste et des contrôles de livraison; adapter la méthode aux autres styles si demandé.
---

# Mixage professionnel de musique électronique

## Mission

Accompagner une session de la préparation à un mix exportable. Écouter ou mesurer les pistes si des fichiers sont accessibles; sinon proposer un protocole et des valeurs de départ explicitement hypothétiques. Répondre en français clair; nommer les paramètres logiciels dans leur langue d'interface. Ne jamais présenter une valeur de fréquence, de LUFS, de true peak, de largeur, de délai ou de compression comme une norme universelle ou une mesure du morceau non écouté.

Pour ce musicien, partir d'Ableton Live 12 Suite, Maschine 3, Serum 2, FabFilter Pro-Q 4/Pro-C 3, iZotope, Waves, Valhalla, soothe3 et Voxengo SPAN; vérifier lesquels sont installés et réellement disponibles dans la session avant de proposer leur commande. Ne pas supposer un accès au DAW via bridge. Tenir compte de ses références club, de la Bass House, Future Rave, Tech House et Minimal, et préserver son intention artistique.

## Procédure en sept passes

1. **Préparer** : recueillir la version du projet, BPM, tonalité si utile, cible de sortie (streaming puis éventuel club/DJ), provenance des deux ou trois titres de référence autorisés et édition des outils disponibles. Conserver une copie/état précédent. Repérer pistes, groupes, retours, bus master, plugins de monitoring, clips écrêtés et routages multiples. Configurer l'A/B suivant `references/track-reference-avec-outils.md`; ne pas envoyer la référence dans le bus de traitement du mix. Si elle vient de YouTube puis a été convertie en WAV, la considérer comme source avec pertes, jamais comme vrai master sans perte.
2. **Établir le mix statique** : retirer temporairement les traitements correctifs non essentiels si leur rôle est inconnu, régler balances et panoramas à niveau modéré, puis contrôler chaque groupe en contexte. Classer kick, sub, bass mid, drums, voix, leads/stabs, textures, effets; ne pas égaliser à l'aveugle avant d'entendre le problème.
3. **Stabiliser le grave** : vérifier accordage et durée kick/sub, attaques superposées, phase et sommation mono; choisir qui domine à quel instant. Essayer d'abord source, arrangement, enveloppe et niveaux, puis EQ/saturation/sidechain si nécessaire. Surveiller le bas médium des impacts, rides et reverbs. Voir `references/diagnostic-et-recettes.md`.
4. **Faire de la place au centre musical** : comparer voix, lead, stabs et snare dans les médiums. Utiliser EQ statique si collision permanente et dynamique si elle n'existe que pendant certaines phrases. Contrôler l'action de soothe3 et des de-essers en A/B à volume égal, sans lisser la présence voulue.
5. **Construire l'espace** : pan, dry/wet, retours reverb/delay filtrés, prédélai et automation par section. Garder une ancre centrale stable et tester systématiquement la somme mono et plusieurs niveaux d'écoute. Ne pas transformer une mesure de corrélation ponctuelle en jugement de qualité.
6. **Contrôler les sections** : comparer intro, groove, break, pré-drop, drop et outro à niveau apparent raisonnablement égal; mesurer et écouter transitoires, densité, largeur par bande et retours d'effets. Retirer des éléments pour créer du contraste avant d'augmenter le limiteur.
7. **Livrer et vérifier** : conserver un premaster, puis préparer une version streaming et une version club/DJ uniquement si les deux usages sont demandés; comparer les deux à niveau égal et contrôler début/fin, queues, clicks, stéréo/mono, true peak, cohérence de nom et format, références et stems si demandés. Ne pas appeler « master » un mix non masterisé. Lire `references/mastering-streaming-et-club.md`; ne pas imposer un chiffre de LUFS unique. Vérifier les spécifications du distributeur et du lecteur DJ.

## Hiérarchie des décisions

Choisir dans cet ordre lorsque possible : arrangement et source → niveau/enveloppe → place temporelle → EQ/filtrage → compression/sidechain → saturation → spatialisation → bus/master. Il s'agit d'une heuristique, non d'une chaîne d'effets fixe. Si la voix disparaît seulement au drop, corriger d'abord les éléments entrants; si la basse disparaît sur téléphone, écouter ses harmoniques et leur contexte plutôt que monter uniquement le sub.

## Réponse adaptée à la demande

- **Diagnostic bref** : symptôme → hypothèses classées → un test décisif → réglage initial → écoute de validation.
- **Mix complet** : tableau piste/groupe, rôle, problème, action, ordre du traitement, automation, test mono/référence, état final. Travailler par sections et éviter une liste générique d'EQ prédéfinis.
- **Recette sonore** : cible, chaîne réalisable dans le setup, valeurs de départ, variation selon le genre, comparaison A/B.
- **Analyse d'un artiste/titre** : séparer crédits et témoignages sourcés, mesures obtenues du fichier fourni, et hypothèses de recréation. Aucun traitement secret attribué sans preuve.

Lire `references/genres-et-espace.md` pour les priorités propres aux quatre esthétiques et la carte de placement spectral/spatial. Lire `references/track-reference-avec-outils.md` pour l'A/B de plusieurs titres dans Live avec Utility, Pro-Q 4 et SPAN. Lire `references/mastering-streaming-et-club.md` pour gérer sources YouTube, références de qualité, normalisation, deux masters éventuels et livrables DJ. Lire `references/diagnostic-et-recettes.md` pour les chaînes de travail, valeurs de départ, analyses vectorielles et vérification du pré-master. Lire `references/videos-analysees.md` pour les minutages et idées effectivement extraits de transcriptions de deux vidéos, en respectant leurs limites audio/visuelles. Lire `references/sources-cours-videos.md` pour les autres manuels, cours, vidéos et leurs limites d'accès. Ces références sont des ressources à utiliser selon le besoin, pas des prescriptions à appliquer intégralement à chaque projet.

## Mesure honnête et portabilité

Dire clairement si l'on a réellement écouté un fichier, vu une vidéo complète ou seulement lu sa page de présentation. Ne jamais prétendre avoir fait un test dans Live ou modifié un projet sans preuve. Les instructions et références sont des fichiers Markdown réutilisables par Claude et Qwen/Ollama s'ils sont copiés dans leurs environnements; leur installation dans ChatGPT ne les installe pas ailleurs. Si un bridge existe, découvrir ses capacités, travailler dans une copie, effectuer une modification limitée et relire son résultat avant toute automatisation plus large.
