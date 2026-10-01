# Serum 2 — automation depuis Live, et migration depuis Serum 1

Recherche du 18 septembre 2026. `[OFF]` = documentation officielle Xfer ou Ableton · `[MAG]` = presse spécialisée · `[FORUM]` = avis d'utilisateurs, non vérifié · `[I]` = déduction.

---

# A. POURQUOI SERUM N'EXPOSE QU'UN PARAMÈTRE — le diagnostic

## Ce n'est pas Serum, c'est Live `[I, à partir de trois sources officielles]`

`[OFF Ableton]` Le manuel Live 12 : Live crée automatiquement un panneau **pour les plug-ins ayant jusqu'à 64 paramètres modifiables**. Au-delà, « les devices dépassant ce seuil **s'ouvrent avec un panneau vide**, que vous pouvez ensuite configurer ».

L'API Live (`device.parameters`) d'un device plug-in **ne liste que les paramètres configurés, plus Device On**. Panneau vide donc `parameters` = `[Device On]`. C'est mécanique.

Serum 2 a **très largement plus de 64 paramètres**, donc panneau vide par défaut. **Serum n'y est pour rien.**

À ne pas confondre avec l'autre liste : la **liste d'automation** de Live, dans le menu déroulant de la lane, est alimentée par les paramètres que le plug-in expose à l'hôte, indépendamment de Configure. C'est là que la particularité propre à Serum 2 intervient.

## La couche propre à Serum 2 : les paramètres d'effet sont dynamiques

**C'est le point décisif, et il vient de Xfer directement.**

Sur le forum officiel, fil « Serum 2 Automation on Live 12.1 » (https://xferrecords.com/forums/general/serum-2-automation-on-live-12-1) :

- `[FORUM, 3 personnes]` Un utilisateur signale en mars 2025 : « les automations des pages OSC et mixer apparaissent, **mais rien de la page FX** n'apparaît dans Ableton ou Bitwig ». Deux autres confirment.
- `[quasi-OFF]` **steve_xfer, staff Xfer**, avril 2025 : c'est **par conception**. Les paramètres d'effets **ne sont pas exposés statiquement**. Il faut faire **clic droit → Automate** sur le contrôle dans Serum pour le rendre automatisable. Raison invoquée : une liste statique aurait produit un menu que les DAW « auraient replié ».
- `[FORUM, 1 personne]` Dans Bitwig, le paramètre n'apparaît qu'après **désactivation puis réactivation du plug-in**.

## La procédure qui en découle `[I]`

1. **Clic droit → Automate** dans Serum sur chaque paramètre d'effet visé, **avant** toute tentative de Configure ou d'écriture par script.
2. **Recharger le device** (bypass puis unbypass) si le paramètre n'apparaît pas.
3. Seulement ensuite, passer en **Configure** dans Live pour le faire entrer dans `device.parameters`.

Les pages **OSC, filtres, mixer, LFO, enveloppes et matrice** sont exposées statiquement. Seuls les **FX** demandent cette manipulation.

---

# B. LE PLAFOND DE 128, ET COMMENT LE CONTOURNER

## Confirmation

`[OFF Ableton]` Le plafond historique de 128 paramètres pour la liste d'un plug-in est confirmé par l'existence de l'option de débogage `-_PluginAutoPopulateThreshold=128`, et par les notes de version de Live 12 qui mentionnent la correction d'un crash lié à cette option **avec certains plug-ins VST3**.

`[FORUM, mais auteur = staff Xfer, donc source privilégiée]` Sur KVR, **bitcrusher (développeur Xfer)** écrit à propos de **Serum 1** : « Live peut automatiser **259 paramètres différents** dans Serum ; dans Live vous êtes restreint à **128 paramètres à la fois**, mais vous pouvez configurer lesquels. »

`[non vérifié]` Le chiffre de 128 pour **Serum 2** est repris par des sources secondaires (« jusqu'à 128 paramètres par instance, sur 8 pages virtuelles »), mais **aucun document Xfer ni Ableton ne le réaffirme explicitement pour Serum 2**.

## Le contournement, et sa réserve

Fichier `Options.txt` à créer dans `~/Library/Preferences/Ableton/Live x.x.x/`, ligne `-_PluginAutoPopulateThreshold=128` (ou `-1`), puis redémarrer Live.

**⚠ Réserve majeure** `[FORUM, 1 intervenant]` : sur le forum Cycling '74, la réponse à la question de l'auto-configuration des paramètres est « **cela ne marche maintenant qu'avec le VST2** ». D'autres fils de 2019 disent la même chose. **Or Serum 2 n'existe pas en VST2.**

`[I]` Le fait que Live 12 ait corrigé un crash **spécifiquement lié à cette option avec des VST3** laisse penser que le VST3 est désormais traité. Mais aucune source ne confirme que ça fonctionne avec Serum 2. **C'est un test de cinq minutes et il tranche la question.**

**Contournement alternatif** `[FORUM]` : héberger le plug-in **dans Max** plutôt que dans Live, et récupérer tous les paramètres en JavaScript. Lourd, mais c'est la seule voie citée qui lève réellement le plafond.

---

# C. LA PROCÉDURE CONFIGURE, ET LE LEVIER LE PLUS SOLIDE

## Ce que dit Ableton `[OFF]`

- Triangle à côté de la clé à molette, puis **Configure**, puis cliquer le paramètre **dans la fenêtre du plug-in**. « Pour certains plug-ins, il peut être nécessaire de **réellement changer la valeur du paramètre** » — un simple clic ne suffit pas toujours.
- Les paramètres se **réordonnent** dans le panneau Configure. **L'ordre est celui que vous fixez**, pas celui de Serum. Pour un pilotage par script, cet ordre est le contrat d'interface : il détermine l'index dans `device.parameters`.
- Un mapping MIDI ou Macro **crée automatiquement** le paramètre dans le panneau.
- Bouger un paramètre **à la souris** dans le plug-in pendant un enregistrement d'automation fait que Live enregistre l'automation **et ajoute le paramètre à la liste** tout seul. C'est le chemin le plus rapide pour peupler Configure.

## Le levier `[I]`

`[OFF]` Clic droit sur la barre de titre du device → **« Save as Default Configuration »**.

`[I]` **C'est la pièce maîtresse.** Construire une fois une configuration de paramètres Serum 2 dans l'ordre voulu, l'enregistrer comme configuration par défaut, et toutes les futures instances exposeront les mêmes paramètres aux mêmes index à l'API Live. **La limite devient fixe et connue au lieu d'être vide.**

## ⚠ Pièges d'indexation confirmés par le changelog officiel `[OFF]`

- **2.0.18** — « Corrigé : le rappel d'automation des paramètres d'effets **décalé d'un index après rechargement du projet** ». C'est la démonstration que **l'indexation des paramètres FX n'est pas intrinsèquement stable**.
- **2.0.17** — « Corrigé : **l'automation Ableton Live s'arrêtait lors de l'ajout de modules FX** ou quand on rendait des paramètres FX automatisables ».
- **2.0.17** — « Corrigé : la molette de modulation apparaissait deux fois dans la liste des paramètres automatisables ».
- **2.0.21** — « Ajout d'un contournement pour **Live n'affichant pas les bons noms de macros après chargement d'un set** ». **Piège direct si un script identifie un paramètre par son nom.**

---

# D. REPRODUCTIBILITÉ : un preset rappelle-t-il exactement le même son ?

**Non, pas inconditionnellement.** Six réserves.

## 1. La version de Serum 2 `[OFF]`

« Serum 2 **n'est pas forward compatible** — il ne peut pas charger des données sauvegardées par des versions plus récentes. »

**Conséquence sévère** : une session sauvée avec une version plus récente se recharge avec **le bon nom de preset mais le son Init**. Silencieusement avant la 2.0.19, qui a ajouté un message d'erreur. La 2.0.24 liste « Corrigé : **perte de données** à l'ouverture de projets faits avec des versions plus récentes ».

**→ Noter la version exacte de Serum 2 dans la mémoire de projet.**

## 2. Le mode S1 Compatibility `[OFF, manuel p. 319]`

« Serum 2 a un moteur sonore **entièrement reconstruit**. Cependant, quand vous chargez un preset Serum 1, cette option est **automatiquement activée** pour préserver une similarité sonore maximale avec Serum 1. »

La formulation officielle est « similarité maximale », **pas identité**. Le même fichier sonne différemment selon l'état de ce réglage.

**→ Conséquence directe : une recette Serum 1 rejouée à la main dans Serum 2, sans le mode S1, ne donnera pas le même résultat qu'un preset Serum 1 importé.**

## 3. Le réglage Quality `[OFF]`

**Draft = 1×, High = 2×, Ultra = 4×** de suréchantillonnage. **Il est stocké dans le preset sauf si on le verrouille** ; verrouillé, Serum ignore le réglage du preset. La préférence **Use Ultra quality when rendering** fait rendre les exports hors ligne en Ultra, quel que soit le réglage de lecture (manuel p. 315, 319).

Ce n'est pas qu'une affaire de CPU : plusieurs correctifs de la 2.0.21 montrent que **le son des warps FM, AM, PD et RM différait selon le Quality**.

## 4. Disable Smoothing `[OFF]`

Le lissage s'applique aussi aux changements par la souris. Serum « supporte l'**automation précise à l'échantillon** » : pour de l'automation rythmique rapide, **il faut désactiver le lissage**, sinon on n'obtient pas la valeur exacte au sample près.

## 5. Les fichiers externes `[OFF]`

Samples, multisamples, wavetables, bruits et réponses impulsionnelles peuvent être **embarqués ou référencés** (« Embed in Preset » ; **impossible pour le contenu d'usine**, manuel p. 22, 130). Le manuel prévoit un cas « missing audio files ». **Un preset non embarqué n'est pas portable.**

Correctifs associés : 2.0.20 « données de multisamples d'usine embarquées **supprimées lors de la sauvegarde** » ; 2.0.21 « **usage RAM excessif** au chargement de presets contenant des multisamples ».

## 6. L'état des verrous `[FORUM]`

La 2.1.5 ajoute une préférence **« restore locks when host sets state »**, ce qui implique que **l'état des verrous n'était pas restauré correctement quand l'hôte réinjecte l'état**. `[I]` Pour un pilotage par script, c'est le genre de chose qui produit des différences invisibles entre deux ouvertures du même Set.

---

# E. SERUM 1 VERS SERUM 2 — ce qui change vraiment

## Les chiffres `[OFF]`

| | Serum 1 | Serum 2 |
|---|---|---|
| Oscillateurs principaux | 2 | **3** |
| Modes par oscillateur | wavetable seul | **5 : Wavetable, Multisample, Sample, Granular, Spectral** |
| Modules de filtre | 1 | **2**, série ou parallèle |
| LFO | 4 | **jusqu'à 10** |
| Enveloppes | 3 | **4** |
| Macros | 4 | **8** |
| Slots de matrice | — | **64** |
| Effets | chaîne fixe | **13 effets + 3 splitters**, 2 bus + master, réordonnables |

## ⚠ Le piège d'interface des LFO `[OFF, manuel]`

« Quand vous initialisez un patch, **seuls les LFO 1 à 6 sont visibles. Les LFO 7 à 10 deviennent visibles après que vous ayez utilisé le LFO 6.** »

`[MAG]` C'est très probablement ce qui explique que MusicTech annonce **six LFO** dans son test alors que la documentation officielle en annonce **dix** : le testeur s'est arrêté au patch initialisé.

## Ce qui n'existe plus ou fonctionne différemment

1. **Pas de VST2.** Serum 2 est VST3, Audio Unit et AAX seulement. Tout ce qui dépendait du VST2 tombe, y compris certains contournements Ableton.
2. **Compatibilité à sens unique** `[OFF]`. Les presets Serum 1 s'ouvrent dans Serum 2 ; **l'inverse est impossible**. Les deux plug-ins s'installent côte à côte et sont **deux plug-ins distincts** : les anciens projets ne sont pas convertis, volontairement, « pour que vous puissiez mettre à jour vos morceaux manuellement ». **Serum 1 est déclaré end-of-life.**
3. **Le switch HOST des LFO a changé de sémantique** `[OFF]`. « Contrairement à Serum 1, le switch HOST a maintenant un effet **quand BPM est désactivé**. » Un LFO vraiment libre exige HOST désactivé. **Mêmes réglages visuels, comportement différent.**
4. **Le verrouillage par paramètre a été supprimé** `[OFF, changelog]`. La 2.0.21 retire l'option de verrouiller individuellement les paramètres FX, la 2.0.22 celle des oscillateurs (sauf coarse, pan et level), enveloppes, mixer, portamento et matrice. Le manuel 1.0.3 (2.0.18) décrit encore **Lock Parameter** sur presque tout contrôle (p. 26) : c'est l'état d'avant ces versions. Le verrouillage est passé d'un grain fin à un grain groupé.
5. **Un warp spectral a été renommé** `[OFF]`. En 2.0.19, « Pitch Shift » est devenu **« Pitch Blend »**, et un nouveau « Pitch Shift » amélioré a pris le nom. **Un patch qui dit « Pitch Shift » ne désigne pas la même chose avant et après.**
6. **Un boost de niveau a été retiré** `[OFF]`. La 2.0.23 « corrige le volume master par défaut des FX de Serum 2 pour retirer un **boost de 1,37 dB** ». Le même patch ne sort pas au même niveau avant et après.
7. **Les FX sont paraphoniques** `[OFF, p. 159]`, voir la fiche dédiée aux effets.

## Les nouveautés structurantes `[OFF]`

- **N'importe quel oscillateur ou filtre peut devenir source de modulation**, donc modulation à taux audio.
- **AUX SOURCE** : une source secondaire qui module la profondeur d'une modulation, avec **courbes éditables sur la source et sur l'aux source**, et inversion possible. Une macro peut servir d'aux source et être elle-même modulée.
- **Les macros sont aussi destinations**, donc chaînables.
- LFO : modes chaos **Lorenz** et **Rossler**, mode **Path** (vectoriel sur grille XY), rate **jusqu'à 1000 Hz**, suivi du swing, phase modulable.
- Enveloppes : option **BPM** et **Legato Inverted** (libellé du menu, manuel p. 185) (déclenchement forcé à chaque note-on même en legato).
- **Mixer** en page dédiée : en Serum 1 le routage était implicite, il devient explicite et adressable.
- **Granular** jusqu'à **256 grains**. **Spectral** avec import d'images PNG comme source `[MAG]`.
- **Multisample** avec chargement de fichiers **SFZ**.

---

# F. AVIS DE LA PRESSE

`[MAG]` **MusicRadar** retient comme réellement nouveau l'**aux source avec courbe éditable** et le fait que **filtres et oscillateurs deviennent sources de modulation**. Il juge que la personnalité de Serum 2 vient de la **profondeur des outils de façonnage de sample**, donc une évolution de fond et non cosmétique. Réserves : interface par endroits « un peu à l'étroit », **absence de vrais oscillateurs virtual analog**.

`[MAG]` **MusicTech**, note de **8 sur 10** : « toujours pertinent mais plus révolutionnaire ». Reproches : **« plus gourmand en CPU que jamais »**, avec une recommandation de **16 Go de RAM minimum, le quadruple de la configuration annoncée** ; mode **Multisample jugé « un peu gadget »**.

---

# G. À TESTER, par ordre de rendement `[I]`

1. **Construire une configuration Configure de référence et l'enregistrer en « Default Configuration ».** Rend l'index API stable et reproductible. Gain immédiat, aucun risque.
2. **Clic droit → Automate** sur les paramètres FX visés, puis bypass et unbypass, puis Configure.
3. **`-_PluginAutoPopulateThreshold=128` dans Options.txt.** Cinq minutes, et ça tranche définitivement la question VST3 contre VST2 dans Live 12. Si ça marche, plus jamais besoin de cliquer dans Configure.
4. **Verrouiller Quality**, fixer **S1 Compatibility** explicitement dans tous les patchs, et **noter la version exacte de Serum 2** dans la mémoire de projet.

## Format à privilégier `[I]`

Sur macOS dans Live, **le VST3** semble préférable : c'est le format que le développement traite en premier, avec des préférences dédiées et des contournements. Les corrections Audio Unit arrivent plus tard. **Mais aucune source ne recommande explicitement l'un ou l'autre** — c'est une appréciation, pas une doctrine.

Les bugs des deux formats sont **distincts, pas équivalents**. Côté AU : messages d'aftertouch, CC et pitch bend non transmis à la sortie (corrigé en 2.0.19), crash intermittent (2.0.23). Côté VST3 : identifiants de notes incorrects sur certains hôtes, avec une préférence **« Ignore VST3 Note IDs »** ajoutée en 2.0.24.

---

# H. Un signalement isolé, à traiter avec prudence

`[FORUM, 1 seul utilisateur, aucune confirmation, aucune réponse Xfer]` Un fil intitulé « Serum 2 Automation and mapping bugs renders Serum 2 useless » décrit deux symptômes sur Live 11 sous Windows : supprimer des points dans l'affichage LFO **efface des macros**, et choisir un paramètre à automatiser **remplace aléatoirement une automation déjà assignée** par un paramètre sans rapport, **notamment « Device On »**.

**À traiter comme un signalement isolé.** Mais il est troublant qu'il mentionne précisément « Device On ».

---

# I. Lacune assumée

Le changelog officiel des versions **2.1.x** est derrière le compte Xfer et n'a pas pu être lu. Le changelog public s'arrête à la **2.0.24 du 13 novembre 2025**. Tout ce qui concerne la 2.1.x vient de résumés de forum, dont : les 2.1.0 et 2.1.1 corrigeraient l'assignation de paramètres d'automation dans Logic et **l'automation AU dans Ableton Live**, et la 2.1.5 ajouterait la préférence « restore locks when host sets state ».
