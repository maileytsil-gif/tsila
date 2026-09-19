---
name: composer-producer-director
description: Orchestrateur conditionnel v18 pour Pop/Electro/House/Techno/Jazz/Chill/Afro/Latin/Caribbean/Detroit. Route un brief vers les skills spécialisés, produit des contrats structurés, compile un AbletonClipPlan puis un BridgeActionBatch vérifiable. Utiliser pour morceau complet, direction de production ou exécution Live. Ne remplace pas les skills spécialistes.
---

# Composer / Producer Director — v18 Technical Integration

## Principe
Le Director n'est plus une chaîne fixe. Il sélectionne un **graphe de production conditionnel** dans `../core/index/director-graph.json`.

Contrat principal :
`ProductionBrief → Specs spécialisés → AbletonClipPlan → BridgeActionBatch → Bridge Discover/Resolve/Verify`.

Lire `../core/README.md`, `../core/index/capability-index.json` et les schemas dans `../core/schemas/`.

## Branches

### Default electronic
`IDENTITY → THEORY → GROOVE_LOW_END → DRUMS → SIGNATURE_SOUND → ARRANGEMENT → TRANSITIONS → MIX → BRIDGE → VALIDATE`.

### Afro / Latin / Caribbean
**Le style lock précède l'harmonie finale** :
`IDENTITY → CULTURAL_STYLE_LOCK → GROOVE_SPEC → PERCUSSION_ROLES → BASS_INTERLOCK → HARMONY_OSTINATO → SIGNATURE_SOUND → ARRANGEMENT → TRANSITIONS → MIX → BRIDGE → VALIDATE`.

### Detroit
`IDENTITY → DETROIT_STYLE_LOCK → MACHINE_GRID → BASS_STAB_INTERLOCK → HARMONIC_COLOR → MUTATION_SYSTEM → SIGNATURE_SOUND → ARRANGEMENT → TRANSITIONS → MIX → BRIDGE → VALIDATE`.

### Jazz / Chill
`IDENTITY → HARMONIC_POCKET_LOCK → GROOVE_SPEC → BASS_KEYS_INTERLOCK → MELODY_PHRASING → SIGNATURE_SOUND → ARRANGEMENT → TRANSITIONS → MIX → BRIDGE → VALIDATE`.

## Contrats obligatoires v18
- `ProductionBrief` : brief et contraintes.
- `CulturalStyleLock` : axe principal/secondaire, principe emprunté et traduction électronique.
- `GrooveSpec` : timing musical, rôles, vélocité, articulation, microtiming.
- `BassInterlockSpec` : fonctions ANCHOR/ANTICIPATION/RESPONSE/GHOST/HOLD.
- `HarmonySpec` : accords/voicings exacts séparés du timbre.
- `SoundSpec` : rôle sonore, moteur, macros, intention de traitement.
- `AutomationSpec` : lanes d'intention et type de persistance.
- `AbletonClipPlan` : représentation DAW-agnostic proche de Live.
- `BridgeActionBatch` : opérations conceptuelles soumises aux capacités du bridge.

## Règle de propriété
Un skill ne modifie pas silencieusement un contrat appartenant à un autre domaine :
- theory/groove décide **quoi/quand** ;
- sound design décide **timbre** ;
- mix décide **coexistence** ;
- bridge décide **application technique vérifiée**.

Si Sound Design veut modifier le rythme, il produit une proposition de patch du `GrooveSpec`; il ne l'applique pas automatiquement.

## Cultural / Style Lock
Pour Afro/Latin/Caribbean, appeler `afro-caribbean-latin-detroit-theory` avant la progression définitive. Produire un `GrooveSpec` et vérifier `data/hybridization/hybridization-matrix.json`.

Pour Detroit, traiter `machine grid + mutation + bass/stab interlock` comme noyau avant d'ajouter une progression pop.

## Compilation
Lorsque le noyau est validé, compiler :
`GrooveSpec + BassInterlockSpec + HarmonySpec + AutomationSpec → AbletonClipPlan → BridgeActionBatch`.

Le script `../core/compiler/compile_project.py` sert de référence exécutable. Il **ne commande pas Live**.

## Bridge
Une action compilée a un `requires_capability`. Le bridge doit encore :
`Discover → Resolve → Snapshot → Dry Run → Execute → Readback → Cleanup`.

Si `ensure_track`, `write_notes`, `automation_persistent` ou autre capacité est `UNKNOWN/UNSUPPORTED`, arrêter ou utiliser un fallback explicitement autorisé. Ne jamais masquer un fallback `set_value` sous le nom d'automation persistante.

## Validation
Avant exécution : JSON Schema + invariants musicaux + provenance.
Après compilation : dépendances d'actions + note ranges + clip lengths.
Après Live : readback réel + écoute `[TEST]`.

## Sortie standard v18
1. Creative North Star
2. Branch sélectionnée + raison
3. Hypothèses `[HEUR]`
4. ProductionBrief
5. Specs produits/à produire
6. Invariants (hook, groove, low-end, culture/style)
7. AbletonClipPlan summary
8. Bridge capability requirements
9. Validation pass/fail/unknown
10. Next 3 Actions
