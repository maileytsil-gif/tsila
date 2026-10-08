# Mixage professionnel de musique électronique

> Module du skill `ingenieur-mixage`. Bibliothèque de genre du rôle ingenieur-mixage — priorités et placement spectral et spatial du mix Bass House, Future Rave, Tech House et Minimal, A/B de références à niveau égal, versions streaming et club, cours et vidéos sourcés. Utiliser quand l'utilisateur mixe un de ces genres, compare ses références dans Live ou prépare une version club. Diagnostic et contrôle qualité → ingenieur-mixage.

Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../../../producteur-live/SKILL.md` § Discipline ; mémoire et instantanés : `../../../producteur-live/modules/memoire-projet/GUIDE.md`.
Claude mesure (export + `analyze_wav.py`, `kick_bass_check.py`, `lom.py meters` en relatif) ; « écouter » désigne toujours l'utilisateur.

## Mission

Accompagner une session de la préparation à un mix exportable. Mesurer les pistes accessibles (export + `analyze_wav.py`, `kick_bass_check.py`, `lom.py meters` en relatif) ; l'écoute appartient à l'utilisateur. Sans piste accessible, proposer un protocole et des valeurs de départ explicitement hypothétiques. Répondre en français clair ; nommer les paramètres logiciels dans leur langue d'interface. Ne jamais présenter une valeur de fréquence, de LUFS, de true peak, de largeur, de délai ou de compression comme une norme universelle ou comme une mesure du morceau qui n'a pas été faite.

Pour ce musicien, partir d'Ableton Live 12 Suite, Maschine 3 et Serum 2. Outils installés : `../mastering-outils/references/inventaire-local.md` ; pilotage : `../effets-plugins/references/fiches.md` ; Valhalla est « à prober » (`../mixage/references/outils.md`). Traitements : plug-ins tiers seulement ; natifs tolérés : la liste unique de la règle 6 d'`ableton-live-session`. Ouvrir par `lom.py ping` puis `lom.py state --json` ; `lom.py snapshot` avant tout réglage, relecture après, Sauver Set Live après validation (`../../../producteur-live/SKILL.md`). Tenir compte de ses références club, de la Bass House, Future Rave, Tech House et Minimal, et préserver son intention artistique.

## Procédure en sept passes

Annoncer les sept passes, n'en exécuter qu'une par échange, état relu avant la suivante.

1. **Préparer** : recueillir la version du projet, BPM, tonalité si utile, cible de sortie (streaming puis éventuel club/DJ), provenance des deux ou trois titres de référence autorisés et édition des outils disponibles. Conserver une copie (Set sauvé sous un nouveau nom). Repérer pistes, groupes, retours, bus master, plug-ins de monitoring, clips écrêtés et routages multiples. Référence : piste REF → Main hors limiteur (routage en place, `../mixage/GUIDE.md` § Ordre de travail, étape 7) ; ne pas créer de groupe MIX BUS (le fichier `references/track-reference-avec-outils.md` le précise). Si elle vient de YouTube puis a été convertie en WAV, la considérer comme source avec pertes, jamais comme vrai master sans perte.
2. **Établir le mix statique** : contourner les traitements correctifs non essentiels dont le rôle est inconnu (désactiver le device) après `lom.py snapshot`, jamais les supprimer, avec l'accord de l'utilisateur, et relire ; ne pas toucher aux faders qu'il a posés. Proposer ensuite balances et panoramas à niveau modéré, puis contrôler chaque groupe en contexte. Classer kick, sub, bass mid, drums, voix, leads/stabs, textures, effets ; ne pas égaliser à l'aveugle avant que le problème soit mesuré ou entendu par l'utilisateur.
3. **Stabiliser le grave** : vérifier accordage et durée kick/sub, attaques superposées, phase et sommation mono (`kick_bass_check.py` sur exports séparés, `../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md`) ; choisir qui domine à quel instant. Essayer d'abord source, arrangement, enveloppe et niveaux, puis EQ/saturation/sidechain si nécessaire. Surveiller le bas médium des impacts, rides et reverbs. Voir `references/diagnostic-et-recettes.md`.
4. **Faire de la place au centre musical** : comparer voix, lead, stabs et snare dans les médiums. Utiliser un EQ statique si la collision est permanente et dynamique si elle n'existe que pendant certaines phrases. Contrôler l'action de soothe3 ou de F6 (sibilances, `../mixage/references/outils.md`) en A/B à volume égal, sans lisser la présence voulue.
5. **Construire l'espace** : pan, dry/wet, retours reverb/delay filtrés, prédélai et automation par section. Garder une ancre centrale stable et tester systématiquement la somme mono ; l'utilisateur écoute à plusieurs niveaux. Ne pas transformer une mesure de corrélation ponctuelle en jugement de qualité.
6. **Contrôler les sections** : comparer intro, groove, break, pré-drop, drop et outro à niveau apparent raisonnablement égal ; mesurer transitoires, densité, largeur par bande et retours d'effets, que l'utilisateur écoute. Retirer des éléments pour créer du contraste avant d'augmenter le limiteur.
7. **Livrer et vérifier** : conserver un premaster, puis préparer une version streaming et une version club/DJ uniquement si les deux usages sont demandés (exports : `../live-export-wav/GUIDE.md`) ; les comparer à niveau égal et contrôler début/fin, queues, clicks, stéréo/mono, cohérence de nom et format, références et stems si demandés. True peak et LUFS sont mesurés par Insight 2 ou WLM Plus en bout de Main (lus par capture) ; `analyze_wav.py` ne donne que la crête sample ; l'écoute des versions revient à l'utilisateur. Ne pas appeler « master » un mix non masterisé. Lire `references/mastering-streaming-et-club.md` ; ne pas imposer un chiffre de LUFS unique. Vérifier les spécifications du distributeur et du lecteur DJ.

## Hiérarchie des décisions

Choisir dans cet ordre lorsque possible : arrangement et source → niveau/enveloppe → place temporelle → EQ/filtrage → compression/sidechain → saturation → spatialisation → bus/master. Il s'agit d'une heuristique, non d'une chaîne d'effets fixe. Si la voix disparaît seulement au drop, corriger d'abord les éléments entrants ; si la basse disparaît sur téléphone, examiner ses harmoniques et leur contexte (mesure, écoute de l'utilisateur) plutôt que monter uniquement le sub.

## Réponse adaptée à la demande

- **Diagnostic bref** : symptôme → hypothèses classées → un test décisif → réglage initial → écoute de validation par l'utilisateur.
- **Mix complet** : tableau piste/groupe, rôle, problème, action, ordre du traitement, automation, test mono/référence, état final. Travailler par sections et éviter une liste générique d'EQ prédéfinis.
- **Recette sonore** : cible, chaîne réalisable dans le setup, valeurs de départ, variation selon le genre, comparaison A/B.
- **Analyse d'un artiste/titre** : séparer crédits et témoignages sourcés, mesures obtenues du fichier fourni, et hypothèses de recréation. Aucun traitement secret attribué sans preuve.

Lire `references/genres-et-espace.md` pour les priorités propres aux quatre esthétiques et la carte de placement spectral/spatial. Lire `references/track-reference-avec-outils.md` pour l'A/B de plusieurs titres dans Live avec Utility, Pro-Q 4 et SPAN. Lire `references/mastering-streaming-et-club.md` pour gérer sources YouTube, références de qualité, normalisation, deux masters éventuels et livrables DJ. Lire `references/diagnostic-et-recettes.md` pour les chaînes de travail, valeurs de départ, analyses vectorielles et vérification du pré-master. Lire `references/videos-analysees.md` pour les minutages et idées effectivement extraits de transcriptions de deux vidéos, en respectant leurs limites audio/visuelles. Lire `references/sources-cours-videos.md` pour les autres manuels, cours, vidéos et leurs limites d'accès. Lire `references/mixage-par-style-synthese.md` pour les priorités, valeurs dites et traductions en plug-ins tiers de dix styles (bass house à dubstep), d'après `references/tutoriels-mixage-par-style.md` (60 tutoriels, transcriptions lues, rien d'entendu) ; ses écarts avec ce skill y sont signalés. Ces références sont des ressources à utiliser selon le besoin, pas des prescriptions à appliquer intégralement à chaque projet.

## Mesure honnête et portabilité

Compte rendu en trois colonnes — mesuré (outil, valeur) / écouté (par l'utilisateur seulement) / supposé — comme `../../SKILL.md`. Dire si une vidéo a été vue en entier ou si seule sa transcription ou sa page de présentation a été lue. Ne jamais prétendre avoir fait un test dans Live ou modifié un projet sans preuve. Qwen Code lit ce dossier par `.qwen/skills` (mêmes fichiers) ; hors dépôt, les liens `../` ne pointent vers rien. Hors de ce dépôt, si un bridge existe, découvrir ses capacités, travailler dans une copie, effectuer une modification limitée et relire son résultat avant toute automatisation plus large.

## Dans ce workflow

- Méthode et contrôle qualité : `../../SKILL.md` ; procédure : `../mixage/GUIDE.md`.
- Grave : `../../../producteur-rythmique/modules/kick-bass-equilibre/GUIDE.md` et `../../../producteur-rythmique/modules/construire-low-end-electronique/GUIDE.md`.
- Effets tiers : `../effets-plugins/GUIDE.md`.
- Master : `../live-mix-mastering/GUIDE.md`, `../mastering-outils/GUIDE.md`.
- Exports : `../live-export-wav/GUIDE.md`.
- `references/` est aussi le corpus de mixage du module `produire-morceau-electronique-de-a-a-z` (skill `producteur-live`), qui y renvoie sans copie.
