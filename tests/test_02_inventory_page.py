from saucedemo_tests.conftest import login_test_params
from saucedemo_tests.pages.inventory_page import InventoryPage
from saucedemo_tests.utils.browser_utils import get_cart_count, sort_items
import pytest

USER_COST = 16

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_product_list_visibility(logged_in_page):
    product_list = logged_in_page.locator(".inventory_list")
    assert product_list.is_visible(), "Product list is not visible on the page"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_inventory_buttons(logged_in_page):
    page = logged_in_page
    inventory_page=InventoryPage(page=page)
    actual_inventory_list = inventory_page.get_inventory_items()
    for index, item in enumerate(actual_inventory_list):
        expected_locator = f"<Locator frame=<Frame name= url='https://www.saucedemo.com/inventory.html'> selector='.inventory_item >> nth={index} >> button'>"
        assert str(expected_locator) == str(item['add_to_cart_button'])

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_add_items_above_price(logged_in_page):
    page = logged_in_page
    initial_cart_count = get_cart_count(page=page)
    inventory_page=InventoryPage(page=page)
    added_items = inventory_page.add_items_above_price(USER_COST)
    final_cart_count = get_cart_count(page=page)
    assert final_cart_count == initial_cart_count + len(added_items), f"Cart count did not increase as expected. Initial: {initial_cart_count}, Final: {final_cart_count}"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_sorted_option_price_low_to_high(logged_in_page):
    sort_items(logged_in_page, "za")

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_sort_price_low_to_high(logged_in_page):
    sort_items(logged_in_page, "lohi")
    prices = logged_in_page.locator(".inventory_item_price").all_text_contents()
    prices = [float(price.strip("$")) for price in prices]
    assert prices == sorted(prices), "Items are not sorted by Price (low to high)"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_sort_price_high_to_low(logged_in_page):
    sort_items(logged_in_page, "hilo")  # Use "hilo" for Price (high to low)
    prices = logged_in_page.locator(".inventory_item_price").all_text_contents()
    prices = [float(price.strip("$")) for price in prices]
    assert prices == sorted(prices, reverse=True), "Items are not sorted by Price (high to low)"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_sort_name_a_to_z(logged_in_page):
    sort_items(logged_in_page, "az")  # Use "az" for Name (A to Z)
    items = logged_in_page.locator(".inventory_item_name").all_text_contents()
    assert items == sorted(items), "Items are not sorted by Name (A to Z)"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_sort_name_z_to_a(logged_in_page):
    sort_items(logged_in_page, "za")  # Use "za" for Name (Z to A)
    items = logged_in_page.locator(".inventory_item_name").all_text_contents()
    assert items == sorted(items, reverse=True), "Items are not sorted by Name (Z to A)"











