# Mode de départ : voix ou instrumental

Première décision du cadrage (`brief-de-demarrage.md`), avant toute composition. Poser la question une fois, avec quatre variantes, une raison entre parenthèses et une recommandation :

**Comment démarrer ce morceau ?**

1. **Voix d'abord avec Suno** : créer et choisir une voix ou une phrase vocale, puis construire tonalité, harmonie, groove, basse et arrangement autour de la prise **retenue**.
2. **Instrumental avec hook vocal** : base instrumentale d'abord, puis un hook vocal court (phrase, chop, motif chanté), généré ou fourni à part.
3. **Instrumental sans voix** : aucune partie vocale ; l'identité vient d'un hook instrumental.
4. **Voix ou sample déjà disponible** : composer autour d'une voix ou d'un sample fourni, après vérification de son contenu, de son tempo et de sa tonalité utiles, et des droits.

Ne poser que les précisions qui dépendent du choix :

- Voix d'abord : voix féminine, masculine ou duo, langue, sujet et paroles, caractère, mélodie chantée par l'utilisateur éventuelle, longueur du hook, références vocales décrites par traits, liberté laissée à Suno.
- Instrumental avec hook : type de vocal (phrase, chop, ad-lib, syllabe), langue, fonction rythmique ou mélodique, voix fournie ou à générer.
- Instrumental sans voix : instrument vedette et ce qui rend le thème mémorable.
- Voix fournie : fichier, droits, tempo et tonalité connus ou à mesurer.

## Voix d'abord avec Suno : passage de relais

L'agent rédige et planifie ; l'utilisateur génère et écoute (aucun agent n'a accès au compte Suno ni n'écoute une prise : règle 4 d'`AGENTS.md`). Prompts Style et Lyrics, curseurs, Cover, Extend, Studio, stems, MIDI, export vers Live, droits et état des fonctions : `../../maitriser-suno/GUIDE.md`. Voix seules à poser sur un instrumental existant : `../../suno-vocals/GUIDE.md`.

1. Établir le brief vocal et sa fonction dramatique (hook, refrain, couplet, intro, ad-lib). Les fonctions et plans de Suno changent : se référer à `../../maitriser-suno/references/sources-et-fonctions.md` et faire revérifier sur le compte.
2. Rédiger Style et Lyrics cohérents et demander quelques essais où **une seule** intention change. BPM, tonalité et mesures orientent la génération sans la verrouiller.
3. **L'utilisateur** écoute chaque sortie et choisit selon phrasé, syllabes, respirations, hauteur, groove et caractère, pas seulement la qualité de production.
4. Vérifier ce qui a été exporté : voix isolée, stem avec fuite d'instrumental, ou mix complet. Si l'isolation est imparfaite, utiliser la prise comme référence de composition et rechanter la ligne si besoin.
5. Établir tonalité et BPM de la prise retenue, par l'écoute de l'utilisateur ou par mesure du fichier s'il est accessible. Ne pas déformer la voix vers une tonalité supposée avant d'avoir vérifié sa mélodie ; corrections locales (édition, étirement, hauteur) contrôlées si besoin.
6. Repérer le rythme et les notes d'appui du chant (numéros MIDI, C3 = 60). Choisir ensuite progression, voicings et basse pour soutenir ces appuis et ces tensions, et construire kick et groove autour des respirations, consonnes, accents et fins de phrases.
7. Faire réécouter la voix dans le mix naissant avant l'arrangement complet. Drops, breaks et transitions servent la narration vocale et laissent un espace intelligible.

## Instrumental avec hook vocal

Composer un instrumental autonome avec une place claire pour le hook : registre et silences réservés, sans supposer le contenu exact. Quand le hook est choisi, ajuster groove, accords, appel-réponse et automation sur ses accents. Pour un chop : répétition, hauteur, articulation, clics, effets, intelligibilité (`textures-ambiances-rythmiques.md`, `../../../compositeur-arrangeur/modules/sampling-composition-avancee/GUIDE.md`).

## Instrumental sans voix

Construire le hook avec un instrument vedette ou une phrase entre instruments, en appliquant le test de chantabilité de `phrase-memorabilite-et-tension.md` : le thème doit rester reconnaissable sur un son neutre sans dépendre d'une voix implicite. Ne générer aucune voix par défaut.

## Droits et transparence

Vérifier les conditions de Suno et les droits du texte ou de l'audio importé avant toute diffusion. Conserver prompt, date, modèle ou version et choix de prise (`../../memoire-projet/scripts/journal.sh`). Ne jamais annoncer que les stems sont parfaits ou que la voix est isolée sans l'avoir contrôlé.
