# projet — funk is not dead

> Fichier créé depuis la session cloud (analyse audio hors Live) le 2026-09-22.
> **À recopier ou fusionner dans la mémoire projet locale**
> (`~/.claude/projects/-Volumes-NO-NAME-caude/memory/`) au début de la prochaine séance locale.

## REPRISE

**État.** Le morceau existe en audio généré (2:09, 64 mesures). Aucune production Ableton n'a encore
été faite depuis cette session. L'analyse audio de la version existante est terminée et chiffrée
ci-dessous.

**Décisions prises par l'utilisateur (2026-09-22).**
- Pour le break : **un nouveau solo dans l'esprit** de celui de la version audio — pas une
  transcription de l'existant.
- Le son : **patch reconstruit dans Serum 2** (pas le stem audio tel quel).

**En attente.**
- Où tombe le break dans le Set en cours (la version audio a son solo aux mesures 34–58, mais le Set
  peut différer — relire l'état réel avant de décider).
- Le mécanisme d'écriture des bends (enveloppe de clip MIDI / glide du synthé / automation) —
  à trancher d'après ce que les outils locaux savent réellement faire.

**Prochaines étapes.** Plan complet en 9 étapes, voir la section « Plan » plus bas.

---

## Mesures de la version audio existante

Source : `Synthesizer_Solo_Electro-Funk_Style.wav` (morceau complet) et `funk_is_not_dead.wav`
(stem synth extrait par Ableton, contenant claviers d'accompagnement **et** lead mélangés).
Analyse faite hors Live, en Python (numpy/scipy/soundfile). **Rien n'a été écouté** : tout est mesuré.

| Élément | Valeur | Fiabilité |
|---|---|---|
| Tempo | **120,00 BPM exact** — 1 mesure = 2,000 s | certaine (estimation phase-invariante) |
| Forme | 64 mesures ; frontières de section aux mesures **33/34** et **58** | certaine |
| Solo de la version audio | **mesures 34 à 58** (66–114 s), 24 mesures | certaine |
| Tonalité | **fa mineur** | solide (chroma concordant sur les 2 fichiers) |
| Registre du lead | **F5–C6** (700–1050 Hz) | solide (spectrogramme du stem) |
| Registre des claviers | F3–F4 (175–350 Hz) | solide |
| Timbre du lead | **dent-de-scie** — H2 −6,3 / H3 −10,0 / H4 −12,2 dB (saw théorique : −6,0 / −9,5 / −12,0) | solide (368 tenues stables) |
| Filtre | passe-bas **doux**, commence à agir à partir de H5 (≈ 3,5–5 kHz) ; écarts vs saw : −2,1 à H5, −4,7 à H7, −8,4 à H9 | solide |
| Centroïde spectral | **1213 Hz** | solide |
| Pairs/impairs | **0,64** (> 0,6 = famille saw ; < 0,3 = carré/pulse) | solide |
| Saturation | **aucune** sur le lead — tous les écarts sont négatifs vs saw | solide |
| Stéréo | corrélation L/R **0,00**, side/mid **1,00** dans 200–1200 Hz → unisson large, totalement décorrélé | indicatif (mesuré sur le mix) |
| Bends | **108** sur le solo — médiane **0,81 demi-ton**, 90e pct **1,8**, max **4,1** | solide |
| Durée des bends | médiane **46 ms**, max 110 ms | solide |
| Sens des bends | 51 montants / 57 descendants | solide |
| Vibrato | **7,1 Hz, ±29 cents**, sur 2 tenues longues sur 9 → occasionnel, pas permanent | indicatif |
| Notes exactes du solo | **non établies** | ⚠️ suivi de hauteur non fiable (34 % de frames, erreurs d'octave) — **ne pas utiliser** |

### Erreur commise et corrigée (à ne pas refaire)

Une première analyse, menée sur le **mix complet**, avait conclu : « ré mineur pentatonique, registre
220–350 Hz, saturation présente, pas de vibrato ». **Tout cela est faux.** Le suivi de hauteur
s'était accroché à la **couche d'accords** (175–350 Hz) au lieu du lead (700–1050 Hz), et le profil
harmonique mesuré était donc celui des claviers.

**Leçon** : sur un mix ou un stem polyphonique, vérifier au spectrogramme **dans quel registre vit
réellement l'élément visé** avant de lancer un suivi de hauteur ; et croiser avec un chroma global,
qui ne dépend pas du suivi.

### Autres constats

- Le fichier nommé `Synthesizer_Solo_Electro-Funk_Style.wav` **est le morceau complet lui-même** —
  corrélation d'enveloppe **0,83** avec le stem après alignement de −0,15 s. Le nom vient du prompt
  de génération.
- Le stem synth n'a **aucune énergie sous 150 Hz** (0,1–0,2 % contre 6,3 % + 32,1 % dans le morceau
  complet) : kick et basse sont bien dans les autres stems.
- La coupure nette à 16 kHz du MP3 est l'encodage, pas le mix.

## Plan retenu (9 étapes)

Plan complet validé le 2026-09-22. Ordre : ouvrir la séance → repérer le break → créer piste +
Serum 2 (anti hot-swap) → régler le patch → **vérifier par la mesure** → composer le solo →
poser l'expression → intégrer au break → sauvegarder et journaliser.

### Cibles chiffrées du patch Serum 2

- **OSC** : dent-de-scie, **unisson large** (spread stéréo poussé — c'est ce qui produit la
  décorrélation L/R mesurée).
- **Filtre** : passe-bas doux, intact jusqu'à H4, action à partir de **3,5–5 kHz**. Pente faible
  plutôt que 24 dB raide. Résonance modeste.
- **Pas de saturation** ajoutée : la mesure n'en montre aucune sur le lead.
- **Mono + portamento** de l'ordre de **46 ms** (durée médiane des bends mesurés).
- **Pitch bend range ±2 demi-tons** — 90 % des bends sont sous 1,8 demi-ton ; un range large rendrait
  les petits mouvements imprécis.

### Cibles du solo à composer

- **Fa mineur**, registre **F5–C6** (MIDI 77 à 84).
- Socle : pentatonique de fa mineur (F, Ab, Bb, C, Eb) ; mineur naturel pour les notes de passage.
- Phrasé : **notes majoritairement tenues**, mouvement concentré aux transitions — pas de flot
  continu de croches.
- Bends de **0,8 à 1,8 demi-ton**, ≈ **46 ms**, autant montants que descendants, aux entrées et
  sorties de notes.
- Vibrato **occasionnel** seulement : 7,1 Hz, ±29 cents, sur certaines tenues longues.

### Vérification

Export d'un clip de test → profil harmonique à ±1 dB de la cible jusqu'à H4, décroche à partir de
H5, centroïde ≈ 1200 Hz, corrélation L/R nettement sous 1. Un seul changement par cycle, dans
l'ordre hauteur → timbre → filtre → largeur.

## Journal

- **2026-09-22** — Analyse audio complète de la version existante (session cloud, hors Live).
  Tempo, forme, tonalité, registre, timbre, bends et vibrato chiffrés ; erreur de registre commise
  puis corrigée. Décisions utilisateur : nouveau solo + patch Serum 2. Aucune modification du Set.
