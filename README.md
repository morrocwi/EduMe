# EduMe

Curriculum design and educational-development workspace built as a public expression of
**UPCC (Universal Problem-Centered Curriculum Compiler)** — the underlying theory this repo
implements. UPCC is a curriculum-design *specialization* of the existing Toledo/HCA equation
family, not an independent framework of its own.

## The four theory layers, at a glance

- **Layer 1 — Master architecture** (`docs/UPCC_MASTER.md`): the conceptual spine.
- **Layer 2 — Production/Compiler system** (`docs/UPCC_PRODUCTION_SYSTEM.md`): the buildable manual.
- **Layer 3 — Empirical Falsification Protocol** (`docs/UPCC_EMPIRICAL_FALSIFICATION_PROTOCOL.md`):
  tries to break every node of Layers 1–2. Introduces no new equations.
- **Layer 4 — Institute Schema v2.0** (`docs/UPCC_INSTITUTE_SCHEMA_v2.md` / `.json`): a fillable
  authoring template bridging Master and Production for independent institutes.

Reconciled overview: `docs/UPCC_UNIFIED_SYSTEM.md`. Knowledge-graph node set: `docs/UPCC_KG_NODES.json`.

## The actual tool: design a curriculum from this repo

`schema/upcc_curriculum_spine.schema.json` is a 17-field minimal-token subset of Layer 4's schema —
small enough to elicit and validate in one pass, load-bearing enough to produce a legitimate
(non-stub) design. `templates/DESIGN_CURRICULUM_DOCUMENT_TEMPLATE.md` renders a filled spine into
the actual deliverable an institute receives.

### Pick the path that matches what you can do — this repo does not assume everyone can install a plugin or run code

**No install, no code execution — a plain chat session reading this repo** (e.g. an AI given this
repo's files through browsing/paste, with no plugin system and no execution ability): **this is the
path to focus on if that's your situation.** Read `schema/upcc_curriculum_spine.schema.json` and
`templates/DESIGN_CURRICULUM_DOCUMENT_TEMPLATE.md` directly, follow the elicitation steps in
`plugins/upcc-curriculum-designer/skills/upcc-curriculum-designer/SKILL.md` by hand, self-check the
17 required fields yourself, and substitute your filled values into the template's placeholders
yourself — mark anything you couldn't fill as `[NOT YET SPECIFIED]` rather than dropping it. The
result is identical in content to the other two paths; only the mechanism differs.

**Can download and run a script, but no MCP client:** download `mcp/server.py` (Python 3 standard
library only — no dependencies, no network, no install step) and use it as a plain CLI:
```
python3 server.py schema                # print the spine JSON Schema
python3 server.py template               # print the document template
python3 server.py validate design.json   # {valid, missing_required, warnings}
python3 server.py render design.json     # the rendered Design Curriculum Document
```

**Full plugin/MCP-capable agent** (Claude Code, etc.): install the Skill —
`/plugin marketplace add morrocwi/EduMe` → `/plugin install upcc-curriculum-designer@edume-upcc` —
and optionally connect `mcp/server.py` as a real MCP stdio server for tool calls
(`get_spine_schema`, `get_document_template`, `validate_design`, `render_design_document`). The
API/MCP layer is a sub-resource the Skill may call when available — never a hard dependency.

### Proof this actually works, not just a design

`demos/` contains 4 real test curricula — spanning online/offline × short/long, run through the
actual `mcp/server.py` CLI, not hand-simulated — plus `demos/ANALYSIS.md`, an honest writeup
including two real implementation bugs the testing found and fixed (a duplicate-validation bug and
a template-substitution bug that leaked documentation text into the rendered output), and what the
demo does and does not prove. Install/uninstall of the MCP server registration was also verified for
real (add/remove a config entry, confirm clean state both ways) — see
`_intake/HANDOFF_UPCC_ultracode_2026-09-20.md` for the session record.

## Status — read this before relying on anything here

- **Evidentiary tier: Dr (declared/narrative), Open.** This is a readout of the corpus as it
  stands, not a certified claim. Nothing here should be read as "proven" or "validated."
- **No independent check has run** on the theory corpus or this document. It has not been through
  this workspace's own maker-checker or adversarial-review discipline.
- **Not yet registered in Toledo's canonical registry.** Toledo PROPOSAL entries have been drafted
  and are pending registrar review — see `registry/proposals/upcc_v1_0.json` in the `toledo`
  repository. Current honest status per object: `SCAFFOLD_CONSTRUCTION_RECORD` is gate-clean
  pending *independent* re-verification (self-checked only so far); `CURRICULUM_EVIDENCE_RECORD`
  and `CURRICULUM_TRACEABILITY_RECORD` still fail a real commuting-square check against a
  constructed real-world domain, for specific named reasons; `ROUTE_DEPENDENCY_RECORD` is
  deliberately held, not patched, since its lineage semantics belong to UPCC's own authors. None of
  the four has a Coq artifact, a registrar review, or an independent checker yet — reported plainly,
  not smoothed over.
- **No Readout Genesis compatibility certification** exists beyond this session's own Dr-tier
  formalization attempt; the honest result for every new object is "open, not closed."
- **No Zenodo deposit** has been made for this system.
- **The curriculum-design tool** (schema + template + `mcp/server.py`) has been tested against 4
  real demo curricula and works structurally — see `demos/ANALYSIS.md` for exactly what that does
  and does not prove (structural completeness, not pedagogical correctness or learner outcomes).

## What this repo does NOT contain

This repository does **not** include any private or applied-example content. Real deployments,
learner data, and organization-specific pathways built on top of UPCC live elsewhere and are
deliberately excluded from this public repo.

## License

See [LICENSE](LICENSE).
