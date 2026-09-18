# Mesurer la relation kick / sub sans oreilles

1. **Exports séparés** : même plage (une boucle du drop, 4–8 mesures), « Piste convertie » = KICK puis SUB (ou BASS), depuis la piste MIDI (avant bus) pour juger la relation brute, puis depuis `AUDIO - X` pour la relation traitée. 24 bits, sans normalisation.
2. **`kick_bass_check.py kick.wav sub.wav [--band 30-120] [--lag 15]`** :
   - niveaux (crête, RMS) et pic spectral de chacun ; part d'énergie sous 60 Hz → qui tient réellement le fondamental ;
   - corrélation de Pearson dans la bande (après filtrage) : > 0,3 renforcement, < −0,3 annulation partielle, ≈ 0 indépendants ;
   - gain de la somme : RMS(kick+sub) comparé à la somme en puissance (attendue si indépendants) → dB gagnés/perdus ;
   - meilleur décalage (± lag ms) et gain si polarité inversée → recommandation « décaler le sub de −7 ms » ou « inverser la polarité du kick » ;
   - ratio crête/RMS du kick seul vs dans la somme → l'attaque est-elle masquée par le sub ?
3. Interpréter : les chiffres dépendent de la note jouée (recontrôler aux changements d'accord) et de la phase de départ des oscillateurs (Serum : retrig/phase fixe, sinon la corrélation varie d'une note à l'autre).
4. Appliquer un seul changement (rôle, polarité, décalage, accord, sidechain), réexporter, remesurer ; noter le résultat dans la signature.
Rappel : `analyze_synth.py --mono-note --fmin 30 --fmax 200` donne la hauteur réelle du kick et du sub pour vérifier l'accord.

Pièges de `kick_bass_check.py` : l'accord se mesure sur la **queue** du kick (le pic spectral de l'attaque descend en pitch) ; le facteur de crête de la somme baisse mécaniquement quand on additionne deux signaux, donc « attaque masquée » est une alerte à relire, pas un verdict ; sans instrument Serum (pistes bouncées), la polarité se corrige par décalage du clip audio ou par Utility (toléré), et l'export « depuis la piste MIDI » devient un export de la piste AUDIO.
