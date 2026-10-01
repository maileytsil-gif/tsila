# Basse FM métallique, « Jauz bass » et future house

## Cible
`BASS HOUSE, FUTURE HOUSE / BASSE MID métallique, élastique / 126–128 BPM / mono, glide / registre +12 au-dessus d'un sub sinus séparé`

Recherche « Jauz bass » : vidéos seulement `[DOC-EXTRAIT]`. Deux recettes écrites et l'ancêtre chiffré (`../../sound-designer-serum/references/patches-genres.md` § 2, Garage Bass) tiennent lieu de base.

## Moteur
Serum 2 : OSC A porteuse, **WARP 1 = FM from OSC** (OSC B modulateur, niveau de B à zéro autorisé), OSC B en mode d'accordage **Ratio** ; WARP 2 = Distortion sur la même table. Operator : FM Drive comme cible de modulation (fiche 39).

## Patch
| Étage | Valeur | Preuve |
|---|---|---|
| OSC A (porteuse) | sinus (Basic Shapes pos. 0), OCT −2 | `[DOC Attack]` |
| OSC B (modulateur) | sinus, Ratio **2:1** (−12 st par rapport à −24) ; **variante métallique : FINE −30 cents** (la « −12,30 » d'Attack : battement inharmonique) ; EDMProd : Ratio **6:1** (2 octaves + quinte) | `[DOC]` ; `[DOC-EXTRAIT]`, `[CALC]` |
| Index FM (quantité de WARP 1) | **MUET** ; départ 45 % + ENV 2 → WARP 1 +60 %, D 150–300 ms S 0 ; 15–25 % = râle, > 40 % = hurlant | `[DOC]` proportions ; `[HEUR]` |
| Autres ratios | 1:3 métallique, 2:5 inharmonique, 3:7 complexe ; cloche = non entier ≥ 4 avec enveloppe rapide sur le modulateur seul | `[DOC-2 DUBFORGE]` |
| FILTER 1 | MG Low 24 ; CUTOFF 25 % de la course (≈ 140–200 Hz `[HEUR]`), RES 0 ; ENV 2 → CUTOFF +100 %, S 0 ; ou LP 3 kHz décroissant en 300 ms | `[DOC]` ; `[DOC-2]` |
| ENV 1 (ampli) | S baissé, R ≈ 33 % (« plucky ») | `[DOC]` |
| Thwack | ENV 3 → CRS +12 st → 0 en 50 ms | `[DOC-2]` |
| LFO 2 → WARP 1 | « ne pas exagérer, ça distord vite » ; en mode Env pour un mouvement par note | `[DOC-EXTRAIT]` |
| Voicing | MONO, PORTA 40–80 ms (10–15 %), LEGATO | `[DOC]` |

## Chaîne
Distortion Tube léger (Warp 2 Diode pour plus de métal `[HEUR]`) → Compressor MULTIBAND MIX 15–25 % → EQ : **coupe-bas 100 Hz** sur ce growl (fiche 37), −3 dB 200–300 Hz → Hyper/Dimension discret → sidechain prononcé. **Sub sinus séparé** sous 100–120 Hz, routé Direct. Drop 1B : moduler l'OCT du modulateur (EDMProd).

## MIDI
Future house : la basse FM joue **fondamentale et octave** de l'accord courant, rarement la tierce (dans le stab) ; off-beat sous des accords m7/m9 ; bass house : riff sur i (`drop-bass-house-trois-couches.md`).

## Erreurs
Chercher le métal dans un ratio non entier alors que l'original est entier + désaccord de 30 cents (fiche 36) ; growl pleine bande ; LFO sans Trig (fiche 3) ; recette Serum 1 rejouée telle quelle (fiche 34 : Quality change les warps FM).

## Vérification
Deux notes extrêmes du riff (l'index FM change de caractère avec la hauteur : ajuster par key track) ; mono ; sub séparé audible seul ; preset sauvé, capture.
