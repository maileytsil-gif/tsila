# Section de cuivres réaliste (échantillonnée)

Quand le morceau veut de vrais cuivres : funk, soul, afrobeat, pop. Le son vient d'une banque ; le réalisme vient du MIDI (`../references/sampled-brass-midi-programming.md`) et de l'écriture (`../references/horn-section-writing.md`).

## Cible
`HOOK, STAB, LINE ou PAD / formation 2 tpt + sax ténor + tbn (ou trio tpt + sax + tbn) / tessitures confort : tpt 52–80, sax ténor 44–75, tbn 40–71 [DOC MuseScore] / VOICE OWNS HOOK, BRASS ANSWERS`

## Moteur, par ordre de préférence
1. **Session Horns Pro** dans Kontakt Player, si possédé [TEST] : un patch « ensemble » avec Smart Voice Split (les notes d'un accord se répartissent automatiquement trompettes en haut, sax/trombone en bas) [DOC-EXTRAIT], articulations par keyswitch dès C−1 (sustain, marcato, staccato, staccatissimo, rips, fp, growl, shake) [DOC-tiers], dynamique par CC11 ou vélocité. Écran seulement, aucune API (`../../native-instruments-control/SKILL.md`).
2. **Ableton Orchestral Brass** (Live Suite) : Racks à macro d'articulations, un instrument par piste [DOC-EXTRAIT] ; **Brass Quartet** (Spitfire) pour trompette/bugle/tenor horn/trombone avec macro Technique (staccatissimo, vibrato, pitch bend, hollow, flutter) [DOC-EXTRAIT]. Paramètres relisibles par l'API.
3. **Serum 2 Multisample** d'usine (`Factory/Winds/Trumpets LE`, `Trombones Tenor LE`, `French Horns`) [DOC corpus] : une instance par pupitre, `TimbreShift` et enveloppe du multisample, vibrato par LFO Rise/Delay, MONO + LEGATO pour une ligne.
4. Sampler avec un multisample perso (zones Key/Velocity, Round Robin) [DOC].

## Construire la section
| Étape | Réglage [HEUR sauf mention] |
|---|---|
| Pistes | une par pupitre : TPT 1, TPT 2, SAX, TBN ; jamais un seul patch « brass » pour tout |
| Voicings | 3–4 notes, harmonisées depuis l'accord ; drop 2 pour la largeur ; unisson/octaves pour les hooks ; rien de plus serré qu'une quinte sous 48 |
| Dynamique | CC1 (couche) écrit en continu, CC11 (phrase) ; vélocité ≥ 100 sur les stabs, 70–88 sur les pads ; repérer les seuils de couches (v95/v96) [TEST] |
| Articulations | staccato 20–30 % du temps ; legato chevauché 10–20 ms ; fall/rip/shake échantillonnés quand ils existent, sinon pitch bend court (±2 st) |
| Timing | section 10–30 ms derrière basse et batterie ; sax 20 ms derrière la section ; humanisation ±10–20 ms, ±8–15 vélocité ; délai de piste négatif pour compenser l'attaque des samples (Spitfire Tightness) [DOC] |
| Section | désaccord ≤ 8 cents entre pupitres, pans distincts (tpt −0,18, tbn +0,34, ténor +0,16), respirations décalées |
| Équilibre | en forte 1 tpt = 1 tbn = 2 cors [DOC Rimsky] ; sax un peu en retrait |

## Processing (piste puis bus)
Piste : `REQ 6 (HP 100–150 Hz ; −2 dB Q 1,5 à 400–500 Hz si honk) → Pro-Q 4 cloche dynamique −3 dB 2,5–4 kHz seulement si mesuré contre la voix`. Bus CUIVRES : `bx_glue 2,5:1, attaque 10, auto release, SC HPF 100 Hz, mix 60 % → J37 815 léger → envoi reverb commun (plate 1,2–1,6 s, pré-delay 20–30 ms)`. Pas de chorus, pas d'Imager sur une section réelle.

## Tests [TEST]
Chaque pupitre seul : registre jouable, aucune note hors tessiture · section : accords à 3–4 notes, pas de seconde majeure dans le grave · avec la voix : les cuivres jouent dans les trous · vélocité 60 vs 110 : deux couches distinctes · mono OK · export d'un stab : crête sous −6 dBFS avant bus.

## Variante
Ska/reggae : trompette et ténor à l'unisson, harmonie au trombone, cuivres hauts dans le mix, contretemps [HEUR]. Salsa : deux trompettes + trombone, moñas sur le montuno, attaques sur la clave [HEUR].
