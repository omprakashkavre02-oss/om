"""Create basic visualizations for the housing dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "housing.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="area_sqft", y="price", hue="location")
plt.title("House Area vs Price")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "area_vs_price.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="location", y="price")
plt.title("House Price by Location")
plt.xlabel("Location")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "price_by_location.png", dpi=150)
plt.close()

print(f"Charts saved in: {OUTPUT_DIR}")
