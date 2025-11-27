import pandas as pd
import statsmodels.formula.api as smf

# Load synthetic data
df = pd.read_csv("data/raw/meetings_synthetic_v1.csv")

# Factor dummies
df["AI_first"] = (df["sequencing"] == "AI_first").astype(int)
df["Human_first"] = (df["sequencing"] == "Human_first").astype(int)
df["Accountability_prompt"] = (df["accountability"] == "Prompt").astype(int)

# Simple OLS with team-clustered SEs
model = smf.ols(
    "junior_critical_turn ~ AI_first + Human_first + Accountability_prompt",
    data=df,
).fit(cov_type="cluster", cov_kwds={"groups": df["team_id"]})

print(model.summary())

