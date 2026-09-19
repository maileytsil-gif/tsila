# Validation sur la machine — ordre de test

Ce protocole transforme une architecture théorique en capacité réellement prouvée.

## Phase A — versions et environnement
- relever macOS, Live, Max, Node for Max, Serum 2, format VST3/AU et version du bridge ;
- ouvrir une copie de Set minimal ;
- désactiver toute exécution automatique non nécessaire.

## Phase B — lecture seule
- lister 1 piste, 1 device, paramètres ;
- changer de piste puis vérifier que la résolution logique suit ;
- recharger le Set et vérifier que les IDs ne sont pas réutilisés aveuglément.

## Phase C — une valeur
- choisir un paramètre natif non critique ;
- snapshot → set → readback → restore → readback ;
- provoquer volontairement une mauvaise cible et vérifier que le bridge refuse.

## Phase D — Serum publié
- charger une instance test ;
- configurer/exposer un seul paramètre ou macro ;
- discovery → set → readback → restore ;
- sauvegarder/recharger et vérifier la stratégie de résolution.

## Phase E — temps réel
- tester `live.remote~` sur un paramètre non dangereux ;
- mouvement lent d'abord ;
- observer interaction avec automation ;
- libérer avec id 0 et confirmer retour au contrôle normal.

## Phase F — automation persistante
- uniquement si une méthode supportée a été identifiée ;
- écrire une courte enveloppe sur une cible test ;
- vérifier visuellement/programmatiquement, sauver/recharger si la persistance est revendiquée ;
- distinguer clairement ce test du remote control.

## Phase G — charge et erreurs
- timeout volontaire ;
- réponse tardive ;
- suppression du device pendant une requête ;
- changement de Set ;
- STOP puis redémarrage.

Le bridge n'est « prêt production » que quand les cas d'erreur échouent proprement et que le rollback/readback sont fiables.
