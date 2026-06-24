import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/cleaned_sales_data.csv")

# Sales by category
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Sales", estimator=sum)
plt.title("Total Sales by Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/sales_by_category.png")
plt.show()

# Profit by region
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Region", y="Profit", estimator=sum)
plt.title("Total Profit by Region")
plt.tight_layout()
plt.savefig("outputs/profit_by_region.png")
plt.show()

# Sales distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("outputs/sales_distribution.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 5))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.show()

print("Charts saved inside outputs folder.")