# 📊 Amazon Product Insights Dashboard

A Power BI dashboard project analyzing Amazon product data based on pricing, ratings, categories, and discounts. Built with Python (for data cleaning) and Power BI (for visualization).

---

## 🔍 Project Overview

This project explores key insights from a real-world Amazon sales dataset, focusing on:

- Product ratings
- Discount trends
- Category-wise product distribution
- Price vs Rating relationships

The goal is to assist in **data-driven decision-making** and uncover **actionable insights** from e-commerce data.

---

## 📁 Dataset Features

The dataset includes over **1,400+ products** with the following columns:

- `product_id`
- `product_name`
- `category`
- `discounted_price`
- `actual_price`
- `rating`
- `discount_percentage`
- `rating_count`
- `review_title`, `review_content`
- `user_id`, `user_name`

📝 *Raw dataset source: Amazon product reviews and pricing data (Kaggle or scraped dataset)*

---

## 🛠 Tools & Technologies Used

| Task | Tool |
|------|------|
| Data Cleaning | Python (Pandas) |
| Data Storage | Excel (`cleaned_amazon_data.xlsx`) |
| Dashboard & Visualization | Power BI |
| File Export | PDF, PBIX |

---

## 🧹 Data Preprocessing (Python)

Key steps:
- Removed ₹ symbols and converted price columns to numeric
- Calculated `discount_amount = actual_price - discounted_price`
- Converted ratings to float and handled missing values
- Simplified multi-category fields using:
```python
df['category'] = df['category'].astype(str).str.split('|').str[0].str.strip()
