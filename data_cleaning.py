import pandas as pd

def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data[column] >= lower) & (data[column] <= upper)]

df = pd.read_csv("data/raw_sales_data.csv")

print("Before Cleaning")
print("Rows:", df.shape[0])
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()

for col in ["Sales", "Profit", "Customer_Age"]:
    df[col] = df[col].fillna(df[col].median())

df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

for col in ["Sales", "Profit", "Customer_Age"]:
    df = remove_outliers_iqr(df, col)

df.to_csv("data/cleaned_sales_data.csv", index=False)

print("\nAfter Cleaning")
print("Rows:", df.shape[0])
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print("\nCleaned data saved as data/cleaned_sales_data.csv")