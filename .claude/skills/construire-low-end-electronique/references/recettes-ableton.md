# Recettes de session Ableton Live 12

Tous les nombres ci-dessous sont des essais initiaux, pas des normes. Comparer à volume compensé et ajuster selon le BPM, la note et la durée du kick.

## A. Bass House : kick prioritaire, sub pulsé

- Choisir un kick dont l'attaque et la queue se lisent dans le mix. Programmer le sub sur les contretemps ou les syncopes; raccourcir une note si elle traverse inutilement le kick suivant.
- Dans Serum 2 ou Operator, partir d'une sinusoïde ou table relativement pauvre en harmoniques pour le sub, phase/retrigger vérifiés à l'écoute. Une onde non « Basic Shapes » peut servir à la couche mid-bass; filtrer cette dernière en regard du sub, sans crossover fixe.
- Sidechain kick → basse : convention de `../../kick-bass-equilibre/SKILL.md` § 4 (source = piste KICK, Post FX si MIDI, Pre FX si piste AUDIO bouncée ; 4:1, attaque 0,1–1 ms, release 80–120 ms puis valeur validée du projet, 4–8 dB sur le sub tenu). Compressor natif seulement s'il est déjà en place (règle 6 d'`ableton-live-session`) ; sinon API-2500 ou Pro-C 3 (à prober). À 125 BPM, contrôler la relation avec 120 et 240 ms ; au-delà de 150 ms de release, vérifier le pompage (`../../mixage/references/diagnostics.md`). Refaire le réglage si le kick change.
- Option Pro-Q 4 : bande dynamique externe centrée sur le conflit mesuré, réduction modérée; comparer au ducking large. Option Pro-C 3 : sidechain externe, écouter le détecteur et vérifier son filtrage. Pro-Q 4 n'expose rien à Live : réglage par la fenêtre, preuve par capture ; Pro-C 3 est à prober avant usage (`../../mixage/references/outils.md`, `../../effets-plugins/references/fiches.md`).
- Garder le layer de sub centré; faire porter distorsion, stéréo et texture par le mid-bass. Comparer en mono et sur petits haut-parleurs.

## B. Future Rave : kick long et basse soutenue

- Mesurer le chevauchement au sein d'un coup complet. Si la queue du kick joue déjà la note grave, éviter de doubler durablement cette fondamentale avec la basse; déplacer la basse rythmiquement ou réduire sa tenue.
- Tester deux scénarios : basse duckée sur toute la durée utile de la queue; ou kick plus court avec basse plus présente. Comparer l'impact du premier coup et l'énergie entre coups.
- Si le lead ou le pad remplit 150–350 Hz, réduire sa contribution dans le drop au lieu de gonfler le kick ou de creuser toute la basse.

## C. Tech/Minimal : groove et variation de notes

- Programmer 1–2 mesures de basse avec silences intentionnels. Contrôler la vélocité, glide et longueur note par note. Un ghost bass faible peut rythmer sans épaissir le sub.
- Utiliser un ducking court seulement si le kick et la basse se rencontrent; ajuster le retour pour préserver le rebond. Vérifier chaque note car une fondamentale plus basse peut exciter davantage la pièce.
- Variante Afro House : tester un kick moins dominant sous une basse mélodique/percussive; ne pas recopier automatiquement la hiérarchie Bass House.

## D. 808 ou sub chantant

- Accorder les notes au morceau, écouter si le glide forme réellement une hauteur lisible et gérer le volume des notes longues.
- Saturation parallèle légère pour générer des harmoniques audibles sur téléphone; garder la branche sub nette, recaler les couches si une latence ou une phase change. Éviter les enhancers qui rendent le bas trop large.
- Si l'808 contient déjà un transient de kick, choisir si un deuxième kick est utile; vérifier la somme et la polarité sur plusieurs attaques.

## E. Contrôle final streaming et club

- Référence : fichier de qualité connue si possible; une extraction YouTube ne constitue pas une référence de fidélité garantie. Niveler l'écoute et ne jamais inférer l'énergie sub depuis un haut-parleur incapable de la reproduire.
- Exporter une version streaming et une version club seulement si la destination le justifie. Mesurer le true peak (Insight 2 ou WLM Plus en bout de Main, par capture ; `analyze_wav.py` ne donne que la crête sample), vérifier le grave en mono, la stabilité à bas volume et une écoute sur système avec grave fiable. Ne pas compenser des limites de monitoring par des boosts automatiques.
