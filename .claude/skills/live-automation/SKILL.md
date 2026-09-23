---
name: live-automation
description: Écrire, corriger et vérifier une automation d'arrangement dans Ableton Live via le LOM Bridge — mouvement de filtre, sweep de coupe-bas, fondu, envoi de reverb/delay, flanger, largeur stéréo, sur une piste MIDI comme sur un bus sans clip. Utilise ce skill dès que l'utilisateur parle d'automation, de mouvement, de montée/descente de filtre, de « part de X Hz », de fondu, de résonance d'un sweep, ou veut qu'un paramètre évolue entre deux mesures.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Automation d'arrangement par le bridge

Chemin : `/Volumes/NO NAME/caude/lom-bridge/lom.py` (`apply spec.json`, `read`). Règles complètes du format : `../ableton-live-session/references/bridge.md`.

## Procédure
1. **Transport arrêté ?** `lom.py transport` → premier chiffre 0 ; sinon demander (l'utilisateur écoute souvent). `lom.py ping` une fois par séance (version chargée = disque).
2. **Support** : la cible doit être couverte par un clip sur toute la fenêtre (un trou n'est pas refusé mais **rien n'y est écrit** : avertissement « n temps non couverts »). Piste MIDI : ses clips (`lom.py clips "<piste>"`). Bus/piste audio sans clip : `scripts/make_silence.py` génère un WAV silencieux dans `Samples/Imported/` (12 mesures à 120 BPM = 24 s) ; le poser avec `ppal-create-clip` (`sampleFile`, `warping: true`) puis `arrangementLength` à la durée voulue. Nommer « support automation (silence) A-B ». Ne jamais les supprimer : l'automation vit dessus.
3. **Device** : s'assurer qu'il est bien sur la piste (`lom.py load "<piste>" "<nom>"`, anti hot-swap vérifié), poser les valeurs statiques (ex. mix 0 %, filtre On à 20 Hz) avec `lom.py setparam` AVANT d'écrire — le bridge ancre l'ancienne valeur aux bords de la fenêtre. Si `setparam` répond `E_AUTOMATED`, le paramètre est déjà automatisé : écrire la valeur statique par `apply` (deux points égaux) plutôt que de surcharger.
4. **Unités** : `disp` pour dB/% ; `raw` pour les fréquences de REQ 6 (affichage en Hz entiers → résolution impossible). Obtenir le raw : `lom.py solve <paramRef> <valeur>` ou balayer 2001 valeurs (`helpers.disp_num`). Fréquence : `curve: lin` en raw = montée régulière en octaves. Accords : `fades` sur un clip audio, `expressions` sur un clip MIDI — `lom.py policy accept=expressions` une fois pour toutes si le Set n'a pas de MPE ; `warp` si le plan le demande.
5. `apply --dry` (le plan dit clips, valeurs résolues, durée de lecture et de relecture), puis `apply` : écriture **tout ou rien** puis **relecture** (`relecture: exact|sampled, n points, écart max …`). `E_ROLLED_BACK` = rien n'est modifié, replanifier ; `relecture: interrupted` = écrit mais non contrôlé. Après un timeout client : `lom.py wait`. Puis **`read` un point par mesure** (`res 0.25`) et montrer le tableau à l'utilisateur — la relecture du bridge contrôle les points écrits, le tableau montre la courbe telle qu'elle joue. `E_AUTOMATION_OVERRIDDEN` = un paramètre automatisé a été bougé à la main : `lom.py py "song.re_enable_automation()"` puis relancer.
6. Sauver (Fichier › Sauver Set Live), `lom.py journal 5` et noter dans la mémoire du projet (spec JSON conservée : c'est la version réappliquable).

## Recettes validées
- Sweep coupe-bas montant sur un break : REQ 6 `Band1 Frq` 100→900 Hz (harmonie), 60→500 (batterie), retour 20 Hz au downbeat suivant (deux points au même instant = saut). Résonance = `Band1 Q` statique (harmonie 4,5, batterie 2,5, basses 2,0).
- Sweep descendant sur un refrain : 1400→100 Hz sur tous les bus, retour 20 Hz.
- Flanger de transition : MetaFlanger `Mix` 0→100 % `exp` sur 4 ou 8 mesures, 0 pile au downbeat suivant.
- Fondus de volume : `mixer` / `Volume` en `disp` (dB).
- Envois : `mixer` / `Send A` (throw de delay : −14 → −7 sur 2 mesures puis retour).
