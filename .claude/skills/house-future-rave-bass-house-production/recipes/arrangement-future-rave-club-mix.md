# Arrangement future rave, club mix de 208 mesures à 128 BPM

## Cible
`FUTURE RAVE / club et festival / 128 BPM / fa♯, fa ou la mineur / 6:30 / références : Guetta & MORTEN « Kill Me Slow », « Detroit 3 AM »`

Les longueurs propres au genre ne sont vérifiées par aucune source `[NON VÉRIFIÉ]` : la grille est le gabarit club à deux drops des fiches lues, calé sur la définition du genre. Avant de figer, mesurer une référence dans la piste REF (repère à chaque changement, `arrangement_map.py`).

## Grille et repères (à poser à l'étape 1, `lom.py locator`)

| Repère | Mesure | Minute | Longueur | Ce qui s'y passe |
|---|---|---|---|---|
| Intro | 1 | 0:00 | 32 | kick filtré, hats en croches dès m1, open hat m9, clap m17, percs m25 ; filtre passe-bas de bus qui s'ouvre sur 16 ; pas de sub |
| Break 1 | 33 | 1:00 | 16 | thème filtré, accords add9/sus tenus, basse roulante filtrée sous 300 Hz, voix en fragments |
| Build 1 | 49 | 1:30 | 16 | riser passe-bande 200 Hz → 8 kHz, snare roll croches → doubles → triples, hats accélérés, HP de bus jusqu'à 400–800 Hz sur les 4 dernières mesures, kick retiré 4–8 mesures avant, sus4 sur les 2 derniers temps, **gap d'un temps** |
| **Drop 1** | 65 | 2:00 | 32 | impact + crash + sub-drop sur le un ; kick long saturé + sub + basse roulante + rave stabs (1, et de 2, 3, et de 4) + lead supersaw ; variation de 2 mesures toutes les 8 ; hit FX toutes les 16 |
| Breakdown | 97 | 3:00 | 32 | batterie retirée, nappe et voix exposées avec reverb, lead seul en mélodie, **kick fantôme** qui garde le sidechain ; −6 à −10 LU sous le drop ; pas de sub |
| Build 2 | 129 | 4:00 | 16 | plus court possible (8) ; mêmes dispositifs, riser différent |
| **Drop 2** | 145 | 4:30 | 32 | drop 1 + une couche (contre-mélodie à l'octave inférieure dans les trous du lead, ou lead +12 sur la note centrale, ou percussion), image plus large ; jamais seulement plus fort |
| Outro | 177 | 5:30 | 32 | soustraction inverse de l'intro ; filtre passe-bas qui se ferme sur 16 ; kick seul à la fin |
| FIN export | 209 | 6:31 | | |

Énergie par section : 2–3 · 4 · 5 → 8 · 10 · 5 → 3 · 5 → 9 · 10 · 10 → 2.

## Éléments
Voir `../references/genres-et-elements.md` § 3.1 (kick, sub, basse roulante ou reese, rave stabs, lead supersaw, arpège, nappes, voix, hats et clap droits, percussions minimales, FX). Trois couches actives au drop : lead, basse, stabs ; hats en croches sans swing ; le groove est dans les stabs et le sidechain.

## Théorie
Fa♯ mineur (Kill Me Slow, Detroit 3 AM) ou la mineur ; i–VI–VII ou i tenu ; stabs en quintes et add9 (`../references/theorie-specifique.md` § 2.1) ; basse off-beat 1/8 ou rolling 1/16 première double vide ; lead motif de 2 mesures, climax à la mesure 7.

## Ordre de travail (huit étapes)
1. Sauver sous, tempo 128, tonalité, repères ci-dessus, courbe d'énergie sur une piste factice.
2. Kick (`../recipes/` kick future rave) puis basse puis lead : la relation kick-basse d'abord.
3. Boucle de 8 mesures du **drop** complète (kick, sub, basse, stabs, lead, hats, clap).
4. Dériver intro, break, build et breakdown par soustraction ; drop 2 par ajout d'une couche.
5. Mix : un porteur par bande, sidechain par élément, master club et streaming (`master-club-et-streaming.md`).
6. Automations sur bus (filtres), largeur réduite en intro et outro.
7. Voix : hook au breakdown, chops au drop.
8. Export club, puis radio edit (`radio-edit-et-extended.md`).

## Vérification
`arrangement_map.py` après chaque édition ; test de soustraction à chaque bloc de 8 ; gap avant chaque drop ; sub absent hors des drops ; drop 2 différent, pas plus fort.
