# Templates de macros — v5

## Règle

Une macro doit décrire une **intention musicale**, pas simplement le nom interne d'un paramètre. Les plages doivent rester sûres et utiles sur toute la course.

[DOC] Serum 2 offre 8 macros ; les Racks Live peuvent afficher jusqu'à 16 macros et mapper plusieurs paramètres avec plages Min/Max.

## Palette standard

- `TONE` : luminosité/équilibre spectral ;
- `MOTION` : profondeur de modulation ;
- `ATTACK` : dureté/temps d'attaque ;
- `DECAY` : durée du corps ;
- `WIDTH` : largeur, jamais comme unique solution de présence ;
- `SPACE` : send/dry-wet espace ;
- `EDGE` : saturation/hautes harmoniques ;
- `TEXTURE` : dosage granular/noise/spectral ;
- `TENSION` : combinaison contrôlée de pitch/filter/drive/feedback pour FX ;
- `SIZE` : durée/room/resonance d'un impact ou d'une nappe ;
- `SOFT↔HARD` : vélocité/timbre d'un key ;
- `CORE↔AIR` : balance corps/couche haute.

## Mapping recommandé [HEUR]

### Pad / nappe
`TONE`, `MOTION`, `TEXTURE`, `WIDTH`, `SPACE`, `ATTACK`, `RELEASE`, `AIR`

### Pluck / stab
`BITE`, `DECAY`, `TONE`, `BODY`, `WIDTH`, `SPACE`, `EDGE`, `VELOCITY RESPONSE`

### Riser
`RISE`, `TENSION`, `BRIGHTNESS`, `DENSITY`, `PULSE`, `WIDTH`, `SPACE`, `DISTORT`

### Impact
`HIT`, `BODY`, `LOW`, `METAL`, `TAIL`, `SIZE`, `DISTORT`, `DRY↔WET`

### Keys
`SOFT↔HARD`, `TONE`, `BELL`, `BODY`, `TREMOLO`, `WIDTH`, `SPACE`, `NOISE`

## Bridge

[TEST] Le fait qu'une macro existe dans Serum ou un Rack ne prouve pas qu'elle est correctement exposée et pilotable par le bridge. Faire une découverte des paramètres, écrire une valeur, relire la valeur et restaurer avant d'automatiser.
