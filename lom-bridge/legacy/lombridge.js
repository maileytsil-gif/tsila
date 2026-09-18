// LOM Bridge v0.1 — pont OSC/UDP <-> Live Object Model (Max for Live, objet [js], ES5)
// Reçoit des commandes OSC sur udpreceive, répond sur udpsend.
// Chaque commande se termine par un message "/end <cmd>". Erreurs : "/err <texte>".
autowatch = 1;
inlets = 1;
outlets = 2;
var VERSION = "0.1.0";

function bang() {
  post("LOM Bridge " + VERSION + " prêt\n");
  var tempo = "?";
  try { tempo = String(first(new LiveAPI("live_set").get("tempo"))); } catch (e) { tempo = "err " + e; }
  reply("/jsready", VERSION, tempo);
  var tk = new Task(function () { reply("/tick", "scheduler ok"); });
  tk.schedule(500);
}
function loadbang() { }

// ---------- utilitaires ----------
function reply() { var a = arrayfromargs(arguments); outlet(0, a); }
function dbg(s) { outlet(1, String(s)); }

function isNum(x) { return typeof x === "number" && !isNaN(x); }

function api(ref) {
  var o;
  if (isNum(ref)) o = new LiveAPI("id " + ref);
  else {
    var s = String(ref);
    if (/^\d+$/.test(s)) o = new LiveAPI("id " + s);
    else o = new LiveAPI(s);
  }
  if (!o || o.id == 0) throw new Error("objet introuvable: " + ref);
  return o;
}

function idOf(r) {
  if (r === null || r === undefined) return 0;
  if (isNum(r)) return r;
  if (r instanceof Array) {
    if (r.length >= 2 && r[0] === "id") return Number(r[1]);
    if (r.length === 1) return idOf(r[0]);
  }
  var m = String(r).match(/id[\s,]+(\d+)/);
  return m ? Number(m[1]) : 0;
}

function ids(arr) { // ["id",1,"id",2] -> [1,2]
  var out = [];
  if (!arr) return out;
  for (var i = 0; i + 1 < arr.length; i += 2) if (arr[i] === "id") out.push(Number(arr[i + 1]));
  return out;
}

function first(x) { return (x instanceof Array) ? x[0] : x; }

function parseDisp(s) { // "-5.0 dB" -> -5 ; "1.20 kHz" -> 1200 ; "-inf dB" -> -Infinity
  s = String(first(s));
  if (/-inf/i.test(s)) return -Infinity;
  var m = s.match(/(-?\d+(?:[.,]\d+)?)\s*([a-zA-Zµ%]*)/);
  if (!m) return NaN;
  var v = parseFloat(m[1].replace(",", "."));
  if (/^k/.test(m[2])) v *= 1000;
  return v;
}

// valeur normalisée correspondant à une valeur d'affichage (dichotomie sur str_for_value)
function solve(param, target) {
  var mn = Number(first(param.get("min"))), mx = Number(first(param.get("max")));
  var f = function (x) { return parseDisp(param.call("str_for_value", x)); };
  var flo = f(mn), fhi = f(mx);
  var inc = fhi > flo;
  if (target <= Math.min(flo, fhi)) return inc ? mn : mx;
  if (target >= Math.max(flo, fhi)) return inc ? mx : mn;
  var lo = mn, hi = mx;
  for (var i = 0; i < 60; i++) {
    var mid = (lo + hi) / 2, fm = f(mid);
    if ((fm < target) === inc) lo = mid; else hi = mid;
  }
  return (lo + hi) / 2;
}

function curveFn(c) {
  if (isNum(c)) return function (x) { return Math.pow(x, c); };
  switch (String(c)) {
    case "exp": return function (x) { return x * x; };
    case "log": return function (x) { return Math.sqrt(x); };
    case "sc": case "scurve": return function (x) { return x * x * (3 - 2 * x); };
    case "sin": return function (x) { return 0.5 - 0.5 * Math.cos(Math.PI * x); };
    default: return function (x) { return x; };
  }
}

function arrangementClips(track) {
  var out = [], list = ids(track.get("arrangement_clips"));
  for (var i = 0; i < list.length; i++) {
    var c = new LiveAPI("id " + list[i]);
    out.push({ id: list[i], start: Number(first(c.get("start_time"))), end: Number(first(c.get("end_time"))) });
  }
  out.sort(function (a, b) { return a.start - b.start; });
  return out;
}

function clipAt(clips, t) {
  for (var i = 0; i < clips.length; i++) if (t >= clips[i].start && t < clips[i].end) return clips[i];
  return null;
}

var envCache = {};
function envelope(clipId, paramId) {
  var key = clipId + ":" + paramId;
  if (envCache[key]) return envCache[key];
  var clip = new LiveAPI("id " + clipId);
  var eid = idOf(clip.call("automation_envelope", "id " + paramId));
  if (!eid) eid = idOf(clip.call("create_automation_envelope", "id " + paramId));
  if (!eid) throw new Error("enveloppe impossible clip " + clipId + " param " + paramId);
  var env = new LiveAPI("id " + eid);
  envCache[key] = env;
  return env;
}

// construit une liste de marches [t, len, v] à partir d'une polyligne [[t,v],...]
function buildSteps(pts, res, curve, hold, holdEnd) {
  var steps = [], cf = curveFn(curve);
  for (var i = 0; i + 1 < pts.length; i++) {
    var t0 = pts[i][0], v0 = pts[i][1], t1 = pts[i + 1][0], v1 = pts[i + 1][1];
    var dur = t1 - t0;
    if (dur <= 0) continue;
    if (v0 === v1) { steps.push([t0, dur, v0]); continue; }
    var n = Math.max(1, Math.round(dur * res));
    var len = dur / n;
    for (var k = 0; k < n; k++) {
      var frac = (k + 0.5) / n; // valeur au milieu de la marche
      steps.push([t0 + k * len, len, v0 + (v1 - v0) * cf(frac)]);
    }
  }
  var last = pts[pts.length - 1];
  if (hold && holdEnd > last[0]) steps.push([last[0], holdEnd - last[0], last[1]]);
  return steps;
}

function findTrack(name) {
  var song = new LiveAPI("live_set");
  var groups = ["tracks", "return_tracks"];
  var lname = String(name).toLowerCase(), sub = null;
  for (var g = 0; g < groups.length; g++) {
    var n = song.getcount(groups[g]);
    for (var i = 0; i < n; i++) {
      var t = new LiveAPI("live_set " + groups[g] + " " + i);
      var tn = String(first(t.get("name")));
      if (tn.toLowerCase() === lname) return t;
      if (!sub && tn.toLowerCase().indexOf(lname) >= 0) sub = t;
    }
  }
  var m = new LiveAPI("live_set master_track");
  if (lname === "master" || lname === "main") return m;
  if (sub) return sub;
  throw new Error("piste introuvable: " + name);
}

function findParam(track, deviceName, paramName) {
  var dn = String(deviceName).toLowerCase(), pn = String(paramName).toLowerCase();
  if (dn === "mixer") {
    var mix = new LiveAPI(track.unquotedpath + " mixer_device");
    if (pn === "volume" || pn === "vol") return new LiveAPI(mix.unquotedpath + " volume");
    if (pn === "pan" || pn === "panning") return new LiveAPI(mix.unquotedpath + " panning");
    var ms = pn.match(/^send\s*([a-l])$/);
    if (ms) return new LiveAPI(mix.unquotedpath + " sends " + (ms[1].charCodeAt(0) - 97));
    throw new Error("param mixer inconnu: " + paramName);
  }
  var nd = track.getcount("devices"), dev = null, devSub = null;
  for (var i = 0; i < nd; i++) {
    var d = new LiveAPI(track.unquotedpath + " devices " + i);
    var name = String(first(d.get("name"))).toLowerCase();
    if (name === dn || String(i) === dn) { dev = d; break; }
    if (!devSub && name.indexOf(dn) >= 0) devSub = d;
  }
  dev = dev || devSub;
  if (!dev) throw new Error("device introuvable: " + deviceName);
  var np = dev.getcount("parameters"), p = null, pSub = null;
  for (var j = 0; j < np; j++) {
    var q = new LiveAPI(dev.unquotedpath + " parameters " + j);
    var qn = String(first(q.get("name"))).toLowerCase();
    if (qn === pn || String(j) === pn) { p = q; break; }
    if (!pSub && qn.indexOf(pn) >= 0) pSub = q;
  }
  p = p || pSub;
  if (!p) throw new Error("paramètre introuvable: " + paramName + " dans " + deviceName);
  return p;
}

function toRaw(param, v, unit) {
  return (unit === "disp" || unit === "db" || unit === "hz") ? solve(param, Number(v)) : Number(v);
}

// ---------- commandes ----------
var H = {};

H["/ping"] = function () { reply("/r", "pong", VERSION, "live", String(first(new LiveAPI("live_app").call("get_version_string")))); };

H["/path"] = function (a) { var o = api(a[0]); reply("/r", o.id, o.unquotedpath, o.type); };

H["/get"] = function (a) { var o = api(a[0]); reply.apply(null, ["/r"].concat(o.get(String(a[1])))); };

H["/set"] = function (a) { var o = api(a[0]); o.set(String(a[1]), a[2]); reply.apply(null, ["/r"].concat(o.get(String(a[1])))); };

H["/call"] = function (a) { var o = api(a[0]); var r = o.call.apply(o, [String(a[1])].concat(a.slice(2))); reply("/r", (r === undefined || r === null) ? "ok" : String(r)); };

H["/info"] = function (a) { var o = api(a[0]); var lines = String(o.info).split("\n"); for (var i = 0; i < lines.length; i++) reply("/r", lines[i]); };

H["/children"] = function (a) { // /children <ref> <child> -> /r index id name
  var o = api(a[0]), child = String(a[1]), n = o.getcount(child);
  for (var i = 0; i < n; i++) { var c = new LiveAPI(o.unquotedpath + " " + child + " " + i); var nm = c.get("name"); reply("/r", i, c.id, nm ? String(first(nm)) : c.type); }
};

H["/track"] = function (a) { var t = findTrack(a[0]); reply("/r", t.id, String(first(t.get("name"))), t.unquotedpath); };

H["/param"] = function (a) { // /param <trackRef|name> <device|mixer> <param>
  var t = isNum(a[0]) ? api(a[0]) : findTrack(a[0]);
  var p = findParam(t, a[1], a[2]);
  var cv = Number(first(p.get("value")));
  reply("/r", p.id, String(first(p.get("name"))), Number(first(p.get("min"))), Number(first(p.get("max"))), cv, String(first(p.call("str_for_value", cv))));
};

H["/params"] = function (a) { // /params <deviceRef> [filtre]
  var d = api(a[0]), f = a[1] ? String(a[1]).toLowerCase() : null, n = d.getcount("parameters");
  for (var i = 0; i < n; i++) {
    var p = new LiveAPI(d.unquotedpath + " parameters " + i);
    var nm = String(first(p.get("name")));
    if (f && nm.toLowerCase().indexOf(f) < 0) continue;
    var v = Number(first(p.get("value")));
    reply("/r", i, p.id, nm, Number(first(p.get("min"))), Number(first(p.get("max"))), v, String(first(p.call("str_for_value", v))), Number(first(p.get("is_quantized"))));
  }
};

H["/solve"] = function (a) { var p = api(a[0]); var v = solve(p, Number(a[1])); reply("/r", v, String(first(p.call("str_for_value", v)))); };

H["/clips"] = function (a) { var t = isNum(a[0]) ? api(a[0]) : findTrack(a[0]); var cs = arrangementClips(t); for (var i = 0; i < cs.length; i++) { var c = new LiveAPI("id " + cs[i].id); reply("/r", cs[i].id, cs[i].start, cs[i].end, String(first(c.get("name")))); } };

// /step <clipId> <paramId> <t_rel> <len> <v>  (temps relatif au clip, valeur brute)
H["/step"] = function (a) { var env = envelope(Number(a[0]), Number(a[1])); env.call("insert_step", Number(a[2]), Number(a[3]), Number(a[4])); reply("/r", "step", env.id); };

// /shape <trackRef> <paramId> <unit raw|disp> <res> <curve> <hold 0|1> t0 v0 t1 v1 ...  (temps absolus en temps/beats)
H["/shape"] = function (a) {
  var t = isNum(a[0]) ? api(a[0]) : findTrack(a[0]);
  var p = api(a[1]); var unit = String(a[2]); var res = Number(a[3]); var curve = a[4]; var hold = Number(a[5]);
  var pts = [];
  for (var i = 6; i + 1 < a.length; i += 2) pts.push([Number(a[i]), toRaw(p, a[i + 1], unit)]);
  if (pts.length < 1) throw new Error("aucun point");
  var clips = arrangementClips(t);
  if (!clips.length) throw new Error("aucun clip d'arrangement sur la piste (l'automation LOM passe par les clips)");
  var last = pts[pts.length - 1], holdEnd = 0;
  var lc = clipAt(clips, last[0]); if (lc) holdEnd = lc.end;
  var steps = buildSteps(pts, res, curve, hold, holdEnd);
  var written = 0, skipped = 0;
  for (var k = 0; k < steps.length; k++) {
    var s = steps[k], tt = s[0], remaining = s[1];
    while (remaining > 1e-6) {
      var c = clipAt(clips, tt);
      if (!c) { skipped++; break; }
      var len = Math.min(remaining, c.end - tt);
      envelope(c.id, p.id).call("insert_step", tt - c.start, len, s[2]);
      written++; tt += len; remaining -= len;
    }
  }
  reply("/r", "shape", written, skipped, steps.length, clips.length);
};

// /read <trackRef> <paramId> <tA> <tB> <res> -> /r t value disp
H["/read"] = function (a) {
  var t = isNum(a[0]) ? api(a[0]) : findTrack(a[0]);
  var p = api(a[1]); var tA = Number(a[2]), tB = Number(a[3]), res = Number(a[4] || 1);
  var clips = arrangementClips(t);
  for (var tt = tA; tt <= tB + 1e-9; tt += 1 / res) {
    var c = clipAt(clips, tt);
    if (!c) { reply("/r", tt, "-", "pas de clip"); continue; }
    var clip = new LiveAPI("id " + c.id);
    var eid = idOf(clip.call("automation_envelope", "id " + p.id));
    if (!eid) { reply("/r", tt, "-", "pas d'enveloppe"); continue; }
    var v = Number(first(new LiveAPI("id " + eid).call("value_at_time", tt - c.start)));
    reply("/r", tt, v, String(first(p.call("str_for_value", v))));
  }
};

// /clear <trackRef> <paramId> [tA tB] : efface l'enveloppe ENTIÈRE des clips qui chevauchent la plage
H["/clear"] = function (a) {
  var t = isNum(a[0]) ? api(a[0]) : findTrack(a[0]);
  var p = api(a[1]); var tA = a.length > 2 ? Number(a[2]) : -Infinity, tB = a.length > 3 ? Number(a[3]) : Infinity;
  var clips = arrangementClips(t), n = 0;
  for (var i = 0; i < clips.length; i++) {
    if (clips[i].end <= tA || clips[i].start >= tB) continue;
    new LiveAPI("id " + clips[i].id).call("clear_envelope", "id " + p.id); n++;
    delete envCache[clips[i].id + ":" + p.id];
  }
  reply("/r", "cleared", n);
};

H["/js"] = function (a) { var r = eval(a.join(" ")); reply("/r", (r === undefined) ? "undefined" : String(r)); };

function anything() {
  var cmd = messagename, a = arrayfromargs(arguments), rid = "";
  if (a.length && typeof a[a.length - 1] === "string" && a[a.length - 1].charAt(0) === "#") { rid = a[a.length - 1].substring(1); a = a.slice(0, -1); }
  reply("/begin", cmd, rid);
  try {
    if (!H[cmd]) throw new Error("commande inconnue " + cmd);
    H[cmd](a);
  } catch (e) {
    reply("/err", cmd + ": " + (e && e.message ? e.message : String(e)));
    dbg("ERR " + cmd + ": " + (e && e.message ? e.message : String(e)));
  }
  reply("/end", cmd, rid);
}
