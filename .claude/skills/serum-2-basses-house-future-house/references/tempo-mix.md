# Changement de BPM, groove et mix

Noire = 60 000/BPM ms, croche = 30 000/BPM, double croche = 15 000/BPM. À 126 BPM : 476,2 / 238,1 / 119,0 ms; à 124 : 483,9 / 241,9 / 121,0 ms; à 174 : 344,8 / 172,4 / 86,2 ms. Pour préserver la proportion métrique d'une enveloppe en ms : durée nouvelle = durée ancienne × BPM ancien/BPM nouveau. Exemple : 200 ms à 126 → 145 ms à 174. Recontrôler l'articulation à l'oreille.

Une LFO synchronisée à 1/8 reste à 1/8 mais change de vitesse physique. Pour garder la même vitesse absolue, choisir Hz ou une autre division. Pointées, triolets et swing demandent une décision musicale. BPM seul ne transpose aucune note. En audio resamplé, choisir un algorithme de warp qui garde la hauteur et écouter les transitoires.

House 124–128 : repérer les quatre kicks; placer pluck/wub dans les espaces ou contretemps. DnB 170–176 : réécrire autour du kick et de la caisse claire du break, ménager de longs trous. À 126→174, le wub 1/8 passe de 238,1 à 172,4 ms; un decay 240 ms devient environ 174 ms. La ligne MIDI doit être recomposée selon la batterie, et les queues revues.

Séparer `SUB` et `MID` pour unison, pitch mobile, gros formants ou FX larges. Router à un bus basses. Un crossover de départ 80–120 Hz se déplace selon la note et le kick; pas de valeur universelle. Ajuster timing, longueur MIDI, phase et ducking en écoutant kick/sub ensemble. Vérifier les pics mobiles du growl, les crêtes du screech, le mono, plusieurs notes, les extrêmes des macros, faible volume et une référence égalisée en niveau. Conserver MIDI et preset lors du resampling; Live 12 Bounce to New Track donne une version audio dont il faut contrôler le point de capture et le routage.

## Dans ce workflow

- **Kick / sub** : qui tient le fondamental, accord du kick, phase et polarité, corrélation 30–120 Hz mesurée sur des exports séparés : `../../kick-bass-equilibre/SKILL.md` (`kick_bass_check.py`) ; table kick/sub d'une tonique : `../../theorie-musicale-electronique/scripts/theorie.py sub F`.
- **Traitements après Serum** : plug-ins tiers seulement (règle 6 d'`../../ableton-live-session/SKILL.md`) ; Utility (mono du grave, trim, phase) et un Compressor en sidechain déjà en place sont tolérés. Ce qui appartient au son (distorsion, Hyper, chorus, OTT) reste dans les effets internes de Serum 2. Chaînes de bus : `../../effets-plugins/SKILL.md`.
- **Niveaux** : `lom.py meters` ne donne que des valeurs relatives (avant/après, piste contre piste) ; pour un chiffre fiable, exporter et analyser (`../../live-export-wav/SKILL.md`).
- **Impression audio** : `../../resampling/SKILL.md` (point de capture, routage, piste source désactivée gardée).
- **Durées en ms** : même règle que `../../composer-hooks-funk-electro/references/sound-design.md` — ne multiplier par le rapport de BPM que ce qui doit garder sa proportion métrique ; attaque, glide et release expressifs restent en temps absolu.
