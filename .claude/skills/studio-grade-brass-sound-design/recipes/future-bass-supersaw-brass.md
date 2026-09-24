# Accords « brass » future bass (supersaw)

L'accord large, chopé, compressé vers le haut. Sources : fiches de recettes lues [HEUR-lu], extraits PML/Monosounds/Unison [HEUR-extrait], structure du supersaw JP-8000 (thèse Szabo, `../../sound-designer-serum/references/leads-nappes-textures.md`) [DOC].

## Cible
`HOOK ou PAD / 140–160 BPM (ressenti 70–80) / accords maj9, m9, add9 en 60–84 / 3 notes par instance maximum / BRASS OWNS HOOK au drop`

## Serum 2 [HEUR sauf mention]
- OSC A scie, **unison 7** (nombre magique documenté [DOC]), **detune 0,12**, **blend 75 %** [DOC défaut], width 80 %, phase aléatoire (`RAND`) obligatoire [DOC Szabo] ; OSC B scie unison 3, detune 0,08, −12 st, −6 dB (ancre la hauteur) ; Stack `Center-12` = sub intégré si besoin.
- Filtre MG Low 12, cutoff 3–5 kHz, résonance 10–20 % ; Env 2 → cutoff +30 % : A 10 ms, D 500 ms, S 60 %, R 300 ms.
- Env 1 : A 5–20 ms, S 100 %, R 200–400 ms.
- **Chop** : LFO 1 dessiné, synchro 1/8 (pour un 1/16 swingué, régler 1/8 et dessiner le swing dans la forme [HEUR-extrait]) → volume ou cutoff ; **pitch de tout l'accord** : LFO 2 sinus synchro 1/8–1/16 → fine pitch ±10–50 cents (retransposer si la source donnait un tempo).
- FX : **Hyper** 2–3 voix plutôt que plus d'unison [DOC manuel] → Compressor MULTIBAND (OTT) **20–45 %**, jamais 100 % → Chorus léger → Reverb Hall 2–4 s, mix 20 % sur BUS 1 avec LO CUT.
- HPF 250 Hz sur le bus [HEUR-lu] ; sidechain du kick 4–6 dB (Pro-C n'est pas installé : Compressor natif avec `sidechainSourceTrackId`, ou bx_glue SC).

## Wavetable natif
2 osc Basic Shapes saw, unison Classic 8 voix chacun [HEUR-lu], LP Clean 3 kHz résonance 10–20 %, Env 2 → cutoff A 10 ms D 500 ms S 60 % R 300 ms +30 %, LFO 1 → Volume 1/8 ; Multiband Dynamics preset OTT 45 % maximum (« attention à ne pas exagérer ») ; Chorus-Ensemble.

## Écriture
Voicing haut, 3 notes (un accord de 5 sons = 35 dents de scie de boue [HEUR-lu]) ; le sub et la basse tiennent la fondamentale ailleurs ; doublage fréquent par un vocal chop formant-shifté. Progressions courantes IV–V–iii–vi, vi–IV–I–V.

## Processing bus
`OTT 20–45 % → EQ coupe-bas 250 Hz → sidechain → reverb grande` ; largeur : un seul élément large à la fois (`fiches-pratiques.md` FICHE 14).

## Tests [TEST]
Mono : l'accord garde son corps (réduire Width avant l'unison) · le chop reste lisible sous la reverb · la fondamentale n'est pas doublée par la basse · niveau OTT compensé.
