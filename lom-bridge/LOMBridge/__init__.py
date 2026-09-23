# -*- coding: utf-8 -*-
"""LOM Bridge — Remote Script Ableton Live (Python) : pont OSC/UDP vers l'API Live, automation d'arrangement comprise.
Numéro de version : LOMBridge/version.py (seule source, partagée avec lom.py).

Principe (contraintes de l'API Live 12.4) : une enveloppe ne se crée que sur un clip de SESSION et n'agit que dans l'étendue
de SON clip. Le bridge reconstruit donc chaque clip d'arrangement concerné depuis la session (mêmes notes / même fichier audio,
marqueurs, warp, enveloppes existantes recopiées) en y ajoutant les nouveaux points, puis le remet à sa place.

Toute écriture (/shape, /clear) se fait en trois phases : lecture de l'existant (peut prendre du temps, rien n'est modifié),
écriture de tous les clips d'un bloc dans une seule étape d'annulation et sans pause, puis relecture de contrôle. Si l'écriture
échoue après qu'un clip a été remplacé, ou si la relecture s'écarte de ce qui devait être écrit, l'étape est défaite (song.undo).

Protocole : OSC sur UDP 127.0.0.1:7421 ; chaque commande se termine par "!<jeton>" puis "#<id de requête>".
Réponses (l'id de requête est TOUJOURS le premier argument) : /begin <id> <cmd> · /r <id> … · /err <id> <texte> · /end <id> <cmd>.
Références d'objets : chaînes opaques "o:<session>:<n>" ; jamais des nombres.
"""
import socket, struct, re, math, traceback, os, json, random
import Live
from _Framework.ControlSurface import ControlSurface

def _read_version():
    ns = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "version.py"), encoding="utf-8") as f: exec(f.read(), ns)
    return ns["VERSION"]
VERSION = _read_version()
RX_PORT = 7421
CONN_FILE = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "LOMBridge", "connection.json")
MAX_READ_POINTS = 400
MAX_SHAPE_POINTS = 4096
MAX_JOBS = 4
SAMPLE_STEP = 0.125        # pas d'échantillonnage (temps) de l'automation existante non exposée
TICK_SECONDS = 0.1          # période approximative d'update_display
CANCEL_GRACE_TICKS = 50     # ticks laissés à une tâche en cours pour s'arrêter d'elle-même après /cancel, avant fermeture forcée
ACCEPT_KEYS = ("fades", "expressions", "warp", "clamp", "unverified")   # unverified : écrire sans relecture de contrôle
VERIFY_TOL = 0.002          # écart toléré à la relecture, en fraction de la plage du paramètre
VERIFY_MAX_CHECKS = 600     # relecture exacte : nombre maximal d'instants contrôlés par clip
VERIFY_EPS = 1e-4           # relecture exacte : distance aux points (de part et d'autre d'une marche)
VERIFY_STEP = 0.0625        # relecture par curseur : distance aux bords de la fenêtre (temps)

# ---------- OSC minimal (int32 'i', int64 'h', float32 'f', string 's') ----------
def _pad(b): return b + b"\0" * ((4 - len(b) % 4) % 4)
def osc_pack(addr, args):
    tags, data = ",", b""
    for a in args:
        if isinstance(a, bool): a = int(a)
        if isinstance(a, int):
            if -2**31 <= a < 2**31: tags += "i"; data += struct.pack(">i", a)
            else: tags += "h"; data += struct.pack(">q", a)
        elif isinstance(a, float):
            if math.isnan(a) or math.isinf(a): a = 0.0
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

# ---------- utilitaires purs ----------
def parse_disp(s):
    s = str(s)
    if "inf" in s.lower(): return -float("inf") if "-" in s else float("inf")
    m = re.search(r"(-?\d+(?:[.,]\d+)?)\s*([a-zA-Zµ%]*)", s)
    if not m: return float("nan")
    v = float(m.group(1).replace(",", "."))
    if m.group(2).lower().startswith("k"): v *= 1000
    return v

def curve_fn(c):
    if isinstance(c, (int, float)) and not isinstance(c, bool): return lambda x: x ** float(c)
    c = str(c)
    if c == "exp": return lambda x: x * x
    if c == "log": return lambda x: math.sqrt(x)
    if c in ("sc", "scurve"): return lambda x: x * x * (3 - 2 * x)
    if c == "sin": return lambda x: 0.5 - 0.5 * math.cos(math.pi * x)
    return lambda x: x

def is_linear(c): return str(c) in ("lin", "linear", "1")
def is_num(x): return isinstance(x, (int, float)) and not isinstance(x, bool)

def simplify(pts, tol=0.0015):
    """Ramer-Douglas-Peucker itératif sur (t, v)."""
    if len(pts) <= 2: return list(pts)
    keep = [False] * len(pts); keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        i0, i1 = stack.pop()
        (t0, v0), (t1, v1) = pts[i0], pts[i1]; dmax, idx = 0.0, -1
        for i in range(i0 + 1, i1):
            t, v = pts[i]
            vi = v0 + (v1 - v0) * ((t - t0) / (t1 - t0) if t1 > t0 else 0.0)
            d = abs(v - vi)
            if d > dmax: dmax, idx = d, i
        if idx >= 0 and dmax > tol:
            keep[idx] = True; stack.append((i0, idx)); stack.append((idx, i1))
    return [p for p, k in zip(pts, keep) if k]

def interp(pts, cf, t, side="right"):
    """Valeur de la polyligne en t ; side='right' = après un saut en t, 'left' = avant."""
    if t < pts[0][0] - 1e-12: return pts[0][1]
    if t > pts[-1][0] + 1e-12: return pts[-1][1]
    same = [v for (tt, v) in pts if abs(tt - t) <= 1e-12]
    if same: return same[-1] if side == "right" else same[0]
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        if t0 <= t <= t1 and t1 > t0: return v0 + (v1 - v0) * cf((t - t0) / (t1 - t0))
    return pts[-1][1]

def count_breakpoints(pts, res, linear):
    n = 1
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        dur = t1 - t0
        if dur <= 0 or linear or v0 == v1: n += 1
        else: n += max(2, int(round(dur * res)))
    return n

def breakpoints(pts, cf, res, linear):
    out = [pts[0]]
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        dur = t1 - t0
        if dur <= 0 or linear or v0 == v1: out.append((t1, v1)); continue
        n = max(2, int(round(dur * res)))
        for k in range(1, n + 1): out.append((t0 + dur * k / n, v0 + (v1 - v0) * cf(k / n)))
    return out

_ident = lambda x: x

# Codes d'erreur stables (premier argument de /err après l'id), déduits du message ; l'ordre compte (premier motif trouvé).
ERROR_CODES = (
    ("ANNULATION AUTOMATIQUE IMPOSSIBLE", "E_ROLLBACK_FAILED"), ("annulée automatiquement", "E_ROLLED_BACK"),
    ("jeton", "E_AUTH"), ("commande inconnue", "E_UNKNOWN_CMD"), ("usage:", "E_USAGE"), ("file de tâches pleine", "E_QUEUE_FULL"),
    ("annulée", "E_CANCELLED"), ("lecture en cours", "E_TRANSPORT_PLAYING"), ("transport démarré", "E_TRANSPORT_PLAYING"),
    ("lecture arrêtée", "E_TRANSPORT_STOPPED"), ("curseur déplacé", "E_CURSOR_MOVED"), ("replanifier", "E_STALE"),
    ("plan invalide", "E_PLAN"), ("surchargée", "E_AUTOMATION_OVERRIDDEN"), ("automatisé", "E_AUTOMATED"),
    ("référence", "E_REF"), ("ids numériques", "E_REF"), ("introuvable", "E_NOT_FOUND"), ("inconnu", "E_NOT_FOUND"),
    ("ambigu", "E_AMBIGUOUS"), ("plusieurs", "E_AMBIGUOUS"), ("accept", "E_ACCEPT"), ("non appliqué", "E_NOT_APPLIED"),
    ("relecture", "E_VERIFY"), ("hors", "E_RANGE"), ("quantifié", "E_RANGE"), ("trop de points", "E_LIMIT"),
    ("invalide", "E_INVALID"), ("non fini", "E_INVALID"), ("négatif", "E_INVALID"), ("disparu", "E_STALE"),
)
def error_code(msg):
    m = str(msg)
    for needle, code in ERROR_CODES:
        if needle in m: return code
    return "E_ERROR"

JOURNAL_CMDS = ("/shape", "/clear", "/setparam", "/restore", "/locator", "/transport")   # commandes qui modifient le Set : journalisées
JOURNAL_MAX_ROWS = 40

def check_points_exact(pts, eps=VERIFY_EPS, limit=VERIFY_MAX_CHECKS):
    """Instants de contrôle d'une enveloppe exposée : de part et d'autre de chaque point (marches comprises) et au milieu
    de chaque segment ; [(t, valeur attendue)], au plus `limit` instants répartis uniformément."""
    times = sorted(set(t for t, _ in pts))
    if not times: return []
    out = []
    for i, t in enumerate(times):
        if i > 0: out.append(t - eps)
        if i < len(times) - 1: out.append(t + eps); out.append((t + times[i + 1]) / 2.0)
    if not out: out = [times[0]]
    if len(out) > limit: out = [out[int(k * (len(out) - 1) / (limit - 1))] for k in range(limit)]
    return [(t, interp(pts, _ident, t)) for t in out]

def check_points_sampled(pts, lo, hi, s, e, rel, step=VERIFY_STEP):
    """Instants de contrôle par curseur (enveloppe non exposée), en temps ABSOLU : près des deux bords et au milieu de la
    fenêtre [lo, hi], plus un ancrage juste avant / juste après quand la fenêtre ne touche pas le bord du clip [s, e].
    `pts` est l'enveloppe attendue en temps relatif, `rel` convertit absolu → relatif ; [(t_abs, valeur attendue)]."""
    d = min(step, (hi - lo) / 4.0)
    times = [lo + d, (lo + hi) / 2.0, hi - d]
    if lo - d > s + 1e-9: times.insert(0, lo - d)
    if hi + d < e - 1e-9: times.append(hi + d)
    return [(t, interp(pts, _ident, rel(t))) for t in times]


class RebuildMismatch(Exception):
    """Le clip a été remplacé mais ne correspond pas à l'original : l'appelant annule l'étape."""


class LOMBridge(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self._id2obj, self._ptr2ref, self._next_id = {}, {}, 1
        self._session_id = "%d" % random.randint(100000, 999999)
        self._jobs = []
        self._tok = None
        self._sock = None
        self._token()   # fichier de connexion écrit dès l'init
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(("127.0.0.1", RX_PORT)); s.setblocking(False)
            self._sock = s
            self.log_message("LOMBridge %s : UDP 127.0.0.1:%d, session %s" % (VERSION, RX_PORT, self._session_id))
            self.show_message("LOM Bridge %s prêt (UDP %d, session %s)" % (VERSION, RX_PORT, self._session_id))
        except Exception as e:
            self.log_message("LOMBridge : bind impossible : %s" % e)
            self.show_message("LOM Bridge : port %d indisponible" % RX_PORT)

    def disconnect(self):
        try:
            if self._sock: self._sock.close()
        except Exception: pass
        ControlSurface.disconnect(self)

    def update_display(self):
        ControlSurface.update_display(self)
        self._job_tick()
        self._poll()

    # ---------- session / jeton ----------
    def _session(self):
        if not getattr(self, "_session_id", None): self._session_id = "%d" % random.randint(100000, 999999)
        return self._session_id

    def _token(self):
        tok = getattr(self, "_tok", None)
        if tok: return tok
        try: tok = json.load(open(CONN_FILE)).get("token") if os.path.exists(CONN_FILE) else None
        except Exception: tok = None
        if not tok: tok = "%032x" % random.getrandbits(128)
        try:
            d = os.path.dirname(CONN_FILE); os.makedirs(d, exist_ok=True); os.chmod(d, 0o700)
            with open(CONN_FILE, "w") as f: json.dump({"port": RX_PORT, "token": tok, "session": self._session(), "version": VERSION}, f)
            os.chmod(CONN_FILE, 0o600)
        except Exception as e: self.log_message("LOMBridge: fichier de connexion impossible: %s" % e)
        self._tok = tok
        return tok

    # ---------- réseau ----------
    def _send(self, addr, path, *args):
        flat = []
        for a in args:
            if isinstance(a, (list, tuple)): flat.extend(a)
            else: flat.append(a)
        try: self._sock.sendto(osc_pack(path, flat), addr)
        except Exception as e: self.log_message("LOMBridge send: %s" % e)

    def _poll(self):
        if not self._sock: return
        for _ in range(200):
            try: data, addr = self._sock.recvfrom(65536)
            except (BlockingIOError, OSError): return
            if addr[0] != "127.0.0.1": continue
            try: cmd, args = osc_unpack(data)
            except Exception as e:
                self._send(addr, "/err", "", "OSC invalide: %s" % e); continue
            rid = ""
            if args and isinstance(args[-1], str) and args[-1].startswith("#"): rid = args[-1][1:]; args = args[:-1]
            tok = None
            if args and isinstance(args[-1], str) and args[-1].startswith("!"): tok = args[-1][1:]; args = args[:-1]
            if tok != self._token():
                self._send(addr, "/begin", rid, cmd); self._fail(addr, rid, "jeton absent ou invalide (lire %s)" % CONN_FILE); self._send(addr, "/end", rid, cmd); continue
            self._dispatch(addr, cmd, args, rid)

    def _fail(self, addr, rid, msg):
        """/err <id> <code> <texte> : le code est stable (E_…), le texte est pour l'humain."""
        self._send(addr, "/err", rid, error_code(msg), str(msg))

    # ---------- journal des écritures ----------
    def _journal_path(self): return os.path.join(os.path.dirname(CONN_FILE), "journal.jsonl")

    def _journal(self, job, error=None):
        """Une ligne JSON par commande qui modifie le Set : quand, quoi (commande, arguments), résultat (lignes) ou erreur."""
        if job["cmd"] not in JOURNAL_CMDS: return
        import time
        entry = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "session": self._session(), "version": VERSION, "rid": job["rid"], "cmd": job["cmd"],
                 "args": [str(x)[:120] for x in job["args"]][:60], "ok": error is None, "rows": job["rows"][:JOURNAL_MAX_ROWS]}
        if error is not None: entry["error"] = str(error)[:500]; entry["code"] = error_code(error)
        try:
            with open(self._journal_path(), "a", encoding="utf-8") as f: f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception as e: self.log_message("LOMBridge journal: %s" % e)

    def _dispatch(self, addr, cmd, args, rid=""):
        self._send(addr, "/begin", rid, cmd)
        job = {"addr": addr, "cmd": cmd, "rid": rid, "args": list(args), "rows": [], "cancel": False, "started": False}
        def reply(*a):
            job["rows"].append([str(x) if not isinstance(x, (int, float)) else x for x in a]); self._send(addr, "/r", rid, *a)
        try:
            h = getattr(self, "cmd_" + cmd.strip("/").replace("-", "_"), None)
            if h is None or not cmd.startswith("/"): raise ValueError("commande inconnue " + cmd)
            r = h(reply, list(args))
            if hasattr(r, "__next__"):
                if len(self._jobs) >= MAX_JOBS: r.close(); raise ValueError("file de tâches pleine (%d) : attendre ou /cancel" % MAX_JOBS)
                job["gen"] = r; self._jobs.append(job); return
            self._journal(job)
        except Exception as e:
            self._fail(addr, rid, "%s: %s" % (cmd, e)); self._journal(job, e)
            self.log_message("LOMBridge %s: %s\n%s" % (cmd, e, traceback.format_exc()))
        self._send(addr, "/end", rid, cmd)

    # ---------- tâches asynchrones ----------
    def _job_tick(self):
        jobs = getattr(self, "_jobs", None)
        if not jobs: return
        job = jobs[0]; gen, addr, cmd, rid = job["gen"], job["addr"], job["cmd"], job["rid"]
        if job["cancel"]:
            # la tâche en cours décide elle-même comment s'arrêter à sa prochaine pause (_sample_at lit le drapeau) : en phase de
            # lecture elle abandonne sans rien modifier, en relecture elle termine en signalant « interrupted » ; sécurité si elle
            # ne réagit pas dans les CANCEL_GRACE_TICKS : fermeture forcée
            job["cancel_ticks"] = job.get("cancel_ticks", 0) + 1
            if job["cancel_ticks"] > CANCEL_GRACE_TICKS:
                jobs.pop(0)
                try: gen.close()
                except Exception as e: self.log_message("LOMBridge cancel %s: %s" % (cmd, e))
                self._fail(addr, rid, "%s: annulée (fermeture forcée)" % cmd); self._journal(job, "annulée (fermeture forcée)"); self._send(addr, "/end", rid, cmd); return
        job["started"] = True
        try: next(gen)
        except StopIteration:
            jobs.pop(0); self._journal(job); self._send(addr, "/end", rid, cmd)
        except Exception as e:
            jobs.pop(0); self._fail(addr, rid, "%s: %s" % (cmd, e)); self._journal(job, e); self._send(addr, "/end", rid, cmd)
            self.log_message("LOMBridge job %s: %s\n%s" % (cmd, e, traceback.format_exc()))

    def _cancel_requested(self):
        jobs = getattr(self, "_jobs", None)
        return bool(jobs) and jobs[0]["cancel"]

    def _sample_at(self, params, times, out):
        """Générateur : lit la valeur réelle des paramètres aux instants donnés en déplaçant le curseur (transport arrêté),
        puis le restaure. Abandon si transport démarré, curseur déplacé par un tiers, ou annulation."""
        times = [float(t) for t in times]
        if not times: return
        if any(not math.isfinite(t) or t < 0 for t in times): raise ValueError("instant d'échantillonnage invalide")
        song = self.song()
        if song.is_playing: raise ValueError("lecture en cours : arrêter le transport (l'échantillonnage déplace le curseur)")
        saved = float(song.current_song_time)
        try:
            for tt in times:
                song.current_song_time = tt; yield
                if self._cancel_requested(): raise ValueError("annulée")
                if song.is_playing: raise ValueError("transport démarré pendant l'échantillonnage : abandon")
                if abs(float(song.current_song_time) - tt) > 1e-3: raise ValueError("curseur déplacé pendant l'échantillonnage : abandon")
                for i, p in enumerate(params): out.setdefault(i, []).append((round(tt, 6), float(p.value)))
        finally:
            try: song.current_song_time = saved
            except Exception: pass

    def _sample(self, params, t0, t1, step, out):
        """Générateur : échantillonne de t0 à t1 au pas `step`, dernier échantillon exactement sur t1."""
        if not (step > 0) or not math.isfinite(step): raise ValueError("pas d'échantillonnage invalide")
        if t1 < t0: raise ValueError("plage inversée")
        if t0 < 0: raise ValueError("temps négatif")
        times, tt = [t0], t0
        while tt < t1 - 1e-9:
            tt = min(tt + step, t1); times.append(tt)
        for _ in self._sample_at(params, times, out): yield

    # ---------- transaction (écriture d'un bloc, défaite sur erreur) ----------
    def _commit(self, song, write):
        """Exécute write(touched) dans UNE étape d'annulation, sans pause. `touched` reçoit le nom de chaque clip effectivement
        remplacé. Sur erreur : rien de remplacé → l'erreur remonte telle quelle ; sinon l'étape est défaite (song.undo)."""
        touched, failure = [], None
        song.begin_undo_step()
        try: result = write(touched)
        except Exception as e: failure = e
        finally: song.end_undo_step()
        if failure is None: return result
        if not touched: raise ValueError("%s ; rien n'est modifié" % failure) from failure
        try: song.undo()
        except Exception as e2: raise ValueError("%s après %d clip(s) remplacé(s) ; ANNULATION AUTOMATIQUE IMPOSSIBLE (%s) : faire Cmd+Z" % (failure, len(touched), e2)) from failure
        raise ValueError("%s ; étape annulée automatiquement (%d clip(s) remis), rien n'est modifié" % (failure, len(touched))) from failure

    def _revalidate(self, track, entries, p, accept):
        """Contrôle que les clips visés (entrées de plan : ref, name, start, end) sont toujours là, au même endroit, et
        toujours reconstructibles, et que le paramètre existe. [(clip, début, fin, entrée)] dans l'ordre des entrées."""
        live_clips = dict((getattr(c, "_live_ptr", id(c)), (c, s, e)) for c, s, e in self._arr_clips(track))
        targets = []
        for entry in entries:
            c = self._obj(entry["ref"]); key = getattr(c, "_live_ptr", id(c))
            if key not in live_clips: raise ValueError("clip %s disparu depuis le plan : replanifier" % entry["name"])
            c, s, e = live_clips[key]
            if abs(s - entry["start"]) > 1e-6 or abs(e - entry["end"]) > 1e-6: raise ValueError("clip %s déplacé depuis le plan : replanifier" % entry["name"])
            fatal, need = self._check_clip(c, accept)
            if fatal or need: raise ValueError("clip %s : " % entry["name"] + " ; ".join(fatal + need))
            targets.append((c, s, e, entry))
        try: float(p.value)
        except Exception: raise ValueError("paramètre disparu : replanifier")
        return targets

    def _verify(self, song, p, done, reply, warnings):
        """Générateur : relit l'automation écrite (done = [(clip reconstruit, lo, hi, points relatifs attendus)]) et compare.
        Enveloppe exposée → relecture exacte, immédiate ; sinon → quelques points par curseur. Écart > tolérance → étape défaite.
        Relecture interrompue (transport, annulation) → avertissement, l'écriture reste."""
        tol = VERIFY_TOL * max(1e-9, float(p.max) - float(p.min))
        n, worst, method = 0, (0.0, None), "exact"
        try:
            for nc, lo, hi, pts in done:
                ev = self._env_of(nc, p)
                if ev is not None:
                    for t_rel, exp in check_points_exact(pts):
                        dev = abs(float(ev.value_at_time(t_rel)) - exp); n += 1
                        if dev > worst[0]: worst = (dev, t_rel - float(nc.start_marker) + float(nc.start_time))
                else:
                    method = "sampled"
                    checks = check_points_sampled(pts, lo, hi, float(nc.start_time), float(nc.end_time), lambda t: self._rel(nc, t))
                    got = {}
                    for _ in self._sample_at([p], [t for t, _ in checks], got): yield
                    for (t_abs, exp), (_, v) in zip(checks, got.get(0, [])):
                        dev = abs(v - exp); n += 1
                        if dev > worst[0]: worst = (dev, t_abs)
        except ValueError as e:
            warnings.append("écrit mais relecture interrompue (%s) : contrôler avec /read" % e)
            reply("verified", n, round(worst[0], 6), round(tol, 6), "interrupted"); return
        if worst[0] > tol:
            msg = "relecture : écart %.5f > tolérance %.5f à t=%.3f (%s)" % (worst[0], tol, worst[1], method)
            try: song.undo()
            except Exception as e2: raise ValueError("%s ; ANNULATION AUTOMATIQUE IMPOSSIBLE (%s) : faire Cmd+Z" % (msg, e2))
            raise ValueError("%s ; étape annulée automatiquement, rien n'est modifié" % msg)
        reply("verified", n, round(worst[0], 6), round(tol, 6), method)

    # ---------- références ----------
    def _ref(self, obj):
        ptr = getattr(obj, "_live_ptr", None)
        if ptr is None: ptr = id(obj)
        if ptr in self._ptr2ref:
            self._id2obj[self._ptr2ref[ptr]] = obj
            return self._ptr2ref[ptr]
        r = "o:%s:%d" % (self._session(), self._next_id); self._next_id += 1
        self._ptr2ref[ptr] = r; self._id2obj[r] = obj
        return r

    def _obj(self, ref):
        ref = str(ref)
        m = re.match(r"^o:(\d+):(\d+)$", ref)
        if not m: raise ValueError("référence attendue (o:session:n) : %r" % ref)
        if m.group(1) != self._session(): raise ValueError("référence d'une autre session (%s ≠ %s) : relire les objets" % (m.group(1), self._session()))
        if ref not in self._id2obj: raise ValueError("référence inconnue %s (relire l'objet)" % ref)
        return self._id2obj[ref]

    def _is_live_obj(self, v):
        return hasattr(v, "_live_ptr") or type(v).__module__.startswith("Live")

    def _conv(self, v):
        if v is None: return "None"
        if isinstance(v, bool): return int(v)
        if isinstance(v, (int, float, str)): return v
        if isinstance(v, bytes): return v.decode("utf-8", "replace")
        if self._is_live_obj(v) and not hasattr(v, "__len__"): return self._ref(v)
        try: return [self._conv(x) for x in v]
        except TypeError: return self._ref(v)

    def _resolve(self, ref):
        s = str(ref).strip().strip('"')
        if s.startswith("o:"): return self._obj(s)
        if re.match(r"^(id\s+)?\d+$", s): raise ValueError("les ids numériques ne sont plus acceptés : utiliser une référence o:session:n")
        return self._path(s)

    def _path(self, s):
        toks = s.split(); root = toks[0]
        if root == "live_set": obj = self.song()
        elif root == "live_app": obj = Live.Application.get_application()
        else: raise ValueError("racine inconnue: " + root)
        i = 1
        while i < len(toks):
            t = toks[i]; i += 1
            if not hasattr(obj, t): raise ValueError("pas de propriété « %s » sur %s" % (t, type(obj).__name__))
            obj = getattr(obj, t)
            if i < len(toks) and re.match(r"^-?\d+$", toks[i]): obj = obj[int(toks[i])]; i += 1
        return obj

    def _arg(self, a):
        if isinstance(a, str) and a.startswith("o:"): return self._obj(a)
        return a

    # ---------- pistes / paramètres (résolution non ambiguë) ----------
    def _find_track(self, ref):
        if isinstance(ref, str) and ref.startswith("o:"): return self._obj(ref)
        name = str(ref); l = name.lower(); song = self.song()
        if l in ("master", "main"): return song.master_track
        cands = list(song.tracks) + list(song.return_tracks)
        exact = [t for t in cands if str(t.name).lower() == l]
        if len(exact) == 1: return exact[0]
        if len(exact) > 1: raise ValueError("plusieurs pistes nommées « %s » : utiliser la référence" % name)
        subs = [t for t in cands if l in str(t.name).lower()]
        if len(subs) == 1: return subs[0]
        if len(subs) > 1: raise ValueError("piste ambiguë « %s » : %s" % (name, ", ".join(str(t.name) for t in subs[:8])))
        raise ValueError("piste introuvable: " + name)

    def _find_named(self, items, key, what):
        k = str(key).lower()
        exact = [x for x in items if str(x.name).lower() == k]
        if len(exact) == 1: return exact[0]
        if len(exact) > 1: raise ValueError("plusieurs %s nommés « %s »" % (what, key))
        if re.match(r"^\d+$", k) and int(k) < len(items): return items[int(k)]
        subs = [x for x in items if k in str(x.name).lower()]
        if len(subs) == 1: return subs[0]
        if len(subs) > 1: raise ValueError("%s ambigu « %s » : %s" % (what, key, ", ".join(str(x.name) for x in subs[:8])))
        raise ValueError("%s introuvable: %s" % (what, key))

    def _find_param(self, track, dev_ref, param_ref):
        dn = str(dev_ref).lower(); pn = str(param_ref).lower()
        if dn == "mixer":
            mix = track.mixer_device
            if pn in ("volume", "vol"): return mix.volume
            if pn in ("pan", "panning"): return mix.panning
            m = re.match(r"^send\s*([a-l])$", pn)
            if m: return mix.sends[ord(m.group(1)) - 97]
            raise ValueError("param mixer inconnu: " + str(param_ref))
        dev = self._obj(dev_ref) if str(dev_ref).startswith("o:") else self._find_named(list(track.devices), dev_ref, "device")
        if str(param_ref).startswith("o:"): return self._obj(param_ref)
        return self._find_named(list(dev.parameters), param_ref, "paramètre")

    def _solve(self, p, target):
        """(valeur normalisée, saturé?) pour une valeur d'affichage."""
        if not math.isfinite(target): raise ValueError("valeur non finie")
        mn, mx = float(p.min), float(p.max)
        f = lambda x: parse_disp(p.str_for_value(x))
        flo, fhi = f(mn), f(mx)
        if (not math.isfinite(flo) and flo != -float("inf")) or not math.isfinite(fhi):
            raise ValueError("affichage non numérique pour %s (%r / %r) : utiliser unit=raw" % (p.name, p.str_for_value(mn), p.str_for_value(mx)))
        inc = fhi > flo
        if target <= min(flo, fhi): return (mn if inc else mx), target < min(flo, fhi)
        if target >= max(flo, fhi): return (mx if inc else mn), target > max(flo, fhi)
        lo, hi = mn, mx
        for _ in range(60):
            mid = (lo + hi) / 2; fm = f(mid)
            if (fm < target) == inc: lo = mid
            else: hi = mid
        x = (lo + hi) / 2; got = f(x)
        if not math.isfinite(got) or abs(got - target) > max(0.02 * abs(target), 0.6):   # 0.6 : arrondi d'affichage entier (« 44 % » pour 45)
            raise ValueError("résolution impossible pour %s : demandé %g, obtenu %r" % (p.name, target, p.str_for_value(x)))
        return x, False

    # ---------- clips / enveloppes ----------
    def _arr_clips(self, track):
        cs = [(c, float(c.start_time), float(c.end_time)) for c in track.arrangement_clips]
        cs.sort(key=lambda x: x[1]); return cs

    def _clip_at(self, clips, t):
        for c in clips:
            if c[1] <= t < c[2]: return c
        return None

    def _env_of(self, clip, param):
        pp = getattr(param, "_live_ptr", None)
        for ev in clip.automation_envelopes:
            try:
                q = ev.parameter
                if q == param or (pp is not None and getattr(q, "_live_ptr", None) == pp): return ev
            except Exception: pass
        return None

    def _sample_env(self, ev, lo, hi):
        out, prev = [], None
        for x in ev.events_in_range(lo, hi):
            tt = x.time + (1e-5 if prev is not None and abs(prev - x.time) < 1e-9 else 0.0)
            out.append((float(x.time), float(ev.value_at_time(tt)))); prev = x.time
        return out

    def _rel(self, clip, t_abs): return t_abs - float(clip.start_time) + float(clip.start_marker)

    def _free_slot(self, track):
        """(slot libre, index de scène créée ou None)."""
        for s in track.clip_slots:
            if not s.has_clip and not getattr(s, "is_group_slot", False): return s, None
        song = self.song(); song.create_scene(-1)
        idx = len(song.scenes) - 1
        return track.clip_slots[idx], idx

    def _check_clip(self, clip, accept):
        """(fatal[], refus sans acceptation[]) pour la reconstruction d'un clip."""
        fatal, need = [], []
        name = str(getattr(clip, "name", "?"))
        try:
            if getattr(clip, "is_take_lane_clip", False): fatal.append("%s : clip de take lane" % name)
            if getattr(clip, "is_recording", False): fatal.append("%s : en enregistrement" % name)
            length = float(clip.end_time) - float(clip.start_time)
            if clip.looping:
                loop = float(clip.loop_end) - float(clip.loop_start)
                if length > loop + 1e-6: fatal.append("%s : clip bouclé étiré (%.2f > boucle %.2f), non reproductible" % (name, length, loop))
            if clip.is_audio_clip:
                if not clip.file_path: fatal.append("%s : clip audio sans fichier" % name)
                if "fades" not in accept: need.append("%s : clip audio, fondus non recopiables (accept=fades)" % name)
            else:
                if "expressions" not in accept: need.append("%s : clip MIDI, expressions de notes (MPE) non recopiables (accept=expressions)" % name)
        except Exception as e: fatal.append("%s : contrôle impossible (%s)" % (name, e))
        return fatal, need

    def _rebuild(self, track, clip, env_specs, warnings, accept, touched=None):
        """Reconstruit le clip d'arrangement depuis la session avec les enveloppes demandées. Nettoie sur erreur.
        `touched` (liste) reçoit le nom du clip dès que l'original a été remplacé dans l'arrangement."""
        E = Live.Envelope.EnvelopeEvent
        song = self.song()
        old_start, old_end = float(clip.start_time), float(clip.end_time)
        slot, scene_idx = self._free_slot(track)
        n = None
        try:
            if clip.is_audio_clip:
                n = slot.create_audio_clip(clip.file_path)
                for prop in ("warping", "warp_mode", "gain", "pitch_coarse", "pitch_fine", "ram_mode"):
                    try: setattr(n, prop, getattr(clip, prop))
                    except Exception as e: warnings.append("%s: %s" % (prop, e))
                old_m = [(round(m.sample_time, 5), round(m.beat_time, 5)) for m in clip.warp_markers]
                new_m = [(round(m.sample_time, 5), round(m.beat_time, 5)) for m in n.warp_markers]
                if old_m != new_m:
                    try:
                        W = Live.Clip.WarpMarker
                        for m in list(n.warp_markers):
                            try: n.remove_warp_marker(m)
                            except Exception: pass
                        for st, bt in old_m: n.add_warp_marker(W(st, bt))
                        got = [(round(m.sample_time, 5), round(m.beat_time, 5)) for m in n.warp_markers]
                        if got != old_m: raise ValueError("marqueurs obtenus %s ≠ attendus %s" % (got, old_m))
                    except Exception as e:
                        if "warp" not in accept: raise ValueError("%s : warp personnalisé non reproductible (%s) ; accept=warp pour passer outre" % (clip.name, e))
                        warnings.append("%s : warp personnalisé non recopié (%s)" % (clip.name, e))
            else:
                length = max(float(clip.end_marker), float(clip.loop_end), float(clip.length), 0.25)   # ligne de temps complète (start_marker peut être 420)
                n = slot.create_clip(length)
                N = Live.Clip.MidiNoteSpecification
                notes = clip.get_all_notes_extended()
                specs = []
                for x in notes:
                    kw = dict(pitch=x.pitch, start_time=x.start_time, duration=x.duration, velocity=x.velocity, mute=x.mute)
                    for extra in ("probability", "velocity_deviation", "release_velocity"):
                        if hasattr(x, extra): kw[extra] = getattr(x, extra)
                    specs.append(N(**kw))
                if specs: n.add_new_notes(tuple(specs))
                if len(n.get_all_notes_extended()) != len(notes): raise ValueError("%s : %d notes recopiées sur %d" % (clip.name, len(n.get_all_notes_extended()), len(notes)))
            marker_errors = []
            for prop in ("looping", "end_marker", "loop_end", "start_marker", "loop_start"):
                try: setattr(n, prop, getattr(clip, prop))
                except Exception as e: marker_errors.append("%s: %s" % (prop, e))
            for prop in ("start_marker", "end_marker", "loop_start", "loop_end"):
                if abs(float(getattr(n, prop)) - float(getattr(clip, prop))) > 1e-6: marker_errors.append("%s attendu %s obtenu %s" % (prop, getattr(clip, prop), getattr(n, prop)))
            if marker_errors: raise ValueError("%s : marqueurs non reproductibles (%s)" % (clip.name, " ; ".join(marker_errors)))
            for prop in ("name", "color", "signature_numerator", "signature_denominator", "launch_mode", "launch_quantization", "legato", "velocity_amount", "muted"):
                try: setattr(n, prop, getattr(clip, prop))
                except Exception: pass
            spec_by_ptr = {}
            for p, pts in env_specs: spec_by_ptr[getattr(p, "_live_ptr", id(p))] = (p, pts)
            done = set()
            for ev in clip.automation_envelopes:
                p = ev.parameter; key = getattr(p, "_live_ptr", id(p))
                try: e2 = n.create_automation_envelope(p)
                except Exception as e: warnings.append("enveloppe %s: %s" % (p.name, e)); continue
                if key in spec_by_ptr: pts = spec_by_ptr[key][1]; done.add(key)
                else: pts = self._sample_env(ev, -1e6, 1e6)
                for t_rel, v in sorted(pts, key=lambda x: x[0]): e2.create_event(E(float(t_rel), float(v)))
            for key, (p, pts) in spec_by_ptr.items():
                if key in done: continue
                e2 = n.create_automation_envelope(p)
                for t_rel, v in sorted(pts, key=lambda x: x[0]): e2.create_event(E(float(t_rel), float(v)))
            new_clip = track.duplicate_clip_to_arrangement(n, old_start)
            if touched is not None: touched.append(str(clip.name))
        except Exception:
            try:
                if n is not None: slot.delete_clip()
            except Exception: pass
            try:
                if scene_idx is not None: song.delete_scene(scene_idx)
            except Exception: pass
            raise
        try: slot.delete_clip()
        except Exception: pass
        try:
            if scene_idx is not None: song.delete_scene(scene_idx)
        except Exception: pass
        ns, ne = float(new_clip.start_time), float(new_clip.end_time)
        if abs(ns - old_start) > 1e-6 or abs(ne - old_end) > 1e-6:
            raise RebuildMismatch("%s : clip reconstruit %.3f-%.3f au lieu de %.3f-%.3f" % (clip.name, ns, ne, old_start, old_end))
        return new_clip

    def _old_points(self, clip, p, win_abs, out):
        """Générateur : anciens points hors fenêtre, en temps relatif, avec ancrages exacts sur lo et hi."""
        s, e = float(clip.start_time), float(clip.end_time)
        lo_abs, hi_abs = max(win_abs[0], s), min(win_abs[1], e)
        lo, hi = self._rel(clip, lo_abs), self._rel(clip, hi_abs)
        before, after = [], []
        ev = self._env_of(clip, p)
        if ev is not None:
            pts = self._sample_env(ev, -1e6, 1e6)
            before = [x for x in pts if x[0] < lo - 1e-9]
            after = [x for x in pts if x[0] > hi + 1e-9]
            if lo_abs > s + 1e-9: before.append((lo, float(ev.value_at_time(lo - 1e-6))))
            if hi_abs < e - 1e-9: after.insert(0, (hi, float(ev.value_at_time(hi + 1e-6))))
        elif int(getattr(p, "automation_state", 0)) != 0:
            if int(getattr(p, "automation_state", 0)) == 2: raise ValueError(self._override_msg(p))
            if lo_abs > s + 1e-9:
                got = {}
                for _ in self._sample([p], s, lo_abs, SAMPLE_STEP, got): yield
                before = [(self._rel(clip, t), v) for t, v in simplify(got.get(0, []))]
            if hi_abs < e - 1e-9:
                got = {}
                for _ in self._sample([p], hi_abs, e - 1e-3, SAMPLE_STEP, got): yield
                after = [(self._rel(clip, t), v) for t, v in simplify(got.get(0, []))]
        out["before"] = before; out["after"] = after

    # ---------- plan (commun à /plan et /shape) ----------
    def _override_msg(self, p):
        return ("automation de %s surchargée (valeur modifiée à la main, état 2) : l'échantillonnage lirait la valeur manuelle et "
                "non l'automation ; réactiver l'automation dans Live (ou song.re_enable_automation()) puis replanifier" % p.name)

    def _parse_accept(self, s):
        acc = set(x.strip() for x in str(s or "").split(",") if x.strip() and x.strip() != "-")
        bad = acc - set(ACCEPT_KEYS)
        if bad: raise ValueError("accept inconnu : %s (valides : %s)" % (", ".join(sorted(bad)), ", ".join(ACCEPT_KEYS)))
        return acc

    def _build_plan(self, a):
        """/plan|/shape <piste> <paramRef> <raw|disp> <res> <courbe> <hold> <accept> t0 v0 [t1 v1 ...]"""
        if len(a) < 9 or (len(a) - 7) % 2: raise ValueError("usage: <piste> <paramRef> <raw|disp> <res> <courbe> <hold> <accept|-> t0 v0 [t1 v1 ...]")
        track = self._find_track(a[0]); p = self._resolve(a[1]); unit = str(a[2]); res = float(a[3]); curve = a[4]; hold = int(a[5]); accept = self._parse_accept(a[6])
        if unit not in ("raw", "disp"): raise ValueError("unité inconnue: " + unit)
        if not (0 < res <= 64) or not math.isfinite(res): raise ValueError("res doit être dans ]0, 64]")
        if int(getattr(p, "is_quantized", 0)) and unit != "raw": raise ValueError("paramètre quantifié : unit=raw avec valeurs entières")
        mn, mx = float(p.min), float(p.max)
        plan = {"version": VERSION, "session": self._session(), "track": {"ref": self._ref(track), "name": str(track.name)},
                "param": {"ref": self._ref(p), "name": str(p.name), "min": mn, "max": mx, "quantized": int(getattr(p, "is_quantized", 0))},
                "unit": unit, "res": res, "curve": str(curve), "hold": hold, "accept": sorted(accept),
                "points": [], "clips": [], "errors": [], "warnings": [], "n_points": 0, "sampling_seconds": 0.0}
        raw = []
        for i in range(7, len(a) - 1, 2):
            tt, vv = float(a[i]), float(a[i + 1])
            if not (math.isfinite(tt) and math.isfinite(vv)): plan["errors"].append("temps ou valeur non fini à l'index %d" % i); continue
            if tt < 0: plan["errors"].append("temps négatif: %g" % tt); continue
            clamped = False
            if unit == "raw":
                r = vv
                if r < mn or r > mx:
                    if "clamp" in accept: r = min(max(r, mn), mx); clamped = True
                    else: plan["errors"].append("valeur brute %g hors [%g, %g] à t=%g (accept=clamp pour saturer)" % (vv, mn, mx, tt)); continue
            else:
                try: r, clamped = self._solve(p, vv)
                except Exception as e: plan["errors"].append(str(e)); continue
                if clamped and "clamp" not in accept: plan["errors"].append("valeur %g hors plage affichable à t=%g : saturée à %r (accept=clamp pour l'admettre)" % (vv, tt, p.str_for_value(r))); continue
            if clamped: plan["warnings"].append("t=%g : valeur %g saturée à %r" % (tt, vv, p.str_for_value(r)))
            plan["points"].append({"t": tt, "in": vv, "raw": r, "display": str(p.str_for_value(r)), "clamped": int(clamped)})
            raw.append((tt, r))
        if not raw: plan["errors"].append("aucun point valide"); return plan
        pts = sorted(raw, key=lambda x: x[0])
        clips = self._arr_clips(track)
        if not clips: plan["errors"].append("aucun clip d'arrangement sur la piste"); return plan
        t_lo, t_hi = pts[0][0], pts[-1][0]
        if hold:
            lc = self._clip_at(clips, t_hi)
            if lc and lc[2] > t_hi + 1e-9: t_hi = lc[2]; pts = pts + [(t_hi, pts[-1][1])]
            else: plan["warnings"].append("hold sans effet : aucun clip après %g" % t_hi)
        if t_hi - t_lo < 1e-9: plan["errors"].append("fenêtre de durée nulle : donner deux temps distincts ou hold=1"); return plan
        plan["t_lo"], plan["t_hi"] = t_lo, t_hi
        n_est = count_breakpoints(pts, res, is_linear(curve))
        plan["n_points"] = n_est
        if n_est > MAX_SHAPE_POINTS: plan["errors"].append("trop de points (%d > %d) : réduire res" % (n_est, MAX_SHAPE_POINTS)); return plan
        covered = 0.0; total_sampling = 0.0; total_verify = 0.0
        state = int(getattr(p, "automation_state", 0))
        for c, s, e in clips:
            if e <= t_lo or s >= t_hi: continue
            lo, hi = max(t_lo, s), min(t_hi, e)
            fatal, need = self._check_clip(c, accept)
            exposes = self._env_of(c, p) is not None
            samp = 0.0
            if not exposes and state != 0:
                if state == 2: fatal.append(self._override_msg(p))
                samp = ((max(0.0, lo - s) + max(0.0, e - hi)) / SAMPLE_STEP + 2) * TICK_SECONDS
            # relecture de contrôle : le clip MIDI reconstruit expose son enveloppe (exact, immédiat) ; l'audio jamais (5 points par curseur)
            verify = 0.0 if "unverified" in accept else (5 * TICK_SECONDS if c.is_audio_clip else 0.0)
            entry = {"ref": self._ref(c), "name": str(c.name), "start": s, "end": e, "window": [lo, hi], "audio": int(c.is_audio_clip), "start_marker": float(c.start_marker), "end_marker": float(c.end_marker),
                     "exposes_envelope": int(exposes), "sampling": int(bool(samp)), "sampling_seconds": round(samp, 1), "verify_seconds": round(verify, 1), "problems": fatal + need}
            plan["clips"].append(entry); covered += hi - lo; total_sampling += samp; total_verify += verify
            for x in fatal: plan["errors"].append(x)
            for x in need: plan["errors"].append(x)
        if not plan["clips"]: plan["errors"].append("aucun clip ne couvre la plage %g-%g" % (t_lo, t_hi))
        gap = max(0.0, (t_hi - t_lo) - covered); plan["gap"] = round(gap, 4); plan["sampling_seconds"] = round(total_sampling, 1)
        plan["verify"] = int("unverified" not in accept); plan["verify_seconds"] = round(total_verify, 1)
        if gap > 1e-3: plan["warnings"].append("%.2f temps de la plage ne sont couverts par aucun clip" % gap)
        plan["_pts"] = pts
        return plan

    def _plan_rows(self, reply, plan):
        pub = dict((k, v) for k, v in plan.items() if not k.startswith("_"))
        reply("plan", json.dumps(pub, ensure_ascii=False))
        for c in plan["clips"]: reply("clip", c["ref"], c["name"], c["start"], c["end"], c["window"][0], c["window"][1], "sampling" if c["sampling"] else "exact", " ; ".join(c["problems"]))
        for w in plan["warnings"]: reply("warn", w)
        for e in plan["errors"]: reply("error", e)

    def cmd_plan(self, reply, a):
        plan = self._build_plan(a); self._plan_rows(reply, plan)
        reply("ok" if not plan["errors"] else "invalid", len(plan["clips"]), plan["n_points"], plan.get("gap", 0), plan["sampling_seconds"])

    def cmd_shape(self, reply, a):
        plan = self._build_plan(a)
        if plan["errors"]:
            self._plan_rows(reply, plan); raise ValueError("plan invalide : " + " ; ".join(plan["errors"]))
        track = self._obj(plan["track"]["ref"]); p = self._obj(plan["param"]["ref"]); pts = plan["_pts"]
        cf = curve_fn(plan["curve"]); linear = is_linear(plan["curve"]); accept = set(plan["accept"])
        bps = breakpoints(pts, cf, plan["res"], linear)
        t_lo, t_hi = plan["t_lo"], plan["t_hi"]
        def job():
            song = self.song(); warnings = list(plan["warnings"])
            # revalidation au démarrage effectif de la tâche
            targets = self._revalidate(track, plan["clips"], p, accept)
            if plan["sampling_seconds"] > 0 and song.is_playing: raise ValueError("lecture en cours : arrêter le transport (échantillonnage nécessaire)")
            # phase 1 : lecture de l'existant (peut prendre du temps ; rien n'est modifié, aucune étape d'annulation ouverte)
            work = []
            for c, s, e, entry in targets:
                if self._cancel_requested(): raise ValueError("annulée")
                lo, hi = max(t_lo, s), min(t_hi, e)
                old = {}
                for _ in self._old_points(c, p, (lo, hi), old): yield
                new = [(self._rel(c, lo), interp(pts, cf, lo, "right"))]
                new += [(self._rel(c, bt), bv) for bt, bv in bps if lo < bt < hi]
                new.append((self._rel(c, hi), interp(pts, cf, hi, "left")))
                merged = sorted(old["before"] + new + old["after"], key=lambda x: x[0])
                work.append((lo, hi, merged, len(old["before"]) + len(old["after"])))
            # phase 2 : écriture de tous les clips d'un bloc (une étape d'annulation, sans pause) ; défaite si un clip échoue
            targets = self._revalidate(track, plan["clips"], p, accept)   # rien n'a bougé pendant la lecture
            def write(touched):
                done = []
                for (lo, hi, merged, nold), (c, s, e, entry) in zip(work, targets):
                    nc = self._rebuild(track, c, [(p, merged)], warnings, accept, touched)
                    done.append((nc, lo, hi, merged, nold))
                return done
            done = self._commit(song, write)
            reply("shape", len(done), len(bps), plan.get("gap", 0))
            for nc, lo, hi, merged, nold in done: reply("rebuilt", self._ref(nc), str(nc.name), nold)
            # phase 3 : relecture de contrôle ; écart > tolérance → étape défaite
            if "unverified" in accept: reply("verified", 0, 0, 0, "skipped")
            else:
                for _ in self._verify(song, p, [(nc, lo, hi, merged) for nc, lo, hi, merged, _ in done], reply, warnings): yield
            for w in warnings: reply("warn", w)
        return job()

    # ---------- autres commandes ----------
    def cmd_ping(self, reply, a):
        """pong <version> live <version Live> session <n> · commands <liste> · accept <clés> · limits …"""
        app = Live.Application.get_application()
        reply("pong", VERSION, "live", "%d.%d.%d" % (app.get_major_version(), app.get_minor_version(), app.get_bugfix_version()), "session", self._session())
        reply("commands", *sorted("/" + n[4:].replace("_", "-") for n in dir(self) if n.startswith("cmd_")))
        reply("accept", ",".join(ACCEPT_KEYS))
        reply("limits", "read_points", MAX_READ_POINTS, "shape_points", MAX_SHAPE_POINTS, "jobs", MAX_JOBS, "verify_tol", VERIFY_TOL)

    def cmd_path(self, reply, a):
        o = self._resolve(a[0]); reply(self._ref(o), type(o).__name__)

    def cmd_get(self, reply, a):
        o = self._resolve(a[0]); reply(self._conv(getattr(o, str(a[1]))))

    def cmd_set(self, reply, a):
        o = self._resolve(a[0]); prop = str(a[1]); cur = getattr(o, prop); v = a[2]
        if isinstance(cur, bool): v = bool(int(v)) if not isinstance(v, str) else v.lower() in ("1", "true", "on")
        elif isinstance(cur, int): v = int(v)
        elif isinstance(cur, float): v = float(v)
        elif isinstance(cur, str): v = str(v)
        elif self._is_live_obj(cur): v = self._arg(v)
        setattr(o, prop, v); reply(self._conv(getattr(o, prop)))

    def cmd_call(self, reply, a):
        o = self._resolve(a[0]); fn = getattr(o, str(a[1])); r = fn(*[self._arg(x) for x in a[2:]])
        reply("ok" if r is None else self._conv(r))

    def cmd_info(self, reply, a):
        o = self._resolve(a[0])
        for n in sorted(x for x in dir(o) if not x.startswith("_")):
            try: v = getattr(o, n)
            except Exception: continue
            reply("function" if callable(v) else "property", n, "" if callable(v) else str(self._conv(v))[:80])

    def cmd_children(self, reply, a):
        o = self._resolve(a[0]); seq = getattr(o, str(a[1]))
        for i, c in enumerate(seq): reply(i, self._ref(c), str(getattr(c, "name", type(c).__name__)))

    def cmd_track(self, reply, a):
        t = self._find_track(a[0]); reply(self._ref(t), str(t.name))

    def cmd_param(self, reply, a):
        t = self._find_track(a[0]); p = self._find_param(t, a[1], a[2])
        reply(self._ref(p), str(p.name), float(p.min), float(p.max), float(p.value), str(p.str_for_value(p.value)), int(getattr(p, "is_quantized", 0)), int(getattr(p, "automation_state", 0)))

    def cmd_params(self, reply, a):
        d = self._resolve(a[0]); f = str(a[1]).lower() if len(a) > 1 else None
        for i, p in enumerate(d.parameters):
            if f and f not in str(p.name).lower(): continue
            reply(i, self._ref(p), str(p.name), float(p.min), float(p.max), float(p.value), str(p.str_for_value(p.value)), int(p.is_quantized))

    def cmd_solve(self, reply, a):
        p = self._resolve(a[0]); v, clamped = self._solve(p, float(a[1])); reply(v, str(p.str_for_value(v)), int(clamped))

    def cmd_clips(self, reply, a):
        t = self._find_track(a[0])
        for c, s, e in self._arr_clips(t): reply(self._ref(c), s, e, str(c.name), int(c.is_audio_clip))

    def cmd_read(self, reply, a):
        if len(a) < 4: raise ValueError("usage: /read <piste> <paramRef> <tA> <tB> [res]")
        t = self._find_track(a[0]); p = self._resolve(a[1]); tA, tB = float(a[2]), float(a[3]); res = float(a[4]) if len(a) > 4 else 1.0
        if not all(math.isfinite(x) for x in (tA, tB, res)): raise ValueError("valeurs non finies")
        if tA < 0 or tB < tA: raise ValueError("plage invalide (tA >= 0, tB >= tA)")
        if not (0 < res <= 64): raise ValueError("res doit être dans ]0, 64]")
        if (tB - tA) * res + 1 > MAX_READ_POINTS: raise ValueError("trop de points (> %d)" % MAX_READ_POINTS)
        def job():
            if int(getattr(p, "automation_state", 0)) == 2: reply("warn", "automation de %s surchargée (état 2) : les valeurs lues sont la valeur manuelle, pas l'automation" % p.name)
            got = {}
            for _ in self._sample([p], tA, tB, 1.0 / res, got): yield
            for tt, v in got.get(0, []): reply(tt, v, str(p.str_for_value(v)))
        return job()

    def cmd_events(self, reply, a):
        t = self._find_track(a[0]); p = self._resolve(a[1])
        tA = float(a[2]) if len(a) > 2 else -1e18; tB = float(a[3]) if len(a) > 3 else 1e18
        for c, s, e in self._arr_clips(t):
            if e <= tA or s >= tB: continue
            ev = self._env_of(c, p)
            if ev is None: continue
            for t_rel, v in self._sample_env(ev, self._rel(c, max(tA, s)), self._rel(c, min(tB, e))):
                reply(round(t_rel + s - float(c.start_marker), 4), v, str(p.str_for_value(v)), str(c.name))

    def cmd_clear(self, reply, a):
        if len(a) < 5: raise ValueError("usage: /clear <piste> <paramRef> <tA> <tB> <accept|->")
        t = self._find_track(a[0]); p = self._resolve(a[1]); tA, tB = float(a[2]), float(a[3]); accept = self._parse_accept(a[4])
        if tA < 0 or tB <= tA: raise ValueError("plage invalide")
        state = int(getattr(p, "automation_state", 0))
        targets = [(c, s, e) for c, s, e in self._arr_clips(t) if not (e <= tA or s >= tB) and (self._env_of(c, p) is not None or state != 0)]
        problems = []
        for c, s, e in targets:
            f, n = self._check_clip(c, accept); problems += f + n
            if state == 2 and self._env_of(c, p) is None: problems.append(self._override_msg(p))
        if problems: raise ValueError("refus : " + " ; ".join(problems))
        entries = [{"ref": self._ref(c), "name": str(c.name), "start": s, "end": e} for c, s, e in targets]
        def job():
            song = self.song(); warnings = []
            # phase 1 : lecture (rien n'est modifié)
            work = []
            for c, s, e, entry in self._revalidate(t, entries, p, accept):
                if self._cancel_requested(): raise ValueError("annulée")
                lo, hi = max(tA, s), min(tB, e); old = {}
                for _ in self._old_points(c, p, (lo, hi), old): yield
                work.append((lo, hi, sorted(old["before"] + old["after"], key=lambda x: x[0])))
            # phase 2 : écriture d'un bloc ; phase 3 : relecture
            cur = self._revalidate(t, entries, p, accept)
            def write(touched):
                return [(self._rebuild(t, c, [(p, merged)], warnings, accept, touched), lo, hi, merged) for (lo, hi, merged), (c, s, e, entry) in zip(work, cur)]
            done = self._commit(song, write)
            reply("cleared", len(done))
            if "unverified" in accept: reply("verified", 0, 0, 0, "skipped")
            else:
                for _ in self._verify(song, p, done, reply, warnings): yield
            for w in warnings: reply("warn", w)
        return job()

    # ---------- commandes typées (remplacent les /py courants) ----------
    def _track_kind(self, t):
        song = self.song()
        if t is song.master_track: return "master"
        if t in list(song.return_tracks): return "return"
        if getattr(t, "is_foldable", False): return "group"
        return "midi" if getattr(t, "has_midi_input", False) else "audio"

    def _meter_db(self, v):
        """Lecture de vu-mètre (échelle du fader : 0,85 = 0 dB) → dB affiché par le fader du master ; ±1 dB entre −7 et −16 dB."""
        try: return str(self.song().master_track.mixer_device.volume.str_for_value(float(v)))
        except Exception: return "?"

    def cmd_transport(self, reply, a):
        """/transport → état ; /transport play [t] | stop | pos <t> | loop on|off | loop <début> <longueur>"""
        song = self.song()
        if a:
            op = str(a[0]).lower()
            if op == "play":
                if len(a) > 1: song.current_song_time = float(a[1])
                if not song.is_playing: song.start_playing()
            elif op == "stop":
                if song.is_playing: song.stop_playing()
            elif op == "pos":
                if len(a) < 2: raise ValueError("usage: /transport pos <t>")
                if song.is_playing: raise ValueError("lecture en cours : /transport stop avant de déplacer le curseur")
                song.current_song_time = float(a[1])
            elif op == "loop":
                if len(a) == 2 and str(a[1]).lower() in ("on", "off", "1", "0"): song.loop = str(a[1]).lower() in ("on", "1")
                elif len(a) == 3:
                    st, ln = float(a[1]), float(a[2])
                    if st < 0 or ln <= 0: raise ValueError("boucle invalide (début >= 0, longueur > 0)")
                    song.loop_start = st; song.loop_length = ln
                else: raise ValueError("usage: /transport loop on|off | loop <début> <longueur>")
            else: raise ValueError("opération inconnue : " + op)
        reply("transport", int(song.is_playing), float(song.current_song_time), float(song.tempo), "%d/%d" % (int(song.signature_numerator), int(song.signature_denominator)),
              int(bool(song.loop)), float(song.loop_start), float(song.loop_length))

    def cmd_meters(self, reply, a):
        """/meters <t_départ> <secondes> [piste …] : lit les vu-mètres pendant la lecture (crête par piste + master), tâche asynchrone.
        Transport arrêté : lance la lecture à t_départ puis l'arrête et restaure le curseur ; déjà en lecture : lit sans rien déplacer.
        Lecture post-devices ET post-fader pour une piste, pré-devices du master pour le master ; dB via la courbe du fader (relatif)."""
        if len(a) < 2: raise ValueError("usage: /meters <t_départ> <secondes> [piste …]")
        t0, secs = float(a[0]), float(a[1])
        if t0 < 0 or not (0 < secs <= 30): raise ValueError("t_départ >= 0 et secondes dans ]0, 30]")
        song = self.song()
        tracks = [self._find_track(x) for x in a[2:]] or list(song.tracks)
        targets = tracks + ([song.master_track] if song.master_track not in tracks else [])
        def job():
            was_playing = bool(song.is_playing); saved = float(song.current_song_time)
            peaks = dict((i, 0.0) for i in range(len(targets))); ticks = max(1, int(round(secs / TICK_SECONDS))); n = 0; start = saved
            try:
                if not was_playing: song.current_song_time = t0; song.start_playing(); start = t0
                for _ in range(ticks):
                    yield
                    if self._cancel_requested(): break
                    if not song.is_playing: raise ValueError("lecture arrêtée pendant la mesure : abandon")
                    for i, t in enumerate(targets): peaks[i] = max(peaks[i], float(t.output_meter_left), float(t.output_meter_right))
                    n += 1
                end = float(song.current_song_time)
            finally:
                if not was_playing:
                    try: song.stop_playing(); song.current_song_time = saved
                    except Exception: pass
            reply("meters", start, end, n)
            for i, t in enumerate(targets): reply("meter", self._ref(t), str(t.name), self._track_kind(t), round(peaks[i], 4), self._meter_db(peaks[i]))
        return job()

    def cmd_setparam(self, reply, a):
        """/setparam <piste> <device|mixer> <param> <valeur> [disp|raw] [override] → set <ref> <nom> <avant> <aff. avant> <après> <aff. après> <état automation>
        Refus si le paramètre est automatisé (une écriture manuelle surcharge l'automation) sauf `override` ; relecture après écriture."""
        if len(a) < 4: raise ValueError("usage: /setparam <piste> <device|mixer> <param> <valeur> [disp|raw] [override]")
        t = self._find_track(a[0]); p = self._find_param(t, a[1], a[2]); target = float(a[3])
        opts = [str(x).lower() for x in a[4:]]; unit = "raw" if "raw" in opts else "disp"; override = "override" in opts
        state = int(getattr(p, "automation_state", 0))
        if state != 0 and not override: raise ValueError("%s est automatisé (état %d) : une écriture manuelle surcharge l'automation (« Réactiver l'automation ») ; ajouter override, ou écrire l'automation avec /shape" % (p.name, state))
        mn, mx = float(p.min), float(p.max)
        if int(getattr(p, "is_quantized", 0)) and unit != "raw": raise ValueError("paramètre quantifié : raw avec une valeur entière")
        if unit == "raw":
            raw = target
            if raw < mn or raw > mx: raise ValueError("valeur %g hors [%g, %g]" % (raw, mn, mx))
        else:
            raw, clamped = self._solve(p, target)
            if clamped: raise ValueError("valeur %g hors plage affichable (%r … %r)" % (target, p.str_for_value(mn), p.str_for_value(mx)))
        before = float(p.value); before_disp = str(p.str_for_value(before))
        p.value = raw
        got = float(p.value)
        if abs(got - raw) > VERIFY_TOL * max(1e-9, mx - mn) and not (int(getattr(p, "is_quantized", 0)) and abs(got - raw) < 0.5):
            raise ValueError("non appliqué : demandé %g, relu %g (%s)" % (raw, got, p.str_for_value(got)))
        reply("set", self._ref(p), str(p.name), before, before_disp, got, str(p.str_for_value(got)), int(getattr(p, "automation_state", 0)))

    def _snap_store(self):
        if not hasattr(self, "_snaps"): self._snaps = {}; self._snap_n = 0
        return self._snaps

    def cmd_snapshot(self, reply, a):
        """/snapshot <piste> [device|mixer] → snapshot <id> <n> puis <ref> <nom> <valeur> <affichage> ; gardé jusqu'au redémarrage de Live."""
        if not a: raise ValueError("usage: /snapshot <piste> [device|mixer]")
        t = self._find_track(a[0]); what = str(a[1]) if len(a) > 1 else None
        if what is None: devs = [t.mixer_device] + list(t.devices)
        elif what.lower() == "mixer": devs = [t.mixer_device]
        else: devs = [self._obj(what) if what.startswith("o:") else self._find_named(list(t.devices), what, "device")]
        params = []
        for d in devs:
            if d is t.mixer_device: params += [d.volume, d.panning] + list(d.sends)
            else: params += list(d.parameters)
        store = self._snap_store(); self._snap_n += 1; sid = "s%d" % self._snap_n
        store[sid] = {"track": str(t.name), "what": what or "all", "values": [(p, float(p.value)) for p in params]}
        reply("snapshot", sid, len(params), str(t.name), what or "all")
        for p, v in store[sid]["values"]: reply(self._ref(p), str(p.name), v, str(p.str_for_value(v)))

    def cmd_snapshots(self, reply, a):
        for sid, s in sorted(self._snap_store().items(), key=lambda kv: int(kv[0][1:])): reply(sid, s["track"], s["what"], len(s["values"]))

    def cmd_restore(self, reply, a):
        """/restore <id> [override] : remet les valeurs d'un snapshot, en une étape d'annulation, puis relit ; refus si un paramètre est automatisé sauf override."""
        if not a: raise ValueError("usage: /restore <id> [override]")
        s = self._snap_store().get(str(a[0]))
        if s is None: raise ValueError("snapshot inconnu %s (voir /snapshots)" % a[0])
        override = any(str(x).lower() == "override" for x in a[1:])
        song = self.song(); blocked, gone = [], []
        for p, v in s["values"]:
            try: float(p.value)
            except Exception: gone.append(str(getattr(p, "name", "?"))); continue
            if int(getattr(p, "automation_state", 0)) != 0 and not override: blocked.append(str(p.name))
        if gone: raise ValueError("paramètres disparus (device supprimé ?) : " + ", ".join(gone))
        if blocked: raise ValueError("automatisés (ajouter override pour surcharger) : " + ", ".join(blocked))
        def write(touched):
            changed = []
            for p, v in s["values"]:
                if abs(float(p.value) - v) < 1e-9: continue
                p.value = v; touched.append(str(p.name)); changed.append(p)
            return changed
        changed = self._commit(song, write)
        worst = 0.0
        for p, v in s["values"]:
            dev = abs(float(p.value) - v) / max(1e-9, float(p.max) - float(p.min)); worst = max(worst, dev)
        if worst > VERIFY_TOL:
            try: song.undo()
            except Exception: pass
            raise ValueError("relecture : écart %.4f de la plage > %.4f ; étape annulée" % (worst, VERIFY_TOL))
        reply("restored", str(a[0]), len(changed), round(worst, 6))

    def cmd_locators(self, reply, a):
        for c in sorted(self.song().cue_points, key=lambda c: float(c.time)): reply(self._ref(c), float(c.time), str(c.name))

    def cmd_locator(self, reply, a):
        """/locator <t> <nom> : pose (ou renomme) un repère à t ; le curseur est déplacé puis restauré (transport arrêté)."""
        if len(a) < 2: raise ValueError("usage: /locator <t> <nom>")
        t, name = float(a[0]), str(a[1]); song = self.song()
        if t < 0: raise ValueError("temps négatif")
        found = [c for c in song.cue_points if abs(float(c.time) - t) < 1e-6]
        if not found:
            if song.is_playing: raise ValueError("lecture en cours : arrêter le transport (le curseur est déplacé pour poser le repère)")
            saved = float(song.current_song_time)
            try: song.current_song_time = t; song.set_or_delete_cue()
            finally: song.current_song_time = saved
            found = [c for c in song.cue_points if abs(float(c.time) - t) < 1e-6]
            if not found: raise ValueError("repère non créé à t=%g" % t)
        c = found[0]; c.name = name
        reply("locator", self._ref(c), float(c.time), str(c.name), "renamed" if len(a) > 2 else "ok")

    def cmd_state(self, reply, a):
        """/state → une ligne `state <json>` : transport, pistes (type, mute/solo, volume, pan, devices, clips, paramètres automatisés), repères."""
        song = self.song(); tracks = []
        for t in list(song.tracks) + list(song.return_tracks) + [song.master_track]:
            kind = self._track_kind(t); mix = t.mixer_device; devs = []; automated = 0
            for d in t.devices:
                n_auto = 0
                try: n_auto = sum(1 for p in d.parameters if int(getattr(p, "automation_state", 0)) != 0)
                except Exception: pass
                automated += n_auto
                devs.append({"ref": self._ref(d), "name": str(d.name), "class": str(getattr(d, "class_name", type(d).__name__)), "on": int(bool(getattr(d, "is_active", 1))), "automated_params": n_auto})
            for p in [mix.volume, mix.panning] + list(mix.sends):
                if int(getattr(p, "automation_state", 0)) != 0: automated += 1
            try: n_clips = len(list(t.arrangement_clips))
            except Exception: n_clips = 0
            tracks.append({"ref": self._ref(t), "name": str(t.name), "kind": kind, "mute": int(bool(getattr(t, "mute", 0))), "solo": int(bool(getattr(t, "solo", 0))),
                           "volume": str(mix.volume.str_for_value(mix.volume.value)), "pan": str(mix.panning.str_for_value(mix.panning.value)),
                           "sends": [str(s.str_for_value(s.value)) for s in mix.sends], "devices": devs, "arrangement_clips": n_clips, "automated_params": automated})
        st = {"version": VERSION, "session": self._session(), "tempo": float(song.tempo), "signature": "%d/%d" % (int(song.signature_numerator), int(song.signature_denominator)),
              "playing": int(song.is_playing), "position": float(song.current_song_time), "loop": {"on": int(bool(song.loop)), "start": float(song.loop_start), "length": float(song.loop_length)},
              "tracks": tracks, "locators": [{"time": float(c.time), "name": str(c.name)} for c in sorted(song.cue_points, key=lambda c: float(c.time))]}
        reply("state", json.dumps(st, ensure_ascii=False))

    def cmd_jobs(self, reply, a):
        for j in self._jobs: reply(j["rid"], j["cmd"], "running" if j["started"] else "queued", int(j["cancel"]))

    def cmd_cancel(self, reply, a):
        """/cancel [<id de requête>] : sans argument, annule toutes les tâches."""
        target = str(a[0]) if a else None; n = 0
        for j in list(self._jobs):
            if target is not None and j["rid"] != target: continue
            if j is self._jobs[0] and j["started"]:
                j["cancel"] = True; n += 1   # la tâche en cours s'arrête à sa prochaine pause (voir _job_tick) ; une écriture déjà faite n'est pas défaite
            else:
                self._jobs.remove(j)
                try: j["gen"].close()
                except Exception: pass
                self._fail(j["addr"], j["rid"], "%s: annulée" % j["cmd"]); self._send(j["addr"], "/end", j["rid"], j["cmd"]); n += 1
        reply("cancelled", n)

    def cmd_journal(self, reply, a):
        """/journal [n] : les n dernières écritures journalisées (défaut 20), une ligne `entry <json>` chacune, plus ancienne d'abord."""
        n = int(a[0]) if a else 20
        try:
            with open(self._journal_path(), encoding="utf-8") as f: lines = [l for l in f.read().splitlines() if l.strip()]
        except FileNotFoundError: lines = []
        for l in lines[-n:]: reply("entry", l)
        reply("journal", self._journal_path(), len(lines))

    def cmd_py(self, reply, a):
        code = " ".join(str(x) for x in a)
        env = {"song": self.song(), "app": Live.Application.get_application(), "Live": Live, "self": self, "obj": self._obj, "ref": self._ref, "reply": reply}
        try: r = eval(code, env)
        except SyntaxError:
            import ast
            tree = ast.parse(code); r = "ok"
            if tree.body and isinstance(tree.body[-1], ast.Expr):
                last = ast.Expression(tree.body[-1].value); tree.body = tree.body[:-1]
                exec(compile(tree, "<py>", "exec"), env); r = eval(compile(last, "<py>", "eval"), env)
            else: exec(code, env)
            if "result" in env: r = env["result"]
        reply(str(self._conv(r)))

    def cmd_reload(self, reply, a):
        path = os.path.abspath(__file__)
        if path.endswith(".pyc"): path = path[:-1]
        ns = {"__name__": "LOMBridge_reloaded", "__file__": path}
        exec(compile(open(path, encoding="utf-8").read(), path, "exec"), ns)
        self.__class__ = ns["LOMBridge"]
        reply("reloaded", ns["VERSION"])


def create_instance(c_instance):
    return LOMBridge(c_instance)
