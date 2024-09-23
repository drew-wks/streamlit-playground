from streamlit.testing.v1 import AppTest
import sys
import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main

def test_main_app():
    # Load the app from the file
    app_test = AppTest.from_file("main.py")  # Adjust the path to your app file if necessary
    
    # Run the app the first time (initial load)
    app_test.run()
    
    # Simulate user input in the text input widget
    app_test.text_input[0].input("Test input").run()

    # Verify the output displayed by the app after the input is processed
    assert "You entered: Test input" in app_test.markdown[1].value  # Checking second markdown output
