# Atelier microhouse complet

## Identité et sources

Ne pas confondre microhouse avec « house jouée plus doucement ». Construire le groove à partir de petites unités sonores et de leurs relations: fragments de voix ou d'objet, basses brèves, silences, décalages, répétitions avec microvariations. Akufen décrit lui-même son microsampling de fragments radio dans [cet entretien Ableton](https://www.ableton.com/en/blog/akufen/). Pour une publication, enregistrer ses propres fragments ou utiliser des sources licenciées; ses enregistrements radio ne donnent pas une permission de sampler des tiers. Recondite décrit [ses variations de vélocité sur l'attaque de basse](https://www.ableton.com/en/blog/recondite-melody-technology-interview/), utile dans une branche minimaliste distincte. Les pages Ableton sur [K. Hart](https://www.ableton.com/en/blog/made-in-ableton-live-k-hart/) et [S1gns Of L1fe](https://www.ableton.com/en/blog/made-in-ableton-live-s1gns-of-l1fe/) décrivent des outils de glitch/granularité; ce ne sont pas des définitions du genre et leurs vidéos n'ont pas encore été visionnées ici.

Un [tutoriel écrit de Studio Brootle](https://www.studiobrootle.com/minimal-microhouse-drum-pattern-ableton-tutorial/) documente un exercice précis: 127 BPM, groove SP1200 16 Swing-71 dosé vers 35 %, échantillons 808 dans Sampler, cowbell baissée d'une octave et bouclée, enveloppe lente raccourcissant la boucle tout en montant le pitch vers un ton; hats/congas en doubles croches et quelques triolets, automatisation ponctuelle de Ping Pong/Grain Delay. Ce sont les choix de **ce tutoriel**, non une loi du genre ni une méthode attribuable à Akufen ou Villalobos. Tester aussi 0 % et 20 % de groove pour choisir à l'oreille.

La [vidéo Studio Brootle](https://www.youtube.com/watch?v=ZUQbnkHhksE) a été analysée via transcription automatique complète, sans lecture audio/visuelle vérifiée: 0:27–2:08 swing et doubles croches/triolets; 3:09–4:35 cowbell bouclée, longueur de boucle et pitch modulés; 5:37–6:17 basse tirée d'un autre sample 808, attaque retirée et boucle aller-retour; 6:19–7:49 Grain Delay et Ping Pong Delay automatisés sur hat; 7:58–10:17 hats ouverts, rimshot et conga bouclé avec bit reduction; 10:44–11:30 montée de chaos suivie d'un retour au groove. Le texte écrit confirme les principaux gestes; vérifier dans Live les mots mal traduits de la transcription.

[Jan Jelinek présente Farben](https://janjelinek.com/products/farben) comme des abstractions house/techno à rythmes géométriques simples et à esthétique sonore détaillée. Son [entretien sur la répétition](https://www.eleventhvolume.com/jan_jelinek/) permet de chercher la nuance entre collage soul/funk et machine sans prétendre qu'un son précis vient d'un preset. [Minor Science détaille chez Ableton](https://www.ableton.com/en/blog/minor-science-language-sampling/) un patch Sampler utilisant un long discours isolé, départ de boucle et fréquence FM randomisés, puis un second LFO modulant le taux de cette variation: méthode avancée pour générer de la matière à sélectionner et resampler, pas un signal aléatoire à laisser tourner sans édition. Le [tutoriel minimal house d'Attack Magazine](https://www.attackmagazine.com/technique/beat-dissected/minimal-house/) donne une autre grille 123–127 BPM avec hat décalé et petits one-shots; ses pourcentages de swing ne sont pas la même échelle que le montant de Groove Pool Live.

## Construire huit mesures avant l'arrangement

Prototype original 124 BPM, 4/4, Fa mineur; changer après test. Numérotation Ableton C3 = 60 (F0 = MIDI 29, 43,7 Hz). Mesures 1–2: kick sur quatre temps avec corps court; clap discret 2/4; hat en contretemps avec vélocités différentes. Basse F0 sur 1& (durée 1/8), C1 sur 2a (1/16), F0 sur 3& (1/8), silence avant 4a; laisser le kick démarrer seul. Mesures 3–4: conserver deux attaques, remplacer C1 par Eb1 sur la réponse, puis revenir à la cellule.

```grille
titre: Microhouse 124 BPM — cellule de basse
tempo: 124
accords: Fm7 | Fm7 | Fm7 | Fm7
basse: F0[1&:2] C1[2a:1] F0[3&:2] | % | F0[1&:2] Eb1[2a:1] F0[3&:2] | F0[1&:2] C1[2a:1] F0[3&:2]
``` Mesures 5–8: un fragment de voix percussive sans syllabe identifiable à 4&, un micro-événement différent en m8, puis retour de la basse m1. Ces notes sont un exercice, pas une transcription de producteur.

Créer 8 à 12 prises personnelles: claquement de doigts, objet en bois, souffle, bouche, bruit de pièce, percussion accordée et voix. Couper chaque fragment à son transient, faire fondus anti-clic de 2–10 ms, nommer source/droit/tonalité si tonal. Ranger dans Drum Rack ou Simpler; créer trois variations de vélocité, hauteur ou start point. Ne pas ajouter les douze prises à la boucle: sélectionner deux ou trois rôles complémentaires.

## Cinq basses à essayer, une à retenir

| Famille | Construction Serum 2 | Geste/contrôle |
|---|---|---|
| Sub ponctuel | SUB sinus Direct, mono, E courte avec release sous la note suivante | F0 (Ableton) sur contretemps; contrôler kick/sub en mono. |
| Pluck boisé | A triangle + N transient d'objet autorisé, filtre enveloppé 100–220 ms | Attaque décalée, petites réponses en octave; M1 tone, M2 decay, M3 transient, M4 room. |
| FM feutrée | A sinus, B modulation faible ratio 2:1, E FM brève | Tester variation de vélocité vers FM; garder fondamentale stable. |
| Basse élastique | A pulse filtrée, enveloppe filtre courte, portamento désactivé sauf transition voulue | Une note plus longue en fin de 4 mesures change la phrase sans nouveau son. |
| Basse samplée | Fragment personnel accordé dans Sampler/oscillateur Sample, start point variant légèrement | Contrôler clic, phase et justesse; ne pas laisser la hauteur dériver d'une variation aléatoire. |

Les macros de basse jouent sur attaque, decay, harmonique audible et texture; exclure largeur/reverb du sub. Pour un patch détaillé, documenter toutes destinations et plages réelles dans Serum 2.

## Glitch contrôlé

Dans ce workflow, Grain Delay, Ping Pong Delay, Beat Repeat et la réduction de bits (Redux) sont des effets natifs de Live : la règle 6 d'`ableton-live-session` les exclut des chaînes de mix sauf accord explicite. Obtenir le geste par édition (coupes MIDI ou audio resamplé, `../../resampling/SKILL.md`) ou demander l'exception, imprimer en audio puis retirer l'effet ; équivalents tiers dans `effets-groupes-vocoder.md` § Dans ce workflow.

1. **Micro-coupe**: resampler une mesure de batterie; répéter un fragment de 1/16 ou 1/32 sur la dernière croche de m4, puis revenir au beat. Vérifier click/fade et contraste de niveau.
2. **Saut de start point**: dans Simpler/Sampler, déplacer le début d'un fragment percussif entre deux transients distincts; imprimer trois prises et choisir la meilleure.
3. **Beat Repeat rare**: placer sur bus percussions filtré, déclencher une seule fenêtre avant changement de section; conserver piste sèche. Ne pas mettre des fills sur chaque 4e mesure par automatisme.
4. **Granular**: une prise courte d'objet/voix dans Granulator III ou l'oscillateur granulaire Serum 2; petite densité en arrière-plan, filtrer sous la basse et vérifier licence du sample.
5. **Artefact tonal**: morceau de percussion accordé joué comme stab dans un registre médium; réponse à la basse sans entrer en compétition avec le clap.

Garder un journal des seeds ou rendre en audio toute randomisation. Réécouter trois répétitions identiques: si le glitch empêche de prédire le prochain « un », réduire sa densité.

## Arrangement de 128 mesures, modèle ajustable

| Mesures | Action perceptible | Élément à retenir |
|---|---|---|
| 1–16 | Kick et deux textures; introduire un petit motif percussif | La pulsation et une signature sonore |
| 17–32 | Basse entre, réponse toutes les 4/8 mesures | Cellule de basse reconnaissable |
| 33–48 | Fragment tonal ou voix originale, une variante de glitch | Une nouvelle question, pas un nouveau morceau |
| 49–64 | Retirer kick ou basse brièvement; filtrer texture; transition courte | Silence qui prépare le retour |
| 65–96 | Plein groove, microvariations de vélocité, start point, espace; alternance A/B toutes les 8/16 mesures | Identité stable malgré détail changeant |
| 97–112 | Contraste de registre ou accord, texture plus chaude; garder fragment commun | Reconnaissance de la cellule |
| 113–128 | Retour, puis sortie DJ progressive par retrait de couches | Mixabilité et résolution |

À 124 BPM, 128 mesures ≈ 4 min 08 s. Ne pas imposer cette longueur: couper à 96 ou étendre si la dramaturgie le justifie. Mettre des locators et une feuille entrée/sortie de chaque piste. Changer un paramètre notable à la fois pour attribuer son effet.

## Mix et livrables

Kick et basse: vérifier les notes de basse individuellement, queues et polarité; pas de sidechain automatique fort si les silences suffisent. Micro-percussions: filtrer et placer en profondeur selon rôle, sans largeur artificielle systématique. Glitches: conserver transient, réduire les fréquences agressives après écoute et ne pas confondre « détail audible » avec « plus fort ». Tester boucle de 8 mesures puis 128 mesures à faible niveau, mono et casque; comparer deux références dans des sections homologues à volume perçu égal. Exporter mix, stems kick/basse/percussions/tonal/FX, versions sans bus FX et liste des sources enregistrées/licences. Ne dire « prêt à diffuser » qu'après écoute du rendu réel et contrôle technique de toute la piste.
