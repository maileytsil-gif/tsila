---
name: vst-sound-design
description: Pilotage des synthés de l'utilisateur dans Ableton Live — charger sans écraser (règle anti hot-swap), régler, relire ou capturer, mesurer le niveau, caler le sidechain : Serum 2 (fenêtre pilotée par clics, presets factory et banques perso, coordonnées dans serum2.md), Wavetable, Operator, Drift, Simpler/Drum Rack (paramètres exposés à l'API, fiches instruments-natifs.md), recettes par rôle (recettes.md). Utilise ce skill pour exécuter une opération sur un instrument (charger un preset, passer un instrument sur Serum, régler un paramètre, remplacer un son, mesurer avant/après) ; le choix du moteur et la conception du timbre relèvent du rôle sound-designer-serum, qui appelle ce skill.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Sound design sur les synthés de l'utilisateur

## Qui se pilote comment
- **Natifs (Wavetable, Operator, Drift, Simpler, Drum Rack)** : tout par `ppal-update-device` (valeurs affichées : « 3000 Hz », « -12 dB », noms d'enum) et pseudo-paramètres (`osc1Wavetable`, `monoPoly`, `sidechainSourceTrackId`…) ; lire avec `ppal-read-device include params/options`. Relire après chaque écriture.
- **Serum 2** : rien d'exposé (sauf ce que l'utilisateur mappe en mode Configure). Chargement par le navigateur (`app.browser.plugins › VST3 › Serum 2`) avec la règle anti-hot-swap — sauf quand on VEUT remplacer l'instrument de la piste : sélectionner l'ancien instrument puis charger = remplacement en place, chaîne d'effets conservée. Réglages dans la fenêtre : voir `references/serum2.md`.
- Fiches des instruments natifs (paramètres exposés relevés) : `references/instruments-natifs.md`.
- Autres VST : vérifier `len(d.parameters)` après chargement (1 = fenêtre seulement). Exposés connus : J37, API-2500, bx_glue, REQ 6, MetaFlanger, L2.

## Procédure
1. Lire la piste (instrument, chaîne, clips, registre MIDI joué) et ce que le son doit faire dans l'arrangement (rôle, registre libre, sidechain).
2. Charger / choisir le preset (recettes dans `references/recettes.md`), garder la chaîne d'effets existante.
3. Régler : natif → paramètres relus ; Serum → clics de fond (`app_click`/`app_batch` sur la fenêtre, coordonnées de `references/serum2.md`), capture après chaque geste ; ce qui ne passe pas en arrière-plan (glisser de bouton, saisie), le dire et proposer à l'utilisateur de le faire ou passer en contrôle plein écran.
4. Mesurer : `levels.sh` (skill `ableton-live-session`) pour comparer au niveau de l'ancien son (crête avant fader) ; compenser sur un Utility ou le volume de l'instrument, pas sur un fader automatisé.
5. Vérifier la hauteur : un preset de kick/one-shot suit souvent la note MIDI (C1 par défaut) — transposer les clips ou le preset si la tonalité compte.
6. Sauver, noter le preset et les valeurs dans la mémoire du projet.

## Garde-fous
- Ne jamais empiler deux instruments sur une piste par erreur : relire `[d.name for d in t.devices]`.
- Sidechains, EQ et automations vivent sur la piste : remplacer l'instrument ne les touche pas, mais un preset plus fort/plus faible change tout le mix → mesurer.
- Sub : sinus mono, release ≥ 60 ms, pas de tierce, passe-bas ≈ 110 Hz derrière.
