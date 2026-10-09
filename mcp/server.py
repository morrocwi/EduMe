#!/usr/bin/env python3
"""
EduMe/UPCC MCP server — stdlib-only, stdio JSON-RPC (MCP protocol) *and* a plain CLI.

Two ways to run it, so it works whether or not the caller has an MCP client:

    python3 server.py                       # stdio MCP server (for an MCP host)
    python3 server.py validate design.json  # CLI: print validation result {valid, missing_required, errors, warnings}
    python3 server.py render design.json    # CLI: print rendered document
    python3 server.py schema                # CLI: print the spine JSON Schema
    python3 server.py template              # CLI: print the document template

No third-party packages, no network access, no filesystem writes at runtime (schema and template
are loaded once from the two sibling files below; everything else is pure computation on the
caller-supplied `spine` object).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE.parent / "schema" / "upcc_curriculum_spine.schema.json"
TEMPLATE_PATH = HERE.parent / "templates" / "DESIGN_CURRICULUM_DOCUMENT_TEMPLATE.md"
PROTOCOL = "2025-06-18"
TOOLS = ["get_spine_schema", "get_document_template", "validate_design", "render_design_document"]


# ---------------------------------------------------------------------------
# ONLINE_SYNCHRONOUS / Toledo EQ-002/H.07.v1 (CAN-1318) enforcement
#
# EQ-002/H.07.v1 is registered in Toledo at tier "Definition": a composition of maps, not a
# proved or validated causal law. This module only checks that a design DESCRIBES the nine
# states in canonical order and does not rest outcome claims on forbidden inferences.
#
# HEURISTIC: the forbidden-inference, endorser and numeric checks below are keyword/enum
# matching on what the designer wrote. They catch the listed patterns; they cannot prove that
# a design is sound, and a determined author can phrase around them. A pass is "no listed
# pattern found", never "evidence is adequate".
# ---------------------------------------------------------------------------

SYNC_MODE = "ONLINE_SYNCHRONOUS"
DELIVERY_MODES = [SYNC_MODE, "ONLINE_ASYNCHRONOUS", "FACE_TO_FACE", "BLENDED", "FIELD"]
H07_STAGES = ["ZoomState", "Barrier", "CandidateRoute", "LiveRoute", "HumanReturn",
              "ReturnDelta", "LiveField", "RealizedOpportunity", "NetAdvancement"]
# stages with the stricter outcome rule (performance-type evidence); platform traces are rejected for every stage except ZoomState and Barrier
H07_TRACE_OK_STAGES = ("ZoomState", "Barrier")
H07_OUTCOME_STAGES = ["HumanReturn", "ReturnDelta", "RealizedOpportunity", "NetAdvancement"]
TRACE_BASIS = {"camera_on", "attendance", "session_duration", "chat_volume", "poll_response"}
GENUINE_BASIS = {"unaided_task_performance", "delayed_unaided_task", "work_product_review",
                 "human_observation", "learner_reflection_record", "other_documented_evidence"}
HUMAN_ENDORSERS = {"human_learner", "human_instructor", "human_peer", "human_other"}
ASSISTANCE_VALUES = {"unassisted", "assisted"}
H07_STAGE_KEYS = {"stage", "design", "evidence_basis", "evidence_plan", "endorser", "assistance_condition"}
TRACE_TEXT_RE = re.compile(
    r"camera[\s_-]*on|video[\s_-]*on|attendance|attended|duration|time[\s_-]*in[\s_-]*(?:session|meeting)|"
    r"chat[\s_-]*(?:volume|count|messages)|poll[\s_-]*(?:response|answers?)|clicked", re.I)
AI_ENDORSER_TOKENS = {"ai", "llm", "bot", "chatbot", "system", "algorithm", "algorithms", "model", "platform",
                      "assistant", "agent", "auto", "gpt", "copilot", "recommender"}


def _is_ai_endorser(text: str) -> bool:
    toks = [x for x in re.split(r"[^a-z0-9]+", text.lower()) if x]
    return any(x in AI_ENDORSER_TOKENS or x.startswith("automat") for x in toks)


NUMERIC_KEY_RE = re.compile(r"score|probab|potential|likelihood|predict|percent|rating|metric|forecast", re.I)
PERFORMANCE_BASIS = {"unaided_task_performance", "delayed_unaided_task", "work_product_review", "human_observation"}
PROSE_NUMBER_RE = re.compile(r"\d+(?:\.\d+)?\s*(?:%|percent\b|per\s*cent\b)|\b(?:probabilit\w*|likelihood|odds)\s+(?:of|that)\b|\bexpect(?:ed|s)?\s+(?:\w+\s+){0,3}\d", re.I)
FORBIDDEN_INFERENCE = ("forbidden inference: camera-on, attendance/duration, chat volume and poll response are platform "
                       "traces, not evidence of unaided Human Return or its downstream states")

NOT_SPECIFIED = "[NOT YET SPECIFIED]"
NOT_SPECIFIED_ARRAY = "[NOT YET SPECIFIED — no entries provided]"


def load_schema() -> dict:
    with open(SCHEMA_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def load_template() -> str:
    with open(TEMPLATE_PATH, encoding="utf-8") as fh:
        return fh.read()


def is_empty(v) -> bool:
    """Empty per this validator's rule: "", null, [], {} are missing. 0 and False are NOT missing."""
    if v is None:
        return True
    if isinstance(v, (str, list, dict)) and len(v) == 0:
        return True
    return False


def walk_missing(schema: dict, spine, prefix: str = "") -> list:
    """Walk the schema's own `required` arrays against `spine`; return list of missing dotted/indexed paths."""
    missing = []
    if not isinstance(spine, dict):
        # whole subtree is malformed/absent -> every field this schema requires is missing
        for req in schema.get("required", []):
            missing.append(f"{prefix}{req}" if not prefix else f"{prefix}.{req}")
        return missing

    props = schema.get("properties", {})
    for req in schema.get("required", []):
        path = f"{prefix}.{req}" if prefix else req
        val = spine.get(req)
        sub_schema = props.get(req, {})
        sub_type = sub_schema.get("type")

        if sub_type == "array":
            if not isinstance(val, list) or len(val) == 0:
                missing.append(path)
                continue
            item_schema = sub_schema.get("items", {})
            if item_schema.get("type") == "object":
                for i, item in enumerate(val):
                    missing.extend(walk_missing(item_schema, item, f"{path}[{i}]"))
            # array of primitives: presence + non-empty already checked above
        elif sub_type == "object":
            missing.extend(walk_missing(sub_schema, val if isinstance(val, dict) else {}, path))
        else:
            if is_empty(val):
                missing.append(path)
    return missing


def get_by_path(spine: dict, path: str):
    """Dotted/indexed path -> value, or None if any hop is missing/malformed. No exceptions raised."""
    cur = spine
    for part in path.replace("]", "").split("."):
        if "[" in part:
            key, idx = part.split("[")
            idx = int(idx)
            if not isinstance(cur, dict) or key not in cur:
                return None
            cur = cur[key]
            if not isinstance(cur, list) or idx >= len(cur):
                return None
            cur = cur[idx]
        else:
            if not isinstance(cur, dict) or part not in cur:
                return None
            cur = cur[part]
    return cur


def fmt_value(v) -> str:
    if v is None:
        return ""
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return str(v)



def _scan_numeric(node, path, errors):
    """The H.07 block describes designs; it carries no numbers, probabilities, scores or predicted outcomes."""
    if isinstance(node, bool) or isinstance(node, (int, float)):
        errors.append(f"{path}: numeric/boolean values are not allowed in toledo_h07 (design descriptions only; no predicted learner-outcome numbers)")
    elif isinstance(node, dict):
        for k, v in node.items():
            if NUMERIC_KEY_RE.search(str(k)):
                errors.append(f"{path}.{k}: numeric/probability/score/potential-style fields are not allowed in toledo_h07")
            _scan_numeric(v, f"{path}.{k}", errors)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _scan_numeric(v, f"{path}[{i}]", errors)


def check_h07(spine: dict):
    """Return (missing, errors) for delivery_mode / toledo_h07. Never raises on malformed input."""
    missing, errors = [], []
    has_mode = "delivery_mode" in spine
    mode = spine.get("delivery_mode")
    has_block = "toledo_h07" in spine
    block = spine.get("toledo_h07")

    mode_ok = True
    if has_mode:
        if not isinstance(mode, str) or mode not in DELIVERY_MODES:
            mode_ok = False
            hint = ""
            if isinstance(mode, str) and mode.upper() in DELIVERY_MODES:
                hint = f" (modes are exact and upper-case; did you mean {mode.upper()!r}?)"
            errors.append(f"delivery_mode {mode!r} is not recognised; allowed values: {DELIVERY_MODES}{hint}")
    is_sync = mode_ok and mode == SYNC_MODE

    if has_block and not is_sync:
        if mode_ok:
            errors.append(f"toledo_h07 is present but delivery_mode is {mode!r}; the H.07 block applies only when delivery_mode is {SYNC_MODE!r}")
        else:
            errors.append(f"toledo_h07 is present but delivery_mode is missing or invalid; the H.07 block applies only when delivery_mode is {SYNC_MODE!r}")
        return missing, errors
    if not is_sync:
        return missing, errors

    # ---- synchronous: block is mandatory ----
    if not has_block or is_empty(block):
        missing.append("toledo_h07")
        return missing, errors
    if not isinstance(block, dict):
        errors.append(f"toledo_h07 must be an object with a 'stages' array; received: {type(block).__name__}")
        return missing, errors
    for k in block:
        if k != "stages":
            errors.append(f"toledo_h07.{k}: unknown key (only 'stages' is allowed)")
    _scan_numeric(block, "toledo_h07", errors)
    stages = block.get("stages")
    if not isinstance(stages, list):
        errors.append(f"toledo_h07.stages must be an array of the 9 canonical stages; received: {type(stages).__name__}")
        return missing, errors

    seen = []
    by_name = {}
    for i, st in enumerate(stages):
        where = f"toledo_h07.stages[{i}]"
        if not isinstance(st, dict):
            errors.append(f"{where} must be an object; received: {type(st).__name__}")
            continue
        name = st.get("stage")
        if not isinstance(name, str) or name not in H07_STAGES:
            errors.append(f"{where}.stage {name!r} is not one of the canonical stage names {H07_STAGES} (exact spelling and case)")
            continue
        if name in by_name:
            errors.append(f"{where}.stage {name!r} is duplicated")
            continue
        by_name[name] = st
        seen.append(name)
        for k in st:
            if k not in H07_STAGE_KEYS:
                if NUMERIC_KEY_RE.search(str(k)):
                    pass  # already reported by _scan_numeric
                else:
                    errors.append(f"{where}.{k}: unknown key")
        if is_empty(st.get("design")) or not isinstance(st.get("design"), str):
            missing.append(f"toledo_h07.stages[{name}].design")

    for name in H07_STAGES:
        if name not in by_name:
            missing.append(f"toledo_h07.stages[{name}]")
    if seen != [n for n in H07_STAGES if n in by_name]:
        errors.append(f"toledo_h07.stages are out of canonical order; required order: {' -> '.join(H07_STAGES)}")

    live = by_name.get("LiveRoute")
    if live is not None:
        end = live.get("endorser")
        if is_empty(end):
            missing.append("toledo_h07.stages[LiveRoute].endorser")
        elif not isinstance(end, str):
            errors.append("LiveRoute.endorser must be a string naming a human endorser")
        elif end in HUMAN_ENDORSERS:
            pass
        elif _is_ai_endorser(end):
            errors.append(f"LiveRoute.endorser {end!r} is an AI/system: an AI suggestion is not a human choice; the live route must be endorsed by a human ({sorted(HUMAN_ENDORSERS)})")
        else:
            errors.append(f"LiveRoute.endorser {end!r} is not recognised; allowed: {sorted(HUMAN_ENDORSERS)}")

    ret = by_name.get("HumanReturn")
    if ret is not None:
        cond = ret.get("assistance_condition")
        if is_empty(cond):
            missing.append("toledo_h07.stages[HumanReturn].assistance_condition")
        elif cond != "unassisted":
            if cond == "assisted":
                errors.append("HumanReturn evidence under an 'assisted' condition is not allowed: assisted performance is not unaided Human Return (consistent with assessment.assistance_condition)")
            else:
                errors.append(f"HumanReturn.assistance_condition {cond!r} is not recognised; allowed: {sorted(ASSISTANCE_VALUES)} (must be 'unassisted')")
        assess = spine.get("assessment")
        ac = assess.get("assistance_condition") if isinstance(assess, dict) else None
        if isinstance(ac, str) and re.match(r"\s*assisted\b", ac, re.I):
            errors.append("assessment.assistance_condition is 'assisted' while the design declares a HumanReturn stage: assisted performance is not unaided Human Return")

    # Platform traces are allowed only for ZoomState and Barrier; every other stage is checked.
    for name in H07_STAGES:
        if name in H07_TRACE_OK_STAGES:
            continue
        outcome = name in H07_OUTCOME_STAGES
        st = by_name.get(name)
        if st is None:
            continue
        basis = st.get("evidence_basis")
        plan = st.get("evidence_plan")
        if basis is not None and not (isinstance(basis, list) and all(isinstance(b, str) for b in basis)):
            errors.append(f"{name}.evidence_basis must be an array of strings")
            continue
        basis = basis or []
        unknown = [b for b in basis if b not in TRACE_BASIS and b not in GENUINE_BASIS]
        if unknown:
            errors.append(f"{name}.evidence_basis has unrecognised values {unknown}; allowed: {sorted(TRACE_BASIS | GENUINE_BASIS)}")
            continue
        has_perf = any(b in PERFORMANCE_BASIS for b in basis)
        text_trace = isinstance(plan, str) and bool(TRACE_TEXT_RE.search(plan))
        if not basis and not text_trace:
            if outcome:
                missing.append(f"toledo_h07.stages[{name}].evidence_basis")
        elif not any(b in GENUINE_BASIS for b in basis):
            errors.append(f"{name} evidence rests only on platform traces (camera-on, attendance/duration, chat volume or poll response); platform traces are allowed only for ZoomState and Barrier; {FORBIDDEN_INFERENCE}")
        elif text_trace and not has_perf:
            errors.append(f"{name} evidence_plan describes platform traces (camera-on, attendance/duration, chat volume or poll response) and evidence_basis has no performance-type kind {sorted(PERFORMANCE_BASIS)}; platform traces are allowed only for ZoomState and Barrier; {FORBIDDEN_INFERENCE}")
        elif outcome and not has_perf:
            errors.append(f"{name}.evidence_basis needs at least one performance-type kind {sorted(PERFORMANCE_BASIS)}; reflection or other documented evidence alone does not show it")
    return missing, errors


def h07_prose_warnings(spine: dict) -> list:
    """HEURISTIC: warn when design/plan prose in the block states a percentage or an expected-outcome number."""
    warnings = []
    block = spine.get("toledo_h07")
    stages = block.get("stages") if isinstance(block, dict) else None
    if not isinstance(stages, list):
        return warnings
    for i, st in enumerate(stages):
        if not isinstance(st, dict):
            continue
        for field in ("design", "evidence_plan"):
            v = st.get(field)
            if isinstance(v, str) and PROSE_NUMBER_RE.search(v):
                warnings.append(f"toledo_h07.stages[{i}].{field} contains a percentage or outcome-number pattern; the H.07 block describes designs and must not predict learner-outcome numbers")
    return warnings


def validate_design(spine, schema=None) -> dict:
    schema = schema or load_schema()
    if not isinstance(spine, dict):
        return {"valid": False, "missing_required": ["<root>"], "errors": [], "warnings": [f"spine is required and must be a JSON object; received: {type(spine).__name__}"]}
    missing = walk_missing(schema, spine)
    h07_missing, errors = check_h07(spine)
    missing = missing + h07_missing
    warnings = h07_prose_warnings(spine)
    # Note: framing.working_words[i].term is already covered by walk_missing's recursion into
    # the schema's own items.required=["term"] — do not re-check it here, or it double-reports
    # (caught by real testing on demo4_prenatal_v0.json, 2026-09-20).
    sessions = spine.get("sessions")
    if isinstance(sessions, list):
        for i, s in enumerate(sessions):
            if isinstance(s, dict) and "minutes" in s and not isinstance(s.get("minutes"), int):
                warnings.append(f"sessions[{i}].minutes is not an integer")
    course = spine.get("course") if isinstance(spine.get("course"), dict) else {}
    if course.get("claim") and course.get("non_claims") and course["claim"] == course["non_claims"]:
        warnings.append("course.claim and course.non_claims are identical text — not meaningfully distinct")
    return {"valid": len(missing) == 0 and len(errors) == 0, "missing_required": missing, "errors": errors, "warnings": warnings}


def render_row(template_block: str, item: dict, missing_prefix_paths: set) -> str:
    out = template_block
    import re
    for m in re.findall(r"\{\{this\.([a-zA-Z_0-9]+)\}\}", template_block):
        val = item.get(m) if isinstance(item, dict) else None
        out = out.replace("{{this." + m + "}}", NOT_SPECIFIED if is_empty(val) else fmt_value(val))
    return out


def get_item_required(schema: dict, path: str) -> set:
    """Dotted path to an array field -> the set of its item schema's required field names.
    Optional item fields must never be marked NOT_SPECIFIED when absent (only required ones)."""
    node = schema
    for part in path.split("."):
        props = node.get("properties", {})
        node = props.get(part, {})
    return set(node.get("items", {}).get("required", []))


def render_design_document(spine, schema=None, template=None) -> str:
    import re
    schema = schema or load_schema()
    template = template if template is not None else load_template()
    missing = set(walk_missing(schema, spine if isinstance(spine, dict) else {}))
    spine = spine if isinstance(spine, dict) else {}

    # Strip the template's own leading HTML documentation comment before substitution — its
    # literal "{{path}}" example text would otherwise be matched by the placeholder regex below
    # (caught by real testing: it rendered as "[NOT YET SPECIFIED]" in every demo, 2026-09-20).
    out = re.sub(r"^<!--.*?-->\n*", "", template, count=1, flags=re.S)

    # conditional blocks: {{#if path}} ... {{/if}} (kept only when path is non-empty; the single
    # newline after {{/if}} is consumed so an absent block leaves the output byte-identical to
    # a template without it). Not nested.
    def expand_if(match):
        return match.group(2) if not is_empty(get_by_path(spine, match.group(1))) else ""

    out = re.sub(r"\{\{#if ([a-zA-Z_.0-9]+)\}\}(.*?)\{\{/if\}\}\n?", lambda m: expand_if(m), out, flags=re.S)

    # repeatable blocks: {{#each path}} ... {{/each}}
    def expand_each(match):
        path = match.group(1)
        block = match.group(2)
        arr = get_by_path(spine, path)
        required_fields = get_item_required(schema, path)
        if not isinstance(arr, list) or len(arr) == 0:
            return NOT_SPECIFIED_ARRAY
        rendered_rows = []
        for item in arr:
            row = block
            for field_match in re.findall(r"\{\{this\.([a-zA-Z_0-9]+)\}\}", block):
                val = item.get(field_match) if isinstance(item, dict) else None
                if is_empty(val):
                    # Optional-and-absent is not a gap: only mark NOT_SPECIFIED for fields this
                    # item's own schema actually requires (caught by real testing on demo3's
                    # optional changed_questions field, 2026-09-20).
                    replacement = NOT_SPECIFIED if field_match in required_fields else ""
                else:
                    replacement = fmt_value(val)
                row = row.replace("{{this." + field_match + "}}", replacement)
            rendered_rows.append(row)
        return "".join(rendered_rows)

    out = re.sub(r"\{\{#each ([a-zA-Z_.0-9]+)\}\}(.*?)\{\{/each\}\}", expand_each, out, flags=re.S)

    # scalar placeholders: {{a.b.c}}
    def expand_scalar(match):
        path = match.group(1)
        if path in missing:
            return NOT_SPECIFIED
        val = get_by_path(spine, path)
        return NOT_SPECIFIED if is_empty(val) else fmt_value(val)

    out = re.sub(r"\{\{([a-zA-Z_.0-9]+)\}\}", expand_scalar, out)
    return out


# ---------------------------------------------------------------------------
# MCP stdio JSON-RPC transport
# ---------------------------------------------------------------------------

def _text_result(text: str) -> dict:
    return {"content": [{"type": "text", "text": text}]}


def _error_result(message: str) -> dict:
    return {"content": [{"type": "text", "text": message}], "isError": True}


def handle_tool_call(name: str, args: dict) -> dict:
    if name == "get_spine_schema":
        if args:
            return _error_result("this tool takes no input; call with {}")
        return _text_result(json.dumps(load_schema(), ensure_ascii=False, indent=2))
    if name == "get_document_template":
        if args:
            return _error_result("this tool takes no input; call with {}")
        return _text_result(load_template())
    if name == "validate_design":
        spine = args.get("spine") if isinstance(args, dict) else None
        if spine is None:
            return _error_result(f"spine is required and must be a JSON object; received: {type(spine).__name__}")
        return _text_result(json.dumps(validate_design(spine), ensure_ascii=False, indent=2))
    if name == "render_design_document":
        spine = args.get("spine") if isinstance(args, dict) else None
        if spine is None:
            return _error_result(f"spine is required and must be a JSON object; received: {type(spine).__name__}")
        return _text_result(render_design_document(spine))
    return _error_result(f"unknown tool {name!r}; call tools/list — valid tools: {TOOLS}")


def tool_schemas() -> list:
    empty_input = {"type": "object", "properties": {}, "additionalProperties": False}
    spine_input = {"type": "object", "required": ["spine"], "properties": {"spine": {"type": "object"}}, "additionalProperties": False}
    return [
        {"name": "get_spine_schema", "description": "Returns the UPCC v2.0 spine JSON Schema (17-field minimal legitimate design) as a JSON string.", "inputSchema": empty_input},
        {"name": "get_document_template", "description": "Returns the Design Curriculum Document markdown template as a string.", "inputSchema": empty_input},
        {"name": "validate_design", "description": "Validates a filled UPCC spine object; returns {valid, missing_required, errors, warnings}; enforces the ONLINE_SYNCHRONOUS / Toledo EQ-002/H.07.v1 block (heuristic forbidden-inference checks).", "inputSchema": spine_input},
        {"name": "render_design_document", "description": "Renders a filled UPCC spine object into the Design Curriculum Document markdown.", "inputSchema": spine_input},
    ]


def dispatch(req: dict) -> dict | None:
    rid = req.get("id")
    method = req.get("method")
    try:
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": rid, "result": {"protocolVersion": PROTOCOL, "serverInfo": {"name": "edume-upcc-mcp", "version": "1.0.0"}, "capabilities": {"tools": {}}}}
        if method == "notifications/initialized":
            return None
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": rid, "result": {"tools": tool_schemas()}}
        if method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {}) or {}
            if name not in TOOLS:
                return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"unknown tool {name!r}; call tools/list — valid tools: {TOOLS}"}}
            return {"jsonrpc": "2.0", "id": rid, "result": handle_tool_call(name, args)}
        return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": f"unknown method {method!r}"}}
    except Exception as e:  # noqa: BLE001 — fail closed, never kill the stdio loop
        return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32000, "message": f"internal error: {e}"}}


def serve_stdio():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}), flush=True)
            continue
        resp = dispatch(req)
        if resp is not None:
            print(json.dumps(resp), flush=True)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) == 1:
        serve_stdio()
        return
    cmd = sys.argv[1]
    if cmd == "schema":
        print(json.dumps(load_schema(), ensure_ascii=False, indent=2))
    elif cmd == "template":
        print(load_template())
    elif cmd in ("validate", "render"):
        if len(sys.argv) < 3:
            print(f"usage: server.py {cmd} <design.json>", file=sys.stderr)
            sys.exit(2)
        with open(sys.argv[2], encoding="utf-8") as fh:
            spine = json.load(fh)
        if cmd == "validate":
            print(json.dumps(validate_design(spine), ensure_ascii=False, indent=2))
        else:
            print(render_design_document(spine))
    else:
        print(f"unknown command {cmd!r}. Usage: server.py [schema|template|validate <f>|render <f>] (no args = stdio MCP server)", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
