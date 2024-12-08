def get_cart_count(page):
    cart_icon_locator = page.locator('//*[@id="shopping_cart_container"]')
    cart_icon_locator.wait_for(state="visible")
    cart_count_text = cart_icon_locator.inner_text().strip()
    return int(cart_count_text) if cart_count_text else 0

def sort_items(page, sort_option: str):
    dropdown_xpath = '//*[@id="header_container"]/div[2]/div/span/select'
    page.select_option(dropdown_xpath, sort_option)
    page.wait_for_load_state("networkidle")




