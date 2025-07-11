import pytest

from Locators.alllocators import LoginPageLocators, CheckoutPageLocators, FinishPageLocators
from Pages.CartPage import CartPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutPage import CheckoutPage
from Pages.FinishPage import FinishPage
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage


@pytest.fixture()
def go_to_final_page(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product_page= ProductPage(driver)
    product_page.click_on_cart_button()
    cart_page = CartPage(driver)
    cart_page.click_checkout_button()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_info(CheckoutPageLocators.valid_first_name,CheckoutPageLocators.valid_last_name,CheckoutPageLocators.valid_zip_code)
    checkout_page.click_continue_button()
    checkout_over_page= CheckoutOverviewPage(driver)
    checkout_over_page.click_finish_button()
    finish_page = FinishPage(driver)
    return finish_page

def test_cart_count(go_to_final_page):
    finish=go_to_final_page
    assert finish.get_current_url()==FinishPageLocators.finish_page_url,f"Finish page url doesn't match. Needed url {finish.get_current_url()} but got {FinishPageLocators.finish_page_url}"
    assert "Checkout: Complete!" in finish.get_finish_title(),f"Finish page title doesn't match:{finish.get_finish_title()}"
    assert finish.get_final_cart_count() == 0,f"Cart has not been reset. Cart count should be 0 but got {finish.get_final_cart_count()}"

def test_thanks_message(go_to_final_page):
    finish=go_to_final_page
    assert finish.is_thank_you_displayed() == True,f"Thank you is not displayed:{finish.is_thank_you_displayed()}"

def test_back_home_button(go_to_final_page):
    finish=go_to_final_page
    finish.click_back_home()
    assert "inventory" in finish.get_current_url(),f"Inventory page url doesn't match:{finish.get_current_url()}"


