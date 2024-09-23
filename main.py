import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a test app.")
st.write("This is a test secret.")
hi = st.secrets["QDRANT_PORT"]
st.write(hi)
st.write("This is a test app with an input field.")

# Input field for user input
user_input = st.text_input("Enter some text:")

# Display the user's input
if user_input:
    st.write(f"You entered: {user_input}")
