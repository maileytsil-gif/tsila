# Analyser harmonie, basse et arrangement dans plusieurs styles

## Méthode

1. Déterminer la mesure, la pulsation, la tonalité ou le centre modal; noter les incertitudes si l'on n'a que de l'audio. Séparer rythme harmonique (fréquence des changements d'accords) et rythme de jeu des instruments.
2. Relever par section les accords **et leur basse réelle**. Nommer fondamentale, renversement ou pédale; noter si l'accord n'est qu'implicite. Écrire les tierces/septièmes et les tensions qui expliquent sa couleur. Une note chromatique brève peut être une approche plutôt qu'un nouvel accord.
3. Écrire une grille rythmique de 16 doubles croches en 4/4 ou sa subdivision adaptée à la mesure. Relever pour chaque événement départ, durée, hauteur, accent et articulation; laisser explicites les silences. Vérifier la relation entre kick, basse et caisse claire avant d'attribuer du swing.
4. Décomposer la basse en ancrages, quintes/octaves, notes d'accord, notes de passage, anticipations, glissés et notes mortes. Identifier sa technique de jeu réelle ou, en MIDI, préciser la banque et les articulations nécessaires. Éviter de confondre note courte et ghost note acoustique.
5. Répartir l'accompagnement : piano/Rhodes/Clavinet/guitare, voix, cuivres ou synthés. Pour chacun : registre, voicing, placement, durée et rôle (soutien, contretemps, appel, réponse, fill). Préserver des fenêtres non occupées pour la mélodie et la batterie.
6. Étudier les transitions : retirer/ajouter, annoncer le changement harmonique, écrire un fill qui s'arrête avant le retour si l'impact en bénéficie. Comparer la première mesure du retour avec et sans fill.
7. Fournir deux livrables distincts selon le cas : **analyse attestée** de la source réellement écoutée/consultée et **exemple original** programmable. Ne pas présenter l'exemple comme une transcription ou attribuer des voicings précis à un artiste sans preuve.

## Adapter plutôt que copier le langage funk

| Style | Rythme harmonique courant à tester | Basse et batterie | Clavier, accords et réponses |
|---|---|---|---|
| Funk | Vamp parfois long; 7/9/13 selon morceau | Premier temps comme ancrage possible, syncopes, notes mortes, durée contrôlée | Stabs brefs de guitare/Clavinet/Rhodes; cuivres en réponse |
| Acid jazz / jazz-funk | Vamps ou ii–V–I avec m9/maj9/13 | Ligne mélodique avec notes guides et approches, interaction avec batterie | Rhodes partiel, piano au break, cuivres harmonisés ou à l'unisson |
| Jazz acoustique | Fonction, substitution, pédale ou forme modale selon contexte | Walking, deux temps, ostinato ou jeu libre suivant style | Piano/guitare comping; extensions et conduite de voix |
| Soul / R&B | Cadences, accords enrichis, gospel ou pédales | Durées expressives; attaques et silences soutenant la voix | Réponses de cuivres, orgue et piano dans les respirations vocales |
| Pop / rock | Changement par mesure/phrase variable; accords souvent plus sobres | Fondamentale, octave ou riff selon morceau | Voicing clair, hook et contraste couplet/refrain |
| House / future house | Boucle harmonique ou vamp, 4/4 | Relation kick-sub, syncopes de basses médium distinctes | Stabs ou piano aux contretemps, fills et automation par phrases |
| Hip-hop / DnB | Sample harmonique parfois statique ou progression plus élaborée | Bassline ou sub lié au kick et aux espaces du flow/break | Chops, pads et réponse aux fins de phrases |
| Musique de film / ambient | Pédales, mode, mouvement gradué ou cadence selon scène | Tenue et évolution de registre plutôt qu'ostinato systématique | Voicings et orchestration qui suivent l'image ou le récit |

Ce tableau décrit des options d'analyse, jamais des obligations historiques. Vérifier les traditions et références précises. Pour les cuivres, écrire d'abord les sons réels, puis contrôler tessiture et transposition des parties instrumentales. Trompette Si♭, sax ténor Si♭ et sax alto Mi♭ demandent une notation adaptée au musicien; ne pas exporter aveuglément les notes MIDI de concert comme partitions transposées.

## Exemple original vérifié : jazz-funk en Ré dorien

4/4 à 100 BPM; un accord par mesure : Dm9 → G13 → Cmaj9 → A7(b9) (Dm9–G13–Cmaj9 = ii–V–I de Do, d'où le Si naturel ; A7(b9) = V de Dm, emprunté au mineur harmonique). Basses D1=38, G0=31, C1=36, A0=33 (numérotation Ableton, C3 = 60). Notes d'accord : Dm9 D-F-A-C-E; G13 G-B-D-F-A-E (la 9e A peut être omise du voicing); Cmaj9 C-E-G-B-D; A7(b9) A-C#-E-G-B♭. La treizième de G est E, pas A; A est sa neuvième.

Pour un voicing de Rhodes sans racine, jouer sur chaque mesure Dm9 : F2-C3-E3-A3; G13 : F2-B2-E3-A3; Cmaj9 : E2-B2-D3-G3; A7(b9) : G2-C#3-E3-B♭3. Vérifier les degrés réellement présents : le dernier voicing inclut la tierce C#, la quinte E, la septième G et la ♭9 B♭. Une version plus claire retire la note haute si la voix occupe le même registre.

Sur la première mesure, grille 16 pas : basse D1 au pas 1, A1 au 4, C2 au 6, note morte au 7, F1 au 9, A1 au 12, C2 au 14, A♭0 (32) au 16 (approche chromatique de G0, basse de la mesure 2 ; vérifié par `grille.py` sur `Dm9 | G13`). Durées courtes sauf D1 et F1 éventuellement sur deux pas. Rhodes aux pas 4/12 si la basse y joue aussi : tester d'abord ensemble, puis décaler ou omettre l'un des deux si l'attaque est encombrée. Cuivres au pas 7 (F-A-C) et au 15 (E-G-B) comme couleurs hautes doriennes, sans basse grave supplémentaire. Le choix des mêmes pas est un **test de dialogue**, pas une obligation d'arrangement.

Pour un fill de 8 mesures : clarifier la phrase en 1–4, densifier en 5–6, faire répondre les cuivres en 7, puis retirer leurs attaques sur la fin de 8 si la première attaque du retour doit rester seule. A/B avec et sans silence.

## Contrôles de justesse

- Recalculer les notes de l'accord et les degrés des tensions (`theorie.py accord`) ; G13 contient la 9 (A), que le voicing peut omettre ; ne pas confondre Gm13 avec G13.
- Vérifier C3 = 60 (numérotation Ableton), les octaves et la tessiture. Une grille 16 pas vaut une mesure de 4/4 et le pas 16 désigne le « a » du quatrième temps.
- Une basse qui tient D sous G13 peut créer une tension ou une inversion perçue; ne pas l'appeler automatiquement G13 en position fondamentale.
- Vérifier durées et collisions : grosse caisse, fondamentale grave, Rhodes main gauche et trombone; si nécessaire, déplacer une attaque plutôt que seulement égaliser.
- Mesurer l'écoute audio si elle est réellement accessible; sinon formuler le résultat comme hypothèse de composition, sans prétendre avoir entendu le groove.

## Sources pour la méthode et l'exemple

Yamaha, [jeu de basse funk](https://hub.yamaha.com/guitars/bass/authentic-bass-playing/) et [groove de basse](https://hub.yamaha.com/guitars/bass/getting-your-bass-into-the-groove/); Berklee, [rythme funk](https://online.berklee.edu/takenote/basic-funk-for-drums/), [basse R&B](https://online.berklee.edu/courses/r-b-bass), [tensions](https://online.berklee.edu/takenote/simplifying-jazz-harmonic-theory-an-interview-with-suzanna-sifter/) et [conduite de voix](https://online.berklee.edu/takenote/voice-leading-paradigms-for-harmony-in-music-composition/); Rhodes Music, [histoire et contexte du Rhodes](https://rhodesmusic.com/the-history-of-rhodes/). Les notes MIDI et les rythmes de l'exemple sont originaux.
