import pytest
from src.immune_model import simulate_immune_response

# Sample test individual with high baseline
individual_high = {
    "age": 30,
    "medical_history": "None",
    "immune_baseline": 0.9
}

# Sample test individual with cancer history
individual_low = {
    "age": 70,
    "medical_history": "Cancer History",
    "immune_baseline": 0.4
}

def test_response_fields_exist():
    response = simulate_immune_response(individual_high)
    assert "b_cell_response" in response
    assert "t_cell_response" in response
    assert "immune_strength" in response
    assert "outcome" in response

def test_immune_strength_bounds():
    response = simulate_immune_response(individual_high)
    assert 0.0 <= response["immune_strength"] <= 1.0

def test_outcome_classification():
    response = simulate_immune_response(individual_low)
    assert response["outcome"] in ["Strong", "Moderate", "Weak"]

def test_b_and_t_response_range():
    response = simulate_immune_response(individual_high)
    assert 0.0 <= response["b_cell_response"] <= 1.5
    assert 0.0 <= response["t_cell_response"] <= 1.5

