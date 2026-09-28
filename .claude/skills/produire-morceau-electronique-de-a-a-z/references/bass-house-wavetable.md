# Wavetable dans Live 12 : applications Bass House

Références vérifiées : [manuel officiel, section 31.13](https://www.ableton.com/en/manual/live-instrument-reference/#wavetable), [pads évolutifs](https://www.ableton.com/fr/blog/pad-it-out-10-ways-make-distinctive-pad-sounds/), [charge CPU](https://help.ableton.com/hc/en-us/articles/360000036930-Managing-CPU-load-when-using-Wavetable).

## Architecture et réglage

- Deux oscillateurs wavetable principaux; déplacer leur **position** change le timbre, pas la note. Commencer avec un seul et écouter les positions avant d'ajouter un second.
- Sous-oscillateur : **Tone 0 %** donne une onde sinusoïdale; monter Tone ajoute des harmoniques. Comparer avec un sub sur piste séparée pour garder un contrôle indépendant.
- Deux filtres et un onglet **Matrix**; l'onglet **Mod Sources** contient l'enveloppe Amp, Env 2, Env 3 et deux LFO. Assigner explicitement Env 2 au cutoff pour une attaque de pluck; l'enveloppe Amp règle sa longueur audible.
- Dans Matrix, moduler la position de table et le cutoff avec des quantités distinctes. Pour un wobble, choisir un LFO synchronisé au tempo; tester Retrigger activé pour une attaque répétable, désactivé pour un mouvement continu. Le mouvement de table seul peut être faible si les formes adjacentes sont proches : écouter puis choisir une autre table ou élargir la plage.
- Mono + Glide pour une basse/lead glissée; Glide agit lorsque les notes se chevauchent en mode Mono. Poly pour les accords de pad. Choisir l'unison avec parcimonie : Classic pour une largeur classique, Position Spread pour répartir les positions de table. Vérifier le bas en mono.

## Trois prototypes à construire et comparer

1. **Wobble body** : OSC 1 riche → filtre LP/BP → LFO sync sur cutoff, avec modulation de position plus lente ou de moindre amplitude. Note courte sur les trous de la basse; sub séparé au départ. Ajouter saturation après Wavetable et ajuster dans le morceau.
2. **Stab** : OSC 1 saw → Env 2 court sur cutoff; Amp avec attaque brève et sustain faible. Tester vélocité sur cutoff dans l'onglet MIDI; jouer deux accents différents en contretemps et comparer.
3. **Pad évolutif** : poly, unison Classic modéré, Amp à attaque/release longs; LFO 1 lent sur position OSC 1 et LFO 2 à autre vitesse sur filtre. Automatiser niveau et filtre par section. L'article Ableton décrit aussi une modulation croisée LFO 1 → vitesse LFO 2 → position de table.

## Performance et contrôle

- Oscillateur supplémentaire, voix d'unison, longues releases et second filtre multiplient le travail CPU. Dans un accord à trois notes, deux oscillateurs et huit voix d'unison peuvent produire 48 voix. Imprimer le patch en audio une fois stabilisé.
- Le mode Hi-Quality peut changer subtilement le son; comparer avant le rendu final et ne pas le présenter comme une amélioration automatique.
- Vérifier en contexte avec kick, sub et hats. Les fréquences de coupe et niveaux de sidechain restent dépendants du mix, pas de l'instrument.
