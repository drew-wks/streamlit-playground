from streamlit.testing.v1 import AppTest

def test_main_app():
    at = AppTest.from_file("main.py", default_timeout=5)
    
    # if you need to access secrets, do that here before at.run()
    at.run()
    assert not at.exception, f"An exception occurred: {at.exception}"
    
    assert "6333" in at.markdown[2].value # confirm the app accessed st.secrets
    # Simulate user input in the text input widget
    at.text_input[0].input("You are doing it, Drew!").run()

    assert "You entered: You are doing it, Drew!" in at.markdown[3].value  # Checks second markdown output for value. If this condition is true, the test passes; otherwise, it fails.
