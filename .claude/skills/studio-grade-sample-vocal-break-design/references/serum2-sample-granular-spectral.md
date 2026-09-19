# Serum 2 — Sample / Granular / Spectral for Vocal & Break FX

## [DOC] Sample oscillator
Serum 2 peut lire un sample, le pitcher, le boucler et le transformer. La présentation officielle décrit aussi :
- snap loop detection ;
- modulation des boucles ;
- Rate pour des effets type tape-stop ;
- slicing avec extraction/lecture de score ;
- tails mode.

### [HEUR] Vocal shot
Sample osc = bon choix lorsque le shot doit rester reconnaissable mais être déclenché/pitché/modulé comme un instrument.

## [DOC] Granular
Granular découpe le matériau en grains et permet stretch/réarrangement/modulation. En mode Manual, le playhead ne scanne pas automatiquement : la position peut être automatisée/modulée. `Loop Grains` respecte les loop markers.

### [HEUR] Break texture
Dupliquer le vocal :
- couche dry lisible ;
- couche Granular en arrière-plan ;
- scanner lentement une voyelle ;
- high-pass de la couche texture ;
- automatiser WIDTH/SPACE plutôt que noyer la couche principale.

## [DOC] Spectral
Le moteur Spectral resynthétise le sample au niveau spectral et utilise un traitement de transients de type avancé pour remodeler temps et fréquences.

### [HEUR]
Réserver Spectral aux transformations où l'on accepte que l'identité de la voix devienne texture/harmonie.

## [DOC] Routing
Les OSC peuvent être envoyés vers Filter, Main, Direct ou None, plus BUS 1/2. Cela permet de conserver une couche dry/directe et de traiter une autre couche fortement.
