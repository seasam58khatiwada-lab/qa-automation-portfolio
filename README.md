#QA Automation Portfolio 

Automated testing projects built with python, pytest and Playwright. 
Built fro scratch as part of a structured learning path toward a QA automation career.

##tech stack 
-Python
-Pytest 
-Playwright

##setup 
1. Clone teh repository 
2. Create a virtual environment: 'python -m venv .venv'
3. Activate it: '.\.venv\Scripts\Activate.ps1'
4. Install dependances: 'pip install -r requirements.txt'
5. Install browsers: 'playwright install'

##Run tests
'pytest'

##Project structure
-'tests/ui' - browser tests
-'tests/api' - API tests
-'pages' - Page Object classes
-'utils' - helper code
-'data' - test data

##Progress
-[x] Project setup and Git workflow
-[x] Login UI test (valid and invalid, data-driven with parametrize)
-[x] Page Object Model (LoginPage, InventoryPage)
-[x] Shared fixtures in conftest.py
-[] API tests
-[] CI with GitHub Actions

