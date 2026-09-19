# Serum 2 — base vérifiée

Révision documentaire : 2026-09-19. Le manuel Web trouvé indique Serum 2 v2.0.18 / Manual 1.0.3, 27 avril 2025. **Ne pas confondre cette version documentée avec la version réellement installée.**

## Architecture principale [DOC]

- Trois oscillateurs principaux : **A, B, C**.
- Moteurs documentés : **Wavetable, Multisample, Sample, Granular, Spectral**.
- Sources additionnelles : SUB et NOISE.
- Deux filtres et routage flexible ; les sources disposent d'options de destination qui permettent notamment des chemins vers filtre/main/direct selon le contexte.
- Effets avec possibilités de bus/routage plus flexibles que Serum 1.
- Matrix pour les relations source→destination.
- Modules intégrés **ARP** et **CLIP**.

Source racine : https://xferrecords.com/manual/serum-2/docs

## Matrix [DOC]

La Matrix documente un ensemble étendu de sources de modulation : LFO/enveloppes/macros, sources liées aux notes/voix, aléatoire, vélocité et dimensions expressives/MPE selon les entrées disponibles. Conséquence : avant d'ajouter un LFO, vérifier si une source d'expression plus pertinente existe.

## CLIP [DOC]

CLIP contient des emplacements de séquence/pattern et des réglages de key/scale/piano-roll. Il peut participer à une preview de preset personnalisée. Ne pas confondre :
- le clip interne Serum ;
- un MIDI Clip Ableton ;
- une automation Arrangement.

## ARP [DOC]

L'ARP possède des patterns/banques et des paramètres de lecture, transposition, retrigger, vélocité, gate/chance/swing selon la version documentée. Si le groove doit rester éditable dans Live, décider explicitement si l'arpège vit dans Serum ou dans le MIDI du DAW.

## Pitch tracking [DOC]

Le tracking de hauteur peut être désactivé. Xfer documente des références différentes selon le moteur lorsqu'il est désactivé ; ne jamais généraliser un comportement de Wavetable aux moteurs Sample/Granular/Spectral. Pour des échanges reproductibles, noter le **numéro MIDI** en plus du nom de note.

## Samples → Wavetable [DOC]

Xfer propose une conversion de sample en wavetable avec estimation de fréquence et conseille des sources harmoniquement lisibles. Un enregistrement complexe peut produire un résultat moins prévisible. Cette conversion est non destructive vis-à-vis du fichier source ; elle n'est pas une séparation de sources.

Source : https://support.xferrecords.com/article/59-converting-samples-to-wavetables

## Root note mapping [DOC]

Serum 2 peut exploiter une note placée dans le nom du sample pour la note racine. Xfer utilise dans cette documentation une nomenclature où MIDI 69 = A3 = 440 Hz ; d'autres environnements nomment cette hauteur A4. Conserver MIDI 69 comme repère non ambigu.

Source : https://support.xferrecords.com/article/57-automatic-sample-root-note-mapping

## CPU [DOC]

Les voix d'unison ont un coût. Xfer recommande de ne pas en multiplier inutilement et indique qu'un chorus sur un bus peut parfois fournir de la largeur avec moins de voix. Pour un patch : augmenter l'unison uniquement si l'A/B apporte un bénéfice audible.

Source : https://support.xferrecords.com/article/51-serum2-sound-design-guidelines-for-optimizing-cpu-usage

## Compatibilité [DOC]

Serum 2 accepte les presets Serum 1 ; l'inverse n'est pas promis. Les projets contenant Serum 1 ne sont pas automatiquement transformés en instances Serum 2. Ne pas migrer un projet historique sans sauvegarde et test.

Source : https://support.xferrecords.com/article/58-how-to-upgrade-from-serum-1-to-serum-2
