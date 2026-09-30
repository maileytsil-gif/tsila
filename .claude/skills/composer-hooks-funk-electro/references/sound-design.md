# Sound design lié au phrasé

Utiliser des réglages comme points de départ à écouter dans un mix, pas comme presets universels. Sauver preset et MIDI séparément. Pour le détail, dans ce workflow : `../../serum-2-basses-house-future-house/SKILL.md` (dix familles de basses Bass House / Future House, fiches jouables, motifs, sub / mid, BPM), `../../sound-designer-serum/references/basses.md` (sub, Reese, growl, 808, division du grave), `../../sound-designer-serum/references/patches-genres.md` (patchs chiffrés bass house / future house, conversions de tempo), `../../produire-morceau-electronique-de-a-a-z/references/bass-house-recettes.md`, `../../bass-house-sound-design/SKILL.md` (stabs, pads, leads Bass House, Wavetable, spectral), `../../kick-bass-equilibre/SKILL.md` (qui tient le sub, phase, mesure) et `../../construire-low-end-electronique/SKILL.md` (grave qui manque de poids, fluctue ou ne traduit pas en club). L'exécution dans Serum 2 passe par `../../vst-sound-design/SKILL.md`.

## Cinq gestes Serum 2

| Rôle | Construction | Phra­sé et contrôle |
|---|---|---|
| Sub | OSC sub sinusoïdal, -1 octave si nécessaire, chemin Direct, mono; attaque 2–8 ms et release 50–100 ms comme départ | Jouer les fondamentales utiles; surveiller phase, notes basses et relation au kick. |
| Mid growl | OSC A table riche; OSC B modulateur harmonique 2:1, sortie B coupée, FM A depuis B modérée; enveloppe LFO sur FM et bandpass/notch | Accent de modulation sur note de réponse, resampling par phrases de deux mesures; sub indépendant. |
| Metallic | FM à rapport non entier ~1,4–1,7 comme essai, quantité modérée; bandpass résonant et decay court | Placer une note métallique en ponctuation plutôt qu'à chaque attaque; surveiller dureté et hauteur perçue. |
| Reese | Deux saw légèrement détunées, filtre passe-bas, modulation lente; largeur uniquement sur mid | Notes plus longues et réponses aux stabs; vérifier mono. |
| Legato | Activer mono/legato, chevaucher notes MIDI pour glide sans redéclenchement selon réglage; comparer retrigger | Utiliser glide 40–120 ms comme essai expressif; contrôler précisément les chevauchements et les fins de note. |

Routage Direct et mono/legato sont documentés dans le manuel Serum 2. Les nombres ci-dessus sont des hypothèses de patch, non des valeurs extraites d'un tutoriel.

## Tempo et perception

Durée d'une noire en ms = `60000 / BPM`; croche = moitié; double croche = quart. À 120 BPM: 500/250/125 ms; 126: 476/238/119; 174: 345/172/86. Synchroniser une modulation périodique si elle doit dessiner le groove; garder pitch glide, attaque et release en temps absolu quand leur geste expressif doit rester similaire. À BPM plus élevé, raccourcir d'abord les tails qui chevauchent la note suivante, puis juger A/B au niveau égal. Ne pas multiplier automatiquement tous les temps par un coefficient.

Pour une version Afro house, conserver la cellule de thème et laisser les percussions répondre; ne pas plaquer une modulation de filtre sur chaque subdivision. Pour bass house, transmettre la cellule aux accents du mid bass et garder le sub stable. Pour tech house, tester une variante plus courte avec silence de fin. Pour house, permettre au Rhodes/lead de tenir sa réponse sans masquer la basse.

## Contrôles

Comparer la phrase sur un son neutre et sur patch final; si le patch masque ses hauteurs, réduire FM ou mouvement. Vérifier sub seul, mid seul, somme en mono, puis kick+basse, et enfin mix à niveau égal. Les effets spatiaux vont généralement sur le mid/retour, à adapter à l'arrangement.
