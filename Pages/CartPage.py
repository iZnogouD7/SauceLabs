from Locators.alllocators import CartPageLocators, ProductPageLocators
from Pages.BasePage import BasePage


class CartPage(BasePage):
    def get_cart_page_url(self):
        return self.driver.current_url

    def cart_title(self):
        return self.find_element(CartPageLocators.cart_page_title).text

    def click_continue_button(self):
        self.click_element(CartPageLocators.continue_shopping_path)

    def click_checkout_button(self):
        self.click_element(CartPageLocators.checkout_path)

    def get_cart_count(self):
        try:
            return int(self.get_text_from_element(ProductPageLocators.cart_count_path))
        except:
            return 0

    def remove_item(self,locator):
        self.driver.find_element(locator).click()