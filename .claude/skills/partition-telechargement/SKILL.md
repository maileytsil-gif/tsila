---
name: partition-telechargement
description: Télécharger réellement en ligne le fichier d'une partition (MIDI, LilyPond, MusicXML/MSCZ, kern, PDF) d'un morceau connu et le ranger dans le projet — Mutopia et OpenScore (téléchargement direct par script), dépôts kern GitHub, IMSLP et MuseScore (via le navigateur Chrome de l'utilisateur, fichier récupéré dans ~/Downloads), puis vérifier le fichier obtenu et l'ouvrir (PDF lisible page par page, MIDI/kern convertis en notes). Utilise ce skill dès que l'utilisateur veut « télécharger », « récupérer », « aller chercher » une partition, un MIDI ou un PDF d'une œuvre, ou nomme IMSLP, Mutopia, MuseScore, OpenScore. Pour choisir la source la plus fiable et convertir les notes vers Live, voir aussi partition-recherche.
---
Règles communes (capacités vérifiées, session préservée, relecture après chaque écriture, une étape par échange, jamais « entendu » sans mesure) : `../ableton-live-session/SKILL.md` § Discipline ; mémoire et instantanés : `../memoire-projet/SKILL.md`.

# Télécharger une partition et la rendre exploitable

## 0. Droit d'auteur et rangement
Domaine public seulement pour une reproduction (compositeur mort depuis plus de 70 ans) ; sinon analyse/référence courte. Tout fichier va dans `~/Desktop/1 Project/Partitions/<Compositeur>/` (créer le dossier), nom = `<compositeur>-<oeuvre>-<source>.<ext>` ; noter l'URL et la date dans la mémoire du projet.

## 1. Sources à téléchargement direct (scripts, sans navigateur)
- **Mutopia** (LilyPond + MIDI + PDF, licence libre) : `scripts/mutopia.sh chercher <CodeCompositeur> [motif]` liste les fichiers (`ftp/...`), puis `scripts/mutopia.sh prendre <chemin ftp> [dest]`. Codes = nom + initiale (SatieE, BachJS, ChopinFF, DebussyC, BeethovenLv, MozartWA, SchubertF…) ; le script les devine à partir d'un nom.
- **OpenScore** (MuseScore .mscz/.mxl, domaine public, GitHub `OpenScore/Lieder` et `OpenScore/StringQuartets`) : `scripts/openscore.sh chercher <fragment>` et `scripts/openscore.sh prendre <chemin> [dest]`.
- **Humdrum kern** (sonates Beethoven/Mozart/Haydn, Chopin, Bach…) : `../partition-recherche/scripts/fetch_kern.sh <dépôt> <fichier>`.
- **Wikimedia Commons** : `curl` direct sur `upload.wikimedia.org` (MIDI/PNG/PDF de thèmes célèbres).

## 2. Sources qui exigent un navigateur
- **IMSLP** (PDF scannés) : `curl` reçoit une redirection JavaScript. Deux voies : (a) **Claude in Chrome** (outils `mcp__claude-in-chrome__*`, charger via ToolSearch) dans le Chrome de l'utilisateur : ouvrir la page de l'œuvre, cliquer le fichier, « I understand », attendre la page « download will start in 15 s », le PDF tombe dans `~/Downloads` → le déplacer dans Partitions ; (b) navigateur intégré (`navigate`) pour **lire** la partition à l'écran (zoom sur le premier système) sans fichier. Toujours vérifier la taille et l'ouverture du PDF (`Read` avec `pages`).
- **musescore.com** (hors OpenScore) : compte requis et œuvres souvent protégées ; préférer OpenScore.
Ne jamais contourner un délai/anti-robot autrement qu'en attendant ; ne pas télécharger depuis des sites de partitions piratées.

## 3. Vérifier et ouvrir
- `file`, taille, durée (MIDI : `scripts/midi_to_notes.py fichier.mid --resume` donne tempo, signature, pistes, nombre de notes) ; PDF : `Read` page 1–3 pour confirmer l'œuvre et l'édition.
- Convertir en notes : MIDI → `midi_to_notes.py --json` (mesures calculées d'après la signature du fichier ; MIDI d'interprétation = rythme rubato à requantifier) ; kern → `../partition-recherche/scripts/kern_to_notes.py` ; LilyPond → générer le MIDI avec `lilypond` s'il est installé, sinon lire le `.ly` ; MusicXML/.mscz → `.mxl` est un zip : `unzip -p` puis parser XML (parties, mesures, `<pitch>`, `<duration>`, `<divisions>`).
- Ensuite `../partition-recherche/scripts/notes_to_ppal.py` pour la notation Producer Pal et la grille du projet.
