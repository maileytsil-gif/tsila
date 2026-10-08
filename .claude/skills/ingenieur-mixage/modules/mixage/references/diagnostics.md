# Diagnostics de mix sans écoute — symptôme → mesure → remède

| symptôme (dit par l'utilisateur) | comment le voir | remède habituel |
|---|---|---|
| boueux, épais | SPAN/Pro-Q : bosse 200–400 Hz cumulés (chercher jusqu'à 900 Hz) ; `mix_snapshot` : plusieurs pistes tenues dans ce registre | creux −2 dB Q 1 sur pad/accords/cordes (REQ 6), coupe-bas plus haut (160–240 Hz) sur les éléments non graves, soothe3 sur le bus harmonie |
| agressif, fatigant | crête 3–8 kHz au master (Pro-Q analyseur), hats/clap dominants dans `levels.sh` | shelf −1,5 dB 10–12 kHz sur hats, bande dynamique 6–7 kHz au master, F6 sur le bus batterie |
| mince, sans corps | grave absent (sub trop bas, coupe-bas trop hauts), largeur appliquée sous 120 Hz | remonter le sub (−4 dB avant fader), Mono Maker 120 Hz, coupe-bas kick 27 Hz / sub 23 Hz seulement si le kick tient le grave (sinon kick 40–50 Hz : `kick-bass-equilibre`) |
| ça pompe | sidechain release > 150 ms ou glue attaque < 3 ms, seuil trop bas | release 110 ms, attaque 10–30 ms sur les bus, seuil pour 1–2 dB |
| trop faible / trop fort | Insight (LUFS, true peak) ; crêtes bus 3 avant L2 | trim master, seuil du L2 (−3 à −7 dB), jamais les faders automatisés |
| la référence sonne plus « pleine » | TBC 3 courbe cible vs mix ; comparer à niveau égal (REF → Main) | corriger la tonalité avant la dynamique ; ne pas empiler les traitements spectraux |
| un passage « ne passe pas » | `clip_summary` : frottement de demi-ton tenu, doublure, tierce dans le grave | problème d'écriture, pas de mix (skill `melodie-composition`) |
Rappels : les vu-mètres API sont pré-fader (pistes) et pré-devices (master), et sous-estiment les crêtes de 2–4 dB ; la vérité est dans l'export analysé.
