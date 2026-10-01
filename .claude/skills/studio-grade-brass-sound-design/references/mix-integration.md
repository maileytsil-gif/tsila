# Intégration au mix

Place, EQ, dynamique, espace et bus d'une section ou d'un cuivre électronique. Valeurs de départ [HEUR] (wikis et fiches de production lues, extraits SOS/tailout non lus) ; chaîne éprouvée du projet dans `../../effets-plugins/references/chaine-actuelle.md` ; procédure complète `../../mixage/SKILL.md`, diagnostic `../../ingenieur-mixage/SKILL.md`.

## Place face à la voix et au lead
La zone 1–4 kHz appartient à la voix : un cuivre non contenu à 2–4 kHz enterre les paroles [HEUR-extrait]. Trois réponses, dans l'ordre : écrire les cuivres dans les trous de la voix (arrangement), les mettre une octave au-dessus ou au-dessous, puis seulement une EQ dynamique qui creuse 2–4 kHz quand la voix est présente (Pro-Q 4 spectral avec sidechain, ou soothe3 en sidechain) [HEUR]. Nommer le modèle de propriété du médium (`brass-architecture.md`) avant tout réglage.

## EQ
| Zone | Action | Source |
|---|---|---|
| Coupe-bas | 60–80 Hz (sauf tuba/low brass) ; section funk 150 Hz ; trompette jazz 150–200, sax 100–150 | [HEUR] |
| Corps 80–300 Hz | couper si conflit avec la basse ; orchestral +1 dB à 300 Hz | [HEUR] |
| Boue/honk 250–500 Hz | −2 dB Q 1,2 à 400 Hz sur une section ; couper 250–400 Hz quand la section s'empile | [HEUR] |
| Mordant 1,5–3 kHz | +2 dB Q 1,1 à 2,5 kHz (funk) ; +1,5 dB à 3 kHz (orchestral) | [HEUR] |
| Dureté 2–5 kHz | −2 dB large si strident ; dynamique/spectrale plutôt que statique | [HEUR] |
| Brillance 4–8 kHz, air 8–12 kHz | shelf +1 dB à 8 kHz ; sax air 8–12 kHz | [HEUR] |
| Formants fixes | trompette ≈ 1 050 Hz, cor ≈ 740, trombone ≈ 240/700, tuba ≈ 230 : à renforcer légèrement sur un synth brass qui « ne sonne pas cuivre », jamais sur un vrai cuivre | [DOC Maresz pour les fréquences, geste HEUR] |

## Dynamique
- Section funk (bus) : 2,5:1, seuil −14 dB, attaque 10 ms, release 100 ms, knee 4 dB, +1,5 dB de makeup [HEUR] ; API-2500 ou bx_glue (`plugin-role-matrix.md`).
- Jazz : 2–3:1, attaque lente 30–50 ms (transitoires), release 200–300 ms, 1–3 dB de réduction au maximum [HEUR].
- Stabs : attaque 15–25 ms pour garder le « blat » ; parallèle 20–30 % d'un signal très compressé [HEUR-extrait].
- Saturation à la place d'une compression : un léger drive sur le bus donne le mordant d'un vrai fortissimo qu'un sample n'a pas ; un limiteur sur un morceau orchestral a fait passer le facteur de crête de 21,8 à 16 dB [HEUR].
- Une section de quatre voix qui attaquent ensemble écrête facilement : vérifier les crêtes des stabs (`../../live-export-wav/SKILL.md`, `analyze_wav.py`).

## Espace et panoramique
- Une seule reverb pour toute la section (« les musiciens jouent ensemble ») : hall/chamber 1,5–3 s, pré-delay 20–40 ms (jazz/acoustique) ; plate 0,8–1,6 s pour une section pop ; delay rare, slapback court [HEUR].
- Pans de section : jazz trompette −0,18, trombone +0,34, ténor +0,16, rien en dur ; orchestre cor −0,26, trompette +0,20, trombone/tuba +0,36 [HEUR]. Sur un stab mono échantillonné : Imager Stereoize II léger, corrélation > 0 [DOC Imager mono-compatible].
- Réduire la largeur d'une reverb de master sinon la corrélation devient négative et le test mono échoue [HEUR].

## Bus de cuivres
Enregistrer ou jouer chaque pupitre séparément, puis lier la section sur un bus par EQ + compresseur [HEUR] : `bx_glue parallèle 60 % → REQ 6 (sweeps automatisés, coupe-bas 150 Hz) → J37 815 léger`. Les cuivres électroniques (future bass, braam) passent par le bus HARMONIE ou un bus dédié avec OTT/sidechain avant la reverb.

## Sonie et contrôle
Cibles jazz −16 à −20 LUFS, moderne −14 à −16 [HEUR] ; mesurer avec Insight 2 après export (`../../live-export-wav/SKILL.md`), spectre SPAN sur le drop. Ne jamais déclarer une section « prête » sans le test mono et le test voix + cuivres (`validation-protocol.md`).
