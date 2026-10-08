# Maîtriser Suno

> Module du skill `producteur-live`. Maîtriser Suno (v6, v6-wild, v6-mini) et Suno Studio 2.0 pour un morceau, un instrumental, une maquette ou une matière à reprendre dans Ableton Live 12 — brief en mesures, champs Style et Lyrics à copier, curseurs Weirdness / Style Influence / Audio Influence, Cover, Extend, Replace Section, Remaster, Studio (MIDI, Chat, effets, automation), stems, MIDI, export vers Live, Original Mix et Extended Mix, droits. Utilise ce skill dès que l'utilisateur parle de Suno, d'un prompt Suno, d'une génération à corriger ou prolonger, de stems ou de MIDI Suno, de Suno Studio, ou d'une idée Suno à reconstruire dans Live. Voix seules à poser sur un instru existant → suno-vocals.

## Cadre
- **L'agent rédige, planifie et mesure ; l'utilisateur génère et écoute.** Aucun agent n'a accès au compte Suno ni n'écoute un rendu (règle 4 d'`AGENTS.md`) : ne jamais écrire « j'ai écouté », « la génération respecte… ». Ce qui se mesure (fichier exporté, MIDI, repères dans Live sur le Mac) se mesure ; le reste se fait écouter à l'utilisateur.
- **Un prompt est une intention, jamais une partition.** BPM, tonalité, mesures, voix et instruments décrits orientent un modèle génératif sans le garantir. Note, timing, durée en mesures ou timbre exacts : partir du MIDI ou de l'audio **original** de l'utilisateur et corriger localement (Studio ou Live).
- **Faits datés.** Modèles, plans, limites et menus changent : `references/sources-et-fonctions.md` dit ce qui a été vérifié, quand et comment. Revérifier sur le compte avant de prescrire une fonction payante ou une durée.
- **Droits.** Ne téléverser (upload, Cover, Audio Influence) que du matériau dont l'utilisateur détient les droits : jamais un titre du commerce, même comme « référence ». Une référence se décrit par ses traits (groove, timbre, structure, énergie), sans nom d'artiste dans le champ Style. L'usage commercial suppose un abonnement payant **au moment de la génération** (pas de rattrapage rétroactif) et ne garantit pas une protection par droit d'auteur ; vérifier aussi les conditions du distributeur.

## Avec quels skills
- Voix seules sur un instru existant (voix malgaches ou africaines, appel-réponse, bus VOIX, calage par section) → `suno-vocals`, qui applique ce cadre.
- Démo VIBRA (référence choisie avec l'utilisateur, une à quatre émotions, noyau de 8 mesures) → `produire-demo-electro-rapide` et `composer-trajectoire-emotionnelle` ; Suno y sert de maquette ou de matière, jamais de master.
- Batterie, kick, sub et mid-bass refaits dans Live → `producteur-rythmique`, `drums-signature`, `serum-2-basses-house-future-house`, `kick-bass-equilibre`.
- Import, warp, découpe, impression dans Live → `ableton-live-session` (discipline) et `resampling` ; mesure d'un fichier (durée, crête, écrêtage) → `python3 ../../../ingenieur-mixage/modules/live-export-wav/scripts/analyze_wav.py`.
- Journal des essais → `memoire-projet` (`../memoire-projet/scripts/journal.sh`).

## Workflow en huit étapes
1. **Brief.** But (démo, voix, sample, morceau), genre, BPM, tonalité, une ambiance et une à quatre émotions dont une dominante, instrumentation, format (Original / Extended), langue et paroles, durée, référence choisie **avec** l'utilisateur et décrite par traits, éléments intouchables, plan Suno (Free, Pro, Premier) dès qu'une fonction en dépend.
2. **Fiche d'arrangement en mesures**, avec le rôle de chaque section. `secondes = mesures × 4 × 60 / BPM` : 8 mesures = 16 s à 120 BPM, 15,48 s à 124, 15,24 s à 126, 15 s à 128 `[CALC]`. Prévenir que les mesures demandées dériveront dans l'audio généré.
3. **Choisir l'outil et le modèle** (tableau ci-dessous) ; vérifier sur le compte que l'outil existe pour ce plan.
4. **Rédiger Style et Lyrics.** Style : peu de descripteurs, les prioritaires d'abord (genre, BPM et feel, batterie et basse, harmonie, voix, humeur, texture, production) ; quatre à sept tiennent mieux qu'une longue liste `[HEUR]`. Lyrics : seulement ce qui doit être chanté, avec des repères simples `[Intro]`, `[Verse]`, `[Chorus]`, `[Bridge]`, `[Instrumental]`, `[Outro]` (indications empiriques, pas un langage garanti). Instrumental pur : activer Instrumental et laisser Lyrics sans texte à chanter. Ni consignes contradictoires, ni nom d'artiste.
5. **Curseurs** (mode Custom). Weirdness vers 50 % au départ : plus bas = versions plus sages, plus haut = davantage d'écarts. Style Influence vers Strong si le style est ignoré. Audio Influence seulement avec un upload. Aucune valeur n'impose une mesure, une voix ou une hauteur.
6. **Deux à quatre essais, une seule variable changée par essai.** Nommer chaque version ; noter modèle, plan, Style, Lyrics, source audio ou MIDI, curseurs, date (gabarit dans `references/recettes-vibra.md`, entrée par `journal.sh`). L'utilisateur écoute contre la fiche : tempo, tonalité, entrée et sortie, motif, phrasé, paroles, kick et basse, énergie, artefacts, longueur. Garder la meilleure version avant de réessayer.
7. **Corriger localement plutôt que tout régénérer** : Replace Section (sélection + nouvelle description ou nouvelles paroles), Extend depuis un point choisi puis Get Whole Song, Remaster Subtle si structure et interprétation plaisent, Studio pour couper, déplacer, remplacer, automatiser. Faire réécouter les jonctions ; conserver les versions source.
8. **Exporter et reprendre dans Live** (procédure ci-dessous) ; Original Mix et Extended Mix sortent du même arrangement maître, vérifiés et exportés séparément.

| Besoin | Outil Suno | Note |
|---|---|---|
| Esquisse rapide, volume d'idées | v6-mini | tous les plans, Free compris |
| Rendu fidèle au brief | v6 | Pro ou Premier ; jusqu'à 8 min par génération |
| Exploration | v6-wild | Pro ou Premier ; résultats moins prévisibles |
| Guider par un brouillon original | Audio Upload + Audio Influence | 60 s en Free, 8 min en Pro et Premier (aide Suno, à revérifier) |
| Changer de style en gardant la mélodie | Cover | réinterprète des détails, ne reproduit pas chaque mesure |
| Allonger | Extend, puis Get Whole Song | réécouter la jonction |
| Refaire une partie | Replace Section | une section à la fois |
| Polir sans changer | Remaster Subtle (Normal, High = plus d'écarts) | High peut changer voix et éléments |
| Notes exactes, montage, stems, MIDI | Studio 2.0 | **Premier** ; pas de VST/AU : Serum 2, FabFilter, Waves restent dans Live |

## Export vers Live (sur le Mac)
1. Depuis Studio : Full Song, Selected Time Range, Multitrack (ZIP), WAV par clip ; stems par Get Stems (Advanced Split) ; MIDI d'un stem par Get MIDI (payé en crédits). Garder les fichiers d'origine intacts.
2. Dans Live, Set sauvé sous un nouveau nom et état relu (règle 2 d'`AGENTS.md`) : WAV rangés dans le dossier `Samples/Imported` du projet, une piste par stem, départ à 1|1.
3. Warp : premier marqueur sur le premier temps fort, puis contrôle aux repères toutes les 8 mesures ; Suno reconnaît des générations en avance ou en retard sur le temps (tempo drift) : poser des marqueurs plutôt que forcer un seul tempo. Complex Pro pour voix et mix, Beats pour batterie.
4. MIDI importé : **le numéro de note fait foi** (Live affiche C3 = 60) ; relire deux ou trois notes connues avant d'écrire autour.
5. Reconstruire kick, sub et mid-bass avec les instruments du projet (sub et mid-bass dans deux instruments, sub mono ; sous 124 BPM, signature de kick VIBRA) ; garder de Suno voix, textures ou parties harmoniques. Pas de nouvel effet natif de Live dans les chaînes de mix.
6. Mesurer ce qui se mesure (`analyze_wav.py` : durée, crête, écrêtage) ; demander à l'utilisateur d'écouter phase, transitoires et artefacts de séparation.

## Sortie attendue à chaque demande
(a) fiche courte des contraintes ; (b) contenu exact à copier dans **Style** et dans **Lyrics**, en deux blocs séparés ; (c) outil, modèle et curseurs choisis ; (d) protocole de deux à quatre essais, une variable par essai ; (e) points d'écoute pour l'utilisateur et corrections possibles ; (f) étape d'export vers Live si demandée ; (g) ligne de journal prête pour `journal.sh`. Vérifier la prosodie, la langue et les répétitions des paroles. Commande musicale exacte demandée : donner en plus notes (numéros MIDI, C3 = 60), accords et mesures pour Live, et dire ce qui restera à contrôler à l'oreille dans Suno.

## Références
- `references/sources-et-fonctions.md` : fonctions, plans et limites, avec date et mode de vérification.
- `references/tutoriels-video.md` : notes horodatées des sept tutoriels officiels de Studio 2.0, raccourcis vérifiés.
- `references/recettes-vibra.md` : prompts de départ VIBRA, protocole d'essais, gabarit de journal.
