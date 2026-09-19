# Serum 2 (VST3 2.1.5) — piloter la fenêtre

## Calibrage — À REFAIRE (19 sept. 2026)

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

## Relever des valeurs sans toucher au patch

Serum n'affiche pas les nombres sous ses boutons. Deux façons de les obtenir, dans cet
ordre — la première ne touche pas à l'interface, donc ne peut rien dérégler.

### 1. Par le bridge (lecture seule, à préférer)

`scripts/pyl.sh lire_serum.py` avec :

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

## Navigateur de presets

Icône liste (1010,36) → arbre à gauche (Factory › Arp/Bass/Bell/…/Drum…) → double-clic
sur le preset → « ‹ nom › » en haut, macros en bas. Presets factory utiles :
Drum › « DR - Kick Minimal » (kick synthétique rond, suit la note MIDI),
Bass › Electric/Sub, Keys/Pad pour nappes. Banques perso dans
`/Library/Audio/Presets/Xfer Records/Serum 2 Presets/Presets/User`
(TKNVLT Techno Kick Collection, « Kick Future House Tsila », F Brooks kicks).

## Template « serum sound designer » — état lu sur capture le 19 sept. 2026

Preset enregistré par l'utilisateur comme **point de départ réutilisable**, pas comme
son fini.

**Nom : « serum sound designer »** — lu dans le champ de preset de Serum sur la
deuxième capture du 19 sept. 2026. La première capture du même jour affichait
« serum design » : le template a donc été renommé ou réenregistré entre les deux.
**Reste à vérifier sur le disque si l'ancien fichier subsiste** ; s'il y en a deux, on
repartira un jour du mauvais sans s'en apercevoir.

Chemin du fichier : **toujours inconnu**. ARTIST et DESC vides.

Relevé **visuellement sur une capture**, pas dans Live : Serum n'affiche pas les valeurs
numériques des boutons, seulement leurs positions.

| Élément | État lu |
|---|---|
| SUB | **off** |
| OSC A | **on** — WAVETABLE, « Default Shapes », OCT 0 / SEM 0 / FIN 0, position 1, phase 180°, RAND 100, UNISON 1, WARP 1 et 2 off |
| OSC B · OSC C · NOISE | **off** (NOISE chargé sur « AC hum1 ») |
| FILTER 1 | **off** |
| FILTER 2 | **on** — « MG Low 12 » (ladder Moog 12 dB), banque A |
| Voicing | **POLY 8**, MONO décoché, LEGATO décoché |
| **ENV 1** (amplitude) | ATK **1,0 ms** · HOLD **0,0 ms** · DEC **1,00 s** · SUS **0,0 dB** · REL **15 ms** · RETRIG |
| ENV 4 | ATK 0,5 ms · HOLD 0,0 ms · DEC 1,00 s · SUS 100 % · REL 15 ms · RETRIG |
| LFO 1 | triangle, Forward, 1/4, synchro BPM |
| Global | TRANSPOSE 0, SWING OFF, macros 1–8 au minimum |

L'état est cohérent avec une intention de template : un seul oscillateur sur la wavetable
par défaut, aucune transposition, unison à 1, warp désactivé, macros à zéro, un filtre
prêt à travailler. Rien n'est sculpté — c'est une toile vierge jouable.

**Ne pas le mettre au registre de signature.** Le registre de `drums-signature` est
réservé aux sons **déjà validés à l'écoute** dans un morceau. Un point de départ neutre
n'en est pas un : sa place est ici, dans les références de `vst-sound-design`, avec les
recettes qui s'appuieront dessus.

**Ce n'est pas non plus le sub validé** du registre (SUB éteint, polyphonique, source
wavetable) : le niveau ≈ −3/−4 dB du sub, sa chaîne EQ 24–130 Hz et la mesure kick/sub
ne sont pas remis en cause.

### Vérifié

- **Routage du filtre — OK** (vérifié à l'écoute par l'utilisateur, 19 sept. 2026).
  Bouger le CUTOFF de FILTER 2 change bien le son : OSC A traverse FILTER 2.
  **Leçon à retenir : le badge `F1` d'un oscillateur ne suffit pas à conclure au
  routage.** OSC A porte `F1` alors que FILTER 1 est éteint et FILTER 2 actif, et le
  son passe quand même par FILTER 2. Ne pas rejouer ce faux diagnostic ; sur une
  question de routage Serum 2, écouter ou mesurer avant d'affirmer.

### Enveloppe d'amplitude — ce qu'elle implique

ENV 1 est **une porte, pas une enveloppe sculptée** : attaque quasi immédiate (1 ms),
maintien à plein niveau tant que la note dure, extinction en 15 ms.

**Conséquence à connaître avant de partir de ce template : DEC = 1,00 s ne fait rien.**
Dans une ADSR, le decay ne descend que vers le sustain ; comme SUS est à **0,0 dB**,
c'est-à-dire le niveau plein, il n'y a rien à descendre. Tourner DEC restera sans effet
audible tant que SUS n'aura pas été baissé. Pour un pluck ou un stab au départ de ce
template : **baisser SUS d'abord, régler DEC ensuite.**

À noter aussi, utile pour lire une capture : **ENV 1 affiche son sustain en dB**
(enveloppe d'amplitude) alors que les enveloppes de modulation l'affichent en **%** —
ENV 4 montre `SUS 100 %`. Même position de bouton, deux unités.

### Reste à vérifier

1. **Valeurs chiffrées** des boutons (CUTOFF, RES, DRIVE, LEVEL) : positions lues,
   nombres non affichés. À relever par survol ou double-clic.
2. **Chemin du fichier** et présence éventuelle d'un doublon « serum design », pour
   pouvoir le recharger sans le chercher et sans se tromper de version.

État du template : **sain sur le trajet du signal, enveloppe d'amplitude connue**,
incomplet sur les valeurs de filtre et le rangement du fichier.

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
