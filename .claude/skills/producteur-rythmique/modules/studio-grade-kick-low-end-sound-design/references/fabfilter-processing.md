# FabFilter — usages ciblés

## Pro-Q 4 [DOC]

Pro-Q 4 propose EQ paramétrique, Dynamic EQ, Spectral Dynamics, Character et analyseur. Utilisations kick :
- diagnostiquer résonance/body trop long ;
- atténuation dynamique plutôt qu'une encoche statique si le problème n'existe que pendant le tail ;
- nettoyer un rumble sans retirer la masse du kick sec.

## Pro-C 3 [DOC]

Le sidechain avancé permet source externe, level/linking et EQ du détecteur. Pour ducking basse/rumble :
- external sidechain depuis kick ;
- ajuster attack/release pour créer un trou temporel suffisant, puis réduire jusqu'au minimum efficace [HEUR].

## Saturn 2 [DOC]

Saturation/distortion multibande avec Mix, Feedback, Dynamics, Style, Tone et Level par bande ; modulation possible. HQ/Superb réduisent l'aliasing au prix de CPU.

### Usage kick [HEUR]
- sub band : faible drive ou dry majoritaire ;
- body/mids : plus de drive pour traduction ;
- click : traiter seulement s'il manque de caractère.

Comparer les crossovers et la phase à l'écoute, notamment si le kick est extrêmement court [TEST].

## Pro-L 2 [DOC]

Limiter True Peak avec oversampling. Dans ce skill, Pro-L 2 sert à protéger un print/bus ou à contrôler les crêtes finales, pas à « fabriquer » le punch. FabFilter recommande l'oversampling pour réduire aliasing et inter-sample peaks, avec coût CPU.
