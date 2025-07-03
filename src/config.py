import random

# Configuration settings
N_USERS = 50
OUTPUT_FILE = "data/synthetic_population.csv"
RACES = ["Black", "White", "Asian", "Hispanic", "Mixed", "Other"]
MEDICAL_CONDITIONS = [
    "None", "Diabetes", "Hypertension", "Asthma", "Allergy", "Cancer History", "Immunodeficiency"
]

# Fix random seed for reproducibility
random.seed(42)
