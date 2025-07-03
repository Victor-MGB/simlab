import requests
import pandas as pd
import random
from src.config import RACES, MEDICAL_CONDITIONS

def fetch_users(n=50):
    """
    Fetch synthetic users from Random User API.
    """
    url = f"https://randomuser.me/api/?results={n}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["results"]

def generate_population(n=50):
    """
    Generate synthetic population with random attributes and immune baseline.
    """
    raw_users = fetch_users(n)
    population = []

    for user in raw_users:
        record = {
            "full_name": f"{user['name']['first']} {user['name']['last']}",
            "age": user['dob']['age'],
            "sex": user['gender'],
            "race_ethnicity": random.choice(RACES),
            "email": user['email'],
            "location": f"{user['location']['city']}, {user['location']['country']}",
            "medical_history": random.choice(MEDICAL_CONDITIONS),
            "immune_baseline": round(random.uniform(0.3, 1.0), 2),
            "image_url": user['picture']['large'],
        }
        population.append(record)

    return pd.DataFrame(population)
