# AutomationExercise Playwright Test Suite

Automated end-to-end tests for [automationexercise.com](https://www.automationexercise.com) using Playwright and Python.

## Project Structure

```
automationexercise/
├── config.py               # Base URLs
├── conftest.py             # Shared fixtures
├── pages/
│   └── signup_page.py      # Signup page object
└── tests/
    └── test_signup.py
```

## Concepts Covered

- **Page Object Model (POM)** — each page has its own class with locators and actions
- **Multi-step flows** — chained fixtures handling multi-page signup
- **Parametrized tests** — testing missing fields with one test function
- **Optional parameters** — flexible methods using default empty strings

## Installation

```bash
pip install pytest-playwright
playwright install
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run headed (see the browser)
pytest tests/ -v --headed
```

## Test Coverage

- First signup step — name and email
- Full registration — all fields filled, account created
- Missing fields — parametrized negative cases
- Checkout Process
