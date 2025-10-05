# 💼 ABC Online Market – 2024 Sales Dashboard (Power BI + Python)

An interactive **Power BI dashboard** showcasing sales performance across **regions, product categories, and months**, built using **Python for data preparation** and **Power BI for visualization**.

This project demonstrates a full **data analytics workflow** — from raw data cleaning to business insights presentation — optimized for clarity, performance tracking, and executive decision-making.

---

## 🧭 Project Overview
The **ABC Online Market – 2024 Dashboard** provides a clear, interactive view of company performance using visual storytelling.  
It enables business users to:
- Track **monthly revenue trends**.
- Identify **top-performing regions** and **product categories**.
- Discover **best-selling products** and **low-performing months**.

**Goal:** Turn sales data into actionable insights for strategic decisions.

---

## 🧰 Tools & Technologies
| Tool | Purpose |
|------|----------|
| **Python (Pandas)** | Data cleaning and preparation |
| **Power BI** | Dashboard creation and data visualization |
| **Matplotlib / Seaborn** | Optional Python visual validation |
| **CSV** | Raw data source |
| **GitHub** | Version control and project documentation |

---

## 🧼 Data Preparation (Python Script)
**Dataset Columns Used:**
transaction_id, order_date, product_category, product_id,
product_name, units_sold, unit_price, total_revenue,
region, payment_method


**Objective:** Clean and standardize raw sales data for Power BI.

### 🧮 Key Steps:
```python
import pandas as pd

# Load dataset
df = pd.read_csv('online_market.csv')

# Convert to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Create Month-Year column
df['Month-Year'] = df['order_date'].dt.strftime('%b-%Y')

# Handle missing values
df.fillna(0, inplace=True)

# Convert numeric columns
num_cols = ['units_sold', 'unit_price', 'total_revenue']
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

# Export cleaned dataset
df.to_csv('market_clean.csv', index=False)
print("Data cleaning complete. File saved as 'market_clean.csv'.")

```



✅ **Output:**  
A cleaned dataset file — `market_clean.csv` — ready for Power BI import.


---

## **📊 ABC Dashboard Highlights**


### 🔹 KPIs (Top Section)
| KPI | Description |
|------|--------------|
| 💰 **Total Revenue:** $3.65M | Overall revenue generated |
| 📦 **Total Units Sold:** 3K | Total items sold across all regions |
| 🛒 **Average Order Revenue:** $3.65K | Revenue generated per transaction |
| 🏷️ **Average Unit Price:** $1.23K | Average selling price per unit |

---

### 🔹 Visuals (Main Dashboard Area)
| Visualization | Description |
|----------------|--------------|
| **Line Chart** | Monthly Revenue Trend (Jan–Dec 2024) |
| **Bar Chart (Horizontal)** | Total Sales by Region (Asia, Europe, North America) |
| **Bar Chart (Horizontal)** | Top 5 Products by Revenue |
| **Donut Chart** | Revenue Distribution by Product Category |

---

### 🔹 Interactive Filters
- **Product Category**  
- **Payment Method**  

These slicers allow users to dynamically explore data across multiple dimensions and compare trends interactively.

---

## 🧠 Key Insights
1. **Asia** region leads with **$1.32M (36%)** of total revenue.  
2. **August** recorded the **lowest sales ($237K)** — indicates a seasonal slowdown.  
3. **Neutrogena Skincare Set** is the **best-selling product** of the year.  
4. **Beauty Products** category contributes the **highest revenue share (19%)**.  
5. **Monthly revenue peaked in December ($358K)** — reflecting strong holiday demand. 

---

## 🎯 Insight Summary
> The dashboard clearly highlights strong performance in Asian markets, consistent year-end growth, and category dominance by Beauty Products — making it ideal for executives to monitor trends, allocate inventory, and plan regional promotions effectively.




