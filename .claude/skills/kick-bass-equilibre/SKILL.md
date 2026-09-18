---
name: kick-bass-equilibre
description: Régler la relation kick / sub / basse dans Ableton Live — décider qui tient le sub (fondamental) et qui tient l'attaque, accorder le kick à la tonalité, aligner phase et polarité, partager le grave par bande et par sidechain, garder le grave mono — avec des mesures (corrélation dans la bande 30–120 Hz, annulation, énergie sous/au-dessus de 60 Hz) sur des exports séparés du kick et du sub. Utilise ce skill dès que l'utilisateur parle de kick et basse ensemble, de sub, de « ça se bagarre dans le grave », de pompage, de phase, de polarité, d'accord du kick, de « qui tient le grave », ou veut choisir un rôle sub/attaque.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Kick, sub et basse : qui tient quoi

## 1. Choisir les rôles (`references/roles.md`)
Deux configurations cohérentes, pas un mélange :
- **Le sub tient le fondamental** (deep/minimal house, tech house, DnB) : sub sinus mono à la tonique, kick court dont le corps est **au-dessus** (60–100 Hz), coupe-bas du kick 25–30 Hz par défaut (signature validée : 28 Hz), monté à 40–50 Hz seulement si `kick_bass_check.py` montre plus de 20 % de l'énergie du kick sous 60 Hz ; sidechain du sub par le kick court (0,1–1 ms, 80–120 ms de départ, valeur validée du projet à noter : el21 = 60 ms) pour libérer l'attaque.
- **Le kick tient le grave** (électro 808, techno rumble, trap) : kick/808 long accordé à la tonique (ou quinte), basse au-dessus de 80–100 Hz ou jouée dans les silences, coupe-bas de la basse 60–80 Hz, sidechain profond et lent.
Le choix dépend du genre, de la longueur du kick et de la note du sub ; il se prend **avant** de mixer et se note dans la signature (skill `drums-signature`).

## 2. Accord, longueur, timing
- Accorder le kick : fondamental à la tonique ou à la quinte (F1 = 43,7 Hz → kick à 87 ou 65 Hz) ; un kick désaccordé bat contre le sub. Kick synthé : macro Pitch / transposition de note ; sample : Simpler transpose (vérifier avec `analyze_synth.py --mono-note`).
- Longueur : décroissance du kick plus courte que l'espace entre kick et note de basse suivante ; sub avec release ≥ 60 ms (pas de clic) mais < intervalle des notes.
- Timing : décaler la note de sub de −5 à −10 ms (ou le kick) quand la somme s'annule ; polarité inversée sur l'un des deux si la corrélation est négative (Utility « Phase Invert » natif, ou dans le synthé).

## 3. Mesurer (`references/mesure.md`, `scripts/kick_bass_check.py`)
1. Exporter séparément KICK et SUB (ou BASS) sur une boucle de drop (skill `live-export-wav`, « Piste convertie » = la piste, même plage) — sans traitement de bus.
2. `kick_bass_check.py kick.wav sub.wav --band 30-120` : niveaux et pics de chaque, énergie sous/au-dessus de 60 Hz (rôles réels), **corrélation dans la bande**, gain de la somme vs somme attendue (annulation ou renforcement), meilleur décalage ±15 ms et effet d'une inversion de polarité, ratio pic/RMS (masquage de l'attaque).
3. Décider : rôle confirmé ou inversé, polarité, décalage, accord, profondeur du sidechain ; appliquer ; réexporter ; remesurer. Un seul changement par cycle.

## 4. Sidechain et bus
Compresseur sur SUB/BASS, source = piste kick (MIDI : Post FX ; piste AUDIO bouncée : Pre FX, convention d'el21), ratio 4:1, attaque 0,1–1 ms, release 80–120 ms de départ (une double-croche = 60000 / BPM / 4 ms : 125 ms à 120, 119 ms à 126) puis la valeur validée du projet, seuil pour 4–8 dB sur le sub tenu ; bus BASSES : Mono Maker < 120 Hz, glue lente (skills `mixage`, `effets-plugins`). Pompage audible → release plus courte ou sidechain filtré (le kick au-dessus de 60 Hz seulement).
