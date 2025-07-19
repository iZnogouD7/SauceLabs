
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Locators.alllocators import ProductPageLocators
from Pages.BasePage import BasePage


class ProductPage(BasePage):
    # def product_title(self):
    #     return self.find_element(ProductPageLocators.title_path)
    def get_page_title(self):
        return self.get_text_from_element(ProductPageLocators.title_path)


    def get_item_count(self):
        print(f"found {self.get_count(ProductPageLocators.inventory_count_path)} items in the product page")
        return self.get_count(ProductPageLocators.inventory_count_path)


    def add_single_item(self,locators):
        self.click_element(locators)
        print(f"added {locators}")
    def remove_single_item(self,locators):
        self.click_element(locators)
        print(f"added {locators}")
    def add_all_item(self):
        add_buttons=[ProductPageLocators.add_back_pack_path,
                     ProductPageLocators.add_bike_light_path,
                     ProductPageLocators.add_Tshirt_path,
                     ProductPageLocators.add_Jacket_path,
                     ProductPageLocators.add_onesie_path,
                     ProductPageLocators.add_allthings_path]
        for add_button in add_buttons:
            self.click_element(add_button)
        # self.click_element(ProductPageLocators.add_back_pack_path)
        # self.click_element(ProductPageLocators.add_Jacket_path)
        # self.click_element(ProductPageLocators.add_onesie_path)
        # self.click_element(ProductPageLocators.add_Tshirt_path)
        # self.click_element(ProductPageLocators.add_allthings_path)
        # self.click_element(ProductPageLocators.add_bike_light_path)
        print("Added all items")

    def remove_all_item(self):
        remove_button=[
            ProductPageLocators.remove_back_pack_path,
            ProductPageLocators.remove_bike_light_path,
            ProductPageLocators.remove_Tshirt_path,
            ProductPageLocators.remove_Jacket_path,
            ProductPageLocators.remove_onesie_path,
            ProductPageLocators.remove_allthings_path
        ]
        for remove_button in remove_button:
            self.click_element(remove_button)

        # self.click_element(ProductPageLocators.remove_back_pack_path)
        # self.click_element(ProductPageLocators.remove_Jacket_path)
        # self.click_element(ProductPageLocators.remove_onesie_path)
        # self.click_element(ProductPageLocators.remove_Tshirt_path)
        # self.click_element(ProductPageLocators.remove_allthings_path)
        # self.click_element(ProductPageLocators.remove_bike_light_path)
        print("All items removed")

    def click_on_cart_button(self):
        self.click_element(ProductPageLocators.cart_button_path)
        print("click on cart button")

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
            try:
                prices_list.append(float(price_text))
            except ValueError:
                prices_list.append(0.0)
        return prices_list

    def is_sorted_descending(self,list1) :
        sorted_copy=list1
        sorted_copy.sort(reverse=True)
        return list1==sorted_copy

    def is_sorted_ascending(self,list2) :
        sorted_copy = list2
        sorted_copy.sort()
        return list2 == sorted_copy

    def add_product_by_name(self,name):
        product_card=self.find_element(ProductPageLocators.product_card_by_name(name))


    def get_product_name(self):
        elements=self.find_element_by_class_name(ProductPageLocators.inventory_name_class_path)
        return [element.text for element in elements]
    def get_product_price(self):
        elements=self.find_element_by_class_name(ProductPageLocators.inventory_price_class_path)
        price=[]
        for element in elements:
            price_text=element.text.replace("$", "")
            price.append(float(price_text))
        return price
    def get_product_details(self,product_name):
        products=self.find_element_by_class_name(ProductPageLocators.inventory_desc_class_path)
        for product in products:
            name_element = product.find_element_by_class_name("inventory_item_name")
            if name_element == product_name:
                return {"name":name_element.text,
                    "description":product.find_element_by_class_name("inventory_item_description").text,
                    "price":product.find_element_by_class_name("inventory_item_price").text,
                    "image":product.find_element_by_class_name("inventory_item_image").get_attribute("src")
                }
        return None

    def click_item_by_name(self,item_name):
        item_title_locator = (By.XPATH, f'//div[@class="inventory-item-name" and text()="{item_name}"]')
        self.click_element(item_title_locator)
        print(f"clicked on item title:{item_name}")
    def click_item_image_by_name(self,item_name):
        item_image_locator = (By.XPATH, f'//img[contains(@alt,"{item_name}" or ancestor::div[contains(@class,"inventory-item")]//div[@class="inventory_item_name" and text()="{item_name}"]]')
        self.click_element(item_image_locator)
        print(f"clicked on item image:{item_name}")

    def get_item_details_from_inventory(self,item_name):
        item_container=self.find_element((By.XPATH,f"//div[@class='inventory-item-name' and text()='{item_name}']/ancestor::div[@class='inventory-item']"))
        details = {
            'name':item_container.find_element_by_class_name("inventory_item_name").text,
            'description':item_container.find_element_by_class_name("inventory_item_description").text,
            'price':item_container.find_element_by_class_name("inventory_item_price").text,
            'image':item_container.find_element_by_class_name("inventory_item_image").get_attribute("src")
        }
        return details
    def get_item_details_from_detail_page(self):
        details={
            'name':self.get_text_from_element(ProductPageLocators.inventory_name_class_path),
            'description':self.get_text_from_element(ProductPageLocators.inventory_desc_class_path),
            'price':self.get_text_from_element(ProductPageLocators.inventory_price_class_path),
            'image':self.find_element(ProductPageLocators.inventory_img_class_path).get_attribute("src")
        }
        return details
    def verify_item_details_match(self,inventory_details,detail_page_details):
        return (inventory_details['name'] == detail_page_details['name']
            and inventory_details['description'] == detail_page_details['description']
            and inventory_details['price'] == detail_page_details['price']
            and inventory_details['image'] == detail_page_details['image'])

    def is_on_item_detail_page(self):
        return "inventory-item" in self.get_current_url()

    def click_back_to_product(self):
        self.click_element(ProductPageLocators.back_to_product)

    def add_item_from_detail_page(self):
        self.click_element(ProductPageLocators.inventory_add_to_cart_button)
        print("added item from detail page")

    def remove_item_from_detail_page(self):
        self.click_element(ProductPageLocators.inventory_add_to_remove_button)
        print("removed item from detail page")

    def get_all_item_names_and_images(self):
        items = []
        item_containers = self.find_elements((By.CLASS_NAME, 'inventory-item'))
        for container in item_containers:
            name = container.find_element_by_class_name("inventory-item-name").text
            image = container.find_element_by_class_name("inventory-item-image").text
            # image=container.find_element(By.TAG_NAME,'img')
            items.append({'name': name, 'image_element': image})
        return items






