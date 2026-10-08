# Sources de partitions fiables et exploitables

## Encodages Humdrum **kern (GitHub, curl direct, exacts)
- `https://raw.githubusercontent.com/craigsapp/<dépôt>/master/kern/<fichier>.krn` — dépôts connus : `beethoven-piano-sonatas` (sonata01-1 … sonata32-4 ; l'Appassionata = `sonata23-1.krn`, 12/8, vérifié le 13 sept. 2026), `mozart-piano-sonatas`, `haydn-piano-sonatas`, `chopin-mazurkas`, `chopin-preludes`, `bach-370-chorales`, `scarlatti-keyboard-sonatas`, `joplin` (rags), `beethoven-string-quartets`. Essayer `master` puis `main`.
- Convention kern : `c` = C4 (do central), `cc` = C5, `C` = C3, `CC` = C2 ; `-` bémol, `#` dièse, `n` bécarre ; durée = inverse de la ronde (`4` noire, `8.` croche pointée, `12` triolet de croche), `[` `]` liaisons, `q` note d'agrément, `r` silence, `=N` barres de mesure numérotées, premier spine = main gauche (staff2). **Ableton nomme une octave plus bas : C4 kern = C3 Ableton = MIDI 60.**

## MusicXML / MIDI / LilyPond
- OpenScore (musescore.com/openscore) : intégrales Lieder, sonates de Beethoven… en MusicXML, domaine public (téléchargement par `../../partition-telechargement/scripts/openscore.sh`).
- Mutopia (mutopiaproject.org) : LilyPond + PDF + MIDI, licence libre ; recherche par compositeur.
- Wikimedia Commons : fichiers `.mid` et images de partitions pour les thèmes très connus.
- piano-midi.de (MIDI d'interprétation, tempo rubato : hauteurs fiables, rythme à requantifier) — téléchargement direct souvent bloqué.

## IMSLP (PDF, domaine public)
- Page œuvre : `https://imslp.org/wiki/<Titre>_(<Compositeur>)` ; liens `Special:ImagefromIndex/<id>` → avertissement → page d'attente 15 s → PDF. `curl` reçoit une redirection JavaScript : utiliser le navigateur intégré (navigate, accepter « I understand », attendre, screenshot/zoom du premier système) et transcrire à l'œil, mesure par mesure, en vérifiant que les durées remplissent la signature.

## Vérifier une transcription
- Somme des durées de chaque mesure = signature ; liaisons résolues ; anacrouse comptée.
- Recouper avec une seconde source ou avec la connaissance de l'œuvre (armure, tonalité, premier accord).
- Conserver l'URL et la date de consultation dans la mémoire du projet.
