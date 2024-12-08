INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

def login_result(username, page):
    valid_users = {
        "standard_user": INVENTORY_URL,
        "problem_user": INVENTORY_URL,
        "performance_glitch_user": INVENTORY_URL,
        "visual_user": INVENTORY_URL,
        "error_user": INVENTORY_URL
    }

    error_messages = {
        "locked_out_user": "Epic sadface: Sorry, this user has been locked out.",
        "": "Epic sadface: Username is required",
        "standard_user2": "Epic sadface: Password is required"
    }
    if username in valid_users:
        if page.url == valid_users[username]:
            return f"Login successful: Redirecting to {valid_users[username]}"
        else:
            return "Unexpected page after login"
    if username in error_messages:
        error_message = page.inner_text(".error-message-container")
        if error_messages[username] in error_message:
            return error_messages[username]
        else:
            return "Unexpected error message"
    return "Unknown user"


class LoginPage:
    def __init__(self, browser):
        self.browser = browser  # Use the browser passed from the fixture
        self.url = "https://www.saucedemo.com/"

    def login(self, username: str, password: str):
        page = self.browser.new_page()
        page.goto(self.url)
        page.fill('#user-name', username)
        page.fill('#password', password)
        page.click('#login-button')
        page.wait_for_load_state('networkidle')
        return login_result(username, page)





















