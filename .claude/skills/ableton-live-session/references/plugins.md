# Plug-ins de l'utilisateur — ce que l'API voit, comment piloter le reste

## Paramètres exposés à l'API Live (réglables par script, valeurs 0–1 → `helpers.solve` / `set_enum`)
- Waves **REQ 6 Stereo** (EQ : `Band1 Type` 'Hi-Pass'/'Bell'/'Hi-Shelf'/'Low-Pass'/'Hi-RShelv', `BandN On/Off`, `BandN Frq` (Hz entiers), `BandN Gain`, `BandN Q` 0,26–6,5), **Q10**, **SSLEQ**, **API-2500** (Ratio '1.5:1'…'10:1', Attack '0.03 ms'…'30 ms', Knee, Thrust Norm/Med/Loud, Type Old/New, Release 'Var s' + `Release Variable`, Mix, Thresh, Makeup Manual/Auto), **L2** (Thresh Slider, Ceiling Slider, ARC, Quantize), **J37 Tape**, **MetaFlanger** (Mix, Depth, Rate, FeedBack, WaveForm), **Reel ADT**.
- Plugin Alliance **bx_glue** (Ratio '2:1'/'4:1'/'10:1', Attack crans 0,1…30 — poser `p.value = p.max` pour 30, Threshold dB, Output Gain, Auto Release On, Sidechain High Pass Filter Hz, Mono Maker Frequency, Mix).
- iZotope **Ozone Imager 2** (Width global seulement).
- Xfer **Serum 2** : rien (Device On) sauf ce que l'utilisateur configure ; fenêtre pilotable au clic.

## Rien d'exposé (fenêtre uniquement)
FabFilter **Pro-Q 4**, Waves **F6**, **TDR Nova**, oeksound **soothe3**, iZotope **Ozone 11 EQ**, **Tonal Balance Control 3**, Waves **Curves AQ**, Voxengo **SPAN**, **Insight 2**.
Vérifier vite : charger sur une piste vide et compter `len(d.parameters)` (1 = rien).

## Techniques de fenêtre (contrôle d'écran, coordonnées dans le cadre du screenshot précédent)
- Ouvrir : `ppal-select` avec `openPluginWindow: true` ; si aucune fenêtre n'apparaît, cliquer le petit bouton « fenêtre » du titre du device dans la fenêtre principale (Serum : x≈29, y≈479 sur la capture 1568 px). Lister avec `app_list_windows` ; les fenêtres de plug-ins n'y figurent pas toujours → screenshot plein écran.
- **Pro-Q 4** : double-clic dans l'affichage crée une bande ; glisser vertical = gain (3 dB ≈ 31 px dans un cadre 1568 px), molette sur le point = Q, clic droit → Make Dynamic / Make Spectral / Shape / Slope ; valeurs lues au **survol** des boutons FREQ/GAIN/Q. La saisie clavier ne répond pas. Le panneau de bande se place sous la bande sélectionnée.
- **soothe3** : double-clic sur une valeur + saisie + Entrée fonctionne ; glisser le nœud pour la fréquence ; réglage doux : depth 4, nœud 357 Hz q 1,5.
- **SPAN** : Mode › ⚙ ouvre le Spectrum Mode Editor (Avg Time double-clic + saisie ; Block Size menu ; pente 4,5 dB/oct déjà par défaut).
- **Serum 2** : clics de fond OK (oscillateurs, MONO/LEGATO, navigateur de presets icône en haut à droite → dossier → double-clic) ; glisser de bouton et saisie ne passent pas en arrière-plan.
- **Tonal Balance Control 3** : pas de reset possible ; remplacer par une instance neuve (charger, puis déplacer en tête avec `ppal-update-device toPath`).
- Menus Live en français ; les items sans titre dans `app_menu list` existent quand même (ex. Fichier › « Exporter Audio/Vidéo... »).
