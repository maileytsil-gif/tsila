# Fiches plug-ins (Live 12.4.5, VST3) — exposé à l'API ? / fenêtre ? / vérification

| plug-in (version) | exposé à Live | nécessite la fenêtre | vérification |
|---|---|---|---|
| FabFilter **Pro-Q 4** (4.1) | rien (Device On) | tout : bandes (double-clic), gain (glisser vertical, 3 dB ≈ 31 px cadre 1568), Q (molette), forme/pente (menus), Make Dynamic/Spectral (clic droit) ; saisie clavier inopérante | survol des boutons FREQ/GAIN/Q → tooltip ; capture de la courbe |
| Waves **REQ 6 Stereo** (17.1) | tout : `BandN Type` ('Hi-Pass','Bell','Hi-Shelf','Hi-RShelv','Low-Pass'), `On/Off`, `Frq` (Hz entiers → automation en `raw`), `Gain`, `Q` (0,26–6,5) | rien | `str_for_value` ; `read` du bridge |
| Waves **Q10 / SSLEQ** | tout | rien | idem |
| Waves **API-2500 Stereo** | Thresh, Ratio ('1.5:1'…'10:1'), Attack ('0.03 ms'…'30 ms'), Release ('Var s' + `Release Variable`), Knee, Thrust (Norm/Med/Loud), Type (Old/New), Analog, Mix, Makeup (Auto/Manual), Output | rien | relecture + crêtes actif/contourné |
| Waves **L2 Stereo** | Thresh Slider, Ceiling Slider, Release, ARC, Quantize, IDR, Noise Shaping | rien | Insight 2 après (true peak) |
| Waves **J37 Tape** | Formula (815/888/…), Speed, Bias, Saturation, Wow/Flutter, Noise, In/Out Level, Delay | rien | relecture |
| Waves **MetaFlanger** | Mix, Depth, Rate, FeedBack, WaveForm, Filter… | rien | relecture ; automation `disp` |
| Waves **F6**, **Curves AQ** | rien | tout | capture |
| Plugin Alliance **bx_glue** (1.1) | Threshold (dB), Ratio ('2:1','4:1','10:1'), Attack (crans 0,1–30 ; `p.max` = 30), Auto Release On, Output Gain, Sidechain High Pass Filter (Hz), Mono Maker Frequency, Mix, XL Saturation | rien | relecture + crêtes |
| oeksound **soothe3** (1.0.5) | rien | tout ; double-clic sur une valeur + saisie + Entrée fonctionne ; nœuds glissables | capture (zone de réduction) |
| iZotope **Ozone Imager 2** | Width, Stereoize | bandes | relecture |
| iZotope **Insight 2**, **Tonal Balance Control 3** | rien | tout (TBC : remplacer l'instance pour « reset ») | capture |
| Voxengo **SPAN** | rien | Mode › ⚙ : Avg Time (saisie), Block Size (menu) | capture |
| Xfer **Serum 2** (2.1.5) | rien (+ ce que l'utilisateur configure) | tout ; toggles/onglets/navigateur OK en arrière-plan, glisser et saisie non | capture ; niveau via `levels.sh` |
| Natifs Live (EQ Eight, Glue, Compressor, Utility, Auto Filter, Saturator) | tout (Producer Pal, valeurs affichées ; EQ Eight fréquence en raw 0–1 côté bridge) | rien | `ppal-read-device` |

Ajouter une ligne à chaque nouveau plug-in probé (`probe_params.py`).
| Waves **L4 / L3 / WLM Plus** (V17, installés) | non relevés : prober `len(d.parameters)` puis `str_for_value` avant tout usage ; L4 a un mode True Peak, WLM Plus mesure LUFS/TP en insert (mesure seule si en bout de Main) | à relever | à relever |
