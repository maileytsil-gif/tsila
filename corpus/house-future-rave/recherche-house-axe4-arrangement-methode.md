---
titre: "Rapport de recherche — axe 4 : Recherche — AXE 4 : Arrangement et méthode de production professionnelle (future rave, bass house, house de festival/club)"
source: recherche web et GitHub, session Claude Code du 2026-09-24 (agent de recherche)
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: arrangement et méthode de production (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: synthèse interne avec étiquettes de preuve ; les sources primaires sont citées dans le texte
---

# Recherche — AXE 4 : Arrangement et méthode de production professionnelle (future rave, bass house, house de festival/club)

Date : 2026-09-24. Pour le skill `house-future-rave-bass-house-production` (Ableton Live 12). Rédigé en français.

## 0. Méthode et légende

- **[DOC]** : donnée primaire lue en entier et vérifiable (dataset Harmonix Set, readme SALAMI, fichiers du dépôt).
- **[DOC-EXTRAIT]** : résumé de recherche web (page non téléchargeable depuis le conteneur, EGRESS_BLOCKED) ; la page est listée dans `urls-axe4.json` pour lecture complète sur le Mac.
- **[DOC-lu]** : document GitHub communautaire lu en entier et archivé dans `corpus/house-future-rave/` ; notes d'auteurs non sourcées, à recouper.
- **[HEUR]** : synthèse ou règle pratique déduite, pas de source unique.
- **[NON VÉRIFIÉ]** : minutage ou chiffre qu'aucune source lue ne confirme ; ne pas le présenter comme un fait.
- Recherches web : 15 (quota épuisé). Téléchargements : raw.githubusercontent.com (curl) + pages github.com (WebFetch, listings). Datasets de structures testés : Harmonix Set (exploité), SALAMI (readme + metadata seulement : pas de titre dance/EDM utile).
- Conversion mesures ↔ secondes (4/4) : `s = mesures × 240 / BPM`. À 128 BPM : 1 mesure = 1,875 s ; 8 = 15 s ; 16 = 30 s ; 32 = 60 s. À 126 : 16 mesures = 30,5 s ; à 130 : 16 mesures = 29,5 s.

## 1. Ce que le dépôt contient déjà (à citer, pas à répéter)

| Fichier | Ce qu'il apporte à l'axe 4 | Compléter par |
|---|---|---|
| `.claude/skills/theorie-musicale-electronique/references/forme-tension.md` | §2 unités (8/16/32, DJ-friendly 16–32, premier élément mélodique pas avant m.17/33) ; §3 schéma « house/techno ≈ 7 min » et « EDM 128 » (intro 16 · groove 16 · break 8 · build 8 · drop 32 · breakdown 16 · drop final 32 · outro 16) ; §4 tableau des dispositifs (riser, snare roll, filtre, coupure, reverse, densification, harmonie, Shepard, première mesure du drop, variation) ; §5 second drop, layering ; §6 forme et harmonie | Ce rapport ajoute les versions radio chiffrées, les analyses Harmonix, la grille section × élément, la méthode de travail et les livrables |
| `.claude/skills/arrangement-avance/SKILL.md` | `arrangement_map.py`, repères (`lom.py locator`), densité (un élément entre/sort toutes les 4–8 mesures), Insérer Silence / Supprimer Zone temporelle, copie de sections, drops « presque statiques », outro | Gestion des versions (§4.6) s'appuie dessus |
| `.claude/skills/ableton-live-session/SKILL.md` | Méthode en 8 étapes de l'utilisateur : 1 cadre (Sauver sous, tempo/tonalité, **structure avec repères et durée exacte**), 2 instruments, 3 **passage central de 8 mesures**, 4 **arrangement complet**, 5 mix, 6 automations, 7 voix, 8 export ; une étape par échange ; natifs tolérés | La méthode pro (§4) est mise en correspondance avec ces 8 étapes, elle ne les remplace pas |
| `corpus/cuivres/amen-sessions-01-house.md` | Arrangement house « additif puis soustractif » 128–160 mesures ≈ 6 min à 124 (drums 0–15, +bass 16, +chords 32, +vocal 48, breakdown 64, build 80, main 96–127, outro) ; « une couche de percussion toutes les 16 mesures » | Contradiction avec la house de festival, voir §6 |
| `corpus/cuivres/amen-sessions-09-edm-and-future-bass.md` | « Universal EDM arrangement » 160 mesures (intro 16 · verse 16 · build 16 · silence 2 · drop 32 · breakdown 16 · build 16 · drop 2 32 · outro 16), **3:00–3:30, intro 4–8 mesures, premier drop possible sous 45 s** ; recette de build en tableau ; « le drop est souvent plus vide que le build » | Repris tel quel ; les fiches amen d'arrangement (form, drop, transitions, templates) sont maintenant archivées |
| `corpus/funk-claviers/amen-16-mixing-process.md` | Ordre de travail du mix, gain staging, automation, référence à niveau égal | §4.2 (mix après arrangement) |
| `corpus/constructeur/live12-manuel-06-arrangement-view.md` | Manuel Live 12, vue Arrangement (repères, boucle, insertion de silence, consolidation) | §4.6 |
| Écrits par les autres agents pendant cette recherche : `corpus/house-future-rave/jefrob-house-arrangements.md` (structures par sous-genre, en mesures et minutes), `bitwize-genre-*-readme.md`, `edm-midi-studio-genres-future-rave-extrait.md` | Voir §2.1 et §2.2 | |

## 2. Structures types par genre

### 2.1 Versions club / DJ (extended)

Toutes les sources lues convergent sur des blocs de 8/16/32 mesures et sur une intro/outro « mixables » (kick + percussions, peu de médiums, pas de mélodie) ; elles divergent sur les longueurs (voir §6). Les grilles ci-dessous sont des **synthèses [HEUR]** appuyées sur les sources citées dans chaque ligne ; les minutes sont calculées, pas mesurées sur des disques.

| Genre (BPM) | Grille club (mesures) | Total | Durée calc. | Sources |
|---|---|---|---|---|
| **Future rave** (126–128) | intro 32 · break 1 (thème filtré, accords) 16 · build 16 · **drop 1** 32 · breakdown 32 (pad, vocal, lead exposé) · build 16 · **drop 2** 32 (+1 couche) · outro 32 | 208 | 6:30 à 128 | Calque du « club track two drops » amen (192 mes., ~6:00) [DOC-lu] + définition future rave (energie EDM, sons techno, émotion trance) [DOC-EXTRAIT weraveyou] ; aucun titre Guetta & MORTEN minuté par une source lue → **[NON VÉRIFIÉ]** pour les longueurs propres au genre |
| **Bass house** (126–128) | intro 16 · intro B 16 · build 16 · **drop 1** 32 · breakdown 16 · build 16 · **drop 2** 32 · outro 16 | 160 | 5:00 à 128 | Fearvox « full track map » 160 mes. [DOC-lu] ; jefrob « Extended Roller » (intro 16 · build 16 · drop 32 · groove 32 · build 8 · drop 32 · outro 16) et « Wobble Standard » (intro 8–16 · build 8–16 · drop 16–32 · breakdown 8–16 · build 8 · drop 16–32 · outro 8–16) [DOC-lu] ; bitwize : « intro 16–32, build, drop 16–32, breakdown, second build, second drop varié, outro ; 4–6 min » [DOC-lu] ; EDMProd : composer d'abord le drop puis dépouiller [DOC-EXTRAIT] |
| **Tech house** (125–127) | intro 16–32 · loop A 32 · build 8 · **drop A** 32 · break 8–16 · **drop B** 32–64 · outro 16–32 | 160–208 | 5:00–6:30 à 126 | jefrob « Functional DJ Tool » [DOC-lu] ; EDMProd (Fisher) : « breakdown + build = 8 mesures » [DOC-EXTRAIT] ; bitwize : intros/outros DJ 32–64 mes., 5–8 min, tension sur phrases de 16–32 [DOC-lu] |
| **Future house** (124–128) | intro 16 · build 16 · **drop 1** 32 · breakdown 16 · build 16 · **drop 2** 32 · outro 16 | 144 | 4:30 à 128 | bitwize : « arrangement EDM standard, 3–5 min, intros/outros DJ » [DOC-lu] ; Heldens « Koala » original 4:24 / radio 2:48 [DOC-EXTRAIT Wikipedia] |
| **Big room / festival** (128–130) | intro 8–16 · thème/hook 16 · build 16 · **drop A** 32 · breakdown 16 · build 16 · **drop B** 32 · outro 8–16 | 144–160 | 4:30–5:00 à 128 | jefrob « Festival Anthem » et « Big Room Standard » [DOC-lu] ; forme-tension §3 « EDM 128 » [DOC] ; Garrix « Animals » original 5:04 / radio 2:57 [DOC-EXTRAIT Wikipedia] |
| **House classique** (122–126) | drums 16 · +bass 16 · +chords 16 · +vocal 16 · breakdown 16 · build 16 · main 64 · reduced 24 · outro 16 | 200 | 6:27 à 124 | amen house template [DOC-lu] : additif/soustractif, pas de drop |

Règles transversales tirées des sources : chaque frontière de section sur un multiple de 8 depuis la mesure 1 (idéalement 16) [DOC-lu amen] ; intro et outro « sans contenu plein-spectre » pour laisser la place à l'autre disque [DOC-lu amen] ; le sommet du morceau entre 60 et 75 % de la durée [DOC-lu amen] ; le point le plus bas juste avant le plus haut [DOC-lu amen].

### 2.2 Versions radio / streaming (2:30–3:30)

| Élément | Chiffre | Source |
|---|---|---|
| Durée | ~3 min pour la radio ; 2:30–3:20 pop moderne ; 3:00–3:30 EDM streaming | Wikipedia Radio edit [DOC-EXTRAIT] ; amen 11 [DOC-lu] ; amen 09 [DOC-lu, déjà au dépôt] |
| Ce qu'on coupe | intro/outro DJ supprimés ou divisés par deux, build initial retiré | Wikipedia Radio edit [DOC-EXTRAIT] ; djcity [DOC-EXTRAIT] |
| Premier refrain / drop | pop : refrain avant 0:50 ; EDM streaming : premier drop possible avant 45 s, intro 4–8 mesures | amen 11 et 09 [DOC-lu] |
| Pourquoi | le streaming récompense les titres courts (2:30 joué deux fois > 4:00 joué une fois) mais pénalise un démarrage lent | majormixing [DOC-EXTRAIT] |
| Grille radio type (128 BPM) | intro 4–8 (7–15 s) · verse/thème 16 (30 s) · build 8 (15 s) · **drop 1** 16–32 (m.29–37, soit 0:52–1:08) · break 16 · build 8 · **drop 2** 32 · outro 4 → 104–112 mes. ≈ 3:15–3:30 | amen EDM festival template 108 mes. ≈ 3:20 [DOC-lu] ; pour un drop **avant 45 s** : intro 4 + thème 8 + build 8 = 20 mes. = 37,5 s [HEUR] |
| Bass house festival | intro 8 · build 16 · drop A 16–32 · mini-break 4–8 · drop B 16–32 · outro 8 → 3–4 min | jefrob « Festival Bass » [DOC-lu] |

### 2.3 Analyses minutées de titres réels

**Ce qui est vérifié [DOC] — Harmonix Set** (annotations humaines de sections, 912 titres ; 31 titres dance/EDM extraits et convertis en mesures ; fichier `corpus/house-future-rave/harmonixset-segments-dance-edm.md`). Vocabulaire des annotateurs : `chorus` = refrain chanté ; `inst` = section instrumentale, c'est-à-dire **le drop** dans un titre EDM-pop ; `prechorus` = souvent le build ; `postchorus`. Les numéros de mesure viennent du fichier beats/downbeats (±1 mesure quand la frontière tombe sur le temps 3 ou 4).

David Guetta (le seul des producteurs de référence présent dans le dataset ; période 2007–2012, avant la future rave) :

| Titre (BPM, durée) | Sections (mesure de départ · mm:ss · longueur) | Ce qu'on en apprend |
|---|---|---|
| **Titanium** feat. Sia (126, 3:31) [DOC] | intro m1 0:00 (4) · verse m5 0:08 (16) · chorus m21 0:38 (16) · **inst/drop m37 1:09 (8)** · verse m45 1:24 (16) · chorus m61 1:54 (16) · **inst m77 2:25 (8)** · bridge m85 2:40 (8) · chorus m93 2:55 (8) · **inst m101 3:10 (8)** · fin m109 | Formule Guetta pop-EDM : refrain chanté 16 → drop instrumental **8 mesures seulement** ; trois drops ; intro 4 mesures ; tout sur des multiples de 8 ; 108 mesures |
| **Memories** feat. Kid Cudi, radio (130, 3:28) [DOC] | intro m1 (8) · **chorus m9 0:15 (16)** · verse m25 0:44 (16) · break m41 1:14 (8) · chorus m49 1:29 (16) · verse m65 1:58 (16) · bridge m81 2:28 (16) · verse m97 2:57 (16) · fin m113 | Hook à 15 s (« cold open sur le hook ») ; break de 8 avant le second refrain |
| **Memories** extended (127, 4:39) [DOC] | intro m1 0:00 (**20**) · chorus m21 0:38 (16) · postchorus m37 1:08 (16) · break m53 1:38 (8) · chorus m61 1:53 (16) · postchorus m77 2:23 (16) · bridge m93 2:53 (16) · postchorus m109 3:23 (16) · inst m125 3:53 (**24**) · fin m149 | Radio → extended : intro 8 → 20, ajout d'un « postchorus » (drop instrumental) de 16 après chaque refrain, outro instrumental de 24 ; les blocs internes de 16 ne changent pas |
| **Sexy Chick** radio (130, 2:41) vs version Akon (130, 3:13) [DOC] | radio : intro 4 · verse 16 · prechorus 16 · **chorus 8** · verse 16 · prechorus 16 · chorus 8 · fin m85 ; Akon : **intro 24** (0:44) · chorus 16 · chorus2 16 · verse 16 · chorus 16 · chorus2 16 · fin m105 | Deux montages du même titre : la version longue ouvre par 24 mesures d'intro et double le refrain |
| **Gettin' Over You** radio (130, 3:05) vs remix Sidney Samson (130, 5:18) [DOC] | radio : intro 2 · chorus m3 0:04 (18) · verse 18 · prechorus 8 · chorus 16 · prechorus 10 · bridge 19 · prechorus 8 · fin m100 ; remix : **intro 16** · chorus m17 0:30 (20) · inst 16 · postchorus 16 · chorus 16 · inst 16 · bridge 16 · inst 24 · **outro 32** (4:19–5:18) · fin m173 | Version club : intro 16, outro 32 (une minute), un drop instrumental (`inst`) après chaque refrain |
| **When Love Takes Over** (130, 3:05) [DOC] | intro 4 · verse 8 · verse2 8 · chorus m21 0:37 (8) · verse3 8 · verse4 8 · chorus m45 1:21 (8) · break m53 1:36 (8) · bridge 8 · outro m69 2:06 (24) · outro2 8 · fin m101 | Tout en blocs de 8 ; refrain à 37 s |
| **Without You** feat. Usher (128, 3:27) [DOC] | intro 8 · verse 16 · verse 16 · chorus m41 1:15 (14) · verse 16 · verse 16 · chorus m87 2:41 (14) · verse 8 · fin m109 | Refrain tardif (1:15) : exception à la règle des 45 s |
| **Everytime We Touch** (129, 4:50) [DOC] | intro 8 · chorus m9 0:15 (16) · verse 16 · chorus 16 · inst m57 1:44 (16) · verse 16 · chorus 16 · inst m105 3:14 (16) · breakdown m121 3:43 (8) · inst m129 3:58 (16) · outro m145 4:28 (12) · fin m157 | Version club de 156 mesures : drops instrumentaux de 16, breakdown de 8 avant le dernier drop |
| **Love Is Gone** extended (128, 5:56) [DOC] | intro 4 · verse 16 · verse 16 · stutter 8 · inst m45 1:22 (28) · break 4 · inst 18 · inst 16 · intro m111 3:26 (4) · verse 16 · verse 16 · stutter 8 · inst 8 · bridge 8 · breakdown m171 5:18 (20) · fin m191 | Forme « deux fois le même morceau » (la seconde moitié rejoue intro-verse-verse-stutter) : montage de remix extended typique 2007 |

Autres titres [DOC] utiles comme références de forme :

| Titre | Sections | Leçon |
|---|---|---|
| Swedish House Mafia **Don't You Worry Child** (130, 3:30) | intro 3 · verse 17 · prechorus m21 0:37 (8) · **chorus m29 0:52 (8)** · inst m37 1:07 (8) · chorus 9 · verse 17 · prechorus 8 · chorus m79 2:25 (8) · bridge 8 · chorus m95 2:55 (8) · outro 8 · fin m111 | Refrain chanté 8 + drop instrumental 8 : la paire « chorus/inst » de 16 mesures est la cellule de la house de festival vocale |
| SHM **Save the World** radio (128, 3:25) | intro 4 · verse 8 · prechorus 8 · chorus m21 0:37 (16) · inst 8 · postchorus 9 · verse 8 · prechorus 8 · chorus m70 2:09 (16) · postchorus 8 · chorus m94 2:54 (16) · fin m110 | Trois refrains, le dernier sans retour de couplet |
| Calvin Harris **Feel So Close** radio (128, 3:22) vs extended (4:30) | radio : **verse m1** (16, pas d'intro) · prechorus 8 · chorus m25 0:45 (16) · verse 16 · chorus 16 · bridge 16 · chorus 16 · outro 3 ; extended : intro 8 · chorus m9 0:15 (16) · guitar 8 · inst 16 · chorus 16 · inst 16 · breakdown m81 2:30 (16) · inst 16 · **outro m113 3:30 (32)** | Le radio edit commence directement sur le couplet ; l'extended ouvre sur le hook après 8 mesures et finit par 32 mesures d'outro |
| Afrojack **Take Over Control** radio (130, 2:43) vs extended (6:12) | radio : intro 4 · chorus m5 0:07 (8) · verse 16 · prechorus 8 · chorus 8 · inst 16 · chorus 8 · chorus 8 · outro 8 · fin m85 ; extended : **intro 16** · verse 16 · verse 16 · chorus m49 1:29 (16) · section 15 · chorus2 9 · chorus 8 · verse 16 · chorus 16 · transition 8 · section 16 · **outro 15+17+16 = 48** (4:41–6:09) | Radio 84 mesures / extended 200 : la différence est presque toute dans intro (4 → 16) et outro (8 → 48) |
| Avicii **My Feelings for You** (128, 5:10) | intro 6 · chorus m7 0:11 (8) · verse 10 · chorus 8 · chorus 8 · inst 4 · chorus 12 · chorus 16 · altchorus 8 · break 8 · chorus 8 · chorus 8 · postchorus 8+8+8 · instchorus 8 · breakdown m137 4:15 (16) · saxobeat 13 · fin m166 | Progressive house : blocs de 8, hook répété, breakdown tardif |
| deadmau5 **Sofi Needs a Ladder** (128, 6:01) | intro 17 · **10 sections de 16** (m18 → m178) · outro 15 · fin m193 | Architecture club pure : 192 mesures, un événement toutes les 16 |
| Daft Punk **Around the World** (121, 2:35) | intro 8 · chorus 16 · inst 4 · chorus 8 · inst 8 · chorus 20 · inst 4 · chorus 8 · fin m77 | Edit radio de french house : alternance hook/instrumental sur 4, 8, 16 |

**Ce qui n'est PAS vérifié pour les artistes demandés.** Aucune source lue ne donne les sections minutées d'un titre de Guetta & MORTEN (future rave), Jauz, Chris Lake, Malaa, Dom Dolla, Fisher, Tchami, Oliver Heldens ou Martin Garrix (hors durées). Faits disponibles :

| Titre | Fait sourcé | Statut |
|---|---|---|
| Fisher — Losing It (2018) | durée 4:08 [DOC-EXTRAIT Wikipedia] ; « les hats restent constants dans toutes les parties mais sont coupés pendant tous les builds ; les claps jouent un motif de 2 mesures, sur le 2e temps de chaque mesure » [DOC-EXTRAIT topmusicarts] | sections/minutage **[NON VÉRIFIÉ]** |
| Martin Garrix — Animals (2013) | original 5:04, radio edit 2:57 [DOC-EXTRAIT Wikipedia] ; analyse « Anatomy of a hit » MusicRadar à lire sur le Mac | sections **[NON VÉRIFIÉ]** |
| Oliver Heldens — Koala | original 4:24, radio 2:48 [DOC-EXTRAIT Wikipedia] | **[NON VÉRIFIÉ]** |
| Guetta & MORTEN — Never Be Alone, Save My Life, Lost in the Rhythm, LUCKY | existence, dates, description sonore (« pitched-up techno synths, vocals placés, bass downbeats ») [DOC-EXTRAIT edm.com/dancingastronaut] | aucun minutage **[NON VÉRIFIÉ]** |
| Jauz — Feel the Volume (2014), Rock the Party (2015, avec Ephwurd) | rôle historique (a fait passer la bass house en festival) [DOC-lu bitwize] | **[NON VÉRIFIÉ]** |
| Dom Dolla — Girls, Saving Up, San Frandisco | pages Wikipedia listées, non lues | **[NON VÉRIFIÉ]** |

Procédure pour obtenir ces minutages sans les inventer (à faire sur le Mac, avec l'utilisateur) [HEUR] : importer l'audio de référence dans une piste `REF` (déjà prévue par `ableton-live-session` : « REF → Main »), warp sur le BPM annoncé, poser un repère à chaque changement (`lom.py locator <t> "<nom>"`), puis `arrangement_map.py` : la carte donne les longueurs exactes en mesures. Sounds of Ibiza décrit la même méthode (compter les mesures de chaque section d'une référence au même tempo, noter tous les 8 mesures quels éléments jouent) [DOC-EXTRAIT].

## 3. Dispositifs

### 3.1 Build-up

| Dispositif | Recette sourcée | Source |
|---|---|---|
| Longueur | big room 16 mes. ; house 8–16 « gentle » ; trap 4–8 ; « 8 normal, 16 pour le drop principal, 4 pour un reset rapide » | amen 02 [DOC-lu] ; R2S : builds 8 mes. dans un squelette 16/16/8/16 [DOC-lu] ; Fearvox : 16 mes. (build 2 plus court : 8) [DOC-lu] |
| Empiler ≥ 4 dimensions | densité rythmique (snare roll 1/8 ×4 mes. → 1/16 ×2 → 1/32 ×1 → 1/64 dernier temps), hauteur (riser bruit band-pass 200 Hz → 8 kHz ; ou ligne d'une octave), volume, registre (**passe-haut du mix jusqu'à 400–800 Hz sur les 4 dernières mesures : la basse disparaît**), harmonie (V, bVI ou sus tenu), espace (reverb/delay qui montent puis coupés net), stéréo (rétrécir avant le drop), timbre (distorsion/filtre) ; « ne monter que le volume ne produit rien » | amen 02 [DOC-lu] ; déjà en partie dans forme-tension §4 |
| Hats accélérés | mes. 33–36 : 1/8 ; 37–40 : 1/16 ; 41–43 : 1/16 + doubles ; 44 : roll 1/32 → crash | Fearvox [DOC-lu] |
| Kick retiré | « strip-back build » : retirer le kick 4–8 mesures avant le drop, ne garder que basse filtrée + pads + riser | Fearvox [DOC-lu] ; forme-tension §4 (kick retiré en fin de phrase) |
| Vocal | vocal chops en appel-réponse dans les builds (bass house) ; fragment vocal seul dans le gap | bitwize bass house [DOC-lu] ; amen 02 [DOC-lu] |
| Accord suspendu | sus4 (ex. Asus4) sur les 2 derniers temps, résolu au drop | Fearvox [DOC-lu] |
| Le gap | « le dernier temps, demi-mesure ou mesure avant le drop doit être presque vide » : 1/16–1/8 = stutter ; **1 temps = standard** ; 2 temps = dramatique ; 1 mesure = très dramatique ; contenu possible : rien, queue de reverb, fragment vocal, sub-drop (sinus 80 → 25 Hz), downlifter, tape-stop ; « deux vrais silences par morceau, pas plus » | amen 02 et 18 [DOC-lu] ; forme-tension dit « deux temps de rien » — voir §6 |
| Premier temps du drop | impact (kick + bruit + reverb inversée) + crash + sub-drop + mix complet, tous sur le même échantillon | amen 02 [DOC-lu] ; forme-tension §4 « première mesure du drop » |

### 3.2 Drop

- **Couches et densité** : big room = kick + sub + un motif de lead, presque rien d'autre ; bass house = « la basse EST le lead », drop dépouillé à kick + basse ; future house = basse FM + vocal chops ; le drop est souvent **plus vide** que le build, le contraste vient du retour du grave et du timbre, pas de la densité [DOC-lu amen 02, bitwize, Fearvox]. Compte d'éléments simultanés : drop 6–10, jamais plus de ~10 [DOC-lu amen 11]. Lead de festival = 3–6 sons en unisson séparés par bande (sub / corps / air) [DOC-lu amen 09, déjà au dépôt].
- **Alternance toutes les 8 mesures** : structure interne « 2 mesures d'appel, 2 de réponse, ×4, escalade aux mesures 13–16 » ; « changer quelque chose toutes les 4 mesures » ; bass house : « une variation de 2 mesures toutes les 8 » (amen 09) ; Fearvox : `drop_var` à la mesure 8 du drop ; « la mesure 16 (ou 32) se termine par un fill ou une coupure » [DOC-lu amen 02 ; Fearvox]. Chris Lake/tech house : les hats coupés dans les builds et constants ailleurs [DOC-EXTRAIT topmusicarts, Fisher].
- **Drop 2** : doit dépasser le premier **sans être plus fort** : +1 élément, +1–2 demi-tons, lead à l'octave, autre pattern de batterie (halftime/doubletime), contre-mélodie, image plus large, vocal, plus long, ou un breakdown précédent plus petit et plus calme [DOC-lu amen 02] ; bass house : « nouveau lead, couche de percussion supplémentaire ou hook vocal » [DOC-lu Fearvox] ; « contrast must be timbral, not just in level » [DOC-lu amen 09].
- **Types alternatifs** : halftime drop, empty drop (sub + hat), false drop (résolution calme puis vrai drop 8 mesures plus tard), double drop, switch-up, vocal drop, build sans drop [DOC-lu amen 02]. Guetta pop-EDM : le drop instrumental fait **8 mesures** après un refrain chanté de 16 (Titanium, DYWC) [DOC Harmonix].
- **Échecs listés** : pas de gap → le drop ne tombe pas ; seul le volume monte → build plat ; build trop dense → drop plus petit que le build (amincir les médiums du build, grossir le grave du drop) ; drop ennuyeux après 8 mesures → changer toutes les 2–4 ; drop 2 identique → anticlimax ; tout à 10 → épuisant (baisser les autres sections de 6 dB+) [DOC-lu amen 02].

### 3.3 Breakdown

- Retirer la batterie (ou pulsation douce), exposer mélodie/vocal avec reverb, **nouvelle matière harmonique ou réharmonisation**, atmosphère, halftime ; **−6 à −10 LU par rapport au drop** ; 16–32 mesures en dance, 8–16 en pop ; « trop long perd la salle, trop court ne remet pas l'oreille à zéro » [DOC-lu amen 02/11]. Tech house : break de 8 (–16) seulement [DOC-lu jefrob ; DOC-EXTRAIT EDMProd]. Bass house : breakdown « fonctionnel » 8–16 [DOC-lu jefrob] ; Fearvox : pads seuls, pas de batterie, 16 mesures [DOC-lu].
- **Sidechain sur le pad** : « sidechain aussi les pads, pas seulement la basse : tout le morceau respire » [DOC-lu amen 01, déjà au dépôt] ; « everything is sidechained to the kick, this is the sound » [DOC-lu amen 09] ; en breakdown sans kick, garder le pompage par un kick fantôme (piste kick muette qui déclenche le sidechain) pour que le pad conserve le mouvement du drop [HEUR, pratique courante non sourcée ici]. Réglages « standard house pump » Fearvox : seuil −20 dB, 6:1, attaque 0,5–1 ms, release 150–200 ms ; « hard bass house pump » : 8:1–10:1, release 100–150 ms [DOC-lu].
- **Le breakdown est un événement de médiums** : ôter le sub et l'extrême aigu, leur retour est la récompense ; « on ne peut pas ouvrir une bande qu'on n'a jamais fermée » [DOC-lu amen 20].

### 3.4 Transitions

Inventaire amen 06 [DOC-lu] : riser 1–8 mes. · downlifter 1–2 mes. au **début** de la nouvelle section · impact/boom sur le temps 1 · sub-drop 1–2 temps · reverse cymbal 1–2 temps · reverse reverb · snare roll 1–4 mes. · filter sweep 4–32 mes. · silence 1–2 temps (« le plus fort ») · tape stop · vinyl rewind · beat repeat/stutter · drum drop-out 1 mes. · crash + kick · ad-lib vocal · delay throw · white noise swell · pitch bend du mix · gate/chop de la dernière mesure. **Transition composée type** : filtre 8 mes. + snare roll 4 + riser 2 + silence 1 temps + impact + crash + sub-drop + mix complet ; « 3 à 5 dispositifs par couture est normal ». Filtre à automatiser **sur un bus**, pas piste par piste (passe-haut 20 → 500 Hz sur 4–8 mes. pour le build, 500 → 20 Hz en 1 mesure au drop ; passe-bas qui se ferme sur 16 mes. pour l'outro). Pièges : riser à chaque transition (ils cessent d'agir), riser sans impact, queues de reverb qui bavent sur la première mesure du drop, riser plus fort que le drop, transitions hors grille, riser d'usine non égalisé (trop de 200–500 Hz). Checklist de couture : quelque chose part ET arrive ; marqueur sur le temps 1 ; dernier temps plus mince ; ≥ 2 dimensions changent ; multiple de 8 ; queue coupée ou assumée.

### 3.5 Tableau section × élément (bass house / future rave, version club 160 mesures à 128 BPM)

Synthèse [HEUR] à partir de la grille Fearvox (✅ / ♻️ / ❌) [DOC-lu], de la matrice amen [DOC-lu] et de la règle du dépôt « un élément entre ou sort toutes les 4–8 mesures » (`arrangement-avance`). Lecture verticale = densité ; horizontale = un élément toujours présent est « papier peint », un élément présent une seule fois est gaspillé. **Test de soustraction** : à chaque bloc de 8, au moins un élément du bloc précédent disparaît [DOC-lu amen 11].

| Élément | Intro A m1–16 (0:00) | Intro B m17–32 (0:30) | Build 1 m33–48 (1:00) | **Drop 1** m49–80 (1:30) | Breakdown m81–96 (2:30) | Build 2 m97–112 (3:00) | **Drop 2** m113–144 (3:30) | Outro m145–160 (4:30) |
|---|---|---|---|---|---|---|---|---|
| Kick | ✅ (filtré/lo-fi) | ✅ | ✅ puis ❌ 4–8 dernières mes. | ✅ | ❌ (ou pulsation) | ✅ puis ❌ | ✅ | ✅ → seul à la fin |
| Hats fermés / ouverts | ✅ 1/8 dès m1, open m9 | ✅ | accélération 1/8 → 1/16 → 1/32 | ✅ (constants) | ❌ | accélération | ✅ | ✅ puis ❌ |
| Clap / snare | ❌ | ♻️ m17 | ✅ + roll | ✅ | ❌ | ✅ + roll | ✅ | ✅ |
| Shaker / percs | ❌ | ♻️ m25 | ✅ | ✅ (+1 couche à m65) | ❌ | ✅ | ✅ (+1 couche) | ♻️ |
| Sub | ❌ | ❌ | ❌ (passe-haut) | ✅ mono | ❌ | ❌ | ✅ | ❌ |
| Basse mid (growl / FM / rave) | ❌ | ♻️ filtrée < 300 Hz (m17) | ♻️ | ✅ **le lead** ; variation 2 mes. toutes les 8 | ❌ | ♻️ | ✅ variante (motif, octave, nouveau patch) | ❌ |
| Accords / pad / stab | ❌ | ❌ | ♻️ filtré (m33) | ✅ | ✅ exposé, reverb, sidechain fantôme | ♻️ | ✅ | ❌ |
| Lead / hook mélodique | ❌ | ❌ | ❌ | ✅ (big room : 1 motif) | ♻️ mélodie seule | ❌ | ✅ + contre-mélodie ou +1 octave | ❌ |
| Vocal | ❌ | ❌ | ♻️ chops appel-réponse | ✅ hook | ♻️ chanté / chops | ♻️ | ✅ variante | ❌ |
| Riser / roll / FX | ❌ | ❌ (un downlifter à m17) | ✅ riser m33, roll m41–48, silence m48 t.4 | impact + crash m49 ; hit FX toutes les 16 | ♻️ ambiance | ✅ (plus court, 8 mes. possibles) | impact + crash m113 | ❌ |
| Filtre bus | ♻️ LP fermé qui s'ouvre sur 16 | LP ouvert | HP 20 → 500–800 Hz sur 4 mes. | HP → 20 Hz en 1 mes. | HP léger (pas de sub) | HP montant | plein spectre | LP qui se ferme sur 16 |
| Énergie 1–10 | 2–3 | 4 | 5 → 8 | 10 | 5 → 3 | 5 → 9 | 10 | 10 → 2 |

Courbe d'énergie chiffrée (autre source, R2S, en % sur un squelette intro 16 · verse 16 · build 8 · drop 16 · verse 2 16 · build 8 · drop 2 16 · outro 16) [DOC-lu] : intro 20–30 · verse 30–40 · build 40 → 90 · drop 100 → 85 · verse 2 35–50 (« un peu plus haut que verse 1 ») · build 2 50 → 95 · drop 2 100 · outro 50 → 0. À tracer **avant** d'écrire (amen 11 et forme-tension disent la même chose).

Grille spectrale par section (amen 20) [DOC-lu] : le sub (20–60 Hz) est **absent** en intro, build et breakdown, présent en drop ; 60–120 Hz absent en intro/build/breakdown ; 6–12 kHz et 12 k+ absents en intro/outro, présents en build (riser) et drop. « Donner à l'octave du haut un endroit où aller : si les hats sont à pleine brillance dès la mesure 1, le refrain n'a plus de montée disponible. »

## 4. Méthode de production professionnelle

### 4.1 Workflow (mise en correspondance avec les 8 étapes de `ableton-live-session`)

| Étape utilisateur | Ce que font les pros (sources) | Étiquette |
|---|---|---|
| 1 Cadre : Sauver sous, tempo, tonalité, **structure avec repères** | Référence : « pull up a reference in the same tempo… count the bars of each section to create your map ; tous les 8 mesures, noter quels éléments jouent et quels effets » (Sounds of Ibiza) ; template : R2S = blocs vides nommés, marqueurs de navigation et **courbe d'énergie dessinée sur une piste factice** avant toute note ; amen : « length in bars = seconds × BPM / 240 ; draw the arrangement matrix ; write the highest-energy section first » | [DOC-EXTRAIT] ; [DOC-lu] |
| 2 Instruments : ordre kick / basse / lead | Chris Lake : « starts tracks with the low end, dragging in kicks and bass from other projects before re-writing elements » (c'est ainsi qu'a commencé « Beggin' ») ; amen : « Groove, then bass, then harmony, then melody, then fx » ; house : « the kick and bass relationship *is* the mix » | [DOC-EXTRAIT MusicRadar] ; [DOC-lu] |
| 3 Passage central de 8 mesures | Bass house : « composer en commençant directement par le drop, qui contient la plupart des éléments, puis dépouiller ou varier pour créer intro et breakdown » (EDMProd) ; amen : « **Write the drop before the intro** ; derive every other section by subtraction, not by writing fresh material » ; PML / Hyperbits / Myloops : « copy your 8-bar core across the drop sections first, then work backwards, stripping elements out to build the intro and breakdown » | [DOC-EXTRAIT] ; [DOC-lu] |
| 4 Arrangement complet | Procédure amen 11 en 9 points : tempo/tonalité/longueur → courbe d'énergie par 8 → sections sur multiples de 8 → boucle du drop → soustraction → une section vraiment contrastante (breakdown/réharmonisation) → transitions à chaque couture → test de soustraction → « quelque chose change toutes les 8, quelque chose de gros toutes les 16 ou 32 » | [DOC-lu] |
| 5 Mix | Après l'arrangement (amen 16 : « spectral problems are almost always arrangement problems » ; décider le budget de bandes avant d'écrire) ; référence à niveau égal ; Garrix : mixe et masterise **98 %** de ses sorties lui-même, ne délègue que s'il bloque « à la fin, plutôt sur le son que sur le mixdown » | [DOC-lu] ; [DOC-EXTRAIT garrixinterview/SOS] |
| 6 Automations | « Automate inside notes, not only between them » ; « sounds amateur but nothing is wrong → automate something » ; filtre sur bus | [DOC-lu amen 11 patterns / 05 ref] |
| 7 Voix | Future rave : vocal « meticulously placed » ; LUCKY (Guetta & MORTEN, été 2025) : vocal écrit avec une IA ; bass house : vocal = élément de production, 1–4 mesures, verrouillé sur kick et basse | [DOC-EXTRAIT edm.com, ravejungle] ; [DOC-lu bitwize] |
| 8 Export et livraison | §4.4 | |

### 4.2 « Finish the track », sessions d'idées, ghost production, A&R

- **Finir** : Garrix — « Finishing tracks is a challenge » ; après l'idée, il décide qui featurer et la direction ; **une fois que le label valide, il passe en « finishing mode »** ; « beaucoup de titres non sortis parce que finir correctement prend beaucoup de temps » [DOC-EXTRAIT garrixinterview, d'après Sound On Sound]. Guetta & MORTEN : répartition des rôles — « Morten came with this sound… I have more experience in making chords and melodies and **structuring records**, so we complete each other » [DOC-EXTRAIT edm.com / weraveyou]. Ableton « One Thing » (100 épisodes) : conseils courts d'artistes « pour démarrer, avancer et **finir** » [DOC-EXTRAIT ableton.com/blog, musictech].
- **Sessions d'idées** : Chris Lake — DJ Mag « Beat From Scratch » (workflow Ableton, sur portable ; « I've released music that I've only monitored on laptop speakers ») [DOC-EXTRAIT MusicRadar, DJ Mag] ; garder des banques de kicks/basses de projets précédents (cf. `drums-signature` du dépôt) [HEUR à partir de MusicRadar].
- **Ghost production / A&R** : livrables attendus = « mastered WAV, unmastered premaster, instrumental, extended mix, radio edit, **stems from bar one**, documentation des droits » ; stems groupés drums / bass / music / FX / vocals, même point de départ, 24 bits 44,1 ou 48 kHz, effets temporels imprimés volontairement ; nommage « Artist_Title_Version_BPM_Key_Date » ; **quand un label demande un intro plus court, un radio edit, un vocal-up ou un instrumental, les stems rendent la demande gérable** ; masters club compétitifs ~ −8 à −6 LUFS intégrés [DOC-EXTRAIT theghostproduction.com, yourghostproduction.com]. Chris Lake 2026 : « protéger la culture de la prise de risque » (label Black Book) [DOC-EXTRAIT edm.com].

### 4.3 Pièges connus (compilés)

Accumulation sans soustraction ; build qui ne monte que le volume ; drop plus dense mais pas différent ; second drop identique ; 90 s d'intro en streaming ; spectre plein dès la mesure 1 (rien à ouvrir, disque immixable) ; sub en breakdown ; riser partout ; queues de reverb sur le drop ; transitions hors grille ; plus de 10 éléments simultanés ; supersaws à 5 notes (3 suffisent) ; juger sans égaliser les niveaux ; mixer fatigué (trop brillant, trop compressé) ; pour la house : structure build-and-drop = EDM, pas house ; kick trop cliquant = techno ; oublier l'intro/outro DJ [DOC-lu amen 01/02/09/11/18/20]. Bass house : « too much going on » — la basse porte tout, les leads sont minimaux [DOC-lu bitwize, Fearvox].

### 4.4 Checklists de livraison (versions)

| Version | Contenu | Longueur | Source |
|---|---|---|---|
| **Original / club mix** (« extended » si un radio edit existe) | intro/outro DJ 16–32 mes. (bass house : 16), deux drops, breakdown complet | 4:30–6:30 ; bass house 4–6 min ; tech house 5–8 | bitwize, Fearvox, jefrob [DOC-lu] ; djcity « 6, 7 ou 8 min » [DOC-EXTRAIT] |
| **Radio edit** | intro 4–8 mes., pas de build initial, premier drop < 45 s–1:00, outro court ; **mêmes blocs internes** (Harmonix : Memories, Feel So Close, Take Over Control) | 2:30–3:30 | Wikipedia, majormixing [DOC-EXTRAIT] ; Harmonix [DOC] |
| **Extended mix** (à partir du radio edit) | même structure + intro 16 et outro 32–48 en soustraction ; parfois un drop instrumental (« postchorus ») ajouté après chaque refrain | +1:00 à +3:30 | Harmonix [DOC] ; Gearspace (fil « fastest way to make a radio edit and an extended version ») [DOC-EXTRAIT, non lu] |
| **Instrumental** | mix sans voix, mêmes automations | = original | theghostproduction [DOC-EXTRAIT] |
| **Acapella** (si libérée) | voix seule, à sec + une version avec effets | — | idem |
| **Stems** | drums, bass, music, FX, vocals ; depuis la mesure 1 ; 24 bits ; même fréquence d'échantillonnage | = original | idem |
| **Premaster** | crête ≈ −6 dBFS, sans limiteur | — | amen 16 [DOC-lu] |
| Contrôles avant envoi | mono, téléphone, bas volume, sub mono, ≤ −1 dBTP, A/B à niveau égal, intro/outro adaptés à la destination (DJ / streaming / album) | — | amen 05 [DOC-lu] |

Le skill `live-export-wav` du dépôt fait l'export (24 bits, sans normalisation, durée exacte par repère « FIN export ») ; `live-mix-mastering` et `mastering-outils` mesurent LUFS/true peak sur le Mac (rien ne le mesure dans le conteneur, rappel du dépôt).

### 4.5 Gestion des versions dans Live 12

- **Set** : « Sauver Set Live sous… » un nouveau nom **avant** toute modification (règle 1 de `ableton-live-session`) ; un Set par version livrable (`<titre> club.als`, `<titre> radio.als`, `<titre> instrumental.als`) ou, plus sûr pour garder les automations alignées, **un seul Set** avec des repères et deux zones d'export [HEUR]. Le manuel Live 12 chapitre Arrangement (`corpus/constructeur/live12-manuel-06-arrangement-view.md`) décrit repères, boucle, Insérer Silence, Supprimer Zone temporelle, Consolider [DOC].
- **Repères (locators)** : un par section (« Intro », « Build 1 », « Drop 1 »…), plus « FIN export m:ss » ; `lom.py locator <t> "<nom>"` renomme sans supprimer ; `arrangement_map.py` reconstruit la carte piste × sections après toute édition manuelle (règle de `arrangement-avance`) [DOC dépôt].
- **Arrangement vs Session** : Session = boucle de 8 mesures et variantes (scènes « drop », « break », « build ») pour l'étape 3 ; Arrangement = structure, automations, exports (étapes 4–8). Passer de l'une à l'autre en enregistrant les scènes dans l'Arrangement ou en glissant les clips ; ne plus composer en Session une fois l'Arrangement commencé, sinon les clips de Session et d'Arrangement divergent [HEUR, pratique courante ; Producer Pal lit et écrit les deux vues].
- **Radio edit à partir du club mix** : dans le même Set, poser la boucle sur les zones à supprimer (intro 17–32, outro 145–160, moitié du breakdown), Edition › Sélectionner boucle → Edition › Supprimer Zone temporelle : clips, automations et repères se déplacent ensemble (procédure « allonger/raccourcir » de `arrangement-avance`) ; relire `arrangement_map.py` ; « FIN export » recalé [DOC dépôt]. Sens inverse (extended depuis un radio edit) : Créer › Insérer Silence, puis remplir par duplication des clips voisins (les automations tiennent leur dernière valeur) [DOC dépôt].
- **Stems** : Fichier › Exporter Audio/Vidéo, « Pistes rendues : toutes les pistes individuelles », depuis 1|1|1 jusqu'au repère de fin, sans normalisation ; ou exporter les **bus** (`BUS - …` du projet) pour obtenir les 5 stems groupés que demandent les labels [HEUR d'après la convention de routage du dépôt ; procédure d'écran : `live-export-wav`].
- **Mémoire** : `memoire-projet` (instantanés avant transformation, journal `lom.py journal`) tient l'historique des versions ; noter dans `projet-<nom>.md` la structure en mesures et les repères de chaque version [DOC dépôt].

## 5. Spécificités par producteur de référence (arrangement)

| Producteur | Faits sourcés | Étiquette |
|---|---|---|
| **David Guetta** | Se décrit comme celui qui « a plus d'expérience pour faire les accords, les mélodies et **structurer les disques** » dans le duo avec MORTEN [DOC-EXTRAIT edm.com/weraveyou]. Harmonix (2007–2012) : intros de 4–8 mesures en radio ; refrain chanté 16 → drop instrumental **8** (Titanium ×3, DYWC avec SHM) ; hook à 15 s (Memories) ; tout en blocs de 8 ; versions extended = intro 16–24 + outro 24–48 + un drop instrumental ajouté après chaque refrain [DOC]. Future rave (2019–) : « energy and hooks of EDM, futuristic sounds of techno, emotion of trance and (future) house » ; ambition affichée : sortir de la structure pop-EDM vers l'underground (techno, melodic techno, tech house) tout en gardant « the sonics of rave music with the power » [DOC-EXTRAIT weraveyou 2020] | [DOC] + [DOC-EXTRAIT] |
| **MORTEN** (Morten Breum) | « Morten came with this sound » (Guetta) ; le duo a produit d'abord « Never Be Alone » (avec Aloe Blacc) et le remix officiel de « Heaven » d'Avicii ; EP « New Rave » (juillet 2020) ; « we make the music we like, the music we want to play » (2022) ; LUCKY travaillé pendant l'été 2025, vocal écrit avec une IA (2025) ; sets B2B « Future Rave » [DOC-EXTRAIT Wikipedia, edm.com, weraveyou, ravejungle]. Aucun détail d'arrangement (longueur de breakdown, mesures) dans les résumés | [DOC-EXTRAIT] ; arrangement **[NON VÉRIFIÉ]** |
| **Martin Garrix** | Mix + master de 98 % de ses sorties ; finition = phase séparée, après validation du label ; beaucoup de titres jamais finis ; synthé préféré Omnisphere 2 [DOC-EXTRAIT garrixinterview/SOS] ; « Animals » : original 5:04, radio 2:57 (big room instrumental) [DOC-EXTRAIT Wikipedia] ; « Like I Do » avec Guetta et Brooks (future bounce) [DOC-lu bitwize] ; MusicRadar « Anatomy of a hit: Animals » à lire sur le Mac | [DOC-EXTRAIT] |
| **Chris Lake** | Commence par le grave (kicks et basses tirés d'autres projets, puis réécrits) ; produit sur portable, a sorti des titres écoutés seulement sur haut-parleurs de portable [DOC-EXTRAIT MusicRadar] ; DJ Mag « Beat From Scratch » : conseils de workflow Ableton [DOC-EXTRAIT] ; « bass tech house », label Black Book, résidences Brooklyn Mirage ; « Deceiver » avec Green Velvet [DOC-lu bitwize] ; 2026 : « protéger la culture de la prise de risque » [DOC-EXTRAIT edm.com] | [DOC-EXTRAIT] |
| **Jauz** | « Feel the Volume » (2014) a fait entrer la bass house sur le circuit festival ; « Rock the Party » (2015, Ephwurd) codifie la variante festival : « massive build-ups, crowd-ready vocal chops, drop built on overdriven mid-range bass » ; genres : trap, bass house, dubstep, future bass [DOC-lu bitwize ; DOC-EXTRAIT Wikipedia] ; template PML « Bass House like Jauz » (structure du template à lire sur le Mac) | [DOC-lu] ; minutages **[NON VÉRIFIÉ]** |
| **Dom Dolla** | Titres « Girls », « Saving Up », « San Frandisco » (pages Wikipedia non lues) ; lauréat EDMAs 2026 [DOC-EXTRAIT edm.com]. Rien d'exploitable sur l'arrangement dans les résultats | **[NON VÉRIFIÉ]** |
| (Fisher, Tchami, Malaa, Heldens) | Fisher « Losing It » 4:08, hats coupés dans les builds, clap sur le 2 ; Tchami a forgé le terme future house (remix « Go Deep », 2013), « any kind of house that hasn't been invented yet » ; Malaa = « dark, minimal, almost no melodic content » ; Heldens « Gecko » 2013, « Koala » 4:24/2:48 [DOC-lu bitwize ; DOC-EXTRAIT Wikipedia, topmusicarts] | [DOC-lu]/[DOC-EXTRAIT] |

## 6. Contradictions relevées

1. **House avec ou sans drop.** amen 01 : « il n'y a pas de drop en house classique ; build-and-drop = EDM » ; EDMProd house : intro DJ → breakdown → drop → drop varié → breakdown → drop → outro (16–32 chacun) ; bitwize house : « breakdown sections stripping to drums before rebuilding ». Lecture : la house de club (deep, classique) est additive ; la house de festival, la bass house, la future house et la future rave sont en build/drop. Le skill doit demander la cible (club ou festival) avant de choisir le schéma.
2. **Longueur du build.** amen 02 : big room 16, house 8–16 ; R2S : 8 ; Fearvox : 16 puis 8 ; EDMProd tech house : breakdown + build = 8 au total ; jefrob tech house : build 8 ; forme-tension EDM 128 : 8. Convergence : 8 en tech house, 16 en festival/bass house pour le premier build, 8 pour le second.
3. **Silence avant le drop.** forme-tension §4 : « deux temps de rien » ; amen 02 : 1 temps = standard, 2 = dramatique, 1 mesure = très dramatique ; Fearvox : kick retiré 4–8 mesures avant (autre chose qu'un silence). Les trois sont compatibles si l'on distingue « kick retiré » (4–8 mes.) et « gap » (1–2 temps).
4. **Second drop plus long ou non.** forme-tension §5 : « pas plus long que le premier » ; amen 02 : « make it longer » figure parmi les moyens de le faire dépasser ; amen club template : drop 2 = 48 mes. contre 32 ; Harmonix : les drops instrumentaux Guetta font la même longueur (8 ou 16) à chaque occurrence. À trancher par le genre : radio = même longueur ; club = drop 2 peut s'allonger.
5. **Longueur d'intro DJ.** bitwize EDM/tech house : 32–64 mesures ; forme-tension et amen : 16–32 ; Fearvox bass house : « 16 plutôt que 32 pour le streaming » ; Harmonix extended (Guetta, Afrojack, Calvin Harris) : **16 mesures** d'intro, outros 24–48. Recommandation : 16 (bass house, future rave), 32 (tech house), jamais 64 sauf demande d'un DJ tool.
6. **Durée totale bass house.** bitwize 4–6 min ; Fearvox 3:30–5:00 streaming, 5–7 DJ ; jefrob 3–4 (festival) à 5–6 ; amen house 5–7 club / 3–4 radio.
7. **Position du sommet.** amen : 60–75 % de la durée (second drop) ; les templates EDM symétriques (deux drops de 32) placent le second drop à 70–80 % : compatible ; le template house amen (main 96–159 sur 200) met le sommet à 50–80 %.
8. **Cibles de sonie.** amen 05 : club −8 à −6, streaming −14 ; amen 09 : big room −6 à −5, future house −7 à −6 ; theghostproduction : −8 à −6. Le dépôt (mastering-outils) tranche par mesure sur le Mac.
9. **Étiquettes Harmonix ≠ vocabulaire producteur.** « chorus » y désigne le refrain chanté et « inst » le drop ; un « prechorus » de 8–16 mesures est souvent le build. Ne pas compter un « chorus » Harmonix comme un drop sans écouter.

## 7. URL à télécharger depuis le Mac

Liste complète (71 entrées, sans YouTube) : `scratchpad/house/urls-axe4.json`. Priorités : EDMProd (house, bass house, tech house), edm.com et weraveyou (Guetta & MORTEN), MusicRadar (Chris Lake ; Anatomy of a hit « Animals »), garrixinterview (SOS), topmusicarts (Losing It), theghostproduction (livrables), Wikipedia (Future rave, Radio edit, Animals, Koala, Losing It), Attack Magazine Deconstructed (Floorplan, DJ Boring : analyses house minutées), Ableton One Thing (100 tips), majormixing (durées streaming), Sounds of Ibiza (références), PML (8-bar loop → track ; pages des templates Jauz / Tchami), Nieto et al. ISMIR 2019 (PDF Harmonix).

## 8. Fichiers écrits dans `corpus/house-future-rave/` (texte intégral, en-tête YAML)

amen-foundations-11-form-and-arrangement · amen-foundations-18-psychoacoustics-and-tension · amen-foundations-20-spectral-arrangement · amen-patterns-02-drop-and-buildup · amen-patterns-06-transitions-and-fx · amen-patterns-10-arrangement-templates · amen-patterns-11-signature-techniques · amen-reference-03-bpm-and-timing-tables · amen-reference-05-quick-decision-tables · harmonixset-readme · harmonixset-segments-dance-edm (31 titres, segments bruts + conversion en mesures) · bitwize-genres-deep-house · fearvox-syn-bass-house-structure-research · microsoft-resource2skill-edm-arrangement-scaffolding-energy-map · dragoscv-mmo-tech-house-ghid-ro (roumain) · salami-data-public-readme. Les six fiches bitwize bass-house / future-house / tech-house / edm / progressive-house / house existaient déjà sous `bitwize-genre-*-readme.md` (autre agent, même source) : mes doublons ont été supprimés.

Sources GitHub (URL raw) : mekedron/claude-amen-sessions (`theory/00-foundations/11,18,20`, `30-patterns/02,06,10,11`, `40-reference/03,05`) · urinieto/harmonixset (`README.md`, `dataset/metadata.csv`, `dataset/segments/*.txt`, `dataset/beats_and_downbeats/*.txt`) · bitwize-music-studio/claude-ai-music-skills (`genres/deep-house/README.md`) · Fearvox/Syn (`research/analysis/bass_house_research.md`, branche master) · microsoft/Resource2Skill (`skills_wiki/reaper/edm_arrangement_scaffolding_energy_map_484eb2a8/text/overview.md`) · dragoscv/mmo (`docs/genuri/tech-house.md`) · DDMAL/salami-data-public (`readme.md`, `readme_metadata.md`, `metadata/metadata.csv` — CLASS popular 285 titres, GENRE « Dance_Pop » 14, « Electronica » 14 : pas de titre EDM connu, non exploité).
