import streamlit as st

st.set_page_config(page_title="Product Chatbot", layout="centered")

st.title("🤖 Amazon Product Chatbot")

# Welcome message
st.write("Hi! Ask me anything about Amazon product insights:")

# Predefined responses (simple version)
responses = {
    "top rated product": "Fire-Boltt Ninja has the highest rating.",
    "most discount": "Fire-Boltt Ninja offers the most discount.",
    "average rating": "The overall average rating is 4.80.",
    "price": "The total combined product price is ₹2000.",
    "category": "Electronics and Home are most common categories."
}

# User input
query = st.text_input("You:", "")

if query:
    matched = False
    for key in responses:
        if key in query.lower():
            st.success(responses[key])
            matched = True
            break
    if not matched:
        st.warning("Sorry, I don't have info on that yet.")
