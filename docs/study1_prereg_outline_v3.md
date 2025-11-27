# Study 1 Preregistration-Style Outline – Version 3

This document mirrors common preregistration structures (e.g., OSF) for the
study "Sequencing AI Recommendations and Accountability Practices in Product Teams."

## 1. Background and Theoretical Rationale

- Brief summary of algorithmic authority, junior voice, and psychological safety.
- Motivation for studying sequencing of AI vs. human recommendations and
  accountability prompts in product teams.

## 2. Research Questions and Hypotheses

- RQ1: How does sequencing AI vs. human recommendations affect junior
  critical participation and decision revision?
- RQ2: How do accountability prompts interact with sequencing?
- RQ3: How do these practices shape perceived authority and team psychological safety?

Explicit hypotheses can be listed here and mapped to the analysis plan in
`docs/study1_analysis_plan_v2.md`.

## 3. Design Overview

- 3 × 2 factorial design at the agenda-item level:
  - Sequencing: AI-first, Human-first, Interleaved
  - Accountability: Prompt vs. No prompt
- Blocking by team (and possibly sprint).

## 4. Outcomes, Measures, and Timing

- Primary outcomes:
  - Junior critical participation on high-stakes items
  - Decision revision
- Secondary outcomes:
  - Perceived authority
  - Psychological safety / junior voice climate
- Timing:
  - Planned number of teams, meetings, and agenda items (illustrative at this stage).

## 5. Randomization and Implementation

- Agenda-level randomization to sequencing × accountability cells, blocked by team.
- Deterministic randomization logic would be implemented in code (to be developed)
  and audited before deployment.

## 6. Analysis Plan Link

- Analysis details (models, estimands) are in
  `docs/study1_analysis_plan_v2.md`.
- Version 3 does not introduce new estimands, but organizes them in a
  preregistration-style template.

## 7. Data

- At this stage, Version 3 still uses **synthetic data** only (see `data/`).
- No real organizational or pilot data are included in the repository.

## 8. Deviations and Future Updates

- Any future changes to hypotheses, outcomes, or analysis will be documented in
  updated versions of this outline and/or in a formal OSF preregistration
  if one is later filed.

