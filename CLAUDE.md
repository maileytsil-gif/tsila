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
lui-même : `lom-bridge/`, scripts, revues, documentation.

Cette règle s'applique à **chaque nouveau morceau**, pas seulement à celui en
cours au moment de son écriture (le morceau "funk is not dead").
