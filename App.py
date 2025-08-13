import streamlit as st
import os
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# Set Streamlit page configuration
st.set_page_config(page_title="🤖 AI Product Chatbot", layout="centered")
st.title("🤖 Amazon Product Chatbot")
st.markdown("Ask me anything about your product data 👇")

# --- Function to load the dataset ---
# Using Streamlit's cache to prevent reloading the data on every rerun
@st.cache_data
def load_data():
    """Loads the Amazon product data from a CSV file."""
    try:
        # Assumes the CSV is named 'amazon.csv' and is in the same directory
        return pd.read_csv("amazon.csv", encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback for different encodings
        return pd.read_csv("amazon.csv", encoding='latin1')
    except FileNotFoundError:
        st.error("Error: 'amazon.csv' not found. Please ensure the file is in the same directory.")
        st.stop()

# Load the dataframe
df = load_data()

# --- API Key Setup ---
# Use Streamlit's secrets management for secure API key storage
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    st.success("🔐 API key loaded: `True`")
    
    # Initialize the LLM with the API key
    llm = OpenAI(api_token=OPENAI_API_KEY)
    
    # Create the SmartDataframe instance
    sdf = SmartDataframe(df, config={"llm": llm})
except KeyError:
    st.error("❌ `OPENAI_API_KEY` not found in Streamlit secrets.")
    st.info("Please add your OpenAI API key to the `secrets.toml` file in your `.streamlit` folder.")
    st.stop()
except Exception as e:
    st.error(f"❌ Could not initialize LLM. Error: {e}")
    st.stop()

# --- Chatbot UI and Logic ---
# Get user input from a text box
user_input = st.text_input("You:", "")

if user_input:
    # Display a spinner while the LLM is thinking
    with st.spinner("Thinking..."):
        try:
            # Use the SmartDataframe's chat method to get a response
            response = sdf.chat(user_input)
            
            # Display the chatbot's answer
            st.markdown("---")
            st.markdown("**Answer:**")
            st.write(response)
        except Exception as e:
            # Handle any errors during the chat interaction
            st.error(f"❌ Error during chat: {str(e)}")

# --- Display the dataframe at the bottom for context ---
st.markdown("---")
st.subheader("Your Amazon Product Data")
st.dataframe(df)

