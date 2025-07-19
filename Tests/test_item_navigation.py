# New comprehensive test file: test_item_navigation.py
import pytest
import time
from Locators.alllocators import LoginPageLocators, ProductPageLocators
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Pages.CartPage import CartPage


@pytest.fixture()
def login_to_product_page(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product_page = ProductPage(driver)
    print("User logged in and on product page")
    return product_page


@pytest.fixture()
def setup_cart_with_items(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product_page = ProductPage(driver)

    # Add multiple items to cart
    product_page.add_single_item(ProductPageLocators.add_back_pack_path)
    product_page.add_single_item(ProductPageLocators.add_Jacket_path)
    product_page.click_on_cart_button()

    cart_page = CartPage(driver)
    print("Cart setup with items")
    return cart_page, product_page


def test_click_item_title_navigation(login_to_product_page):
    """Test clicking item title to navigate to detail page"""
    print("Testing item title click navigation")
    product_page = login_to_product_page

    # Get item details from inventory page
    item_name = "Sauce Labs Backpack"  # Adjust based on your actual item names
    inventory_details = product_page.get_item_details_from_inventory(item_name)

    # Click on item title
    product_page.click_item_by_name(item_name)
    time.sleep(2)

    # Verify navigation to detail page
    assert product_page.is_on_item_detail_page(), "Should be on item detail page"

    # Get details from detail page and verify they match
    detail_page_details = product_page.get_item_details_from_detail_page()
    assert product_page.verify_item_details_match(inventory_details, detail_page_details), \
        "Item details should match between inventory and detail pages"

    print("Item title navigation test passed")


def test_click_item_image_navigation(login_to_product_page):
    """Test clicking item image to navigate to detail page"""
    print("Testing item image click navigation")
    product_page = login_to_product_page

    item_name = "Sauce Labs Bike Light"  # Adjust based on your actual item names
    inventory_details = product_page.get_item_details_from_inventory(item_name)

    # Click on item image
    product_page.click_item_image_by_name(item_name)
    time.sleep(2)

    # Verify navigation and details match
    assert product_page.is_on_item_detail_page(), "Should be on item detail page"
    detail_page_details = product_page.get_item_details_from_detail_page()
    assert product_page.verify_item_details_match(inventory_details, detail_page_details), \
        "Item details should match between inventory and detail pages"

    print("Item image navigation test passed")


def test_add_remove_from_detail_page(login_to_product_page):
    """Test adding and removing items from detail page"""
    print("Testing add/remove from detail page")
    product_page = login_to_product_page

    # Navigate to item detail page
    item_name = "Sauce Labs Backpack"
    product_page.click_item_by_name(item_name)
    time.sleep(1)

    # Test adding item
    initial_cart_count = product_page.get_cart_count()
    product_page.add_item_from_detail_page()
    time.sleep(1)

    new_cart_count = product_page.get_cart_count()
    assert new_cart_count == initial_cart_count + 1, \
        f"Cart count should increase by 1. Expected: {initial_cart_count + 1}, Got: {new_cart_count}"

    # Test removing item
    product_page.remove_item_from_detail_page()
    time.sleep(1)

    final_cart_count = product_page.get_cart_count()
    assert final_cart_count == initial_cart_count, \
        f"Cart count should return to initial value. Expected: {initial_cart_count}, Got: {final_cart_count}"

    print("Add/remove from detail page test passed")


def test_back_to_products_navigation(login_to_product_page):
    """Test back to products button functionality"""
    print("Testing back to products navigation")
    product_page = login_to_product_page

    # Navigate to item detail page
    product_page.click_item_by_name("Sauce Labs Backpack")
    time.sleep(1)
    assert product_page.is_on_item_detail_page(), "Should be on item detail page"

    # Click back to products
    product_page.click_back_to_product()
    time.sleep(1)

    # Verify back on inventory page
    assert "inventory.html" in product_page.get_current_url(), \
        f"Should be back on inventory page. Current URL: {product_page.get_current_url()}"

    print("Back to products navigation test passed")


def test_cart_item_removal(setup_cart_with_items):
    """Test removing items from cart page"""
    print("Testing cart item removal")
    cart_page, product_page = setup_cart_with_items

    # Get initial cart items
    initial_cart_items = cart_page.get_cart_items()
    initial_count = len(initial_cart_items)
    assert initial_count > 0, "Cart should have items"

    # Remove one item
    item_to_remove = initial_cart_items[0]['name']
    cart_page.remove_item_by_name(item_to_remove)
    time.sleep(1)

    # Verify item was removed
    remaining_items = cart_page.get_cart_items()
    assert len(remaining_items) == initial_count - 1, \
        f"Cart should have one less item. Expected: {initial_count - 1}, Got: {len(remaining_items)}"

    # Verify specific item was removed
    remaining_names = [item['name'] for item in remaining_items]
    assert item_to_remove not in remaining_names, f"Item {item_to_remove} should be removed from cart"

    print("Cart item removal test passed")


def test_cart_item_title_navigation(setup_cart_with_items):
    """Test clicking item title in cart to navigate to detail page"""
    print("Testing cart item title navigation")
    cart_page, product_page = setup_cart_with_items

    # Get cart items
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "Cart should have items"

    # Click on first item title
    item_name = cart_items[0]['name']
    cart_details = cart_page.get_item_details_from_cart(item_name)

    cart_page.click_item_title_in_cart(item_name)
    time.sleep(2)

    # Verify navigation to detail page
    assert product_page.is_on_item_detail_page(), "Should navigate to item detail page"

    # Verify item details match
    detail_page_details = product_page.get_item_details_from_detail_page()
    assert cart_details['name'] == detail_page_details['name'], "Item names should match"
    assert cart_details['price'] == detail_page_details['price'], "Item prices should match"

    print("Cart item title navigation test passed")


def test_cart_item_image_navigation(setup_cart_with_items):
    """Test clicking item image in cart to navigate to detail page"""
    print("Testing cart item image navigation")
    cart_page, product_page = setup_cart_with_items

    # Get cart items
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "Cart should have items"

    # Click on first item image
    item_name = cart_items[0]['name']
    cart_page.click_item_image_in_cart(item_name)
    time.sleep(2)

    # Verify navigation to detail page
    assert product_page.is_on_item_detail_page(), "Should navigate to item detail page from cart image"

    print("Cart item image navigation test passed")


def test_remove_all_items_from_cart(setup_cart_with_items):
    """Test removing all items from cart"""
    print("Testing remove all items from cart")
    cart_page, product_page = setup_cart_with_items

    # Verify cart has items initially
    initial_items = cart_page.get_cart_items()
    assert len(initial_items) > 0, "Cart should have items initially"

    # Remove all items
    cart_page.remove_all_items_from_cart()
    time.sleep(2)

    # Verify cart is empty
    assert cart_page.verify_cart_is_empty(), "Cart should be empty after removing all items"
    assert cart_page.get_cart_count() == 0, "Cart count should be 0"

    print("Remove all items from cart test passed")


def test_comprehensive_item_journey(login_to_product_page):
    """Test complete user journey: inventory -> detail -> cart -> detail -> back"""
    print("Testing comprehensive item journey")
    product_page = login_to_product_page

    # Step 1: Click item from inventory page
    item_name = "Sauce Labs Backpack"
    inventory_details = product_page.get_item_details_from_inventory(item_name)
    product_page.click_item_by_name(item_name)
    time.sleep(1)

    # Step 2: Verify detail page and add to cart
    assert product_page.is_on_item_detail_page(), "Should be on detail page"
    detail_details = product_page.get_item_details_from_detail_page()
    assert product_page.verify_item_details_match(inventory_details, detail_details), "Details should match"

    product_page.add_item_from_detail_page()
    assert product_page.get_cart_count() == 1, "Cart should have 1 item"

    # Step 3: Go to cart and verify item
    product_page.click_on_cart_button()
    time.sleep(1)
    cart_page = CartPage
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) == 1, "Cart should have 1 item"
    assert cart_items[0]['name'] == item_name, "Cart item should match added item"

    # Step 4: Click item in cart to go back to detail page
    cart_page.click_item_title_in_cart(item_name)
    time.sleep(1)
    assert product_page.is_on_item_detail_page(), "Should be back on detail page"

    # Step 5: Remove item and go back to inventory
    product_page.remove_item_from_detail_page()
    assert product_page.get_cart_count() == 0, "Cart should be empty after removal"

    product_page.click_back_to_product()
    time.sleep(1)
    assert "inventory.html" in product_page.get_current_url(), "Should be back on inventory page"

    print("Comprehensive item journey test passed")

