# Qwen Code dans ce dépôt

Les règles communes sont dans `AGENTS.md`, chargé avec ce fichier (`.qwen/settings.json` → `context.fileName`). Les skills sont ceux de Claude Code : `.qwen/skills` est un lien vers `.claude/skills`. `/skills` les liste ; `/nom-du-skill` en lance un ; une demande naturelle suffit aussi. Vérifier par `/memory` que `AGENTS.md` et `QWEN.md` sont chargés.

## Ce qui change par rapport à Claude Code

| Besoin | Claude Code | Qwen Code |
|---|---|---|
| Lire l'état de Live | `lom.py ping`, `lom.py state --json` | `python3 agent_gateway.py inspect /ping`, puis `inspect /state` (dans `$LOM_BRIDGE_DIR`, serveur `lom.py serve` lancé par l'utilisateur ou Claude) |
| Écrire une automation | `lom.py apply` | `agent_gateway.py preview spec.json`, accord de l'utilisateur, puis `commit spec.json --sha256 … --plan-sha256 …` ; relire par `inspect /events` ou `inspect /read` |
| Charger un plug-in, régler un paramètre, écrire des notes | `lom.py load`, `setparam`, `notes`, ou Producer Pal | Producer Pal (`ppal-*`) s'il est déclaré (ci-dessous) ; sinon livrer la grille vérifiée (`grille.py`) ou la valeur exacte, que l'utilisateur ou Claude applique. Jamais `lom.py`, `curl`, l'UDP ni `/py` |
| Menus de Live (Sauver Set Live sous…, export), fenêtre de Serum ou d'un plug-in | contrôle d'écran | aucun : demander le geste à l'utilisateur, attendre sa confirmation, puis relire l'état |
| Vidéos, tutoriels | Claude in Chrome (transcription, captures) | aucun accès : demander la transcription ; statut « transcription fournie par l'utilisateur » |
| Mémoire du morceau | `memoire-projet` (`reprise.sh`, `journal.sh`) | les **mêmes** scripts et fichiers (`MEM_DIR`), pour que Claude et Qwen reprennent le même historique ; la mémoire automatique de Qwen ne remplace pas `projet-<nom>.md` |
| Calculs hors Live | `theorie.py`, `grille.py`, `kick_bass_check.py`, `analyze_wav.py`, `session_review.py` | identiques (`python3`) |

Procédure complète, codes d'erreur et limites : skill `piloter-live-lombridge-codex` et sa référence `compatibilite-claude-qwen.md`.

## Consignes

- Tu agis sur Ableton Live uniquement par `python3 agent_gateway.py` dans le dossier du bridge ; tu ne lis ni n'affiches `connection.json` ; jamais `lom.py serve --unsafe`.
- Une spec par étape : `preview`, montrer le `log` et les deux empreintes, attendre l'accord, `commit`, relire. Après un refus (empreinte, code `E_…`), refaire `preview` ou expliquer ; ne jamais forcer.
- Tu ne modifies ni les skills ni le bridge : tu proposes le changement (diff), l'utilisateur décide ; les modifications se font dans le dépôt puis `python3 outils/verifier_skills.py`.
- Tu n'écoutes rien : jamais « j'ai écouté », « ça sonne » ; les tests d'écoute sont faits par l'utilisateur, les mesures par les scripts.
- Garder la confirmation des commandes shell (`tools.approvalMode` à `default`, jamais `yolo`).

## Installer pour tous les projets

Depuis le dépôt, sur le Mac :

```bash
bash outils/installer.sh --qwen                    # simulation : ce qui serait relié dans ~/.qwen/skills
bash outils/installer.sh --claude --qwen --appliquer
bash outils/installer.sh --producer-pal-qwen --appliquer   # déclare le serveur MCP Producer Pal dans ~/.qwen/settings.json
```

`~/.qwen/skills/<nom>` devient un lien vers `~/.claude/skills/<nom>` : une seule copie installée pour les deux outils. Producer Pal demande Node.js 20+ et le device `Producer_Pal.amxd` dans le Set ; vérifier avec `/mcp` dans Qwen Code.

## Qwen via Ollama seul (sans Qwen Code)

Aucun outil : il rédige grilles, specs JSON et réglages ; l'utilisateur exécute et colle le résultat ; chaque réponse dit « non exécuté par moi ». Pour les hooks et timbres de genre : `qwen-musique` (installé par `composer-hooks-funk-electro/scripts/install.sh --qwen`), qui envoie le skill avec une fenêtre de contexte explicite.
