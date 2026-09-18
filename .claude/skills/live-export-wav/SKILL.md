---
name: live-export-wav
description: Exporter le Set Ableton Live en WAV (Fichier › Exporter Audio/Vidéo, en français) par contrôle d'écran, avec durée exacte, 24 bits, sans normalisation, puis vérifier le fichier (durée, crête, écrêtage, queue de fin). Utilise ce skill dès que l'utilisateur demande un export, un bounce, un rendu, un WAV/MP3, « sors-moi le morceau », ou veut vérifier le niveau réel du master.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Export WAV depuis Live

## Avant
1. Boucle/sélection d'export = étendue exacte : `ppal-playback update-arrangement` avec `loopStart 1|1`, `loopEnd <dernière mesure + 1>|1` (le dialogue reprend Début/Longueur de la boucle). Ex. 128 mesures → `129|1`.
2. Muter la piste **REF** (référence) si elle existe ; s'assurer que rien ne joue (`int(song.is_playing)`).
3. Sauver le Set (Fichier › Sauver Set Live).

## Dialogue (contrôle d'écran)
- `app_menu` Fichier › « Exporter Audio/Vidéo... » (item parfois sans titre dans la liste, le chemin marche).
- La fenêtre « Exporter Audio/Vidéo » apparaît dans `app_list_windows` (≈371×781). Vérifier sur capture : Piste convertie **Main**, Début **1.1.1**, Longueur **N.0.0**, Normaliser **Off**, Fréquence = projet (44100), Encoder en PCM **On**, WAV, **Résolution 24** (menu déroulant : refusé en arrière-plan → passer en contrôle plein écran, cliquer, choisir 24), MP3 **Off**.
- « Exporter » → feuille de sauvegarde : ⌘⇧G, taper le dossier (`/Users/r.tsila/Desktop/1 Project`), Entrée, nom, « Save ». Attendre : le fichier cesse de grossir.

## Après — `scripts/analyze_wav.py <fichier.wav> [durée attendue s]`
Convertit en PCM 32 bits entier temporaire (afconvert ; crêtes exactes du 24 bits), puis imprime : durée exacte, crête max dBFS, RMS global et facteur de crête, nombre d'échantillons ≥ −0,1 dBFS (écrêtage), sauts d'échantillon brutaux (clics probables), crête par section (à passer en argument si besoin), niveau des 20 dernières ms (queues éteintes ?). Il ne mesure ni LUFS ni true peak (Insight 2 / WLM Plus). Rapporter ces chiffres à l'utilisateur tels quels ; sans accès audio, dire qu'on n'a pas écouté.
