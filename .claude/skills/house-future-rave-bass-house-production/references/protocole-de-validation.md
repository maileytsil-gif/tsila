# Protocole de validation

Un élément, une section ou un master de future rave, de bass house ou de house n'est validé qu'après ces tests, dans le Set réel, à niveau comparable, et avec les mesures du dépôt (`lom.py meters`, `kick_bass_check.py`, `arrangement_map.py`, Insight 2 ou WLM Plus sur le fichier exporté).

## Son (sound design)

1. **Registre** : le sub ne joue que la fondamentale en octave 0–1 ; aucune tierce sous C2 (48) ; la basse mid commence au-dessus de 80 Hz (bass house : 80–100, future rave : 100–200) ; le lead supersaw est coupé sous 150–250 Hz.
2. **Seul contre dans le mix** : le son validé seul est rejoué avec kick, sub et hats ; s'il disparaît ou domine, on corrige le patch (registre, saturation, largeur), pas le fader.
3. **Mono** : basse et kick restent identiques en mono ; un lead large ne perd que de la largeur, pas de corps (bx_glue Mono Maker ou Utility mono sur le Main, puis retour).
4. **Sidechain** : la basse et les nappes respirent avec le kick (2–4 dB « invisible » ou 4–12 dB audible selon le genre) ; le release ne dépasse pas l'intervalle entre kicks (234 ms par croche, 469 par noire à 128).
5. **Deux notes** : le patch tient la fondamentale la plus basse et la plus haute du riff sans changer de caractère (unisson, filtre key-track, saturation).
6. **Macros aux extrêmes** : chaque macro reste musicale à 0, 50 et 100 % sur la section la plus dense.
7. **Reproductibilité** : preset sauvé sous un nouveau nom ; paramètres relus par l'API pour les natifs, capture pour Serum 2 ; version de Serum 2 notée.

## MIDI et groove

8. **Grille** : kick et clap sans groove ; swing uniquement sur les positions 2 et 4 de chaque temps, à la valeur du genre (50 % future rave et big room, 52–55 % tech house) ; la première double de chaque temps reste vide pour le kick sur une basse roulante.
9. **Vélocités** : plages larges en tech house (ghosts 40–55, accents 110–118), plates en future rave ; rien de tout plat en house.
10. **Harmonie** : le riff de bass house tient sur i (et VII au plus) ; en future rave, add9, sus et quintes plutôt que triades nues ; la tonalité mise dans le compte rendu est vérifiée à l'oreille, pas lue dans Tunebat.

## Arrangement

11. **Grille de forme** : chaque frontière sur un multiple de 8 depuis la mesure 1 ; `arrangement_map.py` relu après toute édition.
12. **Test de soustraction** : à chaque bloc de 8, au moins un élément du bloc précédent disparaît ; drop 2 dépasse drop 1 par un élément, une octave, une couche ou une image, pas par le niveau.
13. **Gap et premier temps** : 1–2 temps quasi vides avant chaque drop ; impact, crash, sub-drop et mix complet sur le même échantillon au un.
14. **Spectre par section** : sub absent en intro, build et breakdown ; hats sans pleine brillance dès la mesure 1 ; breakdown à −6 à −10 LU sous le drop.
15. **Destination** : intro et outro DJ de 16–32 mesures pour le club mix, 4–8 pour le radio edit ; premier drop avant 45 s à 1:00 en radio.

## Mix et master

16. **Un porteur par bande** au drop ; six à dix éléments simultanés, jamais plus.
17. **Grave** : corrélation 30–120 Hz positive (`kick_bass_check.py`), qui tient la fondamentale décidé et écrit (kick porteur en big room et future rave, sub tenu en tech et deep house, couche sub dédiée en bass house).
18. **A/B à sonie égale** avec la référence (REF vers Main hors limiteur, TBC 3, Gain Match du L4 désactivé avant export).
19. **Mesure sur le fichier exporté** : intégré, true peak, LRA, short-term max (drop) et min (breakdown), PLR ; club −8 à −7 LUFS et TP −1,0 ; streaming −10 à −11 ; limiteur 2–4 dB sur le drop, sinon remonter le mix.
20. **Contrôles de livraison** : mono, téléphone, bas volume, ≤ −1 dBTP, versions et stems depuis la mesure 1.

## Conditions d'arrêt

- basse bass house saturée sur la couche sub au lieu de la couche mid ;
- sidechain posé sur un bus déjà compressé ou sur le master ;
- riser ou snare roll sur chaque transition, silence de plus de deux temps deux fois par morceau ;
- drop 2 identique au drop 1, ou plus fort seulement ;
- kick de future rave sans queue ni saturation, hats swingués en future rave ;
- « son de Guetta » ou « son de Jauz » attribué à un réglage précis : aucune source ne documente leurs réglages ;
- master poussé au-delà de −6 LUFS intégrés ou à plus de 4–5 dB de réduction au limiteur ;
- tonalité ou minutage écrit dans un compte rendu à partir d'une base automatique sans vérification.
