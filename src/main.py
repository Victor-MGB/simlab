import os
import argparse
import logging
import pandas as pd
from src.generator import generate_population
from src.immune_model import simulate_immune_response
from src.experiment_engine import run_experiment, TREATMENTS
from src.ml_model import train_and_evaluate_models
from src.visualize import plot_treatment_outcomes, plot_model_accuracy, plot_clusters
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

def run_visualizations():
    os.makedirs("plots", exist_ok=True)
    experiment_df = pd.read_csv("data/experiment_results.csv")
    model_df = pd.read_csv("data/model_predictions.csv")

    logging.info("Generating plots...")
    plot_treatment_outcomes(experiment_df)
    plot_model_accuracy(model_df)
    plot_clusters(model_df)
    logging.info("Plots saved in /plots")

def main(n, output, run_experiments=False, train_model=False, generate_plots=False):
    logging.info(f"Generating {n} synthetic individuals...")
    df = generate_population(n)

    if run_experiments:
        logging.info("Running experiments with treatments...")
        experiments = []
        for treatment in TREATMENTS:
            result = run_experiment(df, treatment)
            experiments.append(result)
        all_results = pd.concat(experiments)
        save_population(all_results, "data/experiment_results.csv")
        logging.info("All treatment simulations completed and saved.")
    else:
        logging.info("Running standard immune simulations...")
        df = run_simulations(df)
        save_population(df, output)
        logging.info("Standard simulation completed and saved.")

    if train_model:
        logging.info("Training ML model on experimental data...")
        df = pd.read_csv("data/experiment_results.csv")
        train_and_evaluate_models(df, output_path="data/model_predictions.csv")

    if generate_plots:
        run_visualizations()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synthetic Immune System Simulation Project")
    parser.add_argument("--n", type=int, default=50, help="Number of individuals to generate")
    parser.add_argument("--output", type=str, default=OUTPUT_FILE, help="Output CSV file path")
    parser.add_argument("--experiment", action='store_true', help="Run experiments with treatments")
    parser.add_argument("--train-model", action='store_true', help="Train ML model on experiment data")
    parser.add_argument("--visualize", action='store_true', help="Generate plots and visualizations")

    args = parser.parse_args()
    main(args.n, args.output, args.experiment, args.train_model, args.visualize)
