import pandas as pd
from src.immune_model import simulate_immune_response

# Define example treatments
TREATMENTS = {
    "control": 1.0,
    "vaccine_boost": 1.2,
    "sleep_deprivation": 0.85,
    "anti_inflammatory": 1.1,
    "stress": 0.8,
}

def apply_treatment(individual, multiplier):
    """
    Apply a treatment by adjusting immune baseline temporarily.
    Returns a copy of the individual with adjusted baseline.
    """
    individual_copy = individual.copy()
    adjusted = individual_copy["immune_baseline"] * multiplier
    individual_copy["immune_baseline"] = min(round(adjusted, 2), 1.0)  # Clamp to max 1.0
    return individual_copy

def run_experiment(individuals, treatment_name):
    """
    Apply a treatment to each individual and simulate immune response.
    Returns a DataFrame of results with treatment label and key features.
    """
    multiplier = TREATMENTS.get(treatment_name, 1.0)
    treated_individuals = individuals.to_dict(orient="records")

    results = []
    for person in treated_individuals:
        treated = apply_treatment(person, multiplier)
        response = simulate_immune_response(treated)

        # Include all necessary ML features in the response
        response.update({
            "treatment": treatment_name,
            "full_name": person.get("full_name", ""),
            "sex": person.get("sex", ""),
            "race_ethnicity": person.get("race_ethnicity", ""),
            "medical_history": person.get("medical_history", "")
        })

        results.append(response)

    return pd.DataFrame(results)
