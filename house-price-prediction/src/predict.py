"""Make a house-price prediction using the trained model."""
from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "linear_regression_model.pkl"

def predict_price(area_sqft, bedrooms, bathrooms, stories, parking, location, age_years):
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Trained model not found. Run: python src/train_model.py")
    model = joblib.load(MODEL_PATH)
    house = pd.DataFrame([{
        "area_sqft": area_sqft, "bedrooms": bedrooms, "bathrooms": bathrooms,
        "stories": stories, "parking": parking, "location": location, "age_years": age_years
    }])
    return model.predict(house)[0]

if __name__ == "__main__":
    price = predict_price(1500, 3, 2, 2, 2, "Urban", 5)
    print(f"Predicted house price: ${price:,.2f}")
