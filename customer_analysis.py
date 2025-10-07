import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Step 1: Load the dataset
# ------------------------------
df = pd.read_csv("sales_data.csv")
print("🧾 Original Data:\n", df)

# ------------------------------
# Step 2: Data cleaning and new column
# ------------------------------
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
df['TotalAmount'] = df['Quantity'] * df['Price']
print("\n✅ Data after adding TotalAmount:\n", df)

# ------------------------------
# Step 3: Analysis
# ------------------------------

# Top Customers by Total Spend
top_customers = df.groupby('Name')['TotalAmount'].sum().sort_values(ascending=False)
print("\n🏆 Top Customers:\n", top_customers)

# Most Popular Products
popular_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\n📦 Most Popular Products:\n", popular_products)

# Total Purchase by Gender
gender_analysis = df.groupby('Gender')['TotalAmount'].sum()
print("\n👥 Total Purchase by Gender:\n", gender_analysis)

# ------------------------------
# Step 4: Visualizations (saved as images)
# ------------------------------

# Top Customers
plt.figure(figsize=(8,5))
sns.barplot(x=top_customers.index, y=top_customers.values)
plt.title("Top Customers by Total Spend")
plt.ylabel("Total Amount ($)")
plt.savefig("top_customers.png")  # Save figure
plt.show()

# Most Popular Products
plt.figure(figsize=(8,5))
sns.barplot(x=popular_products.index, y=popular_products.values)
plt.title("Most Popular Products by Quantity Sold")
plt.ylabel("Total Quantity Sold")
plt.savefig("popular_products.png")  # Save figure
plt.show()

# Total Purchase by Gender
plt.figure(figsize=(6,4))
sns.barplot(x=gender_analysis.index, y=gender_analysis.values)
plt.title("Total Purchase by Gender")
plt.ylabel("Total Amount ($)")
plt.savefig("purchase_by_gender.png")  # Save figure
plt.show()

# ------------------------------
# Step 5: Finish
# ------------------------------
print("\n🎉 Analysis and charts saved successfully!")
