# Portabilité : Claude Code, Codex CLI, Qwen/Ollama

Le même dossier (`SKILL.md`, `references/`, `scripts/`) sert aux trois outils. Les recettes Serum 2 / Ableton sont des points de départ à écouter et ajuster dans un morceau réel.

## Installation (macOS / Linux)

Depuis le dossier du skill :

```bash
bash scripts/install.sh            # chaque outil présent : ~/.claude, ~/.codex, commande ollama
bash scripts/install.sh --claude   # ou --codex, --qwen, --tout
```

- Copie le dossier dans `~/.claude/skills/composer-hooks-funk-electro` et/ou `~/.codex/skills/composer-hooks-funk-electro`.
- Une version déjà installée est déplacée dans `~/.skills-sauvegardes/` (horodatée). La version Codex d'origine la laissait **dans** le dossier des skills : Claude Code et Codex y auraient trouvé deux skills du même nom.
- Lancé depuis une copie déjà installée, il ne l'écrase pas.
- Le lanceur Qwen devient `~/.local/bin/qwen-musique`, lien vers `scripts/qwen-musique.py` de la copie installée (il retrouve ainsi le skill tout seul).
- N'installe ni Claude Code, ni Codex, ni Ollama, ni aucun modèle.

Dans Claude Code, les liens `../<autre-skill>/…` supposent que les skills du workflow sont voisins (même dossier `skills/`), comme dans ce dépôt et dans `~/.claude/skills/`. Installé seul (Codex, autre machine), le skill reste utilisable : ses règles en tête de `SKILL.md` résument ce que les liens apportent.

## Utilisation

- **Claude Code** : `/composer-hooks-funk-electro` ou demander le travail naturellement ; la carte d'`ableton-live-session` l'appelle pour un hook de genre.
- **Codex CLI** : mentionner `$composer-hooks-funk-electro` dans la demande ou chercher le skill avec `/skills`.
- **Qwen via Ollama** :
  ```bash
  ollama list                                             # nom exact du modèle
  qwen-musique --model NOM "Crée un thème électro chill sur Dm9–G13–Cmaj9–A7alt avec MIDI et patch Serum 2"
  qwen-musique --dry-run "hook funk house et vocoder"     # références choisies, taille estimée, sans appeler Ollama
  qwen-musique --model NOM --ref kick-808-detail.md --num-ctx 32768 "deux kicks 808"
  ```
  Le lanceur classe les références par nombre de mots de la demande qu'elles couvrent (sans tenir compte des accents), en garde quatre au plus (`--max-refs`), et retire les dernières si l'ensemble dépasse la fenêtre demandée (`--num-ctx`, défaut 16384, moins `--reserve` 3000 jetons pour la réponse). Il passe par l'API HTTP d'Ollama (`--host`, défaut `$OLLAMA_HOST` ou `http://127.0.0.1:11434`) pour fixer `num_ctx` : `ollama run` tronque en silence au-delà de sa fenêtre par défaut, et ce sont les instructions du skill, en tête, qui disparaissaient. Si Ollama signale un contexte plein, relancer avec une fenêtre plus grande (que le modèle doit supporter) ou moins de références.

## Limites

- Qwen n'a ni navigation web, ni contrôle d'Ableton, ni accès aux autres skills. Pour agir dans Live, un agent sans Claude Code passe par `lom-bridge/agent_gateway.py` (`inspect` → `preview` → `commit`, écriture refusée si le Set a changé ; voir `lom-bridge/README.md`).
- Un modèle local à petit contexte peut perdre une partie des références : préciser une tâche ciblée, forcer la bonne référence (`--ref`) et vérifier la réponse, par exemple avec `scripts/grille.py` (une grille en C4 = 60 se lit avec `--source scientifique`).
- Pour une vidéo ou un exemple d'artiste, exiger URL, statut réel de consultation, minutage vérifié et incertitudes. Pour « label ready », contrôler l'audio dans le mix, l'écoute mono, les niveaux et la référence choisie : aucun modèle ne peut attester un mastering par la seule lecture d'une recette.

## Vérification

```bash
python3 -m unittest discover -s scripts -p 'test_*.py' -v    # grilles, références, lanceur, installation
python3 scripts/grille.py --verifier references/*.md
bash -n scripts/install.sh
```
Ces contrôles tournent aussi dans l'intégration continue du dépôt (`.github/workflows/skills.yml`).
