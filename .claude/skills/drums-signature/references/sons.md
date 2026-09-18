# Choix des sons — sample ou synthé, par élément et par genre

| élément | house deep/minimal | tech house / techno | drum & bass | électro |
|---|---|---|---|---|
| kick | synthé rond et court (Serum « DR - Kick Minimal », Operator sinus + pitch env), accordé à la tonique ; ou sample Drum Booth doux | sample/synthé sec et cliquant (TKNVLT Techno Kick), queue longue en techno (rumble par envoi) | sample court et pointu (couche transitoire + corps), HP 40 Hz, laisse le sub seul sous 60 Hz | 808 (Serum « FH 808 Kick », Drum Rack 808), longue queue accordée |
| clap / snare | clap 808 léger + rim (Core Library « Clap 808 Light Quick », « Rim 808 ») | clap plus épais + reverb courte, snare décalée en techno | snare courte compressée, 2 couches, ghosts très bas | clap/snare 808, snappy |
| hats | fermés doux (« Hihat Closed Kaninchen »), ouvert court (« Hihat Open RKTD ») | 16es plus brillantes, rides métalliques en techno | hats 8es + break samplé | 808 closed/open |
| percs | organiques : cabasa, congas, shakers (Core Library Shaker/Conga), bongos | percs métalliques, toms filtrés | rims, breaks découpés | cowbell, toms 808, clave |
| traitement | REQ 6 HP + creux, bx_glue léger, parallèle 30 % | idem + saturation courte | transitoires préservés (attaque lente sur le bus), HP fort | 808 : saturation J37 douce |

## Sample vs synthé — décider
- **Synthé** quand il faut : accorder (kick/808 à la tonique), régler la longueur au tempo, moduler (pitch env, decay), garder la cohérence d'un morceau à l'autre par preset. Serum 2 se pilote par clics (skill `vst-sound-design`), Operator/Wavetable par API.
- **Sample** quand il faut : un caractère précis (acoustique, vintage, bruité), une attaque naturelle, une couche transitoire. Choisir des one-shots (`ppal-library` `type: oneshot`), vérifier le chemin (`verifyPaths`), et stabiliser l'accord (Simpler transpose) si la tonalité compte.
- **Battery 4** (VST3 installé) : kits NI complets, mais aucun paramètre exposé à l'API → fenêtre uniquement ; préférer un Drum Rack quand il faut scripter.
- Rester cohérent : `ppal-library findSimilar` avec un son du registre comme graine pour trouver des variantes proches.

## Bibliothèques repérées sur le Mac
Core Library `Samples/One Shots/Drums/{Kick,Clap,Rim,Hihat,Shaker,Conga,…}` ; packs sur le disque Seagate (« Drum Booth » multi-samples acoustiques, « Skitter and Step », « Drive and Glow ») ; presets Serum utilisateur (TKNVLT Techno Kick Collection, F Brooks kicks, « Kick Future House Tsila », Kick Renders) ; Battery 4.
