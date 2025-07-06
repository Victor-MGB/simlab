import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

sns.set(style="whitegrid")

def plot_treatment_outcomes(df, save_path="plots/treatment_effects.png"):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="treatment", hue="outcome", palette="Set2")
    plt.title("Treatment vs Immune Outcome")
    plt.ylabel("Number of Individuals")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"📊 Saved: {save_path}")

def plot_model_accuracy(df, save_path="plots/model_accuracy.png"):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="actual", hue="predicted", palette="muted")
    plt.title("Model Accuracy: Actual vs Predicted Outcomes")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"📈 Saved: {save_path}")

def plot_clusters(df, save_path="plots/clusters.png"):
    df = df.copy()
    features = df.select_dtypes(include=["number"]).drop(columns=["actual", "predicted"], errors="ignore")
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(scaled)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=reduced[:, 0], y=reduced[:, 1], hue=df.get("actual", None), palette="cool", s=60)
    plt.title("Immune Response Clusters (PCA)")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"🧠 Saved: {save_path}")
