# Matrice de rôle des plug-ins pour les cuivres

Inventaire réel du Mac (`../../effets-plugins/references/fiches.md`) : ce qui est exposé à l'API de Live s'y lit ; le reste se règle par la fenêtre et se vérifie par capture. Règle : avant d'insérer un plug-in, écrire `PROBLÈME → OUTIL → PARAMÈTRE PRINCIPAL → TEST A/B à niveau égal`.

| Besoin | Premier choix | Alternatives | À éviter |
|---|---|---|---|
| Coupe-bas, boue 250–500 Hz, formants fixes | **REQ 6** (exposé à l'API : type, Frq, Gain, Q) ou EQ Eight | Pro-Q 4 | booster le grave d'une section |
| Dureté 2–5 kHz qui masque la voix | **Pro-Q 4** cloche dynamique ou spectrale −3 à −6 dB (Make Dynamic / Make Spectral par clic droit) | soothe3 mode Soft, nœud 2–5 kHz, depth faible | EQ statique profonde qui éteint le mordant |
| Résonances mobiles d'un sample de cuivre | **soothe3** Soft, Detail moyen | Pro-Q 4 spectral | soothe sur un synth brass propre |
| Tenue d'une ligne, cohésion des stabs | **API-2500** 2–3:1, attaque 10 ms, release 0,1–0,3 s, Knee Med, Thrust Med, Type Old | Glue natif, bx_glue | attaque < 3 ms qui coupe le coup de langue |
| Bus de section (parallèle) | **bx_glue** 4:1, attaque 10–30, Auto Release, SC HPF 100 Hz, Mix 60 % | API-2500 Mix | XL Saturation forte |
| Harmoniques « bande », chaleur | **J37** 815, 15 ips, Saturation modérée, Bias nominal, **Wow/Flutter 0** | Saturator natif Soft Sine | wow/flutter sur des tenues (détune) |
| Épaisseur d'une section synthétique | chorus dans le patch (Serum Chorus/Hyper, Chorus-Ensemble) | **MetaFlanger** en mode chorus (delay 10–20 ms, rate 0,3 Hz, feedback 0) | flanger sur un solo |
| Largeur d'un stab mono échantillonné | **Ozone Imager 2** Stereoize II léger, Width < 120 % | Utility Width | Stereoize I sur une section (phasing) |
| Dynamique par bande, de-esser de sax | **F6** (fenêtre) ou Multiband Dynamics natif bande haute | Pro-Q 4 dynamique | compresser tout le spectre pour un problème à 4 kHz |
| Stabs one-shot organisés | **Battery 4** (cellules, Voice Group, couches de vélocité, AHD) | Drum Rack / Simpler | Battery sans `len(d.parameters)` vérifié |
| Resampler et découper une phrase | **Maschine** (Sync, slices sur pads, écran seulement) | Simpler Slicing, `../../resampling/SKILL.md` | — |
| Mesure | **SPAN** (spectre), **Insight 2** (LUFS, true peak), Tonal Balance | — | juger « à l'oreille » sans mesure |

## Ordre type sur une piste de cuivres
`Instrument → REQ 6 (coupe-bas, boue) → Pro-Q 4 ou soothe3 (dureté, seulement si mesurée) → API-2500 (tenue) → J37 léger → envoi reverb commun`. Sur le bus de section : `bx_glue parallèle → REQ 6 (sweeps automatisés) → Imager si stabs mono`. Retours : coupe-bas 150–200 Hz.

Toutes les valeurs sont [HEUR] ; les capacités citées sont [DOC-EXTRAIT] (manuels bloqués depuis le conteneur, à relire sur le Mac : `../../../../corpus/sources-a-telecharger.json`) ou [DOC-LOCAL] pour l'exposition à l'API.
