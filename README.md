# Airline_Profit_Prediction
# Profit Prediction Model

## \ud83d\udccc Project Overview

This project builds a **profit prediction model** using **machine learning** techniques to estimate the profit of an airline based on key operational and financial parameters. The model is trained on historical data and deployed as a **Streamlit web application** for user interaction.

---

## \ud83d\udd39 Steps in the Project

### 1\ufe0f\u20e3 Data Collection & Preprocessing

- Load the dataset containing financial and operational parameters.
- Handle missing values and outliers.
- Normalize/scale numerical features using **StandardScaler**.
- Perform **Principal Component Analysis (PCA)** for dimensionality reduction (optional).
- Save important files:
  - `original_feature_columns.pkl` (for consistent feature order)
  - `scaler.pkl` (for standardization)
  - `pca.pkl` (if PCA is applied)
  - `full_pipeline.pkl` (if using a complete preprocessing pipeline)

---

### 2\ufe0f\u20e3 Model Selection & Training

- Train multiple regression models:
  - **Multi-Layer Perceptron (MLPRegressor)**
  - **Histogram-Based Gradient Boosting (HistGradientBoosting)**
  - **LightGBM (LGBMRegressor)**
- Save trained models:
  - `MLPRegressor_pipeline.pkl`
  - `HistGradientBoosting_pipeline.pkl`
  - `LGBM_pipeline.pkl`

---

### 3\ufe0f\u20e3 Building the Streamlit App

- Load saved models, scaler, and PCA (if applicable).
- Create a user-friendly **Streamlit** interface for input fields.
- Ensure input feature alignment with `original_feature_columns.pkl`.
- Apply the preprocessing pipeline before making predictions.
- Display predicted profit values from each model.

---

## \ud83d\ude80 Running the Project

### 1\ufe0f\u20e3 Install Dependencies

```sh
pip install -r requirements.txt
```

### 2\ufe0f\u20e3 Run the Streamlit App

```sh
streamlit run app.py
```

---

## \ud83d\udc82\u200d\u2642\ufe0f Power BI Dashboard

A **Power BI dashboard** was created to visualize key airline performance metrics, providing insights into financial and operational efficiency. The dashboard includes:

- **Average of Delay (Minutes) by Flight Number**: Identifies the most and least punctual flights.
- **Average of Aircraft Utilization (Hours/Day) by Quarter**: Analyzes aircraft usage trends across different time periods.
- **Sum of Revenue (USD) by Quarter**: Tracks revenue trends over the year.
- **Sum of Net Profit Margin (%) by Flight Number**: Highlights the profitability of different flights.
- **Sum of Revenue (USD), Sum of Profit (USD), and Sum of Operating Cost (USD) by Month**: Compares revenue, profit, and operating costs to assess financial stability.
- **Sum of Revenue (USD), Sum of Profit (USD), and Sum of Operating Cost (USD) by Quarter**: Provides a broader financial overview.

---

## \ud83d\udcc2 Project Structure

```
\ud83d\udcc2 Profit-Prediction-Project
│── app.py                         # Streamlit application
│── original_feature_columns.pkl   # Feature alignment file
│── full_pipeline.pkl              # Full preprocessing pipeline
│── scaler.pkl                     # StandardScaler model
│── pca.pkl                        # PCA model (if used)
│── MLPRegressor_pipeline.pkl      # MLP Regression Model
│── HistGradientBoosting_pipeline.pkl  # HistGradientBoosting Model
│── LGBM_pipeline.pkl              # LightGBM Model
│── requirements.txt               # Dependencies list
│── PowerBI_Dashboard.pbix         # Power BI Dashboard file
│── README.md                      # Project documentation
```

---

## \ud83d\udcca Results & Insights

- The model successfully predicts airline profits based on financial and operational metrics.
- **LightGBM performed best** with the highest accuracy.
- **Feature engineering and scaling played a crucial role** in improving model performance.
- The **Streamlit interface** makes it easy to input values and get predictions in real-time.
- The **Power BI dashboard** provides key business insights for strategic decision-making.

---

## \ud83d\udee0 Future Improvements

✅ Add more models and compare results.\
✅ Deploy the app using **Streamlit Cloud** or **Heroku**.\
✅ Enhance UI with interactive visualizations.\
✅ Automate feature selection using **SHAP** or **Feature Importance**.\
✅ Improve **Power BI Dashboard** with real-time data integration.

---

## \u2728 Contributors

- **Your Name** *(Data Analyst & Developer)*

\ud83d\udccc Feel free to contribute or raise issues! \ud83d\ude80

