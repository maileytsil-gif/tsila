# Basse en couches du funk moderne (« Don't Start Now », Sub 37, doublage Jamiroquai)

## Cible
`BASSE / nu-disco, pop-funk 110–125 BPM / 28–52 / propriété du grave : COUCHES d'un même clip ou ALTERNANCE avec la basse électrique`

## Faits
« Don't Start Now » (Ian Kirkpatrick) : « c'est du MIDI » — **Scarbee MM-Bass** joué au clavier et édité, **sub** dessous, **slaps Trilian** dans le drop, **thumb bass**, synth « 90s » au pré-refrain [DOC-EXTRAIT SOS Inside Track]. Sub 37 : glide sur Osc 1/2/les deux, **gated** et/ou **legato**, quatre pentes de filtre [DOC-EXTRAIT SOS]. Basse électrique « popped » **dans les trous** de la synth bass (Premier Guitar) ; Toby Smith double la basse de Jamiroquai (Minimoog, Moog Source, Clavinet, Supernova) [HEUR-extrait]. Layering par zones : sub 0–100 Hz sinus, corps 100–500 Hz, définition 500 Hz–2 kHz [HEUR-extrait].

## Couches (un seul clip MIDI, pistes séparées) [HEUR/TEST]
| Couche | Moteur ici | Réglage |
|---|---|---|
| Réaliste | Serum 2 Sample d'usine « JB Fingerstyle » / « PB Fingerstyle » [DOC-mesure] ou NI (Scarbee si installé [TEST]) | vélocité → couche, ghost notes 25–40 |
| Sub | Operator sinus ou Serum Sub, −12 st, sans vélocité | `../../kick-bass-equilibre/SKILL.md` : qui possède le sub |
| Slap / accent | Serum 2 Sample « Alu Slap » sur les notes ≥ 105 seulement (Velocity zone) | gate court |
| Synth 90s (pré-refrain) | Analog scie + carré, LP 24 dB 400 Hz, chorus léger | joué sur une section seulement |
| Synth bass mono (variante) | Drift Mono Legato Glide « gated » (glide seulement sur les notes liées, jamais au relâchement) | recette P-Funk |

## Chaîne et bus
Chaque couche : REQ 6 (HP 30 Hz sur le sub ; HP 100 Hz + LP 5 kHz sur la couche réaliste ; HP 300 Hz sur le slap) → bus BASSES : bx_glue 2:1, 10 ms, auto, Mono Maker 120 Hz → sidechain léger du kick (1–3 dB [HEUR/TEST]). Opto-like sur l'ensemble (CLA-3A chez Ronson [DOC-EXTRAIT]) = Compressor RMS lent.

## Jeu
Un seul clip, vélocités qui choisissent les couches ; la basse électrique (ou la couche réaliste) « pop » dans les silences de la synth bass ; basse −5 à −10 ms devant le kick [HEUR].

## Tests [TEST]
Somme des couches en mono sans creux (phase du sub et du corps) · une couche coupée à la fois : chacune a un rôle · le drop sans slap sonne plus plat · niveau LUFS du bus stable entre couplet et drop.
