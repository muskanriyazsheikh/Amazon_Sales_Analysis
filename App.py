import streamlit as st
import os
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# Load dataset
@st.cache_data
def load_data():
    try:
        return pd.read_csv("Data/amazon_data.csv", encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv("Data/amazon_data.csv", encoding='latin1')

df = load_data()

# ✅ Initialize OpenAI LLM and SmartDataframe (with error handling)
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    st.write("🔐 API key loaded:", bool(OPENAI_API_KEY))  # Debugging output
    llm = OpenAI(api_token=OPENAI_API_KEY)
    sdf = SmartDataframe(df, config={"llm": llm})
except Exception as e:
    st.error(f"❌ Could not initialize LLM: {e}")

# ✅ Streamlit app UI
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
