import streamlit as st
import joblib
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.exceptions import NotFittedError
from sklearn.utils.validation import check_is_fitted

# 🔹 Load Trained Pipelines
st.sidebar.header("📂 Model Loading...")

try:
    mlp_pipeline = joblib.load("MLPRegressor_pipeline.pkl")  # MLP with Scaler
    HistGradientBoosting_pipeline_model = joblib.load("HistGradientBoosting_pipeline.pkl")  # Standalone Model
    LGBM_pipeline_model = joblib.load("LGBM_pipeline.pkl")  # Standalone Model
    st.sidebar.success("✅ Models Loaded Successfully!")
except FileNotFoundError:
    st.sidebar.error("❌ Model files not found! Ensure they are in the directory.")
    mlp_pipeline, extra_trees_model, random_forest_model = None, None, None

# 🔹 Load Scaler (if available)
scaler = None
try:
    scaler = joblib.load("scaler.pkl")  # Ensure it is a StandardScaler object
    check_is_fitted(scaler)  # Verify it is properly fitted
    st.sidebar.success("✅ Scaler is fitted and ready to use!")
except FileNotFoundError:
    st.sidebar.warning("⚠️ No scaler found! Predictions might be inaccurate.")
except NotFittedError:
    st.sidebar.error("❌ Scaler is not fitted! Please fit and save it again.")
    scaler = None  # Reset to None

# 🔹 Load PCA (if used)
pca = None
try:
    pca = joblib.load("pca.pkl")  # Ensure PCA model is loaded correctly
    st.sidebar.success("✅ PCA model loaded!")
except FileNotFoundError:
    st.sidebar.warning("⚠️ No PCA model found!")

# Feature Names (used in training)
feature_columns = [
    "Delay (Minutes)", "Aircraft Utilization (Hours/Day)", "Turnaround Time (Minutes)",
    "Load Factor (%)", "Fleet Availability (%)", "Maintenance Downtime (Hours)",
    "Fuel Efficiency (ASK)", "Revenue (USD)", "Operating Cost (USD)",
    "Ancillary Revenue (USD)", "Debt-to-Equity Ratio", "Departure Month"
]

# Set the title of the app
st.title("💰 Profit Prediction App")

st.subheader("🔹 Enter Business Metrics Manually")
col1, col2 = st.columns(2)

with col1:
    delay = st.number_input("Delay (Minutes)", value=0.0, format="%.2f")
    utilization = st.number_input("Aircraft Utilization (Hours/Day)", value=0.0, format="%.2f")
    turnaround = st.number_input("Turnaround Time (Minutes)", value=0.0, format="%.2f")
    load_factor = st.number_input("Load Factor (%)", value=0.0, format="%.2f")
    fleet_availability = st.number_input("Fleet Availability (%)", value=0.0, format="%.2f")
    maintenance = st.number_input("Maintenance Downtime (Hours)", value=0.0, format="%.2f")

with col2:
    fuel_efficiency = st.number_input("Fuel Efficiency (ASK)", value=0.0, format="%.2f")
    revenue = st.number_input("Revenue (USD)", value=0.0, format="%.2f")
    operating_cost = st.number_input("Operating Cost (USD)", value=0.0, format="%.2f")
    ancillary_revenue = st.number_input("Ancillary Revenue (USD)", value=0.0, format="%.2f")
    debt_equity = st.number_input("Debt-to-Equity Ratio", value=0.0, format="%.2f")
    departure_month = st.number_input("Departure Month", value=1, min_value=1, max_value=12, step=1)

# Convert input to NumPy array
input_data = np.array([
    delay, utilization, turnaround, load_factor, fleet_availability, maintenance,
    fuel_efficiency, revenue, operating_cost, ancillary_revenue, debt_equity, departure_month
]).reshape(1, -1)

# 🚀 Predict Button
if st.button("🔍 Predict Profit"):
    st.subheader("📊 Profit Predictions")

    # Apply Scaler if available
    if scaler is not None:
        try:
            input_data = scaler.transform(input_data)
        except NotFittedError:
            st.sidebar.error("❌ Scaler is not fitted! Predictions might be inaccurate.")

    # Apply PCA if available
    if pca is not None:
        input_data = pca.transform(input_data)

    # Make Predictions
    pred_mlp = mlp_pipeline.predict(input_data)[0] if mlp_pipeline is not None else None
    pred_hist = HistGradientBoosting_pipeline_model.predict(input_data)[0] if HistGradientBoosting_pipeline_model is not None else None
    pred_lgbm = LGBM_pipeline_model.predict(input_data)[0] if LGBM_pipeline_model is not None else None

    # Display Predictions
    if pred_mlp is not None:
        st.write("💵 **MLP Regressor Predicted Profit (USD):**", round(pred_mlp, 2))
    else:
        st.write("⚠️ **MLP Regressor Model Not Loaded!**")

    if pred_hist is not None:
        st.write("💵 **HistGradient Boosting Predicted Profit (USD):**", round(pred_hist, 2))
    else:
        st.write("⚠️ **HistGradient Boosting Model Not Loaded!**")

    if pred_lgbm is not None:
        st.write("💵 **LGBM Predicted Profit (USD):**", round(pred_lgbm, 2))
    else:
        st.write("⚠️ **LGBM Model Not Loaded!**")

st.write("🚀 Ready to Predict! Enter values and click **Predict Profit**.")
