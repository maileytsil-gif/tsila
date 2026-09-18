# Outils de mixage de l'utilisateur, par tâche (pilotage : API = scriptable/relisible ; F = fenêtre)

| tâche | premier choix | alternatives | pilotage |
|---|---|---|---|
| EQ correctif par piste | Waves REQ 6 Stereo | Q10, SSLEQ (couleur), API-550/560 | API |
| EQ dynamique / spectral (résonances, sibilances) | oeksound soothe3 (source), FabFilter Pro-Q 4 (master, Make Dynamic/Spectral) | Waves F6, TDR Nova, Curves Equator/AQ | F |
| Glue de bus | Plugin Alliance bx_glue | Waves API-2500, SSL G (natif Glue interdit) | API |
| Compression parallèle / densité | Waves API-2500 (mix 30–60 %) | CLA-76, dbx-160, H-Comp | API (API-2500) |
| Compression de piste (basse, voix) | Waves CLA-2A/3A, Pro-C 3 | H-Comp, Cramit | F (Pro-C 3), à prober |
| Sidechain kick → sub/basse | Compressor natif (toléré, déjà en place) ou API-2500 S/C | C1 comp-sc | API |
| Couleur / saturation | Abbey Road J37 Tape (master 1) | Abbey Road Saturator, Kramer Tape, bx_enhancer, Trash | API (J37) |
| Grave mono | bx_glue Mono Maker (bus BASSES) | Waves Center, Utility natif (toléré) | API |
| Largeur stéréo | iZotope Ozone Imager 2 (global) | S1 Imager, Brauer Motion, Doubler | API (largeur globale) / F (bandes) |
| Réverb / delay en envoi | Hybrid Reverb natif « Dark Hall » (retour C, toléré), Valhalla (à prober), Abbey Road Plates/Chambers, H-Delay | Aurora (iZotope), CLA EchoSphere | à prober |
| Analyse tonale vs référence | iZotope Tonal Balance Control 3 + Audiolens (cible) | — | F |
| Spectre | Voxengo SPAN (Avg 4000 ms, bloc 8192) | Waves PAZ, F6-RTA | F |
| Loudness / true peak | iZotope Insight 2 (bout de Main) | Waves WLM Plus, Dorrough, TG Meter Bridge | F |
| Limiteur d'export | Waves L2 (fin de BUS MASTER 3, plafond −1,0 dBFS) | Waves L4 (mode True Peak) / L3, WLM Plus en mesure — installés V17, non relevés dans `fiches.md` : prober avant usage ; L1+, Ozone 12 Elements | API (L2) |
| Correction casque/pièce | SoundID Reference — en autonome sur la sortie système, jamais dans l'export | — | — |
Fiches détaillées (exposé / fenêtre / vérification / valeurs validées) : `../../effets-plugins/references/fiches.md`. Natifs tolérés : liste unique dans `../../ableton-live-session/SKILL.md` (règle 6).
