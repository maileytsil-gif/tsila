#!/usr/bin/env python3
"""Regroupement des 44 skills en 5 skills par métier (exécuté une fois, le 8 oct. 2026).

  python3 outils/regrouper_skills.py          # sur un dépôt propre ; `git reset --hard` pour revenir en arrière

Gardé dans le dépôt pour documenter la correspondance ancien skill → skill › module et les règles de
réécriture des renvois (voir docs/regroupement-skills.md). Ce qu'il fait, dans l'ordre :
1. supprime les copies jumelles et le fichier portable du skill A à Z (les originaux restent dans leurs modules) ;
2. déplace le storyboard du clip « Après les heures » dans docs/projets/ ;
3. `git mv` : le skill de base de chaque groupe devient le skill regroupé (ableton-live-session → producteur-live),
   chaque autre skill devient `<skill>/modules/<ancien>/` ;
4. `SKILL.md` d'un module → `GUIDE.md` : en-tête YAML retiré, description gardée en citation sous le titre ;
5. réécrit les renvois dans les skills et dans les fichiers du dépôt qui citent un chemin de skill :
   `../x/…` (relatif au dossier du fichier ou, par convention, à la racine du skill), `x/references/…`
   (relatif à .claude/skills/), `.claude/skills/x/…` ; `SKILL.md` d'un module → `GUIDE.md` ;
6. recalcule le MANIFEST.json d'electronic-production-engineer.
Les textes (routeurs, descriptions, README, AGENTS, vérificateur, installateur, tests, CI) se corrigent ensuite à la main.
"""
import hashlib
import json
import pathlib
import posixpath
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SKILLS = RACINE / '.claude' / 'skills'

# skill regroupé : (skill de base, dont le SKILL.md devient celui du groupe, [modules])
GROUPES = {
    'compositeur-arrangeur': ('compositeur-arrangeur', [
        'melodie-composition', 'composer-hooks-funk-electro', 'arrangement-avance', 'midi-expressif',
        'composer-trajectoire-emotionnelle', 'theorie-musicale-electronique', 'theorie-musicale-composition',
        'partition-recherche', 'partition-telechargement', 'sampling-composition-avancee']),
    'producteur-rythmique': ('producteur-rythmique', [
        'drums-signature', 'kick-bass-equilibre', 'construire-low-end-electronique',
        'native-instruments-control', 'produire-avec-maschine-mk3']),
    'sound-designer-serum': ('sound-designer-serum', [
        'vst-sound-design', 'serum-2-basses-house-future-house', 'bass-house-sound-design',
        'studio-grade-brass-sound-design', 'studio-grade-funk-keys-synth-sound-design',
        'synthese-reference', 'resampling']),
    'ingenieur-mixage': ('ingenieur-mixage', [
        'mixage', 'effets-plugins', 'mixer-house-professionnel', 'live-mix-mastering',
        'mastering-outils', 'live-export-wav']),
    'producteur-live': ('ableton-live-session', [
        'memoire-projet', 'memoire-persistante', 'chef-de-projet', 'piloter-live-lombridge-codex',
        'produire-demo-electro-rapide', 'produire-morceau-electronique-de-a-a-z', 'maitriser-suno',
        'suno-vocals', 'house-future-rave-bass-house-production', 'electronic-production-engineer',
        'live-automation']),
}
OU = {}  # ancien skill → (skill regroupé, est la base du groupe)
for groupe, (base, modules) in GROUPES.items():
    OU[base] = (groupe, True)
    for module in modules:
        OU[module] = (groupe, False)

AZ = 'produire-morceau-electronique-de-a-a-z'
A_SUPPRIMER = [
    *[f'{AZ}/references/bass-house-{n}.md' for n in ('recettes', 'stabs-serum2', 'wavetable', 'spectral-live', 'sources-et-videos')],
    *[f'{AZ}/references/mixage-{n}.md' for n in ('diagnostic-et-recettes', 'genres-et-espace', 'mastering-streaming-et-club',
                                               'sources-cours-videos', 'track-reference-avec-outils', 'videos-analysees')],
    *[f'{AZ}/references/theorie-{n}.md' for n in ('analyse-harmonie-groove-arrangement', 'analyse-producteur-pop-rnb',
                                                'exemples-et-verification', 'styles-et-instruments')],
    f'{AZ}/references/clip-manga-weekend.md', f'{AZ}/scripts/session_review.py',
    f'{AZ}/references/Bass_House_skill_portable_ChatGPT_Claude_Qwen.md',
]
STORYBOARD = 'piloter-live-lombridge-codex/assets/storyboard-manga-weekend.png'
EXTENSIONS = {'.md', '.py', '.sh', '.json', '.yml', '.yaml', '.txt', '.csv'}
NOMS_SANS_EXT = {'Modelfile'}
FICHIERS_DEPOT = ['README.md', 'AGENTS.md', 'CLAUDE.md', 'QWEN.md', 'docs/claude-code-avec-ollama.md',
                  'docs/claude-ollama.sh', 'corpus/INDEX.md', 'corpus/README.md', 'corpus/index.json',
                  '.github/workflows/skills.yml']

NOMS = '|'.join(sorted(OU, key=len, reverse=True))
# `../x/…`, éventuellement suivi de SKILL.md ; plusieurs `../` possibles.
MOTIF_RELATIF = re.compile(r'(?<![\w./-])((?:\.\./)+)(' + NOMS + r')/(SKILL\.md)?')
# `x/references/…`, relatif à .claude/skills/ (fichiers de skills et fichiers racine).
MOTIF_SKILLS = re.compile(r'(?<![\w./-])(' + NOMS + r')/(references|scripts|assets|recipes|SKILL\.md)')
# `.claude/skills/x` ou `.qwen/skills/x`.
MOTIF_INSTALLE = re.compile(r'((?:\.claude|\.qwen)/skills/)(' + NOMS + r')(?![\w-])')


def git(*args):
    subprocess.run(['git', *args], cwd=RACINE, check=True)


def nouvelle_racine(ancien):
    """Racine du skill ou du module dans la nouvelle arborescence, relative à .claude/skills/."""
    groupe, base = OU[ancien]
    return groupe if base else f'{groupe}/modules/{ancien}'


def entree(ancien):
    return 'SKILL.md' if OU[ancien][1] else 'GUIDE.md'


def contexte(fichier):
    """(racine du skill ou du module, dossier du fichier, profondeur dans l'ancien skill), relatifs à .claude/skills/."""
    rel = fichier.relative_to(SKILLS).as_posix()
    parts = rel.split('/')
    racine = '/'.join(parts[:3]) if len(parts) > 2 and parts[1] == 'modules' else parts[0]
    dossier = posixpath.dirname(rel)
    profondeur = len(parts) - len(racine.split('/')) - 1
    return racine, dossier, profondeur


def reecrire(texte, racine=None, dossier=None, profondeur=None):
    compte = [0, 0, 0]

    def relatif(m):
        dots, x, skill = m.group(1), m.group(2), m.group(3)
        n = dots.count('../')
        origine = dossier if n == profondeur + 1 else racine
        rel = posixpath.relpath(nouvelle_racine(x), origine)
        prefixe = '' if rel == '.' else rel + '/'
        compte[0] += 1
        return prefixe + (entree(x) if skill else '')

    def skills(m):
        x, suite = m.group(1), m.group(2)
        compte[1] += 1
        return f'{nouvelle_racine(x)}/{entree(x) if suite == "SKILL.md" else suite}'

    def installe(m):
        compte[2] += 1
        return m.group(1) + nouvelle_racine(m.group(2))

    if racine is not None:
        texte = MOTIF_RELATIF.sub(relatif, texte)
    texte = MOTIF_SKILLS.sub(skills, texte)
    texte = MOTIF_INSTALLE.sub(installe, texte)
    return texte, compte


def est_texte(f):
    return f.is_file() and (f.suffix in EXTENSIONS or f.name in NOMS_SANS_EXT)


def guide(fichier, groupe):
    """SKILL.md d'un module → GUIDE.md : en-tête YAML retiré, description gardée en citation sous le titre."""
    texte = fichier.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n+', texte, re.S)
    if not m:
        sys.exit(f'{fichier} : en-tête YAML absent')
    description = ''
    for ligne in m.group(1).splitlines():
        cle, sep, val = ligne.partition(':')
        if cle == 'description' and sep:
            description = val.strip()
    corps = texte[m.end():]
    if not corps.startswith('# '):
        sys.exit(f'{fichier} : le corps ne commence pas par un titre H1')
    titre, _, reste = corps.partition('\n')
    nouveau = f'{titre}\n\n> Module du skill `{groupe}`. {description}\n{reste}'
    cible = fichier.with_name('GUIDE.md')
    git('mv', str(fichier.relative_to(RACINE)), str(cible.relative_to(RACINE)))
    cible.write_text(nouveau, encoding='utf-8')


def manifest_epe():
    f = SKILLS / 'producteur-live' / 'modules' / 'electronic-production-engineer' / 'MANIFEST.json'
    m = json.loads(f.read_text(encoding='utf-8'))
    for entree_ in m['files']:
        if entree_['path'] == 'SKILL.md':
            entree_['path'] = 'GUIDE.md'
        p = f.parent / entree_['path']
        octets = p.read_bytes()
        entree_['sha256'] = hashlib.sha256(octets).hexdigest()
        entree_['bytes'] = len(octets)
    f.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    if subprocess.run(['git', 'status', '--porcelain'], cwd=RACINE, capture_output=True, text=True).stdout.strip():
        sys.exit('dépôt non propre : commiter ou remiser avant de lancer le regroupement')
    anciens = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    if sorted(OU) != anciens:
        sys.exit(f'skills du dépôt ≠ table : manquants {sorted(set(OU) - set(anciens))}, en trop {sorted(set(anciens) - set(OU))}')
    for d in SKILLS.rglob('__pycache__'):
        subprocess.run(['rm', '-rf', str(d)], check=True)

    # 1. copies jumelles et portable
    for rel in A_SUPPRIMER:
        git('rm', '-q', f'.claude/skills/{rel}')
    # 2. storyboard
    (RACINE / 'docs' / 'projets').mkdir(exist_ok=True)
    git('mv', f'.claude/skills/{STORYBOARD}', f'docs/projets/{posixpath.basename(STORYBOARD)}')
    # 3. déplacements
    deplaces = 0
    for groupe, (base, modules) in GROUPES.items():
        if base != groupe:
            git('mv', f'.claude/skills/{base}', f'.claude/skills/{groupe}')
            deplaces += 1
        (SKILLS / groupe / 'modules').mkdir()
        for module in modules:
            git('mv', f'.claude/skills/{module}', f'.claude/skills/{groupe}/modules/{module}')
            deplaces += 1
    # 4. GUIDE.md
    for groupe, (base, modules) in GROUPES.items():
        for module in modules:
            guide(SKILLS / groupe / 'modules' / module / 'SKILL.md', groupe)
    # 5. renvois
    total = [0, 0, 0]
    touches = 0
    for f in sorted(SKILLS.rglob('*')):
        if not est_texte(f):
            continue
        texte = f.read_text(encoding='utf-8')
        nouveau, compte = reecrire(texte, *contexte(f))
        if nouveau != texte:
            f.write_text(nouveau, encoding='utf-8')
            touches += 1
            total = [a + b for a, b in zip(total, compte)]
    for rel in FICHIERS_DEPOT:
        f = RACINE / rel
        if not f.is_file():
            continue
        texte = f.read_text(encoding='utf-8')
        nouveau, compte = reecrire(texte)
        if nouveau != texte:
            f.write_text(nouveau, encoding='utf-8')
            touches += 1
            total = [a + b for a, b in zip(total, compte)]
    # 6. MANIFEST
    manifest_epe()
    print(f'{deplaces} dossiers déplacés, {len(A_SUPPRIMER)} fichiers supprimés, {touches} fichiers réécrits : '
          f'{total[0]} renvois ../x/, {total[1]} renvois x/references, {total[2]} chemins .claude/skills/x')


if __name__ == '__main__':
    main()
