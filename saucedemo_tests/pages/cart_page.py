from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = ".cart_item"
        self.item_prices = ".inventory_item_price"
        self.remove_buttons = ".cart_button"
        self.continue_shopping_button = "button#continue-shopping"
        self.cart_link_selector = 'a.shopping_cart_link[data-test="shopping-cart-link"]'

    def remove_most_expensive_item(self):
        cart_items = self.page.query_selector_all('div[data-test="inventory-item"]')
        max_price = 0
        item_to_remove = None
        for item in cart_items:
            price_text = item.query_selector('div[data-test="inventory-item-price"]').inner_text()
            price = float(price_text.replace('$', '').strip())  # Convert price to float
            if price > max_price:
                max_price = price
                item_to_remove = item
        if item_to_remove:
            remove_button = item_to_remove.query_selector('button[data-test^="remove-"]')
            if remove_button:
                remove_button.click()

    def add_cheapest_item(self):
        cart_items = self.page.query_selector_all('div[data-test="inventory-item"]')
        min_price = float('inf')
        cheapest_item = None
        for item in cart_items:
            price_text = item.query_selector('div[data-test="inventory-item-price"]').inner_text()
            price = float(price_text.replace('$', '').strip())
            product_name = item.query_selector('div[data-test="inventory-item-name"]').inner_text()
            product_status = self.get_button_status(product_name)
            if (price < min_price) and (product_status == "Add to cart"):
                min_price = price
                cheapest_item = {
                    'name': product_name,
                    'price': price,
                    'add_button': item.query_selector('button[data-test^="add-to-cart"]')  # Add to cart button
                }
        cheapest_item['add_button'].click()

    def get_button_status(self, product_name: str):
        product_id = product_name.lower().replace(" ", "-")
        remove_button_xpath = f'//*[@id="remove-{product_id}"]'
        add_to_cart_button_xpath = f'//*[@id="add-to-cart-{product_id}"]'
        remove_button = self.page.query_selector(remove_button_xpath)
        add_to_cart_button = self.page.query_selector(add_to_cart_button_xpath)
        if remove_button:
            if remove_button.is_visible():
                return "Remove"
        elif add_to_cart_button:
            if add_to_cart_button.is_visible():
                return "Add to cart"
        print(f"Button not found for {product_name}.")
        return None

    def continue_shopping(self):
        self.page.click(self.continue_shopping_button)

    def go_to_cart(self):
        self.page.click(self.cart_link_selector)

    def get_added_items(self):
        cart_items = self.page.query_selector_all('div[data-test="inventory-item"]')
        added_items = []
        for item in cart_items:
            product_name = item.query_selector('div[data-test="inventory-item-name"]').inner_text()
            price_text = item.query_selector('div[data-test="inventory-item-price"]').inner_text()
            price = float(price_text.replace('$', '').strip())
            added_items.append({'name': product_name, 'price': price})
        return added_items
