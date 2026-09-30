#!/usr/bin/env python3
"""Contrôle des skills du dépôt, communs à Claude Code et Qwen Code.

  python3 outils/verifier_skills.py            # depuis la racine du dépôt (ou n'importe où : le dépôt est retrouvé)
  python3 outils/verifier_skills.py --liste    # nom et taille de la description de chaque skill

Vérifie, sans rien modifier :
1. en-tête de chaque SKILL.md : `name` = nom du dossier (minuscules, chiffres, tirets), `description` non vide et
   d'au plus 1024 caractères (limite de la spécification Agent Skills ; Qwen Code valide aussi `name`) ;
2. chemins cités dans les .md des skills — segment entier entre accents graves (`../autre-skill/…`,
   `references/…`, `scripts/…`), cible d'un lien Markdown, et, dans tout segment entre accents graves (commande
   avec arguments comprise : `python3 ../autre-skill/scripts/x.py a.wav`), chaque jeton qui ressemble à un fichier
   du dépôt (`[../][skill/](scripts|references|assets)/….py|sh|md|json|png`, `../skill/SKILL.md` ; jetons avec
   `*`, `<` ou `…` ignorés) : le fichier ou le dossier existe depuis le dossier du fichier, la racine du skill
   ou `.claude/skills/` ;
   les fichiers racine `AGENTS.md`, `CLAUDE.md`, `QWEN.md` et `README.md` aussi, avec en plus les jetons
   `lom-bridge/…`, `outils/…`, `.claude/skills/…`, `.qwen/…`, résolus depuis la racine du dépôt,
   `.claude/skills/`, `lom-bridge/` ou un skill nommé entre accents graves sur la même ligne ;
3. copies jumelles : les fichiers dupliqués volontairement entre deux skills (skill autonome et corpus du skill
   A à Z) restent identiques octet pour octet — corriger les deux ensemble ;
4. copie portable : chaque ligne non vide des cinq références de `bass-house-sound-design` figure telle quelle
   dans `Bass_House_skill_portable_ChatGPT_Claude_Qwen.md` du skill A à Z, qui les concatène ;
5. `.qwen/skills` est un lien vers `../.claude/skills` : Qwen Code lit exactement les skills de Claude Code ;
6. chaque skill est cité dans la carte d'`ableton-live-session`, dont la description annonce le bon nombre de skills.
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
CARTE = 'ableton-live-session'
NOM = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
MAX_DESCRIPTION = 1024

AZ = 'produire-morceau-electronique-de-a-a-z'
BASS_HOUSE = ('recettes', 'stabs-serum2', 'wavetable', 'spectral-live', 'sources-et-videos')
# (fichier du skill autonome, copie dans le corpus du skill A à Z) : même contenu attendu.
JUMEAUX = [
    *[(f'bass-house-sound-design/references/{n}.md', f'{AZ}/references/bass-house-{n}.md') for n in BASS_HOUSE],
    *[(f'mixer-house-professionnel/references/{n}.md', f'{AZ}/references/mixage-{n}.md')
      for n in ('diagnostic-et-recettes', 'genres-et-espace', 'mastering-streaming-et-club',
                'sources-cours-videos', 'track-reference-avec-outils', 'videos-analysees')],
    *[(f'theorie-musicale-composition/references/{n}.md', f'{AZ}/references/theorie-{n}.md')
      for n in ('analyse-harmonie-groove-arrangement', 'analyse-producteur-pop-rnb',
                'exemples-et-verification', 'styles-et-instruments')],
    ('piloter-live-lombridge-codex/references/clip-manga-weekend.md', f'{AZ}/references/clip-manga-weekend.md'),
    ('piloter-live-lombridge-codex/scripts/session_review.py', f'{AZ}/scripts/session_review.py'),
]
# Copie portable : un en-tête suivi des cinq références Bass House concaténées.
PORTABLE = f'{AZ}/references/Bass_House_skill_portable_ChatGPT_Claude_Qwen.md'
PORTABLE_SOURCES = [f'bass-house-sound-design/references/{n}.md' for n in BASS_HOUSE]

# Chemins relatifs cités : segment entier entre accents graves ou cible d'un lien Markdown.
CITE = re.compile(r'`((?:\.\./)+[^`\s]+|(?:references|scripts|assets)/[^`\s]+)`|\]\(((?!https?:|mailto:|#)[^)\s]+)\)')
SEGMENT = re.compile(r'`([^`\n]+)`')
# Dans un segment entre accents graves, jeton qui ressemble à un fichier du dépôt (hors chemin absolu ou ~/…).
JETON = re.compile(r'(?<![\w./-])(?:(?:\.\./)*(?:[a-z0-9-]+/)?(?:scripts|references|assets)/[^\s`*<>{}$|…]+'
                   r'\.(?:py|sh|md|json|png)\b|(?:\.\./)+[a-z0-9-]+/SKILL\.md)')
# Fichiers racine : chemins du dépôt hors des skills.
JETON_RACINE = re.compile(r'(?<![\w./-])(?:lom-bridge|outils|\.claude/skills|\.qwen)/[^\s`]+')
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


def verifier_entetes(erreurs, liste=False):
    noms = []
    for dossier in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        fichier = dossier / 'SKILL.md'
        if not fichier.is_file():
            erreurs.append(f'{dossier.name} : SKILL.md absent')
            continue
        champs = entete(fichier.read_text(encoding='utf-8'))
        if champs is None:
            erreurs.append(f'{dossier.name}/SKILL.md : en-tête YAML (--- … ---) absent')
            continue
        nom, desc = champs.get('name', ''), champs.get('description', '')
        if nom != dossier.name:
            erreurs.append(f'{dossier.name}/SKILL.md : name « {nom} » ≠ nom du dossier')
        if not NOM.match(nom):
            erreurs.append(f'{dossier.name}/SKILL.md : name « {nom} » hors [a-z0-9-]')
        if not desc:
            erreurs.append(f'{dossier.name}/SKILL.md : description vide')
        elif len(desc) > MAX_DESCRIPTION:
            erreurs.append(f'{dossier.name}/SKILL.md : description de {len(desc)} caractères (> {MAX_DESCRIPTION})')
        if liste:
            print(f'{dossier.name:42s} {len(desc):5d}')
        noms.append(dossier.name)
    return noms


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


def verifier_chemins(erreurs):
    fichiers = [(f, [f.parent, SKILLS / f.relative_to(SKILLS).parts[0], SKILLS], False)
                for f in sorted(SKILLS.rglob('*.md'))]
    fichiers += [(RACINE / nom, [RACINE, SKILLS, BRIDGE], True)
                 for nom in FICHIERS_RACINE if (RACINE / nom).is_file()]
    for fichier, bases, racine in fichiers:
        for n, ligne in enumerate(fichier.read_text(encoding='utf-8').splitlines(), 1):
            ici = bases
            if racine:  # « `drums-signature` (`references/signature.md`) » : relatif au skill nommé sur la ligne
                ici = bases + [SKILLS / s for s in SEGMENT.findall(ligne) if NOM.match(s) and (SKILLS / s).is_dir()]
            for cible in chemins_cites(ligne, racine):
                if not any((b / cible).exists() for b in ici):
                    erreurs.append(f'{fichier.relative_to(RACINE)}:{n} : chemin introuvable « {cible} »')


def verifier_jumeaux(erreurs):
    for a, b in JUMEAUX:
        pa, pb = SKILLS / a, SKILLS / b
        manquants = [str(p.relative_to(RACINE)) for p in (pa, pb) if not p.is_file()]
        if manquants:
            erreurs.append('jumeaux : fichier absent ' + ', '.join(manquants))
        elif pa.read_bytes() != pb.read_bytes():
            erreurs.append(f'jumeaux différents : .claude/skills/{a} ≠ .claude/skills/{b} (reporter la correction dans les deux)')


def verifier_portable(erreurs):
    portable = SKILLS / PORTABLE
    sources = [SKILLS / s for s in PORTABLE_SOURCES]
    manquants = [str(p.relative_to(RACINE)) for p in (portable, *sources) if not p.is_file()]
    if manquants:
        erreurs.append('portable : fichier absent ' + ', '.join(manquants))
        return
    lignes = set(portable.read_text(encoding='utf-8').splitlines())
    for source in sources:
        for n, ligne in enumerate(source.read_text(encoding='utf-8').splitlines(), 1):
            if ligne.strip() and ligne not in lignes:
                erreurs.append(f'portable désynchronisé : {source.relative_to(RACINE)} ligne {n} '
                               f'(absente de {portable.name} : reporter la correction)')


def verifier_qwen(erreurs):
    lien = RACINE / '.qwen' / 'skills'
    if not lien.is_symlink():
        erreurs.append('.qwen/skills doit être un lien symbolique vers ../.claude/skills (ln -s ../.claude/skills .qwen/skills)')
    elif os.readlink(lien) != '../.claude/skills':
        erreurs.append(f'.qwen/skills pointe vers {os.readlink(lien)} au lieu de ../.claude/skills')
    elif lien.resolve() != SKILLS.resolve():
        erreurs.append('.qwen/skills ne se résout pas vers .claude/skills')


def verifier_carte(erreurs, noms):
    carte = SKILLS / CARTE / 'SKILL.md'
    if not carte.is_file():
        return
    texte = carte.read_text(encoding='utf-8')
    for nom in noms:
        if nom != CARTE and not re.search(r'(?<![\w-])' + re.escape(nom) + r'(?![\w-])', texte):
            erreurs.append(f'{CARTE}/SKILL.md : le skill « {nom} » n\'apparaît pas dans la carte')
    m = re.search(r'vers les (\d+) autres skills', entete(texte).get('description', ''))
    if m and int(m.group(1)) != len(noms) - 1:
        erreurs.append(f'{CARTE}/SKILL.md : la description annonce {m.group(1)} autres skills, il y en a {len(noms) - 1}')


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--liste', action='store_true', help='afficher nom et taille de la description de chaque skill')
    a = p.parse_args()
    erreurs = []
    noms = verifier_entetes(erreurs, a.liste)
    verifier_chemins(erreurs)
    verifier_jumeaux(erreurs)
    verifier_portable(erreurs)
    verifier_qwen(erreurs)
    verifier_carte(erreurs, noms)
    for e in erreurs:
        print('ERREUR', e)
    print(f'{len(noms)} skills, {len(JUMEAUX)} paires jumelles, {len(erreurs)} erreur(s)')
    return 1 if erreurs else 0


if __name__ == '__main__':
    sys.exit(main())
