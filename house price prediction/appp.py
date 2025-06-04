import streamlit as st
import pandas as pd
import xgboost as xgb
import joblib

# ---- Load the Full Trained Model ----
# This model is trained on all features.
model = joblib.load("house_price_model.pkl")

# ---- Retrieve Expected Feature Names ----
# If your model stores feature names, use them.
# Otherwise, hard-code the full list based on your training.
try:
    expected_features = model.feature_names
except AttributeError:
    expected_features = [
        'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
        'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope',
        'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
        'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle',
        'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea',
        'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond',
        'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2',
        'BsmtUnfSF', 'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir',
        'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
        'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
        'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces',
        'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars',
        'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF',
        'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea',
        'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition'
    ]

# ---- App Title and Introduction ----
st.title("House Price Prediction")
st.write(
    """
    This web app estimates the sale price of a house using an XGBoost model.
    The model was trained on many features. Here, you only enter a few key details;
    all other features use default values (currently set to 0).  
    (For better accuracy, consider using median values from training data as defaults.)
    """
)

# ---- Sidebar: Collect Key Input Features ----
st.sidebar.header("Enter Key House Details")

OverallQual = st.sidebar.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
GrLivArea = st.sidebar.number_input("Above Ground Living Area (sqft)", value=1500)
GarageCars = st.sidebar.number_input("Garage Cars", min_value=0, max_value=5, value=2)
TotalBsmtSF = st.sidebar.number_input("Total Basement Area (sqft)", value=1000)
YearBuilt = st.sidebar.number_input("Year Built", min_value=1900, max_value=2025, value=2000)

# Prepare a dictionary of the key user inputs
key_inputs = {
    "OverallQual": OverallQual,
    "GrLivArea": GrLivArea,
    "GarageCars": GarageCars,
    "TotalBsmtSF": TotalBsmtSF,
    "YearBuilt": YearBuilt
}

# ---- Build a Full Input Dictionary with Defaults ----
# We create an entry for every expected feature and set a default (0 in this example).
full_input = {feature: 0 for feature in expected_features}

# Update the full dictionary with the values provided by the user for the key features.
for feature, value in key_inputs.items():
    if feature in full_input:
        full_input[feature] = value

# Create a DataFrame with the columns ordered exactly as expected by the model.
input_df = pd.DataFrame([full_input], columns=expected_features)

# ---- Prediction Button ----
if st.button("Predict House Price"):
    # Convert DataFrame input to an XGBoost DMatrix
    dmatrix = xgb.DMatrix(input_df)
    prediction = model.predict(dmatrix)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
