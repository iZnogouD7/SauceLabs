import pytest
import time

from Locators.alllocators import LoginPageLocators, ProductPageLocators
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage


@pytest.fixture()
def login_and_go_to_product_page(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product_page = ProductPage(driver)
    return product_page

def test_product_title(login_and_go_to_product_page):
    assert login_and_go_to_product_page.product_title().text == "Products"
    time.sleep(3)
def test_item_count(login_and_go_to_product_page):
    product_page = login_and_go_to_product_page
    assert product_page.get_item_count()==6,"Expected 6 items"
    time.sleep(3)

def test_add_all_items(login_and_go_to_product_page):
    product_page = login_and_go_to_product_page
    product_page.add_all_item()
    assert product_page.get_cart_count()== 6,"Expected 6 items"
    print("All Items added successfully")
    time.sleep(3)
    product_page.remove_all_item()
    assert product_page.get_cart_count() == 0, "Expected 0 items"
    print("All Items Removed successfully")
    time.sleep(3)
# def test_remove_all_items(login_and_go_to_product_page):
#     product_page = ProductPage(login_and_go_to_product_page)
#     product_page.remove_all_item()
#     assert product_page.get_cart_count() == 0,"Expected 0 items"
#     time.sleep(3)

def test_add_item_and_remove_item(login_and_go_to_product_page):
    product_page =login_and_go_to_product_page
    product_page.add_single_item(ProductPageLocators.add_back_pack_path)
    assert product_page.get_cart_count() == 1,"Expected 1 items in the cart counter"
    product_page.add_single_item(ProductPageLocators.add_Jacket_path)
    print("Item added successfully")
    assert product_page.get_cart_count() == 2,"Expected 2 items in the cart counter"
    time.sleep(3)
    print("Item added successfully")
    product_page.remove_single_item(ProductPageLocators.remove_back_pack_path)
    assert product_page.get_cart_count() == 1,"Expected 1 items in the cart counter"
    print("Item Removed successfully")
    product_page.remove_single_item(ProductPageLocators.remove_Jacket_path)
    assert product_page.get_cart_count() == 0,"Expected 0 items in the cart counter"
    print("Item Removed successfully")
    time.sleep(3)

def test_sorting(login_and_go_to_product_page):
    product_page = login_and_go_to_product_page
    product_page.select_filter_button("Name (Z to A)")
    item_name=product_page.get_all_items_names()
    result=product_page.is_sorted_des(item_name)
    assert result==True,"Item are not sorted"
    time.sleep(3)
    product_page.select_filter_button("Price (low to high)")
    item_price = product_page.get_all_items_price()
    result = product_page.is_sorted_asc(item_price)
    assert result == True, "Item are not sorted"
    time.sleep(3)
    product_page.select_filter_button("Price (high to low)")
    item_price = product_page.get_all_items_price()
    result = product_page.is_sorted_des(item_price)
    assert result == True, "Item are not sorted"
    time.sleep(3)
    product_page.select_filter_button("Name (A to Z)")
    item_name = product_page.get_all_items_names()
    result = product_page.is_sorted_asc(item_name)
    assert result == True, "Item are not sorted"
    time.sleep(3)


def test_add_to_cart_button(login_and_go_to_product_page):
    product_page = login_and_go_to_product_page
    product_page.click_on_cart_button()
    assert "cart" in product_page.get_current_url(),"Cart page not found"
    time.sleep(3)

