# Demo Analysis — does the UPCC spine tool actually design curricula?

**Method:** 4 real-world problems, deliberately spanning the 2×2 matrix (online/offline × short/long),
run through the actual `mcp/server.py` CLI (`validate` then `render`) — not hand-simulated. Two of
the four were deliberately drafted with a real gap first (a v0 that should fail validation), fixed,
then re-validated, to check the tool actually catches incompleteness rather than rubber-stamping.

| # | Problem | Modality | Length | v0 had a gap? | Final result |
|---|---|---|---|---|---|
| 1 | New hires misroute support tickets | Online (async) | Short (90 min) | Yes — missing 3 assessment fields | Valid, rendered clean |
| 2 | Street vendors judge batch safety by taste | Offline (in-person) | Short (90 min) | No | Valid, rendered clean |
| 3 | Micro-business owners lose track of cash | Online (async, multi-week) | Long | Yes — missing `routes` and `sessions` arrays entirely | Valid, rendered clean |
| 4 | Health volunteers miss prenatal referral flags | Offline (field/apprenticeship) | Long | Yes — missing a required `working_words[].term` | Valid, rendered clean |

## What actually worked

- **The validator genuinely catches incompleteness**, not just structurally-present-but-empty
  fields: it correctly flagged 3 missing assessment fields (#1), 2 entirely-missing required
  arrays (#3), and 1 missing nested required field (#4) — each was a real gap I introduced on
  purpose, and each was caught before rendering, exactly as intended.
- **The renderer produces a genuinely readable, usable document** for all 4 shapes — a 90-minute
  async onboarding module and a multi-week field apprenticeship program render through the *same*
  10-section template without forcing either into an ill-fitting shape. The route/session tables
  scale naturally from 1 row (demo 1, 2) to 2 rows (demo 3, 4) with no special-casing needed.
- **The 6-field assessment chain (claim/task/observation/criteria/warrant/assistance_condition)
  held up as a real discipline, not decoration** — for demo 4 in particular (referral-flag
  accuracy), writing out `warrant` forced an explicit statement of *why* nurse-agreement is the
  real evidence rather than checklist completion alone, which is exactly the kind of thing UPCC's
  own "assisted performance ≠ Human Return" principle is trying to prevent going unexamined.

## What the testing found broken, and fixed for real

Two genuine implementation bugs were caught by this testing (not found by inspection — found
because the renderer produced visibly wrong output):

1. **Duplicate missing-field reporting.** An early version of `validate_design` re-checked
   `framing.working_words[i].term` in a hand-written loop *in addition to* the schema-driven
   recursive walk that already checked it — every missing `term` was reported twice. Fixed by
   deleting the redundant check and trusting the single schema-driven walk.
2. **The template's own documentation comment leaked into every rendered document.** The
   template's leading `<!-- ... {{path}} ... -->` explanation comment contains the literal text
   `{{path}}`, which the substitution regex matched and replaced as if it were real data —
   producing `[NOT YET SPECIFIED]` inside the *instructions*, in every single demo, not just the
   incomplete ones. Fixed by stripping the leading HTML comment before substitution runs.
3. **(A design bug, not just a code bug) Optional fields were being marked as gaps.** The first
   working version of the renderer marked *any* empty repeated-block field as `[NOT YET SPECIFIED]`,
   including genuinely optional ones (e.g. `framing.working_words[].changed_questions`, which the
   schema does not require). This would have taught every future user that filling in optional
   detail is mandatory, silently defeating the whole point of having a minimal "spine" in the first
   place. Fixed by looking up each array's actual per-item `required` list from the schema and only
   flagging fields that item schema genuinely requires.

## Honest limits — what this demo does NOT show

- **Content correctness was not checked** — the tool validates *structural completeness* (are the
  required fields present and non-empty), never whether the pH threshold, the referral thresholds,
  or the ledger-reconciliation tolerance stated in a demo are actually correct for that domain.
  That judgment call stays with a human subject-matter reviewer; nothing here should be read as
  "this course is pedagogically or factually sound," only "this course's design is complete
  against the UPCC spine's own structural requirements."
- **No learner ever actually took any of these courses.** This is a design-time tool. It cannot
  and does not claim anything about whether the rendered document, if delivered, would actually
  produce the stated Human Return in a real learner — that is exactly what UPCC's own separate
  Empirical Falsification Protocol (Layer 3) exists to test, and this demo did not invoke it.
- **Only 4 problems were tried**, chosen to span one 2×2 matrix (modality × length), not to be
  exhaustive. A genuinely adversarial test (e.g. a problem with no clean single "route", or one
  requiring multiple certifying bodies) was not attempted here.
- **Tier C (a plain chat session with no code execution, following the SKILL.md by hand) was not
  actually run in this pass** — only the CLI (tier B) was exercised for real. Whether an AI with no
  tool access genuinely produces the same result by hand-substitution is asserted by design, not
  independently demonstrated.

## Verdict

**Yes, it can design a structurally complete, UPCC-conformant curriculum for real, across
online/offline and short/long shapes** — demonstrated by 4 actually-executed validate→render round
trips, including 3 that started broken and were only fixed after genuine tool feedback. **No, this
does not demonstrate pedagogical correctness, learner outcomes, or the tier-C no-code-execution
path** — those remain explicitly open, not silently claimed.
