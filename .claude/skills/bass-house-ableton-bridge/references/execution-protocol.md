# Protocole d'exécution sûre

## 1. Handshake

Collecter versions Live/Max/device/bridge, identité du Set, tempo, signature et statut transport. Établir une `session_id` et une version de protocole. Ne pas réutiliser silencieusement une session après reload/changement de Set.

## 2. Discovery

Énumérer uniquement ce qui est requis. Pour chaque cible, obtenir : chemin logique, nom, classe/type, position courante, ID LiveAPI courant si utilisé, et une petite empreinte (ex. nombre de paramètres + noms clés) pour détecter les décalages.

**Important [DOC]** : un ID LiveAPI ne devient pas un identifiant persistant. Stocker le chemin/signature de résolution et redécouvrir l'ID.

## 3. Snapshot

Avant mutation : capturer la valeur ou structure qui sera touchée. Pour un changement multi-paramètres, snapshotter le groupe complet nécessaire au rollback, pas tout le Set.

## 4. Plan

Chaque action doit avoir :
- `request_id` ;
- cible logique ;
- précondition ;
- opération ;
- ancienne valeur attendue si connue ;
- nouvelle valeur ;
- postcondition ;
- rollback ;
- timeout ;
- impact (`low`, `medium`, `high`).

## 5. Execute

Envoyer une petite transaction. Un timeout signifie **état inconnu**, pas « échec certain » : la commande peut avoir été appliquée après l'expiration côté client.

Donc, après timeout : ne pas renvoyer immédiatement une mutation non idempotente. Relire d'abord l'état et décider si retry est nécessaire.

## 6. Late responses

Avec Node/HTTP/MCP asynchrone, une réponse tardive doit être associée à son `request_id`. Si la transaction a été invalidée/annulée, la réponse ne doit pas déclencher une nouvelle mutation ni écraser le statut courant.

## 7. Verify

La réussite vient de Live : readback de l'objet/paramètre/clip. Pour une séquence temps réel, vérifier début, évolution et **release/cleanup**. Pour automation persistante, recharger/relire si le test doit prouver la persistance.

## 8. Rollback

Si une postcondition échoue et que le rollback est sûr, restaurer snapshot puis relire. Si le rollback lui-même échoue : arrêter et produire un rapport, ne pas poursuivre les actions dépendantes.

## 9. Cleanup

Retirer observers/timers temporaires ; libérer `live.remote~` ; arrêter proprement les tâches Node ; invalider handles/IDs de session.
