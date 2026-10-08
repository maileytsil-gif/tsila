# Session commune pour produire un morceau entier

Ce protocole s'applique à Claude et à ChatGPT avec le même Set et le même LOM Bridge. Il ne prétend pas que le bridge 0.8 crée déjà un morceau de zéro : la création des pistes, des clips d'arrangement, l'édition complète des plug-ins tiers et l'export nécessitent encore un opérateur dans Live ou un contrôle d'écran vérifié.

## Préparer le Set

1. Travailler sur une **copie** du Set et noter son chemin, sa version de Live, le tempo, la signature et le nombre de pistes. Garder un original intact.
2. Créer dans Live les pistes, clips MIDI/audio et emplacements nécessaires à l'arrangement. Nommer les pistes et placer des locators par section (intro, couplet, build, drop, outro). Sauvegarder cette copie comme point de départ commun.
3. Chaque agent démarre par `python3 lom.py ping`, `python3 lom.py state --json`, `python3 lom.py locators`, puis `python3 lom.py clips <piste>` sur ses pistes cibles. Conserver ces résultats avec l'heure et le nom du Set.
4. Convenir d'un manifeste musical unique : BPM, tonalité, durée en mesures, sections, pistes, sources sonores, références et critères d'écoute. Les deux agents reçoivent **le même manifeste et la même copie initiale**, chacun travaillant ensuite sur sa propre copie.

## Exécution par sections

Pour chaque section : écrire d'abord les notes avec `/notes`, ensuite les réglages simples avec `/setparam`, puis les automations avec `/plan` et `/shape`. Utiliser `/load` seulement après avoir identifié une source et un nom sans ambiguïté. Après chaque commande d'écriture, contrôler `ok`, `errors`, `codes` et les lignes de réponse ; relire `/notes get`, `/param` ou `/read` selon l'opération. Enregistrer un checkpoint du Set après chaque section terminée et écoutée.

Ne pas traiter `verified … interrupted`, `E_TIMEOUT`, « état du Set incertain », ou « vérifier et Cmd+Z » comme une réussite. Arrêter les écritures, inspecter Live et le journal, puis décider humainement si l'opération a abouti avant de reprendre. Ne jamais relancer aveuglément une écriture après un timeout : une commande peut avoir été appliquée avant la perte de réponse. Éviter toute intervention simultanée de Claude, ChatGPT ou de l'utilisateur sur le même Set pendant une opération du bridge.

Une étape `/load` qui signale une modification inattendue exige une vérification visuelle : son contrôle de « l'autre piste » ne compare que les **nombres** de devices. Une étape `/shape` qui exige `accept=unverified`, `fades`, `warp` ou `expressions` doit consigner exactement l'approximation acceptée. Éviter ces acceptations tant que les tests de la version courante n'ont pas tourné dans Live.

## Critères pour livrer le morceau

- Toutes les sections prévues sont présentes et écoutées ; les clips et locators couvrent l'arrangement annoncé.
- Les réponses du bridge et les relire MIDI/automation ne contiennent aucune erreur non résolue ni vérification interrompue.
- Le mix est contrôlé à l'écoute et aux meters sur les sections clés ; ces crêtes ne constituent pas à elles seules une mesure de loudness, de clipping intersample ou de qualité de mastering.
- Sauvegarder, fermer et rouvrir le Set, vérifier les plug-ins et les parties clés, puis exporter depuis Live et écouter le fichier exporté. Le bridge 0.8 ne commande pas cet export.

## Essais Live avant une session autonome

Rejouer `tests/live_suite.py` dans une copie jetable avec le Remote Script correspondant à ce commit. Vérifier surtout le rollback d'un ajout MIDI partiel, le comportement d'une étape d'annulation vide, `end_undo_step`, la duplication d'un clip et `/load` selon la sélection. Les tests hors Live contrôlent la logique du code, pas ces garanties de Live.
