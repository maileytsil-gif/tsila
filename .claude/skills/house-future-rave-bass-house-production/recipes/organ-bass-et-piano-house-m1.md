# Organ bass et piano house : les deux presets du Korg M1

## Cible
`HOUSE, FUTURE HOUSE (breakdowns), TECH HOUSE / BASSE ORGAN mono (MIDI 36–48) ou PIANO STABS (contretemps, accords 7e/9e) / 122–128 BPM`

Vérifié `[DOC zayansalman]` : I17 **Organ 2** = « Show Me Love », « Gypsy Woman », « Push The Feeling On » ; I01 **Piano 16** = « Ride On Time » (le riff ; la voix est Loleatta Holloway), « Rhythm Is A Dancer », « Finally », « Vogue », « Break My Soul ». « Vogue = Organ 2 » est faux. Les deux sont des PCM : **le multisample est la voie fidèle**, la synthèse une approximation.

## Organ bass
| Approche | Réglage | Preuve |
|---|---|---|
| Multisample (fidèle) | Serum 2 Multisample ou Simpler/Sampler avec l'échantillon ; ENV A 0–2 ms, D 150–300 ms (stab) ou S 60–80 % R 20 ms (ligne) ; MONO, LEGATO, PORTA 0 | `[DOC]` ; enveloppe `[HEUR]` |
| Additif | Operator ou éditeur de table Serum : sinus aux harmoniques **1, 2, 3, 4**, la **3e en avant** (tirettes 88 8000 000 = 16′ + 5⅓′ + 8′) ; key-click = enveloppe de filtre 5–15 ms | `[DOC-2]` |
| Soustractif | triangle ou saw mêlé à 32′ pour le grondement (MusicRadar) ; EDMProd : triangle OCT −2 + carrée +7 st, LP à goût ; UKG : carrée filtrée en stabs courts syncopés | `[DOC-EXTRAIT]`, `[DOC-2]` |
| MIDI | off-beat (pas 3 de chaque temps), gate 50–60 %, contretemps 100–110 ; fondamentale et octave | `[HEUR-lu]` |
| Chaîne | hall court + chorus léger (MusicRadar) ; mono sous 120 ; sidechain 2–4 dB | `[DOC-EXTRAIT]` |

## Piano house
| Point | Réglage | Preuve |
|---|---|---|
| Source | échantillons (pack ProducerStack 732 samples 12 vélocités, préset Serum 2 multisample + Rack Live `[DOC-EXTRAIT]`) ; Simpler/Sampler ; « aucun piano acoustique convaincant par synthèse » (SOS) | `[DOC]` |
| Caractère | brillant, attaque dure, **2e et 3e harmoniques fortes, fondamentale faible** (« it does not sound like a real piano — that is why it cuts through a club system ») ; decay 400–800 ms ; pas de pédale | `[DOC-2]` |
| EQ et espace | HP 200–300 Hz, +1–3 kHz ; plate 1–1,5 s ; léger chorus ; gate serré | `[DOC-2]` |
| MIDI | stabs courts sur les contretemps (pas 2, 6, 10, 14), accords 7e/9e, voicings sans tonique, 3e renversement | `[DOC-2]` |
| Approximation Operator `[HEUR]` | porteuse ratio 1 + modulateur ratio 1 index décroissant (« DX e-piano »), A 0, D 600 ms, bruit court pour le marteau, vélocité → niveau du modulateur | `[DOC-2]` |

## Erreurs
Long release ; fondamentale pleine ; jouer les fondamentales dans les accords ; organ bass polyphonique.

## Vérification
Organ bass seul avec kick 909 : le contretemps porte ; piano stabs dans le breakdown puis au drop en retrait ; mono ; références écoutées à niveau égal.
