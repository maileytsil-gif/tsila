# Serum 2 (VST3 2.1.5) — piloter la fenêtre

## Calibrage — À REFAIRE (19 sept. 2026)

> Repris le 8 oct. 2026 de la branche `claude/new-session-x91wej` (relevé du 19 sept.). Depuis, les notes du 29 sept. disent que les clics de fond fonctionnent, sans préciser l'échelle : **vérifier l'échelle réglée dans Serum et la taille d'une capture de la fenêtre avant tout clic aux coordonnées ci-dessous**, puis remplir le tableau.

| Champ | Valeur |
|---|---|
| Géométrie de référence des repères ci-dessous | **1190 × 759** |
| Géométrie actuelle de la fenêtre | **≈ 1596 × 1024** — mesurée par détection d'arêtes sur capture, voir « Hypothèse d'échelle » |
| Échelle / zoom d'interface Serum | **134 %** (réglée le 19 sept. 2026) |
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

## Hypothèse d'échelle — non vérifiée

L'échelle est à **134 %**. L'ancienne fiche notait « 1190 × 759 » **sans dire à quelle
échelle** : c'est le défaut qui a rendu cette recalibration nécessaire, et il empêche
de conclure ici. Sous l'hypothèse que 1190 × 759 avait été relevé à 100 %, le facteur
est 1,34 et la fenêtre fait **1595 × 1017**.

**Mesure du 19 sept. 2026.** Une capture de la fenêtre (avec le bureau autour) a été
analysée par détection d'arêtes : bords à x ≈ 16 et 1612, y ≈ 16 et 1040, soit une
fenêtre d'environ **1596 × 1024**.

- **Largeur : 1596 contre 1595 prédits — le facteur 1,34 est confirmé à 1 pixel près.**
- Hauteur : 1024 contre 1017 prédits, **7 px de plus, inexpliqués**. Probablement du
  chrome de fenêtre qui ne suit pas le zoom de Serum — c'est exactement la
  non-uniformité annoncée plus bas. Non confirmé.

Ces bords sont détectés sur une capture qui contenait aussi Ableton et le bureau : ils
valent mieux qu'une prédiction, moins qu'une capture propre de la seule fenêtre. La
ligne « Repères vérifiés le » reste vide tant que l'étape 4 n'a pas été faite.

Une capture propre trancherait définitivement :

| Taille de la capture | Conclusion |
|---|---|
| 1595 × 1017 | Hypothèse confirmée, facteur 1,34 |
| 3190 × 2034 | Idem, mais capture Retina 2× — diviser par 2 avant de mapper |
| autre chose | 1190 × 759 n'était pas à 100 %. Le vrai facteur est `largeur_capture / 1190` |

Repères mappés à 1,34 — **hypothèses de départ, aucune n'est vérifiée** :

| Repère | 1190 × 759 | × 1,34 |
|---|---|---|
| SUB on/off | (11,101) | (15,135) |
| OSC A | (86,101) | (115,135) |
| OSC B | (356,101) | (477,135) |
| NOISE | (896,101) | (1201,135) |
| FILTER 1 | (996,101) | (1335,135) |
| onglets OSC / MIX / FX / MATRIX / GLOBAL | 199/266/334/403/470 × 50 | 267/356/448/540/630 × 67 |
| MONO | (1058,627) | (1418,840) |
| LEGATO | (1058,653) | (1418,875) |
| PORTA | (1081,720) | (1449,965) |
| ENV 1 ATK/HOLD/DEC/SUS/REL | 200/255/308/362/413 × 593 | 268/342/413/485/553 × 795 |
| icône navigateur | (1010,36) | (1353,48) |

**Multiplier ne remplace pas vérifier.** Une interface de plug-in ne se remet pas
forcément à l'échelle de façon uniforme : les tailles de police et les bords s'alignent
sur des pixels entiers, et un élément peut se replacer au lieu de grandir. L'erreur se
cumule vers la droite et vers le bas — les repères les plus éloignés de l'origine
(FILTER 1, PORTA, MONO/LEGATO) sont les moins sûrs. L'étape 4 reste obligatoire : le
mapping fait gagner le relevé, pas la vérification.

## Relever des valeurs sans toucher au patch

Serum n'affiche pas les nombres sous ses boutons. Deux façons de les obtenir, dans cet
ordre — la première ne touche pas à l'interface, donc ne peut rien dérégler.

### 1. Par le bridge (lecture seule, à préférer)

`../../../producteur-live/scripts/pyl.sh lire_serum.py` avec :

```python
# Lecture seule : relève les paramètres Serum exposés à Live.
# N'écrit rien — ne fait que lire p.value et demander son affichage.
res = []
for t in song.tracks:
    for d in t.devices:
        if 'Serum' in d.name:
            for p in d.parameters:
                res.append([t.name, p.name, p.str_for_value(p.value)])
result = res
```

Renvoie une liste de `[piste, paramètre, valeur affichée]`. Aucune écriture.

**Limite** : Live ne voit que les paramètres que le plug-in publie à l'hôte. Si CUTOFF,
RES ou DRIVE n'apparaissent pas dans la sortie, c'est qu'ils ne sont pas exposés sur
cette instance — passer à la méthode 2. Le nom affiché dans Serum ne garantit pas une
adresse accessible.

### 2. Par l'interface (avec une précaution)

Double-cliquer le bouton ouvre un champ qui **affiche la valeur courante**. Lire, puis
**quitter par Échap, jamais par Entrée** : Échap annule, Entrée valide, et la fiche note
déjà que la validation se comporte mal en arrière-plan. Sur un template, un chiffre
validé par accident se propage à tout ce qui en descendra.

## Fiche

- Ouvrir : `ppal-select` `openPluginWindow: true` sur le device ; si rien n'apparaît, cliquer le bouton « fenêtre » dans le titre du device (fenêtre principale, vue Session, ≈ x 29 / y 479 sur capture 1568 px). Taille de référence des repères : 1190×759 (échelle non notée, voir « Calibrage ») ; `app_screenshot` de la fenêtre puis `app_click`/`app_batch` en coordonnées de cette capture.
- Repères (capture 1190×759, **à revérifier** : voir « Calibrage ») : oscillateur **SUB** on/off (11,101), OSC A on/off (86,101), OSC B (356,101), NOISE (896,101), FILTER 1 (996,101) ; onglets OSC (199,50) MIX (266) FX (334) MATRIX (403) GLOBAL (470) ; **MONO** (1058,627), **LEGATO** (1058,653), PORTA (1081,720) ; ENV 1 readouts ATK/HOLD/DEC/SUS/REL (≈ 200/255/308/362/413 × 593) — double-clic ouvre un champ mais la validation Entrée n'arrive pas en arrière-plan ; le glisser des boutons ne passe pas non plus.
- **Navigateur de presets** : icône liste (1010,36) → arbre à gauche (Factory › Arp/Bass/Bell/…/Drum…) → double-clic sur le preset → « ‹ nom › » en haut, macros en bas. Presets factory utiles : Drum › « DR - Kick Minimal » (kick synthétique rond, suit la note MIDI), Bass › Electric/Sub, Keys/Pad pour nappes. Banques perso dans `/Library/Audio/Presets/Xfer Records/Serum 2 Presets/Presets/User` (TKNVLT Techno Kick Collection, « Kick Future House Tsila », F Brooks kicks).
- Ce qui a marché en arrière-plan : toggles (SUB, OSC, MONO, LEGATO), onglets, navigateur, double-clic de preset. Ce qui n'a pas marché : saisie de valeur, glisser de bouton → demander à l'utilisateur ou passer en plein écran (`request_full_control`, `computer_batch` avec zoom pour lire).
- Sub Serum validé : osc SUB sinus seul, OSC A off, MONO+LEGATO, release à régler par l'utilisateur (90 ms) ; niveau ≈ −4 dB avant fader avec Utility 0 dB.
- Un preset chargé « suit la hauteur » : clips KICK en C1 → macro Pitch ou transposition des clips (F0/F1) si on veut l'accorder au morceau.
- **Carte complète du plug-in** (chaque page, chaque paramètre, plages, listes de menus, dossiers, ce que Live expose) : `../../../references/serum2-cartographie.md`.
- **Réutiliser un Serum 2 « configuré » dans d'autres Sets (vérifié 29 sept. 2026, Live 12.4.6, Serum 2.1.5)** : envelopper le Serum dans un Instrument Rack (`ppal-update-device wrapInRack`) puis sauver le rack (disquette) → `User Library/Presets/Instruments/Instrument Rack/<nom>.adg`. Le XML du .adg contient `<Vst3Preset>` avec `<ParameterSettings>` = **les 115 `PluginParameterSettings` du Configure** (ParameterId, Type PluginFloatParameter, VisualIndex), `StoredAllParameters true`, plus `<ProcessorState>` et `<ControllerState>` (état du plug-in). Rack de référence : « Serum 2 API » (116 paramètres exposés : Sub/A/B/C enable, octave/semi/fine, WT Pos, warp, level, unison detune/blend, Noise enable/level/pitch, Filter 1 on/freq/res/drive/wet, Env 1 AHDSR, Macro 1–8, LFO 1 rate, Mono/Legato/Porta, Bend). Un `.vstpreset` ne garde PAS cette liste. À charger dans un nouveau Set par le navigateur ou `lom.py load "<piste>" "Serum 2 API" user_library`. **Non exposé même ainsi** : choix de la table d'ondes, Env 2/3, matrice (pitch env), type de filtre, sample du Noise → fenêtre, ou macros mappées par l'utilisateur.
- **Piège « Sub Coarse Pitch » (29 sept. 2026, Set « Sous-Sol »)** : paramètre exposé en demi-tons de −64 à +64 (raw 0,5 = « -- » = 0). Trouvé à −32,38 sur le kick : l'osc Sub jouait ≈ 7 Hz, inaudible, et le kick n'avait aucun grave malgré Sub Enable. Toujours relire `Sub Coarse Pitch` (et A/B/C Coarse Pitch) quand un sub « ne se ressent pas » ; le remettre à raw 0,5. Autre piège du même jour : des notes de kick de 1/16 (117 ms à 128 BPM) coupent le son au note-off, la Decay d'Env 1 ne sert alors à rien → régler Env 1 Release (150 ms pour un 808 court).
