# Airline_Profit_Prediction

## 📌 Project Overview

This project builds a **profit prediction model** using **machine learning** techniques to estimate the profit of an airline based on key operational and financial parameters. The model is trained on historical data and deployed as a **Streamlit web application** for user interaction.

---

## 🔹 Steps in the Project

### 1️⃣ Data Collection & Preprocessing

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

### 2️⃣ Model Selection & Training

- Train multiple regression models:
  - **Multi-Layer Perceptron (MLPRegressor)**
  - **Histogram-Based Gradient Boosting (HistGradientBoosting)**
  - **LightGBM (LGBMRegressor)**
- Save trained models:
  - `MLPRegressor_pipeline.pkl`
  - `HistGradientBoosting_pipeline.pkl`
  - `LGBM_pipeline.pkl`

---

### 3️⃣ Building the Streamlit App

- Load saved models, scaler, and PCA (if applicable).
- Create a user-friendly **Streamlit** interface for input fields.
- Ensure input feature alignment with `original_feature_columns.pkl`.
- Apply the preprocessing pipeline before making predictions.
- Display predicted profit values from each model.

---

## 🚀 Running the Project
---
![Image](https://github.com/user-attachments/assets/096df987-8c4e-4275-a4a7-7338814fb232)
---
### 1️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit App

```sh
streamlit run app.py
```

---

## 📂 Project Structure

```
📂 Profit-Prediction-Project
│── app.py                         # Streamlit application
│── original_feature_columns.pkl   # Feature alignment file
│── full_pipeline.pkl              # Full preprocessing pipeline
│── scaler.pkl                     # StandardScaler model
│── pca.pkl                        # PCA model (if used)
│── MLPRegressor_pipeline.pkl      # MLP Regression Model
│── HistGradientBoosting_pipeline.pkl  # HistGradientBoosting Model
│── LGBM_pipeline.pkl              # LightGBM Model
│── requirements.txt               # Dependencies list
│── README.md                      # Project documentation
```

---

## 📈 Power BI Dashboard

The **Power BI Dashboard** provides interactive visualizations for analyzing key airline performance metrics:

- **Average Delay (Minutes) by Flight Number**
- **Average Aircraft Utilization (Hours/Day) by Quarter**
- **Sum of Revenue (USD) by Quarter**
- **Sum of Net Profit Margin (%) by Flight Number**
- **Sum of Revenue (USD), Sum of Profit (USD), and Sum of Operating Cost (USD) by Month**
- **Sum of Revenue (USD), Sum of Profit (USD), and Sum of Operating Cost (USD) by Quarter**

These insights help in identifying patterns, optimizing airline operations, and improving profitability.

---

![Image](https://github.com/user-attachments/assets/25729543-cc58-4763-b892-24918c6bb18d)

---

## 📈 Results & Insights

- The model successfully predicts airline profits based on financial and operational metrics.
- **MLPRegressor, HistGradientBoosting & LightGBM performed best** with the highest accuracy.
- **Feature engineering and scaling played a crucial role** in improving model performance.
- The **Streamlit interface** makes it easy to input values and get predictions in real-time.

---

## 🛠 Future Improvements

✅ Add more models and compare results.\
✅ Deploy the app using **Streamlit Cloud** .\
✅ Enhance UI with interactive visualizations.\

---

📌 Feel free to contribute or raise issues! 🚀

