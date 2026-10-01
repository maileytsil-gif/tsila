# DX7 BASS 1 (slap FM) dans Operator — boogie, « Take On Me »

## Cible
`BASSE staccato / boogie, électro-funk 105–125 BPM / 28–52 / sec, release 45 ms`

## Le patch d'usine [DOC ROM1A #15]
Algorithme 16 (porteuse unique OP1 ratio 0,5, modulée par OP2 0,5, OP3 0,5 ← OP4 **5,0**, OP5 0,5 ← OP6 **9,0** feedback 7), Osc Key Sync ON, transpose −12 ; **rate scaling 7** sur OP1/2/5 (notes plus courtes dans l'aigu) ; OP4 KVS 5 decay ≈ 470 ms ; OP6 KVS 7 decay ≈ 370 ms ; porteuse A 1 ms, D 4 ms → 95 %, release ≈ 45 ms. BASS 1 + chorus = la basse de « Take On Me » [HEUR-extrait Reverb Machine].

## Operator [TEST]
Algorithme **7 (B + C + D → A)**. A Sine Coarse 0,5 (ou 1 avec Transpose −12) ; A 1 ms, D 4 ms, S −0,4 dB, R 45 ms. B Coarse 0,5, −2 dB (mod. grave). **C Coarse 5**, −1 dB, Lev < Vel 70 %, D 470 ms, S −inf (slap). **D Coarse 9**, −2 dB, **Feedback 100 %**, Lev < Vel 100 %, D 370 ms, S −inf (clic). **Osc Retrig ON** partout (Key Sync) ; Time < Key positif (rate scaling) ; Voices 1 pour le legato si besoin.

## Chaîne
`Operator → Chorus-Ensemble Classic (Take On Me) → REQ 6 HP 40 Hz → Compressor Peak 4:1 attaque 1 ms release 80 ms → Utility Bass Mono`.

## Jeu
Croches et doubles-croches staccato, octaves ; vélocité 90–120 (le slap n'existe qu'au-dessus de ≈ 90) ; gate 30–50 %.

## Variante
BASS 2 (#16, algorithme 17, attaques 0,8–0,9 s sur OP2/OP6) : basse ronde qui gonfle, pour les tenues [DOC].

## Tests [TEST]
Vélocité 60 vs 115 : le slap n'apparaît qu'en haut · aigu : notes plus courtes · mono · pas de queue > 50 ms.
