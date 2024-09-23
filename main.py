import streamlit as st

port = st.secrets["QDRANT_PORT"]
st.write("This is a test app.")

st.write("This is a test secret:")
st.write(port)

# Input field for user input
user_input = st.text_input("Enter some text:")

# Display the user's input
if user_input:
    st.write(f"You entered: {user_input}")
