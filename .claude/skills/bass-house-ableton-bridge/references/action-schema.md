# Bridge Action Schema — v18

La forme canonique est `core/schemas/bridge-action-batch.schema.json`.

Chaque action contient :
- `request_id` ;
- `depends_on` ;
- `requires_capability` ;
- cible logique (pas un ID LiveAPI persistant) ;
- opération + payload ;
- postconditions ;
- rollback ;
- risque.

Opérations conceptuelles : `inspect`, `ensure_track`, `create_clip`, `replace_notes`, `set_value`, realtime remote, automation persistante, snapshot/restore.

`ensure_track` ne signifie pas que Live/LOM sait créer une piste dans l'instance courante : la capability doit être découverte. Si non supportée, le bridge doit demander/préparer manuellement la piste plutôt que prétendre l'avoir créée.
