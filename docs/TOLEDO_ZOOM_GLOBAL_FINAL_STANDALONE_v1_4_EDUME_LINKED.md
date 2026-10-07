# TOLEDO-ZOOM GLOBAL CAUSAL-PREDICTIVE SPEC — EDUME-LINKED FINAL STANDALONE
## Machine-Readable Specification for Synchronous Group Videoconference Learning

```yaml
document:
  id: TOLEDO-ZOOM-GLOBAL-FINAL-STANDALONE-HCA-TESTED
  version: 1.4-edume-linked-canonical-weld
  status: GLOBAL_RESEARCH_GRADE_SPECIFICATION
  class:
    - machine_readable_pseudo_dag
    - evidence_calibrated_framework
    - prediction_specification
    - causal_intervention_specification
  scope: >
    Synchronous group videoconference learning through Zoom, Microsoft Teams,
    Google Meet, Webex, or equivalent systems, across candidate deployment
    domains including schools, higher education, professional training,
    workplace learning, adult learning, community education, language learning,
    values/religious education, and public/nonprofit training.
  standalone: true
  parent_required: false
  external_file_required: false
  canonical_anchor_preserved: true
  problem_coverage: 94_of_94
  empirical_status:
    global_literature_calibrated: true
    external_dataset_backed_replay: true
    raw_row_independent_replication: not_yet_completed
    universal_numeric_fit: false
    universal_causal_validation: false
```


---

# EDUME / UPCC INTEGRATION STATUS — 2026-10-07

This document is the synchronous-group-videoconference domain specification consumed by
`morrocwi/EduMe` when a UPCC curriculum uses `ONLINE_SYNCHRONOUS` delivery.

The central Zoom→Human-Capability composition in §44AC is no longer only a local proposal.
It has been admitted to the Toledo canonical registry as:

- **Code:** `EQ-002/H.07.v1`
- **Internal id:** `CAN-1318`
- **Status:** `current`
- **Tier:** `Definition`

Canonical registered composition:

[
oxed{
Z^{Zoom}_{igt}
\xrightarrow{q_B}
B^{bar}_{i,t}
\xrightarrow{u^*_{diag}}
C^{cand}_{i,t}
\xrightarrow{Endorse_i}
C^{live}_{i,t}
\xrightarrow{\pi^*_{scaffold}}
R^{return}_{H,i,t+1}
\xrightarrow{Retention}
\Delta H_{i,t+1}
\xrightarrow{LiveField}
L_{H,i,t+1}
\xrightarrow{G_O}
\Omega^{real}_{i,t+1}
\xrightarrow{Record}
A^{HCA}_{i,t+1}
}
]

The old local label `PROP-ZHCA-MASTER-01` is retained only as lineage/provenance for this
document. **It must not be treated as a second equation.**

Relationship to UPCC:

```text
TOLEDO-ZOOM state/readout layer
    |
    |  EQ-002/H.07.v1  (canonical delivery-domain weld)
    v
Toledo HCA river / EQ-002/H.03.v1 (CAN-098)
    |
    |  EduMe / UPCC curriculum specialization
    v
Live Problem
→ Barrier Readout
→ Candidate Routes
→ Human Endorsement
→ Adaptive Scaffold
→ Practice
→ Withdrawal
→ Human Return
→ Novel Transfer
→ World Feedback
→ Opportunity Conversion
```

Continuity rule:

[
oxed{
ONLINE_SYNCHRONOUS
\Rightarrow
Readout_{Zoom}
\xrightarrow{EQ-002/H.07.v1}
HCA
\xrightarrow{UPCC}
Curriculum Operations
}
]

This does **not** make every equation in this standalone canonical. Unless explicitly identified
as a registered Toledo object, the prediction, measurement, intervention, and empirical
specializations below retain their stated `DERIVED_PROPOSAL` / empirical status.

---

# 0. AI BOOT INSTRUCTIONS

Any AI using this file MUST execute these rules before reasoning:

```yaml
boot_rules:

  epistemic_classes:
    CANONICAL_TOLEDO:
      meaning: registered Toledo equation/object
      may_modify: false

    DERIVED_PROPOSAL:
      meaning: domain specialization proposed in this specification
      may_present_as_validated_law: false

    EMPIRICAL_PRIOR:
      meaning: effect information from published empirical literature
      may_use_as_local_coefficient_directly: false

    LOCAL_PARAMETER:
      meaning: parameter estimated in a declared target dataset
      may_transport_without_validation: false

    CAUSAL_EFFECT:
      meaning: intervention effect identified under declared assumptions/design
      requires_identification_gate: true

  mandatory_noncollapse:
    - observable_trace_ne_latent_state
    - connection_ne_attendance
    - attendance_ne_participation
    - participation_ne_understanding
    - understanding_ne_retention
    - retention_ne_application
    - prediction_ne_causation
    - measurement_invariance_ne_path_equality
    - resources_ne_access
    - access_ne_capability
    - capability_ne_realized_opportunity
    - assisted_performance_ne_unaided_human_return

  prohibited:
    - invent_numeric_coefficients
    - use_meta_analytic_r_as_local_beta_without_scale_bridge
    - use_camera_state_as_engagement_label
    - use_attendance_as_learning_label
    - assign_one_global_problem_score
    - claim_universal_optimal_camera_policy
    - claim_universal_optimal_breakout_policy
    - claim_universal_optimal_session_duration
    - output_individual_probability_without_validated_local_model
```

---

# 1. ORIGINAL ANCHOR — NEVER REPLACE

\[
\boxed{
Z^{anchor}
=
\langle
A,M,C,B,R,J,P,V,D,I
\rangle
}
\tag{ANCHOR-01}
\]

```yaml
anchor:

  A:
    label: Access
    includes:
      - device
      - connectivity
      - electricity
      - learning_space
      - shared_device
      - digital_skill

  M:
    label: Mediation
    includes:
      - latency
      - bandwidth_state
      - audio_video_quality
      - interface_constraint
      - cue_loss

  C:
    label: Cognitive_Regulation
    includes:
      - attention
      - cognitive_load
      - task_switching
      - working_memory_demand

  B:
    label: Bodily_Affective_Burden
    includes:
      - fatigue
      - visual_strain
      - discomfort
      - anxiety
      - stress

  R:
    label: Relational_Group
    includes:
      - social_presence
      - trust
      - cohesion
      - belonging
      - peer_help
      - coordination

  J:
    label: Teacher_Orchestration
    includes:
      - teaching_presence
      - facilitation
      - feedback
      - technical_orchestration
      - workload
      - technostress

  P:
    label: Pedagogical_Translation
    includes:
      - course_structure
      - activity_design
      - practice
      - feedback_design
      - assessment_design
      - online_translation_loss

  V:
    label: Verification_Ambiguity
    includes:
      - identity_uncertainty
      - participation_uncertainty
      - authorship_uncertainty
      - understanding_uncertainty

  D:
    label: Data_Privacy
    includes:
      - recording
      - camera_exposure
      - identity_data
      - chat_retention
      - access_control

  I:
    label: Structural_Inequality
    includes:
      - socioeconomic_context
      - household_context
      - geography
      - language
      - disability
      - culture
```

Interpretation:

> The ten-domain Anchor is the global problem field. It is not a learner-state vector, not a causal graph by itself, and not a score to sum.

---

# 2. TOLEDO CANONICAL ANCHORS

The following equations are treated as existing Toledo canonical anchors.

## CAN-002 — Root state

\[
\boxed{
S_n=(G_n,\Lambda_n,T_n)
}
\]

## CAN-003 — State transition

\[
\boxed{
S_{n+1}=F(S_n,u_n,c_n,T_n)
}
\]

## CAN-006 — Domain weld

\[
\boxed{
q_{D,n+1}\circ F_n
=
F^\#_{D,n}\circ q_{D,n}
}
\]

Equivalent:

\[
\boxed{
q_D(F(z,u,c,T))
=
F_D(q_D(z),u,c,T)
}
\]

## CAN-007 — Finite-horizon reader equivalence

\[
\boxed{
z\sim_{Q,O,c,L}z'
\iff
O(F^kz)=O(F^kz')
\quad \forall k\le L
}
\]

## CAN-059 — Observation non-collapse

\[
\boxed{
Y_{obs}=O_q(H_{0:T})\neq H_{0:T}
}
\]

## CAN-074 — Assisted performance non-collapse

\[
\boxed{
\Delta Performance_{AI}>0
\not\Rightarrow
\Delta H_{return}>0
}
\]

## CAN-075 — Exposure/retention/improvement non-collapse

\[
\boxed{
Exposure\neq Retention\neq Improvement
}
\]

All education-specific equations below are `DERIVED_PROPOSAL` unless explicitly labeled otherwise.

---

# 3. INDEXING

```yaml
indices:
  i: learner
  g: group_or_class
  j: instructor_or_facilitator
  o: organization_or_institution
  d: deployment_domain
  t: time_or_session_step
  h: prediction_horizon
  k: outcome_type
```

---

# 4. MODEL RECLASSIFICATION

```yaml
reclassification:

  structural_context:
    object: K_i
    anchor_sources: [A, I]

  session_instruction_input:
    object: U_g_t
    anchor_sources: [J, P]
    auxiliary: L_g_t

  mediation_state:
    object: M_i_g_t
    anchor_sources: [M]

  learner_dynamic_state:
    object: X_i_g_t
    anchor_sources: [C, B]
    added_latents: [E, S_enact]

  group_dynamic_state:
    object: G_g_t
    anchor_sources: [R]
    added_latents: [Trust, Cohesion, Coordination]

  teacher_dynamic_state:
    object: H_j_g_t
    anchor_sources: [J]

  organization_context:
    object: N_o_t
    anchor_sources: [I, J, P]

  observation:
    object: O_i_g_t

  verification_uncertainty:
    object: V_i_g_t
    anchor_sources: [V]

  privacy_governance:
    objects: [D_obj_i_g_t, D_perc_i_g_t]
    anchor_sources: [D]

  outcome:
    object: Y_i_g_t_h_k
```

---

# 5. STATE DEFINITIONS

## 5.1 Structural context

\[
\boxed{
K_i=
\langle
A_i,I_i,S_i^{base},Q_i
\rangle
}
\]

where auxiliary stable context is:

\[
\boxed{
Q_i=
\langle
PriorExperience,
BaselineBurden,
StableTraitContext,
AgeRelatedContext
\rangle_i
}
\]

`Q_i` is not an eleventh Anchor dimension.

Protected or sensitive attributes should normally be used for:
- fairness auditing;
- calibration checks;
- effect-modification research;

not as automatic punitive risk weights.

---

## 5.2 Session / instruction input

\[
\boxed{
U_{gt}
=
\langle
J^+_{gt},
J^-_{gt},
P^+_{gt},
P^-_{gt},
L_{gt}
\rangle
}
\]

```yaml
J_plus:
  - teaching_presence
  - facilitation
  - feedback
  - instructional_clarity

J_minus:
  - technical_overload
  - orchestration_burden
  - technostress

P_plus:
  - clear_structure
  - authentic_activity
  - suitable_assessment
  - feedback_design

P_minus:
  - activity_translation_loss
  - practical_skill_representation_failure
  - superficial_online_substitution

L_g_t:
  - duration
  - group_size
  - camera_policy
  - breakout_configuration
  - lecture_activity_ratio
  - break_pattern
  - interaction_requirement
  - task_complexity
```

---

## 5.3 Medium state

\[
\boxed{
M_{igt}
=
\langle
Latency,
Bandwidth,
Audio,
Video,
Interface,
CueLoss
\rangle_{igt}
}
\]

---

## 5.4 Learner dynamic state

\[
\boxed{
X_{igt}
=
\langle
C_{igt},
B_{igt},
E_{igt},
S^{enact}_{igt}
\rangle
}
\]

where:

```yaml
C:
  - attention
  - cognitive_load
  - task_switching
  - working_memory_demand

B:
  - fatigue
  - visual_strain
  - physical_discomfort
  - anxiety
  - stress

E:
  - behavioral_engagement
  - cognitive_engagement
  - emotional_engagement

S_enact:
  - effort_regulation
  - distraction_control
  - metacognitive_monitoring
  - task_management
```

---

## 5.5 Group state

\[
\boxed{
G_{gt}
=
\langle
R^+_{gt},
R^-_{gt},
Trust_{gt},
Cohesion_{gt},
Coordination_{gt}
\rangle
}
\]

```yaml
R_plus:
  - social_presence
  - belonging
  - peer_help
  - trust_resource

R_minus:
  - silence
  - turn_taking_friction
  - free_riding
  - social_anxiety
  - coordination_failure
```

---

## 5.6 Teacher state

\[
\boxed{
H_{jgt}
=
\langle
Presence,
Capacity,
Workload,
TechStress
\rangle_{jgt}
}
\]

---

## 5.7 Organization state

\[
\boxed{
N_{ot}
=
\langle
Infrastructure,
Support,
Policy,
QA,
Staffing
\rangle_{ot}
}
\]

---

# 6. DYNAMIC EQUATIONS

## 6.1 Learner transition

\[
\boxed{
X_{ig,t+1}
=
f_\theta
(
X_{igt},
G_{gt},
H_{jgt},
M_{igt},
U_{gt},
K_i,
N_{ot},
T_t
)
+
\varepsilon_{igt}
}
\tag{PROP-DYN-X}
\]

## 6.2 Group transition

Use a distribution, not only a mean:

\[
\mathcal D(X_{gt})
=
\langle
Mean,
Variance,
TailRisk,
ParticipationInequality
\rangle
\]

Then:

\[
\boxed{
G_{g,t+1}
=
h_\phi
(
G_{gt},
\mathcal D(X_{gt}),
Net_{gt},
U_{gt},
\mathcal D(M_{gt}),
N_{ot},
T_t
)
+
\eta_{gt}
}
\tag{PROP-DYN-G}
\]

## 6.3 Teacher transition

\[
\boxed{
H_{jg,t+1}
=
q(
H_{jgt},
U_{gt},
M_{gt},
GroupDemand_{gt},
N_{ot}
)
+
\xi_{jgt}
}
\tag{PROP-DYN-H}
\]

---

# 7. EMPIRICALLY REFINED FATIGUE SUBMODEL

External dataset-backed studies strengthened this submodel.

\[
\boxed{
B_{t+1}
=
\rho_iB_t
+
\lambda_{NV}L^{NV}_t
+
\lambda_{COMM}L^{COMM}_t
+
\lambda_{INFO}L^{INFO}_t
+
\lambda_{TECH}L^{TECH}_t
+
\lambda_{TASK}L^{TASK}_t
-
Recovery_t
+
\epsilon_t
}
\tag{PROP-BURDEN-EMP}
\]

```yaml
load_channels:

  L_NV:
    - mirror_anxiety
    - hyper_gaze
    - movement_constraint
    - nonverbal_production
    - nonverbal_interpretation

  L_COMM:
    - communication_overload

  L_INFO:
    - information_overload

  L_TECH:
    - connection_failure
    - interface_disruption

  L_TASK:
    - task_complexity
    - simultaneous_channel_demand
```

Association-supported serial candidate:

\[
\boxed{
L^{COMM}_t
\rightarrow
L^{INFO}_t
\rightarrow
B_{t+h}
}
\]

plus:

\[
\boxed{
L^{COMM}_t
\rightarrow
B_{t+h}
}
\]

Status: `ASSOCIATION_SUPPORTED_NOT_UNIVERSAL_CAUSAL`.

---

# 8. ACCESS HURDLE

## 8.1 Entry

\[
\boxed{
Pr(ENTER_{igt}=1)
=
g_A(K_i,U_{gt},N_{ot})
}
\]

## 8.2 Meaningful participation after entry

\[
\boxed{
Pr(EffectiveParticipation=1\mid ENTER=1)
=
g_E(X,G,M,U,K)
}
\]

## 8.3 Learning conditional on entry

\[
\boxed{
Pr(Y^{(k)}_{ig,t+h}=1\mid ENTER=1)
=
f_k(X,G,H,M,U,K,N,\mathcal H_t)
}
\]

AI MUST declare whether the estimand refers to:
- actual entrants;
- all eligible learners;
- a principal stratum;
- a transported target population.

Conditioning on `ENTER=1` can induce selection bias.

---

# 9. OBSERVATION AND VERIFICATION MODEL

Observable traces:

\[
O_{igt}
\]

may include:
- login/logout;
- camera state;
- microphone state;
- chat;
- poll;
- speech turn;
- breakout entry;
- quiz response;
- assignment submission;
- reconnect event.

Measurement equation:

\[
\boxed{
O_{igt}
\sim
p_\psi(
O\mid
X_{igt},G_{gt},M_{igt},U_{gt},K_i
)
}
\tag{PROP-OBS}
\]

Verification uncertainty:

\[
\boxed{
V_{igt}
=
\mathcal U
(
X_{igt}
\mid
O_{\le t},K_i,U_{\le t},M_{\le t},G_{\le t}
)
}
\tag{PROP-VERIFY}
\]

Hard rule:

\[
\boxed{
O_t\neq X_t
}
\]

and:

\[
\boxed{
O_t\neq G_t
}
\]

---

# 10. NON-COLLAPSE LEARNING CHAIN

\[
\boxed{
Connection
\neq
Attendance
\neq
Participation
\neq
Understanding
\neq
Retention
\neq
Application
}
\tag{PROP-NONCOLLAPSE}
\]

Forbidden implications:

\[
Connection\not\Rightarrow Attention
\]

\[
Attendance\not\Rightarrow Engagement
\]

\[
Engagement\not\Rightarrow Understanding
\]

\[
Understanding\not\Rightarrow Retention
\]

\[
Retention\not\Rightarrow Application
\]

---

# 11. PRIVACY / GOVERNANCE SPLIT

Objective privacy/data risk:

\[
\boxed{
D^{obj}_{igt}
=
d(
Capture,
Retention,
Exposure,
AccessControl,
Purpose
)
}
\]

Perceived privacy threat:

\[
\boxed{
D^{perc}_{igt}
=
PerceivedPrivacyThreat_{igt}
}
\]

Candidate paths:

\[
D^{perc}\rightarrow B
\]

\[
D^{perc}\rightarrow O^{camera}
\]

`D_obj` is primarily a governance outcome and MUST NOT be collapsed into learning performance.

---

# 12. CAMERA POLICY

Camera is not a universal positive or negative treatment.

\[
CameraPolicy
\rightarrow
\begin{cases}
R^+ & \text{social presence/accountability}\\
B & \text{fatigue/self-consciousness}\\
D^{perc} & \text{privacy threat}\\
M & \text{bandwidth demand}\\
O & \text{observation quality}
\end{cases}
\]

\[
\boxed{
Effect(Camera)
=
f(
Agency,
Bandwidth,
Privacy,
SocialPresence,
Task,
Learner,
Context
)
}
\]

Direct learning prior: `zero_centered_broad`.

---

# 13. BREAKOUT ROOM MODEL

Do not model `breakout=yes/no` as a universal treatment.

\[
\boxed{
BreakoutBundle
=
\langle
GroupSize,
TaskStructure,
RoleClarity,
Time,
TeacherMonitoring,
Cohesion
\rangle
}
\]

Candidate effect:

\[
\boxed{
Effect(Breakout)
=
f(
TaskStructure,
Cohesion,
GroupSize,
RoleClarity,TeacherMonitoring,
Time,
LearnerAttributes
)
}
\]

---

# 14. PEDAGOGICAL TRANSLATION TEST

For physical/on-site activity \(a\) and online translation \(\tau_Z(a)\):

\[
\boxed{
a
\overset{?}{\sim}_{Q,O,c,L}
\tau_Z(a)
}
\]

Candidate specialization of Toledo CAN-007.

Required fields:

```yaml
translation_test:
  - source_activity
  - translated_activity
  - state_space
  - learning_readout
  - invariant_to_preserve
  - finite_horizon
  - context
  - acceptance_rule
```

If incomplete: `UNRESOLVED`.

---

# 15. OUTCOME VECTOR

Do not use one global problem score.

\[
\boxed{
Y_{ig,t+h}
=
\begin{bmatrix}
Y^{access}\\
Y^{technical}\\
Y^{engagement}\\
Y^{fatigue}\\
Y^{social}\\
Y^{comprehension}\\
Y^{learning}\\
Y^{completion}\\
Y^{verification}\\
Y^{privacy}
\end{bmatrix}
}
\]

Actual learning, perceived learning, satisfaction, retention, and practical performance MUST remain distinct outcomes.

---

# 16. PREDICTIVE EQUATION

For binary outcome \(k\):

\[
\boxed{
\begin{aligned}
\operatorname{logit}
P(Y^{(k)}_{ig,t+h}=1)
=&\;
\alpha^{(k)}_{country,org,course}
+b^{(k)}_i
+c^{(k)}_g
+d^{(k)}_j\\
&+\beta_k^\top X_{igt}
+\gamma_k^\top G_{gt}
+\chi_k^\top H_{jgt}\\
&+\delta_k^\top U_{gt}
+\mu_k^\top M_{igt}
+\zeta_k^\top K_i\\
&+\nu_k^\top N_{ot}
+\Omega_k
\end{aligned}
}
\tag{PROP-PREDICT}
\]

`Ω_k` contains prespecified interactions/nonlinear terms.

All numerical coefficients are empirical parameters.

---

# 17. REQUIRED CANDIDATE INTERACTIONS

```yaml
candidate_interactions:
  - bandwidth_x_camera_policy
  - privacy_threat_x_camera_policy
  - cohesion_x_breakout
  - task_structure_x_breakout
  - teacher_presence_x_low_self_regulation
  - session_duration_x_prior_fatigue
  - digital_skill_x_interface_complexity
  - group_size_x_social_presence
  - device_type_x_task_type
  - language_fluency_x_turn_taking_demand
```

Do not assume all are nonzero.

---

# 18. EMPIRICAL DOSE GUARDRAIL

External dataset-backed replay rejected simplistic universal dose edges.

```yaml
dose_guardrail:

  prohibit:
    - duration_positive_to_all_overload
    - frequency_positive_to_all_overload

  allow:
    - path_specific_effect
    - context_specific_effect
    - nonlinear_effect
    - interaction_with_task_and_role
```

---

# 19. GLOBAL EVIDENCE PRIOR REGISTRY

Published effect sizes below are evidence anchors, not local model coefficients.

```yaml
global_numeric_evidence:

  synchronous_webinar_meta:
    design: randomized_controlled_meta_analysis
    k: 31
    N: 3823
    affective_g_approx: 0.24
    cognitive_g_approx: 0.49_to_0.50
    use: modality_is_not_intrinsically_negative

  teaching_presence_meta:
    perceived_learning_r: 0.602
    satisfaction_r: 0.590
    heterogeneity_I2_percent:
      perceived_learning: 96.24
      satisfaction: 95.31
    use: positive_direction_high_transport_variance

  social_presence_meta:
    satisfaction_r: 0.56
    perceived_learning_r: 0.51
    heterogeneity_I2_percent:
      satisfaction: 86.7
      perceived_learning: 92.8

  self_regulation_meta:
    studies: 42
    N: 11014
    performance_r: 0.14
    use: positive_but_small_direct_performance_prior

  digital_literacy_SRL_meta:
    studies: 31
    r: 0.37

  designed_interaction_meta:
    designed_g: 0.52
    contextual_g: 0.11
    use: tool_presence_ne_designed_interaction

  videoconference_fatigue_meta:
    studies: 38
    psychological_r: 0.24
    feeling_trapped_r: 0.33
```

---

# 20. EXTERNAL DATASET-BACKED STRESS TEST REGISTRY

These datasets were publicly archived and used for evidence replay against pre-existing model implications.

```yaml
external_dataset_registry:

  D1:
    topic: videoconference_fatigue_nonverbal_overload
    sample_N: 9787
    public_archive: OSF
    key_results:
      model_R2: 0.34
      mirror_anxiety_beta: 0.18
      physically_trapped_beta: 0.24
      hyper_gaze_beta: 0.14
      nonverbal_production_beta: 0.07
      nonverbal_interpretation_beta: 0.07
    model_implication:
      - supports_dynamic_B
      - supports_nonverbal_load_channels

  D2_student:
    topic: communication_information_overload_fatigue
    sample_N: 489
    public_archive: Figshare
    paths:
      frequency_to_communication_beta: 0.09
      length_to_communication_beta: -0.02
      communication_to_fatigue_beta: 0.44
      frequency_to_information_beta: 0.01
      length_to_information_beta: 0.04
      communication_to_information_beta: 0.69
      information_to_fatigue_beta: 0.28

  D2_singapore:
    sample_N: 610
    paths:
      frequency_to_communication_beta: 0.13
      length_to_communication_beta: 0.05
      communication_to_fatigue_beta: 0.56
      frequency_to_information_beta: -0.07
      length_to_information_beta: 0.01
      communication_to_information_beta: 0.85
      information_to_fatigue_beta: 0.23

  D2_germany:
    sample_N: 948
    paths:
      frequency_to_communication_beta: 0.20
      length_to_communication_beta: -0.01
      communication_to_fatigue_beta: 0.31
      frequency_to_information_beta: -0.02
      length_to_information_beta: -0.08
      communication_to_information_beta: 0.91
      information_to_fatigue_beta: 0.36

  D2_cross_country:
    measurement_invariance: weak_metric_supported
    equal_structural_paths_rejected:
      chi_square_difference: 541.40
      p: "<0.001"
    implication:
      - measurement_compatibility_ne_path_equality
      - country_path_deviations_required

  D3:
    topic: temporal_learning_analytics_CoI
    public_archive: Zenodo
    learners: 72
    traces: 4276
    implication:
      - supports_time_indexing
      - supports_lagged_processes
      - supports_behavior_trace_as_proxy_not_latent_state

  D4:
    topic: blended_learning_multiconstruct_measurement
    public_archive: Mendeley_Data
    raw_N: 580
    cleaned_N: 436
    constructs: 7
    implication:
      - supports_construct_separation
      - suitable_for_future_measurement_SEM_testing
```

Important:

> `external_dataset_backed_replay = true` does not mean the raw rows were independently refitted in this specification.

---

# 21. META-ANALYTIC PRIOR BRIDGE

A meta-analytic association can be used numerically only when constructs, outcomes, comparators, and effect scales are compatible.

```yaml
prior_scale_bridge:
  require:
    - same_or_justifiably_mapped_construct
    - same_or_compatible_outcome
    - same_or_compatible_comparator
    - same_effect_scale_or_declared_conversion
    - measurement_compatibility

  if_any_fail:
    use_as: structural_direction_only
    numeric_prior: prohibited
```

For a correlation prior:

\[
z=\tanh^{-1}(r)
\]

A robust local prior may be:

\[
\boxed{
z_e^{local}
\sim
\mathcal N
(
z_e^{meta},
SE_{meta,e}^2+\tau_{transport,e}^2
)
}
\]

only when the target parameter is commensurate.

---

# 22. MEASUREMENT INVARIANCE

For deployment domain \(d\):

\[
\boxed{
O^{scale}_{i,d}
=
\Lambda_dX_{i,d}
+
\nu_d
+
\epsilon_{i,d}
}
\]

Required:

```yaml
measurement_invariance:

  configural:
    required_for:
      - same_factor_structure_claim

  metric:
    required_for:
      - regression_path_comparison
      - latent_relationship_transport

  scalar_or_partial_scalar:
    required_for:
      - latent_mean_comparison
      - threshold_comparison

  if_failed:
    - fit_group_specific_measurement_models
    - prohibit_naive_mean_comparison
    - widen_transport_uncertainty
```

Empirical guardrail:

\[
\boxed{
MeasurementInvariance
\not\Rightarrow
StructuralPathEquality
}
\]

---

# 23. LATENT-STATE IDENTIFICATION

```yaml
latent_identification:
  require:
    - construct_definition
    - minimum_indicators
    - scale_anchor_or_constraint
    - discriminant_validity
    - longitudinal_measurement_plan_if_dynamic
    - invariance_check_if_cross_group
```

No single platform trace may equal a latent construct by default.

---

# 24. STATISTICAL TRANSPORTABILITY

For edge \(e\) in deployment domain \(d\):

\[
\boxed{
\theta_{e,d}
=
\theta_{e,global}
+
u_{e,country}
+
u_{e,institution}
+
u_{e,course}
+
u_{e,language}
+
u_{e,population}
+
u_{e,platform}
}
\tag{PROP-TRANSPORT-STAT}
\]

This is partial pooling, not a causal transport theorem.

---

# 25. CAUSAL TRANSPORTABILITY GATE

```yaml
causal_transport_gate:
  require:
    - source_population_defined
    - target_population_defined
    - treatment_version_compatible
    - outcome_measurement_compatible
    - effect_modifiers_declared
    - source_target_overlap_checked
    - positivity_checked
    - selection_mechanism_considered
    - sensitivity_analysis

  if_no_overlap:
    causal_transport: prohibited

  if_measurement_incompatible:
    numeric_transport: prohibited
```

---

# 26. INTERVENTION ACTION SPACE

\[
\boxed{
a_t\in\mathcal A
}
\]

```yaml
intervention_space:

  a_access:
    - device_support
    - low_bandwidth_mode
    - alternate_schedule
    - mobile_safe_material
    - reconnection_path

  a_medium:
    - camera_policy_change
    - hide_self_view
    - interface_simplification
    - explicit_turn_taking
    - screen_rest_pattern

  a_learner:
    - orientation
    - self_regulation_scaffold
    - recovery_break
    - notification_control
    - targeted_help

  a_group:
    - stable_grouping
    - role_assignment
    - breakout_task_structure
    - peer_support
    - participation_rotation
    - group_size_change

  a_teacher:
    - technical_host
    - co_facilitator
    - rehearsal
    - teacher_training
    - workload_reduction

  a_pedagogy:
    - online_native_redesign
    - worked_example
    - comprehension_checkpoint
    - formative_feedback
    - practical_hybrid_component
    - spaced_follow_up

  a_governance:
    - data_minimization
    - minimal_identity_verification
    - recording_policy
    - retention_deletion_rule
    - access_control
    - quality_assurance_protocol

  a_organization:
    - staffing
    - infrastructure_support
    - accessibility_service
    - interpretation_service
    - help_desk
```

---

# 27. CAUSAL ESTIMANDS

Potential outcome:

\[
\boxed{
Y^{(k)}_{ig,t+h}(a)
}
\]

Average treatment effect:

\[
\boxed{
ATE_k(a,a_0)
=
E[Y^{(k)}(a)]
-
E[Y^{(k)}(a_0)]
}
\]

Conditional effect:

\[
\boxed{
CATE_k(a,a_0\mid K_i,X_t,G_t)
=
E[Y^{(k)}(a)-Y^{(k)}(a_0)\mid K_i,X_t,G_t]
}
\]

Do not report an individualized effect unless the design/data support it.

---

# 28. GROUP INTERFERENCE

Define interference set:

\[
\boxed{
\mathcal N_i(t)
=
\{\text{units allowed to affect learner }i\text{ at }t\}
}
\]

Exposure mapping:

\[
\boxed{
E_i(t)
=
g(
\mathbf a_{\mathcal N_i(t)},
Net_t
)
}
\]

Group outcome may be:

\[
\boxed{
Y_i(a_i,\mathbf a_{-i},G)
}
\]

Required:

```yaml
interference_contract:
  - interference_set
  - exposure_mapping
  - group_membership_history
  - breakout_membership_if_relevant
  - network_measurement_sensitivity
```

---

# 29. DYNAMIC INTERVENTION GATE

For adaptive policy:

\[
\boxed{
\pi_t(a\mid\mathcal H_t)
}
\]

Required causal assumptions:

\[
Consistency
\]

\[
Sequential\ Exchangeability
\]

\[
Positivity
\]

\[
No\ Future\ Information\ Leakage
\]

If treatment is adaptive, ordinary regression is not automatically a valid causal estimator.

Candidate designs/methods:
- micro-randomized trial;
- SMART;
- marginal structural model;
- longitudinal g-formula;
- structural nested model;
- longitudinal TMLE;
- doubly robust longitudinal estimation.

---

# 30. MULTI-OBJECTIVE SOLUTION SELECTION

Do not collapse learning, fatigue, privacy, workload, inequality, and cost without explicit stakeholder weights.

\[
\boxed{
\mathcal U(a)
=
\langle
\Delta Learning,
-\Delta Fatigue,
-\Delta PrivacyRisk,
-\Delta TeacherBurden,
-\Delta Inequality,
-\Delta Cost
\rangle
}
\]

Dominance:

\[
a'\succ a
\iff
U_j(a')\ge U_j(a)\ \forall j
\quad\text{and}\quad
U_j(a')>U_j(a)
\text{ for at least one }j
\]

Pareto set:

\[
\boxed{
\mathcal A^{Pareto}
=
\left\{
a:
\nexists a'\text{ such that }a'\succ a
\right\}
}
\]

---

# 31. SAMPLE-SIZE / COMPLEXITY GATE

```yaml
sample_size_gate:
  required_before_fit: true

  account_for:
    - outcome_frequency_or_variance
    - number_of_candidate_parameters
    - nonlinear_terms
    - interactions
    - random_effects
    - clustering
    - repeated_measurements
    - missingness
    - shrinkage_strategy

  if_insufficient:
    - simplify_model
    - shrink_parameters
    - pool_levels
    - reduce_interactions
    - prohibit_operational_prediction
```

Do not use a universal events-per-variable shortcut.

---

# 32. MISSING-DATA ENGINE

\[
\boxed{
Missing\not\perp ProblemRisk
}
\]

```yaml
missing_data_engine:

  diagnose:
    - missingness_by_time
    - missingness_by_access
    - missingness_by_group
    - dropout_reason
    - missingness_after_intervention

  candidate_methods:
    - multiple_imputation_if_MAR_plausible
    - inverse_probability_of_observation_weighting
    - joint_longitudinal_dropout_model

  MNAR_sensitivity:
    - pattern_mixture
    - delta_adjustment
    - selection_model

  prohibited:
    - complete_case_analysis_by_default
```

---

# 33. MULTIPLICITY

```yaml
multiplicity_contract:

  confirmatory:
    require:
      - preregister_primary_outcome
      - preregister_primary_estimand
      - preregister_primary_intervention

  exploratory:
    label: exploratory

  control:
    choose_as_appropriate:
      - familywise_error_control
      - false_discovery_rate
      - hierarchical_testing
```

---

# 34. FAIRNESS

```yaml
fairness_contract:

  report_by_relevant_group:
    - calibration_intercept
    - calibration_slope
    - false_positive_rate_if_action_triggered
    - false_negative_rate_if_action_triggered
    - missingness_rate
    - intervention_access
    - adverse_effect_rate

  prohibited:
    - camera_off_as_negative_label
    - protected_or_proxy_feature_as_penalty_without_justification

  note:
    - fairness_metric_must_match_decision_and_harm
```

---

# 35. PLATFORM SCOPE

```yaml
platform_general:
  - synchronous_latency
  - mediated_presence
  - access_constraint
  - group_coordination
  - fatigue_load
  - observation_state_gap

platform_specific:
  - self_view_layout
  - gallery_layout
  - breakout_implementation
  - reaction_controls
  - host_permissions
  - analytics_available
  - bandwidth_adaptation

rule:
  platform_specific_numeric_effects_require_platform_validation: true
```

---

# 36. PRACTICAL-SKILL RULE

\[
\boxed{
Evidence_{competence}
\neq
Exposure_{online}
}
\]

If competence is materially practical/embodied, valid evidence may require:
- hybrid practice;
- observed demonstration;
- live performance;
- supervised external practice;
- delayed competency check.

---

# 37. VERIFICATION RULE

\[
\boxed{
EvidenceSet
=
\{
Identity,
Participation,
Authorship,
Understanding,
Application
\}
}
\]

Verification is not surveillance.

\[
\boxed{
VerificationGain
\not\Rightarrow
NetBenefit
}
\]

Privacy/governance cost must be included.

---

# 38. VALIDATION CONTRACT

```yaml
validation_contract:

  development:
    - define_population
    - define_prediction_time
    - define_horizon
    - define_outcome
    - define_predictors_available_before_prediction
    - define_missing_data_strategy
    - pass_sample_size_gate

  internal_validation:
    - bootstrap_or_nested_cross_validation_or_temporal_split
    - calibration
    - discrimination

  external_validation:
    - new_cohort_or_site
    - transportability_review
    - subgroup_fairness_review

  performance:
    binary:
      - AUROC
      - AUPRC
      - Brier_score
      - calibration_intercept
      - calibration_slope
      - calibration_plot

  prohibited:
    - training_set_performance_as_final_result
    - accuracy_only
```

Calibration equation:

\[
\boxed{
\operatorname{logit}P(Y=1)
=
a_{cal}
+
b_{cal}\operatorname{logit}(p_{raw})
}
\]

Ideal:

\[
a_{cal}=0,\qquad b_{cal}=1
\]

---

# 39. DEPLOYMENT STATE MACHINE

```yaml
deployment_state_machine:

  GLOBAL_STRUCTURAL:
    probability_output: false
    intervention_claim: candidate_only

  LOCAL_MEASUREMENT_VALIDATED:
    require:
      - local_measurement_model
      - invariance_or_group_specific_model
    probability_output: false

  LOCALLY_FITTED:
    require:
      - sample_size_gate_passed
      - local_fit
      - missing_data_strategy
    probability_output: restricted

  INTERNALLY_VALIDATED:
    require:
      - held_out_or_temporal_validation
      - calibration
      - discrimination
      - fairness_audit
    probability_output: conditional

  EXTERNALLY_VALIDATED:
    require:
      - external_population_or_site
      - transportability_review
    probability_output: allowed_within_scope

  CAUSALLY_VALIDATED_INTERVENTION:
    require:
      - identified_effect
      - comparator
      - interference_handled
      - harm_monitoring
      - replication_or_strong_external_support
    intervention_claim: allowed_within_scope
```

---

# 40. AI RUNTIME ALGORITHM

```yaml
runtime_algorithm:

  step_1_define_scope:
    collect:
      - population
      - platform
      - course_type
      - group_structure
      - prediction_or_intervention_target
      - horizon

  step_2_map_anchor:
    map_problem_to:      - A
      - M
      - C
      - B
      - R
      - J
      - P
      - V
      - D
      - I

  step_3_reclassify:
    construct:
      - K_i
      - U_g_t
      - M_i_g_t
      - X_i_g_t
      - G_g_t
      - H_j_g_t
      - N_o_t
      - O_i_g_t
      - V_i_g_t
      - D_obj_i_g_t
      - D_perc_i_g_t

  step_4_check_access:
    distinguish:
      - failed_entry
      - entered_but_constrained
      - meaningful_participation

  step_5_enforce_noncollapse:
    required: true

  step_6_define_outcome:
    choose_specific_Y_k: true

  step_7_define_horizon:
    required: true

  step_8_check_measurement:
    latent_vs_observed_separated: true
    invariance_if_cross_group: required

  step_9_check_data_quality:
    - leakage
    - missingness
    - sample_size
    - clustering
    - repeated_measurement

  step_10_prediction:
    if_no_validated_local_model:
      probability_output: false
      output: structural_risk_reasoning_only

  step_11_intervention:
    generate_candidate_actions: true
    causal_language_requires_identification: true

  step_12_compare_harms:
    include:
      - fatigue
      - privacy
      - workload
      - inequality
      - access
      - cost

  step_13_output:
    report:
      - triggered_anchor_domains
      - evidence
      - unknowns
      - validation_status
      - uncertainty
      - candidate_interventions
      - causal_status
      - governance_risk
```

---

# 41. AI OUTPUT SCHEMA

```yaml
assessment:

  spec:
    id: TOLEDO-ZOOM-GLOBAL-FINAL-STANDALONE
    deployment_status: GLOBAL_STRUCTURAL

  scope:
    population: null
    platform: null
    course_type: null
    group_size: null
    time_index: null
    prediction_horizon: null

  anchor:
    A: {status: unknown, evidence: []}
    M: {status: unknown, evidence: []}
    C: {status: unknown, evidence: []}
    B: {status: unknown, evidence: []}
    R: {status: unknown, evidence: []}
    J: {status: unknown, evidence: []}
    P: {status: unknown, evidence: []}
    V: {status: unknown, evidence: []}
    D: {status: unknown, evidence: []}
    I: {status: unknown, evidence: []}

  states:
    structural_context: {}
    medium: {}
    learner: {}
    group: {}
    teacher: {}
    organization: {}

  observations: []

  verification:
    status: unresolved
    uncertainty: unknown

  outcomes:
    targets: []

  prediction:
    allowed: false
    reason: no_validated_local_model
    values: []

  interventions:
    candidates: []
    causal_status: candidate_only

  harms:
    fatigue: unknown
    privacy: unknown
    workload: unknown
    inequality: unknown
    access: unknown

  assumptions: []
  missing_data: []
  subgroup_limitations: []
```

---

# 42. SOLUTION STATUS LADDER

```yaml
solution_status:

  S0_DETECTED:
    meaning: problem represented only

  S1_MECHANISM_MAPPED:
    meaning: candidate mechanism/intervention identified

  S2_EVIDENCE_SUPPORTED:
    meaning: external evidence supports direction

  S3_LOCALLY_FITTED:
    meaning: target-site effect estimated

  S4_INTERNALLY_VALIDATED:
    meaning: held-out validation passed

  S5_EXTERNALLY_VALIDATED:
    meaning: replicated externally

  S6_OPERATIONAL:
    meaning: deployment allowed within declared scope with monitoring/rollback
```

---

# 43. CLAIM CEILING

Allowed:

> This is a globally oriented, evidence-calibrated, Toledo-compatible dynamic causal-predictive framework for synchronous group videoconference learning. It structurally covers 94 recurrent problem phenomena and provides a common formal architecture for prediction, intervention, transportability, validation, and governance across populations and settings.

Not allowed without the required validation:

> This model predicts accurately worldwide.

> This model identifies universally optimal interventions.

> A global prior alone justifies an individual risk probability.

---

# 44. FINAL MACHINE RULE

```yaml
final_machine_rule:

  preserve_anchor:
    - A
    - M
    - C
    - B
    - R
    - J
    - P
    - V
    - D
    - I

  before_cross_country_latent_comparison:
    require:
      - measurement_invariance_or_group_specific_measurement

  before_numeric_prediction:
    require:
      - local_fit
      - sample_size_gate
      - missing_data_strategy
      - declared_horizon
      - calibration_status

  before_causal_intervention_claim:
    require:
      - comparator
      - target_outcome
      - identification_strategy
      - consistency
      - positivity
      - exchangeability_or_randomization
      - interference_handling_if_grouped

  before_causal_transport:
    require:
      - source_target_overlap
      - effect_modifier_review
      - measurement_compatibility
      - treatment_consistency

  before_operational_deployment:
    require:
      - internal_or_external_validation_as_claimed
      - fairness_review
      - harm_monitoring
      - rollback_plan

  always_forbid:
    - attendance_equals_learning
    - camera_equals_engagement
    - tool_presence_equals_designed_interaction
    - prediction_equals_causation
    - universal_coefficient_without_transport_validation
```

---


# 44A. EVIDENCE QUALITY GATE

Numerical evidence must be graded before use.

```yaml
evidence_grades:

  A:
    definition: >
      Meta-analysis, meta-review, umbrella review, randomized evidence,
      or multiple high-quality experimental studies directly relevant to the construct.
    prior_policy: robust_informative

  B:
    definition: >
      Systematic review or strong primary empirical evidence with limited
      direct transportability.
    prior_policy: weak_to_moderate_informative

  C:
    definition: >
      Repeated empirical pattern with mixed effects or no stable pooled estimate.
    prior_policy: zero_centered_or_directional_weak

  D:
    definition: conceptually_plausible_but_empirically_weak
    prior_policy: weak_zero_centered

  U:
    definition: untested_or_unknown
    prior_policy: no_directional_claim
```

Numeric-prior gate:

```yaml
numeric_prior_gate:
  accepted_sources:
    - meta_analysis
    - second_order_meta_analysis
    - systematic_review_with_meta_analysis
    - randomized_controlled_trial
    - field_experiment
    - large_longitudinal_or_multilevel_study

  require_at_least_one:
    - effect_size
    - correlation
    - standardized_mean_difference
    - confidence_interval
    - heterogeneity
    - sample_size

  prohibit:
    - narrative_claim_to_numeric_weight
    - prevalence_to_regression_coefficient
    - sample_size_as_effect_magnitude
```

---

# 44B. ROBUST META-ANALYTIC PRIOR

Where a meta-analytic prior is commensurate with the local parameter:

\[
z_e^{local}
\sim
\mathcal N
\left(
z_e^{meta},
SE_{meta,e}^2+\tau_{transport,e}^2
\right)
\]

For highly heterogeneous evidence, use a robust mixture rather than forcing the pooled estimate:

\[
\boxed{
p(\theta_e)
=
w_e\,p_{meta}(\theta_e)
+
(1-w_e)\,p_{weak}(\theta_e)
}
\tag{PROP-ROBUST-PRIOR}
\]

`w_e` MUST NOT be invented. It depends on target/source similarity, measurement compatibility, external validation, and sensitivity analysis.

---

# 44C. OUTCOME-SPECIFIC MODEL CONTRACT

The same predictors MUST NOT be assumed to have identical coefficients across outcomes.

```yaml
outcome_specific_contract:

  Y_access:
    primary_domains: [A, I, M, N]

  Y_fatigue:
    primary_domains: [B, M, C, J, R]
    history_required: true

  Y_engagement:
    primary_domains: [E, S, J, R, P, M, D_perc]

  Y_comprehension:
    primary_domains: [C, J, P, S, M, R]
    target_leakage_prohibited: true

  Y_learning:
    primary_domains: [C, J, P, R, S]

  Y_completion:
    primary_domains: [A, E, S, P, J, N]

  Y_verification:
    primary_domains: [V, O, D]

  Y_privacy:
    primary_domains: [D_obj, D_perc, N]
```

Outcome identities must remain separate:
- actual learning;
- perceived learning;
- satisfaction;
- retention;
- practical performance;
- completion;
- fatigue.

---

# 44D. PREDICTION HORIZON CONTRACT

Every prediction MUST declare \(h\).

```yaml
prediction_horizons:

  within_session:
    examples:
      - fatigue_in_30_minutes
      - disengagement_before_next_break

  next_session:
    examples:
      - failure_to_return
      - elevated_fatigue

  course_end:
    examples:
      - non_completion
      - low_comprehension

  delayed:
    examples:
      - retention_after_7_days
      - transfer_after_30_days
```

A model with no declared horizon MUST NOT be labeled predictive.

---

# 44E. SENSOR / OBSERVATION RELIABILITY CONTRACT

Observable platform traces are noisy sensors.

```yaml
sensor_contract:

  camera_state:
    direct_equivalence_to_engagement: forbidden
    reliability: context_dependent

  attendance_duration:
    target: exposure
    equivalence_to_learning: forbidden

  poll_response:
    target: local_response_or_participation
    equivalence_to_understanding: forbidden

  chat_message:
    target: visible_participation
    limitation: silent_engagement_not_observed

  oral_response:
    target: local_participation_and_understanding
    limitations:
      - language
      - anxiety
      - turn_taking

  quiz:
    target: sampled_knowledge
    limitations:
      - item_quality
      - authorship
      - test_conditions
      - temporal_leakage
```

---

# 44F. GENERAL CAUSAL IDENTIFICATION GATE

No intervention may be labeled `VALIDATED_SOLUTION` unless an identification strategy is declared.

```yaml
causal_identification_gate:

  required_questions:
    - what_is_the_intervention
    - what_is_the_comparator
    - what_is_the_outcome
    - what_is_the_effect_horizon
    - who_receives_the_intervention
    - can_peers_be_affected
    - what_confounders_exist
    - how_was_treatment_assigned
    - what_missing_data_process_exists

  preferred_designs:
    - randomized_controlled_trial
    - cluster_randomized_trial
    - stepped_wedge_cluster_trial
    - randomized_within_person_crossover
    - micro_randomized_trial
    - factorial_experiment

  acceptable_with_caution:
    - difference_in_differences
    - interrupted_time_series
    - regression_discontinuity
    - instrumental_variable
    - target_trial_emulation
    - propensity_weighted_longitudinal_analysis

  insufficient_alone:
    - before_after_without_comparator
    - cross_sectional_correlation
    - descriptive_prevalence
    - instructor_impression
    - platform_log_correlation
```

Effect types:

```yaml
effect_types:
  direct_effect: treated_unit_effect
  indirect_effect: mediator_path_effect
  spillover_effect: effect_on_peers
  cluster_effect: group_level_policy_effect
  governance_effect: privacy_or_process_risk_effect
```

---

# 44G. SOLUTION ADDRESSABILITY GATE

A problem is solution-addressable only when all fields exist:

```yaml
solution_addressability_gate:
  required:
    - problem_detectable
    - mechanism_mapped
    - candidate_intervention_exists
    - outcome_defined
    - comparator_defined
    - harms_defined
    - causal_status_declared
```

If any field is absent, output MUST be:

- `MECHANISM_ONLY`, or
- `CANDIDATE_SOLUTION`

and MUST NOT be `SOLVED`.

---

# 44H. SOLUTION ENGINE RUNTIME

```yaml
solution_runtime:

  step_1_detect:
    output:
      - problem_id
      - anchor_domains
      - evidence

  step_2_decompose:
    output:
      - likely_mechanisms
      - uncertainty
      - competing_explanations

  step_3_generate_actions:
    output:
      - candidate_interventions
      - intervention_family

  step_4_filter_feasibility:
    check:
      - access
      - privacy
      - learner_preference
      - teacher_capacity
      - institutional_capacity
      - curriculum_or_legal_constraints
      - cost

  step_5_check_causal_evidence:
    classify:
      - no_causal_evidence
      - external_only
      - local_observational
      - local_experimental
      - externally_validated

  step_6_estimate_effect:
    only_if_identified: true
    estimands:
      - ATE
      - CATE
      - cluster_effect
      - spillover_effect

  step_7_compare_harms:
    include:
      - fatigue
      - privacy
      - workload
      - inequity
      - technical_failure

  step_8_recommend:
    labels:
      - candidate
      - evidence_supported
      - validated

  step_9_monitor:
    update:
      - outcome
      - adverse_effects
      - calibration
      - subgroup_performance
```

---

# 44I. GOVERNANCE PROBLEM RULE

Privacy, identity-document handling, recording, retention, and QA must not be optimized only as learning outcomes.

\[
\boxed{
RiskReduction
=
Risk_{before}
-
Risk_{after}
}
\]

```yaml
governance_rule:

  primary_objective:
    - minimize_unnecessary_collection
    - minimize_retention
    - restrict_access
    - preserve_auditability
    - meet_declared_purpose

  secondary_objective:
    - avoid_unnecessary_learning_burden
```

---

# 44J. MEDIATION CLAIM GATE

The expression:

\[
TotalEffect^{conceptual}
\leadsto
Direct+MediatedBenefits-MediatedHarms
\]

is conceptual only.

Formal causal mediation requires:

```yaml
mediation_gate:
  required:
    - mediator_defined
    - mediator_time_order_defined
    - mediator_outcome_confounding_addressed
    - exposure_induced_confounding_considered
    - estimand_declared
```

---

# 44K. GLOBAL MINIMUM DATA CONTRACT

Collect only what is necessary for the declared target.

```yaml
global_minimum_data_contract:

  identifiers:
    - pseudonymous_learner_id
    - group_id
    - session_id
    - time_index

  context:
    - device_type
    - connection_quality
    - learning_space_constraint
    - language_support_need
    - accessibility_need
    - digital_skill_or_experience

  session:
    - duration
    - group_size
    - activity_type
    - camera_policy
    - breakout_configuration
    - teacher_or_facilitator_support

  learner_state_measurement:
    - engagement
    - cognitive_load
    - fatigue
    - self_regulation

  group_state_measurement:
    - social_presence
    - cohesion
    - coordination
    - participation_inequality

  observations:
    - attendance_trace
    - response_trace
    - interaction_trace
    - technical_disruption_trace

  outcomes:
    - comprehension
    - learning
    - retention
    - completion
    - fatigue
    - participation
    - practical_performance_if_relevant

  governance:
    - recording_status
    - identity_verification_method
    - personal_data_collected
    - retention_rule
```

---

# 44L. SITE-SPECIFIC CALIBRATION WORKFLOW

```yaml
site_calibration:

  phase_1_measurement:
    - validate_measurement_model
    - test_invariance_if_comparing_groups

  phase_2_fit:
    - pass_sample_size_gate
    - fit_regularized_or_hierarchical_model
    - apply_missing_data_strategy

  phase_3_internal_validation:
    - temporal_holdout_or_bootstrap_or_nested_cross_validation
    - discrimination
    - calibration

  phase_4_recalibration:
    - calibration_intercept
    - calibration_slope

  phase_5_external_validation:
    - new_cohort_or_site
    - transportability_review
    - subgroup_fairness_review
```

---

# 44M. PILOT AND ROLLBACK CONTRACT

Candidate interventions should be tested first through small, reversible designs where ethically appropriate.

```yaml
causal_pilot:

  preferred_units:
    - learner_session
    - breakout_group
    - course_cohort

  candidate_reversible_interventions:
    - checkpoint_frequency
    - breakout_role_structure
    - technical_host
    - camera_choice_vs_default
    - pre_session_orientation
    - recovery_break_pattern
    - feedback_timing

  do_not_randomize_if:
    - privacy_rights_would_be_reduced
    - safeguarding_risk_increases
    - legally_or_ethically_required_content_would_be_withheld
    - accessibility_support_would_be_denied
```

```yaml
rollback_contract:

  monitor:
    - worse_comprehension
    - higher_fatigue
    - privacy_complaint
    - access_exclusion
    - teacher_overload
    - subgroup_harm

  if_material_harm:
    - stop_or_revert
    - investigate
    - update_model
    - document_change
```

---


# 44N. TOLEDO HUMAN CAPABILITY / HUMAN RETURN WELD

This section **extends the existing standalone document without replacing its Anchor**.

The original learning-system Anchor remains:

\[
\boxed{
Z^{Zoom}_{igt}
=
\langle
A^Z,M^Z,C^Z,B^Z,R^Z,J^Z,P^Z,V^Z,D^Z,I^Z
\rangle
}
\]

where \(A^Z\) means **Access**.

The Toledo Human-domain equations below remain canonical Toledo objects.  
All Zoom-to-HCA mappings introduced here are `DERIVED_PROPOSAL`.

---

## 44N.1 Canonical Toledo Human Capability anchors

### CAN-075 — Exposure non-collapse

\[
\boxed{
Exposure
\neq
Retention
\neq
Improvement
}
\]

### CAN-076 — Human return

\[
\boxed{
H_{return}
=
\langle
G_{CTSA},L,M,P,W,\Delta_{dir}
\rangle
}
\]

### CAN-077 — CTSA return

\[
\boxed{
R^{return}_{H}
=
\langle
C,T,S,A
\rangle
}
\]

### CAN-087 — Return conversion vector

\[
\boxed{
\Delta H_s
=
\langle
\Delta C_s,
\Delta T_s,
\Delta S_s,
\Delta A_s,
\Delta A^{corr}_{H,s},
\Delta\Lambda^{live}_{H,s}
\rangle
}
\]

### CAN-098 — Human Capability native river

Canonical sequence:

```text
Retained Difference
→ Human Readout
→ Live Problem
→ Barrier Readout
→ Candidate Routes
→ Human Endorsement
→ Adaptive Scaffold
→ Human Return
→ World Re-entry
```

### CAN-099 — HCA candidate state

\[
\boxed{
Z_{HCA,i,n}
=
\langle
P^{live}_{i,n},
K^{life}_{i,n},
B^{bar}_{i,n},
C^{cand}_{i,n},
C^{live}_{i,n},
h_{i,n},
R^{return}_{H,i,n},
\ldots
\rangle
}
\]

### CAN-100 — Life-capital context

\[
\boxed{
K^{life}_{i,n}
=
\langle
E^{econ},
F^{base},
L^{lang},
D^{digital},
T^{disc},
H^{health},
M^{mob},
N^{mentor},
C^{cred}
\rangle
}
\]

### CAN-101 — Capability non-collapse

\[
\boxed{
Resources
\neq
Access
\neq
Capability
\neq
RealizedOpportunity
}
\]

### CAN-102 — Barrier ledger

\[
\boxed{
B^{bar}_{i,n}
\subseteq
\{
Knowledge,
Skill,
Language,
Tool,
ResourceTime,
Network,
Credential,
Permission,
Opportunity,
Unknown
\}
}
\]

### CAN-103 — Candidate and human-endorsed routes

\[
\boxed{
C^{cand}_{i,n}
=
Gen(
P^{live},B^{bar},
K^{life},
R^{return}
)
}
\]

\[
\boxed{
C^{live}_{i,n}
=
\{
c\in C^{cand}:
Endorse_i(c)=1
\}
}
\]

### CAN-104 — Scaffold fading

\[
\boxed{
Stable\ Unaided\ Return\uparrow
\Rightarrow
h^{decisive}\downarrow
}
\]

Canonical sequence:

```text
Attempt
→ Minimal Sufficient Scaffold
→ Feedback
→ Reattempt
→ Fading
→ Unaided Execution
```

### CAN-105 — Realized opportunity

\[
\boxed{
\Omega^{real}_{i,n}
=
G_O(
R^{return}_{H,i,n},
K^{life}_{i,n},
Cred_{i,n},
Net_{i,n},
Perm_{i,n},
MarketReadout_n
)
}
\]

### CAN-106 — Net advancement record

\[
\boxed{
A^{HCA}_i
=
\langle
Gain_{CTSA},
Loss,
Transfer,
Ownership,
Burden,
BarrierChange,
OpportunityChange,
Provenance,
Warrant
\rangle
}
\]

---

# 44O. SYMBOL NAMESPACE

The symbol `A` is overloaded across domains.

```yaml
namespace:

  A_Z:
    meaning: Zoom_Access

  A_H:
    meaning: Human_Agency_or_A_component_in_Human_Return

  rule:
    - never_collapse_A_Z_and_A_H
```

---

# 44P. ZOOM → HCA DOMAIN WELD

Define a domain readout:

\[
\boxed{
q^{Zoom\rightarrow HCA}
:
(
Z^{Zoom},
K,
U,
X,
G,
H,
N,
O,
V,
D
)
\rightarrow
Z^{HCA}
}
\tag{PROP-ZHCA-WELD-01}
\]

The weld does **not** assert that every Zoom variable is a direct measure of human capability.

It asks:

> Which observed or inferred learning-system states are admissible evidence about barriers, retained human return, live possibilities, and realized opportunity?

---

# 44Q. LIFE-CAPITAL READOUT

Candidate readout from the existing Zoom system:

| Zoom evidence | HCA destination | Status |
|---|---|---|
| device / connection / digital skill | \(D^{digital}\), Tool barrier | candidate direct readout |
| language difficulty | \(L^{lang}\), Language barrier | candidate direct readout |
| time/household constraints | \(E^{econ},F^{base}\), ResourceTime barrier | partial/contextual |
| peer/teacher support | \(N^{mentor}\), Network | only when evidence supports it |
| credential evidence | \(C^{cred}\) | only when explicitly observed |
| health | \(H^{health}\) | UNKNOWN unless directly supplied |
| mobility | \(M^{mob}\) | UNKNOWN unless directly supplied |

```yaml
life_capital_readout_rule:

  if_not_observed:
    value: UNKNOWN

  prohibited:
    - infer_income_from_camera_background
    - infer_health_from_camera_state
    - infer_credential_from_platform_behavior
    - infer_mentor_network_from_chat_frequency_alone
```

---

# 44R. BARRIER EXTRACTION FROM THE ORIGINAL ANCHOR

Derived barrier readout:

\[
\boxed{
B^{bar}_{i,t}
=
q_B
\left(
A^Z,
M^Z,
C^Z,
B^Z,
R^Z,
J^Z,
P^Z,
V^Z,
D^Z,
I^Z
\right)_{i,t}
}
\tag{PROP-ZHCA-BARRIER-01}
\]

The output vocabulary MUST remain constrained by CAN-102.

```yaml
anchor_to_barrier_candidates:

  A_Z:
    likely:
      - Tool
      - ResourceTime
      - Unknown

  M_Z:
    likely:
      - Tool
      - Unknown

  C_Z:
    possible:
      - Knowledge
      - Skill
      - Unknown
    rule:
      - observed_difficulty_ne_skill_deficit

  B_Z:
    possible:
      - ResourceTime
      - Opportunity
      - Unknown
    rule:
      - burden_is_not_automatically_a_skill_barrier

  R_Z:
    possible:
      - Network
      - Unknown

  J_Z:
    possible:
      - Skill
      - Network
      - Unknown
    rule:
      - instructor_failure_ne_learner_skill_failure

  P_Z:
    possible:
      - Knowledge
      - Skill
      - Opportunity
      - Unknown

  V_Z:
    likely:
      - Unknown
    rule:
      - verification_uncertainty_is_not_capability_deficit

  D_Z:
    possible:
      - Permission
      - Opportunity
      - Unknown

  I_Z:
    possible:
      - Language
      - Tool
      - ResourceTime
      - Network
      - Credential
      - Permission
      - Opportunity
      - Unknown
```

---

# 44S. DIAGNOSE BEFORE SCAFFOLD

Before choosing a solution, reduce uncertainty about the barrier.

Using Toledo CAN-112 diagnostic logic:

\[
\boxed{
u^*_{diag}
=
\arg\max_u
[
IG_B(u)
-
\lambda_C Cost(u)
-
\rho Risk(u)
]
}
\]

Candidate low-cost diagnostic actions in this learning domain:

```yaml
diagnostic_actions:
  - comprehension_probe
  - private_help_request
  - connection_check
  - language_check
  - alternate_response_mode
  - short_delayed_recall
  - practical_demonstration
  - authorship_check
```

This creates the sequence:

\[
ObservedProblem
\rightarrow
BarrierHypotheses
\rightarrow
DiagnosticProbe
\rightarrow
UpdatedBarrierLedger
\]

rather than:

\[
ObservedProblem
\rightarrow
AssumedSkillDeficit
\]

---

# 44T. CANDIDATE ROUTES + HUMAN OWNERSHIP

Use Toledo CAN-103:

\[
\boxed{
C^{cand}_{i,t}
=
Gen(
P^{live}_{i,t},
B^{bar}_{i,t},
K^{life}_{i,t},
R^{return}_{H,i,t}
)
}
\]

Then:

\[
\boxed{
C^{live}_{i,t}
=
\{
c\in C^{cand}_{i,t}
:
Endorse_i(c)=1
\}
}
\]

Hard non-collapse:

\[
\boxed{
AI\ Suggestion
\neq
Human\ Endorsement
\neq
Human\ Choice
}
\]

The existing intervention engine therefore generates **candidate routes**.  
It does not own the learner's route.

---

# 44U. LEARNING OUTCOME → HUMAN RETURN

The original Standalone already enforces:

\[
Connection
\neq
Attendance
\neq
Participation
\neq
Understanding
\neq
Retention
\neq
Application
\]

The HCA weld extends this chain:

\[
\boxed{
Application
\neq
UnaidedHumanReturn
\neq
Capability
\neq
RealizedOpportunity
}
\tag{PROP-ZHCA-RETURN-NONCOLLAPSE}
\]

Also preserve Toledo CAN-074:

\[
\boxed{
\Delta Performance_{assisted}>0
\not\Rightarrow
\Delta H_{return}>0
}
\]

Preferred evidence for human return:

```yaml
human_return_evidence:
  stronger:
    - delayed_recall
    - unaided_explanation
    - unaided_reperformance
    - transfer_to_new_problem
    - independent_error_correction
    - performance_after_scaffold_fading

  insufficient_alone:
    - camera_on
    - attendance
    - copied_answer
    - immediate_prompted_answer
    - AI_assisted_answer
    - completion_click
```

---

# 44V. HUMAN RETURN UPDATE

The Zoom framework supplies evidence; Toledo defines the return object.

\[
\boxed{
R^{return}_{H,i,t}
=
\langle
C,T,S,A
\rangle_{i,t}
}
\]

Candidate update:

\[
\boxed{
R^{return}_{H,i,t+1}
=
U_R
\left(
R^{return}_{H,i,t},
E^{unaided}_{i,t+h},
E^{transfer}_{i,t+h},
E^{correction}_{i,t+h},
c_t
\right)
}
\tag{PROP-ZHCA-RETURN-UPDATE-01}
\]

This is a `DERIVED_PROPOSAL`; it does not replace CAN-077.

---

# 44W. RETURN-CONVERSION VECTOR

Use Toledo CAN-087:

\[
\boxed{
\Delta H_s
=
\langle
\Delta C_s,
\Delta T_s,
\Delta S_s,
\Delta A_s,
\Delta A^{corr}_{H,s},
\Delta\Lambda^{live}_{H,s}
\rangle
}
\]

The Zoom system should therefore evaluate more than performance gain.

It may contribute evidence for:

```yaml
return_conversion_readout:
  - capability_change
  - transfer_change
  - self_correction_change
  - agency_change
  - corrigibility_change
  - live_possibility_change
```

---

# 44X. LIVE POSSIBILITY FIELD

Toledo gives:

\[
\boxed{
\Pi^{live}_{H,t}(g)
\subseteq
\Pi^{feas}_{H,t}(g)
\subseteq
\Pi^{phys}_{t}(g)
}
\]

Derived comparison:

\[
\boxed{
\Delta L^{live}_{H,i,t}
=
Compare
\left(
L_{H,i,t+1},
L_{H,i,t}
\right)
}
\tag{PROP-ZHCA-LIVEFIELD-01}
\]

Do not force this into one universal scalar.

```yaml
live_field_change:
  newly_live: []
  strengthened: []
  weakened: []
  no_longer_live: []
  unresolved: []
```

Meaning:

> The learning system is useful for human potential when retained learning makes previously infeasible or psychologically/non-instrumentally inaccessible actions genuinely live for the person.

---

# 44Y. SCAFFOLD FADING

Use Toledo CAN-104:

\[
\boxed{
Stable\ Unaided\ Return\uparrow
\Rightarrow
h^{decisive}\downarrow
}
\]

Integrated learning sequence:

```text
Attempt
→ Detect problem
→ Extract barrier hypotheses
→ Diagnose
→ Minimal sufficient scaffold
→ Feedback
→ Reattempt
→ Verify unaided return
→ Fade scaffold
→ Unaided execution
```

Therefore:

\[
\boxed{
MaxAssistedPerformance
\neq
MaxHumanCapability
}
\]

---

# 44Z. ADVANCEMENT POLICY

The original Standalone already uses Pareto-safe intervention selection.

Connect this to Toledo's advancement objective:

\[
\boxed{
\pi^{*}_{ZHCA}
\in
\arg\max_{\pi\in\mathcal A^{Pareto}}
E[
\Delta H_s
\mid
\pi
]
}
\tag{PROP-ZHCA-POLICY-01}
\]

subject to:

```yaml
constraints:
  - privacy
  - access
  - fairness
  - fatigue
  - teacher_burden
  - legal_and_governance_requirements
  - human_endorsement
```

This is a `DERIVED_PROPOSAL`.

---

# 44AA. REALIZED OPPORTUNITY

Use Toledo CAN-105:

\[
\boxed{
\Omega^{real}_{i,n}
=
G_O(
R^{return}_{H,i,n},
K^{life}_{i,n},
Cred_{i,n},
Net_{i,n},
Perm_{i,n},
MarketReadout_n
)
}
\]

Therefore:

\[
\boxed{
LearningGain
\neq
CapabilityGain
\neq
RealizedOpportunityGain
}
\]

A learner can improve but remain blocked by:

- credential;
- permission;
- network;
- market/opportunity;
- resource/time constraints.

---

# 44AB. NET ADVANCEMENT RECORD

Use Toledo CAN-106 as the terminal record:

\[
\boxed{
A^{HCA}_i
=
\langle
Gain_{CTSA},
Loss,
Transfer,
Ownership,
Burden,
BarrierChange,
OpportunityChange,
Provenance,
Warrant
\rangle
}
\]

The Zoom system should output evidence into this record rather than creating a single "human potential score".

---

# 44AC. INTEGRATED MASTER WELD — CANONICAL TOLEDO `EQ-002/H.07.v1`

**Canonical status update (2026-10-07):** the composition in this subsection was admitted to
Toledo as `EQ-002/H.07.v1` / `CAN-1318`, tier `Definition`, status `current`.
The historical local tag `PROP-ZHCA-MASTER-01` below is a provenance alias only; the canonical
code governs citation and reuse.

\[
\boxed{
Z^{Zoom}_{igt}
\xrightarrow{q_B}
B^{bar}_{i,t}
\xrightarrow{u^*_{diag}}
C^{cand}_{i,t}
\xrightarrow{Endorse_i}
C^{live}_{i,t}
\xrightarrow{\pi^*_{scaffold}}
R^{return}_{H,i,t+1}
\xrightarrow{Retention}
\Delta H_{i,t+1}
\xrightarrow{LiveField}
L_{H,i,t+1}
\xrightarrow{G_O}
\Omega^{real}_{i,t+1}
\xrightarrow{Record}
A^{HCA}_{i,t+1}
}
\tag{PROP-ZHCA-MASTER-01}
\]

Human-readable chain:

```text
Zoom learning state
→ barrier readout
→ diagnostic probe
→ candidate routes
→ human endorsement
→ minimal sufficient scaffold
→ reattempt
→ unaided human return
→ retained capability change
→ live possibility expansion
→ realized opportunity
→ net advancement record
→ world action / feedback
```

---

# 44AD. FULL NON-COLLAPSE SPINE

\[
\boxed{
Resources
\neq
Access
\neq
Exposure
\neq
Participation
\neq
Understanding
\neq
Retention
\neq
Improvement
\neq
UnaidedHumanReturn
\neq
Capability
\neq
RealizedOpportunity
}
\tag{PROP-ZHCA-NONCOLLAPSE-01}
\]

This is the central guardrail against interpreting platform success as human potential.

---

# 44AE. OPTIONAL HCA RUNTIME MODE

The original runtime remains valid.

When the user's goal concerns **human development, capability, durable learning, agency, transfer, or realized opportunity**, activate:

```yaml
HCA_runtime:

  trigger:
    - durable_learning
    - human_potential
    - capability
    - transfer
    - agency
    - independence
    - realized_opportunity

  after_original_runtime:
    step_1:
      action: extract_barrier_ledger
      vocabulary: CAN_102

    step_2:
      action: diagnose_uncertain_barriers

    step_3:
      action: generate_candidate_routes
      equation: CAN_103

    step_4:
      action: require_human_endorsement

    step_5:
      action: apply_minimal_sufficient_scaffold

    step_6:
      action: collect_unaided_return_evidence

    step_7:
      action: update_return_conversion

    step_8:
      action: evaluate_live_field_change

    step_9:
      action: evaluate_realized_opportunity

    step_10:
      action: emit_CAN_106_net_advancement_record

  prohibited:
    - human_potential_scalar_without_validation
    - assisted_output_as_human_return
    - access_as_capability
    - capability_as_realized_opportunity
    - AI_suggestion_as_human_choice
```

---

# 44AF. HCA OUTPUT SCHEMA

```yaml
human_capability_extension:

  active: false

  barrier_ledger:
    Knowledge: []
    Skill: []
    Language: []
    Tool: []
    ResourceTime: []
    Network: []
    Credential: []
    Permission: []
    Opportunity: []
    Unknown: []

  candidate_routes: []

  human_endorsed_routes: []

  scaffold:
    current_level: null
    fading_status: null

  return_evidence:
    delayed_recall: null
    unaided_explanation: null
    unaided_reperformance: null
    transfer: null
    independent_error_correction: null

  return_conversion:
    delta_C: unknown
    delta_T: unknown
    delta_S: unknown
    delta_A: unknown
    delta_A_corr: unknown
    delta_live_field: unknown

  live_field_change:
    newly_live: []
    strengthened: []
    weakened: []
    no_longer_live: []
    unresolved: []

  realized_opportunity:
    status: unresolved
    barriers_remaining: []

  net_advancement:
    Gain_CTSA: null
    Loss: null
    Transfer: null
    Ownership: null
    Burden: null
    BarrierChange: null
    OpportunityChange: null
    Provenance: []
    Warrant: []
```

---

# 44AG. WORLD CLOSURE

Use Toledo CAN-088:

```text
Live Problem
→ Question
→ Dialogue
→ Human Return
→ Action
→ World Feedback
→ Revision / Re-entry
```

The integrated system is therefore complete only when learning returns to human-owned action and observable world feedback.

---



---

# 44AH. EMPIRICAL MATURITY AFTER PHENOMENOLOGY + DATASET STRESS TEST

The integrated HCA weld has now been tested against real phenomenological studies and public-dataset-backed research.

```yaml
HCA_empirical_maturity:

  phenomenological_barrier_mapping:
    status: SUPPORTED

  access_and_context_layer:
    status: STRONGLY_SUPPORTED

  burden_and_fatigue_layer:
    status: STRONGLY_SUPPORTED

  relation_presence_pedagogy_layer:
    status: SUPPORTED

  observation_latent_noncollapse:
    status: STRONGLY_SUPPORTED

  barrier_ledger:
    status: QUALITATIVELY_SUPPORTED

  scaffold_to_immediate_performance:
    status: EMPIRICALLY_TESTABLE

  retention:
    status: PARTIALLY_SUPPORTED

  unaided_human_return:
    status: NOT_YET_DIRECTLY_VALIDATED

  live_possibility_change:
    status: NOT_YET_DIRECTLY_VALIDATED

  realized_opportunity:
    status: NOT_YET_DIRECTLY_VALIDATED
```

---

# 44AI. HCA FALSIFICATION CONTRACT

```yaml
HCA_falsification_contract:

  assisted_gain_without_return:
    if:
      - assisted_performance_improves
      - unaided_performance_does_not_improve
    output: ASSISTED_GAIN_WITHOUT_RETURN

  capability_without_opportunity:
    if:
      - unaided_return_improves
      - external_conversion_barriers_remain_binding
    output: CAPABILITY_GAIN_WITHOUT_REALIZED_OPPORTUNITY

  barrier_misclassification:
    if:
      - initial_barrier_label_is_skill
      - diagnostic_probe_shows_intact_skill
    action:
      - retract_skill_label
      - reopen_barrier_ledger
      - assign_unknown_or_supported_alternative

  scaffold_dependence:
    if:
      - repeated_assisted_success
      - decisive_scaffold_does_not_fade
    output: DEPENDENCE_RISK_OR_RETURN_NOT_ESTABLISHED
```

---

# 44AJ. HCA VALIDATION LADDER
```yaml
HCA_validation_ladder:

  H0:
    label: access_and_exposure
    status: validated_by_existing_evidence_families

  H1:
    label: engagement_and_understanding
    status: broadly_testable

  H2:
    label: retention
    status: partially_tested

  H3:
    label: unaided_human_return
    status: validation_gap

  H4:
    label: live_capability_field
    status: validation_gap

  H5:
    label: realized_opportunity
    status: validation_gap
```

AI MUST NOT propagate confidence from H0-H2 automatically into H3-H5.

---

# 44AK. END-TO-END HCA DATA REQUIREMENT

```yaml
end_to_end_HCA_dataset_required:

  baseline:
    - learner_context
    - barrier_ledger
    - baseline_unaided_task
    - baseline_live_routes

  intervention:
    - scaffold_type
    - scaffold_intensity
    - human_endorsement
    - assistance_source

  immediate:
    - assisted_performance
    - understanding

  delayed:
    - unaided_reperformance
    - delayed_recall
    - transfer_task
    - independent_error_correction

  capability:
    - barrier_change
    - live_route_change
    - agency_change

  realized_opportunity:
    - enacted_action
    - credential_context
    - network_context
    - permission_context
    - opportunity_or_market_context

  harms:
    - fatigue
    - privacy
    - dependence
    - inequality
```

---

# 45. 94-PROBLEM MACHINE MAP

The following 94-problem map is part of this standalone specification.
All interventions remain candidate mappings unless promoted through the solution-status ladder.

```yaml
problem_intervention_map:
  - problem_id: P01
    phenomenon: "Spatial Collapse: The Classroom Enters the Home"
    anchor_path: "K(A,I) → C/B/Dperc"
    audit_status: "🟡 Partial"
    intervention_families: [a_governance]
    candidate_action: "schedule/space/privacy alternatives; reduce simultaneous domestic demand"
    causal_estimand_class: individual_or_session_effect
    current_limit: "home roles are partly outside course control"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P02
    phenomenon: "Unequal Learning Space"
    anchor_path: "K(A,I) → C/B/E"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "minimum learning-space options; low-demand participation modes"
    causal_estimand_class: individual_or_session_effect
    current_limit: "physical environment cannot always be changed"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P03
    phenomenon: "Device Inequality"
    anchor_path: "A + device×task → ENTER/X/Y"
    audit_status: "✅ Structural"
    intervention_families: [a_access, a_pedagogy]
    candidate_action: "match task to device; equipment support; mobile-safe design"
    causal_estimand_class: individual_or_session_effect
    current_limit: "local device/task thresholds still need data"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P04
    phenomenon: "Shared-Device Competition"
    anchor_path: "A/I → ENTER"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "schedule flexibility; alternative access; device support"
    causal_estimand_class: individual_or_session_effect
    current_limit: "household competition is external"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P05
    phenomenon: "Bandwidth Inequality and Unstable Connectivity"
    anchor_path: "A/M → ENTER/C/E/Y"
    audit_status: "✅ Structural"
    intervention_families: [a_access, a_medium]
    candidate_action: "low-bandwidth pathway; adaptive media; reconnection support"
    causal_estimand_class: individual_or_session_effect
    current_limit: "exact bandwidth thresholds need local testing"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P06
    phenomenon: "Latency and Temporal Misalignment"
    anchor_path: "M → G(Coordination) → E/R"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_group]
    candidate_action: "turn-taking protocol; slower pacing; explicit floor control"
    causal_estimand_class: individual_or_session_effect
    current_limit: "optimal protocol depends on group/task"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P07
    phenomenon: "Power and Infrastructure Fragility"
    anchor_path: "A/N → ENTER"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "backup channel; recovery path; alternative attendance evidence"
    causal_estimand_class: individual_or_session_effect
    current_limit: "utility outages remain external"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P08
    phenomenon: "Digital-Skill Asymmetry"
    anchor_path: "A(digital skill) → Sbase/C → X"
    audit_status: "✅ Structural"
    intervention_families: [a_medium]
    candidate_action: "orientation, rehearsal, simpler interface"
    causal_estimand_class: individual_or_session_effect
    current_limit: "measure skill rather than assume it"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P09
    phenomenon: "Technical Presence Without Educational Presence"
    anchor_path: "O ≠ X; O → V"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_pedagogy]
    candidate_action: "multi-signal verification; activity/checkpoint evidence"
    causal_estimand_class: individual_or_session_effect
    current_limit: "cannot infer attention directly"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P10
    phenomenon: "Attendance–Engagement–Learning Mismatch"
    anchor_path: "Non-collapse chain: Connection≠Attendance≠Participation≠Understanding≠Retention≠Application"
    audit_status: "✅ Structural"
    intervention_families: [a_pedagogy]
    candidate_action: "separate attendance, participation, understanding, retention measures"
    causal_estimand_class: individual_or_session_effect
    current_limit: "requires outcome-specific measurement"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P11
    phenomenon: "Hypervisibility Through the Camera"
    anchor_path: "CameraPolicy → Dperc/B/R/M"
    audit_status: "🟡 Partial"
    intervention_families: [a_medium]
    candidate_action: "camera agency; self-view options; alternative participation"
    causal_estimand_class: individual_or_session_effect
    current_limit: "camera effects are mixed/context-dependent"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P12
    phenomenon: "Invisibility Through Camera-Off Participation"
    anchor_path: "O(camera) → V/R, not X directly"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_pedagogy]
    candidate_action: "do not use camera alone; use oral/chat/activity evidence"
    causal_estimand_class: individual_or_session_effect
    current_limit: "sensor reliability must be estimated"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P13
    phenomenon: "The Camera as a Surveillance Signal"
    anchor_path: "CameraPolicy → Dperc → B/O"
    audit_status: "🟡 Partial"
    intervention_families: [a_medium, a_governance]
    candidate_action: "privacy-aware camera policy; avoid camera-as-compliance proxy"
    causal_estimand_class: individual_or_session_effect
    current_limit: "perceived surveillance varies by learner/culture"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P14
    phenomenon: "Mirror Anxiety and Self-Focused Attention"
    anchor_path: "SelfView → Dperc/B/C"
    audit_status: "🟡 Partial"
    intervention_families: [a_learner]
    candidate_action: "hide-self-view/choice; reduce continuous self-monitoring"
    causal_estimand_class: individual_or_session_effect
    current_limit: "magnitude not locally calibrated"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P15
    phenomenon: "Hyper-Gaze and Perceived Social Pressure"
    anchor_path: "Interface/Gallery → B/M"
    audit_status: "🟡 Partial"
    intervention_families: [a_group]
    candidate_action: "reduce persistent gallery exposure; flexible display"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "no universal visual-layout threshold"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P16
    phenomenon: "Restricted Movement"
    anchor_path: "Camera/Session → B(load)"
    audit_status: "✅ Structural"
    intervention_families: [a_medium]
    candidate_action: "movement breaks; camera flexibility; posture change"
    causal_estimand_class: individual_or_session_effect
    current_limit: "optimal recovery dose not calibrated"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P17
    phenomenon: "Digital Eye Strain"
    anchor_path: "Duration/screen → B"
    audit_status: "✅ Structural"
    intervention_families: [a_medium]
    candidate_action: "screen breaks; modality changes; reduce continuous visual demand"
    causal_estimand_class: individual_or_session_effect
    current_limit: "clinical threshold outside current model"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P18
    phenomenon: "Zoom Fatigue"
    anchor_path: "B(t+1)=ρB+Load−Recovery+ε"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_learner]
    candidate_action: "manage duration/load/recovery; monitor fatigue"
    causal_estimand_class: individual_or_session_effect
    current_limit: "ρ and dose-response need local estimation"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P19
    phenomenon: "Nonverbal Production Load"
    anchor_path: "M/B ← performative visibility demand"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "reduce compulsory nonverbal performance; use explicit low-cost responses"
    causal_estimand_class: individual_or_session_effect
    current_limit: "direct educational effect not fully calibrated"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P20
    phenomenon: "Nonverbal Interpretation Load"
    anchor_path: "M/C ← reduced cues"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "explicit verbal cues; simpler visual field; structured checks"
    causal_estimand_class: individual_or_session_effect
    current_limit: "some cue loss is intrinsic to medium"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P21
    phenomenon: "Fragmented Attention"
    anchor_path: "C/Senact + U(task design)"
    audit_status: "✅ Structural"
    intervention_families: [a_learner, a_pedagogy]
    candidate_action: "shorter focused tasks; notification/task-switch control; checkpoints"
    causal_estimand_class: individual_or_session_effect
    current_limit: "attention remains latent"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P22
    phenomenon: "Multitasking Opacity"
    anchor_path: "O/V vs C/E"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "active evidence rather than surveillance; repeated low-cost checkpoints"
    causal_estimand_class: individual_or_session_effect
    current_limit: "multitasking cannot be reliably observed"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P23
    phenomenon: "Cognitive Overload From Interface Management"
    anchor_path: "M + A(skill) → C"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_learner]
    candidate_action: "simplify interface; reduce simultaneous channels; rehearsal"
    causal_estimand_class: individual_or_session_effect
    current_limit: "task-specific load measurement needed"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P24
    phenomenon: "Reconnection Cost After Technical Failure"
    anchor_path: "M disruption → C/E/history"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_pedagogy]
    candidate_action: "re-entry recap; task-state restoration; buddy/summary channel"
    causal_estimand_class: individual_or_session_effect
    current_limit: "severity depends on where disruption occurs"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P25
    phenomenon: "Silence Ambiguity"
    anchor_path: "O(silence) → V; M/R/C/B as alternatives"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "treat silence as ambiguous; request alternative evidence"
    causal_estimand_class: individual_or_session_effect
    current_limit: "requires multiple competing explanations"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P26
    phenomenon: "Turn-Taking Friction"
    anchor_path: "M → G(Coordination) → R/E"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "explicit speaking protocol; hand-raise/chat pathways"
    causal_estimand_class: individual_or_session_effect
    current_limit: "interaction style varies culturally"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P27
    phenomenon: "Reduced Peripheral Awareness"
    anchor_path: "M → R/G/V"
    audit_status: "🟡 Partial"
    intervention_families: [a_group, a_teacher]
    candidate_action: "explicit status signals; facilitator synthesis; group checks"
    causal_estimand_class: individual_or_session_effect
    current_limit: "cannot fully recreate physical peripheral awareness"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P28
    phenomenon: "Social Presence Thinning"
    anchor_path: "R+ → E/Y; J+/P+ → R+"
    audit_status: "✅ Structural"
    intervention_families: [a_group, a_teacher, a_pedagogy]
    candidate_action: "designed interaction; teacher/social presence; peer recognition"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "high heterogeneity across contexts"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P29
    phenomenon: "Loss of Informal Social Interaction"
    anchor_path: "R+/G outside formal task"
    audit_status: "🟡 Partial"
    intervention_families: [a_group]
    candidate_action: "informal pre/post spaces; peer contact opportunities"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "informal interaction cannot be forced"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P30
    phenomenon: "Reduced Sense of Belonging"
    anchor_path: "R+(belonging) → B/E/Y"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "stable cohorts; recognition; peer continuity"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "belonging is latent and context-sensitive"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P31
    phenomenon: "Help-Seeking Friction"
    anchor_path: "R(help) + J+ + N(support) → C/Y"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "low-threshold help channels; scheduled support; response norms"
    causal_estimand_class: individual_or_session_effect
    current_limit: "help quality and timing need measurement"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P32
    phenomenon: "Unequal Verbal Participation"
    anchor_path: "I(language/culture) + R/G + O"
    audit_status: "🟡 Partial"
    intervention_families: [a_group]
    candidate_action: "multi-modal participation; structured turns; written alternatives"
    causal_estimand_class: individual_or_session_effect
    current_limit: "equity effects vary by language/culture"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P33
    phenomenon: "Breakout-Room Silence"
    anchor_path: "Breakout × TaskStructure × Cohesion × TeacherMonitoring"
    audit_status: "✅ Structural"
    intervention_families: [a_group, a_pedagogy]
    candidate_action: "structure task/roles; group preparation; monitoring"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "direct breakout effect must stay zero-centered"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P34
    phenomenon: "Breakout-Room Free-Riding and Unequal Contribution"
    anchor_path: "R−/P/V/O"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "roles, individual evidence, contribution traces, oral verification"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "fairness thresholds need validation"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P35
    phenomenon: "Breakout-Room Time Loss"
    anchor_path: "P/J/M + transition cost"
    audit_status: "✅ Structural"
    intervention_families: [a_group, a_pedagogy]
    candidate_action: "reduce transition overhead; right-size task/time"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "optimal break-out duration unknown"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P36
    phenomenon: "Group Cohesion Fragility"
    anchor_path: "R+(Cohesion/Trust) dynamic"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "stable grouping; trust-building; repeated interaction"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "cohesion measurement required"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P37
    phenomenon: "Emotional Disengagement"
    anchor_path: "E/B/R/J/P"
    audit_status: "✅ Structural"
    intervention_families: [a_group, a_teacher, a_pedagogy]
    candidate_action: "task relevance, social presence, feedback, varied activity"
    causal_estimand_class: individual_or_session_effect
    current_limit: "multiple causal paths"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P38
    phenomenon: "Anxiety and Performance Pressure"
    anchor_path: "B + Dperc + I + participation policy"
    audit_status: "🟡 Partial"
    intervention_families: [a_learner, a_governance]
    candidate_action: "choice of response mode; predictable calling; privacy protections"
    causal_estimand_class: individual_or_session_effect
    current_limit: "anxiety has non-course causes"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P39
    phenomenon: "Loneliness Despite Synchronous Contact"
    anchor_path: "R+/B"
    audit_status: "🟡 Partial"
    intervention_families: [a_group]
    candidate_action: "peer continuity and relational contact, not mere meeting frequency"
    causal_estimand_class: individual_or_session_effect
    current_limit: "loneliness extends beyond course session"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P40
    phenomenon: "Motivation Erosion"
    anchor_path: "E/S/B/P/J"
    audit_status: "✅ Structural"
    intervention_families: [a_learner, a_teacher, a_pedagogy]
    candidate_action: "meaningful tasks, pacing, feedback, scaffolding"
    causal_estimand_class: individual_or_session_effect
    current_limit: "motivation cannot be inferred from attendance"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P41
    phenomenon: "Increased Self-Regulation Burden"
    anchor_path: "Sbase/Senact + C + J/P"
    audit_status: "✅ Structural"
    intervention_families: [a_learner]
    candidate_action: "scaffolds, checklists, pacing, prompts, support"
    causal_estimand_class: individual_or_session_effect
    current_limit: "SRL prior is small; do not overweight"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P42
    phenomenon: "Teacher Role Multiplication"
    anchor_path: "H(Workload/Capacity/TechStress) + J− + N"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_teacher, a_organization]
    candidate_action: "split technical/facilitation roles; staffing/support"
    causal_estimand_class: individual_or_session_effect
    current_limit: "organizational capacity required"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P43
    phenomenon: "Teacher Technostress"
    anchor_path: "H + M + N"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_learner, a_teacher]
    candidate_action: "rehearsal, technical support, platform simplification"
    causal_estimand_class: individual_or_session_effect
    current_limit: "teacher-specific state needs measurement"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P44
    phenomenon: "Loss of Pedagogical Attention to Platform Management"
    anchor_path: "H/J− → J+/P delivery"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_learner, a_teacher, a_pedagogy]
    candidate_action: "technical host; automation; preflight checks"
    causal_estimand_class: individual_or_session_effect
    current_limit: "benefit depends on staffing"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P45
    phenomenon: "On-Site Activity Translation Failure"
    anchor_path: "P− + CAN-007 candidate translation test"
    audit_status: "✅ Structural"
    intervention_families: [a_pedagogy]
    candidate_action: "redesign activity around preserved learning mechanism; verify outcome"
    causal_estimand_class: individual_or_session_effect
    current_limit: "must define invariant/readout/horizon"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P46
    phenomenon: "Practical-Skill Representation Failure"
    anchor_path: "P− → Y(skill)"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "hybrid/physical practice, demonstration, alternate competence evidence"
    causal_estimand_class: individual_or_session_effect
    current_limit: "some skills cannot be solved inside Zoom"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P47
    phenomenon: "Feedback Thinning"
    anchor_path: "J+/P+ → C/E/Y"
    audit_status: "✅ Structural"
    intervention_families: [a_teacher]
    candidate_action: "planned checkpoints; rapid feedback; multiple feedback channels"
    causal_estimand_class: individual_or_session_effect
    current_limit: "feedback quality not just frequency"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P48
    phenomenon: "Assessment Validity Problems"
    anchor_path: "V + O + M/K → Y measurement"
    audit_status: "✅ Structural"
    intervention_families: [a_pedagogy, a_governance]
    candidate_action: "multi-method assessment; authorship/identity checks; control test conditions"
    causal_estimand_class: individual_or_session_effect
    current_limit: "construct validity requires assessment design"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P49
    phenomenon: "Identity Uncertainty"
    anchor_path: "V + O(identity) + D"
    audit_status: "✅ Structural"
    intervention_families: [a_governance]
    candidate_action: "live identity verification + minimal-data record of verification"
    causal_estimand_class: individual_or_session_effect
    current_limit: "privacy safeguards required"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P50
    phenomenon: "Authorship Uncertainty"
    anchor_path: "V + O(performance/oral/activity)"
    audit_status: "🟡 Partial"
    intervention_families: [a_governance]
    candidate_action: "triangulate work with oral/performance evidence"
    causal_estimand_class: individual_or_session_effect
    current_limit: "cannot guarantee authorship from remote artifact alone"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P51
    phenomenon: "Privacy Exposure"
    anchor_path: "Dobj/Dperc"
    audit_status: "🛡 Governance"
    intervention_families: [a_medium, a_governance]
    candidate_action: "minimize visual/data exposure; optional background/camera pathways"
    causal_estimand_class: policy_or_process_effect
    current_limit: "not solved by learning-risk equation alone"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P52
    phenomenon: "Data-Protection Exposure"
    anchor_path: "Dobj + N(policy)"
    audit_status: "🛡 Governance"
    intervention_families: [a_access, a_governance]
    candidate_action: "data minimization, purpose, access, retention/deletion rules"
    causal_estimand_class: policy_or_process_effect
    current_limit: "requires governance/PDPA process"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P53
    phenomenon: "Recording Anxiety"
    anchor_path: "Dperc → B/E/O"
    audit_status: "🛡 Governance"
    intervention_families: [a_access, a_learner, a_governance]
    candidate_action: "recording consent/purpose/access; non-recorded alternatives"
    causal_estimand_class: policy_or_process_effect
    current_limit: "policy decision plus psychological effects"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P54
    phenomenon: "Accessibility Barriers"
    anchor_path: "I(accessibility) + A/P/N"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "captions, accessible materials, alternative interaction modes"
    causal_estimand_class: individual_or_session_effect
    current_limit: "needs impairment-specific design and testing"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P55
    phenomenon: "Language and Accent Barriers"
    anchor_path: "I(language)+M+C+R"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "interpreting/captions, pacing, written reinforcement"
    causal_estimand_class: individual_or_session_effect
    current_limit: "language-specific validation needed"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P56
    phenomenon: "Cultural Participation Mismatch"
    anchor_path: "I(culture)+R/P"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "multiple participation modes; culturally adapted facilitation"
    causal_estimand_class: individual_or_session_effect
    current_limit: "cannot infer preferred style from nationality alone"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P57
    phenomenon: "Socioeconomic Visibility"
    anchor_path: "I + Dperc/B/O(camera)"
    audit_status: "🟡 Partial"
    intervention_families: [a_medium, a_governance]
    candidate_action: "protect background/privacy; avoid camera compliance norms"
    causal_estimand_class: individual_or_session_effect
    current_limit: "underlying inequality remains external"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P58
    phenomenon: "Cumulative Disadvantage"
    anchor_path: "K interactions + N"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "bundle support across access/space/skill/help rather than one fix"
    causal_estimand_class: individual_or_session_effect
    current_limit: "compound effects need interaction estimation"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P59
    phenomenon: "Scalability–Interaction Trade-Off"
    anchor_path: "L(group size) × R/J/P"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "staff ratio, subgroup design, participation architecture"
    causal_estimand_class: individual_or_session_effect
    current_limit: "optimal group size is local/outcome-specific"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P60
    phenomenon: "Normalization of Emergency Remote Teaching"
    anchor_path: "N + P− + QA"
    audit_status: "🛡 Governance"
    intervention_families: [a_pedagogy, a_governance, a_organization]
    candidate_action: "redesign as intentional online course; QA/version control"
    causal_estimand_class: policy_or_process_effect
    current_limit: "organizational policy, not individual prediction"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P61
    phenomenon: "Unequal Device Access"
    anchor_path: "A/I → ENTER"
    audit_status: "✅ Structural"
    intervention_families: [a_access, a_pedagogy]
    candidate_action: "device/access support; device-safe course design"
    causal_estimand_class: individual_or_session_effect
    current_limit: "local prevalence is not a coefficient"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P62
    phenomenon: "Caregiver-Time Constraint"
    anchor_path: "I(household time) → ENTER/S/C"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "schedule flexibility, clearer independent-learning support"
    causal_estimand_class: individual_or_session_effect
    current_limit: "caregiver availability is external"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P63
    phenomenon: "Income-Stratified Access Problems"
    anchor_path: "I→A/N"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "targeted access support; low-cost/low-bandwidth pathway"
    causal_estimand_class: individual_or_session_effect
    current_limit: "course cannot remove income inequality"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P64
    phenomenon: "Smartphone-Centred Remote Learning"
    anchor_path: "A(device) × P(task)"
    audit_status: "✅ Structural"
    intervention_families: [a_access, a_pedagogy]
    candidate_action: "mobile-first materials; avoid tasks requiring desktop-only affordances"
    causal_estimand_class: individual_or_session_effect
    current_limit: "task-by-device effect needs testing"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P65
    phenomenon: "Difficulty Understanding Remote Assignments"
    anchor_path: "C + P+ + J+ → Y(comprehension)"
    audit_status: "✅ Structural"
    intervention_families: [a_teacher, a_pedagogy]
    candidate_action: "clear instructions, examples, concept checks, feedback"
    causal_estimand_class: individual_or_session_effect
    current_limit: "prevent outcome leakage in prediction"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P66
    phenomenon: "Difficulty Finding Help"
    anchor_path: "R(help)+J+/N"
    audit_status: "✅ Structural"
    intervention_families: [a_teacher]
    candidate_action: "visible help channel, response SLA, facilitator availability"
    causal_estimand_class: individual_or_session_effect
    current_limit: "availability ≠ quality; measure response"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P67
    phenomenon: "Weak Daily Well-Being Contact"
    anchor_path: "J+/N → B/E"
    audit_status: "🟡 Partial"
    intervention_families: [a_learner]
    candidate_action: "brief check-ins and escalation pathways"
    causal_estimand_class: individual_or_session_effect
    current_limit: "well-being support may require services beyond course"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P68
    phenomenon: "Limited Confidence Using Video Communication Tools"
    anchor_path: "A(skill)+Sbase+C"
    audit_status: "✅ Structural"
    intervention_families: [a_medium]
    candidate_action: "technical orientation and rehearsal"
    causal_estimand_class: individual_or_session_effect
    current_limit: "confidence should be measured, not assumed"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P69
    phenomenon: "Self-Motivation Difficulty"
    anchor_path: "S/E + J/P"
    audit_status: "✅ Structural"
    intervention_families: [a_learner, a_teacher, a_pedagogy]
    candidate_action: "structure, prompts, manageable tasks, progress feedback"
    causal_estimand_class: individual_or_session_effect
    current_limit: "SRL effect is modest globally"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P70
    phenomenon: "Anxiety Associated With Fully Online Learning"
    anchor_path: "B + K/I + U/M"
    audit_status: "🟡 Partial"
    intervention_families: [a_learner, a_pedagogy, a_governance]
    candidate_action: "identify course-linked stressors; reduce unnecessary performance/privacy load"
    causal_estimand_class: individual_or_session_effect
    current_limit: "pandemic/context confounding limits direct causal claim"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P71
    phenomenon: "Screen-Time and Sleep Disruption"
    anchor_path: "B/history + duration"
    audit_status: "🟡 Partial"
    intervention_families: [a_medium, a_learner]
    candidate_action: "reduce continuous screen dose; schedule/recovery design"
    causal_estimand_class: individual_or_session_effect
    current_limit: "sleep is partly outside session and needs longer-horizon data"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P72
    phenomenon: "Videoconference Fatigue in Local Populations"
    anchor_path: "B dynamic"
    audit_status: "✅ Structural"
    intervention_families: [a_medium, a_learner]
    candidate_action: "load/recovery model; dose and checkpoint monitoring"
    causal_estimand_class: individual_or_session_effect
    current_limit: "target site fatigue parameters not fitted"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P73
    phenomenon: "Stress and Burnout in Intensive Online Professional Education"
    anchor_path: "B/history + course/institution N"
    audit_status: "🟡 Partial"
    intervention_families: [a_learner]
    candidate_action: "workload/support/recovery review"
    causal_estimand_class: individual_or_session_effect
    current_limit: "burnout is longer-term and not Zoom-specific"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P74
    phenomenon: "Unstable Internet During Professional Education"
    anchor_path: "A/M → ENTER/X"
    audit_status: "✅ Structural"
    intervention_families: [a_access, a_medium]
    candidate_action: "low-bandwidth fallback; reconnection protocol"
    causal_estimand_class: individual_or_session_effect
    current_limit: "local network conditions vary"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P75
    phenomenon: "Reduced Peer Interaction in Online Learning"
    anchor_path: "R+ → E/Y"
    audit_status: "✅ Structural"
    intervention_families: [a_group]
    candidate_action: "designed peer interaction and social presence"
    causal_estimand_class: cluster_or_spillover_effect
    current_limit: "interaction quality, not tool presence"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P76
    phenomenon: "Environmental Distraction in Online Learning"
    anchor_path: "K(space/household) → C/S"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "task/pacing flexibility; learner environment planning"
    causal_estimand_class: individual_or_session_effect
    current_limit: "home environment not fully controllable"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P77
    phenomenon: "Perceived Inadequacy for Practical Skills"
    anchor_path: "P− → Y(skill)"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "hybrid/practical assessment; do not substitute verbal exposure for skill"
    causal_estimand_class: individual_or_session_effect
    current_limit: "requires physical competence evidence"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P78
    phenomenon: "Teacher Readiness Problems"
    anchor_path: "H + N + J"
    audit_status: "✅ Structural"
    intervention_families: [a_teacher]
    candidate_action: "training, rehearsal, support roles, readiness checks"
    causal_estimand_class: individual_or_session_effect
    current_limit: "readiness dimensions must be measured"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P79
    phenomenon: "Multi-Level Digital Divide in Synchronous Learning"
    anchor_path: "K(A,I)+N interactions"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "multi-level access/support, not device-only intervention"
    causal_estimand_class: individual_or_session_effect
    current_limit: "structural inequality remains outside course"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P80
    phenomenon: "Learning-Time Reduction and Academic Performance Decline"
    anchor_path: "Y(time/achievement) + K/N/history"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "monitor actual study time/outcomes; support structure"
    causal_estimand_class: individual_or_session_effect
    current_limit: "pandemic closure confounding; not attributable to Zoom alone"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P81
    phenomenon: "Learning-Loss Phenomena"
    anchor_path: "Y(learning/retention) over horizon"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "pre/post/delayed measures; targeted remediation"
    causal_estimand_class: individual_or_session_effect
    current_limit: "requires longitudinal outcome data"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P82
    phenomenon: "Absence and Disengagement in Online Classes"
    anchor_path: "ENTER + O + E + Y(completion)"
    audit_status: "✅ Structural"
    intervention_families: [a_pedagogy]
    candidate_action: "separate absence from silent engagement; early-risk checkpoints"
    causal_estimand_class: individual_or_session_effect
    current_limit: "local risk thresholds need fitting"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P83
    phenomenon: "Unequal Household Support"
    anchor_path: "I/K → S/C/ENTER"
    audit_status: "🟡 Partial"
    intervention_families: [a_pedagogy]
    candidate_action: "reduce reliance on household help; clear self-contained learner support"
    causal_estimand_class: individual_or_session_effect
    current_limit: "family resources external"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P84
    phenomenon: "Rural and Disadvantaged-Community Vulnerability"
    anchor_path: "I/A/N"
    audit_status: "🟡 Partial"
    intervention_families: [a_access]
    candidate_action: "low-bandwidth/access support; localized delivery options"
    causal_estimand_class: individual_or_session_effect
    current_limit: "geographic infrastructure external"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P85
    phenomenon: "Quality-Assurance Uncertainty in Online and Adult Learning"
    anchor_path: "N(QA)+V/Y"
    audit_status: "🛡 Governance"
    intervention_families: [a_governance]
    candidate_action: "define learning outcomes, evidence, versioning, audit and review"
    causal_estimand_class: policy_or_process_effect
    current_limit: "requires institutional QA, not a learner-only equation"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P86
    phenomenon: "The Access Paradox"
    anchor_path: "A/I/M/ENTER decomposition"
    audit_status: "🧩 Composite"
    intervention_families: [a_access, a_medium]
    candidate_action: "separate technical connection, meaningful access and quality constraints"
    causal_estimand_class: component_specific_effects
    current_limit: "not an independent outcome"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P87
    phenomenon: "The Visibility Paradox"
    anchor_path: "CameraPolicy → O/V/B/R/D/M"
    audit_status: "🧩 Composite"
    intervention_families: [a_medium, a_learner, a_governance]
    candidate_action: "balance evidence needs against privacy/fatigue; never use camera alone"
    causal_estimand_class: component_specific_effects
    current_limit: "no single optimal camera rule"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P88
    phenomenon: "The Presence Paradox"
    anchor_path: "O(connected) ≠ X(present); V"
    audit_status: "🧩 Composite"
    intervention_families: [a_learner, a_group]
    candidate_action: "triangulate cognitive/social presence with multiple evidence channels"
    causal_estimand_class: component_specific_effects
    current_limit: "presence remains latent"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P89
    phenomenon: "The Interaction Paradox"
    anchor_path: "Tool presence ≠ designed interaction; P/R/J"
    audit_status: "🧩 Composite"
    intervention_families: [a_teacher]
    candidate_action: "design interaction mechanism, roles and feedback"
    causal_estimand_class: component_specific_effects
    current_limit: "tool activation alone has no guaranteed effect"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P90
    phenomenon: "The Flexibility Paradox"
    anchor_path: "K/I × U(schedule/location)"
    audit_status: "🧩 Composite"
    intervention_families: [a_pedagogy]
    candidate_action: "offer flexibility without shifting all burden to learner/home"
    causal_estimand_class: component_specific_effects
    current_limit: "trade-off depends on context"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P91
    phenomenon: "The Scalability Paradox"
    anchor_path: "L(group size) × R/J/P"
    audit_status: "🧩 Composite"
    intervention_families: [a_group, a_organization]
    candidate_action: "scale staffing/group structure, not room capacity alone"
    causal_estimand_class: component_specific_effects
    current_limit: "no universal size threshold"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P92
    phenomenon: "The Data Paradox"
    anchor_path: "O-rich ≠ X/Y-known; V"
    audit_status: "🧩 Composite"
    intervention_families: [a_governance]
    candidate_action: "use data as noisy sensors; calibration/measurement model"
    causal_estimand_class: component_specific_effects
    current_limit: "more traces do not solve construct validity"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P93
    phenomenon: "The Continuity Paradox"
    anchor_path: "Scheduled delivery ≠ Y(learning/retention)"
    audit_status: "🧩 Composite"
    intervention_families: [a_pedagogy]
    candidate_action: "measure learning continuity, not timetable continuity"
    causal_estimand_class: component_specific_effects
    current_limit: "requires longitudinal outcomes"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
  - problem_id: P94
    phenomenon: "The Group Paradox"
    anchor_path: "same t but K_i/M_i/X_i differ; G dynamic"
    audit_status: "🧩 Composite"
    intervention_families: [a_group]
    candidate_action: "model individual conditions inside group; avoid group-average-only decisions"
    causal_estimand_class: component_specific_effects
    current_limit: "no single group-level fix"
    solution_status: CANDIDATE_NOT_CAUSALLY_VALIDATED
```

---

# 46. REFERENCES / EVIDENCE BASIS

Selected core sources used to construct or calibrate the specification:

1. Gegenfurtner, A., Alijagic, A., Gabel, S., & Keskin, Ö. (2026). Synchronous online learning supports cognitive and affective outcomes more than traditional face-to-face and asynchronous online education: A meta-analysis of webinars. *Learning and Individual Differences, 126*, 102862. DOI: `10.1016/j.lindif.2025.102862`

2. Martin, F., Sun, T., Westine, C. D., & Ritzhaupt, A. D. (2022). Examining research on the impact of distance and online learning: A second-order meta-analysis study. *Educational Research Review, 36*, 100438. DOI: `10.1016/j.edurev.2022.100438`

3. Martin, F., Wu, T., Wan, L., & Xie, K. (2022). A Meta-Analysis on the Community of Inquiry Presences and Learning Outcomes in Online and Blended Learning Environments. *Online Learning, 26*(1). DOI: `10.24059/olj.v26i1.2604`

4. Caskurlu, S., Maeda, Y., Richardson, J. C., & Lv, J. (2020). A meta-analysis addressing the relationship between teaching presence and students’ satisfaction and learning. *Computers & Education, 157*, 103966. DOI: `10.1016/j.compedu.2020.103966`

5. Richardson, J. C., Maeda, Y., Lv, J., & Caskurlu, S. (2017). Social presence in relation to students' satisfaction and learning in the online environment: A meta-analysis. *Computers in Human Behavior, 71*, 402–417. DOI: `10.1016/j.chb.2017.02.001`

6. Zhao, Y., Li, Y., Ma, S., Xu, Z., & Zhang, B. (2025). A meta-analysis of the correlation between self-regulated learning strategies and academic performance in online and blended learning environments. *Computers & Education, 230*, 105279. DOI: `10.1016/j.compedu.2025.105279`

7. Lan, M., Liu, H., & Pan, Q. (2025). Unpacking the digital literacy–self-regulated learning nexus: A systematic review and a three-level meta-analysis. *Educational Research Review*, 100713. DOI: `10.1016/j.edurev.2025.100713`

8. Borokhovski, E., Bernard, R. M., Tamim, R. M., Schmid, R. F., & Sokolovskaya, A. (2016). Technology-supported student interaction in post-secondary education: A meta-analysis of designed versus contextual treatments. *Computers & Education, 96*, 15–28. DOI: `10.1016/j.compedu.2015.11.004`

9. Wang, F., Ni, X., Zhang, M., & Zhang, J. (2024). Educational digital inequality: A meta-analysis of the relationship between digital device use and academic performance in adolescents. *Computers & Education, 213*, 105003. DOI: `10.1016/j.compedu.2024.105003`

10. Beyea, D., Lim, C., Lover, A., Foxman, M., Ratan, R., & Leith, A. (2025). Zoom fatigue in review: A meta-analytical examination of videoconferencing fatigue's antecedents. *Computers in Human Behavior Reports, 17*, 100571. DOI: `10.1016/j.chbr.2024.100571`

11. Shockley, K. M., Gabriel, A. S., Robertson, D., Rosen, C. C., Chawla, N., Ganster, M. L., & Ezerins, M. E. (2021). The fatiguing effects of camera use in virtual meetings: A within-person field experiment. *Journal of Applied Psychology, 106*(8), 1137–1155. DOI: `10.1037/apl0000948`

12. Bennett, A. A., Campion, E. D., Keeler, K. R., & Keener, S. K. (2021). Videoconference fatigue? Exploring changes in fatigue after videoconference meetings during COVID-19. *Journal of Applied Psychology, 106*(3), 330–344. DOI: `10.1037/apl0000906`

13. van Dorresteijn, C., et al. (2025). What Factors Contribute to Effective Online Higher Education? A Meta-Review. *Technology, Knowledge and Learning, 30*, 171–202. DOI: `10.1007/s10758-024-09750-5`

14. Anderson, J. L., & Krasnozhon, L. A. (2024). Turn the camera on to get better grade: Evidence from a field experiment. *International Review of Economics Education, 47*, 100301. DOI: `10.1016/j.iree.2024.100301`

15. Lehtinen, A., Kostiainen, E., & Näykki, P. (2023). Co-construction of knowledge and socioemotional interaction in pre-service teachers’ video-based online collaborative learning. *Teaching and Teacher Education, 133*, 104299. DOI: `10.1016/j.tate.2023.104299`

16. Collins, G. S., et al. (2024). TRIPOD+AI statement. *BMJ, 385*, e078378. DOI: `10.1136/bmj-2023-078378`

17. Moons, K. G. M., et al. (2025). PROBAST+AI. *BMJ, 388*, e082505. DOI: `10.1136/bmj-2024-082505`

Public-dataset-backed external stress-test sources:

18. Fauville, G., Luo, M., Queiroz, A. C. M., Lee, A., Bailenson, J. N., & Hancock, J. T. (2023). Large-sample videoconference-fatigue/nonverbal-mechanism study. Public anonymous data and code archived on OSF (`osf.io/c58zb`).

19. Li, Zhang, & Montag (2024). Too much to process? Exploring communication overload, information overload, and videoconference fatigue. *PLOS ONE, 19*(12), e0312376. DOI: `10.1371/journal.pone.0312376`. Public dataset: Figshare DOI `10.6084/m9.figshare.26772295.v2`.

20. Tirado-Morueta et al. (2026). Temporal dynamics of online learning interactions: A learning analytics study within the CoI framework. *Computers and Education Open, 11*, 100398. DOI: `10.1016/j.caeo.2026.100398`. Public dataset: Zenodo DOI `10.5281/zenodo.17551830`.

21. Le, Le, & Pham (2026). Data on student perceptions of blended learning, engagement, and academic achievement in engineering-related universities in Vietnam. *Data in Brief, 67*, 112958. DOI: `10.1016/j.dib.2026.112958`. Public dataset: Mendeley Data DOI `10.17632/tdsspksw83.1`.

---

# 47. FINAL STATUS

```yaml
final_status:
  standalone: true
  anchor_preserved: true
  problem_map_coverage: 94_of_94
  global_literature_calibration: peer_reviewed_complete_for_current_evidence_set
  external_dataset_backed_replay: completed
  raw_row_independent_refit: pending
  structural_global_use: allowed
  numeric_individual_prediction: requires_validated_local_model
  causal_intervention_claim: requires_identification_and_validation  phenomenology_dataset_stress_test:
    proximal_architecture: PASS
    HCA_distal_layers: VALIDATION_GAP
    anchor_change_required: false
  human_capability_weld:
    toledo_canon_preserved: true
    zoom_anchor_preserved: true
    status: CANONICAL_TOLEDO_EQ-002/H.07.v1
    internal_id: CAN-1318
    note: surrounding Zoom/HCA specializations remain proposal-level unless separately registered
    terminal_record: CAN_106
    scalar_human_potential_score: prohibited_without_validation
  intended_use:
    - AI_reasoning
    - research_design
    - model_development
    - course_system_diagnosis
    - intervention_hypothesis_generation
    - validation_planning
```

## END OF STANDALONE SPEC