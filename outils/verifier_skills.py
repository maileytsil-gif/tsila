#!/usr/bin/env python3
"""Contrôle des skills du dépôt, communs à Claude Code et Qwen Code.

  python3 outils/verifier_skills.py            # depuis la racine du dépôt (ou n'importe où : le dépôt est retrouvé)
  python3 outils/verifier_skills.py --liste    # skills, taille de leur description, modules

Cinq skills (`.claude/skills/<skill>/SKILL.md`), chacun avec ses modules (`<skill>/modules/<module>/GUIDE.md`,
anciens skills déplacés entiers : docs/regroupement-skills.md). Vérifie, sans rien modifier :
1. en-tête de chaque SKILL.md : `name` = nom du dossier (minuscules, chiffres, tirets), `description` non vide et
   d'au plus 1024 caractères (limite de la spécification Agent Skills ; Qwen Code valide aussi `name`) ;
2. modules : chaque dossier de `modules/` a un `GUIDE.md` qui commence par un titre H1 ; aucun `SKILL.md` ailleurs
   qu'à la racine d'un skill (il serait chargé comme un skill de plus) ; chaque module est cité dans le SKILL.md de
   son skill ;
3. chemins cités dans les .md des skills — segment entier entre accents graves (`../autre/…`, `../../SKILL.md`,
   `references/…`, `scripts/…`, `modules/…`), cible d'un lien Markdown, et, dans tout segment entre accents graves
   (commande avec arguments comprise : `python3 ../autre/scripts/x.py a.wav`), chaque jeton qui ressemble à un
   fichier du dépôt (`[../][skill/][modules/module/](scripts|references|assets|recipes)/….py|sh|md|json|png`,
   `../module/GUIDE.md`, `../../SKILL.md` ; jetons avec `*`, `<` ou `…` ignorés) : le fichier ou le dossier existe
   depuis le dossier du fichier, la racine du module, la racine du skill, `.claude/skills/` ou la racine du dépôt
   (commandes lancées depuis le dépôt : `corpus/scripts/…`) ;
   les fichiers racine `AGENTS.md`, `CLAUDE.md`, `QWEN.md` et `README.md` aussi, avec en plus les jetons
   `lom-bridge/…`, `outils/…`, `docs/…`, `.claude/skills/…`, `.qwen/…`, résolus depuis la racine du dépôt,
   `.claude/skills/`, `lom-bridge/` ou un skill ou un module nommé entre accents graves sur la même ligne ;
4. `.qwen/skills` est un lien vers `../.claude/skills` : Qwen Code lit exactement les skills de Claude Code ;
5. chaque skill et chaque module est cité dans la carte de `producteur-live`.
Code de sortie 1 si une erreur est trouvée.
"""
import argparse
import os
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SKILLS = RACINE / '.claude' / 'skills'
BRIDGE = RACINE / 'lom-bridge'
FICHIERS_RACINE = ('AGENTS.md', 'CLAUDE.md', 'QWEN.md', 'README.md')
CARTE = 'producteur-live'
NOM = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
MAX_DESCRIPTION = 1024

# Chemins relatifs cités : segment entier entre accents graves ou cible d'un lien Markdown.
CITE = re.compile(r'`((?:\.\./)+[^`\s]+|(?:references|scripts|assets|recipes|modules)/[^`\s]+)`'
                  r'|\]\(((?!https?:|mailto:|#)[^)\s]+)\)')
SEGMENT = re.compile(r'`([^`\n]+)`')
# Dans un segment entre accents graves, jeton qui ressemble à un fichier du dépôt (hors chemin absolu ou ~/…).
JETON = re.compile(r'(?<![\w./-])(?:(?:\.\./)*(?:[a-z0-9-]+/)?(?:modules/[a-z0-9-]+/)?(?:scripts|references|assets|recipes)/'
                   r'[^\s`*<>{}$|…]+\.(?:py|sh|md|json|png)\b'
                   r'|(?:\.\./)+[a-z0-9-]+/(?:modules/[a-z0-9-]+/)?(?:SKILL|GUIDE)\.md'
                   r'|(?:\.\./)+(?:SKILL|GUIDE)\.md'
                   r'|modules/[a-z0-9-]+/GUIDE\.md)')
# Fichiers racine : chemins du dépôt hors des skills.
JETON_RACINE = re.compile(r'(?<![\w./-])(?:lom-bridge|outils|docs|\.claude/skills|\.qwen)/[^\s`]+')
IGNORER = re.compile(r'[*<>{}$…|]|\.\.\.$')


def entete(texte):
    m = re.match(r'^---\n(.*?)\n---\n', texte, re.S)
    if not m:
        return None
    champs = {}
    for ligne in m.group(1).splitlines():
        cle, sep, val = ligne.partition(':')
        if sep and re.fullmatch(r'[A-Za-z_-]+', cle):
            champs[cle] = val.strip()
    return champs


def skills_et_modules():
    """{skill: [modules]} d'après les dossiers."""
    arbre = {}
    for dossier in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        modules = dossier / 'modules'
        arbre[dossier.name] = sorted(p.name for p in modules.iterdir() if p.is_dir()) if modules.is_dir() else []
    return arbre


def verifier_entetes(erreurs, arbre, liste=False):
    for skill, modules in arbre.items():
        dossier = SKILLS / skill
        fichier = dossier / 'SKILL.md'
        if not fichier.is_file():
            erreurs.append(f'{skill} : SKILL.md absent')
            continue
        champs = entete(fichier.read_text(encoding='utf-8'))
        if champs is None:
            erreurs.append(f'{skill}/SKILL.md : en-tête YAML (--- … ---) absent')
            continue
        nom, desc = champs.get('name', ''), champs.get('description', '')
        if nom != skill:
            erreurs.append(f'{skill}/SKILL.md : name « {nom} » ≠ nom du dossier')
        if not NOM.match(nom):
            erreurs.append(f'{skill}/SKILL.md : name « {nom} » hors [a-z0-9-]')
        if not desc:
            erreurs.append(f'{skill}/SKILL.md : description vide')
        elif len(desc) > MAX_DESCRIPTION:
            erreurs.append(f'{skill}/SKILL.md : description de {len(desc)} caractères (> {MAX_DESCRIPTION})')
        if liste:
            print(f'{skill:42s} {len(desc):5d}   modules : {", ".join(modules) or "—"}')


def verifier_modules(erreurs, arbre):
    for skill, modules in arbre.items():
        texte = (SKILLS / skill / 'SKILL.md').read_text(encoding='utf-8') if (SKILLS / skill / 'SKILL.md').is_file() else ''
        for module in modules:
            if not NOM.match(module):
                erreurs.append(f'{skill}/modules/{module} : nom hors [a-z0-9-]')
            guide = SKILLS / skill / 'modules' / module / 'GUIDE.md'
            if not guide.is_file():
                erreurs.append(f'{skill}/modules/{module} : GUIDE.md absent')
            elif not guide.read_text(encoding='utf-8').startswith('# '):
                erreurs.append(f'{skill}/modules/{module}/GUIDE.md : doit commencer par un titre H1')
            if not re.search(r'(?<![\w-])' + re.escape(module) + r'(?![\w-])', texte):
                erreurs.append(f'{skill}/SKILL.md : le module « {module} » n\'y est pas cité')
        for f in (SKILLS / skill).rglob('SKILL.md'):
            if f.parent != SKILLS / skill:
                erreurs.append(f'{f.relative_to(SKILLS)} : SKILL.md hors de la racine du skill (serait chargé comme un skill)')


def chemins_cites(ligne, racine=False):
    """Chemins relatifs cités sur une ligne : segments entiers, liens Markdown, jetons des segments avec arguments."""
    cibles = []
    for m in CITE.finditer(ligne):
        cible = (m.group(1) or m.group(2)).split('#')[0].rstrip('.,;:)')
        if m.group(2) and not re.search(r'\.(md|py|sh|json|png)$|/$', cible):
            continue  # lien Markdown vers autre chose qu'un fichier du dépôt
        cibles.append(cible)
    for segment in SEGMENT.findall(ligne):
        for mot in segment.split():
            if any(c in mot for c in '*<…'):
                continue  # motif ou emplacement à remplir, pas un fichier
            jetons = JETON.findall(mot) + (JETON_RACINE.findall(mot) if racine else [])
            cibles += [j.split('#')[0].rstrip('.,;:)') for j in jetons]
    return [c for c in dict.fromkeys(cibles) if c and not IGNORER.search(c) and ' ' not in c]


def dossier_nomme(nom):
    """Dossier d'un skill ou d'un module nommé entre accents graves dans un fichier racine."""
    if (SKILLS / nom).is_dir():
        return SKILLS / nom
    for d in SKILLS.glob(f'*/modules/{nom}'):
        return d
    return None


def bases_skill(f):
    """Dossier du fichier, racine du module s'il y en a une, racine du skill, .claude/skills/, racine du dépôt."""
    parts = f.relative_to(SKILLS).parts
    bases = [f.parent]
    if len(parts) > 3 and parts[1] == 'modules':
        bases.append(SKILLS / parts[0] / 'modules' / parts[2])
    return bases + [SKILLS / parts[0], SKILLS, RACINE]


def verifier_chemins(erreurs):
    fichiers = [(f, bases_skill(f), False) for f in sorted(SKILLS.rglob('*.md'))]
    fichiers += [(RACINE / nom, [RACINE, SKILLS, BRIDGE], True)
                 for nom in FICHIERS_RACINE if (RACINE / nom).is_file()]
    for fichier, bases, racine in fichiers:
        for n, ligne in enumerate(fichier.read_text(encoding='utf-8').splitlines(), 1):
            ici = bases
            if racine:  # « `drums-signature` (`references/signature.md`) » : relatif au skill ou module nommé sur la ligne
                ici = bases + [d for d in (dossier_nomme(s) for s in SEGMENT.findall(ligne) if NOM.match(s)) if d]
            for cible in chemins_cites(ligne, racine):
                if not any((b / cible).exists() for b in ici):
                    erreurs.append(f'{fichier.relative_to(RACINE)}:{n} : chemin introuvable « {cible} »')


def verifier_qwen(erreurs):
    lien = RACINE / '.qwen' / 'skills'
    if not lien.is_symlink():
        erreurs.append('.qwen/skills doit être un lien symbolique vers ../.claude/skills (ln -s ../.claude/skills .qwen/skills)')
    elif os.readlink(lien) != '../.claude/skills':
        erreurs.append(f'.qwen/skills pointe vers {os.readlink(lien)} au lieu de ../.claude/skills')
    elif lien.resolve() != SKILLS.resolve():
        erreurs.append('.qwen/skills ne se résout pas vers .claude/skills')


def verifier_carte(erreurs, arbre):
    carte = SKILLS / CARTE / 'SKILL.md'
    if not carte.is_file():
        erreurs.append(f'{CARTE}/SKILL.md absent : la carte « situation → skill › module » est attendue là')
        return
    texte = carte.read_text(encoding='utf-8')
    for nom in [s for s in arbre if s != CARTE] + [m for ms in arbre.values() for m in ms]:
        if not re.search(r'(?<![\w-])' + re.escape(nom) + r'(?![\w-])', texte):
            erreurs.append(f'{CARTE}/SKILL.md : « {nom} » n\'apparaît pas dans la carte')


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--liste', action='store_true', help='afficher chaque skill, la taille de sa description et ses modules')
    a = p.parse_args()
    erreurs = []
    arbre = skills_et_modules()
    verifier_entetes(erreurs, arbre, a.liste)
    verifier_modules(erreurs, arbre)
    verifier_chemins(erreurs)
    verifier_qwen(erreurs)
    verifier_carte(erreurs, arbre)
    for e in erreurs:
        print('ERREUR', e)
    print(f'{len(arbre)} skills, {sum(len(m) for m in arbre.values())} modules, {len(erreurs)} erreur(s)')
    return 1 if erreurs else 0


if __name__ == '__main__':
    sys.exit(main())
