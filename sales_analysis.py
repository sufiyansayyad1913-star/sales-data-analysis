
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print(df)

print("First 5 rows:")
print(df.head())

print("Dataset Shape:")
print(df.shape)

print("Column Names:")
print(df.columns)

print("Dataset Information:")
df.info()

print("Statistical Summary:")
print(df.describe())


print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:")
print(df.duplicated().sum())


# 1. Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# 2. Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# 3. Sales by Product
product_sales = df.groupby("Product")["Sales"].sum()
print("Sales by Product:")
print(product_sales)

# 4. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("Sales by Region:")
print(region_sales)


# Region-wise Sales Chart
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()


# Product-wise Sales
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("Product-wise Sales:")
print(product_sales)

# Product Sales Chart
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Profit by Product
product_profit = df.groupby("Product")["Profit"].sum().sort_values(ascending=False)

print("Profit by Product:")
print(product_profit)

# Profit Chart
product_profit.plot(kind="bar")

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Convert Order_Date into datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Extract month
df["Month"] = df["Order_Date"].dt.month_name()

# Calculate monthly sales
monthly_sales = df.groupby(
    df["Order_Date"].dt.month
)["Sales"].sum()

monthly_sales.index = ["January", "February"]

print(monthly_sales)

# Monthly Sales Chart
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



# Final Business Insights Report

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

best_product = df.groupby("Product")["Sales"].sum().idxmax()
best_region = df.groupby("Region")["Sales"].sum().idxmax()
best_profit_product = df.groupby("Product")["Profit"].sum().idxmax()

print("\n===== SALES ANALYSIS REPORT =====")
print(f"Total Sales: Rs. {total_sales:,}")
print(f"Total Profit: Rs. {total_profit:,}")
print(f"Best Selling Product: {best_product}")
print(f"Top Sales Region: {best_region}")
print(f"Highest Profit Product: {best_profit_product}")
print("================================")