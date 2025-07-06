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

 Example Output Fields (added to CSV)
immune_baseline	b_cell_response	t_cell_response	immune_strength	outcome
0.82	0.79	0.61	0.7	Moderate

 Code Location
Core logic: src/immune_model.py

Simulation applied in: src/main.py



Testing
I use pytest to ensure the immune system simulation code works correctly and reliably.

What is tested?
Correct output fields from the immune response simulation

Immune strength values are within expected bounds (0 to 1)

Proper classification of immune response outcomes (Strong, Moderate, Weak)

B-cell and T-cell response values within plausible ranges

How to run tests
pip install pytest
Run tests from the project root directory:

pytest tests/



 Experiment Engine with Varied Treatments
I’ve implemented an Experiment Engine to test how individuals respond to different treatments such as vaccines, stress, or sleep deprivation.

Each treatment modifies the individual's immune baseline, and i re-run immune simulations to observe changes in:

B-cell and T-cell responses

Immune strength score

Final classification (Strong / Moderate / Weak)
 Treatments Simulated
Treatment	Effect
control	No change
vaccine_boost	Boosts immune response by 20%
sleep_deprivation	Reduces immune response by 15%
anti_inflammatory	Mild immune support (10% boost)
stress	Suppresses immune response by 20%

How to Run All Treatments:
python -m src.main --experiment

This generates a new CSV file:
data/treatment_experiments.csv

| full\_name | treatment          | immune\_strength | outcome  |
| ---------- | ------------------ | ---------------- | -------- |
| Lolita     | control            | 0.62             | Moderate |
| Momčilo    | vaccine\_boost     | 0.81             | Strong   |
| Mitchell   | sleep\_deprivation | 0.47             | Weak     |



I trained a machine learning model (Random Forest) to predict immune response outcomes based on:

Sex

Race/Ethnicity

Medical History

Treatment Type

Immune Baseline

How it Works:
Experimental data from Day 5 is read from data/experiment_results.csv

Categorical features are one-hot encoded

A model is trained and evaluated on accuracy

Predictions and actual outcomes are saved in data/model_predictions.csv

Outputs:
File	Description
experiment_results.csv	All individuals across all treatments
model_predictions.csv	ML predictions vs actual outcomes

 Challenges faced and Resolved:
Handled missing columns in experiment output

Improved error handling in preprocessing

Standardized filenames for smoother automation




Plot Sections

Visualization of Immune Simulation Results: 

For better understanding and communicating the outcome of our simulations and machine learning predictions, we generated the following plots:

1. Treatment vs Outcome:
File: plots/treatment_effects.png
This shows how bar chart display different treatments affected immune system outcomes (e.g. infection cleared vs not cleared).

Useful for visualizing the effectiveness of interventions like vaccine_boost, stress, etc.

2. Model Accuracy – Actual vs Predicted
File: plots/model_accuracy.png
This chart compares the model’s predictions with the true outcomes, helping to evaluate model performance in real-world project.

it is Used to evaluate ML model accuracy and ensure correct predictions across classes.

3. PCA Clustering – Immune Profiles
File: plots/clusters.png
I use PCA (Principal Component Analysis) to reduce immune feature dimensions and plot clusters of individual immune profiles.

Helps identify patterns or subgroups in the population based on immune responses.


The plots was auto-generated when run below:
python -m src.main --experiment --train-model --visualize
