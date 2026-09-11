# 🏠 House Price Prediction using Linear Regression

A beginner-friendly machine learning project that predicts house prices using Linear Regression based on property features such as area, bedrooms, bathrooms, parking, location, and age.

## 📌 Project Objective

The objective is to build a regression model that learns the relationship between house features and their selling price, then uses that relationship to predict the price of a new house.

## 🧠 Machine Learning Workflow

```text
Dataset → Data Loading → Cleaning & Preprocessing → Categorical Encoding → Feature Scaling → Train/Test Split → Linear Regression → Evaluation → Prediction
```

## 📊 Features

| Feature | Description |
|---|---|
| area_sqft | House area in square feet |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| stories | Number of floors |
| parking | Number of parking spaces |
| location | Urban, Suburban or Rural |
| age_years | Approximate age of the house |
| price | Target house price |

## 🛠️ Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Joblib
- Jupyter Notebook

## 🚀 How to Run

```bash
git clone https://github.com/omprakashkavre02-oss/om.git
cd om/house-price-prediction
pip install -r requirements.txt
python src/train_model.py
python src/predict.py
python src/visualize.py
```

## 📈 Evaluation Metrics
- MAE — Mean Absolute Error
- MSE — Mean Squared Error
- RMSE — Root Mean Squared Error
- R² Score — coefficient of determination

## 📁 Project Structure

```text
house-price-prediction/
├── data/housing.csv
├── notebooks/house_price_prediction.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│   └── visualize.py
├── models/
├── outputs/
├── requirements.txt
├── .gitignore
└── LICENSE
```

## 🎯 Example

The included example predicts the price of a 1500 sq ft, 3-bedroom, 2-bathroom Urban house with 2 parking spaces and 5 years of age.

> Educational project for demonstrating an end-to-end Linear Regression workflow.