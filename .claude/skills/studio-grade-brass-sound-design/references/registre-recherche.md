# Registre de recherche — skill cuivres (24 septembre 2026)

Cinq axes de recherche menés en parallèle, rapports complets dans `../../../../corpus/cuivres/recherche-axe1-*.md` à `recherche-axe5-*.md`. Ce registre dit ce qui a été lu, ce qui n'a pas pu l'être, et ce qu'il reste à faire.

| Axe | Lu intégralement (exemples) | Connu seulement par extraits | Manques |
|---|---|---|---|
| 1 Acoustique, Synth Secrets | SS 23-27 ; Maresz 2026 ; mémoire LAUM ; STK ; Faust ; MuseScore ; music21 ; MusicXML ; Chowning (transcriptions) ; DX7 BRASS 1 | Hirschberg 1996 (abstract), UNSW, HyperPhysics, Luce & Clark, JASA sax, pédagogie des sourdines | Meyer/Benade/Fletcher-Rossing en direct ; attaque de trompette en ms ; vibrato en cents ; spectres bucket/plunger ; formants sax ténor/bari ; « Practical Brass Synthesis » n'existe pas (SS 26-27 en tiennent lieu) |
| 2 Vintage et FM | ROM1A décodée (BRASS 1-3) ; Juno-60/106 d'usine ; SS 24-27, 8, 10 ; Chowning ×3 ; Nord Modular Book ; presets OB-Xd ; recettes Hydrasynth ; spec Axel F | Reverb Machine (Jump, Axel F, Vangelis), MusicRadar, Syntorial, Wikipédia | OB-X vs OB-Xa sur « Jump » non tranché ; Prophet-5, Jupiter-8, CS-80, Polysix, Polymoog sans fiche d'usine ; conversion rates DX7 → ms ; index FM chiffré dans Operator/Serum |
| 3 Électronique moderne | 8 patchs Surge « Brass » ; 12 presets Vital ; 5 synthdefs ; corpus des 626 presets Serum 2 ; fiches de genre tierces (mekedron, JefroB, GMS…) | Attack, ADSR, PML, Cymatics, EDMProd, Monosounds, Unison, VI-Control, Ableton blog, Wikipédia | aucun tutoriel commercial lu ; braam chiffré de tutoriel ; trap Metro Boomin ; cuivres afro house/amapiano (aucune source) ; BPM des LFO synchro ; presets Serum 2 nommés « Brass » |
| 4 Constructeurs | manuel Live 12 ch. 24/28/30 ; manuel Serum 1.0.1 ; changelog Xfer ; aide Imager Ozone 9 ; spécification SFZ | site Xfer, packs Ableton (Orchestral Brass, Brass Quartet), NI (Session Horns Pro, KFL2, Symphony Brass, Komplete Start), oeksound, FabFilter, Waves, bx_glue, Battery, Maschine | contenu Multisample d'usine (réponse partielle par l'axe 3), opcodes SFZ lus par Serum 2, articulations des packs, contenu Komplete, libellés des modes de LFO en 2.1.5 |
| 5 Écriture, MIDI, mix | music21, MuseScore 4.4.4, Abjad ; MusicXML, SMuFL, LilyPond ; Rimsky-Korsakov ; manuel Spitfire ; cartes Reaticulate (SHP, CineBrass, Spitfire, BBCSO) ; copies Wikipédia ; wikis de production | SOS « Top Brass », NI blog, Dorico, Berklee/LJS, tailout, Evan Rogers | manuel Session Horns Pro et plage de pitch bend ; timing mesuré de vraies sections ; arrangements Tower of Power/Chicago/BS&T/« Uptown Funk » ; écrits Fred Wesley/Jerry Hey ; opto vs FET pour cuivres ; de-esser de sax |

## Conditions
Le conteneur n'atteint que `raw.githubusercontent.com` (et PyPI/S3 ponctuellement). WebSearch fonctionne mais ne rend que des extraits ; son quota de session (200 requêtes) s'est épuisé sur deux axes. Les agents ont compensé par des sources primaires hébergées sur GitHub, souvent plus solides que les tutoriels visés.

## À faire sur le Mac (réseau ouvert)
1. `python3 corpus/scripts/fetch_sources.py --dossier cuivres` puis `--dossier constructeur` : télécharge les pages bloquées listées dans `corpus/sources-a-telecharger.json`, puis `build_index.py`.
2. Requalifier dans ce skill les `[DOC-EXTRAIT]` / `[HEUR-extrait]` en `[DOC]` ou les corriger (surtout : Reverb Machine « Jump », Session Horns Pro, packs Ableton, Serum 2 Multisample).
3. Relever dans Serum 2.1.5 : dossiers du navigateur Multisample (Winds/Brass), libellés des modes de LFO, existence d'un filtre Formant/Vowel, chemin `Multisamples/User` ; tester un SFZ minimal.
4. Relever dans Live : contenu du Core Library « Brass », articulations d'Orchestral Brass et de Brass Quartet.
5. Vérifier la possession de Session Horns (Pro) et de Kontakt Factory Library 2.

## Corrections apportées par la recherche
- « Mask Off » : flûte, pas cuivre.
- Il n'existe pas d'article Synth Secrets « Practical Brass Synthesis ».
- Vulf Compressor (skill funk) : origine SP-303 « Vinyl Sim », pas SP-1200.
- Le scoop de hauteur à l'attaque est une habitude de tutoriel : absent des patchs d'usine DX7/Juno, déconseillé par Reid (bandes latérales).
