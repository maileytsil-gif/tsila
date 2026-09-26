---
name: house-future-rave-bass-house-production
description: Produire un titre de future rave, bass house, future house, tech house, big room ou house de club dans Ableton Live 12 de bout en bout — genres et éléments constitutifs d'un track, méthode de production professionnelle, sound design (supersaw future rave, basse sub + mid, kick de festival, drop bass house trois couches, basse FM, talking bass, basse tech house rolling, stabs, organ bass et piano M1, risers), arrangement (club mix, radio edit, extended, DJ tool), théorie propre au genre (tonalités, grilles 16 pas, swing), mixage et mastering (sidechain, grave, deux masters club et streaming) — avec six producteurs de référence : David Guetta, MORTEN, Martin Garrix, Chris Lake, Jauz, Dom Dolla. Utilise ce skill dès que l'utilisateur parle de future rave, bass house, house, tech house, future house, big room, festival, « un drop à la Guetta », « une basse à la Jauz », « un groove à la Chris Lake / Dom Dolla / Fisher », « un lead à la Garrix », Animals, Titanium, Kill Me Slow, Rock The Party, San Frandisco, Turn Off The Lights, build, drop, breakdown, club mix, extended, radio edit, master club, pump — même en deux mots. Faits avec preuves [DOC]/[DOC-2]/[DOC-EXTRAIT]/[HEUR]/[CALC]/[TEST], corpus local `corpus/house-future-rave/`, recettes Serum 2 et natives chiffrées, validation mesurée. S'appuie sur sound-designer-serum, vst-sound-design, arrangement-avance, theorie-musicale-electronique, drums-signature, kick-bass-equilibre, ingenieur-mixage, live-mix-mastering, mastering-outils, live-automation.
---

# House, future rave, bass house — production — v1

Ce skill fait un titre **qui tient dans un set** : un drop qui frappe plus fort que le build sans être seulement plus fort, une basse qui groove seule avec le kick, un lead lisible en trois notes, un arrangement qu'un DJ peut mixer, deux masters mesurés. Il prend six producteurs comme **références d'écoute et de méthode**, sans revendiquer aucune affiliation et sans jamais présenter un réglage comme « le son de » l'un d'eux : aucune page lue ne chiffre leurs patchs. Il suit les règles communes des rôles (`../sound-designer-serum/SKILL.md`) et la méthode en huit étapes de `../ableton-live-session/SKILL.md` : capacités vérifiées, session préservée (anti hot-swap), chaque réglage relu, jamais « entendu » sans mesure.

## Ordre de lecture obligatoire
1. `references/genres-et-elements.md` — les cinq familles en dates, tableau comparatif (tempo, swing, tonalités, harmonie, durées, sonie, contraste, zone dominante), les éléments d'un track genre par genre, titres à écouter.
2. `references/six-producteurs.md` — parcours, outils, signatures, arrangement, méthode, mix, théorie de Guetta, MORTEN, Garrix, Chris Lake, Jauz, Dom Dolla ; ce qui n'est **pas** établi.
3. `references/theorie-specifique.md` — tempos et tonalités mesurés sur données, harmonie en degrés et en notes, riffs, grilles de basse et de batterie en 16 pas avec vélocités, gate et swing.
4. `references/arrangement-et-methode.md` — structures club et radio, Harmonix Set (seules structures vérifiées), dispositifs de build et de drop, méthode pro calée sur les huit étapes, livraison.
5. `references/sound-design-genres.md` — vingt-neuf sons avec les noms exacts de Serum 2, puis la recette de `recipes/`.
6. `references/mixage-mastering.md` — cibles de sonie, grave, spectre, bus et master, outils de ce Mac.
7. `references/protocole-de-validation.md` puis `references/schema-de-sortie.md`.

## Système de preuve
- **[DOC]** : document lu en entier (manuel, jeu de données Harmonix / GiantSteps / WhatBPM / Spotify archivé, copie Wikipédia, fichier du dépôt).
- **[DOC-2]** : compilation secondaire lue en entier (dotbeat, amen-sessions) qui cite sa source primaire ; **[COMM]** : fiche communautaire lue (JefroB, bitwize, Music Production Wiki), convention déclarée et non mesure.
- **[DOC-EXTRAIT]** : résumé d'une page bloquée depuis le conteneur (Sound On Sound, MusicTech, MusicRadar, Billboard, EDM.com…) ; **aucune citation n'est vérifiée mot pour mot** tant que la page n'a pas été relue depuis le Mac.
- **[DOC-Spotify]** : « audio feature » algorithmique ; la tierce et la relative peuvent être fausses.
- **[HEUR]** / **[HEUR-lu]** : pratique ou déduction, avec sa logique ; **[CALC]** : arithmétique ; **[TEST]** : à mesurer dans le Set ; **[NON VÉRIFIÉ]** et **MUET** : rien de lu.
Ne jamais transformer une plage `[HEUR]` ou `[COMM]` en règle, ni une paraphrase `[DOC-EXTRAIT]` en citation.

## Ce que le skill a décidé (contradictions tranchées)
- **Tempo** : future rave, bass house, big room **128** ; tech house **126** en club, 128 en festival ; house de club 122–126 `[DOC WhatBPM ; HEUR]`.
- **Swing** : future rave et big room **droits (50 %)** ; tech house **52–55 %** sur basse, hats et percs, jamais sur le kick ; bass house : deux écoles (droite pour le festival, 55–65 % pour Night Bass / UK bassline), choisir une et s'y tenir.
- **Tonalité** : mineur dans ≈ 85 % des cas `[DOC GiantSteps]` ; fa♯ mineur récurrent chez Guetta & MORTEN, fa mineur pour « Animals » `[DOC-Spotify]` ; aucune tierce sous C2 (48).
- **Grave** : trois architectures, une par genre — **kick porteur** (big room, future rave : le kick saturé tient 50–80 Hz, la basse s'écarte), **sub tenu** (tech house, deep : sub propre, kick court), **sub dédié + basse mid** (bass house : sub sinus mono sous 100 Hz, la couche mid distordue porte le hook) (`mixage-mastering.md` § 2).
- **Deux masters** : **club / Beatport −8 à −7 LUFS intégrés** (big room et future rave jusqu'à −6,5), TP −1,0 dBTP ; **streaming −10 à −11**, TP −1,0 (−2 si la plateforme l'exige). Si le LUFS visé exige plus de 4–5 dB au limiteur, c'est le mix qu'on remonte.
- **Structures** : blocs de 8, événement toutes les 8, gros changement toutes les 16 ou 32 ; seule la formule pop-EDM de Guetta est vérifiée (Titanium : refrain chanté 16 → drop instrumental **8**, trois fois) `[DOC Harmonix]` ; les autres minutages sont `[HEUR]` et se mesurent sur une référence dans la piste REF.

## Recettes
| Besoin | Recette |
|---|---|
| Structure future rave, club mix | `recipes/arrangement-future-rave-club-mix.md` |
| Structure bass house (160 mesures) | `recipes/arrangement-bass-house-160.md` |
| Structure tech house, DJ tool | `recipes/arrangement-tech-house-dj-tool.md` |
| Radio edit et extended à partir du même Set | `recipes/radio-edit-et-extended.md` |
| Lead future rave (supersaw « déguisée en basse ») | `recipes/lead-future-rave-supersaw-basse.md` |
| Basse future rave sub + mid | `recipes/basse-future-rave-sub-et-mid.md` |
| Kick de festival et kick future rave | `recipes/kick-festival-et-future-rave.md` |
| Drop bass house en trois couches (Jauz, Malaa, AC Slater) | `recipes/drop-bass-house-trois-couches.md` |
| Basse FM métallique (future house, bass house) | `recipes/basse-fm-metallique-bass-house.md` |
| Talking bass, formants, « yoi » | `recipes/talking-bass-formants.md` |
| Basse tech house rolling (Chris Lake, Fisher, Dom Dolla) | `recipes/basse-tech-house-rolling-chris-lake.md` |
| Stabs et accords house, tech house, future rave | `recipes/stabs-house-et-tech-house.md` |
| Organ bass et piano house (Korg M1) | `recipes/organ-bass-et-piano-house-m1.md` |
| Lead big room supersaw (Garrix) | `recipes/lead-big-room-supersaw.md` |
| Risers, impacts, downlifters, vocal risers | `recipes/risers-impacts-downlifters.md` |
| Sidechain et pump par genre | `recipes/sidechain-et-pump.md` |
| Master club et master streaming | `recipes/master-club-et-streaming.md` |

## Les six producteurs : ce qu'on leur prend
| Producteur | Référence pour | À écouter |
|---|---|---|
| **David Guetta** | forme pop-EDM vérifiée (refrain 16 → drop 8), radio edit + extended systématiques, voix « meticulously placed », future rave depuis 2019 | Titanium, Kill Me Slow, I'm Good (Blue) |
| **MORTEN** | le lead « techno pitché » et le drop dur de la future rave, gabarit 126–128, fa♯ / si mineur | Never Be Alone, Polar, Kill Me Slow |
| **Martin Garrix** | drop big room = kick + un seul riff (« how little is actually there »), FL Studio + Sylenth1, mixe et masterise 98 % de ses sorties | Animals, Tremor, High On Life |
| **Chris Lake** | commencer par le grave, vocal chop en ostinato, arrangement par drop-outs, Ableton Live | Turn Off The Lights, Operator (Ring Ring) |
| **Jauz** | la basse **est** le hook, drop réduit à kick + basse, resampling dans Serum, Ableton Live | Feel The Volume, Rock The Party |
| **Dom Dolla** | un seul chop « stabbé » contre le temps, riff de basse revoisé et filtré à chaque passage, maîtriser un plug-in avant le suivant | Take It, San Frandisco, Saving Up |
Écouter une référence = la poser dans la piste REF au même tempo, à niveau égal, et compter les mesures ; jamais citer un chiffre de leur studio qui n'est pas dans `six-producteurs.md`.

## Ordre de production (les huit étapes, version house)
1. **Cadre** : Sauver sous, tempo, tonalité, référence dans REF ; **grille en repères et courbe d'énergie par 8 mesures avant toute note** (`arrangement-et-methode.md` § 3, `../arrangement-avance/SKILL.md`, `../memoire-projet/SKILL.md`).
2. **Grave d'abord** : choisir l'architecture du grave, kick puis basse, accordés et vérifiés (`../kick-bass-equilibre/SKILL.md`, `kick_bass_check.py`) ; batterie depuis `theorie-specifique.md` § 5 et `../drums-signature/SKILL.md`.
3. **Le drop en premier**, boucle de 8 mesures : kick + basse + un motif de trois notes au plus ; tester qu'il groove sans rien d'autre.
4. **Arrangement par soustraction** depuis le drop, une vraie section contrastante, trois à cinq dispositifs par couture, deux vrais silences, second drop **différent** (+1 couche, +1–2 st ou variation), jamais seulement plus fort.
5. **Mix** : bus, sidechain par genre, grave mono sous 120 Hz, comparaison à niveau égal (`../ingenieur-mixage/SKILL.md`).
6. **Automations** : filtres de bus, sends, largeur, « à l'intérieur des notes » (`../live-automation/SKILL.md`).
7. **Voix** : chop de 1–4 mesures verrouillé sur kick et basse, ou toplines placées (`../suno-vocals/SKILL.md`).
8. **Master et export** : deux masters mesurés sur le fichier exporté (`../live-mix-mastering/SKILL.md`, `../mastering-outils/SKILL.md`, `../live-export-wav/SKILL.md`).
Une étape par échange ; journal dans la mémoire du projet à chaque fin d'étape.

## Choix du moteur
- **Serum 2** : supersaw, basses FM et mid, talking bass (filtres formants, MIX), multisample M1 ; réglages par clics et captures (`../sound-designer-serum/references/serum2-cartographie.md` pour les noms exacts).
- **Live 12 natif** : Operator (basse FM, organ bass additif, kick sinus), Wavetable (supersaw unison Classic, basse tech house filtre 12 dB), Analog, Drift, Simpler/Sampler (piano et orgue M1), Drum Rack ; tout relisible par `ppal-read-device` (`../vst-sound-design/SKILL.md`).
- Préférer le natif quand la reproductibilité compte ; Serum 2 quand la recette le chiffre.

## Exigences de sortie
Toute réponse suit `references/schema-de-sortie.md` (dix rubriques : cible, éléments, structure, théorie, sons, méthode, mix, vérification, références producteurs, limites). Ne jamais déclarer un drop, une basse ou un master « prêt », « pro » ou « club » sans : kick + basse testés seuls et en mono, drop comparé à une référence à niveau égal, second drop différent du premier, intégré / TP / LRA / short-term du drop et du breakdown mesurés sur l'export.

## Corpus documentaire local
Tout ce qui a été lu est dans `../../../corpus/house-future-rave/` : les six rapports de recherche (axes genres, producteurs, sound design, arrangement, mix-mastering, théorie), le Harmonix Set, GiantSteps, WhatBPM, les données Spotify et Beatport, les fiches communautaires, pyloudnorm et ffmpeg ebur128. Lire le fichier local avant de chercher en ligne. Les pages bloquées (Sound On Sound « Inside Track », MusicTech, MusicRadar « Anatomy of a hit », EDMProd…) sont listées dans `../../../corpus/sources-a-telecharger-house.json` : à télécharger sur le Mac (`python3 corpus/scripts/fetch_sources.py --dossier house-future-rave`), puis relire avant toute citation. Qwen/Ollama : `python3 corpus/scripts/ask_corpus.py "…"` indexe aussi ce skill.

## Passer la main
Un son seul hors de ces recettes → `sound-designer-serum` puis `vst-sound-design` ; grille harmonique ou mélodie à écrire → `compositeur-arrangeur` et `theorie-musicale-electronique` ; batterie et groove → `producteur-rythmique` et `drums-signature` ; minutage, repères, Insérer Silence → `arrangement-avance` ; le grave se bat → `kick-bass-equilibre` ; masquage, diagnostic → `ingenieur-mixage` ; LUFS, true peak, livraison → `live-mix-mastering`, `mastering-outils`, `live-export-wav` ; référence audio à analyser → `synthese-reference` ; cuivres de festival ou horn stabs → `studio-grade-brass-sound-design` ; vélocités et gate → `midi-expressif` ; genres hors de ce skill (techno, afro house, melodic, dubstep, DnB), robotic bass et vocoder, reverse et pré-FX, QC « label-ready » et livraison complète → `electronic-production-engineer` (son ADN bass house, `references/genres/bass-house.md`, complète celui-ci par quatre références d'écoute : Skrillex & Habstrakt, JOYRYDE, Knock2, AC Slater).
