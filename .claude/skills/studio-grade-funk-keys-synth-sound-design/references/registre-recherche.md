# Registre de recherche — skill claviers et synthés funk (24 septembre 2026)

Cinq axes en parallèle ; rapports complets : `../../../../corpus/funk-claviers/recherche-funk-axe1-*.md` à `-axe5-*.md`.

| Axe | Lu intégralement | Connu par extraits | Manques |
|---|---|---|---|
| F1 Électromécaniques | Wikipédia (Rhodes, Wurli, Clavinet, Hammond) ; manuel Live (Electric, Tension, Operator) ; SS 42, 55-59 ; setBfree ; openwurli ; STK ; DX7 E.PIANO 1 ; noms API Electric | Chicago Electric Piano (bark), fenderrhodes.com (Suitcase, Dyno), clavinet.com, PianoGroove, forums Leslie | Hz du trémolo Suitcase ; réglages de phaser ; presets Electric ; fréquences des filtres D6 ; réglages de « Superstition » ; Cory Henry |
| F2 Synth funk historique | ROM1A et ROM1B décodées ; Dexed ; manuel Live (Vocoder) ; SS 8, 23, 42 | Reverb (Worrell, 5 Minimoog), Attack (Flash Light), MusicRadar (Chameleon, Thriller), Syntorial (G Thang, Rockit), Wikipédia (Zapp, Prince, G-funk) | Boogie On Reggae Woman ; Thriller (ARP 2600 vs 2 Minimoog) ; Rockit ; synth bass de Zapp ; presets OB-Xa de Prince ; lead de « Regulate » ; chorus Juno chiffré |
| F3 Funk moderne | aucune page (tout bloqué) | NPR, Relix, Variety, Waves, MusicRadar, SOS Inside Track, Splice, Goodhertz, Guitar World, Equipboard | Inside Track « Uptown Funk » (inexistant ?) ; instruments de Silk Sonic ; chaîne Rhodes Vulfpeck ; synthés Thundercat/Louis Cole/Tuxedo ; valeurs de mix |
| F4 Constructeurs | manuel Live 12 ch. 28/30 ; soothe2 ; corpus Serum 2 ; surface Pro-Q 4 ; noms VST3 Vulf | Ableton packs, Xfer, NI, Waves, FabFilter, oeksound, bx_glue, iZotope, Goodhertz | Stretch Center d'Electric ; liste des amplis d'Amp ; Body Types de Tension ; filtre vocalique de Serum 2 ; Scarbee Mark I détaillé ; KFL2 ; NKS |
| F5 Jeu, voicings, mix | Wikipédia (Funk, Hammond, So What, Hancock) ; jazzpianodays ; SS 55-58 ; setBfree ; manuel Live (effets) | Pianote, Attack (Linn swing), musicproductionnerds, iZotope EQ, Production Expert | notes exactes des riffs (Superstition, Use Me, Chameleon) ; Junie Morrison, George Duke ; squabble ; EQ d'orgue ; Groove Pool ; swing mesuré |

## À faire sur le Mac
1. `python3 corpus/scripts/fetch_sources.py` avec `sources-a-telecharger-funk.json` (renommer ou fusionner avec `sources-a-telecharger.json`), puis `build_index.py`.
2. Requalifier les `[DOC-EXTRAIT]` / `[HEUR-extrait]` en priorité : Attack « Flash Light », MusicRadar « Chameleon » et « Thriller », Reverb (Worrell, Bruno Mars), Syntorial (« G Thang », « Rockit »), SOS « Don't Start Now », manuel Vulf.
3. Relever dans Live : noms exacts des paramètres d'Electric par l'API (le catalogue local ne montre que 5 macros), Stretch Center, Body Types de Tension, contenu des packs Electric Pianos / Electric Keyboards / Clav.
4. Relever dans Serum 2.1.5 : filtre Formant/Vowel, multisample « Elec.Piano Suitcase », samples « Bass/ ».
5. Tester les points [TEST] de `playing-voicings-midi.md` et `mix-integration.md`.

## Corrections apportées par la recherche
- Vulf Compressor = algorithme du **SP-303**, pas du SP-1200 ; pas de paramètres « DX style / Pumping / Reel / Zap ».
- Mark II Rhodes = changements cosmétiques sur les derniers Mark I.
- Le « vibrato » du Suitcase et du Wurlitzer est un **trémolo** (panoramique pour le Suitcase, de gain et mono pour le Wurlitzer).
- Il n'existe pas d'épisode Synth Secrets sur le Clavinet.
- « Superstition » : Mu-Tron III documenté sur « Higher Ground », pas sur « Superstition » ; Clavinet modèle C selon Wikipédia.
- DX7 : BASS 1 = algorithme 16 (un dépôt tiers dit 1, à tort) ; « CALIOPE » est l'orthographe d'usine.
