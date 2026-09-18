# Harmonie et mélodie avancées pour la production électronique

Conventions : do = C, numérotation Ableton (C3 = MIDI 60, une octave de moins que la notation scientifique). `scripts/theorie.py` calcule gammes, accords, degrés, transpositions, harmonie négative et fréquences.

## 1. Cadre : l'harmonie de groove est optionnelle et statique

En musique de boucle, les accords signalent une position dans le cycle plus qu'une fonction ; les boucles à 0, 1 ou 2 accords sont les plus fréquentes, 3 ou 4 ensuite (Hein). Les boucles pop/EDM à 4 accords documentées : i–VI–III–VII (= vi–IV–I–V), VI–VII–i–III ; les « plateau loops » VI–VII–i planent sans cadence (Duinker). La techno rejette les cadences (Butler). Conséquence : choisir d'abord **combien** d'accords et **à quelle vitesse** ils changent (rythme harmonique), puis seulement lesquels.

## 2. Modes : du clair au sombre

Ordre de Hein, chaque pas abaisse une note : lydien (#4) → ionien → mixolydien (b7) → dorien (b3) → éolien (b6) → phrygien (b2) → locrien (b5). Note caractéristique à faire entendre dans la mélodie ou la basse, sinon le mode n'existe pas :

| Mode | Caractéristique | Usage électronique |
|---|---|---|
| Dorien | 6te majeure sur mineur (A dans C dorien) | deep house (vamp i7–IV7), DnB liquid, disco |
| Phrygien | 2de mineure (Db) | psytrance, dubstep, hard techno, trap sombre |
| Lydien | 4te augmentée (F#) | ambient, future bass, pads « flottants » |
| Mixolydien | 7e mineure sur majeur (Bb) | funk, disco, French touch |
| Éolien | b6 b7 | mineur « par défaut » de presque tout |
| Phrygien dominant (5e du mineur harmonique) | b2 + 3 majeure : C Db E F G Ab Bb | psytrance, hardstyle, Moyen-Orient |
| Double harmonique | C Db E F G Ab B | psytrance, « byzantin » |
| Hongroise mineure | C D Eb F# G Ab B | idem, avec #4 |
| Lydien dominant | C D E F# G A Bb | film, couleur « acoustique » |
| Altérée | C Db Eb Fb Gb Ab Bb | sur une dominante, jazz |
| Pentatoniques maj/min | C D E G A / C Eb F G Bb | hooks sans frottement, riffs, trap |
| Blues | C Eb F Gb G Bb | riffs acid, basslines |
| Tons entiers | C D E F# G# A# | flou, transitions |
| Octatonique | C D Eb F F# G# A B | sur diminués, tension |
| Hirajoshi / in / insen | C D Eb G Ab / C Db F G Ab / C Db F G Bb | textures, plucks « japonais » |

## 3. Chromatisme fonctionnel utile

- **Emprunt modal** (mode parallèle, même tonique) : en do majeur, iv F–Ab–C, bVI Ab–C–Eb, bVII Bb–D–F, bIII, ii°, i. Change la couleur, pas la fonction (OMT). En mineur, l'emprunt le plus utile est le **IV majeur** ou le **V majeur** (mineur harmonique) pour une vraie dominante.
- **Napolitain bII** : Db–F–Ab en do, souvent en premier renversement, puis V. Sombre et solennel ; en synthwave i–bII est courant.
- **Médiantes chromatiques** : deux accords de même qualité à une tierce, une note commune. Depuis C : E, A, Eb, Ab. Effet « cinéma », rupture sans modulation (C → Ab, note commune C).
- **Dominante secondaire** : V d'un autre degré (D7 → G, A7 → Dm). Une queue de sample contenant la note naturelle (F) frotte avec la sensible (F#) : vérifier.
- **Substitution tritonique** : bII7 pour V7, mêmes notes guides (G7 : B/F ; Db7 : F/Cb). Dm7–Db7–Cmaj7 : basse chromatique.
- **Sixte augmentée** : Ab–C–(Eb)–F# → G ; l'allemande est enharmonique d'Ab7, porte vers la substitution tritonique et la modulation enharmonique.
- **Harmonie négative** : miroir autour de l'axe tonique/quinte (entre Eb et E en do) : C↔G, D↔F, Db↔F#, Eb↔E, B↔Ab, Bb↔A. Majeur devient mineur, dominante 7 devient mineur 6 : G7 → Fm6 ; Am–Dm–G–C → Eb–Bb–Fm–C. Sert à trouver une « autre » cadence ou un B section miroir (`theorie.py negatif`).
- **Modulation** : par pivot (accord commun), par note commune (pratique aux tierces : F tenu de Bb vers F), directe (au début d'une section), chromatique (Cn → C#), enharmonique (sixte allemande relue V7). En électronique, la modulation la plus courante est **directe au drop** ou au dernier refrain (+1/2 ton ou +1 ton).
- **Bitonalité** : deux triades superposées (C + F#, Petrouchka) : réservée aux textures, aux stabs dissonants, à l'IDM.

## 4. Harmonie non fonctionnelle (pads, stabs, textures)

- **sus2 / sus4** (C–D–G / C–F–G) : pas de tierce, ni majeur ni mineur ; base des pads ambient et melodic techno. **add9 / add11** : tierce conservée + note ajoutée (Cadd9 = C–E–G–D).
- **Quartal / quintal** : C–F–Bb, « So What » E–A–D–G–B, ou C–G–D ; pad type D–G–C–F–A. Ouvert, moderne, sans hiérarchie.
- **Clusters** : trois notes adjacentes, doux aux cordes et pads filtrés, agressifs sur des sons riches.
- **Planing** : même forme d'accord déplacée (Cm7–Dbm7–Ebm7, ou stabs techno Em9 transposés « hors tonalité, sans importance », Attack). Annule la sensation de progression : effet de texture en mouvement.
- **Accords sans tierce** (C–G–C) : les seuls tolérés dans le grave.
- **Pédale / drone** : tonique ou dominante tenue sous des accords qui changent ; base de la techno, du dubstep, de la psytrance, de l'ambient. Au-dessus d'une pédale de tonique, tout accord diatonique fonctionne ; les accords hors gamme créent la tension.
- **Extensions pour synthés** : m7, maj7, m9, add9 partout (deep house, lo-fi, melodic techno, future bass) ; 11 et 13 avec fondamentale omise dans le stab quand la basse la tient (Chandler) ; jamais de triades nues sur un supersaw (« trop joyeux »).

## 5. Conduite des voix pour synthés

**Limites d'intervalle dans le grave** (note la plus basse de l'intervalle, Ableton) : 2de mineure E2 · 2de majeure Eb2 · **3ce mineure C2** · 3ce majeure Bb1 · 4te Bb1 · triton Bb1 · **5te Bb0** · 6te mineure Eb1 · 6te majeure C1 · 7e F1 · octave sans limite. Règle : sous C2, plus de tierce ; sous Bb0, plus de quinte ; la basse tient fondamentale et octave, la tierce monte. Un sinus tolère plus bas qu'une dent de scie (moins de partiels qui battent). Le script signale les violations.

**Voicings** : fermé (serré), ouvert (large), drop 2 (2e voix du haut descend d'une octave : C–E–G–B → G–C–E–B). Doubler la fondamentale, pas la tierce. Pads : tierce au-dessus de C3, fondamentale doublée à l'octave, quinte facultative.

**Voice leading parcimonieux** : chaque voix bouge le moins possible, notes communes tenues, basse et aigu en mouvement contraire. Transformations P/L/R : C → Cm (P, E→Eb), C → Em (L, C→B), C → Am (R, G→A) ; cycle pour pads : C → Am → F → Fm → Db → … (`theorie.py progression` propose le renversement le plus lié).

## 6. Accordage et physique

- **Cents** : 100 par demi-ton ; c = 1200·log2(f2/f1) ; seuil ≈ 5 cents en mélodie, moins en harmonie (battements).
- **Série harmonique** : 2f octave, 3f quinte, 4f, 5f tierce majeure (−14 cents), 7f 7e mineure (−31 cents). Dent de scie = tous les partiels en 1/n ; carré = impairs ; sinus = fondamentale seule.
- **Pourquoi la tierce grave est boueuse** : rugosité maximale quand deux partiels tombent dans la même bande critique, large comme une tierce mineure dans le grave (Plomp-Levelt). C1 + E1 : partiels 327 et 329,6 Hz battent à 2,6 Hz.
- **Fréquences** (f = 440·2^((n−69)/12), A3 = 69) : E0 41,2 · F0 43,65 · G0 49 · A0 55 · C1 65,4 · E1 82,4 · F1 87,3 · C2 130,8 · E2 164,8 · F2 174,6 Hz. `theorie.py sub <tonique>` donne la table.
- **Kick et sub** : repérer la fondamentale du kick à l'analyseur, l'accorder à la tonique (ou à la quinte) ; sub sur la fondamentale de la note de basse en octave 0–1 ; la basse mid insiste une octave au-dessus plutôt que sur la même note. En hardstyle le kick **est** la basse, accordé.
- **808 glide** : seulement en mono/legato avec notes qui se chevauchent dans le piano roll.
- **Détune / unison** : quelques cents par voix (ratio 2^(c/1200)) ; l'écart fait le mouvement, trop d'écart vide le centre ; garder le sub sans unison.
- **Juste vs tempéré** : quinte 3:2 (702 vs 700), tierce majeure 5:4 (386 vs 400 : 14 cents audibles). Un accord tenu de synthé peut être « justifié » en désaccordant la tierce de −14 cents : plus stable, moins de battements.
- **Microtonalité** : 24-TET (quarts de ton), Bohlen-Pierce (13 pas dans 3:1). Serum et Wavetable acceptent des fichiers .tun/.scl (à vérifier par version).
- **A = 432 Hz** : la norme est 440 (ISO 16) ; les vertus prêtées à 432 n'ont pas de fondement.

## 7. Mélodie et hook

- **Contour** : arc, descente, ondulation ; conjoint (≤ 1 ton) avec quelques sauts placés ; notes d'accord sur les temps forts, degrés instables (2, 4, 6, 7) sur les temps faibles ou en passage.
- **Notes étrangères** : passage (C–D–E), broderie (E–F–E), appogiature (saut puis résolution par degré sur temps fort), échappée, anticipation, retard (4-3, 7-6, 9-8).
- **Motif et développement** : répétition, séquence (motif transposé par degré), inversion, augmentation/diminution, fragmentation, rotation ; varier dès la 3e répétition.
- **Hook** : court, répétable, un intervalle caractéristique et une figure rythmique récurrente ; 2 à 4 mesures en musique de club (usage courant), 4 à 8 en pop.
- **Question / réponse** : la première phrase finit ouverte (sur 2, 5 ou 7), la seconde ferme (sur 1 ou 3).
- **Arpèges** : up, down, up-down, 1-5-8, octaves ; arpèges de 7e et 9e pour la trance et le melodic techno (la mélodie = l'arpège de la progression).
- **Contre-chant** : mouvement contraire, rythme complémentaire (joue dans les silences), registre distinct.

## 8. Tension et résolution (hauteurs)

Sensible → tonique, 7e de dominante → tierce ; retards préparés puis résolus par degré ; cadences : parfaite V–I (la plus forte), plagale IV–I, rompue V–vi ou V–bVI (surprise au drop), demi-cadence sur V (appel). **Rythme harmonique** : relatif ; un drop tient souvent un accord (ou une pédale) et le break accélère ; en bass music, un changement par 8 ou 16 mesures suffit, placé sur la mesure 8 ou 16.

## Sources principales
Open Music Theory (viva.pressbooks.pub/openmusictheory : modal mixture, augmented sixth, neo-Riemannian, chord schemas) · Ethan Hein (ethanhein.com : groove harmony, modes light to dark, dorian) · Duinker, MTO 25.4 (plateau loops) · Tymoczko, MTO 16.1 et *A Geometry of Music* · Wikipedia (negative harmony, chromatic mediant, tritone substitution, quartal harmony, parallel harmony, nonchord tone, cadence, harmonic series, cent, just intonation, consonance and dissonance, concert pitch) · FunJazz / Robin Hoffmann (low interval limits) · Sound On Sound Synth Secrets (série harmonique) · Attack Magazine (tuning drums, legato/glide, Kerri Chandler chords, techno parallel stabs, techno pads).
