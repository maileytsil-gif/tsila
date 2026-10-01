# Projet : test du skill house — basse future house (Serum 2, piste 5)

**REPRISE (1er oct. 2026, Set non sauvegardé par Claude)** : nouveau Set Ableton ouvert par l'utilisateur, Serum 2 sur la piste 5. **Recette choisie : 2, FH Metal FM** ; la fiche de montage pas à pas est plus bas, § « Fiche de montage, recette 2 ». Rien n'a encore été écrit dans Live : les sessions précédentes tournaient dans le cloud, sans accès au Mac.
En attente : le nom du Set.
Prochaines étapes : 1) sur le Mac, `cd ~/tsila && git pull`, puis lancer Claude Code dans `~/tsila` (Producer Pal, `lom.py` et contrôle d'écran y sont disponibles) ; 2) Sauver sous, tempo 126, la mineur, repères ; 3) fiche de montage, étapes M1 à M9, une étape par échange, sur la piste 5 ; 4) clip de test et les 5 vérifications ; 5) preset sauvé sous « FH Metal FM » ; 6) kick 909 + sidechain, puis éventuellement les recettes 1 et 3 pour comparer.

## Consignes permanentes
- Une étape par échange ; Set sauvé avant et après chaque étape ; règle anti hot-swap (ne jamais remplacer Serum sur la piste 5 sans le dire).
- Aucun réglage n'est « le son de » Tchami, Oliver Heldens ou un autre : références d'écoute seulement.

## Cadre commun
126 BPM · la mineur · notes MIDI 41–64 (C3 = 60), tonique A1 = 45 (55 Hz). Recettes 1 et 2 : **SUB** Sine OCT 0 routé **Direct** (page MIX : sans filtre ni effets), la couche FM une octave au-dessus. Modulation : glisser la poignée d'ENV/LFO sur le bouton, quantité dans MATRIX.

## Recette 1 — FM « garage » à rebond (FH Garage FM)
Source : *Garage Bass* d'Attack Magazine (Massive), convertie. Détail : `.claude/skills/house-future-rave-bass-house-production/recipes/basse-fm-metallique-bass-house.md`, `.claude/skills/sound-designer-serum/references/patches-genres.md`.
- OSC A sinus (WT POS 1), OCT +1 → FILTER 1 · OSC B sinus OCT +2 (2:1), FIN 0 (rond) ou −30 cents (métal), niveau 0, allumé, routage None.
- WARP 1 (OSC A) = **FM (B)** ≈ 45 % `[HEUR]` ; ENV 2 (ATK 0, DEC 238 ms = 1/8 à 126, SUS 0, REL 30 ms) → WARP 1 +60 %, → CUTOFF +100 %.
- FILTER 1 MG Low 24, CUTOFF ≈ 25 % (140–200 Hz), RES 0 · ENV 1 ATK 0, DEC 300 ms, SUS −6 dB, REL ≈ 150 ms `[HEUR]`.
- MONO + LEGATO, PORTA 40–80 ms · FX MAIN : Distortion Tube (drive et mix ≈ 25–30 %) → Hyper/Dimension (SIZE 0, MIX ≈ 25 %) → EQ coupe-bas 75 Hz.
- Macros : M1 FM (WARP 1 0–70 %), M2 Cutoff, M3 Drive.

## Recette 2 — FM métallique élastique, pour le drop (FH Metal FM)
- SUB comme ci-dessus · OSC A sinus OCT +1 → FILTER 1 · OSC B sinus **OCT +3, SEM +7** (6:1, EDMProd), niveau 0, allumé.
- WARP 1 = FM (B) 30 % + ENV 2 (DEC 180 ms, SUS 0) → WARP 1 +50 % (> 40 % = hurlant) · WARP 2 = Distortion **Diode 2** ≈ 30 % `[HEUR]`.
- « Thwack » : ENV 3 (ATK 0, DEC 50 ms, SUS 0) → **CRS** d'OSC A +12 st (CRS et non SEM : CRS est le réglage continu prévu pour la modulation de hauteur, `[DOC p. 29–30]`) · LFO 2 MODE ENVELOPE 1/4 → WARP 1 +10 %.
- FILTER 1 MG Low 24, CUTOFF 30 %, ENV 2 → CUTOFF +70 % · MONO + LEGATO, PORTA 60 ms.
- FX : Distortion Tube léger → Compressor MULTIBAND MIX 20 % → EQ coupe-bas 75 Hz, −3 dB vers 250 Hz → Hyper/Dimension discret. Drop 2 : automatiser l'OCT d'OSC B de +3 à +2.

## Recette 3 — Organ bass en contretemps (FH Organ)
Approximation additive du Korg M1 *Organ 2* (tirettes 16′ + 8′ + 5⅓′) ; un vrai multisample serait plus fidèle.
- SUB éteint · OSC A sinus OCT 0 (h1) · OSC B sinus OCT +1 (h2), −3 dB · OSC C sinus, clic droit sur OCT › **Harmonics** ×3 (h3), 0 dB.
- FILTER 1 (A+B+C) MG Low 12, CUTOFF ≈ 1 kHz, ENV 2 → CUTOFF +40 % avec DEC 10 ms (clic de touche).
- ENV 1 ATK 1 ms, DEC 250 ms, SUS 0 (court) ou SUS 70 %, REL 20 ms (tenu) · MONO + LEGATO, PORTA 0.
- FX : Chorus (MIX 15 %) → Reverb Hall courte (MIX 10 %) → Utility MONO BASS 120 Hz.

## Fiche de montage, recette 2 (FH Metal FM) : étapes M1 à M9
Pour la session Mac. Une étape par échange, capture de Serum après chaque étape, Set sauvé avant M1 et après M9. Ne pas remplacer l'instance de Serum 2 de la piste 5 (règle anti hot-swap) : demander d'abord si le patch qui s'y trouve doit être gardé, puis partir de menu principal › Initialization › **Init Preset**. Repères : `.claude/skills/sound-designer-serum/references/serum2-cartographie.md` § 3, 4.2, 5, 6, 7, 8, 9. À 126 BPM : 1/16 = 119 ms, 1/8 = 238 ms, 1/4 = 476 ms `[CALC]`.

| Étape | Où | Réglages | Contrôle |
|---|---|---|---|
| **M1** Sources | page OSC | **SUB** allumé, forme Sine, OCT 0, LEVEL 100 % · **OSC A** Wavetable, WT POS 1 (sinus), OCT +1, SEM 0, FIN 0 · **OSC B** allumé, sinus, **OCT +3, SEM +7** = 2 octaves + quinte au-dessus d'A, soit 6:1 à 2 cents près `[CALC]` ; ratio exact : clic droit sur OCT d'OSC B › Ratio, source A, ratio 6 `[DOC p. 30]` | Vue 2D : A et B montrent un sinus |
| **M2** Routage | page MIX | SUB → **Direct** (sans filtre ni effets) · OSC A → Filter (FILTER 1) · OSC B → **None** (source de FM muette, elle doit rester allumée `[DOC p. 54–56]`) · FILTER 1 → Main | SUB seul : sinus propre ; OSC B seul : silence |
| **M3** FM et grain | OSC A | **WARP 1 = FM (B)**, 30 % ; si un type de FM est demandé, Linear (garde la hauteur même très modulé `[DOC p. 54–55]`), noter le type pris · **WARP 2 = Distortion › Diode 2**, 30 % `[HEUR]` | A1 tenu : hauteur juste, râle métallique |
| **M4** Filtre | FILTER 1 | allumé, **MG Low 24**, CUTOFF 30 %, RES 0, DRIVE 0, key track off | Courbe passe-bas visible, A grisé tant qu'il n'y est pas routé |
| **M5** Enveloppes | ENV 1–3 | **ENV 1** ATK 0, DEC 300 ms, SUS −6 dB, REL 120 ms `[HEUR]` · **ENV 2** ATK 0, DEC 180 ms, SUS 0, REL 30 ms → glisser sur WARP 1 d'OSC A **+50 %** et sur CUTOFF de FILTER 1 **+70 %** · **ENV 3** ATK 0, DEC 50 ms, SUS 0, REL 0 → glisser sur **CRS** d'OSC A, profondeur réglée pour **+12 st** au pic (≈ 9 % si la profondeur se compte sur toute la course −64…+64 `[CALC]`, à vérifier à l'infobulle ou à l'oreille `[TEST]`) | MATRIX : 3 lignes ENV ; attaque « thwack » d'une octave qui retombe en 50 ms |
| **M6** Mouvement | LFO 2 | MODE **ENVELOPE**, BPM, RATE 1/4, forme par défaut → WARP 1 d'OSC A **+10 %** (pas plus : ça distord vite) | MATRIX : ligne LFO 2 ; au pic, WARP 1 ≈ 30 + 50 + 10 = 90 % puis retombe vers 30 % |
| **M7** Jeu | panneau VOICING | **MONO** + **LEGATO**, PORTA 60 ms, ALWAYS off : le glide ne s'entend que si deux notes se chevauchent, le clip de test n'en a pas | Une seule voix active à la fois |
| **M8** Effets | page FX, rack MAIN, dans l'ordre | **Distortion** MODE Tube, DRIVE ≈ 20 %, MIX ≈ 30 % `[HEUR]` → **Compressor** MODE Multiband, MIX 20 % → **Equalizer** : bande basse **High Pass 75 Hz**, bande haute **Peak 250 Hz −3 dB** → **Hyper/Dimension** UNISON 0 (Dimension seul), SIZE bas, MIX ≈ 15 % | Le SUB, routé Direct, ne passe dans aucun de ces modules |
| **M9** Macros et preset | bas droite, puis barre du haut | **M1 « FM »** → WARP 1 d'OSC A (0 → +70 %) · **M2 « CUTOFF »** → CUTOFF de FILTER 1 · **M3 « DRIVE »** → WARP 2 d'OSC A · **M4 « B OCT »** → OCT d'OSC B, profondeur −1 octave (pour le drop 2 : automatiser M4 dans Live, les macros sont visibles sans Configure) · sauver le preset sous **« FH Metal FM »** | Infobulle de chaque macro : bonne destination ; preset rechargeable |

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
- 1er oct. 2026 : **réponse de l'utilisateur : recette 2 (FH Metal FM)**. Fiche de montage M1–M9 écrite (cloud, rien d'écrit dans Live). Corrections : le thwack module **CRS** d'OSC A, pas SEM (CRS est le réglage continu prévu pour la modulation de hauteur, manuel p. 29–30) ; « Basic Shapes pos. 0 » devient « WT POS 1 » (la position va de 1 à 256). Reste : construire sur le Mac, puis le clip de test et les 5 vérifications.
