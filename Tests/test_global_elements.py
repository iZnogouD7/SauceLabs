import pytest

from Locators.alllocators import LoginPageLocators, ProductPageLocators
from Pages.CartPage import CartPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.LoginPage import LoginPage
from Pages.OtherPage import OtherPage
from Pages.ProductPage import ProductPage


@pytest.mark.parametrize("page_url",["/inventory.html","/cart.html","/checkout-step-one.html","/checkout-step-two.html"])
def test_global_elements(driver,page_url):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username,LoginPageLocators.valid_password)
    driver.get(f"https://www.saucedemo.com{page_url}")
    other_page = OtherPage(driver)
    assert other_page.is_menu_sidebar_displayed(),"Menu Button Not Displayed"
    assert other_page.is_cart_button_displayed(),"Cart Button Not Displayed"
    assert other_page.is_footer_displayed(),"Footer Not Displayed"

def test_known_verification(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username,LoginPageLocators.valid_password)
    product_page = ProductPage(driver)
    product_page.add_single_item(ProductPageLocators.add_back_pack_path)
    expected={
        'name':'Sauce Labs Backpack',
        'desc': 'carry.allTheThings()',
        'price':29.99,
        'image':'backpack.jpg'
    }
    product_page.click_on_cart_button()
    cart_page = CartPage(driver)
    assert cart_page.get_i