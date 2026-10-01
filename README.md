# tsila

Workflow de production musicale (Ableton Live 12, Serum 2, Maschine MK3) piloté dans le terminal par Claude Code et Qwen Code : des skills, un pont vers Live (LOM Bridge) et des outils de contrôle.

## Contenu du dépôt

| Chemin | Rôle |
|---|---|
| `.claude/skills/` | les 44 skills du workflow, **source unique** |
| `.claude/settings.json` | réglage de projet de Claude Code : `skillListingBudgetFraction` 0,03, soit 3 % du contexte pour la liste des skills (1 % par défaut), pour que les 44 descriptions y restent |
| `.qwen/skills` | lien vers `../.claude/skills` : Qwen Code lit exactement les mêmes fichiers |
| `.qwen/settings.json` | `context.fileName` : Qwen Code charge `AGENTS.md` et `QWEN.md` |
| `AGENTS.md` | règles communes à tous les agents : par où entrer, règles de chaque morceau, règles du workflow |
| `CLAUDE.md` | lu par Claude Code : importe `AGENTS.md` et ajoute ce qui est propre à Claude |
| `QWEN.md` | lu par Qwen Code avec `AGENTS.md` : différences avec Claude Code, consignes, installation |
| `lom-bridge/` | LOM Bridge 0.8.1 : Remote Script de Live, `lom.py`, `agent_gateway.py`, tests hors Live ; installation dans `lom-bridge/README.md` |
| `outils/` | `installer.sh` (installation des skills), `verifier_skills.py` (contrôle), `test_outils.py` (leurs tests) |
| `.github/workflows/` | `skills.yml` et `tests.yml` : les contrôles ci-dessous, lancés à chaque push et pull request |

## Démarrer

Lancer l'outil dans le dossier du dépôt :

```bash
cd tsila
claude      # Claude Code : lit CLAUDE.md (qui importe AGENTS.md) et les skills de .claude/skills
qwen        # Qwen Code : lit AGENTS.md et QWEN.md, et les mêmes skills par le lien .qwen/skills
```

- Un skill s'appelle par `/nom-du-skill` (par exemple `/chef-de-projet`) ou par une demande en langage naturel. Dans Qwen Code, `/skills` les liste et `/memory` montre que `AGENTS.md` et `QWEN.md` sont chargés.
- `ableton-live-session` contient la carte « situation → skills » : elle dit quel skill prend la main et lesquels suivent.
- L'agent annonce le plan complet puis exécute ou fait valider **une étape par échange** ; il relit l'état réel de Live avant d'agir.

Premières demandes possibles :

| Vous écrivez | Skill qui prend la main |
|---|---|
| « Nouvelle démo VIBRAAXIS en bass house » | `produire-demo-electro-rapide`, après l'ouverture de séance par `ableton-live-session` et `memoire-projet` |
| « On reprend » | `memoire-projet` (`reprise.sh`) ; `chef-de-projet` si plusieurs morceaux sont en cours |
| « Où on en est ? », « on fait quoi maintenant ? » | `chef-de-projet` (tableau de bord, prochaine étape) |
| « La basse du drop », « corrige le master » | `ableton-live-session`, puis la chaîne donnée par sa carte |

En session cloud (claude.ai/code), ni Live ni Mac : seulement les skills, les grilles, la théorie et les contrôles.

## Installer les skills pour tous les projets (sur le Mac)

`outils/installer.sh` copie les skills dans `~/.claude/skills` et relie `~/.qwen/skills`. Sans `--appliquer`, c'est une **simulation** : rien n'est écrit, la liste de ce qui changerait est affichée.

```bash
bash outils/installer.sh --help
bash outils/installer.sh                                      # simulation, pour chaque outil dont le dossier existe (~/.claude, ~/.qwen)
bash outils/installer.sh --claude --qwen --appliquer          # installe pour les deux outils
bash outils/installer.sh --skill drums-signature --appliquer  # un seul skill (--skill est répétable)
bash outils/installer.sh --producer-pal-qwen --appliquer      # déclare Producer Pal dans ~/.qwen/settings.json
```

- `--claude` copie chaque skill dans `~/.claude/skills/<nom>`.
- `--qwen` fait de `~/.qwen/skills/<nom>` un lien vers la copie Claude : une seule copie installée pour les deux outils. Sans copie Claude, le skill est copié ; d'où `--claude --qwen` ensemble.
- Une version installée différente n'est pas écrasée : elle est déplacée dans `~/.skills-sauvegardes/<date>/<outil>/`, hors des dossiers de skills (une copie laissée à côté serait chargée comme un second skill du même nom).
- Le registre de signature de `drums-signature` (`references/signature.md`, `scripts/signature.json`) est conservé s'il a changé depuis l'installation.
- `--producer-pal-qwen` ajoute le serveur MCP (`npx producer-pal@latest`) sans toucher au reste du fichier, s'il n'y est pas déjà. Il faut Node.js 20+ et le device `Producer_Pal.amxd` dans le Set ; vérifier par `/mcp` dans Qwen Code.
- Relancer Claude Code ou Qwen Code après l'installation pour recharger les skills.

## Claude Code et Qwen Code

Détail dans `QWEN.md` et dans le skill `piloter-live-lombridge-codex`.

- Mêmes skills, mêmes règles (`AGENTS.md`) et **même mémoire de projet** (`memoire-projet`, `MEM_DIR`) : ce que l'un note, l'autre le reprend.
- Claude Code agit dans Live par Producer Pal, `lom.py` et le contrôle d'écran (menus, export, fenêtres de plug-ins).
- Qwen Code agit dans Live **uniquement** par `lom-bridge/agent_gateway.py` (`inspect`, puis `preview`, accord de l'utilisateur, `commit`), avec le serveur `lom.py serve` lancé par l'utilisateur ou par Claude ; jamais `lom.py`, `curl`, l'UDP ni `/py`.
- Pas de contrôle d'écran ni d'accès aux vidéos pour Qwen : il demande le geste (Sauver Set Live sous…, export, fenêtre de Serum) ou la transcription, attend la confirmation, puis relit l'état.
- Producer Pal est optionnel côté Qwen (`--producer-pal-qwen`) ; sans lui, Qwen livre la grille vérifiée ou la valeur exacte, que l'utilisateur ou Claude applique.
- Qwen ne modifie ni les skills ni le bridge : il propose le changement, l'utilisateur décide.

## Skills ajoutés depuis le pack VIBRA du 30 sept. 2026

| Skill | Rôle |
|---|---|
| `produire-demo-electro-rapide` | démo VIBRA jouable : brief, référence, émotions, noyau de 8 mesures, Original Mix et Extended Mix |
| `composer-trajectoire-emotionnelle` | ambiance et une à quatre émotions placées en mesures, perception testée à l'écoute par l'utilisateur |
| `produire-avec-maschine-mk3` | grooves, kits, patterns, scènes et Perform FX sur Maschine MK3, puis intégration dans Live |
| `bass-house-sound-design` | stabs, pads, leads et impacts Bass House (Serum 2, Wavetable, effets spectraux de Live) |
| `construire-low-end-electronique` | grave électronique (kick, sub, basse, 808) : procédure, recettes par genre, symptôme → preuve → changement |
| `mixer-house-professionnel` | mix Bass House, Future Rave, Tech House et Minimal : priorités du genre, A/B de références, versions streaming et club |
| `theorie-musicale-composition` | théorie et écriture hors électro (classique, jazz, pop, film…) et cours avec exercices corrigés |
| `piloter-live-lombridge-codex` | procédure d'un agent autre que Claude Code (Qwen Code, Codex) par `agent_gateway.py`, bilan de séance |

Les versions du pack de `composer-hooks-funk-electro`, `serum-2-basses-house-future-house` et `produire-morceau-electronique-de-a-a-z` étaient antérieures aux versions corrigées du dépôt, qui ont été gardées. Le client `agent_gateway.py` du pack (v0.4) n'a pas été repris : le serveur 0.8.1 le refuse. Seul `lom-bridge/agent_gateway.py` est à utiliser.

## Contrôles

Depuis la racine du dépôt, hors Live ; aucun ne modifie le dépôt ni les copies installées.

```bash
python3 outils/verifier_skills.py                           # en-têtes, chemins cités, copies jumelles, lien .qwen, carte
python3 -m unittest discover -s outils -p 'test_*.py' -v    # installateur (HOME temporaire) et vérificateur
(cd lom-bridge && python3 -W ignore -m unittest tests/test_offline.py tests/test_gateway.py -v)   # bridge : 60 + 16 tests
(cd .claude/skills/composer-hooks-funk-electro && python3 scripts/grille.py --verifier references/*.md)
(cd .claude/skills/serum-2-basses-house-future-house && python3 ../composer-hooks-funk-electro/scripts/grille.py --verifier references/*.md)
```

Les deux dernières lignes vérifient les grilles MIDI (C3 = 60) écrites dans les skills. La CI lance les mêmes contrôles : `skills.yml` (vérificateur, tests d'`outils/`, syntaxe de tous les scripts Python des skills, tests et grilles) quand les skills, `.qwen`, `outils/` ou les fichiers `AGENTS.md`, `CLAUDE.md`, `QWEN.md` changent ; `tests.yml` (tests du bridge sous Python 3.11 et 3.12) quand `lom-bridge/` change.

## Modifier un skill

1. Modifier dans ce dépôt, jamais dans `~/.claude/skills` ni `~/.qwen/skills` : la prochaine installation remplacerait la copie installée.
2. `python3 outils/verifier_skills.py`, et les tests ci-dessus si un script a changé.
3. Commit.
4. Sur le Mac : `bash outils/installer.sh` (simulation), puis `bash outils/installer.sh --appliquer`, et relancer Claude Code / Qwen Code.

Copies jumelles : certains fichiers de `bass-house-sound-design`, `mixer-house-professionnel`, `theorie-musicale-composition` et `piloter-live-lombridge-codex` sont aussi dans le corpus de `produire-morceau-electronique-de-a-a-z`. Les corriger ensemble dans les deux fichiers : le vérificateur refuse deux jumeaux différents.
