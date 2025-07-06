import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Page Setup
st.set_page_config(layout="wide")
st.title(" Immune Simulation Tech Dashboard")
st.markdown("Explore synthetic population, experiments, and ML predictions with interactive charts.")

# Load all datasets
@st.cache_data
def load_data():
    try:
        synthetic = pd.read_csv("data/synthetic_population.csv")
        experiment = pd.read_csv("data/experiment_results.csv")
        model = pd.read_csv("data/model_predictions.csv")
        return synthetic, experiment, model
    except Exception as e:
        st.error(f"⚠️ Error loading datasets: {e}")
        return None, None, None

synthetic_df, exp_df, pred_df = load_data()

# Tabs for navigation
tabs = st.tabs([" Synthetic Population", "Experiments", "Model Predictions"])

# --- Tab 1: Synthetic Population ---
# ---  Tab 1: Synthetic Population ---
with tabs[0]:
    st.header(" Synthetic Population Overview")

    if synthetic_df is not None:
        # Sidebar filters
        with st.sidebar:
            st.subheader(" Population Filters")
            selected_condition = st.selectbox("Medical History", ["All"] + synthetic_df["medical_history"].unique().tolist())
            st.markdown("---")
            st.subheader(" View Individual Profile")
            selected_user = st.selectbox("Select User", synthetic_df["full_name"].tolist())

        # Filter by medical condition
        filtered = synthetic_df.copy()
        if selected_condition != "All":
            filtered = filtered[filtered["medical_history"] == selected_condition]

        st.markdown("###  Immune Strength Distribution")
        fig, ax = plt.subplots()
        sns.histplot(filtered["immune_baseline"], kde=True, ax=ax)
        st.pyplot(fig)

        st.markdown("###  Synthetic Population Data")
        st.dataframe(filtered)

        # User Profile Display
        st.markdown("---")
        st.markdown("###  Selected User Profile")

        user = synthetic_df[synthetic_df["full_name"] == selected_user].iloc[0]
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(user["image_url"], caption=user["full_name"], width=160)

        with col2:
            st.markdown(f"""
                **Full Name:** {user['full_name']}  
                **Age:** {user['age']}  
                **Sex:** {user['sex'].capitalize()}  
                **Location:** {user['location']}  
                **Medical History:** {user['medical_history']}  
                **Immune Baseline:** {user['immune_baseline']}  
                **Email:** {user['email']}
            """)

    else:
        st.warning("Synthetic data not available.")

# ---  Tab 2: Experiments ---
with tabs[1]:
    st.header("Immune Treatment Experiments")

    if exp_df is not None:
        with st.sidebar:
            st.subheader(" Experiment Filters")
            treatments = st.multiselect("Treatment", exp_df['treatment'].unique(), default=exp_df['treatment'].unique())
            outcomes = st.multiselect("Outcome", exp_df['outcome'].unique(), default=exp_df['outcome'].unique())

        filtered_exp = exp_df[(exp_df['treatment'].isin(treatments)) & (exp_df['outcome'].isin(outcomes))]

        st.markdown("###  Outcome by Treatment")
        fig1, ax1 = plt.subplots(figsize=(10, 4))
        sns.countplot(data=filtered_exp, x="treatment", hue="outcome", palette="Set2", ax=ax1)
        st.pyplot(fig1)

        st.markdown("###  Data Table")
        st.dataframe(filtered_exp)
    else:
        st.warning("Experiment results not available.")

# ---  Tab 3: ML Model Predictions ---
with tabs[2]:
    st.header(" ML Model: Actual vs Predicted")

    if pred_df is not None:
        st.markdown("###  Accuracy Comparison")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.countplot(data=pred_df, x="actual", hue="predicted", palette="muted", ax=ax2)
        st.pyplot(fig2)

        st.markdown("###  PCA Clustering of Immune Profiles")
        features = pred_df.select_dtypes(include="number").drop(columns=["actual", "predicted"], errors="ignore")
        scaled = StandardScaler().fit_transform(features)
        pca = PCA(n_components=2).fit_transform(scaled)
        pca_df = pd.DataFrame(pca, columns=["PC1", "PC2"])
        pca_df["actual"] = pred_df["actual"].values

        fig3, ax3 = plt.subplots(figsize=(8, 4))
        sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="actual", palette="cool", ax=ax3)
        st.pyplot(fig3)

        st.markdown("###  Prediction Data")
        st.dataframe(pred_df.head(100))
    else:
        st.warning("Model prediction data not available.")
