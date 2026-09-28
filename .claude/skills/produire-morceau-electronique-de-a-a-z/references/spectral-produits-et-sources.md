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
