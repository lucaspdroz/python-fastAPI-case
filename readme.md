# Python Web Study

This is not a walkthrough, I'm just sharing my learning process.

1. Familiarize with the Web Environment
I already have some knowledge of Python 3 and now need to acclimate to its use in a web context.

2. Set Up a Local Server
I chose to use the "uvicorn" package due to its similarity to Node.js.

3. Develop a Basic FastAPI Application
I want to create a FastAPI application that aligns with current market trends.
    * Running the Project: How to run the project effectively.

4. Create a Local Environment
Establishing a local environment is crucial (I've seen a lot of examples already! 😅).

5. Break Down the Paths into Routes
Start with creating basic routes.

6. Create More Complex Endpoints - ex: Implement POST methods for data processing and explore passing data as query parameters.

7. Security and Validation
    * URL validation to prevent various types of attacks (XSS, DoS, Input Length Attacks)

## Commands

### Create venv (only first-time)

Create a Virtual Environment (only on the first run)

> python3 -m venv [venv_name]

### Activate venv

Activate the Virtual Environment

> source venv/bin/activate

### Deactivate venv

Deactivate the Virtual Environment

> deactivate

### Save packages

Save Installed Packages and Versions to a File

> pip freeze > requirements.txt

### Installing requirements

Install Requirements from a File

> pip install -r requirements.txt

### Starting application

Start the Application (with auto-reload)

> uvicorn app.main:app --reload
