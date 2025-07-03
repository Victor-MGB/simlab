import os
import argparse
import logging
import pandas as pd
from src.generator import generate_population
from src.immune_model import simulate_immune_response
from src.config import OUTPUT_FILE

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def save_population(df, filename):
    """
    Save the synthetic population to a CSV file.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    logging.info(f"Saved {len(df)} records to {filename}")

def run_simulations(df):
    """
    Run immune simulations for each individual in the DataFrame.
    Adds results as new columns.
    """
    responses = df.apply(simulate_immune_response, axis=1, result_type='expand')
    return pd.concat([df, responses], axis=1)

def main(n, output):
    """
    Main function to generate and save the population with simulation results.
    """
    logging.info(f"Generating {n} synthetic individuals...")
    df = generate_population(n)
    df = run_simulations(df)
    save_population(df, output)
    logging.info("Simulation complete. File saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synthetic Population + Immune Simulation")
    parser.add_argument("--n", type=int, default=50, help="Number of individuals to generate")
    parser.add_argument("--output", type=str, default=OUTPUT_FILE, help="Output CSV file path")
    args = parser.parse_args()

    main(args.n, args.output)
