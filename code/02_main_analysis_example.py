import pandas as pd
import statsmodels.formula.api as smf

# Load synthetic data
df = pd.read_csv("data/raw/meetings_synthetic_v1.csv")

# Create dummies for sequencing and accountability
df["ai_first"] = (df["sequencing"] == "AI_first").astype(int)
df["human_first"] = (df["sequencing"] == "Human_first").astype(int)
df["accountability_prompt"] = (df["accountability"] == "Prompt").astype(int)

# Simple linear model: junior critical turn as outcome
model = smf.ols(
    "junior_critical_turn ~ ai_first + human_first + accountability_prompt",
    data=df
).fit(cov_type="cluster", cov_kwds={"groups": df["team_id"]})

print(model.summary())

