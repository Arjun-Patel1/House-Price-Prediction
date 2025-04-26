🏡 House Price Prediction using XGBoost
📚 Project Overview
This project aims to predict house prices based on various features like lot size, year built, overall material quality, and more.
We used the famous House Prices - Advanced Regression Techniques dataset from Kaggle and built a regression model using XGBoost — one of the most powerful machine learning algorithms for structured/tabular data.

The final model achieved an excellent Validation R² Score of 91.82% and a Validation RMSE of 25,052.45!

📂 Dataset
Training Data: train.csv

Testing Data: test.csv

Features include numeric and categorical data related to properties (e.g., area, year, quality ratings).

Target variable: SalePrice

🛠️ Steps Followed
Import Libraries: Loaded essential libraries such as pandas, numpy, sklearn, xgboost, and matplotlib.

Load Dataset: Imported the training and testing data.

Data Preprocessing:

Dropped columns with more than 80% missing values.

Handled missing values:

Filled categorical columns with the mode.

Filled numerical columns with the median.

Label Encoded all categorical variables.

Train-Validation Split:

Split the data into training and validation sets (80/20 split).

Model Training:

Created DMatrix for efficient computation.

Tuned hyperparameters like learning_rate, max_depth, min_child_weight, gamma, subsample, colsample_bytree.

Used early stopping to avoid overfitting.

Model Evaluation:

Calculated RMSE and R² Score on the validation set.

Feature Importance:

Plotted the top 10 important features influencing house prices.

📈 Final Model Performance

Metric	Score
Validation RMSE	25,052.45
Validation R²	0.9182 (91.82% Accuracy)
🔥 Key Libraries Used
pandas: Data loading and manipulation

numpy: Mathematical operations

scikit-learn: Data preprocessing and evaluation metrics

xgboost: Machine learning model

matplotlib: Visualization

