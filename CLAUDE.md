# Règle d'environnement : travail Ableton = session locale uniquement

Ce dépôt (`maileytsil-gif/tsila`) contient le code du LOM Bridge et les skills
de production musicale, mais **pas** de Set Ableton Live, pas de mémoire de
morceau (`memory/projet-*.md`), et aucun accès à Producer Pal, au LOM Bridge
en direct, ou au contrôle d'écran. Ces outils n'existent que dans la session
Claude Code **locale** sur le Mac de l'utilisateur, là où Ableton Live est
réellement ouvert.

**Dès qu'une session cloud (Claude Code on the web) reçoit une demande liée à
Ableton, un Set Live, un morceau, une piste, un clip, un device, un plug-in,
un bus, un mix ou une sauvegarde** : ne pas tenter d'agir dans Live depuis
ici. Rediriger l'utilisateur vers sa session Claude Code locale (sur le Mac,
dans le dossier du projet, ex. `/Volumes/NO NAME/caude`), où le skill
`ableton-live-session` et la mémoire persistante (`memoire-projet`) prennent
le relais.

Cette session cloud reste utile pour tout ce qui touche au code du dépôt
lui-même : `lom-bridge/`, scripts, revues, documentation. Elle sait aussi
analyser des fichiers audio fournis (mesures, spectrogrammes) et écrire la
mémoire projet.

Cette règle s'applique à **chaque nouveau morceau**, pas seulement à celui en
cours au moment de son écriture (le morceau "funk is not dead").

## Ouvrir une session qui peut piloter Live

**Claude Code web** (claude.ai/code) = conteneur cloud : ni Ableton, ni écran,
ni route réseau vers le Mac. **Claude Code dans le Terminal du Mac** = accès
complet. C'est le seul choix qui compte — tout le reste est déjà en place.

Sur le Mac :

```sh
cd "/Volumes/NO NAME/caude"
claude
```

Puis reprendre par « on reprend \<nom du morceau\> ».

### Déjà configuré, à ne pas refaire

| Élément | Où il est déclaré |
|---|---|
| Producer Pal (`ppal-*`) | config utilisateur → présent dans **toutes** les sessions locales |
| LOM Bridge | `.claude/skills/ableton-live-session/scripts/pyl.sh` |
| Les 26 skills musique | `.claude/skills/` (dans ce dépôt) |
| Les permissions | `.claude/settings.local.json` |

### Pourquoi aucun réglage GitHub ne peut y changer quoi que ce soit

Producer Pal joint Ableton par **localhost**, le bridge est un **script local**,
et le contrôle d'écran a besoin d'**un écran**. Un conteneur cloud n'a aucun des
trois. Ce n'est pas une permission manquante — c'est une autre machine.
