import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Data/amazon_data.csv")

df = load_data()

# Set OpenAI key here (keep it secret)
OPENAI_API_KEY = "your-openai-api-key"  # Replace with your actual key
llm = OpenAI(api_token=OPENAI_API_KEY)
sdf = SmartDataframe(df, config={"llm": llm})

# Streamlit app UI
st.set_page_config(page_title="🤖 AI Product Chatbot", layout="centered")
st.title("🤖 Amazon Product Chatbot")
st.markdown("Ask me anything about your product data 👇")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = sdf.chat(user_input)
            st.markdown("**Answer:**")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

