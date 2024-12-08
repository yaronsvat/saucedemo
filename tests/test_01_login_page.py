from saucedemo_tests.pages.login_page import LoginPage

def test_login_standard_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("standard_user", "secret_sauce")
    assert result == "Login successful: Redirecting to https://www.saucedemo.com/inventory.html"

def test_login_problem_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("problem_user", "secret_sauce")
    assert result == "Login successful: Redirecting to https://www.saucedemo.com/inventory.html"

def test_login_performance_glitch_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("performance_glitch_user", "secret_sauce")
    assert result == "Login successful: Redirecting to https://www.saucedemo.com/inventory.html"

def test_login_error_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("error_user", "secret_sauce")
    assert result == "Login successful: Redirecting to https://www.saucedemo.com/inventory.html"

def test_login_visual_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("visual_user", "secret_sauce")
    assert result == "Login successful: Redirecting to https://www.saucedemo.com/inventory.html"

def test_login_locked_out_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("locked_out_user", "secret_sauce")
    assert result == "Epic sadface: Sorry, this user has been locked out."

def test_invalid_login_standard_user(browser):
    login_page = LoginPage(browser)
    result = login_page.login("standard_user", "wrong_secret_sauce")
    assert result == "Unexpected page after login"

def test_login_with_empty_credentials(browser):
    login_page = LoginPage(browser)
    result = login_page.login("", "")
    assert result == "Epic sadface: Username is required"

def test_login_with_empty_password(browser):
    login_page = LoginPage(browser)
    result = login_page.login("standard_user2", "")
    assert result == "Epic sadface: Password is required"