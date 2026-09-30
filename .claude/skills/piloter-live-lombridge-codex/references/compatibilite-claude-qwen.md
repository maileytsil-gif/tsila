# Claude, Qwen Code, Qwen/Ollama et Codex devant le LOM Bridge 0.8.1

## Statut

Le client agent est `lom-bridge/agent_gateway.py` du dépôt, écrit pour le serveur HTTP de LOM Bridge 0.8.1 (`lom.py serve`) ; la version unique est dans `lom-bridge/LOMBridge/version.py`. L'adaptateur préparé sur une copie v0.4 (pack du 28 sept. 2026) n'est pas repris : sans jeton, le serveur 0.8.1 le refuse (HTTP 401) ; il cherche le trou de couverture à la racine de la réponse alors que 0.8.1 le place dans `results[].plan.gap` (il accepterait donc un plan non couvert) ; il ne compare pas le plan entre preview et écriture. Contrôlé le 30 sept. 2026 sur le faux Live du dépôt.

Trois voies :
- le Remote Script dans Live (OSC sur UDP 127.0.0.1:7421, jeton, toutes les commandes, `/py` compris), utilisé par `lom.py` ;
- le serveur HTTP `lom.py serve` (127.0.0.1:7480 par défaut, jeton Bearer, `/py /set /call /reload` bloqués sauf `--unsafe`) ;
- le client `agent_gateway.py` (lectures en liste blanche, automation par preview puis commit).

L'ancien device Max for Live (UDP 7411/7412, `lom-bridge/legacy/`) est abandonné.

Preuves : la chaîne `fake_live_server` + `lom.py serve` + `agent_gateway.py` a été vérifiée hors Live le 28 sept. 2026. `tests/live_suite.py` a été rejouée dans Live pour la dernière fois en 0.4.x : les fonctions 0.5 à 0.8, dont tout ce qu'utilise ce client, restent à confirmer sur une copie de Set.

## Installation

Rien à copier : le client est déjà à côté de `lom.py`. Ne jamais remplacer `lom-bridge/agent_gateway.py` par une autre version.
1. Sur le Mac, `$LOM_BRIDGE_DIR` (défaut `/Volumes/NO NAME/caude/lom-bridge`) doit avoir la version du dépôt : `LOMBridge/version.py` = 0.8.1, et `python3 lom.py ping` répond `pong 0.8.1 …` sans ligne `ATTENTION …`. Sinon, le Remote Script chargé n'est pas celui du disque : relancer Live, ou réinstaller `LOMBridge/` selon `lom-bridge/README.md` § Installation.
2. L'utilisateur, ou Claude Code, lance le serveur dans un terminal séparé :
   ```bash
   cd "$LOM_BRIDGE_DIR" && python3 lom.py serve --port 7480
   ```
   Réponse attendue : `LOM Bridge HTTP sur http://127.0.0.1:7480 — Authorization: Bearer <token> ; /py, /set, /call, /reload bloqués`. Jamais `--unsafe` pour un agent.
3. Premier contrôle par l'agent : `python3 agent_gateway.py inspect /ping`, puis `python3 agent_gateway.py inspect /state`. Ne pas tester `GET /` avec curl : il faudrait écrire le jeton dans la commande.
4. Répétition sans Live, **Live fermé** : `python3 tests/fake_live_server.py`, `python3 lom.py serve`, puis les mêmes commandes.

## Utilisation par Claude

Claude Code sur le Mac suit `ableton-live-session` : `lom.py` et ses commandes typées (`state`, `transport`, `setparam`, `snapshot`/`restore`, `load`, `notes`, `apply`, `read`, `journal`), `py` pour ce qui n'a pas de commande, contrôle d'écran pour les menus et les fenêtres. Il ne se limite pas à `agent_gateway.py`, qui n'écrit que de l'automation ; il ne l'utilise que pour répéter la procédure d'un autre agent ou si l'utilisateur le demande. Face à un autre agent, Claude démarre `lom.py serve`, sauve le Set, relit après lui et tient la mémoire de projet.

## Utilisation par Qwen

### Qwen Code (CLI avec outil shell)

Lancé dans le dépôt, Qwen Code lit `AGENTS.md` et `QWEN.md` (`.qwen/settings.json` → `context.fileName`, réglage documenté de Qwen Code) et les skills par `.qwen/skills` → `.claude/skills`. Instruction de projet pour agir dans Live (reprise dans `QWEN.md`) :

« Tu agis sur Ableton Live par `python3 agent_gateway.py` dans le dossier du bridge (`$LOM_BRIDGE_DIR`) pour lire l'état et écrire l'automation, et par Producer Pal (`ppal-*`), s'il est déclaré, pour notes, clips, pistes et devices natifs (jamais un VST, ni une sauvegarde), chaque écriture relue par `ppal-read-*`. Jamais `lom.py`, `curl`, l'UDP, `/py`, ni `lom.py serve --unsafe` ; tu ne lis ni n'affiches `connection.json`. Commence par `inspect /ping`, `inspect /state`, `inspect /transport`, puis les pistes, clips et paramètres utiles. Prépare une seule spec JSON d'après l'état relu, lance `preview`, montre à l'utilisateur le `log` et les deux empreintes, attends son accord, puis lance `commit spec.json --sha256 … --plan-sha256 …`. Relis avec `inspect /events` ou `inspect /read`. Si le transport joue, demande-lui de l'arrêter ; demande-lui aussi de sauver le Set. Après un refus (empreinte, code `E_…`), n'insiste pas : refais `preview` ou explique. Tu ne modifies ni les skills ni le bridge. Tu n'écoutes rien : ne rapporte jamais une écoute. »

Garder la confirmation manuelle des commandes shell : `tools.approvalMode` de Qwen Code à `default`, jamais `yolo`.

### Qwen via Ollama seul (aucun outil)

Ollama exécute le modèle, pas le shell : Qwen ne voit ni ne contrôle Live. Déroulement :
1. Qwen rédige la spec JSON et les commandes exactes.
2. L'utilisateur lance `preview` et colle le résultat (le client n'affiche jamais le jeton).
3. Qwen analyse le résultat.
4. L'utilisateur lance `commit` et colle la relecture.

Chaque réponse porte « non exécuté par moi ». Donner ce skill en message système avec une fenêtre de contexte explicite : `ollama run` tronque en silence au-delà de sa fenêtre par défaut (voir `../../composer-hooks-funk-electro/references/portabilite.md`). Le lanceur `qwen-musique` ne charge que `composer-hooks-funk-electro`.

## Points d'amélioration — état en 0.8.1

| Point (pack v0.4) | État 0.8.1 | Reste à faire |
|---|---|---|
| Interface agent, découverte de la version et des capacités, validation avant écriture | **En partie fait** : `GET /` (version, commandes HTTP, `unsafe`) ; `/ping` (version, Live, session, `commands`, `accept`, `limits`) ; validation par `lom.py` (`validate_entry`), plan serveur, contrôles de `agent_gateway.py` | Pas de MCP ni de JSON-RPC ; pas de schéma JSON formel |
| Authentification, écoute limitée à la boucle locale, jeton hors des prompts | **Fait** : Bearer obligatoire (401), `Origin` refusé (403), 127.0.0.1 codé en dur, 256 Kio au plus (413), `/py /set /call /reload` bloqués sauf `--unsafe`, jeton jamais affiché par le client | Les écritures restent ouvertes en HTTP à qui détient le jeton ; `--unsafe` existe ; le jeton est lisible par tout processus du même utilisateur |
| Compte rendu de chaque mutation | **Fait pour l'essentiel** : codes `E_…` stables, lignes `shape`, `rebuilt`, `verified <n> <écart> <tolérance> <mode>`, avant/après de `setparam`, `loaded … added\|replaced`, journal JSONL horodaté (session, version, id de requête, arguments, résultat ou code), `/jobs`, `/cancel <id>`, `lom.py wait` | L'id de requête n'est pas renvoyé au client HTTP ; une spec à plusieurs entrées n'est pas atomique (une étape d'annulation par entrée) ; `dry` n'est pas une transaction |
| Détecter un changement du Set entre preview et écriture | **En partie fait** : `plan_sha256` côté client (cible, valeurs résolues, références et bornes des clips, trou), `commit` refusé si le plan diffère ; références liées à la session ; revalidation serveur des clips et du paramètre au démarrage de la tâche et avant l'écriture (`E_STALE`) | Le serveur ne reçoit pas l'empreinte relue : une courte fenêtre subsiste entre la replanification du `commit` et `/shape` ; l'empreinte ne couvre que la cible ; la réponse d'écriture ne contient pas le plan |
| Paramètres réellement exposés des VST | **Outillé** : `/params <deviceRef> [filtre]`, `/param`, `/solve`, `/state` (devices, paramètres automatisés) ; fiches `effets-plugins` et `vst-sound-design` | Fenêtre de Serum ou plug-ins sans paramètres exposés : contrôle d'écran, Claude seulement |

Autres écarts relevés au contrôle (non corrigés dans le code) : `lom.py` ignore la variable `LOM_BRIDGE_CONN`, que lisent `agent_gateway.py` et `tests/fake_live_server.py` (définie, elle mène à un 401) ; `tests/fake_live_server.py` réécrit le vrai `connection.json` et occupe le port UDP 7421 : ne le lancer que Live fermé.

## Tests

Depuis `lom-bridge/` :
```bash
python3 -W ignore -m unittest tests/test_offline.py tests/test_gateway.py -v   # commande de la CI : 60 + 16 tests, sans Live
```

`tests/test_gateway.py` vérifie : boucle locale seule ; liste blanche (écritures refusées avant toute requête) ; jeton Bearer lu dans `connection.json` et absent de la sortie ; erreur HTTP relayée ; spec canonique, `skip`, `param` implicite refusé ; plan refusé sur trou, erreur ou mauvais nombre d'entrées ; `commit` refusé si la spec ou le plan relu ont changé ; écriture partielle relayée avec son code ; liste blanche incluse dans `SAFE_HTTP`.

Répétition de bout en bout sans Live (Live fermé) : `tests/fake_live_server.py`, puis `lom.py serve`, puis `agent_gateway.py`. Dans Live, sur un Set jetable ou une copie : `python3 tests/live_suite.py [--keep]` crée puis supprime les pistes « LOM TEST » et « LOM TEST AUDIO ». Elle passe par `/py` en UDP : à lancer par Claude ou par l'utilisateur, jamais par un agent en HTTP. **Aucun test ne simule Ableton Live réel.**
