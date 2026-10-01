# Paramètres exposés à l'API Live par les plug-ins VST3

Relevé le 26 septembre 2026 avec `probe_params.py` (skill `vst-sound-design`) sur une piste audio vide créée en fin d'un Set vierge, Live 12.4.6, LOM Bridge 0.8.3. Chaque plug-in a été chargé seul depuis le navigateur (dossier VST3), ses paramètres listés, puis le device et la piste supprimés. Les valeurs sont normalisées 0–1 ; la colonne « affichage » vient de `str_for_value`.

| plug-in | chemin navigateur | paramètres exposés (hors Device On) | verdict |
|---|---|---|---|
| Analog Obsession **RazorClip** | VST3/AnalogObsession/RazorClip | 5 | pilotable |
| Analog Obsession **TheBus** | VST3/AnalogObsession/TheBus | 9 | pilotable |
| Cableguys **ShaperBox 3** | VST3/Cableguys/ShaperBox 3 | 0 | fenêtre seulement |
| FabFilter **Pro-C 3** | VST3/FabFilter/Pro-C 3 | 0 | fenêtre seulement |
| Valhalla DSP **ValhallaVintageVerb** | VST3/Valhalla DSP/ValhallaVintageVerb | 17 | pilotable, piège `str_for_value` |
| Waves **L4 Ultramaximizer Stereo** | VST3/Waves/L4 Ultramaximizer Stereo (Mono existe aussi) | 7 | pilotable |

## RazorClip (6 paramètres)

| idx | nom | 0,0 | 0,5 | 1,0 | remarque |
|---|---|---|---|---|---|
| 1 | GAIN | 0,0 dB | 12,0 dB | 24,0 dB | linéaire, 24 dB par unité |
| 2 | OUTPUT | −24,0 dB | 0,0 dB | 24,0 dB | linéaire |
| 3 | MIX | 0 % | 50 % | 100 % | pas de 1 % |
| 4 | MODEL | 0 | 2 | 4 | 5 modèles, affichés « 0 » à « 4 » (seuils 0,125 / 0,375 / 0,625 / 0,875) ; non marqué quantifié |
| 5 | BYPASS | 0 | 1 | 1 | valeur par défaut 1 = actif (inversé par rapport au nom) ; non quantifié |

## TheBus (10 paramètres)

| idx | nom | 0,0 | 0,5 | 1,0 | remarque |
|---|---|---|---|---|---|
| 1 | Attack | 0.1ms | 10ms | 30ms | 3 crans : 0,1 ms (< 0,25), 10 ms (0,25–0,75), 30 ms (≥ 0,75) |
| 2 | Release | 50ms | 400ms | 800ms | 3 crans, mêmes seuils |
| 3 | Threshold | −40,0 dB | −20,0 dB | 0,0 dB | linéaire |
| 4 | Output | −15,0 dB | 0,0 dB | 15,0 dB | linéaire |
| 5 | Mix | 0 % | 50 % | 100 % | pas de 1 % |
| 6 | Sidechain Filter | 20 Hz | 260 Hz | 500 Hz | linéaire en Hz |
| 7 | Paramètre #7 | 0 | 1 | 1 | nom non transmis par le plug-in ; bascule 0/1, rôle à identifier dans la fenêtre |
| 8 | Bypass | 0 | 1 | 1 | défaut 1 = actif (inversé) |
| 9 | External Sidechain | 0 | 1 | 1 | bascule ; le routage sidechain de Live reste à confirmer |

## ShaperBox 3 et Pro-C 3

Un seul paramètre exposé : `Device On`. Comme Pro-Q 4, ces plug-ins se règlent uniquement par la fenêtre (contrôle d'écran) ou après configuration manuelle des paramètres dans Live (bouton « Configure » du device, non testé).

## ValhallaVintageVerb (18 paramètres)

**Piège** : `str_for_value(v)` ignore `v` et renvoie toujours l'affichage de la valeur courante (test : Decay à 4,00 s, `str_for_value(0.0)` → « 4.00 s »). `solve()` et `set_enum()` de `helpers.py`, qui balayent `str_for_value`, ne fonctionnent donc pas ici : écrire `p.value` puis relire. Les bornes ci-dessous ont été obtenues en écrivant réellement les valeurs sur la piste de sonde.

| idx | nom | 0,0 | 0,25 | 0,5 | 0,75 | 1,0 |
|---|---|---|---|---|---|---|
| 1 | Mix | 0,0 % | 25,0 % | 50,0 % | 75,0 % | 100,0 % |
| 2 | PreDelay | 0,00 ms | 20,00 ms | 100,00 ms | 256,37 ms | 500,00 ms |
| 3 | Decay | 0,20 s | 0,86 s | 7,00 s | 26,75 s | 70,00 s |
| 4 | Size | 0,0 % | 25,0 % | 50,0 % | 75,0 % | 100,0 % |
| 5 | Attack | 0,0 % | 25,0 % | 50,0 % | 75,0 % | 100,0 % |
| 6 | BassMult | 0,25 X | 0,40 X | 1,00 X | 2,17 X | 4,00 X |
| 7 | BassXover | 100 Hz | 140 Hz | 700 Hz | 3190 Hz | 10000 Hz |
| 8 | HighShelf | −24,00 dB | −18,00 dB | −12,00 dB | −6,00 dB | 0,00 dB |
| 9 | HighFreq | 100 Hz | 1850 Hz | 6000 Hz | 12110 Hz | 20000 Hz |
| 10 | EarlyDiffusion | 0,0 % | 25,0 % | 50,0 % | 75,0 % | 100,0 % |
| 11 | LateDiffusion | 0,0 % | 25,0 % | 50,0 % | 75,0 % | 100,0 % |
| 12 | ModRate | 0,10 Hz | 2,57 Hz | 5,05 Hz | 7,52 Hz | 10,00 Hz |
| 13 | ModDepth | 0,0 % | 25,0 % | 50,0 % | 75,0 % | 100,0 % |
| 14 | HighCut | 100 Hz | 1850 Hz | 6000 Hz | 12110 Hz | 20000 Hz |
| 15 | LowCut | 10 Hz | 380 Hz | 760 Hz | 1130 Hz | 1500 Hz |

Valeurs par défaut au chargement : Mix 100 %, PreDelay 20 ms, Decay 4,00 s, Size 100 %, BassMult 1,50 X, BassXover 300 Hz, HighShelf −24 dB, HighFreq 6000 Hz, ModRate 2,53 Hz, ModDepth 38 %, HighCut 8000 Hz, LowCut 10 Hz, ColorMode seventies, ReverbMode Concert Hall. Les fréquences et le Decay sont logarithmiques (pas d'automation `disp` sur ces paramètres : utiliser `raw`).

- **ColorMode** (idx 16) : 3 valeurs, seventies (0–0,66), eighties (≈ 0,667), now (≥ 0,75 environ). Défaut 0,333.
- **ReverbMode** (idx 17) : 22 modes, un cran ≈ 1/24 ; écrire n/24 avec n = 1 Concert Hall, 2 Plate, 3 Room, 4 Chamber, 5 Random Space, 6 Chorus Space, 7 Ambience, 8 Bright Hall, 9 Sanctuary, 10 Dirty Hall, 11 Dirty Plate, 12 Smooth Plate, 13 Smooth Room, 14 Smooth Random, 15 Nonlin, 16 Chaotic Chamber, 17 Chaotic Hall, 18 Chaotic Neutral, 19 Cathedral, 20 Palace, 21 Chamber1979, 22 Hall1984. Les valeurs 0 et ≥ 0,958 affichent aussi Concert Hall. Relire l'affichage après écriture.

## L4 Ultramaximizer Stereo (8 paramètres)

| idx | nom | 0,0 | 0,5 | 1,0 | remarque |
|---|---|---|---|---|---|
| 1 | Clip | x0.10 | ≈ x1.00 | x10.00 | logarithmique (0,575 → x1.41) ; défaut 0,5 = x1.00 |
| 2 | Release | x0.10 | ≈ x1.00 | x10.00 | logarithmique, même courbe ; défaut x1.00 |
| 3 | Threshold | −30,00 dB | −15,00 dB | 0,00 dB | linéaire, 30 dB de course |
| 4 | Stereo Link | 0 % | 50 % | 100 % | pas de 1 % ; défaut 100 % |
| 5 | Ceiling | −30,00 dB | −15,00 dB | 0,00 dB | linéaire ; −1 dBFS = 0,9667 |
| 6 | Over Sampling | Off | x4 | x16 | 5 crans Off / x2 / x4 / x8 / x16 (seuils 0,125 / 0,375 / 0,625 / 0,875) ; non marqué quantifié |
| 7 | Upward | 0,0 dB | 5,0 dB | 10,0 dB | pas de 0,1 dB |

Rien n'est exposé pour le mode True Peak ni pour les vu-mètres : à vérifier dans la fenêtre. Insight 2 après le L4 reste la mesure du true peak.

## Méthode et limites

- Aucun des six plug-ins ne marque ses commutateurs comme quantifiés (`is_quantized` = 0 sauf Device On) : `value_items` est vide, les crans se déduisent par balayage de `str_for_value` (RazorClip, TheBus, L4) ou par écriture puis relecture (Valhalla).
- Les valeurs par défaut de RazorClip et TheBus mettent `BYPASS` à 1 alors que le plug-in traite : ne pas y toucher sans vérifier dans la fenêtre.
- Non testé : le son (aucun signal envoyé), le bouton « Configure » de Live pour exposer davantage de paramètres sur ShaperBox 3 et Pro-C 3, le routage sidechain de TheBus.
