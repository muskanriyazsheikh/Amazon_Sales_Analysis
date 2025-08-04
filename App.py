import streamlit as st
import os
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# Set page config
st.set_page_config(page_title="🤖 AI Product Chatbot", layout="centered")
st.title("🤖 Amazon Product Chatbot")
st.markdown("Ask me anything about your product data 👇")

# Load dataset (optimized for Streamlit Cloud)
@st.cache_data
def load_data():
    try:
        return pd.read_csv("amazon.csv", encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv("amazon.csv", encoding='latin1')

df = load_data()

# API Key Setup
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    st.success("🔐 API key loaded: `True`")
    llm = OpenAI(api_token=OPENAI_API_KEY)
    sdf = SmartDataframe(df, config={"llm": llm})
except Exception as e:
    st.error(f"❌ Could not initialize LLM: {e}")
    st.stop()

# Chat input
user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = sdf.chat(user_input)
            st.markdown("**Answer:**")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error during chat: {str(e)}")
