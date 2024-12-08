from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    inventory_items = ".inventory_item"

    def get_inventory_items(self):
        items = self.page.locator(self.inventory_items)
        inventory_list = []
        for i in range(items.count()):
            item = items.nth(i)
            name = item.locator(".inventory_item_name").inner_text()
            description = item.locator(".inventory_item_desc").inner_text()
            price = float(item.locator(".inventory_item_price").inner_text().replace("$", ""))
            add_to_cart_button = item.locator("button")
            inventory_list.append({
                "name": name,
                "description": description,
                "price": price,
                "add_to_cart_button": add_to_cart_button
            })
        return inventory_list

    def add_items_above_price(self, price_threshold: float):
        items = self.get_inventory_items()
        added_items = []
        for item in items:
            if item["price"] > price_threshold:
                item["add_to_cart_button"].click()
                added_items.append(item["name"])
        return added_items




