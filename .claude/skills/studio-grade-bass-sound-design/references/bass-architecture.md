# Architecture fonctionnelle des basses

## 1. SUB
Objectif : porter la fondamentale sans instabilité inutile.

[HEUR]
- sine ou triangle douce pour un sub propre ;
- mono / phase cohérente ;
- peu ou pas d'unison ;
- pas de reverb directe sauf effet voulu ;
- une saturation légère peut créer des harmoniques utiles, mais comparer à niveau égal.

Dans Serum 2, la source sub peut être routée `Direct` afin de contourner filtres/FX [DOC]. Dans Wavetable Ableton, Tone=0% sur le Sub donne une sine pure [DOC].

## 2. BODY
Objectif : rendre la note audible autour du grave supérieur/bas-médium et donner l'identité.

Sources [HEUR] : saw/square, wavetable, FM légère, sample court, layer resamplé. Le BODY peut être filtré, saturé et stéréo beaucoup plus librement que le vrai sub.

## 3. ATTACK
Objectif : rendre le début de note lisible et renforcer le groove. Ce n'est pas toujours nécessaire.

Solutions [HEUR] : enveloppe de filtre rapide, bruit court, pitch transient léger, click synthétique, transient shaper, sample layer.

## 4. MOTION
Objectif : faire de la basse une phrase et non une note statique.

Axes : cutoff, wavetable position, FM/ratio amount, drive, volume, pan du haut du spectre, formant/notch, feedback, FX mix.

Règle : un mouvement principal fort vaut mieux que cinq modulations aléatoires [HEUR].

## 5. AIR/SPACE
Objectif : largeur, sensation de pièce, delay, texture et tail. Ne doit pas brouiller la propriété du sub.

Créer sur layer haut, send ou piste resamplée. High-pass/low-cut le retour si nécessaire [HEUR].

## Architecture recommandée pour Bass House

`SUB CLEAN` + `MID CHARACTER` + éventuellement `ATTACK/NOISE`.

Le SUB suit les notes et le sidechain. Le MID CHARACTER fournit growl/reese/metal/format. Pour les réponses complexes, partager un sub commun ou alterner les basses plutôt que superposer plusieurs sub layers [HEUR].
