# Jeu, voicings et programmation MIDI du funk

Le funk est d'abord une affaire de doubles-croches, d'espaces et de dynamique. Sources lues : Wikipédia « Funk », « Hammond organ », « So What chord », leçons jazzpianodays (voicings rootless et quartaux), Synth Secrets 55-58, setBfree [DOC] ; compilations tkgally et amen, cours et skills tiers [HEUR] ; extraits Pianote, Attack, Roger Linn [HEUR-extrait]. Rapport complet : `../../../../corpus/funk-claviers/recherche-funk-axe5-jeu-voicings-mix.md`. Convention : MIDI, C3 = 60 (Ableton). Pour appliquer dans Live : `../../midi-expressif/SKILL.md`, `../../compositeur-arrangeur/SKILL.md`, `../../theorie-musicale-electronique/SKILL.md`.

## Vocabulaire harmonique [DOC Wikipédia « Funk »]
Accords étendus : **Fm11, C7(♯9)sus4, F9, Cm6, F6/9** ; **m7 préférés aux triades mineures** (« trop minces ») ; vamps d'un ou deux accords, souvent m7 ↔ dominante voisine (Am → D7) ; **planing chromatique** du même voicing (« Play That Funky Music » : E9, F♯9, F9) ; modes dorien ou mixolydien + gamme blues. « E9 pour tout un morceau est normal » [HEUR].

## Voicings (notes exactes, main droite au-dessus de 48)
| Voicing | Notes | MIDI | Preuve |
|---|---|---|---|
| E9 « James Brown » (3-b7-9-5, sans fondamentale) | G♯2 D3 F♯3 B3 | 56 62 66 71 | contenu HEUR-extrait, placement MÉMOIRE |
| E13 (5 → 13) | G♯2 D3 F♯3 C♯4 | 56 62 66 73 | HEUR |
| Rootless type A 7(9) = 3-5-7-9 ; type B = 7-9-3-5 | Cmaj9 A : E2 G2 B2 D3 / B : B2 D3 E3 G3 | 52 55 59 62 / 59 62 64 67 | DOC jazzpianodays |
| Dominante 9-13 : A = 3-13-b7-9, B = b7-9-3-13 | G13 A : B2 E3 F3 A3 / B : F2 A2 B2 E3 | 59 64 65 69 / 53 57 59 64 | DOC |
| ii-V-I A-B-A | Dm9 → G13 → Cmaj9 | 53 57 60 64 → 53 57 59 64 → 52 55 59 62 | DOC (une voix bouge) |
| « Chameleon » Bbm9 A → Eb13 B | D♭2 F2 A♭2 C3 → D♭2 F2 G2 C3 | 49 53 56 60 → 49 53 55 60 | formules DOC, vamp HEUR |
| « Use Me » Em7(9) A → A13 B | G2 B2 D3 F♯3 → G2 B2 C♯3 F♯3 | 55 59 62 66 → 55 59 61 66 | formules DOC, harmonie HEUR-extrait |
| So What (3 quartes + tierce) sur D | D2 G2 C3 F3 A3 | 50 55 60 65 69 | DOC Wikipédia |
| Quartal D dorien 5 notes | D2 G2 C3 F3 B♭3 | 50 55 60 65 70 | DOC |
| « Hancock » Am11 (triade Am + triade G) | A1 C2 E2 ‖ D3 G3 B3 | 45 48 52 ‖ 62 67 71 | HEUR-extrait |
| E7♯9 rootless | G♯2 D3 G3 B3 | 56 62 67 71 | HEUR |
| E7(♯9)sus4 | A2 B2 D3 G3 | 57 59 62 67 | DOC (accord cité) |
| Bb/C (C7sus, couleur funk) | C2 ‖ B♭2 D3 F3 | 48 ‖ 58 62 65 | HEUR |
| C6/9 gospel « sur le I » | C1 G1 ‖ E2 A2 D3 | 36 43 ‖ 52 57 62 | HEUR-extrait |
Cadence gospel IVmaj7/5 – V7sus – V7 – I ; backdoor bVII7 – I ; m9 parallèles par tons [HEUR]. Registre : voicings entre 48 et 72 ; « quatre notes serrées trop bas deviennent boueuses » [DOC].

**Limites du grave** [HEUR] : 2de mineure pas sous E2 (52), 3ce mineure pas sous C2 (48), 3ce majeure pas sous B♭1 (46), 4te pas sous F1 (41), 5te pas sous B♭0 (34). **Avec une basse** : main gauche sans fondamentale, au-dessus de 48 ; si un synth bass joue, la main gauche ne double ni fondamentale ni octave grave [DOC jazzpianodays / HEUR].

## Rythme et comping
- « **The One** » (James Brown) ; caisse claire sur 2 et 4 ; tempos lents = 16 placements par mesure ; « le son du funk repose autant sur les espaces » [DOC Wikipédia].
- **Interlock** : chaque partie occupe des doubles-croches différentes ; si deux parties jouent le même rythme, l'une est de trop [HEUR].
- **Anticipation** d'une double-croche des accords et de la basse [HEUR].
- **« Superstition »** [HEUR / HEUR-extrait] : Eb mineur pentatonique, **≈ 101 BPM**, doubles-croches droites ; la b7 (D♭) arrive **une double-croche tôt, sur le « a » de 3** ; résolution sur la dernière double-croche de la cellule de 2 mesures ; **deux Clavinets pannés extrême G/D** ; clics étouffés (têtes en x) et ghost notes ; Clavinet modèle C selon Wikipédia ; les notes exactes du riff ne sont pas vérifiées : ne pas les inventer.

### Grille « Clavinet lattice » (1 mesure, gabarit, pas une transcription) [HEUR]
```
pas :      1   e   &   a | 2   e   &   a | 3   e   &   a | 4   e   &   a
rôle :     A   g   x   P | B   x   g   P | A'  x   g   S | B   x   g   P
vélocité : 118 28  20  96| 112 22  30  90| 110 20  32  100|114 24  30  92
gate % de la double-croche : A/B 45-60 · P/S 40-50 · g 25-35 · x 15-25
```
A = accent sur le un · B = backbeat · P = push (anticipation sur le « a ») · S = syncope du « a de 3 » · g = ghost (10–35) · x = clic étouffé (vélocité 15–30 ou articulation mute). Doublage « à la Stevie » : second clip complémentaire (g/x et pushes), pan 60–100 % à l'opposé, autre pickup/filtre.

### Grille « stabs Rhodes » [HEUR]
```
pas :      1   e   &   a | 2   e   &   a | 3   e   &   a | 4   e   &   a
frappe :   X             |         P     |             S |         P
vélocité : 112           |         96    |             88|         94
durée :    1/8 (gate 90 %)|        1/16  |  1/16 (lié au 1 suivant) | 1/16
```
Variante nappe + stab (tenue du 1 au « et » de 2, re-frappe −15 sur le « a » de 3) ; variante contretemps (frappes sur les « et » seulement, le 1 laissé à la basse et au kick) [MÉMOIRE, à écouter]. Main gauche jazz : stab sur le 1 tenu 1,5 temps, push sur le « et » de 2, pushes +10 à +15 de vélocité, contretemps main droite ×0,75 [HEUR].

### Grille « synth bass mono » (E dorien/blues) [HEUR]
```
pas :   1    e   &    a | 2   e   &    a | 3    e    &    a | 4   e    &   a
note :  E1       E2     |         D2     | E1   x    E2      |     G1       D♯1→E1
MIDI :  40       52     |         50     | 40   (40) 52      |     43       39
vél. :  118      95     |         82     | 110  30   100     |     88       92
gate :  1/8      1/16   |         1/16   | 1/16 1/32 1/16    |     1/16     1/16 legato
```
x = dead note ; approche chromatique par en dessous sur la dernière double-croche, glide 45 ms par chevauchement en Mono ; sauts d'octave ; « la basse ne commence jamais exactement avec le kick » [DOC Wikipédia pour la grammaire, HEUR pour la grille].

## Vélocités, durées, micro-timing, swing
| Rôle | Vélocité [HEUR] |
|---|---|
| Accent | 110–127 |
| Normal | 85–105 |
| Doux | 60–80 |
| Ghost | 25–50 (ou 10–30, « bien sous 70 ») |
Variation ±5–10 sur les coups répétés ; note de mélodie la plus forte dans un accord ; roll d'accord 5–25 ms, grave d'abord. Durées : staccato 30–50 % du pas, normal 70–90 %, legato 100–110 %.

**Micro-timing — ce que dit la recherche** [HEUR, citant Frühauf 2013, Senn 2016, Danielsen] : la **grille quantifiée est une bonne base** ; les décalages **précoces sont pires** que tardifs ; un **jitter aléatoire uniforme est la pire option** ; le « feel » vient de décalages **fixes, par instrument, identiques à chaque cycle**, couplés à un changement de vélocité/timbre. Pratique : basse −5 à −10 ms (mène le kick), caisse claire +10 à +25 ms (laid-back), comping ±10–30 ms, jamais de jitter sur kick et sub. Dans Live : **Track Delay** fixe plutôt que Random du Groove Pool (Timing 100 %, Random 0 %, Velocity 0–30 %) [HEUR/TEST].

**Swing** : définition MPC — retarde les doubles-croches paires ; 50 % = droit, 54 % détend sans sonner swing, 62 % relâché à 90 BPM, 66 % = triolet [HEUR-extrait Roger Linn] ; funk 52–58 % ou droit avec micro-timing ; « Flash Light » : « Swing 16ths 59 » [HEUR-extrait] ; Dilla 53–56 % + décalages fixes. Décalage en ms = `(swing/100 − 0,5) × 2 × 15000 / BPM` → à 100 BPM : 54 % = +12 ms, 58 % = +24 ms, 62 % = +36 ms [calcul].

## Orgue Hammond en MIDI
- Vélocité constante (≈ 100) ; dynamique par la **pédale d'expression / swell** (CC 11) [DOC setBfree pour le swell].
- **Percussion single-trigger** : pour qu'elle sonne à chaque accord, **laisser un silence (≥ 1/32)** entre les accords ; en legato, elle ne sonne qu'à la première attaque [DOC ; durée du silence TEST].
- **Leslie** : bascule par CC 64 (setBfree) ; transitions horn 1–3 s, tambour 5–9 s → passer en rapide **1 à 2 mesures avant** le climax [DOC / HEUR-extrait].
- Key click indépendant de la vélocité, à garder en funk [DOC].
- CC de setBfree : drawbars supérieurs CC 70–78, percussion 80–82, vibrato 83, Leslie 64 ; manuels 36–96, pédalier 24–55 [DOC].
- Palm smear : rafale ascendante espacée de 15–30 ms, chevauchement total, finie par l'accord tenu ; palm slap : 3–6 touches frappées [HEUR-extrait / TEST]. « Squabble » : définition non lue.

## Non trouvé (ne pas inventer)
Notes exactes des riffs « Superstition », « Use Me », basse de « Chameleon » ; Junie Morrison, George Duke ; commutateurs exacts du D6 ; valeurs de swing mesurées sur des enregistrements funk.
