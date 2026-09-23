# Pièges appris (à recopier dans le skill technique concerné dès qu'ils sont confirmés)

## Mesure
- `output_meter_left/right` (LOM) est sur une **échelle non linéaire** (type fader) : 20·log10 sous-estime fortement (fader −14 dB → lecture ≈ −4). Comparer en relatif seulement ; pour un chiffre absolu, exporter et analyser le WAV.
- **Mesuré le 15 sept. 2026 sur une piste audio** : `output_meter` lit **après les devices ET après le fader** (fader −14 dB → lecture qui chute ; Utility de fin de chaîne → lecture qui chute). Master : pré-devices du master. Conversion mètre → dB : table `volume.str_for_value(v)` (la courbe du fader, 0,85 = 0 dB, 0,5 = −14 dB) interpolée — fiable ±1 dB entre −7 et −16 dB, sous-estime les écarts en dessous de −20 dB.
- Un `sleep` dans un `/py` gèle les mètres : échantillonner par appels séparés (`../../ableton-live-session/scripts/levels.sh`, chiffres relatifs seulement).

## Bridge (lom.py)
- `read` et `apply` exigent le transport arrêté ; l'utilisateur relance souvent la lecture juste après un `apply` → tester `int(song.is_playing)` juste avant, et ne pas l'arrêter sans le dire.
- `read` : bornes en **temps** (beats), pas en mesures ; max 400 points par appel.
- `apply` : une plage dont un segment n'est couvert par aucun clip n'est pas refusée (depuis 0.4.x : avertissement « n temps non couverts »), mais **rien n'est écrit dans le trou** : l'automation y reste ce qu'elle était. Si la plage ne touche aucun clip → erreur. Faire une entrée par zone couverte, dernier point = valeur du fader.
- Rien n'est automatisable hors d'un clip : sur un bus ou une piste sans clip, poser un clip audio silencieux comme support. Le bridge reconstruit ce clip pour y écrire l'enveloppe (audio → accepter `fades`, souvent `warp`). Ne pas supprimer un clip pour le réécrire : réécrire ses notes dedans (`lom.py notes set`, ou `remove_notes_extended` + `add_new_notes`).
- Depuis 0.5.0 : écriture tout ou rien puis relecture (`verified …`) ; `E_ROLLED_BACK` = rien n'est modifié ; `E_AUTOMATION_OVERRIDDEN` = un paramètre automatisé a été bougé à la main → `song.re_enable_automation()` avant d'écrire. `lom.py journal` relit les dernières écritures.
- Nom du paramètre mixer : `Volume`, `Send A`… (pas `Track Volume`). Après un `param.value =` manuel, `song.re_enable_automation()` et vérifier `automation_state == 1`.
- Le solveur refuse « −inf » : viser −40 dB pour couper un envoi.
- `apply_note_modifications` refuse une liste Python → remove + add_new_notes. `duplicate_clip_to_arrangement` marche d'une piste à l'autre.

## Harmonie / notes
- Identifier les accords sur les notes **d'origine**, jamais sur un re-voicing précédent (cascade Fm9 → Ab → Gm7♭5).
- Convention d'affichage Ableton : C3 = 60. Un pizz « 64–77 » est mi3–fa4.

## zsh
- `echo =====` : un mot commençant par `=` est une expansion de commande en zsh → mettre des guillemets.
