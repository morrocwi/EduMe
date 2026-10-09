"""Tests for the ONLINE_SYNCHRONOUS / Toledo EQ-002/H.07.v1 enforcement. Stdlib unittest only.

Run from the repo root:  python3 -I -m unittest discover -s tests -v
"""
import copy
import glob
import json
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER = os.path.join(ROOT, "mcp", "server.py")
DEMOS = os.path.join(ROOT, "demos")

sys.path.insert(0, os.path.join(ROOT, "mcp"))
import server  # noqa: E402

STAGES = ["ZoomState", "Barrier", "CandidateRoute", "LiveRoute", "HumanReturn",
          "ReturnDelta", "LiveField", "RealizedOpportunity", "NetAdvancement"]
OUTCOME = ["HumanReturn", "ReturnDelta", "RealizedOpportunity", "NetAdvancement"]


def load(name):
    with open(os.path.join(DEMOS, name), encoding="utf-8") as fh:
        return json.load(fh)


def demo5():
    return load("demo5_zoom_seed_packet.json")


def stage(spine, name):
    return next(s for s in spine["toledo_h07"]["stages"] if s["stage"] == name)


class ValidatorCase(unittest.TestCase):
    def assertInvalid(self, spine, needle=None):
        r = server.validate_design(spine)
        self.assertFalse(r["valid"], r)
        if needle:
            blob = json.dumps(r)
            self.assertIn(needle, blob)
        return r

    def test_demo5_valid_clean(self):
        r = server.validate_design(demo5())
        self.assertEqual(r, {"valid": True, "missing_required": [], "errors": [], "warnings": []})

    def test_block_missing_when_sync(self):
        s = demo5()
        del s["toledo_h07"]
        r = self.assertInvalid(s)
        self.assertIn("toledo_h07", r["missing_required"])

    def test_each_stage_missing(self):
        for name in STAGES:
            with self.subTest(stage=name):
                s = demo5()
                s["toledo_h07"]["stages"] = [x for x in s["toledo_h07"]["stages"] if x["stage"] != name]
                r = self.assertInvalid(s)
                self.assertIn(f"toledo_h07.stages[{name}]", r["missing_required"])

    def test_reordered_stages(self):
        s = demo5()
        st = s["toledo_h07"]["stages"]
        st[0], st[1] = st[1], st[0]
        self.assertInvalid(s, "canonical order")

    def test_duplicate_and_unknown_stage(self):
        s = demo5()
        s["toledo_h07"]["stages"].append(copy.deepcopy(s["toledo_h07"]["stages"][0]))
        self.assertInvalid(s, "duplicated")
        s = demo5()
        s["toledo_h07"]["stages"][1]["stage"] = "barrier"
        self.assertInvalid(s, "canonical stage names")

    def test_bad_mode_values(self):
        for bad in ["online_synchronous", "Online_Synchronous", "ONLINE-SYNCHRONOUS", "ZOOM", "", None, 5, ["ONLINE_SYNCHRONOUS"]]:
            with self.subTest(mode=bad):
                s = demo5()
                s["delivery_mode"] = bad
                self.assertInvalid(s, "delivery_mode")

    def test_wrong_case_mode_hint(self):
        s = demo5()
        s["delivery_mode"] = "online_synchronous"
        self.assertInvalid(s, "upper-case")

    def test_block_with_non_sync_mode(self):
        for mode in ["ONLINE_ASYNCHRONOUS", "FACE_TO_FACE", "BLENDED", "FIELD"]:
            with self.subTest(mode=mode):
                s = demo5()
                s["delivery_mode"] = mode
                self.assertInvalid(s, "applies only when")

    def test_block_without_mode(self):
        s = demo5()
        del s["delivery_mode"]
        self.assertInvalid(s, "applies only when")

    def test_non_sync_mode_without_block_is_fine(self):
        s = load("demo1_ticketing.json")
        s["delivery_mode"] = "FACE_TO_FACE"
        self.assertTrue(server.validate_design(s)["valid"])

    def test_malformed_block_never_raises(self):
        for bad in ["a string", None, [], [1, 2], 7, True, {"stages": "x"}, {"stages": None},
                    {"stages": [None, "x", 3, []]}, {"stages": {}}, {}]:
            with self.subTest(block=bad):
                s = demo5()
                s["toledo_h07"] = bad
                r = server.validate_design(s)
                self.assertFalse(r["valid"], r)
                server.render_design_document(s)  # must not raise either

    def test_malformed_fields_inside_stages(self):
        s = demo5()
        stage(s, "HumanReturn")["evidence_basis"] = "delayed_unaided_task"
        self.assertInvalid(s, "array of strings")
        s = demo5()
        stage(s, "LiveRoute")["endorser"] = ["human_learner"]
        self.assertInvalid(s, "endorser")

    def test_trace_only_evidence_rejected(self):
        for name in OUTCOME:
            for trace in ["camera_on", "attendance", "session_duration", "chat_volume", "poll_response"]:
                with self.subTest(stage=name, trace=trace):
                    s = demo5()
                    stage(s, name)["evidence_basis"] = [trace]
                    r = self.assertInvalid(s, "forbidden inference")
                    self.assertIn(name, json.dumps(r))

    def test_trace_only_rejected_for_other_stages(self):
        for name in ["CandidateRoute", "LiveRoute", "LiveField"]:
            for trace in ["camera_on", "attendance", "session_duration", "chat_volume", "poll_response"]:
                with self.subTest(stage=name, trace=trace):
                    s = demo5()
                    stage(s, name)["evidence_basis"] = [trace]
                    self.assertInvalid(s, "allowed only for ZoomState and Barrier")

    def test_trace_text_only_rejected_for_other_stages(self):
        for name in ["CandidateRoute", "LiveRoute", "LiveField"]:
            with self.subTest(stage=name):
                s = demo5()
                st = stage(s, name)
                st["evidence_basis"] = []
                st["evidence_plan"] = "Use attendance and chat volume as the evidence."
                self.assertInvalid(s, "forbidden inference")

    def test_other_stages_without_basis_or_with_genuine_ok(self):
        for name in ["CandidateRoute", "LiveRoute", "LiveField"]:
            with self.subTest(stage=name):
                s = demo5()
                st = stage(s, name)
                st.pop("evidence_basis", None)
                st["evidence_plan"] = "A conversation."
                self.assertTrue(server.validate_design(s)["valid"])
                st["evidence_basis"] = ["attendance", "learner_reflection_record"]
                self.assertTrue(server.validate_design(s)["valid"])

    def test_all_traces_together_still_rejected(self):
        s = demo5()
        stage(s, "RealizedOpportunity")["evidence_basis"] = ["camera_on", "attendance", "chat_volume", "poll_response"]
        self.assertInvalid(s, "forbidden inference")

    def test_trace_text_only_rejected(self):
        s = demo5()
        st = stage(s, "NetAdvancement")
        st["evidence_basis"] = []
        st["evidence_plan"] = "Count how many kept the camera on and their attendance."
        self.assertInvalid(s, "forbidden inference")

    def test_trace_text_with_non_performance_basis_rejected(self):
        for name in OUTCOME:
            with self.subTest(stage=name):
                s = demo5()
                st = stage(s, name)
                st["evidence_basis"] = ["other_documented_evidence"]
                st["evidence_plan"] = "Camera on for the whole session and attendance logged."
                self.assertInvalid(s, "performance-type")

    def test_trace_text_with_performance_basis_ok(self):
        s = demo5()
        st = stage(s, "ReturnDelta")
        st["evidence_basis"] = ["work_product_review"]
        st["evidence_plan"] = "Review the work product; attendance is only noted for context."
        self.assertTrue(server.validate_design(s)["valid"])

    def test_trace_text_with_reflection_only_rejected_any_non_trace_stage(self):
        for name in ["CandidateRoute", "LiveRoute", "LiveField"]:
            with self.subTest(stage=name):
                s = demo5()
                st = stage(s, name)
                st["evidence_basis"] = ["learner_reflection_record"]
                st["evidence_plan"] = "We count attendance"
                self.assertInvalid(s, "forbidden inference")
        s = demo5()
        st = stage(s, "LiveField")
        st["evidence_basis"] = ["human_observation"]
        st["evidence_plan"] = "We count attendance and observe"
        self.assertTrue(server.validate_design(s)["valid"])

    def test_outcome_stages_need_performance_kind(self):
        for name in OUTCOME:
            for basis in (["learner_reflection_record"], ["other_documented_evidence"],
                          ["learner_reflection_record", "other_documented_evidence"], ["attendance", "learner_reflection_record"]):
                with self.subTest(stage=name, basis=basis):
                    s = demo5()
                    stage(s, name)["evidence_basis"] = basis
                    self.assertInvalid(s, "performance-type")
            for kind in ["unaided_task_performance", "delayed_unaided_task", "work_product_review", "human_observation"]:
                with self.subTest(stage=name, kind=kind):
                    s = demo5()
                    stage(s, name)["evidence_basis"] = [kind]
                    self.assertTrue(server.validate_design(s)["valid"])

    def test_human_return_needs_performance_kind(self):
        for basis in (["learner_reflection_record"], ["other_documented_evidence"],
                      ["learner_reflection_record", "other_documented_evidence"]):
            with self.subTest(basis=basis):
                s = demo5()
                stage(s, "HumanReturn")["evidence_basis"] = basis
                self.assertInvalid(s, "performance-type")

    def test_prose_number_warns_not_errors(self):
        for text in ["Expect 80% of learners to improve.", "About 12 percent will return.", "Expect 3 of 4 learners to succeed.", "The probability of success is high."]:
            with self.subTest(text=text):
                s = demo5()
                stage(s, "NetAdvancement")["design"] = text
                r = server.validate_design(s)
                self.assertTrue(r["valid"], r)
                self.assertEqual(len(r["warnings"]), 1, r)
                self.assertIn("percentage or outcome-number", r["warnings"][0])
        s = demo5()
        stage(s, "Barrier")["evidence_plan"] = "Poll for 5 minutes."
        self.assertEqual(server.validate_design(s)["warnings"], [])

    def test_map_names_verbatim(self):
        with open(os.path.join(DEMOS, "demo5_zoom_seed_packet.rendered.md"), encoding="utf-8") as fh:
            r = fh.read()
        self.assertIn("--u*_{diag}-->", r)
        self.assertIn("--pi*_{scaffold}-->", r)

    def test_outcome_stage_without_evidence_basis(self):
        s = demo5()
        st = stage(s, "ReturnDelta")
        del st["evidence_basis"]
        st["evidence_plan"] = "A conversation."
        r = self.assertInvalid(s)
        self.assertIn("toledo_h07.stages[ReturnDelta].evidence_basis", r["missing_required"])

    def test_traces_allowed_for_zoomstate_and_barrier(self):
        s = demo5()
        stage(s, "ZoomState")["evidence_basis"] = ["camera_on", "attendance", "session_duration"]
        stage(s, "Barrier")["evidence_basis"] = ["chat_volume", "poll_response"]
        self.assertTrue(server.validate_design(s)["valid"])

    def test_trace_plus_genuine_is_allowed(self):
        s = demo5()
        stage(s, "HumanReturn")["evidence_basis"] = ["attendance", "delayed_unaided_task"]
        self.assertTrue(server.validate_design(s)["valid"])

    def test_unknown_evidence_basis_rejected(self):
        s = demo5()
        stage(s, "HumanReturn")["evidence_basis"] = ["vibes"]
        self.assertInvalid(s, "unrecognised")

    def test_ai_endorser_rejected(self):
        for who in ["ai", "AI", "system", "LLM", "the platform", "automated recommender", "AI assistant", "ai_system"]:
            with self.subTest(who=who):
                s = demo5()
                stage(s, "LiveRoute")["endorser"] = who
                self.assertInvalid(s, "AI suggestion is not a human choice")

    def test_endorser_missing_or_unknown(self):
        s = demo5()
        del stage(s, "LiveRoute")["endorser"]
        r = self.assertInvalid(s)
        self.assertIn("toledo_h07.stages[LiveRoute].endorser", r["missing_required"])
        s = demo5()
        stage(s, "LiveRoute")["endorser"] = "Sam"
        self.assertInvalid(s, "not recognised")

    def test_assisted_human_return_rejected(self):
        s = demo5()
        stage(s, "HumanReturn")["assistance_condition"] = "assisted"
        self.assertInvalid(s, "not unaided Human Return")

    def test_assisted_assessment_conflicts(self):
        s = demo5()
        s["assessment"]["assistance_condition"] = "assisted - the instructor helped"
        self.assertInvalid(s, "not unaided Human Return")

    def test_assistance_missing_or_unknown(self):
        s = demo5()
        del stage(s, "HumanReturn")["assistance_condition"]
        r = self.assertInvalid(s)
        self.assertIn("toledo_h07.stages[HumanReturn].assistance_condition", r["missing_required"])
        s = demo5()
        stage(s, "HumanReturn")["assistance_condition"] = "Unassisted"
        self.assertInvalid(s, "not recognised")

    def test_no_numeric_fields(self):
        s = demo5()
        stage(s, "NetAdvancement")["score"] = 0.8
        self.assertInvalid(s, "not allowed")
        s = demo5()
        stage(s, "HumanReturn")["design"] = 5
        r = self.assertInvalid(s)
        self.assertIn("numeric", json.dumps(r))
        s = demo5()
        s["toledo_h07"]["human_potential"] = "high"
        self.assertInvalid(s, "potential")
        s = demo5()
        stage(s, "ReturnDelta")["probability"] = "likely"
        self.assertInvalid(s, "not allowed")

    def test_unknown_stage_key_rejected(self):
        s = demo5()
        stage(s, "Barrier")["notes"] = "x"
        self.assertInvalid(s, "unknown key")

    def test_stage_design_missing(self):
        s = demo5()
        stage(s, "LiveField")["design"] = ""
        r = self.assertInvalid(s)
        self.assertIn("toledo_h07.stages[LiveField].design", r["missing_required"])

    def test_top_level_required_unchanged(self):
        schema = server.load_schema()
        self.assertEqual(schema["required"], ["course", "live_problem", "learner", "framing", "routes",
                                              "capability", "content", "sessions", "assessment", "support"])
        self.assertIn("delivery_mode", schema["properties"])
        self.assertIn("toledo_h07", schema["properties"])


class BackwardCompat(unittest.TestCase):
    def test_demos_1_to_4(self):
        files = sorted(glob.glob(os.path.join(DEMOS, "demo[1-4]_*.json")))
        self.assertEqual(len(files), 4)
        for f in files:
            with self.subTest(demo=os.path.basename(f)):
                with open(f, encoding="utf-8") as fh:
                    spine = json.load(fh)
                r = server.validate_design(spine)
                self.assertTrue(r["valid"])
                self.assertEqual(r["warnings"], [])
                self.assertEqual(r["errors"], [])
                with open(f[:-5] + ".rendered.md", encoding="utf-8") as fh:
                    committed = fh.read()
                cli = subprocess.run([sys.executable, "-I", SERVER, "render", f], capture_output=True, text=True, check=True).stdout
                self.assertEqual(cli.encode(), committed.encode())
                self.assertNotIn("Toledo EQ-002/H.07", cli)


class Demo5(unittest.TestCase):
    def test_render_matches_committed(self):
        f = os.path.join(DEMOS, "demo5_zoom_seed_packet.json")
        fresh = subprocess.run([sys.executable, "-I", SERVER, "render", f], capture_output=True, text=True, check=True).stdout
        with open(f[:-5] + ".rendered.md", encoding="utf-8") as fh:
            self.assertEqual(fh.read(), fresh)
        self.assertEqual(fresh.count("[NOT YET SPECIFIED"), 0)
        self.assertEqual(fresh.count("{{"), 0)
        self.assertIn("Toledo EQ-002/H.07.v1 (CAN-1318) — Definition (composition), not a proved or validated causal law", fresh)
        for c in ["NOT_YET_DIRECTLY_VALIDATED", "raw_row_independent_replication: not_yet_completed", "universal_causal_validation: false"]:
            self.assertIn(c, fresh)
        pos = [fresh.index(f"| {n} |") for n in STAGES]
        self.assertEqual(pos, sorted(pos))

    def test_no_numeric_values_in_block(self):
        def walk(n):
            self.assertFalse(isinstance(n, (int, float)))
            if isinstance(n, dict):
                [walk(v) for v in n.values()]
            elif isinstance(n, list):
                [walk(v) for v in n]
        walk(demo5()["toledo_h07"])


def rpc(*reqs):
    inp = "\n".join(json.dumps(r) for r in reqs) + "\n"
    out = subprocess.run([sys.executable, "-I", SERVER], input=inp, capture_output=True, text=True, check=True).stdout
    return [json.loads(l) for l in out.splitlines() if l.strip()]


class McpAndCli(unittest.TestCase):
    def test_initialize_and_tools(self):
        out = rpc({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
                  {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        self.assertEqual(out[0]["result"]["serverInfo"]["name"], "edume-upcc-mcp")
        names = [t["name"] for t in out[1]["result"]["tools"]]
        self.assertEqual(names, ["get_spine_schema", "get_document_template", "validate_design", "render_design_document"])

    def test_tools_call_validate_demo5(self):
        out = rpc({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                   "params": {"name": "validate_design", "arguments": {"spine": demo5()}}})
        res = json.loads(out[0]["result"]["content"][0]["text"])
        self.assertTrue(res["valid"])
        self.assertEqual(res["warnings"], [])

    def test_tools_call_malformed_blocks(self):
        reqs = []
        for i, bad in enumerate(["str", None, [], [1], {"stages": "x"}, 3]):
            s = demo5()
            s["toledo_h07"] = bad
            reqs.append({"jsonrpc": "2.0", "id": i, "method": "tools/call",
                         "params": {"name": "validate_design", "arguments": {"spine": s}}})
        for o in rpc(*reqs):
            self.assertNotIn("error", o)
            self.assertFalse(json.loads(o["result"]["content"][0]["text"])["valid"])

    def test_tools_call_render_demo5(self):
        out = rpc({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                   "params": {"name": "render_design_document", "arguments": {"spine": demo5()}}})
        self.assertIn("## 11. Synchronous Videoconference Delivery", out[0]["result"]["content"][0]["text"])

    def test_cli_validate_malformed_block(self):
        import tempfile
        s = demo5()
        s["toledo_h07"] = "oops"
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.json")
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(s, fh)
            r = subprocess.run([sys.executable, "-I", SERVER, "validate", p], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(json.loads(r.stdout)["valid"])


if __name__ == "__main__":
    unittest.main()
