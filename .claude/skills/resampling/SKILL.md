---
name: resampling
description: Capturer en audio une piste, un bus ou le Main dans Ableton Live, puis préparer la prise pour une boucle, un one-shot, un reverse ou un instrument échantillonné. Utiliser pour resampler, imprimer un synthé avec ses effets ou transformer une prise audio. Pour un export final du morceau, utiliser live-export-wav.
---

# Resampling dans Ableton Live

## Cadre et outils

Lire `../ableton-live-session/SKILL.md` avant d'agir dans Live : outils disponibles, relecture, transport et sauvegarde. Appliquer ses conventions de travail, sauf instruction contraire de l'utilisateur. Utiliser les outils réellement disponibles : Producer Pal ou LOM Bridge pour les opérations exposées, contrôle d'écran pour les menus et l'enregistrement qui ne le sont pas. Ne pas inventer de méthode API ni de libellé de menu ; inspecter l'état actuel.

Ce skill produit une prise audio réutilisable et conserve la source. Il ne déclenche pas à lui seul un mixage ou un mastering. Pour charger la prise dans Simpler ou travailler son timbre, lire `../vst-sound-design/SKILL.md` au besoin ; pour livrer un fichier par export, lire `../live-export-wav/SKILL.md`.

## Choisir la capture

Déduire de la demande et du Set : source, plage musicale, effets à imprimer, usage final et besoin de queue. Demander uniquement les informations qui empêchent de choisir la bonne source ou la bonne plage.

- **Piste ou bus précis** : créer une piste audio alimentée par cette source. Choisir le point de capture d'après les traitements à conserver.
- **Pre FX** : signal audio avant les devices de la piste ; ne convient pas pour imprimer le son d'un instrument MIDI avant sa génération audio.
- **Post FX** : sortie des devices avant les réglages du mixer de la piste.
- **Post Mixer** : inclut les réglages du mixer de la piste source. Les traitements situés sur les bus en aval et les retours d'effets séparés ne sont pas automatiquement inclus.
- **Resampling** : capture la sortie Main. Vérifier tout ce qui l'alimente, notamment REF, retours, autres pistes et traitements du Main. Pour capturer un bus avant le Main, sélectionner ce bus comme source.

Ne pas isoler aveuglément une piste par Solo : un sidechain ou un retour peut dépendre d'autres pistes. Conserver les signaux de commande nécessaires et vérifier le résultat du routage. Pour inclure des effets en retour, identifier un point qui reçoit réellement leur somme avec le signal direct.

## Préparer et enregistrer

1. Relire le transport, la source, le routage, les clips actifs, la plage, le tempo, les solos/mutes, les armements et les retours. Noter les valeurs à rétablir. Annoncer toute interruption nécessaire de la lecture.
2. Créer une destination audio vide nommée, par exemple, `RESAMPLE - source - prise 01`. Conserver les clips et devices d'origine ; ne pas aplatir ou remplacer la source pour une simple capture.
3. Régler son entrée et son point de capture ; mettre son monitoring sur **Off** et ses envois à zéro pour cette capture. Vérifier l'absence de boucle de routage ou de double écoute. Désarmer les autres pistes qui risqueraient d'enregistrer, après avoir relevé leur état.
4. Choisir Session ou Arrangement selon la demande. En Arrangement, vérifier que la plage de destination est vide ; en Session, utiliser un slot vide. Inspecter la quantification, le décompte, la boucle et les points de punch qui pourraient modifier le début ou la fin.
5. Inspecter le format d'enregistrement et la fréquence du Set. Éviter de modifier les préférences globales pour cette seule opération. Ne pas normaliser automatiquement ni appliquer une cible LUFS de master à un sample.
6. Définir un début qui conserve l'attaque et, si nécessaire, une amorce pour les effets, le sidechain ou les notes tenues. Capturer la fin des delays/réverbs au-delà de la plage musicale ; distinguer la durée de boucle de la durée du fichier avec sa queue.
7. Armer uniquement la destination nécessaire et lancer l'enregistrement. Contrôler le signal et la progression sans bloquer Live avec une attente exécutée à l'intérieur du bridge. Arrêter à la fin prévue et désarmer la destination. Si la capture est vide ou provient de la mauvaise source, inspecter la cause avant une nouvelle prise ; garder les sources intactes.

## Préparer la prise pour son usage

- Conserver une prise brute et travailler sur une copie pour les transformations.
- **Boucle** : placer les bornes sur la grille voulue, examiner la jonction et protéger les attaques. Ne pas couper une queue audible pour obtenir mécaniquement un nombre entier de mesures ; utiliser un fondu ou une queue séparée selon l'intention.
- **One-shot** : préserver le transitoire, nettoyer seulement le silence superflu, ajouter de courts fondus si nécessaires et garder la décroissance utile.
- **Reverse / pitch / découpage** : appliquer seulement les transformations demandées et vérifier la durée, les limites et le gain après traitement.
- **Warp** : inspecter son état après création ou import. Pour une impression fidèle au tempo d'origine, éviter toute déformation involontaire ; pour une boucle à recaler, vérifier le tempo source, le premier temps et choisir le mode selon le matériau.
- **Réinsertion** : éviter de repasser une prise déjà traitée dans les mêmes effets de bus ou de Main. Ne pas laisser la source et sa copie jouer ensemble si l'objectif est un remplacement ; conserver la source désactivée et récupérable dans ce cas.

## Vérifier et terminer

Relire l'existence du clip et de son fichier, sa plage, sa durée, ses bornes de boucle, son Warp et son routage. Vérifier un signal non vide, les attaques, la queue et l'alignement ; ne pas compenser une latence supposée sans la mesurer. Si le fichier est accessible, mesurer ses crêtes, son RMS et rechercher un écrêtage avec `../live-export-wav/scripts/analyze_wav.py`, et sa hauteur avec `../synthese-reference/scripts/analyze_synth.py` : les vu-mètres seuls ne prouvent pas l'intégrité du fichier. Instantané des clips avant toute transformation de la source : `../memoire-projet/SKILL.md`.

Comparer à niveau cohérent si une comparaison est demandée. Sans écoute disponible, rapporter uniquement ce qui a été vérifié par état, forme d'onde ou mesure ; ne pas affirmer une qualité sonore entendue.

Rétablir les solos, mutes, armements et réglages temporaires, sauf ceux nécessaires au résultat demandé. Ne pas rétablir un armement susceptible de relancer un enregistrement tant que l'enregistrement global est actif. Sauvegarder selon le workflow de session. Indiquer la piste créée, la source et le point capturé, la plage et les transformations ; signaler les vérifications encore impossibles.

## Documentation de référence

Pour confirmer les points de capture ou un comportement dépendant de la version, consulter le [manuel Ableton : Routing and I/O](https://www.ableton.com/en/manual/routing-and-i-o/), notamment Resampling et Internal Routings. Pour les alternatives de rendu disponibles dans la version installée, consulter [Committing Audio in Live](https://help.ableton.com/hc/en-us/articles/22998838817820-Committing-Audio-in-Live). Ne pas supposer qu'une commande de bounce existe sur toutes les versions de Live 12.
