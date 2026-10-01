# Master club et master streaming, avec les outils de ce Mac

## Cible
`Toute famille / deux masters depuis le même premaster : club et Beatport (−8 à −7 LUFS intégrés, TP −1,0) et streaming (−10 à −11, TP −1,0 ; −2 si Amazon ou YouTube l'exigent)`

Aucune mesure publiée de masters commerciaux du genre : les cibles sont déclarées (EDMProd −6 ST, iZotope −7,5, Mastering The Mix −9 à −7, Shepherd −10 ST maximum) `[DOC-EXTRAIT]` ; d'où deux masters plutôt qu'un compromis. Chaîne et réglages : `../references/mixage-mastering.md` § 4–5 ; chaîne déjà en place dans le projet : `../../effets-plugins/references/chaine-actuelle.md`.

## Avant le master
- Premaster à ≈ −6 dBFS de crête, sans limiteur ; kick et basse validés (`../../kick-bass-equilibre/SKILL.md`) ; sub mono ; un porteur par bande au drop.
- Référence achetée (WAV Beatport) dans REF → Main hors limiteur ; mesurer ses valeurs (Insight 2 ou WLM Plus) : intégré, TP, LRA, ST max au drop, ST min au breakdown, PLR. Consigner dans la mémoire du projet.

## Chaîne (ordre du consensus)
| Étage | Outil | Réglage de départ |
|---|---|---|
| HPF < 20 Hz et EQ correctif | Pro-Q 4 (fenêtre) ou REQ 6 (API) | 200–300 Hz si boueux ; shelf +1–2 dB au-dessus de 8 kHz si terne |
| Glue | bx_glue | 2:1, attaque 30 ms, release auto, SC HP 99 Hz, **1–2 dB** sur le drop |
| Couleur | J37 (7,5 ips, 815 → 888) ou TG Mastering Chain | léger ; avant le clipper |
| Résonances dynamiques | soothe3 ou F6 | 200–400 Hz sur les supersaws, 6–7 kHz si agressif ; jamais empilés avec un multibande |
| Stéréo | Imager 2 | +8 % global ; rien sous 120 Hz (150 en bass house) |
| **Clipper** | L4 (Clip) ou J37 en entrée forte ; RazorClip à prober | 1–3 dB sur le drop `[HEUR]` ; HPF avant si le grave s'écrase |
| Limiteur | L2 ou L4 (true peak), Ozone Elements Maximizer | ceiling −1,0 dBTP ; **2–4 dB** de réduction sur le drop ; au-delà de 4–5 dB, remonter le mix |
| Mesure | Insight 2, WLM Plus (mesure seule) ; hors Live pyloudnorm ou ffmpeg | I, TP, LRA, ST max, ST min, PLR |

Rien après le limiteur sauf la mesure. Dither : aucun en 24 bits ; TPDF une fois pour un 16 bits final.

## Master club
Seuil du limiteur pour −8 à −7 LUFS intégrés (big room et future rave jusqu'à −6,5) ; drop −7/−6 ST, breakdown −12/−14 ST `[HEUR]` ; LRA 4–7 ; contrôle mono (Utility mono toléré, corrélation SPAN) ; L4 Gain Match désactivé avant export.

## Master streaming
Même chaîne, limiteur reculé pour −10 à −11 intégrés (ou −14 si l'utilisateur veut la dynamique complète) ; contraste breakdown/drop borné : un breakdown trop faible est avalé par la normalisation ; TP −1,0 (−2 pour Amazon).

## Vérification
Mesures sur le **fichier exporté**, jamais sur le vu-mètre ; A/B à sonie égale (TBC 3) ; kick en mono ; téléphone et bas volume ; ≤ −1 dBTP ; les deux fichiers nommés `Artist_Title_ClubMaster_128_Fm_Date` et `…_StreamMaster_…`.

## Conditions d'arrêt
Master au-delà de −6 LUFS ; plus de 4–5 dB au limiteur ; sidechain ou compresseur multibande empilés sur le master « pour la densité » ; élargissement au mix et au master sans contrôle mono.
