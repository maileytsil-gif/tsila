# Intégration au mix des claviers et synthés funk

Valeurs de départ [HEUR] (compilations et extraits lus), faits de manuel [DOC] ; procédure complète `../../mixage/SKILL.md`, diagnostic `../../ingenieur-mixage/SKILL.md`, grave `../../kick-bass-equilibre/SKILL.md`.

## Place de chacun
- **Guitare rythmique** : « les médiums sont souvent coupés pour se distinguer des cuivres et des claviers ; aigus montés ; pas de sustain » (Nile Rodgers) [DOC Wikipédia « Funk »] ; guitare coupée sous 120 Hz [HEUR].
- **Interlock** = première séparation : si Clav et guitare jouent les mêmes doubles-croches, l'un est de trop ; en cas de conflit spectral, couper le moins important dans la bande de l'autre plutôt que booster [HEUR].
- **Basse** : mono sous 120 Hz ; accords et pads passés au passe-haut 150–300 Hz ; « basse et guitare se battent pour 200–500 Hz » [HEUR] ; accords passe-haut pour laisser la basse (Kaytranada [HEUR-extrait]).
- **Voix** : creux de 1–3 kHz dans les pads ; le Rhodes « laisse un trou spectral là où est la voix » [DOC-W] ; pads −8 à −15 dB sous l'élément principal [HEUR].

## EQ par instrument [HEUR / HEUR-extrait]
| Instrument | Zones |
|---|---|
| Rhodes | +1 à +2 dB 100–250 Hz (chaleur) · −3 dB ≈ 300 Hz si boueux · −3 dB 600–800 Hz et −1 à −2 dB 1,2 kHz (« cheese » numérique) · bark / bruit d'étouffoirs 800 Hz–1 kHz · présence 1,5–2 kHz · creux doux 2–4 kHz (fatigue) · +3 dB 6–8 kHz (attaque) · passe-bas 2–5 kHz pour un néo-soul sombre |
| Clavinet | corps 200–500 Hz ; stabs coupés 150–250 Hz pour la basse ; médium funky 500 Hz–2 kHz ; Brilliant ≈ +3 dB vers 4 kHz ; saturation plus forte que sur les autres claviers |
| Wurlitzer | honk 800 Hz–1 kHz ; harmoniques impairs ; trémolo mono ≈ 5,5 Hz |
| Orgue | crossover Leslie 800 Hz [DOC] ; passe-haut 60–100 Hz et creux 250–400 Hz si nappe épaisse [MÉMOIRE, TEST] |
| Synth bass | mono < 120 Hz ; harmoniques 500 Hz–2 kHz pour la lisibilité sur petits systèmes |

## Compression [HEUR sauf mention]
Keys : 2–3:1, attaque 15–30 ms, release 150–300 ms, 2–4 dB. Rhodes ballade 3:1 (2–3 dB), rythmique 5:1 (4–6 dB), type 1176 2:1 ≈ 3 dB ; Clav : FET rapide ; parallèle 10:1+ mélangée 20–50 %. Manuel Live [DOC] : attaque 10–50 ms laisse passer les crêtes ; > 6 dB de réduction altère fortement le son ; Glue = bus SSL, Range −60/−70 dB = matériel. Ronson/Bhasker : opto (CLA-3A) sur voix et basse [DOC-EXTRAIT].

## Modulation et mono
Auto-pan Rhodes à 180° : **l'effet disparaît en somme mono** (le signal reste) → Phase 120–150° ou mode Tremolo si le morceau doit rester vivant en mono [HEUR/TEST]. Chorus/ensemble : mono correct ; Haas : mauvais [HEUR]. Wurlitzer et Clavinet (sauf doublage L/R) : mono.

## Espace [HEUR]
Room 0,3–0,8 s pour la cohésion ; plate 1–3 s (longue plate = années 70) ; pré-delay 20–40 ms ; retour passe-haut 200–500 Hz, passe-bas 5–10 kHz ; RT60 ≤ une mesure sur du matériel rythmique ; slapback 60–140 ms ; Rhodes panné ±10–25 %.

## Bus et sonie
Bus claviers : Glue ou bx_glue 2:1, 10–30 ms, Auto, 1–3 dB, sidechain léger du kick (1–3 dB) pour laisser respirer le « one » [HEUR/TEST]. Mix « chaud » : roll-off au-dessus de 14 kHz, +100–200 Hz doux, saturation bande ; « le son 70s est largement un produit de la compression bande et console » [HEUR]. Sonie funk −10 à −8 LUFS, néo-soul −11 à −9 [HEUR] ; mesurer après export (`../../live-export-wav/SKILL.md`).
