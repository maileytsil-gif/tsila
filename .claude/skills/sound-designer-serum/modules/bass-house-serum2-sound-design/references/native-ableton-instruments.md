# Instruments natifs Ableton Live 12 — choix documenté par architecture

Source principale : https://www.ableton.com/en/manual/live-instrument-reference/

## Operator [DOC]
Quatre oscillateurs multi-formes peuvent se moduler en fréquence selon plusieurs algorithmes. Operator combine FM, synthèse additive/soustractive, filtre, LFO, enveloppes par oscillateur, pitch et filtre. Choisir lorsque la relation harmonique/FM ou des enveloppes indépendantes sont centrales : plucks digitaux, keys FM, cloches, transients, basses.

## Drift [DOC]
Synthétiseur soustractif à faible charge avec deux oscillateurs, bruit, filtre, deux enveloppes, Cycling Envelope, LFO et destinations de modulation. Son LFO propose notamment Saw Up/Down et des formes d'enveloppe one-shot. Choix direct pour synthés simples, stabs, plucks et risers.

## Wavetable [DOC]
Deux oscillateurs wavetable, sub, deux filtres et système de modulation avec enveloppes/LFO. Le mouvement dans une table produit une évolution de timbre continue. Choisir pour synthés, pads, nappes et timbres dont la trajectoire spectrale est centrale.

## Meld [DOC]
Deux moteurs polyphoniques indépendants, chacun avec filtres, enveloppes, LFO et matrice MIDI/MPE. Les macros dépendent du moteur sélectionné. Choisir pour pads, nappes et timbres hybrides/bi-timbraux.

## Analog [DOC]
Deux oscillateurs + bruit, deux filtres multimodes, deux amplis, enveloppes et LFO avec routage série/parallèle. Choisir pour stabs, synthés et pads analogiques classiques.

## Electric [DOC]
Piano électrique modélisé physiquement, avec Hammer, Fork/Tine/Tone, Pickup et Damper. Choix principal pour keys de type electric piano lorsque le comportement instrumental doit répondre au jeu.

## Collision [DOC]
Mallet et Noise excitent jusqu'à deux resonators ; les résonateurs définissent l'essentiel du caractère. Choix intéressant pour plucks, mallets, bells et keys percussifs. Les fortes résonances peuvent produire de grands écarts de niveau : valider à bas niveau.

## Tension [DOC]
Modèle physique de corde avec exciter (bow, hammer, bouncing hammer, plectrum), damper, string, termination, pickup/body et filtre. Choix pour plucks et keys à comportement de corde.

## Simpler [DOC]
Trois modes de lecture dont Classic, One-Shot et Slicing. One-Shot est monophonique ; avec Trigger, le sample continue après le relâchement de la note. Choix direct pour stabs et impacts audio.

## Sampler [DOC]
Multisampling, zones, modulation interne profonde et mappings. Choix pour keys/multisamples complexes ou couches à plusieurs vélocités/notes.

## Drum Sampler [DOC]
Instrument one-shot pour Drum Racks, avec AHD, pitch, filtre, modulation et playback effects : Stretch, Loop, Pitch Env, Punch, 8-Bit, FM, Ring Mod, Sub Osc, Noise. Choix très efficace pour impacts/transients construits à partir d'un sample.

## Granulator III [DOC]
Instrument granular Live 12 avec capture temps réel, modes Classic/Loop/Cloud et MPE. Ableton indique que la technique se prête aux pads/textures et que Cloud convient aux drones/textures expérimentales. Choix pour nappes, drones, pads, risers et transformation de samples.

## Instrument Rack [DOC]
Chaînes parallèles d'instruments/effets et jusqu'à 16 Macro Controls. Utiliser pour réunir des couches ayant des fonctions différentes et exposer une interface réduite au bridge.

## Règle de sélection [HEUR]
- simple/soustractif → Drift/Analog ;
- FM/digital → Operator ;
- wavetable évolutif → Wavetable ;
- hybride/bi-timbral → Meld ;
- electric piano → Electric ;
- mallet/string physique → Collision/Tension ;
- one-shot → Drum Sampler/Simpler ;
- multisample → Sampler ;
- granular/textural → Granulator III.
