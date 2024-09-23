### Repo Purpose
 To test streamlit, including accessing secrets and using the streamlit test framework

### Setup

### How to Set up and Run Locally (using VS Code)
1. Clone the repository
2. Open the project in VS Code.
3. Set up your local environment and python interpreter 
   - Open a terminal and navigate to the directory where your `setup.sh` file is located.  
- Run the following command to give the script executable permission:  

    ```bash
    chmod +x setup.sh
    ```
- Once the file is executable, you can run the script by entering the following command:  
    ```bash
    ./setup.sh
    ```

- If you're running this in a virtual environment or other specific shell, make sure the environment is activated first.  
4. Add your streamlit secrets into .secrets.toml
5. Select the main.py file
6. Go to the "Run and Debug" panel in VS Code Ctrl+Shift+D or Cmd+Shift+D).
7. Select "Run Streamlit App" and press the green play button to start
8. The Streamlit user interface will load in the default browser

### How to Run tests