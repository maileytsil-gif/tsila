#!/usr/bin/env python3
"""qwen-musique — donne le skill composer-hooks-funk-electro à un modèle local servi par Ollama.

Ollama ne découvre pas les skills : ce lanceur envoie GUIDE.md (l'entrée du module) et les références les plus pertinentes
(d'après les mots de la demande) en message système, par l'API HTTP d'Ollama avec une fenêtre de contexte
explicite (`num_ctx`). `ollama run` tronque en silence tout ce qui dépasse sa fenêtre par défaut : les
instructions du skill, placées en tête, étaient les premières perdues.

  qwen-musique --model qwen3:14b "Crée un thème électro chill sur Dm9–G13–Cmaj9–A7alt avec MIDI et patch Serum 2"
  qwen-musique --model qwen3:14b --ref kick-808-detail.md "deux kicks 808"
  qwen-musique --dry-run "hook funk house et vocoder"      # références choisies et taille, sans appeler Ollama
  echo "demande" | qwen-musique --model qwen3:14b

Le modèle n'a ni web, ni contrôle d'Ableton, ni accès aux autres skills : il livre des grilles et des réglages
que l'utilisateur (ou un agent passant par lom-bridge/agent_gateway.py) applique puis vérifie.
"""
import argparse
import json
import os
import pathlib
import sys
import unicodedata
import urllib.error
import urllib.request

NOM = 'composer-hooks-funk-electro'
# référence -> mots de la demande qui la rendent utile (comparés sans accents ni majuscules)
MOTS = {
    'atelier-themes.md': ('theme', 'accord', 'melodie', 'hook', 'motif', 'riff', 'grille', 'midi', 'harmon'),
    'phrases-par-instrument.md': ('phras', 'funk', 'rhodes', 'guitare', 'cuivre', 'clav', 'trompette', 'sax',
                                  'afro', 'tech house', 'bass house', 'electro house', 'orchestr', 'instrument'),
    'cinquante-cinq-recettes.md': ('serum', 'recette', 'preset', 'patch', 'sound design', 'pad', 'pluck',
                                   'lead', 'drone', 'riser', 'impact', 'ambiance', 'stab'),
    'palette-production.md': ('macro', 'palette', 'serum', 'kick', 'percussion', 'snare', 'clap', 'hat'),
    'kick-808-detail.md': ('kick', '808'),
    'sound-design.md': ('basse', 'bass', 'sub', 'reese', 'growl', 'legato', 'glide', 'bpm'),
    'chill-electro-jazz.md': ('chill', 'downtempo', 'jazz chill', 'lounge'),
    'electro-rnb-2021-2026.md': ('r&b', 'rnb', 'tinashe', 'kelela', 'sza', 'weeknd', 'beyonce', 'twigs'),
    'microhouse-complet.md': ('microhouse', 'micro house', 'glitch', 'minimal'),
    'sampling-arrangement.md': ('sampl', 'chop', 'break', 'pont', 'arrangement', 'resampl'),
    'effets-groupes-vocoder.md': ('vocoder', 'chorus', 'flanger', 'phaser', 'effet', 'sweep', 'transition', 'bus'),
    'sources-videos.md': ('source', 'video', 'youtube', 'tuto'),
    'producteurs-exemples.md': ('producteur', 'artiste', 'rihanna', 'guetta', 'odd mob', 'black coffee'),
}
DEFAUT = ['atelier-themes.md', 'palette-production.md']
SYSTEME = ("Réponds en français. Applique le skill ci-dessous à la demande de l'utilisateur. "
           "Numérotation Ableton : C3 = 60 ; donne aussi le numéro MIDI de chaque note. "
           "Tu n'as ni web, ni contrôle d'Ableton, ni accès aux autres skills cités par des chemins « ../ » : "
           "applique les règles résumées dans le skill et livre des grilles et réglages à vérifier. "
           "Signale les limites de contexte et toute source non vérifiée. "
           "Ne prétends jamais avoir entendu un son ou regardé une vidéo.")


def sans_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.casefold()) if unicodedata.category(c) != 'Mn')


def trouver_skill(explicite=None):
    ici = pathlib.Path(__file__).resolve().parent.parent  # scripts/ -> dossier du skill (suit les liens symboliques)
    candidats = [explicite, os.environ.get('QWEN_MUSIQUE_SKILL'), ici,
                 pathlib.Path.home() / '.claude/skills/compositeur-arrangeur/modules' / NOM,
                 pathlib.Path.home() / '.codex/skills/compositeur-arrangeur/modules' / NOM]
    for c in candidats:
        if c and (pathlib.Path(c).expanduser() / 'GUIDE.md').is_file():
            return pathlib.Path(c).expanduser()
    return None


def choisir(question, forcees=(), maximum=4):
    """Références classées par nombre de mots trouvés dans la demande ; les forcées d'abord."""
    q = sans_accents(question)
    score = {nom: sum(sans_accents(m) in q for m in mots) for nom, mots in MOTS.items()}
    classees = [n for n in sorted(MOTS, key=lambda n: -score[n]) if score[n] > 0]
    choix = list(dict.fromkeys(list(forcees) + classees))
    return (choix or DEFAUT)[:max(maximum, len(forcees))]


def jetons(texte):
    return len(texte) // 3 + 1  # estimation prudente pour du français balisé (≈ 3 caractères par jeton)


def construire(racine, question, refs, num_ctx, reserve):
    """Message système avec GUIDE.md puis les références ; retire les dernières si la fenêtre déborde."""
    skill = (racine / 'GUIDE.md').read_text(encoding='utf-8')
    budget = num_ctx - reserve - jetons(SYSTEME) - jetons(question)
    gardees, ecartees, sections = [], [], []
    total = jetons(skill)
    for nom in refs:
        f = racine / 'references' / nom
        if not f.is_file():
            ecartees.append(f'{nom} (absent)')
            continue
        texte = f'\n\n# Référence : {nom}\n\n' + f.read_text(encoding='utf-8')
        if total + jetons(texte) > budget:
            ecartees.append(f'{nom} (fenêtre)')
            continue
        gardees.append(nom); sections.append(texte); total += jetons(texte)
    return SYSTEME + '\n\n' + skill + ''.join(sections), gardees, ecartees, total


def appeler(hote, modele, systeme, question, num_ctx):
    corps = json.dumps({'model': modele, 'stream': True, 'options': {'num_ctx': num_ctx},
                        'messages': [{'role': 'system', 'content': systeme}, {'role': 'user', 'content': question}]})
    req = urllib.request.Request(hote.rstrip('/') + '/api/chat', data=corps.encode(), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            for ligne in r:
                if not ligne.strip():
                    continue
                d = json.loads(ligne)
                if d.get('error'):
                    raise SystemExit(f"Ollama : {d['error']}")
                sys.stdout.write(d.get('message', {}).get('content', '')); sys.stdout.flush()
                if d.get('done'):
                    n = d.get('prompt_eval_count')
                    if n and n >= num_ctx:
                        print(f'\n[qwen-musique] le contexte a atteint {n} jetons sur {num_ctx} : réponse peut-être tronquée, '
                              'relancer avec --num-ctx plus grand ou moins de références', file=sys.stderr)
        print()
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors='replace')
        raise SystemExit(f'Ollama a refusé la requête ({e.code}) : {detail} — vérifier le nom exact avec `ollama list`')
    except urllib.error.URLError as e:
        raise SystemExit(f'Ollama ne répond pas sur {hote} ({e.reason}) : lancer `ollama serve` ou préciser --host')


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__.split('\n', 1)[1])
    p.add_argument('--model', help='nom exact affiché par `ollama list`')
    p.add_argument('--skill-dir', help=f'dossier du module (défaut : celui du script, puis ~/.claude/skills/compositeur-arrangeur/modules/{NOM}, idem sous ~/.codex)')
    p.add_argument('--ref', action='append', default=[], help='référence à inclure en priorité (répétable)')
    p.add_argument('--max-refs', type=int, default=4)
    p.add_argument('--num-ctx', type=int, default=int(os.environ.get('QWEN_MUSIQUE_NUM_CTX', 16384)),
                   help='fenêtre de contexte demandée à Ollama (défaut 16384 ; le modèle doit la supporter)')
    p.add_argument('--reserve', type=int, default=3000, help='jetons gardés pour la réponse')
    p.add_argument('--host', default=os.environ.get('OLLAMA_HOST', 'http://127.0.0.1:11434'))
    p.add_argument('--dry-run', action='store_true', help='afficher les références choisies et la taille, sans appeler Ollama')
    p.add_argument('question', nargs='*')
    a = p.parse_args(argv)
    if not a.host.startswith('http'):
        a.host = 'http://' + a.host
    question = ' '.join(a.question).strip()
    if not question and not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    if not question:
        p.error('donner une demande en argument ou sur stdin')
    racine = trouver_skill(a.skill_dir)
    if not racine:
        p.error(f'skill introuvable : lancer scripts/install.sh ou préciser --skill-dir')
    inconnues = [r for r in a.ref if r not in MOTS]
    if inconnues:
        p.error(f"référence inconnue : {', '.join(inconnues)} (connues : {', '.join(MOTS)})")
    refs = choisir(question, a.ref, a.max_refs)
    systeme, gardees, ecartees, total = construire(racine, question, refs, a.num_ctx, a.reserve)
    print(f"[qwen-musique] skill : {racine} ; références : {', '.join(gardees) or 'aucune'}"
          + (f" ; écartées : {', '.join(ecartees)}" if ecartees else '')
          + f" ; ≈ {total} jetons sur num_ctx {a.num_ctx}", file=sys.stderr)
    if a.dry_run:
        return 0
    if not a.model:
        p.error('--model est requis (nom exact de `ollama list`)')
    appeler(a.host, a.model, systeme, question, a.num_ctx)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
