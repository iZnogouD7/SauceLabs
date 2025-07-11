
import time
import pytest

from Locators.alllocators import LoginPageLocators, CheckoutPageLocators
from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.LoginPage import LoginPage
from Pages.ProductPage import ProductPage
from Utils.FileReader import load_csv_data

@pytest.fixture()
def checkout_setup(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product=ProductPage(driver)
    product.click_on_cart_button()
    time.sleep(3)
    cart=CartPage(driver)
    cart.click_checkout_button()
    checkout_page = CheckoutPage(driver)
    return checkout_page

@pytest.mark.parametrize("firstname,lastname,zip_code,expected", load_csv_data("Data/checkout_data.csv"))
def test_checkout_validation(checkout_setup,firstname, lastname,zip_code,expected):
    assert checkout_setup.get_current_url()== CheckoutPageLocators.checkout_page_url
    checkout_setup.enter_checkout_info(firstname,lastname,zip_code)
    if "Success" in expected:
        assert checkout_setup.get_current_url() == "https://www.saucedemo.com/checkout-step-two.html",f"{checkout_setup.get_current_url()}"
        assert checkout_setup.checkout_title() == "Checkout: Overview",f"Got checkout title: {checkout_setup.checkout_title()}"
    elif "FirstNameNotGiven" in expected:
        print(f"FAILURE{firstname}{lastname}{zip_code}{checkout_setup.get_error()}")

        assert "Error: First Name is required" in checkout_setup.get_error(),f"Got error : {checkout_setup.get_error()}"
    elif "LastNameNotGiven" in expected:
        print(f"FAILURE{firstname}{lastname}{zip_code}{checkout_setup.get_error()}")

        assert "Error: Last Name is required" in checkout_setup.get_error(),f"Got error : {checkout_setup.get_error()}"
    elif "ZipCodeNotGiven" in expected:
        print(f"FAILURE{firstname}{lastname}{zip_code}{checkout_setup.get_error()}")

        assert "Error: Postal Code is required" in checkout_setup.get_error(), f"Got error : {checkout_setup.get_error()}"
    else:
        print("Other Errors Found")