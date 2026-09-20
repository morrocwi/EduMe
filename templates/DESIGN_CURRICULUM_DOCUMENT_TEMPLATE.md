<!--
Design Curriculum Document — TEMPLATE (v1, 2026-09-20)
UPCC v2.0 spine schema (schema/upcc_curriculum_spine.schema.json) -> rendered deliverable.
Field paths below match the spine schema exactly (10 top-level keys, 17 spine fields).
{{path}} = scalar substitution. Any REQUIRED field left empty by the source design is substituted
as "[NOT YET SPECIFIED]" by the renderer, never silently dropped. Repeatable sections (routes,
sessions, framing.working_words) render one block per array item; an empty/missing required array
renders a single "[NOT YET SPECIFIED — no entries provided]" line instead of a blank section.
-->

> **Document status: Dr-tier design artifact — not a certified or accredited curriculum.**
> This document is the output of the UPCC v2.0 spine schema filled in below. It records a
> *design*, not a completion, delivery, or accreditation claim. Any statement of readiness or
> effectiveness in this document must match exactly what was specified in the fields below.
> A human reviewer must confirm this document before it is used with learners or institutions.

# {{course.identity.title}}

Design Curriculum Document — UPCC v2.0 spine

---

## 1. Course Identity & Claim

**Title:** {{course.identity.title}}

**Claim** — what this course commits to producing in the learner:
> {{course.claim}}

**Non-claims** — explicitly out of scope, stated so no one over-reads the claim above:
> {{course.non_claims}}

---

## 2. Live Problem & Purpose

- **Situation:** {{live_problem.situation}}
- **Purpose of this course:** {{live_problem.purpose}}

---

## 3. Learner Profile & Barriers

- **Prior knowledge assumed:** {{learner.prior_knowledge}}
- **Barriers:** {{learner.barriers}}

---

## 4. Framing — Working Words

One block per working word (the term/lens that reframes the problem into an actionable question):

{{#each framing.working_words}}
- **Term:** {{this.term}}
  - Opens: {{this.opens}}
  - Changed questions: {{this.changed_questions}}
{{/each}}

---

## 5. Route Map (question → domain → tool → workflow → criteria → skill)

| Question | Domain | Tool / function | Workflow | Criteria | Skill |
|---|---|---|---|---|---|
{{#each routes}}
| {{this.question}} | {{this.domain}} | {{this.tool_function}} | {{this.workflow}} | {{this.criteria}} | {{this.skill}} |
{{/each}}

---

## 6. Capability Outcomes (incl. Human Return)

- **Overall capability claim:** {{capability.overall}}
- **Human Return** (what the learner can do unassisted — the proof the capability is theirs):
  {{capability.human_return}}

---

## 7. Content Architecture

- **Must know:** {{content.must_know}}
- **Must do:** {{content.must_do}}

---

## 8. Session Plan

| Session | Time (min) | Capability target | Learner action | Artifact produced | Evidence |
|---|---|---|---|---|---|
{{#each sessions}}
| {{this.id}} | {{this.minutes}} | {{this.capability_target}} | {{this.learner_action}} | {{this.artifact}} | {{this.evidence}} |
{{/each}}

---

## 9. Assessment Plan

UPCC's 6-field evidence chain — stops the course from asserting a capability it never checked:

| Claim | Task | Observation | Criteria | Warrant | Assistance condition |
|---|---|---|---|---|---|
| {{assessment.claim}} | {{assessment.task}} | {{assessment.observation}} | {{assessment.criteria}} | {{assessment.warrant}} | {{assessment.assistance_condition}} |

---

## 10. Support & Closure

- **Closure pack** (what the learner leaves with): {{support.closure_pack}}
- **Single Return Window offered:** {{support.single_return_if_needed}}

This is the institute's *single* declared follow-up window, not an open-ended support
commitment — state its actual terms above, don't imply more availability than was designed.

---

*Generated against UPCC v2.0 spine schema. This is a minimal-token spine design — extended
fields (target group, modality, duration, learner experiential-capital detail, tool-abstraction
contracts, rhythm/activity-demand profile, alignment map) are deliberately deferred; ask for them
explicitly if this document needs to become a full syllabus/registration record.*
