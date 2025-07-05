from src.generator import generate_population
from src.experiment_engine import run_experiment, TREATMENTS
import pandas as pd
import os

print("Generating population...")
df = generate_population(50)
print("Running experiments...")

experiments = []

for treatment in TREATMENTS:
    result = run_experiment(df, treatment)
    experiments.append(result)

if not experiments:
    print("⚠️ No experiment results generated!")
else:
    all_results = pd.concat(experiments)
    os.makedirs("data", exist_ok=True)
    all_results.to_csv("data/treatment_experiments.csv", index=False)
    print("✅ Data saved to data/treatment_experiments.csv")
    print(all_results.head())
