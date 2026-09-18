# Pièges appris (à recopier dans le skill technique concerné dès qu'ils sont confirmés)

## Mesure
- `output_meter_left/right` (LOM) est sur une **échelle non linéaire** (type fader) : 20·log10 sous-estime fortement (fader −14 dB → lecture ≈ −4). Comparer en relatif seulement ; pour un chiffre absolu, exporter et analyser le WAV.
- **Mesuré le 15 sept. 2026 sur une piste audio** : `output_meter` lit **après les devices ET après le fader** (fader −14 dB → lecture qui chute ; Utility de fin de chaîne → lecture qui chute). Master : pré-devices du master. Conversion mètre → dB : table `volume.str_for_value(v)` (la courbe du fader, 0,85 = 0 dB, 0,5 = −14 dB) interpolée — fiable ±1 dB entre −7 et −16 dB, sous-estime les écarts en dessous de −20 dB.
- Un `sleep` dans un `/py` gèle les mètres : échantillonner par appels séparés (`../../ableton-live-session/scripts/levels.sh`, chiffres relatifs seulement).

## Bridge (lom.py)
- `read` et `apply` exigent le transport arrêté ; l'utilisateur relance souvent la lecture juste après un `apply` → tester `int(song.is_playing)` juste avant, et ne pas l'arrêter sans le dire.
- `read` : bornes en **temps** (beats), pas en mesures ; max 400 points par appel.
- `apply` : une plage dont un segment n'est couvert par aucun clip fait planter `/shape` → une entrée par zone couverte, dernier point = valeur du fader.
- Les clips support silencieux n'ont pas d'enveloppe de clip : le bridge écrit l'automation de piste et n'a besoin du clip que pour échantillonner. Ne pas supprimer un clip pour le réécrire (réécrire ses notes dedans).
- Nom du paramètre mixer : `Volume`, `Send A`… (pas `Track Volume`). Après un `param.value =` manuel, `song.re_enable_automation()` et vérifier `automation_state == 1`.
- Le solveur refuse « −inf » : viser −40 dB pour couper un envoi.
- `apply_note_modifications` refuse une liste Python → remove + add_new_notes. `duplicate_clip_to_arrangement` marche d'une piste à l'autre.

## Harmonie / notes
- Identifier les accords sur les notes **d'origine**, jamais sur un re-voicing précédent (cascade Fm9 → Ab → Gm7♭5).
- Convention d'affichage Ableton : C3 = 60. Un pizz « 64–77 » est mi3–fa4.

## zsh
- `echo =====` : un mot commençant par `=` est une expansion de commande en zsh → mettre des guillemets.
