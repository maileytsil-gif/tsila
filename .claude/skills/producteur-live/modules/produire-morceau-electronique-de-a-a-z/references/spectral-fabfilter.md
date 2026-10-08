# Compétence FabFilter Pro-Q 4 et Pro-C 3

## Pro-Q 4

Manuel https://www.fabfilter.com/downloads/pdf/help/ffproq4-manual.pdf ; dynamique spectrale https://www.fabfilter.com/help/pro-q/using/spectral-dynamics ; dynamique https://www.fabfilter.com/help/pro-q/using/dynamic-eq . EQ statique pour enlever une zone toujours problématique ; EQ dynamique pour ne traiter une bande qu'aux événements ; mode **Spectral** pour agir sur les fréquences dépassant le seuil **dans** la bande plutôt que sur toute la bande. Créer Bell ou Shelf, fixer la plage dynamique et activer l'icône Spectral ; écouter les attaques et comparer au mode dynamique ordinaire. Choisir Mid/Side si le conflit est spatial et vérifier mono. Minimum Phase pour usage général ; Linear Phase seulement après écoute des transitoires et compensation de latence, particulièrement kick/basse ; Natural Phase à comparer selon le cas. L'analyseur et la liste d'instances aident à repérer chevauchements, sans prouver qu'ils sont audibles. Sidechain externe sur bande dynamique si une source prioritaire doit déclencher l'EQ ; vérifier dans version hôte et écouter la clé.

**Cas** : lead Future Rave variable en 3–5 kHz → Bell large à gain neutre/déplacement de gain modéré, plage dynamique descendante en mode Spectral, seuil tel que seule l'agressivité des fortes notes déclenche ; A/B contre soothe3 sur **la même piste**, même niveau. Si un synthé est systématiquement trop dur, EQ statique suffit. Kick et basse dont l'énergie spectrale change selon les notes → bande dynamique externe sur basse, clé kick, sélectionner strictement la zone de recouvrement ; si l'ensemble du corps de la basse doit descendre à chaque kick, Pro-C 3 est plus prévisible.

## Pro-C 3

Manuel https://www.fabfilter.com/downloads/pdf/help/ffproc3-manual.pdf ; styles https://www.fabfilter.com/help/pro-c/using/styleandcharacter ; dynamique https://www.fabfilter.com/help/pro-c/using/dynamicscontrols ; configuration Live https://www.fabfilter.com/help/pro-c/support/externalsidechaining . Compression de **niveau** et d'enveloppe : Threshold, Ratio, Attack, Release, Knee, Range, Lookahead, Mix, Side Chain EQ et audition de clé selon l'interface. Pro-C 3 compte **14 styles** ; Clean neutre, Versatile polyvalent, Smooth pour colle, Punch pour impact, Upward pour remontée des passages faibles ; les styles TTM et colorés sont plus créatifs et changent le résultat, donc ne pas permuter sans réécoute. Vérifier Attack/Release contre la durée de la mesure et les transitoires. **Range** limite le changement de gain maximal ; ne le confondre ni avec Ratio ni avec la plage dynamique de Pro-Q. Mode external sidechain : Live route la piste clé vers l'entrée sidechain du périphérique puis choisir **Ext** dans Pro-C 3 et auditionner le déclencheur. Side Chain EQ modifie la détection ; contrôler si le style choisi (notamment TTM) change l'effet audible des bandes.

**Recettes de départ, heuristiques** : kick → basse, Pro-C 3 sur basse, clé kick, Clean ou Versatile ; attaque brève si le kick doit prendre la place immédiatement, release suffisamment court pour le contretemps mais sans clic ; ajuster Threshold pour réduction audible puis limiter Range et égaliser les niveaux. Pour pompage assumé Future House, prolonger Release jusqu'au rebond musical ; pour Tech House sobre, limiter Range et préserver la pulsation. Bus batterie : Smooth ou Punch, ratio modéré, attaque laissant passer les transitoires, release revenant avant prochain temps ; si cymbales provoquent compression indue, filtrer la détection. Vocaux : Versatile/Smooth, compression en plusieurs passages légers si grande variation, recontrôler consonnes et souffle. Aucun chiffre de GR n'est universel.

## Décision et combinaison

| Problème | Premier essai | Alternative ou complément si nécessaire |
|---|---|---|
| Pic tonal fixe | Pro-Q 4 statique | Corriger source ; Equator pour plusieurs pics mobiles |
| Résonance mouvante dans une seule piste | soothe3 ou Pro-Q 4 Spectral | Equator Captured/Adaptive, A/B à niveau identique |
| Deux pistes se masquent ponctuellement | Resolve | Pro-Q 4 dynamique externe pour bande précise |
| Basse entière doit reculer devant kick | Pro-C 3 externe | Resolve si seules quelques fréquences doivent reculer |
| Crêtes/bus et groove | Pro-C 3 | Modifier arrangement et enveloppes avant compression excessive |
| Déséquilibre tonal général | Pro-Q 4 statique ou AQ | Comparer sections homologues de référence |

Placer d'abord l'EQ correctif avant compression si la résonance déclenche exagérément le compresseur ; essayer après si le compresseur fait ressortir la dureté. Un sidechain spectral et un compresseur sidechain peuvent coexister si chacun résout une gêne distincte, avec mesure cumulée et A/B de chaque maillon. Ne jamais transformer les réglages de réduction propres à chaque produit en nombres équivalents.
