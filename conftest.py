import pytest

login_test_params = [
    {"username": "standard_user", "password": "secret_sauce"}
]

@pytest.fixture(scope="module")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def logged_in_page(browser, request):
    print("Fixture 'logged_in_page' is being set up")
    username = request.param.get("username")
    password = request.param.get("password")
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill('#user-name', username)
    page.fill('#password', password)
    page.click('#login-button')
    page.wait_for_load_state('networkidle')
    yield page
    page.close()