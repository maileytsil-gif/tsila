# DX7 E.PIANO 1 dans Operator (le « Rhodes FM » des années 80)

## Cible
`COMPING ou nappe / boogie, R&B 80s, néo-soul / 48–84 / vélocité = tout`

## Le patch d'usine [DOC ROM1A #11]
Algorithme 5 (trois piles), feedback 6 sur OP6 ; pile A = OP2 (**ratio 14, niveau 58, KVS 7**) → OP1 (1,00, +3) ; piles B et C 1:1 (OP4 → OP3 ; OP6 (+7, feedback) → OP5 (−7)) ; enveloppes : porteuses D ≈ 2,2 s, modulateur « tine » D ≈ 140 ms puis 1,8 s, release ≈ 74 ms ; LFO 5,4 Hz sans profondeur (vibrato à la molette) ; niveaux 99/58/99/89/99/79 ; OP6 atténué au-dessus de E3.

## Operator [TEST]
| Osc | Rôle | Réglage |
|---|---|---|
| A | porteuse cloche | Sine, Coarse 1, 0 dB ; A 1 ms, D 2–4 s, S 0, R 300 ms |
| B → A | tine | Sine, **Coarse 14**, Level −30 à −18 dB (à l'oreille), **Lev < Vel 80–100 %**, A 1 ms, D 300–500 ms, S −12 dB, R 10 ms |
| C | porteuse corps | Sine, Coarse 1, −3 dB, A 1 ms, D 750 ms, S −0,4 dB, R 550 ms |
| D → C | corps | Sine, Coarse 1, Fine +6 cents (ou Spread 10–20 %), **Feedback 40–70 %**, Level −12 à −6 dB, Lev < Vel 85 %, **Lev < Key** négatif au-dessus de E3 ; D 250 ms, R 450 ms |
Algorithme « deux paires parallèles » (n° 8, lecture locale de la figure [MÉMOIRE]) ; la 3e pile manque : Spread ou seconde instance. Les niveaux DX7 0–99 ne se convertissent pas sans table [TEST]. Variante ratio 18 = plus dur [HEUR-extrait]. Alternative documentée : STK Rhodey (base 2f, ratios 1 / 0,5 / 1 / 15, cloche decay 0,25 s) [DOC].

## Chaîne
`Operator → Chorus-Ensemble Classic 0,5 Hz 40 % → Compressor RMS 2:1 → plate 1,5 s 15 %` (« comme sur les disques de l'époque » [HEUR]).

## Serum 2
Warp FM from B Linear, B sinus à +3 octaves + 2 st ≈ ratio 14 (caler à l'oreille), Velocity → Warp amount ; Sub sinus 1:1 pour le corps ; moins direct qu'Operator [TEST].

## Tests [TEST]
Vélocité 40 : presque une sinus ; 110 : la cloche apparaît puis s'éteint en ≈ 150 ms · aigu au-dessus de E3 plus doux · accords 4 sons sans boue (rootless 48–72).
