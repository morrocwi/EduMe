# UPCC — Unified System Readout (v1, 2026-09-20)

**Status: Dr-tier / Open — a readout of the corpus as it stands, not a certified claim. Produced by
two internal multi-agent research passes over 15 files. No independent
check has run on this document itself. Nothing here has been registered in Toledo, checked against
Readout Genesis, or deposited to Zenodo — this is the foundation pass the founder asked for before
the next stage of development.**

**Excluded, deliberately:** `02_APPLIED_EXAMPLE/ARAYA_PRIVATE_NIKAH_LEARNING_PATHWAY_v2.0_UPCC.md`
was never extracted, read, or analyzed in either pass — it is named PRIVATE and out of scope for
this document and for any public repo. See §5 of the glosa plan below for why it must also stay out
of any future deposit.

---

## 1. The system, as one stream

UPCC is a **four-layer system** for turning a lived problem into a traceable, non-collapsing change
in a human being — a curriculum-design *specialization* of the existing Toledo/HCA equation family,
not an independent mathematical universe of its own.

- **Layer 1 — Master architecture** (current: v1.3 `MODALITY_RHYTHM_CLOSURE_STANDALONE`). The
  conceptual spine: reuses the Toledo HCA "river" wholesale (Retained Difference → Human Readout →
  Live Problem → Barrier Readout → Candidate Routes → Human Endorsement → Adaptive Scaffold →
  Practice → Withdrawal → Human Return → Novel Transfer → World Feedback → Opportunity Conversion),
  wraps it in six operational-language word classes, a ten-category barrier taxonomy, adult/child
  governance, an eight-stage DCP epistemic cycle, an Evidence Ledger discipline, a
  refuse-to-collapse Net Advancement tuple, a Rhythm/Burden/Activity-State system, a full Delivery
  Modality Layer, and ~44 numbered non-collapse invariants. Proposes exactly **three** new objects
  (Curriculum Evidence Record, Curriculum Traceability Record, Scaffold Construction Record), each
  parented to Toledo codes and explicitly labeled PROPOSAL.
- **Layer 2 — Production/Compiler system** (current: v1.3 `MODALITY_ASYNC_ONEWAY`). The buildable
  manual: a 25-item output checklist, an 18-node Operational Curriculum Spine, a Tool Abstraction
  Layer (14 abstract functions, vendor-swappable), the same claim-ceiling ladder as Layer 1, a
  Delivery Modality Engine, one-way-media design method.
- **Layer 3 — Empirical Falsification Protocol** (current: v0.2 `PAPER_MECHANISM`). Introduces
  **zero** new Toledo equations. Its entire job is to try to break every node of Layers 1–2: a
  CLAIM/TASK/OBSERVATION/WARRANT chain, an Adversarial Task Bank, kill tests for propositions
  P1–P10, five experimental layers (red-team → mechanism tests → ablation → SMART/adaptive trials →
  confirmatory replication), and a six-way falsification decision rule.
- **Layer 4 (bridge, not a parallel research layer) — Institute Schema v2.0** (`UPCC-Core Edition`).
  A fillable authoring template + machine-readable YAML/JSON schema for independent
  (non-government-accredited) institutes. Its own header explicitly anchors it to "Master v1.3 +
  Production v1.3" — it sits **downstream of Master** (inherits its vocabulary without redefining
  it) and **upstream of Production** (its schema is the data contract Production consumes to emit
  17 AI-generatable deliverables: syllabus, teacher guide, assessment plan, etc.). It extends
  Layer 3's 4-field CLAIM/TASK/OBSERVATION/WARRANT chain to 6 fields (+CRITERIA, +ASSISTANCE
  CONDITION) for authoring-time assessment design. It cites **no** Toledo or Genesis codes at all —
  clean of the legacy namespace-invention mistake, but also a step below Master's own discipline of
  citing explicit parents for every reused node.

A pre-UPCC **legacy protocol track** (v0.1→v0.4) is the historical precursor: v0.1 invented an
independent `UPCC-*` equation namespace (~40 formulas), then progressively retracted almost all of
it in favor of direct Toledo-HCA reuse by v0.4 — the Toledo-lookup-first pipeline every current
layer still uses verbatim originates here. This is, in miniature, exactly the failure mode
`EPIS-REUSE-PIPELINE` now exists to prevent — reinvented and self-corrected before that standing
rule was written down.

## 2. Knowledge-graph node set (main.hub card shape)

Five nodes. Full detail (is/is_not/relations) is in `docs/UPCC_KG_NODES.json` in this repo —
condensed here:

| id | class | role | key relations |
|---|---|---|---|
| `legacy-upcc-protocol` | lineage-track | Superseded equation-track, v0.1→v0.4 | `superseded-by` → master; `cautionary-precedent-for` → institute-schema-v2 |
| `upcc-master-architecture` | current-layer | Layer 1, conceptual spine | `operationalized-by` → institute-schema-v2; `reuses` → toledo:CAN-098; `sibling-layer-of` → production-system |
| `upcc-production-system` | current-layer | Layer 2, compiler manual | `consumes-schema-from` → institute-schema-v2; `implements` → master-architecture |
| `upcc-empirical-falsification-protocol` | current-layer | Layer 3, adversarial testing | `field-chain-extended-by` → institute-schema-v2; `still-unresolved-duplication-with` → master-architecture |
| `upcc-institute-schema-v2` | bridge-artifact | Layer 4, authoring/data-schema bridge | `operationalizes` → master; `feeds-schema-into` → production; `extends-field-chain-of` → empirical-protocol; `unverified-against` → readout_genesis compatibility check |

## 3. Open questions / contradictions (not silently resolved)

1. **Genesis-compatibility check has never been run for anything in this corpus** — Toledo reuse
   discipline only. This is a real gap against the workspace's own `EPIS-REUSE-PIPELINE` two-step
   requirement (Toledo *and* Genesis), not something either UPCC pass can close on its own.
2. Master v1.3's own embedded falsification sections vs. the standalone Empirical Protocol v0.2 —
   supersede / mirror / summarize each other? Unresolved in the source text.
3. Cross-document version anchoring is inconsistent: Production v1.0–v1.2 cite Master v1.1; the
   Institute Schema v2.0 explicitly anchors to "Master v1.3 + Production v1.3" — but no text
   confirms Production v1.3 itself anchors to Master v1.3 rather than the older v1.1.
4. Institute Schema v2.0's renamed pipeline stages (Current Premise/Words, New Working Words,
   Changed Questions) are not mapped node-for-node onto Master's canonical HCA-river stage names —
   treat as an unreconciled restatement of one spine, not confirmed-identical.
5. v2.0's Alignment Map (9-column table) plausibly duplicates Master's Curriculum Traceability
   Record PROPOSAL under a new name; v2.0's per-section scaffold record plausibly duplicates the
   Scaffold Construction Record PROPOSAL. Neither document confirms this either way.
6. v2.0's 25 document sections vs. Production v1.3's own 25-item output checklist — same list
   restructured, a superset, or genuinely separate? Unconfirmed.
7. The Net Advancement tuple `A_HCA` carries a single "Burden" field even though the corpus
   insists burden is not reducible to one scalar — not fully reconciled in practice.
8. **Confirmed overclaim candidate (new finding, not merely "open"):** several files write
   `Rhythm_n = Ω(T_n, B_n)` as if it were a derivation, but its Toledo parent `CAN-198` is
   registered with an explicit non-collapse caveat: *"parallel descriptors, not a derivation
   chain."* **Corrected in `docs/UPCC_MASTER.md` §27.1** (2026-09-20 editorial pass) — original
   text preserved for lineage, correction marked as the authoritative reading.
9. `CAN-123` (group-state family) was split in the live registry into `weld/S.47–50.v1` /
   `CAN-123-SPLIT-01..04`. Pre-v0.4 files cite the pre-split parent generically (stale but not
   fabricated); **v0.4 already cites the correct split codes** — no action needed there.
10. Adaptive-Scaffold/Withdrawal fading relation (`CAN-104`) is marked OPEN in every version to
    date, including the live Toledo registry itself (`tier: Open`) — genuinely unresolved, not a
    documentation gap.

## 4. Toledo reuse-pipeline finding (the actual lookup was run — this is the good news)

Full report produced during this session's research pass (not included in this repo — headline result summarized here):

- **Almost every code the UPCC corpus cites resolves in the live `CANONICAL.json` to an entry whose
  registered name matches the UPCC file's own description.** ~30 codes cross-checked line-by-line
  (table in the report), all ✅. This is *not* a case of drift or fabrication.
- Object-by-object verdict: everything in Master/Production's non-collapse rules, tuples, and
  pipelines is **REUSE** (cite the code, don't restate under a new symbol). The curriculum-specific
  record schemas (`CURRICULUM_EVIDENCE_RECORD`, `CURRICULUM_TRACEABILITY_RECORD`,
  `SCAFFOLD_CONSTRUCTION_RECORD`, `ROUTE_DEPENDENCY_RECORD`, and a few less-formalized siblings) are
  **genuinely new** and already correctly labeled PROPOSAL by the corpus itself.
- What actually blocks real registration for every new-object candidate: **the Genesis-compatibility
  step (never run for anything here)**, no Coq file yet for any of them, and free-slot code numbers
  need to come from live registrar tooling, not be guessed.

## 5. Glosa / Zenodo positioning plan (planning only — nothing drafted or submitted)

Full report produced during this session's research pass (not included in this repo — headline points summarized here):

- Domain routes through **glosa** (human–AI collaboration/method), not Toledo (no new equations to
  register at the corpus level) or Genesis (no ontological claim) — per
  `toledo/EQUATION_SOURCE_POLICY.md`'s domain split.
- Needs a `glosa-blackbox-note` run with the founder **first** — no Blackbox Note exists yet for
  UPCC; drafting a claim card straight from the documents would be AI narrating AI, not human
  standpoint capture.
- Realistic K-state ceiling right now: **K0** (public working release, not peer reviewed) — K1 only
  becomes honest after a real cross-vendor independent check is actually run and logged.
- Full R1–R8 publish-gate pass required before any Zenodo submission, run by a session distinct from
  whoever assembles the deposit bundle (this session should not self-certify it).
- **The private applied-example file must never be part of any public deposit**, in whole, in
  redacted form, or by inference from cross-references — explicit standing constraint.

## 3a. Items 1 and 2 resolved (2026-09-20)

**Item 2 — Master v1.3 vs standalone Empirical Protocol v0.2: RESOLVED (inference, well-evidenced).**
Verdict: **Master v1.3 supersedes the standalone v0.2**, though v0.2 is never explicitly declared
obsolete. Evidence: Master lists v0.2 as its "Empirical anchor" (its own vocabulary for an absorbed
source), explicitly states it "consolidates... the empirical falsification programme into one
standalone specification," and reproduces essentially every structural piece of v0.2 (§46–§71)
under its own numbering — while also *extending* it (a new Stage-4 operational-language kill test,
a new §57 Operational-Language Ablation test, P2 decomposed into P2-a/b/c/d that v0.2 keeps nested).
Countervailing: Master compresses some of v0.2's fine-grained detail (hostile-task-trap
descriptions, some worked-example structure), and two of v0.2's sections (Level-4
additive-lens-preservation dual judgment; the Term-to-World Trajectory schema keys) weren't
confirmed reproduced in Master. **Practical read: treat Master v1.3 as the current authority; keep
v0.2 as a reference for the handful of not-clearly-reproduced sections rather than as a competing
"current" document.**

**Item 1 — Readout Genesis compatibility check: RUN, honest result is "open, not closed."**
Full gate-by-gate detail was produced during this session's research pass (not included in this repo — condensed here); the actual gate
definitions (read from the 7612-line core file, not from any one-line gloss):
was read from `~/ANSE.ASIA/readout_genesis/READOUT_GENESIS_CORE.md` directly, not from a gloss.

Checked against all 6 named gates (Exact Domain Gate, Reader Equivalence/Commuting-Square, Sufficiency,
Lineage Preservation, Occupation/Partition, Spine Lyapunov Face) for the 5 new PROPOSAL-track objects
(`CURRICULUM_EVIDENCE_RECORD`, `CURRICULUM_TRACEABILITY_RECORD`, `SCAFFOLD_CONSTRUCTION_RECORD`,
`ROUTE_DEPENDENCY_RECORD`, and the `TERM_TO_WORLD_TRAJECTORY`/`ORCHESTRATION_RECORD`/
`RETAINED_KNOWLEDGE_RECORD`/`CORRECTION_HISTORY_RECORD` group). **Every object's overall verdict is
`open-unresolved` — not compatible, not incompatible, not "passed."** Key findings, none papered over:

- Genesis's Seven General Gates are **explicitly stated to be domain-neutral** (A.13: "none of them
  is chemistry-specific, biology-specific, or physics-specific") — so it is *legitimate* to run a
  curriculum/pedagogy object through them, not a category error.
- BUT: none of the 5 UPCC objects has ever been formalized as the actual tuple Genesis's gates
  operate on — a retained state `𝔃`, a transition `F`, a question `𝒬`, a quotient `q_α`. Without that
  formal construction, most gates (domain gate, reader equivalence, sufficiency, lineage
  preservation) can't be resolved to compatible/incompatible from text alone — they come back
  `open-unresolved` because **the prerequisite step (formalize the object first) was never done**,
  not because the object failed a check.
- The **Occupation/Partition gate and the Spine Lyapunov Face gate come back `not-applicable`
  across every object** — these are tied to Genesis's literal synthesis-graph/spine-PDE machinery,
  which the source text itself (I.3) does not claim as physically settled even for physics; forcing
  a pedagogy object through that literal apparatus would be over-claiming, not rigor.
- Genesis's own text is candid that extending its spine machinery to non-physical domains
  (cognitive/social leaves, V.8/V.9) is tagged `[Dr]` (declared/narrative), not `Th_coqc` — i.e.
  Genesis itself doesn't claim proven domain-generality, only a framework commitment to try.
- `ROUTE_DEPENDENCY_RECORD` and the four-object implementation-record group are checked even more
  thinly, since their own formal content doesn't exist on disk anywhere yet — only the summary
  descriptions in this session's own handoff docs.

**Bottom line on item 1: the honest state after actually running the check is "still open, and now we
know exactly why" — not closed, not failed, not passed.** To move any of these 5 objects past
`open-unresolved`, each needs its own `(𝔃, F, 𝒬, q_α)` formalization done first (a real design task,
not a lookup), before the Domain/Reader-Equivalence/Sufficiency/Lineage gates can return an actual
verdict. This is now a concrete, scoped next step rather than a vague "never checked" gap.

## 6. What's still the founder's call (not decided here)

- **Repo placement.** The Institute Schema v2.0 is a bridge artifact, not a fifth independent node
  — it explicitly anchors to both Master and Production, which argues against it having a repo home
  independent of wherever those two end up. Three live options: (a) one dedicated `upcc` repo for
  all four layers; (b) fold Master+Production+v2.0 into the public `EduMe` repo as the buildable
  curriculum product, keep Empirical Falsification separate (readout_genesis/toledo-style); (c) some
  other split.
- **Whether/when to run the Genesis-compatibility check** that's been missing across the entire
  corpus's history.
- **Whether to correct the `Rhythm_n = Ω(...)` overclaim** before doing anything else with the
  Rhythm/Burden system, given it's now a confirmed (not merely suspected) mismatch against the live
  registry's own non-collapse wording.
- **Whether to fold in the two "how/when AI expands human potential" source papers** (`03_SOURCE_PAPERS/`,
  not yet extracted — likely already tracked elsewhere per `readout-genesis-repo.md` /
  `project-textbook-written-by-ai.md` memory) or treat them as separate from the UPCC system proper.

Everything above stays in scratch/staging until you say where it goes.
