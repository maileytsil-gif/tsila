#!/usr/bin/env python3
"""Extrait le texte de la dernière réponse de Claude (hook Stop) et le rend lisible à voix haute.

Entrée : le JSON du hook sur stdin (champ `last_assistant_message` s'il existe, sinon `transcript_path`).
Sortie : le texte nettoyé du Markdown, ou rien.
"""
import json, os, re, sys

MAX = int(os.environ.get("CLAUDE_VOIX_MAX", "3000"))

def texte_du_transcript(chemin):
    morceaux = []
    try:
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                try:
                    e = json.loads(ligne)
                except ValueError:
                    continue
                msg = e.get("message") or {}
                contenu = msg.get("content")
                if e.get("type") == "user":
                    # une vraie demande de l'utilisateur ouvre un nouveau tour ; un résultat d'outil non
                    if isinstance(contenu, str) or (isinstance(contenu, list) and any(
                            isinstance(b, dict) and b.get("type") == "text" for b in contenu)):
                        morceaux = []
                elif e.get("type") == "assistant" and isinstance(contenu, list):
                    for b in contenu:
                        if not isinstance(b, dict):
                            continue
                        if b.get("type") == "tool_use":
                            morceaux = []          # ne garder que le texte venu après le dernier outil
                        elif b.get("type") == "text" and b.get("text", "").strip():
                            morceaux.append(b["text"])
    except OSError:
        return ""
    return "\n".join(morceaux)

def nettoyer(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)             # blocs de code : non lus
    t = re.sub(r"`([^`]*)`", r"\1", t)                         # code en ligne : garder le mot
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)          # liens Markdown : garder le texte
    t = re.sub(r"https?://\S+", " ", t)                        # adresses : non lues
    t = re.sub(r"^\s*\|?\s*:?-{2,}.*$", " ", t, flags=re.M)    # lignes de séparation des tableaux
    t = t.replace("|", ", ")
    t = re.sub(r"^\s{0,3}#{1,6}\s*", "", t, flags=re.M)        # titres
    t = re.sub(r"^\s*[-*+]\s+", "", t, flags=re.M)             # puces
    t = re.sub(r"[*_~>]", "", t)                               # gras, italique, citations
    t = t.replace("→", " puis ").replace("≈", " environ ").replace("…", ".")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{2,}", "\n", t).strip()
    return t[:MAX]

def main():
    try:
        d = json.load(sys.stdin)
    except ValueError:
        return
    brut = d.get("last_assistant_message") or ""
    if not brut and d.get("transcript_path"):
        brut = texte_du_transcript(os.path.expanduser(d["transcript_path"]))
    if brut:
        sys.stdout.write(nettoyer(brut))

if __name__ == "__main__":
    main()
