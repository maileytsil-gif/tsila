# Validation des sous-types professionnels — v5

## Test A — identité
Le son doit rester identifiable **sans reverb/delay**. Si l'identité disparaît quand les FX sont coupés, revoir source/enveloppe/filtre avant d'ajouter plus d'espace.

## Test B — articulation
Tester au minimum : note très courte, note de 1/8, note tenue, vélocité faible/forte si pertinente. Pour stabs/plucks/keys, vérifier les notes répétées rapides.

## Test C — registre
Jouer au moins une octave sous et une octave au-dessus du registre prévu. Corriger key tracking, filtres, résonances et couches qui deviennent incohérentes.

## Test D — contexte
Écouter avec kick + basse + hook principal. Pour pad/nappe/drone, mesurer surtout le masquage ; pour impact/riser, mesurer la transition ; pour keys/pluck/stab, mesurer la lisibilité rythmique.

## Test E — mono/stéréo
Passer en mono. Une couche décorative peut perdre de la largeur ; la fondamentale, l'attaque et le groove ne doivent pas disparaître.

## Test F — queues
Arrêter le MIDI/audio brutalement avant un drop. Vérifier les tails de reverb/delay, feedback, release et effets de résonance.

## Test G — CPU
Pour Granular/Spectral/Meld/Racks multi-chaînes : vérifier charge en jouant le nombre maximal de voix attendu. Réduire unison/voix/layers ou resampler si nécessaire.

## Test H — bridge [TEST]
Pour un patch destiné au contrôle IA : découvrir paramètres exposés → snapshot → modification unique → lecture de contrôle → restauration → seulement ensuite mouvement/automation.
