from streamlit.testing.v1 import AppTest
import sys
import os


import main

def test_main_app():
    # Load the app from the file
    at = AppTest.from_file("main.py")  # Adjust the path to your app file if necessary
    hi = at.secrets["QDRANT_PORT"]
    
    # Run the app the first time (initial load)
    at.run()
    
    # Simulate user input in the text input widget
    at.text_input[0].input("Test input").run()

    # Verify the output displayed by the app after the input is processed
    assert "You entered: Test input" in at.markdown[1].value  # Checking second markdown output
