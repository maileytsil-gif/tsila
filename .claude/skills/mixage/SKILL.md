---
name: mixage
description: Procédure de mixage dans le Set Ableton Live, appelée par le rôle ingenieur-mixage — carte du mix (mix_snapshot.py), gain staging, grave d'abord (sub/kick/sidechain), balance statique sur la section la plus dense, EQ correctif puis dynamique/spectral, glue et parallèle par bus, profondeur par envois, largeur, bus masters en série, limiteur d'export, comparaison à une référence, cibles indicatives ; inventaire des outils par tâche (outils.md) et diagnostics symptôme → mesure → remède (diagnostics.md). Utilise ce skill quand ingenieur-mixage a posé le diagnostic et qu'il faut exécuter la passe de mix étape par étape dans Live, ou quand l'utilisateur demande explicitement « la procédure de mix », « l'ordre des étapes du mix », « quel outil pour quoi ».
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Mixage : méthode, outils, mesures

## Ordre de travail (une étape validée par échange)
1. **Carte du mix** : `scripts/mix_snapshot.py` (via `pyl.sh`) — par piste : fader, pan, envois, devices, sortie ; état des bus. Relire avant chaque étape : l'utilisateur bouge les faders lui-même.
2. **Grave d'abord** : sub sinus mono (≤ 110 Hz), kick rond et court ; les deux se partagent 40–120 Hz par sidechain (compresseur sur SUB/BASS, source piste KICK Post FX, attaque 0,1–1 ms, release ≈ 110 ms, 4:1) plutôt que par EQ. Grave centré (Mono Maker/Utility < 120 Hz sur le bus BASSES).
3. **Balance statique** sur le passage le plus dense (souvent le dernier drop) : crêtes avant fader relevées avec `levels.sh` (pré-fader ! le master est pré-devices), faders posés, puis vérification par bus.
4. **EQ correctif à la source** (pistes AUDIO, REQ 6) : coupe-bas partout sauf kick/sub, un creux de désencombrement (250–900 Hz) là où deux éléments se chevauchent, shelf doux sur les aigus agressifs. Résonances → dynamique/spectral (soothe3, Pro-Q 4 spectral, F6) avant la compression.
5. **Bus** : glue légère (bx_glue 2–4:1, attaque lente, release auto, 1–2 dB), compression parallèle pour la densité (API-2500, mix 30–60 %), une seule couleur (J37) au master 1, largeur seulement au-dessus de 120 Hz (Imager, largeur des textures automatisée).
6. **Profondeur** : envois (réverb courte A, delay B, grande salle sombre C) automatisés par section, envois post-fader pour que les queues suivent les fondus ; les envois automatisés restent sur les pistes MIDI.
7. **Masters en série** : 1 cohésion/couleur (Pro-Q 4 → bx_glue → J37), 2 dynamique/espace (API-2500 // → Imager), 3 mesure/sortie (TBC → SPAN → L2), Main = Insight. REF → Main, hors limiteur.
8. **Référence** : Audiolens → cible dans TBC 3 ; SPAN moyennage 4 s, bloc 8192 ; comparer sur des sections équivalentes à niveau égalisé.
9. **Cibles (indicatives, à confirmer avec l'utilisateur)** : crêtes avant limiteur ≈ −4 à −6 dBFS ; limiteur L2 plafond −1,0 dBFS (son plafond est un sample peak : −0,4 ne garantit pas le true peak) ou L4 en mode True Peak ; sortie ≤ −1 dBTP lue dans Insight 2 ; LUFS intégré ≈ −14 streaming, −9 à −7 club, lus dans Insight 2 ou WLM Plus (aucun outil local ne mesure LUFS/TP). L'export analysé (`analyze_wav.py`) tranche la crête sample, la durée, l'écrêtage et le RMS.

## Diagnostics sans oreilles (`references/diagnostics.md`)
Boueux → 200–400 Hz cumulés (pad, accords, cordes, piano) ; agressif → 3–8 kHz (hats, pluck, saturation) ; mince → coupe-bas trop hauts ou grave non centré ; pompage → sidechain trop long/release, ou glue à attaque rapide ; refrain qui « ne passe pas » → frottement de demi-ton entre voix, pas un problème de mix.

## Outils : lequel pour quoi
`references/outils.md` — inventaire de l'utilisateur classé par tâche (correctif, dynamique/spectral, glue, parallèle, couleur, largeur, mesure, limiteur), avec le mode de pilotage (API ou fenêtre) et le lien vers la fiche (`effets-plugins`). Règle en vigueur : **pas d'effets natifs** dans les chaînes de mix.
