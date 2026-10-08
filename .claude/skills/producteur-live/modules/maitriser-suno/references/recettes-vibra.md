# Recettes de départ VIBRA

Hypothèses d'essai, à faire écouter et comparer par l'utilisateur. Ne jamais demander à Suno de reproduire une œuvre ou un artiste : décrire des traits. Préférer un motif original de l'utilisateur (MIDI ou audio) pour garder son identité. Règles VIBRA qui s'appliquent après Suno, dans Live (`AGENTS.md`) : sub et mid-bass dans deux instruments, sub mono ; **sous 124 BPM**, kick de signature Serum 2 doux, clair et chaleureux, hats fins, clap net et discret, refaits dans Live (le kick de Suno n'est qu'un repère) ; variation audible de batterie ou de transition avant chaque frontière de 8 mesures des drops, en alternant les gestes ; Original Mix et Extended Mix issus du même noyau.

Chaque recette donne un Style long (description complète) et un Style court (sept descripteurs au plus, à essayer si le long est mal suivi `[HEUR]`).

## 1. Deep chill minimal house, 120 BPM, fa mineur

**Style long**
```
Deep chill minimal house, 120 BPM, F minor, warm soft 808-like kick, fine closed hats, intimate clap, round restrained sub, soulful legato mid-bass, sparse Rhodes voicings, nocturnal but comforting, gradual tension and release, spacious clean production, instrumental breaks
```
**Style court**
```
Deep minimal house, 120 BPM, F minor, soft warm kick and fine hats, round sub with legato mid-bass, sparse Rhodes chords, nocturnal comforting mood
```
**Lyrics / structure de départ**
```
[Intro]
Take your body, mind and soul
Let the bass bring us home

[Instrumental]

[Verse]
The city breathes beneath the light
We move in time across the night

[Chorus]
Take your body, mind and soul
Let the bass bring us home

[Instrumental]

[Bridge]
Only the rhythm knows the way

[Outro]
```
120 BPM est sous 124 : kick, hats et clap de signature refaits dans Live. Instrumental pur : activer Instrumental et ne pas fournir de paroles à chanter. Repérer la longueur des sections dans la forme d'onde ; reconstruire les 16 ou 32 mesures exactes dans Live ou dans Studio.

## 2. Bass house à drop contrasté, 126 BPM, la mineur

**Style long**
```
Bass house, 126 BPM, A minor, punchy four-on-the-floor kick, tight fine hi-hats and clap, syncopated metallic mid-bass with short legato replies, clean separate sub, confident rhythmic female vocal hook, sparse verses, rising tension, dry club-focused drop, controlled stereo width
```
**Style court**
```
Bass house, 126 BPM, A minor, punchy kick with tight hats and clap, syncopated metallic mid-bass, confident female vocal hook, dry club-focused drop
```
**Lyrics**
```
[Intro]
[Verse]
Your move, my move, watch the light
[Chorus]
It's a sexy game tonight
[Instrumental]
[Bridge]
Noch ein Schritt, wir sind bereit
[Chorus]
It's a sexy game tonight
[Outro]
```
Faire juger l'intelligibilité de l'anglais et de l'allemand séparément (un essai par langue). Drop : dans Live, varier la fin de chaque bloc de 8 mesures en alternant fill, reverse, retrait momentané de la basse ou du kick, impact, silence ; ne pas supposer que Suno respecte ces repères. Mid-bass métallique : recette FH Metal FM (`docs/projets/projet-test-basse-future-house.md` à la racine du dépôt) ou `serum-2-basses-house-future-house`.

## 3. Cover d'un brouillon original exporté de Live
Pour donner à Suno le thème exact de l'utilisateur (hook, chant témoin, accords).
1. Dans Live, exporter 8 à 16 mesures du brouillon **original** (aucun sample du commerce), en WAV, départ sur un temps fort ; noter BPM et tonalité.
2. Suno : upload (60 s en Free, 8 min en Pro et Premier, à revérifier), puis Cover avec un Style court ; Audio Influence haute pour garder la mélodie.
3. Trois essais, une variable : Audio Influence haute, moyenne, basse ; ou Style court avec trois timbres de voix. L'utilisateur juge : mélodie gardée, phrasé, artefacts.
4. Garder la meilleure ; Get Stems ; ne reprendre dans Live que la voix ou la texture voulue (procédure d'export du `GUIDE.md`).

## De l'esquisse à la sortie
1. Donner à Suno un hook original court venu de Live, un chant témoin ou un MIDI dont l'utilisateur a les droits.
2. Générer des idées de voix, d'arrangement ou de textures ; noter les crédits dépensés ; conserver les originaux.
3. Garder la meilleure interprétation ; extraire voix, textures ou parties harmoniques ; faire écouter les artefacts.
4. Refaire batterie, kick, sub, mid-bass legato et transitions dans Live avec Serum 2 ou Maschine ; grave mono, sidechain.
5. Dupliquer l'arrangement final pour Original Mix et Extended Mix ; intro et outro DJ par sections mesurées ; vérifier et exporter les deux versions séparément.

## Journal d'essais
Une ligne par essai, dans la mémoire de projet (`../memoire-projet/scripts/journal.sh <slug> "<texte>"`) :

`Date | objectif | modèle | plan | Style | Lyrics | audio ou MIDI source | curseurs | version | BPM mesuré | tonalité jugée | défaut majeur | action suivante`

« BPM mesuré » vient des marqueurs de warp dans Live ; « tonalité jugée » et « défaut majeur » viennent de l'écoute de l'utilisateur, jamais d'une supposition de l'agent.
