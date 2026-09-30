# Traitement spectral dans Ableton Live 12 Suite

Sources : [manuel des effets Live 12, Spectral Resonator et Spectral Time](https://www.ableton.com/en/manual/live-audio-effect-reference/), [explication FFT par Ableton](https://www.ableton.com/en/blog/spectral-sound-a-look-at-live-11s-new-spectral-devices/), [guide Spectral Time](https://www.ableton.com/fr/blog/freeze-delay-and-deconstruct-sound-design-with-spectral-time/). Vérifié le 28 septembre 2026.

**Dans ce workflow** : Spectral Resonator et Spectral Time sont des effets natifs ; la règle 6 d'`ableton-live-session` les exclut des chaînes de mix. Les employer seulement sur une piste de sound design dédiée, imprimer le résultat (`resampling`) puis retirer le device ; jamais sur un retour ni dans une chaîne de mix. Les écoutes demandées ci-dessous reviennent à l'utilisateur.

## Clarifier le vocabulaire

Il n'existe pas un unique « mode spectral » commun à Wavetable et aux effets de Live. **Wavetable** est un instrument qui parcourt des formes d'onde; ses effets d'oscillateur sont FM, Classic et Modern selon le manuel. **Spectral Resonator** et **Spectral Time** sont des effets audio qui décomposent le signal par FFT, modifient ses composantes fréquentielles puis le resynthétisent. **Spectrum** ne fait qu'analyser et afficher le signal; il ne le transforme pas.

| Effet | Action principale | Usage Bass House |
|---|---|---|
| Spectral Resonator | Résonances accordées, harmoniques, decay et modulation | Tonaliser un hit, vocal chop, percussion; générer une réponse métallique ou un pad à partir d'une source courte |
| Spectral Time | Gel spectral et retard dont les bandes de fréquences peuvent évoluer différemment | Transition figée, queue d'impact, texture glitch, riser et espace mouvant |
| Spectrum | Mesure des fréquences | Vérifier la hauteur et les zones d'énergie, sans traitement audio |

## Spectral Resonator : procédure

1. Placer l'effet après une source audio courte et riche (clap, voix, bruit, stab), de préférence en parallèle pour préserver l'attaque originale. Essayer une note de tonalité en mode **Internal**; en mode **MIDI**, choisir une piste MIDI dans External Source et jouer les notes ou accords voulus.
2. Régler **Decay** selon la place dans le groove; **Harmonics** détermine la brillance et **HF/LF Damp** atténuent les partiels hauts/bas. **Stretch** change l'espacement des harmoniques : explorer avec prudence si l'effet devient dissonant. **Shift** transpose le spectre de l'entrée, pas celui du résonateur.
3. Tester **None**, **Chorus**, **Wander** et **Granular** dans la section Modulation. Pour un son robotique court, commencer sans modulation ou avec Chorus subtil; pour une texture mouvante, essayer Wander; Granular donne un grain fragmenté.
4. Sur la piste de sound design dédiée, régler Dry/Wet à 100 %, filtrer au besoin la sortie traitée et imprimer une sélection audio. En MIDI Poly, MIDI Gate est toujours actif; garder de courtes notes pour des réponses rythmiques.

## Spectral Time : procédure

1. Choisir **Freezer** pour tenir une tranche de son, ou **Delay** pour répéter des composantes. Le gel peut être manuel, déclenché à la détection de transitoires (**Onsets**) ou à intervalles synchronisés (**Sync**).
2. Sur une voix ou un impact de fin de phrase, activer Freeze juste avant le changement de section; automatiser le volume de retour puis enregistrer la queue. Pour un glitch, utiliser Retrigger Sync et raccourcir l'intervalle.
3. Dans Delay, **Tilt** retarde différemment graves et aigus, **Spray** disperse les temps de manière aléatoire, **Mask** limite Tilt/Spray à une région grave ou aiguë, **Shift** déplace la fréquence des répétitions. Garder la basse principale hors de la sortie traitée si elle trouble le kick.
4. **Resolution** élevé améliore la précision mais augmente la latence; réduire en jeu/monitoring si nécessaire. L'ordre Freezer → Delay ou Delay → Freezer se choisit selon l'effet désiré. Dry/Wet global à 100 %, puis imprimer et retirer le device.

## Vérifications

- Écouter en solo puis dans le drop à niveau égal. Les effets FFT peuvent étirer les attaques et produire des queues qui recouvrent la mesure suivante.
- Imprimer en audio et aligner les transitoires si le résultat doit rester très serré; regarder la latence de l'appareil dans Live au besoin.
- Vérifier hauteur, mono et conflit avec sub/kick; garder l'effet comme couche de caractère lorsque la fondamentale du son principal doit rester stable.
