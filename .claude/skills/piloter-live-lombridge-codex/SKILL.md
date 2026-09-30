---
name: piloter-live-lombridge-codex
description: Procédure pour un agent autre que Claude Code (Qwen Code, Codex, Qwen via Ollama) qui agit dans Live 12 par lom-bridge/agent_gateway.py (inspect → preview → commit), bilan de séance sur preuves (session_review.py), amélioration proposée du bridge, clip « Après les heures ». Utiliser quand un autre agent doit agir dans Live ou que l'utilisateur demande un bilan de séance. Claude Code → ableton-live-session.
---

# LOM Bridge : procédure pour un autre agent (Qwen Code, Codex)

Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

## Vérifier les accès réels

Le bridge de référence est celui du dépôt : `lom-bridge/` (LOM Bridge **0.8.1**, version unique dans `lom-bridge/LOMBridge/version.py`) ; sur le Mac, `$LOM_BRIDGE_DIR` (défaut `/Volumes/NO NAME/caude/lom-bridge`). La copie v0.4 d'où vient la première version de ce skill, et son ancien client, sont périmés : ne rien installer ni copier depuis le pack d'origine.

Avant chaque séance :
- Mac en ligne, terminal ; contrôle d'écran pour Claude Code seulement (menus de Live, fenêtres de plug-ins).
- Live lancé avec la surface de contrôle LOMBridge. `python3 lom.py ping` (Claude) ou `python3 agent_gateway.py inspect /ping` (autre agent) répond `pong 0.8.1 live <version de Live> session <n>`, puis `commands …`, `accept …`, `limits …`. Si `lom.py ping` affiche `ATTENTION : bridge chargé dans Live = x, script sur le disque = y`, relancer Live avant toute écriture.
- Qui utilise quoi : Claude Code suit `../ableton-live-session/SKILL.md` (`lom.py`, commandes typées). Tout autre agent (Qwen Code, Codex, second Claude) passe par `lom-bridge/agent_gateway.py` pour lire l'état et écrire l'automation (et par Producer Pal (`ppal-*`), s'il est déclaré, pour notes, clips, pistes et devices natifs (jamais un VST, ni une sauvegarde), chaque écriture relue par `ppal-read-*`), jamais par `lom.py`, sur le serveur `lom.py serve` démarré par l'utilisateur ou par Claude, jamais avec `--unsafe`.
- Le jeton est dans `~/Library/Application Support/LOMBridge/connection.json` ; `agent_gateway.py` le lit lui-même. Ne jamais l'ouvrir, l'afficher ni le recopier dans un prompt, un fichier ou une réponse.
- Seule la réponse du bridge, puis la relecture, prouve qu'une commande a été exécutée ; jamais la documentation.
- État des preuves : dans Live réel, `tests/live_suite.py` n'a pas été rejouée depuis 0.4.x ; la chaîne `lom.py serve` + `agent_gateway.py` n'est vérifiée que sur le faux Live (`tests/fake_live_server.py`, 28 sept. 2026). La première écriture réelle d'un agent se fait sur une copie de Set.

## Enchaînement obligatoire

Une étape par échange : annoncer le plan complet, n'exécuter qu'une étape, attendre l'accord de l'utilisateur. Il modifie le Set entre deux échanges : relire avant d'agir. Commandes lancées depuis le dossier du bridge (`cd "$LOM_BRIDGE_DIR"`) ; mettre les temps `mesure|temps` entre guillemets (sinon le shell lit `|` comme un tube).

1. **Copie et mémoire.** Le Set est sauvé sous un nouveau nom avant toute modification (Fichier › Sauver Set Live sous… : Claude par contrôle d'écran, sinon l'utilisateur ; un agent sans écran le demande et attend la confirmation). Ouvrir la séance par `../memoire-projet/SKILL.md` (`reprise.sh`). Noter le chemin du Set, la version du bridge et la session (ligne `pong`), jamais le jeton.
2. **Découvrir l'état réel** (rien n'est écrit) :
   ```bash
   python3 agent_gateway.py inspect /state                            # tempo, signature, transport, pistes, devices (refs), paramètres automatisés, repères
   python3 agent_gateway.py inspect /transport                        # sans argument = lecture seule
   python3 agent_gateway.py inspect /clips "NOM EXACT"                # ref début fin nom audio
   python3 agent_gateway.py inspect /param "NOM EXACT" mixer Volume   # ref nom min max valeur affichage quantifié état_automation
   python3 agent_gateway.py inspect /params <deviceRef> [filtre]      # paramètres réellement exposés d'un device
   python3 agent_gateway.py inspect /journal 10                       # dernières écritures du bridge
   ```
   Claude fait les mêmes lectures avec `lom.py state --json`, `lom.py transport`, `lom.py clips`, `lom.py param`, `lom.py params`, `lom.py journal 10`. Les références `o:<session>:<n>` sont refusées si elles viennent d'une autre session de Live et changent pour chaque clip reconstruit : les relire après chaque écriture, redémarrage ou chargement de Set. Un paramètre absent de `/params` n'est pas pilotable par l'API ; ne supposer aucun accès à la fenêtre de Serum ou d'un plug-in (contrôle d'écran : Claude seulement).
3. **Objectif, spec, plan.** Fixer un objectif musical précis (section en mesures, paramètre, valeurs). Écrire une spec au format de `lom-bridge/README.md` :
   ```json
   {"automations":[{"track":"NOM EXACT","device":"mixer","param":"Volume","unit":"disp","res":8,"curve":"lin","hold":false,"accept":["fades"],"points":[["5|1",-5],["9|1",0]],"note":"…"}]}
   ```
   `param` est toujours explicite ; au plus 32 entrées actives ; `unit` vaut `disp` (valeur affichée), `raw` (0–1) ou `rel` (décalage de la valeur courante). Puis `python3 agent_gateway.py preview spec.json`, qui renvoie `sha256` (spec), `plan_sha256` (plan relu), `log` et `preview` ; rien n'est écrit. Lire dans `log` les valeurs résolues, les clips, les lignes `non couvert`, `avertissement`, `ERREUR` et la durée d'échantillonnage. Le client refuse un plan en erreur ou une plage non couverte par des clips.
   Écrire une automation **reconstruit** chaque clip couvert. Les fondus de clip audio (`fades`), les expressions MIDI (`expressions`) et le warp non reproductible (`warp`) ne sont pas recopiés : il faut les accepter explicitement, sinon le plan est refusé. Les clips bouclés étirés et les take lanes sont refusés. Si un échantillonnage est annoncé, le transport doit être arrêté : le demander à l'utilisateur (un agent ne peut pas l'arrêter). Montrer le plan et attendre l'accord.
4. **Écrire une seule spec, puis relire.**
   ```bash
   python3 agent_gateway.py commit spec.json --sha256 <sha256> --plan-sha256 <plan_sha256>
   ```
   Le client replanifie et refuse si la spec ou le plan ont changé (autre session, clip déplacé, valeur courante changée avec `rel`) : refaire alors `preview`. Le bridge écrit chaque entrée en tout ou rien, la relit (`relecture: exact|sampled …`) et défait lui-même une écriture fausse (`E_ROLLED_BACK` : rien n'est modifié). Chaque entrée est une étape d'annulation séparée : une spec à plusieurs entrées n'est pas atomique. `E_STALE` → refaire `preview` ; `E_TRANSPORT_PLAYING` → demander l'arrêt ; `E_ROLLBACK_FAILED` → demander Cmd+Z tout de suite.
   Relire ensuite :
   ```bash
   python3 agent_gateway.py inspect /events "NOM EXACT" <paramRef>               # enveloppes exposées (clips MIDI reconstruits)
   python3 agent_gateway.py inspect /read "NOM EXACT" <paramRef> "5|1" "9|1" 1   # valeur réelle (transport arrêté ; curseur déplacé puis restauré)
   ```
   Faire sauver le Set et noter l'étape (`journal.sh`). Si la qualité musicale est en jeu, un rendu (`../live-export-wav/SKILL.md`) est **écouté par l'utilisateur** : un agent n'écoute rien. Pour un morceau entier, les portes composition → son → arrangement → mix → rendu sont celles de `../produire-morceau-electronique-de-a-a-z/SKILL.md`. Du MIDI créé n'est pas un morceau livré.
5. **Bilan.** Depuis le dossier du skill : `python3 scripts/session_review.py session.json [--output bilan.json]` (copie jumelle de celui de `produire-morceau-electronique-de-a-a-z`). Champs du journal JSON : `session_id`, `project_copy`, `bridge_version` ; `bridge_commands` (recopiées de `inspect /journal 20` ou de `lom.py journal 20`) ; `renders` ; `listening` (écoutes **de l'utilisateur**, avec ses mots) ; `user_feedback` (`approved` seulement s'il l'a dit) ; `errors`. Ne jamais inventer une écoute ni une approbation. Clore la séance par `memoire-projet`.
6. **Améliorer : proposer, ne pas appliquer.** Un comportement répété (piège, commande plus sûre, réglage validé) se note d'abord dans la mémoire de projet, puis se **propose** à l'utilisateur comme modification de skill. Le diff lui est montré ; il n'est appliqué qu'avec son accord, dans le dépôt et jamais dans une copie installée, contrôlé par `python3 outils/verifier_skills.py`, et commité seulement à sa demande (`AGENTS.md` du dépôt). Le code du bridge ne se modifie que dans `lom-bridge/` du dépôt, sur demande explicite de l'utilisateur et par Claude Code : reproduire le problème, écrire un test hors Live (`tests/test_offline.py` ou `tests/test_gateway.py`), changer la version dans `LOMBridge/version.py`, mettre à jour le README (« Ce qui a été vérifié »), puis essayer sur une copie de Set (`tests/live_suite.py`). Un agent qui passe par `agent_gateway.py` ne modifie ni les skills ni le bridge. Une séance réussie ne suffit jamais à réécrire une procédure.

## Adaptateur local et portabilité

Ce skill n'embarque aucun client : il utilise `lom-bridge/agent_gateway.py` du dépôt (client 0.8.x ; 16 tests hors Live dans `lom-bridge/tests/test_gateway.py`). Prérequis : LOMBridge actif dans Live, puis dans un terminal séparé `cd "$LOM_BRIDGE_DIR" && python3 lom.py serve --port 7480`. Ce serveur n'écoute que sur 127.0.0.1, exige `Authorization: Bearer`, refuse l'en-tête `Origin` et les corps de plus de 256 Kio, et bloque `/py`, `/set`, `/call`, `/reload` ; jamais `--unsafe` pour un agent. Routes : `POST /cmd`, `POST /apply` (`dry` vrai par défaut), `GET /` (aide ; jeton exigé).

Garde-fous du client : boucle locale seulement ; jeton lu dans `connection.json` et jamais affiché (garder le chemin par défaut : `lom.py serve` ne lit pas `LOM_BRIDGE_CONN`) ; `inspect` limité à une liste blanche de lectures (`/ping /state /track /param /params /solve /clips /plan /read /events /jobs /children /get /info /path /snapshots /locators /journal`, `/transport` sans argument, `/notes get`) ; `preview` puis `commit` avec les deux empreintes. Ces garde-fous ne protègent pas le serveur : en HTTP, le détenteur du jeton peut aussi écrire (`/shape`, `/clear`, `/setparam`, `/load`, `/notes set`, `/transport`…). Un agent qui a un shell s'interdit donc `lom.py`, `curl`, l'UDP et la lecture de `connection.json`, et l'utilisateur garde la confirmation des commandes shell.

- Claude Code : `../ableton-live-session/SKILL.md` ; ce skill seulement pour répéter la procédure d'un autre agent ou pour le bilan.
- Qwen Code (shell) et Codex : `agent_gateway.py` pour la lecture et l'automation, selon les étapes ci-dessus ; Producer Pal (`ppal-*`), s'il est déclaré, pour notes, clips, pistes et devices natifs (jamais un VST, ni une sauvegarde), chaque écriture relue par `ppal-read-*` ; instruction de projet dans `references/compatibilite-claude-qwen.md` (reprise dans `QWEN.md` à la racine du dépôt).
- Qwen via Ollama seul : aucun outil, donc aucun contrôle de Live. Il rédige la spec et les commandes ; l'utilisateur les exécute et colle le résultat ; chaque réponse dit « non exécuté par moi ».

Répétition hors Live, **Live fermé** (le faux Live réécrit `connection.json` et écoute sur le port UDP 7421 du vrai bridge) : `python3 tests/fake_live_server.py` (terminal 1), `python3 lom.py serve` (terminal 2), puis les commandes ci-dessus (terminal 3). Set simulé : `AUDIO - Sub` et `3-MIDI`.

## Projet de vidéo

Pour accompagner une production, écrire synopsis, personnage, boucle visuelle par section, palette et liste de plans avant de générer des images. Le concept préparé « Après les heures » est dans `references/clip-manga-weekend.md` (copie jumelle de celui du skill A à Z) ; storyboard de travail en quatre cases : `assets/storyboard-manga-weekend.png`. Ce storyboard montre le logo SBB en gare de Genève : le retirer des visuels finaux, comme toute marque réelle (règle du concept). Séparer effets sur un DJ set et éléments visuels embarqués dans le clip. Ne pas utiliser d'images de marques ou d'artistes réels sans raison.
