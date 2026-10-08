# Regroupement des 44 skills en 5 — plan

État : **plan soumis le 8 oct. 2026, rien n'est encore déplacé.** Une fois validé, ce fichier devient la description de la structure des skills (modules, conventions, comment en ajouter un).

Base : `main` après la fusion de [#13](https://github.com/maileytsil-gif/tsila/pull/13). Mesures du dépôt : 44 skills, 437 fichiers, 9,2 Mo, 340 Ko de `SKILL.md` cumulés, 43 scripts, 1 153 renvois `../autre-skill/` entre skills, 17 paires de copies jumelles.

## 1. Pourquoi cinq et pas un

- La description d'un skill (≤ 1 024 caractères) est ce que l'agent lit pour choisir : 44 listes de mots déclencheurs ne tiennent pas dans une seule. Cinq descriptions, une par métier, restent lisibles.
- Les 340 Ko de `SKILL.md` ne tiennent pas dans un seul fichier chargé à chaque appel ; cinq routeurs de 15 à 22 Ko, oui.
- Les quatre rôles existants (`compositeur-arrangeur`, `producteur-rythmique`, `sound-designer-serum`, `ingenieur-mixage`) sont déjà des têtes de chapitre : chacun orchestre des skills spécialisés et dit quand passer la main. Le cinquième regroupe ce qui pilote la séance et le morceau entier.

## 2. Les cinq skills et leurs modules

Chaque ancien skill devient un **module** du nouveau, déplacé entier (`git mv`, historique conservé). Le rôle actuel fournit le `SKILL.md` du skill regroupé.

| Skill regroupé | Modules (anciens skills) | Fichiers | Taille |
|---|---|---|---|
| **compositeur-arrangeur** (notes, harmonie, forme) | compositeur-arrangeur (rôle), melodie-composition, composer-hooks-funk-electro, arrangement-avance, midi-expressif, composer-trajectoire-emotionnelle, theorie-musicale-electronique, theorie-musicale-composition, partition-recherche, partition-telechargement, sampling-composition-avancee | 62 | 0,84 Mo |
| **producteur-rythmique** (batterie, groove, grave) | producteur-rythmique (rôle), drums-signature, kick-bass-equilibre, construire-low-end-electronique, native-instruments-control, produire-avec-maschine-mk3 | 32 | 0,66 Mo |
| **sound-designer-serum** (timbres, Serum 2, VST, capture) | sound-designer-serum (rôle), vst-sound-design, serum-2-basses-house-future-house, bass-house-sound-design, studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design, synthese-reference, resampling | 138 | 2,4 Mo |
| **ingenieur-mixage** (mix, mastering, export) | ingenieur-mixage (rôle), mixage, effets-plugins, mixer-house-professionnel, live-mix-mastering, mastering-outils, live-export-wav | 31 | 0,69 Mo |
| **producteur-live** (séance, mémoire, projet, morceau entier, Suno) | ableton-live-session (discipline, bridge, carte d'entrée), memoire-projet, memoire-persistante, chef-de-projet, piloter-live-lombridge-codex, produire-demo-electro-rapide, produire-morceau-electronique-de-a-a-z, maitriser-suno, suno-vocals, house-future-rave-bass-house-production, electronic-production-engineer, live-automation | 174 | 4,8 Mo (1,4 sans le storyboard PNG) |

Placements qui méritent une raison :

- `midi-expressif` est appelé par les deux premiers rôles ; il agit sur les notes (vélocités, durées, articulations), donc **compositeur-arrangeur**.
- `kick-bass-equilibre` (72 renvois entrants) est utilisé par le mix aussi ; le rôle `producteur-rythmique` l'orchestre déjà et la carte l'enchaîne avec `construire-low-end-electronique`, donc **producteur-rythmique**.
- `sampling-composition-avancee` compose à partir de samples (harmonie, conduite des voix) → **compositeur-arrangeur** ; la capture (`resampling`) reste en **sound design**, comme le rôle le prévoit.
- `live-automation` est une opération du bridge appelée par l'arrangement comme par le mix ; aucun rôle ne la revendique → **producteur-live**, à côté d'`ableton-live-session`.
- `house-future-rave-bass-house-production` et `electronic-production-engineer` sont des pipelines entiers (sound design + arrangement + mix + masters) → **producteur-live**, avec le skill A à Z. EPE reste tel quel (anglais, versionné, lanceur Ollama).

## 3. Structure d'un skill regroupé

```text
sound-designer-serum/
  SKILL.md                      ← routeur : rôle (méthode actuelle, règles communes, passer la main)
                                   + carte « situation → module » + une ligne par module
  modules/
    vst-sound-design/
      GUIDE.md                  ← ancien SKILL.md : en-tête YAML retiré, titre H1 gardé,
      references/…               ligne « Module du skill `sound-designer-serum` » ajoutée
      scripts/…
    serum-2-basses-house-future-house/
    …
```

Conventions :

- **Aucun `SKILL.md` sous `modules/`** (un chargeur qui lirait les sous-dossiers y verrait des skills). L'entrée d'un module s'appelle `GUIDE.md`.
- Un module garde ses `references/`, `scripts/`, `recipes/`, `assets/` tels quels ; ses chemins internes ne changent pas.
- Renvois réécrits par script : même skill, `../x/SKILL.md` → `../x/GUIDE.md` (les modules sont voisins dans `modules/`, le reste du chemin tient) ; autre skill, `../x/…` → `../../../<skill>/modules/x/…`. Le vérificateur refuse tout renvoi cassé.
- Le `SKILL.md` du rôle devient celui du skill : sa méthode et son « passer la main » restent, la liste de ses bibliothèques devient la carte des modules. Pour `producteur-live`, le `SKILL.md` part d'`ableton-live-session` (19 Ko), dont la carte « situation → skills » est réécrite en « situation → skill › module » sans s'allonger.
- Les cinq descriptions sont réécrites en listes de mots déclencheurs couvrant tous les modules, ≤ 1 024 caractères (contrôlé par le vérificateur).

## 4. Ce qui change hors des skills

| Fichier | Changement |
|---|---|
| `outils/verifier_skills.py` | résolution des chemins depuis la racine du module en plus de celle du skill ; jetons `modules/<x>/…`, `../<x>/GUIDE.md`, `../../../<skill>/modules/<x>/…` ; carte = `producteur-live` ; règle 6 : chaque module est cité dans le `SKILL.md` de son skill et dans la carte, plus de nombre annoncé dans la description ; règle nouvelle : pas de `SKILL.md` sous `modules/`, chaque `GUIDE.md` commence par un H1 ; copies jumelles et fichier portable selon la décision 2 ; noms de modules reconnus dans les fichiers racine |
| `outils/installer.sh` | données de l'utilisateur : `producteur-rythmique/modules/drums-signature/references/signature.md` et `scripts/signature.json` ; **option `--retirer-absents`** : tout dossier de `~/.claude/skills` et tout lien de `~/.qwen/skills` dont le nom n'est pas un skill du dépôt est déplacé dans `~/.skills-sauvegardes/<date>/` (jamais supprimé), simulation par défaut. Sans cela, les 44 anciens skills installés resteraient chargés à côté des 5 nouveaux |
| `outils/test_outils.py` | noms de skills (`resampling` → `sound-designer-serum`…), test du registre de signature, test de `--retirer-absents`, tests des jumeaux selon la décision 2 |
| `.github/workflows/skills.yml` | `working-directory` des grilles : `…/compositeur-arrangeur/modules/composer-hooks-funk-electro` et `…/sound-designer-serum/modules/serum-2-basses-house-future-house` |
| `README.md`, `AGENTS.md`, `CLAUDE.md`, `QWEN.md` | tableaux « par où entrer », compteur 44, liste des skills du pack, section « copies jumelles », « modifier un skill » |
| `corpus/INDEX.md`, `corpus/index.json`, `docs/claude-code-avec-ollama.md` | noms de skills → `skill › module` |
| `.claude/settings.json` | `skillListingBudgetFraction` 0,03 devient inutile (cinq descriptions ≈ 5 Ko) ; laissé ou retiré, sans effet |
| Scripts qui citent `SKILL.md` ou un autre skill | `composer-hooks-funk-electro/scripts/install.sh` (installe ce seul skill pour Claude, Codex et Qwen-Ollama : à faire installer `compositeur-arrangeur` entier ou à retirer au profit d'`outils/installer.sh`), `qwen-musique.py`, `electronic-production-engineer/ollama/run_skill.py`, `scripts/validate_skill.py`, `MANIFEST.json` (listent `SKILL.md` → `GUIDE.md`), `melodie-composition/scripts/check_scale.py` |

Sur le Mac, hors dépôt : la mémoire de projet (`projet-*.md`) cite les anciens noms ; rien à changer, ils restent les noms des modules.

## 5. Ce que tu gagnes et ce que tu perds

- **Gagné** : cinq points d'entrée au lieu de 44 ; une description par métier ; plus de concurrence entre skills sur une même demande ; un seul endroit par métier pour les règles communes.
- **Perdu** : les commandes `/chef-de-projet`, `/maitriser-suno`, `/memoire-projet`… Il reste `/producteur-live` suivi de la demande (« fais le point », « prompt Suno », « on reprend ») ou une demande naturelle ; le routeur fait le reste.
- **Non testable ici** : le déclenchement automatique. Il se vérifie sur le Mac après installation (trois demandes témoins : « la basse du drop », « où on en est », « c'est boueux »). `AGENTS.md` « Par où entrer » reste la carte de secours.

## 6. Décisions à prendre avant d'exécuter

1. **Nom du cinquième skill** : `producteur-live` (recommandé) ; sinon `production-live`, `producteur-electronique`, ou garder `ableton-live-session`.
2. **Copies jumelles (17 paires) et fichier portable** : les supprimer et les remplacer par des renvois (recommandé : plus de doublons à tenir à jour, vérificateur allégé ; un usage « A à Z seul » sous Ollama copie les cinq skills) ; ou les garder, chemins mis à jour.
3. **Storyboard du clip « Après les heures »** (`piloter-live-lombridge-codex/assets/…png`, 3,4 Mo) : le déplacer dans `docs/projets/` (recommandé : c'est une donnée de projet, pas une méthode ; `producteur-live` pèse alors 1,4 Mo au lieu de 4,8) ; ou le laisser.

## 7. Déroulé d'exécution (une PR, étape par étape)

1. `outils/regrouper_skills.py` (gardé dans le dépôt) : table de correspondance, `git mv` de chaque skill vers `<skill>/modules/<ancien>/`, `SKILL.md` → `GUIDE.md`, réécriture des renvois, création des cinq `SKILL.md`.
2. Outils : vérificateur, installateur, tests, CI.
3. Textes : `README.md`, `AGENTS.md`, `CLAUDE.md`, `QWEN.md`, corpus, docs ; ce fichier devient la doc de structure.
4. Contrôles : `verifier_skills.py`, `test_outils.py`, `py_compile` de tous les scripts, tests et grilles de `composer-hooks-funk-electro`, grilles de `serum-2-basses-house-future-house` ; tests du bridge inchangés.
5. Relecture des cinq descriptions et des cinq routeurs.
6. PR en brouillon. Après fusion, sur le Mac : `bash outils/installer.sh --retirer-absents` (simulation), puis `--appliquer`, relancer Claude Code et Qwen Code, trois demandes témoins.
