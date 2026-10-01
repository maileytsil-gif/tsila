# Architecture fonctionnelle d'un cuivre

Un cuivre, émulé ou électronique, se pense en **sept fonctions indépendantes**. Une même couche peut en remplir plusieurs ; chaque couche ajoutée doit justifier la sienne. L'ordre ci-dessous est l'ordre de construction.

## Deux familles, deux règles

| | Émulation (trompette, section réaliste) | Cuivre électronique (synth brass, braam, future bass, stab) |
|---|---|---|
| Source | un oscillateur dent de scie, ou multisample / spectral | plusieurs oscillateurs, unisson, désaccord, tables, FM |
| Ce qui fait « cuivre » | brillance qui suit la force, transitoire à deux vitesses, growl bref, vibrato retardé | mêmes marqueurs, exagérés : l'enveloppe de filtre plus lente que l'ampli reste le signe distinctif |
| Interdits | désaccord entre oscillateurs, vibrato dès l'attaque, accord de six notes | rien, sauf perdre la lisibilité du hook |
| Réalisme | vient du MIDI (articulations, respirations, vélocité) autant que du patch | vient du mouvement (LFO, macro) et du traitement |

## 1. CORPS
Objectif : la note, la série harmonique, le registre.

- Émulation : une dent de scie [DOC], niveau modéré, octave selon l'instrument ; tuba/trombone : + carré une octave dessous [DOC]. Ou un multisample de l'instrument (Serum 2 Multisample, Sampler, Kontakt) [DOC].
- Synth brass : 2 à 3 dents de scie, désaccord 5-15 cents [HEUR], parfois pulse en PWM lente ; le sub n'existe pas sauf braam.
- Registre : jouer dans la tessiture réelle de l'instrument imité (`genre-brass-specifications.md`) ; un synth brass de section vit surtout entre C2 et C5 (C3 = 60) [HEUR].

## 2. ATTAQUE
Objectif : le coup de langue, l'installation de la note.

- Ampli : attaque courte (≈ 10-100 ms selon la force), sustain élevé, release court non nul [DOC].
- Growl d'installation : triangle 80 Hz ou bruit → cutoff, fondu en 50-150 ms [DOC/HEUR]. Dans Serum 2 : LFO en mode Env, forme triangle, vitesse en Hz ; dans Operator : LFO en plage Hi vers FIL, quantité par l'enveloppe du LFO [DOC].
- Scoop de hauteur : facultatif et léger (−20 à −50 cents sur 30-60 ms) [HEUR] ; jamais de modulation périodique de la hauteur pendant l'attaque [DOC].
- Stab / hit : attaque 0-5 ms, decay court, l'attaque est portée par le filtre qui se referme [HEUR].

## 3. BRILLANCE
Objectif : le spectre qui s'ouvre avec la force et avec le temps — **la** signature.

- Enveloppe de filtre **plus lente que l'ampli** (attaque 300-600 ms sur une tenue, 30-80 ms sur un stab) avec **decay** vers un sustain plus bas (le « parp ») [DOC pour la forme, valeurs stab HEUR].
- Vélocité → quantité d'enveloppe de filtre ; molette ou aftertouch → cutoff en tenue [DOC].
- Résonance légère, qui peut monter avec la force [DOC]. Suivi de clavier ≈ 95 % [DOC].
- FM : l'équivalent est l'index de modulation (Operator : niveau du modulateur ou `FM Drive` ; Serum 2 : quantité de warp FM) piloté par la même enveloppe et la vélocité [DOC].

## 4. SOUFFLE
Objectif : réalisme et « air » d'une émulation ; texture d'un cuivre électronique.

- Bruit **façonné** (passe-bande vers 1-3 kHz ou filtre à formants), niveau presque inaudible, suit l'enveloppe d'ampli [DOC pour le principe, plage HEUR].
- Sur un multisample, le souffle est déjà dans l'échantillon : ne pas en rajouter.

## 5. EXPRESSION
Objectif : ce qui bouge pendant la note et entre les notes.

- Vibrato retardé 5 Hz, faible, rampe 300-600 ms [DOC/HEUR] ; ou vibrato joué (molette, pitch bend).
- Gonflement / diminuendo par CC11 ou macro ; falls, doits, shakes, scoops par enveloppe de hauteur ou pitch bend (plage 2 demi-tons pour le réalisme, 12 pour un braam) [HEUR].
- Legato sans retrigger pour les notes liées ; retrigger pour les notes détachées [DOC].
- Cuivre électronique : tremolo rythmique (future bass), LFO de cutoff synchronisé, macro « ouverture » automatisée vers le drop.

## 6. SECTION
Objectif : passer d'un soliste à un pupitre.

- Réalisme : **plusieurs instruments, pas un unisson** — deux à quatre pistes ou voix avec désaccord ≤ 8 cents, décalages de 5-25 ms, vélocités différentes, panoramiques distincts [HEUR]. Les libraries « section » le font en interne (Session Horns : voix réparties automatiquement) [DOC si installée].
- Synth brass : unisson 2-4 voix, détune modéré, chorus ou Spread ; largeur au-dessus de 200 Hz seulement ; vérifier en mono [HEUR].
- Voicing : voir `horn-section-writing.md` ; un stab de section réaliste a 3-4 notes, pas 6.

## 7. ESPACE
Objectif : distance, pièce, réponse.

- Reverb courte (pièce/plate 0,8-1,6 s) pour une section pop, hall pour un cuivre cinématique, pré-delay 10-30 ms pour garder l'attaque [HEUR].
- La distance se rend par un passe-bas doux et moins de transitoire, pas seulement par plus de reverb [HEUR].
- Delay throw en fin de phrase (1/4 ou 1/8 pointé) sur un stab, jamais sur toute la ligne [HEUR].
- Retour spatial coupé sous 150-200 Hz [HEUR].

## Rôle et propriété du médium

Avant de régler quoi que ce soit, nommer le rôle et qui possède le médium (1-4 kHz, la zone de la voix) :

| Rôle | Description | Modèle de propriété |
|---|---|---|
| LEAD | mélodie principale, souvent solo | BRASS OWNS HOOK |
| HOOK | riff de section répété, identité du morceau | BRASS OWNS HOOK |
| STAB | accents courts sur des temps précis | BRASS ACCENTS (la voix ou le lead possède le médium) |
| LINE | contre-chant, réponse à la voix | VOICE OWNS HOOK, BRASS ANSWERS |
| PAD | tenues de section en arrière-plan | BRASS IN BACKGROUND |
| HIT | impact isolé (braam, hit orchestral, transition) | BRASS ACCENTS |

Le modèle décide du registre, du niveau, de la largeur et du moment où le cuivre joue : deux éléments ne possèdent pas le médium en même temps [HEUR]. Sur les morceaux à voix, la ligne de cuivres répond dans les trous ou double la voix à l'octave, elle ne joue pas sous les mots.

## Ordre de construction

1. Rôle, propriété du médium, registre, durée des notes, BPM.
2. Famille : émulation ou cuivre électronique ; moteur (`serum2-brass-design.md`, `ableton-brass-design.md`, `sampled-brass-midi-programming.md`).
3. CORPS + enveloppe d'ampli.
4. BRILLANCE : enveloppe de filtre plus lente, vélocité, molette.
5. ATTAQUE : growl, scoop, ou stab.
6. Jouer le clip réel : registre complet, vélocités basses et hautes, legato. Corriger le MIDI avant le son.
7. SOUFFLE, EXPRESSION.
8. SECTION : seulement si le rôle l'exige ; mono vérifié.
9. ESPACE et traitement, chaque plug-in avec son problème écrit (`plugin-role-matrix.md`).
10. Macros (`macro-bridge-schema.md`), validation (`validation-protocol.md`), réponse au format (`output-schema.md`).
