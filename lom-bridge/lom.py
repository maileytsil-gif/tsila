#!/usr/bin/env python3
"""lom.py — client du LOM Bridge (Remote Script Ableton Live). Zéro dépendance (Python 3.8+). Version : LOMBridge/version.py.

  lom.py ping
  lom.py children live_set tracks
  lom.py track "AUDIO - Sub"
  lom.py param "AUDIO - Sub" mixer Volume                  -> ref, nom, min, max, valeur, affichage, quantifié, état automation
  lom.py params <deviceRef> [filtre]
  lom.py clips "AUDIO - Sub"
  lom.py plan  "AUDIO - Sub" <paramRef> --unit disp --res 8 --curve lin --accept fades  5|1 -5 8|4.5 -5 9|1 0
  lom.py shape "AUDIO - Sub" <paramRef> --unit disp --res 8 --curve lin --accept fades  5|1 -5 8|4.5 -5 9|1 0
  lom.py read  "AUDIO - Sub" <paramRef> 5|1 9|1 --res 1
  lom.py clear "AUDIO - Sub" <paramRef> 5|1 9|1 --accept fades
  lom.py apply spec.json [--dry]                            -> plan serveur (dry) ou écriture, mêmes contrôles
  lom.py jobs | cancel [<id>] | py "song.tempo" | serve --port 7480 [--unsafe]
  lom.py transport [play [t] | stop | pos <t> | loop on|off | loop <début> <longueur>]
  lom.py meters <t_départ> <secondes> [piste …]            -> crête par piste (+ master) pendant la lecture, transport restauré
  lom.py setparam "<piste>" <device|mixer> <param> <valeur> [raw] [override]   -> avant/après, relu ; refus si automatisé sans override
  lom.py snapshot "<piste>" [device|mixer] | snapshots | restore <id> [override]
  lom.py locators | locator <t> <nom> | state [--json]
  lom.py load "<piste>" "<nom>" [plugins|sounds|audio_effects|…] [replace=<device>]   -> charge sans hot-swap, vérifié
  lom.py notes get "<piste>" <clipRef|t> [tA tB] | notes set|add "<piste>" <clipRef|t> '<json>' [tA tB]
  lom.py wait [<id>]                                        -> attend la fin d'une tâche (ou de toutes)
  lom.py journal [n]                                        -> dernières écritures journalisées par le bridge
  lom.py policy [accept=fades,expressions]                  -> accords acceptés d'office par ce client (policy.json)
  --bpb <n> : temps par mesure pour « mesure|temps » (sinon la signature est lue dans Live) ; erreurs : `ERREUR [E_CODE]: texte`

Références d'objets : chaînes opaques "o:<session>:<n>" renvoyées par le bridge, jamais des nombres.
Temps : nombre de temps (noires) depuis 1|1, ou « mesure|temps » (17|1, 17|3.5, 5|2|3), 4/4 par défaut.
"""
import socket, struct, sys, json, time, argparse, re, os, math

def _script_version():
    """Version du script sur le disque (LOMBridge/version.py à côté de ce fichier) ; None si le dossier n'est pas là."""
    try:
        ns = {}
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "LOMBridge", "version.py"), encoding="utf-8") as f: exec(f.read(), ns)
        return ns["VERSION"]
    except Exception: return None
VERSION = _script_version()
HOST, TX = "127.0.0.1", 7421
CONN_FILE = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "LOMBridge", "connection.json")
BEATS_PER_BAR = 4
SAFE_HTTP = {"/ping", "/track", "/param", "/params", "/solve", "/clips", "/plan", "/shape", "/read", "/events", "/clear", "/jobs", "/cancel", "/children", "/get", "/info", "/path",
             "/transport", "/meters", "/setparam", "/snapshot", "/snapshots", "/restore", "/locators", "/locator", "/state", "/journal", "/load", "/notes"}
TIME_ARGS = {"transport": (1, 2), "meters": (0,), "locator": (0,), "notes": (2, 3, 4, 5)}   # positions des arguments « temps » (mesure|temps accepté) par commande générique

# ---------- OSC minimal (i, h, f, s) ----------
def _pad(b): return b + b"\0" * ((4 - len(b) % 4) % 4)
def osc_pack(addr, args):
    tags, data = ",", b""
    for a in args:
        if isinstance(a, bool): a = int(a)
        if isinstance(a, int):
            if -2**31 <= a < 2**31: tags += "i"; data += struct.pack(">i", a)
            elif -2**63 <= a < 2**63: tags += "h"; data += struct.pack(">q", a)
            else: raise ValueError("entier hors int64: %r" % a)
        elif isinstance(a, float):
            if not math.isfinite(a): raise ValueError("flottant non fini")
            tags += "f"; data += struct.pack(">f", a)
        else: tags += "s"; data += _pad(str(a).encode("utf-8") + b"\0")
    return _pad(addr.encode() + b"\0") + _pad(tags.encode() + b"\0") + data
def _str(buf, i):
    j = buf.index(b"\0", i); s = buf[i:j].decode("utf-8", "replace"); return s, i + ((j - i) // 4 + 1) * 4
def osc_unpack(buf):
    addr, i = _str(buf, 0); tags, i = _str(buf, i); args = []
    for t in tags[1:]:
        if t == "i": args.append(struct.unpack(">i", buf[i:i+4])[0]); i += 4
        elif t == "h": args.append(struct.unpack(">q", buf[i:i+8])[0]); i += 8
        elif t == "f": args.append(struct.unpack(">f", buf[i:i+4])[0]); i += 4
        elif t == "d": args.append(struct.unpack(">d", buf[i:i+8])[0]); i += 8
        elif t == "s": s, i = _str(buf, i); args.append(s)
        elif t == "T": args.append(True)
        elif t == "F": args.append(False)
        else: raise ValueError("type OSC non géré: " + t)
    return addr, args

# ---------- temps / nombres ----------
def parse_time(s, bpb=None):
    bpb = bpb or BEATS_PER_BAR
    if isinstance(s, (int, float)) and not isinstance(s, bool): return float(s)
    s = str(s).strip()
    m = re.match(r"^(\d+)\|(\d+(?:\.\d+)?)(?:\|(\d+(?:\.\d+)?))?$", s)
    if m:
        bar, beat = int(m.group(1)), float(m.group(2)); tick = float(m.group(3)) if m.group(3) else 1
        return (bar - 1) * bpb + (beat - 1) + (tick - 1) * 0.25
    if re.match(r"^-?\d+(\.\d+)?$", s): return float(s)
    raise ValueError("temps invalide: %r" % s)
def fmt_time(t, bpb=None):
    bpb = bpb or BEATS_PER_BAR
    bar = int(t // bpb) + 1; beat = t - (bar - 1) * bpb + 1
    return f"{bar}|{beat:g}"
def num(x):
    """Chaîne de ligne de commande -> int exact / float ; les références (o:…) et tout le reste restent des chaînes."""
    if not isinstance(x, str): return x
    if re.match(r"^-?\d+$", x): return int(x)
    if re.match(r"^-?\d+\.\d+$", x): return float(x)
    return x
def _parse_disp(s):
    s = str(s)
    if "inf" in s.lower(): return -float("inf")
    m = re.search(r"(-?\d+(?:[.,]\d+)?)\s*([a-zA-Z%]*)", s)
    if not m: return float("nan")
    v = float(m.group(1).replace(",", "."))
    return v * 1000 if m.group(2).lower().startswith("k") else v

# ---------- client ----------
def read_connection(path=CONN_FILE):
    try: c = json.load(open(path))
    except FileNotFoundError: raise RuntimeError("fichier de connexion absent (%s) : LOMBridge est-il actif dans Live ? (Réglages > Link, Tempo & MIDI > Surface de contrôle)" % path)
    if not isinstance(c.get("token"), str): raise RuntimeError("fichier de connexion invalide")
    return c

class Bridge:
    def __init__(self, host=HOST, tx=None, timeout=240.0, conn=None):
        conn = conn or read_connection()
        self.host, self.tx, self.timeout, self.token = host, tx or conn.get("port", TX), timeout, conn["token"]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, 0)); self.sock.settimeout(0.5); self._seq = 0
    def send(self, cmd, *args):
        """{'ok', 'rows', 'errors', 'codes'} ; chaque ligne reçue porte l'id de requête en premier argument, le reste est ignoré.
        Une erreur arrive comme `/err <id> <code E_…> <texte>` : le code va dans 'codes', le texte dans 'errors' (même index)."""
        self._drain()
        rid = "%d-%d" % (time.time_ns() % 10**9, self._seq); self._seq += 1
        self.sock.sendto(osc_pack(cmd, list(args) + ["!" + self.token, "#" + rid]), (self.host, self.tx))
        rows, errors, codes, t0 = [], [], [], time.time()
        while time.time() - t0 < self.timeout:
            try: data, _ = self.sock.recvfrom(65536)
            except socket.timeout: continue
            addr, a = osc_unpack(data)
            if not a or str(a[0]) != rid: continue
            body = a[1:]
            if addr == "/end": return {"ok": not errors, "rows": rows, "errors": errors, "codes": codes}
            if addr == "/err":
                if body and isinstance(body[0], str) and body[0].startswith("E_"): codes.append(body[0]); body = body[1:]
                else: codes.append("E_ERROR")
                errors.append(" ".join(map(str, body)))
            elif addr == "/r": rows.append(body)
        return {"ok": False, "rows": rows, "errors": errors + [f"timeout {self.timeout}s (LOMBridge actif ? transport arrêté ?)"], "codes": codes + ["E_TIMEOUT"]}
    def _drain(self):
        self.sock.setblocking(False)
        try:
            while True: self.sock.recvfrom(65536)
        except (BlockingIOError, OSError): pass
        finally: self.sock.settimeout(0.5)
    def beats_per_bar(self):
        """Signature lue dans Live (numérateur), mise en cache ; 4 si le bridge ne répond pas."""
        if getattr(self, "_bpb", None): return self._bpb
        r = self.send("/transport"); sig = str(r["rows"][0][4]) if r["ok"] and r["rows"] else "4/4"
        self._bpb = int(sig.split("/")[0]) or 4; return self._bpb
    def wait(self, rid=None, poll=0.5, log=None):
        """Attend la fin d'une tâche (par id) ou de toutes ; renvoie True si la file s'est vidée avant le délai."""
        t0 = time.time()
        while time.time() - t0 < self.timeout:
            r = self.send("/jobs")
            if not r["ok"]: raise RuntimeError("; ".join(r["errors"]))
            pending = [j for j in r["rows"] if rid is None or str(j[0]) == str(rid)]
            if not pending: return True
            if log: log("en attente : " + ", ".join(f"{j[1]} {j[0]} {j[2]}" for j in pending))
            time.sleep(poll)
        return False

# ---------- accords par défaut (côté client) ----------
POLICY_FILE = os.path.join(os.path.dirname(CONN_FILE), "policy.json")
def read_policy(path=POLICY_FILE):
    """{'accept': [...]} : pertes acceptées d'office par ce client (ex. expressions sur tout clip MIDI sans MPE)."""
    try:
        with open(path, encoding="utf-8") as f: p = json.load(f)
        acc = p.get("accept", [])
        return {"accept": [x for x in acc if isinstance(x, str)]} if isinstance(acc, list) else {"accept": []}
    except Exception: return {"accept": []}
def write_policy(policy, path=POLICY_FILE):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f: json.dump(policy, f, ensure_ascii=False)
def merge_accept(accept, policy=None):
    """Union ordonnée des accords demandés et de ceux de la politique ; refuse une clé inconnue."""
    policy = read_policy() if policy is None else policy
    out = []
    for x in list(accept or []) + list(policy.get("accept", [])):
        if x not in ACCEPT_KEYS: raise ValueError("accept invalide : %s (valides : %s)" % (x, ", ".join(ACCEPT_KEYS)))
        if x not in out: out.append(x)
    return out

# ---------- haut niveau ----------
def resolve_param(b, track, device, param):
    r = b.send("/param", track, device, param)
    if not r["ok"]: raise RuntimeError("; ".join(r["errors"]))
    ref, name, mn, mx, val, disp = r["rows"][0][:6]
    return {"ref": str(ref), "name": name, "min": mn, "max": mx, "value": val, "display": disp,
            "quantized": int(r["rows"][0][6]) if len(r["rows"][0]) > 6 else 0}

VALID_CURVES = {"lin", "linear", "exp", "log", "sc", "scurve", "sin"}
ACCEPT_KEYS = ("fades", "expressions", "warp", "clamp", "unverified")

def version_warning(ping_rows):
    """Après /ping : message si le bridge chargé dans Live n'a pas la version du script sur le disque (rechargement à chaud
    perdu au chargement d'un Set : relancer Live), sinon None."""
    if not VERSION: return None
    row = next((r for r in ping_rows if r and r[0] == "pong"), None)
    if not row or len(row) < 2 or str(row[1]) == VERSION: return None
    return "ATTENTION : bridge chargé dans Live = %s, script sur le disque = %s (relancer Live pour charger le script du disque)" % (row[1], VERSION)

def validate_entry(a, i):
    if not isinstance(a, dict): raise ValueError(f"[{i}] entrée non objet")
    for k in ("track", "points"):
        if k not in a: raise ValueError(f"[{i}] champ manquant : {k}")
    if not isinstance(a["track"], str) or not a["track"].strip(): raise ValueError(f"[{i}] track invalide")
    if a.get("unit", "disp") not in ("rel", "disp", "raw"): raise ValueError(f"[{i}] unit invalide : {a.get('unit')}")
    res = a.get("res", 8)
    if isinstance(res, bool) or not isinstance(res, (int, float)) or not (0 < res <= 64): raise ValueError(f"[{i}] res doit être dans ]0, 64] : {res}")
    curve = a.get("curve", "lin")
    if not (curve in VALID_CURVES or (isinstance(curve, (int, float)) and not isinstance(curve, bool))): raise ValueError(f"[{i}] curve invalide : {curve}")
    acc = a.get("accept", [])
    if not isinstance(acc, list) or any(x not in ACCEPT_KEYS for x in acc): raise ValueError(f"[{i}] accept invalide : {acc} (valides : {', '.join(ACCEPT_KEYS)})")
    pts = a["points"]
    if not isinstance(pts, list) or not pts: raise ValueError(f"[{i}] points vide")
    out = []
    for p in pts:
        if not (isinstance(p, list) and len(p) == 2): raise ValueError(f"[{i}] point mal formé : {p}")
        t = parse_time(p[0]); v = p[1]
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v): raise ValueError(f"[{i}] valeur non finie : {p}")
        if t < 0: raise ValueError(f"[{i}] temps négatif : {p}")
        out.append((t, float(v)))
    if any(b_[0] < a_[0] for a_, b_ in zip(out, out[1:])): raise ValueError(f"[{i}] points non ordonnés dans le temps")
    return out

def shape_args(track, ref, unit, res, curve, hold, accept, pts):
    return [track, ref, unit, float(res), curve, int(bool(hold)), ",".join(accept) if accept else "-"] + [x for t, v in pts for x in (float(t), float(v))]

def apply_spec(b, spec, dry=False, log=print, policy=None):
    """dry=True : /plan côté serveur (mêmes contrôles que l'écriture, rien n'est modifié) ; sinon /shape.
    beatsPerBar : celui de la spec, sinon la signature lue dans Live. accept : ceux de l'entrée + la politique du client."""
    global BEATS_PER_BAR
    BEATS_PER_BAR = spec.get("beatsPerBar") or b.beats_per_bar()
    policy = read_policy() if policy is None else policy
    results = []
    for i, a in enumerate(spec.get("automations", [])):
        if isinstance(a, dict) and a.get("skip"): continue
        try: pts = validate_entry(a, i)
        except Exception as e:
            log(f"ERR {e}"); results.append({"index": i, "ok": False, "errors": [str(e)]}); continue
        track, device, param = a["track"], a.get("device", "mixer"), a.get("param", "Volume")
        unit, res, curve, hold, accept = a.get("unit", "disp"), a.get("res", 8), a.get("curve", "lin"), a.get("hold", False), merge_accept(a.get("accept", []), policy)
        try: info = resolve_param(b, track, device, param)
        except Exception as e:
            log(f"ERR [{i}] {track} / {device} / {param} : {e}"); results.append({"index": i, "ok": False, "errors": [str(e)]}); continue
        if unit == "rel":
            base = _parse_disp(info["display"])
            if not math.isfinite(base):
                msg = f"[{i}] unit=rel impossible : affichage courant non numérique ({info['display']!r})"; log("ERR " + msg); results.append({"index": i, "ok": False, "errors": [msg]}); continue
            pts = [(t, round(base + v, 4)) for t, v in pts]; unit = "disp"
        args = shape_args(track, info["ref"], unit, res, curve, hold, accept, pts)
        desc = f"[{i}] {track} / {device} / {info['name']} : " + ", ".join(f"{fmt_time(t)}={v:g}" for t, v in pts) + (f"  — {a['note']}" if a.get("note") else "")
        r = b.send("/plan" if dry else "/shape", *args)
        plan = next((json.loads(x[1]) for x in r["rows"] if x and x[0] == "plan"), None)
        if plan:
            desc += "\n      valeurs: " + ", ".join(f"{p['display']}{' (saturée)' if p['clamped'] else ''}" for p in plan["points"])
            desc += "\n      clips: " + "; ".join(f"{c['name'] or '(sans nom)'} {fmt_time(c['window'][0])}-{fmt_time(c['window'][1])}{' échantillonnage ' + str(c['sampling_seconds']) + ' s' if c['sampling'] else ''}" for c in plan["clips"])
            if plan.get("gap"): desc += f"\n      non couvert: {plan['gap']:g} temps"
            for w in plan["warnings"]: desc += f"\n      avertissement: {w}"
            for e in plan["errors"]: desc += f"\n      ERREUR: {e}"
        for x in r["rows"]:
            if x and x[0] == "verified": desc += f"\n      relecture: {x[4]}" + (f", {x[1]} points, écart max {x[2]:g} (tolérance {x[3]:g})" if x[1] else "")
            elif x and x[0] == "warn": desc += f"\n      avertissement: {x[1]}"
        ok = r["ok"] and (not plan or not plan["errors"])
        log(("DRY " if dry else "OK  ") + desc if ok else "ERR " + desc + ("\n      " + "; ".join(f"[{c}] {e}" for c, e in zip(r.get("codes", []), r["errors"])) if r["errors"] else ""))
        results.append({"index": i, "ok": ok, "dry": dry, "param": info, "plan": plan, "reply": r["rows"], "errors": r["errors"], "codes": r.get("codes", [])})
    return results

# ---------- serveur HTTP (clients non-OSC : ChatGPT, curl) ----------
def http_allowed(cmd, unsafe=False): return unsafe or cmd in SAFE_HTTP

def serve(port, unsafe=False):
    from http.server import BaseHTTPRequestHandler, HTTPServer
    b = Bridge(); token = b.token
    class H(BaseHTTPRequestHandler):
        def _json(self, code, obj):
            body = json.dumps(obj, ensure_ascii=False).encode()
            self.send_response(code); self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
        def _auth(self):
            if self.headers.get("Origin"): self._json(403, {"error": "Origin refusé"}); return False
            if self.headers.get("Authorization") != "Bearer " + token: self._json(401, {"error": "Authorization: Bearer <token> requis (token dans %s)" % CONN_FILE}); return False
            return True
        def do_GET(self):
            if not self._auth(): return
            self._json(200, {"service": "LOM Bridge HTTP", "version": VERSION, "commands": sorted(SAFE_HTTP), "unsafe": unsafe,
                             "usage": {"POST /cmd": {"cmd": "/param", "args": ["AUDIO - Sub", "mixer", "Volume"]}, "POST /apply": {"spec": {"automations": []}, "dry": True}}})
        def do_POST(self):
            if not self._auth(): return
            n = int(self.headers.get("Content-Length", 0))
            if n > 262144: self._json(413, {"error": "trop volumineux"}); return
            try: body = json.loads(self.rfile.read(n) or b"{}")
            except Exception: self._json(400, {"error": "JSON invalide"}); return
            try:
                if self.path == "/cmd":
                    cmd = str(body.get("cmd", ""))
                    if not http_allowed(cmd, unsafe): self._json(403, {"error": "commande non autorisée en HTTP : " + cmd}); return
                    args = [parse_time(x) if isinstance(x, str) and "|" in x else x for x in body.get("args", [])]
                    self._json(200, b.send(cmd, *args))
                elif self.path == "/apply":
                    logs = []; res = apply_spec(b, body["spec"], body.get("dry", True), logs.append)
                    self._json(200, {"log": logs, "results": res})
                else: self._json(404, {"error": "routes : POST /cmd, POST /apply"})
            except Exception as e: self._json(500, {"error": str(e)})
        def log_message(self, *a): pass
    print(f"LOM Bridge HTTP sur http://127.0.0.1:{port} — Authorization: Bearer <token> ; /py, /set, /call, /reload {'AUTORISÉS (--unsafe)' if unsafe else 'bloqués'}")
    HTTPServer(("127.0.0.1", port), H).serve_forever()

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    ap.add_argument("--unit", default="disp"); ap.add_argument("--res", type=float, default=8); ap.add_argument("--curve", default="lin")
    ap.add_argument("--hold", type=int, default=0); ap.add_argument("--accept", default=""); ap.add_argument("--dry", action="store_true")
    ap.add_argument("--port", type=int, default=7480); ap.add_argument("--unsafe", action="store_true")
    ap.add_argument("--timeout", type=float, default=240.0); ap.add_argument("--json", action="store_true")
    ap.add_argument("--bpb", type=int, default=0, help="temps par mesure pour « mesure|temps » (défaut : signature lue dans Live)")
    o = ap.parse_args()
    global BEATS_PER_BAR
    if o.cmd == "serve": return serve(o.port, o.unsafe)
    if o.cmd == "policy":
        pol = read_policy()
        for x in o.args:
            k, _, v = x.partition("=")
            if k != "accept": raise SystemExit("usage: lom.py policy [accept=fades,expressions,…]  (accept= vide pour effacer)")
            pol["accept"] = merge_accept([y for y in v.split(",") if y], {"accept": []}); write_policy(pol)
        print(json.dumps({"file": POLICY_FILE, **pol}, ensure_ascii=False)); return
    b = Bridge(timeout=o.timeout)
    if o.bpb: BEATS_PER_BAR = o.bpb
    elif any("|" in x for x in o.args): BEATS_PER_BAR = b.beats_per_bar()
    accept = merge_accept([x for x in o.accept.split(",") if x]) if o.cmd in ("shape", "plan", "clear") else []
    if o.cmd == "apply":
        spec = json.load(open(o.args[0]))
        if o.bpb: spec["beatsPerBar"] = o.bpb
        res = apply_spec(b, spec, o.dry)
        return sys.exit(0 if all(r.get("ok") for r in res) else 1)
    if o.cmd == "wait":
        done = b.wait(o.args[0] if o.args else None, log=lambda m: print(m, file=sys.stderr))
        print("terminé" if done else "toujours en cours"); return sys.exit(0 if done else 1)
    a = [num(x) for x in o.args]
    if o.cmd in ("shape", "plan"):
        track, ref = o.args[0], o.args[1]
        pts = [(parse_time(o.args[i]), float(o.args[i + 1])) for i in range(2, len(o.args) - 1, 2)]
        r = b.send("/" + o.cmd, *shape_args(track, ref, o.unit, o.res, o.curve, o.hold, accept, pts))
    elif o.cmd == "read":
        r = b.send("/read", o.args[0], o.args[1], parse_time(o.args[2]), parse_time(o.args[3]), o.res)
        for row in r["rows"]:
            if isinstance(row[0], (int, float)): row.insert(0, fmt_time(row[0]))
    elif o.cmd == "clear":
        r = b.send("/clear", o.args[0], o.args[1], parse_time(o.args[2]), parse_time(o.args[3]), ",".join(accept) or "-")
    elif o.cmd in ("py", "js"):
        r = b.send("/py", " ".join(o.args))
    elif o.cmd == "setparam":
        r = b.send("/setparam", o.args[0], o.args[1], o.args[2], float(o.args[3]), *o.args[4:])
    else:
        for i in TIME_ARGS.get(o.cmd, ()):
            if i < len(a) and isinstance(a[i], str) and "|" in a[i]: a[i] = parse_time(a[i])
        r = b.send("/" + o.cmd, *a)
    if o.cmd == "ping":
        w = version_warning(r["rows"])
        if w: r["errors"].append(w)
    if o.json: print(json.dumps(r, ensure_ascii=False)); return
    for row in r["rows"]: print(" ".join(f"{x:.4f}" if isinstance(x, float) else str(x) for x in row))
    for c, e in zip(r.get("codes", []) + ["E_ERROR"] * len(r["errors"]), r["errors"]): print(f"ERREUR [{c}]:", e, file=sys.stderr)
    sys.exit(0 if r["ok"] else 1)

if __name__ == "__main__": main()
