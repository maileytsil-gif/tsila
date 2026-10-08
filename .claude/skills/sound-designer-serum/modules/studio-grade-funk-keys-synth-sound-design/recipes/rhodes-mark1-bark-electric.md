# Rhodes Mark I « bark » (Electric) avec trémolo Suitcase et phaser

## Cible
`COMPING ou STAB / 80–115 BPM / voicings rootless 48–72 / VOICE OWNS MEDIUM : le Rhodes laisse le trou de la voix`

## Pourquoi ces réglages
Le bark est une non-linéarité de captation qui dépend de la force de frappe (position et distance tine/pickup, 2e harmonique qui monte) [HEUR-extrait / DOC secondaire] ; Electric modélise exactement ce mécanisme : Symmetry, Distance, Input, Force < Vel [DOC manuel]. Le « vibrato » du Suitcase est un trémolo panoramique [DOC-W].

## Electric (noms API) [TEST, sémantique DOC]
| Paramètre | Départ | Raison |
|---|---|---|
| Pickup Model | **R** | électrodynamique |
| P Symmetry | 40–45 % ou 55–60 % | hors de 50 % (le plus brillant) : asymétrie = 2e harmonique |
| P Distance | bas-moyen | « plus proche = plus overdrivé » |
| P Amp In / P Amp Out | In moyen-haut / Out pour le niveau | « Input faible + Output fort = plus propre » |
| M Force / M Force < Vel | 60–70 % / **élevé** | la vélocité fait apparaître le bark |
| M Stiffness / M Stiff < Vel | 50–60 % / moyen | 50–70 % naturel, > 80 % métallique [HEUR] |
| F Tine Vol / F Tone Vol | Tine > Tone (Mark I brillant) | inverser pour un Suitcase doux |
| F Tine Color | moyen | équilibre partiels haut/bas |
| F Release | court | les dampers coupent vite |
| Damp Amount / Damp Balance | faible non nul / vers le relâchement (+30 à +60) | bruit d'étouffoir surtout à la levée |
| Noise Amount | 10–20 % | bruit de marteau |
| KB Stretch | > 0 | l'accord étiré fait partie du son |
Variante « Bright Mark II » : Stiffness ≈ 70, Tine Color haut, pickup plus proche [HEUR].

## Chaîne
`Electric → Auto Pan-Tremolo (Panning, Sine ou Triangle, 3–7 Hz ou 1/8–1/4 synchro, Phase 180° — 120–150° si le morceau doit vivre en mono, Amount 40–70 %) → Phaser-Flanger (Phaser, 4–6 notches, 0,3–0,8 Hz, Triangle Analog, Feedback faible, Safe Bass on) → API-2500 (3:1, attaque 10–30 ms, Knee Med, Thrust Loud, 2–3 dB) → J37 (815, 15 ips, Wow/Flutter 0) → envoi room 0,5 s`. Variante Breakbot : `Amp Clean + Cabinet 2×12 Near Off-Axis` à la place du phaser (Rhodes → Twin → SM57 [DOC-EXTRAIT]). Variante Dyno : REQ 6 cloche +2 dB vers 3–5 kHz et Chorus-Ensemble Classic [HEUR].

## Alternatives de moteur
Pack **Electric Pianos** (Rhodes Stage 73 samplé, 70 racks) [DOC-EXTRAIT] ; Serum 2 Multisample « Elec.Piano Suitcase » [DOC-mesure] ; NI Scarbee Mark I (« woody » 1974 / « metallic » 1976, préampli, EQ 3 bandes) [DOC-EXTRAIT].

## Jeu
Rootless type A/B, main droite 48–72, fondamentale à la basse ; stabs sur le un et pushes (`../references/playing-voicings-midi.md`) ; vélocités 60–118 : à 60 le Rhodes doit être pur et sombre, à 110 il aboie.

## Tests [TEST]
Vélocité 50 vs 115 : le bark apparaît seulement en haut · mono : trémolo à 180° disparaît, le corps reste · avec la voix : creux 2–4 kHz si fatigue · release : pas de queue synthétique · EQ : −3 dB ≈ 300 Hz si boueux.
