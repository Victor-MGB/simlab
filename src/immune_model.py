import math
import random

def simulate_immune_response(individual):
    """
    Simulate B-cell and T-cell immune response to an infection for a single individual.
    Returns a dictionary with immune scores and infection outcome.
    """
    # Extract relevant features
    baseline = individual["immune_baseline"]
    age = individual["age"]
    history = individual["medical_history"]

    # Simulate B-cell response (antibody production)
    b_cell_response = baseline * random.uniform(0.7, 1.1)

    # Age penalty: older individuals typically have slower T-cell activation
    age_factor = 1 - (max(age - 40, 0) / 100)  # Reduce after age 40

    # Simulate T-cell response (clearing infected cells)
    t_cell_response = baseline * age_factor * random.uniform(0.6, 1.0)

    # History penalty (if immunocompromised or chronic illness)
    penalty = 0.1 if history in ["Cancer History", "Immunodeficiency"] else 0.0

    # Final immune response score
    immune_strength = (b_cell_response + t_cell_response) / 2 - penalty
    immune_strength = max(0, min(round(immune_strength, 2), 1))  # Clamp between 0–1

    # Outcome classification
    if immune_strength >= 0.75:
        outcome = "Strong"
    elif immune_strength >= 0.5:
        outcome = "Moderate"
    else:
        outcome = "Weak"

    return {
        "b_cell_response": round(b_cell_response, 2),
        "t_cell_response": round(t_cell_response, 2),
        "immune_strength": immune_strength,
        "outcome": outcome
    }
