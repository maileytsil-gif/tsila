# projet — funk is not dead

> Fichier créé depuis la session cloud (analyse audio hors Live), mis à jour le 2026-09-22.
> **À recopier ou fusionner dans la mémoire projet locale**
> (`~/.claude/projects/-Volumes-NO-NAME-caude/memory/`) au début de la prochaine séance locale.

## REPRISE

**État.** Aucune modification n'a été faite dans Ableton. Tout ce qui suit est de la préparation :
analyse de timbre d'une référence, et une proposition de petit solo écrite mais **pas encore posée
dans le Set**.

**Le morceau.** Funk jazz, **120,00 BPM exact**, **fa mineur dorien** (F G Ab Bb C **D** Eb — la
sixte majeure D est la couleur caractéristique). Durée 2:09, 64 mesures.

**La cible.** Un **petit solo de synthé**, pas un break : **mesure 30 temps 3 → mesure 33**
(levée de deux temps puis deux mesures pleines). ⚠️ *Interprétation de « de 30,3 à 33 » à confirmer
avec l'utilisateur à la reprise.*

**Décisions prises par l'utilisateur (2026-09-22).**
- Le son : **patch reconstruit dans Serum 2** (pas le stem audio tel quel).
- Le solo : **une nouvelle ligne**, pas une transcription.
- **La référence audio sert UNIQUEMENT au sound design, pas au matériel musical.**

**En attente.**
- Confirmation de l'emplacement exact (« 30,3 »).
- Validation (ou réécriture) de la proposition de solo ci-dessous.
- Le mécanisme d'écriture des bends : enveloppe de clip MIDI / glide du synthé / automation —
  à trancher d'après ce que les outils locaux savent réellement faire. *Deux explorations avaient
  été lancées là-dessus côté cloud sans rendre de réponse.*

**Prochaine étape à la reprise.** Ping du bridge, **Sauver Set Live sous…** un nouveau nom, puis
relire l'état réel du Set (repères, pistes, clips) avant quoi que ce soit — ne rien supposer de la
structure à partir de l'audio.

---

## Référence de sound design

⚠️ **Cadrage donné par l'utilisateur : cette référence sert au SON, pas à la musique.** Toute
analyse mélodique qui en a été tirée est hors sujet et ne doit pas servir à écrire des notes.

Fichier : `Synthesizer_Solo_Electro-Funk_Style.wav`. Analyse faite hors Live en Python
(numpy/scipy/soundfile), sur un stem synth extrait par Ableton (`funk_is_not_dead.wav`, qui contient
claviers d'accompagnement **et** lead mélangés — séparables par registre, deux octaves d'écart).
**Rien n'a été écouté : tout est mesuré.**

### Timbre du lead — ce qui sert vraiment

| Élément | Valeur | Fiabilité |
|---|---|---|
| Forme d'onde | **dent-de-scie** — H2 −6,3 / H3 −10,0 / H4 −12,2 dB (saw théorique : −6,0 / −9,5 / −12,0) | solide (368 tenues stables) |
| Pairs/impairs | **0,64** (> 0,6 = famille saw ; < 0,3 = carré/pulse) | solide |
| Filtre | passe-bas **doux**, intact jusqu'à H4, commence à agir à partir de H5 (≈ **3,5–5 kHz**) ; écarts vs saw : −2,1 à H5, −4,7 à H7, −8,4 à H9 | solide |
| Centroïde spectral | **1213 Hz** | solide |
| Saturation | **aucune** — tous les écarts sont négatifs vs saw | solide |
| Stéréo | corrélation L/R **0,00**, side/mid **1,00** dans 200–1200 Hz → **unisson large, totalement décorrélé** | indicatif (mesuré sur un mix) |
| Bends | médiane **0,81 demi-ton**, 90e pct **1,8**, max 4,1 ; durée **médiane 46 ms** ; 51 montants / 57 descendants | solide |
| Vibrato | **7,1 Hz, ±29 cents**, occasionnel (2 tenues longues sur 9), pas permanent | indicatif |

### Cibles chiffrées du patch Serum 2

- **OSC** : dent-de-scie, **unisson large** (spread stéréo poussé — c'est ce qui produit la
  décorrélation L/R mesurée).
- **Filtre** : passe-bas doux, intact jusqu'à H4, action à partir de **3,5–5 kHz**. Pente faible
  plutôt que 24 dB raide. Résonance modeste.
- **Pas de saturation** ajoutée : la mesure n'en montre aucune.
- **Mono + portamento** de l'ordre de **46 ms**.
- **Pitch bend range ±2 demi-tons** — 90 % des bends mesurés sont sous 1,8 demi-ton ; un range large
  rendrait les petits mouvements imprécis.

### Vérification du patch

Clip de test hors morceau → export de la plage → profil harmonique à ±1 dB de la cible jusqu'à H4,
décroche à partir de H5, centroïde ≈ 1200 Hz au registre visé, corrélation L/R nettement sous 1.
**Un seul changement par cycle**, dans l'ordre hauteur → timbre → filtre → largeur.

## Proposition de petit solo (écrite le 2026-09-22, NON posée dans le Set)

Fa dorien, funk jazz. Notes en **numéro MIDI** (autorité ; en affichage Ableton C3=60 ça se lit
Bb3 à Ab4). Registre MIDI 70→80, bien au-dessus des claviers d'accompagnement (F3–F4).

**Levée — mesure 30**

| Position | MIDI | Note | Durée |
|---|---|---|---|
| 30 t. 3,5 | 70 | Bb | double |
| 30 t. 3,75 | 72 | C | double |
| 30 t. 4 | 75 | Eb | croche |
| 30 t. 4,5 | 77 | F | croche, **scoop +1 d-t à l'attaque** |

**Mesure 31 — l'énoncé**

| Position | MIDI | Note | Durée |
|---|---|---|---|
| 31 t. 1 | 80 | Ab | noire tenue, **bend +1 d-t en entrée**, chute en sortie |
| 31 t. 2,5 | 79 | G | croche |
| 31 t. 3 | 77 | F | croche |
| 31 t. 3,5 | 74 | **D** | croche ← couleur dorienne |
| 31 t. 4 | — | silence | l'espace est essentiel en funk |
| 31 t. 4,5 | 72 | C | croche |

**Mesure 32 — la réponse, montée chromatique**

| Position | MIDI | Note | Durée |
|---|---|---|---|
| 32 t. 1 | 70 | Bb | croche |
| 32 t. 2 | 72 | C | double |
| 32 t. 2,25 | 73 | Db | double, approche chromatique |
| 32 t. 2,5 | 74 | **D** | croche ← dorien |
| 32 t. 3 | 75 | Eb | double |
| 32 t. 3,25 | 77 | F | double |
| 32 t. 3,5 | 79 | G | croche |
| 32 t. 4 | 80 | Ab | noire, **vibrato 7 Hz ±30 cents** |

**Mesure 33 — résolution**

| Position | MIDI | Note | Durée |
|---|---|---|---|
| 33 t. 1 | 77 | F | tenue, **bend +1 d-t en entrée** |

Trois bends seulement, tous d'un demi-ton, plus un vibrato sur la tenue de la mesure 32 — conforme
aux amplitudes mesurées, et le phrasé garde de l'air.

## Pièges rencontrés (à ne pas refaire)

- **Registre avant suivi de hauteur.** Une première analyse menée sur le mix complet a conclu à tort
  « ré mineur, registre 220–350 Hz, saturation présente, pas de vibrato ». Le suivi s'était accroché
  à la **couche d'accords** au lieu du lead. Toujours vérifier au spectrogramme **dans quel registre
  vit réellement l'élément visé** avant de lancer un suivi, et croiser avec un chroma global.
- **Suivi de hauteur sur polyphonie = peu fiable.** Même corrigé, le suivi ne retenait que 34 % des
  frames et produisait des grappes chromatiques. Les **amplitudes de bend** restent valables (elles
  ne dépendent pas de l'octave), les **notes exactes non**.
- **Test d'accordage sur une couche d'accords = sans objet.** La distribution des écarts était plate :
  l'autocorrélation sur du polyphonique ne donne pas une hauteur sur la grille tempérée.
- **Demucs inutilisable en session cloud** : les poids sont sur `huggingface.co` et
  `dl.fbaipublicfiles.com`, bloqués par la politique réseau (403). Séparation faite à la place en
  traitement du signal (HPSS par filtrage médian + masque harmonique).

## Journal

- **2026-09-22** — Analyse de timbre de la référence synthé (session cloud, hors Live). Tempo, forme
  et profil harmonique chiffrés ; erreur de registre commise puis corrigée. Cadrage rectifié par
  l'utilisateur : référence = sound design seulement, morceau en **fa mineur dorien**, style **funk
  jazz**, cible = **petit solo mesures 30 t.3 → 33** (et non un break de 24 mesures). Proposition de
  solo écrite, non posée. **Aucune modification du Set.**
