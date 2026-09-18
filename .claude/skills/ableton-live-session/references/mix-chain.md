# Chaîne de mix tiers (plus de natifs) — valeurs du projet « deep chill minimal house » (sept. 2026)

Ce sont les valeurs validées sur CE morceau, pas « la chaîne en place » de tout Set : pour el21, lire `projet-el21.md` dans la mémoire ; pour un nouveau morceau, partir d'ici et relire.

- **Pistes AUDIO - X** : REQ 6 — coupe-bas (KICK 27 Hz 48 dB quand le kick tient le grave — 40–50 Hz si le sub tient le fondamental, voir `kick-bass-equilibre`, SUB 23 Hz + passe-bas 109 Hz, BASS 40, PIANO 90, NAPPE 120, PAD 160, CLAP 179, CHORDS 190, PERC/PIZZ 200, HOOK/MÉLODIE 239, TEX 300, HATS 399) + une cloche Q 1 de désencombrement (−1,5 à −2,6 dB entre 260 et 900 Hz) ; shelf −1,6 dB 12 kHz sur HATS, −1,1 dB 10 kHz sur HOOK.
- **BUS - BATTERIE** : bx_glue 4:1, attaque 3 ms, release auto, seuil −13, +1,5 dB, SC HP 60 Hz → API-2500 parallèle 30 % (10:1, 1 ms, Hard, Thrust Med, New, rel 0,1 s, seuil −10, makeup Manual) → REQ 6 (coupe-bas des sweeps, Q 2,5).
- **BUS - BASSES** : bx_glue 2:1, 10 ms, auto, −15, +1, Mono Maker 120 Hz → REQ 6 (sweeps, Q 2,0).
- **BUS - HARMONIE** : soothe3 (soft, depth 4, nœud 357 Hz q 1,5) → API-2500 parallèle 35 % (4:1, 10 ms, Soft, Norm, Old, rel 0,2 s, seuil −12) → REQ 6 (sweeps, Q 4,5) → MetaFlanger (mix automatisé).
- **BUS - CORDES** : bx_glue 2:1, 10 ms, auto, −20, +1 → MetaFlanger (mix automatisé).
- **BUS MASTER 1** (cohésion/couleur) : Pro-Q 4 (Low Cut 24 Hz 24 dB/oct ; 317 Hz spectral −1 dB Q 3,2 ; 6,8 kHz dynamique −1,3 dB Q 1) → bx_glue (2:1, 30 ms, auto, seuil −20, +1, SC HP 99) → J37 Tape (888, saturation 2, 15 ips, wow/flutter 0).
- **BUS MASTER 2** (dynamique/espace) : API-2500 parallèle 60 % (2:1, 30 ms, Soft, Med, Old, rel 0,5 s, seuil −6) → Ozone Imager 2 (width +8 %).
- **BUS MASTER 3** (mesure/sortie) : Tonal Balance Control 3 → SPAN (Avg 4000 ms, bloc 8192) → L2 (seuil −5,1, plafond −1,0 dBFS — c'est un sample peak, −0,4 laissait passer des true peaks > −1 dBTP —, ARC, 24 bits). REF → Main directement (hors limiteur).
- **Main** : Utility 0 dB → Insight 2 (LUFS/true peak = export).
Calibrer un compresseur : comparer les crêtes du bus device actif/contourné (`is_active`) sur une boucle du drop ; viser 1–2 dB sur le corps, transitoires préservés (attaque lente).
