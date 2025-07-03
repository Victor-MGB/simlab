# SimLab: In-Silico Immune System Experiments

SimLab is a Python-based simulation engine for immune system modeling. It enables reproducible, keyboard-driven experiments using synthetic populations varied by age, sex, race, and medical history.

## Features
- Generate synthetic biological populations
- Simulate immune responses to treatments
- Run repeated experiments
- Analyze outcomes with ML models
- Optional dashboard for visualization

## Folder Structure
- `src/`: Python modules
- `notebooks/`: Jupyter development files
- `data/`: Synthetic and processed datasets
- `results/`: Simulation outputs
- `app/`: Streamlit dashboard (optional)

## Getting Started
pip install -r requirements.txt




## GitHub Setup

1. Go to [https://github.com/new](https://github.com/new)
2. Name the repo `simlab`
3. Don’t initialize with README (we already did)
4. Choose **MIT License**
5. Click **Create Repository**
6. Then follow the instructions it gives to push your local files:

git init
git remote add origin https://github.com/YOUR_USERNAME/simlab.git
git add .
git commit -m "Initial project structure setup"
git push -u origin main


 Day 2 – Synthetic Population Generator

Python-based population generator that uses the public **[Random User API](https://randomuser.me)** to fetch realistic user profiles, and enriches them with:

- **Race/Ethnicity** (randomized from a list)
- **Medical history** (mocked conditions)
- **Immune baseline scores** (random float between 0.3 and 1.0)
- **Profile picture URL** (realistic image link from API)

The result is a rich, diverse, synthetic population that mimics real-world data across demographic and health factors.

###  Example Output Fields

| full_name | age | sex | race_ethnicity | email | location | medical_history | immune_baseline | image_url |
|-----------|-----|-----|----------------|-------|----------|------------------|------------------|------------|
| Jane Doe  | 34  | female | Asian | jane@example.com | Tokyo, Japan | Asthma | 0.78 | `https://randomuser.me/api/portraits/men/84.jpg` |


 How to Run:
 python -m src.main



  Day 3 – Immune System Simulation (B/T Cell Model)
Built a simulation engine that models how each synthetic individual responds to infection using a simplified version of real-world immune response logic.

Each individual’s response is based on:

Immune baseline score

Age-related immune decline

Medical history (e.g. immunodeficiency, cancer)

The model computes:

B-cell response (antibody production)

T-cell response (cell-mediated immunity)

Immune strength score (0.0 to 1.0)

Outcome classification (Strong, Moderate, Weak)

🔬 Example Output Fields (added to CSV)
immune_baseline	b_cell_response	t_cell_response	immune_strength	outcome
0.82	0.79	0.61	0.7	Moderate

⚙️ Code Location
Core logic: src/immune_model.py

Simulation applied in: src/main.py