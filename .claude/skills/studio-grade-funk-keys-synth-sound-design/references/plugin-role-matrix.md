# Matrice de rôle des plug-ins pour les claviers et synthés funk

Inventaire réel du Mac (`../../effets-plugins/references/fiches.md`) : exposition à l'API relevée localement ; capacités constructeur en `[DOC-EXTRAIT]` (manuels bloqués depuis le conteneur, à relire sur le Mac). Règle : `PROBLÈME → OUTIL → PARAMÈTRE PRINCIPAL → TEST A/B à niveau égal`.

| Besoin | Premier choix | Alternatives | À éviter |
|---|---|---|---|
| Auto-wah / envelope filter (Clav « Higher Ground ») | **Auto Filter** BP ou LP 12 dB, circuit MS2/PRD, Envelope +, Attack bas, Release 120–180 ms | Meld Vowel, Phaser-Flanger avec env follower | un LFO synchro à la place de l'enveloppe |
| Phaser Rhodes / Clav | **Phaser-Flanger** Phaser, 4–6 notches, 0,3–0,8 Hz, Triangle Analog | **MetaFlanger** (Tape, 0–50 ms, thru-zero), Phaser de Serum | feedback élevé sur les basses (Safe Bass) |
| Trémolo panoramique Suitcase | **Auto Pan-Tremolo** Panning, Phase 180°, 3–7 Hz | Imager pour élargir | oublier le test mono (à 180° l'effet disparaît en mono) |
| Trémolo Wurlitzer | Auto Pan-Tremolo **Tremolo**, ≈ 5,6 Hz, Vintage, Square adouci, Saturator **avant** | — | trémolo stéréo, sinus lent |
| Chorus Juno / Dyno / Dimension | **Chorus-Ensemble** Ensemble ou Classic, 0,5–1 Hz, Width 100 % | Chorus Serum (4 voix), MetaFlanger en chorus | chorus sur l'orgue (« trop luxuriant ») |
| Leslie | Rack 2 bandes (800 Hz) + Auto Pan-Tremolo + Chorus-Ensemble Vibrato + **Cabinet**, rampes automatisées | NI Vintage Organs (Leslie intégré) | un simple auto-pan |
| Ampli (Rhodes → Twin, Wurli, Clav) | **Amp** Clean (canal Brilliant 60s) + **Cabinet** 1×12/2×12 Near Off-Axis | Pedal Overdrive (Compressor avant) | Fuzz sur un Rhodes |
| Saturation bande | **J37** 815, 15 ips, Saturation modérée, Wow/Flutter **0** sur les tenues | Saturator Analog Clip, Roar Tube Preamp | wow/flutter sur un pad tenu |
| Compression de tenue (Rhodes, Clav) | **API-2500** 2–3:1, attaque 10–30 ms, Knee Med, **Thrust Loud** (le grave ne déclenche pas) | Compressor RMS ; opto (Glue lent) ; CLA-3A absent → Compressor RMS lent | attaque < 5 ms qui tue le bark |
| Pumping lo-fi (SP-303 / Vulf) | Compressor Peak release court + **Redux** + Saturator | Drum Buss Comp + Crunch | promettre le « son Vulf » |
| Bus claviers | **bx_glue** 2:1, attaque 10–30, Auto Release, SC HPF 100 Hz, 1–3 dB, Mix 60 % | Glue 2:1 Range −60 dB | sidechain au kick > 3 dB |
| Résonances d'un sample (Rhodes 800 Hz–1 kHz, Clav 2–4 kHz) | **soothe3** Soft, depth faible, Detail moyen | Pro-Q 4 cloche dynamique/spectrale | soothe sur un modèle physique déjà doux |
| EQ corrective | **REQ 6** (exposé API : types, Hz, gain, Q) | Pro-Q 4 (fenêtre) | booster le grave d'un Rhodes sous une basse |
| Largeur | **Ozone Imager 2** Stereoize II, Width ≤ 120 % | Utility | élargir sous 150 Hz |
| Talkbox | **Vocoder** carrier External (piste synthé scie), Retro, Formant | Auto Filter Vowel ; plug-ins tiers (MDA TalkBox, VocalSynth 2) s'ils sont installés [TEST] | Pitch Tracking seul (robotique) |
| Mesure | SPAN, Insight 2, Tonal Balance | — | juger sans A/B |

## Ordre de chaîne historique (instrument → effets)
`Instrument (Electric / Clav / Analog / Serum) → [Pedal ou Amp+Cabinet] → Auto Filter (wah) → Phaser-Flanger ou Chorus-Ensemble → Auto Pan-Tremolo → compresseur (API-2500 ou Compressor) → J37 → envoi room/plate`. Le placement phaser avant/après compression n'est documenté nulle part : avant = la compression lisse les creux (son « pédale » du Clav), après = balayage plus net sur un Rhodes tenu [TEST].
