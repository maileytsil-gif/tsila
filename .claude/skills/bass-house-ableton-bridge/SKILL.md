---
name: bass-house-ableton-bridge
description: Traduire un plan musical en opérations structurées et sûres pour Ableton Live 12, Serum 2 et un bridge LOM/MCP, notamment pistes, clips MIDI, devices, paramètres, macros, automation et modulation. Utiliser quand l'utilisateur demande une exécution ou un plan machine ; exiger découverte des capacités, validation, lecture de contrôle et sauvegarde non destructive.
---

# Ableton Live / LOM / MCP Bridge — v18 Integration Contract

Transformer une intention musicale en modifications **reproductibles, observables et annulables**. Le bridge ne doit jamais prétendre qu'une capacité existe avant de l'avoir découverte dans le Live Set et la version installée.

## Documentation requise

Lire `references/documentation-map.md`, `references/capability-matrix.md`, `references/execution-protocol.md`, `references/ableton-automation-model.md`, `references/vst-control.md` et `references/machine-validation.md`. Le schéma d'actions est dans `references/action-schema.md`.

## Règles critiques [DOC]

- Le Live Object Model n'expose pas nécessairement tout ce que l'interface de Live sait faire. L'absence d'une propriété/méthode doit être traitée comme une capacité manquante, pas contournée par invention.
- Les **IDs LiveAPI sont dynamiques** et ne doivent pas être conservés comme identifiants persistants entre les exécutions/sessions. Rechercher les objets par chemin/contexte/signature puis confirmer l'ID actuel.
- `LiveAPI`/`live.object` conviennent à l'inspection et aux changements de propriétés, mais le contrôle temps réel haute résolution d'un `DeviceParameter` relève d'autres mécanismes comme `live.remote~` lorsqu'ils sont appropriés.
- `live.remote~` prend le contrôle d'un paramètre en temps réel ; sa relation avec l'automation/contrôle normal de Live impose une gestion explicite. Libérer le contrôle en remettant son id à 0 lorsqu'il n'est plus nécessaire. Ne pas confondre sa valeur temporaire avec une valeur stockée dans le Set ou une écriture d'automation.
- Node for Max s'exécute comme processus Node séparé et communique de façon asynchrone. Toute architecture réseau/MCP doit utiliser request IDs, timeouts, gestion des réponses tardives et arrêt propre.
- Pour les VST/AU, Live ne peut configurer/automatiser que les paramètres réellement publiés par le plug-in à l'hôte. Le nom visible dans l'UI du plug-in ne garantit pas une adresse accessible.

## Autorisation et sûreté

- Une demande d'analyse n'autorise aucune mutation.
- Avant un gros changement, travailler sur copie/version du Set ou exiger sauvegarde.
- Pas de suppression, flatten, freeze destructif, remplacement de piste ou écrasement de clip sans autorisation explicite.
- Capturer l'état utile avant mutation : tempo/signature, pistes/chaînes ciblées, clips, devices, valeurs de paramètres et état d'automation.
- Les actions doivent être petites, idempotentes si possible, identifiées par request ID et suivies d'une lecture de contrôle.
- Après erreur répétée, timeout ambigu, objet disparu ou état incohérent : **stop**, rediscover, ne pas continuer aveuglément.

## Pipeline obligatoire

1. **Discover** — versions Live/Max/bridge, Set actif, capacités, objets LOM, paramètres hôte exposés, min/max/unités et état d'automation.
2. **Resolve** — convertir les cibles humaines (`track="Bass A"`, `device="Serum 2"`, macro `BITE`) en cibles actuelles vérifiées. Ne jamais se fier au seul index si l'ordre peut changer.
3. **Plan** — produire un manifeste avec préconditions, mutations, postconditions, rollback et niveau de risque.
4. **Dry run** — résoudre toutes les cibles sans écriture ; pour une opération importante, montrer le résumé avant exécution si le workflow l'exige.
5. **Execute** — transaction logique courte ; journaliser request ID, cible, ancienne/nouvelle valeur et résultat.
6. **Verify** — relire depuis Live, pas seulement depuis le cache du bridge. Pour une automation, vérifier plage temporelle/points/cible ; pour un clip, notes/durées/pitches ; pour audio, compléter par écoute/export.
7. **Release/Cleanup** — libérer remote controls, timers, observers et ressources Node ; invalider les handles qui ne doivent pas survivre au contexte.
8. **Report** — exact changes, unchanged items, warnings, failed actions, rollback status et éléments [TEST] restant à écouter.

## Trois opérations à ne jamais confondre

1. **Set value** : modifier une valeur actuelle de paramètre.
2. **Realtime modulation/control** : faire varier un paramètre pendant la lecture, par exemple via `live.remote~`.
3. **Persistent automation** : écrire des données d'automation éditables/stokées dans Live lorsque l'API/méthode supportée le permet.

Une démonstration réussie du n°1 ne prouve ni le n°2 ni le n°3.

## VST/Serum 2

Privilégier : paramètres publiés à l'hôte → paramètres configurés dans Live → macros d'Instrument Rack stables. Pour des tâches complexes de sound design, exposer en amont des macros d'intention (`BITE`, `MOTION`, `WIDTH`, etc.) est plus robuste que dépendre de centaines d'indices de paramètres. Toujours redécouvrir l'exposition réelle sur l'instance concernée.

## Critère de fin

Une action est terminée uniquement lorsque **l'état relu** satisfait la postcondition et que les ressources temporaires ont été nettoyées. Une action audio n'est artistiquement validée qu'après écoute/mesure appropriée ; un succès API signifie « modification appliquée », pas « son meilleur ».


## Contrats v18
Le bridge accepte de préférence un `BridgeActionBatch` validé par `../core/schemas/bridge-action-batch.schema.json`. La source de vérité musicale est l'`AbletonClipPlan`; le batch n'est qu'un plan de mutations.

Chaque action porte `requires_capability`. Une action compilée ne doit pas être exécutée si la capability matrix de la session n'est pas `SUPPORTED` ou explicitement gérée en fallback.

### Compiler boundary
`core/compiler/compile_project.py` ne commande pas Live. Il prépare les actions. Le bridge reste responsable de `Discover/Resolve/Snapshot/Dry Run/Execute/Verify/Cleanup`.
