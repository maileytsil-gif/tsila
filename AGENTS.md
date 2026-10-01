# Projet musical VIBRA — règles communes aux agents

Ce fichier est lu par Claude Code (importé par `CLAUDE.md`), Qwen Code (`.qwen/settings.json` → `context.fileName`) et Codex. Il dit où entrer et ce qui ne se négocie pas ; le détail est dans les skills.

## Le dépôt

- `.claude/skills/` : les skills du workflow, **source unique**. `.qwen/skills` est un lien vers ce dossier : Claude Code et Qwen Code lisent les mêmes fichiers. Ne jamais créer une seconde copie à tenir à jour à la main.
- `lom-bridge/` : LOM Bridge 0.8.1 (Remote Script, `lom.py`, `agent_gateway.py`, tests hors Live). Sur le Mac : `$LOM_BRIDGE_DIR` (défaut `/Volumes/NO NAME/caude/lom-bridge`).
- `outils/installer.sh` : installe ou met à jour les skills dans `~/.claude/skills` et `~/.qwen/skills` (simulation par défaut). `outils/verifier_skills.py` : contrôle des skills, lancé aussi par l'intégration continue.

## Par où entrer

| Demande | Premier skill |
|---|---|
| Tout ce qui touche Live (Set, piste, clip, plug-in, niveau, sauvegarde) | `ableton-live-session` : discipline, puis carte « situation → skills » |
| Nouvelle démo ou nouveau morceau VIBRA (brief, référence, émotions, Original / Extended Mix) | `produire-demo-electro-rapide`, après l'ouverture de séance d'`ableton-live-session` et de `memoire-projet` ; `produire-morceau-electronique-de-a-a-z` prend le relais une fois la démo validée |
| Suno : prompt, génération à corriger, Studio, stems ou MIDI à reprendre dans Live | `maitriser-suno` ; voix seules sur un instru existant : `suno-vocals` |
| « Où on en est », plusieurs morceaux, reprise après une pause | `chef-de-projet` |
| Question de théorie sans écriture dans Live | `theorie-musicale-electronique` (électro) ou `theorie-musicale-composition` (tous styles, cours) |

## Règles de l'utilisateur pour chaque morceau

- **Référence** : au moins une, choisie **avec** l'utilisateur selon le style (titre, artiste, critères : groove, timbre, structure, mix, énergie). Proposer des candidats si elle manque, faire valider avant de fixer le brief. Ne jamais copier mélodie, paroles ni enregistrement ; pas d'audio de référence dans une sortie sans droits.
- **Émotions** : une ambiance générale et **une à quatre émotions au total**, dont une dominante, placées en mesures (`composer-trajectoire-emotionnelle`).
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
5. **Pas de nouvel effet natif de Live** dans les chaînes de mix (règle 6 d'`ableton-live-session`) ; instruments natifs tolérés ; traitements par plug-ins tiers.
6. **Mémoire** : ouvrir et fermer chaque séance par `memoire-projet` (`reprise.sh`, `journal.sh`) ; tenir le journal des fichiers créés et des vérifications. Claude et Qwen écrivent dans **la même** mémoire de projet (`MEM_DIR`, défaut `~/.claude/projects/-Volumes-NO-NAME-caude/memory`).
7. **Secrets** : le jeton de `connection.json` ne s'affiche ni ne se copie dans une réponse, un fichier ou un prompt.

## Modifier un skill

Dans ce dépôt, jamais dans une copie installée. Puis `python3 outils/verifier_skills.py` (en-têtes, chemins, copies jumelles, lien `.qwen`, carte), commit **seulement à la demande de l'utilisateur**, et `bash outils/installer.sh --appliquer` sur le Mac. Qwen Code et les autres agents proposent un diff sans l'appliquer. Un skill en double (skill autonome et corpus du skill A à Z) se corrige dans les deux fichiers : le vérificateur refuse deux jumeaux différents.
