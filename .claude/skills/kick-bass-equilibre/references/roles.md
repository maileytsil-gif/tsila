# Rôles kick / sub / basse — matrice de décision

| critère | le SUB tient le fondamental | le KICK tient le grave |
|---|---|---|
| genres | deep/minimal/tech house, DnB, UK garage | électro 808, trap, techno « rumble », certains house 909 |
| kick | court (decay < 200 ms), corps 60–100 Hz, coupe-bas 25–30 Hz par défaut (40–50 Hz si > 20 % d'énergie du kick sous 60 Hz), transitoire net | long (300–800 ms), accordé, descente de pitch, coupe-bas 25–30 Hz |
| sub / basse | sinus mono à la tonique, tenue, release 60–120 ms, sidechain 4–8 dB | basse au-dessus de 80–100 Hz, ou notes courtes dans les silences du kick |
| sidechain | rapide (0,1–1 ms / 80–120 ms), libère l'attaque | profond et lent, ou pas de sub séparé |
| mono | tout < 120 Hz mono | idem |
| risques | sub et kick à la même note → battements, annulation : accorder le kick à la quinte ou plus haut | basse et kick se masquent : basse HP plus haut, ou jouer en contretemps |
| vérification | corrélation 30–120 Hz proche de 0 ou > 0 aux attaques ; énergie < 60 Hz portée par le sub | énergie < 60 Hz portée par le kick ; basse > 80 Hz |

Accord rapide : tonique F → sub F0 43,7 Hz ; kick accordé F1 87 Hz (octave) ou C1 65 Hz (quinte) ; éviter 43–50 Hz pour le kick si le sub y est. Une note de basse différente du sub (drops à changements d'accord) déplace la question : recontrôler aux mesures de changement.

Signature : une fois le rôle choisi et vérifié, l'inscrire dans `drums-signature/scripts/signature.json` (kick : accord, longueur, coupe-bas ; sub : note, release ; sidechain : valeurs).
