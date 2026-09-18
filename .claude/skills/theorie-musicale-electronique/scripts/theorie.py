#!/usr/bin/env python3
"""Outils de théorie musicale pour la production électronique (stdlib seulement).
Numérotation Ableton : C3 = 60. Octave scientifique = octave Ableton + 1.

  theorie.py gamme F mineur                 notes, degrés, accords diatoniques
  theorie.py modes [F]                      les modes et leur note caractéristique
  theorie.py accord Fm9 [--octave 2] [--voicing ferme|ouvert|drop2]
  theorie.py progression "Fm9 Dbmaj7 Abmaj7 Eb" --tonalite "F mineur" [--octave 3]
  theorie.py transpose "C E G" 3            transposition chromatique T_n
  theorie.py inversion "C E G" 7            inversion de classes I_n
  theorie.py negatif "G7" --tonalite C      harmonie négative (axe tonique/quinte)
  theorie.py euclid 5 16 [rotation]         rythme euclidien sur une grille
  theorie.py syncope "x..x..x........."     indice de syncope (Longuet-Higgins & Lee)
  theorie.py contrepoint "Db4 F4 Eb4 Db4" "Bb4 Bb4 C5 Bb4" [--tonalite "Bb mineur"]
                                            intervalles, mouvement (contraire/oblique/direct), frottements
  theorie.py freq F1 | theorie.py freq 41   fréquence d'une note / note d'un MIDI
  theorie.py sub F                          table sub/kick pour une tonique
"""
import sys, argparse, math

NOMS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOMS_B = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

MODES = {  # intervalles en demi-tons depuis la tonique
    'majeur': [0, 2, 4, 5, 7, 9, 11], 'ionien': [0, 2, 4, 5, 7, 9, 11],
    'dorien': [0, 2, 3, 5, 7, 9, 10], 'phrygien': [0, 1, 3, 5, 7, 8, 10],
    'lydien': [0, 2, 4, 6, 7, 9, 11], 'mixolydien': [0, 2, 4, 5, 7, 9, 10],
    'mineur': [0, 2, 3, 5, 7, 8, 10], 'eolien': [0, 2, 3, 5, 7, 8, 10],
    'locrien': [0, 1, 3, 5, 6, 8, 10],
    'mineur-harmonique': [0, 2, 3, 5, 7, 8, 11], 'mineur-melodique': [0, 2, 3, 5, 7, 9, 11],
    'phrygien-dominant': [0, 1, 4, 5, 7, 8, 10], 'lydien-dominant': [0, 2, 4, 6, 7, 9, 10],
    'altere': [0, 1, 3, 4, 6, 8, 10], 'double-harmonique': [0, 1, 4, 5, 7, 8, 11],
    'hongroise-mineure': [0, 2, 3, 6, 7, 8, 11],
    'pentatonique-majeure': [0, 2, 4, 7, 9], 'pentatonique-mineure': [0, 3, 5, 7, 10],
    'blues': [0, 3, 5, 6, 7, 10], 'tons-entiers': [0, 2, 4, 6, 8, 10],
    'octatonique': [0, 2, 3, 5, 6, 8, 9, 11], 'hirajoshi': [0, 2, 3, 7, 8],
    'in': [0, 1, 5, 7, 8], 'insen': [0, 1, 5, 7, 10],
}
CARACTERISTIQUE = {
    'ionien': '7e majeure + 4te juste : repos, clarté', 'majeur': '7e majeure + 4te juste : repos, clarté',
    'dorien': '6te majeure sur un mineur : mineur lumineux (deep house, DnB liquid)',
    'phrygien': '2de mineure : sombre, tendu (psytrance, hard techno, dubstep)',
    'lydien': '4te augmentée : flottant, rêveur (ambient, future bass)',
    'mixolydien': '7e mineure sur un majeur : majeur relâché, funk, disco',
    'mineur': '6te et 7e mineures : le mineur « par défaut » de l\'électronique', 'eolien': 'idem mineur naturel',
    'locrien': '5te diminuée : instable, rarement centre tonal',
    'mineur-harmonique': '7e majeure sur un mineur : dominante forte, couleur orientale (2de augmentée)',
    'mineur-melodique': '6te et 7e majeures ascendantes : mineur jazz',
    'phrygien-dominant': 'b2 + 3 majeure : flamenco, psytrance, Moyen-Orient',
    'lydien-dominant': '#4 + b7 : Lydian b7, film, Simpsons',
    'altere': 'toutes les tensions altérées sur une dominante',
    'double-harmonique': 'b2 + 7 majeure : « byzantine », psytrance, hardstyle mélodique',
    'hongroise-mineure': 'mineur harmonique avec #4',
    'pentatonique-majeure': 'sans demi-tons : hooks faciles, pas de frottement',
    'pentatonique-mineure': 'base des riffs, blues, trap',
    'blues': 'pentatonique mineure + b5', 'tons-entiers': 'symétrique, flou, sans repos',
    'octatonique': 'demi-ton/ton, symétrique, tension', 'hirajoshi': 'pentatonique japonaise sombre',
    'in': 'pentatonique japonaise (b2)', 'insen': 'pentatonique japonaise (b2, b7)',
}

QUALITES = {  # symbole -> intervalles
    '': [0, 4, 7], 'maj': [0, 4, 7], 'M': [0, 4, 7], 'm': [0, 3, 7], 'min': [0, 3, 7], '-': [0, 3, 7],
    'dim': [0, 3, 6], '°': [0, 3, 6], 'aug': [0, 4, 8], '+': [0, 4, 8], '5': [0, 7],
    'sus2': [0, 2, 7], 'sus4': [0, 5, 7], 'sus': [0, 5, 7],
    '6': [0, 4, 7, 9], 'm6': [0, 3, 7, 9], '7': [0, 4, 7, 10], 'maj7': [0, 4, 7, 11], 'M7': [0, 4, 7, 11],
    'm7': [0, 3, 7, 10], 'min7': [0, 3, 7, 10], '-7': [0, 3, 7, 10], 'mmaj7': [0, 3, 7, 11], 'mM7': [0, 3, 7, 11],
    'dim7': [0, 3, 6, 9], '°7': [0, 3, 6, 9], 'm7b5': [0, 3, 6, 10], 'ø7': [0, 3, 6, 10], 'ø': [0, 3, 6, 10],
    '7sus4': [0, 5, 7, 10], '7sus2': [0, 2, 7, 10], 'add9': [0, 4, 7, 14], 'madd9': [0, 3, 7, 14],
    'add11': [0, 4, 7, 17], 'madd11': [0, 3, 7, 17], '9': [0, 4, 7, 10, 14], 'maj9': [0, 4, 7, 11, 14],
    'M9': [0, 4, 7, 11, 14], 'm9': [0, 3, 7, 10, 14], 'min9': [0, 3, 7, 10, 14], '69': [0, 4, 7, 9, 14],
    'm69': [0, 3, 7, 9, 14], '11': [0, 4, 7, 10, 14, 17], 'm11': [0, 3, 7, 10, 14, 17], 'maj11': [0, 4, 7, 11, 14, 17],
    '13': [0, 4, 7, 10, 14, 21], 'm13': [0, 3, 7, 10, 14, 21], 'maj13': [0, 4, 7, 11, 14, 21],
    '7b9': [0, 4, 7, 10, 13], '7#9': [0, 4, 7, 10, 15], '7#11': [0, 4, 7, 10, 18], 'maj7#11': [0, 4, 7, 11, 18],
    '7b5': [0, 4, 6, 10], '7#5': [0, 4, 8, 10], 'quartal': [0, 5, 10, 15], 'quintal': [0, 7, 14, 21],
}
# Limites d'intervalle dans le grave (note la plus basse de l'intervalle), MIDI (C3 = 60 Ableton).
# Valeurs d'orchestration usuelles ; dépendent du timbre (un sinus tolère plus bas qu'une scie).
LIMITES = {1: 52, 2: 51, 3: 48, 4: 46, 5: 46, 6: 46, 7: 34, 8: 39, 9: 36, 10: 41, 11: 41}


def nom(pc, bemol=False):
    return (NOMS_B if bemol else NOMS)[pc % 12]


def parse_note(s):
    """'F#1', 'Bb', 'C3' -> (classe, octave|None). Octave Ableton."""
    s = s.strip()
    if not s or s[0].upper() not in PC:
        raise ValueError(f'note illisible : {s}')
    pc = PC[s[0].upper()]; i = 1
    while i < len(s) and s[i] in '#b':
        pc += 1 if s[i] == '#' else -1; i += 1
    octv = int(s[i:]) if s[i:].lstrip('-').isdigit() else None
    return pc % 12, octv


def midi(pc, octv):
    return (octv + 2) * 12 + pc  # C3 = 60 -> C(-2) = 0


def nom_midi(n, bemol=False):
    return f'{nom(n, bemol)}{n // 12 - 2}'


def freq(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def parse_accord(sym):
    """'Dbmaj7/F' -> (racine pc, qualité, intervalles, basse pc|None)"""
    basse = None
    if '/' in sym:
        sym, b = sym.split('/', 1); basse = parse_note(b)[0]
    pc, _ = parse_note(sym); i = 1
    while i < len(sym) and sym[i] in '#b':
        i += 1
    q = sym[i:]
    if q not in QUALITES:
        raise ValueError(f'qualité inconnue « {q} » dans {sym} (connues : {", ".join(sorted(QUALITES))})')
    return pc, q, QUALITES[q], basse


def gamme(tonique, mode):
    mode = mode.lower().replace('_', '-')
    if mode not in MODES:
        raise ValueError(f'mode inconnu : {mode} (connus : {", ".join(MODES)})')
    return [(tonique + i) % 12 for i in MODES[mode]], mode


LETTRES = 'CDEFGAB'
FLAT_KEYS = {5, 10, 3, 8, 1, 6}


def epellation(tonique_nom, notes):
    """Dict classe -> nom, avec lettres consécutives pour 7 notes (F mineur -> Ab, pas G#)."""
    if len(notes) == 7:
        li = LETTRES.index(tonique_nom[0].upper()); m = {}
        for i, pc in enumerate(notes):
            lettre = LETTRES[(li + i) % 7]; nat = PC[lettre]; d = (pc - nat) % 12
            if d > 6: d -= 12
            m[pc] = lettre + {-2: 'bb', -1: 'b', 0: '', 1: '#', 2: '##'}.get(d, '?')
        return m
    bem = notes[0] in FLAT_KEYS or 'b' in tonique_nom[1:]
    return {pc: nom(pc, bem) for pc in notes}


def nommer(pc, m, bem=True):
    return m.get(pc % 12, nom(pc, bem))


ROMAINS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']


def degre(pc_root, quality_ivs, tonique, mode_ivs):
    """Chiffrage romain d'un accord dans une gamme heptatonique ; b/# si racine hors gamme."""
    d = (pc_root - tonique) % 12
    if d in mode_ivs:
        idx = mode_ivs.index(d); alt = ''
    else:
        # degré le plus proche au-dessus, précédé de b
        above = [i for i, v in enumerate(mode_ivs) if v > d]
        idx = above[0] if above else 0; alt = 'b'
    r = ROMAINS[idx]
    mineur = 3 in quality_ivs and 4 not in quality_ivs
    dim = 6 in quality_ivs and 7 not in quality_ivs
    r = r.lower() if (mineur or dim) else r
    return alt + r + ('°' if dim else '')


def voicing_notes(pc, ivs, octave, style, basse=None):
    notes = [midi(pc, octave) + iv for iv in ivs]
    if style == 'ouvert' and len(notes) >= 3:
        notes = [notes[0]] + [notes[2]] + [n + 12 for n in notes[1:2]] + [n + 12 for n in notes[3:]]
    elif style == 'drop2' and len(notes) >= 4:
        notes = sorted(notes); notes[-2] -= 12
    if basse is not None:
        b = midi(basse, octave - 1)
        notes = [b] + [n for n in sorted(notes)]
    return sorted(notes)


def verif_grave(notes):
    avis = []
    for a, b in zip(notes, notes[1:]):
        iv = (b - a)
        if iv == 0 or iv % 12 == 0:
            continue
        lim = LIMITES.get(iv % 12 if iv < 12 else iv % 12, None)
        if iv < 12 and lim and a < lim:
            avis.append(f'{nom_midi(a)}–{nom_midi(b)} ({iv} demi-tons) sous la limite usuelle ({nom_midi(lim)}) : risque de boue')
    return avis


def euclid(k, n, rot=0):
    """Bjorklund : k attaques réparties sur n pas."""
    if k <= 0: return [0] * n
    if k >= n: return [1] * n
    pattern = []; counts = []; remainders = [k]; divisor = n - k; level = 0
    while True:
        counts.append(divisor // remainders[level]); remainders.append(divisor % remainders[level])
        divisor = remainders[level]; level += 1
        if remainders[level] <= 1: break
    counts.append(divisor)
    def build(l):
        if l == -1: pattern.append(0)
        elif l == -2: pattern.append(1)
        else:
            for _ in range(counts[l]): build(l - 1)
            if remainders[l] != 0: build(l - 2)
    build(level)
    i = pattern.index(1); pattern = pattern[i:] + pattern[:i]
    return pattern[-rot % n:] + pattern[:-rot % n] if rot else pattern


def grille(p):
    s = ''
    for i, v in enumerate(p):
        s += ('x' if v else '.') + (' | ' if (i + 1) % 4 == 0 and i + 1 < len(p) else ' ')
    return s.strip()


def cmd_gamme(a):
    t, _ = parse_note(a.tonique); notes, mode = gamme(t, a.mode); m = epellation(a.tonique, notes)
    print(f'{nommer(t, m)} {mode} — {CARACTERISTIQUE.get(mode, "")}')
    print('Degrés :', ' '.join(f'{i + 1}:{nommer(n, m)}' for i, n in enumerate(notes)))
    if len(notes) == 7:
        print('Accords diatoniques (triade / 7e) :')
        for i in range(7):
            tri = [notes[i], notes[(i + 2) % 7], notes[(i + 4) % 7]]
            sept = tri + [notes[(i + 6) % 7]]
            ivs = sorted(((x - tri[0]) % 12) for x in tri); ivs7 = sorted(((x - sept[0]) % 12) for x in sept)
            q = {(0, 4, 7): '', (0, 3, 7): 'm', (0, 3, 6): 'dim', (0, 4, 8): 'aug'}.get(tuple(ivs), '?')
            q7 = {(0, 4, 7, 11): 'maj7', (0, 3, 7, 10): 'm7', (0, 4, 7, 10): '7', (0, 3, 6, 10): 'm7b5',
                  (0, 3, 6, 9): 'dim7', (0, 3, 7, 11): 'mmaj7', (0, 4, 8, 11): 'maj7#5'}.get(tuple(ivs7), '?')
            print(f'  {degre(tri[0], ivs, t, MODES[mode]):>5}  {nommer(tri[0], m)}{q:<4} {nommer(tri[0], m)}{q7}')


def cmd_modes(a):
    t = parse_note(a.tonique)[0] if a.tonique else 0
    for m, ivs in MODES.items():
        print(f'{m:<22} {" ".join(nom((t + i) % 12, True) for i in ivs):<32} {CARACTERISTIQUE.get(m, "")}')


def cmd_accord(a):
    pc, q, ivs, basse = parse_accord(a.symbole)
    notes = voicing_notes(pc, ivs, a.octave, a.voicing, basse)
    bem = 'b' in a.symbole[1:2] or (pc in FLAT_KEYS and '#' not in a.symbole[1:2])
    print(f'{a.symbole} : classes {" ".join(nom((pc + i) % 12, bem) for i in ivs)}')
    print(f'Voicing {a.voicing} depuis l\'octave {a.octave} : {" ".join(nom_midi(n, bem) for n in notes)}  MIDI {notes}')
    for av in verif_grave(notes): print('  ⚠', av)


def cmd_progression(a):
    ton_s = a.tonalite.split(); t = parse_note(ton_s[0])[0]; mode = ton_s[1] if len(ton_s) > 1 else 'mineur'
    sc, mode = gamme(t, mode); m = epellation(ton_s[0], sc); bem = sc[0] in FLAT_KEYS or 'b' in ton_s[0][1:]
    prev = None; total = 0
    print(f'Tonalité {nommer(t, m)} {mode} : {" ".join(nommer(n, m) for n in sc)}')
    for sym in a.accords.split():
        pc, q, ivs, basse = parse_accord(sym)
        hors = [nom((pc + i) % 12, bem) for i in ivs if (pc + i) % 12 not in sc]
        nm = lambda n: nommer(n, m, bem) + str(n // 12 - 2)
        # conduite des voix : parmi les renversements/octaves, le plus proche du précédent
        cands = []
        for octv in (a.octave - 1, a.octave, a.octave + 1):
            base = voicing_notes(pc, ivs, octv, 'ferme', None)
            for r in range(len(base)):
                v = sorted(base[r:] + [n + 12 for n in base[:r]])
                cands.append(v)
        if prev:
            def cout(v):
                return sum(min(abs(x - y) for y in prev) for x in v) + sum(min(abs(x - y) for y in v) for x in prev)
            best = min(cands, key=cout); mv = cout(best) // 2
        else:
            best = min(cands, key=lambda v: abs(v[0] - midi(pc, a.octave))); mv = 0
        total += mv
        if basse is not None:
            best = [midi(basse, a.octave - 1)] + best
        rom = degre(pc, ivs, t, MODES[mode]) if len(sc) == 7 else '—'
        print(f'{sym:<9} {rom:<6} {" ".join(nm(n) for n in best):<28} MIDI {best}'
              + (f'   hors gamme : {" ".join(hors)} (emprunt / couleur)' if hors else '')
              + (f'   mouvement ≈ {mv} demi-tons' if prev else ''))
        for av in verif_grave(best): print('   ⚠', av)
        cl = [f'{nom_midi(x, bem)}–{nom_midi(y, bem)}' for x, y in zip(best[1:], best[2:]) if 0 < y - x <= 2]
        if cl: print('   ⚠ cluster :', ', '.join(cl), '— écarter une voix d\'une octave si le pad doit rester lisible')
        prev = best
    print(f'Mouvement total des voix ≈ {total} demi-tons (plus petit = plus lié).')


def pcs(s):
    return [parse_note(x)[0] for x in s.replace(',', ' ').split()]


def cmd_transpose(a):
    src = pcs(a.notes); out = [(p + a.n) % 12 for p in src]
    print(f'T_{a.n}({" ".join(nom(p, True) for p in src)}) = {" ".join(nom(p, True) for p in out)}   classes {out}')


def cmd_inversion(a):
    src = pcs(a.notes); out = [(a.n - p) % 12 for p in src]
    print(f'I_{a.n}({" ".join(nom(p, True) for p in src)}) = {" ".join(nom(p, True) for p in out)}   classes {out}')


def cmd_negatif(a):
    t = parse_note(a.tonalite.split()[0])[0]
    pc, q, ivs, _ = parse_accord(a.symbole)
    src = [(pc + i) % 12 for i in ivs]; out = [(2 * t + 7 - p) % 12 for p in src]
    print(f'Axe entre {nom(t, True)} et {nom((t + 7) % 12, True)} : {a.symbole} ({" ".join(nom(p, True) for p in src)})'
          f' → {" ".join(nom(p, True) for p in out)}')
    print('Lire l\'accord obtenu par sa basse la plus probable ; ex. en C, G7 → Fm6, C → Cm.')


def cmd_euclid(a):
    p = euclid(a.k, a.n, a.rotation)
    print(f'E({a.k},{a.n}) rotation {a.rotation} : {grille(p)}')
    print('Pas actifs (0 = premier pas) :', [i for i, v in enumerate(p) if v])


def cmd_contrepoint(a):
    """Deux voix note à note : intervalle, mouvement, frottements, notes hors gamme."""
    def suite(s):
        out = []
        for x in s.replace(',', ' ').split():
            pc, octv = parse_note(x)
            if octv is None: raise SystemExit(f'octave manquante : {x} (ex. Db4)')
            out.append(midi(pc, octv))
        return out
    v1, v2 = suite(a.voix1), suite(a.voix2)
    if len(v1) != len(v2): raise SystemExit(f'{len(v1)} notes contre {len(v2)} : même nombre attendu')
    sc = None
    if a.tonalite:
        ton = a.tonalite.split(); sc = gamme(parse_note(ton[0])[0], ton[1] if len(ton) > 1 else 'mineur')[0]
        hors = sorted({nom(n % 12, True) for n in v1 + v2 if n % 12 not in sc})
        print('hors gamme :', ' '.join(hors) if hors else 'aucune')
    NOMI = {0: 'unisson', 1: '2m', 2: '2M', 3: '3m', 4: '3M', 5: '4', 6: 'triton', 7: '5', 8: '6m', 9: '6M', 10: '7m', 11: '7M'}
    par = 0
    for i, (a1, b1) in enumerate(zip(v1, v2)):
        iv = abs(b1 - a1); nm = 'octave' if iv and iv % 12 == 0 else NOMI[iv % 12]
        mv = ''
        if i:
            d1, d2 = v1[i] - v1[i - 1], v2[i] - v2[i - 1]
            mv = 'contraire' if d1 * d2 < 0 else ('oblique' if d1 == 0 or d2 == 0 else 'direct')
            if mv == 'direct' and iv % 12 in (0, 7):
                par += 1; mv += ' ⚠ quinte/octave parallèle'
        flag = ' ⚠ frottement' if iv % 12 in (1, 11) and iv < 24 else ''
        print(f'  {i + 1:>2}  {nom_midi(a1, True):<5} {nom_midi(b1, True):<5} {nm:<8} {mv}{flag}')
    print(f'Mouvements contraires recommandés quand la voix principale bouge ; {par} parallélisme(s) de quinte/octave.')


def cmd_syncope(a):
    """Indice de syncope de Longuet-Higgins & Lee sur une grille de 16 (ou 8) cases."""
    g = [c for c in a.grille.replace('|', '').replace(' ', '') if c in 'x.oX']
    n = len(g)
    if n not in (8, 16): raise SystemExit('grille de 8 ou 16 cases attendue (x . o X)')
    def poids(i):
        i = i * (16 // n)
        return 0 if i == 0 else -1 if i == 8 else -2 if i % 4 == 0 else -3 if i % 2 == 0 else -4
    notes = [i for i, c in enumerate(g) if c != '.']; total = 0; det = []
    for i in notes:
        j = (i + 1) % n; best = None
        while g[j] == '.':
            best = poids(j) if best is None else max(best, poids(j)); j = (j + 1) % n
            if j == i: break
        if best is not None and best > poids(i):
            total += best - poids(i); det.append(f'case {i + 1} ({poids(i)}) → repos {best} : +{best - poids(i)}')
    print(f'{grille([0 if c == "." else 1 for c in g])}\nIndice LHL = {total}  (four-on-the-floor 0, tresillo 4)')
    for d in det: print('  ', d)


def cmd_freq(a):
    s = a.note
    if s.lstrip('-').isdigit():
        n = int(s); print(f'MIDI {n} = {nom_midi(n)} ({nom_midi(n, True)}) = {freq(n):.2f} Hz')
    else:
        pc, octv = parse_note(s)
        if octv is None: raise SystemExit('donne une octave, ex. F1')
        n = midi(pc, octv); print(f'{s} = MIDI {n} = {freq(n):.2f} Hz ; harmoniques 2–4 : '
                                  + ', '.join(f'{freq(n) * k:.1f}' for k in (2, 3, 4)))


def cmd_sub(a):
    t = parse_note(a.tonique)[0]
    print(f'Tonique {nom(t, True)} — sub et kick accordés (Ableton C3 = 60) :')
    for octv in (-1, 0, 1, 2):
        n = midi(t, octv); q = n + 7
        print(f'  {nom_midi(n, True):<5} MIDI {n:>3} {freq(n):7.2f} Hz   quinte {nom_midi(q, True)} {freq(q):7.2f} Hz')
    print('Sub : octave 0 (≈ 30–65 Hz) ; octave 1 = basse jouée (65–130 Hz). Kick accordé sur la tonique ou la quinte, une octave au-dessus du sub.')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest='cmd', required=True)
    s = sp.add_parser('gamme'); s.add_argument('tonique'); s.add_argument('mode', nargs='?', default='mineur'); s.set_defaults(f=cmd_gamme)
    s = sp.add_parser('modes'); s.add_argument('tonique', nargs='?'); s.set_defaults(f=cmd_modes)
    s = sp.add_parser('accord'); s.add_argument('symbole'); s.add_argument('--octave', type=int, default=3)
    s.add_argument('--voicing', choices=['ferme', 'ouvert', 'drop2'], default='ferme'); s.set_defaults(f=cmd_accord)
    s = sp.add_parser('progression'); s.add_argument('accords'); s.add_argument('--tonalite', required=True)
    s.add_argument('--octave', type=int, default=3); s.set_defaults(f=cmd_progression)
    s = sp.add_parser('transpose'); s.add_argument('notes'); s.add_argument('n', type=int); s.set_defaults(f=cmd_transpose)
    s = sp.add_parser('inversion'); s.add_argument('notes'); s.add_argument('n', type=int); s.set_defaults(f=cmd_inversion)
    s = sp.add_parser('negatif'); s.add_argument('symbole'); s.add_argument('--tonalite', required=True); s.set_defaults(f=cmd_negatif)
    s = sp.add_parser('euclid'); s.add_argument('k', type=int); s.add_argument('n', type=int)
    s.add_argument('rotation', type=int, nargs='?', default=0); s.set_defaults(f=cmd_euclid)
    s = sp.add_parser('contrepoint'); s.add_argument('voix1'); s.add_argument('voix2')
    s.add_argument('--tonalite'); s.set_defaults(f=cmd_contrepoint)
    s = sp.add_parser('syncope'); s.add_argument('grille'); s.set_defaults(f=cmd_syncope)
    s = sp.add_parser('freq'); s.add_argument('note'); s.set_defaults(f=cmd_freq)
    s = sp.add_parser('sub'); s.add_argument('tonique'); s.set_defaults(f=cmd_sub)
    a = p.parse_args()
    try:
        a.f(a)
    except ValueError as e:
        raise SystemExit(f'Erreur : {e}')


if __name__ == '__main__':
    main()
