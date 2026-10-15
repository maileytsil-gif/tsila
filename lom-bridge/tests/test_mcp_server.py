# -*- coding: utf-8 -*-
"""Tests hors Live du connecteur MCP : python3 -W ignore -m unittest tests/test_mcp_server.py -v   (nécessite `pip install "mcp>=2"`)
Chaîne réelle : client MCP en mémoire -> mcp_server.py -> lom.Bridge (UDP réel, jeton lu dans un connection.json de test)
-> vrai Remote Script LOMBridge sur les faux objets de test_offline.py (même faux Live que tests/fake_live_server.py,
sur un port libre). Ignorés sans le paquet `mcp` 2.x. Ce n'est pas Live : rien ici ne prouve un rendu audio ni le comportement réel de l'API Live."""
import json, os, socket, sys, tempfile, threading, time, unittest
from unittest.mock import patch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "tests"))
from test_offline import FakeClip, FakeTrack, FakeSong, FollowParam, load_bridge   # noqa: E402
try:
    import mcp_server   # noqa: E402
    from mcp import Client   # noqa: E402
    HAVE_MCP = True
except (ImportError, SystemExit):   # mcp_server quitte avec un message si le SDK 2.x manque
    HAVE_MCP = False

READ_TOOLS = {"live_ping", "live_state", "live_read", "live_journal", "live_automation_preview"}
WRITE_TOOLS = {"live_automation_commit", "live_setparam", "live_snapshot", "live_restore", "live_notes_write", "live_load_device",
               "live_transport", "live_locator", "live_meters"}
SPEC = {"automations": [{"track": "3-MIDI", "device": "mixer", "param": "Volume", "accept": ["expressions"], "points": [["5|1", -3], ["9|1", 0]]}]}


class FakeLive:
    """Remote Script réel sur faux Set, UDP sur un port libre, connexion dans un dossier temporaire."""
    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.midi = FakeTrack("3-MIDI", [FakeClip("A", 16.0, 32.0), FakeClip("B", 32.0, 48.0)])
        self.audio = FakeTrack("AUDIO - Sub", [FakeClip("tone", 16.0, 32.0, audio=True)], midi=False, expose=False)
        self.song = FakeSong([self.midi, self.audio])
        vol = FollowParam("Track Volume", automation_state=1); vol.song, vol.track = self.song, self.audio; self.audio.mixer_device.volume = vol
        self.mod, self.bridge = load_bridge(self.song, self.tmp.name)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); self.sock.bind(("127.0.0.1", 0)); self.sock.setblocking(False)
        self.mod.RX_PORT = self.sock.getsockname()[1]; self.bridge._sock = self.sock
        self.bridge._tok = None; self.bridge._token()
        self.conn = self.mod.CONN_FILE
        with open(self.conn) as f: self.token = json.load(f)["token"]
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._loop, daemon=True); self._thread.start()
    def _loop(self):
        while not self._stop.is_set(): self.bridge.update_display(); time.sleep(0.003)
    def close(self):
        self._stop.set(); self._thread.join(2); self.sock.close(); self.tmp.cleanup()


@unittest.skipUnless(HAVE_MCP, 'pip install "mcp>=2"')
class McpTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.live = FakeLive(); self.addCleanup(self.live.close)
        patcher = patch.dict(os.environ, {"LOM_BRIDGE_CONN": self.live.conn}); patcher.start(); self.addCleanup(patcher.stop)
        self.outputs = []

    async def call(self, client, tool, **args):
        r = await client.call_tool(tool, args)
        text = " ".join(getattr(x, "text", "") for x in r.content)
        self.outputs.append(text)
        return r, text

    async def writes_journaled(self, client):
        """Commandes d'écriture du journal du bridge (la lecture de la signature, `/transport` sans argument, y est aussi consignée)."""
        r, _ = await self.call(client, "live_journal", n=50)
        return [e["cmd"] for e in r.structured_content["entries"] if e["cmd"] != "/transport"]

    def assertNoToken(self):
        self.assertFalse(any(self.live.token in o for o in self.outputs), "le jeton ne doit apparaître dans aucune réponse")

    # --- ce qui est exposé ---
    async def test_read_only_mode_exposes_no_writer(self):
        async with Client(mcp_server.build_server(False)) as c:
            tools = (await c.list_tools()).tools
        self.assertEqual({t.name for t in tools}, READ_TOOLS)
        self.assertTrue(all(t.annotations.read_only_hint for t in tools))

    async def test_write_mode_adds_the_writers_and_never_the_raw_ones(self):
        async with Client(mcp_server.build_server(True)) as c:
            tools = (await c.list_tools()).tools
        self.assertEqual({t.name for t in tools}, READ_TOOLS | WRITE_TOOLS)
        self.assertFalse(any(x in t.name for t in tools for x in ("py", "reload", "call", "set_", "shape", "clear")))
        self.assertTrue(all(not t.annotations.read_only_hint for t in tools if t.name in WRITE_TOOLS))

    # --- lecture ---
    async def test_ping_state_and_read(self):
        async with Client(mcp_server.build_server(False)) as c:
            r, _ = await self.call(c, "live_ping")
            self.assertFalse(r.is_error); self.assertEqual(r.structured_content["rows"][0][0], "pong"); self.assertIs(r.structured_content["write_enabled"], False)
            r, _ = await self.call(c, "live_state")
            self.assertEqual([t["name"] for t in r.structured_content["state"]["tracks"][:2]], ["3-MIDI", "AUDIO - Sub"])
            r, _ = await self.call(c, "live_read", command="/param", args=["AUDIO - Sub", "mixer", "Volume"])
            self.assertEqual(r.structured_content["rows"][0][1], "Track Volume")
            r, _ = await self.call(c, "live_read", command="clips", args=["3-MIDI"])   # « / » facultatif
            self.assertEqual([row[3] for row in r.structured_content["rows"]], ["A", "B"])
            r, _ = await self.call(c, "live_read", command="/notes", args=["get", "3-MIDI", "5|1"])   # « mesure|temps » converti
            self.assertEqual(r.structured_content["rows"][0][2], "A")
        self.assertNoToken()

    async def test_read_refuses_everything_that_writes_before_any_request(self):
        attempts = [("/py", ["1"]), ("/set", ["live_set", "tempo", 100]), ("/call", ["live_set", "stop_playing"]), ("/reload", []), ("/shape", ["3-MIDI"]),
                    ("/setparam", ["3-MIDI", "mixer", "Volume", -6]), ("/load", ["3-MIDI", "Pro-Q 4"]), ("/clear", ["3-MIDI"]), ("/meters", ["1|1", 1]),
                    ("/transport", ["play"]), ("/notes", ["set", "3-MIDI", "5|1", "[]"]), ("/notes", []), ("/locator", ["5|1", "x"])]
        with patch.object(mcp_server, "bridge", side_effect=AssertionError("aucune requête attendue")):
            async with Client(mcp_server.build_server(False)) as c:
                for cmd, args in attempts:
                    r, text = await self.call(c, "live_read", command=cmd, args=args)
                    self.assertTrue(r.is_error and "liste blanche" in text, (cmd, args, text))

    async def test_bridge_error_keeps_its_stable_code(self):
        async with Client(mcp_server.build_server(False)) as c:
            r, text = await self.call(c, "live_read", command="/track", args=["inexistante"])
        self.assertTrue(r.is_error); self.assertIn("[E_NOT_FOUND]", text)

    async def test_missing_or_wrong_connection_fails_cleanly(self):
        async with Client(mcp_server.build_server(False)) as c:
            with patch.dict(os.environ, {"LOM_BRIDGE_CONN": os.path.join(self.live.tmp.name, "absent.json")}):
                r, text = await self.call(c, "live_ping")
            self.assertTrue(r.is_error); self.assertIn("fichier de connexion absent", text)
            bad = os.path.join(self.live.tmp.name, "bad.json")
            with open(bad, "w") as f: json.dump({"port": json.load(open(self.live.conn))["port"], "token": "mauvais"}, f)
            with patch.dict(os.environ, {"LOM_BRIDGE_CONN": bad}), patch.object(mcp_server, "READ_TIMEOUT", 1.0):
                r, text = await self.call(c, "live_ping")
            self.assertTrue(r.is_error); self.assertIn("E_", text)
        self.assertNoToken()

    # --- écriture ---
    async def test_setparam_snapshot_restore(self):
        async with Client(mcp_server.build_server(True)) as c:
            vol = self.live.midi.mixer_device.volume; before = vol.value
            r, _ = await self.call(c, "live_snapshot", track="3-MIDI"); self.assertFalse(r.is_error)
            snap = next(row[1] for row in r.structured_content["rows"] if row[0] == "snapshot")
            r, _ = await self.call(c, "live_setparam", track="3-MIDI", device="mixer", param="Volume", value=-6)
            self.assertFalse(r.is_error); self.assertNotAlmostEqual(vol.value, before, places=3)
            r, _ = await self.call(c, "live_restore", snapshot_id=snap)
            self.assertFalse(r.is_error); self.assertAlmostEqual(vol.value, before, places=6)

    async def test_setparam_refuses_automated_parameter_unless_override(self):
        async with Client(mcp_server.build_server(True)) as c:
            vol = self.live.audio.mixer_device.volume; before = vol.value
            r, text = await self.call(c, "live_setparam", track="AUDIO - Sub", device="mixer", param="Volume", value=-3)
            self.assertTrue(r.is_error); self.assertIn("[E_AUTOMATED]", text); self.assertEqual(vol.value, before)

    async def test_notes_write_then_read_back(self):
        async with Client(mcp_server.build_server(True)) as c:
            r, _ = await self.call(c, "live_notes_write", mode="set", track="3-MIDI", clip="5|1", notes=[{"pitch": 60, "start": 0, "duration": 1}, {"pitch": 64, "start": 1, "duration": 1, "velocity": 90}])
            self.assertFalse(r.is_error)
            r, _ = await self.call(c, "live_read", command="/notes", args=["get", "3-MIDI", "5|1"])
            self.assertEqual([row[1] for row in r.structured_content["rows"] if row[0] == "note"], [60, 64])
            r, text = await self.call(c, "live_notes_write", mode="set", track="3-MIDI", clip="5|1", notes=[{"pitch": 200, "start": 0, "duration": 1}])
            self.assertTrue(r.is_error)   # refusé par le schéma, rien d'envoyé
            for bad in ({"window_start": 0.0}, {"mode": "add", "window_start": 0.0, "window_end": 2.0}):
                r, text = await self.call(c, "live_notes_write", **{"mode": "set", "track": "3-MIDI", "clip": "5|1", "notes": [{"pitch": 60, "start": 0, "duration": 1}], **bad})
                self.assertTrue(r.is_error, bad)

    async def test_transport_and_locator_use_bars_and_beats(self):
        async with Client(mcp_server.build_server(True)) as c:
            r, _ = await self.call(c, "live_transport", action="pos", position="5|1")
            self.assertFalse(r.is_error); self.assertEqual(self.live.song.current_song_time, 16.0)
            r, _ = await self.call(c, "live_locator", time="9|1", name="Drop")
            self.assertFalse(r.is_error); self.assertEqual([(c_.time, c_.name) for c_ in self.live.song.cue_points], [(32.0, "Drop")])
            r, text = await self.call(c, "live_transport", action="pos"); self.assertTrue(r.is_error); self.assertIn("exige", text)

    async def test_arguments_sent_to_the_bridge(self):
        sent = []
        def capture(command, args=(), *a, **kw): sent.append((command, list(args))); return [], None
        with patch.object(mcp_server, "run", side_effect=capture):
            async with Client(mcp_server.build_server(True)) as c:
                await self.call(c, "live_load_device", track="PAD", name="Serum 2", replace="Wavetable")
                await self.call(c, "live_load_device", track="PAD", name="Pro-Q 4")
                await self.call(c, "live_setparam", track="PAD", device="mixer", param="Volume", value=-6, unit="raw", override=True)
                await self.call(c, "live_transport", action="loop", position="5|1", loop_length=16)
                await self.call(c, "live_transport", action="loop_off")
                await self.call(c, "live_meters", start="17|1", seconds=5, tracks=["AUDIO - Kick"])
                await self.call(c, "live_notes_write", mode="set", track="PAD", clip="o:1:4", notes=[{"pitch": 60, "start": 0, "duration": 1}], window_start=0, window_end=4)
                r, _ = await self.call(c, "live_meters", start=1, seconds=31); self.assertTrue(r.is_error)
        self.assertEqual(sent[0], ("/load", ["PAD", "Serum 2", "plugins", "replace=Wavetable"]))
        self.assertEqual(sent[1], ("/load", ["PAD", "Pro-Q 4", "plugins"]))
        self.assertEqual(sent[2], ("/setparam", ["PAD", "mixer", "Volume", -6.0, "raw", "override"]))
        self.assertEqual(sent[3], ("/transport", ["loop", "5|1", 16.0]))
        self.assertEqual(sent[4], ("/transport", ["loop", "off"]))
        self.assertEqual(sent[5], ("/meters", ["17|1", 5.0, "AUDIO - Kick"]))
        self.assertEqual(sent[6][0], "/notes"); self.assertEqual(sent[6][1][:3], ["set", "PAD", "o:1:4"]); self.assertEqual(sent[6][1][4:], [0.0, 4.0])
        self.assertEqual(len(sent), 7)   # le dernier appel (seconds=31) est refusé avant toute requête

    # --- automation ---
    async def test_automation_preview_then_commit(self):
        async with Client(mcp_server.build_server(True)) as c:
            r, _ = await self.call(c, "live_automation_preview", spec=SPEC)
            self.assertFalse(r.is_error); sc = r.structured_content
            self.assertEqual(len(sc["sha256"]), 64); self.assertEqual(len(sc["plan_sha256"]), 64)
            self.assertEqual(await self.writes_journaled(c), [], "le preview n'écrit rien")
            ref = sc["preview"][0]["param"]["ref"]
            r, text = await self.call(c, "live_automation_commit", spec=SPEC, sha256=sc["sha256"], plan_sha256=sc["plan_sha256"])
            self.assertFalse(r.is_error, text); self.assertIs(r.structured_content["verify_in_live"], True)
            self.assertEqual(await self.writes_journaled(c), ["/shape"])
            r, _ = await self.call(c, "live_read", command="/events", args=["3-MIDI", ref])
            self.assertTrue(r.structured_content["rows"], "l'enveloppe écrite doit être relisible")
        self.assertNoToken()

    async def test_commit_refused_when_plan_or_spec_differs(self):
        async with Client(mcp_server.build_server(True)) as c:
            r, _ = await self.call(c, "live_automation_preview", spec=SPEC); sc = r.structured_content
            r, text = await self.call(c, "live_automation_commit", spec=SPEC, sha256=sc["sha256"], plan_sha256="0" * 64)
            self.assertTrue(r.is_error); self.assertIn("plan différent", text)
            changed = json.loads(json.dumps(SPEC)); changed["automations"][0]["points"][0][1] = -4
            r, text = await self.call(c, "live_automation_commit", spec=changed, sha256=sc["sha256"], plan_sha256=sc["plan_sha256"])
            self.assertTrue(r.is_error); self.assertIn("spec a changé", text)
            self.assertEqual(await self.writes_journaled(c), [], "aucune écriture après deux refus")

    async def test_preview_refuses_uncovered_range_and_empty_spec(self):
        far = {"automations": [{"track": "3-MIDI", "param": "Volume", "accept": ["expressions"], "points": [["5|1", -3], ["30|1", 0]]}]}
        async with Client(mcp_server.build_server(True)) as c:
            r, text = await self.call(c, "live_automation_preview", spec=far); self.assertTrue(r.is_error); self.assertIn("non couverte", text)
            r, text = await self.call(c, "live_automation_preview", spec={"automations": []}); self.assertTrue(r.is_error)
            r, text = await self.call(c, "live_automation_preview", spec={"automations": [{"track": "3-MIDI", "points": [["5|1", 0], ["9|1", 1]]}]})
            self.assertTrue(r.is_error); self.assertIn("param explicite", text)


if __name__ == "__main__":
    unittest.main()
