# Piloter Ableton avec les skills et les outils de Claude Code, sur Qwen via Ollama

Question de départ : comment « transférer » vers Ollama/Qwen les skills et les outils (Producer Pal,
LOM Bridge, scripts) que Claude Code utilise dans le terminal pour agir dans Ableton Live ?

Réponse courte : **on ne transfère rien, on change le modèle sous Claude Code.** Depuis Ollama 0.14,
Ollama expose l'API Messages d'Anthropic (`/v1/messages`, outils compris). Claude Code, lancé avec
`ANTHROPIC_BASE_URL` pointé sur Ollama, garde ses skills (`~/.claude/skills`), ses serveurs MCP
(Producer Pal), son outil Bash (donc `lom.py`, `theorie.py`, `analyze_wav.py`…) et sa mémoire de
projet. Seul le cerveau change. Sources : documentation Ollama (`docs/api/anthropic-compatibility`,
`docs/integrations/claude-code`, dépôt ollama/ollama, lus le 24 septembre 2026).

## 1. Ce qui se transfère tel quel, et ce qui ne se transfère pas

| Brique | Nature | Avec Qwen sous Claude Code |
|---|---|---|
| Skills (`~/.claude/skills/*/SKILL.md`, références, recettes) | Fichiers Markdown, standard ouvert *Agent Skills* | **Identiques**, chargés par Claude Code comme aujourd'hui |
| Scripts des skills (`lom.py`, `helpers.py`, `levels.sh`, `theorie.py`, `drum_pattern.py`, `analyze_wav.py`…) | Python/shell lancés par l'outil Bash | **Identiques** |
| LOM Bridge (`lom-bridge/LOMBridge` Remote Script + `lom.py`) | Script Python dans Live + client CLI, OSC/UDP 7421, aucune dépendance à Claude | **Identique** ; ses commandes typées se relisent elles-mêmes, ce qui compense un modèle plus faible |
| Producer Pal (`ppal-*`) | Serveur MCP dans un device Max for Live, déclaré dans Claude Code (`claude mcp list`) | **Identique** : le MCP est branché sur Claude Code, pas sur le modèle. Producer Pal documente d'ailleurs « local models via Ollama or LM Studio » |
| Corpus (`corpus/`, `ask_corpus.py`) | Fichiers + script BM25 → Ollama | Déjà local ; et Claude Code sur Qwen peut le lire directement (outils Read/Grep) |
| Contrôle d'écran (`app_screenshot`, `app_click`, `app_batch`, `computer_batch`, `request_full_control`) | Outils fournis par l'**application de bureau** Claude, pas par le CLI | **Ne se transfère pas.** Remplacement : `screencapture -x` + un modèle à vision (`qwen3-vl`) pour lire, `cliclick` (`brew install cliclick`) pour cliquer, appelés par Bash. Les coordonnées de `vst-sound-design/references/serum2.md` (capture 1190 × 759 de la fenêtre Serum) restent valables si la capture est faite sur la fenêtre, pas sur l'écran entier |
| Recherche web, WebFetch | Outils Claude Code | Passent par la recherche web d'Ollama si configurée, sinon absents |

## 2. Mise en route sur le Mac

```sh
# 1. Ollama à jour (≥ 0.14) et un modèle qui sait appeler des outils
ollama --version
ollama pull qwen3-coder          # 30B-A3B, ≈ 19 Go ; le mieux pour piloter des outils
# ollama pull qwen2.5-coder:14b  # ≈ 9 Go si la RAM manque (moins fiable en multi-étapes)
# ollama pull qwen3-vl           # si tu veux qu'il lise des captures d'écran

# 2. Contexte : les skills sont longs, 64k minimum (Ollama recommande 64k+ pour Claude Code)
#    Soit dans l'app Ollama (réglage Context length), soit :
OLLAMA_CONTEXT_LENGTH=65536 ollama serve

# 3a. Voie officielle Ollama : sélecteur de modèle, réglages faits pour toi
ollama launch claude
ollama launch claude --model qwen3-coder --yes -- -p "lom.py ping puis lom.py state --json ; résume le Set"

# 3b. Voie manuelle (même chose, depuis ce dépôt, avec le script fourni)
docs/claude-ollama.sh qwen3-coder
```

Le script `docs/claude-ollama.sh` exporte `ANTHROPIC_BASE_URL=http://localhost:11434`,
`ANTHROPIC_AUTH_TOKEN=ollama`, retire une éventuelle `ANTHROPIC_API_KEY`, force le même modèle pour
les sous-agents, puis lance `claude --model <modèle>` à la racine du dépôt. Les serveurs MCP déjà
déclarés (Producer Pal) et les skills de `~/.claude/skills` sont vus comme d'habitude : vérifier avec
`/mcp` et `/skills` une fois dans Claude Code.

## 3. Ce à quoi s'attendre avec un modèle local

- **Suivre 8 étapes, relire après chaque action, ne pas hot-swapper** : c'est le rôle des skills, et un
  modèle de 7 à 14 milliards de paramètres les respecte mal. Le LOM Bridge protège (commandes typées,
  refus si un paramètre est automatisé, `snapshot`/`restore`), Producer Pal ne protège pas
  (`browser.load_item` remplace le device sélectionné). Commencer par des tâches courtes et
  vérifiables : `lom.py state`, `lom.py meters`, écrire des notes dans un clip, régler un paramètre.
- **Contexte** : `ableton-live-session/SKILL.md` + une référence + le JSON de `state` remplissent vite
  32k. D'où 64k minimum, et un skill à la fois.
- **Outils** : Ollama supporte messages, système, multi-tours, outils, résultats d'outils, vision,
  thinking ; pas `tool_choice`. Qwen3-Coder est entraîné pour l'appel d'outils ; les Qwen généralistes
  se trompent plus souvent dans les arguments JSON. En cas d'échec répété, `--model` vers un modèle
  cloud d'Ollama (`qwen3-coder:480b-cloud`, `gemma4:cloud`) garde la même installation sans compte
  Anthropic.
- **Permissions** : Claude Code demande confirmation comme d'habitude. Ne pas passer
  `--dangerously-skip-permissions` avec un modèle local sur un Set non sauvegardé.
- **Vision** : Qwen3-Coder ne voit pas les images. Pour lire l'écran de Live ou de Serum, lancer avec
  `qwen3-vl` (ou `gemma4`) et faire `screencapture -x -l <id fenêtre> /tmp/serum.png` puis Read.

## 4. Alternative sans Claude Code

Tout hôte MCP compatible Ollama (Goose de Block, OpenCode, LM Studio, Claude Desktop avec le
`.mcpb` Producer Pal) peut brancher Producer Pal ; Goose et OpenCode lisent aussi le standard
*Agent Skills* (`SKILL.md`) : copier `~/.claude/skills` dans leur dossier de skills. `lom.py` reste un
simple programme à lancer. Mais on perd la mémoire de projet, les hooks et les scripts pensés pour
Claude Code ; la voie « Claude Code + Ollama » demande zéro adaptation.

## 5. Répartition raisonnable

- **Qwen local pour lire** : le corpus (`ask_corpus.py`), les manuels, les recettes ; questions de
  théorie ; résumés.
- **Qwen local pour agir sur des tâches bornées** via `lom.py` (état, mesures, notes, paramètres).
- **Claude (cloud) pour les sessions complètes** : nouveau morceau, mix, export, tout ce qui enchaîne
  plusieurs skills et exige de relire l'état réel sans se tromper.
