# Chill out, électro chill et jazz chill

## Composition et phrasé

Construire une cellule de 2 à 4 mesures avec un silence reconnaissable, une note cible et une réponse. Dans le chill out, laisser respirer la fin de phrase; dans l'électro chill, faire dialoguer pluck et fragment vocal; dans le jazz chill, faire entendre 3e, 7e, 9e ou 13e par des conduites de voix souples. Garder le thème chantable sans production. Exemple en Dm9–G13–Cmaj9–A7(b9,#9), 4/4, grille de doubles croches, **numérotation Ableton C3 = 60** : Rhodes D3 au 1, F3 au 2&, E3 au 3&, silence au 4 (m1, Dm9) ; réponse E3 au 1&, D3 au 2&, C3 au 4 (m3, Cmaj9). Adapter les notes à chaque accord et tester la résolution de A7(b9,#9) vers Dm9. C'est un exercice original, pas une transcription ; tempo et durées du bloc ci-dessous sont des propositions d'essai (depuis le dossier du skill, `scripts/grille.py --fichier references/chill-electro-jazz.md` donne le tableau et la notation Producer Pal).

```grille
titre: Jazz chill — cellule et réponse du Rhodes
tempo: 90
accords: Dm9 | G13 | Cmaj9 | A7b9#9
rhodes: D3[1:3] F3[2&:3] E3[3&:2] | | E3[1&:2] D3[2&:4] C3[4:4] |
```

Basse: fondamentales et approches discrètes, départ parfois après le kick. Batterie: vélocités variables, ghost notes et microtiming contrôlé; le swing doit servir le motif. Rhodes/guitare: voicings courts avec respirations. Pad: mouvement lent, sans masquer la tierce du thème. Pluck/lead: 3 à 6 attaques distinctes, réponse en registre différent. Ambiance: texture contextualisée, pas de bruit continu sans fonction.

## Cinq points de départ Serum 2 par famille

Les valeurs sont des plages d'essai, dépendantes de la version et du niveau du projet. Affecter quatre macros: M1 couleur (filtre ou morph), M2 mouvement (profondeur/vitesse de modulation), M3 espace (mix des effets, bas exclu), M4 intensité (drive/transitoire/niveau compensé). Chaque ligne donne cinq variantes; développer ensuite la sélection avec oscillateurs, enveloppes, routage, valeurs exactes et automation mesurée. Ne jamais déclarer « label ready » sans écoute dans le morceau et comparaison de référence.

| Famille | Variantes 1 à 5 | Contrôle décisif |
| --- | --- | --- |
| Kick | sinus doux 90–50 Hz; attaque feutrée; kick acoustique filtré; hybride sine/click; kick court saturé | décroissance liée au tempo, accord avec basse, mono |
| Basse/sub | sine ronde; triangle pluck; FM douce; basse électrique synthétique; Reese filtrée lente | niveau stable entre notes, mono sous 120 Hz |
| Percussions | rim boisé; shaker bruit filtré; hat soufflé; tom tonal; microclic granulaire | vélocité, place dans le groove, pas d'aigu agressif |
| Rhodes/keys | sine+harmoniques; tine FM; EP chorus léger; clav étouffé; orgue doux | voicing et transitoires lisibles |
| Plucks/leads | triangle perlé; wavetable filtrée; FM verre; guitare synthétique; lead vocalisé doux | silhouette mélodique et absence de conflit vocal |
| Pads/drones | saw filtrée; sine additive; wavetable animée; texture granulaire; drone de quinte | largeur hors grave, automation lente, silence utile |
| Riser/impact | bruit montant; note rééchantillonnée inversée; souffle granulé; pitch tonal discret; impact sub atténué | passage de section sans pic ni grave prolongé |
| Ambiance/sample | bruit de pièce; field recording découpé; tape hiss filtré; vocal sans mots rééchantillonné; cluster tonal | provenance, licence, intention, niveau |

## Arrangement et effets

Intro 8–16 mesures: cellule partielle et texture. Partie A 16: thème + basse. Variation 8–16: réponse ou inversion du timbre. Pont/break 8: retirer le kick, isoler le motif, envoyer une queue de delay/réverbération depuis un bus; balayer le filtre à résonance modérée, vérifier les pics. Retour 16: reprendre la cellule identifiable, ajouter une contreligne seulement si elle n'en cache pas le rythme. Sortie: retirer progressivement, sans multiplier les risers.

Un chorus sur le groupe keys, un flanger subtil sur une transition de percussion et un effet de découpe sur une seule réponse peuvent suffire. Automatiser les sends et le retour à zéro au changement de section. Pour vocoder: porteuse harmonique au registre mid, modulateur vocal/percussif, sub séparé propre, puis vérifier l'intelligibilité, les droits de la source et le mono. Voir effets-groupes-vocoder.md et sampling-arrangement.md.

## Validation

Comparer à niveau perçu égal avec deux références choisies pour le sous-style, sans prétendre copier leur patch. Tester thème sans effets, puis avec basse/batterie, casque/moniteurs/mono et faible volume. Noter les différences de densité, transitoires, largeur et longueur de queue. Préserver un export MIDI, la recette, les macros et les sources exactes des samples. Une recette demeure provisoire jusqu'à écoute réelle et ajustement.
