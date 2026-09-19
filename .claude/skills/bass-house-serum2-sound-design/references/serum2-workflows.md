# Serum 2 — workflows pratiques dérivés de la documentation

Les architectures ci-dessous sont **[HEUR]** : elles utilisent des capacités [DOC], mais les valeurs exactes se règlent à l'écoute.

## Sub stable

But : fondamentale lisible, peu de mouvement de phase.
- moteur simple et contenu harmonique réduit ;
- mono/une voix comme point de départ ;
- articulation d'amplitude adaptée à la durée des notes ;
- pas de largeur sur l'extrême grave ;
- si le mid-bass exige distorsion/unison lourds, séparer le sub.

Test : jouer la ligne une octave autour de la zone cible, vérifier niveau, phase et trous entre les notes.

## Mid-bass articulée

But : identité rythmique + harmoniques.
- choisir Wavetable/FM-like routing via moteur approprié ou moteur Spectral/Granular seulement si le mouvement le justifie ;
- enveloppe courte ou modulation one-shot pour le filtre/timbre ;
- distorsion avant espace ;
- macro `BITE` pour une plage de brillance/résonance sûre ;
- macro `MOTION` pour profondeur de modulation, pas nécessairement fréquence.

Test : bypass des FX et audition avec kick. Le motif doit rester lisible sans mastering.

## Pluck/Stab

But : attaque reconnaissable et queue contrôlée.
- définir d'abord enveloppe d'amplitude ;
- modulation de filtre/timbre plus courte ou complémentaire ;
- limiter le tail des delays/reverbs pour ne pas manger le rythme ;
- tester accords et notes isolées : les résonances peuvent changer avec la hauteur.

## Pad/Nappe

But : soutien et mouvement sans masquer le hook.
- sources larges mais articulation lente ;
- mouvement à plusieurs vitesses, faible profondeur ;
- utiliser routing/bus pour séparer texture et espace ;
- filtrer/arranger avant d'EQ « correctivement » à outrance.

## Riser/Tension

But : trajectoire, pas seulement montée de volume.
- combiner 2–3 dimensions max : pitch, cutoff/timbre, densité/noise, largeur, reverb/delay ;
- piloter via une macro `TENSION` qui mappe plusieurs paramètres sur des plages sûres ;
- couper ou réduire l'énergie grave avant l'impact si cela sert l'arrangement.

## Resampling/sample→wavetable

Pour une source personnelle : isoler un sample clair, convertir via la fonction documentée, puis vérifier la stabilité de pitch et la continuité du balayage. Si la source est complexe, accepter que l'estimation soit moins régulière et traiter le résultat comme nouveau matériau plutôt que comme reconstruction fidèle.
