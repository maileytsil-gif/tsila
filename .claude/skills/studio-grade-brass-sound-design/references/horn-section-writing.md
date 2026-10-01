# Écrire pour une section de cuivres (pop, funk, soul, afrobeat, salsa, jazz)

Sources : Wikipédia « Funk » et pages instruments (copies lues) [DOC-W], Rimsky-Korsakov [DOC], fiches d'arrangeurs et wikis lus [HEUR] — `../../../../corpus/cuivres/recherche-axe5-ecriture-midi-mix.md`. Notes en MIDI, C3 = 60.

## Formations
| Formation | Exemple | Preuve |
|---|---|---|
| Duo | trompette + sax, trompette + trombone | [DOC-W] |
| Trio standard | trompette + sax ténor + trombone ; ou 1 tpt + 2 sax ; ou 2 tpt + 1 sax | [DOC-W] |
| Quatuor | trio + trompette ou sax ; Phenix Horns (EWF) = 2 trompettes + sax + trombone | [DOC-W] |
| Quintette | 3 sax (alto/ténor/bari ou ténor/ténor/bari) + trompette + trombone | [DOC-W] |
| Fela Kuti | baryton, trompette, ténor (trio) | [HEUR-extrait] |
| Big band | 5 sax, 4 trompettes, 4 trombones | [HEUR] |
| Orchestre | 2–3 trompettes, 4–8 cors, 3 trombones, tuba | [DOC Rimsky] |

## Rôles
- Funk : parties « rythmiques et syncopées », phrases à contretemps, **stabs courts dans les espaces entre les mots** ; l'intro est un lieu privilégié d'arrangement de cuivres [DOC-W]. James Brown : la section est une voix de percussion, stabs unisson serrés dans les trous [HEUR].
- Pop/R&B : stabs sur temps forts ou contretemps + riffs unisson au refrain ; réserver les cuivres aux entrées de refrain et aux fills, sinon « ça sonne bon marché » [HEUR].
- Salsa : un mambo (grand passage instrumental après le premier montuno), plusieurs moñas (riffs courts sur la progression du montuno) ; toute attaque commune tombe sur un coup de clave ; réponses « jamais sous le chanteur » [HEUR].
- Afrobeat : riff unisson, puis à l'octave pour le « shout » ; stabs harmonisés en tierces/quartes ou tierces/sixtes parallèles ; call-and-response [HEUR].
- Orchestre : fanfares diatoniques issues de la série harmonique ; tenues à deux ou quatre cors à l'octave ; le trombone rarement dans les tenues [DOC Rimsky].
- Big band : shout chorus avec drop 2-4 aux cuivres, trompettes qui montent ; **jamais plus de deux pupitres en même temps hors climax** [HEUR].

## Voicings
Règles : écriture serrée « sans trous » [DOC Rimsky] ; harmoniser **depuis l'accord**, jamais par intervalle constant (la 2e trompette prend la note d'accord suivante sous la mélodie) ; serré au médium, ouvert dans le grave ; **rien de plus serré qu'une quinte sous MIDI 48** ; le trombone ou le tuba double ou remplace la basse [HEUR].

| Type | Accord C7 (exemple construit, à écouter [TEST]) | Trompette | Sax ténor | Trombone | Note |
|---|---|---|---|---|---|
| Unisson | riff | 67 | 67 | 55 | trombone à l'octave dessous |
| Octaves | riff | 79 | 67 | 55 | 79 = limite confort trompette |
| Close 3 voix | stab | 70 (7) | 67 (5) | 64 (3) | fondamentale à la basse |
| Four-way close | 4 voix | 70 | 67 | 64 | + 60 (2e trompette ou bari) |
| Drop 2 | 4 voix | 70 | 64 | 60 | 2e voix du haut (67) descendue à 55 → trombone/bari |
| Spread | | 70 | 64 | 48 | > 1 octave |
| Pad | tenue | 72 | — | 60 | deux instruments à l'octave, vélocité 70–88 |

Drop 2 documenté : « prendre la deuxième note du haut et la baisser d'une octave » : `[60,64,67,71] → [55,60,64,71]` [HEUR]. Structures supérieures sans fondamentale (salsa) : Cm9 = `[63,67,70,74]`, G7alt = `[62,65,71,73]` [HEUR]. Reggae/ska/soul : les harmonies à 3 voix sonnent vite « trop sucrées » ; trompette et ténor à l'unisson/octave, harmonie au trombone [HEUR-extrait]. Registres par pupitre en big band (ballade) : trompette 1 66–86, trombone 1 53–70, bari 38–48 [HEUR].

## Articulations (notation → geste)
staccato (point), staccatissimo (coin), tenuto, marcato (accent vertical), sforzando-piano (« sf > p » excellent aux cuivres [DOC Rimsky]), scoop / plop / doit / fall (court, moyen, long) [DOC MusicXML], shake = trille de lèvres entre partiels voisins, lip trill, rip/lift = glissando violent vers la note, flutter = « R » roulé (15–30 Hz [HEUR-extrait]), growl = voix + note ou plunger, glissando de trombone ≤ triton dans une seule direction [DOC-W], coup de langue double seulement sur petites embouchures (trompette, cornet) [DOC Rimsky], respiration (`\breathe`).

## Phrasé
Les cuivres respirent comme les bois : leur laisser du repos [DOC Rimsky]. Phrases de 8–12 s, tenues ré-attaquées après 2 mesures, respirations décalées entre pupitres, un « trou » dans toute ligne de 8 mesures [HEUR]. Brillance : « plus le registre monte, plus le son est brillant ; pp doux, ff dur et crépitant » [DOC Rimsky] → écrire le climax en haut du registre, pas seulement plus fort.

## Ce qui n'a pas été trouvé
Composition exacte des sections Tower of Power, Chicago, Blood Sweat & Tears ; arrangement d'« Uptown Funk » ; écrits de Fred Wesley et Jerry Hey (Jerry Hey : « cuivres en ponctuations rythmiques plutôt qu'en leads », *Off the Wall*, *Thriller* [HEUR]). À compléter sur le Mac avec `../../../../corpus/scripts/fetch_sources.py`.
