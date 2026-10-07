# Projet : Bass House en sol majeur, 126 BPM (titre provisoire « BH 126 G »)

**REPRISE (7 oct. 2026, session cloud, rien d'écrit dans Live)** : brief rédigé d'après les recommandations validées par l'utilisateur (« ok pour tes recommandations »). Aucun Set créé, aucun son écouté.
Non confirmé : critères tirés des références (l'utilisateur n'a pas détaillé ce qu'il aime dans chacune) ; tonalité de « Rhyme Dust » (sol majeur selon le corpus, à vérifier à l'oreille) ; placement des émotions en mesures ; nom définitif.
En attente : écoute des trois références et retour de l'utilisateur ; confirmation de la progression A ; réponse « chop vocal court : oui » à reconfirmer au moment du montage.
Prochaines étapes : 1) valider cette fiche ; 2) sur le Mac : `cd ~/tsila && git pull`, Claude Code dans `~/tsila`, `reprise.sh bass-house-sol-majeur`, `lom.py ping` puis `lom.py state --json`, Seagate branché, rescan des plug-ins après le déplacement des AU, version de Maschine et du routage à relire ; 3) nouveau Set sauvé sous un nouveau nom, 126 BPM, sol majeur, repères ; 4) harmonie : progression A, voicings et stabs ; 5) groove : trois patterns de densités différentes dans Maschine, choisis à l'écoute ; 6) kick Serum 2, sub, basse médium, accordés sur G ; 7) arrangement Original puis Extended ; 8) mix et exports séparés. Une étape par échange.

## Consignes permanentes
- **Répartition du travail (décision du 7 oct. 2026)** : tout ce qui touche Ableton Live se fait dans le **Terminal du Mac avec Claude Code** (Producer Pal, `lom.py`, contrôle d'écran). La session cloud prépare le brief, la théorie, les grilles MIDI (`grille.py`) et les recettes, sans accès à Live.
- **Synthés : tous dans Serum 2** (décision du 7 oct. 2026) : kick, sub, basse médium, stabs, lead, pad, textures, impacts ; une instance par rôle. Pas d'autre synthé pour ces rôles.
- Une étape par échange ; Set sauvé avant et après chaque étape ; état relu avant d'agir ; règle anti hot-swap (ne jamais remplacer un instrument sans le dire).
- C3 = 60 ; le numéro MIDI fait foi.
- Jamais « entendu » sans l'écoute de l'utilisateur : distinguer réglé, relu, mesuré, proposé.
- Grave : sub et basse médium dans **deux instruments séparés** ; sub mono.
- Signature de kick sous 124 BPM : **non applicable** à 126 BPM ; kick incisif conçu dans Serum 2.
- Drops : variation audible de batterie ou de transition avant chaque frontière de 8 mesures (fill, retrait de kick, roulement, reverse, impact, silence), gestes alternés.
- Deux versions, **Original Mix** et **Extended Mix**, issues du même noyau, vérifiées et exportées séparément.
- Pas de nouvel effet natif de Live dans les chaînes de mix ; traitements par plug-ins tiers (VST3).
- Références : critères seulement ; aucune mélodie, aucun enregistrement copiés ; aucun audio de référence dans un export sans droits.

## Cadre
| Élément | Choix |
|---|---|
| Style | Bass House, sol majeur (tonalité claire et festive ; le genre est surtout en mineur) |
| BPM | 126 (1 mesure = 1,905 s) |
| Label | VIBRAAXIS (ou VIBRAMOTIVE si l'utilisateur vise le label principal, à confirmer) |
| Usage | club et DJ |
| Vedette | la basse du drop et un hook de stabs ; chop vocal court optionnel |
| À éviter | cuivres par défaut, pads trop larges qui perdent la mono, réverbe sur le kick |

## Références (à écouter par l'utilisateur ; non écoutées par Claude)
| Rôle | Titre | Tonalité · BPM (corpus, bases automatiques) | À retenir |
|---|---|---|---|
| Basse et structure | Jauz & Ephwurd, « Rock The Party » (2015) | sol mineur · 128 | basse = hook, drop centré sur la basse, 3:56 ; même tonique G |
| Couleur harmonique | MK & Dom Dolla, « Rhyme Dust » (2023) | sol majeur · 128 | **à vérifier à l'oreille** : si c'est mi mineur, ne garder que le groove |
| Groove et chop | Chris Lake, « Turn Off The Lights » (2018) | si mineur · 125 | groove basse et percussions, arrangement par drop-outs, chop vocal en ostinato |

Critères à remplir après écoute : groove, timbres, structure, mix, énergie (une ligne par référence).

## Émotions (une dominante)
Ambiance générale : festive, claire, énergique. **Euphorie festive (dominante)** ; espièglerie groovy ; tension dans les builds. Placement en mesures : tableaux ci-dessous, à ajuster à l'étape `composer-trajectoire-emotionnelle`.

## Harmonie : sol majeur, progression A (G – D – Em – C)
Gamme G A B C D E F#. Voicings (script `theorie.py`, C3 = 60) :
| Accord | Degré | Notes | MIDI |
|---|---|---|---|
| G | I | G3 B3 D4 | 67, 71, 74 |
| D (1er renv.) | V | F#3 A3 D4 | 66, 69, 74 |
| Em | vi | G3 B3 E4 | 67, 71, 76 |
| C (2e renv.) | IV | G3 C4 E4 | 67, 72, 76 |

Grave : sub sur G0 = MIDI 31 (49,0 Hz), basse médium sur G1 = MIDI 43 (98,0 Hz). Drop : basse monotonale sur G, la progression vit dans les stabs, l'intro et le break. Fondamentales si la basse suit les accords : D1 = 38 (73,4 Hz), E1 = 40 (82,4 Hz), C1 = 36 (65,4 Hz) ; D0 (MIDI 26, 36,7 Hz) est trop grave pour le sub. Accord du kick sur la tonique ou la quinte : à décider avec `kick-bass-equilibre`.

## Rôles des outils
| Élément | Où | Sortie | Perform FX |
|---|---|---|---|
| Kick | Serum 2, piste Live (sidechain, mono) ; **jamais aussi dans Maschine** | piste Live | non |
| Sub | Serum 2, piste Live, sinus mono routé Direct | piste Live | non |
| Basse médium | Serum 2, piste Live séparée ; famille choisie à l'étape basse (organ bass, hollow FM, donk métallique, pluck rond) | piste Live | non |
| Stabs | Serum 2 (organ, disco, vowel « wah », ou recette piano M1 de Serum 2), choix à l'étape harmonie | piste Live | non |
| Lead, pad, textures, impacts | Serum 2, une instance par rôle, au besoin | piste Live | non |
| Hats, clap, percussions | Maschine, jeu de l'utilisateur aux pads | sorties individuelles (Ext. 2 à 16) vers `AUDIO - <son>` puis `BUS - PERCUSSIONS` | non |
| Chop vocal court | Maschine (sampling) | sortie individuelle | non |
| Fills et transitions | Maschine | par le Master, **performance imprimée** en audio, prise dry gardée | oui |

Serum 2 dans Live : seuls les paramètres « configurés » (Configure, 128 au maximum) sont pilotables par Producer Pal ou `lom.py` ; les macros sont visibles sans Configure. À prévoir pour chaque instance : nommer 3 ou 4 macros par rôle, puis configurer les paramètres à automatiser. Les réglages internes (oscillateurs, filtre, enveloppes) se font dans la fenêtre du plug-in, par clics, avec capture après chaque geste.

Règles Maschine : une sortie externe directe contourne le Perform FX du Master ; ne jamais additionner le retour Master et la sortie externe du même signal ; gestes matériels faits par l'utilisateur ; chemin vérifié par niveaux relatifs et capture d'écran. Groove sans humanisation aléatoire : vélocités en motif répété, trois patterns de 4 à 8 mesures de densités différentes, choisis à l'écoute (swing éventuel sur basse, hats et percussions, jamais sur le kick, à décider à l'étape groove).

## Structure proposée (126 BPM, à valider)
**Original Mix, 112 mesures ≈ 3:33**
| Section | Mesures | Émotion |
|---|---|---|
| Intro | 1–16 | espièglerie |
| Build 1 | 17–24 | tension |
| Drop 1 | 25–40 | euphorie |
| Breakdown | 41–56 | espièglerie, chaleur (hook de stabs, chop) |
| Build 2 | 57–64 | tension |
| Drop 2 (varié) | 65–88 | euphorie |
| Outro DJ | 89–112 | espièglerie |

**Extended Mix, 192 mesures ≈ 6:06** : intro DJ 1–32 · build 1 33–40 · drop 1 41–56 · breakdown 57–72 · build 2 73–80 · drop 2 81–104 · pont 105–112 · build 3 113–120 · drop 3 121–160 · outro DJ 161–192. Même noyau que l'Original ; intro et outro plus longues sans affaiblir la version courte.

Variation de batterie ou de transition avant les frontières de 8 mesures des drops (mes. 32 et 40, 72, 80 et 88 pour l'Original ; à recalculer pour l'Extended).

## Environnement (état du 7 oct. 2026)
- 53 composants AU mis de côté sur le Seagate (`AU-mis-de-cote-2026-10-07`, commande de retour affichée par le script) ; les versions VST3 restent installées (bx_glue, TDR Nova, Battery 4, etc.). À contrôler : ouvrir un Set récent et vérifier qu'aucun device n'est grisé.
- Bibliothèques NI, Ableton et Waves sur le Seagate (`native instruments/shared`, `ableton `, `waves`) : le disque doit être branché pendant la production. Ne pas les déplacer ni les renommer.
- Disque interne : 46 Go libres ; Set de production sur le disque interne, archivage sur le Seagate ensuite.
- Maschine 3.6.0 (VST3/AU repérés le 14 sept. 2026) : version et routage à relire dans la session réelle.

## Journal
- 7 oct. 2026 : brief proposé (Afro House 122 BPM) puis remplacé à la demande de l'utilisateur par un **Bass House en sol majeur** ; Afro House mis de côté.
- 7 oct. 2026 : l'utilisateur a validé **« ok pour tes recommandations »** : références (Rock The Party, Rhyme Dust à vérifier, Turn Off The Lights), BPM 126, progression A, chop vocal court, émotions, rôle de Maschine. Fiche rédigée (cloud, rien d'écrit dans Live). Reste : écoute des références, retour de l'utilisateur, montage sur le Mac.
- 7 oct. 2026 : l'utilisateur a décidé que **le Terminal avec Claude Code reste l'outil pour Ableton**, et que **tous les synthés sont dans Serum 2**. Fiche mise à jour (consignes permanentes et rôles des outils).
