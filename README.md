# 🏡 House Price Prediction using XGBoost & Streamlit

## Project Overview

This project leverages the **House Prices - Advanced Regression Techniques** dataset from Kaggle to predict the sale price of a house based on numerous property features. Initially, an XGBoost regression model was developed and evaluated, achieving excellent performance. The repository has since evolved to include an interactive **Streamlit web application** that lets users input a few key features, while default values fill in the remaining features expected by the model. 

**Key Performance Metrics:**
- **Validation R² Score:** 91.82%
- **Validation RMSE:** 25,052.45

---

## Dataset Details

- **Training Data:** `train.csv`
- **Testing Data:** `test.csv`
- **Target Variable:** `SalePrice`
- **Features:** A mix of numerical and categorical data (e.g., area, year built, quality ratings, etc.)

---

## Project Workflow

### 1. Data Preprocessing & Model Training

- **Import Libraries:**  
  Utilized key libraries such as `pandas`, `numpy`, `scikit-learn`, `xgboost`, and `matplotlib` for data processing, modeling, and visualizations.

- **Data Cleaning & Preprocessing:**  
  - Dropped columns with more than 80% missing values.  
  - Handled missing values by filling categorical features with the mode and numerical features with the median.  
  - Applied Label Encoding to transform categorical variables.

- **Train-Validation Split:**  
  Data was divided into an 80/20 train-validation split.

- **Model Training:**  
  Constructed training and validation sets using XGBoost’s `DMatrix`. Key hyperparameters such as `learning_rate`, `max_depth`, `min_child_weight`, `gamma`, `subsample`, and `colsample_bytree` were tuned, with early stopping implemented to avoid overfitting.

- **Model Evaluation:**  
  Evaluated using RMSE and R², and analyzed feature importance using XGBoost's visualization tools.

---

### 2. Enhancing Accessibility with a Web App (New Update!)

To make the model accessible and user-friendly, a **Streamlit web application** was developed with the following features:

- **Interactive User Interface:**  
  Users provide key property details (e.g., Overall Quality, Above Ground Living Area, Garage Cars, Total Basement Area, Year Built) via an intuitive sidebar.

- **Full-Model Integration:**  
  The original model was trained on a comprehensive set of features. For web app predictions, a full feature vector is constructed by filling unprovided inputs with default values (currently set to 0, though these can be updated to more representative medians).

- **Real-Time Predictions:**  
  Upon clicking the "Predict House Price" button, the app converts user input to the expected format, passes it to the XGBoost model, and displays the estimated sale price.

- **Running the App:**  
  The app can be launched locally using the command `streamlit run appp.py`.

---

## How to Run the Project Locally

### Clone the Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction


