# Cuivres échantillonnés et programmation MIDI réaliste

Le réalisme d'une section virtuelle vient du MIDI autant que de la banque. Sources : manuel Spitfire lu [DOC], cartes d'articulations Reaticulate des banques [DOC-tiers], spécification SFZ [DOC], Rimsky-Korsakov [DOC], wikis de production [HEUR] — détails dans `../../../../corpus/cuivres/recherche-axe5-ecriture-midi-mix.md`.

## Banques disponibles ou probables sur ce Mac
| Banque | Ce qu'elle offre | Statut |
|---|---|---|
| Ableton **Orchestral Brass** (Live Suite, SONiVOX) | solo et ensembles cor/trombone/trompette/tuba, articulations commutées par une macro de Rack, Simpler | [DOC-EXTRAIT] ; articulations exactes à relever [TEST] |
| Ableton **Brass Quartet** (Spitfire) | trompette, bugle, tenor horn, trombone ; staccatissimo, vibrato, pitch bend, hollow, flutter, mélangeables par la macro Technique | [DOC-EXTRAIT] (inclus dans Live 11 Suite) |
| NI **Session Horns Pro** (Kontakt Player) | 3 sax, 2 trombones, 3 trompettes, tuba, bugle ; 34 articulations dont sustain, vibrato, marcato, staccato, staccatissimo, **rips, fp 2/4 temps, growl, shake, trilles** ; keyswitches à partir de C−1 ; dynamique par **CC11** ou vélocité ; **Smart Voice Split** répartit les notes d'un accord sur les instruments | [DOC-tiers cartes] ; possession à vérifier (`native-instruments-control`) [TEST] |
| NI **Kontakt Factory Library 2** | cuivres d'orchestre (Berlin Series) | [DOC-EXTRAIT] ; patches non listés |
| Serum 2 **Multisample d'usine** | French Horns, Trumpets LE, Trombones Tenor/Cimbasso LE, Arp Solina Horn | [DOC corpus] ; couches et articulations à relever [TEST] |
| Serum 2 **Sample d'usine** | Brass Wall Low, Trombone, Trombone Alt, DX Brass2 | [DOC corpus] |

## Contrôleurs : qui fait quoi
- **Vélocité** : choix de la couche (mp/f) sur les banques à vélocité (CineBrass en mode velocity map, Session Horns en mode vélocité) ; repérer les seuils de couches avant d'écrire la dynamique (un exemple lu : v95 = mp, v96 = f, rien entre) [HEUR] → tester v95/v96 [TEST].
- **CC1 (molette)** : crossfade des couches de dynamique sur Spitfire et la plupart des banques orchestrales ; « le contrôleur le plus important » [DOC Spitfire] ; l'écrire en continu, jamais plat.
- **CC11 (expression)** : trim de volume de phrase sans changer la couche [DOC Spitfire] ; dynamique principale de Session Horns Pro [DOC-tiers].
- **Vibrato** : CC dédié (Spitfire) ou articulation séparée (Session Horns Pro) ; jamais un LFO global identique pour toutes les voix [HEUR].
- **Interdit physique** : CC1 à 90–127 avec CC11 à 1–40 [HEUR].
- **Tightness** (Spitfire) : coupe le début mou du sample ; serrer pour jouer, puis relâcher et poser un **délai de piste négatif** dans Live [DOC].

## Articulations et keyswitches
Vocabulaire normalisé [DOC MusicXML 4] : scoop (avant la note, par-dessous), plop (avant, par-dessus), doit (après, vers le haut), fall (après, vers le bas, court/moyen/long), shake (trille de lèvres rapide entre partiels voisins), brass-bend, flip, smear, sourdines straight/cup/harmon (ouvert, fermé, demi)/bucket/plunger. Rendu MIDI d'un bend par défaut : 4 messages de pitch bend entre 25 % et 75 % de la durée [DOC MusicXML].

- Session Horns Pro : keyswitches successifs dès C−1, deux canaux pour toutes les articulations [DOC-tiers].
- Live : pas de keyswitch natif ; **Chain Select** d'un Rack piloté par macro, automatisé dans l'arrangement [DOC ch. 24].
- Serum 2 Multisample : `sw_*`, `trigger=legato`, crossfades CC non vérifiés → un preset par articulation [TEST].
- Préférer l'articulation échantillonnée (rip, fall, shake, glissando) au pitch bend quand elle existe ; plage de pitch bend de Kontakt à vérifier [TEST] (±2 st [MÉMOIRE]).

## Écrire la partie
| Paramètre | Valeur de départ [HEUR sauf mention] |
|---|---|
| Staccato / stab | 20–30 % de la valeur du temps ; toutes les voix sur la même double-croche ; vélocité ≥ 100 |
| Legato | chevauchement 10–20 ms (100–110 % de longueur) ; un silence > 20 ms redéclenche |
| Faux legato (banque sans legato) | chevaucher 0,06–0,08 mesure et avancer chaque note de 0,015 mesure pour que l'attaque molle parle sur le temps |
| Retard des cuivres | 10–30 ms derrière basse et batterie (composante du swing) ; sax 20 ms derrière la section ; aucune source lue ne documente un cuivre « en avance » |
| Humanisation | ±10–20 ms, ±8–15 de vélocité, ±5–15 % de longueur, ±3–8 cents par voix ; au-delà de 30 ms à 120 BPM c'est faux |
| Notes répétées | pas de round robin → varier vélocité et micro-timing ou alterner deux instances |
| Section | 2–4 pistes/instances, désaccord ≤ 8 cents, panoramiques distincts, respirations décalées entre pupitres |
| Respiration | fin de phrase 0,03–0,06 mesure plus tôt ; jamais 8 mesures sans trou ; phrases 8–12 s (trompette), 6–10 s (tuba) ; re-attaquer toute tenue > 2 mesures |
| Scoop par bend | −4 st sur 400 ms (mesuré 465 → 524 Hz) ou −2 st remonté en 50–150 ms |
| Fall | sur une note courte répétée en fin de phrase ; shake ±60 cents |
| Doublage | cors à côté du même accord aux trompettes ou trombones [DOC Rimsky] ; 2 cors pour 1 trompette en forte [DOC Rimsky] |

## Erreurs qui trahissent une section virtuelle
Accords de 5–6 notes sur 3–4 instruments · tenues de 8 mesures · registre hors tessiture · vélocité plate, aucun CC · staccatos trop longs · seconde majeure entre deux cuivres dans le grave (« un growl, pas un accord ») · même LFO de vibrato partout · tout le monde joue tout le temps (deux pupitres maximum hors climax) [HEUR/DOC Rimsky].

Voir `horn-section-writing.md` pour les voicings et `../../midi-expressif/SKILL.md` pour appliquer vélocités, durées et décalages dans Live.
