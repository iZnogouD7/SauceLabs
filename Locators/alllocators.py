from selenium.webdriver.common.by import By
class LoginPageLocators:
    loginpageUrl="https://www.saucedemo.com/"
    valid_username="standard_user"
    valid_password="secret_sauce"

    username_field = (By.ID,"user-name")
    password_field = (By.ID,"password")
    login_button=(By.ID,"login-button")
    error_field_path = (By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

class ProductPageLocators:
    ProductPageUrl="https://www.saucedemo.com/inventory.html"
    title_path=(By.XPATH,'//*[@id="header_container"]/div[2]/span')
    inventory_count_path=(By.CLASS_NAME,'inventory_item')
    cart_count_path=(By.CLASS_NAME,'shopping_cart_badge')

    # menu_button_path=(By.ID,'react-burger-menu-btn')
    # all_item_path=(By.ID,'inventory_sidebar_link')
    # about_path=(By.ID,'about_sidebar_link')
    # logout_path=(By.ID,'logout_sidebar_link')
    # reset_app_state_path=(By.ID,'reset_sidebar_link')
    # menu_close_path=(By.ID,'react-burger-cross-btn')

    cart_button_path = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    select_filter_path=(By.CLASS_NAME, 'product_sort_container')
    all_item_name_class_path=(By.CLASS_NAME,'inventory_item_name')
    all_item_price_class_path=(By.CLASS_NAME,'inventory_item_price')
    all_item_img_class_path=(By.CLASS_NAME,'inventory_item_img')

    img_back_pack_path=(By.XPATH,'//*[@id="item_4_img_link"]/img')
    img_bike_light_path=(By.XPATH,'//*[@id="item_0_img_link"]/img')
    img_Tshirt_path=(By.XPATH,'//*[@id="item_1_img_link"]/img')
    img_Jacket_path=(By.XPATH,'//*[@id="item_5_img_link"]/img')
    img_onesie_path=(By.XPATH,'//*[@id="item_2_img_link"]/img')
    img_allthing_path=(By.XPATH,'//*[@id="item_3_img_link"]/img')

    title_back_pack_path=(By.XPATH,'//*[@id="item_4_title_link"]/div')
    title_bike_light_path=(By.XPATH,'//*[@id="item_0_title_link"]/div')
    title_Tshirt_path=(By.XPATH,'//*[@id="item_1_title_link"]/div')
    title_Jacket_path=(By.XPATH,'//*[@id="item_5_title_link"]/div')
    title_onesie_path=(By.XPATH,'//*[@id="item_2_title_link"]/div')
    title_allthing_path=(By.XPATH,'//*[@id="item_3_title_link"]/div')

    add_back_pack_path = (By.ID,'add-to-cart-sauce-labs-backpack')
    add_bike_light_path = (By.ID,'add-to-cart-sauce-labs-bike-light')
    add_Tshirt_path = (By.ID,'add-to-cart-sauce-labs-bolt-t-shirt')
    add_Jacket_path = (By.ID,'add-to-cart-sauce-labs-fleece-jacket')
    add_onesie_path=(By.ID,'add-to-cart-sauce-labs-onesie')
    add_allthings_path=(By.ID,'add-to-cart-test.allthethings()-t-shirt-(red)')

    remove_back_pack_path=(By.ID,'remove-sauce-labs-backpack')
    remove_bike_light_path=(By.ID,'remove-sauce-labs-bike-light')
    remove_Tshirt_path=(By.ID,'remove-sauce-labs-bolt-t-shirt')
    remove_Jacket_path=(By.ID,'remove-sauce-labs-fleece-jacket')
    remove_onesie_path=(By.ID,'remove-sauce-labs-onesie')
    remove_allthings_path=(By.ID,'remove-test.allthethings()-t-shirt-(red)')


    # twitter_path=(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    # facebook_path=(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[2]/a')
    # linkedin_path=(By.XPATH,'//*[@id="page_wrapper"]/footer/ul/li[3]/a')

    back_to_product = (By.ID, 'back-to-products')


class CartPageLocators:
    continue_shopping_path=(By.ID,'continue-shopping')
    checkout_path=(By.ID,'checkout')
    first_item_path=(By.XPATH,'// *[ @ id = "item_4_title_link"] / div')
    second_item_path=(By.XPATH,'//*[@id="item_0_title_link"]/div')
class CheckoutPageLocators:
    first_name_path=(By.ID,'first-name')
    last_name_path=(By.ID,'last-name')
    Zip_code_path=(By.ID,'postal-code')
    cancel_button_path=(By.ID,'cancel')
    continue_button_path=(By.ID,'continue')
    finish_button_path=(By.ID,'finish')

class OtherPageLocators:
    menu_button_path = (By.ID, 'react-burger-menu-btn')
    all_item_path = (By.ID, 'inventory_sidebar_link')
    about_path = (By.ID, 'about_sidebar_link')
    logout_path = (By.ID, 'logout_sidebar_link')
    reset_app_state_path = (By.ID, 'reset_sidebar_link')
    menu_close_path = (By.ID, 'react-burger-cross-btn')

    twitter_path = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[1]/a')
    facebook_path = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[2]/a')
    linkedin_path = (By.XPATH, '//*[@id="page_wrapper"]/footer/ul/li[3]/a')



