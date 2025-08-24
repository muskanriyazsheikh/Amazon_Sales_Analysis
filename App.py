import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import os

# --- Page settings ---
st.set_page_config(page_title="Amazon Product Chatbot", layout="centered")

# --- Load CSV directly (replace with your file path) ---
CSV_PATH = "amazon.csv"  # Change this to your dataset path
df = pd.read_csv(CSV_PATH)

# --- Initialize PandasAI ---
os.environ["OPENAI_API_KEY"] = "sk-proj-...."
llm = OpenAI(api_token=os.getenv("OPENAI_API_KEY"))
sdf = SmartDataframe(df, config={"llm": llm})

# --- Pre-calculated values ---
avg_rating = df["Rating"].mean().round(2)
avg_rating_per_cat = df.groupby("Category")["Rating"].mean().round(2).to_dict()
avg_rating_per_cat_str = ", ".join([f"{cat} - {rating}" for cat, rating in avg_rating_per_cat.items()])

price_vs_rating = df.groupby("Actual Price")["Rating"].mean().round(2).to_dict()
price_vs_rating_str = ", ".join([f"₹{price} → {rating}★" for price, rating in price_vs_rating.items()])

# --- Predefined responses ---
responses = {
    "top rated product": "🔥 Fire-Boltt Ninja is the top-rated product with a 4.9 rating.",
    "highest rating": "🔥 Fire-Boltt Ninja is the top-rated product with a 4.9 rating.",
    "most discount": "💸 Fire-Boltt Ninja has the highest discount among all products.",
    "discount": "💸 Fire-Boltt Ninja has the highest discount among all products.",
    "average rating": f"⭐ The average product rating is {avg_rating}.",
    "rating per category": f"📊 Average rating per category: {avg_rating_per_cat_str}",
    "actual price vs rating": f"💰 Price vs Rating: {price_vs_rating_str}",
    "total price": f"💰 The total price of all products combined is ₹{df['Actual Price'].sum():,.0f}.",
    "category": "📦 Electronics and Home are the most common product categories.",
    "categories": "📦 Electronics and Home are the most common product categories.",
    "top categories": "📦 Electronics and Home are the most common product categories.",
    "how many products": f"📊 There are {len(df)} products in the dataset."
}

# --- UI ---
st.title("🤖 Amazon Product Chatbot")
st.write("Hi! Ask me anything about Amazon product insights:")

query = st.text_input("You:", "")

if query:
    cleaned_query = query.lower().strip().replace("-", "").replace("?", "")
    matched = False

    for key in responses:
        if key in cleaned_query:
            st.success(responses[key])
            matched = True
            break

    if not matched:
        try:
            answer = sdf.chat(query)
            st.info(answer)
        except Exception as e:
            st.error(f"Error: {str(e)}")
