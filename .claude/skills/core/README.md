# v18 Core Integration Layer

La v18 ajoute un **control plane** au-dessus des skills existants sans casser leur installabilité individuelle.

## Contrats
`ProductionBrief → CulturalStyleLock → GrooveSpec / HarmonySpec / BassInterlockSpec / SoundSpec / AutomationSpec → AbletonClipPlan → BridgeActionBatch`.

Le compilateur produit des plans machine lisibles et validables. Il **n'exécute pas Ableton** : le bridge réel doit encore `Discover → Resolve → Dry Run → Execute → Verify → Rollback/Cleanup`.

## Principe de séparation
- théorie/groove = **quoi jouer et quand** ;
- sound design = **comment le son est fabriqué** ;
- mix = **comment les éléments coexistent** ;
- bridge = **comment appliquer une décision dans Live**.

Une skill de sound design ne doit donc pas modifier silencieusement le rythme d'un `GrooveSpec` ou les notes d'un `HarmonySpec`.
