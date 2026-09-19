# Serum 2 (VST3 2.1.5) — piloter la fenêtre

## Calibrage — À REFAIRE (19 sept. 2026)

| Champ | Valeur |
|---|---|
| Géométrie de référence des repères ci-dessous | **1190 × 759** |
| Géométrie actuelle de la fenêtre | **inconnue** — fenêtre redimensionnée « pour plus de visibilité » |
| Échelle / zoom d'interface Serum | **à relever** |
| Capture de référence du bouton « fenêtre » du device | 1568 px de large |
| Repères vérifiés le | — |

**Tant que ce tableau n'est pas rempli, aucun clic aux coordonnées stockées.** Elles
sont absolues et calées sur 1190 × 759 : après un redimensionnement, un clic ne « rate »
pas, il tombe sur un autre contrôle et modifie le patch sans rien signaler. Capture
d'abord, clic ensuite.

## Recalibrer en 5 étapes

1. **Instance jetable.** Créer une piste MIDI vide, y charger Serum 2, calibrer
   dessus. Ne jamais calibrer sur une instance dont le patch compte : Live n'annule
   pas de façon fiable un changement interne à un VST. Supprimer la piste à la fin.
2. **Déclarer la géométrie.** `app_screenshot` de la fenêtre Serum entière. Relever
   largeur × hauteur de la capture et le réglage d'échelle de Serum, puis les écrire
   dans le tableau ci-dessus **avant** de relever le moindre repère.
3. **La rangée d'ancrage.** SUB, OSC A, OSC B, NOISE et FILTER 1 sont sur une même
   rangée : une capture donne le `y` commun et les cinq `x`. C'est la rangée qui sert
   de contrôle pour tout le reste.
4. **Vérifier par un aller-retour réversible.** Cliquer SUB on/off, relire l'état,
   le remettre. Un repère n'est validé que si la relecture confirme le basculement —
   jamais sur la seule apparence de la capture. Calibrer uniquement sur des toggles,
   jamais sur un bouton rotatif ou un champ de valeur.
5. **Relever le reste et réécrire la fiche.** Onglets (OSC/MIX/FX/MATRIX/GLOBAL),
   MONO/LEGATO/PORTA, readouts ENV 1, icône du navigateur de presets. Remplacer les
   coordonnées ci-dessous, dater la ligne « Repères vérifiés le », et retester
   l'ouverture du navigateur de presets de bout en bout.

## Ouvrir la fenêtre

`ppal-select` avec `openPluginWindow: true` sur le device ; si rien n'apparaît, cliquer
le bouton « fenêtre » dans le titre du device (fenêtre principale, vue Session,
≈ x 29 / y 479 sur capture 1568 px). Puis `app_screenshot` de la fenêtre et
`app_click` / `app_batch` en coordonnées de cette capture.

## Repères — géométrie 1190 × 759, à revérifier

- Oscillateurs : **SUB** on/off (11,101), **OSC A** (86,101), **OSC B** (356,101),
  **NOISE** (896,101), **FILTER 1** (996,101).
- Onglets : OSC (199,50), MIX (266), FX (334), MATRIX (403), GLOBAL (470).
- Voicing : **MONO** (1058,627), **LEGATO** (1058,653), PORTA (1081,720).
- Readouts ENV 1 ATK/HOLD/DEC/SUS/REL : ≈ 200/255/308/362/413 × 593. Le double-clic
  ouvre un champ mais la validation Entrée n'arrive pas en arrière-plan ; le glisser
  des boutons ne passe pas non plus.

## Navigateur de presets

Icône liste (1010,36) → arbre à gauche (Factory › Arp/Bass/Bell/…/Drum…) → double-clic
sur le preset → « ‹ nom › » en haut, macros en bas. Presets factory utiles :
Drum › « DR - Kick Minimal » (kick synthétique rond, suit la note MIDI),
Bass › Electric/Sub, Keys/Pad pour nappes. Banques perso dans
`/Library/Audio/Presets/Xfer Records/Serum 2 Presets/Presets/User`
(TKNVLT Techno Kick Collection, « Kick Future House Tsila », F Brooks kicks).

## Ce qui marche, ce qui ne marche pas

En arrière-plan : toggles (SUB, OSC, MONO, LEGATO), onglets, navigateur, double-clic de
preset. **Ne marche pas** : saisie de valeur, glisser de bouton → demander à
l'utilisateur, ou passer en plein écran (`request_full_control`, `computer_batch` avec
zoom pour lire).

## Acquis à ne pas reperdre

- **Sub Serum validé** : osc SUB sinus seul, OSC A off, MONO + LEGATO, release réglée
  par l'utilisateur (90 ms) ; niveau ≈ −4 dB avant fader avec Utility à 0 dB.
- Un preset chargé **suit la hauteur** : clips KICK en C1 → macro Pitch ou transposition
  des clips (F0/F1) pour l'accorder au morceau.
