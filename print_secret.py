# print_secret.py
import streamlit as st

# Access and print the secret
if "QDRANT_API_KEY" in st.secrets:
    api_key = st.secrets["QDRANT_API_KEY"]
    st.write(f"QDRANT_API_KEY: {api_key}")
else:
    st.write("QDRANT_API_KEY not found in secrets.")
