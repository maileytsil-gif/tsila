#!/usr/bin/env python3
"""grille.py — grille de doubles croches du skill → tableau, notation Producer Pal et contrôle harmonique.

Notation d'une voix (4/4, une mesure entre deux « | ») :
    Ab3[1&:2] C4[2a:1] Eb4[3&:2] C4[4&:1] | Ab3[1&:2] … | % | …
    position : 1 e & a 2 e & a 3 e & a 4 e & a  (« 2a » = dernière double croche du temps 2 ; « + » = « & »)
    durée    : en doubles croches (décimales admises) ; « [pos:durée:vélocité] » fixe la vélocité d'une note
    F3+Ab3+C4[1:4] = accord ; Bb3![3a:1] = tension voulue (non signalée) ; « % » = mesure précédente
Numérotation Ableton C3 = 60 (le numéro MIDI fait foi). --source scientifique lit C4 = 60 et convertit.

Usage :
  grille.py "Ab3[1&:2] C4[2a:1] | …" [--accords "Fm9 | Fm9 | Bb13 | Bb13"] [--vel 96] [--source scientifique]
            [--transposer N] [--format rapport|ppal|tableau|json]
  grille.py --fichier references/atelier-themes.md [--titre funk] [--transposer N] [--format …]
  grille.py --verifier references/*.md          blocs ```grille``` : code 1 si erreur (lecture, chevauchement,
                                               note hors accord non résolue et non marquée « ! »)
Un bloc ```grille``` contient des lignes « clé: valeur » : titre, tempo, accords, source, vel ; toute autre clé est une voix.
Accords : un symbole par mesure, séparés par « | » ; deux symboles dans une mesure se partagent la mesure.
Contrôle, pas écoute : une note hors accord est « résolue » si la note suivante de la voix est à 1–2 demi-tons et
appartient à l'accord ; les frottements de demi-ton / neuvième mineure entre voix sont signalés pour information.
"""
import argparse
import json
import re
import sys
from fractions import Fraction as F

PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NOMS_B = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
SUBDIV = {'': 0, 'e': 1, '&': 2, '+': 2, 'a': 3}
# Mêmes symboles et intervalles que compositeur-arrangeur/modules/theorie-musicale-electronique/scripts/theorie.py (vérifié par test_grille.py).
QUALITES = {
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
    '7b9#9': [0, 4, 7, 10, 13, 15], '7b9b13': [0, 4, 7, 10, 13, 20], '7alt': [0, 4, 10, 13, 15, 18, 20],
}


def lire_note(s, source='ableton'):
    """'Ab3' -> MIDI (C3 = 60 ; en source scientifique C4 = 60)."""
    m = re.fullmatch(r'([A-Ga-g])([#b♯♭]*)(-?\d+)', s.strip())
    if not m:
        raise ValueError(f'note illisible : « {s} » (attendu p. ex. Ab3, F#1, C-1)')
    pc = PC[m.group(1).upper()] + sum(1 if c in '#♯' else -1 for c in m.group(2))
    octv = int(m.group(3))
    n = (octv + (1 if source == 'scientifique' else 2)) * 12 + pc
    if not 0 <= n <= 127:
        raise ValueError(f'note hors MIDI 0–127 : {s} → {n}')
    return n


def nom(n):
    return f'{NOMS_B[n % 12]}{n // 12 - 2}'


def lire_accord(sym):
    """'Bb13' -> (racine, classes) ; 'A7(b9,#9)' = 'A7b9#9' ; '/basse' ajoutée aux classes."""
    s = sym.strip().replace('♭', 'b').replace('♯', '#').replace('(', '').replace(')', '').replace(',', '')
    basse = None
    if '/' in s:
        s, b = s.split('/', 1)
        basse = lire_note(b + '0') % 12
    m = re.fullmatch(r'([A-G])([#b]*)(.*)', s)
    if not m or m.group(3) not in QUALITES:
        raise ValueError(f'accord inconnu : « {sym} » (qualités : {", ".join(sorted(k for k in QUALITES if k))})')
    racine = (PC[m.group(1)] + sum(1 if c == '#' else -1 for c in m.group(2))) % 12
    ivs = QUALITES[m.group(3)]
    classes = {(racine + i) % 12 for i in ivs} | ({basse} if basse is not None else set())
    return racine, classes, {i % 12 for i in ivs}


def degre(n, racine, ivs):
    """Nom du degré d'une classe dans l'accord (1, b3, 3, 5, b7, 9, 13…)."""
    i = (n - racine) % 12
    tierce_majeure = 4 in ivs
    return {0: '1', 1: 'b9', 2: '9', 3: '#9' if tierce_majeure else 'b3', 4: '3', 5: '11',
            6: 'b5' if (7 not in ivs and 6 in ivs and not tierce_majeure) else '#11', 7: '5',
            8: '#5' if (7 not in ivs and tierce_majeure and 10 not in ivs) else 'b13',
            9: '6' if 10 not in ivs and 11 not in ivs else '13', 10: 'b7', 11: '7'}[i]


def lire_position(tok, mesure):
    m = re.fullmatch(r'([1-4])([e&+a]?)', tok.strip())
    if not m:
        raise ValueError(f'position illisible « {tok} » en mesure {mesure} (attendu 1, 1e, 1&, 1a … 4a)')
    return (int(m.group(1)) - 1) * 4 + SUBDIV[m.group(2)]


def lire_voix(texte, source='ableton', vel=96):
    """Retourne une liste de notes {mesure, pas (0–15), duree (doubles croches), midi, vel, voulue}."""
    notes, precedente = [], []
    for i, bloc in enumerate(texte.split('|')):
        mesure = i + 1
        bloc = bloc.strip()
        if bloc == '%':
            courante = [dict(n, mesure=mesure) for n in precedente]
        else:
            courante = []
            for tok in bloc.split():
                m = re.fullmatch(r'([^\[\]]+?)(!?)\[([^\]:]+):([\d.]+)(?::(\d+))?\]', tok)
                if not m:
                    raise ValueError(f'jeton illisible « {tok} » en mesure {mesure} (attendu Note[pos:durée] ou Note[pos:durée:vél])')
                pas = lire_position(m.group(3), mesure)
                duree = F(m.group(4)).limit_denominator(64)
                if duree <= 0:
                    raise ValueError(f'durée nulle « {tok} » en mesure {mesure}')
                v = int(m.group(5)) if m.group(5) else vel
                if not 1 <= v <= 127:
                    raise ValueError(f'vélocité hors 1–127 « {tok} » en mesure {mesure}')
                for part in m.group(1).split('+'):
                    courante.append({'mesure': mesure, 'pas': pas, 'duree': duree, 'midi': lire_note(part, source),
                                     'vel': v, 'voulue': bool(m.group(2))})
        notes.extend(courante)
        precedente = courante
    return sorted(notes, key=lambda n: (n['mesure'], n['pas'], n['midi']))


def lire_accords(texte):
    """'Fm9 | Fm9 | Bb13 Eb9' -> liste par mesure de [(pas de début, symbole, racine, classes, intervalles)]."""
    par_mesure = []
    for bloc in texte.split('|'):
        syms = bloc.split()
        if not syms:
            par_mesure.append(par_mesure[-1] if par_mesure else [])
            continue
        pas = [F(16 * k, len(syms)) for k in range(len(syms))]
        par_mesure.append([(p, s) + lire_accord(s) for p, s in zip(pas, syms)])
    return par_mesure


def accord_a(accords, mesure, pas):
    if not accords:
        return None
    liste = accords[min(mesure, len(accords)) - 1]
    courant = None
    for a in liste:
        if a[0] <= pas:
            courant = a
    return courant


def debut(n):
    return (n['mesure'] - 1) * 16 + n['pas']


def pos_ppal(n):
    return f"{n['mesure']}|{float(1 + F(n['pas'], 4)):g}"


def duree_ppal(d):
    r = F(d) / 16  # fraction de ronde
    return f'n/{r.denominator}' if r.numerator == 1 else f'n{r.numerator}/{r.denominator}'


def analyser(notes, accords):
    """Ajoute degré et statut à chaque note ; retourne la liste des erreurs."""
    erreurs = []
    for k, n in enumerate(notes):
        a = accord_a(accords, n['mesure'], n['pas'])
        n['accord'] = a[1] if a else ''
        if not a:
            n['degre'], n['statut'] = '', ''
            continue
        _, _, racine, classes, ivs = a
        n['degre'] = degre(n['midi'], racine, ivs)
        if n['midi'] % 12 in classes:
            n['statut'] = 'accord'
            continue
        suivantes = [s for s in notes[k + 1:] if debut(s) > debut(n)]
        suite = [s for s in suivantes if debut(s) == debut(suivantes[0])] if suivantes else []
        resolue = False
        for s in suite:
            b = accord_a(accords, s['mesure'], s['pas'])
            if b and s['midi'] % 12 in b[3] and 1 <= abs(s['midi'] - n['midi']) <= 2:
                resolue = True
        if resolue:
            n['statut'] = 'passage/approche'
        elif n['voulue']:
            n['statut'] = 'tension voulue'
        else:
            n['statut'] = '⚠ hors accord non résolue'
            voisins = sorted({NOMS_B[c] for c in classes if (n['midi'] - c) % 12 in (1, 11)})
            erreurs.append(f"{pos_ppal(n)} {nom(n['midi'])} sur {a[1]} : hors accord, non résolue"
                           + (f" — demi-ton contre {', '.join(voisins)}" if voisins else ''))
    # chevauchements de même hauteur dans la voix
    for i, n in enumerate(notes):
        for s in notes[i + 1:]:
            if s['midi'] == n['midi'] and debut(s) < debut(n) + n['duree']:
                erreurs.append(f"{pos_ppal(n)} {nom(n['midi'])} chevauche la même note en {pos_ppal(s)}")
    return erreurs


def frottements(voix):
    """Demi-ton ou neuvième mineure entre deux voix qui sonnent ensemble (information)."""
    infos, noms = [], list(voix)
    for i, a in enumerate(noms):
        for b in noms[i + 1:]:
            for n in voix[a]:
                for s in voix[b]:
                    d0, d1 = max(debut(n), debut(s)), min(debut(n) + n['duree'], debut(s) + s['duree'])
                    if d0 < d1 and abs(n['midi'] - s['midi']) in (1, 13):
                        infos.append(f"{a}/{b} : {nom(n['midi'])} contre {nom(s['midi'])} "
                                     f"à la mesure {int(d0 // 16) + 1} (écart {abs(n['midi'] - s['midi'])} demi-tons)")
    return sorted(set(infos))


def attaques(notes, nb_mesures):
    lignes = []
    for m in range(1, nb_mesures + 1):
        cases = ['.'] * 16
        for n in notes:
            if n['mesure'] == m:
                cases[n['pas']] = 'x'
        lignes.append(''.join(cases))
    return lignes


def transposer_accords(texte, n):
    def t(sym):
        m = re.match(r'([A-G][#b♯♭]*)(.*)', sym)
        if not m:
            return sym
        racine = lire_note(m.group(1) + '3') + n
        reste = m.group(2)
        if '/' in reste:
            q, b = reste.split('/', 1)
            reste = q + '/' + NOMS_B[(lire_note(b + '3') + n) % 12]
        return NOMS_B[racine % 12] + reste
    return ' | '.join(' '.join(t(s) for s in bloc.split()) for bloc in texte.split('|'))


def sortie(titre, tempo, textes_accords, voix, fmt, transposer):
    """Analyse toutes les voix puis les met en forme ; retourne (erreurs, texte ou dict pour --format json)."""
    accords = lire_accords(textes_accords) if textes_accords else []
    nom_bloc = titre or 'grille'
    erreurs = {k: analyser(v, accords) for k, v in voix.items()}
    total_err = [f'{nom_bloc} / {k} : {e}' for k, es in erreurs.items() for e in es]
    if fmt == 'json':
        return total_err, {'titre': titre, 'tempo': tempo, 'accords': textes_accords, 'voix': {
            k: [{'mesure': n['mesure'], 'temps': float(1 + F(n['pas'], 4)), 'midi': n['midi'], 'note': nom(n['midi']),
                 'duree_noires': float(F(n['duree']) / 4), 'vel': n['vel'], 'degre': n['degre'], 'statut': n['statut']}
                for n in v] for k, v in voix.items()}}
    nb_mesures = max([len(textes_accords.split('|')) if textes_accords else 0]
                     + [max((n['mesure'] for n in v), default=0) for v in voix.values()])
    rapport = [f"== {nom_bloc}" + (f" — {tempo} BPM" if tempo else '') + (f" — transposé de {transposer:+d}" if transposer else '')
               + (f"\n   accords : {textes_accords}" if textes_accords else '')]
    if fmt == 'ppal':
        rapport = ['# ' + ligne.strip() for ligne in rapport[0].splitlines()]
    for nomv, notes in voix.items():
        if fmt in ('rapport', 'tableau'):
            rapport.append(f'\n-- {nomv}')
            rapport.append('| Mesure\\|Temps | Note | Octave | Début (noire = 1) | Durée (noires) | Vélocité | MIDI | Degré |')
            rapport.append('|---|---|---|---|---|---|---|---|')
            for n in notes:
                deg = n['degre'] + (f" ({n['statut']})" if n['statut'] not in ('', 'accord') else '')
                temps = f"{float(1 + F(n['pas'], 4)):g}"
                rapport.append(f"| {n['mesure']}\\|{temps} | {NOMS_B[n['midi'] % 12]} | {n['midi'] // 12 - 2} | {temps} "
                               f"| {float(F(n['duree']) / 4):g} | {n['vel']} | {n['midi']} | {deg} |")
        if fmt == 'ppal':
            rapport.append(f'# {nomv}')
        if fmt in ('rapport', 'ppal'):
            if fmt == 'rapport':
                rapport.append('Producer Pal :')
            rapport += [f"v{n['vel']} {duree_ppal(n['duree'])} {nom(n['midi'])} {pos_ppal(n)}" for n in notes]
        if fmt == 'rapport':
            if notes:
                bas, haut = min(n['midi'] for n in notes), max(n['midi'] for n in notes)
                rapport.append(f"Tessiture : {nom(bas)}–{nom(haut)} (MIDI {bas}–{haut})")
            rapport.append('Attaques (theorie.py syncope) : ' + ' | '.join(attaques(notes, nb_mesures)))
            rapport.append(('Contrôle : ' + '; '.join(erreurs[nomv])) if erreurs[nomv]
                           else 'Contrôle : aucune note hors accord non résolue, aucun chevauchement')
    if fmt == 'rapport' and len(voix) > 1:
        fr = frottements(voix)
        rapport.append('\nFrottements entre voix (information) : ' + ('; '.join(fr) if fr else 'aucun'))
    return total_err, '\n'.join(rapport)


def blocs(chemin):
    with open(chemin, encoding='utf-8') as f:
        texte = f.read()
    for m in re.finditer(r'^```grille[^\n]*\n(.*?)^```', texte, re.S | re.M):
        bloc = {'voix': {}}
        for ligne in m.group(1).splitlines():
            ligne = ligne.strip()
            if not ligne or ligne.startswith('#'):
                continue
            cle, _, val = ligne.partition(':')
            cle, val = cle.strip(), val.strip()
            if cle in ('titre', 'tempo', 'accords', 'source', 'vel'):
                bloc[cle] = val
            else:
                bloc['voix'][cle] = val
        yield bloc


def traiter(bloc, fmt, transposer):
    source = bloc.get('source', 'ableton')
    vel = int(bloc.get('vel', 96))
    voix = {}
    for k, v in bloc['voix'].items():
        notes = lire_voix(v, source, vel)
        for n in notes:
            n['midi'] += transposer
            if not 0 <= n['midi'] <= 127:
                raise ValueError(f'{k} : transposition hors MIDI 0–127')
        voix[k] = notes
    accords = transposer_accords(bloc['accords'], transposer) if bloc.get('accords') and transposer else bloc.get('accords', '')
    return sortie(bloc.get('titre', ''), bloc.get('tempo', ''), accords, voix, fmt, transposer)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__.split('\n', 1)[1])
    p.add_argument('grille', nargs='?', help='voix en notation de grille (entre guillemets)')
    p.add_argument('--accords', default='', help='un accord par mesure, séparés par « | »')
    p.add_argument('--vel', type=int, default=96)
    p.add_argument('--source', choices=['ableton', 'scientifique'], default='ableton',
                   help='convention des octaves de la grille lue (sortie toujours en C3 = 60)')
    p.add_argument('--transposer', type=int, default=0, help='demi-tons, notes et accords')
    p.add_argument('--format', choices=['rapport', 'ppal', 'tableau', 'json'], default='rapport')
    p.add_argument('--fichier', nargs='+', help='lire les blocs ```grille``` de ces fichiers')
    p.add_argument('--titre', default='', help='avec --fichier : blocs dont le titre contient ce texte')
    p.add_argument('--verifier', nargs='+', metavar='FICHIER', help='vérifier tous les blocs ```grille``` (code 1 si erreur)')
    a = p.parse_args(argv)
    try:
        if a.verifier:
            erreurs, compte = [], 0
            for chemin in a.verifier:
                for b in blocs(chemin):
                    compte += 1
                    e, _ = traiter(b, 'rapport', 0)
                    erreurs += [f'{chemin} : {x}' for x in e]
            print(f'{compte} bloc(s) vérifié(s), {len(erreurs)} erreur(s)')
            for e in erreurs:
                print('  ' + e)
            return 1 if erreurs else 0
        if a.fichier:
            trouves = [b for c in a.fichier for b in blocs(c) if a.titre.casefold() in b.get('titre', '').casefold()]
            if not trouves:
                p.error('aucun bloc ```grille``` correspondant')
            sorties = [traiter(b, a.format, a.transposer)[1] for b in trouves]
            print(json.dumps(sorties, ensure_ascii=False, indent=1) if a.format == 'json' else '\n\n'.join(sorties))
            return 0
        if not a.grille:
            p.error('donner une grille, --fichier ou --verifier')
        bloc = {'voix': {'voix': a.grille}, 'accords': a.accords, 'source': a.source, 'vel': a.vel}
        _, texte = traiter(bloc, a.format, a.transposer)
        print(json.dumps(texte, ensure_ascii=False, indent=1) if a.format == 'json' else texte)
        return 0
    except (ValueError, OSError) as e:
        print(f'Erreur : {e}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
