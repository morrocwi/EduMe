#!/usr/bin/env python3
"""
EduMe/UPCC MCP server — stdlib-only, stdio JSON-RPC (MCP protocol) *and* a plain CLI.

Two ways to run it, so it works whether or not the caller has an MCP client:

    python3 server.py                       # stdio MCP server (for an MCP host)
    python3 server.py validate design.json  # CLI: print validation result
    python3 server.py render design.json    # CLI: print rendered document
    python3 server.py schema                # CLI: print the spine JSON Schema
    python3 server.py template              # CLI: print the document template

No third-party packages, no network access, no filesystem writes at runtime (schema and template
are loaded once from the two sibling files below; everything else is pure computation on the
caller-supplied `spine` object).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE.parent / "schema" / "upcc_curriculum_spine.schema.json"
TEMPLATE_PATH = HERE.parent / "templates" / "DESIGN_CURRICULUM_DOCUMENT_TEMPLATE.md"
PROTOCOL = "2025-06-18"
TOOLS = ["get_spine_schema", "get_document_template", "validate_design", "render_design_document"]

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


def validate_design(spine, schema=None) -> dict:
    schema = schema or load_schema()
    if not isinstance(spine, dict):
        return {"valid": False, "missing_required": ["<root>"], "warnings": [f"spine is required and must be a JSON object; received: {type(spine).__name__}"]}
    missing = walk_missing(schema, spine)
    warnings = []
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
    return {"valid": len(missing) == 0, "missing_required": missing, "warnings": warnings}


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
        {"name": "validate_design", "description": "Validates a filled UPCC spine object; returns {valid, missing_required, warnings}.", "inputSchema": spine_input},
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
