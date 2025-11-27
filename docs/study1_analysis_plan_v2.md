# Study 1 Analysis Plan – Version 2

This document expands the analysis details that accompany the proposal
"Sequencing AI Recommendations and Accountability Practices in Product Teams:
Algorithmic Authority, Junior Voice, and Psychological Safety."

## 1. Experimental design

- 3 × 2 factorial at the agenda-item level:
  - Sequencing: AI-first, Human-first, Interleaved
  - Accountability: Accountability prompt vs. No prompt
- Blocking by team (and optionally sprint).
- Outcome unit: agenda item within a meeting.

## 2. Main outcomes

1. **Junior critical participation**
   - Binary indicator for whether a junior team member challenges, questions,
     or proposes an alternative to the focal recommendation on that item.
2. **Decision revision**
   - Binary indicator for whether the team changes its initial decision for
     that item.
3. **Perceived authority**
   - Item-level perception of whether the AI or human is "in charge" for
     the decision (derived from post-meeting surveys).
4. **Team psychological safety / junior voice climate**
   - Team-level measures from periodic surveys (e.g., Edmondson-style scales).

## 3. Main estimands

For each outcome \(Y_{ij}\) (agenda item \(i\) in team \(j\)):

- Average effect of AI-first vs. Human-first sequencing.
- Average effect of accountability prompt vs. no prompt.
- Interaction of sequencing × accountability.

## 4. Baseline models (illustrative)

Agenda-item model with team fixed effects:

\[
Y_{ij} = \beta_0
       + \beta_1 \text{AIFirst}_{ij}
       + \beta_2 \text{HumanFirst}_{ij}
       + \beta_3 \text{AccountabilityPrompt}_{ij}
       + \beta_4 (\text{AIFirst}_{ij} \times \text{AccountabilityPrompt}_{ij})
       + \beta_5 (\text{HumanFirst}_{ij} \times \text{AccountabilityPrompt}_{ij})
       + \alpha_j + \varepsilon_{ij},
\]

with standard errors clustered at the team level.

## 5. Link to synthetic data

Version 2 still uses **synthetic data** only:

- `data/raw/meetings_synthetic_v1.csv`
- `data/processed/agenda_item_panel_synthetic_v1.csv`

The example analysis script in `code/` illustrates how these models would be
estimated once real data are available.

