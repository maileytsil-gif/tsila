# Étude pratique : soothe3, Waves Curves, Pro-Q 4 et Pro-C 3

Analyse et recettes pour Bass House, Future Rave, Tech House et Minimal, dans Ableton Live 12 Suite. Sources officielles consultées le 28 septembre 2026. Les repères de traitement sont des hypothèses d’écoute, à ajuster au morceau. Les pages de vidéos et leurs chapitres ont été examinés ; les exemples audio n’ont pas été auditionnés.

# Produits, fonctionnement et sources primaires

## Soothe3, distinguer soigneusement de soothe2

Manuel officiel mis à jour le 4 août 2026 : https://oeksound.com/manuals/soothe3/ . Détecte les pics résonants et les atténue avec un filtre dynamique adaptatif. **Soft** : seuil adaptatif relatif au contenu tonal, réponse moins dépendante du niveau ; **Hard** : plus agressif et dépendant du niveau. Commencer Soft ; choisir Hard seulement si l'effet désiré le justifie, puis réduire Depth. **Depth** dose la réduction ; **Detail** choisit largeur des accumulations versus précision des résonances ; **Attack/Release** règlent la dynamique ; **Max cut** limite la réduction maximale ; **Wet trim** précède Mix ; jusqu'à huit bandes de courbe avec depth et Q locaux. **Delta** auditionne le signal retiré. **SC** active un sidechain externe, avec bouton d'écoute de la clé. Stéréo L/R ou M/S ; Link 100 % analyse commune, 0 % indépendant ; focus global et par bande ; le découplage M/S peut élargir l'image, ce qui requiert contrôle mono. Tilt de Detail/Attack/Release bas et haut : ralentir l'attaque dans le bas peut préserver le punch. Qualité règle la fréquence de mise à jour des filtres ; vérifier compensation de latence et mode faible latence pour le jeu temps réel. Pas de commande d'oversampling dans soothe3 : https://oeksound.com/support/oversampling-in-soothe/ . **Ne pas recopier les contrôles sharpness/selectivity ou le comportement de soothe2.**

## Curves Equator

Manuel officiel : https://assets.wavescdn.com/pdf/plugins/curves-equator.pdf . Suppression des résonances par courbe de seuil et traitement dynamique. **Adaptive** part d'une courbe plate ou d'usine que l'on modèle ; **Captured** apprend un passage représentatif quand la nature sonore convient et demande un affinage. Le seuil principal agit sur la quantité ; capturer section stable et vérifier les autres sections. Peut construire la courbe avec sidechain. Version **Live** à latence nulle, avec gel de courbe pendant les pauses. Vérifier les noms précis de réglages secondaires dans la version installée ; éviter l'équivalence chiffrée avec Depth de soothe3.

## Curves Resolve

Manuel officiel : https://assets.wavescdn.com/pdf/plugins/curves-resolve.pdf . Insérer sur la piste **à réduire**, acheminer la piste prioritaire en sidechain. Détecte le recouvrement spectral ; commande principale 0–100 %, quatre zones délimitées par trois crossovers, chacune 0–200 % de la réduction normale. Mode **Dynamic** suit la clé instantanée ; **Steady** utilise un profil capturé par Learn/Freeze/Scan File. Le manuel recommande Dynamic pour la plupart des usages ; Steady peut lisser les artefacts. **Follow SC On** pour libérer l'espace uniquement quand la clé joue ; Off laisse un traitement continu. **Ducker** offre une atténuation plus large, avec Wide ou Unmask. Filtres HPF/LPF et Tilt façonnent **seulement la détection** sidechain ; SC audition vérifie la clé. Sélecteur Sidechain Content (Vocals, Kick, Bass, etc.) déplace plusieurs réglages de départ ; le vérifier après sélection. **Attack** et **Release** 0–1000 ms, Precision 0–100. Auto Make-Up Gain OFF par défaut : garder OFF pour comparaison initiale, aligner manuellement. Delta auditionne l'atténuation. Balance Linked/Split/M/S, selon version et hôte ; Pro Tools a des restrictions de sidechain stéréo. Limiteur interne éventuel à -0,1 dB n'est pas une chaîne de mastering streaming/club.

## Curves AQ

Manuel officiel : https://assets.wavescdn.com/pdf/plugins/curves-aq.pdf ; présentation https://www.waves.com/in-depth-tutorial-curves-aq . Learn produit plusieurs profils tonals à choisir puis modifier, avec cibles, tilt, boost/cut, traitement statique/dynamique. Il voit sa **piste**, pas le conflit complet du mix : ne pas le présenter comme un Resolve automatique. Employer pour redessiner globalement un timbre en comparant une référence pertinente, préserver les choix intentionnels de synthèse.

## Vidéos officielles à exploiter

- Waves, «Curves Resolve In-Depth», 26 janvier 2026, 0:44 route initiale, 2:52 voix, 4:53 kick/basse, 5:58 ducking, 6:42 réverbérations, 7:54 instances multiples : https://www.waves.com/curves-resolve-in-depth . Le découpage est fourni par Waves ; ne pas prétendre avoir entendu les exemples audio si seule la page et son descriptif sont accessibles.
- Waves, «In-Depth Tutorial of Curves AQ», 1:39 Learn, 4:46 statique/dynamique, 7:24 cible, 11:25 MixSense : https://www.waves.com/in-depth-tutorial-curves-aq .
- Waves, «Quick Start with Curves Resolve» : https://www.waves.com/quick-start-curves-resolve .

Ne pas attribuer de valeur universelle en dB/Hz à ces outils. Les chiffres des recettes sont des **points de départ de mix**, indépendants des recommandations officielles.


# Compétence FabFilter Pro-Q 4 et Pro-C 3

## Pro-Q 4

Manuel https://www.fabfilter.com/downloads/pdf/help/ffproq4-manual.pdf ; dynamique spectrale https://www.fabfilter.com/help/pro-q/using/spectral-dynamics ; dynamique https://www.fabfilter.com/help/pro-q/using/dynamic-eq . EQ statique pour enlever une zone toujours problématique ; EQ dynamique pour ne traiter une bande qu'aux événements ; mode **Spectral** pour agir sur les fréquences dépassant le seuil **dans** la bande plutôt que sur toute la bande. Créer Bell ou Shelf, fixer la plage dynamique et activer l'icône Spectral ; écouter les attaques et comparer au mode dynamique ordinaire. Choisir Mid/Side si le conflit est spatial et vérifier mono. Minimum Phase pour usage général ; Linear Phase seulement après écoute des transitoires et compensation de latence, particulièrement kick/basse ; Natural Phase à comparer selon le cas. L'analyseur et la liste d'instances aident à repérer chevauchements, sans prouver qu'ils sont audibles. Sidechain externe sur bande dynamique si une source prioritaire doit déclencher l'EQ ; vérifier dans version hôte et écouter la clé.

**Cas** : lead Future Rave variable en 3–5 kHz → Bell large à gain neutre/déplacement de gain modéré, plage dynamique descendante en mode Spectral, seuil tel que seule l'agressivité des fortes notes déclenche ; A/B contre soothe3 sur **la même piste**, même niveau. Si un synthé est systématiquement trop dur, EQ statique suffit. Kick et basse dont l'énergie spectrale change selon les notes → bande dynamique externe sur basse, clé kick, sélectionner strictement la zone de recouvrement ; si l'ensemble du corps de la basse doit descendre à chaque kick, Pro-C 3 est plus prévisible.

## Pro-C 3

Manuel https://www.fabfilter.com/downloads/pdf/help/ffproc3-manual.pdf ; styles https://www.fabfilter.com/help/pro-c/using/styleandcharacter ; dynamique https://www.fabfilter.com/help/pro-c/using/dynamicscontrols ; configuration Live https://www.fabfilter.com/help/pro-c/support/externalsidechaining . Compression de **niveau** et d'enveloppe : Threshold, Ratio, Attack, Release, Knee, Range, Lookahead, Mix, Side Chain EQ et audition de clé selon l'interface. Pro-C 3 compte **14 styles** ; Clean neutre, Versatile polyvalent, Smooth pour colle, Punch pour impact, Upward pour remontée des passages faibles ; les styles TTM et colorés sont plus créatifs et changent le résultat, donc ne pas permuter sans réécoute. Vérifier Attack/Release contre la durée de la mesure et les transitoires. **Range** limite le changement de gain maximal ; ne le confondre ni avec Ratio ni avec la plage dynamique de Pro-Q. Mode external sidechain : Live route la piste clé vers l'entrée sidechain du périphérique puis choisir **Ext** dans Pro-C 3 et auditionner le déclencheur. Side Chain EQ modifie la détection ; contrôler si le style choisi (notamment TTM) change l'effet audible des bandes.

**Recettes de départ, heuristiques** : kick → basse, Pro-C 3 sur basse, clé kick, Clean ou Versatile ; attaque brève si le kick doit prendre la place immédiatement, release suffisamment court pour le contretemps mais sans clic ; ajuster Threshold pour réduction audible puis limiter Range et égaliser les niveaux. Pour pompage assumé Future House, prolonger Release jusqu'au rebond musical ; pour Tech House sobre, limiter Range et préserver la pulsation. Bus batterie : Smooth ou Punch, ratio modéré, attaque laissant passer les transitoires, release revenant avant prochain temps ; si cymbales provoquent compression indue, filtrer la détection. Vocaux : Versatile/Smooth, compression en plusieurs passages légers si grande variation, recontrôler consonnes et souffle. Aucun chiffre de GR n'est universel.

## Décision et combinaison

| Problème | Premier essai | Alternative ou complément si nécessaire |
|---|---|---|
| Pic tonal fixe | Pro-Q 4 statique | Corriger source ; Equator pour plusieurs pics mobiles |
| Résonance mouvante dans une seule piste | soothe3 ou Pro-Q 4 Spectral | Equator Captured/Adaptive, A/B à niveau identique |
| Deux pistes se masquent ponctuellement | Resolve | Pro-Q 4 dynamique externe pour bande précise |
| Basse entière doit reculer devant kick | Pro-C 3 externe | Resolve si seules quelques fréquences doivent reculer |
| Crêtes/bus et groove | Pro-C 3 | Modifier arrangement et enveloppes avant compression excessive |
| Déséquilibre tonal général | Pro-Q 4 statique ou AQ | Comparer sections homologues de référence |

Placer d'abord l'EQ correctif avant compression si la résonance déclenche exagérément le compresseur ; essayer après si le compresseur fait ressortir la dureté. Un sidechain spectral et un compresseur sidechain peuvent coexister si chacun résout une gêne distincte, avec mesure cumulée et A/B de chaque maillon. Ne jamais transformer les réglages de réduction propres à chaque produit en nombres équivalents.


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

