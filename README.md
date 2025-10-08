# Customer Behavior Analysis

This mini project demonstrates **Customer Behavior Analysis** using Python, Pandas, and data visualization libraries (Matplotlib & Seaborn).  
The goal is to analyze a sample sales dataset to gain insights into customer purchase patterns and spending behavior.

---

## 📌 Project Overview

This project performs the following tasks:

1. **Load and clean data**  
   - Converts purchase dates to proper datetime format  
   - Calculates total spending per transaction  

2. **Analyze customer behavior**  
   - Identify **top customers** by total spend  
   - Find **most popular products** by quantity sold  
   - Aggregate **purchases by gender**  

3. **Visualize results**  
   - Bar charts for top customers, popular products, and total purchases by gender  

---

## 🧰 Technologies Used

- Python 3  
- Pandas (Data manipulation)  
- Matplotlib & Seaborn (Data visualization)  

---

## 📂 Dataset

Sample CSV file: `sales_data.csv`

| CustomerID | Name | Age | Gender | Product | Quantity | Price | PurchaseDate |
|------------|------|-----|--------|---------|----------|-------|--------------|
| 1 | John | 28 | Male | Laptop | 1 | 800 | 2025-01-10 |
| 2 | Anna | 35 | Female | Phone | 2 | 500 | 2025-02-15 |
| 3 | Bob | 40 | Male | Laptop | 1 | 800 | 2025-02-20 |
| ... | ... | ... | ... | ... | ... | ... | ... |

*(You can replace this sample with real customer sales data.)*

---

## 🧠 Key Learnings

- Grouping and aggregating data with `groupby()`  
- Sorting and filtering results (`sort_values()`, `WHERE`)  
- Calculating new metrics (Total Amount spent per transaction)  
- Visualizing insights using bar charts and Seaborn  

---

## ⚙️ How to Run

1. Install required libraries:

pip install pandas matplotlib seaborn

2. Run the Python script:

python customer_analysis.py


3. Observe:

Printed summary of top customers, popular products, and purchase by gender

Bar charts displaying insights visually
