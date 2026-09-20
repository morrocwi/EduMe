# UPCC CURRICULUM PRODUCTION SYSTEM
## A Tangible Course-Design and Delivery System
### From Live Problem → Operational Language → Tools / Workflow → Practice → Human Return

**Version:** 1.3  
**Status:** Standalone implementation manual  
**Architecture anchor:** `UPCC_MASTER_v1.1_RESTORED_COMPLETE_STANDALONE.md`  
**Purpose:** turn the UPCC architecture into courses that can be scheduled hour by hour, taught with real tools, supported before and after class, and audited from problem to Human Return.

---

# 0. What This Manual Produces

This manual turns an abstract curriculum architecture into a complete teaching package.

For any course, workshop, training programme, or learning module, the output should include:

```text
1. COURSE BRIEF
2. LIVE-PROBLEM MAP
3. CONTEXT / EXPERIENTIAL-CAPITAL INTAKE
4. SOURCE PACK
5. SOURCE-NAVIGATION PACK
6. WORKING-WORDS + OPERATIONAL-LANGUAGE MAP
7. ROUTE MAP
8. TOOL INVENTORY
9. WORKFLOW MAP
10. SKILL / ROLE MAP
11. ROUTE-DEPENDENCY MAP
12. HOUR-BY-HOUR LESSON PLAN
13. TEACHER GUIDE
14. LEARNER WORKBOOK
15. PRACTICE KIT
16. VERIFICATION KIT
17. HUMAN-RETURN ASSESSMENT
18. TRANSFER CASE
19. BEFORE-COURSE SUPPORT PLAN
20. DURING-COURSE SUPPORT PLAN
21. AFTER-COURSE SUPPORT PLAN
22. REFERRAL / EXPERT DIRECTORY
23. RETAINED-KNOWLEDGE RECORD
24. CORRECTION / FEEDBACK LOG
25. NEXT-CYCLE ACTION PLAN
```

The system is designed so that a curriculum designer can answer:

> What are we doing in hour 4?

> What tool is the learner using?

> What vocabulary must they understand before touching the tool?

> What workflow are they practising?

> What will the teacher do?

> What will the learner produce?

> What evidence will show that the learner—not the AI—can now do something?

---

# 1. The Operational Curriculum Spine

The implementation spine is:

```text
LIVE PROBLEM / PURPOSE
        ↓
CONTEXT + EXPERIENTIAL CAPITAL
        ↓
CURRENT WORDS / CURRENT FRAMING
        ↓
PROBLEM-JUNCTION WORDS
        ↓
CHANGED QUESTIONS
        ↓
ROUTE / DOMAIN
        ↓
OPERATIONAL LANGUAGE
        ↓
TOOL
        ↓
WORKFLOW
        ↓
CRITERIA / CHECKING
        ↓
SKILL / ROLE GAP
        ↓
MODELING
        ↓
COACHED PRACTICE
        ↓
REATTEMPT
        ↓
CHALLENGE + VERIFY
        ↓
REDUCE DECISIVE SUPPORT
        ↓
HUMAN RETURN
        ↓
TRANSFER
        ↓
WORLD / EXPERT FEEDBACK
        ↓
RETAINED KNOWLEDGE
        ↓
NEXT ACTION / NEXT PROBLEM
```

Everything in an hour-by-hour schedule must connect to this spine.

---

# 2. The Rule for Selecting Teaching Content

Do not begin with:

```text
"What chapters should we cover?"
```

Begin with:

```text
"What problem is this learner trying to handle?"

"What route has become relevant?"

"What tool / workflow does that route require?"

"What language must the learner understand to operate it?"

"What capability must become human-owned?"
```

Teaching content is selected because it enables the next valid move.

---

# 3. The Six Operational-Language Classes

Every route is translated into six language classes.

## 3.1 Problem-junction words

Purpose:

```text
change or sharpen the question
open another legitimate domain
surface another practice system
```

Examples:

```text
risk
stakeholder
counterparty
cash flow
constraint
root cause
evidence
jurisdiction
load
variance
```

---

## 3.2 Tool words

Purpose:

```text
recognize, select, understand, and operate the tool
```

Teach only what the selected tool actually requires.

Examples:

```text
input
output
parameter
cell
formula
filter
layer
query
column
field
range
unit
setting
mode
```

---

## 3.3 Workflow words

Purpose:

```text
navigate a sequence of work
```

Examples:

```text
intake
screen
classify
prioritize
verify
approve
handoff
iterate
escalate
close
```

Also teach:

```text
precondition
dependency
decision point
branch
handoff
review point
completion condition
```

---

## 3.4 Criteria / evidence / failure words

Purpose:

```text
judge whether an output or action is acceptable
```

Examples:

```text
threshold
valid
reliable
complete
consistent
exception
tolerance
failure mode
assumption
uncertainty
evidence
source
error
```

---

## 3.5 Skill / role words

Purpose:

```text
identify who must do what
and what competence the work requires
```

Examples:

```text
facilitator
analyst
reviewer
approver
operator
interpreter
advisor
supervisor
assessor
technician
```

Also teach:

```text
responsibility
scope
competence
supervision
handoff
review
```

---

## 3.6 Boundary / permission / referral words

Purpose:

```text
know when not to proceed alone
```

Examples:

```text
authorization
consent
jurisdiction
scope of practice
credential
high risk
irreversible
referral
escalation
expert review
```

---

# 4. Tool Abstraction Layer

UPCC must never bind a curriculum to a specific product.

A curriculum should depend on **tool functions**, not brand names.

The core relation is:

```text
LEARNING NEED
    ↓
ABSTRACT TOOL FUNCTION
    ↓
TOOL CONTRACT
    ↓
SELECTION CRITERIA
    ↓
CURRENT IMPLEMENTATION
```

A product may be replaced whenever another tool satisfies the same contract better.

Therefore:

```text
NotebookLM
is not the architecture.

ChatGPT
is not the architecture.

Google Classroom
is not the architecture.

H5P
is not the architecture.
```

They are only current implementations of abstract functions.

---

## 4.1 Tool Contract

Every tool slot in a course must be defined by a contract before a product is chosen.

```text
TOOL_CONTRACT:
    function_name
    educational_goal
    required_capabilities
    required_inputs
    required_outputs
    learner_actions_enabled
    teacher_actions_enabled
    evidence_created
    interoperability_needs
    privacy_requirements
    accessibility_requirements
    language_requirements
    offline_or_low_bandwidth_requirement
    safety_constraints
    cost_constraints
    human_override
    failure_modes
    substitution_criteria
```

The contract remains stable even when the product changes.

---

## 4.2 Tool Selection Rule

Select the tool that best satisfies the function under the actual context.

Selection criteria may include:

```text
FIT
    Does it perform the required learning function?

SOURCE TRACEABILITY
    Can learners see where claims / materials came from?

HUMAN AGENCY
    Can learner and teacher inspect, correct, override, or reject outputs?

PRACTICE FIDELITY
    Does the tool resemble the practice the learner must eventually perform?

INTEROPERABILITY
    Can artifacts move into / out of the rest of the course?

ACCESSIBILITY
    Can the actual learner population use it?

LANGUAGE
    Does it support the required language(s)?

PRIVACY / GOVERNANCE
    Is data handling appropriate to the learners and stakes?

COST
    Is access realistic?

RELIABILITY
    Will it work in the teaching environment?

OFFLINE / BANDWIDTH
    Can it function under actual infrastructure constraints?

TEACHER OPERABILITY
    Can instructors learn and administer it?

LONGEVITY
    Can the course survive if the vendor changes or disappears?

EXPORTABILITY
    Can learner work be retained outside the product?

SAFETY
    Does use stay within domain and learner-safety boundaries?
```

No single criterion always dominates.

---

## 4.3 Substitution Rule

A tool may be replaced without redesigning the curriculum when:

```text
new_tool.required_capabilities
    satisfy
tool_contract.required_capabilities

AND

new_tool does not weaken:
    governance
    evidence traceability
    practice fidelity
    accessibility
    safety
    Human Return design
```

If substitution changes the **learning function**, it is not merely a tool swap and the course must be recompiled.

Example:

```text
Replacing one source-grounded document navigator
with a better source-grounded document navigator
= possible substitution.

Replacing actual spreadsheet practice
with a chatbot describing spreadsheets
= NOT equivalent substitution.
```

---

## 4.4 Tool Registry

The course should maintain a replaceable registry:

```text
TOOL_REGISTRY:
    abstract_function
    current_tool
    version / date reviewed
    why_selected
    known limitations
    approved alternatives
    migration notes
```

This allows the curriculum to evolve without rewriting the conceptual design.

---

# 5. Abstract Tool Functions

The following functions are reusable across courses.

A course does not need every function.

It needs every function required by its capability target.

---

## F1. Intake / Human-Readout Function

### Goal

Capture enough learner context to route learning responsibly.

### Must support

```text
prior experience
current problem
prior attempts
language / access constraints
baseline evidence
support needs
```

### Output

```text
Human Readout
Experiential Capital
initial Barrier hypotheses
```

### Current examples

```text
structured interview
paper intake
Google Forms
LMS form
custom intake application
```

---

## F2. Source-Grounded Navigation Function

### Goal

Help learners work with a bounded source corpus without replacing the sources.

### Must support

```text
ingest curated sources
search / question across sources
return source-linked answers
navigate back to source
compare source passages
```

### Output

```text
source-grounded orientation
source references
questions for further checking
```

### Current examples

```text
NotebookLM
institutional document-search assistant
library / knowledge-base search
curated LMS source collection
```

Current example note: NotebookLM can answer questions grounded in provided sources and provides citations, while Google itself warns that generated responses can still be inaccurate. It also currently provides source-derived overview formats such as audio, slides, infographic, and video.  
citeturn637782search1

---

## F3. Generative Route-Exploration Function

### Goal

Expand possible framings, terms, routes, examples, counterexamples, and simulations.

### Must support

```text
alternative framing
candidate route generation
counterexample generation
role-play / simulation
question generation
challenge
changed-case generation
```

### Output

```text
candidate terms
candidate routes
candidate cases
candidate objections
```

### Current examples

```text
ChatGPT
other capable generative AI
human brainstorming facilitator
expert panel
```

This function generates candidates.

It is not automatically the verification function.

---

## F4. Operational-Language Support Function

### Goal

Help learners acquire the language needed to enter a selected practice system.

### Must support

```text
problem-junction words
tool words
workflow words
criteria words
failure words
skill / role words
boundary / referral words
```

### Output

```text
operational vocabulary in context
```

### Current examples

```text
annotated manual
interactive glossary
NotebookLM over curated manuals
flashcard system
H5P activity
physical cards
annotated interface
```

---

## F5. Actual Practice-Tool Function

### Goal

Let learners perform the real or defensibly simulated operation.

### Requirement

This function has the highest fidelity obligation.

Examples:

```text
spreadsheet work
→ actual spreadsheet application

coding
→ actual development environment

microscopy
→ microscope or defensible simulator

interviewing
→ actual interview interaction

negotiation
→ interactive negotiation

design
→ actual design tool / materials
```

A text-generating AI explaining a tool does not satisfy this function when actual tool operation is the target capability.

---

## F6. Workflow Representation Function

### Goal

Make sequence, handoffs, branch points, and completion conditions visible and usable.

### Must support

```text
ordered stages
dependencies
branching decisions
handoffs
review points
completion states
```

### Current examples

```text
SOP
checklist
flowchart
BPMN diagram
physical workflow cards
branching scenario
process application
```

---

## F7. Guided Practice / Simulation Function

### Goal

Create safe repeated action with feedback before full independent performance.

### Must support some combination of

```text
attempt
feedback
reattempt
branching
changing cases
error insertion
safe failure
```

### Current examples

```text
practice file
sandbox
simulator
role-play
case environment
H5P Branching Scenario
real equipment under supervision
```

H5P's current Branching Scenario supports choice-based paths with multiple branches and endings, while its Interactive Video and related content types can embed interaction into instructional material.  
citeturn637782search0turn637782search2turn637782search9

---

## F8. Verification / Resistance Function

### Goal

Introduce evidence or resistance sufficiently independent of the candidate-generation path.

### Must support

```text
check against authoritative or empirical source
perform calculation
inspect data
run experiment
apply external criterion
obtain qualified review
```

### Current examples

```text
primary source
official regulation
dataset
calculator
measurement instrument
experiment
qualified practitioner
independent rubric
```

Do not satisfy this slot merely by asking the same generative system again.

---

## F9. Collaboration / Orchestration Function

### Goal

Coordinate group work without confusing group output with individual capability.

### Must support as needed

```text
shared artifact
role assignment
peer objection
handoff
teacher monitoring
individual contribution trace
```

### Current examples

```text
LMS
shared document
collaborative whiteboard
breakout room
role cards
peer-review protocol
project-management system
```

---

## F10. Course Delivery / Sequencing Function

### Goal

Deliver materials, release tasks, collect work, and communicate the course path.

### Must support

```text
module organization
resource delivery
assignment release
submission
feedback
schedule
support links
```

### Current examples

```text
Google Classroom
Moodle
Canvas
institutional LMS
simple website + shared drive
paper-based course binder
```

The function does not require an LMS if a simpler system meets the same contract.

---

## F11. Diagnostic / Retrieval Function

### Goal

Collect low-cost evidence about current knowledge or recall.

### Must support

```text
short response
classification
retrieval
basic scoring / review
```

### Current examples

```text
Google Forms
LMS quiz
H5P question set
paper quiz
oral questioning
```

This function is not sufficient for assessing tool operation, workflow judgment, or professional capability.

---

## F12. Human-Return Function

### Goal

Observe what the learner can now do with reduced decisive assistance.

### Must support

```text
new / changed task
reduced hints
independent decision
tool use where appropriate
error detection
boundary judgment
```

### Current examples

```text
new case
live demonstration
blank workflow task
oral defense
reduced-hint tool task
field task
```

Human Return is a learning function, not a software product.

---

## F13. Retention / Portfolio Function

### Goal

Preserve learner-owned traces across cycles.

### Must support

```text
retained knowledge
correction history
practice evidence
transfer evidence
reflection
next action
```

### Current examples

```text
portfolio
Google Drive
LMS journal
Git repository
physical logbook
competency record
```

---

## F14. Support / Escalation / Referral Function

### Goal

Route learners to the right level of support.

### Must support

```text
self-help
peer
AI support
teacher
practitioner
institutional escalation
```

### Current examples

```text
FAQ
office hours
chat channel
help desk
mentor system
expert directory
appointment system
formal referral process
```

---

# 6. Tool Completeness Is Functional Completeness

A course is not "complete" because it uses many technologies.

It is complete when every required learning function has a valid implementation.

Use a matrix:

| Abstract Function | Required? | Selected Implementation | Why | Backup / Substitute |
|---|---|---|---|---|
| F1 Intake / Readout | Y/N | | | |
| F2 Source Navigation | Y/N | | | |
| F3 Route Exploration | Y/N | | | |
| F4 Operational Language | Y/N | | | |
| F5 Actual Practice Tool | Y/N | | | |
| F6 Workflow Representation | Y/N | | | |
| F7 Practice / Simulation | Y/N | | | |
| F8 Verification / Resistance | Y/N | | | |
| F9 Collaboration | Y/N | | | |
| F10 Delivery / Sequencing | Y/N | | | |
| F11 Diagnostic / Retrieval | Y/N | | | |
| F12 Human Return | Y/N | | | |
| F13 Retention / Portfolio | Y/N | | | |
| F14 Support / Referral | Y/N | | | |

`N/A` must have a reason.

---

# 7. Future-Proofing Rule

Every course should be able to survive tool obsolescence.

Before launch, ask:

```text
If this product disappears tomorrow:

What learning function would be lost?

What data or learner work would be trapped?

What other tool could satisfy the same contract?

Can we export the artifacts?

Does the teacher know the underlying method without the product?
```

The course design should remain intelligible without the brand name.

---

# 8. Example of Abstraction Before Product

Bad design:

```text
Hour 4:
Use NotebookLM for 30 minutes.
```

Better design:

```text
Hour 4 objective:
Learner must navigate a bounded source corpus,
locate where a workflow term is defined,
compare two source statements,
and return to the original source.

Required function:
SOURCE-GROUNDED NAVIGATION.

Current implementation:
NotebookLM.

Acceptable future substitute:
any system that satisfies the same source-grounding,
citation, navigation, governance, and accessibility contract.
```

Bad design:

```text
Use H5P Branching Scenario.
```

Better design:

```text
Required function:
SAFE BRANCHING WORKFLOW PRACTICE.

Learner must make decision-point choices,
experience consequences,
receive feedback,
and retry.

Current implementation example:
H5P Branching Scenario.

Other possible implementation:
live role-play,
custom simulator,
LMS branching lesson,
physical decision cards,
future adaptive simulation tool.
```

---



# 8. Delivery Modality Engine

Before building sessions, choose how the learning functions will be delivered.

```text
FACE_TO_FACE
ONLINE_SYNCHRONOUS
ASYNC_SELF_PACED
ONE_WAY_MEDIA
BLENDED
FIELD / APPRENTICESHIP
HYBRID / MIXED
```

Do not choose modality from convenience alone.

Ask:

```text
What must the learner actually do?
Which parts require live feedback?
Which parts require a real tool?
Which parts can be learned by watching?
Which parts require practice?
Which parts require an assessor?
Which parts can be self-paced?
Which parts need peer or expert interaction?
```

---

## 8.1 Modality Planning Card

```text
MODALITY:

CAPABILITY TARGET:

WHAT CAN BE TAUGHT ONE-WAY:

WHAT REQUIRES LEARNER ACTION:

WHAT REQUIRES FEEDBACK:

WHAT REQUIRES ACTUAL TOOL USE:

WHAT REQUIRES LIVE / EXPERT INTERACTION:

WHAT CAN BE SELF-PACED:

WHAT EVIDENCE CAN THIS MODALITY PRODUCE:

WHAT THIS MODALITY CANNOT CLAIM:

COMPENSATING DESIGN:
```

---

## 8.2 One-Way Media Course Design

A course may legitimately be:

```text
video 1
video 2
video 3
...
video N
```

but the curriculum compiler should not treat the playlist itself as the learning architecture.

Each clip must have a function such as:

```text
ORIENT
EXPLAIN
MODEL
DEMONSTRATE
CHALLENGE
PROMPT_ACTION
REVIEW
PREPARE_TRANSFER
```

Recommended sequence pattern:

```text
CLIP
    ↓
STOP POINT
    ↓
LEARNER ACTION
    ↓
SELF-CHECK / ARTIFACT
    ↓
NEXT CLIP
```

For pure orientation courses, some clips may legitimately require no artifact.

For skill courses, long runs of passive clips are insufficient.

---

## 8.3 Video Segment Card

```text
CLIP / SEGMENT:

FUNCTION:

CAPABILITY LINK:

PREREQUISITE:

KEY OPERATIONAL WORDS:

WHAT THE LEARNER WATCHES:

WHAT THE LEARNER MUST NOTICE:

PAUSE / STOP POINT:

WHAT THE LEARNER DOES NEXT:

TOOL / MATERIAL NEEDED:

SELF-CHECK:

ARTIFACT IF ANY:

NEXT SEGMENT CONDITION:
```

---

## 8.4 Self-Paced Course Rhythm

Do not impose a universal clip length.

Use learner control:

```text
pause
resume
replay
change pace
move to practice
take a break
return later
```

Design visible transitions:

```text
WATCH
→ DO
→ CHECK
→ CONTINUE
```

A long recorded lecture can remain a reference resource, but it should not automatically become one uninterrupted skill-learning block.

---

## 8.5 Self-Paced Course Claim Levels

### Exposure Course

```text
content presented
```

### Orientation Course

Adds:

```text
self-check
key language
source navigation
```

### Guided Application Course

Adds:

```text
practice
worked examples
feedback / answer keys
reattempt
```

### Evidenced Performance Course

Adds:

```text
submitted artifact
recorded demonstration
inspectable tool task
criteria-based review
```

### Human Return / Transfer Course

Adds:

```text
reduced-support performance
changed case
transfer
appropriate verification
```

Certificate wording and public claims should match the highest level actually evidenced.

---

## 8.6 Online Synchronous Profile

Useful functions:

```text
live explanation
Q&A
screen demonstration
breakout work
peer challenge
teacher feedback
shared documents
live digital tool use
```

Potential gaps:

```text
physical equipment
environmental observation
certain embodied skills
local supervision
```

Fill gaps through:

```text
home kit
simulation
local tool
later onsite block
```

---

## 8.7 Blended Profile

Assign functions deliberately.

Example:

```text
ASYNC BEFORE
    orientation
    vocabulary
    source navigation
    demonstration

LIVE
    diagnosis
    coached practice
    challenge
    correction

ASYNC AFTER
    reattempt
    changed case
    retained-knowledge record
```

Do not duplicate the same lecture online and in class unless repetition has a declared purpose.

---

## 8.8 One-Way Course Support

One-way delivery should not create heavy follow-up.

At course end provide:

```text
source pack
tool / practice route
FAQ
boundary / referral route
optional help channel
next action
```

Default:

```text
NO repeated proactive follow-up
```

If the course needs delayed evidence, use the same **Single Return Window** protocol.

If the course is orientation-only, even that return may be unnecessary.

---


# 9. The Course-Design Workspace

Before designing lessons, create one project folder.

Recommended structure:

```text
00_COURSE_BRIEF/
01_PROBLEM_CONTEXT/
02_SOURCE_PACK/
03_SOURCE_NAVIGATION/
04_WORKING_WORDS/
05_ROUTE_MAP/
06_TOOL_WORKFLOW/
07_SKILL_ROLE/
08_DEPENDENCIES/
09_HOURLY_PLANS/
10_TEACHER_GUIDE/
11_LEARNER_WORKBOOK/
12_PRACTICE_KIT/
13_VERIFICATION/
14_HUMAN_RETURN/
15_TRANSFER/
16_SUPPORT_BEFORE/
17_SUPPORT_AFTER/
18_REFERRAL_EXPERTS/
19_RETAINED_KNOWLEDGE/
20_CORRECTION_LOG/
```

This folder is the practical equivalent of the curriculum traceability record.

---

# 5. Step Zero: Course Brief

Before opening NotebookLM, AI, or a textbook, freeze a one-page course brief.

```text
COURSE TITLE:

LEARNER GROUP:

AGE / GOVERNANCE STATUS:

LIVE PROBLEM OR PURPOSE:

WHY THIS MATTERS TO THE LEARNER:

EXTERNAL REQUIREMENTS:

TIME AVAILABLE:

TARGET HUMAN-OWNED CAPABILITY:

WHAT MAY REMAIN TOOL-ASSISTED:

STAKES:

IRREVERSIBILITY:

PERMISSIONS / SAFETY:

EXPECTED WORLD CONTEXT:

SUCCESS EVIDENCE:

TRANSFER CASE:

AFTER-COURSE ACTION:
```

If these fields are unclear, do not begin writing slides.

---

# 6. Before-Course Research and Planning

The designer performs eight tasks before building the hourly schedule.

## 6.1 Read the real problem

Collect:

```text
learner stories
real cases
common failures
prior attempts
institutional constraints
existing forms / records / examples
local terminology
```

Output:

`PROBLEM_CONTEXT_BRIEF`

---

## 6.2 Build the Source Pack

Do not use one textbook for every function.

Build a small source ecology.

### Source Type A — Core explanatory source

Use for:

```text
conceptual orientation
definitions
basic models
```

Examples:

```text
textbook chapter
official handbook
professional manual
high-quality review
```

### Source Type B — Tool manual

Use for:

```text
tool words
operations
commands
settings
```

Examples:

```text
software manual
equipment guide
spreadsheet reference
instrument manual
```

### Source Type C — Workflow / SOP source

Use for:

```text
sequence
handoffs
decision points
review points
```

Examples:

```text
SOP
checklist
procedure
process diagram
professional guideline
```

### Source Type D — Criteria / evidence source

Use for:

```text
what counts as acceptable
what must be checked
```

Examples:

```text
rubric
standard
regulation
evidence guideline
quality checklist
```

### Source Type E — Case source

Use for:

```text
examples
failures
edge cases
transfer cases
```

Examples:

```text
real case
case report
incident
worked example
sample project
```

### Source Type F — Local-context source

Use for:

```text
local law
institutional rule
local language
local process
resource constraints
```

### Source Type G — Failure / boundary source

Use for:

```text
red flags
common errors
scope limits
referral rules
```

---

# 12. Current Example: NotebookLM for Source-Grounded Navigation

Use NotebookLM when the learner or teacher needs to work repeatedly with a bounded set of sources.

Recommended uses:

```text
upload the curated source pack

ask source-grounded questions

compare definitions across sources

generate a study guide

create an FAQ

surface key terms

create source-based briefing materials

generate Audio Overview / other source summaries when useful

ask:
    "Which source supports this?"
    "Where do these two manuals disagree?"
    "What terms must I know before using this workflow?"
```

NotebookLM should function as:

```text
SOURCE NAVIGATOR
not
FINAL AUTHORITY
```

Rule:

```text
NotebookLM answer
→ inspect citation / source
→ verify against the actual source when the claim matters
```

Create one notebook per coherent module or problem cluster rather than one enormous notebook for the entire programme.

Recommended notebook contents:

```text
01 core explanation
02 tool manual
03 workflow / SOP
04 criteria / standard
05 2–5 cases
06 local-context source
07 failure / boundary guide
```

---

# 13. Current Example: Generative AI for Route Exploration and Challenge

Use ChatGPT or another generative AI for tasks such as:

```text
generate alternative framings

identify possible domains

suggest problem-junction terms

generate candidate routes

create counterexamples

challenge assumptions

role-play a practitioner / client / reviewer

generate changed-case practice

simulate objections

create draft practice data or scenarios
```

Do not use the same generative dialogue as the sole source of verification.

Useful prompt modes:

```text
EXPAND
"What other legitimate lenses might expose a different practice system?"

CHALLENGE
"What important fact might this framing make disappear?"

DISCRIMINATE
"What observation would distinguish these two explanations?"

WORKFLOW
"What are the decision points in this process?"

FAILURE
"Where does this workflow commonly fail?"

BOUNDARY
"What should a novice not do without supervision?"
```

---

# 14. Current Example: LMS / Course Hub for Delivery

Use an LMS or course hub to distribute and schedule the learning path.

Possible backbone:

```text
Google Classroom
Moodle
institutional LMS
```

The LMS should contain:

```text
course map
scheduled materials
source pack
pre-work
hour-by-hour activities
assignments
practice files
feedback
return tasks
after-course challenges
support contacts
```

Do not turn the LMS into a file dump.

Organize it around the learning trajectory.

Suggested module naming:

```text
0. Before We Start
1. The Problem
2. The Words
3. The Route
4. The Tool
5. The Workflow
6. Practice
7. Challenge and Verify
8. Do It With Less Help
9. Transfer
10. Bring It Back to the World
11. What Stays With You
```

---

# 15. Current Example: Lightweight Diagnostic Tools

Use simple tools for low-cost diagnostics.

Possible tools:

```text
Google Forms
LMS quiz
H5P quiz
short oral check
whiteboard task
tool demonstration
mini case
```

Use a quiz only when the target is quiz-like knowledge.

For workflow, tool use, judgment, or boundary recognition, use performance tasks instead.

---

# 16. Current Example: Interactive-Practice Platforms

H5P is useful for converting passive material into bounded interactive practice.

Useful content types include:

```text
Interactive Video
Branching Scenario
Course Presentation
Quiz / Question Set
Drag and Drop
Mark the Words
Flashcards
Interactive Book
Virtual Tour
```

Best UPCC uses:

```text
pause a demonstration video at a decision point

branch learners based on workflow choice

ask learners to identify failure modes

sequence workflow stages

classify candidate knowledge status

choose the correct referral / escalation point
```

Use H5P to rehearse decisions.

Do not use it as a substitute for real tool practice when the tool itself is available.

---

# 17. Physical Teaching Equipment

Digital curriculum still needs physical teaching design.

Minimum classroom kit:

```text
projector / large display
whiteboard
markers
sticky notes
A3 paper
index cards
timer
learner laptops / tablets as needed
charging access
internet
printed backup materials
```

Useful UPCC-specific physical materials:

```text
PROBLEM CARDS
WORKING-WORD CARDS
TOOL CARDS
WORKFLOW CARDS
CRITERIA CARDS
FAILURE-MODE CARDS
ROLE CARDS
BOUNDARY / REFERRAL CARDS
EVIDENCE CARDS
```

These allow learners to physically build:

```text
problem → word → route → tool → workflow → check
```

before the same logic is moved into software.

---

# 18. Course Artifacts the Learner Produces

Each course should leave a visible trail.

## Artifact A — Problem Card

```text
What happened?
What matters?
What is observed?
What is inferred?
What is unknown?
What has already been tried?
```

---

## Artifact B — Working-Words Map

```text
current term
alternative term / lens
questions opened
critical facts preserved
```

---

## Artifact C — Route Map

```text
term
→ domain
→ tool
→ workflow
→ criterion
→ skill / role
```

---

## Artifact D — Operational-Language Sheet

```text
tool words
workflow words
criteria words
failure words
skill / role words
boundary words
```

---

## Artifact E — Tool / Workflow Map

```text
input
action
decision point
output
check
handoff
```

---

## Artifact F — Skill-Gap Ledger

```text
I can already do:
I can do with help:
I cannot yet do:
I must not do without supervision:
```

---

## Artifact G — Practice Log

```text
attempt
error
feedback
change
reattempt
```

---

## Artifact H — Verification Ledger

```text
claim
source / method
independent?
result
revision
```

---

## Artifact I — Human Return Card

```text
I can now:
I can check:
I still need help with:
I know to stop / refer when:
```

---

## Artifact J — Retained Knowledge Card

```text
what has a basis
what I can do
when it applies
how I check it
where it fails / when I refer
```

---

# 18A. Attention–Energy–Movement Design Protocol

UPCC does not assign a hidden "energy score" to a learner.

Course delivery uses two visible objects:

```text
LEARNER_ACTIVITY_STATE_READOUT
+
ACTIVITY_DEMAND_PROFILE
```

and adapts the activity when the fit degrades.

## Learner-state signals

Possible bounded observations:

```text
response slows
errors increase
participation changes
learner asks to pause
learner wants to move
posture / orientation changes
learner reports tiredness
learner reports boredom
learner reports overload
learner reports under-challenge
```

Never infer a diagnosis from one signal.

---

## Activity demand

Each block should identify:

```text
duration
cognitive demand
literacy demand
stillness demand
movement opportunity
social demand
decision density
novelty
tool switching
verification demand
```

---

## Adaptation menu

If the planned mode no longer fits, preserve the capability target and change the mode:

```text
KEEP
SHORTEN
SWITCH_MODE
ADD_MOVEMENT
BREAK
LOWER_DEMAND
RAISE_CHALLENGE
SOCIALIZE
INDIVIDUALIZE
RETURN_TO_PRACTICE
```

Examples of movement that remain instructional:

```text
stand and sequence workflow cards
move to a tool station
gallery walk competing solutions
perform the actual procedure
role-play a handoff
inspect an environment
physically sort evidence / criteria
```

Movement is therefore not restricted to "break time."

---

## Design rule

Do not force every course into a fixed ratio such as:

```text
20 minutes lecture
10 minutes activity
5 minutes break
```

Instead:

```text
planned time budget
→ observe learner/group
→ compare with activity demand
→ adapt while preserving the target
```

Private and group formats may use different proportions.

---

# 19. The Default One-Hour Learning Pattern

A normal 60-minute UPCC hour should not be 60 minutes of lecture.

Default pattern:

```text
00–08  RETURN TO THE LIVE PROBLEM
       reconnect activity to the problem

08–18  INPUT / MODEL
       only the knowledge / vocabulary / demonstration required now

18–38  LEARNER ACTION
       learner uses the tool, workflow, case, or source

38–48  RESISTANCE
       error, counterexample, comparison, peer challenge, evidence check

48–56  REATTEMPT / INTEGRATE
       learner revises and acts again

56–60  RETURN TRACE
       learner records what is now clearer / doable / uncertain
```

This is a default rhythm, not a mandatory formula.

Some hours should be almost entirely practice.

Some should be fieldwork.

Some should be source analysis.

---

# 20. Activity Types by UPCC Stage

| UPCC Stage | Good Activity Types | Avoid |
|---|---|---|
| Live Problem | case reconstruction, story, artifact inspection, field observation | starting with abstract definitions |
| Context Injection | interview, timeline, observed-vs-inferred sorting, constraint map | generic prompt writing |
| Working Words | term comparison, concept cards, lens swap, question rewrite | glossary memorization only |
| Route Generation | route mapping, domain hunt, expert-role map, AI expansion | one "correct" route too early |
| Operational Language | manual scavenger hunt, label tool screenshot, workflow vocabulary task | decontextual vocabulary lists |
| Tool | live demonstration, guided tool use, sandbox task | screenshots only |
| Workflow | cards sequencing, branching scenario, role-play handoff, SOP walkthrough | lecture on steps only |
| Criteria / Checking | compare outputs, apply rubric, detect error, verify claim | teacher says "correct" without criteria |
| Skill / Role | supervised performance, role handoff, practitioner demonstration | role-title memorization |
| Practice | attempt-feedback-reattempt, varied cases, tool task | passive review |
| Challenge | counterexample, red-team, opposite case, false premise | confirmation-only AI use |
| Verify | primary source check, calculation, experiment, expert review | another AI paraphrase |
| Withdrawal | reduced prompts, hidden workflow, tool-only condition | abrupt total removal of all tools |
| Human Return | reduced-help performance, explain decisions, detect new error | final artifact only |
| Transfer | changed case, different format, new surface features | exact repetition |
| World Feedback | simulation, practitioner critique, client/user test, local rule check | AI-generated approval only |
| Retention | teach-back, delayed return, next-problem bridge | immediate recall only |

---

# 21. Current Tool Examples by Stage

## Before learning

```text
Google Forms / intake form
    learner context
    prior experience
    diagnostic

Google Drive / shared folder
    source pack

NotebookLM
    source-grounded orientation

Google Classroom / LMS
    schedule + pre-work + support information

Video / short demo
    course orientation

Calendar / reminders
    deadlines and support sessions
```

---

## Problem and framing

```text
paper / whiteboard
problem card
timeline
stakeholder map
ChatGPT for alternative framing
NotebookLM for source-grounded clarification
```

---

## Working words / operational language

```text
source glossary
manual
source-grounded navigation / Q&A
working-word cards
shared Google Doc
H5P flashcards only for retrieval support
actual tool interface screenshots
```

---

## Tool / workflow

```text
actual software / physical tool
sandbox or demo account
SOP
workflow diagram
screen recording
H5P Branching Scenario
checklist
```

---

## Practice

```text
real tool
practice file
simulator
case packet
worked example
teacher / practitioner coaching
screen recording for review
```

---

## Verification

```text
primary source
manual
dataset
calculator
measurement instrument
qualified expert
official regulation
independent rubric
```

---

## Human Return

```text
new case
reduced-AI condition
tool with fewer hints
blank workflow sheet
oral explanation
live demonstration
error diagnosis task
```

---

## After learning

```text
Google Classroom / LMS
scheduled transfer cases

Google Forms
short delayed return checks

NotebookLM
source re-entry / revision

Google Docs
retained-knowledge journal

expert / mentor clinic
real referral path

calendar reminders
spaced return tasks
```

---

# 22. Source Pack + Source-Navigation Pack

For every course module, prepare a bounded pack.

Minimum:

```text
1 CORE TEXT
1 TOOL MANUAL
1 WORKFLOW / SOP
1 CRITERIA / STANDARD
2–5 CASES
1 FAILURE / BOUNDARY GUIDE
1 LOCAL-CONTEXT SOURCE
```

Optional:

```text
video demonstration
audio
sample data
template
worked example
expert interview
```

Do not upload random web results into the learning notebook.

The source pack should be curated before the learner enters it.

---

# 23. Teacher Preparation Pack

The teacher receives:

```text
COURSE MAP

LIVE-PROBLEM BACKGROUND

KNOWN LEARNER BARRIERS

WORKING-WORD MAP

TOOL / WORKFLOW MANUAL

KEY FAILURE MODES

MODEL DEMONSTRATION SCRIPT

SCaffold options

CHALLENGE PROMPTS

VERIFICATION ROUTES

REFERRAL BOUNDARIES

HUMAN-RETURN RUBRIC

TRANSFER CASE

AFTER-COURSE SUPPORT PLAN
```

Teacher preparation is not "make slides."

It is preparation to orchestrate a trajectory.

---

# 24. Learner Preparation Pack

Send 3–7 days before the course when possible.

Include:

```text
one-page welcome

why the course matters

one short real case

intake / diagnostic

tool access instructions

required accounts

source-navigation environment / source pack link if used

5–15 essential terms only

what to bring

what the learner should NOT prepare

support contact

accessibility / language support route
```

Do not front-load the entire textbook.

---

# 25. Technical Readiness Before Class

At least 24 hours before class, verify:

```text
login works
internet works
software version
practice files open
permissions correct
links work
LMS access
source-navigation tool access
projector
audio
charging
backup files
printed fallback
```

A technical failure should not become a false "skill deficit."

---

# 26. Before-Course Support System

Use three support lanes.

## Lane A — Orientation

```text
short video
course map
FAQ
NotebookLM notebook
tool setup guide
```

---

## Lane B — Human help

```text
office hour
chat channel
email
teacher assistant
language / accessibility support
```

---

## Lane C — Risk / referral

```text
privacy questions
child / adult governance
professional boundary
technical escalation
expert referral
```

Every learner should know which lane to use before class starts.

---

# 27. During-Course Support System

Do not make all support come from the instructor.

Recommended structure:

```text
LEVEL 0
self-check:
    checklist / source / notebook / tool help

LEVEL 1
peer:
    compare reasoning / workflow

LEVEL 2
AI:
    explanation / alternative framing / simulation

LEVEL 3
teacher:
    diagnose barrier / scaffold / feedback

LEVEL 4
practitioner / expert:
    domain boundary / high-stakes judgment

LEVEL 5
institution:
    permission / credential / formal action
```

Escalation should be visible.

---

# 28. Course Closure + Single Return Protocol

A course should close cleanly.

Do not create a default chain of repeated follow-ups.

## At course closure

Give the learner everything normally required to continue:

```text
support pack
retained-knowledge card
practice / tool route
source route
verification route
known boundary / referral route
next action
how to request help
```

This is part of the course itself.

It is not a later follow-up.

---

## One scheduled Return Window

When delayed Human Return or first real use matters, schedule **one** return window.

Timing is selected by the course designer according to how long learners need to encounter the capability in real life.

A common short-course window may be roughly one to two weeks, but this is an implementation example, not a universal rule.

Check only:

```text
USE
What did you actually use?

FRICTION
What became difficult, forgotten, or unclear?

RETURN
What can you now do / explain / verify with less help?

NEXT
Continue / Practise / Learn Next / Refer?
```

---

## Private delivery

```text
one short individual return conversation or task
```

---

## Group delivery

```text
one return session
+
one individual return trace per learner
```

Group discussion does not replace individual return.

---

## After that

Default:

```text
SELF-SERVICE MATERIALS
+
ON-DEMAND HELP
```

Do not proactively chase the learner through repeated 72-hour / 7-day / 14-day / 30-day contacts unless the programme itself requires longitudinal supervision.

Additional scheduled support must have an explicit reason such as:

```text
safety
supervised practice
credential requirement
longitudinal programme design
learner opt-in
```

---

# 29. Example Profile: 12-Hour Applied Course

This is a tangible default for a substantial short course.

It can be compressed or expanded.

---

## Hour 0 — Before class: Intake and readiness

**Not classroom time.**

### Learner

```text
submit intake
describe real problem
state prior attempts
run baseline task
check tool access
```

### Teacher

```text
read experiential capital
identify likely barriers
prepare differentiated scaffold options
```

### Tools

```text
Google Forms
Drive
Classroom / LMS
source-navigation pack
technical checklist
```

### Output

```text
Human Readout
Experiential Capital
initial Barrier hypotheses
```

---

## Hour 1 — The Live Problem

### Goal

Make the real problem visible before teaching the solution.

### Activity

```text
case / learner story
problem reconstruction
observed vs inferred sorting
timeline
constraints
```

### Teacher

```text
problem steward
diagnostic reader
```

### Tools

```text
Problem Card
whiteboard
sticky notes
shared Doc
```

### Learner output

`Problem Card v1`

### Evidence

Can the learner distinguish:

```text
facts
assumptions
unknowns
constraints
```

---

## Hour 2 — Change the Words, Change the Questions

### Goal

Show how terms and lenses alter reachable questions.

### Activity

```text
current term
→ alternative term
→ question rewrite
→ lens comparison
```

### Tools

```text
Working-Word Cards
ChatGPT Expand / Challenge
source-grounded navigation to check source meaning
```

### Teacher

```text
language bridge
fact-preservation guard
```

### Learner output

`Working-Words Map`

### Evidence

Did the new term:

```text
open a new question?
preserve important facts?
```

---

## Hour 3 — From Words to Routes

### Goal

Turn terms into actual practice systems.

### Activity

For each selected term:

```text
term
→ domain
→ tool
→ workflow
→ criterion
→ skill / role
```

### Tools

```text
route-map template
source-grounded navigation
ChatGPT route expansion
manuals
professional sources
```

### Teacher

```text
route-fit reviewer
```

### Learner output

`Route Map`

### Evidence

Can learner explain why the route is relevant?

---

## Hour 4 — Operational Language

### Goal

Teach the minimum language required to enter the tool and workflow.

### Activity

```text
manual scavenger hunt
label interface
match terms to workflow
identify criteria
identify failure / boundary terms
```

### Tools

```text
actual manual
NotebookLM
tool screenshot
H5P / card sorting
glossary sheet
```

### Teacher

```text
language bridge
```

### Learner output

`Operational-Language Sheet`

### Evidence

Not "Can you define the word?"

Ask:

```text
Can you use the word to make the next valid move?
```

---

## Hour 5 — Tool Modeling

### Goal

Make hidden operation and judgment visible.

### Activity

Teacher / practitioner demonstrates:

```text
input
action
decision point
check
error
output
```

while verbalizing reasoning.

### Tools

```text
actual tool
projector / screen share
worked example
screen recording
```

### Teacher

```text
modeler
```

### Learner output

annotated `Tool / Workflow Map`

### Evidence

Learner identifies:

```text
what happened
why
where a choice was made
how result was checked
```

---

## Hour 6 — Coached Practice

### Goal

Learner performs the workflow with support.

### Activity

```text
attempt
feedback
reattempt
```

### Tools

```text
actual tool
practice file
checklist
teacher coaching
```

### Teacher

```text
coach
```

### Learner output

`Practice Log 1`

### Evidence

Which steps are:

```text
independent
prompted
incorrect
not yet attempted
```

---

## Hour 7 — Articulation + Challenge

### Goal

Expose reasoning and find weak points.

### Activity

```text
learner explains workflow
peer asks why
AI challenge prompt
counterexample
false premise
failure case
```

### Tools

```text
ChatGPT Challenge mode
peer review sheet
failure cards
```

### Teacher

```text
opposition / discrimination facilitator
```

### Learner output

`Reasoning Trace`

### Evidence

Can learner state:

```text
criterion
assumption
failure condition
what would change the decision
```

---

## Hour 8 — Verification

### Goal

Move from candidate to warranted knowledge.

### Activity

```text
select a claim
choose independent check
verify
revise
```

### Tools

```text
primary source
manual
dataset
calculator
expert
official rule
```

### Teacher

```text
verification coach
```

### Learner output

`Verification Ledger`

### Evidence

Can learner distinguish:

```text
AI agreement
from
independent support
```

---

## Hour 9 — Reattempt With Less Help

### Goal

Test what is beginning to return to the learner.

### Activity

Same capability, but reduce one decisive support.

Examples:

```text
blank workflow
no worked example
tool remains
AI cannot perform decisive step
```

### Tools

```text
actual tool
reduced-support task
```

### Teacher

```text
observer / minimal scaffold
```

### Learner output

`Practice Log 2`

### Evidence

What survived?

---

## Hour 10 — Transfer / Changed Case

### Goal

Test whether the learner can adapt rather than copy.

### Activity

Change:

```text
surface details
format
constraints
error
stakeholder
input data
```

while preserving the underlying capability.

### Tools

```text
new case packet
simulation
branching scenario
new dataset
```

### Teacher

```text
transfer observer
```

### Learner output

`Transfer Record`

### Evidence

Can learner:

```text
recognize the relevant principle
choose the right tool/workflow
adapt
recognize a boundary
```

---

## Hour 11 — World / Expert Resistance

### Goal

Expose the route to resistance outside the learning dialogue.

### Activity

Possible:

```text
practitioner critique
client/user test
simulation
local rule check
real dataset
external reviewer
```

### Tools

```text
expert
rubric
official source
field environment
simulation
```

### Teacher

```text
world-bridge / safety governor
```

### Learner output

`World Feedback Record`

### Evidence

Does learner revise rather than defend automatically?

---

## Hour 12 — Human Return + Retained Knowledge + Next Plan

### Goal

Close the cycle and prepare the next one.

### Activity

Learner independently states / demonstrates:

```text
what now has a basis
what I can now do
when it applies
how I check
where I stop / refer
what I will do next
```

### Tools

```text
Human Return Card
Retained Knowledge Card
next-action planner
```

### Teacher

```text
assessor
boundary checker
next-cycle planner
```

### Output

```text
Human Return Record
Retained Knowledge Record
After-Course Action Plan
```

---

# 30. Other Duration Profiles

## 3-hour micro workshop

```text
Hour 1
Problem + Words + Route

Hour 2
Tool / Workflow + Guided Practice

Hour 3
Challenge / Verify + Human Return + Next Action
```

Use only for low-complexity targets.

---

## 6-hour intensive

```text
1 Problem / Context
2 Words / Route / Operational Language
3 Modeling / Tool / Workflow
4 Coached Practice
5 Challenge / Verify / Reattempt
6 Transfer / Human Return / Retention
```

---

## 24-hour programme

Double the practical core:

```text
more tool practice
more workflow variation
peer / group work
expert clinic
field encounter
multiple return cycles
```

Do not double lecture time.

---

# 31. The Hourly Lesson Card

Every hour must be printable as one card.

```text
HOUR / SEGMENT:

DELIVERY MODALITY:

LIVE PROBLEM LINK:

HUMAN CAPABILITY TARGET:

BARRIER BEING ADDRESSED:

OPERATIONAL WORDS:

TOOL:

WORKFLOW:

CRITERION / CHECK:

ACTIVITY:

TEACHER ROLE:

LEARNER ACTION:

SCAFFOLD:

ACTIVITY DEMAND:
    cognitive / literacy / stillness / movement / social / decision density

RHYTHM CHECK:
    what signal would trigger KEEP / SWITCH / MOVE / BREAK / RE-SCAFFOLD?

WHAT AI MAY DO:

WHAT AI MAY NOT DO:

EVIDENCE CREATED:

OUTPUT / ARTIFACT:

RETURN QUESTION:

NEXT-HOUR / NEXT-SEGMENT DEPENDENCY:

IF ASYNCHRONOUS:
    pause point / learner action / self-check / progression condition

SUPPORT IF LEARNER GETS STUCK:
```

If the designer cannot fill this card, the hour is not yet designed.

---

# 32. Tool-Function Matching Rules

Do not select technology because it is fashionable or because the curriculum was originally written around it.

Select the **abstract function first**, write the tool contract, then choose the current implementation.

```text
Need source-grounded orientation?
→ NotebookLM + curated sources

Need generative route expansion?
→ ChatGPT / generative AI

Need independent verification?
→ primary source / expert / data / experiment
not the same dialogue

Need retrieval check?
→ Forms / H5P / LMS quiz

Need tool capability?
→ actual tool

Need workflow judgment?
→ case / branching scenario / role-play

Need peer objection?
→ forum / workshop / structured peer review

Need delayed support?
→ LMS + scheduled task + mentor / office hour

Need Human Return?
→ reduced-help performance task

Need one-way orientation?
→ media + source navigation + self-check

Need one-way skill development?
→ media alone is insufficient;
   add learner action + practice + feedback + reattempt

Need online synchronous delivery?
→ live interaction tool + shared workspace + actual/simulated practice tool

Need blended delivery?
→ assign each learning function to the modality that carries it best
```

---

# 33. Current Example: Textbook / Reference Source

A textbook is not the curriculum.

Use it as one of several infrastructure pieces.

Good uses:

```text
conceptual explanation
stable terminology
worked examples
reference
background
```

Bad uses:

```text
chapter order automatically becomes learning order

all textbook content becomes mandatory

textbook definitions replace live problem framing
```

Course sequencing should follow:

```text
route-specific dependencies
```

not default chapter order unless they happen to align.

---

# 34. Current Example: NotebookLM

Use it for:

```text
source re-entry
questioning a bounded corpus
finding where a term appears
comparing two sources
generating study aids
revisiting source evidence after class
```

Do not use it for:

```text
declaring truth
replacing the primary source in high-stakes checking
replacing actual tool practice
replacing expert supervision where required
```

---

# 35. Current Example: ChatGPT / Generative AI

Use it for:

```text
route generation
reframing
alternative examples
challenge
simulation
practice cases
role-play
question generation
feedback drafts
```

Do not let it silently own:

```text
learner goal
final verification
decisive reasoning that the learner is meant to own
professional authorization
```

---

# 36. Current Example: Google Classroom / LMS

Use it to:

```text
sequence access
schedule materials
collect work
give feedback
release follow-up cases
host support information
track submissions
```

Course structure should mirror the trajectory, not merely weeks or file types.

---

# 37. Current Example: Google Forms / Lightweight Form Tool

Good for:

```text
intake
basic diagnostic
retrieval
short delayed check
feedback
self-report burden
support request
```

Not sufficient alone for:

```text
tool use
workflow execution
judgment
professional performance
Human Return
```

---

# 38. Current Example: H5P / Interactive Content

Good for:

```text
interactive demonstration
branching workflow
decision rehearsal
workflow ordering
failure-mode recognition
low-risk practice
```

Use actual tools when actual tool operation is the target.

---

# 39. Support Escalation Card

Every course should tell learners:

```text
IF I DON'T UNDERSTAND A TERM
→ source / NotebookLM / glossary

IF I DON'T UNDERSTAND THE CONCEPT
→ explanation / teacher

IF I KNOW IT BUT CANNOT USE THE TOOL
→ tool demo / coached practice

IF I CAN USE THE TOOL BUT CANNOT COMPLETE THE WORKFLOW
→ workflow map / coach

IF I CANNOT JUDGE WHETHER OUTPUT IS GOOD
→ criteria / verification support

IF THE TASK IS OUTSIDE MY SCOPE
→ refer / expert / institution
```

This turns support into part of learning rather than rescue after failure.

---

# 40. After-Course Action Plan

Every learner leaves with:

```text
NEXT REAL PROBLEM:

ONE CAPABILITY TO USE:

ONE TOOL / WORKFLOW TO PRACTISE:

ONE CHECKING ROUTE:

ONE KNOWN BOUNDARY:

ONE PERSON / EXPERT TO CONTACT:

ONE TRANSFER TASK:

DATE OF RETURN CHECK:

WHAT EVIDENCE I WILL BRING BACK:
```

---

# 41. Course Designer's Final Checklist

Before launch:

```text
[ ] live problem is real and legible

[ ] learner context / experiential capital collected

[ ] governance and safety checked

[ ] source pack curated

[ ] NotebookLM pack built if useful

[ ] candidate routes mapped

[ ] critical facts preserved across reframing

[ ] operational language extracted

[ ] delivery modality selected by function, not convenience alone

[ ] one-way / async segments have declared functions

[ ] passive media is not used as evidence of capability

[ ] learner action / self-check / artifact added where the target requires it

[ ] modality limitations and compensating design are explicit

[ ] tool available

[ ] workflow visible

[ ] criteria explicit

[ ] skill / role boundaries explicit

[ ] route dependencies mapped

[ ] hourly cards completed

[ ] actual learner action appears in every practical block

[ ] verification is not merely another AI answer

[ ] Human Return task is separate from polished artifact

[ ] transfer case prepared

[ ] world / practitioner resistance prepared where appropriate

[ ] before-course support ready

[ ] during-course escalation visible

[ ] ordinary support materials are handed over at course closure

[ ] one Return Window scheduled only if delayed return is relevant

[ ] repeated proactive follow-up has been removed unless explicitly justified

[ ] activity-demand profiles considered for major blocks

[ ] movement / mode-switch options prepared where useful

[ ] referral route exists

[ ] retained-knowledge card prepared

[ ] technical backup exists
```

---

# 42. Minimal Current Implementation Stack

A small organization can run UPCC without expensive infrastructure.

The following is only a **current example implementation**, not a required stack.

## Example minimal digital stack (2026)

```text
shared file repository
collaborative document editor
lightweight intake / quiz tool
course-delivery hub
source-grounded navigation system
generative route-exploration system
actual domain-practice tool
```

A present-day implementation might use:

```text
Google Drive
Google Docs
Google Forms
Google Classroom or another LMS
NotebookLM
ChatGPT / another capable generative AI
actual domain tool
```

## Add if needed

```text
H5P
Moodle
video recording
screen recording
simulation software
data tools
physical equipment
expert / practitioner sessions
```

The most important "tool" is always the **actual tool of practice**.

A curriculum about spreadsheets needs spreadsheets.

A curriculum about interviewing needs interviews.

A curriculum about microscopy needs microscopes or a defensible simulation.

A curriculum about negotiation needs interactive negotiation.

---

# 43. Final Course-Production Rule

A curriculum is not complete when all slides are finished.

It is complete when the designer can trace:

```text
problem
→ word
→ question
→ route
→ operational language
→ tool
→ workflow
→ criterion
→ skill / role
→ scaffold
→ practice
→ verification
→ Human Return
→ transfer
→ world feedback
→ retained knowledge
→ next action
```

and can answer for **every hour**:

> What is the learner doing?

> With what tool?

> Using what language?

> Following what workflow?

> Judged by what criterion?

> Supported by whom?

> Producing what evidence?

> What changes in the learner if this hour works?

---

**End of UPCC Curriculum Production System v1.3**
