
from selenium.webdriver.support.ui import Select

from Locators.alllocators import ProductPageLocators
from Pages.BasePage import BasePage


class ProductPage(BasePage):
    def product_title(self):
        return self.find_element(ProductPageLocators.title_path)

    def get_item_count(self):
        return self.get_count(ProductPageLocators.inventory_count_path)


    def add_single_item(self,locators):
        self.click_element(locators)
    def remove_single_item(self,locators):
        self.click_element(locators)
    def add_all_item(self):
        self.click_element(ProductPageLocators.add_back_pack_path)
        self.click_element(ProductPageLocators.add_Jacket_path)
        self.click_element(ProductPageLocators.add_onesie_path)
        self.click_element(ProductPageLocators.add_Tshirt_path)
        self.click_element(ProductPageLocators.add_allthings_path)
        self.click_element(ProductPageLocators.add_bike_light_path)

    def remove_all_item(self):
        self.click_element(ProductPageLocators.remove_back_pack_path)
        self.click_element(ProductPageLocators.remove_Jacket_path)
        self.click_element(ProductPageLocators.remove_onesie_path)
        self.click_element(ProductPageLocators.remove_Tshirt_path)
        self.click_element(ProductPageLocators.remove_allthings_path)
        self.click_element(ProductPageLocators.remove_bike_light_path)

    def click_on_cart_button(self):
        self.click_element(ProductPageLocators.cart_button_path)

    def get_cart_count(self):
        return int(self.get_text_from_element(ProductPageLocators.cart_count_path))
        #return self.get_count(ProductPageLocators.cart_count_path)

    def select_filter_button(self,visible_text):
        dropdown=self.find_element(ProductPageLocators.select_filter_path)
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)

    def get_all_items_names(self):
        elements=self.find_elements(ProductPageLocators.all_item_name_class_path)
        items_list=[]
        for element in elements:
            items_list.append(element.text)
        return items_list

    def get_all_items_price(self):
        elements=self.find_elements(ProductPageLocators.all_item_price_class_path)
        prices_list=[]
        for element in elements:
            price_text = element.text.replace("$", "")
            prices_list.append(float(price_text))
        return prices_list

    def is_sorted_des(self,list1) :
        sorted_copy=list1
        sorted_copy.sort(reverse=True)
        return list1==sorted_copy

    def is_sorted_asc(self,list2) :
        sorted_copy = list2
        sorted_copy.sort()
        return list2 == sorted_copy

    def refresh_page(self):
        self.driver.refresh()






