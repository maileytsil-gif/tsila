---
name: suno-vocals
description: Écrire un prompt Suno (style + paroles balisées) pour des voix à poser sur un morceau existant dans Ableton — voix africaines/malgaches homme et femme, appel-réponse, paroles fournies par l'utilisateur ou à écrire — puis intégrer les fichiers générés dans Live (piste et bus VOIX, calage par section, transposition si le refrain module). Utilise ce skill dès que l'utilisateur mentionne Suno, un prompt vocal, des paroles, une voix homme/femme, des chœurs, ou veut « une voix sur le morceau ».
---

# Prompt Suno pour voix sur un instru existant

## Deux champs, mode Custom
- **Style of Music** (court, priorités d'abord) : genre + BPM + tonalité, timbre de chaque voix (*deep velvety male, airy soulful female, Malagasy/West African*), *call and response, sparse phrasing, long held notes, humming, intimate close-mic, natural pitch, no autotune*, et les interdits (*no EDM build-ups, no big choir, no fast rap*). Si le refrain module : *chorus modulates up a fourth*.
- **Lyrics** : balises `[Section – minutage – indication de voix]` alignées sur la structure réelle du Set (lire les repères avec `ppal-read-live-set` `locators`). Peu de mots dans les drops (un mot sur le temps fort toutes les 4 mesures), couplets sur les breaks, refrain = hook répété, spoken word sur un pont, hum seul en outro, silence avant la fin exacte.
- Demander **deux générations** : le morceau complet, puis la même avec `a cappella, dry vocal stems, no instruments` (ou « Get Stems » si l'abonnement le permet) — c'est celle qui s'importe.
- Langue : Suno prononce bien les mots courts (malgache : *mora mora, aza maika, andao hifaly*) ; prévoir des voyelles tenues (« eh », « oh ») en repli.

## Intégration dans Live
1. WAV dans `Desktop/1 Project/Samples/Imported/`.
2. Piste audio **VOIX** → bus **BUS - VOIX** (Monitor In) → BUS MASTER 1. Chaîne tiers : REQ 6 (coupe-bas 120 Hz) → soothe3 (sibilances) → API-2500 doux (2:1, 10 ms) → envoi C-Space.
3. Clip à 1|1, warp **Complex Pro**, tempo du projet ; découper par section (`arrangementSplit`) et recaler chaque phrase sur les repères — Suno ne respecte jamais les minutages.
4. Refrain modulé : `ppal-update-clip pitchShift +5` sur les clips du refrain si la génération est restée dans la tonalité de base.
5. Automation de volume (skill `live-automation`) pour éteindre la voix avant la fin ; vérifier, sauver.
