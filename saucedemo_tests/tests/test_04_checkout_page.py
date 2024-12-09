import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saucedemo_tests')))

from saucedemo_tests.pages.checkout_page import CheckoutPage
from saucedemo_tests.pages.cart_page import CartPage
from saucedemo_tests.pages.inventory_page import InventoryPage
from utils.browser_utils import get_cart_count
from utils.conftest import logged_in_page, login_test_params
import pytest

USER_COST = 16

@pytest.mark.parametrize("logged_in_page", login_test_params, indirect=True)
def test_end2end_checkout_process(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page=page)
    initial_cart_count = get_cart_count(page=page)
    added_items = inventory_page.add_items_above_price(USER_COST)
    final_cart_count = get_cart_count(page=page)
    assert initial_cart_count + len(added_items) == final_cart_count, (
        f"Expected final cart count to be {initial_cart_count + len(added_items)}, "
        f"but got {final_cart_count}. "
        f"Initial count: {initial_cart_count}, Added items: {len(added_items)}"
    )
    cart_page=CartPage(page=page)
    cart_page.go_to_cart()
    checkout_page = CheckoutPage(page=page)
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("Lionel", "Messi", "66666")
    checkout_page.finish_checkout()
    final_cart_count = get_cart_count(page=page)
    assert final_cart_count == 0, f"Cart count should be 0 after checkout"

