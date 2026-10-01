# Chaîne « pumping » lo-fi (SP-303 → Vulf Compressor) avec les natifs

## Cible
`TRAITEMENT d'un Rhodes, d'un Wurli, d'un bus claviers ou batterie / esthétique Vulfpeck, Dilla, Knxwledge`

## Ce qui est documenté [DOC-EXTRAIT Goodhertz]
Origine : algorithme « Vinyl Sim » du **Boss SP-303** (J Dilla, Madlib), porté par Devin Kerr à la demande de Jack Stratton ; **pas de threshold ni de ratio** ; « même à 0 % le son est là » ; Comp Release court = « plus fort, pumping audible, voire distorsion » ; Digital Ref Level **0 dB = snappy**, **−36 dB = écrasé et saturé** ; Sidechain Tilt **+100 % = grosse basse libre**, **−100 % = basse serrée, pumping évident** ; Lo-Fi (Analog / 1990s / 1980s Digital, Crunch, Noise) ; Wow/Flutter 33/45/78 RPM. Les termes « DX style », « Pumping », « Reel », « Zap » n'existent pas dans la documentation. Aucun réglage Vulfpeck n'est publié.

## Approximation native [HEUR/TEST]
1. **Compressor** : Peak, ratio 6–10:1, attaque 1–5 ms, **release 30–80 ms** (« les releases courts provoquent le pumping » [DOC manuel]), Log, Dry/Wet 50–70 % ; sidechain EQ : passe-haut pour « Tilt −100 % » (la basse déclenche moins → plus serré) ou passe-bas pour « +100 % ».
2. **Redux** : Rate réduit (8–20 kHz), Bits 12 (SP-303/1200-like), Shape moyen ; ou Drum Buss Crunch.
3. **Saturator** Analog Clip léger ou **Vinyl Distortion** (Soft « dub plate », Crackle bas) pour « Analog » + bruit.
4. Wow/Flutter : **Chorus-Ensemble Vibrato** Rate 0,55 Hz (33 RPM) à 1,3 Hz (78 RPM), Amount faible, ou rien sur des tenues.
5. Contrôle : niveau compensé, A/B à niveau égal ; pas sur la basse principale (Tilt) sans test mono.

## Où l'appliquer
Rhodes/Wurli comping, bus claviers, kick/snare (« Vulf-compressés » [HEUR-extrait]) ; jamais sur le master avant mesure (`../../mastering-outils/SKILL.md`).

## Tests [TEST]
Le pumping suit le kick sans manger le « one » · la basse garde sa fondamentale en mono · le bruit reste sous le plancher du morceau · réglages notés dans la mémoire du projet, pas présentés comme « le réglage Vulf ».
