#!/usr/bin/env python3
"""Usage: tableau.py [--projet <slug>] [--memoire <dossier>]
Tableau de bord de tous les morceaux : état, dernière activité, étape en cours, questions en attente, Set sur le disque.
Lit les fichiers projet-*.md de la mémoire (aucune écriture, aucun accès à Live)."""
import sys, os, re, glob, datetime

if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
    print(__doc__); raise SystemExit(0)
def opt(k, d):
    return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d

MEM = opt('--memoire', os.path.expanduser('~/.claude/projects/-Volumes-NO-NAME-caude/memory'))
SETS = os.path.expanduser('/Volumes/Seagate Portable Drive/abl proj/1 Project')
seul = opt('--projet', None)

PHASES = ['cadre', 'instruments', 'groove', 'arrangement', 'mix', 'automation', 'voix', 'export', 'mastering']
# Expressions -> phase atteinte. Estimation d'après le vocabulaire des entrées récentes : à confirmer,
# jamais à annoncer comme un fait (« bus master » n'est pas du mastering, un « drop » n'est pas l'arrangement).
INDICES = [
    (8, r'master(?:is|é|iser|ing)\b|LUFS|true ?peak|dBTP|L2 \b|limiteur d.export'),
    (7, r'\bexport\b|\bbounc|\bWAV\b|rendu final'),
    (6, r'\bvoix\b|\bSuno\b|\bvocal|paroles'),
    (5, r'automation|\bsweep\b|fondu automatisé|marches post'),
    (4, r'\bmix\b|sidechain|\bEQ\b|balance|glue|coupe-bas|soothe|Pro-Q|REQ 6|gain staging'),
    (3, r'arrangement|structure|marqueur|repère|\bsection\b|\bbreak\b|\bpont\b|\bdrop \d'),
    (2, r'\bhook\b|mélodie|melodie|\bbasse\b|batterie|groove|\bclip\b|\bnotes?\b'),
    (1, r'\bpiste\b|preset|Serum|instrument|Drum Rack'),
]

def lire(path):
    t = open(path, encoding='utf-8', errors='ignore').read()
    d = {'fichier': os.path.basename(path), 'slug': re.sub(r'^projet-|\.md$', '', os.path.basename(path))}
    m = re.search(r'^description: *"?(.*?)"?$', t, re.M)
    d['description'] = (m.group(1) if m else '')[:300]
    d['entrees'] = re.findall(r'^- (.+)$', t, re.M)
    m = re.search(r'^\*\*REPRISE\*\*(.*)$', t, re.M)
    d['reprise'] = bool(m)
    qs = re.findall(r'^[^\n]*(?:question posée|en attente de décision|à trancher|sans réponse|à décider)[^\n]*$', t, re.M | re.I)
    d['questions'] = [re.sub(r'^[-*\s]+', '', q).strip()[:170] for q in qs][:4]
    # tempo / tonalité
    idx = ''
    ip = os.path.join(os.path.dirname(path), 'MEMORY.md')
    if os.path.exists(ip):
        for ligne in open(ip, encoding='utf-8', errors='ignore'):
            if d['fichier'] in ligne: idx = ligne; break
    d['index'] = idx.strip()[:200]
    m = re.search(r'(\d{2,3})\s*BPM', t, re.I); d['bpm'] = m.group(1) if m else '?'
    m = re.search(r'\b(?:en |, )?((?:[A-G]b?#?|do|ré|re|mi|fa|sol|la|si)\s*(?:mineur|majeur))', t, re.I)
    d['tonalite'] = m.group(1) if m else '?'
    m = re.search(r'(\d{1,4})\s*mesures', d['description'] + ' ' + idx)   # description puis index font foi
    if not m:
        c = [x for x in re.findall(r'(\d{1,4})\s*mesures', t[:2000]) if 8 <= int(x) <= 400]
        m = c[0] if c else None
        d['mesures'] = m if m else '?'
    else:
        d['mesures'] = m.group(1)
    # phase atteinte : le mot le plus avancé dans les 8 entrées les plus récentes (journal en tête)
    txt = re.sub(r'bus master|BUS MASTER', ' ', ' '.join(d['entrees'][:8]), flags=re.I)
    d['phase'] = max((n for n, pat in INDICES if re.search(pat, txt, re.I)), default=0)
    d['pause'] = bool(re.search(r'en pause|suspendu|mis de côté', d['description'] + ' ' + idx, re.I))
    d['maj'] = datetime.date.fromtimestamp(os.path.getmtime(path))
    return d

def sets_du_projet(slug):
    pats = {slug, slug.replace('-', ' '), slug.replace('-', '')}
    out = []
    for f in glob.glob(os.path.join(SETS, '*.als')):
        b = os.path.basename(f).lower()
        if any(p.lower() in b for p in pats):
            out.append((datetime.date.fromtimestamp(os.path.getmtime(f)), os.path.basename(f)))
    return sorted(out, reverse=True)[:2]

fichiers = sorted(glob.glob(os.path.join(MEM, 'projet-*.md')))
if seul:
    fichiers = [f for f in fichiers if seul in os.path.basename(f)]
    if not fichiers: raise SystemExit('aucun projet nommé « %s » dans %s' % (seul, MEM))
if not fichiers: raise SystemExit('aucun fichier projet-*.md dans ' + MEM)

projets = [lire(f) for f in fichiers]
auj = datetime.date.today()
projets.sort(key=lambda p: p['maj'], reverse=True)

print('TABLEAU DE BORD — %d morceaux — %s\n' % (len(projets), auj.isoformat()))
print('%-26s %-7s %-12s %-7s %-22s %s' % ('morceau', 'BPM', 'tonalité', 'mes.', 'phase atteinte', 'dernière note'))
print('-' * 100)
for p in projets:
    age = (auj - p['maj']).days
    etat = 'EN PAUSE' if p['pause'] else ('actif' if age <= 3 else 'dormant %d j' % age)
    print('%-26s %-7s %-12s %-7s %-22s %s (%s)' % (
        p['slug'][:26], p['bpm'], p['tonalite'][:12], p['mesures'],
        '%d/8 %s' % (p['phase'], PHASES[p['phase']]), p['maj'].isoformat(), etat))
    dernier = max(p2['maj'] for p2 in projets)

for p in projets:
    print('\n=== %s' % p['slug'])
    print('  description : %s' % (p['description'][:200] or '—'))
    if p.get('index'): print('  index mémoire : %s' % p['index'])
    print('  journal : %d entrées ; en-tête REPRISE : %s' % (len(p['entrees']), 'oui' if p['reprise'] else 'ABSENT — à écrire en fin de session'))
    if p['entrees']:
        print('  dernière entrée : %s' % p['entrees'][0][:180])
    if p['questions']:
        print('  À TRANCHER :')
        for q in p['questions']: print('    - %s' % q)
    s = sets_du_projet(p['slug'])
    print('  Set : %s' % (', '.join('%s (%s)' % (n, d.isoformat()) for d, n in s) if s else 'aucun .als trouvé sous /Volumes/Seagate Portable Drive/abl proj/1 Project'))

print('\nPhase = estimation d\'après le vocabulaire du journal, à confirmer en relisant le Set.')
print('Rappels : une étape par échange, plan complet annoncé d\'abord ; relire l\'état réel dans Live avant d\'agir ;')
print('journal et en-tête REPRISE mis à jour après chaque étape validée (skill memoire-projet).')
