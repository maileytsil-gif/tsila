# -*- coding: utf-8 -*-
"""Tests logiciels hors Live pour LOM Bridge : python3 -m unittest tests/test_offline.py -v
Un faux module `Live` et un faux `_Framework.ControlSurface` sont injectés ; aucun accès à Ableton.
Les faux reproduisent ce qui compte pour l'écriture : le clip dupliqué dans l'arrangement porte les enveloppes créées en session
(exposées, ou cachées comme pour l'audio réel), `song.undo()` remet les clips d'avant `begin_undo_step`, et `FollowParam`
suit l'automation au curseur comme un paramètre de Live transport arrêté."""
import sys, os, types, json, tempfile, unittest, importlib.util, struct

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# ---------- faux Live ----------
class FakeParam:
    _n = 0
    def __init__(self, name, mn=0.0, mx=1.0, value=0.85, quantized=0, automation_state=0, disp=None):
        FakeParam._n += 1; self._live_ptr = 1000 + FakeParam._n
        self.name, self.min, self.max, self.value, self.is_quantized, self.automation_state = name, mn, mx, value, quantized, automation_state
        self._disp = disp or (lambda v: "%.3f dB" % (20 * (v - 0.85) * 3))   # affichage croissant simple
    def str_for_value(self, v): return self._disp(v)

class FollowParam(FakeParam):
    """Paramètre dont la valeur suit l'automation d'arrangement de sa piste au curseur (état 1), exposée ou cachée ;
    en état 0 ou 2 (surchargé), la valeur manuelle."""
    def __init__(self, name, **kw):
        self.song = self.track = None; FakeParam.__init__(self, name, **kw)
    @property
    def value(self):
        if self.automation_state != 1 or self.song is None: return self._value
        t = self.song.current_song_time
        for c in self.track.arrangement_clips:
            if c.start_time <= t < c.end_time:
                for ev in list(c.automation_envelopes) + list(getattr(c, "hidden_envelopes", [])):
                    if ev.parameter is self: return ev.value_at_time(t - c.start_time + c.start_marker)
        return self._value
    @value.setter
    def value(self, v): self._value = v

class FakeEvent:
    def __init__(self, t, v): self.time, self.value = t, v
class FakeEnvelope:
    def __init__(self, param, pts=None):
        self.parameter, self.events, self.created = param, list(pts or []), []
    def events_in_range(self, lo, hi): return [FakeEvent(t, v) for t, v in self.events if lo <= t <= hi]
    def value_at_time(self, t):
        pts = self.events
        if not pts: return 0.0
        if t <= pts[0][0]: return pts[0][1]
        for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
            if t0 <= t <= t1: return v0 if t1 == t0 else v0 + (v1 - v0) * (t - t0) / (t1 - t0)
        return pts[-1][1]
    def create_event(self, ev): self.created.append((ev.time, ev.value))

class FakeClip:
    _n = 0
    def __init__(self, name, start, end, audio=False, envelopes=None, looping=False, loop_len=None):
        FakeClip._n += 1; self._live_ptr = 5000 + FakeClip._n
        self.name, self.start_time, self.end_time, self.is_audio_clip = name, start, end, audio
        self.start_marker, self.end_marker, self.looping = 0.0, end - start, looping
        self.loop_start, self.loop_end = 0.0, (loop_len if loop_len is not None else end - start)
        self.length = end - start; self.file_path = "/tmp/x.wav" if audio else ""
        self.is_take_lane_clip = False; self.is_recording = False
        self.automation_envelopes = envelopes or []; self.notes = []
        self.warping, self.warp_mode, self.gain, self.pitch_coarse, self.pitch_fine, self.ram_mode = False, 0, 0.5, 0, 0, False
        self.warp_markers = []; self.color = 0; self.muted = False
        self.signature_numerator, self.signature_denominator, self.launch_mode, self.launch_quantization, self.legato, self.velocity_amount = 4, 4, 0, 0, False, 0
        self.envs_created = {}
    def __setattr__(self, k, v):
        if k == "start_marker" and v > getattr(self, "end_marker", 1e18) + 1e-9: return   # Live ignore silencieusement
        if k == "end_marker" and v > getattr(self, "timeline", 1e18) + 1e-9: return
        object.__setattr__(self, k, v)
    def get_all_notes_extended(self): return list(self.notes)
    def add_new_notes(self, specs): self.notes.extend(specs)
    def create_automation_envelope(self, p):
        e = FakeEnvelope(p); self.envs_created[p.name] = e; return e
class FakeSlot:
    def __init__(self, track): self.track, self.clip, self.has_clip, self.is_group_slot, self.deleted = track, None, False, False, 0
    def create_clip(self, length):
        self.clip = FakeClip("session", 0.0, length); self.clip.timeline = length; self.has_clip = True; return self.clip
    def create_audio_clip(self, path):
        self.clip = FakeClip("session", 0.0, 4.0, audio=True); self.clip.file_path = path; self.has_clip = True; return self.clip
    def delete_clip(self): self.clip, self.has_clip, self.deleted = None, False, self.deleted + 1
class FakeMixer:
    def __init__(self):
        self.volume = FakeParam("Track Volume"); self.panning = FakeParam("Track Panning", -1, 1, 0.0, disp=lambda v: "%.0f" % (v * 50)); self.sends = [FakeParam("A-Reverb", 0, 1, 0.1)]
class FakeTrack:
    _n = 0
    def __init__(self, name, clips=None, midi=True, expose=True):
        FakeTrack._n += 1; self._live_ptr = 100 + FakeTrack._n
        self.name, self.arrangement_clips, self.devices, self.mixer_device = name, clips or [], [], FakeMixer()
        self.clip_slots = [FakeSlot(self) for _ in range(4)]; self.has_midi_input = midi; self.dup_calls = []; self.fail_duplicate = False
        self.expose = expose   # False : le clip d'arrangement n'expose pas ses enveloppes (audio réel), elles restent cachées
    def duplicate_clip_to_arrangement(self, clip, t):
        self.dup_calls.append((clip, t))
        if self.fail_duplicate: raise RuntimeError("duplicate refused")
        nc = FakeClip(clip.name, t, t + (clip.end_marker - clip.start_marker), audio=clip.is_audio_clip)
        nc.timeline = getattr(clip, "timeline", 1e18); nc.end_marker = clip.end_marker; nc.start_marker = clip.start_marker
        envs = [FakeEnvelope(e.parameter, sorted(e.created)) for e in clip.envs_created.values()]
        if self.expose: nc.automation_envelopes = envs
        else: nc.hidden_envelopes = envs
        old = [c for c in self.arrangement_clips if abs(c.start_time - t) < 1e-9]
        for c in old: self.arrangement_clips.remove(c)
        self.arrangement_clips.append(nc); return nc
class FakeSong:
    def __init__(self, tracks):
        self.tracks, self.return_tracks, self.master_track = tracks, [], FakeTrack("Main")
        self.is_playing, self.current_song_time, self.scenes, self.undo_log = False, 0.0, [1, 2, 3, 4], []
        self.tempo = 126.0; self.undo_calls = []; self._snapshot = None
    def begin_undo_step(self):
        self.undo_log.append("begin"); self._snapshot = [(t, list(t.arrangement_clips)) for t in self.tracks]
    def end_undo_step(self): self.undo_log.append("end")
    def undo(self):
        """Remet les clips d'arrangement tels qu'avant la dernière étape (une seule étape, comme Cmd+Z)."""
        self.undo_calls.append(1)
        for t, clips in self._snapshot or []: t.arrangement_clips = list(clips)
    def create_scene(self, i): self.scenes.append(len(self.scenes) + 1)
    def delete_scene(self, i): self.scenes.pop(i)

def make_live_module():
    Live = types.ModuleType("Live")
    class Env: pass
    class EnvelopeEvent:
        def __init__(self, t, v, cc=None): self.time, self.value = t, v
    Live.Envelope = types.SimpleNamespace(EnvelopeEvent=EnvelopeEvent)
    class WarpMarker:
        def __init__(self, st, bt): self.sample_time, self.beat_time = st, bt
    class MidiNoteSpecification:
        def __init__(self, **kw): self.__dict__.update(kw)
    Live.Clip = types.SimpleNamespace(WarpMarker=WarpMarker, MidiNoteSpecification=MidiNoteSpecification)
    app = types.SimpleNamespace(get_major_version=lambda: 12, get_minor_version=lambda: 4, get_bugfix_version=lambda: 5)
    Live.Application = types.SimpleNamespace(get_application=lambda: app)
    return Live

def load_bridge(song, tmpdir):
    sys.modules["Live"] = make_live_module()
    fw = types.ModuleType("_Framework"); cs = types.ModuleType("_Framework.ControlSurface")
    class ControlSurface:
        def __init__(self, c): self.msgs = []
        def disconnect(self): pass
        def update_display(self): pass
        def log_message(self, m): self.msgs.append(m)
        def show_message(self, m): self.msgs.append(m)
        def song(self): return self._song
    cs.ControlSurface = ControlSurface; fw.ControlSurface = cs
    sys.modules["_Framework"] = fw; sys.modules["_Framework.ControlSurface"] = cs
    spec = importlib.util.spec_from_file_location("LOMBridgeTest", os.path.join(ROOT, "LOMBridge", "__init__.py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    mod.CONN_FILE = os.path.join(tmpdir, "connection.json")
    mod.LOMBridge._song = song
    b = mod.LOMBridge(None)
    b._sock = FakeSock(); b._song = song
    return mod, b

class FakeSock:
    def __init__(self): self.sent = []; self.inbox = []
    def sendto(self, data, addr): self.sent.append((addr, data))
    def recvfrom(self, n):
        if not self.inbox: raise BlockingIOError()
        return self.inbox.pop(0)
    def close(self): pass

def _load(p):
    with open(p) as f: return json.load(f)

def decode_sent(mod, sock): return [mod.osc_unpack(d) for _, d in sock.sent]

import lom

class TestOSC(unittest.TestCase):
    def test_big_ints_roundtrip_exact(self):
        for v in (9000000001, 9000000002, 2**40 + 7, -5, 7):
            self.assertEqual(lom.osc_unpack(lom.osc_pack("/x", [v]))[1], [v])
    def test_refs_and_strings_untouched(self):
        a = ["o:123456:9000000001", "AUDIO - Sub", "17|1", "#rid", "!tok"]
        self.assertEqual(lom.osc_unpack(lom.osc_pack("/x", a))[1], a)
    def test_num_keeps_refs_and_ints(self):
        self.assertEqual(lom.num("1140992001"), 1140992001); self.assertIsInstance(lom.num("1140992001"), int)
        self.assertEqual(lom.num("o:1:2"), "o:1:2"); self.assertEqual(lom.num("1.5"), 1.5); self.assertEqual(lom.num("17|1"), "17|1")
    def test_parse_time(self):
        self.assertEqual(lom.parse_time("17|1"), 64.0); self.assertEqual(lom.parse_time("5|2|3"), 17.5)
        with self.assertRaises(ValueError): lom.parse_time("abc")

class TestPure(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(); self.song = FakeSong([]); self.mod, self.b = load_bridge(self.song, self.tmp)
    def test_interp_sides(self):
        pts = [(0, 1.0), (4, 1.0), (4, 0.0), (8, 0.0)]; f = lambda x: x
        self.assertEqual(self.mod.interp(pts, f, 4, "right"), 0.0); self.assertEqual(self.mod.interp(pts, f, 4, "left"), 1.0)
        self.assertAlmostEqual(self.mod.interp([(0, 0.0), (8, 1.0)], f, 2), 0.25)
    def test_breakpoint_budget_matches(self):
        pts = [(0, 0.0), (10, 1.0), (10, 0.2), (30, 0.9)]; f = self.mod.curve_fn("exp")
        n = self.mod.count_breakpoints(pts, 8, False); self.assertEqual(n, len(self.mod.breakpoints(pts, f, 8, False)))
        self.assertEqual(self.mod.count_breakpoints(pts, 8, True), len(self.mod.breakpoints(pts, f, 8, True)))
    def test_simplify_keeps_corners(self):
        pts = [(t, (0.0 if t < 4 else 1.0)) for t in range(0, 9)]
        s = self.mod.simplify(pts); self.assertEqual(s[0], (0, 0.0)); self.assertEqual(s[-1], (8, 1.0)); self.assertLess(len(s), len(pts))

class TestProtocol(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(); self.song = FakeSong([FakeTrack("3-MIDI")]); self.mod, self.b = load_bridge(self.song, self.tmp)
        self.tok = _load(self.mod.CONN_FILE)["token"]
    def send(self, cmd, *args, rid="r1", token=None):
        tok = self.tok if token is None else token
        self.b._sock.inbox.append((self.mod.osc_pack(cmd, list(args) + ["!" + tok, "#" + rid]), ("127.0.0.1", 5555)))
        self.b._sock.sent = []; self.b._poll(); return decode_sent(self.mod, self.b._sock)
    def test_token_file_created_at_init(self):
        c = _load(self.mod.CONN_FILE); self.assertEqual(c["port"], 7421); self.assertEqual(len(c["token"]), 32)
        self.assertEqual(oct(os.stat(self.mod.CONN_FILE).st_mode & 0o777), "0o600")
    def test_token_required(self):
        out = self.send("/ping", token="faux"); self.assertEqual(out[1][0], "/err"); self.assertIn("jeton", out[1][1][1])
    def test_every_line_carries_rid(self):
        out = self.send("/children", "live_set", "tracks", rid="abc")
        self.assertEqual([o[0] for o in out], ["/begin", "/r", "/end"]); self.assertTrue(all(o[1][0] == "abc" for o in out))
    def test_ref_roundtrip_no_loss(self):
        out = self.send("/children", "live_set", "tracks"); ref = out[1][1][2]
        self.assertTrue(ref.startswith("o:")); self.assertIs(self.b._obj(ref), self.song.tracks[0])
        # sur le fil : la référence traverse OSC inchangée, même avec un grand compteur
        self.b._next_id = 9000000001; ref2 = self.b._ref(self.song.master_track)
        self.assertEqual(lom.osc_unpack(lom.osc_pack("/x", [ref2]))[1], [ref2]); self.assertIs(self.b._obj(ref2), self.song.master_track)
    def test_numeric_ids_refused_and_foreign_session(self):
        with self.assertRaises(ValueError): self.b._resolve("25")
        with self.assertRaises(ValueError): self.b._resolve("id 25")
        with self.assertRaises(ValueError): self.b._obj("o:000000:1")
    def test_client_filters_foreign_lines(self):
        class S:
            def __init__(s): s.q = []; s.sent = []
            def setblocking(s, b): pass
            def settimeout(s, t): pass
            def bind(s, a): pass
            def sendto(s, d, a):
                s.sent.append(d); rid = [x for x in lom.osc_unpack(d)[1] if str(x).startswith("#")][0][1:]
                s.q = [lom.osc_pack("/begin", ["OLD", "/read"]), lom.osc_pack("/r", ["OLD", "late"]), lom.osc_pack("/end", ["OLD", "/read"]),
                       lom.osc_pack("/begin", [rid, "/ping"]), lom.osc_pack("/r", [rid, "pong"]), lom.osc_pack("/r", ["OLD", "late2"]), lom.osc_pack("/end", [rid, "/ping"])]
            def recvfrom(s, n):
                if not s.q: raise BlockingIOError()
                return s.q.pop(0), ("127.0.0.1", 1)
        br = lom.Bridge.__new__(lom.Bridge); br.host, br.tx, br.timeout, br.token, br._seq = "127.0.0.1", 1, 2, "t", 0; br.sock = S()
        r = br.send("/ping"); self.assertTrue(r["ok"]); self.assertEqual(r["rows"], [["pong"]])
    def test_http_allowlist(self):
        self.assertFalse(lom.http_allowed("/py")); self.assertFalse(lom.http_allowed("/set")); self.assertTrue(lom.http_allowed("/plan")); self.assertTrue(lom.http_allowed("/py", unsafe=True))

class TestPlanAndRebuild(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.track = FakeTrack("3-MIDI", [FakeClip("A", 16.0, 32.0), FakeClip("B", 32.0, 48.0)])
        self.audio = FakeTrack("1-tone", [FakeClip("tone", 16.0, 24.0, audio=True)], midi=False)
        self.song = FakeSong([self.track, self.audio]); self.mod, self.b = load_bridge(self.song, self.tmp)
        self.vol = self.track.mixer_device.volume; self.vref = self.b._ref(self.vol)
    def plan(self, *a): return self.b._build_plan(list(a))
    def test_zero_window_refused_unless_hold(self):
        p = self.plan("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 20.0, 0.5)
        self.assertTrue(any("durée nulle" in e for e in p["errors"]))
        p = self.plan("3-MIDI", self.vref, "raw", 8, "lin", 1, "expressions", 20.0, 0.5)
        self.assertEqual(p["errors"], []); self.assertEqual(p["t_hi"], 32.0)
    def test_clamp_reported(self):
        p = self.plan("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 0.2, 20.0, 5.0)
        self.assertTrue(any("hors" in e for e in p["errors"]))
        p = self.plan("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions,clamp", 16.0, 0.2, 20.0, 5.0)
        self.assertEqual(p["errors"], []); self.assertEqual(p["points"][1]["clamped"], 1); self.assertTrue(any("saturée" in w for w in p["warnings"]))
    def test_audio_requires_accept_fades(self):
        vref = self.b._ref(self.audio.mixer_device.volume)
        p = self.plan("1-tone", vref, "raw", 8, "lin", 0, "-", 16.0, 0.2, 20.0, 0.4); self.assertTrue(any("fondus" in e for e in p["errors"]))
        p = self.plan("1-tone", vref, "raw", 8, "lin", 0, "fades", 16.0, 0.2, 20.0, 0.4); self.assertEqual(p["errors"], [])
    def test_budget_before_generation(self):
        p = self.plan("3-MIDI", self.vref, "raw", 64, "exp", 0, "expressions", 16.0, 0.0, 116.0, 1.0)
        self.assertTrue(any("trop de points" in e for e in p["errors"])); self.assertNotIn("_pts", p) if p["errors"] else None
    def test_looped_stretched_refused(self):
        c = FakeClip("L", 48.0, 64.0, looping=True, loop_len=4.0); self.track.arrangement_clips.append(c)
        p = self.plan("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 50.0, 0.2, 52.0, 0.4); self.assertTrue(any("étiré" in e for e in p["errors"]))
    def test_res_and_accept_validation(self):
        with self.assertRaises(ValueError): self.plan("3-MIDI", self.vref, "raw", -1, "lin", 0, "expressions", 16.0, 0.2, 20.0, 0.4)
        with self.assertRaises(ValueError): self.plan("3-MIDI", self.vref, "raw", 8, "lin", 0, "nimporte", 16.0, 0.2, 20.0, 0.4)
    def test_old_points_exact_anchors(self):
        env = FakeEnvelope(self.vol, [(0.0, 0.0), (16.0, 1.0)]); clip = self.track.arrangement_clips[0]; clip.automation_envelopes = [env]
        out = {}; list(self.b._old_points(clip, self.vol, (20.0, 24.0), out))
        self.assertEqual(out["before"][-1][0], 4.0); self.assertAlmostEqual(out["before"][-1][1], 0.25, places=5)
        self.assertEqual(out["after"][0][0], 8.0); self.assertAlmostEqual(out["after"][0][1], 0.5, places=5)
        self.assertTrue(all(t < 4.0 for t, v in out["before"][:-1])); self.assertTrue(all(t > 8.0 for t, v in out["after"][1:]))
        out = {}; list(self.b._old_points(clip, self.vol, (16.0, 24.0), out)); self.assertEqual(out["before"], [])   # fenêtre collée au début : pas d'ancrage
    def test_shape_orders_jump_and_writes_events(self):
        rows = []; reply = lambda *a: rows.append(a)
        gen = self.b.cmd_shape(reply, ["3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 1.0, 32.0, 1.0, 32.0, 0.0, 48.0, 0.0])
        list(gen)
        self.assertEqual(rows[0][0], "shape"); self.assertEqual(rows[0][1], 2)
        created = [s.clip for s in []]  # les clips de session sont supprimés ; on relit les appels de duplication
        (c1, t1), (c2, t2) = self.track.dup_calls; self.assertEqual((t1, t2), (16.0, 32.0))
        e1 = c1.envs_created["Track Volume"].created; e2 = c2.envs_created["Track Volume"].created
        self.assertEqual(e1[0], (0.0, 1.0)); self.assertEqual(e1[-1], (16.0, 1.0))      # clip A : valeur avant le saut jusqu'à sa fin
        self.assertEqual(e2[0], (0.0, 0.0)); self.assertEqual(e2[-1], (16.0, 0.0))      # clip B : valeur après le saut dès son début
        self.assertEqual(self.song.undo_log, ["begin", "end"])
    def test_trimmed_midi_clip_rebuilt_exactly(self):
        c = FakeClip("Hook 3", 176.0, 336.0); c.timeline = 1e18; c.end_marker = 580.0; c.start_marker = 420.0; c.loop_start, c.loop_end, c.length = 420.0, 580.0, 160.0
        self.track.arrangement_clips = [c]; self.track.mixer_device.volume.automation_state = 0
        rows = []; gen = self.b.cmd_shape(lambda *a: rows.append(a), ["3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 256.0, 0.2, 272.0, 0.8]); list(gen)
        (sess, t), = self.track.dup_calls
        self.assertGreaterEqual(sess.timeline, 580.0); self.assertEqual((sess.start_marker, sess.end_marker), (420.0, 580.0))
        nc = self.track.arrangement_clips[0]; self.assertEqual((nc.start_time, nc.end_time), (176.0, 336.0))
        ev = sess.envs_created["Track Volume"].created; self.assertEqual(ev[0][0], 500.0); self.assertEqual(ev[-1][0], 516.0)   # temps relatifs = 256-176+420
    def test_post_condition_triggers_auto_undo(self):
        c = FakeClip("Bad", 16.0, 32.0); self.track.arrangement_clips = [c]
        orig = self.track.duplicate_clip_to_arrangement
        def bad_dup(clip, t):
            nc = orig(clip, t); nc.end_time = t + 999.0; return nc
        self.track.duplicate_clip_to_arrangement = bad_dup; self.song.undo_calls = []; self.song.undo = lambda: self.song.undo_calls.append(1)
        rows = []; gen = self.b.cmd_shape(lambda *a: rows.append(a), ["3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 0.2, 20.0, 0.4])
        with self.assertRaises(ValueError) as cm: list(gen)
        self.assertIn("annulée automatiquement", str(cm.exception)); self.assertEqual(self.song.undo_calls, [1]); self.assertEqual(self.song.undo_log[-1], "end")
    def test_rebuild_cleans_up_on_error(self):
        clip = self.track.arrangement_clips[0]; self.track.fail_duplicate = True; slot = self.track.clip_slots[0]
        with self.assertRaises(RuntimeError): self.b._rebuild(self.track, clip, [(self.vol, [(0.0, 0.5)])], [], set(["expressions"]))
        self.assertEqual(slot.deleted, 1); self.assertFalse(slot.has_clip)
    def shape(self, *a, **kw):
        rows = []; gen = self.b.cmd_shape(lambda *x: rows.append(x), list(a)); return rows, gen
    def verified_row(self, rows): return next(r for r in rows if r[0] == "verified")
    def test_verified_exact_after_shape(self):
        rows, gen = self.shape("3-MIDI", self.vref, "raw", 8, "exp", 0, "expressions", 16.0, 0.1, 40.0, 0.9); list(gen)
        v = self.verified_row(rows); self.assertEqual(v[4], "exact"); self.assertGreater(v[1], 10); self.assertLessEqual(v[2], v[3])
        self.assertEqual(self.song.undo_calls, [])
    def test_partial_failure_rolls_back_all(self):
        before = list(self.track.arrangement_clips); orig = self.track.duplicate_clip_to_arrangement
        def dup(clip, t):
            if self.track.dup_calls: raise RuntimeError("clip B impossible")   # le 1er clip est déjà remplacé
            return orig(clip, t)
        self.track.duplicate_clip_to_arrangement = dup
        rows, gen = self.shape("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 0.2, 48.0, 0.8)
        with self.assertRaises(ValueError) as cm: list(gen)
        self.assertIn("1 clip(s) remis", str(cm.exception)); self.assertIn("rien n'est modifié", str(cm.exception))
        self.assertEqual(self.song.undo_calls, [1]); self.assertEqual(self.track.arrangement_clips, before)
        self.assertEqual(self.song.undo_log, ["begin", "end"]); self.assertEqual(rows, [])
    def test_failure_before_any_write_does_not_undo(self):
        before = list(self.track.arrangement_clips); self.track.fail_duplicate = True
        rows, gen = self.shape("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 0.2, 20.0, 0.8)
        with self.assertRaises(ValueError) as cm: list(gen)
        self.assertIn("rien n'est modifié", str(cm.exception)); self.assertNotIn("annulée automatiquement", str(cm.exception))
        self.assertEqual(self.song.undo_calls, []); self.assertEqual(self.track.arrangement_clips, before)
    def test_verify_failure_triggers_undo(self):
        before = list(self.track.arrangement_clips); orig = self.track.duplicate_clip_to_arrangement
        def corrupt(clip, t):
            nc = orig(clip, t)
            for ev in nc.automation_envelopes: ev.events = [(tt, 0.0) for tt, _ in ev.events]   # Live n'aurait pas écrit ce qu'on lui a donné
            return nc
        self.track.duplicate_clip_to_arrangement = corrupt
        rows, gen = self.shape("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 0.2, 20.0, 0.8)
        with self.assertRaises(ValueError) as cm: list(gen)
        self.assertIn("relecture", str(cm.exception)); self.assertIn("annulée automatiquement", str(cm.exception))
        self.assertEqual(self.song.undo_calls, [1]); self.assertEqual(self.track.arrangement_clips, before)
        self.assertEqual(rows[0][0], "shape")   # les lignes d'écriture ont été émises avant la relecture, puis l'erreur
    def test_accept_unverified_skips_verification(self):
        orig = self.track.duplicate_clip_to_arrangement
        def corrupt(clip, t):
            nc = orig(clip, t)
            for ev in nc.automation_envelopes: ev.events = [(tt, 0.0) for tt, _ in ev.events]
            return nc
        self.track.duplicate_clip_to_arrangement = corrupt
        rows, gen = self.shape("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions,unverified", 16.0, 0.2, 20.0, 0.8); list(gen)
        self.assertEqual(self.verified_row(rows)[4], "skipped"); self.assertEqual(self.song.undo_calls, [])
    def _audio_following(self):
        """Piste audio réelle : enveloppes non exposées, paramètre qui suit l'automation existante 0,2 → 0,8 sur 16–24."""
        self.audio.expose = False; vol = FollowParam("Track Volume", automation_state=1); vol.song, vol.track = self.song, self.audio
        self.audio.mixer_device.volume = vol; clip = self.audio.arrangement_clips[0]
        clip.hidden_envelopes = [FakeEnvelope(vol, [(0.0, 0.2), (8.0, 0.8)])]
        return vol, self.b._ref(vol)
    def test_no_undo_step_open_across_pauses_and_sampled_verify(self):
        vol, vref = self._audio_following()
        rows, gen = self.shape("1-tone", vref, "raw", 8, "lin", 0, "fades", 18.0, 0.5, 20.0, 0.5)
        pauses = 0
        for _ in gen:
            pauses += 1; self.assertEqual(self.song.undo_log.count("begin"), self.song.undo_log.count("end"), "étape d'annulation ouverte pendant une pause")
        self.assertGreater(pauses, 5); self.assertEqual(self.song.undo_log, ["begin", "end"])
        v = self.verified_row(rows); self.assertEqual(v[4], "sampled"); self.assertEqual(v[1], 5); self.assertLessEqual(v[2], v[3])
        self.song.current_song_time = 17.0; self.assertAlmostEqual(vol.value, 0.275, places=3)   # ancienne rampe conservée
        self.song.current_song_time = 19.0; self.assertAlmostEqual(vol.value, 0.5, places=3)
        self.song.current_song_time = 23.0; self.assertAlmostEqual(vol.value, 0.725, places=3)
    def test_sampled_verify_catches_wrong_write(self):
        vol, vref = self._audio_following(); before = list(self.audio.arrangement_clips); orig = self.audio.duplicate_clip_to_arrangement
        def corrupt(clip, t):
            nc = orig(clip, t)
            for ev in nc.hidden_envelopes: ev.events = [(tt, min(1.0, v + 0.1)) for tt, v in ev.events]
            return nc
        self.audio.duplicate_clip_to_arrangement = corrupt
        rows, gen = self.shape("1-tone", vref, "raw", 8, "lin", 0, "fades", 18.0, 0.5, 20.0, 0.5)
        with self.assertRaises(ValueError) as cm: list(gen)
        self.assertIn("(sampled)", str(cm.exception)); self.assertEqual(self.song.undo_calls, [1]); self.assertEqual(self.audio.arrangement_clips, before)
    def test_override_refused_when_sampling_needed(self):
        vol, vref = self._audio_following(); vol.automation_state = 2
        p = self.plan("1-tone", vref, "raw", 8, "lin", 0, "fades", 18.0, 0.5, 20.0, 0.5)
        self.assertTrue(any("surchargée" in e for e in p["errors"]))
        # enveloppe exposée : pas d'échantillonnage, l'état 2 n'empêche rien
        self.vol.automation_state = 2; self.track.arrangement_clips[0].automation_envelopes = [FakeEnvelope(self.vol, [(0.0, 0.0), (16.0, 1.0)])]
        p = self.plan("3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 18.0, 0.5, 20.0, 0.5); self.assertEqual(p["errors"], [])
    def test_clear_transactional_and_verified(self):
        clip = self.track.arrangement_clips[0]; clip.automation_envelopes = [FakeEnvelope(self.vol, [(0.0, 0.0), (16.0, 1.0)])]
        rows = []; gen = self.b.cmd_clear(lambda *x: rows.append(x), ["3-MIDI", self.vref, 20.0, 24.0, "expressions"]); list(gen)
        self.assertEqual(rows[0], ("cleared", 1)); self.assertEqual(self.verified_row(rows)[4], "exact")
        (sess, _), = self.track.dup_calls; times = [t for t, _ in sess.envs_created["Track Volume"].created]
        self.assertTrue(all(t <= 4.0 or t >= 8.0 for t in times)); self.assertIn(4.0, times); self.assertIn(8.0, times)
        self.assertEqual(self.song.undo_log, ["begin", "end"]); self.assertEqual(self.song.undo_calls, [])
    def test_ping_lists_commands_and_single_version(self):
        rows = []; self.b.cmd_ping(lambda *x: rows.append(x), [])
        self.assertEqual(rows[0][:2], ("pong", self.mod.VERSION)); self.assertEqual(lom.VERSION, self.mod.VERSION)
        cmds = next(r for r in rows if r[0] == "commands"); self.assertIn("/shape", cmds); self.assertIn("/ping", cmds)
        self.assertIn("unverified", next(r for r in rows if r[0] == "accept")[1])
    def test_job_cancel_by_id_and_revalidation(self):
        self.song.is_playing = False; rows = []
        def dispatch(cmd, args, rid):
            self.b._sock.inbox.append((self.mod.osc_pack(cmd, list(args) + ["!" + _load(self.mod.CONN_FILE)["token"], "#" + rid]), ("127.0.0.1", 1)))
            self.b._poll()
        dispatch("/read", ["3-MIDI", self.vref, 0, 4, 1], "j1"); dispatch("/read", ["3-MIDI", self.vref, 0, 4, 1], "j2")
        self.assertEqual([j["rid"] for j in self.b._jobs], ["j1", "j2"])
        self.b._sock.sent = []; dispatch("/cancel", ["j2"], "c1")
        out = decode_sent(self.mod, self.b._sock); self.assertIn(("/err", ["j2", "/read: annulée"]), out); self.assertEqual([j["rid"] for j in self.b._jobs], ["j1"])
        for _ in range(10): self.b._job_tick()
        self.assertEqual(self.b._jobs, [])
        # annulation d'une tâche EN COURS : elle s'arrête d'elle-même à sa prochaine pause, sans fermeture forcée
        self.song.current_song_time = 3.0
        dispatch("/read", ["3-MIDI", self.vref, 0, 40, 1], "j3"); self.b._job_tick(); self.b._job_tick()
        self.b._sock.sent = []; dispatch("/cancel", ["j3"], "c2"); self.b._job_tick()
        out = decode_sent(self.mod, self.b._sock); self.assertIn(("/err", ["j3", "/read: annulée"]), out); self.assertEqual(self.b._jobs, [])
        self.assertEqual(self.song.current_song_time, 3.0)   # curseur restauré
    def test_cancel_during_verification_keeps_the_write(self):
        vol, vref = self._audio_following()
        rows, gen = self.shape("1-tone", vref, "raw", 8, "lin", 0, "fades", 18.0, 0.5, 20.0, 0.5)
        while not any(r[0] == "shape" for r in rows): next(gen)     # écrit ; la relecture par curseur commence
        self.b._jobs = [{"gen": gen, "cancel": True, "started": True, "rid": "x", "cmd": "/shape", "addr": None}]
        list(gen)
        self.assertEqual(self.verified_row(rows)[4], "interrupted"); self.assertTrue(any(r[0] == "warn" and "interrompue" in r[1] for r in rows))
        self.assertEqual(self.song.undo_calls, []); self.song.current_song_time = 19.0; self.assertAlmostEqual(vol.value, 0.5, places=3)
        # revalidation : clip disparu entre plan et exécution
        rows = []; gen = self.b.cmd_shape(lambda *a: rows.append(a), ["3-MIDI", self.vref, "raw", 8, "lin", 0, "expressions", 16.0, 0.2, 20.0, 0.4])
        self.track.arrangement_clips.pop(0)
        with self.assertRaises(ValueError) as cm: list(gen)
        self.assertIn("disparu", str(cm.exception)); self.assertEqual(self.track.dup_calls, [])

if __name__ == "__main__": unittest.main()
