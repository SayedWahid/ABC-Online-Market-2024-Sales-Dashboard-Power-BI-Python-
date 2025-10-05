## 🧼 Data Preparation (Python Script)

**Dataset Columns Used**
transaction_id, order_date, product_category, product_id,
product_name, units_sold, unit_price, total_revenue,
region, payment_method


**Objective:**  
Clean and standardize raw sales data before importing into Power BI.

---

### 🧮 Key Data Cleaning Steps (Python)
```python
# Import necessary library
import pandas as pd

# Load dataset
df = pd.read_csv('market.csv')

# Convert order_date column to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Create Month-Year column for time-series analysis
df['Month-Year'] = df['order_date'].dt.strftime('%b-%Y')

# Handle missing values (replace with zeros)
df.fillna(0, inplace=True)

# Ensure numeric columns are properly formatted
num_cols = ['units_sold', 'unit_price', 'total_revenue']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

# Save cleaned dataset for Power BI visualization
df.to_csv('market_clean.csv', index=False)

print("Data cleaning complete. File saved as 'market_clean.csv'.")
