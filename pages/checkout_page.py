from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = "button#checkout"
        self.first_name_field = "input#first-name"
        self.last_name_field = "input#last-name"
        self.postal_code_field = "input#postal-code"
        self.continue_button = "input#continue"
        self.finish_button = "button#finish"

    def start_checkout(self):
        self.page.click(self.checkout_button)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.first_name_field, first_name)
        self.page.fill(self.last_name_field, last_name)
        self.page.fill(self.postal_code_field, postal_code)
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)
