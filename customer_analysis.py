import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the data
df = pd.read_csv("sales_data.csv")
print("🧾 Original Data:\n", df)

# Step 2: Basic Data Cleaning
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
df['TotalAmount'] = df['Quantity'] * df['Price']
print("\n✅ Data after adding TotalAmount:\n", df)

# Step 3: Top Customers by Total Spend
top_customers = df.groupby('Name')['TotalAmount'].sum().sort_values(ascending=False)
print("\n🏆 Top Customers:\n", top_customers)

# Step 4: Most Popular Products
popular_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\n📦 Most Popular Products:\n", popular_products)

# Step 5: Gender-based Purchase Analysis
gender_analysis = df.groupby('Gender')['TotalAmount'].sum()
print("\n👥 Total Purchase by Gender:\n", gender_analysis)

# Step 6: Visualizations
plt.figure(figsize=(8,5))
sns.barplot(x=top_customers.index, y=top_customers.values)
plt.title("Top Customers by Total Spend")
plt.ylabel("Total Amount ($)")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=popular_products.index, y=popular_products.values)
plt.title("Most Popular Products by Quantity Sold")
plt.ylabel("Total Quantity Sold")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=gender_analysis.index, y=gender_analysis.values)
plt.title("Total Purchase by Gender")
plt.ylabel("Total Amount ($)")
plt.show()
