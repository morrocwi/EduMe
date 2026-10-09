---
name: upcc-curriculum-designer
description: Design a UPCC-based course curriculum from a live-problem description. Triggers on "design a course", "curriculum for X", "หลักสูตร", "สอน", "training plan", "build a course on ___". Elicits the 17-field UPCC v2.0 spine (course identity/claim, live problem, learner, framing, routes, capability, content, sessions, assessment, support), validates it, and renders a Design Curriculum Document — without loading the full UPCC theory docs.
---

## When to use
- "design a course / curriculum for X"
- "หลักสูตร", "สอน", "training plan"
- Any request to turn a real-world problem into a teachable course

## Three ways to run this — pick whichever your environment supports

**A. You have this plugin installed (Claude Code, etc.):** you already have `schema/upcc_curriculum_spine.schema.json`, `templates/DESIGN_CURRICULUM_DOCUMENT_TEMPLATE.md`, and `mcp/server.py` available as repo files — use them directly (tier B or C below), or call the MCP tools if the server is also connected.

**B. You can download and run a script but have no MCP client** (e.g. a code-interpreter-capable session, or a user just running Python): download `mcp/server.py` (stdlib-only, no dependencies) and call it as a plain CLI —
```
python3 server.py schema                # print the spine JSON Schema
python3 server.py template               # print the document template
python3 server.py validate design.json   # {valid, missing_required, errors, warnings}
python3 server.py render design.json     # the rendered Design Curriculum Document
```
No install step, no MCP wiring — this is the path to focus on if you can execute Python but aren't a tool-calling agent.

**C. You are a plain chat session with no install and no execution ability at all** (e.g. an AI reading this repo through a browsing/paste feature, ChatGPT-style, with no plugin system and no code execution): **this is the path to focus on.** Read `schema/upcc_curriculum_spine.schema.json` and `templates/DESIGN_CURRICULUM_DOCUMENT_TEMPLATE.md` directly from the repo, follow the elicitation steps below by hand, self-check the 17 required fields are all present and non-empty (that's what "valid" means — no tool call needed to verify this yourself), and produce the final document by substituting your filled values into the template's placeholders yourself, marking any field you genuinely could not fill as `[NOT YET SPECIFIED]` rather than omitting it silently. The result is identical in content to tiers A/B — only the mechanism differs.

**D. A real MCP server is connected** (optional accelerator, not required by any of the above): call `get_spine_schema`, `validate_design`, `render_design_document` as tools instead of reading/computing by hand. Same result, less work.

## Core workflow (all tiers)

1. **Elicit the spine only** — the 17 fields defined in `schema/upcc_curriculum_spine.schema.json`:
   `course.identity`, `course.claim`, `course.non_claims`, `live_problem.situation`, `live_problem.purpose`, `learner.prior_knowledge`, `learner.barriers`, `framing.working_words`, `routes[]`, `capability.overall`, `capability.human_return`, `content.must_know`, `content.must_do`, `sessions[]`, `assessment` (6-field evidence chain incl. `assistance_condition`), `support.closure_pack`, `support.single_return_if_needed`.
   Do not repeat the field descriptions here — read the schema file for the exact elicitation question and required shape of each field. Ask one field (or tight cluster) at a time from the user's live-problem description; don't dump all 17 questions at once.
2. **Fill from the user's answers.** `routes[]` and `sessions[]` are uniform row-sets — encode them as TOON when passing them between tool calls or into a template-render prompt; `framing.working_words` and `assessment` are non-uniform/single-object — keep them as plain JSON (see the `toon-format` skill for why: TOON only wins on uniform tabular data).
3. **Validate** (tier B/D: call the tool/CLI; tier C: self-check the 17 fields against the schema by hand).
4. **Render** (tier B/D: call the tool/CLI; tier C: substitute into the template by hand).


### ONLINE_SYNCHRONOUS bridge rule (Toledo EQ-002/H.07.v1, CAN-1318)

Use this ONLY when synchronous **group videoconference** is actually part of the delivery. Do not use it for face-to-face, asynchronous, field or other modalities.

**Tier:** `EQ-002/H.07.v1` is registered in Toledo at tier **Definition** — a composition of maps, not a proved or validated causal law. In the linked standalone (`docs/TOLEDO_ZOOM_GLOBAL_FINAL_STANDALONE_v1_4_EDUME_LINKED.md`) unaided return, live possibility and realized opportunity are `NOT_YET_DIRECTLY_VALIDATED` (section 44AH); the header `empirical_status` block states `raw_row_independent_replication: not_yet_completed` and `universal_causal_validation: false`. The designer records a *design*; it never predicts a learner outcome and never carries numbers, probabilities, scores or "human potential" fields in this block.

**Canonical chain (9 states, 8 maps; use these names verbatim):**

```text
ZoomState --q_B--> Barrier --u*_{diag}--> CandidateRoute --Endorse_i--> LiveRoute --pi*_{scaffold}--> HumanReturn
  --Retention--> ReturnDelta --LiveField--> LiveField --G_O--> RealizedOpportunity --Record--> NetAdvancement
```

Set `delivery_mode: "ONLINE_SYNCHRONOUS"` (exact, upper-case) and fill `toledo_h07.stages` with all 9 stages in this order, each with `stage` and `design` (a description). Elicit one question per stage, and only when synchronous group videoconference is present:

1. **ZoomState** — What does the live session look like (who joins how, what is shown or said)? How will you read it?
2. **Barrier** — What is getting in each participant's way in the session right now, and how will you find out?
3. **CandidateRoute** — For each barrier, which routes could be offered?
4. **LiveRoute** — Which route does a *human* actually choose (set `endorser`: `human_learner`, `human_instructor`, `human_peer` or `human_other`)?
5. **HumanReturn** — With scaffolds removed, what does the participant do alone, later? (set `assistance_condition: "unassisted"`; give `evidence_basis`.)
6. **ReturnDelta** — In words, what changed in what they can do alone, and how retained?
7. **LiveField** — In words, what options are now genuinely open to them?
8. **RealizedOpportunity** — Which of those options did they actually use?
9. **NetAdvancement** — In words, what is the net change, including burden or cost?

`evidence_basis` values: platform traces `camera_on`, `attendance`, `session_duration`, `chat_volume`, `poll_response`; and genuine kinds `unaided_task_performance`, `delayed_unaided_task`, `work_product_review`, `human_observation`, `learner_reflection_record`, `other_documented_evidence`.

**Forbidden inferences (the validator rejects these with `valid: false`):**

- On any stage other than ZoomState and Barrier: `evidence_basis` made only of platform traces (camera-on, attendance/duration, chat volume, poll response), or an `evidence_plan` that mentions such traces while `evidence_basis` has no performance-type kind. These traces are allowed for ZoomState and Barrier only.
- On HumanReturn, ReturnDelta, RealizedOpportunity and NetAdvancement: no `evidence_basis`, or one without a performance-type kind (`unaided_task_performance`, `delayed_unaided_task`, `work_product_review`, `human_observation`). Reflection or other documented evidence alone does not pass.
- A LiveRoute endorsed by an AI/system. An AI suggestion is not a human choice.
- HumanReturn evidence under an "assisted" condition. Assisted performance is not unaided Human Return (consistent with `assessment.assistance_condition`).
- `toledo_h07` with a non-synchronous or missing `delivery_mode`; missing, duplicated or reordered stages; numeric fields.

**These checks are heuristic** — keyword and enum matching on what the designer wrote (see `mcp/server.py`). A pass means "no listed pattern was found", not "the evidence is adequate"; a human reviewer still decides.

Parents reused (cite, do not restate): `EQ-002/H.03.v1`, `A.5/H.17.v1`, `EQ-015/H.32.v1` (tier Open), `A.5/H.18.v1`, `A.8/H.03.v1`. Do not add a new equation here; any other formula must be labelled "NEW DERIVATION / PROPOSAL — not yet in Toledo". See `demos/demo5_zoom_seed_packet.json` for a worked example.

## Do NOT read the full theory docs for ordinary requests

Do **not** load `docs/UPCC_MASTER.md` or `docs/UPCC_PRODUCTION_SYSTEM.md` for a normal curriculum-design request — the spine schema above already encodes what an ordinary design needs, and loading those multi-thousand-line docs defeats this skill's minimal-token goal. Only read them when the user explicitly asks for: deep theoretical grounding, a specific extended artifact (e.g. the Tool Abstraction Layer), or a citation back to the underlying UPCC theory.

## Worked micro-example

**Live problem:** "Our street-food vendors don't know if today's batch of fermented sauce is safe to sell."
**Spine (excerpt):** `claim`: "Vendor can decide sell/hold from a pH reading" · `route`: pH meter → compare to threshold → log batch · `session S1`: 90 min, learner takes 3 real readings, evidence = 3/3 correctly classified unassisted.
**Rendered document opening:**
> ## Course: Safe-Batch Decision Training
> **Claim:** This course enables a vendor to decide, unassisted, whether today's batch is safe to sell, using a pH reading against a published threshold — not to formulate or certify the product...

See `demos/` in this repo for five full worked examples (four online/offline × short/long, plus one synchronous-videoconference design) with their actual rendered output.

## Status

Dr-tier design tool. Validated against 5 test curricula, 2 real bugs found and fixed during that
testing (see `demos/ANALYSIS.md`). Not independently reviewed by anyone other than this session.
