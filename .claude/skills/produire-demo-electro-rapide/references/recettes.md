# Recettes de départ

## Deux versions pour chaque morceau

Écrire l'Original Mix en privilégiant l'arrivée rapide de l'idée principale et la continuité d'écoute. Dériver l'Extended Mix d'une copie du Set validé (« Sauver Set Live sous… <nom> - Extended »), intro et outro allongées par Créer › Insérer Silence (`../../arrangement-avance/SKILL.md` § Opérations sûres) : allonger l'intro et l'outro par phrases de 8 ou 16 mesures selon le genre, donner au DJ une percussion et un repère harmonique exploitables, puis conserver les moments clés du morceau. Un long préambule ne suffit pas : vérifier aussi le point d'entrée, la transition vers le premier thème, le dernier drop et la sortie. Adapter à la référence choisie sans reproduire son arrangement.

Exporter deux fichiers clairement nommés, avec départ/fin propres (`../../live-export-wav/SKILL.md`, `analyze_wav.py`), que l'utilisateur écoute en entier. Comparer les sections communes à niveau égal; contrôler que les effets, automations, queues et changements de bus ne divergent pas par erreur. Documenter mesures, durée et éventuelles différences artistiques voulues.

## Variations de drop par phrases de huit mesures

Repérer les mesures 8, 16, 24, 32 de chaque drop, puis dessiner le dernier demi-temps, temps ou deux mesures selon la tension voulue. Exemple évolutif : fin du premier bloc, hat ouvert et petite réponse de snare; deuxième, retrait du dernier kick et reverse cymbal terminant exactement sur le temps 1; troisième, tom/perc et silence d'un demi-temps; dernier, fill plus affirmé et impact à la section suivante. Ajuster le reverse par fade, longueur et niveau pour éviter un pic avant le nouveau kick. Ne pas remplir chaque frontière avec tous les effets; vérifier la transition dans le morceau entier et à faible volume.

## Référence obligatoire par morceau

Choisir avec l'utilisateur un titre identifiable du style retenu. Relever, par l'écoute de l'utilisateur, une source fiable ou l'analyse d'un fichier fourni (`../../synthese-reference/SKILL.md`), BPM approximatif, placement du kick, rythme du sub, caractère de la basse médium, densité, longueur des phrases, transitions et dynamique des sections. Identifier explicitement les observations vérifiées et les hypothèses. Traduire en objectifs mesurables ou audibles pour une composition originale; comparer les exports à niveau perçu semblable. Si le choix n'est pas encore validé, préparer des candidats et continuer le travail réversible, mais ne pas présenter l'un d'eux comme référence convenue.

## Kick synthétisé dans Serum 2

Point de départ pour un kick house : OSC A sinusoïdale, phase constante et random phase à zéro; ENV 1 (amplitude) : attaque 0 ms, hold 0, decay 250–450 ms, **sustain au minimum (−inf dB)** — sinon le decay n'agit pas —, release court ; ENV 2 → hauteur d'OSC A par la matrice, sustain 0 : départ élevé, chute rapide vers la fondamentale en environ 20–60 ms. Ajuster profondeur et courbe pour distinguer click, corps et queue. Ajouter un bruit ou une seconde couche courte pour le click uniquement si nécessaire, puis saturation/filtre avec parcimonie dans les FX de Serum 2 (dans Live : plug-in tiers seulement, règle 6 d'`ableton-live-session`). Accorder la queue au contexte musical; tester plusieurs hauteurs et durées sur les notes réelles de la basse. Exporter et vérifier les attaques isolées, avec sub, à faible volume et en mono. Les nombres sont des amorces de patch, à ajuster à l'oreille de l'utilisateur. Kicks 808 entièrement spécifiés : `../../composer-hooks-funk-electro/references/kick-808-detail.md`.

Pour les autres sons Serum, documenter une fiche reproductible : OSC et warp, enveloppes, LFO et destinations, filtre, FX, macros, plage de jeu et rôle dans le morceau. Sauvegarder les presets lorsque l'interface est réellement accessible; sinon livrer les réglages détaillés.

## Signature rythmique sous 124 BPM

Référence esthétique fournie par l'utilisateur **pour le kick seulement** : **Solomun feat. Jamie Foxx – Ocean (Original Mix)**, ou un son proche. L'identification du titre est vérifiée, mais le timbre précis décrit ci-dessous est un objectif de design formulé par l'utilisateur, pas une mesure de ce master. Comparer le kick à niveau égal avec un extrait accessible lorsqu'une écoute réelle est possible. Ne pas utiliser Ocean comme modèle imposé pour hats, clap, harmonie ou arrangement.

Si l'utilisateur fournit des stems d'Ocean, relever la provenance et le procédé de séparation, puis analyser **le kick** en contexte et isolé : forme d'onde/attaque, durée et évolution de hauteur, spectre, niveau relatif et interaction avec la basse. Une séparation de stems peut laisser du repisse et des artefacts; comparer au mix original. Utiliser les résultats pour concevoir un kick original et ne pas incorporer l'audio de référence dans la sortie sans autorisation adaptée.

- **Kick Serum 2, esprit 808 soft** : OSC A sinus avec départ de phase stable; enveloppe de pitch brève et courbe douce, débuter autour de 30–60 ms; enveloppe d'amplitude (sustain −inf) 280–500 ms, toujours plus courte que l'écart entre deux kicks (60000/BPM ms : 536 ms à 112 BPM, 500 ms à 120) et que l'écart avant la note de sub suivante (`../../kick-bass-equilibre/SKILL.md` §2). Ajouter une harmonique très modérée par saturation/drive pour rester audible à faible niveau. Si le click devient dur, réduire profondeur de pitch, niveau de bruit et énergie aiguë avant de couper le corps. Régler note et longueur sur plusieurs fondamentales; ne pas supposer qu'une unique note sert tout le morceau.
- **Hi-hat fin** : source bruitée courte dans Serum ou un Sound Maschine, attaque immédiate, decay bref; contrôler sibilance et crêtes, varier vélocités et ouvertures sans couvrir la voix. Placer une petite variation avant la fin des huit mesures du drop.
- **Clap** : impulsion claire avec queue courte et éventuelle couche de corps très basse en niveau; tester sur temps 2/4 ou placement adapté au groove. Il doit rester audible sans rendre le mix agressif.
- **Couple kick/sub** : comparer séparément et ensemble, en mono, avec le sub jouant toutes les notes de la progression. Ajuster durée MIDI, enveloppe, relation de phase et sidechain si nécessaire (source et réglages : `../../kick-bass-equilibre/SKILL.md` §4 ; Compressor natif seulement s'il est déjà en place). Préserver le centre grave; hi-hat et clap peuvent occuper une largeur modérée après contrôle de mono.

Créer un petit jeu de presets et de macros (durée de queue, chaleur, attaque, finesse des hats) ; le son validé entre au registre `../../drums-signature/references/signature.md`. Revalider à chaque morceau; l'identité vient d'une cohérence de caractère, pas d'un preset figé. À 124 BPM exactement et au-dessus, la signature reste une option, pas une obligation.

## Ordre des étapes (une par échange, sans durée promise)

| Étape | Sortie |
| --- | --- |
| 1 | Brief, référence, BPM, tonalité, hook cible |
| 2 | Trois hooks en mots, boucle de 8 mesures couche par couche et choix en contexte |
| 3 | Arrangement, variations et transitions |
| 4 | Palette définitive et mix de départ |
| 5 | Export vérifié (`analyze_wav.py`), écoute par l'utilisateur, trois corrections, nouvel export |

La version d'origine proposait un cycle de 90 minutes : c'est un exercice de décision, pas une échéance (`../../chef-de-projet/SKILL.md` §5). Prolonger si hook, transitions ou grave ne fonctionnent pas.

## Bass House soul, 124 BPM, La mineur

Essai harmonique sur huit mesures : Am9 (2), Fmaj7 (2), Cmaj7 (2), G6 (2). Sub mono sur fondamentales et rares passages; glide legato de départ 60–120 ms, à ajuster selon tempo et registre. Basse médium distincte : réponses syncopées entre kicks, attaque et harmoniques, saturation modérée et filtre expressif; filtrer le bas selon sommation avec le sub, puis vérifier en mono. Kick quatre temps, clap 2/4, hats accentués avec variations volontaires. Trois variantes rythmiques du hook avant de changer le timbre.

Grille d'essai (Original Mix) : intro 16, exposition 16, montée 8, drop 32, break 16, montée 8, drop 32, outro 16 = 144 mesures, environ 4 min 39 s. Extended Mix : intro 32 et outro 32 → 176 mesures, environ 5 min 41 s. Adapter la durée cible.

## Électro/R&B chill, 112 BPM, Fa mineur

Essai : Fm9, Dbmaj7, Abmaj9, Eb69 (Eb6/9), chaque accord sur deux mesures. Tester les renversements pour libérer le grave. Sub legato sur changements avec glissés rares; médiums soul syncopés en réponse au chant. Kick discret, caisse claire/clap expressif, hats aérés; ménage de l'espace pour la voix.

Grille d'essai : intro 16, couplet 16, refrain 16, pont 8, couplet 16, refrain 16, break 8, dernier refrain 16, outro 8 = 120 mesures, environ 4 min 17 s.

## Décisions à l'écoute

| Élément | Question | Première action |
| --- | --- | --- |
| Kick/sub | Attaques et fondamentale distinctes en mono ? | Rythme, durée MIDI, enveloppes avant EQ |
| Mid bass | Phrase expressive ou simple doublage ? | Modifier silences et articulation |
| Hook | Mémorisable après deux écoutes ? | Réduire notes et clarifier réponse |
| Voix | Intelligible dans le refrain ? | Dégager arrangement avant compression |
| Transition | Nouvelle section perceptible ? | Retrait, fill ou silence |

## Sources vérifiables

- Suno, entraînement : https://help.suno.com/en/articles/9709569
- Suno Studio : https://suno.com/blog/suno-studio
- Suno MIDI : https://help.suno.com/en/articles/13670593
- Evans et al., génération latente rapide : https://proceedings.mlr.press/v235/evans24a.html
- Grötschla et al., préférences humaines : https://arxiv.org/abs/2506.19085

Ces sources ne documentent pas l'architecture exacte de Suno. Les réglages et harmonies sont des points de départ artistiques à vérifier, pas des conclusions tirées des études.
