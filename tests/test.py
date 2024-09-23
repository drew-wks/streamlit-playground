from streamlit.testing.v1 import AppTest

def test_main_app():
    # Create an instance of AppTest with the target script
    app = AppTest(main)

    # Run the app and simulate user input
    result = app.run(input={"Enter some text:": "Test input"})

    # Check if the expected output is in the results
    assert "You entered: Test input" in result
