import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def prepare_data(df):
    """
    Prepares data for ML by encoding categorical features and selecting input/output columns.
    """
    required_cols = ["sex", "race_ethnicity", "medical_history", "treatment"]

    # Ensure required columns exist
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.copy()
    df = pd.get_dummies(df, columns=required_cols, drop_first=True)

    # Safe drop of unused text columns
    X = df.drop(columns=["full_name", "email", "location", "outcome"], errors="ignore")
    y = df["outcome"]

    return train_test_split(X, y, test_size=0.3, random_state=42)

def train_and_evaluate_models(df, output_path="data/model_predictions.csv"):
    """
    Train and evaluate ML models and optionally save test predictions.
    """
    X_train, X_test, y_train, y_test = prepare_data(df)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("\nResults for Random Forest")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
    print(classification_report(y_test, predictions))

    # Save predictions
    results_df = X_test.copy()
    results_df["actual"] = y_test
    results_df["predicted"] = predictions
    results_df.to_csv(output_path, index=False)
    print(f"Saved model predictions to {output_path}")
