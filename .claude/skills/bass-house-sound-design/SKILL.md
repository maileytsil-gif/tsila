---
name: bass-house-sound-design
description: Bibliothèque Bass House hors basses — stabs Serum 2 (organ, vowel « wah », métallique, disco, rave sync), pads, leads, impacts, prototypes Wavetable natif et effets spectraux imprimés. Utiliser quand l'utilisateur demande un stab, un accord house, un pad, un lead, un impact ou une texture spectrale en Bass House, ou le même patch dans Wavetable. Basses (sub, Reese, wub, growl) → serum-2-basses-house-future-house.
---

# Sound design Bass House

Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

1. Déduire ou demander BPM, tonalité, référence, rôle et section. Sans Set : 128 BPM Bass House, 126 BPM Future House (tempos documentés dans `../sound-designer-serum/references/patches-genres.md`), en le disant ; jamais une règle.
2. Sélectionner une technique dans [recettes.md](references/recettes.md). Donner les étapes et réglages de départ ajustables; distinguer amplitude, filtre, hauteur et modulation rythmique.
3. Écrire un motif MIDI concret de 1 à 4 mesures et préciser sa relation au kick, clap et basse. Faire comparer A/B par l'utilisateur dans le morceau, à niveau égal : Claude n'entend pas ; il relit les réglages (capture) et mesure les niveaux relatifs (`lom.py meters`). Chaque « écouter » des références est une consigne pour l'utilisateur. Notes en numérotation Ableton C3 = 60, vérifiées avec `../composer-hooks-funk-electro/scripts/grille.py`.
4. Construire dans cet ordre: source, enveloppe, modulation/filtre, saturation, espace sur retour, resampling éventuel. Pour les synthés rythmiques, commencer par les notes.
5. Vérifier durée, attaques, niveau, conflits kick/sub, phase, mono et largeur. Doser le sidechain selon le kick réel; supprimer les couches qui masquent le groove. Ne pas imposer de bandes fréquentielles fixes ou de chaîne universelle.
6. Pour livrer un son avec un morceau: sauvegarder preset et MIDI, imprimer une version audio et une version sans effets de bus, noter BPM/tonalité et vérifier les droits des samples.

Lire [recettes.md](references/recettes.md) pour les familles sonores. Pour des stabs Serum 2 sans Basic Shapes, lire [stabs-serum2.md](references/stabs-serum2.md) : préserver le choix de table et la relation entre enveloppes, MIDI et mix. Pour un patch Ableton Wavetable, lire [wavetable.md](references/wavetable.md). Pour les effets spectraux, lire [spectral-live.md](references/spectral-live.md) et distinguer instrument, effet et analyseur. Lire [sources-et-videos.md](references/sources-et-videos.md) pour les sources. Ne pas prétendre avoir visionné les vidéos si seul leur descriptif a été consulté.

## Dans ce workflow

- Méthode, choix du moteur et tableau section / paramètre / valeur / comment réglé / vérifié : `../sound-designer-serum/SKILL.md` ; doc Serum 2 : `../sound-designer-serum/references/moteurs-synthese.md` et `serum2-fx-clip-arp.md` ; Wavetable : `../sound-designer-serum/references/ableton-instruments.md`. Leads, hooks, stabs d'accords et pads faits dans Serum, d'après 90 tutoriels (house d'abord) : `../sound-designer-serum/references/synths-serum-synthese.md`.
- Basses : `../serum-2-basses-house-future-house/SKILL.md`. Chargement sans hot-swap et clics dans Serum 2 : `../vst-sound-design/SKILL.md`.
- Notes et motif : `../compositeur-arrangeur/SKILL.md`, grille vérifiée par `../composer-hooks-funk-electro/scripts/grille.py`.
- Kick/sub : `../kick-bass-equilibre/SKILL.md` ; impression audio : `../resampling/SKILL.md` ; effets tiers : `../effets-plugins/SKILL.md` ; mémoire : `../memoire-projet/SKILL.md`.
- `references/` est la jumelle de `../produire-morceau-electronique-de-a-a-z/references/bass-house-*.md` (et de la version portable `Bass_House_skill_portable_ChatGPT_Claude_Qwen.md`) : corriger les copies ensemble, `python3 outils/verifier_skills.py` refuse deux jumelles différentes.
