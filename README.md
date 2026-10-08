# tsila

Workflow de production musicale (Ableton Live 12, Serum 2, Maschine MK3) piloté dans le terminal par Claude Code et Qwen Code : des skills, un pont vers Live (LOM Bridge) et des outils de contrôle.

## Contenu du dépôt

| Chemin | Rôle |
|---|---|
| `.claude/skills/` | les **cinq skills** du workflow, **source unique**, chacun avec ses modules (`<skill>/modules/<module>/GUIDE.md` : les 44 anciens skills, déplacés entiers le 8 oct. 2026 ; correspondance et conventions dans `docs/regroupement-skills.md`) |
| `.claude/settings.json` | réglage de projet de Claude Code : `skillListingBudgetFraction` 0,03, soit 3 % du contexte pour la liste des skills (1 % par défaut) ; nécessaire avec 44 descriptions, sans effet avec cinq, laissé |
| `.qwen/skills` | lien vers `../.claude/skills` : Qwen Code lit exactement les mêmes fichiers |
| `.qwen/settings.json` | `context.fileName` : Qwen Code charge `AGENTS.md` et `QWEN.md` |
| `AGENTS.md` | règles communes à tous les agents : par où entrer, règles de chaque morceau, règles du workflow |
| `CLAUDE.md` | lu par Claude Code : importe `AGENTS.md` et ajoute ce qui est propre à Claude |
| `QWEN.md` | lu par Qwen Code avec `AGENTS.md` : différences avec Claude Code, consignes, installation |
| `lom-bridge/` | LOM Bridge 0.8.3 : Remote Script de Live, `lom.py`, `agent_gateway.py`, tests hors Live ; installation dans `lom-bridge/README.md` |
| `outils/` | `installer.sh` (installation des skills), `verifier_skills.py` (contrôle), `test_outils.py` (leurs tests), `regrouper_skills.py` (regroupement 44 → 5 du 8 oct. 2026, gardé pour la correspondance et les règles de réécriture) |
| `.github/workflows/` | `skills.yml` et `tests.yml` : les contrôles ci-dessous, lancés à chaque push et pull request |

## Démarrer

Lancer l'outil dans le dossier du dépôt :

```bash
cd tsila
claude      # Claude Code : lit CLAUDE.md (qui importe AGENTS.md) et les skills de .claude/skills
qwen        # Qwen Code : lit AGENTS.md et QWEN.md, et les mêmes skills par le lien .qwen/skills
```

- Un skill s'appelle par `/nom-du-skill` (par exemple `/producteur-live`) ou par une demande en langage naturel ; un ancien skill est un module, qu'on nomme dans la demande (« fais le point » ouvre le module `chef-de-projet`). Dans Qwen Code, `/skills` les liste et `/memory` montre que `AGENTS.md` et `QWEN.md` sont chargés.
- `producteur-live` contient la carte « situation → skill › module » : elle dit quel skill prend la main, quel module ouvrir et lesquels suivent.
- L'agent annonce le plan complet puis exécute ou fait valider **une étape par échange** ; il relit l'état réel de Live avant d'agir.

Les cinq skills et leurs modules :

Les modules marqués « pack v18 » (intégrés le 8 oct. 2026) fournissent la matière musicale ; les modules maison décident et exécutent (`docs/integration-pack-v18.md`).

| Skill | Rôle | Modules |
|---|---|---|
| `producteur-live` | séance Live (discipline, bridge, écran), mémoire, projet, morceau entier, Suno, autre agent ; porte d'entrée et carte | memoire-projet, memoire-persistante, chef-de-projet, produire-demo-electro-rapide, produire-morceau-electronique-de-a-a-z, house-future-rave-bass-house-production, electronic-production-engineer, maitriser-suno, suno-vocals, live-automation, piloter-live-lombridge-codex ; pack v18 : composer-producer-director, bass-house-ableton-bridge |
| `compositeur-arrangeur` | notes, harmonie, forme, théorie, émotion | melodie-composition, composer-hooks-funk-electro, arrangement-avance, midi-expressif, composer-trajectoire-emotionnelle, theorie-musicale-electronique, theorie-musicale-composition, partition-recherche, partition-telechargement, sampling-composition-avancee ; pack v18 : bass-house-composition, modern-pop-electronic-music-theory, modern-jazz-chillout-theory, afro-caribbean-latin-detroit-theory |
| `producteur-rythmique` | batterie, groove, grave, Maschine | drums-signature, kick-bass-equilibre, construire-low-end-electronique, native-instruments-control, produire-avec-maschine-mk3 ; pack v18 : studio-grade-kick-low-end-sound-design, studio-grade-drums-electronic-percussion |
| `sound-designer-serum` | timbres, Serum 2, VST, capture | vst-sound-design, serum-2-basses-house-future-house, bass-house-sound-design, studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design, synthese-reference, resampling ; pack v18 : bass-house-serum2-sound-design, studio-grade-bass-sound-design, studio-grade-sample-vocal-break-design, studio-grade-transition-fx-director |
| `ingenieur-mixage` | mix, mastering, export | mixage, effets-plugins, mixer-house-professionnel, live-mix-mastering, mastering-outils, live-export-wav ; pack v18 : bass-house-mixing-mastering |

Premières demandes possibles :

| Vous écrivez | Skill › module qui prend la main |
|---|---|
| « Nouvelle démo VIBRAAXIS en bass house » | `producteur-live` › produire-demo-electro-rapide, après l'ouverture de séance (discipline de `producteur-live`, module memoire-projet) |
| « On reprend » | `producteur-live` › memoire-projet (`reprise.sh`) ; chef-de-projet si plusieurs morceaux sont en cours |
| « Où on en est ? », « on fait quoi maintenant ? » | `producteur-live` › chef-de-projet (tableau de bord, prochaine étape) |
| « La basse du drop », « corrige le master » | `producteur-live` (discipline de séance), puis `sound-designer-serum` ou `ingenieur-mixage` selon sa carte |

En session cloud (claude.ai/code), ni Live ni Mac : seulement les skills, les grilles, la théorie et les contrôles.

## Installer les skills pour tous les projets (sur le Mac)

`outils/installer.sh` copie les skills dans `~/.claude/skills` et relie `~/.qwen/skills`. Sans `--appliquer`, c'est une **simulation** : rien n'est écrit, la liste de ce qui changerait est affichée.

```bash
bash outils/installer.sh --help
bash outils/installer.sh                                      # simulation, pour chaque outil dont le dossier existe (~/.claude, ~/.qwen)
bash outils/installer.sh --claude --qwen --appliquer          # installe pour les deux outils
bash outils/installer.sh --skill producteur-rythmique --appliquer  # un seul skill, modules compris (--skill est répétable)
bash outils/installer.sh --retirer-absents --appliquer        # écarte les skills installés qui ne sont plus dans le dépôt (les 44 anciens)
bash outils/installer.sh --producer-pal-qwen --appliquer      # déclare Producer Pal dans ~/.qwen/settings.json
```

- `--claude` copie chaque skill, avec ses modules, dans `~/.claude/skills/<nom>`.
- `--qwen` fait de `~/.qwen/skills/<nom>` un lien vers la copie Claude : une seule copie installée pour les deux outils. Sans copie Claude, le skill est copié ; d'où `--claude --qwen` ensemble.
- Une version installée différente n'est pas écrasée : elle est déplacée dans `~/.skills-sauvegardes/<date>/<outil>/`, hors des dossiers de skills (une copie laissée à côté serait chargée comme un second skill du même nom).
- `--retirer-absents` déplace de la même façon tout skill installé (dossier ou lien) qui n'existe plus dans le dépôt : à lancer une fois après le regroupement en cinq skills, sinon les 44 anciens restent chargés à côté des cinq nouveaux. Rien n'est supprimé.
- Le registre de signature du module `drums-signature` (`references/signature.md`, `scripts/signature.json`) est conservé s'il a changé depuis l'installation.
- `--producer-pal-qwen` ajoute le serveur MCP (`npx producer-pal@latest`) sans toucher au reste du fichier, s'il n'y est pas déjà. Il faut Node.js 20+ et le device `Producer_Pal.amxd` dans le Set ; vérifier par `/mcp` dans Qwen Code.
- Relancer Claude Code ou Qwen Code après l'installation pour recharger les skills.

## Claude Code et Qwen Code

Détail dans `QWEN.md` et dans le module `piloter-live-lombridge-codex` de `producteur-live`.

- Mêmes skills, mêmes règles (`AGENTS.md`) et **même mémoire de projet** (module `memoire-projet`, `MEM_DIR`) : ce que l'un note, l'autre le reprend.
- Claude Code agit dans Live par Producer Pal, `lom.py` et le contrôle d'écran (menus, export, fenêtres de plug-ins).
- Qwen Code agit dans Live **uniquement** par `lom-bridge/agent_gateway.py` (`inspect`, puis `preview`, accord de l'utilisateur, `commit`), avec le serveur `lom.py serve` lancé par l'utilisateur ou par Claude ; jamais `lom.py`, `curl`, l'UDP ni `/py`.
- Pas de contrôle d'écran ni d'accès aux vidéos pour Qwen : il demande le geste (Sauver Set Live sous…, export, fenêtre de Serum) ou la transcription, attend la confirmation, puis relit l'état.
- Producer Pal est optionnel côté Qwen (`--producer-pal-qwen`) ; sans lui, Qwen livre la grille vérifiée ou la valeur exacte, que l'utilisateur ou Claude applique.
- Qwen ne modifie ni les skills ni le bridge : il propose le changement, l'utilisateur décide.

## Modules ajoutés depuis le pack VIBRA du 30 sept. 2026

| Module (skill) | Rôle |
|---|---|
| `produire-demo-electro-rapide` (producteur-live) | démo VIBRA jouable : brief, référence, émotions, noyau de 8 mesures, Original Mix et Extended Mix |
| `composer-trajectoire-emotionnelle` (compositeur-arrangeur) | ambiance et une à quatre émotions placées en mesures, perception testée à l'écoute par l'utilisateur |
| `produire-avec-maschine-mk3` (producteur-rythmique) | grooves, kits, patterns, scènes et Perform FX sur Maschine MK3, puis intégration dans Live |
| `bass-house-sound-design` (sound-designer-serum) | stabs, pads, leads et impacts Bass House (Serum 2, Wavetable, effets spectraux de Live) |
| `construire-low-end-electronique` (producteur-rythmique) | grave électronique (kick, sub, basse, 808) : procédure, recettes par genre, symptôme → preuve → changement |
| `mixer-house-professionnel` (ingenieur-mixage) | mix Bass House, Future Rave, Tech House et Minimal : priorités du genre, A/B de références, versions streaming et club |
| `theorie-musicale-composition` (compositeur-arrangeur) | théorie et écriture hors électro (classique, jazz, pop, film…) et cours avec exercices corrigés |
| `piloter-live-lombridge-codex` (producteur-live) | procédure d'un agent autre que Claude Code (Qwen Code, Codex) par `agent_gateway.py`, bilan de séance |

Les versions du pack de `composer-hooks-funk-electro`, `serum-2-basses-house-future-house` et `produire-morceau-electronique-de-a-a-z` étaient antérieures aux versions corrigées du dépôt, qui ont été gardées. Le client `agent_gateway.py` du pack (v0.4) n'a pas été repris : le serveur 0.8.1 le refuse. Seul `lom-bridge/agent_gateway.py` est à utiliser.

## Contrôles

Depuis la racine du dépôt, hors Live ; aucun ne modifie le dépôt ni les copies installées.

```bash
python3 outils/verifier_skills.py                           # en-têtes, modules, chemins cités, lien .qwen, carte
python3 -m unittest discover -s outils -p 'test_*.py' -v    # installateur (HOME temporaire) et vérificateur
(cd lom-bridge && python3 -W ignore -m unittest tests/test_offline.py tests/test_gateway.py -v)   # bridge : 60 + 16 tests
(cd .claude/skills/compositeur-arrangeur/modules/composer-hooks-funk-electro && python3 scripts/grille.py --verifier references/*.md)
(cd .claude/skills/sound-designer-serum/modules/serum-2-basses-house-future-house && python3 ../../../compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/grille.py --verifier references/*.md)
```

Les deux dernières lignes vérifient les grilles MIDI (C3 = 60) écrites dans les skills. La CI lance les mêmes contrôles : `skills.yml` (vérificateur, tests d'`outils/`, syntaxe de tous les scripts Python des skills, tests et grilles) quand les skills, `.qwen`, `outils/` ou les fichiers `AGENTS.md`, `CLAUDE.md`, `QWEN.md` changent ; `tests.yml` (tests du bridge sous Python 3.11 et 3.12) quand `lom-bridge/` change.

## Modifier un skill ou un module

1. Modifier dans ce dépôt, jamais dans `~/.claude/skills` ni `~/.qwen/skills` : la prochaine installation remplacerait la copie installée.
2. `python3 outils/verifier_skills.py`, et les tests ci-dessus si un script a changé.
3. Commit.
4. Sur le Mac : `bash outils/installer.sh` (simulation), puis `bash outils/installer.sh --appliquer`, et relancer Claude Code / Qwen Code.

Structure : un skill est `.claude/skills/<skill>/SKILL.md` (en-tête YAML, méthode du rôle, tableau « Modules de ce skill ») ; un module est `<skill>/modules/<module>/GUIDE.md` (titre H1, pas d'en-tête YAML, jamais de `SKILL.md` sous `modules/`, sinon il serait chargé comme un skill de plus) avec ses `references/`, `scripts/`, `recipes/`. Renvois : `../<module>/…` entre modules d'un même skill, `../../../<skill>/modules/<module>/…` vers un module d'un autre skill, `../../` vers le skill parent (son `SKILL.md`, ses `references/`) ; ils se lisent depuis la racine du module. Pour ajouter un module : un dossier dans `modules/`, son `GUIDE.md`, une ligne dans le tableau du `SKILL.md` et dans la carte de `producteur-live` ; le vérificateur refuse l'oubli.
