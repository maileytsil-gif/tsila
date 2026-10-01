# Macros et schéma de pilotage par le bridge

Pour un patch destiné au contrôle par l'IA (Producer Pal sur les natifs, paramètres Serum 2 mappés par l'utilisateur, voir `../../sound-designer-serum/references/serum2-automation-et-migration.md`), exposer en priorité :

| Macro | Fonction | Plage sûre à déterminer [TEST] |
|---|---|---|
| Brightness | cutoff ou index FM, suit la dynamique | ne jamais fermer au point d'éteindre le corps ; sur un multisample, agit sur la couche de vélocité ou un filtre en aval |
| Bite | attaque : quantité d'enveloppe de filtre, transitoire de langue, scoop | éviter le clic et le décalage de hauteur audible sur les tenues |
| Breath | niveau du bruit de souffle | rester sous le corps, inaudible seul à faible volume |
| Vibrato | profondeur du LFO retardé | 0 = aucun ; le délai reste fixé dans le patch, pas dans la macro |
| Section | détune, spread, nombre de voix d'unisson | vérifier en mono à chaque cran |
| Space | départ reverb ou delay | retour filtré, pas de reverb sur les stabs courts sans test |
| Fall | enveloppe de hauteur descendante en fin de note | état par défaut neutre (0) |
| Drive | saturation ou distorsion du corps | compensation de niveau incluse |

Le bridge doit : `snapshot` → modifier → relire → comparer → `restore` si hors plage. Ne pas automatiser un paramètre non exposé ou non confirmé [TEST]. Les macros nommées d'après un geste musical (« plus brillant au refrain ») se lisent mieux dans la mémoire du projet que des noms de paramètre.

Ce qui appartient au MIDI et non aux macros : la dynamique note à note (vélocité), l'expression continue (molette CC1, expression CC11), les articulations d'un multisample (keyswitches). Voir `sampled-brass-midi-programming.md`.
