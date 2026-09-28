# Diagnostic et principes du grave

## Mesurer sans confondre les phénomènes

- **Fréquence** : le C1 MIDI 24 vaut ≈32,7 Hz, E1 ≈41,2 Hz, G1 ≈49,0 Hz, C2 ≈65,4 Hz. Les fondamentales du sub dépendent de la ligne jouée : adapter la gamme, la tessiture et les harmoniques. Une basse audible sur téléphone doit porter des harmoniques au-dessus de sa fondamentale.
- **Temps** : à 125 BPM, une noire dure 480 ms, une croche 240 ms, une double croche 120 ms. Comparer ces durées à la queue du kick et au retour du ducking. Ne pas confondre « release du compresseur » et durée totale audible du trou.
- **Niveau** : mesurer le gain de crête et l'énergie perçue de chaque source puis de leur somme. Une hausse de crête peut provenir de l'addition temporelle sans augmentation musicale utile.
- **Phase** : deux signaux corrélés de même fréquence peuvent se renforcer ou s'annuler suivant leur phase. L'inversion de polarité est un test binaire; elle n'est pas un « alignement automatique ». Un déplacement d'échantillons, un filtre ou un crossover modifie aussi la relation en fréquence; vérifier plusieurs coups et plusieurs notes.
- **Mono** : comparer le mix en mono et stéréo; un sub très large et décorrélé risque de varier selon la diffusion. Une largeur au-dessus du sub peut demeurer intéressante : choisir à l'écoute, avec contrôle de corrélation et de la composante Side.
- **Pièce** : les modes propres peuvent créer pics et creux de grave au point d'écoute. Déplacer la tête/position, recouper au casque et aux références avant d'équaliser une supposée « bosse du fichier ».

## Protocole A/B reproductible

1. Définir une boucle de 8 ou 16 mesures au drop et conserver le même niveau de monitoring.
2. Exporter avant/après, égaliser le niveau perçu, noter BPM, tonalité, note de sub, kick, effets actifs et latence si connue.
3. Solo kick, solo basse, somme, mix complet; répéter en mono. Comparer attaque, tenue, stabilité entre notes, audible sur petits systèmes et énergie du sub.
4. Tester la correction dans un deuxième passage différent (break ou seconde note). Garder uniquement la correction qui améliore l'ensemble.

## Erreurs fréquentes

- Monter le sub pour corriger l'absence de 2e/3e harmonique.
- Couper automatiquement chaque piste à 120 Hz ou chaque sub à 30 Hz : la pente et la fréquence doivent servir le son, les fondamentales et le système.
- Croire qu'un analyseur prouve à lui seul une bonne balance : il affiche de l'énergie, pas la qualité de groove.
- Employer un EQ linéaire à fort Q sur l'attaque sans écouter le pre-ring.
- Caler la phase sur un seul kick alors que le sample, la basse ou la note changent.
- Masteriser un low end instable avec limiteur ou multibande au lieu de corriger l'arrangement/mix.
