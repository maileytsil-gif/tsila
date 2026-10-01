# Autorité des sources — claviers et synthés funk

Priorité : donnée d'usine décodée ou code source > documentation constructeur > manuel ou traité > article de référence lu > notes de tiers lues > extrait de recherche (page non lue) > mémoire.

Condition de lecture (24 septembre 2026) : le conteneur cloud n'atteint que GitHub ; les manuels constructeurs, Sound On Sound, Wikipédia, Reverb, Attack, MusicRadar, Goodhertz étaient bloqués et le quota de recherche s'est épuisé. Les copies intégrales trouvées sur GitHub sont `[DOC]` ; le reste est `[DOC-EXTRAIT]` / `[HEUR-extrait]`. Tout est conservé dans `../../../../corpus/` ; les pages à relire sur le Mac sont dans `corpus/sources-a-telecharger-funk.json` (`corpus/scripts/fetch_sources.py`).

## Sources primaires lues [DOC]
- Manuel Ableton Live 12, ch. 28 (effets) et 30 (instruments), version ≥ 12.3, copie intégrale — `corpus/constructeur/`
- Synth Secrets 8, 23 (formants), 42-43 (pianos, hard sync et Clavinet), 55-59 (orgue et Leslie) — `corpus/synth-secrets/`
- setBfree (émulateur B-3/Leslie de référence) : `default.cfg`, `default.pgm`, `whirl.c`, `vibrato.c`, `tonegen.h` — `corpus/funk-claviers/`
- openwurli (modèle du Wurlitzer 200A dérivé du schéma et du service manual) — `corpus/funk-claviers/`
- STK `Rhodey`, `Wurley`, `BeeThree` ; cartouches DX7 ROM1A/ROM1B décodées ; Dexed `env.cc`, `lfo.cc`, `dx7note.cc` — `corpus/synthes-vintage/`, `corpus/funk-claviers/`
- Juno-60 et Juno-106 d'usine ; Nord Modular Book — `corpus/synthes-vintage/`
- Miroirs Wikipédia : Rhodes, Wurlitzer, Clavinet, Hammond, Funk, So What chord, Herbie Hancock — `corpus/funk-claviers/`
- Leçons jazzpianodays (voicings rootless, quartaux, main gauche) — `corpus/funk-claviers/`
- Corpus des 626 presets d'usine Serum 2 (contenu Keys/Bass) — `corpus/cuivres/` (partagé)
- Manuel soothe2, noms de paramètres du Vulf Compressor 3, catalogue Goodhertz — `corpus/constructeur/`

## Extraits de pages officielles [DOC-EXTRAIT]
Packs Ableton Electric Pianos, Electric Keyboards, Clav, Microtron ; Serum 2 (site produit, forum SFZ) ; NI Scarbee Mark I / Vintage Keys, Komplete Start, Monark, Massive X, Maschine 3 ; Waves J37, MetaFlanger, REQ 6, F6 ; API 2500 (Thrust) ; FabFilter Pro-Q 4 ; oeksound soothe3 ; bx_glue ; Ozone Imager ; manuel et histoire du Vulf Compressor ; interviews SOS (« Don't Start Now », « Say So », RAM), NPR, Relix, Waves (Ronson), MusicRadar (24K Magic), Splice (Chromeo).

## Règle d'utilisation
Les valeurs de patch sont `[HEUR]` sauf si elles reproduisent une donnée d'usine décodée (DX7, Juno) ou un paramètre documenté (setBfree, openwurli, manuel Live). Une valeur d'un autre instrument (Minimoog, Odyssey, DX7) reste à transposer et à valider `[TEST]`. Ne jamais citer « DX style », « Pumping », « Reel », « Zap » comme paramètres du Vulf Compressor, ni écrire « Vulf = SP-1200 ».
