# Projet : test du skill house — basse future house (Serum 2, piste 5)

**REPRISE (24 sept. 2026, Set non sauvegardé par Claude)** : nouveau Set Ableton ouvert par l'utilisateur, Serum 2 sur la piste 5. Trois recettes de basse future house proposées (skill `house-future-rave-bass-house-production`), aucune encore construite ni écoutée. Rien n'a été écrit dans Live : la session de travail tournait dans le cloud, sans accès au Mac.
En attente : le choix de l'utilisateur entre les recettes 1, 2 et 3 ; le nom du Set.
Prochaines étapes proposées : 1) sur le Mac, `cd ~/tsila && git pull`, puis lancer Claude Code dans `~/tsila` (Producer Pal, `lom.py` et contrôle d'écran y sont disponibles) ; 2) Sauver sous, tempo 126, la mineur, repères ; 3) construire la recette choisie sur la piste 5 avec le clip de test ci-dessous, puis les 5 vérifications ; 4) sauver le preset sous un nouveau nom ; 5) kick 909 + sidechain, puis les deux autres recettes pour comparer.

## Consignes permanentes
- Une étape par échange ; Set sauvé avant et après chaque étape ; règle anti hot-swap (ne jamais remplacer Serum sur la piste 5 sans le dire).
- Aucun réglage n'est « le son de » Tchami, Oliver Heldens ou un autre : références d'écoute seulement.

## Cadre commun
126 BPM · la mineur · notes MIDI 41–64 (C3 = 60), tonique A1 = 45 (55 Hz). Recettes 1 et 2 : **SUB** Sine OCT 0 routé **Direct** (page MIX : sans filtre ni effets), la couche FM une octave au-dessus. Modulation : glisser la poignée d'ENV/LFO sur le bouton, quantité dans MATRIX.

## Recette 1 — FM « garage » à rebond (FH Garage FM)
Source : *Garage Bass* d'Attack Magazine (Massive), convertie. Détail : `.claude/skills/house-future-rave-bass-house-production/recipes/basse-fm-metallique-bass-house.md`, `.claude/skills/sound-designer-serum/references/patches-genres.md`.
- OSC A sinus (Basic Shapes pos. 0), OCT +1 → FILTER 1 · OSC B sinus OCT +2 (2:1), FIN 0 (rond) ou −30 cents (métal), niveau 0, allumé, routage None.
- WARP 1 (OSC A) = **FM (B)** ≈ 45 % `[HEUR]` ; ENV 2 (ATK 0, DEC 238 ms = 1/8 à 126, SUS 0, REL 30 ms) → WARP 1 +60 %, → CUTOFF +100 %.
- FILTER 1 MG Low 24, CUTOFF ≈ 25 % (140–200 Hz), RES 0 · ENV 1 ATK 0, DEC 300 ms, SUS −6 dB, REL ≈ 150 ms `[HEUR]`.
- MONO + LEGATO, PORTA 40–80 ms · FX MAIN : Distortion Tube (drive et mix ≈ 25–30 %) → Hyper/Dimension (SIZE 0, MIX ≈ 25 %) → EQ coupe-bas 75 Hz.
- Macros : M1 FM (WARP 1 0–70 %), M2 Cutoff, M3 Drive.

## Recette 2 — FM métallique élastique, pour le drop (FH Metal FM)
- SUB comme ci-dessus · OSC A sinus OCT +1 → FILTER 1 · OSC B sinus **OCT +3, SEM +7** (6:1, EDMProd), niveau 0, allumé.
- WARP 1 = FM (B) 30 % + ENV 2 (DEC 180 ms, SUS 0) → WARP 1 +50 % (> 40 % = hurlant) · WARP 2 = Distortion **Diode 2** ≈ 30 % `[HEUR]`.
- « Thwack » : ENV 3 (ATK 0, DEC 50 ms, SUS 0) → SEM d'OSC A +12 · LFO 2 MODE ENVELOPE 1/4 → WARP 1 +10 %.
- FILTER 1 MG Low 24, CUTOFF 30 %, ENV 2 → CUTOFF +70 % · MONO + LEGATO, PORTA 60 ms.
- FX : Distortion Tube léger → Compressor MULTIBAND MIX 20 % → EQ coupe-bas 75 Hz, −3 dB vers 250 Hz → Hyper/Dimension discret. Drop 2 : automatiser l'OCT d'OSC B de +3 à +2.

## Recette 3 — Organ bass en contretemps (FH Organ)
Approximation additive du Korg M1 *Organ 2* (tirettes 16′ + 8′ + 5⅓′) ; un vrai multisample serait plus fidèle.
- SUB éteint · OSC A sinus OCT 0 (h1) · OSC B sinus OCT +1 (h2), −3 dB · OSC C sinus, clic droit sur OCT › **Harmonics** ×3 (h3), 0 dB.
- FILTER 1 (A+B+C) MG Low 12, CUTOFF ≈ 1 kHz, ENV 2 → CUTOFF +40 % avec DEC 10 ms (clic de touche).
- ENV 1 ATK 1 ms, DEC 250 ms, SUS 0 (court) ou SUS 70 %, REL 20 ms (tenu) · MONO + LEGATO, PORTA 0.
- FX : Chorus (MIX 15 %) → Reverb Hall courte (MIX 10 %) → Utility MONO BASS 120 Hz.

## Clip MIDI de test (4 mesures, contretemps : pas 3, 7, 11, 15)
| Mesure | Accord (stabs) | Pas 3 | Pas 7 | Pas 11 | Pas 15 |
|---|---|---|---|---|---|
| 1 | Am7 | A1 45 | A1 45 | A2 57 | A1 45 |
| 2 | Fmaj7 | F1 41 | F1 41 | F2 53 | F1 41 |
| 3 | Dm9 | D2 50 | D2 50 | D3 62 | D2 50 |
| 4 | Em7 | E2 52 | E2 52 | E3 64 | E2 52 |
Vélocités 110 (pas 3 et 11) / 100 ; durée 0,25 temps (recettes 1, 2) ou 0,3 (recette 3) ; swing 52–56 % sur les hats seulement.

## Vérifications
1. Kick 909 + basse seuls, 8 mesures : ça groove, sinon corriger le MIDI. 2. Utility mono sur le Main : sub inchangé, FM garde son corps. 3. F1 (41) puis E3 (64) : caractère stable, sinon baisser M1 dans l'aigu. 4. Sidechain (Compressor natif, déclenché par le kick) 3–6 dB, attaque 1–5 ms, release 100–150 ms, 6:1 `[HEUR]`. 5. Preset sauvé sous un nouveau nom.

## Journal
- 24 sept. 2026 : **trois recettes de basse future house proposées** (FH Garage FM, FH Metal FM, FH Organ) avec clip de test Am7–Fmaj7–Dm9–Em7 ; rien d'écrit dans Live ; reste : construire la recette choisie.
- 24 sept. 2026 : **question posée, sans réponse** : « laquelle des trois recettes construis-tu en premier ? » — à reposer en début de session.
