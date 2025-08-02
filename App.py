import streamlit as st

st.set_page_config(page_title="Amazon Product Chatbot", layout="centered")

st.title("🤖 Amazon Product Chatbot")

st.write("Hi! Ask me anything about Amazon product insights:")

# 🔍 Define responses (more flexible, covers synonyms)
responses = {
    "top rated product": "🔥 Fire-Boltt Ninja is the top-rated product with a 4.9 rating.",
    "highest rating": "🔥 Fire-Boltt Ninja is the top-rated product with a 4.9 rating.",
    "most discount": "💸 Fire-Boltt Ninja has the highest discount among all products.",
    "discount": "💸 Fire-Boltt Ninja has the highest discount among all products.",
    "average rating": "⭐ The average product rating is 4.80.",
    "rating": "⭐ The average product rating is 4.80.",
    "total price": "💰 The total price of all products combined is ₹2,000.",
    "price": "💰 The total price of all products combined is ₹2,000.",
    "category": "📦 Electronics and Home are the most common product categories.",
    "categories": "📦 Electronics and Home are the most common product categories.",
    "top categories": "📦 Electronics and Home are the most common product categories.",
    "how many products": "📊 There are 120 products in the dataset."
}

# 🧠 Normalize and process user input
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
        st.warning("😕 Sorry, I don't have info on that yet. Try asking about rating, price, or category.")
