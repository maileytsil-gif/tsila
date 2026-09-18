# LOM Bridge v0.4.1 — dossier de revue pour ChatGPT (fiabilisation)

## Ce qui a été fait depuis ta revue de la 0.4.0
Chaque constat a été **vérifié avant correction** (reproduction locale de l'arrondi OSC : 9000000001 et 9000000002 → 9000000512 ; conversion `num()` en flottant ; absence d'exposition des fondus et des expressions de notes dans l'API, constatée par introspection dans Live ; `Live.Clip.WarpMarker(sample_time, beat_time)` fonctionnel). Architecture conservée (Remote Script + client UDP), aucune fonction nouvelle.

| Point | Correction 0.4.1 | Preuve logicielle (tests/test_offline.py) | Vérification dans Live |
|---|---|---|---|
| Ids arrondis par OSC ; client convertit en flottant | Références opaques `o:<session>:<n>` ; entiers hors int32 en int64 ; `num()` garde les références et rend des `int` exacts ; session vérifiée à chaque résolution ; ids numériques refusés | `test_big_ints_roundtrip_exact`, `test_refs_and_strings_untouched`, `test_num_keeps_refs_and_ints`, `test_ref_roundtrip_no_loss`, `test_numeric_ids_refused_and_foreign_session` | `/ping` → session ; `/track` → `o:493090:1` ; suite Live « références opaques » |
| HTTP sans authentification, `/py` relayé | `Authorization: Bearer <token>` obligatoire, `Origin` refusé, liste blanche (`/py /set /call /reload` bloqués sauf `--unsafe`) | `test_http_allowlist` | non testé avec un client HTTP réel |
| Contrôle des clips incomplet (fondus, warp, expressions) | `_check_clip` : fatal (take lane, enregistrement, clip bouclé étiré, audio sans fichier) ; **acceptation requise** : `fades` (audio), `expressions` (MIDI), `warp` (marqueurs non recréables, contrôle à la reconstruction, abandon avant remplacement), `clamp` | `test_audio_requires_accept_fades`, `test_looped_stretched_refused`, `test_res_and_accept_validation` | « audio sans accept=fades refusé » ; warp markers recréés sur clip audio (essai manuel) |
| Pas de plan commun dry/exécution | `_build_plan` unique : valeurs résolues et vérifiées, clips, extension `hold`, compatibilité, budget calculé **avant** génération (`count_breakpoints` = nombre réel de points), trous, estimation d'échantillonnage ; `/plan` = ce plan sans écriture ; `/shape` = même plan puis exécution ; `apply --dry` appelle `/plan` | `test_budget_before_generation`, `test_breakpoint_budget_matches`, `test_zero_window_refused_unless_hold`, `test_clamp_reported` | « plan valide », « fenêtre nulle refusée », « saturation refusée / acceptée et signalée » |
| Revalidation, annulation par id, nettoyage | Revalidation au **démarrage effectif** de la tâche (clips présents aux mêmes positions, paramètre vivant, transport arrêté si échantillonnage) ; `/cancel <id>` (tâche en file : retirée ; en cours : arrêt au prochain point d'attente) ; `/jobs` ; reconstruction nettoyée sur erreur (clip de session et scène créée supprimés) | `test_job_cancel_by_id_and_revalidation`, `test_rebuild_cleans_up_on_error` | « annulation par id », « file vide », « revalidation : clip disparu » |
| Jeton au premier démarrage | fichier de connexion écrit dans `__init__` (plus de première requête refusée) | `test_token_file_created_at_init`, `test_token_required` | ping après réouverture de Set |
| Fenêtre de durée nulle | refusée sauf `hold=1` (tenue jusqu'à la fin du clip) | `test_zero_window_refused_unless_hold` | « fenêtre nulle refusée » |
| Valeurs saturées | plan : erreur sans `accept=clamp`, sinon `clamped:1` + avertissement | `test_clamp_reported` | « saturation … » |
| Bande d'ancrage (0.3.2) | ancrages **exactement** sur les bords (deux points au même instant) | `test_old_points_exact_anchors` | 192 points hors fenêtre inchangés ; 19,9375 → 0,2461 |
| Saut au début d'un clip (0.3.2) | interpolation droite/gauche aux bords | `test_interp_sides`, `test_shape_orders_jump_and_writes_events` | 1,0 à 31,75 ; 0,0 à 32,0 |
| `SameFileError` du générateur `.amxd` | device M4L retiré du paquet (`legacy/`, protocole obsolète, sans automation) | — | — |

## Essais dans Live 12.4.5
1. **Copie d'el21** (`el21 - test LOM.als`, faite après sauvegarde par l'utilisateur) : `tests/live_suite.py` → 26/26 (deux pistes temporaires créées puis supprimées).
2. Sur la même copie, cibles réelles : réécriture d'une fenêtre 29|1–31|1 sur le filtre de CHORDS 2 (clip qui porte déjà un sweep 33→37). Zones non ciblées sur d'autres pistes (kick 57–69, sub 5–13, 42 points) : identiques. Sweep 33→37 du **même clip** : conservé à **0,0011** près (le clip n'expose plus son enveloppe après réouverture du Set → chemin échantillonné, pas 1/8 de temps, tolérance 0,0015). `song.undo()` : une seule étape, tout revient. « Sauver Set Live » puis fermeture/réouverture réelle de la copie : sweep et fenêtre identiques à **0,0000** près.

## Contrat explicite (à critiquer)
- Hors fenêtre : identité **stricte** quand le clip expose l'enveloppe (clip MIDI créé dans la session Live courante), sinon identité à **0,0015 normalisé** près par échantillonnage au 1/8 de temps (≈ 0,1 s par pas : 8 mesures ≈ 26 s, transport arrêté, curseur déplacé puis restauré).
- Jamais recopiés : fondus de clip, expressions de notes → acceptation obligatoire. Refusés : clips bouclés étirés, take lanes, clip en enregistrement. Rien hors d'un clip.
- Sécurité : loopback + jeton 0600 ; `/py` uniquement en UDP local avec jeton. Pas de limitation de débit.
- Une seule tâche exécutée à la fois, file de 4, latence de 100 ms par tick.

## Ce que je te demande
Rejoue tes tests sur cette version (sources jointes), puis cherche : cas limites du plan (points au même instant aux bords, `hold` sur un clip suivant absent, clip couvrant partiellement la plage), robustesse de `_free_slot` (slots de groupe), comportement si la reconstruction échoue **après** `duplicate_clip_to_arrangement` (l'ancien clip est déjà remplacé), et tout ce qui manque pour un usage par une IA sans erreur.
