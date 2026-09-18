---
name: live-automation
description: Écrire, corriger et vérifier une automation d'arrangement dans Ableton Live via le LOM Bridge — mouvement de filtre, sweep de coupe-bas, fondu, envoi de reverb/delay, flanger, largeur stéréo, sur une piste MIDI comme sur un bus sans clip. Utilise ce skill dès que l'utilisateur parle d'automation, de mouvement, de montée/descente de filtre, de « part de X Hz », de fondu, de résonance d'un sweep, ou veut qu'un paramètre évolue entre deux mesures.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Automation d'arrangement par le bridge

Chemin : `/Volumes/NO NAME/caude/lom-bridge/lom.py` (`apply spec.json`, `read`). Règles complètes du format : `../ableton-live-session/references/bridge.md`.

## Procédure
1. **Transport arrêté ?** `int(song.is_playing)` doit valoir 0 ; sinon demander (l'utilisateur écoute souvent).
2. **Support** : la cible doit être couverte par un clip sur toute la fenêtre. Piste MIDI : ses clips. Bus/piste audio sans clip : `scripts/make_silence.py` génère un WAV silencieux dans `Samples/Imported/` (12 mesures à 120 BPM = 24 s) ; le poser avec `ppal-create-clip` (`sampleFile`, `warping: true`) puis `arrangementLength` à la durée voulue. Nommer « support automation (silence) A-B ». Ne jamais les supprimer : l'automation vit dessus.
3. **Device** : s'assurer qu'il est bien sur la piste (charger avec la règle anti-hot-swap), poser les valeurs statiques (ex. mix 0 %, filtre On à 20 Hz) AVANT d'écrire — le bridge ancre l'ancienne valeur aux bords de la fenêtre.
4. **Unités** : `disp` pour dB/% ; `raw` pour les fréquences de REQ 6 (affichage en Hz entiers → résolution impossible). Obtenir le raw : balayer 2001 valeurs et garder l'affichage le plus proche (`helpers.disp_num`). Fréquence : `curve: lin` en raw = montée régulière en octaves.
5. `apply --dry`, puis `apply`, attendre `jobs` vide, puis **`read` un point par mesure** (`res 0.25`) et montrer le tableau à l'utilisateur. Ignorer un « ERR » si la relecture est bonne ; ne jamais croire un « OK » sans relire.
6. Sauver (Fichier › Sauver Set Live) et noter dans la mémoire du projet.

## Recettes validées
- Sweep coupe-bas montant sur un break : REQ 6 `Band1 Frq` 100→900 Hz (harmonie), 60→500 (batterie), retour 20 Hz au downbeat suivant (deux points au même instant = saut). Résonance = `Band1 Q` statique (harmonie 4,5, batterie 2,5, basses 2,0).
- Sweep descendant sur un refrain : 1400→100 Hz sur tous les bus, retour 20 Hz.
- Flanger de transition : MetaFlanger `Mix` 0→100 % `exp` sur 4 ou 8 mesures, 0 pile au downbeat suivant.
- Fondus de volume : `mixer` / `Volume` en `disp` (dB).
- Envois : `mixer` / `Send A` (throw de delay : −14 → −7 sur 2 mesures puis retour).
