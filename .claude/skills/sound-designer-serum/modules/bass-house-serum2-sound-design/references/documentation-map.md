# Carte documentaire — Sound Design

| Règle | Type | Source | Conséquence pratique |
|---|---|---|---|
| Serum 2 : OSC A/B/C avec plusieurs moteurs | DOC | Manuel Xfer Serum 2 | Choix du moteur par fonction, pas seulement wavetable |
| Routing sources/filtres/bus | DOC | Manuel Xfer — routing | Architectures série/parallèle et directes contrôlées |
| Matrix riche en sources/destinations | DOC | Manuel Xfer — Matrix | Macros/modulations explicites |
| ARP et CLIP intégrés | DOC | Manuel Xfer | Séquences internes à distinguer du MIDI de Live |
| Pitch tracking variable selon moteur | DOC | Xfer pitch tracking | Ne pas supposer une note fixe universelle |
| Limiter l'unison inutile | DOC | Xfer CPU guideline | Contrôle CPU/phase |
| Operator/Drift/Wavetable/Meld/Analog structures | DOC | Live 12 Instrument Reference | Choix du synthé natif selon architecture |
| Granulator III inclus dans Suite et orienté granular/MPE | DOC | Ableton Granulator III | Textures/resampling, pas sub par défaut |
| « sub = sine, mono, une voix » | HEUR | pratique de production | Point de départ robuste, à tester |
| Macro `BITE`, `MOTION`, etc. | HEUR | architecture de contrôle | Convention de nommage, non fonctionnalité officielle Serum |
| Paramètre Serum accessible au bridge | TEST | Live + plug-in installé | Découverte hôte obligatoire |

## Sources principales

- https://xferrecords.com/manual/serum-2/docs
- https://xferrecords.com/web-manual/serum-2/welcome
- https://support.xferrecords.com/article/51-serum2-sound-design-guidelines-for-optimizing-cpu-usage
- https://support.xferrecords.com/article/59-converting-samples-to-wavetables
- https://support.xferrecords.com/article/57-automatic-sample-root-note-mapping
- https://support.xferrecords.com/article/52-serum-2-preset-previews
- https://www.ableton.com/en/live-manual/12/live-instrument-reference/
- https://www.ableton.com/en/packs/granulator-iii/

## Extension v4

Pour synthé, nappe, drone, stab, riser, impact, pluck, pad et keys, consulter `sound-family-documentation-map.md`, `sound-family-index.md` et le fichier de famille correspondant dans `sound-families/`.
