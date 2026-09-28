#!/usr/bin/env python3
"""Client local, neutre vis-à-vis de l'agent (Claude, Qwen/Ollama, Codex…), pour le serveur HTTP du LOM Bridge
(`lom.py serve`, 0.8.x) : `inspect` (lecture seule, liste blanche), `preview` (plan serveur, rien n'est écrit),
`commit` (même spec, même plan, puis écriture).

Garde-fous propres à ce client — ils ne sécurisent pas le serveur contre un autre processus local :
- boucle locale seulement, jeton lu dans connection.json et jamais affiché ;
- aucune commande qui modifie le Set via `inspect` (`/py`, `/set`, `/call` sont de toute façon refusés par le serveur) ;
- `commit` exige l'empreinte de la spec ET celle du plan relu : si le Set a changé depuis `preview`
  (autre session Live, clips déplacés, valeur courante changée pour `unit: rel`…), l'écriture est refusée.
"""
import argparse
import hashlib
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

CONN_FILE = os.environ.get("LOM_BRIDGE_CONN") or os.path.join(os.path.expanduser("~"), "Library", "Application Support", "LOMBridge", "connection.json")
# Sous-ensemble en lecture seule de SAFE_HTTP (lom.py). /transport et /notes : voir read_only().
READ_COMMANDS = {"/ping", "/track", "/param", "/params", "/solve", "/clips", "/plan", "/read", "/events", "/jobs",
                 "/children", "/get", "/info", "/path", "/snapshots", "/locators", "/state", "/journal", "/transport", "/notes"}
MAX_REQUEST = 262144   # limite du serveur (413 au-delà)
MAX_RESPONSE = 4_000_000
MAX_ENTRIES = 32


def endpoint(value):
    u = urllib.parse.urlsplit(value)
    if u.scheme != "http" or u.hostname not in {"127.0.0.1", "localhost", "::1"} or u.username or u.password or u.query or u.fragment or u.path not in {"", "/"}:
        raise ValueError("l'adresse du bridge doit être une URL HTTP de base en boucle locale (http://127.0.0.1:7480)")
    return value.rstrip("/")


def read_only(command, args):
    """/transport sans argument lit l'état ; avec argument il le change. /notes get lit ; set/add écrivent."""
    if command not in READ_COMMANDS: return False
    if command == "/transport": return not args
    if command == "/notes": return bool(args) and args[0] == "get"
    return True


def token(path=None):
    path = path or CONN_FILE
    try: conn = json.loads(pathlib.Path(path).read_text())
    except FileNotFoundError: raise ValueError("fichier de connexion absent (%s) : LOMBridge est-il actif dans Live ?" % path)
    if not isinstance(conn, dict) or not isinstance(conn.get("token"), str) or not conn["token"]:
        raise ValueError("fichier de connexion invalide (%s)" % path)
    return conn["token"]


def post(base, route, body, timeout=8, conn=None):
    data = json.dumps(body, ensure_ascii=False, allow_nan=False).encode()
    if len(data) > MAX_REQUEST: raise ValueError("requête > 256 Kio : découper la spec")
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token(conn)}
    request = urllib.request.Request(endpoint(base) + route, data, headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read(MAX_RESPONSE + 1)
    except urllib.error.HTTPError as e:
        detail = e.read(4000).decode("utf-8", "replace")
        raise ValueError("HTTP %d sur %s : %s" % (e.code, route, detail))
    if len(raw) > MAX_RESPONSE: raise ValueError("réponse trop volumineuse")
    return json.loads(raw)


def spec_from_file(path):
    data = pathlib.Path(path).read_bytes()
    if len(data) > MAX_REQUEST: raise ValueError("spec > 256 Kio : découper")
    spec = json.loads(data)
    if not isinstance(spec, dict) or not isinstance(spec.get("automations"), list) or not spec["automations"]:
        raise ValueError("spec.automations doit être une liste non vide")
    active = [a for a in spec["automations"] if not (isinstance(a, dict) and a.get("skip"))]
    if not active: raise ValueError("toutes les entrées sont en skip")
    if len(active) > MAX_ENTRIES: raise ValueError("plus de %d automations : découper en lots" % MAX_ENTRIES)
    for i, item in enumerate(active):
        if not isinstance(item, dict) or not isinstance(item.get("track"), str) or not item["track"].strip():
            raise ValueError("[%d] track exact requis" % i)
        if not isinstance(item.get("param"), str) or not item["param"].strip():
            raise ValueError("[%d] param explicite requis (le bridge prendrait Volume par défaut)" % i)
        if not isinstance(item.get("points"), list) or not item["points"]:
            raise ValueError("[%d] points requis" % i)
        if len(item["points"]) < 2 and not item.get("hold"):
            raise ValueError("[%d] un seul point : donner deux temps ou hold" % i)
    canonical = json.dumps(spec, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode()
    return spec, hashlib.sha256(canonical).hexdigest(), len(active)


def plan_fingerprint(results):
    """Empreinte de ce que le bridge a planifié : cible résolue, valeurs, clips (références de session comprises), trou."""
    keep = []
    for r in results:
        p, plan = r.get("param") or {}, r.get("plan") or {}
        keep.append({"param": [p.get("ref"), p.get("name"), p.get("min"), p.get("max")],
                     "points": [[x.get("t"), x.get("raw"), x.get("display"), x.get("clamped")] for x in plan.get("points", [])],
                     "clips": [[c.get("ref"), c.get("start"), c.get("end"), c.get("window"), c.get("audio"), c.get("exposes_envelope"), c.get("problems")] for c in plan.get("clips", [])],
                     "gap": plan.get("gap", 0)})
    return hashlib.sha256(json.dumps(keep, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def check_preview(reply, expected):
    if not isinstance(reply, dict) or "error" in reply or not isinstance(reply.get("results"), list):
        raise ValueError("plan du bridge absent ou invalide : " + json.dumps(reply, ensure_ascii=False)[:1500])
    results = reply["results"]
    if len(results) != expected: raise ValueError("le bridge a planifié %d entrée(s) sur %d" % (len(results), expected))
    bad = []
    for r in results:
        plan = r.get("plan")
        if (r.get("ok") is not True or r.get("dry") is not True or not isinstance(plan, dict) or plan.get("errors")
                or float(plan.get("gap", 0)) > 1e-3):
            bad.append({k: r.get(k) for k in ("index", "ok", "errors", "codes")} | {"plan_errors": (plan or {}).get("errors"), "gap": (plan or {}).get("gap")})
    if bad: raise ValueError("plan refusé ou plage non couverte : " + json.dumps(bad, ensure_ascii=False)[:1500])
    return results


def main(argv=None, out=sys.stdout):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", default="http://127.0.0.1:7480")
    sub = ap.add_subparsers(dest="action", required=True)
    p = sub.add_parser("inspect", help="commande en lecture seule (liste blanche)")
    p.add_argument("command"); p.add_argument("args", nargs="*")
    p = sub.add_parser("preview", help="plan serveur de la spec, rien n'est écrit")
    p.add_argument("spec")
    p = sub.add_parser("commit", help="replanifie, compare au preview relu, puis écrit")
    p.add_argument("spec")
    p.add_argument("--sha256", required=True, help="empreinte de la spec donnée par preview")
    p.add_argument("--plan-sha256", required=True, help="empreinte du plan donnée par preview")
    a = ap.parse_args(argv)
    if a.action == "inspect":
        if not read_only(a.command, a.args): raise ValueError("commande hors liste blanche lecture seule : %s %s" % (a.command, " ".join(a.args[:1])))
        result = post(a.url, "/cmd", {"cmd": a.command, "args": a.args}, timeout=60)
        if result.get("ok") is not True: raise ValueError("commande refusée : " + json.dumps(result, ensure_ascii=False)[:1500])
        print(json.dumps(result, ensure_ascii=False, indent=2), file=out); return 0
    spec, digest, expected = spec_from_file(a.spec)
    if a.action == "commit" and digest != a.sha256: raise ValueError("la spec a changé depuis le preview : le refaire et le relire")
    dry = post(a.url, "/apply", {"spec": spec, "dry": True}, timeout=240)
    plan_digest = plan_fingerprint(check_preview(dry, expected))
    if a.action == "preview":
        print(json.dumps({"ok": True, "sha256": digest, "plan_sha256": plan_digest, "log": dry.get("log", []), "preview": dry["results"]}, ensure_ascii=False, indent=2), file=out); return 0
    if plan_digest != a.plan_sha256: raise ValueError("le Set a changé depuis le preview (plan différent) : refaire preview et relire")
    applied = post(a.url, "/apply", {"spec": spec, "dry": False}, timeout=600)
    results = applied.get("results") if isinstance(applied, dict) else None
    if not isinstance(results, list) or len(results) != expected or any(r.get("ok") is not True for r in results):
        raise ValueError("écriture refusée ou incomplète (chaque entrée est une étape d'annulation séparée) : contrôler dans Live, `lom.py journal`, Cmd+Z si besoin : "
                         + json.dumps(applied, ensure_ascii=False)[:1500])
    print(json.dumps({"ok": True, "sha256": digest, "plan_sha256": plan_digest, "log": applied.get("log", []),
                      "codes": [r.get("codes", []) for r in results], "verify_in_live": True}, ensure_ascii=False, indent=2), file=out); return 0


if __name__ == "__main__":
    try: raise SystemExit(main())
    except (ValueError, OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1)
