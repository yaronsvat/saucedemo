import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saucedemo_tests')))

from saucedemo_tests.pages.cart_page import CartPage
from saucedemo_tests.pages.inventory_page import InventoryPage
from utils.browser_utils import get_cart_count
import pytest
from conftest import login_test_params, logged_in_page

USER_COST = 16

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_view_cart_items(logged_in_page):
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': 29.99},
        {'name': 'Sauce Labs Fleece Jacket', 'price': 49.99}
    ]
    page = logged_in_page
    inventory_page=InventoryPage(page=page)
    inventory_page.add_items_above_price(USER_COST)
    cart_page=CartPage(page=page)
    cart_page.go_to_cart()
    added_items = cart_page.get_added_items()
    assert len(added_items) == len(expected_items), "Number of items in the cart does not match"
    for expected_item in expected_items:
        assert any(
            actual_item['name'] == expected_item['name'] and actual_item['price'] == expected_item['price']
            for actual_item in added_items
        ), f"Item {expected_item['name']} with price {expected_item['price']} not found in the cart"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_remove_from_cart_the_most_expensive(logged_in_page):
    page = logged_in_page
    inventory_page=InventoryPage(page=page)
    inventory_page.add_items_above_price(USER_COST)
    cart_page=CartPage(page=page)
    cart_page.go_to_cart()
    initial_cart_count = get_cart_count(page=page)
    cart_page.remove_most_expensive_item()
    final_cart_count = get_cart_count(page=page)
    assert final_cart_count == initial_cart_count - 1, f"Cart count did not decrease as expected. Initial: {initial_cart_count}, Final: {final_cart_count}"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_continue_shopping_and_add_the_cheapest_item(logged_in_page):
    page = logged_in_page
    inventory_page=InventoryPage(page=page)
    inventory_page.add_items_above_price(USER_COST)
    cart_page=CartPage(page=page)
    cart_page.go_to_cart()
    initial_cart_count = get_cart_count(page=page)
    cart_page.continue_shopping()
    cart_page.add_cheapest_item()
    final_cart_count = get_cart_count(page=page)
    assert final_cart_count == initial_cart_count + 1, f"Cart count did not decrease as expected. Initial: {initial_cart_count}, Final: {final_cart_count}"

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_checkout_button_visibility(logged_in_page):
    page = logged_in_page
    cart_page=CartPage(page=page)
    cart_page.go_to_cart()
    checkout_button = page.locator('.checkout_button')
    assert checkout_button.is_visible(), "Checkout button is not visible"
    checkout_button.click()
    expected_url = 'https://www.saucedemo.com/checkout-step-one.html'
    assert page.url == expected_url, f"User did not proceed to the checkout page. Expected URL: {expected_url}, but got: {page.url}"







