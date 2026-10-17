#!/usr/bin/env python3
"""Variations d'une prise WAV/AIFF hors de Live, calées sur la grille du morceau.

Trois gestes, chacun écrit dans un NOUVEAU fichier (la source n'est jamais modifiée) :
  fade     A, subtil : raccourcit la fin par un fondu (respiration avant la suite)
  stutter  B, créatif : répète une tranche d'une valeur de note à une position donnée
  reverse  C, risqué  : reverse swell (la note qui suit, inversée, monte vers son attaque)
                        ou reverse de queue (fin du fichier inversée et mélangée)
  toutes   écrit A, B et C dans un dossier vide, avec RAPPORT.json

Positions en notation Live, relatives au DÉBUT DU FICHIER (le fichier commence à 1.1.1),
mesure à 4 temps : « 4.4 » = mesure 4, temps 4 ; « 8.4.3 » = mesure 8, temps 4,
3e double croche ; « fin » = fin du fichier. Valeurs de note : 1/4, 1/8, 1/16, 1/32, 1/8t…

Exemples :
  variations_wav.py stutter basse.wav sortie.wav --bpm 126 --position 4.4 --grille 1/32 --repetitions 4
  variations_wav.py reverse lead.wav sortie.wav --bpm 126 --mode swell --cible 5.1 --longueur 1/4
  variations_wav.py toutes basse.wav dossier_vide --bpm 126

Mesures rapportées : crête échantillon et RMS en dBFS. Ni LUFS ni true peak. Le script ne
juge pas le résultat : écouter chaque variante dans la phrase, à niveau comparable.
Dépendances : numpy, soundfile.
"""
import argparse, hashlib, json, math, sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import soundfile as sf

FONDU_MS = 3.0  # fondus anti-clic aux coupes


# ---------- lecture, grille, mesures ----------

def charger(chemin):
    data, sr = sf.read(str(chemin), always_2d=True, dtype='float64')
    if data.size == 0 or not np.isfinite(data).all():
        raise SystemExit(f'{chemin} : audio vide ou valeurs non finies')
    return data, sr


def valeur_note(texte):
    """'1/16' -> fraction de ronde ; suffixe t = triolet, suffixe . = pointé."""
    t = texte.strip().lower()
    triolet, pointe = t.endswith('t'), t.endswith('.')
    t = t.rstrip('t.')
    try:
        f = Fraction(t)
    except ValueError:
        raise SystemExit(f'valeur de note illisible : {texte} (ex. 1/16, 1/8t, 1/8.)')
    if triolet:
        f *= Fraction(2, 3)
    if pointe:
        f *= Fraction(3, 2)
    return f


def echantillons(fraction_ronde, sr, bpm):
    return int(round(float(fraction_ronde) * 4 * 60 / bpm * sr))


def position(texte, sr, bpm, n):
    """'4.4' / '8.4.3' / 'fin' -> indice d'échantillon depuis le début du fichier."""
    if texte == 'fin':
        return n
    parts = [int(x) for x in texte.split('.')]
    if not 1 <= len(parts) <= 3 or any(p < 1 for p in parts):
        raise SystemExit(f'position illisible : {texte} (ex. 4.4 ou 8.4.3)')
    mes, tps, dbl = (parts + [1, 1])[:3]
    if tps > 4 or dbl > 4:
        raise SystemExit(f'position {texte} : 4 temps et 4 doubles croches au plus')
    temps = (mes - 1) * 4 + (tps - 1) + (dbl - 1) / 4
    i = int(round(temps * 60 / bpm * sr))
    if i > n:
        raise SystemExit(f'position {texte} au-delà de la fin du fichier ({n / sr:.3f} s)')
    return i


def db(x):
    return round(20 * math.log10(max(float(x), 1e-12)), 2)


def mesures(data):
    return {'crete_dbfs': db(np.max(np.abs(data))),
            'rms_dbfs': db(np.sqrt(np.mean(data ** 2))),
            'echantillons_a_0dbfs_ou_plus': int(np.sum(np.abs(data) >= 1.0))}


def part_grave(data, sr):
    n = min(len(data), 1 << 18)
    x = data[:n].mean(axis=1)
    p = np.abs(np.fft.rfft(x * np.hanning(n))) ** 2
    f = np.fft.rfftfreq(n, 1 / sr)
    return float(p[f < 120].sum() / max(p.sum(), 1e-30))


def rampe(k, montee):
    r = np.linspace(0.0, 1.0, k)[:, None]
    return r if montee else r[::-1]


# ---------- les trois gestes ----------

def fade(data, sr, fade_ms):
    if fade_ms <= 0:
        raise SystemExit('--fade-ms doit être positif')
    y = data.copy()
    k = min(len(y), max(2, round(sr * fade_ms / 1000)))
    # fondu en cosinus : plus naturel qu'une rampe linéaire sur une queue
    courbe = (0.5 + 0.5 * np.cos(np.linspace(0, math.pi, k)))[:, None]
    y[-k:] *= courbe
    return y, {'fade_ms': fade_ms}


def stutter(data, sr, bpm, debut, grille, repetitions, decroissance_db):
    if not 2 <= repetitions <= 16:
        raise SystemExit('--repetitions entre 2 et 16')
    tranche = echantillons(grille, sr, bpm)
    if tranche < 64:
        raise SystemExit('tranche trop courte : grille plus large ou BPM plus lent')
    i = position(debut, sr, bpm, len(data))
    if debut == 'fin':
        i = len(data) - tranche * repetitions
    depasse = i + tranche * repetitions - len(data)
    if i < 0 or depasse > tranche // 8:  # quelques échantillons d'arrondi de grille sont tolérés
        raise SystemExit('le stutter dépasse le fichier : position plus tôt ou moins de répétitions')
    y = data.copy()
    source = data[i:i + tranche].copy()
    f = min(max(2, round(sr * FONDU_MS / 1000)), tranche // 4)
    for j in range(repetitions):
        frag = source * 10 ** (-decroissance_db * j / 20)
        if j > 0:
            frag[:f] *= rampe(f, True)
        frag[-f:] *= rampe(f, False)
        lo, hi = i + j * tranche, min(i + (j + 1) * tranche, len(y))
        y[lo:hi] = frag[:hi - lo]
    # raccord avec la suite : petit fondu d'entrée de ce qui reprend après le stutter
    fin = i + tranche * repetitions
    if fin < len(y):
        k = min(f, len(y) - fin)
        y[fin:fin + k] *= rampe(k, True)
    return y, {'position': debut, 'debut_s': round(i / sr, 4), 'grille': str(grille),
               'repetitions': repetitions, 'tranche_ms': round(tranche / sr * 1000, 2),
               'decroissance_db_par_repetition': decroissance_db}


def reverse_swell(data, sr, bpm, cible, longueur, mix):
    """La matière qui commence à `cible`, inversée, placée juste AVANT `cible` :
    elle monte et culmine sur l'attaque. Durée du fichier inchangée."""
    k = echantillons(longueur, sr, bpm)
    c = position(cible, sr, bpm, len(data))
    if c - k < 0 or c + k > len(data):
        raise SystemExit('le swell sort du fichier : cible plus tard ou longueur plus courte')
    y = data.copy()
    rev = data[c:c + k][::-1].copy()
    rev *= np.linspace(0.0, 1.0, k)[:, None] ** 2  # montée progressive, pas d'attaque sèche
    f = min(max(2, round(sr * FONDU_MS / 1000)), k // 4)
    rev[-f:] *= rampe(f, False)  # s'efface juste avant l'attaque réelle
    y[c - k:c] += mix * rev
    return y, {'mode': 'swell', 'cible': cible, 'cible_s': round(c / sr, 4),
               'longueur': str(longueur), 'longueur_ms': round(k / sr * 1000, 2), 'mix': mix}


def reverse_queue(data, sr, queue_ms, mix):
    k = min(len(data), max(2, round(sr * queue_ms / 1000)))
    y = data.copy()
    queue = y[-k:].copy()
    melange = (1 - mix) * queue + mix * queue[::-1]
    f = min(max(2, round(sr * FONDU_MS / 1000)), k // 3)
    poids = np.ones(k)
    poids[:f] = np.linspace(0, 1, f)
    y[-k:] = queue + (melange - queue) * poids[:, None]
    return y, {'mode': 'queue', 'queue_ms': queue_ms, 'mix': mix}


# ---------- écriture ----------

def ecrire(source, dst, data, sr, y, geste, params, format_):
    src, dst = Path(source).resolve(), Path(dst).resolve()
    if src == dst:
        raise SystemExit('refus : la sortie écraserait la source')
    if dst.exists():
        raise SystemExit(f'refus : {dst} existe déjà')
    if y.shape != data.shape or not np.isfinite(y).all():
        raise SystemExit('résultat invalide (forme ou valeurs)')
    apres = mesures(y)
    alertes = []
    if format_ == 'PCM_24' and apres['echantillons_a_0dbfs_ou_plus']:
        alertes.append('crête ≥ 0 dBFS en 24 bits : écrêtage. Baisser la source ou --format FLOAT')
    ecart = np.abs(y - data).max(axis=1)
    zone = np.nonzero(ecart > 1e-7)[0]
    if not len(zone) or np.max(np.abs(data[zone[0]:zone[-1] + 1])) < 10 ** (-60 / 20):
        alertes.append('zone modifiée silencieuse (< −60 dBFS) : variante inaudible, choisir une '
                       'autre --position / --cible ou couper le silence de fin')
    if y.shape[1] == 2 and geste == 'stutter' and part_grave(data, sr) > 0.3:
        alertes.append('basse stéréo : vérifier le grave du stutter en mono')
    dst.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(dst), y, sr, format='WAV', subtype=format_)
    relu, sr2 = sf.read(str(dst), always_2d=True)
    if relu.shape != y.shape or sr2 != sr:
        dst.unlink()
        raise SystemExit('relecture différente du rendu : fichier supprimé')
    return {'geste': geste, 'sortie': str(dst), 'format': f'WAV {format_}', 'frequence': sr,
            'canaux': int(y.shape[1]), 'duree_s': round(len(y) / sr, 4), 'parametres': params,
            'avant': mesures(data), 'apres': apres, 'alertes': alertes,
            'sha256_sortie': hashlib.sha256(dst.read_bytes()).hexdigest()}


def appliquer(a, data, sr):
    if a.geste == 'fade':
        return fade(data, sr, a.fade_ms)
    if a.geste == 'stutter':
        return stutter(data, sr, a.bpm, a.position, valeur_note(a.grille), a.repetitions,
                       a.decroissance_db)
    if a.mode == 'swell':
        if not a.cible:
            raise SystemExit('--cible requis en mode swell (ex. 5.1 : l\'attaque à préparer)')
        return reverse_swell(data, sr, a.bpm, a.cible, valeur_note(a.longueur), a.mix)
    return reverse_queue(data, sr, a.queue_ms, a.mix)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='geste', required=True)

    def commun(p, sortie):
        p.add_argument('source')
        p.add_argument('sortie', help=sortie)
        p.add_argument('--bpm', type=float, required=True)
        p.add_argument('--format', choices=['PCM_24', 'FLOAT'], default='PCM_24')

    def opts_fade(p):
        p.add_argument('--fade-ms', type=float, default=30)

    def opts_stutter(p, pos='fin', grille='1/32', rep=4):
        p.add_argument('--position', default=pos, help='début du stutter (ex. 4.4) ou « fin »')
        p.add_argument('--grille', default=grille, help='taille de la tranche (1/16, 1/32, 1/16t…)')
        p.add_argument('--repetitions', type=int, default=rep)
        p.add_argument('--decroissance-db', type=float, default=0.0,
                       help='baisse de niveau à chaque répétition (0 = égales)')

    def opts_reverse(p, mode='queue'):
        p.add_argument('--mode', choices=['swell', 'queue'], default=mode)
        p.add_argument('--cible', help='swell : position de l\'attaque à préparer (ex. 5.1)')
        p.add_argument('--longueur', default='1/4', help='swell : durée du reverse (1/8, 1/4, 1/2…)')
        p.add_argument('--queue-ms', type=float, default=120)
        p.add_argument('--mix', type=float, default=0.7)

    p = sub.add_parser('fade'); commun(p, 'fichier WAV à créer'); opts_fade(p)
    p = sub.add_parser('stutter'); commun(p, 'fichier WAV à créer'); opts_stutter(p)
    p = sub.add_parser('reverse'); commun(p, 'fichier WAV à créer'); opts_reverse(p)
    p = sub.add_parser('toutes'); commun(p, 'dossier inexistant ou vide')
    opts_fade(p); opts_stutter(p); opts_reverse(p)
    a = ap.parse_args()

    if not 30 <= a.bpm <= 300:
        raise SystemExit('--bpm entre 30 et 300')
    if hasattr(a, 'mix') and not 0 <= a.mix <= 1:
        raise SystemExit('--mix entre 0 et 1')
    data, sr = charger(a.source)

    if a.geste != 'toutes':
        y, params = appliquer(a, data, sr)
        rapport = ecrire(a.source, a.sortie, data, sr, y, a.geste, params, a.format)
        Path(a.sortie).with_suffix('.json').write_text(json.dumps(rapport, indent=2, ensure_ascii=False))
        print(json.dumps(rapport, indent=2, ensure_ascii=False))
        return

    dossier = Path(a.sortie)
    if dossier.exists() and any(dossier.iterdir()):
        raise SystemExit(f'refus : {dossier} n\'est pas vide')
    nom = Path(a.source).stem
    if a.mode == 'swell' and not a.cible:
        a.mode = 'queue'  # sans cible, le swell n'a pas d'attaque à préparer
    rendus = []  # tout calculer avant d'écrire : une erreur ne laisse pas un dossier à moitié rempli
    for lettre, geste in (('A', 'fade'), ('B', 'stutter'), ('C', 'reverse')):
        a.geste = geste
        rendus.append((lettre, geste) + appliquer(a, data, sr))
    resultats = [ecrire(a.source, dossier / f'{nom} - {lettre} {geste}.wav', data, sr, y, geste,
                        params, a.format) for lettre, geste, y, params in rendus]
    rapport = {'source': str(Path(a.source).resolve()),
               'sha256_source': hashlib.sha256(Path(a.source).read_bytes()).hexdigest(),
               'bpm': a.bpm, 'variantes': resultats,
               'a_faire': 'Importer chaque variante sous la source (même départ), écouter dans la '
                          'phrase et avec le kick, à niveau comparable, en mono pour le grave ; '
                          'garder l\'original s\'il reste meilleur.'}
    (dossier / 'RAPPORT.json').write_text(json.dumps(rapport, indent=2, ensure_ascii=False))
    for r in resultats:
        print(f"{Path(r['sortie']).name} : crête {r['apres']['crete_dbfs']} dBFS, "
              f"RMS {r['apres']['rms_dbfs']} dBFS" + (f"  ⚠ {'; '.join(r['alertes'])}" if r['alertes'] else ''))
    print(f'Rapport : {dossier / "RAPPORT.json"}')


if __name__ == '__main__':
    main()
