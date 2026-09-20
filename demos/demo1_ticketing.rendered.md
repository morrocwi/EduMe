> **Document status: Dr-tier design artifact — not a certified or accredited curriculum.**
> This document is the output of the UPCC v2.0 spine schema filled in below. It records a
> *design*, not a completion, delivery, or accreditation claim. Any statement of readiness or
> effectiveness in this document must match exactly what was specified in the fields below.
> A human reviewer must confirm this document before it is used with learners or institutions.

# Ticketing System Quick-Start for New Hires

Design Curriculum Document — UPCC v2.0 spine

---

## 1. Course Identity & Claim

**Title:** Ticketing System Quick-Start for New Hires

**Claim** — what this course commits to producing in the learner:
> New hires can log, route, and close a support ticket correctly on their first day without a supervisor watching.

**Non-claims** — explicitly out of scope, stated so no one over-reads the claim above:
> Does not certify advanced ticket triage, SLA management, or escalation authority.

---

## 2. Live Problem & Purpose

- **Situation:** New hires open tickets in the wrong queue, skip required fields, and escalate issues that should be self-resolved, creating rework for senior staff.
- **Purpose of this course:** A new hire can independently create a correctly-routed, correctly-tagged ticket within their first shift.

---

## 3. Learner Profile & Barriers

- **Prior knowledge assumed:** Comfortable with basic web forms; no prior exposure to this specific ticketing tool or the team's queue structure.
- **Barriers:** No time for a multi-day onboarding course; must be usable async, on day one, in under 2 hours.

---

## 4. Framing — Working Words

One block per working word (the term/lens that reframes the problem into an actionable question):


- **Term:** queue-fit, not urgency-fit
  - Opens: a ticket is routed by WHO owns the fix, not by how urgent it feels
  - Changed questions: which team actually owns this class of problem?


---

## 5. Route Map (question → domain → tool → workflow → criteria → skill)

| Question | Domain | Tool / function | Workflow | Criteria | Skill |
|---|---|---|---|---|---|

| Which queue does this ticket belong in? | internal_support_ops | ticketing_system_queue_picker | read_symptom -> match_to_queue_table -> select_queue -> fill_required_fields -> submit | ticket lands in the queue matching the published symptom-to-queue table | queue_table_lookup_and_field_completion |


---

## 6. Capability Outcomes (incl. Human Return)

- **Overall capability claim:** New hire can create a correctly-routed, correctly-tagged ticket unassisted.
- **Human Return** (what the learner can do unassisted — the proof the capability is theirs):
  Given a new, unseen symptom description, the hire selects the right queue from the table and fills all required fields without asking a colleague.

---

## 7. Content Architecture

- **Must know:** The symptom-to-queue table; the required fields for a valid ticket.
- **Must do:** Create at least one real or simulated ticket end-to-end.

---

## 8. Session Plan

| Session | Time (min) | Capability target | Learner action | Artifact produced | Evidence |
|---|---|---|---|---|---|

| S1 | 90 | queue_selection_and_field_completion | Given 3 sample symptom descriptions, the learner creates 3 tickets in a sandbox instance. | 3 completed sandbox tickets | 3/3 tickets land in the correct queue with all required fields filled |


---

## 9. Assessment Plan

UPCC's 6-field evidence chain — stops the course from asserting a capability it never checked:

| Claim | Task | Observation | Criteria | Warrant | Assistance condition |
|---|---|---|---|---|---|
| Learner can independently create a correctly-routed ticket. | Create a ticket from a new, unseen symptom description in the sandbox instance. | Which queue the ticket lands in; which required fields are filled. | Ticket lands in the queue matching the published symptom-to-queue table AND all required fields are non-empty. | Correct queue + complete fields on an unseen symptom is the operational definition of 'can independently create a correctly-routed ticket' for this role — there is no additional real-world task this course claims to prepare for. | unassisted — no supervisor or reference material beyond the closure-pack quick-reference card, which is allowed since it ships with the role permanently. |

---

## 10. Support & Closure

- **Closure pack** (what the learner leaves with): symptom-to-queue quick-reference card, link to sandbox instance for future practice
- **Single Return Window offered:** True

This is the institute's *single* declared follow-up window, not an open-ended support
commitment — state its actual terms above, don't imply more availability than was designed.

---

*Generated against UPCC v2.0 spine schema. This is a minimal-token spine design — extended
fields (target group, modality, duration, learner experiential-capital detail, tool-abstraction
contracts, rhythm/activity-demand profile, alignment map) are deliberately deferred; ask for them
explicitly if this document needs to become a full syllabus/registration record.*

