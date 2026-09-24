---
titre: "GiantSteps key dataset (Knees, Faraldo et al., ISMIR 2015) — README + tonalités manuelles de 604 extraits Beatport par sous-genre (tech house, deep house, progressive house, electro house, house, trance…)"
source: https://raw.githubusercontent.com/GiantSteps/giantsteps-key-dataset/master/README (+ sources.xlsx du même dépôt, + giantsteps-mtg-key-dataset/annotations/annotations.txt)
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: théorie spécifique (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Jeu de données académique [DOC] : annotations de tonalité corrigées manuellement (forums Beatport), genre lu dans le JSON du site. Référence : Knees, Faraldo, Herrera, Vogl, Böck, Hörschläger, Le Goff, « Two data sets for tempo estimation and key detection in electronic dance music annotated from user corrections », ISMIR 2015.

# README (texte intégral)

```
name:             GiantSteps (key)

contact:          Peter Knees <peter.knees@jku.at>
                  Ángel Faraldo <angel.faraldo@upf.edu>
                  Richard Vogl <richard.vogl@jku.at>

description:      collection of annotations for 604 2min(1) audio previews from
                  www.beatport.com

reference:        Peter Knees, Ángel Faraldo, Perfecto Herrera, Richard Vogl,
                  Sebastian Böck, Florian Hörschläger, Mickael Le Goff: "Two data
                  sets for tempo estimation and key detection in electronic dance
                  music annotated from user corrections," Proc. of the 16th
                  Conference of the International Society for Music Information
                  Retrieval (ISMIR'15), Oct. 2015, Malaga, Spain.

annotations:      key

content:
=========================================================================
audio/                   original audio files in mp3 format
md5/                     md5 hashes of original audio files
annotations/genre/       genre annotations
annotations/key/         key annotations
annotations/giantsteps/  annotations in the GiantSteps project format
annotations/jams/	 annotations in the JAMS (https://github.com/marl/jams) format

notes:
=========================================================================
The audio files (604 files, size ~850Mb) can be downloaded from http://www.beatport.com/
using the bash script:

./audio_dl.sh

To download the files manually use links of the following form:
http://geo-samples.beatport.com/lofi/<name of mp3 file>
e.g.:
http://geo-samples.beatport.com/lofi/5377710.LOFI.mp3

To convert the audio files to .wav use (bash + sox):

./convert_audio.sh

To retrieve the genre information, the JSON contained within the website was parsed.
The key annotation was extracted from forum entries of people correcting the key annotations (i.e. manual annotation of tempo).
For more information please contact creators.


(1): Most of the audio files are 120 seconds long. Exceptions are:
name              length
1224698.LOFI.mp3  45
1442809.LOFI.mp3  62
3424038.LOFI.mp3  77
4452003.LOFI.mp3  59


```

# Annexe (calcul local, mode synthese) : tonalités manuelles par sous-genre Beatport, d'après `sources.xlsx` du dépôt (colonnes TRACK, SOURCE, GLOBAL KEY, BEATPORT KEY, SUBGENRE, AUDIO LINK, ARTIST, TRACK)

« mineur » = part des tonalités manuelles (GLOBAL KEY) en mode mineur ; « accord » = part des titres où l'annotation automatique de Beatport (BEATPORT KEY) coïncide avec l'annotation manuelle.

| Sous-genre | n | mineur | accord Beatport/manuel | tonalités les plus fréquentes | toniques |
|---|---|---|---|---|---|
| TOUT | 604 | 85 % | 29 % | F minor 12 %, G minor 10 %, A minor 9 %, C minor 9 %, E minor 8 %, D minor 7 % | F 14 %, G 12 %, C 11 %, A 11 %, E 10 % |
| progressive-house | 88 | 76 % | 18 % | A minor 14 %, E minor 9 %, F minor 8 %, G minor 7 %, C minor 7 %, B minor 7 % | A 15 %, C 11 %, E 10 %, G 9 %, F 9 % |
| tech-house | 81 | 88 % | 40 % | D minor 16 %, C minor 11 %, Eb minor 11 %, F minor 10 %, A minor 10 %, Ab minor 6 % | D 16 %, C 12 %, A 12 %, F 11 %, Eb 11 % |
| deep-house | 77 | 95 % | 55 % | C minor 13 %, Bb minor 12 %, B minor 10 %, E minor 10 %, Eb minor 9 %, D minor 8 % | C 13 %, Bb 12 %, B 12 %, E 10 %, Eb 9 % |
| trance | 58 | 88 % | 9 % | F minor 24 %, C minor 9 %, E minor 9 %, Eb minor 9 %, Ab minor 7 %, Db minor 7 % | F 24 %, E 12 %, C 9 %, Eb 9 %, Bb 9 % |
| electro-house | 51 | 90 % | 8 % | F minor 25 %, G minor 16 %, A minor 12 %, E minor 10 %, C minor 8 %, Ab minor 8 % | F 25 %, G 16 %, A 14 %, E 12 %, C 8 % |
| house | 47 | 83 % | 40 % | G minor 13 %, C minor 13 %, A minor 11 %, E minor 9 %, B minor 9 %, Eb minor 6 % | C 17 %, G 15 %, A 15 %, Eb 11 %, E 9 % |
| drum-and-bass | 38 | 82 % | 16 % | G minor 32 %, F minor 21 %, Bb minor 5 %, A minor 5 %, Ab major 5 %, Gb minor 5 % | G 34 %, F 24 %, Gb 8 %, Bb 5 %, B 5 % |
| techno | 34 | 82 % | 24 % | C minor 18 %, Ab minor 15 %, D minor 9 %, Gb minor 9 %, A minor 9 %, G minor 9 % | C 21 %, Ab 18 %, A 12 %, D 9 %, Gb 9 % |
| dubstep | 22 | 91 % | 18 % | F minor 23 %, Gb minor 14 %, E minor 14 %, G minor 14 %, A minor 14 %, B major 5 % | F 23 %, Gb 18 %, E 14 %, G 14 %, A 14 % |
| electronica | 20 | 80 % | 25 % | F minor 20 %, Eb minor 15 %, Gb minor 15 %, Db minor 10 %, G major 5 %, E major 5 % | Eb 20 %, F 20 %, Gb 15 %, E 10 %, Db 10 % |
| breaks | 14 | 71 % | 21 % | C major 21 %, Bb minor 14 %, Db minor 14 %, C minor 14 %, D major 7 %, D minor 7 % | C 36 %, D 14 %, Bb 14 %, Db 14 %, A 7 % |
| indie-dance nu-disco | 14 | 79 % | 57 % | E major 14 %, B minor 14 %, A minor 14 %, D minor 14 %, G minor 14 %, F major 7 % | E 14 %, B 14 %, A 14 %, D 14 %, G 14 % |
| minimal | 11 | 100 % | 18 % | E minor 27 %, A minor 27 %, G minor 18 %, C minor 9 %, Bb minor 9 %, Eb minor 9 % | E 27 %, A 27 %, G 18 %, C 9 %, Bb 9 % |
| chill-out | 11 | 64 % | 36 % | Ab major 18 %, E minor 18 %, D minor 18 %, Db minor 9 %, F major 9 %, F minor 9 % | Ab 18 %, E 18 %, F 18 %, D 18 %, Db 9 % |


## Complément : GiantSteps-MTG key dataset (1486 extraits Beatport, annotations manuelles, sans genre) — https://raw.githubusercontent.com/GiantSteps/giantsteps-mtg-key-dataset/master/annotations/annotations.txt

n = 1486 ; mineur = 66 % ; tonalités les plus fréquentes : C minor (127), F minor (122), E minor (94), D minor (86), C# minor (85), G minor (74), A minor (74), B minor (63), D# minor (53).
