from Locators.alllocators import CheckoutOverviewPageLocators, CheckoutPageLocators
from Pages.BasePage import BasePage


class CheckoutOverviewPage(BasePage):
    def click_finish_button(self):
        self.click_element(CheckoutOverviewPageLocators.finish_button_path)
    def click_cancel_button(self):
        self.click_element(CheckoutPageLocators.cancel_button_path)