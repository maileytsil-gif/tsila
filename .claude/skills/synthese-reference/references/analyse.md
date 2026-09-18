# Analyse du son de référence

## Écoute et séparation des indices
Conserver le fichier original et travailler sur un extrait. Relever le timecode exact, le canal choisi et toute conversion. Éviter warp, normalisation ou traitement caché de la référence. Un réglage de volume temporaire pour comparer doit rester distinct du fichier original.

Examiner séparément :

| Partie | À relever | Ambiguïtés à conserver |
|---|---|---|
| Hauteur et jeu | Note, accordage, glissando, retrigger, legato, vélocité | Fondamentale absente, octave, accord, pitch envelope |
| Attaque | Départ net/lent, clic/bruit, balayage de hauteur ou de filtre | Compression, réverbération précoce, percussion superposée |
| Tenue | Partiels, stabilité, battements, densité et bruit | Filtrage, unisson, chorus, distorsion peuvent se ressembler |
| Relâchement | Décroissance et coloration après la note | Release du synthé, reverb et feedback de delay ne sont pas identiques |
| Mouvement | Vibrato, PWM, balayage spectral, pulsation et périodicité | LFO libre, synchro, séquence, sidechain ou automation de mix |
| Stéréo | Centre, largeur, mouvement latéral, perte en mono | Unisson, double prise, délai court ou décor réverbéré |

Les harmoniques majoritairement impaires peuvent suggérer une onde carrée ; un spectre riche peut évoquer une dent-de-scie ; des partiels non harmoniques peuvent orienter vers FM ou une source inharmonique. Ce sont des hypothèses à tester, pas une identification automatique. Un filtre, une distorsion et le mix environnant changent ces indices.

Décrire le degré d'évidence en termes concrets : « battements audibles dans la tenue », « oscillateur exact indéterminé », « queue pouvant venir d'une reverb ». Sans écoute accessible, ne pas transformer une mesure en observation auditive.

## Mesurer sans surinterpréter
Sur une note stable, estimer f0 et examiner les rapports harmoniques ; vérifier l'octave en jouant la note candidate. Sur une basse avec fondamentale faible, le pic le plus fort n'est pas forcément f0. Sur un accord ou une texture bruitée, ne pas forcer une note unique.

Observer l'enveloppe par fenêtres courtes. Une enveloppe audio mesurée n'est pas directement l'ADSR du synthé : durée MIDI, filtre, compression, chorus et reverb y contribuent. Décrire l'attaque et la queue avant de proposer des réglages de départ.

Comparer un spectre de l'attaque et de la tenue, pas seulement un spectre moyen. Indiquer la fenêtre et la résolution ; une largeur de pic peut provenir du fenêtrage plutôt que de l'unisson. Pour une pulsation, observer plusieurs cycles avant de conclure au tempo ou à une subdivision.

## Analyseur inclus
Le script demande Python 3 avec `numpy` et `soundfile` ; les dépendances sont listées dans `scripts/requirements.txt`. Employer les bibliothèques déjà disponibles ; si une installation est nécessaire, utiliser un environnement de travail isolé, selon les permissions de l'environnement. Le script ne contacte aucun service, ne charge aucun plug-in et ne modifie pas le fichier audio.

Exemple, en remplaçant les chemins par ceux réellement accessibles :

```sh
python3 '/chemin/du/skill/scripts/analyze_synth.py' '/chemin/reference.wav' --start 1.2 --duration 3 --mono-note --output '/chemin/analyse-reference.json'
```

- `--start` : secondes depuis le début du fichier ; `--duration` : secondes à analyser, 8 par défaut, maximum 60.
- `--mono-note` : demander une estimation de hauteur uniquement si l'extrait est supposé monophonique. Omettre pour un mix ou un accord. `--fmin`/`--fmax` définissent la recherche, 30–2000 Hz par défaut.
- Le format est lu par libsndfile/soundfile : WAV/FLAC/AIFF courants selon l'environnement ; ne pas promettre tous les codecs. Le helper traite mono/stéréo, 8–192 kHz. Préparer explicitement une copie adaptée si nécessaire.
- L'analyse porte sur l'extrait, pas nécessairement le morceau entier. Le spectre et les estimations de hauteur utilisent le canal de RMS maximal pour éviter une annulation par sommation mono. La référence complète stéréo reste celle de l'écoute.
- L'enveloppe est mesurée par blocs de 10 ms ; le spectre utilise des fenêtres Hann et un centroïde pondéré par la puissance. Ses pics sont les centres des bins, pas des fréquences exactes d'oscillateurs.
- La périodicité provient d'une autocorrélation normalisée sur des fenêtres de 250 ms. Elle peut confondre octaves, harmonies, unisson et notes successives. Son indicateur n'est pas une probabilité de justesse. Les extraits trop courts ou insuffisamment périodiques ne reçoivent pas de hauteur.
- Les notes indiquent les deux conventions : scientifique C4=MIDI 60 et Ableton C3=MIDI 60, pour A=440 Hz.
- `null` signifie non défini/non mesuré (par exemple niveau nul), pas 0 dB. Les crêtes sont des sample peaks, pas des true peaks. Ni LUFS, ni détection certaine d'écrêtage, ni identité du synthé ne sont fournis.

Créer un nouveau rapport pour la reconstruction avec la même sélection pertinente. Utiliser les différences pour orienter l'écoute et les réglages ; ne pas réduire l'objectif à un rapprochement numérique des centroïdes.
