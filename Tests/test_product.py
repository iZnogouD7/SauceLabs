import pytest

from Locators.alllocators import LoginPageLocators, ProductPageLocators
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage


@pytest.fixture()
def login_and_go_to_product_page(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product_page = ProductPage(driver)
    return product_page

def test_product_page(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    assert product_page.product_title()=="Swag Labs","Product title Swag Labs is not displayed"

def test_item_count(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    assert product_page.get_item_count()==6,"Expected 6 items"

def test_add_all_items(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    product_page.add_all_item()
    assert product_page.get_cart_count()== 6,"Expected 6 items"

def test_remove_all_items(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    product_page.remove_all_item()
    assert product_page.get_cart_count() == 0,"Expected 0 items"

def test_add_item_and_remove_item(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    product_page.add_single_item(ProductPageLocators.add_back_pack_path)
    assert product_page.get_cart_count() == 1,"Expected 1 items in the cart counter"
    product_page.add_single_item(ProductPageLocators.add_Jacket_path)
    assert product_page.get_cart_count() == 2,"Expected 2 items in the cart counter"
    product_page.remove_single_item(ProductPageLocators.add_back_pack_path)
    assert product_page.get_cart_count() == 1,"Expected 1 items in the cart counter"
    product_page.remove_single_item(ProductPageLocators.add_Jacket_path)
    assert product_page.get_cart_count() == 0,

def test_sorting(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    product_page.select_filter_button("Name (Z to A)")

def test_add_to_cart_button(login_and_go_to_product_page):
    product_page = ProductPage(login_and_go_to_product_page)
    product_page.click_on_cart_button()
    assert product_page.,"Check out Page"