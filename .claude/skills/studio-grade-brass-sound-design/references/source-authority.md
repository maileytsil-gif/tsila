# Autorité des sources — cuivres

Priorité : donnée d'usine décodée ou code source > documentation constructeur > manuel ou traité de référence > article de référence (Sound On Sound) > notes de tiers lues > extrait de recherche (page non lue) > mémoire.

Condition de lecture de cette session (24 septembre 2026) : le conteneur cloud n'atteint que GitHub. Les manuels Ableton, Xfer, Native Instruments, Waves, FabFilter, iZotope, oeksound et les sites Sound On Sound, Wikipédia, Attack, ADSR, PML, Reverb Machine sont **bloqués** ; leurs pages n'ont été connues que par extraits `[DOC-EXTRAIT]` / `[HEUR-extrait]`. Les copies intégrales trouvées sur GitHub (manuel Live 12, Synth Secrets, ROM DX7, patchs d'usine) sont `[DOC]`. Tout est conservé dans `../../../../corpus/` ; les pages bloquées sont listées dans `../../../../corpus/sources-a-telecharger.json` pour être relues sur le Mac (`corpus/scripts/fetch_sources.py`).

## Acoustique et synthèse classique [DOC]
- Gordon Reid, *Synth Secrets* 23 (formants), 24 (vents), 25 (cuivres), 26 (Minimoog), 27 (SH-101, ARP Axxe), 8 et 10 — texte intégral : `corpus/synth-secrets/synth-secrets-23.md` … `-27.md` ; origine https://www.soundonsound.com/series/synth-secrets-sound-sound
- Yan Maresz (CNSMDP), *Référence formantique de l'orchestre*, 2026 — `corpus/cuivres/maresz-2026-formants-orchestre.md`
- Mémoire LAUM (Gilbert, Dalmont), son cuivré et ondes de choc — `corpus/cuivres/olympiades-2009-son-cuivre-tuyau.md`
- Chowning 1973 par trois transcriptions concordantes (Csound, musx, CLM) — `corpus/synthes-vintage/csound-tutorial-chowning-brass-bell.md`, `clm-fm-schottstaedt.md`, `csound-book-1115-brass-chowning.md`
- STK `Brass.cpp`, Faust `physmodels.lib` — `corpus/cuivres/stk-brass-model.md`, `faust-physmodels-brass.md`
- Tessitures : MuseScore `instruments.xml`, music21, Abjad — `corpus/cuivres/musescore-instruments-tessitures-cuivres.md`
- Articulations : MusicXML 4.0, SMuFL, LilyPond — `corpus/cuivres/musicxml-4-articulations-sourdines.md` et fichiers voisins
- Rimsky-Korsakov, *Principles of Orchestration* (Gutenberg 33900) — `corpus/cuivres/`

## Patchs d'usine et presets décodés [DOC]
- Yamaha DX7 ROM1A (BRASS 1-3 et 29 autres voix) — `corpus/synthes-vintage/dx7-rom1a-32-voix-decodees.md`
- Roland Juno-106 (128 patches) et Juno-60 (56 chartes) — `corpus/synthes-vintage/roland-juno-106-patches-usine-amy.md`, `roland-juno-60-chartes-usine-phosphor.md`
- Surge XT dossier « Brass » (8 patchs), presets Vital (12), synthdefs vibelang (5) — `corpus/cuivres/`
- Corpus des 626 presets d'usine Serum 2 (contenu Brass/Winds) — `corpus/cuivres/`
- Presets OB-Xd « Jump » et Hydrasynth — `corpus/synthes-vintage/` [HEUR : communautaires]

## Constructeurs
- Ableton Live 12, manuel ch. 24, 28, 30 (copie intégrale) — `corpus/constructeur/` ; origine https://www.ableton.com/en/manual/live-instrument-reference/ [DOC]
- Xfer Serum 2 : manuel dépouillé localement (`../../sound-designer-serum/references/serum2-fx-clip-arp.md`, `moteurs-synthese.md`, `modulation-effets.md`), manuel Serum 1.0.1 lu (`corpus/constructeur/`), changelog, site produit en extraits — https://xferrecords.com/manual/serum-2/docs [DOC-LOCAL / DOC-EXTRAIT]
- Spécification SFZ (sfzformat.com, source GitHub) — `corpus/constructeur/` [DOC]
- Native Instruments : Session Horns Pro, Symphony Series Brass, Kontakt Factory Library 2, Komplete Start — pages produit en extraits [DOC-EXTRAIT] ; cartes d'articulations Reaticulate [DOC-tiers]
- Spitfire (manuel SSO lu) — `corpus/constructeur/` [DOC]
- Waves (API-2500, REQ 6, J37, F6, MetaFlanger), FabFilter Pro-Q 4, oeksound soothe3, Plugin Alliance bx_glue, iZotope Imager — extraits officiels [DOC-EXTRAIT] ; exposition à l'API de Live relevée localement (`../../effets-plugins/references/fiches.md`) [DOC-LOCAL]

## Règle d'utilisation
Les valeurs de cutoff, enveloppes, unisson, compression proposées dans les recettes sont `[HEUR]` sauf si elles reproduisent une valeur d'usine ou une valeur de Reid citée avec sa source. Une valeur `[DOC]` d'un autre synthé (Minimoog, DX7, Juno, Vital, Surge) reste à transposer et donc à valider `[TEST]` dans Serum 2 ou Live. Ne jamais transformer une plage `[HEUR]` en « règle constructeur ».
