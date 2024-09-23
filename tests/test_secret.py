import os
import pytest
from streamlit.testing.v1 import AppTest

# Test function to access and print st.secrets.QDRANT_API_KEY
def test_print_qdrant_api_key():
    # Path to the Streamlit app script (now pointing to the root directory)
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'print_secret.py'))
    
    # Initialize AppTest for the script
    at = AppTest.from_file(script_path)
    
    # Run the app
    at.run()
    
    # Optionally, print the secrets to confirm access
    print("Secrets:", at.secrets)
    
    # Check if the secret is present and printed
    assert "QDRANT_API_KEY" in at.secrets, "QDRANT_API_KEY not found in secrets."
    qdrant_api_key = at.secrets["QDRANT_API_KEY"]
    
    # Print the key
    print(f"QDRANT_API_KEY: {qdrant_api_key}")
    
    # Ensure the key is not empty
    assert qdrant_api_key is not None
    assert len(qdrant_api_key) > 0
