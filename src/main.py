import os
import argparse
import logging
import pandas as pd
from src.ml_model import train_and_evaluate_models
from src.generator import generate_population
from src.immune_model import simulate_immune_response
from src.experiment_engine import run_experiment, TREATMENTS
from src.config import OUTPUT_FILE

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def save_population(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    logging.info(f"Saved {len(df)} records to {filename}")

def run_simulations(df):
    responses = df.apply(simulate_immune_response, axis=1, result_type='expand')
    return pd.concat([df, responses], axis=1)

def main(n, output, run_experiments=False):
    logging.info(f"Generating {n} synthetic individuals...")
    df = generate_population(n)

    if run_experiments:
        logging.info("Running experiments with treatments...")
        experiments = []
        for treatment in TREATMENTS:
            result = run_experiment(df, treatment)
            experiments.append(result)
        all_results = pd.concat(experiments)
        experiment_path = "data/experiment_results.csv"
        save_population(all_results, experiment_path)
        logging.info("All treatment simulations completed and saved.")
        return experiment_path  # Return path to file for ML use
    else:
        logging.info("Running standard immune simulations...")
        df = run_simulations(df)
        save_population(df, output)
        logging.info("Standard simulation completed and saved.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synthetic Population + Immune Simulation")
    parser.add_argument("--n", type=int, default=50, help="Number of individuals to generate")
    parser.add_argument("--output", type=str, default=OUTPUT_FILE, help="Output CSV file path")
    parser.add_argument("--experiment", action='store_true', help="Run experiments with treatments")
    parser.add_argument("--train-model", action='store_true', help="Train ML model on experiment data")

    args = parser.parse_args()
    
    # 👇 Run main and get path to experiment file if applicable
    experiment_file = main(args.n, args.output, args.experiment)

    # 👇 Train ML model only if experiment was run and model training was requested
    if args.train_model and experiment_file:
        logging.info("Training ML model on experimental data...")
        df = pd.read_csv(experiment_file)
        train_and_evaluate_models(df, output_path="data/model_predictions.csv")
