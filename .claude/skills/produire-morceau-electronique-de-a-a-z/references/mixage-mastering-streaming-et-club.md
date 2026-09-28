# Références YouTube, master streaming et version club/DJ

*Vérification documentaire du 28 septembre 2026. Les exigences du distributeur et du destinataire prévalent; les fonctionnalités des applications changent. Les niveaux proposés sont des essais, jamais une garantie de diffusion.*

## 1. Classer la fiabilité de chaque référence

| Origine | Ce qu'elle permet | Ce qu'elle ne prouve pas |
|---|---|---|
| Fichier original WAV/AIFF/FLAC d'une édition connue, obtenu légitimement | Comparaison critique du grave, des transitoires, des aigus et du master, à niveau égal | La session, le plugin ou la chaîne exacte de l'artiste |
| Achat DJ lossless identifié, version club correspondante | Contraste de drop, mix DJ, spectre et densité selon le master publié | Un objectif de LUFS universel pour le genre |
| Audio d'une vidéo YouTube reconverti en WAV | Repères d'arrangement, densité, groove, structure, contraste relatif et timbre global | Un master sans perte, les vrais transitoires, l'air dans les aigus, true peak d'origine, la dynamique ou LUFS du master avant plateforme |
| Lecture YouTube dans l'application | Perception dans un environnement de streaming précis | Comparaison contrôlée si réglages de « volume stable », publicité, sorties et normalisation diffèrent |

**Pourquoi :** le chemin de diffusion YouTube peut comprendre encodage avec pertes; enregistrer ou convertir le résultat en PCM WAV conserve le signal *déjà décodé* mais ne reconstitue pas l'original. Il peut aussi exister plusieurs uploads/masters d'un même titre. La [documentation YouTube sur l'encodage](https://support.google.com/youtube/answer/1722171?hl=en) identifie les codecs d'upload; celle sur [Stable volume](https://support.google.com/youtube/answer/14106294?hl=en) décrit une modification possible du niveau pendant la lecture. L'explication « WAV ne récupère pas la qualité perdue » est une inférence de la conversion irréversible, pas une annonce de spécification de mastering YouTube.

Pour tes références actuelles, conserver le nom `REF_YT_SOURCE_VERSION`, noter URL/date/version lorsque connues et utiliser le protocole Live de `track-reference-avec-outils.md`. À chaque fois qu'une conclusion concerne dureté des aigus, distorsion, largeur extrême ou limiteur, confirmer avec au moins une source lossless légalement obtenue si possible. Ne jamais assimiler téléchargement/conversion de vidéo à autorisation d'échantillonnage ou de redistribution.

## 2. Un mix cohérent, deux tests de destination

Exporter un **premaster stéréo** de la session sans limitation finale ajoutée uniquement pour gagner du niveau, avec marge suffisante pour le traitement suivant, sans clipping. Le chiffre de marge n'est pas une obligation fixe; vérifier la sortie et les bus. Conserver sa fréquence native et une profondeur de travail de haute résolution selon le projet. Travailler sur copie pour le mastering, pas sur la seule version du mix.

**Streaming :** faire un master qui maintient groove, attaque du kick, basses lisibles, voix/lead et transcodage propre; mesurer integrated LUFS et true peak sur le fichier exporté avec un outil approprié. Spotify annonce une normalisation de lecture à **−14 LUFS**, réglages possibles **−11/−14/−19 LUFS** selon contexte, conseille **moins de −1 dBTP** et, si le master est plus fort que −14 LUFS, **moins de −2 dBTP** pour limiter les risques lors de l'encodage. Cette information est une recommandation Spotify, **pas une consigne universelle pour masteriser toute house à −14 LUFS**. Spotify demande un seul master stéréo de qualité par titre et la normalisation ne modifie pas le fichier avant lecture. [Page officielle Spotify](https://support.spotify.com/us/artists/article/loudness-normalization/).

**Apple :** son [guide Apple Digital Masters](https://www.apple.com/apple-music/apple-digital-masters/docs/apple-digital-masters.pdf) conseille sources de qualité et audition de l'encodage; Apple propose des outils pour détecter les problèmes d'encodage et d'écrêtage. Ne pas inventer une cible LUFS publique d'Apple à partir d'une valeur circulant sur les forums. La certification Apple Digital Masters suit ses propres critères et acteurs autorisés; ne pas qualifier arbitrairement un export comme tel.

**Club/DJ :** garder de la matière au kick et à la basse et une lecture nette dans un mix DJ; la version n'a aucune obligation d'être systématiquement plus forte. Comparer au niveau égalisé avec des titres lossless réellement joués par les DJs cibles. Essayer une version alternative seulement si la version streaming s'effondre sur sono ou si la structure DJ demande intro/outro et durée différentes. Dans le second cas, il s'agit d'un **edit/extended mix**, pas uniquement d'un mastering différent. Vérifier format et lecture sur le matériel prévu : [rekordbox](https://rekordbox.com/fr/download/) accepte plusieurs formats; le [CDJ-3000X](https://downloads.support.alphatheta.com/manuals/dj-players/CDJ-3000X/html/en/000_CDJ-3000X_IM_01_EN_DRI1956-A_en/Product_overview/Product_overview.htm?rhtocid=_2) documente WAV/AIFF notamment en 16/24 bits et plusieurs fréquences. La compatibilité d'autres modèles et du distributeur doit être vérifiée individuellement.

**Distribution :** si un distributeur envoie le même enregistrement vers Beatport et les plateformes, demander son cahier des charges; ne pas présumer que l'on peut fournir deux fichiers de master distincts pour un même identifiant/titre. Garder une version DJ distincte pour set ou sortie club si le circuit de distribution le permet, avec nom/version et droits clairs. [Beatport décrit les fournisseurs de distribution et les genres](https://greenroom.beatport.com/providers), sans fournir sur cette page un plafond LUFS universel.

## 3. Chaîne de décision avec les outils possédés

1. **Écoute et mesure du premaster** : importer sur piste dédiée Live; Utility pour écoute mono, SPAN pour spectre et Mid/Side, Pro-Q 4 pour repérer des problèmes *réellement audibles*. Noter les morceaux du même style et l'origine de chaque référence. Un analyseur spectral seul ne mesure ni LUFS intégré ni true peak.
2. **Corrections légères** : Pro-Q 4 uniquement sur déséquilibre persistant; si le problème existe seulement dans le refrain, revenir au mix ou automatiser plutôt que corriger toute la chanson. Pro-C 3 ou outils iZotope présents uniquement si un comportement dynamique précis l'exige; ne pas utiliser soothe3 pour corriger un sample mal choisi sans A/B.
3. **Contrôle de niveau final** : Live 12 Limiter dispose d'un mode **True Peak** selon le [manuel Live 12](https://www.ableton.com/en/manual/live-audio-effect-reference/); vérifier que la version installée possède cette interface. Si un limiteur iZotope ou FabFilter Pro-L 2 est effectivement possédé, vérifier ses fonctions de metering et son état. Ne pas assimiler Pro-Q 4, Pro-C 3 ou SPAN à un mesureur true peak/LUFS garanti. Ajouter si nécessaire un meter fiable présent ou autorisé avant de rapporter des chiffres. Placer le limiteur final en dernier dans le trajet réellement exporté; vérifier absence de processing postérieur qui modifie le pic.
4. **Tests comparatifs** : version A plus dynamique, version B plus poussée par petits incréments; égaliser leur volume de lecture et noter si A conserve plus de punch, si B devient dure, si le sub pompe ou si les queues se collent. Simuler un niveau réduit de diffusion par gain de monitoring pour juger le caractère après normalisation; cette simulation par gain n'imite pas nécessairement chaque codec ou appareil.
5. **Contrôle de l'export réel** : réimporter WAV masterisé, écouter 30 secondes d'intro, un break, une entrée de drop, le passage le plus fort, outro et fins; mesurer le fichier, tester en mono, écouter casque + enceintes et si possible appareil modeste. Si le mix change drastiquement après compression, retourner au mix.

### Feuille de décision à remplir, jamais à inventer

| Version | Référence de comparaison | LUFS intégré réellement mesuré | True peak réellement mesuré | Kick/sub en mono | Distorsion/codec | Choix |
|---|---|---|---|---|---|---|
| Premaster | Fichier lossless ou référence YT identifiée | ... | ... | ... | ... | Base |
| Master streaming A | Master lossless comparable | ... | ... | ... | ... | À décider |
| Variante club B | Achat DJ lossless comparable | ... | ... | ... | ... | À décider |

## 4. Apprendre auprès d'ingénieurs et de cours

- **Ingénierie du mastering et plateformes :** [Spotify, normalisation officielle](https://support.spotify.com/us/artists/article/loudness-normalization/), [Apple Digital Masters, document technique PDF](https://www.apple.com/apple-music/apple-digital-masters/docs/apple-digital-masters.pdf), [iZotope, cours sur mastering streaming](https://www.izotope.com/en/learn/mastering-for-streaming-platforms.html). Distinguer objectifs de lecture et spécifications d'envoi.
- **Cours vidéo structurés :** [iZotope « Are You Listening? », épisode 1 avec ingénieur](https://www.youtube.com/watch?v=E-6Lnp8RB00) et [questions de mastering de la série](https://www.izotope.com/community/blog/we-are-listening-your-mastering-questions-answered); [FabFilter, tutoriels mixing/mastering](https://www.fabfilter.com/learn/videos/category/mixing-mastering-tutorials). Pages et descriptions consultées, contenu intégral non visionné ici.
- **Workshops de professionnels :** [Mix with the Masters, Tony Maserati sur le grave](https://mixwiththemasters.com/videos/tony-maserati-managing-low-end-when-mixing/part/0) et [Justice, construction du son électronique](https://mixwiththemasters.com/videos/justice-justice-dear-alan/part/0). Accès aux sessions longues selon abonnement; ne pas leur attribuer des réglages non accessibles dans les extraits publics.
- **Analyse critique de loudness :** [Ian Shepherd, article historique sur la diffusion YouTube](https://productionadvice.co.uk/youtube-loudness/). Article de 2015 : ne pas le transformer en spécification officielle de YouTube en 2026.
