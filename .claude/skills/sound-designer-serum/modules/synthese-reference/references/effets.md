# Chaîne d'effets : reproduire la texture et l'espace

D'abord rapprocher le patch sec, puis reconstruire les effets. Si le son de référence est uniquement disponible traité, conserver l'incertitude sur le partage synthé/effets. Un chorus peut ressembler à l'unisson, et une reverb courte peut modifier l'attaque.

## Choix des étages

| Besoin observé | Effet à envisager | Vérifier |
|---|---|---|
| Déséquilibre stable | EQ, par exemple Pro-Q, F6/REQ/Q10 Waves si disponibles | Zone, largeur, gain, phase et niveau compensé |
| Harmoniques ou densité supplémentaires | Drive/saturation interne, J37 ou autre effet approprié | Gain d'entrée, sortie, modulation/bruit éventuels, perte de grave |
| Battements, épaisseur et mouvement | Unisson d'abord, puis chorus/flanger/doublage si nécessaire | Vitesse, profondeur, feedback, dosage, mono |
| Répétitions | Delay adapté, interne ou plug-in disponible | Temps, synchro, feedback, filtre, panoramique, dosage |
| Espace et queue diffuse | Reverb adaptée, interne ou plug-in disponible | Pré-delay, durée, diffusion, filtrage et dosage |
| Pulsation de niveau | LFO/automation ou sidechain selon le contexte | Déclencheur, rythme, profondeur, récupération |
| Contrôle de dynamique | Compresseur adapté | Attaque, release, gain compensé, transitoire |

Les marques citées sont des options, pas une confirmation de disponibilité de chaque effet. Pour Waves, vérifier le composant dans le navigateur ; les bundles repérés dans le contexte ne prouvent pas licence ni fonctionnement. Si mastering-outils est présent, sa fiche Waves peut guider l'accès et les différences entre composants, sans appliquer une chaîne de mastering au son par défaut.

## Réglages et ordre
Noter le trajet exact : effets internes au synthé, inserts externes, retours et routage de sidechain. L'ordre change le résultat : saturation avant filtre, après filtre ou après reverb produit des comportements différents. Choisir l'ordre qui explique la référence et comparer les variantes utiles.

Pour les effets synchronisés, convertir seulement si le tempo est connu. Une noire dure `60000 / BPM` millisecondes ; la croche vaut la moitié, une valeur pointée multiplie par 1,5 et un triolet par 2/3. Si le délai semble libre, ajuster en millisecondes plutôt que le forcer sur la grille.

Un effet sur retour est généralement réglé pour ne pas dupliquer inutilement le signal sec ; inspecter le routage et le dosage avant d'appliquer cette convention. Sur insert, choisir le mix sec/traité souhaité. Ne pas compenser un excès de reverb avec un raccourcissement artificiel de toutes les notes.

La pulsation d'un morceau peut venir d'un compresseur déclenché par le kick, d'une automation, d'un LFO ou simplement de notes espacées. Pour un patch réutilisable, documenter les dépendances au tempo et à la piste de sidechain. Ne pas inventer une source de kick absente du projet.

## Préférences de cet utilisateur
Les synthés natifs Ableton sont explicitement possibles. Pour les effets de piste, conserver sa préférence pour les effets tiers, Waves compris, sauf nouvelle demande de chaîne entièrement native. Décrire clairement quels effets résident dans Serum et lesquels doivent être rappelés dans Live. Adapter aux outils disponibles, sans imposer d'achat.

## Sauvegarder la chaîne
Inclure les états de bypass, ordre, gains, dosages et automations nécessaires. Avec un rack, choisir quelques macros qui servent réellement le son (par exemple brillance, mouvement, espace) et vérifier leurs plages sans surcharger la sortie. Préserver les réglages d'origine avant toute modification.
