import numpy as np
import pandas as pd
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parents[1]
raw_path = ROOT / "data" / "raw" / "meetings_synthetic_v1.csv"
processed_path = ROOT / "data" / "processed" / "agenda_item_panel_synthetic_v1.csv"

np.random.seed(42)

n_teams = 8
n_meetings_per_team = 20
n_items_per_meeting = 5

rows = []
item_id = 0

for team in range(1, n_teams + 1):
    for m in range(1, n_meetings_per_team + 1):
        for k in range(1, n_items_per_meeting + 1):
            item_id += 1

            # conditions
            sequencing = np.random.choice(["AI_first", "Human_first", "Interleaved"])
            accountability = np.random.choice(["Prompt", "NoPrompt"])

            critical = np.random.binomial(1, 0.4)

            # synthetic outcomes
            base_prob_crit_turn = 0.2 + 0.15 * (accountability == "Prompt")
            if sequencing == "Human_first":
                base_prob_crit_turn += 0.05
            if sequencing == "AI_first":
                base_prob_crit_turn -= 0.05

            junior_crit_turn = np.random.binomial(1, base_prob_crit_turn)
            decision_revised = np.random.binomial(1, 0.25 + 0.2 * junior_crit_turn)

            rows.append(
                dict(
                    team_id=team,
                    meeting_id=f"T{team}_M{m}",
                    agenda_item_id=item_id,
                    sequencing=sequencing,
                    accountability=accountability,
                    is_critical=critical,
                    junior_critical_turn=junior_crit_turn,
                    decision_revised=decision_revised,
                )
            )

df_raw = pd.DataFrame(rows)
raw_path.parent.mkdir(parents=True, exist_ok=True)
processed_path.parent.mkdir(parents=True, exist_ok=True)

df_raw.to_csv(raw_path, index=False)

# For now processed = same structure; you can add derived vars later
df_raw.to_csv(processed_path, index=False)

print(f"Saved raw to {raw_path}")
print(f"Saved processed to {processed_path}")

