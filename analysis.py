import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
df_2021 = pd.read_csv("data/Bike_Sales_2021.csv")
df_2022 = pd.read_csv("data/Bike_Sales_2022.csv")

# Step 2: Combine Data
df = pd.concat([df_2021, df_2022])

# Step 3: Basic Info
print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

# Step 4: Clean Data (drop missing values)
df = df.dropna()

# Step 5: Analysis
total_sales = df["Revenue"].sum()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()
top_product = df.groupby("Product")["Revenue"].sum().idxmax()

print(f"Total Revenue: {total_sales}")
print(f"Top Region: {top_region}")
print(f"Best Selling Product: {top_product}")

# Step 6: Visualization
plt.figure(figsize=(8,5))
df.groupby("Region")["Revenue"].sum().plot(kind="bar", color="skyblue")
plt.title("Total Revenue by Region (2021-2022)")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bike_sales_by_region.png")
plt.show()
