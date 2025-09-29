# TheCatsTest

TheCatsTest API Automation Framework
This is a test automation framework for TheCatsAPI, built with Python, Pytest, and Requests. It provides a structured and scalable way to write and execute API tests.


## Prerequisites
Before you begin, ensure you have the following installed:

Python 3.10+

pip and venv

Allure


## Local Setup and Installation
Clone the repository:

git clone https://github.com/KesorT/TheCatsTest.git
cd TheCatsTest

## Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

## Install dependencies:

pip install -r requirements.txt


## Configure environment variables:
Create a file named .env in the project root and add your API key and the base URL. You can use the .env.example file as a template.

.env file
BASE_URL="https://your-url"
API_KEY="your-api-key-here"

# CI/CD Integration
This project is fully integrated with a Continuous Integration (CI) pipeline using GitHub Actions.

The workflow is defined in the .github/workflows/tests.yml file and provides the following automation:

Automatic Triggering: The workflow runs automatically on every push and pull_request to the main branch.

Environment Setup: It sets up a clean environment with the correct versions of Python, Java, and Allure Commandline.

Test Execution: It securely injects the BASE_URL and API_KEY from GitHub Secrets and runs the entire pytest suite.

Report Generation & Publishing: After the tests run, it automatically generates the Allure report and deploys it to GitHub Pages.

## The latest test report for the main branch is always available at the following URL:
https://kesort.github.io/TheCatsTest/

