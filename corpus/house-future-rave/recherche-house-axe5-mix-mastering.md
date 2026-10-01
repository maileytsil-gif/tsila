---
titre: "Rapport de recherche — axe 5 : Recherche — Axe 5 : mixage et mastering de la future rave, de la bass house et de la house de festival/club (future house, tech house, big room)"
source: recherche web et GitHub, session Claude Code du 2026-09-24 (agent de recherche)
recupere_le: 2026-09-24
mode: synthese
langue: fr
axe: mixage et mastering (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: synthèse interne avec étiquettes de preuve ; les sources primaires sont citées dans le texte
---

# Recherche — Axe 5 : mixage et mastering de la future rave, de la bass house et de la house de festival/club (future house, tech house, big room)

Date : 2026-09-24. Périmètre : Ableton Live 12 Suite + plug-ins de l'utilisateur (FabFilter Pro-Q 4 / Pro-C 3, Waves REQ 6 / API-2500 / L2 / L4 / J37 / MetaFlanger / F6 / WLM Plus / TG Mastering Chain, bx_glue, soothe3, iZotope Imager 2 / Insight 2 / Tonal Balance Control 3 / Ozone Elements, SPAN, TDR Nova).

## Étiquettes

| étiquette | sens |
|---|---|
| **[DOC]** | document lu en entier (manuel constructeur du corpus, dépôt GitHub téléchargé, doc ffmpeg/pyloudnorm) |
| **[COMM]** | document communautaire lu en entier (JefroB, bitwize, Music Production Wiki) : valeurs *déclarées* comme conventions de genre, **pas des mesures** de masters commerciaux — à traiter comme [HEUR] sourcé |
| **[DOC-EXTRAIT]** | résumé de recherche web (page non téléchargeable depuis le conteneur : EGRESS_BLOCKED) ; à revérifier sur l'URL listée dans `urls-axe5.json` |
| **[CALC]** | arithmétique à partir de valeurs étiquetées |
| **[DÉPÔT]** | déjà dans le dépôt (skills) — cité, pas répété |
| **[HEUR]** | valeur de pratique sans source (proposition de départ) |

**Constat principal** : aucune source accessible ne publie de *mesures* de masters commerciaux de future rave, bass house ou big room (LUFS, PLR, ST drop vs breakdown). Les chiffres disponibles sont des cibles déclarées par des ingénieurs, des sites de mastering et des fiches de genre communautaires. Les analyses mesurées trouvées (Music Production Wiki) portent sur la pop (« Blinding Lights », « bad guy »), le hip-hop et le disco-funk. Des mesures locales sur des références achetées (Beatport, WAV) restent le seul moyen d'avoir des chiffres du genre : procédure en §1.4.

---

## 1. Cibles de sonie, true peak, PLR, dynamique drop/breakdown

### 1.1 Normalisation des plateformes (état 2026)

| plateforme | cible intégrée | true peak recommandé | remarques | source |
|---|---|---|---|---|
| Spotify | −14 LUFS (modes « Loud » −11, « Quiet » −23) | −1 dBTP (−2 dBTP si le master dépasse −14 selon Spotify) | monte aussi les titres faibles (sauf en mode Quiet) | [DOC-EXTRAIT] forasoft, uptrack, support.spotify |
| YouTube | −14 LUFS | −1 dBTP | **ne fait que baisser**, jamais monter ; toujours actif | [DOC-EXTRAIT] forasoft, MusicPulse |
| Apple Music (Sound Check) | −16 LUFS | −1 dBTP | par titre par défaut ; mode album documenté mais inconstant | [DOC-EXTRAIT] forasoft, Venia |
| TIDAL | −14 LUFS (par album) | −1 dBTP | | [DOC-EXTRAIT] forasoft |
| Amazon Music | −14 LUFS | **−2 dBTP** | la plus stricte sur le TP | [DOC-EXTRAIT] uptrack, Venia |
| Deezer | −15 LUFS | −1 dBTP | | [DOC-EXTRAIT] forasoft |
| SoundCloud | −14 LUFS | −1 dBTP | | [DOC-EXTRAIT] forasoft |
| **Beatport, Bandcamp** | **aucune normalisation** | — | le DJ et le mixer re-gainent ; c'est la destination qui justifie les masters à −8/−6 | [DOC-EXTRAIT] kansamples, Gearspace 1200043, trackscore |
| broadcast (EBU R128) | −23 LUFS, LRA max | −1 dBTP | hors sujet, référence | [COMM] MPW loudness ; [DOC] ffmpeg loudnorm (défaut I −24, TP −2, LRA 7) |

Convergence AES TD1008 citée par plusieurs pages [DOC-EXTRAIT]. **Contradiction** : la « bible » Music Production Wiki (lue en entier) écrit encore « Apple Music **et Tidal** −16 LUFS » [COMM] alors que les pages 2026 donnent Tidal −14 [DOC-EXTRAIT] ; retenir −14 pour Tidal, −16 pour Apple, vérifier sur l'URL Spotify listée.

### 1.2 Ce que disent les pros et les sites de mastering pour l'EDM club/festival

| source | cible | remarque |
|---|---|---|
| EDMProd « LUFS » | **−6 LUFS short-term** = « sweet spot » des EDM fortes ; si on veut −2 dBTP, viser plutôt **−8 ST** (−6 ST + −2 dBTP ensemble = master distordu) ; ceiling **−1,0 dBTP** pour rester propre | [DOC-EXTRAIT] edmprod.com/lufs |
| iZotope (Are You Listening / blog streaming) | EDM ≈ **−7,5 LUFS** intégrés ; ≥ 1 dB de marge TP ; Ozone Maximizer : ceiling −1 dB + True Peak pour le streaming, **−0,6 à −0,8 dB** si conversion mp3/aac | [DOC-EXTRAIT] izotope.com ; doc Maximizer Ozone Elements |
| Mastering The Mix « How loud should you master » | club EDM **−9 à −7 LUFS intégrés** ; « la sonie atteignable se décide dans le mix, pas au limiteur » | [DOC-EXTRAIT] masteringthemix.com |
| Ian Shepherd (SOS, Production Advice, Mastering Show #92) | **ne pas dépasser −10 LUFS short-term** aux passages les plus forts, TP ≤ −1 ; « EDM et thrash à −10 ST tout du long → −10/−11 intégrés » ; au-delà de −9 ST il n'y prend plus plaisir | [DOC-EXTRAIT] soundonsound.com/techniques/ian-shepherd-loudness-dynamics ; productionadvice.co.uk/how-loud |
| Beatport-style club masters | **≈ −8 LUFS intégrés, parfois plus** ; « −8 à −6 » ; « −11 à −8 a l'impact que les PA demandent » | [DOC-EXTRAIT] kansamples ; luvlang ; trackscore ; larslentz |
| Music Production Wiki — tableau mastering, ligne **House** | cible **−10 à −9 LUFS** ; compresseur 2:1–3:1 attaque 30–60 ms release 200–400 ms + limiteur ; « vérifier le kick en mono, référence club mono » ; ligne Trap : −9/−8, sub mono < 80 Hz | [COMM] |
| JefroB — fiches de genre (déclaré) | tech house **−8/−9** (DJ tool, DR 5–8 dB) ; **electro house −6/−8** (DR 4–6 dB, « clipping avant limiting ») ; **bass house −7/−9** (DR 5–7 dB, 4–6 dB GR sur le bus basse) ; progressive house −9/−11 ; **peak time techno −7/−9** (limiteur 2–4 dB GR) ; uplifting trance −8/−10 (DR 8–12) ; tech trance −7/−9 ; french touch −7/−9 ; streaming : −14 partout | [COMM] `corpus/house-future-rave/jefrob-genre-house-mixing-and-mastering.md`, `…techno…`, `…trance…` |
| Flotown Mastering | plaide pour un **crest factor plus élevé** en EDM (moins de fatigue, plus de clarté) — position minoritaire mais argumentée | [DOC-EXTRAIT] flotownmastering.com |

**Contradictions signalées**
1. −6 LUFS ST (EDMProd) contre −10 LUFS ST maximum (Shepherd) : 4 LU d'écart sur la même mesure. Les deux sont cohérents avec leur destination : EDMProd parle de compétitivité Beatport/festival, Shepherd de qualité perçue et de streaming normalisé. Pour un skill : **deux masters** (club ≈ −8/−7 intégrés, TP −1 ; streaming ≈ −10/−11 intégrés ou plus dynamique), comme le préconisent MPW et Venia [COMM][DOC-EXTRAIT].
2. Ceiling pour les formats avec pertes : iZotope −0,6/−0,8 dB [DOC-EXTRAIT] contre −2 dBTP (MPW, Amazon) [COMM][DOC-EXTRAIT] ; l'argument commun est le dépassement d'encodage de 0,5–2 dB [COMM]. Retenir −1,0 dBTP par défaut (déjà la valeur du dépôt [DÉPÔT] `notes-locales.md`) et −2 dBTP pour Amazon/YouTube si demandé.
3. JefroB donne « dynamic range 4–6 dB » pour l'electro house sans définir la mesure (PLR ? LRA ? DR-meter ?) [COMM] : à ne pas citer comme LRA.

### 1.3 PLR, crest factor, LRA, drop vs breakdown

- Définitions : PLR = true peak − LUFS intégrés ; crest factor = crête − niveau moyen sur tout le titre [DOC-EXTRAIT] Sweetwater, Lars Lentz. MPW : crest 12–14 LU = master dynamique, < 6 LU = brickwall ; **LRA musique commerciale 4–9 LU**, < 4 LU = master plat ; « viser au moins 8 LU entre TP et intégré ; si le LUFS demandé exige > 4–5 dB de GR au limiteur, c'est le mix qu'il faut remonter » [COMM].
- [CALC] avec TP à −1 dBTP : master à −7 LUFS → PLR 6 dB ; −8 → 7 dB ; −10 → 9 dB ; −14 → 13 dB. Les cibles club de §1.2 impliquent donc des PLR de 5–8 dB, c'est-à-dire des masters où **clipper et limiteur portent 4–8 dB** de réduction sur le drop — d'où l'importance du clipping (§4.3).
- Short-term par section : MPW (streaming, mix à −14 intégrés) : sections fortes **−10 à −12 LUFS ST**, intros **−18 à −20 ST** ; colonnes de genre du tableau : ST des sections fortes entre −9 et −14, LRA cible entre 4 et 10 LU selon le genre [COMM]. JefroB (trance) : « breakdown trop faible par rapport au drop : la normalisation streaming tue le build » — donc contraste voulu mais borné [COMM].
- **Aucune mesure publiée** du ST drop/breakdown en future rave/bass house n'a été trouvée [gap]. Proposition de départ [HEUR] pour un master club à −8 intégrés : drop −7/−6 ST, breakdown −12/−14 ST (écart 5–7 LU), LRA 4–7 LU ; à remplacer par les mesures locales de §1.4.
- Exemples mesurés hors genre (pour calibrer l'oreille) [COMM] MPW : « Blinding Lights » ≈ −7/−8 intégrés (crest sacrifié ≈ 6–7 LU) ; « HUMBLE. » −8/−9 ; « Get Lucky » ≈ −11 avec crest 10–11 LU ; « bad guy » ≈ −14.

### 1.4 Mesurer soi-même (le seul chemin vers des chiffres du genre)

- Sur le Mac : ffmpeg, sox et pyloudnorm sont absents [DÉPÔT] `mastering-outils/references/notes-locales.md` ; Insight 2 en bout de Main et WLM Plus en mesure seule (capture d'écran) [DÉPÔT] `waves-mastering.md`.
- Si l'utilisateur accepte une installation : `pip install pyloudnorm` (BS.1770-4, `integrated_loudness`, `loudness_range` EBU Tech 3342, blocs 400 ms, filtres De Man) [DOC] `corpus/house-future-rave/pyloudnorm-readme.md` ; ou ffmpeg `ebur128=peak=true` (M/S/I/LRA, SPK/TPK) et `loudnorm` en double passe [DOC] `corpus/house-future-rave/ffmpeg-filters-loudnorm-ebur128.md`. Outils GitHub batch : LoudScan (rapport HTML, LUFS/TP/LRA via ffmpeg), mstcgalis/lufs (CLI INT/TP/ST/LRA) [DOC-EXTRAIT].
- Protocole [HEUR] : 6–10 références WAV Beatport par genre → intégré, TP, LRA, ST max (drop) et ST min hors intro (breakdown), PLR = TP − I ; remplir un tableau « genre → I / TP / PLR / ΔST drop-break » dans la mémoire projet ; recontrôler sur le fichier exporté, jamais sur le vu-mètre [DÉPÔT] `mastering-mesures.md`.

---

## 2. Le grave : kick, sub, sidechain, mono, saturation, layering

### 2.1 Fréquences et rôles par genre

| genre | kick | sub / basse | qui tient la fondamentale | source |
|---|---|---|---|---|
| tech house | sub 50–70 Hz, corps 100 Hz, click 3–5 kHz, HPF 30 Hz, transient shaping ; « pas assez de click = erreur classique » | basse 60–200 Hz (plus de médium que la deep), distorsion/saturation, sidechain **rapide**, mono ; coupe 200–300 Hz | kick (sub court) + basse au-dessus ; [DÉPÔT] `roles.md` : « deep/minimal/tech house → le SUB tient le fondamental » (cas basse-sub sinus) — les deux écoles existent | [COMM] JefroB house sound-design & mixing |
| bass house | kick : couper 80–100 Hz **si** conflit avec le sub ; click 2–6 kHz | 3 couches : **sub HPF 25 / LPF 80 Hz** ; **mid « wobble » HPF 80, 100–500 Hz** ; **top HPF 300 Hz** ; toutes sidechainées au kick ; 60–200 Hz = zone DOMINANTE ; mono < 150 Hz ; 4–6 dB GR sur le bus basse ; bitwize : sub + growl médium + harmoniques hautes | le **sub** (couche dédiée) | [COMM] JefroB bass house ; bitwize bass-house |
| electro house / big room | présence 4–5 kHz ; big room : centré **50–60 Hz**, court, transitoire en couche, « gentle clipping » ; sub sinus **≈ 50 Hz, < 100 ms** ; cloche +1–2 dB à 100 Hz ; queue audible **200–350 ms** ; à 138 BPM une queue > ≈ 215 ms (½ temps) entre en collision avec la remontée du sidechain ; **accordé à la tonique ou à la quinte** | sub HPF 30 / LPF 80 Hz ; « sidechain EVERYTHING » (leads compris) | le **kick** (sub intégré) + sub de renfort court | [COMM] JefroB electro house ; [DOC-EXTRAIT] myloops, KVR |
| future rave (par voisinage peak-time techno + trance) | couches : **sinus 50–60 Hz + punch saturé 100–200 Hz + click 3–5 kHz**, enveloppe de pitch ≈ 200 Hz → fondamentale en < 20 ms ; boost 50–60 et 3–4 kHz, creux 200–400 ; 50–100 Hz = zone DOMINANTE ; tout le reste HPF 80–120 Hz | reese / rolling bass 200 Hz–4 kHz HPF au-dessus du kick, saturation parallèle, sidechain ; sub séparé mono | le **kick** ; la basse « rolling » vit au-dessus (≥ 80–100 Hz) | [COMM] JefroB techno peak time (sound-design, mixing) ; [DOC-EXTRAIT] melodigging/Wikipedia future rave (« reese/rolling basslines, offbeat stabs, 126–130 BPM ») |
| future house | basse FM métallique/élastique, sidechain proéminent, mix propre | | selon design : sub sinus + basse FM au-dessus [HEUR] | [COMM] bitwize future-house |
| deep house (référence basse) | fondamentale 50–60, corps 80–120, HPF 30 | basse 40–120 Hz, sidechain **2–3 dB**, mono < 120 Hz ; HPF basse 35 Hz | sub | [COMM] JefroB |

Rappels déjà dans le dépôt [DÉPÔT] : matrice sub/kick, accord (F → 43,7 Hz ; kick F1 87 / C1 65), corrélation 30–120 Hz, `kick_bass_check.py` : `kick-bass-equilibre/references/roles.md`, `mesure.md`. Les chiffres ci-dessus ne les contredisent pas ; ils ajoutent la règle **big room/future rave = kick porteur** avec sub court de renfort, alors que la deep/tech house garde le sub tenu.

### 2.2 Sidechain : profondeur, forme, durée, outils

Valeurs de départ [COMM] MPW bible sidechain (tableau « session-ready ») :

| paramètre | général | bass / keys (kick → basse) | bus / master |
|---|---|---|---|
| seuil (relatif à la crête du déclencheur) | −18 à −12 dBFS | −18 à −10 dBFS | −30 à −20 dBFS |
| attaque | 1–10 ms | **1–5 ms** | 10–30 ms |
| release | 50–200 ms | **50–150 ms** | 100–400 ms |
| ratio | 3:1–6:1 | 4:1–10:1 | 2:1–4:1 |
| HPF de détection | 80–120 Hz | 80–100 Hz | 100–140 Hz |
| réduction | 3–8 dB | **4–12 dB** | 1–4 dB |

- Pompage audible : attaque **0,1–1 ms** ; transparent : 5–20 ms ; « la douceur d'un pump se règle au release, pas à l'attaque » ; attaque 20–50 ms = pump mou [COMM].
- Release calé au tempo : 60 000 / BPM → **128 BPM = 469 ms** par noire (234 ms pour une croche) ; release > intervalle entre kicks = réduction cumulée, jamais de récupération [COMM]. À 126 BPM : 476 ms ; 130 BPM : 462 ms [CALC].
- Cohésion kick/basse « invisible » : 2–4 dB, attaque 5–20 ms, release 60–100 ms [COMM]. Profondeur par genre [COMM] JefroB : deep house 2–3 dB ; afro sub 4–6 dB ; tech house « fast » ; bass/electro house : « tight ducking » sur toutes les couches ; **french touch 8–12 dB** sur tout (pads, samples, basse, voix). Big room / future rave : leads et pads pompés de façon audible, 6–10 dB [HEUR] (aucune valeur publiée trouvée).
- Kick fantôme (clip muet routé vers le sidechain) pour garder le pump pendant les fills/breaks [COMM] ; lier L/R sur un déclencheur mono sinon l'image bouge à chaque pump [COMM].
- Outils [DOC-EXTRAIT] : Kickstart (préréglages 4/4), LFO Tool (courbe dessinée, rate 1/4), ShaperBox (Volume shaper **par bande** : ne creuser que le grave d'un son) — **aucun n'est dans la liste de l'utilisateur**. Multibande sur 60–120 Hz avec attaque rapide + lookahead pour « réagir juste avant le kick » [DOC-EXTRAIT].
- Correspondance locale : voir §5 (Compressor natif toléré, bx_glue sidechain externe + HPF, API-2500 S/C, Pro-C 3).

### 2.3 Mono sous X Hz, saturation, layering

- Mono : « tout < 120 Hz » (deep/tech house, dépôt) [COMM][DÉPÔT] ; **< 150 Hz** bass house [COMM] ; « strict mono below 200 Hz » (MPW, ligne House du tableau de mix) [COMM] ; vinyle 150–200 Hz [COMM]. **Contradiction** 120/150/200 : la valeur haute (200) coupe la largeur des stabs et de la basse médium ; retenir 120 Hz par défaut (Mono Maker bx_glue déjà réglé ainsi [DÉPÔT] `chaine-actuelle.md`), 150 Hz pour la bass house dont la couche « mid » commence à 80–100 Hz [HEUR]. Les sub des clubs sont sommés mono même en stéréo [DOC-EXTRAIT] producerschool.
- Saturation du sub/basse : soft clip **5–15 % de drive** donne du contenu 100–800 Hz audible sur petites enceintes [DOC-EXTRAIT] ; J37 : **7,5 ips** « pour le matériel orienté grave (kick, basse) », niveau d'entrée = quantité de saturation/compression, formule 888 la plus sale, 815 la plus plate [DOC] `corpus/constructeur/assets-wavescdn-com-pdf-plugins-j37-tape-pdf-texte.md` ; bx_glue XL saturation (light → heavy) [DOC] `…bx-glue-manual-pdf-texte.md`. Ne pas saturer la couche sub sinus elle-même en bass house : la distorsion vit sur la couche mid [COMM].
- Layering de kick (attaque / corps / queue) : techno peak-time « sub sinus 50–60 + punch 100–200 saturé + click 3–5 kHz » [COMM] ; big room « kick court 50–60 Hz + transitoire 2–4 kHz + sub sinus ≈ 50 Hz < 100 ms, queue 200–350 ms » [DOC-EXTRAIT] ; deuxième couche = **transitoire seul** pour le punch [DOC-EXTRAIT]. Vérifier la queue contre le release du sidechain (½ temps ≈ 232 ms à 129 BPM [CALC]).

---

## 3. Spectre et densité

### 3.1 Carte fréquentielle élément → bande → coupe → boost (drop, genres cibles)

| élément | bande utile | coupe | boost | mono/large | sources |
|---|---|---|---|---|---|
| kick | sub 50–60 (fut. rave/big room) ou 50–70 (tech house) ; corps 80–120/100 ; click 3–5 kHz | HPF 30 Hz ; 200–400 Hz (boxiness) ; 80–100 Hz si conflit avec sub (bass house) ; 300–500 « ballon de plage » | 50–60 Hz ; 3–4 kHz ; 4–5 kHz (electro) | mono | [COMM] JefroB ; [DOC] iZotope EQ cheat sheet (corpus) |
| sub | 25–80 Hz | HPF 25–30, LPF 80–100 | — | mono | [COMM] |
| basse mid / wobble / reese | 80–500 (bass house), 200 Hz–4 kHz (rolling techno), 60–250 (funky) | HPF 80–100 ; 200–300 (boue) | 100–200 (corps) | mono < 120–150, largeur au-dessus | [COMM] |
| lead supersaw (big room, future rave) | 200 Hz–5 kHz, DOMINANT 500 Hz–2 kHz en drop | HPF 150–200 ; **200–400 Hz** (boue) ; dip 2 kHz sur les pads pour laisser la place | 500 Hz–2 kHz (impact, electro) ; 2–4 kHz (présence) | corps centré/étroit + couche large ; « trop large = s'effondre en mono » | [COMM] JefroB trance & electro |
| stabs offbeat / accords | 300 Hz–1 kHz corps, 1–4 kHz présence | 200–300 Hz | 2–4 kHz | étroit | [COMM] techno |
| pads | 200–500 corps, 2–8 kHz air | scoop 200–400 ; HPF 150–200 | 8–12 kHz | large | [COMM] progressive |
| vocal chops | 500 Hz–2 kHz corps ; présence 2–4/3–5 kHz | HPF 200 Hz ; notch 500 Hz–1 kHz (résonances) | 2–4 kHz | centre (principal), chops secondaires larges | [COMM] tech house, UKG |
| clap / snare | 200 Hz corps, 3–4 kHz crack, 5–8 kHz snap | 400–600 (boxy) ; HPF 300–500 sur perc | 3–4 kHz | étroit (±20 %) | [COMM] |
| hats / rides / shakers | 6–12 kHz | HPF 3 kHz (house) / 5 kHz (UKG) / 6–8 kHz (techno) ; shelf −1,5 dB 12 kHz si fatigant | 10–12 kHz | large (±50–80 %) | [COMM] ; [DÉPÔT] `diagnostics.md` |
| FX / risers / reverb returns | noise 200 Hz → 10 kHz ; crash 5–15 kHz HPF 500 | HPF 150–200 sur les retours, LPF 6–8 kHz si sombre | — | large | [COMM] |
| master | — | 200–300 Hz si boueux ; HPF < 20 Hz (infrasons) | shelf +1–2 dB > 8 kHz (air) | — | [COMM] techno, trance, MPW |

### 3.2 Traitements par famille

- **Leads future rave / big room** : 5–7 dents de scie détunées ±10–30 cents [COMM] ; « saturated supersaw leads, distorted yet controlled » [DOC-EXTRAIT] ; chorus, plate/hall courte, sidechain, élargissement ; largeur **maximale dans le drop, plus étroite en intro/outro pour le DJ** [COMM] ; reverb/delay dans le drop : HPF des retours 150–200 Hz et ducking du retour par le signal sec [COMM] ; contrôle 200–400 Hz en dynamique (soothe3 / Pro-Q 4 dyn) plutôt qu'en statique quand le lead joue des accords [HEUR].
- **Basses bass house** : trois couches (§2.1), distorsion sur la mid seulement, multibande 60–120 Hz avec lookahead [DOC-EXTRAIT], mono < 150 Hz, kick « perdu derrière la basse » = sidechain + EQ [COMM].
- **Vocals** : chops = texture, pas lead (tech house) ; pitch ± octave = design (axe voix) ; « reverb throw » = envoi automatisé sur le dernier mot + retour sidechainé au vocal sec [COMM] MPW ; présence 2–4 kHz, HPF 200 [COMM].
- **Hats/claps** : transitoires préservés (attaque de compresseur lente 10–25 ms sur pistes, 15–40 ms sur bus) [COMM] MPW compression ; F6 bande dynamique 6–7 kHz au master si agressif [DÉPÔT] `diagnostics.md`.

### 3.3 Densité du drop, sidechain global vs par élément, largeur par bande, automation

- Combien d'éléments : les fiches ne donnent pas de nombre ; règles déclarées : « too many elements » = erreur en deep house, « minimalism is the point » en gqom, drops bass house « strip back to kick and bass » [COMM] bitwize. Proposition [HEUR] pour ces genres : dans le drop, **un seul porteur par bande** (sub ; kick ; basse mid ; lead ; stab/chords ; vocal ; hats ; FX) = 6–8 familles, chaque nouvelle couche d'un lead remplaçant du spectre plutôt que s'y ajoutant (couche large HPF 300 Hz, couche centrale sans air).
- « Gros sans boue » [COMM] : HPF de tout sauf kick/basse à 80–120 Hz (techno, progressive) ; creux 200–400 sur pads/supersaws ; sidechain de tout au kick (electro) ; **parallèle** plutôt que série pour la densité (API-2500 30–60 % déjà dans le dépôt [DÉPÔT]).
- Sidechain global vs par élément : MPW — pomper un bus **déjà compressé** ou le master est une erreur (dynamique et mono) ; HPF de détection 80–120 Hz sur le bus [COMM] ; french touch = tout pompé (esthétique) [COMM]. Proposition [HEUR] : par élément (sub, basse mid, lead, pads) avec profondeurs différentes, jamais sur BUS MASTER.
- Largeur par bande [COMM] techno : centre = kick, sub, fondamentale des stabs ; ±20 % clap/perc ; ±50–80 % hats/rides/retours ; MPW : empiler élargissement au mix **et** au master sans contrôle mono = master creux sur enceinte Bluetooth mono.
- Automation par section [COMM][DÉPÔT] : contraste breakdown/drop borné (§1.3) ; largeur réduite en intro/outro ; les corrections de niveau par section passent par `live-automation` [DÉPÔT] ; ST −18/−20 en intro contre −10/−12 en section forte (streaming) [COMM].

---

## 4. Bus et master

### 4.1 Ordre de chaîne (consensus des sources)

`HPF < 20 Hz → EQ correctif → compression/glue → EQ tonal → stéréo (M/S) → saturation → clipper → limiteur true peak → mesure` [DOC-EXTRAIT] twisby, El Stray, audiospectra ; [COMM] MPW (avec une **deuxième passe d'EQ** après compression). Règle dure : rien après le limiteur sauf la mesure [DOC-EXTRAIT]. La chaîne du dépôt suit cet ordre sur trois bus [DÉPÔT] `effets-plugins/references/chaine-actuelle.md` (Pro-Q 4 → bx_glue → J37 → API-2500 parallèle → Imager → TBC/SPAN → L2).

### 4.2 Réglages de départ

| étage | valeur de départ | source |
|---|---|---|
| glue de mix bus | 2:1–3:1, attaque 30–60 ms, release 200–400 ms ou auto, **1–2 dB GR**, HPF de détection 80–100 Hz | [COMM] MPW mastering (House) & compression |
| bus batterie | attaque 15–40 ms, release 150–300 ms, 4–8 dB GR max ; tech house 3–4 dB GR + parallèle ; electro 4–6 dB ; peak-time techno 4–6 dB attaque rapide | [COMM] |
| bus basse (bass house) | 4–6 dB GR ; multibande/limiteur 4–6 dB **seulement 20–80 Hz** au master si les crêtes viennent du sub | [COMM] |
| multibande master | seulement si le comportement varie par zone ; ne pas empiler EQ dyn + résonances + multibande | [DÉPÔT] `waves-mastering.md` |
| clipper | après EQ, avant limiteur ; hard clip convient à l'EDM ; **ne pas clipper le grave** (HPF avant clipper ou clipper multibande) ; but : le limiteur travaille moins, kick garde le punch | [DOC-EXTRAIT] masteringthemix, newfangled, gearspace ; [COMM] JefroB electro « use clipping before limiting » |
| limiteur | ceiling −1,0 dBTP (−2 pour Amazon/YouTube si demandé) ; **2–4 dB GR** sur le drop (techno) ; si > 4–5 dB de GR nécessaire, remonter le mix ; mode True Peak/oversampling | [COMM] ; [DOC-EXTRAIT] iZotope |
| dither | aucun en 24 bits ; TPDF seulement pour un 16 bits final, une seule fois, coordonné avec le limiteur (IDR du L2) | [COMM] MPW ; [DÉPÔT] `mesures-et-livraison.md` |
| export | 24 bits, sans normalisation, fréquence du projet | [DÉPÔT] `live-export-wav` |

### 4.3 Clipping vs limiting en EDM

Tous les articles trouvés convergent [DOC-EXTRAIT] : le clipper rase les transitoires (kick, snare) sans pompage, le limiteur gère le reste ; ordre clipper → limiteur ; risque = grave écrêté (boue) → filtrer ou clipper par bande. Aucune valeur chiffrée fiable de « dB de clip » n'est publiée ; en pratique 1–3 dB de clip sur le drop puis 2–4 dB de limiteur [HEUR]. **Outils locaux** : aucun clipper dédié dans la liste ; L4 possède un contrôle **Clip** d'allocation [DÉPÔT] `waves-mastering.md` ; RazorClip repéré mais non documenté [DÉPÔT] `inventaire-local.md` ; J37 en entrée forte agit en soft clip/compression [DOC] ; Saturator natif interdit par la règle 6 [DÉPÔT].

### 4.4 Qui masterise Guetta, Garrix, Chris Lake, Jauz, Dom Dolla, MORTEN

**Non documenté par les sources accessibles** : les recherches (SoundBetter, Wikipédia « So Far Away », « Like I Do », EDM.com) ne nomment pas d'ingénieur de mastering ; SOS « Martin Garrix: Superstar DJ » (bloqué ici) est la seule interview d'ingénierie identifiée — à télécharger depuis le Mac. Pistes : crédits Tidal/Apple (« mastered by ») et Discogs pour chaque single ; ne rien affirmer dans le skill sans ces crédits.

### 4.5 Références A/B et contrôle mono/club

- Comparer à niveau égal : REF → Main hors limiteur, TBC 3 [DÉPÔT] ; L4 **Gain Match** (désactive Ceiling : quitter avant export) [DÉPÔT] `waves-mastering.md` ; MPW : « toujours A/B à sonie appariée » [COMM].
- Mono/club : sub sommés mono dans les clubs [DOC-EXTRAIT] ; « vérifier le kick en mono, référence club mono » [COMM] ; corrélation SPAN, Utility mono toléré [DÉPÔT] `outils.md` ; sidechain lié L/R [COMM].

---

## 5. Correspondance avec les outils de l'utilisateur

Inventaire, pilotage et fiches : [DÉPÔT] `mixage/references/outils.md`, `effets-plugins/references/fiches.md`, `mastering-outils/references/inventaire-local.md`, `waves-mastering.md`, `outils-et-reglages.md`. Le tableau n'ajoute que ce qui vient de cette recherche.

| tâche | natif Live (statut règle 6) | tiers de la liste | réglage de départ | étiquette |
|---|---|---|---|---|
| coupe-bas / EQ correctif par piste | EQ Eight (interdit) | **REQ 6** (API) ; Pro-Q 4 (fenêtre) | kick HPF 30 Hz (40–50 si le sub tient le grave [DÉPÔT]) ; sub HPF 25 / LPF 80 ; basse mid HPF 80 ; top de basse HPF 300 ; supersaw HPF 150–200 + creux 200–400 ; hats HPF 3–8 kHz ; tout le reste HPF 80–120 | [COMM] |
| résonances / boue dynamique (lead, bus harmonie) | — | **soothe3** (source), Pro-Q 4 Make Dynamic, **F6** (6 bandes flottantes, M/S, sidechain externe [DOC]), TDR Nova | bande 200–400 Hz, −2 à −4 dB dynamiques sur supersaws/pads ; F6 : bande 6–7 kHz au master si agressif | [COMM][DÉPÔT] |
| sidechain kick → sub / basse / lead | **Compressor natif** déjà en place (toléré) ; Shaper/LFO M4L = nouveau natif → hors règle | **bx_glue** (Ext. + Int. Gain + HPF Hz [DOC]), **API-2500** S/C, **Pro-C 3** (sidechain filtré) | attaque 0,1–1 ms (pump) / 5–20 ms (transparent) ; release 50–150 ms, ≤ 469 ms à 128 BPM ; ratio 4:1–10:1 ; 4–12 dB sur la basse, 2–4 dB « invisible » ; HPF détection 80–100 Hz sur bus | [COMM] |
| volume shaper (courbe dessinée) | Utility (toléré) + **automation de gain** (`live-automation`) — remplace LFO Tool/Kickstart/ShaperBox absents | — | courbe par noire : creux −6 à −12 dB, retour en 60–70 % du temps [HEUR] | [DOC-EXTRAIT][HEUR] |
| mono du grave | Utility (toléré) | **bx_glue Mono Maker** (bus BASSES) ; Imager 2 par bande (fenêtre) ; Waves Center/S1 | 120 Hz (house, dépôt) ; 150 Hz bass house ; 200 Hz = valeur haute contradictoire | [COMM][DÉPÔT] |
| saturation sub/basse/kick | Saturator (interdit) | **J37** 7,5 ips, entrée −3–0 VU, 815 → 888 pour plus de sale [DOC] ; bx_glue XL ; Abbey Road Saturator (inventaire) | drive « 5–15 % » soft clip équivalent ; ne saturer que la couche mid | [DOC][DOC-EXTRAIT] |
| multibande basse / master | Multiband Dynamics (interdit) | **F6** (EQ dyn), **L3 Multi/L3-16**, LinMB/C4/C6 (inventaire, à prober) | 20–80 Hz : 4–6 dB de réduction uniquement si les crêtes viennent du sub ; 60–120 Hz attaque rapide sur la basse | [COMM][DÉPÔT] |
| glue de bus | Glue Compressor (interdit) | **bx_glue** (2:1, 30 ms, auto, SC HP 99 Hz déjà réglé [DÉPÔT]) ; **API-2500** (Thrust = HPF au détecteur RMS [DOC] `api-2500-pdf-texte.md`) | 1–2 dB GR mix bus ; 3–6 dB bus batterie selon genre ; release 200–400 ms ou auto | [COMM][DÉPÔT] |
| parallèle / densité | — | **API-2500** mix 30–60 % (Thrust Med/Loud pour ne pas pomper sur le kick) | 10:1, 1 ms, Hard, 30 % sur batterie (dépôt) | [DÉPÔT] |
| clipper | Saturator (interdit) | **L4** (Clip) ; RazorClip (à prober) ; J37 entrée forte | 1–3 dB de clip sur le drop [HEUR] ; HPF avant si le grave s'écrase | [DÉPÔT][DOC-EXTRAIT] |
| limiteur | Limiter (interdit) | **L2** (Thresh, Ceiling, Release, ARC, IDR [DÉPÔT]) ; **L4** (True Peak, Gain Match [DÉPÔT]) ; **Ozone Elements Maximizer** (True Peak = suréchantillonnage [DOC-EXTRAIT]) ; WLM Plus (limiteur TP) | ceiling −1,0 dBTP ; seuil pour 2–4 dB GR sur le drop ; club −8/−7 int., streaming −10/−11 int. ou −14 | [COMM][DOC-EXTRAIT] |
| largeur | Utility width (toléré) | **Imager 2** (Width global API, bandes en fenêtre) ; S1 | +8 % global (dépôt) ; leads/hats élargis, jamais < 120 Hz ; intro/outro plus étroits | [DÉPÔT][COMM] |
| mesure LUFS/TP/LRA | — | **Insight 2** (bout de Main), **WLM Plus** (mesure seule : Gain 0, pas de Trim, limiteur off [DÉPÔT]) ; hors Live : pyloudnorm / ffmpeg ebur128 si installés | I, ST max (drop), ST min (break), TP, LRA, PLR = TP − I | [DOC][DÉPÔT] |
| équilibre tonal vs référence | — | **TBC 3** + courbe cible ; SPAN Avg 4000 ms | corriger la tonalité avant la dynamique [DÉPÔT] | [DÉPÔT] |
| couleur master | — | **TG Mastering Chain** (mode Limit ≠ brickwall [DÉPÔT]) ; J37 | après EQ, avant limiteur | [DÉPÔT] |

---

## 6. Ce que le dépôt sait déjà (cité, non répété)

- `mixage/references/outils.md` : tableau tâche → premier choix → pilotage ; `diagnostics.md` : boueux/agressif/mince/pompe → mesure → remède, vu-mètres API sous-estiment les crêtes de 2–4 dB.
- `kick-bass-equilibre/references/roles.md` et `mesure.md` : matrice sub/kick, accord F → 43,7 Hz, corrélation 30–120 Hz, `kick_bass_check.py`, pièges (accord mesuré sur la queue).
- `live-mix-mastering/` : phases, prémaster (pas de −6 dBFS obligatoire), `mastering-mesures.md` (dBFS vs dBTP vs LUFS vs LRA), `notes-locales.md` (chaîne en place, ffmpeg absent, cibles indicatives −14 streaming / −9 à −7 club).
- `mastering-outils/` : fiches L4 (Gain Match désactive Ceiling), L2/L3, WLM Plus, TG (Limit ≠ brickwall), F6, LinMB/C4/C6, API-2500, Imager, Insight/SPAN/TBC ; inventaire V16/V17 ; commande ffmpeg `ebur128=peak=true`.
- `effets-plugins/references/chaine-actuelle.md` : valeurs éprouvées (bx_glue, API-2500, J37, Imager, L2 −5,1/−0,4) sur « deep chill minimal house » — point de départ à durcir pour ces genres (GR de bus 3–6 dB, clipper avant L2, ceiling −1,0).

## 7. Manques et suites

1. Mesures réelles du genre (I, TP, PLR, ΔST drop/break) : à faire localement (§1.4) ; aucune base publiée trouvée (les dépôts GitHub trouvés sont des *outils* de mesure, pas des jeux de données).
2. Ingénieurs de mastering des artistes cités : non documentés ici ; crédits à lire depuis le Mac (SOS Garrix, Wikipédia, Tidal/Discogs).
3. Réglages exacts LFO Tool/Kickstart/ShaperBox : outils absents ; le skill doit décrire l'équivalent automation Utility (toléré) ou proposer, si l'utilisateur relâche la règle 6, Shaper/LFO M4L.
4. Ozone Elements : modules réels à confirmer dans la version 12.1 (EQ, Imager, Maximizer, assistant) avant de lui attribuer une fonction [DÉPÔT] `outils-et-reglages.md`.
5. Pages de blog à télécharger et à vérifier : `urls-axe5.json` (≈ 70 URL, sans YouTube).

## 8. Documents ajoutés au corpus (`corpus/house-future-rave/`, texte intégral, en-tête YAML)

jefrob-genre-house-{mixing-and-mastering, sound-design, production-techniques}.md ; jefrob-genre-techno-mixing-and-mastering.md ; jefrob-genre-trance-mixing-and-mastering.md ; bitwize-genre-{bass-house, future-house, tech-house}-readme.md ; musicproductionwiki-bible-{sidechain, loudness, mastering, mixing, compression}.md ; musicproductionwiki-tools-stereo-width-ms.md ; pyloudnorm-readme.md ; ffmpeg-filters-loudnorm-ebur128.md. Rappel : `scripts/build_index.py` à relancer pour `INDEX.md`/`index.json` (non fait ici : aucun commit, rien d'autre touché).
