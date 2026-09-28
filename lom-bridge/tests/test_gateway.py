# -*- coding: utf-8 -*-
"""Tests hors Live du client agent_gateway.py : python3 -m unittest tests/test_gateway.py -v
Le serveur HTTP est remplacé par un faux (`post` simulé) ; le contrat vérifié est celui de lom.py 0.8.x :
jeton Bearer, réponses de `/apply` (`results[].ok/dry/plan{errors,gap,...}`), entrées `skip`, empreinte du plan."""
import io, json, os, sys, tempfile, unittest
from unittest.mock import patch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import agent_gateway as gw   # noqa: E402

SPEC = {"automations": [{"track": "AUDIO - Sub", "param": "Volume", "points": [["5|1", -3], ["9|1", 0]]}]}
PARAM = {"ref": "o:1:4", "name": "Track Volume", "min": 0, "max": 1, "value": 0.85, "display": "0.0 dB"}
def plan(gap=0.0, errors=(), clip_start=16.0):
    return {"points": [{"t": 16.0, "raw": 0.7, "display": "-3.0 dB", "clamped": 0}, {"t": 32.0, "raw": 0.85, "display": "0.0 dB", "clamped": 0}],
            "clips": [{"ref": "o:1:9", "start": clip_start, "end": 48.0, "window": [16.0, 32.0], "audio": 1, "exposes_envelope": 0, "problems": []}],
            "errors": list(errors), "warnings": [], "gap": gap, "n_points": 2, "sampling_seconds": 0.0}
def dry_reply(**kw): return {"log": ["DRY …"], "results": [{"index": 0, "ok": not kw.get("errors"), "dry": True, "param": PARAM, "plan": plan(**kw), "errors": [], "codes": []}]}
WET_OK = {"log": ["OK  …"], "results": [{"index": 0, "ok": True, "dry": False, "param": PARAM, "plan": plan(), "errors": [], "codes": []}]}


class GatewayTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.spec = os.path.join(self.tmp.name, "spec.json"); self.write(SPEC)
        self.conn = os.path.join(self.tmp.name, "connection.json")
        with open(self.conn, "w") as f: json.dump({"port": 7421, "token": "secret", "session": 1, "version": "0.8.1"}, f)
        self.out = io.StringIO()
    def write(self, spec):
        with open(self.spec, "w") as f: json.dump(spec, f)
    def run_gw(self, argv, replies):
        with patch.object(gw, "post", side_effect=replies) as mocked:
            code = gw.main(argv, out=self.out)
        return code, mocked, json.loads(self.out.getvalue())

    # --- garde-fous locaux ---
    def test_endpoint_loopback_only(self):
        for url in ("http://example.com:7480", "https://127.0.0.1:7480", "http://127.0.0.1:7480/cmd", "http://u:p@127.0.0.1:7480", "http://127.0.0.1:7480?x=1"):
            with self.assertRaises(ValueError, msg=url): gw.endpoint(url)
        self.assertEqual(gw.endpoint("http://127.0.0.1:7480/"), "http://127.0.0.1:7480")
    def test_read_only_allowlist(self):
        for cmd in ("/py", "/set", "/call", "/shape", "/clear", "/setparam", "/restore", "/locator", "/load", "/reload", "/cancel", "/meters"):
            self.assertFalse(gw.read_only(cmd, []), cmd)
        for cmd in ("/ping", "/state", "/param", "/clips", "/plan", "/read", "/journal", "/locators", "/snapshots"): self.assertTrue(gw.read_only(cmd, ["x"]), cmd)
        self.assertTrue(gw.read_only("/transport", [])); self.assertFalse(gw.read_only("/transport", ["stop"]))
        self.assertTrue(gw.read_only("/notes", ["get", "PAD", "17|1"])); self.assertFalse(gw.read_only("/notes", ["set", "PAD", "17|1", "[]"])); self.assertFalse(gw.read_only("/notes", []))
    def test_inspect_refuses_writes_before_any_request(self):
        with patch.object(gw, "post") as mocked:
            with self.assertRaises(ValueError): gw.main(["inspect", "/setparam", "A", "mixer", "Volume", "-3"], out=self.out)
            with self.assertRaises(ValueError): gw.main(["inspect", "/transport", "play"], out=self.out)
        mocked.assert_not_called()
    def test_bearer_token_from_connection_file_not_in_output(self):
        captured = {}
        class Resp(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *a): pass
        def fake_open(req, timeout):
            captured["auth"] = req.get_header("Authorization"); captured["url"] = req.full_url; return Resp(b'{"ok": true, "rows": [["pong"]], "errors": []}')
        with patch.object(gw.urllib.request, "urlopen", fake_open):
            r = gw.post("http://127.0.0.1:7480", "/cmd", {"cmd": "/ping", "args": []}, conn=self.conn)
        self.assertEqual(captured["auth"], "Bearer secret"); self.assertEqual(captured["url"], "http://127.0.0.1:7480/cmd"); self.assertTrue(r["ok"])
        with self.assertRaises(ValueError): gw.token(os.path.join(self.tmp.name, "absent.json"))
    def test_http_error_body_is_reported(self):
        def fail(req, timeout):
            raise gw.urllib.error.HTTPError(req.full_url, 401, "Unauthorized", {}, io.BytesIO(b'{"error": "Authorization: Bearer <token> requis"}'))
        with patch.object(gw.urllib.request, "urlopen", fail):
            with self.assertRaises(ValueError) as cm: gw.post("http://127.0.0.1:7480", "/cmd", {}, conn=self.conn)
        self.assertIn("401", str(cm.exception)); self.assertIn("Bearer", str(cm.exception))

    # --- spec ---
    def test_spec_validation(self):
        self.write({"automations": []});                                                            self.assertRaises(ValueError, gw.spec_from_file, self.spec)
        self.write({"automations": [{"track": "A", "param": "Volume", "points": [[0, 0]]}]});       self.assertRaises(ValueError, gw.spec_from_file, self.spec)
        self.write({"automations": [{"track": "A", "param": "Volume", "points": [[0, 0]], "hold": 1}]}); self.assertEqual(gw.spec_from_file(self.spec)[2], 1)
        self.write({"automations": [{"track": "A", "points": [[0, 0], [1, 1]]}]});                self.assertRaises(ValueError, gw.spec_from_file, self.spec)   # param implicite refusé
        self.write({"automations": [{"track": "A", "param": "Volume", "points": [[0, 0], [1, 1]], "skip": True}]}); self.assertRaises(ValueError, gw.spec_from_file, self.spec)
        self.write({"automations": [{"skip": True}, {"track": "A", "param": "Volume", "points": [[0, 0], [1, 1]]}]}); self.assertEqual(gw.spec_from_file(self.spec)[2], 1)
        self.write({"automations": [{"track": "A", "param": "Volume", "points": [[0, 0], [1, 1]]}] * 33}); self.assertRaises(ValueError, gw.spec_from_file, self.spec)
    def test_spec_hash_is_canonical(self):
        _, h1, _ = gw.spec_from_file(self.spec)
        with open(self.spec, "w") as f: f.write(json.dumps(SPEC, indent=4, sort_keys=True))   # même contenu, autre mise en forme
        self.assertEqual(gw.spec_from_file(self.spec)[1], h1)
        self.write({"automations": [dict(SPEC["automations"][0], param="Pan")]}); self.assertNotEqual(gw.spec_from_file(self.spec)[1], h1)

    # --- preview ---
    def test_preview_prints_both_fingerprints_and_writes_nothing(self):
        code, mocked, res = self.run_gw(["preview", self.spec], [dry_reply()])
        self.assertEqual(code, 0); self.assertEqual(mocked.call_count, 1)
        self.assertEqual(mocked.call_args.args[1], "/apply"); self.assertIs(mocked.call_args.args[2]["dry"], True)
        self.assertEqual(res["sha256"], gw.spec_from_file(self.spec)[1]); self.assertEqual(len(res["plan_sha256"]), 64); self.assertEqual(res["log"], ["DRY …"])
    def test_preview_rejects_gap_plan_errors_and_wrong_count(self):
        for reply in (dry_reply(gap=0.5), dry_reply(errors=["aucun clip ne couvre la plage 16-32"]),
                      {"results": []}, {"error": "boom"}, {"results": [dict(dry_reply()["results"][0], dry=False)]},
                      {"results": dry_reply()["results"] * 2}):
            with patch.object(gw, "post", return_value=reply):
                with self.assertRaises(ValueError, msg=json.dumps(reply)[:80]): gw.main(["preview", self.spec], out=self.out)
    def test_bridge_level_failure_is_reported_with_code(self):
        reply = {"results": [{"index": 0, "ok": False, "errors": ["piste introuvable"], "codes": ["E_NOT_FOUND"]}]}
        with patch.object(gw, "post", return_value=reply):
            with self.assertRaises(ValueError) as cm: gw.main(["preview", self.spec], out=self.out)
        self.assertIn("E_NOT_FOUND", str(cm.exception))

    # --- commit ---
    def test_commit_revalidates_then_writes(self):
        _, _, pv = self.run_gw(["preview", self.spec], [dry_reply()]); self.out = io.StringIO()
        code, mocked, res = self.run_gw(["commit", self.spec, "--sha256", pv["sha256"], "--plan-sha256", pv["plan_sha256"]], [dry_reply(), WET_OK])
        self.assertEqual(code, 0); self.assertEqual(mocked.call_count, 2)
        self.assertIs(mocked.call_args_list[0].args[2]["dry"], True); self.assertIs(mocked.call_args_list[1].args[2]["dry"], False)
        self.assertTrue(res["verify_in_live"])
    def test_commit_refuses_changed_spec(self):
        _, _, pv = self.run_gw(["preview", self.spec], [dry_reply()])
        self.write({"automations": [dict(SPEC["automations"][0], param="Pan")]})
        with patch.object(gw, "post") as mocked:
            with self.assertRaises(ValueError): gw.main(["commit", self.spec, "--sha256", pv["sha256"], "--plan-sha256", pv["plan_sha256"]], out=io.StringIO())
        mocked.assert_not_called()
    def test_commit_refuses_when_live_state_changed(self):
        """Même spec, mais le clip a bougé (ou autre session : autres références) entre preview et commit → pas d'écriture."""
        _, _, pv = self.run_gw(["preview", self.spec], [dry_reply()])
        with patch.object(gw, "post", side_effect=[dry_reply(clip_start=8.0), WET_OK]) as mocked:
            with self.assertRaises(ValueError) as cm: gw.main(["commit", self.spec, "--sha256", pv["sha256"], "--plan-sha256", pv["plan_sha256"]], out=io.StringIO())
        self.assertEqual(mocked.call_count, 1); self.assertIn("preview", str(cm.exception))
    def test_commit_refuses_when_replan_fails(self):
        _, _, pv = self.run_gw(["preview", self.spec], [dry_reply()])
        with patch.object(gw, "post", side_effect=[dry_reply(gap=1.0), WET_OK]) as mocked:
            with self.assertRaises(ValueError): gw.main(["commit", self.spec, "--sha256", pv["sha256"], "--plan-sha256", pv["plan_sha256"]], out=io.StringIO())
        self.assertEqual(mocked.call_count, 1)
    def test_commit_reports_partial_write(self):
        _, _, pv = self.run_gw(["preview", self.spec], [dry_reply()])
        bad = {"log": ["ERR …"], "results": [{"index": 0, "ok": False, "dry": False, "errors": ["relecture : écart"], "codes": ["E_ROLLED_BACK"]}]}
        with patch.object(gw, "post", side_effect=[dry_reply(), bad]):
            with self.assertRaises(ValueError) as cm: gw.main(["commit", self.spec, "--sha256", pv["sha256"], "--plan-sha256", pv["plan_sha256"]], out=io.StringIO())
        self.assertIn("E_ROLLED_BACK", str(cm.exception)); self.assertIn("journal", str(cm.exception))

    # --- cohérence avec lom.py ---
    def test_allowlist_is_subset_of_lom_safe_http(self):
        import lom
        self.assertTrue(gw.READ_COMMANDS <= lom.SAFE_HTTP, gw.READ_COMMANDS - lom.SAFE_HTTP)
        self.assertEqual(gw.MAX_REQUEST, 262144)


if __name__ == "__main__": unittest.main()
