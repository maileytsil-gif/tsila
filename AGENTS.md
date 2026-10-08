# Projet musical VIBRA — règles communes aux agents

Ce fichier est lu par Claude Code (importé par `CLAUDE.md`), Qwen Code (`.qwen/settings.json` → `context.fileName`) et Codex. Il dit où entrer et ce qui ne se négocie pas ; le détail est dans les skills.

## Le dépôt

- `.claude/skills/` : les **cinq skills** du workflow, **source unique** — `producteur-live` (séance, mémoire, projet, morceau entier, Suno ; porte d'entrée et carte), `compositeur-arrangeur`, `producteur-rythmique`, `sound-designer-serum`, `ingenieur-mixage`. Chacun contient ses **modules** (`<skill>/modules/<module>/GUIDE.md`) : les 44 anciens skills, déplacés entiers le 8 oct. 2026 (correspondance et conventions : `docs/regroupement-skills.md`). `.qwen/skills` est un lien vers ce dossier : Claude Code et Qwen Code lisent les mêmes fichiers. Ne jamais créer une seconde copie à tenir à jour à la main.
- `lom-bridge/` : LOM Bridge 0.8.1 (Remote Script, `lom.py`, `agent_gateway.py`, tests hors Live). Sur le Mac : `$LOM_BRIDGE_DIR` (défaut `/Volumes/NO NAME/caude/lom-bridge`).
- `outils/installer.sh` : installe ou met à jour les skills dans `~/.claude/skills` et `~/.qwen/skills` (simulation par défaut ; `--retirer-absents` écarte les anciens skills installés). `outils/verifier_skills.py` : contrôle des skills et de leurs modules, lancé aussi par l'intégration continue.

## Par où entrer

| Demande | Premier skill › module |
|---|---|
| Tout ce qui touche Live (Set, piste, clip, plug-in, niveau, sauvegarde) | `producteur-live` : discipline de séance, puis carte « situation → skill › module » |
| Nouvelle démo ou nouveau morceau VIBRA (brief, référence, émotions, Original / Extended Mix) | `producteur-live` › `produire-demo-electro-rapide`, après l'ouverture de séance (discipline de `producteur-live`, module `memoire-projet`) ; le module `produire-morceau-electronique-de-a-a-z` prend le relais une fois la démo validée |
| Suno : prompt, génération à corriger, Studio, stems ou MIDI à reprendre dans Live | `producteur-live` › `maitriser-suno` ; voix seules sur un instru existant : module `suno-vocals` |
| « Où on en est », plusieurs morceaux, reprise après une pause | `producteur-live` › `chef-de-projet` |
| Notes, mélodie, hook, accords, arrangement, émotion, question de théorie | `compositeur-arrangeur` ; théorie seule : ses modules `theorie-musicale-electronique` (électro) ou `theorie-musicale-composition` (tous styles, cours) |
| Batterie, groove, kick et basse, grave, Maschine | `producteur-rythmique` |
| Un son, un preset, Serum 2, une basse, des cuivres, un Rhodes, une capture audio | `sound-designer-serum` |
| Mix, master, export, « c'est boueux », LUFS | `ingenieur-mixage` |

## Règles de l'utilisateur pour chaque morceau

- **Référence** : au moins une, choisie **avec** l'utilisateur selon le style (titre, artiste, critères : groove, timbre, structure, mix, énergie). Proposer des candidats si elle manque, faire valider avant de fixer le brief. Ne jamais copier mélodie, paroles ni enregistrement ; pas d'audio de référence dans une sortie sans droits.
- **Émotions** : une ambiance générale et **une à quatre émotions au total**, dont une dominante, placées en mesures (module `composer-trajectoire-emotionnelle` de `compositeur-arrangeur`).
- **Grave** : sub et basse médium dans **deux instruments** séparés (sub mono).
- **Signature sous 124 BPM** (strictement) : kick Serum 2 doux, clair et chaleureux, dont « Solomun feat. Jamie Foxx – Ocean » n'est que la **référence du kick** ; hats fins, clap net et discret, adaptés au morceau et à sa propre référence. Tester en contexte, adapter si elle contrarie le groove voulu.
- **Drops** : variation audible de batterie ou de transition avant chaque frontière de huit mesures (fill, retrait de kick, roulement, reverse, impact, silence), en alternant les gestes.
- **Deux versions** : Original Mix et Extended Mix, issues du même noyau, vérifiées et exportées séparément.
- **Maschine** : dans cette installation, une sortie externe directe de Maschine **contourne** le Perform FX du Master. Choisir par élément : passer par le Master et imprimer la prise, ou sortie séparée sans cet effet ; tester dans la session réelle.
- **Labels** : VIBRAAXIS (productions personnelles), VIBRAVECTOR (DnB / Jungle), VIBRAMOTIVE (label principal), quand l'utilisateur le précise.

## Règles du workflow (toujours)

1. **Une étape par échange** : annoncer le plan complet, exécuter ou faire valider une seule étape ; l'utilisateur corrige dans Live entre deux, donc relire l'état réel avant d'agir.
2. **Avant toute écriture dans Live** : Set sauvé sous un nouveau nom, état relu — `lom.py ping` puis `lom.py state --json` (Claude), `agent_gateway.py inspect /ping` puis `/state` (autres agents) —, transport vérifié. Après : relire. Les capacités du bridge, de Producer Pal et des plug-ins se **découvrent** dans la session, jamais supposées.
3. **C3 = 60** (numérotation Ableton) ; le numéro MIDI fait foi.
4. **Jamais « entendu »** : un agent n'écoute ni le Set, ni un rendu, ni une vidéo. Distinguer réglé et relu, mesuré (export, niveaux relatifs), proposé. Les tests d'écoute reviennent à l'utilisateur. Ne jamais inventer une écoute, un rendu, un preset, un stem, un Set ou une approbation.
5. **Pas de nouvel effet natif de Live** dans les chaînes de mix (règle 6 de `producteur-live`) ; instruments natifs tolérés ; traitements par plug-ins tiers.
6. **Mémoire** : ouvrir et fermer chaque séance par le module `memoire-projet` de `producteur-live` (`reprise.sh`, `journal.sh`) ; tenir le journal des fichiers créés et des vérifications. Claude et Qwen écrivent dans **la même** mémoire de projet (`MEM_DIR`, défaut `~/.claude/projects/-Volumes-NO-NAME-caude/memory`).
7. **Secrets** : le jeton de `connection.json` ne s'affiche ni ne se copie dans une réponse, un fichier ou un prompt.

## Modifier un skill ou un module

Dans ce dépôt, jamais dans une copie installée. Puis `python3 outils/verifier_skills.py` (en-têtes, modules, chemins, lien `.qwen`, carte), commit **seulement à la demande de l'utilisateur**, et `bash outils/installer.sh --appliquer` sur le Mac. Qwen Code et les autres agents proposent un diff sans l'appliquer. Un module est `<skill>/modules/<module>/GUIDE.md` (titre H1, jamais de `SKILL.md` sous `modules/`) ; un nouveau module se cite dans le tableau « Modules de ce skill » du `SKILL.md` de son skill et dans la carte de `producteur-live` ; les renvois se lisent depuis la racine du module (`../<module>/…`, `../../../<skill>/modules/<module>/…`, `../../` vers le skill parent).
