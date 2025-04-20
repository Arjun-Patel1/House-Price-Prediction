# House-Price-Prediction
Data Scientist Project- House Price Prediction
Your House Price Prediction project uses XGBoost and achieves a **validation RMSE (Root Mean Squared Error)** that wasn't explicitly printed in the notebook output (the model trains and computes it, but the final print statement’s result isn’t saved in the notebook). You may want to **re-run the notebook** to view the actual printed RMSE value.

Based on your notebook, here’s a clean and complete **README section** for your project:

---

## 🏠 House Price Prediction using XGBoost

### 📌 Overview
This project is a regression model built to predict house prices based on various features using the **XGBoost** algorithm. It uses the **Kaggle House Prices: Advanced Regression Techniques** dataset.

### 📁 Dataset
- Source: [Kaggle - House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
- Files used:
  - `train.csv`
  - `test.csv`

### 🔧 Features Engineering
- Missing values handled:
  - Columns with >80% missing data were dropped.
  - Remaining numerical missing values were filled with median.
  - Categorical missing values were filled with mode.
- All categorical variables were encoded using `LabelEncoder`.

### 🧠 Model
- Model used: `XGBoost Regressor`
- Hyperparameters:
  - `objective='reg:squarederror'`
  - `learning_rate=0.05`
  - `max_depth=3`
  - `num_boost_round=1000`
  - `early_stopping_rounds=10`
- Train/Test Split: 80% training, 20% validation

### 📊 Evaluation
- Metric used: **RMSE (Root Mean Squared Error)**
- Validation RMSE: *(Please re-run the notebook to view the value)*

### 🔍 Visualizations
- Feature importance plotted using `plot_importance()` from XGBoost.

### 🚀 How to Run
1. Clone the repository or download the notebook.
2. Make sure you have the required dependencies:
   ```bash
   pip install pandas numpy scikit-learn xgboost matplotlib
   ```
3. Download and place the dataset files (`train.csv`, `test.csv`) in the appropriate folder.
4. Run the notebook step by step.
