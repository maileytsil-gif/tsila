@AGENTS.md

## Propre à Claude Code

- **Sur le Mac** (terminal lancé dans ce dépôt ou avec les skills installés dans `~/.claude/skills`) : Producer Pal (`ppal-*`) pour MIDI, clips, pistes et devices natifs ; `lom.py` pour l'état, les paramètres, le chargement sans hot-swap, les notes relues, l'automation d'arrangement ; contrôle d'écran pour les menus de Live (en français), les dialogues d'export et les fenêtres de plug-ins. Détail et pièges : `ableton-live-session`.
- **En session cloud** (claude.ai/code) : ni Live, ni Mac, ni YouTube. Travail possible : skills, bridge hors Live (`lom-bridge/tests`), grilles (`composer-hooks-funk-electro/scripts/grille.py`), théorie (`theorie-musicale-electronique/scripts/theorie.py`), contrôles (`python3 outils/verifier_skills.py`).
- Un skill s'appelle par `/nom-du-skill` ou par une demande naturelle ; la carte d'`ableton-live-session` dit lequel enchaîner.
- Qwen Code travaille sur les mêmes skills et la même mémoire de projet (`QWEN.md`) : ce que l'un note, l'autre le reprend.
