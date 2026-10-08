# Les cinq skills et leurs modules

État : **regroupement exécuté le 8 oct. 2026** (plan validé le même jour). Ce fichier décrit la structure qui en résulte, la correspondance des 44 anciens skills et les conventions à respecter pour modifier ou ajouter un module. Le script qui a fait le déplacement, `outils/regrouper_skills.py`, reste dans le dépôt pour documenter la table de correspondance et les règles de réécriture des renvois.

## 1. Pourquoi cinq et pas 44, ni un seul

- La description d'un skill (≤ 1 024 caractères) est ce que l'agent lit pour choisir : 44 listes de mots déclencheurs se concurrençaient sur une même demande ; une seule n'aurait pas pu les contenir. Cinq descriptions, une par métier, listent les mots déclencheurs de tous leurs modules.
- Les 340 Ko de `SKILL.md` cumulés ne tenaient pas dans un seul fichier chargé à chaque appel ; cinq routeurs de 15 à 22 Ko, oui.
- Les quatre rôles existants (`compositeur-arrangeur`, `producteur-rythmique`, `sound-designer-serum`, `ingenieur-mixage`) étaient déjà des têtes de chapitre ; le cinquième, `producteur-live`, regroupe ce qui pilote la séance et le morceau entier et porte la carte d'entrée.

## 2. Correspondance

Chaque ancien skill est devenu un **module**, déplacé entier (`git mv`, historique conservé). Le skill de base de chaque groupe a fourni le `SKILL.md` du skill regroupé (`ableton-live-session` est devenu `producteur-live`).

| Skill | Modules (anciens skills) |
|---|---|
| **producteur-live** (ex `ableton-live-session` : discipline de séance, bridge, écran, carte) | memoire-projet, memoire-persistante, chef-de-projet, piloter-live-lombridge-codex, produire-demo-electro-rapide, produire-morceau-electronique-de-a-a-z, maitriser-suno, suno-vocals, house-future-rave-bass-house-production, electronic-production-engineer, live-automation |
| **compositeur-arrangeur** (notes, harmonie, forme) | melodie-composition, composer-hooks-funk-electro, arrangement-avance, midi-expressif, composer-trajectoire-emotionnelle, theorie-musicale-electronique, theorie-musicale-composition, partition-recherche, partition-telechargement, sampling-composition-avancee |
| **producteur-rythmique** (batterie, groove, grave) | drums-signature, kick-bass-equilibre, construire-low-end-electronique, native-instruments-control, produire-avec-maschine-mk3 |
| **sound-designer-serum** (timbres, Serum 2, VST, capture) | vst-sound-design, serum-2-basses-house-future-house, bass-house-sound-design, studio-grade-brass-sound-design, studio-grade-funk-keys-synth-sound-design, synthese-reference, resampling |
| **ingenieur-mixage** (mix, mastering, export) | mixage, effets-plugins, mixer-house-professionnel, live-mix-mastering, mastering-outils, live-export-wav |

Placements qui méritent une raison : `midi-expressif` agit sur les notes (compositeur) bien que le rythme l'appelle ; `kick-bass-equilibre` est orchestré par le rôle rythmique et le mix y renvoie ; `sampling-composition-avancee` compose à partir de samples (compositeur), la capture `resampling` reste en sound design ; `live-automation` est une opération du bridge, donc `producteur-live` ; `house-future-rave-bass-house-production` et `electronic-production-engineer` sont des pipelines entiers, donc `producteur-live`.

## 3. Structure et conventions

```text
sound-designer-serum/
  SKILL.md                      ← en-tête YAML, méthode du rôle, « passer la main », tableau « Modules de ce skill »
  references/…                  ← fiches du rôle (seuls sound-designer-serum et producteur-live en ont)
  modules/
    vst-sound-design/
      GUIDE.md                  ← ancien SKILL.md : titre H1, puis « > Module du skill `…`. <ancienne description> »
      references/… scripts/…
    serum-2-basses-house-future-house/
    …
```

- **Jamais de `SKILL.md` sous `modules/`** : il serait chargé comme un skill de plus. L'entrée d'un module s'appelle `GUIDE.md` et commence par un titre H1. Quatorze anciens skills commençaient sans titre : ils en ont reçu un (table `TITRES` du script).
- Un module garde ses `references/`, `scripts/`, `recipes/`, `assets/` ; ses chemins internes n'ont pas changé.
- **Renvois**, lus par convention depuis la racine du module (le vérificateur accepte aussi le dossier du fichier, la racine du skill, `.claude/skills/` et la racine du dépôt) : `../<module>/…` entre modules d'un même skill ; `../../../<skill>/modules/<module>/…` vers un module d'un autre skill ; `../../SKILL.md` et `../../references/…` vers le skill parent ; `../../../<skill>/SKILL.md` vers un autre skill ; `../../../../../corpus/…` vers la racine du dépôt depuis la racine d'un module (`.claude/skills/` compte pour deux niveaux).
- Les cinq descriptions (≤ 1 024 caractères, contrôlées) listent les mots déclencheurs de tous leurs modules. Chaque `SKILL.md` se termine par le tableau « Modules de ce skill » (module, quand l'ouvrir, entrée). `producteur-live/SKILL.md` porte en plus « Où sont les modules » et la carte « situation → skill › module ».
- Les 17 paires de copies jumelles et le fichier portable Bass House ont été supprimés : le module `produire-morceau-electronique-de-a-a-z` renvoie aux modules `bass-house-sound-design`, `mixer-house-professionnel`, `theorie-musicale-composition` et `piloter-live-lombridge-codex` (dont `session_review.py`). Le storyboard du clip « Après les heures » (3,4 Mo) est dans `docs/projets/`.

## 4. Ajouter ou modifier un module

1. Modifier dans ce dépôt, jamais dans une copie installée.
2. Nouveau module : un dossier dans `modules/`, son `GUIDE.md` (H1 puis ligne « Module du skill … »), une ligne dans le tableau « Modules de ce skill » du `SKILL.md`, une ligne ou une mention dans la carte de `producteur-live`. Mots déclencheurs importants : les ajouter à la description du skill, sans dépasser 1 024 caractères.
3. `python3 outils/verifier_skills.py` (en-têtes, modules, chemins, lien `.qwen`, carte) et, si un script a changé, les tests listés dans `README.md`.
4. Commit à la demande de l'utilisateur ; sur le Mac, `bash outils/installer.sh --appliquer`.

## 5. Ce qui a changé hors des skills

| Fichier | Changement |
|---|---|
| `outils/verifier_skills.py` | résolution depuis la racine du module ; jetons `modules/<x>/…`, `../<x>/GUIDE.md`, `../../SKILL.md` ; carte = `producteur-live`, plus de nombre annoncé ; règles « GUIDE.md avec H1 », « pas de SKILL.md sous modules/ », « module cité dans son SKILL.md et dans la carte » ; copies jumelles et portable retirés ; noms de modules reconnus dans les fichiers racine |
| `outils/installer.sh` | données de l'utilisateur sous `producteur-rythmique/modules/drums-signature/` ; option `--retirer-absents` (déplace dans `~/.skills-sauvegardes/` tout skill installé absent du dépôt, sans rien supprimer) |
| `outils/test_outils.py` | tests sur `ingenieur-mixage`, registre de signature, `--retirer-absents`, `SKILL.md` sous `modules/` refusé, module absent ou non cité |
| `.github/workflows/skills.yml` | chemins des modules pour les grilles et les tests de `composer-hooks-funk-electro` ; `py_compile` d'`outils/` |
| `README.md`, `AGENTS.md`, `CLAUDE.md`, `QWEN.md`, `docs/claude-code-avec-ollama.md` | cinq skills, modules, `--retirer-absents`, conventions |
| `corpus/scripts/ask_corpus.py` | `--dossier` accepte un nom de module (`.claude/skills/*/modules/<nom>`) |
| `composer-hooks-funk-electro/scripts/install.sh`, `qwen-musique.py` | installent le skill `compositeur-arrangeur` entier ; le lanceur lit `GUIDE.md` |
| `electronic-production-engineer` | `ollama/run_skill.py`, `scripts/validate_skill.py`, `MANIFEST.json` (recalculé par `outils/regrouper_skills.py --manifest`), adaptateurs : `GUIDE.md` |
| `.gitignore` | `__pycache__/` |

Script : `outils/regrouper_skills.py` a déplacé 44 dossiers, supprimé 18 fichiers (copies jumelles, portable), déplacé le storyboard, converti 39 `SKILL.md` en `GUIDE.md` et réécrit environ 1 200 renvois (981 `../x/`, 115 `x/references/…`, 11 `.claude/skills/x`, 99 chemins vers la racine du dépôt). Rejoué (`--renvois`), il ne change plus rien. Il ne peut pas être relancé sur ce dépôt (les 44 anciens dossiers n'existent plus) ; il documente.

## 6. Sur le Mac, après la fusion

```bash
bash outils/installer.sh --retirer-absents            # simulation : cinq skills à copier, 44 anciens à écarter
bash outils/installer.sh --retirer-absents --appliquer
```

Relancer Claude Code et Qwen Code, puis trois demandes témoins pour contrôler le déclenchement, qui ne se teste pas en session cloud : « la basse du drop » (sound-designer-serum), « où on en est » (producteur-live › chef-de-projet), « c'est boueux » (ingenieur-mixage). Les commandes `/chef-de-projet`, `/maitriser-suno`… n'existent plus : `/producteur-live` suivi de la demande, ou une demande naturelle qui nomme le module. La mémoire de projet sur le Mac cite les anciens noms : rien à changer, ce sont les noms des modules.

## 7. Modules ajoutés depuis : pack v18 (8 oct. 2026)

Les 13 skills du pack v18 (branche `claude/new-session-x91wej`, 19 sept., jamais fusionnée) sont devenus des modules avec les mêmes conventions (`GUIDE.md`, renvois réécrits, tableau « Modules de ce skill », carte de `producteur-live`) :

| Skill | Modules du pack v18 |
|---|---|
| **producteur-live** | composer-producer-director, bass-house-ableton-bridge |
| **compositeur-arrangeur** | bass-house-composition, modern-pop-electronic-music-theory, modern-jazz-chillout-theory, afro-caribbean-latin-detroit-theory |
| **producteur-rythmique** | studio-grade-kick-low-end-sound-design, studio-grade-drums-electronic-percussion |
| **sound-designer-serum** | bass-house-serum2-sound-design, studio-grade-bass-sound-design, studio-grade-sample-vocal-break-design, studio-grade-transition-fx-director |
| **ingenieur-mixage** | bass-house-mixing-mastering |

Les dossiers de support du pack (`core/`, `data/`, `producer-intelligence/`, `history/`) sont dans le module `composer-producer-director`. Arbitrage, plug-ins absents et recouvrements : `docs/integration-pack-v18.md`.
